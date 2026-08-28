#!/usr/bin/env python3
"""
build.py — assemble the site and the README from the canonical JSON in data/.

  data/wheel.json + data/native.json + data/navarasa.json
      -> index.html      (single self-contained page, no build tooling)
      -> README.md       (the same content as flat markdown tables)
      -> data/wheel.csv  (one row per word)

Run:  python3 scripts/build.py
"""

import csv
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA, SRC = ROOT / "data", ROOT / "src"

wheel = json.loads((DATA / "wheel.json").read_text(encoding="utf-8"))
native = json.loads((DATA / "native.json").read_text(encoding="utf-8"))
rasa = json.loads((DATA / "navarasa.json").read_text(encoding="utf-8"))

STATUS = {
    "direct": ("rala's own answer", "the dictionary's top hit is the word on the wheel"),
    "shaped": ("reshaped", "rala had it, but buried in technical noise or in the wrong register"),
    "gap": ("dictionary gap", "no usable entry; the word comes from Kannada usage"),
}
RINGS = ["core", "branch", "leaf"]


def walk():
    """Yield (ring_index, core_english, node) for all 130 nodes, wheel order."""
    for core in wheel:
        yield 0, core["en"], core
        for mid in core["kids"]:
            yield 1, core["en"], mid
            for leaf in mid["kids"]:
                yield 2, core["en"], leaf


def md(text):
    """The notes carry a little inline HTML; markdown wants its own."""
    text = re.sub(r"</?(?:i|em)>", "*", text or "")
    return text.replace("|", "\\|")


# ---------------------------------------------------------------- index.html
def build_html():
    head = (SRC / "head.html").read_text(encoding="utf-8")
    body = (SRC / "body.html").read_text(encoding="utf-8")
    app = (SRC / "app.js").read_text(encoding="utf-8")
    payload = "\n".join(
        f"const {name} = {json.dumps(obj, ensure_ascii=False, separators=(',', ':'))};"
        for name, obj in (("WHEEL", wheel), ("NATIVE", native), ("RASA", rasa))
    )
    doc = f"""<!doctype html>
<html lang="kn">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="A feeling wheel in Kannada. 130 words taken through the rala English-Kannada dictionary and then argued with.">
<meta property="og:title" content="ಭಾವಚಕ್ರ">
<meta property="og:description" content="A feeling wheel in Kannada, built from the rala dictionary API.">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='15' fill='%23A9790F'/%3E%3Ccircle cx='16' cy='16' r='7' fill='%23E6E9E2'/%3E%3C/svg%3E">
{head}
</head>
<body>
{body}
<script>
{payload}

{app}
</script>
</body>
</html>
"""
    (ROOT / "index.html").write_text(doc, encoding="utf-8")
    return len(doc)


# ----------------------------------------------------------------- wheel.csv
def build_csv():
    with (DATA / "wheel.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ring", "sector_en", "english", "kannada", "transliteration",
                    "status", "rala_hits", "note"])
        for ring, sector, n in walk():
            w.writerow([RINGS[ring], sector, n["en"], n["kn"], n["tr"], n["status"],
                        " ; ".join(n.get("rala") or []),
                        re.sub(r"</?(?:i|em)>", "", n.get("note", ""))])


# ----------------------------------------------------------------- README.md
def build_readme():
    counts = {}
    for _, _, n in walk():
        counts[n["status"]] = counts.get(n["status"], 0) + 1
    total = sum(counts.values())

    L = []
    add = L.append
    add("# ಭಾವಚಕ್ರ · a feeling wheel in Kannada\n")
    add("**[Open the wheel →](https://pvnkmrksk.github.io/bhavachakra/)**\n")
    add("The English feeling wheel, taken through a Kannada dictionary and then argued with. "
        f"Each of the {total} Kannada words on it came out of "
        "[**rala**](https://pvnkmrksk.github.io/rala/) — 478,680 English→Kannada entries, "
        "reversed from [Alar](https://alar.ink) and Padakanaja — and was then kept, reshaped, "
        "or thrown out and replaced with what a Kannada speaker would actually say.\n")
    add("Everything is in flat JSON and CSV under [`data/`](data/) if you want the words "
        "without the page.\n")

    add("## The lookup\n")
    add("```\nGET https://rala-search.rala-search.workers.dev/?q=<english word>\n\n"
        "{ \"query\": str,\n  \"count\": int,\n"
        "  \"results\": [ { \"kannada\", \"definition\", \"type\", \"source\" } ] }\n```\n")
    add("Calls were made one at a time with 0.35 s between them, and without the "
        "`X-Rala-Intent: primary` header, so none of this landed in rala's own search "
        "analytics. [alar.ink](https://alar.ink) itself was never queried — Alar reaches "
        "this wheel only through rala's reversal of it.\n")
    add("rala matches whole words against definition text, so a query only finds the exact "
        "form the dictionary happens to use: `annoyed` returns nothing, `annoy` returns "
        "thirteen entries. [`scripts/rala.py`](scripts/rala.py) works around this with a "
        "morphological expander that strips `-ness`, `-ly`, `-ed`, `-ing`, `-ful`, `-ity` "
        "and friends, and retries. Of the 52 words that first came back empty, morphology "
        "alone recovered 38. The last 14 needed hand-picked synonyms — `repelled → repulse`, "
        "`boredom → tedium`, `skeptical → sceptic` — which is the part a dictionary API "
        "cannot do for you, and the part a thesaurus layer would fix.\n")

    add("## What came back\n")
    add("| | count | meaning |\n|---|---:|---|")
    for k in ("direct", "shaped", "gap"):
        label, desc = STATUS[k]
        add(f"| `{k}` | {counts.get(k, 0)} | **{label}** — {desc} |")
    add(f"| | **{total}** | |\n")

    add("Where rala is excellent: fear, anger and grief. Seven graded fear words "
        "(ಅಂಜಿಕೆ, ಹೆದರಿಕೆ, ದಿಗಿಲು, ಗಾಬರಿ, ಆತಂಕ, ಭೀತಿ, ಭಯ), four for doubt, and ತೇಜೋವಧೆ — "
        "\"the murder of someone's lustre\" — for *humiliate*.\n")
    add("Where it falls down, it falls down structurally: rala's bulk is Padakanaja, which "
        "is administrative, legal, scientific and agricultural. So —\n")
    add("| query | what rala returned |\n|---|---|")
    for q, r in [("stressed", "ಪ್ರತಿಬಲ — tensile stress, shear stress (materials engineering)"),
                 ("confused", "ತುಕ್ಕುಗೆಂಪು — the confused flour beetle"),
                 ("let down", "ಹಾಲೊಸರಿಕೆ — milk let-down, the dairy term"),
                 ("loving", "ನೆರಳು ಪ್ರಿಯ — shade-loving, of plants"),
                 ("depressed", "ದಲಿತ, ಶೋಷಿತ — from the colonial phrase \"depressed classes\""),
                 ("accepted", "ಅಂಗೀಕೃತ ಟೆಂಡರ್ — accepted tender"),
                 ("tired", "ದಣಿದ ಮಣ್ಣು — tired soil"),
                 ("critical", "ಕ್ರಾಂತಿಕೋನ — critical angle"),
                 ("proud / inspired / boredom / threatened", "nothing at all")]:
        add(f"| `{q}` | {r} |")
    add("")

    add("## The wheel\n")
    add("Seven core feelings, each with branches and leaves. `status` is defined in the "
        "table above; **rala's hits** are the dictionary candidates that were actually "
        "considered, trimmed to the short ones.\n")
    for core in wheel:
        add(f"### {core['kn']} · {core['en']} — *{core['tr']}*\n")
        add("| ring | English | ಕನ್ನಡ | roman | status | rala's hits |")
        add("|---|---|---|---|---|---|")
        rows = [(0, core)] + [(1, m) for m in core["kids"]]
        ordered = [(0, core)]
        for m in core["kids"]:
            ordered.append((1, m))
            ordered += [(2, l) for l in m["kids"]]
        for ring, n in ordered:
            hits = ", ".join(md(h) for h in (n.get("rala") or [])) or "—"
            add(f"| {RINGS[ring]} | {n['en']} | **{n['kn']}** | *{n['tr']}* | `{n['status']}` | {hits} |")
        add("")
        notes = [(r, n) for r, n in ordered if n.get("note")]
        if notes:
            add("<details><summary>Reading — why these words and not the dictionary's</summary>\n")
            for _, n in notes:
                add(f"- **{n['kn']}** *({n['en']})* — {md(n['note'])}")
            add("\n</details>\n")

    add("## ಕನ್ನಡದ್ದೇ ಪದಗಳು — words with nowhere to sit on the wheel\n")
    add("Feelings Kannada names precisely and English can only paraphrase. The wheel is an "
        "English object; these are the argument for redrawing one rather than translating it.\n")
    add("| ಕನ್ನಡ | roman | what it means |\n|---|---|---|")
    for w in native:
        add(f"| **{w['kn']}** | *{w['tr']}* | {md(w['gloss'])} |")
    add("")

    add("## ನವರಸ — the older map, laid over the wheel\n")
    add("| ರಸ | roman | flavour | where it lands on the wheel |\n|---|---|---|---|")
    for r in rasa:
        add(f"| **{r['kn']}** | *{r['tr']}* | {r['en']} | {md(r['map'])} |")
    add("")

    add("## Files\n")
    add("| path | what's in it |\n|---|---|")
    add("| [`index.html`](index.html) | the whole site — one file, no build step, no runtime dependencies |")
    add("| [`data/wheel.json`](data/wheel.json) | canonical. 7 core objects, each with `kids` (branches), each with `kids` (leaves). Every node has `en`, `kn`, `tr`, `status`, `rala[]`, and often `note`. |")
    add("| [`data/wheel.csv`](data/wheel.csv) | the same 130 words flattened — `ring, sector_en, english, kannada, transliteration, status, rala_hits, note` |")
    add("| [`data/native.json`](data/native.json) | the untranslatable list — `kn`, `tr`, `gloss` |")
    add("| [`data/navarasa.json`](data/navarasa.json) | the nine rasas — `kn`, `tr`, `en`, `map` |")
    add("| [`data/rala-responses.json`](data/rala-responses.json) | raw API responses, keyed by query. Provenance for every claim above. |")
    add("| [`scripts/rala.py`](scripts/rala.py) | rala client + the morphological expander |")
    add("| [`scripts/build.py`](scripts/build.py) | regenerates `index.html`, this README and `wheel.csv` from `data/` |")
    add("| [`src/`](src/) | the page's parts — markup, styles, and the SVG wheel renderer |")
    add("")
    add("```bash\npython3 scripts/build.py      # rebuild the site and this README\n"
        "python3 scripts/rala.py loneliness annoyed   # try the expander\n```\n")

    add("## Attribution\n")
    add("- Word data from [**rala**](https://github.com/pvnkmrksk/rala), a reversal of "
        "[**Alar**](https://alar.ink) by V. Krishna, licensed "
        "[ODC-ODbL](https://opendatacommons.org/licenses/odbl/), combined with "
        "[Padakanaja](https://padakanaja.karnataka.gov.in/dictionary), Government of Karnataka.\n"
        "- Wheel structure after Gloria Willcox's Feeling Wheel (1982) and its widely "
        "circulated three-ring descendant. The Kannada here is a reinterpretation, not a "
        "translation of it.\n"
        "- Derived data in `data/` is offered under ODbL, matching Alar. The page and code "
        "are MIT.\n")
    (ROOT / "README.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    return len("\n".join(L))


if __name__ == "__main__":
    h = build_html()
    build_csv()
    r = build_readme()
    print(f"index.html {h:,} bytes · README.md {r:,} bytes · data/wheel.csv written")

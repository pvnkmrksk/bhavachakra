#!/usr/bin/env python3
"""
build.py — assemble the site and the README from data/wheels/*.json.

  data/wheels/{bhava,odalu,rasa}.json
      -> index.html       three wheels behind one slider, no build step at serve time
      -> README.md        every word as flat markdown, plus the dictionary evidence
      -> data/words.csv   one row per word across all three wheels

The site is for reading the words. The README is the extended cut: it carries
the rala lookups, the misfires and the counts, which are diagnostics and do not
belong on the page.

Run:  python3 scripts/build.py
"""

import csv
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA, SRC = ROOT / "data", ROOT / "src"
RINGS = ["core", "branch", "leaf"]

load = lambda n: json.loads((DATA / "wheels" / f"{n}.json").read_text(encoding="utf-8"))

WHEELS = [
 {"id": "bhava", "file": "bhava",
  "name": "ಭಾವಚಕ್ರ", "hubKn": "ಭಾವಚಕ್ರ", "hubRom": "bhāva-cakra",
  "hint": "Hover or tap any segment — the panel names it in both scripts. Tap a "
          "sector to zoom into it, and again to go back out.",
  "blurb": "The English feeling wheel, taken through a Kannada dictionary and then argued "
           "with. Seven core feelings, three rings, 130 words. Where the dictionary was "
           "right it was kept; where it answered in the register of a government circular "
           "it was replaced with what a Kannada speaker would actually say — "
           "<em>ನೆಮ್ಮದಿ</em> and not ಶಾಂತಿ, <em>ಹೊಟ್ಟೆಕಿಚ್ಚು</em> and not ಅಸೂಯೆ.",
  "aboutTitle": "ಎರವಲಿನ ಆಕಾರ", "aboutLat": "a borrowed shape",
  "about": "This wheel's structure is not Kannada. It is Gloria Willcox's Feeling Wheel and "
           "its widely circulated three-ring descendant, which is an English object with "
           "English assumptions — seven cores, a slot called <em>Bad</em>, a distinction "
           "between <em>guilty</em> and <em>ashamed</em>. Filling it in Kannada is worth "
           "doing precisely because the seams show, and the seams are the interesting part.",
  "cards": [
    {"h": "Where it fits badly",
     "p": "There is no Kannada feeling called <em>ಕೆಟ್ಟ</em>. But everything the English wheel "
          "files under <em>Bad</em> — bored, busy, stressed, tired — is one Kannada word, "
          "ಬೇಸರ. English needs four words to circle what Kannada says in one."},
    {"h": "Words with no slot",
     "p": "ಒಪ್ಪಿಗೆ and ತಿರಸ್ಕಾರ describe what somebody did to you; Kannada gives no noun for "
          "the receiving end. ದುರ್ಬಲತೆ is the only word available for <em>vulnerable</em>, "
          "and it is an insult. Neither gap is a failure of the language — they are places "
          "the English wheel assumed something Kannada does not."},
    {"h": "Register, not correctness",
     "p": "Almost every change made here was a register change rather than a correction. "
          "ಅಸೂಯೆ, ರೋಷ, ವಿಸ್ಮಯ and ಆಶಾವಾದ are all correct. They are also words nobody says at "
          "home, so the wheel uses ಹೊಟ್ಟೆಕಿಚ್ಚು, ರೊಚ್ಚು, ದಂಗು and ಭರವಸೆ instead."},
    {"h": "The evidence",
     "p": "Every word here was looked up in rala first, and the full record — what the "
          "dictionary returned, what was kept, what was overruled and why — is in the "
          "<a href='https://github.com/pvnkmrksk/bhavachakra#readme'>README</a>. It is "
          "diagnostics, and it belongs there rather than here."}]},

 {"id": "odalu", "file": "odalu",
  "name": "ಒಡಲ ಚಕ್ರ", "hubKn": "ಒಡಲು", "hubRom": "oḍalu · the body as vessel",
  "hint": "Hover or tap any segment. The centre is where in the body it happens, the middle "
          "ring is the feeling, and the outer ring is what Kannada actually says.",
  "blurb": "Not a translation of anything. Kannada mostly names a feeling by saying "
           "<em>where in the body it is happening</em> — ಹೊಟ್ಟೆಕಿಚ್ಚು, belly-fire; ಎದೆಗುಂದು, "
           "the chest sinks; ಕರುಳು ಚುರುಕ್, the gut stings. So the seven seats are the centre, "
           "the feelings you would actually name are the middle ring, and the phrases people "
           "say are the outer one.",
  "aboutTitle": "ಒಡಲು", "aboutLat": "the body as the vessel of feeling",
  "about": "ಒಡಲು is an old word for the body considered as a container — the thing feeling "
           "happens inside. English builds compounds like this too (heartbroken, gutted, "
           "hot-headed) but treats them as figurative colour on top of a real vocabulary. "
           "In Kannada they <em>are</em> the vocabulary, and they are not heard as metaphor: "
           "ಹೊಟ್ಟೆ ತೊಳಸು covers moral revulsion and actual nausea with nothing between the "
           "two senses.",
  "cards": [
    {"h": "Navigate by the feeling, not the organ",
     "p": "The seat is the grouping, but the ring you actually read is the middle one, and "
          "it holds ordinary feeling-names: ಧೈರ್ಯ, ಹೆಮ್ಮೆ, ಚಿಂತೆ, ಮುನಿಸು, ನೆಮ್ಮದಿ. The body "
          "explains why those particular feelings sit together."},
    {"h": "What it holds that the first wheel could not",
     "p": "ಮುನಿಸು, the sulk you are only entitled to with someone who loves you. ಸಲಿಗೆ, the "
          "earned licence to be informal. ಕರುಳ ಬಳ್ಳಿ, the gut-vine. ಎದೆ ಝಲ್, the single cold "
          "jolt. None of them had an English slot to sit in."},
    {"h": "ಕರುಳು is the strange one",
     "p": "In Kannada the gut is the organ of kinship — your child is your ಕರುಳ ಬಳ್ಳಿ — so "
          "every feeling sited there is about your own people. ಕರುಳು ಕಿತ್ತು ಬರು is kept for "
          "the death of a child or a parent, and using it lightly would be shocking."},
    {"h": "What it misses",
     "p": "Feelings with no bodily seat fall off: ಅಭಿಮಾನ, ಹಂಬಲ, ಕೃತಜ್ಞತೆ, ಸಂಭ್ರಮ. Catching "
          "those needs a second axis — probably direction, since ವಾತ್ಸಲ್ಯ only ever flows "
          "downward, ಗೌರವ upward and ಸಲಿಗೆ sideways."}]},

 {"id": "rasa", "file": "rasa",
  "name": "ರಸಚಕ್ರ", "hubKn": "ನವರಸ", "hubRom": "nava-rasa · the nine flavours",
  "hint": "Hover or tap any segment. The nine rasas are the centre; underneath each one are "
          "the words Kannada actually uses for that flavour.",
  "blurb": "The oldest map of feeling this language has, opened out. The nine rasas are an "
           "aesthetic theory — what an audience can be made to feel — and a thousand years "
           "of Kannada poetry is organised by them. Here each rasa keeps its Sanskrit name, "
           "because that is what everyone calls it, and everything beneath it is the daily "
           "word: ಸಿಟ್ಟು under ರೌದ್ರ, ಬೆರಗು under ಅದ್ಭುತ, ಬೇಸರ under ಬೀಭತ್ಸ.",
  "aboutTitle": "ನವರಸ", "aboutLat": "nine flavours, not nine emotions",
  "about": "A rasa is not an emotion. It is the flavour an audience tastes — which is why "
           "each has a ಸ್ಥಾಯಿಭಾವ, a durable underlying feeling, listed separately in the "
           "panel: ಶೃಂಗಾರ is the flavour, ರತಿ is the feeling. That distinction has no "
           "equivalent in any Western emotion wheel, and it is the reason this map can hold "
           "ವೀರ and ಹಾಸ್ಯ, which the other two cannot.",
  "cards": [
    {"h": "Sanskrit at the centre, Kannada everywhere else",
     "p": "The nine names are Sanskrit and stay Sanskrit: ಶೃಂಗಾರ, ಹಾಸ್ಯ, ಕರುಣ, ರೌದ್ರ, ವೀರ, "
          "ಭಯಾನಕ, ಬೀಭತ್ಸ, ಅದ್ಭುತ, ಶಾಂತ. Every Kannada speaker who has watched a dance "
          "recital knows them. Underneath, the words are ordinary: ರೊಚ್ಚು, ಗಾಬರಿ, ಹೊಟ್ಟೆ "
          "ತೊಳಸು, ಗತ್ತು, ದಂಗು, ಸೇಡು."},
    {"h": "The two the other wheels lose",
     "p": "ವೀರ, the heroic, and ಶೃಂಗಾರ, the erotic. No English feeling wheel has a slot for "
          "either. ವೀರ's underlying feeling is not courage but ಉತ್ಸಾಹ, energy — which "
          "quietly claims heroism is a kind of enthusiasm."},
    {"h": "ಶಾಂತ, the one they argued about",
     "p": "The ninth rasa was added late and disputed for centuries: can the absence of "
          "agitation be a flavour at all? The English wheel files peace under happiness. The "
          "rasa tradition insists it is a state of its own, and gives it ಶಮ — quiet — as its "
          "durable feeling."},
    {"h": "The colours are not decoration",
     "p": "The Nāṭyaśāstra assigns each rasa a colour, and this wheel follows them: ಶೃಂಗಾರ "
          "śyāma green, ರೌದ್ರ red, ವೀರ wheaten gold, ಭಯಾನಕ black, ಬೀಭತ್ಸ blue, ಅದ್ಭುತ yellow, "
          "ಕರುಣ dove grey, ಹಾಸ್ಯ and ಶಾಂತ white — the last three shifted just far enough to "
          "stay legible on both a light and a dark ground."}]},
]

for w in WHEELS:
    w["data"] = load(w["file"])


def walk(data):
    for core in data:
        yield 0, core["kn"], core
        for mid in core["kids"]:
            yield 1, core["kn"], mid
            for leaf in mid["kids"]:
                yield 2, core["kn"], leaf


def md(t):
    return re.sub(r"</?(?:i|em)>", "*", t or "").replace("|", "\\|")


# ---------------------------------------------------------------- index.html
def build_html():
    head = (SRC / "head.html").read_text(encoding="utf-8")
    body = (SRC / "body.html").read_text(encoding="utf-8")
    js = (SRC / "wheel.js").read_text(encoding="utf-8") + "\n" + (SRC / "app.js").read_text(encoding="utf-8")
    payload = "const WHEELS = " + json.dumps(
        [{k: v for k, v in w.items() if k != "file"} for w in WHEELS],
        ensure_ascii=False, separators=(",", ":")) + ";"
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Three emotion wheels in Kannada: one translated from the English feeling wheel, one built from the body, one from the nine rasas.">
<meta property="og:title" content="ಭಾವಚಕ್ರ">
<meta property="og:description" content="Three emotion wheels in Kannada — from English, from the body, from the nine rasas.">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='15' fill='%239C6E0C'/%3E%3Ccircle cx='16' cy='16' r='7' fill='%23E6E9E2'/%3E%3C/svg%3E">
{head}
</head>
<body>
{body}
<script>
{payload}

{js}
</script>
</body>
</html>
"""
    (ROOT / "index.html").write_text(doc, encoding="utf-8")
    return len(doc)


# ----------------------------------------------------------------- words.csv
def build_csv():
    with (DATA / "words.csv").open("w", newline="", encoding="utf-8") as f:
        c = csv.writer(f)
        c.writerow(["wheel", "ring", "sector", "kannada", "transliteration", "english",
                    "literal", "english_source", "status", "rala_hits", "note"])
        for w in WHEELS:
            for ring, sector, n in walk(w["data"]):
                c.writerow([w["id"], RINGS[ring], sector, n["kn"], n["tr"], n["en"],
                            n.get("lit", ""),
                            n.get("en", "") if w["id"] == "bhava" else "",
                            n.get("status", ""), " ; ".join(n.get("rala") or []),
                            re.sub(r"</?(?:i|em)>", "", n.get("note", ""))])


# ----------------------------------------------------------------- README.md
def build_readme():
    L = []
    add = L.append
    total = sum(len(list(walk(w["data"]))) for w in WHEELS)
    add("# ಭಾವಚಕ್ರ · three feeling wheels in Kannada\n")
    add("**[Open the wheels →](https://pvnkmrksk.github.io/bhavachakra/)**\n")
    add(f"{total} words across three maps of the same territory:\n")
    add("| wheel | built from | words |\n|---|---|---:|")
    src = {"bhava": "the English feeling wheel, translated and then argued with",
           "odalu": "the part of the body Kannada sites each feeling in",
           "rasa": "the nine rasas of the Nāṭyaśāstra, opened out into daily Kannada"}
    for w in WHEELS:
        add(f"| **{w['name']}** *{w['id']}* | {src[w['id']]} | {len(list(walk(w['data'])))} |")
    add("\nThe site is for reading the words. This README is the extended cut: it carries the "
        "dictionary evidence, the misfires and the counts, which are diagnostics.\n")

    add("## The lookup\n")
    add("```\nGET https://rala-search.rala-search.workers.dev/?q=<english word>\n\n"
        "{ \"query\": str,\n  \"count\": int,\n"
        "  \"results\": [ { \"kannada\", \"definition\", \"type\", \"source\" } ] }\n```\n")
    add("Calls were made one at a time with 0.35 s between them and without the "
        "`X-Rala-Intent: primary` header, so none of this reached rala's own search "
        "analytics. [alar.ink](https://alar.ink) was never queried — Alar arrives here only "
        "through rala's reversal of it.\n")
    add("rala matches whole words against definition text, so a query only finds the exact "
        "form the dictionary happens to use: `annoyed` returns nothing, `annoy` returns "
        "thirteen entries. [`scripts/rala.py`](scripts/rala.py) fixes this client-side with a "
        "morphological expander — 26 suffix rules, longest first, doubled-consonant undo, and "
        "one level of recursion so `playfully → playful → play`.\n")
    add("```\nloneliness  → loneliness, lonely, lone\n"
        "frustrated  → frustrated, frustrat, frustrate\n"
        "victimised  → victimised, victimise, victimize\n"
        "stopped     → stopped, stopp, stoppe, stop\n```\n")
    add("Of the 52 words that first came back empty, morphology alone recovered 38. The last "
        "14 needed hand-picked synonyms — `repelled → repulse`, `boredom → tedium`, "
        "`skeptical → sceptic` — which is the part stemming cannot reach, and the argument "
        "for a thesaurus layer inside the worker rather than in every client.\n")

    counts = {}
    for _, _, n in walk(WHEELS[0]["data"]):
        if n.get("status"):
            counts[n["status"]] = counts.get(n["status"], 0) + 1
    add("## What rala returned, for ಭಾವಚಕ್ರ\n")
    add("| | count | meaning |\n|---|---:|---|")
    for k, label in [("direct", "the dictionary's top hit is the word on the wheel"),
                     ("shaped", "rala had it, but buried in technical noise or in the wrong register"),
                     ("gap", "no usable entry; the word comes from Kannada usage")]:
        add(f"| `{k}` | {counts.get(k,0)} | {label} |")
    add(f"| | **{sum(counts.values())}** | |\n")
    add("Where rala is excellent: fear, anger and grief. Seven graded fear words, four for "
        "doubt, and ತೇಜೋವಧೆ — \"the murder of someone's lustre\" — for *humiliate*.\n")
    add("Where it falls down it falls down structurally, because rala's bulk is Padakanaja, "
        "which is administrative, legal, scientific and agricultural:\n")
    add("| query | what rala returned |\n|---|---|")
    for q, r in [("stressed", "ಪ್ರತಿಬಲ — tensile stress, shear stress"),
                 ("confused", "ತುಕ್ಕುಗೆಂಪು — the confused flour beetle"),
                 ("let down", "ಹಾಲೊಸರಿಕೆ — milk let-down, the dairy term"),
                 ("loving", "ನೆರಳು ಪ್ರಿಯ — shade-loving, of plants"),
                 ("depressed", "ದಲಿತ, ಶೋಷಿತ — from the phrase \"depressed classes\""),
                 ("accepted", "ಅಂಗೀಕೃತ ಟೆಂಡರ್ — accepted tender"),
                 ("tired", "ದಣಿದ ಮಣ್ಣು — tired soil"),
                 ("critical", "ಕ್ರಾಂತಿಕೋನ — critical angle"),
                 ("proud / inspired / boredom / threatened", "nothing at all")]:
        add(f"| `{q}` | {r} |")
    add("")

    for w in WHEELS:
        add(f"## {w['name']} — {src[w['id']]}\n")
        for core in w["data"]:
            head_bits = [f"### {core['kn']} · {core['en']} — *{core['tr']}*"]
            if core.get("sthayi"):
                head_bits.append(f"ಸ್ಥಾಯಿಭಾವ · {core['sthayi']}")
            add("  \n".join(head_bits) + "\n")
            cols = "| ring | ಕನ್ನಡ | roman | meaning |"
            sep = "|---|---|---|---|"
            if w["id"] == "bhava":
                cols = "| ring | ಕನ್ನಡ | roman | English slot | status | rala's hits |"
                sep = "|---|---|---|---|---|---|"
            add(cols); add(sep)
            ordered = [(0, core)]
            for m in core["kids"]:
                ordered.append((1, m))
                ordered += [(2, l) for l in m["kids"]]
            for ring, n in ordered:
                if w["id"] == "bhava":
                    hits = ", ".join(md(h) for h in (n.get("rala") or [])) or "—"
                    add(f"| {RINGS[ring]} | **{n['kn']}** | *{n['tr']}* | {n['en']} | "
                        f"`{n.get('status','')}` | {hits} |")
                else:
                    m = n["en"] + (f" — literally, {n['lit']}" if n.get("lit") else "")
                    add(f"| {RINGS[ring]} | **{n['kn']}** | *{n['tr']}* | {md(m)} |")
            add("")
            notes = [n for _, n in ordered if n.get("note")]
            if notes:
                add("<details><summary>Reading</summary>\n")
                for n in notes:
                    add(f"- **{n['kn']}** *({n['en']})* — {md(n['note'])}")
                add("\n</details>\n")

    native = json.loads((DATA / "native.json").read_text(encoding="utf-8"))
    add("## Appendix — words with nowhere to sit\n")
    add("Feelings Kannada names precisely and English can only paraphrase. Most of these now "
        "live inside ಒಡಲ ಚಕ್ರ or ರಸಚಕ್ರ; they are listed together here because the list is the "
        "argument for redrawing a wheel rather than translating one.\n")
    add("| ಕನ್ನಡ | roman | what it means |\n|---|---|---|")
    for x in native:
        add(f"| **{x['kn']}** | *{x['tr']}* | {md(x['gloss'])} |")
    add("")

    add("## Files\n")
    add("| path | what's in it |\n|---|---|")
    add("| [`index.html`](index.html) | the whole site — one file, three wheels, no runtime dependencies |")
    add("| [`data/wheels/bhava.json`](data/wheels/bhava.json) | wheel one. Every node has `kn`, `tr`, `en`, `status`, `rala[]` and usually `note` |")
    add("| [`data/wheels/odalu.json`](data/wheels/odalu.json) | wheel two, the body. Adds `lit`, the literal reading of each phrase |")
    add("| [`data/wheels/rasa.json`](data/wheels/rasa.json) | wheel three. Cores carry `sthayi`, the durable feeling under each rasa |")
    add("| [`data/words.csv`](data/words.csv) | all three wheels flattened into one table |")
    add("| [`data/native.json`](data/native.json) | the untranslatables appendix — `kn`, `tr`, `gloss` |")
    add("| [`data/rala-responses.json`](data/rala-responses.json) | raw API responses keyed by query — provenance for every claim above |")
    add("| [`scripts/rala.py`](scripts/rala.py) | rala client and the morphological expander |")
    add("| [`scripts/build.py`](scripts/build.py) | regenerates `index.html`, this README and `words.csv` |")
    add("| [`src/wheel.js`](src/wheel.js) | the sunburst renderer, shared by all three wheels |")
    add("")
    add("```bash\npython3 scripts/build.py                    # rebuild site + README\n"
        "python3 scripts/rala.py loneliness annoyed  # try the expander\n```\n")
    add("### One rendering note\n")
    add("Do not use SVG `<textPath>` for Kannada. It positions each glyph separately along "
        "the path, which shatters an akshara into base, vowel sign and ottakshara, each "
        "rotated on its own — ಅಸಹ್ಯ came out as three unrelated pieces. Core labels here are "
        "horizontal and never rotated; the outer rings rotate the whole string as one unit, "
        "which is safe.\n")

    add("## Attribution\n")
    add("- Word data checked against [**rala**](https://github.com/pvnkmrksk/rala), a "
        "reversal of [**Alar**](https://alar.ink) by V. Krishna, licensed "
        "[ODC-ODbL](https://opendatacommons.org/licenses/odbl/), combined with "
        "[Padakanaja](https://padakanaja.karnataka.gov.in/dictionary), Government of Karnataka.\n"
        "- ಭಾವಚಕ್ರ's structure follows Gloria Willcox's Feeling Wheel (1982) and its widely "
        "circulated three-ring descendant. ಒಡಲ ಚಕ್ರ and ರಸಚಕ್ರ are not translations of anything.\n"
        "- Derived data in `data/` is offered under ODbL, matching Alar. Code and page are MIT.\n")
    (ROOT / "README.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    return len("\n".join(L))


if __name__ == "__main__":
    h = build_html()
    build_csv()
    r = build_readme()
    print(f"index.html {h:,} · README.md {r:,} · data/words.csv")

#!/usr/bin/env python3
"""
build.py: assemble the site and the README from data/wheels/*.json.

  data/wheels/{bhava,odalu,rasa}.json
      -> index.html       three wheels behind one slider, no build step at serve time
      -> README.md        every word as flat markdown, plus the dictionary evidence

The site is for reading the words. The README is the extended cut: it carries
the rala lookups, the misfires and the counts, which are diagnostics and do not
belong on the page.

Run:  python3 scripts/build.py
"""

import csv
import hashlib
import json
import pathlib
import re
import sys

# Flip this to "https://bhava.kutuhula.in" once the DNS CNAME exists, and add a
# CNAME file at the repo root with the bare host. Doing it before DNS resolves
# takes the github.io URL down too, because Pages starts redirecting to it.
SITE = "https://bhava.kutuhula.in"

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA, SRC = ROOT / "data", ROOT / "src"
RINGS = ["core", "branch", "leaf"]

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from wheels import load, walk, inherit  # noqa: E402

WHEELS = [
 {"id": "bhava",
  "hint": "Tap or hover any segment: the panel names it in both scripts and lists the "
          "words that did not fit. Tap a sector to zoom in, and the middle of the wheel "
          "to come back out.",
  "blurb": "Seven core feelings, three rings, 130 words. The shape is borrowed from Gloria "
           "Willcox's Feeling Wheel, the one that circulates as a therapy handout. The "
           "Kannada in it is the word you would reach for out loud, with its close relatives "
           "listed beside it. Open a sector to read it.",
  "aboutTitle": "ಎರವಲಿನ ಆಕಾರ", "aboutLat": "a borrowed shape",
  "about": "Seven cores, a slot called <em>Bad</em>, <em>ashamed</em> kept apart from "
           "<em>guilty</em>: those are English assumptions about where feeling divides. "
           "Filling them in Kannada is worth doing exactly where the two languages disagree, "
           "and they disagree often enough that the other two wheels start somewhere else "
           "instead.",
  "cards": [
    {"h": "ಬೇಸರ does the work of four",
     "p": "Bored, busy, stressed and tired are four separate slots on the English wheel. "
          "In Kannada they sit in one word. ಬೇಸರಾಗಿದೆ can be any of them, and the listener "
          "works out which from your face."},
    {"h": "Where one word covers two",
     "p": "ನೋವು is bodily pain and hurt feelings without distinction: ಮನಸ್ಸಿಗೆ ನೋವಾಯಿತು, it "
          "hurt my mind, is the ordinary way to say you were wounded. ಚಿಂತೆ is worry and "
          "simply thought. ನಾಚಿಕೆ is shyness, modesty and shame at once."},
    {"h": "Where Kannada has six and a wedge has one",
     "p": "Fear comes graded, ಅಂಜಿಕೆ, ಹೆದರಿಕೆ, ದಿಗಿಲು, ಗಾಬರಿ, ಆತಂಕ, ಭೀತಿ, and doubt four "
          "ways: ಶಂಕೆ leans toward fear, ಸಂಶಯ toward suspicion of a person, ಸಂದೇಹ toward "
          "uncertainty about a fact, ಅನುಮಾನ is the everyday one. The wheel shows one and "
          "keeps the rest under ಹೀಗೂ ಹೇಳುತ್ತಾರೆ."},
    {"h": "Where the wheel asks for something not there",
     "p": "<em>Vulnerable</em> in its warm modern sense has no Kannada noun: ದುರ್ಬಲತೆ and "
          "ಸುಭೇದ್ಯ mean weak and breachable. Kannada puts it as something you do rather than "
          "something you are: ಮನಸ್ಸು ಬಿಚ್ಚು, to unfold the mind."}]},

 {"id": "odalu",
  "hint": "The centre is where in the body it happens, the middle ring is the feeling, and "
          "the outer ring is what gets said. Tap to zoom in; tap the middle to come back out.",
  "blurb": "Not a translation of anything. Kannada mostly names a feeling by saying "
           "<em>where in the body it is happening</em>: ಹೊಟ್ಟೆಕಿಚ್ಚು, belly-fire; ಎದೆಗುಂದು, "
           "the chest sinks; ಕರುಳು ಚುರುಕ್, the gut stings. So the seven seats are the centre, "
           "the feelings you would actually name are the middle ring, and the phrases people "
           "say are the outer one.",
  "aboutTitle": "ಒಡಲು", "aboutLat": "the body as the vessel of feeling",
  "about": "ಒಡಲು is an old word for the body considered as a container: the thing feeling "
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
    {"h": "Words with no English slot",
     "p": "ಮುನಿಸು, the sulk you are only entitled to with someone who loves you. ಸಲಿಗೆ, the "
          "earned licence to be informal with a person. ಕರುಳ ಬಳ್ಳಿ, the gut-vine: your own "
          "child. ಎದೆ ಝಲ್, the single cold jolt of alarm."},
    {"h": "ಕರುಳು is the strange one",
     "p": "In Kannada the gut is the organ of kinship, your child is your ಕರುಳ ಬಳ್ಳಿ, so "
          "every feeling sited there is about your own people. ಕರುಳು ಕಿತ್ತು ಬರು is kept for "
          "the death of a child or a parent, and using it lightly would be shocking."},
    {"h": "What it misses",
     "p": "Feelings with no bodily seat fall off: ಅಭಿಮಾನ, ಹಂಬಲ, ಕೃತಜ್ಞತೆ, ಸಂಭ್ರಮ. Catching "
          "those needs a second axis: probably direction, since ವಾತ್ಸಲ್ಯ only ever flows "
          "downward, ಗೌರವ upward and ಸಲಿಗೆ sideways."}]},

 {"id": "rasa",
  "hint": "The nine rasas are the centre; underneath each one are the words Kannada uses "
          "for that flavour. Tap to zoom in; tap the middle to come back out.",
  "blurb": "The oldest map of feeling this language has, opened out. The nine rasas are an "
           "aesthetic theory, what an audience can be made to feel, and a thousand years "
           "of Kannada poetry is organised by them. Here each rasa keeps its Sanskrit name, "
           "because that is what everyone calls it, and everything beneath it is the daily "
           "word: ಸಿಟ್ಟು under ರೌದ್ರ, ಬೆರಗು under ಅದ್ಭುತ, ಬೇಸರ under ಬೀಭತ್ಸ.",
  "aboutTitle": "ನವರಸ", "aboutLat": "nine flavours, not nine emotions",
  "about": "A rasa is not an emotion. It is the flavour an audience tastes, which is why "
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
          "either. ವೀರ's underlying feeling is not courage but ಉತ್ಸಾಹ, energy, which "
          "quietly claims heroism is a kind of enthusiasm."},
    {"h": "ಶಾಂತ, the one they argued about",
     "p": "The ninth rasa was added late and disputed for centuries: can the absence of "
          "agitation be a flavour at all? The English wheel files peace under happiness. The "
          "rasa tradition insists it is a state of its own, and gives it ಶಮ, quiet: as its "
          "durable feeling."},
    {"h": "The colours are not decoration",
     "p": "The Nāṭyaśāstra assigns each rasa a colour, and this wheel follows them: ಶೃಂಗಾರ "
          "śyāma green, ರೌದ್ರ red, ವೀರ wheaten gold, ಭಯಾನಕ black, ಬೀಭತ್ಸ blue, ಅದ್ಭುತ yellow, "
          "ಕರುಣ dove grey, ಹಾಸ್ಯ and ಶಾಂತ white: the last three shifted just far enough to "
          "stay legible on both a light and a dark ground."}]},
]

PROSE = {w["id"]: w for w in WHEELS}
WHEELS = [dict(PROSE[w["id"]], **w) for w in load(DATA / "words.csv")]
SONG_OWN, SONG_BORROWED = inherit(WHEELS)

SOURCES = json.loads((DATA / "sources.json").read_text(encoding="utf-8"))


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
    js = "\n".join((SRC / f).read_text(encoding="utf-8")
                   for f in ("track.js", "wheel.js", "player.js", "app.js"))
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
<meta property="og:description" content="Three emotion wheels in Kannada: from English, from the body, from the nine rasas.">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}/">
<link rel="canonical" href="{SITE}/">
<link rel="icon" href="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2032%2032'%3E%3Ccircle%20cx='16'%20cy='16'%20r='16'%20fill='%239C6E0C'/%3E%3Ccircle%20cx='16'%20cy='16'%20r='11'%20fill='%2316696E'/%3E%3Ccircle%20cx='16'%20cy='16'%20r='6'%20fill='%23A53426'/%3E%3C/svg%3E">
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#E6E9E2" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#12160F" media="(prefers-color-scheme: dark)">
<link rel="apple-touch-icon" href="assets/icon-192.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="ಭಾವಚಕ್ರ">
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
    build_pwa(doc)
    return len(doc)


# ------------------------------------------------------------------- the PWA
def build_pwa(doc):
    """manifest + service worker, so the wheel installs to a home screen."""
    version = hashlib.sha256(doc.encode("utf-8")).hexdigest()[:12]
    manifest = {
        "name": "ಭಾವಚಕ್ರ · three feeling wheels in Kannada",
        "short_name": "ಭಾವಚಕ್ರ",
        "description": "353 Kannada words for feeling, in three wheels.",
        "start_url": "./",
        "scope": "./",
        "display": "standalone",
        "orientation": "any",
        "lang": "kn",
        "dir": "ltr",
        "background_color": "#E6E9E2",
        "theme_color": "#E6E9E2",
        "icons": [
            {"src": "assets/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "assets/icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "assets/icon-maskable-512.png", "sizes": "512x512",
             "type": "image/png", "purpose": "maskable"},
        ],
        "shortcuts": [
            {"name": w["name"], "url": f"./#w={w['id']}",
             "icons": [{"src": "assets/icon-192.png", "sizes": "192x192"}]}
            for w in WHEELS
        ],
    }
    (ROOT / "manifest.webmanifest").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    sw = (SRC / "sw.js").read_text(encoding="utf-8").replace("__VERSION__", version)
    (ROOT / "sw.js").write_text(sw, encoding="utf-8")


# ---------------------------------------------------------------- wheels.json
def build_json():
    out = [{"id": w["id"], "name": w["name"], "tag": w["tag"], "wheel": w["data"]}
           for w in WHEELS]
    (DATA / "wheels.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")


# ------------------------------------------------------- README + METHOD
BUILT_FROM = {"bhava": "the English feeling wheel, translated and then argued with",
       "odalu": "the part of the body Kannada sites each feeling in",
       "rasa":  "the nine rasas of the Nāṭyaśāstra, opened out into daily Kannada"}


def nested(w, out):
    """Every ring of one wheel as an indented list: readable, and easy to scrape."""
    for core in w["data"]:
        head = [f"### {core['kn']} · {core['en']} · *{core['tr']}*"]
        if core.get("sthayi"):
            head.append(f"ಸ್ಥಾಯಿಭಾವ · {core['sthayi']}")
        out.append("  \n".join(head) + "\n")

        def line(n, depth):
            pad = "  " * depth
            bits = [f"{pad}- **{n['kn']}** · *{n['tr']}* · {md(n['en'])}"]
            if n.get("lit"):
                bits.append(f"literally {md(n['lit'])}")
            out.append(" · ".join(bits))
            if n.get("also"):
                out.append(f"{pad}  - also said: " + ", ".join(
                    f"**{a['kn']}** *{a['tr']}* {md(a['en'])}" for a in n["also"]))
            if n.get("note"):
                out.append(f"{pad}  - {md(n['note'])}")
            for k in n.get("kids", []):
                line(k, depth + 1)

        line(core, 0)
        out.append("")


def build_readme():
    L, add = [], None
    add = L.append
    total = sum(sum(1 for _ in walk(w["data"])) for w in WHEELS)
    add("# ಭಾವಚಕ್ರ · three feeling wheels in Kannada\n")
    add(f"**[{SITE.replace('https://','')}]({SITE}/)**\n")
    add(f"{total} words, three maps of the same territory. Every ring of every wheel is "
        "listed below.\n")
    add("| wheel | built from | words |\n|---|---|---:|")
    for w in WHEELS:
        add(f"| **{w['name']}** `{w['id']}` | {BUILT_FROM[w['id']]} | {sum(1 for _ in walk(w['data']))} |")
    add("")
    add("<p align=\"center\">\n"
        "  <a href=\"https://bhava.kutuhula.in/#w=bhava\"><img src=\"assets/bhava.png\" width=\"32%\" alt=\"ಭಾವಚಕ್ರ, the feeling wheel in Kannada\"></a>\n"
        "  <a href=\"https://bhava.kutuhula.in/#w=odalu\"><img src=\"assets/odalu.png\" width=\"32%\" alt=\"ಒಡಲ ಚಕ್ರ, feelings by where in the body they happen\"></a>\n"
        "  <a href=\"https://bhava.kutuhula.in/#w=rasa\"><img src=\"assets/rasa.png\" width=\"32%\" alt=\"ರಸಚಕ್ರ, the nine rasas opened out\"></a>\n"
        "</p>\n")
    add("*Full size: [ಭಾವಚಕ್ರ](assets/bhava.png) · [ಒಡಲ ಚಕ್ರ](assets/odalu.png) · "
        "[ರಸಚಕ್ರ](assets/rasa.png). As vector: [bhava.svg](assets/bhava.svg) · "
        "[odalu.svg](assets/odalu.svg) · [rasa.svg](assets/rasa.svg). "
        "CC BY-SA 4.0, the same as the text, so they can go on Wikipedia. "
        "Regenerate them with [`scripts/export_wheels.js`](scripts/export_wheels.js) "
        "and [`scripts/export_wheels.sh`](scripts/export_wheels.sh).*\n")

    add("**Everything lives in one file: [`data/words.csv`](data/words.csv).** One row per "
        "word, hierarchy from the `level` column and row order, exactly like an indented "
        "outline. Edit it in a spreadsheet or a text editor, commit, and push: "
        "[the build workflow](.github/workflows/build.yml) runs `scripts/build.py` and "
        "commits the rebuilt site back, so the CSV is the only file you ever touch. "
        "How the words were found is in [METHOD.md](METHOD.md).\n")
    add("```\nwheel  level  kannada  roman     english          sthayi  note  song  by  source  yt  start\n"
        "rasa   wheel  ರಸಚಕ್ರ    nava-rasa  <caption>\n"
        "rasa   0      ಶೃಂಗಾರ    śṛṅgāra    love, the erotic  ರತಿ           ಜೊತೆಯಲಿ ಜೊತೆ ಜೊತೆಯಲಿ  ಇಳಯರಾಜ  ಗೀತಾ · 1981  8HbwsAOfoRY  25\n"
        "rasa   1      ಒಲವು      olavu      fondness                       ಒಲವಿನ ಉಡುಗೊರೆ         ಎಂ. ರಂಗರಾವ್  ...  19r6J7zYjcA  20\n"
        "rasa   2      ಪ್ರೀತಿ     prīti      love\n```\n")

    add("### Changing a song\n")
    add("Five columns carry it, all in the same row as the word:\n")
    add("| column | what goes in it |\n|---|---|\n"
        "| `song` | the title, in Kannada |\n"
        "| `by` | composer, singer, poet |\n"
        "| `source` | the film and year, or the poet and the form |\n"
        "| `yt` | the eleven characters after `v=` in a YouTube URL |\n"
        "| `start` | the second the pallavi lands, set by ear |\n")
    add("`start` is worth setting. Old film songs open on a long orchestral prelude, and "
        "thirty seconds of strings is not what the word means. Play the song, note where "
        "the voice arrives, put that number in.\n")
    add("A word with no `yt` borrows from the nearest word above it that has one, and the "
        "panel says whose song it is, so you only fill in the rows worth filling in. If an "
        "id stops working the player falls back the same way.\n")
    add("Before pushing a new id it is worth running "
        "`python3 scripts/check_songs.py`, which asks YouTube whether every id is still "
        "public and still embeddable and exits non-zero if one has rotted.\n")

    for w in WHEELS:
        add(f"## {w['name']} · {BUILT_FROM[w['id']]}\n")
        add(f"*{w['tag']}*\n")
        nested(w, L)

    native = json.loads((DATA / "native.json").read_text(encoding="utf-8"))
    add("## Appendix: words with nowhere to sit\n")
    add("Feelings Kannada names precisely and English can only paraphrase. Most now live "
        "inside one of the wheels; the list is the argument for redrawing a wheel rather "
        "than translating one.\n")
    add("| ಕನ್ನಡ | roman | what it means |\n|---|---|---|")
    for x in native:
        add(f"| **{x['kn']}** | *{x['tr']}* | {md(x['gloss'])} |")
    add("")
    add("## Attribution\n")
    add("- Words checked against [**rala**](https://github.com/pvnkmrksk/rala), a reversal "
        "of [**Alar**](https://alar.ink) by V. Krishna, licensed "
        "[ODC-ODbL](https://opendatacommons.org/licenses/odbl/), combined with "
        "[Padakanaja](https://padakanaja.karnataka.gov.in/dictionary), Government of "
        "Karnataka. alar.ink itself was never queried.\n"
        "- ಭಾವಚಕ್ರ follows Gloria Willcox's Feeling Wheel (1982) and its widely circulated "
        "three-ring descendant. ಒಡಲ ಚಕ್ರ and ರಸಚಕ್ರ are not translations of anything.\n"
        "- Derived data under ODbL, matching Alar. Code and page are MIT.\n")
    (ROOT / "README.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    return len("\n".join(L))


def build_method():
    L, add = [], None
    add = L.append
    add("# How the words were found\n")
    add("Back to the [wheels](README.md).\n")
    add("## The lookup\n")
    add("```\nGET https://rala-search.rala-search.workers.dev/?q=<english word>\n\n"
        "{ \"query\": str,\n  \"count\": int,\n"
        "  \"results\": [ { \"kannada\", \"definition\", \"type\", \"source\" } ] }\n```\n")
    add("Calls were made one at a time with 0.35 s between them and without the "
        "`X-Rala-Intent: primary` header, so none of this reached rala's own search "
        "analytics. [alar.ink](https://alar.ink) was never queried: Alar arrives here only "
        "through rala's reversal of it.\n")
    add("rala matches whole words against definition text, so a query only finds the exact "
        "form the dictionary happens to use: `annoyed` returns nothing, `annoy` returns "
        "thirteen entries. [`scripts/rala.py`](scripts/rala.py) fixes this client-side with "
        "a morphological expander: 26 suffix rules, longest first, doubled-consonant undo, "
        "and one level of recursion so `playfully → playful → play`.\n")
    add("```\nloneliness  → loneliness, lonely, lone\n"
        "frustrated  → frustrated, frustrat, frustrate\n"
        "victimised  → victimised, victimise, victimize\n"
        "stopped     → stopped, stopp, stoppe, stop\n```\n")
    add("Of the 52 words that first came back empty, morphology alone recovered 38. The last "
        "14 needed hand-picked synonyms, `repelled → repulse`, `boredom → tedium`, "
        "`skeptical → sceptic`, which stemming cannot reach, and which is the argument for "
        "a thesaurus layer inside the worker rather than in every client.\n")

    counts = {}
    for k, v in SOURCES.get("bhava", {}).items():
        counts[v["status"]] = counts.get(v["status"], 0) + 1
    add("## What came back, for ಭಾವಚಕ್ರ\n")
    add("| | count | meaning |\n|---|---:|---|")
    for k, label in [("direct", "the dictionary's top hit is the word on the wheel"),
                     ("shaped", "rala had it, but buried in technical noise or in another register"),
                     ("gap", "no usable entry; the word comes from Kannada usage")]:
        add(f"| `{k}` | {counts.get(k,0)} | {label} |")
    add(f"| | **{sum(counts.values())}** | |\n")
    add("Where rala is excellent: fear, anger and grief. Seven graded fear words, four for "
        "doubt, and ತೇಜೋವಧೆ, \"the murder of someone's lustre\", for *humiliate*.\n")
    add("Where it falls down it falls down structurally, because rala's bulk is Padakanaja, "
        "which is administrative, legal, scientific and agricultural:\n")
    add("| query | what rala returned |\n|---|---|")
    for q, r in [("stressed", "ಪ್ರತಿಬಲ, tensile stress, shear stress"),
                 ("confused", "ತುಕ್ಕುಗೆಂಪು, the confused flour beetle"),
                 ("let down", "ಹಾಲೊಸರಿಕೆ, milk let-down, the dairy term"),
                 ("loving", "ನೆರಳು ಪ್ರಿಯ, shade-loving, of plants"),
                 ("depressed", "ದಲಿತ, ಶೋಷಿತ, from the phrase \"depressed classes\""),
                 ("accepted", "ಅಂಗೀಕೃತ ಟೆಂಡರ್, accepted tender"),
                 ("tired", "ದಣಿದ ಮಣ್ಣು, tired soil"),
                 ("critical", "ಕ್ರಾಂತಿಕೋನ: critical angle"),
                 ("proud / inspired / boredom / threatened", "nothing at all")]:
        add(f"| `{q}` | {r} |")
    add("")
    add("## Every lookup\n")
    add("Raw responses are in [`data/rala-responses.json`](data/rala-responses.json), keyed "
        "by query. The trail behind each word on ಭಾವಚಕ್ರ is in "
        "[`data/sources.json`](data/sources.json) and reproduced here.\n")
    add("| ಕನ್ನಡ | English slot | status | what rala returned |\n|---|---|---|---|")
    for kn, v in SOURCES.get("bhava", {}).items():
        add(f"| **{kn}** | {v['english']} | `{v['status']}` | "
            f"{', '.join(md(h) for h in v['rala']) or 'nothing'} |")
    add("")
    add("## One rendering note\n")
    add("Do not use SVG `<textPath>` for Kannada. It positions each glyph separately along "
        "the path, which shatters an akshara into base, vowel sign and ottakshara, each "
        "rotated on its own: ಅಸಹ್ಯ came out as three unrelated pieces. Labels on the "
        "innermost visible ring are upright and never rotated; the outer rings rotate the "
        "whole string as one unit, which is safe.\n")
    (ROOT / "METHOD.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    return len("\n".join(L))


if __name__ == "__main__":
    h = build_html()
    build_json()
    r = build_readme()
    m = build_method()
    print(f"index.html {h:,} · README.md {r:,} · METHOD.md {m:,} · wheels.json · words.csv")
    print(f"songs: {SONG_OWN} of their own, {SONG_BORROWED} borrowed from a parent")

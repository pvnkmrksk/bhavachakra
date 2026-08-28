#!/usr/bin/env python3
"""
build_draft.py — assemble draft/index.html, the second wheel.

v1 (index.html) translates the English feeling wheel into Kannada and shows
its own seams.  v2 throws the English structure away: its centre ring is the
part of the body a feeling is sited in, because that is how Kannada mostly
builds its emotion vocabulary — ಹೊಟ್ಟೆಕಿಚ್ಚು, ಎದೆಗುಂದು, ಕರುಳು ಚುರುಕ್, ತಲೆಬಿಸಿ.

Run:  python3 scripts/build_draft.py
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
seats = json.loads((ROOT / "draft" / "seats.json").read_text(encoding="utf-8"))

# The v1 stylesheet, with the seven sector hues swapped for the seats.
head = (ROOT / "src" / "head.html").read_text(encoding="utf-8")
HUE_MAP = [
    # light                                   dark
    (("--h-joy", "#A9790F"), ("--h-ede", "#A6384A"), ("--h-ede", "#DC6C7D")),
]
light_old = ("  --h-joy:#A9790F; --h-wonder:#16696E; --h-weary:#64744A;\n"
             "  --h-fear:#43478E; --h-anger:#A53426; --h-disgust:#723A6D; --h-sorrow:#26597F;")
light_new = ("  --h-ede:#A6384A; --h-hotte:#946E10; --h-karulu:#7A2B45;\n"
             "  --h-manassu:#3C4890; --h-tale:#146A75; --h-mai:#6A3F8E; --h-mukha:#586B3E;")
dark_old = ("--h-joy:#E2AC33; --h-wonder:#2AA0A5; --h-weary:#93A56E;\n"
            "  --h-fear:#6E73C8; --h-anger:#D45444; --h-disgust:#A75BA0; --h-sorrow:#3D84BC;")
dark_new = ("--h-ede:#DE6B7C; --h-hotte:#D2A032; --h-karulu:#C0637F;\n"
            "  --h-manassu:#6C77CE; --h-tale:#2E9BA6; --h-mai:#A177CE; --h-mukha:#94AB6C;")
head = head.replace(light_old, light_new)
head = head.replace(dark_old, dark_new)                       # :root[data-theme="dark"]
head = head.replace(dark_old.replace("\n  ", "\n    "),
                    dark_new.replace("\n  ", "\n    "))       # prefers-color-scheme block
# the draft's accent leans toward the body palette rather than turmeric
head = head.replace("--accent:#A8791A;", "--accent:#A6384A;")
head = head.replace("--accent-soft:#EFE3C6;", "--accent-soft:#F2DFE1;")
head = head.replace("--accent:#D9A93C;", "--accent:#DE6B7C;")
head = head.replace("--accent-soft:#332A14;", "--accent-soft:#33191C;")
head = head.replace("<title>ಭಾವಚಕ್ರ</title>", "<title>ಒಡಲ ಚಕ್ರ</title>")

body = """
<header class="wrap">
  <div class="mast">
    <div class="eyebrow">ಡ್ರಾಫ್ಟ್ · draft two · not a translation of anything</div>
    <h1>ಒಡಲ ಚಕ್ರ</h1>
    <p class="sub serif">The <a href="../">first wheel</a> was the English feeling wheel put into Kannada, and it showed its seams — ಶಾಂತಿ where ನೆಮ್ಮದಿ was meant, no word at all for <em>proud</em> or <em>vulnerable</em>. This one starts somewhere else. Kannada mostly names a feeling by saying <em>where in the body it is happening</em> and <em>what that part is doing</em>: ಹೊಟ್ಟೆಕಿಚ್ಚು, belly-fire. ಎದೆಗುಂದು, the chest sinks. ಕರುಳು ಚುರುಕ್, the gut stings. So the seat is the centre ring, the verb is the middle ring, and the feeling is what the two make together.</p>
    <div class="tally">
      <div><b>7</b><span>ಒಡಲ ನೆಲೆಗಳು · seats</span></div>
      <div><b>32</b><span>ಕ್ರಿಯೆಗಳು · movements</span></div>
      <div><b>64</b><span>ಭಾವಗಳು · feelings</span></div>
      <div><b>0</b><span>translated from English</span></div>
    </div>
  </div>

  <div class="bar">
    <div class="legend">
      <span class="lg">centre · where it happens &nbsp;→&nbsp; middle · what that part does &nbsp;→&nbsp; outer · the feeling</span>
    </div>
    <button class="toggle" id="langToggle" aria-pressed="false">Show meanings</button>
  </div>

  <div class="stage">
    <div class="wheelbox">
      <a class="skip" href="#reading">Skip the wheel's 103 segments</a>
      <svg class="wheel" id="wheel" viewBox="0 0 800 800" role="img" aria-label="A Kannada emotion wheel organised by the part of the body each feeling is sited in"></svg>
      <div class="hub" id="hub" aria-hidden="true">
        <div class="hw" id="hubWord">ಒಡಲು</div>
        <div class="ht" id="hubRom">oḍalu · the body as vessel</div>
      </div>
    </div>
    <aside class="detail" id="detail" aria-live="polite">
      <p class="hint">Hover or tap any segment. The centre ring is where in the body the feeling is sited, the middle ring is what that part does, and the outer ring is the feeling that compound names.</p>
    </aside>
  </div>
</header>

<main class="wrap">
<section id="reading">
  <div class="shead">
    <div class="eyebrow">ಏಕೆ ಹೀಗೆ · why this shape</div>
    <h2>ಒಡಲು <span class="lat">the body as the vessel of feeling</span></h2>
    <p>ಒಡಲು is an old Kannada word for the body considered as a container — the thing feeling happens inside. It is the right centre for this wheel because Kannada's emotional vocabulary is overwhelmingly compositional: a body part plus a verb. English does this too (heartbroken, gutted, hot-headed) but treats it as figurative colour on top of a real vocabulary. In Kannada it <em>is</em> the vocabulary, and it is not felt as metaphor — ಹೊಟ್ಟೆ ತೊಳಸು is used for moral revulsion and for actual nausea with no marker between the two senses.</p>
  </div>
  <div class="method">
    <div>
      <h3>What this buys you</h3>
      <p>An entry point English wheels do not have. "Where do you feel it?" is a better first question than "which of these seven?", and it is the question this wheel asks. It also holds words the first wheel had to leave out — ಮುನಿಸು, ಸಲಿಗೆ, ಕರುಳ ಬಳ್ಳಿ, ಮನಸ್ಸು ಬಿಚ್ಚು — because they had no English slot to sit in.</p>
    </div>
    <div>
      <h3>What it costs</h3>
      <p>Some real feelings have no bodily seat and are missing here: ಅಭಿಮಾನ, ಹಂಬಲ, ಕೃತಜ್ಞತೆ, ಸಂಭ್ರಮ. A second organising axis would catch them — direction of feeling (ವಾತ್ಸಲ್ಯ flows down, ಗೌರವ flows up, ಸಲಿಗೆ flows sideways), which is the other thing Kannada is strict about.</p>
    </div>
    <div>
      <h3>Open questions for a native ear</h3>
      <p>Every phrase here is one I can defend, but a draft is a draft. Worth checking: whether ಎದೆ ಝಲ್ and ಮೈ ಝುಮ್ read as too colloquial to print; whether ಸಪ್ಪೆ ಮೋರೆ is regional; whether ಒಡಲು survives as a living word or has gone fully literary; and whether ಕರುಳು deserves more of the wheel than it has, given how much of Kannada kinship runs through it.</p>
    </div>
    <div>
      <h3>Not from a dictionary</h3>
      <p>Unlike the <a href="../">first wheel</a>, this one was not assembled from rala lookups — an English→Kannada dictionary cannot produce a structure that has no English to start from. rala was used only in the other direction, to check that candidate words exist and to widen the outer ring (ತಣಿವು, ರೋಮಾಂಚ, ಕಕ್ಕಾಬಿಕ್ಕಿ, ಕನಿಕರ, ಮರುಕ all came out of it).</p>
    </div>
  </div>
  <footer>
    Draft two of <a href="https://github.com/pvnkmrksk/bhavachakra">ಭಾವಚಕ್ರ</a>. The <a href="../">first wheel</a> translates and shows its seams; this one starts from Kannada and will be wrong in different places. Corrections welcome as issues.
  </footer>
</section>
</main>
"""

app = (ROOT / "draft" / "app-v2.js").read_text(encoding="utf-8")
payload = "const SEATS = " + json.dumps(seats, ensure_ascii=False, separators=(",", ":")) + ";"

doc = f"""<!doctype html>
<html lang="kn">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="A Kannada emotion wheel built on where in the body each feeling is sited, rather than translated from English.">
<meta property="og:title" content="ಒಡಲ ಚಕ್ರ">
<meta property="og:description" content="A Kannada emotion wheel organised by the body, not translated from English.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='15' fill='%23A6384A'/%3E%3Ccircle cx='16' cy='16' r='7' fill='%23E6E9E2'/%3E%3C/svg%3E">
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
(ROOT / "draft" / "index.html").write_text(doc, encoding="utf-8")
print(f"draft/index.html {len(doc):,} bytes")

"""
rala.py: a thin client for the rala English→Kannada API, with the
morphological expansion the API does not (yet) do itself.

rala matches whole words against definition text, so it only finds a word in
the exact form the dictionary happens to use.  `annoyed` returns nothing;
`annoy` returns thirteen entries.  `loneliness` returns nothing; `lonely`
returns three.  The expander below turns a query into an ordered list of
candidate word-forms and tries them until one hits.

API:  GET https://rala-search.rala-search.workers.dev/?q=<word>
      -> {"query": str, "count": int,
          "results": [{"kannada", "definition", "type", "source", ...}]}

Be a good citizen: the module sleeps between calls and never sends the
X-Rala-Intent: primary header, which is what writes a query into the site's
own search logs.
"""

import json
import time
import urllib.parse
import urllib.request

API = "https://rala-search.rala-search.workers.dev/?q="
UA = "bhavachakra/1.0 (+https://github.com/pvnkmrksk/bhavachakra)"
DELAY = 0.35  # seconds between calls

# Endings that carry grammar rather than meaning, longest first so that
# -iness is tried before -ness and -ation before -ion.
SUFFIXES = [
    ("iness", ["y"]),
    ("ation", ["e", "ate", ""]),
    ("ously", ["ous", ""]),
    ("ement", ["e", ""]),
    ("ically", ["ic", "y"]),
    ("ised", ["ise", "ize"]),
    ("ized", ["ize", "ise"]),
    ("ness", [""]),
    ("ment", ["", "e"]),
    ("ible", ["", "e"]),
    ("able", ["", "e"]),
    ("ally", ["al", ""]),
    ("ity", ["e", ""]),
    ("ful", [""]),
    ("ous", ["", "e"]),
    ("ive", ["", "e"]),
    ("ies", ["y"]),
    ("ied", ["y"]),
    ("ing", ["", "e"]),
    ("est", ["", "e"]),
    ("ly", [""]),
    ("ed", ["", "e"]),
    ("es", ["", "e"]),
    ("er", ["", "e"]),
    ("al", [""]),
    ("s", [""]),
]


def expand(word, _depth=0):
    """Ordered candidate forms for one English query, most literal first."""
    w = word.lower().strip()
    out = [w]

    def add(c):
        if len(c) > 2 and c not in out:
            out.append(c)

    for suffix, replacements in SUFFIXES:
        if w.endswith(suffix) and len(w) - len(suffix) >= 3:
            stem = w[: -len(suffix)]
            for r in replacements:
                add(stem + r)
            # undo a doubled final consonant: "stopped" -> "stopp" -> "stop"
            if len(stem) > 3 and stem[-1] == stem[-2] and stem[-1] not in "aeiou":
                add(stem[:-1])
            break

    # one more level, so "playfully" reaches "play" via "playful"
    if _depth == 0:
        for c in list(out[1:]):
            for deeper in expand(c, _depth=1):
                add(deeper)

    # multi-word queries: also try the head word alone
    if " " in w:
        add(w.split()[-1])
        add(w.split()[0])
    return out


def search(query, timeout=30):
    """One raw call. Returns the parsed response dict."""
    req = urllib.request.Request(API + urllib.parse.quote(query), headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def lookup(word, max_forms=4, verbose=False):
    """
    Search rala for `word`, falling back through morphological variants.

    Returns {"query", "matched_form", "results", "tried"} where matched_form is
    the word-form that actually produced hits (None if nothing did).
    """
    tried = []
    for form in expand(word)[:max_forms]:
        tried.append(form)
        try:
            data = search(form)
            results = data.get("results", [])
        except Exception as exc:  # network hiccup, 503 from the worker, etc.
            if verbose:
                print(f"  ! {form}: {exc}")
            results = []
        time.sleep(DELAY)
        if results:
            if verbose:
                print(f"  {word} -> {form}: {len(results)}")
            return {"query": word, "matched_form": form, "results": results, "tried": tried}
    if verbose:
        print(f"  {word} -> nothing (tried {', '.join(tried)})")
    return {"query": word, "matched_form": None, "results": [], "tried": tried}


if __name__ == "__main__":
    import sys

    for w in sys.argv[1:] or ["loneliness", "annoyed", "playfully", "frustrated"]:
        r = lookup(w, verbose=True)
        for hit in r["results"][:5]:
            print(f"    {hit['kannada']}  <{hit['definition'][:44]}>")

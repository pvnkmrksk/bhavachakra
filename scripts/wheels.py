"""
wheels.py: read data/words.csv, the one file you edit by hand.

Every wheel, ring and word is a row. Hierarchy comes from row order plus the
`level` column, exactly like an indented outline, so it opens in any
spreadsheet and diffs cleanly in git.

    wheel  level  kannada  roman  english  literal  sthayi  also  note
      song  by  source  yt  start
    ---------------------------------------------------------------------
    rasa   wheel  ರಸಚಕ್ರ    nava-rasa   <the line shown above the wheel>   ನವರಸ
    rasa   0      ಶೃಂಗಾರ    śṛṅgāra     love, the erotic
    rasa   1      ಒಲವು      olavu       fondness
    rasa   2      ಪ್ರೀತಿ     prīti       love

  level   `wheel` for a wheel's own row, then 0 = sector, 1 = branch, 2 = leaf.
          A level-1 row belongs to the level-0 row above it, and so on.
  literal on a word row, the literal reading; on a `wheel` row, the hub label.
  roman   on a `wheel` row, the hub's second line.
  english on a `wheel` row, the caption printed above the wheel.
  also    synonyms that did not fit: `ಪದ|pada|meaning ;; ಪದ|pada|meaning`
  note    prose about the word. Inline <i> is allowed.
  song    the song for this word, in Kannada
  by      composer, singer, poet
  source  the film and year, or the poet and the form
  yt      an eleven-character YouTube id. Several, comma separated, make a
          little catalogue for that word, played in the order written.
  start   the second the pallavi lands, set by ear: old film songs open on a
          long orchestral prelude and nobody wants thirty seconds of strings

  song, by, source and start take either one value, which applies to every
  song in `yt`, or one value per song, comma separated in the same order.

A word with no `yt` inherits the nearest ancestor that has one, so ಕೊಂಕು plays
ಬೀಭತ್ಸ's song and the page says whose it is.

Add a row, run `python3 scripts/build.py`, and the site, the README and the
JSON all follow.
"""

import csv
import pathlib


def load(path):
    wheels, by_id, stack = [], {}, []
    with pathlib.Path(path).open(encoding="utf-8") as f:
        for i, r in enumerate(csv.DictReader(f), start=2):
            wid = (r.get("wheel") or "").strip()
            lvl = (r.get("level") or "").strip()
            if not wid or not lvl:
                continue

            if lvl == "wheel":
                w = {"id": wid, "name": r["kannada"].strip(),
                     "hubKn": (r["literal"] or r["kannada"]).strip(),
                     "hubRom": r["roman"].strip(), "tag": r["english"].strip(),
                     "data": []}
                wheels.append(w); by_id[wid] = w; stack = []
                continue

            if wid not in by_id:
                raise ValueError(f"{path}:{i}: no `wheel` row for {wid!r} yet")
            try:
                depth = int(lvl)
            except ValueError:
                raise ValueError(f"{path}:{i}: level must be `wheel`, 0, 1 or 2")
            if depth > len(stack):
                raise ValueError(f"{path}:{i}: {r['kannada']!r} is level {depth} "
                                 f"but has no level {depth - 1} row above it")

            node = {"kn": r["kannada"].strip(), "tr": r["roman"].strip(),
                    "en": r["english"].strip(), "kids": []}
            for key, col in (("lit", "literal"), ("sthayi", "sthayi"), ("note", "note")):
                if r.get(col, "").strip():
                    node[key] = r[col].strip()
            ids = [v.strip() for v in (r.get("yt") or "").split(",") if v.strip()]
            if ids:
                for v in ids:
                    if len(v) != 11:
                        raise ValueError(f"{path}:{i}: {r['kannada']!r} has a bad "
                                         f"YouTube id {v!r}")

                # One value applies to every song, or give one per song. So a
                # run of songs from the same film needs `source` written once,
                # but each can have its own `start`.
                def column(name, default=""):
                    vals = [v.strip() for v in (r.get(name) or "").split(",")]
                    vals = [v for v in vals if v] or [default]
                    if len(vals) == 1:
                        return vals * len(ids)
                    if len(vals) != len(ids):
                        raise ValueError(
                            f"{path}:{i}: {r['kannada']!r} lists {len(ids)} songs "
                            f"but {len(vals)} values in `{name}`. Give one, or one each.")
                    return vals

                titles, bys = column("song"), column("by")
                srcs, starts = column("source"), column("start", "0")
                node["songs"] = [
                    {"t": titles[k], "by": bys[k], "src": srcs[k],
                     "yt": ids[k], "st": int(starts[k] or 0)}
                    for k in range(len(ids))]
            if r.get("also", "").strip():
                node["also"] = [
                    {"kn": p[0].strip(), "tr": p[1].strip(), "en": "|".join(p[2:]).strip()}
                    for p in (c.split("|") for c in r["also"].split(";;")) if len(p) >= 3]

            del stack[depth:]
            (stack[-1]["kids"] if stack else by_id[wid]["data"]).append(node)
            stack.append(node)
    return wheels


def walk(data, depth=0, sector=None):
    """Yield (depth, sector_kn, node) over a wheel, in wheel order."""
    for n in data:
        s = sector or n["kn"]
        yield depth, s, n
        yield from walk(n.get("kids", []), depth + 1, s)


def inherit(wheels):
    """Fill `song` downward, marking what a word had to borrow.

    Returns (own, borrowed) for the build to print, so a wheel that quietly
    stopped matching its songs is visible in one line of output.
    """
    own = borrowed = 0

    def walk(nodes, carried):
        nonlocal own, borrowed
        for n in nodes:
            if "songs" in n:
                own += len(n["songs"])
                carry = (n["songs"], n["kn"])
            elif carried:
                songs, src = carried
                n["songs"] = [dict(x, **{"from": src}) for x in songs]
                borrowed += 1
                carry = carried
            else:
                carry = None
            walk(n.get("kids", []), carry)

    for w in wheels:
        walk(w["data"], None)
    return own, borrowed

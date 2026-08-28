"""
wheels.py — read the hand-editable wheel sources in data/*.md.

The source of truth is a nested markdown list. Edit those files by hand; the
site, the README, the JSON and the CSV are all generated from them.

    # ರಸಚಕ್ರ                     <- display name
    id: rasa                     <- header keys, one per line, until the first node
    hub: ನವರಸ | nava-rasa
    tag: one line shown above the wheel

    - ಶೃಂಗಾರ | śṛṅgāra | love, the erotic
      sthayi: ರತಿ · rati, desire
      note: prose about the word
      - ಒಲವು | olavu | fondness
        - ಪ್ರೀತಿ | prīti | love
          also: ಮಮತೆ | mamate | attachment-love ;; ಅಕ್ಕರೆ | akkare | fondness

A node line is `- kannada | transliteration | meaning`. Two spaces of indent per
level. Any `key: value` line indented under a node attaches to it. `also` holds
synonyms separated by ` ;; `, each written the same way as a node line.
"""

import pathlib

FIELDS = ("note", "lit", "sthayi")


def parse(path):
    meta, roots, stack = {}, [], []
    name = None
    for raw in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        if raw.startswith("# "):
            name = raw[2:].strip()
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()

        if line.startswith("- "):
            bits = [b.strip() for b in line[2:].split("|")]
            if len(bits) < 3:
                raise ValueError(f"{path}: node needs kn | tr | en → {line!r}")
            node = {"kn": bits[0], "tr": bits[1], "en": " | ".join(bits[2:]), "kids": []}
            depth = indent // 2
            del stack[depth:]
            (stack[-1]["kids"] if stack else roots).append(node)
            stack.append(node)
            continue

        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if not stack:                      # header, before any node
            meta[key] = val
            continue
        if key == "also":
            stack[-1]["also"] = [
                {"kn": p[0], "tr": p[1], "en": " | ".join(p[2:])}
                for p in ([x.strip() for x in chunk.split("|")]
                          for chunk in val.split(";;")) if len(p) >= 3]
        elif key in FIELDS:
            stack[-1][key] = val
        else:
            raise ValueError(f"{path}: unknown field {key!r}")
    meta["name"] = name
    meta["data"] = roots
    return meta


def walk(data, depth=0, sector=None):
    """Yield (depth, sector_kn, node) over a whole wheel, in wheel order."""
    for n in data:
        s = sector or n["kn"]
        yield depth, s, n
        yield from walk(n.get("kids", []), depth + 1, s)


def count(data):
    return sum(1 for _ in walk(data))

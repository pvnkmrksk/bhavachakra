#!/usr/bin/env python3
"""
check_songs.py: confirm every YouTube id in data/words.csv is still playable.

YouTube ids rot: a video goes private, a label pulls a track, or embedding gets
switched off on an upload that used to allow it. A dead id is invisible on the
page until someone clicks it, so check before you ship.

    python3 scripts/check_songs.py          all of them
    python3 scripts/check_songs.py rasa     one wheel

Exits non-zero if anything is unplayable, so it can gate a deploy.
"""

import csv
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
      "Accept-Language": "en-US,en;q=0.9"}


def check(vid):
    try:
        req = urllib.request.Request("https://www.youtube.com/watch?v=" + vid, headers=UA)
        h = urllib.request.urlopen(req, timeout=25).read().decode("utf8", "replace")
    except Exception as e:
        return False, f"unreachable: {e}"
    st = re.search(r'"status":"(\w+)"', h)
    status = st.group(1) if st else "?"
    if status != "OK":
        return False, f"status {status}"
    if '"playableInEmbed":true' not in h:
        return False, "embedding disabled"
    chan = re.search(r'"ownerChannelName":"([^"]*)"', h)
    return True, chan.group(1).encode().decode("unicode_escape") if chan else ""


def repeats(rows):
    """A song may appear in more than one wheel: the wheels are different maps
       of the same territory and a song can sit honestly in each. Twice inside
       one wheel is a mistake, because one of the two words is being told a
       lie about itself."""
    seen = {}
    for r in rows:
        for v in (r.get("yt") or "").split(","):
            v = v.strip()
            if v:
                seen.setdefault((r["wheel"], v), []).append(r["kannada"])
    return {k: v for k, v in seen.items() if len(v) > 1}


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    rows = [r for r in csv.DictReader((ROOT / "data/words.csv").open(encoding="utf-8"))
            if r.get("yt", "").strip() and (not only or r["wheel"] == only)]
    dup = repeats(rows)
    for (wheel, vid), words in dup.items():
        print(f"REPEAT  {wheel}  {vid}  ->  {', '.join(words)}")

    bad = []
    for r in rows:
        ok, why = check(r["yt"].strip())
        print(f"{'ok  ' if ok else 'DEAD'}  {r['wheel']:6}  {r['kannada']:14}  {r['yt']}  {why}")
        if not ok:
            bad.append((r["kannada"], r["yt"], why))
    print(f"\n{len(rows) - len(bad)} of {len(rows)} playable"
          f"{f', {len(dup)} repeated inside a wheel' if dup else ''}")
    if bad:
        print("\nreplace these:")
        for kn, vid, why in bad:
            print(f"  {kn}  {vid}  ({why})")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

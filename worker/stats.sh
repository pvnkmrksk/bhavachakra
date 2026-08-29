#!/bin/sh
# Read the counter. The only way in, on purpose.
#
# There is no stats endpoint on the Worker: nothing on the public internet can
# read this data, with or without a key. This script goes through
# `wrangler d1 execute`, which goes through your Cloudflare login, which is the
# only lock here worth trusting.
#
#   ./stats.sh            the last 30 days
#   ./stats.sh 7          the last 7 days
set -e
cd "$(dirname "$0")"
DAYS="${1:-30}"
SINCE="(strftime('%s','now') - ${DAYS}*86400)*1000"

run() {
  printf '\n\033[1m%s\033[0m\n' "$1"
  npx wrangler d1 execute bhava-log --remote --json --command "$2" 2>/dev/null \
    | python3 -c '
import json,sys
rows = json.load(sys.stdin)[0]["results"]
if not rows: print("  (nothing yet)"); raise SystemExit
cols = list(rows[0])
w = {c: max(len(str(c)), *(len(str(r[c])) for r in rows)) for c in cols}
print("  " + "  ".join(str(c).ljust(w[c]) for c in cols))
for r in rows: print("  " + "  ".join(str(r[c]).ljust(w[c]) for c in cols))
'
}

run "reach" "SELECT COUNT(DISTINCT aid) people, COUNT(DISTINCT sid) visits, COUNT(*) events FROM events WHERE ts > $SINCE"

run "wheels" "SELECT wheel, COUNT(DISTINCT sid) visits FROM events WHERE ts > $SINCE AND ev='open' GROUP BY wheel ORDER BY visits DESC"

run "where they are" "SELECT country, city, SUM(visits) visits FROM geo WHERE day >= date('now', '-$DAYS day') GROUP BY country, city ORDER BY visits DESC LIMIT 20"

run "words opened" "SELECT wheel, word, COUNT(*) opens, COUNT(DISTINCT aid) people FROM events WHERE ts > $SINCE AND ev='sel' AND word IS NOT NULL GROUP BY wheel, word ORDER BY opens DESC LIMIT 25"

run "how they move" "SELECT prev || ' -> ' || word AS move, COUNT(*) n FROM events WHERE ts > $SINCE AND ev='sel' AND prev IS NOT NULL GROUP BY prev, word ORDER BY n DESC LIMIT 25"

run "where they stop" "SELECT word, COUNT(*) n FROM events e WHERE ts > $SINCE AND ev='sel' AND ts = (SELECT MAX(ts) FROM events WHERE sid = e.sid AND ev='sel') GROUP BY word ORDER BY n DESC LIMIT 15"

run "songs, and how much of them" "SELECT word, COUNT(*) plays, SUM(ms)/1000 secs, SUM(ms)/COUNT(*)/1000 avg_secs FROM events WHERE ts > $SINCE AND ev='listen' GROUP BY word, yt ORDER BY secs DESC LIMIT 20"

printf '\n  a song with many plays and a low avg_secs is one people skip:\n  either its start offset is wrong, or the song is.\n\n'

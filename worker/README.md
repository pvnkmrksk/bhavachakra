# bhava-log

A counter for [ಭಾವಚಕ್ರ](https://bhava.kutuhula.in). One Cloudflare Worker, one
D1 table, no third party.

The question it exists to answer is not *how many people looked at ಕರುಣ* but
*where did they come from, and where did they go next*. A pile of view counts
cannot tell you that readers reach ವಿರಹ from ಪ್ರೀತಿ rather than from ಶೃಂಗಾರ.
So every selection records the word before it and how long the reader stayed
there, which turns the log into a graph of moves.

## What is stored

| column | |
|---|---|
| `aid` | a random uuid kept in the reader's own localStorage |
| `sid` | one visit; new on every page load |
| `ev` | `open` · `sel` · `drill` · `play` · `listen` · `lang` |
| `wheel`, `word` | which wheel, which word |
| `prev` | for `sel`, the word they came from |
| `ms` | dwell on `prev`, or milliseconds of song that actually sounded |
| `yt` | the song, when one played |

Not stored on an event: IP, user agent, referrer, or anything typed. No cookies.

City and country **are** recorded, once per visit, in a separate `geo` table
that carries no `aid` and no `sid`. That separation is the whole point. You
can ask how many people opened the wheel in Bengaluru on Tuesday; you cannot
ask what the reader in Bengaluru looked at, because the schema has no column
that would join the two.
Readers who send Do Not Track or Global Privacy Control are not counted at
all, and `localStorage['bhava.notrack'] = 1` opts out by hand.

## Nothing can read it over the internet

The Worker has one route, `POST /e`. There is no stats endpoint, no key, and
nothing to leak or rotate. Every other path returns 404:

```
GET /stats  ->  404      GET /       ->  404
GET /e      ->  404      GET /geo    ->  404
```

The data is read with `wrangler`, which goes through your Cloudflare login and
its 2FA. That is the only lock here worth trusting, and it is the one you
already have.

The write path cannot be authenticated: it is called by every reader's
browser, so any secret shipped to it is public by the second page view. The
Origin allowlist stops other websites but not `curl`, which can claim any
Origin. That is an accepted cost, and a cheap one: the worst case is junk rows
in a table nobody but you can read.

Worker logs are on, persisted, and visible only in your own Cloudflare
dashboard. Nothing in `analytics.js` ever writes an event, a word or an id
into a log line, so the logs hold request metadata and nothing else.

## Reading it

```sh
cd worker
./stats.sh          # the last 30 days
./stats.sh 7        # the last 7
```

That prints reach, which wheels get opened, where readers are, the words they
open, **how they move**, where they stop, and how much of each song actually
played. Or ask D1 whatever you like directly:

```sh
npx wrangler d1 execute bhava-log --remote --command "..."
```

**The words people actually open**

```sql
SELECT wheel, word, COUNT(*) opens, COUNT(DISTINCT aid) people
  FROM events WHERE ev='sel' GROUP BY wheel, word ORDER BY opens DESC LIMIT 30;
```

**How they move: the edges of the graph**

```sql
SELECT wheel, prev AS from_word, word AS to_word, COUNT(*) n
  FROM events WHERE ev='sel' AND prev IS NOT NULL
 GROUP BY wheel, prev, word ORDER BY n DESC LIMIT 40;
```

**Where people stop** — the last word of each visit, which is as close as this
gets to asking what someone was looking for

```sql
SELECT word, COUNT(*) n FROM events e
 WHERE ev='sel' AND ts = (SELECT MAX(ts) FROM events WHERE sid = e.sid AND ev='sel')
 GROUP BY word ORDER BY n DESC LIMIT 20;
```

**Which songs are listened to rather than merely started**

```sql
SELECT word, yt, COUNT(*) plays, SUM(ms)/1000 secs, SUM(ms)/COUNT(*)/1000 avg_secs
  FROM events WHERE ev='listen' GROUP BY word, yt ORDER BY secs DESC LIMIT 30;
```

A song with many plays and a low `avg_secs` is one people skip: either the
`start` offset lands in the wrong place, or the song is wrong for the word.

**How long a word holds someone**

```sql
SELECT prev AS word, COUNT(*) n, AVG(ms)/1000 avg_secs
  FROM events WHERE ev='sel' AND prev IS NOT NULL AND ms < 600000
 GROUP BY prev HAVING n > 5 ORDER BY avg_secs DESC LIMIT 30;
```

**Where the audience is**

```sql
SELECT country, city, SUM(visits) visits
  FROM geo GROUP BY country, city ORDER BY visits DESC LIMIT 30;
```

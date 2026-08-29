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

## What the key does and does not protect

`/stats` is a public URL with a shared secret in front of it. It is **not**
behind your Cloudflare login: anyone holding that string can read the
aggregates from anywhere, and 2FA on the dashboard does not apply. If you want
it behind a real login, put [Cloudflare
Access](https://developers.cloudflare.com/cloudflare-one/policies/access/) in
front of the Worker route in Zero Trust and require your identity provider;
then the key becomes a second lock rather than the only one.

`POST /e` has no key at all, and cannot have one: it is called by every
reader's browser, so any secret shipped to it would be public by the second
page view. It is guarded by an Origin allowlist, which stops other websites
from posting but not `curl`, which can claim any Origin it likes. The exposure
is junk rows, not disclosure: nothing is readable through that path.

Rotate the key any time with `npx wrangler secret put STATS_KEY`. The old one
stops working the moment the new one deploys.

## Deploy

Deployed and live at **https://bhava-log.rala-search.workers.dev**, writing to
the D1 database `bhava-log`. `ENDPOINT` in [`src/track.js`](../src/track.js)
already points at it.

`/stats` stays closed until you give it a key:

```sh
cd worker
npx wrangler secret put STATS_KEY
```

To redeploy after editing `analytics.js`: `npx wrangler deploy`.

## Reading it

`GET /stats` returns the aggregates below as JSON. Send the key as a header,
not in the URL:

```sh
curl -H "Authorization: Bearer $BHAVA_STATS_KEY" \
     "https://bhava-log.rala-search.workers.dev/stats?days=30"
```

`?key=` still works so the endpoint can be opened in a browser in a pinch, but
a key in a query string is written into every log it passes, into browser
history, and into the Referer of anything clicked from that page. The Worker
has `redact_query_string` on so its own logs will not keep it, which does
nothing about the other three.

The comparison is done on SHA-256 digests rather than with `===`, so a wrong
key takes the same time to reject however much of it was right, and a wrong
key gets a 404 rather than a 401: an endpoint that answers differently when
the key is merely wrong is an endpoint that confirms it exists. `/stats`
returns no CORS headers, so no page in any browser can read it.

Or ask D1 directly:

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

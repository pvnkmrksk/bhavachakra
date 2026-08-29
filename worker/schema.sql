-- One row per thing a reader did. No IP, no user agent, no location: the
-- question is how people move through the wheel, and none of that helps
-- answer it.
--
--   aid   an anonymous id, a random uuid kept in the reader's localStorage.
--         It survives reloads so a returning reader is one line, not many,
--         and it is meaningless outside this site.
--   sid   one visit. New on every page load.
--   ev    open | sel | drill | play | listen | lang
--   prev  for `sel`, the word they were on before this one. This column is
--         the whole point: it turns a pile of views into a graph of moves.
--   ms    for `sel`, how long they stayed on `prev`. For `listen`, how many
--         milliseconds of the song actually played.

CREATE TABLE IF NOT EXISTS events (
  id     INTEGER PRIMARY KEY AUTOINCREMENT,
  ts     INTEGER NOT NULL,
  aid    TEXT    NOT NULL,
  sid    TEXT    NOT NULL,
  wheel  TEXT,
  ev     TEXT    NOT NULL,
  word   TEXT,
  prev   TEXT,
  ms     INTEGER,
  yt     TEXT
);

CREATE INDEX IF NOT EXISTS ix_events_ts    ON events(ts);
CREATE INDEX IF NOT EXISTS ix_events_word  ON events(wheel, word);
CREATE INDEX IF NOT EXISTS ix_events_edge  ON events(wheel, prev, word);
CREATE INDEX IF NOT EXISTS ix_events_aid   ON events(aid);

-- Audience, kept deliberately separate from behaviour.
--
-- Cloudflare hands the Worker a city and country for free. Putting them on the
-- events table would have made every row a place plus a person plus a word,
-- which is a profile. So they live here instead: a count per place per day,
-- with no aid and no sid on the row. You can ask how many people read the
-- wheel in Bengaluru on Tuesday. You cannot ask what the person in Bengaluru
-- read, because that link does not exist in the schema.

CREATE TABLE IF NOT EXISTS geo (
  day      TEXT NOT NULL,          -- YYYY-MM-DD, UTC
  country  TEXT,
  region   TEXT,
  city     TEXT,
  visits   INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (day, country, region, city)
);

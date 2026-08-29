/* bhava-log: a counter for the wheel.
 *
 * POST /e   a batch of events from one reader, written to D1
 * GET  /stats?key=...   aggregates: what gets read, and how people move
 *
 * What is deliberately not stored: IP, user agent, referrer, country. The
 * question is how a reader moves through the wheel, and none of those help
 * answer it. Cloudflare sees the IP to route the request; we never write it.
 */

const EV = new Set(["open", "sel", "drill", "play", "listen", "lang"]);
const MAX_BATCH = 60;
const MAX_BODY = 24 * 1024;

const cors = origin => ({
  "Access-Control-Allow-Origin": origin,
  "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
  "Access-Control-Allow-Headers": "content-type",
  "Access-Control-Max-Age": "86400",
  "Vary": "Origin",
});

const clip = (v, n) => (typeof v === "string" ? v.slice(0, n) : null);
const num = v => (Number.isFinite(+v) ? Math.max(0, Math.min(+v, 86_400_000)) | 0 : null);

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const origin = request.headers.get("Origin") || "";
    const allowed = (env.ALLOWED || "").split(",").map(s => s.trim()).filter(Boolean);
    const ok = allowed.includes(origin) ? origin : allowed[0] || "";

    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: cors(ok) });

    if (url.pathname === "/e" && request.method === "POST") {
      if (origin && !allowed.includes(origin))
        return new Response("no", { status: 403, headers: cors(ok) });

      const raw = await request.text();
      if (raw.length > MAX_BODY)
        return new Response("too big", { status: 413, headers: cors(ok) });

      let body;
      try { body = JSON.parse(raw); } catch { return new Response("bad json", { status: 400, headers: cors(ok) }); }

      const aid = clip(body.aid, 40), sid = clip(body.sid, 40);
      const list = Array.isArray(body.ev) ? body.ev.slice(0, MAX_BATCH) : [];
      if (!aid || !sid || !list.length)
        return new Response("nothing to do", { status: 400, headers: cors(ok) });

      const now = Date.now();
      const stmt = env.DB.prepare(
        "INSERT INTO events (ts, aid, sid, wheel, ev, word, prev, ms, yt) VALUES (?,?,?,?,?,?,?,?,?)");
      const rows = [];
      for (const e of list) {
        if (!e || !EV.has(e.t)) continue;
        rows.push(stmt.bind(now, aid, sid, clip(e.w, 16), e.t,
                            clip(e.k, 80), clip(e.p, 80), num(e.ms), clip(e.yt, 16)));
      }
      if (!rows.length) return new Response("nothing to do", { status: 400, headers: cors(ok) });

      // Audience, counted once per visit and kept in its own table with no id
      // on the row: a place per day, never a place per person per word.
      if (body.first) {
        const cf = request.cf || {};
        const day = new Date(now).toISOString().slice(0, 10);
        rows.push(env.DB.prepare(
          `INSERT INTO geo (day, country, region, city, visits) VALUES (?,?,?,?,1)
             ON CONFLICT(day, country, region, city) DO UPDATE SET visits = visits + 1`)
          .bind(day, clip(cf.country, 8) || "??", clip(cf.region, 40) || "",
                clip(cf.city, 60) || ""));
      }

      await env.DB.batch(rows);
      return new Response(String(rows.length), { status: 202, headers: cors(ok) });
    }

    if (url.pathname === "/stats" && request.method === "GET") {
      if (!env.STATS_KEY || url.searchParams.get("key") !== env.STATS_KEY)
        return new Response("closed", { status: 404, headers: cors(ok) });

      const days = Math.min(parseInt(url.searchParams.get("days") || "30", 10) || 30, 365);
      const since = Date.now() - days * 86_400_000;
      const q = sql => env.DB.prepare(sql).bind(since).all().then(r => r.results);

      const [words, edges, listens, reach, funnel, places] = await Promise.all([
        q(`SELECT wheel, word, COUNT(*) n, COUNT(DISTINCT aid) people
             FROM events WHERE ts > ? AND ev='sel' AND word IS NOT NULL
            GROUP BY wheel, word ORDER BY n DESC LIMIT 200`),
        q(`SELECT wheel, prev, word, COUNT(*) n
             FROM events WHERE ts > ? AND ev='sel' AND prev IS NOT NULL
            GROUP BY wheel, prev, word ORDER BY n DESC LIMIT 300`),
        q(`SELECT wheel, word, yt, COUNT(*) plays, SUM(ms)/1000 seconds
             FROM events WHERE ts > ? AND ev='listen'
            GROUP BY wheel, word, yt ORDER BY seconds DESC LIMIT 200`),
        q(`SELECT COUNT(DISTINCT aid) people, COUNT(DISTINCT sid) visits
             FROM events WHERE ts > ?`),
        q(`SELECT wheel, COUNT(DISTINCT sid) visits FROM events
            WHERE ts > ? AND ev='open' GROUP BY wheel ORDER BY visits DESC`),
        env.DB.prepare(
          `SELECT country, city, SUM(visits) visits FROM geo
             WHERE day >= date(?/1000, 'unixepoch')
            GROUP BY country, city ORDER BY visits DESC LIMIT 100`)
          .bind(since).all().then(r => r.results),
      ]);

      return Response.json(
        { days, reach: reach[0], wheels: funnel, places, words, edges, listens },
        { headers: cors(ok) });
    }

    return new Response("bhava-log", { status: 200, headers: cors(ok) });
  },
};

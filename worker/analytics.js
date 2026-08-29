/* bhava-log: a counter for the wheel.
 *
 * POST /e   a batch of events from one reader, written to D1
 *
 * That is the only route. There is deliberately no way to read anything back
 * out over the internet: no stats endpoint, no key to leak, nothing to attack.
 * The data is read with `wrangler d1 execute`, which goes through a Cloudflare
 * login, which is the only lock here worth trusting. See stats.sh.
 *
 * A write endpoint cannot be authenticated, because it is called by every
 * reader's browser and any secret shipped there is public by the second page
 * view. The Origin allowlist stops other websites but not curl. That is an
 * accepted cost: the worst case is junk rows, and nothing can be read back.
 *
 * What is deliberately not stored: IP, user agent, referrer. The question is
 * how a reader moves through the wheel, and none of those help answer it.
 * Cloudflare sees the IP to route the request; we never write it, and nothing
 * here writes an event into the log either.
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
      return new Response(String(rows.length),
        { status: 202, headers: { ...cors(ok), "Cache-Control": "no-store" } });
    }

    return new Response("not found", { status: 404, headers: { "Cache-Control": "no-store" } });
  },
};

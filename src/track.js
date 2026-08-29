/* How the wheel gets read.

   Set ENDPOINT to the URL of the bhava-log worker and this starts counting.
   Leave it empty and nothing is sent, nothing is stored, and no id is minted:
   the file is inert until you fill in one line.

   What it records: which wheel was opened, which word was selected and which
   word the reader came from, how long they stayed there, and how much of a
   song actually played. The `from` is the interesting one, because a pile of
   view counts cannot tell you that people arrive at ವಿರಹ from ಪ್ರೀತಿ rather
   than from ಶೃಂಗಾರ, and that is the question.

   What it does not record: no cookies, no IP, no user agent, no referrer, no
   location, nothing typed. The id is a random uuid in localStorage that means
   nothing anywhere else, and a reader who has asked not to be tracked is not
   tracked: Do Not Track and Global Privacy Control are both honoured, and
   `localStorage['bhava.notrack'] = 1` opts out by hand.                     */
(function () {
  const ENDPOINT = "https://bhava-log.rala-search.workers.dev/e";

  const off = !ENDPOINT ||
    navigator.doNotTrack === "1" || window.doNotTrack === "1" ||
    navigator.globalPrivacyControl === true ||
    (() => { try { return localStorage.getItem("bhava.notrack") === "1"; } catch (e) { return true; } })();

  if (off) { window.Track = () => {}; return; }

  const id = () => (crypto.randomUUID ? crypto.randomUUID()
    : String(Math.random()).slice(2) + Date.now().toString(36));

  let aid;
  try {
    aid = localStorage.getItem("bhava.aid");
    if (!aid) { aid = id(); localStorage.setItem("bhava.aid", aid); }
  } catch (e) { aid = id(); }        // private window: a one-visit id is fine
  const sid = id();

  let queue = [], timer = null, first = true;

  function flush() {
    clearTimeout(timer); timer = null;
    if (!queue.length) return;
    // `first` asks the worker to count one visit against the city it sees.
    // That count lands in its own table with no id on the row, so it can
    // never be joined back to what this reader looked at.
    const body = JSON.stringify({ aid, sid, first, ev: queue.splice(0, 60) });
    first = false;
    // sendBeacon survives the page being closed, which is exactly when the
    // last and most interesting events are sitting in the queue
    // text/plain, not application/json, and it matters: application/json is
    // not a CORS-safelisted content type, so the browser would want a preflight
    // first, and sendBeacon cannot preflight. It returns true, queues nothing
    // that survives, and the events vanish without an error anywhere. The
    // worker reads the body as text and parses it itself, so the header is
    // decoration either way.
    const blob = new Blob([body], { type: "text/plain;charset=UTF-8" });
    try {
      if (!navigator.sendBeacon || !navigator.sendBeacon(ENDPOINT, blob))
        fetch(ENDPOINT, { method: "POST", body, keepalive: true,
                          headers: { "content-type": "text/plain;charset=UTF-8" } }).catch(() => {});
    } catch (e) {}
  }

  window.Track = function (t, d) {
    queue.push(Object.assign({ t }, d || {}));
    if (queue.length >= 40) return flush();
    if (!timer) timer = setTimeout(flush, 15000);
  };

  addEventListener("visibilitychange", () => { if (document.visibilityState === "hidden") flush(); });
  addEventListener("pagehide", flush);
})();

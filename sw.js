/* Service worker: make the wheel openable without a network.

   Network first, cache second, deliberately. Cache-first is the usual advice
   and it is wrong here: the whole site is one generated index.html, so a stale
   cache would pin a reader to an old copy of the words for as long as the
   worker lives. This way a reader online always gets the current build, and a
   reader on a train still gets the wheel.

   7aac2d51dfed is replaced at build time with a hash of index.html, so a new
   build is a new cache and the old one is deleted on activate.              */
const CACHE = "bhava-7aac2d51dfed";
const SHELL = ["./", "./index.html", "./assets/icon-192.png", "./assets/icon-512.png"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", e => {
  e.waitUntil(caches.keys()
    .then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  // never touch YouTube or the counter: one must stay live, the other is a
  // POST beacon that has no business in a cache
  if (url.hostname.endsWith("youtube.com") || url.hostname.endsWith("ytimg.com")) return;

  e.respondWith(
    fetch(req)
      .then(res => {
        if (res && res.status === 200 && (url.origin === location.origin ||
            url.hostname.endsWith("gstatic.com") || url.hostname.endsWith("googleapis.com"))) {
          const copy = res.clone();
          caches.open(CACHE).then(c => c.put(req, copy));
        }
        return res;
      })
      .catch(() => caches.match(req).then(hit => hit ||
        (req.mode === "navigate" ? caches.match("./index.html") : undefined)))
  );
});

/* The song behind a word.

   Two players, not one. A crossfade needs the outgoing song still sounding
   while the incoming one comes up, and a single YouTube player can only hold
   one video at a time: loading the next one cuts the last one dead. So there
   are two, they take turns, and each handover is a real fade across.

   Every play is a standard embed on the rights holder's own channel, so the
   artist gets the view. We host no audio and cache nothing.

   `play` takes a chain, most specific first: the word's own song, then the
   song of the word above it, and so on. If an id has gone private or had
   embedding switched off since it was checked, the next one up is tried, which
   is the same fallback the wheel does for a word with no song of its own.   */
(function () {
  const API = "https://www.youtube.com/iframe_api";
  // YouTube will not embed into a page with no real origin. Opened over
  // file:// it answers every request with error 153, so say so plainly.
  const SERVED = /^https?:$/.test(location.protocol);
  const CODES = { 2: "the video id is malformed", 5: "the player failed",
                  100: "the video is gone", 101: "the owner disabled embedding",
                  150: "the owner disabled embedding",
                  153: "no origin: serve the page over http, not file://" };

  const CROSS = 1400, TICK = 60;      // crossfade length, and how often we step
  const listeners = new Set();

  let decks = [], live = 0, ready = false, booted = false;
  let cur = null, err = null, want = null, chain = [], rung = 0;

  const other = () => (live + 1) % 2;
  const esc = s => String(s == null ? "" : s).replace(/[&<>"]/g,
    c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  function boot() {
    if (booted) return;
    booted = true;
    const s = document.createElement("script");
    s.src = API;
    document.head.appendChild(s);
  }

  window.onYouTubeIframeAPIReady = function () {
    decks = [0, 1].map(i => new YT.Player("ytdeck" + i, {
      height: "200", width: "200", videoId: "",
      playerVars: { rel: 0, modestbranding: 1, playsinline: 1, origin: location.origin },
      events: {
        onReady: () => { if (decks.every(d => d && d.loadVideoById)) { ready = true; flush(); } },
        onError: e => { if (i === live) next(CODES[e.data] || "error " + e.data); },
        onStateChange: e => {
          if (i !== live) return;
          if (e.data === YT.PlayerState.ENDED) stop();
          else if (e.data === YT.PlayerState.PLAYING && decks[i].isMuted()) decks[i].unMute();
        }
      }
    }));
  };

  /* -------------------------------------------------------------- fading */
  /* Fix direction and step count up front. Deriving them from the current
     volume each tick overshoots the target, flips, and oscillates forever. */
  function fadeTo(deck, to, ms, done) {
    clearInterval(deck.__fade);
    const from = Math.max(0, Math.min(100, deck.getVolume() || 0));
    if (from === to) { deck.setVolume(to); if (done) done(); return; }
    const steps = Math.max(1, Math.round(ms / TICK));
    let i = 0;
    deck.__fade = setInterval(() => {
      i += 1;
      deck.setVolume(Math.round(from + (to - from) * (i / steps)));
      if (i >= steps) {
        clearInterval(deck.__fade); deck.__fade = null;
        deck.setVolume(to);
        if (done) done();
      }
    }, TICK);
  }

  /* --------------------------------------------------------------- play */
  function flush() { if (want) { const c = want; want = null; start(c); } }

  function play(songs) {
    const list = [].concat(songs).filter(Boolean);
    if (!list.length) return;
    if (!SERVED) {
      cur = list[0].yt;
      err = "ಈ ಪುಟ ಸರ್ವರ್‌ನಿಂದ ತೆರೆಯಬೇಕು · " + CODES[153];
      emit(); return;
    }
    chain = list; rung = 0;
    boot();
    if (!ready) { want = list; cur = list[0].yt; err = null; emit(); return; }
    start(list);
  }

  /* try the next song up the chain when this one will not embed */
  function next(why) {
    if (rung + 1 < chain.length) { rung += 1; start(chain, rung); return; }
    err = "ಈ ಹಾಡು ನುಡಿಯಲಿಲ್ಲ · " + why;
    emit();
  }

  function start(list, at) {
    rung = at || 0;
    const song = list[rung];
    const incoming = decks[other()], outgoing = decks[live];
    cur = song.yt; err = null;

    incoming.loadVideoById({ videoId: song.yt, startSeconds: song.st || 0 });
    incoming.unMute();               // it can arrive muted; volume alone will not save you
    incoming.setVolume(0);
    fadeTo(incoming, 100, CROSS);
    if (outgoing && outgoing.getPlayerState && outgoing.getPlayerState() === 1) {
      fadeTo(outgoing, 0, CROSS, () => outgoing.pauseVideo());
    }
    live = other();
    emit();
  }

  function stop() {
    want = null; chain = []; cur = null; err = null;
    const d = decks[live];
    if (ready && d) fadeTo(d, 0, CROSS / 2, () => d.pauseVideo());
    emit();
  }

  const toggle = songs => {
    const first = [].concat(songs).filter(Boolean)[0];
    return first && cur === first.yt ? stop() : play(songs);
  };
  const playing = id => cur === id;
  const onChange = fn => listeners.add(fn);

  function emit() {
    const deck = document.getElementById("deck");
    if (deck) deck.hidden = !cur;
    listeners.forEach(fn => fn(cur, err));
  }

  /* What the player is actually doing, which is not always what was asked for:
     for a now-playing line, and for checking by hand that a `start` offset
     lands where you meant it to.                                            */
  function now() {
    const d = decks[live];
    if (!ready || !d || d.getPlayerState() === -1) return null;
    const id = ((d.getVideoUrl() || "").match(/[?&]v=([\w-]{11})/) || [])[1] || null;
    return { yt: id, wanted: cur, at: Math.round(d.getCurrentTime()),
             state: d.getPlayerState(), vol: d.getVolume(), muted: d.isMuted(),
             deck: live, rung: rung, error: err,
             // both decks, so a crossfade can be seen to overlap rather than cut
             mix: decks.map(x => [x.getVolume(), x.getPlayerState()]) };
  }

  window.Song = { play, toggle, stop, playing, onChange, now, esc };
})();

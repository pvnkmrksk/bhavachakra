/* The song behind a word.

   Two players, not one. A crossfade needs the outgoing song still sounding
   while the incoming one comes up, and a single YouTube player can only hold
   one video at a time: loading the next one cuts the last one dead. So there
   are two, they take turns, and each handover is a real fade across.

   Every play is a standard embed on the rights holder's own channel, so the
   artist gets the view. We host no audio and cache nothing.

   `play` takes a queue: the word's own songs in the order they are written,
   then its family's, shuffled, then the words above it. Tapping ಕರುಣ does not
   play one song, it opens the whole of ಕರುಣ and keeps going through ಅಳಲು and
   ಸಂಕಟ until you stop it.

   The queue is also the fallback. If an id has gone private or had embedding
   switched off since it was checked, the next entry simply takes its turn, so
   a dead link is a track that never plays rather than a silence.            */
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
  let word = null, since = 0, tail = null;   // what is playing, since when

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

  /* Warm up on the reader's first touch of the page, not on their first tap
     of a word.

     A cross-origin iframe only has user activation if it existed when the
     gesture happened. Booting inside the first tap means the script loads, the
     players are built a second or two later, and by then the tap is over: the
     video loads and refuses to play. The second tap works because the iframes
     are there to receive it. That is the whole of the first-click bug, and it
     only shows on phones because desktop Chrome hands out autoplay far more
     freely.

     Deliberately not on page load: a reader who opens the wheel and never
     touches it never contacts YouTube at all. The first scroll or touch is
     enough of a head start, and almost nobody taps a sector as their very
     first act.                                                              */
  ["pointerdown", "touchstart", "keydown", "scroll"].forEach(e =>
    addEventListener(e, boot, { once: true, passive: true, capture: true }));

  window.onYouTubeIframeAPIReady = function () {
    decks = [0, 1].map(i => new YT.Player("ytdeck" + i, {
      height: "200", width: "200", videoId: "",
      playerVars: { rel: 0, modestbranding: 1, playsinline: 1, origin: location.origin },
      events: {
        onReady: () => { if (decks.every(d => d && d.loadVideoById)) { ready = true; flush(); } },
        onError: e => { if (i === live) next(CODES[e.data] || "error " + e.data); },
        onStateChange: e => {
          if (i !== live) return;
          if (e.data === YT.PlayerState.ENDED) advance();
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
  /* Report the song that is ending before the next one starts. Seconds that
     actually sounded, not seconds the page was open.                        */
  function done() {
    if (!since || !window.Track) { since = 0; return; }
    Track("listen", { k: word, yt: cur, ms: Date.now() - since });
    since = 0;
  }

  function flush() { if (want) { const c = want; want = null; start(c); } }

  function play(songs, forWord) {
    if (forWord !== undefined) word = forWord;
    const list = [].concat(songs).filter(Boolean);
    if (!list.length) return;
    if (!SERVED) {
      cur = list[0].yt;
      err = "ಈ ಪುಟ ಸರ್ವರ್‌ನಿಂದ ತೆರೆಯಬೇಕು · " + CODES[153];
      emit(); return;
    }
    chain = list; rung = 0;
    done();
    boot();
    if (!ready) { want = list; cur = list[0].yt; err = null; emit(); return; }
    start(list);
  }

  /* The next thing in the queue, whether this one ended or never played. */
  function advance(why) {
    if (rung + 1 < chain.length) { rung += 1; start(chain, rung); return; }
    if (why) { err = "ಈ ಹಾಡು ನುಡಿಯಲಿಲ್ಲ · " + why; emit(); }
    else stop();                       // the whole family has played
  }
  const next = advance;

  /* Move on a crossfade's width before the end, so one song reaches into the
     next instead of stopping dead and starting again. Checked on a timer
     rather than scheduled: a paused or buffering player would make any
     schedule set at play time a lie.                                        */
  function watchTail() {
    clearInterval(tail);
    tail = setInterval(() => {
      const d = decks[live];
      if (!ready || !d || d.getPlayerState() !== 1) return;
      const left = d.getDuration() - d.getCurrentTime();
      if (left > 0 && left <= CROSS / 1000 + 0.4) { clearInterval(tail); advance(); }
    }, 1000);
  }

  function start(list, at) {
    rung = at || 0;
    const song = list[rung];
    const incoming = decks[other()], outgoing = decks[live];
    cur = song.yt; err = null;

    if (window.Track) Track("play", { k: word, yt: song.yt });
    since = Date.now();
    incoming.loadVideoById({ videoId: song.yt, startSeconds: song.st || 0 });
    incoming.unMute();               // it can arrive muted; volume alone will not save you
    incoming.setVolume(0);
    fadeTo(incoming, 100, CROSS);
    if (outgoing && outgoing.getPlayerState && outgoing.getPlayerState() === 1) {
      fadeTo(outgoing, 0, CROSS, () => outgoing.pauseVideo());
    }
    live = other();
    watchTail();

    /* If the player came up without activation it will sit in CUED rather than
       play. Ask once more, explicitly: sometimes the gesture is still live and
       this is all it needed.                                                 */
    const deck = incoming;
    setTimeout(() => {
      if (cur === song.yt && deck.getPlayerState && deck.getPlayerState() !== 1) {
        try { deck.playVideo(); } catch (e) {}
      }
    }, 900);

    emit();
  }

  function stop() {
    done();
    clearInterval(tail); tail = null;
    want = null; chain = []; cur = null; err = null;
    const d = decks[live];
    if (ready && d) fadeTo(d, 0, CROSS / 2, () => d.pauseVideo());
    emit();
  }

  // tapping the card while anything from this queue is sounding means stop
  const toggle = (songs, forWord) => {
    const list = [].concat(songs).filter(Boolean);
    const inQueue = cur && list.some(x => x.yt === cur);
    return inQueue ? stop() : play(songs, forWord);
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
             deck: live, rung: rung, queue: chain.length, error: err,
             // both decks, so a crossfade can be seen to overlap rather than cut
             mix: decks.map(x => [x.getVolume(), x.getPlayerState()]) };
  }

  // skip: the next thing in the queue, for a control on the page and for
  // checking by hand that the queue advances without waiting out a song
  window.Song = { play, toggle, stop, skip: () => advance(), playing, onChange, now, esc };
})();

/* Sunburst renderer shared by all three wheels.

   Two rules learned the hard way:

   1. Never use <textPath> for Kannada. It positions each glyph separately along
      the arc, which shatters an akshara into base + vowel sign + ottakshara,
      each rotated on its own. The innermost visible ring is therefore upright
      and never rotated; the outer rings rotate the whole string as one unit.

   2. Do not zoom by scaling the group. A CSS transform needs overflow:visible
      to look right, and then the dimmed rest of the wheel paints over the page.
      Drilling in re-lays-out instead: the chosen sector's children are given
      the full 360 degrees and the radii are recomputed, so the drawing always
      fills exactly the same box and the middle is always the way back out.   */
(function () {
  const SVG = "http://www.w3.org/2000/svg";
  const CX = 400, CY = 400;
  const R_FULL = [96, 186, 262, 352];   // whole wheel: sector, branch, leaf
  const R_ZOOM = [140, 250, 352];       // one sector opened out: branch, leaf
  const FS_FULL = [21, 15, 12];
  const FS_ZOOM = [26, 17];
  // a ring keeps the colour it has on the whole wheel, so opening a sector does
  // not recolour it: mix by the word's real depth, never by where it is drawn
  const MIX = ["100%", "var(--mix-mid)", "var(--mix-leaf)"];
  const INK = ["var(--core-ink)", "var(--mid-ink)", "var(--leaf-ink)"];
  const EASE = t => t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;

  const svg = document.getElementById("wheel");
  const detail = document.getElementById("detail");
  const backBtn = document.getElementById("zoomOut");

  let gRoot, hubDisc, hubText, nodes = [], wheel = null;
  let english = false, focus = null, held = null, anim = null, hot = null;
  let byName = new Map();          // kannada -> node, for restoring a shared link
  let lastSel = null, lastSelAt = 0;   // where the reader came from, and when
  let onChange = () => {};

  const el = (n, a) => {
    const e = document.createElementNS(SVG, n);
    for (const k in a) e.setAttribute(k, a[k]);
    return e;
  };
  const pol = (a, r) => {
    const t = (a - 90) * Math.PI / 180;
    return [CX + r * Math.cos(t), CY + r * Math.sin(t)];
  };
  function arc(a0, a1, r0, r1) {
    if (a1 - a0 < 0.01 || r1 - r0 < 0.01) return "M0 0";
    const big = (a1 - a0) > 180 ? 1 : 0;
    const [x0, y0] = pol(a0, r1), [x1, y1] = pol(a1, r1);
    const [x2, y2] = pol(a1, r0), [x3, y3] = pol(a0, r0);
    return `M${x0} ${y0}A${r1} ${r1} 0 ${big} 1 ${x1} ${y1}` +
           `L${x2} ${y2}A${r0} ${r0} 0 ${big} 0 ${x3} ${y3}Z`;
  }
  const esc = s => String(s == null ? "" : s)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

  /* ------------------------------------------------------------- build */
  function build(w) {
    wheel = w;
    svg.textContent = "";
    nodes = [];
    focus = null; held = null;

    gRoot = el("g", {});
    (function add(list, depth, parent, sector) {
      list.forEach((d, i) => {
        const n = { d, depth, parent, sector: depth === 0 ? i : sector, kids: [] };
        n.cur = { a0: 0, a1: 0, r0: R_FULL[0], r1: R_FULL[0], o: 0 };
        nodes.push(n);
        if (parent) parent.kids.push(n);
        if (d.kids && d.kids.length) add(d.kids, depth + 1, n, n.sector);
      });
    })(w.data, 0, null, 0);

    byName = new Map(nodes.map(n => [n.d.kn, n]));   // for restoring a shared link

    nodes.forEach(n => {
      const g = el("g", { class: "seg", tabindex: "0", role: "button" });
      n.path = el("path", {
        fill: `color-mix(in oklab, var(--${w.id}-${n.sector}) ${MIX[n.depth]}, var(--mixer))`,
        stroke: "var(--ground)", "stroke-width": 1.4, "vector-effect": "non-scaling-stroke" });
      n.text = el("text", { "text-anchor": "middle", "dominant-baseline": "central" });
      n.text.textContent = n.d.kn;
      g.appendChild(n.path); g.appendChild(n.text);
      g.setAttribute("aria-label", `${n.d.kn}, ${n.d.tr}, ${n.d.en}`);
      n.g = g;

      // mouse only: on a touchscreen pointerenter fires while the finger is
      // dragging the page and would swap the panel out mid-scroll
      g.addEventListener("pointerenter", e => {
        if (e.pointerType !== "mouse") return;
        setHot(n); if (!held) show(n);
      });
      g.addEventListener("pointerleave", e => {
        if (e.pointerType === "mouse" && hot === n) setHot(null);
      });
      g.addEventListener("focus", () => show(n));
      g.addEventListener("click", e => {
        e.stopPropagation();
        if (!focus) drill(n, true);   // open the sector first: drilling resets
        show(n); held = n;            // ...then keep the word that was tapped
        // the click is the gesture the browser wants, so the song starts here
        // and never in show(), which also runs on hover
        if (n.d.song && window.Song && !Song.playing(n.d.song.yt))
          Song.play(songChain(n), n.d.kn);
        trackSel(n);
        onChange();
      });
      gRoot.appendChild(g);
    });
    svg.appendChild(gRoot);

    // painted last so it stays above the ring it sits inside: always the way back
    hubDisc = el("circle", { cx: CX, cy: CY, r: R_FULL[0], class: "hubdisc",
      fill: "var(--plate)", stroke: "none" });
    hubDisc.addEventListener("click", e => { e.stopPropagation(); drill(null); });
    svg.appendChild(hubDisc);

    // the hub label lives in the SVG so it scales with the wheel instead of
    // being an HTML overlay sized against the viewport
    hubText = el("g", { class: "hublabel" });
    svg.appendChild(hubText);

    layout(true);
    reset(true);
  }

  /* ------------------------------------------------- geometry per level */
  function targets() {
    const shown = focus ? focus.kids : nodes.filter(n => n.depth === 0);
    const rings = focus ? R_ZOOM : R_FULL;
    const maxLv = rings.length - 2;            // deepest visible level, 0-based
    const base = focus ? focus.depth + 1 : 0;

    const leaves = n => (n.depth - base >= maxLv || !n.kids.length)
      ? 1 : n.kids.reduce((s, k) => s + leaves(k), 0);
    const unit = 360 / (shown.reduce((s, n) => s + leaves(n), 0) || 1);

    // everything starts collapsed into the hub; only the visible subtree opens
    nodes.forEach(n => { n.t = { a0: 0, a1: 0, r0: rings[0], r1: rings[0], o: 0 }; });

    let cursor = 0;
    (function walk(list) {
      list.forEach(n => {
        const lv = n.depth - base, start = cursor;
        if (lv < maxLv && n.kids.length) walk(n.kids);
        else cursor += leaves(n) * unit;
        n.t = { a0: start, a1: cursor, r0: rings[lv], r1: rings[lv + 1], o: 1 };
      });
    })(shown);

    hubDisc.setAttribute("r", rings[0]);
    return rings;
  }

  function draw(n, f) {
    const c = n.cur, t = n.t;
    const g = {
      a0: c.a0 + (t.a0 - c.a0) * f, a1: c.a1 + (t.a1 - c.a1) * f,
      r0: c.r0 + (t.r0 - c.r0) * f, r1: c.r1 + (t.r1 - c.r1) * f,
      o: c.o + (t.o - c.o) * f
    };
    const lift = n === hot ? 4 : 0;
    n.path.setAttribute("d", arc(g.a0, g.a1, g.r0, g.r1 + lift * g.o));
    n.g.style.opacity = g.o;
    n.g.style.pointerEvents = g.o > .5 ? "auto" : "none";
    return g;
  }

  function place(rings) {
    const fs = focus ? FS_ZOOM : FS_FULL;
    const base = focus ? focus.depth + 1 : 0;
    nodes.forEach(n => {
      const t = n.t, lv = n.depth - base;
      if (!t.o) { n.text.textContent = ""; return; }
      n.text.textContent = english ? shortEn(n.d.en) : n.d.kn;
      const mid = (t.a0 + t.a1) / 2, rMid = (t.r0 + t.r1) / 2;
      const [px, py] = pol(mid, rMid);
      const band = t.r1 - t.r0;
      const chord = 2 * rMid * Math.sin(((t.a1 - t.a0) / 2) * Math.PI / 180);
      // upright wherever there is room for it: radial only on the crowded
      // outer rings of the whole wheel, where a word has nowhere else to go
      const upright = focus || lv === 0;
      if (upright) {
        n.text.setAttribute("x", px); n.text.setAttribute("y", py);
        n.text.removeAttribute("transform");
        n.room = Math.min(band, chord) * .9;
      } else {
        let rot = mid - 90; if (mid > 180) rot += 180;
        n.text.removeAttribute("x"); n.text.removeAttribute("y");
        n.text.setAttribute("transform", `translate(${px} ${py}) rotate(${rot})`);
        n.room = band * .86;
      }
      n.text.setAttribute("font-size", fs[lv]);
      n.text.setAttribute("font-weight", n.depth === 0 ? 600 : 500);
      n.text.setAttribute("fill", INK[n.depth]);
      let len = 0;
      try { len = n.text.getComputedTextLength(); } catch (e) { return; }
      if (len > n.room)
        n.text.setAttribute("font-size", Math.max(7.4, fs[lv] * n.room / len).toFixed(2));
    });
  }

  function layout(animate = true) {
    const rings = targets();
    if (anim) cancelAnimationFrame(anim);
    nodes.forEach(n => { n.text.textContent = ""; });
    const t0 = performance.now(), dur = animate ? 420 : 0;
    (function frame(now) {
      const f = dur ? Math.min(1, (now - t0) / dur) : 1;
      const e = EASE(f);
      nodes.forEach(n => { n.cur = draw(n, e); });
      if (f < 1) anim = requestAnimationFrame(frame);
      else { anim = null; nodes.forEach(n => { n.cur = { ...n.t }; }); place(rings); }
    })(t0);
  }

  const sectorOf = n => { while (n && n.depth > 0) n = n.parent; return n; };

  // there are exactly two states: the whole wheel, or one sector opened out.
  // drilling to a branch would give it 360 degrees to share between two leaves.
  function drill(n, quiet) {
    n = sectorOf(n);
    if (focus === n) return;
    focus = n;
    backBtn.hidden = !n;
    if (n) backBtn.textContent = `← ${wheel.name}`;
    layout();
    reset();
    if (!quiet) onChange();
  }

  /* ------------------------------------------------------ detail panel */
  const shortEn = s => s.split(/[,;(:]/)[0].trim();

  function chain(n) { const c = []; for (let x = n; x; x = x.parent) c.unshift(x); return c; }

  function show(n) {
    svg.classList.add("dimmed");
    const line = chain(n);
    nodes.forEach(o => {
      o.g.classList.toggle("on", chain(o).includes(line[0]) &&
        (line.length === 1 || chain(o).includes(line[1]) || o.depth < line.length - 1));
      o.g.classList.toggle("sel", o === n);
    });
    setHub(n.d.kn, n.d.tr, n.d.en, !!focus);
    detail.innerHTML =
      `<div class="crumb">${line.map((x, i) => i === line.length - 1
        ? `<b>${esc(x.d.kn)}</b>`
        : `<span>${esc(x.d.kn)} <i>${esc(x.d.en)}</i></span>`).join("<em>›</em>")}</div>` +
      `<div class="word">${esc(n.d.kn)}</div>` +
      `<div class="rom">${esc(n.d.tr)}</div>` +
      `<div class="means">${esc(n.d.en)}</div>` +
      (n.d.lit ? `<div class="lit">literally, ${esc(n.d.lit)}</div>` : "") +
      (n.d.sthayi ? `<div class="lit">ಸ್ಥಾಯಿಭಾವ · ${esc(n.d.sthayi)}</div>` : "") +
      (n.d.also ? `<div class="also"><h4>ಹೀಗೂ ಹೇಳುತ್ತಾರೆ · also said</h4><ul>` +
        n.d.also.map(a => `<li><b>${esc(a.kn)}</b> <i>${esc(a.tr)}</i> <span>${esc(a.en)}</span></li>`)
          .join("") + `</ul></div>` : "") +
      (n.d.note ? `<p class="note">${n.d.note}</p>` : "") +
      songCard(n.d.song);
    wireSong(n);
  }

  /* A move, not a view. `p` is the word they were on before this one and
     `ms` is how long they stayed there: a pile of view counts cannot tell you
     that readers reach ವಿರಹ from ಪ್ರೀತಿ rather than from ಶೃಂಗಾರ.            */
  function trackSel(n) {
    if (!window.Track) return;
    const now = Date.now();
    Track("sel", { w: wheel.id, k: n.d.kn,
                   p: lastSel, ms: lastSel ? now - lastSelAt : null });
    lastSel = n.d.kn; lastSelAt = now;
  }

  /* --------------------------------------------------------------- song */
  /* Most specific first: this word's song, then the song of the word above it.
     If an id has gone private since it was last checked the player falls to
     the next one, which is the same borrowing the wheel already does for a
     word that never had a song of its own.                                  */
  function songChain(n) {
    const seen = new Set(), out = [];
    for (let x = n; x; x = x.parent) {
      const s = x.d.song;
      if (s && !seen.has(s.yt)) { seen.add(s.yt); out.push(s); }
    }
    return out;
  }

  function songCard(s) {
    if (!s) return "";
    return `<div class="song${s.from ? " borrowed" : ""}">` +
      (s.from ? `<p class="from">ಈ ಪದಕ್ಕೆ ತನ್ನದೇ ಹಾಡಿಲ್ಲ · borrowed from <b>${esc(s.from)}</b></p>` : "") +
      `<button class="play" type="button" aria-pressed="false">
         <img class="art" alt="" loading="lazy" decoding="async"
              src="https://i.ytimg.com/vi/${esc(s.yt)}/mqdefault.jpg">
         <span class="glyph" aria-hidden="true"></span>
         <span class="pt"><b>${esc(s.t)}</b><i>${esc(s.src)}</i></span></button>` +
      `<p class="by">${esc(s.by)}</p>` +
      `<p class="oops" hidden></p>` +
      `<a class="src" href="https://www.youtube.com/watch?v=${esc(s.yt)}&t=${s.st | 0}"
          target="_blank" rel="noopener">ಯೂಟ್ಯೂಬ್‌ನಲ್ಲಿ ಕೇಳಿ · official / rights-holder upload ↗</a>` +
      `</div>`;
  }

  function wireSong(n) {
    const s = n.d.song, b = detail.querySelector(".song .play");
    if (!b || !s || !window.Song) return;
    const oops = detail.querySelector(".song .oops");
    const sync = (id, err) => {
      const on = Song.playing(s.yt);
      b.setAttribute("aria-pressed", String(on));
      b.closest(".song").classList.toggle("on", on);
      if (oops) {
        oops.hidden = !(on && err);
        oops.textContent = on && err ? err : "";
      }
    };
    b.addEventListener("click", () => Song.toggle(songChain(n), n.d.kn));
    Song.onChange(sync);
    sync();
  }

  function state() {
    return { open: focus ? focus.d.kn : "", sel: held ? chain(held).map(x => x.d.kn) : [] };
  }

  // restore what a link asks for, silently: never bounce the URL back out
  function apply(open, sel) {
    const o = open ? byName.get(open) : null;
    drill(o || null, true);          // unknown or absent -> back to the whole wheel
    const leaf = sel && sel.length && byName.get(sel[sel.length - 1]);
    if (leaf) { show(leaf); held = leaf; }
  }

  function setHub(word, rom, en, back) {
    const r = focus ? R_ZOOM[0] : R_FULL[0];
    const room = r * 1.62;                      // chord across the disc, with margin
    hubText.textContent = "";
    const rows = [
      { t: word, size: 34, y: en ? -20 : -6, cls: "hw" },
      { t: rom,  size: 15, y: en ? 6 : 18,   cls: "hr" },
      { t: en,   size: 16, y: 28,            cls: "he" },
      { t: back ? "\u2190" : "", size: 22, y: 56, cls: "hb" }
    ];
    rows.forEach(row => {
      if (!row.t) return;
      const t = el("text", { x: CX, y: CY + row.y, class: row.cls,
        "text-anchor": "middle", "dominant-baseline": "central", "font-size": row.size });
      t.textContent = row.t;
      hubText.appendChild(t);
      let len = 0;
      try { len = t.getComputedTextLength(); } catch (e) { return; }
      if (len > room) t.setAttribute("font-size", Math.max(8, row.size * room / len).toFixed(2));
    });
  }

  // one cheap redraw of just the two wedges whose lift changed
  function setHot(n) {
    if (hot === n) return;
    const was = hot; hot = n;
    [was, n].forEach(x => { if (x && !anim) draw(x, 1); });
  }

  function reset(quiet) {
    held = null; setHot(null);
    svg.classList.remove("dimmed");
    nodes.forEach(o => { o.g.classList.remove("on"); o.g.classList.remove("sel"); });
    if (focus) setHub(focus.d.kn, focus.d.tr, focus.d.en, true);
    else setHub(wheel.hubKn, wheel.hubRom, "", false);
    detail.innerHTML = `<p class="hint">${wheel.hint}</p>`;
    if (!quiet) onChange();
  }

  svg.addEventListener("pointerleave", () => { if (!held) reset(); });
  svg.addEventListener("click", e => { if (e.target === svg) { e.stopPropagation(); drill(null); } });
  document.addEventListener("click", e => {
    // clicking a control, or the panel itself, must not drop the selection
    if (held && !e.target.closest(".bar, .switcher, .detail, .zoomout")) reset();
  });
  document.addEventListener("keydown", e => {
    if (e.key !== "Escape") return;
    if (focus) drill(null); else reset();
  });
  backBtn.addEventListener("click", e => { e.stopPropagation(); drill(null); });

  function setLang(v) {
    english = v;
    place(focus ? R_ZOOM : R_FULL);
    const keep = held;                 // switching script must not lose the word
    reset(true);
    if (keep) { show(keep); held = keep; }
  }

  window.Wheel = { build, setLang, apply, state,
    isEnglish: () => english,
    onChange: fn => { onChange = fn; } };
})();

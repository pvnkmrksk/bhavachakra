/* Sunburst renderer shared by all three wheels.
   Two rules learned the hard way:
   1. Never use <textPath> for Kannada. It positions each glyph separately along
      the arc, which shatters an akshara into base + vowel sign + ottakshara,
      each rotated on its own. Core labels are therefore horizontal, and the two
      outer rings rotate the whole string as a single unit.
   2. Zooming is a transform on the root <g>, not a viewBox tween, so it can be
      handed to CSS and stays smooth on a phone.                               */
(function () {
  const SVG = "http://www.w3.org/2000/svg";
  const CX = 400, CY = 400;
  const R = [96, 186, 262, 352];
  const FS = [20, 14.5, 11.8];
  const MIX = ["100%", "var(--mix-mid)", "var(--mix-leaf)"];

  const svg = document.getElementById("wheel");
  const gRoot = document.createElementNS(SVG, "g");
  const detail = document.getElementById("detail");
  const hub = document.getElementById("hub");
  const hubWord = document.getElementById("hubWord");
  const hubRom = document.getElementById("hubRom");
  const backBtn = document.getElementById("zoomOut");

  let nodes = [], wheel = null, english = false, focus = null, hoverLock = null;

  const el = (n, a) => {
    const e = document.createElementNS(SVG, n);
    for (const k in a) e.setAttribute(k, a[k]);
    return e;
  };
  const pol = (a, r) => {
    const t = (a - 90) * Math.PI / 180;
    return [CX + r * Math.cos(t), CY + r * Math.sin(t)];
  };
  function arcPath(a0, a1, r0, r1) {
    const big = (a1 - a0) > 180 ? 1 : 0;
    const [x0, y0] = pol(a0, r1), [x1, y1] = pol(a1, r1);
    const [x2, y2] = pol(a1, r0), [x3, y3] = pol(a0, r0);
    return `M${x0} ${y0}A${r1} ${r1} 0 ${big} 1 ${x1} ${y1}L${x2} ${y2}A${r0} ${r0} 0 ${big} 0 ${x3} ${y3}Z`;
  }
  const esc = s => String(s == null ? "" : s)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

  /* ---------------------------------------------------------------- build */
  function build(w) {
    wheel = w;
    svg.textContent = "";
    gRoot.textContent = "";
    nodes = [];
    focus = null;
    hoverLock = null;

    const totalLeaves = w.data.reduce(
      (s, c) => s + c.kids.reduce((t, m) => t + m.kids.length, 0), 0);
    const unit = 360 / totalLeaves;

    let cursor = 0;
    w.data.forEach((core, ci) => {
      const span = core.kids.reduce((t, m) => t + m.kids.length, 0);
      nodes.push({ d: core, ring: 0, a0: cursor * unit, a1: (cursor + span) * unit,
                   hue: ci, core, path: [core] });
      core.kids.forEach(mid => {
        nodes.push({ d: mid, ring: 1, a0: cursor * unit, a1: (cursor + mid.kids.length) * unit,
                     hue: ci, core, path: [core, mid] });
        mid.kids.forEach(leaf => {
          nodes.push({ d: leaf, ring: 2, a0: cursor * unit, a1: (cursor + 1) * unit,
                       hue: ci, core, path: [core, mid, leaf] });
          cursor++;
        });
      });
    });

    svg.appendChild(el("circle", { cx: CX, cy: CY, r: R[0] - 1,
      fill: "var(--plate)", stroke: "var(--rule)", "stroke-width": 1 }));
    svg.appendChild(gRoot);

    nodes.forEach(n => {
      const g = el("g", { class: "seg", tabindex: "0", role: "button" });
      g.style.animationDelay = (0.12 + (n.a0 / 360) * 0.4 + n.ring * 0.04).toFixed(3) + "s";
      g.appendChild(el("path", {
        d: arcPath(n.a0, n.a1, R[n.ring], R[n.ring + 1]),
        fill: `color-mix(in oklab, var(--${w.id}-${n.hue}) ${MIX[n.ring]}, var(--mixer))`,
        stroke: "var(--ground)", "stroke-width": n.ring === 2 ? 1 : 1.6,
        "vector-effect": "non-scaling-stroke"
      }));

      const mid = (n.a0 + n.a1) / 2;
      const rMid = (R[n.ring] + R[n.ring + 1]) / 2;
      const t = el("text", {
        "text-anchor": "middle", "dominant-baseline": "central",
        "font-size": FS[n.ring],
        "font-weight": n.ring === 0 ? 600 : n.ring === 1 ? 550 : 480,
        fill: n.ring === 0 ? "var(--core-ink)"
            : n.ring === 1 ? "var(--mid-ink)" : "var(--leaf-ink)"
      });
      const [px, py] = pol(mid, rMid);
      if (n.ring === 0) {
        // upright, never rotated: the safest possible setting for Kannada
        t.setAttribute("x", px); t.setAttribute("y", py);
        const chord = 2 * rMid * Math.sin(((n.a1 - n.a0) / 2) * Math.PI / 180);
        n.room = Math.min(R[1] - R[0], chord) * 0.88;
      } else {
        let rot = mid - 90; if (mid > 180) rot += 180;
        t.setAttribute("transform", `translate(${px} ${py}) rotate(${rot})`);
        n.room = (R[n.ring + 1] - R[n.ring]) * (n.ring === 1 ? 0.82 : 0.86);
      }
      t.textContent = n.d.kn;
      g.appendChild(t);
      g.setAttribute("aria-label", `${n.d.kn} — ${n.d.tr} — ${n.d.en}`);
      n.g = g; n.text = t;

      g.addEventListener("pointerenter", () => { if (!hoverLock) show(n); });
      g.addEventListener("focus", () => show(n));
      g.addEventListener("click", e => {
        e.stopPropagation();
        show(n); hoverLock = n;
        if (n.ring === 0) zoom(focus === n ? null : n);
        else if (n.ring === 1) zoom(focus === n ? n.path[0] : n);
      });
      gRoot.appendChild(g);
    });

    svg.appendChild(el("circle", { cx: CX, cy: CY, r: R[3], fill: "none",
      stroke: "var(--rule)", "stroke-width": 1, "pointer-events": "none" }));

    fit();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
    setTimeout(fit, 700);
    zoom(null);   // a wheel switch must drop the previous wheel's zoom
    reset();
  }

  function fit() {
    nodes.forEach(n => {
      n.text.setAttribute("font-size", FS[n.ring]);
      let len = 0;
      try { len = n.text.getComputedTextLength(); } catch (e) { return; }
      if (len > n.room)
        n.text.setAttribute("font-size", Math.max(7.4, FS[n.ring] * n.room / len).toFixed(2));
    });
  }

  /* ----------------------------------------------------------- zoom level */
  function wedgeBox(n) {
    let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
    for (let a = n.a0; a <= n.a1 + 0.001; a += Math.min(3, (n.a1 - n.a0) / 8)) {
      for (const r of [R[n.ring], R[3]]) {
        const [x, y] = pol(a, r);
        x0 = Math.min(x0, x); y0 = Math.min(y0, y);
        x1 = Math.max(x1, x); y1 = Math.max(y1, y);
      }
    }
    return { x: (x0 + x1) / 2, y: (y0 + y1) / 2, w: x1 - x0, h: y1 - y0 };
  }

  function zoom(n) {
    focus = n;
    if (!n) {
      gRoot.style.transform = "";
      svg.classList.remove("zoomed");
      backBtn.hidden = true;
      hub.hidden = false;
      return;
    }
    const b = wedgeBox(n);
    const k = Math.min(3.4, Math.max(1.15, Math.min(720 / b.w, 720 / b.h)));
    gRoot.style.transform =
      `translate(${CX}px, ${CY}px) scale(${k}) translate(${-b.x}px, ${-b.y}px)`;
    svg.classList.add("zoomed");
    backBtn.hidden = false;
    backBtn.textContent = n.ring === 1
      ? `← ${english ? n.path[0].en : n.path[0].kn}`
      : "← ಪೂರ್ಣ ಚಕ್ರ · whole wheel";
    hub.hidden = true;
  }

  /* -------------------------------------------------------- detail panel */
  function show(n) {
    svg.classList.add("dimmed");
    nodes.forEach(o => o.g.classList.toggle("on",
      o.core === n.core && (o.ring === 0 || n.ring === 0 || o.path.includes(n.path[1]))));
    hubWord.textContent = n.d.kn;
    hubRom.textContent = n.d.tr;

    const crumb = n.path.map((x, i) =>
      i === n.path.length - 1
        ? `<b>${esc(x.kn)}</b>`
        : `<span>${esc(x.kn)} <i>${esc(x.en)}</i></span>`).join("<em>›</em>");

    detail.innerHTML =
      `<div class="crumb">${crumb}</div>` +
      `<div class="word">${esc(n.d.kn)}</div>` +
      `<div class="rom">${esc(n.d.tr)}</div>` +
      `<div class="means">${esc(n.d.en)}</div>` +
      (n.d.lit ? `<div class="lit">literally, ${esc(n.d.lit)}</div>` : "") +
      (n.d.sthayi ? `<div class="lit">ಸ್ಥಾಯಿಭಾವ · ${esc(n.d.sthayi)}</div>` : "") +
      (n.d.note ? `<p class="note">${n.d.note}</p>` : "");
  }

  function reset() {
    hoverLock = null;
    svg.classList.remove("dimmed");
    nodes.forEach(o => o.g.classList.remove("on"));
    hubWord.textContent = wheel.hubKn;
    hubRom.textContent = wheel.hubRom;
    detail.innerHTML = `<p class="hint">${wheel.hint}</p>`;
  }

  svg.addEventListener("pointerleave", () => { if (!hoverLock) reset(); });
  document.addEventListener("click", () => { if (hoverLock) reset(); });
  document.addEventListener("keydown", e => {
    if (e.key !== "Escape") return;
    if (focus) zoom(focus.ring === 1 ? focus.path[0] : null); else reset();
  });
  backBtn.addEventListener("click", e => {
    e.stopPropagation();
    zoom(focus && focus.ring === 1 ? focus.path[0] : null);
  });

  // Wedge labels take only the first clause of an English gloss — the panel
  // carries the full sense, and "equanimity, or the cold shoulder" shrinks to
  // an illegible 7px if you try to fit all of it into one segment.
  const shortEn = s => s.split(/[,;(]|\s—\s/)[0].trim();

  function setLang(v) {
    english = v;
    nodes.forEach(n => { n.text.textContent = english ? shortEn(n.d.en) : n.d.kn; });
    fit();
    if (focus) zoom(focus);
  }

  window.Wheel = { build, setLang, reset, isEnglish: () => english };
})();

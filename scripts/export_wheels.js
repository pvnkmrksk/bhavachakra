/* Export the three wheels as standalone SVG.

   The per-label font sizes are decided by getComputedTextLength(), a browser
   measurement, so the wheels have to be exported from a real rendering rather
   than redrawn from wheels.json: redrawing would drift.

   The page paints its rings with color-mix() in oklab, which resolves to
   oklab() in the computed style, which rsvg-convert and most other SVG
   consumers do not understand and silently paint black. So every colour is
   pushed through a 1x1 canvas first, which rasterises it to exact sRGB.

   To run: open https://bhava.kutuhula.in in a browser set to the light theme,
   paste this whole file into the console, and answer the download prompts.
   Then put the three files in assets/ and run scripts/export_wheels.sh.      */
(async function () {
  const cv = document.createElement("canvas"); cv.width = cv.height = 1;
  const ctx = cv.getContext("2d", { willReadFrequently: true });
  const memo = new Map();

  function sRGB(v) {
    if (!v) return v;
    v = v.trim();
    if (v === "none" || v.startsWith("#")) return v;
    if (memo.has(v)) return memo.get(v);
    let out = v;
    try {
      ctx.clearRect(0, 0, 1, 1); ctx.fillStyle = "#000"; ctx.fillStyle = v;
      ctx.fillRect(0, 0, 1, 1);
      const d = ctx.getImageData(0, 0, 1, 1).data;
      const hex = "#" + [d[0], d[1], d[2]].map(x => x.toString(16).padStart(2, "0")).join("");
      out = d[3] === 255 ? hex : `rgba(${d[0]},${d[1]},${d[2]},${(d[3] / 255).toFixed(3)})`;
    } catch (e) {}
    memo.set(v, out); return out;
  }

  function snapshot() {
    const live = document.getElementById("wheel"), clone = live.cloneNode(true);
    const L = live.querySelectorAll("*"), C = clone.querySelectorAll("*");
    const KAN = "'Noto Sans Kannada','Anek Kannada','Kannada MN','Nirmala UI',sans-serif";
    for (let i = 0; i < L.length; i++) {
      const cs = getComputedStyle(L[i]), c = C[i];
      c.setAttribute("fill", sRGB(cs.fill));
      const st = cs.stroke;
      if (st && st !== "none") {
        c.setAttribute("stroke", sRGB(st));
        c.setAttribute("stroke-width", cs.strokeWidth);
      }
      const op = parseFloat(cs.opacity);
      if (op < 1) c.setAttribute("opacity", op.toFixed(3));
      if (c.tagName === "text") {
        c.setAttribute("font-family", KAN);
        c.setAttribute("font-size", cs.fontSize);
        c.setAttribute("font-weight", cs.fontWeight);
        if (cs.fontStyle !== "normal") c.setAttribute("font-style", cs.fontStyle);
        c.setAttribute("text-anchor", cs.textAnchor);
      }
      ["class", "style", "tabindex", "role", "aria-label"].forEach(a => c.removeAttribute(a));
      if (op < 0.02) c.remove();          // a ring mid-fade is not part of the picture
    }
    clone.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    clone.setAttribute("width", "800"); clone.setAttribute("height", "800");
    clone.setAttribute("viewBox", "0 0 800 800");
    ["class", "style", "role", "aria-label"].forEach(a => clone.removeAttribute(a));
    const bg = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    bg.setAttribute("width", "800"); bg.setAttribute("height", "800");
    bg.setAttribute("fill", sRGB(getComputedStyle(document.body).backgroundColor));
    clone.insertBefore(bg, clone.firstChild);
    return new XMLSerializer().serializeToString(clone);
  }

  const tabs = [...document.querySelectorAll(".opt")];
  for (const [i, id] of [[0, "bhava"], [1, "odalu"], [2, "rasa"]]) {
    tabs[i].click();
    await new Promise(r => setTimeout(r, 1500));
    await document.fonts.ready;
    await new Promise(r => setTimeout(r, 600));   // the rings animate into place
    const blob = new Blob([snapshot()], { type: "image/svg+xml" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob); a.download = id + ".svg";
    a.click(); URL.revokeObjectURL(a.href);
    console.log("exported", id);
  }
  tabs[2].click();
})();

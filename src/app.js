/* Page shell: wheel switching, the language slider, and the URL.

   The address bar always describes exactly what is on screen, so a link can be
   copied mid-thought and it reopens on the same word:

     #w=rasa                                  a wheel
     #w=rasa&open=ಶೃಂಗಾರ                       a sector opened out
     #w=rasa&open=ಶೃಂಗಾರ&sel=ಶೃಂಗಾರ.ಒಲವು.ಪ್ರೀತಿ  and a word selected
     #w=bhava&lang=en                          labels in English

   Words are their own identifiers rather than row numbers, so a link keeps
   working after words.csv is reordered.                                     */
(function () {
  const stage = document.querySelector(".stage");
  const thumb = document.getElementById("thumb");
  const opts = [...document.querySelectorAll(".opt")];
  const langBtn = document.getElementById("langBtn");
  const lopts = [...document.querySelectorAll(".lopt")];
  let current = -1, restoring = false;

  function paint(i, quiet) {
    if (i === current) return;
    current = i;
    const w = WHEELS[i];
    stage.dataset.wheel = w.id;
    document.getElementById("tag").innerHTML = w.tag;
    document.getElementById("mastTitle").textContent = w.name;
    document.getElementById("mastSub").innerHTML = w.blurb;
    document.getElementById("aboutTitle").innerHTML =
      `${w.aboutTitle} <span class="lat">${w.aboutLat}</span>`;
    document.getElementById("aboutBody").innerHTML = w.about;
    document.getElementById("aboutGrid").innerHTML = w.cards
      .map(c => `<div><h3>${c.h}</h3><p>${c.p}</p></div>`).join("");
    opts.forEach((o, j) => o.setAttribute("aria-selected", String(j === i)));
    thumb.style.transform = `translateX(${i * 100}%)`;
    Wheel.build(w);
    if (Wheel.isEnglish()) Wheel.setLang(true);
    if (!quiet) writeUrl();
  }

  /* ------------------------------------------------------------- url */
  function writeUrl() {
    if (restoring) return;
    const s = Wheel.state();
    const bits = [`w=${WHEELS[current].id}`];
    if (s.open) bits.push("open=" + encodeURIComponent(s.open));
    if (s.sel.length) bits.push("sel=" + s.sel.map(encodeURIComponent).join("."));
    if (Wheel.isEnglish()) bits.push("lang=en");
    history.replaceState(null, "", "#" + bits.join("&"));
  }

  function readUrl() {
    const q = new URLSearchParams(location.hash.replace(/^#/, ""));
    const i = Math.max(0, WHEELS.findIndex(w => w.id === q.get("w")));
    restoring = true;
    paint(i, true);
    const wantEn = q.get("lang") === "en";
    if (wantEn !== Wheel.isEnglish()) toggleLang(wantEn, true);
    Wheel.apply(q.get("open") || "", (q.get("sel") || "").split(".").filter(Boolean));
    restoring = false;
  }

  Wheel.onChange(writeUrl);
  window.addEventListener("hashchange", readUrl);

  /* --------------------------------------------------------- controls */
  opts.forEach(o => o.addEventListener("click", () => paint(+o.dataset.i)));
  document.querySelector(".switcher").addEventListener("keydown", e => {
    if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
    e.preventDefault();
    const next = (current + (e.key === "ArrowRight" ? 1 : WHEELS.length - 1)) % WHEELS.length;
    paint(next); opts[next].focus();
  });

  function toggleLang(on, quiet) {
    langBtn.setAttribute("aria-checked", String(on));
    lopts[0].classList.toggle("on", !on);
    lopts[1].classList.toggle("on", on);
    Wheel.setLang(on);
    if (!quiet) writeUrl();
  }
  langBtn.addEventListener("click", () =>
    toggleLang(langBtn.getAttribute("aria-checked") !== "true"));

  readUrl();
})();

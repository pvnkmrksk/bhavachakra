/* Page shell: wheel switching, the language slider, and the prose that
   changes with each wheel. All three wheels share one renderer. */
(function () {
  const stage = document.querySelector(".stage");
  const thumb = document.getElementById("thumb");
  const opts = [...document.querySelectorAll(".opt")];
  const langBtn = document.getElementById("langBtn");
  const lopts = [...document.querySelectorAll(".lopt")];
  let current = -1;

  function paint(i) {
    if (i === current) return;
    current = i;
    const w = WHEELS[i];
    stage.dataset.wheel = w.id;
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
  }

  opts.forEach(o => o.addEventListener("click", () => paint(+o.dataset.i)));
  document.querySelector(".switcher").addEventListener("keydown", e => {
    if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
    e.preventDefault();
    const next = (current + (e.key === "ArrowRight" ? 1 : WHEELS.length - 1)) % WHEELS.length;
    paint(next); opts[next].focus();
  });

  langBtn.addEventListener("click", () => {
    const on = langBtn.getAttribute("aria-checked") !== "true";
    langBtn.setAttribute("aria-checked", String(on));
    lopts[0].classList.toggle("on", !on);
    lopts[1].classList.toggle("on", on);
    Wheel.setLang(on);
  });

  paint(0);
})();

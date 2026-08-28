(function(){
const SVG="http://www.w3.org/2000/svg";
const cx=400, cy=400;
const R=[96,186,262,352];               // hub edge, core/mid, mid/leaf, outer
const FS=[21,14.5,11.8];                // base font size per ring
const MIX=["100%","var(--mix-mid)","var(--mix-leaf)"];  // share of hue surviving per ring
const svg=document.getElementById("wheel");
const detail=document.getElementById("detail");
const hubWord=document.getElementById("hubWord");
const hubRom=document.getElementById("hubRom");
let english=false, pinned=null;

const totalLeaves=WHEEL.reduce((s,c)=>s+c.kids.reduce((t,m)=>t+m.kids.length,0),0);
const unit=360/totalLeaves;

function pol(a,r){const t=(a-90)*Math.PI/180; return [cx+r*Math.cos(t), cy+r*Math.sin(t)];}
function arcPath(a0,a1,r0,r1){
  const large=(a1-a0)>180?1:0;
  const [x0,y0]=pol(a0,r1),[x1,y1]=pol(a1,r1),[x2,y2]=pol(a1,r0),[x3,y3]=pol(a0,r0);
  return `M${x0} ${y0}A${r1} ${r1} 0 ${large} 1 ${x1} ${y1}L${x2} ${y2}A${r0} ${r0} 0 ${large} 0 ${x3} ${y3}Z`;
}
function el(n,attrs){const e=document.createElementNS(SVG,n); for(const k in attrs) e.setAttribute(k,attrs[k]); return e;}

// ---- build node list with geometry ----
const nodes=[]; let cursor=0;
WHEEL.forEach(core=>{
  const coreLeaves=core.kids.reduce((t,m)=>t+m.kids.length,0);
  const coreA0=cursor*unit, coreA1=(cursor+coreLeaves)*unit;
  nodes.push({d:core, ring:0, a0:coreA0, a1:coreA1, hue:core.hue, core:core, path:[core]});
  core.kids.forEach(mid=>{
    const midA0=cursor*unit, midA1=(cursor+mid.kids.length)*unit;
    nodes.push({d:mid, ring:1, a0:midA0, a1:midA1, hue:core.hue, core:core, path:[core,mid]});
    mid.kids.forEach(leaf=>{
      nodes.push({d:leaf, ring:2, a0:cursor*unit, a1:(cursor+1)*unit, hue:core.hue, core:core, path:[core,mid,leaf]});
      cursor++;
    });
  });
});

// ---- render ----
const gRoot=el("g",{});
svg.appendChild(el("circle",{cx:cx,cy:cy,r:R[0]-1,fill:"var(--plate)",stroke:"var(--rule)","stroke-width":1}));
svg.appendChild(gRoot);
nodes.forEach((n,i)=>{
  const g=el("g",{class:"seg", tabindex:"0", role:"button"});
  g.style.animationDelay=(0.18+ (n.a0/360)*0.55 + n.ring*0.05).toFixed(3)+"s";
  const fill=`color-mix(in oklab, var(--h-${n.hue}) ${MIX[n.ring]}, var(--mixer))`;
  const p=el("path",{d:arcPath(n.a0,n.a1,R[n.ring],R[n.ring+1]), fill:fill,
                     stroke:"var(--ground)", "stroke-width":n.ring===2?1:1.6});
  g.appendChild(p);

  const mid=(n.a0+n.a1)/2, rMid=(R[n.ring]+R[n.ring+1])/2, band=R[n.ring+1]-R[n.ring];
  const t=el("text",{
    "text-anchor":"middle","dominant-baseline":"central",
    "font-size":FS[n.ring], "font-weight":n.ring===0?600:n.ring===1?550:480,
    fill:n.ring===0?"var(--core-ink)":n.ring===1?"var(--mid-ink)":"var(--leaf-ink)"
  });
  if(n.ring===0){
    // core words run along the arc, which gives them far more room than the radial band
    const flip = mid>90 && mid<270;
    const [ax,ay]=pol(flip?n.a1:n.a0, rMid), [bx,by]=pol(flip?n.a0:n.a1, rMid);
    const id="arc"+i;
    gRoot.appendChild(el("path",{id:id, d:`M${ax} ${ay}A${rMid} ${rMid} 0 0 ${flip?0:1} ${bx} ${by}`, fill:"none"}));
    const tp=document.createElementNS(SVG,"textPath");
    tp.setAttribute("href","#"+id); tp.setAttribute("startOffset","50%");
    tp.textContent=n.d.kn; t.appendChild(tp);
    n.tp=tp; n.arcLen=Math.abs(n.a1-n.a0)*Math.PI/180*rMid;
  } else {
    let rot=mid-90; if(mid>180) rot+=180;
    t.setAttribute("transform",`translate(${pol(mid,rMid)[0]} ${pol(mid,rMid)[1]}) rotate(${rot})`);
    t.textContent=n.d.kn;
  }
  g.appendChild(t);
  g.setAttribute("aria-label",`${n.d.kn}, ${n.d.tr}, ${n.d.en}`);
  n.g=g; n.text=t; n.band=band;
  g.addEventListener("pointerenter",()=>{ if(!pinned) activate(n); });
  g.addEventListener("focus",()=>activate(n));
  g.addEventListener("click",e=>{ e.stopPropagation(); pinned = (pinned===n)?null:n; activate(n); });
  gRoot.appendChild(g);
});

svg.appendChild(el("circle",{cx:cx,cy:cy,r:R[3],fill:"none",stroke:"var(--rule)","stroke-width":1,"pointer-events":"none"}));

function fitLabels(){
  nodes.forEach(n=>{
    n.text.setAttribute("font-size",FS[n.ring]);
    const max = n.ring===0 ? n.arcLen*0.78 : n.band*(n.ring===1?0.82:0.86);
    let len=0; try{ len=n.text.getComputedTextLength(); }catch(e){ return; }
    if(len>max) n.text.setAttribute("font-size",Math.max(7.6,FS[n.ring]*max/len).toFixed(2));
  });
}
if(document.fonts && document.fonts.ready) document.fonts.ready.then(fitLabels);
requestAnimationFrame(fitLabels); setTimeout(fitLabels,900);

// ---- interaction ----
const LABEL={direct:"rala's own answer", shaped:"reshaped by ear", gap:"no usable entry"};
const esc=s=>String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
// rala strings and notes are authored here, so limited inline markup is allowed in notes only
function activate(n){
  svg.classList.add("dimmed");
  nodes.forEach(o=>o.g.classList.toggle("on", o.core===n.core &&
    (o.ring===0 || o.path.includes(n.path[1]) || n.ring===0)));
  hubWord.textContent=n.d.kn; hubRom.textContent=n.d.tr;
  const crumb=n.path.map((x,i)=> i===n.path.length-1 ? `<b>${esc(x.kn)}</b>` : esc(x.kn)).join(" › ");
  const rl=(n.d.rala&&n.d.rala.length)
    ? `<div class="rlist">${n.d.rala.map(r=>`<span>${esc(r)}</span>`).join("")}</div>`
    : `<div class="rlist"><span class="none">no results at all</span></div>`;
  detail.innerHTML=
    `<div class="crumb">${crumb}</div>`+
    `<div class="word">${esc(n.d.kn)}</div>`+
    `<div class="rom">${esc(n.d.tr)}</div>`+
    `<div class="src">for English <b>${esc(n.d.en)}</b></div>`+
    `<span class="chip ${n.d.status}">${LABEL[n.d.status]}</span>`+
    `<h4>What rala returned</h4>${rl}`+
    (n.d.note?`<h4>Reading</h4><p class="note">${n.d.note}</p>`:"");
}
function clear(){
  if(pinned) return;
  svg.classList.remove("dimmed");
  nodes.forEach(o=>o.g.classList.remove("on"));
  hubWord.textContent="ಭಾವಚಕ್ರ"; hubRom.textContent="bhāva-cakra";
  detail.innerHTML=`<p class="hint">Hover or tap any segment. Each card shows what rala returned for the English word, and why the Kannada on the wheel is or isn't that.</p>`;
}
svg.addEventListener("pointerleave",clear);
document.addEventListener("click",()=>{ if(pinned){ pinned=null; clear(); } });
document.addEventListener("keydown",e=>{ if(e.key==="Escape"){ pinned=null; clear(); } });

// ---- language toggle ----
const btn=document.getElementById("langToggle");
btn.addEventListener("click",()=>{
  english=!english;
  btn.setAttribute("aria-pressed",String(english));
  btn.textContent=english?"ಕನ್ನಡ ತೋರಿಸು":"Show English";
  nodes.forEach(n=>{ (n.tp||n.text).textContent = english?n.d.en:n.d.kn; });
  fitLabels();
});

// ---- sections ----
document.getElementById("nativeCards").innerHTML=NATIVE.map(w=>
  `<div class="card"><div class="w">${esc(w.kn)}</div><div class="r">${esc(w.tr)}</div><div class="g">${w.gloss}</div></div>`
).join("");
document.getElementById("rasaBody").innerHTML=RASA.map(r=>
  `<tr><td class="k">${esc(r.kn)}</td><td class="t">${esc(r.tr)}</td><td class="e">${esc(r.en)}</td><td class="m">${esc(r.map)}</td></tr>`
).join("");
})();

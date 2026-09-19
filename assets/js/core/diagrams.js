const MERMAID_URL='https://cdn.jsdelivr.net/npm/mermaid@12.0.0/dist/mermaid.esm.min.mjs';
let mermaidPromise=null, renderSeq=0;

function esc(s=''){return String(s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[m]))}
function themeName(){
  const explicit=document.documentElement.dataset.theme;
  if(explicit==='dark') return 'dark';
  if(explicit==='light') return 'base';
  return matchMedia?.('(prefers-color-scheme: dark)').matches?'dark':'base';
}
async function engine(){
  if(!mermaidPromise){
    mermaidPromise=import(MERMAID_URL).then(mod=>{
      const mermaid=mod.default;
      mermaid.initialize({
        startOnLoad:false,
        securityLevel:'strict',
        theme:themeName(),
        look:'classic',
        layout:'dagre',
        fontFamily:'Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif',
        flowchart:{htmlLabels:false,useMaxWidth:true,curve:'basis',nodeSpacing:32,rankSpacing:42},
        sequence:{useMaxWidth:true,wrap:true,diagramMarginX:24,diagramMarginY:18,messageMargin:28}
      });
      return mermaid;
    }).catch(err=>{mermaidPromise=null;throw err});
  }
  return mermaidPromise;
}

export function diagramSection(content,{lessonId=null,courseId=null,placement=null,limit=4}={}){
  let list=lessonId?(content.diagramsByLesson[lessonId]||[]):courseId?(content.diagramsByCourse[courseId]||[]):[];
  if(placement) list=list.filter(d=>d.placement===placement);
  list=list.slice(0,limit);
  if(!list.length) return '';
  return `<div class="diagram-grid">${list.map(d=>`<figure class="diagram-card" data-diagram-id="${esc(d.id)}"><figcaption><span><strong>${esc(d.title)}</strong><small>${esc(d.description||'')}</small></span><span class="badge">SVG · Mermaid</span></figcaption><div class="diagram-stage"><div class="diagram-loading">Diagramm wird gerendert …</div></div><div class="diagram-actions"><button class="btn btn-soft diagram-open" type="button">Vergrößern</button><button class="btn btn-ghost diagram-svg" type="button">SVG speichern</button></div></figure>`).join('')}</div>`;
}

export async function hydrateDiagrams(ctx,root=document){
  const nodes=[...root.querySelectorAll('[data-diagram-id]')].filter(n=>!n.dataset.rendered);
  if(!nodes.length) return;
  let mermaid;
  try{mermaid=await engine()}catch(err){
    nodes.forEach(n=>showFallback(ctx,n,'Diagrammbibliothek derzeit nicht verfügbar.'));
    console.warn('Mermaid konnte nicht geladen werden',err);
    return;
  }
  for(const node of nodes){
    const d=ctx.content.diagramById[node.dataset.diagramId];
    if(!d){showFallback(ctx,node,'Diagrammdefinition fehlt.');continue}
    try{
      const id=`ea-diagram-${++renderSeq}`;
      const {svg,bindFunctions}=await mermaid.render(id,d.definition);
      const stage=node.querySelector('.diagram-stage');
      stage.innerHTML=svg;
      stage.querySelector('svg')?.setAttribute('role','img');
      stage.querySelector('svg')?.setAttribute('aria-label',d.title);
      bindFunctions?.(stage);
      node.dataset.rendered='1';
      node.querySelector('.diagram-open')?.addEventListener('click',()=>openViewer(d,svg));
      node.querySelector('.diagram-svg')?.addEventListener('click',()=>downloadSvg(d,svg));
    }catch(err){
      console.warn('Diagrammfehler',d.id,err);
      showFallback(ctx,node,'Diagramm konnte nicht gerendert werden.');
    }
  }
}

function showFallback(ctx,node,message){
  const d=ctx.content.diagramById[node.dataset.diagramId];
  node.dataset.rendered='error';
  const stage=node.querySelector('.diagram-stage');
  stage.innerHTML=`<div class="diagram-fallback"><strong>${esc(message)}</strong><p>${esc(d?.description||'')}</p><details><summary>Struktur anzeigen</summary><pre>${esc(d?.definition||'')}</pre></details></div>`;
  node.querySelector('.diagram-actions')?.classList.add('hidden');
}

function ensureViewer(){
  let v=document.querySelector('#diagramViewer');
  if(v) return v;
  v=document.createElement('div');
  v.id='diagramViewer';v.className='diagram-viewer hidden';v.setAttribute('role','dialog');v.setAttribute('aria-modal','true');
  v.innerHTML=`<div class="diagram-viewer-shell"><div class="diagram-viewer-head"><div><small>Vektordiagramm</small><h2 id="diagramViewerTitle">Diagramm</h2></div><div class="diagram-viewer-controls"><button type="button" data-zoom="out" class="icon-btn" aria-label="Verkleinern">−</button><button type="button" data-zoom="reset" class="icon-btn" aria-label="Zoom zurücksetzen">1:1</button><button type="button" data-zoom="in" class="icon-btn" aria-label="Vergrößern">+</button><button type="button" data-close class="icon-btn" aria-label="Schließen">×</button></div></div><div class="diagram-viewer-canvas"><div class="diagram-viewer-svg"></div></div><p id="diagramViewerText" class="small muted"></p></div>`;
  document.body.appendChild(v);
  v.addEventListener('click',e=>{if(e.target===v||e.target.closest('[data-close]')) closeViewer()});
  v.addEventListener('keydown',e=>{if(e.key==='Escape') closeViewer()});
  return v;
}
function openViewer(d,svg){
  const v=ensureViewer();v.classList.remove('hidden');v.tabIndex=-1;
  v.querySelector('#diagramViewerTitle').textContent=d.title;
  v.querySelector('#diagramViewerText').textContent=d.description||'';
  const box=v.querySelector('.diagram-viewer-svg');box.innerHTML=svg;box.dataset.scale='1';applyScale(box);
  v.querySelectorAll('[data-zoom]').forEach(b=>b.onclick=()=>{let s=Number(box.dataset.scale||1);if(b.dataset.zoom==='in')s=Math.min(2.5,s+.2);else if(b.dataset.zoom==='out')s=Math.max(.5,s-.2);else s=1;box.dataset.scale=String(s);applyScale(box)});
  document.body.classList.add('modal-open');v.focus();
}
function applyScale(box){const s=Number(box.dataset.scale||1);const svg=box.querySelector('svg');if(svg){svg.style.transform=`scale(${s})`;svg.style.transformOrigin='top left';box.style.minWidth=`${100*s}%`;box.style.minHeight=`${100*s}%`}}
function closeViewer(){document.querySelector('#diagramViewer')?.classList.add('hidden');document.body.classList.remove('modal-open')}
function downloadSvg(d,svg){
  const blob=new Blob([svg],{type:'image/svg+xml;charset=utf-8'}),u=URL.createObjectURL(blob),a=document.createElement('a');
  a.href=u;a.download=(d.id||'ea-diagram')+'.svg';document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(u),1000);
}

export async function preloadDiagramEngine(){
  try{
    const m=await engine();
    await m.render(`ea-preload-flow-${++renderSeq}`,'flowchart LR\nA["EA"] --> B["Architecture"]');
    await m.render(`ea-preload-seq-${++renderSeq}`,'sequenceDiagram\nparticipant A\nparticipant B\nA->>B: Contract');
    return true;
  }catch{return false}
}

const $ = (s, root=document) => root.querySelector(s);
const $$ = (s, root=document) => [...root.querySelectorAll(s)];
const KEYS = {progress:'eaapp.progress.v1', favorites:'eaapp.favorites.v1', notes:'eaapp.notes.v1', recent:'eaapp.recent.v1', seenVersion:'eaapp.seenVersion'};
let catalog = null, searchIndex = null, installPrompt = null, activeCategory = 'Alle';
const app = $('#app');

const store = {
  get(k, fallback={}) { try { return JSON.parse(localStorage.getItem(k)) ?? fallback; } catch { return fallback; } },
  set(k,v){ localStorage.setItem(k, JSON.stringify(v)); }
};
const escapeHtml = s => String(s??'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[m]));
const moduleById = id => catalog?.modules.find(m=>m.id===id);
const progressOf = id => store.get(KEYS.progress,{})[id] || 0;
const isFav = id => (store.get(KEYS.favorites,[])||[]).includes(id);

function toast(msg){ const el=$('#toast'); el.textContent=msg; el.classList.remove('hidden'); clearTimeout(el._t); el._t=setTimeout(()=>el.classList.add('hidden'),2200); }
function setProgress(id, value){ const p=store.get(KEYS.progress,{}); p[id]=Math.max(p[id]||0,Math.min(100,Math.round(value))); store.set(KEYS.progress,p); }
function toggleFav(id){ const f=store.get(KEYS.favorites,[]); const i=f.indexOf(id); if(i>=0)f.splice(i,1);else f.unshift(id); store.set(KEYS.favorites,f); toast(i>=0?'Aus Favoriten entfernt':'Zu Favoriten hinzugefügt'); route(); }
function addRecent(id){ let r=store.get(KEYS.recent,[]); r=r.filter(x=>x!==id); r.unshift(id); store.set(KEYS.recent,r.slice(0,12)); }
function categories(){ return ['Alle',...new Set(catalog.modules.map(m=>m.category))]; }

function card(m){ const p=progressOf(m.id); return `<article class="card">
  <div class="badge">${escapeHtml(m.category)}</div>
  <h3><a href="#module=${encodeURIComponent(m.id)}">${escapeHtml(m.title)}</a></h3>
  <p>${escapeHtml(m.summary)}</p>
  <div>${m.tags.map(t=>`<span class="tag">${escapeHtml(t)}</span>`).join('')}</div>
  <div class="progress" title="${p}% gelesen"><span style="width:${p}%"></span></div>
  <div class="card-footer"><span class="muted small">${m.minutes} Min · ${Math.round(m.words/100)/10}k Wörter</span><button class="btn btn-outline fav-btn" data-id="${m.id}">${isFav(m.id)?'★':'☆'}</button></div>
</article>`; }

function bindCards(){ $$('.fav-btn').forEach(b=>b.onclick=e=>{e.preventDefault();toggleFav(b.dataset.id)}); }
function navActive(name){ $$('.main-nav a').forEach(a=>a.classList.toggle('active',a.dataset.nav===name)); }

function renderHome(){ navActive('home'); const p=store.get(KEYS.progress,{}); const done=Object.values(p).filter(v=>v>=100).length; const started=Object.values(p).filter(v=>v>0).length; const fav=store.get(KEYS.favorites,[]).length; const recent=store.get(KEYS.recent,[]).map(moduleById).filter(Boolean).slice(0,6);
 app.innerHTML=`<section class="hero"><h1>Enterprise Architecture lernen. Strukturiert. Praxisnah.</h1><p>Die gesamte Projektbibliothek für Enterprise Architecture im Behördenkontext – durchsuchbar, offline nutzbar und jederzeit erweiterbar.</p><div class="hero-actions"><a class="btn btn-light" href="#library">Bibliothek öffnen</a><a class="btn btn-outline" style="color:white;border-color:#9db5c8" href="#module=togaf-lernkurs">TOGAF-Lernkurs starten</a></div></section>
 <div class="stats"><div class="stat-card"><div class="stat">${catalog.modules.length}</div><small>Lernmodule</small></div><div class="stat-card"><div class="stat">${started}</div><small>begonnen</small></div><div class="stat-card"><div class="stat">${done}</div><small>abgeschlossen</small></div><div class="stat-card"><div class="stat">${fav}</div><small>Favoriten</small></div></div>
 <section class="section"><div class="section-head"><h2>Kategorien</h2><a href="#library">Alle Module</a></div><div class="grid">${categories().filter(x=>x!=='Alle').map(c=>{const n=catalog.modules.filter(m=>m.category===c).length; return `<a class="card" href="#library?cat=${encodeURIComponent(c)}"><h3>${escapeHtml(c)}</h3><p>${n} Module</p></a>`}).join('')}</div></section>
 <section class="section"><div class="section-head"><h2>Zuletzt geöffnet</h2></div>${recent.length?`<div class="grid">${recent.map(card).join('')}</div>`:`<div class="empty">Noch keine Module geöffnet.</div>`}</section>`; bindCards(); }

function renderLibrary(catFromHash){ navActive('library'); if(catFromHash) activeCategory=catFromHash; const cats=categories(); const mods=activeCategory==='Alle'?catalog.modules:catalog.modules.filter(m=>m.category===activeCategory);
 app.innerHTML=`<div class="section-head"><div><h1>Bibliothek</h1><div class="muted">${catalog.modules.length} Module aus Projektdateien und Lernpfaden.</div></div></div><div class="filters">${cats.map(c=>`<button class="filter ${c===activeCategory?'active':''}" data-cat="${escapeHtml(c)}">${escapeHtml(c)}</button>`).join('')}</div><div class="grid">${mods.map(card).join('')}</div>`;
 $$('.filter').forEach(b=>b.onclick=()=>{activeCategory=b.dataset.cat;renderLibrary()}); bindCards(); }

function renderFavorites(){ navActive('favorites'); const ids=store.get(KEYS.favorites,[]); const mods=ids.map(moduleById).filter(Boolean); app.innerHTML=`<div class="section-head"><div><h1>Favoriten</h1><div class="muted">Deine persönliche Leseliste.</div></div></div>${mods.length?`<div class="grid">${mods.map(card).join('')}</div>`:`<div class="empty">Noch keine Favoriten. Markiere Module mit ☆.</div>`}`; bindCards(); }

function renderProgress(){ navActive('progress'); const p=store.get(KEYS.progress,{}); const mods=catalog.modules.filter(m=>(p[m.id]||0)>0).sort((a,b)=>(p[b.id]||0)-(p[a.id]||0)); const avg=mods.length?Math.round(mods.reduce((s,m)=>s+(p[m.id]||0),0)/mods.length):0;
 app.innerHTML=`<div class="section-head"><div><h1>Lernfortschritt</h1><div class="muted">Fortschritt wird lokal auf diesem Gerät gespeichert.</div></div><div><strong>${avg}%</strong> Ø begonnen</div></div>${mods.length?`<div class="grid">${mods.map(card).join('')}</div>`:`<div class="empty">Öffne ein Modul und beginne zu lesen.</div>`}`; bindCards(); }

function renderAbout(){ navActive('about'); app.innerHTML=`<article class="reader"><h1>Über EA Learnings</h1><p>EA Learnings ist eine statische Progressive Web App für die Enterprise-Architecture-Projektbibliothek. Sie läuft auf GitHub Pages und benötigt keinen Server.</p><h2>Erweiterbares Content-Modell</h2><p>Neue Inhalte werden als Markdown-Datei unter <code>content/modules/</code> oder <code>content/derived/</code> abgelegt und in <code>content/index.json</code> registriert. Dadurch bleibt UI und Inhalt getrennt.</p><h2>Lokale Daten</h2><p>Lernfortschritt, Favoriten und persönliche Notizen liegen ausschließlich im Browser-Storage des Geräts.</p><h2>Updates</h2><p><code>content/version.json</code> enthält die aktuelle Inhaltsversion. Die App prüft beim Start und bei Fokuswechseln auf eine neue Version und zeigt dann einen Aktualisieren-Hinweis.</p><h2>GitHub Pages</h2><p>Die Anwendung nutzt ausschließlich relative Pfade und funktioniert dadurch unter dem Repository-Pfad <code>/eaapp/</code>.</p></article>`; }

function inlineMd(s){ s=escapeHtml(s); s=s.replace(/\[([^\]]+)\]\((https?:\/\/[^)]+)\)/g,'<a href="$2" target="_blank" rel="noopener">$1</a>'); s=s.replace(/`([^`]+)`/g,'<code>$1</code>'); s=s.replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>'); s=s.replace(/\*([^*]+)\*/g,'<em>$1</em>'); return s; }
function renderMarkdown(md){ const lines=md.replace(/\r/g,'').split('\n'); let out=[], inCode=false, code=[], list=null, para=[]; let headings=[];
 const flushPara=()=>{if(para.length){out.push(`<p>${inlineMd(para.join(' '))}</p>`);para=[]}}; const closeList=()=>{if(list){out.push(`</${list}>`);list=null}};
 for(let i=0;i<lines.length;i++){let line=lines[i]; if(line.trim().startsWith('```')){flushPara();closeList(); if(!inCode){inCode=true;code=[]}else{out.push(`<pre><code>${escapeHtml(code.join('\n'))}</code></pre>`);inCode=false} continue;} if(inCode){code.push(line);continue;}
  if(/^\s*$/.test(line)){flushPara();closeList();continue;} if(/^---+$/.test(line.trim())){flushPara();closeList();out.push('<hr>');continue;}
  const hm=line.match(/^(#{1,4})\s+(.+)$/); if(hm){flushPara();closeList();const lvl=hm[1].length;const txt=hm[2].trim();const id='h-'+slugifyJs(txt)+'-'+headings.length;headings.push({lvl,txt,id});out.push(`<h${lvl} id="${id}">${inlineMd(txt)}</h${lvl}>`);continue;}
  if(/^>\s?/.test(line)){flushPara();closeList();out.push(`<blockquote>${inlineMd(line.replace(/^>\s?/,''))}</blockquote>`);continue;}
  if(/^\|.*\|\s*$/.test(line) && i+1<lines.length && /^\|?\s*:?-+/.test(lines[i+1])){flushPara();closeList();let table=[];table.push(line);i+=2;while(i<lines.length && /^\|.*\|\s*$/.test(lines[i])){table.push(lines[i]);i++;}i--;const rows=table.map(r=>r.trim().replace(/^\||\|$/g,'').split('|').map(x=>x.trim()));const head=rows.shift();out.push('<table><thead><tr>'+head.map(c=>`<th>${inlineMd(c)}</th>`).join('')+'</tr></thead><tbody>'+rows.map(r=>'<tr>'+r.map(c=>`<td>${inlineMd(c)}</td>`).join('')+'</tr>').join('')+'</tbody></table>');continue;}
  const ul=line.match(/^\s*[-*+]\s+(.+)$/); const ol=line.match(/^\s*\d+[.)]\s+(.+)$/); if(ul||ol){flushPara();const type=ul?'ul':'ol';if(list!==type){closeList();list=type;out.push(`<${type}>`)}out.push(`<li>${inlineMd((ul||ol)[1])}</li>`);continue;}
  para.push(line.trim()); }
 flushPara();closeList(); if(inCode)out.push(`<pre><code>${escapeHtml(code.join('\n'))}</code></pre>`); return {html:out.join('\n'),headings}; }
function slugifyJs(s){return s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')||'section'}

async function renderModule(id){ const m=moduleById(id); if(!m){app.innerHTML='<div class="empty">Modul nicht gefunden.</div>';return;} addRecent(id); navActive(''); const res=await fetch(m.path); const md=await res.text(); const r=renderMarkdown(md); const source=m.kind==='project-source'?`Projektquelle: ${escapeHtml(m.sourceTitle)}`:'Aus den Projektgesprächen abgeleiteter Lerninhalt';
 app.innerHTML=`<div class="reader-layout"><article class="reader" id="reader"><div class="source-note">${source}</div><div class="reader-actions"><button id="favCurrent" class="btn btn-outline">${isFav(id)?'★ Favorit':'☆ Favorit'}</button><button id="doneCurrent" class="btn btn-primary">Als abgeschlossen markieren</button><a href="#library" class="btn btn-outline">Zur Bibliothek</a></div>${r.html}<section class="notes"><h2>Meine Notizen</h2><textarea id="noteBox" placeholder="Persönliche Notizen zu diesem Modul …"></textarea><div class="small muted">Automatisch lokal gespeichert.</div></section></article><aside class="toc"><strong>Inhalt</strong>${r.headings.filter(h=>h.lvl<=3).map(h=>`<a class="l${h.lvl}" href="#${h.id}" data-anchor="${h.id}">${escapeHtml(h.txt)}</a>`).join('')}</aside></div>`;
 const note=$('#noteBox'); const notes=store.get(KEYS.notes,{}); note.value=notes[id]||''; note.oninput=()=>{const n=store.get(KEYS.notes,{});n[id]=note.value;store.set(KEYS.notes,n)}; $('#favCurrent').onclick=()=>toggleFav(id); $('#doneCurrent').onclick=()=>{setProgress(id,100);toast('Modul abgeschlossen');}; $$('.toc a').forEach(a=>a.onclick=e=>{e.preventDefault();document.getElementById(a.dataset.anchor)?.scrollIntoView({behavior:'smooth'});history.replaceState(null,'',`#module=${encodeURIComponent(id)}`)});
 const onScroll=()=>{const reader=$('#reader'); if(!reader)return; const rect=reader.getBoundingClientRect(); const total=Math.max(1,reader.scrollHeight-window.innerHeight*.55); const top=Math.max(0,-rect.top+100); const pct=Math.min(99,(top/total)*100); if(pct>progressOf(id)) setProgress(id,pct);}; window._moduleScroll && window.removeEventListener('scroll',window._moduleScroll); window._moduleScroll=onScroll;window.addEventListener('scroll',onScroll,{passive:true}); }

function excerpt(text,q){const lower=text.toLowerCase(),i=lower.indexOf(q.toLowerCase());if(i<0)return text.slice(0,220)+' …';const a=Math.max(0,i-90),b=Math.min(text.length,i+160);return (a?'… ':'')+text.slice(a,b)+(b<text.length?' …':'');}
function highlight(s,q){return escapeHtml(s).replace(new RegExp(`(${q.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')})`,'ig'),'<mark>$1</mark>')}
async function renderSearch(q){navActive(''); if(!searchIndex)searchIndex=await (await fetch('content/search-index.json')).json(); const terms=q.trim().toLowerCase().split(/\s+/).filter(Boolean); const results=searchIndex.map(d=>{const hay=(d.title+' '+d.category+' '+d.tags.join(' ')+' '+d.text).toLowerCase();let score=0;for(const t of terms){if(d.title.toLowerCase().includes(t))score+=10;if(d.tags.join(' ').toLowerCase().includes(t))score+=5;score+=(hay.split(t).length-1);}return {...d,score}}).filter(x=>x.score>0).sort((a,b)=>b.score-a.score).slice(0,60);
 app.innerHTML=`<div class="section-head"><div><h1>Suche</h1><div class="muted">${results.length} Treffer für „${escapeHtml(q)}“</div></div></div>${results.length?`<div class="card">${results.map(r=>`<div class="search-result"><div class="badge">${escapeHtml(r.category)}</div><h3><a href="#module=${encodeURIComponent(r.id)}">${highlight(r.title,q)}</a></h3><p>${highlight(excerpt(r.text,terms[0]||q),terms[0]||q)}</p></div>`).join('')}</div>`:`<div class="empty">Keine Treffer gefunden.</div>`}`; }

async function checkVersion(force=false){ try{const v=await (await fetch(`content/version.json?ts=${Date.now()}`,{cache:'no-store'})).json(); $('#contentVersion').textContent=v.version; const seen=localStorage.getItem(KEYS.seenVersion); if(seen && seen!==v.version){$('#updateMessage').textContent=v.message||`Version ${v.version} ist verfügbar.`;$('#updateBanner').classList.remove('hidden');} else if(!seen||force){localStorage.setItem(KEYS.seenVersion,v.version);} }catch{} }
async function hardRefresh(){ try{if('caches'in window){for(const k of await caches.keys())await caches.delete(k)} localStorage.setItem(KEYS.seenVersion,catalog.contentVersion);}finally{location.reload(true)} }

async function route(){ if(!catalog)return; window._moduleScroll && window.removeEventListener('scroll',window._moduleScroll); const raw=location.hash.slice(1)||'home'; if(raw.startsWith('module='))return renderModule(decodeURIComponent(raw.slice(7))); if(raw.startsWith('search='))return renderSearch(decodeURIComponent(raw.slice(7))); if(raw.startsWith('library')){const m=raw.match(/[?&]cat=([^&]+)/);return renderLibrary(m?decodeURIComponent(m[1]):null)} if(raw==='favorites')return renderFavorites(); if(raw==='progress')return renderProgress(); if(raw==='about')return renderAbout(); return renderHome(); }

async function init(){ catalog=await (await fetch('content/index.json')).json(); $('#contentVersion').textContent=catalog.contentVersion; await checkVersion(); window.addEventListener('hashchange',route); $('#globalSearch').addEventListener('input',e=>{const q=e.target.value.trim(); if(q.length>=2){clearTimeout(e.target._t);e.target._t=setTimeout(()=>location.hash='search='+encodeURIComponent(q),220)}}); $('#reloadUpdate').onclick=hardRefresh; window.addEventListener('online',setOnline);window.addEventListener('offline',setOnline);window.addEventListener('focus',()=>checkVersion());setOnline(); route();
 if('serviceWorker'in navigator){navigator.serviceWorker.register('./sw.js').then(reg=>{reg.addEventListener('updatefound',()=>{const nw=reg.installing;nw?.addEventListener('statechange',()=>{if(nw.state==='installed'&&navigator.serviceWorker.controller){$('#updateBanner').classList.remove('hidden')}})})}).catch(()=>{});}
 window.addEventListener('beforeinstallprompt',e=>{e.preventDefault();installPrompt=e;$('#installBtn').classList.remove('hidden')});$('#installBtn').onclick=async()=>{if(!installPrompt)return;installPrompt.prompt();await installPrompt.userChoice;installPrompt=null;$('#installBtn').classList.add('hidden')}; }
function setOnline(){const e=$('#onlineState');const on=navigator.onLine;e.textContent=on?'Online':'Offline';e.classList.toggle('offline',!on)}
init();

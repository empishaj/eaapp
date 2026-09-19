import {$,$$,esc,toast,setActiveNav,routeParams} from './core/utils.js';
import {loadContent} from './core/content.js';
import {initStore,saveState,resetState,logActivity} from './core/store.js';
import {renderDashboard} from './views/dashboard.js';
import {renderAcademy,renderCourse} from './views/academy.js';
import {renderLesson} from './views/lesson.js';
import {renderPractice,renderReview,renderCases,renderCase,renderArtifacts,renderArtifact,renderDiagnostic} from './views/practice.js';
import {renderKnowledge,renderTerm,renderSource} from './views/knowledge.js';
import {renderProfile} from './views/profile.js';
import {renderBSIAcademy,renderBSIModule,renderBSITopic,renderBSICard,renderBSIStudy,renderBSIReview,renderBSIReviewTopic,renderBSIExam} from './views/bsi.js';
import {preloadDiagramEngine} from './core/diagrams.js';

const ROOT=new URL('../../',import.meta.url);
let content,state,saveTimer,latestVersion,installPrompt;
const ctx={get state(){return state},get content(){return content},save:queueSave,log:(t,p)=>{logActivity(state,t,p);queueSave()},applySettings,downloadOffline,clearCaches,replaceState:o=>{for(const k of Object.keys(state))delete state[k];Object.assign(state,o);queueSave()},resetAll};

async function init(){
  try{[content,state]=await Promise.all([loadContent(),initStore()]);latestVersion=content.version.version;$('#versionLabel').textContent=latestVersion;applySettings();bindGlobal();setOnline();await checkVersion();if('serviceWorker'in navigator)navigator.serviceWorker.register(new URL('sw.js',ROOT),{scope:'/eaapp/',updateViaCache:'none'});if(!state.profile.onboarded&&!location.hash)location.hash='onboarding';else if(!location.hash)location.hash=state.lastLocation||'#today';await route();}
  catch(e){console.error(e);$('#app').innerHTML=`<div class="card"><h1>EA Mastery konnte nicht starten</h1><p>${esc(e.message)}</p><button class="btn btn-primary" onclick="location.reload()">Neu laden</button></div>`}
}
function queueSave(){clearTimeout(saveTimer);saveTimer=setTimeout(()=>saveState(state),100)}
function applySettings(){const t=state.settings.theme;document.documentElement.dataset.theme=t==='system'?'':t;document.documentElement.style.setProperty('--font-scale',String(state.settings.fontScale||1))}
function bindGlobal(){window.addEventListener('hashchange',route);window.addEventListener('online',setOnline);window.addEventListener('offline',setOnline);window.addEventListener('focus',checkVersion);window.addEventListener('beforeinstallprompt',e=>{e.preventDefault();installPrompt=e});$('#globalSearchBtn').onclick=openSearch;$('#closeSearch').onclick=closeSearch;$('#searchOverlay').onclick=e=>{if(e.target.id==='searchOverlay')closeSearch()};$('#searchInput').oninput=e=>search(e.target.value);$('#updateNow').onclick=hardRefresh}
function setOnline(){const e=$('#onlineState');e.textContent=navigator.onLine?'Online':'Offline';e.classList.toggle('offline',!navigator.onLine)}
function navFor(p){if(p.course||p.lesson||p.bsimodule||p.bsitopic||p.bsicard||p['bsi-study']||p.page==='bsi')return'academy';if(p.review||p.case||p.artifact||p['bsi-review-topic']||['practice','cases','artifacts','diagnostic','bsi-review','bsi-exam'].includes(p.page))return'practice';if(p.term||p.source||p.knowledge||p.page==='knowledge')return'knowledge';if(p.page==='profile')return'profile';return'today'}
async function route(){if(!content)return;const p=routeParams();state.lastLocation=location.hash||'#today';queueSave();setActiveNav(navFor(p));window.scrollTo({top:0,behavior:'instant'});
  if(p.page==='onboarding')return renderOnboarding();
  if(p.page==='bsi')return renderBSIAcademy(ctx);
  if(p.bsimodule)return renderBSIModule(ctx,p.bsimodule);
  if(p.bsitopic)return renderBSITopic(ctx,p.bsitopic);
  if(p.bsicard)return renderBSICard(ctx,p.bsicard);
  if(p['bsi-study'])return renderBSIStudy(ctx,p['bsi-study']);
  if(p['bsi-review-topic'])return renderBSIReviewTopic(ctx,p['bsi-review-topic']);
  if(p.page==='bsi-review')return renderBSIReview(ctx);
  if(p.page==='bsi-exam')return renderBSIExam(ctx);
  if(p.course)return renderCourse(ctx,p.course);
  if(p.lesson)return renderLesson(ctx,p.lesson);
  if(p.review!==undefined)return renderReview(ctx,p.review||null);
  if(p.case)return renderCase(ctx,p.case);
  if(p.artifact)return renderArtifact(ctx,p.artifact);
  if(p.term)return renderTerm(ctx,p.term);
  if(p.source)return renderSource(ctx,p.source);
  if(p.knowledge)return renderKnowledge(ctx,p.knowledge);
  if(p.page==='today')return renderDashboard(ctx);
  if(p.page==='academy')return renderAcademy(ctx);
  if(p.page==='practice')return renderPractice(ctx);
  if(p.page==='review')return renderReview(ctx);
  if(p.page==='cases')return renderCases(ctx);
  if(p.page==='artifacts')return renderArtifacts(ctx);
  if(p.page==='diagnostic')return renderDiagnostic(ctx);
  if(p.page==='knowledge')return renderKnowledge(ctx);
  if(p.page==='profile')return renderProfile(ctx);
  location.hash='today';
}
function renderOnboarding(){setActiveNav('today');$('#app').innerHTML=`<section class="hero" style="max-width:850px;margin:5vh auto"><div class="eyebrow">EA Mastery 5.3</div><h1>Enterprise Architecture und BSI IT-Grundschutz – von den Grundlagen bis zur professionellen Handlungsfähigkeit.</h1><p class="lead">Diese App misst nicht, wie viel du gelesen hast. Sie führt dich durch Erklären, aktives Erinnern, Behördenfälle und professionelle Architekturartefakte.</p><div class="grid-3 section"><div class="card flat"><strong>1 · Verstehen</strong><p class="small muted">Grundlagen, Begriffe, mentale Modelle.</p></div><div class="card flat"><strong>2 · Anwenden</strong><p class="small muted">Fälle, Trade-offs, Reviews.</p></div><div class="card flat"><strong>3 · Liefern</strong><p class="small muted">Artefakte erstellen und verteidigen.</p></div></div><div class="settings-grid"><label class="field"><span>Tägliche Lernzeit</span><select id="onboardGoal"><option>10</option><option selected>20</option><option>30</option><option>45</option><option>60</option></select></label><label class="field"><span>Lernmodus</span><select id="onboardMode"><option value="guided">Geführt – empfohlen</option><option value="free">Frei erkunden</option></select></label></div><div class="hero-actions"><button id="startAcademy" class="btn btn-primary">Akademie starten</button><button id="startDiagnostic" class="btn btn-soft">Mit Level-Check starten</button></div><p class="small muted">Alle Lerndaten bleiben lokal auf deinem Gerät und können exportiert oder zurückgesetzt werden.</p></section>`;$('#startAcademy').onclick=()=>finishOnboarding(false);$('#startDiagnostic').onclick=()=>finishOnboarding(true)}
function finishOnboarding(diag){state.profile.onboarded=true;state.profile.dailyGoal=Number($('#onboardGoal').value);state.profile.mode=$('#onboardMode').value;logActivity(state,'onboarding');queueSave();location.hash=diag?'diagnostic':'today'}
function openSearch(){$('#searchOverlay').classList.remove('hidden');$('#searchInput').value='';$('#searchResults').innerHTML='<div class="empty">Suche in EA-Lerneinheiten, BSI-Karten, Lexikon, Fachbüchern und Projektquellen.</div>';setTimeout(()=>$('#searchInput').focus(),30)}
function closeSearch(){$('#searchOverlay').classList.add('hidden')}
function search(q){q=q.trim().toLowerCase();if(q.length<2){$('#searchResults').innerHTML='<div class="empty">Mindestens zwei Zeichen eingeben.</div>';return}let hits=[];for(const x of content.search){const hay=(x.title+' '+x.meta+' '+x.text).toLowerCase();let score=0;if(x.title.toLowerCase().includes(q))score+=20;if(hay.includes(q))score+=5;if(score)hits.push({...x,score})}for(const theme of content.books)for(const b of theme.books){const hay=(b.title+' '+b.author+' '+b.summary).toLowerCase();if(hay.includes(q))hits.push({kind:'book',id:'',title:b.title,meta:`Buch · ${theme.title}`,text:b.summary,score:8})}for(const a of content.artifactExamples){const hay=(a.title+' '+a.purpose+' '+a.scenario+' '+a.audience.join(' ')).toLowerCase();if(hay.includes(q))hits.push({kind:'artifact',id:a.lessonId,title:a.title,meta:`Artefakt · ${a.label}`,text:a.purpose,score:12})}for(const c of content.bsiCards){const hay=(c.topic+' '+c.front+' '+c.tags.join(' ')).toLowerCase();if(hay.includes(q))hits.push({kind:'bsi',id:c.id,title:c.topic,meta:`BSI · ${c.card_type}`,text:c.front,score:c.topic.toLowerCase().includes(q)?16:7})}hits.sort((a,b)=>b.score-a.score);$('#searchResults').innerHTML=hits.slice(0,35).map(h=>{const href=h.kind==='lesson'?`#lesson=${h.id}`:h.kind==='term'?`#term=${h.id}`:h.kind==='source'?`#source=${h.id}`:h.kind==='artifact'?`#artifact=${h.id}`:h.kind==='bsi'?`#bsicard=${h.id}`:'#knowledge=books';return `<a class="search-result" href="${href}" onclick="document.querySelector('#searchOverlay').classList.add('hidden')"><span class="badge">${esc(h.meta)}</span><strong style="display:block;margin-top:5px">${esc(h.title)}</strong><p class="small muted">${esc((h.text||'').slice(0,220))}</p></a>`}).join('')||'<div class="empty">Keine Treffer.</div>'}
async function checkVersion(){try{const r=await fetch(new URL(`content/version.json?t=${Date.now()}`,ROOT),{cache:'no-store'}),v=await r.json();const seen=localStorage.getItem('eaMasterySeen');if(seen&&seen!==v.version){$('#updateText').textContent=v.message||v.version;$('#updateBanner').classList.remove('hidden')}else if(!seen)localStorage.setItem('eaMasterySeen',v.version)}catch{}}
async function clearCaches(){if(!('caches'in window))return;for(const k of await caches.keys())await caches.delete(k)}
async function hardRefresh(){await clearCaches();localStorage.setItem('eaMasterySeen',latestVersion);location.reload()}
<<<<<<< HEAD
async function downloadOffline(){try{if(navigator.storage?.persist)await navigator.storage.persist();const cache=await caches.open('ea-mastery-v5.4.0');const core=['./','./index.html','./assets/styles.css','./assets/js/app.js','./assets/js/core/content.js','./assets/js/core/store.js','./assets/js/core/srs.js','./assets/js/core/mastery.js','./assets/js/core/utils.js','./assets/js/core/diagrams.js','./assets/js/views/dashboard.js','./assets/js/views/academy.js','./assets/js/views/lesson.js','./assets/js/views/practice.js','./assets/js/views/knowledge.js','./assets/js/views/profile.js','./assets/js/views/bsi.js','./content/curriculum/courses.json','./content/curriculum/lessons.json','./content/practice/cards.json','./content/practice/cases.json','./content/practice/artifacts.json','./content/bsi/bsi_lernkarten_950.json','./content/bsi/bsi_curriculum_map.json','./content/knowledge/lexicon.json','./content/knowledge/books.json','./content/knowledge/sources.json','./content/knowledge/search.json','./content/visuals/diagrams.json'];const urls=[...core,...content.sources.map(s=>'./'+s.path)].map(u=>new URL(u,ROOT).href);let n=0;for(const u of urls){try{await cache.add(u)}catch{}if(++n%10===0)toast(`Offline ${n}/${urls.length}`)}await preloadDiagramEngine();toast('Offline-Paket vollständig – Diagramm-Engine vorgeladen')}catch(e){toast('Offline-Paket konnte nicht vollständig geladen werden')}}
=======
async function downloadOffline(){try{if(navigator.storage?.persist)await navigator.storage.persist();const cache=await caches.open('ea-mastery-v5.3.0');const core=['./','./index.html','./assets/styles.css','./assets/js/app.js','./assets/js/core/content.js','./assets/js/core/store.js','./assets/js/core/srs.js','./assets/js/core/mastery.js','./assets/js/core/utils.js','./assets/js/core/diagrams.js','./assets/js/views/dashboard.js','./assets/js/views/academy.js','./assets/js/views/lesson.js','./assets/js/views/practice.js','./assets/js/views/knowledge.js','./assets/js/views/profile.js','./assets/js/views/bsi.js','./content/curriculum/courses.json','./content/curriculum/lessons.json','./content/practice/cards.json','./content/practice/cases.json','./content/practice/artifacts.json','./content/bsi/bsi_lernkarten_500.json','./content/bsi/bsi_curriculum_map.json','./content/knowledge/lexicon.json','./content/knowledge/books.json','./content/knowledge/sources.json','./content/knowledge/search.json','./content/visuals/diagrams.json'];const urls=[...core,...content.sources.map(s=>'./'+s.path)].map(u=>new URL(u,ROOT).href);let n=0;for(const u of urls){try{await cache.add(u)}catch{}if(++n%10===0)toast(`Offline ${n}/${urls.length}`)}await preloadDiagramEngine();toast('Offline-Paket vollständig – Diagramm-Engine vorgeladen')}catch(e){toast('Offline-Paket konnte nicht vollständig geladen werden')}}
>>>>>>> 7defe2fa0f7b407bc646ef14f72a4d2df23b3530
async function resetAll(){if(!confirm('Wirklich alle Lerndaten, Notizen und Einstellungen löschen?'))return;state=await resetState();await clearCaches();location.hash='onboarding';location.reload()}
init();

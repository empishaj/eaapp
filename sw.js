const CACHE='ea-mastery-v5.1.0';
const CORE=[
  './','./index.html','./manifest.webmanifest','./assets/styles.css','./assets/js/app.js',
  './assets/js/core/content.js','./assets/js/core/store.js','./assets/js/core/srs.js','./assets/js/core/mastery.js','./assets/js/core/utils.js','./assets/js/core/diagrams.js',
  './assets/js/views/dashboard.js','./assets/js/views/academy.js','./assets/js/views/lesson.js','./assets/js/views/practice.js','./assets/js/views/knowledge.js','./assets/js/views/profile.js',
  './content/version.json','./content/curriculum/courses.json','./content/curriculum/lessons.json','./content/visuals/diagrams.json',
  './content/practice/cards.json','./content/practice/cases.json','./content/knowledge/lexicon.json','./content/knowledge/books.json','./content/knowledge/sources.json','./content/knowledge/search.json'
];
self.addEventListener('install',e=>e.waitUntil((async()=>{
  const c=await caches.open(CACHE);
  await Promise.allSettled(CORE.map(u=>c.add(u)));
  await self.skipWaiting();
})()));
self.addEventListener('activate',e=>e.waitUntil((async()=>{
  for(const k of await caches.keys()) if(k!==CACHE) await caches.delete(k);
  await self.clients.claim();
})()));
self.addEventListener('fetch',e=>{
  if(e.request.method!=='GET')return;
  const url=new URL(e.request.url);

  // Mermaid is loaded from jsDelivr and cached after first successful use.
  if(url.hostname==='cdn.jsdelivr.net' && url.pathname.includes('/mermaid@12.0.0/')){
    e.respondWith((async()=>{
      const c=await caches.open(CACHE),hit=await c.match(e.request);
      if(hit)return hit;
      const r=await fetch(e.request);
      if(r.ok)await c.put(e.request,r.clone());
      return r;
    })());
    return;
  }
  if(url.origin!==self.location.origin)return;
  if(e.request.mode==='navigate'){
    e.respondWith(fetch(e.request).then(async r=>{const c=await caches.open(CACHE);c.put('./index.html',r.clone());return r}).catch(()=>caches.match('./index.html')));
    return;
  }
  if(url.pathname.endsWith('/content/version.json')){
    e.respondWith(fetch(e.request,{cache:'no-store'}).catch(()=>caches.match(e.request)));
    return;
  }
  e.respondWith(caches.match(e.request).then(hit=>hit||fetch(e.request).then(async r=>{if(r.ok){const c=await caches.open(CACHE);c.put(e.request,r.clone())}return r})));
});

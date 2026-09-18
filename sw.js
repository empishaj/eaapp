const CACHE='ea-learnings-v2.2.0';
const CORE=['./','./index.html','./manifest.webmanifest','./assets/styles.css','./assets/app.js','./assets/icon-192.png','./assets/icon-512.png','./content/index.json','./content/learning.json','./content/units.json','./content/lexicon.json','./content/search-index.json','./content/version.json'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{const u=new URL(e.request.url);if(e.request.method!=='GET'||u.origin!==location.origin)return;
  if(u.pathname.endsWith('/content/version.json')){e.respondWith(fetch(e.request,{cache:'no-store'}).catch(()=>caches.match(e.request)));return}
  if(u.pathname.includes('/content/')){e.respondWith(caches.open(CACHE).then(async c=>{const cached=await c.match(e.request);const network=fetch(e.request).then(r=>{if(r.ok)c.put(e.request,r.clone());return r}).catch(()=>cached);return cached||network}));return}
  e.respondWith(caches.match(e.request).then(cached=>cached||fetch(e.request).then(r=>{if(r.ok)caches.open(CACHE).then(c=>c.put(e.request,r.clone()));return r}).catch(()=>caches.match('./index.html'))));
});

const CACHE='ea-mastery-v5.0.0';
const CORE=[
  './','./index.html','./manifest.webmanifest','./assets/styles.css','./assets/js/app.js',
  './assets/js/core/content.js','./assets/js/core/store.js','./assets/js/core/srs.js','./assets/js/core/mastery.js','./assets/js/core/utils.js',
  './assets/js/views/dashboard.js','./assets/js/views/academy.js','./assets/js/views/lesson.js','./assets/js/views/practice.js','./assets/js/views/knowledge.js','./assets/js/views/profile.js',
  './content/version.json','./content/curriculum/courses.json','./content/curriculum/lessons.json',
  './content/practice/cards.json','./content/practice/cases.json','./content/knowledge/lexicon.json','./content/knowledge/books.json','./content/knowledge/sources.json','./content/knowledge/search.json'
];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{
  if(e.request.method!=='GET')return;
  const url=new URL(e.request.url);
  if(url.origin!==location.origin)return;
  if(url.pathname.endsWith('/content/version.json')){
    e.respondWith(fetch(e.request).catch(()=>caches.match(e.request))); return;
  }
  e.respondWith(caches.match(e.request).then(hit=>hit||fetch(e.request).then(r=>{const copy=r.clone();caches.open(CACHE).then(c=>c.put(e.request,copy));return r;}).catch(()=>caches.match('./index.html'))));
});

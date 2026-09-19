export const $=(s,r=document)=>r.querySelector(s);
export const $$=(s,r=document)=>[...r.querySelectorAll(s)];
export const clamp=(n,min,max)=>Math.min(max,Math.max(min,n));
export function esc(v=''){return String(v).replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]))}
export function nowIso(){return new Date().toISOString()}
export function dateKey(d=new Date()){return d.toISOString().slice(0,10)}
export function daysFromNow(days){const d=new Date();d.setHours(d.getHours()+days*24);return d.toISOString()}
export function formatDate(iso){if(!iso)return '–';return new Intl.DateTimeFormat('de-DE',{day:'2-digit',month:'2-digit',year:'numeric'}).format(new Date(iso))}
export function formatRelative(iso){if(!iso)return 'jetzt';const ms=new Date(iso)-Date.now();const d=Math.round(ms/86400000);if(d===0)return ms>0?'heute':'fällig';if(d===1)return 'morgen';if(d===-1)return 'gestern';return d>0?`in ${d} Tagen`:`${Math.abs(d)} Tage überfällig`}
export function slug(s=''){return s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')}
export function uniq(a){return [...new Set(a)]}
export function pct(n){return `${Math.round(n)} %`}
export function toast(msg){const e=$('#toast');if(!e)return;e.textContent=msg;e.classList.remove('hidden');clearTimeout(window.__toastT);window.__toastT=setTimeout(()=>e.classList.add('hidden'),2600)}
export function setActiveNav(name){$$('[data-nav]').forEach(a=>a.classList.toggle('active',a.dataset.nav===name))}
export function routeParams(){const raw=location.hash.slice(1)||'today';if(!raw.includes('='))return {page:raw};const p=new URLSearchParams(raw);return Object.fromEntries(p.entries())}
export function md(src=''){
  let s=esc(src).replace(/```([\s\S]*?)```/g,'<pre><code>$1</code></pre>');
  s=s.replace(/^### (.*)$/gm,'<h3>$1</h3>').replace(/^## (.*)$/gm,'<h2>$1</h2>').replace(/^# (.*)$/gm,'<h1>$1</h1>');
  s=s.replace(/\*\*(.*?)\*\*/g,'<strong>$1</strong>').replace(/`([^`]+)`/g,'<code>$1</code>');
  s=s.replace(/^[-*] (.*)$/gm,'<li>$1</li>').replace(/(<li>.*<\/li>\n?)+/g,m=>`<ul>${m}</ul>`);
  s=s.replace(/^> (.*)$/gm,'<blockquote>$1</blockquote>');
  s=s.split(/\n{2,}/).map(b=>/^<(h\d|ul|pre|blockquote)/.test(b)?b:`<p>${b.replace(/\n/g,'<br>')}</p>`).join('');
  return s;
}
export function downloadJSON(name,obj){const blob=new Blob([JSON.stringify(obj,null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000)}

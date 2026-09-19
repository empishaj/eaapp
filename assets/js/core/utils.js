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
  const input=String(src||'').replace(/\r\n?/g,'\n');
  const lines=input.split('\n');
  const out=[];
  const inline=(value='')=>{
    let x=esc(value);
    x=x.replace(/`([^`]+)`/g,'<code>$1</code>');
    x=x.replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>');
    x=x.replace(/\*(.+?)\*/g,'<em>$1</em>');
    return x;
  };
  const tableCells=line=>{
    let t=String(line).trim();
    if(t.startsWith('|'))t=t.slice(1);
    if(t.endsWith('|'))t=t.slice(0,-1);
    return t.split('|').map(c=>c.trim());
  };
  const isTableDivider=line=>/^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$/.test(line||'');
  const isSpecial=(idx)=>{
    const l=lines[idx]||'';
    if(!l.trim())return true;
    if(/^```/.test(l.trim())||/^#{1,4}\s+/.test(l)||/^>\s?/.test(l)||/^[-*+]\s+/.test(l)||/^\d+\.\s+/.test(l)||/^\s*---+\s*$/.test(l))return true;
    if(l.includes('|')&&isTableDivider(lines[idx+1]||''))return true;
    return false;
  };
  let i=0;
  while(i<lines.length){
    const raw=lines[i],line=raw.trimEnd();
    if(!line.trim()){i++;continue}

    if(/^```/.test(line.trim())){
      const lang=line.trim().slice(3).trim();i++;
      const buf=[];
      while(i<lines.length&&!/^```/.test(lines[i].trim())){buf.push(lines[i]);i++}
      if(i<lines.length)i++;
      out.push(`<pre class="content-code"><code${lang?` data-lang="${esc(lang)}"`:''}>${esc(buf.join('\n'))}</code></pre>`);
      continue;
    }

    const hm=line.match(/^(#{1,4})\s+(.*)$/);
    if(hm){const level=hm[1].length;out.push(`<h${level} class="content-heading content-heading-${level}">${inline(hm[2])}</h${level}>`);i++;continue}

    if(line.includes('|')&&isTableDivider(lines[i+1]||'')){
      const headers=tableCells(line);i+=2;
      const rows=[];
      while(i<lines.length&&lines[i].trim()&&lines[i].includes('|')&&!isSpecial(i)){
        rows.push(tableCells(lines[i]));i++;
      }
      const colCount=Math.max(headers.length,...rows.map(r=>r.length));
      const head=headers.map((h,idx)=>`<th scope="col" data-col="${idx+1}">${inline(h)}</th>`).join('');
      const body=rows.map((r,rowIdx)=>`<tr data-row="${rowIdx+1}">${Array.from({length:colCount},(_,idx)=>`<td data-label="${esc(headers[idx]||`Spalte ${idx+1}`)}">${inline(r[idx]||'')}</td>`).join('')}</tr>`).join('');
      out.push(`<div class="content-table-shell" data-columns="${colCount}" role="region" aria-label="Tabelle" tabindex="0"><table class="content-table"><thead><tr>${head}</tr></thead><tbody>${body}</tbody></table></div>`);
      continue;
    }

    if(/^[-*+]\s+/.test(line)){
      const items=[];
      while(i<lines.length&&/^[-*+]\s+/.test(lines[i].trim())){items.push(lines[i].trim().replace(/^[-*+]\s+/,''));i++}
      out.push(`<ul class="content-list">${items.map(x=>`<li>${inline(x)}</li>`).join('')}</ul>`);continue;
    }

    if(/^\d+\.\s+/.test(line.trim())){
      const items=[];
      while(i<lines.length&&/^\d+\.\s+/.test(lines[i].trim())){items.push(lines[i].trim().replace(/^\d+\.\s+/,''));i++}
      out.push(`<ol class="content-list content-list-ordered">${items.map(x=>`<li>${inline(x)}</li>`).join('')}</ol>`);continue;
    }

    if(/^>\s?/.test(line)){
      const buf=[];
      while(i<lines.length&&/^>\s?/.test(lines[i].trim())){buf.push(lines[i].trim().replace(/^>\s?/,''));i++}
      out.push(`<blockquote class="content-callout">${buf.map(inline).join('<br>')}</blockquote>`);continue;
    }

    if(/^\s*---+\s*$/.test(line)){out.push('<hr class="content-rule">');i++;continue}

    const paragraph=[line.trim()];i++;
    while(i<lines.length&&!isSpecial(i)){paragraph.push(lines[i].trim());i++}
    out.push(`<p>${inline(paragraph.join(' '))}</p>`);
  }
  return `<div class="prose-content">${out.join('')}</div>`;
}
export function downloadJSON(name,obj){const blob=new Blob([JSON.stringify(obj,null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000)}

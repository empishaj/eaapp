import {nowIso,dateKey} from './utils.js';
const DB='ea-learnings-local', VERSION=3, STORE='kv';let db;
const DEFAULT={
  schema:6,createdAt:null,updatedAt:null,
  profile:{onboarded:false,dailyGoal:20,mode:'guided',diagnosticDone:false},
  settings:{theme:'system',fontScale:1,autoResume:true},
  lessonProgress:{},cardState:{},caseState:{},artifactState:{},bsiCardState:{},bsiExamHistory:[],bsiExamSession:null,notes:{},favorites:[],activity:[],lastLocation:'#today',migration:{}
};
function open(){return new Promise((res,rej)=>{const q=indexedDB.open(DB,VERSION);q.onupgradeneeded=()=>{const d=q.result;if(!d.objectStoreNames.contains(STORE))d.createObjectStore(STORE)};q.onsuccess=()=>res(q.result);q.onerror=()=>rej(q.error)})}
function get(key){return new Promise((res,rej)=>{const q=db.transaction(STORE,'readonly').objectStore(STORE).get(key);q.onsuccess=()=>res(q.result);q.onerror=()=>rej(q.error)})}
function put(key,v){return new Promise((res,rej)=>{const tx=db.transaction(STORE,'readwrite');tx.objectStore(STORE).put(v,key);tx.oncomplete=()=>res();tx.onerror=()=>rej(tx.error)})}
function merge(base,x){return {...base,...x,profile:{...base.profile,...(x?.profile||{})},settings:{...base.settings,...(x?.settings||{})}}}
function migrateOld(old){
  const n=structuredClone(DEFAULT);n.createdAt=old.createdAt||nowIso();n.migration.from='v4';
  n.settings={...n.settings,...(old.settings||{})};n.notes=old.notes||{};n.favorites=Array.isArray(old.favorites)?old.favorites:Object.keys(old.favorites||{}).filter(k=>old.favorites[k]);
  for(const [id,p] of Object.entries(old.progress||{}))n.lessonProgress[id]={status:p.completed?'completed':'active',completedAt:p.completedAt||null,step:p.completed?5:0,updatedAt:old.updatedAt||nowIso()};
  for(const [id,pct] of Object.entries(old.unitProgress||{})){const done=Number(pct)>=100;n.lessonProgress[id]={...(n.lessonProgress[id]||{}),status:done?'completed':'active',step:done?5:Math.min(4,Math.floor(Number(pct)/20)),completedAt:done?(old.updatedAt||nowIso()):null,updatedAt:old.updatedAt||nowIso()}}
  n.cardState=old.cardState||{};n.activity=old.activity||[];return n;
}
export async function initStore(){db=await open();let s=await get('state');if(!s){const old=await get('memory');s=old?migrateOld(old):structuredClone(DEFAULT)}s=merge(DEFAULT,s);s.createdAt??=nowIso();await put('state',s);return s}
export async function saveState(s){s.updatedAt=nowIso();await put('state',s)}
export async function resetState(){const s=structuredClone(DEFAULT);s.createdAt=nowIso();await put('state',s);return s}
export function logActivity(s,type,payload={}){s.activity.unshift({at:nowIso(),day:dateKey(),type,...payload});s.activity=s.activity.slice(0,500)}

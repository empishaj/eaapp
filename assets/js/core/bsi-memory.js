import {normalizeCardState,reviewCard} from './srs.js';

const iso=()=>new Date().toISOString();
const BASE={
  firstSeenAt:null,lastSeenAt:null,viewCount:0,
  firstReadAt:null,lastReadAt:null,readCount:0,
  firstRatedAt:null,lastRatedAt:null,ratingCount:0,ratingHistory:[]
};

export function normalizeBSIMemory(raw={}){
  const s={...BASE,...normalizeCardState(raw),...raw};
  s.ratingHistory=Array.isArray(raw.ratingHistory)?raw.ratingHistory.slice(-20):[];
  // Migration aus 5.3/5.4: bereits bewertete Karten gelten mindestens als gesehen und gelesen.
  if(s.lastReviewedAt){
    s.firstSeenAt??=s.lastReviewedAt;s.lastSeenAt??=s.lastReviewedAt;
    s.firstReadAt??=s.lastReviewedAt;s.lastReadAt??=s.lastReviewedAt;
    s.firstRatedAt??=s.lastReviewedAt;s.lastRatedAt??=s.lastReviewedAt;
    s.viewCount=Math.max(1,Number(s.viewCount)||0);
    s.readCount=Math.max(1,Number(s.readCount)||0);
    s.ratingCount=Math.max(1,Number(s.ratingCount)||0);
    if(!s.ratingHistory.length&&s.lastRating!==null&&s.lastRating!==undefined)s.ratingHistory=[{at:s.lastReviewedAt,rating:s.lastRating,migrated:true}];
  }
  return s;
}

export function ensureBSIMemory(state,cards){
  state.bsiCardState??={};state.bsiRecentCards??=[];
  let changed=false;
  for(const c of cards){
    const before=state.bsiCardState[c.id];
    const after=normalizeBSIMemory(before||{});
    if(!before||JSON.stringify(before)!==JSON.stringify(after)){state.bsiCardState[c.id]=after;changed=true}
  }
  return changed;
}

export function getBSIMemory(state,id){
  state.bsiCardState??={};
  state.bsiCardState[id]=normalizeBSIMemory(state.bsiCardState[id]||{});
  return state.bsiCardState[id];
}

export function markBSISeen(state,id){
  const s=getBSIMemory(state,id),now=iso();
  const last=s.lastSeenAt?new Date(s.lastSeenAt).getTime():0;
  if(!s.firstSeenAt)s.firstSeenAt=now;
  // Re-render nach einer Bewertung nicht als neuen Besuch zählen.
  if(!last||Date.now()-last>30000)s.viewCount=(s.viewCount||0)+1;
  s.lastSeenAt=now;rememberRecent(state,id);return s;
}

export function markBSIRead(state,id){
  const s=getBSIMemory(state,id),now=iso();
  if(!s.firstReadAt)s.firstReadAt=now;
  s.lastReadAt=now;s.readCount=(s.readCount||0)+1;return s;
}

export function rateBSICard(state,id,rating){
  const previous=getBSIMemory(state,id),now=iso();
  const s={...reviewCard(previous,rating)};
  s.firstSeenAt=previous.firstSeenAt||now;s.lastSeenAt=previous.lastSeenAt||now;s.viewCount=Math.max(1,previous.viewCount||0);
  s.firstReadAt=previous.firstReadAt||now;s.lastReadAt=previous.lastReadAt||now;s.readCount=Math.max(1,previous.readCount||0);
  s.firstRatedAt=previous.firstRatedAt||now;s.lastRatedAt=now;s.ratingCount=(previous.ratingCount||0)+1;
  s.ratingHistory=[...(previous.ratingHistory||[]),{at:now,rating}].slice(-20);
  state.bsiCardState[id]=s;rememberRecent(state,id);return s;
}

export function rememberRecent(state,id,max=50){
  state.bsiRecentCards=Array.isArray(state.bsiRecentCards)?state.bsiRecentCards:[];
  state.bsiRecentCards=[id,...state.bsiRecentCards.filter(x=>x!==id)].slice(0,max);
}

export const wasSeen=s=>Boolean(s?.firstSeenAt);
export const wasRead=s=>Boolean(s?.firstReadAt);
export const wasRated=s=>Boolean((s?.ratingCount||0)>0||s?.firstRatedAt||s?.lastReviewedAt);

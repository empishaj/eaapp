import {daysFromNow} from './utils.js';
export function normalizeCardState(s={}){const n={reps:0,interval:0,ease:2.35,lapses:0,dueAt:new Date(0).toISOString(),lastRating:null,lastReviewedAt:null,...s};if(!s.dueAt&&s.due)n.dueAt=s.due;if(!s.lastReviewedAt&&s.lastSeen)n.lastReviewedAt=s.lastSeen;return n}
export function reviewCard(state,rating){
  const s=normalizeCardState(state); // 0 again,1 hard,2 good,3 easy
  if(rating===0){s.reps=0;s.lapses++;s.interval=.15;s.ease=Math.max(1.5,s.ease-.2)}
  else if(rating===1){s.reps++;s.interval=s.interval<1?1:Math.max(1,Math.round(s.interval*1.25));s.ease=Math.max(1.5,s.ease-.08)}
  else if(rating===2){s.reps++;s.interval=s.interval<1?1:s.interval<2?3:Math.round(s.interval*s.ease);s.ease=Math.min(3.0,s.ease+.03)}
  else {s.reps++;s.interval=s.interval<1?4:Math.round(s.interval*s.ease*1.45);s.ease=Math.min(3.2,s.ease+.1)}
  s.lastRating=rating;s.lastReviewedAt=new Date().toISOString();s.dueAt=daysFromNow(s.interval);return s;
}
export function isDue(s){return !s||!s.dueAt||new Date(s.dueAt)<=new Date()}
export function cardScore(s){if(!s?.lastRating&&s?.lastRating!==0)return 0;const base=[15,45,76,94][s.lastRating];const stability=Math.min(6,s.reps||0)*1.2;return Math.min(100,base+stability)}

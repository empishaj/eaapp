import {cardScore} from './srs.js';
export function lessonMastery(lessonId,state,content){
  const lp=state.lessonProgress[lessonId]||{};const cards=content.cardsByLesson[lessonId]||[];
  const reading=lp.status==='completed'?100:(lp.step?Math.min(85,lp.step*16):0);
  const recall=cards.length?cards.reduce((a,c)=>a+cardScore(state.cardState[c.id]),0)/cards.length:0;
  const cs=state.caseState[lessonId]||{};const applied=cs.bestRating==null?0:[20,50,78,100][cs.bestRating]||0;
  const art=state.artifactState[lessonId]||{};const artifact={none:0,draft:45,reviewed:75,defended:100}[art.status||'none'];
  return Math.round(reading*.15+recall*.35+applied*.2+artifact*.3);
}
export function courseMastery(courseId,state,content){const ls=content.lessons.filter(l=>l.courseId===courseId);return ls.length?Math.round(ls.reduce((a,l)=>a+lessonMastery(l.id,state,content),0)/ls.length):0}
export function overallMastery(state,content){return content.courses.length?Math.round(content.courses.reduce((a,c)=>a+courseMastery(c.id,state,content),0)/content.courses.length):0}
export function masteryLabel(score){if(score>=85)return'Master';if(score>=70)return'Advanced';if(score>=50)return'Practitioner';if(score>=25)return'Foundation';return'Neu'}
export function evidenceLabel(score){if(score>=85)return'professionell belegt';if(score>=70)return'fortgeschritten';if(score>=50)return'anwendbar';if(score>=25)return'Grundlage aufgebaut';return'noch offen'}
export function nextLesson(state,content){
  const priority=['course-01','course-02','course-03','course-04','course-05','course-06','course-07','course-09','course-10','course-12','course-13','course-14','course-08','course-11','course-15','course-16'];
  for(let order=1;order<=6;order++)for(const cid of priority){const l=content.lessons.find(x=>x.courseId===cid&&x.order===order);if(l&&state.lessonProgress[l.id]?.status!=='completed')return l}
  return content.lessons[0];
}
export function streak(state){const days=[...new Set((state.activity||[]).map(x=>x.day))].sort().reverse();if(!days.length)return 0;let n=0,d=new Date();for(let i=0;i<90;i++){const k=d.toISOString().slice(0,10);if(days.includes(k)){n++;d.setDate(d.getDate()-1)}else if(i===0){d.setDate(d.getDate()-1)}else break}return n}

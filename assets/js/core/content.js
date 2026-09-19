const ROOT=new URL('../../../',import.meta.url);
const paths={
  version:'content/version.json',courses:'content/curriculum/courses.json',lessons:'content/curriculum/lessons.json',
  cards:'content/practice/cards.json',cases:'content/practice/cases.json',lexicon:'content/knowledge/lexicon.json',
  books:'content/knowledge/books.json',sources:'content/knowledge/sources.json',search:'content/knowledge/search.json',
  artifacts:'content/practice/artifacts.json',diagrams:'content/visuals/diagrams.json',
<<<<<<< HEAD
  bsiCards:'content/bsi/bsi_lernkarten_950.json',bsiCurriculum:'content/bsi/bsi_curriculum_map.json'
=======
  bsiCards:'content/bsi/bsi_lernkarten_500.json',bsiCurriculum:'content/bsi/bsi_curriculum_map.json'
>>>>>>> 7defe2fa0f7b407bc646ef14f72a4d2df23b3530
};
async function j(path){const r=await fetch(new URL(path,ROOT));if(!r.ok)throw new Error(`${path}: ${r.status}`);return r.json()}
const moduleId=name=>String(name).match(/^(\d+)/)?.[1]||name.toLowerCase().replace(/[^a-z0-9]+/g,'-');
export async function loadContent(){
  const [version,courses,lessons,cards,cases,lexicon,books,sources,search,artifacts,diagrams,bsiCards,bsiCurriculum]=await Promise.all(Object.values(paths).map(j));
  const data={version,courses:courses.courses,stages:courses.stages,lessons:lessons.lessons,cards:cards.cards,cases:cases.cases,lexicon:lexicon.entries||[],books:books.themes||[],sources:sources.sources||[],search:search.items||[],artifactExamples:artifacts.artifacts||[],diagrams:diagrams.diagrams||[],bsiCards:bsiCards.cards||[],bsiBasis:bsiCards.basis||{},bsiVersion:bsiCards.version||'1.0.0',bsiModules:(bsiCurriculum.modules||[]).map(m=>({...m,id:moduleId(m.module)}))};
  data.courseById=Object.fromEntries(data.courses.map(x=>[x.id,x]));
  data.lessonById=Object.fromEntries(data.lessons.map(x=>[x.id,x]));
  data.cardById=Object.fromEntries(data.cards.map(x=>[x.id,x]));
  data.caseById=Object.fromEntries(data.cases.map(x=>[x.id,x]));
  data.termById=Object.fromEntries(data.lexicon.map(x=>[x.id,x]));
  data.sourceById=Object.fromEntries(data.sources.map(x=>[x.id,x]));
  data.diagramById=Object.fromEntries(data.diagrams.map(x=>[x.id,x]));
  data.diagramsByLesson={};data.diagramsByCourse={};for(const d of data.diagrams){if(d.lessonId)(data.diagramsByLesson[d.lessonId]??=[]).push(d);if(d.courseId)(data.diagramsByCourse[d.courseId]??=[]).push(d)}
  data.cardsByLesson={};for(const c of data.cards)(data.cardsByLesson[c.unit]??=[]).push(c);
  data.caseByLesson=Object.fromEntries(data.cases.map(x=>[x.lessonId,x]));
  data.artifactByLesson=Object.fromEntries(data.artifactExamples.map(x=>[x.lessonId,x]));
  data.artifactById=Object.fromEntries(data.artifactExamples.map(x=>[x.id,x]));
  data.bsiCardById=Object.fromEntries(data.bsiCards.map(x=>[x.id,x]));
  data.bsiCardsByTopic={};data.bsiCardsByModule={};
  for(const c of data.bsiCards){(data.bsiCardsByTopic[c.topic_id]??=[]).push(c);const mid=moduleId(c.module);(data.bsiCardsByModule[mid]??=[]).push(c)}
  data.bsiTopicMeta={};
  for(const c of data.bsiCards)if(!data.bsiTopicMeta[c.topic_id])data.bsiTopicMeta[c.topic_id]={id:c.topic_id,title:c.topic,module:c.module,moduleId:moduleId(c.module)};
  return data;
}

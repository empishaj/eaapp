const ROOT=new URL('../../../',import.meta.url);
const paths={
  version:'content/version.json',courses:'content/curriculum/courses.json',lessons:'content/curriculum/lessons.json',
  cards:'content/practice/cards.json',cases:'content/practice/cases.json',lexicon:'content/knowledge/lexicon.json',
  books:'content/knowledge/books.json',sources:'content/knowledge/sources.json',search:'content/knowledge/search.json',diagrams:'content/visuals/diagrams.json'
};
async function j(path){const r=await fetch(new URL(path,ROOT));if(!r.ok)throw new Error(`${path}: ${r.status}`);return r.json()}
export async function loadContent(){
  const [version,courses,lessons,cards,cases,lexicon,books,sources,search,diagrams]=await Promise.all(Object.values(paths).map(j));
  const data={version,courses:courses.courses,stages:courses.stages,lessons:lessons.lessons,cards:cards.cards,cases:cases.cases,lexicon:lexicon.entries||[],books:books.themes||[],sources:sources.sources||[],search:search.items||[],diagrams:diagrams.diagrams||[]};
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
  return data;
}

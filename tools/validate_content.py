from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
def load(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
errors=[]
courses=load('content/curriculum/courses.json')['courses']
lessons=load('content/curriculum/lessons.json')['lessons']
cards=load('content/practice/cards.json')['cards']
cases=load('content/practice/cases.json')['cases']
lex=load('content/knowledge/lexicon.json')['entries']
sources=load('content/knowledge/sources.json')['sources']
books=load('content/knowledge/books.json')['themes']
course_ids={c['id'] for c in courses}; lesson_ids={l['id'] for l in lessons}; source_ids={s['id'] for s in sources}
if len(courses)!=16: errors.append(f'expected 16 courses, got {len(courses)}')
for c in courses:
    ls=sorted([l for l in lessons if l['courseId']==c['id']],key=lambda x:x['order'])
    if [x['order'] for x in ls] != [1,2,3,4,5,6]: errors.append(f'{c["id"]}: stages incomplete')
for l in lessons:
    if l['courseId'] not in course_ids: errors.append(f'lesson {l["id"]}: unknown course')
    for s in l.get('sourceModules',[]):
        if s not in source_ids: errors.append(f'lesson {l["id"]}: unknown source {s}')
    if not l.get('scenario',{}).get('prompt'): errors.append(f'lesson {l["id"]}: missing scenario')
    if not l.get('deliverable'): errors.append(f'lesson {l["id"]}: missing deliverable')
    if len(l.get('connections',[]))<2: errors.append(f'lesson {l["id"]}: insufficient connections')
for c in cards:
    if c['unit'] not in lesson_ids: errors.append(f'card {c["id"]}: unknown lesson')
for c in cases:
    if c['lessonId'] not in lesson_ids: errors.append(f'case {c["id"]}: unknown lesson')
for s in sources:
    if not (ROOT/s['path']).exists(): errors.append(f'source file missing: {s["path"]}')
if len(cards)<400: errors.append('too few cards')
if len(lex)<250: errors.append('too few lexicon entries')
if sum(len(x['books']) for x in books)<150: errors.append('too few book entries')
if errors:
    print('\n'.join('ERROR: '+x for x in errors)); sys.exit(1)
print(f'OK: {len(courses)} courses, {len(lessons)} lessons, {len(cards)} cards, {len(cases)} cases, {len(lex)} terms, {len(sources)} sources, {sum(len(x["books"]) for x in books)} books')

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
diagrams=load('content/visuals/diagrams.json')['diagrams']
bsi=load('content/bsi/bsi_lernkarten_950.json')
bsi_cards=bsi['cards']
bsi_modules=load('content/bsi/bsi_curriculum_map.json')['modules']
course_ids={c['id'] for c in courses}; lesson_ids={l['id'] for l in lessons}; source_ids={s['id'] for s in sources}; diagram_ids={d['id'] for d in diagrams}
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
if len(diagrams)<200: errors.append(f'too few diagrams: {len(diagrams)}')
if len(diagram_ids)!=len(diagrams): errors.append('duplicate diagram ids')
for d in diagrams:
    if d.get('lessonId') and d['lessonId'] not in lesson_ids: errors.append(f'diagram {d["id"]}: unknown lesson')
    if d.get('courseId') and d['courseId'] not in course_ids: errors.append(f'diagram {d["id"]}: unknown course')
    definition=d.get('definition','').strip()
    if not definition: errors.append(f'diagram {d["id"]}: empty definition')
    elif not (definition.startswith('flowchart') or definition.startswith('sequenceDiagram')): errors.append(f'diagram {d["id"]}: unsupported diagram syntax')
if len(cards)<400: errors.append('too few EA cards')
if len(lex)<250: errors.append('too few lexicon entries')
if sum(len(x['books']) for x in books)<150: errors.append('too few book entries')
# BSI academy
if len(bsi_cards)!=950: errors.append(f'expected 950 BSI cards, got {len(bsi_cards)}')
if len(bsi_modules)!=15: errors.append(f'expected 15 BSI modules, got {len(bsi_modules)}')
bsi_ids=[c['id'] for c in bsi_cards]
if len(set(bsi_ids))!=len(bsi_ids): errors.append('duplicate BSI card ids')
topics={c['topic_id'] for c in bsi_cards}
if len(topics)!=83: errors.append(f'expected 83 BSI topics, got {len(topics)}')
exam=[c for c in bsi_cards if c.get('card_type')=='Prüfungsfrage']
if len(exam)<50: errors.append(f'need at least 50 BSI exam cards, got {len(exam)}')
for c in bsi_cards:
    for field in ['topic_id','module','topic','card_type','front','back','sources']:
        if not c.get(field): errors.append(f'BSI card {c.get("id")}: missing {field}')
if errors:
    print('\n'.join('ERROR: '+x for x in errors)); sys.exit(1)
print(f'OK: {len(courses)} EA courses, {len(lessons)} lessons, {len(cards)} EA cards, {len(cases)} cases, {len(lex)} terms, {len(sources)} sources, {sum(len(x["books"]) for x in books)} books, {len(diagrams)} diagrams; BSI: {len(bsi_modules)} modules, {len(topics)} topics, {len(bsi_cards)} cards, {len(exam)} exam cards')

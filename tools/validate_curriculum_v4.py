import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
C=R/'content'
idx=json.load(open(C/'index.json',encoding='utf-8'))
units=json.load(open(C/'units.json',encoding='utf-8'))
learning=json.load(open(C/'learning.json',encoding='utf-8'))
lex=json.load(open(C/'lexicon.json',encoding='utf-8'))
books=json.load(open(C/'books.json',encoding='utf-8'))
errors=[]; warnings=[]
if idx.get('contentVersion')!='4.0.0': errors.append('index version')
if units.get('version')!='4.0.0': errors.append('units version')
if learning.get('version')!='4.0.0': errors.append('learning version')
if lex.get('version')!='4.0.0': errors.append('lexicon version')
if len(units.get('courses',[]))!=16: errors.append('expected 16 courses')
if len(units.get('units',[]))!=96: errors.append('expected 96 units')
if len(learning.get('cards',[]))!=480: errors.append('expected 480 cards')
if len(learning.get('curriculumPaths',[]))!=16: errors.append('expected 16 paths')
if len(books.get('themes',[]))!=16: errors.append('expected 16 book themes')
uid={u['id'] for u in units['units']}; mids={m['id'] for m in idx['modules']}
for p in learning['curriculumPaths']:
    if len(p.get('units',[]))!=6: errors.append(f"path {p['id']} not 6 units")
    for x in p.get('units',[]):
        if x not in uid: errors.append(f'bad path unit {x}')
for u in units['units']:
    if u.get('courseOrder') not in range(1,7): errors.append(f"bad order {u['id']}")
    if len(u.get('literature',[]))<3: warnings.append(f"little literature {u['id']}")
    for m in u.get('sourceModules',[]):
        if m not in mids: errors.append(f"bad source {m} in {u['id']}")
    for r in u.get('relatedUnits',[]):
        if r['id'] not in uid: errors.append(f"bad related {r['id']}")
for c in learning['cards']:
    if c.get('unit') not in uid: errors.append(f"bad card unit {c['id']}")
    if c.get('module') not in mids: errors.append(f"bad card module {c['id']}")
if any(len(e.get('examples',[]))<2 for e in lex['entries']): errors.append('lexicon example coverage <2')
print(f"courses={len(units['courses'])} units={len(uid)} cards={len(learning['cards'])} lexicon={len(lex['entries'])} book_themes={len(books['themes'])}")
if warnings: print('WARN',len(warnings),warnings[:5])
if errors:
    print('ERRORS',len(errors)); print('\n'.join(errors[:50])); sys.exit(1)
print('VALID: EA Learnings 4.0 referentially consistent.')

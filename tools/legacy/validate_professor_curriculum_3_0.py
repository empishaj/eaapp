#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
CONTENT=ROOT/'content'

def load(name):
    return json.loads((CONTENT/name).read_text(encoding='utf-8'))

idx=load('index.json'); learning=load('learning.json'); unit_doc=load('units.json'); lex=load('lexicon.json')
mods={m['id']:m for m in idx['modules']}; units={u['id']:u for u in unit_doc['units']}; cards=learning['cards']; entries=lex['entries']
errors=[]; warnings=[]

if idx.get('contentVersion')!='3.0.0': warnings.append('index contentVersion ist nicht 3.0.0')
if unit_doc.get('version')!='3.0.0': errors.append('units.json hat falsche Version')
if learning.get('version')!='3.0.0': errors.append('learning.json hat falsche Version')
if lex.get('version')!='3.0.0': errors.append('lexicon.json hat falsche Version')
if len(units)!=64: errors.append(f'Erwartet 64 Units, gefunden {len(units)}')
if len(cards)!=256: errors.append(f'Erwartet 256 Cards, gefunden {len(cards)}')
if len(learning.get('curriculumPaths',[]))!=10: errors.append('Erwartet 10 Curriculum-Pfade')

required=['title','track','competency','basis','objectives','core','whyItMatters','mentalModel','narrative','connections','misconceptions','scenario','deliverable','reviewQuestions','socraticQuestions','mastery','sources','relatedUnits']
for uid,u in units.items():
    for k in required:
        if not u.get(k): errors.append(f'{uid}: Feld {k} fehlt/leer')
    for mid in u.get('sourceModules',[]):
        if mid not in mods: errors.append(f'{uid}: unbekanntes Source-Modul {mid}')
    rel=u.get('relatedUnits',[])
    if len(rel)<4: warnings.append(f'{uid}: nur {len(rel)} Related Units')
    for r in rel:
        if r.get('id') not in units: errors.append(f'{uid}: unbekannte Related Unit {r.get("id")}')

for c in cards:
    if c.get('unit') not in units: errors.append(f'Card {c.get("id")}: unbekannte Unit {c.get("unit")}')
    if c.get('module') not in mods: errors.append(f'Card {c.get("id")}: unbekanntes Modul {c.get("module")}')

for p in learning.get('curriculumPaths',[]):
    for uid in p.get('units',[]):
        if uid not in units: errors.append(f'Pfad {p.get("id")}: unbekannte Unit {uid}')

for e in entries:
    for ex in e.get('examples',[]):
        if ex.get('moduleId') and ex['moduleId'] not in mods: errors.append(f'Lexikon {e.get("id")}: unbekanntes Modul {ex["moduleId"]}')
        if ex.get('unitId') and ex['unitId'] not in units: errors.append(f'Lexikon {e.get("id")}: unbekannte Unit {ex["unitId"]}')

print(f'Module: {len(mods)}')
print(f'Professoren-Einheiten: {len(units)}')
print(f'Lernkarten: {len(cards)}')
print(f'Curriculum-Pfade: {len(learning.get("curriculumPaths",[]))}')
print(f'Lexikonbegriffe: {len(entries)}')
print(f'Fehler: {len(errors)} | Warnungen: {len(warnings)}')
for w in warnings[:30]: print('WARN:',w)
for e in errors[:100]: print('ERROR:',e)
if errors: sys.exit(1)
print('VALID: EA Learnings Professoren-Curriculum 3.0 ist referenziell konsistent.')

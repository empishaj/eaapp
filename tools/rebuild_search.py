from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parents[1]
idx=json.loads((ROOT/'content/index.json').read_text(encoding='utf-8'))

def strip_md(text):
    text=re.sub(r'```.*?```',' ',text,flags=re.S)
    text=re.sub(r'!\[[^\]]*\]\([^)]*\)',' ',text)
    text=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',text)
    text=re.sub(r'[#>*_|`~-]+',' ',text)
    return re.sub(r'\s+',' ',text).strip()

search=[]
for m in idx['modules']:
    p=ROOT/m['path']
    if not p.exists():
        raise SystemExit(f'Missing module: {p}')
    text=p.read_text(encoding='utf-8')
    search.append({'id':m['id'],'title':m['title'],'category':m['category'],'tags':m.get('tags',[]),'text':strip_md(text)})
(ROOT/'content/search-index.json').write_text(json.dumps(search,ensure_ascii=False),encoding='utf-8')
print(f'Rebuilt search index for {len(search)} modules')

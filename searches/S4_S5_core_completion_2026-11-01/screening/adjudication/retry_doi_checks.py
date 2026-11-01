import json,time,urllib.request
from pathlib import Path
p=Path('outputs/S4 S5 Core Review/screening/adjudication/doi_registry_checks.json');rows=json.loads(p.read_text(encoding='utf-8'))
for x in rows:
 if '429' not in x.get('error',''):continue
 time.sleep(1)
 try:
  m=json.load(urllib.request.urlopen(x['url'],timeout=15))['message']
  x.update(status='found',**{k:m.get(k) for k in ['DOI','title','author','publisher','container-title','volume','issue','page','article-number','type','resource','relation']});x.pop('error',None)
 except Exception as e:x['error']=str(e)
 p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in x.items() if k not in ['author','resource','relation']},ensure_ascii=False),flush=True)

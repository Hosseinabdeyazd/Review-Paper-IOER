import json,urllib.request,urllib.parse,concurrent.futures
from pathlib import Path
p=Path('outputs/S4 S5 Core Review/screening/adjudication/duplicate_decisions.json')
d=json.loads(p.read_text(encoding='utf-8'))
import csv,zipfile,io
with zipfile.ZipFile(p.parent.parent/'tables/all_records_screening.zip') as z:
 records={r['record_id']:r for r in csv.DictReader(io.TextIOWrapper(z.open('all_records_screening.csv'),encoding='utf-8-sig'))}
jobs=[(k,records[i]['doi']) for k,v in d.items() if v['decision']=='retain_pending_identifier_verification' for i in v['candidate_ids'].split(';')]
def fetch(job):
 group,doi=job;url='https://api.crossref.org/works/'+urllib.parse.quote(doi,safe='')
 try:
  m=json.load(urllib.request.urlopen(url,timeout=30))['message']
  return {'group':group,'supplied_doi':doi,'url':url,'status':'found',**{k:m.get(k) for k in ['DOI','title','author','publisher','container-title','volume','issue','page','article-number','type','resource','relation']}}
 except Exception as e:return {'group':group,'supplied_doi':doi,'url':url,'status':'lookup_failed','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:out=list(pool.map(fetch,jobs))
(p.parent/'doi_registry_checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
for x in out:print(json.dumps({k:v for k,v in x.items() if k not in ['author','resource','relation']},ensure_ascii=False))

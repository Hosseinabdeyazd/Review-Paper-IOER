import csv,json,urllib.request,concurrent.futures,time,hashlib
from pathlib import Path
p=Path('outputs/Manuscript/methods_audit/eligibility');out=p/'broad_retrieval';out.mkdir(exist_ok=True);(out/'pdfs').mkdir(exist_ok=True)
r=list(csv.DictReader((p/'broad_dtu_unique_decisions.csv').open(encoding='utf-8-sig')));updates={x['record_id']:x for x in csv.DictReader((p/'broad_dtu_unclear_adjudication.csv').open(encoding='utf-8-sig'))}
for x in r:
 if x['record_id'] in updates:
  u=updates[x['record_id']];x.update({k:u[k] for k in ['decision','reason','evidence_quote']})
with (p/'broad_dtu_adjudicated_decisions.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=r[0]);w.writeheader();w.writerows(r)
candidates=[x for x in r if x['decision'] in ['retain_fulltext','retain_secondary'] and x['doi']]
def get(url):
 return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'ResearchLiteratureReview/1.0','Accept':'application/json, application/pdf;q=0.9, */*;q=0.1'}),timeout=8)
def run(x):
 log={'record_id':x['record_id'],'doi':x['doi'],'attempts':[],'status':'no_pdf_retrieved'}
 try:
  with get('https://api.crossref.org/works/'+urllib.parse.quote(x['doi'],safe='')) as f:data=json.load(f)['message']
  (out/(x['record_id']+'.json')).write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
  links=[z['URL'] for z in data.get('link',[]) if z.get('content-type')=='application/pdf']
  for url in list(dict.fromkeys(links))[:2]:
   try:
    with get(url) as f:b=f.read(25_000_001)
    if b.startswith(b'%PDF') and len(b)<=25_000_000:
     dest=out/'pdfs'/(x['record_id']+'.pdf');dest.write_bytes(b);log.update(status='pdf_downloaded_unverified_identity',path=str(dest),sha256=hashlib.sha256(b).hexdigest(),url=url);break
    log['attempts'].append({'url':url,'result':'not_pdf_or_too_large'})
   except Exception as e:log['attempts'].append({'url':url,'result':str(e)})
 except Exception as e:log['metadata_error']=str(e)
 return log
print('Candidates with DOI',len(candidates),flush=True)
with (out/'retrieval_log.jsonl').open('w',encoding='utf-8') as f,concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for i,result in enumerate(pool.map(run,candidates)):
  f.write(json.dumps(result,ensure_ascii=False)+'\n');f.flush()
  if (i+1)%20==0 or result['status'].startswith('pdf_'):print(i+1,result['record_id'],result['status'],flush=True)

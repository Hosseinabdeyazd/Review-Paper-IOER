from pathlib import Path
import csv,json,urllib.request,urllib.parse,concurrent.futures,hashlib
p=Path('outputs/Manuscript/methods_audit/eligibility');o=p/'broad_retrieval';m=o/'openalex';m.mkdir(exist_ok=True)
r=[x for x in csv.DictReader((p/'broad_dtu_retrieval_status.csv').open(encoding='utf-8-sig')) if x['retrieval_status']!='fulltext_assessed' and x['doi']]
def job(x):
 z={'record_id':x['record_id'],'doi':x['doi'],'status':'no_pdf_retrieved','attempts':[]}
 try:
  with urllib.request.urlopen('https://api.openalex.org/works/https://doi.org/'+urllib.parse.quote(x['doi'],safe='/'),timeout=10) as f:d=json.load(f)
  (m/(x['record_id']+'.json')).write_text(json.dumps(d,ensure_ascii=False),encoding='utf-8')
  links=list(dict.fromkeys(l['pdf_url'] for l in d.get('locations',[]) if l.get('pdf_url') and l.get('is_oa')))
  z['oa_pdf_candidates']=links
  for u in links[:3]:
   try:
    with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=8) as f:b=f.read(25000001)
    if b.startswith(b'%PDF') and len(b)<25000000:
     dest=o/'pdfs'/(x['record_id']+'.pdf');dest.write_bytes(b);z.update(status='pdf_downloaded_unverified_identity',path=str(dest),url=u,sha256=hashlib.sha256(b).hexdigest());break
    z['attempts'].append({'url':u,'result':'not_pdf'})
   except Exception as e:z['attempts'].append({'url':u,'result':str(e)})
 except Exception as e:z['metadata_error']=str(e)
 return z
print('OA location lookup',len(r),flush=True)
with (o/'retrieval_openalex.jsonl').open('w',encoding='utf-8') as f,concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for i,z in enumerate(pool.map(job,r)):
  f.write(json.dumps(z)+'\n');f.flush()
  if z['status'].startswith('pdf_') or (i+1)%30==0:print(i+1,z['record_id'],z['status'],flush=True)

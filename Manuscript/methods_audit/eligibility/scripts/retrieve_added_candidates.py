from pathlib import Path
import csv,json,urllib.request,urllib.parse,concurrent.futures,hashlib
p=Path('outputs/Manuscript/methods_audit/eligibility');o=p/'broad_retrieval'
r=list(csv.DictReader((p/'broad_dtu_adjudicated_decisions.csv').open(encoding='utf-8-sig')))
r=[x for x in r if x['decision']!='exclude_domain' and x['doi'] and not(o/(x['record_id']+'.json')).exists()]
def job(x):
 z={'record_id':x['record_id'],'doi':x['doi'],'status':'no_pdf_retrieved','attempts':[]}
 try:
  with urllib.request.urlopen('https://api.crossref.org/works/'+urllib.parse.quote(x['doi'],safe=''),timeout=8) as f:d=json.load(f)['message']
  (o/(x['record_id']+'.json')).write_text(json.dumps(d,ensure_ascii=False),encoding='utf-8')
  for l in d.get('link',[]):
   if l.get('content-type') not in ['application/pdf','unspecified']:continue
   try:
    with urllib.request.urlopen(urllib.request.Request(l['URL'],headers={'User-Agent':'Mozilla/5.0'}),timeout=8) as f:b=f.read(25000001)
    if b.startswith(b'%PDF') and len(b)<25000000:
     dest=o/'pdfs'/(x['record_id']+'.pdf');dest.write_bytes(b);z.update(status='pdf_downloaded_unverified_identity',path=str(dest),url=l['URL'],sha256=hashlib.sha256(b).hexdigest());break
    z['attempts'].append({'url':l['URL'],'result':'not_pdf'})
   except Exception as e:z['attempts'].append({'url':l['URL'],'result':str(e)})
 except Exception as e:z['metadata_error']=str(e)
 return z
print('New candidate metadata',len(r),flush=True)
with (o/'retrieval_added_candidates.jsonl').open('w',encoding='utf-8') as f,concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for z in pool.map(job,r):f.write(json.dumps(z)+'\n');f.flush();print(z['record_id'],z['status'],flush=True)

import csv,json,urllib.request,concurrent.futures,hashlib
from pathlib import Path
P=Path('outputs/Manuscript/methods_audit/eligibility/broad_retrieval');O=Path('outputs/Manuscript/completion_review');(O/'recovered').mkdir(exist_ok=True)
rows=[r for r in csv.DictReader((O/'retrieval_evidence_audit.csv').open(encoding='utf8')) if r['audit_status']!='assessed_in_existing_ledger']
def job(r):
 links=[]
 for p in [P/(r['record_id']+'.json'),P/'openalex'/(r['record_id']+'.json')]:
  if not p.exists():continue
  d=json.loads(p.read_text(encoding='utf8'))
  links += [x['URL'] for x in d.get('link',[]) if x.get('content-type')=='application/pdf']
  links += [x['pdf_url'] for x in d.get('locations',[]) if x.get('is_oa') and x.get('pdf_url')]
 z={'record_id':r['record_id'],'doi':r['doi'],'status':'no_cached_pdf_location','attempts':[]}
 for u in list(dict.fromkeys(links))[:3]:
  try:
   with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=10) as f:b=f.read(30000001)
   if b.startswith(b'%PDF') and len(b)<=30000000:
    p=O/'recovered'/(r['record_id']+'.pdf');p.write_bytes(b);z.update(status='downloaded_requires_identity_and_fulltext_review',path=str(p),sha256=hashlib.sha256(b).hexdigest());break
   z['attempts'].append({'url':u,'result':'not_pdf_or_size_limit'})
  except Exception as e:z['attempts'].append({'url':u,'result':str(e)})
 if z['attempts'] and not z['status'].startswith('downloaded'):z['status']='document_retrieval_failed'
 return z
with (O/'recovery_attempts.jsonl').open('w',encoding='utf8') as f,concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for i,z in enumerate(pool.map(job,rows)):
  f.write(json.dumps(z)+'\n');f.flush()
  if (i+1)%20==0 or z['status'].startswith('downloaded'):print(i+1,z['record_id'],z['status'],flush=True)

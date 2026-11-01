"""Validate fresh IEEE/Scopus architecture searches and compare prior local tagging."""
from pathlib import Path
import csv,json,re,hashlib
csv.field_size_limit(100000000)
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'analysis/architecture_focus'
QUERY='"digital twin" AND uncertainty AND (architectur* OR "probabilistic graphical model*" OR "Bayesian network*" OR "knowledge graph*" OR "data assimilation" OR "sensor fusion" OR "uncertainty propagation" OR provenance OR traceability OR "runtime verification")'
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(p,rows):
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
audit={};comparison=[]
for db,folder,count,cols,baseline in [('IEEE','IEEE_Xplore',349,28,'IEEE_DTU_1228.csv'),('SCOPUS','Scopus',1011,45,'SCOPUS_DTU_3501.csv')]:
 raw=ROOT/f'searches/{folder}/DT-UA/results/raw/{db}_DTUA_{count}.csv';rows=read(raw)
 assert len(rows)==count and all(len(r)==cols and None not in r and all(v is not None for v in r.values()) for r in rows)
 def ident(r):
  if db=='SCOPUS':return 'SCOPUS:'+r['EID']
  m=re.search(r'(?:arnumber=|fileName=)(\d+)',r['PDF Link']);assert m
  return 'IEEE:'+m[1]
 records=[{'record_id':ident(r),'source_database':'IEEE Xplore' if db=='IEEE' else 'Scopus','search_id':f'{db}-DTUA-2026-11-01','source_batch':raw.name,'source_csv_row':n,**r} for n,r in enumerate(rows,2)]
 ids={r['record_id'] for r in records};assert len(ids)==count
 base={r['record_id']:r for r in read(ROOT/'data/merged'/baseline)}
 local={r['record_id'] for r in read(OUT/f'{db}_architecture_focus_full_metadata.csv')}
 write(ROOT/f'data/merged/{db}_DTUA_{count}.csv',records)
 title='Document Title' if db=='IEEE' else 'Title'
 for i in sorted(ids|local):
  r=next((r for r in records if r['record_id']==i),base.get(i,{}))
  comparison.append({'source_database':db,'record_id':i,'Title':r.get(title,''),'DOI':r.get('DOI',''),'fresh_search':int(i in ids),'prior_local_match':int(i in local),'in_broad_baseline':int(i in base)})
 audit[db]={'query':QUERY,'expected_results':count,'export_rows':len(rows),'unique_source_ids':len(ids),'native_column_count':cols,'missing_by_field':{k:sum(not r[k].strip() for r in rows) for k in rows[0]},'raw_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'prior_local_matches':len(local),'shared_with_local':len(ids&local),'fresh_only_vs_local':sorted(ids-local),'local_only_vs_fresh':sorted(local-ids),'outside_baseline':sorted(ids-set(base)),'metadata_changed_vs_baseline':sum(any(r[k]!=base[r['record_id']].get(k) for k in rows[0]) for r in records if r['record_id'] in base)}
 audit[db]['abstract_unavailable_placeholder_count']=sum(r['Abstract'].strip().lower()=='[no abstract available]' for r in rows)
 (raw.parent/'manifest.json').write_text(json.dumps({'search_id':f'{db}-DTUA-2026-11-01','query':QUERY,'records':count,'native_columns':cols,'file':raw.name,'sha256':audit[db]['raw_sha256']},indent=2)+'\n',encoding='utf-8')
write(OUT/'fresh_search_vs_local_IEEE_SCOPUS.csv',comparison)
(OUT/'fresh_search_audit_IEEE_SCOPUS.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8')
print(json.dumps({db:{k:v for k,v in a.items() if k not in ['missing_by_field','fresh_only_vs_local','local_only_vs_fresh']}|{'fresh_only_count':len(a['fresh_only_vs_local']),'local_only_count':len(a['local_only_vs_fresh']),'missing_DOI':a['missing_by_field']['DOI'],'missing_abstract':a['missing_by_field']['Abstract']} for db,a in audit.items()},indent=2))

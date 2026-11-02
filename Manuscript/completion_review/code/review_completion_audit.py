from pathlib import Path
import csv,json,collections,hashlib
P=Path('outputs/Manuscript/methods_audit/eligibility');O=Path('outputs/Manuscript/completion_review');O.mkdir(exist_ok=True)
def read(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
logs=collections.defaultdict(list)
for p in (P/'broad_retrieval').glob('*.jsonl'):
 for line in p.read_text(encoding='utf8').splitlines():
  try:r=json.loads(line)
  except ValueError:continue
  logs[r.get('record_id','')].append((p.name,r))
rows=[]
for r in read(P/'broad_dtu_retrieval_status.csv'):
 hist=logs[r['record_id']];attempts=[a for _,z in hist for a in z.get('attempts',[])];urls={a.get('url') for a in attempts if a.get('url')}
 errors=[z.get('metadata_error') for _,z in hist if z.get('metadata_error')]
 rows.append({**r,'document_url_attempt_count':len(urls),'document_url_attempts':json.dumps(sorted(urls)), 'metadata_errors':json.dumps(errors),'audit_status':'assessed_in_existing_ledger' if r['retrieval_status']=='fulltext_assessed' else ('retrieval_attempted_not_assessed' if urls else 'no_document_url_attempt_in_jsonl')})
with (O/'retrieval_evidence_audit.csv').open('w',encoding='utf8',newline='') as f:
 w=csv.DictWriter(f,rows[0]);w.writeheader();w.writerows(rows)
dt=read(P/'broad_dt_unique_title_abstract_decisions.csv')
summary={'broad_dtu_retrieval_rows':len(rows),'retrieval_audit_status':dict(collections.Counter(r['audit_status'] for r in rows)),'existing_fulltext_validation':json.loads((P/'broad_dtu_fulltext_validation.json').read_text()),'base_dt':json.loads((P/'broad_dt_unique_screening_counts.json').read_text()),'rules':['Metadata lookup failure is not proof that report retrieval was attempted.','Not-retrieved reports are distinct from full-text exclusions.','Do not transfer uncertainty-based exclusions to DT-only eligibility.','Old numerical verification does not establish new full-text semantic verification.']}
(O/'completion_status.json').write_text(json.dumps(summary,indent=2),encoding='utf8');print(json.dumps(summary,indent=2))

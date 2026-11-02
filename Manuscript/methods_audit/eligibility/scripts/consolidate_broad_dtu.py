from pathlib import Path
import csv,json,collections,re
p=Path('outputs/Manuscript/methods_audit/eligibility')
src=list(csv.DictReader((p/'deduplication/Base_DT_U_canonical_records.csv').open(encoding='utf-8-sig'))); by={r['record_id']:r for r in src};out=[]
for f in sorted(p.glob('broad_dtu_[0-9]*.csv')):
 for r in csv.DictReader(f.open(encoding='utf-8-sig')):
  s=by[r['record_id']]; d=r.get('screening_decision',r.get('decision')); q=r.get('evidence_quote',r.get('supporting_quote',''))
  assert q.lower() in (s['title']+' '+s['abstract']).lower() or not q,(r['record_id'],q)
  out.append(dict(record_id=r['record_id'],title=s['title'],doi=s['doi'],year=s['year'],authors=s['authors'],databases=s['databases'],stages=s['stages'],decision=d,reason=r.get('decision_reason',r.get('reason')),evidence_quote=q,exclusion_reason_code=r.get('exclusion_reason_code','outside_building_material_chain' if d=='exclude_domain' else ''),assessment_basis='Full supplied title and abstract reviewed; not full-text eligibility',source_batch=f.name))
assert len(out)==len(src)==len(set(r['record_id'] for r in out))==528
assert set(r['record_id'] for r in out)==set(by)
with (p/'broad_dtu_title_abstract_decisions.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(out)
counts=dict(collections.Counter(r['decision'] for r in out));print(counts)
(p/'broad_dtu_screening_validation.json').write_text(json.dumps({'source_records':len(src),'decisions':len(out),'unique_ids':len(by),'missing_ids':[],'duplicate_decision_ids':[],'verbatim_quote_validation':'passed','counts':counts,'scope':'Title/abstract screening only; retained includes secondary and unresolved candidates; not final inclusion'},indent=2),encoding='utf-8')

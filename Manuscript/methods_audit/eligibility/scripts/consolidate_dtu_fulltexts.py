from pathlib import Path
import csv,json,collections,hashlib
p=Path('outputs/Manuscript/methods_audit/eligibility')
def read(f):return list(csv.DictReader(f.open(encoding='utf-8-sig')))
files=[p/'broad_dtu_existing_fulltext_decisions.csv',p/'broad_dtu_root_fulltext_decisions.csv']+sorted(p.glob('broad_dtu_downloaded_batch*.csv'))
rr=[]
for f in files:
 for x in read(f):
  def first(*keys):return next((x[k] for k in keys if x.get(k)), '')
  rr.append(dict(record_id=x['record_id'],doi=x['doi'],title=x['title'],decision=x['decision'],evidence_role=first('evidence_role','domain_relevance','domain'),reason=first('reason','decision_reason'),evidence_locator=first('locators','evidence_locations','evidence_locator'),dt_status=first('DTstatus','DT_status','dt_status'),uncertainty_treatment=first('Umechanism','U_mechanism','uncertainty_treatment','uncertainty_mechanism'),limitations=first('limits','limitations'),source_path=first('reviewed_file','source_local_path','local_pdf','local_path'),sha256=first('sha256','source_sha256','pdf_sha256'),assessment_scope=first('review_extent','assessment_basis','read_scope','review_scope'),decision_source=f.name))
assert len(rr)==len(set(x['record_id'] for x in rr))
by={x['record_id']:x for x in rr}
for o in read(p/'broad_dtu_final_overrides.csv'):
 x=by[o['record_id']];x['decision']=o['final_decision'];x['evidence_role']=o['evidence_role'];x['reason']=o['reason'];x['evidence_locator']=o['locators'];x['decision_source']+=';broad_dtu_final_overrides.csv'
for x in rr:
 x['counting_stream']='domain_included' if x['decision'].startswith('include') and x['decision']!='include_complementary' else ('complementary_included' if x['decision']=='include_complementary' else 'excluded_from_triple_intersection')
 assert x['reason'] and x['evidence_locator'] and x['sha256'],x
 f=Path(x['source_path']);assert f.exists(),str(f)
 assert hashlib.sha256(f.read_bytes()).hexdigest()==x['sha256'],str(f)
with (p/'broad_dtu_fulltext_final_decisions.csv').open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=rr[0]);w.writeheader();w.writerows(rr)
allpdf={x.stem for x in (p/'broad_retrieval/pdfs').glob('*.pdf')};missing=allpdf-set(by)
counts=dict(collections.Counter(x['counting_stream'] for x in rr));print('Fulltexts',len(rr),'counts',counts,'unassessedpdf',missing)
(p/'broad_dtu_fulltext_validation.json').write_text(json.dumps({'assessed_unique_publications':len(rr),'counts':counts,'unassessed_downloaded_pdf_ids':sorted(missing),'reason_locator_hash_validation':'passed','scope':'All currently archived broad DTU fulltexts; not closure of all search scenarios'},indent=2),encoding='utf-8')

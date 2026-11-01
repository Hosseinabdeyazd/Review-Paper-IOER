"""Integrate individually authored second readings; no automated eligibility classification.
Input: immutable canonical_screening_complete.zip plus unclear946_queue.json and four decision logs.
"""
from pathlib import Path
import csv,io,json,zipfile,hashlib
from collections import Counter
ROOT=Path.cwd(); W=ROOT/'work'; BASE=ROOT/'outputs/S4 S5 Core Review/screening/adjudication'
OUT=BASE/'unclear946_recheck'; OUT.mkdir(exist_ok=True)
with zipfile.ZipFile(BASE/'canonical_screening_complete.zip') as z:
 rows=list(csv.DictReader(io.TextIOWrapper(z.open('canonical_screening_complete.csv'),encoding='utf-8-sig')))
 provenance=z.read('merged_metadata_provenance.json')
original={r['record_id']:dict(r) for r in rows}
queue=json.loads((W/'unclear946_queue.json').read_text(encoding='utf8'))
assert len(rows)==len(original)==9587 and len(queue)==946
assert {r['record_id'] for r in queue}=={r['record_id'] for r in rows if r['adjudication_status']=='retain_fulltext_unclear'}
decisions={}
for name in ['a','b','c','root']:
 batch=json.loads((W/f'unclear946_{name}.json').read_text(encoding='utf8'))
 assert not set(batch)&set(decisions)
 decisions.update(batch)
assert set(decisions)=={r['record_id'] for r in queue},len(decisions)
overrides=json.loads((W/'unclear946_qa_overrides.json').read_text(encoding='utf8')) if (W/'unclear946_qa_overrides.json').exists() else {}
for rid,d in overrides.items():
 assert rid in decisions
 decisions[rid]={**decisions[rid],**d}
allowed={'retain_for_fulltext','retain_fulltext_unclear','retain_secondary','exclude_core_keep_methods','exclude_title_abstract','exclude_nonresearch_component'}
for q in queue:
 rid=q['record_id'];d=decisions[rid]
 assert q==original[rid] and queue[d['queue_index']]['record_id']==rid
 assert d['decision'] in allowed and len(d['reason'])>30
 assert isinstance(d['evidence'],str) and d['evidence'].strip()
 assert d['evidence'] in q['title'] or d['evidence'] in q['abstract'],rid
 assert d['remaining_information_gap'] and ((d['decision']=='retain_fulltext_unclear') == (d['remaining_information_gap']!='none'))
def layer(r):
 return 'uncertainty_query_member' if set(r['queries'].split(';'))&{'S4-2','S5-2'} else 'base_only'
for r in rows:
 rid=r['record_id'];d=decisions.get(rid)
 r['search_layer_membership']=layer(r)
 r['pre_unclear_recheck_status']=r['adjudication_status']
 r['pre_unclear_recheck_reason']=r['adjudication_reason']
 r['unclear_recheck_completed']='yes' if d else 'not_in_946_queue'
 r['unclear_recheck_gap']=d['remaining_information_gap'] if d else ''
 r['unclear_recheck_index']=d['queue_index'] if d else ''
 r['verified_title']='';r['verified_title_source']=''
 if d:
  r.update(adjudication_status=d['decision'],adjudication_reason=d['reason'],adjudication_evidence=d['evidence'],adjudication_reviewer=d['reviewer_method'])
 if rid=='S45-b7761f1ee86d':
  r['verified_title']='Adaptive reuse of buildings'
  r['verified_title_source']='https://ekonomiaisrodowisko.pl/journal/article/view/575'
 for k,v in original[rid].items():
  if k not in {'adjudication_status','adjudication_reason','adjudication_evidence','adjudication_reviewer'}: assert r[k]==v,(rid,k)
 if not d: assert all(r[k]==v for k,v in original[rid].items())
def cb(rs):
 s=io.StringIO(newline='');fields=list(dict.fromkeys(k for r in rs for k in r));w=csv.DictWriter(s,fieldnames=fields);w.writeheader();w.writerows(rs);return s.getvalue().encode('utf-8-sig')
def jw(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf8')
counts=Counter(r['adjudication_status'] for r in rows);changes=Counter(d['decision'] for d in decisions.values())
layers=[{'status':s,'base_only':sum(r['adjudication_status']==s and layer(r)=='base_only' for r in rows),'uncertainty_query_member':sum(r['adjudication_status']==s and layer(r)=='uncertainty_query_member' for r in rows)} for s in sorted(counts)]
assert sum(counts.values())==9587 and sum(changes.values())==946
summary={'rechecked':946,'pending_recheck':0,'recheck_outcomes':dict(changes),'canonical_records':9587,'all_current_outcomes':dict(counts),'layer_breakdown':layers,'baseline_retained':2668,'baseline_retained_uncertainty_query_members':345,'baseline_retained_base_only':2323,'independent_human_reviewers':0,'full_text_eligibility_completed':False,'query_membership_is_not_uncertainty_propagation_evidence':True}
jw('recheck_summary.json',summary);jw('individual_decisions.json',decisions)
with zipfile.ZipFile(OUT/'current_canonical_records.zip','w',zipfile.ZIP_DEFLATED) as z:
 z.writestr('current_canonical_records.csv',cb(rows));z.writestr('merged_metadata_provenance.json',provenance)
with zipfile.ZipFile(OUT/'recheck_946_full_metadata.zip','w',zipfile.ZIP_DEFLATED) as z:
 z.writestr('recheck_946_full_metadata.csv',cb([r for r in rows if r['record_id'] in decisions]))
with zipfile.ZipFile(OUT/'decision_sets.zip','w',zipfile.ZIP_DEFLATED) as z:
 for s in sorted(counts): z.writestr(s+'.csv',cb([r for r in rows if r['adjudication_status']==s]))
(OUT/'search_layer_counts.csv').write_bytes(cb(layers))
prisma=[('exported_query_memberships',19963),('within_database_overlap_removed',5094),('database_distinct_identified',14869),('previous_cross_database_duplicates_removed',4951),('additional_adjudicated_duplicates_removed',331),('canonical_records_screened',9587),('records_unreviewed',0),('unclear_records_rechecked',946),('recheck_pending',0)]+[(s,n) for s,n in sorted(counts.items())]
(OUT/'prisma_counts.csv').write_bytes(cb([{'stage':k,'count':v} for k,v in prisma]))
retained=sum(counts[s] for s in ['retain_for_fulltext','retain_fulltext_unclear','retain_secondary'])
status_table='\n'.join(f'| {s} | {n} |' for s,n in sorted(counts.items()))
change_table='\n'.join(f'| {s} | {n} |' for s,n in sorted(changes.items()))
layer_table='\n'.join(f"| {r['status']} | {r['base_only']} | {r['uncertainty_query_member']} |" for r in layers)
report=f'''# S4/S5 — second reading of all 946 unclear records

All 946 prior unclear canonical records were reread using title, entire available abstract and prior reason. No record was silently dropped; zero rechecks remain pending. This is AI-assisted semantic screening, not an independent human review or complete full-text eligibility assessment.

## Decisions in this revision

| New decision | Records |
|---|---:|
{change_table}

Unresolved cases now record the exact missing information: absent chapter/abstract, actual evaluation criteria, operational-versus-embodied boundary, or physical reuse/material scope. Absence of quantitative findings alone does not justify ambiguity when scope is explicit. Broad S4/S5 eligibility is not conditional on Digital Twin or uncertainty terminology.

Operational-only performance, generic project governance, and mechanical tests with no assessed material/reuse consequence were separated from core evidence. Useful transferable methods remain available in the methods/background set. An uncertainty method or historic-building setting alone does not establish material-chain relevance. Direct reuse/retention feasibility, recovery, material environmental assessment and applicable secondary evidence remain eligible for full-text review.

## Updated entire corpus

| Current decision | Records |
|---|---:|
{status_table}

All 9587 canonical records have a screening decision. {retained} reports remain for core full-text or secondary assessment; {9587-retained} are outside that set. These are report counts, not independent-study or final-inclusion counts. Full-text eligibility and quantitative uncertainty-transfer extraction have not been completed by this revision.

## Base versus uncertainty search layers

The previous 2668 clear retain_for_fulltext records comprised 2323 Base-only records and 345 records also retrieved by S4-2 or S5-2. The number was 2668, not 2268. Including unclear and secondary candidates, the previous broader candidate total was 3937 (3408 Base-only, 529 uncertainty-query members). The updated membership table is:

| Current status | Base only | Member of S4-2 or S5-2 |
|---|---:|---:|
{layer_table}

Membership is computed from original query IDs only; it is not a new keyword classifier and does not prove uncertainty quantification or propagation. The uncertainty subset is a retrieval subset, not a verified mechanistic evidence set. Full-text extraction must distinguish mention, quantification, propagation between stages, and validation/monitoring. No Base records were discarded merely to make the corpus smaller.

## PRISMA accounting

19963 query memberships - 5094 within-database overlaps = 14869 database-distinct records. Prior cross-database removals 4951 plus 331 adjudicated duplicates leave 9587 canonical records. All 330 candidate duplicate groups and 14 DOI-conflict decisions remain unchanged. This revision changes screening outcomes only, not identification or deduplication denominators. A remaining blank unverified DOI has not been invented. The 91 duplicate-alias original IDs not separately read remain documented in the prior audit; canonical coverage must not be described as all original IDs independently read.

## Publisher-verified metadata correction

Record S45-b7761f1ee86d (DOI 10.34659/eis.2022.83.4.575) has an electronic-waste title in the supplied data but a building-reuse abstract. The [publisher page](https://ekonomiaisrodowisko.pl/journal/article/view/575) identifies it as **Adaptive reuse of buildings** with the matching abstract. A legacy PDF indexed by a repository retains the anomalous title. Raw title/DOI/abstract are preserved; `verified_title` and `verified_title_source` record the correction separately. The record is retained based on the confirmed reuse subject, not silently relabelled.

## Reproducibility and limits

The 946-row full-metadata CSV records before/after decisions. `individual_decisions.json` records the new authored decisions, rationale, literal evidence and remaining gap. `current_canonical_records.zip` includes all original bibliographic fields and unchanged merged provenance. `decision_sets.zip` splits current records by outcome; excluded records are retained for audit. `search_layer_counts.csv` and `prisma_counts.csv` reconcile exactly to current records. Additional primary-source checks are documented in `primary_source_checks.json`; one targeted publisher fulltext check resolved record S45-9664a9714f51 to methods background. This does not constitute completion of fulltext eligibility for the corpus.

The script integrates authored decisions and validates coverage/evidence/preservation; it does not infer scientific eligibility. Four assistant readers divided the queue, and a further targeted consistency audit checked borderline decisions. No independent human reviewer participated. Incomplete abstracts remain incomplete; three attempted MDPI direct-page checks returned HTTP429, so no conclusions were inferred from those failed accesses. Full-text retrieval remains needed for unresolved cases. Earlier completion files remain immutable historical inputs and are superseded only for current screening counts.

To reproduce, extract `reproducibility_bundle.zip` at the workspace root with the prior `outputs/S4 S5 Core Review/screening/adjudication/canonical_screening_complete.zip` present, then run `python work/integrate_unclear946.py`.
'''
(OUT/'PRISMA_RECHECK.md').write_text(report,encoding='utf8')
(OUT/'README.md').write_text('# Current S4/S5 screening after 946-record recheck\n\nRead PRISMA_RECHECK.md for current counts, boundaries and decisions. All 946 reread; zero pending. Current CSVs are in current_canonical_records.zip and decision_sets.zip. Use adjudication_status/reason/evidence for current decisions; pre_unclear_recheck_* retain the previous decision. Original automated screening_status/decision_reason fields are historical, not current. Search-layer membership is retrieval provenance, not verified uncertainty evidence. No final included-study count is asserted.\n',encoding='utf8')
(OUT/'integrate_unclear946.py').write_bytes(Path(__file__).read_bytes())
(OUT/'primary_source_checks.json').write_bytes((W/'unclear946_a_sources.json').read_bytes())
with zipfile.ZipFile(OUT/'reproducibility_bundle.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in [W/'unclear946_queue.json',W/'integrate_unclear946.py',W/'read_unclear946.py',W/'save_unclear946.py',W/'unclear946_a_sources.json']+[W/f'unclear946_{n}.json' for n in ['a','b','c','root']]+([W/'unclear946_qa_overrides.json'] if overrides else []): z.write(p,p.relative_to(ROOT))
jw('validation.json',{'exact_946_coverage':True,'pending':0,'other_8641_decisions_unchanged':True,'original_bibliographic_fields_preserved':True,'literal_evidence_validated':946,'duplicate_decisions_unchanged':True,'counts_reconcile':True,'source_sha256':hashlib.sha256((BASE/'canonical_screening_complete.zip').read_bytes()).hexdigest(),'scientific_correctness_not_guaranteed_by_automated_validation':True})
manifest={}
for p in sorted(OUT.iterdir()):
 if p.is_file() and p.name!='manifest.json':
  b=p.read_bytes();manifest[p.name]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_sha1':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
jw('manifest.json',manifest)
print(json.dumps(summary,indent=2))

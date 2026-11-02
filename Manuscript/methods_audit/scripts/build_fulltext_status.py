from pathlib import Path
import csv,json,collections
p=Path('outputs/Manuscript/methods_audit/eligibility')
def read(f):return list(csv.DictReader(f.open(encoding='utf-8-sig')))
a=read(p/'broad_dtu_adjudicated_decisions.csv');ft={x['record_id']:x for x in read(p/'broad_dtu_fulltext_final_decisions.csv')};attempts=collections.defaultdict(list)
for f in (p/'broad_retrieval').glob('*.jsonl'):
 for l in f.read_text(encoding='utf-8').splitlines():
  x=json.loads(l);attempts[x['record_id']].append(f.name+':'+x['status'])
for f in [p/'recovery_missing_metadata.csv',p/'broad_retrieval/ieee_institutional_attempts.csv']:
 for x in read(f):attempts[x['record_id']].append(f.name)
r=[]
for x in a:
 if x['decision']=='exclude_domain':continue
 rid=x['record_id'];v=ft.get(rid)
 if v and v['counting_stream']=='not_assessed_retrieval_defect':v=None
 r.append(dict(record_id=rid,title=x['title'],doi=v['doi'] if v else x['doi'],title_abstract_decision=x['decision'],retrieval_status='fulltext_assessed' if v else ('html_body_access_confirmed_pending_capture_review' if rid=='DTMFU-13f51d56212107d7' else 'not_archived_after_recorded_routes'),eligibility_decision=v['decision'] if v else '',counting_stream=v['counting_stream'] if v else '',attempt_logs=';'.join(attempts[rid]),fulltext_source_path=v['source_path'] if v else ''))
assert len(r)==308 and all(x['attempt_logs'] for x in r)
with (p/'broad_dtu_retrieval_status.csv').open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=r[0]);w.writeheader();w.writerows(r)
summary=json.loads((p/'broad_dtu_fulltext_validation.json').read_text())
counts=summary['counts'];n=summary['assessed_unique_publications'];pending=308-n
report=f'''# Full-text eligibility and retrieval update

This update records substantive reading and decisions, not closure of every search scenario.

## Broad S1–S5 + DT + U

903 exported query occurrences yielded528 records after375 repeats were removed. All528 supplied titles/abstracts were read. Two additional aliases were resolved during screening, leaving526 publication records. Second-pass adjudication gives196 direct-domain full-text candidates,107 secondary/complementary candidates,5 unresolved-metadata candidates carried forward and218 domain exclusions. Secondary/complementary candidates remain a separate evidence stream.

All308 carried-forward records have a recorded retrieval route. Crossref publisher links, institutional/repository retrieval and authenticated SLUB IEEE access were used. A failed PDF route is not proof that no full text exists.

**{n} full texts have completed eligibility decisions: {counts['domain_included']} domain inclusions, {counts['complementary_included']} complementary inclusions and {counts['excluded_from_triple_intersection']} exclusions from the triple-intersection set.** Every decision has page/section evidence. PDF assessments retain file hashes; HTML assessments label the hash as assessment-notes-only, not a hash of the publisher full text. All downloaded files have been checked, but two are retrieval defects: one unrelated PDF and one partial book preview. These two do not count as full-text assessments or exclusions. Domain inclusions contain primary and secondary evidence and enabling or conceptual architectures; they are not all implemented twins or demonstrations of continuous uncertainty propagation.

{pending} candidates lack completed full-text eligibility assessment. These candidates still need an adequate complete text; wrong-file and partial-preview retrievals remain pending. These are not eligibility exclusions, and the broad search is not declared final.

## Previously selected focused sets

The separate S–U, focused bridge and focused DT–U sets comprise53 memberships/52 unique publications.45 full texts were assessed:43 retained and2 focused-scope exclusions;7 not retrieved. One assessment uses the complete publisher HTML; its PDF remains unarchived. These overlap the broad search and must not be added as independent populations. Their decisions answer different inclusion scopes.

## Eligibility and evidence interpretation

A substantive DT role requires described model/data/architecture connections, not a future-application sentence or keyword. Implemented, conceptual and enabling architectures remain distinguished. Uncertainty evidence may include explicit probabilistic analysis, structured reliability assessment or measured reference-based calibration/error analysis. Qualitative caveats or routine correction without a stated comparison are insufficient. Continuous propagation across stages is an extraction outcome, never assumed from inclusion. Operational energy-only or other-domain methods may enter the separately labelled complementary architecture stream, not direct material-chain counts.

The final-overrides table preserves the second-reading changes, notably the distinction between unstructured qualitative geometry correction and measured BIM/GIS volume calibration. Original decisions are retained for audit. This is an assisted review workflow, not a claim of two independent human reviewers or a prospectively registered protocol.

## Files and reproducibility

`broad_dtu_fulltext_final_decisions.csv` is the consolidated full-text decision table; individual batch tables retain the original extraction detail. `broad_dtu_retrieval_status.csv` links every candidate to retrieval logs. `broad_dtu_fulltext_validation.json` checks unique IDs, source hashes, reasons and evidence locators. Raw publisher PDFs remain in the local research archive; this commit publishes decision data and provenance, not a blanket republication of copyrighted full texts.

The broader Base+DT and Base/Base+U scenarios remain separate work queues. The manuscript and PRISMA figures must not report their eligibility stages as complete on the strength of this subset.
'''
(p/'FULLTEXT_UPDATE.md').write_text(report,encoding='utf-8');print(collections.Counter(x['retrieval_status'] for x in r))

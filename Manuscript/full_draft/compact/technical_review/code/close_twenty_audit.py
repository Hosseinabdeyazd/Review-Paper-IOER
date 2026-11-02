from pathlib import Path
import json,csv,re,shutil,hashlib
O=Path('outputs/Manuscript/full_draft/compact/technical_review')
p=O/'manuscript_en.html';s=p.read_text(encoding='utf8').replace('64.7% means that eleven of seventeen publications','70.0% means that fourteen of twenty publications').replace('contributes 64.7% of output variance','contributes 70.0% of output variance');p.write_text(s,encoding='utf8')
def read(p):return list(csv.DictReader(Path(p).open(encoding='utf-8-sig')))
rows=read(O/'data/su_twenty_paper_coding.csv');ids={r['paper_id'] for r in rows}
contexts=read('outputs/Manuscript/relational_analysis/results/inputs/su_context_assessments.csv');contexts=[r for r in contexts if r['included_in_counts']=='1']
assert ids=={r['paper_id'] for r in contexts} and len(contexts)==23
for name in ['F01_sources','F02_methods','F03_outcomes']:
 for r in read(O/'data'/(name+'.csv')):
  support=set(filter(None,r['paper_ids'].split(';')))
  assert support<=ids and len(support)==int(r['n']) and int(r['N'])==20
  assert float(r['percent'])==5*int(r['n'])
# Non-positive outcomes are intentionally not inferred from changes in mean impact.
decisions=read(O/'data/three_paper_coding_decisions.csv')
for pid in ['U19','U20','U21']:
 ref=next(r for r in rows if r['paper_id']==pid)
 for outcome in ['Preserved','Amplified','Legitimately reduced','Masked / lost']:
  decisions.append(dict(paper_id=pid,doi=ref['doi'],axis='outcomes',code=outcome,state='not positively coded',reason='No sufficiently explicit, comparable upstream/downstream uncertainty evidence for this outcome. Mean-impact changes and fixed assumptions alone are insufficient.',evidence_locator=ref['evidence_locator']))
with (O/'data/three_paper_coding_decisions.csv').open('w',encoding='utf8',newline='') as f:
 w=csv.DictWriter(f,list(decisions[0]));w.writeheader();w.writerows(decisions)
report='''TWENTY-PUBLICATION UPDATE AND RECONCILIATION

Scope: the selected S1–S5 + U cohort, not all broad search candidates.
Selected reports sought 21; not retrieved 1 (U10); assessed 20; full-text excluded 0; included 20.
The 17 archived eligible codings are retained. Three new codings are U19 Almeida et al., U20 Aljawhari et al., U21 Caruso et al. Current U19 is NOT legacy row 19: DOI-based identity is essential.

F01/F02/F03 now count distinct current publication IDs over N=20. D01/F04 and D04 already use 23 contexts from the identical 20 publications. Their context denominators are intentionally retained. D02 uses nine domain-DT publications; D03/F05 use ten general-DT records, not the S+U population. Independent arithmetic verification of those four relational diagrams passes.

New coding distinguishes quantified source uncertainty from acknowledged limitations. F01 combines both, as a source-documentation profile; it is not an assessment-success rate. The three-paper decision CSV identifies these distinctions. Legacy states are not retroactively upgraded. U21 explicitly reports ECF propagation but does not specify its numerical algorithm in the reviewed text; UM12 preserves this limitation instead of inventing a Monte Carlo or analytical method. UM11 records its documented event-based probabilistic risk calculation.

U19: sections 3.3–3.4 and 4.2.4 describe reuse/quality/lifetime-to-MCI/CFF impact coupling, seven scenarios, and 2000 Monte Carlo draws. Section 5.1 leaves later-cycle virgin input/waste contributions unresolved. Full joint-draw continuity is not established. U20: sections 3–4 and 6–8 describe conditional demand/damage/consequence propagation, 10000 component samples and 1000 risk realisations per intensity, plus Beta-distribution checks; dependence assumptions are retained as limits. U21: pp.2,6–13 and supplementary pp.1–4 describe ECF variability, event-based risk, cost/carbon proxy and unmodelled quantity uncertainty. U20/U21 are complementary damage-to-impact evidence; neither is counted as direct material-recovery S4→S5 evidence.

Outcome labels are multi-label: transformed 10/20 (50%); unassessed 11/20 (55%); preserved 3/20 (15%); masked/lost 3/20 (15%); amplified 1/20 (5%); legitimately reduced 1/20 (5%). These are documented classifications of operations/inputs, not measured shares of output variance. A paper may transform one uncertainty and leave another unassessed. New papers do not add amplified/reduced labels based on changes in mean carbon.

Figure 2b now uses the PRISMA visual grammar for the separate focused B+DT search: 83−40=43; 43−29=14; 14−2=12; 12−2=10. Figure 2c uses the same grammar for selected-report eligibility: 21−1=20; 20−0=20. Broad retrieval summaries are separate, with no misleading connecting arrows. The broad database-wide workflows remain incomplete; the selected-set flow cannot close them.

Files: su_twenty_paper_coding.csv gives DOI membership; three_paper_coding_decisions.csv gives positive and withheld judgments; F01/F02/F03 CSVs give every numerator, denominator and supporting ID. Original 17-paper inputs remain unchanged for provenance. Manuscript and supplementary figure PDFs are rebuilt from the updated HTML/SVG sources.
'''
(O/'TWENTY_PAPER_UPDATE.txt').write_text(report,encoding='utf8')
p=O/'README.md';s=p.read_text(encoding='utf8');s='## Current 20-publication update\n\nSource, method and outcome profiles now use all 20 included S1–S5+U publications (17 retained codings plus 3 newly coded full texts). See `TWENTY_PAPER_UPDATE.txt`, `data/su_twenty_paper_coding.csv`, and `data/three_paper_coding_decisions.csv`. Earlier 17-paper descriptions below are historical. Broad eligibility remains incomplete; selected-set inclusion is reconciled separately.\n\n'+s;p.write_text(s,encoding='utf8')
shutil.copyfile(__file__,O/'code/close_twenty_audit.py')
print('Verified 20 DOI-linked publications; 23 context records; all F01/F02/F03 numerators and denominators.')

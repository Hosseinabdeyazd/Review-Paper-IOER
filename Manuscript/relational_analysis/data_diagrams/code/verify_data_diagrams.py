"""Check edge weights against original decisions, not against plotting arrays."""
from pathlib import Path
from collections import Counter
import csv,json,hashlib
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1];SRC=ROOT.parent/'results'
def read(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
ass=[r for r in read(SRC/'inputs/su_context_assessments.csv') if r['included_in_counts']=='1']
def ids(text):return set(filter(None,text.split(';')))
edges=read(ROOT/'S_U_boundary_continuity_edges.csv')
for edge in edges:
    rows=[r for r in ass if r['context']==edge['context'] and r['continuity_code']==edge['continuity']]
    assert int(edge['assessments'])==len(rows)
    assert ids(edge['paper_ids'])=={r['paper_id'] for r in rows}
    assert ids(edge['dois'])=={r['doi'] for r in rows}
assert sum(int(r['assessments']) for r in edges)==len(ass)==23
assert Counter(r['continuity_code'] for r in ass)=={'Q':2,'N':5,'R':1,'S':4,'P':7,'E':4}

sd=read(SRC/'S_DT_complete_coding.csv')
sd_edges=read(ROOT/'S_DT_stage_function_edges.csv')
for edge in sd_edges:
    rows=[r for r in sd if r['stage']==edge['stage'] and r['feature']==edge['feature'] and r['state']=='R']
    assert ids(edge['paper_ids'])=={r['source_id'] for r in rows}
    assert int(edge['paper_count'])==len({r['source_id'] for r in rows})
assert sum(int(r['paper_count'])>0 for r in sd_edges)==16

du=read(SRC/'DT_U_complete_coding.csv')
eligible={r['source_id'] for r in du if r['architecture_family']!='Review / reference architecture'}
configs=read(ROOT/'DT_U_exact_configurations.csv');seen=set()
for group in configs:
    papers=ids(group['paper_ids']);assert not seen&papers;seen|=papers
    assert len(papers)==int(group['paper_count'])
    expected=ids(group['mechanisms'])
    for p in papers:
        assert expected=={r['feature'] for r in du if r['source_id']==p and r['state']=='R'}
assert seen==eligible and len(seen)==10 and len(configs)==9
assert len({r['mechanisms'] for r in configs})==len(configs)

pos=[r for r in read(SRC/'inputs/su_positive_theme_assignments.csv') if r['counted']=='1']
pairs=read(ROOT/'S_U_source_method_edges.csv')
valid_contexts={(r['paper_id'],r['context']) for r in ass}
for edge in pairs:
    source={(r['paper_id'],r['context']) for r in pos if r['dimension']=='source' and r['theme_code']==edge['source_code']}
    method={(r['paper_id'],r['context']) for r in pos if r['dimension']=='method' and r['theme_code']==edge['method_code']}
    both=source&method;assert both<=valid_contexts
    assert int(edge['shared_assessments'])==len(both)
    assert ids(edge['assessment_ids'])=={p+'@'+c for p,c in both}
    assert ids(edge['paper_ids'])=={p for p,c in both}
    assert int(edge['source_assessments'])==len(source)
    assert abs(float(edge['percent_of_source_assessments'])-100*len(both)/len(source))<.006
assert len(pairs)==100 and sum(int(r['shared_assessments'])>0 for r in pairs)==46

summary=json.loads((ROOT/'analysis_summary.json').read_text())
for rel,expected in summary['source_sha256'].items():
    assert hashlib.sha256((SRC/rel).read_bytes()).hexdigest()==expected
for name in summary['figures']:
    assert len(PdfReader(ROOT/'figures'/f'{name}.pdf').pages)==1
    for ext in ('png','svg','pdf'):assert (ROOT/'figures'/f'{name}.{ext}').stat().st_size>1000
assert len(PdfReader(ROOT/'Data_Derived_Diagrams.pdf').pages)==4
out={'status':'passed','boundary_status_cells':len(edges),'stage_function_cells':len(sd_edges),
     'exact_configurations':len(configs),'configuration_records':len(seen),'source_method_cells':len(pairs),
     'source_hashes':len(summary['source_sha256']),'pdf_pages':4,
     'interpretation':'Arithmetic and same-record joins verified; semantic coding is inherited, not independently revalidated.'}
(ROOT/'verification.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))

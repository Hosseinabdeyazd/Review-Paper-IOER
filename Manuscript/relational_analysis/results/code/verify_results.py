"""Recalculate published counts from exported decisions and check provenance.

This validates arithmetic/coverage, not the truth of semantic review decisions.
"""
from pathlib import Path
import csv, json, hashlib, math
from collections import Counter
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
def read(name):
    with (ROOT/name).open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

sd = read('S_DT_complete_coding.csv')
du = read('DT_U_complete_coding.csv')
register = read('new_coding_record_register.csv')
validation = json.loads((ROOT/'validation.json').read_text())
assert len(register) == 32
assert Counter((r['stream'], r['included']) for r in register) == {
    ('S_DT','1'):12, ('S_DT','0'):2, ('DT_U','1'):13, ('DT_U','0'):5}
for stream, rows, key in [('S_DT',sd,('source_id','stage','feature')), ('DT_U',du,('source_id','feature'))]:
    assert len({tuple(r[k] for k in key) for r in rows}) == len(rows)
    assert {r['source_id'] for r in rows} == {r['source_id'] for r in register if r['stream']==stream and r['included']=='1'}
    assert all(r['state'] in {'R','C','NR'} and r['decision_reason'] and r['title'] and r['evidence_anchor'] for r in rows)
    assert all((ROOT/r['source_file']).is_file() for r in rows)
assert len(sd)==648 and len(du)==91

for c in read('S_DT_counts.csv'):
    for state in ('R','C'):
        ids={r['alias'] for r in sd if r['stage']==c['stage'] and r['feature']==c['feature'] and r['state']==state}
        assert int(c[state+'_count'])==len(ids)
        assert set(filter(None,c[state+'_aliases'].split(';')))==ids
    denominator={r['source_id'] for r in sd if r['stage']==c['stage'] and r['state']=='R'}
    assert int(c['stage_R_denominator'])==len(denominator)
for c in read('DT_U_counts.csv'):
    for state in ('R','C'):
        ids={r['source_id'] for r in du if r['feature']==c['feature'] and r['state']==state}
        assert int(c[state+'_count'])==len(ids)
        assert set(filter(None,c[state+'_paper_ids'].split(';')))==ids

methods={r['source_id'] for r in du if r['architecture_family']!='Review / reference architecture'}
assert len(methods)==10
positive={f:{r['source_id'] for r in du if r['source_id'] in methods and r['state']=='R' and r['feature']==f} for f in {r['feature'] for r in du}}
for c in read('cooccurrence_and_sensitivity.csv'):
    a,b=positive[c['feature_1']],positive[c['feature_2']]
    expected=len(a&b)/len(a|b)
    loo=[len((a-{i})&(b-{i}))/len((a-{i})|(b-{i})) for i in methods]
    assert int(c['joint_count'])==len(a&b)
    assert set(filter(None,c['support_ids'].split(';')))==a&b
    assert math.isclose(float(c['jaccard']),expected,abs_tol=0.000051)
    assert math.isclose(float(c['leave_one_out_min']),min(loo),abs_tol=0.000051)
    assert math.isclose(float(c['leave_one_out_max']),max(loo),abs_tol=0.000051)
assert len(positive['prob']&positive['bayes'])==7
assert len(positive['prob']|positive['bayes'])==8
assert len(positive['detect']&positive['decision'])==7
assert len(positive['detect']|positive['decision'])==8
assert not (positive['joint']&positive['cover'])

ass=read('inputs/su_context_assessments.csv')
included=[r for r in ass if r['included_in_counts']=='1']
assert len(included)==23 and len({r['paper_id'] for r in included})==20
assert Counter(r['context'] for r in included)=={'B12':9,'B23':6,'B45':1,'O5':7}
for c in read('inputs/su_theme_counts.csv'):
    ids=set(filter(None,c['paper_ids'].split(';')))
    eligible={r['paper_id'] for r in included if r['context']==c['context']}
    assert ids<=eligible and int(c['paper_count'])==len(ids)
    assert int(c['context_denominator'])==len(eligible)

for name,expected in validation['input_sha256'].items():
    assert hashlib.sha256((ROOT/'inputs'/name).read_bytes()).hexdigest()==expected
for name in validation['figures']:
    for ext in ('png','svg','pdf'):
        assert (ROOT/'figures'/f'{name}.{ext}').stat().st_size>1000
    pdf=PdfReader(ROOT/'figures'/f'{name}.pdf')
    assert len(pdf.pages)==1 and len(pdf.pages[0].extract_text())>300
assert len(PdfReader(ROOT/'Results_Atlas.pdf').pages)==6

result={'status':'passed','decision_cells_checked':len(sd)+len(du),'cooccurrence_cells_checked':49,
        'source_records_checked':32,'su_context_assessments_checked':23,'input_hashes_checked':len(validation['input_sha256']),
        'single_page_figures_checked':6,'atlas_pages_checked':6,
        'scope':'Arithmetic, provenance, coverage and file integrity; not independent semantic or full-text validation'}
(ROOT/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))

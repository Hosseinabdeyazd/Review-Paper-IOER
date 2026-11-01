from pathlib import Path
import json,csv,collections,hashlib,zipfile
R=Path.cwd();W=R/'work'; O=R/'outputs/S4 S5 Core Review/screening/adjudication/uncertainty392_mechanisms';O.mkdir(exist_ok=True)
q=json.loads((W/'uq392_queue.json').read_text(encoding='utf8')); ds={}
for n in ['a','b','c']:
 d=json.loads((W/f'uq392_{n}.json').read_text(encoding='utf8'));assert not ds.keys()&d.keys();ds.update(d)
assert len(q)==len(ds)==392 and set(ds)=={r['record_id'] for r in q}
out=[]
for i,r in enumerate(q):
 d=ds[r['record_id']];assert d['index']==i
 assert d['evidence'].strip() and (d['evidence'] in r['title'] or d['evidence'] in r['abstract']),r['record_id']
 assert len(d['reason'])>30 and d['evidence_level']=='title_abstract'
 out.append({**r,**{'mechanism_'+k:v for k,v in d.items()}})
def csvwrite(name,rs):
 with (O/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rs[0]));w.writeheader();w.writerows(rs)
csvwrite('all_392_mechanism_decisions.csv',out)
for name,pred in [('propagation_candidates.csv',lambda r:r['mechanism_category']=='explicit_propagation'),('cross_stage_candidates.csv',lambda r:r['mechanism_cross_stage_s4_s5']=='explicit')]:
 rr=[r for r in out if pred(r)]
 if rr:csvwrite(name,rr)
checks=json.loads((W/'uq392_source_checks.json').read_text(encoding='utf8'))
for c in checks:
 c['record_id']=q[c['index']]['record_id'];c['title']=q[c['index']]['title'];c['doi']=q[c['index']]['doi']
csvwrite('targeted_source_checks.csv',checks)
stats=[]
for cat in sorted({d['category'] for d in ds.values()}):
 rr=[r for r in out if r['mechanism_category']==cat]
 stats.append({'category':cat,'unique_records':len(rr),'S4_query_members':sum('S4-2' in r['queries'].split(';') for r in rr),'S5_query_members':sum('S5-2' in r['queries'].split(';') for r in rr),'both_query_members':sum(all(s in r['queries'].split(';') for s in ['S4-2','S5-2']) for r in rr)})
csvwrite('mechanism_counts.csv',stats)
(O/'summary.json').write_text(json.dumps({'screened':392,'S4':143,'S5':331,'intersection':82,'S4_only':61,'S5_only':249,'categories':stats,'cross_stage_claims':dict(collections.Counter(d['cross_stage_s4_s5'] for d in ds.values()))},indent=2),encoding='utf8')
(O/'individual_decisions.json').write_text(json.dumps(ds,ensure_ascii=False,indent=2),encoding='utf8')
(O/'integrate_uq392.py').write_bytes(Path(__file__).read_bytes())
with zipfile.ZipFile(O/'reproducibility.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in [W/'uq392_queue.json',W/'integrate_uq392.py',W/'uq392_source_checks.json']+[W/f'uq392_{n}.json' for n in ['a','b','c']]:z.write(p,'work/'+p.name)
table='\n'.join('| '+ ' | '.join(str(v) for v in s.values())+' |' for s in stats)
report=f'''# S4/S5 uncertainty mechanism screening

392 unique clear fulltext candidates retrieved by the uncertainty-layer queries were individually assessed from titles and complete available abstracts. This is AI-assisted title/abstract mechanism screening, not fulltext verification or independent human review.

S4+Uncertainty:143; S5+Uncertainty:331; intersection:82; unique union:392. S4-only:61; S5-only:249. These are query memberships, not confirmed scientific stage assignments. The 33 unclear and 51 secondary uncertainty-query records are outside this requested 392-record cohort.

| Evidence category | Unique | S4 query | S5 query | Both queries |
|---|---:|---:|---:|---:|
{table}

Explicit propagation requires an uncertain input, a stated mapping/model and an uncertain output in the available abstract. Quantification alone, deterministic scenarios and sensitivity alone are separate. An explicit S4-to-S5 claim requires a described recovery/reuse uncertainty carried into environmental/LCA or decision outputs; appearing in both searches is insufficient. Missing information is not evidence of absence. No final included-study count is asserted.

Each row preserves source metadata and original decisions; mechanism_* fields record this new assessment, input, transformation, output, evidence and reason. The earlier broad S4/S5 screening counts and duplicate adjudications are unchanged. This is an additional thematic selection, not new PRISMA identification or a fulltext exclusion round.

Three assistant readers reviewed disjoint record batches. Fulltext checks are required before treating these candidates as confirmed mechanisms, especially to establish equations, distributions, dependence assumptions, calibration and actual stage interfaces. No mandatory Digital Twin criterion was used in the original S4/S5 queries.

## Targeted primary-source checks

The separate targeted_source_checks.csv documents four followups without overwriting abstract-only decisions. Mutale et al. use a Bayesian network for stock-property inference; reuse quantities and embodied carbon remain proposed extensions (sections2.3,3.5.3,4). Di Bari et al., DOI10.3390/buildings10030048, map stochastic earthquakes through repair/rebuild choices to GWP/cost outcomes (sections3-4); this is a qualified building-retention bridge, not a recovered-material quality/yield model. Galimshina et al. author slides show PCE-based LCA/LCC distributions, but slides are not the article fulltext. Almeida et al., DOI10.1016/j.jclepro.2026.148705, directly connect multicycle recovery/circularity with environmental allocation and probabilistic parameters at abstract level; fulltext access failed. Source URLs and limitations accompany each check.

Generic propagation counts include peripheral hazard, cost and stock-property models. They must not be presented as counts of demonstrated material recovery-to-LCA propagation. Likewise, a repair-to-carbon pathway is a building-retention bridge, distinct from modelling uncertain recovered-material quality or recovery yields. `cross_stage_candidates.csv` is the narrower abstract-level candidate set, still requiring fulltext confirmation.

## Closest pathways identified

- Almeida et al., [10.1016/j.jclepro.2026.148705](https://doi.org/10.1016/j.jclepro.2026.148705): strongest direct material circularity-to-environment candidate. Recovery/reuse and lifetimes feed multicycle MCIRENO/CFF outcomes with probabilistic parameter analysis. Exact uncertainty distributions and dependence across loops remain unverified.
- [10.1016/j.jobe.2023.108149](https://doi.org/10.1016/j.jobe.2023.108149): seismic component damage is converted through repair-material consequence models to embodied-carbon distributions. Explicit repair-to-environment pathway, not recovered-component quality transfer.
- [10.1038/s41467-025-68120-6](https://doi.org/10.1038/s41467-025-68120-6): probabilistic earthquake scenarios combine with repair/reconstruction material quantities and carbon factors to embodied-carbon risk at continental scale. A repair/reconstruction pathway.
- [10.3390/buildings10030048](https://doi.org/10.3390/buildings10030048): targeted methods check confirms event sampling, retention/rebuild decisions and GWP/LCC accumulation. Treat as a qualified retention bridge, not an uncertain recovery-yield model.

These mechanisms support complementary parts of a future architecture; none of these checks establishes a complete Digital Twin uncertainty-tracking implementation. The architecture mapping is the reviewer's interpretation, not terminology necessarily used by the authors.
'''
(O/'REPORT.md').write_text(report,encoding='utf8')
(O/'README.md').write_text('# Uncertainty mechanisms in 392 S4/S5 candidates\n\nSee REPORT.md and all_392_mechanism_decisions.csv. All classifications are based on title/abstract evidence; fulltext confirmation is not claimed.\n',encoding='utf8')
manifest={}
for p in O.iterdir():
 if p.is_file() and p.name!='manifest.json':
  b=p.read_bytes();manifest[p.name]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_sha1':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
(O/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
print((O/'summary.json').read_text())

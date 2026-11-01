"""Package evidence-coded full-text review; no automatic eligibility classifier.

Run from repository/workspace root. Inputs are prior bibliography and reviewed JSONs.
Does not reproduce the articles' Monte Carlo models or infer missing distributions.
"""
from pathlib import Path
import csv, json, hashlib, shutil
from pypdf import PdfReader

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=(HERE if (HERE/'paper1_extraction.json').exists() else ROOT/'outputs/S4 S5 Core Review/screening/adjudication/three_fulltexts')
OUT.mkdir(parents=True,exist_ok=True)
SOURCE=OUT.parent/'uncertainty392_mechanisms/all_392_mechanism_decisions.csv'
if not SOURCE.exists(): SOURCE=OUT/'bibliographic_inputs.csv'
csv.field_size_limit(100000000)
with SOURCE.open(encoding='utf-8-sig',newline='') as f: records=list(csv.DictReader(f))
specs=[
('10.1016/j.jclepro.2026.148705','Almeida_2026_Multicycle_framework.pdf','direct_relevant_shared_input_bridge','Closest topical anchor; shared reuse-feasibility inputs and parallel probabilistic circularity/CFF branches. Joint uncertainty transfer is not fully specified.','U2 functional reuse potential constrains plausible R2 entering the next lifecycle; MCI score is not passed into LCA.','2000 Monte Carlo runs; input distribution families/parameters and paired draws unreported.','Circularity and GWP distributions; no documented joint output distribution.','pp9–10 sections3.3–3.4; pp16–18 section4.2.4/Fig12','1','2'),
('10.1016/j.jobe.2023.108149','Aljawhari_2024_Earthquake_environmental_impacts.pdf','adjacent_repair_carbon_mechanism','Strong conditional intervention-to-carbon propagation, but repair/retention is not the review’s circular recoverability S4. Fixed recycling excludes uncertain recovery yield.','Geometry and damage define repair quantities; carbon factors map quantities to component consequences; damage/repairability branches aggregate to building risk.','10000 component Monte Carlo draws; lognormal consequences; 1000 PACT realizations/intensity; Beta global damage-state surrogates.','Component/building carbon distributions and annual risk; Beta surrogates omit collapse/excess residual drift.','pp5–10 section4; pp12–13 section6.2; pp14–16 section7','2','1'),
('10.1038/s41467-025-68120-6','Caruso_2026_Unveiling_environmental_impact_earthquakes_Europe.pdf','adjacent_portfolio_proxy','Scalable hazard/repair-risk-to-carbon proxy; not uncertain circular recoverability. Quantities and recovery share are fixed.','Assume carbon loss ratio equals economic loss ratio; multiply structural/nonstructural AALR by replacement embodied carbon and aggregate assets.','Stochastic hazard/vulnerability; ECF variability propagated to replacement carbon per authors; final joint propagation procedure not reported.','Expected annual embodied carbon; REC CoV about0.35 is not a confidence interval on final annual carbon.','pp6,9,12–14 Fig8; supplement pp1–4','3','3')]

def writecsv(name,rows):
    keys=list(dict.fromkeys(k for r in rows for k in r))
    with (OUT/name).open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)

extractions=[];manifest=[];steps=[]
for i,(doi,filename,decision,reason,bridge,method,output,anchor,rank,mechanism_rank) in enumerate(specs,1):
    matches=[r for r in records if r['doi'].lower()==doi]
    assert len(matches)==1,(doi,len(matches))
    r=dict(matches[0]);jp=ROOT/f'work/fulltext{i}_extraction.json'
    if not jp.exists():jp=OUT/f'paper{i}_extraction.json'
    j=json.loads(jp.read_text(encoding='utf-8-sig'))
    p=OUT/'pdfs'/filename
    r.update(fulltext_decision=decision,fulltext_reason=reason,fulltext_bridge=bridge,
             fulltext_uncertainty_method=method,fulltext_output=output,fulltext_evidence_anchor=anchor,
             fulltext_topic_rank=rank,fulltext_mechanism_rank=mechanism_rank,
             fulltext_digital_twin_demonstrated='no',fulltext_review_date='2026-11-02',
             fulltext_review_basis='AI-assisted substantive full-text reading and selected visual checks; no independent human validation',
             fulltext_pdf=filename,fulltext_pdf_downloaded=str(p.exists()).lower(),
             fulltext_joint_circular_recovery_to_lca_verified='no')
    extractions.append(r)
    if p.exists():
        data=p.read_bytes();assert data.startswith(b'%PDF')
        reader=PdfReader(p);first=reader.pages[0].extract_text() or ''
        assert doi.lower() in first.lower(),(filename,'DOI absent page1')
        manifest.append(dict(doi=doi,file='pdfs/'+filename,pages=len(reader.pages),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),version='publisher PDF',status='downloaded_verified',source='https://doi.org/'+doi))
    else:manifest.append(dict(doi=doi,file='pdfs/'+filename,status='download_pending',source='https://doi.org/'+doi))
    (OUT/f'paper{i}_extraction.json').write_text(json.dumps(j,ensure_ascii=False,indent=2),encoding='utf-8')
    np=ROOT/f'work/fulltext{i}_notes.md'
    if np.exists():shutil.copyfile(np,OUT/f'paper{i}_notes.md')
    ss=j.get('propagation_steps',j.get('mechanism_steps',[]))
    if i==1:ss=[
        dict(input='Reuse feasibility U2, lifespan L2, baseline MCI',mapping='Sample inputs through normalized MCI_RENO',output='Circularity distribution',locator='pp5,7; pp16–18/Fig12A'),
        dict(input='Functional reuse feasibility, shared boundary and scenarios',mapping='Constrain plausible CFF R2; not MCI score conversion; no verified paired sampler',output='Compatible CFF reuse/recovery input',locator='pp9–10 sections3.3–3.4'),
        dict(input='CFF reuse/recycling shares, quality, virgin/processing/disposal factors and allocation',mapping='2000 Monte Carlo iterations through CFF; avoided virgin production and disposal contributions',output='GWP distribution; joint relation to circularity distribution unreported',locator='p9 Eq5; pp16–18/Fig12B')]
    for n,s in enumerate(ss,1):
        steps.append(dict(doi=doi,step=n,input=s.get('input',''),transformation=s.get('mapping',s.get('transform','')),output=s.get('output',''),anchor=s.get('locator',s.get('anchor',''))))
writecsv('fulltext_extraction.csv',extractions)
writecsv('bibliographic_inputs.csv',[r for r in records if r['doi'].lower() in {s[0] for s in specs}])
writecsv('mechanism_steps.csv',steps)
for p in (OUT/'pdfs').glob('*Supplementary*.pdf'):
    d=p.read_bytes();manifest.append(dict(doi=specs[2][0],file='pdfs/'+p.name,pages=len(PdfReader(p).pages),bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),version='publisher supplementary information',status='downloaded_verified',source='https://www.nature.com/articles/s41467-025-68120-6'))
archive=OUT/'Aljawhari_2024_publisher_fulltext.txt'
if archive.exists():
    d=archive.read_bytes();manifest.append(dict(doi=specs[1][0],file=archive.name,bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),version='publisher rendered HTML text archive; not PDF',status='downloaded_verified_text',source='https://www.sciencedirect.com/science/article/pii/S235271022302329X'))
writecsv('download_manifest.csv',manifest)
audit=ROOT/'work/three_paper_synthesis_audit.md'
if audit.exists():shutil.copyfile(audit,OUT/'synthesis_audit.md')
if Path(__file__).resolve()!=OUT/'build_three_fulltexts.py':shutil.copyfile(Path(__file__),OUT/'build_three_fulltexts.py')
print(json.dumps({'reviewed':len(extractions),'main_pdfs':sum(p['version']=='publisher PDF' for p in manifest if 'version' in p),'files':len(manifest),'decisions':[r['fulltext_decision'] for r in extractions]},indent=2))

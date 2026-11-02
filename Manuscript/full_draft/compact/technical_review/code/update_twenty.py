from pathlib import Path
import csv,json,re,sys,html,shutil
sys.path.insert(0,str(Path('work/plot_dependencies').resolve()))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=Path('outputs/Manuscript/full_draft/compact/technical_review'); D=O/'data'; F=O/'figures'
def read(p):
 return list(csv.DictReader(Path(p).open(encoding='utf-8-sig')))
def write(p,rows):
 with Path(p).open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
legacy=read('outputs/Manuscript/full_draft/inputs/uncertainty_3axis_coding_19_papers.csv')
cross={r['legacy_id']:r for r in read('outputs/Manuscript/full_draft/data/legacy_eligibility_crosswalk.csv')}
elig=read('outputs/Manuscript/methods_audit/eligibility/su_fulltext_verified.csv')
new={
 'U19':{'sources':{'U04':('assessed','Recycled content R1 and material quality ratios varied in CFF.'),'U06':('assessed','Secondary service life L2 varied.'),'U07':('assessed','Reuse potential U2 and CFF reusability R2 varied; U2 constrains but is not equal to R2.'),'U10':('assessed','Virgin, recycling and disposal emission factors varied.'),'U11':('assessed','Allocation factor A affects CFF results.'),'U12':('assessed','Seven renovation/reuse scenarios compared.')},'methods':{'UM01':'One-way sensitivity explicitly reported.','UM02':'Global probabilistic sensitivity explicitly reported; Spearman/regression summaries.','UM03':'Seven scenarios compared.','UM04':'GWP distributions, boxplots and percentile-based sensitivity reported.','UM05':'2000 Monte Carlo simulations explicitly reported.'},'outcomes':{'Transformed':'Reuse/quality and lifetime parameters mapped to MCI and GWP; representation and output meaning change.','Unassessed':'Later-cycle virgin inputs and unrecovered waste omitted; their uncertain contribution is not evaluated (section 5.1).'},'locator':'PDF pp.9–10,16–19; sections 3.3–3.4,4.2.4,5.1; Fig.12','limit':'No shared-draw U2-to-R2 or dependence specification sufficient to establish complete continuity. Lower GWP is not evidence of reduced uncertainty.'},
 'U20':{'sources':{'U04':('assessed','Wall dimensions sampled to obtain repair-material quantities.'),'U05':('acknowledged/tested','Damage-to-cost proxy tested against damage-to-carbon; mismatch strongest at DS1.'),'U10':('assessed','EPD emission-factor variability propagated to component consequences.'),'U13':('acknowledged','US fragility models substituted where Italian low/high-code models unavailable.')},'methods':{'UM04':'16th/84th fractiles and distribution summaries reported.','UM05':'10000 component-level samples; 1000 risk realisations per intensity level.','UM08':'Lognormal component consequences and fitted Beta damage-to-carbon models, with goodness-of-fit checks.'},'outcomes':{'Transformed':'Demand and damage probabilities mapped through repair activities to embodied-carbon loss distributions.'},'locator':'Publisher full text sections 3.1–3.2,4.1,6.2,7–8; Figs.11–14','limit':'Geometry dependence neglected; damage within performance groups assumed uncorrelated. Lower expected carbon is not uncertainty reduction. Complementary damage-to-impact, not material-reuse S4-to-S5.'},
 'U21':{'sources':{'U02':('acknowledged','Exposure building-type misclassification discussed.'),'U04':('explicitly unassessed','Component-quantity uncertainty explicitly not modelled.'),'U05':('acknowledged/tested','One-to-one economic/carbon loss-ratio proxy; limitations and illustrative checks in supplement.'),'U06':('acknowledged','ECFs constrained by temporal scope of EPD data; 5-year validity discussed.'),'U08':('acknowledged','Transport variability acknowledged then fixed distance assumptions adopted.'),'U10':('assessed','ECF variability propagated; replacement-carbon coefficient of variation approximately 0.35.'),'U13':('acknowledged','ECFs from data-rich countries applied regionally; quantities assumed location-independent.'),'U12':('acknowledged','Build Back Better assumption contrasted with alternative repair/retrofit futures.')},'methods':{'UM11':'OpenQuake event-based probabilistic risk calculation across stochastic earthquake events.','UM12':'ECF propagation explicitly reported, but propagation algorithm and covariance treatment not specified in reviewed text/supplement.'},'outcomes':{'Transformed':'Hazard/vulnerability losses converted through AALR-to-AAECR proxy to annual embodied carbon.','Unassessed':'Component-quantity uncertainty explicitly not modelled; regional proxy and transport assumptions not jointly quantified.'},'locator':'PDF pp.2,6–7,9,11–13; Supplement pp.1–4','limit':'Do not infer Monte Carlo or analytical propagation for ECFs from a reported coefficient of variation. Proxy is not a direct uncertain recovery-quality interface.'}
}
records=[]; decisions=[]
for r in legacy:
 if r['ID'] not in cross:continue
 c=cross[r['ID']]
 out=[x for x in ['Preserved','Transformed','Amplified','Legitimately reduced','Masked / lost','Unassessed'] if {'Masked / lost':'masked','Legitimately reduced':'reduced'}.get(x,x).lower() in r['Propagation outcome'].lower()]
 records.append(dict(paper_id=c['current_id'],doi=r['DOI'],title=r['Title'],sources=r['Uncertainty source/type'],methods=r['Uncertainty method code'],outcomes='; '.join(out),evidence_locator=c['evidence_locator'],coding_basis='Retained archived coding; eligibility identity checked',limitations=r['Coding note']))
for pid,n in new.items():
 e=next(r for r in elig if r['paper_id']==pid)
 records.append(dict(paper_id=pid,doi=e['doi'],title=e['title'],sources='; '.join(n['sources']),methods='; '.join(n['methods']),outcomes='; '.join(n['outcomes']),evidence_locator=n['locator'],coding_basis='New full-text and relevant supplementary-material coding',limitations=n['limit']))
 for axis in ['sources','methods','outcomes']:
  for code,val in n[axis].items():
   state,why=val if isinstance(val,tuple) else ('documented',val)
   decisions.append(dict(paper_id=pid,doi=e['doi'],axis=axis,code=code,state=state,reason=why,evidence_locator=n['locator']))
assert len(records)==20 and {r['paper_id'] for r in records}=={r['paper_id'] for r in elig if r['decision']=='include'}
assert len({r['doi'].lower() for r in records})==20
write(D/'su_twenty_paper_coding.csv',records);write(D/'three_paper_coding_decisions.csv',decisions)
plt.rcParams.update({'font.family':'Times New Roman','font.size':11,'svg.fonttype':'none','pdf.fonttype':42,'axes.spines.top':False,'axes.spines.right':False})
stats={}
for name,axis,title,color in [('F01_sources','sources','Uncertainty sources documented in 20 included publications','#72B7B2'),('F02_methods','methods','Uncertainty methods documented in 20 included publications','#4C78A8'),('F03_outcomes','outcomes','Recorded uncertainty outcomes in 20 included publications','#9D755D')]:
 old=read(D/(name+'.csv'))
 labels={r.get('code',r['label']):r['label'] for r in old}
 if axis=='methods':labels.update(UM11='Event-based probabilistic risk',UM12='Reported propagation / algorithm unspecified')
 rows=[]
 for code,label in labels.items():
  ids=sorted(r['paper_id'] for r in records if code in [v.strip() for v in r[axis].split(';')])
  rows.append(dict(code=code,label=label,n=len(ids),N=20,percent=5*len(ids),paper_ids=';'.join(ids),basis='20 included publications; retained 17 plus 3 new full-text-coded papers; multi-label'))
 write(D/(name+'.csv'),rows);stats[axis]=rows
 fig,ax=plt.subplots(figsize=(10,6.4));rr=sorted(rows,key=lambda r:r['n'])
 ax.barh(range(len(rr)),[r['percent'] for r in rr],color=color)
 ax.set_yticks(range(len(rr)),[r['label'] for r in rr]);ax.set_xlim(0,100);ax.set_xlabel('Share of included S1–S5 + U publications (%)');ax.set_title(title,fontweight='bold',pad=16)
 for i,r in enumerate(rr):ax.text(r['percent']+1,i,f"{r['n']}/20 ({r['percent']:.1f}%)",va='center',fontsize=10)
 ax.grid(axis='x',color='#D9D9D9',linewidth=.5);ax.set_axisbelow(True)
 note='Multi-label; sources include assessed and explicitly acknowledged uncertainty. Not all sources are propagated.' if axis=='sources' else 'Multi-label; one paper may support several categories. Frequencies do not measure uncertainty magnitude.'
 fig.text(.01,-.025,note,fontsize=9)
 for ext in ['svg','png']:fig.savefig(F/(name+'.'+ext),bbox_inches='tight',dpi=180)
 plt.close(fig)
def para(s,start,newtext):
 return re.sub(r'<p>'+re.escape(start)+r'.*?</p>','<p>'+newtext+'</p>',s,flags=re.S)
def fmt(axis,c):
 r=next(x for x in stats[axis] if x['code']==c);return f"{r['n']}/20 ({r['percent']:.1f}%)"
p=O/'manuscript_en.html';s=p.read_text(encoding='utf8')
s=para(s,'The available analyses reveal','The linked analyses use 20 included S1–S5+U publications for source, method and outcome frequencies. These same publications contribute 23 publication–context assessments of continuity. The DT stage–function network uses nine publications with S1–S5 function codes, and the general DT+U configuration analysis uses ten non-review publications. Those denominators answer different questions and are not added as independent review totals.')
s=para(s,'All source and method percentages','The source, method and outcome dataset combines the 17 previously coded publications with three newly coded full texts, joined by DOI to the 20 included reports in the selected-set eligibility ledger. Sources include explicitly acknowledged as well as quantified uncertainties; the new decision table distinguishes these states. Each paper contributes at most once to each category. This update reconciles membership and arithmetic, while retaining the provenance of earlier interpretive codes.')
s=para(s,'Material intensity/composition is',f"Material intensity/composition occurs in {fmt('sources','U04')}, followed by scenario/future context in {fmt('sources','U12')}. Temporal/event and LCA inventory/factor sources each occur in {fmt('sources','U06')}; model-form uncertainty occurs in {fmt('sources','U05')}. Recovery/technical feasibility is recorded in {fmt('sources','U07')}. These frequencies describe documented sources, including acknowledged limitations; they are not the proportion of studies that successfully propagate each source. For example, Caruso et al. (2026) explicitly acknowledge but do not model component-quantity uncertainty.")
s=s.replace('Recalculated source frequencies, archived 17-paper coding. Multi-label, paper denominator.','Source frequencies across the 20 included S1–S5+U publications. Multi-label; assessed and acknowledged sources are distinguished in the coding table.')
s=para(s,'The legacy method codes record',f"Local/one-way sensitivity occurs in {fmt('methods','UM01')}; scenario comparison in {fmt('methods','UM03')}; Monte Carlo in {fmt('methods','UM05')}; and interval/range representation in {fmt('methods','UM04')}. Almeida et al. (2026) add explicit global sensitivity, while Aljawhari et al. (2024) propagate sampled damage and repair consequences. Caruso et al. (2026) use event-based probabilistic risk; their reported ECF propagation is separately coded because its algorithm is not specified in the reviewed text. Bootstrap remains a broad inherited category and does not always imply output-interval estimation.")
s=para(s,'The six legacy downstream-outcome',f"Transformed outcomes are recorded in {fmt('outcomes','Transformed')}, and unassessed components or interfaces in {fmt('outcomes','Unassessed')}. Preserved and masked/lost each occur in {fmt('outcomes','Preserved')}; amplified and legitimately reduced each occur in {fmt('outcomes','Amplified')}. Outcomes overlap at paper level because different variables or interfaces can receive different classifications. The three additions provide transformation evidence, but none establishes amplification or justified reduction of uncertainty merely through a change in mean carbon impact. Supplementary Figure S3 reports all six categories.")
s=para(s,'The strongest quantitative statements','The quantitative distributions describe the 20-publication selected set, not population prevalence. Seventeen publications retain their archived coding and three have newly documented source-level decisions. The 23-context continuity analysis uses a separate evidence-status taxonomy on the same publication set. The small general-DT sample remains cross-domain. These distributions cannot rank method effectiveness or establish complete propagation through every S1–S5 boundary.')
s=s.replace('from the legacy six-outcome labels','from the six outcome labels')
p.write_text(s,encoding='utf8')
p=O/'supplement_figures_en.html';s=p.read_text(encoding='utf8')
s=para(s,'The 17-paper legacy subset','Source, method and outcome frequencies use the 20 included S1–S5+U publications: 17 retained archived codings and three newly coded full texts. Positive categories are counted once per paper and divided by 20. Sources can be quantified or explicitly acknowledged; new rows preserve that distinction. Method additions distinguish event-based risk from reported propagation with an unspecified algorithm. Outcome labels are multi-label and refer to documented operations or unresolved inputs, not differences in mean environmental impact. DOI membership equals the selected-set Included list. The 23 contexts are dependent assessments from the same 20 publications. General-DT mechanism frequencies retain their distinct ten-paper denominator.')
s=s.replace('archived 17-paper','20-paper').replace('17-paper subset','20-paper set').replace('17 papers','20 papers')
p.write_text(s,encoding='utf8')
audit=dict(included_publications=20,unique_dois=20,retained_archived_codings=17,new_fulltext_codings=3,selected_reports_sought=21,not_retrieved=1,assessed=20,excluded=0,included=20,context_assessments=23,dt_function_publications=9,general_dtu_publications=10,source_counts={r['code']:r['n'] for r in stats['sources']},method_counts={r['code']:r['n'] for r in stats['methods']},outcome_counts={r['code']:r['n'] for r in stats['outcomes']},broad_search_eligibility_closed=False)
(O/'frequency_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf8')
(O/'code').mkdir(exist_ok=True);shutil.copyfile(__file__,O/'code/update_twenty.py')
print(json.dumps(audit,indent=2))

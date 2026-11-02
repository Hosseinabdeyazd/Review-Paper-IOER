"""Reproduce descriptive content figures from explicit, reviewable coding.

Python 3; matplotlib/numpy. Run from any directory. No automatic keyword coding.
Inputs are archived extraction tables, NOT newly reread full texts.
"""
from pathlib import Path
import csv
import json
import hashlib
from collections import Counter
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.patches import Patch
from matplotlib.ticker import MaxNLocator

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / 'inputs'
FIG = ROOT / 'figures'
FIG.mkdir(exist_ok=True)

def read_csv(p):
    with p.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def write_csv(name, rows, fields=None):
    rows = list(rows)
    with (ROOT / name).open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fields or list(rows[0]))
        w.writeheader()
        w.writerows(rows)

papers = {r['paper_id']: r for r in read_csv(INPUT / 'transition_extraction.csv')}
legacy = {r['DOI'].lower(): r for r in read_csv(INPUT / 'legacy_19_coding.csv')}

# Codes here are new descriptive labels; they do not reinterpret the old Uxx codes.
SOURCES = [
    ('data_quality', 'Data accuracy, completeness & currency', 'Data quality discussed as uncertain input; not a quantitative UQ claim.'),
    ('geometry', 'Geometry, morphology & design', 'Building geometry, design or morphology variability/error.'),
    ('prediction', 'Classification & prediction error', 'Prediction, classification or inferred-event accuracy/error explicitly recorded.'),
    ('material', 'Material intensity & stock parameters', 'Variation/ranges in material intensity, composition or material-stock parameters.'),
    ('timing', 'Lifetime, turnover & event timing', 'Service lives, turnover, event dates or analysis horizons; distinct from elapsed computing time.'),
    ('model', 'Model form & upscaling assumptions', 'Model-family, representation or upscaling choice; not automatically an epistemic classification.'),
    ('scenario', 'Future scenarios & policy assumptions', 'Alternative futures or policy assumptions; scenarios are not assigned probabilities here.'),
    ('recovery', 'Recovery share, reuse & quality', 'Recoverability, reuse feasibility or material quality in circular routing.'),
    ('environment', 'Environmental factors & processes', 'Emission factors, environmental parameters or carbonation process parameters.'),
    ('damage', 'Hazard & damage states', 'Seismic hazard, damage or loss in complementary consequence studies.'),
]
METHODS = [
    ('qualitative', 'Qualitative quality / uncertainty assessment', 'Qualitative input-quality or uncertainty assessment.'),
    ('validation', 'Prediction-error / validation diagnostics', 'Model accuracy, residual/error scores or predictive validation; not propagated UQ by default.'),
    ('ranges', 'Ranges / probability-distribution representation', 'Explicit range or distribution representation; does not by itself establish transfer.'),
    ('sampling', 'Monte Carlo / probabilistic sampling', 'Monte Carlo or parameter sampling recorded; no implication that all inputs are jointly propagated.'),
    ('bootstrap', 'Bootstrap for uncertainty outputs', 'Resampling linked to output uncertainty; ML training-data augmentation is excluded.'),
    ('sensitivity', 'Sensitivity / representation comparison', 'Input, model-family, geometry or importance comparisons; not necessarily probabilistic.'),
    ('scenarios', 'Scenario comparison', 'Alternative-future or policy scenario evaluation.'),
    ('conditional', 'Conditional consequence distributions', 'Conditional mapping from damage to interventions/consequences.'),
    ('proxy', 'Proxy conversion & aggregation', 'Expected-loss proxy transformed to expected environmental consequences.'),
    ('review', 'Review synthesis', 'Secondary methodological synthesis; no primary propagation experiment.'),
]
CONTEXTS = ['B12', 'B23', 'B34', 'B45', 'O5']
LABELS = ['S1 → S2', 'S2 → S3', 'S3 → S4', 'S4 → S5', 'Other → S5*']
COLORS = ['#2878B5', '#E3A329', '#8B98A6', '#2A9D8F', '#A66BBE']
STATES = {
    'Q': ('Discussion / review', '#D4DDE5'),
    'N': ('Downstream transfer not demonstrated', '#D97A71'),
    'R': ('Inputs prepared for propagation', '#D7B654'),
    'S': ('Sensitivity / representation comparison', '#89A7CB'),
    'P': ('Partial or incompletely documented transfer', '#58B8AE'),
    'E': ('Quantified outputs for selected uncertain inputs', '#277266'),
}

# Each tuple is an article-context assessment, with separate source and method tags.
# Assignments are scoped to the indicated interface: e.g. U06 emission-factor MC
# is NOT copied into its S1→S2 assessment.
DECISIONS = [
    ('U01','B12','geometry material','','N','Geometry/material stock errors are discussed; the extraction does not carry their joint uncertainty into stock outputs.'),
    ('U01','B23','timing scenario','ranges scenarios','P','Lifetime/scenario uncertainty is introduced in dynamic waste modelling; upstream geometry/MI error is not jointly carried.'),
    ('U02','B12','data_quality','qualitative','Q','Source accuracy, completeness and currency concern stock inputs; qualitative comparison only.'),
    ('U03','B12','material','ranges','R','Fitted MI distributions are available to a downstream stock model; propagation is not executed.'),
    ('U04','B12','geometry material prediction','validation sensitivity','N','RF validation, bootstrap and importance address MI estimates; total-stock uncertainty is not propagated. Training bootstrap is not counted as output-UQ bootstrap.'),
    ('U05','B12','geometry prediction','validation','N','Building-feature prediction errors are discussed, but point estimates are aggregated; bootstrap augmentation is not output-UQ propagation.'),
    ('U06','B12','geometry prediction material','validation ranges','P','MI ranges are rescaled into quantities, while footprint/height/classification errors are not jointly propagated. Uses the revised U06 main+SI note.'),
    ('U06','B23','prediction timing','validation','N','Construction/demolition-year accuracy is evaluated; probabilities are reduced to selected event years. The new U06 note does not demonstrate uncertainty transfer at this specific boundary.'),
    ('U06','O5','environment','sampling ranges','P','Emission-factor distributions are constructed and transformed to carbon; upstream EO error and joint dependence are not carried. No recovery stage is established.'),
    ('U07','B12','geometry material','sensitivity','S','Geometry-informed and archetypal MI representations differ; variability is not automatically a probability distribution.'),
    ('U08','B12','geometry material model','qualitative','N','Geometry/archetype/upscaling uncertainties are acknowledged; no demonstrated propagation.'),
    ('U09','B12','geometry','sensitivity','S','Design-space sensitivity is explicitly distinguished from real-world probability distributions.'),
    ('U10','B23','material timing','','','Abstract-only stock ranges and dynamic MFA; retained in the register but excluded from all full-text-based counts.'),
    ('U11','B23','timing model','ranges sampling sensitivity','E','Lifetime-family and parameter uncertainty is sampled into stocks and demolition flows; scale affects outputs.'),
    ('U12','B23','material timing','sampling bootstrap sensitivity','E','Monte Carlo and bootstrap propagate selected inputs into dynamic stock/flow probability intervals.'),
    ('U13','B23','material timing scenario','ranges sampling scenarios','P','Spatial stock attributes, lifetime parameters and scenarios affect flows, but full output UQ remains incomplete.'),
    ('U14','O5','timing scenario environment','review','Q','Review of dynamic LCA; methodological evidence, not an observed primary transfer.'),
    ('U15','O5','environment scenario','sensitivity scenarios','S','Emission/decarbonization scenarios and sensitivity; not a direct recovery-to-impact transition.'),
    ('U16','O5','environment','bootstrap','E','Emission factors propagated into carbon SE and confidence intervals; no demolition-timing transfer is inferred.'),
    ('U17','O5','timing environment scenario','sensitivity scenarios','S','Lifetime, factors and policy scenarios varied individually/scenario-wise; no joint probability distribution.'),
    ('U18','B23','timing model','ranges sensitivity','P','Layer lifetimes/model form change renovation flows; no full joint probabilistic propagation.'),
    ('U19','B45','recovery','sampling scenarios','P','Recovery/reuse feasibility constrains circularity and CFF branches; Monte Carlo and scenarios are reported, but paired draws/dependence are undocumented.'),
    ('U20','O5','damage geometry environment','sampling conditional','E','Complementary damage-to-carbon probabilistic conversion; recycling is fixed, so this is not S4→S5 recovery-yield evidence.'),
    ('U21','O5','damage environment','proxy','P','Complementary expected-loss-to-carbon proxy and aggregation; joint final uncertainty distribution undocumented.'),
]

codebook = [{'dimension': dim, 'code': code, 'label': label, 'definition': definition}
            for dim, categories in [('source', SOURCES), ('method', METHODS)]
            for code, label, definition in categories]
write_csv('codebook.csv', codebook)
context_rows, assignments, full_matrix = [], [], []
seen = set()
for pid, ctx, sources, methods, state, reason in DECISIONS:
    assert (pid,ctx) not in seen
    seen.add((pid,ctx))
    r = papers[pid]
    included = pid != 'U10'
    assert ctx in CONTEXTS and (state in STATES if included else state == '')
    role = 'methodological_review' if pid in ['U02','U14'] else ('complementary_primary' if pid in ['U20','U21'] else 'primary_research')
    common = {'paper_id': pid, 'doi': r['doi'], 'title': r['title'],
              'context': ctx, 'evidence_role': role, 'included_in_counts': int(included),
              'continuity_code': state, 'decision_reason': reason,
              'original_audited_transition': r['audited_transition'],
              'original_evidence_class': r['evidence_class'],
              'input_uncertainty': r['input_uncertainty'],
              'transformation': r['transformation'],
              'interface_limitation': r['interface_limitation'],
              'evidence_anchor': r['evidence_anchor'], 'prior_review_basis': r['review_basis'],
              'coding_basis': '2026-11-02 semantic harmonization of archived extraction; no new fulltext rereading',
              'legacy_method_description': legacy.get(r['doi'].lower(),{}).get('Uncertainty method',''),
              'source_location': 'inputs/transition_extraction.csv' + ('; inputs/legacy_19_coding.csv' if int(pid[1:])<=18 else '; inputs/three_fulltext_extraction.csv') + ('; inputs/U06_review.md' if pid=='U06' else '')}
    context_rows.append(common)
    for dim, categorylist, selected in [('source', SOURCES, sources.split()), ('method', METHODS, methods.split())]:
        assert set(selected) <= {c[0] for c in categorylist}
        for code, label, definition in categorylist:
            row = {**common, 'dimension':dim, 'theme_code':code, 'theme_label':label,
                   'coding_status': 'recorded' if code in selected else 'not_recorded_in_extraction',
                   'counted': int(included and code in selected)}
            full_matrix.append(row)
            if code in selected:
                assignments.append(row)
write_csv('article_context_assessments.csv', context_rows)
write_csv('positive_theme_assignments.csv', assignments)
matrix_fields = ['paper_id','doi','context','dimension','theme_code','theme_label','coding_status','counted','included_in_counts']
write_csv('complete_coding_matrix.csv', [{k:r[k] for k in matrix_fields} for r in full_matrix])

eligible = [r for r in context_rows if r['included_in_counts']]
denoms = {c: len({r['paper_id'] for r in eligible if r['context']==c}) for c in CONTEXTS}
assert len(papers)==21 and len({r['doi'].lower() for r in papers.values()})==21
assert {r['paper_id'] for r in context_rows} == set(papers)
assert len({r['paper_id'] for r in eligible})==20 and len(eligible)==23
assert denoms == {'B12':9,'B23':6,'B34':0,'B45':1,'O5':7}

aggregates=[]
for dim, cats in [('source',SOURCES),('method',METHODS)]:
    for code,label,_ in cats:
        for ctx in CONTEXTS:
            members = sorted({r['paper_id'] for r in assignments if r['counted'] and r['dimension']==dim and r['theme_code']==code and r['context']==ctx})
            assert len(members)<=denoms[ctx]
            aggregates.append({'dimension':dim,'theme_code':code,'theme_label':label,'context':ctx,
                               'paper_count':len(members),'context_denominator':denoms[ctx],
                               'percent_of_context': round(100*len(members)/denoms[ctx],2) if denoms[ctx] else '',
                               'paper_ids':';'.join(members),
                               'interpretation': 'recorded theme in extraction; not proof of transfer or an estimate of literature prevalence'})
write_csv('theme_context_counts.csv',aggregates)

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,
                     'axes.spines.right':False,'svg.fonttype':'none','pdf.fonttype':42,
                     'savefig.facecolor':'white','axes.titleweight':'bold'})

def save(fig,name):
    for ext in ['pdf','svg','png']:
        fig.savefig(FIG/f'{name}.{ext}',dpi=170,bbox_inches='tight',pad_inches=.22)
    plt.close(fig)

def theme_figure(dim,cats,name,title):
    mat=np.array([[next(r['paper_count'] for r in aggregates if r['dimension']==dim and r['theme_code']==code and r['context']==ctx)
                   for ctx in CONTEXTS] for code,_,_ in cats])
    perc=mat/np.array([denoms[c] or np.nan for c in CONTEXTS])*100
    fig=plt.figure(figsize=(14.5,8.5))
    grid=fig.add_gridspec(1,2,width_ratios=[1.0,1.05],left=.32,right=.98,top=.79,bottom=.22,wspace=.15)
    ax=fig.add_subplot(grid[0]); bar=fig.add_subplot(grid[1],sharey=ax)
    cmap=plt.get_cmap('Blues').copy();cmap.set_bad('#ECEFF2')
    ax.imshow(perc,cmap=cmap,vmin=0,vmax=100,aspect='auto')
    ax.set_yticks(range(len(cats)),[label for _,label,_ in cats],fontsize=10.5)
    ax.set_xticks(range(5),LABELS,rotation=40,ha='right',fontsize=10)
    ax.tick_params(axis='both',length=0,pad=9)
    for i in range(len(cats)):
        for j,ctx in enumerate(CONTEXTS):
            value=f'{mat[i,j]}/{denoms[ctx]}' if denoms[ctx] else '—'
            ax.text(j,i,value,ha='center',va='center',fontsize=10,color='white' if perc[i,j]>=65 else '#22313F')
    ax.set_xticks(np.arange(-.5,5,1),minor=True);ax.set_yticks(np.arange(-.5,len(cats),1),minor=True)
    ax.grid(which='minor',color='white',linewidth=2);ax.tick_params(which='minor',length=0)
    ax.set_title('Recorded coverage within each context\nCell = papers / assessed context papers',fontsize=11,pad=17)
    left=np.zeros(len(cats))
    for j,ctx in enumerate(CONTEXTS):
        bar.barh(np.arange(len(cats)),mat[:,j],left=left,color=COLORS[j],height=.66,label=LABELS[j])
        for i,n in enumerate(mat[:,j]):
            if n:bar.text(left[i]+n/2,i,str(n),ha='center',va='center',fontsize=10,color='white' if j!=1 else '#25303B',fontweight='bold')
        left+=mat[:,j]
    bar.set_ylim(len(cats)-.5,-.5);bar.tick_params(axis='y',left=False,labelleft=False)
    bar.xaxis.set_major_locator(MaxNLocator(integer=True));bar.grid(axis='x',alpha=.18);bar.set_axisbelow(True)
    bar.set_xlabel('Article–context assignments',labelpad=9)
    bar.set_title('Frequency of recorded themes\nStacked by assessed context',fontsize=11,pad=17)
    bar.set_xlim(0,max(left)+1)
    for i,total in enumerate(left):bar.text(total+.13,i,str(int(total)),va='center',fontsize=9,color='#4C5865')
    for a in [ax,bar]:
        for spine in a.spines.values():spine.set_visible(False)
    fig.suptitle(title,x=.035,y=.97,ha='left',fontsize=19,fontweight='bold',color='#183448')
    fig.text(.035,.915,'S1–S5 + uncertainty working evidence set • 20 assessed papers • 1 abstract-only record excluded',fontsize=11,color='#4C5865')
    fig.legend(handles=[Patch(facecolor=COLORS[i],label=LABELS[i]) for i in range(5)],loc='lower center',bbox_to_anchor=(.64,.105),ncol=5,frameon=False,fontsize=9.5)
    fig.text(.035,.078,'Colour intensity: 0–100% recorded coverage. Grey dash: no assessed article in this context; not evidence of absence.',fontsize=9,color='#4C5865')
    fig.text(.035,.049,'* Other → S5 includes quantity/factor/damage-to-impact pathways. It is not relabelled as recovery → impact.',fontsize=9,color='#4C5865')
    fig.text(.035,.020,'Themes and contexts may overlap within one paper. Bars count assignments, not unique-paper totals. No significance test.',fontsize=9,color='#4C5865')
    save(fig,name)

theme_figure('source',SOURCES,'01_uncertainty_sources','Which uncertainties are discussed within the cluster?')
theme_figure('method',METHODS,'02_uncertainty_methods','How is uncertainty analysed within the cluster?')

# This figure distinguishes theme occurrence from actual continuity evidence.
state_order=list(STATES)
smat=np.array([[sum(r['context']==c and r['continuity_code']==s for r in eligible) for c in CONTEXTS] for s in state_order])
assert np.array_equal(smat.sum(axis=0),np.array(list(denoms.values())))
fig,ax=plt.subplots(figsize=(12,6.6))
fig.subplots_adjust(left=.18,right=.97,top=.77,bottom=.40)
bottom=np.zeros(5)
for k,state in enumerate(state_order):
    label,col=STATES[state]
    ax.bar(np.arange(5),smat[k],bottom=bottom,color=col,label=f'{state}  {label}',width=.63)
    for j,n in enumerate(smat[k]):
        if n:ax.text(j,bottom[j]+n/2,str(n),ha='center',va='center',color='white' if state=='E' else '#182E3A',fontweight='bold')
    bottom+=smat[k]
ax.set_xticks(range(5),LABELS);ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_ylabel('Article–context assessments');ax.set_ylim(0,10.5)
ax.grid(axis='y',alpha=.15);ax.set_axisbelow(True)
for j,n in enumerate(bottom):
    ax.text(j,n+.23, f'n = {int(n)}' if n else 'No assessed\narticle',ha='center',va='bottom',fontsize=10,color='#4C5865')
fig.suptitle('Does local uncertainty analysis continue across the interface?',x=.035,y=.97,ha='left',fontsize=17,fontweight='bold',color='#183448')
fig.text(.035,.90,'Separate from topic frequency: one assessed continuity category per article and context.',fontsize=11,color='#4C5865')
fig.legend(loc='lower left',bbox_to_anchor=(.12,.15),ncol=2,frameon=False,fontsize=9.5)
fig.text(.035,.102,'E confirms quantified outputs for selected inputs, not complete S1–S5 continuity. P retains documented limitations.',fontsize=9)
fig.text(.035,.067,'Other → S5 includes two complementary damage studies and a methodological review. S3 → S4 has no assessed article here.',fontsize=9)
fig.text(.035,.032,'20 papers generate 23 context assessments. U10 is abstract-only and excluded. No claim about the entire indexed literature.',fontsize=9)
save(fig,'03_continuity_evidence')

continuity_counts=[{'context':ctx,'continuity_code':s,'label':STATES[s][0],
                   'paper_count':int(smat[i,j]),
                   'paper_ids':';'.join(sorted(r['paper_id'] for r in eligible if r['context']==ctx and r['continuity_code']==s))}
                  for i,s in enumerate(state_order) for j,ctx in enumerate(CONTEXTS)]
write_csv('continuity_counts.csv',continuity_counts)
audit={'created':'2026-11-02','source_records':len(papers),'unique_dois':21,'counted_papers':20,
       'excluded_from_figures':['U10'],'counted_article_contexts':len(eligible),'context_denominators':denoms,
       'positive_counted_theme_assignments':sum(r['counted'] for r in assignments),
       'duplicate_paper_contexts':0,'all_counts_within_denominator':True,
       'continuity_categories_sum_to_context_denominators':True,
       'new_fulltext_rereading':False,'independent_human_validation':False,
       'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in INPUT.iterdir() if p.is_file()}}
(ROOT/'validation.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
print(json.dumps(audit,indent=2))

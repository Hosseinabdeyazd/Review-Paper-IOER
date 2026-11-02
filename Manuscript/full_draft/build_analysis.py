from pathlib import Path
import sys,csv,json,hashlib,collections,re,shutil
ROOT=Path(__file__).resolve().parent; M=ROOT.parent
sys.path.insert(0,str(M.parents[1]/'work/plot_dependencies'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
F=ROOT/'figures'; F.mkdir(exist_ok=True); D=ROOT/'data';D.mkdir(exist_ok=True)
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(name,rows):
 with (D/name).open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,list(rows[0]));w.writeheader();w.writerows(rows)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','pdf.fonttype':42})
def save(fig,name):
 for ext in ['svg','pdf','png']:fig.savefig(F/(name+'.'+ext),bbox_inches='tight',dpi=170)
 plt.close(fig)
def bar(rows,name,title,note):
 fig,ax=plt.subplots(figsize=(10,6.4));rows=sorted(rows,key=lambda r:r['n']); y=np.arange(len(rows))
 ax.barh(y,[r['percent'] for r in rows],color='#307f92');ax.set_yticks(y,[r['label'] for r in rows]);ax.set_xlim(0,115);ax.set_xlabel('Share of the stated analytical subset (%)');ax.set_title(title,loc='left',fontweight='bold',pad=18)
 for i,r in enumerate(rows):ax.text(r['percent']+1,i,f"{r['n']}/{r['N']}  ({r['percent']:.1f}%)",va='center',fontsize=10)
 ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True);fig.text(.02,-.025,note,fontsize=9);save(fig,name)
legacy=read(ROOT/'inputs/uncertainty_3axis_coding_19_papers.csv'); inc=[r for r in legacy if r['ID'] not in ['10','19']];assert len(inc)==17
audit=[]
for col,stat,labelkey,name,title in [('Uncertainty source/type','uncertainty_source_stats_17_verified.csv','Uncertainty source/type','F01_sources','Uncertainty sources in the archived 17-paper subset'),('Uncertainty method code','uncertainty_method_stats_17_verified.csv','Uncertainty method','F02_methods','Analysis methods in the archived 17-paper subset')]:
 rr=[]
 for r in read(ROOT/'inputs'/stat):
  ids=[x['ID'] for x in inc if r['Code'] in [v.strip() for v in x[col].split(';')]];n=len(ids);assert n==int(r['Papers']);assert abs(100*n/17-float(r['Share (%)']))<.051
  rr.append({'code':r['Code'],'label':r[labelkey],'n':n,'N':17,'percent':100*n/17,'paper_ids':';'.join(ids),'basis':'Archived multi-label coding; arithmetic checked, not newly full-text recoded'})
 write(name+'.csv',rr);bar(rr,name,title,'Multi-label counts; zeros mean no recorded code in this subset, not absence from the literature.');audit.append({'dataset':stat,'rows_verified':len(rr),'result':'passed'})
rr=[]
for r in read(ROOT/'inputs/propagation_outcome_stats_17_verified.csv'):
 label=r['Propagation outcome'];term={'Masked / lost':'masked','Legitimately reduced':'reduced'}.get(label,label).lower()
 ids=[x['ID'] for x in inc if term in x['Propagation outcome'].lower()];n=len(ids);assert n==int(r['Papers']);assert abs(100*n/17-float(r['Share (%)']))<.051
 rr.append({'label':label,'n':n,'N':17,'percent':100*n/17,'paper_ids':';'.join(ids),'basis':'Legacy wording-matched outcome labels; not a new quantitative propagation judgement'})
write('F03_outcomes.csv',rr);bar(rr,'F03_outcomes','Recorded downstream outcomes: overlapping paper labels','17 papers; multi-label. Unassessed and transformed may concern different interfaces in the same paper.')
ass=[r for r in read(M/'relational_analysis/results/inputs/su_context_assessments.csv') if r['included_in_counts']=='1']; assert len(ass)==23
status=['Q','N','R','S','P','E']; labels=['Review/discussion','Transfer not demonstrated','Inputs prepared','Sensitivity/comparison','Partial transfer','Quantified selected inputs'];colors=['#9baab4','#c7776c','#d7b34e','#7099bd','#56a59d','#276f5b']
fig,ax=plt.subplots(figsize=(10,6));rr=[]
for i,b in enumerate(['B12','B23','B34','B45','O5']):
 rows=[r for r in ass if r['context']==b];N=len(rows);left=0
 for c,label,color in zip(status,labels,colors):
  ids=[r['paper_id'] for r in rows if r['continuity_code']==c];n=len(ids);pc=100*n/N if N else None
  rr.append({'boundary':b,'status':c,'label':label,'n':n,'N':N,'percent':pc,'paper_ids':';'.join(ids)})
  if n:ax.barh(i,pc,left=left,color=color);ax.text(left+pc/2,i,str(n),ha='center',va='center',color='white',fontweight='bold');left+=pc
 if not N:ax.text(3,i,'No assessed context; percentage undefined',va='center',color='#64717c')
ax.set_yticks(range(5),['S1 → S2  (N=9)','S2 → S3  (N=6)','S3 → S4  (N=0)','S4 → S5  (N=1)','Other → S5  (N=7)']);ax.invert_yaxis();ax.set_xlim(0,100);ax.set_xlabel('Share of assessed contexts within each boundary (%)');ax.set_title('Continuity status by boundary: current 23-context coding',loc='left',fontweight='bold')
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=c,label=l) for c,l in zip(colors,labels)],loc='upper center',bbox_to_anchor=(.5,-.16),ncol=2,frameon=False);fig.text(.02,-.15,'20 publications contribute 23 contexts. Counts inside segments; B34 is not evidence of literature-wide absence.',fontsize=9)
save(fig,'F04_boundary_percentages');write('F04_boundary_percentages.csv',rr)
dt=[r for r in read(M/'relational_analysis/results/DT_U_complete_coding.csv') if r['architecture_family']!='Review / reference architecture']; ids={r['source_id'] for r in dt};assert len(ids)==10
rr=[]
for feat in dict.fromkeys(r['feature'] for r in dt):
 rows=[r for r in dt if r['feature']==feat];positive=sorted({r['source_id'] for r in rows if r['state']=='R'});rr.append({'code':feat,'label':rows[0]['label'],'n':len(positive),'N':len(ids),'percent':100*len(positive)/len(ids),'paper_ids':';'.join(positive)})
write('F05_dt_mechanisms.csv',rr);bar(rr,'F05_dt_mechanisms','DT uncertainty mechanisms: 10 non-review coded records','Positive R codes only. Conceptual and unrecorded states are not proof of absence. Multi-label percentages.')
# Illustrative distributions: no fitted data, no measured uncertainty reduction.
x=np.linspace(-4,4,500)
def norm(mu,s):return np.exp(-.5*((x-mu)/s)**2)/(s*np.sqrt(2*np.pi))
fig,axes=plt.subplots(6,2,figsize=(10,10));names=['Preserved','Transformed','Amplified','Reduced with evidence','Masked / lost','Unassessed']
for i,label in enumerate(names):
 for j in [0,1]:
  a=axes[i,j];a.set_xlim(-4,4);a.set_ylim(0,1);a.set_xticks([]);a.set_yticks([]);a.spines[['left','right','top']].set_visible(False)
  y=norm(0,.8)
  if j and i==1:y=.5*norm(-1,.45)+.5*norm(1,.45)
  if j and i==2:y=norm(0,1.5)
  if j and i==3:y=norm(0,.43)
  if j and i==4:a.vlines(0,0,.8,color='#3a5364');a.plot(0,.8,'o',color='#3a5364')
  elif j and i==5:a.text(.5,.4,'?',transform=a.transAxes,ha='center',fontsize=28)
  else:a.plot(x,y,color='#307f92');a.fill_between(x,y,alpha=.2,color='#307f92')
 axes[i,0].set_ylabel(label,rotation=0,ha='right',va='center',labelpad=15)
axes[0,0].set_title('Upstream representation');axes[0,1].set_title('Downstream representation');fig.suptitle('Interpretive outcome vocabulary — conceptual examples',fontweight='bold');fig.text(.08,.01,'Synthetic normalized curves only. Narrowing requires validation; variance across different units is not directly comparable.',fontsize=9);fig.tight_layout(rect=[0,.04,1,.96]);save(fig,'F06_outcome_vocabulary')
write('arithmetic_audit.csv',audit+[{'dataset':'propagation_outcome_stats_17_verified.csv','rows_verified':6,'result':'passed; explicit legacy wording mapping retained'}])
# Reconcile identities to eligibility without asserting revalidated codes.
elig={r['doi'].lower():r for r in read(M/'methods_audit/eligibility/su_fulltext_verified.csv')};join=[]
for r in inc:
 e=elig.get(r['DOI'].lower(),{});join.append({'legacy_id':r['ID'],'doi':r['DOI'],'current_id':e.get('paper_id',''),'current_decision':e.get('decision',''),'role':e.get('evidence_role',''),'evidence_locator':e.get('evidence_locator',''),'semantic_recoding':'not performed in this update'})
assert all(r['current_decision']=='include' for r in join);write('legacy_eligibility_crosswalk.csv',join)
for name in ['figure_S2_configuration_choices (1).svg','Figure_07_Propagation_Outcomes.svg','Figure_05_Uncertainty_Source_Taxonomy.svg']:
 source=Path('C:/Users/technokade/Downloads')/name
 if source.exists():shutil.copyfile(source,ROOT/'inputs'/name)
 else:assert (ROOT/'inputs'/name).exists(),name
summary={'legacy_papers':17,'current_su_papers':len({r['paper_id'] for r in ass}),'current_su_contexts':len(ass),'dtu_nonreview_papers':len(ids),'legacy_all_include_in_current_ledger':True,'new_fulltext_recoding':False,'uncertainty_magnitudes_meta_analysed':False,'legacy_figures_reproduced':True,'source_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'inputs').glob('*.csv')}}
(ROOT/'analysis_validation.json').write_text(json.dumps(summary,indent=2),encoding='utf8');print(json.dumps(summary,indent=2))

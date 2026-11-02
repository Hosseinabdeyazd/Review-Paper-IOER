from pathlib import Path
import csv,sys,textwrap
sys.path.insert(0,str(Path('work/plot_dependencies').resolve()))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path('outputs/Manuscript/completion_review')
R=Path('outputs/Manuscript/relational_analysis/results/DT_U_complete_coding.csv')
rows=list(csv.DictReader(R.open(encoding='utf-8-sig')))
features=[('detect','Mismatch detection','Compare observations with predictions; investigate residuals and drift.'),('bayes','State / parameter inference','Update uncertain states using observations and explicit noise assumptions.'),('joint','Dependency transport','Pass joint samples or covariance across model interfaces.'),('cover','Calibration check','Test predictive interval coverage against held-out observations.'),('decision','Decision interface','Link confidence to alerts, decisions or requests for evidence.')]
support=[]
for f,label,desc in features:
 records=[r for r in rows if r['feature']==f and r['state']=='R' and r['architecture_family']!='Review / reference architecture']
 for r in records:
  support.append({'module':label,'feature':f,'source_id':r['source_id'],'doi':r['doi'],'title':r['title'],'evidence_anchor':r['evidence_anchor'],'decision_reason':r['decision_reason'],'verification_basis':r['basis'],'allocation_status':'Mechanism supported in general DT corpus; S1-S5 placement is reviewer synthesis, not demonstrated deployment.'})
with (O/'architecture_module_evidence.csv').open('w',encoding='utf8',newline='') as h:
 w=csv.DictWriter(h,support[0]);w.writeheader();w.writerows(support)
fig,ax=plt.subplots(figsize=(15,11));ax.set(xlim=(0,15),ylim=(0,11));ax.axis('off')
def box(x,y,w,h,title,body,color='#eaf3f6',dash=False):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.04',facecolor=color,edgecolor='#477383',linestyle='--' if dash else '-',linewidth=1.2))
 ax.text(x+.15,y+h-.18,textwrap.fill(title,24) if w<3 else title,fontsize=10,weight='bold',color='#16394c',va='top')
 ax.text(x+.15,y+h-.72,textwrap.fill(body,max(18,int(w*10))),fontsize=10,va='top',linespacing=1.45)
def arrow(x1,y1,x2,y2):ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='->',color='#477383',lw=1.5))
ax.text(.2,10.7,'A digital twin architecture for uncertainty continuity',fontsize=21,weight='bold',color='#16394c')
ax.text(.2,10.27,'Literature-informed synthesis: supported mechanisms + proposed cross-stage connections',fontsize=12)
box(.25,8.95,14.5,1.0,'A  DESIGN BRIEF','Decision and stakeholder information needs • spatial support • time horizon • evidence requirements • acceptable risk',color='#edf0f4')
stages=[('S1  Observe / infer','Geometry and attributes'),('S2  Inventory','Material quantities'),('S3  Dynamics','Release amount / time'),('S4  Recovery','Quality and usable yield'),('S5  Impacts','Environmental outcomes')]
for i,(t,b) in enumerate(stages):
 x=.25+i*2.94;box(x,7.55,2.65,1.0,t,b)
 if i<4:arrow(x+2.69,8.05,x+2.92,8.05)
ax.text(.25,7.14,'B  CONFIGURATION: model basis, data coupling, update strategy and uncertainty representation',fontsize=11,weight='bold')
box(.25,5.78,14.5,1.05,'Shared uncertainty record at every interface','Entity ID + quantity/unit + source/version + timestamp + spatial support + distribution/interval/scenario + dependence + validation status',color='#fff3df',dash=True)
for i in range(5):arrow(1.55+i*2.94,7.04,1.55+i*2.94,6.87)
ax.text(.25,5.35,'C  FUNCTIONAL ALLOCATION: assessment modules supporting the stage chain',fontsize=11,weight='bold')
for i,(f,label,desc) in enumerate(features):
 n=len({r['source_id'] for r in support if r['feature']==f})
 box(.25+i*2.94,2.87,2.65,2.12,label,desc+'  General DT evidence: '+str(n)+'/10 papers.',color='#eef5ef')
 arrow(1.55+i*2.94,5.2,1.55+i*2.94,5.03)
box(.25,1.47,14.5,1.05,'Proposed feedback loop','Flag a failed check → trace its upstream source and affected outputs → acquire evidence or revise assumptions → rerun downstream models',color='#fff3df',dash=True)
arrow(7.5,2.83,7.5,2.56)
ax.text(.25,1.04,'Green: mechanisms coded in general DT studies. Dashed amber: our proposed integration across S1–S5.',fontsize=10)
ax.text(.25,.65,'Counts are non-exclusive paper frequencies, not accuracy, uncertainty reduction or proof of deployment in the material chain.',fontsize=10)
ax.text(.25,.26,'Source IDs and coding anchors: architecture_module_evidence.csv. Existing coding reused; no claim of a new independent full-text audit.',fontsize=9,color='#526676')
for ext in ['svg','png']:fig.savefig(O/f'dt_uncertainty_architecture.{ext}',dpi=180,bbox_inches='tight')
print('Architecture modules:',len(support),'traceable module-paper links')



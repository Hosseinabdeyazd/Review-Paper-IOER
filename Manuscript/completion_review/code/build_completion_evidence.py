from pathlib import Path
import csv,json,sys,textwrap,collections,hashlib
sys.path.insert(0,str(Path('work/plot_dependencies').resolve()))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path('outputs/Manuscript/completion_review');R=Path('outputs/Manuscript/relational_analysis/results')
def read(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
def write(name,rows):
 with (O/name).open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,rows[0]);w.writeheader();w.writerows(rows)
du=read(R/'DT_U_complete_coding.csv');su=[r for r in read(R/'inputs/su_context_assessments.csv') if r['included_in_counts']=='1']
contexts=['B12','B23','B34','B45'];features=['prob','bayes','joint','detect','adapt','coverage','decision']
print('DT feature codes',sorted({r['feature'] for r in du}))
rows=[
 ['S1 → S2','Geometry, class probabilities, material coefficients','Attribute inference → material inventory','Check geometry error; calibrate classes; propagate shared archetype uncertainty','Mass distribution + identity + dependencies','obs;semantic;quantity','prob;bayes;joint'],
 ['S2 → S3','Stock, cohorts, service-life assumptions','Inventory → event-conditioned release','Check lifetime fit; retain stock–lifetime dependence; compare observed outflows','Release amount and time, conditional on scenario','time;exchange','prob;bayes;joint;adapt'],
 ['S3 → S4','Release, condition, contamination, separability','Released → technically recoverable material','Inspect/test quality; model yield and rejection; check mass balance','Pathway-specific quantity and quality','recovery','prob;detect;decision'],
 ['S4 → S5','Recovery yield, substitution, process and transport factors','Recoverable material → environmental consequence','Propagate compatible inputs; compare scenarios; test decision reversals','Impact distribution + assumptions + decision robustness','environment;decision','prob;joint;decision']]
out=[]
for i,r in enumerate(rows):
 c=[x for x in su if x['context']==contexts[i]]
 support=sorted({x['source_id'] for x in du if x['feature'] in r[6].split(';') and x['state']=='R' and x['architecture_family']!='Review / reference architecture'})
 out.append(dict(zip(['boundary','uncertain_input','transformation','assessment_requirement','output_contract','domain_function_requirements','general_mechanism_requirements'],r))|{'domain_context_count':len(c),'domain_paper_ids':';'.join(sorted({x['paper_id'] for x in c})),'general_mechanism_paper_ids':';'.join(support),'evidence_status':'Cross-study architectural proposal; general mechanism support is not evidence of deployment at this boundary.'})
write('boundary_architecture_requirements.csv',out)
fig,ax=plt.subplots(figsize=(15,10));ax.set(xlim=(0,15),ylim=(0,10));ax.axis('off')
ax.text(.25,9.65,'Where the digital twin can assess uncertainty',fontsize=22,weight='bold',color='#17384b')
ax.text(.25,9.23,'Proposed allocation across S1–S5; implementation and end-to-end effectiveness are not established.',fontsize=11)
headers=['Interface','Uncertain information','Transformation','Assessment module','Traceable output'];xs=[.25,1.9,5.0,7.9,11.3];ws=[1.45,2.9,2.7,3.2,3.4]
for x,w,h in zip(xs,ws,headers):ax.text(x,8.65,h,fontsize=11,weight='bold')
for i,row in enumerate(rows):
 y=8.3-i*1.55
 for j,(x,w,txt) in enumerate(zip(xs,ws,row[:5])):
  ax.add_patch(FancyBboxPatch((x,y-1.15),w,1.3,boxstyle='round,pad=.02',facecolor=['#edf4f8','#edf4f8','#eef5ef','#fff2dc','#eef5ef'][j],edgecolor='#98aab4'))
  ax.text(x+.12,y+.02,textwrap.fill(txt,width=15 if j==0 else 25 if j==2 else 31),fontsize=10,va='top')
ax.text(.25,1.55,'Shared information contract: entity ID • units • time • spatial support • model version • source • dependencies',fontsize=12,weight='bold')
ax.text(.25,1.05,'Feedback: failed checks → locate the upstream source → acquire evidence or revise the model → rerun downstream analysis',fontsize=11)
ax.text(.25,.5,'Error diagnostics can flag disagreement. A calibrated predictive interval assesses uncertainty; neither proves its unique cause.',fontsize=11)
for ext in ['png','svg']:fig.savefig(O/f'architecture_assessment_locations.{ext}',dpi=180,bbox_inches='tight')
plt.close(fig)
codes=['N','R','S','P','E','Q'];labels=['Transfer not demonstrated','Inputs prepared','Sensitivity comparison','Partial transfer','Quantified outputs','Review/discussion']
fig,ax=plt.subplots(figsize=(12,5));colors=['#bd6965','#ddb85a','#7a9bc1','#6aaea7','#247760','#a4b1bc'];left=[0]*4
for code,label,color in zip(codes,labels,colors):
 counts=[sum(r['context']==c and r['continuity_code']==code for r in su) for c in contexts]
 ax.barh(range(4),counts,left=left,label=label,color=color)
 for i,n in enumerate(counts):
  if n:ax.text(left[i]+n/2,i,str(n),ha='center',va='center')
 left=[a+b for a,b in zip(left,counts)]
ax.set_yticks(range(4),[r[0] for r in rows]);ax.invert_yaxis();ax.set_xlabel('Assessed paper–boundary contexts (not uncertainty magnitude)');ax.set_title('Evidence at adjacent interfaces');ax.text(.1,2,'No assessed context in this extraction',va='center',fontsize=10);ax.legend(bbox_to_anchor=(1.01,1),loc='upper left');fig.tight_layout()
for ext in ['png','svg']:fig.savefig(O/f'adjacent_boundary_evidence.{ext}',dpi=180,bbox_inches='tight')
plt.close(fig)
write('adjacent_boundary_counts.csv',[{'boundary':row[0],'context':c,'status':code,'count':sum(r['context']==c and r['continuity_code']==code for r in su),'paper_ids':';'.join(sorted({r['paper_id'] for r in su if r['context']==c and r['continuity_code']==code}))} for c,row in zip(contexts,rows) for code in codes])
doi='10.1038/s41598-025-33338-3';p=O/'recovered/DTMFU-44793dd305eb954a.pdf'
write('new_fulltext_decisions.csv',[{'record_id':'DTMFU-44793dd305eb954a','doi':doi,'decision':'include_primary','counting_stream':'domain_included','evidence_role':'S1 enabling geometry and error-assessment method','reason':'Semantic registration and adaptive UAV/LiDAR fusion are implemented and tested for building geometry. Consistent with the existing S1 enabling-module criterion, retain as domain-enabling evidence, not as demonstrated material-flow uncertainty transfer.','evidence_locator':'PDF pp6–9 architecture and equations12–14; pp11–14 Tables2–6; p15 limitations','uncertainty_boundary':'Segmentation-error propagation is explicitly left for future work (p11). RMSE reduction is measured reconstruction error, not calibrated posterior uncertainty. Time-series fusion is future work (p15).','source_path':str(p.resolve()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'assessment_scope':'Read extracted article body pp1–15; reference list excluded; figures not independently reproduced.'}])
write('doi_correction.csv',[{'record_id':'DTMFU-d52dc48a0eac5845','original_doi':'10.31387/oscm0640505','corrected_doi':'10.31387/oscm0640504','source':'https://journal.oscm-forum.org/publication/toc/oscm-volume-19-issue-1-2026','status':'Publisher title/authors/pages confirm correction. Original source identity retained. Correct article accessible in web PDF; local download returned403. Full eligibility decision still pending.'}])

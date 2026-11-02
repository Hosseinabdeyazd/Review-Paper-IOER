"""Build six evidence-linked figures, tables and a six-page PDF atlas.

Requires numpy, matplotlib and pypdf. Semantic decisions live in coding.py.
No keyword classifier or generated data. Run from any working directory.
"""
from pathlib import Path
import csv, json, hashlib, shutil, math, textwrap, html, zipfile
from collections import Counter
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Patch, Rectangle
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.ticker import MaxNLocator
from pypdf import PdfWriter, PdfReader
from coding import SDT, SDT_FEATURES, STAGES, DTU, DTU_FEATURES, NEGATIVE_NOTES

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parents[2]
FIG=ROOT/'figures'; INP=ROOT/'inputs'
FIG.mkdir(exist_ok=True);INP.mkdir(exist_ok=True)

def locate(rel):
    for b in [BASE,BASE/'analysis_ready']:
        if (b/rel).is_file():return b/rel
    raise FileNotFoundError(rel)

SOURCES={
 'sdt_extraction.csv':'Digital Twin Material Flow Review/bridge_searches/fulltext_review/extraction_14.csv',
 'dtu_extraction.csv':'Digital Twin Uncertainty Review/fulltext/fulltext_extraction.csv',
 'su_extraction.csv':'seleted papers S1-S5 + U/transition_extraction.csv',
 'su_theme_counts.csv':'Manuscript/content_profiles/theme_context_counts.csv',
 'su_context_assessments.csv':'Manuscript/content_profiles/article_context_assessments.csv',
 'su_positive_theme_assignments.csv':'Manuscript/content_profiles/positive_theme_assignments.csv',
 'su_codebook.csv':'Manuscript/content_profiles/codebook.csv',
 'synthesis_paths.csv':'Manuscript/relational_analysis/synthesis_paths.csv'}
for name,rel in SOURCES.items():
    if not (INP/name).exists():shutil.copyfile(locate(rel),INP/name)

def read(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(name,rows):
    rows=list(rows)
    with (ROOT/name).open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,list(rows[0]));w.writeheader();w.writerows(rows)
sdsrc={r['record_id']:r for r in read(INP/'sdt_extraction.csv')}
dusrc={r['publication_id']:r for r in read(INP/'dtu_extraction.csv')}
su=read(INP/'su_theme_counts.csv')
suass=read(INP/'su_context_assessments.csv')

# Complete coding records, including not-recorded cells, retain evidence and reasons.
sdrows=[]
for alias,pid,short,role,rtags,ctags,reason in SDT:
    src=sdsrc[pid];R=set(rtags.split());C=set(ctags.split())
    assert not (R&C) and src['evidence']!='abstract_only_pending_fulltext'
    for stage in STAGES:
        for feature,label in SDT_FEATURES:
            state='R' if stage+':'+feature in R else ('C' if stage+':'+feature in C else 'NR')
            sdrows.append({'alias':alias,'source_id':pid,'doi':src['doi'],'title':src['title'],
                           'role':role,'stage':stage,'feature':feature,'feature_label':label,'state':state,
                           'decision_reason':reason if state!='NR' else 'No positive coding for this stage/function in the archived extraction; not proof of absence.',
                           'evidence_anchor':src['location'],'source_field_evidence':src['architecture']+' | '+src['temporal_link'],
                           'source_file':'inputs/sdt_extraction.csv','basis':'Semantic review of archived extraction; no new fulltext reading'})
write('S_DT_complete_coding.csv',sdrows)
sdcounts=[]
for stage in STAGES:
    denom=len({r['source_id'] for r in sdrows if r['stage']==stage and r['state']=='R'})
    for feature,label in SDT_FEATURES:
        rset=sorted({r['alias'] for r in sdrows if r['stage']==stage and r['feature']==feature and r['state']=='R'})
        cset=sorted({r['alias'] for r in sdrows if r['stage']==stage and r['feature']==feature and r['state']=='C'})
        sdcounts.append({'stage':stage,'feature':feature,'label':label,'R_count':len(rset),'C_count':len(cset),
                         'R_aliases':';'.join(rset),'C_aliases':';'.join(cset),'stage_R_denominator':denom})
write('S_DT_counts.csv',sdcounts)

durows=[]
for pid,short,family,decisions in DTU:
    src=dusrc[pid];assert src['full_text_status'].startswith('read_')
    for feature,label in DTU_FEATURES:
        state,reason=decisions.get(feature,('NR',NEGATIVE_NOTES.get((pid,feature),'No positive coding for this mechanism in the archived appraisal; not a claim of absence.')))
        durows.append({'source_id':pid,'doi':src['DOI'],'title':src['Title'],'short_name':short,'architecture_family':family,
                       'feature':feature,'label':label.replace('\n',' '),'state':state,'decision_reason':reason,
                       'source_file':'inputs/dtu_extraction.csv','evidence_anchor':src['report_anchor'],
                       'version_examined':src['version_note'] or src['full_text_status'],
                       'basis':'Semantic review of archived fulltext appraisal; no new fulltext reading'})
write('DT_U_complete_coding.csv',durows)
ducounts=[]
for f,label in DTU_FEATURES:
    sets={s:sorted(r['source_id'] for r in durows if r['feature']==f and r['state']==s) for s in ['R','C']}
    ducounts.append({'feature':f,'label':label.replace('\n',' '),'R_count':len(sets['R']),'C_count':len(sets['C']),
                     'R_paper_ids':';'.join(sets['R']),'C_paper_ids':';'.join(sets['C']),'assessed_papers':13})
write('DT_U_counts.csv',ducounts)

REGISTER=[]
for stream,src,ids in [('S_DT',sdsrc,{x[1]:x[0] for x in SDT}),('DT_U',dusrc,{x[0]:x[0] for x in DTU})]:
    for pid,r in src.items():
        REGISTER.append({'stream':stream,'source_id':pid,'plot_alias':ids.get(pid,''),'doi':r.get('doi',r.get('DOI','')),
                         'title':r.get('title',r.get('Title','')),'included':int(pid in ids),
                         'access_status':r.get('evidence',r.get('full_text_status','')),
                         'reason':'Archived full-text assessment available' if pid in ids else 'Full-text assessment pending; excluded from content counts'})
write('new_coding_record_register.csv',REGISTER)

NAVY='#18384B'; BLUE='#347CA5'; TEAL='#247E78'; AMBER='#D99A31'; GREY='#E8EDF1'; PURPLE='#8768A8'; RED='#B8584D'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,
                     'svg.fonttype':'none','pdf.fonttype':42,'axes.titleweight':'bold','savefig.facecolor':'white'})
NAMES=[]
def save(fig,name):
    NAMES.append(name)
    for ext in ['png','svg','pdf']:fig.savefig(FIG/f'{name}.{ext}',dpi=165,bbox_inches='tight',pad_inches=.23)
    plt.close(fig)
def heading(fig,title,subtitle):
    fig.text(.035,.963,title,fontsize=21,fontweight='bold',color=NAVY,va='top')
    fig.text(.035,.915,subtitle,fontsize=10.5,color='#546371',va='top')
def wrap(s,n):return '\n'.join(textwrap.wrap(s,n))
def foot(fig,text,y=.025):fig.text(.035,y,text,fontsize=9,color='#546371',va='bottom')

# 01. Stage/uncertainty: same-paper counts plus separate continuity assessments.
contexts=['B12','B23','B34','B45','O5']; ctxlabels=['S1 → S2','S2 → S3','S3 → S4','S4 → S5','Other → S5*']
srcs=[r for r in su if r['dimension']=='source' and r['context']=='B12']
mat=np.array([[int(next(x['paper_count'] for x in su if x['dimension']=='source' and x['theme_code']==r['theme_code'] and x['context']==c)) for c in contexts] for r in srcs])
den=np.array([9,6,0,1,7]);pct=mat/np.where(den==0,np.nan,den)*100
fig=plt.figure(figsize=(16,10));heading(fig,'01  Stages × uncertainty','Recorded sources and continuity are different outcomes. Working set: 20 assessed papers; U10 excluded.')
gs=fig.add_gridspec(1,2,left=.32,right=.97,top=.80,bottom=.23,width_ratios=[1.1,1],wspace=.20)
ax=fig.add_subplot(gs[0]);bar=fig.add_subplot(gs[1])
cmap=plt.get_cmap('Blues').copy();cmap.set_bad(GREY)
ax.imshow(pct,cmap=cmap,vmin=0,vmax=100,aspect='auto')
ax.set_yticks(range(10),[wrap(r['theme_label'],34) for r in srcs],fontsize=10)
ax.set_xticks(range(5),ctxlabels,rotation=35,ha='right');ax.tick_params(length=0,pad=8)
for i in range(10):
    for j in range(5):ax.text(j,i,f'{mat[i,j]}/{den[j]}' if den[j] else '—',ha='center',va='center',color='white' if pct[i,j]>65 else NAVY,fontsize=10)
ax.set_title('Source coverage\nPapers / assessed context papers',pad=18,fontsize=12)
statecodes=['Q','N','R','S','P','E'];statecols=['#D4DDE5','#D97A71','#D7B654','#89A7CB','#58B8AE','#277266']
statelabels=['Discussion / review','Transfer not demonstrated','Propagation-ready inputs','Sensitivity / representation','Partial / limited transfer','Quantified output for selected U']
bottom=np.zeros(5)
for state,col,label in zip(statecodes,statecols,statelabels):
    v=np.array([sum(r['context']==c and r['continuity_code']==state and r['included_in_counts']=='1' for r in suass) for c in contexts])
    bar.bar(range(5),v,bottom=bottom,color=col,width=.65,label=label)
    for j,n in enumerate(v):
        if n:bar.text(j,bottom[j]+n/2,str(n),ha='center',va='center',color='white' if state=='E' else NAVY,fontweight='bold')
    bottom+=v
bar.set_xticks(range(5),ctxlabels,rotation=35,ha='right');bar.set_ylim(0,10.5);bar.yaxis.set_major_locator(MaxNLocator(integer=True))
bar.set_title('Continuity evidence\nOne assessment per paper–context',pad=18,fontsize=12)
bar.set_ylabel('Paper–context assessments');bar.grid(axis='y',alpha=.18);bar.set_axisbelow(True)
bar.legend(loc='upper right',frameon=False,fontsize=8.5,bbox_to_anchor=(1,.98))
bar.text(2,.25,'No assessed\narticle',ha='center',va='bottom',fontsize=8,color='#546371')
foot(fig,'* Other → S5 keeps factor-, quantity- and damage-to-impact studies separate from recovery → impact.',.10)
foot(fig,'Twenty papers yield 23 context assessments. Zero means not recorded in this extraction; grey means no assessed context.',.065)
foot(fig,'Quantified outputs for selected inputs do not establish a complete S1–S5 uncertainty chain.',.03)
save(fig,'01_stages_uncertainty')

# 02. S–DT functions: construction/cost analogues explicitly separated.
smat=np.array([[next(x['R_count'] for x in sdcounts if x['feature']==f and x['stage']==s) for s in STAGES] for f,_ in SDT_FEATURES])
cmat=np.array([[next(x['C_count'] for x in sdcounts if x['feature']==f and x['stage']==s) for s in STAGES] for f,_ in SDT_FEATURES])
stage_den=[next(x['stage_R_denominator'] for x in sdcounts if x['stage']==s) for s in STAGES]
fig=plt.figure(figsize=(16,9));heading(fig,'02  Stages × Digital Twin and enabling functions','Twelve assessed domain / enabling studies. Functions are counted; this is not a count of twelve validated DTs.')
gs=fig.add_gridspec(1,2,left=.30,right=.97,top=.79,bottom=.25,width_ratios=[1.5,1],wspace=.18)
ax=fig.add_subplot(gs[0]);bar=fig.add_subplot(gs[1],sharey=ax)
ax.imshow(smat,cmap='Blues',vmin=0,vmax=max(1,smat.max()),aspect='auto')
ax.set_yticks(range(9),[wrap(l,32) for _,l in SDT_FEATURES],fontsize=10)
labs=['S1\nAttributes','S2\nInventory','S3\nTime / flows','S4\nRecovery','S5\nImpacts','Adjacent*\nconstruction']
ax.set_xticks(range(6),labs,fontsize=9);ax.tick_params(length=0,pad=10)
for i in range(9):
    for j in range(6):
        a=smat[i,j];c=cmat[i,j]
        ax.text(j,i,f'{a}'+(f' + {c}C' if c else ''),ha='center',va='center',fontsize=10,color='white' if a>=4 else NAVY)
ax.axvline(4.5,color=AMBER,lw=3);ax.set_title('Described functions by stage\nC = conceptual / prospective only',fontsize=12,pad=18)
uniqueR=[len({r['source_id'] for r in sdrows if r['feature']==f and r['state']=='R'}) for f,_ in SDT_FEATURES]
uniqueC=[len({r['source_id'] for r in sdrows if r['feature']==f and r['state']=='C'}-{r['source_id'] for r in sdrows if r['feature']==f and r['state']=='R'}) for f,_ in SDT_FEATURES]
bar.barh(range(9),uniqueR,color=BLUE,label='Described method/function')
bar.barh(range(9),uniqueC,left=uniqueR,color=AMBER,label='Concept only in this record')
for i,(r,c) in enumerate(zip(uniqueR,uniqueC)):bar.text(r+c+.12,i,f'{r+c}/12',va='center',fontsize=9)
bar.tick_params(axis='y',left=False,labelleft=False);bar.set_xlim(0,12.8);bar.xaxis.set_major_locator(MaxNLocator(integer=True));bar.set_xlabel('Distinct papers per function')
bar.set_title('Function coverage\nOne paper counted once per row',fontsize=12,pad=18)
fig.legend(*bar.get_legend_handles_labels(),loc='lower center',bbox_to_anchor=(.63,.17),ncol=2,fontsize=9,frameon=False)
bar.grid(axis='x',alpha=.18);bar.set_axisbelow(True)
foot(fig,'Stage records with described functions: '+', '.join(f'{s}={n}' for s,n in zip(STAGES,stage_den))+'. Stage memberships overlap.',.125)
foot(fig,'* Adjacent construction logistics, cost and schedule studies are not relabelled as building-stock turnover.',.09)
foot(fig,'S3 includes retrospective event detection; S4 includes reuse information; neither label proves probabilistic flow/recovery modelling.',.055)
foot(fig,'Zero = not positively coded, not proven absence. Sparse S4/S5 coverage is a property of this subset, not the entire literature.',.02)
save(fig,'02_stages_dt_functions')

# 03. DT architecture profiles vs U mechanisms, all 13 assessed records visible.
features=[x[0] for x in DTU_FEATURES];ids=[x[0] for x in DTU]
dmat=np.array([[{'NR':0,'C':1,'R':2}[next(r['state'] for r in durows if r['source_id']==pid and r['feature']==f)] for f in features] for pid in ids])
fig=plt.figure(figsize=(16,11));heading(fig,'03  Digital Twin architectures × uncertainty mechanisms','Thirteen archived appraisals. Method description, conceptual support and missing positive coding remain separate.')
gs=fig.add_gridspec(2,1,left=.39,right=.97,top=.81,bottom=.20,height_ratios=[5,1.4],hspace=.08)
ax=fig.add_subplot(gs[0]);b=fig.add_subplot(gs[1],sharex=ax)
ax.imshow(dmat,cmap=ListedColormap(['#F0F3F5','#F2C779',BLUE]),norm=BoundaryNorm([-.5,.5,1.5,2.5],3),aspect='auto')
ax.set_yticks(range(13),[f'{pid[-3:]}  {short}' for pid,short,_,_ in DTU],fontsize=10);ax.tick_params(axis='x',bottom=False,labelbottom=False);ax.tick_params(axis='y',length=0,pad=10)
for i in range(13):
    for j in range(7):ax.text(j,i,['·','C','R'][dmat[i,j]],ha='center',va='center',color='white' if dmat[i,j]==2 else NAVY,fontsize=11,fontweight='bold')
for split in [2.5,3.5,4.5,7.5,10.5]:ax.axhline(split,color='white',lw=4)
family_starts=[]
for i,(_,_,fam,_) in enumerate(DTU):
    if i==0 or DTU[i-1][2]!=fam:family_starts.append((i,fam))
for n,(start,fam) in enumerate(family_starts):
    end=family_starts[n+1][0]-1 if n+1<len(family_starts) else 12
    ax.text(-.55,(start+end)/2,wrap(fam,14),transform=ax.get_yaxis_transform(),ha='center',va='center',fontsize=9,color=PURPLE,fontweight='bold')
rv=(dmat==2).sum(axis=0);cv=(dmat==1).sum(axis=0)
b.bar(range(7),rv,color=BLUE);b.bar(range(7),cv,bottom=rv,color=AMBER)
for j,(r,c) in enumerate(zip(rv,cv)):
    if r:b.text(j,r/2,str(r),ha='center',va='center',color='white',fontweight='bold')
    if c:b.text(j,r+c/2,str(c),ha='center',va='center',color=NAVY,fontweight='bold')
b.set_ylim(0,14);b.set_yticks([0,5,10]);b.set_ylabel('Papers',fontsize=9);b.set_xticks(range(7),[l for _,l in DTU_FEATURES],rotation=27,ha='right',fontsize=9)
fig.legend(handles=[Patch(color=BLUE,label='R: operational method described'),Patch(color=AMBER,label='C: review / proposal / future work'),Patch(color='#F0F3F5',label='·: not positively recorded')],loc='lower center',bbox_to_anchor=(.60,.077),ncol=3,frameon=False,fontsize=9)
foot(fig,'R does not mean independently validated. 004 is a preprint inference component; 015 is an adjacent control system.',.047)
foot(fig,'Joint/dependence transport is coded for the specified variables only. It does not establish end-to-end DT continuity.',.02)
save(fig,'03_dt_uncertainty_mechanisms')

# 04. Descriptive co-occurrence on ten method-level records, reviews excluded.
nonreview=[i for i,x in enumerate(DTU) if x[2]!='Review / reference architecture']
binary=(dmat[nonreview]==2).astype(int);assert binary.shape==(10,7)
def jaccard(X):
    inter=X.T@X;tot=X.sum(axis=0);union=tot[:,None]+tot[None,:]-inter
    return np.divide(inter,union,out=np.zeros_like(inter,dtype=float),where=union>0),inter
J,inter=jaccard(binary)
def cluster(D):
    groups={i:([i],i) for i in range(len(D))};merges=[];nextid=len(D)
    while len(groups)>1:
        keys=sorted(groups)
        candidates=[(float(np.mean(D[np.ix_(groups[a][0],groups[b][0])])),a,b) for ai,a in enumerate(keys) for b in keys[ai+1:]]
        height,a,b=min(candidates);ga,gb=groups.pop(a),groups.pop(b)
        members=ga[0]+gb[0];merges.append((a,b,height,len(members)));groups[nextid]=(members,nextid);nextid+=1
    return merges
merges=cluster(1-J)
def leaves(node):
    if node<7:return [node]
    a,b,_,_=merges[node-7];return leaves(a)+leaves(b)
order=leaves(12)
loo=np.array([jaccard(np.delete(binary,i,axis=0))[0] for i in range(10)])
pairrows=[]
for i,f in enumerate(features):
    for j,g in enumerate(features):
        pairrows.append({'feature_1':f,'feature_2':g,'joint_count':int(inter[i,j]),'jaccard':round(float(J[i,j]),4),
                         'leave_one_out_min':round(float(loo[:,i,j].min()),4),'leave_one_out_max':round(float(loo[:,i,j].max()),4),
                         'support_ids':';'.join(ids[nonreview[k]] for k in range(10) if binary[k,i] and binary[k,j])})
write('cooccurrence_and_sensitivity.csv',pairrows)
write('cluster_merges.csv',[{'left':a,'right':b,'average_jaccard_distance':d,'members':n} for a,b,d,n in merges])
fig=plt.figure(figsize=(13,10));heading(fig,'04  Which uncertainty mechanisms occur together?','Exploratory average-linkage clustering of ten method-level records. Reviews and conceptual-only tags are excluded.')
gs=fig.add_gridspec(1,2,left=.07,right=.74,top=.80,bottom=.28,width_ratios=[1,4],wspace=.03)
tree=fig.add_subplot(gs[0]);ax=fig.add_subplot(gs[1]);pos={f:order.index(f) for f in range(7)};height={i:0 for i in range(7)}
for k,(a,b,h,n) in enumerate(merges):
    ya,yb=pos[a],pos[b];tree.plot([height[a],h,h,height[b]],[ya,ya,yb,yb],color='#718594',lw=1.6);pos[7+k]=(ya+yb)/2;height[7+k]=h
tree.set_xlim(max(height.values())*1.07,-.015);tree.set_ylim(6.5,-.5);tree.set_yticks([]);tree.set_xlabel('Jaccard\ndistance',fontsize=9);tree.spines[['left','top','right']].set_visible(False)
im=ax.imshow(J[np.ix_(order,order)],vmin=0,vmax=1,cmap='YlGnBu',aspect='auto')
labels=[DTU_FEATURES[k][1] for k in order]
ax.set_xticks(range(7),labels,rotation=35,ha='right',fontsize=9);ax.set_yticks(range(7),labels,fontsize=9);ax.yaxis.tick_right();ax.tick_params(length=0,pad=10)
for i,a in enumerate(order):
    for j,bx in enumerate(order):
        v=J[a,bx];ax.text(j,i,f'{v:.2f}\nn={inter[a,bx]}',ha='center',va='center',fontsize=9,color='white' if v>.55 else NAVY)
cb=fig.add_axes([.47,.855,.24,.012]);fig.colorbar(im,cax=cb,orientation='horizontal',label='Jaccard similarity')
foot(fig,'Each cell shows similarity and the number of records reporting both methods. Clusters describe this selected working set.',.135)
foot(fig,'Co-occurrence does not establish model coupling, causation or independent corroboration. Related author/study families remain a limitation.',.095)
foot(fig,'Leave-one-record-out ranges are provided in the CSV. No significance test or stable architectural taxonomy is claimed.',.055)
save(fig,'04_method_cooccurrence')

# Drawing helpers for evidence and architecture plates.
def box(ax,x,y,w,h,face=GREY,edge='none',lw=1.2,ls='-',radius=.012):
    p=FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0.008,rounding_size={radius}',facecolor=face,edgecolor=edge,linewidth=lw,linestyle=ls)
    ax.add_patch(p);return p
def txt(ax,x,y,s,size=10,color=NAVY,weight='normal',ha='left',va='top'):
    return ax.text(x,y,s,fontsize=size,color=color,fontweight=weight,ha=ha,va=va,linespacing=1.45)
def arrow(ax,start,end,color=AMBER,ls='--',lw=1.6):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=13,color=color,linestyle=ls,linewidth=lw))

# 05. Four evidence-to-design paths; arrows are explicit synthesis, not measured flows.
fig=plt.figure(figsize=(18,10));heading(fig,'05  Connecting the three evidence streams','Four boundary-specific syntheses. Existing mechanisms are not automatically validated in the material-flow domain.')
ax=fig.add_axes([.025,.12,.95,.72]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
xs=[.00,.11,.335,.56,.785];ws=[.085,.20,.20,.20,.20]
headers=['Boundary','S–U: requirement / gap','S–DT: domain function','DT–U: candidate mechanism','Synthesis / proposed addition']
for x,w,h in zip(xs,ws,headers):txt(ax,x+.008,.99,wrap(h,26),11,weight='bold')
paths=[
 ('S1 → S2','U03 / U05 / U06\nAttribute and MI variability\nmay become point inventory.','B05 / B03\nBIM–GIS quantity mapping;\nalternatives can be averaged.','004 / 016\nConditional or covariance\nrepresentations preserve\nselected dependencies.','Keep material alternatives,\nshared dependencies and\nuncertainty through the\nquantity interface.'),
 ('S2 → S3','U11 / U12 / U18\nLifetime and stock assumptions\nchange flow timing.','B03\nLayer masses + service lives\nproduce annual outflow CSV.','004 / 016\nSequential inference and\nmeasured feedback can\nupdate represented states.','Link inventory realizations\nto conditioned lifetime\nmodels; revise with\nnew event evidence.'),
 ('S3 → S4','Selected-set gap\nNo assessed direct uncertainty\nchain from outflow to\nrecoverable quality.','B04 / B11\nReuse/disassembly information;\nnot a verified probabilistic\nrecovery-state transition.','018 (analogy)\nConsistency / prognostics\nmechanisms; own covariance\nhandoff remains limited.','Specify condition, damage,\ncontamination and routing\ninterfaces. Domain data\nand validation are required.'),
 ('S4 → S5','U19\nShared recovery inputs;\njoint draws and dependence\ninsufficiently documented.','Not established here\nFocused domain bridge set\ndoes not establish a direct\nS4–S5 DT architecture.','016 (analogy)\nCovariance/cross-covariance\ntransport for represented\nperformance quantities.','Define joint recovery-to-\nimpact input realizations\nand burden/credit mappings;\nvalidate in the target domain.')]
for row,data in enumerate(paths):
    y=.70-row*.225
    for col,(x,w,text) in enumerate(zip(xs,ws,data)):
        face=['#EEF2F5','#E5F1EE','#E8F0F7','#EEE8F4','#FFF0D8'][col]
        box(ax,x+.004,y,w,.18,face=face,edge=AMBER if col==4 else 'none',ls='--' if col==4 else '-')
        txt(ax,x+.015,y+.163,text,10 if col else 12,weight='bold' if col==0 else 'normal')
        if col in [1,2,3]:arrow(ax,(x+w+.008,y+.09),(xs[col+1]-.003,y+.09),color=AMBER)
foot(fig,'B aliases identify domain/enabling papers; numeric 004/016/018 labels identify DTUM studies. Full identifiers, DOIs and rationales are in the CSVs.',.065)
foot(fig,'Dashed arrows are reviewer synthesis/proposals. Missing direct evidence is retained; no complete deployed S1–S5 system is claimed.',.025)
save(fig,'05_evidence_to_architecture')

# 06. Synthesized architecture, with proposed U contracts visibly separated.
fig=plt.figure(figsize=(19,12));heading(fig,'06  A synthesized architecture for uncertainty continuity','Material-flow functions are evidence-informed. The integrated architecture and its uncertainty-carrying interfaces are proposals for evaluation.')
ax=fig.add_axes([.025,.12,.95,.73]);ax.set_xlim(-.01,1.01);ax.set_ylim(0,1);ax.axis('off')
xlist=[.005,.207,.409,.611,.813];w=.18
stages=[
 ('S1','Observe / infer','Geometry, typology,\nmaterial class, condition','Attribute uncertainty','U03 / U06; B05 / B13'),
 ('S2','Build inventory','Material quantities,\ncomposition and hierarchy','Quantity / composition U','U05 / U07; B01 / B03'),
 ('S3','Model stock change','Service lives, interventions,\nrelease timing and flows','Time-indexed flow U','U11 / U12 / U18; B03'),
 ('S4','Assess recovery','Recoverability, quality,\nreuse / recycling routes','Recoverable quantity / quality U','U19; B04 / B11 (information)'),
 ('S5','Assess consequences','Environmental burdens,\ncredits and alternatives','Impact / decision U','U16 / U19; B12 (analogue)')]
for i,(s,title,body,out,refs) in enumerate(stages):
    x=xlist[i];box(ax,x,.715,w,.23,face='#E8F0F7',edge=BLUE)
    txt(ax,x+.012,.927,s+'  '+title,11,weight='bold');txt(ax,x+.012,.875,body,10)
    txt(ax,x+.012,.805,wrap(out,25),9.5,color=TEAL,weight='bold');txt(ax,x+.012,.748,refs,7.8,color='#526B7D')
    if i<4:arrow(ax,(x+w+.003,.83),(xlist[i+1]-.004,.83));txt(ax,x+w+.011,.865,'P',9,color=AMBER,weight='bold',ha='center')
txt(ax,.50,.700,'P  •  Shared uncertainty record carried through every proposed interface',12,color='#A46A13',weight='bold',ha='center')
box(ax,.005,.56,.988,.095,face='#FFF2DD',edge=AMBER,ls='--',lw=1.6)
txt(ax,.025,.635,'Entity / material / event ID   ·   value + units   ·   distribution / alternatives / samples   ·   dependency references',10.5,weight='bold')
txt(ax,.025,.599,'Source + model version   ·   timestamp + validity   ·   source/target scale   ·   transformation + discarded information',10.5)
for x in xlist:arrow(ax,(x+w/2,.71),(x+w/2,.66),lw=1.2)
modules=[
 (.005,'S  Propagation and dependence','Carry conditional distributions, shared\nrealizations or covariance as appropriate.\nAudit approximations at model boundaries.','Generic support: DTUM-004 / 016'),
 (.345,'S  Consistency and updating','Compare predictions and observations;\ncheck shift / coverage; trigger new data,\nparameter updates or model revision.','Generic support: DTUM-012 / 013 / 018'),
 (.685,'S  Decision and communication','Expose uncertain alternatives, missing\nevidence and threshold exceedance;\nlink outputs to decision requirements.','Generic support: DTUM-002 / 012 / 015 / 018')]
for x,title,body,refs in modules:
    box(ax,x,.27,.307,.235,face='#EEEAF4',edge=PURPLE)
    txt(ax,x+.015,.486,title,11,weight='bold',color='#5C4678');txt(ax,x+.015,.434,body,10);txt(ax,x+.015,.302,refs,8.5,color='#5C4678')
    arrow(ax,(x+.153,.554),(x+.153,.51),color=PURPLE,ls='-')
txt(ax,.5,.238,'P  •  Cross-cutting interface requirements',11,color='#A46A13',weight='bold',ha='center')
cross=[(.005,'SPACE','Source → target scale;\naggregation and shared dependence'),(.345,'TIME','Event resolution; update interval;\nprediction horizon; decision timing'),(.685,'INFORMATION ROLES','Data producer; model maintainer;\nvalidator; decision recipient')]
for x,title,body in cross:
    box(ax,x,.09,.307,.12,face='#F5F6F8',edge='#AEBAC4',ls='--');txt(ax,x+.015,.192,title,9.5,weight='bold');txt(ax,x+.015,.157,body,9)
txt(ax,.5,.045,'Priority gap: S3 → S4. Recoverable quality / routing requires domain evidence and validation.',11,color=RED,weight='bold',ha='center')
foot(fig,'S = cross-study synthesis. P = proposed domain addition / interface. Source IDs support individual functions or mechanisms, not the whole assembly.',.065)
foot(fig,'No universal scalability, real-time requirement or end-to-end validation is claimed. The purpose is to make every proposed connection testable.',.025)
save(fig,'06_synthesized_architecture')

# Consolidated portable reading copy.
writer=PdfWriter()
for name in NAMES:writer.append(str(FIG/f'{name}.pdf'))
with (ROOT/'Results_Atlas.pdf').open('wb') as f:writer.write(f)
assert len(PdfReader(ROOT/'Results_Atlas.pdf').pages)==6

summary={'S_U_counted_papers':20,'S_U_context_assessments':23,'S_DT_counted_papers':12,'S_DT_pending':2,
         'S_DT_stage_described_denominators':dict(zip(STAGES,stage_den)),'DT_U_counted_papers':13,'DT_U_pending':5,
         'DT_U_method_level_records_for_cooccurrence':10,'DT_U_R_counts':dict(zip(features,map(int,(dmat==2).sum(axis=0)))),
         'DT_U_C_counts':dict(zip(features,map(int,(dmat==1).sum(axis=0)))),
         'figures':NAMES,'pdf_atlas_pages':6,'new_fulltext_reading':False,'new_semantic_coding_of_archived_extraction':True,
         'independent_human_validation':False,'inferential_significance_test':False,
         'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in INP.iterdir() if p.is_file()}}
assert len(sdsrc)==14 and len(dusrc)==18 and len(SDT)==12 and len(DTU)==13
assert len(sdrows)==12*6*9 and len(durows)==13*7
assert not any(x['doi']=='' and x['source_id']!='DTMFB-2394c459ec04' for x in REGISTER if x['stream']=='S_DT' and x['included'])
assert np.allclose(J,J.T) and np.allclose(np.diag(J),1)
(ROOT/'validation.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')

cards=''.join(f'<section><h2>{html.escape(name.replace("_"," "))}</h2><a href="figures/{name}.pdf"><img src="figures/{name}.png" alt="{name}"></a><p><a href="figures/{name}.pdf">PDF</a> · <a href="figures/{name}.svg">SVG</a> · <a href="figures/{name}.png">PNG</a></p></section>' for name in NAMES)
(ROOT/'gallery.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>Stages, DT and uncertainty — Results atlas</title><style>body{margin:40px auto;max-width:1500px;background:#f2f5f7;color:#18384b;font:17px system-ui}header,section{background:white;padding:25px;margin:24px;border-radius:10px}img{width:100%;height:auto}a{color:#276a94}h1{font-size:32px}h2{font-size:20px}</style><header><h1>Stages, Digital Twin and uncertainty</h1><p>Six evidence-linked figures. Semantic coding of archived working-set extractions; no new full-text review or inferential significance claim.</p><a href="Results_Atlas.pdf">Open the six-page PDF atlas</a> · <a href="README.md">Scope and methods</a></header>'+cards+'</html>',encoding='utf-8')
print(json.dumps(summary,indent=2))

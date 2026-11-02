"""Pure aggregation of existing paper-level codes; no proposed architecture edges.

Input semantics are inherited from results/. This script adds no article labels.
Every plotted connection/configuration has source IDs in its exported table.
"""
from pathlib import Path
from collections import Counter, defaultdict
import csv, json, math, hashlib, html, textwrap, xml.etree.ElementTree as ET
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.path import Path as MPath
from matplotlib.patches import PathPatch, Rectangle
from matplotlib.lines import Line2D
from matplotlib.colors import Normalize
from pypdf import PdfWriter, PdfReader

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'results'
FIG=ROOT/'figures'; FIG.mkdir(parents=True,exist_ok=True)
def read(rel):
    with (SOURCE/rel).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(name,rows):
    with (ROOT/name).open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,list(rows[0]));w.writeheader();w.writerows(rows)
def wrap(s,n):return '\n'.join(textwrap.wrap(s,n))
NAVY='#17364A'; TEAL='#287F7A'; BLUE='#337FA8'; GOLD='#C48730'; GRAY='#DDE5EB'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'svg.fonttype':'none','pdf.fonttype':42,
    'axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white'})
NAMES=[];TIPS={}
def heading(fig,title,subtitle):
    fig.text(.035,.963,title,fontsize=21,weight='bold',color=NAVY,va='top')
    fig.text(.035,.91,subtitle,fontsize=11,color='#526676',va='top')
def foot(fig,s,y):fig.text(.035,y,s,fontsize=9.5,color='#526676',va='bottom')
def save(fig,name):
    NAMES.append(name)
    for ext in ('png','pdf','svg'):fig.savefig(FIG/f'{name}.{ext}',dpi=180,bbox_inches='tight',pad_inches=.25)
    plt.close(fig)
    # Native SVG hover text exposes the records behind each network edge.
    p=FIG/f'{name}.svg';tree=ET.parse(p);ns='{http://www.w3.org/2000/svg}'
    for e in tree.iter():
        gid=e.attrib.get('id')
        if gid in TIPS:
            title=ET.Element(ns+'title');title.text=TIPS[gid];e.insert(0,title)
    tree.write(p,encoding='utf-8',xml_declaration=True)

ass=[r for r in read('inputs/su_context_assessments.csv') if r['included_in_counts']=='1']
assert len({(r['paper_id'],r['context']) for r in ass})==len(ass)
positive=[r for r in read('inputs/su_positive_theme_assignments.csv') if r['counted']=='1']
sd=read('S_DT_complete_coding.csv');du=read('DT_U_complete_coding.csv')
book=read('inputs/su_codebook.csv')

# D01: a conserved distribution of assessments, never a physical/U flow.
context_labels={'B12':'S1 → S2','B23':'S2 → S3','B34':'S3 → S4','B45':'S4 → S5','O5':'Other inputs → S5'}
status_labels={'Q':'Discussion / review','N':'Downstream transfer not demonstrated',
    'R':'Inputs prepared for propagation','S':'Sensitivity / representation comparison',
    'P':'Partial / incompletely documented transfer','E':'Quantified outputs for selected uncertain inputs'}
status_colors={'Q':'#90A0AD','N':'#C86C65','R':'#D8AA4A','S':'#7D9CC4','P':'#53A79D','E':'#28745E'}
boundary_edges=[]
for c in context_labels:
    for s in status_labels:
        rows=[r for r in ass if r['context']==c and r['continuity_code']==s]
        boundary_edges.append({'context':c,'context_label':context_labels[c],'continuity':s,'continuity_label':status_labels[s],
            'assessments':len(rows),'paper_ids':';'.join(r['paper_id'] for r in rows),'dois':';'.join(r['doi'] for r in rows),
            'unit':'paper-context assessment','source':'results/inputs/su_context_assessments.csv'})
write('S_U_boundary_continuity_edges.csv',boundary_edges)
LC=Counter(r['context'] for r in ass);RC=Counter(r['continuity_code'] for r in ass)
total=len(ass);scale=.58/total
left={};right={};cursor=.88
for k in context_labels:
    if not LC[k]:continue
    left[k]=(cursor-LC[k]*scale,cursor);cursor-=LC[k]*scale+.04
cursor=.88
for k in status_labels:
    if not RC[k]:continue
    right[k]=(cursor-RC[k]*scale,cursor);cursor-=RC[k]*scale+.025
fig=plt.figure(figsize=(16,10));heading(fig,'D01  Where is uncertainty continuity documented?',
    f'Computed distribution of {total} paper–context assessments from {len(set(r["paper_id"] for r in ass))} publications. Ribbon width = assessment count.')
ax=fig.add_axes([.025,.17,.95,.66]);ax.set_xlim(0,1);ax.set_ylim(.10,.96);ax.axis('off')
x0,x1=.24,.66
lo={k:v[1] for k,v in left.items()};ro={k:v[1] for k,v in right.items()}
for row in boundary_edges:
    n=row['assessments'];c=row['context'];s=row['continuity']
    if not n:continue
    ya=lo[c];yb=ro[s];h=n*scale;lo[c]-=h;ro[s]-=h
    verts=[(x0,ya),(x0+.17,ya),(x1-.17,yb),(x1,yb),(x1,yb-h),
           (x1-.17,yb-h),(x0+.17,ya-h),(x0,ya-h),(x0,ya)]
    codes=[MPath.MOVETO,MPath.CURVE4,MPath.CURVE4,MPath.CURVE4,MPath.LINETO,MPath.CURVE4,MPath.CURVE4,MPath.CURVE4,MPath.CLOSEPOLY]
    patch=PathPatch(MPath(verts,codes),facecolor=status_colors[s],edgecolor='white',lw=.6,alpha=.65)
    gid=f'boundary_{c}_{s}';patch.set_gid(gid);TIPS[gid]=f'{context_labels[c]} | {status_labels[s]} | n={n} | {row["paper_ids"]}'
    ax.add_patch(patch);ax.text(x0+.018,ya-h/2,str(n),va='center',ha='left',fontsize=9,color=NAVY,weight='bold')
for c,(bottom,top) in left.items():
    ax.add_patch(Rectangle((x0-.012,bottom),.012,top-bottom,color=BLUE))
    ax.text(x0-.026,(bottom+top)/2,f'{context_labels[c]}\nn = {LC[c]}',ha='right',va='center',fontsize=12,color=NAVY)
for s,(bottom,top) in right.items():
    ax.add_patch(Rectangle((x1,bottom),.012,top-bottom,color=status_colors[s]))
    ax.text(x1+.027,(bottom+top)/2,wrap(status_labels[s],35)+f'  (n={RC[s]})',ha='left',va='center',fontsize=10.5,color=NAVY)
ax.text(x0,.95,'ASSESSED BOUNDARY',ha='center',fontsize=10,weight='bold',color=NAVY)
ax.text(x1,.95,'RECORDED CONTINUITY STATUS',ha='center',fontsize=10,weight='bold',color=NAVY)
foot(fig,'S3 → S4: no assessed article in this selected set; it has no ribbon. This is not proof of absence in the wider literature.',.105)
foot(fig,'Each assessment has exactly one status. Multiple contexts from one publication remain dependent observations.',.065)
foot(fig,'Ribbons classify evidence records; they do not show physical material flow or measured transfer of uncertainty.',.025)
save(fig,'D01_boundary_continuity_alluvial')

# D02: weighted bipartite incidence network, only observed R-coded pairs.
stage_order=['S1','S2','S3','S4','S5']
stage_labels=['Attributes','Inventory','Time / flows','Recovery','Impacts']
stage_colors=dict(zip(stage_order,['#357FA3','#278D88','#9477B5','#D2943E','#B96765']))
features=list(dict.fromkeys(r['feature'] for r in sd))
flabel={r['feature']:r['feature_label'] for r in sd}
domain=[r for r in sd if r['stage'] in stage_order and r['state']=='R']
domain_ids={r['source_id'] for r in domain}
adjacent_only={r['source_id'] for r in sd if r['state']=='R'}-domain_ids
edge_rows=[]
for s in stage_order:
    for f in features:
        rows=[r for r in domain if r['stage']==s and r['feature']==f]
        edge_rows.append({'stage':s,'feature':f,'feature_label':flabel[f],'paper_count':len(rows),
          'paper_ids':';'.join(r['source_id'] for r in rows),'aliases':';'.join(r['alias'] for r in rows),
          'dois':';'.join(r['doi'] for r in rows),'unit':'distinct publication within stage-function pair',
          'source':'results/S_DT_complete_coding.csv','relation':'coded function in stage; not a directed interface'})
write('S_DT_stage_function_edges.csv',edge_rows)
nonzero=[r for r in edge_rows if r['paper_count']]
frequency_stage={s:len({r['source_id'] for r in domain if r['stage']==s}) for s in stage_order}
frequency_feature={f:len({r['source_id'] for r in domain if r['feature']==f}) for f in features}
def bary(f):
    cells=[r for r in nonzero if r['feature']==f]
    return sum(stage_order.index(r['stage'])*r['paper_count'] for r in cells)/sum(r['paper_count'] for r in cells)
f_order=sorted((f for f in features if frequency_feature[f]),key=lambda f:(bary(f),features.index(f)))
ly=dict(zip(stage_order,np.linspace(.89,.15,5)));ry=dict(zip(f_order,np.linspace(.94,.10,len(f_order))))
fig=plt.figure(figsize=(16,10));heading(fig,'D02  Which DT/enabling functions occur at each stage?',
    f'Weighted network from R-coded stage–function cells: {len(domain_ids)} records with S1–S5 functions; {len(adjacent_only)} adjacent-only records are kept outside this graph.')
ax=fig.add_axes([.035,.18,.93,.64]);ax.set_xlim(0,1);ax.set_ylim(.035,1.015);ax.axis('off')
for row in sorted(nonzero,key=lambda r:-r['paper_count']):
    s,f,n=row['stage'],row['feature'],row['paper_count']
    path=MPath([(.235,ly[s]),(.43,ly[s]),(.47,ry[f]),(.66,ry[f])],[MPath.MOVETO]+[MPath.CURVE4]*3)
    patch=PathPatch(path,facecolor='none',edgecolor=stage_colors[s],lw=1.0*n,alpha=.60)
    gid=f'stage_function_{s}_{f}';patch.set_gid(gid);TIPS[gid]=f'{s} | {flabel[f]} | n={n} | {row["aliases"]}'
    ax.add_patch(patch)
for s,label in zip(stage_order,stage_labels):
    n=frequency_stage[s];ax.scatter(.235,ly[s],s=220+55*n,color=stage_colors[s],edgecolor='white',lw=1.5,zorder=4)
    ax.text(.205,ly[s],f'{s}  {label}\n{n} papers',ha='right',va='center',fontsize=12,color=NAVY)
for f in f_order:
    n=frequency_feature[f];ax.scatter(.66,ry[f],s=170+45*n,color=BLUE,edgecolor='white',lw=1.5,zorder=4)
    ax.text(.69,ry[f],wrap(flabel[f],38)+f'  (n={n})',ha='left',va='center',fontsize=10.5,color=NAVY)
fig.legend(handles=[Line2D([0],[0],color='#617D8C',lw=n,label=f'{n} shared '+('paper' if n==1 else 'papers')) for n in (1,3,7)],
    loc='lower center',bbox_to_anchor=(.53,.115),ncol=3,frameon=False,fontsize=10)
foot(fig,'Node area reflects distinct supporting papers. Edge width = papers with that exact stage–function code; all positive edges are shown.',.085)
foot(fig,'Nodes and edges overlap in membership and must not be summed as unique papers. SVG hover labels and the CSV identify each supporting record.',.05)
foot(fig,'A connection means the function is coded at that stage. It is not evidence of uncertainty propagation or a working interface between stages.',.015)
save(fig,'D02_stage_function_network')

# D03: exact observed binary configurations, without reviewer-defined families.
mechanisms=list(dict.fromkeys(r['feature'] for r in du))
mlabel={r['feature']:r['label'] for r in du}
method_ids=sorted({r['source_id'] for r in du if r['architecture_family']!='Review / reference architecture'})
sets={p:frozenset(r['feature'] for r in du if r['source_id']==p and r['state']=='R') for p in method_ids}
groups=defaultdict(list)
for p,s in sets.items():groups[tuple(int(f in s) for f in mechanisms)].append(p)
patterns=sorted(groups,key=lambda k:(-len(groups[k]),-sum(k),tuple(-v for v in k)))
configs=[];members=[]
for i,pat in enumerate(patterns):
    name=f'C{i+1:02d}';papers=groups[pat]
    configs.append({'configuration':name,'paper_count':len(papers),'mechanism_count':sum(pat),
       'mechanisms':';'.join(f for f,v in zip(mechanisms,pat) if v),'paper_ids':';'.join(papers),
       'dois':';'.join(next(r['doi'] for r in du if r['source_id']==p) for p in papers),
       'definition':'exact set of R-coded mechanisms; C and NR do not enter the positive set'})
    for p in papers:members.append({'paper_id':p,'configuration':name,**dict(zip(mechanisms,pat))})
write('DT_U_exact_configurations.csv',configs);write('DT_U_configuration_membership.csv',members)
freq=[sum(f in s for s in sets.values()) for f in mechanisms]
fig=plt.figure(figsize=(16,10));heading(fig,'D03  Which uncertainty configurations are actually recorded?',
    f'Exact intersection analysis of {len(method_ids)} non-review records and {len(mechanisms)} mechanisms; {len(patterns)} distinct positive-code configurations.')
gs=fig.add_gridspec(2,2,left=.32,right=.96,bottom=.21,top=.78,width_ratios=[1,3.5],height_ratios=[1.15,2.5],hspace=.13,wspace=.12)
bar=fig.add_subplot(gs[1,0]);matrix=fig.add_subplot(gs[1,1]);top=fig.add_subplot(gs[0,1],sharex=matrix)
bar.barh(range(len(mechanisms)),freq,color=BLUE,height=.60)
bar.set_yticks(range(len(mechanisms)),[wrap(mlabel[f],30) for f in mechanisms],fontsize=10);bar.invert_yaxis();bar.set_xlim(0,10)
bar.set_ylim(len(mechanisms)-.5,-.5);bar.set_xticks([0,5,10]);bar.set_xlabel('Papers with mechanism',fontsize=9)
for i,n in enumerate(freq):bar.text(n+.15,i,str(n),va='center',fontsize=10,color=NAVY)
matrix.set_ylim(len(mechanisms)-.5,-.5);matrix.set_xlim(-.6,len(patterns)-.4)
matrix.set_yticks([]);matrix.set_xticks(range(len(patterns)),[r['configuration'] for r in configs],fontsize=10)
for j,pat in enumerate(patterns):
    active=[i for i,v in enumerate(pat) if v]
    matrix.axvspan(j-.45,j+.45,color='#F0F4F6' if j%2==0 else 'white',zorder=0)
    matrix.scatter([j]*len(mechanisms),range(len(mechanisms)),s=24,color='#D5DEE4')
    matrix.plot([j,j],[min(active),max(active)],lw=2.2,color=TEAL,zorder=2)
    matrix.scatter([j]*len(active),active,s=80,color=TEAL,zorder=3)
top.bar(range(len(patterns)),[len(groups[p]) for p in patterns],color=TEAL,width=.60)
top.set_ylim(0,max(len(v) for v in groups.values())+1.2);top.set_yticks([0,1,2,3]);top.set_ylabel('Papers in exact set',fontsize=10)
top.tick_params(axis='x',bottom=False,labelbottom=False)
for j,p in enumerate(patterns):
    n=len(groups[p]);top.text(j,n+.12,str(n),ha='center',weight='bold',fontsize=11,color=NAVY)
    top.text(j,n+.42,'\n'.join(x.replace('DTUM-','') for x in groups[p]),ha='center',fontsize=9,color='#526676')
matrix.spines[['left','right','top']].set_visible(False)
foot(fig,'Each column is an observed exact set, not an architecture proposed by the reviewer. Each paper enters exactly one column.',.125)
foot(fig,'Filled circles indicate R-coded methods. Grey circles mean no positive R code; conceptual support and unrecorded features remain distinct in the source CSV.',.085)
foot(fig,'Top bars sum to ten records. Three-digit labels identify sources (DTUM prefix omitted). Similar code sets do not establish identical implementations.',.045)
save(fig,'D03_exact_uncertainty_configurations')

# D04: only same-paper, same-context source/method associations.
source_codes=[r['code'] for r in book if r['dimension']=='source']
method_codes=[r['code'] for r in book if r['dimension']=='method']
names={r['code']:r['label'] for r in book}
source_sets={f:{(r['paper_id'],r['context']) for r in positive if r['dimension']=='source' and r['theme_code']==f} for f in source_codes}
method_sets={f:{(r['paper_id'],r['context']) for r in positive if r['dimension']=='method' and r['theme_code']==f} for f in method_codes}
source_sort=sorted(source_codes,key=lambda f:(-len(source_sets[f]),source_codes.index(f)))
method_sort=sorted(method_codes,key=lambda f:(-len(method_sets[f]),method_codes.index(f)))
pair_rows=[]
for s in source_codes:
    for m in method_codes:
        shared=sorted(source_sets[s]&method_sets[m]);N=len(source_sets[s])
        pair_rows.append({'source_code':s,'source_label':names[s],'method_code':m,'method_label':names[m],
          'shared_assessments':len(shared),'source_assessments':N,'percent_of_source_assessments':round(100*len(shared)/N,2) if N else '',
          'assessment_ids':';'.join(p+'@'+c for p,c in shared),'paper_ids':';'.join(sorted({p for p,c in shared})),
          'dois':';'.join(sorted({r['doi'] for r in ass if (r['paper_id'],r['context']) in shared})),
          'unit':'same-paper same-context association','source':'results/inputs/su_positive_theme_assignments.csv'})
write('S_U_source_method_edges.csv',pair_rows)
fig=plt.figure(figsize=(16,11));heading(fig,'D04  Which analysis methods accompany each uncertainty source?',
    'Computed same-paper, same-context associations. Bubble area = assessment count; colour = share of that source’s assessments.')
ax=fig.add_axes([.32,.29,.62,.51]);norm=Normalize(0,100);cmap=plt.get_cmap('YlGnBu')
for i,s in enumerate(source_sort):
    for j,m in enumerate(method_sort):
        n=len(source_sets[s]&method_sets[m]);pct=100*n/len(source_sets[s]) if source_sets[s] else 0
        if n:
            ax.scatter(j,i,s=n*150,c=[pct],cmap=cmap,norm=norm,edgecolor='#738D9F',lw=.6)
            ax.text(j,i,str(n),ha='center',va='center',fontsize=10,color='white' if pct>65 else NAVY,weight='bold')
        else:ax.scatter(j,i,s=8,color='#D9E1E7')
ax.set_xlim(-.6,len(method_sort)-.4);ax.set_ylim(len(source_sort)-.4,-.6)
ax.set_yticks(range(len(source_sort)),[wrap(names[s],32)+f'  (N={len(source_sets[s])})' for s in source_sort],fontsize=10)
short={'qualitative':'Qualitative\nassessment','validation':'Prediction-error\ndiagnostics','ranges':'Range / distribution\nrepresentation','sampling':'Probabilistic\nsampling','bootstrap':'Output-UQ\nbootstrap','sensitivity':'Sensitivity /\nrepresentation','scenarios':'Scenario\ncomparison','conditional':'Conditional\nconsequences','proxy':'Proxy /\naggregation','review':'Review\nsynthesis'}
ax.set_xticks(range(len(method_sort)),[short[m] for m in method_sort],rotation=38,ha='right',fontsize=9.5)
ax.tick_params(length=0,pad=12);ax.spines[['left','right','top','bottom']].set_visible(False)
cb=fig.add_axes([.56,.85,.27,.012]);fig.colorbar(plt.cm.ScalarMappable(norm=norm,cmap=cmap),cax=cb,orientation='horizontal',label='Share of source assessments (%)')
fig.legend(handles=[plt.scatter([],[],s=n*150,color='#91BBCB',edgecolor='#738D9F',label=f'n={n}') for n in (1,3,5)],
    loc='lower center',bbox_to_anchor=(.67,.155),frameon=False,ncol=3,fontsize=10)
foot(fig,'Only codes within the identical publication and boundary are joined. Multiple sources/methods can occur in one assessment; cells are not additive.',.105)
foot(fig,'The labels describe sources, not automatically epistemic/aleatory categories. A method association does not prove uncertainty transfer.',.065)
foot(fig,'Zero is no recorded association in this extraction; N is the number of assessed contexts carrying that source. All edges and supporting IDs are exported.',.025)
save(fig,'D04_uncertainty_source_method_associations')

writer=PdfWriter()
for name in NAMES:writer.append(str(FIG/f'{name}.pdf'))
with (ROOT/'Data_Derived_Diagrams.pdf').open('wb') as f:writer.write(f)
sources=['S_DT_complete_coding.csv','DT_U_complete_coding.csv','inputs/su_context_assessments.csv','inputs/su_positive_theme_assignments.csv','inputs/su_codebook.csv']
summary={'assessed_su_papers':len({r['paper_id'] for r in ass}),'su_contexts':len(ass),'continuity_counts':dict(RC),
 'sdt_domain_records':len(domain_ids),'sdt_positive_stage_function_edges':len(nonzero),'dtu_method_records':len(method_ids),
 'dtu_exact_configurations':len(patterns),'largest_exact_configuration_n':max(map(len,groups.values())),
 'su_positive_source_method_edges':sum(r['shared_assessments']>0 for r in pair_rows),'figures':NAMES,
 'plotted_architecture_proposals':False,'new_semantic_coding':False,'basis':'Aggregation of existing semantic extraction codes',
 'source_sha256':{p:hashlib.sha256((SOURCE/p).read_bytes()).hexdigest() for p in sources}}
assert sum(r['assessments'] for r in boundary_edges)==len(ass)
assert sum(r['paper_count'] for r in configs)==len(method_ids)
assert len(PdfReader(ROOT/'Data_Derived_Diagrams.pdf').pages)==len(NAMES)
(ROOT/'analysis_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
cards=''.join(f'<section><h2>{html.escape(n.replace("_"," "))}</h2><object data="figures/{n}.svg" type="image/svg+xml" style="width:100%"></object><p><a href="figures/{n}.pdf">PDF</a> · <a href="figures/{n}.svg">SVG</a> · <a href="figures/{n}.png">PNG</a></p></section>' for n in NAMES)
(ROOT/'gallery.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>Data-derived relational diagrams</title><style>body{font:17px system-ui;max-width:1500px;margin:30px auto;background:#f3f6f8;color:#17364a}header,section{background:white;padding:30px;margin:25px;border-radius:10px}a{color:#337fa8}h2{font-size:20px}</style><header><h1>Data-derived relational diagrams</h1><p>Every ribbon, connection and configuration is aggregated from recorded article-level codes. No proposed architecture links are plotted. Hover over the SVG edges in D01 and D02 to inspect the supporting record IDs.</p><a href="Data_Derived_Diagrams.pdf">Four-page PDF</a> · <a href="README.md">Methods and limits</a></header>'+cards,encoding='utf-8')
print(json.dumps(summary,indent=2))

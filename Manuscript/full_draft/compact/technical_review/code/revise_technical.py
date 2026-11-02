from pathlib import Path
import shutil,re,html,textwrap,json
B=Path('outputs/Manuscript/full_draft/compact/structural_review'); O=B.parent/'technical_review'
shutil.copytree(B,O,dirs_exist_ok=True,ignore=shutil.ignore_patterns('qa','*.pdf'))
for f in (O/'figures').glob('*.svg'):
 s=f.read_text(encoding='utf8')
 # Override both family attributes and matplotlib font shorthand without altering geometry.
 s=re.sub(r'(</(?:\w+:)?svg>)', '<style>text,tspan{font-family:"Times New Roman",serif !important}</style>\\1',s)
 f.write_text(s,encoding='utf8')
s=(O/'manuscript_en.html').read_text(encoding='utf8')
s=s.replace('</style>', '.figure.small img{width:82%;margin-left:auto;margin-right:auto}.figure.large img{width:108%;max-width:none;margin-left:-4%;max-height:210mm}.equation{display:block;text-align:center!important;text-align-last:center;margin:12pt 0;break-inside:avoid;font-style:italic}</style>',1)
def sizefig(m):
 t=m[0]; n=re.search(r'Figure (\d+)\.',t)
 if n and int(n[1])==3:t=t.replace('class="figure"','class="figure small"',1)
 if n and 4<=int(n[1])<=8:t=t.replace('class="figure"','class="figure large"',1)
 return t
s=re.sub(r'<div class="figure">.*?</div>',sizefig,s,flags=re.S)
s=s.replace('Reference keys are resolved in the supplementary architectural source register.', 'R1–R16 are source keys, not review counts: for example, R1 = Xiong et al. (2025), R2 = Human et al. (2023), and R12 = Bitencourt et al. (2025). The supplementary register resolves every key and its reading status.')
s=s.replace('The design-to-use structure is a substantive synthesis output of this review (Figure 9), rather than background decoration.', 'Figure 9 synthesizes the design, credibility-assessment and decision logic used to interpret the review findings.')
s=s.replace('The supporting studies inform particular concepts; their combination and allocation to the GeoAI–circular-material workflow are our synthesis.', 'Figures 9–11 combine reviewed DT mechanisms with an auxiliary architectural source set (R1–R16). That register includes partial-text sources and is not a separately completed systematic corpus. Sources support specific concepts; the A/B/C arrangement and its application to GeoAI–circular-material interfaces are our synthesis.')
s=s.replace('The proposed responsibility map in Figure 12 therefore associates each family with an explicit operation and a checkable output.', 'Figure 12 expands the third card of Figure 10, the system architecture brief, into proposed services with explicit inputs, operations and checkable outputs. The six configuration families determine how these services are implemented.')
s=s.replace('Figure 12. Proposed allocation of uncertainty responsibilities to the six configuration families. The operations are design requirements derived by connecting the architectural vocabulary to material-flow interfaces; they are not observed deployment frequencies. A defines acceptance requirements and C assigns each operation to a model, service or accountable role.', 'Figure 12. Technical expansion of the system architecture brief (Figure 10, third card). Numerical inference and propagation are separated from interface checks, diagnostic evaluation and orchestration. The uncertainty-bearing record crosses all four material interfaces. Service allocation and record schema are our proposed synthesis; concept-level sources do not validate the integrated implementation.')
old='An agent can orchestrate these tasks, but the estimator and validation procedure supply the uncertainty evidence. Human review and automated actions may coexist. Agentic AI remains an unresolved configuration descriptor in this source set, rather than a required uncertainty-detection component (Kritzinger et al., 2018; Shao and Helu, 2020; Agrawal et al., 2023).'
new='Agent-based simulation represents interacting entities inside a model; multi-agent orchestration distributes tasks among software actors. Neither alone quantifies uncertainty. Agentic AI denotes goal-directed tool orchestration here and remains unsupported as a specific category in this source set. Its proposed role is to request evidence or invoke checked services, with logged inputs and human escalation; numerical inference and validation remain separate responsibilities (Kritzinger et al., 2018; Shao and Helu, 2020; Agrawal et al., 2023).'
s=s.replace(old,new)
# Standalone mathematical displays; each retains an editable LaTeX expression.
equations=[
('E(p,i,j) = {entity, input, transformation, output, uncertainty-in, uncertainty-out, dependencies, DT-function, context, evidence}',r'E_{p,i,j}=\{\mathrm{entity,input,transformation,output},U_{in},U_{out},\mathrm{dependencies,DT\ function,context,evidence}\}'),
('n(q,m)=|A(q) intersection A(m)|',r'n(q,m)=|A(q)\cap A(m)|'),
('N(q)=|A(q)|',r'N(q)=|A(q)|'),
('P(m|q)=100 n(q,m)/N(q)',r'P(m\mid q)=100\,n(q,m)/N(q)'),
('Var(ΣMᵢ)=ΣVar(Mᵢ)+2Σᵢ&lt;ⱼCov(Mᵢ,Mⱼ)',r'\operatorname{Var}(\sum_i M_i)=\sum_i\operatorname{Var}(M_i)+2\sum_{i<j}\operatorname{Cov}(M_i,M_j)'),
('M = Σ_b A_b I_b',r'M=\sum_b A_b I_b'),
('O(t) = Σ_c M_c f_c(t | age, scenario)',r'O(t)=\sum_c M_c f_c(t\mid\mathrm{age,scenario})'),
('R = O × η × q',r'R=O\,\eta\,q'),
('r = y_observed − y_predicted',r'r=y_{\mathrm{observed}}-y_{\mathrm{predicted}}')]
for plain,latex in equations:
 s=s.replace(plain,'</p><p class="equation" data-latex="'+html.escape(latex,quote=True)+'">'+plain+'</p><p>')
# Keep growth within the agreed main-text ceiling by removing redundant narrative.
s=s.replace('These are proposed applications of the use-specific design brief, not universal accuracy thresholds ', 'These use-specific requirements follow ')
s=s.replace('This identity explains a design requirement, not a new empirical variance estimate.','')
(O/'manuscript_en.html').write_text(s,encoding='utf8')
W,H=1500,1470
v=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="100%" height="100%" fill="white"/><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#4C78A8"/></marker></defs>']
def t(x,y,z,size=24,bold=False):v.append(f'<text x="{x}" y="{y}" font-family="Times New Roman" font-size="{size}" fill="#2F2F2F" font-weight="{700 if bold else 400}">{html.escape(z)}</text>')
def lines(x,y,z,width=55,size=23):
 for i,line in enumerate(textwrap.wrap(z,width)):t(x,y+29*i,line,size)
def box(x,y,w,h,title,body,color='#4C78A8'):
 v.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="#FFFFFF" stroke="{color}" stroke-width="2.5"/>');t(x+16,y+33,title,25,True);lines(x+16,y+66,body,int(w/12),22)
def arrow(x,y,x2,y2):v.append(f'<path d="M{x},{y} L{x2},{y2}" stroke="#4C78A8" stroke-width="3" fill="none" marker-end="url(#a)"/>')
t(30,42,'Expanding A3: the system architecture brief',34,True)
lines(30,82,'A defines intended use and acceptance criteria; B configures the implementation; C assigns each service and decision to an accountable role.',110)
box(30,158,1440,130,'Shared uncertainty-bearing record at every interface', 'Entity + variable + unit + spatial support + timestamp + model/version + evidence locator; distribution / interval / scenario + dependency links + validity status + upstream record IDs. Proposed schema.', '#72B7B2')
t(30,329,'MATERIAL TRANSFORMATIONS — retain the record, update the represented quantity',25,True)
stages=[('S1','GeoAI attributes'),('S2','Material stock'),('S3','Dated outflows'),('S4','Usable recovery'),('S5','Impact / decision')]
for i,(a,b) in enumerate(stages):
 x=30+i*294;box(x,353,264,99,a,b)
 if i<4:arrow(x+265,403,x+290,403)
box(30,492,700,162,'1  Data and identity service','Checks units, entity matches, missing values, age and lineage. Output: qualified inputs and flags; invalid records are held for review. Semantic linkage: Kosse et al. (2025).')
box(770,492,700,162,'2  Inference and calibration service','Observations + prior/model → state or parameter estimates with uncertainty. Preserve fitting/evaluation separation. Probabilistic formulation: Kapteyn et al. (2021).')
arrow(731,571,765,571)
box(30,698,700,185,'3  Interface propagation service','For each Sᵢ → Sᵢ₊₁: apply its transformation to joint samples, intervals or explicit scenarios. Output: downstream uncertainty plus dependency/lineage links. Check units, support, assumptions and lost fields. Proposed integration.','#72B7B2')
box(770,698,700,185,'4  Diagnostic and validation service','Compare observations and predictions; evaluate residuals and, where applicable, interval coverage. Flag mismatch; investigate data, parameters or model form before revision. A flag does not identify its cause. Kapteyn et al. (2021).','#72B7B2')
arrow(1120,655,1120,690);arrow(765,788,735,788)
box(30,927,700,163,'5  Dependency and revision ledger','Version every estimate and link its upstream evidence. A revised input invalidates affected descendants; recalculate only after checks. Output: auditable S1–S5 change history. Proposed tracking service.','#9D755D')
box(770,927,700,163,'6  Decision and evidence interface','Expose impact ranges/scenarios, validity flags and sensitivity to recovery assumptions. Compare evidence with A; refer unresolved decisions to the assigned role. Role allocation: Agrawal et al. (2023).','#9D755D')
arrow(380,884,380,920);arrow(731,1005,765,1005)
box(30,1136,1440,146,'Orchestration, timing and authority — not a substitute for uncertainty computation','Human or software actors schedule checks, request missing evidence, invoke services and record approvals. Multi-agent coordination distributes these tasks; agent-based simulation is a model choice. Agentic AI is an unverified optional proposal here. Updates may be periodic or event-triggered, according to intended use.','#7F7F7F')
t(30,1325,'Responsibility test: every interface must name its input, transformation, uncertainty output and checking service.',23,True)
lines(30,1370,'Solid links show proposed information dependencies, not an empirically validated deployed architecture. Concept sources support individual functions; the complete S1–S5 integration is the review’s synthesis.',114,22)
v.append('</svg>');(O/'figures/configuration_uncertainty_responsibilities.svg').write_text('\n'.join(v),encoding='utf8')
for old,new in [('render_structural_review.cjs','render_technical_review.cjs'),('verify_structural_review.py','verify_technical_review.py')]:
 z=Path('work',old).read_text(encoding='utf8').replace('structural_review','technical_review')
 if old.startswith('verify'):
  z=z.replace("p=ns['Parser']();", "original_tex=ns['tex']\ndef adapted_tex(n):\n if isinstance(n,dict) and n['attrs'].get('class')=='equation':return '\\\\[\\n'+n['attrs']['data-latex']+'\\n\\\\]\\n'\n if isinstance(n,dict) and n['attrs'].get('class','').startswith('figure '):n['attrs']['class']='figure'\n return original_tex(n)\nns['tex']=adapted_tex\np=ns['Parser']();")
 Path('work',new).write_text(z,encoding='utf8')
(O/'README.md').write_text('Technical and typographic revision. Figure 12 expands A3; sources and synthesis are distinguished. Figure fonts: Times New Roman. Equations displayed separately. No new full-text eligibility decisions or semantic recoding claimed. Archived 17-paper percentages remain multi-label coding frequencies. LaTeX is editable but not compilation-verified.\n',encoding='utf8')
print(O)

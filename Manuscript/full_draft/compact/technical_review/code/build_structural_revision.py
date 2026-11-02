from pathlib import Path
import shutil,re,json,csv,textwrap,html
B=Path('outputs/Manuscript/full_draft/compact/english_review');O=B.parent/'structural_review';O.mkdir(exist_ok=True)
for p in B.iterdir():
 if p.is_file() and p.suffix in ['.html','.tex','.json']:shutil.copyfile(p,O/p.name)
shutil.copytree(B/'figures',O/'figures',dirs_exist_ok=True)
s=Path('outputs/Manuscript/full_draft/inputs/figure_S1_design_brief.svg').read_text(encoding='utf8')
mapping={'#23354d':'#2f2f2f','#26374d':'#2f2f2f','#315c7d':'#4c78a8','#355f80':'#4c78a8','#35627f':'#4c78a8','#316d73':'#72b7b2','#6b7280':'#7f7f7f','#f0f5f8':'#ececec','#eff4f8':'#ececec'}
s=re.sub(r'#[0-9a-fA-F]{6}',lambda m:mapping.get(m[0].lower(),m[0]),s);(O/'figures/figure_S1_design_brief.svg').write_text(s,encoding='utf8')
rows=[
('System composition','Retain dependencies when entities are combined','Building / component → stock: shared archetypes and coefficients must remain linked','Joint samples or covariance; aggregation lineage','R2; R16; general variance identity'),
('Internal architecture','Make uncertainty-bearing information traceable','Connect GeoAI attributes, inventory, release, recovery and LCA by stable identities and interface contracts','Entity ID, units, provenance, model version and dependency links','R15; R2'),
('Computational model','Estimate and propagate uncertainty','Infer attributes; compute material mass; forecast release; model recovery; propagate to impacts','Distribution, interval or scenario outputs; stated assumptions','R3; R4; material-interface synthesis'),
('Coupling & control','Test mismatch and route feedback','Compare model output with new survey / inspection evidence; trigger justified downstream revisions','Residual / discrepancy; revision trigger; action permissions','R14; R3; R6'),
('Agency & intelligence','Assign coordination and accountability','Request data, invoke estimators, inspect failed checks and approve recovery decisions','Task owner, escalation rule, decision and audit trail','R6; R8; agentic AI remains unresolved'),
('Temporal organization','Maintain validity over time','Distinguish observation date, model update and forecast horizon; reassess after relevant events','Timestamp, validity interval and affected-output list','R5; specific timing labels remain unresolved')]
with (O/'configuration_responsibilities.csv').open('w',encoding='utf8',newline='') as f:
 w=csv.writer(f);w.writerow(['configuration_family','responsibility','material_workflow_application','required_output','concept_support','allocation_status']);w.writerows([r+('Proposed cross-study allocation; source concepts do not validate the full mapping',) for r in rows])
W=1400;H=1260;svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="100%" height="100%" fill="white"/>']
def text(x,y,t,size=20,color='#2F2F2F',bold=False):svg.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}">{html.escape(t)}</text>')
def lines(x,y,t,width,size=19):
 for j,line in enumerate(textwrap.wrap(t,width)):text(x,y+j*26,line,size)
text(35,42,'Responsibilities within the original DT configuration structure',28,bold=True)
text(35,82,'A: specify the decision, quantity, scale, horizon and required evidence.',21,'#4C78A8',True)
text(35,114,'B: choose how the responsibilities below are implemented. The six families coexist.',20)
xs=[35,280,610,1035];widths=[220,305,400,330]
for x,t in zip(xs,['Configuration family','Uncertainty responsibility','GeoAI → circular material workflow','Required traceable output']):text(x,161,t,19,bold=True)
for i,r in enumerate(rows):
 y=181+i*144
 svg.append(f'<rect x="25" y="{y}" width="1350" height="135" rx="5" fill="{["#ECECEC","#FFFFFF"][i%2]}" stroke="#D9D9D9"/>')
 lines(xs[0],y+31,r[0],19,21);lines(xs[1],y+31,r[1],29);lines(xs[2],y+31,r[2],38);lines(xs[3],y+31,r[3],28)
text(35,1091,'C: assign each check to an executable model/service and an accountable human or automated role.',21,'#4C78A8',True)
text(35,1133,'Assess: observe → diagnose → calibrate where justified → validate → propagate → communicate.',21)
text(35,1175,'A residual flags disagreement; diagnosis establishes plausible causes. Agency coordinates; models compute.',18)
text(35,1215,'The allocation is our synthesis. Concept references and evidence limits are retained in configuration_responsibilities.csv.',17,'#7F7F7F')
svg.append('</svg>');(O/'figures/configuration_uncertainty_responsibilities.svg').write_text('\n'.join(svg),encoding='utf8')
h=(B/'manuscript_en.html').read_text(encoding='utf8');section=Path('work/dt_structure_section.html').read_text(encoding='utf8')
h=re.sub(r'<h2>4\.5\..*?(?=<h1>5\.)',lambda m:section,h,flags=re.S)
h=h.replace('line-height:1.38','line-height:1.32')
h=h.replace('An agent can orchestrate these tasks, but the estimator and validation procedure supply the uncertainty evidence.','Agent-based models simulate interacting actors; software agents coordinate services. Neither label guarantees uncertainty assessment. An agent can orchestrate checks, but the estimator and validation procedure supply the uncertainty evidence.')
marker='<h2>3.7.'
idx=h.index(marker)
h=h[:idx]+'''<p>The architectural synthesis additionally maps each configuration family to its proposed uncertainty responsibility, material-interface application and required output. The extraction separates a source-supported concept from our allocation of that concept to S1–S5. Unresolved descriptors retain that status. A mapped capability is therefore a design requirement unless a source demonstrates the corresponding operation; candidate connections in the configuration diagram are not counted as empirical observations.</p>'''+h[idx:]
# Keep section 5.4 directed to the actual configuration families rather than a replacement five-stage architecture.
start=h.index('<h2>5.4.');end=h.index('<h2>5.5.',start)
h=h[:start]+'''<h2>5.4. Why computation, integration and agency have different roles</h2>
<p>The architecture in Figures 9–12 makes a specific distinction: uncertainty estimation is a model operation, whereas continuity is also an integration and governance requirement. A sophisticated predictor may quantify its own error while exporting only a point estimate. A semantic platform may preserve provenance while carrying no uncertainty distribution. An automated agent may rerun both without checking whether their units, dependencies and evidence remain compatible. Consequently, no configuration family alone establishes an uncertainty-aware circular workflow.</p>
<p>For GeoAI-to-inventory transfer, computational choices determine the representation of attribute error; internal architecture preserves its association with the building and material estimate. For inventory-to-release transfer, model composition and timing determine whether shared coefficients, lifetime assumptions and renovation events remain connected. For release-to-recovery transfer, inspection and quality evidence must update the recoverable quantity rather than merely annotate a visualization. For recovery-to-impact transfer, the contract must expose substitution, processing and system-boundary assumptions. These allocations are hypotheses for implementation and evaluation derived from the review, not empirical demonstrations of an end-to-end twin.</p>
<p>Agency becomes useful when it makes this process operational: scheduling a check, requesting missing evidence, invoking the appropriate estimator and escalating a decision outside the assessed scope. It cannot replace uncertainty modelling or independent validation. Spatial scalability likewise requires explicit aggregation, dependency treatment and resolution checks; a federated or multiscale label does not demonstrate validity at every scale. The design brief therefore sets the evidence requirements, while functional allocation identifies who or what must satisfy them.</p>
''' +h[end:]
(O/'manuscript_en.html').write_text(h,encoding='utf8')
shutil.copyfile('outputs/Manuscript/full_draft/inputs/academic-foundations.md',O/'academic-foundations.md')
print('Revised section 4.5 and 5.4; original A-B-C, design brief and configuration diagrams now in main text')

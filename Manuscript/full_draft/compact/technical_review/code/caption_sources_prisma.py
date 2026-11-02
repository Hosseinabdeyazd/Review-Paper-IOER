from pathlib import Path
import re,html,json,textwrap,shutil
O=Path('outputs/Manuscript/full_draft/compact/technical_review')
foundation=(O/'academic-foundations.md').read_text(encoding='utf8')
refs={}
for m in re.finditer(r'### R(\d+) [^\n]+\n\n([^\n]+)',foundation):refs[int(m[1])]=m[2]
refs[16]='Gervasi, M., Bove, L., Corallo, A., Miglietta, M., Negro, L., Pellegrino, G., Ria, F., and Visaggio, C. A. (2026). Systems of Digital Twins: A Systematic Literature Review and a formal framework. Digital Engineering, 9, 100100. DOI: https://doi.org/10.1016/j.dte.2026.100100.'
for f in (O/'figures').glob('*.svg'):
 s=f.read_text(encoding='utf8');s=re.sub(r'\[R\d+(?:\s*[-–,;]\s*R?\d+)*\]','',s)
 s=s.replace('Reference keys and evidence limits: papers/academic-foundations.md.','Concept sources and evidence limits are given in the caption and source register.')
 s=s.replace('Reference keys','Concept sources')
 f.write_text(s,encoding='utf8')
caps={
'figure_1_design_to_use.svg':'Concept sources: Xiong et al. (2025), Human et al. (2023), Kapteyn et al. (2021), Shao and Helu (2020), Agrawal et al. (2023), Walton et al. (2024), Ogunsakin et al. (2023), Kerin et al. (2023), Chen et al. (2026), Lugaresi et al. (2026), Bitencourt et al. (2025), and van Beek et al. (2023). The arrangement and links are our synthesis.',
'figure_S1_design_brief.svg':'Concept sources: Xiong et al. (2025), Human et al. (2023), Shao and Helu (2020), Agrawal et al. (2023), and van Beek et al. (2023); the five-card arrangement is our synthesis.',
'figure_S2_configuration_choices (1).svg':'Concept sources: Xiong et al. (2025), Human et al. (2023), Kapteyn et al. (2021), Ferrari and Willcox (2024), Shao and Helu (2020), Agrawal et al. (2023), Ogunsakin et al. (2023), Chen et al. (2026), Kritzinger et al. (2018), Kosse et al. (2025), and Gervasi et al. (2026). Sources support descriptors, not every connecting curve.',
'figure_S3_functional_allocation.svg':'Concept sources: Human et al. (2023), Kapteyn et al. (2021), Agrawal et al. (2023), Walton et al. (2024), Ogunsakin et al. (2023), Chen et al. (2026), Lugaresi et al. (2026), and Bitencourt et al. (2025). Functional allocation is our synthesis.'}
for name in ['manuscript_en.html','supplement_figures_en.html']:
 p=O/name;s=p.read_text(encoding='utf8')
 def change(m):
  t=m[0]
  for fig,cap in caps.items():
   if 'figures/'+fig+'"' in t:
    t=re.sub(r'R1–R16 are source keys.*?reading status\.','',t)
    t=t.replace('</p></div>',' '+cap+'</p></div>')
  return t
 s=re.sub(r'<div class="figure[^\"]*">.*?</div>',change,s,flags=re.S)
 if name=='manuscript_en.html':
  start=s.index('class="refs"');body=s[:start];end=s[start:]
  for num,line in refs.items():
   doi=re.search(r'10\.\d{4,9}/[^\s\]\)]+',line)
   if doi and doi[0].rstrip('.') in end:continue
   plain=re.sub(r'\[([^\]]+)\]\([^\)]+\)',r'\1',line).replace('**','').replace('*','')
   end=end.replace('</div>', '<p>'+html.escape(plain)+'</p></div>',1)
  s=body+end
 p.write_text(s,encoding='utf8')
def diagram(name,title,left,right,notes):
 v=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="1100" viewBox="0 0 1100 1100"><rect width="1100" height="1100" fill="white"/><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0L8,4L0,8"/></marker></defs>']
 def text(x,y,t,size=22):v.append(f'<text x="{x}" y="{y}" font-family="Times New Roman" font-size="{size}" fill="#2F2F2F">{html.escape(t)}</text>')
 v.append('<rect x="35" y="20" width="1030" height="60" fill="#9D755D"/>');text(55,58,title,25)
 for i,(l,r) in enumerate(zip(left,right)):
  y=110+i*165
  for x,content in [(80,l),(610,r)]:
   v.append(f'<rect x="{x}" y="{y}" width="430" height="132" fill="#ECECEC" stroke="#7F7F7F"/>')
   for j,line in enumerate(content.split('|')):text(x+15,y+30+j*27,line)
  if i<4:v.append(f'<path d="M295,{y+132} L295,{y+165}" stroke="#2F2F2F" marker-end="url(#a)"/>')
  v.append(f'<path d="M510,{y+66} L610,{y+66}" stroke="#2F2F2F" marker-end="url(#a)"/>')
 for i,line in enumerate(textwrap.wrap(notes,112)):text(35,985+i*27,line,20)
 v.append('</svg>');(O/'figures'/name).write_text('\n'.join(v),encoding='utf8')
diagram('prisma_base_dt_en.svg','B + DT: broad screening and separate focused eligibility',
 ['Query occurrences: 4,124','Unique records screened: 2,400','Broad full-text candidates: 1,676|Direct: 890; complementary: 762|Unclear: 24','Focused bridge: 14 reports sought|12 full texts assessed','Focused bridge included: 10|Direct: 4; complementary: 6'],
 ['Repeated occurrences: 1,724|4,124 minus 2,400|Includes late alias adjudication','Screening exclusions: 724','Broad retrieval / eligibility|Not closed; candidates are not|Included publications','Focused reports not retrieved: 2|Separate search: 83 occurrences|40 duplicates; 43 screened','Focused full-text exclusions: 2|Outside focused interface|29/43 outside focused candidate set'],
 'Broad and focused routes are not one continuous denominator. The 10 focused inclusions do not close the 1,676 broad candidates. Counts: unique screening ledger and bridge eligibility ledger.')
diagram('prisma_base_u_en.svg','B + U: shared retrieval context and selected-set eligibility',
 ['S4–S5 shared Base / Base+U|19,963 query occurrences|14,869 database-distinct records','Shared unique records: 9,587|Not a separate B+U denominator','S4–S5 U-focused candidates: 392|3 prioritized for full-text appraisal|389 not thereby excluded','Selected S1–S5 + U reports: 21|Full texts assessed: 20','Selected-set included reports: 20|Not the total broad B+U yield'],
 ['Within-source overlaps: 5,094|Cross-source duplicates: 5,282','Outside retained set: 5,977|Retained candidates: 3,610|2,932 clear; 327 unclear; 351 secondary','Other mechanism classifications|Possible cross-stage: 90|Not demonstrated: 299','Selected reports not retrieved: 1|Earlier S1–S3 + S4–S5 selection|Full search-to-selection join open','Selected full-text exclusions: 0|20 assessed = 20 included|Independent-study count not established'],
 'These are nested/selected audit routes, not a reconstructed exhaustive B+U flow. Shared retrieval cannot supply an independent B+U identification count. Selected eligibility is verified separately.')
p=O/'manuscript_en.html';s=p.read_text(encoding='utf8')
needle='<div class="figure small">'
pos=s.index(needle)
extra='<div class="figure"><img src="figures/prisma_base_dt_en.svg"><p class="caption">Figure 2b. B+DT selection audit: broad screening and focused bridge eligibility are displayed separately. B denotes the domain/stage search; DT denotes digital twin. The focused endpoint cannot substitute for unfinished broad eligibility.</p></div>\n<div class="figure"><img src="figures/prisma_base_u_en.svg"><p class="caption">Figure 2c. B+U selection audit. U denotes uncertainty. The shared Base/Base+U search, mechanism subset and selected full-text set have different denominators; connecting rows organize the audit rather than assert an exhaustive flow between these sets.</p></div>\n'
s=s[:pos]+extra+s[pos:];p.write_text(s,encoding='utf8')
shutil.copyfile(__file__,O/'code'/Path(__file__).name)
(O/'prisma_family_provenance.json').write_text(json.dumps({'B_DT':'methods_audit/eligibility/broad_dt_unique_screening_counts.json','B_DT_focused':'methods_audit/eligibility/bridge_counts.json','B_U_selected':'methods_audit/eligibility/verified_fulltext_counts.json','B_U_shared':'methods_audit/figures/counts_and_labels.json','new_eligibility_decisions':False},indent=2),encoding='utf8')

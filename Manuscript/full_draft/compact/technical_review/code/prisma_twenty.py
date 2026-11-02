from pathlib import Path
import html,textwrap,shutil,re
O=Path('outputs/Manuscript/full_draft/compact/technical_review')
def diagram(name,title,left,right,bands,note):
 v=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="1120" viewBox="0 0 1100 1120"><rect width="1100" height="1120" fill="white"/><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0L8,4L0,8" fill="#2F2F2F"/></marker></defs>']
 def text(x,y,t,size=23,anchor='middle'):
  v.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Times New Roman" font-size="{size}" fill="#2F2F2F">{html.escape(t)}</text>')
 v.append('<rect x="115" y="25" width="940" height="60" fill="#9D755D"/>');text(585,63,title,25)
 for i,l in enumerate(left):
  y=110+i*164
  for x,lines in [(115,l),(635,right[i])]:
   if not lines:continue
   v.append(f'<rect x="{x}" y="{y}" width="420" height="126" fill="white" stroke="#2F2F2F" stroke-width="1.4"/>')
   yy=y+63-(len(lines)-1)*14
   for j,line in enumerate(lines):text(x+210,yy+j*28,line,22)
  if i<len(left)-1:v.append(f'<path d="M325,{y+126}V{y+164}" fill="none" stroke="#2F2F2F" stroke-width="1.5" marker-end="url(#a)"/>')
  if right[i]:v.append(f'<path d="M535,{y+63}H635" stroke="#2F2F2F" stroke-width="1.5" marker-end="url(#a)"/>')
 for label,start,end in bands:
  y=110+start*164;h=(end-start)*164+126;cy=y+h/2
  v.append(f'<rect x="30" y="{y}" width="65" height="{h}" fill="#B8B8B8" stroke="#7F7F7F"/><text x="62" y="{cy}" transform="rotate(-90 62 {cy})" text-anchor="middle" font-family="Times New Roman" font-size="23">{label}</text>')
 for i,line in enumerate(textwrap.wrap(note,114)):text(30,970+i*26,line,20,'start')
 v.append('</svg>');(O/'figures'/name).write_text('\n'.join(v),encoding='utf8')
diagram('prisma_base_dt_en.svg','Base + DT: focused bridge selection',[
 ['Records identified from databases','Query occurrences (n = 83)'],['Records screened (n = 43)'],['Reports sought for retrieval (n = 14)'],['Reports assessed for eligibility','(n = 12)'],['Reports included (n = 10)','Direct evidence: 4','Complementary evidence: 6']],
 [['Duplicate records removed','(n = 40)'],['Records not selected (n = 29)','Background: 18; excluded: 11'],['Reports not retrieved (n = 2)'],['Reports excluded (n = 2)','Outside focused interface'],[]],
 [('Identification',0,0),('Screening',1,1),('Retrieval / eligibility',2,3),('Included',4,4)],
 'Independent focused search. Broad B+DT retrieval: 4,124 occurrences; 1,724 repeats; 2,400 unique records; 724 screening exclusions; 1,676 candidates. Broad eligibility is not closed and is not the denominator of this focused flow. Counts refer to publications/reports; underlying-study independence is not established.')
diagram('prisma_base_u_en.svg','Base + U: selected S1–S5 report eligibility',[
 ['Previously selected reports','S1–S3 and S4–S5 sets (n = 21)'],['Selected reports forwarded','for retrieval (n = 21)'],['Reports sought for retrieval (n = 21)'],['Reports assessed for eligibility','(n = 20)'],['Reports included (n = 20)','Same 20-paper denominator in','source, method and outcome profiles']],
 [[],[],['Reports not retrieved (n = 1)'],['Full-text reports excluded (n = 0)','All 20 assessed reports retained'],[]],
 [('Selected reports',0,1),('Retrieval / eligibility',2,3),('Included',4,4)],
 'Selected-set eligibility flow, not a reconstructed database-wide PRISMA. Shared S4–S5 Base/Base+U retrieval: 19,963 occurrences; 9,587 unique records; 3,610 retained candidates, including 392 U-focused candidates. Those shared counts are not an independent B+U identification denominator and are not connected to the 21-report flow.')
p=O/'manuscript_en.html';s=p.read_text(encoding='utf8')
for fig,caption in [('prisma_base_dt_en.svg','Figure 2b. PRISMA-style selection for the independent focused Base+DT bridge search. The separate broad retrieval is reported below the diagram, without implying that focused inclusion closes broad eligibility.'),('prisma_base_u_en.svg','Figure 2c. PRISMA-style retrieval and eligibility for the selected S1–S5+U reports. Twenty assessed reports were included; one was not retrieved. This selected-set flow does not reconstruct earlier database-wide screening.')]:
 pattern=r'(<div class="figure[^\"]*"><img src="figures/'+re.escape(fig)+r'"><p class="caption">).*?(</p></div>)'
 s=re.sub(pattern,lambda m:m[1]+caption+m[2],s,flags=re.S)
p.write_text(s,encoding='utf8');shutil.copyfile(__file__,O/'code/prisma_twenty.py')

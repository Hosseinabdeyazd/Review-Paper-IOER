from pathlib import Path
import csv,json,hashlib,re,html,collections,shutil
P=Path('outputs/Manuscript/full_draft/compact/technical_review');D=P/'base_u_comparison'
def read(p): return list(csv.DictReader(p.open(encoding='utf-8-sig')))
def save(name,rows):
 with (D/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
stages=read(D/'stage_base_u_counts.csv');ctx=[r for r in read(D/'fulltext_context_evidence.csv') if r['included_in_counts']=='1']
assert len(ctx)==23 and len({r['paper_id'] for r in ctx})==20
mapping={'B12':['S1','S2'],'B23':['S2','S3'],'B34':['S3','S4'],'B45':['S4','S5'],'O5':['S5']}
members=[];rows=[]
for st in stages:
 stage=st['stage']; rr=[r for r in ctx if stage in mapping[r['context']]];ids={r['paper_id'] for r in rr}
 a={r['paper_id'] for r in rr if r['continuity_code']=='P'};b={r['paper_id'] for r in rr if r['continuity_code']=='E'}
 rows.append(dict(stage=stage,assessed_papers=len(ids),partial_n=len(a),partial_pct=100*len(a)/len(ids),quantified_selected_inputs_n=len(b),quantified_pct=100*len(b)/len(ids),paper_ids=';'.join(sorted(ids)),partial_ids=';'.join(sorted(a)),quantified_ids=';'.join(sorted(b))))
 for r in rr: members.append(dict(stage=stage,paper_id=r['paper_id'],doi=r['doi'],context=r['context'],continuity_code=r['continuity_code'],reason=r['decision_reason']))
save('figure2d_stage_fulltext_counts.csv',rows);save('figure2d_stage_context_memberships.csv',members)
pilot=read(D/'s123_multistage_screening_source.csv');assert len(pilot)==73
save('s123_multistage_screening_summary.csv',[dict(stage=s,screened=sum(s in r['Broad stage membership'] for r in pilot),**{k.replace(' ','_'):sum(s in r['Broad stage membership'] and r['Screening status']==k for r in pilot) for k in ['Include','Unclear','Secondary evidence','Exclude']}) for s in ['S1','S2','S3']])
# Source pilot CSV is archived beside the derived tables.
old=P/'figures/base_u_treatment_en.svg';backup=P/'figures/s45_title_abstract_treatment_en.svg'
if not backup.exists():shutil.copyfile(old,backup)
v=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="1000" viewBox="0 0 1100 1000"><rect width="1100" height="1000" fill="white"/>']
def rect(x,y,w,h,c='#ECECEC'):v.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>')
def text(x,y,s,size=23,anchor='start'):v.append(f'<text x="{x}" y="{y}" font-family="Times New Roman" font-size="{size}" fill="black" text-anchor="{anchor}">{html.escape(str(s))}</text>')
rect(15,10,1070,45,'#9D755D');text(35,41,'S1–S5: search membership and assessed uncertainty evidence',27)
text(30,90,'A   Search records and full-text evidence by stage',25)
text(30,121,'U share uses Base records; P and E shares use distinct assessed papers at that stage.',21)
xs=[38,145,280,510,710,920]
for x,s in zip(xs,['Stage','Base n','Base ∩ U','Assessed papers','Partial transfer (P)','Quantified inputs (E)']):text(x,160,s,21)
for i,(st,r) in enumerate(zip(stages,rows)):
 y=182+58*i;rect(25,y,1050,53,'#ECECEC' if i%2==0 else '#F7F7F7')
 values=[st['stage'],f"{int(st['base_n']):,}",f"{st['intersection_n']} / {st['base_n']} ({float(st['u_share_of_base_pct']):.1f}%)"+('*' if st['stage']=='S1' else ''),r['assessed_papers'],f"{r['partial_n']}/{r['assessed_papers']} ({r['partial_pct']:.1f}%)",f"{r['quantified_selected_inputs_n']}/{r['assessed_papers']} ({r['quantified_pct']:.1f}%)"]
 for x,s in zip(xs,values):text(x,y+34,s,22)
text(30,505,'* S1 U includes reconstructed Scopus membership. S3 additionally has one U-only record.',20)
text(30,533,'Stage evidence counts papers at either endpoint; memberships overlap across stages and P/E.',20)
rect(15,560,1070,40,'#9D755D');text(35,589,'B   Interface-specific evidence: 23 contexts from 20 included publications',25)
for x,s in zip([35,285,435,675,910],['Interface','Assessed n','Partial transfer (P)','Quantified inputs (E)','Other evidence']):text(x,637,s,21)
bound=[]
for i,(c,label) in enumerate([('B12','S1 → S2'),('B23','S2 → S3'),('B34','S3 → S4'),('B45','S4 → S5'),('O5','Other inputs → S5')]):
 rr=[r for r in ctx if r['context']==c];n=len(rr);a=sum(r['continuity_code']=='P' for r in rr);b=sum(r['continuity_code']=='E' for r in rr);other=n-a-b
 bound.append(dict(context=c,n=n,partial=a,quantified=b,other=other))
 y=655+48*i;rect(25,y,1050,44,'#ECECEC' if i%2==0 else '#F7F7F7')
 val=lambda k:f'{k}/{n} ({100*k/n:.1f}%)' if n else '—'
 for x,s in zip([35,285,435,675,910],[label,n,val(a),val(b),val(other)]):text(x,y+29,s,22)
text(30,922,'P: partial transfer; E: quantified outputs for selected uncertain inputs, not a complete chain.',20)
text(30,950,'Other: discussion, no demonstrated transfer, propagation-ready inputs, or sensitivity comparison.',20)
text(30,978,'S3 → S4: no assessed context in this selected set; percentage undefined. Search share ≠ UQ prevalence.',20)
v.append('</svg>');svg='\n'.join(v);svg=re.sub(r'\b(y|height)="([\d.]+)"',lambda m:f'{m[1]}="{float(m[2])*.8:g}"',svg).replace('viewBox="0 0 1100 1000"','viewBox="0 0 1100 800"');old.write_text(svg,encoding='utf-8')
save('figure2d_boundary_counts.csv',bound)
f=P/'manuscript_en.html';s=f.read_text(encoding='utf-8')
s=re.sub(r'(<p class="caption">(?:<a[^>]*>)?Figure 2d(?:</a>)?\.).*?</p>',r'\1 Search membership and full-text evidence across S1–S5. P/E percentages use distinct assessed publications per stage (A) and publication–interface contexts (B). Stage membership follows the endpoints of coded interfaces; it is not exhaustive thematic coverage. U-layer retrieval does not establish substantive uncertainty analysis.</p>',s,flags=re.S)
oldtext='In the assessed U candidates, explicit propagation is reported in 17/143 S4 and 43/331 S5 title/abstract records; this need not cross a stage boundary. Three S4–S5 screening claims reduce at full-text appraisal to one partial S4→S5 case and two other-input→S5 cases. The companion audit provides memberships, percentages and reasons.'
newtext='Figure 2d links these retrieval counts to the selected full-text evidence. Stage denominators count distinct papers at either endpoint of a coded interface; interface denominators count paper–context assessments. S1–S3 pilot screening and S4–S5 mechanism screening use different categories and are retained separately in the supplementary evidence tables. Neither estimates five-stage prevalence.'
s=s.replace(oldtext,newtext);f.write_text(s,encoding='utf-8')
f=P/'supplement_figures_en.html';s=f.read_text(encoding='utf-8')
if 's45_title_abstract_treatment_en.svg' not in s:s=s.replace('</body>','<div class="figure"><img src="figures/s45_title_abstract_treatment_en.svg"><p class="caption">Supplementary Figure S10. Title/abstract mechanism screening of S4–S5 U-layer candidates; 392 distinct records, with overlapping stage membership. This separate screening cohort is not the denominator of Figure 2d full-text percentages.</p></div></body>')
f.write_text(s,encoding='utf-8')
audit=dict(assessed_publications=20,assessed_contexts=23,stage_counts=rows,pilot_records=73,new_semantic_coding=False,method='Distinct publication sets per endpoint stage; P/E codes retained from existing interface assessments; zero context denominator gives undefined percentage.',inputs={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in [D/'fulltext_context_evidence.csv',D/'stage_base_u_counts.csv',D/'s123_multistage_screening_source.csv']})
(D/'figure2d_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
print(json.dumps(rows,indent=2))

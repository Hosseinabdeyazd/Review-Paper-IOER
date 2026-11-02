from pathlib import Path
import csv, io, json, re, zipfile, hashlib, html, collections

ROOT=Path.cwd()
O=ROOT/'outputs/Manuscript/full_draft/compact/technical_review'
D=O/'base_u_comparison'; D.mkdir(exist_ok=True)
T=ROOT/'outputs/Manuscript/temporal_trends/inputs'
A=ROOT/'outputs/S4 S5 Core Review/screening/adjudication'
def read(p):
    return list(csv.DictReader(p.open(encoding='utf-8-sig')))
def save(name,rows):
    with (D/name).open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def doi(s): return re.sub(r'^https?://(?:dx\.)?doi.org/','',s.strip().lower())
def key(r): return 'doi:'+doi(r['DOI']) if r['DOI'].strip() else 'title:'+re.sub(r'[^\w]','',r['Title'].lower())+'|'+r['Year']
def queries(r): return set(re.findall(r'S[1-5]-[12]',r['queries']))
with zipfile.ZipFile(A/'unclear946_recheck/current_canonical_records.zip') as z:
    canonical=list(csv.DictReader(io.TextIOWrapper(z.open('current_canonical_records.csv'),encoding='utf-8-sig')))
mechanisms=read(A/'uncertainty392_mechanisms/all_392_mechanism_decisions.csv')
assert len(canonical)==9587 and len({r['record_id'] for r in canonical})==9587
assert len(mechanisms)==392 and len({r['record_id'] for r in mechanisms})==392
stages=[];members=[];sets={};inputs=[]
for i in range(1,6):
    if i<4:
        br=read(T/f'S{i}b.csv');ur=read(T/f'S{i}u.csv')
        b={key(r) for r in br};u={key(r) for r in ur}
        records={key(r):r for r in br+ur}
        assert len(b)==len(br) and len(u)==len(ur)
        source='archived merged pre-screening corpora'
        caveat=('Scopus U contribution reconstructed from Base; not an independently verified U search' if i==1 else 'Conservative DOI / exact-title-year identities; unresolved title aliases not merged')
        for suffix in ['b','u']:
            p=T/f'S{i}{suffix}.csv';inputs.append(dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    else:
        records={r['record_id']:r for r in canonical}
        b={k for k,r in records.items() if f'S{i}-1' in queries(r)}
        u={k for k,r in records.items() if f'S{i}-2' in queries(r)}
        source='adjudicated canonical search memberships'
        caveat='Query labels parsed across semicolon and pipe separators; not semantic stage assignment'
    sets[i]=(b,u)
    for k in sorted(b|u):
        r=records[k]
        members.append(dict(stage=f'S{i}',record_key=k,doi=doi(r.get('DOI',r.get('doi',''))),title=r.get('Title',r.get('title','')),in_base=int(k in b),in_u=int(k in u),partition='intersection' if k in b&u else 'base_only' if k in b else 'u_only',source=source))
    stages.append(dict(stage=f'S{i}',base_n=len(b),u_layer_n=len(u),intersection_n=len(b&u),base_only_n=len(b-u),u_only_n=len(u-b),u_share_of_base_pct=100*len(b&u)/len(b),base_only_pct=100*len(b-u)/len(b),source=source,qualification=caveat))
    assert len(b)==len(b&u)+len(b-u) and len(u)==len(b&u)+len(u-b)
save('stage_base_u_counts.csv',stages);save('record_membership.csv',members)
save('u_only_records.csv',[r for r in members if r['partition']=='u_only'])

# These are existing title/abstract decisions, not newly inferred full-text outcomes.
mech_summary=[];mech_members=[];screen_counts=[]
for i in [4,5]:
    b,u=sets[i]
    mr=[r for r in mechanisms if r['record_id'] in b&u]
    retained={r['record_id'] for r in canonical if r['record_id'] in b&u and r['adjudication_status']=='retain_for_fulltext'}
    assert retained=={r['record_id'] for r in mr}
    for status,n in sorted(collections.Counter(r['adjudication_status'] for r in canonical if r['record_id'] in b&u).items()):
        screen_counts.append(dict(stage=f'S{i}',status=status,records=n,denominator=len(b&u),percent=100*n/len(b&u)))
    for r in mr:
        mech_members.append({k:r.get(k,'') for k in ['record_id','doi','title','queries','mechanism_category','mechanism_cross_stage_s4_s5','mechanism_reason','mechanism_evidence','mechanism_evidence_level']}|{'search_stage':f'S{i}'})
    for axis,column in [('uncertainty_treatment','mechanism_category'),('cross_stage_claim','mechanism_cross_stage_s4_s5')]:
        for value,n in sorted(collections.Counter(r[column] for r in mr).items()):
            mech_summary.append(dict(stage=f'S{i}',axis=axis,category=value,count=n,assessed_title_abstract_n=len(mr),percent=100*n/len(mr),evidence_level='title_abstract',full_u_layer_n=len(u)))
save('title_abstract_treatment_counts.csv',mech_summary);save('title_abstract_decision_memberships.csv',mech_members);save('u_screening_partitions.csv',screen_counts)

contexts=[r for r in read(ROOT/'outputs/Manuscript/relational_analysis/results/inputs/su_context_assessments.csv') if r['included_in_counts']=='1']
assert len(contexts)==23 and len({r['paper_id'] for r in contexts})==20
boundary=[]
for ctx,label in [('B12','S1→S2'),('B23','S2→S3'),('B34','S3→S4'),('B45','S4→S5'),('O5','Other inputs→S5')]:
    rr=[r for r in contexts if r['context']==ctx];n=len(rr)
    for code in ['Q','N','R','S','P','E']:
        ss=[r for r in rr if r['continuity_code']==code]
        boundary.append(dict(boundary=label,context=ctx,continuity_code=code,assessments=len(ss),denominator=n,percent=100*len(ss)/n if n else '',paper_ids=';'.join(r['paper_id'] for r in ss)))
save('fulltext_boundary_counts.csv',boundary);save('fulltext_context_evidence.csv',contexts)
for p in [A/'unclear946_recheck/current_canonical_records.zip',A/'uncertainty392_mechanisms/all_392_mechanism_decisions.csv',ROOT/'outputs/Manuscript/relational_analysis/results/inputs/su_context_assessments.csv']:
    inputs.append(dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(D/'audit.json').write_text(json.dumps(dict(inputs=inputs,stage_counts=stages,canonical_s45=9587,u_union_s45=len(sets[4][1]|sets[5][1]),mechanism_union=392,fulltext_publications=20,fulltext_contexts=23,new_screening_decisions=False,checks='All partitions and assessed memberships reconciled; S1 reconstructed and S3 U-only record explicitly retained'),indent=2),encoding='utf8')

# Vector figure; the upper panel is a set comparison, not a PRISMA exclusion step.
v=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="1250" viewBox="0 0 1100 1250"><rect width="1100" height="1250" fill="white"/><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0L8,4L0,8" fill="black"/></marker></defs>']
def text(x,y,s,size=22,anchor='start'):
    v.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Times New Roman" font-size="{size}" fill="black">{html.escape(str(s))}</text>')
def rect(x,y,w,h,fill='white'):
    v.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#7F7F7F"/>')
def box(x,y,w,h,lines):
    rect(x,y,w,h)
    for j,s in enumerate(lines):text(x+w/2,y+h/2-(len(lines)-1)*13+j*26,s,22,'middle')
def arrow(x,y,xx,yy):v.append(f'<path d="M{x},{y}L{xx},{yy}" stroke="black" fill="none" marker-end="url(#arrow)"/>')
rect(20,15,1060,48,'#9D755D');text(40,47,'A   Base to uncertainty-layer membership: matched archived records',25)
for x,s in [(42,'Stage'),(150,'Base'),(320,'Base ∩ U'),(535,'Share of Base'),(770,'Base outside U')]:text(x,103,s,23)
for j,r in enumerate(stages):
    y=125+j*53;rect(30,y-16,1040,49,'#ECECEC' if j%2==0 else 'white')
    text(42,y+15,r['stage']+('*' if j==0 else ''));text(150,y+15,f"{r['base_n']:,}")
    text(320,y+15,f"{r['intersection_n']:,}")
    rect(535,y,140*r['u_share_of_base_pct']/100,19,'#72B7B2');text(690,y+15,f"{r['u_share_of_base_pct']:.1f}%",21,'end')
    text(770,y+15,f"{r['base_only_n']:,} ({r['base_only_pct']:.1f}%)")
text(35,420,'* S1 U includes reconstructed Scopus membership; its percentage is provisional.',20)
text(35,448,'S3 U totals 49: 48 overlap Base; one U-only record is retained separately.',20)
text(35,476,'Outside U means no matching layer membership, not evidence of no uncertainty analysis.',20)
rect(20,505,1060,48,'#9D755D');text(40,537,'B   Selected S1–S5 + U reports: retrieval, eligibility and inclusion',25)
text(35,581,'Separate selected-set pathway; no inferred funnel from panel A to these 21 reports.',20)
left=[['Previously selected reports (n = 21)','S1–S3 and S4–S5 selections'],['Reports sought for retrieval (n = 21)'],['Reports assessed for eligibility (n = 20)'],['Reports included in synthesis (n = 20)','23 assessed publication–boundary contexts']]
right=[[],['Reports not retrieved (n = 1)'],['Full-text reports excluded (n = 0)'],['Full-text boundary coverage','S1→S2: 9; S2→S3: 6','S3→S4: 0; S4→S5: 1; Other→S5: 7']]
for j,(l,r) in enumerate(zip(left,right)):
    y=610+j*137;box(130,y,440,103,l)
    if r:box(650,y,420,103,r);arrow(570,y+51,650,y+51)
    if j<3:arrow(350,y+103,350,y+137)
for label,y,h in [('Selected',610,103),('Retrieval',747,103),('Eligibility',884,103),('Included',1021,103)]:
    rect(30,y,62,h,'#ECECEC');v.append(f'<text x="65" y="{y+h/2}" transform="rotate(-90 65 {y+h/2})" font-family="Times New Roman" text-anchor="middle" font-size="21">{label}</text>')
text(35,1170,'U membership, title/abstract treatment and full-text transfer evidence use different denominators.',20)
text(35,1198,'Broad eligibility remains open. Stages overlap; stage counts must not be summed.',20)
v.append('</svg>');(O/'figures/prisma_base_u_en.svg').write_text('\n'.join(v),encoding='utf8')

v=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="670" viewBox="0 0 1100 670"><rect width="1100" height="670" fill="white"/>']
rect(20,15,1060,48,'#9D755D');text(40,47,'Uncertainty treatment among assessed U-layer candidates',25)
text(35,102,'Title/abstract evidence: S4 n = 143; S5 n = 331; union n = 392 (82 overlap).',22)
colors=['#ECECEC','#4C78A8','#72B7B2','#9D755D']
cats=['mention_or_no_demonstrated_uq','sensitivity_scenarios_only','quantified_uncertainty_only','explicit_propagation']
for j,i in enumerate([4,5]):
    y=145+j*90;text(35,y+35,f'S{i}',25);x=120
    for cat,color in zip(cats,colors):
        r=next(r for r in mech_summary if r['stage']==f'S{i}' and r['category']==cat)
        w=930*r['percent']/100;rect(x,y,w,55,color);text(x+w/2,y+34,f"{r['count']} ({r['percent']:.1f}%)",20,'middle');x+=w
for j,(label,color) in enumerate(zip(['Mention / no demonstrated UQ','Sensitivity or scenarios only','Quantified uncertainty only','Explicit propagation; boundary unspecified'],colors)):
    x=35+(j%2)*530;y=357+(j//2)*43;rect(x,y-16,20,20,color);text(x+30,y,label,21)
text(35,460,'Explicit cross-stage screening claims: S4 1/143 (0.7%); S5 3/331 (0.9%).',22)
rect(35,490,1030,94,'#ECECEC');text(550,525,'Full-text appraisal of the three distinct cross-stage candidates:',23,'middle')
text(550,558,'1 partial S4→S5 case + 2 other-input→S5 cases',24,'middle')
text(35,622,'Propagation within a model does not establish transfer across S boundaries.',21)
text(35,651,'These selected-candidate percentages are not prevalence estimates for all Base publications.',21)
v.append('</svg>');(O/'figures/base_u_treatment_en.svg').write_text('\n'.join(v),encoding='utf8')

# Compact companion report with semantic screening and full-text boundary evidence.
def table(headers,rows):
    return '<table><thead><tr>'+''.join('<th>'+html.escape(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+html.escape(str(x))+'</td>' for x in r)+'</tr>' for r in rows)+'</tbody></table>'
report='''<html><head><meta charset="utf-8"><style>@page{size:A4;margin:17mm}body{font:11pt/1.35 'Times New Roman';color:black}p{text-align:justify}h1{font-size:17pt}h2{font-size:13pt}table{border-collapse:collapse;width:100%;font-size:10pt}th,td{border-bottom:1px solid #aaa;padding:6px;text-align:left}th{background:#ECECEC}.page{break-before:page}</style></head><body><h1>Base, uncertainty treatment and transition evidence across S1–S5</h1><p>This audit separates search-layer membership from substantive uncertainty treatment and full-text evidence of transfer. It recomputes archived data; it does not rerun searches or introduce new screening decisions.</p>'''
report+=table(['Stage','Base','U layer','Base ∩ U','% Base','Base outside U'],[[r['stage'],r['base_n'],r['u_layer_n'],r['intersection_n'],f"{r['u_share_of_base_pct']:.1f}%",r['base_only_n']] for r in stages])
report+='''<p>S1–S3 are pre-screening merged corpora, including scope noise. S1 uncertainty membership includes reconstructed Scopus records and requires query verification. S3 has one U-only publication (DOI 10.1111/jiec.13604); it is not silently added to the Base denominator. S4–S5 use adjudicated canonical identifiers. Parsing both pipe and semicolon separators recovers memberships previously hidden by compound query cells. Different stage scopes and review histories prevent interpreting these percentages as comparative uncertainty-analysis prevalence.</p><p>The S4–S5 union contains 9,587 Base records and 1,934 U-layer records (20.2%). These are retrieval memberships, not final relevant studies. Among U-layer records, 392 clear candidates have archived title/abstract mechanism assessments; these assessments do not cover the complete Base or U sets.</p><h2>Uncertainty treatment in assessed U candidates</h2>'''
cats=['mention_or_no_demonstrated_uq','sensitivity_scenarios_only','quantified_uncertainty_only','explicit_propagation']
labels=['Mention / no demonstrated UQ','Sensitivity or scenarios only','Quantified uncertainty only','Explicit propagation (not necessarily cross-stage)']
rows=[]
for cat,label in zip(cats,labels):
    vals=[]
    for i in [4,5]:
        r=next(x for x in mech_summary if x['stage']==f'S{i}' and x['category']==cat);vals.append(f"{r['count']}/{r['assessed_title_abstract_n']} ({r['percent']:.1f}%)")
    rows.append([label]+vals)
report+=table(['Title/abstract classification','S4 query members','S5 query members'],rows)
report+='''<p>Stage groups overlap (82 shared records); their 143 and 331 assessments represent 392 distinct publications. Across the union, 144 only mention uncertainty or provide no demonstrated UQ, 156 use sensitivity/scenarios, 40 quantify uncertainty without an explicit propagation classification, and 52 are classified as explicit propagation. These historical title/abstract labels are not proof of propagation across an S boundary.</p><h2 class="page">Cross-stage claims and full-text adjudication</h2>'''
report+=table(['Title/abstract S4–S5 claim','S4 query members','S5 query members'],[[cat]+[next(f"{r['count']}/{r['assessed_title_abstract_n']} ({r['percent']:.1f}%)" for r in mech_summary if r['stage']==f'S{i}' and r['axis']=='cross_stage_claim' and r['category']==cat) for i in [4,5]] for cat in ['explicit','possible','not_demonstrated']])
report+='''<p>Three union records carried explicit cross-stage claims in title/abstract screening. Full-text appraisal places Almeida et al. at S4→S5 with partial transfer; Aljawhari et al. and Caruso et al. concern other inputs→S5. Thus three screening claims must not be reported as three confirmed S4→S5 transfers.</p>'''
report+=table(['Boundary','Assessed contexts','Partial transfer (P)','Quantified selected inputs (E)','Other codes'],[[label,n,sum(x['assessments'] for x in boundary if x['context']==c and x['continuity_code']=='P'),sum(x['assessments'] for x in boundary if x['context']==c and x['continuity_code']=='E'),'; '.join(f"{x['continuity_code']}={x['assessments']}" for x in boundary if x['context']==c and x['continuity_code'] not in ['P','E'] and x['assessments']) or '—'] for c,label,n in [('B12','S1→S2',9),('B23','S2→S3',6),('B34','S3→S4',0),('B45','S4→S5',1),('O5','Other inputs→S5',7)]])
report+='''<p>Q: discussion/review; N: downstream transfer not demonstrated; R: inputs prepared for propagation; S: sensitivity/representation comparison. P and E must not be combined as proof of a complete uncertain chain. The 23 contexts come from 20 publications. A zero assessed-context denominator gives an undefined percentage, not zero prevalence.</p><h2>PRISMA accounting and reproducibility</h2><p>The selected set has 21 reports sought, one not retrieved, 20 assessed, zero full-text exclusions and 20 included. It is separate from the broad search denominators. Missing links between broad screening and focused selection cannot be reconstructed by subtraction. All source hashes, record-level memberships, category decisions and full-text context reasons accompany this report in CSV files. No unassessed record is labelled as lacking uncertainty analysis.</p><p>Population-wide uncertainty-treatment rates for S1–S5 remain unestablished. The reported rates are exact arithmetic for the specified archived cohorts, with the S1 provenance qualification retained. Wider substantive rates require systematic content review of the remaining records, including Base-only records.</p></body></html>'''
(D/'report_en.html').write_text(report,encoding='utf8')
(D/'README.md').write_text('# Base and uncertainty-layer comparison\n\nSee report_en.pdf for the complete audit. Counts are recomputed from existing archived records; no new screening decisions. stage_base_u_counts.csv and record_membership.csv reproduce Figure 2c. title_abstract_treatment_counts.csv describes the 392 assessed S4/S5 candidates. fulltext_boundary_counts.csv uses the 23 contexts from 20 included publications. Stage memberships overlap. S1 U membership is partly reconstructed; S3 has one U-only record. Base outside U is not equivalent to absence of uncertainty analysis.\n',encoding='utf8')

p=O/'manuscript_en.html';s=p.read_text(encoding='utf8')
old=r'(<div class="figure[^\"]*"><img src="figures/prisma_base_u_en.svg"><p class="caption">).*?(</p></div>)'
s,n=re.subn(old,lambda m:m[1]+'Figure 2c. Base-to-U membership by stage and the separate selected-report PRISMA pathway. Percentages use the Base intersection; S1 is provisional. Search non-membership does not establish absence of uncertainty analysis.'+m[2],s,flags=re.S);assert n==1
prefix='(?:For clarity, the four domain combinations|For each stage, B\\(i\\) and U\\(i\\))'
s,n=re.subn(r'<p>'+prefix+r'.*?</p>','<p>For each stage, B(i) and U(i) are sets of publication identities. The matched uncertainty-layer share is 100 |B(i) ∩ U(i)| / |B(i)|; U-only records are retained separately. Search membership, title/abstract uncertainty treatment and full-text transfer evidence are reported separately, with their own denominators (Figure 2c). Base-only records are not classified as having no uncertainty analysis. The S1 U layer partly reconstructs Scopus membership and remains provisional.</p>',s,count=1,flags=re.S);assert n==1
prefix='(?:The source, method and outcome dataset combines|Matched U membership is)'
s,n=re.subn(r'<p>'+prefix+r'.*?</p>','<p>Matched U membership is 256/878 (29.2%) for S1, 44/246 (17.9%) for S2, 48/165 (29.1%) for S3, 543/3,098 (17.5%) for S4 and 1,584/7,593 (20.9%) for S5. These archived retrieval shares are not content-based prevalence estimates. S3 also has one U-only record. In the assessed U candidates, explicit propagation is reported in 17/143 S4 and 43/331 S5 title/abstract records; this need not cross a stage boundary. Three S4–S5 screening claims reduce at full-text appraisal to one partial S4→S5 case and two other-input→S5 cases. The companion audit provides memberships, percentages and reasons.</p>',s,count=1,flags=re.S);assert n==1
# Remove redundant explanation to keep the added evidence within the existing word budget.
prefix='(?:The percentages are frequencies of recorded evidence.|Source, method and outcome frequencies use all 20)'
s,n=re.subn(r'<p>'+prefix+r'.*?</p>','<p>Source, method and outcome frequencies use all 20 included publications, combining 17 archived codings and three subsequent full-text codings. These percentages describe recorded evidence, not shares of output variance or model performance.</p>',s,count=1,flags=re.S);assert n==1
p.write_text(s,encoding='utf8')
if 'figures/base_u_treatment_en.svg' not in s:
    anchor='<div class="figure small"><img src="figures/focused_selection_status_en.svg">'
    graphic='<div class="figure"><img src="figures/base_u_treatment_en.svg"><p class="caption">Figure 2d. Content-based treatment within assessed S4–S5 U candidates. Stage memberships overlap; cross-stage screening claims are distinguished from full-text boundary findings.</p></div>\n'
    assert anchor in s;s=s.replace(anchor,graphic+anchor)
    p.write_text(s,encoding='utf8')
print(json.dumps(stages,indent=2))

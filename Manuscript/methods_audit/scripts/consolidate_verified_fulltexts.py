from pathlib import Path
import csv,json,collections,re
p=Path('outputs/Manuscript/methods_audit/eligibility')
rows=[]
for fam,fn in [('S_U_selected','su_fulltext_verified.csv'),('DT_bridge_focused','bridge_fulltext_verified.csv'),('DT_U_focused','dtu_fulltext_verified.csv')]:
 for r in csv.DictReader((p/fn).open(encoding='utf-8-sig')):
  def first(*ks):return next((r[k] for k in ks if r.get(k)), '')
  rows.append(dict(family=fam,record_id=first('paper_id','record_id','publication_id'),doi=r['doi'].lower().strip(),title=r['title'],decision=r['decision'],evidence_role=r['evidence_role'],reason=first('decision_reason','reason'),evidence_locator=first('evidence_locator','source_locator','pdf_page_evidence'),limits=first('interpretive_limit','limitations','limitations_and_boundary'),sha256=first('sha256','source_sha256'),assessment_scope=first('assessment_scope','focused_scope','review_scope')))
for x in rows:
 x['source_type']='publisher_fulltext_HTML' if x['record_id']=='DTUM-006' else ('not_retrieved' if x['decision']=='not_retrieved' else 'local_fulltext')
 x['hash_scope']='assessment_notes_only' if x['record_id']=='DTUM-006' else 'reviewed_local_file'
def write(name,rr):
 with (p/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=rr[0]);w.writeheader();w.writerows(rr)
write('verified_fulltext_memberships.csv',rows)
groups=collections.defaultdict(list)
for r in rows:groups[r['doi'] or re.sub(r'\W','',r['title'].lower())].append(r)
unique=[]
for key,rs in groups.items():
 ds=set(r['decision'] for r in rs)
 decision='include' if 'include' in ds else ('exclude' if 'exclude' in ds else 'not_retrieved')
 unique.append(dict(publication_key=key,title=rs[0]['title'],doi=rs[0]['doi'],families=';'.join(r['family'] for r in rs),record_ids=';'.join(r['record_id'] for r in rs),decision=decision,membership_decisions=';'.join(r['family']+':'+r['decision'] for r in rs)))
write('verified_fulltext_unique_publications.csv',unique)
counts={'scope':'Previously selected focused sets only; not closure of the broad search families','memberships':len(rows),'unique_publications':len(unique),'decisions':dict(collections.Counter(r['decision'] for r in unique)),'by_family':{f:dict(collections.Counter(r['decision'] for r in rows if r['family']==f)) for f in sorted(set(r['family'] for r in rows))}}
(p/'verified_fulltext_counts.json').write_text(json.dumps(counts,indent=2),encoding='utf-8')
assert all(r['evidence_locator'] and r['reason'] and r['sha256'] for r in rows if r['decision']!='not_retrieved')
print(json.dumps(counts,indent=2));print('Overlaps:',[(k,[r['record_id'] for r in v]) for k,v in groups.items() if len(v)>1])

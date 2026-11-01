"""Rebuild authored reassessment decisions; no automatic semantic review."""
import csv,io,json,zipfile,hashlib
from pathlib import Path
from collections import Counter
HERE=Path(__file__).resolve().parent
INPUT=HERE.parent/'tables/all_records_screening.zip'
with zipfile.ZipFile(INPUT) as z:
 rows=list(csv.DictReader(io.TextIOWrapper(z.open('all_records_screening.csv'),encoding='utf-8-sig')))
records={r['record_id']:r for r in rows}
dup=json.loads((HERE/'duplicate_decisions.json').read_text(encoding='utf-8'))
reviews=json.loads((HERE/'title_abstract_decisions.json').read_text(encoding='utf-8'))
queue_ids={r['record_id'] for r in rows if r['screening_status'] in ('retain_unclear','exclude_automated')}
requested_read=len(queue_ids & set(reviews))
complete=requested_read==len(queue_ids)
supplemental_path=HERE/'supplemental_integrity_decisions.json'
supplemental=json.loads(supplemental_path.read_text(encoding='utf-8')) if supplemental_path.exists() else {}
assert not (set(supplemental)&set(reviews)), 'Supplemental decisions must not overwrite queue decisions'
reviews={**reviews,**supplemental}
resolution_path=HERE/'canonical_conflict_resolutions.json'
resolutions=json.loads(resolution_path.read_text(encoding='utf-8')) if resolution_path.exists() else {}
aliases={k:k for k in records};canonical_dois={};audit=[]
for group,v in dup.items():
 ids=v['candidate_ids'].split(';'); merge_ids=ids if v['decision']=='merge' else ids[:2] if v['decision']=='partial_merge' else []
 canonical=''
 if merge_ids:
  canonical=max(merge_ids,key=lambda x:(bool(records[x]['doi']),len(records[x]['abstract'])))
  for x in merge_ids:aliases[x]=canonical
  if 'canonical_doi' in v:canonical_dois[canonical]=v['canonical_doi']
 audit.append({'group_id':'DUP-'+str(int(group)+1).zfill(3),**v,'canonical_id':canonical,'merged_record_ids':';'.join(merge_ids),'reviewer':'assistant bibliographic adjudication','independent_human_review':'not performed'})
def csvout(name,rr):
 fields=list(dict.fromkeys(k for r in rr for k in r))
 with (HERE/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rr)
csvout('duplicate_group_adjudication.csv',audit)
csvout('record_alias_map.csv',[{'original_id':x,'canonical_id':y,'removed_as_duplicate':str(x!=y).lower()} for x,y in aliases.items()])
members={}
for x,y in aliases.items():members.setdefault(y,[]).append(x)
out=[]
for canonical,ids in members.items():
 r=dict(records[canonical]);r['canonical_record_id']=canonical;r['all_member_record_ids']=';'.join(ids)
 r['supplied_doi_values']=' | '.join(dict.fromkeys(records[x]['doi'] for x in ids if records[x]['doi']))
 if canonical in canonical_dois:r['doi']=canonical_dois[canonical]
 for field in ['databases','queries','source_files','source_identifiers']:
  r[field]=' | '.join(dict.fromkeys(records[x][field] for x in ids if records[x][field]))
 r['abstract']=max((records[x]['abstract'] for x in ids),key=len)
 for field in r:
  if not r[field] and field in records[canonical] and not (field=='doi' and canonical in canonical_dois):
   r[field]=next((records[x][field] for x in ids if records[x].get(field)),r[field])
 rr=[(x,reviews[x]) for x in ids if x in reviews]
 r['adjudication_status']='not_yet_reassessed';r['adjudication_reason']='';r['adjudication_evidence']='';r['adjudication_reviewed_ids']='';r['adjudication_reviewer']=''
 if rr:
  statuses={v['decision'] for x,v in rr}
  r['adjudication_status']=next(iter(statuses)) if len(statuses)==1 else 'retain_conflicting_review_decisions'
  r['adjudication_reason']=' | '.join(v['reason'] for x,v in rr)
  r['adjudication_evidence']=' | '.join(v['evidence'] for x,v in rr)
  r['adjudication_reviewed_ids']=';'.join(x for x,v in rr)
  r['adjudication_reviewer']=' | '.join(dict.fromkeys(v.get('reviewer_method','assistant title-and-complete-available-abstract reading; no independent human review') for x,v in rr))
 r['prior_member_decisions']=''
 if canonical in resolutions:
  v=resolutions[canonical]
  r['prior_member_decisions']=';'.join(sorted({v0['decision'] for _,v0 in rr}))
  r['adjudication_status']=v['decision']
  r['adjudication_reason']+=' | Canonical reconciliation: '+v['reason']
  r['adjudication_evidence']+=' | '+v['evidence']
 out.append(r)
with zipfile.ZipFile(HERE/'revised_records.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
 with z.open('revised_records.csv','w') as f:
  t=io.TextIOWrapper(f,encoding='utf-8-sig',newline='');w=csv.DictWriter(t,fieldnames=list(out[0]));w.writeheader();w.writerows(out);t.flush()
 with z.open('merged_metadata_provenance.json','w') as f:
  f.write(json.dumps({c:[records[x] for x in ids] for c,ids in members.items() if len(ids)>1},ensure_ascii=False).encode())
csvout('title_abstract_review_log.csv',[{'record_id':x,'canonical_id':aliases[x],**records[x],**v,'reviewer':v.get('reviewer_method','assistant; independent human review not performed')} for x,v in reviews.items()])
summary={'status':'REQUESTED_REASSESSMENT_COMPLETE' if complete else 'PARTIAL_NOT_FINAL','input_records':len(rows),'duplicate_groups_examined':len(dup),'duplicate_group_decisions':dict(Counter(v['decision'] for v in dup.values())),'additional_duplicate_records_removed':len(rows)-len(out),'remaining_records':len(out),'requested_title_abstract_records':len(queue_ids),'requested_records_read':requested_read,'supplemental_integrity_reviews':len(supplemental),'original_records_actually_read_this_revision':len(reviews),'original_records_not_yet_read_in_requested_queue':len(queue_ids)-requested_read,'canonical_records_with_reading_decision':sum(r['adjudication_status']!='not_yet_reassessed' for r in out),'canonical_outcomes':dict(Counter(r['adjudication_status'] for r in out)),'independent_human_reviewers':0,'fulltexts_assessed_in_this_revision':0,'final_included_studies':None}
(HERE/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
csvout('prisma_reassessment_counts.csv',[{'item':k,'count':v,'qualification':'Requested title/abstract reassessment only; full-text eligibility not performed'} for k,v in {'database_unique_records_identified':14869,'previous_duplicates_removed':4951,'additional_duplicates_removed':len(rows)-len(out),'records_after_current_deduplication':len(out),'requested_records_actually_read':requested_read,'requested_records_still_unread':len(queue_ids)-requested_read,'supplemental_integrity_reviews':len(supplemental),'fulltexts_assessed':0,'final_included_studies':''}.items()])
assert len(aliases)==9918 and len(out)+sum(x!=y for x,y in aliases.items())==9918
assert all(aliases[y]==y for y in aliases.values())
print(json.dumps(summary,ensure_ascii=False))

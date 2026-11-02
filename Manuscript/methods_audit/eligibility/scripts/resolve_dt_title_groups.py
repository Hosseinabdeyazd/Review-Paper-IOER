from pathlib import Path
import csv,json
root=Path('outputs/Digital Twin Material Flow Review')
out=Path('outputs/Manuscript/methods_audit/eligibility/deduplication');out.mkdir(parents=True,exist_ok=True)
def read(p):return list(csv.DictReader(p.open(encoding='utf-8-sig')))
def write(p,rows):
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
summ=[]
for family,b,groupfile in [('Base_DT',root/'analysis','possible_title_duplicates.csv'),('Base_DT_U',root/'uncertainty_stage_searches_2026-11-02/analysis','title_duplicate_adjudication.csv')]:
 records=read(b/'deduplicated_records.csv');byid={r['record_id']:r for r in records};aliases={r['record_id']:r['record_id'] for r in records};decisions=[]
 for i,g in enumerate(read(b/groupfile)):
  ids=g['record_ids'].split(';');members=[byid[x] for x in ids]
  if family=='Base_DT':
   merge=i not in [2,6,8,10,39]
   reason=('Same article title/year and corresponding author sequence/venue; indexing variants retained in source records.' if merge else 'Conference-container records or distinct editorial authors/DOIs are not merged solely on generic title.')
   if i==40: reason='Same article title, author list and abstract; issue-number DOI variant retained as alias. Canonical issue 7 supported by published citation 10.1155/ina/9640243; not an independent study.'
   if i==41:reason='Publisher article 18814 confirms DOI 10.4995/vitruvio-ijats.2023.18814; nonhyphenated variant is an indexing alias.'
  else:
   merge=g['merge_suggestion']=='merge_suggested';reason=g['reason']
  canonical=next((r['record_id'] for r in members if r['doi']),ids[0]) if merge else ''
  if family=='Base_DT' and i==40:canonical=next(r['record_id'] for r in members if '/7/' in r['doi'])
  if family=='Base_DT' and i==41:canonical=next(r['record_id'] for r in members if 'vitruvio-ijats' in r['doi'])
  if merge:
   for id in ids:aliases[id]=canonical
  decisions.append(dict(group=i,record_ids=';'.join(ids),decision='merge' if merge else 'retain_separate',canonical_id=canonical,reason=reason,scope='Bibliographic identity only; not eligibility or full-text assessment'))
 canonical_rows=[]
 for r in records:
  if aliases[r['record_id']]!=r['record_id']:continue
  row=dict(r);mem=[x for x in records if aliases[x['record_id']]==r['record_id']]
  row['source_record_ids']=';'.join(x['record_id'] for x in mem)
  row['doi_variants']=';'.join(sorted({x['doi'] for x in mem if x['doi']}))
  for key in ['databases','stages']:
   row[key]=';'.join(sorted({v.strip() for x in mem for v in x[key].replace('|',';').split(';') if v.strip()}))
  canonical_rows.append(row)
 write(out/f'{family}_group_decisions.csv',decisions)
 write(out/f'{family}_canonical_records.csv',canonical_rows)
 write(out/f'{family}_aliases.csv',[dict(source_id=k,canonical_id=v) for k,v in aliases.items()])
 summ.append(dict(family=family,before=len(records),after=len(canonical_rows),additional_duplicates=len(records)-len(canonical_rows),groups_resolved=len(decisions)))
(out/'summary.json').write_text(json.dumps(summ,indent=2),encoding='utf-8')
print(json.dumps(summ))

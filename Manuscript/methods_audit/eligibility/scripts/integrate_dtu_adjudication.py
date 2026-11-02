from pathlib import Path
import csv,json,collections
p=Path('outputs/Manuscript/methods_audit/eligibility')
def read(n):return list(csv.DictReader((p/n).open(encoding='utf-8-sig')))
r=read('broad_dtu_unique_decisions.csv');by={x['record_id']:x for x in r}
for fn in ['broad_dtu_unclear_adjudication.csv','broad_dtu_policy_corrections.csv']:
 for u in read(fn):
  x=by[u['record_id']];x.update({k:u[k] for k in ['decision','reason','evidence_quote']});x['source_batch']+=';'+fn
with (p/'broad_dtu_adjudicated_decisions.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=r[0]);w.writeheader();w.writerows(r)
c=collections.Counter(x['decision'] for x in r);print(c)
(p/'broad_dtu_adjudicated_counts.json').write_text(json.dumps({'identified_query_occurrences':903,'duplicates_before_screening':375,'records_screened':528,'additional_duplicate_records_identified_during_screening':2,'unique_publications_after_screening':526,'unique_publication_decisions':dict(c),'retained_not_included':True,'remaining_unclear_carried_forward_for_retrieval':5},indent=2),encoding='utf-8')

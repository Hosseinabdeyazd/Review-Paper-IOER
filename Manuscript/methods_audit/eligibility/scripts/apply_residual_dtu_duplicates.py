from pathlib import Path
import csv,json,collections
p=Path('outputs/Manuscript/methods_audit/eligibility')
def read(f):return list(csv.DictReader((p/f).open(encoding='utf-8-sig')))
r=read('broad_dtu_title_abstract_decisions.csv');by={x['record_id']:x for x in r};aliases={}
for g in read('residual_duplicate_decisions.csv'):
 if g['decision']=='merge_alias':
  for aid in g['alias_record_ids'].split(';'):aliases[aid]=g['canonical_record_id']
for aid,cid in aliases.items():
 a,c=by[aid],by[cid]
 assert a['decision']==c['decision'],(aid,cid,a['decision'],c['decision'])
 for k in ['stages','databases']:
  c[k]=';'.join(sorted(set(a[k].split(';')+c[k].split(';'))))
out=[]
for x in r:
 if x['record_id'] in aliases:continue
 x['source_screened_ids']=';'.join([x['record_id']]+[a for a,c in aliases.items() if c==x['record_id']]);out.append(x)
with (p/'broad_dtu_unique_decisions.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(out)
assert len(out)==526
print(collections.Counter(x['decision'] for x in out))

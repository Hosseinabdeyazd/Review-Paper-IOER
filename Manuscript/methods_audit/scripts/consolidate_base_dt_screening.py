"""Validate record-level screening; do not infer full-text eligibility."""
from pathlib import Path
import csv, json, re, collections, hashlib

p=Path('outputs/Manuscript/methods_audit/eligibility')
def read(path):
    return list(csv.DictReader(path.open(encoding='utf-8-sig')))
def write(path, rows):
    if not rows: return
    keys=list(dict.fromkeys(k for r in rows for k in r))
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)
def norm(s): return re.sub(r'\s+',' ',s).strip()
canonical=read(p/'deduplication/Base_DT_canonical_records.csv')
pending_source=read(p/'broad_dt_unreviewed.csv')
by_id={x['record_id']:x for x in canonical}
out=[]; seen=set(); indices=set(); errors=[]
for f in sorted(p.glob('broad_dt_[0-9]*_[0-9]*.csv')):
    for x in read(f):
        x['reason']=x.get('reason') or x.get('decision_reason','')
        i=int(x['row_index']);rid=x['record_id']
        assert rid==pending_source[i]['record_id'],(f,i,rid)
        assert rid not in seen and i not in indices,(f,rid)
        assert x['decision'] in {'retain_fulltext','retain_secondary','exclude_domain','unclear'}
        assert x['reason'].strip(),rid
        x['evidence_quote']=x.get('evidence_quote') or x.get('source_quote','')
        q=norm(x['evidence_quote'])
        text=norm(by_id[rid].get('abstract','')+' '+by_id[rid]['title'])
        if q and q not in text: errors.append({'record_id':rid,'file':f.name,'issue':'quote is not a literal normalized source substring'})
        row=dict(by_id[rid]);row.update({k:v for k,v in x.items() if k not in row})
        row['decision']=x['decision'];row['reason']=x['reason'];row['decision_source']=f.name
        row['assessment_scope']='title_and_abstract_only'
        row['source_sha256']=hashlib.sha256((by_id[rid]['title']+'\n'+by_id[rid].get('abstract','')).encode()).hexdigest()
        out.append(row);seen.add(rid);indices.add(i)
for x in read(p/'broad_dt_transferred_ta.csv'):
    rid=x['record_id']; assert rid not in seen
    row=dict(by_id[rid]);row.update(x);row['decision_source']='broad_dt_transferred_ta.csv'
    row['assessment_scope']='same_publication_domain_screening_transfer_only'
    out.append(row);seen.add(rid)
remaining=[x for x in canonical if x['record_id'] not in seen]
write(p/'broad_dt_title_abstract_decisions.csv',out)
write(p/'broad_dt_pending_title_abstract.csv',remaining)
if not remaining:
    with (p/'broad_dt_pending_title_abstract.csv').open('w',encoding='utf-8-sig',newline='') as f:
        csv.DictWriter(f,fieldnames=list(canonical[0])).writeheader()
write(p/'broad_dt_quote_validation_issues.csv',errors)
groups=collections.defaultdict(list)
for x in out:groups[re.sub(r'\W','',x['title'].casefold())].append(x)
repeats=[]
for key,rr in groups.items():
    if len(rr)>1:
        for x in rr:repeats.append({k:x.get(k,'') for k in ['record_id','title','year','doi','authors','decision','reason']})
write(p/'broad_dt_residual_title_groups.csv',repeats)
summary={'canonical_records_before_residual_adjudication':len(canonical),'screened_records':len(out),'individually_read_new_records':len(indices),'same_publication_transfers':len(out)-len(indices),'remaining_title_abstract_records':len(remaining),'decision_counts':dict(collections.Counter(x['decision'] for x in out)),'quote_validation_issues':len(errors),'residual_exact_title_groups':sum(len(v)>1 for v in groups.values()),'status':'Title/abstract decisions only. Retained records are not full-text Included studies.'}
(p/'broad_dt_screening_validation.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))

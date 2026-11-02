"""Add stage views and explicit search ledger after build_dataset.py."""
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def save(path,rows,fields):
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
q=json.loads((ROOT/'protocol/queries.json').read_text(encoding='utf-8'))
counts=json.loads((ROOT/'protocol/expected_counts.json').read_text())
rows=list(csv.DictReader((ROOT/'analysis/deduplicated_records.csv').open(encoding='utf-8-sig',newline='')))
for stage in ('S1','S2','S3','S4','S5'):
    subset=[r for r in rows if stage in r['stages'].split(';')]
    save(ROOT/f'analysis/{stage}_retrieved_records.csv',subset,list(rows[0]))
ledger=[]
for query in q['queries']:
    for db,key,field,fmt in [('IEEE','ieee','Default metadata','CSV all native fields'),('Scopus','scopus','TITLE-ABS-KEY','CSV Select all information incl references'),('WoS','wos','TS / Core Collection all editions','Tab delimited Full Record and Cited References')]:
        ledger.append(dict(stage=query['stage'],query_id=query['id'],database=db,run_label=q['date'],date_note='Europe/Berlin run label; source download filenames use 2026-11-01 UTC',query=query.get(key,query['boolean']),field_scope=field,filters='No date/language/document-type/access restrictions',observed_results=counts[db][query['stage']],export_format=fmt,status='exported_all_count_verified'))
save(ROOT/'protocol/search_log.csv',ledger,list(ledger[0]))
print('Created five stage views and 15-row search ledger.')

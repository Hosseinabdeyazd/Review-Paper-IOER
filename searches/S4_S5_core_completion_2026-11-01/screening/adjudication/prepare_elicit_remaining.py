import csv,io,zipfile,json
from pathlib import Path
root=Path('outputs/S4 S5 Core Review/screening')
done=json.loads((root/'adjudication/title_abstract_decisions.json').read_text(encoding='utf-8'))
with zipfile.ZipFile(root/'tables/all_records_screening.zip') as z:
 rows=[r for r in csv.DictReader(io.TextIOWrapper(z.open('all_records_screening.csv'),encoding='utf-8-sig')) if r['screening_status'] in ['retain_unclear','exclude_automated'] and r['record_id'] not in done]
p=Path('work/S4_S5_remaining_7188.csv')
fields=['record_id','title','abstract','authors','year','doi','source','document_type']
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
assert len(rows)==7188
print(json.dumps({'path':str(p.resolve()),'rows':len(rows),'bytes':p.stat().st_size}))

"""Validate and rebuild complete WoS DT-U corpus, preserving all native fields."""
from pathlib import Path
from collections import Counter
import csv,json,hashlib,re
csv.field_size_limit(100000000)
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'searches/Web_of_Science/DT-U/results/raw'
OUT=ROOT/'data/merged'; AN=ROOT/'analysis'
rows=[]; manifest=[]; columns=None
for start,end in [(1,500),(501,1000),(1001,1500),(1501,2000),(2001,2016)]:
    p=RAW/f'WOS_DTU_{start:04d}_{end:04d}.tsv'
    with p.open(encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(f,delimiter='\t'); batch=list(reader)
        if columns is None: columns=reader.fieldnames
        assert columns==reader.fieldnames
    assert len(batch)==end-start+1,(p,len(batch))
    manifest.append({'file':p.name,'start_record':start,'end_record':end,'rows':len(batch),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    for n,r in enumerate(batch,2):
        assert None not in r and all(v is not None for v in r.values())
        assert r['UT'].strip()
        rows.append({'record_id':r['UT'],'source_database':'Web of Science Core Collection','search_id':'WOS-DTU-2026-11-01','source_batch':p.name,'source_csv_row':n,**r})
assert len(rows)==2016==len({r['UT'] for r in rows})
def write(p,rs,cols):
    with p.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(rs)
write(OUT/'WOS_DTU_2016.csv',rows,list(rows[0]))
rules=json.loads((AN/'triage_rules.json').read_text(encoding='utf-8'))
triage=[]
for r in rows:
    text=' '.join(r[k] for k in ['TI','AB','DE','ID'])
    flags={k:int(bool(re.search(v,text,re.I))) for k,v in rules.items()}
    triage.append({'record_id':r['UT'],'DOI':r['DI'],'Title':r['TI'],'Year':r['PY'],**flags,'screening_status':'not_screened'})
write(AN/'WOS_mechanism_triage_2016.csv',triage,list(triage[0]))
audit={'expected_results':2016,'raw_rows':len(rows),'unique_UT':len({r['UT'] for r in rows}),'duplicates':0,'native_columns':columns,'native_column_count':len(columns),'missing_by_field':{k:sum(not r[k].strip() for r in rows) for k in columns},'doi_present_count':sum(bool(r['DI'].strip()) for r in rows),'year_counts':dict(sorted(Counter(r['PY'] for r in rows).items())),'index_field_counts':dict(Counter(r['WE'] for r in rows)),'mechanism_term_counts':{k:sum(r[k] for r in triage) for k in rules},'full_text_review':'not_performed','eligibility_screening':'not_performed'}
(RAW/'manifest.json').write_text(json.dumps({'database':'Web of Science Core Collection','query':'TS=("digital twin" AND uncertainty)','editions':'All available','date_restriction':'None added','sort':'Relevance','record_content':'Full Record and Cited References','batches':manifest},indent=2)+'\n',encoding='utf-8')
(AN/'WOS_corpus_audit.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8')
print(json.dumps(audit,indent=2))

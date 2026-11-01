"""Rebuild complete Scopus export, provenance and lexical reading queue (stdlib)."""
from pathlib import Path
from collections import Counter, defaultdict
import csv, json, hashlib, re

csv.field_size_limit(100000000)
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'searches/Scopus/DT-U/results/raw'
OUT=ROOT/'data/merged'
AN=ROOT/'analysis'
for d in (OUT,AN): d.mkdir(parents=True,exist_ok=True)
manifest=json.loads((RAW/'manifest.json').read_text(encoding='utf-8'))
records={}; provenance=defaultdict(list); conflicts=[]; total=0; cols=None
for batch in manifest['batches']:
    p=RAW/batch['file']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==batch['sha256'],p
    with p.open(encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(f); rows=list(reader)
        if cols is None: cols=reader.fieldnames
        assert cols==reader.fieldnames
    assert len(rows)==batch['rows']
    total+=len(rows)
    for n,r in enumerate(rows,2):
        assert None not in r and all(v is not None for v in r.values())
        eid=r['EID'].strip(); assert eid
        if eid in records and records[eid]!=r:
            conflicts.append({'EID':eid,'batch':batch['file'],'differing_fields':[k for k in cols if records[eid][k]!=r[k]]})
        records.setdefault(eid,r)
        provenance[eid].append(f"{batch['file']}:{n}")
assert len(records)==3501, f'Incomplete export: {len(records)} / 3501'
assert not conflicts, conflicts

def write(p,rows,fields):
    with p.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)

merged=[{'record_id':'SCOPUS:'+eid,'source_database':'Scopus','search_id':'SCOPUS-DTU-2026-11-01','source_rows':' | '.join(provenance[eid]),**r} for eid,r in sorted(records.items())]
write(OUT/'SCOPUS_DTU_3501.csv',merged,['record_id','source_database','search_id','source_rows']+cols)
parts=OUT/'SCOPUS_DTU_3501_parts'; parts.mkdir(exist_ok=True)
part_manifest=[]
for i in range(7):
    subset=merged[i*500:(i+1)*500] if i<6 else merged[i*500:]
    p=parts/f'SCOPUS_DTU_3501_part_{i+1:02d}_of_07.csv'
    write(p,subset,['record_id','source_database','search_id','source_rows']+cols)
    part_manifest.append({'file':p.name,'records':len(subset),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(parts/'manifest.json').write_text(json.dumps({'total_records':3501,'native_columns':45,'provenance_columns':4,'parts':part_manifest},indent=2)+'\n',encoding='utf-8')
rules=json.loads((AN/'triage_rules.json').read_text(encoding='utf-8'))
triage=[]
for eid,r in sorted(records.items()):
    text=' '.join(r[k] for k in ['Title','Abstract','Author Keywords','Index Keywords'])
    flags={k:int(bool(re.search(v,text,re.I))) for k,v in rules.items()}
    triage.append({'record_id':'SCOPUS:'+eid,'EID':eid,'DOI':r['DOI'],'Title':r['Title'],'Year':r['Year'],**flags,'screening_status':'not_screened'})
write(AN/'SCOPUS_mechanism_triage_3501.csv',triage,list(triage[0]))
audit={'expected_results':3501,'raw_rows':total,'unique_eids':len(records),'duplicate_occurrences':total-len(records),'conflicting_duplicate_records':conflicts,'native_columns':cols,'missing_by_field':{k:sum(not r[k].strip() for r in records.values()) for k in cols},'year_counts':dict(sorted(Counter(r['Year'] for r in records.values()).items())),'mechanism_term_counts':{k:sum(r[k] for r in triage) for k in rules},'max_field_characters':{k:max(len(r[k]) for r in records.values()) for k in cols},'truncation_option':False,'eligibility_screening':'not_performed','full_text_review':'not_performed'}
audit['abstract_unavailable_placeholder_count']=sum(r['Abstract'].strip().lower()=='[no abstract available]' for r in records.values())
audit['doi_present_count']=len(records)-audit['missing_by_field']['DOI']
(AN/'SCOPUS_corpus_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:audit[k] for k in ['expected_results','raw_rows','unique_eids','duplicate_occurrences','mechanism_term_counts']},indent=2))

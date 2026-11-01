"""Rebuild S4/S5 retrieval tables from untouched native exports (Python stdlib)."""
import csv, json, re, hashlib, zipfile, io
from pathlib import Path
from collections import defaultdict

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'final'; OUT.mkdir(exist_ok=True)
EXPECTED={'Scopus':[2538,415,6621,1359],'WoS':[1883,361,4834,1142],'IEEE':[242,54,433,81]}
QUERIES=['S4-1','S4-2','S5-1','S5-2']
def writecsv(path,rows,fields=None):
    rows=list(rows)
    fields=fields or list(dict.fromkeys(k for row in rows for k in row))
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def doi(x):
    return re.sub(r'^(https?://(dx\.)?doi\.org/|doi:\s*)','',x.strip(),flags=re.I).lower()
records=[]; manifests=[]; counts=[]; native_sets={}
for db,nums in EXPECTED.items():
    for q,n in zip(QUERIES,nums):
        group=[]; ids=[]
        for p in sorted((ROOT/'raw'/db).glob('*'+q+'*')):
            if p.suffix.lower() not in {'.csv','.txt','.tsv'}:continue
            with p.open(encoding='utf-8-sig',newline='') as f:
                # WoS TSV contains literal, unescaped quotation marks. Do not use CSV quoting.
                rr=list(csv.DictReader(f,delimiter='\t' if db=='WoS' else ',',quoting=csv.QUOTE_NONE if db=='WoS' else csv.QUOTE_MINIMAL))
            assert all(None not in row for row in rr),p
            manifests.append(dict(file=p.relative_to(ROOT).as_posix(),records=len(rr),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
            for row_number,row in enumerate(rr,start=2):
                get=lambda *keys: next((row[k] for k in keys if row.get(k)), '')
                d=doi(get('DOI','DI'))
                native=get('EID','UT') if db!='IEEE' else get('PDF Link')
                if db=='IEEE':
                    m=re.search(r'arnumber=(\d+)',native)
                    native=m.group(1) if m else native
                if not native:native=d or get('Document Title','Title','TI')
                rec=dict(database=db,query_id=q,stage=q[:2],stream='base' if q.endswith('1') else 'uncertainty',native_id=native,doi=d,title=get('Document Title','Title','TI'),authors=get('Authors','AU'),year=get('Year','Publication Year','PY'),source=get('Source title','Publication Title','SO'),abstract=get('Abstract','AB'),keywords=get('Author Keywords','Author keywords','DE'),document_type=get('Document Type','Document Identifier','DT'),source_file=p.relative_to(ROOT).as_posix(),source_row=row_number)
                group.append(rec);ids.append(native)
        native_sets[(db,q)]=set(ids)
        counts.append(dict(database=db,query_id=q,displayed_count=n,exported_count=len(group),unique_native_ids=len(set(ids)),doi_present=sum(bool(x['doi']) for x in group),abstract_present=sum(bool(x['abstract']) for x in group),status='complete' if n==len(group)==len(set(ids)) else 'INCOMPLETE'))
        records.extend(group)
writecsv(OUT/'search_counts.csv',counts)
writecsv(OUT/'raw_manifest.csv',manifests)
writecsv(OUT/'source_records.csv',records)
subsets=[]
for db in EXPECTED:
    for s in ['S4','S5']:
        missing=native_sets[(db,s+'-2')]-native_sets[(db,s+'-1')]
        subsets.append(dict(database=db,stage=s,uncertainty_outside_base=len(missing),ids=';'.join(sorted(missing))))
writecsv(OUT/'subset_audit.csv',subsets)
groups=defaultdict(list)
for row in records:
    key='doi:'+row['doi'] if row['doi'] else row['database']+':'+row['native_id']
    groups[key].append(row)
merged=[];membership=[]
for key,rows in sorted(groups.items()):
    uid='S45-'+hashlib.sha256(key.encode()).hexdigest()[:12]
    best=max(rows,key=lambda x:len(x['abstract']))
    rec={k:best[k] for k in ['doi','title','authors','year','source','abstract','keywords','document_type']}
    rec.update(record_id=uid,databases=';'.join(sorted({r['database'] for r in rows})),queries=';'.join(sorted({r['query_id'] for r in rows})),source_occurrences=len(rows),screening_status='not_screened')
    merged.append(rec)
    membership.extend(dict(record_id=uid,database=r['database'],query_id=r['query_id'],native_id=r['native_id'],source_file=r['source_file']) for r in rows)
writecsv(OUT/'deduplicated_records.csv',merged)
writecsv(OUT/'membership.csv',membership)
titles=defaultdict(list)
for r in merged:
    k=(re.sub(r'\W+','',r['title'].lower()),r['year'])
    if k[0]:titles[k].append(r)
candidate=[]
for rows in titles.values():
    if len(rows)>1:
        candidate.extend(dict(record_id=r['record_id'],title=r['title'],year=r['year'],doi=r['doi'],candidate_group=';'.join(x['record_id'] for x in rows)) for r in rows)
writecsv(OUT/'title_year_candidates.csv',candidate,['record_id','title','year','doi','candidate_group'])
summary=dict(raw_occurrences=len(records),unique_records=len(merged),removed_repeated_occurrences=len(records)-len(merged),doi_present=sum(bool(r['doi']) for r in merged),candidate_title_year_groups=sum(len(v)>1 for v in titles.values()),complete_queries=sum(x['status']=='complete' for x in counts),total_queries=12,subset_exceptions=sum(x['uncertainty_outside_base'] for x in subsets))
(OUT/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf8')
print(json.dumps(summary,indent=2))

"""Rebuild auditable metadata tables from native exports. Python 3, stdlib only."""
from pathlib import Path
import csv, json, hashlib, re, collections

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)
EXPECTED = {'IEEE':[389,9,64,160,102], 'Scopus':[1043,65,115,547,346], 'WoS':[652,38,61,331,202]}

def write(name, rows, fields=None):
    path=ROOT/name; path.parent.mkdir(parents=True,exist_ok=True)
    fields=fields or list(rows[0])
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def doi(s):
    return re.sub(r'^(?:https?://(?:dx\.)?doi.org/|doi:\s*)','',s.strip(),flags=re.I).lower()

def main():
    records=[]; files=[]; counts=collections.Counter()
    for p in sorted((ROOT/'raw').glob('*/*')):
        if p.suffix not in ('.csv','.txt'):continue
        db=p.parent.name; stage=re.search(r'S[1-5]',p.name).group()
        raw=p.read_bytes(); text=raw.decode('utf-8-sig')
        # StringIO preserves embedded line breaks in quoted abstracts/references.
        import io
        rows=list(csv.DictReader(io.StringIO(text),delimiter='\t' if db=='WoS' else ','))
        rows=[r for r in rows if any(v for v in r.values())]
        files.append(dict(file=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),rows=len(rows),fields=len(rows[0]) if rows else 0))
        counts[db,stage]+=len(rows)
        if db=='WoS':write('converted/'+p.stem+'.csv',rows)
        for i,r in enumerate(rows,1):
            def get(*keys):return next((r[k] for k in keys if r.get(k)), '')
            title=get('Document Title','Title','TI'); year=get('Publication Year','Year','PY'); d=doi(get('DOI','DI'))
            sid=get('EID','UT','PDF Link') or f'{p.name}:{i}'
            records.append(dict(database=db,stage=stage,query_id=f'DTMF-{stage}-v1',source_id=sid,title=title,year=year,doi=d,authors=get('Authors','AU'),source_title=get('Publication Title','Source title','SO'),abstract=get('Abstract','AB'),author_keywords=get('Author Keywords','DE'),index_keywords=get('IEEE Terms','Index Keywords','ID'),document_type=get('Document Identifier','Document Type','DT'),url=get('Link','PDF Link'),raw_file=p.relative_to(ROOT).as_posix(),raw_record=i))
    log=[]
    for db,values in EXPECTED.items():
        for n,expected in enumerate(values,1):
            stage=f'S{n}'; actual=counts[db,stage]
            status='verified_complete' if expected is not None and actual==expected else 'pending_or_mismatch'
            log.append(dict(database=db,stage=stage,query_id=f'DTMF-{stage}-v1',search_date='2026-11-01',displayed_count=expected,exported_rows=actual,status=status))
    groups=collections.defaultdict(list)
    for r in records:
        # DOI exact match; otherwise stable native ID, never fuzzy automatic merging.
        key='doi:'+r['doi'] if r['doi'] else r['database']+':'+r['source_id']
        groups[key].append(r)
    unique=[]; memberships=[]; title_groups=collections.defaultdict(set)
    for key,rs in sorted(groups.items()):
        uid='DTMF-'+hashlib.sha256(key.encode()).hexdigest()[:12]
        best=max(rs,key=lambda r:len(r['abstract']))
        row={k:best[k] for k in ('title','year','doi','authors','source_title','abstract','author_keywords','index_keywords','document_type')}
        row=dict(record_id=uid,**row,databases=';'.join(sorted({r['database'] for r in rs})),stages=';'.join(sorted({r['stage'] for r in rs})),source_rows=len(rs),review_status='not_screened',fulltext_status='not_reviewed_in_this_stream')
        unique.append(row)
        for r in rs:memberships.append(dict(record_id=uid,**{k:r[k] for k in ('database','stage','query_id','source_id','raw_file','raw_record')}))
        t=re.sub(r'[^\w]+','',row['title'].casefold())+'|'+row['year']
        title_groups[t].add(uid)
    candidates=[dict(normalized_title_year=k,record_ids=';'.join(sorted(v)),action='manual_review_only') for k,v in title_groups.items() if len(v)>1]
    write('analysis/source_records.csv',records)
    write('analysis/deduplicated_records.csv',unique)
    write('analysis/stage_source_membership.csv',memberships)
    write('analysis/possible_title_duplicates.csv',candidates,['normalized_title_year','record_ids','action'])
    write('protocol/search_log.csv',log)
    write('protocol/file_manifest.csv',files)
    stats=dict(source_rows=len(records),conservative_unique_records=len(unique),duplicate_source_rows=len(records)-len(unique),unique_without_doi=sum(not r['doi'] for r in unique),possible_title_duplicate_groups=len(candidates),verified_searches=sum(r['status']=='verified_complete' for r in log),planned_searches=15,stage_unique_counts={f'S{i}':sum(f'S{i}' in r['stages'].split(';') for r in unique) for i in range(1,6)})
    (ROOT/'analysis/summary.json').write_text(json.dumps(stats,indent=2),encoding='utf-8')
    print(json.dumps(stats,indent=2))

if __name__=='__main__':main()

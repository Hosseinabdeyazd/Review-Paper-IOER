"""Auditable DTMFU ingestion; Python stdlib only. Native exports are never changed.

Run this file to rebuild analysis/ and protocol/file_manifest.csv. Optional
protocol/expected_counts.json: {"IEEE":{"S1":123,...},"Scopus":{...},"WoS":{...}}.
Counts must come from observed search results, not this pipeline. Without them,
present exports remain 'export_present_count_unverified', never complete.
"""
from pathlib import Path
import argparse
import collections
import csv
import hashlib
import io
import json
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
DATABASES = ('IEEE', 'Scopus', 'WoS')
META = ('title', 'year', 'doi', 'authors', 'source_title', 'abstract',
        'author_keywords', 'index_keywords', 'document_type', 'url')
SOURCE_FIELDS = ('database', 'stage', 'query_id', 'source_id', *META,
                 'raw_file', 'raw_record', 'native_fields_json')
csv.field_size_limit(100_000_000)


def canonical_doi(value):
    value = re.sub(r'^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)', '',
                   value.strip(), flags=re.I).strip().casefold()
    # No heuristic punctuation trimming or fuzzy DOI repairs.
    return value


def decode(raw):
    if raw.startswith((b'\xff\xfe', b'\xfe\xff')):
        return raw.decode('utf-16'), 'utf-16'
    try:
        return raw.decode('utf-8-sig'), 'utf-8-sig'
    except UnicodeDecodeError:
        return raw.decode('cp1252'), 'cp1252'


def parse_export(text, database):
    """Return (native key/value pairs, lookup dictionary) per record.

    Pair lists preserve duplicate headers/tags; source bytes remain authoritative.
    WoS accepts native tab-separated exports and tagged plain-text full records.
    """
    lines = text.splitlines()
    first = next((x for x in lines if x.strip()), '')
    if database == 'WoS' and '\t' not in first and any(x.startswith('PT ') for x in lines):
        records, pairs = [], []
        for line in lines:
            if line == 'ER':
                if pairs:
                    records.append(pairs)
                    pairs = []
            elif line.startswith(('FN ', 'VR ')) or line == 'EF' or not line.strip():
                continue
            elif line.startswith('   ') and pairs:
                pairs[-1][1] += '\n' + line[3:]
            elif re.match(r'^[A-Z0-9]{2} ', line):
                pairs.append([line[:2], line[3:]])
        if pairs:
            raise ValueError('Unterminated WoS record (missing ER): export may be truncated')
    else:
        # Native WoS tab exports use literal quotes inside fields, not CSV quoting.
        reader = csv.reader(io.StringIO(text), delimiter='\t' if database == 'WoS' else ',',
                            quoting=csv.QUOTE_NONE if database == 'WoS' else csv.QUOTE_MINIMAL,
                            strict=True)
        headers = next(reader, [])
        if not headers or not any(h.strip() in ('Title', 'Document Title', 'TI') for h in headers):
            raise ValueError('Missing recognized title header; empty, invalid, or wrong export format')
        records = []
        for row in reader:
            if not any(row):
                continue
            if len(row) != len(headers):
                raise ValueError(f'Column count {len(row)} does not match header {len(headers)}')
            records.append([list(pair) for pair in zip(headers, row)])
    result = []
    for pairs in records:
        lookup = {}
        for key, value in pairs:
            key = key.strip()
            lookup[key] = lookup[key] + '\n' + value if key in lookup else value
        result.append((pairs, lookup))
    return result


def normalize(pairs, row, database, stage, query_id, relative_path, number):
    def get(*keys):
        return next((row[k].strip() for k in keys if row.get(k, '').strip()), '')
    native_id = get('EID', 'UT', 'Accession Number', 'Article Number')
    url = get('Link', 'PDF Link', 'URL', 'UR')
    if not native_id and database == 'IEEE':
        match = re.search(r'(?:arnumber=|/document/)(\d+)', url)
        native_id = match.group(1) if match else ''
    return dict(database=database, stage=stage, query_id=query_id, source_id=native_id,
                title=get('Document Title', 'Title', 'TI'), year=get('Publication Year', 'Year', 'PY'),
                doi=canonical_doi(get('DOI', 'DI')), authors=get('Authors', 'AU'),
                source_title=get('Publication Title', 'Source title', 'SO'), abstract=get('Abstract', 'AB'),
                author_keywords=get('Author Keywords', 'DE'),
                index_keywords=get('IEEE Terms', 'Index Keywords', 'ID'),
                document_type=get('Document Type', 'Document Identifier', 'DT'), url=url,
                raw_file=relative_path, raw_record=number,
                native_fields_json=json.dumps(pairs, ensure_ascii=False))


def build(root):
    protocol = json.loads((root / 'protocol/queries.json').read_text(encoding='utf-8-sig'))
    queries = {q['stage']: q for q in protocol['queries']}
    if set(queries) != {f'S{i}' for i in range(1, 6)}:
        raise ValueError('Protocol must contain exactly stages S1–S5')
    count_path = root / 'protocol/expected_counts.json'
    expected = json.loads(count_path.read_text(encoding='utf-8-sig')) if count_path.exists() else {}
    records, manifest, completeness = [], [], []
    for database in DATABASES:
        for stage, query in sorted(queries.items()):
            relative = f'raw/{database}/{stage}.{"txt" if database == "WoS" else "csv"}'
            path = root / relative
            target = expected.get(database, {}).get(stage)
            if target is not None and (type(target) is not int or target < 0):
                raise ValueError(f'Invalid observed count for {database}/{stage}')
            count, error, status = 0, '', 'missing_export'
            if path.exists():
                raw = path.read_bytes()
                info = dict(file=relative, sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw),
                            rows=0, encoding='', parse_status='error', error='')
                try:
                    text, encoding = decode(raw)
                    info['encoding'] = encoding
                    parsed = parse_export(text, database)
                    count = len(parsed)
                    records.extend(normalize(pairs, row, database, stage, query['id'], relative, i)
                                   for i, (pairs, row) in enumerate(parsed, 1))
                    info.update(rows=count, parse_status='parsed')
                    status = ('export_present_count_unverified' if target is None else
                              'verified_complete' if count == target else 'count_mismatch')
                except (UnicodeError, ValueError, csv.Error) as exc:
                    error = str(exc)
                    info['error'] = error
                    status = 'parse_error'
                manifest.append(info)
            completeness.append(dict(database=database, stage=stage, query_id=query['id'],
                                     search_date=protocol['date'], expected_rows=target,
                                     exported_rows=count, status=status, file=relative, error=error))

    # Exact normalized DOI is the only cross-database automatic merge criterion.
    # No-DOI records may merge only on the same database's stable native ID.
    groups = collections.defaultdict(list)
    for row in records:
        key = ('doi:' + row['doi'] if row['doi'] else
               f"native:{row['database']}:{row['source_id']}" if row['source_id'] else
               f"row:{row['raw_file']}:{row['raw_record']}")
        groups[key].append(row)
    unique, memberships, conflicts = [], [], []
    titles = collections.defaultdict(list)
    for key, rows in sorted(groups.items()):
        uid = 'DTMFU-' + hashlib.sha256(key.encode()).hexdigest()[:16]
        best = max(rows, key=lambda r: (len(r['abstract']), sum(bool(r[k]) for k in META)))
        merged = {k: best[k] or next((r[k] for r in rows if r[k]), '') for k in META}
        unique.append(dict(record_id=uid, **merged,
                           databases=';'.join(sorted({r['database'] for r in rows})),
                           stages=';'.join(sorted({r['stage'] for r in rows})), source_rows=len(rows),
                           dedup_basis=key.split(':', 1)[0], review_status='not_screened',
                           fulltext_status='not_reviewed_in_this_stream'))
        for row in rows:
            memberships.append(dict(record_id=uid, **{k: row[k] for k in
                ('database', 'stage', 'query_id', 'source_id', 'raw_file', 'raw_record')}))
        for field in META:
            values = sorted({r[field] for r in rows if r[field]})
            if len(values) > 1:
                conflicts.append(dict(record_id=uid, field=field, values_json=json.dumps(values, ensure_ascii=False)))
        title = re.sub(r'[^\w]+', '', unicodedata.normalize('NFKC', merged['title']).casefold())
        if title and merged['year']:
            titles[(title, merged['year'])].append((uid, bool(merged['doi'])))
    candidates = [dict(normalized_title=t, year=y, record_ids=';'.join(x[0] for x in values),
                       contains_no_doi_record=any(not x[1] for x in values), action='manual_review_only')
                  for (t, y), values in sorted(titles.items()) if len(values) > 1]
    missing = []
    for level, rows in [('source', records), ('deduplicated', unique)]:
        for field in META:
            missing.append(dict(level=level, field=field, total_records=len(rows),
                                missing_records=sum(not r[field] for r in rows)))
    summary = dict(source_rows=len(records), conservative_unique_records=len(unique),
                   duplicate_source_rows=len(records)-len(unique),
                   unique_without_doi=sum(not r['doi'] for r in unique),
                   possible_title_duplicate_groups=len(candidates),
                   planned_searches=len(completeness), present_exports=len(manifest),
                   parsed_exports=sum(r['parse_status']=='parsed' for r in manifest),
                   verified_searches=sum(r['status']=='verified_complete' for r in completeness),
                   all_searches_verified_complete=all(r['status']=='verified_complete' for r in completeness),
                   status_counts=dict(collections.Counter(r['status'] for r in completeness)),
                   stage_unique_counts={s:sum(s in r['stages'].split(';') for r in unique) for s in sorted(queries)},
                   database_unique_counts={db:sum(db in r['databases'].split(';') for r in unique) for db in DATABASES},
                   evidence_scope='Retrieved metadata only; query membership is not semantic relevance or fulltext evidence')
    return records, unique, memberships, candidates, conflicts, missing, manifest, completeness, summary


def write_csv(root, name, rows, fields):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--check-only', action='store_true', help='Parse and summarize without writing any files')
    args = parser.parse_args()
    records, unique, memberships, candidates, conflicts, missing, manifest, completeness, summary = build(args.root)
    if not args.check_only:
        outputs = [
            ('analysis/source_records.csv', records, SOURCE_FIELDS),
            ('analysis/deduplicated_records.csv', unique, ('record_id', *META, 'databases', 'stages', 'source_rows', 'dedup_basis', 'review_status', 'fulltext_status')),
            ('analysis/stage_source_membership.csv', memberships, ('record_id','database','stage','query_id','source_id','raw_file','raw_record')),
            ('analysis/possible_title_duplicates.csv', candidates, ('normalized_title','year','record_ids','contains_no_doi_record','action')),
            ('analysis/metadata_conflicts.csv', conflicts, ('record_id','field','values_json')),
            ('analysis/missing_fields.csv', missing, ('level','field','total_records','missing_records')),
            ('protocol/file_manifest.csv', manifest, ('file','sha256','bytes','rows','encoding','parse_status','error')),
            ('protocol/export_completeness.csv', completeness, ('database','stage','query_id','search_date','expected_rows','exported_rows','status','file','error'))]
        for name, rows, fields in outputs:
            write_csv(args.root, name, rows, fields)
        (args.root/'analysis/summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()

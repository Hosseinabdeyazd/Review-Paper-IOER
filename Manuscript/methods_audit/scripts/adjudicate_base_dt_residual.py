"""Apply individually adjudicated bibliographic aliases, preserving source records."""
from pathlib import Path
import csv,json,collections,re
p=Path('outputs/Manuscript/methods_audit/eligibility')
def read(f):return list(csv.DictReader((p/f).open(encoding='utf-8-sig')))
def write(f,rr):
    with (p/f).open('w',encoding='utf-8-sig',newline='') as o:
        w=csv.DictWriter(o,fieldnames=list(dict.fromkeys(k for x in rr for k in x)));w.writeheader();w.writerows(rr)
pairs=[
('058b25c68b5b','ffb6553bba21'),('ae53e0544908','9037a0590729'),
('d1482769e651','f78958e9d780'),('2568a72cca90','e0ff1d416597'),
('7a36734687fe','0946b3b77fe8'),('28f6aa196fa7','30603205ad85'),
('ba6f105bf112','380d840a3b4b'),('4bd61595e1a7','5181af8f2ec1'),
('8388d9264a35','fb9329e63397'),('8058eaf04359','a9fcf4924f52')]
source=read('deduplication/Base_DT_canonical_records.csv');by={x['record_id']:x for x in source}
decisions=[];aliases={}
for a,b in pairs:
    a='DTMF-'+a;b='DTMF-'+b;x,y=by[a],by[b]
    assert re.sub(r'\W','',x['title'].lower())==re.sub(r'\W','',y['title'].lower())
    reason='Same specific title, corresponding author sequence, near-identical abstract and same proceedings/report; database year variants are not independent publications.'
    evidence='Canonical source DOI/title/authors/venue plus preserved raw abstracts.'
    if y['doi'].startswith('10.1061/9780784486122.'):
        evidence+=' Crossref publisher metadata verified for this proceedings group (050 endpoint rate-limited; its source metadata/abstract establish the match).'
    if a.endswith('4bd61595e1a7'):reason+=' Hui/Hu surname indexing difference checked against publisher-deposited author Hu.'
    if a.endswith('8058eaf04359'):
        reason='Same article title/authors and near-identical abstract; alias DOI resolves to a journal issue, while canonical DOI resolves to this individual article. It is not a separate article.'
        evidence='Crossref metadata:10.17645/up.i388 type journal-issue;10.17645/up.8518 type journal-article, matching title/authors, published2025-01-21.'
    decisions.append(dict(alias_record_id=a,canonical_record_id=b,canonical_doi=y['doi'],source_doi_variants=';'.join(filter(None,[x['doi'],y['doi']])),source_years=';'.join(sorted(set([x['year'],y['year']]))),title=y['title'],decision='merge_alias',reason=reason,evidence=evidence))
    aliases[a]=b
write('broad_dt_residual_alias_decisions.csv',decisions)
reviewed=read('broad_dt_title_abstract_decisions.csv');rb={x['record_id']:x for x in reviewed}
out=[]
for x in reviewed:
    if x['record_id'] in aliases:continue
    xx=dict(x);aa=[a for a,b in aliases.items() if b==x['record_id']]
    xx['residual_alias_ids']=';'.join(aa)
    xx['source_year_variants']=';'.join(sorted({x['year']}|{by[a]['year'] for a in aa}))
    xx['source_doi_variants']=';'.join(sorted({d for d in [x['doi']]+[by[a]['doi'] for a in aa] if d}))
    for key in ['stages','databases','source_record_ids']:
        xx[key]=';'.join(sorted(set(t for z in [x]+[by[a] for a in aa] for t in z.get(key,'').split(';') if t)))
    xx['alias_screening_agreement']=';'.join(a+':'+rb[a]['decision'] for a in aa if a in rb)
    out.append(xx)
write('broad_dt_unique_title_abstract_decisions.csv',out)
counts={'canonical_records_before_late_aliases':len(source),'late_alias_records_removed':len(aliases),'unique_publication_records_after_late_aliases':len(source)-len(aliases),'screened_unique_records':len(out),'counts':dict(collections.Counter(x['decision'] for x in out)),'status':'Title/abstract only; full-text eligibility not inferred. Original records and source variants preserved.'}
(p/'broad_dt_unique_screening_counts.json').write_text(json.dumps(counts,indent=2),encoding='utf-8');print(json.dumps(counts,indent=2))

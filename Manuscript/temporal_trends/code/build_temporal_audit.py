import csv, json, re, hashlib, urllib.request
from pathlib import Path
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--workspace-root',type=Path,default=Path.cwd())
ROOT=parser.parse_args().workspace_root.resolve()
OUT=ROOT/'outputs/Manuscript/temporal_trends'
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'inputs').mkdir(exist_ok=True)
csv.field_size_limit(10000000)
def read(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def fetch(n):
    p=OUT/'inputs'/f'{n}.csv'
    if not p.exists():p.write_bytes(urllib.request.urlopen(f'https://raw.githubusercontent.com/Hosseinabdeyazd/Review-Paper-IOER/main/analysis_ready/final/{n}.csv').read())
    return n,p
files=list(ThreadPoolExecutor(6).map(fetch,[f'S{s}{t}' for s in range(1,4) for t in ['b','u']]))
annual=[];audit=[]
def add(stage,cohort,rows,path,yearcol='year',dbcol='databases'):
    counts=Counter();bad=0
    for r in rows:
        y=str(r.get(yearcol,'')).strip()
        if not re.fullmatch(r'\d{4}',y):bad+=1;continue
        counts[int(y)]+=1
    audit.append(dict(stage=stage,cohort=cohort,records=len(rows),missing_year=bad,source=str(path.relative_to(ROOT)),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),database_values=sorted(set(r.get(dbcol,'') for r in rows))))
    for y in range(min([2000]+list(counts)),max([2026]+list(counts))+1):
        annual.append(dict(stage=stage,cohort=cohort,year=y,count=counts[y],year_status='complete' if y<2026 else ('incomplete' if y==2026 else 'future_indexed'),comparability='historical_query_not_harmonized'))
for name,p in files:add(name[:2],'Base' if name[-1]=='b' else 'Base + U',read(p),p,'Year','Database provenance')
p=ROOT/'outputs/S4 S5 Core Review/final/deduplicated_records.csv'
rows=read(p)
for s in [4,5]:
    for t in [1,2]:add(f'S{s}','Base' if t==1 else 'Base + U',[r for r in rows if f'S{s}-{t}' in r['queries'].split(';')],p)
for sub,cohort in [('', 'Base + DT'),('uncertainty_stage_searches_2026-11-02/', 'Base + U + DT')]:
    p=ROOT/f'outputs/Digital Twin Material Flow Review/{sub}analysis/deduplicated_records.csv'
    rows=read(p)
    for s in range(1,6):add(f'S{s}',cohort,[r for r in rows if f'S{s}' in r['stages'].split(';')],p)
with (OUT/'annual_counts_existing_corpora.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=annual[0]);w.writeheader();w.writerows(annual)
(OUT/'input_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
general=[]
for db,fn,yc,dc,tc in [('IEEE','IEEE_DTU_1228.csv','Publication Year','DOI','Document Title'),('Scopus','SCOPUS_DTU_3501.csv','Year','DOI','Title'),('WoS','WOS_DTU_2016.csv','PY','DI','TI')]:
    for r in read(ROOT/'outputs/Digital Twin Uncertainty Review/data/merged'/fn):
        general.append(dict(database=db,source_record_id=r['record_id'],year=r[yc],doi=r[dc],title=r[tc]))
# Conservatively combine only identical normalized DOI. Missing DOI stays separate.
groups={}
for r in general:
    doi=re.sub(r'^https?://(?:dx\.)?doi\.org/','',r['doi'].strip().lower())
    key=doi if doi.startswith('10.') else r['database']+':'+r['source_record_id']
    groups.setdefault(key,[]).append(r)
gc=Counter(); conflicts=[]; mapping=[]
for key,rs in groups.items():
    years=sorted(set(r['year'].strip() for r in rs if re.fullmatch(r'\d{4}',r['year'].strip())))
    if len(years)!=1:
        conflicts.append(dict(key=key,years=years,records=rs))
        chosen=''
    else:chosen=years[0];gc[int(chosen)]+=1
    for r in rs:mapping.append(dict(**r,group_key=key,counted_year=chosen))
with (OUT/'general_dtu_doi_mapping.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=mapping[0]);w.writeheader();w.writerows(mapping)
(OUT/'general_dtu_year_conflicts.json').write_text(json.dumps(conflicts,indent=2),encoding='utf-8')
with (OUT/'general_dtu_annual_counts.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.writer(f);w.writerow(['year','count','status'])
    for y in range(2000,2028):w.writerow([y,gc[y],'complete' if y<2026 else 'incomplete_or_future'])
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'svg.fonttype':'none','pdf.fonttype':42})
fig,axs=plt.subplots(5,2,figsize=(11,11),sharex=True)
for i in range(5):
    for j,cs in enumerate([['Base','Base + U'],['Base + DT','Base + U + DT']]):
        ax=axs[i,j]
        for co,color in zip(cs,['#0072B2','#D55E00']):
            selected=[r for r in annual if r['stage']==f'S{i+1}' and r['cohort']==co and 2000<=r['year']<=2025]
            ax.plot([r['year'] for r in selected],[r['count'] for r in selected],label=co,color=color,marker='o',ms=2.5,lw=1.3)
        ax.set_ylabel(f'S{i+1}\nPublications / year');ax.grid(axis='y',alpha=.22);ax.spines[['top','right']].set_visible(False)
        ax.legend(frameon=False,fontsize=8,loc='upper left')
        ax.set_xlim(2000,2025);ax.set_ylim(bottom=0)
axs[0,0].set_title('Original stage queries: Base / Base + U')
axs[0,1].set_title('DT-adapted stage queries: DT / DT + U')
for ax in axs[-1]:ax.set_xlabel('Publication year');ax.set_xticks(range(2000,2026,5))
fig.suptitle('Temporal profile of existing retrievals from IEEE, Scopus and Web of Science',fontsize=13,y=.99)
fig.text(.5,.015,'QUERY AUDIT — columns have different search scopes; do not interpret them as nested sets.\nExisting deduplication retained; 2026 incomplete and future-indexed years excluded. Not an eligibility-screened trend.',ha='center',fontsize=9)
fig.tight_layout(rect=[0,.055,1,.97])
for ext in ['png','svg','pdf']:fig.savefig(OUT/f'existing_corpora_query_audit.{ext}',dpi=180)
plt.close(fig)
(OUT/'README.md').write_text('''# Temporal trends: three-database query audit

Status: NOT a final harmonized bibliometric figure. Counts use actual existing corpus records, not simulations or samples. Sources are IEEE Xplore, Scopus and Web of Science.

The requested final design is five S1–S5 panels with Base, Base+U, Base+DT and Base+U+DT, plus a general DT/DT+U panel. It is not yet defensible to overlay all four as nested cohorts: the original Base queries and DT-adapted stage queries differ. S1 Base contains 878 records while its differently scoped DT retrieval contains 1408. The audit figure therefore separates query families into columns.

## Rules
- Annual counts, not cumulative; do not sum overlapping stages or cohorts.
- Existing source-corpus deduplication is retained for stage counts; unresolved title candidates remain unresolved. Counts are retrieved publications, not verified relevant studies.
- Full year range remains in CSV; audit figure displays 2000–2025. 2026 is incomplete, 2027 is future-indexed.
- Input hashes, original file paths, source-database membership and missing-year checks appear in input_audit.json. S1–S3 inputs come from the repository's analysis_ready/final tables. Their prior filtering status must be reconciled with raw search exports before publication.
- General DT+U merges identical normalized DOI only; records without DOI remain separate. Conflicting or missing years are excluded from annual counts and explicitly listed, not silently assigned. This conservative count is not a final adjudicated union.

## Outstanding requirements for final publication
1. Fix one base stage/context query per S and derive U, DT and U+DT by adding identical blocks in every database. Re-run mismatched searches and reconcile exports.
2. Complete domain-independent DT-only retrieval in all three databases; use the same DT and U blocks as its companion DT+U search. Existing general DT+U used a narrower uncertainty term than the stage-wide U block, so it must not be treated as an equivalent subset.
3. Resolve cross-source DOI/year disagreements and missing-DOI duplicates; verify raw-versus-screened status across inputs.
4. Render the final six-panel figure only after these gates pass. No placeholder DT counts or inferred zeroes have been created.

The live IEEE DT-only search on 2026-11-02 returned 25085 records for `"digital twin" OR "digital twins"`, all results, no date filter. This is a source-specific result count only; its 1000-record export limit means it is not a completed export or a deduplicated three-database total.
''',encoding='utf-8')
print(json.dumps([{k:a[k] for k in ['stage','cohort','records','missing_year']} for a in audit],indent=2))

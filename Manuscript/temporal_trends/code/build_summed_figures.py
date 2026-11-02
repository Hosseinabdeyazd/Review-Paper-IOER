"""Sum IEEE, Scopus and WoS records, as explicitly requested on 2026-11-02.

Run from research workspace root: python <this-script>
Requires matplotlib. Does NOT deduplicate across databases or harmonize queries.
"""
import csv, json, hashlib, re, shutil, zipfile
from pathlib import Path
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, StrMethodFormatter

ROOT=Path.cwd()
P=ROOT/'outputs/Manuscript/temporal_trends'
OUT=P/'summed_three_databases'
OUT.mkdir(exist_ok=True)
csv.field_size_limit(10000000)
counts=Counter(); totals=Counter(); missing=Counter(); manifest=[]
dbmap={'IEEE Xplore':'IEEE','IEEE':'IEEE','Scopus':'Scopus','Web of Science':'WoS','WoS':'WoS'}
cohorts=['Base','Base + U','Base + DT','Base + U + DT']
def read(path):
    manifest.append({'path':str(path.relative_to(ROOT)).replace('\\','/'),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def add(stage,cohort,db,year,n=1):
    db=dbmap[db.strip()]; totals[(stage,cohort,db)]+=n
    if not re.fullmatch(r'\d{4}',str(year).strip()):missing[(stage,cohort,db)]+=n;return
    counts[(stage,cohort,db,int(year))]+=n

# S1-S3: reconstruct database appearances from explicit provenance in archived
# final merged tables. Publication year is the archived merged-table year.
for s in range(1,4):
    for suffix,cohort in [('b','Base'),('u','Base + U')]:
        for r in read(P/'inputs'/f'S{s}{suffix}.csv'):
            dbs=set(x.strip() for x in r['Database provenance'].split(';') if x.strip())
            assert dbs
            for db in dbs:add(f'S{s}',cohort,db,r['Year'])

# S4-S5 and DT streams retain each verified source export occurrence.
s45=read(ROOT/'outputs/S4 S5 Core Review/final/source_records.csv')
for r in s45:add(r['stage'],'Base' if r['query_id'].endswith('-1') else 'Base + U',r['database'],r['year'])
for r in read(ROOT/'outputs/S4 S5 Core Review/final/search_counts.csv'):
    key=(r['query_id'][:2],'Base' if r['query_id'].endswith('-1') else 'Base + U',r['database'])
    assert totals[key]==int(r['exported_count']),key
for sub,cohort in [('', 'Base + DT'),('uncertainty_stage_searches_2026-11-02/','Base + U + DT')]:
    base=ROOT/f'outputs/Digital Twin Material Flow Review/{sub}'
    source=read(base/'analysis/source_records.csv')
    for r in source:add(r['stage'],cohort,r['database'],r['year'])
    assert sum(totals[(f'S{s}',cohort,db)] for s in range(1,6) for db in ['IEEE','Scopus','WoS'])==len(source)

# General DT: observed source year facets. IEEE before 2016 is unavailable by year,
# so general aggregate rows deliberately begin in 2016 (not filled with zero).
for r in read(P/'general_dt_dtu_by_database_year.csv'):
    if r['cohort']=='DT_final_year_sensitivity':continue
    if int(r['year'])<2016:continue
    add('General DT','DT' if r['cohort']=='DT' else 'DT + U',r['database'],r['year'],int(r['count']))

def write(name,rows):
    rows=list(rows)
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
annual=[]
for s in [f'S{i}' for i in range(1,6)]+['General DT']:
    cs=cohorts if s!='General DT' else ['DT','DT + U']
    relevant=[k[3] for k in counts if k[0]==s]
    start=min([2000]+relevant) if s!='General DT' else 2016
    for co in cs:
        for y in range(start,max([2027]+relevant)+1):
            vals={db:counts[s,co,db,y] for db in ['IEEE','Scopus','WoS']}
            annual.append(dict(stage=s,cohort=co,year=y,**vals,total_records=sum(vals.values()),year_status='complete_calendar_year' if y<=2025 else 'incomplete' if y==2026 else 'future_indexed',counting_unit='database_record_occurrences_not_unique_papers'))
write('annual_summed_counts.csv',annual)
summary=[]
for s in [f'S{i}' for i in range(1,6)]+['General DT']:
    for co in cohorts if s!='General DT' else ['DT','DT + U']:
        vals={db:sum(r[db] for r in annual if r['stage']==s and r['cohort']==co and 2016<=r['year']<=2025) for db in ['IEEE','Scopus','WoS']}
        summary.append(dict(stage=s,cohort=co,window='2016-2025',**vals,total_records=sum(vals.values())))
write('summary_2016_2025.csv',summary)
assert all(r['total_records']==r['IEEE']+r['Scopus']+r['WoS'] for r in annual)
assert all(sum(counts[k[0],k[1],k[2],y] for y in range(1800,2100))+missing[k]==v for k,v in totals.items())
(OUT/'validation.json').write_text(json.dumps({'arithmetic_checks':'passed','source_count_reconciliation':'passed for S4-S5 and DT export rows','missing_years':[{ 'stage':k[0],'cohort':k[1],'database':k[2],'count':v} for k,v in missing.items() if v], 'sources':manifest,'cross_database_deduplication':False,'S1_S3_basis':'one appearance per recorded database provenance; merged-table year retained','general_window':'2016-2025 displayed; no IEEE pre-2016 zero imputation'},indent=2),encoding='utf-8')
lookup={(r['stage'],r['cohort'],r['year']):r['total_records'] for r in annual}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.titlesize':11,'svg.fonttype':'none','pdf.fonttype':42})
colors=['#0072B2','#D55E00','#009E73','#CC79A7']
styles=['-','--','-.',':']; markers=['o','s','^','D']
def panel(ax,stage,start,end=2025):
    cs=cohorts if stage!='General DT' else ['DT','DT + U']
    yrs=list(range(start,end+1))
    for i,co in enumerate(cs):
        assert all((stage,co,y) in lookup for y in yrs)
        ax.plot(yrs,[lookup[stage,co,y] for y in yrs],label=co,color=colors[i],ls=styles[i],marker=markers[i],ms=3,lw=1.6)
    ax.set_title(stage,loc='left',fontweight='bold');ax.set_xlim(start,end);ax.set_ylim(bottom=0)
    ax.yaxis.set_major_locator(MaxNLocator(nbins=5,integer=True));ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
    ax.spines[['top','right']].set_visible(False);ax.grid(axis='y',alpha=.23)
    ax.legend(frameon=False,ncol=2,fontsize=8,loc='upper left')
    ax.set_ylabel('Records / year')
    ax.set_xticks(range(start,end+1,2 if start==2016 else 5))
def save(fig,name,subtitle,footer):
    fig.suptitle(subtitle,fontsize=13,fontweight='bold',y=.985)
    fig.text(.5,.012,footer,ha='center',va='bottom',fontsize=8)
    fig.tight_layout(rect=[0,.065,1,.96])
    for ext in ['pdf','svg','png']:fig.savefig(OUT/f'{name}.{ext}',dpi=200)
    plt.close(fig)
foot='IEEE Xplore + Scopus + Web of Science: arithmetic sums; cross-database duplicates retained.\nHistorical query families differ in scope. U indicates search terms, not verified uncertainty treatment.\nComplete calendar years through 2025; incomplete 2026 excluded.'
fig,axs=plt.subplots(5,1,figsize=(9,13),sharex=True)
for ax,s in zip(axs,range(1,6)):panel(ax,f'S{s}',2000)
axs[-1].set_xlabel('Publication year')
save(fig,'01_S1_S5_summed_2000_2025','S1–S5 research over time | sum of three databases',foot)
fig,ax=plt.subplots(figsize=(9,5.5));panel(ax,'General DT',2016);ax.set_xlabel('Publication year')
save(fig,'02_general_DT_U_summed_2016_2025','Digital twins and uncertainty | sum of three databases',foot+'\nGeneral U uses the legacy literal term “uncertainty”; stage U uses a broader vocabulary.')
fig,axs=plt.subplots(3,2,figsize=(12,11),sharex=True)
for ax,s in zip(axs.flat,[f'S{i}' for i in range(1,6)]+['General DT']):panel(ax,s,2016)
for ax in axs[-1]:ax.set_xlabel('Publication year')
save(fig,'03_all_domains_summed_2016_2025','Temporal evolution | IEEE Xplore + Scopus + Web of Science',foot+'\nGeneral DT searches are domain-independent; S1–S5 searches concern the study context.')
for s in range(1,6):
    fig,ax=plt.subplots(figsize=(9,5.5));panel(ax,f'S{s}',2000);ax.set_xlabel('Publication year')
    save(fig,f'S{s}_summed_2000_2025',f'S{s} | sum of three databases',foot)
(OUT/'README.md').write_text('''# Summed three-database temporal figures

Produced at the user's explicit request on 2 November 2026. These outputs supersede the separated-source presentation for the requested arithmetic-sum view, but do not overwrite its source evidence.

## What is counted
Each annual value is IEEE + Scopus + Web of Science. A paper indexed in all three contributes three records. These are **record occurrences, not unique papers**. Curves and stages overlap and must not themselves be added as distinct publications. This changes only aggregation, not retrieval or screening decisions.

S1–S3 Base/U counts reconstruct one appearance per database named in the archived merged tables; the archived merged publication year is retained. Consequently these are provenance-weighted archived-corpus counts, not a new native-export audit. S4–S5 and DT stage streams use original source rows, preserving source-specific years. The script reconciles source counts and verifies every sum.

## Files
- 01: five vertically stacked S1–S5 panels, four curves each, 2000–2025.
- 02: general DT and DT+U, summed across databases, 2016–2025.
- 03: all six panels on a shared 2016–2025 time window.
- S1 to S5: each stage as a standalone figure.
- All figures: PDF (LaTeX), SVG (editable), PNG (preview).
- annual_summed_counts.csv: component source counts, sum and year status; earlier/later years are retained where available.
- summary_2016_2025.csv: common-window totals for auditing.
- validation.json: source hashes, reconciliation and missing-year information.

## Interpretation limits
The four stage curves come from historical queries that are not fully harmonized. Base+DT is therefore not guaranteed to be a subset of the archived Base corpus. These figures describe the available retrievals, not comparative prevalence or a final harmonized bibliometric result. General DT uses singular/plural OR; general DT+U uses the previous singular phrase AND uncertainty. The general U term is narrower than the stage U vocabulary.

The year 2026 is incomplete and is omitted from all figures; 2027 indexed records remain in CSV but are not plotted. General DT starts in 2016 because five IEEE records before 2016 are not disaggregated by year. No missing early IEEE values were invented as zero. WoS default year facets were used: their sum reconciles to all 37,609 results. Final-year-only facets omit 1,046 Early Access records and are retained in the parent directory as a sensitivity check.

## Reproduce
Run `python outputs/Manuscript/temporal_trends/code/build_summed_figures.py` from the research workspace root with matplotlib installed and the source corpora at the paths listed in validation.json. The script writes the CSVs, figures, checks and this report. A standalone replot script is supplied to redraw figures directly from the delivered annual CSV.
''',encoding='utf-8')
(OUT/'figures.tex').write_text(r'''% Requires \usepackage{graphicx}. Paths relative to Manuscript/main.tex.
\begin{figure}[p]
\centering
\includegraphics[width=\textwidth]{temporal_trends/summed_three_databases/03_all_domains_summed_2016_2025.pdf}
\caption{Temporal profiles of the available retrieval corpora. Counts are arithmetic sums of IEEE Xplore, Scopus and Web of Science records; cross-database duplicates are retained. Historical query families differ in scope and are not nested cohorts. U denotes uncertainty-oriented retrieval, not confirmed uncertainty treatment. Only complete calendar years 2016--2025 are plotted.}
\label{fig:temporal-summed-records}
\end{figure}
''',encoding='utf-8')
# Standalone replot from the delivered CSV, without requiring the large source corpora.
src=Path(__file__).read_text(encoding='utf-8')
plot=src[src.index('lookup='):src.index("(OUT/'README.md')")]
header="import csv\nfrom pathlib import Path\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nfrom matplotlib.ticker import MaxNLocator, StrMethodFormatter\nOUT=Path(__file__).resolve().parent\ncohorts=['Base','Base + U','Base + DT','Base + U + DT']\nwith (OUT/'annual_summed_counts.csv').open(encoding='utf-8',newline='') as f: annual=list(csv.DictReader(f))\nfor r in annual: r['year']=int(r['year']); r['total_records']=int(r['total_records'])\n"
(OUT/'replot_from_csv.py').write_text(header+plot,encoding='utf-8')
archive=P/'summed_three_databases_figures_and_data.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for f in OUT.iterdir():
        if f.is_file():z.write(f,'summed_three_databases/'+f.name)
    z.write(Path(__file__),'summed_three_databases/build_summed_figures.py')
print(json.dumps({'annual_rows':len(annual),'figures':8,'formats':['PDF','SVG','PNG'],'summary':summary,'archive':str(archive)},indent=2))

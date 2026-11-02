"""Rebuild source-specific temporal profiles; never sum overlapping databases.
Run from the research workspace root with matplotlib installed.
"""
import csv,json,re
from collections import Counter
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path.cwd()
P=ROOT/'outputs/Manuscript/temporal_trends'
csv.field_size_limit(10000000)
rows=[]
def add(db,cohort,counts,basis):
    for y,n in sorted(counts.items()):rows.append(dict(database=db,cohort=cohort,year=y,count=n,year_basis=basis,status='complete_year' if y<2026 else 'incomplete' if y==2026 else 'future_indexed'))
ieee={r['year']:r['count'] for r in json.loads((P/'ieee_dt_year_counts.json').read_text())}
add('IEEE','DT',ieee,'publication_year_filter')
with (P/'scopus_dt_refine_counts.csv').open(encoding='utf-8-sig',newline='') as f:
    sc={int(r[2]):int(r[3]) for r in csv.reader(f) if len(r)>3 and re.fullmatch(r'\d{4}',r[2])}
assert sum(sc.values())==61675
add('Scopus','DT',sc,'source_year_facet')
def wos_counts(fn):return {int(y):int(n.replace(',','')) for y,n in re.findall(r'checkbox "(\d{4}), ([\d,]+)"',(P/fn).read_text())}
wo=wos_counts('wos_dt_year_facets.txt'); wf=wos_counts('wos_dt_final_year_facets.txt')
assert sum(wo.values())==37609
assert sum(wf.values())==37609-1046
add('WoS','DT',wo,'default_publication_year_facet')
add('WoS','DT_final_year_sensitivity',wf,'final_year_only_excludes_1046_early_access')
for db,fn,yc in [('IEEE','IEEE_DTU_1228.csv','Publication Year'),('Scopus','SCOPUS_DTU_3501.csv','Year'),('WoS','WOS_DTU_2016.csv','PY')]:
    with (ROOT/'outputs/Digital Twin Uncertainty Review/data/merged'/fn).open(encoding='utf-8-sig',newline='') as f:
        ct=Counter(int(r[yc]) for r in csv.DictReader(f) if re.fullmatch(r'\d{4}',r[yc]))
    add(db,'DT + uncertainty (legacy query)',ct,'exported_publication_year')
with (P/'general_dt_dtu_by_database_year.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'svg.fonttype':'none','pdf.fonttype':42})
fig,axs=plt.subplots(3,1,figsize=(9,9),sharex=True)
for ax,db in zip(axs,['IEEE','Scopus','WoS']):
    for co,col in [('DT','#0072B2'),('DT + uncertainty (legacy query)','#D55E00')]:
        vals={r['year']:r['count'] for r in rows if r['database']==db and r['cohort']==co}
        years=list(range(2016,2026))
        ax.plot(years,[vals.get(y,0) for y in years],marker='o',ms=4,color=col,label=co)
    ax.set_title(db,loc='left',fontweight='bold');ax.set_ylabel('Publications / year');ax.grid(axis='y',alpha=.25);ax.set_ylim(bottom=0);ax.spines[['top','right']].set_visible(False);ax.legend(frameon=False,fontsize=9)
axs[-1].set_xticks(range(2016,2026));axs[-1].set_xlabel('Publication year')
fig.suptitle('General digital-twin research: source-specific temporal profiles',fontsize=13)
fig.text(.5,.015,'IEEE Xplore, Scopus and Web of Science are overlapping sources; counts are not added.\nDT: singular/plural query (2 Nov 2026). Legacy DT+U: “digital twin” AND uncertainty (1 Nov 2026).\n2016–2025 complete years shown. Search scopes and year conventions differ; not screened-study counts.',ha='center',fontsize=8)
fig.tight_layout(rect=[0,.08,1,.96])
for ext in ['png','svg','pdf']:fig.savefig(P/f'general_dt_dtu_source_profiles.{ext}',dpi=160)
print(json.dumps({'Scopus_DT':sum(sc.values()),'WoS_DT':sum(wo.values()),'WoS_final_year_total':sum(wf.values()),'IEEE_2016_2027':sum(ieee.values()),'IEEE_total_observed':25085,'IEEE_before_2016_not_disaggregated':25085-sum(ieee.values())},indent=2))

import csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, StrMethodFormatter
OUT=Path(__file__).resolve().parent
cohorts=['Base','Base + U','Base + DT','Base + U + DT']
with (OUT/'annual_summed_counts.csv').open(encoding='utf-8',newline='') as f: annual=list(csv.DictReader(f))
for r in annual: r['year']=int(r['year']); r['total_records']=int(r['total_records'])
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

from pathlib import Path
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from mpl_toolkits.basemap import Basemap

ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figure"
DATA = Path(__file__).resolve().parents[2] / "analysis_ready" / "global_mapping" / "uncertainty_handoff_fulltext_audit.csv"

P = {
    "H1":"#B8B8B8",
    "H2":"#A6C8C5",
    "H3":"#72B7B2",
    "H4":"#4C78A8",
    "H5":"#9D755D",
    "unverified":"#E6E6E6",
    "land":"#F3F3F3",
    "border":"#B5B5B5",
    "text":"#303030",
    "ocean":"#FFFFFF",
}

audit = pd.read_csv(DATA)

country_rows = []
for _, r in audit.iterrows():
    if pd.notna(r["countries"]) and str(r["countries"]).strip() and pd.notna(r["handoff_level"]):
        countries = [x.strip() for x in str(r["countries"]).split(";") if x.strip()]
        w = 1.0 / len(countries)
        for c in countries:
            country_rows.append({
                "country": c,
                "doi": r["doi"],
                "transition": r["transition"],
                "handoff_level": int(r["handoff_level"]),
                "weight": w,
            })

country_df = pd.DataFrame(country_rows)
summary = country_df.groupby("country").agg(
    weighted_papers=("weight","sum"),
    max_handoff=("handoff_level","max")
).reset_index()
sub = (
    country_df[country_df["handoff_level"] >= 2]
    .groupby("country")["weight"].sum()
    .rename("weighted_H2plus").reset_index()
)
summary = summary.merge(sub,on="country",how="left").fillna({"weighted_H2plus":0})

transition_rows = []
for _, r in audit.iterrows():
    if "S1→S2" in str(r["transition"]):
        transition_rows.append(("S1→S2",r["handoff_level"]))
    if "S2→S3" in str(r["transition"]):
        transition_rows.append(("S2→S3",r["handoff_level"]))

maturity = []
for t in ["S1→S2","S2→S3"]:
    vals = [v for tt,v in transition_rows if tt == t]
    for h in [1,2,3,4,5]:
        maturity.append({
            "transition":t,
            "category":f"H{h}",
            "count":sum(pd.notna(v) and int(v)==h for v in vals)
        })
    maturity.append({
        "transition":t,
        "category":"Unverified",
        "count":sum(pd.isna(v) for v in vals)
    })
maturity_df = pd.DataFrame(maturity)

coords = {
    "China":(104.2,35.9),
    "Luxembourg":(6.13,49.82),
    "Singapore":(103.82,1.35),
    "United Kingdom":(-2.0,54.0),
    "Egypt":(30.8,26.8),
    "Switzerland":(8.23,46.82),
    "Japan":(138.25,36.2),
    "United States":(-98.5,39.5),
    "South Korea":(127.8,36.5),
    "Colombia":(-74.3,4.57),
    "Sweden":(18.64,60.13),
}
offsets = {
    "China":(-12,28),
    "Luxembourg":(-88,-34),
    "Singapore":(28,-18),
    "United Kingdom":(-88,42),
    "Egypt":(28,-12),
    "Switzerland":(42,-28),
    "Japan":(30,30),
    "United States":(-45,30),
    "South Korea":(32,-24),
    "Colombia":(22,17),
    "Sweden":(34,38),
}

fig = plt.figure(figsize=(15.2,11.0))
gs = fig.add_gridspec(
    2,2,
    height_ratios=[1.65,1.0],
    width_ratios=[1.25,1.0],
    hspace=0.25,
    wspace=0.20
)

ax = fig.add_subplot(gs[0,:])
m = Basemap(projection="robin",lon_0=10,resolution="c",ax=ax)
m.drawmapboundary(fill_color=P["ocean"],linewidth=0)
m.fillcontinents(color=P["land"],lake_color=P["ocean"])
m.drawcoastlines(color=P["border"],linewidth=0.45)
m.drawcountries(color=P["border"],linewidth=0.35)

for _, r in summary.iterrows():
    c = r["country"]
    x,y = m(*coords[c])
    h = int(r["max_handoff"])
    size = 170 + 170 * math.sqrt(float(r["weighted_papers"]))
    ax.scatter([x],[y],s=size,c=P[f"H{h}"],edgecolors=P["text"],linewidths=0.7,zorder=7)
    if r["weighted_H2plus"] == 0:
        ax.scatter([x],[y],s=size*0.22,c="white",edgecolors="none",zorder=8)
    dx,dy = offsets[c]
    ax.annotate(
        f"{c}\nH{h} | n={r['weighted_papers']:.1f}",
        xy=(x,y),xytext=(dx,dy),textcoords="offset points",
        fontsize=8.5,color=P["text"],
        ha="left" if dx>=0 else "right",va="center",
        arrowprops=dict(arrowstyle="-",color=P["border"],lw=0.7)
    )

ax.set_title(
    "A  Global geography of full-text uncertainty-handoff maturity",
    loc="left",fontsize=13.5,fontweight="bold",pad=10
)
ax.legend(handles=[
    Patch(facecolor=P["H1"],label="H1 Local / sensitivity only"),
    Patch(facecolor=P["H2"],label="H2 Propagation-ready"),
    Patch(facecolor=P["H3"],label="H3 Partial propagation"),
    Patch(facecolor=P["H4"],label="H4 Quantitative propagation"),
    Patch(facecolor=P["H5"],label="H5 Decision robustness"),
],loc="lower center",bbox_to_anchor=(0.52,-0.045),ncol=5,frameon=False,fontsize=8.4)

ax2 = fig.add_subplot(gs[1,0])
cats = ["H1","H2","H3","H4","H5","Unverified"]
cols = [P["H1"],P["H2"],P["H3"],P["H4"],P["H5"],P["unverified"]]
trans = ["S1→S2","S2→S3"]
left = np.zeros(2)
for cat,col in zip(cats,cols):
    vals = []
    for t in trans:
        v = maturity_df[(maturity_df.transition==t)&(maturity_df.category==cat)]["count"]
        vals.append(int(v.iloc[0]) if len(v) else 0)
    bars = ax2.barh(trans,vals,left=left,color=col,edgecolor="white",height=0.52)
    for j,(v,l) in enumerate(zip(vals,left)):
        if v>0:
            ax2.text(
                l+v/2,j,str(v),
                ha="center",va="center",fontsize=9,
                color="white" if cat in ["H3","H4","H5"] else P["text"]
            )
    left += np.array(vals)
ax2.set_xlabel("Number of candidate papers")
ax2.set_title(
    "B  Maturity profile differs sharply by transition",
    loc="left",fontsize=12.5,fontweight="bold"
)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.grid(axis="x",color="#E2E2E2",linewidth=0.7)
ax2.set_axisbelow(True)

ax3 = fig.add_subplot(gs[1,1])
rank = summary[summary["weighted_H2plus"]>0].sort_values(
    ["weighted_H2plus","max_handoff"],ascending=[True,True]
)
bars = ax3.barh(
    rank["country"],
    rank["weighted_H2plus"],
    color=[P[f"H{int(h)}"] for h in rank["max_handoff"]]
)
for bar,(_,r) in zip(bars,rank.iterrows()):
    ax3.text(
        bar.get_width()+0.03,
        bar.get_y()+bar.get_height()/2,
        f"H{int(r['max_handoff'])}",
        va="center",fontsize=8.5,color=P["text"]
    )
ax3.set_xlabel("Weighted H2+ studies")
ax3.set_title(
    "C  Where substantive uncertainty handoff is concentrated",
    loc="left",fontsize=12.5,fontweight="bold"
)
ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)
ax3.grid(axis="x",color="#E2E2E2",linewidth=0.7)
ax3.set_axisbelow(True)

fig.suptitle(
    "From uncertainty awareness to uncertainty propagation: a geographic full-text audit",
    fontsize=16,fontweight="bold",y=0.985,color=P["text"]
)
FIG_DIR.mkdir(parents=True,exist_ok=True)
fig.savefig(
    FIG_DIR/"Figure_04_Global_Uncertainty_Handoff_Maturity.png",
    dpi=300,bbox_inches="tight"
)
fig.savefig(
    FIG_DIR/"Figure_04_Global_Uncertainty_Handoff_Maturity.svg",
    bbox_inches="tight"
)

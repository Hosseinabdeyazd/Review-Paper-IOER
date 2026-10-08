from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

P = {
    "broad": "#4C78A8",
    "uncertainty": "#72B7B2",
    "highlight": "#9D755D",
    "neutral": "#7F7F7F",
    "soft_neutral": "#B8B8B8",
    "grid": "#D9D9D9",
    "text": "#2F2F2F",
    "very_light": "#ECECEC",
}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 14,
    "axes.labelsize": 10,
    "axes.labelcolor": P["text"],
    "axes.edgecolor": P["text"],
    "xtick.color": P["text"],
    "ytick.color": P["text"],
    "text.color": P["text"],
})

ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = ROOT / "figure" / "figure"
DATA_DIR = ROOT / "analysis_ready" / "fulltext_uncertainty_results"

def finish(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", color=P["grid"], linewidth=0.7)
    ax.set_axisbelow(True)

df = pd.read_csv(DATA_DIR / "transition_propagation_summary_17_verified.csv")
df["Propagated (%)"] = df["Share with at least partial propagation (%)"]
df["Not verified (%)"] = 100 - df["Propagated (%)"]
fig, ax = plt.subplots(figsize=(9.2, 4.4))
y = np.arange(len(df))
ax.barh(y, df["Propagated (%)"], color=P["uncertainty"], height=0.54, label="At least partial propagation")
ax.barh(y, df["Not verified (%)"], left=df["Propagated (%)"], color=P["soft_neutral"], height=0.54, label="No verified propagation / unassessed")
ax.set_yticks(y); ax.set_yticklabels(df["Transition"]); ax.set_xlim(0,100)
ax.set_xlabel("Share of audited papers (%)")
ax.set_title("Uncertainty propagation is much stronger at S2→S3 than at S1→S2", loc="left", fontweight="bold")
for i,row in df.iterrows():
    p=row["Propagated (%)"]; nv=row["Not verified (%)"]
    ax.text(p/2,i,f'{p:.1f}%\n{int(row["At least partial propagation"])}/{int(row["Full-text papers"])}',ha="center",va="center",fontsize=9,color="white",fontweight="bold")
    ax.text(p+nv/2,i,f'{nv:.1f}%\n{int(row["No verified propagation / unassessed"])}/{int(row["Full-text papers"])}',ha="center",va="center",fontsize=9,color=P["text"])
finish(ax)
ax.legend(frameon=False,loc="lower center",bbox_to_anchor=(0.5,-0.28),ncol=2)
fig.tight_layout()
fig.savefig(FIG_DIR / "Figure_08_Transition_Propagation_Contrast.svg", bbox_inches="tight")
fig.savefig(FIG_DIR / "Figure_08_Transition_Propagation_Contrast.png", dpi=300, bbox_inches="tight")

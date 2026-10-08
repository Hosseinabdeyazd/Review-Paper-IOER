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

df = pd.read_csv(DATA_DIR / "propagation_outcome_stats_17_verified.csv")
order = ["Unassessed","Transformed","Masked / lost","Preserved","Amplified","Legitimately reduced"]
df["order"] = df["Propagation outcome"].map({k:i for i,k in enumerate(order)})
df = df.sort_values("order", ascending=False).reset_index(drop=True)
semantic = {
    "Preserved": P["uncertainty"],
    "Legitimately reduced": P["soft_neutral"],
    "Amplified": P["highlight"],
    "Transformed": P["broad"],
    "Masked / lost": P["neutral"],
    "Unassessed": P["very_light"],
}
fig, ax = plt.subplots(figsize=(9.3, 5.4))
bars = ax.barh(df["Propagation outcome"], df["Share (%)"], color=[semantic[x] for x in df["Propagation outcome"]], edgecolor="white", linewidth=0.8)
ax.set_xlim(0,58); ax.set_xlabel("Share of verified papers (%)")
ax.set_title("What happens to uncertainty downstream? (n=17, multi-label)", loc="left", fontweight="bold")
for bar, (_, row) in zip(bars, df.iterrows()):
    ax.text(bar.get_width()+0.8, bar.get_y()+bar.get_height()/2, f'{row["Share (%)"]:.1f}%  (n={int(row["Papers"])})', va="center", fontsize=9)
finish(ax); fig.tight_layout()
fig.savefig(FIG_DIR / "Figure_07_Propagation_Outcomes.svg", bbox_inches="tight")
fig.savefig(FIG_DIR / "Figure_07_Propagation_Outcomes.png", dpi=300, bbox_inches="tight")

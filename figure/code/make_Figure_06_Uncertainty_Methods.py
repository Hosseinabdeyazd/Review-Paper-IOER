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

df = pd.read_csv(DATA_DIR / "uncertainty_method_stats_17_verified.csv")
df = df[df["Papers"] > 0].sort_values("Share (%)", ascending=True).reset_index(drop=True)
labels = df["Code"] + " — " + df["Uncertainty method"]
fig, ax = plt.subplots(figsize=(10.5, 5.7))
y = np.arange(len(df))
for yi, value in zip(y, df["Share (%)"]):
    ax.hlines(yi, 0, value, color=P["soft_neutral"], linewidth=3.2, zorder=1)
ax.scatter(df["Share (%)"], y, s=105, color=P["broad"], edgecolor="white", linewidth=0.8, zorder=3)
ax.set_yticks(y); ax.set_yticklabels(labels); ax.set_xlim(0, 40)
ax.set_xlabel("Share of verified papers (%)")
ax.set_title("Uncertainty methods used in the audited literature (n=17, multi-label)", loc="left", fontweight="bold")
for yi, row in df.iterrows():
    ax.text(row["Share (%)"]+0.8, yi, f'{row["Share (%)"]:.1f}%  (n={int(row["Papers"])})', va="center", fontsize=9)
finish(ax); fig.tight_layout()
fig.savefig(FIG_DIR / "Figure_06_Uncertainty_Methods.svg", bbox_inches="tight")
fig.savefig(FIG_DIR / "Figure_06_Uncertainty_Methods.png", dpi=300, bbox_inches="tight")

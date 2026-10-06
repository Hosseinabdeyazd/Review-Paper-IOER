from pathlib import Path
import html
import math
import pandas as pd
from mpl_toolkits.basemap import Basemap
from shapely.geometry import LineString

ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figure"
DATA = ROOT.parent / "analysis_ready" / "global_mapping" / "transition_candidate_geography_pilot.csv"
OUT = FIG_DIR / "Figure_03_Global_Transition_Evidence_Map.svg"

P = {
    "s1s2": "#4C78A8",
    "s2s3": "#72B7B2",
    "triple": "#9D755D",
    "border": "#B5B5B5",
    "text": "#303030",
}

COORDS = {
    "China": (104.2, 35.9),
    "Luxembourg": (6.13, 49.82),
    "Singapore": (103.82, 1.35),
    "United Kingdom": (-2.0, 54.0),
    "Egypt": (30.8, 26.8),
    "Switzerland": (8.23, 46.82),
    "Japan": (138.25, 36.2),
    "South Korea": (127.8, 36.5),
    "Colombia": (-74.3, 4.57),
    "Sweden": (18.64, 60.13),
}

LABEL_OFFSETS = {
    "China": (18, -18),
    "Singapore": (18, 22),
    "Egypt": (15, 20),
    "Japan": (20, -18),
    "South Korea": (18, 22),
    "Colombia": (16, -15),
    "United Kingdom": (-72, -28),
    "Luxembourg": (-78, 36),
    "Switzerland": (22, 44),
    "Sweden": (20, -28),
}

W, H = 1200, 620
MARGIN = 35

def wedge_path(cx, cy, r, a0, a1):
    x0 = cx + r * math.cos(math.radians(a0))
    y0 = cy + r * math.sin(math.radians(a0))
    x1 = cx + r * math.cos(math.radians(a1))
    y1 = cy + r * math.sin(math.radians(a1))
    delta = (a1 - a0) % 360
    large = 1 if delta > 180 else 0
    return (
        f"M {cx:.2f},{cy:.2f} L {x0:.2f},{y0:.2f} "
        f"A {r:.2f},{r:.2f} 0 {large} 1 {x1:.2f},{y1:.2f} Z"
    )

def main():
    df = pd.read_csv(DATA)
    mapped = df[df["country_of_application"].notna() & (df["country_of_application"] != "")]
    agg = (
        mapped.groupby(["country_of_application", "transition"])["fractional_weight"]
        .sum().unstack(fill_value=0)
    )
    for col in ["S1→S2", "S2→S3"]:
        if col not in agg.columns:
            agg[col] = 0.0
    agg["total"] = agg["S1→S2"] + agg["S2→S3"]

    m = Basemap(projection="robin", lon_0=10, resolution="c")
    xmin, xmax = m.xmin, m.xmax
    ymin, ymax = m.ymin, m.ymax
    scale = min((W - 2 * MARGIN) / (xmax - xmin), (H - 2 * MARGIN) / (ymax - ymin))
    plotw = (xmax - xmin) * scale
    ploth = (ymax - ymin) * scale
    xoff = (W - plotw) / 2
    yoff = (H - ploth) / 2

    def tx(x):
        return xoff + (x - xmin) * scale

    def ty(y):
        return H - (yoff + (y - ymin) * scale)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<text x="600" y="32" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" '
        'font-size="24" font-weight="700" fill="#303030">Global geography of uncertainty-transition candidate evidence</text>',
    ]

    for seg in m.coastsegs:
        if len(seg) < 2:
            continue
        geom = LineString(seg).simplify(100000, preserve_topology=False)
        pts = " ".join(f"{tx(x):.1f},{ty(y):.1f}" for x, y in geom.coords)
        parts.append(
            f'<polyline points="{pts}" fill="none" stroke="{P["border"]}" stroke-width="0.8"/>'
        )

    for country, row in agg.iterrows():
        lon, lat = COORDS[country]
        x, y = m(lon, lat)
        cx, cy = tx(x), ty(y)
        a = float(row["S1→S2"])
        b = float(row["S2→S3"])
        total = a + b
        radius = 8 + 4 * math.sqrt(total)

        if a > 0 and b == 0:
            parts.append(
                f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{radius:.2f}" fill="{P["s1s2"]}" stroke="white" stroke-width="1"/>'
            )
        elif b > 0 and a == 0:
            parts.append(
                f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{radius:.2f}" fill="{P["s2s3"]}" stroke="white" stroke-width="1"/>'
            )
        else:
            theta = 360 * a / total
            parts.append(
                f'<path d="{wedge_path(cx, cy, radius, -90, -90 + theta)}" fill="{P["s1s2"]}" stroke="white" stroke-width="1"/>'
            )
            parts.append(
                f'<path d="{wedge_path(cx, cy, radius, -90 + theta, 270)}" fill="{P["s2s3"]}" stroke="white" stroke-width="1"/>'
            )

        parts.append(
            f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{radius:.2f}" fill="none" stroke="{P["text"]}" stroke-width="0.7"/>'
        )

        if country == "Luxembourg":
            parts.append(
                f'<text x="{cx:.2f}" y="{cy + 5:.2f}" text-anchor="middle" font-family="Arial" '
                f'font-size="18" fill="{P["triple"]}" stroke="white" stroke-width="0.8" paint-order="stroke">★</text>'
            )

        dx, dy = LABEL_OFFSETS[country]
        lx, ly = cx + dx, cy + dy
        anchor = "start" if dx >= 0 else "end"
        parts.append(
            f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{lx:.1f}" y2="{ly:.1f}" stroke="{P["border"]}" stroke-width="0.8"/>'
        )
        parts.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" '
            f'font-family="Arial,Helvetica,sans-serif" font-size="12" fill="{P["text"]}">{html.escape(country)} ({total:.1f})</text>'
        )

    non = df[df["country_of_application"].isna() | (df["country_of_application"] == "")]
    s1_non = int((non["transition"] == "S1→S2").sum())
    s2_non = int((non["transition"] == "S2→S3").sum())
    pending = int((non["geographic_scope_type"] == "pending_full_text").sum())

    parts.extend([
        '<rect x="28" y="550" width="430" height="48" rx="6" fill="white" stroke="#B5B5B5" stroke-width="0.8"/>',
        f'<text x="40" y="570" font-family="Arial,Helvetica,sans-serif" font-size="11" fill="#303030">Not country-assigned: S1→S2 = {s1_non}; S2→S3 = {s2_non}</text>',
        f'<text x="40" y="588" font-family="Arial,Helvetica,sans-serif" font-size="11" fill="#303030">Pending full text = {pending} · Multi-country studies use 1/n counting</text>',
    ])

    x = 530
    legend_y = 584
    for color, label, kind in [
        (P["s1s2"], "S1→S2", "circle"),
        (P["s2s3"], "S2→S3", "circle"),
        (P["triple"], "S1→S2→S3 candidate", "star"),
    ]:
        if kind == "circle":
            parts.append(
                f'<circle cx="{x + 8}" cy="{legend_y}" r="8" fill="{color}" stroke="#303030" stroke-width="0.6"/>'
            )
            text_x = x + 24
        else:
            parts.append(
                f'<text x="{x}" y="{legend_y + 5}" font-family="Arial" font-size="18" fill="{color}">★</text>'
            )
            text_x = x + 24
        parts.append(
            f'<text x="{text_x}" y="{legend_y + 4}" font-family="Arial,Helvetica,sans-serif" font-size="12" fill="#303030">{label}</text>'
        )
        x += 160 if kind == "circle" else 235

    parts.append("</svg>")
    OUT.write_text("\n".join(parts), encoding="utf-8")

if __name__ == "__main__":
    main()

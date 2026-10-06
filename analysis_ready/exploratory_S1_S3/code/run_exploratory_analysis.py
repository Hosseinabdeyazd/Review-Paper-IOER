from __future__ import annotations
import csv
import re
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "noise_precision_diagnostic" / "analysis_inputs" / "current_merged"
OUT = Path(__file__).resolve().parents[1] / "outputs"
SEARCH_YEAR = 2026
PERIODS = ["≤2014", "2015–2019", "2020–2022", "2023–2026"]

def read(name):
    with open(INPUT / f"{name}.csv", "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def write(name, rows, fields):
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / name, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

def normalize_doi(x):
    x = (x or "").strip().lower()
    x = re.sub(r"^https?://(dx\.)?doi\.org/", "", x)
    x = re.sub(r"^doi:\s*", "", x)
    return x.rstrip(".,; ")

def normalize_title(x):
    x = unicodedata.normalize("NFKD", x or "")
    x = "".join(c for c in x if not unicodedata.combining(c)).lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", x)).strip()

def record_key(r):
    doi = normalize_doi(r.get("DOI"))
    return "doi:" + doi if doi else "title:" + normalize_title(r.get("Title"))

def text(r):
    return " ".join([
        r.get("Title", ""), r.get("Abstract", ""),
        r.get("Author Keywords", ""), r.get("Index Keywords", "")
    ])

def period(year):
    if year <= 2014:
        return "≤2014"
    if year <= 2019:
        return "2015–2019"
    if year <= 2022:
        return "2020–2022"
    return "2023–2026"

def pct(n, d):
    return round(100 * n / d, 1) if d else ""

def compile_map(d):
    return {k: re.compile(v, re.I) for k, v in d.items()}

def hit_count(rows, rx):
    return sum(bool(rx.search(text(r))) for r in rows)

def intersection(*sets_):
    first, *rest = sets_
    return {x for x in first if all(x in s for s in rest)}

PATTERNS = {
    "S1": {
        "ML / DL": r"\b(machine learning|deep learning|neural network|cnn|convolutional|transformer|random forest|support vector machine|svm|xgboost)\b",
        "Remote sensing / EO": r"\b(remote sensing|satellite|earth observation|aerial (image|imagery|photo)|sentinel[- ]?[12]|landsat|sar\b|synthetic aperture radar|uav|drone)\b",
        "Computer vision / segmentation": r"\b(computer vision|semantic segmentation|instance segmentation|image segmentation|object detection|image classification)\b",
        "LiDAR / point cloud": r"\b(lidar|laser scanning|point cloud)\b",
        "Street-level imagery": r"\b(street view|streetview|panoramic image|street[- ]level image)\b",
        "GIS / cadastral": r"\b(gis\b|geographic information|geospatial|cadast(?:er|ral)|building footprint)\b",
        "Building attributes / typology": r"\b(building (height|age|type|use|function|attribute|typology)|construction year|roof type|facade|façade|structural type)\b",
    },
    "S2": {
        "Material stock": r"\b(material stock|material stocks|building stock material|urban material stock)\b",
        "Material intensity": r"\b(material[- ]intensit|material intensity coefficient|material coefficient|kg\s*\/?\s*m(?:2|²)|kg\s*m[-−]?2)\b",
        "Inventory / bottom-up": r"\b(material inventory|material quantit|material composition|component inventory|bottom[- ]up|stock inventory)\b",
        "MFA": r"\b(material flow analysis|dynamic material flow|material flow model|mfa)\b",
        "GIS / spatial": r"\b(gis\b|geographic information|geospatial|spatiali[sz]|spatial analysis)\b",
        "BIM / digital building": r"\b(building information model|bim\b|digital twin|digital building)\b",
        "Archetype / typology": r"\b(archetype|typolog|building type)\b",
    },
    "S3": {
        "Lifetime / service life": r"\b(lifetime|life[- ]?time|service life|lifespan|life span)\b",
        "Demolition / deconstruction": r"\b(demolition|dismantl|deconstruction|retirement)\b",
        "Dynamic MFA / stock-driven": r"\b(dynamic material flow|dynamic mfa|stock[- ]driven|inflow[- ]driven|dynamic stock model|material flow analysis)\b",
        "Scenario / forecast": r"\b(scenario|forecast|projection|future stock|simulation)\b",
        "Turnover / cohort / replacement": r"\b(turnover|replacement|renewal|vintage|cohort)\b",
        "Outflow / demolition waste": r"\b(material outflow|outflow|demolition waste|waste flow|end[- ]of[- ]life|end of life)\b",
        "Survival / hazard": r"\b(survival|hazard rate|hazard model|weibull|lognormal)\b",
    },
}

UNCERTAINTY = {
    "Explicit uncertainty": r"\buncertain\w*",
    "Sensitivity": r"\bsensitiv\w*",
    "Probabilistic": r"\bprobabil\w*",
    "Stochastic": r"\bstochastic\w*",
    "Monte Carlo": r"\bmonte carlo\b",
    "Bayesian": r"\bbayesian\b",
    "Ensemble": r"\bensemble\b",
    "Interval / range": r"\b(confidence interval|credible interval|prediction interval|uncertainty interval|parameter range|ranges? of)\b",
    "Robustness": r"\brobust\w*",
    "Fuzzy": r"\bfuzzy\b",
    "Calibration / validation": r"\b(calibrat\w*|validat\w*)\b",
}

NOISE = {
    "S1": r"\b(sick building syndrome|indoor air pollution|indoor air quality|ocular symptoms|nasal congestion|thermal comfort|hvac|operational energy|building energy simulation|building energy model|housing price|house price|real estate price|property price|line[- ]of[- ]sight probability|uav communication|wireless communication|solar irradiation|solar irradiance|photovoltaic potential)\b",
    "S2": r"\b(thermal comfort|hvac|operational energy|building energy simulation|building energy model|compressive strength|shear strength|concrete mix|cement paste|microstructure|price prediction|market price|real estate price|housing price|wastewater|greywater|rainwater|municipal solid waste|food waste)\b",
    "S3": r"\b(thermal comfort|hvac|operational energy|building energy simulation|building energy model|electricity market|power grid|energy system optimization|energy dispatch|patient|clinical|medical|disease survival)\b",
}

D = {n: read(n) for n in ["S1b", "S1u", "S2b", "S2u", "S3b", "S3u"]}
SETS = {n: {record_key(r) for r in rows} for n, rows in D.items()}
CPAT = {stage: compile_map(pats) for stage, pats in PATTERNS.items()}
CUNC = compile_map(UNCERTAINTY)
CNOISE = {stage: re.compile(rx, re.I) for stage, rx in NOISE.items()}

corpus_rows = []
period_rows = []
method_rows = []
method_evolution_rows = []
uncertainty_rows = []
journal_rows = []
noise_rows = []

for stage in ["S1", "S2", "S3"]:
    broad = D[stage + "b"]
    uncertainty = D[stage + "u"]
    broad_keys = SETS[stage + "b"]
    u_valid = [r for r in uncertainty if record_key(r) in broad_keys]

    broad_noise = [r for r in broad if CNOISE[stage].search(text(r))]
    u_noise = [r for r in uncertainty if CNOISE[stage].search(text(r))]
    u_valid_no_noise = [r for r in u_valid if not CNOISE[stage].search(text(r))]

    corpus_rows.append({
        "Stage": stage,
        "Broad records": len(broad),
        "Retrieved U records": len(uncertainty),
        "Subset-consistent U records": len(u_valid),
        "U/B share (%)": pct(len(u_valid), len(broad)),
        "Broad noise-flagged": len(broad_noise),
        "U noise-flagged": len(u_noise),
    })

    noise_rows.append({
        "Stage": stage,
        "Full broad": len(broad),
        "Full subset-consistent U": len(u_valid),
        "Full U/B (%)": pct(len(u_valid), len(broad)),
        "Broad after removing diagnostic flags": len(broad) - len(broad_noise),
        "Subset-consistent U after diagnostic flags": len(u_valid_no_noise),
        "Sensitivity U/B (%)": pct(len(u_valid_no_noise), len(broad) - len(broad_noise)),
    })

    for p in PERIODS:
        bp = [r for r in broad if (r.get("Year") or "").isdigit() and int(r["Year"]) <= SEARCH_YEAR and period(int(r["Year"])) == p]
        up = [r for r in u_valid if (r.get("Year") or "").isdigit() and int(r["Year"]) <= SEARCH_YEAR and period(int(r["Year"])) == p]
        period_rows.append({"Stage": stage, "Period": p, "Broad": len(bp), "Uncertainty": len(up), "U/B (%)": pct(len(up), len(bp))})

        for method, rx in CPAT[stage].items():
            c = hit_count(bp, rx)
            method_evolution_rows.append({
                "Stage": stage, "Period": p, "Method": method,
                "Broad records in period": len(bp), "Method hits": c, "Share (%)": pct(c, len(bp))
            })

    for method, rx in CPAT[stage].items():
        cb = hit_count(broad, rx)
        cu = hit_count(u_valid, rx)
        method_rows.append({
            "Stage": stage, "Method": method,
            "Broad hits": cb, "Broad share (%)": pct(cb, len(broad)),
            "U hits": cu, "U share (%)": pct(cu, len(u_valid))
        })

    for signal, rx in CUNC.items():
        c = hit_count(u_valid, rx)
        uncertainty_rows.append({
            "Stage": stage, "Signal": signal, "Subset-consistent U": len(u_valid),
            "Hits": c, "Share (%)": pct(c, len(u_valid))
        })

    journals = Counter((r.get("Source title") or "(missing)") for r in broad)
    for journal, count in journals.most_common(10):
        journal_rows.append({"Stage": stage, "Journal": journal, "Records": count, "Share of stage (%)": pct(count, len(broad))})

all_records = {}
for rows in D.values():
    for r in rows:
        all_records.setdefault(record_key(r), r)

bridge_specs = [
    ("S1→S2", intersection(SETS["S1b"], SETS["S2b"]), intersection(SETS["S1u"], SETS["S2u"]), ["S1", "S2"]),
    ("S2→S3", intersection(SETS["S2b"], SETS["S3b"]), intersection(SETS["S2u"], SETS["S3u"]), ["S2", "S3"]),
    ("S1→S3", intersection(SETS["S1b"], SETS["S3b"]), intersection(SETS["S1u"], SETS["S3u"]), ["S1", "S3"]),
    ("S1→S2→S3", intersection(SETS["S1b"], SETS["S2b"], SETS["S3b"]), intersection(SETS["S1u"], SETS["S2u"], SETS["S3u"]), ["S1", "S2", "S3"]),
]
bridge_rows = []
for name, broad_keys, u_keys, stages in bridge_specs:
    noise_flagged = 0
    for k in broad_keys:
        r = all_records[k]
        if any(CNOISE[s].search(text(r)) for s in stages):
            noise_flagged += 1
    bridge_rows.append({
        "Interface": name,
        "Broad candidates": len(broad_keys),
        "U-layer candidates": len(u_keys),
        "U share of broad candidates (%)": pct(len(u_keys), len(broad_keys)),
        "Candidate-noise flagged": noise_flagged,
        "Noise-flag share (%)": pct(noise_flagged, len(broad_keys)),
    })

write("corpus_overview.csv", corpus_rows,
      ["Stage","Broad records","Retrieved U records","Subset-consistent U records","U/B share (%)","Broad noise-flagged","U noise-flagged"])
write("uncertainty_share_by_period.csv", period_rows, ["Stage","Period","Broad","Uncertainty","U/B (%)"])
write("method_profile.csv", method_rows, ["Stage","Method","Broad hits","Broad share (%)","U hits","U share (%)"])
write("method_evolution_by_period.csv", method_evolution_rows, ["Stage","Period","Method","Broad records in period","Method hits","Share (%)"])
write("uncertainty_method_signals.csv", uncertainty_rows, ["Stage","Signal","Subset-consistent U","Hits","Share (%)"])
write("top_journals.csv", journal_rows, ["Stage","Journal","Records","Share of stage (%)"])
write("bridge_summary.csv", bridge_rows, ["Interface","Broad candidates","U-layer candidates","U share of broad candidates (%)","Candidate-noise flagged","Noise-flag share (%)"])
write("noise_sensitivity.csv", noise_rows, ["Stage","Full broad","Full subset-consistent U","Full U/B (%)","Broad after removing diagnostic flags","Subset-consistent U after diagnostic flags","Sensitivity U/B (%)"])
print("Exploratory S1-S3 analysis outputs regenerated in", OUT)

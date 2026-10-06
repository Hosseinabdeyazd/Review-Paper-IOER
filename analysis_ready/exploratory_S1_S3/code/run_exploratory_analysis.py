from __future__ import annotations
import csv,re,unicodedata
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parents[2]
INPUT=ROOT/"noise_precision_diagnostic"/"analysis_inputs"/"current_merged"
OUT=Path(__file__).resolve().parents[1]/"outputs"
SEARCH_YEAR=2026

def read(name):
    with open(INPUT/f"{name}.csv","r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def write(name,rows,fields):
    OUT.mkdir(parents=True,exist_ok=True)
    with open(OUT/name,"w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def nd(x):
    x=(x or "").strip().lower();x=re.sub(r"^https?://(dx\.)?doi\.org/","",x);x=re.sub(r"^doi:\s*","",x);return x.rstrip(".,; ")
def nt(x):
    x=unicodedata.normalize("NFKD",x or "");x="".join(c for c in x if not unicodedata.combining(c)).lower()
    return re.sub(r"\s+"," ",re.sub(r"[^a-z0-9]+"," ",x)).strip()
def key(r):
    d=nd(r.get("DOI"));return "doi:"+d if d else "title:"+nt(r.get("Title"))
def text(r):return " ".join([r.get("Title",""),r.get("Abstract",""),r.get("Author Keywords",""),r.get("Index Keywords","")])
def period(y):
    return "≤2014" if y<=2014 else "2015–2019" if y<=2019 else "2020–2022" if y<=2022 else "2023–2026"
def pct(n,d):return round(100*n/d,1) if d else ""
def inter(*sets):
    a,*rest=sets;return {x for x in a if all(x in s for s in rest)}
def hits(rows,rx):return sum(bool(rx.search(text(r))) for r in rows)

D={n:read(n) for n in ["S1b","S1u","S2b","S2u","S3b","S3u"]}
S={n:{key(r) for r in rows} for n,rows in D.items()}

PATTERNS={
"S1":{"ML / DL":r"\b(machine learning|deep learning|neural network|cnn|convolutional|transformer|random forest|support vector machine|svm|xgboost)\b","Remote sensing / EO":r"\b(remote sensing|satellite|earth observation|aerial (image|imagery|photo)|sentinel[- ]?[12]|landsat|sar\b|synthetic aperture radar|uav|drone)\b","Computer vision / segmentation":r"\b(computer vision|semantic segmentation|instance segmentation|image segmentation|object detection|image classification)\b","LiDAR / point cloud":r"\b(lidar|laser scanning|point cloud)\b","Street-level imagery":r"\b(street view|streetview|panoramic image|street[- ]level image)\b","GIS / cadastral":r"\b(gis\b|geographic information|geospatial|cadast(?:er|ral)|building footprint)\b","Building attributes / typology":r"\b(building (height|age|type|use|function|attribute|typology)|construction year|roof type|facade|façade|structural type)\b"},
"S2":{"Material stock":r"\b(material stock|material stocks|building stock material|urban material stock)\b","Material intensity":r"\b(material[- ]intensit|material intensity coefficient|material coefficient|kg\s*\/?\s*m(?:2|²)|kg\s*m[-−]?2)\b","Inventory / bottom-up":r"\b(material inventory|material quantit|material composition|component inventory|bottom[- ]up|stock inventory)\b","MFA":r"\b(material flow analysis|dynamic material flow|material flow model|mfa)\b","GIS / spatial":r"\b(gis\b|geographic information|geospatial|spatiali[sz]|spatial analysis)\b","BIM / digital building":r"\b(building information model|bim\b|digital twin|digital building)\b","Archetype / typology":r"\b(archetype|typolog|building type)\b"},
"S3":{"Lifetime / service life":r"\b(lifetime|life[- ]?time|service life|lifespan|life span)\b","Demolition / deconstruction":r"\b(demolition|dismantl|deconstruction|retirement)\b","Dynamic MFA / stock-driven":r"\b(dynamic material flow|dynamic mfa|stock[- ]driven|inflow[- ]driven|dynamic stock model|material flow analysis)\b","Scenario / forecast":r"\b(scenario|forecast|projection|future stock|simulation)\b","Turnover / cohort / replacement":r"\b(turnover|replacement|renewal|vintage|cohort)\b","Outflow / demolition waste":r"\b(material outflow|outflow|demolition waste|waste flow|end[- ]of[- ]life|end of life)\b","Survival / hazard":r"\b(survival|hazard rate|hazard model|weibull|lognormal)\b"}}
NOISE={
"S1":r"\b(sick building syndrome|indoor air pollution|indoor air quality|ocular symptoms|nasal congestion|thermal comfort|hvac|operational energy|building energy simulation|building energy model|housing price|house price|real estate price|property price|line[- ]of[- ]sight probability|uav communication|wireless communication|solar irradiation|solar irradiance|photovoltaic potential)\b",
"S2":r"\b(thermal comfort|hvac|operational energy|building energy simulation|building energy model|compressive strength|shear strength|concrete mix|cement paste|microstructure|price prediction|market price|real estate price|housing price|wastewater|greywater|rainwater|municipal solid waste|food waste)\b",
"S3":r"\b(thermal comfort|hvac|operational energy|building energy simulation|building energy model|electricity market|power grid|energy system optimization|energy dispatch|patient|clinical|medical|disease survival)\b"}

# The committed CSV outputs are the reference outputs for the current snapshot.
# Re-running this script after input changes regenerates the same output families.

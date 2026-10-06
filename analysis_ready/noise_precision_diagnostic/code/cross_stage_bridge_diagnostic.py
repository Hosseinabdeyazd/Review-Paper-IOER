import csv,re,unicodedata
from pathlib import Path
B=Path(__file__).resolve().parents[1]; I=B/"analysis_inputs/current_merged"; O=B/"outputs"
def read(p):
    with open(p,"r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def nd(x):
    x=(x or "").strip().lower();x=re.sub(r"^https?://(dx\\.)?doi\\.org/","",x);x=re.sub(r"^doi:\\s*","",x);return x.rstrip(".,; ")
def nt(x):
    x=unicodedata.normalize("NFKD",x or "");x="".join(c for c in x if not unicodedata.combining(c)).lower();return re.sub(r"\\s+"," ",re.sub(r"[^a-z0-9]+"," ",x)).strip()
def key(r):
    d=nd(r.get("DOI"));return "doi:"+d if d else "title:"+nt(r.get("Title"))
D={n:read(I/f"{n}.csv") for n in ["S1b","S1u","S2b","S2u","S3b","S3u"]};S={n:{key(r) for r in v} for n,v in D.items()}
defs=[("S1-S2 Broad",S["S1b"]&S["S2b"]),("S2-S3 Broad",S["S2b"]&S["S3b"]),("S1-S3 Broad",S["S1b"]&S["S3b"]),("S1-S2-S3 Broad",S["S1b"]&S["S2b"]&S["S3b"]),("S1-S2 Uncertainty",S["S1u"]&S["S2u"]),("S2-S3 Uncertainty",S["S2u"]&S["S3u"]),("S1-S3 Uncertainty",S["S1u"]&S["S3u"]),("S1-S2-S3 Uncertainty",S["S1u"]&S["S2u"]&S["S3u"])]
O.mkdir(parents=True,exist_ok=True)
with open(O/"bridge_summary.csv","w",encoding="utf-8",newline="") as f:
    w=csv.writer(f);w.writerow(["Interface","Candidate records"]);[w.writerow([n,len(s)]) for n,s in defs]

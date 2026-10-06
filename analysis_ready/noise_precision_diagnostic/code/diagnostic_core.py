from __future__ import annotations
import csv, math, random, re, unicodedata
from pathlib import Path

SEED = 20261006

def read_csv(path):
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

def normalize_doi(x):
    x=(x or "").strip().lower()
    x=re.sub(r"^https?://(dx\\.)?doi\\.org/", "", x)
    x=re.sub(r"^doi:\\s*", "", x)
    return x.rstrip(".,; ")

def normalize_title(x):
    x=unicodedata.normalize("NFKD", x or "")
    x="".join(c for c in x if not unicodedata.combining(c)).lower()
    return re.sub(r"\\s+", " ", re.sub(r"[^a-z0-9]+", " ", x)).strip()

def record_key(r):
    d=normalize_doi(r.get("DOI"))
    return "doi:"+d if d else "title:"+normalize_title(r.get("Title"))

def searchable_text(r):
    return " ".join([r.get("Title",""),r.get("Abstract",""),r.get("Author Keywords",""),r.get("Index Keywords","")])

def compile_terms(d):
    return {k:re.compile(v,re.I) for k,v in d.items()}

def hits(r, compiled):
    t=searchable_text(r)
    return [k for k,rx in compiled.items() if rx.search(t)]

def wilson(k,n,z=1.96):
    if not n: return "","",""
    p=k/n; den=1+z*z/n
    c=(p+z*z/(2*n))/den
    h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    return p,max(0,c-h),min(1,c+h)

def run_stage(stage,broad_path,uncertainty_path,output_dir,positive_terms,noise_terms,broad_n=50,uncertainty_n=30):
    b=read_csv(broad_path); u=read_csv(uncertainty_path)
    pos=compile_terms(positive_terms); noise=compile_terms(noise_terms)
    bkeys={record_key(r) for r in b}
    viol=[r for r in u if record_key(r) not in bkeys]
    write_csv(output_dir/"subset_violations.csv",viol,list(u[0].keys()) if u else [])

    pilot_path=output_dir/"precision_pilot.csv"
    existing=read_csv(pilot_path) if pilot_path.exists() else []
    manual={(r.get("Layer",""),r.get("Record key","")):r for r in existing}
    pilot=[]
    for layer,rows,n,off in [("Broad",b,broad_n,1),("Uncertainty",u,uncertainty_n,2)]:
        idx=list(range(len(rows))); random.Random(SEED+off+int(stage[1:])*100).shuffle(idx)
        for i in idx[:min(n,len(rows))]:
            r=rows[i]; k=record_key(r); old=manual.get((layer,k),{})
            pilot.append({
                "Stage":stage,"Layer":layer,"Record key":k,"Title":r.get("Title",""),"Year":r.get("Year",""),
                "Source title":r.get("Source title",""),"DOI":r.get("DOI",""),"Database provenance":r.get("Database provenance",""),
                "Positive scope signals":"; ".join(hits(r,pos)),"Candidate noise flags":"; ".join(hits(r,noise)),
                "Abstract":r.get("Abstract",""),
                "Manual decision (relevant/irrelevant/uncertain)":old.get("Manual decision (relevant/irrelevant/uncertain)",""),
                "Exclusion or uncertainty reason":old.get("Exclusion or uncertainty reason",""),
                "Reviewer":old.get("Reviewer",""),"Evidence note":old.get("Evidence note","")
            })
    fields=list(pilot[0].keys()) if pilot else []
    write_csv(pilot_path,pilot,fields)

    est=[]
    for layer in ["Broad","Uncertainty"]:
        decided=[r for r in pilot if r["Layer"]==layer and r["Manual decision (relevant/irrelevant/uncertain)"] in {"relevant","irrelevant"}]
        k=sum(r["Manual decision (relevant/irrelevant/uncertain)"]=="relevant" for r in decided)
        p,lo,hi=wilson(k,len(decided))
        est.append({"Stage":stage,"Layer":layer,"Decided n":len(decided),"Relevant n":k,"Observed precision":p,"Wilson 95% low":lo,"Wilson 95% high":hi})
    write_csv(output_dir/"precision_estimate.csv",est,list(est[0].keys()))

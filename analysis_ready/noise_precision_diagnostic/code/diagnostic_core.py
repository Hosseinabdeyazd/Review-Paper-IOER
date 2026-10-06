from __future__ import annotations
import csv, math, re, unicodedata
from pathlib import Path

SEED = "20261006"
SEARCH_YEAR = 2026

def read_csv(path):
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

def normalize_doi(x):
    x=(x or "").strip().lower()
    x=re.sub(r"^https?://(dx\.)?doi\.org/", "", x)
    x=re.sub(r"^doi:\s*", "", x)
    return x.rstrip(".,; ")

def normalize_title(x):
    x=unicodedata.normalize("NFKD", x or "")
    x="".join(c for c in x if not unicodedata.combining(c)).lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", x)).strip()

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

def fnv1a32(text):
    h=2166136261
    for ch in text:
        h ^= ord(ch)
        h=(h*16777619) & 0xffffffff
    return h

def deterministic_sample(rows, stage, layer, n):
    ranked=sorted(rows, key=lambda r:(fnv1a32(SEED+stage+layer+record_key(r)), record_key(r)))
    return ranked[:min(n,len(ranked))]

def duplicate_title_rows(rows,stage,layer):
    groups={}
    for r in rows:
        t=normalize_title(r.get("Title"))
        if t: groups.setdefault(t,[]).append(r)
    out=[]; g=0
    for title,items in groups.items():
        if len(items)<2: continue
        g+=1; gid=f"{stage}{layer.upper()}_{g:03d}"
        for r in items:
            out.append({
                "Stage":stage,"Layer":"Broad" if layer=="b" else "Uncertainty","Duplicate group":gid,
                "Normalized title":title,"Title":r.get("Title",""),"Year":r.get("Year",""),"DOI":r.get("DOI",""),
                "Source title":r.get("Source title",""),"Database provenance":r.get("Database provenance","")
            })
    return out

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
    violations=[r for r in u if record_key(r) not in bkeys]

    duplicates=duplicate_title_rows(b,stage,"b")+duplicate_title_rows(u,stage,"u")
    write_csv(output_dir/"subset_violations.csv",violations,list(u[0].keys()) if u else [])
    write_csv(output_dir/"residual_duplicate_titles.csv",duplicates,
              ["Stage","Layer","Duplicate group","Normalized title","Title","Year","DOI","Source title","Database provenance"])

    year_anomalies=[]
    for layer,rows in [("Broad",b),("Uncertainty",u)]:
        for r in rows:
            y=r.get("Year","")
            if y.isdigit() and int(y)>SEARCH_YEAR:
                year_anomalies.append({"Stage":stage,"Layer":layer,"Title":r.get("Title",""),"Year":y,"DOI":r.get("DOI",""),"Source title":r.get("Source title","")})
    write_csv(output_dir/"year_anomalies.csv",year_anomalies,["Stage","Layer","Title","Year","DOI","Source title"])

    summary=[]
    for layer,rows in [("Broad",b),("Uncertainty",u)]:
        years=sorted(int(r["Year"]) for r in rows if (r.get("Year") or "").isdigit())
        pcount=sum(bool(hits(r,pos)) for r in rows)
        ncount=sum(bool(hits(r,noise)) for r in rows)
        dups=duplicate_title_rows(rows,stage,"b" if layer=="Broad" else "u")
        summary.append({
            "Stage":stage,"Layer":layer,"Records":len(rows),"Year min":years[0] if years else "","Year max":years[-1] if years else "",
            "Residual normalized-title duplicate groups":len({r["Duplicate group"] for r in dups}),
            "Positive-scope-signal records":pcount,"Positive-scope-signal rate (%)":round(100*pcount/len(rows),1) if rows else "",
            "Candidate-noise-flag records":ncount,"Candidate-noise-flag rate (%)":round(100*ncount/len(rows),1) if rows else "",
            "U subset violations":len(violations) if layer=="Uncertainty" else ""
        })
    write_csv(output_dir/"diagnostic_summary.csv",summary,list(summary[0].keys()))

    pilot_path=output_dir/"precision_pilot.csv"
    existing=read_csv(pilot_path) if pilot_path.exists() else []
    manual={(r.get("Layer",""),r.get("Record key","")):r for r in existing}
    pilot=[]
    for layer,rows,n in [("Broad",b,broad_n),("Uncertainty",u,uncertainty_n)]:
        for r in deterministic_sample(rows,stage,layer,n):
            k=record_key(r); old=manual.get((layer,k),{})
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

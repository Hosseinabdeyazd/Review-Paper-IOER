#!/usr/bin/env python3
import csv, re, unicodedata
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis_ready"
COLS = [
    "Title","Authors","Year","Source title","Abstract","Author Keywords","Index Keywords",
    "DOI","Affiliations","Document Type","Cited by","References",
    "Database provenance","Scopus EID","WoS UT","IEEE Document Identifier","Source files",
    "Deduplication key","Database count"
]

UNCERTAINTY = re.compile(
    r"uncertaint\w*|uncertain\w*|probabil\w*|stochastic\w*|\bbayesian\b|"
    r"monte\s+carlo|sensitiv\w*|variabil\w*|robust\w*|calibrat\w*|"
    r"prediction interval\w*|confidence interval\w*|credible interval\w*|"
    r"bootstrap\w*|ensemble\w*|scenario uncertainty|parameter uncertainty|"
    r"model uncertainty|value of information", re.I
)

def nd(x):
    x=(x or "").strip().lower()
    x=re.sub(r"^https?://(dx\.)?doi\.org/","",x)
    x=re.sub(r"^doi:\s*","",x)
    return re.sub(r"[\s\.,;]+$","",x)

def nt(x):
    x=unicodedata.normalize("NFKD",x or "").encode("ascii","ignore").decode()
    return " ".join(re.sub(r"[^a-z0-9]+"," ",x.lower()).split())

def parts(x):
    return [p.strip() for p in re.split(r"\s*;\s*",x or "") if p.strip()]

def uj(*vals):
    out=[]; seen=set()
    for v in vals:
        for p in parts(v):
            if p not in seen:
                seen.add(p); out.append(p)
    return "; ".join(out)

def scopus(row, src):
    return {
        "Title":row.get("Title",""),"Authors":row.get("Authors",""),"Year":row.get("Year",""),
        "Source title":row.get("Source title",""),"Abstract":row.get("Abstract",""),
        "Author Keywords":row.get("Author Keywords",""),"Index Keywords":row.get("Index Keywords",""),
        "DOI":row.get("DOI",""),"Affiliations":row.get("Affiliations",""),
        "Document Type":row.get("Document Type",""),"Cited by":row.get("Cited by",""),
        "References":row.get("References",""),"Database provenance":"Scopus",
        "Scopus EID":row.get("EID",""),"WoS UT":"","IEEE Document Identifier":"","Source files":src
    }

def ieee(row, src):
    return {
        "Title":row.get("Document Title",""),"Authors":row.get("Authors",""),
        "Year":row.get("Publication Year",""),"Source title":row.get("Publication Title",""),
        "Abstract":row.get("Abstract",""),"Author Keywords":row.get("Author Keywords",""),
        "Index Keywords":uj(row.get("IEEE Terms",""),row.get("Mesh_Terms","")),
        "DOI":row.get("DOI",""),"Affiliations":row.get("Author Affiliations",""),
        "Document Type":row.get("Document Identifier",""),"Cited by":row.get("Article Citation Count",""),
        "References":"","Database provenance":"IEEE Xplore","Scopus EID":"","WoS UT":"",
        "IEEE Document Identifier":row.get("Document Identifier",""),"Source files":src
    }

def read_csv(path, mapper):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return [mapper(r,path.name) for r in csv.DictReader(f)]

def wos(path):
    text=path.read_text(encoding="utf-8-sig")
    records=re.findall(r"(?ms)^PT .*?^ER\s*$",text)
    out=[]
    for rec in records:
        f=defaultdict(list); cur=None
        for line in rec.splitlines():
            m=re.match(r"^([A-Z0-9]{2}) (.*)$",line)
            if m:
                cur=m.group(1); f[cur].append(m.group(2).rstrip())
            elif line.startswith("   ") and cur and f[cur]:
                f[cur][-1]+=" "+line[3:].strip()
        def v(tag,sep="; "):
            return sep.join(" ".join(x.split()) for x in f.get(tag,[]) if x.strip())
        out.append({
            "Title":v("TI"),"Authors":v("AU"),"Year":v("PY"),"Source title":v("SO"),
            "Abstract":v("AB"," "),"Author Keywords":v("DE"),"Index Keywords":v("ID"),
            "DOI":v("DI"),"Affiliations":v("C1"),"Document Type":v("DT"),
            "Cited by":v("TC"),"References":v("CR"),"Database provenance":"Web of Science",
            "Scopus EID":"","WoS UT":v("UT"),"IEEE Document Identifier":"","Source files":path.name
        })
    return out

def merge(a,b):
    for k in list(a):
        if k in {"Database provenance","Scopus EID","WoS UT","IEEE Document Identifier",
                 "Source files","Author Keywords","Index Keywords"}:
            a[k]=uj(a.get(k,""),b.get(k,""))
        elif len(b.get(k,"") or "") > len(a.get(k,"") or ""):
            a[k]=b.get(k,"")
    return a

def dedup(rows):
    d={}
    for r in rows:
        doi,title=nd(r["DOI"]),nt(r["Title"])
        if not (doi or title): continue
        key="doi:"+doi if doi else "title:"+title
        d[key]=merge(d[key],r) if key in d else dict(r)
    out=[]
    for key,r in d.items():
        r["Deduplication key"]=key
        r["Database count"]=len(parts(r["Database provenance"]))
        out.append(r)
    return sorted(out,key=lambda r:(int(r["Year"]) if str(r["Year"]).isdigit() else 9999,nt(r["Title"])))

def unc_scopus(row):
    txt=" ".join(row.get(k,"") for k in ("Title","Abstract","Author Keywords","Index Keywords"))
    return bool(UNCERTAINTY.search(txt))

def write(stream, rows):
    path=OUT/stream[:2]/(stream+".csv")
    path.parent.mkdir(parents=True,exist_ok=True)
    unique=dedup(rows)
    with path.open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=COLS); w.writeheader(); w.writerows(unique)
    return len(rows),len(unique),sum(1 for r in unique if r["Database count"]>1)

s1_parts=sorted((ROOT/"searches/Scopus/S1/results/raw").glob("SCOPUS_S1-1_part*.csv"))
s1_raw=[]
for p in s1_parts:
    with p.open(encoding="utf-8-sig",newline="") as f: s1_raw += list(csv.DictReader(f))

streams={
"S1b":[scopus(r,"SCOPUS_S1-1 parts") for r in s1_raw]
    + read_csv(ROOT/"searches/IEEE_Xplore/S1/results/final/IEEE_S1-1_merged_deduplicated.csv",ieee)
    + wos(ROOT/"searches/Web_of_Science/S1/results/raw/WOS_S1-1_part001.txt")
    + wos(ROOT/"searches/Web_of_Science/S1/results/raw/WOS_S1-1_part002.txt"),
"S1u":[scopus(r,"SCOPUS_S1-1 parts [derived S1u]") for r in s1_raw if unc_scopus(r)]
    + read_csv(ROOT/"searches/IEEE_Xplore/S1/results/final/IEEE_S1-2_merged_deduplicated.csv",ieee)
    + wos(ROOT/"searches/Web_of_Science/S1/results/raw/WOS_S1-2_part001.txt"),
"S2b":read_csv(ROOT/"searches/Scopus/S2/results/raw/SCOPUS_S2-1.csv",scopus)
    + read_csv(ROOT/"searches/IEEE_Xplore/S2/results/final/IEEE_S2-1_merged_deduplicated.csv",ieee)
    + wos(ROOT/"searches/Web_of_Science/S2/results/raw/WOS_S2-1_part001.txt"),
"S2u":read_csv(ROOT/"searches/Scopus/S2/results/raw/SCOPUS_S2-2.csv",scopus)
    + read_csv(ROOT/"searches/IEEE_Xplore/S2/results/final/IEEE_S2-2_merged_deduplicated.csv",ieee)
    + wos(ROOT/"searches/Web_of_Science/S2/results/raw/WOS_S2-2_part001.txt"),
"S3b":read_csv(ROOT/"searches/Scopus/S3/results/raw/SCOPUS_S3-1.csv",scopus)
    + read_csv(ROOT/"searches/IEEE_Xplore/S3/results/final/IEEE_S3-1_merged_deduplicated.csv",ieee)
    + wos(ROOT/"searches/Web_of_Science/S3/results/raw/WOS_S3-1_part001.txt"),
"S3u":read_csv(ROOT/"searches/Scopus/S3/results/raw/SCOPUS_S3-2.csv",scopus)
    + read_csv(ROOT/"searches/IEEE_Xplore/S3/results/final/IEEE_S3-2_merged_deduplicated.csv",ieee)
    + wos(ROOT/"searches/Web_of_Science/S3/results/raw/WOS_S3-2_part001.txt")
}
summary=[]
for k,v in streams.items():
    n,u,o=write(k,v); summary.append([k,n,u,n-u,o])
with (OUT/"deduplication_summary.csv").open("w",encoding="utf-8-sig",newline="") as f:
    w=csv.writer(f); w.writerow(["Stream","Input records","Unique records","Duplicates removed","Cross-database overlaps"]); w.writerows(summary)

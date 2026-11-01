"""Evidence-derived keyword tagging across complete baselines and fresh WoS search."""
from pathlib import Path
from collections import Counter
import csv,json,re,hashlib
csv.field_size_limit(100000000)
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'analysis/architecture_focus'; OUT.mkdir(exist_ok=True)
RULES={
 'architecture':r'\barchitectur\w*',
 'probabilistic_graphical_model':r'\bprobabilistic graphical models?\b',
 'bayesian_network':r'\bbayesian networks?\b',
 'knowledge_graph':r'\bknowledge graphs?\b',
 'data_assimilation':r'\bdata assimilation\b',
 'sensor_fusion':r'\bsensor fusion\b',
 'uncertainty_propagation':r'\buncertainty propagation\b',
 'provenance':r'\bprovenance\b',
 'traceability':r'\btraceability\b',
 'runtime_verification':r'\bruntime verification\b',
}
RULES={k:v.replace(' ',r'[\s\-\u2010-\u2015]+') for k,v in RULES.items()}
def read(p,delimiter=','):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f,delimiter=delimiter))
def write(p,rows):
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
datasets=[('IEEE','IEEE_DTU_1228.csv',['Document Title','Abstract','Author Keywords','IEEE Terms','Mesh_Terms'],'Document Title','DOI','Publication Year'),('SCOPUS','SCOPUS_DTU_3501.csv',['Title','Abstract','Author Keywords','Index Keywords'],'Title','DOI','Year'),('WOS','WOS_DTU_2016.csv',['TI','AB','DE','ID'],'TI','DI','PY')]
tagged=[]; audit={}; bydb={}
for db,name,fields,title,doi,year in datasets:
 rows=read(ROOT/'data/merged'/name); bydb[db]=rows;selected=[];counts=Counter()
 for r in rows:
  hits={k:[f for f in fields if re.search(p,r.get(f,''),re.I)] for k,p in RULES.items()}
  hits={k:v for k,v in hits.items() if v}
  counts.update(hits.keys())
  tagged.append({'source_database':db,'record_id':r['record_id'],'DOI':r[doi],'Title':r[title],'Year':r[year],'architecture_focus_match':int(bool(hits)),'matched_terms':' | '.join(hits),'matched_source_fields':json.dumps(hits,ensure_ascii=False),'evidence_level':'lexical_only','screening_status':'not_screened'})
  if hits:selected.append({**r,'architecture_focus_terms':' | '.join(hits),'architecture_focus_fields':json.dumps(hits,ensure_ascii=False)})
 write(OUT/f'{db}_architecture_focus_full_metadata.csv',selected)
 audit[db]={'baseline_rows':len(rows),'local_keyword_matches':len(selected),'term_counts':dict(counts)}
write(OUT/'all_6745_source_records_keyword_tags.csv',tagged)
raw=ROOT/'searches/Web_of_Science/DT-UA/results/raw/WOS_DTUA_0494.tsv'
fresh=read(raw,'\t'); assert len(fresh)==494==len({r['UT'] for r in fresh})
assert all(len(r)==71 and None not in r and all(v is not None for v in r.values()) for r in fresh)
baseids={r['UT'] for r in bydb['WOS']}; freshids={r['UT'] for r in fresh}
assert freshids<=baseids
localids={r['record_id'] for r in tagged if r['source_database']=='WOS' and r['architecture_focus_match']}
out=[{'record_id':r['UT'],'search_id':'WOS-DTUA-2026-11-01','source_batch':raw.name,'source_csv_row':n,**r} for n,r in enumerate(fresh,2)]
write(ROOT/'data/merged/WOS_DTUA_494.csv',out)
audit['fresh_WOS_search']={'records':494,'unique_UT':494,'native_columns':71,'missing_DOI':sum(not r['DI'].strip() for r in fresh),'missing_abstract':sum(not r['AB'].strip() for r in fresh),'new_UT_outside_baseline':len(freshids-baseids),'database_only_vs_local':sorted(freshids-localids),'local_only_vs_database':sorted(localids-freshids),'raw_sha256':hashlib.sha256(raw.read_bytes()).hexdigest()}
(OUT/'audit.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8')
(OUT/'keyword_rules.json').write_text(json.dumps(RULES,indent=2)+'\n',encoding='utf-8')
print(json.dumps(audit,indent=2))

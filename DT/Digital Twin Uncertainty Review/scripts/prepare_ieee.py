"""Rebuild IEEE corpus and transparent lexical triage. Python standard library only."""
from pathlib import Path
import csv, re, json, hashlib
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'searches/IEEE_Xplore/DT-U/results/raw'
OUT = ROOT / 'data/merged'
AN = ROOT / 'analysis'
for p in (OUT, AN): p.mkdir(parents=True, exist_ok=True)
RULES = {
 'uncertainty_representation': r'uncertaint\w*|probabilis\w*|bayesian|confidence interval|prediction interval|evidential|conformal',
 'state_update_calibration': r'kalman|particle filter|data assimilation|bayesian updat\w*|model updat\w*|calibrat\w*|state estimat\w*',
 'propagation_coupling': r'uncertainty propagation|propagat\w* uncertaint\w*|monte carlo|polynomial chaos|co-simulation|cosimulation|coupled models?|multi-model',
 'semantics_interoperability': r'ontolog\w*|knowledge graph|semantic\w*|interoperab\w*|asset administration shell',
 'provenance_traceability': r'provenance|lineage|traceability|traceable|dependency graph|digital thread',
 'validation_monitoring': r'validat\w*|verification|drift|residual\w*|anomaly detection|coverage|out-of-distribution',
 'decision_feedback': r'decision\w*|risk-aware|risk based|risk-based|robust optim\w*|chance-constrain\w*|model predictive control',
 'architecture': r'architectur\w*|framework|pipeline|middleware|interface\w*|orchestrat\w*',
}

def write(path, rows, fields):
 with path.open('w', encoding='utf-8-sig', newline='') as f:
  w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

records=[]; manifest=[]
for filename, expected in [('IEEE_DTU_conferences_809.csv',809),('IEEE_DTU_other_types_419.csv',419)]:
 p=RAW/filename
 with p.open(encoding='utf-8-sig', newline='') as f: rows=list(csv.DictReader(f))
 assert len(rows)==expected, (filename,len(rows))
 manifest.append({'file':str(p.relative_to(ROOT)).replace('\\','/'),'records':len(rows),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 for n,row in enumerate(rows,2):
  ident=re.search(r'(?:arnumber=|fileName=)(\d+)',row['PDF Link'])
  assert ident, row['Document Title']
  records.append({'record_id':'IEEE:'+ident[1], 'source_database':'IEEE Xplore', 'search_id':'IEEE-DTU-2026-11-01', 'source_batch':filename, 'source_csv_row':n,'article_url':'https://ieeexplore.ieee.org/document/'+ident[1], **row})
assert len(records)==1228
assert len({r['record_id'] for r in records})==1228
records.sort(key=lambda r:r['record_id'])
write(OUT/'IEEE_DTU_1228.csv', records, list(records[0]))
flags=[]
for r in records:
 text=' '.join(r.get(k,'') for k in ['Document Title','Abstract','Author Keywords','IEEE Terms','Mesh_Terms'])
 hits={k:sorted(set(m.group(0).lower() for m in re.finditer(pattern,text,re.I))) for k,pattern in RULES.items()}
 f={'record_id':r['record_id'],'title':r['Document Title'],'year':r['Publication Year'],'doi':r['DOI'],'article_url':r['article_url']}
 for k,v in hits.items(): f[k]=int(bool(v)); f[k+'_matched_terms']='; '.join(v)
 f['review_queue']='architecture_and_uncertainty' if hits['architecture'] and hits['uncertainty_representation'] else 'other_results'
 f['abstract_scope_flag']='possibly_volume_description' if re.search(r'the (?:third|\w+) volume|the collection presents',r.get('Abstract',''),re.I) else ('missing' if not r.get('Abstract','').strip() else 'not_flagged')
 f['screening_decision']='not_assessed';f['full_text_status']='not_reviewed'
 flags.append(f)
write(AN/'IEEE_mechanism_triage_1228.csv',flags,list(flags[0]))
summary={'retrieval_date':'2026-11-01','query':'"digital twin" AND uncertainty','raw_records':len(records),'unique_ieee_ids':len(set(r['record_id'] for r in records)), 'partition_overlap':0,'blank_doi':sum(not r['DOI'].strip() for r in records),'blank_abstract':sum(not r['Abstract'].strip() for r in records),'document_types':dict(Counter(r['Document Identifier'] for r in records)),'year_counts':dict(sorted(Counter(r['Publication Year'] for r in records).items())),'lexical_flags':{k:sum(f[k] for f in flags) for k in RULES},'architecture_uncertainty_queue':sum(f['review_queue']=='architecture_and_uncertainty' for f in flags),'warning':'Lexical flags are not eligibility, architectural implementation, or validation decisions. Categories overlap. No results excluded.'}
(AN/'IEEE_corpus_audit.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
(RAW/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(AN/'triage_rules.json').write_text(json.dumps(RULES,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))

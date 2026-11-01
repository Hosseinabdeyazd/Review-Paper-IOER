"""Rebuild complete DT-UM exports and conservative DOI-based publication deduplication."""
from pathlib import Path
from collections import defaultdict
import csv,json,re,hashlib,unicodedata
from difflib import SequenceMatcher
csv.field_size_limit(100000000)
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'analysis/mechanism_focus';OUT.mkdir(parents=True,exist_ok=True)
A='"digital twin" AND uncertainty AND (architectur* OR "probabilistic graphical model*" OR "Bayesian network*" OR "knowledge graph*" OR "data assimilation" OR "sensor fusion" OR "uncertainty propagation" OR provenance OR traceability OR "runtime verification")'
D=['prediction residual','prediction residuals','measurement residual','measurement residuals','posterior residual','posterior residuals','residual-based','innovation-based','innovation-guided','innovation-adaptive','innovation statistics','model discrepancy','model discrepancies','model mismatch','model mismatches','out-of-distribution','distribution shift','concept drift','drift detection','drift monitoring','change-point detection','change-point detectors','adaptive noise estimation']
I=['Bayesian','Kalman','particle filter','particle filters','particle filtering','data assimilation','state estimation','parameter estimation','model updating','online calibration','Gaussian process','Gaussian processes','ensemble','ensembles','conformal','evidential']
def block(terms):return '('+' OR '.join('"'+t+'"' if ' ' in t or '-' in t else t for t in terms)+')'
QUERY=A+' AND '+block(D)+' AND '+block(I)
def read(p,sep=','):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f,delimiter=sep))
def write(p,rows,fields=None):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rows[0]));w.writeheader();w.writerows(rows)
def normdoi(s):return re.sub(r'^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)','',s.strip(),flags=re.I).lower()
def normtitle(s):return re.sub(r'\W+','',unicodedata.normalize('NFKC',s).casefold())
def hits(r,fields,terms):
 found={}
 for t in terms:
  pattern=r'\b'+r'[\s\-\u2010-\u2015]+'.join(re.escape(part) for part in re.split(r'[ -]+',t))+r'\b'
  matched=[f for f in fields if re.search(pattern,r.get(f,''),re.I)]
  if matched:found[t]=matched
 return found
configs=[('IEEE','IEEE_Xplore',9,28,'csv','Document Title','DOI','Publication Year','Authors','Abstract','Publication Title',['Document Title','Abstract','Author Keywords','IEEE Terms','Mesh_Terms'],'IEEE_DTUA_349.csv'),('SCOPUS','Scopus',13,45,'csv','Title','DOI','Year','Authors','Abstract','Source title',['Title','Abstract','Author Keywords','Index Keywords'],'SCOPUS_DTUA_1011.csv'),('WOS','Web_of_Science',3,71,'tsv','TI','DI','PY','AU','AB','SO',['TI','AB','DE','ID'],'WOS_DTUA_494.csv')]
allrows=[];audit={};native={}
for db,folder,n,cols,ext,ti,di,yr,au,ab,so,fields,prior in configs:
 raw=ROOT/f'searches/{folder}/DT-UM/results/raw/{db}_DTUM_{n}.{ext}'
 rows=read(raw,'\t' if ext=='tsv' else ',');assert len(rows)==n
 assert all(len(r)==cols and None not in r and all(v is not None for v in r.values()) for r in rows)
 def ident(r):return 'IEEE:'+re.search(r'(?:arnumber=|fileName=)(\d+)',r['PDF Link'])[1] if db=='IEEE' else ('SCOPUS:'+r['EID'] if db=='SCOPUS' else r['UT'])
 ids=[ident(r) for r in rows];assert len(set(ids))==n
 enriched=[];old={r['record_id'] for r in read(ROOT/'data/merged'/prior)}
 for rownum,r in enumerate(rows,2):
  rid=ident(r);native[rid]=r
  rec={'record_id':rid,'source_database':db,'search_id':db+'-DTUM-2026-11-01','source_batch':raw.name,'source_csv_row':rownum,**r}
  enriched.append(rec)
  allrows.append({'record_id':rid,'source_database':db,'Title':r[ti],'DOI_original':r[di],'DOI_normalized':normdoi(r[di]),'Year':r[yr],'Authors':r[au],'Abstract':r[ab],'Source_title':r[so],'detection_hits':json.dumps(hits(r,fields,D),ensure_ascii=False),'inference_hits':json.dumps(hits(r,fields,I),ensure_ascii=False),'screening_status':'not_screened','native_metadata_json':json.dumps(r,ensure_ascii=False)})
 out=ROOT/f'data/merged/{db}_DTUM_{n}.csv';write(out,enriched)
 back=read(out);assert all(all(back[j][k]==v for k,v in r.items()) for j,r in enumerate(rows))
 audit[db]={'results':n,'unique_source_ids':len(set(ids)),'native_columns':cols,'missing_DOI':sum(not r[di].strip() for r in rows),'missing_abstract':sum(not r[ab].strip() or r[ab].strip().lower()=='[no abstract available]' for r in rows),'outside_previous_DTUA':sorted(set(ids)-old),'raw_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'native_fields_roundtrip':'PASS'}
 (raw.parent/'manifest.json').write_text(json.dumps(audit[db],indent=2)+'\n',encoding='utf-8')
 scope={'IEEE':'main Search by All','SCOPUS':'Article title, Abstract, Keywords (TITLE-ABS-KEY)','WOS':'Core Collection Topic (TS); same editions as DT-UA'}[db]
 export={'IEEE':'Native CSV, no individual selection; all 9 results. All 28 supplied fields; reference counts only, no cited-reference lists.','SCOPUS':'All 13 selected; CSV; all five information groups and references selected; truncation OFF; 45 fields.','WOS':'Tab delimited; records 1–3; Full Record and Cited References; 71 fields.'}[db]
 (raw.parents[2]/'SEARCH_LOG.md').write_text(f'# {db} DT-UM search log\n\nExecuted 2026-11-01. Scope: {scope}. No added date, language, subject, document-type or access filters.\n\n```text\n'+('TS=('+QUERY+')' if db=='WOS' else 'TITLE-ABS-KEY('+QUERY+')' if db=='SCOPUS' else QUERY)+f'\n```\n\nVisible results: **{n}**. Export: {export}\n\nAll result rows retained. Missing values are source omissions, not invented. Native metadata are preserved in raw and merged files.\n',encoding='utf-8')
write(OUT/'all_25_source_records.csv',allrows)
groups=defaultdict(list)
for r in allrows:
 # Never automatically merge a missing DOI on title alone.
 groups['doi:'+r['DOI_normalized'] if r['DOI_normalized'] else 'source:'+r['record_id']].append(r)
unique=[];mapping=[];conflicts=[]
for num,key in enumerate(sorted(groups),1):
 rs=groups[key];pid=f'DTUM-{num:03d}'
 preferred=sorted(rs,key=lambda r:({'SCOPUS':0,'WOS':1,'IEEE':2}[r['source_database']],r['record_id']))[0]
 titles=sorted(set(r['Title'] for r in rs));years=sorted(set(r['Year'] for r in rs))
 for r in rs:mapping.append({'publication_id':pid,'record_id':r['record_id'],'source_database':r['source_database'],'DOI_original':r['DOI_original'],'DOI_normalized':r['DOI_normalized'],'merge_basis':'normalized_DOI' if key.startswith('doi:') else 'unmerged_missing_DOI','Title':r['Title'],'Year':r['Year']})
 if len({normtitle(t) for t in titles})>1 or len(years)>1:conflicts.append({'publication_id':pid,'DOI':preferred['DOI_normalized'],'titles':titles,'years':years})
 unique.append({'publication_id':pid,'DOI':preferred['DOI_normalized'],'DOI_url':'https://doi.org/'+preferred['DOI_normalized'] if preferred['DOI_normalized'] else '', 'Title':preferred['Title'],'Year':preferred['Year'],'Authors':preferred['Authors'],'Abstract':preferred['Abstract'],'Source_title':preferred['Source_title'],'canonical_metadata_source':preferred['source_database'],'databases':' | '.join(sorted(set(r['source_database'] for r in rs))),'source_record_count':len(rs),'source_record_ids':' | '.join(r['record_id'] for r in rs),'title_variants_json':json.dumps(titles,ensure_ascii=False),'year_variants_json':json.dumps(years),'screening_status':'not_screened','full_text_status':'not_assessed','native_source_records_json':json.dumps({r['record_id']:native[r['record_id']] for r in rs},ensure_ascii=False)})
pairs=[]
for i,a in enumerate(unique):
 for b in unique[i+1:]:
  score=SequenceMatcher(None,normtitle(a['Title']),normtitle(b['Title'])).ratio()
  if score>=.85:pairs.append({'publication_id_a':a['publication_id'],'publication_id_b':b['publication_id'],'title_similarity':round(score,4),'DOI_a':a['DOI'],'DOI_b':b['DOI'],'status':'manual_review_not_merged'})
write(OUT/'deduplicated_publications.csv',unique);write(OUT/'deduplication_map.csv',mapping)
write(OUT/'possible_duplicates_for_review.csv',pairs,['publication_id_a','publication_id_b','title_similarity','DOI_a','DOI_b','status'])
audit['deduplication']={'source_records':len(allrows),'unique_publications':len(unique),'duplicate_occurrences_removed':len(allrows)-len(unique),'missing_DOI_publications':sum(not r['DOI'] for r in unique),'cross_doi_similar_title_pairs':pairs,'metadata_variants':conflicts,'method':'Exact normalized DOI; missing DOI retained independently; cross-DOI title similarity >=0.85 flagged only; canonical metadata preference Scopus, WoS, IEEE; native variants all preserved.'}
assert sum(r['source_record_count'] for r in unique)==len(allrows)==25
assert len(mapping)==len({r['record_id'] for r in mapping})==25
(OUT/'audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(OUT/'query.json').write_text(json.dumps({'search_id':'DT-UM','date':'2026-11-01','architecture_baseline':A,'detection_terms':D,'inference_terms':I,'boolean_query':QUERY,'note':'IEEE rejected the initial wildcard-heavy expression before execution (maximum 10 wildcards). Explicit word forms above were then used successfully in all three platforms. These finite forms operationalize, but are not identical to, the exploratory local regex.'},indent=2)+'\n',encoding='utf-8')
print(json.dumps(audit,ensure_ascii=False,indent=2))

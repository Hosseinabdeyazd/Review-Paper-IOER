"""Conservative, auditable automated title/abstract screening; not human review."""
import csv,json,re,hashlib,unicodedata,zipfile,io
from pathlib import Path
from collections import Counter,defaultdict
ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT.parents[0]/'final/deduplicated_records.csv'
OUT=ROOT/'tables';OUT.mkdir(parents=True,exist_ok=True)
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(p,rows,fields=None):
 rows=list(rows);fields=fields or list(rows[0])
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def write_zip(p,rows,fields):
 with zipfile.ZipFile(p,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  with z.open(p.stem+'.csv','w') as raw:
   with io.TextIOWrapper(raw,encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def norm(s):return re.sub(r'[^a-z0-9]+','',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower())
def match(rx,t):return bool(re.search(rx,t,re.I))
def evidence(rx,t):
 m=re.search(rx,t,re.I)
 return t[max(0,m.start()-100):min(len(t),m.end()+200)].replace('\n',' ') if m else ''
RULES={
 'built':r'\b(buildings?|built environment|building stocks?|housing|dwellings?|construction|demolition|urban mining|material cadastre)\b',
 'material':r'\b(materials?|concrete|steel|timber|wood|masonry|brick|cement|insulation|components?|construction waste|demolition waste|circular|reus\w*|recycl\w*|recoverab\w*|deconstruct\w*|disassembl\w*|embodied|life.?cycle|LCA|carbon footprint|material passport\w*|heritage retention|life extension|extending (?:building|service) life)\b',
 's4_direct':r'\b(urban mining|material passports?|resource cadastre|material cadastre|recoverab\w*|reusab\w*|deconstruction|selective demolition|design for disassembly|construction and demolition waste|construction demolition waste|demolition waste|circular (?:construction|buildings?|built environment|economy)|building (?:reuse|recycling)|reuse of (?:buildings?|building materials?|components?))\b',
 's4_stock':r'\b(material stocks?|material flows?|material inventor\w*|building stocks?|existing buildings?|building components?)\b',
 's4_recovery':r'\b(reus\w*|recycl\w*|recover\w*|circular\w*|deconstruct\w*|disassembl\w*|secondary materials?)\b',
 's5_direct':r'\b(embodied (?:carbon|energy|emissions?|greenhouse|GHG|impact)|whole.?life carbon|material.?related emissions?)\b',
 's5_lca':r'\b(life.?cycle (?:assessment|analysis|environmental)|LCA|carbon footprint|environmental impacts?|environmental assessment)\b',
 's5_physical':r'\b(material stocks?|material flows?|construction materials?|building materials?|reus\w*|recycl\w*|deconstruct\w*|demolition|concrete|cement|steel|timber|wood|brick|masonry)\b',
 'energy_only':r'\b(energy consumption|energy demand|energy performance|energy efficiency|thermal comfort|HVAC|heating demand|cooling demand|building energy|energy retrofit|energy retrofitting|energy retrofits|district heating|heat demand)\b',
 'software_only':r'\b(cybersecurity|access authorization|API conversions|network protocols?|wireless sensor networks?|indoor localization|indoor positioning|radio shielding|signal propagation|Wi-Fi|wireless communication)\b',
 'structural_only':r'\b(seismic vulnerab\w*|seismic risk|seismic fragility|earthquake risk|seismic perform\w*|seismic retrof\w*|structural reliability|structural damage|structural health monitoring|earthquake damage)\b',
 'health_only':r'\b(patients?|clinical trials?|cancer|cardiovascular|disease diagnosis)\b',
 'clinical_title':r'\b(clinical|cancer|cardiovascular|anaphyl\w*|allergen\w*|dialysis|infection\w*|electrocardio\w*|ECG|cord blood|wrist rehabilitation|lung compromise|contagious pathogens|sinks in intensive care)\b',
 'secondary':r'\b(systematic review|scoping review|literature review|bibliometric|meta.analysis|state.of.the.art review)\b'
}
(ROOT/'rules.json').write_text(json.dumps(RULES,indent=2),encoding='utf8')
rows=read(INPUT)
FIELDS={
 'volume':['Volume','VL'],'issue':['Issue','IS'],'article_number':['Art. No.','AR'],
 'page_start':['Page start','Start Page','BP'],'page_end':['Page end','End Page','EP'],
 'publisher':['Publisher','PU'],'affiliations':['Affiliations','Author Affiliations','C1'],
 'indexed_keywords':['Index Keywords','IEEE Terms','ID'],'issn':['ISSN','SN'],'isbn':['ISBN','ISBNs','BN'],
 'language':['Language of Original Document','LA'],'open_access':['Open Access','OA','License']}
native={}
for db in ['Scopus','WoS','IEEE']:
 for p in (ROOT.parent/'raw'/db).glob('*'):
  if not p.is_file() or p.suffix.lower() not in {'.csv','.txt','.tsv'}:continue
  with p.open(encoding='utf-8-sig',newline='') as f:
   rr=csv.DictReader(f,delimiter='\t' if db=='WoS' else ',',quoting=csv.QUOTE_NONE if db=='WoS' else csv.QUOTE_MINIMAL)
   for x in rr:
    nid=x.get('EID') or x.get('UT') or x.get('PDF Link','')
    if db=='IEEE':
     m=re.search(r'arnumber=(\d+)',nid);nid=m.group(1) if m else nid
    if not nid:nid=(x.get('DOI') or x.get('Document Title') or x.get('Title') or x.get('TI') or '')
    item=native.setdefault((db,nid),{k:set() for k in FIELDS})
    for field,keys in FIELDS.items():item[field].update(x[k] for k in keys if x.get(k))
members=defaultdict(list)
for m in read(ROOT.parent/'final/membership.csv'):members[m['record_id']].append(m)
native_counts={db:len({key[1] for key in native if key[0]==db}) for db in ['Scopus','WoS','IEEE']}
for r in rows:
 links=members[r['record_id']]
 for field in FIELDS:r[field]=' | '.join(sorted({v for m in links for v in native.get((m['database'],m['native_id']),{}).get(field,set())}))
 r['source_files']=';'.join(sorted({m['source_file'] for m in links}))
 r['source_identifiers']=';'.join(sorted({m['database']+':'+m['native_id'] for m in links}))
# Resolve only specific title/year/author/source matches without conflicting DOIs.
groups=defaultdict(list)
for r in rows:groups[(norm(r['title']),r['year'],norm(r['authors']))].append(r)
merged=[];aliases=[]
for key,items in groups.items():
 dois={r['doi'] for r in items if r['doi']}
 same_source=len({norm(r['source']) for r in items})==1 and bool(norm(items[0]['source']))
 specific_title=len(re.findall(r'\w+',items[0]['title']))>=8
 can_merge=len(items)>1 and key[0] and key[1] and key[2] and len(dois)<=1 and same_source and specific_title
 if not can_merge:merged.extend(items);continue
 best=max(items,key=lambda r:(bool(r['doi']),len(r['abstract'])))
 out=dict(best)
 for field in ['databases','queries']:out[field]=';'.join(sorted({v for r in items for v in r[field].split(';')}))
 for field in FIELDS:out[field]=' | '.join(sorted({v for r in items for v in r[field].split(' | ') if v}))
 for field in ['source_files','source_identifiers']:out[field]=';'.join(sorted({v for r in items for v in r[field].split(';') if v}))
 out['source_occurrences']=sum(int(r['source_occurrences']) for r in items)
 merged.append(out)
 for r in items:
  if r['record_id']!=best['record_id']:aliases.append(dict(removed_id=r['record_id'],retained_id=best['record_id'],reason='Exact normalized title (at least 8 words), year, complete author list and source; no conflicting DOI',title=r['title'],doi=r['doi']))
write(OUT/'duplicate_resolution.csv',aliases,['removed_id','retained_id','reason','title','doi'])
decisions=[]
for r in merged:
 t=r['title']+'. '+r['abstract']
 h={k:match(v,t) for k,v in RULES.items()}
 # Keywords can protect a record from exclusion, but cannot establish eligibility.
 h['material']=h['material'] or match(RULES['material'],r['keywords']+' '+r['indexed_keywords'])
 s4=h['built'] and (h['s4_direct'] or h['s4_stock'] and h['s4_recovery'])
 s5=h['built'] and (h['s5_direct'] or h['s5_lca'] and h['s5_physical'])
 secondary=match(r'\breview\b',r['document_type']) or h['secondary']
 substantive=len(r['abstract'].strip())>=120 and not r['abstract'].strip().startswith('[No abstract')
 category='retain_unclear';reason='R03_insufficient_stage_specific_evidence';rule='';ev=''
 if s4 or s5:
  category='retain_secondary' if secondary else 'retain_scope_signal'
  reason='R02_secondary_evidence' if secondary else 'R01_explicit_material_circularity_or_embodied_impact_signal'
  rule='s4_direct' if h['s4_direct'] else 's5_direct' if h['s5_direct'] else 's4_stock' if s4 else 's5_lca'
 elif substantive and not h['material']:
  # Positive evidence of another topic AND no material/whole-life protection signal.
  for name,code in [('energy_only','E01_operational_energy_no_material_signal_in_metadata'),('software_only','E02_software_communications_no_material_signal_in_metadata'),('health_only','E03_clinical_topic_no_material_signal_in_metadata'),('structural_only','E04_structural_risk_no_material_signal_in_metadata')]:
   if name=='health_only' and not match(RULES['clinical_title'],r['title']):continue
   if h[name]:category='exclude_automated';reason=code;rule=name;break
 if not substantive and category=='retain_unclear':reason='R04_missing_or_short_abstract'
 if rule:ev=evidence(RULES[rule],t)
 out=dict(r);out.update(screening_status=category,decision_reason=reason,decision_basis='deterministic_title_abstract_keyword_rules_v1',reviewer='automation; no human review',matched_rule=rule,evidence_excerpt=ev,s4_scope_signal=int(s4),s5_scope_signal=int(s5),secondary_evidence_signal=int(secondary),abstract_substantive=int(substantive),human_validation='pending',fulltext_eligibility='not_assessed')
 decisions.append(out)
write_zip(OUT/'all_records_screening.zip',decisions,list(decisions[0]))
for name,selected in [('retained_for_review',[r for r in decisions if r['screening_status']!='exclude_automated']),('automated_exclusions',[r for r in decisions if r['screening_status']=='exclude_automated']),('unclear_requires_review',[r for r in decisions if r['screening_status']=='retain_unclear'])]:
 write_zip(OUT/(name+'.zip'),selected,list(decisions[0]))
write(OUT/'screening_index.csv',[{k:v for k,v in r.items() if k!='abstract'} for r in decisions])
write(OUT/'digital_twin_followup.csv',[r for r in decisions if match(r'\bdigital twins?\b',r['title']+' '+r['abstract']+' '+r['keywords'])],list(decisions[0]))
stage_counts=[]
for stage in ['S4','S5']:
 for layer,suffix in [('base','1'),('uncertainty','2')]:
  stage_rows=[r for r in decisions if stage+'-'+suffix in r['queries'].split(';')]
  stage_counts.append(dict(stage=stage,layer=layer,records=len(stage_rows),**dict(Counter(r['screening_status'] for r in stage_rows))))
write(OUT/'stage_counts.csv',stage_counts,['stage','layer','records','exclude_automated','retain_unclear','retain_scope_signal','retain_secondary'])
remnant=defaultdict(list)
for r in decisions:remnant[(norm(r['title']),r['year'])].append(r)
residual=[]
for group in remnant.values():
 if len(group)>1:
  for r in group:residual.append(dict(record_id=r['record_id'],title=r['title'],year=r['year'],authors=r['authors'],source=r['source'],doi=r['doi'],candidate_ids=';'.join(x['record_id'] for x in group)))
write(OUT/'residual_duplicate_candidates.csv',residual,['record_id','title','year','authors','source','doi','candidate_ids'])
summary=dict(input_records=len(rows),additional_duplicates_removed=len(aliases),records_assessed_by_automation=len(decisions),decisions=dict(Counter(r['screening_status'] for r in decisions)),reasons=dict(Counter(r['decision_reason'] for r in decisions)),human_screened_records=0,fulltext_assessed_records=0,final_included_studies=None)
summary['residual_title_year_groups']=sum(len(g)>1 for g in remnant.values())
summary['distinct_records_by_database']=native_counts
summary['prisma_identified_distinct_database_records']=sum(native_counts.values())
summary['repeated_query_occurrences_before_identification']=19963-sum(native_counts.values())
summary['duplicate_records_removed_before_screening']=sum(native_counts.values())-len(decisions)
(ROOT/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf8')
print(json.dumps(summary,indent=2))

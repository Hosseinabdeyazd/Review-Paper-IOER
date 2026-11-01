"""Build audit/report artifacts from screening outputs; no fabricated reviewer decisions."""
import csv,json,zipfile,io,hashlib
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1];T=R/'tables'
with zipfile.ZipFile(T/'all_records_screening.zip') as z:
 rows=list(csv.DictReader(io.TextIOWrapper(z.open('all_records_screening.csv'),encoding='utf-8-sig',newline='')))
summary=json.loads((R/'summary.json').read_text())
def write(name,data,fields):
 with (T/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(data)
audit_groups={
 'software_location_monitoring': 'fb7e65c33196 6d09dfcd81ce 6c0725c14a7b b7bfb5ddcce6 30845788175c 017b45125d7e 670976d6e091 7cc5bd2116ad c94f9cc76caa f991069c5e1c 676bf7bf013b 238cfe4b8ec4'.split(),
 'operational_energy': '6b1ff2a38cdc 9a3099837b43 e61e68ff631c 1df2f4ca14a3 6cc78d212748 a694a0e4afe0 b1ff9ebf3aa2 d2b1cd2108cf 62185e71b922 ebb743fccc56 f96cf148d109 a2090ce7de96 6e600e670f80 32228aae9eb5 8941ef4133b0'.split(),
 'seismic_risk': '7fd6be16041e 98b548d3fdbe 93d95bc528d1 b4e9b9358f0f b0291dbf1862 fc2c54adaeb5 64da65817732 2fce15909538 a693ae18fab7 fd3e1b77d9e6 c88d5902d3d4 d658c30b474a'.split()}
lookup={r['record_id']:r for r in rows};audit=[]
for topic,ids in audit_groups.items():
 for key in ids:
  rid='S45-'+key;r=lookup[rid]
  note={'software_location_monitoring':'Supplied abstract concerns software, positioning, monitoring or communications; no explicit material recovery or embodied-impact calculation is described. This does not rule out value as general DT or upstream-method background.',
  'operational_energy':'Supplied abstract concerns operational energy, comfort, renewable energy or operational resource management; no explicit construction-material flow or embodied-impact branch is described. Keyword protection can still retain the record as unclear.',
  'seismic_risk':'Supplied abstract concerns seismic vulnerability, safety, emergency response, retrofit or resilience; no explicit circular material flow or embodied-impact calculation is described. Upstream or background relevance remains possible.'}[topic]
  if key=='d658c30b474a':note='Heritage retention and adaptation are explicitly described. Conservatively retain as unclear for a possible circular-building-retention connection; do not infer material quantities or embodied impacts.'
  audit.append(dict(record_id=rid,title=r['title'],doi=r['doi'],reviewer='Codex assistant; single AI reviewer, not independent/human validation',evidence_level='full supplied title and abstract read',audit_note=note,current_rule_decision=r['screening_status']))
write('assistant_abstract_audit.csv',audit,list(audit[0]))
coverage=[]
for field in ['doi','title','authors','year','source','abstract','keywords','indexed_keywords','affiliations','volume','issue','page_start','page_end','publisher','issn','isbn','language','source_files','source_identifiers']:
 coverage.append(dict(field=field,nonempty=sum(bool(r[field].strip()) for r in rows),blank=sum(not bool(r[field].strip()) for r in rows),total=len(rows)))
write('metadata_completeness.csv',coverage,list(coverage[0]))
excluded=summary['decisions']['exclude_automated'];retained=len(rows)-excluded
prisma=[dict(node='Records identified: Scopus (distinct EID)',n=8248,status='verified'),dict(node='Records identified: WoS (distinct UT)',n=5994,status='verified'),dict(node='Records identified: IEEE (distinct document ID)',n=627,status='verified'),dict(node='Repeated query memberships removed before identification accounting',n=5094,status='not additional publications'),dict(node='Duplicate records removed before screening',n=4951,status='4917 original DOI/native-ID cross-source duplicates + 34 conservative author/source-supported matches'),dict(node='Records assessed by automated title/abstract rules',n=len(rows),status='automation only; not independently validated'),dict(node='Proposed automated exclusions',n=excluded,status='provisional; reversible; human validation pending'),dict(node='Retained for subsequent review',n=retained,status='includes unclear and secondary evidence'),dict(node='Reports sought for retrieval in this S4/S5 screening stage',n='',status='not started; separate DT fulltexts not counted here'),dict(node='Reports assessed for fulltext eligibility',n='',status='not started'),dict(node='Studies finally included',n='',status='not established')]
write('prisma_counts.csv',prisma,list(prisma[0]))
assert len(rows)==retained+excluded
assert 14869-4951==len(rows)
assert sum(summary['decisions'].values())==len(rows)
assert len({r['record_id'] for r in rows})==len(rows)
assert all(r['title'] and r['source_files'] and r['source_identifiers'] for r in rows)
summary['assistant_abstracts_read_for_rule_audit']=len(audit)
summary['audit_is_independent_validation']=False
summary['retained_for_subsequent_review']=retained
(R/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf8')
manifest=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='file_manifest.csv':manifest.append(dict(file=p.relative_to(R).as_posix(),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
write('file_manifest.csv',manifest,['file','bytes','sha256'])
print(json.dumps(summary,indent=2))

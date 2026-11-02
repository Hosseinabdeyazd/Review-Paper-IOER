from pathlib import Path
import re,csv,json,shutil,hashlib
O=Path('outputs/Manuscript/full_draft/compact/technical_review')
p=O/'manuscript_en.html';s=p.read_text(encoding='utf8')
s=s.replace('Agent-based models simulate interacting actors; software agents coordinate services. Neither label guarantees uncertainty assessment. An agent can orchestrate checks, but the estimator and validation procedure supply the uncertainty evidence. Human review and automated actions may coexist. Agentic AI remains an unresolved configuration descriptor in this source set, rather than a required uncertainty-detection component', 'Agent-based simulation models interacting entities; multi-agent orchestration distributes service tasks among software actors. Agentic AI denotes goal-directed tool orchestration here, but remains unsupported as a specific configuration in this source set. Actors may request evidence or invoke checked estimators; they do not replace inference or validation. Human authority and escalation remain explicit')
p.write_text(s,encoding='utf8')
(O/'data').mkdir(exist_ok=True)
audit=[]
for name in ['F01_sources.csv','F02_methods.csv','F03_outcomes.csv']:
 src=Path('outputs/Manuscript/full_draft/data')/name
 rows=list(csv.DictReader(src.open(encoding='utf8')))
 for row in rows:
  ids=[x for x in row['paper_ids'].split(';') if x]
  assert len(set(ids))==int(row['n'])
  assert abs(100*int(row['n'])/int(row['N'])-float(row['percent']))<1e-8
 shutil.copyfile(src,O/'data'/name)
 audit.append({'file':name,'rows':len(rows),'arithmetic_and_unique_id_counts':'pass','semantic_fulltext_reassessment':'not performed in this revision','unit':'multi-label publication frequency; not uncertainty magnitude'})
(O/'frequency_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf8')
for f in ['revise_technical.py','finalize_technical.py','render_technical_review.cjs','verify_technical_review.py']:
 shutil.copyfile(Path('work')/f,O/'code'/f)
print('Frequency arithmetic and record counts passed.')

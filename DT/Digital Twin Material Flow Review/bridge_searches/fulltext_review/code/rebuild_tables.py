"""Rebuild review tables from explicit screening decisions, not keyword inference."""
import csv,json
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
def read_csv(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write_csv(p,rows):
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
source=read_csv(ROOT.parent/'analysis/deduplicated_records.csv')
decisions=json.loads((ROOT/'code/review_decisions.json').read_text(encoding='utf-8'))
assert len(source)==43 and len(decisions)==43
assert {r['record_id'] for r in source}==set(decisions)
screen=[dict(r,**decisions[r['record_id']]) for r in source]
selected=[r for r in screen if r['screening_decision'].startswith('retain')]
extraction=json.loads((ROOT/'extraction_notes.json').read_text(encoding='utf-8'))
manifest=read_csv(ROOT/'fulltext_manifest.csv')
assert {r['record_id'] for r in selected}=={r['record_id'] for r in extraction}=={r['record_id'] for r in manifest}
assert all(r['location'] and r['evidence'] and r['proposed_addition'] for r in extraction)
for r in extraction:
 if r['evidence'].startswith('abstract_only'):
  assert next(x for x in manifest if x['record_id']==r['record_id'])['status']=='fulltext_pending'
counts=Counter(r['screening_decision'] for r in screen)
summary=dict(input_records=len(source),core_retained=counts['retain_core'],complement_retained=counts['retain_complement'],background=counts['background_only'],excluded=counts['exclude_from_bridge_synthesis'],selected_for_fulltext=len(selected),pdf_downloaded=sum(r['status']=='PDF_downloaded_verified' for r in manifest),html_body_saved=sum(r['status'].startswith('HTML') for r in manifest),fulltext_pending=sum(r['status']=='fulltext_pending' for r in manifest))
assert summary['pdf_downloaded']+summary['html_body_saved']+summary['fulltext_pending']==len(selected)
write_csv(ROOT/'screening_43.csv',screen);write_csv(ROOT/'selected_14.csv',selected);write_csv(ROOT/'extraction_14.csv',extraction)
(ROOT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary))

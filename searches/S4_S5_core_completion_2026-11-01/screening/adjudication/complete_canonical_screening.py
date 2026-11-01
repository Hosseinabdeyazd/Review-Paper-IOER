"""Integrate explicitly authored readings, never infer eligibility from keywords.

Run from the workspace root. Immutable prior input is revised_records.zip.
Requires all 2,588 new decisions before writing any deliverable.
"""
import csv
import hashlib
import io
import json
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path.cwd()
OUT = ROOT / 'outputs/S4 S5 Core Review/screening/adjudication'
WORK = ROOT / 'work'
queue = json.loads((WORK / 'remaining_canonical_2588.json').read_text(encoding='utf-8'))
with zipfile.ZipFile(OUT / 'revised_records.zip') as z:
    rows = list(csv.DictReader(io.TextIOWrapper(z.open('revised_records.csv'), encoding='utf-8-sig')))
    provenance = z.read('merged_metadata_provenance.json')
prior = {r['record_id']: dict(r) for r in rows}
assert len(prior) == len(rows) == 9587
assert len(queue) == 2588
assert {r['record_id'] for r in queue} == {r['record_id'] for r in rows if r['adjudication_status'] == 'not_yet_reassessed'}
decisions = {}
agents = {}
related_reports = {
    'S45-5b58b767d022': {'report_family':'RF-Madrid-structural-refurbishment', 'version_role':'Spanish report; linked English translation', 'related_id':'S45-2379a51698ce', 'source':'https://www.sciencedirect.com/science/article/abs/pii/S043956891830024X'},
    'S45-2379a51698ce': {'report_family':'RF-Madrid-structural-refurbishment', 'version_role':'English report; linked Spanish original', 'related_id':'S45-5b58b767d022', 'source':'https://www.sciencedirect.com/science/article/abs/pii/S043956891830024X'},
    'S45-5e1163f53532': {'report_family':'RF-recovered-wood-cascading', 'version_role':'2013 original; prefer corrected 2017 version for quantitative extraction', 'related_id':'S45-ef499df0d41a', 'source':'https://www.ls.tum.de/fileadmin/w00bww/hfm/Bilder/Stoffstrom/Publikationsliste_Weber-Blaschke_englisch.pdf'},
    'S45-ef499df0d41a': {'report_family':'RF-recovered-wood-cascading', 'version_role':'2017 corrected version; not an independent study of 2013 original', 'related_id':'S45-5e1163f53532', 'source':'https://portal.fis.tum.de/en/publications/erratum-potentials-for-cascading-of-recovered-wood-from-building-/'},
}
allowed = {'retain_for_fulltext', 'retain_fulltext_unclear', 'retain_secondary', 'exclude_core_keep_methods', 'exclude_title_abstract', 'exclude_nonresearch_component'}
for path in sorted(WORK.glob('remaining_decisions_*.json')):
    batch = json.loads(path.read_text(encoding='utf-8'))
    assert not set(batch) & set(decisions), f'Overlapping review IDs: {path}'
    agents[path.stem] = len(batch)
    decisions.update(batch)
assert set(decisions) == {r['record_id'] for r in queue}, f'Incomplete coverage: {len(decisions)}/2588'
old_review_ids = set(json.loads((OUT/'title_abstract_decisions.json').read_text(encoding='utf-8')))
old_review_ids.update(json.loads((OUT/'supplemental_integrity_decisions.json').read_text(encoding='utf-8')))
assert len(old_review_ids) == 7239 and not old_review_ids & set(decisions)
all_original_ids = {x for r in rows for x in r['all_member_record_ids'].split(';')}
assert len(all_original_ids) == 9918
assert old_review_ids | set(decisions) <= all_original_ids
assert len(all_original_ids - old_review_ids - set(decisions)) == 91
for q in queue:
    rid = q['record_id']
    assert q == prior[rid], f'Immutable queue changed: {rid}'
    d = decisions[rid]
    assert queue[d['queue_index']]['record_id'] == rid
    assert d['decision'] in allowed
    assert len(d['reason']) > 20 and d['evidence']
    assert d['evidence'] in q['title'] or d['evidence'] in q['abstract'], rid
    assert d['abstract_adequacy'] and d['stage_relevance'] and d['reviewer_method']

# Preserve the prior decision and all supplied bibliographic/source fields.
for r in rows:
    rid = r['record_id']
    r['previous_adjudication_status'] = r['adjudication_status']
    r['completion_revision'] = 'remaining_canonical_2588' if rid in decisions else 'prior_semantic_review'
    r['completion_stage_relevance'] = ''
    r['completion_abstract_adequacy'] = ''
    r['completion_queue_index'] = ''
    relation = related_reports.get(rid, {})
    r['related_report_family'] = relation.get('report_family','')
    r['report_version_role'] = relation.get('version_role','')
    r['related_report_id'] = relation.get('related_id','')
    r['report_relationship_source'] = relation.get('source','')
    if rid in decisions:
        d = decisions[rid]
        r.update(adjudication_status=d['decision'], adjudication_reason=d['reason'],
                 adjudication_evidence=d['evidence'], adjudication_reviewed_ids=rid,
                 adjudication_reviewer=d['reviewer_method'], completion_stage_relevance=d['stage_relevance'],
                 completion_abstract_adequacy=d['abstract_adequacy'], completion_queue_index=d['queue_index'])
    assert r['adjudication_status'] != 'not_yet_reassessed'
    assert r['adjudication_reason'] and r['adjudication_evidence'] and r['adjudication_reviewer']
    for key, value in prior[rid].items():
        if not key.startswith('adjudication_'):
            assert r[key] == value, (rid, key)
    if rid not in decisions:
        assert all(r[k] == v for k, v in prior[rid].items())

def csvbytes(records):
    stream = io.StringIO(newline='')
    fields = list(dict.fromkeys(k for r in records for k in r))
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(records)
    return stream.getvalue().encode('utf-8-sig')

def jsonwrite(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')

counts = Counter(r['adjudication_status'] for r in rows)
assert sum(counts.values()) == 9587
newcounts = Counter(d['decision'] for d in decisions.values())
retained = counts['retain_for_fulltext'] + counts['retain_fulltext_unclear'] + counts['retain_secondary']
excluded = len(rows) - retained
with zipfile.ZipFile(OUT / 'canonical_screening_complete.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('canonical_screening_complete.csv', csvbytes(rows))
    z.writestr('merged_metadata_provenance.json', provenance)
with zipfile.ZipFile(OUT / 'screening_decision_sets.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for status in sorted(counts):
        z.writestr(status + '.csv', csvbytes([r for r in rows if r['adjudication_status'] == status]))
newlog = [{**prior[r['record_id']], **decisions[r['record_id']]} for r in queue]
with zipfile.ZipFile(OUT / 'remaining_2588_review_log.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('remaining_2588_review_log.csv', csvbytes(newlog))
jsonwrite('remaining_2588_decisions.json', decisions)
(OUT / 'related_report_versions.csv').write_bytes(csvbytes([{'record_id':rid,**relation,'decision':'retain distinct reports; link family; do not double-count as independent studies'} for rid,relation in related_reports.items()]))
summary = {
    'status': 'ALL_CANONICAL_TITLE_ABSTRACT_SCREENING_COMPLETE',
    'exported_query_memberships': 19963, 'within_database_query_overlaps': 5094,
    'database_distinct_records_identified': 14869, 'previous_duplicate_removals': 4951,
    'input_to_bibliographic_adjudication': 9918, 'candidate_duplicate_groups_resolved': 330,
    'duplicate_group_outcomes': {'merge': 318, 'retain_distinct_reports': 11, 'partial_merge': 1},
    'additional_duplicate_removals': 331, 'canonical_records': len(rows),
    'previously_semantically_screened_canonical_records': 6999,
    'new_canonical_records_screened': len(decisions), 'canonical_records_screened': len(rows),
    'canonical_records_pending': 0, 'canonical_outcomes': dict(sorted(counts.items())),
    'new_2588_outcomes': dict(sorted(newcounts.items())),
    'records_retained_for_fulltext_or_secondary_assessment': retained,
    'records_removed_from_core_at_title_abstract': excluded,
    'original_ids_directly_read_across_revisions': 9827,
    'duplicate_alias_original_ids_not_separately_read': 91,
    'new_review_assignment_counts': agents,
    'independent_human_reviewers': 0, 'fulltexts_assessed_in_this_screening_revision': 0,
    'reports_sought_for_fulltext': None, 'reports_retrieved_for_fulltext': None,
    'final_included_studies': None,
}
assert 19963 - 5094 == 14869 and 14869 - 4951 - 331 == len(rows)
assert 7239 + len(decisions) == 9827 and 9918 - 9827 == 91
jsonwrite('completion_summary.json', summary)
validation = {
    'queue_ids_exactly_covered': True, 'all_9587_canonical_records_have_decisions': True,
    'overlapping_new_review_ids': 0, 'new_literal_evidence_matches_source': 2588,
    'all_nonadjudication_input_fields_preserved': True, 'prior_6999_decisions_unchanged': True,
    'duplicate_adjudication_unchanged': True, 'merged_metadata_provenance_preserved': True,
    'all_new_reasons_nonempty_individually_authored': True,
    'automated_checks_validate_traceability_not_scientific_accuracy': True,
    'unverified_doi_not_invented': True,
    'prior_input_sha256': hashlib.sha256((OUT / 'revised_records.zip').read_bytes()).hexdigest(),
    'immutable_queue_sha256': hashlib.sha256((WORK / 'remaining_canonical_2588.json').read_bytes()).hexdigest(),
}
jsonwrite('completion_validation.json', validation)
prisma = [
    ('query_memberships',19963),('within_database_overlap_removed',5094),('database_distinct_records',14869),
    ('prior_duplicates_removed',4951),('additional_duplicates_removed',331),('records_screened',9587),
    ('records_pending_title_abstract',0),('records_excluded_from_core',excluded),
    ('records_retained_for_next_assessment',retained),
] + [(k,v) for k,v in sorted(counts.items())]
(OUT / 'prisma_complete_counts.csv').write_bytes(csvbytes([{'item':k,'count':v,'unit':'records; not final included studies'} for k,v in prisma]))
table = '\n'.join(f'| {k} | {v:,} | {newcounts.get(k,0):,} |' for k,v in sorted(counts.items()))
report = f'''# S4/S5 PRISMA reporting record — complete title/abstract screening

All **9,587 canonical records** now have semantic title-and-complete-available-abstract decisions; **0 remain unscreened**. This revision completes the remaining **2,588**. This is AI-assisted screening, not completed full-text eligibility or independent human review.

## Identification and duplicates

19,963 exported query memberships − 5,094 within-database query overlaps = 14,869 database-distinct records. After 4,951 earlier cross-database duplicate removals and 331 additional bibliographically adjudicated removals, 9,587 canonical records remain. The 330 candidate groups were resolved as 318 merges, 11 distinct-report groups and one partial merge. All 14 DOI-conflict groups retain their documented resolution; one canonical DOI remains unverified and blank, with supplied identifiers preserved. No new bibliographic merges were performed in this revision.

## Screening outcomes

| Decision | All canonical records | New 2,588 |
|---|---:|---:|
{table}

{retained:,} records remain for full-text or secondary-source assessment; {excluded:,} are removed from the S4/S5 core at title/abstract stage. The methods/background category is retained in a separate evidence library, although excluded from the core. `retain_fulltext_unclear` means eligibility is unresolved and requires source/full-text examination, not final inclusion. `retain_secondary` is secondary literature kept separately from primary reports.

## Reading coverage and method

The earlier requested queue contained 7,238 original IDs (50 previously read plus 7,188 completed). One supplemental retraction review brought directly read original IDs to 7,239, corresponding to 6,999 canonical decisions after bibliographic merges. The present 2,588 canonical IDs were read directly by the primary assistant and three delegated assistants. Combined: 9,827 original IDs were directly read; 91 duplicate-alias IDs were not separately read. All 9,587 canonical records are covered. These denominators must not be interchanged.

Each new decision contains the record ID, queue position, individual reason, literal title/abstract evidence, stage relevance, abstract adequacy and AI attribution. Complete available abstracts were read; missing or mismatched metadata is explicitly flagged. S4 includes recoverability, reuse, repair and physical building retention; S5 includes material-related embodied and life-cycle environmental assessment. Digital Twin and uncertainty terms were not mandatory. Operational-energy-only, financial-cost-only and unrelated topics are excluded; transferable technical methods remain separate. Retention is deliberately inclusive at title/abstract stage and does not prove an uncertainty-transfer mechanism.

Elicit delivered 80 records in the prior phase, all reread by the primary assistant, with 14 corrections. No Elicit upgrade was purchased and no additional Elicit output is claimed in this revision. All new decisions are direct assistant readings. No independent human reviewer participated. Scripts persist authored decisions, check coverage and build tables; they do not classify eligibility by keyword rules.

## Validation and limits

Exact queue coverage, absence of overlapping new IDs, nonempty reasons, literal evidence, all original bibliographic/source fields, prior 6,999 decisions and merged provenance were checked. DOI, authors, titles, abstracts and all other supplied fields are preserved. Missing metadata is not fabricated. Source inconsistencies may remain for full-text verification; for example, `S45-b7761f1ee86d` has an electronic-waste title but an adaptive-building-reuse abstract and is retained as unclear.

Two additional related-report families were flagged during reading and verified against publisher/university metadata: the [Madrid Spanish/English reports](https://www.sciencedirect.com/science/article/abs/pii/S043956891830024X) and the [recovered-wood original/corrected report](https://portal.fis.tum.de/en/publications/erratum-potentials-for-cascading-of-recovered-wood-from-building-/). They retain distinct report records and source identifiers, with explicit family/version fields and `related_report_versions.csv`; do not count these versions as independent studies. Prefer the corrected wood version for quantitative extraction. This does not alter the prior 330 duplicate-group decisions or report-level denominator.

These checks establish completeness and traceability, not independent validation of scientific accuracy. Reports sought/retrieved, full-text exclusion reasons and final included-study counts are not yet determined. Full texts assessed in this screening revision: **0**. The earlier Digital Twin full-text corpus is separate. A PRISMA flow must stop at title/abstract screening until full-text eligibility is actually performed.

Reporting basis: [PRISMA 2020 explanation and elaboration](https://www.bmj.com/content/372/bmj.n160), particularly selection process and flow reporting. PRISMA is a reporting guideline, not a certification of screening quality.

## Current files and reproducibility

Use `canonical_screening_complete.zip`, `screening_decision_sets.zip`, `remaining_2588_review_log.zip`, `remaining_2588_decisions.json`, `completion_summary.json`, `completion_validation.json` and `prisma_complete_counts.csv`. The previous `revised_records.zip` and `summary.json` remain immutable historical inputs, not the current result.

`completion_reproducibility_bundle.zip` contains the immutable queue, four authored decision files and read/save/integration scripts. Extract at the workspace root with the prior `revised_records.zip`, `title_abstract_decisions.json` and `supplemental_integrity_decisions.json` in `outputs/S4 S5 Core Review/screening/adjudication/`, then run `python work/complete_canonical_screening.py`. All three prerequisites are preserved in this repository folder. The integration aborts unless every new ID has an authored decision and all preservation checks pass. No API, paid service or automatic semantic classifier is needed to reproduce the outputs.
'''
(OUT / 'PRISMA_REASSESSMENT.md').write_text(report, encoding='utf-8')
(OUT / 'README.md').write_text(f'''# S4/S5 — all canonical title/abstract records screened

**9,587/9,587 canonical records screened; 0 pending.** The final 2,588 are completed in this revision. This is AI-assisted title/abstract screening; full-text eligibility remains a separate next step.

| Outcome | Count |
|---|---:|
| Retain for full text | {counts['retain_for_fulltext']:,} |
| Unclear: retain for full-text verification | {counts['retain_fulltext_unclear']:,} |
| Secondary literature | {counts['retain_secondary']:,} |
| Methods/background, outside core | {counts['exclude_core_keep_methods']:,} |
| Out-of-scope title/abstract exclusions | {counts['exclude_title_abstract']:,} |
| Nonresearch components | {counts['exclude_nonresearch_component']:,} |
| Retracted source | {counts['exclude_retracted_source']:,} |

## Current deliverables

- `canonical_screening_complete.zip`: complete CSV with all original bibliographic fields, DOI/authors/abstract, provenance, previous status and final screening reasons/evidence; original merged metadata JSON preserved.
- `screening_decision_sets.zip`: seven full-metadata CSVs split by decision.
- `remaining_2588_review_log.zip` and `remaining_2588_decisions.json`: all newly authored decisions with individual reasons, literal evidence, stage and abstract adequacy.
- `PRISMA_REASSESSMENT.md`, `prisma_complete_counts.csv`, `completion_summary.json`: actual coverage/counts and methodological qualifications.
- `completion_validation.json`: preservation and coverage checks.
- `related_report_versions.csv`: two publisher/university-verified translation/correction families; distinct reports must not be double-counted as independent studies.
- `completion_reproducibility_bundle.zip`: authored decisions, immutable queue and processing code.
- `duplicate_group_adjudication.csv`, `record_alias_map.csv`, `IDENTIFIER_RESOLUTION.md`: unchanged evidence for all 330 duplicate groups and 14 DOI-conflict resolutions. 331 additional removals; one unverified DOI blank rather than invented.

## Historical inputs

`revised_records.zip`, `summary.json`, `title_abstract_review_log.zip`, `title_abstract_decisions.json`, `direct_review_coverage.json`, `final_validation.json`, `final_manifest.json`, `prisma_reassessment_counts.csv` and `reproducibility_bundle.zip` describe the previous completed queue of 7,238 original IDs plus one supplemental integrity review. They remain auditable inputs and are superseded for current totals by the completion files above. Earlier partial/checkpoint files are historical only. Do not rerun the older build scripts over the new report.

There was no independent human review; Elicit was not upgraded. Retained reports are not final included studies. Full-text assessment count for this revision is zero. See the PRISMA report for exact original-ID versus canonical denominators and limits.

## CSV field interpretation

Use `adjudication_status`, `adjudication_reason`, `adjudication_evidence` and `adjudication_reviewer` for the current semantic decision. `screening_status`, `decision_reason`, `decision_basis`, `matched_rule` and `reviewer` are preserved original automated-routing fields, not the current decision. `previous_adjudication_status` records the prior revision. The `completion_*` stage/adequacy fields are populated for the new 2,588 only; older detailed adequacy/stage evidence remains in the previous original-ID review log. All original author, DOI, abstract, journal, year, source and identifier fields remain available. Empty DOI means missing/unverified, not a fabricated identifier. `related_report_family` links known versions without asserting that every possible study family has been resolved.
''', encoding='utf-8')
with zipfile.ZipFile(OUT / 'completion_reproducibility_bundle.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for path in [WORK/'remaining_canonical_2588.json', WORK/'complete_canonical_screening.py', WORK/'read_remaining_canonical.py', WORK/'save_remaining_canonical.py', *sorted(WORK.glob('remaining_decisions_*.json'))]:
        z.write(path, path.relative_to(ROOT))
(OUT / 'complete_canonical_screening.py').write_bytes((WORK / 'complete_canonical_screening.py').read_bytes())
files = ['canonical_screening_complete.zip','screening_decision_sets.zip','remaining_2588_review_log.zip','remaining_2588_decisions.json','completion_summary.json','completion_validation.json','prisma_complete_counts.csv','PRISMA_REASSESSMENT.md','README.md','completion_reproducibility_bundle.zip','related_report_versions.csv','complete_canonical_screening.py']
jsonwrite('completion_manifest.json', {name: {'bytes':(OUT/name).stat().st_size,'sha256':hashlib.sha256((OUT/name).read_bytes()).hexdigest(), 'git_blob_sha1':hashlib.sha1(b'blob '+str((OUT/name).stat().st_size).encode()+b'\0'+(OUT/name).read_bytes()).hexdigest()} for name in files})
print(json.dumps(summary, ensure_ascii=False, indent=2))

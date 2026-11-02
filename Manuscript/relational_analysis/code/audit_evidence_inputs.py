"""Reconcile existing review streams without inventing thematic annotations.

Run from a checkout containing Manuscript/ and analysis_ready/. In the local
authoring workspace the same inputs also live directly under outputs/.
"""
from pathlib import Path
from collections import Counter, defaultdict
import csv, hashlib, json

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parents[1]

def locate(relative):
    for base in [BASE, BASE/'analysis_ready']:
        p=base/relative
        if p.is_file(): return p
    raise FileNotFoundError(relative)

def read(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def write(name,rows):
    with (ROOT/name).open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

specs=[
 ('S_U','seleted papers S1-S5 + U/transition_extraction.csv','paper_id','doi','title','evidence_status_prior'),
 ('S_DT','Digital Twin Material Flow Review/bridge_searches/fulltext_review/extraction_14.csv','record_id','doi','title','evidence'),
 ('DT_U','Digital Twin Uncertainty Review/fulltext/fulltext_extraction.csv','publication_id','DOI','Title','full_text_status')]
membership=[];papers={};audit=[]
for stream,rel,idcol,doicol,titlecol,statuscol in specs:
    p=locate(rel);data=read(p);qual=0
    for r in data:
        doi=r[doicol].lower().strip().removeprefix('https://doi.org/').removeprefix('http://doi.org/')
        pid=r[idcol];status=r[statuscol]
        key='doi:'+doi if doi else 'source:'+stream+':'+pid
        canonical='P-'+hashlib.sha256(key.encode()).hexdigest()[:12]
        if stream=='S_U':
            ready=pid!='U10';role='methodological_review' if pid in ['U02','U14'] else ('complementary_primary' if pid in ['U20','U21'] else 'primary_topic')
            location=r['evidence_anchor'];note=r['review_basis']
        elif stream=='S_DT':
            ready=status not in ['abstract_only_pending_fulltext',''];role='domain_or_enabling_architecture_candidate'
            location=r['location'];note='Bridge-search selection includes complements; S1-S2/S2-S3 focus, not complete S1-S5 DT coverage.'
        else:
            ready=status.startswith('read_');role='mechanism_or_architecture_candidate'
            location=r['report_anchor'];note=r['version_note'] or 'Archived appraisal; primary, secondary and adjacent-system evidence require separate eligibility labels.'
        qual+=int(ready)
        membership.append({'canonical_id':canonical,'stream':stream,'source_id':pid,'doi':doi,'title':r[titlecol],
                           'recorded_evidence_status':status,'has_archived_fulltext_based_assessment':int(ready),
                           'role_caution':role,'anchor':location,'basis_note':note,'source_file':rel,
                           'new_fulltext_review_this_update':0,'harmonized_relational_coding_complete':0})
        if canonical not in papers:papers[canonical]={'canonical_id':canonical,'doi':doi,'title':r[titlecol],'streams':set(),'source_ids':set(),'ready':False}
        papers[canonical]['streams'].add(stream);papers[canonical]['source_ids'].add(stream+':'+pid)
        papers[canonical]['ready']|=ready
    audit.append({'stream':stream,'source_file':rel,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                  'records':len(data),'archived_fulltext_based_assessments':qual,'pending_or_abstract_only':len(data)-qual,
                  'scope':'selected working evidence, not all indexed retrievals','relational_recoding':'pending'})
registry=[{'canonical_id':p['canonical_id'],'doi':p['doi'],'title':p['title'],
           'streams':';'.join(sorted(p['streams'])),'source_ids':';'.join(sorted(p['source_ids'])),
           'has_archived_fulltext_based_assessment':int(p['ready']),
           'merge_rule':'exact normalized DOI across streams' if p['doi'] else 'source identity retained; no guessed DOI or fuzzy title merge'} for p in papers.values()]
write('paper_registry.csv',registry);write('stream_membership.csv',membership);write('corpus_readiness.csv',audit)
validation={'date':'2026-11-02','stream_memberships':len(membership),'distinct_records_after_exact_doi_merge':len(registry),
            'distinct_records_with_doi':sum(bool(p['doi']) for p in registry),
            'distinct_records_with_archived_fulltext_based_assessment':sum(p['has_archived_fulltext_based_assessment'] for p in registry),
            'multiple_stream_records':[p['canonical_id'] for p in registry if ';' in p['streams']],
            'publication_unit_caution':'Reviews and related studies are not independent primary experiments. DOI matching does not resolve study families.',
            'semantic_relational_analysis_completed':False,'reference_paper_added_as_selected_study':False}
assert len(membership)==53 and len(registry)==52
assert len({(x['stream'],x['source_id']) for x in membership})==len(membership)
assert len([p['doi'] for p in registry if p['doi']])==len({p['doi'] for p in registry if p['doi']})
(ROOT/'validation.json').write_text(json.dumps(validation,indent=2),encoding='utf-8')
print(json.dumps(validation,indent=2))

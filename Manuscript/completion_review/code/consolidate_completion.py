from pathlib import Path
import csv,json,hashlib
O=Path('outputs/Manuscript/completion_review')
E=Path('outputs/Manuscript/methods_audit/eligibility')
def read(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
def write(p,rows):
 with p.open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,list(rows[0]));w.writeheader();w.writerows(rows)
old=read(E/'broad_dtu_fulltext_final_decisions.csv');fields=list(old[0])
yang=read(O/'new_fulltext_decisions.csv')[0]
yang.update(decision='exclude',counting_stream='excluded_from_triple_intersection',evidence_role='Complementary S1 reconstruction-error evidence outside strict DT intersection',reason='Applies the existing cross-batch DT boundary consistently: the implemented semantic reconstruction/fusion pipeline has geometric-error evaluation, but DT use is a prospective application rather than a specified asset updating, provenance or decision interface. Retain for S1 background; exclude from strict S+DT+U synthesis.')
yang['title']='Research on multi-source data fusion and high-precision mapping method for complex landforms based on computer vision'
yang['dt_status']='Prospective DT foundation; temporal fusion and scene-graph integration are future work'
yang['uncertainty_treatment']='Measured reconstruction error and learned fusion weights; no calibrated uncertainty distribution or downstream material propagation'
yang['limitations']=yang.pop('uncertainty_boundary',yang.get('limitations',''))
yang.update(decision_source='completion_review/new_fulltext_decisions.csv',source_type='local_PDF',hash_scope='reviewed_local_file')
url='https://journal.oscm-forum.org/publication/pdf/digital-twins-for-sustainable-and-low-carbon--supply-chains-in-industry-x.0-crossing-the--fragmented'
review={k:'' for k in fields}
review.update(record_id='DTMFU-d52dc48a0eac5845',doi='10.31387/oscm0640504',title='Digital Twins for Sustainable and Low-Carbon Supply Chains in Industry X.0: Crossing the Fragmented Bridge Between Academic Research and Industrial Adoption',decision='exclude',counting_stream='excluded_from_triple_intersection',evidence_role='Contextual secondary review; not an extractable uncertainty-assessment mechanism',reason='Bibliometric/thematic supply-chain review. BIM-to-LCA uncertainty is discussed as an interoperability limitation, without a defined assessment or propagation mechanism. Retain as background, outside strict S+DT+U evidence.',evidence_locator='PDF pp3-4 methods; pp5-9 results; pp10-12 discussion/conclusion; section4.5.3 on PDF p9',dt_status='Secondary review of DT applications',uncertainty_treatment='Qualitative limitations concerning data mapping and system boundaries',limitations='Deployment percentages use title-based categorisation (section5), not full-text implementation verification. Do not import them into our results.',source_path=url,assessment_scope='Publisher fulltext accessed; targeted eligibility reading of methods/results/discussion. References and underlying studies not independently checked.',decision_source='completion_review/new_fulltext_decisions.csv',source_type='publisher_web_PDF',hash_scope='No local corrected-PDF hash; publisher URL and page locators retained')
new=[{k:yang.get(k,'') for k in fields},review]
write(O/'new_fulltext_decisions.csv',new)
merged={r['record_id']:r for r in old}
for r in new:merged[r['record_id']]=r
rows=list(merged.values());write(O/'broad_dtu_current_fulltext_decisions.csv',rows)
assessed=[r for r in rows if r['counting_stream']!='not_assessed_retrieval_defect']
counts={x:sum(r['counting_stream']==x for r in assessed) for x in sorted({r['counting_stream'] for r in assessed})}
assert len(assessed)==91 and sum(counts.values())==91
known_dois=[r['doi'].lower() for r in assessed if r['doi'].strip()]
assert len(set(known_dois))==len(known_dois)
status=json.loads((O/'completion_status.json').read_text())
status['updated_fulltext_validation']={'assessed_unique_publications':len(assessed),'counts':counts,'candidates':308,'unassessed':308-len(assessed),'new_decisions':2,'source_ledger_sha256':hashlib.sha256((E/'broad_dtu_fulltext_final_decisions.csv').read_bytes()).hexdigest(),'scope':'Current versioned reconciliation; no inference that all candidates have been assessed or are irretrievable.'}
(O/'completion_status.json').write_text(json.dumps(status,indent=2),encoding='utf8')
cor=read(O/'doi_correction.csv');cor[0]['status']='Corrected using publisher title/authors/pages; targeted fulltext eligibility completed. Excluded from strict triple intersection; contextual review retained. Corrected DOI not found elsewhere in local CSV corpus.';write(O/'doi_correction.csv',cor)
print(status['updated_fulltext_validation'])

import json, urllib.request
from pathlib import Path
P=Path('outputs/S4 S5 Core Review/screening/adjudication')
d=json.loads((P/'duplicate_decisions.json').read_text(encoding='utf-8'))
resolutions={
309:('10.1007/978-3-540-95991-5_22','Crossref verifies the underscore chapter DOI and matching chapter title/pages; the hyphen variant returned 404.'),
312:('10.2166/wst.1996.0563','Both supplied DOIs are registered for the same title, authors, journal volume 34 issues 5–6 and report. Preserve the Elsevier-form DOI as a valid alias; prefer the IWA DOI.'),
315:('10.1080/13632460609350594','Current and legacy Crossref entries agree on French, Journal of Earthquake Engineering 10(2), page 207; the current entry gives the matching title and pages 207–236. The legacy DOI is not invalid; retain as an alias.'),
317:('10.1088/1742-6596/3140/3/032010','Both Crossref requests return the same canonical DOI with issue 3 and matching title; issue 5 in the supplied alternative is not the canonical identifier.'),
318:('10.1088/1742-6596/3140/7/072010','Both Crossref requests return the same canonical DOI with issue 7 and matching title; issue 8 in the supplied alternative is not the canonical identifier.'),
319:('10.1109/ecodim.2003.1322733','Both registered DOIs resolve in Crossref resource metadata to IEEE document 1322733 and agree on title, Weng/Yashiro and pages 541–543. The VETECF container is inconsistent; this is one EcoDesign report, not two conference reports. Preserve both identifiers.'),
321:('10.1109/icmss.2011.5998416','Crossref verifies the matching Carbon Impact Air Curtains report under 5998416; the extra-leading-zero variant returned 404.'),
322:('10.1109/smartiot.2018.00046','Crossref verifies the matching fuzzy-logic fire/IoT report and pages 216–221 under 00046; the supplied 000-2 variant returned 404.'),
324:('10.3763/aber.2009.0402','Crossref identifies this DOI as the matching HVAC article, volume 4(1), pages 23–44. The other identifier 10.4324/9781849776349 is the parent book, not a separate version of this article.'),
325:('','Publisher XML RP-053-P264 confirms the identical title, Babendererde/Elsner authors and anchor-recovery abstract. Both supplied complete DOI strings returned Crossref 404; the publisher exposes only local article identifier RP-053-P264. Merge the duplicated report on bibliographic evidence, leave canonical DOI unverified/blank and retain both supplied strings. A Crossref 404 alone does not establish global DOI invalidity.'),
326:('10.4018/978-1-4666-1761-2.ch013','Crossref verifies the matching book chapter A Good Role Model for Ontologies, pages 225–235, as ch013; ch0013 returned 404. Do not merge with the separate 2010 journal version.'),
327:('10.62754/ais.v6i1.132','Crossref and publisher article 132 match the architecture title, authors and pages 334–343. The alternative 10.48619 identifier returned 404.'),
328:('10.4995/vitruvio-ijats.2023.18801','Both DOI spellings are registered and point to publisher article 18801 with identical title/authors/pages 56–65. Merge as one report and preserve both valid DOI aliases.'),
329:('10.4995/vitruvio-ijats.2023.19674','Both DOI spellings are registered and point to publisher article 19674 with identical title/authors/pages 98–105. Merge as one report and preserve both valid DOI aliases.')}
checks=json.loads((P/'doi_registry_checks.json').read_text(encoding='utf-8'))
for i,(doi,reason) in resolutions.items():
 v=d[str(i)];v.update(decision='merge',reason=reason,canonical_doi=doi,identifier_status='verified' if doi else 'unverified_preserved',verification_date='2026-11-01',evidence_urls=' | '.join(x['url'] for x in checks if x['group']==str(i)))
 if i==325:v['evidence_urls']+=' | https://rpsonline.com.sg/proceedings/9789810737573/html/RP-053-P264.xml'
(P/'duplicate_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
u='https://rpsonline.com.sg/proceedings/9789810737573/html/RP-053-P264.xml'
(P/'publisher_anchor_recovery.xml').write_bytes(urllib.request.urlopen(u,timeout=30).read())
print('Resolved 14 duplicate groups; one canonical DOI remains unverified, explicitly blank.')

# Adjudication of the 14 identifier-conflict groups

Verified 2026-11-01 against Crossref metadata and publisher records. Group numbers in the CSV are one-based; keys in the JSON evidence are zero-based.

All 14 groups describe duplicate reports and are merged. This removes 14 additional records beyond the previous checkpoint: 331 additional removals overall, leaving 9,587 records. The 330 group outcomes are 318 merges, 11 distinct-report groups and one partial merge. These are record counts, not included-study counts.

| CSV group | Resolution |
|---|---|
| DUP-310 | Springer chapter: underscore DOI verified; hyphen variant not found in Crossref. |
| DUP-313 | IWA/Elsevier DOI aliases for the same report; both registered. |
| DUP-316 | Current Taylor & Francis and legacy World Scientific identifiers describe the same journal report. |
| DUP-318 | Crossref normalizes both requests to the issue-3 DOI. |
| DUP-319 | Crossref normalizes both requests to the issue-7 DOI. |
| DUP-320 | Both identifiers point to IEEE document 1322733; one container name is inconsistent. |
| DUP-322 | Extra leading zero removed; matching IEEE report verified. |
| DUP-323 | IEEE suffix 00046 verified; supplied 000-2 not found. |
| DUP-325 | Matching article DOI selected; other identifier belongs to its parent book. |
| DUP-326 | Matching publisher title, authors and abstract establish one report. Neither supplied DOI verified; canonical DOI blank, original strings preserved. |
| DUP-327 | IGI chapter suffix ch013 verified; ch0013 not found. |
| DUP-328 | Publisher article 132 and Crossref support 10.62754/ais.v6i1.132. |
| DUP-329 | Both hyphenated/nonhyphenated DOI forms registered for article 18801. |
| DUP-330 | Both hyphenated/nonhyphenated DOI forms registered for article 19674. |

`doi_registry_checks.json` preserves query URLs, returned canonical DOIs and bibliographic metadata. A 404 from Crossref means that this registry lookup failed, not proof that an identifier cannot exist elsewhere. `publisher_anchor_recovery.xml` preserves the publisher's article metadata for DUP-326. The identifier RP-053-P264 in that XML is a local identifier, not a complete verified DOI.

`duplicate_group_adjudication.csv` contains individual rationales and evidence URLs. `record_alias_map.csv` preserves all 9,918 input IDs. `revised_records_partial.zip` preserves all supplied DOI strings and merged source metadata. Bibliographic deduplication does not decide topical eligibility; title/abstract screening remains a separate task.

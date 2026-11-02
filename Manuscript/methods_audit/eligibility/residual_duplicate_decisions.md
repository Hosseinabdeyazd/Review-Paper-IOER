# Residual exact-title duplicate review

Scope: all 528 canonical Base+DT+U records. Titles normalized using Unicode decomposition, ASCII transliteration, case folding and removal of non-alphanumeric characters; no year restriction. Three repeated-title groups found: two pairs of study reports and one eight-record proceedings group.

## Findings

- Merge row 522 into row 145 (DOI 10.1061/9780784483893.069): same title, author order, substantive abstract and conference. The ASCE publisher confirms the report and an online date of 24 May 2022, despite the proceedings edition being titled 2021. Source years must remain in provenance.
- Merge row 494 into row 371 (DOI 10.26868/25222708.2019.210257): same title, six authors, substantive abstract and conference. The IBPSA publisher confirms the DOI and pages 1304–1310. RWTH repository links the same Scopus identifier 85107486052 to this DOI; 2019/2020 is a bibliographic-year difference, not an independent report.
- Preserve rows 509–516 as eight distinct conference-volume records: the original Scopus export supplies volumes 44,40,45,38,41,43,42,39 respectively. Although the titles and topic-list abstracts repeat, there is affirmative evidence of distinct volumes. They remain excluded by report type in screening and must not be counted as seven duplicate removals.

Applying only these mappings would reduce 528 canonical records to 526; it does not establish absence of near-title or DOI-format duplicates. No original canonical or screening CSV was modified. Merge source memberships and retain aliases before recounting. One fulltext candidate duplicate (522) and one already domain-excluded duplicate (494) are affected; therefore do not subtract both from a single screening category.

## Sources

- https://ascelibrary.org/doi/10.1061/9780784483893.069
- https://publications.ibpsa.org/conference/paper/?id=bs2019_210257
- https://publications.rwth-aachen.de/record/766474
- Local raw Scopus S4.csv (path in decision CSV), whose Volume and EID fields resolve the conference-container group.

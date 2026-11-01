# Three full-text candidates: S4 → S5 uncertainty mechanisms

Review date: 2026-11-02. Scope: the three narrow bridge candidates selected from the 392 Base + Uncertainty records. This is a new full-text assessment layer; the earlier abstract decisions are retained in the extraction CSV for audit.

Local acquisition at this checkpoint: publisher PDFs for Almeida (22 pages) and Caruso (16 pages), plus Caruso's 5-page supplement, are saved and verified. Aljawhari's complete publisher-rendered text is saved as `Aljawhari_2024_publisher_fulltext.txt`; its 20-page original PDF is open in the browser but local PDF saving remains pending. Full-text reading is complete for all three; PDF downloading is not yet complete for all three. These states must not be conflated.

**Result: one directly relevant circularity–LCA framework and two adjacent repair/reconstruction-to-carbon mechanisms. None verifies the complete target chain of uncertain circular recovery → joint LCA → operational digital-twin updating.**

Read [REPORT_FA.md](REPORT_FA.md) for the Persian synthesis. The [extraction table](fulltext_extraction.csv) retains all prior bibliographic fields, DOI, source IDs and prior decisions and adds the full-text decision, reason, mechanism and page anchors. Detailed evidence is in `paper1_notes.md` through `paper3_notes.md` and their JSONs. [download_manifest.csv](download_manifest.csv) records PDF versions, lengths, pages and SHA-256. PDFs are retained locally; this GitHub package contains the extraction and analysis, not redistributed full article text.

| Paper | Direct match to S4 circular recoverability → S5 embodied LCA | Full-text decision |
|---|---|---|
| Almeida et al., 10.1016/j.jclepro.2026.148705 | Closest | Shared reuse-feasibility inputs; probabilistic propagation in circularity and CFF branches. Joint cross-branch sampling/dependence not documented. |
| Aljawhari et al., 10.1016/j.jobe.2023.108149 | Adjacent | Explicit damage → repair quantities → carbon uncertainty. Fixed recycling; not uncertain recovery yield or quality. |
| Caruso et al., 10.1038/s41467-025-68120-6 | Adjacent | Economic risk ratio → replacement-carbon proxy at portfolio scale. Fixed quantities and recovery share. |

## Review accounting

Three reports sought, three substantive full texts assessed. No new search, duplicate removal or revision of the 392-record universe is performed here. One report is retained as a direct topical anchor and two as adjacent methodological evidence. Zero reports establish the complete target joint circular-recovery-to-LCA/DT mechanism. These are evidence-use classifications, not three new independent studies added to the prior PRISMA total. The other 389 records were not full-text reviewed in this step. Supplementary information for Caruso was also read, but is not an additional study.

This is AI-assisted review with cross-paper consistency checking, not independent human double screening. No article simulation was reproduced; missing distributions, covariance, code or source data were not invented. References inside articles were not individually screened.

## Reproducibility

`build_three_fulltexts.py` packages manually authored full-text extractions, merges the existing bibliography by exact DOI and verifies PDF headers/DOI/page counts and hashes. It is not an automated eligibility classifier or a reconstruction of the published Monte Carlo models. Its original workspace inputs are `work/fulltext{1,2,3}_extraction.json`, companion notes and the adjacent prior 392-record CSV. When executed beside the delivered files it reads the delivered JSONs/notes and falls back to `bibliographic_inputs.csv`. PDF verification requires the locally retained PDFs under `pdfs/`; an absent file is marked pending rather than invented.

The review's stage labels are **S4 circularity/recoverability** and **S5 embodied LCA/decision**. The article-specific scenarios S1–S7 in Almeida are unrelated to these review stages. Repair/retention in papers 2–3 must not be silently relabelled as circular recoverability.

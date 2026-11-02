FULL MANUSCRIPT WORKING DRAFT — NO ABSTRACT

Reading copies:
pdf/manuscript_no_abstract_en.pdf
pdf/manuscript_no_abstract_fa.pdf

Five sections: Introduction; Related work (continuous); Methods; Results; Discussion.
Each language contains 18 figures, including four methods/selection figures, four previously coded D01–D04 results, five recalculated frequency/percentage figures, a conceptual outcome vocabulary, three supplied DT design figures and one proposed tracking overlay. Figure captions distinguish measured coding frequencies from conceptual diagrams.

Evidence status:
This is a complete-text working draft, not a closed submission-ready systematic review. Broad eligibility remains incomplete. No new full-text decisions or comprehensive semantic recoding were performed in this update. The 17-paper legacy source/method/outcome counts were reconstructed from the article-level coding; all 17 identities matched included records in the current eligibility ledger. The 17-paper and 20-paper/23-context analytical sets are not interchangeable. General DT mechanism percentages use 10 non-review coded records. No pooled uncertainty magnitude or percentage reduction is claimed.

The original 17-paper outcome words were reproduced through explicit wording aliases. Reproduction does not validate their interpretation as measured propagation, amplification or legitimate reduction. The manuscript explains this distinction and retains the separate context-based continuity classification. The old 1/9 versus 6/9 transition contrast was not promoted to a current result because boundary allocation differs from the later context coding.

Architecture:
The A/B/C design vocabulary is a prior literature-informed synthesis, not a frequency result. Its original reference keys and access limitations are retained in inputs/academic-foundations.md and inputs/references.bib. The complete S1–S5 tracking overlay is proposed synthesis. Residuals, coverage, dependencies, timestamps and decision authority are operationally defined; no automatic detection of every uncertainty source or universal scaling claim is made.

Reproduction:
1. Run build_analysis.py to recompute counts and six new analytical/conceptual graphics.
2. Run build_manuscript.py to assemble bilingual reading HTML/text, a figure manifest, references and English LaTeX.
3. Run render.cjs to render reading PDFs and the additional vector figure PDFs.
4. The earlier D01–D04 verifier remains at ../relational_analysis/data_diagrams/code/verify_data_diagrams.py.

The Python plotting path and Chrome/Playwright paths reflect this workstation; adapt them or install the corresponding packages on another machine. User-supplied SVG input copies are preserved in inputs. Build_analysis.py refreshes them from the original Downloads paths on this workstation; if unavailable elsewhere, retain the archived copies.

LaTeX:
tex/main.tex is the no-abstract entry point (XeLaTeX + BibTeX). It uses the parent repository figures and bibliography style. The reading PDFs were rendered from HTML and visually inspected; a full LaTeX compilation was not performed. This does not overwrite the earlier manuscript draft.

Data and provenance:
data/*.csv retain numerators, denominators and supporting IDs; analysis_validation.json records source hashes and limits. figure_manifest.csv maps figure numbers to files and captions. Original source data were obtained from Review-Paper-IOER analysis_ready/fulltext_uncertainty_results and Manuscript/relational_analysis. The primary version of the design concepts is retained under DT/DT structure in the same repository.

Query strings remain in ../supplementary_material/S1_search_strategies.txt and S1_S3_recovered_queries.txt. This writing update did not execute new searches or change historical query membership.

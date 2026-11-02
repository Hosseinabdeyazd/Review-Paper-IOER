SECTIONS 2 AND 3: CONNECTED REVIEW DESIGN

Reading versions:
pdf/sections_2_3_en.pdf
pdf/sections_2_3_fa.pdf
reading_versions/sections_2_3_en.html
reading_versions/sections_2_3_fa.html
reading_versions/sections_2_3_en.txt
reading_versions/sections_2_3_fa.txt

Section 2 is continuous related work without subsections. Section 3 specifies a shared interface record joining S1-S5, uncertainty operations, DT capabilities and evidence locators. Both versions include four figures, two analytical/query tables, an actual archived Scopus query example and 21 references in author-year form.

LaTeX integration:
main.tex now includes sections/02_related_work.tex and sections/03_methods.tex.
The previous sections/02_methods.tex and Persian counterpart are archived historical drafts, no longer included by main.tex. Later draft section filenames are retained; LaTeX automatically renumbers their section headings. The last paragraph of the English introduction is updated to match this order. The complete main manuscript was not compiled in this change; the two reading PDFs were rendered and checked separately.

Figure status:
1 workflow: conceptual methodological diagram, not a research finding.
2 evidence_join: shared extraction and relational-analysis design, not empirical frequency.
3 prisma_broad_dtu_status: ledger-derived audit snapshot, NOT final all-scenario PRISMA.
4 focused_selection_status: focused-subset full-text adjudication, NOT database identification; overlaps broad searches.

No new eligibility decisions were made in this writing update. The 219 pending broad DTU candidates were NOT converted to full-text exclusions or not-retrieved records. The 25 assessed broad DTU inclusions do not close the 308-candidate search. The 43 focused unique inclusions cannot be added to them without a record-level overlap reconciliation. No inclusion cap of 30-40 or 100 was imposed.

Query provenance:
supplementary_material/S1_search_strategies.txt
supplementary_material/S1_S3_recovered_queries.txt
The explanatory block table is not a replacement for archived executed strings. Historical missing execution details remain an audit issue; no new search was performed for the conceptual query display.

Reproduction:
python Manuscript/build_sections_2_3.py
node Manuscript/render_sections_2_3.cjs
The rendering script uses the local bundled Playwright and Chrome paths; adapt those two paths on another machine. HTML and SVG remain browser-readable without this script. No authenticated browser profile is used by rendering. Figure count inputs and source hashes are in figures/methods/figure_counts.csv and validation.json.

New coding dimensions in section 3 specify the integrated synthesis protocol. They have not been retrospectively filled for every historical record. Final submission requires completion of pending eligibility and the shared extraction ledger, reconciliation of all search-family flows, and updating the explicit reporting-status note.

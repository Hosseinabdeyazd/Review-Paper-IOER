# Compact manuscript: references retained, counted separately

| File | Main text and figures | References | Total PDF pages | Main word count |
|---|---:|---:|---:|---:|
| [English manuscript](manuscript_en.pdf) | 24 | 4 | 28 | 8,436 |
| [Persian manuscript](manuscript_fa.pdf) | 24 | 4 | 28 | 8,847 |

The 28-page ceiling applies to the main manuscript only. References remain inside both manuscript PDFs, beginning on page 25. The word counts exclude the title/front notice and reference list; they include main headings, tables and captions. Text embedded in figure assets is not included in the word count. Both versions retain 58 bibliography entries; no references were removed or added in this layout revision.

Each manuscript contains nine main figures. Nine supporting figures, the search-block table, detailed counting equations, reproducibility checks and architectural source register are retained in [English supporting material](supplement_figures_en.pdf) and [Persian supporting material](supplement_figures_fa.pdf). Full historical search and evidence files remain in the parent Manuscript folders.

## Editable files and reproduction

The HTML files are the editable sources used to render these PDFs. The English `main.tex` uses the Elsevier `elsarticle` class, with `body.tex` containing matching manuscript text and references. Compile with XeLaTeX in an environment with elsarticle and TeX Gyre Termes; figure PDFs are referenced from their existing repository locations. TeX compilation was not performed here, so its pagination is not asserted to match the supplied PDFs.

Run `../compact.cjs` to rebuild both manuscript and supporting-material PDFs; run `export_source.py` to export English LaTeX and verify the page/word limits. `layout_audit.json` records the verified counts.

## Status

This is a compact working manuscript, without abstract as requested. This revision changes layout and placement of supporting material; it does not close outstanding review eligibility or validate new scientific claims. The selection status remains explicit in the manuscript and source audit. A reference ceiling of up to 100 is the author's working preference, not a claim of publisher approval. Submission-specific requirements still require a final check.

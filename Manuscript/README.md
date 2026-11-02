# Manuscript — working LaTeX draft

Version 0.2, 2026-11-02. English draft for the systematic-review project on circular building material flows, uncertainty and evidence-traceable DT architecture.

Approved title: **From GeoAI to environmental impact assessment: A systematic review of uncertainty continuity and digital twin architecture for the circular built environment**.

The introduction has been rewritten with 35 references (30 Elsevier and five Nature Portfolio; 34 published in 2020 or later). It contains 1,039 words excluding citations, or 1,160 including author–year citations. Read `Introduction.md` for the introduction and its complete bibliography; edit `sections/01_introduction.tex` for the LaTeX manuscript. Background references are not automatically members of the systematic-review corpus. Other sections remain preliminary.

## Open and build

Open `main.tex` in Overleaf or a standard TeX Live/MiKTeX project. Use pdfLaTeX + BibTeX:

```sh
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

The portable `article` class is used for drafting. This is not represented as an official Journal of Cleaner Production template. Citations use natbib author–year and Elsevier's `elsarticle-harv.bst`, included from the elsarticle distribution on CTAN (https://mirrors.ctan.org/macros/latex/contrib/elsarticle/elsarticle-harv.bst). Author order and affiliations are deliberately unassigned.

## Written in this version

Working title and abstract; introduction and research questions; three-stream synthesis protocol; bounded preliminary evidence; architecture-synthesis specification; discussion and limits. The results are explicitly preliminary. No final PRISMA counts, review completion, universal scalability or validated architecture are claimed.

## Files

- `main.tex`: entry point.
- `sections/*.tex`: editable manuscript sections.
- `references.bib`: DOI-linked references from the previously checked Crossref metadata.
- `evidence_ledger.csv`: claims, source locations and evidence status.
- `WRITING_PLAN.md`: next writing work and unresolved evidence.
- `validate_sources.py`: static checks of section files, citation keys and evidence references. This is not a LaTeX compilation test.

PDFs, institutional credentials and signed download links are not included. Source datasets remain in the repository's existing review folders.

## Verification

Static validation results are recorded in `validation.json`. A LaTeX compiler was not available in the current environment; PDF compilation and visual layout verification remain pending. No compiled PDF is claimed.

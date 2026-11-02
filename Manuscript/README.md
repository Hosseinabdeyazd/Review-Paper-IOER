# Manuscript — working LaTeX draft

Version 0.1, 2026-11-02. English draft for the systematic-review project on circular building material flows, uncertainty and evidence-traceable DT architecture.

## Open and build

Open `main.tex` in Overleaf or a standard TeX Live/MiKTeX project. Use pdfLaTeX + BibTeX:

```sh
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

The portable `article` class is used for drafting. This is not represented as an official Journal of Cleaner Production template. Journal-specific formatting will be applied after the manuscript structure stabilizes. Author order and affiliations are deliberately unassigned.

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

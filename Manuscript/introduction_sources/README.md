# Introduction source and validation record

This folder supports the introduction revision dated 2026-11-02. It does not redefine systematic-review eligibility or add background sources to included-study counts.

- `introduction_draft.txt`: editable text with source identifiers.
- `crossref_metadata.json`: DOI metadata retained for deterministic generation of references.
- `reference_audit.csv`: all 35 sources, author–year labels, complete authors, DOI, journal and publisher.
- `build_introduction.py`: generates the LaTeX introduction, readable introduction with full reference list, bibliography updates and validation record. Run from any directory with Python 3. Existing DOI-matched bibliography keys are reused.
- `validation.json`: word counts, publisher/year composition and citation coverage.

Source identification used primary publisher records and abstracts, with Crossref DOI metadata for author lists, titles, dates and bibliographic fields. This is a background-literature writing exercise, not a new full-text systematic screening exercise. Publication year follows the issue/print year when available rather than the year embedded in a DOI. Nature Portfolio papers carry Springer Nature publisher metadata; no general Springer journal was substituted for Nature Portfolio.

The introduction distinguishes literature-backed descriptions of methods from this review's proposed analytical vocabulary and questions. In particular, the definition of uncertainty continuity, five-stage interface interpretation and candidate architecture functions are presented as the review's framing, not as an already validated consensus architecture. Claims about the extent of gaps await the evidence synthesis.

All 35 references appear in the introduction; all have a DOI. The restricted publisher selection applies to the introduction requested here, not to the systematic-review search/eligibility protocol. One 2017 study is retained for its direct examination of lifespan assumptions in material-stock and demolition-waste accounts.

LaTeX inputs and citation keys were checked statically. No local LaTeX compiler was available; no compiled or visually verified manuscript PDF is claimed. `elsarticle-harv.bst` is supplied for author–year bibliography formatting.

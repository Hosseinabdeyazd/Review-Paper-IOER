# Summed three-database temporal figures

Produced at the user's explicit request on 2 November 2026. These outputs supersede the separated-source presentation for the requested arithmetic-sum view, but do not overwrite its source evidence.

## What is counted
Each annual value is IEEE + Scopus + Web of Science. A paper indexed in all three contributes three records. These are **record occurrences, not unique papers**. Curves and stages overlap and must not themselves be added as distinct publications. This changes only aggregation, not retrieval or screening decisions.

S1–S3 Base/U counts reconstruct one appearance per database named in the archived merged tables; the archived merged publication year is retained. Consequently these are provenance-weighted archived-corpus counts, not a new native-export audit. S4–S5 and DT stage streams use original source rows, preserving source-specific years. The script reconciles source counts and verifies every sum.

## Files
- 01: five vertically stacked S1–S5 panels, four curves each, 2000–2025.
- 02: general DT and DT+U, summed across databases, 2016–2025.
- 03: all six panels on a shared 2016–2025 time window.
- S1 to S5: each stage as a standalone figure.
- All figures: PDF (LaTeX), SVG (editable), PNG (preview).
- annual_summed_counts.csv: component source counts, sum and year status; earlier/later years are retained where available.
- summary_2016_2025.csv: common-window totals for auditing.
- validation.json: source hashes, reconciliation and missing-year information.

## Interpretation limits
The four stage curves come from historical queries that are not fully harmonized. Base+DT is therefore not guaranteed to be a subset of the archived Base corpus. These figures describe the available retrievals, not comparative prevalence or a final harmonized bibliometric result. General DT uses singular/plural OR; general DT+U uses the previous singular phrase AND uncertainty. The general U term is narrower than the stage U vocabulary.

The year 2026 is incomplete and is omitted from all figures; 2027 indexed records remain in CSV but are not plotted. General DT starts in 2016 because five IEEE records before 2016 are not disaggregated by year. No missing early IEEE values were invented as zero. WoS default year facets were used: their sum reconciles to all 37,609 results. Final-year-only facets omit 1,046 Early Access records and are retained in the parent directory as a sensitivity check.

## Reproduce
Run `python outputs/Manuscript/temporal_trends/code/build_summed_figures.py` from the research workspace root with matplotlib installed and the source corpora at the paths listed in validation.json. The script writes the CSVs, figures, checks and this report. A standalone replot script is supplied to redraw figures directly from the delivered annual CSV.

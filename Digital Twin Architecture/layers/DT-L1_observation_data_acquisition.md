# DT-L1 — Observation & Data Acquisition

## Status
Working scaffold — not yet analyzed in detail.

## Core question
What observations are needed to characterize buildings and their context with sufficient quality for downstream S1–S5 analyses?

## Candidate input families
- satellite imagery
- aerial imagery
- street-level imagery
- LiDAR / point clouds
- photogrammetry / UAV
- cadastral data
- building registries
- BIM / design documents
- permits / renovation records
- on-site surveys
- material inspections
- environmental/contextual datasets

## To define
- minimum metadata
- spatial grain and coverage
- temporal validity
- data quality and provenance
- measurement/classification uncertainty
- validation strategy
- update frequency
- triggers for additional observation
- outputs needed by S1–S5

## Uncertainty analysis
To be completed layer by layer.


## Output contract to Material Decision Profile

DT-L1 is successful only if its observations constrain one or more downstream material-decision variables, such as:
- material identification;
- material quantity;
- quality/state;
- component accessibility/separability;
- age/renovation history;
- release timing.

Every observation should carry provenance, spatial/temporal validity and uncertainty.

## Feedback trigger

If DT-L5 identifies a decision bottleneck caused by missing or uncertain physical evidence, DT-L1 should support targeted reacquisition—inspection, imagery, records, scan or sampling—rather than indiscriminate collection of more data.

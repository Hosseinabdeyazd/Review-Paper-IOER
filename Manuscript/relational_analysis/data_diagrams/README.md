# Diagrams computed from coded article data

**These four diagrams are outputs of aggregation, network construction and exact-set analysis. No proposed architecture connections enter them.** They reuse the existing semantic codes; they do not introduce new article classifications or claim a new full-text reading.

[Four-page PDF](Data_Derived_Diagrams.pdf) · [SVG gallery with edge hover labels](gallery.html) · [Persian interpretation](REPORT_FA.md)

## What each mark means

| Diagram | Input and calculation | Visual mark | Evidence unit |
|---|---|---|---|
| D01: boundary–continuity alluvial | Group included records by `(context, continuity_code)` | Ribbon width = number of assessments in that group | 23 publication–context assessments from 20 publications |
| D02: stage–function network | Keep R codes in S1–S5; count unique publications in each `(stage, function)` pair | Edge width = supporting publications; node area increases with its distinct publication count | Nine records with domain-stage functions; three adjacent-only records excluded |
| D03: exact uncertainty configurations | For each non-review DT–U record, form the exact set of R-coded mechanisms; group identical sets | Each column = an observed set; top bar = its publication count | Ten records, each counted once, generating nine distinct sets |
| D04: uncertainty source–method associations | Join positive source and method codes **within the same paper and same context** | Bubble area = shared assessments; colour = shared assessments / all assessments carrying the source | 23 contexts; multiple codes per context, not independent cells |

The node/feature definitions were established by semantic review. Graph edges, weights, configurations and ordering are calculated from those codes. This distinction matters: computed diagrams remain conditional on the quality and scope of the underlying coding.

D01 ribbons distribute records into categories; they do not measure uncertainty moving between physical stages. D02 edges are stage/function incidence, not directed model interfaces. D03 connecting lines identify membership in the same set, not a model execution path. D04 associations are co-occurrences, not causal relationships or demonstrations of propagation. No cross-stream path is invented by joining a stage from one paper to a mechanism from another.

## Results

- D01 partitions 23 assessments into: discussion/review **2**; downstream transfer not demonstrated **5**; inputs prepared for propagation **1**; sensitivity/representation **4**; partial/incompletely documented transfer **7**; quantified output for selected uncertain inputs **4**. S3→S4 has no assessed article in this selected set and is not assigned an artificial ribbon.
- D02 contains **16 positive stage–function edges**. All positive edges are shown; no visual threshold hides small counts. Right-side nodes are ordered by their weighted average stage index to improve readability. Node and edge memberships overlap and cannot be added as distinct papers. A baseline marker area is added for readability; the count remains printed beside every node.
- D03 yields **9 exact recorded configurations among 10 method-level records**. Only one configuration is repeated (DTUM-013 and DTUM-018); the other eight appear once. This is variation in recorded mechanism sets, not evidence that nine stable architecture classes exist. Three reviews are excluded, and conceptual-only codes do not count as operationally described methods.
- D04 contains **46 positive source–method pairs among 100 possible pairs**. For example, all four contexts coded for prediction/classification error also record prediction-error diagnostics. This is a coding association, not an independent statistical finding. A method or source may appear in several cells.

## Traceability

- `S_U_boundary_continuity_edges.csv`: all 30 boundary/status cells, including zeros, with paper IDs and DOIs.
- `S_DT_stage_function_edges.csv`: all 45 stage/function pairs, including zeros, with paper IDs, aliases and DOIs.
- `DT_U_exact_configurations.csv`: each exact positive-code configuration and its supporting records.
- `DT_U_configuration_membership.csv`: one row per record with the binary mechanism vector and configuration assignment.
- `S_U_source_method_edges.csv`: all 100 source/method pairs, counts, denominators, paper IDs, DOIs and paper@context identifiers.
- `analysis_summary.json`: computed counts and SHA-256 hashes of every source file.
- `verification.json`: independent recalculation of the exported tables and source joins.

Inputs are the existing tables under `../results/`. Their DOI/version/locator fields and rationales remain authoritative. Missing positive codes are not verified absences; no independent human adjudication or study-family independence audit was added. These are selected working sets, not pooled retrieval counts or final PRISMA inclusions.

## Reproduce

Requires Python, NumPy, Matplotlib and pypdf. Keep the `results` and `data_diagrams` folders adjacent.

```text
python data_diagrams/code/build_data_diagrams.py
python data_diagrams/code/verify_data_diagrams.py
```

PDF, SVG and PNG versions are generated from the same calculations. SVG edges in D01 and D02 expose supporting IDs on hover. No graph drawing tool or image generator supplies the data.

## Separation from conceptual synthesis

The former Figures 05–06 have been moved to [`../conceptual_synthesis/`](../conceptual_synthesis/README.md). They remain proposed architecture material for discussion. They are excluded from this data-derived atlas and from the revised four-page `results/Results_Atlas.pdf`.

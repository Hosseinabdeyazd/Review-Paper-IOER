# Architecture and uncertainty-continuity extraction protocol

## Eligibility and evidence hierarchy

Screen for a building/component/material object and a concrete DT role. Classify each record as implemented twin, tested prototype, conceptual architecture, enabling method, review, incidental DT mention, or out of scope. Record the author's definition and physical-to-digital update mechanism; do not turn every BIM model or static inventory into a twin by assumption.

Use `fulltext_explicit`, `abstract_explicit`, `review_secondary`, `our_inference`, or `not_reported` for every claim. Full-text claims require DOI, page, section, figure/table/equation locator and a concise paraphrase. An abstract's omission of uncertainty is **not evidence of absence** in the article.

## Required architecture fields

1. Physical entity and scale: building, component, material batch, district; persistent IDs and parent/child relations.
2. Observation: sensors, scans, images, BIM/IFC, GIS/CityGML, records; frequency, units and provenance.
3. Integration: semantic model, ontology/knowledge graph, database, API, coordinate/time alignment and entity matching.
4. Transformation: exact input, function/model, parameters, output, units and spatial/temporal resolution.
5. Dynamics: update trigger, versioning, state estimation, lifetime/event model and scenario identity.
6. Decision: recoverability/matching, logistics, environmental accounting, ranking and feedback.
7. Verification: data comparison, validation design, uncertainty calibration, mass balance and external test scope.

## Interface-based S1–S5 coding

| Interface | Object transferred | Transformation to inspect | Uncertainty evidence to seek |
|---|---|---|---|
| S1 → S2 | Geometry, age, type, component labels, IDs | Geometry/attributes → material inventory using archetype and intensity/composition | Class probability retention, geometry error, archetype transferability, dependency of age/type/composition |
| S2 → S3 | Material amount and component identity | Stock × lifetime/event model → dated outflows | Joint quantity/timing uncertainty; inherited inventory uncertainty; component-level versus building-level demolition |
| S3 → S4 | Dated and located material batches | Outflow → recoverable supply and demand matching | Quality/contamination, recovery yield, availability time, shared scenario assumptions |
| S4 → S5 | Recovery route, displacement, transport and processing | Circular flows → impacts and alternatives | Factor uncertainty, allocation/substitution assumptions, scenario dependence, ranking stability |
| Feedback | New measurements/events/decisions | Updated state and downstream recalculation | Which prior versions are superseded; whether uncertainty is updated and propagated again |

These are **our coding questions**, not findings that every DT already implements these mechanisms.

## Distinguish five uncertainty operations

- Detection: evidence that the observed state conflicts with expectations, data quality, model consistency or domain validity.
- Quantification: a justified uncertainty representation (probability distribution, interval, ensemble, qualitative category or explicit unknown).
- Propagation: the representation is actually passed through a transformation, preserving relevant dependencies.
- Transformation: representation, target variable, units or resolution changes; describe before and after.
- Tracking: provenance links connect sources, representations, model versions, scenarios and output consequences over time.

A residual is not automatically an uncertainty distribution. A knowledge graph is not automatically probabilistic. A passport's provenance is not automatically uncertainty propagation. A sensor stream does not prove calibration. A scenario is not a probability without justification.

## Proposed additions to test, not claimed article findings

An uncertainty payload linked to the building/component/batch ID could carry `source_id`, target parameter, evidence, representation, units, time/version, dependency/correlation group, model version, scenario and validation status. Each transformation could log inherited versus newly introduced uncertainty and input/output lineage. A shared age variable should feed both archetype and lifetime calculations coherently; independent resampling can destroy that dependency. Unknowns must remain unknown where distributions cannot be justified.

Record transfer, representation change, magnitude change and decision consequences separately. Do not compare uncertainty magnitudes across different units or resolutions without a declared comparison basis. Verify whether new observations narrow uncertainty, reveal bias or increase it; updating does not necessarily reduce uncertainty.

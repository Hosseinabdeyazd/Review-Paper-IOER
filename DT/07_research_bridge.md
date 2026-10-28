# From digital-twin architecture to circular built environment / MFA — the research bridge

**Key methodological principle:** first derive DT definitions, structural/functional patterns, actual coupling evidence and architecture conditions; *then* compare with material-system workflows. No paper has to instantiate S1–S5 to qualify as a DT.

## Distinguish three objects of study

1. **Digital Twin system:** defines physical counterparts, persistent digital representation, synchronization, services, users and potential action/feedback.
2. **Circular built-environment analytical chain:** a convenient cross-study analytic reference, not a DT definition or set of five mandatory layers:
   - **S1** observation and building characterization;
   - **S2** building component/material stock;
   - **S3** stock dynamics, renovation/demolition, dynamic MFA;
   - **S4** reuse/recovery/recycling and supply–demand;
   - **S5** environmental impact assessment / LCA.
3. **Digital thread + uncertainty continuity:** identity/semantic/temporal provenance and the fate of assumptions/distributions across interfaces. Whether a specific DT already supports this is an empirical review question.

## Crosswalk — only candidate relations; seek empirical edges

| Circular-system function | Candidate DT entities/data | Candidate services / inter-model edges | Observed physical update | Decision and stakeholder | What to code for uncertainty |
|---|---|---|---|---|---|
| S1 building observation | building ID, footprint, height, age, typology, imagery, survey, permits | GeoAI / classifiers / BIM-GIS mapping → building class/attributes | survey update, building permit, measured geometry | planners, asset registry, surveyors | classification probabilities, coverage, domain shift, timestamp |
| S2 material-stock characterization | component ID, connections, assembly, material passport, density/MI factors | geometric quantity + material intensity + archetype → material quantities | inspection, material audit, as-built amendment | owners, planners, inventory custodians | hidden materials, MI choice, density distributions, conditional structure |
| S3 prospective/dynamic MFA | installation/renovation/demolition event, stock age, service-life distributions | stock quantities + service life + scenario → inflows/outflows | actual renovation/demolition and recorded quantities | municipalities, owners, waste/recycling actors | service-life, events, cohort assumptions, mass balance |
| S4 circular pathways | connection type, recovery quality, contamination, location, actor, material marketplace | released flows + quality/technical feasibility + logistics + demand → recoverable availability | pre-demolition audit, recovery yields, transactions | demolition/reuse enterprises, markets, procurement | quality/recovery yield, disassembly and market demand |
| S5 LCA environmental accounting | functional unit, unit processes, EPD, scenarios, system boundary | material/pathway quantities + LCI + transport/processing → impacts and scenarios | EPD revision, supplier technology, measured logistics | design and policy, LCA specialists | scenario/process/correlation/substitution assumptions |

The five steps are neither exhaustive nor necessarily sequential; studies may skip, nest, branch or directly couple (e.g., S2→S5). A complete DT can support one narrow purpose and still be a DT under some published definitions.

## Architectural coupling questions for the review

- **Entity continuity:** is the same component/material/event identifiable across BIM, cadastral GIS, stock model, MFA, reuse marketplace and LCA?
- **Temporal continuity:** distinguish *observation time*, *actual event time*, *state-effective time*, *scenario/forecast time* and *update time*.
- **Physical feedback:** does the reported system detect or ingest actual material replacement, audit, demolition, disposal or resale events?
- **Computational feedback:** does new evidence trigger recomputation of affected stock-flow/LCA models and update their dependency graph?
- **Circular closure:** does a reported R-strategy connect technical recoverability to actual quality, available timing/location and secondary demand? (Not the same as cyber-physical closed loop.)
- **Uncertainty continuity:** does the target model carry and use upstream probability, range and model structural choices, or does it silently collapse them? What evidence demonstrates this?

## From a single building DT to a digital city

A **city-scale material DT is not a literal merger of all building twins**. Three patterns need empirical evaluation:
- **Centralized material stock twin:** city-level registry links buildings and aggregates to stock/flows, possibly without individual autonomous building DTs.
- **Hierarchical multi-scale DT:** nested building → district → city entities with explicit aggregation / disaggregation rules, authoritative IDs and version mappings.
- **Federated ecosystem:** heterogeneous municipal registers, building-owner DTs, recycling logistics, reuse marketplaces and environmental inventories exchange minimally sufficient data through governed semantic interfaces. Ownership and access may remain distributed.

No pattern is automatically superior; compare by **decision scope, temporal refresh, spatial coverage, information loss, stakeholder authority and quality of evidence**.

## Mapping Georg's questions to review dimensions

| Georg's aspect | Where captured |
|---|---|
| Definition of DT, relevant processes, operational/strategic stakeholders | D1 and D2; source definitions / user and decision edges |
| Spatial/system boundaries; temporal scenarios | D2; entity and time semantics; granularity and temporal architecture |
| MFA methods, typologies, BIM, GIS, digital/geoinformatics models | D3; modelling services and integration edge type |
| Material-flow / circularity indicators, R-strategies, material/civil features | D3; material entities and quantitative functions |
| AI role and implementation languages | D3; tool function and reported stack |
| Elements, components, mechanical connections, physical dimensions | Physical entity graph and S2/S4 crosswalk |
| Anthropogenic/natural resource supply vs demand | Material resource graph, markets, logistics, prospective availability |

## Candidate architecture–function–evidence outputs

1. **Definition evidence map**, separating source definitions, minimum criteria, optional features and dissenting views.
2. **Topology catalogue**, coding physically evidenced open/human/automated loops distinctly from model execution links; HPRT/LTDS as additional component patterns.
3. **Architecture–Function–Evidence matrix**, reported vs implemented vs validated vs not assessed, not a capability wish list.
4. **Interface and uncertainty handoff map**, based on review-coded edges with explicit denominators.
5. **Evidence-derived design requirements**, tied to concrete failure modes, decisions and scales rather than to invented performance improvements.

## Priority direct sources and earlier project materials

- Abdelrahman et al. (2025), DOI 10.1016/j.buildenv.2025.112748, PDF pp. 8–15 for definitions and HPRT/LTDS.
- Geremicca et al. (2026), DOI 10.1016/j.enbuild.2026.117332, PDF pp. 4–14, 18–19 for architecture, MFA/LCA and event updates.
- Geremicca & Bilec (2024), DOI 10.1016/j.scs.2024.105445, PDF pp. 1–4, 14–15 for city-scale UM/DT.
- De Wolf et al. (2024), DOI 10.1038/s44296-024-00034-8, publisher abstract for D5 flow.
- Malihi (2026), DOI 10.1016/j.dte.2026.100140, PDF pp. 5–11 for UQ and calibration.
- Earlier proposed (not yet source-coded/validated): [../Digital Twin Architecture/CORE_ARCHITECTURE.md](../Digital%20Twin%20Architecture/CORE_ARCHITECTURE.md), [../Digital Twin Architecture/MASTER_ARCHITECTURE_SPECIFICATION.md](../Digital%20Twin%20Architecture/MASTER_ARCHITECTURE_SPECIFICATION.md), [../Digital Twin Architecture/S1_S5_CONNECTION_MATRIX.md](../Digital%20Twin%20Architecture/S1_S5_CONNECTION_MATRIX.md).

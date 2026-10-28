# Architecture and coupling taxonomy — candidate coding scheme v0.1

**Status:** hypothesis-generating framework; **not** an empirically derived DT architecture. Its purpose is to extract and compare *reported* nodes, relations and functions rather than to fit papers into a presupposed stack.

## A. Keep distinct what literature distinguishes

Abdelrahman et al. (2025, *Building and Environment* 274, 112748, PDF §3.2 and §4.1, pp. 8–14) distinguish:
- **five generalized component families:** Data; Analysis & Services; Infrastructure; Interface; System Governance (Table 3, p. 8);
- **two empirically identified component-pattern families:**
  - **HPRT — High-Performance Real-Time**: correlated real-time, large-data, simulation/AI/ML and compute-oriented components;
  - **LTDS — Long-Term Decision Support**: correlated data representation, validation, visualization, policy and decision-oriented components suited to building, architecture and urban planning contexts.

**Coding caveats:** their statistical associations do not prove a necessary-and-sufficient definition. HPRT/LTDS describe *patterns of components and typical use cases*, not mutually exclusive topology classes; a system can combine capabilities. Real-time synchronization and AI/ML are not universal requirements for long-horizon material flows.

Davila Delgado & Oyedele (2021, DOI 10.1016/j.aei.2021.101332) distinguish **structural models** (conceptual, system architecture, data) and **functional models** (process, communication). Report six process families: DT creation, synchronisation, asset monitoring, prognosis/simulation, optimal operations, optimised design. Do not conflate process with layer.

Geremicca et al. (2026, DOI 10.1016/j.enbuild.2026.117332, PDF pp. 4–7) use four **architecture design decisions**: Outcome, Scope, Virtual Representation, Data Interconnections. They are not four sequential software layers.

Kosse et al. (2025, DOI 10.1016/j.aei.2025.103483) propose semantic modular architecture with AAS, ICDD, linked data, submodels, ontologies, and interfaces; this is **one implemented technical pattern**, not a universal definition.

## B. Five orthogonal architectural dimensions proposed for extraction

| Dimension | What to extract (candidate options) | What must be evidenced |
|---|---|---|
| **1. Coupling topology** | Physical→Digital observation; Digital→human decision; Human→physical action; Automated actuation; physical re-observation; model–model link | Actual source/target, direction, channel, trigger and performed vs proposed status |
| **2. Organizational topology** | Centralized repository; modular services; hierarchical nested assets; federated systems; multi-twin ecosystem | Data ownership, sharing boundary, APIs/identifiers, consistent cross-system state |
| **3. Temporal architecture** | Static baseline; periodic update; event-driven update; streaming; asynchronous multirate synchronization; forward scenario | Observation time, effective time, model valid time, event trigger, update latency |
| **4. Spatial and entity granularity** | Component/material → building → block → neighbourhood → city → region; cross-scale aggregation | Stable identifiers, geometry, aggregation mapping, boundary consistency |
| **5. Trust and propagation** | Provenance, versioning, semantic consistency, validation, calibration, uncertainty encoding, covariance/dependency handling | Concrete measures, logs, tests, propagated distributions, benchmark, decision tolerance |

These axes overlap by design: **a federated LTDS architecture can have event-driven updates and human-mediated feedback**, and a single asset may host both streaming operations and long-run stock modelling.

## C. Graph representation for systematic extraction

For study k, code a **directed typed multigraph** G_k=(V_k,E_k). Nodes may be a physical referent, observation, data object, semantic entity, computational model, service, human actor, decision or intervention. Edges are *reported directed interactions*: observes; digitizes; maps/identifies; transforms; aggregates; supplies parameter; simulates; validates; updates; recommends; authorizes; actuates; re-observes; propagates uncertainty.

**Required edge record:** study_id; source_node_id; target_node_id; edge_type; direction; trigger/cadence; spatial level; data contract/units; physical-event link; information provenance; upstream uncertainty representation; downstream uncertainty representation; evidence page/figure; evidence status.

A drawn bidirectional arrow without evidence of both directions must be coded **claimed / not validated**; an API connection is not itself a feedback control loop.

### Two independent loop notions

- **Physical–digital loop:** real-world event → observation → digital state change → human/automated decision → documented intervention → subsequent observation. This is a **candidate process distinction**, not an assertion that all steps are necessary in every published DT definition.
- **Inter-model computational loop:** S1/S2/S3/S4/S5 and other analytic modules exchange parameters, scenarios, results and sometimes recalibration signals. These cycles can be internal to a simulation platform with **no physical feedback**.

We must record whether each loop is **open**, **human-mediated closed** or **automated closed**; "closed" refers to *observed full path*, not diagram styling.

### Descriptive open/closed-loop terminology

**Open-loop, closed-loop, feedback, hierarchy and federation are not new words invented by this research.** Candidate fine-grained codes (subject to evidence testing):

| Code | Operational candidate definition | Do **not** conclude |
|---|---|---|
| P-O | Physical-to-digital observations and predictions, no evidenced decision→physical action link | That the system cannot be a DT under every definition |
| P-H | Human decision and intervention documented, later state reconciled with new observations | That actuation is automated |
| P-A | Automated intervention and measured physical response evidenced | That uncertainty is propagated |
| C-F | Analytic models can re-run or pass feedback results / parameter corrections | That physical reality is synchronized |
| X-F | Separately owned twins share identified and semantically reconciled state | That a single city-wide source-of-truth database exists |

**Novelty audit required:** check these against control theory, Industry 4.0, urban digital twins, federated DTs and cyber-physical systems before proposing any new formal label.

## D. Built-environment domain mapping (requested by Georg)

**Physical:** building; element; component; connection/joint; material; natural/anthropogenic resource; material quality; installation/renovation/demolition events.

**Spatial:** building, block, neighbourhood, city, region; cross-scale identity, geometry, resolution and boundaries.

**Temporal:** event time, sensor time, planning horizon, replacement/service-life, scenario year, data validity and update cadence.

**MFA/circular methods:** bottom-up, top-down, hybrid, material-intensity, stock-flow consistency, continuous/dynamic MFA, recovery efficiency, R-strategies, design-for-disassembly, reuse/recycling, transportation, supply–demand matching.

**Methods & implementation:** BIM, GIS, remote sensing, GeoAI, digital models, AI/ML roles, programming languages (Python/R/SQL if reported), APIs/ontologies/data schemas, simulation methods and code availability.

**Users:** operational roles (building/asset manager, demolition/reuse/recycling operator) versus strategic roles (municipal/regional planner, policymaker, market/industry stakeholders). Record actual decision type and authority.

## E. Source and evidence audit

| Source | Evidence extracted | Known limitation |
|---|---|---|
| Abdelrahman et al. 2025 | 5 generic component families; HPRT/LTDS; BDT/UDT operational definitions | Primarily definitional/component significance, not complete observed topology |
| Davila Delgado & Oyedele 2021 | Structural versus functional model types, process families | Cross-domain extrapolation |
| Kosse et al. 2025 | Modular semantic AAS / ICDD / ontology architecture | Precast factory use case, not citywide material flows |
| Geremicca et al. 2026 | Outcome/scope/representation/interconnections; BIM–MFA–LCA; BAS / event updates | One building; no complete uncertainty-handoff quantification |
| Malihi 2026 | Lifecycle/LoD-aware calibration, data/model/integration uncertainty | Position paper, not an operational MFA case |
| De Wolf et al. 2024 | Circular D5 workflow linking reuse steps | Circular process, not a full DT architecture |

## F. Inference restrictions

- Stage S1–S5 is an *analytic route*, not five DT architectural layers.
- **Open-loop recycling** and **open-loop control** have unrelated meanings; never code them under the same category.
- **LTDS is not automatically open-loop**, and **HPRT is not automatically closed-loop**.
- **Federation is not feedback:** it describes organizational/data ownership topology, not control direction.
- Architecture existence ≠ interface quality ≠ calibrated uncertainty ≠ demonstrated improvement in circular decisions.

References: DOI 10.1016/j.buildenv.2025.112748; 10.1016/j.aei.2021.101332; 10.1016/j.aei.2025.103483; 10.1016/j.enbuild.2026.117332; 10.1016/j.dte.2026.100140; 10.1038/s44296-024-00034-8.

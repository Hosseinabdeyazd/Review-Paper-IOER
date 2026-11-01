# What lets a digital twin track uncertainty?

## Evidence basis

Initial synthesis of the complete 1,228-record IEEE export, retrieved 2026-11-01. Automated term matching covers all records; the evidence examples below were read at abstract level. This is a review framework and preliminary interpretation, not a validated reference architecture or a completed systematic full-text synthesis.

The most directly relevant example found is **Uncertainty Propagation in Hierarchical Human-Centered Digital Twins for Dependable Human-Robot Collaboration** ([DOI](https://doi.org/10.1109/CASE69030.2026.11704391), IEEE:11704391). Its abstract describes component-level aleatoric/epistemic uncertainty, assumption-consistency checks, sensitivity-based screening, and propagation in three coupled twins. This directly connects uncertainty management to hierarchical coupling. The reported conclusion about structural coupling is the authors' case-study finding, not a universal conclusion established by this review.

## Candidate architectural mechanisms

| Mechanism | What it contributes | Abstract-level evidence | What still needs full-text verification |
|---|---|---|---|
| Measurement and uncertainty enter together | Sensor values retain uncertainty and metrological traceability during fusion | [Uncertainty-aware sensor fusion](https://doi.org/10.1109/I2MTC48687.2022.9806580): modular service integrated with two IIoT testbeds; propagates input measurement uncertainty | Covariance handling, calibration chain, service payload and traceability records |
| Probabilistic state/model representation | DT stores a distribution or other uncertainty representation, enabling uncertainty-aware prediction and actions | [Bayesian DT framework](https://doi.org/10.1109/JSAC.2023.3310093): model uncertainty supports control, anomaly monitoring, data collection and counterfactual analysis | Posterior representation, assumptions, update schedule, model discrepancy |
| Observation-driven updating | New measurements revise state and/or uncertainty instead of leaving the twin static | [Vehicle-state estimation and synchronization](https://doi.org/10.1109/ITSC58415.2024.10919877): communication correction and extended Kalman estimation, simulation evaluation | Sensor/communication covariance, latency assumptions, consistency testing |
| Explicit component coupling and propagation | Tracks where uncertainty passes, changes or becomes dominant across components | [Hierarchical human-centered twins](https://doi.org/10.1109/CASE69030.2026.11704391): three coupled DTs, sensitivity and assumption checks | Actual interface variables, dependence assumptions, propagation equations and quantitative comparison |
| Graph structure connecting data, models and decisions | Makes dependencies explicit and may support uncertainty reasoning across them | [Graph formulations](https://doi.org/10.1109/SWC62898.2024.00327): multilayer combination of knowledge graphs and graphical models | Treat as conceptual from abstract; verify implemented graph and inference, not just conceptual connectivity |
| Validation and runtime monitors | Detects inconsistency or violated operating assumptions and connects detection to action | [DT runtime verification](https://doi.org/10.1109/DS-RT62209.2024.00012): TeSSLa monitors, MQTT integration and action approval/denial | Monitor semantics, false alarms, timing, uncertainty representation; MQTT alone is not propagation evidence |
| Decision service consumes uncertainty | Converts uncertainty into constraints, risks or requests for more information | [Feedrate optimization](https://doi.org/10.1109/ACCESS.2024.3384471): physics/data hybrid learns uncertainty from sensors and uses error distributions in MPC; physical machine experiments reported | Constraint calibration, dependence assumptions and which uncertainty sources are covered |
| Metrology integrated throughout the DT | Connects calibration, traceability, estimation, propagation and safety monitoring | [Metrology-driven framework](https://doi.org/10.1109/MetroInd4.0IoT69397.2026.11653119): explicitly conceptual framework with simulation-based healthcare robotics case | Do not label this operational deployment; inspect equations, calibration evidence and simulation scope |

## Proposed extraction model

The review can test a chain of **measurement plus uncertainty → probabilistic state/model → dependency-aware interfaces → propagation → checks/update → decision**. Each arrow needs its own evidence. Store an interface record containing source and destination component, transferred variable, unit, spatial/temporal support, uncertainty representation, dependence assumptions, transformation, provenance/version and validation anchor. These fields are our proposed coding model, not fields proven present in every cited system.

Three distinct evidence levels matter:

1. **Representation:** the system encodes an uncertainty object (distribution, interval, ensemble, belief or another explicit form).
2. **Continuity across an interface:** that object and its dependencies survive or are deliberately transformed between components.
3. **Decision relevance:** downstream decisions use the resulting uncertainty and assess their reliability.

A digital twin label, live sensor connection, bidirectional arrow, API, knowledge graph, or high prediction accuracy alone establishes none of all three. A knowledge graph may expose dependencies but still need a probabilistic inference/propagation layer. A synchronized state estimate may quantify physical-to-digital error without establishing uncertainty continuity across multiple models.

## Corpus-wide lexical triage

Search fields: exported title, abstract, author keywords, IEEE Terms and Mesh_Terms. Patterns and matched terms are retained in `triage_rules.json` and `IEEE_mechanism_triage_1228.csv`. Categories overlap and counts measure lexical mentions, not implemented features:

| Candidate flag | Records |
|---|---:|
| Uncertainty representation terms | 1,101 |
| State update/calibration | 177 |
| Propagation/coupling | 66 |
| Semantics/interoperability | 106 |
| Provenance/traceability | 41 |
| Validation/monitoring | 426 |
| Decision/feedback | 423 |
| Architecture/framework/interface | 682 |

629 records mention both the architecture and uncertainty term groups and form a broad reading queue. All other records remain in the corpus. These broad patterns have both false positives and false negatives and are not a relevance score, exclusion rule or prevalence estimate.

## Important distinctions found during inspection

- IEEE:11056499 (structured knowledge graph) and IEEE:11058138 (error-based framework) have promising titles but their exported abstracts describe whole edited volumes. They are leads for full-text retrieval, not evidence of specific chapter methods.
- [Trust Beyond Perfection](https://doi.org/10.1109/ICC59461.2026.11586834) describes trust evaluation from disagreement among DT services. Trust/reputation uncertainty should be coded separately from physical/model uncertainty propagation.
- [Curated Uncertainty Exchange](https://doi.org/10.1109/DCOSS-IoT69657.2026.00167) suggests an expert escalation pattern, but the abstract does not establish a functioning DT. Retain for screening; do not count it as implemented DT architecture from this evidence.
- 62 records have no DOI, 2 no abstract, and some chapter descriptions are shared at volume level. Missing fields or absent abstract detail mean **not assessed**, not absent functionality or masked/lost uncertainty.

## Next synthesis step

Retrieve full texts for the directly relevant mechanism papers, capture page/figure/equation anchors and separately code implementation and validation. Expand with DT-A and DT-P searches and Scopus/WoS before assessing coverage or novelty. In particular, the hierarchical-twin paper means a claim that nobody has studied inter-twin uncertainty propagation would already be unsupported.


# End-to-End Uncertainty Engine

## Purpose

Track where uncertainty originates, how it moves through DT-L1–DT-L5 and S1–S5, and which parameter, material, layer, or scenario dominates final circularity and environmental decision uncertainty.

The objective is not to force every source into one uncertainty taxonomy. Original terminology is retained and harmonization is separate.

---

# 1. Core distinction

## Variability
Real heterogeneity in the system, for example:
- actual differences among buildings;
- actual differences in material composition;
- spatial variation;
- temporal variation;
- differences in real service life.

## Uncertainty
Incomplete knowledge, for example:
- missing data;
- measurement error;
- classification uncertainty;
- proxy/archetype uncertainty;
- model-form uncertainty;
- future scenario uncertainty.

Representation and aggregation can suppress real variability and create uncertainty in downstream estimates.

---

# 2. Uncertainty record

Every identifiable uncertainty source should receive:

- uncertainty_source_id;
- entity ID;
- parameter ID;
- material/component ID if relevant;
- DT layer;
- S stream;
- original source terminology;
- harmonized source type;
- variability/uncertainty classification;
- epistemic/aleatory/mixed if supported;
- numerical representation;
- evidence source;
- validation evidence;
- dependency links;
- downstream affected variables.

---

# 3. DT-L1 — Observation and acquisition uncertainty

Potential sources:
- sensor measurement error;
- imagery resolution;
- point-cloud density;
- occlusion;
- hidden facades;
- inaccessible interiors;
- temporal mismatch between datasets;
- geolocation error;
- segmentation error;
- classification error;
- image-domain shift;
- missing registry data;
- outdated plans;
- incomplete BIM;
- manual survey error;
- sampling error;
- material-test measurement error.

Useful outputs:
- measurement confidence;
- coverage/completeness;
- classification probability;
- validation metrics;
- observation date;
- source-specific bias.

---

# 4. DT-L2 — Identity, integration, context, and scale uncertainty

Potential sources:
- Building ID mismatch;
- duplicate entities;
- parcel-building mismatch;
- component/material entity mismatch;
- schema mapping error;
- semantic mismatch;
- coordinate-system error;
- temporal alignment error;
- source/target spatial-grain mismatch;
- aggregation/disaggregation;
- regionalization mismatch;
- cross-region proxy use;
- unit conversion;
- missing provenance;
- version conflict.

These errors can propagate without changing the numerical value itself, so contextual validity must be tracked separately from measurement uncertainty.

---

# 5. DT-L3 — Building state and material reconstruction uncertainty

Potential sources:
- construction-period classification;
- archetype assignment;
- structural-system inference;
- hidden component inference;
- wall/roof/floor assembly inference;
- material identity;
- material-intensity distribution;
- reference-building selection;
- regional transferability of MI;
- component geometry;
- density conversion;
- quantity take-off;
- renovation-history inference;
- material condition/quality inference;
- hazardous-content inference;
- remaining-service-life inference.

Output should generally be a material-specific distribution, not only one deterministic quantity.

---

# 6. DT-L4 — Dynamics and material-flow uncertainty

Potential sources:
- building lifetime;
- component lifetime;
- renovation cycle;
- repair/replacement timing;
- demolition timing;
- building survival;
- conditional renovation;
- event probability;
- affected component fraction;
- future use conversion;
- future policy;
- future technology;
- future demand;
- release quantity;
- release quality.

Key dependencies:
- renovation probability conditional on survival;
- component replacement conditional on component age/condition;
- demolition probability dependent on location, use, policy, and economics.

---

# 7. DT-L5 — Circularity / LCA / decision uncertainty

## Circularity
- access and separability;
- connection damage;
- salvage yield;
- quality;
- contamination;
- sorting efficiency;
- process yield;
- future facility availability;
- facility capacity;
- market demand;
- temporal supply-demand match;
- transport;
- substitution ratio;
- replacement coefficient;
- recertification outcome;
- regulatory acceptance.

## LCA
- quantity;
- dataset choice;
- unit conversion;
- geographic representativeness;
- temporal representativeness;
- technology representativeness;
- service life;
- system boundary;
- allocation;
- characterization factor;
- future energy mix;
- future process efficiency.

## Decision
- objective/weights;
- risk tolerance;
- threshold choice;
- scenario set;
- missing alternatives;
- model structural uncertainty.

---

# 8. Uncertainty fate — multi-axis coding

Do not use one mutually exclusive label for the entire study or link.

For each uncertainty source and link, record separately:

## Transfer status
- preserved/transferred;
- partially transferred;
- explicitly excluded;
- unknown;
- not applicable.

## Representation change
- unchanged;
- transformed;
- aggregated;
- disaggregated;
- probabilistically updated;
- deterministic collapse;
- unknown.

## Magnitude change
- legitimately reduced;
- amplified;
- unchanged where comparable;
- incomparable;
- not assessed.

## Reporting status
- sufficient;
- partial;
- insufficient;
- absent.

Masked/lost requires evidence. Non-reporting is not evidence that uncertainty was eliminated.

---

# 9. Numerical representations

Architecture should support, as appropriate:
- empirical distributions;
- parametric distributions;
- intervals;
- confidence intervals;
- classification probabilities;
- probability mass over archetypes;
- percentiles;
- Bayesian posterior distributions;
- scenario ensembles;
- fuzzy/possibility representations if encountered;
- qualitative ordinal uncertainty when quantitative data are unavailable.

Avoid forcing a normal distribution where evidence is bounded, skewed, or multimodal.

---

# 10. Propagation methods

Potential methods:
- Monte Carlo simulation;
- Latin hypercube / stratified sampling;
- analytical error propagation;
- Bayesian updating;
- bootstrap;
- empirical resampling;
- interval propagation;
- scenario ensembles;
- polynomial/surrogate models for expensive chains.

Method choice should follow model structure and evidence availability.

---

# 11. Dependence and correlation

Important dependency examples:
- age ↔ construction technology;
- age ↔ archetype;
- height ↔ structural system;
- structural system ↔ material intensity;
- footprint/form ↔ component quantities;
- component age ↔ condition;
- building survival ↔ renovation;
- quality ↔ reuse feasibility;
- contamination ↔ recycling yield;
- process yield ↔ substitution;
- distance ↔ environmental burden/cost;
- region ↔ energy mix/LCI;
- demand ↔ effective reuse.

The engine must support conditional/joint representations. Independent sampling should be an explicit assumption, not the default.

---

# 12. Sensitivity and uncertainty-hotspot analysis

## Parameter level
Possible tools:
- local sensitivity;
- rank correlation;
- variance decomposition;
- Sobol indices;
- Morris screening;
- Shapley effects when dependencies matter.

## Material level
Questions:
- which material contributes most to final impact uncertainty?
- which material contributes most to circularity uncertainty?

## DT-layer level
Questions:
- how much uncertainty is generated/inherited in DT-L1, L2, L3, L4, L5?
- which layer is the current bottleneck for a specific decision?

## Decision level
Questions:
- which uncertainty can flip reuse vs recycling?
- probability a circular scenario outperforms the baseline;
- probability a minimum substitution/circularity target is achieved.

Impact hotspot and uncertainty hotspot must be reported separately.

---

# 13. Uncertainty hotspot cube

Target indexing:

Material
× parameter
× DT layer
× S stream
× scenario
× time
× spatial unit

Possible visual outputs:
- material × layer heatmap;
- uncertainty Sankey;
- sensitivity tornado plot;
- spatial uncertainty map;
- release-time uncertainty fan chart;
- decision-flip map.

---

# 14. Value-of-information / targeted refinement logic

When a decision is not robust:

1. identify dominant uncertainty;
2. locate its upstream source;
3. determine whether it is observable/refinable;
4. identify a feasible additional data source;
5. estimate whether refinement could change the decision;
6. update only the needed Digital Twin layer;
7. re-run downstream propagation.

Examples:
- quantity uncertainty → better geometry/BIM/inspection;
- structural-system uncertainty → structural records or targeted survey;
- material identity uncertainty → spectral/visual/material sampling;
- quality uncertainty → testing/sampling;
- timing uncertainty → permits/maintenance/demolition records;
- separability uncertainty → connection/disassembly survey;
- recovery uncertainty → facility/process data;
- substitution uncertainty → product/process-specific evidence;
- LCA uncertainty → better regional/product-specific EPD/LCI.

---

# 15. Rule for claiming uncertainty reduction

A Digital Twin capability may be described as reducing uncertainty only when:

- the uncertainty metric is defined;
- before/after values are comparable;
- the information/update mechanism is documented;
- reduction is not merely caused by deleting variability or narrowing assumptions;
- dependency changes are considered;
- evidence supports the claim.

Otherwise use more precise language:
- improved traceability;
- increased information completeness;
- transformed representation;
- reduced missingness;
- better contextual representativeness;
- unresolved effect on uncertainty magnitude.

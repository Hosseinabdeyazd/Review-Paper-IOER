
# Data Acquisition and Inference Architecture

## Purpose

Define how parameters enter the Digital Twin and how data quality/uncertainty changes when the system moves from direct observation to inference.

The system should prefer targeted progressive refinement rather than maximum-detail data collection for every building.

---

# 1. Source classes

## Authoritative / documentary
- cadastral data;
- building registry;
- permits;
- construction drawings;
- structural drawings;
- BIM;
- bills of quantities;
- product schedules;
- EPDs/product documentation;
- maintenance logs;
- refurbishment records;
- inspection reports;
- demolition/pre-demolition audits.

## Remote/mobile sensing
- satellite imagery;
- aerial imagery;
- street-level imagery;
- UAV imagery;
- LiDAR;
- mobile laser scanning;
- photogrammetry;
- thermal imagery;
- hyperspectral imagery.

## On-site
- visual survey;
- component inventory;
- dimensional survey;
- connection survey;
- material sampling;
- non-destructive testing;
- laboratory testing;
- hazardous-material survey.

## Model-inferred
- GeoAI building segmentation;
- age inference;
- use inference;
- archetype assignment;
- structural-system classification;
- facade/material classification;
- component geometry inference;
- material-intensity assignment;
- condition prediction;
- lifetime prediction.

## Contextual/external
- regional typology data;
- material databases;
- recycling/reuse facility databases;
- transport network;
- market/demand data;
- energy mix;
- waste policy/regulation;
- LCI/EPD databases.

---

# 2. Evidence-status hierarchy for any value

Every populated field should indicate one acquisition class:

- verified_direct;
- measured;
- documentary;
- remotely_observed;
- inferred_building_specific;
- inferred_archetype;
- regional_proxy;
- generic_proxy;
- scenario_assumption.

This is separate from uncertainty magnitude.

---

# 3. Geometry acquisition

Possible sources:
- cadastral footprint;
- official 3D city model;
- LiDAR;
- photogrammetry;
- BIM;
- drawings;
- manual survey.

Outputs:
- footprint;
- perimeter;
- height;
- floors;
- gross floor area;
- gross volume;
- roof geometry;
- facade areas;
- openings;
- component dimensions.

Quality fields:
- LOD;
- resolution;
- point density;
- occlusion;
- missing surfaces;
- date;
- validation metric.

---

# 4. Construction age and history

Priority sources:
1. registry / permits;
2. archival drawings;
3. historic maps/orthophotos;
4. refurbishment records;
5. visual/GeoAI inference;
6. typology proxy.

Store:
- exact year only if supported;
- otherwise period/range/distribution;
- source;
- confidence;
- major renovation years;
- use-change history;
- extensions;
- partial demolition.

Never replace an uncertain construction period with a false exact year.

---

# 5. Use / function acquisition

Potential sources:
- cadastral/municipal records;
- address/business registries;
- planning/zoning;
- field survey;
- imagery;
- GeoAI;
- floorplan/BIM.

For mixed-use buildings:
- store use by area/floor/component if possible;
- otherwise store fractions and uncertainty.

---

# 6. Structural-system acquisition

Preferred hierarchy:
1. structural BIM / engineering drawings;
2. on-site structural inspection;
3. registry / engineering archive;
4. documented building typology;
5. probabilistic inference from age + use + height + shape + region + facade/structural clues.

Output:
- structural-system probability vector when inferred;
- selected class if required by downstream model;
- classification uncertainty retained separately.

---

# 7. Envelope and visible-component acquisition

Street/UAV/aerial imagery may support:
- facade material;
- cladding;
- window count/area/frame;
- door count;
- roof cover;
- roof form;
- visible deterioration.

LiDAR/photogrammetry may support:
- component dimensions;
- facade/opening geometry;
- roof geometry.

Thermal/hyperspectral may support:
- thermal anomalies;
- material differentiation;
- moisture/condition proxies.

Critical limitation:
hidden layers, internal walls, reinforcement, insulation, adhesives, and connection details generally require documents, archetypes, inspection, or sampling.

The Digital Twin must distinguish visible/observed from inferred/verified.

---

# 8. Interior/component acquisition

Potential sources:
- BIM;
- floor plans;
- building documentation;
- indoor scans;
- indoor imagery;
- on-site inventory;
- renovation records;
- archetypes.

Target objects:
- internal walls;
- floor finishes;
- ceilings;
- doors;
- stairs;
- sanitary/kitchen fittings;
- MEP;
- structural members.

---

# 9. Material-quantity acquisition hierarchy

Preferred order:

1. verified bill of quantities / material take-off;
2. high-quality BIM with validated material assignments;
3. component geometry × verified composition;
4. drawings/CAD/PDF quantity take-off;
5. building-specific inferred component inventory;
6. archetype-specific material-intensity distribution;
7. regional/national material-intensity proxy;
8. global/generic proxy.

Each fallback step creates:
- a provenance flag;
- a transferability flag;
- a specific uncertainty record.

---

# 10. Material identity and composition acquisition

Potential sources:
- EPD/product label/passport;
- BIM/product schedule;
- construction documents;
- supplier/manufacturer data;
- imagery;
- spectroscopy/spectral data;
- material sampling;
- regional construction-period archetypes.

Output can range from:
- exact product;
- exact material;
- material family;
- unknown/mixed.

Never invent product specificity unsupported by the data.

---

# 11. Condition and quality acquisition

Potential methods:
- visual inspection;
- maintenance/repair history;
- non-destructive testing;
- structural testing;
- laboratory testing;
- product documentation;
- age/service history;
- thermal/hyperspectral/image proxies.

Outputs:
- condition grade;
- property-specific test results;
- contamination;
- residual service life;
- pathway-specific suitability;
- uncertainty.

One generic quality score is insufficient for all circular pathways.

---

# 12. Connection and disassembly acquisition

Potential sources:
- BIM/detail drawings;
- construction manuals;
- on-site inspection;
- borescope/endoscope where justified;
- deconstruction trial;
- material passport/product documentation.

Outputs:
- connection type;
- mechanical/chemical;
- reversibility;
- accessibility;
- visibility;
- number of connectors;
- tools;
- labor/time;
- damage risk;
- salvage yield.

---

# 13. Lifecycle-event acquisition

Sources:
- maintenance logs;
- building-management systems;
- permits;
- insurance/inspection records;
- renovation documentation;
- historical imagery;
- owner/manager interviews;
- statistical stock models.

Outputs:
- event history;
- event probability;
- lifetime distributions;
- renovation cycles;
- demolition probability;
- future event scenarios.

---

# 14. Circular-facility and market acquisition

Sources:
- reuse platforms;
- recycling operators;
- waste operators;
- municipal datasets;
- company databases;
- procurement platforms;
- GIS/network services;
- market reports.

Store:
- accepted materials/components;
- required quality;
- dimensions;
- capacity;
- process technology;
- yield;
- location;
- opening/availability period;
- cost/gate fee;
- demand quantity;
- demand timing.

---

# 15. LCA data acquisition

Potential sources:
- product-specific EPD;
- ÖKOBAUDAT;
- national/regional LCI databases;
- licensed databases such as ecoinvent where available;
- EPiC for Australian material coefficients;
- project-specific measurements.

Always store:
- version;
- year;
- geographic scope;
- technology scope;
- declared unit;
- system boundary;
- life-cycle modules;
- conversion factor;
- validity;
- specific/representative/generic class;
- uncertainty/data quality.

---

# 16. Progressive refinement strategy

## Tier 0 — portfolio screening
Typical inputs:
- footprint;
- height;
- rough use;
- construction period;
- broad archetype;
- coarse MI.

Use:
- city-scale screening;
- identify candidate buildings/material hotspots.

## Tier 1 — building-specific external observation
Add:
- improved 3D geometry;
- facade/opening inventory;
- roof;
- external materials;
- improved typology/structure inference.

Use:
- improve building-specific stock.

## Tier 2 — document enrichment
Add:
- plans;
- BIM;
- permits;
- renovation history;
- product schedules;
- maintenance records.

Use:
- open hidden building layers.

## Tier 3 — targeted inspection
Add:
- internal components;
- connections;
- condition;
- contamination;
- component dimensions;
- pre-demolition audit.

Use:
- circularity feasibility.

## Tier 4 — material testing
Add only where decision-sensitive:
- mechanical testing;
- composition;
- contamination lab analysis;
- durability;
- recertification evidence.

Use:
- high-confidence reuse/remanufacturing decision.

The trigger to move to a higher tier should be decision uncertainty/value of information, not a desire for maximum data completeness.

---

# 17. Adaptive feedback rule

For each decision:
1. run with currently available data;
2. decompose uncertainty;
3. identify decision-sensitive missing/uncertain parameters;
4. identify lowest-cost evidence source capable of refining them;
5. update the relevant entity/layer;
6. rerun propagation;
7. stop when decision robustness is sufficient or new information is not worth its cost.

# DT-L1 — Observation & Data Acquisition

## Status
Architecture v0.3 — detailed working specification.

## Mission
Acquire building-specific and contextual evidence that can constrain **material identity, quantity, quality, release timing and circularity feasibility**.

DT-L1 does not output unquestioned facts. It outputs **EvidenceItems** with provenance, temporal validity, spatial context, validation and uncertainty.

---

## 1. Evidence channels

### A. Geospatial base data
- cadastral footprint;
- parcel;
- address;
- coordinates;
- 2D/3D city model;
- terrain/elevation;
- administrative boundaries;
- building function/use;
- building height/volume;
- number of storeys where available.

### B. Remote sensing / GeoAI
- satellite imagery;
- aerial orthophoto;
- oblique imagery;
- street-level imagery;
- LiDAR / point cloud;
- photogrammetry/UAV;
- thermal imagery where relevant.

Potential observations:
- footprint;
- height;
- roof type/material cues;
- façade material cues;
- windows/WWR;
- storeys;
- use/typology cues;
- structural clues;
- condition/damage cues.

### C. Administrative/document evidence
- construction year;
- building use;
- permits;
- renovation/refurbishment records;
- change-of-use records;
- demolition permits;
- building-energy/asset records;
- heritage status.

### D. Design/construction documents
- BIM/IFC;
- drawings;
- sections/elevations;
- schedules;
- specifications;
- bill of quantities;
- product data;
- EPD/material-passport/DPP references;
- structural calculations;
- as-built records.

### E. Physical survey
- measured geometry;
- visual inspection;
- interior survey;
- opening-up inspection;
- component/material inventory;
- connection survey;
- pre-demolition audit.

### F. Testing
- material sampling;
- NDT;
- destructive testing;
- strength/grade verification;
- moisture/corrosion;
- hazardous-material tests;
- contamination tests.

### G. Context data
- material cadastre;
- local building typologies/MCIs;
- regional waste statistics;
- facility locations;
- process technologies;
- energy mix;
- secondary-material demand;
- regulations.

---

## 2. Mandatory metadata for every observation

- evidence_id;
- source;
- acquisition method;
- observation date;
- source version;
- object/building/component ID;
- spatial grain/coverage;
- coordinate system if spatial;
- regionalization status;
- data completeness;
- validation status;
- uncertainty/confidence;
- access/usage restrictions if relevant.

---

## 3. Quality checks

### Geometry
- topology validity;
- footprint overlap/conflict;
- height plausibility;
- floor-count consistency;
- GFA/volume consistency;
- LoD/resolution.

### Classification
- class probability vector;
- confusion/validation metrics;
- out-of-domain flag;
- image/document date.

### Documents
- as-designed vs as-built?;
- document date;
- renovation superseding document?;
- completeness;
- building-ID match.

### Inspection/testing
- sample location;
- sample representativeness;
- test method;
- uncertainty/measurement precision;
- chain of custody/provenance.

---

## 4. Evidence tiers

- E0 regional/archetype prior;
- E1 geospatial/GeoAI;
- E2 administrative record;
- E3 BIM/plan/BoQ;
- E4 inspection/audit/test;
- E5 dynamic asset/maintenance evidence.

Higher tier means more direct/specific evidence, not guaranteed lower uncertainty.

---

## 5. Output to DT-L2 / DT-L3

DT-L1 sends:
- raw evidence;
- observed geometry;
- classification probabilities;
- construction/use/history records;
- component evidence;
- material clues;
- quality/condition evidence;
- connection/separability evidence;
- hazards;
- contextual datasets.

No observation may lose its provenance on transfer.

---

## 6. Uncertainty sources

- measurement error;
- spatial resolution;
- geolocation error;
- occlusion;
- incomplete imagery;
- classification uncertainty;
- class imbalance/domain shift;
- missing/incorrect records;
- outdated documentation;
- as-designed vs as-built mismatch;
- renovation not documented;
- sampling uncertainty;
- test uncertainty;
- observer subjectivity.

---

## 7. Targeted reacquisition logic

DT-L5 may request additional evidence.

Examples:
- material quantity dominates uncertainty → retrieve plan/BIM or scan;
- wall composition uncertain → opening-up survey;
- reuse quality uncertain → condition/strength test;
- pollutant risk uncertain → targeted lab test;
- separability uncertain → connection inspection;
- age/renovation uncertain → permit/archive lookup.

The architecture should prefer **decision-relevant information gain** over indiscriminate data accumulation.

---

## 8. Success criterion

DT-L1 is successful when every downstream material-decision variable can state:
- what direct evidence exists;
- what remains inferred;
- how current/specific the evidence is;
- what uncertainty it carries;
- what additional acquisition could improve it.

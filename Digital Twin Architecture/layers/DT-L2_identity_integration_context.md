# DT-L2 — Identity, Integration & Context

## Status
Architecture v0.3 — detailed working specification.

## Mission
Create the **semantic and contextual backbone** that keeps all evidence, parameters and outputs attached to the correct building/component/material, place, time, scale and source.

---

## 1. Persistent identities

Required object IDs:
- building_id;
- component_id;
- assembly_id;
- material_batch_id;
- connection_id;
- event_id;
- flow_id;
- process_id;
- facility_id;
- demand_id;
- scenario_id;
- LCA model/result ID;
- evidence_id;
- uncertainty_id.

Crosswalk external IDs:
- cadastral IDs;
- CityGML/3D city IDs;
- BIM GUIDs;
- asset-management IDs;
- product/DPP/material-passport IDs.

---

## 2. Entity resolution

Potential conflicts:
- same building represented by different datasets;
- footprint split/merge over time;
- building extension;
- address change;
- demolition/rebuild on same parcel;
- multiple BIM versions.

Record:
- linkage confidence;
- linkage method;
- temporal validity;
- manual override if used.

---

## 3. Spatial context services

- georeferencing;
- spatial joins;
- coordinate transformation;
- building → parcel → block → district → region;
- building → nearest/feasible facility;
- building → demand node;
- building → regional material cadastre;
- route/network distance.

### Spatialization
Assign object/flow to a geographic location/unit.

### Regionalization
Select/adapt data representative of that geographic context.

These are distinct operations.

---

## 4. Scale/grain management

For each value:
- source grain;
- target grain;
- spatial coverage;
- aggregation/disaggregation rule;
- native resolution;
- information-loss flag.

Examples:
- regional MCI → building-specific estimate;
- component inventory → building material total;
- building releases → district secondary-material supply;
- national LCI factor → local process approximation.

No scale transition should be invisible.

---

## 5. Temporal context

Store separately:
- evidence observation date;
- building construction year;
- component installation year;
- renovation date;
- model reference year;
- facility/process year;
- LCI reference year;
- scenario target year.

Detect:
- data older than intervention;
- future scenario using current facility/market without assumption;
- energy-mix mismatch;
- superseded BIM/document.

---

## 6. Taxonomy/schema harmonization

Canonical mappings:
- building-use taxonomies;
- component classes;
- material groups/subgroups;
- raw-material categories;
- waste/EWC codes;
- lifecycle modules;
- pathway types;
- LCA indicators.

Store:
- original code/name;
- harmonized code;
- mapping rule;
- ambiguity.

---

## 7. Regional-context selection hierarchy

Candidate order:
1. building-specific verified data;
2. local/city data;
3. regional data;
4. national data;
5. transferred/generic data.

This is a selection hierarchy, not automatic accuracy ranking.

For transferred data record:
- source region;
- target region;
- adaptation method;
- transferability evidence;
- residual uncertainty.

---

## 8. Provenance graph

Every derived result should be traceable:

```text
evidence → transformation/model → intermediate result → downstream model → final output
```

Store model/version, parameters and execution time.

---

## 9. Interoperability targets

Architecture should be able to map:
- GIS/CityGML;
- BIM/IFC;
- material passport/DPP;
- tabular cadastre;
- LCI/EPD data;
- waste/facility datasets;
- user scenario files.

The internal schema remains stable even when external sources change.

---

## 10. Context uncertainty

Potential sources:
- wrong entity match;
- taxonomic mismatch;
- generic data used locally;
- spatial aggregation;
- temporal mismatch;
- invalid transfer of MCI;
- unit/functional-reference mismatch;
- outdated process/facility data.

Outputs:
- context-quality flag;
- representativeness status;
- mapping uncertainty;
- information-loss record.

---

## 11. Success criterion

Every value in the Material Decision Profile can answer:
**what object, where, when, at what scale, from which source, under which taxonomy/model version, and with what representativeness?**

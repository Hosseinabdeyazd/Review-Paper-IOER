# Literature Evidence Map — Digital Twin Architecture v1

## Purpose

This file records which literature families justify which parts of the architecture. It separates **source-supported requirements** from **our synthesis**.

| Evidence theme | Literature anchor | Architectural consequence |
|---|---|---|
| Material composition indicators depend on context | Schiller et al.; German/Japanese MCI work | store region, archetype, reference unit, transferability domain |
| Building sampling and MI derivation require transparent building descriptors | Vienna random-sampling study incl. Schiller | age, use, volume, dimensions, plan-based provenance |
| Archetyping needs more than age/use | Dong et al. 2026; Gillott et al. 2025 | structure, built form, geography, height, footprint/GFA, construction type |
| Component-level stock matters for reuse | Arora et al. 2020 | component entity and reuse pathway, not material mass only |
| Scalable urban observation can extract components | Arbabi et al. 2022 | façade, windows, doors, footprint, height with probabilistic outputs |
| Material stock dynamics require spatial and temporal modelling | Reis Santos et al. 2019 | DT-L4 spatial/temporal/cohort model |
| Renovation needs layered lifetimes | Liu et al. 2026 | structure/skin/space/services layers and conditional renovation |
| Material passport information must persist through lifecycle | BAMB; passport reviews | provenance, product/component ID, quality/modifications, reuse/recycling fields |
| Circularity must track quantity and quality | Hossain & Ng; Bayram & Greiff | quality, contamination, output grade, substitution |
| Recycling LCA depends on input composition and product quality | Bayram & Greiff 2023 | mixed/sorted waste, RA quality, process burden |
| Replacement coefficient needs purity, technical quality and market | Rigamonti formulation discussed by Bayram & Greiff | Q1, Q2, M and explicit substituted product |
| Open/closed loop distinction matters | CDW LCA literature; Hossain & Ng | pathway-specific scenario model |
| Disassembly/adaptability matters for reuse | ISO 20887; DfD reviews | connection, accessibility, reversibility, sequence, damage, safety |
| Material impacts need robust environmental coefficients | Crawford et al. EPiC | material-level energy/water/GHG coefficients + data quality |
| Mass does not equal impact importance | city/building stock embodied-impact studies | calculate material-specific environmental impacts |
| Regionalization ≠ spatialization | Patouillard et al. | separate fields and operations |
| Uncertainty source ≠ fate | Baustert & Benetto | source, transfer, representation, magnitude fields |
| Decision feedback can target data collection | synthesis from uncertainty + DT literature | next-best data acquisition based on dominant uncertainty |

## Named researchers requested by project owner

### Georg Schiller
Especially relevant for:
- material composition indicators;
- transferability across national/contextual settings;
- German building stocks;
- empirical building sampling/material intensities;
- bottom-up urban mining/material stock logic.

### Robert H. Crawford
Especially relevant for:
- embodied environmental impact coefficients;
- hybrid LCA/EPiC data;
- system-boundary truncation;
- integration of LCA into building design decisions.

## Important boundary

Neither Schiller's work nor Crawford's work by itself provides the complete Digital Twin architecture in this repository. The architecture is a synthesis that connects material-stock characterization, component-level urban mining, dynamics, circularity, material passports, LCA and uncertainty propagation.

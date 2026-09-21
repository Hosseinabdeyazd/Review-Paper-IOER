# Systematic Review and Evidence Map with Nested Meta-analyses

## End-to-End Uncertainty Propagation in GeoAI-Informed Urban Material-Stock and Circularity Decisions

This repository contains the reproducible search, screening, coding, analysis, and visualization workflow for a global **systematic review and evidence map with nested meta-analyses**.

The review addresses **Gap 8: end-to-end uncertainty propagation** across the full analytical chain from building observation to material and environmental decision-making:

```text
GeoAI / building observation
        ↓
Building characterization and material-stock estimation
        ↓
Stock dynamics and event timing
        ↓
Material release, recovery, and circular processing
        ↓
Embodied-impact / LCA assessment
        ↓
Planning and circularity decisions
```

The central question is not only whether uncertainty is reported at an individual modelling stage, but also whether it is preserved, reduced, amplified, transformed, masked, or lost as information moves between stages and spatial scales.

> **Project status:** Active development. The Scopus queries for **S1–S3 are currently approved**. The S4 and S5 search strategies and query strings remain **draft / not fixed** and must not be used for formal retrieval until they are reviewed and frozen.

---

## Review objectives

The project aims to:

1. map the global evidence base connecting GeoAI, building-stock characterization, material-stock modelling, stock dynamics, circularity, and embodied-impact assessment;
2. distinguish deterministic studies from studies that explicitly represent uncertainty;
3. trace uncertainty across linked analytical stages rather than treating each model independently;
4. assess how spatial aggregation and scale transitions affect uncertainty;
5. identify where uncertainty becomes unavailable or invisible before a decision is made;
6. conduct nested meta-analyses where sufficiently comparable effect-level evidence is available; and
7. develop a reproducible evidence base for robust urban-mining, circularity, and embodied-carbon decisions.

---

## Scope

The review covers studies concerning buildings, building materials, urban building stocks, and associated material flows at one or more of the following levels:

- building;
- block;
- neighbourhood;
- city;
- region; and
- multi-scale systems.

The review is global. No lower publication-year limit or primary-language restriction is imposed at the search stage.

Studies focused only on operational energy are outside the scope unless their material-stock, embodied-impact, or life-cycle branch is reported separately and can be extracted independently.

Cross-scale terms are treated primarily as extraction variables rather than mandatory search filters. This prevents the search from excluding relevant studies that perform spatial aggregation without describing it in the title, abstract, or keywords.

---

## Search-stream architecture

Five complementary evidence streams cover the end-to-end chain. Each stream is executed in two layers.

### Naming convention

| Suffix | Layer | Meaning |
|---|---|---|
| `Sx-1` | Base | Broad stream-specific search |
| `Sx-2` | Base + uncertainty | The same broad search with an additional uncertainty block |

The second layer does **not** replace the base search. The paired design retains deterministic comparator studies and makes it possible to quantify how much of the literature explicitly addresses uncertainty.

In query notation:

```text
Sx-1 = P AND stream-specific block
Sx-2 = P AND stream-specific block AND U
```

where:

- `P` = population/domain block: buildings, building materials, building stocks, and urban material stocks;
- `U` = uncertainty block: uncertainty, error, confidence, sensitivity, variability, validation, propagation, and related concepts.

### S1 — Observation / GeoAI

**Purpose:** Identify how the built environment is observed, detected, classified, segmented, or reconstructed from geospatial and remotely sensed data.

Typical topics include:

- GeoAI, machine learning, and deep learning;
- computer vision and semantic segmentation;
- satellite and aerial remote sensing;
- LiDAR, point clouds, photogrammetry, and UAV data;
- building-footprint and geometry extraction;
- building-use, age, height, roof, façade, and typology classification;
- accuracy assessment, validation, transferability, and domain shift.

```text
S1-1 = P AND O
S1-2 = P AND O AND U
```

Here, `O` is the Observation / GeoAI concept block.

### S2 — Building characterization / Material stock

**Purpose:** Identify methods used to translate building observations or archetypes into material quantities, intensities, compositions, and inventories.

Typical topics include:

- building material stock;
- material intensity coefficients;
- construction systems and material composition;
- building archetypes and typologies;
- bottom-up and top-down stock estimation;
- BIM, digital building records, and material passports;
- material inventories at building and urban scales;
- uncertainty in coefficients, classifications, geometries, and archetype assignment.

```text
S2-1 = P AND M
S2-2 = P AND M AND U
```

Here, `M` is the Material-stock concept block.

### S3 — Stock dynamics / Event timing

**Purpose:** Identify how studies represent change in the building stock and the timing of material inflows and outflows.

Typical topics include:

- dynamic stock modelling;
- construction, renovation, replacement, and demolition;
- building lifetimes and lifetime distributions;
- survival, hazard, and cohort models;
- turnover and obsolescence;
- scenario-based stock development;
- timing and magnitude of future material flows;
- temporal uncertainty and sensitivity.

```text
S3-1 = P AND T
S3-2 = P AND T AND U
```

Here, `T` is the stock-dynamics and event-timing concept block.

### S4 — Circularity / Recoverability *(Draft — not fixed)*

**Purpose:** Identify how estimated stocks and released materials are converted into technically and practically recoverable circular resources.

Typical topics include:

- urban mining;
- reuse, recycling, and recovery;
- deconstruction and selective demolition;
- recoverability and reusability;
- contamination, quality loss, and downcycling;
- sorting, processing, and circular supply;
- spatial and temporal availability of secondary materials;
- recovery rates, process yields, and circularity assumptions.

```text
S4-1 = P AND C
S4-2 = P AND C AND U
```

Here, `C` is the Circularity concept block.

### S5 — LCA / Decision *(Draft — not fixed)*

**Purpose:** Identify how material-stock and circularity evidence is translated into environmental assessment and decision support.

Typical topics include:

- embodied energy and embodied carbon;
- life-cycle assessment;
- avoided impacts and substitution benefits;
- recycling and reuse allocation;
- prospective and consequential assessment;
- circularity indicators;
- planning, policy, and investment decisions;
- sensitivity, scenario robustness, and decision uncertainty.

```text
S5-1 = P AND L
S5-2 = P AND L AND U
```

Here, `L` is the LCA and decision concept block.

---

## Databases

The preregistered search is designed for reproducible execution in:

- Scopus;
- Web of Science Core Collection;
- Compendex; and
- IEEE Xplore.

Database-specific syntax, field codes, controlled terms, export dates, result counts, and deviations from the frozen protocol will be documented for every search.

---

## Evidence units

Data extraction is organized at three linked levels:

| Level | Unit of analysis | Examples |
|---|---|---|
| Study | Publication or report | bibliographic data, geography, study design, data sources |
| Chain / link | Connection between analytical stages | GeoAI → archetype, archetype → material stock, demolition → recovery |
| Effect | Quantitative comparison or estimate | error, sensitivity, uncertainty interval, scenario difference, effect size |

This multi-level structure allows several effects or analytical links to be retained within a single study while accounting for their dependence in nested analyses.

---

## Uncertainty-propagation coding

For every eligible link in the evidence chain, uncertainty is coded as one of the following:

| Code | Interpretation |
|---|---|
| Preserved | Upstream uncertainty remains explicitly represented downstream |
| Legitimately reduced | Uncertainty decreases through additional evidence, calibration, or valid constraint |
| Amplified | Downstream processing increases uncertainty |
| Transformed | The form or metric of uncertainty changes between stages |
| Masked / lost | Upstream uncertainty is omitted, collapsed, or hidden downstream |
| Unassessed | The study does not evaluate the relevant propagation |

Additional extraction variables cover uncertainty source, representation, propagation method, validation, sensitivity analysis, spatial grain, spatial extent, temporal horizon, and decision level.

---

## Planned repository structure

```text
Review-Paper-IOER/
├── README.md
├── requirements.txt
│
├── searches/
│   ├── S1_observation_geoai/
│   │   ├── S1-1_base/
│   │   └── S1-2_base_plus_uncertainty/
│   ├── S2_material_stock/
│   │   ├── S2-1_base/
│   │   └── S2-2_base_plus_uncertainty/
│   ├── S3_stock_dynamics/
│   │   ├── S3-1_base/
│   │   └── S3-2_base_plus_uncertainty/
│   ├── S4_circularity/
│   │   ├── S4-1_base/
│   │   └── S4-2_base_plus_uncertainty/
│   └── S5_lca_decision/
│       ├── S5-1_base/
│       └── S5-2_base_plus_uncertainty/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   ├── merged/
│   ├── screened/
│   └── final/
│
├── scripts/
│   ├── 01_import/
│   ├── 02_cleaning/
│   ├── 03_deduplication/
│   ├── 04_screening/
│   ├── 05_coding/
│   ├── 06_analysis/
│   └── 07_figures/
│
├── outputs/
│   ├── figures/
│   ├── tables/
│   ├── networks/
│   └── statistics/
│
└── docs/
    ├── search_strategy.md
    ├── screening_protocol.md
    ├── coding_framework.md
    └── data_dictionary.md
```

---

## Data workflow

```text
Database exports
      ↓
Raw, immutable records
      ↓
Cleaning and field harmonization
      ↓
Cross-database deduplication
      ↓
Title/abstract screening
      ↓
Full-text eligibility assessment
      ↓
Multi-level coding
      ↓
Evidence mapping and descriptive synthesis
      ↓
Nested meta-analysis where appropriate
      ↓
Figures, tables, networks, and statistics
```

### Folder rules

- `data/raw/` stores original database exports and must not be edited manually.
- `data/cleaned/` stores standardized, database-specific records.
- `data/merged/` stores combined and deduplicated records.
- `data/screened/` stores title/abstract and full-text screening decisions.
- `data/final/` stores analysis-ready study-, link-, and effect-level datasets.
- `outputs/` contains generated products only; analytical results should be reproducible from the scripts and final coded data.
- Search strings and search logs remain separated by stream, layer, and database.

The project CSV and spreadsheet files will be added separately as each stage is finalized.

---

## Reproducibility principles

The repository follows these rules:

1. search strategies are preregistered and frozen before formal execution;
2. every database query is saved exactly as run;
3. search dates, platforms, field restrictions, and result counts are logged;
4. raw exports remain unchanged;
5. all cleaning, deduplication, coding transformations, and analyses are scripted;
6. inclusion and exclusion decisions are traceable;
7. deterministic and uncertainty-focused evidence remain distinguishable;
8. all figures and tables are generated from version-controlled code; and
9. protocol deviations are documented rather than silently incorporated.

---

## Expected outputs

The repository is intended to support:

- a PRISMA-style study-selection record;
- a global evidence map;
- bibliometric and topic-network analyses;
- study-, link-, and effect-level evidence tables;
- spatial- and temporal-scale analyses;
- uncertainty-propagation maps;
- comparisons between base and uncertainty-aware evidence;
- nested meta-analyses where evidence is sufficiently comparable;
- research-gap and future-method recommendations; and
- reproducible manuscript figures, tables, and supplementary materials.

---

## Citation

Citation information will be added after publication. Until then, please cite the repository URL and the version or commit used.

## License

A license will be specified before the public release of data and reusable code. Third-party database exports and copyrighted full texts will not be redistributed unless their licenses explicitly permit it.

## Contact

**Hossein Abdeyazdan**  
Research Associate / PhD Researcher  
TU Dresden / Leibniz Institute of Ecological Urban and Regional Development (IOER)

# Literature Evidence Base — Digital Twin Architecture

## Purpose

This file is the literature-to-architecture evidence ledger for the **Building-to-Material Decision Twin**.

It does **not** claim that any single source proposes our Digital Twin. Instead, it records which architectural requirements are supported by which research traditions and distinguishes:

- **[SRC] Source-supported** — explicitly present in a cited source;
- **[SYN] Synthesis** — integration of findings across sources;
- **[PROP] Proposed by us** — architecture or implementation decision not directly established by a source.

The literature sweep is intentionally broad and will remain a living evidence base as the systematic review grows.

---

## A. Material cadastres, building-stock material composition and Georg Schiller / IOER

### A1. Ortlepp, Gruhler & Schiller (2016)
**Material stocks in Germany's non-domestic buildings: a new quantification method.** Building Research & Information 44(8), 840–862. DOI: 10.1080/09613218.2016.1112096.

**[SRC] Architectural implications**
- material composition indicators (MCIs) are building-type dependent;
- gross/floor-space information and building-type disaggregation are key stock-model inputs;
- residential and non-residential buildings require differentiated typologies;
- building-stock information can support urban-mining and circular-economy planning.

**Architecture fields affected:** building use/type, floor area, typology, MCI source, MCI applicability, material quantity.

### A2. Ortlepp, Gruhler & Schiller (2018)
**Materials in Germany's domestic building stock: calculation model and uncertainties.** Building Research & Information 46(2), 164–178. DOI: 10.1080/09613218.2016.1264121.

**[SRC] Architectural implications**
- building age is an explicit classifier for residential material composition;
- highly specific MCIs can be associated with age-based building types;
- parameter- and model-related uncertainties must be quantified/validated;
- stock, inflow and outflow calculations belong in the same information chain.

**Architecture fields affected:** construction period, age class, MCI uncertainty, model uncertainty, validation status, stock/inflow/outflow.

### A3. Schiller, Gruhler & Ortlepp (2017)
**Continuous Material Flow Analysis Approach for Bulk Nonmetallic Mineral Building Materials Applied to the German Building Sector.** Journal of Industrial Ecology 21(3), 673–688. DOI: 10.1111/jiec.12595.

**[SRC] Architectural implications**
- a closed material loop requires linking outflows to inflows, not modelling them separately;
- quality as well as quantity controls technical recycling potential;
- process engineering, waste-management technology and building structure influence circularity;
- demolition capture, processing into secondary raw material and reintegration into new products are distinct process stages.

**Architecture fields affected:** material quality, demolition recovery, processing yield, secondary-material output quality, recycling pathway, closed-loop substitution.

### A4. Schiller et al. (2019)
**Transferability of Material Composition Indicators for Residential Buildings: A Conceptual Approach Based on a German-Japanese Comparison.** Journal of Industrial Ecology 23(4), 796–807. DOI: 10.1111/jiec.12817.

**[SRC] Architectural implications**
- MCI transfer across regions/countries is limited and context-sensitive;
- socioeconomic, cultural, technical and environmental context can affect material composition;
- harmonization of indicator definitions is needed before transfer/comparison.

**Architecture fields affected:** geographic validity, regionalization status, source context, target context, transferability evidence, harmonization method.

### A5. Schwarz, Gruhler & Schiller (2023)
**Mapping building material stocks in cities: regional material cadastres. Guideline.**

**[SRC] Architectural implications**
- material cadastres require spatially referenced building information such as area/footprint, height, volume, use and construction age/type;
- material composition indicators can be differentiated by component;
- IOER's approach distinguishes foundation, exterior wall, interior wall, ceiling/floor and roof;
- material categories can be linked from building materials to raw materials and waste categories;
- regional construction practices matter;
- grey-emission information can be associated with material stocks.

**Architecture fields affected:** geometry, use, age, construction type, component hierarchy, material taxonomy, raw-material linkage, waste-code linkage, embodied-impact factor.

### A6. IOER Material Cadastre of Buildings in Germany (2025)
**[SRC] Architectural implications**
- national 3D building models can provide building volume and function-based typology;
- typical material compositions are derived from foundations, walls, ceilings/floors and roofs;
- type-based material estimates are useful for strategic analysis but can differ from the actual composition of an individual building;
- building age is identified as a useful refinement and pollutant risk as a relevant future extension;
- detailed building-level evidence can enrich type-based cadastre values.

**Architecture fields affected:** data-evidence tier, 3D geometry, building function, typology, age, pollutant risk, archetype-vs-building-specific status.

### A7. KartAL-IV, IOER
**[SRC] Architectural implications**
- individual-building material inventories and regional material cadastres serve complementary information needs;
- expected material outputs from replacement and dismantling are relevant;
- an integrated information-management system can link building-level inventories with regional cadastres.

**[SYN] Use in our architecture**
- DT-L2 should link the selected building to regional material-cadastre priors;
- better building-specific evidence should update/override priors while preserving provenance.

### A8. INTEGRAL / CirCon4Climate, IOER
**[SRC] Architectural implications**
- circularity depends on recycling-process chains, facility locations, transport distances and processing technologies;
- regional supply-demand relations for secondary materials matter;
- pre-demolition audit is a concrete use case for material cadastres.

**Architecture fields affected:** facility, capacity, technology, transport distance, processing area, regional supply/demand, audit status.

---

## B. Geo-referenced stock-flow dynamics and component/service-life modelling

### B1. Heeren & Hellweg (2019)
**Tracking Construction Material over Space and Time: Prospective and Geo-referenced Modeling of Building Stocks and Construction Material Flows.** Journal of Industrial Ecology 23, 253–267. DOI: 10.1111/jiec.12739.

**[SRC] Architectural implications**
- 3D and geo-referenced building data can drive building-level material-stock estimation;
- future material flows can be modelled probabilistically;
- construction/refurbishment/demolition assumptions affect future flows;
- material-flow scenarios can be evaluated with LCA.

**Architecture fields affected:** 3D geometry, geolocation, material inventory, service-life/event distributions, scenario assumptions, material inflow/outflow, LCA link.

### B2. Stephan & Athanassiadis (2018)
**Towards a more circular construction sector: estimating and spatializing current and future non-structural material replacement flows to maintain urban building stocks.** Resources, Conservation and Recycling 129, 248–262. DOI: 10.1016/j.resconrec.2017.09.022.

**[SRC] Architectural implications**
- replacement flows are not limited to demolition;
- non-structural components can generate recurrent material flows;
- material/component service life and replacement timing should be spatially represented.

**Architecture fields affected:** component service life, replacement cycle, installation year, maintenance/refurbishment event, spatial release.

### B3. Goulouti et al. (2020)
**Uncertainty of building elements' service lives in building LCA & LCC: What matters?** Building and Environment 183, 106904. DOI: 10.1016/j.buildenv.2020.106904.

**[SRC] Architectural implications**
- element service life can be represented probabilistically;
- service-life uncertainty affects replacement-stage environmental results;
- the importance of service-life uncertainty differs across element types;
- global sensitivity analysis can identify dominant uncertainty contributors.

**Architecture fields affected:** reference service life, service-life distribution, replacement count, sensitivity index, uncertainty contribution.

---

## C. Building archetypes, geometry and material-intensity prediction

### C1. German non-residential LCI archetype research
**Developing non-residential building stock archetypes for LCI — a German case study of office and administration buildings.** International Journal of Life Cycle Assessment (2021).

**[SRC] Architectural implications**
- useful geometry includes base area, length, width, height, window-to-wall ratio, floor number and floor height;
- construction information includes roof/wall construction, building age, renovation state and insulation thickness;
- component-level geometry is needed for exterior walls, basement walls, windows, roof, floors and foundations.

**Architecture fields affected:** building dimensions, GFA, WWR, floor heights, component areas, insulation, wall/roof system, renovation state.

### C2. Zhang et al. (2022)
**What matters most to the material intensity coefficient of buildings? Random forest-based evidence from China.** Journal of Industrial Ecology 26(5), 1809–1823.

**[SRC] Architectural implications**
- structural system, construction year, use type and region are material-intensity predictors;
- the relative importance of predictors should be empirically evaluated rather than assumed.

**Architecture fields affected:** structure, year, use, region, feature importance, model uncertainty.

### C3. Parametric archetype literature
**[SRC] Recurrent predictors across recent material-stock work**
- height, footprint, volume, gross floor area and perimeter-to-area ratio;
- use, age, region and structural system;
- plan shape affects wall-to-floor ratios and therefore façade/window material quantities.

**[SYN] Architecture rule**
Geometry features should be retained as continuous building-specific evidence, rather than collapsing everything prematurely into a typology label.

---

## D. Material passports, digital product passports, BIM and information models

### D1. Honic et al. (2021)
**Material Passports for the end-of-life stage of buildings: Challenges and potentials.** Journal of Cleaner Production 319, 128702. DOI: 10.1016/j.jclepro.2021.128702.

**[SRC] Architectural implications**
- existing-building material passports require detailed acquisition;
- BIM-based methods can derive exact quantities when building-specific information exists;
- passports can support recycling-potential assessment.

**Architecture fields affected:** acquisition method, BIM/scan source, material quantity, recycling potential, completeness.

### D2. Heisel & Rau-Oberhuber (2020)
**Calculation and evaluation of circularity indicators for the built environment using the case studies of UMAR and Madaster.** Journal of Cleaner Production.

**[SRC] Architectural implications**
- material passports contain materials/components/products and information on quantity, quality, dimensions and location;
- building-level registration is a basis for resource management.

**Architecture fields affected:** product/component/material hierarchy, quantity, quality, dimensions, location, circularity indicator.

### D3. Kebede et al. (2024)
**A modular ontology modeling approach to developing digital product passports to promote circular economy in the built environment.** Sustainable Production and Consumption 48, 248–268. DOI: 10.1016/j.spc.2024.05.007.

**[SRC] Architectural implications**
Frequently reported DPP information includes:
- unique identifiers and product descriptions;
- function/performance and technical specifications;
- dimensions, weight, density and strength;
- bill of materials;
- design-for-disassembly information;
- BIM/digital-twin information;
- thermal properties;
- assembling/disassembling process;
- material origin/type/composition/properties;
- material mass, quality/quantity, hazards, location, provenance and material efficiency.

**[SYN] Architecture rule**
A modular ontology/knowledge-graph core is preferable to one flat building table because the information belongs to different entities and lifecycle stages.

### D4. Madaster / material-passport practice
**[SRC] Architectural implications**
Operational passports commonly track:
- quality and origin;
- location;
- disassemblability;
- circularity/environmental information;
- building/product/material hierarchy.

**Caution:** platform-specific scores are not adopted automatically as scientific ground truth.

---

## E. Deconstruction, reuse, quality and recovery

### E1. DGNB Circularity Indices
**[SRC] Architectural implications**
Future circularity is influenced by:
- pollutant load/material compatibility;
- detachability;
- material separability;
- recycling/recovery pathway.
Detachability is evaluated using connection nature, recovery effort and damage; separability considers process/tool effort, accessibility and purity/single-origin recovery.

**Architecture fields affected:** connection type, reversibility, tool/effort, accessibility, deconstruction damage, separability, material purity, pollutants, recovery route.

**Caution:** DGNB scoring factors are not adopted as universal values; the underlying variables/classes are used as evidence.

### E2. Rakhshan et al. (2020)
**Components reuse in the building sector — A systematic review.** Waste Management & Research 38(4). DOI: 10.1177/0734242X20910463.

**[SRC] Architectural implications**
- reuse depends on technical, market, regulatory, organizational and risk factors;
- permanent/composite/inaccessible connections reduce deconstruction feasibility;
- missing drawings/certificates/material characteristics increase uncertainty;
- hazardous coatings/materials affect reuse;
- deconstruction space, time and storage/logistics can matter.

**Architecture fields affected:** documentation availability, connection/access, hazards, deconstruction logistics, certification, market context.

### E3. Quality assurance for reused components
**[SRC] Recurring process**
pre-deconstruction audit → condition investigation/testing → deconstruction planning/execution → second-use design checks → product approval/authorization.

**Architecture fields affected:** audit status, visual inspection, NDT/destructive test, damage, structural/durability properties, deconstruction damage, certification/approval.

### E4. Design-for-disassembly/reuse literature
**[SRC] Recurrent variables**
- connection type and reversibility;
- adhesive/weld/mortar vs dry/bolted/screwed connections;
- accessibility;
- expected damage during removal;
- specialist tools/processes;
- remaining structural capacity and dimensional compatibility.

---

## F. LCA, environmental factors and Robert H. Crawford

### F1. Crawford, Stephan & Prideaux (2022)
**The EPiC database: Hybrid embodied environmental flow coefficients for construction materials.** Resources, Conservation and Recycling 180, 106058. DOI: 10.1016/j.resconrec.2021.106058.

**[SRC] Architectural implications**
- construction-material environmental profiles should not be represented by a context-free single number;
- coefficient type/method and system boundary matter;
- embodied energy, water and GHG can be tracked separately;
- process-system boundaries can be incomplete; hybrid coefficients address truncation.

**Architecture fields affected:** environmental factor, indicator type, LCI method, system boundary, database/version, region/year, uncertainty/completeness.

### F2. Crawford et al. (2018)
**Hybrid life cycle inventory methods — A review.** Journal of Cleaner Production 172, 1273–1288.

**[SRC] Architectural implications**
- process, input-output and hybrid inventory methods have different scopes/limitations;
- the exact LCI method must be explicit for interpretation and comparison.

**Architecture fields affected:** LCI method, truncation/completeness, source/database, method version.

### F3. Rauf & Crawford (2015)
**The effect of building and material service life on the life cycle embodied energy of an apartment building.**

**[SRC] Architectural implication**
Replacement of building materials/components over time changes embodied resource/energy demand; therefore building and component service lives should not be hidden constants.

### F4. Muñoz, Hosseini & Crawford (2023)
**Exploring the environmental assessment of circular economy in the construction industry: A scoping review.** Sustainable Production and Consumption 42, 196–210. DOI: 10.1016/j.spc.2023.09.022.

**[SRC] Architectural implications**
- CE environmental assessment uses a broad and non-uniform indicator space;
- LCA and MFA are major quantitative methods;
- circular scenarios need environmental assessment, not circularity claims alone;
- connection/disassembly, lifetime, material use, waste, energy, water, GWP and chemical/toxicity considerations recur across frameworks/tools.

**Architecture rule**
Do not collapse environmental performance and circularity into one scalar by default.

---

## G. LCA uncertainty and environmental hotspot logic

### G1. Hoxha et al. (2017)
**Influence of construction material uncertainties on residential building LCA reliability.** Journal of Cleaner Production 144, 33–47. DOI: 10.1016/j.jclepro.2016.12.068.

**[SRC] Architectural implications**
- material quantity, service life and characterization factors can be uncertain;
- the largest impact contributor need not be the largest uncertainty contributor;
- uncertainty contribution can be material-specific.

**Architecture fields affected:** quantity uncertainty, service-life uncertainty, characterization-factor uncertainty, sensitivity/uncertainty contribution.

### G2. Level(s), European Commission
**[SRC] Architectural implications**
- bill of quantities, materials and lifespans are foundational lifecycle data;
- specific lifetimes can be associated with building elements;
- deconstruction, reuse/recycling and whole-life GWP belong to the lifecycle assessment context.

**Architecture fields affected:** BoQ, component lifetime, lifecycle stage, reuse/recycling, whole-life environmental result.

---

## H. Architecture synthesis derived from the evidence

### H1. [SYN] The Digital Twin needs a shared semantic core
The sources repeatedly operate at different levels — building, component, product, material, event, process, facility and scenario. Therefore the architecture uses a linked entity graph rather than a single flat table.

### H2. [SYN] Building-level priors must be updatable
Typology/MCI data are useful when direct evidence is sparse, but individual-building composition can differ. The architecture therefore treats archetype values as priors/evidence tiers, not immutable truth.

### H3. [SYN] Circularity requires stock + state + process + destination
Material quantity alone is insufficient. Circular outcomes depend on quality, contamination, connection/separability, release timing, recovery process, logistics, market/demand and substitution.

### H4. [SYN] Uncertainty is first-class data
Every value should be allowed to carry a distribution/interval/confidence plus provenance and validation status. The system must preserve inherited uncertainty across links.

### H5. [PROP] Decision-driven reacquisition loop
When final pathway comparison is not robust, the Digital Twin should identify the dominant uncertainty and request targeted additional evidence (records, imagery, scan, inspection or testing) at the relevant layer.

### H6. [PROP] Canonical output
For every material/component batch in a selected building:
**stock → state/quality → release time → pathway-specific feasible mass → effective substitution → environmental consequence → uncertainty decomposition → next-data recommendation.**

---

## I. Evidence gaps to search next

- material-specific quality thresholds for direct reuse;
- validated contamination/pollutant rules by material and construction period;
- substitution ratios by material, product and loop type;
- process yields and quality losses for recycling technologies;
- facility acceptance criteria and capacity constraints;
- market/demand matching methods for secondary components/materials;
- correlations among building attributes and material-intensity estimates;
- validated probabilistic models for renovation/demolition timing;
- uncertainty propagation from GeoAI classification to material-stock and LCA decisions;
- building-service/MEP material inventories, which are often less complete than structural/envelope inventories.

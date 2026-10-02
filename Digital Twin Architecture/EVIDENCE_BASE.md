
# Evidence Base for the Digital Twin Architecture

## Purpose

This file is a living evidence ledger for the detailed Digital Twin architecture. It records which literature supports individual parameter families, model links, and uncertainty mechanisms.

This is not yet the final systematic-review evidence base. It is a broad evidence-driven architecture synthesis that will be updated as the review proceeds.

Important rule: the Digital Twin synthesis is our own integration. A paper is never presented as evidence for a Digital Twin unless it actually studies Digital Twins.

---

## A. Building material stock, archetypes, and material intensity

### Ortlepp, Gruhler & Schiller — Materials in Germany's domestic building stock: calculation model and uncertainties

Building Research & Information (2018), DOI 10.1080/09613218.2016.1264121.

Architecture lessons:
- classify residential building types by building age;
- derive building-type-specific material composition indicators;
- combine indicators with floor-space data to estimate stocks and flows;
- quantify parameter-related and model-related uncertainty;
- preserve limits of transferability between regions and building classes.

Supports:
construction period; building type; floor area; material composition/material intensity; parameter uncertainty; model uncertainty.

### Schiller et al. — Determining the material intensities of buildings selected by random sampling: A case study from Vienna

Journal of Industrial Ecology, DOI 10.1111/jiec.13100.

Architecture lessons:
- stratify buildings by age, use, and volume;
- derive material quantities from building documents and plans;
- document the reference dimension used for material intensity;
- use transparent sampling rather than undocumented "representative" buildings.

Supports:
building age; use; gross volume; reference building; sample design; material-intensity reference unit; drawings/plans.

### Schiller, Gruhler & Ortlepp — Continuous Material Flow Analysis Approach for Bulk Nonmetallic Mineral Building Materials Applied to the German Building Sector

Journal of Industrial Ecology (2017), DOI 10.1111/jiec.12595.

Architecture lessons:
- stocks must be linked to inflows and outflows;
- closed loops depend on quality as well as quantity;
- outflow quantity does not automatically equal substitutable secondary resource.

Supports:
stock-flow link; inflow/outflow; material quality; closed-loop matching.

### Schiller et al. — Transferability of Material Composition Indicators for Residential Buildings

Journal of Industrial Ecology, DOI 10.1111/jiec.12817.

Architecture lessons:
- material composition indicators are not automatically transferable between countries/regions;
- regional construction history and practices matter;
- a Digital Twin must store the geographic validity of material-intensity data.

Supports:
regional validity; transferability; regional typology; proxy uncertainty.

### Kleemann et al. — GIS-based Analysis of Vienna's Material Stock in Buildings

Journal of Industrial Ecology (2017), DOI 10.1111/jiec.12446.

Architecture lessons:
- combine municipal GIS with construction period and utilization;
- calculate building-level gross volume;
- assign category-specific material intensities;
- preserve spatial distribution of stocks.

Supports:
location; construction period; building use; geometry; gross volume; spatial material stock; material intensity.

### Heeren & Fishman — A database seed for a community-driven material intensity research platform

Scientific Data (2019), DOI 10.1038/s41597-019-0021-x.

Architecture lessons:
- material-intensity studies require harmonized units and descriptors;
- source/provenance and building descriptors must be stored;
- comparability requires explicit codebooks.

Supports:
MI source; MI unit; building descriptors; harmonization; provenance.

### Fishman et al. — RASMI: Global ranges of building material intensities differentiated by region, structure, and function

Scientific Data (2024), DOI 10.1038/s41597-024-03190-7.

Architecture lessons:
- material intensity should often be represented as a range/distribution rather than one deterministic value;
- region, structural construction type, and building function affect material intensity;
- material-specific distributions should be retained.

Supports:
region; structural system; function; material-specific MI distributions; uncertainty.

### Bian et al. — Enhanced material stock accounting by predicting building structures with morphological indicators

Journal of Industrial Ecology (2026), DOI 10.1007/s44498-026-00094-0.

Architecture lessons:
- structural system is a critical stock descriptor;
- structure may be inferred from morphology, age, and height when missing;
- structural classification uncertainty must propagate into stock estimates.

Supports:
building shape; age; height; structural-system probability; classification uncertainty.

### Jia & Feng — Assessing the sensitivity of material-intensity-based building stock estimates to design parameters

Journal of Industrial Ecology (2026), DOI 10.1007/s44498-026-00138-5.

Architecture lessons:
- equal gross floor area does not imply equal material stock;
- floor count, structural configuration, footprint shape, and unit/layout variables can strongly alter material quantities;
- component-based reconstruction exposes variability hidden by fixed MI approaches.

Supports:
floor count; structural configuration; footprint shape; unit count; component-based stock reconstruction.

### Dong et al. — Material intensity variability-driven archetype classification for bottom-up modelling of building material stocks and flows

Resources, Conservation & Recycling (2026), DOI 10.1016/j.resconrec.2025.108751.

Architecture lessons:
- candidate archetype variables include structural, morphological, semantic, socioeconomic, and geographic attributes;
- structure type, function, built form, topography, and seismic context can matter;
- adding variables does not automatically improve the model.

Supports:
archetype variable selection; structure; function; built form; topography; seismic zone; feature importance.

---

## B. Data acquisition and component-level reconstruction

### Ajayebi et al. — A scalable data collection, characterization, and accounting framework for urban material stocks

Journal of Industrial Ecology (2022), DOI 10.1111/jiec.13198.

Architecture lessons:
- LiDAR can provide building/component geometry;
- visual imagery can identify facade components;
- thermal/hyperspectral sensing can support material and condition inference;
- drive-by sensing can miss hidden facades;
- component-level information is more useful for circularity than bulk mass alone.

Supports:
sensor type; observation coverage; occlusion; component geometry; facade materials; windows/doors; condition; observation completeness.

### Raghu, Armeni & De Wolf — Urban-scale facade material mapping from street-view images using vision-language models for circular construction planning

Scientific Reports (2026).

Architecture lessons:
- street-level imagery can support facade-material inference;
- classification confidence and validation must be retained;
- cross-city transferability is an uncertainty source.

Supports:
facade material; image source; classification probability; validation; domain-transfer uncertainty.

### Non-residential building-stock archetype / LCI studies

Architecture lessons:
- basic attributes include use, age, area, volume, and ownership/context;
- envelope attributes include facade, window, wall, roof, and basement systems;
- building-service systems can be relevant material stocks;
- geometry includes base area, perimeter, height, floors, and floor height.

Supports:
facade type; window type; wall type; roof type; basement; perimeter; floor height; MEP systems.

---

## C. Components, material passports, and digital records

### Arora et al. — Buildings and the circular economy: Estimating urban mining, recovery and reuse potential of building components

Resources, Conservation & Recycling (2020), DOI 10.1016/j.resconrec.2019.104581.

Architecture lessons:
- represent component stocks, not only material mass;
- windows, doors, tiles, lighting, fittings, and structural components can become reusable objects;
- distinguish total stock, recoverable stock, reusable stock, and receiving demand.

Supports:
component ID; component type; recoverable quantity; reusable quantity; demand matching.

### Honic, Kovacic & Rechberger — Improving the recycling potential of buildings through Material Passports

Journal of Cleaner Production (2019), DOI 10.1016/j.jclepro.2019.01.212.

Architecture lessons:
- material passports connect embedded materials to quantities;
- recycling potential and environmental impact can be evaluated from passport data.

Supports:
material passport; material inventory; recycling potential; environmental impact.

### Honic et al. — Material Passports for the end-of-life stage of buildings

Journal of Cleaner Production (2021), DOI 10.1016/j.jclepro.2021.128702.

Architecture lessons:
- existing buildings require detailed data acquisition;
- BIM can provide detailed quantities where adequate models exist;
- end-of-life pathways should remain linked to product/component identity.

Supports:
BIM quantity; existing-building acquisition; EoL pathway; component identity.

### Çetin et al. — Data requirements and availabilities for material passports

Sustainable Production and Consumption (2023), DOI 10.1016/j.spc.2023.07.011.

Architecture lessons:
- MP design should be driven by decision users and data availability;
- critical gaps for existing buildings include composition, hazardous contents, condition, reuse potential, and recycling potential;
- AI, scanning systems, and human expertise can complement missing data.

Supports:
composition; hazardous content; condition assessment; reuse potential; recycling potential; stakeholder/data-provider.

### The Material Passport for a Circular Construction Industry — PRISMA-based systematic review

Sustainability (2026).

Architecture lessons:
- preserve building-level and material/product/component-level identity;
- useful data groups include composition, physical/chemical properties, safety, circularity, disassembly, O&M, and economic information;
- connection details, accessibility, disassembly instructions, maintenance logs, future EoL pathways, reusability, and recycling potential are repeatedly reported;
- component-specific passports should survive building dismantling.

Supports:
component identity; manufacturer/supplier; manufacturing data; material properties; hazards; contamination; circularity; disassembly; accessibility; O&M history; end-of-life value.

---

## D. Disassembly, condition, durability, and reuse quality

### Dams et al. — A circular construction evaluation framework to promote designing for disassembly and adaptability

Journal of Cleaner Production (2021), DOI 10.1016/j.jclepro.2021.128122.

Architecture lessons:
- reuse depends on simplicity, standardization, modularity, and durability;
- reversible and accessible mechanical connections support disassembly.

Supports:
modularity; standardization; connection reversibility; accessibility; durability.

### Design for Disassembly: A systematic scoping review

Sustainable Production and Consumption (2024).

Architecture lessons:
- DfD attributes include accessibility, documentation, durability, reversible/exposed connections, independence, recyclability, refurbishability, remanufacturability, reusability, and simplicity;
- service-life layer separation matters;
- deconstruction time, tools, skills, and recertification can constrain reuse.

Supports:
connection type; joint visibility; layer independence; tools; deconstruction time; skill requirement; recertification.

### Devènes, Bastien-Masse & Fivet — Reusability assessment of reinforced concrete components prior to deconstruction

Journal of Building Engineering (2024), DOI 10.1016/j.jobe.2024.108584.

Architecture lessons:
- inventory and classify components;
- record geometry, material properties, and damage;
- reuse grading depends on damage/use/intervention conditions;
- residual durability should be assessed separately.

Supports:
damage class; material properties; use class; intervention class; remaining durability; reuse grade.

---

## E. Dynamics, service life, renovation, and future release

### Santos et al. — Dynamic Assessment of Construction Materials in Urban Building Stocks: A Critical Review

Environmental Science & Technology (2019), DOI 10.1021/acs.est.9b01952.

Architecture lessons:
- distinguish spatial, evolutionary-temporal, and spatial-cohort dynamics;
- renovation dynamics are often underrepresented;
- material intensity and emission intensity can change over time.

Supports:
dynamic type; retrofit event; time-varying MI; time-varying environmental coefficient.

### Sandberg et al. — Dynamic building stock modelling: General algorithm and exemplification for Norway

Energy and Buildings (2016), DOI 10.1016/j.enbuild.2016.05.098.

Architecture lessons:
- building lifetime and renovation cycles can be represented probabilistically;
- construction, demolition, and renovation flows should be linked;
- stock dynamics should be validated against statistics.

Supports:
lifetime distribution; renovation-cycle distribution; demolition flow; stock validation.

### Liu et al. — A layered dynamic material flow framework for modeling building renovations

Journal of Industrial Ecology (2026), DOI 10.1007/s44498-026-00164-3.

Architecture lessons:
- buildings should be treated as systems of components/layers with different lifetimes;
- structure, skin, space, and services may follow separate renewal cycles;
- renovation probability should be conditional on building survival;
- layer/cohort-specific material intensities are preferable when available.

Supports:
building layer; component lifetime; conditional renovation; cohort MI; renovation release.

---

## F. Spatial circularity, facilities, supply-demand, and logistics

### Zhang, Gruhler & Schiller — A review of spatial characteristics influencing circular economy in the built environment

Environmental Science and Pollution Research (2023), DOI 10.1007/s11356-023-26326-5.

Architecture lessons:
- circularity is conditioned by place, not only intrinsic material properties;
- relevant spatial variables include building/population density, construction/demolition dynamics, secondary supply/demand, transport distance, terrain, road access, land availability, facility availability, and landfill capacity;
- recycling rate alone does not guarantee high-quality substitution.

Supports:
building density; population density; construction activity; secondary supply; demand; facility distance; road access; terrain; on-site sorting space; landfill capacity; recycling quality.

---

## G. LCA, environmental coefficients, and material-level impacts

### Crawford, Stephan & Prideaux — The EPiC database: Hybrid embodied environmental flow coefficients for construction materials

Resources, Conservation & Recycling (2022), DOI 10.1016/j.resconrec.2021.106058.

Architecture lessons:
- environmental coefficients should be stored at material/product level with explicit system boundaries;
- embodied energy, water, and greenhouse-gas coefficients can be linked to material quantities;
- completeness and background-inventory assumptions matter.

Supports:
LCA dataset; coefficient; declared unit; system boundary; embodied energy; embodied water; GHG.

### Pei, Biljecki & Stouffs — Techniques and tools for integrating building material stock analysis and LCA at the urban scale

Building and Environment (2024), DOI 10.1016/j.buildenv.2024.111741.

Architecture lessons:
- material-stock and LCA representations must be compatible;
- spatial and temporal stock evolution should remain connected to impact assessment.

Supports:
stock-LCA mapping; material-to-LCI mapping; spatiotemporal LCA.

### Hoxha et al. — Influence of construction material uncertainties on residential building LCA reliability

Journal of Cleaner Production (2017), DOI 10.1016/j.jclepro.2016.12.068.

Architecture lessons:
- relevant material-input uncertainties include quantity, density, service life, and characterization/environmental coefficients;
- the materials contributing most to impact may differ from those contributing most to uncertainty.

Supports:
quantity uncertainty; density; service-life uncertainty; impact-coefficient uncertainty; uncertainty contribution.

### Häfliger et al. — Buildings environmental impacts' sensitivity related to LCA modelling choices of construction materials

Journal of Cleaner Production (2017), DOI 10.1016/j.jclepro.2017.06.052.

Architecture lessons:
- database choice, system boundary, reference study period/replacement assumptions, and material modelling choices can materially affect results;
- these choices should be explicit scenario metadata.

Supports:
database choice; system boundary; replacement scenario; LCA model choice.

### ÖKOBAUDAT / EN 15804-compatible datasets

Architecture lessons:
- declared units and conversion properties must be preserved;
- dataset geography, validity, version, and product category must be tracked;
- material information may require density, area/linear/volume/mass conversion attributes.

Supports:
declared unit; conversion factor; density; surface/linear weights; thickness; dataset geography; version; validity.

### EU life-cycle GWP framework (2026/52)

Architecture lessons:
- preserve life-cycle stages A1-A5, B stages, C1-C4, and benefits/loads beyond the system boundary;
- deconstruction, transport, waste processing, and disposal remain distinguishable;
- reuse/recycling/recovery potential should be reported separately rather than silently netted into product-stage burdens;
- component scope should be explicit.

Supports:
life-cycle module; reference study period; C1 deconstruction; C2 transport; C3 processing; C4 disposal; D1 reuse/recycling/recovery.

---

## H. Circular pathways and uncertainty

### Hossain & Ng — Critical consideration of buildings' environmental impact assessment towards adoption of circular economy

Journal of Cleaner Production (2018), DOI 10.1016/j.jclepro.2018.09.120.

Architecture lessons:
- circularity should be considered across construction, renovation, and end-of-life;
- quantity loss, quality loss, and contamination matter;
- open-loop and closed-loop pathways should be distinguished;
- substitution ratio and replacement coefficient can mediate the transition from recovered material to avoided primary production;
- LCA, MFA, and design/digital tools can be integrated.

Supports:
loop type; quality loss; contamination; substitution ratio; replacement coefficient; MFA-LCA linkage.

### Patouillard et al. — Critical review and practical recommendations to integrate the spatial dimension into LCA

Journal of Cleaner Production (2018), DOI 10.1016/j.jclepro.2017.12.192.

Architecture lessons:
- spatialization and regionalization are distinct;
- source and target spatial resolutions need not match;
- aggregation can affect information and uncertainty;
- impact hotspots and uncertainty hotspots are different concepts.

Supports:
regionalization; spatialization; scale transition; spatial information loss; uncertainty hotspot.

### Baustert & Benetto — Uncertainty analysis in agent-based modelling and consequential LCA coupled models: A critical review

Journal of Cleaner Production (2017), DOI 10.1016/j.jclepro.2017.03.193.

Architecture lessons:
- understand coupling architecture before selecting propagation methods;
- uncertainty source and uncertainty fate are separate dimensions;
- transfer, representation change, and magnitude change should not be collapsed into one label.

Supports:
uncertainty source; transfer status; representation change; magnitude change; coupling direction.

---

## Evidence-status rules

Every architecture field should eventually be tagged:

- E1 — directly source-supported;
- E2 — supported by synthesis of multiple sources;
- E3 — proposed by us from the evidence;
- E4 — placeholder / not yet supported.

No field is removed merely because evidence is currently sparse. Instead, its evidence status remains explicit.

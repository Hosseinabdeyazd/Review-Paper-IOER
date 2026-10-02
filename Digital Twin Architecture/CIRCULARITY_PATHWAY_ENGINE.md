# Circularity Pathway Engine

## Purpose

This module converts a **released material/component batch** into a set of scenario-dependent circular pathways.

It does not assign one generic circularity percentage to a building.

The key object is:

> MaterialBatch × release event × location × time × pathway scenario.

---

# 1. Input gate

A released batch can only enter the pathway engine when the system has, or explicitly marks as unknown:

- material identity;
- released quantity;
- component/source;
- quality/condition;
- contamination/hazard status;
- connection/separability information;
- release time;
- location;
- uncertainty/provenance.

Unknown data are permitted, but must widen/qualify the result rather than silently default to favorable circularity.

---

# 2. Mass cascade

For each material batch:

```text
In-building stock
   ↓ event
Released mass
   ↓ accessibility
Accessible mass
   ↓ deconstruction/removal damage
Intact/removable mass
   ↓ separability/source separation
Separated mass
   ↓ contamination / quality acceptance
Technically recoverable mass
   ├── direct reuse
   ├── preparation for reuse / remanufacture
   ├── closed-loop recycling
   ├── open-loop recycling
   ├── other material recovery
   ├── energy recovery
   ├── backfilling
   └── landfill / hazardous disposal
```

Every step can carry uncertainty.

---

# 3. Stage variables

## 3.1 Accessibility gate
Inputs:
- component location;
- access constraints;
- demolition/deconstruction sequence;
- covering/encapsulation;
- hazardous-access constraints;
- equipment access.

Outputs:
- accessible fraction;
- inaccessible fraction;
- uncertainty.

## 3.2 Detachability gate
Inputs:
- connection type;
- reversible connection?;
- fasteners;
- bonding/adhesive/mortar/weld;
- tools required;
- effort;
- sequence dependencies;
- expected breakage/damage.

Outputs:
- removable intact fraction;
- damaged fraction;
- disassembly effort class.

## 3.3 Separability gate
Inputs:
- mono-material vs composite;
- layer separability;
- attachments;
- contamination by adjacent materials;
- sorting capability;
- selective deconstruction strategy.

Outputs:
- source-separated fraction;
- mixed fraction;
- purity distribution.

## 3.4 Hazard/contamination gate
Inputs:
- hazardous substances;
- coating/treatment;
- asbestos/lead/PCB/PAH/etc. risk;
- mixed contamination;
- laboratory/field evidence;
- regulatory acceptance threshold.

Outputs:
- acceptable-for-reuse fraction;
- acceptable-for-recycling fraction;
- special-treatment fraction;
- hazardous-disposal fraction.

## 3.5 Quality gate
Inputs:
- condition;
- damage;
- retained performance;
- mechanical/functional test;
- age/service history;
- moisture/corrosion/rot/fire/fatigue;
- product standard/grade;
- certification traceability.

Outputs:
- direct-reuse quality-pass fraction;
- recycling-feedstock quality;
- additional test/repair need;
- uncertainty.

---

# 4. Direct/component reuse pathway

## 4.1 Technical eligibility
Check:
- material/component remains intact;
- required functional properties retained;
- component geometry/dimensions known;
- remaining service life sufficient;
- structural capacity where applicable;
- hazards acceptable;
- connection/deconstruction feasible;
- recertification route possible where required.

## 4.2 Matching eligibility
Check:
- receiving demand exists;
- demand timing overlaps material availability;
- location/logistics feasible;
- quantity matches;
- dimensions/specification match;
- required certification/quality matches.

## 4.3 Reuse outputs
- gross reusable candidate mass;
- deconstruction loss;
- inspection/test rejection;
- repair/refurbishment loss;
- final reusable mass;
- receiving-use class;
- transport;
- storage;
- uncertainty.

**Architecture rule:** reusable potential and realized reuse are separate outputs.

---

# 5. Closed-loop recycling pathway

Definition is scenario/function specific: output is used in the same or functionally equivalent material/product system under an explicit criterion.

Required fields:
- recycling process;
- input quality;
- acceptance threshold;
- collection yield;
- sorting yield;
- processing yield;
- output grade;
- quality retention;
- virgin material displaced;
- substitution ratio;
- process energy/emissions;
- residue;
- transport;
- uncertainty.

Outputs:
- closed-loop feedstock mass;
- recycled-output mass;
- effective substituted virgin mass;
- residual/disposal mass;
- environmental consequence.

**Do not equate recycling rate with substitution ratio.**

---

# 6. Open-loop recycling pathway

Required fields:
- alternative output product/material;
- intended application;
- collection/sorting/process yield;
- quality transformation;
- downcycling/upcycling classification;
- replacement coefficient;
- displaced alternative product/material;
- functional-equivalence basis;
- market/demand;
- environmental process burden;
- uncertainty.

Outputs:
- open-loop output mass;
- effective replacement quantity;
- destination;
- environmental consequence.

---

# 7. Other pathways

## Preparation for reuse/remanufacturing
- cleaning;
- repair;
- refinishing;
- recertification;
- remanufacturing yield.

## Other material recovery
- process;
- output;
- resource displacement.

## Energy recovery
- calorific value;
- efficiency;
- energy displaced;
- emissions;
- ash/residue.

## Backfilling
- accepted material;
- displaced fill material;
- processing/transport.

## Landfill
- landfill class/type;
- hazardous/non-hazardous;
- pretreatment;
- transport;
- emissions;
- long-term assumptions.

---

# 8. Scenario pathway fractions

For each released mass, the engine may use:
- empirically observed fractions;
- policy/statistical rates;
- process-model outputs;
- probabilistic rates;
- user-specified scenario rates.

Required metadata:
- geography;
- reference year;
- material/product;
- facility/process context;
- source;
- uncertainty;
- whether rate is observed, modelled or assumed.

**No universal landfill/recycling/reuse percentage is stored as a default truth.**

---

# 9. Mass balance

For material m and event e:

```text
Released
= Direct reuse
+ Preparation/remanufacture
+ Closed-loop input
+ Open-loop input
+ Other recovery
+ Energy recovery
+ Backfill
+ Landfill
+ Hazardous disposal
+ Temporary storage
+ Unaccounted
```

Each processing route then has its own:

```text
Process input = useful output + residue + process loss
```

Diagnostics:
- negative flow → invalid;
- pathway totals > released mass → invalid;
- unaccounted mass > tolerance → flag;
- material duplicated across mutually exclusive pathways → flag.

---

# 10. Circularity output metrics

Keep metrics separate:

## Physical stock metrics
- total material stock;
- released mass;
- recovered mass.

## Reuse metrics
- technical reuse potential;
- realized/matched reuse potential;
- reuse fraction of released mass.

## Recycling metrics
- closed-loop input/output;
- open-loop input/output;
- recycling yield.

## Substitution metrics
- effective virgin displacement;
- replacement coefficient;
- substitution ratio.

## Disposal metrics
- landfill;
- hazardous disposal;
- process residues.

## Quality metrics
- retained quality;
- purity;
- damage.

## Spatial/logistical metrics
- transport distance;
- facility availability;
- demand match.

A single composite circularity index may be calculated later, but it must never replace these underlying quantities.

---

# 11. Uncertainty model

Potential uncertainty sources:
- stock quantity;
- material identity;
- quality;
- hazard status;
- connections;
- accessibility;
- damage;
- separability;
- collection yield;
- sorting yield;
- process yield;
- output quality;
- substitution;
- facility availability;
- demand;
- transport;
- regulation/technology at future target year.

For each pathway report:
- central estimate if appropriate;
- interval/distribution/qualitative confidence;
- dominant source(s);
- unassessed source(s);
- evidence tier.

---

# 12. Decision feedback

Examples:

### Case A — high quantity uncertainty
Request better geometry/BIM/material audit.

### Case B — high quality uncertainty
Request material inspection/test.

### Case C — high separability uncertainty
Request connection inspection/opening-up survey.

### Case D — high circularity-process uncertainty
Request facility/process-specific data.

### Case E — high actual-reuse uncertainty
Request demand/receiving-project matching.

### Case F — high environmental uncertainty
Request better LCI/EPD/process/transport data.

---

# 13. Material-specific rule packs

The architecture supports plug-in rule packs rather than hard-coded universal rules.

Future rule packs should be developed for:
- structural concrete / precast concrete;
- masonry/brick;
- structural steel;
- aluminium;
- timber/mass timber;
- glass/windows;
- gypsum;
- mineral wool;
- polymer insulation;
- plastics;
- ceramic tiles;
- roofing membranes/bitumen;
- services/MEP metals and equipment.

Each pack may define:
- required quality fields;
- relevant hazards;
- reusable product forms;
- testing requirements;
- process options;
- output grades;
- substitution logic;
- LCA factors;
- uncertainty model.


# Circularity Pathway Engine

## Purpose

Convert the material/component stock of a selected building into scenario-specific quantities for:

- direct reuse;
- repair/refurbishment;
- remanufacturing;
- closed-loop recycling;
- open-loop recycling;
- energy recovery;
- backfilling where relevant;
- landfill / residual disposal;

while preserving quality, location, time, uncertainty, and environmental consequences.

This is a material/component flow engine, not a single circularity score.

---

# 1. State transition

In-use material/component
→ lifecycle event
→ released stock
→ accessibility / selective removal
→ salvage
→ condition / quality / contamination gate
→ pathway allocation
→ processing / preparation
→ secondary component/material/product
→ effective substitution
→ environmental consequence
→ decision robustness

A stock can split among multiple pathways.

---

# 2. Required mass-balance logic

For material/component i, event e, scenario s:

- Q_stock = quantity currently in use;
- Q_release = quantity affected by the event;
- Q_salvaged = physically recovered without unacceptable damage;
- Q_reuse = allocated to direct reuse;
- Q_refurbish = allocated to refurbishment/remanufacturing;
- Q_closed_input = input to closed-loop recycling;
- Q_open_input = input to open-loop recycling;
- Q_energy = energy recovery input;
- Q_landfill = disposal;
- Q_loss = untracked/process/deconstruction loss.

Required accounting:

Q_release = Q_reuse + Q_refurbish + Q_closed_input + Q_open_input + Q_energy + Q_landfill + Q_loss

Process outputs may be lower than inputs because yields can be below 1.

Do not multiply independent-looking recovery factors by default. Accessibility, damage, contamination, sorting, and quality may be statistically dependent.

---

# 3. Distinguish circularity quantities

The system must not collapse the following into one "recyclable quantity":

1. total in-use stock;
2. theoretically releasable stock;
3. technically recoverable stock;
4. accessible stock;
5. salvageable stock;
6. quality-compliant stock;
7. market-feasible stock;
8. actual secondary output;
9. effective substituted primary material/product.

Each stage can introduce loss and uncertainty.

---

# 4. Release stage

Inputs:
- stock quantity;
- component/material identity;
- event type;
- affected fraction;
- event probability;
- event-time distribution;
- building/component survival;
- scenario.

Candidate release events:
- construction waste;
- maintenance;
- repair;
- replacement;
- refurbishment;
- use conversion;
- adaptive reuse;
- partial demolition;
- complete demolition.

Outputs:
- release quantity distribution;
- release-time distribution;
- affected material/component list.

---

# 5. Pre-demolition / pre-renovation audit

Capture:
- audit date;
- accessible components;
- estimated quantities;
- hazardous substances;
- contamination;
- connection types;
- component condition;
- sampling/testing performed;
- selective-demolition feasibility;
- reusable components;
- recycling candidates;
- disposal-only materials.

Audit results should update DT-L3 material/quality states before DT-L5 pathway evaluation.

---

# 6. Accessibility and selective deconstruction

Key variables:
- component location;
- physical access;
- connection type;
- reversibility;
- connection independence;
- connection visibility;
- number of connection points;
- tool requirements;
- lifting requirements;
- component mass/size;
- surrounding-component dependency;
- disassembly sequence;
- available working space;
- selective-demolition method;
- expected deconstruction damage;
- time/labor/cost/energy.

Outputs:
- accessible fraction;
- salvage yield;
- damage probability;
- salvageable quantity distribution.

---

# 7. Quality gate

For each salvaged material/component evaluate, where relevant:

- current condition;
- visible damage;
- mechanical properties;
- dimensional accuracy;
- purity;
- mixed-material contamination;
- hazardous contamination;
- corrosion/moisture/fire/fatigue damage;
- remaining service life;
- certification;
- recertification feasibility;
- regulatory acceptance;
- required cleaning/decontamination;
- required repair.

Output:
- pathway-specific eligibility.

A material may be:
- eligible for direct reuse;
- unsuitable for direct reuse but suitable for remanufacturing;
- suitable for high-quality closed-loop recycling;
- suitable only for open-loop/downcycling;
- suitable for energy recovery;
- disposal only.

Quality is therefore not one universal score.

---

# 8. Direct reuse pathway

Inputs:
- intact component quantity;
- geometry/dimensions;
- quality;
- residual service life;
- structural/functional compliance;
- connection damage;
- certification/recertification;
- demand;
- time match;
- location match;
- storage;
- transport.

Outputs:
- technically reusable quantity;
- certified/acceptable reusable quantity;
- demand-matched reusable quantity;
- effective reuse quantity;
- residual service-life distribution.

A useful limiting concept is:

effective reuse quantity = minimum of feasible supply and matched demand

but the implementation must allow probabilistic supply/demand and multiple receivers.

---

# 9. Repair, refurbishment, and remanufacturing pathway

Inputs:
- repairable fraction;
- refurbishment process;
- replacement parts;
- process yield;
- energy/material input;
- quality after processing;
- residual life after processing;
- certification.

Outputs:
- refurbished quantity;
- remanufactured quantity;
- post-process quality;
- post-process service life;
- process burden;
- reuse destination.

---

# 10. Closed-loop recycling pathway

Closed-loop is defined at the material/product-function level for the scenario; it is not a permanent building attribute.

Inputs:
- recoverable input;
- collection rate;
- sorting efficiency;
- contamination;
- processing technology;
- processing yield;
- quality retention;
- facility capacity;
- regional demand;
- transport.

Outputs:
- secondary material quantity;
- secondary material quality;
- substitution ratio;
- effective avoided primary material.

Conceptual relation:

effective closed-loop substitution = secondary output × substitution ratio

The substitution ratio must be material-, process-, quality-, market-, and scenario-specific.

---

# 11. Open-loop recycling pathway

Inputs:
- recovered material;
- downstream application;
- process yield;
- quality transformation;
- technical specification of receiving product;
- demand;
- market;
- transport;
- replacement coefficient.

Outputs:
- transformed secondary product/material;
- effective replacement of an alternative product/material;
- quality loss or gain;
- environmental consequence.

Conceptual relation:

effective open-loop substitution = open-loop output × replacement coefficient

One kilogram of open-loop output must not automatically be treated as one kilogram of virgin material avoided.

---

# 12. Energy recovery, backfilling, and landfill

Capture:
- eligible fraction;
- lower heating value if relevant;
- recovery technology;
- energy-recovery efficiency;
- substituted energy carrier if modeled;
- residues/ash;
- backfilling eligibility;
- landfill fraction;
- landfill class;
- hazardous disposal;
- landfill distance;
- long-term treatment assumptions where included in LCA.

---

# 13. Spatial feasibility

Circularity is constrained by spatial context.

Parameters can include:
- distance to reuse demand;
- distance to recycling facility;
- distance to processor;
- distance to landfill;
- road/rail access;
- local construction/demolition density;
- local material supply;
- local secondary-material demand;
- facility capacity;
- on-site sorting space;
- storage availability;
- terrain;
- landfill capacity.

Technical recyclability is not the same as actual circularity.

---

# 14. Temporal feasibility

Circular matching requires time compatibility.

Capture:
- material release year/interval;
- receiver demand year/interval;
- storage duration;
- storage capacity;
- technology availability;
- future facility capacity;
- future regulation;
- future energy mix;
- future primary/secondary demand.

A material available in 2050 cannot be matched to a 2035 demand without an explicit storage/temporal scenario.

---

# 15. Circularity outputs per material × scenario

- current stock;
- released quantity;
- salvageable quantity;
- direct-reuse quantity;
- refurbished/remanufactured quantity;
- closed-loop recycling input;
- closed-loop secondary output;
- open-loop recycling input;
- open-loop secondary output;
- energy-recovery quantity;
- backfilling quantity;
- landfill quantity;
- processing/deconstruction losses;
- effective primary-material substitution;
- effective alternative-product substitution;
- quality retained/lost;
- transport and storage requirements;
- process burdens;
- uncertainty distributions.

No summary circularity score should replace this flow accounting. If a score is later used, it must remain traceable to these quantities.

---

# 16. Uncertainty sources inside the circularity engine

- release quantity;
- release timing;
- accessibility;
- deconstruction damage;
- salvage yield;
- quality/condition;
- contamination;
- sorting efficiency;
- process yield;
- future technology;
- facility capacity;
- demand;
- transport;
- substitution ratio;
- replacement coefficient;
- regulation;
- market acceptance.

All should be material- and pathway-specific where possible.

---

# 17. Feedback to earlier Digital Twin layers

If downstream uncertainty is dominated by:

- quantity → request better geometry/BIM/material take-off;
- material identity → request targeted observation/sampling;
- structural system → request structural records/inspection;
- quality → request inspection/testing;
- connection/separability → request disassembly survey;
- timing → improve lifetime/renovation/demolition model;
- contamination → perform hazardous-material survey;
- market → update demand/facility data;
- substitution → obtain process/product-specific evidence;
- LCA → improve regional/temporal LCI/EPD match.

The Digital Twin should recommend the most valuable next information acquisition step rather than simply requesting more data.

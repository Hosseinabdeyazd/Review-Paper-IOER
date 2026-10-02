# Digital Twin ↔ S1–S5 Connection Matrix

## Principle

Digital Twin layers and S1–S5 are two different coordinate systems.

- S1–S5 describe the analytical evidence chain.
- DT-L1–DT-L5 describe capabilities required to operate and connect that chain.
- No one-to-one correspondence is assumed.

---

## Working connection matrix

| DT capability | S1 Observation / GeoAI | S2 Material Stock | S3 Dynamics | S4 Circularity | S5 LCA / Decision |
|---|---|---|---|---|---|
| DT-L1 Observation & Data Acquisition | direct | input support | event-data support | inspection / facility data | contextual / LCI inputs |
| DT-L2 Identity, Integration & Context | object linkage | material linkage | temporal linkage | flow / facility linkage | scenario / LCA linkage |
| DT-L3 State & Material Reconstruction | consumes S1 | core | initial state | quality / recoverability state | material inventory support |
| DT-L4 Dynamics & Material Flow | feedback possible | stock-to-flow | core | release / recovery flows | future scenario inputs |
| DT-L5 Circularity / LCA / Decision | requests extra evidence | requests refined stock | uses timing | core | core |

This table is conceptual and will be revised with evidence.

---

## Output dependency logic

### Material identity and quantity
Primarily depends on:
- S1 observations;
- S2 material characterization;
- DT-L2 contextualization;
- DT-L3 inference.

### Material release timing
Primarily depends on:
- S2 current stock;
- S3 lifetimes/events;
- DT-L4 dynamics.

### Circular pathway feasibility
Primarily depends on:
- material quality / condition;
- release state;
- S4 recoverability;
- DT-L5 scenario configuration.

### Effective substitution
Depends on:
- recovered quantity;
- pathway type;
- material quality;
- substitution ratio / replacement coefficient;
- processing and market assumptions.

### Environmental consequence
Depends on:
- S5 LCA;
- material flow;
- transport;
- processing;
- substitution;
- baseline choice;
- uncertainty propagated from upstream.

---

## Feedback examples

### Example A — uncertain material quantity
DT-L5 cannot distinguish scenarios robustly
→ dominant uncertainty traced to DT-L3 material quantity
→ request additional observation / inspection from DT-L1
→ update DT-L3
→ rerun DT-L4 / DT-L5.

### Example B — uncertain release year
Decision is sensitive to future electricity mix / market
→ uncertainty traced to DT-L4 timing
→ refine lifetime/event model using S3 evidence
→ rerun future scenario.

### Example C — uncertain circular route
Material quantity is known but quality/contamination is not
→ request material inspection
→ update DT-L3 quality state
→ recompute S4 pathway feasibility and S5 LCA.

---

## Key research question

The matrix will ultimately support the question:

> For each material-level decision, which Digital Twin capability and which S1–S5 evidence stream contributes most to remaining uncertainty, and what additional information would most efficiently reduce it?

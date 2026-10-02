# Uncertainty Hotspot Register

This file will track where uncertainty appears to be largest or most consequential across the Digital Twin architecture.

Hotspots are tracked at the intersection of **Digital Twin layer × material/component × analytical stream × decision variable**. A building-level uncertainty score alone is not sufficient.

No hotspot should be declared from intuition alone. Each entry must distinguish:
- uncertainty source;
- evidence;
- affected Digital Twin layer;
- affected S1–S5 stream(s);
- whether the issue concerns variability, uncertainty, or representation/aggregation;
- whether the uncertainty is quantified or only qualitatively identified;
- effect on downstream decisions.

| ID | Building/context | Material/component | DT layer | S stream(s) | Variable/process | Uncertainty source | Evidence/magnitude | Fate downstream | Decision consequence | Candidate mitigation | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | — | not yet assessed |

## Rules

1. High variability is not automatically high uncertainty.
2. High impact contribution is not automatically high uncertainty contribution.
3. Missing reporting is not evidence of zero uncertainty.
4. Aggregation may transform or mask information; do not call it reduction without evidence.
5. A finer spatial resolution is not automatically more appropriate.
6. Any claim that a Digital Twin capability reduces uncertainty must identify the mechanism and evidence.


## Candidate uncertainty families

- observation / measurement uncertainty;
- identity and linkage uncertainty;
- spatial / temporal / context mismatch;
- archetype and material-inference uncertainty;
- quantity and composition uncertainty;
- quality / condition / contamination uncertainty;
- lifetime and release-time uncertainty;
- recovery / process uncertainty;
- open-loop / closed-loop pathway uncertainty;
- substitution / replacement uncertainty;
- market / facility / transport uncertainty;
- LCA foreground/background/model-choice uncertainty;
- scenario and decision uncertainty.

## Hotspot question

For every final material profile ask:

> Which uncertainty source contributes most to uncertainty in the decision-relevant output, and which additional evidence or model improvement would reduce that uncertainty most effectively?

Do not assign a numerical contribution unless a study/model provides a defensible basis for attribution.

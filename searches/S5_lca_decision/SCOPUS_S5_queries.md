# Scopus queries — S5: LCA / Decision

**Status:** DRAFT — NOT FIXED

> **Warning:** These queries are provisional and must not be used for formal retrieval until reviewed and frozen.

## S5-1 — Base

```text
TITLE-ABS-KEY(("building stock*" OR "building material stock*" OR "urban material stock*" OR "built environment stock*" OR "building inventor*" OR "building archetype*" OR "material cadastre*" OR "resource cadastre*" OR "existing building*" OR "building portfolio*" OR "urban building*" OR "built stock*") AND ("embodied carbon" OR "embodied emission*" OR "embodied greenhouse gas*" OR "life cycle assessment" OR "life-cycle assessment" OR LCA OR "environmental impact*" OR decision* OR ranking OR priorit* OR "decision support" OR intervention* OR "carbon footprint"))
```

## S5-2 — Base + uncertainty

```text
TITLE-ABS-KEY(("building stock*" OR "building material stock*" OR "urban material stock*" OR "built environment stock*" OR "building inventor*" OR "building archetype*" OR "material cadastre*" OR "resource cadastre*" OR "existing building*" OR "building portfolio*" OR "urban building*" OR "built stock*") AND ("embodied carbon" OR "embodied emission*" OR "embodied greenhouse gas*" OR "life cycle assessment" OR "life-cycle assessment" OR LCA OR "environmental impact*" OR decision* OR ranking OR priorit* OR "decision support" OR intervention* OR "carbon footprint") AND (uncertaint* OR probabil* OR stochastic* OR Bayesian OR "Monte Carlo" OR sensitiv* OR variabil* OR calibrat* OR robust* OR "decision confidence" OR "value of information" OR "prediction interval*" OR "confidence interval*"))
```

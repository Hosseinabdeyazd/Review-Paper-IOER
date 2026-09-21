# Scopus queries — S4: Circularity / Recoverability

**Status:** DRAFT — NOT FIXED

> **Warning:** These queries are provisional and must not be used for formal retrieval until reviewed and frozen.

## S4-1 — Base

```text
TITLE-ABS-KEY(("building stock*" OR "building material stock*" OR "urban material stock*" OR "built environment stock*" OR "building inventor*" OR "building archetype*" OR "material cadastre*" OR "resource cadastre*" OR "existing building*" OR "building portfolio*" OR "urban building*" OR "built stock*") AND (reuse OR recycl* OR recover* OR deconstruction OR "urban mining" OR "secondary material*" OR "material passport*" OR matching OR logistics OR separab* OR disassembl* OR circular* OR "reverse logistics"))
```

## S4-2 — Base + uncertainty

```text
TITLE-ABS-KEY(("building stock*" OR "building material stock*" OR "urban material stock*" OR "built environment stock*" OR "building inventor*" OR "building archetype*" OR "material cadastre*" OR "resource cadastre*" OR "existing building*" OR "building portfolio*" OR "urban building*" OR "built stock*") AND (reuse OR recycl* OR recover* OR deconstruction OR "urban mining" OR "secondary material*" OR "material passport*" OR matching OR logistics OR separab* OR disassembl* OR circular* OR "reverse logistics") AND (uncertaint* OR probabil* OR stochastic* OR Bayesian OR "Monte Carlo" OR sensitiv* OR variabil* OR calibrat* OR robust* OR "decision confidence" OR "value of information" OR "prediction interval*" OR "confidence interval*"))
```

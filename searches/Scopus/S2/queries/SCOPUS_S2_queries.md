# Scopus queries — S2: Building characterization / Material stock

**Status:** APPROVED

## S2-1 — Base

```text
TITLE-ABS-KEY(("building stock*" OR "building material stock*" OR "urban material stock*" OR "built environment stock*" OR "building inventor*" OR "building archetype*" OR "material cadastre*" OR "resource cadastre*" OR "existing building*" OR "building portfolio*" OR "urban building*" OR "built stock*") AND ("material stock*" OR "material intensit*" OR "material composition" OR "material inventor*" OR archetype* OR typolog* OR "construction type*" OR "structural system*" OR "building material*" OR "material quant*" OR "component inventor*"))
```

## S2-2 — Base + uncertainty

```text
TITLE-ABS-KEY(("building stock*" OR "building material stock*" OR "urban material stock*" OR "built environment stock*" OR "building inventor*" OR "building archetype*" OR "material cadastre*" OR "resource cadastre*" OR "existing building*" OR "building portfolio*" OR "urban building*" OR "built stock*") AND ("material stock*" OR "material intensit*" OR "material composition" OR "material inventor*" OR archetype* OR typolog* OR "construction type*" OR "structural system*" OR "building material*" OR "material quant*" OR "component inventor*") AND (uncertaint* OR probabil* OR stochastic* OR Bayesian OR "Monte Carlo" OR sensitiv* OR variabil* OR calibrat* OR robust* OR "decision confidence" OR "value of information" OR "prediction interval*" OR "confidence interval*"))
```

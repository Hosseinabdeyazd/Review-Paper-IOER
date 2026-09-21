# Scopus queries — S3: Stock dynamics / Event timing

**Status:** APPROVED

## S3-1 — Base

```text
TITLE-ABS-KEY(("building stock*" OR "building material stock*" OR "urban material stock*" OR "built environment stock*" OR "building inventor*" OR "building archetype*" OR "material cadastre*" OR "resource cadastre*" OR "existing building*" OR "building portfolio*" OR "urban building*" OR "built stock*") AND (lifetime* OR lifespan* OR demolition OR renovat* OR refurbish* OR replacement OR turnover OR "stock dynamics" OR "dynamic material flow analysis" OR survival OR hazard OR "competing risk*" OR "multi-state"))
```

## S3-2 — Base + uncertainty

```text
TITLE-ABS-KEY(("building stock*" OR "building material stock*" OR "urban material stock*" OR "built environment stock*" OR "building inventor*" OR "building archetype*" OR "material cadastre*" OR "resource cadastre*" OR "existing building*" OR "building portfolio*" OR "urban building*" OR "built stock*") AND (lifetime* OR lifespan* OR demolition OR renovat* OR refurbish* OR replacement OR turnover OR "stock dynamics" OR "dynamic material flow analysis" OR survival OR hazard OR "competing risk*" OR "multi-state") AND (uncertaint* OR probabil* OR stochastic* OR Bayesian OR "Monte Carlo" OR sensitiv* OR variabil* OR calibrat* OR robust* OR "decision confidence" OR "value of information" OR "prediction interval*" OR "confidence interval*"))
```

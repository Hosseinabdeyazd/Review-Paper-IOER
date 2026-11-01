# Paper 3: full-text mechanism extraction

Caruso, Silva, Aljawhari, Nafeh and Galasso (2026), *Unveiling the environmental impact of earthquakes in Europe*, Nature Communications 17:1366. DOI: https://doi.org/10.1038/s41467-025-68120-6.

The final publisher PDF (16 pages) and Supplementary Information (5 pages) were downloaded from Nature/Springer and read completely. Main Figures 6 and 8 were also visually checked. This is AI-assisted full-text extraction, not independent human verification. Source hashes and exact local paths are in `fulltext3_extraction.json`. No GitHub upload was performed by this agent.

## Finding

The paper supports an explicit **seismic damage/repair-to-embodied-carbon uncertainty transformation**, with a material limitation: it transfers economic risk into carbon risk through a fixed proxy. It is relevant to broad S4 building repair/retention/reconstruction consequences and S5 carbon assessment. It does **not** demonstrate uncertain reclaimed-material quality, recovery yield, contamination, sorting, or secondary-material availability propagating into LCA. It also does not optimise a physical retain-versus-demolish decision. There is no demonstrated digital twin.

## Implemented chain and anchors

1. **Stochastic hazard → shaking → damage/loss.** The event-based OpenQuake calculator simulates earthquake events and ground-motion fields. Building-specific vulnerability functions combine conditional damage probabilities and consequence models. Aggregated economic losses divided by event-set duration give average annual loss; dividing by replacement cost gives AALR. Main pp5–7, “Embodied-carbon seismic risk model for European buildings”; p13, “Data sources and integration.”
2. **Material quantities → replacement carbon.** Archetype structural designs and nonstructural inventories supply component quantities. These are multiplied by average embodied-carbon factors (ECFs), with transport/construction/demolition contributions added. Per-area carbon is multiplied by exposed floor area. Main pp11–13, quantity estimation and carbon-data methods; Figure 8, p14.
3. **Loss ratio → carbon ratio.** The model assumes AAECR=AALR. Its principal calculation is component-group specific:

   `AAEC_asset = AALR_struct × REC_struct + AALR_nonstruct × REC_nonstruct`

   Asset values are summed into regional/national totals. This separation is visible in Figure 8, p14; see also p6 and p13. REC denotes replacement embodied carbon, while AAEC denotes expected annual earthquake-damage carbon.
4. **Life-cycle interpretation.** REC covers construction of a modern substitute (A1–A5), with the old building’s demolition/disposal counted under A5.1. AAEC is interpreted as recurring damage-driven B3–B5 emissions during the existing building’s life. The work is not a complete whole-life LCA and excludes operational B6–B7 from the damage metric. Figure 6 and Methods, pp9–10.

## What is uncertain, and what is fixed

The hazard/damage side is probabilistic. The main paper cites more than 3 million earthquake scenarios and explains the event-to-loss averaging. It does not provide the exact event-set duration, probability families, correlation settings, logic-tree branches or all fragility parameters; those are delegated to GEM/source models. Do not invent lognormal/normal distributions for this paper.

Material ECF variability is quantified: CoVs range 0.17–0.80, with predominant concrete/cement/hollow-clay materials below 0.35. The paper reports propagated replacement-carbon CoV close to 0.35 (p2). It does not document the numerical propagation algorithm, covariance assumptions, or a joint sampled ECF/AALR distribution for final AAEC in the main paper or supplement. The mapped outputs are annual expected values, not annual-output confidence intervals.

Component quantities are explicitly not modelled as uncertain (Discussion p9). Structural quantities use simplified gravity-load archetypes; the additional material caused by seismic design is omitted (pp11–12). Geographic variation in component quantities is also simplified. The carbon-loss proxy is fixed, without an explicit discrepancy distribution.

Post-disaster reconstruction is mapped to contemporary improved types, generally within the same broad material category; obsolete masonry can become reinforced masonry (Table 3, p11; pp2,10–11). This is a normative replacement scenario, not a stochastic recovery/retention decision.

End-of-life assumptions are particularly important for S4 interpretation (p12):

- C1 demolition emissions equal 25% of construction-activity emissions.
- Waste transport assumes 50 km plus 50% for empty returns.
- C3–C4 uses 0.013kgCO2e/kg, based on fixed 90% recovery and 10% landfill.
- A4 assumes 120 km plus 70% empty returns, with 0.053kgCO2/t-km.
- Module D is introduced as a general life-cycle concept, but no demonstrated avoided-virgin-production credit or stochastic recovered-material substitution chain is supplied.

The authors themselves note that damaged post-disaster materials may be unsuitable for recovery and that emergency landfill practices can differ substantially. Thus, the 90% recovery assumption must not be reported as an estimated recovery probability or a validated disaster recovery yield.

## Proxy validation and its limits

The supplement directly tests the economic-to-carbon approximation rather than supplying a new continental damage-to-carbon model. Read anchors: Supplement pp1–4, Tables1–2 and Figures1–2.

For a 4.00 m × 2.75 m clay-brick wall, normalised repair-cost versus carbon ratios are 0.16 versus 0.12 at DS1,0.27 versus 0.26 at DS2, and 1.00 versus 1.00 at DS3. The minor-damage proxy therefore overestimates carbon in this illustration. A low-code five-storey reinforced-concrete frame and a three-storey steel office provide further examples. The steel example has greater dispersion and uses FEMA economic-input-output environmental factors, which warrants caution about independence of the economic/environmental comparison.

The relationship is weaker at minor damage because labour, services, shoring and scaffolding contribute to costs but little carbon; severe damage requires more material replacement, aligning the two ratios more closely. These examples support plausibility, not universal validation across all 46 countries, building types and post-disaster practices.

## Results and interpretation

The exposure covers approximately 157 million buildings and 35 billion m². Estimated replacement carbon is about 14 billion tonnes CO2e; expected annual earthquake-related carbon exceeds 6.6 million tonnes CO2e. Türkiye, Italy, Romania, Greece, Spain and Bulgaria together account for roughly 90% of the latter. These are long-run risk estimates, not measured emissions from one calendar year. Main pp5–9, Table 2 and Figures3–5.

Production A1–A3 contributes at least 85% of estimated replacement carbon (p3). Consequently, material selection and damage reduction are important policy levers, but the paper does not directly calculate an optimal retrofit or circular procurement strategy.

## Extraction limits for synthesis

Use this paper as evidence of **probabilistic seismic repair/reconstruction consequences converted to S5 carbon using a cost-ratio proxy**. Keep it distinct from a **recovered-material quality/yield-to-LCA uncertainty chain**. Do not describe GIS, stock exposure or OpenQuake as a digital twin. Do not claim that component-quantity, recovery-rate, geographic ECF and proxy uncertainties were jointly propagated. Main Discussion pp9–11 expressly limits the model’s precision and calls for structure-specific damage-to-carbon models.

The final PDF is CC BY-NC-ND 4.0; retain it unchanged with attribution. This note and JSON are independently authored analysis, not an edited copy of the paper. Third-party figure conditions remain separate. The supplemental source and final PDF were saved; source-data spreadsheet and peer-review file were not needed to read the complete research article and supplement and were not analysed here.

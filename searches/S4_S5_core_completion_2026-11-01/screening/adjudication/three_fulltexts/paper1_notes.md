# Fulltext mechanism extraction — Almeida et al.

**Article:** Integrating circularity and lifecycle assessment for building renovation: A multicycle framework. DOI: 10.1016/j.jclepro.2026.148705.

**Evidence read:** complete substantive publisher-rendered text in `work/almeida_fulltext_browser.txt`: abstract, glossary, sections 1–6, Tables 1–5, rendered equations 1–5, figure captions and declarations/data availability. References were not evaluated individually. Subsequently verified the 22-page publisher PDF, visually inspecting complete pages 17–18 and Figure 12 at 250 dpi. These are fulltext findings, not independent reproduction of calculations. Figure-specific corrections below supersede the prose-only numeric interpretation.

## Main finding

The paper supplies an operational S4-to-S5 **input bridge**: functionally feasible reuse/recoverability informs the CFF share of material entering the next system. It also explicitly performs Monte Carlo propagation to circularity and environmental outputs. However, the reported integration is **shared scenario assumptions and compatible inputs**, not feeding an MCI score, or its probability distribution, into LCA. The text does not document a single joint stochastic chain in which an independently estimated S4 distribution is transferred into S5 while preserving sample identities and dependence.

The strongest defensible description is: **a shared-input circularity–LCA framework with probabilistic propagation within the circularity and CFF branches, and an explicit functional-reuse bridge; implementation details of joint cross-branch uncertainty transfer are not reported.** It should not be described as end-to-end measured-building/digital-twin uncertainty propagation.

## System, case and boundary

- Sections 3 and 4: adapted material circularity indicator MCI_RENO plus Circular Footprint Formula (CFF) environmental allocation. Inert materials are the intended domain; bricks demonstrate the method.
- Sections 4.1–4.1.2: façade of a 1970s public building in Växjö, Sweden. Functional unit is brick mass in 10 m² of façade; inventory lists 1800 kg brick/material and virgin feedstock, and 100 kg unrecovered waste. Ökobaudat 2021 supplies inventory. Original actual lifetime is later given as 54 years.
- Two consecutive lifecycles are actually evaluated. Production, end-of-life and beyond-system allocation phases A, C and D are included; use/operational phase B is excluded. Closed-loop reuse is assumed. R1=0 for initially virgin bricks and R3=0 because inert brick does not provide energy recovery.
- Baseline allocation A=0.5; incoming, outgoing and virgin quality factors each equal 1. Reference lifetime L_av=50 years; reference use U_av=0.95. Lifetime extension is assumed by mortar/construction technology, not measured as a survival distribution.
- Seven scenarios (Table 4): S1 cement/BAU (L2=0,U2=0); S2 cement (25 years,10%); S3 lime (40,50%); S4 RICS recommendation (50,50%); S5 cement (25,57%); S6 lime (40,80%); S7 PEFCR recommendation (50,97.5%). Swedish pilot evidence supports approximately 75–80% recovery for the high-reuse example. Scenario recommendations are not empirical distributions.

## Equations and transformation

Section 3.1, equations 1–2: original MCI = 1 − LFI F(X), with LFI=(V+W)/(2M), F(X)=0.9/X and X=(L/L_av)(U/U_av). MCI_actual substitutes actual lifetime and intensity. The browser rendering of the nested division in equation 2 is typographically ambiguous; use the PDF for exact mathematical layout.

Section 3.1, equation 3: MCI_RENO = MCI_actual + Σ(i=2…n)[(Li/L_av)(Ui/U_av)]. The added service terms assume equivalent function and equal weighting of service across cycles. Subsequent-cycle virgin input and unrecovered-waste terms are omitted on the assumption of negligible extra inputs/losses. The raw cumulative score can exceed 1. This is functional-service accounting, not a direct engineering reliability measure.

Section 3.1.1, equation 4: MCI_RENO_N = min[1, MCI_RENO / {1+Σ(i=2…n)(Li/L_av)}]. For two cycles, reuse, lifetime and the baseline score therefore enter a normalized nonlinear ratio. No score is then inserted into equation 5.

Sections 3.2.2–3.3, equation 5: CFF adds material, energy-recovery and disposal contributions. The material term is (1−R1)Ev + R1[A E_recycled +(1−A)Ev(Qsin/Qp)] +(1−A)R2[E_recyclingEOL − E*v(Qsout/Qp)]. Disposal is (1−R2−R3)Ed. The energy-recovery term is irrelevant for this inert case because R3=0. The avoided-virgin-production term is the principal mechanism by which greater reuse changes GWP.

Section 3.3 explicitly cautions that U2↔R2 is not a mathematical equivalence or direct conversion. U2 represents the share fit for same/equivalent-function reuse; it constrains plausible R2, the share entering a subsequent system after collection/recovery inefficiencies. Functionality should be supported by technical evidence. Table 3 step 4 reuses the reuse-potential data collected in step 2; step 6 compares the resulting circularity and impact outputs. Thus the arrow is **reuse information → plausible CFF R2**, not **MCI_RENO score → carbon**.

## What the uncertainty analysis actually reports

Section 4.2.4 and Fig. 12 describe OWSA and global probabilistic sensitivity analysis using Google Colab and **2000 Monte Carlo iterations**. Influential inputs receive probability distributions; inputs are randomly sampled for each run; circularity/GWP are recalculated, producing output distributions. The prose does not specify distribution families, numerical bounds/parameters, sampling algorithm, seed, convergence test or input covariance assumptions. Do not invent uniform/normal/triangular distributions, independence, or uncertainty ranges. Figure axes might reveal plotted ranges but those are not necessarily prescribed distribution bounds.

**Circularity branch, Fig. 12A:** S2 and S6 sample U2, L2 and MCI_actual and calculate MCI_RENO_N. Reported associations:

| Input | S2 | S6 |
|---|---:|---:|
| U2 | 0.2521 | 0.9202 |
| L2 | −0.1522 | 0.1223 |
| MCI_actual | 0.9617 | 0.3869 |

The text first describes scatterplot correlations/regression and then states accompanying Spearman plots confirm the trends. It does not clearly label the above coefficients as Pearson versus Spearman; retain this distinction rather than assigning an unverified coefficient type. The baseline score dominates low-reuse S2; recovery potential dominates high-reuse S6.

**Environmental branch, Fig. 12B:** GWP distributions are shown for all seven scenarios. Inputs discussed are R1, R2, Qsin, Qsout, Ev, ErecEOL, A, Erec and Ed. Reported global Spearman associations are R1 −0.76; R2 −0.33; Qsin +0.30; Qsout −0.26; Ev +0.19; ErecEOL −0.05; A 0.00; Erec 0.00; Ed +0.02. These are **input–output** correlations, not evidence of correlations among input variables. A separate plot evaluates impact changes from parameter 5th to 95th percentiles. Low-reuse cases have broader GWP spreads; high-reuse S6/S7 have lower/narrower spreads. Numerical output quantiles, confidence limits and ranking probabilities are not tabulated in the text.

**Joint-transfer limit:** Figure 12A and B have different parameter lists. The prose does not establish paired draws, a common U2/R2 random variable, a conditional mapping distribution, or dependence between recovery quality, yield and lifespan. Nor does it state that MCI_actual is re-derived from uncertain measured inventory in every run; it is treated as a sampled baseline score in branch A. Consequently, the paper demonstrates uncertainty in relevant S4 and S5 calculations but does not fully document an auditable cross-branch joint probability model. Independence cannot be assumed from this omission.

## Results and interpretation

Table 5 gives deterministic normalized circularity/GWP pairs: S1 (0.55,0.583); S2 (0.40,1.11); S3 (0.53,0.610); S4 (0.52,0.436); S5 (0.56,0.831); S6 (0.66,0.487); S7 (0.76,0.297). GWP is printed as CO2eq/ton/m², an unusual compound normalization; retain the reported unit pending PDF verification. S7 is about 49% below S1; S6 about 16% below S1. Some reuse options are worse than BAU, supporting the distinction between circularity and environmental performance. Avoided virgin production is the main impact mechanism.

The analysis does not establish a universal causal correlation between circularity scores and climate benefit. The authors explicitly limit findings to scenarios, allocation choices, quality and technology. Numeric input–output correlations are sensitivity summaries, not validation of causal dominance in other materials or projects.

## Reporting issues to check against PDF/figure

1. Baseline R1=0 in §4.1.2, but R1 varies and dominates environmental PSA in §4.2.4. The uncertainty distribution and justification for varying a historically virgin input are not provided in text.
2. §4.2.4 calls the quality-factor associations negative collectively but prints Qsin=+0.30. Preserve the positive number and flag the prose mismatch; the positive sign is compatible with its placement in the CFF burden expression.
3. §4.1 says detailed scenarios S1/S6, whereas §4.2.4 uses S2/S6 for circularity PSA.
4. §4.1.1 mentions a subsequent 50-year phase, while Table 4 specifies 0–50-year scenario lifetimes.
5. §4.2.1 calls S5 U2=50% in one passage, whereas Table 4 gives 57%.
6. §4.2.2 gives S7 circularity 0.80 and labels it MCI_RENO; Table 5 labels normalized score and gives 0.76, while §4.2.1 gives raw score 1.60. Prefer explicitly identified Table 5 values and do not silently reconcile.
7. §3.1.1 narrative lifetime curves rise then fall, which is not transparent from the positive additive formula unless reuse trajectories or other inputs change. No reproducible trajectory specification appears in the prose; do not infer a decay law.
8. Correlation sensitivity does not establish that nonlinear interactions were independently quantified, despite the authors' broader claim. No Sobol decomposition or interaction indices are reported.

## Demonstrated versus proposed digital extensions

Demonstrated: literature/database inputs, spreadsheet-style framework, scenario modelling and Google Colab Monte Carlo. No live sensors, digital twin, BIM inference or sequential Bayesian evidence updating is implemented.

Sections 4.3 and 5.1 propose material passports, pre-demolition audits, condition assessment, certification, BIM, RFID and IoT to improve future input quality. Digital material passports and robotic selective demolition are future research comparisons. Do not attribute a demonstrated digital-twin pipeline to this article.

## Reproducibility and extraction judgement

Data availability says data are available on request; the read text provides no executable Monte Carlo implementation or complete probability specification. The article qualifies as fulltext-demonstrated probabilistic propagation in a directly relevant material-circularity/LCA framework. For a stricter claim of **S4-estimated uncertainty transferred into S5**, code/supplementary distributions and joint sampling details remain necessary.

## PDF verification and page anchors (supersedes unverified prose values where stated)

Publisher PDF: `outputs/S4 S5 Core Review/screening/adjudication/three_fulltexts/pdfs/Almeida_2026_Multicycle_framework.pdf`. PDF page numbers and printed article pages agree (22 pages).

| Item | Printed/PDF page |
|---|---|
| Equation 1 | 4 |
| Equations 2–3 | 5 |
| Equation 4 normalization | 7 |
| Equation 5 CFF; §3.3 integration rationale begins | 9 |
| §3.4 integrated workflow | 10 |
| §§4.1.1–4.1.2 case scope/assumptions begin | 11 |
| Table 4 scenario specification | 12 |
| Table 5 deterministic results; §4.2.4 Monte Carlo description | 16 |
| Sensitivity interpretation and recommendations | 17 |
| Figure 12 entire multi-panel uncertainty figure | 18 |
| §5.1 limitations/future work and §6 conclusion | 19 |
| Data availability | 20 |

**Figure 12A, p.18:** Scatterplot axes and numeric labels are readable and conflict materially with parts of the prose/table. S2 has plotted U2 ticks approximately 0.135–0.165 (centred around 0.15), L2 ticks 23–27 years, and MCI_actual ticks 0.50–0.60. S6 has U2 ticks 0.72–0.88, L2 ticks 72–88 years, and MCI_actual ticks 0.50–0.60. These are **visible plotted tick spans**, not confirmed sampling bounds or distribution parameters. In particular, S2's plotted reuse level differs from Table 4's 0.10; S6's plotted lifespan differs from Table 4's 40 years. The cloud shapes alone cannot establish distribution families.

| Figure 12A coefficient | S2 | S6 |
|---|---:|---:|
| Scatterplot r, U2 | +0.1522 | +0.9202 |
| Scatterplot r, L2 | −0.2521 | +0.1223 |
| Scatterplot r, MCI_actual | +0.9617 | +0.3869 |
| Explicitly labelled Spearman, U2 | +0.1448 | +0.9153 |
| Explicitly labelled Spearman, L2 | −0.2310 | +0.1060 |
| Explicitly labelled Spearman, MCI_actual | +0.9603 | +0.3713 |

Thus the prose swaps S2's U2/L2 correlation magnitudes. The graph distinguishes scatterplot r from separate Spearman bars; do not call the scatter coefficients verified Spearman coefficients.

**Figure 12B, p.18:** The blue panel label specifies CFF parameter probability distribution for **S2**, while its first panel shows GWP boxplots for all seven scenarios. The next panel is an explicitly labelled global Spearman bar chart, and the third is a one-way percentile impact-range chart. The nine scatterplot r labels are those reported numerically in the prose, but the Spearman bar heights visibly differ (for example R1 is around −0.7, rather than the scatter r=−0.76; Ev is around +0.3, rather than scatter r=+0.19). Exact bar values are not printed; do not substitute eyeballed values into the structured extraction.

The negative-r=−0.05 scatter is labelled **E*v (EOL Credit)**, not ErecEOL. This is the substituted virgin production credit in the formula; the prose misidentifies it as end-of-life recycling impact. The positive Qsin r=+0.30 is visually confirmed, contradicting the prose's collective description of negative quality correlations. The GWP scatter axes use kg CO2eq/ton/m², preserving the unusual compound unit; figure verification does not resolve its physical normalization.

Visible environmental scatter tick spans: R1, R2, Qsin, Qsout and A span 0–1; Ev approximately 0.35–0.70; E*v approximately 0.4–0.7; Erec approximately 0.010–0.018; Ed approximately 0.020–0.040. Some points/axes extend past tick endpoints. These are observations of display ranges only. There is no PDF figure legend specifying distributions, truncation rules, parameter standard deviations, joint covariance, sampling identities or common U2/R2 draws. The circularity S2 U2 display is narrow around 0.15, whereas the environmental S2 R2 display spans 0–1; this is evidence against claiming an identically sampled common scalar on the basis of the published figure. It does not prove statistical independence.

**Updated judgement:** Monte Carlo propagation is demonstrated in both branches, but the figure reinforces the need to distinguish shared conceptual input mapping from a reproducibly specified joint S4-to-S5 stochastic chain. The reported scenario/parameter mismatches are substantive reproducibility limitations, not grounds to invent corrected assumptions.

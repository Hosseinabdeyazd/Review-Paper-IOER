# Noise and precision diagnostic — Methods note

Before descriptive evidence mapping, cross-stage overlap analysis, or uncertainty-propagation coding, each merged S1-S3 corpus is subjected to a reproducible noise and precision diagnostic.

The diagnostic is positioned after cross-database deduplication and before formal title/abstract screening. It does not replace screening and it does not automatically exclude records.

## Components

1. Structural consistency: verify U is a subset of B, identify residual DOI/title duplicates, inspect year anomalies, and retain provenance.
2. Stage-specific scope diagnostics: apply transparent positive-scope and candidate-noise dictionaries to title, abstract, and keywords. These flags prioritize review only.
3. Fixed-seed precision pilot: use deterministic pseudo-random hash ranking to sample broad and uncertainty layers, manually code records as relevant, irrelevant, or uncertain, record reasons, and calculate observed precision with a Wilson 95% confidence interval after coding.
4. Cross-stage bridge diagnostic: identify S1-S2, S2-S3, S1-S3, and S1-S2-S3 overlaps as candidate links. Overlap is not evidence of information or uncertainty propagation.

The current pilot seed is 20261006. Sampling uses seeded FNV-1a hash ranking of stable record keys so the selected records are exactly reproducible across runs and platforms. The default pilot contains 50 broad records and 30 uncertainty-layer records per stage, or all records if the layer is smaller.

Propagation, masking/loss, preservation, amplification, or transformation can only be coded after full-text assessment with an evidence anchor.

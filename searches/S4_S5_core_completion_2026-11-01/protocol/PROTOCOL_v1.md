# S4–S5 core review retrieval, version 1

Frozen for this execution on 2026-11-01, before retrieval, following the user's explicit instruction to complete the original core review's S4 and S5 base and uncertainty streams. This is a dated execution protocol, not a claim of independent preregistration or external peer approval.

Source: searches/Scopus/S4/queries/SCOPUS_S4_queries.md and searches/Scopus/S5/queries/SCOPUS_S5_queries.md at repository commit 64e25b0a59cb348c46c4592f3371b36285c0e9cf. Their original draft text is preserved in source_queries.json. The vocabulary is unchanged for comparability. S4 = circularity/recoverability; S5 = embodied LCA/decision. No mandatory Digital Twin filter. Broad decision terms may retrieve operational-energy studies; these require later screening, not silent query removal.

Four searches per database: S4-1 base, S4-2 base + uncertainty, S5-1 base, S5-2 base + uncertainty. No date, language or document-type restriction added. Scopus uses TITLE-ABS-KEY. WoS uses TS (includes Keywords Plus, a documented field difference). IEEE uses All Metadata and partitions when its term/wildcard limits require it; unions and overlaps must be audited. Preserve native exports and DOI blanks. No sample is represented as complete.

Store exact executed queries, displayed counts, export ranges, access blockers, raw hashes and parsed counts. Verify uncertainty-set inclusion in base using native identifiers. Deduplicate DOI exactly; flag ambiguous title/year matches for manual review. Corpus membership is not full-text evidence of uncertainty propagation.

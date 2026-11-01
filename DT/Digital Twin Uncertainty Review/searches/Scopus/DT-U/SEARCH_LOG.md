# Scopus DT-U — complete retrieval

- Date: 2026-11-01; institutional access: SLUB Dresden; active personal Scopus session.
- Search: Documents; Article title, Abstract, Keywords; `"digital twin" AND uncertainty`.
- Result count: **3,501**. No date, language, subject, document-type or open-access restriction. Preprints and Secondary documents were not searched.
- Native CSV export: all information groups selected; **Truncate to optimize for Excel OFF**; no preference changes saved.
- All 45 native columns are retained, including EID, DOI, authors and IDs, affiliations, abstract, author/index keywords, references, funding, publication and conference details, serial identifiers and access status.

## Reconciliation

The result display is capped at 2,000, although the export dialog advertises up to 20,000. Full-range export attempts did not yield verified files. We used native current-page exports with 200 results per page: Date (newest), pages 1–10, followed by Date (oldest), pages 1–8. These are complementary retrieval batches of the same unfiltered query, not samples or screening subsets.

18 batches × 200 = **3,600 raw rows**; **99 repeated EID occurrences**, identical across all 45 fields; **3,501 unique EIDs**. The unique count exactly matches the source search count. Batch membership and SHA-256 hashes are in `results/raw/manifest.json`. Original export bytes are unchanged; descriptive filenames map back to native filenames in the manifest. The merged file records every originating batch and CSV row number.

**3,315 records have DOI values; 186 have no DOI in the source.** Missing values are retained. An EID is a source record identifier, not proof of a unique study: distinct versions and conference/journal records remain separate. No title-based merging, eligibility exclusion or cross-database deduplication was applied.

Some abstracts contain the source placeholder `[No abstract available]`; these are reported separately from blank cells in the audit. Future issue years (including 2027) are preserved as supplied. References can exceed Excel's cell limit; the CSV retains full exported text and is not optimized by truncating it.

## Rebuild and interpretation

Run `python scripts/prepare_scopus.py` from the review root (or use its absolute path). It verifies hashes, column schemas, record identifiers, duplicate consistency and the 3,501-record target before building the merged CSV, audit and lexical reading queue.

The unified CSV is 48,688,027 bytes. GitHub's create-blob endpoint rejected that request as too large. For complete publication, the merged data are stored in seven CSV partitions (500 records in each of the first six, 501 in the seventh) under `data/merged/SCOPUS_DTU_3501_parts/`, with a separate manifest. They have identical schemas and no overlap. The script rebuilds both the unified local file and all publication partitions. This packaging does not change the corpus or remove any fields.

The reading queue matches terms in titles, abstracts and keywords. It is **not** study eligibility, a quality score, a demonstrated architecture or a prevalence estimate. Full-text assessment remains pending. See `analysis/SCOPUS_ARCHITECTURE_FINDINGS.md` for explicitly limited abstract-level interpretation.

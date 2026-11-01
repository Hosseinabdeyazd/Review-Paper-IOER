# S4/S5 adjudication — incomplete checkpoint

**This is not the final screening result.** The user's requested reassessment covers 7,238 original records (5,093 unclear and 2,145 proposed automated exclusions). Only **50** of these have been read in this revision; **7,188 remain unread**. No random sample, accuracy estimate, independent human validation or completed PRISMA review is claimed.

## Duplicate adjudication

All 330 candidate groups were inspected bibliographically. Outcomes:

| Group outcome | Groups |
|---|---:|
| Merge as the same report | 304 |
| Keep distinct reports/volumes | 11 |
| Merge two of three records, retain the third report | 1 |
| Retain both pending conflicting-identifier verification | 14 |

These decisions remove 317 additional duplicate records, leaving **9,601 records**, not included studies. Fourteen identifier-conflict groups remain unresolved and are deliberately not collapsed. The 11 distinct groups include separate proceedings volumes and possible conference/journal or thesis/article report families. They are not necessarily independent studies.

Names, titles, publication locations, pagination and DOI values were compared. Author-string discrepancies were inspected. For ambiguous pagination and author cases, complete abstract differences were compared; typography and copyright additions were distinguished from substantive differences. Matching abstracts alone did not collapse differently paginated journal/conference versions. DOI corrections supported by external evidence include a `verification_url`; original supplied identifiers remain in provenance. Other DOI conflicts remain pending.

## Title/abstract decisions

The full **available** abstract and title of the first 50 requested records in the preserved input ordering were read by the assistant. Missing abstracts and book-wide promotional descriptions are explicitly identified in the reasons. These 50 are a sequential progress checkpoint, not a representative pilot and not validation of the previous keyword rules. Individual decisions and evidence are in `title_abstract_review_log.csv`.

`exclude_title_abstract` means an assistant scope decision at this stage, not a full-text decision. `exclude_nonresearch_component` identifies indexes/bibliographic back matter. `exclude_core_keep_methods` preserves a separate methods/background lead outside the S4/S5 core. `retain_fulltext_unclear` requires chapter/full-text evidence. No uncertainty keyword is mandatory and no paper is finally included on a keyword match.

The previous `screening_status` remains unchanged as an audit field. Use the new `adjudication_status` to identify actually reassessed rows; **`not_yet_reassessed` must not be treated as reviewed**. Records in the previous direct-scope/secondary groups are also outside this partial reassessment.

## Data and reproducibility

- `revised_records_partial.zip`: complete metadata CSV, 9,601 rows; DOI, authors, title, abstract and other original fields retained. Includes JSON containing all original metadata for merged groups.
- `record_alias_map.csv`: every original ID mapped to its current canonical ID, including unchanged records.
- `duplicate_group_adjudication.csv`: every group, candidate IDs, decision, rationale, canonical ID and verification link where available.
- `title_abstract_review_log.csv`: 50 actually read records, full original metadata and per-record reason.
- JSON decision files: explicit assistant-authored decisions, not generated keyword labels.
- `build_revision.py`: reruns the merge/application and count checks without assigning semantic decisions. Run beside the JSON files; input is `../tables/all_records_screening.zip`.
- `prisma_checkpoint.csv`, `summary.json`: reconciled partial counts. Identification 14,869; prior duplicates 4,951; additional duplicates 317; remaining 9,601. No final included-study number is supplied.

The raw exports, original 9,918-row screening dataset and previous automated outputs remain preserved. The earlier 12 digital-twin full texts are a separate corpus and are not counted here. This directory supersedes neither the raw data nor a final review; it records auditable progress and outstanding work.

## وضعیت به فارسی

۳۳۰ گروه از نظر کتاب‌شناختی بررسی شده‌اند: ۳۰۴ گروه ادغام، ۱۱ گروه حفظ به‌عنوان گزارش یا جلد جداگانه، یک گروه ادغام جزئی، و ۱۴ گروه دارای اختلاف DOI که هنوز تعیین هویت قطعی نشده‌اند. با ادغام‌های تأییدشده، ۳۱۷ رکورد دیگر کنار رفته و ۹۶۰۱ رکورد باقی مانده است.

بازبینی دقیق عنوان و چکیده **هنوز کامل نشده است**: ۵۰ مورد خوانده شده و ۷۱۸۸ مورد از صف درخواستی باقی مانده است. فایل‌های این پوشه گزارش مرحلهٔ جاری‌اند و نباید به‌عنوان PRISMA نهایی یا فهرست مقالات پذیرفته‌شده استفاده شوند. برای هر تصمیم انجام‌شده دلیل ثبت شده؛ تصمیم تازه‌ای به رکوردهای خوانده‌نشده نسبت داده نشده است.

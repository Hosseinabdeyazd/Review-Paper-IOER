#!/usr/bin/env python3
"""Convert Web of Science tagged Plain Text exports to a Scopus-shaped CSV.

The Scopus columns retain their exact labels and order. Scopus-only identifiers
are left blank where WoS has no equivalent; WoS-specific metadata is appended
in explicitly labelled columns so it is not mislabeled or discarded.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

SCOPUS_COLUMNS = [
    "Authors", "Author full names", "Author(s) ID", "Title", "Year",
    "Source title", "Volume", "Issue", "Art. No.", "Page start",
    "Page end", "Cited by", "DOI", "Link", "Affiliations",
    "Authors with affiliations", "Abstract", "Author Keywords",
    "Index Keywords", "Molecular Sequence Numbers", "Chemicals/CAS",
    "Tradenames", "Manufacturers", "Funding Details", "Funding Texts",
    "References", "Correspondence Address", "Editors", "Publisher",
    "Sponsors", "Conference name", "Conference date", "Conference location",
    "Conference code", "ISSN", "ISBN", "CODEN", "PubMed ID",
    "Language of Original Document", "Abbreviated Source Title",
    "Document Type", "Publication Stage", "Open Access", "Source", "EID",
]
WOS_EXTRA_COLUMNS = [
    "UT", "ResearcherID", "ORCID", "Keywords Plus",
    "Times Cited All Databases", "WoS Categories", "Web of Science Indexes",
    "Research Areas", "Early Access Date",
]


def parse_tagged_record(text: str) -> dict[str, list[str]]:
    fields: dict[str, list[str]] = defaultdict(list)
    current: str | None = None
    for line in text.splitlines():
        match = re.match(r"^([A-Z0-9]{2}) (.*)$", line)
        if match:
            current = match.group(1)
            fields[current].append(match.group(2).rstrip())
        elif line.startswith("   ") and current:
            if fields[current]:
                fields[current][-1] += " " + line[3:].strip()
    return fields


def value(fields: dict[str, list[str]], tag: str, sep: str = "; ") -> str:
    vals = [" ".join(v.split()) for v in fields.get(tag, []) if v.strip()]
    return sep.join(vals)


def first(fields: dict[str, list[str]], tag: str) -> str:
    return value(fields, tag)


def title_normalized(title: str) -> str:
    title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", title.lower()).split())


def identity(fields: dict[str, list[str]]) -> tuple[str, str]:
    ut = first(fields, "UT")
    if ut:
        return ("UT", ut.casefold())
    doi = first(fields, "DI")
    if doi:
        return ("DOI", doi.casefold().removeprefix("https://doi.org/"))
    return ("Title", title_normalized(first(fields, "TI")))


def map_record(fields: dict[str, list[str]]) -> dict[str, str]:
    doi = first(fields, "DI")
    issn = "; ".join(x for x in (first(fields, "SN"), first(fields, "EI")) if x)
    # C1 preserves WoS's author-to-affiliation grouping and is also the
    # closest direct equivalent to Scopus's authors-with-affiliations field.
    affiliation = value(fields, "C1")
    correspondence = value(fields, "RP")
    emails = value(fields, "EM")
    if emails:
        correspondence = "; ".join(x for x in (correspondence, emails) if x)

    row = {column: "" for column in SCOPUS_COLUMNS + WOS_EXTRA_COLUMNS}
    row.update({
        "Authors": value(fields, "AU"),
        "Author full names": value(fields, "AF"),
        # Scopus author IDs are platform-specific; WoS identifiers are kept
        # in their own additional columns below.
        "Title": first(fields, "TI"),
        "Year": first(fields, "PY"),
        "Source title": first(fields, "SO"),
        "Volume": first(fields, "VL"),
        "Issue": first(fields, "IS"),
        "Art. No.": first(fields, "AR"),
        "Page start": first(fields, "BP"),
        "Page end": first(fields, "EP"),
        "Cited by": first(fields, "TC"),
        "DOI": doi,
        "Link": ("https://doi.org/" + doi) if doi else "",
        "Affiliations": affiliation,
        "Authors with affiliations": affiliation,
        "Abstract": value(fields, "AB", sep=" "),
        "Author Keywords": value(fields, "DE"),
        "Index Keywords": value(fields, "ID"),
        "Funding Details": value(fields, "FU"),
        "Funding Texts": value(fields, "FX", sep=" "),
        "References": value(fields, "CR"),
        "Correspondence Address": correspondence,
        "Editors": value(fields, "BE"),
        "Publisher": first(fields, "PU"),
        "Conference name": value(fields, "CT"),
        "Conference date": value(fields, "CY"),
        "Conference location": value(fields, "CL"),
        "ISSN": issn,
        "ISBN": first(fields, "BN"),
        "CODEN": first(fields, "CD"),
        "PubMed ID": first(fields, "PM"),
        "Language of Original Document": first(fields, "LA"),
        "Abbreviated Source Title": first(fields, "J9"),
        "Document Type": first(fields, "DT"),
        "Publication Stage": "Early Access" if first(fields, "EA") else "",
        "Open Access": first(fields, "OA"),
        "Source": "Web of Science Core Collection",
        "UT": first(fields, "UT"),
        "ResearcherID": value(fields, "RI"),
        "ORCID": value(fields, "OI"),
        "Keywords Plus": value(fields, "ID"),
        "Times Cited All Databases": first(fields, "Z9"),
        "WoS Categories": value(fields, "WC"),
        "Web of Science Indexes": value(fields, "WE"),
        "Research Areas": value(fields, "SC"),
        "Early Access Date": first(fields, "EA"),
    })
    return row


def read_records(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8-sig")
    records = re.findall(r"(?ms)^PT .*?^ER\s*$", text)
    if not records:
        raise ValueError(f"No WoS records found in {path}")
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", type=Path, help="WoS tagged Plain Text exports")
    parser.add_argument("-o", "--output", required=True, type=Path, help="Destination CSV")
    args = parser.parse_args()

    seen: set[tuple[str, str]] = set()
    rows: list[dict[str, str]] = []
    raw_count = 0
    duplicate_count = 0
    for path in args.inputs:
        for record in read_records(path):
            raw_count += 1
            fields = parse_tagged_record(record)
            key = identity(fields)
            if key in seen:
                duplicate_count += 1
                continue
            seen.add(key)
            rows.append(map_record(fields))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8-sig", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=SCOPUS_COLUMNS + WOS_EXTRA_COLUMNS,
                                quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Raw records: {raw_count}")
    print(f"Duplicates removed: {duplicate_count}")
    print(f"Final records: {len(rows)}")
    print(f"Columns: {len(SCOPUS_COLUMNS) + len(WOS_EXTRA_COLUMNS)}")
    print(f"CSV: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

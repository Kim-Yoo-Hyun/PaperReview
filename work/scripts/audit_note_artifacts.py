#!/usr/bin/env python3
"""Audit and conservatively clean legacy PDF-extraction artifacts in paper notes.

The audit is scoped to the five standard note files listed by papers.json.  It
does not download PDFs, regenerate analysis, change reading status, or infer
paper facts.  Without --apply it is read-only.  With --apply it only applies
high-confidence textual cleanup and writes a compact before/after report.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PAPERS = ROOT / "work" / "sources" / "papers.json"
DEFAULT_REPORT = ROOT / "work" / "sources" / "note_artifact_audit_2026-09-02.json"
NOTE_NAMES = (
    "01_overview.md",
    "02_problem.md",
    "03_method.md",
    "04_evaluation.md",
    "05_insights.md",
)

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b")
FRONT_MATTER_RE = re.compile(r"front matter", re.I)
EQUAL_RE = re.compile(
    r"(?:[*†‡∗]\s*)?(?:equal (?:contribution|contributions|advising)|"
    r"authors? contributed equally(?: to this work)?)\b",
    re.I,
)
ACCEPTED_RE = re.compile(
    r"\baccepted\s+(?:january|february|march|april|may|june|july|august|"
    r"september|october|november|december)(?:\s*[,/]?\s*\d{1,2})?"
    r"\s*[,/]?\s*20\d{2}\b",
    re.I,
)
MANUSCRIPT_RE = re.compile(r"\bmanuscript received\s*:", re.I)
PUBLISHED_RE = re.compile(
    r"\bpublished in\s+[^\n()]{1,180}\(\s*\d{1,2}\s*/\s*20\d{2}\s*\)",
    re.I,
)
PUBLISHED_AS_RE = re.compile(
    r"\bpublished as a (?:conference|journal) paper at\s+[^\n]{1,120}?\b20\d{2}\b",
    re.I,
)
ARXIV_HEADER_RE = re.compile(
    r"(?:all rights reserved\s+)?arXiv:\s*\d{4}\.\d{4,}(?:v\d+)?\s*"
    r"(?:\[[^\]\n]+\]\s*)?\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|"
    r"January|February|March|April|May|June|July|August|September|October|November|December)"
    r"\s+20\d{2}\b",
    re.I,
)
ARXIV_CUE_RE = re.compile(
    r"(?:[A-Za-z]{1,5})?arXiv:\s*\d{4}\.\d{4,}v\d+(?:\s*\[[^\]\n]+\])?"
    r"(?:\s+\d{1,2}\s+[A-Za-z]+\s+20\d{2})?(?:\s+\.\.\.)?",
    re.I,
)
JOURNAL_FOOTER_RE = re.compile(
    r"\bpublished\s*,?\s+transactions\s*,?\s+machine\s*,?\s+learning\s*,?\s+research\b",
    re.I,
)
COPYRIGHT_RE = re.compile(r"(?:\bcopyright\b|all rights reserved|©\s*(?:19|20)\d{2})", re.I)
FUNDING_RE = re.compile(
    r"(?:[*†‡∗]\s*)?(?:this work was supported(?: in part)? by|supported by|funded by)\b",
    re.I,
)
PROCEEDINGS_FOOTER_RE = re.compile(
    r"\bproceedings of the\s+\d{4}\b[^\n]{0,220}(?:0-\d{4}-\d{4}|\$\s*\d+(?:\.\d+)?|©)",
    re.I,
)
RSS_HEADER_RE = re.compile(r"\brobotics:\s*science and systems\s+20\d{2}\b[^\n]*", re.I)
PAGE_HEADER_RE = re.compile(
    r"\b[A-Z]{4,}\*?,\s*[A-Z]{4,}\*?(?:\s+[A-Z]{4,}\*?)*\s+et al\.:",
)
AFFILIATION_RE = re.compile(
    r"\b(?:department of|associate professor|assistant professor|professor,|"
    r"national key laboratory|state key laboratory|laboratory for manufacturing and productivity|"
    r"school of [a-z]|college of [a-z]|institute of robotics and machine intelligence|"
    r"massachusetts institute of technology|arizona state university|"
    r"jet propulsion laboratory|california institute of technology|"
    r"midea group|east china normal university|shanghai university|"
    r"peking university|chinese university of hong kong|"
    r"beijing innovation center of humanoid robotics|university of nottingham|"
    r"poznan university of technology|work done during [^\n]{0,100} internship at)\b",
    re.I,
)
AFFILIATION_SECTION_RE = re.compile(
    r"(?:\bp\.\s*\d+\s*/\s*(?:\d+(?:\.\d+)*\s+)?"
    r"[^:|()\n-]{1,120}(?:university|institute|laboratory)"
    r"[^:|()\n-]*(?:\)|\s+-\s+extractive)|"
    r"\bp\.\s*\d+\s*\(\s*(?:\d+(?:\.\d+)*\s+)?"
    r"[^()\n]{1,120}(?:university|institute|laboratory)[^()\n]*\))",
    re.I,
)
AFFILIATION_PARENT_RE = re.compile(
    r"\((?:\d+(?:\.\d+)*\s+)?[^()\n]*(?:university|institute|laboratory)[^()\n]*\)",
    re.I,
)
AFFILIATION_LABEL_RE = re.compile(
    r"(\bp\.\s*\d+\s*/\s*)([^|\n-]{0,120}"
    r"(?:university|institute|laboratory)[^|\n-]*)(\s+-\s+extractive)",
    re.I,
)


def load_paper_folders() -> list[Path]:
    papers = json.loads(PAPERS.read_text(encoding="utf-8"))
    return [ROOT / item["folder"] for item in papers if item.get("folder")]


def note_paths() -> list[Path]:
    paths: list[Path] = []
    for folder in load_paper_folders():
        paths.extend(folder / name for name in NOTE_NAMES if (folder / name).exists())
    return paths


def issue_kinds(line: str) -> list[str]:
    issues: list[str] = []
    if FRONT_MATTER_RE.search(line):
        issues.append("front_matter_anchor")
    if EQUAL_RE.search(line):
        issues.append("author_footnote")
    if (
        ACCEPTED_RE.search(line)
        or MANUSCRIPT_RE.search(line)
        or PUBLISHED_RE.search(line)
        or PUBLISHED_AS_RE.search(line)
    ):
        issues.append("publication_stamp")
    if COPYRIGHT_RE.search(line):
        issues.append("copyright_footer")
    if ARXIV_HEADER_RE.search(line) or ARXIV_CUE_RE.search(line):
        issues.append("source_header")
    if JOURNAL_FOOTER_RE.search(line):
        issues.append("publisher_or_funding_footer")
    if funding_artifact(line) or PROCEEDINGS_FOOTER_RE.search(line) or RSS_HEADER_RE.search(line):
        issues.append("publisher_or_funding_footer")
    if PAGE_HEADER_RE.search(line):
        issues.append("page_header")
    if EMAIL_RE.search(line) or AFFILIATION_RE.search(line):
        issues.append("author_affiliation")
    if AFFILIATION_SECTION_RE.search(line):
        issues.append("affiliation_section_label")
    return issues


def funding_artifact(line: str) -> re.Match[str] | None:
    match = FUNDING_RE.search(line)
    if not match:
        return None
    prefix = line[: match.start()]
    if re.search(r"[*†‡∗]\s*$", prefix) or re.match(r"[*†‡∗]", match.group()):
        return match
    body = body_part(line).lstrip()
    body = re.sub(r"^[*†‡∗]\s*", "", body)
    if body.casefold().startswith(("this work was supported", "supported by", "funded by")):
        return match
    return None


def scan(paths: list[Path]) -> dict:
    counts: Counter[str] = Counter()
    files_by_issue: dict[str, set[str]] = {}
    findings: list[dict] = []
    for path in paths:
        file_issues: Counter[str] = Counter()
        line_numbers: dict[str, list[int]] = {}
        text = path.read_text(encoding="utf-8", errors="ignore")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for issue in issue_kinds(line):
                counts[issue] += 1
                file_issues[issue] += 1
                line_numbers.setdefault(issue, []).append(line_number)
                files_by_issue.setdefault(issue, set()).add(str(path.relative_to(ROOT)))
        if file_issues:
            findings.append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "issues": dict(sorted(file_issues.items())),
                    "line_numbers": {key: values for key, values in sorted(line_numbers.items())},
                }
            )
    return {
        "note_files_scanned": len(paths),
        "files_with_findings": len(findings),
        "occurrences": dict(sorted(counts.items())),
        "files_by_issue": {
            key: sorted(values) for key, values in sorted(files_by_issue.items())
        },
        "findings": findings,
    }


def alpha_count(value: str) -> int:
    return sum(char.isalpha() for char in value)


def body_part(value: str) -> str:
    if "**:" in value:
        return value.split("**:", 1)[1]
    if "|" in value:
        return value.split("|", 1)[-1]
    return value


def ends_incomplete(value: str) -> bool:
    return bool(
        re.search(
            r"\b(?:a|an|and|as|at|by|for|from|in|into|of|on|or|the|to|with|"
            r"but|do not|does not|can|cannot|that|which|because|through|via|"
            r"we|our|they|he|she|it|this|these|those)\s*$",
            value.strip(" -,:;"),
            re.I,
        )
    )


def finish_body_prefix(prefix: str) -> str:
    prefix = re.sub(r"[\s*†‡∗]+$", "", prefix).rstrip(" ,;:")
    if prefix and prefix[-1] not in ".!?)]}":
        prefix += "."
    return prefix


def clean_line(line: str, changes: Counter[str]) -> str | None:
    newline = "\n" if line.endswith("\n") else ""
    content = line[:-1] if newline else line
    original = content

    if FRONT_MATTER_RE.search(content):
        content = FRONT_MATTER_RE.sub("body section not recovered", content)
        changes["relabel_front_matter_anchor"] += 1

    # Legacy heading recovery can mistake an author affiliation for a paper
    # section (for example, ``p. 1 / 2 Nanyang Technological University``).
    # The body cue may still be useful, but the affiliation cannot be its
    # section provenance, so relabel only the heading/anchor fragment.
    if AFFILIATION_SECTION_RE.search(content):
        parent_cleaned = AFFILIATION_PARENT_RE.sub("(body section not recovered)", content)
        if parent_cleaned != content:
            changes["relabel_affiliation_section"] += 1
            content = parent_cleaned
        label_cleaned = AFFILIATION_LABEL_RE.sub(
            r"\1body section not recovered\3",
            content,
        )
        if label_cleaned != content:
            changes["relabel_affiliation_section"] += 1
            content = label_cleaned

    stripped_artifact = False

    rss_header = RSS_HEADER_RE.search(content)
    if rss_header:
        prefix = content[: rss_header.start()].rstrip()
        if alpha_count(body_part(prefix)) >= 45 and not ends_incomplete(prefix):
            content = finish_body_prefix(prefix)
        elif alpha_count(body_part(prefix)) >= 45:
            content = prefix + " ..."
        else:
            changes["remove_contaminated_publisher_line"] += 1
            return None
        changes["remove_rss_header"] += 1
        stripped_artifact = True

    proceedings = PROCEEDINGS_FOOTER_RE.search(content)
    if proceedings:
        prefix = content[: proceedings.start()].rstrip()
        if alpha_count(body_part(prefix)) >= 45 and not ends_incomplete(prefix):
            content = finish_body_prefix(prefix)
        elif alpha_count(body_part(prefix)) >= 45:
            content = prefix + " ..."
        else:
            changes["remove_contaminated_publisher_line"] += 1
            return None
        changes["remove_proceedings_footer"] += 1
        stripped_artifact = True

    page_header = PAGE_HEADER_RE.search(content)
    if page_header:
        continuation = re.search(
            r"\b(?:Figure|Fig\.|Table|Tab\.)\s+\d+\b",
            content[page_header.end() :],
            re.I,
        )
        if continuation:
            offset = page_header.end() + continuation.start()
            content = content[: page_header.start()] + content[offset:]
        else:
            prefix = content[: page_header.start()].rstrip()
            if alpha_count(body_part(prefix)) >= 45 and not ends_incomplete(prefix):
                content = finish_body_prefix(prefix)
            elif alpha_count(body_part(prefix)) >= 45:
                content = prefix + " ..."
            else:
                changes["remove_contaminated_page_header_line"] += 1
                return None
        changes["remove_page_header"] += 1
        stripped_artifact = True

    arxiv_header = ARXIV_HEADER_RE.search(content)
    if not arxiv_header:
        arxiv_header = ARXIV_CUE_RE.search(content)
    if arxiv_header:
        prefix = content[: arxiv_header.start()].rstrip()
        # A page number is sometimes emitted immediately before the arXiv
        # running header (``... training 1 arXiv:...``).  It is page chrome,
        # not part of the body sentence.
        prefix = re.sub(r"\s+\d{1,3}$", "", prefix)
        suffix = content[arxiv_header.end() :].strip()
        if alpha_count(body_part(prefix)) >= 45:
            if suffix and alpha_count(body_part(suffix)) >= 25:
                content = prefix + " " + suffix
            elif ends_incomplete(prefix):
                content = prefix + " ..."
            else:
                content = finish_body_prefix(prefix)
        elif suffix and alpha_count(body_part(suffix)) >= 25:
            content = suffix
        else:
            changes["remove_contaminated_source_header_line"] += 1
            return None
        changes["remove_source_header"] += 1
        stripped_artifact = True

    # Keep a body sentence only when a publication footer is clearly a prefix
    # or suffix.  If removing the footer would leave a fragment, drop the
    # contaminated evidence line rather than preserve a false sentence.
    manuscript = MANUSCRIPT_RE.search(content)
    if manuscript:
        prefix = content[: manuscript.start()].rstrip()
        if alpha_count(body_part(prefix)) >= 45 and prefix.rstrip().endswith((".", "!", "?")):
            content = prefix
        else:
            changes["remove_contaminated_publication_line"] += 1
            return None
        changes["remove_manuscript_stamp"] += 1

    published = PUBLISHED_RE.search(content)
    if published:
        content = (content[: published.start()] + " " + content[published.end() :]).strip()
        changes["remove_published_stamp"] += 1
        stripped_artifact = True

    published_as = PUBLISHED_AS_RE.search(content)
    if published_as:
        content = (content[: published_as.start()] + " " + content[published_as.end() :]).strip()
        changes["remove_published_stamp"] += 1
        stripped_artifact = True

    journal_footer = JOURNAL_FOOTER_RE.search(content)
    if journal_footer:
        prefix = content[: journal_footer.start()].rstrip()
        if alpha_count(body_part(prefix)) >= 45:
            if ends_incomplete(prefix):
                content = prefix + " ..."
            else:
                content = finish_body_prefix(prefix)
        else:
            changes["remove_contaminated_publisher_line"] += 1
            return None
        changes["remove_journal_footer"] += 1
        stripped_artifact = True

    accepted = ACCEPTED_RE.search(content)
    if accepted:
        content = (content[: accepted.start()] + " " + content[accepted.end() :]).strip()
        changes["remove_accepted_stamp"] += 1
        stripped_artifact = True

    funding = funding_artifact(content)
    if funding:
        prefix = content[: funding.start()].rstrip()
        if alpha_count(body_part(prefix)) >= 45:
            content = finish_body_prefix(prefix)
        else:
            changes["remove_contaminated_funding_line"] += 1
            return None
        changes["remove_funding_footnote"] += 1
        stripped_artifact = True

    copyright = COPYRIGHT_RE.search(content)
    if copyright:
        prefix = content[: copyright.start()].rstrip(" ,;:")
        if alpha_count(body_part(prefix)) >= 45 and not ends_incomplete(prefix):
            content = finish_body_prefix(prefix)
        else:
            changes["remove_contaminated_copyright_line"] += 1
            return None
        changes["remove_copyright_footer"] += 1
        stripped_artifact = True

    equal = EQUAL_RE.search(content)
    if equal:
        prefix = content[: equal.start()]
        # Preserve a sufficiently long body cue even when the footnote marker
        # is attached to an incomplete sentence (for example, ``... do not *``).
        # Dropping that whole line would lose valid paper evidence along with
        # the author metadata.  Short or clearly metadata-only lines remain
        # excluded as contaminated extraction.
        if alpha_count(body_part(prefix)) >= 45:
            if ends_incomplete(prefix):
                content = prefix.rstrip(" -*†‡∗") + " ..."
            else:
                content = finish_body_prefix(prefix)
        else:
            changes["remove_contaminated_author_line"] += 1
            return None
        changes["remove_author_footnote"] += 1

    # Email tokens are unambiguous author metadata.  Remove only the token;
    # the surrounding sentence may still contain a valid body cue.
    if EMAIL_RE.search(content):
        content = EMAIL_RE.sub("", content)
        content = re.sub(r"\s{2,}", " ", content)
        changes["remove_email_token"] += 1

    affiliation = AFFILIATION_RE.search(content)
    if affiliation:
        prefix = content[: affiliation.start()].rstrip(" ,;:")
        if alpha_count(body_part(prefix)) >= 45:
            if ends_incomplete(prefix):
                content = prefix + " ..."
            else:
                content = finish_body_prefix(prefix)
        else:
            changes["remove_contaminated_affiliation_line"] += 1
            return None
        changes["remove_affiliation_tail"] += 1
        stripped_artifact = True

    content = re.sub(r"[ \t]{2,}", " ", content).rstrip()
    if stripped_artifact and alpha_count(body_part(content)) < 25:
        changes["remove_empty_artifact_line"] += 1
        return None
    if content != original:
        return content + newline
    return line


def apply_cleanup(paths: list[Path]) -> dict:
    changes: Counter[str] = Counter()
    modified_files: list[str] = []
    for path in paths:
        original = path.read_text(encoding="utf-8", errors="ignore")
        output: list[str] = []
        for line in original.splitlines(keepends=True):
            cleaned = clean_line(line, changes)
            if cleaned is not None:
                output.append(cleaned)
        updated = "".join(output)
        if original.endswith("\n") and updated and not updated.endswith("\n"):
            updated += "\n"
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            modified_files.append(str(path.relative_to(ROOT)))
    return {
        "modified_files": modified_files,
        "modified_file_count": len(modified_files),
        "changes": dict(sorted(changes.items())),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="apply only high-confidence cleanup and write the audit report")
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    paths = note_paths()
    before = scan(paths)
    result = {
        "schema_version": "1.0",
        "audit_date": str(date.today()),
        "scope": "five standard note files under paper folders listed in work/sources/papers.json",
        "pdf_access": "none; note text only",
        "policy": {
            "auto_cleaned": [
                "Front matter anchor relabelled as body section not recovered",
                "acceptance/publication/source/copyright stamps removed when separable",
                "equal-contribution author footnotes removed",
                "publisher/funding footer, journal/source header, and page-header fragments removed when separable",
                "unambiguous email and affiliation metadata removed",
                "affiliation mistaken for a section label relabelled as body section not recovered",
            ],
            "manual_review_only": [
                "ambiguous section labels such as a university/institute heading",
                "OCR corruption that cannot be safely reconstructed",
                "claims requiring the original PDF or experiment context",
            ],
        },
        "before": before,
        "applied": False,
    }
    if args.apply:
        applied = apply_cleanup(paths)
        after = scan(paths)
        result["applied"] = True
        result["cleanup"] = applied
        result["after"] = after

    report_path = args.report if args.report.is_absolute() else ROOT / args.report
    if args.apply:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        {
            "mode": "apply" if args.apply else "dry-run",
            "note_files_scanned": before["note_files_scanned"],
            "files_with_findings_before": before["files_with_findings"],
            "occurrences_before": before["occurrences"],
            "modified_files": result.get("cleanup", {}).get("modified_file_count", 0),
            "report": str(report_path.relative_to(ROOT)) if args.apply else None,
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

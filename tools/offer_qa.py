#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Georgian OFFER QA Runner
========================

Implements the 7-check Georgian syntax QA pattern from ai2026-automation
Step 6.5 + ai2026-knowledge-base/references/georgian-offer-qa.md.

Runs the canonical pre-delivery checks against any client folder:

  1. Em-dashes (—)         — BANNED in Georgian
  2. En-dashes  (–)         — BANNED
  3. Forbidden abbreviations (მაგ. სთ. გვ. შპს ა.შ. ე.ი. და სხვ.)
  4. AI-ს genitive         — should be AI-ის (NOT AI-ს) in genitive context
  5. NGO-ს genitive        — should be NGO-ის
  6. SmartAcademy / unwanted brand refs (configurable)
  7. Foreign-word genitive  — workflow, Caritas Georgia, Copilot, M365, ...

Designed for the ai2026 project at C:/Users/GBASILAIA/claude/ai2026/,
but works on any folder of .md / .html files.

Usage
-----

    # Scan one client
    python offer_qa.py --client C:/Users/GBASILAIA/claude/ai2026/orbi

    # Scan all client folders under ai2026
    python offer_qa.py --root C:/Users/GBASILAIA/claude/ai2026 --all

    # Auto-fix safe issues (em-dash, en-dash, abbreviations, AI/NGO genitive)
    python offer_qa.py --client .../orbi --fix

    # JSON output for CI / pipelines
    python offer_qa.py --client .../orbi --json

    # Save a markdown report to the client folder
    python offer_qa.py --client .../orbi --report

Exit codes: 0 = clean, 1 = issues found, 2 = error.

Author: Hermes Agent (Giorgi Basilaia)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Iterable

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# File extensions to scan (HTML, MD, plain text)
SCAN_EXTENSIONS = {".md", ".html", ".htm", ".txt"}

# Forbidden abbreviations: (regex_pattern, expansion)
# The expansion may include a trailing colon / space where natural.
ABBREVIATIONS: list[tuple[re.Pattern[str], str]] = [
    # The .\\. is intentionally optional (?\\.?) because OFFERs use both
    # forms: "1სთ." (textbook) and "1 სთ" (running text). The trailing
    # boundary (\\b|\\s|$) prevents matching the suffix of a longer word.
    (re.compile(r"მაგ\.?(?=\s|$|[\)\,;:])"), "მაგალითად"),
    (re.compile(r"(?<=\d|\b)სთ\.?(?=\s|$|[\)\,;:])"), "საათი"),
    (re.compile(r"(?<=\d|\b)წთ\.?(?=\s|$|[\)\,;:])"), "წუთი"),
    (re.compile(r"(?<=\d|\b)წმ\.?(?=\s|$|[\)\,;:])"), "წამი"),
    (re.compile(r"გვ\.?(?=\s|$|[\)\,;:])"), "გვერდი"),
    (re.compile(r"\bშპს\b"), "შეზღუდული პასუხისმგებლობის საზოგადოება"),
    (re.compile(r"\bა\.შ\."), "ასეთივე"),
    (re.compile(r"\bე\.ი\."), "ესე იგი"),
    (re.compile(r"და\s+სხვ\."), "და სხვები"),
    (re.compile(r"და\s+ა\.შ\."), "და ასეთივე"),
    (re.compile(r"\bწლ\.?(?=\s|$|[\)\,;:])"), "წელი"),
    (re.compile(r"\bთვ\.?(?=\s|$|[\)\,;:])"), "თვე"),
    (re.compile(r"\bკვ\.?(?=\s|$|[\)\,;:])"), "კვირა"),
    (re.compile(r"\bდღ\.?(?=\s|$|[\)\,;:])"), "დღე"),
    (re.compile(r"\bქვ\.?(?=\s|$|[\)\,;:])"), "ქვეყანა"),
]

# Postpositions and dative-governing verbs that take -ს (not -ის) after
# foreign acronyms — i.e. contexts that LOOK like genitive errors but
# are actually dative + postposition. We must NOT fix these.
#
# Pattern: any of these substrings in the matched line means leave it alone.
GENITIVE_FALSE_POSITIVES = [
    # Postpositions (take dative)
    "სთვის", "სთან", "სგან", "სკენ",
    # Locative (looks like genitive, isn't)
    # -ში / -ზე are tricky to match without false-negatives, so we
    # handle them per-line below using a word-boundary check.
    # Verbs that govern dative (object in dative case)
    "იყენებ", "გამოიყენებ", "აღწერს", "სჭირდება", "ჩაშენებულია",
    "დამატებითი",  # "additional [tool]" — descriptive, not genitive
]

# Dative + postposition / purpose marker (catches `AI-ს დასანერგავად`,
# `AI-ს ყოველდღიურ საქმიანობაში`, etc.)
DATIVE_PURPOSE_MARKERS = [
    "დასანერგავად", "დასაწყისში", "ყოველდღიურ", "საქმიანობაში",
    "დახმარებით", "ერთად",
]

# Foreign words that get the same -ს / -ის genitive treatment as AI/NGO.
# Two-word names must be quoted; single words are bare.
# Order doesn't matter; the loop short-circuits on the first match per line.
FOREIGN_WORDS = [
    "workflow",
    "Caritas Georgia", "Czech Republic",
    "Copilot", "M365", "format", "NotebookLM", "Claude", "Perplexity",
    "Lovable", "Make.com", "Canva", "SharePoint", "EDM",
    "ChatGPT", "Gemini", "Salesforce", "HubSpot", "Zapier",
    "Airtable", "Notion", "Confluence", "Jira", "Asana",
    "Monday.com", "Trello", "Linear", "Figma", "Vercel", "Stripe",
    "Microsoft", "OpenAI", "Anthropic", "Google", "Slack", "Zoom",
    "Teams", "Outlook", "Gmail", "PowerPoint", "Word", "Excel",
]

# SmartAcademy / unwanted brand references. The user is no longer affiliated
# with Smart Academy, so any reference in OFFERs is a leak.
UNWANTED_BRANDS = [
    re.compile(r"SmartAcademy"),
    re.compile(r"Smart\s+Academy"),
    re.compile(r"SmartAcademy\.ge"),
]

# Issue severity
SEV_ERROR = "ERROR"     # must fix before delivery
SEV_WARN = "WARN"       # review manually


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class Issue:
    """A single QA finding."""
    check_id: int           # 1..7
    check_name: str
    file: str               # path relative to scan root
    line: int
    column: int
    text: str               # the offending substring
    line_content: str       # the full line (truncated)
    severity: str = SEV_ERROR
    auto_fixable: bool = False
    suggested_fix: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class QAResult:
    """All QA findings for one client folder."""
    client_path: str
    scanned_files: list[str] = field(default_factory=list)
    issues: list[Issue] = field(default_factory=list)
    started_at: str = ""
    finished_at: str = ""

    @property
    def total(self) -> int:
        return len(self.issues)

    @property
    def failed(self) -> bool:
        return any(i.severity == SEV_ERROR for i in self.issues)

    def by_check(self) -> dict[int, list[Issue]]:
        out: dict[int, list[Issue]] = {}
        for i in self.issues:
            out.setdefault(i.check_id, []).append(i)
        return out

    def to_dict(self) -> dict:
        return {
            "client_path": self.client_path,
            "scanned_files": self.scanned_files,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "total_issues": self.total,
            "failed": self.failed,
            "issues": [i.to_dict() for i in self.issues],
        }


# ---------------------------------------------------------------------------
# File scanning
# ---------------------------------------------------------------------------

def discover_files(root: Path) -> list[Path]:
    """Return a sorted list of .md/.html/.txt files under root (recursive).

    Excludes any directory starting with `.` (e.g. .git, .claude, .gemini)
    and any _qa_report_* files (we don't want to scan our own reports).
    """
    if not root.exists():
        raise FileNotFoundError(f"Client folder does not exist: {root}")
    if not root.is_dir():
        raise NotADirectoryError(f"Not a directory: {root}")

    excluded_dir_prefixes = (".",)
    excluded_name_patterns = ("_qa_report_",)

    out: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in SCAN_EXTENSIONS:
            continue
        # Skip files in hidden directories
        if any(part.startswith(excluded_dir_prefixes) for part in path.parts):
            continue
        # Skip our own QA reports
        if any(p.startswith(excluded_name_patterns) for p in path.parts):
            continue
        out.append(path)
    return sorted(out)


def iter_lines(path: Path) -> Iterable[tuple[int, str]]:
    """Yield (1-based line number, line text) for a file.

    Decodes as UTF-8 with errors='replace' so we never crash on a weird byte.
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        print(f"WARN: could not read {path}: {exc}", file=sys.stderr)
        return
    for n, line in enumerate(text.splitlines(), start=1):
        yield n, line


# ---------------------------------------------------------------------------
# The 7 checks
# ---------------------------------------------------------------------------

def _truncate(s: str, n: int = 200) -> str:
    s = s.rstrip("\r\n")
    if len(s) <= n:
        return s
    return s[: n - 1] + "…"


def _is_dative_false_positive(line: str) -> bool:
    """Return True if the line contains a context that makes -ს dative,
    not genitive. We never want to auto-fix these."""
    for marker in GENITIVE_FALSE_POSITIVES:
        if marker in line:
            return True
    for marker in DATIVE_PURPOSE_MARKERS:
        if marker in line:
            return True
    # Locative postpositions as standalone suffixes on a following word.
    # We match the pattern "-ს <word>ში" or "-ს <word>ზე" loosely.
    if re.search(r"-ს\s+[\u10d0-\u10ff]+(?:ში|ზე)\b", line):
        return True
    return False


def check_em_dash(file: Path, line_num: int, line: str, root: Path) -> list[Issue]:
    """Check 1: em-dashes (—) — BANNED in Georgian."""
    issues = []
    for m in re.finditer("—", line):
        issues.append(Issue(
            check_id=1,
            check_name="em-dash",
            file=str(file.relative_to(root)),
            line=line_num,
            column=m.start() + 1,
            text="—",
            line_content=_truncate(line),
            severity=SEV_ERROR,
            auto_fixable=True,
            suggested_fix="-",
        ))
    return issues


def check_en_dash(file: Path, line_num: int, line: str, root: Path) -> list[Issue]:
    """Check 2: en-dashes (–) — BANNED in Georgian."""
    issues = []
    for m in re.finditer("–", line):
        issues.append(Issue(
            check_id=2,
            check_name="en-dash",
            file=str(file.relative_to(root)),
            line=line_num,
            column=m.start() + 1,
            text="–",
            line_content=_truncate(line),
            severity=SEV_ERROR,
            auto_fixable=True,
            suggested_fix="-",
        ))
    return issues


def check_abbreviations(file: Path, line_num: int, line: str, root: Path) -> list[Issue]:
    """Check 3: forbidden abbreviations (მაგ., სთ., გვ., შპს, ა.შ., ე.ი., და სხვ.)"""
    issues = []
    for pattern, expansion in ABBREVIATIONS:
        for m in pattern.finditer(line):
            issues.append(Issue(
                check_id=3,
                check_name="forbidden-abbrev",
                file=str(file.relative_to(root)),
                line=line_num,
                column=m.start() + 1,
                text=m.group(0),
                line_content=_truncate(line),
                severity=SEV_ERROR,
                auto_fixable=True,
                suggested_fix=expansion,
            ))
    return issues


def check_ai_genitive(file: Path, line_num: int, line: str, root: Path) -> list[Issue]:
    """Check 4: AI-ს genitive — should be AI-ის when followed by a noun
    in nominative (not dative + postposition, not object of dative verb)."""
    issues = []
    # Look for AI-ს followed by a Georgian letter
    for m in re.finditer(r"AI-ს\s+([\u10d0-\u10ff])", line):
        if _is_dative_false_positive(line):
            continue
        issues.append(Issue(
            check_id=4,
            check_name="ai-genitive",
            file=str(file.relative_to(root)),
            line=line_num,
            column=m.start() + 1,
            text="AI-ს",
            line_content=_truncate(line),
            severity=SEV_ERROR,
            auto_fixable=True,
            suggested_fix="AI-ის",
        ))
    return issues


def check_ngo_genitive(file: Path, line_num: int, line: str, root: Path) -> list[Issue]:
    """Check 5: NGO-ს genitive — should be NGO-ის when followed by a noun."""
    issues = []
    for m in re.finditer(r"NGO-ს\s+([\u10d0-\u10ff])", line):
        if _is_dative_false_positive(line):
            continue
        issues.append(Issue(
            check_id=5,
            check_name="ngo-genitive",
            file=str(file.relative_to(root)),
            line=line_num,
            column=m.start() + 1,
            text="NGO-ს",
            line_content=_truncate(line),
            severity=SEV_ERROR,
            auto_fixable=True,
            suggested_fix="NGO-ის",
        ))
    return issues


def check_unwanted_brands(file: Path, line_num: int, line: str, root: Path) -> list[Issue]:
    """Check 6: SmartAcademy / Smart Academy / SmartAcademy.ge — config-driven."""
    issues = []
    for pattern in UNWANTED_BRANDS:
        for m in pattern.finditer(line):
            issues.append(Issue(
                check_id=6,
                check_name="unwanted-brand",
                file=str(file.relative_to(root)),
                line=line_num,
                column=m.start() + 1,
                text=m.group(0),
                line_content=_truncate(line),
                severity=SEV_ERROR,
                auto_fixable=False,  # requires manual review (context-dependent)
                suggested_fix="(remove or replace — review context)",
            ))
    return issues


def check_foreign_genitive(file: Path, line_num: int, line: str, root: Path) -> list[Issue]:
    """Check 7: foreign-word genitive (workflow, Caritas Georgia, etc.)."""
    issues = []
    if _is_dative_false_positive(line):
        return issues
    for word in FOREIGN_WORDS:
        # Match `word-ს` followed by a Georgian letter. For multi-word
        # names (e.g. "Caritas Georgia") we anchor on the boundary char.
        # Use a flexible boundary: word can be followed by punctuation.
        pattern = re.compile(
            rf"(?:^|[\s\(\[\"\'>])"      # preceded by start, whitespace, or open bracket/quote
            rf"({re.escape(word)})"      # the foreign word
            rf"-ს\s+([\u10d0-\u10ff])"   # -ს followed by a Georgian letter
        )
        for m in pattern.finditer(line):
            # Skip if the -ს is the start of a Georgian compound suffix
            # rather than a case marker (very rare in practice, but safe).
            word_start = m.start(1)
            column = word_start + 1
            issues.append(Issue(
                check_id=7,
                check_name="foreign-genitive",
                file=str(file.relative_to(root)),
                line=line_num,
                column=column,
                text=f"{word}-ს",
                line_content=_truncate(line),
                severity=SEV_ERROR,
                auto_fixable=False,  # multi-word risk; require manual confirmation
                suggested_fix=f"{word}-ის",
            ))
    return issues


ALL_CHECKS = [
    check_em_dash,
    check_en_dash,
    check_abbreviations,
    check_ai_genitive,
    check_ngo_genitive,
    check_unwanted_brands,
    check_foreign_genitive,
]


# ---------------------------------------------------------------------------
# Run / report
# ---------------------------------------------------------------------------

def run_qa(root: Path) -> QAResult:
    """Run all 7 checks against every scannable file under root."""
    result = QAResult(
        client_path=str(root.resolve()),
        started_at=datetime.now().isoformat(timespec="seconds"),
    )
    files = discover_files(root)
    for f in files:
        result.scanned_files.append(str(f.relative_to(root)))
        for line_num, line in iter_lines(f):
            for check in ALL_CHECKS:
                result.issues.extend(check(f, line_num, line, root))
    result.finished_at = datetime.now().isoformat(timespec="seconds")
    return result


def render_text_report(result: QAResult) -> str:
    """Human-readable report. Used for console output AND .md file save."""
    by_check = result.by_check()
    lines: list[str] = []
    lines.append("=" * 72)
    lines.append(f"Georgian OFFER QA Report")
    lines.append(f"Client:  {result.client_path}")
    lines.append(f"Scanned: {len(result.scanned_files)} files")
    lines.append(f"Started: {result.started_at}")
    lines.append(f"Result:  {'FAIL' if result.failed else 'PASS'} "
                 f"({result.total} issue{'s' if result.total != 1 else ''})")
    lines.append("=" * 72)

    if not result.issues:
        lines.append("")
        lines.append("✅ All 7 checks passed. Client folder is delivery-ready.")
        lines.append("")
        return "\n".join(lines)

    lines.append("")
    for check_id in sorted(by_check):
        check_issues = by_check[check_id]
        # Use first issue's name as the section title
        name = check_issues[0].check_name
        lines.append(f"── Check #{check_id}: {name}  "
                     f"({len(check_issues)} hit{'s' if len(check_issues) != 1 else ''}) "
                     f"{'—' if any(i.severity == SEV_ERROR for i in check_issues) else ''}")
        for i in check_issues:
            flag = "🔧" if i.auto_fixable else "👀"
            lines.append(f"   {flag} {i.file}:{i.line}:{i.column}")
            lines.append(f"      found:    {i.text!r}")
            if i.suggested_fix:
                lines.append(f"      suggested: {i.suggested_fix!r}")
            ctx = i.line_content.strip()
            if len(ctx) > 140:
                ctx = ctx[:139] + "…"
            lines.append(f"      context:  {ctx}")
        lines.append("")

    lines.append("─" * 72)
    lines.append(f"Legend: 🔧 = auto-fixable   👀 = manual review required")
    lines.append("─" * 72)
    return "\n".join(lines)


def render_markdown_report(result: QAResult) -> str:
    """Markdown report suitable for committing to the client folder."""
    by_check = result.by_check()
    lines: list[str] = []
    lines.append(f"# Georgian OFFER QA Report")
    lines.append("")
    lines.append(f"- **Client folder:** `{result.client_path}`")
    lines.append(f"- **Generated:** {result.started_at}")
    lines.append(f"- **Files scanned:** {len(result.scanned_files)}")
    lines.append(f"- **Total issues:** {result.total}")
    lines.append(f"- **Status:** {'❌ FAIL' if result.failed else '✅ PASS'}")
    lines.append("")

    if not result.issues:
        lines.append("All 7 checks passed. The OFFER is delivery-ready.")
        return "\n".join(lines)

    lines.append("## Summary by check")
    lines.append("")
    lines.append("| # | Check | Hits | Auto-fixable |")
    lines.append("|---|-------|------|--------------|")
    for check_id in sorted(by_check):
        check_issues = by_check[check_id]
        name = check_issues[0].check_name
        n_fix = sum(1 for i in check_issues if i.auto_fixable)
        total = len(check_issues)
        lines.append(f"| {check_id} | {name} | {total} | {n_fix} |")
    lines.append("")

    lines.append("## Detailed findings")
    lines.append("")
    for check_id in sorted(by_check):
        check_issues = by_check[check_id]
        name = check_issues[0].check_name
        lines.append(f"### Check #{check_id}: {name}")
        lines.append("")
        for i in check_issues:
            flag = "🔧 auto-fix" if i.auto_fixable else "👀 manual"
            lines.append(f"- `{i.file}:{i.line}:{i.column}` {flag}")
            lines.append(f"  - Found: `{i.text}`")
            if i.suggested_fix:
                lines.append(f"  - Suggested: `{i.suggested_fix}`")
            ctx = i.line_content.strip()
            if len(ctx) > 200:
                ctx = ctx[:199] + "…"
            lines.append(f"  - Context: `{ctx}`")
        lines.append("")

    lines.append("---")
    lines.append(f"_Generated by `tools/offer_qa.py` at {result.finished_at}_")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Auto-fix
# ---------------------------------------------------------------------------

def apply_fixes(result: QAResult) -> dict[str, int]:
    """Apply auto-fixable transforms in-place to the scanned files.

    Returns a dict of {file_path: fix_count}.
    Strategy: rebuild the file once with all fixes for that file applied
    in a single pass, to avoid offset drift.
    """
    if not result.issues:
        return {}

    # Group issues by file
    by_file: dict[Path, list[Issue]] = {}
    for issue in result.issues:
        if not issue.auto_fixable:
            continue
        fpath = Path(issue.file)
        if not fpath.is_absolute():
            fpath = Path(result.client_path) / fpath
        by_file.setdefault(fpath, []).append(issue)

    counts: dict[str, int] = {}
    for fpath, issues in by_file.items():
        if not fpath.exists():
            continue
        try:
            text = fpath.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            print(f"WARN: could not read {fpath} for fix: {exc}", file=sys.stderr)
            continue

        original = text
        # Apply most common transforms in one pass per file
        text = text.replace("—", "-")
        text = text.replace("–", "-")
        for pattern, expansion in ABBREVIATIONS:
            text = pattern.sub(expansion, text)
        # AI/NGO genitive: only inside lines that don't look dative.
        # We do this line-by-line to honor _is_dative_false_positive.
        new_lines: list[str] = []
        for line in text.splitlines(keepends=True):
            if not _is_dative_false_positive(line):
                line = re.sub(r"AI-ს(\s+[\u10d0-\u10ff])", r"AI-ის\1", line)
                line = re.sub(r"NGO-ს(\s+[\u10d0-\u10ff])", r"NGO-ის\1", line)
            new_lines.append(line)
        text = "".join(new_lines)

        if text != original:
            try:
                fpath.write_text(text, encoding="utf-8")
                counts[str(fpath.relative_to(Path(result.client_path)))] = len(issues)
            except OSError as exc:
                print(f"WARN: could not write {fpath}: {exc}", file=sys.stderr)
    return counts


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Georgian OFFER QA runner (7-check pattern).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument(
        "--client",
        type=Path,
        help="Path to a single client folder to scan.",
    )
    target.add_argument(
        "--root",
        type=Path,
        help="Path to the ai2026 root (used with --all).",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="When set with --root, scan every immediate subfolder as a client.",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Auto-fix safe issues (em-dash, en-dash, abbreviations, AI/NGO genitive).",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Save a markdown _qa_report_*.md to the client folder.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON to stdout (suppresses text report).",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress the text report (still exit with correct code).",
    )
    args = parser.parse_args(argv)

    # Determine the list of client folders to scan
    if args.client:
        clients: list[Path] = [args.client]
    else:
        if not args.all:
            parser.error("--root requires --all")
        if not args.root or not args.root.is_dir():
            print(f"ERROR: --root must be an existing directory: {args.root}",
                  file=sys.stderr)
            return 2
        # Treat every immediate subdirectory as a client folder
        clients = sorted(
            d for d in args.root.iterdir()
            if d.is_dir() and not d.name.startswith(".")
        )

    overall_failed = False
    all_results: list[QAResult] = []

    for client in clients:
        try:
            result = run_qa(client)
        except (FileNotFoundError, NotADirectoryError) as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 2

        # Auto-fix if requested
        if args.fix and result.issues:
            counts = apply_fixes(result)
            if counts:
                print(f"Applied fixes in {len(counts)} file(s):", file=sys.stderr)
                for f, n in counts.items():
                    print(f"   - {f}: {n} issue(s)", file=sys.stderr)
                # Re-run to confirm clean state
                result = run_qa(client)

        all_results.append(result)
        if result.failed:
            overall_failed = True

        # Output
        if args.json:
            print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
        elif not args.quiet:
            print(render_text_report(result))

        # Save markdown report
        if args.report:
            stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_path = client / f"_qa_report_{stamp}.md"
            try:
                report_path.write_text(
                    render_markdown_report(result), encoding="utf-8"
                )
                if not args.quiet and not args.json:
                    print(f"📄 Saved report: {report_path}", file=sys.stderr)
            except OSError as exc:
                print(f"WARN: could not save report {report_path}: {exc}",
                      file=sys.stderr)

    if not args.json and not args.quiet and len(all_results) > 1:
        # Aggregate summary across all clients
        total_issues = sum(r.total for r in all_results)
        passing = sum(1 for r in all_results if not r.failed)
        print("=" * 72)
        print(f"Aggregate: {passing}/{len(all_results)} clients clean, "
              f"{total_issues} total issue(s).")
        print("=" * 72)

    return 1 if overall_failed else 0


if __name__ == "__main__":
    sys.exit(main())

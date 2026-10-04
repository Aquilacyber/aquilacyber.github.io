#!/usr/bin/env python3
"""Check the "Last reviewed" line on every page.

Each page outside the exempt list must have a line near the top that reads:

    Last reviewed: YYYY-MM-DD

Usage:
    python3 scripts/check_review_dates.py                  # format and age check
    python3 scripts/check_review_dates.py --format-only    # format check only (used on pull requests)
    python3 scripts/check_review_dates.py --max-age 365    # change the age limit in days
    python3 scripts/check_review_dates.py --report out.md  # also write a Markdown list of stale pages
    python3 scripts/check_review_dates.py --today 2026-10-04   # pretend today is this date

Exit status is 1 when a page has a missing, invalid or future date, or, unless
--format-only is given, when a page is older than the age limit.

Exempt pages are third-party copies and archives. They carry a source note
instead. See CREDITS.md.
"""
import argparse
import datetime
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKIP_DIRS = {".git", "node_modules", "_site"}
EXEMPT_PREFIXES = ("reference/free-training/", "reference/licenses/", ".github/")
EXEMPT_FILES = {
    "reference/cryptography.md",
    "reference/endpoint-security.md",
    "reference/incident-response.md",
    "reference/iot-security.md",
    "reference/offensive-security.md",
    "reference/threat-intelligence.md",
    "reference/threat-modeling.md",
}
# Files in templates/ are meant to be copied, so only the folder index carries a date.
TEMPLATES_INDEX = "templates/README.md"
LINE_RE = re.compile(r"^\s*\*?Last reviewed:\s*(\S+?)\*?\s*$", re.M)
HEAD_LINES = 15


def exempt(rel):
    if rel in EXEMPT_FILES or rel.startswith(EXEMPT_PREFIXES):
        return True
    return rel.startswith("templates/") and rel != TEMPLATES_INDEX


def pages():
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in sorted(fns):
            if fn.endswith(".md"):
                rel = os.path.relpath(os.path.join(dp, fn), ROOT).replace(os.sep, "/")
                if not exempt(rel):
                    yield rel


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max-age", type=int, default=365)
    ap.add_argument("--format-only", action="store_true")
    ap.add_argument("--report")
    ap.add_argument("--today")
    args = ap.parse_args()
    today = datetime.date.fromisoformat(args.today) if args.today else datetime.date.today()

    bad, stale, n = [], [], 0
    for rel in pages():
        n += 1
        with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as fh:
            head = "".join(fh.readline() for _ in range(HEAD_LINES))
        m = LINE_RE.search(head)
        if not m:
            bad.append((rel, "no 'Last reviewed: YYYY-MM-DD' line in the first lines"))
            continue
        try:
            d = datetime.date.fromisoformat(m.group(1))
        except ValueError:
            bad.append((rel, f"invalid date '{m.group(1)}', use YYYY-MM-DD"))
            continue
        if d > today:
            bad.append((rel, f"date {d} is in the future"))
        elif (today - d).days > args.max_age:
            stale.append((rel, d, (today - d).days))

    print(f"Checked {n} pages.")
    if bad:
        print(f"{len(bad)} page(s) with a missing or invalid date:")
        for rel, why in bad:
            print(f"  {rel}: {why}")
    if stale and not args.format_only:
        print(f"{len(stale)} page(s) not reviewed in the last {args.max_age} days:")
        for rel, d, age in sorted(stale, key=lambda x: x[1]):
            print(f"  {rel}: reviewed {d} ({age} days ago)")
    if args.report:
        if stale and not args.format_only:
            with open(args.report, "w", encoding="utf-8") as out:
                out.write(f"These pages were last reviewed more than {args.max_age} days ago. ")
                out.write("Check each one for facts, prices, exam codes, regulations and links that have changed, ")
                out.write("then update its `Last reviewed` date. See CONTRIBUTING.md.\n\n")
                out.write("| Page | Last reviewed | Days ago |\n|---|---|---|\n")
                for rel, d, age in sorted(stale, key=lambda x: x[1]):
                    out.write(f"| `{rel}` | {d} | {age} |\n")
        elif os.path.exists(args.report):
            os.remove(args.report)
    if bad or (stale and not args.format_only):
        return 1
    print("All review dates are present and valid." if args.format_only else "All pages were reviewed recently.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Check the repository's style rules.

Rules, for original content (everything outside reference/):
  - no emoji
  - no em dashes
  - no placeholder text such as "your-invite-link"
  - none of a short list of hype words
File and folder names, everywhere:
  - lowercase letters, digits and hyphens, no spaces or parentheses
    (README.md, CONTRIBUTING.md, CREDITS.md and LICENSE are allowed)

Usage:
    python3 scripts/check_style.py
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKIP_DIRS = {".git", "node_modules", "_site", "__pycache__"}
THIRD_PARTY_DIRS = {"reference"}          # copies and archives are exempt from content rules
ALLOWED_UPPER = {"README.md", "CONTRIBUTING.md", "CREDITS.md", "LICENSE"}
NAME_OK = re.compile(r"^[a-z0-9][a-z0-9._-]*$")

EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\U0001F1E6-\U0001F1FF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u200D\u20E3]"
)
EM_DASH = "\u2014"
PLACEHOLDERS = re.compile(r"your-invite-link|your-handle|lorem ipsum|\bTBD\b|\bTODO\b|coming soon", re.I)
HYPE = re.compile(
    r"\b(delve|leverage[sd]?|seamless(?:ly)?|robust|unlock(?:s|ed|ing)?|empower(?:s|ed|ing)?|"
    r"cutting-edge|game-changer|tapestry|embark|navigate the|in today's|it's important to note|"
    r"comprehensive|(?<!Linux )journey|landscape|dive (?:in|into|deeper))\b",
    re.I,
)
HYPE_EXEMPT_FILES = {"CONTRIBUTING.md"}   # this file lists the banned words


def is_third_party(rel):
    return rel.split(os.sep)[0] in THIRD_PARTY_DIRS


def main():
    problems = []
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        rel_dir = os.path.relpath(dp, ROOT)
        in_github = rel_dir == '.github' or rel_dir.startswith('.github' + os.sep)
        for name in dns + fns:
            if in_github or name in ALLOWED_UPPER or name.startswith("."):
                continue
            if not NAME_OK.match(name) and name != "_config.yml":
                problems.append((os.path.join(rel_dir, name), "name must be lowercase, hyphenated, no spaces"))
        for fn in fns:
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dp, fn)
            rel = os.path.relpath(path, ROOT)
            if is_third_party(rel) and not rel.startswith(os.path.join("reference", "README")):
                if rel not in {os.path.join("reference", f) for f in
                               ("cloud-security.md", "defensive-tools.md", "web3-security.md", "README.md")}:
                    continue
            with open(path, encoding="utf-8", errors="replace") as fh:
                for n, line in enumerate(fh, 1):
                    if EMOJI.search(line):
                        problems.append((f"{rel}:{n}", "emoji"))
                    if EM_DASH in line:
                        problems.append((f"{rel}:{n}", "em dash"))
                    if PLACEHOLDERS.search(line):
                        problems.append((f"{rel}:{n}", "placeholder text"))
                    if fn not in HYPE_EXEMPT_FILES:
                        m = HYPE.search(line)
                        if m:
                            problems.append((f"{rel}:{n}", f"hype word: {m.group(0)}"))
    if problems:
        print(f"{len(problems)} style problem(s):")
        for where, why in problems:
            print(f"  {where}: {why}")
        return 1
    print("Style check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

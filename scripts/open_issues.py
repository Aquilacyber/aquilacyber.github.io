#!/usr/bin/env python3
"""Open the drafted issues in .github/issues-to-open/ on GitHub.

This is a dry run unless you pass --create, so nothing happens by accident.

Usage:
    python3 scripts/open_issues.py                 # show what would be created
    python3 scripts/open_issues.py --create        # create the issues
    python3 scripts/open_issues.py --create --only 03 09 11   # only these numbers

Requirements for --create: the GitHub CLI (`gh`), signed in with `gh auth login`.

Each draft starts with front matter:
    title:  the issue title
    labels: comma-separated labels (created if they do not exist)
    repo:   optional OWNER/REPO, for issues that belong in another repository

An issue is skipped if one with the same title already exists in that
repository, open or closed, so the script is safe to run more than once.
"""
import argparse
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DRAFTS = os.path.join(ROOT, ".github", "issues-to-open")
DEFAULT_REPO = "Aquilacyber/aquilacyber.github.io"
LABELS = {
    "needs-info": ("D93F0B", "Waiting for information only the maintainers have"),
    "verification": ("0E8A16", "Something to test or confirm"),
    "content": ("1D76DB", "New or changed learning content"),
    "maintenance": ("FBCA04", "Repository, tooling or process"),
    "low-priority": ("C5DEF5", "Not urgent"),
    "other-repo": ("5319E7", "Belongs in a different repository"),
}


def parse(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing front matter")
    head, body = text[4:].split("\n---\n", 1)
    meta = {}
    for line in head.splitlines():
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    labels = [x.strip() for x in meta.get("labels", "").split(",") if x.strip()]
    return {
        "file": os.path.basename(path),
        "title": meta["title"],
        "labels": labels,
        "repo": meta.get("repo") or DEFAULT_REPO,
        "body": body.strip() + "\n",
    }


def gh(*args, check=True):
    return subprocess.run(["gh", *args], capture_output=True, text=True, check=check)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--create", action="store_true", help="really create the issues")
    ap.add_argument("--only", nargs="*", help="two-digit numbers of the drafts to use, for example 03 09")
    args = ap.parse_args()

    files = sorted(f for f in glob.glob(os.path.join(DRAFTS, "[0-9][0-9]-*.md")))
    if args.only:
        files = [f for f in files if os.path.basename(f)[:2] in args.only]
    issues = [parse(f) for f in files]
    if not issues:
        print("No drafts found.")
        return 1

    print(f"{len(issues)} draft(s){'' if args.create else ' (dry run, nothing will be created)'}:")
    for i in issues:
        print(f"  {i['file'][:2]}  [{', '.join(i['labels'])}]  {i['title']}  ->  {i['repo']}")
    if not args.create:
        print("\nRun again with --create to open them.")
        return 0

    if shutil.which("gh") is None:
        print("The GitHub CLI (gh) is not installed. See https://cli.github.com/", file=sys.stderr)
        return 1
    if gh("auth", "status", check=False).returncode != 0:
        print("You are not signed in. Run: gh auth login", file=sys.stderr)
        return 1

    made = skipped = 0
    prepared = set()
    for i in issues:
        repo = i["repo"]
        if repo not in prepared:
            for name, (color, desc) in LABELS.items():
                gh("label", "create", name, "--color", color, "--description", desc, "--force", "--repo", repo, check=False)
            prepared.add(repo)
        found = gh("issue", "list", "--repo", repo, "--state", "all", "--search", f'"{i["title"]}" in:title',
                   "--json", "title", "--limit", "20", check=False)
        titles = [x["title"] for x in json.loads(found.stdout or "[]")]
        if i["title"] in titles:
            print(f"skip   {i['file']}: already exists")
            skipped += 1
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as tmp:
            tmp.write(i["body"])
            path = tmp.name
        cmd = ["issue", "create", "--repo", repo, "--title", i["title"], "--body-file", path]
        for label in i["labels"]:
            cmd += ["--label", label]
        result = gh(*cmd, check=False)
        os.unlink(path)
        if result.returncode == 0:
            print(f"opened {i['file']}: {result.stdout.strip()}")
            made += 1
        else:
            print(f"FAILED {i['file']}: {result.stderr.strip()}", file=sys.stderr)
    print(f"\nDone. Opened {made}, skipped {skipped}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

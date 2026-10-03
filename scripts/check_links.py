#!/usr/bin/env python3
"""Check internal links, anchors and images in the Markdown files of this repository.

Usage:
    python3 scripts/check_links.py            # check the whole repository
    python3 scripts/check_links.py roadmap    # check one folder or file

External (http/https) links are not fetched here. The weekly external check in
.github/workflows/links.yml covers those.

Exit status is 1 when any broken internal link, missing image or missing
anchor is found, so the script can gate a pull request.
"""
import os
import re
import sys
import urllib.parse

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKIP_DIRS = {".git", "node_modules", "_site"}

FENCE_RE = re.compile(r"^(```|~~~).*?^\1[^\n]*$", re.S | re.M)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$", re.M)
SETEXT_RE = re.compile(r"^ {0,3}([^\s#>*+\-`|][^\n]*)\n {0,3}(?:=+|-{2,})[ \t]*$", re.M)
HTML_ANCHOR_RE = re.compile(r"""<a\s+[^>]*?(?:name|id)\s*=\s*["']([^"']+)["']""", re.I)
HTML_ID_RE = re.compile(r"""\bid\s*=\s*["']([^"']+)["']""", re.I)
HTML_SRC_RE = re.compile(r"""<(?:img|source)\s+[^>]*?src\s*=\s*["']([^"']+)["']""", re.I)
HTML_HREF_RE = re.compile(r"""<a\s+[^>]*?href\s*=\s*["']([^"']+)["']""", re.I)


def slugify(text):
    """GitHub-style heading slug."""
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[*_`~]", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return text.replace(" ", "-")


def strip_code(text):
    text = FENCE_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def collect_anchors(text):
    anchors, seen = set(), {}
    body = FENCE_RE.sub("", text)
    titles = [m.group(2) for m in HEADING_RE.finditer(body)]
    titles += [m.group(1) for m in SETEXT_RE.finditer(body)]
    for title in titles:
        slug = slugify(title)
        n = seen.get(slug, 0)
        seen[slug] = n + 1
        anchors.add(slug if n == 0 else f"{slug}-{n}")
    anchors.update(HTML_ANCHOR_RE.findall(text))
    anchors.update(HTML_ID_RE.findall(text))
    return anchors


def inline_targets(text):
    """Yield link targets from [text](target) and ![alt](target), allowing balanced parentheses."""
    i = 0
    while True:
        i = text.find("](", i)
        if i == -1:
            return
        j = i + 2
        if j < len(text) and text[j] == "<":
            k = text.find(">", j)
            if k == -1:
                i = j
                continue
            yield text[j + 1:k]
            i = k
            continue
        depth, k = 1, j
        while k < len(text) and depth:
            c = text[k]
            if c == "\\":
                k += 2
                continue
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
            elif c == "\n" and text[j:k].strip() == "":
                break
            k += 1
        if depth == 0:
            raw = text[j:k - 1].strip()
            m = re.match(r'^(\S+)(?:\s+(?:"[^"]*"|\'[^\']*\'))?$', raw)
            if m:
                yield m.group(1).replace("\\(", "(").replace("\\)", ")")
        i = j


def iter_markdown(paths):
    for p in paths:
        p = os.path.abspath(p)
        if os.path.isfile(p):
            if p.endswith(".md"):
                yield p
            continue
        for dp, dns, fns in os.walk(p):
            dns[:] = [d for d in dns if d not in SKIP_DIRS]
            for fn in sorted(fns):
                if fn.endswith(".md"):
                    yield os.path.join(dp, fn)


def main(argv):
    targets = argv[1:] or [ROOT]
    files = sorted(set(iter_markdown(targets)))
    anchor_cache, errors, checked = {}, [], 0

    def anchors_of(path):
        if path not in anchor_cache:
            with open(path, encoding="utf-8", errors="replace") as fh:
                anchor_cache[path] = collect_anchors(fh.read())
        return anchor_cache[path]

    for f in files:
        with open(f, encoding="utf-8", errors="replace") as fh:
            raw = fh.read()
        text = strip_code(raw)
        refs = list(inline_targets(text)) + HTML_SRC_RE.findall(text) + HTML_HREF_RE.findall(text)
        for url in refs:
            if not url or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url) or url.startswith("//"):
                continue
            checked += 1
            path, _, frag = url.partition("#")
            path = urllib.parse.unquote(path.split("?")[0])
            rel = os.path.relpath(f, ROOT)
            if path.startswith("/"):
                errors.append((rel, url, "absolute path, use a relative link"))
                continue
            dest = f if path == "" else os.path.normpath(os.path.join(os.path.dirname(f), path))
            if not os.path.exists(dest):
                errors.append((rel, url, "file not found"))
                continue
            if frag and os.path.isfile(dest) and dest.endswith(".md"):
                if urllib.parse.unquote(frag) not in anchors_of(dest):
                    errors.append((rel, url, "anchor not found"))

    print(f"Checked {len(files)} Markdown files and {checked} internal references.")
    if errors:
        print(f"{len(errors)} problem(s):")
        for rel, url, why in errors:
            print(f"  {rel}: {url}  ({why})")
        return 1
    print("No broken internal links.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

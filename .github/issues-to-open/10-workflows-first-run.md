---
title: Confirm the three workflows run
labels: verification
---

**Context.** `.github/workflows/checks.yml`, `links.yml` and `review-dates.yml` were checked as YAML only. They have not run on GitHub.

**Steps.**
1. Open a pull request and confirm `checks.yml` passes.
2. Start `links.yml` by hand with "Run workflow". Check that the lychee options are accepted, that the `--exclude-path` patterns skip only the third-party copies and that example addresses are ignored.
3. Start `review-dates.yml` by hand. It should report nothing, because every page is dated 2026-10-03. Confirm that it has permission to create issues when it does find something.

**Done when.** All three have run once without errors.

---
title: Add a spell check to CI
labels: maintenance
---

**Why.** Running codespell over the repository found real typos in original pages, which were fixed. Nothing stops new ones.

**Proposal.** Add codespell to `checks.yml` with a skip list for the third-party copies under `reference/` and a short list of accepted words.

**Done when.** The check passes on the current repository and fails on a seeded typo.

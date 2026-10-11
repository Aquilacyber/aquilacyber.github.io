---
title: Add a site build and crawl check to CI
labels: maintenance
---

**Why.** A test build with real Jekyll found two problems that `scripts/check_links.py` could not see: `CONTRIBUTING.md` was skipped by the front matter plugin and a link to a folder of text files led nowhere. Both only exist on the published site.

**Proposal.**
1. Add a workflow that builds the site with the same plugins.
2. Add a small script that crawls the built `_site` folder and fails on any internal link whose target does not exist.
3. Run it on pull requests.

**Done when.** The workflow catches a deliberately broken link in a test pull request.

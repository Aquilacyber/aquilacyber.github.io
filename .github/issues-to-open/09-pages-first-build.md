---
title: Check the first GitHub Pages build and the theme
labels: verification
---

**Context.** A test build with Jekyll 4.3.2 and the same plugins, without the theme, produced 112 pages and no broken internal links. The `include:` setting for `CONTRIBUTING.md` and the licences index page were added after that test found two problems.

**Not tested.** The `jekyll-theme-minimal` layout, GitHub's own Pages build and the live site. One maintainer saw `ERR_CONNECTION_REFUSED` for aquilacyber.github.io in a browser, which usually points to the local network and not to the site.

**Steps.**
1. Push, then open Settings, Pages. Choose "Deploy from a branch", `main`, `/ (root)`.
2. Open the live site on desktop and on a phone.
3. Check ten pages: the home page, a track, a career profile, a domain page, a template, the glossary.
4. Check that tables, code blocks and the `- [ ]` checklists display acceptably. Checklists may show as plain text.
5. If the layout is poor, remove `theme:` and the plugins from `_config.yml` and rely on GitHub's own Markdown rendering.

**Done when.** The site is live and the ten pages look right.

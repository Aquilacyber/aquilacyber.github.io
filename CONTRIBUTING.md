# Contributing

Last reviewed: 2026-10-03

Thank you for helping. The most useful contributions are small: a dead link fixed, an unclear sentence rewritten, an out-of-date fact corrected, one good resource added.

## Report a problem

Open an issue and pick the matching template: broken link, wrong or outdated information, or new resource suggestion. Say which page and what is wrong.

## Make a change

1. Fork the repository and make a branch.
2. Make your change.
3. Run the checks:

   ```
   python3 scripts/check_links.py
   python3 scripts/check_style.py
   ```

4. Open a pull request. Say what you changed and why.

Both scripts use only the Python standard library.

## Adding a resource

A resource belongs in [resources/](resources/README.md) when it meets all of these:

- It is free, or it is clearly marked as paid and nothing free does the same job.
- A beginner can use it without extra background.
- You have used it yourself.
- You can say in one line what a beginner gets from it.

Put the one-line description next to the link. Do not copy text from the resource's own site.

## Adding a page

Write the page in your own words. Pages in this repository follow the same pattern: what it is, who it is for, what to do and how to know you are done. Look at an existing page in the same folder first.

Wanted pages:

- Careers: security awareness specialist, third-party risk analyst, security product manager
- Tracks: vulnerability management, mobile security
- Python for security basics
- Git and GitHub for your portfolio
- How to read a CVE and a vendor advisory
- Notes from your own experience getting a first role in Nigeria

## Review dates

Every page outside `reference/` carries a line near the top that reads `Last reviewed: YYYY-MM-DD`. That date means a person read the page, checked the facts and links that can be checked, and fixed or removed what was out of date. Update the date only when you have actually done that. Do not change it to quiet the check.

`python3 scripts/check_review_dates.py` checks the format. A monthly workflow opens an issue that lists pages not reviewed in the last 365 days.

## Third-party material

Do not copy text, lists or images from another project unless its licence allows it. "Found it on GitHub" is not a licence. A repository with no licence file is all rights reserved by default. If you add permitted material, put it under `reference/`, include the licence text in `reference/licenses/`, add a source note at the top of the page and add a row to [CREDITS.md](CREDITS.md). When in doubt, link to the original instead of copying it.

## Style

- Write plainly. Short sentences. Say what you mean.
- No emoji.
- No em dashes. Use a comma, a colon, brackets or a new sentence.
- No hype words. Do not call anything powerful, comprehensive, robust or seamless. Say what it does.
- Say what you actually know. If a fact can change, such as an exam code or a price, say where to check it.
- Write for someone who is starting. Define a term the first time you use it, or link to the [glossary](guides/glossary.md).
- Use relative links between pages.
- Name files and folders in lowercase with hyphens and no spaces.
- Keep one idea per paragraph.

## Ground rules

- Never add instructions that help someone attack a system they do not have permission to test.
- Never publish real credentials, personal data or answers to active competitions.
- Be respectful in issues and reviews.

## Licence

By contributing you agree that your contribution is released under [CC BY 4.0](LICENSE), the same as the rest of the original content.

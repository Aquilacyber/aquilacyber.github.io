# Issues to open

Drafts of the open items found while building and testing this repository. Each file is one issue, ready to open. They cover things that need information from the maintainers, things that need testing on GitHub, and content still to be written.

## Open them all

After you sign in with the GitHub CLI (`gh auth login`):

```
python3 scripts/open_issues.py            # dry run, lists what would be created
python3 scripts/open_issues.py --create   # creates them
```

The script creates the labels it needs and skips any issue whose title already exists, so running it twice does no harm. To open only some, add their numbers: `--only 03 09 11`.

Issue 22 belongs in a different repository (`Aquilacyber/Aquilacyber-CTF`), and the script sends it there.

## Or open them by hand

Copy the text below the front matter into a new issue and use the title and labels from the top of the file.

## Order

| Priority | Numbers | Why |
|---|---|---|
| First | 09, 10, 11 | Nothing has run on GitHub yet. These confirm that the site and the checks work |
| Needs the maintainers | 01 to 08 | Information or decisions only the maintainers can give |
| Content | 12 to 18 | New pages and templates, in order of value |
| Maintenance | 19 to 21 | Checks and housekeeping |
| Other repository | 22 | The portal README |

When an issue is finished, close it on GitHub and delete its draft file in the same pull request.

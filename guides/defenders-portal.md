# AquilaCyber Defenders Portal

Last reviewed: 2026-10-03

The Defenders Portal is AquilaCyber's own capture the flag (CTF) platform. It was built by AquilaCyber for university Defenders chapters across Africa, and any learner can register for an account. This page explains what is on it, which order to take the challenges in and what to learn first so you get more out of each one.

Portal: [ctf.aquilacyber.org](https://ctf.aquilacyber.org/). Register at [ctf.aquilacyber.org/auth/register](https://ctf.aquilacyber.org/auth/register). The source code is public at [github.com/Aquilacyber/Aquilacyber-CTF](https://github.com/Aquilacyber/Aquilacyber-CTF). The challenge list below comes from that repository as of October 2026, so check the portal for what is live now.

## What is on it

Thirteen flags across two kinds of challenge:

- Ten web security labs. Each is a small intentionally vulnerable web application.
- One investigation called Phantom Insider, an OSINT lab with three stages that you solve in sequence.

### Web security labs

| # | Lab | Weakness | Difficulty | Learn it first at |
|---|---|---|---|---|
| 1 | Login Bypass | SQL injection | Easy | PortSwigger: SQL injection |
| 2 | XSS Search | Reflected cross-site scripting | Easy | PortSwigger: Cross-site scripting |
| 3 | User Profile | Insecure direct object reference (IDOR) | Medium | PortSwigger: Access control vulnerabilities |
| 4 | Ping Tool | Command injection | Medium | PortSwigger: OS command injection |
| 5 | Secret Vault | JWT bypass | Hard | PortSwigger: JWT attacks |
| 6 | Calculator | Remote code execution | Hard | PortSwigger: server-side topics on code injection |
| 7 | Settings Panel | Cross-site request forgery (CSRF) | Medium | PortSwigger: CSRF |
| 8 | File Manager | Insecure file upload | Easy | PortSwigger: File upload vulnerabilities |
| 9 | XML Parser | XML external entity injection (XXE) | Hard | PortSwigger: XXE injection |
| 10 | URL Fetcher | Server-side request forgery (SSRF) | Medium | PortSwigger: SSRF |

The learning column points to the free [PortSwigger Web Security Academy](https://portswigger.net/web-security). Read the topic, do two or three of its labs, then come back to the portal challenge. You will solve it faster and you will understand why it worked.

### Phantom Insider

A multi-stage investigation of a corporate insider threat. You work from digital evidence to identify who did it.

| # | Stage | Goal |
|---|---|---|
| 11 | Identity resolution | Identify the insider from digital evidence |
| 12 | Geolocation | Extract EXIF metadata from recovered media |
| 13 | Data decryption | Crack credentials and decrypt the stolen archive |

This one suits learners heading toward the [blue team](../tracks/blue-team.md) and [digital forensics](../tracks/digital-forensics.md) tracks. It practises reading evidence, which matters in those tracks.

## Suggested order

1. **Start with the easy web labs:** Login Bypass, XSS Search and File Manager.
2. **Move to the medium labs:** User Profile, Settings Panel, Ping Tool and URL Fetcher.
3. **Finish with the hard labs:** Secret Vault, XML Parser and Calculator.
4. **Do Phantom Insider** whenever you want a change from web testing. It does not depend on the web labs.

Follow the same order as phase 2 of the [roadmap](../roadmap/02-hands-on.md): finish the Linux and networking parts of phase 1 first, then spend your first portal sessions on the easy web labs.

## How scoring works

- Each flag is worth 100 points, so the maximum is 1,300.
- Each hint costs 20 points. There are three hints per challenge.
- You can play solo or in a team. Create a team or join one with a six-character code. In team mode one teammate solving a challenge scores it for the team. Individual and team leaderboards are separate.
- Organisers can run timed events with a start time, an end time and a point where the leaderboard freezes.

A hint costs 20 points. That is a small price when you are learning, so use one after you have tried for about half an hour and written down what you tried.

## Rules for yourself

- Attack the challenge pages only. Do not probe the platform itself, its server or other users' accounts.
- Do not share flags or step-by-step solutions for a challenge that is part of a live event.
- Check the portal's own rules before you publish a write-up of any challenge.
- Write a short note for every challenge you solve, using the [write-up template](../templates/writeup-template.md). Include what you tried that did not work.

Read the [ethics and law guide](ethics-and-law.md) once, even though this platform exists to be attacked. The habits carry over to real targets.

## When you get stuck

Ask in the AquilaCyber community. Describe what you have tried and what happened. Ask for a nudge and not for the flag. See the [community page](community.md).

## For chapter organisers

The platform is open source under the MIT licence. It is built to be self-hosted with Docker for events. The repository contains a clear warning: it holds intentionally vulnerable code, so run it only on a private or isolated network and never on a public server next to anything you care about. Read its README and security policy before you deploy it.

## Where to go next

- More practice: the [practice labs list](../resources/practice-labs.md)
- Web testing in depth: the [red team track](../tracks/red-team.md) and the [application security track](../tracks/application-security.md)
- Investigation skills: the [digital forensics track](../tracks/digital-forensics.md)

# Red team track

Red team work is testing systems for weaknesses, with permission, and reporting what you find so it can be fixed. The words you will see are penetration testing, application security testing and bug bounty hunting.

Everything on this page depends on authorisation. Read the [ethics and law guide](../guides/ethics-and-law.md) before you start and again before you test anything that is not your own lab.

## What the work looks like

A penetration tester is hired for a defined scope and time. Most of the engagement is careful enumeration, testing and note-taking. The deliverable is a report. A tester who finds a serious flaw and cannot explain it clearly to a developer has done half the job. Few people start here. Most spend a year or two in IT, development or security operations first.

## Skills to build

- How web applications work: HTTP, cookies, sessions, authentication
- The OWASP Top 10 and how each category is exploited and fixed
- A proxy tool such as Burp Suite Community Edition
- Network scanning and service enumeration with Nmap
- Linux and Windows privilege escalation basics
- Writing a finding: title, severity, description, steps to reproduce, impact and fix

## Plan

### Weeks 1 to 4: web applications

- Complete the PortSwigger Web Security Academy [learning paths](https://portswigger.net/web-security/all-topics) for SQL injection, cross-site scripting, authentication, access control and server-side request forgery. Go past the apprentice labs into practitioner level.
- Read the [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/).
- Install [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) in your lab and attack it.

### Weeks 5 to 8: networks and hosts

- Work through the network and privilege escalation rooms on [TryHackMe](https://tryhackme.com/) and the modules on [Hack The Box Academy](https://academy.hackthebox.com/).
- Practise enumeration until it is routine: ports, services, shares, users.
- Watch [IppSec](https://www.youtube.com/channel/UCa6eh7gCkpPo5XXUDfygQQA) walkthroughs of retired machines after you have tried the machine yourself.

### Weeks 9 to 12: reporting and real programmes

- Rewrite three of your earlier write-ups as formal findings.
- Read the rules and scope of a public bug bounty programme on [HackerOne](https://www.hackerone.com/), [Bugcrowd](https://www.bugcrowd.com/) or [Intigriti](https://www.intigriti.com/). Stay inside the stated scope, always. Many beginners spend months without a valid report, so treat the early weeks as practice.

## Two projects

1. **A full test report.** Run a complete test against an intentionally vulnerable application in your lab, such as Juice Shop. Produce a professional report: executive summary, scope, method, findings with severity and evidence, and remediation advice.
2. **A small tool.** Write a script that does one useful job, for example a port scanner with banner grabbing, a login brute-force detector or a header checker for common security headers. Publish it with a README and a clear warning to use it only on systems you own or have permission to test.

## Certifications worth considering

See the [certifications guide](../guides/certifications.md). Common choices are eJPT, PNPT, CompTIA PenTest+ and, later, OSCP. Do not start with the hardest exam.

## Where it leads

[Web Penetration Tester](../careers/web-penetration-tester.md), [Network Penetration Tester](../careers/network-penetration-tester.md), [Application Security Expert](../careers/application-security-expert.md), [Bug Bounty Hunter](../careers/bug-bounty-hunter.md), [Red Team Member](../careers/red-team-member.md).

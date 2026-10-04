# Introduction to offensive security

Last reviewed: 2026-10-03

Offensive security is the work of testing systems the way an attacker would, with the owner's permission, to find weaknesses before real attackers do. It includes penetration testing, red teaming and bug bounty hunting. The results are reports that help people fix what is wrong.

Everything on this page depends on authorisation. Read the [ethics and law guide](../guides/ethics-and-law.md) before you try anything.

## Why it matters

A system that has never been attacked is a system nobody knows the strength of. Testing shows which defences work, which do not and what a real attacker could reach. It also teaches defenders how attacks look, which is why good defenders often learn the offensive side.

## Kinds of work

| Kind | What it is | Typical output |
|---|---|---|
| Vulnerability assessment | Scanning for known weaknesses. No attempt to exploit them | A prioritised list |
| Penetration test | A scoped, time-limited attempt to exploit weaknesses and show their impact | A report of findings with evidence and fixes |
| Red team | A goal-based engagement that copies a real attacker and tests detection and response as well as technology | A report and a debrief with the defenders |
| Bug bounty | A public programme that pays for valid reports within its rules | Individual reports |
| Purple team | Red and blue teams working together so defenders learn from each step | Improved detections |

Tests are described by how much the tester knows in advance. **Black box** means nothing. **Grey box** means some information, such as a user account. **White box** means full access to source code and configuration.

## The phases of a test

1. **Planning and scope.** Agree what may be tested, when, how and who to call if something breaks. Get it in writing.
2. **Reconnaissance.** Collect information about the target.
3. **Scanning and enumeration.** Find hosts, services, applications and accounts.
4. **Exploitation.** Try to use weaknesses to gain access, within the scope.
5. **Post-exploitation.** Show what the access allows, such as reaching other systems or data, within the rules.
6. **Reporting.** Write findings clearly, with evidence, impact and fixes.
7. **Retest.** Check that the fixes worked.

Teams often describe attacker behaviour with [MITRE ATT&CK](https://attack.mitre.org/), which gives both sides a shared language. The [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) is the standard method for testing web applications.

## Rules that never change

- Written authorisation before anything starts
- A defined scope. Anything outside it is off limits
- Rules of engagement that say what is allowed, such as no denial of service
- Handle any data you see as the client's. Do not keep or share it
- Stop and report if you find something serious or something goes wrong
- Tell the truth in the report, including what you could not test

## What people in this field do

- A web or network penetration tester runs tests and writes reports.
- A red team member plans and carries out longer, goal-based engagements.
- A bug bounty hunter looks for flaws in public programmes.
- An exploit developer and a security researcher study vulnerabilities in depth. These roles are senior and rare.

Most of the job is careful enumeration, testing and note-taking. A tester who finds a serious flaw but cannot explain it to a developer has done half the work.

## Common tools

Know what each does before you use it, and use it only on your own lab or on targets you may test.

| Tool | What it does |
|---|---|
| [Nmap](https://nmap.org/) | Finds hosts, open ports and services |
| [Burp Suite](https://portswigger.net/burp) | Intercepts and modifies web traffic |
| [Metasploit Framework](https://www.metasploit.com/) | A framework of tested exploits and helpers |
| [Wireshark](https://www.wireshark.org/) | Shows network traffic |
| [John the Ripper](https://www.openwall.com/john/) and [hashcat](https://hashcat.net/hashcat/) | Test password strength on hashes you have permission to test |
| Greenbone OpenVAS and Nessus | Vulnerability scanners |

The [offensive security reference page](../reference/offensive-security.md) is a long list organised by the stage of an attack. It describes attacker techniques, so read it with the ethics guide in mind.

## Try it in your lab

1. Scan a vulnerable VM in your lab with Nmap and explain every line of the output.
2. Run [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) and work through its easy challenges.
3. Solve the web labs on the [AquilaCyber Defenders Portal](../guides/defenders-portal.md), starting with the easy ones.
4. Work through the apprentice labs on the [PortSwigger Web Security Academy](https://portswigger.net/web-security).
5. Write one finding in the format of the [penetration test report template](../templates/pentest-report-template.md).

## Mistakes beginners make

- Running tools without knowing what they do
- Testing something that is not in scope
- Skipping notes, then being unable to reproduce a finding
- Writing a report that lists tool output and no explanation
- Learning attacks and never learning how to fix them

## Where to go next

- The [red team track](../tracks/red-team.md)
- Roles: [Web Penetration Tester](../careers/web-penetration-tester.md), [Network Penetration Tester](../careers/network-penetration-tester.md), [Red Team Member](../careers/red-team-member.md), [Bug Bounty Hunter](../careers/bug-bounty-hunter.md)
- Practice platforms: the [practice labs list](../resources/practice-labs.md)
- Related: [network security](network-security.md) and [cryptography](cryptography.md)

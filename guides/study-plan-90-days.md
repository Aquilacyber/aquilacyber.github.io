# 90-day study plan

Last reviewed: 2026-10-03

A daily schedule for your first three months. It covers phase 1 of the [roadmap](../roadmap/01-foundations.md) and the start of phase 2. It assumes one to two hours a day, six days a week, with one rest day. If you can only manage a few hours a week, spread each block over more days. Finishing the block matters more than finishing it on time.

You will not be job-ready at day 90. You will have a solid base, a lab, a first set of write-ups and a clear idea of which track to pick.

| Days | Topic | Output |
|---|---|---|
| 1 to 10 | Networking | A subnetting worksheet and a Wireshark capture with notes |
| 11 to 20 | Linux command line | OverTheWire Bandit to level 15 |
| 21 to 30 | Security concepts | One page explaining the CIA triad, hashing and common attacks in your own words |
| 31 to 40 | Windows and logs | Notes on ten Windows event IDs and what they record |
| 41 to 50 | Python and Git | A log-parsing script on GitHub |
| 51 to 60 | Lab and scanning | A working lab and an Nmap scan write-up |
| 61 to 70 | Web basics | Ten PortSwigger apprentice labs and two write-ups |
| 71 to 80 | Guided path | One third of a TryHackMe path, with write-ups |
| 81 to 90 | Review and decide | A track choice and a plan for the next 12 weeks |

## Days 1 to 10: networking

- Days 1 to 3: IP addressing, subnet masks and CIDR notation. Practise by hand until you can split a /24 into smaller subnets.
- Days 4 to 5: DNS, DHCP and how a device gets online.
- Days 6 to 7: TCP and UDP, ports, the three-way handshake.
- Days 8 to 9: HTTP, HTTPS and TLS. Look at a request in your browser's developer tools.
- Day 10: capture your own traffic in Wireshark and annotate it.

Use [Professor Messer](https://www.professormesser.com/) and the Pre Security path on [TryHackMe](https://tryhackme.com/). Read the [network security basics](network-security-basics.md) page at the end of the block.

## Days 11 to 20: Linux

- Days 11 to 13: navigation, files, permissions, users.
- Days 14 to 16: pipes, redirection, `grep`, `find`, `sed` and `awk` at a basic level.
- Days 17 to 18: processes, services, package managers and SSH.
- Days 19 to 20: finish Bandit to level 15 and write your notes.

Use the [Linux basics guide](linux-basics.md), [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) and [Linux Journey](https://linuxjourney.com/).

## Days 21 to 30: security concepts

- Days 21 to 22: confidentiality, integrity, availability. Threats, vulnerabilities and risk.
- Days 23 to 24: authentication, authorisation and MFA. Password storage and why it uses hashes.
- Days 25 to 26: symmetric and public key encryption at a high level, and TLS.
- Days 27 to 28: common attacks: phishing, malware, SQL injection, cross-site scripting, denial of service.
- Days 29 to 30: write your one-page summary and test yourself against the [glossary](glossary.md).

Use the free Security+ videos on [Professor Messer](https://www.professormesser.com/), matched to the current exam.

## Days 31 to 40: Windows and logs

- Days 31 to 33: Windows users, groups, services and the registry. Read parts 1 and 2 of the [Windows and Active Directory basics](windows-and-active-directory.md) guide.
- Days 34 to 36: the Event Viewer. Learn the event IDs for logon success and failure, account creation and process creation.
- Days 37 to 38: basic PowerShell.
- Days 39 to 40: read a sample log set and write down what you can tell from it.

## Days 41 to 50: Python and Git

- Days 41 to 45: variables, loops, functions, files and regular expressions, using [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/).
- Days 46 to 47: Git basics: init, add, commit, push. Create your portfolio repository on GitHub.
- Days 48 to 50: write a script that counts failed logins per IP address in a log file. Commit it with a README.

## Days 51 to 60: lab and scanning

- Days 51 to 53: follow the [lab setup guide](lab-setup.md). Install VirtualBox, Kali and one vulnerable target on a host-only network.
- Days 54 to 56: read the [ethics and law guide](ethics-and-law.md) again. Learn Nmap host discovery and port scanning against your own lab.
- Days 57 to 58: capture the scan in Wireshark and find your own probes in the capture.
- Days 59 to 60: write up the scan.

## Days 61 to 70: web basics

- Days 61 to 62: how web applications work: requests, cookies, sessions.
- Days 63 to 65: SQL injection labs on the [PortSwigger Web Security Academy](https://portswigger.net/web-security).
- Days 66 to 67: cross-site scripting labs.
- Days 68 to 70: access control and authentication labs. Write up two of them.

## Days 71 to 80: guided path

Pick one path on TryHackMe and start it. Aim for a third of it. Write up every room you finish. Register on the [AquilaCyber Defenders Portal](https://ctf.aquilacyber.org/) and solve a few challenges there too. The [guide](defenders-portal.md) gives an order. Choose a path matching the track you suspect you like, and be ready to change your mind.

## Days 81 to 90: review and decide

- Days 81 to 83: go through the [progress checklist](progress-checklist.md) and mark what you can honestly do.
- Days 84 to 86: fill the biggest gap with extra practice.
- Days 87 to 88: read the eleven [domain introductions](../domains/README.md), then [phase 3](../roadmap/03-pick-a-track.md) and the track pages.
- Days 89 to 90: choose a track and write the 12-week plan in your portfolio repository.

## If you fall behind

Do not skip ahead. Take the missed days off the end of the block you are in and keep going. A plan that stretches to 120 days is still a plan that finishes.

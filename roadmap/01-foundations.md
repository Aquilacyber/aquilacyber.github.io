# Phase 1: Foundations

**Time:** about 6 weeks at 8 to 10 hours a week.

**Goal:** understand how computers and networks work well enough that security concepts make sense. Most beginners who struggle in phase 2 skipped this one.

You do not need a lab for this phase. A laptop and a browser are enough. If you do not have a laptop, read the [lab setup guide](../guides/lab-setup.md) first.

## 1. Networking (weeks 1 and 2)

Learn: IP addresses and subnets, DNS, TCP and UDP, ports, HTTP and HTTPS, what a router, switch and firewall each do, and the OSI model as vocabulary. You do not need to memorise every layer. You do need to know what people mean when they say "layer 7".

Use:
- [Professor Messer's Network+ course](https://www.professormesser.com/): free videos. You are using the exam objectives as a syllabus. You do not have to sit the exam.
- [Cisco Networking Academy](https://www.netacad.com/): free self-paced courses. Check the current list.
- The Pre Security path on [TryHackMe](https://tryhackme.com/).

Do:
- Split a /24 network into four /26 subnets on paper, with no calculator.
- Install [Wireshark](https://www.wireshark.org/), open a page in your browser and find the DNS query and the TLS handshake in the capture.

## 2. The Linux command line (weeks 2 to 4)

Learn: files and directories, permissions, users and groups, processes, pipes and redirection, `grep`, `find`, `sed` and `awk` at a basic level, package managers and SSH.

Use:
- [OverTheWire Bandit](https://overthewire.org/wargames/bandit/): a game played in a terminal over SSH. It runs from any machine with an SSH client, including a phone.
- [Linux Journey](https://linuxjourney.com/): short lessons with exercises.
- [The Linux Command Line](https://linuxcommand.org/tlcl.php) by William Shotts: a free book.

Do: reach Bandit level 15 without looking up the solution.

## 3. Core security concepts (weeks 3 to 5)

Learn: confidentiality, integrity and availability; authentication and authorisation; multi-factor authentication; hashing and encryption and why they are different; public key cryptography at a high level; the common attack types (phishing, malware, password attacks, SQL injection, denial of service); the difference between a threat, a vulnerability and a risk; defence in depth.

Use:
- [Professor Messer's Security+ course](https://www.professormesser.com/). The exam code changes over time, so pick the course that matches the current exam. Again, treat it as a syllabus.
- The [glossary](../guides/glossary.md) in this repository for quick definitions.

Do: explain to a friend, in plain words, why a password should be hashed and not encrypted.

## 4. Windows basics (week 5)

Most organisations run Windows. Learn users and groups, the registry, services, the Event Viewer and basic PowerShell commands.

Use: the Windows Fundamentals rooms on [TryHackMe](https://tryhackme.com/).

## 5. Scripting (weeks 4 to 6)

Pick Python. Learn variables, loops, functions, reading and writing files, regular expressions and making HTTP requests. Bash comes later and is easier once you know Python.

Use:
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/): free to read online.
- [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/): free course with exercises.

Do: write a script that reads a log file and counts failed SSH logins per IP address. Sample `auth.log` files are easy to find, and you can generate your own later in phase 2.

## Checkpoint

You are ready for phase 2 when you can do all of these without looking anything up:

- [ ] Explain what happens, step by step, when you type a web address into a browser and press Enter.
- [ ] Subnet a /24 network by hand.
- [ ] Move around a Linux system, change file permissions and search the contents of files from the terminal.
- [ ] Explain the difference between hashing and encryption, and between a threat and a vulnerability.
- [ ] Write a short Python script that reads a file and prints a summary of it.

Next: [Phase 2, Hands-on](02-hands-on.md).

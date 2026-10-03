# Phase 2: Hands-on

**Time:** about 10 weeks at 8 to 10 hours a week.

**Goal:** stop reading and start doing. You will build a small lab, finish one guided learning path and learn to write up what you solve. This phase is where you find out which part of security you enjoy.

Before you run any scanner or attack tool, read the [ethics and law guide](../guides/ethics-and-law.md). The short version: only touch systems you own or have written permission to test.

## 1. Set up a lab (week 1)

Follow the [lab setup guide](../guides/lab-setup.md). A working lab is one virtualisation program, one attacker machine and one deliberately vulnerable target on an isolated network. If your hardware cannot run virtual machines, use the browser-based options in that guide and carry on.

## 2. Finish one guided path (weeks 1 to 8)

Pick one beginner path on [TryHackMe](https://tryhackme.com/) and finish it. Choose by what you think you want to do:

- Interested in attacking systems: a penetration testing path.
- Interested in detecting attacks: a SOC analyst path.
- No idea yet: the shortest beginner path on the current list.

The platform changes its path names, so look at what is on offer when you start. Finishing matters more than which path you pick. Alongside it:

- Finish [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) if you have not already, then start Natas for web basics.
- Play [picoCTF](https://picoctf.org/), a beginner-friendly capture the flag run by Carnegie Mellon University. Its practice area stays open all year.
- Work through the apprentice-level labs on the [PortSwigger Web Security Academy](https://portswigger.net/web-security). It is free and it is the best resource for learning how web attacks work.

## 3. Write up what you solve (every week)

Write a short report for every room, machine or lab you finish. Use this structure:

1. **Target and goal.** What was it and what were you trying to do?
2. **Approach.** What did you try, including what failed?
3. **Solution.** The steps that worked, with the commands.
4. **What I learned.** One or two sentences. What would you do faster next time?

Do not publish flags or answers for active competitions, and check the platform's rules before you publish a write-up for a live machine. Retired machines and your own lab notes are fine.

Keep the write-ups in a public GitHub repository. In phase 4 they become your portfolio.

## 4. Learn to read traffic and logs (weeks 6 to 10)

Whatever track you choose later, you need this skill.

- Capture traffic with Wireshark while you scan your own lab target with Nmap, then find your own scan in the capture.
- Read the [Nmap book](https://nmap.org/book/) chapters on port scanning.
- Generate failed SSH logins against your own lab machine and write a script that detects them.

## Checkpoint

You are ready for phase 3 when:

- [ ] Your lab runs and you can rebuild it from scratch in under an hour.
- [ ] You have finished one full guided path.
- [ ] You have published at least three write-ups.
- [ ] You can scan a lab host with Nmap and explain every line of the output.
- [ ] You have solved at least ten PortSwigger apprentice labs, or ten equivalent exercises, and can explain how SQL injection and cross-site scripting work.

Next: [Phase 3, Pick a track](03-pick-a-track.md).

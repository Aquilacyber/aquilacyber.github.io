# Ethics and law

Security tools are the same tools criminals use. What separates a professional from a criminal is permission.

This page is general guidance for learners. It is not legal advice. If you are unsure whether something is allowed, do not do it and ask someone qualified.

## The rule

Test only systems you own, or systems where the owner has given you written permission that states what you may do, when and against which targets.

"I was only looking" and "I wanted to help" are not permission. Neither is a bug bounty programme's general invitation when you step outside its stated scope.

## What is fine

- Your own lab: virtual machines on your own computer, on an isolated network.
- Deliberately vulnerable targets built for practice, such as Juice Shop, DVWA and VulnHub machines, run in your lab.
- Platforms that give you a target to attack and say so, such as TryHackMe, Hack The Box, picoCTF and OverTheWire. Follow their rules.
- Bug bounty programmes, inside their published scope and rules.
- Your own accounts and devices.

## What is not

- Scanning or testing your school, university, employer, ISP or neighbour's network without written permission.
- Testing a website you use, even if you think it is weak.
- Running a tool you found without knowing what it does.
- Accessing data you come across by accident beyond what is needed to confirm and report the problem.
- Keeping, sharing or selling any data you should not have.
- Denial-of-service testing against anything that is not yours.

## The law in Nigeria

The Cybercrimes (Prohibition, Prevention, etc.) Act 2015 was amended in February 2024. Among other things it makes unlawful access to a computer an offence. The definitions are broad and the test turns on authorisation. Read the Act yourself and, if you plan to do paid security work, talk to a lawyer who understands it. Other countries have similar laws, and they can apply when you test a system located abroad.

## Handling malware

Malware analysis is a legitimate skill. Do it only in an isolated virtual machine with no network access and no shared folders, on a snapshot you can discard. Do not run live malware on your main computer, and do not send it to anyone.

## If you find a vulnerability by accident

1. Stop. Do not look further or try to prove how bad it is.
2. Write down what you saw, when and how you came across it. Do not keep any data.
3. Look for a security contact on the organisation's website, often a `security.txt` file or a "report a vulnerability" page.
4. Report it plainly: what you found, where and how to reproduce it. Do not demand payment and do not threaten to publish.
5. Give the organisation a reasonable time to fix it before you say anything in public.

Some organisations respond well. Some respond badly. This is why learning on your own lab and on platforms built for it is safer.

## Professional ethics

Professional bodies publish codes of ethics. The [ISC2 Code of Ethics](https://www.isc2.org/ethics) is a good short one to read. The common themes are to protect society and the public, act honestly, give diligent service and advance the profession.

## Quick test before you start any test

1. Do I own this system, or do I have written permission?
2. Does the permission cover this target and this method?
3. Could this harm real people, real data or a real service?
4. Would I be comfortable explaining exactly what I did to the owner?

If any answer is no or unclear, stop.

# Digital forensics track

Last reviewed: 2026-10-03

Digital forensics is the work of finding out what happened on a computer or network and proving it. It is used after a security incident, in internal investigations and, in some cases, in legal proceedings. Incident response teams use it to find out how an attacker got in and what they touched.

This track suits people who like detail, patience and writing things down exactly.

## What the work looks like

A forensic analyst receives a device or a disk image, makes sure the original is not changed, analyses the evidence, builds a timeline of events and writes a report that another person can check. Every step is documented, because the evidence may be questioned. A lot of the work is reading artefacts: records that operating systems leave behind without being asked.

## Skills to build

- File systems: how NTFS and ext4 store files, and what remains after a file is deleted
- Hashing, to prove a copy matches the original
- Evidence handling: chain of custody, documentation and why you never work on the original
- Windows artefacts: the registry, event logs, prefetch files, shortcut files and browser history
- Memory forensics: finding running processes, network connections and injected code in a memory image
- Timeline analysis: putting events from many sources in order
- Report writing for technical and non-technical readers

## Rules for this track

Practise only on data you own, on public training images, or on cases you have written permission to examine. Do not examine another person's device without authority, and do not keep data you were not meant to see. Read the [ethics and law guide](../guides/ethics-and-law.md).

Nigeria's Evidence Act 2011 contains provisions on how computer-generated evidence is admitted in court. If you intend to do forensic work that could reach a court, learn those rules and take advice from a lawyer.

## Plan

### Weeks 1 to 4: foundations and evidence handling

- Read the [Windows and Active Directory basics](../guides/windows-and-active-directory.md) page.
- Learn how files are stored on disk and how to hash a file in Windows and Linux.
- Install FTK Imager, which Exterro offers as a free download, in a Windows lab VM and make a forensic image of a small virtual disk. Verify the hash.
- Write a one-page chain of custody form and use it for every exercise from now on.

### Weeks 5 to 8: Windows artefacts

- Learn the main artefacts: registry hives, the Security and System event logs, prefetch, shortcut files, browser history and the master file table.
- Use free tools such as [Autopsy](https://www.autopsy.com/) and Eric Zimmerman's forensic tools.
- Practise on public cases from [CyberDefenders](https://cyberdefenders.org/) and [Blue Team Labs Online](https://blueteamlabs.online/).
- Watch the 13Cubed channel on YouTube for clear explanations of artefacts.

### Weeks 9 to 12: memory, timelines and reports

- Learn memory analysis with [Volatility](https://volatilityfoundation.org/) on a public memory sample.
- Build a timeline from several sources and mark the events that matter.
- Try the Phantom Insider investigation on the [AquilaCyber Defenders Portal](../guides/defenders-portal.md), which practises reading evidence, EXIF metadata and decryption.
- Download a public case from the [NIST CFReDS](https://cfreds.nist.gov/) data sets or [Digital Corpora](https://digitalcorpora.org/) and investigate it from start to finish.
- Write the report.

## Two projects

1. **A disk investigation report.** Use the [write-up template](../templates/writeup-template.md) as a base. Take a public disk image, verify its hash, find the evidence that answers a stated question, build a timeline and write the report. Include the chain of custody log, what you did, what you found and what you could not determine.
2. **A memory forensics write-up.** Analyse a public memory image with Volatility. Identify the suspicious process, show how you found it, list the network connections and explain what the attacker did.

## Certifications worth considering

GIAC certifications such as GCFE and GCFA are well regarded and expensive. Magnet's MCFE and others exist at lower cost. Check what employers ask for before you pay. See the [certifications guide](../guides/certifications.md).

## Where it leads

[Digital Forensic Analyst](../careers/digital-forensic-analyst.md), [Incident Responder](../careers/incident-responder.md), [Malware Analyst](../careers/malware-analyst.md).

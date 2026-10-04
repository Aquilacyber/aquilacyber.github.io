# Introduction to digital forensics

Last reviewed: 2026-10-03

Digital forensics is the work of finding out what happened on a computer, phone or network and being able to prove it. It is used after a security incident, in internal investigations and, sometimes, in legal proceedings. Every step is documented so that another person can check it.

## Why it matters

When an attack is over, someone has to explain how it happened, what was taken and whether the attacker is still there. Forensics answers those questions from the evidence that systems leave behind. In some cases the answer has to stand up to a lawyer's questions, so the way evidence is handled matters as much as what it shows.

## Key ideas

- **Preserve first.** Never work on the original. Make a verified copy and analyse the copy.
- **Hashing proves a copy matches.** If the hash of the copy equals the hash of the original, they are identical.
- **Chain of custody.** A written record of who held the evidence, when, and what they did with it.
- **Order of volatility.** Collect the most fragile evidence first. Memory is lost when a machine is powered off and a disk is not. [RFC 3227](https://www.rfc-editor.org/rfc/rfc3227) gives the classic order: processor registers and cache, then routing and process tables, memory, temporary files, disk, remote logs and monitoring data, physical configuration and finally archival media.
- **Artefacts.** The traces that operating systems and programs leave without being asked, such as logs, registry entries, prefetch files, browser history and the master file table.
- **Timelines.** Putting events from many sources in order often shows the story.
- **Document everything.** Write what you did, with times, as you do it.

Kinds of forensics:

| Kind | What you examine |
|---|---|
| Disk or computer | Drives and file systems, including deleted files |
| Memory | A snapshot of what was running, including processes and network connections |
| Network | Captured traffic and logs |
| Mobile | Phones and tablets |
| Cloud | Provider logs and snapshots of cloud systems |
| Malware | Samples of malicious software, which overlaps with malware analysis |

## What people in this field do

- A digital forensic analyst collects and analyses evidence and writes the report.
- An incident responder uses forensic techniques to find out how an attacker got in and what they touched.
- A malware analyst studies the files found.
- Law enforcement and e-discovery staff handle evidence for legal cases.

The work is detailed and slow. A good report says what was found, how, and what could not be determined.

## Common tools

| Tool | What it does |
|---|---|
| FTK Imager | Makes forensic images, available free from Exterro |
| [Autopsy](https://www.autopsy.com/) and [The Sleuth Kit](https://github.com/sleuthkit/sleuthkit) | Analyse disk images and file systems |
| [Volatility](https://volatilityfoundation.org/) | Analyses memory images |
| [Eric Zimmerman's tools](https://ericzimmerman.github.io/) | Parse Windows artefacts such as the registry and the master file table |
| [Wireshark](https://www.wireshark.org/) | Analyses captured network traffic |
| SIFT Workstation | A Linux distribution that bundles forensic tools |

## Try it in your lab

Use only data you own or public training data.

1. Hash a file with `sha256sum`, copy it and hash the copy. Change one byte of the copy and hash it again.
2. Practise deletion and recovery on a small image file, which writes only to a file and nothing on your real drives:

   ```
   dd if=/dev/zero of=fat.img bs=1M count=50
   mkfs.vfat fat.img
   sudo mkdir -p /mnt/fat && sudo mount -o loop fat.img /mnt/fat
   echo "meeting notes" | sudo tee /mnt/fat/notes.txt
   sudo rm /mnt/fat/notes.txt
   sudo umount /mnt/fat
   ```

   Open `fat.img` in Autopsy and find the deleted file. You can also list it from the command line with The Sleuth Kit (`sudo apt install sleuthkit`):

   ```
   fls -r fat.img
   icat -r fat.img 3
   ```

   Deleted entries are marked with an asterisk. FAT overwrites the first character of a deleted file's name, so `notes.txt` shows up as `_otes.txt`. The number in the `fls` output is the inode. Use it with `icat -r` to recover the content, and in your own run replace `3` with the number you see. Write down the hash of the image before and after you analyse it, and check that the analysis did not change it.
3. On a Windows VM, find where the Security log, the prefetch folder and the browser history live, and say what each one can tell an investigator.
4. Try the Phantom Insider investigation on the [AquilaCyber Defenders Portal](../guides/defenders-portal.md). It practises reading digital evidence and image metadata.
5. Download a public case from [NIST CFReDS](https://cfreds.nist.gov/) or [Digital Corpora](https://digitalcorpora.org/) and write a short report on what you found.

## Mistakes beginners make

- Opening files directly on the evidence
- Forgetting to hash before and after
- Not writing down what was done and when
- Stating conclusions the evidence does not support
- Ignoring the order of volatility and powering a machine off first

## Where to go next

- The [digital forensics track](../tracks/digital-forensics.md), with a 12-week plan and two projects
- The [Windows and Active Directory basics](../guides/windows-and-active-directory.md) guide for the artefacts
- Roles: [Digital Forensic Analyst](../careers/digital-forensic-analyst.md), [Incident Responder](../careers/incident-responder.md), [Malware Analyst](../careers/malware-analyst.md)
- Related: [incident response](incident-response.md)
- Learn more: the 13Cubed channel on YouTube, and the [free training archive](../reference/free-training/README.md)

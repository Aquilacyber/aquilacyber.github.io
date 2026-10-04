# Introduction to endpoint security

Last reviewed: 2026-10-03

An endpoint is any device that connects to a network: a laptop, a desktop, a server, a phone or a tablet. Endpoint security is the work of protecting those devices, detecting attacks on them and responding when something gets through.

## Why it matters

Most attacks end on an endpoint. A phishing attachment runs on a laptop. Ransomware encrypts files on a server. Passwords are stolen from the memory of a machine. If you can see and control what happens on endpoints, you can stop a large share of attacks and investigate the rest.

## Key ideas

- **Prevention and detection.** Antivirus blocks known bad files. Endpoint detection and response (EDR) records what happens on a machine, such as which process started which, and lets analysts investigate and isolate it from a console. XDR extends the idea to email, network and cloud data, and MDR is a service where an outside team watches it for you.
- **Hardening.** Remove what is not needed and configure the rest securely. The CIS Benchmarks give step-by-step settings for each operating system.
- **Least privilege.** Ordinary users should not be local administrators.
- **Patching.** Known vulnerabilities are the easiest way in, so updates matter more than almost any tool.
- **Encryption.** Full disk encryption, such as BitLocker on Windows, protects a lost or stolen device.
- **Application control.** Allow only approved programs to run.
- **Device management.** Mobile device management lets an organisation enforce settings and wipe a lost phone.
- **Logging.** Without good logs, an investigation has nothing to work from.

| Control | What it helps stop |
|---|---|
| Patching | Exploitation of known vulnerabilities |
| Removing local admin rights | Malware changing the system, easy privilege escalation |
| Application allow-listing | Unapproved and malicious programs |
| Disk encryption | Data loss from a stolen device |
| EDR with someone watching it | Attacks that avoid signature-based tools |
| Logging such as Sysmon | Investigations with no evidence |

Common threats on endpoints include malware, ransomware, malicious documents and scripts, credential theft and persistence, where an attacker makes sure their access survives a reboot by using start-up entries, scheduled tasks, services or cron jobs.

## What people in this field do

- An endpoint or security engineer deploys, tunes and maintains the EDR and the hardening settings.
- A SOC analyst triages EDR alerts and decides what is real.
- An incident responder isolates a machine and collects evidence from it.
- A vulnerability management analyst chases patches.
- A malware analyst takes apart what was found.

## Common tools

| Tool | What it does |
|---|---|
| Microsoft Defender | Built-in antivirus and, in some editions, EDR for Windows |
| [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) | Detailed Windows logging of process, network and file activity |
| [Sysinternals Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns) | Lists everything that starts automatically on Windows |
| [osquery](https://osquery.io/) | Query your machines like a database |
| [Wazuh](https://wazuh.com/) | Open source agent with log analysis and alerting |
| [Velociraptor](https://docs.velociraptor.app/) | Endpoint visibility and forensics at scale |
| [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) | Small tests that simulate attacker techniques, for checking your detections |

## Try it in your lab

1. On a Windows VM, open Process Explorer or Task Manager and read the process tree. Pick three processes and say what each one is and what started it.
2. Run Autoruns and list five places where programs start automatically. Explain why an attacker would use one.
3. Install Sysmon with the community [SwiftOnSecurity configuration](https://github.com/SwiftOnSecurity/sysmon-config), start a program, and find the process creation event.
4. Apply one section of a CIS Benchmark to a Windows or Linux VM and note what changed. Take a snapshot first.
5. In an isolated VM, run one Atomic Red Team test for a single technique and find the evidence in your logs. Use a snapshot and do not do this on a machine you care about.

## Mistakes beginners make

- Relying on antivirus alone
- Leaving every user a local administrator
- Buying an EDR product and having nobody read its alerts
- Skipping logging because it fills the disk
- Running attack simulation on a machine that is not isolated

## Where to go next

- The [Windows and Active Directory basics](../guides/windows-and-active-directory.md) and [Linux basics](../guides/linux-basics.md) guides
- The [blue team track](../tracks/blue-team.md)
- Roles: [Security Operations Center (SOC) Analyst](../careers/security-operations-center.md), [Security Engineer (Software)](../careers/security-engineer-software.md), [Malware Analyst](../careers/malware-analyst.md)
- A long list of endpoint resources: [reference: endpoint security](../reference/endpoint-security.md)
- Learn more: [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks), [MITRE ATT&CK](https://attack.mitre.org/)

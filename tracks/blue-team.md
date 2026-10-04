# Blue team track

Last reviewed: 2026-10-03

Blue team work is detecting attacks, investigating them and limiting the damage. Most people start as a SOC analyst, which is a security operations centre role.

## What the work looks like

A SOC analyst watches alerts from tools such as a SIEM, an endpoint detection product and email security. Most alerts are false alarms. The job is to decide quickly which ones are not, collect evidence, escalate and write down what you found. The days are repetitive at first. You get better by learning what normal looks like in your organisation.

## Skills to build

- Windows event logs, Linux logs and what each one records
- How common attacks look in logs: brute force, phishing, malware execution, lateral movement
- A SIEM query language, at least basic search and filtering
- The MITRE ATT&CK framework as a shared vocabulary
- The incident handling process: preparation, detection and analysis, containment, eradication, recovery and lessons learned
- Clear written reports

## Plan

### Weeks 1 to 4: logs and visibility

- Read the [Windows and Active Directory basics](../guides/windows-and-active-directory.md) guide, including its table of event IDs.
- Install [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) on a Windows lab VM and read what it records.
- Work through the SOC analyst content on [TryHackMe](https://tryhackme.com/) or [LetsDefend](https://letsdefend.io/).

### Weeks 5 to 8: a SIEM of your own

- Install [Wazuh](https://wazuh.com/) or [Security Onion](https://securityonionsolutions.com/) in your lab and send logs to it. Check the memory requirements first, because both are heavy. The [lab setup guide](../guides/lab-setup.md) covers what to do on a small machine.
- Learn the query language of your chosen tool.
- Browse the [Sigma rules repository](https://github.com/SigmaHQ/sigma) to see how detection logic is written.

### Weeks 9 to 12: investigations

- Try the Phantom Insider investigation on the [AquilaCyber Defenders Portal](../guides/defenders-portal.md).
- Do investigation exercises on [CyberDefenders](https://cyberdefenders.org/) and [Blue Team Labs Online](https://blueteamlabs.online/).
- Study the [MITRE ATT&CK](https://attack.mitre.org/) techniques you saw in those exercises.
- Read NIST SP 800-61, the computer security incident handling guide, at [csrc.nist.gov](https://csrc.nist.gov/).

## Two projects

1. **Detection lab.** Build the SIEM from weeks 5 to 8. Generate failed logins and a few suspicious PowerShell commands against your own lab machines. Write at least five detection rules, say what each one catches and show the alert firing. Publish the rules and a README.
2. **Incident report.** Take a completed investigation exercise and write the report an employer would expect, using the [write-up template](../templates/writeup-template.md) as a base: timeline, affected systems, evidence, root cause, containment steps and recommendations. One to two pages.

## Certifications worth considering

See the [certifications guide](../guides/certifications.md). For this track the usual candidates are CompTIA Security+, CompTIA CySA+ and the Blue Team Level 1 from Security Blue Team. Read job adverts before you buy.

## Where it leads

[Security Operations Center analyst](../careers/security-operations-center.md), [Incident Responder](../careers/incident-responder.md), [Threat Hunter](../careers/threat-hunter.md), [Detection Engineer](../careers/detection-engineer.md), [Vulnerability Management Analyst](../careers/vulnerability-management-analyst.md), [Digital Forensic Analyst](../careers/digital-forensic-analyst.md), [Malware Analyst](../careers/malware-analyst.md). If the investigation work appeals most, read the [digital forensics track](digital-forensics.md).

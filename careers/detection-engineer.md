# Detection Engineer

Last reviewed: 2026-10-03

[All roles](README.md)

## Summary

Builds and maintains the rules that tell a security team an attack is happening. Writes detection logic for a SIEM, an endpoint product or a network sensor, tests it against simulated attacks, and tunes it so analysts see real threats and fewer false alarms. A detection engineer decides what the SOC sees, so the work shapes every analyst's day.

Most detection engineers spent a year or two as SOC analysts first. The job title varies. You may also see "security detection analyst" or "SOC engineer".

## Hard Skills

- Writing queries in at least one SIEM language, such as Splunk SPL, Elastic KQL or EQL, or Microsoft Sentinel KQL
- Detection rule formats: Sigma for log-based rules, YARA for files, Suricata or Snort for network traffic
- How attacks look in Windows, Linux and cloud logs
- The MITRE ATT&CK framework, used to describe what a rule covers and to find gaps
- Testing detections with attack simulation, for example Atomic Red Team
- Version control with Git, because rules are code and need review and history
- Basic Python or another scripting language for parsing, enrichment and testing
- Measuring detection quality: false positive rate, coverage and time to detect

## Soft Skills

- Patience with noisy data and with analysts' complaints about it
- Clear writing, so that every rule says what it detects and what to do when it fires
- Working with analysts, incident responders and system owners to understand what normal looks like

## Education

No specific degree. Employers look at your rules, your write-ups and your SOC experience. A computer science or IT degree helps but is not required.

## How to get there

1. Work as a SOC analyst and keep a list of alerts that wasted your time.
2. For each one, work out why the rule was noisy and how you would fix it.
3. Build the detection lab in the [blue team track](../tracks/blue-team.md) and write rules of your own.
4. Publish them, with the test you used to prove each rule fires, in your portfolio.

## Certifications

No single certification dominates. Vendor certifications for the SIEM your employer uses carry the most weight, such as Splunk's certifications or Microsoft's SC-200. Check what employers list. See the [certifications guide](../guides/certifications.md).

## Interview Questions

- Write a detection for repeated failed logins followed by a success from the same address. What fields do you need?
- A rule fires 400 times a day and 399 are false positives. What do you do?
- How would you test that a new rule actually works?
- What is the difference between a signature-based detection and a behaviour-based one?
- How do you decide whether a gap in ATT&CK coverage matters for a particular organisation?

## Training Resources

- [Sigma rules repository](https://github.com/SigmaHQ/sigma)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- [Wazuh](https://wazuh.com/) and [Security Onion](https://securityonionsolutions.com/) for a lab SIEM

Related roles: [Security Operations Center (SOC) Analyst](security-operations-center.md), [Threat Hunter](threat-hunter.md), [Automation Engineer](automation-engineer.md).

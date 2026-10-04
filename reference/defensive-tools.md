# Defensive tools

Last reviewed: 2026-10-03

Free and open source tools used by blue teams, grouped by what they do. This page was written by AquilaCyber. For a far longer list, see [BlueTeam-Tools](https://github.com/A-poc/BlueTeam-Tools) by A-poc.

Install and try one tool from each group in your lab. See the [security operations concepts](../guides/security-operations-concepts.md) guide for what each category is for.

## Network visibility

- [Wireshark](https://www.wireshark.org/): packet capture and analysis.
- [Zeek](https://zeek.org/): turns network traffic into structured logs.
- [Suricata](https://suricata.io/): intrusion detection and prevention.
- [Snort](https://www.snort.org/): intrusion detection and prevention.

## Hosts and endpoints

- [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon): detailed Windows activity logging.
- [osquery](https://osquery.io/): query your machines like a database.
- [Velociraptor](https://docs.velociraptor.app/): endpoint visibility and digital forensics at scale.

## Log collection and SIEM

- [Wazuh](https://wazuh.com/): host monitoring, log analysis and alerting.
- [Security Onion](https://securityonionsolutions.com/): a Linux distribution that bundles network and host monitoring tools.
- [Elastic Security](https://www.elastic.co/security): a search-based SIEM with a free tier.

## Analysis

- [CyberChef](https://gchq.github.io/CyberChef/): decode, decrypt and transform data in a browser.
- [VirusTotal](https://www.virustotal.com/): scan files, URLs and hashes against many engines. Do not upload anything confidential.

## Threat intelligence

- [MISP](https://www.misp-project.org/): an open source platform for sharing indicators of compromise.

## Vulnerability scanning

- [Greenbone OpenVAS](https://www.greenbone.net/en/): a vulnerability scanner.
- [Nmap](https://nmap.org/): host and service discovery, also useful for defenders who need to know what is on their own network.

## Forensics

- [Autopsy](https://www.autopsy.com/): disk image analysis.
- [Volatility](https://volatilityfoundation.org/): memory forensics.

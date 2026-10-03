# Security operations concepts

The tools a security team uses, what each one does and how they connect. Product names change. The categories stay the same.

## The tools

**Firewall.** Allows or blocks network traffic by rules, for example by address, port or application. A next-generation firewall also inspects the traffic content.

**IDS and IPS.** An intrusion detection system watches traffic or hosts and raises an alert when it sees something that matches a known bad pattern. An intrusion prevention system can also block the traffic. Suricata and Snort are open source examples.

**Antivirus and EDR.** Antivirus compares files to known malware. Endpoint detection and response goes further: it records what happens on a computer, such as processes started and connections made, so analysts can investigate and isolate the machine remotely. XDR extends that idea across email, network and cloud data. MDR is a managed service where an outside team watches your EDR for you.

**SIEM.** A security information and event management system collects logs from many sources, stores them, lets analysts search them and raises alerts when rules match. It is the main screen of a security operations centre. Wazuh, Elastic and Splunk are well-known examples.

**SOAR.** Security orchestration, automation and response tools run repeatable steps automatically, such as looking up an IP address, disabling an account or opening a ticket, when an alert fires.

**UEBA.** User and entity behaviour analytics learns what normal looks like for each user and device and flags unusual activity, such as a finance clerk logging in at 3 a.m. from another country.

**Vulnerability scanner.** Scans systems for known weaknesses such as missing patches. Nessus and OpenVAS are common. A scanner finds weaknesses. It does not prove they can be exploited.

**Threat intelligence platform.** Collects and shares indicators of compromise, such as malicious IP addresses and file hashes, and the context around them. MISP is an open source example.

**Case management.** Tracks each incident from alert to closure, with notes, evidence and who did what. TheHive is an open source example.

## How they connect

1. Sensors and endpoints produce logs and alerts: firewalls, IDS, EDR, servers, cloud services.
2. The SIEM collects them and applies detection rules.
3. An alert opens a case.
4. A SOAR playbook might enrich the alert automatically.
5. An analyst investigates, decides whether it is real and escalates or closes it.
6. Lessons from the case feed back into the detection rules.

## Where to learn more

- The [blue team track](../tracks/blue-team.md) has a plan and two projects.
- The [reference section](../reference/README.md) lists open source defensive tools.

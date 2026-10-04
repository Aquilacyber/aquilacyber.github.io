# Introduction to incident response

Last reviewed: 2026-10-03

An incident is an event that harms, or threatens, the confidentiality, integrity or availability of an organisation's systems or data. Incident response (IR) is the planned way of handling one: confirm it, limit the damage, remove the attacker, recover and learn from it.

## Why it matters

Prevention will sometimes fail. How an organisation responds then decides whether a bad day becomes a disaster. A prepared team can contain a ransomware attack to a few machines. An unprepared one finds out who has the backup passwords while the files are being encrypted.

There are legal duties too. Under the Nigeria Data Protection Act, a controller must notify the NDPC within 72 hours of becoming aware of a personal data breach that is likely to put people's rights at risk. Banks and payment service banks have reporting duties to the CBN. See the [Nigeria guide](../guides/nigeria.md).

## The lifecycle

Frameworks name the phases a little differently. NIST's incident handling guide, SP 800-61, groups them into four. SANS splits the middle into more steps. The ideas are the same.

| Phase | What happens |
|---|---|
| Preparation | Plans, contacts, tools, logging, training and exercises, all in place before anything happens |
| Detection and analysis | An alert or a report arrives. You decide whether it is real, how serious it is and what it affects |
| Containment, eradication and recovery | Stop the spread, remove the attacker and their access, restore systems and confirm they are clean |
| Post-incident activity | Write the report, find the root cause, fix what let it happen and update the plan |

## Key ideas

- **Severity levels.** A simple scale, such as low, medium, high and critical, that decides who is called and how fast.
- **Roles.** An incident lead who makes decisions, analysts who investigate, someone for communications, and legal and management contacts. Decide who does what before the incident.
- **Playbooks.** Step-by-step plans for common incidents, such as phishing, ransomware, a lost laptop and a compromised account.
- **Evidence.** Preserve logs and system state before you change things. See [digital forensics](digital-forensics.md).
- **Containment trade-offs.** Cutting off a machine stops the spread but alerts the attacker and can destroy evidence.
- **A timeline.** Write down what happened, when and who did what. It is the backbone of the final report.
- **Communication.** Use a channel the attacker cannot read. If email is compromised, an email thread is not a safe place to plan.
- **Exercises.** A tabletop exercise talks through a scenario around a table. It finds gaps in the plan cheaply.
- **Measures.** Mean time to detect and mean time to respond show whether the team is improving.

### The first hour of a ransomware incident

This shows how the pieces fit. Follow your own plan, which may differ.

1. Confirm it is real and declare an incident. Wake the incident lead.
2. Disconnect affected machines from the network. Do not power them off unless the plan says so, because memory holds evidence.
3. Protect backups by disconnecting them so the attacker cannot reach them.
4. Preserve logs and note the time of each action.
5. Find out how far it has spread.
6. Tell management and legal. Decisions about contacting the attacker or paying are theirs, not the analyst's.
7. Start working out how the attacker got in.

## What people in this field do

- A SOC analyst starts most incidents by triaging an alert and escalating.
- An incident responder leads the investigation and the recovery.
- A forensic analyst examines devices and logs for evidence.
- A threat hunter checks whether the attacker is anywhere else.
- Management, legal and communications staff handle decisions and notices.

## Common tools

| Tool | What it does |
|---|---|
| SIEM and EDR | Show alerts and what happened on machines |
| [TheHive](https://github.com/TheHive-Project/TheHive) | Open source case management |
| [Velociraptor](https://docs.velociraptor.app/) | Collects evidence from many machines |
| Playbooks and checklists | Keep the team calm and consistent |

The [incident response reference page](../reference/incident-response.md) has a long list of tools, playbooks and books.

## Try it

1. Write a one-page playbook for a phishing email report. Include who is told, what is checked, how you decide it is serious and when you close it.
2. Run a tabletop exercise with two friends. One reads a scenario aloud, such as a staff member's email sending spam, and the others say what they would do at each step. Write down every gap.
3. Work through an investigation case on [Blue Team Labs Online](https://blueteamlabs.online/), [LetsDefend](https://letsdefend.io/) or [CyberDefenders](https://cyberdefenders.org/), then write the incident report using the [write-up template](../templates/writeup-template.md).
4. Build a timeline from a set of sample logs and mark the events that matter.

## Mistakes beginners make

- Powering off a machine and losing the evidence in its memory
- Changing a system before recording its state
- Skipping the written timeline
- Letting a team find out its roles during the incident
- Closing the incident without finding the root cause

## Where to go next

- The [blue team track](../tracks/blue-team.md)
- Roles: [Incident Responder](../careers/incident-responder.md), [Security Operations Center (SOC) Analyst](../careers/security-operations-center.md), [Threat Hunter](../careers/threat-hunter.md)
- Learn more: NIST SP 800-61 at [csrc.nist.gov](https://csrc.nist.gov/), [MITRE ATT&CK](https://attack.mitre.org/)
- Related: [digital forensics](digital-forensics.md) and [threat intelligence](threat-intelligence.md)

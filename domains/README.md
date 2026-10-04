# Security domains

Last reviewed: 2026-10-03

Security is split into areas that overlap but have their own tools, vocabulary and jobs. This section gives a short introduction to eleven of them. Each page tells you what the area is, why it matters, the key ideas, what the work looks like, which tools to know, what to try in your own lab and where to go next.

Each page takes about fifteen minutes to read. Read all eleven after phase 1 and before you choose a track in [phase 3](../roadmap/03-pick-a-track.md). You will make a better choice once you know what each area actually involves.

## Domain or track

A **domain** is an area of security, such as cryptography or incident response. A **track** is a learning plan with projects, such as the [blue team track](../tracks/blue-team.md). A track draws on several domains, and some domains, such as cryptography, belong to every track.

## The eleven domains

| Domain | In one line | Related track | Large reference list |
|---|---|---|---|
| [Network security](network-security.md) | Controlling and watching the traffic between systems | [Blue team](../tracks/blue-team.md) | [Network security basics guide](../guides/network-security-basics.md) |
| [Endpoint security](endpoint-security.md) | Protecting laptops, servers and phones | [Blue team](../tracks/blue-team.md) | [Endpoint security](../reference/endpoint-security.md) |
| [Cloud security](cloud-security.md) | Securing systems in AWS, Azure and Google Cloud | [Cloud security](../tracks/cloud-security.md) | [Cloud security](../reference/cloud-security.md) |
| [IoT security](iot-security.md) | Securing small connected devices and the services behind them | [Red team](../tracks/red-team.md) | [IoT security](../reference/iot-security.md) |
| [Cryptography](cryptography.md) | Protecting data with mathematics | Used in every track | [Cryptography](../reference/cryptography.md) |
| [Threat modeling](threat-modeling.md) | Finding design weaknesses before a system is built | [Application security](../tracks/application-security.md) | [Threat modeling](../reference/threat-modeling.md) |
| [Incident response](incident-response.md) | Handling an attack while it is happening | [Blue team](../tracks/blue-team.md) | [Incident response](../reference/incident-response.md) |
| [Digital forensics](digital-forensics.md) | Finding out what happened and proving it | [Digital forensics](../tracks/digital-forensics.md) | [Free training archive](../reference/free-training/README.md) |
| [Threat intelligence](threat-intelligence.md) | Knowing who attacks you and how | [Blue team](../tracks/blue-team.md) | [Threat intelligence](../reference/threat-intelligence.md) |
| [Offensive security](offensive-security.md) | Testing systems by attacking them, with permission | [Red team](../tracks/red-team.md) | [Offensive security](../reference/offensive-security.md) |
| [GRC](grc.md) | Risk, rules, audit and privacy | [GRC](../tracks/grc.md) | [Frameworks and standards](../guides/frameworks-and-standards.md) |

## How they fit together

A useful way to remember the shape of the field:

- **Design and prevent.** Threat modeling finds weaknesses on paper. Network, endpoint, cloud and IoT security make attacks harder in practice, with cryptography underneath.
- **Detect and respond.** Threat intelligence, incident response and digital forensics find attacks, stop them and explain them.
- **Test.** Offensive security checks whether the prevention and detection work.
- **Govern.** GRC decides what must be protected, sets the rules and proves to others that it was done.

Every real incident touches most of these. A phishing email lands on an endpoint, crosses the network, steals a cloud login, triggers an alert, goes to incident response, ends in a forensic report and a change to policy.

## Before you start any lab

Read the [ethics and law guide](../guides/ethics-and-law.md). Every exercise in this section is meant for your own lab or for platforms that give you targets.

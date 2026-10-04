# Introduction to threat intelligence

Last reviewed: 2026-10-03

Threat intelligence is information about who attacks, why, how and with what, turned into something a defender can act on. A list of bad IP addresses is data. A short report that says which group is targeting Nigerian banks this month, how they get in and what to check for is intelligence.

## Why it matters

Defenders cannot watch for everything. Intelligence tells them what to watch for first. It helps a SOC write better detections, helps leaders decide where to spend money and helps an incident response team understand an attacker faster.

## Key ideas

### Four types

| Type | For whom | Example |
|---|---|---|
| Strategic | Executives and boards | Which groups target our sector over the next year and why |
| Operational | Security leads and responders | A campaign is active against banks, using phishing that carries a specific loader |
| Tactical | Defenders and detection engineers | The techniques the attackers use, so we can write detections for them |
| Technical | Tools and analysts | Hashes, addresses and domains linked to the activity |

### The intelligence cycle

1. **Direction.** Decide what questions the people who will use the intelligence need answered.
2. **Collection.** Gather information from the sources you have.
3. **Processing.** Clean it up, remove duplicates and put it in a usable form.
4. **Analysis.** Work out what it means and how sure you are.
5. **Dissemination.** Give it to the right people in a form they can use.
6. **Feedback.** Ask whether it helped, and adjust.

### Indicators and behaviour

An **indicator of compromise** (IOC) is a clue such as a file hash, an IP address or a domain. IOCs are easy to collect and easy for attackers to change. **Tactics, techniques and procedures** (TTPs) describe how attackers behave, and they are much harder to change. The Pyramid of Pain, written by David Bianco, ranks indicators by how much trouble it causes an attacker when you detect them. Hashes are at the bottom and are trivial to change. TTPs are at the top and are painful to change. Aim detections at the top.

### Shared vocabulary

- **[MITRE ATT&CK](https://attack.mitre.org/)** is a catalogue of attacker techniques. Analysts use it to describe behaviour and to find gaps in detection.
- **STIX and TAXII** are standards for describing and sharing threat information. See the [STIX documentation](https://github.com/oasis-open/cti-documentation).
- **The Traffic Light Protocol** (TLP) marks how far information may be shared. The colours in version 2 are TLP:CLEAR, TLP:GREEN, TLP:AMBER and TLP:RED, with an extra AMBER+STRICT. See [first.org/tlp](https://www.first.org/tlp/).

### Judging information

Ask where it came from, how reliable the source has been and whether anyone else confirms it. State your confidence and why. Attribution, naming who was behind an attack, is hard and often unnecessary. Knowing the technique is usually enough to defend.

## What people in this field do

- A threat analyst follows groups and campaigns, reads reports, writes briefings and feeds detections.
- A cyber intelligence specialist produces products for a particular audience, such as a bank's leadership.
- A threat hunter uses intelligence to decide where to search.
- A detection engineer turns tactics into detection rules.

## Sources

- Vendor and researcher reports
- Government advisories, such as those from [CISA](https://www.cisa.gov/news-events/cybersecurity-advisories) and Nigeria's ngCERT
- Information sharing groups for a sector
- Open source information, such as news, forums and code repositories
- Your own incidents, which are often the best source

## Common tools

| Tool | What it does |
|---|---|
| [MISP](https://www.misp-project.org/) | Open source platform for storing and sharing indicators |
| [OpenCTI](https://github.com/OpenCTI-Platform/opencti) | Open source platform for organising threat knowledge |
| [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) | Colours a matrix of techniques so you can see coverage and gaps |
| [VirusTotal](https://www.virustotal.com/) | Checks files, URLs and hashes. Do not upload anything confidential |
| [CyberChef](https://gchq.github.io/CyberChef/) | Decodes and transforms data |

The [threat intelligence reference page](../reference/threat-intelligence.md) lists many feeds and tools.

## Try it

1. Read the [Pyramid of Pain](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html) and explain it with one example of your own.
2. Pick a public threat report. List the techniques it describes and map them to ATT&CK.
3. Write a one-page briefing about that report for a non-technical manager. Say what it means for the organisation and what to do first.
4. Write a short threat profile of a sector you care about, such as Nigerian fintech. Say who targets it, how they get in and what a defender should watch for. Use only public sources and name them.
5. Run MISP in your lab and import a public feed. Say which entries are useful and which are noise.

## Mistakes beginners make

- Collecting long indicator lists nobody uses
- Treating old indicators as current
- Claiming attribution with little evidence
- Writing for other analysts when the reader is a manager
- Producing intelligence with no one who needs it

## Where to go next

- The [blue team track](../tracks/blue-team.md)
- Roles: [Cyber Threat Analyst](../careers/cyber-threat-analyst.md), [Cyber Intelligence Specialist](../careers/cyber-intelligence-specialist.md), [Threat Hunter](../careers/threat-hunter.md), [Detection Engineer](../careers/detection-engineer.md)
- Related: [incident response](incident-response.md) and [endpoint security](endpoint-security.md)

# Glossary

Last reviewed: 2026-10-03

Short definitions of terms you will meet in the roadmap.

**Access control.** Rules that decide who can use which resource.

**Active Directory.** Microsoft's directory service. It keeps one central record of the users, groups and computers in an organisation and handles logons. See [Windows and Active Directory basics](windows-and-active-directory.md).

**APT.** Advanced persistent threat. A well-resourced attacker, often linked to a state, who stays inside a network for a long time.

**Attack surface.** All the places where an attacker could try to get in.

**Authentication.** Proving who you are, for example with a password and a code from your phone.

**Authorisation.** Deciding what an authenticated person is allowed to do.

**Blue team.** The people who defend systems and respond to attacks.

**Botnet.** A group of infected computers controlled by an attacker.

**Brute force.** Trying many passwords or keys until one works.

**Bug bounty.** A programme where an organisation pays people who report valid security flaws within a set scope.

**Chain of custody.** A written record of who held a piece of evidence, when and what they did with it. It lets others trust that the evidence was not changed.

**CIA triad.** Confidentiality, integrity and availability: the three goals of information security.

**CSPM.** Cloud security posture management. Tools that check cloud accounts for risky settings such as public storage.

**CTF.** Capture the flag. A security puzzle or competition where you find hidden text strings called flags.

**CVE.** Common Vulnerabilities and Exposures. A public identifier for a specific known vulnerability, such as CVE-2021-44228.

**CVSS.** A scoring system, from 0 to 10, for the severity of a vulnerability.

**DAST.** Dynamic application security testing. Testing a running application from the outside, as an attacker would.

**Defence in depth.** Using several layers of protection so one failure does not expose everything.

**DMZ.** A network zone for systems that must be reachable from the internet, kept apart from the internal network.

**DNS.** The Domain Name System. It turns names such as example.com into IP addresses.

**Domain controller.** A Windows server that holds a copy of the Active Directory directory and checks logons for the domain.

**EDR.** Endpoint detection and response. Software that records and analyses activity on computers so threats can be found and contained.

**Encryption.** Scrambling data so only someone with the key can read it. It can be reversed with the key.

**Entra ID.** Microsoft's cloud identity service, called Azure Active Directory until 2023. It is not the same product as on-premises Active Directory.

**EPSS.** Exploit Prediction Scoring System. A score from FIRST that estimates how likely a vulnerability is to be exploited in the next 30 days.

**Exploit.** Code or a technique that takes advantage of a vulnerability.

**Firewall.** A control that allows or blocks network traffic by rules.

**Forensic image.** An exact bit-for-bit copy of a disk or memory, made so the original is not touched during an investigation.

**GRC.** Governance, risk and compliance.

**Group Policy.** A feature of Active Directory that pushes settings, such as password rules, to many computers and users at once.

**Hash.** A fixed-length fingerprint of data produced by a one-way function. You cannot turn a hash back into the original. Used for passwords and file integrity.

**IaC.** Infrastructure as code. Defining servers, networks and cloud resources in files, such as Terraform, instead of clicking in a console.

**IAM.** Identity and access management. The processes and tools that decide who can access which systems.

**IDOR.** Insecure direct object reference. A flaw where changing an identifier in a request, such as a user number, shows another person's data.

**IDS and IPS.** Intrusion detection system and intrusion prevention system.

**Incident response.** The process of detecting, containing and recovering from a security incident.

**IOC.** Indicator of compromise. A clue that a system has been attacked, such as a known bad IP address or file hash.

**Kerberos.** The default authentication protocol in Active Directory. You prove who you are once and receive a ticket that expires.

**KEV.** The CISA Known Exploited Vulnerabilities catalogue, a list of vulnerabilities that attackers are known to be using.

**Least privilege.** Giving a user or program only the access it needs and nothing more.

**Malware.** Software built to cause harm, including viruses, worms, ransomware and trojans.

**MFA.** Multi-factor authentication. Requiring two or more kinds of proof, such as a password and a one-time code.

**MITRE ATT&CK.** A public catalogue of attacker tactics and techniques.

**NAT.** Network address translation. Lets many private addresses share one public address. It is not a security control by itself.

**NDPA.** The Nigeria Data Protection Act 2023.

**NDPC.** The Nigeria Data Protection Commission.

**OAuth.** A standard for letting one application act for a user on another service without sharing the user's password.

**OSINT.** Open source intelligence. Information gathered from public sources.

**PAM.** Privileged access management. Controls and records the use of administrator-level accounts. Also short for pluggable authentication modules on Linux, so check the context.

**Patch.** A software update that fixes a vulnerability or bug.

**Penetration test.** An authorised, simulated attack on a system to find weaknesses.

**Phishing.** A message that tricks someone into giving up credentials or running malware.

**Privilege escalation.** Gaining more access than you were given.

**Ransomware.** Malware that encrypts files and demands payment to restore them.

**RBAC.** Role-based access control. Access is given to roles, such as accountant, and people are placed in roles.

**Red team.** The people who simulate attackers to test an organisation's defences.

**Risk.** The likelihood that a threat uses a vulnerability, multiplied by the harm it would cause.

**SAML.** Security Assertion Markup Language. A standard that lets a user sign in once with an identity provider and reach other applications.

**SAST.** Static application security testing. Analysing source code for flaws without running it.

**SCA.** Software composition analysis. Checking the third-party libraries an application uses for known vulnerabilities.

**Segmentation.** Dividing a network into zones so a problem in one does not spread to the others.

**SIEM.** Security information and event management. A system that collects logs and raises alerts.

**Sigma rule.** A vendor-neutral format for writing log-based detection rules that can be converted for different SIEM tools.

**SOAR.** Security orchestration, automation and response.

**SOC.** Security operations centre. The team and room that monitor and respond to security alerts.

**Social engineering.** Manipulating people, not computers, to get access or information.

**SQL injection.** An attack that inserts database commands into an input field to read or change data.

**SSO.** Single sign-on. Signing in once to reach several applications.

**STRIDE.** A threat modelling method that asks about six kinds of threat: spoofing, tampering, repudiation, information disclosure, denial of service and elevation of privilege.

**SUID.** A Linux permission that makes a program run as its owner, often root. A weak SUID program is a common route to root.

**Threat.** Anything that could harm an asset. A vulnerability is a weakness. A risk combines the two with impact.

**TLS.** Transport Layer Security. The protocol behind the padlock in your browser.

**VPN.** Virtual private network. An encrypted tunnel between your device and another network.

**Vulnerability.** A weakness that could be used to cause harm.

**XSS.** Cross-site scripting. An attack that makes a website run an attacker's script in a visitor's browser.

**YARA rule.** A rule that describes patterns in files or memory, used to identify malware.

**Zero trust.** A security approach that does not trust a request because it comes from inside the network. Each request is checked for identity, device and permission.

**Zero-day.** A vulnerability that the vendor does not yet know about or has not fixed.

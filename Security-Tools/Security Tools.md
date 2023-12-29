
# Security Tools
[Back to the Top](https://github.com/mikeroyal/Open-Source-Security-Guide#table-of-contents)

[Acra](https://cossacklabs.com/acra) is a single database security suite with 9 strong security controls: application level encryption, searchable encryption, data masking, data tokenization, secure authentication, data leakage prevention, database request firewall, cryptographically signed audit logging, security events automation. It is designed to cover the most important data security requirements with SQL and NoSQL databases and distributed apps in a fast, convenient, and reliable way.

[Netdata](https://github.com/netdata/netdata) is high-fidelity infrastructure monitoring and troubleshooting, real-time monitoring Agent collects thousands of metrics from systems, hardware, containers, and applications with zero configuration. It runs permanently on all your physical/virtual servers, containers, cloud deployments, and edge/IoT devices, and is perfectly safe to install on your systems mid-incident without any preparation.

[Themis](https://cossacklabs.com/themis) is a free open-source high-level cryptographic library for mobile and backend platforms. Recommended by OWASP for application security, it allows protecting sensitive data (PII, locations, messages, etc.). While giving easy-to-use and hard-to-misuse API, Themis works to provide secure data storage, message exchange, socket connections, and authentication in apps across 15 platforms and languages.

[OWASP](https://www.owasp.org/index.php/Main_Page) is an online community, produces freely-available articles, methodologies, documentation, tools, and technologies in the field of web application security.

[OpenSCAP](https://www.open-scap.org/) is U.S. standard maintained by [National Institute of Standards and Technology (NIST)](https://www.nist.gov/). It provides multiple tools to assist administrators and auditors with assessment, measurement, and enforcement of security baselines. OpenSCAP maintains great flexibility and interoperability by reducing the costs of performing security audits. Whether you want to evaluate DISA STIGs, NIST‘s USGCB, or Red Hat’s Security Response Team’s content, all are supported by OpenSCAP.

[Open Vulnerability and Assessment Language](https://oval.mitre.org/) is a community effort to standardize how to assess and report upon the machine state of computer systems. OVAL includes a language to encode system details, and community repositories of content. Tools and services that use OVAL provide enterprises with accurate, consistent, and actionable information to improve their security.

[Trivy](https://aquasecurity.github.io/trivy/) is a comprehensive security scanner for vulnerabilities in container images, file systems, and Git repositories, as well as for configuration issues and hard-coded secrets.

[Lynis](https://cisofy.com/lynis/) is a security auditing tool for Linux, macOS, and UNIX-based systems. Assists with compliance testing (HIPAA/ISO27001/PCI DSS) and system hardening. Agentless, and installation optional. 

[RustScan](https://github.com/RustScan/RustScan) is a Modern Port Scanner.

[gosec](https://github.com/securego/gosec) is a Golang Security Checker that inspects source code for security problems by scanning the Go AST.

[Age](https://age-encryption.org/) is a simple, modern and secure encryption tool (and Go library) with small explicit keys, no config options, and UNIX-style composability. 

[SOPS](https://github.com/mozilla/sops) is an editor of encrypted files that supports YAML, JSON, ENV, INI and BINARY formats and encrypts with AWS KMS, GCP KMS, Azure Key Vault, age, and PGP.

[Tailnet lock](https://tailscale.com/kb/1226/tailnet-lock/) is a tool that allows you to verify that no node is added to your tailnet without being signed by trusted nodes in your tailnet. When tailnet lock is enabled, even if Tailscale infrastructure is malicious or hacked, attackers can’t send or receive traffic on your tailnet.

[Sandstorm](https://sandstorm.io/) is a self-hostable web productivity suite. It's implemented as a security-hardened web app package manager. 

[mkcert](https://mkcert.dev/) is a simple zero-config tool to make locally trusted development certificates with any names you'd like. 

[Tailnet](https://tailscale.com/kb/1136/tailnet/) is your private network. When you log in for the first time to Tailscale on your phone, laptop, desktop, or cloud VM, a tailnet is created. For personal users, you are a tailnet of many devices and one person. Each device gets a private Tailscale IP address in the [CGNAT](https://tailscale.com/kb/1015/100.x-addresses/) range and every device can talk directly to every other device, wherever they are on the internet.

[Tailscale SSH](https://tailscale.com/kb/1193/tailscale-ssh/) is a service that allows Tailscale to manage the authentication and authorization of SSH connections on your tailnet.

[Tailscale Funnel](https://tailscale.com/kb/1223/tailscale-funnel/) is a feature that allows you to route traffic from the wider internet to one or more of your Tailscale nodes. You can think of this as publicly sharing a node for anyone to access, even if they don’t have Tailscale themselves. 

[Universal Radio Hacker (URH)](https://github.com/jopohl/urh) is a complete suite for wireless protocol investigation with native support for many common Software Defined Radios. URH allows easy demodulation of signals combined with an automatic detection of modulation parameters making it a breeze to identify the bits and bytes that fly over the air. 

[Cloudflare Tunnel client](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide) is a tunneling daemon that proxies traffic from the Cloudflare network to your origins. This daemon sits between Cloudflare network and your origin (e.g. a webserver). Cloudflare attracts client requests and sends them to you via this daemon, without requiring you to poke holes on your firewall --- your origin can remain as closed as possible. 

[Cloudflare WARP client](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/) is a tool that allows you to protect corporate devices by securely and privately sending traffic from those devices to Cloudflare’s edge, where Cloudflare Gateway can apply advanced web filtering. It also makes it possible to apply advanced Zero Trust policies that check for a device’s health before it connects to corporate applications.

[Prowler](https://github.com/prowler-cloud/prowler) is an Open Source security tool to perform AWS security best practices assessments, audits, incident response, continuous monitoring, hardening and forensics readiness. It contains more than 240 controls covering CIS, PCI-DSS, ISO27001, GDPR, HIPAA, FFIEC, SOC2, AWS FTR, ENS and custom security frameworks. 

[eNgine](https://github.com/yogeshojha/rengine) is an automated reconnaissance framework for web applications with a focus on highly configurable streamlined recon process via Engines, recon data correlation and organization, continuous monitoring, backed by a database, and simple yet intuitive UI. 

[Osmedeus](https://github.com/j3ssie/osmedeus) is a Workflow Engine for Offensive Security. It was designed to build a foundation with the capability and flexibility that allows you to build your own reconnaissance system and run it on a large number of targets.

[OWASP Nettacker](https://github.com/OWASP/Nettacker) is a project created to automate information gathering, vulnerability scanning and eventually generating a report for networks, including services, bugs, vulnerabilities, misconfigurations, and other information. This software will utilize TCP SYN, ACK, ICMP, and many other protocols in order to detect and bypass Firewall/IDS/IPS devices. 

[Terrascan](https://runterrascan.io/) is a static code analyzer for Infrastructure as Code to mitigate risk before provisioning cloud native infrastructure. 

[Sliver](https://github.com/BishopFox/sliver) is an open source cross-platform adversary emulation/red team framework, it can be used by organizations of all sizes to perform security testing. Sliver's implants support C2 over Mutual TLS (mTLS), WireGuard, HTTP(S), and DNS and are dynamically compiled with per-binary asymmetric encryption keys.

[Payloads All The Things](https://github.com/swisskyrepo/PayloadsAllTheThings) is a list of useful payloads and bypass for Web Application Security and Pentest/CTF. 

[TheHive](https://thehive-project.org/) is a scalable 3-in-1 open source and free Security Incident Response Platform designed to make life easier for SOCs, CSIRTs, CERTs and any information security practitioner dealing with security incidents that need to be investigated and acted upon swiftly. It is the perfect companion to [MISP](http://www.misp-project.org/). 

[MITRE ATT&CK®](https://attack.mitre.org/) is a global knowledge base of adversary tactics and techniques based on real-world security observations. It is used as a foundation for the development of specific threat models and methodologies in the private sector, in government, and in the cybersecurity product and service community.

[CALDERA™](https://caldera.mitre.org/) is a cyber security platform designed to easily automate adversary emulation, assist manual red-teams, and automate incident response.

[Pyrsia](https://pyrsia.io/) is a Decentralized Package Network that aims to secure the software supply chain of open-source dependencies by creating a system that secures open-source builds and distribution.

[GitGuardian shield (ggshield)](https://github.com/GitGuardian/ggshield) is a CLI application that runs in your local environment or in a CI environment to help you detect more than 350+ types of secrets, as well as other potential security vulnerabilities or policy breaks.

[ggshield-action](https://github.com/GitGuardian/ggshield-action) is a GitGuardian Shield GitHub Action to find exposed credentials in your commits.

[Atomic Red Team™](https://github.com/redcanaryco/atomic-red-team) is a library of tests mapped to the [MITRE ATT&CK®](https://attack.mitre.org/) framework. Security teams can use Atomic Red Team to quickly, portably, and reproducibly test their environments.

[OpenCTI](https://www.opencti.io/) is an open source platform allowing organizations to manage their cyber threat intelligence knowledge and observables. It has been created in order to structure, store, organize and visualize technical and non-technical information about cyber threats.

[OWASP Amass](https://owasp.org/www-project-amass/) is a tool that performs network mapping of attack surfaces and external asset discovery using open source information gathering and active reconnaissance techniques.

[CrowdSec](https://www.crowdsec.net/) is an open-source and collaborative security stack leveraging the crowd power to generate a global CTI database to protect the user network. It will analyze behaviors, respond to attacks & share signals across the community. 

[Crowdsec Firewall Bouncer](https://github.com/crowdsecurity/cs-firewall-bouncer) is a tool that will fetch new and old decisions from a CrowdSec API to add them in a blocklist used by supported firewalls.

**Supported firewalls:**

  * iptables (IPv4 heavy_check_mark / IPv6 heavy_check_mark )
  * nftables (IPv4 heavy_check_mark / IPv6 heavy_check_mark )
  * ipset only (IPv4 heavy_check_mark / IPv6 heavy_check_mark )
  * pf (IPV4 heavy_check_mark / IPV6 heavy_check_mark )


[Pulse](https://kean.blog/pulse/home) is a powerful logging system for Apple Platforms builtin in SwiftUI. It allows you to record and inspect logs and ```URLSession``` network requests right from your iOS app. Shared logs and view them in [Pulse Pro](https://kean.blog/pulse/pro) or use remote logging to see them in real-time. Logs are stored locally and never leave your devices.

[tshark.dev](https://tshark.dev/) is your complete guide to working with packet captures on the command-line.

[Nebula](https://github.com/slackhq/nebula) is a scalable overlay networking tool with a focus on performance, simplicity and security. It lets you seamlessly connect computers anywhere in the world. Nebula is portable, and runs on Linux, OSX, Windows, iOS, and Android. It can be used to connect a small number of computers, but is also able to connect tens of thousands of computers.

[Parca](https://parca.dev/) is a tool for continuous profiling for analysis of CPU and memory usage, down to the line number and throughout time. Saving infrastructure cost, improving performance, and increasing reliability.

[DeepFlow](https://github.com/deepflowys/deepflow) is a highly automated observability platform for cloud-native developers. Using new technologies such as eBPF, WASM, and OpenTelemetry, DeepFlow innovatively implements core mechanisms such as AutoTracing, AutoMetrics, AutoTagging, and SmartEncoding, which greatly avoids code instrumentation and significantly reduces the resource overhead of back-end data warehouses. 

[LGTM](https://github.com/marketplace/lgtm) is a tool that finds and prevents zero-days and other critical bugs, with customizable alerts and automated code review.

[Semgrep](https://github.com/marketplace/semgrep-dev) is a code scanning at ludicrous speed. Find bugs and reachable dependency vulnerabilities. Enforce standards on every commit.

[Socket Security](https://github.com/marketplace/socket-security) is a tool that protects your app from malicious open source dependencies.

[ir-rescue](https://github.com/diogo-fernan/ir-rescue) is a Windows Batch script and a Unix Bash script to comprehensively collect host forensic data during incident response.

[Live Response Collection](https://www.brimorlabs.com/tools/) is an automated tool that collects volatile data from Windows, MacOS, and \*nix based operating systems.

[Margarita Shotgun](https://github.com/ThreatResponse/margaritashotgun) is a  Command line utility (that works with or without Amazon EC2 instances) to parallelize remote memory acquisition.

[Catalyst](https://github.com/SecurityBrewery/catalyst) is a free SOAR system that helps to automate alert handling and incident response processes.

[CyberCPR](https://www.cybercpr.com) is a community and commercial incident management tool with Need-to-Know built in to support GDPR compliance while handling sensitive incidents.

[Snyk](https://github.com/marketplace/snyk) is a tool that find, fix (and prevent!) known vulnerabilities in your code.

[GitProtect.io](https://github.com/marketplace/gitprotect-io) is a free Backup for GitHub that does automatic, daily repo and metadata backup - no maintenance needed: fast restore, DR, AWS, and S3 cloud storage support.

[Cloudback Backup](https://github.com/marketplace/cloudback) is a tool that automatically backups of your repos, metadata and even LFS. Backup to AWS, Azure, OneDrive, GCP, and more. Also, does instant restores.

[Mend Bolt](https://github.com/marketplace/whitesource-bolt) isa that detects open source vulnerabilities in real time with suggested fixes for quick remediation.

[Rewind Backups for GitHub (Formerly BackHub)](https://github.com/marketplace/backhub) is a tool that does daily, automatic backups of your repos & metadata. Restore your backups with metadata in seconds + Sync to your S3 or Azure.

[Renovate](https://github.com/marketplace/renovate) is a tool that keeps dependencies up-to-date with automated Pull Requests.

[GuardRails](https://github.com/marketplace/guardrails) provides continuous security feedback for modern development teams.

[Dnsmasq](https://dnsmasq.org/) is a tool that provides network infrastructure for small networks: DNS, DHCP, router advertisement and network boot. It is designed to be lightweight and have a small footprint, suitable for resource constrained routers and firewalls. It has also been widely used for tethering on smartphones and portable hotspots, and to support virtual networking in virtualisation frameworks. Supported platforms include Linux (with glibc and uclibc), Android, BSD, and MacOS. 

[Matano](https://matano.dev/) is an Open source cloud-native security lake platform (SIEM alternative) for threat hunting, detection & response, and cybersecurity analytics at petabyte scale on AWS.

[Hetty](https://github.com/dstotijn/hetty) is an HTTP toolkit for security research. It aims to become an open source alternative to commercial software like Burp Suite Pro, with powerful features tailored to the needs of the infosec and bug bounty community.

[Dissect](https://github.com/fox-it/dissect) is a digital forensics & incident response framework and toolset that allows you to quickly access and analyse forensic artefacts from various disk and file formats, developed by Fox-IT (part of NCC Group).

[Acquire](https://github.com/fox-it/acquire) is a tool to quickly gather forensic artifacts from disk images or a live system into a lightweight container. 
 
[Faraday](https://www.faradaysec.com/) is an Open Source Vulnerability Management Platform. It aggregates and normalizes the data you load, allowing exploring it into different visualizations that are useful to managers and analysts alike.
 
[Security Onion](https://github.com/Security-Onion-Solutions/securityonion) is a free and open platform for threat hunting, enterprise security monitoring, and log management. It includes our own interfaces for alerting, dashboards, hunting, PCAP, and case management. 

[OpenCTI](https://www.opencti.io/) is an open source platform allowing organizations to manage their cyber threat intelligence knowledge and observables. It has been created in order to structure, store, organize and visualize technical and non-technical information about cyber threats.

[nDPI®](http://www.ntop.org/) is an open source LGPLv3 library for deep-packet inspection. Based on OpenDPI it includes ntop extensions. 

[Azure Sentinel](https://github.com/Azure/Azure-Sentinel) is a Cloud-native SIEM for intelligent security analytics for your entire enterprise. 

[NETworkManager](https://github.com/BornToBeRoot/NETworkManager) is a powerful tool for managing networks and troubleshoot network problems. It contains features like a WiFi analyzer, IP scanner, port scanner, ping monitor, traceroute, DNS lookup or a LLDP/CDP capture. 

[ORY Oathkeeper](https://github.com/ory/oathkeeper) is an Identity & Access Proxy (IAP) and Access Control Decision API that authorizes HTTP requests based on sets of Access Rules.

[Ory Kratos](https://github.com/ory/kratos) is a developer-friendly, security-hardened and battle-test Identity, User Management and Authentication system for the Cloud. The Kratos identity server (similiar to Auth0, Okta, Firebase) with Ory-hardened authentication, MFA, FIDO2, TOTP, WebAuthn, profile management, identity schemas, social sign in, registration, account recovery, passwordless. 

[Ory Hydra](https://github.com/ory/hydra) is a hardened, OpenID Certified OAuth 2.0 Server and OpenID Connect Provider optimized for low-latency, high throughput, and low resource consumption. Ory Hydra is not an identity provider (user sign up, user login, password reset flow), but connects to your existing identity provider through a [login and consent app](https://www.ory.sh/docs/hydra/oauth2#authenticating-users-and-requesting-consent).

[Ory Keto](https://github.com/ory/keto) is an Open Source (Go) implementation of [Zanzibar: Google's Consistent, Global Authorization System](https://research.google/pubs/pub48190/). It ships gRPC, REST APIs, newSQL, and an easy and granular permission language. Supports ACL, RBAC, and other access models. 

[Smap](https://github.com/s0md3v/Smap) is a port scanner built with shodan.io's free API. It takes same command line arguments as Nmap and produces the same output which makes it a drop-in replacament for Nmap.

[IVRE](https://ivre.rocks/) is a network recon framework. That let's you build your own, self-hosted and fully-controlled alternatives to Shodan, ZoomEye, Censys, and GreyNoise. IVRE can run your Passive DNS service, collect and analyse network intelligence from your sensors, and much more.

[MISP](https://www.misp-project.org/) is an open source software solution for collecting, storing, distributing and sharing cyber security indicators and threats about cyber security incidents analysis and malware analysis. MISP is designed by and for incident analysts, security and ICT professionals or malware reversers to support their day-to-day operations to share structured information efficiently.

[Rapid7 Nexpose](https://www.rapid7.com/products/nexpose/) is a vulnerability scanner which aims to support the entire vulnerability management lifecycle, including discovery, detection, verification, risk classification, impact analysis, reporting and mitigation. It integrates with Rapid7's Metasploit for vulnerability exploitation.

[Nikto](https://github.com/sullo/nikto) is an Open Source web server scanner which performs comprehensive tests against web servers for multiple items, including over 6400 potentially dangerous files/CGIs, checks for outdated versions of over 1200 servers, and version specific problems on over 270 servers.

[Scapy](https://scapy.net/) is a powerful interactive packet manipulation tool, packet generator, network scanner, network discovery tool, and packet sniffer.

[OSSEC HIDS(Host Intrusion Detection System)](https://www.ossec.net/) is an open source security tool that performs log analysis, integrity checking, rootkit detection, time-based alerting and active response. In addition to its IDS functionality, it is commonly used as a SEM/SIM solution.

[OpenMPTCProuter](https://www.openmptcprouter.com/) is a tool that uses [MultiPath TCP (MPTCP)](https://www.multipath-tcp.org/) to really aggregate multiple Internet connections and [OpenWrt](https://openwrt.org/).

[Cortex](https://thehive-project.org/) is a Powerful Observable Analysis and Active Response Engine. This solves a common problem frequently encountered by SOCs, CSIRTs and security researchers in the course of threat intelligence, digital forensics and incident response.
 
[Scrummage](https://github.com/matamorphosis/Scrummage) is an OSINT tool that centralises search functionality from a bounty of powerful, publicly-available, third-party, [OSINT](https://osintframework.com/) websites.

[Bettercap](https://www.bettercap.org/) is a powerful, easily extensible and portable framework written in Go which aims to offer to security researchers, red teamers and reverse engineers an easy to use, all-in-one solution with all the features they might possibly need for performing reconnaissance and attacking [WiFi](https://www.bettercap.org/modules/wifi/) networks, [Bluetooth Low Energy](https://www.bettercap.org/modules/ble/) devices, wireless [HID](https://www.bettercap.org/modules/hid/) devices and [Ethernet](https://www.bettercap.org/modules/ethernet) networks.

[Wifiphisher](https://wifiphisher.org/) is a rogue Access Point framework for conducting red team engagements or Wi-Fi security testing. Using Wifiphisher, penetration testers can easily achieve a man-in-the-middle position against wireless clients by performing targeted Wi-Fi association attacks.

[Attack Surface Analyzer](https://github.com/microsoft/AttackSurfaceAnalyzer) is a [Microsoft](https://github.com/microsoft/) developed open source security tool that analyzes the attack surface of a target system and reports on potential security vulnerabilities introduced during the installation of software or system misconfiguration.

[Intel Owl](https://intelowl.readthedocs.io/) is an Open Source Intelligence, or OSINT solution to get threat intelligence data about a specific file, an IP or a domain from a single API at scale. It integrates a number of analyzers available online and a lot of cutting-edge malware analysis tools.

[Deepfence ThreatMapper](https://deepfence.io/) is a runtime tool that hunts for vulnerabilities in your cloud native production platforms(Linux, K8s, AWS Fargate and more.), and ranks these vulnerabilities based on their risk-of-exploit. 

[Dockle](https://containers.goodwith.tech/) is a Container Image Linter for Security and helping build the Best-Practice Docker Image.

[SpiceDB](https://docs.authzed.com/) is an open source database system for managing security-critical application permissions inspired by Google's [Zanzibar](https://authzed.com/blog/what-is-zanzibar/) paper.

[Virtualization-based Security (VBS)](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs) is a hardware virtualization feature to create and isolate a secure region of memory from the normal operating system.

[Hypervisor-Enforced Code Integrity (HVCI)](https://docs.microsoft.com/en-us/windows-hardware/drivers/bringup/device-guard-and-credential-guard) is a mechanism whereby a hypervisor, such as Hyper-V, uses hardware virtualization to protect kernel-mode processes against the injection and execution of malicious or unverified code. Code integrity validation is performed in a secure environment that is resistant to attack from malicious software, and page permissions for kernel mode are set and maintained by the hypervisor.

[eBPF](https://ebpf.io/) is a technology that can run sandboxed programs in the Linux kernel without changing kernel source code or loading kernel modules. By making the Linux kernel programmable, infrastructure software can leverage existing layers, making them more intelligent and feature-rich without continuing to add additional layers of complexity to the system.

[eBPF for Windows](https://github.com/microsoft/ebpf-for-windows) is an eBPF implementation that runs on top of Windows. eBPF is a well-known technology for providing programmability and agility, especially for extending an OS kernel, for use cases such as DoS protection and observability.

[Coreboot](https://doc.coreboot.org/getting_started/index.html) is a replacement for your BIOS / UEFI with a strong focus on boot speed, security and flexibility. It is designed to boot your operating system as fast as possible without any compromise to security, with no back doors.

[TianoCore](https://www.tianocore.org/) is a community project supporting an open source implementation of the Unified Extensible Firmware Interface (UEFI). EDK II is a modern, feature-rich, cross-platform firmware development environment for the UEFI and UEFI Platform Initialization (PI) specifications.

[OWASP Zed Attack Proxy (ZAP)](https://owasp.org/www-project-zap/) is a free, open-source penetration testing tool being maintained under the umbrella of the Open Web Application Security Project (OWASP). ZAP is designed specifically for testing web applications and is both flexible and extensible. Great for pentesters, devs, QA, and CI/CD integration. At its core, ZAP is what is known as a "man-in-the-middle proxy."

[IDA Pro(Interactive DisAssembler Professional)](https://hex-rays.com/IDA-pro/) is a programmable and multi-processor disassembler combined with a local/remote debugger and along with a complete plugin programming environment. It's a great tool for testing and discovering security vulnerabilities.

[Ghidra](https://github.com/NationalSecurityAgency/ghidra) is a software reverse engineering (SRE) framework developed by NSA's Research Directorate for NSA's cybersecurity mission. It helps analyze any malicious code and malware like viruses, and can give cybersecurity professionals a better understanding of potential vulnerabilities in their networks and systems.

[Exploit Database](https://www.exploit-db.com/) is a CVE compliant archive of public exploits and corresponding vulnerable software, developed for use by penetration testers and vulnerability researchers. The goal is to serve the most comprehensive collection of exploits gathered through direct submissions, mailing lists, as well as other public sources, and present them.

[Rapid7 Vulnerability & Exploit Database](https://www.rapid7.com/db/) is a curated repository of vetted computer software exploits and exploitable vulnerabilities. Technical details for over 180,000 vulnerabilities and 4,000 exploits are available for security professionals and researchers to review. These vulnerabilities are utilized by our vulnerability management tool [InsightVM](https://www.rapid7.com/products/insightvm/).

[InsightVM](https://www.rapid7.com/products/insightvm/) is a data-rich resource that can amplify the other solutions in your tech stack, from SIEMs and firewalls to ticketing systems. Only InsightVM integrates with 40+ other leading technologies, and with an open RESTful API, your vulnerability data makes your other tools more valuable.

[DataWave](https://github.com/NationalSecurityAgency/datawave) is an ingest/query framework that leverages [Apache Accumulo](https://accumulo.apache.org/) to provide fast, secure data access.

[Emissary](https://github.com/NationalSecurityAgency/emissary) is a P2P based data-driven workflow engine that runs in a heterogeneous possibly widely dispersed, multi-tiered P2P network of compute resources. Workflow itineraries are not pre-planned as in conventional workflow engines, but are discovered as more information is discovered about the data.

[MADCert](https://github.com/NationalSecurityAgency/MADCert) is a cross-platform tool that consists of a certificate generator, a file system certificate manager, and a command line interface for the purposes of testing.

[BLESS(Bastion's Lambda Ephemeral SSH Service)](https://github.com/Netflix/bless) is an SSH Certificate Authority that runs as an AWS Lambda function and is used to sign SSH public keys.

[Zuul](https://github.com/Netflix/zuul) is an [L7 application gateway](https://www.f5.com/services/resources/glossary/application-layer-gateway) that provides capabilities for dynamic routing, monitoring, resiliency, security, and more.

[Chaos Monkey](https://github.com/Netflix/chaosmonkey) is a resiliency tool that helps applications tolerate random instance failures. It is fully integrated with [Spinnaker](https://www.spinnaker.io/), the continuous delivery platform. Chaos Monkey will work with any backend that Spinnaker supports (AWS, Google Compute Engine, Azure, Kubernetes, Cloud Foundry).

[Vuls](https://vuls.io/) is an agent-less vulnerability scanner for Linux, FreeBSD, Container, WordPress, Programming language libraries, Network devices.

[SpiderFoot](https://github.com/smicallef/spiderfoot) is an open source intelligence (OSINT) automation tool. It integrates with just about every data source available and utilises a range of methods for data analysis, making that data easy to navigate.

[Lynis](https://cisofy.com/lynis/) is a security auditing tool for Linux, macOS, and UNIX-based systems. Assists with compliance testing (HIPAA/ISO27001/PCI DSS) and system hardening. Agentless, and installation is optional.

[Priam](https://github.com/Netflix/Priam) is a tool/process for backup/recovery, Token Management, and Centralized Configuration management for Cassandra.

[Vector](https://github.com/Netflix/vector) is an on-host performance monitoring framework which exposes hand picked high resolution metrics to every engineer’s browser.

[Atlas](https://github.com/Netflix/atlas) is an in-memory dimensional [time series database](https://en.wikipedia.org/wiki/Time_series_database).

[SELinux](https://github.com/SELinuxProject/selinux) is a security enhancement to Linux which allows users and administrators more control over access control. Access can be constrained on such variables as which users and applications can access which resources. These resources may take the form of files. Standard Linux access controls, such as file modes (-rwxr-xr-x) are modifiable by the user and the applications which the user runs. Conversely, SELinux access controls are determined by a policy loaded on the system which may not be changed by careless users or misbehaving applications.

[AppArmor](https://www.apparmor.net/) is an effective and easy-to-use Linux application security system. AppArmor proactively protects the operating system and applications from external or internal threats, even zero-day attacks, by enforcing good behavior and preventing both known and unknown application flaws from being exploited. AppArmor supplements the traditional Unix discretionary access control (DAC) model by providing mandatory access control (MAC). It has been included in the mainline Linux kernel since version 2.6.36 and its development has been supported by Canonical since 2009.

[Control Groups(Cgroups)](https://www.redhat.com/sysadmin/cgroups-part-one) is a Linux kernel feature that allows you to allocate resources such as CPU time, system memory, network bandwidth, or any combination of these resources for user-defined groups of tasks (processes) running on a system.

[EarlyOOM](https://github.com/rfjakob/earlyoom) is a daemon for Linux that enables users to more quickly recover and regain control over their system in low-memory situations with heavy swap usage. 

[Libgcrypt](https://www.gnupg.org/related_software/libgcrypt/) is a general purpose cryptographic library originally based on code from GnuPG.

[Kali Linux](https://www.kali.org/)  is an open source project that is maintained and funded by Offensive Security, a provider of world-class information security training and penetration testing services.

[Pi-hole](https://pi-hole.net/) is a [DNS sinkhole](https://en.wikipedia.org/wiki/DNS_Sinkhole) that protects your devices from unwanted content, without installing any client-side software, intended for use on a private network. It is designed for use on embedded devices with network capability, such as the Raspberry Pi, but it can be used on other machines running Linux and cloud implementations.

[Aircrack-ng](https://www.aircrack-ng.org/) is a network software suite consisting of a detector, packet sniffer, WEP and WPA/WPA2-PSK cracker and analysis tool for 802.11 wireless LANs. It works with any wireless network interface controller whose driver supports raw monitoring mode and can sniff 802.11a, 802.11b and 802.11g traffic.

[Burp Suite](https://portswigger.net/burp) is a leading range of cybersecurity tools.

[KernelCI](https://foundation.kernelci.org/) is a community-based open source distributed test automation system focused on upstream kernel development. The primary goal of KernelCI is to use an open testing philosophy to ensure the quality, stability and long-term maintenance of the Linux kernel.

[Continuous Kernel Integration project](https://github.com/cki-project) helps find bugs in kernel patches before they are commited to an upstram kernel tree. We are team of kernel developers, kernel testers, and automation engineers.

[Cilium](https://cilium.io/) uses eBPF to accelerate getting data in and out of L7 proxies such as Envoy, enabling efficient visibility into API protocols like HTTP, gRPC, and Kafka. 

[Hubble](https://github.com/cilium/hubble) is a Network, Service & Security Observability for Kubernetes using eBPF.

[Istio](https://istio.io/) is an open platform to connect, manage, and secure microservices. Istio's control plane provides an abstraction layer over the underlying cluster management platform, such as Kubernetes and Mesos.

[Certgen](https://github.com/cilium/certgen) is a convenience tool to generate and store certificates for Hubble Relay mTLS.

[syzkaller](https://github.com/google/syzkaller) is an unsupervised, coverage-guided kernel fuzzer.

[SchedViz](https://github.com/google/schedviz) is a tool for gathering and visualizing kernel scheduling traces on Linux machines.

[oss-fuzz](https://google.github.io/oss-fuzz/) aims to make common open source software more secure and stable by combining modern fuzzing techniques with scalable, distributed execution.

[OSSEC](https://www.ossec.net/) is a free, open-source host-based intrusion detection system. It performs log analysis, integrity checking, Windows registry monitoring, rootkit detection, time-based alerting, and active response.

[Metasploit Project](https://www.metasploit.com/) is a computer security project that provides information about security vulnerabilities and aids in penetration testing and IDS signature development.

[Wfuzz](https://github.com/xmendez/wfuzz) was created to facilitate the task in web applications assessments and it is based on a simple concept: it replaces any reference to the FUZZ keyword by the value of a given payload.

[Nmap](https://nmap.org/) is a security scanner used to discover hosts and services on a computer network, thus building a "map" of the network. 

[Patchwork](https://github.com/getpatchwork/patchwork) is a web-based patch tracking system designed to facilitate the contribution and management of contributions to an open-source project. 

[pfSense](https://www.pfsense.org/) is a free and open source firewall and router that also features unified threat management, load balancing, multi WAN, and more.

[Snowpatch](https://github.com/ruscur/snowpatch) is a continuous integration tool for projects using a patch-based, mailing-list-centric git workflow. This workflow is used by a number of well-known open source projects such as the Linux kernel.

[Snort](https://www.snort.org/) is an open-source, free and lightweight network intrusion detection system (NIDS) software for Linux and Windows to detect emerging threats.

[Wireshark](https://www.wireshark.org/) is a free and open-source packet analyzer. It is used for network troubleshooting, analysis, software and communications protocol development, and education. 

[Tink](https://github.com/google/tink) is a multi-language, cross-platform, open source library that provides cryptographic APIs that are secure, easy to use correctly, and harder to misuse. 

[ClamAV](https://www.clamav.net/) is an open source antivirus engine for detecting trojans, viruses, malware & other malicious threats.


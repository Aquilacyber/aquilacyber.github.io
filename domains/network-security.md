# Introduction to network security

Last reviewed: 2026-10-03

Network security is the work of controlling and watching the traffic between systems, so that only the right devices and people can talk to each other and anything unusual is noticed. It covers the equipment that carries traffic, the rules that decide what may pass and the encryption that protects data on the way.

## Why it matters

Almost every attack crosses a network. The network is also where defenders can see the most: who talked to whom, when and how much. A well-designed network limits the damage when one machine is compromised. A flat, open one lets an attacker walk from a stolen laptop to the servers.

## Key ideas

- **Attack surface.** Everything that can be reached. Each open port and each exposed service adds to it.
- **Default deny.** Block everything and allow only what is needed.
- **Segmentation.** Divide the network into zones so a problem in one does not spread to all.
- **Defence in depth.** Layer controls so one failure does not expose everything.
- **Encryption in transit.** Protect data as it moves, with TLS and VPNs.
- **Visibility.** Collect logs and traffic data. You cannot defend what you cannot see.

| Control | What it does | Example |
|---|---|---|
| Firewall | Allows or blocks traffic by rule | Allow web traffic in, block everything else |
| Segmentation | Separates systems by purpose | Servers apart from staff laptops |
| Secure protocols | Replace clear-text ones | SSH instead of Telnet |
| Intrusion detection and prevention | Alerts on or blocks known bad patterns | Suricata, Snort |
| Remote access | Lets people in safely | VPN with multi-factor authentication |
| Monitoring | Records who talked to whom | Flow data, DNS logs, packet capture |

The [network security basics guide](../guides/network-security-basics.md) covers each of these in detail and has three lab exercises.

## What people in this field do

- A network security engineer designs firewall rules, VPNs and segmentation, and keeps them correct as the network changes.
- A SOC analyst reads firewall, DNS and intrusion detection alerts to spot attacks.
- A penetration tester maps a network the way an attacker would and reports what is exposed.
- An incident responder traces how an attacker moved from one machine to another.

## Common tools

| Tool | What it does |
|---|---|
| [Wireshark](https://www.wireshark.org/) | Captures and analyses packets |
| tcpdump | Captures packets from the command line |
| [Nmap](https://nmap.org/) | Finds hosts, open ports and services |
| [Zeek](https://zeek.org/) | Turns traffic into structured logs |
| [Suricata](https://suricata.io/) | Intrusion detection and prevention |
| ufw, iptables and nftables | Host firewalls on Linux |
| [OPNsense](https://opnsense.org/) and [pfSense](https://www.pfsense.org/) | Open source firewall and router software |

## Try it in your lab

1. Capture a web request in Wireshark and find the DNS lookup, the TCP handshake and the HTTP or TLS exchange.
2. Run `nmap -sV` against a lab VM, turn on `ufw` with default deny, and scan again. Compare the two results.
3. Send a clear-text password over HTTP between two VMs and find it in the capture. Then do the same over SSH and show you cannot read it.
4. Open a training capture from [Malware Traffic Analysis](https://www.malware-traffic-analysis.net/) in Wireshark. Read the page's instructions first. Open only the capture file, and never run any sample that comes with it.
5. Put two VMs on separate internal networks and confirm they cannot reach each other.

## Mistakes beginners make

- Treating NAT as if it were a firewall
- Leaving a flat network with no zones
- Exposing remote desktop or file sharing to the internet
- Ignoring DNS logs, which show where malware tries to connect
- Writing firewall rules and never reviewing them

## Where to go next

- The [network security basics guide](../guides/network-security-basics.md)
- The [blue team track](../tracks/blue-team.md)
- Roles: [Security Operations Center (SOC) Analyst](../careers/security-operations-center.md), [Network Penetration Tester](../careers/network-penetration-tester.md), [Security Architect](../careers/security-architect.md)
- Learn more: [Professor Messer](https://www.professormesser.com/), [Practical Networking](https://www.practicalnetworking.net/), [The Nmap book](https://nmap.org/book/)

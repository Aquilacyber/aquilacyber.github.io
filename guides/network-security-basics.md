# Network security basics

Last reviewed: 2026-10-03

Every attack that reaches a system travels over a network, and every defender watches one. This page covers the core ideas of securing a network, the protocols that cause trouble, and lab exercises that prove you understand them. Do [phase 1 networking](../roadmap/01-foundations.md) first. You need to know what an IP address, a port and DNS are before this page makes sense.

## Core ideas

- **Attack surface.** Everything on your network that someone could try to reach. Each open port and each exposed service adds to it. Turn off what you do not use.
- **Default deny.** Block everything, then allow only what is needed. It is easier to defend a short allow list than a long block list.
- **Least privilege.** Give each device and user the access they need and no more.
- **Defence in depth.** Use several layers, so that one failure does not expose everything.
- **Segmentation.** Divide a network into zones so a problem in one does not spread to all.

## Firewalls

A firewall allows or blocks traffic according to rules.

| Type | What it looks at |
|---|---|
| Packet filter | Source and destination address, port and protocol, one packet at a time |
| Stateful firewall | The same, plus whether a packet belongs to a connection that was started from inside. Most firewalls today are stateful |
| Next-generation firewall | Adds application awareness and content inspection |
| Web application firewall (WAF) | Sits in front of a website and filters web attacks such as SQL injection. It protects applications, not the whole network |

Rules are checked in order, and the first match wins. Put specific rules before general ones, and finish with a deny rule.

A host firewall protects a single machine. On Ubuntu, `ufw` is the simple front end:

```
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw enable
sudo ufw status verbose
```

## Segmentation

A flat network, where every device can reach every other device, lets an attacker who compromises one laptop reach the servers. Segmentation separates devices by purpose and controls what may cross between the zones.

A typical design has these zones, each behind a firewall:

- **Users**, for staff laptops
- **Servers**, for internal systems
- **DMZ**, for systems that must be reachable from the internet, such as a public website
- **Guest**, for visitors, with internet access only
- **IoT and cameras**, which are often poorly secured, kept away from everything else

Segments are often built with VLANs, which split one physical switch into several logical networks.

## NAT and VPNs

**Network address translation (NAT)** lets many private addresses share one public address. It hides internal addresses from the internet as a side effect. It is not a security control by itself. A firewall is.

A **VPN** creates an encrypted tunnel between a device and a network, so traffic crossing an untrusted network cannot be read. Common VPN technologies are IPsec, OpenVPN and WireGuard.

## Protocols and their risks

Some protocols were designed when networks were trusted and send everything in clear text. A person who can capture traffic can read it.

| Protocol | Port | Problem | Use instead |
|---|---|---|---|
| Telnet | 23 | Sends passwords in clear text | SSH, port 22 |
| FTP | 21 | Sends passwords and files in clear text | SFTP or FTPS |
| HTTP | 80 | No encryption | HTTPS, port 443 |
| SNMP v1 and v2c | 161 | Community strings sent in clear text | SNMPv3 |
| LDAP | 389 | Clear text unless wrapped in TLS | LDAPS, port 636, or LDAP with StartTLS |
| SMB | 445 | Should never face the internet | Keep it internal and patched |
| RDP | 3389 | A frequent target of password guessing when exposed | A VPN or a gateway with MFA in front |

DNS, on port 53, is not encrypted by default, and attackers abuse it. Defenders watch DNS logs because malware has to look up its servers.

## Encryption in transit

**TLS** protects data between a browser and a website, and between many other programs and their servers. It does two jobs: it encrypts the traffic and it proves the server's identity with a certificate issued by a trusted certificate authority. Learn to read a certificate in your browser and check its name, issuer and expiry date.

## Wireless security

- Use **WPA3** where available. **WPA2** with a long, unique passphrase is acceptable.
- Do not use WEP, which is broken, or an open network for anything private.
- Turn off WPS, the push-button setup feature, which has known weaknesses.
- Put visitors on a separate guest network.
- Organisations should use WPA2 or WPA3 Enterprise, where each person logs in with their own credentials instead of sharing one passphrase.
- On public Wi-Fi assume others can see your traffic. Use HTTPS and a VPN.

## Common network attacks and defences

| Attack | What it is | Defences |
|---|---|---|
| Port scanning | Probing to find open services before an attack | Expose fewer services, filter at the firewall, alert on scans |
| Sniffing | Capturing traffic to read it | Encrypt traffic, restrict who can capture on the network |
| ARP spoofing | Lying on a local network to sit between two devices | Port security and dynamic ARP inspection on managed switches, encryption on top |
| DNS spoofing | Giving a victim a false answer to a DNS question | DNSSEC where supported, TLS certificate checks |
| Denial of service | Overwhelming a service until it stops answering | Rate limiting, upstream DDoS protection, enough capacity |
| Password guessing on remote services | Trying passwords against SSH, RDP or VPNs | MFA, key-based login, lockout and rate limits |
| Rogue devices | An unknown device plugged into the network | Network access control with 802.1X, switch port security |

## Monitoring

A network you cannot see is a network you cannot defend. At minimum:

- Collect firewall, DNS and authentication logs in one place.
- Record flow data, which says who talked to whom and how much, with tools such as NetFlow or similar.
- Capture packets when you need to investigate, with Wireshark or tcpdump.
- Run an intrusion detection system such as Suricata or Zeek.

See [security operations concepts](security-operations-concepts.md) and the [defensive tools list](../reference/defensive-tools.md).

## Zero trust

Older designs trusted anything inside the network. Zero trust drops that assumption. Each request is checked on who is asking, from which device and for what, whether the device is inside or outside the building. It does not replace the ideas above. It builds on segmentation, least privilege and strong identity.

## Build it yourself

Use only your own lab on a host-only network. See the [lab setup guide](lab-setup.md).

### Exercise 1: see a clear-text password

1. On an Ubuntu VM, serve a folder with `python3 -m http.server 8000`.
2. On your Kali VM, start a Wireshark capture on the lab interface.
3. Send a request with credentials: `curl -u alice:secret http://<ubuntu-ip>:8000/`.
4. Find the request in the capture. Open the HTTP headers and read the `Authorization` line. Decode the value. Basic authentication is encoded, not encrypted.
5. Now capture an SSH login to the same machine. Show that you cannot read the content.
6. Write two sentences on what this means for any service that uses HTTP or Telnet.

### Exercise 2: a firewall that changes what a scan sees

1. On the Ubuntu VM, install and start the SSH server and the Python web server above.
2. From Kali, run `nmap -sV <ubuntu-ip>`. Save the result.
3. On Ubuntu, set `ufw` to default deny and allow only port 22.
4. Run the same scan again. Compare the two results line by line.
5. Write down which ports changed state and what Nmap reports for filtered ports.

### Exercise 3: segmentation by hand

1. Put one VM on an internal network named `users` and another on one named `servers`.
2. Confirm they cannot reach each other with `ping`.
3. Explain, in your own words, what you would need to add so that only the web port could cross between them.

## Where to learn more

- [Professor Messer](https://www.professormesser.com/) for networking and security concepts
- [Practical Networking](https://www.practicalnetworking.net/) for clear articles on how networks work
- [Wireshark documentation](https://www.wireshark.org/docs/)
- [The Nmap book](https://nmap.org/book/)
- The networking rooms on [TryHackMe](https://tryhackme.com/)
- The [glossary](glossary.md)

## Checkpoint

You have learned enough when you can do these without help:

- [ ] Explain default deny and why it is safer than a block list
- [ ] Say why a flat network is dangerous and what segmentation fixes
- [ ] Name three clear-text protocols and what replaces each
- [ ] Capture traffic and show a clear-text credential in Wireshark
- [ ] Write a host firewall rule set that allows only SSH
- [ ] Explain why NAT is not a firewall

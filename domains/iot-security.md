# Introduction to IoT security

Last reviewed: 2026-10-03

The Internet of Things (IoT) is the large and growing set of small connected devices: cameras, routers, smart meters, door locks, sensors, medical equipment and the card terminals in shops. Each one is a small computer running software called firmware, usually with limited memory and power. IoT security is the work of making those devices, and the networks and services behind them, hard to attack.

## Why it matters

IoT devices are everywhere, they are often cheap and they are often forgotten. Many ship with a default password, receive no updates and stay in use for ten years. Attackers take advantage of that. The Mirai botnet in 2016 grew by logging in to cameras and routers that still had factory passwords, and then used them to flood websites with traffic. Some devices also carry physical risk, because a hacked meter, lock or medical device can cause harm that a hacked website cannot.

In Nigeria you will meet routers, CCTV cameras, smart meters and payment terminals. These are all embedded devices with the same kinds of weakness.

## The four layers

A connected product is more than the device in your hand. Each layer has its own attack surface.

| Layer | What it includes | Typical weaknesses |
|---|---|---|
| Hardware | The circuit board, chips and debug ports | Open debug ports such as UART or JTAG, firmware that can be read off the flash chip |
| Firmware | The software on the device | Hard-coded passwords and keys, outdated components, updates that are not signed |
| Network | How it talks to others: Wi-Fi, Bluetooth Low Energy, Zigbee, LoRaWAN, cellular | Clear-text protocols, services left open, weak pairing |
| Cloud and app | The mobile app and the server that manages the device | Weak authentication on the API, one account that can reach every device |

## Key ideas

- **Weak or default credentials.** The most common problem. Every device should have its own strong credentials.
- **Updates.** A device that cannot be updated securely will stay vulnerable. Updates should be signed so a device refuses a fake one.
- **Secure boot.** The device checks that its software is genuine before it runs.
- **Minimal services.** A device should not listen on ports it does not need.
- **Encryption in transit.** Data between the device, the app and the cloud should use TLS or an equivalent. MQTT, a common messaging protocol for devices, sends clear text on port 1883 and can use TLS on port 8883.
- **Isolation.** Put IoT devices on their own network segment so a hacked camera cannot reach your laptop or your servers.
- **End of life.** Plan for what happens when the vendor stops supporting a device.

Two public documents help here. The OWASP IoT Top 10, from 2018, lists the most common weaknesses, including weak passwords, insecure update mechanisms, outdated components and insecure default settings. ETSI EN 303 645 and the NIST IR 8259 series set out baseline security expectations for consumer and manufactured devices.

## What people in this field do

- A hardware or embedded security engineer designs secure boot, update and key storage, and tests devices before release.
- A penetration tester or researcher examines a device's hardware, firmware, network traffic and app for weaknesses.
- An industrial control and SCADA security specialist protects devices that run factories, power and water. See the [SCADA profile](../careers/scada-security-specialist.md).
- A defender segments and monitors the IoT devices on a corporate network.

## Common tools

| Tool | What it does |
|---|---|
| [Binwalk](https://github.com/ReFirmLabs/binwalk) | Finds and extracts files inside a firmware image |
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | Reverse engineering of programs |
| QEMU | Emulates other processors, so you can run firmware without the hardware |
| [Wireshark](https://www.wireshark.org/) and [Nmap](https://nmap.org/) | Show the traffic and the open ports of a device |
| USB-to-serial adapter and multimeter | Connect to a device's serial console and find its pins |
| [OWASP IoTGoat](https://github.com/OWASP/IoTGoat) | A deliberately vulnerable firmware for practice |

## Try it

Only use devices you own, or practice firmware built for the purpose.

1. List every connected device in your home or lab from your router's device page. For each one, say whether you changed the default password and when it last had an update.
2. Move your IoT devices onto a guest or separate network and check that your computers cannot reach them.
3. Scan one of your own devices with `nmap -sV <device-ip>` and list the services it offers. Ask whether each one is needed.
4. Capture the traffic between a device and its app in Wireshark. Say which parts are encrypted and which are clear text.
5. Download a firmware image from the IoTGoat project and run `binwalk` on it, then `binwalk -e` to extract it. Browse the files and look for configuration files and credentials.
6. Threat model a smart door lock or a CCTV camera using the [threat modeling introduction](threat-modeling.md).

## Law and ethics

Search engines such as Shodan list devices that are reachable from the internet. Looking at the list is one thing. Connecting to, logging in to or changing a device that you do not own is unauthorised access, even when it uses a default password. If you find an exposed device, report it to the owner or to a national response team such as ngCERT. See the [ethics and law guide](../guides/ethics-and-law.md).

## Mistakes beginners make

- Leaving default credentials in place
- Putting every device on one flat network
- Assuming a small device is too unimportant to attack
- Having no way to update or replace a device
- Testing a device that belongs to someone else

## Where to go next

- Roles: [Security Engineer (Hardware)](../careers/security-engineer-hardware.md), [SCADA Security Specialist](../careers/scada-security-specialist.md), [Security Researcher](../careers/security-researcher.md)
- A large list of hardware, radio and firmware resources: [reference: IoT security](../reference/iot-security.md)
- Related: [network security](network-security.md), [threat modeling](threat-modeling.md) and the [network security basics guide](../guides/network-security-basics.md)

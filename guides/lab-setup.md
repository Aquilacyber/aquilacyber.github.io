# Lab setup

You need a safe place to practise. This page covers what to run, what hardware you need, what to do if you have no laptop and how to cope with expensive data and unreliable power.

## What a beginner lab is

Three parts:

1. A virtualisation program on your own computer.
2. An attacker machine, usually Kali Linux.
3. One or more deliberately vulnerable targets.

The machines talk to each other on a private network that never touches your home or campus network. That last part matters. Vulnerable systems must not be reachable from anywhere else.

## Hardware

| Spec | Workable | Comfortable |
|---|---|---|
| RAM | 8 GB | 16 GB |
| Storage | 100 GB free, SSD preferred | 250 GB free |
| CPU | Any 64-bit CPU with virtualisation support | 4 or more cores |

With 8 GB you can run one attacker VM and one target at a time. Close your browser tabs first. Heavy tools such as a full SIEM may not fit, and the [blue team track](../tracks/blue-team.md) points to lighter options.

Check that virtualisation is switched on. On most laptops it is a setting in the BIOS or UEFI, often called Intel VT-x or AMD-V. If your virtual machines refuse to start, that is the first thing to check.

## Software

- **Virtualisation:** [VirtualBox](https://www.virtualbox.org/) is free. Windows users with Pro editions can use Hyper-V instead. Do not run both at once.
- **Attacker machine:** [Kali Linux](https://www.kali.org/get-kali/) publishes ready-made virtual machine images, so you do not need to install it from scratch.
- **Windows target:** Microsoft publishes time-limited evaluation versions of Windows at the [Evaluation Center](https://www.microsoft.com/en-us/evalcenter/). They are free and ideal for practice.
- **Vulnerable web applications:** [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) and [DVWA](https://github.com/digininja/DVWA).
- **Vulnerable machines:** [VulnHub](https://www.vulnhub.com/) hosts downloadable practice machines.
- **Blue team tools:** [Security Onion](https://securityonionsolutions.com/), [Wazuh](https://wazuh.com/) and Sysmon.

## Network settings

- Use a **host-only** or **internal** network for the attacker and the targets.
- Add a second **NAT** adapter to the attacker machine only, for updates.
- Never use **bridged** networking for a vulnerable machine. It puts the machine on your real network.
- Take a **snapshot** of each machine when it is clean. Roll back when you break something, which you will.

## If you do not have a laptop

You can still do phase 1 and most of phase 2.

- [OverTheWire](https://overthewire.org/wargames/) runs over SSH. A phone with an SSH client app is enough.
- [picoCTF](https://picoctf.org/) runs in the browser.
- [TryHackMe](https://tryhackme.com/) gives you a browser-based attacker machine. Free usage is limited each day, so use it for focused sessions.
- [PortSwigger Web Security Academy](https://portswigger.net/web-security) needs only a browser and Burp Suite Community Edition on a computer.

Many universities, libraries and community hubs have computer labs. Ask whether you can use one and whether they allow security tools. Get permission before you install anything.

## Data and power

- Download large files such as ISO images and VM images once, from the cheapest and fastest connection you can reach. Keep them on a flash drive and share them with other learners in the community.
- Many providers sell cheaper night or weekend bundles. Check yours.
- Pause updates inside your VMs when you are on mobile data and run them later on a better connection.
- Lab work saves badly when the power cuts. Use the VM snapshot feature, save your notes often and keep a power bank or UPS if you can afford one.

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| VM will not start, error mentions VT-x or AMD-V | Virtualisation is off in the BIOS or UEFI, or Hyper-V is running |
| VM is very slow | Too little RAM given to the VM, or too many programs open on the host |
| Attacker and target cannot see each other | They are on different virtual networks. Put both on the same host-only network |
| Kali cannot update | The NAT adapter is missing or disabled |

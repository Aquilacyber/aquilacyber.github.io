# Windows and Active Directory basics

Last reviewed: 2026-10-03

Most organisations run Windows on their laptops and servers, and most of those machines are managed through Active Directory. Attackers go after it for that reason, and defenders spend much of their time reading its logs. You need to know how it works whichever [track](../tracks/README.md) you pick.

This page covers what to learn and gives you exercises to prove you have learned it. It fits into [phase 1](../roadmap/01-foundations.md).

## Part 1: Windows basics

### Users, groups and permissions

- Every action in Windows runs as a user. A user belongs to groups, and permissions are usually granted to groups.
- **Administrators** is the local group with full control of a machine. **Users** is the normal group.
- User Account Control (UAC) asks for confirmation before something runs with administrator rights.
- NTFS permissions control access to files and folders. Right-click a folder, open Properties, then Security, and read who can do what.

Try this: create two local users, make one an administrator and compare what each one can change.

### Processes and services

- A **process** is a running program. Task Manager lists them.
- A **service** is a program that runs in the background and often starts at boot. Services are a common place to hide persistence, because few people look at them.
- Learn the usual process tree: for example, `explorer.exe` starts the programs you open, and `svchost.exe` hosts many services. Something unfamiliar starting from an Office program deserves a look.

### The registry

The registry is a database of settings. You will see five top-level hives. Two matter most to a beginner:

- `HKEY_LOCAL_MACHINE` (HKLM) holds machine-wide settings.
- `HKEY_CURRENT_USER` (HKCU) holds settings for the logged-in user.

Programs that start at logon are listed under `Run` keys in both. Defenders check these. Do not edit the registry on a machine you care about. Use a lab VM.

### The command line and PowerShell

Learn a short list of commands first:

| Command | What it shows |
|---|---|
| `whoami /groups` | Who you are and which groups you are in |
| `ipconfig /all` | Network configuration |
| `netstat -ano` | Open connections and the process that owns each |
| `tasklist` | Running processes |
| `net user` | Local user accounts |
| `Get-Process` | Running processes, in PowerShell |
| `Get-Service` | Services, in PowerShell |
| `Get-WinEvent` | Read event logs, in PowerShell |

### Logs

Open Event Viewer and look at **Windows Logs**. Three logs matter:

- **Security** records logons, privilege use and account changes.
- **System** records services starting and stopping and driver problems.
- **Application** records messages from installed software.

### Built-in protection

Know what is there: Microsoft Defender Antivirus, Windows Firewall, BitLocker for disk encryption and Windows Update. Be able to say where each is configured.

## Part 2: Active Directory

### What it is

Active Directory (AD) is Microsoft's directory service. It keeps one central record of the users, groups and computers in an organisation, and it answers the question "is this person who they say they are, and what may they do?" for every machine in the domain.

### The building blocks

| Term | Meaning |
|---|---|
| Domain | A group of users, computers and other objects managed together, for example `company.local` |
| Domain controller (DC) | A server that holds a copy of the directory and handles logons. Compromise of a DC is serious |
| Forest and tree | A forest is the top-level boundary. A tree is a set of domains that share a name space |
| Organisational unit (OU) | A folder inside a domain used to organise objects and apply policy |
| User, group, computer | The main kinds of object. Groups collect users so permissions can be granted once |
| Group Policy (GPO) | Settings pushed to many machines or users at once, such as password rules or a locked-down desktop |
| LDAP | The protocol used to query the directory |
| DNS | Active Directory depends on DNS to find domain controllers |

Two groups to know by name: **Domain Admins** has full control of the domain, and **Enterprise Admins** has full control of the forest. Membership of these groups should be tiny and closely watched.

### How logon works

AD uses two authentication protocols:

- **Kerberos** is the default. In outline: you prove who you are to the domain controller and receive a ticket. You present that ticket to services instead of sending your password. Tickets expire.
- **NTLM** is an older protocol kept for compatibility. It is weaker, and many organisations try to turn it off.

You do not need the cryptographic detail yet. You need to know the vocabulary so that a log line mentioning a ticket request makes sense.

### Microsoft Entra ID

Microsoft renamed Azure Active Directory to **Microsoft Entra ID** in 2023. It is the cloud identity service used by Microsoft 365 and Azure. It is not the same product as on-premises AD, although many organisations connect the two in a hybrid setup. Learn on-premises AD first, then the cloud service.

## Part 3: The security view

Defenders and attackers both focus on AD because whoever controls identity controls everything. Know the broad categories of weakness. At this stage you only need to recognise them, not exploit them.

- Weak or reused passwords
- Too many accounts in privileged groups
- Service accounts with powerful rights and passwords that never change
- Legacy protocols such as NTLM left switched on
- Unpatched domain controllers
- Poorly designed Group Policy

Defenders reduce these through least privilege, strong password policy, multi-factor authentication, patching and monitoring.

### Event IDs worth knowing

Read these in the Security log on a domain controller or a Windows machine.

| Event ID | What it records |
|---|---|
| 4624 | A successful logon |
| 4625 | A failed logon |
| 4634 | A logoff |
| 4672 | Special privileges assigned to a new logon, which means an administrator-level logon |
| 4688 | A new process was created (needs process auditing turned on) |
| 4720 | A user account was created |
| 4728, 4732, 4756 | A member was added to a security group |
| 4768 | A Kerberos ticket was requested |
| 4769 | A Kerberos service ticket was requested |
| 4776 | The domain controller tried to validate credentials, which covers NTLM |
| 1102 | The Security log was cleared. Treat this one as suspicious |
| 7045 | A new service was installed (System log) |

Several of these only appear if the right auditing is enabled. Learning what is audited by default and what is not is a useful exercise.

## Part 4: Build it yourself

You learn AD by building a domain, not by reading about one. Plan on a machine with at least 16 GB of RAM for a comfortable lab. With 8 GB it can be done with one small domain controller and one client, running only those two, but it will be slow. See the [lab setup guide](lab-setup.md).

1. Download a Windows Server evaluation from the [Microsoft Evaluation Center](https://www.microsoft.com/en-us/evalcenter/). It is free for a limited period.
2. Install it in a VM and add the Active Directory Domain Services role. Promote it to a domain controller for a new domain.
3. Create two OUs, five users and two groups. Add users to the groups.
4. Create a Group Policy that sets a minimum password length and link it to an OU.
5. Install a Windows 10 or 11 client VM, join it to the domain and log in as a domain user.
6. On the domain controller, find the logon you just made in the Security log. Identify the event ID, the account name and the logon type.
7. Fail a logon on purpose and find event 4625.
8. Add a user to a group and find the matching event.
9. Take a snapshot of the finished lab.

## Where to learn more

- The Windows Fundamentals and Active Directory Basics rooms on [TryHackMe](https://tryhackme.com/)
- [Microsoft Learn](https://learn.microsoft.com/en-us/training/), including the Windows Server and identity modules
- [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) for richer process and network logging, covered in the [blue team track](../tracks/blue-team.md)
- The [glossary](glossary.md) for terms

## Checkpoint

You have learned enough when you can do these without help:

- [ ] Explain the difference between a local user and a domain user
- [ ] Open Event Viewer and find a logon event for a specific user
- [ ] Explain what a domain controller does and why it is a high-value target
- [ ] Say what Group Policy is and give two examples of what it controls
- [ ] Describe, in plain words, why Domain Admins membership should be small
- [ ] Build a small domain in a lab and join a client to it

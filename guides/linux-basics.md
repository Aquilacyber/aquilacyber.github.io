# Linux basics

Last reviewed: 2026-10-03

Most servers, cloud machines, security tools and capture the flag targets run Linux. You will use it whichever [track](../tracks/README.md) you pick. This page covers what to learn and gives you a lab to prove it. It fits into [phase 1](../roadmap/01-foundations.md) and pairs with the [Windows and Active Directory basics](windows-and-active-directory.md) page.

Commands below work on Debian-based systems such as Ubuntu and Kali. Red Hat family systems differ in a few places, and the page says where.

## Part 1: The basics

### Where things live

| Path | What it holds |
|---|---|
| `/home` | Each user's files |
| `/root` | The home directory of the root user |
| `/etc` | System configuration files |
| `/var/log` | Logs |
| `/tmp` | Temporary files that anyone can write to |
| `/usr` and `/bin` | Programs |
| `/proc` | Live information about processes, shown as files |
| `/dev` | Devices, shown as files |

### Users and groups

- `root` is the all-powerful account, with user ID 0.
- `/etc/passwd` lists accounts. It does not hold passwords despite the name.
- `/etc/shadow` holds password hashes. Only root can read it.
- `id` shows your user and groups. `whoami` shows your username.
- `sudo` runs a single command as root if you are allowed to. `/etc/sudoers` controls who may, and you edit it with `visudo`.

### Permissions

Run `ls -l`. You will see lines like this:

```
-rwxr-x---  1 alice dev  4096 Oct  3 10:00 backup.sh
```

Read the first column in four parts: the file type (`-` for a file, `d` for a directory), then the owner's permissions (`rwx`), the group's (`r-x`) and everyone else's (`---`).

Each permission has a number: read is 4, write is 2 and execute is 1. Add them up for each part. So `rwxr-x---` is 750.

| Command | What it does |
|---|---|
| `chmod 750 backup.sh` | Sets permissions to rwxr-x--- |
| `chmod u+x backup.sh` | Adds execute for the owner |
| `chown alice:dev backup.sh` | Changes owner and group |

Three special permissions matter for security:

- **SUID** (setuid): the program runs as its owner, often root. `passwd` needs this to change your password. A badly chosen SUID program is a classic way to gain root.
- **SGID**: the program or directory uses the file's group.
- **Sticky bit**: in a shared directory such as `/tmp`, only a file's owner can delete it.

### Processes and services

| Command | What it does |
|---|---|
| `ps aux` | Lists all processes |
| `top` | Live view of processes |
| `kill 1234` | Asks process 1234 to stop |
| `systemctl status ssh` | Shows a service's state |
| `systemctl enable --now ssh` | Starts a service and sets it to start at boot |
| `journalctl -u ssh` | Shows a service's logs |

### Packages

On Debian-based systems:

```
sudo apt update
sudo apt upgrade
sudo apt install nmap
```

On Red Hat family systems, `dnf` does the same job.

### Networking commands

| Command | What it shows |
|---|---|
| `ip a` | Your network interfaces and addresses |
| `ip route` | Your routing table |
| `ss -tulpn` | Listening ports and the program behind each |
| `ping host` | Whether a host answers |
| `curl -I https://example.com` | The response headers of a web request |
| `dig example.com` | DNS answers |

### Reading and searching text

Learn these until they are habit:

- `cat`, `less`, `head` and `tail -f` to read files, and to follow a log as it grows
- `grep -i "text" file` to search, with `-r` to search folders, `-n` for line numbers and `-v` to invert
- `find / -name "*.conf" 2>/dev/null` to find files
- `sort`, `uniq -c`, `cut`, `wc -l` to count and summarise
- `awk` and `sed` for picking columns and changing text
- The pipe `|` to send one command's output into the next, and `>` and `>>` to write output to a file

### Logs

Authentication events go to `/var/log/auth.log` on Debian-based systems and `/var/log/secure` on Red Hat family systems. `journalctl` reads the systemd journal on both. Read these logs early. Defenders live in them.

### SSH

SSH is how you reach most Linux servers.

- `ssh alice@192.168.56.10` logs in with a password or a key.
- `ssh-keygen` creates a key pair. `ssh-copy-id alice@192.168.56.10` installs your public key on the server.
- The server's settings are in `/etc/ssh/sshd_config`. Two important ones are `PasswordAuthentication` and `PermitRootLogin`.

### Scheduled jobs

`cron` runs commands on a schedule. `crontab -l` lists yours, and system jobs are in `/etc/crontab` and `/etc/cron.d`. Attackers like cron because a scheduled job survives a reboot.

### Shell scripts

A script is a text file of commands. The first line, `#!/bin/bash`, says which shell runs it. Learn variables, `if`, `for` loops and exit codes. Python is the better choice for anything long, and you will learn it in phase 1 too.

## Part 2: The security view

Common weaknesses that testers look for and defenders fix:

- Weak or default passwords
- SSH open to the internet with password login on
- World-writable files and directories where they should not be
- SUID programs that can be abused to become root
- Sudo rules that let a user run something too powerful
- Cron jobs that run a script a normal user can edit
- Old packages with known vulnerabilities
- Secrets left in shell history or configuration files

Defenders reduce these with key-only SSH logins, root login turned off, regular updates, least privilege, a host firewall such as `ufw`, and logging that someone actually reads. Tools such as fail2ban block repeated failed logins, and auditd records detailed system events.

Commands that help you check a machine you own:

| Command | What it shows |
|---|---|
| `last` | Recent logins |
| `w` | Who is logged in and what they are doing |
| `find / -perm -4000 -type f 2>/dev/null` | Every SUID file |
| `sudo -l` | What your account may run with sudo |
| `ss -tulpn` | What is listening for connections |

## Part 3: Build it yourself

Plan on 2 to 4 GB of RAM for one server VM. See the [lab setup guide](lab-setup.md).

1. Download [Ubuntu Server](https://ubuntu.com/download/server) and install it in a VM on a host-only network.
2. Create two users, `alice` and `bob`. Create a folder that `alice` owns and `bob` cannot read. Prove it by logging in as `bob`.
3. Install the SSH server. Log in from your host machine, first with a password and then with a key.
4. Turn off password login in `sshd_config`, restart the service and confirm that a password login now fails.
5. Fail a login on purpose three times, then find the three entries in `/var/log/auth.log`.
6. Count failed logins per source address with a one-line command:

   ```
   grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn
   ```

   Work out why `$(NF-3)` picks the address. Then write the same logic as a Python script. That is the phase 1 scripting exercise.
7. List all SUID files. Look up two of them and say why they need the permission.
8. Create a cron job that appends the date to a file every minute. Find it with `crontab -l`, then remove it.
9. Take a snapshot of the finished lab.

## Where to learn more

- [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) for practice that runs entirely in a terminal
- The Linux Fundamentals rooms on [TryHackMe](https://tryhackme.com/)
- [Linux Journey](https://linuxjourney.com/)
- [The Linux Command Line](https://linuxcommand.org/tlcl.php) by William Shotts
- The [glossary](glossary.md)

## Checkpoint

You have learned enough when you can do these without help:

- [ ] Read an `ls -l` line and say who can read, write and run the file
- [ ] Change a file's permissions with `chmod` using both letter and number forms
- [ ] Find the process listening on port 22 and the service that started it
- [ ] Find a failed SSH login in the log and say which address it came from
- [ ] Explain why SUID programs matter for security
- [ ] Log in over SSH with a key and with password login disabled

# Endpoint Security: Theory, Techniques, and Tools

# Theory

## `Theory` - Table of Contents

- [Introduction](#introduction)
- [What is endpoint security](#what-is-endpoint-security-)

## `Techniques` - Table of Contents

## `Tools` - Table of Contents

## `What is Endpoint Security? `

You'll often find the term **endpoint** used to describe systems, servers, and other types of devices that need protection. In computing, the term endpoint refers to pretty much anything connected to the network, and endpoint security refers to solutions designed to protect them.

![endpoint-nist](https://github.com/paulveillard/cybersecurity-endpoint-security/blob/main/img/endpoint_dr_guide_1.png)

[Endpoint security](https://www.fortinet.com/resources/cyberglossary/what-is-endpoint-security), like endpoint detection and response, is the process of protecting devices like workstations, servers, and other devices (that can accept a security client) from malicious threats and cyberattacks. Endpoint security software enables businesses to protect devices that employees use for work purposes or servers that are either on a network or in the cloud from cyber threats.

- In this guide, when I talk about endpoints, I mean systems, laptops, servers, and even smartphones. If it talks to the network and can be compromised by an attacker, endpoint security should apply to it.
- An endpoint can be considered as a device that enables an employee to connect to a corporate network. The growth in BYOD and other connected systems such as the Internet of Things (IoT) is seeing the number of devices that could potentially connect to a network increase exponentially.

![endpoint-intro](https://github.com/paulveillard/cybersecurity-endpoint-security/blob/main/img/img.jpg)

#### Some of the more common devices that can be considered an endpoint include:

- ATM machines
- IoT-enabled smart devices
- Industrial machines
- Laptop computers
- Medical devices
- Mobile phones
- Printers
- Servers
- Tablets
- Wearables, such as smartwatches

## `Why Is Endpoint Security Important?`

![endpoint-security-important](https://github.com/paulveillard/cybersecurity-endpoint-security/blob/main/img/endpoint-compliance.png)

## `Endpoint Protection vs. Antivirus: What Is the Difference?`

> Antivirus software helps businesses detect, eliminate, and prevent malware from infecting devices. Antivirus solutions are installed directly on endpoint devices, such as laptops, PCs, network servers, and mobile devices. These solutions detect malware by scanning files and directories to discover patterns that match the definitions and signatures of a virus. They can also only recognize known threats and must be updated to detect the latest malware strains.

> Endpoint security threat prevention is fundamentally different from the approach of antivirus software. Instead of protecting an individual device, endpoint security solutions protect the entire business network, including all of the endpoints connecting to it.

There are several significant differences between endpoint protection and antivirus software. These include:

|             Differences | Antivirus  | Endpoint |
| ----------------------: | ---------- | -------- |
|         Device Coverage | Javascript |
| Protection from threats | Javascript |
|   Continuous Protection | Python     |
|                       3 | SQL        |

## `Endpoint Security Solutions`

GRR, MIG, and osquery are endpoint-security solutions that allow investigators to inspect the systems of their infrastructure in real time.

## `How Does Endpoint Security Work?`

The **main goal of any endpoint security solution is to protect data and workflows associated with all devices that connect to the corporate network.** It does this by examining files as they enter the network and comparing them against an ever-increasing database of threat information, which is stored in the cloud.

![how-it-works](https://github.com/paulveillard/cybersecurity-endpoint-security/blob/main/img/how-endpoint-security-works.png)

The endpoint security solution provides system admins with a centralized management console that is installed on a network or server and enables them to control the security of all devices connecting to them. Client software is then deployed to each endpoint, either remotely or directly. With the endpoint set up, the software pushes updates to it whenever necessary, authenticates login attempts that are made from it, and administers corporate policies.

In addition, the endpoint security solution secures endpoints through application control. This blocks the user from downloading or accessing applications that are unsafe or unauthorized by the organization. It also uses encryption to prevent data loss.

The endpoint security solution enables businesses to quickly detect malware and other common security threats. It can also provide endpoint monitoring, detection and response, which enables the business to detect more advanced threats like fileless malware, polymorphic attacks, and zero-day attacks. This more advanced approach provides enhanced visibility and a wider variety of response options in the face of a security threat.

## `What Are the Components of Endpoint Security Software?`

![image](https://github.com/paulveillard/cybersecurity-endpoint-security/blob/main/img/edr-key.PNG)

## `What is The Difference between Endpoint Security and a Firewall? `

**A firewall is a network security solution that monitors incoming and outgoing traffic and decides whether to allow or deny access. Endpoint security protects the data on the device itself, enabling the business to monitor the activity and status of all its employees’ devices at all times.**

Traditionally, firewalls were ideal for businesses that had all employees working from the same building and signing into the same network. However, with people increasingly working remotely or from home, a firewall no longer suffices as traffic no longer goes through the central network, which leaves devices vulnerable.

This also boils down to businesses protecting networks or endpoints. Network security enables businesses to stop potential security threats at the network level by locking down open ports, restricting traffic, and employing intrusion detection and prevention services. Endpoint security helps businesses keep the devices that connect to a network secure. By making endpoints the new network perimeter, organizations can prevent risks and detect suspicious activity no matter where employees are.

Selecting the best security solution depends on every organization’s individual situation and security requirements. Important factors to build into this decision include:

**1) The number of employees:**

> Small businesses may find a product that requires managing devices on an individual basis works just fine. But as they get larger, it can become more difficult for IT and security teams to manage each device in this manner. Therefore, they will gain huge efficiency by deploying a security solution that centralizes endpoint control.

**2) Employee location:**

> Businesses that have employees working from one central location may not experience any issues with managing endpoint access. But those with a disparate workforce, employees working from home, remote offices, or on the go will need an endpoint security solution that secures endpoints no matter where or when employees attempt to connect to their networks and resources.

**3) Device ownership:**

> The rise of BYOD has blurred the lines of device ownership. Employees increasingly use their own devices to sign in and out of business networks and need to do so securely. An endpoint security solution enables businesses to secure employees every time they sign in to their networks and monitor access at all times.

**Data sensitivity:**

> Businesses that handle high-value intellectual property or sensitive data will find that antivirus software does not suffice in safeguarding their data, as it only protects it from viruses. To protect themselves from data loss incidents that pose a huge financial and reputational risk, these organizations need to deploy endpoint security solutions. Doing so will help them protect their most critical data, meet compliance requirements, and pass their audits.

## FAQs

#### What is an endpoint?

> An endpoint is any device that employees use to connect to business networks represents a potential risk that cyber criminals can exploit to steal corporate data.

#### What is endpoint security?

> Endpoint security is the process of protecting devices like desktops, laptops, mobile phones, and tablets from malicious threats and cyberattacks.

#### Why do we need endpoint security?

> Endpoint security technology plays a vital role in protecting organizations from the increasingly dangerous threat landscape.

#### Is endpoint security and antivirus the same?

> Antivirus software helps businesses detect, eliminate, and prevent malware from infecting devices. Antivirus solutions are installed directly on endpoint devices, such as laptops, PCs, network servers, and mobile devices. Endpoint security solutions protect the entire business network instead of protecting an individual device.

# Techniques

# Tools

Collection of tool you need to have in your EDR arsenal

- [The Hives Project](https://thehive-project.org/) - A scalable, open source and free Security Incident Response Platform, tightly integrated with MISP (Malware Information Sharing Platform), designed to make life easier for SOCs, CSIRTs, CERTs and any information security practitioner dealing with security incidents that need to be investigated and acted upon swiftly.
  - [TheHive](https://github.com/TheHive-Project/TheHive) - A Scalable, Open Source and Free Security Incident Response Platform
  - [Cortex](https://github.com/TheHive-Project/Cortex) - A Powerful Observable Analysis and Active Response Engine
  - [Hippocampe](https://github.com/TheHive-Project/Hippocampe) - Threat Feed Aggregation, Made Easy
- [Zeek](https://github.com/zeek/zeek) - Zeek is a powerful network analysis framework that is much different from the typical IDS you may know.
- [_Mozzila Mig [Depreciated]_](https://github.com/mozilla/mig) : Distributed & real time digital forensics at the speed of the cloud.
- [Osquery](https://osquery.io/) - Performant endpoint visibility.  
  **Tool to extend Osquery** :
  - [AitBnB StreamAlert](https://github.com/airbnb/streamalert) - StreamAlert is a serverless, realtime data analysis framework which empowers you to ingest, analyze, and alert on data from any environment, using datasources and alerting logic you define.
  - [Fleet](https://github.com/kolide/fleet) - A flexible control server for osquery fleets.
  - [Doorman](https://github.com/mwielgoszewski/doorman) - An osquery fleet manager.
  - [Palantir osquery-configuration](https://github.com/palantir/osquery-configuration) - A repository for using osquery for incident detection and response.
  - [Zentral](https://github.com/zentralopensource/zentral) - Zentral is an Event Hub to gather, process, and monitor system events and link them to an inventory.
  - [Osquery-attck](https://github.com/teoseller/osquery-attck) - Mapping the MITRE ATT&CK Matrix with Osquery.
  - [Osquery Launcher](https://github.com/kolide/launcher) - Osquery launcher, autoupdater, and packager.
  - [osquery-python](https://github.com/osquery/osquery-python) - Python bindings for osquery's Thrift API.
  - [osquery-go](https://github.com/kolide/osquery-go) - Go bindings for osquery.
- [Cuckoo](https://github.com/cuckoosandbox/cuckoo) - Cuckoo Sandbox is the leading open source automated malware analysis system (MISP)
- [Google GRR](https://github.com/google/grr) - GRR Rapid Response: remote live forensics for incident response.
- [Wazuh](https://github.com/wazuh/wazuh) - The Open Source Security Platform - Wazuh helps you to gain deeper security visibility into your infrastructure by monitoring hosts at an operating system and application level. [Wazuh GIT](https://github.com/wazuh) : Lot of ressources for wazuh main software.
- [MISP](https://github.com/MISP/MISP) - MISP (core software) - Open Source Threat Intelligence and Sharing Platform (formely known as Malware Information Sharing Platform)
- [OpenEDR - By Comodo](https://github.com/ComodoSecurity/openedr) : OpenEDR allows you to analyze what’s happening across your entire environment at base-security-event level.
- [Bluespawn](https://github.com/ION28/BLUESPAWN) : An Active Defense and EDR software to empower Blue Teams.
- [OSSEC](https://www.ossec.net/) : OSSEC has a powerful correlation and analysis engine, integrating log analysis, file integrity monitoring, Windows registry monitoring, centralized policy enforcement, rootkit detection, real-time alerting and active response.

special thanks to [Paul Veillard](https://github.com/paulveillard/).

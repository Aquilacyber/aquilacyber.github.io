# Introduction to threat modeling

Last reviewed: 2026-10-03

Threat modeling is a structured way to ask what could go wrong with a system, decide what matters most and plan what to do about it. You do it on paper or on a whiteboard, usually while the system is still being designed. Fixing a design flaw at this stage costs a conversation. Fixing it after launch can cost months.

## Why it matters

Most security tools find bugs in what has already been built. Threat modeling finds the weaknesses in the design itself, such as a feature that lets any user view any other user's data, which no scanner will catch because the code works exactly as written. It also gives a team a shared picture of what it is protecting and from whom.

## The four questions

A simple way to run it is to ask four questions, in this order:

1. **What are we working on?** Draw the system.
2. **What can go wrong?** List the threats.
3. **What are we going to do about it?** Choose a response for each one.
4. **Did we do a good enough job?** Review the result and check that the responses were carried out.

## Key ideas

- **Assets.** What you are protecting: data, accounts, money, availability, reputation.
- **Actors.** Who uses the system, and who might attack it: customers, staff, administrators, outsiders, insiders.
- **Trust boundaries.** Lines where the level of trust changes, such as between the internet and your server, or between your application and a third-party service. Threats cluster on these lines.
- **Data flow diagram (DFD).** A simple drawing of the system with five kinds of element: an external entity such as a user, a process, a data store, a data flow and a trust boundary.

### STRIDE

STRIDE is a list of six kinds of threat. For each element in your diagram, ask whether any of them apply.

| Letter | Threat | The property it breaks | Example |
|---|---|---|---|
| S | Spoofing | Authentication | Using someone else's stolen login |
| T | Tampering | Integrity | Changing the amount in a payment request |
| R | Repudiation | Accountability | A user denies making a transfer and there is no log to show otherwise |
| I | Information disclosure | Confidentiality | Reading another customer's statement by changing a number in the address |
| D | Denial of service | Availability | Flooding the login page until real users cannot sign in |
| E | Elevation of privilege | Authorisation | A customer calling an administrator function |

Other methods exist. Attack trees break one attacker goal into steps. LINDDUN is a method for privacy threats. PASTA starts from business objectives. STRIDE is the usual starting point.

### Choosing a response

For each threat you can prevent it, detect it, respond to it or accept it. Record the reason. Prioritise with a plain scale of high, medium and low and a sentence of explanation. Some teams use numeric schemes such as DREAD, but many practitioners avoid it because its scores are subjective.

## A worked example

A mobile app lets customers send money to other customers. The data flow has the app, an API server, a database and a third-party payment service. The trust boundaries sit between the phone and the API, and between the API and the payment service.

| Threat | STRIDE | Response |
|---|---|---|
| An attacker logs in with a stolen password | Spoofing | Multi-factor authentication, device binding, alerts on new devices |
| The amount or recipient is changed in the request | Tampering | Validate everything on the server, sign sensitive requests |
| A customer denies sending a payment | Repudiation | Audit log of every transaction with time, device and approval step |
| Changing an account number in the address shows someone else's statement | Information disclosure | Check on the server that the account belongs to the caller |
| Thousands of login attempts take the service down | Denial of service | Rate limits, lockouts and upstream protection |
| A customer account calls an administrator endpoint | Elevation of privilege | Role checks on every administrator function |

Notice that most of the responses are design decisions, not products.

## When to do it

- When you design a new system or feature
- When you add an integration with another service
- When something significant changes, such as moving to the cloud
- After an incident, to see which threats you missed

## What people in this field do

- An application security engineer runs sessions with developers and tracks the resulting fixes.
- A security architect models whole systems and sets the standards teams follow.
- A hardware or software security engineer models a product before it is built.
- A penetration tester uses a model to decide where to look first.

## Common tools

| Tool | What it does |
|---|---|
| A whiteboard or paper | Where most good threat models start |
| [diagrams.net](https://www.diagrams.net/) | Free drawing tool for data flow diagrams |
| [OWASP Threat Dragon](https://github.com/OWASP/threat-dragon) | Free tool for drawing diagrams and recording threats |
| [Microsoft Threat Modeling Tool](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool) | Free tool for Windows that generates STRIDE threats from a diagram |

## Try it

1. Draw a data flow diagram of a simple login system: a browser, a web server, a database and an email service for password resets. Mark the trust boundaries.
2. Walk STRIDE over each element and write down at least ten threats.
3. Choose a response for each and say who would do it.
4. Pick the three most serious threats and explain your reasoning in one sentence each.
5. Threat model a smart door lock, using the layers in the [IoT security introduction](iot-security.md).
6. Show your model to a friend or to the community and ask what you missed.

## Mistakes beginners make

- Drawing a diagram and never listing the threats
- Trying to find every threat instead of the important ones
- Modeling only outside attackers and forgetting insiders and mistakes
- Leaving out the data stores and third-party services
- Treating it as a one-off instead of updating it when the system changes
- Writing responses that nobody turns into tasks

## Where to go next

- The [application security track](../tracks/application-security.md), where it is one of the projects
- Roles: [Application Security Expert](../careers/application-security-expert.md), [Security Architect](../careers/security-architect.md), [Security Engineer (Software)](../careers/security-engineer-software.md), [Security Engineer (Hardware)](../careers/security-engineer-hardware.md)
- Lists of methods, books and tools: [reference: threat modeling](../reference/threat-modeling.md)
- Learn more: the [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/), the [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) and the book *Threat Modeling: Designing for Security* by Adam Shostack

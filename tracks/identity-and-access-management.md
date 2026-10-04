# Identity and access management track

Last reviewed: 2026-10-03

Identity and access management, shortened to IAM, decides who can get into which systems and what they can do once inside. It covers how accounts are created, how people prove who they are, what they are allowed to reach and how that access is reviewed and removed. Most serious breaches involve stolen or over-powered accounts, so this work is central to security.

This track suits people with a Windows administration, help desk or IT operations background, and anyone who likes process and detail.

## What the work looks like

An IAM analyst creates and removes accounts as people join and leave, handles access requests, runs access reviews, rolls out multi-factor authentication and fixes login problems. An IAM engineer designs and builds the systems behind it: single sign-on, directories and privileged access tools. Both spend time with HR, managers and application owners. The job depends as much on process as on technology.

## Skills to build

- Directory services: Active Directory and Microsoft Entra ID. Read the [Windows and Active Directory basics](../guides/windows-and-active-directory.md) guide first
- The identity lifecycle, called joiner, mover, leaver: grant access when someone joins, change it when they move, remove it when they leave
- Authentication: passwords, multi-factor authentication, and phishing-resistant methods such as passkeys and FIDO2 security keys
- Single sign-on and federation: SAML, OAuth 2.0 and OpenID Connect
- Authorisation models: role-based access control (RBAC) and attribute-based access control (ABAC)
- Least privilege and separation of duties
- Privileged access management: how to control, record and limit the use of administrator accounts
- Service accounts and secrets
- Access reviews, also called recertification

## Plan

### Weeks 1 to 4: directories and fundamentals

- Complete the [Windows and Active Directory basics](../guides/windows-and-active-directory.md) lab. Build a domain with users, groups and a password policy.
- Learn Microsoft Entra ID through [Microsoft Learn](https://learn.microsoft.com/en-us/training/).
- Read the NIST Digital Identity Guidelines, SP 800-63, at [csrc.nist.gov](https://csrc.nist.gov/), for how organisations should think about authentication.
- Read the OWASP cheat sheets on [authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) and [authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).

### Weeks 5 to 8: protocols and single sign-on

- Learn how [OAuth 2.0](https://oauth.net/2/) and [OpenID Connect](https://openid.net/developers/how-connect-works/) work. Draw the login flow by hand until you can explain each redirect.
- Run [Keycloak](https://github.com/keycloak/keycloak), an open source identity server, in a lab. Create a realm, users, groups and roles.
- Connect a small sample app to Keycloak with OpenID Connect and turn on multi-factor authentication.

### Weeks 9 to 12: governance

- Design the joiner, mover and leaver process for an invented company, on one page.
- Design a small set of roles that gives each department only what it needs.
- Learn how privileged access management works: vaulting passwords, session recording and just-in-time access.
- Read the identity events in Windows Security logs from the Windows guide and say which ones an analyst would alert on.

## Two projects

1. **A single sign-on lab.** With Keycloak, configure two sample applications with single sign-on, roles and multi-factor authentication. Document the setup and show a user logging in once and reaching both. Include a note on what you would change before using it in production.
2. **An access review.** Invent a company of about 30 staff and write their access list in a spreadsheet. Plant five problems, such as a leaver who still has access and a person who can both raise and approve payments. Run a review, find the problems and report how you would fix each one. Use the [risk register template](../templates/risk-register-template.md) to record the risks.

## Certifications worth considering

Microsoft's SC-300 Identity and Access Administrator is the common choice for the Microsoft stack. CompTIA Security+ and ISC2 CC cover the basics. Vendor courses from identity providers such as Okta and from privileged access vendors are useful once an employer uses them. See the [certifications guide](../guides/certifications.md).

## Where it leads

[Identity and Access Management Analyst](../careers/identity-and-access-management-analyst.md), [Security Architect](../careers/security-architect.md), [Cloud Security Engineer](../careers/cloud-security-engineer.md), [IT Auditor](../careers/it-auditor.md), [Information Security Analyst](../careers/information-security-analyst.md).

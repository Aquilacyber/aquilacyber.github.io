# Cloud security track

Last reviewed: 2026-10-03

Cloud security is the work of keeping systems safe in AWS, Azure or Google Cloud. Most cloud breaches come from misconfiguration, not from clever attacks, so much of the work is finding and fixing settings that are wrong.

This is a specialist track. It suits you most if you already have a head start: system administration, development or DevOps. If you do not, finish the [blue team track](blue-team.md) first and come back, because cloud security builds on the same logging and investigation skills.

## What the work looks like

A cloud security engineer reviews who has access to what, checks that logging is on, scans infrastructure code before it is deployed, watches for misconfigurations and risky changes, and helps developers fix what is found. When an incident happens in the cloud, they revoke access, isolate resources and preserve logs.

## Skills to build

- Identity and access management on one provider. This is the most important topic
- Cloud networking: virtual networks, security groups and private endpoints
- Logging: what each provider records and how to search it
- Infrastructure as code, with Terraform as the usual starting point
- Container basics and, later, Kubernetes security
- Reading a provider's shared responsibility model and knowing which half is yours

## Before you start: cost and accounts

Cloud providers charge for what you leave running. Set a budget alert on day one, use the free tier, and delete everything when you finish a session. A forgotten resource can generate a bill you cannot pay.

Most providers need a payment card that can pay in US dollars. If you do not have one, start with the options that need no account:

- [flaws.cloud](https://flaws.cloud/): AWS puzzles hosted by their author, no account needed.
- Some modules on [Microsoft Learn](https://learn.microsoft.com/en-us/training/) give you a temporary Azure environment without a card.
- [AWS Skill Builder](https://skillbuilder.aws/) has free learning content.

## Plan

### Weeks 1 to 4: one provider, properly

- Pick AWS or Azure. Learn one in depth and ignore the others for now.
- Study identity and access management until you can explain a policy line by line.
- Work through the provider's free foundation training.
- Turn on logging in your own account and find your own actions in the logs.

### Weeks 5 to 8: find misconfigurations

- Work through [flaws.cloud](https://flaws.cloud/).
- Read the cloud benchmarks from [CIS](https://www.cisecurity.org/cis-benchmarks) for your provider.
- Run [Prowler](https://github.com/prowler-cloud/prowler) or [ScoutSuite](https://github.com/nccgroup/ScoutSuite) against your own account only, and read every finding.
- Learn Terraform basics and scan your code with a tool such as Checkov before you deploy it.

### Weeks 9 to 12: detect and respond

- Learn the provider's threat detection and posture services: AWS GuardDuty and Security Hub, or Microsoft Defender for Cloud.
- Try [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) scenarios in your own account, then write down how you would detect each one.
- Learn container basics and scan an image with Trivy.
- Read the [cloud security reference page](../reference/cloud-security.md) for more tools.

## Two projects

1. **A secured baseline.** With Terraform, build a small environment that follows least privilege: separate roles, no public storage, logging turned on and encryption enabled. Scan it with Checkov and Prowler, fix what they find and document what you changed and why.
2. **A misconfiguration audit.** Take a deliberately weak setup, such as a CloudGoat scenario, and write an audit report using the [penetration test report template](../templates/pentest-report-template.md) as a base. List at least five issues, map each to a CIS benchmark control, rate the risk and give the fix.

## Certifications worth considering

See the cloud section of the [certifications guide](../guides/certifications.md). The provider foundation exam first, then the provider's security exam once you have used the platform.

## Where it leads

[Cloud Security Engineer](../careers/cloud-security-engineer.md), [DevSecOps Engineer](../careers/devsecops-engineer.md), [Security Engineer (Software)](../careers/security-engineer-software.md).

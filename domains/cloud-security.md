# Introduction to cloud security

Last reviewed: 2026-10-03

Cloud security is the work of keeping systems and data safe when they run on a provider's infrastructure, such as Amazon Web Services (AWS), Microsoft Azure or Google Cloud. The ideas are the same as elsewhere in security. What changes is where the controls are and who is responsible for each one.

## Why it matters

Organisations move systems to the cloud because it is quick and cheap to start. It is also quick to make a mistake. A single wrong setting can expose a database to the whole internet. Most cloud breaches come from misconfiguration and stolen credentials, not from clever attacks on the provider.

## Key ideas

- **Shared responsibility.** The provider secures the cloud itself: the buildings, hardware and core services. You secure what you put in it: your configuration, identities, data and code. Where the line sits depends on the type of service. With a virtual machine you manage more than with a fully managed database or a software service.
- **Identity is the control point.** In the cloud, access is decided by identity and access management (IAM): users, roles and policies. Least privilege and multi-factor authentication matter more here than anywhere.
- **Misconfiguration.** Public storage, open firewall rules, overly broad roles and logging that was never switched on.
- **Logging.** Every provider records activity. You have to turn it on, keep it and read it.
- **Data protection.** Encryption, key management and backups.
- **Infrastructure as code.** Defining resources in files, such as Terraform, lets you scan for problems before anything is built.
- **Containers.** Container images and Kubernetes clusters bring their own set of settings to get right.

The three big providers have close equivalents for most things:

| Need | AWS | Microsoft Azure | Google Cloud |
|---|---|---|---|
| Identity and access | IAM | Microsoft Entra ID and Azure RBAC | Cloud IAM |
| Activity logs | CloudTrail | Activity Log | Cloud Audit Logs |
| Threat detection | GuardDuty | Defender for Cloud | Security Command Center |
| Key management | KMS | Key Vault | Cloud KMS |
| Object storage | S3 | Blob Storage | Cloud Storage |

## Common problems

- Access keys committed to a public code repository
- Storage buckets open to the internet
- Roles with far more permission than the job needs, often `*` in a policy
- No multi-factor authentication on the most powerful account
- Logging turned off, so nobody can tell what happened
- Forgotten resources that keep running and keep costing money

## What people in this field do

- A cloud security engineer sets up and reviews identity, networking, logging and encryption, and scans infrastructure code.
- A DevSecOps engineer puts security checks into the build and deployment pipeline.
- A security architect designs how accounts, networks and services fit together securely.
- A SOC analyst or incident responder investigates cloud logs when something goes wrong.
- An auditor checks cloud settings against a benchmark or a standard.

## Common tools

| Tool | What it does |
|---|---|
| The provider's own security services | Threat detection, posture checks, key management |
| [Prowler](https://github.com/prowler-cloud/prowler) and [ScoutSuite](https://github.com/nccgroup/ScoutSuite) | Check an account against security best practice |
| Terraform and Checkov | Define infrastructure as code and scan it |
| Trivy | Scan container images for known vulnerabilities |
| [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) | Hardening settings for each provider |

## Try it in your lab

Cloud providers charge for what you leave running. Set a budget alert before you build anything, and delete everything when you finish. Most need a card that can pay in US dollars, so start with the options that need no account.

1. Work through [flaws.cloud](https://flaws.cloud/), which needs no account.
2. Read the provider's shared responsibility page, for example [AWS's](https://aws.amazon.com/compliance/shared-responsibility-model/), and write down in your own words what you are responsible for.
3. In a free account, enable multi-factor authentication on the root or owner account, create a user with read-only access and confirm it cannot change anything.
4. Turn on activity logging and find your own actions in it.
5. Run Prowler or ScoutSuite against your own account only, and read every finding.

## Mistakes beginners make

- Assuming the provider secures everything
- Using the most powerful account for everyday work
- Copying a sample policy that grants far too much
- Leaving resources running and getting a surprise bill

## Where to go next

- The [cloud security track](../tracks/cloud-security.md)
- Roles: [Cloud Security Engineer](../careers/cloud-security-engineer.md), [DevSecOps Engineer](../careers/devsecops-engineer.md), [Security Architect](../careers/security-architect.md)
- Starting points and tools: [reference: cloud security](../reference/cloud-security.md)
- Learn more: [Cloud Security Alliance](https://cloudsecurityalliance.org/), [Microsoft Learn](https://learn.microsoft.com/en-us/training/), [AWS Skill Builder](https://skillbuilder.aws/)

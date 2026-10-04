# Cloud Security Engineer

Last reviewed: 2026-10-03

[All roles](README.md)

## Summary

Secures an organisation's systems in AWS, Azure or Google Cloud. Controls who can do what through identity and access management, keeps storage and networks configured safely, makes sure logging is on, scans infrastructure code before it deploys, and helps respond when something goes wrong in the cloud. Most cloud breaches come from misconfiguration, such as a public storage bucket or an over-permissive role, so the job is mostly preventing and finding those.

Common entry routes are system administration, DevOps, software development or a cloud support role, with security added on top.

## Hard Skills

- One cloud platform in depth. Identity and access management comes first
- Cloud networking: virtual networks, security groups, private endpoints
- Logging and monitoring: AWS CloudTrail and GuardDuty, Azure Activity Log and Defender for Cloud, Google Cloud audit logs
- Infrastructure as code, such as Terraform, and scanning it before deployment with tools like Checkov
- Posture assessment tools. Examples are Prowler, ScoutSuite and the provider's own security services
- Containers and Kubernetes security basics, including image scanning with Trivy
- Encryption and key management services
- Responding to an incident in a cloud account: revoking keys, isolating resources and preserving logs

## Soft Skills

- Working with developers, who own the code and the infrastructure you are securing
- Explaining risk in terms of the business and not just the technology
- Cost awareness. A misconfigured lab or a forgotten resource can generate a large bill

## Education

No specific degree. Cloud provider certifications and hands-on projects carry weight.

## How to get there

1. Follow the [cloud security track](../tracks/cloud-security.md).
2. Build and secure a small environment with Terraform and publish it.
3. Learn one provider's security services well before looking at a second one.
4. Add a provider security certification once you have used the platform.

## Certifications

AWS Certified Security - Specialty, Microsoft's AZ-500 Azure Security Engineer Associate, and Google's Professional Cloud Security Engineer are the provider-specific options. CCSP is vendor-neutral and needs experience. Exam lines change, so check the current list. See the [certifications guide](../guides/certifications.md).

## Interview Questions

- A storage bucket is public. How do you find out whether anything sensitive is in it, and how do you fix it?
- Explain the difference between an identity-based and a resource-based policy.
- How would you give a developer access to production for one afternoon?
- What logs would you want turned on in a new cloud account, and why?
- How do you stop insecure infrastructure code from reaching production?

## Training Resources

- [flaws.cloud](https://flaws.cloud/) and [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat)
- [Prowler](https://github.com/prowler-cloud/prowler)
- The [cloud security reference page](../reference/cloud-security.md)

Related roles: [DevSecOps Engineer](devsecops-engineer.md), [Security Engineer (Software)](security-engineer-software.md), [Application Security Expert](application-security-expert.md).

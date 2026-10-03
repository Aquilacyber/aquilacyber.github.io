# Cloud security

Starting points for securing and testing cloud environments. This page was written by AquilaCyber. For a much longer list, see [awesome-cloud-security](https://github.com/4ndersonLin/awesome-cloud-security) by 4ndersonLin.

## Learn the basics

Learn one cloud provider well before you try to compare them. The security model is the same shape on all of them: identity and access management, networking, storage, logging and key management.

- [AWS Security](https://aws.amazon.com/security/)
- [Microsoft Azure security documentation](https://learn.microsoft.com/en-us/azure/security/)
- [Google Cloud security](https://cloud.google.com/security)
- [Cloud Security Alliance](https://cloudsecurityalliance.org/): publishes guidance and the Cloud Controls Matrix
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks): hardening guides for the major cloud platforms

## Practise

- [flaws.cloud](https://flaws.cloud/) and its sequel, flaws2.cloud: AWS misconfiguration puzzles hosted by their author.
- [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat): vulnerable AWS scenarios you deploy in your own account. Watch the costs and tear them down afterwards.
- [Pwned Labs](https://pwnedlabs.io/): hosted cloud security labs.
- [Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat): a deliberately vulnerable Kubernetes cluster to run yourself.

## Free tools

- [ScoutSuite](https://github.com/nccgroup/ScoutSuite): multi-cloud security auditing.
- [Prowler](https://github.com/prowler-cloud/prowler): security checks for AWS, Azure and Google Cloud.
- [Cloud Custodian](https://cloudcustodian.io/): a rules engine for policy and security in cloud accounts.
- [kube-bench](https://github.com/aquasecurity/kube-bench): checks a Kubernetes cluster against the CIS benchmark.

Run these only against accounts you own or have written permission to assess.

## Certifications

See the cloud section of the [certifications guide](../guides/certifications.md).

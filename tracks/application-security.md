# Application security track

Last reviewed: 2026-10-03

Application security, often shortened to AppSec, is the work of finding and preventing security flaws in software before and after it ships. This track is written for people who can already code or are learning to. If you build software, it is the shortest route into security, because you already know what developers need.

## What the work looks like

An application security engineer works with development teams. You review designs and code, run and tune scanning tools, help developers fix findings and set the rules that stop insecure code reaching production. Penetration testing is part of the work in some companies. The main skill is helping people write secure code. Finding flaws is not enough.

## Skills to build

- One programming language well, and the ability to read others
- The OWASP Top 10 and how each category appears in code and how it is fixed
- Authentication, session handling and access control, where most serious flaws live
- API security
- Threat modelling: looking at a design and asking what could go wrong
- Static analysis (SAST), dynamic testing (DAST) and software composition analysis (SCA) for third-party libraries
- Secrets scanning, so that keys and passwords stay out of repositories
- Secure code review
- Explaining a flaw to a developer in terms they can act on

## Plan

### Weeks 1 to 4: how code fails

- Work through the PortSwigger Web Security Academy topics for injection, authentication, access control and server-side request forgery. After each one, find the vulnerable pattern in your own language and write the fixed version.
- Read the [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) pages for authentication, session management, input validation and SQL injection prevention.
- Solve the web labs on the [AquilaCyber Defenders Portal](../guides/defenders-portal.md), then read how each flaw would look in code.

### Weeks 5 to 8: tools in a pipeline

- Run [Semgrep](https://github.com/semgrep/semgrep) on a project of your own and read every finding.
- Try [CodeQL](https://github.com/github/codeql) through GitHub code scanning on a public repository.
- Scan a running app with [OWASP ZAP](https://github.com/zaproxy/zaproxy) in your lab.
- Add dependency scanning, and secrets scanning with [Gitleaks](https://github.com/gitleaks/gitleaks).
- Put these checks into a GitHub Actions workflow so they run on every pull request.

### Weeks 9 to 12: design and review

- Read the [OWASP Application Security Verification Standard](https://github.com/OWASP/ASVS), a checklist of security requirements for web applications.
- Learn the STRIDE method for threat modelling and draw a data flow diagram with [OWASP Threat Dragon](https://github.com/OWASP/threat-dragon).
- Read the [OWASP API Security Top 10](https://owasp.org/API-Security/).
- Review the source of a small deliberately vulnerable app and write up what you find.

## Two projects

1. **Security checks in a pipeline.** Take a small web application of your own. Add a CI workflow that runs static analysis, a dependency scan and secrets scanning on every pull request. Fix what it finds, then write a README that says what each check catches, what it misses and how you tuned out false alarms.
2. **Threat model and code review.** Pick a small app, such as a to-do list with login. Draw its data flow diagram, list at least ten threats with STRIDE, then review the code and report which threats are really present. Use the [pen test report template](../templates/pentest-report-template.md) for the findings.

## Certifications worth considering

The Burp Suite Certified Practitioner from PortSwigger is a respected practical exam for web testing. ISC2's CSSLP covers the secure software lifecycle and suits people with development experience. See the [certifications guide](../guides/certifications.md).

## Where it leads

[Application Security Expert](../careers/application-security-expert.md), [DevSecOps Engineer](../careers/devsecops-engineer.md), [Source Code Auditor](../careers/source-code-auditor.md), [Security Engineer (Software)](../careers/security-engineer-software.md), [Security Architect](../careers/security-architect.md). If you enjoy breaking things more than fixing them, read the [red team track](red-team.md) too.

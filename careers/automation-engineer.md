# Automation Engineer

Last reviewed: 2026-10-03

[All roles](README.md)

## Summary

Builds the scripts, integrations and playbooks that remove repetitive work from a security team. When an alert fires, an automation might look up the IP address, check whether the user is travelling, open a ticket and message the on-call analyst, all before a person looks at it. The aim is to give analysts their time back for decisions that need a human.

You will see the title "security automation engineer". The work sits close to software development. Many people arrive from a SOC or IT background with strong scripting skills, or from software engineering with an interest in security.

## Hard Skills

- Python, and comfort reading and writing JSON
- REST APIs: authentication, requests, pagination and error handling
- SOAR platforms, which run automated response steps. Examples are Splunk SOAR, Cortex XSOAR, Tines and the open source Shuffle
- Integrating a SIEM, a ticketing system, email security, endpoint tools and threat intelligence sources
- Git and code review
- Basics of containers and CI pipelines, so that automations are tested and deployed in a controlled way
- Understanding of the incident response process, so you automate the right steps

## Soft Skills

- Spotting a task that is done by hand ten times a week
- Asking analysts what they actually do instead of guessing
- Writing documentation that someone else can use at 3 a.m.
- Caution. An automation that disables accounts by mistake does damage faster than a person could

## Education

No required degree. A portfolio of working automations counts for more. Software or IT backgrounds are common.

## How to get there

1. Learn Python well enough to call an API and process the result. See [phase 1](../roadmap/01-foundations.md).
2. Pick a repetitive task from the [blue team track](../tracks/blue-team.md), such as enriching a suspicious IP address, and automate it.
3. Try an open source SOAR such as Shuffle in your lab and build one full playbook.
4. Publish the code and a README that explains what the automation does and what it must never do without a human check.

## Certifications

Certifications matter less than working code. Some SOAR vendors offer their own training and exams. See the [certifications guide](../guides/certifications.md) for general options.

## Interview Questions

- Describe an automation you built. What did it save, and what could go wrong?
- How do you make sure an automated response does not lock out a legitimate user?
- How do you handle an API that rate-limits you or goes down?
- Which steps of an incident response process would you never fully automate, and why?
- How would you test a playbook before it touches production?

## Training Resources

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Shuffle](https://github.com/shuffle/shuffle), an open source SOAR
- [TheHive](https://github.com/TheHive-Project/TheHive) for case management

Related roles: [Detection Engineer](detection-engineer.md), [Workflow Engineer](workflow-engineer.md), [Security Operations Center (SOC) Analyst](security-operations-center.md).

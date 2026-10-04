# One-page CV

A CV for a first security role. It should fit on one page when printed. Put your projects first if you have no security experience. Delete the guidance lines in square brackets.

## Rules

- One page. Use a plain layout with no columns, no graphics and no skill bars. Applicant tracking systems read plain text best.
- Save as PDF. Name the file with your name, such as `Ada-Okafor-CV.pdf`.
- Put your portfolio link in the first three lines.
- For each project, say what you built or found, what you used and what the result was. Use numbers when you honestly have them.
- Leave out your date of birth, marital status and photo unless the employer asks. Do not include ID numbers or your home address. A city is enough.
- Be accurate. Interviewers will ask about everything on the page.
- Match the wording of the job advert where it is true of you.

## Template

```
[Full name]
[City, Nigeria] | [email] | [phone] | [GitHub or portfolio link] | [LinkedIn link]

[HEADLINE: one line saying what you are and what you want]
[Example: Self-taught security analyst with a home SIEM lab, looking for a SOC analyst role]

PROJECTS
[Project name], [month year]  |  [link to repository]
- [What you built or found, in one line, with the result]
- [The tools you used and what you learned from it]

[Project name], [month year]  |  [link to repository]
- [One line]
- [One line]

[Project name], [month year]  |  [link to repository]
- [One line]

SKILLS
Security:    [for example log analysis, vulnerability scanning, threat modelling, risk assessment]
Tools:       [for example Wireshark, Nmap, Wazuh, Burp Suite, Terraform]
Systems:     [for example Linux, Windows, Active Directory, AWS]
Languages:   [for example Python, Bash, SQL]

EXPERIENCE
[Job title], [Organisation], [month year] to [month year]
- [What you did that relates to security, support or operations, with a result]
- [One more line]

[Volunteer or community work counts. Include it if it shows skill or reliability.]

EDUCATION
[Degree or course], [Institution], [year or expected year]

CERTIFICATIONS
[Certification name, issuer, year]  [Only list ones you hold. Write "in progress" with a date if you are studying.]

COMMUNITY
[For example: member of AquilaCyber since 2025, helped answer questions from new learners, solved N challenges on the Defenders Portal]
```

## A worked project line

Weak:

```
Built a home lab and learned about SIEM.
```

Better:

```
Detection lab, March 2026 | github.com/example/detection-lab
- Built a Wazuh SIEM with Sysmon on two Windows VMs and wrote 6 detection rules for brute force logins and suspicious PowerShell
- Tested each rule against simulated attacks and cut false positives by tuning the rule thresholds
```

## Before you send it

- [ ] It fits on one page
- [ ] Every link works and goes where it says
- [ ] Every line is true and I can talk about it for two minutes
- [ ] I read it aloud and fixed anything awkward
- [ ] A friend who is not in security read it and understood what I did
- [ ] I changed the headline and top skills to match this job

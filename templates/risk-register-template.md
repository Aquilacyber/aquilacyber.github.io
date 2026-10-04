# Risk register

A risk register is a table of what could go wrong, how bad it would be, how likely it is and what you will do about it. Use the [CSV file](risk-register-template.csv) to work in a spreadsheet, and this page for the scoring rules and the worked examples.

## How to use it

1. List the assets that matter: systems, data, people and processes.
2. For each asset, list what could go wrong. Write each risk as a threat plus a weakness, such as "an attacker uses a weak admin password to read customer data".
3. Record the controls that already exist.
4. Score likelihood and impact using the tables below. Multiply them.
5. Choose a treatment, name an owner and set a date.
6. After the planned controls are in place, score the risk again as the residual risk.
7. Review the register on a fixed schedule. A register nobody updates is worse than none.

## Likelihood scale

| Score | Label | Meaning |
|---|---|---|
| 1 | Rare | Not expected in the next three years |
| 2 | Unlikely | Could happen once in two to three years |
| 3 | Possible | Could happen once a year |
| 4 | Likely | Expected several times a year |
| 5 | Almost certain | Happening now or expected most months |

## Impact scale

Adapt the descriptions to your organisation. Use money figures that make sense for its size.

| Score | Label | Meaning |
|---|---|---|
| 1 | Negligible | No customer effect, a few hours of staff time |
| 2 | Minor | Short disruption, small cost, no regulatory interest |
| 3 | Moderate | A day of disruption or a limited number of customers affected, some regulatory interest |
| 4 | Major | Several days of disruption, many customers affected, a regulator is likely to act |
| 5 | Severe | Business-threatening loss, large data breach, licence or legal action |

## Score and level

Score = likelihood multiplied by impact.

| Score | Level | Expected response |
|---|---|---|
| 1 to 4 | Low | Accept or monitor |
| 5 to 9 | Medium | Plan a fix in the normal cycle |
| 10 to 16 | High | Fix with a firm date and an owner |
| 20 to 25 | Critical | Act now and report to senior management |

## Treatment options

- **Mitigate.** Add controls to reduce likelihood or impact.
- **Transfer.** Share the risk, for example through insurance or a contract. The risk is reduced, not removed.
- **Accept.** Decide to live with it. A named senior person must approve and give a review date.
- **Avoid.** Stop the activity that creates the risk.

## Columns

| Column | What to write |
|---|---|
| ID | A short unique code such as R-01 |
| Asset | What is at risk |
| Threat | What could cause harm |
| Vulnerability | The weakness the threat would use |
| Existing controls | What already reduces the risk |
| Likelihood, Impact, Score, Level | From the tables above |
| Treatment | Mitigate, transfer, accept or avoid |
| Planned controls | What you will add |
| Owner | One named person, not a team |
| Due date | When the treatment will be finished |
| Status | Open, in progress, closed or accepted |
| Residual likelihood, impact, score, level | Scored after the planned controls |

## Worked examples

These come from an invented company called Example Pay Ltd. Replace them with your own.

| ID | Asset | Threat | Vulnerability | Existing controls | L | I | Score | Level | Treatment | Planned controls | Owner | Due | Residual |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-01 | Customer database | Attacker reads customer records through SQL injection | Legacy admin page builds queries by string concatenation | Web application firewall in monitor mode only | 4 | 5 | 20 | Critical | Mitigate | Fix the queries, switch the firewall to blocking, commission a penetration test | Head of Engineering | 2026-12-15 | L2 x I4 = 8, Medium |
| R-02 | Staff email accounts | Phishing leads to account takeover | No multi-factor authentication for part of the staff | Annual awareness training | 4 | 4 | 16 | High | Mitigate | Enforce MFA for everyone, run quarterly phishing tests | Head of IT | 2026-11-30 | L2 x I4 = 8, Medium |
| R-03 | Legacy reporting server | Attacker exploits an unpatched flaw | Vendor no longer supports the software | Server is on an isolated network, access limited to three staff | 2 | 3 | 6 | Medium | Accept | Review when the replacement project finishes | Chief Information Security Officer, who approved the acceptance | 2027-03-31 | Not applicable while accepted |

## Tips

- Be specific. "Hackers" is not a threat. "An attacker using stolen staff credentials" is.
- Do not score everything as high. A register where everything is critical shows nothing.
- Your numbers are judgements. Write down why you chose each score so someone can challenge it.
- Link each risk to a control from a framework where you can. See [frameworks and standards](../guides/frameworks-and-standards.md).

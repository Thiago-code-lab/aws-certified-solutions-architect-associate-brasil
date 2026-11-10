# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| RPO is not restoration speed | No. The recoverable data points must satisfy the 15-minute loss window; restore speed addresses RTO. | RPO describes acceptable data loss in time. The recovery data path needs sufficiently current valid recovery points; fast infrastructure restoration does not make old backups newer. |
| Regional disaster scope | No. A regional recovery design needs usable recovery resources and data outside the affected Region, plus tested recovery procedures. | Multi-AZ deployment addresses AZ-level failures within a Region. Regional recovery needs an appropriately independent recovery location and tested data, configuration, and traffic recovery. |
| Pilot light versus warm standby | Warm standby. | Warm standby maintains a scaled-down functioning workload. Pilot light keeps a smaller core running and requires additional activation or deployment before the full workload can serve. |
| Measure recovery | Restore representative data in an isolated environment, validate the application, measure data loss and recovery duration, and compare them with RPO and RTO. | Recovery testing checks that data, dependencies, permissions, and procedures actually work together. A successful backup is necessary evidence for that copy, but not proof of end-to-end recovery. |
| Availability and corruption recovery | Retained backups or an appropriate point-in-time recovery capability, with tested restoration procedures. | Replication can reproduce logical mistakes as well as correct writes. Availability replicas do not replace retained recoverable history for corruption or accidental deletion. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **RPO is not restoration speed:** Short recovery duration does not change the age of the recovered data.
- **Regional disaster scope:** AZs are isolated locations within a Region, not separate Regions.
- **Pilot light versus warm standby:** The stem explicitly says a fully functional application is already running.
- **Measure recovery:** Backup completion does not validate all restoration and application dependencies.
- **Availability and corruption recovery:** A standby can receive the same deletion and is not an independent historical backup.

## AWS References

[Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

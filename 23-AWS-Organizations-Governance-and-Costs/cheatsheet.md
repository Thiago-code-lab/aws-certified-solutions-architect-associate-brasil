# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Organization permission ceiling | It is denied, unless the principal or action is within a documented SCP exemption. | An applicable SCP deny limits permissions in member accounts, including administrator roles. Management-account principals and some other entities have documented exceptions, which must not be generalized away. |
| Budget is not an instantaneous cap | No. Budget data and notifications are delayed; explicit controls, suitable actions, limits, and cleanup are still needed. | Budgets track costs and usage and can support configured actions. They are not a universal instantaneous hard spending cap; already-running resources and delayed cost data require careful operational controls. |
| Commit only a measured baseline | Right-size from measured usage and evaluate an appropriate Savings Plan commitment for the stable baseline, leaving variable usage to suitable flexible capacity. | A commitment should match expected eligible usage and tolerance for underutilization. Bursts and interruption-sensitive work need a separate capacity and pricing decision. |
| Analyze spending | AWS Cost Explorer with appropriate filters and grouping. | Cost Explorer supports cost and usage analysis. Reliable allocation may require activated cost allocation tags or other account structure; analysis does not automatically implement every optimization. |
| SCP management-account exception | SCPs do not restrict users or roles in the management account; protect that account with appropriate IAM controls and limited use. | AWS documents that SCPs do not affect management-account users or roles. Keep workloads and routine operations appropriately separated from highly privileged organization administration. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Organization permission ceiling:** An identity allow does not override an applicable explicit deny.
- **Budget is not an instantaneous cap:** Notifications alone do not implement universal resource termination.
- **Commit only a measured baseline:** Unmeasured peak commitments risk paying for unused commitment.
- **Analyze spending:** A DLQ stores failed messages rather than cost trends.
- **SCP management-account exception:** This ignores the documented management-account exception.

## AWS References

[Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html), [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html), [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html), [EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html), [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

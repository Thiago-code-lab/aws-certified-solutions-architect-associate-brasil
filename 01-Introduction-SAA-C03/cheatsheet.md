# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Official domain weights | Security 30%, Resilience 26%, Performance 24%, Cost Optimization 20%. | The exam guide assigns these four weights to scored content. A community practice set need not have the same distribution. |
| Shared responsibility for EC2 | The customer operating the EC2 instances. | For EC2, AWS manages the underlying infrastructure; the customer manages the guest OS, applications, and their configuration. Automation can help the customer perform that responsibility. |
| Availability is not backup | Retain previous object versions and test how to restore the required version. | S3 Versioning retains earlier versions so an overwrite can be reversed. Redundant compute and DNS do not retain earlier application data. |
| Interpreting recovery objectives | RPO of 15 minutes and RTO of 2 hours. | RPO limits acceptable data loss measured in time; RTO limits acceptable recovery time. Managed services do not remove the need to define or test those objectives. |
| Requirements before cost preference | Attach an appropriately scoped IAM role to the instance through an instance profile. | An EC2 workload can obtain temporary credentials from its IAM role. Permissions should cover only the application actions and resources it needs. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Official domain weights:** These were the incorrect weights inherited from the source edition.
- **Shared responsibility for EC2:** EC2 does not transfer all guest OS maintenance to AWS.
- **Availability is not backup:** Compute redundancy alone does not preserve historical object contents.
- **Interpreting recovery objectives:** This reverses the meanings of RPO and RTO.
- **Requirements before cost preference:** A baked-in administrator key is long-lived and excessively privileged.

## AWS References

[SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html), [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

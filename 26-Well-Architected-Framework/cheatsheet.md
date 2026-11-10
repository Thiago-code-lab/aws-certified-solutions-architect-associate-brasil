# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Six Well-Architected pillars | Operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability. | The framework has six pillars. The four SAA-C03 scored-content domains are a different grouping and must not be mistaken for the complete framework. |
| Review tool versus automatic remediation | It records review findings and improvement opportunities; implementing and validating improvements remains the team responsibility. | The tool supports structured workload assessment and improvement planning. Review completion is not proof that every recommended change was implemented or tested. |
| Measured cost trade-offs | No. Cost optimization must still satisfy retention and recovery requirements. | The pillars must be considered together. Lower cost is not an improvement when it violates a mandatory data-protection or recovery constraint. |
| Operational excellence evidence | Exercise the runbook in an isolated recovery test, measure results, and update it from observed failures. | A tested procedure exposes missing dependencies, permissions, and timing assumptions. Runbooks and observability support learning and repeatable operations. |
| Security remains a design responsibility | AWS manages more infrastructure, but the team must still design appropriate access, data protection, configuration, and application behavior. | The responsibility boundary depends on the service. Managed infrastructure does not remove customer responsibility for data use, permissions, and workload configuration. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Six Well-Architected pillars:** This omits operational excellence and sustainability and confuses framework pillars with exam domains.
- **Review tool versus automatic remediation:** A review record is not universal automatic remediation.
- **Measured cost trade-offs:** Price alone is not sufficient when requirements are unmet.
- **Operational excellence evidence:** Documentation alone does not validate execution.
- **Security remains a design responsibility:** Managed services do not eliminate the customer side of the responsibility model.

## AWS References

[Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html), [AWS Well-Architected Tool workload review](https://docs.aws.amazon.com/wellarchitected/latest/userguide/tutorial.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

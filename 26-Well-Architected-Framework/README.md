# Well-Architected Framework

## Overview

Review workloads across all six Well-Architected pillars. Assess trade-offs, record assumptions, assign improvement owners, and test that changes actually meet business requirements.

## Key Concepts

- **Six Well-Architected pillars:** The framework has six pillars. The four SAA-C03 scored-content domains are a different grouping and must not be mistaken for the complete framework.
- **Review tool versus automatic remediation:** The tool supports structured workload assessment and improvement planning. Review completion is not proof that every recommended change was implemented or tested.
- **Measured cost trade-offs:** The pillars must be considered together. Lower cost is not an improvement when it violates a mandatory data-protection or recovery constraint.
- **Operational excellence evidence:** A tested procedure exposes missing dependencies, permissions, and timing assumptions. Runbooks and observability support learning and repeatable operations.
- **Security remains a design responsibility:** The responsibility boundary depends on the service. Managed infrastructure does not remove customer responsibility for data use, permissions, and workload configuration.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Six Well-Architected pillars:** Operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.
2. **Review tool versus automatic remediation:** It records review findings and improvement opportunities; implementing and validating improvements remains the team responsibility.
3. **Measured cost trade-offs:** No. Cost optimization must still satisfy retention and recovery requirements.
4. **Operational excellence evidence:** Exercise the runbook in an isolated recovery test, measure results, and update it from observed failures.
5. **Security remains a design responsibility:** AWS manages more infrastructure, but the team must still design appropriate access, data protection, configuration, and application behavior.

## Common Pitfalls

- This omits operational excellence and sustainability and confuses framework pillars with exam domains.
- A review record is not universal automatic remediation.
- Price alone is not sufficient when requirements are unmet.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html), [AWS Well-Architected Tool workload review](https://docs.aws.amazon.com/wellarchitected/latest/userguide/tutorial.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

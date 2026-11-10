# AWS Organizations Governance and Costs

## Overview

Use organization guardrails, account boundaries, cost visibility, and measured commitments together. SCPs do not grant permissions, and a budget notification is not a universal instantaneous spending cap.

## Key Concepts

- **Organization permission ceiling:** An applicable SCP deny limits permissions in member accounts, including administrator roles. Management-account principals and some other entities have documented exceptions, which must not be generalized away.
- **Budget is not an instantaneous cap:** Budgets track costs and usage and can support configured actions. They are not a universal instantaneous hard spending cap; already-running resources and delayed cost data require careful operational controls.
- **Commit only a measured baseline:** A commitment should match expected eligible usage and tolerance for underutilization. Bursts and interruption-sensitive work need a separate capacity and pricing decision.
- **Analyze spending:** Cost Explorer supports cost and usage analysis. Reliable allocation may require activated cost allocation tags or other account structure; analysis does not automatically implement every optimization.
- **SCP management-account exception:** AWS documents that SCPs do not affect management-account users or roles. Keep workloads and routine operations appropriately separated from highly privileged organization administration.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Organization permission ceiling:** It is denied, unless the principal or action is within a documented SCP exemption.
2. **Budget is not an instantaneous cap:** No. Budget data and notifications are delayed; explicit controls, suitable actions, limits, and cleanup are still needed.
3. **Commit only a measured baseline:** Right-size from measured usage and evaluate an appropriate Savings Plan commitment for the stable baseline, leaving variable usage to suitable flexible capacity.
4. **Analyze spending:** AWS Cost Explorer with appropriate filters and grouping.
5. **SCP management-account exception:** SCPs do not restrict users or roles in the management account; protect that account with appropriate IAM controls and limited use.

## Common Pitfalls

- An identity allow does not override an applicable explicit deny.
- Notifications alone do not implement universal resource termination.
- Unmeasured peak commitments risk paying for unused commitment.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html), [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html), [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html), [EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html), [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

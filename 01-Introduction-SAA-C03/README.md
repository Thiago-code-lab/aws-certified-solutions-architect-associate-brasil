# Introduction to SAA-C03

## Overview

Plan SAA-C03 preparation around the official domains, explicit business requirements, shared responsibility, and measurable recovery objectives. A practice score is a learning signal, not a pass guarantee.

## Key Concepts

- **Official domain weights:** The exam guide assigns these four weights to scored content. A community practice set need not have the same distribution.
- **Shared responsibility for EC2:** For EC2, AWS manages the underlying infrastructure; the customer manages the guest OS, applications, and their configuration. Automation can help the customer perform that responsibility.
- **Availability is not backup:** S3 Versioning retains earlier versions so an overwrite can be reversed. Redundant compute and DNS do not retain earlier application data.
- **Interpreting recovery objectives:** RPO limits acceptable data loss measured in time; RTO limits acceptable recovery time. Managed services do not remove the need to define or test those objectives.
- **Requirements before cost preference:** An EC2 workload can obtain temporary credentials from its IAM role. Permissions should cover only the application actions and resources it needs.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Official domain weights:** Security 30%, Resilience 26%, Performance 24%, Cost Optimization 20%.
2. **Shared responsibility for EC2:** The customer operating the EC2 instances.
3. **Availability is not backup:** Retain previous object versions and test how to restore the required version.
4. **Interpreting recovery objectives:** RPO of 15 minutes and RTO of 2 hours.
5. **Requirements before cost preference:** Attach an appropriately scoped IAM role to the instance through an instance profile.

## Common Pitfalls

- These were the incorrect weights inherited from the source edition.
- EC2 does not transfer all guest OS maintenance to AWS.
- Compute redundancy alone does not preserve historical object contents.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html), [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

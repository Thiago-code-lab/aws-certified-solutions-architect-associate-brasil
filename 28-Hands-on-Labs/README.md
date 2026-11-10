# Hands-on Labs

## Overview

Run bounded exercises with dedicated test data, scoped access, an explicit cost estimate, observable outcomes, and a verified cleanup plan. No lab in this repository is a promise of zero charges.

## Key Concepts

- **Lab cost planning:** Short runtime does not imply zero cost. Pricing, plan eligibility, retained resources, and delayed cost reporting must all be considered before deployment.
- **Bounded failure testing:** A bounded recovery experiment needs an explicit hypothesis, recoverable data, observability, and a safe environment. The test result should be compared with its recovery objective.
- **Recover versioned lab objects:** Versioning retains earlier object versions, which can be retrieved or used to restore desired contents. Recovery still depends on retaining the needed version and permissions.
- **Authorize only lab access:** A scoped role limits the blast radius and avoids distributing long-lived credentials. Test data and resource boundaries should be separated from production.
- **Versioned bucket cleanup:** A simple delete in a versioned bucket can add a delete marker while earlier versions remain. Cleanup must account for versions and any retention restrictions without deleting unrelated data.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Lab cost planning:** Estimate the specific regional resources and usage, check the account applicable credits or Free Tier eligibility, set cost notifications, and plan cleanup.
2. **Bounded failure testing:** Use isolated lab resources with non-sensitive test data, define the expected failure and rollback, and verify recovery without touching production.
3. **Recover versioned lab objects:** Retrieve the earlier version and, if needed, copy it to become the current version of the key.
4. **Authorize only lab access:** Use a dedicated workload role scoped to the required actions and object resources.
5. **Versioned bucket cleanup:** Review noncurrent versions and delete markers, along with other retained lab resources, and remove only approved test data.

## Common Pitfalls

- Many resources incur charges during short sessions.
- An uncontrolled production interruption is not an isolated learning experiment.
- The premise says an earlier retained version exists.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[AWS Pricing Calculator](https://calculator.aws/), [AWS Free Tier account eligibility](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html), [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

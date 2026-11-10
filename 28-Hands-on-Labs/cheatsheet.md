# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Lab cost planning | Estimate the specific regional resources and usage, check the account applicable credits or Free Tier eligibility, set cost notifications, and plan cleanup. | Short runtime does not imply zero cost. Pricing, plan eligibility, retained resources, and delayed cost reporting must all be considered before deployment. |
| Bounded failure testing | Use isolated lab resources with non-sensitive test data, define the expected failure and rollback, and verify recovery without touching production. | A bounded recovery experiment needs an explicit hypothesis, recoverable data, observability, and a safe environment. The test result should be compared with its recovery objective. |
| Recover versioned lab objects | Retrieve the earlier version and, if needed, copy it to become the current version of the key. | Versioning retains earlier object versions, which can be retrieved or used to restore desired contents. Recovery still depends on retaining the needed version and permissions. |
| Authorize only lab access | Use a dedicated workload role scoped to the required actions and object resources. | A scoped role limits the blast radius and avoids distributing long-lived credentials. Test data and resource boundaries should be separated from production. |
| Versioned bucket cleanup | Review noncurrent versions and delete markers, along with other retained lab resources, and remove only approved test data. | A simple delete in a versioned bucket can add a delete marker while earlier versions remain. Cleanup must account for versions and any retention restrictions without deleting unrelated data. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Lab cost planning:** Many resources incur charges during short sessions.
- **Bounded failure testing:** An uncontrolled production interruption is not an isolated learning experiment.
- **Recover versioned lab objects:** The premise says an earlier retained version exists.
- **Authorize only lab access:** Root credentials are not appropriate reusable lab credentials.
- **Versioned bucket cleanup:** Delete markers hide an object as current but do not erase all prior versions.

## AWS References

[AWS Pricing Calculator](https://calculator.aws/), [AWS Free Tier account eligibility](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html), [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

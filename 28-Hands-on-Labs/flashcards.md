# Review Flashcards

## Card 01

**Question:** Before creating a NAT gateway and database for a short lab, which cost practice is appropriate?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Estimate the specific regional resources and usage, check the account applicable credits or Free Tier eligibility, set cost notifications, and plan cleanup. Short runtime does not imply zero cost. Pricing, plan eligibility, retained resources, and delayed cost reporting must all be considered before deployment.

**AWS references:** [AWS Pricing Calculator](https://calculator.aws/), [AWS Free Tier account eligibility](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html), [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).

</details>

## Card 02

**Question:** A learner wants to test recovery behavior. Which approach keeps the experiment appropriately scoped?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Use isolated lab resources with non-sensitive test data, define the expected failure and rollback, and verify recovery without touching production. A bounded recovery experiment needs an explicit hypothesis, recoverable data, observability, and a safe environment. The test result should be compared with its recovery objective.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

</details>

## Card 03

**Question:** A learner overwrote an object in a versioning-enabled S3 test bucket. The earlier version was not permanently deleted. Which recovery action fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Retrieve the earlier version and, if needed, copy it to become the current version of the key. Versioning retains earlier object versions, which can be retrieved or used to restore desired contents. Recovery still depends on retaining the needed version and permissions.

**AWS references:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html).

</details>

## Card 04

**Question:** A lab requires read-only access to one test object prefix. Which permission approach fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Use a dedicated workload role scoped to the required actions and object resources. A scoped role limits the blast radius and avoids distributing long-lived credentials. Test data and resource boundaries should be separated from production.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

## Card 05

**Question:** A learner empties only current objects from a versioning-enabled lab bucket. What additional cleanup check is needed before assuming the bucket has no retained billable data?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Review noncurrent versions and delete markers, along with other retained lab resources, and remove only approved test data. A simple delete in a versioned bucket can add a delete marker while earlier versions remain. Cleanup must account for versions and any retention restrictions without deleting unrelated data.

**AWS references:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html).

</details>

## Card 06

**Question:** A learner wants to test recovery behavior. Which approach keeps the experiment appropriately scoped?

Why does this alternative fail: “Interrupt a production database without a test scope or recovery plan.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** An uncontrolled production interruption is not an isolated learning experiment.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

</details>

## Card 07

**Question:** A learner overwrote an object in a versioning-enabled S3 test bucket. The earlier version was not permanently deleted. Which recovery action fits?

Why does this alternative fail: “Assume the object is irrecoverable solely because its key was overwritten.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The premise says an earlier retained version exists.

**AWS references:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html).

</details>

## Card 08

**Question:** A lab requires read-only access to one test object prefix. Which permission approach fits?

Why does this alternative fail: “Reuse a production root access key.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Root credentials are not appropriate reusable lab credentials.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 28-Q01 -->

Before creating a NAT gateway and database for a short lab, which cost practice is appropriate?

A) Assume any resource used for fewer than a few hours is free.

B) Estimate the specific regional resources and usage, check the account applicable credits or Free Tier eligibility, set cost notifications, and plan cleanup.

C) Treat an AWS Budgets email threshold as an instantaneous spending cap.

D) Ignore retained storage because deleting compute always removes all charges.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Short runtime does not imply zero cost. Pricing, plan eligibility, retained resources, and delayed cost reporting must all be considered before deployment.

**Why the other options are incorrect:**

- **A:** Many resources incur charges during short sessions.
- **C:** Budget notifications do not guarantee instantaneous cost enforcement.
- **D:** Storage, snapshots, endpoints, and other retained resources may continue to incur charges.

**AWS references:** [AWS Pricing Calculator](https://calculator.aws/), [AWS Free Tier account eligibility](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html), [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).

</details>

## Question 2

<!-- question-id: 28-Q02 -->

A learner wants to test recovery behavior. Which approach keeps the experiment appropriately scoped?

A) Interrupt a production database without a test scope or recovery plan.

B) Delete every backup before testing restoration.

C) Disable every alarm so the experiment produces no evidence.

D) Use isolated lab resources with non-sensitive test data, define the expected failure and rollback, and verify recovery without touching production.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** A bounded recovery experiment needs an explicit hypothesis, recoverable data, observability, and a safe environment. The test result should be compared with its recovery objective.

**Why the other options are incorrect:**

- **A:** An uncontrolled production interruption is not an isolated learning experiment.
- **B:** Removing recovery copies undermines a restoration test.
- **C:** Disabling evidence collection prevents useful behavioral validation.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

</details>

## Question 3

<!-- question-id: 28-Q03 -->

A learner overwrote an object in a versioning-enabled S3 test bucket. The earlier version was not permanently deleted. Which recovery action fits?

A) Retrieve the earlier version and, if needed, copy it to become the current version of the key.

B) Assume the object is irrecoverable solely because its key was overwritten.

C) Make the bucket public to restore the earlier bytes.

D) Increase the uploader EC2 CPU.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Versioning retains earlier object versions, which can be retrieved or used to restore desired contents. Recovery still depends on retaining the needed version and permissions.

**Why the other options are incorrect:**

- **B:** The premise says an earlier retained version exists.
- **C:** Public exposure is unnecessary and does not perform version restoration.
- **D:** Uploader compute performance cannot restore stored version history.

**AWS references:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html).

</details>

## Question 4

<!-- question-id: 28-Q04 -->

A lab requires read-only access to one test object prefix. Which permission approach fits?

A) Reuse a production root access key.

B) Grant AdministratorAccess to every lab participant.

C) Use a dedicated workload role scoped to the required actions and object resources.

D) Commit a long-lived access key with the lab notes.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** A scoped role limits the blast radius and avoids distributing long-lived credentials. Test data and resource boundaries should be separated from production.

**Why the other options are incorrect:**

- **A:** Root credentials are not appropriate reusable lab credentials.
- **B:** Administrator access is unnecessary for a narrow object-read exercise.
- **D:** Credentials must not be published in repository content.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

## Question 5

<!-- question-id: 28-Q05 -->

A learner empties only current objects from a versioning-enabled lab bucket. What additional cleanup check is needed before assuming the bucket has no retained billable data?

A) Assume a delete marker permanently erases every older version.

B) Assume disabling a budget deletes the bucket contents.

C) Assume versioning makes all stored versions free.

D) Review noncurrent versions and delete markers, along with other retained lab resources, and remove only approved test data.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** A simple delete in a versioned bucket can add a delete marker while earlier versions remain. Cleanup must account for versions and any retention restrictions without deleting unrelated data.

**Why the other options are incorrect:**

- **A:** Delete markers hide an object as current but do not erase all prior versions.
- **B:** Budget configuration does not delete storage objects.
- **C:** Stored versions are subject to normal S3 storage charges.

**AWS references:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

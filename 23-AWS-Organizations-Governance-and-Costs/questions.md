# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 23-Q01 -->

An SCP explicitly denies a service action in a member account. An IAM role there has AdministratorAccess. What happens to a request covered by the SCP deny?

A) AdministratorAccess automatically overrides every SCP deny.

B) It is denied, unless the principal or action is within a documented SCP exemption.

C) SCPs only affect the organization management account.

D) The organization account with the lowest bill decides the result.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** An applicable SCP deny limits permissions in member accounts, including administrator roles. Management-account principals and some other entities have documented exceptions, which must not be generalized away.

**Why the other options are incorrect:**

- **A:** An identity allow does not override an applicable explicit deny.
- **C:** SCPs do not restrict management-account users and roles in this way; they target member accounts.
- **D:** Billing amount is not part of IAM policy evaluation.

**AWS references:** [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

</details>

## Question 2

<!-- question-id: 23-Q02 -->

A lab account has an AWS Budgets notification at a chosen spend threshold. Does this guarantee that all charges stop exactly at that amount?

A) Yes. Every budget automatically terminates every billable resource instantly.

B) Yes. A budget notification is a legal maximum bill.

C) Yes. It makes every AWS service free until the next month.

D) No. Budget data and notifications are delayed; explicit controls, suitable actions, limits, and cleanup are still needed.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Budgets track costs and usage and can support configured actions. They are not a universal instantaneous hard spending cap; already-running resources and delayed cost data require careful operational controls.

**Why the other options are incorrect:**

- **A:** Notifications alone do not implement universal resource termination.
- **B:** A monitoring threshold does not guarantee an upper bound on incurred charges.
- **C:** A budget does not change service pricing.

**AWS references:** [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).

</details>

## Question 3

<!-- question-id: 23-Q03 -->

A workload has a predictable long-running compute baseline plus uncertain bursts. Which cost approach avoids committing to the full possible peak?

A) Commit to the maximum hypothetical peak without measuring utilization.

B) Assume an unused Savings Plan commitment is automatically refunded.

C) Right-size from measured usage and evaluate an appropriate Savings Plan commitment for the stable baseline, leaving variable usage to suitable flexible capacity.

D) Run every critical non-interruptible component only on Spot to avoid commitments.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** A commitment should match expected eligible usage and tolerance for underutilization. Bursts and interruption-sensitive work need a separate capacity and pricing decision.

**Why the other options are incorrect:**

- **A:** Unmeasured peak commitments risk paying for unused commitment.
- **B:** Unused commitment is not automatically refunded.
- **D:** Interruption-sensitive critical components cannot assume uninterrupted Spot availability.

**AWS references:** [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html), [EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html), [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html).

</details>

## Question 4

<!-- question-id: 23-Q04 -->

A team needs to inspect historical AWS costs by service and compare trends before choosing optimization actions. Which service fits?

A) AWS Cost Explorer with appropriate filters and grouping.

B) An SQS dead-letter queue.

C) An EC2 placement group.

D) An S3 Object Lock retention mode.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Cost Explorer supports cost and usage analysis. Reliable allocation may require activated cost allocation tags or other account structure; analysis does not automatically implement every optimization.

**Why the other options are incorrect:**

- **B:** A DLQ stores failed messages rather than cost trends.
- **C:** Placement affects instance location, not billing analysis.
- **D:** Retention protection does not group historical spending.

**AWS references:** [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html).

</details>

## Question 5

<!-- question-id: 23-Q05 -->

A team expects an SCP attached to the organization root to restrict IAM roles in the organization management account. What is the correction?

A) SCPs do not restrict users or roles in the management account; protect that account with appropriate IAM controls and limited use.

B) The expectation is always correct for every management-account identity.

C) An SCP grants root access to every member account automatically.

D) Removing all logging is the recommended management-account protection.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** AWS documents that SCPs do not affect management-account users or roles. Keep workloads and routine operations appropriately separated from highly privileged organization administration.

**Why the other options are incorrect:**

- **B:** This ignores the documented management-account exception.
- **C:** SCPs do not issue blanket permission grants.
- **D:** Logging removal weakens accountability and does not enforce permissions.

**AWS references:** [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

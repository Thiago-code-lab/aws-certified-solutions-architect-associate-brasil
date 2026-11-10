# Review Flashcards

## Card 01

**Question:** An SCP explicitly denies a service action in a member account. An IAM role there has AdministratorAccess. What happens to a request covered by the SCP deny?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** It is denied, unless the principal or action is within a documented SCP exemption. An applicable SCP deny limits permissions in member accounts, including administrator roles. Management-account principals and some other entities have documented exceptions, which must not be generalized away.

**AWS references:** [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

</details>

## Card 02

**Question:** A lab account has an AWS Budgets notification at a chosen spend threshold. Does this guarantee that all charges stop exactly at that amount?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** No. Budget data and notifications are delayed; explicit controls, suitable actions, limits, and cleanup are still needed. Budgets track costs and usage and can support configured actions. They are not a universal instantaneous hard spending cap; already-running resources and delayed cost data require careful operational controls.

**AWS references:** [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).

</details>

## Card 03

**Question:** A workload has a predictable long-running compute baseline plus uncertain bursts. Which cost approach avoids committing to the full possible peak?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Right-size from measured usage and evaluate an appropriate Savings Plan commitment for the stable baseline, leaving variable usage to suitable flexible capacity. A commitment should match expected eligible usage and tolerance for underutilization. Bursts and interruption-sensitive work need a separate capacity and pricing decision.

**AWS references:** [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html), [EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html), [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html).

</details>

## Card 04

**Question:** A team needs to inspect historical AWS costs by service and compare trends before choosing optimization actions. Which service fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** AWS Cost Explorer with appropriate filters and grouping. Cost Explorer supports cost and usage analysis. Reliable allocation may require activated cost allocation tags or other account structure; analysis does not automatically implement every optimization.

**AWS references:** [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html).

</details>

## Card 05

**Question:** A team expects an SCP attached to the organization root to restrict IAM roles in the organization management account. What is the correction?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** SCPs do not restrict users or roles in the management account; protect that account with appropriate IAM controls and limited use. AWS documents that SCPs do not affect management-account users or roles. Keep workloads and routine operations appropriately separated from highly privileged organization administration.

**AWS references:** [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

## Card 06

**Question:** A lab account has an AWS Budgets notification at a chosen spend threshold. Does this guarantee that all charges stop exactly at that amount?

Why does this alternative fail: “Yes. Every budget automatically terminates every billable resource instantly.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Notifications alone do not implement universal resource termination.

**AWS references:** [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).

</details>

## Card 07

**Question:** A workload has a predictable long-running compute baseline plus uncertain bursts. Which cost approach avoids committing to the full possible peak?

Why does this alternative fail: “Commit to the maximum hypothetical peak without measuring utilization.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Unmeasured peak commitments risk paying for unused commitment.

**AWS references:** [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html), [EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html), [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html).

</details>

## Card 08

**Question:** A team needs to inspect historical AWS costs by service and compare trends before choosing optimization actions. Which service fits?

Why does this alternative fail: “An SQS dead-letter queue.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** A DLQ stores failed messages rather than cost trends.

**AWS references:** [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

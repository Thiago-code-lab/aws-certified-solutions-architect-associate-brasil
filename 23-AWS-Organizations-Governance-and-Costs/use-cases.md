# Use Cases

## Scenario 1: Organization permission ceiling

**Requirement:** An SCP explicitly denies a service action in a member account. An IAM role there has AdministratorAccess. What happens to a request covered by the SCP deny?

**Recommended design:** It is denied, unless the principal or action is within a documented SCP exemption.

**Reason and boundary:** An applicable SCP deny limits permissions in member accounts, including administrator roles. Management-account principals and some other entities have documented exceptions, which must not be generalized away.

**Rejected alternative:** AdministratorAccess automatically overrides every SCP deny. An identity allow does not override an applicable explicit deny.

**AWS references:** [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

## Scenario 2: Budget is not an instantaneous cap

**Requirement:** A lab account has an AWS Budgets notification at a chosen spend threshold. Does this guarantee that all charges stop exactly at that amount?

**Recommended design:** No. Budget data and notifications are delayed; explicit controls, suitable actions, limits, and cleanup are still needed.

**Reason and boundary:** Budgets track costs and usage and can support configured actions. They are not a universal instantaneous hard spending cap; already-running resources and delayed cost data require careful operational controls.

**Rejected alternative:** Yes. Every budget automatically terminates every billable resource instantly. Notifications alone do not implement universal resource termination.

**AWS references:** [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).

## Scenario 3: Commit only a measured baseline

**Requirement:** A workload has a predictable long-running compute baseline plus uncertain bursts. Which cost approach avoids committing to the full possible peak?

**Recommended design:** Right-size from measured usage and evaluate an appropriate Savings Plan commitment for the stable baseline, leaving variable usage to suitable flexible capacity.

**Reason and boundary:** A commitment should match expected eligible usage and tolerance for underutilization. Bursts and interruption-sensitive work need a separate capacity and pricing decision.

**Rejected alternative:** Commit to the maximum hypothetical peak without measuring utilization. Unmeasured peak commitments risk paying for unused commitment.

**AWS references:** [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html), [EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html), [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html).

## Scenario 4: Analyze spending

**Requirement:** A team needs to inspect historical AWS costs by service and compare trends before choosing optimization actions. Which service fits?

**Recommended design:** AWS Cost Explorer with appropriate filters and grouping.

**Reason and boundary:** Cost Explorer supports cost and usage analysis. Reliable allocation may require activated cost allocation tags or other account structure; analysis does not automatically implement every optimization.

**Rejected alternative:** An SQS dead-letter queue. A DLQ stores failed messages rather than cost trends.

**AWS references:** [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

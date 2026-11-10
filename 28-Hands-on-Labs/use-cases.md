# Use Cases

## Scenario 1: Lab cost planning

**Requirement:** Before creating a NAT gateway and database for a short lab, which cost practice is appropriate?

**Recommended design:** Estimate the specific regional resources and usage, check the account applicable credits or Free Tier eligibility, set cost notifications, and plan cleanup.

**Reason and boundary:** Short runtime does not imply zero cost. Pricing, plan eligibility, retained resources, and delayed cost reporting must all be considered before deployment.

**Rejected alternative:** Assume any resource used for fewer than a few hours is free. Many resources incur charges during short sessions.

**AWS references:** [AWS Pricing Calculator](https://calculator.aws/), [AWS Free Tier account eligibility](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html), [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).

## Scenario 2: Bounded failure testing

**Requirement:** A learner wants to test recovery behavior. Which approach keeps the experiment appropriately scoped?

**Recommended design:** Use isolated lab resources with non-sensitive test data, define the expected failure and rollback, and verify recovery without touching production.

**Reason and boundary:** A bounded recovery experiment needs an explicit hypothesis, recoverable data, observability, and a safe environment. The test result should be compared with its recovery objective.

**Rejected alternative:** Interrupt a production database without a test scope or recovery plan. An uncontrolled production interruption is not an isolated learning experiment.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

## Scenario 3: Recover versioned lab objects

**Requirement:** A learner overwrote an object in a versioning-enabled S3 test bucket. The earlier version was not permanently deleted. Which recovery action fits?

**Recommended design:** Retrieve the earlier version and, if needed, copy it to become the current version of the key.

**Reason and boundary:** Versioning retains earlier object versions, which can be retrieved or used to restore desired contents. Recovery still depends on retaining the needed version and permissions.

**Rejected alternative:** Assume the object is irrecoverable solely because its key was overwritten. The premise says an earlier retained version exists.

**AWS references:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html).

## Scenario 4: Authorize only lab access

**Requirement:** A lab requires read-only access to one test object prefix. Which permission approach fits?

**Recommended design:** Use a dedicated workload role scoped to the required actions and object resources.

**Reason and boundary:** A scoped role limits the blast radius and avoids distributing long-lived credentials. Test data and resource boundaries should be separated from production.

**Rejected alternative:** Reuse a production root access key. Root credentials are not appropriate reusable lab credentials.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

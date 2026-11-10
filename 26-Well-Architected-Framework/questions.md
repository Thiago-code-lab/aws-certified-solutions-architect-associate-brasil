# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 26-Q01 -->

Which set names the six pillars of the AWS Well-Architected Framework?

A) Security, reliability, performance, and cost only, because exam domains are the complete framework.

B) Compute, storage, networking, databases, analytics, and support.

C) Availability, elasticity, replication, backup, billing, and DNS.

D) Operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** The framework has six pillars. The four SAA-C03 scored-content domains are a different grouping and must not be mistaken for the complete framework.

**Why the other options are incorrect:**

- **A:** This omits operational excellence and sustainability and confuses framework pillars with exam domains.
- **B:** These are service or operational categories, not the six named pillars.
- **C:** These are concepts and functions rather than the named pillar set.

**AWS references:** [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html).

</details>

## Question 2

<!-- question-id: 26-Q02 -->

A team completes a workload review in AWS Well-Architected Tool. What does that establish?

A) Every high-risk issue is automatically fixed in production.

B) It records review findings and improvement opportunities; implementing and validating improvements remains the team responsibility.

C) The application is guaranteed never to fail.

D) IAM policies are automatically replaced with the correct permissions for every workload.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** The tool supports structured workload assessment and improvement planning. Review completion is not proof that every recommended change was implemented or tested.

**Why the other options are incorrect:**

- **A:** A review record is not universal automatic remediation.
- **C:** No architecture review guarantees failure-free operation.
- **D:** The tool does not automatically replace all workload authorization policies.

**AWS references:** [AWS Well-Architected Tool workload review](https://docs.aws.amazon.com/wellarchitected/latest/userguide/tutorial.html), [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html).

</details>

## Question 3

<!-- question-id: 26-Q03 -->

A proposal cuts cost by removing the only recovery copy of irreplaceable business data. The retention and recovery requirements have not changed. Is the proposal justified solely by lower storage cost?

A) Yes. The lowest bill is always the best architecture.

B) Yes. Sustainability requires deleting every backup.

C) No. Cost optimization must still satisfy retention and recovery requirements.

D) Yes. A faster CPU replaces retained recovery data.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** The pillars must be considered together. Lower cost is not an improvement when it violates a mandatory data-protection or recovery constraint.

**Why the other options are incorrect:**

- **A:** Price alone is not sufficient when requirements are unmet.
- **B:** The sustainability pillar does not require violating recovery obligations.
- **D:** Compute performance does not recreate absent recovery copies.

**AWS references:** [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Question 4

<!-- question-id: 26-Q04 -->

Which practice provides useful evidence that an operational recovery runbook works?

A) Exercise the runbook in an isolated recovery test, measure results, and update it from observed failures.

B) Write a runbook and assume its existence proves successful recovery.

C) Delete production resources without an approved test scope.

D) Remove metrics so no failed test appears in dashboards.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** A tested procedure exposes missing dependencies, permissions, and timing assumptions. Runbooks and observability support learning and repeatable operations.

**Why the other options are incorrect:**

- **B:** Documentation alone does not validate execution.
- **C:** An uncontrolled production deletion is not the required isolated validation.
- **D:** Hiding telemetry prevents useful validation and learning.

**AWS references:** [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Question 5

<!-- question-id: 26-Q05 -->

A team migrates a workload to managed services. Which architectural conclusion follows the shared responsibility model?

A) AWS manages more infrastructure, but the team must still design appropriate access, data protection, configuration, and application behavior.

B) Every customer security responsibility disappears.

C) Every resource must be publicly accessible because AWS manages it.

D) All managed services share identical responsibilities and controls.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** The responsibility boundary depends on the service. Managed infrastructure does not remove customer responsibility for data use, permissions, and workload configuration.

**Why the other options are incorrect:**

- **B:** Managed services do not eliminate the customer side of the responsibility model.
- **C:** Public access is a separate authorization and network decision.
- **D:** Responsibility boundaries and configuration controls differ by service.

**AWS references:** [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

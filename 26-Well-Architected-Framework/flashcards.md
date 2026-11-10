# Review Flashcards

## Card 01

**Question:** Which set names the six pillars of the AWS Well-Architected Framework?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability. The framework has six pillars. The four SAA-C03 scored-content domains are a different grouping and must not be mistaken for the complete framework.

**AWS references:** [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html).

</details>

## Card 02

**Question:** A team completes a workload review in AWS Well-Architected Tool. What does that establish?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** It records review findings and improvement opportunities; implementing and validating improvements remains the team responsibility. The tool supports structured workload assessment and improvement planning. Review completion is not proof that every recommended change was implemented or tested.

**AWS references:** [AWS Well-Architected Tool workload review](https://docs.aws.amazon.com/wellarchitected/latest/userguide/tutorial.html), [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html).

</details>

## Card 03

**Question:** A proposal cuts cost by removing the only recovery copy of irreplaceable business data. The retention and recovery requirements have not changed. Is the proposal justified solely by lower storage cost?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** No. Cost optimization must still satisfy retention and recovery requirements. The pillars must be considered together. Lower cost is not an improvement when it violates a mandatory data-protection or recovery constraint.

**AWS references:** [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 04

**Question:** Which practice provides useful evidence that an operational recovery runbook works?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Exercise the runbook in an isolated recovery test, measure results, and update it from observed failures. A tested procedure exposes missing dependencies, permissions, and timing assumptions. Runbooks and observability support learning and repeatable operations.

**AWS references:** [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 05

**Question:** A team migrates a workload to managed services. Which architectural conclusion follows the shared responsibility model?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** AWS manages more infrastructure, but the team must still design appropriate access, data protection, configuration, and application behavior. The responsibility boundary depends on the service. Managed infrastructure does not remove customer responsibility for data use, permissions, and workload configuration.

**AWS references:** [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html).

</details>

## Card 06

**Question:** A team completes a workload review in AWS Well-Architected Tool. What does that establish?

Why does this alternative fail: “Every high-risk issue is automatically fixed in production.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** A review record is not universal automatic remediation.

**AWS references:** [AWS Well-Architected Tool workload review](https://docs.aws.amazon.com/wellarchitected/latest/userguide/tutorial.html), [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html).

</details>

## Card 07

**Question:** A proposal cuts cost by removing the only recovery copy of irreplaceable business data. The retention and recovery requirements have not changed. Is the proposal justified solely by lower storage cost?

Why does this alternative fail: “Yes. The lowest bill is always the best architecture.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Price alone is not sufficient when requirements are unmet.

**AWS references:** [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 08

**Question:** Which practice provides useful evidence that an operational recovery runbook works?

Why does this alternative fail: “Write a runbook and assume its existence proves successful recovery.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Documentation alone does not validate execution.

**AWS references:** [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

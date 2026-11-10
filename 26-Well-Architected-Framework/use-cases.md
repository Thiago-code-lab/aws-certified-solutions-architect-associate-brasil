# Use Cases

## Scenario 1: Six Well-Architected pillars

**Requirement:** Which set names the six pillars of the AWS Well-Architected Framework?

**Recommended design:** Operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

**Reason and boundary:** The framework has six pillars. The four SAA-C03 scored-content domains are a different grouping and must not be mistaken for the complete framework.

**Rejected alternative:** Security, reliability, performance, and cost only, because exam domains are the complete framework. This omits operational excellence and sustainability and confuses framework pillars with exam domains.

**AWS references:** [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html).

## Scenario 2: Review tool versus automatic remediation

**Requirement:** A team completes a workload review in AWS Well-Architected Tool. What does that establish?

**Recommended design:** It records review findings and improvement opportunities; implementing and validating improvements remains the team responsibility.

**Reason and boundary:** The tool supports structured workload assessment and improvement planning. Review completion is not proof that every recommended change was implemented or tested.

**Rejected alternative:** Every high-risk issue is automatically fixed in production. A review record is not universal automatic remediation.

**AWS references:** [AWS Well-Architected Tool workload review](https://docs.aws.amazon.com/wellarchitected/latest/userguide/tutorial.html), [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html).

## Scenario 3: Measured cost trade-offs

**Requirement:** A proposal cuts cost by removing the only recovery copy of irreplaceable business data. The retention and recovery requirements have not changed. Is the proposal justified solely by lower storage cost?

**Recommended design:** No. Cost optimization must still satisfy retention and recovery requirements.

**Reason and boundary:** The pillars must be considered together. Lower cost is not an improvement when it violates a mandatory data-protection or recovery constraint.

**Rejected alternative:** Yes. The lowest bill is always the best architecture. Price alone is not sufficient when requirements are unmet.

**AWS references:** [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

## Scenario 4: Operational excellence evidence

**Requirement:** Which practice provides useful evidence that an operational recovery runbook works?

**Recommended design:** Exercise the runbook in an isolated recovery test, measure results, and update it from observed failures.

**Reason and boundary:** A tested procedure exposes missing dependencies, permissions, and timing assumptions. Runbooks and observability support learning and repeatable operations.

**Rejected alternative:** Write a runbook and assume its existence proves successful recovery. Documentation alone does not validate execution.

**AWS references:** [Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

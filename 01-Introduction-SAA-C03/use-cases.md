# Use Cases

## Scenario 1: Official domain weights

**Requirement:** Which allocation matches the official SAA-C03 scored-content domains?

**Recommended design:** Security 30%, Resilience 26%, Performance 24%, Cost Optimization 20%.

**Reason and boundary:** The exam guide assigns these four weights to scored content. A community practice set need not have the same distribution.

**Rejected alternative:** Security 24%, Resilience 30%, Performance 28%, Cost Optimization 18%. These were the incorrect weights inherited from the source edition.

**AWS references:** [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html).

## Scenario 2: Shared responsibility for EC2

**Requirement:** A team runs its application on EC2 instances. Under the shared responsibility model, who patches the guest operating system?

**Recommended design:** The customer operating the EC2 instances.

**Reason and boundary:** For EC2, AWS manages the underlying infrastructure; the customer manages the guest OS, applications, and their configuration. Automation can help the customer perform that responsibility.

**Rejected alternative:** AWS patches the customer guest OS automatically in every EC2 deployment. EC2 does not transfer all guest OS maintenance to AWS.

**AWS references:** [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

## Scenario 3: Availability is not backup

**Requirement:** A workload must recover a document that a user accidentally overwrote yesterday. Which capability directly addresses that requirement?

**Recommended design:** Retain previous object versions and test how to restore the required version.

**Reason and boundary:** S3 Versioning retains earlier versions so an overwrite can be reversed. Redundant compute and DNS do not retain earlier application data.

**Rejected alternative:** Put two web servers behind a load balancer without versioning the data. Compute redundancy alone does not preserve historical object contents.

**AWS references:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

## Scenario 4: Interpreting recovery objectives

**Requirement:** A business can tolerate losing at most 15 minutes of data and needs service restored within 2 hours. Which objectives express these requirements?

**Recommended design:** RPO of 15 minutes and RTO of 2 hours.

**Reason and boundary:** RPO limits acceptable data loss measured in time; RTO limits acceptable recovery time. Managed services do not remove the need to define or test those objectives.

**Rejected alternative:** RTO of 15 minutes and RPO of 2 hours. This reverses the meanings of RPO and RTO.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Review Flashcards

## Card 01

**Question:** Which allocation matches the official SAA-C03 scored-content domains?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Security 30%, Resilience 26%, Performance 24%, Cost Optimization 20%. The exam guide assigns these four weights to scored content. A community practice set need not have the same distribution.

**AWS references:** [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html).

</details>

## Card 02

**Question:** A team runs its application on EC2 instances. Under the shared responsibility model, who patches the guest operating system?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The customer operating the EC2 instances. For EC2, AWS manages the underlying infrastructure; the customer manages the guest OS, applications, and their configuration. Automation can help the customer perform that responsibility.

**AWS references:** [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

</details>

## Card 03

**Question:** A workload must recover a document that a user accidentally overwrote yesterday. Which capability directly addresses that requirement?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Retain previous object versions and test how to restore the required version. S3 Versioning retains earlier versions so an overwrite can be reversed. Redundant compute and DNS do not retain earlier application data.

**AWS references:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 04

**Question:** A business can tolerate losing at most 15 minutes of data and needs service restored within 2 hours. Which objectives express these requirements?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** RPO of 15 minutes and RTO of 2 hours. RPO limits acceptable data loss measured in time; RTO limits acceptable recovery time. Managed services do not remove the need to define or test those objectives.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

</details>

## Card 05

**Question:** A design requires AWS API access from an EC2 application without distributing long-lived access keys. Which proposal satisfies the security requirement?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Attach an appropriately scoped IAM role to the instance through an instance profile. An EC2 workload can obtain temporary credentials from its IAM role. Permissions should cover only the application actions and resources it needs.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

## Card 06

**Question:** A team runs its application on EC2 instances. Under the shared responsibility model, who patches the guest operating system?

Why does this alternative fail: “AWS patches the customer guest OS automatically in every EC2 deployment.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** EC2 does not transfer all guest OS maintenance to AWS.

**AWS references:** [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

</details>

## Card 07

**Question:** A workload must recover a document that a user accidentally overwrote yesterday. Which capability directly addresses that requirement?

Why does this alternative fail: “Put two web servers behind a load balancer without versioning the data.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Compute redundancy alone does not preserve historical object contents.

**AWS references:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 08

**Question:** A business can tolerate losing at most 15 minutes of data and needs service restored within 2 hours. Which objectives express these requirements?

Why does this alternative fail: “RTO of 15 minutes and RPO of 2 hours.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** This reverses the meanings of RPO and RTO.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

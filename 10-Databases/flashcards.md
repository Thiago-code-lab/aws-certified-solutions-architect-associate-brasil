# Review Flashcards

## Card 01

**Question:** An RDS Multi-AZ DB instance deployment has one primary and one synchronous standby. Which statement about that standby is correct?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** It supports managed failover and does not serve application read traffic. The standby in a Multi-AZ DB instance deployment is for availability. This must not be generalized to Multi-AZ DB clusters, whose reader instances can serve reads.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 02

**Question:** A team selects an RDS Multi-AZ DB cluster deployment with a writer and two readable instances in separate AZs. How can those instances be used?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** They support failover and can serve read traffic through the appropriate endpoints. RDS distinguishes Multi-AZ DB clusters from Multi-AZ DB instance deployments. The cluster has one writer and readable failover candidates distributed across three AZs in one Region.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

</details>

## Card 03

**Question:** Reports are directed to an ordinary asynchronous RDS DB instance read replica. Can an application assume every successful write to the primary is immediately visible there?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** No. Replication lag can make the replica temporarily stale. Asynchronous read replicas are useful for read scaling, but the application must tolerate lag. Read-after-write requirements may require a different read path.

**AWS references:** [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html).

</details>

## Card 04

**Question:** A DynamoDB application requires strongly consistent reads immediately after a successful write. Which read path supports that consistency option?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Read the base table with ConsistentRead enabled, rather than using a GSI for this read. DynamoDB supports strongly consistent reads on tables and local secondary indexes. Global secondary index reads are eventually consistent; that restriction is distinct from global-table consistency modes.

**AWS references:** [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

</details>

## Card 05

**Question:** A review claims that every DynamoDB global table is necessarily eventually consistent across Regions. What is the accurate correction?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Global tables offer multi-Region eventual consistency and multi-Region strong consistency modes; check the selected mode and supported configuration. The current documentation distinguishes MREC and MRSC. Availability, topology, and feature constraints must be checked before choosing a mode; neither blanket consistency claim is correct.

**AWS references:** [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

</details>

## Card 06

**Question:** A team selects an RDS Multi-AZ DB cluster deployment with a writer and two readable instances in separate AZs. How can those instances be used?

Why does this alternative fail: “Neither reader can serve read traffic because every Multi-AZ deployment forbids reads.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** This incorrectly applies the DB instance standby restriction to a DB cluster.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

</details>

## Card 07

**Question:** Reports are directed to an ordinary asynchronous RDS DB instance read replica. Can an application assume every successful write to the primary is immediately visible there?

Why does this alternative fail: “Yes. All RDS read replicas use synchronous commit.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The question explicitly specifies an asynchronous read replica.

**AWS references:** [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html).

</details>

## Card 08

**Question:** A DynamoDB application requires strongly consistent reads immediately after a successful write. Which read path supports that consistency option?

Why does this alternative fail: “Read a global secondary index with ConsistentRead enabled.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** GSIs do not support strongly consistent reads.

**AWS references:** [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

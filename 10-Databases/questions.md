# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 10-Q01 -->

An RDS Multi-AZ DB instance deployment has one primary and one synchronous standby. Which statement about that standby is correct?

A) It supports managed failover and does not serve application read traffic.

B) It is a read-scaling endpoint for reporting queries.

C) It is an asynchronous cross-Region read replica.

D) It replaces the need for backups against accidental data deletion.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** The standby in a Multi-AZ DB instance deployment is for availability. This must not be generalized to Multi-AZ DB clusters, whose reader instances can serve reads.

**Why the other options are incorrect:**

- **B:** The single standby in this deployment type is not readable.
- **C:** The stated deployment is not a cross-Region asynchronous read replica.
- **D:** Replicated deletions or corruption can still require recovery from backups.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Question 2

<!-- question-id: 10-Q02 -->

A team selects an RDS Multi-AZ DB cluster deployment with a writer and two readable instances in separate AZs. How can those instances be used?

A) Neither reader can serve read traffic because every Multi-AZ deployment forbids reads.

B) All three instances independently accept application writes.

C) The cluster is inherently a multi-Region deployment.

D) They support failover and can serve read traffic through the appropriate endpoints.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** RDS distinguishes Multi-AZ DB clusters from Multi-AZ DB instance deployments. The cluster has one writer and readable failover candidates distributed across three AZs in one Region.

**Why the other options are incorrect:**

- **A:** This incorrectly applies the DB instance standby restriction to a DB cluster.
- **B:** This cluster topology has one writer, not three independent writers.
- **C:** Multiple AZs do not imply multiple Regions.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

</details>

## Question 3

<!-- question-id: 10-Q03 -->

Reports are directed to an ordinary asynchronous RDS DB instance read replica. Can an application assume every successful write to the primary is immediately visible there?

A) Yes. All RDS read replicas use synchronous commit.

B) Yes. Adding a DNS name makes replication synchronous.

C) Yes. A security group with broader permissions removes replica lag.

D) No. Replication lag can make the replica temporarily stale.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Asynchronous read replicas are useful for read scaling, but the application must tolerate lag. Read-after-write requirements may require a different read path.

**Why the other options are incorrect:**

- **A:** The question explicitly specifies an asynchronous read replica.
- **B:** DNS naming does not change database replication semantics.
- **C:** Network permissions cannot convert asynchronous replication into synchronous replication.

**AWS references:** [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html).

</details>

## Question 4

<!-- question-id: 10-Q04 -->

A DynamoDB application requires strongly consistent reads immediately after a successful write. Which read path supports that consistency option?

A) Read a global secondary index with ConsistentRead enabled.

B) Assume every eventually consistent read must show the latest write.

C) Read the base table with ConsistentRead enabled, rather than using a GSI for this read.

D) Replace the read with a CloudWatch alarm.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** DynamoDB supports strongly consistent reads on tables and local secondary indexes. Global secondary index reads are eventually consistent; that restriction is distinct from global-table consistency modes.

**Why the other options are incorrect:**

- **A:** GSIs do not support strongly consistent reads.
- **B:** An eventually consistent read can temporarily return an earlier committed value.
- **D:** An alarm is not a database read operation.

**AWS references:** [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

</details>

## Question 5

<!-- question-id: 10-Q05 -->

A review claims that every DynamoDB global table is necessarily eventually consistent across Regions. What is the accurate correction?

A) Every global table always uses strong consistency regardless of configuration.

B) Global tables cannot replicate data between Regions.

C) Global tables offer multi-Region eventual consistency and multi-Region strong consistency modes; check the selected mode and supported configuration.

D) A GSI automatically provides strongly consistent cross-Region reads.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** The current documentation distinguishes MREC and MRSC. Availability, topology, and feature constraints must be checked before choosing a mode; neither blanket consistency claim is correct.

**Why the other options are incorrect:**

- **A:** MREC remains an eventually consistent mode.
- **B:** Multi-Region replication is the defining purpose of global tables.
- **D:** GSI reads remain eventually consistent and do not supply this guarantee.

**AWS references:** [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Use Cases

## Scenario 1: RDS instance deployment standby

**Requirement:** An RDS Multi-AZ DB instance deployment has one primary and one synchronous standby. Which statement about that standby is correct?

**Recommended design:** It supports managed failover and does not serve application read traffic.

**Reason and boundary:** The standby in a Multi-AZ DB instance deployment is for availability. This must not be generalized to Multi-AZ DB clusters, whose reader instances can serve reads.

**Rejected alternative:** It is a read-scaling endpoint for reporting queries. The single standby in this deployment type is not readable.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

## Scenario 2: RDS cluster deployment readers

**Requirement:** A team selects an RDS Multi-AZ DB cluster deployment with a writer and two readable instances in separate AZs. How can those instances be used?

**Recommended design:** They support failover and can serve read traffic through the appropriate endpoints.

**Reason and boundary:** RDS distinguishes Multi-AZ DB clusters from Multi-AZ DB instance deployments. The cluster has one writer and readable failover candidates distributed across three AZs in one Region.

**Rejected alternative:** Neither reader can serve read traffic because every Multi-AZ deployment forbids reads. This incorrectly applies the DB instance standby restriction to a DB cluster.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

## Scenario 3: Read replica lag

**Requirement:** Reports are directed to an ordinary asynchronous RDS DB instance read replica. Can an application assume every successful write to the primary is immediately visible there?

**Recommended design:** No. Replication lag can make the replica temporarily stale.

**Reason and boundary:** Asynchronous read replicas are useful for read scaling, but the application must tolerate lag. Read-after-write requirements may require a different read path.

**Rejected alternative:** Yes. All RDS read replicas use synchronous commit. The question explicitly specifies an asynchronous read replica.

**AWS references:** [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html).

## Scenario 4: DynamoDB GSI consistency

**Requirement:** A DynamoDB application requires strongly consistent reads immediately after a successful write. Which read path supports that consistency option?

**Recommended design:** Read the base table with ConsistentRead enabled, rather than using a GSI for this read.

**Reason and boundary:** DynamoDB supports strongly consistent reads on tables and local secondary indexes. Global secondary index reads are eventually consistent; that restriction is distinct from global-table consistency modes.

**Rejected alternative:** Read a global secondary index with ConsistentRead enabled. GSIs do not support strongly consistent reads.

**AWS references:** [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| RDS instance deployment standby | It supports managed failover and does not serve application read traffic. | The standby in a Multi-AZ DB instance deployment is for availability. This must not be generalized to Multi-AZ DB clusters, whose reader instances can serve reads. |
| RDS cluster deployment readers | They support failover and can serve read traffic through the appropriate endpoints. | RDS distinguishes Multi-AZ DB clusters from Multi-AZ DB instance deployments. The cluster has one writer and readable failover candidates distributed across three AZs in one Region. |
| Read replica lag | No. Replication lag can make the replica temporarily stale. | Asynchronous read replicas are useful for read scaling, but the application must tolerate lag. Read-after-write requirements may require a different read path. |
| DynamoDB GSI consistency | Read the base table with ConsistentRead enabled, rather than using a GSI for this read. | DynamoDB supports strongly consistent reads on tables and local secondary indexes. Global secondary index reads are eventually consistent; that restriction is distinct from global-table consistency modes. |
| DynamoDB global table modes | Global tables offer multi-Region eventual consistency and multi-Region strong consistency modes; check the selected mode and supported configuration. | The current documentation distinguishes MREC and MRSC. Availability, topology, and feature constraints must be checked before choosing a mode; neither blanket consistency claim is correct. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **RDS instance deployment standby:** The single standby in this deployment type is not readable.
- **RDS cluster deployment readers:** This incorrectly applies the DB instance standby restriction to a DB cluster.
- **Read replica lag:** The question explicitly specifies an asynchronous read replica.
- **DynamoDB GSI consistency:** GSIs do not support strongly consistent reads.
- **DynamoDB global table modes:** MREC remains an eventually consistent mode.

## AWS References

[RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html), [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

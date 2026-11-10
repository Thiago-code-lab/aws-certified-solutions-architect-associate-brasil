# Databases

## Overview

Select database deployments from consistency, query, availability, recovery, and capacity requirements. Name the exact RDS deployment type and DynamoDB consistency mode rather than relying on blanket service slogans.

## Key Concepts

- **RDS instance deployment standby:** The standby in a Multi-AZ DB instance deployment is for availability. This must not be generalized to Multi-AZ DB clusters, whose reader instances can serve reads.
- **RDS cluster deployment readers:** RDS distinguishes Multi-AZ DB clusters from Multi-AZ DB instance deployments. The cluster has one writer and readable failover candidates distributed across three AZs in one Region.
- **Read replica lag:** Asynchronous read replicas are useful for read scaling, but the application must tolerate lag. Read-after-write requirements may require a different read path.
- **DynamoDB GSI consistency:** DynamoDB supports strongly consistent reads on tables and local secondary indexes. Global secondary index reads are eventually consistent; that restriction is distinct from global-table consistency modes.
- **DynamoDB global table modes:** The current documentation distinguishes MREC and MRSC. Availability, topology, and feature constraints must be checked before choosing a mode; neither blanket consistency claim is correct.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **RDS instance deployment standby:** It supports managed failover and does not serve application read traffic.
2. **RDS cluster deployment readers:** They support failover and can serve read traffic through the appropriate endpoints.
3. **Read replica lag:** No. Replication lag can make the replica temporarily stale.
4. **DynamoDB GSI consistency:** Read the base table with ConsistentRead enabled, rather than using a GSI for this read.
5. **DynamoDB global table modes:** Global tables offer multi-Region eventual consistency and multi-Region strong consistency modes; check the selected mode and supported configuration.

## Common Pitfalls

- The single standby in this deployment type is not readable.
- This incorrectly applies the DB instance standby restriction to a DB cluster.
- The question explicitly specifies an asynchronous read replica.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html), [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Athena data layout | Use a suitable date partition layout, columnar Parquet or ORC, compression, and queries that filter the partition keys. | Partition pruning and columnar formats can reduce data read. Partition granularity and file sizes must match the workload; excessive small files can hurt performance. |
| Catalog metadata versus ETL | The Glue Data Catalog stores metadata; a Glue ETL job performs the configured transformation. | Catalog tables describe data and schemas. Crawlers can discover metadata; ETL jobs execute transformation logic. Metadata registration is not proof of transformed output. |
| Managed streaming delivery | Amazon Data Firehose. | Data Firehose buffers and delivers streaming records to supported destinations. Buffering and delivery behavior must be included in end-to-end latency planning. |
| Stream consumers and replay | Kinesis Data Streams with suitable retention and consumer throughput configuration. | Kinesis Data Streams supports independent consumers reading retained records. Shard or capacity configuration, retention, partitioning, and consumer limits must fit the workload. |
| Do not use migration as analytics | No. DMS replication and the required analytical transformations must be assessed separately; use an appropriate ETL design such as Glue jobs. | DMS moves data and supports migration-related capabilities; it is not a blanket substitute for arbitrary business ETL. Define the transformations and validate the curated results. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Athena data layout:** Many tiny files add overhead and omit the requested pruning design.
- **Catalog metadata versus ETL:** Registering metadata does not itself rewrite the data files.
- **Managed streaming delivery:** DNS routing does not ingest and deliver streaming records.
- **Stream consumers and replay:** A shared competing-consumer queue does not provide an independent stream replay cursor to every application.
- **Do not use migration as analytics:** Replication does not imply all required analytical transformations.

## AWS References

[Athena data optimization](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html), [AWS Glue components](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html), [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html), [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

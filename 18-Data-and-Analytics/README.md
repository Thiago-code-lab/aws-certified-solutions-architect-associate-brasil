# Data and Analytics

## Overview

Design analytics from data layout, catalog metadata, transformation logic, streaming delivery, and replay requirements. Managed ingestion and replication are not automatic substitutes for the required business ETL.

## Key Concepts

- **Athena data layout:** Partition pruning and columnar formats can reduce data read. Partition granularity and file sizes must match the workload; excessive small files can hurt performance.
- **Catalog metadata versus ETL:** Catalog tables describe data and schemas. Crawlers can discover metadata; ETL jobs execute transformation logic. Metadata registration is not proof of transformed output.
- **Managed streaming delivery:** Data Firehose buffers and delivers streaming records to supported destinations. Buffering and delivery behavior must be included in end-to-end latency planning.
- **Stream consumers and replay:** Kinesis Data Streams supports independent consumers reading retained records. Shard or capacity configuration, retention, partitioning, and consumer limits must fit the workload.
- **Do not use migration as analytics:** DMS moves data and supports migration-related capabilities; it is not a blanket substitute for arbitrary business ETL. Define the transformations and validate the curated results.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Athena data layout:** Use a suitable date partition layout, columnar Parquet or ORC, compression, and queries that filter the partition keys.
2. **Catalog metadata versus ETL:** The Glue Data Catalog stores metadata; a Glue ETL job performs the configured transformation.
3. **Managed streaming delivery:** Amazon Data Firehose.
4. **Stream consumers and replay:** Kinesis Data Streams with suitable retention and consumer throughput configuration.
5. **Do not use migration as analytics:** No. DMS replication and the required analytical transformations must be assessed separately; use an appropriate ETL design such as Glue jobs.

## Common Pitfalls

- Many tiny files add overhead and omit the requested pruning design.
- Registering metadata does not itself rewrite the data files.
- DNS routing does not ingest and deliver streaming records.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[Athena data optimization](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html), [AWS Glue components](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html), [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html), [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

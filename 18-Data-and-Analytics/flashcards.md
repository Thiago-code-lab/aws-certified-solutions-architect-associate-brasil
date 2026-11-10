# Review Flashcards

## Card 01

**Question:** Athena queries frequently filter an S3 dataset by date and read only a few columns. Which change can reduce scanned data for on-demand queries?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Use a suitable date partition layout, columnar Parquet or ORC, compression, and queries that filter the partition keys. Partition pruning and columnar formats can reduce data read. Partition granularity and file sizes must match the workload; excessive small files can hurt performance.

**AWS references:** [Athena data optimization](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html).

</details>

## Card 02

**Question:** A team needs a shared metadata catalog for tables stored in S3 and a separate transformation job. Which distinction is accurate?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The Glue Data Catalog stores metadata; a Glue ETL job performs the configured transformation. Catalog tables describe data and schemas. Crawlers can discover metadata; ETL jobs execute transformation logic. Metadata registration is not proof of transformed output.

**AWS references:** [AWS Glue components](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html), [Athena data optimization](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html).

</details>

## Card 03

**Question:** An application needs managed delivery of streaming records into S3 and can tolerate buffering before delivery. Which service directly matches?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Amazon Data Firehose. Data Firehose buffers and delivers streaming records to supported destinations. Buffering and delivery behavior must be included in end-to-end latency planning.

**AWS references:** [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html).

</details>

## Card 04

**Question:** Several applications need to read a stream independently and reprocess retained records using their own consumer positions. Which service is designed for this model?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Kinesis Data Streams with suitable retention and consumer throughput configuration. Kinesis Data Streams supports independent consumers reading retained records. Shard or capacity configuration, retention, partitioning, and consumer limits must fit the workload.

**AWS references:** [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).

</details>

## Card 05

**Question:** A team must transform and curate S3 data for analytics. Is an AWS DMS ongoing replication task alone proof that the required business ETL has been implemented?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** No. DMS replication and the required analytical transformations must be assessed separately; use an appropriate ETL design such as Glue jobs. DMS moves data and supports migration-related capabilities; it is not a blanket substitute for arbitrary business ETL. Define the transformations and validate the curated results.

**AWS references:** [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html), [AWS Glue components](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html).

</details>

## Card 06

**Question:** A team needs a shared metadata catalog for tables stored in S3 and a separate transformation job. Which distinction is accurate?

Why does this alternative fail: “Creating a catalog table automatically rewrites all source data into Parquet.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Registering metadata does not itself rewrite the data files.

**AWS references:** [AWS Glue components](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html), [Athena data optimization](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html).

</details>

## Card 07

**Question:** An application needs managed delivery of streaming records into S3 and can tolerate buffering before delivery. Which service directly matches?

Why does this alternative fail: “A Route 53 weighted record.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** DNS routing does not ingest and deliver streaming records.

**AWS references:** [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html).

</details>

## Card 08

**Question:** Several applications need to read a stream independently and reprocess retained records using their own consumer positions. Which service is designed for this model?

Why does this alternative fail: “One SQS queue with all applications competing for the same messages, assuming independent replay positions.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** A shared competing-consumer queue does not provide an independent stream replay cursor to every application.

**AWS references:** [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

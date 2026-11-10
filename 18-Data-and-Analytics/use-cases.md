# Use Cases

## Scenario 1: Athena data layout

**Requirement:** Athena queries frequently filter an S3 dataset by date and read only a few columns. Which change can reduce scanned data for on-demand queries?

**Recommended design:** Use a suitable date partition layout, columnar Parquet or ORC, compression, and queries that filter the partition keys.

**Reason and boundary:** Partition pruning and columnar formats can reduce data read. Partition granularity and file sizes must match the workload; excessive small files can hurt performance.

**Rejected alternative:** Put every record in many tiny unpartitioned CSV objects. Many tiny files add overhead and omit the requested pruning design.

**AWS references:** [Athena data optimization](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html).

## Scenario 2: Catalog metadata versus ETL

**Requirement:** A team needs a shared metadata catalog for tables stored in S3 and a separate transformation job. Which distinction is accurate?

**Recommended design:** The Glue Data Catalog stores metadata; a Glue ETL job performs the configured transformation.

**Reason and boundary:** Catalog tables describe data and schemas. Crawlers can discover metadata; ETL jobs execute transformation logic. Metadata registration is not proof of transformed output.

**Rejected alternative:** Creating a catalog table automatically rewrites all source data into Parquet. Registering metadata does not itself rewrite the data files.

**AWS references:** [AWS Glue components](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html), [Athena data optimization](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html).

## Scenario 3: Managed streaming delivery

**Requirement:** An application needs managed delivery of streaming records into S3 and can tolerate buffering before delivery. Which service directly matches?

**Recommended design:** Amazon Data Firehose.

**Reason and boundary:** Data Firehose buffers and delivers streaming records to supported destinations. Buffering and delivery behavior must be included in end-to-end latency planning.

**Rejected alternative:** A Route 53 weighted record. DNS routing does not ingest and deliver streaming records.

**AWS references:** [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html).

## Scenario 4: Stream consumers and replay

**Requirement:** Several applications need to read a stream independently and reprocess retained records using their own consumer positions. Which service is designed for this model?

**Recommended design:** Kinesis Data Streams with suitable retention and consumer throughput configuration.

**Reason and boundary:** Kinesis Data Streams supports independent consumers reading retained records. Shard or capacity configuration, retention, partitioning, and consumer limits must fit the workload.

**Rejected alternative:** One SQS queue with all applications competing for the same messages, assuming independent replay positions. A shared competing-consumer queue does not provide an independent stream replay cursor to every application.

**AWS references:** [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

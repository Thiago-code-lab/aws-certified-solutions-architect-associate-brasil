# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 18-Q01 -->

Athena queries frequently filter an S3 dataset by date and read only a few columns. Which change can reduce scanned data for on-demand queries?

A) Use a suitable date partition layout, columnar Parquet or ORC, compression, and queries that filter the partition keys.

B) Put every record in many tiny unpartitioned CSV objects.

C) Select every column for every query, even when unused.

D) Move the SQL text into an IAM policy.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Partition pruning and columnar formats can reduce data read. Partition granularity and file sizes must match the workload; excessive small files can hurt performance.

**Why the other options are incorrect:**

- **B:** Many tiny files add overhead and omit the requested pruning design.
- **C:** Reading unnecessary columns can increase scanning.
- **D:** An IAM policy cannot execute an Athena query or optimize data layout.

**AWS references:** [Athena data optimization](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html).

</details>

## Question 2

<!-- question-id: 18-Q02 -->

A team needs a shared metadata catalog for tables stored in S3 and a separate transformation job. Which distinction is accurate?

A) Creating a catalog table automatically rewrites all source data into Parquet.

B) A crawler alone guarantees the business transformation has run.

C) The Glue Data Catalog stores metadata; a Glue ETL job performs the configured transformation.

D) The Data Catalog stores the entire source dataset as its metadata records.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Catalog tables describe data and schemas. Crawlers can discover metadata; ETL jobs execute transformation logic. Metadata registration is not proof of transformed output.

**Why the other options are incorrect:**

- **A:** Registering metadata does not itself rewrite the data files.
- **B:** Schema discovery is not execution of the requested ETL logic.
- **D:** Catalog metadata points to data rather than replacing its storage.

**AWS references:** [AWS Glue components](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html), [Athena data optimization](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html).

</details>

## Question 3

<!-- question-id: 18-Q03 -->

An application needs managed delivery of streaming records into S3 and can tolerate buffering before delivery. Which service directly matches?

A) A Route 53 weighted record.

B) A security group.

C) An EBS snapshot schedule.

D) Amazon Data Firehose.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Data Firehose buffers and delivers streaming records to supported destinations. Buffering and delivery behavior must be included in end-to-end latency planning.

**Why the other options are incorrect:**

- **A:** DNS routing does not ingest and deliver streaming records.
- **B:** Traffic filters are not managed stream delivery.
- **C:** Block-storage backups do not ingest application streams.

**AWS references:** [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html).

</details>

## Question 4

<!-- question-id: 18-Q04 -->

Several applications need to read a stream independently and reprocess retained records using their own consumer positions. Which service is designed for this model?

A) One SQS queue with all applications competing for the same messages, assuming independent replay positions.

B) A public NAT gateway.

C) Kinesis Data Streams with suitable retention and consumer throughput configuration.

D) An S3 bucket policy alone.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Kinesis Data Streams supports independent consumers reading retained records. Shard or capacity configuration, retention, partitioning, and consumer limits must fit the workload.

**Why the other options are incorrect:**

- **A:** A shared competing-consumer queue does not provide an independent stream replay cursor to every application.
- **B:** NAT does not store a replayable stream.
- **D:** An access policy does not implement stream retention or consumers.

**AWS references:** [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).

</details>

## Question 5

<!-- question-id: 18-Q05 -->

A team must transform and curate S3 data for analytics. Is an AWS DMS ongoing replication task alone proof that the required business ETL has been implemented?

A) Yes. Every DMS task automatically supplies all business transformations.

B) No. DMS replication and the required analytical transformations must be assessed separately; use an appropriate ETL design such as Glue jobs.

C) Yes. Any database replication task is equivalent to a data warehouse.

D) Yes. An S3 ACL automatically creates the curated dataset.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** DMS moves data and supports migration-related capabilities; it is not a blanket substitute for arbitrary business ETL. Define the transformations and validate the curated results.

**Why the other options are incorrect:**

- **A:** Replication does not imply all required analytical transformations.
- **C:** Replication and warehouse query processing serve different purposes.
- **D:** An ACL controls access, not data transformation.

**AWS references:** [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html), [AWS Glue components](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

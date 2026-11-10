# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 21-Q01 -->

A heterogeneous relational database migration needs schema assessment and low-downtime data replication. Which plan accounts for both?

A) Assume a data-copy task automatically converts every stored procedure without review.

B) Use only a DNS change while leaving the target database empty.

C) Assess and convert the schema using suitable DMS Schema Conversion or AWS SCT capabilities, then configure supported full-load and CDC replication with cutover validation.

D) Use an S3 lifecycle rule as database change data capture.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** DMS includes schema-conversion and data-migration capabilities, but support and conversion gaps depend on the source and target. Replication, application compatibility, and cutover must be validated separately.

**Why the other options are incorrect:**

- **A:** Conversion support is not universal and incompatible objects can require changes.
- **B:** DNS changes do not populate or validate a database.
- **D:** Object lifecycle does not capture database transaction changes.

**AWS references:** [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html).

</details>

## Question 2

<!-- question-id: 21-Q02 -->

A team wants to rehost supported physical or virtual servers on AWS using continuous block-level replication. Which service is designed for this?

A) Amazon Comprehend.

B) AWS Transform MGN, formerly AWS Application Migration Service.

C) AWS WAF.

D) AWS Secrets Manager rotation alone.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** MGN replicates server blocks and supports test launches and cutover for rehosting. Rehosting is not the same as database-engine conversion or application refactoring.

**Why the other options are incorrect:**

- **A:** Text analysis does not replicate server disks.
- **C:** Web request filtering does not migrate server operating systems.
- **D:** Secret rotation does not replicate or launch a server.

**AWS references:** [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html), [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html).

</details>

## Question 3

<!-- question-id: 21-Q03 -->

An organization has adequate network connectivity and must regularly copy files from a supported on-premises NFS share into S3 with integrity validation. Which service fits?

A) A Route 53 failover record.

B) AWS DataSync.

C) An IAM permissions boundary alone.

D) An ALB listener rule.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** DataSync automates transfers between supported file or object storage systems and AWS storage. Source support, permissions, connectivity, and task settings still need verification.

**Why the other options are incorrect:**

- **A:** DNS failover does not copy a file dataset.
- **C:** A permissions boundary does not transfer files.
- **D:** HTTP target selection is not file synchronization.

**AWS references:** [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html).

</details>

## Question 4

<!-- question-id: 21-Q04 -->

Partners must keep their existing SFTP clients while uploading files to managed AWS-backed storage. Which service directly provides an SFTP endpoint?

A) A bare S3 bucket endpoint assumed to speak SFTP.

B) AWS Transfer Family configured with a supported storage backend and authentication design.

C) A DataSync task assumed to be an interactive partner SFTP server.

D) An SQS queue.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Transfer Family provides managed file-transfer protocol endpoints, including SFTP. S3 storage is not itself an SFTP server, and DataSync serves a different transfer model.

**Why the other options are incorrect:**

- **A:** The S3 API endpoint does not directly provide the SFTP protocol.
- **C:** A DataSync task is not the requested partner-facing SFTP endpoint.
- **D:** SQS transports messages rather than SFTP file sessions.

**AWS references:** [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html), [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html).

</details>

## Question 5

<!-- question-id: 21-Q05 -->

A new AWS customer in a commercial Region is planning a deployment on November 10, 2026. Should a new Snowball device order be assumed available?

A) Yes. A mention in an exam service list guarantees new-customer production availability.

B) No. Snowball Edge is closed to new customers, and AWS has announced commercial-Region device support ending December 31, 2026; evaluate currently available transfer alternatives.

C) Yes. Snowcone is the unrestricted replacement for every new customer.

D) Yes. Buying a Savings Plan creates Snowball device eligibility.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** AWS service availability notices govern deployment eligibility. The exam scope list and historical offline-transfer patterns do not override customer or lifecycle restrictions.

**Why the other options are incorrect:**

- **A:** Exam scope is not a service-ordering entitlement.
- **C:** Snowcone was discontinued; it is not an unrestricted replacement.
- **D:** A compute pricing commitment does not grant device-order eligibility.

**AWS references:** [AWS Snowball availability notice](https://aws.amazon.com/snowball/), [Snowball availability history](https://docs.aws.amazon.com/snowball/latest/developer-guide/doc-history.html), [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

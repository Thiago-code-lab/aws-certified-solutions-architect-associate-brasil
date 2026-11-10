# Review Flashcards

## Card 01

**Question:** A heterogeneous relational database migration needs schema assessment and low-downtime data replication. Which plan accounts for both?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Assess and convert the schema using suitable DMS Schema Conversion or AWS SCT capabilities, then configure supported full-load and CDC replication with cutover validation. DMS includes schema-conversion and data-migration capabilities, but support and conversion gaps depend on the source and target. Replication, application compatibility, and cutover must be validated separately.

**AWS references:** [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html).

</details>

## Card 02

**Question:** A team wants to rehost supported physical or virtual servers on AWS using continuous block-level replication. Which service is designed for this?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** AWS Transform MGN, formerly AWS Application Migration Service. MGN replicates server blocks and supports test launches and cutover for rehosting. Rehosting is not the same as database-engine conversion or application refactoring.

**AWS references:** [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html), [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html).

</details>

## Card 03

**Question:** An organization has adequate network connectivity and must regularly copy files from a supported on-premises NFS share into S3 with integrity validation. Which service fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** AWS DataSync. DataSync automates transfers between supported file or object storage systems and AWS storage. Source support, permissions, connectivity, and task settings still need verification.

**AWS references:** [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html).

</details>

## Card 04

**Question:** Partners must keep their existing SFTP clients while uploading files to managed AWS-backed storage. Which service directly provides an SFTP endpoint?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** AWS Transfer Family configured with a supported storage backend and authentication design. Transfer Family provides managed file-transfer protocol endpoints, including SFTP. S3 storage is not itself an SFTP server, and DataSync serves a different transfer model.

**AWS references:** [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html), [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html).

</details>

## Card 05

**Question:** A new AWS customer in a commercial Region is planning a deployment on November 10, 2026. Should a new Snowball device order be assumed available?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** No. Snowball Edge is closed to new customers, and AWS has announced commercial-Region device support ending December 31, 2026; evaluate currently available transfer alternatives. AWS service availability notices govern deployment eligibility. The exam scope list and historical offline-transfer patterns do not override customer or lifecycle restrictions.

**AWS references:** [AWS Snowball availability notice](https://aws.amazon.com/snowball/), [Snowball availability history](https://docs.aws.amazon.com/snowball/latest/developer-guide/doc-history.html), [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html).

</details>

## Card 06

**Question:** A team wants to rehost supported physical or virtual servers on AWS using continuous block-level replication. Which service is designed for this?

Why does this alternative fail: “Amazon Comprehend.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Text analysis does not replicate server disks.

**AWS references:** [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html), [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html).

</details>

## Card 07

**Question:** An organization has adequate network connectivity and must regularly copy files from a supported on-premises NFS share into S3 with integrity validation. Which service fits?

Why does this alternative fail: “A Route 53 failover record.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** DNS failover does not copy a file dataset.

**AWS references:** [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html).

</details>

## Card 08

**Question:** Partners must keep their existing SFTP clients while uploading files to managed AWS-backed storage. Which service directly provides an SFTP endpoint?

Why does this alternative fail: “A bare S3 bucket endpoint assumed to speak SFTP.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The S3 API endpoint does not directly provide the SFTP protocol.

**AWS references:** [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html), [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

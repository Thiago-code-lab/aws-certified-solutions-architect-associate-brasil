# Use Cases

## Scenario 1: Database migration and conversion

**Requirement:** A heterogeneous relational database migration needs schema assessment and low-downtime data replication. Which plan accounts for both?

**Recommended design:** Assess and convert the schema using suitable DMS Schema Conversion or AWS SCT capabilities, then configure supported full-load and CDC replication with cutover validation.

**Reason and boundary:** DMS includes schema-conversion and data-migration capabilities, but support and conversion gaps depend on the source and target. Replication, application compatibility, and cutover must be validated separately.

**Rejected alternative:** Assume a data-copy task automatically converts every stored procedure without review. Conversion support is not universal and incompatible objects can require changes.

**AWS references:** [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html).

## Scenario 2: Server rehosting

**Requirement:** A team wants to rehost supported physical or virtual servers on AWS using continuous block-level replication. Which service is designed for this?

**Recommended design:** AWS Transform MGN, formerly AWS Application Migration Service.

**Reason and boundary:** MGN replicates server blocks and supports test launches and cutover for rehosting. Rehosting is not the same as database-engine conversion or application refactoring.

**Rejected alternative:** Amazon Comprehend. Text analysis does not replicate server disks.

**AWS references:** [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html), [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html).

## Scenario 3: Online file transfer

**Requirement:** An organization has adequate network connectivity and must regularly copy files from a supported on-premises NFS share into S3 with integrity validation. Which service fits?

**Recommended design:** AWS DataSync.

**Reason and boundary:** DataSync automates transfers between supported file or object storage systems and AWS storage. Source support, permissions, connectivity, and task settings still need verification.

**Rejected alternative:** A Route 53 failover record. DNS failover does not copy a file dataset.

**AWS references:** [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html).

## Scenario 4: Keep SFTP clients

**Requirement:** Partners must keep their existing SFTP clients while uploading files to managed AWS-backed storage. Which service directly provides an SFTP endpoint?

**Recommended design:** AWS Transfer Family configured with a supported storage backend and authentication design.

**Reason and boundary:** Transfer Family provides managed file-transfer protocol endpoints, including SFTP. S3 storage is not itself an SFTP server, and DataSync serves a different transfer model.

**Rejected alternative:** A bare S3 bucket endpoint assumed to speak SFTP. The S3 API endpoint does not directly provide the SFTP protocol.

**AWS references:** [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html), [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

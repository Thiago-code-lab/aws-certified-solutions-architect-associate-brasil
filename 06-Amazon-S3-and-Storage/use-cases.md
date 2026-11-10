# Use Cases

## Scenario 1: Recover an overwritten object

**Requirement:** An S3 bucket must retain earlier object contents when an application overwrites an existing key. Which feature directly provides that history?

**Recommended design:** S3 Versioning.

**Reason and boundary:** Versioning retains multiple versions of an object key. A lifecycle policy may be needed to control noncurrent-version storage costs, and permanent version deletion still needs protection.

**Rejected alternative:** A public-read bucket policy. Public read access does not retain earlier versions and is unnecessary here.

**AWS references:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html).

## Scenario 2: Object retention

**Requirement:** Records require a fixed WORM retention period that must not be shortened or bypassed by users, including the account root user. Which S3 feature and mode fits?

**Recommended design:** S3 Object Lock in compliance mode with the required retention period.

**Reason and boundary:** Compliance-mode retention prevents protected versions from being overwritten or deleted during the retention period, including by root. Plan carefully because a test record can remain retained until expiry.

**Rejected alternative:** Versioning alone with unrestricted DeleteObjectVersion access. Versioning alone permits authorized permanent version deletion.

**AWS references:** [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).

## Scenario 3: Single-AZ storage trade-off

**Requirement:** A dataset is the only copy of irreplaceable records and must survive loss of an AZ. Which choice is unsuitable as its sole storage location?

**Recommended design:** S3 One Zone-IA.

**Reason and boundary:** One Zone-IA stores data in one AZ and is not resilient to physical loss of that AZ. It suits reproducible data or appropriate secondary copies, not this sole-copy requirement.

**Rejected alternative:** S3 Standard. Standard stores data across multiple AZs.

**AWS references:** [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html).

## Scenario 4: Prevent public exposure

**Requirement:** A private application bucket must reject accidental public grants through bucket policies or ACLs. Which S3 control is specifically designed for that purpose?

**Recommended design:** S3 Block Public Access configured at the applicable account and bucket levels.

**Reason and boundary:** Block Public Access prevents public access according to its settings. It complements authenticated IAM access and does not replace least-privilege authorization.

**Rejected alternative:** A permissive public-read bucket policy. A public-read policy creates the exposure the requirement forbids.

**AWS references:** [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

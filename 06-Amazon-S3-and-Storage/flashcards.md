# Review Flashcards

## Card 01

**Question:** An S3 bucket must retain earlier object contents when an application overwrites an existing key. Which feature directly provides that history?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** S3 Versioning. Versioning retains multiple versions of an object key. A lifecycle policy may be needed to control noncurrent-version storage costs, and permanent version deletion still needs protection.

**AWS references:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html).

</details>

## Card 02

**Question:** Records require a fixed WORM retention period that must not be shortened or bypassed by users, including the account root user. Which S3 feature and mode fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** S3 Object Lock in compliance mode with the required retention period. Compliance-mode retention prevents protected versions from being overwritten or deleted during the retention period, including by root. Plan carefully because a test record can remain retained until expiry.

**AWS references:** [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).

</details>

## Card 03

**Question:** A dataset is the only copy of irreplaceable records and must survive loss of an AZ. Which choice is unsuitable as its sole storage location?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** S3 One Zone-IA. One Zone-IA stores data in one AZ and is not resilient to physical loss of that AZ. It suits reproducible data or appropriate secondary copies, not this sole-copy requirement.

**AWS references:** [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html).

</details>

## Card 04

**Question:** A private application bucket must reject accidental public grants through bucket policies or ACLs. Which S3 control is specifically designed for that purpose?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** S3 Block Public Access configured at the applicable account and bucket levels. Block Public Access prevents public access according to its settings. It complements authenticated IAM access and does not replace least-privilege authorization.

**AWS references:** [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

## Card 05

**Question:** A retained dataset is rarely read, but every retrieval must begin immediately without a restore job. Which storage decision follows the requirement?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Choose a suitable immediate-access class, such as S3 Glacier Instant Retrieval, after checking retrieval and minimum-duration charges. Glacier Instant Retrieval provides immediate access, whereas Flexible Retrieval and Deep Archive use restore workflows. Storage, request, retrieval, and minimum-duration costs all affect the choice.

**AWS references:** [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html).

</details>

## Card 06

**Question:** Records require a fixed WORM retention period that must not be shortened or bypassed by users, including the account root user. Which S3 feature and mode fits?

Why does this alternative fail: “Versioning alone with unrestricted DeleteObjectVersion access.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Versioning alone permits authorized permanent version deletion.

**AWS references:** [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).

</details>

## Card 07

**Question:** A dataset is the only copy of irreplaceable records and must survive loss of an AZ. Which choice is unsuitable as its sole storage location?

Why does this alternative fail: “S3 Standard.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Standard stores data across multiple AZs.

**AWS references:** [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html).

</details>

## Card 08

**Question:** A private application bucket must reject accidental public grants through bucket policies or ACLs. Which S3 control is specifically designed for that purpose?

Why does this alternative fail: “A permissive public-read bucket policy.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** A public-read policy creates the exposure the requirement forbids.

**AWS references:** [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

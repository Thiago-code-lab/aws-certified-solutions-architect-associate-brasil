# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 06-Q01 -->

An S3 bucket must retain earlier object contents when an application overwrites an existing key. Which feature directly provides that history?

A) A public-read bucket policy.

B) An S3 gateway endpoint alone.

C) A larger EC2 instance uploading the objects.

D) S3 Versioning.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Versioning retains multiple versions of an object key. A lifecycle policy may be needed to control noncurrent-version storage costs, and permanent version deletion still needs protection.

**Why the other options are incorrect:**

- **A:** Public read access does not retain earlier versions and is unnecessary here.
- **B:** An endpoint controls the network path rather than object version history.
- **C:** Uploader compute size does not change S3 version retention.

**AWS references:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html).

</details>

## Question 2

<!-- question-id: 06-Q02 -->

Records require a fixed WORM retention period that must not be shortened or bypassed by users, including the account root user. Which S3 feature and mode fits?

A) Versioning alone with unrestricted DeleteObjectVersion access.

B) Object Lock governance mode with bypass permission granted to administrators.

C) S3 Object Lock in compliance mode with the required retention period.

D) S3 Standard storage class without Object Lock.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Compliance-mode retention prevents protected versions from being overwritten or deleted during the retention period, including by root. Plan carefully because a test record can remain retained until expiry.

**Why the other options are incorrect:**

- **A:** Versioning alone permits authorized permanent version deletion.
- **B:** Governance retention can be bypassed by a principal with the relevant permission.
- **D:** A storage class is not a WORM retention control.

**AWS references:** [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).

</details>

## Question 3

<!-- question-id: 06-Q03 -->

A dataset is the only copy of irreplaceable records and must survive loss of an AZ. Which choice is unsuitable as its sole storage location?

A) S3 Standard.

B) S3 Standard-IA.

C) A suitable S3 Glacier multi-AZ storage class with retrieval requirements accounted for.

D) S3 One Zone-IA.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** One Zone-IA stores data in one AZ and is not resilient to physical loss of that AZ. It suits reproducible data or appropriate secondary copies, not this sole-copy requirement.

**Why the other options are incorrect:**

- **A:** Standard stores data across multiple AZs.
- **B:** Standard-IA uses multiple AZs; its access-cost model must still fit the workload.
- **C:** Multi-AZ archival storage can meet the stated failure scope when retrieval delays are acceptable.

**AWS references:** [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html).

</details>

## Question 4

<!-- question-id: 06-Q04 -->

A private application bucket must reject accidental public grants through bucket policies or ACLs. Which S3 control is specifically designed for that purpose?

A) S3 Block Public Access configured at the applicable account and bucket levels.

B) A permissive public-read bucket policy.

C) An EC2 security group attached to the bucket.

D) Disabling versioning.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Block Public Access prevents public access according to its settings. It complements authenticated IAM access and does not replace least-privilege authorization.

**Why the other options are incorrect:**

- **B:** A public-read policy creates the exposure the requirement forbids.
- **C:** S3 buckets do not use EC2 security groups as bucket access controls.
- **D:** Versioning settings do not block public authorization grants.

**AWS references:** [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

## Question 5

<!-- question-id: 06-Q05 -->

A retained dataset is rarely read, but every retrieval must begin immediately without a restore job. Which storage decision follows the requirement?

A) Choose S3 Glacier Deep Archive solely because its storage rate is low.

B) Assume all storage classes named Glacier have identical retrieval behavior.

C) Delete the data and regenerate it even though retention is mandatory.

D) Choose a suitable immediate-access class, such as S3 Glacier Instant Retrieval, after checking retrieval and minimum-duration charges.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Glacier Instant Retrieval provides immediate access, whereas Flexible Retrieval and Deep Archive use restore workflows. Storage, request, retrieval, and minimum-duration costs all affect the choice.

**Why the other options are incorrect:**

- **A:** Deep Archive does not meet the immediate-without-restore requirement.
- **B:** Glacier storage classes have different access characteristics.
- **C:** Deleting required retained data violates the stated requirement.

**AWS references:** [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

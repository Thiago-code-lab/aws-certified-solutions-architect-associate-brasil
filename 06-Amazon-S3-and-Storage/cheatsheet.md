# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Recover an overwritten object | S3 Versioning. | Versioning retains multiple versions of an object key. A lifecycle policy may be needed to control noncurrent-version storage costs, and permanent version deletion still needs protection. |
| Object retention | S3 Object Lock in compliance mode with the required retention period. | Compliance-mode retention prevents protected versions from being overwritten or deleted during the retention period, including by root. Plan carefully because a test record can remain retained until expiry. |
| Single-AZ storage trade-off | S3 One Zone-IA. | One Zone-IA stores data in one AZ and is not resilient to physical loss of that AZ. It suits reproducible data or appropriate secondary copies, not this sole-copy requirement. |
| Prevent public exposure | S3 Block Public Access configured at the applicable account and bucket levels. | Block Public Access prevents public access according to its settings. It complements authenticated IAM access and does not replace least-privilege authorization. |
| Archive retrieval requirements | Choose a suitable immediate-access class, such as S3 Glacier Instant Retrieval, after checking retrieval and minimum-duration charges. | Glacier Instant Retrieval provides immediate access, whereas Flexible Retrieval and Deep Archive use restore workflows. Storage, request, retrieval, and minimum-duration costs all affect the choice. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Recover an overwritten object:** Public read access does not retain earlier versions and is unnecessary here.
- **Object retention:** Versioning alone permits authorized permanent version deletion.
- **Single-AZ storage trade-off:** Standard stores data across multiple AZs.
- **Prevent public exposure:** A public-read policy creates the exposure the requirement forbids.
- **Archive retrieval requirements:** Deep Archive does not meet the immediate-without-restore requirement.

## AWS References

[S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html), [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html), [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html), [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

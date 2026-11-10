# Amazon S3 and Storage

## Overview

Choose S3 storage and protection features from access patterns, failure tolerance, retention, and authorization requirements. Versioning, Object Lock, storage classes, and private access solve different problems.

## Key Concepts

- **Recover an overwritten object:** Versioning retains multiple versions of an object key. A lifecycle policy may be needed to control noncurrent-version storage costs, and permanent version deletion still needs protection.
- **Object retention:** Compliance-mode retention prevents protected versions from being overwritten or deleted during the retention period, including by root. Plan carefully because a test record can remain retained until expiry.
- **Single-AZ storage trade-off:** One Zone-IA stores data in one AZ and is not resilient to physical loss of that AZ. It suits reproducible data or appropriate secondary copies, not this sole-copy requirement.
- **Prevent public exposure:** Block Public Access prevents public access according to its settings. It complements authenticated IAM access and does not replace least-privilege authorization.
- **Archive retrieval requirements:** Glacier Instant Retrieval provides immediate access, whereas Flexible Retrieval and Deep Archive use restore workflows. Storage, request, retrieval, and minimum-duration costs all affect the choice.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Recover an overwritten object:** S3 Versioning.
2. **Object retention:** S3 Object Lock in compliance mode with the required retention period.
3. **Single-AZ storage trade-off:** S3 One Zone-IA.
4. **Prevent public exposure:** S3 Block Public Access configured at the applicable account and bucket levels.
5. **Archive retrieval requirements:** Choose a suitable immediate-access class, such as S3 Glacier Instant Retrieval, after checking retrieval and minimum-duration charges.

## Common Pitfalls

- Public read access does not retain earlier versions and is unnecessary here.
- Versioning alone permits authorized permanent version deletion.
- Standard stores data across multiple AZs.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html), [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html), [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html), [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

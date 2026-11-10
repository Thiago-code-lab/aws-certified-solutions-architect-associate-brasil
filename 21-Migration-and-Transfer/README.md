# Migration and Transfer

## Overview

Distinguish database migration, server rehosting, online file synchronization, and managed file-transfer endpoints. Review current service eligibility and lifecycle notices before using a historical migration recommendation.

## Key Concepts

- **Database migration and conversion:** DMS includes schema-conversion and data-migration capabilities, but support and conversion gaps depend on the source and target. Replication, application compatibility, and cutover must be validated separately.
- **Server rehosting:** MGN replicates server blocks and supports test launches and cutover for rehosting. Rehosting is not the same as database-engine conversion or application refactoring.
- **Online file transfer:** DataSync automates transfers between supported file or object storage systems and AWS storage. Source support, permissions, connectivity, and task settings still need verification.
- **Keep SFTP clients:** Transfer Family provides managed file-transfer protocol endpoints, including SFTP. S3 storage is not itself an SFTP server, and DataSync serves a different transfer model.
- **Snowball availability caveat:** AWS service availability notices govern deployment eligibility. The exam scope list and historical offline-transfer patterns do not override customer or lifecycle restrictions.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Database migration and conversion:** Assess and convert the schema using suitable DMS Schema Conversion or AWS SCT capabilities, then configure supported full-load and CDC replication with cutover validation.
2. **Server rehosting:** AWS Transform MGN, formerly AWS Application Migration Service.
3. **Online file transfer:** AWS DataSync.
4. **Keep SFTP clients:** AWS Transfer Family configured with a supported storage backend and authentication design.
5. **Snowball availability caveat:** No. Snowball Edge is closed to new customers, and AWS has announced commercial-Region device support ending December 31, 2026; evaluate currently available transfer alternatives.

## Common Pitfalls

- Conversion support is not universal and incompatible objects can require changes.
- Text analysis does not replicate server disks.
- DNS failover does not copy a file dataset.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html), [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html), [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html), [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html), [AWS Snowball availability notice](https://aws.amazon.com/snowball/), [Snowball availability history](https://docs.aws.amazon.com/snowball/latest/developer-guide/doc-history.html), [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

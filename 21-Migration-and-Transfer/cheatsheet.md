# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Database migration and conversion | Assess and convert the schema using suitable DMS Schema Conversion or AWS SCT capabilities, then configure supported full-load and CDC replication with cutover validation. | DMS includes schema-conversion and data-migration capabilities, but support and conversion gaps depend on the source and target. Replication, application compatibility, and cutover must be validated separately. |
| Server rehosting | AWS Transform MGN, formerly AWS Application Migration Service. | MGN replicates server blocks and supports test launches and cutover for rehosting. Rehosting is not the same as database-engine conversion or application refactoring. |
| Online file transfer | AWS DataSync. | DataSync automates transfers between supported file or object storage systems and AWS storage. Source support, permissions, connectivity, and task settings still need verification. |
| Keep SFTP clients | AWS Transfer Family configured with a supported storage backend and authentication design. | Transfer Family provides managed file-transfer protocol endpoints, including SFTP. S3 storage is not itself an SFTP server, and DataSync serves a different transfer model. |
| Snowball availability caveat | No. Snowball Edge is closed to new customers, and AWS has announced commercial-Region device support ending December 31, 2026; evaluate currently available transfer alternatives. | AWS service availability notices govern deployment eligibility. The exam scope list and historical offline-transfer patterns do not override customer or lifecycle restrictions. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Database migration and conversion:** Conversion support is not universal and incompatible objects can require changes.
- **Server rehosting:** Text analysis does not replicate server disks.
- **Online file transfer:** DNS failover does not copy a file dataset.
- **Keep SFTP clients:** The S3 API endpoint does not directly provide the SFTP protocol.
- **Snowball availability caveat:** Exam scope is not a service-ordering entitlement.

## AWS References

[AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html), [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html), [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html), [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html), [AWS Snowball availability notice](https://aws.amazon.com/snowball/), [Snowball availability history](https://docs.aws.amazon.com/snowball/latest/developer-guide/doc-history.html), [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

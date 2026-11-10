# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Survive loss of a web AZ | Deploy replaceable web instances across multiple AZs behind a multi-AZ ALB and keep required state outside individual instances. | The unprotected component is the web tier. Database redundancy does not make single-AZ application compute available during that AZ failure. |
| Independent order subscribers | Publish to SNS and subscribe a separate SQS queue for each subsystem, with retry-safe consumers. | Separate subscribed queues provide independent buffering. Successful publication, correct subscription policies, retry behavior, and idempotent consumers are necessary parts of the design. |
| Private origin for a public CDN | Use CloudFront OAC and a scoped bucket policy while retaining appropriate S3 public-access blocking. | Viewer access and origin access are separate boundaries. OAC plus a distribution-scoped bucket policy lets CloudFront retrieve private origin objects without making the bucket public. |
| Immediate database read after write | Read the known order key from the base table using a strongly consistent read where required. | The base table supports strongly consistent reads. GSI reads do not; a faster caller or cache does not turn an eventually consistent read into a strong read. |
| Select DR from business constraints | Pilot light. | Pilot light keeps core recovery components such as data replication active, then brings up the remaining workload for recovery. The measured RTO depends on that activation path. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Survive loss of a web AZ:** Additional database readers do not remove the web tier AZ dependency.
- **Independent order subscribers:** One competing-consumer queue distributes work rather than independently copying every event to each subsystem.
- **Private origin for a public CDN:** An obscure publicly readable bucket is still directly accessible.
- **Immediate database read after write:** Strongly consistent GSI reads are not supported.
- **Select DR from business constraints:** The stem says the application tier is not already running as a fully functioning standby.

## AWS References

[Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [CloudFront origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html), [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html), [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

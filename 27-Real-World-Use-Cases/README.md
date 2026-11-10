# Real-World Use Cases

## Overview

Apply service distinctions to concrete application scenarios. Identify the unprotected failure domain, required data semantics, consumer independence, and origin-access boundaries before choosing a design.

## Key Concepts

- **Survive loss of a web AZ:** The unprotected component is the web tier. Database redundancy does not make single-AZ application compute available during that AZ failure.
- **Independent order subscribers:** Separate subscribed queues provide independent buffering. Successful publication, correct subscription policies, retry behavior, and idempotent consumers are necessary parts of the design.
- **Private origin for a public CDN:** Viewer access and origin access are separate boundaries. OAC plus a distribution-scoped bucket policy lets CloudFront retrieve private origin objects without making the bucket public.
- **Immediate database read after write:** The base table supports strongly consistent reads. GSI reads do not; a faster caller or cache does not turn an eventually consistent read into a strong read.
- **Select DR from business constraints:** Pilot light keeps core recovery components such as data replication active, then brings up the remaining workload for recovery. The measured RTO depends on that activation path.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Survive loss of a web AZ:** Deploy replaceable web instances across multiple AZs behind a multi-AZ ALB and keep required state outside individual instances.
2. **Independent order subscribers:** Publish to SNS and subscribe a separate SQS queue for each subsystem, with retry-safe consumers.
3. **Private origin for a public CDN:** Use CloudFront OAC and a scoped bucket policy while retaining appropriate S3 public-access blocking.
4. **Immediate database read after write:** Read the known order key from the base table using a strongly consistent read where required.
5. **Select DR from business constraints:** Pilot light.

## Common Pitfalls

- Additional database readers do not remove the web tier AZ dependency.
- One competing-consumer queue distributes work rather than independently copying every event to each subsystem.
- An obscure publicly readable bucket is still directly accessible.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [CloudFront origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html), [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html), [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

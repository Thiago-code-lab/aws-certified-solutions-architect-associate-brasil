# Review Flashcards

## Card 01

**Question:** A web tier runs in one AZ, while its database already has suitable Multi-AZ protection. The business requires the web tier to survive an AZ outage. Which change addresses the missing protection?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Deploy replaceable web instances across multiple AZs behind a multi-AZ ALB and keep required state outside individual instances. The unprotected component is the web tier. Database redundancy does not make single-AZ application compute available during that AZ failure.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

</details>

## Card 02

**Question:** Inventory and invoicing must each receive every accepted order, even if one subsystem is temporarily unavailable. Which design isolates their processing backlogs?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Publish to SNS and subscribe a separate SQS queue for each subsystem, with retry-safe consumers. Separate subscribed queues provide independent buffering. Successful publication, correct subscription policies, retry behavior, and idempotent consumers are necessary parts of the design.

**AWS references:** [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).

</details>

## Card 03

**Question:** Customers must download public website assets through CloudFront, while direct unauthenticated access to the regular S3 bucket origin must remain blocked. Which configuration fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Use CloudFront OAC and a scoped bucket policy while retaining appropriate S3 public-access blocking. Viewer access and origin access are separate boundaries. OAC plus a distribution-scoped bucket policy lets CloudFront retrieve private origin objects without making the bucket public.

**AWS references:** [CloudFront origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html), [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html).

</details>

## Card 04

**Question:** A DynamoDB checkout workflow must confirm the latest committed order state immediately after its write. The current path reads an eventually consistent GSI. Which change directly addresses consistency?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Read the known order key from the base table using a strongly consistent read where required. The base table supports strongly consistent reads. GSI reads do not; a faster caller or cache does not turn an eventually consistent read into a strong read.

**AWS references:** [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

</details>

## Card 05

**Question:** A recovery design replicates critical data to another Region, but application servers there are not running. Recovery requires deploying or activating the application tier. Which pattern is closest?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Pilot light. Pilot light keeps core recovery components such as data replication active, then brings up the remaining workload for recovery. The measured RTO depends on that activation path.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

</details>

## Card 06

**Question:** Inventory and invoicing must each receive every accepted order, even if one subsystem is temporarily unavailable. Which design isolates their processing backlogs?

Why does this alternative fail: “Use one SQS queue and assume both competing consumers always receive every message.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** One competing-consumer queue distributes work rather than independently copying every event to each subsystem.

**AWS references:** [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).

</details>

## Card 07

**Question:** Customers must download public website assets through CloudFront, while direct unauthenticated access to the regular S3 bucket origin must remain blocked. Which configuration fits?

Why does this alternative fail: “Grant public read access to the bucket and hide its name in the HTML.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** An obscure publicly readable bucket is still directly accessible.

**AWS references:** [CloudFront origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html), [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html).

</details>

## Card 08

**Question:** A DynamoDB checkout workflow must confirm the latest committed order state immediately after its write. The current path reads an eventually consistent GSI. Which change directly addresses consistency?

Why does this alternative fail: “Set ConsistentRead on the GSI and assume it is supported.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Strongly consistent GSI reads are not supported.

**AWS references:** [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

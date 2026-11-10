# Review Flashcards

## Card 01

**Question:** A relational database needs managed AZ failover. The chosen deployment is an RDS Multi-AZ DB instance deployment; extra read capacity is not required. Which feature is the direct fit?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The synchronous standby and managed failover of that Multi-AZ DB instance deployment. This specifies the deployment type and availability objective. A Multi-AZ DB instance standby supports managed failover; an asynchronous read replica primarily provides another read or recovery copy with different semantics.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html).

</details>

## Card 02

**Question:** A stateless web application must remain available when one AZ fails. Which design directly addresses that failure scope?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** An ALB with application instances across multiple AZs, working health checks, externalized state, and sufficient surviving capacity. Multiple AZs and appropriately placed state reduce the single-AZ dependency. Recovery copies and static addressing do not by themselves keep a sole failed instance serving requests.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 03

**Question:** A VPC workload needs same-Region S3 access without NAT or public internet routing. Which choice supplies a route-table-based private path?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** An S3 gateway endpoint with the required routes and appropriate endpoint, bucket, and IAM policies. A gateway endpoint supports S3 access through VPC route tables without NAT or an internet gateway for that traffic. Authorization remains a separate requirement.

**AWS references:** [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html).

</details>

## Card 04

**Question:** An API accepts jobs durably and workers can process them asynchronously. It needs to absorb traffic bursts without requiring every worker to be available at acceptance time. Which service fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Amazon SQS with suitable producer error handling and retry-safe consumers. SQS decouples job acceptance from consumer processing. Applications still handle send failures, retention, retries, duplicate processing, and backlog growth.

**AWS references:** [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html).

</details>

## Card 05

**Question:** A learner selects a policy allowing every S3 action on every bucket when the scenario requires reading only one object prefix. Which correction addresses the actual authorization requirement?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Allow the required object-read action only on the specified object-prefix resources, accounting for any separately required bucket actions. Least privilege matches allowed actions and resource scope to the requirement. Bucket-level operations, if genuinely needed, use appropriate bucket resource scopes rather than indiscriminately broad object permissions.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

</details>

## Card 06

**Question:** A stateless web application must remain available when one AZ fails. Which design directly addresses that failure scope?

Why does this alternative fail: “One larger EC2 instance with a daily AMI.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** An AMI supports recovery but does not keep that one instance available during AZ failure.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

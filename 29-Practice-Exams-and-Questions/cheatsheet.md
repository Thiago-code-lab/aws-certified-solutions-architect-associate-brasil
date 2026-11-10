# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| RDS failover question clarified | The synchronous standby and managed failover of that Multi-AZ DB instance deployment. | This specifies the deployment type and availability objective. A Multi-AZ DB instance standby supports managed failover; an asynchronous read replica primarily provides another read or recovery copy with different semantics. |
| Resilient application question clarified | An ALB with application instances across multiple AZs, working health checks, externalized state, and sufficient surviving capacity. | Multiple AZs and appropriately placed state reduce the single-AZ dependency. Recovery copies and static addressing do not by themselves keep a sole failed instance serving requests. |
| Private S3 question clarified | An S3 gateway endpoint with the required routes and appropriate endpoint, bucket, and IAM policies. | A gateway endpoint supports S3 access through VPC route tables without NAT or an internet gateway for that traffic. Authorization remains a separate requirement. |
| Queue decoupling question clarified | Amazon SQS with suitable producer error handling and retry-safe consumers. | SQS decouples job acceptance from consumer processing. Applications still handle send failures, retention, retries, duplicate processing, and backlog growth. |
| IAM review question made concrete | Allow the required object-read action only on the specified object-prefix resources, accounting for any separately required bucket actions. | Least privilege matches allowed actions and resource scope to the requirement. Bucket-level operations, if genuinely needed, use appropriate bucket resource scopes rather than indiscriminately broad object permissions. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **RDS failover question clarified:** An ordinary read replica does not provide the identical synchronous standby failover feature.
- **Resilient application question clarified:** An AMI supports recovery but does not keep that one instance available during AZ failure.
- **Private S3 question clarified:** NAT violates the explicit network-path constraint.
- **Queue decoupling question clarified:** Shared file storage does not provide the managed queue semantics requested.
- **IAM review question made concrete:** Managed policy status does not make broad permissions least privilege for a narrow scenario.

## AWS References

[RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html), [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

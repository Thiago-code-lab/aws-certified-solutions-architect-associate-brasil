# Practice Exams and Questions

## Overview

Practice explicit requirements and compare alternatives using documented AWS behavior. Keep an error log, revisit incorrect reasoning, and distinguish practice-set distribution from official exam weights.

## Key Concepts

- **RDS failover question clarified:** This specifies the deployment type and availability objective. A Multi-AZ DB instance standby supports managed failover; an asynchronous read replica primarily provides another read or recovery copy with different semantics.
- **Resilient application question clarified:** Multiple AZs and appropriately placed state reduce the single-AZ dependency. Recovery copies and static addressing do not by themselves keep a sole failed instance serving requests.
- **Private S3 question clarified:** A gateway endpoint supports S3 access through VPC route tables without NAT or an internet gateway for that traffic. Authorization remains a separate requirement.
- **Queue decoupling question clarified:** SQS decouples job acceptance from consumer processing. Applications still handle send failures, retention, retries, duplicate processing, and backlog growth.
- **IAM review question made concrete:** Least privilege matches allowed actions and resource scope to the requirement. Bucket-level operations, if genuinely needed, use appropriate bucket resource scopes rather than indiscriminately broad object permissions.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **RDS failover question clarified:** The synchronous standby and managed failover of that Multi-AZ DB instance deployment.
2. **Resilient application question clarified:** An ALB with application instances across multiple AZs, working health checks, externalized state, and sufficient surviving capacity.
3. **Private S3 question clarified:** An S3 gateway endpoint with the required routes and appropriate endpoint, bucket, and IAM policies.
4. **Queue decoupling question clarified:** Amazon SQS with suitable producer error handling and retry-safe consumers.
5. **IAM review question made concrete:** Allow the required object-read action only on the specified object-prefix resources, accounting for any separately required bucket actions.

## Common Pitfalls

- An ordinary read replica does not provide the identical synchronous standby failover feature.
- An AMI supports recovery but does not keep that one instance available during AZ failure.
- NAT violates the explicit network-path constraint.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

Additional review tools: [mini practice exams](./mini-practice-exams-by-domain.md), [error log](./error-log.md), and [final review plan](./final-review-saa-c03.md).

## Additional Study

[RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html), [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

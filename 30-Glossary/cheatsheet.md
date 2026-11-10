# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| RPO terminology | Recovery point objective, or RPO. | RPO expresses the acceptable data-loss window. It guides replication and backup requirements rather than the time needed to return the application to service. |
| RTO terminology | Recovery time objective, or RTO. | RTO expresses the recovery-time target for the workload. Recovery testing should measure the end-to-end duration, including dependencies and application validation. |
| Durability versus availability | Durability concerns retaining data; availability concerns being able to access the service when needed. | Data can remain intact during a temporary access outage. Architecture must evaluate both preservation and access requirements rather than treating one as proof of the other. |
| Horizontal versus vertical scaling | Horizontal scaling, or scaling out. | Horizontal scaling adds more workers or instances. Vertical scaling changes the capacity of an individual resource; neither term alone proves application resilience. |
| Idempotency terminology | Idempotent processing of the business operation. | Idempotency makes a repeated operation safe with respect to its intended side effect. It does not require the transport to stop delivering duplicate events. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **RPO terminology:** RTO expresses the acceptable recovery duration.
- **RTO terminology:** RPO concerns tolerable data loss rather than recovery duration.
- **Durability versus availability:** The two properties describe different aspects of service behavior.
- **Horizontal versus vertical scaling:** Scaling up enlarges an individual resource rather than adding instances.
- **Idempotency terminology:** Ordering and idempotency are different properties.

## AWS References

[Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html), [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html), [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

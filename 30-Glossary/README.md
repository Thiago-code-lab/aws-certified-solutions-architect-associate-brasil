# Glossary

## Overview

Use architectural terms precisely. RPO and RTO, durability and availability, scaling directions, and idempotency describe different properties and must not be used as substitutes for one another.

## Key Concepts

- **RPO terminology:** RPO expresses the acceptable data-loss window. It guides replication and backup requirements rather than the time needed to return the application to service.
- **RTO terminology:** RTO expresses the recovery-time target for the workload. Recovery testing should measure the end-to-end duration, including dependencies and application validation.
- **Durability versus availability:** Data can remain intact during a temporary access outage. Architecture must evaluate both preservation and access requirements rather than treating one as proof of the other.
- **Horizontal versus vertical scaling:** Horizontal scaling adds more workers or instances. Vertical scaling changes the capacity of an individual resource; neither term alone proves application resilience.
- **Idempotency terminology:** Idempotency makes a repeated operation safe with respect to its intended side effect. It does not require the transport to stop delivering duplicate events.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **RPO terminology:** Recovery point objective, or RPO.
2. **RTO terminology:** Recovery time objective, or RTO.
3. **Durability versus availability:** Durability concerns retaining data; availability concerns being able to access the service when needed.
4. **Horizontal versus vertical scaling:** Horizontal scaling, or scaling out.
5. **Idempotency terminology:** Idempotent processing of the business operation.

## Common Pitfalls

- RTO expresses the acceptable recovery duration.
- RPO concerns tolerable data loss rather than recovery duration.
- The two properties describe different aspects of service behavior.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html), [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html), [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

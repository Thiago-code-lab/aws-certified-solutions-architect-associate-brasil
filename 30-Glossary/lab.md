# Guided Lab

## Objective

Test architectural vocabulary with concrete counterexamples.

## Services Used

Module glossary, recovery objective documentation, and service behavior references.

## Expected Cost Range

Offline concept exercise. No AWS resource creation is required.

## Step-by-Step Instructions

1. Write separate definitions for availability, durability, RPO, RTO, horizontal scaling, vertical scaling, and idempotency.
2. Describe data that is durable but temporarily unavailable and explain why the two properties differ.
3. Given a retained recovery point and measured restoration time, calculate the observed data-loss window and recovery duration separately.
4. Describe adding application instances versus enlarging one instance.
5. Walk through delivery of the same order event twice and describe a duplicate-safe business operation.
6. Check each explanation against the linked primary documentation and revise any definition that conflates different concepts.

## Validation

- RPO and RTO are not reversed.
- Availability is not equated with historical recoverability.
- Idempotency is not confused with ordering or duplicate-free transport.

## Cleanup

1. Keep the corrected definitions and counterexamples.
2. No cloud resources were created.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

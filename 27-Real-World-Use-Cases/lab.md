# Guided Lab

## Objective

Review a business architecture against failure, consistency, and access requirements.

## Services Used

ALB, SQS/SNS, S3/CloudFront, and DynamoDB design documentation.

## Expected Cost Range

Scenario design exercise. No application fleet, database, or CDN distribution needs to be created.

## Step-by-Step Instructions

1. Choose the order-processing scenario in this module and list web availability, accepted-job durability, consumer independence, and read consistency requirements.
2. Draw multi-AZ web compute with an appropriate load balancer and externalized application state.
3. Draw independent consumer queues behind fan-out and mark acknowledgement, duplicate handling, and backlog monitoring points.
4. Choose the authoritative order-data read path and mark where a stale read would violate the requirement.
5. If static assets are included, draw private S3 origin access separately from public CloudFront viewer access.
6. Walk through loss of one web instance, one consumer, and one AZ; record which requirements still hold and which assumptions require testing.

## Validation

- Each component is tied to a stated requirement.
- No queue, cache, key service, or DNS record is treated as a universal replacement for another service category.
- The diagram records real failure boundaries rather than generic resilience claims.

## Cleanup

1. Keep the architecture decisions and unresolved assumptions.
2. No cloud resources are required for this design exercise.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [CloudFront origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html), [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

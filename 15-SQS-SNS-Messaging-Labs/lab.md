# Guided Lab

## Objective

Demonstrate independent SNS-to-SQS fan-out.

## Services Used

SNS topic and two SQS Standard queues.

## Expected Cost Range

SNS/SQS requests, retained messages, encryption, and optional logs can incur charges. Use a few small synthetic messages.

## Step-by-Step Instructions

1. Create one lab SNS Standard topic and two lab SQS Standard queues.
2. Subscribe each queue to the topic and configure each queue policy to allow only the intended topic to send messages.
3. Publish one synthetic order message containing a unique business operation identifier.
4. Poll both queues and verify each receives its own copy; inspect whether the SNS envelope is enabled or raw delivery is selected.
5. Delete the processed message from only the first queue and verify the second queue processing remains independent.
6. Allow a received test message visibility timeout to expire without deletion, then poll again and explain why consumers must handle repeat processing safely.

## Validation

- Both queues receive the published event.
- Deleting from one queue does not remove the other queue copy.
- The observed retry is not misrepresented as exactly-once business processing.

## Cleanup

1. Remove the subscriptions, delete both lab queues, and delete the topic.
2. Delete optional lab logs or keys only if they were created exclusively for this exercise.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

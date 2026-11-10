# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Standard queue duplicates | Use an idempotency key and an atomic or otherwise safe duplicate-detection operation before committing the order side effect. | Standard queues provide at-least-once delivery. The business operation must safely handle repeated delivery; successful processing and message acknowledgement are separate steps. |
| FIFO ordering scope | Use the customer identifier as MessageGroupId and appropriate deduplication identifiers. | FIFO ordering is scoped to a message group. Separate customer groups allow independent processing while preserving each group order. |
| FIFO deduplication is bounded | SQS suppresses duplicate sends in that interval, but the application must still handle retried processing safely. | FIFO send deduplication operates within a documented five-minute interval. It is not an unlimited transaction guarantee for downstream business effects or failed consumer processing. |
| Independent fan-out consumers | An SNS topic with a separate subscribed SQS queue for each consumer, with appropriate queue access policies. | SNS fan-out can place an event on each subscribed queue. Separate queues preserve independent buffering and retry behavior; duplicates still require safe consumer design. |
| Workflow orchestration | An appropriate AWS Step Functions Standard workflow. | Step Functions models workflow state and task transitions, with supported callback integrations for Standard workflows. An event router can start a workflow but is not itself the full orchestrator. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Standard queue duplicates:** Standard queues can deliver duplicate messages.
- **FIFO ordering scope:** Changing groups per update removes the requested per-customer ordering boundary.
- **FIFO deduplication is bounded:** A queue does not atomically coordinate arbitrary external side effects.
- **Independent fan-out consumers:** Competing consumers on one queue divide messages rather than each receiving every event.
- **Workflow orchestration:** A bucket policy controls access, not workflow execution state.

## AWS References

[SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html), [SQS FIFO delivery logic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html), [SQS FIFO deduplication](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html), [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html), [EventBridge event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

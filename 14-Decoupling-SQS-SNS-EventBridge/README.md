# Decoupling: SQS, SNS, and EventBridge

## Overview

Separate queue buffering, fan-out, event routing, and workflow orchestration. Design retry-safe business operations even when the transport offers ordering or bounded deduplication.

## Key Concepts

- **Standard queue duplicates:** Standard queues provide at-least-once delivery. The business operation must safely handle repeated delivery; successful processing and message acknowledgement are separate steps.
- **FIFO ordering scope:** FIFO ordering is scoped to a message group. Separate customer groups allow independent processing while preserving each group order.
- **FIFO deduplication is bounded:** FIFO send deduplication operates within a documented five-minute interval. It is not an unlimited transaction guarantee for downstream business effects or failed consumer processing.
- **Independent fan-out consumers:** SNS fan-out can place an event on each subscribed queue. Separate queues preserve independent buffering and retry behavior; duplicates still require safe consumer design.
- **Workflow orchestration:** Step Functions models workflow state and task transitions, with supported callback integrations for Standard workflows. An event router can start a workflow but is not itself the full orchestrator.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Standard queue duplicates:** Use an idempotency key and an atomic or otherwise safe duplicate-detection operation before committing the order side effect.
2. **FIFO ordering scope:** Use the customer identifier as MessageGroupId and appropriate deduplication identifiers.
3. **FIFO deduplication is bounded:** SQS suppresses duplicate sends in that interval, but the application must still handle retried processing safely.
4. **Independent fan-out consumers:** An SNS topic with a separate subscribed SQS queue for each consumer, with appropriate queue access policies.
5. **Workflow orchestration:** An appropriate AWS Step Functions Standard workflow.

## Common Pitfalls

- Standard queues can deliver duplicate messages.
- Changing groups per update removes the requested per-customer ordering boundary.
- A queue does not atomically coordinate arbitrary external side effects.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html), [SQS FIFO delivery logic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html), [SQS FIFO deduplication](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html), [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html), [EventBridge event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

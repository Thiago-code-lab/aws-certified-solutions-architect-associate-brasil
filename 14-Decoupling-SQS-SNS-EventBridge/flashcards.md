# Review Flashcards

## Card 01

**Question:** An order worker uses an SQS Standard queue. A message can be delivered again after a retry. Which application design addresses duplicate side effects?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Use an idempotency key and an atomic or otherwise safe duplicate-detection operation before committing the order side effect. Standard queues provide at-least-once delivery. The business operation must safely handle repeated delivery; successful processing and message acknowledgement are separate steps.

**AWS references:** [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

</details>

## Card 02

**Question:** Updates for each customer must remain ordered, while different customers can process in parallel. Which SQS FIFO design matches that requirement?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Use the customer identifier as MessageGroupId and appropriate deduplication identifiers. FIFO ordering is scoped to a message group. Separate customer groups allow independent processing while preserving each group order.

**AWS references:** [SQS FIFO delivery logic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html), [SQS FIFO deduplication](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html).

</details>

## Card 03

**Question:** A producer retries an SQS FIFO SendMessage call with the same deduplication ID within the deduplication interval. Which conclusion is justified?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** SQS suppresses duplicate sends in that interval, but the application must still handle retried processing safely. FIFO send deduplication operates within a documented five-minute interval. It is not an unlimited transaction guarantee for downstream business effects or failed consumer processing.

**AWS references:** [SQS FIFO deduplication](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html), [SQS FIFO delivery logic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html), [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

</details>

## Card 04

**Question:** Billing and shipping must each receive every order event and process independently with durable buffering. Which design fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** An SNS topic with a separate subscribed SQS queue for each consumer, with appropriate queue access policies. SNS fan-out can place an event on each subscribed queue. Separate queues preserve independent buffering and retry behavior; duplicates still require safe consumer design.

**AWS references:** [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).

</details>

## Card 05

**Question:** Order fulfillment needs an explicit sequence of tasks, branching, retries, and a human approval callback. Which service is designed to orchestrate such a workflow?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** An appropriate AWS Step Functions Standard workflow. Step Functions models workflow state and task transitions, with supported callback integrations for Standard workflows. An event router can start a workflow but is not itself the full orchestrator.

**AWS references:** [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html), [EventBridge event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html).

</details>

## Card 06

**Question:** Updates for each customer must remain ordered, while different customers can process in parallel. Which SQS FIFO design matches that requirement?

Why does this alternative fail: “Use a random MessageGroupId for every update to the same customer.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Changing groups per update removes the requested per-customer ordering boundary.

**AWS references:** [SQS FIFO delivery logic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html), [SQS FIFO deduplication](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html).

</details>

## Card 07

**Question:** A producer retries an SQS FIFO SendMessage call with the same deduplication ID within the deduplication interval. Which conclusion is justified?

Why does this alternative fail: “Every external payment side effect is guaranteed to happen exactly once forever.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** A queue does not atomically coordinate arbitrary external side effects.

**AWS references:** [SQS FIFO deduplication](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html), [SQS FIFO delivery logic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html), [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

</details>

## Card 08

**Question:** Billing and shipping must each receive every order event and process independently with durable buffering. Which design fits?

Why does this alternative fail: “One SQS queue with competing billing and shipping consumers, assuming each gets every message.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Competing consumers on one queue divide messages rather than each receiving every event.

**AWS references:** [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

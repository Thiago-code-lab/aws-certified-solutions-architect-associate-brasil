# Use Cases

## Scenario 1: Standard queue duplicates

**Requirement:** An order worker uses an SQS Standard queue. A message can be delivered again after a retry. Which application design addresses duplicate side effects?

**Recommended design:** Use an idempotency key and an atomic or otherwise safe duplicate-detection operation before committing the order side effect.

**Reason and boundary:** Standard queues provide at-least-once delivery. The business operation must safely handle repeated delivery; successful processing and message acknowledgement are separate steps.

**Rejected alternative:** Assume a Standard queue guarantees each message is received exactly once. Standard queues can deliver duplicate messages.

**AWS references:** [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

## Scenario 2: FIFO ordering scope

**Requirement:** Updates for each customer must remain ordered, while different customers can process in parallel. Which SQS FIFO design matches that requirement?

**Recommended design:** Use the customer identifier as MessageGroupId and appropriate deduplication identifiers.

**Reason and boundary:** FIFO ordering is scoped to a message group. Separate customer groups allow independent processing while preserving each group order.

**Rejected alternative:** Use a random MessageGroupId for every update to the same customer. Changing groups per update removes the requested per-customer ordering boundary.

**AWS references:** [SQS FIFO delivery logic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html), [SQS FIFO deduplication](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html).

## Scenario 3: FIFO deduplication is bounded

**Requirement:** A producer retries an SQS FIFO SendMessage call with the same deduplication ID within the deduplication interval. Which conclusion is justified?

**Recommended design:** SQS suppresses duplicate sends in that interval, but the application must still handle retried processing safely.

**Reason and boundary:** FIFO send deduplication operates within a documented five-minute interval. It is not an unlimited transaction guarantee for downstream business effects or failed consumer processing.

**Rejected alternative:** Every external payment side effect is guaranteed to happen exactly once forever. A queue does not atomically coordinate arbitrary external side effects.

**AWS references:** [SQS FIFO deduplication](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html), [SQS FIFO delivery logic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html), [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

## Scenario 4: Independent fan-out consumers

**Requirement:** Billing and shipping must each receive every order event and process independently with durable buffering. Which design fits?

**Recommended design:** An SNS topic with a separate subscribed SQS queue for each consumer, with appropriate queue access policies.

**Reason and boundary:** SNS fan-out can place an event on each subscribed queue. Separate queues preserve independent buffering and retry behavior; duplicates still require safe consumer design.

**Rejected alternative:** One SQS queue with competing billing and shipping consumers, assuming each gets every message. Competing consumers on one queue divide messages rather than each receiving every event.

**AWS references:** [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

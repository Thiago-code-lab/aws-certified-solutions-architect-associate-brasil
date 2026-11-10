# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 14-Q01 -->

An order worker uses an SQS Standard queue. A message can be delivered again after a retry. Which application design addresses duplicate side effects?

A) Use an idempotency key and an atomic or otherwise safe duplicate-detection operation before committing the order side effect.

B) Assume a Standard queue guarantees each message is received exactly once.

C) Delete the message before attempting the business operation, regardless of success.

D) Add a second queue consumer and assume that eliminates duplicates.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Standard queues provide at-least-once delivery. The business operation must safely handle repeated delivery; successful processing and message acknowledgement are separate steps.

**Why the other options are incorrect:**

- **B:** Standard queues can deliver duplicate messages.
- **C:** Premature deletion can lose work if processing subsequently fails.
- **D:** Additional consumers increase parallelism, not exactly-once business semantics.

**AWS references:** [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

</details>

## Question 2

<!-- question-id: 14-Q02 -->

Updates for each customer must remain ordered, while different customers can process in parallel. Which SQS FIFO design matches that requirement?

A) Use a random MessageGroupId for every update to the same customer.

B) Put every customer in one global group to maximize independent customer parallelism.

C) Use the customer identifier as MessageGroupId and appropriate deduplication identifiers.

D) Use a Standard queue and assume strict ordering is guaranteed.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** FIFO ordering is scoped to a message group. Separate customer groups allow independent processing while preserving each group order.

**Why the other options are incorrect:**

- **A:** Changing groups per update removes the requested per-customer ordering boundary.
- **B:** One global group serializes unrelated customer work.
- **D:** Standard queues do not provide strict FIFO ordering.

**AWS references:** [SQS FIFO delivery logic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html), [SQS FIFO deduplication](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html).

</details>

## Question 3

<!-- question-id: 14-Q03 -->

A producer retries an SQS FIFO SendMessage call with the same deduplication ID within the deduplication interval. Which conclusion is justified?

A) Every external payment side effect is guaranteed to happen exactly once forever.

B) Consumer failure can never make a message visible again.

C) The deduplication ID permanently prevents all future messages with that value.

D) SQS suppresses duplicate sends in that interval, but the application must still handle retried processing safely.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** FIFO send deduplication operates within a documented five-minute interval. It is not an unlimited transaction guarantee for downstream business effects or failed consumer processing.

**Why the other options are incorrect:**

- **A:** A queue does not atomically coordinate arbitrary external side effects.
- **B:** Visibility timeout and processing failures can require another processing attempt.
- **C:** Deduplication is bounded by the interval, not permanent.

**AWS references:** [SQS FIFO deduplication](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html), [SQS FIFO delivery logic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html), [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

</details>

## Question 4

<!-- question-id: 14-Q04 -->

Billing and shipping must each receive every order event and process independently with durable buffering. Which design fits?

A) An SNS topic with a separate subscribed SQS queue for each consumer, with appropriate queue access policies.

B) One SQS queue with competing billing and shipping consumers, assuming each gets every message.

C) One shared EBS volume used as a notification bus.

D) An ALB listener expected to retain events until consumers return.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** SNS fan-out can place an event on each subscribed queue. Separate queues preserve independent buffering and retry behavior; duplicates still require safe consumer design.

**Why the other options are incorrect:**

- **B:** Competing consumers on one queue divide messages rather than each receiving every event.
- **C:** EBS is not an SNS-style notification broker.
- **D:** An ALB is not a durable asynchronous event queue.

**AWS references:** [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).

</details>

## Question 5

<!-- question-id: 14-Q05 -->

Order fulfillment needs an explicit sequence of tasks, branching, retries, and a human approval callback. Which service is designed to orchestrate such a workflow?

A) An S3 bucket policy alone.

B) A NAT gateway.

C) An appropriate AWS Step Functions Standard workflow.

D) An EventBridge routing rule alone, with no workflow state machine.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Step Functions models workflow state and task transitions, with supported callback integrations for Standard workflows. An event router can start a workflow but is not itself the full orchestrator.

**Why the other options are incorrect:**

- **A:** A bucket policy controls access, not workflow execution state.
- **B:** NAT translates network connections and does not orchestrate tasks.
- **D:** An event-matching rule alone does not implement the requested stateful task sequence.

**AWS references:** [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html), [EventBridge event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

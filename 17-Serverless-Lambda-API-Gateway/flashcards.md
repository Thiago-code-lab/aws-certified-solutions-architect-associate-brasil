# Review Flashcards

## Card 01

**Question:** A Lambda application must retain customer workflow state across retries and new execution environments. Where should that durable state live?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** In an appropriate external durable store, such as DynamoDB, with a suitable consistency and idempotency design. Execution environment reuse can improve performance, but it is not a durability guarantee. Customer workflow state must survive environment replacement and concurrent invocations.

**AWS references:** [Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html), [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

</details>

## Card 02

**Question:** A team wants to limit a Lambda function concurrency so it cannot overwhelm a database. Which control directly sets a function concurrency ceiling?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Reserved concurrency. Reserved concurrency reserves an allocation and caps that function concurrent execution. Provisioned concurrency pre-initializes environments to reduce cold-start latency and is a different control.

**AWS references:** [Lambda concurrency controls](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html).

</details>

## Card 03

**Question:** A latency-sensitive Lambda function needs pre-initialized execution environments and accepts their additional cost. Which feature is designed for that requirement?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Provisioned concurrency on a supported function version or alias. Provisioned concurrency keeps a configured number of environments initialized. Capacity planning and limits still matter; it is not a promise of zero latency for all traffic.

**AWS references:** [Lambda concurrency controls](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html).

</details>

## Card 04

**Question:** A Lambda SQS batch contains several successful records and one failed record. How can the consumer avoid needlessly retrying the successful records?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Enable and implement partial batch responses, returning the failed item identifiers while making processing idempotent. Partial batch responses let a configured event source mapping retry the failed records. At-least-once processing still requires safe handling of duplicates.

**AWS references:** [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

</details>

## Card 05

**Question:** A public API Gateway REST API uses usage-plan API keys. The team must authenticate users and authorize protected operations. What additional design is required?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Use a supported authorization mechanism, such as an appropriate authorizer or IAM authorization; treat API keys as usage-plan identifiers. API Gateway usage-plan keys support identification for usage control, not authentication or authorization. Protected APIs need an explicit authorization design.

**AWS references:** [API Gateway usage plans and API keys](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html), [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html).

</details>

## Card 06

**Question:** A team wants to limit a Lambda function concurrency so it cannot overwhelm a database. Which control directly sets a function concurrency ceiling?

Why does this alternative fail: “Provisioned concurrency treated solely as a maximum invocation limit.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Provisioned concurrency alone is not the function total concurrency ceiling.

**AWS references:** [Lambda concurrency controls](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html).

</details>

## Card 07

**Question:** A latency-sensitive Lambda function needs pre-initialized execution environments and accepts their additional cost. Which feature is designed for that requirement?

Why does this alternative fail: “Reserved concurrency alone, assuming it pre-initializes environments.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Reserved concurrency allocates and limits concurrency but does not itself pre-initialize environments.

**AWS references:** [Lambda concurrency controls](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html).

</details>

## Card 08

**Question:** A Lambda SQS batch contains several successful records and one failed record. How can the consumer avoid needlessly retrying the successful records?

Why does this alternative fail: “Return success for the entire batch even when required work failed.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Reporting complete success can discard failed work.

**AWS references:** [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 17-Q01 -->

A Lambda application must retain customer workflow state across retries and new execution environments. Where should that durable state live?

A) In an appropriate external durable store, such as DynamoDB, with a suitable consistency and idempotency design.

B) Only in a module-level in-memory variable.

C) Only in /tmp, assuming every later invocation uses the same environment.

D) In the function name.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Execution environment reuse can improve performance, but it is not a durability guarantee. Customer workflow state must survive environment replacement and concurrent invocations.

**Why the other options are incorrect:**

- **B:** Memory belongs to one environment and can be lost or differ across environments.
- **C:** Ephemeral storage is not a cross-environment durable workflow database.
- **D:** A resource name is not a mutable durable state store.

**AWS references:** [Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html), [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

</details>

## Question 2

<!-- question-id: 17-Q02 -->

A team wants to limit a Lambda function concurrency so it cannot overwhelm a database. Which control directly sets a function concurrency ceiling?

A) Provisioned concurrency treated solely as a maximum invocation limit.

B) An S3 lifecycle transition.

C) Reserved concurrency.

D) A larger function deployment package.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Reserved concurrency reserves an allocation and caps that function concurrent execution. Provisioned concurrency pre-initializes environments to reduce cold-start latency and is a different control.

**Why the other options are incorrect:**

- **A:** Provisioned concurrency alone is not the function total concurrency ceiling.
- **B:** Object lifecycle does not limit function invocations.
- **D:** Package size does not configure concurrency admission.

**AWS references:** [Lambda concurrency controls](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html).

</details>

## Question 3

<!-- question-id: 17-Q03 -->

A latency-sensitive Lambda function needs pre-initialized execution environments and accepts their additional cost. Which feature is designed for that requirement?

A) Provisioned concurrency on a supported function version or alias.

B) Reserved concurrency alone, assuming it pre-initializes environments.

C) Disabling all retries for every event source.

D) Using a longer DNS TTL for an unrelated bucket.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Provisioned concurrency keeps a configured number of environments initialized. Capacity planning and limits still matter; it is not a promise of zero latency for all traffic.

**Why the other options are incorrect:**

- **B:** Reserved concurrency allocates and limits concurrency but does not itself pre-initialize environments.
- **C:** Retry policy is not a cold-start initialization feature.
- **D:** An unrelated DNS TTL does not initialize Lambda environments.

**AWS references:** [Lambda concurrency controls](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html).

</details>

## Question 4

<!-- question-id: 17-Q04 -->

A Lambda SQS batch contains several successful records and one failed record. How can the consumer avoid needlessly retrying the successful records?

A) Return success for the entire batch even when required work failed.

B) Assume the default behavior always retries only failed records without configuration.

C) Enable and implement partial batch responses, returning the failed item identifiers while making processing idempotent.

D) Disable the queue visibility timeout entirely.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Partial batch responses let a configured event source mapping retry the failed records. At-least-once processing still requires safe handling of duplicates.

**Why the other options are incorrect:**

- **A:** Reporting complete success can discard failed work.
- **B:** Without the partial response behavior, a failing batch can be retried as a whole.
- **D:** Visibility timeout is part of queue processing and cannot be removed as a replacement for batch handling.

**AWS references:** [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

</details>

## Question 5

<!-- question-id: 17-Q05 -->

A public API Gateway REST API uses usage-plan API keys. The team must authenticate users and authorize protected operations. What additional design is required?

A) Treat the API key alone as secure user authentication and authorization.

B) Use a supported authorization mechanism, such as an appropriate authorizer or IAM authorization; treat API keys as usage-plan identifiers.

C) Put the API key in a public URL and grant every caller administrator permissions.

D) Remove authorization because usage quotas replace identity verification.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** API Gateway usage-plan keys support identification for usage control, not authentication or authorization. Protected APIs need an explicit authorization design.

**Why the other options are incorrect:**

- **A:** AWS explicitly distinguishes API keys from authorization controls.
- **C:** Public exposure and administrator permissions violate the protected-operation requirement.
- **D:** A quota limits usage and does not verify or authorize a principal.

**AWS references:** [API Gateway usage plans and API keys](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html), [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

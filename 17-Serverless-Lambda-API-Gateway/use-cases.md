# Use Cases

## Scenario 1: Durable function state

**Requirement:** A Lambda application must retain customer workflow state across retries and new execution environments. Where should that durable state live?

**Recommended design:** In an appropriate external durable store, such as DynamoDB, with a suitable consistency and idempotency design.

**Reason and boundary:** Execution environment reuse can improve performance, but it is not a durability guarantee. Customer workflow state must survive environment replacement and concurrent invocations.

**Rejected alternative:** Only in a module-level in-memory variable. Memory belongs to one environment and can be lost or differ across environments.

**AWS references:** [Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html), [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

## Scenario 2: Reserved versus provisioned concurrency

**Requirement:** A team wants to limit a Lambda function concurrency so it cannot overwhelm a database. Which control directly sets a function concurrency ceiling?

**Recommended design:** Reserved concurrency.

**Reason and boundary:** Reserved concurrency reserves an allocation and caps that function concurrent execution. Provisioned concurrency pre-initializes environments to reduce cold-start latency and is a different control.

**Rejected alternative:** Provisioned concurrency treated solely as a maximum invocation limit. Provisioned concurrency alone is not the function total concurrency ceiling.

**AWS references:** [Lambda concurrency controls](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html).

## Scenario 3: Reduce cold starts deliberately

**Requirement:** A latency-sensitive Lambda function needs pre-initialized execution environments and accepts their additional cost. Which feature is designed for that requirement?

**Recommended design:** Provisioned concurrency on a supported function version or alias.

**Reason and boundary:** Provisioned concurrency keeps a configured number of environments initialized. Capacity planning and limits still matter; it is not a promise of zero latency for all traffic.

**Rejected alternative:** Reserved concurrency alone, assuming it pre-initializes environments. Reserved concurrency allocates and limits concurrency but does not itself pre-initialize environments.

**AWS references:** [Lambda concurrency controls](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html).

## Scenario 4: SQS partial batch retries

**Requirement:** A Lambda SQS batch contains several successful records and one failed record. How can the consumer avoid needlessly retrying the successful records?

**Recommended design:** Enable and implement partial batch responses, returning the failed item identifiers while making processing idempotent.

**Reason and boundary:** Partial batch responses let a configured event source mapping retry the failed records. At-least-once processing still requires safe handling of duplicates.

**Rejected alternative:** Return success for the entire batch even when required work failed. Reporting complete success can discard failed work.

**AWS references:** [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

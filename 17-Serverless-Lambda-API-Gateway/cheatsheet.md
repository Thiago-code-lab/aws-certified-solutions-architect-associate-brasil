# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Durable function state | In an appropriate external durable store, such as DynamoDB, with a suitable consistency and idempotency design. | Execution environment reuse can improve performance, but it is not a durability guarantee. Customer workflow state must survive environment replacement and concurrent invocations. |
| Reserved versus provisioned concurrency | Reserved concurrency. | Reserved concurrency reserves an allocation and caps that function concurrent execution. Provisioned concurrency pre-initializes environments to reduce cold-start latency and is a different control. |
| Reduce cold starts deliberately | Provisioned concurrency on a supported function version or alias. | Provisioned concurrency keeps a configured number of environments initialized. Capacity planning and limits still matter; it is not a promise of zero latency for all traffic. |
| SQS partial batch retries | Enable and implement partial batch responses, returning the failed item identifiers while making processing idempotent. | Partial batch responses let a configured event source mapping retry the failed records. At-least-once processing still requires safe handling of duplicates. |
| API keys are not authorization | Use a supported authorization mechanism, such as an appropriate authorizer or IAM authorization; treat API keys as usage-plan identifiers. | API Gateway usage-plan keys support identification for usage control, not authentication or authorization. Protected APIs need an explicit authorization design. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Durable function state:** Memory belongs to one environment and can be lost or differ across environments.
- **Reserved versus provisioned concurrency:** Provisioned concurrency alone is not the function total concurrency ceiling.
- **Reduce cold starts deliberately:** Reserved concurrency allocates and limits concurrency but does not itself pre-initialize environments.
- **SQS partial batch retries:** Reporting complete success can discard failed work.
- **API keys are not authorization:** AWS explicitly distinguishes API keys from authorization controls.

## AWS References

[Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html), [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html), [Lambda concurrency controls](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html), [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html), [API Gateway usage plans and API keys](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html), [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

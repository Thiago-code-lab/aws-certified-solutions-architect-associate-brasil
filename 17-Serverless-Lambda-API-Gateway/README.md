# Serverless: Lambda and API Gateway

## Overview

Build serverless applications with explicit authorization, durable external state, idempotency, downstream protection, and measured latency. Managed compute still has quotas, scaling behavior, and billable options.

## Key Concepts

- **Durable function state:** Execution environment reuse can improve performance, but it is not a durability guarantee. Customer workflow state must survive environment replacement and concurrent invocations.
- **Reserved versus provisioned concurrency:** Reserved concurrency reserves an allocation and caps that function concurrent execution. Provisioned concurrency pre-initializes environments to reduce cold-start latency and is a different control.
- **Reduce cold starts deliberately:** Provisioned concurrency keeps a configured number of environments initialized. Capacity planning and limits still matter; it is not a promise of zero latency for all traffic.
- **SQS partial batch retries:** Partial batch responses let a configured event source mapping retry the failed records. At-least-once processing still requires safe handling of duplicates.
- **API keys are not authorization:** API Gateway usage-plan keys support identification for usage control, not authentication or authorization. Protected APIs need an explicit authorization design.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Durable function state:** In an appropriate external durable store, such as DynamoDB, with a suitable consistency and idempotency design.
2. **Reserved versus provisioned concurrency:** Reserved concurrency.
3. **Reduce cold starts deliberately:** Provisioned concurrency on a supported function version or alias.
4. **SQS partial batch retries:** Enable and implement partial batch responses, returning the failed item identifiers while making processing idempotent.
5. **API keys are not authorization:** Use a supported authorization mechanism, such as an appropriate authorizer or IAM authorization; treat API keys as usage-plan identifiers.

## Common Pitfalls

- Memory belongs to one environment and can be lost or differ across environments.
- Provisioned concurrency alone is not the function total concurrency ceiling.
- Reserved concurrency allocates and limits concurrency but does not itself pre-initialize environments.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html), [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html), [Lambda concurrency controls](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html), [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html), [API Gateway usage plans and API keys](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html), [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

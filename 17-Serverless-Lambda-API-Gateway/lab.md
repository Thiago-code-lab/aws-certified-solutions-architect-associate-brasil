# Guided Lab

## Objective

Review retry-safe Lambda SQS batch handling and concurrency protection.

## Services Used

Lambda, SQS event source mapping, and a test-only function.

## Expected Cost Range

Function requests and duration, queue requests, logs, and provisioned concurrency can incur charges. This lab does not require provisioned concurrency.

## Step-by-Step Instructions

1. Use a dedicated test function and Standard queue in the same Region; give the execution role only the required queue and logging permissions.
2. Configure the mapping visibility timeout and function timeout using the linked Lambda SQS documentation, and enable reporting of batch item failures.
3. Use a tested handler with durable idempotency state keyed by business operation identifier. Coordinate completion state with the side effect using a transaction or a downstream idempotency mechanism; recording an identifier alone before the effect can lose work after a crash. Test retries, concurrent duplicates, and failures between state changes locally before connecting the queue.
4. Prepare a small batch with one intentionally failing synthetic record and otherwise successful records.
5. Verify the handler returns the failed record identifier in its partial batch response and that successful records are not needlessly retried by the mapping.
6. Set an appropriate reserved-concurrency ceiling and mapping concurrency limits for the exercise; document how they protect downstream dependencies.
7. If a complete tested handler or durable idempotency store is not available, perform this as a design review and do not claim a live exactly-once side-effect result.

## Validation

- The recorded result distinguishes design review from executed integration evidence.
- Batch-failure reporting and duplicate handling are separate verified behaviors.
- Reserved concurrency is not called a cold-start preinitialization feature.

## Cleanup

1. Disable/delete the lab event source mapping before removing the function and queue.
2. Remove the test idempotency data and exclusively lab-created tables or logs.
3. Check concurrency settings and retained data for any remaining lab resource.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html), [Lambda concurrency controls](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html), [Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

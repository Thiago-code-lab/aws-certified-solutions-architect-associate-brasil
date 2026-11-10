# Guided Lab

## Objective

Distinguish CloudWatch telemetry, CloudTrail data events, and Config findings.

## Services Used

CloudWatch, CloudTrail, and AWS Config documentation; optional scoped test resources.

## Expected Cost Range

Data events, retained logs, custom metrics, Config recording/rules, and storage can incur charges. Start with a documentation review; enable only the specific lab signals needed.

## Step-by-Step Instructions

1. Choose a synthetic application request and list the evidence wanted: latency metric, API caller, resource configuration change, or distributed trace.
2. Map each evidence type to CloudWatch, CloudTrail, Config, or an appropriate tracing pipeline.
3. For a private test bucket, review an object data-event selector for the intended operation and object prefix; note that default management history is insufficient.
4. If executing the optional audit test, enable the narrow selector, perform a small authorized object operation, and verify the corresponding delivered event.
5. Compare a Config compliance finding with the separate actions needed for remediation or prevention.
6. Review the X-Ray SDK/daemon maintenance notice and choose suitable OpenTelemetry instrumentation for new tracing work rather than recommending legacy SDKs without qualification.

## Validation

- The evidence types are not treated as interchangeable.
- The record distinguishes configured logging from verified event delivery.
- Detective findings are not described as automatic prevention.

## Cleanup

1. Remove lab-only selectors, trails, event data stores, rules, alarms, and recording settings as applicable.
2. Retain or delete test evidence according to the lab retention decision; do not disable shared production logging.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), [CloudTrail data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html), [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [X-Ray SDK and daemon maintenance](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Operational telemetry | Amazon CloudWatch. | CloudWatch supports metrics, dashboards, logs, and alarms. The application must publish or instrument the relevant latency signal if it is not supplied automatically. |
| Object API audit events | Configure appropriate S3 object data-event logging on a trail or event data store, including its cost and selection scope. | S3 object operations are CloudTrail data events. Trails and event data stores do not log data events by default; selectors must include the needed activity. |
| Configuration history | AWS Config with the required recording and rules enabled. | Config records supported resource configuration history and evaluates configuration against rules. CloudTrail complements it with API activity, but serves a different primary question. |
| Tracing instrumentation maintenance | No. Review the maintenance notice and prefer an appropriate OpenTelemetry instrumentation and collection path. | AWS documents maintenance mode for the X-Ray SDKs and daemon starting February 25, 2026 and recommends OpenTelemetry migration. Distinguish instrumentation lifecycle from the availability of the X-Ray service. |
| Telemetry is not prevention by default | The rule detects the condition; prevention or remediation requires an additional appropriate control. | Detection, prevention, and remediation are distinct capabilities. A configured rule evaluation is not proof that corrective action occurred or that all security requirements are met. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Operational telemetry:** Retention controls protect object versions rather than evaluate latency metrics.
- **Object API audit events:** Management event history does not automatically supply all object data events.
- **Configuration history:** CPU time series do not reconstruct a security group configuration history.
- **Tracing instrumentation maintenance:** The SDK/daemon notice does not state that the X-Ray service is unavailable.
- **Telemetry is not prevention by default:** A detective evaluation is not inherently a creation-time denial.

## AWS References

[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), [CloudTrail data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html), [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [X-Ray SDK and daemon maintenance](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html), [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

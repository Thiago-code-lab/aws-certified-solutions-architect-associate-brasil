# Monitoring: CloudWatch and CloudTrail

## Overview

Distinguish metrics and alarms, API auditing, configuration history, and distributed tracing. Configure the signals and event categories you need, and separate detective findings from preventive or remedial actions.

## Key Concepts

- **Operational telemetry:** CloudWatch supports metrics, dashboards, logs, and alarms. The application must publish or instrument the relevant latency signal if it is not supplied automatically.
- **Object API audit events:** S3 object operations are CloudTrail data events. Trails and event data stores do not log data events by default; selectors must include the needed activity.
- **Configuration history:** Config records supported resource configuration history and evaluates configuration against rules. CloudTrail complements it with API activity, but serves a different primary question.
- **Tracing instrumentation maintenance:** AWS documents maintenance mode for the X-Ray SDKs and daemon starting February 25, 2026 and recommends OpenTelemetry migration. Distinguish instrumentation lifecycle from the availability of the X-Ray service.
- **Telemetry is not prevention by default:** Detection, prevention, and remediation are distinct capabilities. A configured rule evaluation is not proof that corrective action occurred or that all security requirements are met.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Operational telemetry:** Amazon CloudWatch.
2. **Object API audit events:** Configure appropriate S3 object data-event logging on a trail or event data store, including its cost and selection scope.
3. **Configuration history:** AWS Config with the required recording and rules enabled.
4. **Tracing instrumentation maintenance:** No. Review the maintenance notice and prefer an appropriate OpenTelemetry instrumentation and collection path.
5. **Telemetry is not prevention by default:** The rule detects the condition; prevention or remediation requires an additional appropriate control.

## Common Pitfalls

- Retention controls protect object versions rather than evaluate latency metrics.
- Management event history does not automatically supply all object data events.
- CPU time series do not reconstruct a security group configuration history.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), [CloudTrail data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html), [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [X-Ray SDK and daemon maintenance](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html), [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Use Cases

## Scenario 1: Operational telemetry

**Requirement:** An operations team needs a dashboard and alarm for an EC2 application latency metric. Which service directly provides metrics, dashboards, and alarms?

**Recommended design:** Amazon CloudWatch.

**Reason and boundary:** CloudWatch supports metrics, dashboards, logs, and alarms. The application must publish or instrument the relevant latency signal if it is not supplied automatically.

**Rejected alternative:** An S3 Object Lock retention setting. Retention controls protect object versions rather than evaluate latency metrics.

**AWS references:** [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

## Scenario 2: Object API audit events

**Requirement:** Auditors need S3 GetObject activity for a selected bucket. The team has only the default CloudTrail event history view. What must be considered?

**Recommended design:** Configure appropriate S3 object data-event logging on a trail or event data store, including its cost and selection scope.

**Reason and boundary:** S3 object operations are CloudTrail data events. Trails and event data stores do not log data events by default; selectors must include the needed activity.

**Rejected alternative:** Assume all S3 object data events appear automatically in default management event history. Management event history does not automatically supply all object data events.

**AWS references:** [CloudTrail data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html).

## Scenario 3: Configuration history

**Requirement:** A team must determine how a supported security group configuration changed over time and evaluate it against configuration rules. Which service fits?

**Recommended design:** AWS Config with the required recording and rules enabled.

**Reason and boundary:** Config records supported resource configuration history and evaluates configuration against rules. CloudTrail complements it with API activity, but serves a different primary question.

**Rejected alternative:** A CloudWatch CPU metric alone. CPU time series do not reconstruct a security group configuration history.

**AWS references:** [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [CloudTrail data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html).

## Scenario 4: Tracing instrumentation maintenance

**Requirement:** A new distributed application needs tracing. Should the team treat the legacy X-Ray SDK and daemon as the preferred long-term instrumentation choice without reviewing support status?

**Recommended design:** No. Review the maintenance notice and prefer an appropriate OpenTelemetry instrumentation and collection path.

**Reason and boundary:** AWS documents maintenance mode for the X-Ray SDKs and daemon starting February 25, 2026 and recommends OpenTelemetry migration. Distinguish instrumentation lifecycle from the availability of the X-Ray service.

**Rejected alternative:** Yes. The X-Ray SDK maintenance notice means the X-Ray service itself is already unavailable. The SDK/daemon notice does not state that the X-Ray service is unavailable.

**AWS references:** [X-Ray SDK and daemon maintenance](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html), [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

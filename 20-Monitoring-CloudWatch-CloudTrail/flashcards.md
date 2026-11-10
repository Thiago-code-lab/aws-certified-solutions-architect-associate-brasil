# Review Flashcards

## Card 01

**Question:** An operations team needs a dashboard and alarm for an EC2 application latency metric. Which service directly provides metrics, dashboards, and alarms?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Amazon CloudWatch. CloudWatch supports metrics, dashboards, logs, and alarms. The application must publish or instrument the relevant latency signal if it is not supplied automatically.

**AWS references:** [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

</details>

## Card 02

**Question:** Auditors need S3 GetObject activity for a selected bucket. The team has only the default CloudTrail event history view. What must be considered?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Configure appropriate S3 object data-event logging on a trail or event data store, including its cost and selection scope. S3 object operations are CloudTrail data events. Trails and event data stores do not log data events by default; selectors must include the needed activity.

**AWS references:** [CloudTrail data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html).

</details>

## Card 03

**Question:** A team must determine how a supported security group configuration changed over time and evaluate it against configuration rules. Which service fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** AWS Config with the required recording and rules enabled. Config records supported resource configuration history and evaluates configuration against rules. CloudTrail complements it with API activity, but serves a different primary question.

**AWS references:** [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [CloudTrail data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html).

</details>

## Card 04

**Question:** A new distributed application needs tracing. Should the team treat the legacy X-Ray SDK and daemon as the preferred long-term instrumentation choice without reviewing support status?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** No. Review the maintenance notice and prefer an appropriate OpenTelemetry instrumentation and collection path. AWS documents maintenance mode for the X-Ray SDKs and daemon starting February 25, 2026 and recommends OpenTelemetry migration. Distinguish instrumentation lifecycle from the availability of the X-Ray service.

**AWS references:** [X-Ray SDK and daemon maintenance](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html), [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

</details>

## Card 05

**Question:** A Config rule reports that a resource is noncompliant. No remediation or preventive policy is configured. Which statement is justified?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The rule detects the condition; prevention or remediation requires an additional appropriate control. Detection, prevention, and remediation are distinct capabilities. A configured rule evaluation is not proof that corrective action occurred or that all security requirements are met.

**AWS references:** [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).

</details>

## Card 06

**Question:** Auditors need S3 GetObject activity for a selected bucket. The team has only the default CloudTrail event history view. What must be considered?

Why does this alternative fail: “Assume all S3 object data events appear automatically in default management event history.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Management event history does not automatically supply all object data events.

**AWS references:** [CloudTrail data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html).

</details>

## Card 07

**Question:** A team must determine how a supported security group configuration changed over time and evaluate it against configuration rules. Which service fits?

Why does this alternative fail: “A CloudWatch CPU metric alone.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** CPU time series do not reconstruct a security group configuration history.

**AWS references:** [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [CloudTrail data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html).

</details>

## Card 08

**Question:** A new distributed application needs tracing. Should the team treat the legacy X-Ray SDK and daemon as the preferred long-term instrumentation choice without reviewing support status?

Why does this alternative fail: “Yes. The X-Ray SDK maintenance notice means the X-Ray service itself is already unavailable.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The SDK/daemon notice does not state that the X-Ray service is unavailable.

**AWS references:** [X-Ray SDK and daemon maintenance](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html), [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

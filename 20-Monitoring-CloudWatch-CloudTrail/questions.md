# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 20-Q01 -->

An operations team needs a dashboard and alarm for an EC2 application latency metric. Which service directly provides metrics, dashboards, and alarms?

A) An S3 Object Lock retention setting.

B) AWS DMS schema conversion.

C) Amazon CloudWatch.

D) An SCP as a time-series metrics store.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** CloudWatch supports metrics, dashboards, logs, and alarms. The application must publish or instrument the relevant latency signal if it is not supplied automatically.

**Why the other options are incorrect:**

- **A:** Retention controls protect object versions rather than evaluate latency metrics.
- **B:** Schema migration does not provide an operational latency alarm.
- **D:** SCPs are permission guardrails rather than a metrics store.

**AWS references:** [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

</details>

## Question 2

<!-- question-id: 20-Q02 -->

Auditors need S3 GetObject activity for a selected bucket. The team has only the default CloudTrail event history view. What must be considered?

A) Assume all S3 object data events appear automatically in default management event history.

B) Configure appropriate S3 object data-event logging on a trail or event data store, including its cost and selection scope.

C) Enable EC2 detailed monitoring and assume it records S3 object API callers.

D) Add a Route 53 TXT record for the bucket name.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** S3 object operations are CloudTrail data events. Trails and event data stores do not log data events by default; selectors must include the needed activity.

**Why the other options are incorrect:**

- **A:** Management event history does not automatically supply all object data events.
- **C:** EC2 metric frequency is unrelated to S3 API caller auditing.
- **D:** DNS text records do not enable CloudTrail data-event capture.

**AWS references:** [CloudTrail data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html).

</details>

## Question 3

<!-- question-id: 20-Q03 -->

A team must determine how a supported security group configuration changed over time and evaluate it against configuration rules. Which service fits?

A) A CloudWatch CPU metric alone.

B) A NAT gateway.

C) AWS Config with the required recording and rules enabled.

D) An SQS visibility timeout.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Config records supported resource configuration history and evaluates configuration against rules. CloudTrail complements it with API activity, but serves a different primary question.

**Why the other options are incorrect:**

- **A:** CPU time series do not reconstruct a security group configuration history.
- **B:** NAT is not a configuration recorder.
- **D:** Queue message visibility does not evaluate security group compliance.

**AWS references:** [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [CloudTrail data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html).

</details>

## Question 4

<!-- question-id: 20-Q04 -->

A new distributed application needs tracing. Should the team treat the legacy X-Ray SDK and daemon as the preferred long-term instrumentation choice without reviewing support status?

A) Yes. The X-Ray SDK maintenance notice means the X-Ray service itself is already unavailable.

B) Yes. Maintenance status never affects instrumentation decisions.

C) Disable tracing because CloudTrail provides complete request-span traces.

D) No. Review the maintenance notice and prefer an appropriate OpenTelemetry instrumentation and collection path.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** AWS documents maintenance mode for the X-Ray SDKs and daemon starting February 25, 2026 and recommends OpenTelemetry migration. Distinguish instrumentation lifecycle from the availability of the X-Ray service.

**Why the other options are incorrect:**

- **A:** The SDK/daemon notice does not state that the X-Ray service is unavailable.
- **B:** Support lifecycle affects maintenance and migration planning.
- **C:** CloudTrail API auditing is not a substitute for application distributed tracing.

**AWS references:** [X-Ray SDK and daemon maintenance](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html), [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

</details>

## Question 5

<!-- question-id: 20-Q05 -->

A Config rule reports that a resource is noncompliant. No remediation or preventive policy is configured. Which statement is justified?

A) The resource must already have been blocked from being created.

B) Every Config rule automatically deletes every noncompliant resource.

C) A compliance result guarantees the entire application is secure.

D) The rule detects the condition; prevention or remediation requires an additional appropriate control.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Detection, prevention, and remediation are distinct capabilities. A configured rule evaluation is not proof that corrective action occurred or that all security requirements are met.

**Why the other options are incorrect:**

- **A:** A detective evaluation is not inherently a creation-time denial.
- **B:** Deletion is not the automatic behavior of every rule.
- **C:** Compliance with selected rules does not prove all aspects of application security.

**AWS references:** [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

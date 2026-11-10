# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 27-Q01 -->

A web tier runs in one AZ, while its database already has suitable Multi-AZ protection. The business requires the web tier to survive an AZ outage. Which change addresses the missing protection?

A) Add a read replica but leave every web instance in one AZ.

B) Deploy replaceable web instances across multiple AZs behind a multi-AZ ALB and keep required state outside individual instances.

C) Increase CPU on the same single-AZ web instance.

D) Add a second DNS name for the same web instance.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** The unprotected component is the web tier. Database redundancy does not make single-AZ application compute available during that AZ failure.

**Why the other options are incorrect:**

- **A:** Additional database readers do not remove the web tier AZ dependency.
- **C:** A larger instance remains in the same failure domain.
- **D:** Another name does not create another serving location.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

</details>

## Question 2

<!-- question-id: 27-Q02 -->

Inventory and invoicing must each receive every accepted order, even if one subsystem is temporarily unavailable. Which design isolates their processing backlogs?

A) Use one SQS queue and assume both competing consumers always receive every message.

B) Send orders only to the currently fastest consumer.

C) Keep accepted orders only in one web server memory.

D) Publish to SNS and subscribe a separate SQS queue for each subsystem, with retry-safe consumers.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Separate subscribed queues provide independent buffering. Successful publication, correct subscription policies, retry behavior, and idempotent consumers are necessary parts of the design.

**Why the other options are incorrect:**

- **A:** One competing-consumer queue distributes work rather than independently copying every event to each subsystem.
- **B:** Sending to only one subsystem misses a required recipient.
- **C:** Instance memory is not durable accepted-order buffering.

**AWS references:** [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).

</details>

## Question 3

<!-- question-id: 27-Q03 -->

Customers must download public website assets through CloudFront, while direct unauthenticated access to the regular S3 bucket origin must remain blocked. Which configuration fits?

A) Grant public read access to the bucket and hide its name in the HTML.

B) Use CloudFront OAC and a scoped bucket policy while retaining appropriate S3 public-access blocking.

C) Use an S3 website endpoint with OAC as though it were a regular S3 origin.

D) Disable every bucket permission, including the intended CloudFront grant.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Viewer access and origin access are separate boundaries. OAC plus a distribution-scoped bucket policy lets CloudFront retrieve private origin objects without making the bucket public.

**Why the other options are incorrect:**

- **A:** An obscure publicly readable bucket is still directly accessible.
- **C:** S3 website endpoints do not support OAC.
- **D:** Removing the required origin permission prevents the authorized CDN from reading the objects.

**AWS references:** [CloudFront origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html), [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html).

</details>

## Question 4

<!-- question-id: 27-Q04 -->

A DynamoDB checkout workflow must confirm the latest committed order state immediately after its write. The current path reads an eventually consistent GSI. Which change directly addresses consistency?

A) Set ConsistentRead on the GSI and assume it is supported.

B) Read the known order key from the base table using a strongly consistent read where required.

C) Increase the web server CPU only.

D) Use an older cached result as the authoritative confirmation.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** The base table supports strongly consistent reads. GSI reads do not; a faster caller or cache does not turn an eventually consistent read into a strong read.

**Why the other options are incorrect:**

- **A:** Strongly consistent GSI reads are not supported.
- **C:** Compute capacity does not change database consistency semantics.
- **D:** A stale cached value cannot establish immediate confirmation of the latest write.

**AWS references:** [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

</details>

## Question 5

<!-- question-id: 27-Q05 -->

A recovery design replicates critical data to another Region, but application servers there are not running. Recovery requires deploying or activating the application tier. Which pattern is closest?

A) Pilot light.

B) Warm standby with a fully functioning scaled-down application already serving test traffic.

C) Multi-site active/active with both Regions serving production.

D) A same-Region read replica described as a complete regional recovery plan.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Pilot light keeps core recovery components such as data replication active, then brings up the remaining workload for recovery. The measured RTO depends on that activation path.

**Why the other options are incorrect:**

- **B:** The stem says the application tier is not already running as a fully functioning standby.
- **C:** Both Regions are not serving production traffic.
- **D:** A same-Region replica does not address the stated regional recovery topology.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

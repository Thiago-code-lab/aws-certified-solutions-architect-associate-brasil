# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 29-Q01 -->

A relational database needs managed AZ failover. The chosen deployment is an RDS Multi-AZ DB instance deployment; extra read capacity is not required. Which feature is the direct fit?

A) Only an ordinary asynchronous read replica, assumed to be the same feature.

B) The synchronous standby and managed failover of that Multi-AZ DB instance deployment.

C) A cache that does not retain the authoritative database.

D) A manually installed database on one EC2 instance with no failover automation.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** This specifies the deployment type and availability objective. A Multi-AZ DB instance standby supports managed failover; an asynchronous read replica primarily provides another read or recovery copy with different semantics.

**Why the other options are incorrect:**

- **A:** An ordinary read replica does not provide the identical synchronous standby failover feature.
- **C:** A cache is not a substitute for protecting the authoritative database.
- **D:** A single self-managed instance lacks the requested managed AZ failover.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html).

</details>

## Question 2

<!-- question-id: 29-Q02 -->

A stateless web application must remain available when one AZ fails. Which design directly addresses that failure scope?

A) One larger EC2 instance with a daily AMI.

B) Two application instances confined to the same AZ.

C) An ALB with application instances across multiple AZs, working health checks, externalized state, and sufficient surviving capacity.

D) An Elastic IP associated with the only web instance.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Multiple AZs and appropriately placed state reduce the single-AZ dependency. Recovery copies and static addressing do not by themselves keep a sole failed instance serving requests.

**Why the other options are incorrect:**

- **A:** An AMI supports recovery but does not keep that one instance available during AZ failure.
- **B:** One AZ remains the common failure domain.
- **D:** An address does not supply a healthy replacement application server.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Question 3

<!-- question-id: 29-Q03 -->

A VPC workload needs same-Region S3 access without NAT or public internet routing. Which choice supplies a route-table-based private path?

A) A NAT gateway used for all S3 traffic.

B) An internet gateway described as an attachment to a private subnet.

C) An S3 gateway endpoint with the required routes and appropriate endpoint, bucket, and IAM policies.

D) An Elastic IP assigned to the S3 bucket.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** A gateway endpoint supports S3 access through VPC route tables without NAT or an internet gateway for that traffic. Authorization remains a separate requirement.

**Why the other options are incorrect:**

- **A:** NAT violates the explicit network-path constraint.
- **B:** Internet gateways attach to VPCs and do not satisfy the private endpoint requirement.
- **D:** S3 buckets do not receive Elastic IP addresses.

**AWS references:** [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html).

</details>

## Question 4

<!-- question-id: 29-Q04 -->

An API accepts jobs durably and workers can process them asynchronously. It needs to absorb traffic bursts without requiring every worker to be available at acceptance time. Which service fits?

A) Amazon SQS with suitable producer error handling and retry-safe consumers.

B) Amazon EFS used as if it were a managed queue.

C) AWS WAF used as durable job storage.

D) AWS Direct Connect used as message retention.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** SQS decouples job acceptance from consumer processing. Applications still handle send failures, retention, retries, duplicate processing, and backlog growth.

**Why the other options are incorrect:**

- **B:** Shared file storage does not provide the managed queue semantics requested.
- **C:** Web request filtering is not durable job buffering.
- **D:** A network circuit does not retain jobs.

**AWS references:** [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html).

</details>

## Question 5

<!-- question-id: 29-Q05 -->

A learner selects a policy allowing every S3 action on every bucket when the scenario requires reading only one object prefix. Which correction addresses the actual authorization requirement?

A) Allow the required object-read action only on the specified object-prefix resources, accounting for any separately required bucket actions.

B) Keep administrator permissions because all managed policies are inherently least privilege.

C) Replace the role with a shared root key.

D) Modify only network ACL rules while leaving excessive IAM authorization unchanged.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Least privilege matches allowed actions and resource scope to the requirement. Bucket-level operations, if genuinely needed, use appropriate bucket resource scopes rather than indiscriminately broad object permissions.

**Why the other options are incorrect:**

- **B:** Managed policy status does not make broad permissions least privilege for a narrow scenario.
- **C:** Root credentials broaden risk and do not solve resource scoping.
- **D:** Network filters do not remove excessive IAM permissions.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

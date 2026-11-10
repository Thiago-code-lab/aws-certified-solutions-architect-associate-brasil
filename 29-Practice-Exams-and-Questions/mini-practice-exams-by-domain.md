# Mini Practice Exams by Domain

Choose one answer for each question. These original practice items are not AWS exam questions.

Four equal practice blocks are provided for review; this is not an exam-weighted mock. Official scored-content weights: Security 30%, Resilience 26%, Performance 24%, Cost Optimization 20%.


## Resilience

### Question 1

<!-- question-id: 29-M-Q01 -->

A relational workload needs a primary and a synchronous standby in another AZ with managed failover, not a readable standby. Which RDS deployment matches?

A) A single-AZ DB instance with only weekly snapshots.

B) An ordinary asynchronous read replica treated as the same topology.

C) A local application cache without a protected database.

D) An RDS Multi-AZ DB instance deployment.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** The Multi-AZ DB instance topology supplies the specified synchronous standby and managed failover. The deployment type is explicit to avoid confusing it with a Multi-AZ DB cluster.

**Why the other options are incorrect:**

- **A:** Snapshots are recovery copies and do not provide this running standby.
- **B:** The stated asynchronous replica has different replication and failover semantics.
- **C:** A cache does not provide the authoritative database standby.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html).

</details>

### Question 2

<!-- question-id: 29-M-Q02 -->

A job producer can accept asynchronous processing, and workers temporarily cannot keep up with a burst. Which pattern buffers accepted work independently of worker availability?

A) An SQS queue with controlled worker scaling and retry-safe processing.

B) A synchronous request to one fixed worker with no buffering.

C) Dropping all excess accepted jobs without informing the caller.

D) A DNS TXT record as a persistent job log.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** A queue decouples acceptance from processing. Retention, send errors, backlog age, consumer capacity, and duplicates still need explicit handling.

**Why the other options are incorrect:**

- **B:** No buffering means a slow or unavailable worker directly affects acceptance.
- **C:** Silently dropping accepted work violates the buffering requirement.
- **D:** A DNS record is not a job queue.

**AWS references:** [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html).

</details>

### Question 3

<!-- question-id: 29-M-Q03 -->

A recovery Region has replicated core data, but the application tier must be started or deployed during failover. Which pattern best describes this?

A) Pilot light.

B) Warm standby with a fully running scaled-down application.

C) Active/active with both Regions already serving normal traffic.

D) A same-AZ backup only.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Pilot light keeps core recovery components ready while additional workload components need activation. Recovery-time targets must account for that activation.

**Why the other options are incorrect:**

- **B:** Warm standby already maintains a functioning workload, unlike the stem.
- **C:** Normal traffic is not being served by the recovery Region.
- **D:** The described recovery site is in another Region with replicated core data.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

### Question 4

<!-- question-id: 29-M-Q04 -->

A logical deletion has replicated from an RDS primary to its standby. Which capability can recover a valid earlier data state?

A) An available backup or point-in-time recovery history with tested restore procedures.

B) Increasing the number of web servers only.

C) Assuming the synchronized standby must still contain pre-delete data.

D) Adding a second name for the database endpoint.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Historical recovery data protects against mistakes that replication can reproduce. Application recovery must use a retained point from before the logical error.

**Why the other options are incorrect:**

- **B:** Web compute does not restore deleted database history.
- **C:** The premise says the deletion has already replicated.
- **D:** DNS aliases do not retain historical database states.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

</details>

### Question 5

<!-- question-id: 29-M-Q05 -->

A website needs edge caching for HTTP(S) static assets to reduce repeated trips to the origin. Which service directly fits?

A) Amazon CloudFront with suitable cache and origin configuration.

B) An SQS queue as the viewer-facing CDN.

C) A NAT gateway as a worldwide cache.

D) A KMS key as the asset distribution network.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** CloudFront distributes HTTP(S) content through edge locations. Cache behavior, origin access, viewer security, and invalidation or versioning must fit the application.

**Why the other options are incorrect:**

- **B:** A queue buffers messages rather than serving HTTP assets as a CDN.
- **C:** A NAT gateway translates connections and does not provide global content caching.
- **D:** Key management does not supply edge delivery.

**AWS references:** [CloudFront origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html), [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html).

</details>


## Performance

### Question 6

<!-- question-id: 29-M-Q06 -->

Athena repeatedly queries only a few columns from a large S3 dataset. Which storage format change can reduce the data read?

A) Duplicate the data into many tiny CSV files without a query-aware layout.

B) Require SELECT * for all queries.

C) Store the dataset schema only in a security group description.

D) Use an appropriate columnar format such as Parquet or ORC, with compression and sensible file sizes.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Columnar formats support reading the needed columns. Compression and a suitable layout help, while excessive small files can increase overhead.

**Why the other options are incorrect:**

- **A:** Tiny unoptimized files increase overhead and do not create column pruning.
- **B:** Selecting unused columns can increase scanning.
- **C:** Network rule descriptions are not a data catalog or storage format.

**AWS references:** [Athena data optimization](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html).

</details>

### Question 7

<!-- question-id: 29-M-Q07 -->

A Lambda HTTP endpoint has a cold-start latency objective and a budget for pre-initialized environments. Which feature specifically addresses that objective?

A) Reserved concurrency alone assumed to initialize environments.

B) A higher S3 retention period.

C) An API key used as a prewarming command.

D) Provisioned concurrency on a supported version or alias.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Provisioned concurrency keeps configured execution environments initialized. It has an additional cost and must be sized for the workload.

**Why the other options are incorrect:**

- **A:** Reserved concurrency reserves and caps concurrency but does not itself pre-initialize environments.
- **B:** Object retention does not initialize function environments.
- **C:** A usage-plan key is not a Lambda capacity-initialization feature.

**AWS references:** [Lambda concurrency controls](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html).

</details>

### Question 8

<!-- question-id: 29-M-Q08 -->

A DynamoDB workload has difficult-to-predict request volume and the team wants AWS to manage request-capacity scaling rather than choosing provisioned read and write capacity units. Which mode fits?

A) Static provisioned capacity with no scaling or workload planning.

B) No capacity mode because DynamoDB ignores all quotas.

C) A local CSV file as a managed DynamoDB capacity mode.

D) On-demand capacity mode, while still accounting for quotas, partition design, and documented scaling behavior.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** On-demand mode removes the need to provision read and write capacity units. It does not make limits, key distribution, or capacity behavior irrelevant.

**Why the other options are incorrect:**

- **A:** A fixed provisioned allocation requires a different capacity-planning approach.
- **B:** DynamoDB still has service limits and workload design constraints.
- **C:** A CSV file is not a DynamoDB capacity mode.

**AWS references:** [DynamoDB capacity modes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html), [DynamoDB partition key design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html).

</details>

### Question 9

<!-- question-id: 29-M-Q09 -->

Athena needs table metadata describing data in S3. Which component commonly supplies that metadata?

A) An internet gateway.

B) An EC2 key pair.

C) An S3 delete marker.

D) The AWS Glue Data Catalog.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** The Data Catalog stores table and schema metadata used by Athena. It does not replace the underlying S3 data or automatically perform every data transformation.

**Why the other options are incorrect:**

- **A:** Internet routing does not hold analytical table schemas.
- **B:** An instance access key pair is not a table metadata catalog.
- **C:** A delete marker controls object-version visibility rather than schema metadata.

**AWS references:** [AWS Glue components](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html), [Athena data optimization](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html).

</details>

### Question 10

<!-- question-id: 29-M-Q10 -->

A VPC needs private access to a supported service exposed through interface endpoints. Which technology is designed for that service-oriented connectivity?

A) AWS PrivateLink.

B) A public NAT gateway described as mandatory private-service access.

C) Transitive VPC peering assumed to happen automatically.

D) An S3 lifecycle policy.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** PrivateLink provides supported private service connectivity through endpoints. Endpoint policies, security groups, DNS, and service permissions must be designed as applicable.

**Why the other options are incorrect:**

- **B:** A NAT gateway is not the required interface endpoint technology.
- **C:** Peering is nontransitive and is a different connectivity model.
- **D:** Object lifecycle does not establish a service network endpoint.

**AWS references:** [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html), [VPC peering limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html).

</details>


## Security

### Question 11

<!-- question-id: 29-M-Q11 -->

A database password must be stored centrally and rotated in both the database and the stored secret. Which service directly supports that lifecycle?

A) KMS key-material rotation alone.

B) AWS Secrets Manager with an appropriate supported rotation configuration.

C) A static plaintext pipeline variable.

D) A security group description containing the password.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Secrets Manager rotation updates the credential and its stored representation using the configured mechanism. It is different from cryptographic key-material rotation.

**Why the other options are incorrect:**

- **A:** KMS rotation does not change the database password.
- **C:** A static plaintext value does not implement controlled rotation.
- **D:** Resource descriptions must not expose secrets and do not rotate them.

**AWS references:** [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html), [KMS key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html).

</details>

### Question 12

<!-- question-id: 29-M-Q12 -->

A workload only reads objects under one S3 prefix. Which policy design best matches least privilege?

A) Allow every S3 action on every resource.

B) Share the organization root access key.

C) Grant IAM administrator permissions because the data is encrypted.

D) Allow the necessary object-read action on the specified object-prefix resources through an appropriate workload role.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Least privilege scopes actions and resources to the workload. Encryption does not justify unrelated administrative access.

**Why the other options are incorrect:**

- **A:** Global service permissions exceed the requirement.
- **B:** Root keys are not appropriate workload credentials.
- **C:** At-rest encryption does not reduce an administrator credential to least privilege.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

</details>

### Question 13

<!-- question-id: 29-M-Q13 -->

A security investigation needs S3 DeleteObject activity for a specific bucket. Which CloudTrail configuration must be considered?

A) Only assume management event history automatically captures every object deletion.

B) Only enable an EC2 CPU alarm.

C) Only change a DNS record.

D) Appropriate object data-event selectors on a trail or event data store, with log protection and cost planning.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** S3 object operations are data events and are not logged by default by trails or event data stores. The intended resource and operation scope must be selected.

**Why the other options are incorrect:**

- **A:** Default management event history is not an automatic record of all object data events.
- **B:** Compute metrics do not identify S3 object API calls.
- **C:** DNS configuration does not turn on API data-event logging.

**AWS references:** [CloudTrail data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html).

</details>

### Question 14

<!-- question-id: 29-M-Q14 -->

A workload needs customer-controlled KMS key policy management and auditable permitted key use. Which key type is appropriate?

A) An AWS owned key whose policy cannot be managed by the customer.

B) An IAM user password treated as a KMS key.

C) An S3 public-read ACL as a cryptographic key.

D) A customer managed KMS key configured with appropriate policies.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Customer managed keys provide customer policy and lifecycle control. IAM and KMS authorization must still permit only the intended cryptographic operations.

**Why the other options are incorrect:**

- **A:** An AWS owned key does not provide customer policy management.
- **B:** A sign-in credential is not a KMS key resource.
- **C:** An ACL controls object access and is not cryptographic key material.

**AWS references:** [AWS KMS key concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html).

</details>

### Question 15

<!-- question-id: 29-M-Q15 -->

A database tier should accept its database port only from the application tier security group, not from the whole internet. Which design fits?

A) Open the database port to 0.0.0.0/0 solely for convenience.

B) Assume KMS encryption permits unrestricted network access.

C) An appropriate database security group rule referencing the application tier security group, with suitable subnet routing and no unnecessary public exposure.

D) Use the same unrestricted inbound rule for every tier.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Security group references can scope allowed traffic between suitable resources. Network segmentation complements authentication and encryption rather than being replaced by them.

**Why the other options are incorrect:**

- **A:** An internet-wide source exceeds the stated application-only requirement.
- **B:** At-rest encryption is not a network access policy.
- **D:** An unrestricted shared rule does not enforce the intended tier boundary.

**AWS references:** [VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>


## Cost Optimization

### Question 16

<!-- question-id: 29-M-Q16 -->

Records are retained long term, rarely retrieved, and a restore delay is acceptable. Which decision process is appropriate?

A) Choose a class only by its storage-unit rate and ignore every retrieval requirement.

B) Delete all records to reduce cost despite mandatory retention.

C) Evaluate a suitable S3 archival class using retrieval time, request and retrieval costs, minimum storage duration, and retention requirements.

D) Assume every Glacier class has identical access behavior.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Archival choices must satisfy access and retention constraints, not only storage price. S3 archival classes differ in retrieval behavior and charging dimensions.

**Why the other options are incorrect:**

- **A:** A low storage rate does not establish suitability or lowest total cost.
- **B:** Deletion violates the retention requirement.
- **D:** The classes have different access and restore characteristics.

**AWS references:** [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html).

</details>

### Question 17

<!-- question-id: 29-M-Q17 -->

A predictable EC2 baseline runs continuously and cannot tolerate arbitrary capacity interruptions. Which pricing approach is worth evaluating after rightsizing?

A) Spot alone assumed to guarantee uninterrupted capacity.

B) An appropriately sized Savings Plan or applicable Reserved Instance pricing commitment, with capacity needs assessed separately.

C) A commitment to the unmeasured maximum possible peak.

D) An EBS snapshot mistaken for an EC2 usage discount.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Pricing commitments can suit stable eligible usage. They are not a universal capacity guarantee, and Spot interruption behavior must not be ignored for this workload.

**Why the other options are incorrect:**

- **A:** Spot capacity can be interrupted.
- **C:** Unmeasured peak commitments can create underutilized spend.
- **D:** Snapshots are recovery storage, not a compute pricing commitment.

**AWS references:** [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html), [EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html), [EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html).

</details>

### Question 18

<!-- question-id: 29-M-Q18 -->

A short event-processing task runs only occasionally. What supports evaluating Lambda as a cost option rather than automatically keeping an idle server running?

A) Lambda is always cheaper than EC2 for every workload.

B) Lambda has unlimited free execution for every account.

C) Its request and execution-based charging can reduce idle compute cost, while total cost still depends on duration, memory, traffic, dependencies, and optional features.

D) Provisioned concurrency has no additional cost.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Serverless pricing can fit intermittent work but is not universally cheapest. Compare the actual workload and applicable pricing, including pre-initialized capacity when configured.

**Why the other options are incorrect:**

- **A:** No service is universally cheapest regardless of workload.
- **B:** Pricing and eligibility limits still apply.
- **D:** Provisioned concurrency incurs additional charges.

**AWS references:** [Lambda concurrency controls](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html), [AWS Pricing Calculator](https://calculator.aws/), [AWS Free Tier account eligibility](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html).

</details>

### Question 19

<!-- question-id: 29-M-Q19 -->

A same-Region VPC workload accesses S3 through a NAT gateway. Which alternative should be evaluated to remove NAT processing for that supported S3 path?

A) An S3 gateway endpoint, with correct routes and access policies.

B) A second NAT gateway solely to make each S3 request traverse more NAT processing.

C) A public bucket policy as a network cost control.

D) A larger DNS TTL assumed to remove all NAT processing charges.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** A gateway endpoint supplies the supported private S3 path without using NAT for that traffic. It does not imply all S3 or data-transfer charges disappear.

**Why the other options are incorrect:**

- **B:** Adding unnecessary NAT processing does not solve the stated path cost.
- **C:** Public authorization is not needed to configure a gateway endpoint.
- **D:** DNS caching does not remove NAT processing for the data traffic.

**AWS references:** [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html), [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html).

</details>

### Question 20

<!-- question-id: 29-M-Q20 -->

Which operating practice supports ongoing cost optimization without treating a notification as a hard spending cap?

A) Review the bill only once a year and ignore ownership.

B) Combine Cost Explorer analysis, allocation discipline, AWS Budgets notifications, ownership, and review of measured optimization opportunities.

C) Assume a budget notification immediately halts every possible charge.

D) Disable cost allocation and delete usage records to simplify reporting.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Cost governance combines visibility with accountable decisions and follow-through. Budgets track and notify or invoke configured actions; they are not instantaneous universal charge cutoffs.

**Why the other options are incorrect:**

- **A:** Infrequent review and no ownership delay detection and action.
- **C:** Cost updates and actions have limits and delays.
- **D:** Removing allocation and evidence makes cost accountability harder.

**AWS references:** [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html), [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

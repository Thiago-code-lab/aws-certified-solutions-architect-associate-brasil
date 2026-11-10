# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 04-Q01 -->

A batch job checkpoints its progress and can resume after interruption. It has a flexible completion window. Which EC2 purchase option is designed for spare capacity at a discount?

A) Spot Instances.

B) Dedicated Hosts solely to obtain the lowest batch price.

C) On-Demand Capacity Reservations as a guaranteed discount mechanism.

D) A larger EBS volume as a compute purchase option.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Spot uses spare EC2 capacity and can be interrupted. Checkpointing and flexible scheduling make the stated batch workload a suitable candidate, subject to capacity availability.

**Why the other options are incorrect:**

- **B:** Dedicated hardware addresses isolation or licensing, not this spare-capacity objective.
- **C:** A capacity reservation addresses capacity; it does not inherently supply a pricing discount.
- **D:** EBS is storage, not an EC2 compute purchase option.

**AWS references:** [EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html), [EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html).

</details>

## Question 2

<!-- question-id: 04-Q02 -->

An EC2 instance is in one Availability Zone and an EBS volume is in another. How can the data be made available as an attachable EBS volume to that instance?

A) Attach the existing volume directly across Availability Zones.

B) Create a snapshot and create a new volume from it in the instance Availability Zone.

C) Change only the instance security group.

D) Assign an Elastic IP to the EBS volume.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** An EBS volume attaches to instances in its own Availability Zone. A snapshot can be used to create a volume in another Availability Zone in the Region.

**Why the other options are incorrect:**

- **A:** EBS attachment is not cross-AZ.
- **C:** Network rules do not change a volume location.
- **D:** EBS volumes do not become cross-AZ network disks through Elastic IPs.

**AWS references:** [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html).

</details>

## Question 3

<!-- question-id: 04-Q03 -->

Linux EC2 instances in multiple Availability Zones need concurrent access to the same managed NFS file system. Which choice fits?

A) An ordinary single EBS volume attached across Availability Zones.

B) Amazon EFS Regional with mount targets and suitable security group rules.

C) Instance store as the sole shared file system.

D) An SQS queue mounted as an NFS volume.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** EFS provides managed shared NFS storage; the Regional storage option supports a multi-AZ design. Mount targets and network access still need configuration.

**Why the other options are incorrect:**

- **A:** Ordinary EBS attachment does not provide multi-AZ NFS sharing.
- **C:** Instance store is local instance storage, not a managed shared NFS service.
- **D:** SQS is a messaging service and is not an NFS file system.

**AWS references:** [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html), [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html).

</details>

## Question 4

<!-- question-id: 04-Q04 -->

Tightly coupled EC2 workers need low-latency communication inside one Availability Zone. Which common placement strategy targets this requirement?

A) A spread placement group selected specifically to separate underlying hardware.

B) A cluster placement group.

C) Independent DNS records for each worker.

D) A cross-Region S3 replication rule.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** A cluster placement group places supported instances close together in one AZ for tightly coupled workloads. This is a performance choice, not protection from losing that AZ.

**Why the other options are incorrect:**

- **A:** Spread prioritizes hardware separation rather than tightly packed placement.
- **C:** DNS naming does not control instance placement.
- **D:** Object replication does not place EC2 workers.

**AWS references:** [EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html).

</details>

## Question 5

<!-- question-id: 04-Q05 -->

A team buys a Compute Savings Plan for its steady baseline. Which statement is accurate?

A) It discounts eligible usage in exchange for a spend commitment; it does not by itself reserve EC2 capacity.

B) It guarantees any requested EC2 instance can launch in any AZ.

C) It makes unused committed spend refundable automatically.

D) It guarantees Spot capacity will never be interrupted.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Savings Plans are pricing commitments. Capacity reservations are a separate design consideration, and unused commitment can reduce realized savings.

**Why the other options are incorrect:**

- **B:** A pricing commitment is not a capacity guarantee.
- **C:** Commitment utilization must be managed; unused commitment is not automatically refunded.
- **D:** Spot interruption behavior is not removed by buying a Savings Plan.

**AWS references:** [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html), [EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html), [EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Review Flashcards

## Card 01

**Question:** A batch job checkpoints its progress and can resume after interruption. It has a flexible completion window. Which EC2 purchase option is designed for spare capacity at a discount?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Spot Instances. Spot uses spare EC2 capacity and can be interrupted. Checkpointing and flexible scheduling make the stated batch workload a suitable candidate, subject to capacity availability.

**AWS references:** [EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html), [EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html).

</details>

## Card 02

**Question:** An EC2 instance is in one Availability Zone and an EBS volume is in another. How can the data be made available as an attachable EBS volume to that instance?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Create a snapshot and create a new volume from it in the instance Availability Zone. An EBS volume attaches to instances in its own Availability Zone. A snapshot can be used to create a volume in another Availability Zone in the Region.

**AWS references:** [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html).

</details>

## Card 03

**Question:** Linux EC2 instances in multiple Availability Zones need concurrent access to the same managed NFS file system. Which choice fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Amazon EFS Regional with mount targets and suitable security group rules. EFS provides managed shared NFS storage; the Regional storage option supports a multi-AZ design. Mount targets and network access still need configuration.

**AWS references:** [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html), [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html).

</details>

## Card 04

**Question:** Tightly coupled EC2 workers need low-latency communication inside one Availability Zone. Which common placement strategy targets this requirement?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** A cluster placement group. A cluster placement group places supported instances close together in one AZ for tightly coupled workloads. This is a performance choice, not protection from losing that AZ.

**AWS references:** [EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html).

</details>

## Card 05

**Question:** A team buys a Compute Savings Plan for its steady baseline. Which statement is accurate?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** It discounts eligible usage in exchange for a spend commitment; it does not by itself reserve EC2 capacity. Savings Plans are pricing commitments. Capacity reservations are a separate design consideration, and unused commitment can reduce realized savings.

**AWS references:** [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html), [EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html), [EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html).

</details>

## Card 06

**Question:** An EC2 instance is in one Availability Zone and an EBS volume is in another. How can the data be made available as an attachable EBS volume to that instance?

Why does this alternative fail: “Attach the existing volume directly across Availability Zones.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** EBS attachment is not cross-AZ.

**AWS references:** [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html).

</details>

## Card 07

**Question:** Linux EC2 instances in multiple Availability Zones need concurrent access to the same managed NFS file system. Which choice fits?

Why does this alternative fail: “An ordinary single EBS volume attached across Availability Zones.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Ordinary EBS attachment does not provide multi-AZ NFS sharing.

**AWS references:** [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html), [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html).

</details>

## Card 08

**Question:** Tightly coupled EC2 workers need low-latency communication inside one Availability Zone. Which common placement strategy targets this requirement?

Why does this alternative fail: “A spread placement group selected specifically to separate underlying hardware.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Spread prioritizes hardware separation rather than tightly packed placement.

**AWS references:** [EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

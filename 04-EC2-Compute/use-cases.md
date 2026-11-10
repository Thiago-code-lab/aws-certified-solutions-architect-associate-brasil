# Use Cases

## Scenario 1: Interruptible compute

**Requirement:** A batch job checkpoints its progress and can resume after interruption. It has a flexible completion window. Which EC2 purchase option is designed for spare capacity at a discount?

**Recommended design:** Spot Instances.

**Reason and boundary:** Spot uses spare EC2 capacity and can be interrupted. Checkpointing and flexible scheduling make the stated batch workload a suitable candidate, subject to capacity availability.

**Rejected alternative:** Dedicated Hosts solely to obtain the lowest batch price. Dedicated hardware addresses isolation or licensing, not this spare-capacity objective.

**AWS references:** [EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html), [EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html).

## Scenario 2: EBS Availability Zone scope

**Requirement:** An EC2 instance is in one Availability Zone and an EBS volume is in another. How can the data be made available as an attachable EBS volume to that instance?

**Recommended design:** Create a snapshot and create a new volume from it in the instance Availability Zone.

**Reason and boundary:** An EBS volume attaches to instances in its own Availability Zone. A snapshot can be used to create a volume in another Availability Zone in the Region.

**Rejected alternative:** Attach the existing volume directly across Availability Zones. EBS attachment is not cross-AZ.

**AWS references:** [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html).

## Scenario 3: Shared file storage

**Requirement:** Linux EC2 instances in multiple Availability Zones need concurrent access to the same managed NFS file system. Which choice fits?

**Recommended design:** Amazon EFS Regional with mount targets and suitable security group rules.

**Reason and boundary:** EFS provides managed shared NFS storage; the Regional storage option supports a multi-AZ design. Mount targets and network access still need configuration.

**Rejected alternative:** An ordinary single EBS volume attached across Availability Zones. Ordinary EBS attachment does not provide multi-AZ NFS sharing.

**AWS references:** [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html), [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html).

## Scenario 4: Low-latency placement

**Requirement:** Tightly coupled EC2 workers need low-latency communication inside one Availability Zone. Which common placement strategy targets this requirement?

**Recommended design:** A cluster placement group.

**Reason and boundary:** A cluster placement group places supported instances close together in one AZ for tightly coupled workloads. This is a performance choice, not protection from losing that AZ.

**Rejected alternative:** A spread placement group selected specifically to separate underlying hardware. Spread prioritizes hardware separation rather than tightly packed placement.

**AWS references:** [EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

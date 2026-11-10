# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Interruptible compute | Spot Instances. | Spot uses spare EC2 capacity and can be interrupted. Checkpointing and flexible scheduling make the stated batch workload a suitable candidate, subject to capacity availability. |
| EBS Availability Zone scope | Create a snapshot and create a new volume from it in the instance Availability Zone. | An EBS volume attaches to instances in its own Availability Zone. A snapshot can be used to create a volume in another Availability Zone in the Region. |
| Shared file storage | Amazon EFS Regional with mount targets and suitable security group rules. | EFS provides managed shared NFS storage; the Regional storage option supports a multi-AZ design. Mount targets and network access still need configuration. |
| Low-latency placement | A cluster placement group. | A cluster placement group places supported instances close together in one AZ for tightly coupled workloads. This is a performance choice, not protection from losing that AZ. |
| Pricing commitment versus capacity | It discounts eligible usage in exchange for a spend commitment; it does not by itself reserve EC2 capacity. | Savings Plans are pricing commitments. Capacity reservations are a separate design consideration, and unused commitment can reduce realized savings. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Interruptible compute:** Dedicated hardware addresses isolation or licensing, not this spare-capacity objective.
- **EBS Availability Zone scope:** EBS attachment is not cross-AZ.
- **Shared file storage:** Ordinary EBS attachment does not provide multi-AZ NFS sharing.
- **Low-latency placement:** Spread prioritizes hardware separation rather than tightly packed placement.
- **Pricing commitment versus capacity:** A pricing commitment is not a capacity guarantee.

## AWS References

[EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html), [EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html), [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html), [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html), [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

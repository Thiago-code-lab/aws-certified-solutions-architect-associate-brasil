# EC2 Compute

## Overview

Choose EC2 compute, storage, placement, and pricing from workload requirements. Separate interruption tolerance, Availability Zone scope, shared file access, pricing commitments, and capacity reservations.

## Key Concepts

- **Interruptible compute:** Spot uses spare EC2 capacity and can be interrupted. Checkpointing and flexible scheduling make the stated batch workload a suitable candidate, subject to capacity availability.
- **EBS Availability Zone scope:** An EBS volume attaches to instances in its own Availability Zone. A snapshot can be used to create a volume in another Availability Zone in the Region.
- **Shared file storage:** EFS provides managed shared NFS storage; the Regional storage option supports a multi-AZ design. Mount targets and network access still need configuration.
- **Low-latency placement:** A cluster placement group places supported instances close together in one AZ for tightly coupled workloads. This is a performance choice, not protection from losing that AZ.
- **Pricing commitment versus capacity:** Savings Plans are pricing commitments. Capacity reservations are a separate design consideration, and unused commitment can reduce realized savings.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Interruptible compute:** Spot Instances.
2. **EBS Availability Zone scope:** Create a snapshot and create a new volume from it in the instance Availability Zone.
3. **Shared file storage:** Amazon EFS Regional with mount targets and suitable security group rules.
4. **Low-latency placement:** A cluster placement group.
5. **Pricing commitment versus capacity:** It discounts eligible usage in exchange for a spend commitment; it does not by itself reserve EC2 capacity.

## Common Pitfalls

- Dedicated hardware addresses isolation or licensing, not this spare-capacity objective.
- EBS attachment is not cross-AZ.
- Ordinary EBS attachment does not provide multi-AZ NFS sharing.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html), [EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html), [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html), [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html), [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

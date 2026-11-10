# Guided Lab

## Objective

Verify that EBS volume attachment is scoped to an Availability Zone.

## Services Used

EC2, EBS, and EBS snapshots.

## Expected Cost Range

EC2 runtime, EBS volumes, snapshots, and public IPv4 addresses can incur charges. Estimate the selected sizes and Region before launching.

## Step-by-Step Instructions

1. Choose an isolated lab account, one Region, and two AZs; tag every created resource for cleanup.
2. Create a small test EBS volume in the first AZ and a supported small EC2 instance in the second AZ using approved access and networking.
3. Inspect attachment eligibility and confirm the first-AZ volume cannot attach to the second-AZ instance.
4. Create a snapshot of the test volume and wait until the snapshot is complete.
5. Create a new volume from the snapshot in the instance AZ and attach that new volume to the instance.
6. Record the volume AZs, attachment state, and the distinction between a volume and a snapshot.

## Validation

- Only the volume in the instance AZ can be attached.
- The copied volume is a new resource, not a cross-AZ attachment.
- No production volume or snapshot is used.

## Cleanup

1. Detach and delete both lab volumes when no longer needed.
2. Terminate the lab instance and inspect its remaining volumes.
3. Delete the lab snapshot after confirming no retention requirement applies.
4. Release lab public addresses and review the inventory and delayed billing data.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

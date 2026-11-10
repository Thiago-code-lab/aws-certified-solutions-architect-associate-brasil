# Guided Lab

## Objective

Measure a bounded backup restoration against explicit RPO and RTO targets.

## Services Used

A dedicated S3 versioned test dataset or another approved nonproduction backup system.

## Expected Cost Range

Small object storage, versioning, requests, and any optional recovery infrastructure can incur charges. Do not create a full standby Region solely for this basic restoration exercise.

## Step-by-Step Instructions

1. Write a concrete acceptable data-loss window and recovery-time target for the test dataset.
2. Create a small synthetic dataset and retain a known recoverable version or backup.
3. Record the backup point, apply a controlled change only to the test data, and record the time the simulated disruption is declared.
4. Restore the selected valid version into an isolated recovery location and validate its contents.
5. Measure the restored data age relative to the last valid writes and the full elapsed recovery duration.
6. Compare those observations with RPO and RTO. Explain which additional infrastructure, configuration, and traffic changes a real regional workload recovery would require.

## Validation

- Recovered contents match the chosen valid recovery point.
- Data-loss window and restoration duration are measured separately.
- An object restoration is not mislabeled as proof of complete regional application recovery.

## Cleanup

1. Remove only the synthetic restored copies and disposable versions.
2. Keep required evidence or backups until their lab retention decision permits deletion.
3. Inspect all retained versions and recovery resources for ongoing charges.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Guided Lab

## Objective

Recover a versioned S3 test object and inspect retention costs without locking data irreversibly.

## Services Used

S3 Versioning, Lifecycle, and private bucket access.

## Expected Cost Range

Storage, requests, versions, and optional retrievals can incur charges. Use small non-sensitive files. This exercise does not require Object Lock compliance retention.

## Step-by-Step Instructions

1. Create a private general-purpose S3 lab bucket with Block Public Access enabled and enable versioning.
2. Upload a small text file under training/ and record its version ID.
3. Overwrite the same key with different test contents and compare the two versions.
4. Delete the key without specifying a version and inspect the resulting delete marker and retained earlier versions.
5. Retrieve the earlier version, then restore the desired contents by making a new current version or removing the relevant delete marker when appropriate.
6. Draft a lifecycle policy for noncurrent lab versions; review eligibility and minimum-duration implications before enabling transitions.

## Validation

- Earlier version contents remain retrievable while that version is retained.
- A delete marker is not mistaken for permanent erasure of all versions.
- The bucket remains private throughout the exercise.

## Cleanup

1. Remove the lab lifecycle configuration if it is no longer needed.
2. Delete only the lab object versions and delete markers, then delete the empty bucket.
3. Check that retention or legal-hold settings do not block intended cleanup.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html), [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html), [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

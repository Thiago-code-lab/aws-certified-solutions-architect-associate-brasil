# Guided Lab

## Objective

Evaluate least-privilege object-read permissions in an isolated policy exercise.

## Services Used

IAM policy editor, policy validation, and policy simulation.

## Expected Cost Range

Policy exercise; no EC2 instance, database, or production access key is required. Review any account-specific tooling costs before use.

## Step-by-Step Instructions

1. Define a fictional test-bucket object prefix training/ and write the requirement: read objects in that prefix, with no write or delete access.
2. In the IAM policy editor, create a candidate statement allowing only s3:GetObject on the object ARN pattern for that prefix. Do not use a bucket ARN for an object action.
3. Validate the policy and resolve syntax or overly broad resource warnings before proceeding.
4. Use a policy simulation to test GetObject inside the prefix, GetObject outside it, PutObject, and DeleteObject.
5. Record that identity simulation does not by itself validate every live bucket policy, organization policy, endpoint policy, or runtime request context.

## Validation

- The intended GetObject request is allowed by the candidate identity policy.
- Other tested actions or object resources are not allowed by that policy.
- No long-lived credential is created or committed.

## Cleanup

1. Remove any unattached draft policy created only for this exercise.
2. Do not detach policies from production identities.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

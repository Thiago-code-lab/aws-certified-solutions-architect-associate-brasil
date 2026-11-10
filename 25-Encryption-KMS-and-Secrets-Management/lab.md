# Guided Lab

## Objective

Distinguish configuration, secret rotation, and KMS key material using test-only data.

## Services Used

Parameter Store, Secrets Manager, KMS, and their official documentation.

## Expected Cost Range

Secrets, customer managed KMS keys, API operations, and optional rotation functions can incur charges. Use synthetic values and do not schedule key deletion on a shared key.

## Step-by-Step Instructions

1. Create a non-secret lab configuration parameter, retrieve it, update it, and inspect its version history.
2. Create a separate synthetic lab secret only if the cost plan allows it; grant retrieval only to the intended lab principal.
3. Review the secret encryption key type and distinguish its key policy from the permission to retrieve the secret.
4. Read the supported secret-rotation options and describe how the target credential and stored value must be updated together. Do not claim that changing a secret string has rotated a real database password.
5. Review KMS key-material rotation and state explicitly that it does not rewrite existing protected data or rotate application passwords.
6. Record how HTTPS/TLS protects transport separately from KMS-backed at-rest encryption.

## Validation

- Configuration parameter versioning is observed independently from secret rotation.
- No production credential is used or printed.
- The notes separate key rotation, credential rotation, authorization, and transport.

## Cleanup

1. Delete disposable parameters and schedule disposal of synthetic secrets using the applicable supported recovery policy.
2. Delete lab-only rotation resources if created.
3. For a lab-only KMS key, review the mandatory deletion waiting period and retained ciphertext dependencies before scheduling deletion.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html), [AWS KMS key concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html), [KMS key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

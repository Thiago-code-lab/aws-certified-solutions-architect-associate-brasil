# Review Flashcards

## Card 01

**Question:** An application must store a database credential and rotate that credential in both the secret store and the database. Which service directly provides this secret lifecycle capability?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** AWS Secrets Manager with a supported rotation integration or correctly configured rotation function. Secrets Manager rotation updates the secret and the target service using a supported mechanism. KMS protects cryptographic keys and data; rotating KMS material does not change a database password.

**AWS references:** [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html), [KMS key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html).

</details>

## Card 02

**Question:** Automatic rotation changes the key material of a supported customer managed KMS key. What happens to existing data protected by that key?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** It is not automatically re-encrypted; KMS retains the material required to decrypt earlier ciphertext. KMS rotation changes backing key material for future cryptographic operations. It does not rotate generated data keys or rewrite application data, and it is not secret credential rotation.

**AWS references:** [KMS key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html), [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

</details>

## Card 03

**Question:** A regulated workload needs the customer to control a KMS key policy and its deletion lifecycle. Which key type fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** A customer managed KMS key. Customer managed keys let customers manage key policies and lifecycle settings, subject to KMS controls. AWS owned keys are managed by the service and do not provide that customer policy control.

**AWS references:** [AWS KMS key concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html).

</details>

## Card 04

**Question:** A team needs versioned retrieval of a non-secret application configuration value. It does not require credential rotation. Which service is a suitable key-value configuration store?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Systems Manager Parameter Store. Parameter Store supports centrally managed parameter values and versioning. SecureString adds KMS encryption when needed; secrets requiring purpose-built rotation should use an appropriate secrets service.

**AWS references:** [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

</details>

## Card 05

**Question:** An S3 object uses SSE-KMS. A policy also requires encrypted transport for clients. What additional transport requirement is appropriate?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Require HTTPS/TLS for the client connection and enforce the relevant access policy. SSE-KMS protects object data at rest. TLS protects the network connection; authorization and transport enforcement are separate controls.

**AWS references:** [AWS KMS key concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [Direct Connect encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html).

</details>

## Card 06

**Question:** Automatic rotation changes the key material of a supported customer managed KMS key. What happens to existing data protected by that key?

Why does this alternative fail: “Every protected object is immediately rewritten using new data keys.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Rotation alone does not rewrite protected data or rotate all data keys.

**AWS references:** [KMS key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html), [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

</details>

## Card 07

**Question:** A regulated workload needs the customer to control a KMS key policy and its deletion lifecycle. Which key type fits?

Why does this alternative fail: “An AWS owned key whose policy the customer cannot manage.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Customers cannot manage the policy and deletion lifecycle of an AWS owned key.

**AWS references:** [AWS KMS key concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html).

</details>

## Card 08

**Question:** A team needs versioned retrieval of a non-secret application configuration value. It does not require credential rotation. Which service is a suitable key-value configuration store?

Why does this alternative fail: “A KMS key alias used as the entire configuration database.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** A key alias identifies a KMS key and is not a general configuration store.

**AWS references:** [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

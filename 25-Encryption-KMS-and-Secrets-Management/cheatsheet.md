# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Key management versus secret rotation | AWS Secrets Manager with a supported rotation integration or correctly configured rotation function. | Secrets Manager rotation updates the secret and the target service using a supported mechanism. KMS protects cryptographic keys and data; rotating KMS material does not change a database password. |
| KMS rotation is not re-encryption | It is not automatically re-encrypted; KMS retains the material required to decrypt earlier ciphertext. | KMS rotation changes backing key material for future cryptographic operations. It does not rotate generated data keys or rewrite application data, and it is not secret credential rotation. |
| Customer-controlled key policy | A customer managed KMS key. | Customer managed keys let customers manage key policies and lifecycle settings, subject to KMS controls. AWS owned keys are managed by the service and do not provide that customer policy control. |
| Configuration versus rotating credential | Systems Manager Parameter Store. | Parameter Store supports centrally managed parameter values and versioning. SecureString adds KMS encryption when needed; secrets requiring purpose-built rotation should use an appropriate secrets service. |
| Encryption at rest versus transport | Require HTTPS/TLS for the client connection and enforce the relevant access policy. | SSE-KMS protects object data at rest. TLS protects the network connection; authorization and transport enforcement are separate controls. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Key management versus secret rotation:** Key rotation and credential rotation are different operations.
- **KMS rotation is not re-encryption:** Rotation alone does not rewrite protected data or rotate all data keys.
- **Customer-controlled key policy:** Customers cannot manage the policy and deletion lifecycle of an AWS owned key.
- **Configuration versus rotating credential:** A key alias identifies a KMS key and is not a general configuration store.
- **Encryption at rest versus transport:** At-rest encryption is not a blanket transport-encryption guarantee.

## AWS References

[Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html), [KMS key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html), [AWS KMS key concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html), [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [Direct Connect encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

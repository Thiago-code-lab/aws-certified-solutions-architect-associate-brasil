# Encryption, KMS, and Secrets Management

## Overview

Separate cryptographic key management, encrypted configuration storage, credential rotation, and transport security. Use current KMS key terminology and an explicit policy and lifecycle design.

## Key Concepts

- **Key management versus secret rotation:** Secrets Manager rotation updates the secret and the target service using a supported mechanism. KMS protects cryptographic keys and data; rotating KMS material does not change a database password.
- **KMS rotation is not re-encryption:** KMS rotation changes backing key material for future cryptographic operations. It does not rotate generated data keys or rewrite application data, and it is not secret credential rotation.
- **Customer-controlled key policy:** Customer managed keys let customers manage key policies and lifecycle settings, subject to KMS controls. AWS owned keys are managed by the service and do not provide that customer policy control.
- **Configuration versus rotating credential:** Parameter Store supports centrally managed parameter values and versioning. SecureString adds KMS encryption when needed; secrets requiring purpose-built rotation should use an appropriate secrets service.
- **Encryption at rest versus transport:** SSE-KMS protects object data at rest. TLS protects the network connection; authorization and transport enforcement are separate controls.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Key management versus secret rotation:** AWS Secrets Manager with a supported rotation integration or correctly configured rotation function.
2. **KMS rotation is not re-encryption:** It is not automatically re-encrypted; KMS retains the material required to decrypt earlier ciphertext.
3. **Customer-controlled key policy:** A customer managed KMS key.
4. **Configuration versus rotating credential:** Systems Manager Parameter Store.
5. **Encryption at rest versus transport:** Require HTTPS/TLS for the client connection and enforce the relevant access policy.

## Common Pitfalls

- Key rotation and credential rotation are different operations.
- Rotation alone does not rewrite protected data or rotate all data keys.
- Customers cannot manage the policy and deletion lifecycle of an AWS owned key.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html), [KMS key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html), [AWS KMS key concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html), [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [Direct Connect encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

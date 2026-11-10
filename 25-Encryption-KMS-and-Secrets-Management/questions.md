# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 25-Q01 -->

An application must store a database credential and rotate that credential in both the secret store and the database. Which service directly provides this secret lifecycle capability?

A) AWS KMS key-material rotation alone.

B) A security group rule.

C) A plaintext constant in the application image.

D) AWS Secrets Manager with a supported rotation integration or correctly configured rotation function.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Secrets Manager rotation updates the secret and the target service using a supported mechanism. KMS protects cryptographic keys and data; rotating KMS material does not change a database password.

**Why the other options are incorrect:**

- **A:** Key rotation and credential rotation are different operations.
- **B:** Network filtering does not store and rotate credentials.
- **C:** A baked-in plaintext value does not implement controlled secret rotation.

**AWS references:** [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html), [KMS key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html).

</details>

## Question 2

<!-- question-id: 25-Q02 -->

Automatic rotation changes the key material of a supported customer managed KMS key. What happens to existing data protected by that key?

A) Every protected object is immediately rewritten using new data keys.

B) All earlier ciphertext becomes undecryptable immediately.

C) The application database password changes automatically.

D) It is not automatically re-encrypted; KMS retains the material required to decrypt earlier ciphertext.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** KMS rotation changes backing key material for future cryptographic operations. It does not rotate generated data keys or rewrite application data, and it is not secret credential rotation.

**Why the other options are incorrect:**

- **A:** Rotation alone does not rewrite protected data or rotate all data keys.
- **B:** KMS retains earlier material so valid earlier ciphertext remains decryptable.
- **C:** A database credential requires a separate secret-rotation mechanism.

**AWS references:** [KMS key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html), [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

</details>

## Question 3

<!-- question-id: 25-Q03 -->

A regulated workload needs the customer to control a KMS key policy and its deletion lifecycle. Which key type fits?

A) An AWS owned key whose policy the customer cannot manage.

B) A customer managed KMS key.

C) A public TLS certificate alone.

D) An IAM access key treated as a KMS encryption key.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Customer managed keys let customers manage key policies and lifecycle settings, subject to KMS controls. AWS owned keys are managed by the service and do not provide that customer policy control.

**Why the other options are incorrect:**

- **A:** Customers cannot manage the policy and deletion lifecycle of an AWS owned key.
- **C:** A certificate is not the requested KMS key resource.
- **D:** An IAM credential signs API requests and is not a KMS key.

**AWS references:** [AWS KMS key concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html).

</details>

## Question 4

<!-- question-id: 25-Q04 -->

A team needs versioned retrieval of a non-secret application configuration value. It does not require credential rotation. Which service is a suitable key-value configuration store?

A) Systems Manager Parameter Store.

B) A KMS key alias used as the entire configuration database.

C) An SQS dead-letter queue as the configuration source.

D) A public repository containing production passwords.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Parameter Store supports centrally managed parameter values and versioning. SecureString adds KMS encryption when needed; secrets requiring purpose-built rotation should use an appropriate secrets service.

**Why the other options are incorrect:**

- **B:** A key alias identifies a KMS key and is not a general configuration store.
- **C:** A DLQ is for failed message handling, not stable versioned configuration.
- **D:** Publishing credentials is neither required nor appropriate for non-secret configuration management.

**AWS references:** [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

</details>

## Question 5

<!-- question-id: 25-Q05 -->

An S3 object uses SSE-KMS. A policy also requires encrypted transport for clients. What additional transport requirement is appropriate?

A) Assume SSE-KMS encrypts every network connection automatically.

B) Remove authentication because the object is encrypted at rest.

C) Require HTTPS/TLS for the client connection and enforce the relevant access policy.

D) Store the KMS plaintext key material in the URL.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** SSE-KMS protects object data at rest. TLS protects the network connection; authorization and transport enforcement are separate controls.

**Why the other options are incorrect:**

- **A:** At-rest encryption is not a blanket transport-encryption guarantee.
- **B:** Encryption does not replace authentication and authorization.
- **D:** Exposing key material is unsafe and not the KMS service model.

**AWS references:** [AWS KMS key concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [Direct Connect encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

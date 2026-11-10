# Use Cases

## Scenario 1: Key management versus secret rotation

**Requirement:** An application must store a database credential and rotate that credential in both the secret store and the database. Which service directly provides this secret lifecycle capability?

**Recommended design:** AWS Secrets Manager with a supported rotation integration or correctly configured rotation function.

**Reason and boundary:** Secrets Manager rotation updates the secret and the target service using a supported mechanism. KMS protects cryptographic keys and data; rotating KMS material does not change a database password.

**Rejected alternative:** AWS KMS key-material rotation alone. Key rotation and credential rotation are different operations.

**AWS references:** [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html), [KMS key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html).

## Scenario 2: KMS rotation is not re-encryption

**Requirement:** Automatic rotation changes the key material of a supported customer managed KMS key. What happens to existing data protected by that key?

**Recommended design:** It is not automatically re-encrypted; KMS retains the material required to decrypt earlier ciphertext.

**Reason and boundary:** KMS rotation changes backing key material for future cryptographic operations. It does not rotate generated data keys or rewrite application data, and it is not secret credential rotation.

**Rejected alternative:** Every protected object is immediately rewritten using new data keys. Rotation alone does not rewrite protected data or rotate all data keys.

**AWS references:** [KMS key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html), [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

## Scenario 3: Customer-controlled key policy

**Requirement:** A regulated workload needs the customer to control a KMS key policy and its deletion lifecycle. Which key type fits?

**Recommended design:** A customer managed KMS key.

**Reason and boundary:** Customer managed keys let customers manage key policies and lifecycle settings, subject to KMS controls. AWS owned keys are managed by the service and do not provide that customer policy control.

**Rejected alternative:** An AWS owned key whose policy the customer cannot manage. Customers cannot manage the policy and deletion lifecycle of an AWS owned key.

**AWS references:** [AWS KMS key concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html).

## Scenario 4: Configuration versus rotating credential

**Requirement:** A team needs versioned retrieval of a non-secret application configuration value. It does not require credential rotation. Which service is a suitable key-value configuration store?

**Recommended design:** Systems Manager Parameter Store.

**Reason and boundary:** Parameter Store supports centrally managed parameter values and versioning. SecureString adds KMS encryption when needed; secrets requiring purpose-built rotation should use an appropriate secrets service.

**Rejected alternative:** A KMS key alias used as the entire configuration database. A key alias identifies a KMS key and is not a general configuration store.

**AWS references:** [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 02-Q01 -->

An EC2 application needs to read objects only from one S3 prefix. What is the recommended credential and permission design?

A) An instance role with temporary credentials and s3:GetObject scoped to the required object prefix.

B) A shared IAM user with AdministratorAccess embedded in the application.

C) A root access key copied onto each instance.

D) An IAM role with no allow policy, relying only on a descriptive role name.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Roles avoid distributing long-lived keys. The object ARN scope and permitted action must match the required prefix; a role name alone grants nothing.

**Why the other options are incorrect:**

- **B:** Shared administrator credentials violate the temporary-credential and least-privilege requirements.
- **C:** Root credentials provide unnecessary privileges and must be protected.
- **D:** A role needs applicable permissions for the requested action.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

</details>

## Question 2

<!-- question-id: 02-Q02 -->

An identity policy allows an S3 action, but an applicable bucket policy explicitly denies that same request. What is the authorization result?

A) The request is denied.

B) The identity allow always overrides the bucket policy.

C) The newer policy automatically wins.

D) AWS selects an outcome at random when policies conflict.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** An applicable explicit deny overrides an allow for the same request. Policy creation time does not determine authorization precedence.

**Why the other options are incorrect:**

- **B:** An explicit deny is not overridden by an identity allow.
- **C:** Policy evaluation is based on policy logic, not recency.
- **D:** Authorization uses deterministic evaluation rules.

**AWS references:** [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

</details>

## Question 3

<!-- question-id: 02-Q03 -->

A member account has an SCP that allows S3 actions, but a new IAM role has no identity or resource policy granting S3 access. What does the SCP provide?

A) An automatic grant of every S3 action to the role.

B) A temporary access key for the role.

C) A permissions ceiling; the role still needs an applicable permission grant.

D) An S3 bucket containing all permitted resources.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** SCPs limit permissions in member accounts and do not grant access. Applicable identity or resource policies must grant the action within those limits.

**Why the other options are incorrect:**

- **A:** An allow in an SCP is not itself an IAM permission grant.
- **B:** SCPs do not issue credentials.
- **D:** Organization policies do not create storage resources.

**AWS references:** [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

</details>

## Question 4

<!-- question-id: 02-Q04 -->

Employees need centrally managed sign-in to several AWS accounts with short-lived sessions. Which approach best fits?

A) Share one root account password across all employees.

B) Create a shared administrator access key for the entire workforce.

C) Use security group rules to assign IAM account permissions.

D) Use IAM Identity Center with account assignments and permission sets.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** IAM Identity Center supports centralized workforce access to AWS accounts. Permission sets define the account permissions available through the assigned sessions.

**Why the other options are incorrect:**

- **A:** Root sharing removes individual accountability and exposes privileged credentials.
- **B:** A shared long-lived key does not provide individual federated sessions.
- **C:** Security groups control network traffic, not IAM workforce permissions.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

## Question 5

<!-- question-id: 02-Q05 -->

A production role has broader permissions than its observed workload requires. Which improvement follows AWS least-privilege guidance?

A) Add AdministratorAccess to avoid permission errors.

B) Remove all logging before changing the policy.

C) Replace the role with a root access key.

D) Review access activity, generate and validate a scoped policy, test required operations, and remove unused permissions.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Access analysis and testing help reduce permissions while preserving required behavior. Observed activity is evidence, but infrequent legitimate operations must also be considered.

**Why the other options are incorrect:**

- **A:** Adding administrator permissions increases the problem.
- **B:** Removing logs discards evidence needed for review and investigation.
- **C:** Root credentials are not a least-privilege substitute for a workload role.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

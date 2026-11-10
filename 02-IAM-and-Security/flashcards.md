# Review Flashcards

## Card 01

**Question:** An EC2 application needs to read objects only from one S3 prefix. What is the recommended credential and permission design?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** An instance role with temporary credentials and s3:GetObject scoped to the required object prefix. Roles avoid distributing long-lived keys. The object ARN scope and permitted action must match the required prefix; a role name alone grants nothing.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

</details>

## Card 02

**Question:** An identity policy allows an S3 action, but an applicable bucket policy explicitly denies that same request. What is the authorization result?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The request is denied. An applicable explicit deny overrides an allow for the same request. Policy creation time does not determine authorization precedence.

**AWS references:** [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

</details>

## Card 03

**Question:** A member account has an SCP that allows S3 actions, but a new IAM role has no identity or resource policy granting S3 access. What does the SCP provide?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** A permissions ceiling; the role still needs an applicable permission grant. SCPs limit permissions in member accounts and do not grant access. Applicable identity or resource policies must grant the action within those limits.

**AWS references:** [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

</details>

## Card 04

**Question:** Employees need centrally managed sign-in to several AWS accounts with short-lived sessions. Which approach best fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Use IAM Identity Center with account assignments and permission sets. IAM Identity Center supports centralized workforce access to AWS accounts. Permission sets define the account permissions available through the assigned sessions.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

## Card 05

**Question:** A production role has broader permissions than its observed workload requires. Which improvement follows AWS least-privilege guidance?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Review access activity, generate and validate a scoped policy, test required operations, and remove unused permissions. Access analysis and testing help reduce permissions while preserving required behavior. Observed activity is evidence, but infrequent legitimate operations must also be considered.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

## Card 06

**Question:** An identity policy allows an S3 action, but an applicable bucket policy explicitly denies that same request. What is the authorization result?

Why does this alternative fail: “The identity allow always overrides the bucket policy.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** An explicit deny is not overridden by an identity allow.

**AWS references:** [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

</details>

## Card 07

**Question:** A member account has an SCP that allows S3 actions, but a new IAM role has no identity or resource policy granting S3 access. What does the SCP provide?

Why does this alternative fail: “An automatic grant of every S3 action to the role.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** An allow in an SCP is not itself an IAM permission grant.

**AWS references:** [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

</details>

## Card 08

**Question:** Employees need centrally managed sign-in to several AWS accounts with short-lived sessions. Which approach best fits?

Why does this alternative fail: “Share one root account password across all employees.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Root sharing removes individual accountability and exposes privileged credentials.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

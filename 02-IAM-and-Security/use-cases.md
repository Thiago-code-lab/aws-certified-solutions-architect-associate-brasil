# Use Cases

## Scenario 1: Temporary workload credentials

**Requirement:** An EC2 application needs to read objects only from one S3 prefix. What is the recommended credential and permission design?

**Recommended design:** An instance role with temporary credentials and s3:GetObject scoped to the required object prefix.

**Reason and boundary:** Roles avoid distributing long-lived keys. The object ARN scope and permitted action must match the required prefix; a role name alone grants nothing.

**Rejected alternative:** A shared IAM user with AdministratorAccess embedded in the application. Shared administrator credentials violate the temporary-credential and least-privilege requirements.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

## Scenario 2: Explicit deny precedence

**Requirement:** An identity policy allows an S3 action, but an applicable bucket policy explicitly denies that same request. What is the authorization result?

**Recommended design:** The request is denied.

**Reason and boundary:** An applicable explicit deny overrides an allow for the same request. Policy creation time does not determine authorization precedence.

**Rejected alternative:** The identity allow always overrides the bucket policy. An explicit deny is not overridden by an identity allow.

**AWS references:** [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

## Scenario 3: SCPs are guardrails

**Requirement:** A member account has an SCP that allows S3 actions, but a new IAM role has no identity or resource policy granting S3 access. What does the SCP provide?

**Recommended design:** A permissions ceiling; the role still needs an applicable permission grant.

**Reason and boundary:** SCPs limit permissions in member accounts and do not grant access. Applicable identity or resource policies must grant the action within those limits.

**Rejected alternative:** An automatic grant of every S3 action to the role. An allow in an SCP is not itself an IAM permission grant.

**AWS references:** [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

## Scenario 4: Workforce access

**Requirement:** Employees need centrally managed sign-in to several AWS accounts with short-lived sessions. Which approach best fits?

**Recommended design:** Use IAM Identity Center with account assignments and permission sets.

**Reason and boundary:** IAM Identity Center supports centralized workforce access to AWS accounts. Permission sets define the account permissions available through the assigned sessions.

**Rejected alternative:** Share one root account password across all employees. Root sharing removes individual accountability and exposes privileged credentials.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

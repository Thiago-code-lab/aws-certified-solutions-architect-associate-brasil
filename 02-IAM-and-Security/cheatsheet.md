# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Temporary workload credentials | An instance role with temporary credentials and s3:GetObject scoped to the required object prefix. | Roles avoid distributing long-lived keys. The object ARN scope and permitted action must match the required prefix; a role name alone grants nothing. |
| Explicit deny precedence | The request is denied. | An applicable explicit deny overrides an allow for the same request. Policy creation time does not determine authorization precedence. |
| SCPs are guardrails | A permissions ceiling; the role still needs an applicable permission grant. | SCPs limit permissions in member accounts and do not grant access. Applicable identity or resource policies must grant the action within those limits. |
| Workforce access | Use IAM Identity Center with account assignments and permission sets. | IAM Identity Center supports centralized workforce access to AWS accounts. Permission sets define the account permissions available through the assigned sessions. |
| Least privilege analysis | Review access activity, generate and validate a scoped policy, test required operations, and remove unused permissions. | Access analysis and testing help reduce permissions while preserving required behavior. Observed activity is evidence, but infrequent legitimate operations must also be considered. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Temporary workload credentials:** Shared administrator credentials violate the temporary-credential and least-privilege requirements.
- **Explicit deny precedence:** An explicit deny is not overridden by an identity allow.
- **SCPs are guardrails:** An allow in an SCP is not itself an IAM permission grant.
- **Workforce access:** Root sharing removes individual accountability and exposes privileged credentials.
- **Least privilege analysis:** Adding administrator permissions increases the problem.

## AWS References

[IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html), [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

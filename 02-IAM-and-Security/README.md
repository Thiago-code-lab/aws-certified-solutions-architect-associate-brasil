# IAM and Security

## Overview

Design access using temporary credentials, least privilege, explicit policy evaluation, and appropriate organization guardrails. Network controls and encryption complement authorization; they do not replace it.

## Key Concepts

- **Temporary workload credentials:** Roles avoid distributing long-lived keys. The object ARN scope and permitted action must match the required prefix; a role name alone grants nothing.
- **Explicit deny precedence:** An applicable explicit deny overrides an allow for the same request. Policy creation time does not determine authorization precedence.
- **SCPs are guardrails:** SCPs limit permissions in member accounts and do not grant access. Applicable identity or resource policies must grant the action within those limits.
- **Workforce access:** IAM Identity Center supports centralized workforce access to AWS accounts. Permission sets define the account permissions available through the assigned sessions.
- **Least privilege analysis:** Access analysis and testing help reduce permissions while preserving required behavior. Observed activity is evidence, but infrequent legitimate operations must also be considered.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Temporary workload credentials:** An instance role with temporary credentials and s3:GetObject scoped to the required object prefix.
2. **Explicit deny precedence:** The request is denied.
3. **SCPs are guardrails:** A permissions ceiling; the role still needs an applicable permission grant.
4. **Workforce access:** Use IAM Identity Center with account assignments and permission sets.
5. **Least privilege analysis:** Review access activity, generate and validate a scoped policy, test required operations, and remove unused permissions.

## Common Pitfalls

- Shared administrator credentials violate the temporary-credential and least-privilege requirements.
- An explicit deny is not overridden by an identity allow.
- An allow in an SCP is not itself an IAM permission grant.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html), [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Primary exam reference | The current AWS SAA-C03 exam guide. | AWS defines the exam content domains and scored-content weights. Community question counts and promotional statements do not define the exam blueprint. |
| Exam scope is not a frequency guarantee | It is within the published scope, but the list does not promise a fixed number of questions for that service. | The guide describes scope and says the service list is non-exhaustive and subject to change. Exam coverage, deployment availability, and the correctness of a study explanation are separate questions. |
| Service-specific documentation | Current RDS documentation distinguishing Multi-AZ DB instance deployments from Multi-AZ DB cluster deployments. | The deployment-specific documentation establishes the distinction: a DB instance standby does not serve reads, while Multi-AZ DB cluster readers can serve reads. |
| Verify live service availability | Check current AWS availability and lifecycle notices, then select an eligible transfer approach for the actual customer and date. | Historical learning value does not guarantee present deployment availability. Current service notices must inform actual implementation decisions. |
| Evidence-backed content correction | Identify the exact question, define the scenario assumptions, cite applicable AWS documentation, and update the answer plus all affected explanations together. | A defensible correction aligns the stem, alternatives, answer, and explanation under explicit assumptions. Traceable references and a question identifier let reviewers evaluate the change. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Primary exam reference:** A practice set distribution is an editorial choice, not the exam definition.
- **Exam scope is not a frequency guarantee:** The guide does not assign a fixed per-service question count.
- **Service-specific documentation:** A summary without the deployment scope repeats the ambiguity rather than resolving it.
- **Verify live service availability:** Document availability does not establish service-order eligibility.
- **Evidence-backed content correction:** A letter-only edit can leave the explanation and alternatives contradictory.

## AWS References

[SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html), [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html), [AWS Snowball availability notice](https://aws.amazon.com/snowball/), [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [Snowball availability history](https://docs.aws.amazon.com/snowball/latest/developer-guide/doc-history.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

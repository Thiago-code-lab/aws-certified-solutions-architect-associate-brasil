# Resources and Links

## Overview

Use the official exam guide for scope and weights, service-specific documentation for behavior, and current lifecycle notices for deployment availability. Community study aids complement these primary references.

## Key Concepts

- **Primary exam reference:** AWS defines the exam content domains and scored-content weights. Community question counts and promotional statements do not define the exam blueprint.
- **Exam scope is not a frequency guarantee:** The guide describes scope and says the service list is non-exhaustive and subject to change. Exam coverage, deployment availability, and the correctness of a study explanation are separate questions.
- **Service-specific documentation:** The deployment-specific documentation establishes the distinction: a DB instance standby does not serve reads, while Multi-AZ DB cluster readers can serve reads.
- **Verify live service availability:** Historical learning value does not guarantee present deployment availability. Current service notices must inform actual implementation decisions.
- **Evidence-backed content correction:** A defensible correction aligns the stem, alternatives, answer, and explanation under explicit assumptions. Traceable references and a question identifier let reviewers evaluate the change.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Primary exam reference:** The current AWS SAA-C03 exam guide.
2. **Exam scope is not a frequency guarantee:** It is within the published scope, but the list does not promise a fixed number of questions for that service.
3. **Service-specific documentation:** Current RDS documentation distinguishing Multi-AZ DB instance deployments from Multi-AZ DB cluster deployments.
4. **Verify live service availability:** Check current AWS availability and lifecycle notices, then select an eligible transfer approach for the actual customer and date.
5. **Evidence-backed content correction:** Identify the exact question, define the scenario assumptions, cite applicable AWS documentation, and update the answer plus all affected explanations together.

## Common Pitfalls

- A practice set distribution is an editorial choice, not the exam definition.
- The guide does not assign a fixed per-service question count.
- A summary without the deployment scope repeats the ambiguity rather than resolving it.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html), [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html), [AWS Snowball availability notice](https://aws.amazon.com/snowball/), [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [Snowball availability history](https://docs.aws.amazon.com/snowball/latest/developer-guide/doc-history.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

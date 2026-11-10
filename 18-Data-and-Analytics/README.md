# Data and Analytics

## Overview

This module covers **data pipelines, queries, and managed analytics**, focusing on the decisions tested on the SAA-C03. The goal is to turn business requirements into clear technical choices while balancing resilience, performance, security, and cost. Success on the exam depends on identifying the scenario's most important constraint and choosing a pattern that reduces operational risk, beyond memorizing individual services.

## Key Concepts

- Role of services: Kinesis, Glue, Athena, Redshift.
- Prioritization by dominant requirement (latency, availability, compliance or cost).
- Integration between services with decoupling and minimal observability.
- Choose the least complex architecture that meets the requirements.

## Exam Relevance

On the SAA-C03, questions in this domain often have two technically feasible options. Details such as the consistency model, failover strategy, recurring operating costs, throughput impact, and required automation determine the better answer. Studying this module means practicing those selection criteria as well as learning terminology.

## Practical Cues (3 to 5)

1. When the scenario calls for elasticity with little manual work, favor managed services.
2. When components depend on each other, check for decoupling to absorb spikes and partial failures.
3. When security is a constraint, verify encryption in transit and at rest, along with least privilege.
4. If cost is a requirement, compare usage classes, capacity modes, and access patterns.
5. If the scenario is global, validate traffic route, latency and distribution strategy.

## Common Pitfalls

- Choosing a premium feature that the scenario does not require.
- Confusing high availability features with read scaling features.
- Ignoring service limits and failure behavior.
- Addressing a security requirement with a tool unsuited to the secret lifecycle.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) to reinforce decision-making cues.
2. Answer [questions.md](./questions.md) without reference materials to test your technical judgment.
3. Use [flashcards.md](./flashcards.md) for a brief daily review to reinforce critical distinctions.

## Additional Study

To strengthen your AWS fundamentals before studying architectural scenarios in depth:
https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil

For an additional learning path connecting architecture with generative AI and Bedrock:
https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

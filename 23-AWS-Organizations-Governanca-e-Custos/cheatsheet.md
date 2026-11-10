# Quick Guide

## Decision Table

| Scenario cue | When to use | When to avoid | Exam pitfall |
|---|---|---|---|
| Low manual effort | A managed service with built-in automation | An unnecessary self-managed solution | Confusing full control with lower total cost |
| Unpredictable spikes | Horizontal scaling and decoupling | Fixed capacity and manual adjustments | Sizing for average demand and failing during spikes |
| Strong security requirement | Least privilege + encryption + auditing | Broad permission for convenience | Assuming encryption alone addresses governance |
| Cost as an explicit constraint | Select based on usage and access patterns | One storage class for all data | Reducing costs without checking functional impact |

## Service Selection Cues

- **Organizations**: prioritize when the scenario requires native integration and lower operational overhead.
- **Control Tower**: use when controlled elasticity and predictable behavior during spikes are required.

## When to Use This Module During Review

- Before architecture practice exams that focus on trade-offs.
- When you repeatedly struggle to choose between two similar options.
- During final review, to improve how you eliminate answer options.

## Recurring Pitfalls

- Trying to meet an availability requirement with a performance feature.
- Replacing a simple design with an oversized architecture.
- Omitting observability from the final architecture.

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

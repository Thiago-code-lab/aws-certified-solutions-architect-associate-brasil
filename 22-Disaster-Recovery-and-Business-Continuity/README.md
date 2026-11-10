# Disaster Recovery and Business Continuity

## Overview

Define business RPO and RTO before choosing a recovery strategy. AZ availability, regional recovery, logical corruption recovery, and backup restoration are related but different requirements.

## Key Concepts

- **RPO is not restoration speed:** RPO describes acceptable data loss in time. The recovery data path needs sufficiently current valid recovery points; fast infrastructure restoration does not make old backups newer.
- **Regional disaster scope:** Multi-AZ deployment addresses AZ-level failures within a Region. Regional recovery needs an appropriately independent recovery location and tested data, configuration, and traffic recovery.
- **Pilot light versus warm standby:** Warm standby maintains a scaled-down functioning workload. Pilot light keeps a smaller core running and requires additional activation or deployment before the full workload can serve.
- **Measure recovery:** Recovery testing checks that data, dependencies, permissions, and procedures actually work together. A successful backup is necessary evidence for that copy, but not proof of end-to-end recovery.
- **Availability and corruption recovery:** Replication can reproduce logical mistakes as well as correct writes. Availability replicas do not replace retained recoverable history for corruption or accidental deletion.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **RPO is not restoration speed:** No. The recoverable data points must satisfy the 15-minute loss window; restore speed addresses RTO.
2. **Regional disaster scope:** No. A regional recovery design needs usable recovery resources and data outside the affected Region, plus tested recovery procedures.
3. **Pilot light versus warm standby:** Warm standby.
4. **Measure recovery:** Restore representative data in an isolated environment, validate the application, measure data loss and recovery duration, and compare them with RPO and RTO.
5. **Availability and corruption recovery:** Retained backups or an appropriate point-in-time recovery capability, with tested restoration procedures.

## Common Pitfalls

- Short recovery duration does not change the age of the recovered data.
- AZs are isolated locations within a Region, not separate Regions.
- The stem explicitly says a fully functional application is already running.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

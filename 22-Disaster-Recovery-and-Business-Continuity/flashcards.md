# Review Flashcards

## Card 01

**Question:** Backups complete every 24 hours. A business requires at most 15 minutes of data loss. Can a fast restore alone prove this design meets the RPO?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** No. The recoverable data points must satisfy the 15-minute loss window; restore speed addresses RTO. RPO describes acceptable data loss in time. The recovery data path needs sufficiently current valid recovery points; fast infrastructure restoration does not make old backups newer.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 02

**Question:** A workload must recover after an entire AWS Region becomes unavailable. Does deploying the application and database across AZs only within that Region satisfy the failure scope by itself?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** No. A regional recovery design needs usable recovery resources and data outside the affected Region, plus tested recovery procedures. Multi-AZ deployment addresses AZ-level failures within a Region. Regional recovery needs an appropriately independent recovery location and tested data, configuration, and traffic recovery.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 03

**Question:** A recovery Region maintains a small but fully functional copy of the application that can serve traffic before being scaled up. Which DR pattern best describes this?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Warm standby. Warm standby maintains a scaled-down functioning workload. Pilot light keeps a smaller core running and requires additional activation or deployment before the full workload can serve.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 04

**Question:** A team has a backup marked successful. What provides stronger evidence that business recovery objectives can be met?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Restore representative data in an isolated environment, validate the application, measure data loss and recovery duration, and compare them with RPO and RTO. Recovery testing checks that data, dependencies, permissions, and procedures actually work together. A successful backup is necessary evidence for that copy, but not proof of end-to-end recovery.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

</details>

## Card 05

**Question:** An accidental application command deletes valid records from a database whose changes replicate to its standby. What protection is additionally needed?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Retained backups or an appropriate point-in-time recovery capability, with tested restoration procedures. Replication can reproduce logical mistakes as well as correct writes. Availability replicas do not replace retained recoverable history for corruption or accidental deletion.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

</details>

## Card 06

**Question:** A workload must recover after an entire AWS Region becomes unavailable. Does deploying the application and database across AZs only within that Region satisfy the failure scope by itself?

Why does this alternative fail: “Yes. Every AZ is an independent AWS Region.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** AZs are isolated locations within a Region, not separate Regions.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 07

**Question:** A recovery Region maintains a small but fully functional copy of the application that can serve traffic before being scaled up. Which DR pattern best describes this?

Why does this alternative fail: “Pilot light with only core data components active and application capacity still needing deployment.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The stem explicitly says a fully functional application is already running.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 08

**Question:** A team has a backup marked successful. What provides stronger evidence that business recovery objectives can be met?

Why does this alternative fail: “Treat the backup job status alone as a guarantee of successful restoration.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Backup completion does not validate all restoration and application dependencies.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

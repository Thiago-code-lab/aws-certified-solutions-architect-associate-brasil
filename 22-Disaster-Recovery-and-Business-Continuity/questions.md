# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 22-Q01 -->

Backups complete every 24 hours. A business requires at most 15 minutes of data loss. Can a fast restore alone prove this design meets the RPO?

A) Yes. Any restore taking less than 15 minutes guarantees a 15-minute RPO.

B) No. The recoverable data points must satisfy the 15-minute loss window; restore speed addresses RTO.

C) Yes. RPO and RTO are interchangeable names.

D) Yes. A backup schedule automatically protects every write until the next backup.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** RPO describes acceptable data loss in time. The recovery data path needs sufficiently current valid recovery points; fast infrastructure restoration does not make old backups newer.

**Why the other options are incorrect:**

- **A:** Short recovery duration does not change the age of the recovered data.
- **C:** RPO and RTO measure different requirements.
- **D:** Periodic backups do not automatically include subsequent unbacked-up writes.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Question 2

<!-- question-id: 22-Q02 -->

A workload must recover after an entire AWS Region becomes unavailable. Does deploying the application and database across AZs only within that Region satisfy the failure scope by itself?

A) Yes. Every AZ is an independent AWS Region.

B) Yes. An additional private subnet in the same VPC provides regional recovery.

C) Yes. A larger instance removes the regional dependency.

D) No. A regional recovery design needs usable recovery resources and data outside the affected Region, plus tested recovery procedures.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Multi-AZ deployment addresses AZ-level failures within a Region. Regional recovery needs an appropriately independent recovery location and tested data, configuration, and traffic recovery.

**Why the other options are incorrect:**

- **A:** AZs are isolated locations within a Region, not separate Regions.
- **B:** Another same-Region subnet does not remove the Region dependency.
- **C:** Instance size does not change geographic failure scope.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Question 3

<!-- question-id: 22-Q03 -->

A recovery Region maintains a small but fully functional copy of the application that can serve traffic before being scaled up. Which DR pattern best describes this?

A) Pilot light with only core data components active and application capacity still needing deployment.

B) Warm standby.

C) Backup and restore with no running application.

D) Multi-site active/active serving production traffic from both Regions.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Warm standby maintains a scaled-down functioning workload. Pilot light keeps a smaller core running and requires additional activation or deployment before the full workload can serve.

**Why the other options are incorrect:**

- **A:** The stem explicitly says a fully functional application is already running.
- **C:** The stem includes a running application, not only stored backups.
- **D:** The recovery copy is standby, not already sharing normal production traffic.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Question 4

<!-- question-id: 22-Q04 -->

A team has a backup marked successful. What provides stronger evidence that business recovery objectives can be met?

A) Treat the backup job status alone as a guarantee of successful restoration.

B) Assume a DNS record proves database recoverability.

C) Restore representative data in an isolated environment, validate the application, measure data loss and recovery duration, and compare them with RPO and RTO.

D) Delete the source database before planning a restore test.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Recovery testing checks that data, dependencies, permissions, and procedures actually work together. A successful backup is necessary evidence for that copy, but not proof of end-to-end recovery.

**Why the other options are incorrect:**

- **A:** Backup completion does not validate all restoration and application dependencies.
- **B:** DNS configuration does not verify restored data.
- **D:** Destructive production actions are unnecessary for an isolated recovery test.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

</details>

## Question 5

<!-- question-id: 22-Q05 -->

An accidental application command deletes valid records from a database whose changes replicate to its standby. What protection is additionally needed?

A) Assume synchronous standby replication always preserves the pre-delete data as an independent backup.

B) Use an ALB listener rule to reconstruct deleted rows.

C) Retained backups or an appropriate point-in-time recovery capability, with tested restoration procedures.

D) Increase the database CPU without a recovery copy.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Replication can reproduce logical mistakes as well as correct writes. Availability replicas do not replace retained recoverable history for corruption or accidental deletion.

**Why the other options are incorrect:**

- **A:** A standby can receive the same deletion and is not an independent historical backup.
- **B:** A load balancer does not reconstruct database history.
- **D:** Additional CPU does not restore lost data.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

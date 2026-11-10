# Use Cases

## Scenario 1: RPO is not restoration speed

**Requirement:** Backups complete every 24 hours. A business requires at most 15 minutes of data loss. Can a fast restore alone prove this design meets the RPO?

**Recommended design:** No. The recoverable data points must satisfy the 15-minute loss window; restore speed addresses RTO.

**Reason and boundary:** RPO describes acceptable data loss in time. The recovery data path needs sufficiently current valid recovery points; fast infrastructure restoration does not make old backups newer.

**Rejected alternative:** Yes. Any restore taking less than 15 minutes guarantees a 15-minute RPO. Short recovery duration does not change the age of the recovered data.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

## Scenario 2: Regional disaster scope

**Requirement:** A workload must recover after an entire AWS Region becomes unavailable. Does deploying the application and database across AZs only within that Region satisfy the failure scope by itself?

**Recommended design:** No. A regional recovery design needs usable recovery resources and data outside the affected Region, plus tested recovery procedures.

**Reason and boundary:** Multi-AZ deployment addresses AZ-level failures within a Region. Regional recovery needs an appropriately independent recovery location and tested data, configuration, and traffic recovery.

**Rejected alternative:** Yes. Every AZ is an independent AWS Region. AZs are isolated locations within a Region, not separate Regions.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

## Scenario 3: Pilot light versus warm standby

**Requirement:** A recovery Region maintains a small but fully functional copy of the application that can serve traffic before being scaled up. Which DR pattern best describes this?

**Recommended design:** Warm standby.

**Reason and boundary:** Warm standby maintains a scaled-down functioning workload. Pilot light keeps a smaller core running and requires additional activation or deployment before the full workload can serve.

**Rejected alternative:** Pilot light with only core data components active and application capacity still needing deployment. The stem explicitly says a fully functional application is already running.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

## Scenario 4: Measure recovery

**Requirement:** A team has a backup marked successful. What provides stronger evidence that business recovery objectives can be met?

**Recommended design:** Restore representative data in an isolated environment, validate the application, measure data loss and recovery duration, and compare them with RPO and RTO.

**Reason and boundary:** Recovery testing checks that data, dependencies, permissions, and procedures actually work together. A successful backup is necessary evidence for that copy, but not proof of end-to-end recovery.

**Rejected alternative:** Treat the backup job status alone as a guarantee of successful restoration. Backup completion does not validate all restoration and application dependencies.

**AWS references:** [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

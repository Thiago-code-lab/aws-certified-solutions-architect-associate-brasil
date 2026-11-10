# Guided Lab

## Objective

Inspect and test the failover behavior of an RDS Multi-AZ DB instance deployment.

## Services Used

RDS MySQL or PostgreSQL, a private lab client, and monitoring.

## Expected Cost Range

A Multi-AZ database, standby capacity, storage, backups, and client compute can be billable. Estimate before creation and use a short window; this is not a guaranteed Free Tier exercise.

## Step-by-Step Instructions

1. Choose a supported engine/version for a Multi-AZ DB instance deployment with one standby, and explicitly avoid confusing it with a Multi-AZ DB cluster.
2. Create a private lab database using a DB subnet group across the required AZs and permit the database port only from the lab-client security group.
3. Connect from an approved lab client using securely stored lab credentials; create a small marker table and commit a test row.
4. Record the writer endpoint, primary AZ, deployment type, and the database events and metrics to watch.
5. Use the documented reboot-with-failover operation for this supported lab deployment. Observe the connection interruption and primary AZ change.
6. Reconnect through the database endpoint after failover, confirm the committed marker row, and record recovery duration.

## Validation

- A client can reconnect and read the committed marker after the managed failover.
- The measured interruption is recorded rather than presented as a universal RTO guarantee.
- The single standby is not treated as a readable reporting endpoint.

## Cleanup

1. Delete the lab database after deciding whether any lab final snapshot is needed.
2. Delete lab-only snapshots and retained automated backups that have no retention requirement.
3. Remove lab clients, secrets, subnet groups, and security groups only when no other resource uses them.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

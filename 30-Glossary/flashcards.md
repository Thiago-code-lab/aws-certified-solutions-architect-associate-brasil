# Review Flashcards

## Card 01

**Question:** Which term expresses the maximum acceptable amount of data loss measured in time after a disruption?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Recovery point objective, or RPO. RPO expresses the acceptable data-loss window. It guides replication and backup requirements rather than the time needed to return the application to service.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

</details>

## Card 02

**Question:** Which term expresses the maximum acceptable time to restore service after a disruption?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Recovery time objective, or RTO. RTO expresses the recovery-time target for the workload. Recovery testing should measure the end-to-end duration, including dependencies and application validation.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 03

**Question:** A storage system retains data safely but is temporarily unable to serve requests. Which distinction explains why this can occur?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Durability concerns retaining data; availability concerns being able to access the service when needed. Data can remain intact during a temporary access outage. Architecture must evaluate both preservation and access requirements rather than treating one as proof of the other.

**AWS references:** [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 04

**Question:** An application increases capacity by adding more instances behind a load balancer rather than enlarging one instance. What is this called?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Horizontal scaling, or scaling out. Horizontal scaling adds more workers or instances. Vertical scaling changes the capacity of an individual resource; neither term alone proves application resilience.

**AWS references:** [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html), [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html).

</details>

## Card 05

**Question:** A consumer may receive the same order event more than once. It records an order operation so retries do not charge the customer again. Which property is it implementing?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Idempotent processing of the business operation. Idempotency makes a repeated operation safe with respect to its intended side effect. It does not require the transport to stop delivering duplicate events.

**AWS references:** [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html).

</details>

## Card 06

**Question:** Which term expresses the maximum acceptable time to restore service after a disruption?

Why does this alternative fail: “Recovery point objective, or RPO.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** RPO concerns tolerable data loss rather than recovery duration.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 07

**Question:** A storage system retains data safely but is temporarily unable to serve requests. Which distinction explains why this can occur?

Why does this alternative fail: “Durability and availability always mean exactly the same property.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The two properties describe different aspects of service behavior.

**AWS references:** [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 08

**Question:** An application increases capacity by adding more instances behind a load balancer rather than enlarging one instance. What is this called?

Why does this alternative fail: “Vertical scaling, or scaling up.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Scaling up enlarges an individual resource rather than adding instances.

**AWS references:** [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html), [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

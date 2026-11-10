# Use Cases

## Scenario 1: RPO terminology

**Requirement:** Which term expresses the maximum acceptable amount of data loss measured in time after a disruption?

**Recommended design:** Recovery point objective, or RPO.

**Reason and boundary:** RPO expresses the acceptable data-loss window. It guides replication and backup requirements rather than the time needed to return the application to service.

**Rejected alternative:** Recovery time objective, or RTO. RTO expresses the acceptable recovery duration.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

## Scenario 2: RTO terminology

**Requirement:** Which term expresses the maximum acceptable time to restore service after a disruption?

**Recommended design:** Recovery time objective, or RTO.

**Reason and boundary:** RTO expresses the recovery-time target for the workload. Recovery testing should measure the end-to-end duration, including dependencies and application validation.

**Rejected alternative:** Recovery point objective, or RPO. RPO concerns tolerable data loss rather than recovery duration.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

## Scenario 3: Durability versus availability

**Requirement:** A storage system retains data safely but is temporarily unable to serve requests. Which distinction explains why this can occur?

**Recommended design:** Durability concerns retaining data; availability concerns being able to access the service when needed.

**Reason and boundary:** Data can remain intact during a temporary access outage. Architecture must evaluate both preservation and access requirements rather than treating one as proof of the other.

**Rejected alternative:** Durability and availability always mean exactly the same property. The two properties describe different aspects of service behavior.

**AWS references:** [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

## Scenario 4: Horizontal versus vertical scaling

**Requirement:** An application increases capacity by adding more instances behind a load balancer rather than enlarging one instance. What is this called?

**Recommended design:** Horizontal scaling, or scaling out.

**Reason and boundary:** Horizontal scaling adds more workers or instances. Vertical scaling changes the capacity of an individual resource; neither term alone proves application resilience.

**Rejected alternative:** Vertical scaling, or scaling up. Scaling up enlarges an individual resource rather than adding instances.

**AWS references:** [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html), [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 30-Q01 -->

Which term expresses the maximum acceptable amount of data loss measured in time after a disruption?

A) Recovery time objective, or RTO.

B) The DNS time to live.

C) The instance CPU utilization target.

D) Recovery point objective, or RPO.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** RPO expresses the acceptable data-loss window. It guides replication and backup requirements rather than the time needed to return the application to service.

**Why the other options are incorrect:**

- **A:** RTO expresses the acceptable recovery duration.
- **B:** DNS TTL controls caching behavior rather than the business data-loss tolerance.
- **C:** A compute scaling target is unrelated to acceptable recovered data age.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

</details>

## Question 2

<!-- question-id: 30-Q02 -->

Which term expresses the maximum acceptable time to restore service after a disruption?

A) Recovery point objective, or RPO.

B) An S3 object retention date.

C) A KMS key identifier.

D) Recovery time objective, or RTO.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** RTO expresses the recovery-time target for the workload. Recovery testing should measure the end-to-end duration, including dependencies and application validation.

**Why the other options are incorrect:**

- **A:** RPO concerns tolerable data loss rather than recovery duration.
- **B:** A retention date protects an object version until a time; it is not an application recovery objective.
- **C:** A resource identifier is not a recovery duration.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Question 3

<!-- question-id: 30-Q03 -->

A storage system retains data safely but is temporarily unable to serve requests. Which distinction explains why this can occur?

A) Durability and availability always mean exactly the same property.

B) Higher CPU utilization guarantees both properties for every storage service.

C) DNS caching is the definition of storage durability.

D) Durability concerns retaining data; availability concerns being able to access the service when needed.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Data can remain intact during a temporary access outage. Architecture must evaluate both preservation and access requirements rather than treating one as proof of the other.

**Why the other options are incorrect:**

- **A:** The two properties describe different aspects of service behavior.
- **B:** CPU utilization is not a universal guarantee of data retention or service accessibility.
- **C:** DNS caching does not define storage data retention.

**AWS references:** [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Question 4

<!-- question-id: 30-Q04 -->

An application increases capacity by adding more instances behind a load balancer rather than enlarging one instance. What is this called?

A) Vertical scaling, or scaling up.

B) Horizontal scaling, or scaling out.

C) Encryption at rest.

D) A backup retention extension.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Horizontal scaling adds more workers or instances. Vertical scaling changes the capacity of an individual resource; neither term alone proves application resilience.

**Why the other options are incorrect:**

- **A:** Scaling up enlarges an individual resource rather than adding instances.
- **C:** Encryption protects data and is not a capacity-scaling term.
- **D:** Retention changes recoverable history, not instance count.

**AWS references:** [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html), [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html).

</details>

## Question 5

<!-- question-id: 30-Q05 -->

A consumer may receive the same order event more than once. It records an order operation so retries do not charge the customer again. Which property is it implementing?

A) Strict global ordering for every message regardless of queue type.

B) A guarantee that network delivery can never repeat.

C) Public access to the order database.

D) Idempotent processing of the business operation.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Idempotency makes a repeated operation safe with respect to its intended side effect. It does not require the transport to stop delivering duplicate events.

**Why the other options are incorrect:**

- **A:** Ordering and idempotency are different properties.
- **B:** Safe repeated processing does not prove duplicate-free delivery.
- **C:** Public exposure is unrelated to safe handling of retries.

**AWS references:** [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

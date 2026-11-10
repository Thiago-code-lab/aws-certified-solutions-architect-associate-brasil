# Use Cases

## Scenario 1: RDS failover question clarified

**Requirement:** A relational database needs managed AZ failover. The chosen deployment is an RDS Multi-AZ DB instance deployment; extra read capacity is not required. Which feature is the direct fit?

**Recommended design:** The synchronous standby and managed failover of that Multi-AZ DB instance deployment.

**Reason and boundary:** This specifies the deployment type and availability objective. A Multi-AZ DB instance standby supports managed failover; an asynchronous read replica primarily provides another read or recovery copy with different semantics.

**Rejected alternative:** Only an ordinary asynchronous read replica, assumed to be the same feature. An ordinary read replica does not provide the identical synchronous standby failover feature.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html).

## Scenario 2: Resilient application question clarified

**Requirement:** A stateless web application must remain available when one AZ fails. Which design directly addresses that failure scope?

**Recommended design:** An ALB with application instances across multiple AZs, working health checks, externalized state, and sufficient surviving capacity.

**Reason and boundary:** Multiple AZs and appropriately placed state reduce the single-AZ dependency. Recovery copies and static addressing do not by themselves keep a sole failed instance serving requests.

**Rejected alternative:** One larger EC2 instance with a daily AMI. An AMI supports recovery but does not keep that one instance available during AZ failure.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

## Scenario 3: Private S3 question clarified

**Requirement:** A VPC workload needs same-Region S3 access without NAT or public internet routing. Which choice supplies a route-table-based private path?

**Recommended design:** An S3 gateway endpoint with the required routes and appropriate endpoint, bucket, and IAM policies.

**Reason and boundary:** A gateway endpoint supports S3 access through VPC route tables without NAT or an internet gateway for that traffic. Authorization remains a separate requirement.

**Rejected alternative:** A NAT gateway used for all S3 traffic. NAT violates the explicit network-path constraint.

**AWS references:** [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html).

## Scenario 4: Queue decoupling question clarified

**Requirement:** An API accepts jobs durably and workers can process them asynchronously. It needs to absorb traffic bursts without requiring every worker to be available at acceptance time. Which service fits?

**Recommended design:** Amazon SQS with suitable producer error handling and retry-safe consumers.

**Reason and boundary:** SQS decouples job acceptance from consumer processing. Applications still handle send failures, retention, retries, duplicate processing, and backlog growth.

**Rejected alternative:** Amazon EFS used as if it were a managed queue. Shared file storage does not provide the managed queue semantics requested.

**AWS references:** [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html), [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 05-Q01 -->

A stateless HTTP application must tolerate an AZ outage. Which design addresses that failure scope?

A) A larger single EC2 instance with daily snapshots.

B) An ALB and an Auto Scaling group spanning at least two AZs, with enough surviving capacity and externalized application state.

C) Two EC2 instances placed in only one AZ.

D) A second DNS name for the same single instance.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Distributing compute and load balancing across AZs reduces dependence on one AZ. Surviving capacity, health checks, and state placement must also support the application during failure.

**Why the other options are incorrect:**

- **A:** Snapshots help recovery but do not keep a single instance serving through an AZ outage.
- **C:** Both instances can fail with their shared AZ.
- **D:** Additional names do not remove the single compute failure domain.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [EC2 Auto Scaling health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Question 2

<!-- question-id: 05-Q02 -->

One HTTPS entry point must route /images to one target group and /orders to another. Which load balancer provides this request-path routing?

A) Application Load Balancer.

B) Network Load Balancer using only transport-layer listeners.

C) A NAT gateway.

D) A security group.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** ALB evaluates application-layer listener rules, including path conditions. The other choices do not provide HTTP path-based target-group routing.

**Why the other options are incorrect:**

- **B:** NLB transport listeners do not evaluate HTTP URL paths for routing.
- **C:** A NAT gateway translates outbound connections rather than routing application paths.
- **D:** Security groups filter traffic and do not dispatch HTTP requests to target groups.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html).

</details>

## Question 3

<!-- question-id: 05-Q03 -->

An Auto Scaling instance passes EC2 status checks, but its application fails ALB health checks. Which configuration lets the group use those application health results to replace it?

A) Assume attaching a target group automatically enables every group health check.

B) Disable all health checks.

C) Increase the instance EBS volume size without addressing the application.

D) Enable Elastic Load Balancing health checks for the group and configure an appropriate grace period.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** The group must be configured to use ELB health checks in addition to its default EC2 checks. A suitable grace period avoids replacing instances merely because startup is still in progress.

**Why the other options are incorrect:**

- **A:** Default EC2 health checks alone do not detect every application failure.
- **B:** Disabling checks prevents reliable unhealthy-instance detection.
- **C:** Storage capacity is not the missing application-health integration.

**AWS references:** [EC2 Auto Scaling health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html).

</details>

## Question 4

<!-- question-id: 05-Q04 -->

HTTP traffic varies unpredictably. The team wants the instance count to follow a utilization metric around a chosen target. Which policy fits?

A) Scheduled scaling alone at a fixed daily time.

B) Manual instance launches during every spike.

C) A fixed desired capacity with no scaling policies.

D) Target tracking scaling with a suitable metric and instance warmup configuration.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Target tracking changes capacity to keep a supported metric near its target. Scheduled changes can complement it for known events, but cannot alone react to unpredictable demand.

**Why the other options are incorrect:**

- **A:** A clock-based schedule does not respond to unanticipated metric changes.
- **B:** Manual launches do not provide the requested automatic response.
- **C:** A fixed capacity does not follow the changing utilization target.

**AWS references:** [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html).

</details>

## Question 5

<!-- question-id: 05-Q05 -->

Users lose shopping carts when an application instance is replaced. Carts exist only in that instance memory. Which change addresses the data-placement problem?

A) Treat ALB session stickiness as a durable backup of instance memory.

B) Store cart state in an appropriate shared data store and make web instances replaceable.

C) Increase the DNS record TTL.

D) Move all application instances into one AZ.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** External state storage lets a replacement instance retrieve the cart, subject to the store consistency and durability design. Routing a user to one instance does not persist that instance memory.

**Why the other options are incorrect:**

- **A:** Stickiness is a routing feature and does not preserve memory after instance loss.
- **C:** DNS caching does not store application cart data.
- **D:** Concentrating compute in one AZ increases correlated failure exposure.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

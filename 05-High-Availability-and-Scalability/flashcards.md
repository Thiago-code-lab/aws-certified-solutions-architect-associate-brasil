# Review Flashcards

## Card 01

**Question:** A stateless HTTP application must tolerate an AZ outage. Which design addresses that failure scope?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** An ALB and an Auto Scaling group spanning at least two AZs, with enough surviving capacity and externalized application state. Distributing compute and load balancing across AZs reduces dependence on one AZ. Surviving capacity, health checks, and state placement must also support the application during failure.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [EC2 Auto Scaling health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Card 02

**Question:** One HTTPS entry point must route /images to one target group and /orders to another. Which load balancer provides this request-path routing?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Application Load Balancer. ALB evaluates application-layer listener rules, including path conditions. The other choices do not provide HTTP path-based target-group routing.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html).

</details>

## Card 03

**Question:** An Auto Scaling instance passes EC2 status checks, but its application fails ALB health checks. Which configuration lets the group use those application health results to replace it?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Enable Elastic Load Balancing health checks for the group and configure an appropriate grace period. The group must be configured to use ELB health checks in addition to its default EC2 checks. A suitable grace period avoids replacing instances merely because startup is still in progress.

**AWS references:** [EC2 Auto Scaling health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html).

</details>

## Card 04

**Question:** HTTP traffic varies unpredictably. The team wants the instance count to follow a utilization metric around a chosen target. Which policy fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Target tracking scaling with a suitable metric and instance warmup configuration. Target tracking changes capacity to keep a supported metric near its target. Scheduled changes can complement it for known events, but cannot alone react to unpredictable demand.

**AWS references:** [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html).

</details>

## Card 05

**Question:** Users lose shopping carts when an application instance is replaced. Carts exist only in that instance memory. Which change addresses the data-placement problem?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Store cart state in an appropriate shared data store and make web instances replaceable. External state storage lets a replacement instance retrieve the cart, subject to the store consistency and durability design. Routing a user to one instance does not persist that instance memory.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

</details>

## Card 06

**Question:** One HTTPS entry point must route /images to one target group and /orders to another. Which load balancer provides this request-path routing?

Why does this alternative fail: “Network Load Balancer using only transport-layer listeners.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** NLB transport listeners do not evaluate HTTP URL paths for routing.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html).

</details>

## Card 07

**Question:** An Auto Scaling instance passes EC2 status checks, but its application fails ALB health checks. Which configuration lets the group use those application health results to replace it?

Why does this alternative fail: “Assume attaching a target group automatically enables every group health check.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Default EC2 health checks alone do not detect every application failure.

**AWS references:** [EC2 Auto Scaling health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html).

</details>

## Card 08

**Question:** HTTP traffic varies unpredictably. The team wants the instance count to follow a utilization metric around a chosen target. Which policy fits?

Why does this alternative fail: “Scheduled scaling alone at a fixed daily time.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** A clock-based schedule does not respond to unanticipated metric changes.

**AWS references:** [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

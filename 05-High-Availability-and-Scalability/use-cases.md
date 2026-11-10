# Use Cases

## Scenario 1: Multi-AZ application availability

**Requirement:** A stateless HTTP application must tolerate an AZ outage. Which design addresses that failure scope?

**Recommended design:** An ALB and an Auto Scaling group spanning at least two AZs, with enough surviving capacity and externalized application state.

**Reason and boundary:** Distributing compute and load balancing across AZs reduces dependence on one AZ. Surviving capacity, health checks, and state placement must also support the application during failure.

**Rejected alternative:** A larger single EC2 instance with daily snapshots. Snapshots help recovery but do not keep a single instance serving through an AZ outage.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [EC2 Auto Scaling health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

## Scenario 2: Layer 7 routing

**Requirement:** One HTTPS entry point must route /images to one target group and /orders to another. Which load balancer provides this request-path routing?

**Recommended design:** Application Load Balancer.

**Reason and boundary:** ALB evaluates application-layer listener rules, including path conditions. The other choices do not provide HTTP path-based target-group routing.

**Rejected alternative:** Network Load Balancer using only transport-layer listeners. NLB transport listeners do not evaluate HTTP URL paths for routing.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html).

## Scenario 3: Application health replacement

**Requirement:** An Auto Scaling instance passes EC2 status checks, but its application fails ALB health checks. Which configuration lets the group use those application health results to replace it?

**Recommended design:** Enable Elastic Load Balancing health checks for the group and configure an appropriate grace period.

**Reason and boundary:** The group must be configured to use ELB health checks in addition to its default EC2 checks. A suitable grace period avoids replacing instances merely because startup is still in progress.

**Rejected alternative:** Assume attaching a target group automatically enables every group health check. Default EC2 health checks alone do not detect every application failure.

**AWS references:** [EC2 Auto Scaling health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html).

## Scenario 4: Dynamic scaling

**Requirement:** HTTP traffic varies unpredictably. The team wants the instance count to follow a utilization metric around a chosen target. Which policy fits?

**Recommended design:** Target tracking scaling with a suitable metric and instance warmup configuration.

**Reason and boundary:** Target tracking changes capacity to keep a supported metric near its target. Scheduled changes can complement it for known events, but cannot alone react to unpredictable demand.

**Rejected alternative:** Scheduled scaling alone at a fixed daily time. A clock-based schedule does not respond to unanticipated metric changes.

**AWS references:** [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

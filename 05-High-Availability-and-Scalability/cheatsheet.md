# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Multi-AZ application availability | An ALB and an Auto Scaling group spanning at least two AZs, with enough surviving capacity and externalized application state. | Distributing compute and load balancing across AZs reduces dependence on one AZ. Surviving capacity, health checks, and state placement must also support the application during failure. |
| Layer 7 routing | Application Load Balancer. | ALB evaluates application-layer listener rules, including path conditions. The other choices do not provide HTTP path-based target-group routing. |
| Application health replacement | Enable Elastic Load Balancing health checks for the group and configure an appropriate grace period. | The group must be configured to use ELB health checks in addition to its default EC2 checks. A suitable grace period avoids replacing instances merely because startup is still in progress. |
| Dynamic scaling | Target tracking scaling with a suitable metric and instance warmup configuration. | Target tracking changes capacity to keep a supported metric near its target. Scheduled changes can complement it for known events, but cannot alone react to unpredictable demand. |
| Session state during replacement | Store cart state in an appropriate shared data store and make web instances replaceable. | External state storage lets a replacement instance retrieve the cart, subject to the store consistency and durability design. Routing a user to one instance does not persist that instance memory. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Multi-AZ application availability:** Snapshots help recovery but do not keep a single instance serving through an AZ outage.
- **Layer 7 routing:** NLB transport listeners do not evaluate HTTP URL paths for routing.
- **Application health replacement:** Default EC2 health checks alone do not detect every application failure.
- **Dynamic scaling:** A clock-based schedule does not respond to unanticipated metric changes.
- **Session state during replacement:** Stickiness is a routing feature and does not preserve memory after instance loss.

## AWS References

[Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [EC2 Auto Scaling health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html), [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html), [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

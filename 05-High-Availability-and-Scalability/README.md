# High Availability and Scalability

## Overview

Design application availability and elasticity together. Multiple instances only protect against a failure when their placement, health checks, capacity, application state, and dependencies match the failure scope.

## Key Concepts

- **Multi-AZ application availability:** Distributing compute and load balancing across AZs reduces dependence on one AZ. Surviving capacity, health checks, and state placement must also support the application during failure.
- **Layer 7 routing:** ALB evaluates application-layer listener rules, including path conditions. The other choices do not provide HTTP path-based target-group routing.
- **Application health replacement:** The group must be configured to use ELB health checks in addition to its default EC2 checks. A suitable grace period avoids replacing instances merely because startup is still in progress.
- **Dynamic scaling:** Target tracking changes capacity to keep a supported metric near its target. Scheduled changes can complement it for known events, but cannot alone react to unpredictable demand.
- **Session state during replacement:** External state storage lets a replacement instance retrieve the cart, subject to the store consistency and durability design. Routing a user to one instance does not persist that instance memory.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Multi-AZ application availability:** An ALB and an Auto Scaling group spanning at least two AZs, with enough surviving capacity and externalized application state.
2. **Layer 7 routing:** Application Load Balancer.
3. **Application health replacement:** Enable Elastic Load Balancing health checks for the group and configure an appropriate grace period.
4. **Dynamic scaling:** Target tracking scaling with a suitable metric and instance warmup configuration.
5. **Session state during replacement:** Store cart state in an appropriate shared data store and make web instances replaceable.

## Common Pitfalls

- Snapshots help recovery but do not keep a single instance serving through an AZ outage.
- NLB transport listeners do not evaluate HTTP URL paths for routing.
- Default EC2 health checks alone do not detect every application failure.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [EC2 Auto Scaling health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html), [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html), [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

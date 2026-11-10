# Quick Guide

## Decision Table

| Scenario cue | Best choice | Avoid | Common pitfall |
|---|---|---|---|
| “Minimum necessary access” | Granular IAM policy + role | User with broad permissions | Confusing agility with full permission |
| “Unpredictable spikes” | ASG + ALB + decoupling | A single vertically scaled instance | Sizing for average demand and collapsing during spikes |
| “No public internet” | VPC Endpoint/PrivateLink | NAT for AWS internal traffic | Pay more and expand risk surface |
| “Low RPO / short RTO” | Multi-AZ or warm standby, depending on the target | Occasional, untested backups | Choosing a DR strategy too inexpensive to meet an aggressive target |
| “Cost with predictable use” | Savings Plans/RI + rightsizing | On-Demand without analysis | Ignore commitment at steady load |

## Quick elimination checklist

1. Does the option violate explicit security requirements?
2. Does the option add components unnecessarily?
3. Does the option add manual work without a technical benefit?
4. Is there a managed service that solves the problem with less risk?

## Commonly Confused Service Groups on the SAA-C03

- **SG vs. NACL**: a security group is stateful at the ENI; a network ACL is stateless at the subnet.
- **Multi-AZ vs. Read Replica**: Multi-AZ = availability; read replica = read scaling.
- **SQS vs SNS vs EventBridge**: durable queue, pub/sub fan-out, event routing.

## Using This Material During Final Review

- Review before each mini practice exam.
- Identify the decision-table row where you made the wrong choice.
- Update the error log with the correct decision rule.

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

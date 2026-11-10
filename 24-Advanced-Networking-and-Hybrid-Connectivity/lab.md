# Guided Lab

## Objective

Review hybrid-network routing, encryption, and redundancy boundaries.

## Services Used

Transit Gateway, VPC peering, PrivateLink, Direct Connect, and Site-to-Site VPN documentation.

## Expected Cost Range

Design exercise. Real gateways, VPNs, endpoints, circuits, and data transfers can incur charges; do not provision them simply to draw the topology.

## Step-by-Step Instructions

1. Draw three non-overlapping sample VPC networks and an on-premises network.
2. Draw A-to-B and B-to-C peering and show why it does not create an A-to-C transit route.
3. Replace the intended hub connectivity with appropriate Transit Gateway attachments and separate route-table domains on the diagram.
4. Draw a separate PrivateLink consumer-to-service path and label why it is not general network transit.
5. Annotate each Direct Connect or VPN link with its encryption mechanism and exact coverage; do not label a private circuit encrypted by default.
6. Remove one drawn path or tunnel at a time and explain the remaining routes and any single points of failure.

## Validation

- Return routing, traffic filters, and service authorization are considered separately.
- Peering is not assumed transitive.
- Encryption coverage and redundancy are explicit rather than implied by a service name.

## Cleanup

1. Keep the topology and failure observations.
2. No live circuit or gateway is required; remove any separately approved disposable network resources under their own dependency-aware plan.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [VPC peering limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html), [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html), [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html), [Direct Connect encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html), [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

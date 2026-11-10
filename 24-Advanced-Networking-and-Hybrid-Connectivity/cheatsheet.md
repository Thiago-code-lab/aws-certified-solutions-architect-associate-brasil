# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Direct Connect encryption | Direct Connect is not encrypted by default; choose suitable TLS, IPsec VPN, or supported MACsec protection for the required path. | Private connectivity and encryption are separate properties. MACsec protects supported connection segments, so its coverage must be matched to the actual requirement rather than assumed end-to-end. |
| Nontransitive peering | No. VPC peering does not support transitive routing. | A-to-B and B-to-C peerings do not create an A-to-C transit route. Use a supported connectivity design, such as suitable direct peerings or Transit Gateway attachments and routing. |
| Hub network connectivity | AWS Transit Gateway with appropriate attachments and route tables. | Transit Gateway supplies a regional transit hub for supported attachments. Its route table associations, propagation, segmentation, and failure design still need explicit configuration. |
| Private service exposure | AWS PrivateLink with a suitable endpoint service and consumer interface endpoints. | PrivateLink supports private connectivity to supported services through endpoints. It is service-oriented connectivity, not general-purpose transitive routing between all attached networks. |
| VPN and redundancy | AWS Site-to-Site VPN, with both provided tunnels and appropriate customer-side routing and redundancy. | Site-to-Site VPN provides IPsec connectivity. Using both tunnels and designing customer-device and path redundancy improves resilience; no single connection choice guarantees uninterrupted availability. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Direct Connect encryption:** A private circuit does not inherently provide encryption.
- **Nontransitive peering:** Peering does not provide transitive routing.
- **Hub network connectivity:** Security groups filter traffic and do not provide transit routing.
- **Private service exposure:** A public-only path violates the private connectivity requirement.
- **VPN and redundancy:** Direct Connect is a different connectivity model and lacks default transport encryption.

## AWS References

[Direct Connect encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html), [VPC peering limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html), [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html), [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html), [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html), [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Advanced Networking and Hybrid Connectivity

## Overview

Design hybrid and multi-VPC connectivity from routing, service boundaries, encryption, and failure paths. Private connectivity does not automatically imply encryption, and VPC peering is not transitive.

## Key Concepts

- **Direct Connect encryption:** Private connectivity and encryption are separate properties. MACsec protects supported connection segments, so its coverage must be matched to the actual requirement rather than assumed end-to-end.
- **Nontransitive peering:** A-to-B and B-to-C peerings do not create an A-to-C transit route. Use a supported connectivity design, such as suitable direct peerings or Transit Gateway attachments and routing.
- **Hub network connectivity:** Transit Gateway supplies a regional transit hub for supported attachments. Its route table associations, propagation, segmentation, and failure design still need explicit configuration.
- **Private service exposure:** PrivateLink supports private connectivity to supported services through endpoints. It is service-oriented connectivity, not general-purpose transitive routing between all attached networks.
- **VPN and redundancy:** Site-to-Site VPN provides IPsec connectivity. Using both tunnels and designing customer-device and path redundancy improves resilience; no single connection choice guarantees uninterrupted availability.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Direct Connect encryption:** Direct Connect is not encrypted by default; choose suitable TLS, IPsec VPN, or supported MACsec protection for the required path.
2. **Nontransitive peering:** No. VPC peering does not support transitive routing.
3. **Hub network connectivity:** AWS Transit Gateway with appropriate attachments and route tables.
4. **Private service exposure:** AWS PrivateLink with a suitable endpoint service and consumer interface endpoints.
5. **VPN and redundancy:** AWS Site-to-Site VPN, with both provided tunnels and appropriate customer-side routing and redundancy.

## Common Pitfalls

- A private circuit does not inherently provide encryption.
- Peering does not provide transitive routing.
- Security groups filter traffic and do not provide transit routing.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[Direct Connect encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html), [VPC peering limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html), [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html), [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html), [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html), [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

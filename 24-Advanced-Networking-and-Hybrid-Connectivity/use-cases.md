# Use Cases

## Scenario 1: Direct Connect encryption

**Requirement:** A design uses Direct Connect and must encrypt data in transit. Which statement is accurate?

**Recommended design:** Direct Connect is not encrypted by default; choose suitable TLS, IPsec VPN, or supported MACsec protection for the required path.

**Reason and boundary:** Private connectivity and encryption are separate properties. MACsec protects supported connection segments, so its coverage must be matched to the actual requirement rather than assumed end-to-end.

**Rejected alternative:** A dedicated circuit automatically means every application byte is encrypted end to end. A private circuit does not inherently provide encryption.

**AWS references:** [Direct Connect encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html).

## Scenario 2: Nontransitive peering

**Requirement:** VPC A is peered with VPC B, and B is peered with C. There is no A-to-C peering or transit service. Can A use B to reach C through those peerings?

**Recommended design:** No. VPC peering does not support transitive routing.

**Reason and boundary:** A-to-B and B-to-C peerings do not create an A-to-C transit route. Use a supported connectivity design, such as suitable direct peerings or Transit Gateway attachments and routing.

**Rejected alternative:** Yes. All peering connections are automatically transitive. Peering does not provide transitive routing.

**AWS references:** [VPC peering limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html), [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).

## Scenario 3: Hub network connectivity

**Requirement:** Many VPCs and on-premises networks need a managed hub-and-spoke connectivity design with centralized routing domains. Which service fits?

**Recommended design:** AWS Transit Gateway with appropriate attachments and route tables.

**Reason and boundary:** Transit Gateway supplies a regional transit hub for supported attachments. Its route table associations, propagation, segmentation, and failure design still need explicit configuration.

**Rejected alternative:** A single security group shared as if it were a router. Security groups filter traffic and do not provide transit routing.

**AWS references:** [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).

## Scenario 4: Private service exposure

**Requirement:** A provider wants to expose a supported application service privately to consumer VPCs without providing general network transit between the VPCs. Which pattern fits?

**Recommended design:** AWS PrivateLink with a suitable endpoint service and consumer interface endpoints.

**Reason and boundary:** PrivateLink supports private connectivity to supported services through endpoints. It is service-oriented connectivity, not general-purpose transitive routing between all attached networks.

**Rejected alternative:** An unrestricted internet endpoint as the only service path. A public-only path violates the private connectivity requirement.

**AWS references:** [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html), [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html), [VPC peering limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

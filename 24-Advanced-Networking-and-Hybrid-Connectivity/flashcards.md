# Review Flashcards

## Card 01

**Question:** A design uses Direct Connect and must encrypt data in transit. Which statement is accurate?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Direct Connect is not encrypted by default; choose suitable TLS, IPsec VPN, or supported MACsec protection for the required path. Private connectivity and encryption are separate properties. MACsec protects supported connection segments, so its coverage must be matched to the actual requirement rather than assumed end-to-end.

**AWS references:** [Direct Connect encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html).

</details>

## Card 02

**Question:** VPC A is peered with VPC B, and B is peered with C. There is no A-to-C peering or transit service. Can A use B to reach C through those peerings?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** No. VPC peering does not support transitive routing. A-to-B and B-to-C peerings do not create an A-to-C transit route. Use a supported connectivity design, such as suitable direct peerings or Transit Gateway attachments and routing.

**AWS references:** [VPC peering limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html), [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).

</details>

## Card 03

**Question:** Many VPCs and on-premises networks need a managed hub-and-spoke connectivity design with centralized routing domains. Which service fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** AWS Transit Gateway with appropriate attachments and route tables. Transit Gateway supplies a regional transit hub for supported attachments. Its route table associations, propagation, segmentation, and failure design still need explicit configuration.

**AWS references:** [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).

</details>

## Card 04

**Question:** A provider wants to expose a supported application service privately to consumer VPCs without providing general network transit between the VPCs. Which pattern fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** AWS PrivateLink with a suitable endpoint service and consumer interface endpoints. PrivateLink supports private connectivity to supported services through endpoints. It is service-oriented connectivity, not general-purpose transitive routing between all attached networks.

**AWS references:** [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html), [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html), [VPC peering limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html).

</details>

## Card 05

**Question:** A new design needs encrypted on-premises-to-VPC connectivity over existing internet access. Which service directly fits that transport model?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** AWS Site-to-Site VPN, with both provided tunnels and appropriate customer-side routing and redundancy. Site-to-Site VPN provides IPsec connectivity. Using both tunnels and designing customer-device and path redundancy improves resilience; no single connection choice guarantees uninterrupted availability.

**AWS references:** [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html), [Direct Connect encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html).

</details>

## Card 06

**Question:** VPC A is peered with VPC B, and B is peered with C. There is no A-to-C peering or transit service. Can A use B to reach C through those peerings?

Why does this alternative fail: “Yes. All peering connections are automatically transitive.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Peering does not provide transitive routing.

**AWS references:** [VPC peering limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html), [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).

</details>

## Card 07

**Question:** Many VPCs and on-premises networks need a managed hub-and-spoke connectivity design with centralized routing domains. Which service fits?

Why does this alternative fail: “A single security group shared as if it were a router.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Security groups filter traffic and do not provide transit routing.

**AWS references:** [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).

</details>

## Card 08

**Question:** A provider wants to expose a supported application service privately to consumer VPCs without providing general network transit between the VPCs. Which pattern fits?

Why does this alternative fail: “An unrestricted internet endpoint as the only service path.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** A public-only path violates the private connectivity requirement.

**AWS references:** [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html), [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html), [VPC peering limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

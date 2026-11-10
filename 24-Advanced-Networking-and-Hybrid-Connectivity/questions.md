# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 24-Q01 -->

A design uses Direct Connect and must encrypt data in transit. Which statement is accurate?

A) A dedicated circuit automatically means every application byte is encrypted end to end.

B) SSE-KMS on an S3 object encrypts every network hop automatically.

C) Direct Connect is not encrypted by default; choose suitable TLS, IPsec VPN, or supported MACsec protection for the required path.

D) A route table alone supplies cryptographic protection.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Private connectivity and encryption are separate properties. MACsec protects supported connection segments, so its coverage must be matched to the actual requirement rather than assumed end-to-end.

**Why the other options are incorrect:**

- **A:** A private circuit does not inherently provide encryption.
- **B:** Encryption at rest does not establish transport encryption.
- **D:** Routing entries do not encrypt traffic.

**AWS references:** [Direct Connect encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html).

</details>

## Question 2

<!-- question-id: 24-Q02 -->

VPC A is peered with VPC B, and B is peered with C. There is no A-to-C peering or transit service. Can A use B to reach C through those peerings?

A) Yes. All peering connections are automatically transitive.

B) Yes. Adding an IAM allow policy alone creates the transit path.

C) Yes. Increasing the DNS TTL enables transit.

D) No. VPC peering does not support transitive routing.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** A-to-B and B-to-C peerings do not create an A-to-C transit route. Use a supported connectivity design, such as suitable direct peerings or Transit Gateway attachments and routing.

**Why the other options are incorrect:**

- **A:** Peering does not provide transitive routing.
- **B:** IAM permissions do not create an unsupported network transit path.
- **C:** DNS caching does not change peering routing behavior.

**AWS references:** [VPC peering limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html), [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).

</details>

## Question 3

<!-- question-id: 24-Q03 -->

Many VPCs and on-premises networks need a managed hub-and-spoke connectivity design with centralized routing domains. Which service fits?

A) A single security group shared as if it were a router.

B) An S3 bucket as a transit router.

C) Assuming every possible VPC peering connection is already present.

D) AWS Transit Gateway with appropriate attachments and route tables.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Transit Gateway supplies a regional transit hub for supported attachments. Its route table associations, propagation, segmentation, and failure design still need explicit configuration.

**Why the other options are incorrect:**

- **A:** Security groups filter traffic and do not provide transit routing.
- **B:** Object storage is not a network transit hub.
- **C:** Peering links must be created and do not automatically form the requested hub.

**AWS references:** [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).

</details>

## Question 4

<!-- question-id: 24-Q04 -->

A provider wants to expose a supported application service privately to consumer VPCs without providing general network transit between the VPCs. Which pattern fits?

A) An unrestricted internet endpoint as the only service path.

B) AWS PrivateLink with a suitable endpoint service and consumer interface endpoints.

C) A gateway endpoint for every arbitrary provider service.

D) Transitive VPC peering assumed to require no routing design.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** PrivateLink supports private connectivity to supported services through endpoints. It is service-oriented connectivity, not general-purpose transitive routing between all attached networks.

**Why the other options are incorrect:**

- **A:** A public-only path violates the private connectivity requirement.
- **C:** Gateway endpoints do not support arbitrary provider application services.
- **D:** VPC peering is not transitive and is a different network model.

**AWS references:** [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html), [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html), [VPC peering limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html).

</details>

## Question 5

<!-- question-id: 24-Q05 -->

A new design needs encrypted on-premises-to-VPC connectivity over existing internet access. Which service directly fits that transport model?

A) Direct Connect alone assumed to be internet-based and encrypted by default.

B) An S3 gateway endpoint advertised as an on-premises VPN server.

C) AWS Site-to-Site VPN, with both provided tunnels and appropriate customer-side routing and redundancy.

D) An EC2 security group alone.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Site-to-Site VPN provides IPsec connectivity. Using both tunnels and designing customer-device and path redundancy improves resilience; no single connection choice guarantees uninterrupted availability.

**Why the other options are incorrect:**

- **A:** Direct Connect is a different connectivity model and lacks default transport encryption.
- **B:** A gateway endpoint is not an on-premises IPsec VPN service.
- **D:** A traffic filter cannot create an encrypted tunnel.

**AWS references:** [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html), [Direct Connect encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

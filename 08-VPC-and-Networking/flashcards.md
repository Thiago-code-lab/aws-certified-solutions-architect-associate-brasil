# Review Flashcards

## Card 01

**Question:** EC2 workloads in a VPC need same-Region S3 access without using an internet gateway or a NAT gateway. Which endpoint type can be added to the relevant route tables?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** An S3 gateway VPC endpoint. An S3 gateway endpoint provides a route-based private path to supported S3 destinations. Bucket, endpoint, and IAM policies still need to permit the requests.

**AWS references:** [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html).

</details>

## Card 02

**Question:** A security group permits an EC2 instance to initiate an outbound TCP connection. What is its behavior for response traffic belonging to that connection?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** It allows the response traffic through connection tracking, subject to the documented tracking behavior. Security groups are stateful. Network ACLs and routes remain separate requirements; the security group does not replace either.

**AWS references:** [VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html), [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html).

</details>

## Card 03

**Question:** A custom network ACL allows inbound HTTPS to an instance but denies all outbound traffic. Why can a client connection still fail?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The stateless ACL must also allow the required outbound return traffic, including client ephemeral ports. Network ACLs evaluate inbound and outbound packets independently. Required return traffic must match an outbound allow rule before a deny rule.

**AWS references:** [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), [VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html).

</details>

## Card 04

**Question:** A subnet route table points to an internet gateway. An EC2 instance has only a private IPv4 address. Which statement is correct for direct IPv4 internet connectivity?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The route makes the subnet public, but the instance also needs a public IPv4 address or Elastic IP and appropriate network rules for direct internet communication. Public-subnet routing and public addressing are separate requirements. Security groups and network ACLs must also allow the intended traffic.

**AWS references:** [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html).

</details>

## Card 05

**Question:** Private IPv4 instances need to initiate connections to public software repositories, while unsolicited inbound internet connections must remain unavailable. Which design fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Use an appropriately routed public NAT gateway and keep the instances without public IPv4 addresses. A public NAT gateway supports outbound-initiated IPv4 internet connectivity for private instances. It does not accept unsolicited inbound connections to them; routing and firewall rules still matter.

**AWS references:** [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html), [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html), [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html).

</details>

## Card 06

**Question:** A security group permits an EC2 instance to initiate an outbound TCP connection. What is its behavior for response traffic belonging to that connection?

Why does this alternative fail: “It always requires a matching inbound security group rule for every response packet.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** This describes a stateless filtering requirement, not normal tracked security group responses.

**AWS references:** [VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html), [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html).

</details>

## Card 07

**Question:** A custom network ACL allows inbound HTTPS to an instance but denies all outbound traffic. Why can a client connection still fail?

Why does this alternative fail: “Network ACLs automatically allow all responses because they are stateful.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Network ACLs are stateless, unlike security groups.

**AWS references:** [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), [VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html).

</details>

## Card 08

**Question:** A subnet route table points to an internet gateway. An EC2 instance has only a private IPv4 address. Which statement is correct for direct IPv4 internet connectivity?

Why does this alternative fail: “The route alone assigns the instance a public IPv4 address.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Route table entries do not assign public addresses.

**AWS references:** [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

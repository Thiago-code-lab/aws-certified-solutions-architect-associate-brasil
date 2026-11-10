# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 08-Q01 -->

EC2 workloads in a VPC need same-Region S3 access without using an internet gateway or a NAT gateway. Which endpoint type can be added to the relevant route tables?

A) A public NAT gateway for every S3 request.

B) An internet gateway attached directly to the S3 bucket.

C) A security group rule with no routing or endpoint change.

D) An S3 gateway VPC endpoint.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** An S3 gateway endpoint provides a route-based private path to supported S3 destinations. Bucket, endpoint, and IAM policies still need to permit the requests.

**Why the other options are incorrect:**

- **A:** The requirement explicitly excludes a NAT path.
- **B:** Internet gateways attach to VPCs, not S3 buckets.
- **C:** A firewall rule does not create the required private service path.

**AWS references:** [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html).

</details>

## Question 2

<!-- question-id: 08-Q02 -->

A security group permits an EC2 instance to initiate an outbound TCP connection. What is its behavior for response traffic belonging to that connection?

A) It always requires a matching inbound security group rule for every response packet.

B) It evaluates numbered deny rules before allow rules.

C) It allows the response traffic through connection tracking, subject to the documented tracking behavior.

D) It provides a route to the destination even if the route table has none.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Security groups are stateful. Network ACLs and routes remain separate requirements; the security group does not replace either.

**Why the other options are incorrect:**

- **A:** This describes a stateless filtering requirement, not normal tracked security group responses.
- **B:** Security groups have allow rules rather than ordered explicit deny rules.
- **D:** Filtering permission cannot supply a missing network route.

**AWS references:** [VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html), [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html).

</details>

## Question 3

<!-- question-id: 08-Q03 -->

A custom network ACL allows inbound HTTPS to an instance but denies all outbound traffic. Why can a client connection still fail?

A) Network ACLs automatically allow all responses because they are stateful.

B) The stateless ACL must also allow the required outbound return traffic, including client ephemeral ports.

C) Adding an IAM policy to the client automatically changes the ACL.

D) An S3 lifecycle rule must first expire the connection.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Network ACLs evaluate inbound and outbound packets independently. Required return traffic must match an outbound allow rule before a deny rule.

**Why the other options are incorrect:**

- **A:** Network ACLs are stateless, unlike security groups.
- **C:** IAM authorization does not rewrite subnet network ACL rules.
- **D:** S3 object lifecycle has no role in TCP return traffic.

**AWS references:** [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), [VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html).

</details>

## Question 4

<!-- question-id: 08-Q04 -->

A subnet route table points to an internet gateway. An EC2 instance has only a private IPv4 address. Which statement is correct for direct IPv4 internet connectivity?

A) The route makes the subnet public, but the instance also needs a public IPv4 address or Elastic IP and appropriate network rules for direct internet communication.

B) The route alone assigns the instance a public IPv4 address.

C) A bucket policy supplies a public address to the instance.

D) Every instance in any subnet is directly reachable from the internet.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Public-subnet routing and public addressing are separate requirements. Security groups and network ACLs must also allow the intended traffic.

**Why the other options are incorrect:**

- **B:** Route table entries do not assign public addresses.
- **C:** S3 authorization has no effect on EC2 address assignment.
- **D:** Private addresses are not directly internet-routable.

**AWS references:** [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html).

</details>

## Question 5

<!-- question-id: 08-Q05 -->

Private IPv4 instances need to initiate connections to public software repositories, while unsolicited inbound internet connections must remain unavailable. Which design fits?

A) Assign each private instance a public address and allow all inbound traffic.

B) Use an appropriately routed public NAT gateway and keep the instances without public IPv4 addresses.

C) Use an S3 gateway endpoint as a general internet proxy.

D) Attach an internet gateway to each instance network interface.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** A public NAT gateway supports outbound-initiated IPv4 internet connectivity for private instances. It does not accept unsolicited inbound connections to them; routing and firewall rules still matter.

**Why the other options are incorrect:**

- **A:** This exposes directly addressable instances and violates the inbound constraint.
- **C:** An S3 gateway endpoint is not a general-purpose internet proxy.
- **D:** Internet gateways attach to the VPC, not individual interfaces.

**AWS references:** [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html), [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html), [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

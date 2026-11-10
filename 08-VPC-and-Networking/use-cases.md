# Use Cases

## Scenario 1: Private S3 network path

**Requirement:** EC2 workloads in a VPC need same-Region S3 access without using an internet gateway or a NAT gateway. Which endpoint type can be added to the relevant route tables?

**Recommended design:** An S3 gateway VPC endpoint.

**Reason and boundary:** An S3 gateway endpoint provides a route-based private path to supported S3 destinations. Bucket, endpoint, and IAM policies still need to permit the requests.

**Rejected alternative:** A public NAT gateway for every S3 request. The requirement explicitly excludes a NAT path.

**AWS references:** [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html).

## Scenario 2: Security group statefulness

**Requirement:** A security group permits an EC2 instance to initiate an outbound TCP connection. What is its behavior for response traffic belonging to that connection?

**Recommended design:** It allows the response traffic through connection tracking, subject to the documented tracking behavior.

**Reason and boundary:** Security groups are stateful. Network ACLs and routes remain separate requirements; the security group does not replace either.

**Rejected alternative:** It always requires a matching inbound security group rule for every response packet. This describes a stateless filtering requirement, not normal tracked security group responses.

**AWS references:** [VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html), [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html).

## Scenario 3: Network ACL return traffic

**Requirement:** A custom network ACL allows inbound HTTPS to an instance but denies all outbound traffic. Why can a client connection still fail?

**Recommended design:** The stateless ACL must also allow the required outbound return traffic, including client ephemeral ports.

**Reason and boundary:** Network ACLs evaluate inbound and outbound packets independently. Required return traffic must match an outbound allow rule before a deny rule.

**Rejected alternative:** Network ACLs automatically allow all responses because they are stateful. Network ACLs are stateless, unlike security groups.

**AWS references:** [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), [VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html).

## Scenario 4: Public subnet versus reachable instance

**Requirement:** A subnet route table points to an internet gateway. An EC2 instance has only a private IPv4 address. Which statement is correct for direct IPv4 internet connectivity?

**Recommended design:** The route makes the subnet public, but the instance also needs a public IPv4 address or Elastic IP and appropriate network rules for direct internet communication.

**Reason and boundary:** Public-subnet routing and public addressing are separate requirements. Security groups and network ACLs must also allow the intended traffic.

**Rejected alternative:** The route alone assigns the instance a public IPv4 address. Route table entries do not assign public addresses.

**AWS references:** [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

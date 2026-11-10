# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Private S3 network path | An S3 gateway VPC endpoint. | An S3 gateway endpoint provides a route-based private path to supported S3 destinations. Bucket, endpoint, and IAM policies still need to permit the requests. |
| Security group statefulness | It allows the response traffic through connection tracking, subject to the documented tracking behavior. | Security groups are stateful. Network ACLs and routes remain separate requirements; the security group does not replace either. |
| Network ACL return traffic | The stateless ACL must also allow the required outbound return traffic, including client ephemeral ports. | Network ACLs evaluate inbound and outbound packets independently. Required return traffic must match an outbound allow rule before a deny rule. |
| Public subnet versus reachable instance | The route makes the subnet public, but the instance also needs a public IPv4 address or Elastic IP and appropriate network rules for direct internet communication. | Public-subnet routing and public addressing are separate requirements. Security groups and network ACLs must also allow the intended traffic. |
| Outbound NAT does not grant inbound access | Use an appropriately routed public NAT gateway and keep the instances without public IPv4 addresses. | A public NAT gateway supports outbound-initiated IPv4 internet connectivity for private instances. It does not accept unsolicited inbound connections to them; routing and firewall rules still matter. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Private S3 network path:** The requirement explicitly excludes a NAT path.
- **Security group statefulness:** This describes a stateless filtering requirement, not normal tracked security group responses.
- **Network ACL return traffic:** Network ACLs are stateless, unlike security groups.
- **Public subnet versus reachable instance:** Route table entries do not assign public addresses.
- **Outbound NAT does not grant inbound access:** This exposes directly addressable instances and violates the inbound constraint.

## AWS References

[Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html), [VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html), [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html), [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

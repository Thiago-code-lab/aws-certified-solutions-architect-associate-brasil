# VPC and Networking

## Overview

Trace both the network path and the authorization path. Route tables, addresses, internet and NAT gateways, endpoints, security groups, and network ACLs have distinct responsibilities.

## Key Concepts

- **Private S3 network path:** An S3 gateway endpoint provides a route-based private path to supported S3 destinations. Bucket, endpoint, and IAM policies still need to permit the requests.
- **Security group statefulness:** Security groups are stateful. Network ACLs and routes remain separate requirements; the security group does not replace either.
- **Network ACL return traffic:** Network ACLs evaluate inbound and outbound packets independently. Required return traffic must match an outbound allow rule before a deny rule.
- **Public subnet versus reachable instance:** Public-subnet routing and public addressing are separate requirements. Security groups and network ACLs must also allow the intended traffic.
- **Outbound NAT does not grant inbound access:** A public NAT gateway supports outbound-initiated IPv4 internet connectivity for private instances. It does not accept unsolicited inbound connections to them; routing and firewall rules still matter.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Private S3 network path:** An S3 gateway VPC endpoint.
2. **Security group statefulness:** It allows the response traffic through connection tracking, subject to the documented tracking behavior.
3. **Network ACL return traffic:** The stateless ACL must also allow the required outbound return traffic, including client ephemeral ports.
4. **Public subnet versus reachable instance:** The route makes the subnet public, but the instance also needs a public IPv4 address or Elastic IP and appropriate network rules for direct internet communication.
5. **Outbound NAT does not grant inbound access:** Use an appropriately routed public NAT gateway and keep the instances without public IPv4 addresses.

## Common Pitfalls

- The requirement explicitly excludes a NAT path.
- This describes a stateless filtering requirement, not normal tracked security group responses.
- Network ACLs are stateless, unlike security groups.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html), [VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html), [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html), [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

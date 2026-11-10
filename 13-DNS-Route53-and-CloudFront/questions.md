# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 13-Q01 -->

A new CloudFront distribution serves a regular private S3 bucket origin. The bucket must stay private while CloudFront can read objects. Which design is recommended?

A) Make the bucket publicly readable and rely only on an obscure URL.

B) Configure OAC, signed origin requests, and a bucket policy restricted to the intended CloudFront distribution.

C) Use OAC with an S3 static website endpoint as if it were a regular S3 origin.

D) Attach an EC2 security group to the S3 bucket.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Origin access control authorizes CloudFront access to a regular S3 origin. The bucket policy must allow the intended distribution. Website endpoints are custom origins and do not support OAC.

**Why the other options are incorrect:**

- **A:** Obscurity does not enforce private origin access.
- **C:** OAC is not supported for S3 website endpoints.
- **D:** S3 bucket authorization is not implemented by attaching EC2 security groups.

**AWS references:** [CloudFront origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html).

</details>

## Question 2

<!-- question-id: 13-Q02 -->

An application has equivalent endpoints in multiple AWS Regions. DNS responses should favor the Region offering the best latency to the user. Which Route 53 policy fits?

A) Latency-based routing.

B) Weighted routing used solely for a fixed traffic proportion.

C) Simple routing to one endpoint only.

D) An S3 lifecycle rule.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Latency-based routing selects among configured regional resources using latency information. It does not promise the geographically nearest location or a fixed split of requests.

**Why the other options are incorrect:**

- **B:** Weighted routing expresses configured proportions rather than optimizing latency.
- **C:** One simple endpoint does not make the requested regional selection.
- **D:** Object retention rules do not select DNS endpoints.

**AWS references:** [Route 53 routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html).

</details>

## Question 3

<!-- question-id: 13-Q03 -->

A team wants DNS responses distributed between old and new regional endpoints in configured relative proportions. Which Route 53 policy is intended for this?

A) Failover routing used only as active-passive standby.

B) A security group with two outbound rules.

C) Weighted routing.

D) A larger EC2 instance for the old endpoint.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Weighted records support relative response proportions. DNS caching and resolver behavior mean the observed application-request split is not an exact per-request percentage guarantee.

**Why the other options are incorrect:**

- **A:** Active-passive failover is not a proportional rollout policy.
- **B:** Firewall rules do not assign DNS response weights.
- **D:** Instance size does not control DNS selection proportions.

**AWS references:** [Route 53 routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html).

</details>

## Question 4

<!-- question-id: 13-Q04 -->

A globally used UDP application needs static anycast entry IPs and routing across the AWS network to healthy regional endpoints. Which service fits?

A) AWS Global Accelerator with supported endpoints.

B) CloudFront as a general-purpose arbitrary UDP proxy.

C) An S3 website endpoint.

D) A NAT gateway as the global inbound application endpoint.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Global Accelerator supports TCP and UDP applications with static anycast IP addresses and regional endpoint routing. CloudFront is an HTTP(S) content delivery service, not an arbitrary UDP proxy.

**Why the other options are incorrect:**

- **B:** CloudFront does not provide the arbitrary UDP proxy behavior in the stem.
- **C:** An S3 website endpoint is not a UDP application accelerator.
- **D:** NAT gateways are not global inbound anycast application front doors.

**AWS references:** [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html).

</details>

## Question 5

<!-- question-id: 13-Q05 -->

An HTTP application behind an ALB needs managed rule-based filtering for common web exploits. Which service is designed for that application-layer filtering?

A) A Route 53 TXT record.

B) An EBS snapshot.

C) A network ACL expected to inspect SQL injection payloads.

D) AWS WAF associated with the supported application resource.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** AWS WAF evaluates web requests with rules and can protect supported resources such as an ALB. Its rules complement, rather than replace, secure application design and network controls.

**Why the other options are incorrect:**

- **A:** DNS text records do not inspect HTTP requests.
- **B:** A block-storage snapshot is not a web firewall.
- **C:** Subnet ACLs filter network traffic rather than parsing web exploit payloads.

**AWS references:** [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

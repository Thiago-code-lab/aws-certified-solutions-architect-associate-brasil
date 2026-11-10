# Review Flashcards

## Card 01

**Question:** A new CloudFront distribution serves a regular private S3 bucket origin. The bucket must stay private while CloudFront can read objects. Which design is recommended?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Configure OAC, signed origin requests, and a bucket policy restricted to the intended CloudFront distribution. Origin access control authorizes CloudFront access to a regular S3 origin. The bucket policy must allow the intended distribution. Website endpoints are custom origins and do not support OAC.

**AWS references:** [CloudFront origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html).

</details>

## Card 02

**Question:** An application has equivalent endpoints in multiple AWS Regions. DNS responses should favor the Region offering the best latency to the user. Which Route 53 policy fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Latency-based routing. Latency-based routing selects among configured regional resources using latency information. It does not promise the geographically nearest location or a fixed split of requests.

**AWS references:** [Route 53 routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html).

</details>

## Card 03

**Question:** A team wants DNS responses distributed between old and new regional endpoints in configured relative proportions. Which Route 53 policy is intended for this?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Weighted routing. Weighted records support relative response proportions. DNS caching and resolver behavior mean the observed application-request split is not an exact per-request percentage guarantee.

**AWS references:** [Route 53 routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html).

</details>

## Card 04

**Question:** A globally used UDP application needs static anycast entry IPs and routing across the AWS network to healthy regional endpoints. Which service fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** AWS Global Accelerator with supported endpoints. Global Accelerator supports TCP and UDP applications with static anycast IP addresses and regional endpoint routing. CloudFront is an HTTP(S) content delivery service, not an arbitrary UDP proxy.

**AWS references:** [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html).

</details>

## Card 05

**Question:** An HTTP application behind an ALB needs managed rule-based filtering for common web exploits. Which service is designed for that application-layer filtering?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** AWS WAF associated with the supported application resource. AWS WAF evaluates web requests with rules and can protect supported resources such as an ALB. Its rules complement, rather than replace, secure application design and network controls.

**AWS references:** [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html).

</details>

## Card 06

**Question:** An application has equivalent endpoints in multiple AWS Regions. DNS responses should favor the Region offering the best latency to the user. Which Route 53 policy fits?

Why does this alternative fail: “Weighted routing used solely for a fixed traffic proportion.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Weighted routing expresses configured proportions rather than optimizing latency.

**AWS references:** [Route 53 routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html).

</details>

## Card 07

**Question:** A team wants DNS responses distributed between old and new regional endpoints in configured relative proportions. Which Route 53 policy is intended for this?

Why does this alternative fail: “Failover routing used only as active-passive standby.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Active-passive failover is not a proportional rollout policy.

**AWS references:** [Route 53 routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html).

</details>

## Card 08

**Question:** A globally used UDP application needs static anycast entry IPs and routing across the AWS network to healthy regional endpoints. Which service fits?

Why does this alternative fail: “CloudFront as a general-purpose arbitrary UDP proxy.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** CloudFront does not provide the arbitrary UDP proxy behavior in the stem.

**AWS references:** [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

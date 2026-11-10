# Use Cases

## Scenario 1: Private S3 origin access

**Requirement:** A new CloudFront distribution serves a regular private S3 bucket origin. The bucket must stay private while CloudFront can read objects. Which design is recommended?

**Recommended design:** Configure OAC, signed origin requests, and a bucket policy restricted to the intended CloudFront distribution.

**Reason and boundary:** Origin access control authorizes CloudFront access to a regular S3 origin. The bucket policy must allow the intended distribution. Website endpoints are custom origins and do not support OAC.

**Rejected alternative:** Make the bucket publicly readable and rely only on an obscure URL. Obscurity does not enforce private origin access.

**AWS references:** [CloudFront origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html).

## Scenario 2: Latency-based DNS

**Requirement:** An application has equivalent endpoints in multiple AWS Regions. DNS responses should favor the Region offering the best latency to the user. Which Route 53 policy fits?

**Recommended design:** Latency-based routing.

**Reason and boundary:** Latency-based routing selects among configured regional resources using latency information. It does not promise the geographically nearest location or a fixed split of requests.

**Rejected alternative:** Weighted routing used solely for a fixed traffic proportion. Weighted routing expresses configured proportions rather than optimizing latency.

**AWS references:** [Route 53 routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html).

## Scenario 3: DNS-weighted rollout

**Requirement:** A team wants DNS responses distributed between old and new regional endpoints in configured relative proportions. Which Route 53 policy is intended for this?

**Recommended design:** Weighted routing.

**Reason and boundary:** Weighted records support relative response proportions. DNS caching and resolver behavior mean the observed application-request split is not an exact per-request percentage guarantee.

**Rejected alternative:** Failover routing used only as active-passive standby. Active-passive failover is not a proportional rollout policy.

**AWS references:** [Route 53 routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html).

## Scenario 4: Global UDP acceleration

**Requirement:** A globally used UDP application needs static anycast entry IPs and routing across the AWS network to healthy regional endpoints. Which service fits?

**Recommended design:** AWS Global Accelerator with supported endpoints.

**Reason and boundary:** Global Accelerator supports TCP and UDP applications with static anycast IP addresses and regional endpoint routing. CloudFront is an HTTP(S) content delivery service, not an arbitrary UDP proxy.

**Rejected alternative:** CloudFront as a general-purpose arbitrary UDP proxy. CloudFront does not provide the arbitrary UDP proxy behavior in the stem.

**AWS references:** [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

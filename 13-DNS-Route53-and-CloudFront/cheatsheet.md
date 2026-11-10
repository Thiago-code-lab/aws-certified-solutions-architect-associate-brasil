# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Private S3 origin access | Configure OAC, signed origin requests, and a bucket policy restricted to the intended CloudFront distribution. | Origin access control authorizes CloudFront access to a regular S3 origin. The bucket policy must allow the intended distribution. Website endpoints are custom origins and do not support OAC. |
| Latency-based DNS | Latency-based routing. | Latency-based routing selects among configured regional resources using latency information. It does not promise the geographically nearest location or a fixed split of requests. |
| DNS-weighted rollout | Weighted routing. | Weighted records support relative response proportions. DNS caching and resolver behavior mean the observed application-request split is not an exact per-request percentage guarantee. |
| Global UDP acceleration | AWS Global Accelerator with supported endpoints. | Global Accelerator supports TCP and UDP applications with static anycast IP addresses and regional endpoint routing. CloudFront is an HTTP(S) content delivery service, not an arbitrary UDP proxy. |
| Web request filtering | AWS WAF associated with the supported application resource. | AWS WAF evaluates web requests with rules and can protect supported resources such as an ALB. Its rules complement, rather than replace, secure application design and network controls. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Private S3 origin access:** Obscurity does not enforce private origin access.
- **Latency-based DNS:** Weighted routing expresses configured proportions rather than optimizing latency.
- **DNS-weighted rollout:** Active-passive failover is not a proportional rollout policy.
- **Global UDP acceleration:** CloudFront does not provide the arbitrary UDP proxy behavior in the stem.
- **Web request filtering:** DNS text records do not inspect HTTP requests.

## AWS References

[CloudFront origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html), [Route 53 routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html), [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html), [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

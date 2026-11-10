# DNS, Route 53, and CloudFront

## Overview

Separate DNS selection, HTTP content delivery, private origin authorization, global network acceleration, and web request filtering. DNS cache behavior and endpoint health affect traffic changes.

## Key Concepts

- **Private S3 origin access:** Origin access control authorizes CloudFront access to a regular S3 origin. The bucket policy must allow the intended distribution. Website endpoints are custom origins and do not support OAC.
- **Latency-based DNS:** Latency-based routing selects among configured regional resources using latency information. It does not promise the geographically nearest location or a fixed split of requests.
- **DNS-weighted rollout:** Weighted records support relative response proportions. DNS caching and resolver behavior mean the observed application-request split is not an exact per-request percentage guarantee.
- **Global UDP acceleration:** Global Accelerator supports TCP and UDP applications with static anycast IP addresses and regional endpoint routing. CloudFront is an HTTP(S) content delivery service, not an arbitrary UDP proxy.
- **Web request filtering:** AWS WAF evaluates web requests with rules and can protect supported resources such as an ALB. Its rules complement, rather than replace, secure application design and network controls.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Private S3 origin access:** Configure OAC, signed origin requests, and a bucket policy restricted to the intended CloudFront distribution.
2. **Latency-based DNS:** Latency-based routing.
3. **DNS-weighted rollout:** Weighted routing.
4. **Global UDP acceleration:** AWS Global Accelerator with supported endpoints.
5. **Web request filtering:** AWS WAF associated with the supported application resource.

## Common Pitfalls

- Obscurity does not enforce private origin access.
- Weighted routing expresses configured proportions rather than optimizing latency.
- Active-passive failover is not a proportional rollout policy.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[CloudFront origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html), [Route 53 routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html), [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html), [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

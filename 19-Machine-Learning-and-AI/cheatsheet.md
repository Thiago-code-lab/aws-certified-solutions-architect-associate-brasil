# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Managed custom ML | Amazon SageMaker AI. | SageMaker AI provides managed training and deployment capabilities. The team still owns dataset quality, model evaluation, permissions, and the suitability of the model for its use case. |
| Pretrained text analysis | Amazon Comprehend. | Comprehend offers pretrained natural-language analysis, including entities and sentiment. Supported languages, input types, and feature constraints must be checked for the specific operation. |
| Document extraction | Amazon Textract. | Textract supports document text, form, and table extraction. Validate extraction quality and route uncertain business-critical results for appropriate review. |
| Generative AI context without scope claims | Amazon Bedrock. | Bedrock provides managed foundation-model access. This is optional architecture context: the current SAA-C03 service list is non-exhaustive, and the repository must not claim a guaranteed exam question or weight for this topic. |
| Managed inference still needs evaluation | Evaluate output quality on representative data, protect inputs and outputs, and implement suitable handling for errors or unacceptable results. | Managed infrastructure does not establish that a model is appropriate for every business input. Application data handling, permissions, evaluation, and failure behavior remain part of the customer design. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Managed custom ML:** DNS routing does not train or host a custom model.
- **Pretrained text analysis:** Text extraction and document layout analysis are not the requested sentiment capability.
- **Document extraction:** Sentiment analysis is not document form and table extraction.
- **Generative AI context without scope claims:** Config tracks resource configuration and compliance, not foundation-model inference.
- **Managed inference still needs evaluation:** Managed hosting is not a guarantee of prediction correctness.

## AWS References

[Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html), [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html), [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html), [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

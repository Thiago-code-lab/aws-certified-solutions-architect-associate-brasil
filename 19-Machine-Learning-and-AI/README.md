# Machine Learning and AI

## Overview

Match managed AI/ML services to a concrete capability: custom model development, pretrained language analysis, or document extraction. Amazon SageMaker AI is the current name of the ML service. Bedrock is optional generative AI architecture context; no fixed exam frequency is claimed.

## Key Concepts

- **Managed custom ML:** SageMaker AI provides managed training and deployment capabilities. The team still owns dataset quality, model evaluation, permissions, and the suitability of the model for its use case.
- **Pretrained text analysis:** Comprehend offers pretrained natural-language analysis, including entities and sentiment. Supported languages, input types, and feature constraints must be checked for the specific operation.
- **Document extraction:** Textract supports document text, form, and table extraction. Validate extraction quality and route uncertain business-critical results for appropriate review.
- **Generative AI context without scope claims:** Bedrock provides managed foundation-model access. This is optional architecture context: the current SAA-C03 service list is non-exhaustive, and the repository must not claim a guaranteed exam question or weight for this topic.
- **Managed inference still needs evaluation:** Managed infrastructure does not establish that a model is appropriate for every business input. Application data handling, permissions, evaluation, and failure behavior remain part of the customer design.

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Managed custom ML:** Amazon SageMaker AI.
2. **Pretrained text analysis:** Amazon Comprehend.
3. **Document extraction:** Amazon Textract.
4. **Generative AI context without scope claims:** Amazon Bedrock.
5. **Managed inference still needs evaluation:** Evaluate output quality on representative data, protect inputs and outputs, and implement suitable handling for errors or unacceptable results.

## Common Pitfalls

- DNS routing does not train or host a custom model.
- Text extraction and document layout analysis are not the requested sentiment capability.
- Sentiment analysis is not document form and table extraction.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html), [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html), [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html), [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

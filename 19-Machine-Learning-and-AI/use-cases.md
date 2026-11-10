# Use Cases

## Scenario 1: Managed custom ML

**Requirement:** Data scientists need managed tools to build, train, and deploy a custom machine learning model. Which service directly supports that lifecycle?

**Recommended design:** Amazon SageMaker AI.

**Reason and boundary:** SageMaker AI provides managed training and deployment capabilities. The team still owns dataset quality, model evaluation, permissions, and the suitability of the model for its use case.

**Rejected alternative:** Amazon Route 53. DNS routing does not train or host a custom model.

**AWS references:** [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html).

## Scenario 2: Pretrained text analysis

**Requirement:** An application needs entity and sentiment analysis of supported text without first building a custom model. Which service fits?

**Recommended design:** Amazon Comprehend.

**Reason and boundary:** Comprehend offers pretrained natural-language analysis, including entities and sentiment. Supported languages, input types, and feature constraints must be checked for the specific operation.

**Rejected alternative:** Amazon Textract used solely to extract document text and tables. Text extraction and document layout analysis are not the requested sentiment capability.

**AWS references:** [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html), [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html).

## Scenario 3: Document extraction

**Requirement:** A workflow must extract form fields and tables from scanned business documents using a managed document-analysis API. Which service fits?

**Recommended design:** Amazon Textract.

**Reason and boundary:** Textract supports document text, form, and table extraction. Validate extraction quality and route uncertain business-critical results for appropriate review.

**Rejected alternative:** Amazon Comprehend sentiment analysis alone. Sentiment analysis is not document form and table extraction.

**AWS references:** [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html), [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html).

## Scenario 4: Generative AI context without scope claims

**Requirement:** An optional generative AI exercise needs managed access to foundation models rather than building a model-serving fleet. Which service matches that capability?

**Recommended design:** Amazon Bedrock.

**Reason and boundary:** Bedrock provides managed foundation-model access. This is optional architecture context: the current SAA-C03 service list is non-exhaustive, and the repository must not claim a guaranteed exam question or weight for this topic.

**Rejected alternative:** AWS Config. Config tracks resource configuration and compliance, not foundation-model inference.

**AWS references:** [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

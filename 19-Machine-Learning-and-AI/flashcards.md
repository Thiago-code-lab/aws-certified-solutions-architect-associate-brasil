# Review Flashcards

## Card 01

**Question:** Data scientists need managed tools to build, train, and deploy a custom machine learning model. Which service directly supports that lifecycle?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Amazon SageMaker AI. SageMaker AI provides managed training and deployment capabilities. The team still owns dataset quality, model evaluation, permissions, and the suitability of the model for its use case.

**AWS references:** [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html).

</details>

## Card 02

**Question:** An application needs entity and sentiment analysis of supported text without first building a custom model. Which service fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Amazon Comprehend. Comprehend offers pretrained natural-language analysis, including entities and sentiment. Supported languages, input types, and feature constraints must be checked for the specific operation.

**AWS references:** [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html), [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html).

</details>

## Card 03

**Question:** A workflow must extract form fields and tables from scanned business documents using a managed document-analysis API. Which service fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Amazon Textract. Textract supports document text, form, and table extraction. Validate extraction quality and route uncertain business-critical results for appropriate review.

**AWS references:** [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html), [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html).

</details>

## Card 04

**Question:** An optional generative AI exercise needs managed access to foundation models rather than building a model-serving fleet. Which service matches that capability?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Amazon Bedrock. Bedrock provides managed foundation-model access. This is optional architecture context: the current SAA-C03 service list is non-exhaustive, and the repository must not claim a guaranteed exam question or weight for this topic.

**AWS references:** [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html).

</details>

## Card 05

**Question:** A team uses a managed model API for customer-facing decisions. Which operational responsibility remains with the team?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Evaluate output quality on representative data, protect inputs and outputs, and implement suitable handling for errors or unacceptable results. Managed infrastructure does not establish that a model is appropriate for every business input. Application data handling, permissions, evaluation, and failure behavior remain part of the customer design.

**AWS references:** [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

## Card 06

**Question:** An application needs entity and sentiment analysis of supported text without first building a custom model. Which service fits?

Why does this alternative fail: “Amazon Textract used solely to extract document text and tables.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Text extraction and document layout analysis are not the requested sentiment capability.

**AWS references:** [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html), [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html).

</details>

## Card 07

**Question:** A workflow must extract form fields and tables from scanned business documents using a managed document-analysis API. Which service fits?

Why does this alternative fail: “Amazon Comprehend sentiment analysis alone.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Sentiment analysis is not document form and table extraction.

**AWS references:** [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html), [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html).

</details>

## Card 08

**Question:** An optional generative AI exercise needs managed access to foundation models rather than building a model-serving fleet. Which service matches that capability?

Why does this alternative fail: “AWS Config.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Config tracks resource configuration and compliance, not foundation-model inference.

**AWS references:** [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 19-Q01 -->

Data scientists need managed tools to build, train, and deploy a custom machine learning model. Which service directly supports that lifecycle?

A) Amazon SageMaker AI.

B) Amazon Route 53.

C) AWS KMS alone.

D) An S3 gateway endpoint alone.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** SageMaker AI provides managed training and deployment capabilities. The team still owns dataset quality, model evaluation, permissions, and the suitability of the model for its use case.

**Why the other options are incorrect:**

- **B:** DNS routing does not train or host a custom model.
- **C:** Key management is not a model-training platform.
- **D:** A private network path to S3 is not a training or inference service.

**AWS references:** [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html).

</details>

## Question 2

<!-- question-id: 19-Q02 -->

An application needs entity and sentiment analysis of supported text without first building a custom model. Which service fits?

A) Amazon Textract used solely to extract document text and tables.

B) AWS Direct Connect.

C) An Auto Scaling group health check.

D) Amazon Comprehend.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** Comprehend offers pretrained natural-language analysis, including entities and sentiment. Supported languages, input types, and feature constraints must be checked for the specific operation.

**Why the other options are incorrect:**

- **A:** Text extraction and document layout analysis are not the requested sentiment capability.
- **B:** A dedicated network connection does not perform language analysis.
- **C:** A health check evaluates service health rather than text meaning.

**AWS references:** [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html), [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html).

</details>

## Question 3

<!-- question-id: 19-Q03 -->

A workflow must extract form fields and tables from scanned business documents using a managed document-analysis API. Which service fits?

A) Amazon Comprehend sentiment analysis alone.

B) An S3 lifecycle rule.

C) Amazon Textract.

D) A Route 53 latency policy.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Textract supports document text, form, and table extraction. Validate extraction quality and route uncertain business-critical results for appropriate review.

**Why the other options are incorrect:**

- **A:** Sentiment analysis is not document form and table extraction.
- **B:** Lifecycle rules move or expire objects rather than parse document contents.
- **D:** DNS routing does not extract fields from documents.

**AWS references:** [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html), [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html).

</details>

## Question 4

<!-- question-id: 19-Q04 -->

An optional generative AI exercise needs managed access to foundation models rather than building a model-serving fleet. Which service matches that capability?

A) Amazon Bedrock.

B) AWS Config.

C) A network ACL.

D) An EBS snapshot.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Bedrock provides managed foundation-model access. This is optional architecture context: the current SAA-C03 service list is non-exhaustive, and the repository must not claim a guaranteed exam question or weight for this topic.

**Why the other options are incorrect:**

- **B:** Config tracks resource configuration and compliance, not foundation-model inference.
- **C:** A subnet traffic filter does not host foundation models.
- **D:** A storage snapshot is not a model inference API.

**AWS references:** [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html).

</details>

## Question 5

<!-- question-id: 19-Q05 -->

A team uses a managed model API for customer-facing decisions. Which operational responsibility remains with the team?

A) Evaluate output quality on representative data, protect inputs and outputs, and implement suitable handling for errors or unacceptable results.

B) Assume every prediction is correct because the service is managed.

C) Send production secrets as sample text to simplify troubleshooting.

D) Remove application access controls because AWS manages the model infrastructure.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Managed infrastructure does not establish that a model is appropriate for every business input. Application data handling, permissions, evaluation, and failure behavior remain part of the customer design.

**Why the other options are incorrect:**

- **B:** Managed hosting is not a guarantee of prediction correctness.
- **C:** Secrets should not be exposed in test inputs or logs.
- **D:** The customer still controls application access and data use.

**AWS references:** [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

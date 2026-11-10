# Guided Lab

## Objective

Evaluate a managed document-analysis capability on non-sensitive data.

## Services Used

Amazon Textract or a documentation-only service-selection review.

## Expected Cost Range

Textract API calls and storage can incur charges. Use one small synthetic supported document, check regional availability and pricing, and do not provision a training fleet for a pretrained extraction exercise.

## Step-by-Step Instructions

1. Prepare a synthetic document containing a short table and a few labeled fields, with no personal or confidential information.
2. Check the selected Textract operation input-format, size, and Region requirements in the official documentation.
3. If account permissions and the cost plan allow it, submit that document to the appropriate document-analysis operation using the console or an approved client.
4. Compare extracted fields, table cells, and confidence information with the known source document.
5. Record any incorrect or missing values and define when a real workflow would require validation or human review.
6. Explain how the task differs from Comprehend sentiment analysis, SageMaker AI custom training, and optional Bedrock generative-model access.

## Validation

- Results are compared with known ground truth rather than assumed correct.
- The record states whether an API call was executed or only documentation was reviewed.
- No fixed exam frequency is claimed for a service.

## Cleanup

1. Remove the synthetic input and output objects and optional lab-only logs.
2. Check that no training endpoint, notebook, or provisioned inference capacity was accidentally left running.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html), [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html), [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

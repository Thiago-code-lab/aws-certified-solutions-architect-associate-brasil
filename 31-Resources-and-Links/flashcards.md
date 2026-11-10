# Review Flashcards

## Card 01

**Question:** Two community study plans disagree about SAA-C03 domain weights. Which source should determine the official allocation?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The current AWS SAA-C03 exam guide. AWS defines the exam content domains and scored-content weights. Community question counts and promotional statements do not define the exam blueprint.

**AWS references:** [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html).

</details>

## Card 02

**Question:** A service appears in the current AWS in-scope list. Which conclusion is justified?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** It is within the published scope, but the list does not promise a fixed number of questions for that service. The guide describes scope and says the service list is non-exhaustive and subject to change. Exam coverage, deployment availability, and the correctness of a study explanation are separate questions.

**AWS references:** [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html), [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html), [AWS Snowball availability notice](https://aws.amazon.com/snowball/).

</details>

## Card 03

**Question:** A study note says that every RDS Multi-AZ deployment has no readable standbys. Which source most directly resolves the claim?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Current RDS documentation distinguishing Multi-AZ DB instance deployments from Multi-AZ DB cluster deployments. The deployment-specific documentation establishes the distinction: a DB instance standby does not serve reads, while Multi-AZ DB cluster readers can serve reads.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

</details>

## Card 04

**Question:** An older learning resource recommends Snowball for a new commercial-Region deployment. What is the responsible next step?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Check current AWS availability and lifecycle notices, then select an eligible transfer approach for the actual customer and date. Historical learning value does not guarantee present deployment availability. Current service notices must inform actual implementation decisions.

**AWS references:** [AWS Snowball availability notice](https://aws.amazon.com/snowball/), [Snowball availability history](https://docs.aws.amazon.com/snowball/latest/developer-guide/doc-history.html).

</details>

## Card 05

**Question:** A contributor finds a contradiction between a practice answer and AWS documentation. What makes the proposed correction reviewable?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Identify the exact question, define the scenario assumptions, cite applicable AWS documentation, and update the answer plus all affected explanations together. A defensible correction aligns the stem, alternatives, answer, and explanation under explicit assumptions. Traceable references and a question identifier let reviewers evaluate the change.

**AWS references:** [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html), [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

</details>

## Card 06

**Question:** A service appears in the current AWS in-scope list. Which conclusion is justified?

Why does this alternative fail: “Every exam form must contain exactly five questions about it.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The guide does not assign a fixed per-service question count.

**AWS references:** [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html), [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html), [AWS Snowball availability notice](https://aws.amazon.com/snowball/).

</details>

## Card 07

**Question:** A study note says that every RDS Multi-AZ deployment has no readable standbys. Which source most directly resolves the claim?

Why does this alternative fail: “An old summary that does not name the deployment type.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** A summary without the deployment scope repeats the ambiguity rather than resolving it.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

</details>

## Card 08

**Question:** An older learning resource recommends Snowball for a new commercial-Region deployment. What is the responsible next step?

Why does this alternative fail: “Assume the recommendation remains deployable because the PDF is downloadable.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Document availability does not establish service-order eligibility.

**AWS references:** [AWS Snowball availability notice](https://aws.amazon.com/snowball/), [Snowball availability history](https://docs.aws.amazon.com/snowball/latest/developer-guide/doc-history.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

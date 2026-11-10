# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 31-Q01 -->

Two community study plans disagree about SAA-C03 domain weights. Which source should determine the official allocation?

A) The number of questions in this repository mini practice blocks.

B) The highest-ranked unverified social media post.

C) An advertisement promising a particular pass result.

D) The current AWS SAA-C03 exam guide.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** AWS defines the exam content domains and scored-content weights. Community question counts and promotional statements do not define the exam blueprint.

**Why the other options are incorrect:**

- **A:** A practice set distribution is an editorial choice, not the exam definition.
- **B:** Popularity does not make a post an authoritative exam specification.
- **C:** A promotional promise is not the official blueprint.

**AWS references:** [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html).

</details>

## Question 2

<!-- question-id: 31-Q02 -->

A service appears in the current AWS in-scope list. Which conclusion is justified?

A) It is within the published scope, but the list does not promise a fixed number of questions for that service.

B) Every exam form must contain exactly five questions about it.

C) It must be available to every new AWS customer in every Region.

D) Its appearance guarantees every community claim about the service is correct.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** The guide describes scope and says the service list is non-exhaustive and subject to change. Exam coverage, deployment availability, and the correctness of a study explanation are separate questions.

**Why the other options are incorrect:**

- **B:** The guide does not assign a fixed per-service question count.
- **C:** Service lifecycle, regional availability, and customer eligibility still need checking.
- **D:** Community explanations require independent technical verification.

**AWS references:** [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html), [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html), [AWS Snowball availability notice](https://aws.amazon.com/snowball/).

</details>

## Question 3

<!-- question-id: 31-Q03 -->

A study note says that every RDS Multi-AZ deployment has no readable standbys. Which source most directly resolves the claim?

A) An old summary that does not name the deployment type.

B) A pricing badge for an unrelated course.

C) Current RDS documentation distinguishing Multi-AZ DB instance deployments from Multi-AZ DB cluster deployments.

D) An IAM policy describing S3 read permissions.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** The deployment-specific documentation establishes the distinction: a DB instance standby does not serve reads, while Multi-AZ DB cluster readers can serve reads.

**Why the other options are incorrect:**

- **A:** A summary without the deployment scope repeats the ambiguity rather than resolving it.
- **B:** Course promotion does not establish RDS replication behavior.
- **D:** S3 authorization documentation does not define RDS reader topology.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

</details>

## Question 4

<!-- question-id: 31-Q04 -->

An older learning resource recommends Snowball for a new commercial-Region deployment. What is the responsible next step?

A) Check current AWS availability and lifecycle notices, then select an eligible transfer approach for the actual customer and date.

B) Assume the recommendation remains deployable because the PDF is downloadable.

C) Assume an exam-scope entry overrides a service end-of-support announcement.

D) Order discontinued hardware without checking customer eligibility.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Historical learning value does not guarantee present deployment availability. Current service notices must inform actual implementation decisions.

**Why the other options are incorrect:**

- **B:** Document availability does not establish service-order eligibility.
- **C:** An exam list is not a service lifecycle contract.
- **D:** Eligibility and support must be checked before committing to an implementation.

**AWS references:** [AWS Snowball availability notice](https://aws.amazon.com/snowball/), [Snowball availability history](https://docs.aws.amazon.com/snowball/latest/developer-guide/doc-history.html).

</details>

## Question 5

<!-- question-id: 31-Q05 -->

A contributor finds a contradiction between a practice answer and AWS documentation. What makes the proposed correction reviewable?

A) Change only the answer letter without reviewing the options.

B) Identify the exact question, define the scenario assumptions, cite applicable AWS documentation, and update the answer plus all affected explanations together.

C) Keep a known wrong answer solely to preserve translation parity.

D) Delete the question report without correcting the learner-facing material.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** A defensible correction aligns the stem, alternatives, answer, and explanation under explicit assumptions. Traceable references and a question identifier let reviewers evaluate the change.

**Why the other options are incorrect:**

- **A:** A letter-only edit can leave the explanation and alternatives contradictory.
- **C:** Translation history does not justify teaching a known error.
- **D:** Removing the evidence does not resolve the educational defect.

**AWS references:** [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html), [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

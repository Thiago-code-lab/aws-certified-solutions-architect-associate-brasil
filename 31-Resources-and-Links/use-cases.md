# Use Cases

## Scenario 1: Primary exam reference

**Requirement:** Two community study plans disagree about SAA-C03 domain weights. Which source should determine the official allocation?

**Recommended design:** The current AWS SAA-C03 exam guide.

**Reason and boundary:** AWS defines the exam content domains and scored-content weights. Community question counts and promotional statements do not define the exam blueprint.

**Rejected alternative:** The number of questions in this repository mini practice blocks. A practice set distribution is an editorial choice, not the exam definition.

**AWS references:** [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html).

## Scenario 2: Exam scope is not a frequency guarantee

**Requirement:** A service appears in the current AWS in-scope list. Which conclusion is justified?

**Recommended design:** It is within the published scope, but the list does not promise a fixed number of questions for that service.

**Reason and boundary:** The guide describes scope and says the service list is non-exhaustive and subject to change. Exam coverage, deployment availability, and the correctness of a study explanation are separate questions.

**Rejected alternative:** Every exam form must contain exactly five questions about it. The guide does not assign a fixed per-service question count.

**AWS references:** [SAA-C03 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html), [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html), [AWS Snowball availability notice](https://aws.amazon.com/snowball/).

## Scenario 3: Service-specific documentation

**Requirement:** A study note says that every RDS Multi-AZ deployment has no readable standbys. Which source most directly resolves the claim?

**Recommended design:** Current RDS documentation distinguishing Multi-AZ DB instance deployments from Multi-AZ DB cluster deployments.

**Reason and boundary:** The deployment-specific documentation establishes the distinction: a DB instance standby does not serve reads, while Multi-AZ DB cluster readers can serve reads.

**Rejected alternative:** An old summary that does not name the deployment type. A summary without the deployment scope repeats the ambiguity rather than resolving it.

**AWS references:** [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

## Scenario 4: Verify live service availability

**Requirement:** An older learning resource recommends Snowball for a new commercial-Region deployment. What is the responsible next step?

**Recommended design:** Check current AWS availability and lifecycle notices, then select an eligible transfer approach for the actual customer and date.

**Reason and boundary:** Historical learning value does not guarantee present deployment availability. Current service notices must inform actual implementation decisions.

**Rejected alternative:** Assume the recommendation remains deployable because the PDF is downloadable. Document availability does not establish service-order eligibility.

**AWS references:** [AWS Snowball availability notice](https://aws.amazon.com/snowball/), [Snowball availability history](https://docs.aws.amazon.com/snowball/latest/developer-guide/doc-history.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

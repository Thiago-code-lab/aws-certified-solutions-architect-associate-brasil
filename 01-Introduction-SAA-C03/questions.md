# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 01-Q01 -->

Which allocation matches the official SAA-C03 scored-content domains?

A) Security 30%, Resilience 26%, Performance 24%, Cost Optimization 20%.

B) Security 24%, Resilience 30%, Performance 28%, Cost Optimization 18%.

C) Each of the four domains has a fixed weight of 25%.

D) Security 20%, Resilience 24%, Performance 26%, Cost Optimization 30%.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** The exam guide assigns these four weights to scored content. A community practice set need not have the same distribution.

**Why the other options are incorrect:**

- **B:** These were the incorrect weights inherited from the source edition.
- **C:** Equal practice blocks do not imply equally weighted exam domains.
- **D:** These numbers assign the official weights to the wrong domains.

**AWS references:** [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html).

</details>

## Question 2

<!-- question-id: 01-Q02 -->

A team runs its application on EC2 instances. Under the shared responsibility model, who patches the guest operating system?

A) AWS patches the customer guest OS automatically in every EC2 deployment.

B) The customer operating the EC2 instances.

C) The internet service provider.

D) The domain registrar.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** For EC2, AWS manages the underlying infrastructure; the customer manages the guest OS, applications, and their configuration. Automation can help the customer perform that responsibility.

**Why the other options are incorrect:**

- **A:** EC2 does not transfer all guest OS maintenance to AWS.
- **C:** Network connectivity providers do not manage the EC2 guest OS.
- **D:** Domain registration does not include server patch management.

**AWS references:** [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

</details>

## Question 3

<!-- question-id: 01-Q03 -->

A workload must recover a document that a user accidentally overwrote yesterday. Which capability directly addresses that requirement?

A) Put two web servers behind a load balancer without versioning the data.

B) Increase the CPU of the web server.

C) Retain previous object versions and test how to restore the required version.

D) Add a second DNS record pointing to the same server.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** S3 Versioning retains earlier versions so an overwrite can be reversed. Redundant compute and DNS do not retain earlier application data.

**Why the other options are incorrect:**

- **A:** Compute redundancy alone does not preserve historical object contents.
- **B:** CPU capacity does not undo an overwrite.
- **D:** Another DNS record does not create an independent historical copy.

**AWS references:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

</details>

## Question 4

<!-- question-id: 01-Q04 -->

A business can tolerate losing at most 15 minutes of data and needs service restored within 2 hours. Which objectives express these requirements?

A) RPO of 15 minutes and RTO of 2 hours.

B) RTO of 15 minutes and RPO of 2 hours.

C) Availability of 15 minutes and durability of 2 hours.

D) A recovery objective is unnecessary when a database is managed.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** RPO limits acceptable data loss measured in time; RTO limits acceptable recovery time. Managed services do not remove the need to define or test those objectives.

**Why the other options are incorrect:**

- **B:** This reverses the meanings of RPO and RTO.
- **C:** Availability and durability are not names for these recovery-time limits.
- **D:** The business must still define recovery objectives for managed workloads.

**AWS references:** [Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html).

</details>

## Question 5

<!-- question-id: 01-Q05 -->

A design requires AWS API access from an EC2 application without distributing long-lived access keys. Which proposal satisfies the security requirement?

A) Store an administrator access key in the machine image.

B) Attach an appropriately scoped IAM role to the instance through an instance profile.

C) Put the root access key in a source repository.

D) Remove authentication so the application has no credential to manage.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** An EC2 workload can obtain temporary credentials from its IAM role. Permissions should cover only the application actions and resources it needs.

**Why the other options are incorrect:**

- **A:** A baked-in administrator key is long-lived and excessively privileged.
- **C:** Root credentials must not be distributed or committed.
- **D:** Removing authentication does not provide authorized AWS API access.

**AWS references:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

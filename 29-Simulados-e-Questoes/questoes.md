# Review Questions

## Question 1

A web application must remain available if an Availability Zone fails. Traffic must be distributed automatically among healthy instances. Which approach best meets these requirements?

A) A single EC2 instance with daily snapshot.
B) Auto Scaling Group in multiple AZs behind an Application Load Balancer.
C) A larger EC2 instance on a public subnet.
D) Manual backup of the AMI before each deployment.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:**
A multi-AZ Auto Scaling group behind an ALB distributes traffic to healthy targets and maintains capacity even if an Availability Zone fails.

**Why option A is wrong:**
Snapshot helps recovery, but does not deliver high availability during failure.

</details>

## Question 2

A company wants to reduce the cost of accessing S3 from private workloads in a VPC, without exposing traffic to the internet. Which choice is best?

A) NAT Gateway for all access to S3.
B) Internet Gateway associated with the private subnet.
C) VPC Gateway Endpoint for S3.
D) Elastic IP on each private instance.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:**
Gateway Endpoint for S3 maintains traffic on the AWS network and reduces dependence on NAT Gateway for this access.

**Why option A is wrong:**
Works for egress, but adds cost and is not the most straightforward option for private S3.

</details>

## Question 3

A relational database needs automatic failover with minimal disruption. Read scaling is not the primary goal. Which feature best meets this requirement?

A) RDS Multi-AZ.
B) Read Replica in another region.
C) Export to S3 every hour.
D) EC2 with a manually installed database.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:**
RDS Multi-AZ provides high availability with managed failover for the primary database.

**Why option B is wrong:**
A read replica supports read workloads and DR, but does not replace Multi-AZ for managed failover with synchronous replication in the same scope.

</details>

## Question 4

An API receives unpredictable spikes and needs to decouple producers and consumers, accepting asynchronous processing. Which service best reduces operational risk?

A) Amazon SQS.
B) Amazon EFS.
C) AWS WAF.
D) AWS Direct Connect.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:**
SQS absorbs spikes, decouples components and allows asynchronous processing by consumers at different rates.

**Why option B is wrong:**
EFS is shared file storage, not a decoupling queue.

</details>

## Question 5

During final review, a learner answers IAM questions incorrectly by choosing overly broad permissions. Which practice best addresses this pattern?

A) Use managed policies with full permissions to avoid access restrictions.
B) Review least privilege, scope of resources, and conditions in policies.
C) Ignore IAM and focus only on networks.
D) Memorize service names without analyzing allowed actions.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:**
SAA-C03 security questions often test least privilege, correct resource scoping, and explicit access control.

**Why option A is wrong:**
Broad permissions increase risk and usually conflict with the exam's security requirements.

</details>

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Mini Practice Exams by Domain

## How to Use This Material

- 4 blocks of 5 questions (20 in total).
- Target time: 8 to 10 minutes per block.
- Check answers immediately and record mistakes in your error log.

## Block A: Resilience

1. A scenario requires automatic failover between Availability Zones with minimal downtime.
A) A single larger instance. B) Multi-AZ with monitoring and native failover. C) Manual weekly backups. D) Vertical scaling only.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Multi-AZ handles an Availability Zone failure with automatic failover and less downtime.

</details>

2. An application with unpredictable traffic spikes must absorb load without losing requests.
A) Decoupled queue + elastic consumers. B) Fixed synchronous processing. C) Manual retry on the client. D) Block extra requests.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** A queue protects the producer and lets consumers scale with the backlog.

</details>

3. DR requirement with low RPO and moderate cost.
A) Annual backup. B) Pilot light. C) No replication. D) Local snapshots only.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Pilot light balances cost with faster recovery than a backup-only strategy.

</details>

4. High availability for a transactional relational database.
A) A read replica only. B) Multi-AZ. C) A local cache. D) A Spot Instance.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Multi-AZ prioritizes write continuity with managed failover.

</details>

5. Global distribution of static content with low latency.
A) CloudFront. B) EC2 single region. C) NAT Gateway. D) SQS.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** CloudFront serves content at edge locations, reducing latency caused by distance.

</details>

## Block B: Performance

6. Heavy, repeated reads of frequently accessed session data.
A) Managed cache. B) Daily snapshot. C) Manual logging. D) ASG without cache.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** An in-memory cache reduces latency and database load.

</details>

7. An API with variable throughput and low operational overhead.
A) Serverless with automatic scaling. B) Fixed EC2 capacity. C) A cron process. D) A monolith without a load balancer.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Serverless adjusts capacity on demand without server management.

</details>

8. DynamoDB with irregular read demand and spikes.
A) On-demand capacity mode. B) Static provisioned capacity without auto scaling. C) A local database. D) A CSV spreadsheet.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** On-demand capacity handles usage variation and avoids throttling caused by underprovisioning.

</details>

9. Analytical query on data in S3 without dedicated cluster.
A) Athena. B) NAT Gateway. C) IAM Identity Center. D) Route 53.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Athena runs SQL directly on S3 with no infrastructure to manage.

</details>

10. Private connectivity to an AWS service without using the public internet.
A) VPC Endpoint. B) Public NAT. C) Mandatory Bastion. D) On-prem VPN for everything.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** A private endpoint avoids the public internet and reduces the attack surface.

</details>

## Block C: Security

11. Application credential with automatic rotation.
A) Secrets Manager. B) Text file in EC2. C) Fixed variable in pipeline. D) KMS alone.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Secrets Manager manages secret storage, access and rotation.

</details>

12. Least privilege in IAM means:
A) A broad policy for simplicity. B) The minimum permissions needed for each function. C) The same role for everything. D) No logs.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Least privilege reduces the impact of compromised credentials.

</details>

13. Need for audit trail of API calls.
A) CloudTrail. B) CloudFront. C) EFS. D) Snowball.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** CloudTrail logs API calls for investigation and compliance.

</details>

14. Encryption at rest with a key under your control.
A) KMS with a CMK. B) SG inbound rules. C) An ASG policy. D) An IAM group.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** KMS with CMK offers key governance and usage auditing.

</details>

15. Segment traffic between application tiers in a VPC.
A) Security groups and NACLs by function. B) Everything in a public subnet. C) Open access from 0.0.0.0/0. D) A single broadly permissive SG.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Segmentation by application tier reduces the blast radius and the risk of lateral movement.

</details>

## Block D: Cost

16. Rarely accessed data, long retention.
A) An appropriate archival storage class. B) Standard for everything. C) EBS io2 for cold backups. D) Replicate unnecessarily.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Glacier/Archive reduces costs when data is accessed infrequently.

</details>

17. A predictable EC2 workload running 24x7.
A) A usage commitment (Savings Plans/RI). B) Spot for a single critical database. C) On-Demand without analysis. D) Daily manual scaling.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Steady usage usually benefits from commitment-based discounts.

</details>

18. Short, occasional Lambda executions to reduce operational costs.
A) A good fit for serverless. B) A permanently running ECS service is mandatory. C) A fixed dedicated cluster. D) Use a database as a queue.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Paying per invocation avoids fixed costs for idle capacity when workloads run occasionally.

</details>

19. Avoid unnecessary data transfer costs when accessing AWS services internally.
A) Private endpoints when applicable. B) NAT for everything. C) Manual tunnel. D) public S3.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** A private endpoint removes an unnecessary hop through the internet or a NAT gateway.

</details>

20. Continuous cost review process.
A) Budgets + alerts + monthly review. B) See invoice only at the end of the year. C) Ignore tags. D) No ownership.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:** Cost governance requires proactive monitoring and accountability.

</details>

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

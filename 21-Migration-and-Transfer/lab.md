# Guided Lab

## Objective

Build a migration decision and cutover plan without assuming retired services are available.

## Services Used

AWS DMS, AWS Transform MGN, DataSync, Transfer Family, and current availability notices.

## Expected Cost Range

Planning exercise. Do not deploy migration replication instances, agents, endpoints, or hardware orders merely to compare service responsibilities.

## Step-by-Step Instructions

1. Inventory one sample server, relational database, NFS dataset, and partner SFTP workflow using non-sensitive descriptions.
2. Map server rehosting to MGN, database migration/conversion to the appropriate DMS/SCT capabilities, supported online file copies to DataSync, and partner protocol endpoints to Transfer Family.
3. For the database, record source/target support, schema-conversion gaps, CDC prerequisites, validation, and a cutover/rollback plan.
4. For file transfer, record source protocol, bandwidth, integrity checks, authentication, and destination permissions.
5. Check Snowball new-customer eligibility and announced commercial-Region end of support. Treat historical exam examples separately from deployable new-customer recommendations.
6. Write a test-launch or sample-data validation procedure for the selected migration before considering any live cutover.

## Validation

- Each migration requirement is mapped to the correct service responsibility.
- Eligibility and lifecycle dates are checked explicitly.
- The plan does not claim that copying data automatically converts every application dependency.

## Cleanup

1. Keep the assessment and rollback plan.
2. No migration infrastructure was required; if any optional resources were created separately, inventory and remove them under their own cleanup plan.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html), [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html), [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html), [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html), [AWS Snowball availability notice](https://aws.amazon.com/snowball/), [Snowball availability history](https://docs.aws.amazon.com/snowball/latest/developer-guide/doc-history.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

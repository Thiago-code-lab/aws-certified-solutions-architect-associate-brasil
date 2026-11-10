# Guided Lab

## Objective

Observe DynamoDB base-table access and review capacity and consistency settings.

## Services Used

DynamoDB and its console item explorer.

## Expected Cost Range

Table storage and read/write requests can incur charges. Use tiny synthetic items and a small bounded number of operations; do not assume on-demand mode is free or limitless.

## Step-by-Step Instructions

1. Create a lab table in on-demand mode with a string partition key named orderId.
2. Insert a few small synthetic orders with distinct orderId values.
3. Read an item by its full primary key and inspect how an API GetItem request can request ConsistentRead.
4. Compare a key-based lookup with the work needed by a broad Scan as the dataset grows; do not generate a large load merely to demonstrate the distinction.
5. Review GSI read-consistency limitations and the documented MREC/MRSC global-table modes without creating unnecessary replicas.
6. Record why key distribution, quotas, and capacity-mode behavior still matter in on-demand mode.

## Validation

- Synthetic items can be retrieved by their primary key.
- Strong consistency is not claimed for GSI reads.
- The notes separate capacity mode from consistency mode and key design.

## Cleanup

1. Delete the lab table after removing any optional test backups or exports that are no longer required.
2. Confirm no replica table or extra billable resource was created unintentionally.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html), [DynamoDB capacity modes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html), [DynamoDB partition key design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

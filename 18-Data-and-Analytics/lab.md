# Guided Lab

## Objective

Compare Athena scanning for an unpartitioned and a query-aware dataset.

## Services Used

S3, Athena, and Glue Data Catalog.

## Expected Cost Range

S3 storage/requests, Athena scanning or capacity, and optional Glue jobs/crawlers can incur charges. Set a workgroup query-scan limit and use a small synthetic dataset.

## Step-by-Step Instructions

1. Create a private lab bucket with separate raw, curated, and query-results prefixes.
2. Upload a small synthetic tabular dataset containing an event date and several data columns.
3. Register the raw table in the Glue Data Catalog using a schema matching the actual uploaded files.
4. Use a bounded Athena transformation such as CTAS to write a Parquet copy to a distinct empty curated location with a sensible date partition, reviewing the official CTAS requirements first.
5. Query the same selected columns and matching date range in both datasets; inspect bytes scanned and results.
6. Check that partition pruning actually applies and avoid concluding that every small-file or high-cardinality partition layout is faster.

## Validation

- Both queries return equivalent intended results.
- Scanning metrics are recorded, not replaced by a universal savings claim.
- Catalog registration is distinguished from the transformation that wrote the curated files.

## Cleanup

1. Drop the lab catalog tables and database if exclusively used by the lab.
2. Remove raw, curated, and query-result objects and their versions as appropriate.
3. Delete any optional crawler or ETL job resources and inspect storage left behind.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [Athena data optimization](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html), [AWS Glue components](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Guided Lab

## Objective

Compare cost evidence, pricing commitments, and permissions guardrails.

## Services Used

Cost Explorer, AWS Budgets, Savings Plans documentation, and SCP documentation.

## Expected Cost Range

Read-only planning exercise; account permissions and available cost history may vary. Do not purchase a Savings Plan or create paid workloads for this exercise.

## Step-by-Step Instructions

1. Inspect available cost history by service and account, using existing authorized data or a synthetic cost worksheet.
2. Identify a stable eligible compute baseline separately from uncertain bursts, and estimate the risk of underutilized commitment.
3. Draft budget notification thresholds and assign an owner for review; document delayed cost reporting and the limits of configured actions.
4. Draft an account and OU structure separating experiments from production.
5. Review an example SCP as a permissions ceiling and record why it neither grants permissions nor restricts management-account roles.
6. Write one measurable optimization hypothesis and its validation metric before changing any workload.

## Validation

- A cost notification is not called a guaranteed spending cap.
- No pricing commitment is purchased as a learning side effect.
- SCPs, IAM grants, and billing analysis have distinct roles.

## Cleanup

1. Remove optional lab-only budget subscriptions if created.
2. Keep the cost assessment; do not remove shared cost reporting or organization guardrails.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html), [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html), [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html), [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

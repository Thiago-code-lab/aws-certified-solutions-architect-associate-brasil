# Guided Lab

## Objective

Observe explicit-deny precedence and distinguish an allow from a permissions ceiling.

## Services Used

IAM policy simulation and AWS Organizations documentation.

## Expected Cost Range

Policy and documentation exercise. Do not attach experimental SCPs to a production organization.

## Step-by-Step Instructions

1. Start with the narrow object-read allow designed in module 02.
2. Add an explicit deny for one of the allowed test object resources in the simulated policy set.
3. Simulate that same request and compare its result with an allowed object that the deny does not match.
4. Read the SCP documentation and draw the intersection between applicable organization guardrails and an IAM grant.
5. Record the management-account exception and explain why an SCP allow does not grant access to a new role.

## Validation

- The applicable explicit deny wins over the allow.
- A nonmatching deny is not treated as a global denial.
- The notes distinguish identity grants, explicit denies, and organization ceilings.

## Cleanup

1. Discard the experimental simulated policy set.
2. Remove only draft lab policies; no live organization policy needs modification.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html), [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

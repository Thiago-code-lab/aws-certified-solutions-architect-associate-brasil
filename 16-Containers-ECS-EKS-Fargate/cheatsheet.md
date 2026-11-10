# Quick Guide

## Decision Table

| Requirement or distinction | Appropriate choice | Limitation to remember |
|---|---|---|
| Container compute without EC2 hosts | AWS Fargate for the ECS tasks. | Fargate supplies managed container compute. The team still configures task resources, images, permissions, networking, and service scaling. |
| Task role versus execution role | The ECS task IAM role. | The task role supplies permissions to code running in containers. The task execution role serves agent operations such as pulling images and shipping configured logs. |
| Image pulls and log delivery | The task execution IAM role with the necessary permissions. | The execution role authorizes supported ECS/Fargate agent operations. Application API permissions remain separate in the task role. |
| Kubernetes orchestration | Amazon EKS. | EKS provides a managed Kubernetes control plane. Compute, access, add-ons, networking, and workload configuration still need an appropriate operating model. |
| Fargate does not choose task demand | Configure an appropriate ECS service scaling policy and limits; Fargate alone does not choose the service desired count from application demand. | Fargate manages the underlying task compute. Application Auto Scaling policies determine desired-count changes for an ECS service, subject to configured limits and available capacity. |

## Service Selection Cues

A service name is not an architectural requirement. Verify the deployment type, consistency or retry model, failure scope, quotas, permissions, and cost dimensions that apply to the proposed configuration.

## When to Use This Module During Review

Use this table before practice questions and after a wrong answer. Explain why the rejected alternatives fail the stated constraints; do not memorize a letter or assume the longest option is correct.

## Recurring Pitfalls

- **Container compute without EC2 hosts:** Self-managed EC2 hosts retain host-management responsibilities.
- **Task role versus execution role:** Execution-role permissions are for the ECS/Fargate agents and are not the application task credentials.
- **Image pulls and log delivery:** Task-role application permissions do not replace execution-role permissions for these operations.
- **Kubernetes orchestration:** ECS is a different orchestration API and does not fulfill a Kubernetes API requirement.
- **Fargate does not choose task demand:** Managed hosts and application service scaling are separate concerns.

## AWS References

[Fargate for ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html), [ECS task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html), [ECS task IAM roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html), [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), [ECS service auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

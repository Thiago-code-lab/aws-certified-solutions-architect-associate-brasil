# Containers: ECS, EKS, and Fargate

## Overview

Choose container orchestration and compute independently. ECS, EKS, Fargate, and ECR are not interchangeable, and application permissions differ from the permissions used by a container agent.

## Key Concepts

- **Container compute without EC2 hosts:** Fargate supplies managed container compute. The team still configures task resources, images, permissions, networking, and service scaling.
- **Task role versus execution role:** The task role supplies permissions to code running in containers. The task execution role serves agent operations such as pulling images and shipping configured logs.
- **Image pulls and log delivery:** The execution role authorizes supported ECS/Fargate agent operations. Application API permissions remain separate in the task role.
- **Kubernetes orchestration:** EKS provides a managed Kubernetes control plane. Compute, access, add-ons, networking, and workload configuration still need an appropriate operating model.
- **Fargate does not choose task demand:** Fargate manages the underlying task compute. Application Auto Scaling policies determine desired-count changes for an ECS service, subject to configured limits and available capacity.

**Availability note:** App Runner is closed to new customers; existing customers can continue using it. For a new container application, evaluate currently available ECS deployment options against the workload requirements. See the [AWS availability notice](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

## Exam Relevance

Use the scenario requirements to select an answer. The official scored-content weights are Security 30%, Resilience 26%, Performance 24%, and Cost Optimization 20%. These weights apply to exam domains, not to an individual module or service.

## Practical Cues

1. **Container compute without EC2 hosts:** AWS Fargate for the ECS tasks.
2. **Task role versus execution role:** The ECS task IAM role.
3. **Image pulls and log delivery:** The task execution IAM role with the necessary permissions.
4. **Kubernetes orchestration:** Amazon EKS.
5. **Fargate does not choose task demand:** Configure an appropriate ECS service scaling policy and limits; Fargate alone does not choose the service desired count from application demand.

## Common Pitfalls

- Self-managed EC2 hosts retain host-management responsibilities.
- Execution-role permissions are for the ECS/Fargate agents and are not the application task credentials.
- Task-role application permissions do not replace execution-role permissions for these operations.

## Next Review Steps

1. Review [cheatsheet.md](./cheatsheet.md) and explain the assumptions behind each choice.
2. Answer [questions.md](./questions.md) before revealing the explanations.
3. Use [flashcards.md](./flashcards.md) for spaced retrieval and record recurring mistakes.

## Additional Study

[Fargate for ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html), [ECS task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html), [ECS task IAM roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html), [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), [ECS service auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html).

Related community paths: [Cloud Practitioner](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil) and [AI Practitioner](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil). These external repositories may contain Portuguese material.

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To reinforce architecture concepts through real data projects on AWS, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

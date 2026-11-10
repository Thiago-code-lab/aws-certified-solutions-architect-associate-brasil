# Review Flashcards

## Card 01

**Question:** A team chooses ECS for long-running containers and does not want to provision or patch EC2 worker hosts. Which compute option fits?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** AWS Fargate for the ECS tasks. Fargate supplies managed container compute. The team still configures task resources, images, permissions, networking, and service scaling.

**AWS references:** [Fargate for ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html), [ECS task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html).

</details>

## Card 02

**Question:** Application code inside an ECS task calls S3. Which role should carry the application S3 permissions?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The ECS task IAM role. The task role supplies permissions to code running in containers. The task execution role serves agent operations such as pulling images and shipping configured logs.

**AWS references:** [ECS task IAM roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html), [ECS task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html).

</details>

## Card 03

**Question:** A Fargate task needs its agent to pull a private ECR image and send logs with the awslogs driver. Which role is relevant to those agent operations?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** The task execution IAM role with the necessary permissions. The execution role authorizes supported ECS/Fargate agent operations. Application API permissions remain separate in the task role.

**AWS references:** [ECS task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html), [ECS task IAM roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html).

</details>

## Card 04

**Question:** A workload explicitly requires Kubernetes APIs and Kubernetes-native controllers. Which AWS managed orchestration service matches that requirement?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Amazon EKS. EKS provides a managed Kubernetes control plane. Compute, access, add-ons, networking, and workload configuration still need an appropriate operating model.

**AWS references:** [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), [Fargate for ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html).

</details>

## Card 05

**Question:** An ECS service on Fargate must increase its desired task count as load rises. What is still required?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Configure an appropriate ECS service scaling policy and limits; Fargate alone does not choose the service desired count from application demand. Fargate manages the underlying task compute. Application Auto Scaling policies determine desired-count changes for an ECS service, subject to configured limits and available capacity.

**AWS references:** [Fargate for ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html), [ECS service auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html).

</details>

## Card 06

**Question:** Application code inside an ECS task calls S3. Which role should carry the application S3 permissions?

Why does this alternative fail: “Only the task execution role, assuming its credentials are application credentials.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Execution-role permissions are for the ECS/Fargate agents and are not the application task credentials.

**AWS references:** [ECS task IAM roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html), [ECS task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html).

</details>

## Card 07

**Question:** A Fargate task needs its agent to pull a private ECR image and send logs with the awslogs driver. Which role is relevant to those agent operations?

Why does this alternative fail: “The application task role as the only role needed for agent image pulls.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** Task-role application permissions do not replace execution-role permissions for these operations.

**AWS references:** [ECS task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html), [ECS task IAM roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html).

</details>

## Card 08

**Question:** A workload explicitly requires Kubernetes APIs and Kubernetes-native controllers. Which AWS managed orchestration service matches that requirement?

Why does this alternative fail: “Amazon ECS solely because it also runs containers.”?

<details>
<summary><strong>View answer</strong></summary>

**Answer:** ECS is a different orchestration API and does not fulfill a Kubernetes API requirement.

**AWS references:** [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), [Fargate for ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

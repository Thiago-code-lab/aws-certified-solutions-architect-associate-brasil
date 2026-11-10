# Use Cases

## Scenario 1: Container compute without EC2 hosts

**Requirement:** A team chooses ECS for long-running containers and does not want to provision or patch EC2 worker hosts. Which compute option fits?

**Recommended design:** AWS Fargate for the ECS tasks.

**Reason and boundary:** Fargate supplies managed container compute. The team still configures task resources, images, permissions, networking, and service scaling.

**Rejected alternative:** ECS on self-managed EC2 hosts with no host maintenance process. Self-managed EC2 hosts retain host-management responsibilities.

**AWS references:** [Fargate for ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html), [ECS task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html).

## Scenario 2: Task role versus execution role

**Requirement:** Application code inside an ECS task calls S3. Which role should carry the application S3 permissions?

**Recommended design:** The ECS task IAM role.

**Reason and boundary:** The task role supplies permissions to code running in containers. The task execution role serves agent operations such as pulling images and shipping configured logs.

**Rejected alternative:** Only the task execution role, assuming its credentials are application credentials. Execution-role permissions are for the ECS/Fargate agents and are not the application task credentials.

**AWS references:** [ECS task IAM roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html), [ECS task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html).

## Scenario 3: Image pulls and log delivery

**Requirement:** A Fargate task needs its agent to pull a private ECR image and send logs with the awslogs driver. Which role is relevant to those agent operations?

**Recommended design:** The task execution IAM role with the necessary permissions.

**Reason and boundary:** The execution role authorizes supported ECS/Fargate agent operations. Application API permissions remain separate in the task role.

**Rejected alternative:** The application task role as the only role needed for agent image pulls. Task-role application permissions do not replace execution-role permissions for these operations.

**AWS references:** [ECS task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html), [ECS task IAM roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html).

## Scenario 4: Kubernetes orchestration

**Requirement:** A workload explicitly requires Kubernetes APIs and Kubernetes-native controllers. Which AWS managed orchestration service matches that requirement?

**Recommended design:** Amazon EKS.

**Reason and boundary:** EKS provides a managed Kubernetes control plane. Compute, access, add-ons, networking, and workload configuration still need an appropriate operating model.

**Rejected alternative:** Amazon ECS solely because it also runs containers. ECS is a different orchestration API and does not fulfill a Kubernetes API requirement.

**AWS references:** [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), [Fargate for ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

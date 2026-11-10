# Review Questions

Choose one answer for each question. These original practice items are not AWS exam questions.

## Question 1

<!-- question-id: 16-Q01 -->

A team chooses ECS for long-running containers and does not want to provision or patch EC2 worker hosts. Which compute option fits?

A) ECS on self-managed EC2 hosts with no host maintenance process.

B) AWS Fargate for the ECS tasks.

C) An ECR repository by itself as running compute.

D) A task IAM role by itself as a container host.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** Fargate supplies managed container compute. The team still configures task resources, images, permissions, networking, and service scaling.

**Why the other options are incorrect:**

- **A:** Self-managed EC2 hosts retain host-management responsibilities.
- **C:** ECR stores images rather than executing application containers.
- **D:** An IAM role grants permissions and does not supply compute.

**AWS references:** [Fargate for ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html), [ECS task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html).

</details>

## Question 2

<!-- question-id: 16-Q02 -->

Application code inside an ECS task calls S3. Which role should carry the application S3 permissions?

A) Only the task execution role, assuming its credentials are application credentials.

B) A root access key built into the container image.

C) The ALB service-linked role.

D) The ECS task IAM role.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** D

**Explanation:** The task role supplies permissions to code running in containers. The task execution role serves agent operations such as pulling images and shipping configured logs.

**Why the other options are incorrect:**

- **A:** Execution-role permissions are for the ECS/Fargate agents and are not the application task credentials.
- **B:** Embedded root keys are unsafe and unnecessary.
- **C:** Load balancer service permissions do not authorize application S3 calls.

**AWS references:** [ECS task IAM roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html), [ECS task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html).

</details>

## Question 3

<!-- question-id: 16-Q03 -->

A Fargate task needs its agent to pull a private ECR image and send logs with the awslogs driver. Which role is relevant to those agent operations?

A) The application task role as the only role needed for agent image pulls.

B) The task execution IAM role with the necessary permissions.

C) An IAM user password pasted into the Dockerfile.

D) A Route 53 hosted zone.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:** The execution role authorizes supported ECS/Fargate agent operations. Application API permissions remain separate in the task role.

**Why the other options are incorrect:**

- **A:** Task-role application permissions do not replace execution-role permissions for these operations.
- **C:** A baked-in user password is not the supported execution-role design.
- **D:** DNS zones cannot authorize ECR pulls or log delivery.

**AWS references:** [ECS task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html), [ECS task IAM roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html).

</details>

## Question 4

<!-- question-id: 16-Q04 -->

A workload explicitly requires Kubernetes APIs and Kubernetes-native controllers. Which AWS managed orchestration service matches that requirement?

A) Amazon ECS solely because it also runs containers.

B) Amazon ECR as a Kubernetes control plane.

C) Amazon EKS.

D) An SQS FIFO queue.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** EKS provides a managed Kubernetes control plane. Compute, access, add-ons, networking, and workload configuration still need an appropriate operating model.

**Why the other options are incorrect:**

- **A:** ECS is a different orchestration API and does not fulfill a Kubernetes API requirement.
- **B:** ECR is an image registry, not a Kubernetes control plane.
- **D:** A message queue does not provide container orchestration.

**AWS references:** [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), [Fargate for ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html).

</details>

## Question 5

<!-- question-id: 16-Q05 -->

An ECS service on Fargate must increase its desired task count as load rises. What is still required?

A) Assume every Fargate service automatically increases its desired count with traffic without a scaling configuration.

B) Increase the ECR repository storage quota to scale running tasks.

C) Configure an appropriate ECS service scaling policy and limits; Fargate alone does not choose the service desired count from application demand.

D) Add administrator keys to every task.

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** C

**Explanation:** Fargate manages the underlying task compute. Application Auto Scaling policies determine desired-count changes for an ECS service, subject to configured limits and available capacity.

**Why the other options are incorrect:**

- **A:** Managed hosts and application service scaling are separate concerns.
- **B:** Registry storage capacity is not running service desired count.
- **D:** Broader credentials do not implement a scaling policy.

**AWS references:** [Fargate for ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html), [ECS service auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html).

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect AWS architecture with ingestion, processing, and analytics, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

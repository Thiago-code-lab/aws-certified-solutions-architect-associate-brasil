# Guided Lab

## Objective

Observe replacement of a lab web instance behind a multi-AZ load balancer.

## Services Used

EC2 Auto Scaling, ALB, target groups, and EC2.

## Expected Cost Range

ALB runtime, EC2 instances, EBS, and public IPv4 use are billable as applicable. Use a short planned test window and do not buy a pricing commitment for this lab.

## Step-by-Step Instructions

1. Create dedicated lab networking across two AZs with the outbound access required for package installation. Allow HTTP to application instances only from the ALB security group.
2. Create an Amazon Linux 2023 launch template and use the complete user-data script below to install a minimal HTTP target.
3. Create an HTTP target group with the /health health-check path and an ALB spanning the two AZs. Limit viewer access to the intended lab client network.
4. Create an Auto Scaling group across those AZs with desired capacity two and attach the target group. Enable ELB health checks and choose a grace period that covers installation.
5. Wait for two healthy targets and request the ALB endpoint from the allowed client.
6. Mark one lab group instance unhealthy using the Auto Scaling controls; observe replacement events and target-health recovery. Do not remove the last healthy target deliberately.
7. Record capacity during replacement and explain why two instances alone do not guarantee every workload availability target.

### Web Target User Data

```bash
#!/bin/bash
set -euo pipefail
dnf install -y httpd
printf 'healthy\n' > /var/www/html/health
printf 'SAA-C03 lab\n' > /var/www/html/index.html
systemctl enable --now httpd
```

## Validation

- The ALB has healthy targets in the planned AZs before the experiment.
- The group launches a replacement and the target group returns to the planned healthy capacity.
- The test demonstrates controlled instance replacement, not a real AWS AZ outage.

## Cleanup

1. Delete the Auto Scaling group and terminate its remaining lab instances.
2. Delete the lab ALB, target group, launch template, and unused lab network resources.
3. Check remaining volumes and public addresses; review delayed charges.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [EC2 Auto Scaling health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html), [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this topic to data scenarios, lakehouse architectures, and hands-on projects, explore: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

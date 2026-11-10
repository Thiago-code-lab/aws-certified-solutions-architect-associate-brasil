# Use Cases

## Scenario 1: Survive loss of a web AZ

**Requirement:** A web tier runs in one AZ, while its database already has suitable Multi-AZ protection. The business requires the web tier to survive an AZ outage. Which change addresses the missing protection?

**Recommended design:** Deploy replaceable web instances across multiple AZs behind a multi-AZ ALB and keep required state outside individual instances.

**Reason and boundary:** The unprotected component is the web tier. Database redundancy does not make single-AZ application compute available during that AZ failure.

**Rejected alternative:** Add a read replica but leave every web instance in one AZ. Additional database readers do not remove the web tier AZ dependency.

**AWS references:** [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Disaster recovery strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [RDS Multi-AZ deployment types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

## Scenario 2: Independent order subscribers

**Requirement:** Inventory and invoicing must each receive every accepted order, even if one subsystem is temporarily unavailable. Which design isolates their processing backlogs?

**Recommended design:** Publish to SNS and subscribe a separate SQS queue for each subsystem, with retry-safe consumers.

**Reason and boundary:** Separate subscribed queues provide independent buffering. Successful publication, correct subscription policies, retry behavior, and idempotent consumers are necessary parts of the design.

**Rejected alternative:** Use one SQS queue and assume both competing consumers always receive every message. One competing-consumer queue distributes work rather than independently copying every event to each subsystem.

**AWS references:** [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html), [SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).

## Scenario 3: Private origin for a public CDN

**Requirement:** Customers must download public website assets through CloudFront, while direct unauthenticated access to the regular S3 bucket origin must remain blocked. Which configuration fits?

**Recommended design:** Use CloudFront OAC and a scoped bucket policy while retaining appropriate S3 public-access blocking.

**Reason and boundary:** Viewer access and origin access are separate boundaries. OAC plus a distribution-scoped bucket policy lets CloudFront retrieve private origin objects without making the bucket public.

**Rejected alternative:** Grant public read access to the bucket and hide its name in the HTML. An obscure publicly readable bucket is still directly accessible.

**AWS references:** [CloudFront origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html), [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html).

## Scenario 4: Immediate database read after write

**Requirement:** A DynamoDB checkout workflow must confirm the latest committed order state immediately after its write. The current path reads an eventually consistent GSI. Which change directly addresses consistency?

**Recommended design:** Read the known order key from the base table using a strongly consistent read where required.

**Reason and boundary:** The base table supports strongly consistent reads. GSI reads do not; a faster caller or cache does not turn an eventually consistent read into a strong read.

**Rejected alternative:** Set ConsistentRead on the GSI and assume it is supported. Strongly consistent GSI reads are not supported.

**AWS references:** [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To apply this architecture foundation to pipelines, data, and analytics, you can also follow the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

# Guided Lab

## Objective

Trace a private same-Region S3 network path through a gateway endpoint.

## Services Used

VPC route tables, S3 gateway endpoint, IAM, and a private test client.

## Expected Cost Range

Gateway endpoints have a different charging model from interface endpoints and NAT gateways. Client compute, storage, requests, and any existing access infrastructure can still cost money.

## Step-by-Step Instructions

1. Use dedicated lab VPC networking and an approved private test client that already has a secure management path. Do not open management ports to the entire internet.
2. Create a private S3 test bucket in the same Region and grant the client role read access only to a small test object.
3. Create an S3 gateway endpoint and associate it with the route table used by the test-client subnet.
4. Review the added S3 prefix-list route and the endpoint policy. Keep bucket and IAM authorization in place.
5. From the managed test client, retrieve the known object using its existing temporary role credentials.
6. Inspect the route selection and verify that this S3 request path does not depend on a NAT gateway or internet gateway. Do not change unrelated production routes.

## Validation

- The endpoint route applies to the test subnet route table.
- The scoped authorized request succeeds without public bucket access.
- The learner distinguishes connectivity permission from IAM authorization.

## Cleanup

1. Delete the lab endpoint and remove its lab route associations.
2. Remove the test bucket object and bucket, client compute, and lab-only access infrastructure as appropriate.
3. Verify that no interface endpoint or NAT gateway created for access was overlooked.

## Exam Takeaway

State what the exercise proves, the assumptions it relies on, and what it does not test. A successful lab is evidence for the tested configuration, not a guarantee for every workload.

**AWS references:** [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html), [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html), [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

---

## ☁️ Follow CloudStudy

CloudStudy is an AWS certification preparation platform for structured study and practical learning.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> This module also connects with cloud data projects. To practice that aspect, explore the additional learning path: [Data Engineering on AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

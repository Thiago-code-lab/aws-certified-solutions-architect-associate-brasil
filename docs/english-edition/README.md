# English Edition Release Audit

This is the complete textual English edition of the original SAA-C03 repository.
All original educational documents are represented. The inherited editorial issues
and original Portuguese banner artwork described below remain explicit limitations.

## Branch Information

- Source: `origin/main`, commit `d43bc6a571c668b22127b283315582ac8c413a70`.
- Target: [`saa-c03-english`](https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english).
- Local `main` and remote `main` were preserved at the source commit.
- The protected `gh-pages` ref before publication was `e3c8302917591c90cec89c2e3b4c19a30ffc3a74`.
- The release uses ordinary commits and pushes exclusively to the English branch;
  no merge, pull request to `main`, force-push, or Pages publication is part of this release.
- To identify the exact checked-out release commit, run `git rev-parse HEAD`.

## Translation Coverage

| Measure | Result |
|---|---:|
| Original tracked files recursively analyzed | 198 |
| Original Markdown documents translated | 187 |
| Educational documents inside modules | 178 |
| HTML interfaces translated | 2 |
| Shell utilities selectively translated | 1 |
| Total original files with translated human-facing text | 190 |
| Modules represented in English | 31 of 31 |
| Directories renamed | 27 |
| Existing directory names already suitable for English | 4 |
| File basenames renamed | 56 |
| Original files with a changed full path | 166 |
| Correct-answer keys preserved in order | 145 |
| Answer options preserved in order | 580 |
| Expandable answer blocks preserved | 343 |
| Original visual assets preserved | 5 |
| Original lab documents preserved | 25 |
| Remaining Portuguese lesson or interface prose | 0 |

[source-inventory.json](./source-inventory.json) is the complete per-file inventory,
including source and target paths, classifications, source sizes and SHA-256 digests,
section counts, answer keys, alternatives, and disclosure blocks. The classifications are:

- Translatable educational content: 184 files.
- Translatable interface content: 2 files.
- Selectively translatable technical content: 4 files.
- Binary or visual assets: 5 files.
- Configuration, automation, or licensing: 3 files.

The last category includes the already-English deployment workflow. Its only change
is a branch guard that also protects manual runs; its deployment steps remain intact.
Inventory digests capture the original Windows checkout. Validation accepts the
equivalent CRLF checkout representation of Git's LF-normalized text blobs.
Binary asset hashes are compared without normalization.

Draft translations were followed by semantic inspection, terminology corrections,
consistent translations of repeated passages, and structural comparisons against the
source commit. The English terminology includes high availability, decoupling,
relational databases, encryption at rest, least privilege, practice exams, and hands-on labs.
Original product names, destinations, regional context, attribution, scenarios, question
options, and keyed answers remain represented. No educational sections were summarized away.

## Structural and Navigation Changes

The numeric module order remains 01 through 31. Existing English directory names
were retained for modules 12, 16, 17, and 26. Six dedicated lab modules retain their
original two-document structure: 03, 07, 09, 11, 12, and 15. No missing README or
lesson was fabricated for those modules.

Portuguese file basenames were replaced with descriptive English names, including
`use-cases.md`, `questions.md`, `error-log.md`, `mini-practice-exams-by-domain.md`,
`final-review-saa-c03.md`, `MODULE_TEMPLATE.md`, and `DOMAIN_STUDY_PATHS.md`.
Relative references, module paths, README anchors, image references, and the root
redirect now resolve to the English edition. Review filenames in module READMEs
are clickable, and the practice-exam hub links to all additional review tools.
Answer options have separate paragraphs for readable Markdown rendering.

CloudStudy logos, links, sponsorship, attribution, badges, photography, and the MIT
license are preserved. Language and promotional badge labels are in English.

## Portal Implementation

[`aws-saa-portal.html`](../../aws-saa-portal.html) retains the original colors,
typography, sidebar, filters, progress indicators, and reading layout. Both HTML
entry points use `lang="en"`. Repository loading is centralized in `REPOSITORY`:

- Owner: `Thiago-code-lab`.
- Repository: `aws-certified-solutions-architect-associate-brasil`.
- Branch: `saa-c03-english`.

Both Raw content requests and GitHub document links derive from that configuration.
The incorrect repository owner is no longer present in the portal. The original
`aws-saa-progress-v1` storage key and module-number keys remain unchanged.

Module resource navigation exposes every educational document. Relative document
links open within the portal; images use the correct Raw paths; anchors scroll
within the reading panel. External Markdown is restricted to supported HTML tags,
attributes, and HTTP(S) URLs before insertion. Requests time out, support retry,
and cannot overwrite a newer module selection. Invalid or unavailable browser
storage produces an English status message while allowing study to continue.
Completion controls support the keyboard and have English accessibility labels.

## Technical Validation

Machine-readable evidence is checked in alongside this report:

- [Content and link validation](./validation-results.json).
- [Chromium portal validation](./portal-test-results.json).
- [JavaScript, shell, YAML, and migration validation](./support-test-results.json).
- [Published GitHub Raw and downloaded-portal verification](./live-test-results.json).
- [Desktop screenshot](./portal-desktop.png).
- [Tablet screenshot](./portal-tablet.png).

The content validator compares every original file with its mapped English target.
It checks all module headings, numerical-value inventories, table structure,
answer options and keys, answer blocks, original educational external URLs, and
code blocks. There were no fenced code blocks in the source Markdown documents.
The license, funding file, and all original binary assets are protected comparisons.
Portuguese scans cover both accented and unaccented prose; immutable source paths
in audit data and historical migration inputs are intentional exceptions.

Chromium loaded all 31 modules and rendered all 187 original Markdown documents.
Tests cover search, empty states, all filters, progress toggling, keyboard controls,
reload persistence, domain progress, resource navigation, Markdown links, anchors,
images, GitHub links, HTTP failure and retry, request races, unsafe HTML, malformed
saved progress, unavailable storage, and desktop/tablet layout. Both HTML entry
points parse without HTML5 errors; portal JavaScript passes `node --check`.

The shell script passes `bash -n` and five fixture scenarios: no-op, migration of
current Portuguese names, migration of legacy names, duplicate destinations, and
existing-destination conflicts. Successful migrations are idempotent, and conflicts
fail before any directory is moved. Two YAML configurations and all three issue
template front-matter blocks parse successfully. The Pages workflow accepts push
events only from `main`, and its job explicitly requires `refs/heads/main` for manual runs.

## Reproducing Validation

Use Python 3.10 or later, Node.js, and Bash. Dependencies are pinned in
[`scripts/requirements-qa.txt`](../../scripts/requirements-qa.txt).

```sh
python -m venv .venv
# Activate .venv using the command appropriate for your shell.
python -m pip install -r scripts/requirements-qa.txt
python -m playwright install chromium
python scripts/validate_english.py
python scripts/test_english_portal.py
python scripts/test_english_support.py
git diff --check
```

The browser suite serves a local HTTP preview and intercepts the configured English
Raw URLs with the actual translated checkout, so it can run before publication.
To preview the portal manually, run `python -m http.server 8000` at the repository
root and open `http://localhost:8000/aws-saa-portal.html`. Its content still loads
from the configured public English branch; an internet connection is required.

After publication, all 198 original file equivalents were fetched from real English-branch
GitHub Raw URLs and matched byte for byte against their committed Git blobs. Chromium
also opened the downloaded/local HTML portal without request interception, loaded all
31 modules from GitHub, and retained progress after reload. This live verification
covered implementation commit `76e84d90f1af583902cf2fc87d53e4074e19515f`; the subsequent
audit-only commit adds this evidence without changing any of those 198 files.
The remote `main` and `gh-pages` refs remained unchanged.

## Source-Content Limitations

**Exam domain metadata — `README.md` and `aws-saa-portal.html`.** The source assigns
30% to resilience, 28% to performance, 24% to security, and 18% to cost. These source
numbers remain present to honor the preservation requirement. The
[official AWS exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03.html),
checked on November 10, 2026, assigns security 30%, resilience 26%, performance 24%,
and cost optimization 20%. The README and portal explicitly identify the inherited
allocations and direct learners to AWS. Use the official guide for exam planning.

**Inherited question explanations — the following 24 files.** In Question 4,
the stem asks for the incorrect option, but the generic source explanation describes
option B as the best fit and says option A is wrong even though option A describes
meeting the dominant requirement. The keyed answer B, all alternatives, and all
explanations were preserved. Each affected question set carries a source-edition
note. Resolving those editorial contradictions requires a separate content revision;
answer-preservation checks do not certify the correctness of the inherited claims.

- [01-Introduction-SAA-C03/questions.md](../../01-Introduction-SAA-C03/questions.md)
- [02-IAM-and-Security/questions.md](../../02-IAM-and-Security/questions.md)
- [04-EC2-Compute/questions.md](../../04-EC2-Compute/questions.md)
- [05-High-Availability-and-Scalability/questions.md](../../05-High-Availability-and-Scalability/questions.md)
- [06-Amazon-S3-and-Storage/questions.md](../../06-Amazon-S3-and-Storage/questions.md)
- [08-VPC-and-Networking/questions.md](../../08-VPC-and-Networking/questions.md)
- [10-Databases/questions.md](../../10-Databases/questions.md)
- [13-DNS-Route53-and-CloudFront/questions.md](../../13-DNS-Route53-and-CloudFront/questions.md)
- [14-Decoupling-SQS-SNS-EventBridge/questions.md](../../14-Decoupling-SQS-SNS-EventBridge/questions.md)
- [16-Containers-ECS-EKS-Fargate/questions.md](../../16-Containers-ECS-EKS-Fargate/questions.md)
- [17-Serverless-Lambda-API-Gateway/questions.md](../../17-Serverless-Lambda-API-Gateway/questions.md)
- [18-Data-and-Analytics/questions.md](../../18-Data-and-Analytics/questions.md)
- [19-Machine-Learning-and-AI/questions.md](../../19-Machine-Learning-and-AI/questions.md)
- [20-Monitoring-CloudWatch-CloudTrail/questions.md](../../20-Monitoring-CloudWatch-CloudTrail/questions.md)
- [21-Migration-and-Transfer/questions.md](../../21-Migration-and-Transfer/questions.md)
- [22-Disaster-Recovery-and-Business-Continuity/questions.md](../../22-Disaster-Recovery-and-Business-Continuity/questions.md)
- [23-AWS-Organizations-Governance-and-Costs/questions.md](../../23-AWS-Organizations-Governance-and-Costs/questions.md)
- [24-Advanced-Networking-and-Hybrid-Connectivity/questions.md](../../24-Advanced-Networking-and-Hybrid-Connectivity/questions.md)
- [25-Encryption-KMS-and-Secrets-Management/questions.md](../../25-Encryption-KMS-and-Secrets-Management/questions.md)
- [26-Well-Architected-Framework/questions.md](../../26-Well-Architected-Framework/questions.md)
- [27-Real-World-Use-Cases/questions.md](../../27-Real-World-Use-Cases/questions.md)
- [28-Hands-on-Labs/questions.md](../../28-Hands-on-Labs/questions.md)
- [30-Glossary/questions.md](../../30-Glossary/questions.md)
- [31-Resources-and-Links/questions.md](../../31-Resources-and-Links/questions.md)

## Visual and Execution Limitations

**`assets/Banner-SolutionsArchitect.png`.** This flattened branded artwork embeds
Portuguese captions. No editable source was available, so it was preserved byte for
byte rather than altering the CloudStudy branding or AWS artwork. Its full message
is translated into an adjacent English caption in the root README, and its alternative
text identifies the original artwork. All five original images were visually inspected;
the other four contain branding, English text, or photography and require no translation.

**External resources.** Original AWS, community, Udemy, and CloudStudy destination URLs
remain in place; some external resources intentionally remain in Portuguese. Their
contents are outside this repository's translation scope. AWS labs were not provisioned
in a live account, so resource behavior, billing, and full technical assertions were
not independently re-audited. The preserved lab documents are:

- [01-Introduction-SAA-C03/lab.md](../../01-Introduction-SAA-C03/lab.md)
- [02-IAM-and-Security/lab.md](../../02-IAM-and-Security/lab.md)
- [03-IAM-and-Security-Labs/lab.md](../../03-IAM-and-Security-Labs/lab.md)
- [04-EC2-Compute/lab.md](../../04-EC2-Compute/lab.md)
- [05-High-Availability-and-Scalability/lab.md](../../05-High-Availability-and-Scalability/lab.md)
- [07-Advanced-S3-Labs/lab.md](../../07-Advanced-S3-Labs/lab.md)
- [09-VPC-and-Networking-Labs/lab.md](../../09-VPC-and-Networking-Labs/lab.md)
- [11-RDS-and-Relational-Databases-Labs/lab.md](../../11-RDS-and-Relational-Databases-Labs/lab.md)
- [12-DynamoDB/lab.md](../../12-DynamoDB/lab.md)
- [15-SQS-SNS-Messaging-Labs/lab.md](../../15-SQS-SNS-Messaging-Labs/lab.md)
- [17-Serverless-Lambda-API-Gateway/lab.md](../../17-Serverless-Lambda-API-Gateway/lab.md)
- [18-Data-and-Analytics/lab.md](../../18-Data-and-Analytics/lab.md)
- [19-Machine-Learning-and-AI/lab.md](../../19-Machine-Learning-and-AI/lab.md)
- [20-Monitoring-CloudWatch-CloudTrail/lab.md](../../20-Monitoring-CloudWatch-CloudTrail/lab.md)
- [21-Migration-and-Transfer/lab.md](../../21-Migration-and-Transfer/lab.md)
- [22-Disaster-Recovery-and-Business-Continuity/lab.md](../../22-Disaster-Recovery-and-Business-Continuity/lab.md)
- [23-AWS-Organizations-Governance-and-Costs/lab.md](../../23-AWS-Organizations-Governance-and-Costs/lab.md)
- [24-Advanced-Networking-and-Hybrid-Connectivity/lab.md](../../24-Advanced-Networking-and-Hybrid-Connectivity/lab.md)
- [25-Encryption-KMS-and-Secrets-Management/lab.md](../../25-Encryption-KMS-and-Secrets-Management/lab.md)
- [26-Well-Architected-Framework/lab.md](../../26-Well-Architected-Framework/lab.md)
- [27-Real-World-Use-Cases/lab.md](../../27-Real-World-Use-Cases/lab.md)
- [28-Hands-on-Labs/lab.md](../../28-Hands-on-Labs/lab.md)
- [29-Practice-Exams-and-Questions/lab.md](../../29-Practice-Exams-and-Questions/lab.md)
- [30-Glossary/lab.md](../../30-Glossary/lab.md)
- [31-Resources-and-Links/lab.md](../../31-Resources-and-Links/lab.md)

**Hosting and browser constraints.** No English GitHub Pages deployment was created.
Use the branch selector and the local/downloaded portal. Content loading requires
GitHub Raw and the existing Marked CDN dependency; fonts use the original Google Fonts
URLs. The original small-screen sidebar layout is retained, with tablet overflow fixes;
a phone-specific interface redesign is outside this translation release.

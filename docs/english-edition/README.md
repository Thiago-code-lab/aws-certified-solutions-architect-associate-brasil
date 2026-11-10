# English Edition Audit Index

The English translation was published before this educational accuracy pass. The
current edition intentionally corrects inherited technical errors, ambiguous
questions, obsolete recommendations, and promotional language. Correctness takes
precedence over literal translation parity.

Read the [complete educational accuracy and release report](./editorial-release-report.md)
for every corrected question, all updated exam-weight references, broader teaching
corrections, validation results, publication status, and remaining limitations.

## Branch and coverage

- Working and publication branch: [`saa-c03-english`](https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english).
- Published English translation baseline: `b8d55e0f10de899c68e84b0388b6393a21104734`.
- Original Portuguese source and protected `main`: `d43bc6a571c668b22127b283315582ac8c413a70`.
- Protected `gh-pages`: `e3c8302917591c90cec89c2e3b4c19a30ffc3a74`.
- Coverage retained: 198 original file equivalents, 187 Markdown documents,
  178 module documents, 31 modules, 145 practice questions, 198 flashcards,
  100 use cases, and 25 lab documents.
- All 24 question files flagged by the translation audit have been corrected;
  their inherited Question 4 contradictions are marked **Priority Q4** in the report.
- No original document or module was removed. No merge or pull request to `main`,
  Pages publication, force-push, or modification of `gh-pages` is authorized by this release.

## Review records and evidence

| Record | Purpose |
|---|---|
| [Source inventory](./source-inventory.json) | Immutable mapping and digests of the original Portuguese files; historical coverage evidence. |
| [Editorial manifest](./editorial-manifest.json) | Review status, approved English digest, rationale, and AWS sources for each of the 198 original file equivalents. |
| [Question audit](./question-audit.json) | Every original/revised stem, original/revised key, stable ID, approved question digest, correction rationale, and AWS sources. |
| [Exam-reference ledger](./exam-reference-updates.json) | Every active exam-domain percentage reference, including explicitly rejected assessment alternatives. |
| [AWS reference catalog](./aws-reference-catalog.json) | Canonical primary sources used for technical review. |
| [AWS source verification](./aws-source-verification.json) | HTTP status, page title, and resolved URL for the reviewed catalog. |
| [Content validation](./validation-results.json) | Coverage, approved changes, counts, local links, language, weights, and deployment guard. |
| [Educational regression tests](./educational-test-results.json) | Corrected-answer acceptance and rejection of unapproved or contradictory changes. |
| [Portal tests](./portal-test-results.json) | Chromium rendering, navigation, progress, weights, security, errors, and layout. |
| [Support tests](./support-test-results.json) | JavaScript/Bash syntax, migration fixtures, YAML, and issue-template metadata. |
| [Published-release evidence](./live-test-results.json) | Exact verified implementation commit, real GitHub Raw comparisons, live portal checks, and protected refs. |
| [Desktop screenshot](./portal-desktop.png) / [tablet screenshot](./portal-tablet.png) | Visual verification of the retained portal. |

The previous translation-only audit is available in
[the published baseline](https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/blob/b8d55e0f10de899c68e84b0388b6393a21104734/docs/english-edition/README.md).
Its source-parity statements and unresolved-question warnings describe that historical
release, not the corrected edition.

## Editorial validation contract

The immutable source inventory still prevents loss of files, modules, answer options,
and expandable answer blocks. Original branding assets, license, funding, and deployment
isolation remain protected. The original numerical values, answer letters, tables,
and wording are no longer required to survive an intentional educational correction.

The new manifest compares reviewed content with the published English baseline and
binds approved file digests to explicit review reasons. A separate question ledger
binds all 145 reviewed blocks, answers, explanations, distractor rationales, and AWS
references. Contributors must review the technical change and update the relevant
records together. Automatically refreshing a digest is not a technical review.

Automated tests verify this contract and known regression boundaries. They do not
independently establish AWS semantic truth, exam readiness, lab runtime, or future
service availability. See the report for the execution and artwork limitations.

## Official exam weights

Use Security **30%**, Resilience **26%**, Performance **24%**, and Cost Optimization
**20%**, as specified by the
[official SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html).
These percentages apply to scored exam content. The portal's module-completion
indicators and the four equal mini-practice blocks are study tools.

## Reproducing validation

Use Python 3.10 or later, Node.js, and Bash. Dependencies are pinned in
[scripts/requirements-qa.txt](../../scripts/requirements-qa.txt).

```sh
python -m venv .venv
# Activate .venv using the command appropriate for your shell.
python -m pip install -r scripts/requirements-qa.txt
python -m playwright install chromium
python scripts/validate_english.py
python scripts/test_educational_accuracy.py
python scripts/test_english_portal.py
python scripts/test_english_support.py
git -c core.safecrlf=false diff --check
```

The portal suite serves a local HTTP preview and intercepts the configured English
GitHub Raw requests with actual checkout files. It loads all 31 modules and renders
all 187 original documents, then exercises navigation, persistence, keyboard controls,
official weights, sanitization, storage failures, request races, retry, and layout.
Supporting checks validate both HTML entry points, JavaScript, the migration utility,
the included lab Bash example, YAML, and issue templates.

For a manual preview, run `python -m http.server 8000` at the repository root and
open `http://localhost:8000/aws-saa-portal.html`. The unmodified portal retrieves
the configured public English branch and needs internet access. Downloading and
opening the HTML file is also supported. The existing Pages workflow remains
restricted to `main`, including manual-run job protection.

After branch-only publication, verify the live evidence's implementation commit
against the published content. Later audit-only commits may add verification evidence
without changing the original 198 file equivalents.

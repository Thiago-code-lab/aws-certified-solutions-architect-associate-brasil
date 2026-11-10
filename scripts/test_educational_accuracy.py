"""Regression tests for reviewed educational contracts, not a semantic AWS oracle."""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from editorial_checks import (AUDIT, ROOT, STALE_PROMOTION, check_question_bank,
    check_weights, parse_questions, question_errors)


class EducationalAccuracyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = json.loads((AUDIT / 'question-audit.json').read_text(encoding='utf-8'))
        cls.approvals = {item['id']: item for item in cls.audit['questions']}
        cls.catalog = json.loads((AUDIT / 'aws-reference-catalog.json').read_text(encoding='utf-8'))['sources']
        cls.questions = {}
        for path in {item['path'] for item in cls.audit['questions']}:
            cls.questions.update({item['id']: item for item in parse_questions((ROOT / path).read_text(encoding='utf-8'))})

    def test_complete_reviewed_bank(self) -> None:
        errors: list[str] = []
        totals = check_question_bank(errors)
        self.assertEqual(errors, [])
        self.assertEqual(totals, {'practice_questions': 145, 'explained_distractors': 435})

    def test_intentional_answer_changes_are_allowed(self) -> None:
        changed = [item for item in self.audit['questions'] if item['original_answer'] != item['answer']]
        self.assertGreater(len(changed), 0)
        for approved in changed:
            self.assertEqual(question_errors(self.questions[approved['id']], approved, self.catalog), [])

    def test_unapproved_answer_edit_is_rejected(self) -> None:
        original = self.questions['10-Q01']
        approved = self.approvals[original['id']]
        replacement = next(letter for letter in 'ABCD' if letter != approved['answer'])
        block = original['block'].replace(f'Correct answer:** {approved["answer"]}', f'Correct answer:** {replacement}')
        errors = question_errors(parse_questions(block)[0], approved, self.catalog)
        self.assertTrue(any('keyed answer' in error for error in errors))

    def test_contradictory_distractor_label_is_rejected(self) -> None:
        original = self.questions['02-Q02']
        approved = self.approvals[original['id']]
        wrong = next(iter(original['rationales']))
        block = original['block'].replace(f'- **{wrong}:**', f'- **{approved["answer"]}:**', 1)
        errors = question_errors(parse_questions(block)[0], approved, self.catalog)
        self.assertTrue(any('rationale' in error for error in errors))

    def test_unapproved_stem_edit_is_rejected(self) -> None:
        original = self.questions['14-Q03']
        block = original['block'].replace('within the deduplication interval', 'at any time forever', 1)
        self.assertNotEqual(block, original['block'])
        errors = question_errors(parse_questions(block)[0], self.approvals[original['id']], self.catalog)
        self.assertTrue(any('unapproved stem' in error for error in errors))

    def test_official_domain_weights_and_old_weight_regression(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        portal = (ROOT / 'aws-saa-portal.html').read_text(encoding='utf-8')
        self.assertEqual(check_weights(readme, portal), [])
        old = readme.replace('| Design Secure Architectures | 30% |', '| Design Secure Architectures | 24% |')
        self.assertTrue(check_weights(old, portal))
        self.assertTrue(check_weights(readme, portal.replace("pct:'26%', name:'Resilient Architectures'", "pct:'30%', name:'Resilient Architectures'")))

    def test_critical_aws_distinctions_remain_explicit(self) -> None:
        facts = {
            '10-Q01': ['does not serve application read traffic'],
            '10-Q02': ['can serve read traffic'],
            '10-Q05': ['multi-Region eventual consistency', 'multi-Region strong consistency'],
            '14-Q03': ['interval', 'retried processing safely'],
            '17-Q04': ['partial batch responses', 'failed item identifiers'],
            '21-Q05': ['closed to new customers', 'December 31, 2026'],
            '23-Q02': ['delayed', 'controls'],
            '24-Q01': ['not encrypted by default'],
            '25-Q02': ['not automatically re-encrypted'],
            '26-Q01': ['operational excellence', 'sustainability'],
        }
        for identity, required in facts.items():
            question = self.questions[identity]
            answer = question['options'][question['keys'][0]]
            for phrase in required:
                self.assertIn(phrase.casefold(), answer.casefold(), identity)

    def test_cloudstudy_launch_language_regression(self) -> None:
        self.assertIsNotNone(STALE_PROMOTION.search('Join the CloudStudy waitlist'))
        self.assertIsNotNone(STALE_PROMOTION.search('We are building a platform'))
        self.assertIsNone(STALE_PROMOTION.search('CloudStudy is an AWS certification preparation platform.'))
        for path in [ROOT / 'README.md', *ROOT.glob('[0-9][0-9]-*/*.md')]:
            self.assertIsNone(STALE_PROMOTION.search(path.read_text(encoding='utf-8')), str(path))

    def test_source_verification_matches_reviewed_catalog(self) -> None:
        evidence = json.loads((AUDIT / 'aws-source-verification.json').read_text(encoding='utf-8'))
        records = {item['id']: item for item in evidence['sources']}
        self.assertEqual(set(records), set(self.catalog))
        for identity, source in self.catalog.items():
            self.assertEqual(records[identity]['requested_url'], source['url'], identity)
            self.assertEqual(records[identity]['status'], 200, identity)
            self.assertTrue(records[identity]['page_title'], identity)

    def test_curriculum_resource_counts_are_preserved(self) -> None:
        modules = [path for path in ROOT.glob('[0-9][0-9]-*') if path.is_dir()]
        self.assertEqual(len(modules), 31)
        self.assertEqual(len(list(ROOT.glob('[0-9][0-9]-*/lab.md'))), 25)
        cards = sum(len(re.findall(r'^## Card \d+', path.read_text(encoding='utf-8'), re.M)) for path in ROOT.glob('[0-9][0-9]-*/flashcards.md'))
        scenarios = sum(len(re.findall(r'^## Scenario \d+:', path.read_text(encoding='utf-8'), re.M)) for path in ROOT.glob('[0-9][0-9]-*/use-cases.md'))
        self.assertEqual(cards, 198)
        self.assertEqual(scenarios, 100)


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(EducationalAccuracyTests))
    report = {'suite': 'educational accuracy regressions', 'tests_run': result.testsRun,
        'failures': len(result.failures), 'errors': len(result.errors),
        'practice_questions': 145, 'distractor_explanations': 435, 'passed': result.wasSuccessful()}
    (AUDIT / 'educational-test-results.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    raise SystemExit(0 if result.wasSuccessful() else 1)

"""Educational-release invariants separate approved edits from translation drift."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'docs/english-edition'
ENGLISH_BASELINE = 'b8d55e0f10de899c68e84b0388b6393a21104734'
WEIGHTS = {'security': 30, 'resilient': 26, 'performance': 24, 'cost': 20}
QUESTION_BLOCK = re.compile(r'#{2,3} Question (?P<number>\d+)\n\n<!-- question-id: (?P<id>[\w-]+) -->\n\n.*?</details>\n', re.S)
STALE_PROMOTION = re.compile(r'join.{0,30}waitlist|JOIN_THE_WAITLIST|early access to the platform|building a platform|pre-launch', re.I)


def digest(data: bytes, binary: bool = False) -> str:
    normalized = data if binary else data.replace(b'\r\n', b'\n')
    return hashlib.sha256(normalized).hexdigest()


def read_git_files(commit: str, paths: list[str]) -> dict[str, bytes]:
    request = '\n'.join(f'{commit}:{path}' for path in paths) + '\n'
    output = subprocess.run(['git', 'cat-file', '--batch'], cwd=ROOT, input=request.encode(),
        stdout=subprocess.PIPE, check=True).stdout
    result: dict[str, bytes] = {}
    offset = 0
    for path in paths:
        end = output.index(b'\n', offset)
        header = output[offset:end].split()
        if header[-1] == b'missing':
            raise ValueError(f'Missing editorial baseline file: {path}')
        size = int(header[-1])
        result[path] = output[end+1:end+1+size]
        offset = end + size + 2
    return result


def check_approved_files(inventory: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    manifest = json.loads((AUDIT / 'editorial-manifest.json').read_text(encoding='utf-8'))
    if manifest['baseline_commit'] != ENGLISH_BASELINE:
        errors.append('Editorial baseline must remain the published English translation commit')
    expected = {item['target'] for item in inventory['files']}
    entries = manifest['files']
    if set(entries) != expected:
        errors.append('Editorial approvals must cover exactly the complete original file inventory')
    baseline = read_git_files(ENGLISH_BASELINE, sorted(expected))
    for path, entry in entries.items():
        binary = Path(path).suffix in {'.png', '.jpg'}
        if entry['baseline_sha256'] != digest(baseline[path], binary):
            errors.append(f'Editorial baseline digest mismatch: {path}')
        current = ROOT / path
        if not current.is_file() or entry['approved_sha256'] != digest(current.read_bytes(), binary):
            errors.append(f'Unapproved editorial content change: {path}')
        if not entry.get('review_reason'):
            errors.append(f'Missing editorial review rationale: {path}')
        if entry['baseline_sha256'] != entry['approved_sha256'] and entry['status'] != 'editorially-corrected':
            errors.append(f'Changed content was not classified as an intentional correction: {path}')
    return {'editorial_baseline': manifest['baseline_commit'], 'reviewed_original_files': len(entries),
        'intentional_editorial_file_changes': sum(item['status'] == 'editorially-corrected' for item in entries.values())}


def parse_questions(text: str) -> list[dict[str, Any]]:
    result = []
    for match in QUESTION_BLOCK.finditer(text):
        block = match[0]
        options = dict(re.findall(r'^([A-D])\) (.+)$', block, re.M))
        keys = re.findall(r'Correct answer:\*\*\s*([A-D])', block)
        rationale = dict(re.findall(r'^- \*\*([A-D]):\*\* (.+)$', block, re.M))
        explanation = re.search(r'\*\*Explanation:\*\* (.*?)\n\n', block, re.S)
        result.append({'id': match['id'], 'number': int(match['number']), 'block': block,
            'option_labels': re.findall(r'^([A-D])\) ', block, re.M), 'options': options,
            'keys': keys, 'rationales': rationale, 'explanation': explanation[1] if explanation else ''})
    return result


def question_errors(question: dict[str, Any], approved: dict[str, Any], catalog: dict[str, Any]) -> list[str]:
    errors = []
    identity = question['id']
    if question['option_labels'] != list('ABCD') or len(set(question['options'].values())) != 4:
        errors.append(f'{identity}: four distinct ordered alternatives required')
    if question['keys'] != [approved['answer']]:
        errors.append(f'{identity}: keyed answer differs from the reviewed answer')
    if len(question['keys']) == 1 and set(question['rationales']) != set('ABCD') - set(question['keys']):
        errors.append(f'{identity}: a separate rationale is required for every distractor, not the keyed answer')
    if len(question['explanation'].split()) < 15 or any(len(value.split()) < 4 for value in question['rationales'].values()):
        errors.append(f'{identity}: substantive answer and distractor explanations required')
    if digest(question['block'].encode()) != approved['sha256']:
        errors.append(f'{identity}: unapproved stem, alternative, explanation, or source change')
    for key in approved['sources']:
        if key not in catalog or catalog[key]['url'] not in question['block']:
            errors.append(f'{identity}: missing reviewed AWS source {key}')
    return errors


def check_question_bank(errors: list[str]) -> dict[str, int]:
    audit = json.loads((AUDIT / 'question-audit.json').read_text(encoding='utf-8'))
    catalog = json.loads((AUDIT / 'aws-reference-catalog.json').read_text(encoding='utf-8'))['sources']
    approvals = {item['id']: item for item in audit['questions']}
    seen: set[str] = set()
    totals: Counter[str] = Counter()
    for path in sorted({item['path'] for item in audit['questions']}):
        text = (ROOT / path).read_text(encoding='utf-8')
        questions = parse_questions(text)
        expected = [item for item in audit['questions'] if item['path'] == path]
        if len(questions) != len(expected) or [item['number'] for item in questions] != list(range(1, len(expected)+1)):
            errors.append(f'Question count or numbering mismatch: {path}')
        for question in questions:
            identity = question['id']
            if identity in seen or identity not in approvals:
                errors.append(f'Duplicate or unapproved question ID: {identity}')
                continue
            seen.add(identity)
            if approvals[identity]['path'] != path:
                errors.append(f'Question moved outside its reviewed module: {identity}')
            errors.extend(question_errors(question, approvals[identity], catalog))
            totals.update(practice_questions=1, explained_distractors=len(question['rationales']))
    if len(seen) != 145 or seen != set(approvals):
        errors.append('The release must contain all 145 individually reviewed practice questions')
    for key, source in catalog.items():
        if urlsplit(source['url']).hostname not in {'docs.aws.amazon.com', 'aws.amazon.com', 'calculator.aws'}:
            errors.append(f'Non-primary source in AWS reference catalog: {key}')
    return dict(totals)


def check_weights(readme: str, portal: str) -> list[str]:
    expected_names = {'security': 'Design Secure Architectures', 'resilient': 'Design Resilient Architectures',
        'performance': 'Design High-Performing Architectures', 'cost': 'Design Cost-Optimized Architectures'}
    errors = []
    for key, name in expected_names.items():
        if not re.search(rf'\| {re.escape(name)} \| {WEIGHTS[key]}% \|', readme):
            errors.append(f'Incorrect official README exam weight: {name}')
    cards = re.search(r'const DOMAIN_CARDS = \[(.*?)\];', portal, re.S)
    actual = {} if not cards else {domain: int(weight) for weight, domain in re.findall(r"pct:'(\d+)%'.*?domain:'([^']+)'", cards[1])}
    if actual != WEIGHTS:
        errors.append('Portal domain cards must use Security 30 / Resilience 26 / Performance 24 / Cost 20')
    return errors


def check_learning_guidance(files: list[Path], errors: list[str]) -> None:
    for path in files:
        if path.is_relative_to(AUDIT):
            continue
        text = path.read_text(encoding='utf-8')
        if STALE_PROMOTION.search(text):
            errors.append(f'Obsolete CloudStudy launch language: {path.relative_to(ROOT)}')
        if 'when controlled elasticity and predictable behavior during spikes are required' in text:
            errors.append(f'Cross-topic service-selection boilerplate remains: {path.relative_to(ROOT)}')
        if '**Source-edition note:**' in text or 'Domain mastered: consistently score above 80%' in text:
            errors.append(f'Superseded educational guidance remains: {path.relative_to(ROOT)}')

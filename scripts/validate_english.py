"""Validate English coverage, content preservation, links, and deployment isolation.

Run with Python 3.10+ and PyYAML: python scripts/validate_english.py
The immutable inventory identifies the source Git commit for every comparison.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'docs/english-edition'
INVENTORY: dict[str, Any] = json.loads((AUDIT / 'source-inventory.json').read_text(encoding='utf-8'))
URL_PATTERN = re.compile(r'https?://[^\s<>"\)\]]+')
PORTUGUESE = re.compile(
    r'\b(?:nao|não|voce|você|questoes|questões|questao|questão|enunciado|prova|'
    r'simulado[s]?|seguranca|segurança|armazenamento|documentacao|documentação|'
    r'custo[s]?|dados|revisao|revisão|modulo[s]?|módulo[s]?|trilha[s]?|'
    r'escalabilidade|desacoplamento|servico[s]?|serviço[s]?|concluido|concluído|'
    r'introducao|introdução|termos|quando|sem|com|para|porem|porém|tambem|também)\b', re.I)


def git(*args: str) -> bytes:
    return subprocess.check_output(['git', *args], cwd=ROOT)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def source_blobs() -> dict[str, bytes]:
    specs = [f'{INVENTORY["source_commit"]}:{item["source"]}' for item in INVENTORY['files']]
    response = subprocess.run(['git', 'cat-file', '--batch'], cwd=ROOT,
        input=('\n'.join(specs) + '\n').encode(), stdout=subprocess.PIPE, check=True).stdout
    blobs: dict[str, bytes] = {}
    position = 0
    for spec in specs:
        end = response.index(b'\n', position)
        size = int(response[position:end].split()[-1])
        blobs[spec.split(':', 1)[1]] = response[end+1:end+1+size]
        position = end + size + 2
    return blobs


def prose(text: str) -> str:
    return re.sub(r'<[^>]*>|`[^`]*`|https?://[^\s<>\)"\]]+|\]\([^)]*\)', '', text)


def structure(text: str, source: bool) -> dict[str, Any]:
    key = 'Resposta correta' if source else 'Correct answer'
    return {
        'headings': re.findall(r'^#{1,6} ', text.lstrip('\ufeff'), re.M),
        'answers': re.findall(rf'{key}:\*\*\s*([A-D])', text),
        'options': re.findall(r'(?:^| )([A-D])\)', text, re.M),
        'details': text.count('<details>'),
        'summaries': text.count('<summary>'),
        'tables': [line.count('|') for line in text.splitlines() if line.startswith('|')],
        'numbers': Counter(re.findall(r'\d+(?:[.,]\d+)*', prose(text))),
        'code': re.findall(r'```[^\n]*\n(.*?)```', text, re.S),
    }


def check_content(blobs: dict[str, bytes], errors: list[str]) -> dict[str, int]:
    totals = Counter(documents=0, answer_keys=0, answer_options=0, answer_blocks=0)
    for item in INVENTORY['files']:
        target = ROOT / item['target']
        require(target.is_file(), f'Missing source equivalent: {item["target"]}', errors)
        original = blobs[item['source']]
        digests = {hashlib.sha256(original).hexdigest()}
        if item['category'] != 'binary-or-visual-asset':
            digests.add(hashlib.sha256(original.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')).hexdigest())
        require(item['sha256'] in digests,
            f'Invalid source digest: {item["source"]}', errors)
        if not target.is_file():
            continue
        if item['category'] == 'binary-or-visual-asset' or item['source'] in {'LICENSE', '.github/FUNDING.yml'}:
            require(target.read_bytes().replace(b'\r\n', b'\n') == blobs[item['source']].replace(b'\r\n', b'\n'),
                f'Protected file modified: {item["target"]}', errors)
        if not target.suffix == '.md':
            continue
        old = structure(blobs[item['source']].decode('utf-8'), True)
        target_text = target.read_text(encoding='utf-8')
        new = structure(target_text, False)
        for field in ['answers', 'options', 'details', 'summaries', 'code', 'tables']:
            require(old[field] == new[field], f'Changed {field}: {item["target"]}', errors)
        if re.match(r'^\d{2}-', item['target']):
            old_urls = Counter(URL_PATTERN.findall(unescape(blobs[item['source']].decode('utf-8'))))
            new_urls = Counter(URL_PATTERN.findall(unescape(target_text)))
            require(not old_urls - new_urls, f'Original external URLs missing: {item["target"]}', errors)
            for field in ['headings', 'numbers']:
                require(old[field] == new[field], f'Changed {field}: {item["target"]}', errors)
        totals.update(documents=1, answer_keys=len(new['answers']),
            answer_options=len(new['options']), answer_blocks=new['details'])
    return dict(totals)


class References(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        self.links.extend(value for name, value in attrs if name in {'href', 'src'} and value)
        if values.get('id'):
            self.ids.add(str(values['id']))


def heading_ids(text: str) -> set[str]:
    parser = References()
    parser.feed(text)
    ids = parser.ids
    occurrences: Counter[str] = Counter()
    for heading in re.findall(r'^#{1,6} (.*)', text, re.M):
        heading = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', heading).replace('`', '')
        cleaned = ''.join(c for c in unescape(heading).lower()
            if c in {' ', '-', '_'} or unicodedata.category(c)[0] in {'L', 'N'})
        slug = cleaned.replace(' ', '-')
        number = occurrences[slug]
        occurrences[slug] += 1
        ids.add(slug + (f'-{number}' if number else ''))
    return ids


def check_links(files: list[Path], errors: list[str]) -> dict[str, int]:
    references = anchors = 0
    for path in files:
        text = path.read_text(encoding='utf-8')
        parser = References()
        parser.feed(text)
        links = parser.links + re.findall(r'\]\(([^)]+)\)', text)
        for raw in links:
            if any(token in raw for token in ['${', '{{', '`']):
                continue
            link = urlsplit(unescape(raw).strip('<>'))
            if link.scheme or link.netloc:
                continue
            destination = (path.parent / unquote(link.path)).resolve() if link.path else path
            references += 1
            require(destination.is_relative_to(ROOT) and destination.exists(),
                f'Broken local reference in {path.relative_to(ROOT)}: {raw}', errors)
            if link.fragment and destination.is_file() and destination.suffix in {'.md', '.html'}:
                anchors += 1
                require(unquote(link.fragment) in heading_ids(destination.read_text(encoding='utf-8')),
                    f'Broken anchor in {path.relative_to(ROOT)}: {raw}', errors)
    return {'local_references': references, 'anchors': anchors}


def check_language(files: list[Path], errors: list[str]) -> None:
    for path in files:
        for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if match := PORTUGUESE.search(prose(line)):
                errors.append(f'Portuguese prose in {path.relative_to(ROOT)}:{number}: {match[0]}')
            if '\ufffd' in line or 'ZXQ' in line or 'â✅' in line:
                errors.append(f'Encoding or translation artifact in {path.relative_to(ROOT)}:{number}')


def check_portal(errors: list[str]) -> int:
    text = (ROOT / 'aws-saa-portal.html').read_text(encoding='utf-8')
    paths = re.findall(r"num:'\d{2}'.*?file:'([^']+)'", text)
    require(len(paths) == 31 and len(set(paths)) == 31, 'Portal must list 31 unique modules', errors)
    for path in paths:
        require((ROOT / path).is_file(), f'Portal file missing: {path}', errors)
    for value in ['lang="en"', "owner: 'Thiago-code-lab'", "branch: 'saa-c03-english'",
                  "name: 'aws-certified-solutions-architect-associate-brasil'", "'aws-saa-progress-v1'"]:
        require(value in text, f'Portal configuration missing: {value}', errors)
    require('cleytonsilva' not in text, 'Portal still references the incorrect owner', errors)
    return len(paths)


def check_automation(errors: list[str]) -> None:
    paths = list((ROOT / '.github').rglob('*.yml'))
    for path in paths:
        yaml.safe_load(path.read_text(encoding='utf-8'))
    workflow = yaml.load((ROOT / '.github/workflows/deploy.yml').read_text(encoding='utf-8'), Loader=yaml.BaseLoader)
    require(workflow['on']['push']['branches'] == ['main'], 'Pages push trigger changed', errors)
    require(workflow['jobs']['deploy']['if'] == "github.ref == 'refs/heads/main'", 'Pages manual guard missing', errors)


def main() -> int:
    errors: list[str] = []
    blobs = source_blobs()
    totals = check_content(blobs, errors)
    files = [ROOT / item['target'] for item in INVENTORY['files']
             if Path(item['target']).suffix in {'.md', '.html'} and (ROOT / item['target']).exists()]
    files.extend(sorted(AUDIT.glob('*.md')))
    module_dirs = sorted(path.name for path in ROOT.iterdir() if path.is_dir() and re.match(r'^\d{2}-', path.name))
    require(module_dirs == sorted(INVENTORY['directories'].values()), 'Module directory inventory changed', errors)
    links = check_links(files, errors)
    check_language(files, errors)
    check_automation(errors)
    report = {'source_commit': INVENTORY['source_commit'], 'source_files': len(INVENTORY['files']),
        'modules': len(module_dirs), **totals, **links, 'portal_modules': check_portal(errors), 'errors': errors}
    (AUDIT / 'validation-results.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())

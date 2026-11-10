"""Check JavaScript syntax, YAML templates, and safe migration behavior."""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def bash_path() -> str:
    candidate = Path(os.environ.get('ProgramFiles', 'C:/Program Files')) / 'Git/bin/bash.exe'
    executable = str(candidate) if os.name == 'nt' and candidate.is_file() else shutil.which('bash')
    if not executable:
        raise RuntimeError('Bash is required to check the migration script')
    return executable


def run_migration(bash: str, directory: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run([bash, str(ROOT / 'scripts/renumber-saa-c03-modules.sh')],
        cwd=directory, text=True, capture_output=True, check=False)


def check_migration(bash: str, workspace: Path) -> int:
    scenarios = [
        ('empty', [], [], True),
        ('current-portuguese', ['01-Introducao-SAA-C03', '08-VPC-e-Redes'],
            ['01-Introduction-SAA-C03', '08-VPC-and-Networking'], True),
        ('legacy', ['03-Computacao-EC2', '16-Well-Architected-Framework'],
            ['04-EC2-Compute', '26-Well-Architected-Framework'], True),
        ('duplicate-target', ['03-Computacao-EC2', '04-Computacao-EC2'], [], False),
        ('existing-target', ['01-Introducao-SAA-C03', '01-Introduction-SAA-C03'], [], False),
    ]
    for name, sources, targets, success in scenarios:
        fixture = workspace / name
        fixture.mkdir()
        for source in sources:
            (fixture / source).mkdir()
            (fixture / source / 'marker.txt').write_text(source, encoding='utf-8')
        result = run_migration(bash, fixture)
        assert (result.returncode == 0) == success, result.stderr
        if success:
            for source, target in zip(sources, targets, strict=True):
                assert (fixture / target / 'marker.txt').read_text(encoding='utf-8') == source
            assert run_migration(bash, fixture).returncode == 0, 'Migration must be idempotent'
        else:
            assert all((fixture / source / 'marker.txt').exists() for source in sources)
            assert not list(fixture.glob('__tmp__*')), 'Preflight must fail before any move'
    return len(scenarios)


def check_yaml() -> dict[str, int]:
    configurations = list((ROOT / '.github').rglob('*.yml'))
    for path in configurations:
        yaml.safe_load(path.read_text(encoding='utf-8'))
    templates = list((ROOT / '.github/ISSUE_TEMPLATE').glob('*.md'))
    for path in templates:
        metadata = yaml.safe_load(path.read_text(encoding='utf-8').split('---', 2)[1])
        assert {'name', 'about', 'labels'} <= metadata.keys(), path
        assert isinstance(metadata['about'], str), path
    return {'yaml_configurations': len(configurations), 'issue_template_front_matter': len(templates)}


def main() -> None:
    bash = bash_path()
    subprocess.run([bash, '-n', str(ROOT / 'scripts/renumber-saa-c03-modules.sh')], check=True)
    with tempfile.TemporaryDirectory(prefix='saa-c03-english-qa-') as temporary:
        workspace = Path(temporary).resolve()
        assert workspace.parent == Path(tempfile.gettempdir()).resolve()
        source = (ROOT / 'aws-saa-portal.html').read_text(encoding='utf-8')
        javascript = workspace / 'portal.js'
        javascript.write_text('\n'.join(re.findall(r'<script>(.*?)</script>', source, re.S)), encoding='utf-8')
        subprocess.run(['node', '--check', str(javascript)], check=True)
        scenarios = check_migration(bash, workspace)
    report = {'javascript_syntax': 'passed', 'shell_syntax': 'passed',
        'migration_scenarios': scenarios, 'collision_protection': 'passed', 'idempotence': 'passed',
        **check_yaml(), 'errors': []}
    (ROOT / 'docs/english-edition/support-test-results.json').write_text(
        json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()

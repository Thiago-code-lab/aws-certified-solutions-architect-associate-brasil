"""Exercise the English portal in Chromium against the translated checkout.

Dependencies: playwright, html5lib. Run `playwright install chromium` first.
Raw GitHub requests are intercepted and served from the working tree, allowing
the complete release to be tested before the branch is published.
"""
from __future__ import annotations

import asyncio
import functools
import json
import mimetypes
import re
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

import html5lib
from playwright.async_api import Page, Route, async_playwright

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'docs/english-edition'
RAW = 'https://raw.githubusercontent.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/saa-c03-english/'
GITHUB = 'https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/blob/saa-c03-english/'


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: Any) -> None:
        pass


def check_html() -> dict[str, int]:
    results = {}
    for name in ['aws-saa-portal.html', 'index.html']:
        parser = html5lib.HTMLParser(strict=False)
        parser.parse((ROOT / name).read_text(encoding='utf-8'))
        assert not parser.errors, f'{name}: {parser.errors}'
        results[name] = len(parser.errors)
    return results


async def serve_checkout(route: Route, state: dict[str, Any]) -> None:
    path = unquote(urlsplit(route.request.url).path.split('/saa-c03-english/', 1)[1])
    file = (ROOT / path).resolve()
    assert file.is_relative_to(ROOT), f'Invalid raw path: {path}'
    state['requests'].add(path)
    if path == state.get('failure'):
        await route.fulfill(status=503, body='Unavailable')
    elif path == state.get('delay'):
        await asyncio.sleep(0.3)
        await route.fulfill(path=file, content_type='text/markdown; charset=utf-8')
    elif file.is_file():
        content_type = 'text/markdown; charset=utf-8' if file.suffix == '.md' else mimetypes.guess_type(file.name)[0]
        await route.fulfill(path=file, content_type=content_type or 'application/octet-stream')
    else:
        await route.fulfill(status=404, body='Missing checkout file')


async def check_all_documents(page: Page) -> tuple[int, int]:
    modules = await page.evaluate('MODULES')
    assert len(modules) == 31
    for module in modules:
        await page.evaluate('async mod => await loadModule(mod)', module)
        assert await page.locator('.md-content h1').count() == 1, module['file']
        assert await page.locator('.error-state').count() == 0, module['file']
    paths = await page.evaluate('[...DOCUMENT_PATHS]')
    for path in paths:
        module = next((mod for mod in modules if mod['file'].split('/')[0] == path.split('/')[0]), modules[0])
        await page.evaluate('async ({mod,path}) => await loadDocument(mod,path)', {'mod': module, 'path': path})
        assert await page.locator('.md-content h1, .md-content h2').count() > 0, path
        assert await page.locator('.error-state').count() == 0, path
        assert (await page.locator('.md-content').inner_text()).strip(), path
    return len(modules), len(paths)


async def check_filters(page: Page) -> None:
    await page.locator('#searchInput').fill('security')
    assert await page.locator('.mod-item').count() == 2
    await page.locator('#searchInput').fill('31')
    assert await page.locator('.mod-item').count() == 1
    await page.locator('#searchInput').fill('no-such-module-test')
    assert await page.locator('#sidebarList').inner_text() == 'No modules found'
    await page.locator('#searchInput').fill('')
    await page.locator('#f-completed').click()
    assert await page.locator('.mod-item').count() == 0
    await page.locator('#f-all').click()
    assert await page.locator('.mod-item').count() == 31


async def check_progress(page: Page) -> None:
    await page.locator('[role=checkbox]').nth(1).click()
    assert await page.locator('#progressCount').inner_text() == '1/31'
    assert await page.evaluate('JSON.parse(localStorage.getItem(STORAGE_KEY))["02"]') is True
    await page.reload()
    await page.wait_for_function('typeof MODULES !== "undefined"')
    assert await page.locator('#progressCount').inner_text() == '1/31'
    count = await page.evaluate('MODULES.filter(m => m.domain === "security").length')
    assert await page.locator('.dm3 .dm-prog').inner_text() == f'1/{count}'
    await page.locator('#f-pending').click()
    assert await page.locator('.mod-item').count() == 30
    await page.locator('#f-completed').click()
    assert await page.locator('.mod-item').count() == 1
    await page.evaluate('async () => await loadModule(MODULES[1])')
    assert await page.locator('.complete-banner').count() == 1
    await page.locator('[role=checkbox]').press('Space')
    assert await page.locator('#progressCount').inner_text() == '0/31'
    assert await page.locator('.complete-banner').count() == 0
    await page.locator('#f-all').click()


async def check_navigation(page: Page) -> None:
    await page.evaluate('async () => await loadModule(MODULES[1])')
    await page.locator('.md-content a[data-document$="/questions.md"]').click()
    await page.wait_for_function('activePath.endsWith("/questions.md") && document.querySelector(".md-content")')
    assert await page.locator('#contentActions a').get_attribute('href') == GITHUB + '02-IAM-and-Security/questions.md'
    await page.locator('.resource-nav a', has_text='Flashcards').click()
    await page.wait_for_function('activePath.endsWith("/flashcards.md") && document.querySelector(".md-content")')
    await page.evaluate('async () => await loadDocument(MODULES[0], "README.md")')
    images = await page.locator('.md-content img').evaluate_all('(images) => images.map(image => image.src)')
    assert any(url.startswith(RAW + 'assets/') for url in images)
    await page.locator('.md-content a[href="#how-to-use-this-repository"]').click()
    assert await page.locator('#contentBody').evaluate('(element) => element.scrollTop') > 0
    assert await page.locator('#repositoryLink').get_attribute('href') == GITHUB.replace('/blob/', '/tree/').rstrip('/')


async def check_failures(page: Page, state: dict[str, Any]) -> None:
    state['failure'] = '01-Introduction-SAA-C03/README.md'
    await page.evaluate('async () => await loadModule(MODULES[0])')
    assert 'Unable to load this document' in await page.locator('.error-state').inner_text()
    assert await page.locator('.error-state a').get_attribute('href') == GITHUB + state['failure']
    state.pop('failure')
    await page.locator('#retryDocument').click()
    await page.wait_for_selector('.md-content')
    state['delay'] = '01-Introduction-SAA-C03/README.md'
    await page.evaluate('async () => await Promise.all([loadModule(MODULES[0]), loadModule(MODULES[30])])')
    assert await page.evaluate('activePath') == '31-Resources-and-Links/README.md'
    assert await page.locator('.md-content h1').inner_text() == 'Resources and Links'
    state.pop('delay')


async def check_defensive_inputs(page: Page) -> None:
    sanitized = await page.evaluate('''() => renderMarkdown(
      '<script>window.bad=true<\\/script><img src="javascript:bad" onerror="window.bad=true">' +
      '<iframe src="https://example.com"></iframe><a href="javascript:bad">unsafe</a>' +
      '<a href="http://[">malformed</a>', MODULES[0].file).innerHTML''')
    assert not re.search(r'<script|<iframe|onerror|javascript:', sanitized, re.I), sanitized
    await page.evaluate('localStorage.setItem(STORAGE_KEY, "[]")')
    await page.reload()
    await page.wait_for_function('typeof MODULES !== "undefined"')
    assert await page.locator('#progressCount').inner_text() == '0/31'
    assert 'Saved progress could not be read' in await page.locator('#toastMsg').inner_text()
    await page.evaluate('Object.defineProperty(Storage.prototype, "setItem", { value() { throw new Error("blocked"); } })')
    await page.locator('[role=checkbox]').first.click()
    assert await page.locator('#progressCount').inner_text() == '1/31'
    assert 'browser storage is unavailable' in await page.locator('#toastMsg').inner_text()


async def check_layout(page: Page) -> list[str]:
    screenshots = []
    for width, height, name in [(1440, 1000, 'portal-desktop.png'), (768, 1024, 'portal-tablet.png')]:
        await page.set_viewport_size({'width': width, 'height': height})
        await page.evaluate('async () => await loadModule(MODULES[1])')
        await page.evaluate('document.getElementById("toast").classList.remove("show"); clearTimeout(toastTimer)')
        assert await page.evaluate('document.documentElement.scrollWidth <= innerWidth')
        await page.screenshot(path=AUDIT / name, full_page=True)
        screenshots.append(name)
    return screenshots


async def run_browser(base: str) -> dict[str, Any]:
    state: dict[str, Any] = {'requests': set()}
    errors: list[str] = []
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page(viewport={'width': 1440, 'height': 1000})
        page.on('pageerror', lambda error: errors.append(str(error)))
        await page.route(RAW + '**', lambda route: serve_checkout(route, state))
        await page.goto(base + '/aws-saa-portal.html')
        await page.wait_for_function('typeof MODULES !== "undefined"')
        assert await page.locator('html').get_attribute('lang') == 'en'
        modules, documents = await check_all_documents(page)
        await check_filters(page)
        await check_progress(page)
        await check_navigation(page)
        await check_failures(page, state)
        screenshots = await check_layout(page)
        await check_defensive_inputs(page)
        assert not errors, errors
        await browser.close()
    return {'browser': 'Chromium', 'mode': 'local checkout served through intercepted English-branch Raw URLs',
        'modules_loaded': modules, 'documents_rendered': documents,
        'checks': ['search', 'empty state', 'all/pending/completed filters', 'progress toggling',
            'keyboard progress controls', 'persistence after reload', 'domain progress', 'resource navigation',
            'relative Markdown links', 'anchor navigation', 'image rebasing', 'GitHub links',
            'HTTP error and retry', 'request race handling', 'HTML sanitization',
            'malformed localStorage', 'unavailable localStorage', 'desktop and tablet layout'],
        'screenshots': screenshots, 'page_errors': errors}


def main() -> None:
    html = check_html()
    handler = functools.partial(QuietHandler, directory=str(ROOT))
    with ThreadingHTTPServer(('127.0.0.1', 0), handler) as server:
        threading.Thread(target=server.serve_forever, daemon=True).start()
        try:
            report = asyncio.run(run_browser(f'http://127.0.0.1:{server.server_port}'))
        finally:
            server.shutdown()
    report['html_parse_errors'] = html
    (AUDIT / 'portal-test-results.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()

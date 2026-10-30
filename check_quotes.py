"""Check that every quoted line in index.html appears in the 3-2-1 issue it cites.

Usage: python3 check_quotes.py [cache_dir]

Fetches each cited issue from jamesclear.com/3-2-1/<month>-<day>-<year> (cached in
cache_dir, default ./.issues) and exits 1 if any quote is missing from every issue it cites.
"""
import datetime
import html
import pathlib
import re
import sys
import urllib.error
import urllib.request

QUOTE = re.compile(r'"([^"]{8,300})"')
DATES = re.compile(r'\((\d{4}-\d{2}-\d{2}(?: · \d{4}-\d{2}-\d{2})*)\)|^(\d{4}-\d{2}-\d{2})$', re.M)


def text_of(page: str) -> str:
    page = re.sub(r'<(script|style)\b.*?</\1>', ' ', page, flags=re.S)
    return html.unescape(re.sub(r'<[^>]+>', '\n', page))


def norm(s: str) -> str:
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', '-').replace('–', '-').replace(' ', ' ').replace('​', '')
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()


def citations(page_text: str):
    """Yield (quote, [dates]): each quoted line paired with the next date group after it."""
    page_text = page_text[page_text.index('\u2605 The 15 best'):page_text.index('\u27f3 From reading')]
    flat = '\n'.join(ln.strip() for ln in page_text.splitlines() if ln.strip())
    pending = []
    pos = 0
    for m in DATES.finditer(flat):
        # quotes under 3 words are coined terms ("muddy puddles"), not citations
        pending += [q.replace('\n', ' ') for q in QUOTE.findall(flat[pos:m.start()]) if len(q.split()) >= 3]
        dates = (m.group(1) or m.group(2)).split(' · ')
        for q in pending:
            yield q, dates
        pending = []
        pos = m.end()


def issue(date: str, cache: pathlib.Path) -> str:
    d = datetime.date.fromisoformat(date)
    slug = f'{d.strftime("%B").lower()}-{d.day}-{d.year}'
    f = cache / f'{slug}.html'
    if not f.exists():
        req = urllib.request.Request(f'https://jamesclear.com/3-2-1/{slug}', headers={'User-Agent': 'Mozilla/5.0'})
        try:
            f.write_bytes(urllib.request.urlopen(req, timeout=30).read())
        except urllib.error.HTTPError as e:
            if e.code != 404:
                raise
            return ''  # no issue was sent that day
    return norm(text_of(f.read_text(errors='replace')))


def found(quote: str, body: str) -> bool:
    # an ellipsis marks an elision, so each kept fragment must appear on its own
    parts = [norm(p) for p in re.split(r'…|\.\.\.|\[[^\]]*\]', quote)]
    return all(p in body for p in parts if p)


def main() -> int:
    cache = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.issues')
    cache.mkdir(exist_ok=True)
    page = text_of((pathlib.Path(__file__).parent / 'index.html').read_text())
    bad = 0
    total = 0
    for quote, dates in citations(page):
        total += 1
        if not any(found(quote, issue(d, cache)) for d in dates):
            bad += 1
            print(f'MISSING  {" · ".join(dates)}  "{quote}"')
    print(f'{total - bad}/{total} quotes found in their cited issue')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())

import json
from pathlib import Path
from mismatch import VOCAB, tokens

def gaps(catalog):
    known = set(VOCAB)
    rows = []
    for r in catalog:
        for t in tokens(r.get('title') or ''):
            if t not in known:
                rows.append({'sku': r['sku'], 'token': t})
    return rows

if __name__ == '__main__':
    cat = json.loads(Path('catalog.json').read_text())
    g = gaps(cat)
    Path('vocab_gaps.json').write_text(json.dumps(g, indent=2))
    print('gaps', len(g))
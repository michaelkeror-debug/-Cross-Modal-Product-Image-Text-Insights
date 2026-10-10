import json
from pathlib import Path

def attach(rows):
    out = []
    for r in rows:
        p = Path('audio') / (r['sku'].lower() + '.ogg.txt')
        row = dict(r)
        row['transcript'] = p.read_text().strip() if p.exists() else ''
        out.append(row)
    return out

if __name__ == '__main__':
    rows = json.loads(Path('catalog.json').read_text())
    Path('catalog_with_audio.json').write_text(json.dumps(attach(rows), indent=2))
    print('attached')
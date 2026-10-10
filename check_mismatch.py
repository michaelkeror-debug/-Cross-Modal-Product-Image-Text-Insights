import json
from pathlib import Path

def main() -> int:
    rows = {r['sku']: r for r in json.loads(Path('mismatch_report.json').read_text())}
    a, b = rows['KND-01'], rows['NK-99']
    print('KND-01', a)
    print('NK-99', b)
    if a['flag'] or not b['flag']:
        print('FAIL: expected KND-01 clear and NK-99 flagged')
        return 1
    print('mismatch gold pair OK')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
import hashlib, json
from pathlib import Path

PROMPT = Path('prompts/gen/kiondo_lifestyle_v1.txt')

def main() -> int:
    if not PROMPT.exists():
        print('FAIL prompt file missing:', PROMPT)
        return 1
    sha256 = hashlib.sha256(PROMPT.read_bytes()).hexdigest()
    pin = {"prompt_file": str(PROMPT), "sha256": sha256}
    Path('gen_pin.json').write_text(json.dumps(pin, indent=2))
    print('wrote gen_pin.json')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
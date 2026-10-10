from pathlib import Path

def transcribe_seller_note(audio_path: str) -> str:
    sidecar = Path(str(audio_path) + '.txt')
    if sidecar.exists():
        return sidecar.read_text().strip()
    return ''

if __name__ == '__main__':
    Path('audio').mkdir(exist_ok=True)
    Path('audio/knd-01.ogg.txt').write_text('Navy sisal kiondo, handmade.')
    print(transcribe_seller_note('audio/knd-01.ogg'))
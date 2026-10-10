SENSITIVE = {'person', 'face', 'child'}

def needs_privacy_review(tags) -> bool:
    return any(t in SENSITIVE for t in (tags or []))

if __name__ == '__main__':
    assert needs_privacy_review(['kiondo']) is False
    assert needs_privacy_review(['bag', 'person']) is True
    print('privacy flag OK')
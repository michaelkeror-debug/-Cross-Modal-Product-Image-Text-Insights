# -Cross-Modal-Product-Image-Text-Insights
# Week 10: Advanced Multimodal AI (SokoniHub)

## Overview
SokoniHub joins product images and text: each SKU in `catalog.json` has a title and image tags (read from a photo sidecar), and `mismatch.py` scores how well the title matches the tags and flags likely mismatches, such as a kiondo bag listed under a Nike title. The scores come from a simple bag-of-words stub (`lab-bow-v1`), not a trained model. A CLIP encode pass (`openai/clip-vit-base-patch32`) was run separately as a smoke test and cached in `encode_cache.json`, but it did not produce the scores. The catalog is a teaching slice of 4 SKUs. Audio is optional (transcript sidecars, no Whisper) and image generation uses a stub with provenance metadata.

## Encoder honesty
- encoder_pin.json: `lab-bow-v1` (this is what produced the scores)


## Join
- How to run mismatch.py and check_mismatch.py:
  ```
  python mismatch.py          # writes the report JSON
  python check_mismatch.py    # gold check
  ```
- Gold pair result: KND-01 clear, NK-99 flagged (KND-01 {'sku': 'KND-01', 'score': 1.0, 'flag': False}
NK-99 {'sku': 'NK-99', 'score': 0.0, 'flag': True}
mismatch gold pair OK)

## Insights
- Path to insights.json: `insights.json` (per SKU: score, flag, seller_message, optional transcript)

## Tools
- hf_pipeline.yaml: `hf_pipeline.yaml` (task, model, revision, device)
- DALL-E / SD / stub (circle one): DALL-E / SD / **stub**
- Provenance path: `outputs/knd-01_meta.json` (prompt file + prompt hash, `not_a_photo_of_the_sku: true`); mapping in `gen_twin.json`

## Analytics
- rates.json (quote n): `rates.json`, n = 4 SKUs (per-category and overall flag_rate)
- vocab_gaps: `vocab_gaps.json`, 7 Kenyan product terms missing from the tiny English vocabulary

## Ethics
- Link ethics_note.md: [ethics_note.md](ethics_note.md)
- Review path in one sentence: Flags go to sellers or moderators, titles are never silently rewritten, and nothing is taken down on bag-of-words scores alone.

## Fallbacks declared
- [x] no GPU / no transformers (scores use the `lab-bow-v1` stub; CLIP was only a smoke test)
- [x] no OpenAI image key (stub)
- [x] no Whisper (sidecars)
- [x] n is a teaching slice

## Checklist
- [ ] NK-99 flagged, KND-01 clear
- [ ] outputs/ not mixed into gold images/
- [ ] no unhackable claims
- [ ] Weeks 5/7/8/9 reuse documented

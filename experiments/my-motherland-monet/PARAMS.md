# 参数与校验记录

## Round 01

- Use case: `style-transfer`
- Model: `hy-image-v3.5-preview`
- Provider: GMI Cloud
- Mode: reference-guided generation, 1 style-only reference
- Style source: `submission/the-field-i-remember/final.png`
- Uploaded derivative: `references/style-refs/the-field-i-remember-style-1024.jpg`
- Uploaded derivative dimensions: `771x1024`
- Uploaded derivative bytes: `245092`
- Uploaded derivative SHA256: `5f5ca60d295242a80770c9c1cdec2d71e123d2bd8249449305e751c0b45d53e3`
- Prompt: `round-01/prompt.txt`
- Prompt SHA256: `af145bc4521d258d5cf6aca066e6fc99c23a48850a120def8190c846f712ff4f`
- Requested/API-reported size: `1368x1024`
- Actual file pixels: `1360x1024`
- Request ID: `7a9968ec-db05-4bdc-b498-4cd2c34bad89`
- Status: `success`
- Created: `2026-09-29T22:36:41+08:00`
- Updated: `2026-09-29T22:36:58+08:00`
- Output bytes: `2555215`
- Output SHA256: `6ed2ac09e7ab9f1fe73472fc00cd9f09e6f7154fecaeb44be36fa58bc7a67bf7`
- Calls made: `1`

## Round 02

- Use case: `style-transfer`
- Targeted change: expand one intimate riverside home into a continuous shared homeland without political symbols
- Model: `hy-image-v3.5-preview`
- Provider: GMI Cloud
- Mode: reference-guided generation, 2 references
- Reference 1 role: Round 01 content continuity
- Reference 1: `references/style-refs/my-motherland-round-01-1024.jpg`
- Reference 1 dimensions: `1024x771`
- Reference 1 bytes: `236838`
- Reference 1 SHA256: `bcc5dc77ca49c503c4f78ee210f717ec639971a1af4ef0ce5f51d939fffd65d9`
- Reference 2 role: soft Impressionist visual language only
- Reference 2 source: `submission/the-field-i-remember/final.png`
- Reference 2 uploaded derivative: `references/style-refs/the-field-i-remember-style-1024.jpg`
- Reference 2 SHA256: `5f5ca60d295242a80770c9c1cdec2d71e123d2bd8249449305e751c0b45d53e3`
- Prompt: `round-02/prompt.txt`
- Prompt SHA256: `2631ae4401ac14de57e8cf52b9b86befedcd230a0fa0492789934d6e0b810bcb`
- Requested/API-reported size: `1368x1024`
- Actual file pixels: `1360x1024`
- Request ID: `fa537fcb-5153-40d9-9a95-600d974575da`
- Status: `success`
- Created: `2026-09-30T08:46:02+08:00`
- Updated: `2026-09-30T08:46:50+08:00`
- Output bytes: `2231364`
- Output SHA256: `c8e9dbb699f57a50238002fa09eff60fa9fb9a422660b30f0dcbb57f6f7f2fe0`
- Calls made: `1`

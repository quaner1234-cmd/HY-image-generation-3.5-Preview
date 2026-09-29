# Provenance — The Field I Remember

## Final artifact

- File: `final.png`
- Selected source: `experiments/reference-replication-09-41-42/round-04/01.png`
- SHA-256: `2574488dcc7873cd5eac764880b54c289d9c906547eddbd209bc340e26a376b1`
- File bytes: `2,595,726`
- Actual file pixels: `1024 × 1360`
- Visual post-processing after generation: none
- Copy method: binary file copy; hash verified after copying

## Generation request

- Provider/source: GMI Cloud
- Endpoint: `https://console.gmicloud.ai/api/v1/ie/requestqueue/apikey/requests`
- Model: `hy-image-v3.5-preview`
- Mode: reference-guided image generation/editing with two references
- Request ID: `fd219d7d-bfa7-401a-8633-7342106ae10e`
- Status: `success`
- Requested/API-reported size: `1024 × 1368`
- Actual downloaded file size: `1024 × 1360`
- Created: `2026-09-29T11:49:13+08:00`
- Updated: `2026-09-29T11:49:35+08:00`
- Local file written: `2026-09-29T11:49:37+08:00`
- Campaign window: `2026-09-25` through `2026-10-01`
- Window check: **PASS** — the request was created during the campaign window
- Full response JSON: `experiments/reference-replication-09-41-42/round-04/01.json`
- Original provenance record: `experiments/reference-replication-09-41-42/round-04/01.png.provenance.md`
- Exact prompt: `FINAL_PROMPT.txt` and `experiments/reference-replication-09-41-42/round-04/prompt.txt`

## Request inputs

1. `references/style-refs/style-2026-09-29-09_41_42-AM-1.jpg`
   - Role: composition/content reference
   - Pixels: `768 × 1024`
   - Bytes: `375,566`
   - Origin: compressed copy of the user-supplied file `ChatGPT Image Sep 29, 2026, 09_41_42 AM-1.png`
2. `references/style-refs/monet-houses-parliament-sunset-nga-1024.jpg`
   - Role: style-only reference
   - Pixels: `1024 × 904`
   - Bytes: `242,251`
   - Source: National Gallery of Art, Claude Monet, *The Houses of Parliament, Sunset* (1903), public domain

The original hometown photograph was an upstream source for the exploration, but it was **not directly uploaded in the final GMI request**. The final request used the intermediate composition reference listed above.

## Original photograph

- Package file: `source-photo.jpg`
- Source path: `references/ChatGPT Image Sep 28, 2026, 04_31_58 PM.jpg`
- Author: user / entrant
- SHA-256: `3a849539e636c49d651040a8c829f24a5c451418847d50b1ae4997a27376ea16`
- Bytes: `717,945`
- Pixels: `1152 × 1536`
- Captured/generated timestamp metadata: **UNKNOWN**
- Local file timestamp: `2026-09-28T16:31:59+08:00`

## Attribution limits

- Supporting tools/models used during visual-language exploration: present, but exact model identities are **UNKNOWN** where not recorded.
- Final generation/refinement model: verified as `hy-image-v3.5-preview` through GMI Cloud.
- No API key, account email, or private credential is stored in this package.

## Public-release privacy check

The source photograph is included intentionally for judging and provenance. It contains no visible people, address, license plate, or other direct personal identifier. Its embedded metadata contains no GPS coordinates, capture time, device make, device model, or author name. It does show ordinary, recognizable rural infrastructure; publication of that visual context is part of the entrant's submission decision.

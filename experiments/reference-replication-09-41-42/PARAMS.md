# 参数与校验记录

- Model: `hy-image-v3.5-preview`
- Mode: image-to-image, 1 reference
- Reference source: user-supplied file `ChatGPT Image Sep 29, 2026, 09_41_42 AM-1.png`
- Reference source dimensions: `1086x1448`
- Uploaded reference: `references/style-refs/style-2026-09-29-09_41_42-AM-1.jpg`
- Uploaded reference dimensions: `768x1024`
- Uploaded reference bytes: `375566`
- Prompt: `round-01/prompt.txt`
- Requested size: `1024x1368`
- API-reported size: `1024x1368`
- File pixel size: `1024x1360`
- Elapsed: `26.8s`
- Request ID: `49d1a512-0e2f-46ea-a4e4-cd43afa214ff`
- Status: `success`
- Output bytes: `2761464`
- Output SHA256: `927de54b9af20bfe9d107d31d15b7bead467f95c7eb79b5d1c71f08c4583150c`
- Full-image edge correlation vs source: `0.851` (`same`)
- Center 70% edge correlation vs source: `0.726` (`same`)
- Recovery: not used
- Calls made: 1

## Round 02

- Model: `hy-image-v3.5-preview`
- Mode: image-to-image, 1 reference
- Reference: `references/style-refs/style-2026-09-29-09_41_42-AM-1.jpg`
- Prompt: `round-02/prompt.txt`
- Requested size: `1024x1368`
- File pixel size: `1024x1360`
- Elapsed: `26.5s`
- Request ID: `4da9836a-6180-4b1f-97db-c5c3e119f358`
- Status: `success`
- Output bytes: `2824604`
- Output SHA256: `3c5440f466286bf5bf85f9777b49f3dafb213f47c6a359166ef2c886a4026b59`
- Full-image edge correlation vs source: `0.627` (`same`)
- Recovery: not used

## Round 03

- Model: `hy-image-v3.5-preview`
- Mode: text-to-image, no reference
- Prompt: `round-03/prompt.txt`
- Requested size: `1024x1368`
- File pixel size: `1024x1360`
- Elapsed: `22.5s`
- Request ID: `6fff0b3e-fe16-4814-96a8-383b1f27ed26`
- Status: `success`
- Output bytes: `2653842`
- Output SHA256: `bc6775c527390712fbd72036fa8d5ddab3316ac52089d1192c08d524472f3fa1`
- Recovery: not used

## Round 04

- Model: `hy-image-v3.5-preview`
- Mode: image-to-image, 2 references
- Reference 1: `references/style-refs/style-2026-09-29-09_41_42-AM-1.jpg` (`768x1024`, `375566` bytes), composition/content
- Reference 2: `references/style-refs/monet-houses-parliament-sunset-nga-1024.jpg` (`1024x904`, `242251` bytes), Monet style only
- Reference 2 source: National Gallery of Art open-access IIIF, *The Houses of Parliament, Sunset*, accession `1963.10.48`
- Prompt: `round-04/prompt.txt`
- Requested size: `1024x1368`
- File pixel size: `1024x1360`
- Elapsed: `24.0s`
- Request ID: `fd219d7d-bfa7-401a-8633-7342106ae10e`
- Status: `success`
- Output bytes: `2595726`
- Output SHA256: `2574488dcc7873cd5eac764880b54c289d9c906547eddbd209bc340e26a376b1`
- Full-image edge correlation vs source: `0.331` (`drifted`)
- Center 70% edge correlation vs source: `0.245` (`different`)
- Recovery: not used
- Monet experiment calls made: 3

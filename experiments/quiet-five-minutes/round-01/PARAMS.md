# Quiet Five Minutes — Round 01 参数记录（只记录，不评价）

> 与现有所有参赛 concept 无关的独立创作实验。
> 本轮 Cline 未做任何视觉评价、排名与下一轮方案。

- 模型：`hy-image-v3.5-preview`（经 GMI Cloud）
- 模式：text-to-image，无 reference（`--ref` 未使用）
- Prompt：`prompt.txt`（逐字原文，四次完全相同，未补充任何视觉方案/构图/风格/物体/摄影参数）
- 尺寸：`1024x1024`（gen.py 默认；未传 `--size`、`--max-pixels`）
- 时间：2026-09-28 20:48–20:52 (+0800)

| 文件 | request_id | 尺寸 | bytes | elapsed |
|---|---|---|---|---|
| 01.png / 01.json | 96fba98a-7bef-41ba-9a19-16d957f4c5f7 | 1024x1024 | 2071578 | 22.1s |
| 02.png / 02.json | 6b05d813-d44a-4a94-81ec-3153a8502195 | 1024x1024 | 1722104 | 17.8s |
| 03.png / 03.json | 826da8e7-b76a-4625-8f54-657ac6657b8d | 1024x1024 | 1856451 | 23.8s |
| 04.png / 04.json | 398e51a1-f391-4d42-a08d-d879c6d9cebe | 1024x1024 | 2026249 | 19.9s |

- 附带文件：每个 PNG 有同名 `.json`（完整 API 响应）与 `.png.provenance.md`（模型/时间/request-id/尺寸/状态）。
- 校验：4 张 SHA256 互不相同，Pillow 确认均为 1024x1024 RGB 有效 PNG。
- 状态：Raw / Unreviewed。生成完成后已停止，无评价、无排名、无下一轮方案。

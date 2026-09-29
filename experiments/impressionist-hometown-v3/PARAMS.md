# 印象派转译 v3 — 参数与校验记录（只记事实，不评价）

> 配套：`README.md`（参考图登记、复刻路线、人眼检查）
> 状态：**Raw / Unreviewed**。生成完毕即停止，无评价、无排名、无下一轮方案。

## 1. 调用参数

- 模型：`hy-image-v3.5-preview`（GMI Cloud，endpoint 见 `gen.py`）
- 模式：**image-to-image**，参考图按顺序提交（见下表）；prompt 用 UTF-8 读取后 `import gen` 调用
- 请求尺寸：`1024x1368`（竖版）→ **实际交付 1024×1360**，见第 3 节
- 参考图：原照片 `references/ChatGPT Image Sep 28, 2026, 04_32_33 PM.jpg`（614 KB）
  ＋你给的风格图的等比例副本 `references/style-refs/style-…AM-5.jpg`（378 KB）、`…AM-4.jpg`（360 KB）
  ——副本规则：长边 1024、JPEG q92，放在 `references/` 下（与原始照片一样**不入库**）
- 生成时间：2026-09-29 09:57–10:01（+0800，本机）

## 2. 四张产物

| 目录 | 提交的参考图 | request_id | bytes | elapsed | sha256(前16) | 来源 |
|---|---|---|---|---|---|---|
| `01-photo-plus-style-ref/` | 照片 ＋ AM-5 | 23d4c757-ba61-4052-bd42-74dd1ead48c2 | 2888806 | 27.0s(服务端) | e115b2543cecbc31 | 找回 |
| `02-boost-over-ref/` | 照片 ＋ AM-5 | 9ed84312-742a-49f0-9d07-a0e967fea0b5 | 2825883 | 57.0s(服务端) | e83785b8859d2923 | 找回 |
| `03-text-only-style/` | 照片 | 0e85d6c3-0759-4d7c-8257-1782ed66de09 | 2910605 | 22.5s | 85b80efad457351d | 一次跑完 |
| `04-two-style-refs/` | 照片 ＋ AM-5 ＋ AM-4 | df56bbdf-2f21-449e-836c-b74609c5419d | 2885768 | 28.0s(服务端) | 077779aff3e8f970 | 找回 |

"找回" = 前台命令撞 30s 上限被杀，但服务端已 success，随后从历史请求列表取回（未重跑，`recovered: true`）。

## 3. 尺寸：请求值 ≠ 实际像素（沿用 v2 的结论）

- 请求 `1024x1368`，API 响应 `outcome.media_urls[0].width/height` 也报 1024/1368，但下载到的文件是 **1024×1360**（接口把长边向下对齐到 16 的倍数）。
- 四张 `.json` 同时存 `dimensions`（文件实际像素）与 `api_metadata_size`（API 元数据值）；provenance 里是 `Size` / `Size-Reported-By-API` 两行。
- 本轮发现并修正：`recover.py` 早先写出的记录漏了 `api_metadata_size` 字段，已补齐（脚本加固 + 本次 3 个找回产物回填），现在四份记录的字段集合一致。

## 4. 上传体积与超时找回（本轮关键实测）

参考图上传体积直接决定前台命令能否在 30s 内跑完：

| 参考图体积 | 样本 | 结果 |
|---|---|---|
| 1 张，614 KB | `03-text-only-style` | 22.5s 一次跑完 |
| 2 张，约 1.0 MB | `01`、`02` | 前台被 30s 上限杀掉（服务端 success） |
| 3 张，约 1.35 MB | `04` | 前台被 30s 上限杀掉（服务端 success） |

找回过程（全部成功，零重跑）：

- `01`、`02`：`python recover.py _tmp_jobs_v3.json <key>`（当时列表 `limit=8` 还能在 30s 内拉回）；
- `04`：`recover.py` 的**列表拉取本身也超时**——列表响应里带参考图 base64，含 3 张参考图的条目约 1.9 MB。改为两步走：
  `python recover.py _tmp_jobs_v3.json 04-two-style-refs --limit 1 --list-only`（拉列表并缓存到 `_recover_cache.json`）
  → `python recover.py _tmp_jobs_v3.json 04-two-style-refs --from-cache`（从缓存落盘，只下载结果 PNG）。
- `recover.py` 为此升级：新增 `--limit N` / `--list-only` / `--from-cache`；命中项的 `outcome.media_urls` 已存在时不再额外拉详情（省掉一次大响应往返）。
- **结论**：带 2 张及以上参考图时，默认预期前台超时，直接按两步找回流程走。

## 5. 两两像素差异

缩放到 256×340 后在 0–255 尺度上计算 MAE / RMS（数值越大差异越大）：

| 对比 | MAE | RMS |
|---|---|---|
| **01-photo-plus-style-ref vs 02-boost-over-ref** | **9.83** | **13.58** |
| 01-photo-plus-style-ref vs 04-two-style-refs | 21.86 | 30.83 |
| 02-boost-over-ref vs 04-two-style-refs | 20.69 | 29.19 |
| 02-boost-over-ref vs 03-text-only-style | 22.76 | 31.22 |
| 01-photo-plus-style-ref vs 03-text-only-style | 24.54 | 33.44 |
| 03-text-only-style vs 04-two-style-refs | 27.57 | 36.25 |

- 事实一：`01` 与 `02`（同一组参考图、prompt 不同）差异约为其余各对的一半 —— 同一张风格参考图主导了输出。
- 事实二：`03`（不给风格图）与 `01`／`02` 的差异（22.8／24.5）明显大于 `01` 与 `02` 之间（9.8）—— 给不给风格图，比 prompt 怎么调，影响更大。

与你的风格参考图 `AM-5` 的粗略对比（缩放到同尺寸后 MAE）：01 = 35.34、02 = 35.73、03 = 39.55、04 = 34.81。
**注意**：`AM-5` 与本轮输出虽然同场景，但构图不同（它的太阳更偏左、地块划分不同），这组数字里混着构图差异，只能当作粗略参考，不能读成"风格像不像"。

## 6. 已知限制

- 本轮四条路线的产图差异偏小（`01`／`02` 近乎重复）；想拉开差距需要改的是**风格目标本身**，而不是参考图数量或 prompt 措辞。
- 尺寸统一为 1024×1360（3:4 竖版），未做横版或更大尺寸变体。
- 审美判断需人眼完成（GMI 视觉模型因账户余额不足不可用，本机 Windows 无 OCR 工具，仓库 `ocr` 为 macOS-only）。

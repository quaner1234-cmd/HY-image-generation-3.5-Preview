# 印象派转译 v2 — 参数与校验记录（只记事实，不评价）

> 配套：`README.md`（选图理由与清单）
> 状态：**Raw / Unreviewed**。生成完毕即停止，无评价、无排名、无下一轮方案。

## 1. 调用参数

- 模型：`hy-image-v3.5-preview`（GMI Cloud，endpoint 见 `gen.py`）
- 模式：**image-to-image**，参考图 = 原照片 `references/ChatGPT Image Sep 28, 2026, 04_32_33 PM.jpg`（四张完全相同）
- 请求尺寸：`1024x1368`（竖版）→ **实际交付 1024×1360**，见第 3 节
- prompt：中文长文本，四份各自独立（结构相同、"画面决策"部分不同），写进各自 `prompt.txt`，UTF-8 读取后 `import gen` 调用
- 生成时间：2026-09-29 10:49–11:01（+0800，本机）

## 2. 四张产物

| 文件 | 方向 | request_id | bytes | elapsed | sha256(前16) |
|---|---|---|---|---|---|
| `01-light/light.png` | 光感优先 | 3f3fcd94-8508-4b4a-86f6-d24c59cd2a55 | 2474052 | 23.0s | 97ae4c36e574addf |
| `02-color/color.png` | 色彩优先 | 80706639-7cc7-49e4-946e-4856436d5b59 | 2489784 | 21.0s | 5826e0b6fda2ae35 |
| `03-brushwork/brushwork.png` | 笔触优先 | 71b98ef8-6a42-4cff-aa8a-e68d7f30a8d5 | 2695211 | 79.0s(服务端，含排队) | d1d474e0f28980d0 |
| `04-completion/completion.png` | 完成度优先 | 3c9ed057-ccd4-4934-a7dd-2be641e46ca5 | 2404654 | 25.0s | 9158cec1dd7d5c7d |

## 3. 尺寸：请求值 ≠ 实际像素（重要）

- 请求 `1024x1368`，API 响应里 `outcome.media_urls[0].width/height` 也报 `1024/1368`，但**下载到的文件实际是 1024×1360**。
- 判断：该接口把长边向下对齐到 16 的倍数（1368 → 1360）。
- 因此本目录所有记录（`.json` 的 `dimensions`、`.provenance.md` 的 `Size`/`Size-Note`）一律以**文件实际像素**为准，并存下 API 元数据值作为对照。
- 同一问题在上一轮（`../impressionist-hometown/`）的记录里存在：那 6 份 provenance 原先把 API 值 1024x1368 当作实际尺寸，已于 2026-09-29 修正为 1024x1360 并加 `Size-Note` 说明；`PARAMS.md` 与 `README.md` 的相应描述同步更正。
- `recover.py` 已同步加固：下载后用 Pillow 读实际像素，不再直接采信 API 元数据。

## 4. 校验结果

- 四张 PNG 均通过 Pillow 读取与 `verify()`；文件字节数、SHA256、实际像素与各自 `.json`、`.provenance.md` 三方一致；
- 四张 SHA256 互不相同；
- 新增"两两像素差"统计（缩放到 256×340 后计算 0–255 尺度上的 MAE / RMS，数值越大差异越大）：

  | 对比 | MAE | RMS |
  |---|---|---|
  | 01-light vs 02-color | 12.87 | 17.85 |
  | 01-light vs 03-brushwork | 12.40 | 18.14 |
  | 01-light vs 04-completion | 11.78 | 17.44 |
  | 02-color vs 03-brushwork | 15.03 | 22.31 |
  | **02-color vs 04-completion** | **6.58** | **8.03** |
  | 03-brushwork vs 04-completion | 15.01 | 22.87 |

  事实：`02-color` 与 `04-completion` 两张高度接近（差异约为其余各对的 1/2），其余各对差异量级相近。

## 5. 中断与找回（如实记录）

- 第 3 张 `03-brushwork` 的前台命令在 30s 上限处被杀；当时该请求在服务端的状态为 `dispatched`（成功但尚未写入结果），
  约 30 秒后变为 `success`，随后用 `python recover.py _tmp_jobs.json 03-brushwork` 找回，**没有重新生成、没有重复消耗**。
  该张的 `.json` 中 `recovered: true`、`elapsed_note` 记录了这一点。
- 其余三张一次成功，无重试。

## 6. 已知限制

- 四张的出图差异幅度有限（同一模型、同一参考图，仅 prompt 的"画面决策"段不同）；上表给出量化事实。
- 尺寸统一为 1024×1360（约 3:4 竖版），未做横版或更大尺寸变体。
- 审美判断需人眼完成（GMI 视觉模型因账户余额不足不可用，本机 Windows 无 OCR 工具，仓库 `ocr` 为 macOS-only）。

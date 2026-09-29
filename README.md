# HY Image Generation 3.5 Preview

GMI Cloud **Hy Image Challenge** 参赛工作区。

- 比赛页：https://www.gmicloud.ai/hy-week
- 截止：**2026-10-01 23:59 PT**（北京时间 10-02 14:59）
- 最终赛道：**Track 2 — Commercial**
- 最终作品：**The Field I Remember**
- 生成模型：`hy-image-v3.5-preview`，经 GMI Cloud 调用

评委入口与最终提交材料见 **[`submission/the-field-i-remember/README.md`](submission/the-field-i-remember/README.md)**。
早期 Track 1 与其他方向的内容作为历史实验保留，不代表最终参赛赛道。

---

## 工具链

| 文件 | 作用 | 备注 |
|---|---|---|
| `gen.py` | 生图 CLI（主入口） | 凭据读环境变量 `GMI_API_KEY`，**不含任何明文凭据** |
| `run.cmd` | Windows 薄包装 | 仅切目录后调用 `gen.py`，参数原样透传 |
| `ocr.swift` → `ocr` | 本机 OCR 客观校验文字 | 用 `swiftc -O ocr.swift -o ocr` 编译；`ocr` 本身已 gitignore |
| `compare.py` | 边缘结构互相关 | 判断主体/版式是否漂移 |
| `eval.py` | GMI 视觉模型评审 | ⚠️ 当前账户余额不足（402），暂不可用 |

> `ocr` 关闭语言纠错（`usesLanguageCorrection = false`），
> 否则 OCR 会用语言模型"猜"出正确拼写，掩盖真实的文字渲染缺陷。

## 目录

| 目录 | 内容 |
|---|---|
| `probe/` | 首轮能力探测 + `FINDINGS.md` 实测基线 |
| `explore/` | 变量对照实验（文字可控性 / 风格一致性 / 参考图编辑） |
| `series/` | 三联画链路测试（独立生成 vs 参考图链式） |
| `concepts/` | 概念方案探索：`national-day-poster/`、`river-awakens/`、`hometown-memory/` (Candidate / Exploring) |
| `submission/` | 最终参赛提交包；当前作品为 `the-field-i-remember/` |
| `歌曲调研-我的祖国/` | 歌曲史实与简谱 |
| `_archive/` | 已弃用研究材料，仅为可追溯保留 |

## 文档

- `RESEARCH.md` — 混元生图能力调研（含独立榜单反证、参考图编辑实测）
- `RESEARCH-hy-image-35-positioning.md` — **官方定位与能力设计研究**（含赛事背景；官方事实 / 第三方观察 / 推论 三级标注）
- `probe/FINDINGS.md` — 能力实测基线
- `我的祖国_歌曲全面研究.md` — 创作素材调研

## 凭据

所有脚本通过 macOS Keychain 读取 `GMI_API_KEY`（service = `GMI_API_KEY`）：

```bash
security find-generic-password -a "$USER" -s "GMI_API_KEY" -w
```

**仓库内不含任何密钥、令牌或邮箱。**

### Windows PowerShell

凭据读取优先级：`gen.py` / `eval.py` 一致 —— 先读环境变量 `GMI_API_KEY`，未设置且系统为 macOS 时才回退 Keychain。

```powershell
# 当前会话生效
$env:GMI_API_KEY = "<你的 key>"

# 永久生效（重开终端后可用）
setx GMI_API_KEY "<你的 key>"
```

生图（默认模型 `hy-image-v3.5-preview`，默认输出到 `outputs/`）：

```powershell
# 方式一：直接跑主入口
python gen.py --prompt "a red apple on a wooden table"

# 方式二：薄包装（等价，自动定位仓库目录）
.\run.cmd --prompt "a red apple on a wooden table"
```

其他参数：

```powershell
python gen.py --prompt "..." --size 1920x1080 --out concepts\poster.png
python gen.py --prompt "..." --ref a.png --ref b.png --out edit.png
python gen.py --prompt "..." --max-pixels 4194304
```

> 省略 `--out` 时自动写入仓库内 `outputs/hy-<时间戳>.png`（该目录已 gitignore）。

### macOS

```bash
export GMI_API_KEY="$(security find-generic-password -a "$USER" -s GMI_API_KEY -w)"
python3 gen.py --prompt "a red apple on a wooden table"
```

> 依赖：`gen.py` 仅用 Python 标准库（建议 3.9+）；`compare.py` 需要 `numpy` + `Pillow`；
> `ocr.swift` 需要 Swift 工具链，用 `swiftc -O ocr.swift -o ocr` 编译。

## 已知限制

- `*.json` 响应中的 GCS 链接含账号 `ownerId` 路径段（该链接本身即为公开分享地址）
- GMI 上游视觉模型因账户余额不足不可用，审美判断需人工完成

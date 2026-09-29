# AGENTS.md — HY-image-generation-3.5-Preview

## 仓库用途
Hy Image 3.5 preview（GMI Cloud）生图实验工作区。核心脚本：`gen.py`（生图 CLI）、`eval.py`、`compare.py`。
实验产物放在 `experiments/<实验名>/round-NN/`，每轮包含 `prompt.txt`、`PARAMS.md`、`NN.png` + `NN.json` + `NN.png.provenance.md`。
凭据：环境变量 `GMI_API_KEY`（Windows 亦会读用户环境变量）。不落盘、不打印、绝不提交。

## 生图命令
```
python gen.py --prompt "..." --size 1024x1024 --out x.png [--ref a.png ...]
```
prompt 是长中文时不要写在命令行里（PowerShell 引号/编码易错）：把 prompt 写进 `prompt.txt`，
用一次性脚手架脚本以 UTF-8 读取后 `import gen` 调用，跑完删掉脚手架。

## 已知陷阱（2026-09-28 Round 03 实测）
1. 单次生图约 20–23s。**一条命令只生成一张**：把 4 张塞进同一前台命令会超过工具 30s 上限被杀。
2. 不要用 `Start-Process` 把生成脚本丢到后台：本机实测后台进程会残留并在前台重跑之后再次写入同名文件，
   造成 `NN.png` 被覆盖、`NN.json` 的 request_id 与日志不一致的竞态，白烧 API 调用。
3. 提交前核对每个序号的三元组是否自洽：`NN.png` 字节数 == `NN.json` / `NN.png.provenance.md` 里的 `Bytes` 与 `request_id`；
   必要时连续两次算 SHA256 确认无写入者。不一致就重跑该序号，不要提交。
4. 批量生成后删除临时脚手架脚本与日志，别留在仓库里。
5. **网络操作必须串行**：同时发起两个大请求（例如"拉历史请求列表"＋"生图"）会互相拖垮——
   2026-09-29 实测两者先后超时失败（`WinError 10060`）。一条命令只做一件网络事。
6. 前台命令被 30s 上限杀掉 **≠ 生成失败**：服务端往往已经 success。**先找回，不要急着重跑**（见下节）。
7. **参考图数量／体积决定会不会超时**（2026-09-29 v3 实测）：1 张 614 KB → 22.5s 一次跑完；
   2 张约 1.0 MB、3 张约 1.35 MB → 前台命令**全部**被杀（服务端均 success，可完整找回）。
   结论：带 2 张及以上参考图时，直接按"两步找回"流程走，别指望一次跑完；
   外来的风格参考图先压到长边 1024 / JPEG q92（约 360–400 KB／张）再上传。

## 历史请求接口与超时找回（2026-09-29 实测）
- `GET {endpoint}?limit=N`（同一 Bearer key）返回最近 N 条历史请求，字段：
  `request_id` / `status` / `payload`（**含参考图 base64，响应体很大，别整份打印**）/ `outcome.media_urls`（可直接下载）。
- `GET {endpoint}/{request_id}` 取单条详情（注意：末尾多一个斜杠会 404）。
- 被前台超时"丢掉"的结果可原样找回，不必重跑：
  ```
  python recover.py <jobs.json> <job-key>
  ```
  匹配条件 = `status=success` + `size` 相同 + `prompt` 与本地 prompt 文件逐字相同；落盘内容与正常生成一致
  （PNG + 完整响应 JSON + provenance，provenance 标注 `Recovered: yes`）。
- 没有匹配 → 说明该次请求根本没到服务端（连接超时），此时才重跑。
- 需要 `jobs.json`（键 → `prompt`/`out`/`refs`/`size`/`task`），一次一个 key 串行执行。
- `refs` 是**数组**（多参考图，按提交顺序写进 prompt 指代）；provenance 记 `Reference-1` / `Reference-Other`。
- **列表响应会随参考图体积膨胀**：含 3 张参考图的条目约 1.9 MB，此时连 `?limit=8` 的列表拉取本身也会撞 30s 上限。
  改为两步走（2026-09-29 v3 实测有效）：
  ```
  python recover.py <jobs.json> <key> --limit 1 --list-only   # 只拉列表，缓存到 _recover_cache.json
  python recover.py <jobs.json> <key> --from-cache            # 从缓存落盘，只下载结果 PNG
  ```
  命中项若自带 `outcome.media_urls` 就不再拉详情，省掉一次大响应往返。
- `_recover_cache.json` 里含 base64 参考图，很大：用完删除，**绝不提交**。

## 尺寸与目录约定（2026-09-29 实测）
- 实测可用尺寸：`1024x1024`、`1024x1368`（3:4）、`1536x2048`、`2048x1536`、`2048x2048`。
  带参考图时 `1536x2048` 及以上容易撞 30s 上限 → **竖版照片转译统一用 `1024x1368`**（19–22s 稳定跑完）。
- 照片转译类任务目录约定：`experiments/<实验名>/<A|B|C>/`，每张照片一个目录（字母 ↔ 源照片映射写在
  实验级 `README.md`），目录内放 `prompt-conservative.txt` / `prompt-expressive.txt` 与
  `conservative.png|.json|.provenance.md`、`expressive.png|.json|.provenance.md`；
  实验级 `README.md` 记录选图理由与交付清单，`PARAMS.md` 记录参数、校验与过程中断记录。
- 方向型实验（同一张照片的多个处理方向）目录约定：`experiments/<实验名>/<NN-direction>/`，内部
  `prompt.txt` + `<direction>.png|.json|.provenance.md`；实验级 `README.md`（选图理由＋方向说明＋清单）与
  `PARAMS.md`（参数、校验、两两像素差异统计、中断记录）。例：`experiments/impressionist-hometown-v2/`。
- **用户提供的"风格参考图／目标图"**（例如"照这 5 张的样子复刻"）副本放 `references/style-refs/`，
  与原始照片同在 `references/` 下、**不入库**；上传前压到长边 1024 / JPEG q92，
  文件名保留用户原始时间戳（如 `style-09_41_53_AM-5.jpg`）以便溯源。
  用法见 `experiments/impressionist-hometown-v3/`（照片＋风格图、双风格图、纯文字三条路线对照）。
- **请求尺寸 ≠ 实际像素**（2026-09-29 实测）：请求 `1024x1368` 时，API 响应里的 `media_urls[].width/height`
  也报 1368，但下载到的文件是 **1024×1360**（接口把长边向下对齐到 16 的倍数）。
  一律用 Pillow 读**文件实际像素**再写进 `.json` / provenance，不要把 API 元数据当尺寸记录；
  `recover.py` 已按此加固。


## 实验协议（用户约定）
- 每轮同一 prompt 生成 4 张，保留原图 + 完整响应 JSON + provenance（Agent/Task/Session/模型/时间/request-id/状态）。
- `PARAMS.md` 只记录参数与校验事实（模型、ref、prompt 构成、尺寸、时间、request_id），
  **不写评价、不写排名、不写下一轮方案**。
- 生成完成即停止，等用户给反馈；下一轮方向由用户决定。

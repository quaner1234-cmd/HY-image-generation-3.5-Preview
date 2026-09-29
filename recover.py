#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 GMI Cloud 的历史请求列表中找回被前台 30s 超时中断的生成结果。

为什么需要它：单次生图约 19–25s，加上参考图上传后很容易撞上工具/终端 30s 上限。
前台命令被杀 ≠ 生成失败——服务端往往已经 success。直接重跑会白烧一次 API 调用。

用法:
  python recover.py <jobs.json> <job-key>                     # 常规：拉最近 8 条并落盘
  python recover.py <jobs.json> <job-key> --limit 3           # 控制列表条数（参考图越多、响应越大）
  python recover.py <jobs.json> <job-key> --limit 1 --list-only   # 只拉列表并缓存，打印摘要
  python recover.py <jobs.json> <job-key> --from-cache        # 从缓存列表落盘（响应太大时分两步走）

列表响应会缓存到 `_recover_cache.json`（含 base64 参考图，很大；用完请删除，且绝不提交）。
若命中项自带 `outcome.media_urls` 则不再额外拉取详情，避免又一次大响应往返。

jobs.json 结构（键 → 任务）:
{
  "A-conservative": {
    "prompt": "experiments/xxx/A/prompt-conservative.txt",
    "out":    "experiments/xxx/A/conservative.png",
    "ref":    "references/photo.jpg",            # 单参考图
    "refs":   ["references/photo.jpg", "..."],   # 或：多参考图（按顺序提交，优先使用）
    "size":   "1024x1368",
    "task":   "…provenance 里的任务名…"
  }
}

匹配规则：status=success + size 相同 + payload.prompt 与本地 prompt 文件逐字相同 + 本地尚无产物。
落盘内容与正常生成完全一致：PNG + 记录 JSON + `<png>.png.provenance.md`（标注 Recovered: yes）。

凭据同 gen.py：环境变量 `GMI_API_KEY`（Windows 亦读用户环境变量），不落盘、不打印明文。
"""
import hashlib
import json
import os
import sys
import time
import urllib.request

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

import gen  # noqa: E402


def api_get(url, apikey, timeout=30):
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + apikey})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_recover_cache.json")


def parse_args(argv):
    positional, limit, list_only, from_cache = [], 8, False, False
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--list-only":
            list_only = True
        elif a == "--from-cache":
            from_cache = True
        elif a == "--limit":
            i += 1
            limit = int(argv[i])
        elif a.startswith("--limit="):
            limit = int(a.split("=", 1)[1])
        else:
            positional.append(a)
        i += 1
    if len(positional) != 2:
        sys.exit(__doc__)
    return positional[0], positional[1], limit, list_only, from_cache


def summarize(items):
    for it in items:
        p = it.get("payload") or {}
        media = (it.get("outcome") or {}).get("media_urls") or []
        print("%s | %-10s | %-10s | media=%d | %s" % (
            str(it.get("request_id"))[:8], str(it.get("status")), str(p.get("size")),
            len(media), (p.get("prompt") or "").replace("\n", " ")[:24]))


def main():
    jobs_file, job_key, limit, list_only, from_cache = parse_args(sys.argv[1:])
    with open(jobs_file, encoding="utf-8") as f:
        job = json.load(f)[job_key]

    prompt = open(job["prompt"], encoding="utf-8").read().strip()
    refs = job.get("refs") or ([job["ref"]] if job.get("ref") else [])
    out_png = job["out"]
    base = out_png[:-4] if out_png.lower().endswith(".png") else out_png

    if not list_only and os.path.exists(out_png) and os.path.exists(base + ".png.provenance.md"):
        print("ALREADY PRESENT (delete it first if you really want to recover): " + out_png)
        return

    apikey = None if from_cache else gen.get_key()

    if from_cache:
        with open(CACHE, encoding="utf-8") as f:
            listing = json.load(f)
        print("using cached list: " + CACHE)
    else:
        listing = api_get(gen.ENDPOINT + "?limit=%d" % limit, apikey)
        with open(CACHE, "w", encoding="utf-8") as f:
            json.dump(listing, f)
        print("fetched up to %d request(s), cached to %s" % (limit, CACHE))

    items = listing.get("requests") if isinstance(listing, dict) else listing
    if list_only:
        summarize(items)
        return

    hit = None
    for it in items:
        payload = it.get("payload") or {}
        media = (it.get("outcome") or {}).get("media_urls") or []
        if (it.get("status") == "success"
                and payload.get("size") == job["size"]
                and (payload.get("prompt") or "").strip() == prompt
                and media):
            hit = it
            break

    if hit is None:
        print("NOT FOUND for key=" + job_key +
              " —— 请求可能还在处理中（dispatched）或根本没到服务端。")
        sys.exit(1)

    rid = hit["request_id"]
    media = (hit.get("outcome") or {}).get("media_urls") or []
    if media:
        detail = hit          # 列表项已带 media_urls，省掉一次大响应往返
    else:
        try:
            detail = api_get(gen.ENDPOINT + "/" + rid, apikey or gen.get_key())
        except Exception as exc:  # noqa: BLE001
            print("detail fetch failed (" + str(exc)[:120] + "), falling back to the list item")
            detail = hit

    media = detail["outcome"]["media_urls"][0]
    api_w, api_h = media.get("width"), media.get("height")
    nbytes = gen.download(media["url"], out_png)
    with Image.open(out_png) as im:   # 实测 API 元数据不等于实际像素（1368 vs 1360），以文件为准
        w, h = im.size
    if (api_w, api_h) != (w, h):
        print("NOTE: API metadata %sx%s != file pixels %dx%d (using the file)" % (api_w, api_h, w, h))
    digest = sha256(out_png)

    # 剥掉回显的参考图 base64，保持 JSON 体量与正常生成的响应一致
    if isinstance(detail.get("payload"), dict):
        detail["payload"].pop("image", None)

    elapsed = None
    if hit.get("created_at") and hit.get("updated_at"):
        try:
            elapsed = round(float(hit["updated_at"]) - float(hit["created_at"]), 1)
        except (TypeError, ValueError):
            elapsed = None

    # 与正常生成产出的 JSON 保持同一结构，便于统一校验
    record = {
        "job": job_key,
        "task": job.get("task"),
        "request_id": rid,
        "status": detail.get("status"),
        "model": detail.get("model", gen.MODEL),
        "size": job["size"],
        "references": refs,
        "prompt_file": os.path.basename(job["prompt"]),
        "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "elapsed_seconds": elapsed,
        "elapsed_note": "server side; the foreground command hit the 30s limit and the result was "
                        "retrieved from the request list instead of being re-generated",
        "recovered": True,
        "bytes": nbytes,
        "dimensions": "%dx%d" % (w, h),
        "api_metadata_size": "%sx%s" % (api_w, api_h),
        "sha256": digest,
        "output": os.path.basename(out_png),
        "media_url": media["url"],
        "raw_response": detail,
    }
    with open(base + ".json", "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, ensure_ascii=False)

    prov = "\n".join([
        "Agent: Cline",
        "Task: " + job["task"],
        "Session: unavailable",
        "Time: " + time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "Model: hy-image-v3.5-preview",
        "Mode: image-to-image (" + str(len(refs)) + " reference(s))",
        "Reference-1: " + (refs[0] if refs else "-"),
        "Reference-Other: " + ("; ".join(refs[1:]) if len(refs) > 1 else "-"),
        "Size: " + str(w) + "x" + str(h) + " (file pixels)",
        "Size-Reported-By-API: " + str(api_w) + "x" + str(api_h) + " (metadata value only)",
        "Request-ID: " + str(rid),
        "Prompt-File: " + os.path.basename(job["prompt"]),
        "Elapsed: " + (("%.1fs (server side)" % elapsed) if elapsed is not None
                       else "(recovered from request list)"),
        "Bytes: " + str(nbytes),
        "Dimensions: " + str(w) + "x" + str(h),
        "SHA256: " + digest,
        "Output: " + os.path.basename(out_png),
        "Recovered: yes (original call was cut off by the 30s foreground limit; "
        "the result was retrieved from the request list, not re-generated)",
        "Status: Raw / Unreviewed",
        "",
    ])
    with open(base + ".png.provenance.md", "w", encoding="utf-8") as f:
        f.write(prov)

    print("RECOVERED " + job_key + " " + out_png + " " + str(w) + "x" + str(h) +
          " " + str(nbytes) + " bytes  request_id=" + rid)
    print("   sha256=" + digest[:16])


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Hy Image 3.5 preview (GMI Cloud) 生图 CLI — Hy Image Challenge 工作区专用

凭据: 先读环境变量 GMI_API_KEY；未设置且系统为 macOS 时，回退 Keychain
      (service = "GMI_API_KEY")。不落盘、不打印明文。

用法:
  python gen.py --prompt "..."
  python gen.py --prompt "..." --size 1024x1024 --out foo.png
  python gen.py --prompt "..." --size 1920x1080 --out bar.png --max-pixels 4194304
  python gen.py --prompt "..." --ref a.png --ref b.png --out edit.png
  Windows 亦可直接:  run.cmd --prompt "..."

事实来源:
  endpoint  https://console.gmicloud.ai/api/v1/ie/requestqueue/apikey/requests
  model     hy-image-v3.5-preview
  活动页     https://www.gmicloud.ai/hy-week
"""
import argparse
import base64
import json
import mimetypes
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

ENDPOINT = "https://console.gmicloud.ai/api/v1/ie/requestqueue/apikey/requests"
STATUS_ENDPOINT = "https://console.gmicloud.ai/api/v1/ie/requestqueue/apikey/requests"
MODEL = "hy-image-v3.5-preview"
KEYCHAIN_SERVICE = "GMI_API_KEY"
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUT_DIR = os.path.join(REPO_DIR, "outputs")


def get_key() -> str:
    """凭据优先级: 环境变量 GMI_API_KEY -> Windows 注册表用户环境变量 -> (仅 macOS) Keychain。不打印明文。"""
    key = os.environ.get("GMI_API_KEY", "").strip()
    if key:
        return key

    if sys.platform == "win32":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as k:
                val, _ = winreg.QueryValueEx(k, "GMI_API_KEY")
                if val and str(val).strip():
                    return str(val).strip()
        except Exception:
            pass

    if sys.platform == "darwin":
        r = subprocess.run(
            ["/usr/bin/security", "find-generic-password", "-a", os.environ.get("USER", ""),
             "-s", KEYCHAIN_SERVICE, "-w"],
            capture_output=True, text=True,
        )
        key = r.stdout.strip()
        if key:
            return key

    sys.exit(
        "ERROR: 未找到 GMI_API_KEY。\n"
        "  Windows PowerShell (当前会话):  $env:GMI_API_KEY = \"<你的 key>\"\n"
        "  Windows 永久生效:              setx GMI_API_KEY \"<你的 key>\"\n"
        "  macOS:                         security add-generic-password -a \"$USER\" -s GMI_API_KEY -w \"<你的 key>\""
    )


def default_out() -> str:
    """未指定 --out 时，写入仓库内 outputs/<时间戳>-<短提示>.png。"""
    os.makedirs(DEFAULT_OUT_DIR, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    return os.path.join(DEFAULT_OUT_DIR, f"hy-{stamp}.png")


def data_uri(path: str) -> str:
    mime = mimetypes.guess_type(path)[0] or "image/png"
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()


def post(payload: dict, key: str, model: str = MODEL, timeout: int = 180) -> dict:
    body = {"model": model, "payload": payload}
    req = urllib.request.Request(
        ENDPOINT, data=json.dumps(body).encode(), method="POST",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        body_text = e.read().decode(errors="replace")
        sys.exit(f"ERROR: HTTP {e.code}\n{body_text[:1500]}")


def poll(request_id: str, key: str, max_wait: int = 600) -> dict:
    """该接口通常同步返回 success；此函数仅在返回 queued/processing 时兜底轮询。"""
    deadline = time.time() + max_wait
    while time.time() < deadline:
        req = urllib.request.Request(f"{STATUS_ENDPOINT}/{request_id}",
                                     headers={"Authorization": f"Bearer {key}"})
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.loads(r.read().decode())
        if d.get("status") in ("success", "failed", "error", "cancelled"):
            return d
        time.sleep(5)
    sys.exit("ERROR: 轮询超时")


def download(url: str, out: str) -> int:
    parent = os.path.dirname(os.path.abspath(out))
    if parent:
        os.makedirs(parent, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8"})
    with urllib.request.urlopen(req, timeout=180) as r:
        data = r.read()
    with open(out, "wb") as f:
        f.write(data)
    return len(data)


def main():
    # Windows 控制台默认可能是 GBK/CP1252，遇到生僻字会抛 UnicodeEncodeError
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    p = argparse.ArgumentParser()
    p.add_argument("--prompt", required=True)
    p.add_argument("--size", default="1024x1024")
    p.add_argument("--model", default=MODEL, help=f"默认 {MODEL}")
    p.add_argument("--out", help="输出 PNG 路径；省略则写入 outputs/<时间戳>.png")
    p.add_argument("--ref", action="append", default=[],
                   help="参考图路径，可重复，最多 5 张")
    p.add_argument("--max-pixels", type=int, default=None,
                   help="generate_max_pixels，官方博客示例值 4194304")
    p.add_argument("--json-out", help="同时保存完整响应 JSON")
    args = p.parse_args()

    out_path = args.out or default_out()

    if len(args.ref) > 5:
        sys.exit("ERROR: 官方限制每次调用最多 5 张参考图")

    payload = {"prompt": args.prompt, "size": args.size}
    if args.ref:
        payload["image"] = [data_uri(r) for r in args.ref]
    if args.max_pixels:
        payload["generate_max_pixels"] = args.max_pixels

    key = get_key()
    t0 = time.time()
    resp = post(payload, key, model=args.model)
    rid = resp.get("request_id")

    if resp.get("status") not in ("success", "failed"):
        resp = poll(rid, key)

    elapsed = time.time() - t0
    if resp.get("status") != "success":
        print(f"FAILED after {elapsed:.1f}s")
        print(json.dumps(resp, indent=2)[:2000])
        sys.exit(1)

    media = resp.get("outcome", {}).get("media_urls", [])
    if not media:
        print("FAILED: success 但 outcome.media_urls 为空")
        print(json.dumps(resp, indent=2)[:2000])
        sys.exit(1)

    nbytes = download(media[0]["url"], out_path)
    m = media[0]
    print(f"OK  {out_path}  {m.get('width')}x{m.get('height')}  {nbytes} bytes  {elapsed:.1f}s")
    print(f"    request_id={rid}")
    print(f"    out={os.path.abspath(out_path)}")

    if args.json_out:
        with open(args.json_out, "w") as f:
            json.dump(resp, f, indent=2, ensure_ascii=False)
        print(f"    json -> {args.json_out}")


if __name__ == "__main__":
    main()

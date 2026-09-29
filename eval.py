#!/usr/bin/env python3
"""
图片审视器 — 用 GMI Cloud 上的视觉模型评估生成结果。
主模型（Space Bunny）无读图能力，Track 1 的成败取决于文字/排版是否正确，
因此用独立视觉模型做客观评判，避免凭感觉下结论。

用法:
  ./eval.py probe/A-english-type.png
  ./eval.py probe/A.png --expect "MIDNIGHT STANDARD / OCT 1 — NOV 30"
  ./eval.py *.png --expect "四阶段标签: EVAPORATION, CONDENSATION, PRECIPITATION, COLLECTION"

注意: 视觉模型调用走 GMI 计费通道 (api.gmi-serving.com)，非免费额度。
      默认用 flash-lite，单次成本极低。
"""
import argparse
import base64
import json
import mimetypes
import os
import subprocess
import sys
import urllib.error
import urllib.request

BASE = "https://api.gmi-serving.com/v1/chat/completions"
DEFAULT_MODEL = "google/gemini-3.1-flash-lite-preview"

PROMPT = """You are a strict art director judging AI-generated design work for an
award competition. Analyze the attached image and report ONLY what is actually
visible. Do not be generous. Do not assume the intent of the prompt.

Report in this exact structure:

## 1. TEXT RENDERING (critical)
- List every piece of visible text, transcribed EXACTLY as rendered.
- For each: is it spelled correctly? Are there garbled/merged/fake characters?
- Verdict: PASS / FAIL / N/A (no text present)

## 2. LAYOUT & TYPOGRAPHY
- Hierarchy, alignment, spacing, grid discipline, margins, balance.
- Any overlapping, clipping, or misaligned elements?
- Rate 1-10 with a one-line reason.

## 3. OVERALL DESIGN QUALITY
- Composition, color, craft, print-readiness.
- Rate 1-10 with a one-line reason.

## 4. WEAKNESSES
- Top 3 concrete, fixable problems. Be specific about what and where.

## 5. VERDICT
- One line: would this pass a professional design review? Why/why not."""

EXPECT_TMPL = """
## 0. PROMPT FIDELITY (critical)
The generation prompt asked for exactly this text/content: {expect}
- Transcribe what is ACTUALLY rendered in the image.
- Compare character by character. Mark each required string CORRECT / WRONG / MISSING.
- Verdict: PASS only if all required strings render correctly.
"""


def get_key() -> str:
    """凭据优先级: 环境变量 GMI_API_KEY -> (仅 macOS) Keychain。不打印明文。"""
    key = os.environ.get("GMI_API_KEY", "").strip()
    if key:
        return key

    if sys.platform == "darwin":
        r = subprocess.run(
            ["/usr/bin/security", "find-generic-password", "-a", os.environ.get("USER", ""),
             "-s", "GMI_API_KEY", "-w"],
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


def data_uri(path: str) -> str:
    mime = mimetypes.guess_type(path)[0] or "image/png"
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()


def evaluate(path, expect, model):
    prompt = PROMPT
    if expect:
        prompt = EXPECT_TMPL.format(expect=expect) + prompt
    body = {
        "model": model,
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": data_uri(path)}},
        ]}],
        "max_tokens": 2048,
    }
    req = urllib.request.Request(
        BASE, data=json.dumps(body).encode(), method="POST",
        headers={"Authorization": f"Bearer {get_key()}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            d = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"ERROR: HTTP {e.code}\n{e.read().decode(errors='replace')[:800]}")
    return d["choices"][0]["message"]["content"]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("images", nargs="+")
    p.add_argument("--expect", help="prompt 中要求渲染的确切文字/内容")
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--json-out", help="把所有评估写成 JSON")
    args = p.parse_args()

    results = {}
    for img in args.images:
        print(f"\n{'='*70}\n{img}\n{'='*70}")
        verdict = evaluate(img, args.expect, args.model)
        print(verdict)
        results[img] = verdict

    if args.json_out:
        with open(args.json_out, "w") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\njson -> {args.json_out}")


if __name__ == "__main__":
    main()

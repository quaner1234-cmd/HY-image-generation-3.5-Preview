#!/usr/bin/env python3
"""
图像一致性对比 — 在没有视觉模型的情况下，客观衡量「主体有没有漂移」。

思路:
  1. 灰度 + Sobel 边缘 → 得到「结构图」(与颜色、亮度无关)
  2. 可选中心裁剪 → 隔离画面中心的��体，避开刻意变化的背景
  3. 归一化互相关 → 1.0 完全相同，0 无关，负数=结构被翻转

背景是被刻意改掉的，所以「全图相关性」低不代表主体变了。
判断主体一致性要看 center 指标。

用法:
  ./compare.py a.png b.png c.png          # 逐张与第一张比
  ./compare.py --center 0.5 a.png b.png   # 只比中心 50% 区域
"""
import sys
import numpy as np
from PIL import Image, ImageFilter


def edge_sig(path, center=1.0, n=256):
    im = Image.open(path).convert("L")
    w, h = im.size
    if center < 1.0:
        cw, ch = int(w * center), int(h * center)
        im = im.crop(((w - cw) // 2, (h - ch) // 2, (w + cw) // 2, (h + ch) // 2))
    e = im.filter(ImageFilter.FIND_EDGES).resize((n, n), Image.LANCZOS)
    a = np.asarray(e, dtype=float)
    a -= a.mean()
    return a / (a.std() + 1e-9)


def main():
    args = [a for a in sys.argv[1:]]
    center = 1.0
    if "--center" in args:
        i = args.index("--center")
        center = float(args[i + 1])
        del args[i:i + 2]
    if len(args) < 2:
        sys.exit(__doc__)

    base = args[0]
    print(f"baseline: {base}   (center={center})\n")
    print(f"{'image':<40} {'corr':>8}  {'verdict':<12}")
    print("-" * 64)
    b = edge_sig(base, center)
    for p in args[1:]:
        c = float((b * edge_sig(p, center)).mean())
        verdict = "same" if c > 0.6 else "drifted" if c > 0.3 else "different"
        print(f"{p.split('/')[-1]:<40} {c:>8.3f}  {verdict:<12}")


if __name__ == "__main__":
    main()

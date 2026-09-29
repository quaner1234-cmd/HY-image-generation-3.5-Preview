# 印象派转译 v4 — 全画面重新绘制（单张）

> 目标：用户要求——第一张照片只提供地点／构图／物体关系，第二张风格图只提供绘画语言；
> 整幅画不得有任何照片感，前景叶菜必须概括成有方向、有厚度、有冷暖变化的绿色笔触。
> 生成：2026-09-29（+0800），模型 `hy-image-v3.5-preview`（GMI Cloud）。
> 状态：**Raw / Unreviewed** —— 只记事实，不评价、不排名。

## 交付物

```
experiments/impressionist-hometown-v4/
├── README.md          本文件
└── 01-repaint/        prompt.txt + repaint.png + repaint.json + repaint.png.provenance.md
```

`01-repaint/repaint.png`：1024×1360（请求 1024x1368），原照片 ＋ `references/style-refs/style-09_41_53_AM-5.jpg`
两张参考图，request `508ac125-…`，前台提交后服务端 success、用 `recover.py --limit 2` 落盘（未重跑），
provenance 标注 `Recovered: yes`。

## 人眼检查（只记事实）

- 构图、地点、主要元素（地平线、落日、大树、防风林带、村舍、铁塔、电线杆、菜畦垄沟、前景叶菜）保留；无新增主要景物；无文字／水印／边框。
- **前景近景放大核对**：把照片与新图的前景条带并排放大看，新图的叶菜仍保留叶脉走向、卷边阴影和照片式表面质感，
  笔触感不明显——"把叶菜概括为绿色笔触"这条**没有达到**（天空与远景的笔触化程度高于前景）。
- 整张与 v3 四张同一风格族；与 v3-01 的实测像素差为 MAE 21.47 ／ RMS 31.64——
  与 v3 内部"不同 prompt"各对的量级相当（20–28），明显大于 v3-01／v3-02 这对同配置重抽（9.83）。

# Hy Image Challenge 事实底稿

> 用途：供 DSH 创建比赛工作区、后续查证规则与技术信息。  
> 文档性质：**仅事实整理，不包含选题建议、赛道推荐、创意方向判断或获胜策略。**  
> 核对日期：2026-09-26  
> 主办/联合评审：GMI Cloud + Tencent Hunyuan  
> 官方活动页：https://www.gmicloud.ai/hy-week

---

## 1. 活动概览

活动名称：**Hy Image Challenge**

活动对应模型：**Hy Image 3.5 preview**

活动页顶部给出的活动窗口：

- `2026.09.25 – 2026.10.01`
- 活动页称 `7 Days Free`
- 活动页称该模型在活动期间免费，活动后恢复标准定价
- 官方活动页写明：Hy Image 3.5 preview 在此次活动中通过 **GMI Cloud** 提供

官方活动页：

- https://www.gmicloud.ai/hy-week

注意：

- 活动页没有明确写“9 月 25 日从哪个具体时区、几点开始”。
- 截止时间则明确写为 **October 1, 2026, 11:59 PM PT**。

---

## 2. 截止时间

官方规则写明：

**Submit by October 1, 2026, 11:59 PM PT.**

来源：

- https://www.gmicloud.ai/hy-week

### 时区换算（派生信息）

2026-10-01 美国 Pacific Time 仍处于夏令时，因此为 PDT（UTC-7）。

对应：

- 日本时间 JST（UTC+9）：**2026-10-02 15:59**
- 中国北京时间 CST / UTC+8：**2026-10-02 14:59**

这是时区换算结果，不是活动页原文。

---

## 3. 谁可以参加

活动页原文含义：

- **Anyone, anywhere in the world.**
- 即：任何人、任何地区均可参加。

来源：

- https://www.gmicloud.ai/hy-week

目前公开活动页没有看到：

- 年龄限制
- 指定国家排除列表
- 团队参赛规则
- 每队人数规则

因此不要自行假设团队参赛被允许或禁止；如计划以团队名义参加，应重新检查活动页面或直接向主办方确认。

---

## 4. 每人提交数量

官方写明：

- **One submission per person**
- 每人只能提交一次
- 只能选择一个赛道

活动页同时写明：

- `Three tracks, one submission.`
- `One entry`
- `One submission per person. Pick your track and commit.`

来源：

- https://www.gmicloud.ai/hy-week

---

## 5. 作品时间要求

官方写明：

- 作品必须在此次 **seven-day window** 内制作
- 可提交：
  - **one piece**
  - 或 **one set**
- 只能参加一个 track

原意：

> One piece or one set, one track, made during the seven-day window.

来源：

- https://www.gmicloud.ai/hy-week

因此可确认：

- 单件作品可以提交
- “一组作品 / one set”也在规则允许范围内

活动页没有进一步定义：

- `one set` 最多包含几张图片
- 一组作品是否必须为统一主题
- gallery 的最大图片数量
- 视频最大时长
- 文件大小限制

---

## 6. 三个赛道

### Track 1 — Type & Layout

活动页给出的示例：

- Posters
- Infographics
- Packaging

即：

- 海报
- 信息图
- 包装

来源：

- https://www.gmicloud.ai/hy-week

### Track 2 — Commercial

活动页给出的示例：

- Product shots
- Brand systems
- Ad creative

即：

- 产品视觉 / 产品拍摄类视觉
- 品牌系统
- 广告创意

来源：

- https://www.gmicloud.ai/hy-week

### Track 3 — Game Art

活动页给出的示例：

- Full UI screens
- Character sheets
- Scene concepts

即：

- 完整 UI 页面
- 角色设定图
- 场景概念图

来源：

- https://www.gmicloud.ai/hy-week

---

## 7. 核心模型使用要求

活动页明确写明：

- **Generation runs on Hy Image 3.5 preview served through GMI Cloud.**
- 其他模型可以参与辅助 workflow。

FAQ 再次明确：

- 可以使用其他模型
- 但 generation 必须运行在 **GMI Cloud 提供的 Hy Image 3.5 preview**
- 官方还明确表示，把它与 video model 或 editing model 串联是允许的

来源：

- https://www.gmicloud.ai/hy-week

因此可以确认：

### 必须

核心图像生成必须使用：

`Hy Image 3.5 preview`

并且必须通过：

`GMI Cloud`

### 可以

workflow 中可以存在：

- 其他 AI 模型
- 视频模型
- 编辑模型
- 其他辅助步骤

### 活动页没有禁止

目前公开规则没有写：

- 禁止 Photoshop
- 禁止人工后期
- 禁止代码
- 禁止其他生成模型参与辅助
- 禁止视频化
- 禁止将结果做成 gallery

但“其他工具未被禁止”不等于主办方对所有工具形式做了明确授权；最终资格仍应以最新活动页为准。

---

## 8. 必须展示 Prompt 或 Workflow

活动页写明：

**Show your work — Include the prompt or a description of the workflow.**

提交表单中也存在字段：

**Prompt or workflow description**

因此提交时需要准备：

- Prompt
- 或 workflow description

来源：

- https://www.gmicloud.ai/hy-week

活动页没有规定：

- 必须公开全部 prompt
- 必须提交完整调用参数
- 必须公开源代码
- 必须提供 GitHub repository
- 必须提交 workflow JSON
- 必须公开 API 日志

不要自行添加这些要求。

---

## 9. X 公共发布是参赛要求

官方要求先在 X 发布作品。

要求：

- X post 必须公开
- 必须 tag：
  - `@gmi_cloud`
  - `@TencentHunyuan`
- 提交表单中需要填写：
  - X handle
  - X post URL

官方 FAQ 明确：

- locked/private X account 无法参与评审
- public sharing 是 entry 的一部分

来源：

- https://www.gmicloud.ai/hy-week

---

## 10. 官方提交流程

活动页给出四步：

1. Create a GMI account
2. Make something
3. Post and submit
4. Get judged

更具体地：

### Step 1

创建 GMI Cloud account。

活动期间：

- Hy Image 3.5 preview 对活动开放免费使用

### Step 2

在 7 天窗口内制作作品，并选择一个 track。

### Step 3

先在 X 发布：

- tag `@gmi_cloud`
- tag `@TencentHunyuan`

然后通过活动页表单提交。

### Step 4

GMI Cloud 与 Tencent Hunyuan 共同评审。

来源：

- https://www.gmicloud.ai/hy-week

---

## 11. 提交表单字段

活动页当前可见的表单字段包括：

### Contact

- Full name
- GMI Cloud account email
- Country
- X handle
- Link to your X post

其中 GMI Cloud account email 下方提示：

> The account your generations ran on.

因此应使用实际执行 generation 的 GMI Cloud 账户邮箱。

### Work

- Track
- Title
- Prompt or workflow description
- Link to the work

`Link to the work` 字段提示：

- Image
- gallery
- or short video

因此官方提交表单明确接受作品链接指向：

- 图片
- gallery
- short video

来源：

- https://www.gmicloud.ai/hy-week

---

## 12. 原创声明与授权

提交表单包含以下声明/同意项。

### 原创声明

表单文字：

> This is original work made during the campaign.

这意味着参赛者需要声明：

- 作品为原创
- 作品是在 campaign 期间制作

### 展示授权

表单还包含：

> I give GMI Cloud and Tencent Hunyuan permission to feature this work, including at LA and SF Tech Week.

即表单中包含允许：

- GMI Cloud 展示作品
- Tencent Hunyuan 展示作品
- 包括 LA / SF Tech Week 场景

### 产品更新

还有一个：

- Send me product updates from GMI Cloud

该项在活动页明确标注：

- **Optional**

来源：

- https://www.gmicloud.ai/hy-week

### 未明确项

静态活动页文字没有明确说明：

- “原创声明”checkbox 在网页前端是否技术上必填
- “展示授权”checkbox 在网页前端是否技术上必填

但它们均位于 submission form 的 Consent 区域。

如提交前需要精确确认表单必填状态，应直接打开活动页检查最新表单行为。

---

## 13. 奖项

活动页写明：

- Three tracks
- Three winners
- One winner per track

每位获奖者的奖项列表：

1. **$200 cash prize**
2. **$200 GMI Cloud credits — any model**
3. **$200 GMI Cloud credits — Hy Image models only**
4. **Tech Week feature**

页面宣传总额：

**$1,800 in cash and credits**

计算：

- 每位获奖者现金 + credits = $600
- 3 位获奖者 × $600 = $1,800

来源：

- https://www.gmicloud.ai/hy-week

---

## 14. 奖励发放方式

FAQ 写明：

### Cash

- 通过 **wire transfer** 发放

### GMI Cloud credits

- 通过 **vouchers** 加到获奖账户

来源：

- https://www.gmicloud.ai/hy-week

公开活动页没有看到：

- wire transfer 手续费由谁承担
- 税务责任说明
- voucher 有效期
- credits 是否可转让
- credits 是否可兑换现金

---

## 15. Tech Week 展示存在一处表述差异

活动页奖项区域写：

- `One winner per track. Every winner receives all four.`

其中第四项是：

- Tech Week feature

但 FAQ 又写：

> Selected work may be shown at Tencent Hunyuan’s LA and SF Tech Week presence.

这里存在表述上的不完全一致。

因此不要直接断言：

- “所有获奖作品一定会在线下展示”

提交/获奖前如这一点重要，应重新向主办方确认。

来源：

- https://www.gmicloud.ai/hy-week

---

## 16. 评审

官方明确：

- GMI Cloud 和 Tencent Hunyuan 共同 review 每个 eligible entry
- 三个赛道各一名 winner
- Winners announced：**October 8, 2026**

来源：

- https://www.gmicloud.ai/hy-week

### 目前公开页面没有给出评分标准

截至本文件核对日期，Hy Image Challenge 活动页没有看到类似以下明确评分维度：

- originality 权重
- visual quality 权重
- model usage 权重
- technical complexity 权重
- commercial usefulness 权重
- usability 权重
- public engagement 权重
- likes / reposts 是否计分
- prompt complexity 是否计分
- workflow complexity 是否计分

因此：

**不要把其他 GMI 比赛（例如 MiniMax Week）的 judging criteria 自动套用到 Hy Image Challenge。**

若后续页面新增评分规则，应以更新后的 Hy Image Challenge 页面为准。

---

## 17. 获奖公布时间

官方：

**October 8, 2026**

来源：

- https://www.gmicloud.ai/hy-week

活动页写明：

- submissions close 后进行 review
- winners announced October 8

没有看到：

- 明确公布时刻
- 公布时区
- 是否通过邮件单独通知
- 是否必须在 X 关注官方账户

---

## 18. Hy Image 3.5 preview — 活动页确认的技术能力

活动页写明：

- Image / Generation + Editing
- Text and image in
- up to 2K out
- Text rendering and layout
- approximately 20 seconds per image
- up to 5 reference images per call
- 1K–2K output resolution

来源：

- https://www.gmicloud.ai/hy-week

---

## 19. 官方技术文章提供的补充信息

GMI Cloud 于 2026-09-23 发布：

**Why Hy Image 3.5 Preview Matters: What Held Up When I Tested It**

URL：

https://www.gmicloud.ai/zh-tw/blog/why-hy-image-35-preview-matters-what-held-up-when-i-tested-it

文章写明：

- 模型 ID：`hy-image-v3.5-preview`
- 可接收 text prompts
- 最多 5 张 reference images
- 文章称可输出 `1K / 2K / 4K`
- generation 约 20 秒
- standard international price 文中写为 `$0.024 per image` for 2K and below
- 文中称按 output pixels 计费
- 文章提供 GMI Cloud API 示例

### 注意：2K / 4K 表述冲突

活动比赛页写：

- `1K–2K Output resolution`
- `up to 2K out`

官方技术文章写：

- `1K/2K/4K`

因此：

**比赛期间实际可用上限 / 比赛是否接受 4K，应在需要使用 4K 时重新查证。**

不要仅凭技术文章自动认为比赛页的 2K 描述已经失效。

---

## 20. 已确认的 GMI Cloud API 调用

官方 GMI 技术文章给出的 endpoint：

```text
POST https://console.gmicloud.ai/api/v1/ie/requestqueue/apikey/requests
```

认证：

```text
Authorization: Bearer YOUR_API_KEY
```

Model：

```text
hy-image-v3.5-preview
```

官方示例结构：

```json
{
  "model": "hy-image-v3.5-preview",
  "payload": {
    "prompt": "A misty mountain village at sunrise, traditional architecture, soft golden light.",
    "size": "1920x1080",
    "generate_max_pixels": 4194304
  }
}
```

官方来源：

https://www.gmicloud.ai/zh-tw/blog/why-hy-image-35-preview-matters-what-held-up-when-i-tested-it

---

## 21. 当前本地已经验证的调用事实

在本次准备过程中，已实际成功通过上述 endpoint 调用：

```text
model = hy-image-v3.5-preview
size = 1024x1024
```

返回状态：

```text
status = success
```

返回结构包含：

```text
outcome.media_urls[]
```

并成功取得 1024×1024 PNG。

这是当前用户环境中的实际验证结果，不是比赛规则本身。

工作区根目录保存了一次测试产物：

```text
hy-image-response.json
hy-test.png
```

后续 workspace 不应把这张测试图自动视为参赛作品。

---

## 22. 免费活动规则

官方活动页写：

- GMI account 创建免费
- Hy Image 3.5 preview 在 campaign 期间免费
- `Free for 7 days`
- campaign 后恢复 standard pricing

来源：

- https://www.gmicloud.ai/hy-week

### 活动页未说明

当前公开 Hy Image Challenge 页面没有看到明确说明：

- 每个账户免费多少张
- 每日 generation limit
- 总 generation limit
- 免费 pixel 总量
- concurrency limit
- rate limit
- 是否存在 fair-use cap
- 是否可以自动批量调用
- 是否允许多账户获取更多免费 generation

因此不要将“Free for 7 days”自动解释为“无限调用”。

涉及大规模生成前，应检查：

- GMI console
- API response headers
- 最新活动规则
- GMI Acceptable Use Policy

---

## 23. GMI Cloud 通用法律/使用政策

比赛页底部链接到 GMI 的 Legal / Terms。

Legal hub：

https://www.gmicloud.ai/en/legal

Acceptable Use Policy：

https://www.gmicloud.ai/en/legal/acceptable-use-policy

User Content Disclaimer：

https://www.gmicloud.ai/en/legal/user-content-disclaimer

Console Terms of Service：

https://www.gmicloud.ai/en/legal/console-terms-of-service

---

## 24. Acceptable Use Policy 中与作品相关的事实

GMI Cloud Acceptable Use Policy 要求服务使用合法、合规。

其中公开列出的禁止/限制事项包括但不限于：

- 违法活动
- 仇恨/歧视相关滥用
- 色情或明确性内容等禁止内容
- 侵犯第三方 intellectual property rights
- 侵犯 privacy rights
- 未经授权披露内容
- 欺诈或误导内容
- 其他违法使用

来源：

https://www.gmicloud.ai/en/legal/acceptable-use-policy

这不是比赛专属规则，而是 GMI Cloud 服务的通用使用政策。

---

## 25. User Content Disclaimer 中与作品相关的事实

GMI 的 User Content Disclaimer 表明：

- 用户对自己创建、发布、分享或传输的 User Content 负责
- 用户不得提交违反 Acceptable Use Policy 或适用法律的内容
- GMI 保留移除或限制违规内容的权利

来源：

https://www.gmicloud.ai/en/legal/user-content-disclaimer

同样，这属于 GMI Cloud 通用政策，不是比赛单独的评分规则。

---

## 26. 当前明确 UNKNOWN / 不应自行假设的事项

截至 2026-09-26，从公开活动页未确认以下内容：

### Judging

- 具体评分维度
- 各维度权重
- 是否看社交媒体互动量
- X likes / reposts 是否影响评奖
- 是否偏好技术复杂度
- 是否偏好单图还是 set
- 是否偏好纯图还是 short video
- Prompt 是否作为评分对象
- Workflow 描述详细程度是否计分

### Submission format

- gallery 最大图片数
- short video 最大时长
- file size limit
- image format 限制
- aspect ratio 限制
- 是否要求 1K / 2K
- 是否接受 4K
- 是否必须保留 metadata
- 是否要求提供原始 generation
- 是否要求提供未后期版本

### Workflow

- Photoshop 等人工后期的具体边界
- 其他生成模型可参与到什么程度
- 最终作品中 Hy Image generation 必须占多少比例
- 是否要求每张 set 内图片都由 Hy Image 生成
- 是否允许完全由 Hy Image 生成后再大量人工 compositing

官方只明确：

> Generation has to run on Hy Image 3.5 preview served through GMI Cloud. Other models can support the workflow.

如某个方案触及上述边界，应提交前向官方确认。

### Rights / IP

比赛页没有完整列出：

- 参赛作品版权最终归属条款
- 奖项是否附带独占授权
- 展示授权期限
- 展示授权地域
- 是否允许主办方二次商业使用
- 商标/真人肖像/第三方素材的具体竞赛级要求

比赛表单明确包含“允许 GMI Cloud 和 Tencent Hunyuan feature this work”的 consent，但完整法律效果需结合最终提交页面和适用 Terms 判断。

### Team

- 是否允许团队共同署名
- 多人合作时“一人一次 submission”如何计算
- 奖金如何分配

公开 Hy Image Challenge 页面未写明。

---

## 27. DSH 后续查证原则

如果工作区内后续 agent 对规则产生疑问，按以下优先级复核：

### 优先级 1：Hy Image Challenge 当前活动页

https://www.gmicloud.ai/hy-week

这是比赛规则的第一事实来源。

### 优先级 2：GMI Cloud 官方 Hy Image 3.5 技术文章

https://www.gmicloud.ai/zh-tw/blog/why-hy-image-35-preview-matters-what-held-up-when-i-tested-it

用于确认：

- model id
- endpoint
- API payload
- 技术能力
- 普通定价信息

技术文章不能自动覆盖比赛规则。

### 优先级 3：GMI Documentation

https://docs.gmicloud.ai/

用于确认：

- API schema
- inference 调用
- image/reference 参数
- rate limits 等技术事项

### 优先级 4：GMI Legal

https://www.gmicloud.ai/en/legal

用于确认：

- Terms
- Acceptable Use
- User Content
- Privacy
- 其他法律条款

### 优先级 5：主办方官方渠道

活动页列出的：

- X
- Discord
- LinkedIn
- YouTube

若活动页和技术文档没有回答关键资格问题，应向主办方确认，而不是由 agent 猜测。

---

## 28. DSH 不应自动推断的事项

在方向尚未确定前，workspace / agent 不应默认：

- 参加 Type & Layout
- 参加 Commercial
- 参加 Game Art
- 做户外服装
- 做 Tarot
- 做品牌广告
- 做 UI
- 做单图
- 做四图套系
- 做视频
- 使用某个特定主题
- 某个赛道“更适合用户”
- 某个方向“更容易获奖”

这些都属于后续创意/决策问题，不属于已确认事实。

---

## 29. 提交前事实核对 Checklist

在最终提交前重新打开：

https://www.gmicloud.ai/hy-week

确认：

- [ ] Deadline 是否仍为 October 1, 2026, 11:59 PM PT
- [ ] Track 名称是否仍为 Type & Layout / Commercial / Game Art
- [ ] 是否仍为 one submission per person
- [ ] 是否仍要求 generation 运行在 GMI Cloud 的 Hy Image 3.5 preview
- [ ] 是否仍允许 other models support workflow
- [ ] X tag 是否仍为 `@gmi_cloud` 与 `@TencentHunyuan`
- [ ] X post 是否仍要求 public
- [ ] Submission form 字段是否发生变化
- [ ] 是否新增 judging criteria
- [ ] 是否新增尺寸 / 文件 / 视频限制
- [ ] 是否新增 anti-abuse / usage cap
- [ ] 是否新增版权或授权条款
- [ ] Consent 文本是否变化
- [ ] 作品链接可以正常公开访问
- [ ] 使用的 GMI account email 与 generation account 一致

---

## 30. 官方 URL 索引

### Competition

https://www.gmicloud.ai/hy-week

### Hy Image 3.5 technical article

https://www.gmicloud.ai/zh-tw/blog/why-hy-image-35-preview-matters-what-held-up-when-i-tested-it

### GMI Documentation

https://docs.gmicloud.ai/

### GMI Legal Hub

https://www.gmicloud.ai/en/legal

### Acceptable Use Policy

https://www.gmicloud.ai/en/legal/acceptable-use-policy

### User Content Disclaimer

https://www.gmicloud.ai/en/legal/user-content-disclaimer

### Console Terms of Service

https://www.gmicloud.ai/en/legal/console-terms-of-service

---

## 31. 当前事实状态摘要

截至 2026-09-26，可以确认：

- 活动进行中：是
- 模型：Hy Image 3.5 preview
- 模型 ID：`hy-image-v3.5-preview`
- 必须通过 GMI Cloud 完成 generation：是
- 可以使用其他模型辅助：是
- 可以提交 one piece 或 one set：是
- 三个赛道：Type & Layout / Commercial / Game Art
- 每人只能提交一次：是
- 只能选一个赛道：是
- X 公开发布：必须
- 必须 tag `@gmi_cloud`：是
- 必须 tag `@TencentHunyuan`：是
- 提交 Prompt 或 workflow description：是
- 最终作品链接可为 image / gallery / short video：是
- 截止：2026-10-01 23:59 PT
- Winners announced：2026-10-08
- Winner 数量：3
- 每个 track 1 名 winner
- 每位 winner：$200 cash + $200 any-model GMI credits + $200 Hy Image credits
- 当前公开比赛页存在明确 judging rubric：**否**
- 当前公开比赛页写明 generation 数量上限：**否**
- 当前公开比赛页写明 gallery 图片数量上限：**否**
- 当前公开比赛页写明 short video 最大时长：**否**
- 活动页与技术文章对最大输出分辨率完全一致：**否（2K vs 4K）**
- Tech Week 展示是否对所有 winner 绝对保证：**页面存在表述差异，需复核**

---

_End of factual brief._

# 微信公众号 HTML 红色组件极简长文排版规范

> yinyo-writer 产出的公众号推文，最终以带排版的 HTML 交付，方便直接复制到公众号编辑器。
> v3.5 起，排版层升级为「yinyo红色组件长文版」：以红色组件排版为标尺，不再走米色高级极简；核心是微信原生发布感、红色强品牌锚点、红底白字标题块、红色表头、紧凑正文节奏。
> v3.6 起，增加「主题视觉化」原则：先达到 95 分微信原生阅读感，再让文章主题长出自己的视觉语言。红色不是装饰色，而是指针色；坐标、点、框、路径线不是代码装饰，而是空间指认系统。
> 注意：这里只替换输出样式，不替换 yinyo-writer 的写作方法论、选题逻辑、质检体系和隐曜 DNA。

---

## 0. 样式目标

这版的目标不是"高级极简"，而是"yinyo 原文观感"：红色锚点强、标题切段明确、正文紧凑、组件丰富但不花。

一句话：

> 能撑住 9000 字技术长文的公众号排版：干净、密集、能读下去，不像模板海报。

这套样式不是某个颜色，而是阅读体验：

1. **开头先让读者进入现场。** 热点/体验/叙事型文章优先开场钩子，不默认置顶摘要；技术长文才用「核心总结/路线图」给读者减负。
2. **正文靠短段落推进。** 一段一个意思，很多句子可以单独成段。
3. **小标题少，但要有力量（判断式标题）。** 标题像判断句，不像 PPT 栏目名。
4. **正文强调靠黑色加粗，情感高潮靠 §11 引文块。** 关键判断、数字、方法名加粗；情感判断、核心结论、个人金句用 §11 内容重点引文块（红边 + 斜体 + 浅紫背景）。
5. **表格可以用。** 涉及模型对比、评分、时间线、参数时，表格比散文清楚。
6. **代码/坐标/论文术语要轻量呈现。** 用等宽字体或浅灰代码块，不做炫技代码框。
7. **少 emoji。** 不用 emoji 当列表符号。
8. **广告感要低。** 尾注轻，CTA 轻，不要像知识星球海报。

---

## 0.5 v3.6 主题视觉化原则

当文章已经达到 95 分微信原生阅读感，不要继续机械追求"更红"。下一步要问：

> 这篇文章自己的主题，能不能变成视觉语言？

2026-05-01 DeepSeek 视觉原语推文的最终方案：

- **红色 = 指针色**：只用于指向关键判断、表格关键行、标题锚点。
- **坐标/点/框/路径线 = 主题本身**：用于解释视觉原语，而不是炫技代码块。
- **浅灰坐标块优先**：黑底代码块冲击强，但白底长文里割裂；简单坐标示例用浅灰底 + 红色左线。
- **开篇结论不要默认置顶**：技术读者需要 15 秒扫完时才用；热点/叙事文章先让读者进入现场，再给路线图。
- **标题节奏要变化**：红底白字标题是 yinyo 锚点，但长文里可穿插左线开放标题，避免组件疲劳。
- **尾部品牌轻标识**：不用黑色金句卡片，长文读完后越干净越高级。

最终微调参数：

| 位置 | 参数 | 原因 |
|---|---|---|
| 开篇结论条目间距 | `margin:0 0 8px` | 比 7px 多一点呼吸感，仍保持紧凑 |
| 首段引用字号 | `font-size:16px` | 和正文主字号对齐，更像开场说话 |
| 坐标/代码块 | `background:#f6f8fa;border-radius:6px;`（Mac 终端块风格 §10.2 为准，不再使用红色左线） | 统一用 Mac 三圆代码块，避免与 §11 引文块的红边冲突 |
| 尾部品牌 | `border-top:1px solid #eeeeee;color:#999999` | 轻，但有识别度 |

使用边界：

- 主题视觉化不是每篇都加花样，而是把文章核心概念转成排版语法。
- 如果主题没有明确视觉原语，宁可回到 yinyo 基础版。
- 所有主题化组件必须通过一句话解释：它如何帮助读者理解文章。解释不了就删。

## 1. yinyo红色组件参数

推荐固定参数：

- 外层容器：`max-width:700px; padding:16px 12px 36px;`
- 正文字号：`16px`
- 正文行高：`1.85`
- 正文字色：`#1A1A1A`
- 主品牌红：`#D32F2F`
- 标题块：红底白字，`font-size:20px; line-height:1.4; padding:12px 20px; border-radius:4px;`
- 正文段落：`margin:18px 0`，不要过松
- 表格表头：`background:#D32F2F; color:#FFFFFF; padding:10px 14px;`
- 重点引文（§11）：红色左线 + 斜体 + 浅紫背景，用于核心结论/情感高潮/个人金句
- 摘要：优先普通正文连续段；如用摘要块，必须用红色左线，不用米色 Notion 感
- 代码/坐标块：全部使用 §10.2 Mac 终端块风格（三圆 + 浅灰底），不再使用红色左线

舒服感不等于低饱和。yinyo 的舒服感来自：正文克制 + 红色组件做节奏锚点。

## 2. 全局容器

所有内容包在一个外层 `<section>` 中。

```html
<section style="background-color:#fff;padding:16px 12px 36px;max-width:700px;margin:0 auto;box-sizing:border-box;word-wrap:break-word;font-family:-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Hiragino Sans GB','Microsoft YaHei UI','Microsoft YaHei',Arial,sans-serif;color:#1A1A1A;line-height:1.85;font-size:16px;letter-spacing:0.2px;">
  <!-- 正文 -->
</section>
```

规则：

- 不使用 `<style>`。
- 不使用 class。
- 不使用 `<div>`。
- 样式全部内联。
- 微信编辑器兼容优先。

---

## 3. 文章标题

标题左对齐，黑色，不居中，不加背景。

```html
<p style="margin:0 0 22px;font-size:24px;line-height:1.45;color:#111;font-weight:800;">
文章标题
</p>
```

标题规则：

- 一篇只出现一次。
- 不用 emoji 开头。
- 不加下划线。
- 不做居中大字报。

---

## 4. 开头摘要区

yinyo式长文的关键是开头先帮读者抓重点。超过 2500 字的文章，必须有摘要区。

### 4.1 超长预警 + 核心总结

```html
<section style="margin:0 0 26px;padding:14px 16px 12px;background:rgba(211,47,47,0.05);border-left:4px solid #D32F2F;box-sizing:border-box;">
  <p style="margin:0 0 10px;font-size:15px;line-height:1.85;color:#555;">
  超长预警，这篇文章预计阅读时长 12 分钟。如果你只想看结论，先看这四条：
  </p>
  <p style="margin:0 0 8px;font-size:15px;line-height:1.85;color:#222;">
  <b style="font-weight:700;color:#111;">1、</b>第一条核心结论。
  </p>
  <p style="margin:0 0 8px;font-size:15px;line-height:1.85;color:#222;">
  <b style="font-weight:700;color:#111;">2、</b>第二条核心结论。
  </p>
  <p style="margin:0;font-size:15px;line-height:1.85;color:#222;">
  <b style="font-weight:700;color:#111;">3、</b>第三条核心结论。
  </p>
</section>
```

摘要区规则：

- 只用于开头，不要全文到处放卡片。
- 背景只用极浅灰。
- 左侧细线即可，不做大面积彩色块。
- 3-5 条为宜。
- 每条必须是真结论，不是目录。

### 4.2 短文不用摘要卡

如果文章少于 2000 字，可以直接开头：

```html
<p style="margin:0 0 18px;font-size:16px;line-height:1.85;color:#1A1A1A;">
先说结论。
</p>
```

---

## 5. 正文段落

### 5.1 普通段落

```html
<p style="margin:0 0 18px;font-size:16px;line-height:1.85;color:#1A1A1A;">
正文内容。
</p>
```

段落规则：

- 一段尽量 20-80 字。
- 一个段落只讲一个意思。
- 不要把多个判断塞进一段。
- 长句拆短。
- 关键转折可以单独成段。

### 5.2 独立判断句

适合放核心判断、反共识句、章节前的钩子。

```html
<p style="margin:26px 0 20px;font-size:17px;line-height:1.88;color:#111111;font-weight:800;">
真正的问题，不是看得清，而是指得准。
</p>
```

规则：

- 不要滥用。
- 每 800-1200 字出现 1 次左右。
- 必须像人话判断，不要像口号。

---

## 6. 标题体系（二级节奏锚点）

长文标题承担切段功能，两个层级依次递进，视觉差异明显。

---

### 6.1 小节标题（红底白字标签块 + 阴影立体感）

用于文章最大章节切分（如「第一部分」「写在最后」）。`display:inline-block`（自适应宽度，像标签）+ `box-shadow`（立体感）。

**来源参考：** Draco公众号《火山卷出天际的Agent Plan》（"第一部分：获取和配置Agent Plan"、"写在最后"）——2026-05-19 经用户确认为 yinyo-writer 新标题样式，同时清理旧全宽块标题。

```html
<h2 style="display:inline-block;padding:0.3em 1em;margin:4em 8px 2em;border-radius:8px;
  font-size:19.5px;line-height:1.5;color:#fff;background:#FA5151;
  box-shadow:0 4px 6px rgba(0,0,0,0.1);text-align:left;font-weight:700;">
  <span leaf="">第一部分：获取和配置Agent Plan</span>
</h2>
```

关键参数：

| 属性 | 值 | 效果 |
|------|-----|------|
| `display:inline-block` | 自适应宽度 | 不占满行，视觉更轻盈 |
| `background:#FA5151` | 品牌红 | 略亮于 #D32F2F |
| `box-shadow:0 4px 6px rgba(0,0,0,0.1)` | 投影 | 立体感 |
| `margin:4em 8px 2em` | 大间距 | 与正文充分拉开 |
| `border-radius:8px` | 8px | 圆角柔和 |

**使用场景：** 文章的最大章节分割（如"第一部分""写在最后"）。与 §6.2 左线子标题构成二级节奏。一篇 5000 字长文使用 2-3 次。

---

### 6.2 子标题（左红竖线 + 黑粗体 + 红色虚下划线）

用于最小层级的子标题，视觉最轻、最内敛。区别于 §6.1 的红色背景大块，它用左竖线 + 虚下划线做弱标记。

**来源参考：** Draco公众号《火山卷出天际的Agent Plan》（"获取Agent Plan"、"配置Agent Plan"、"案例1：自媒体工作流…"）——2026-05-19 经用户确认为 yinyo-writer 子标题样式。

```html
<h3 style="padding-left:12px;border-left:4px solid #FA5151;
  border-bottom:1px dashed #FA5151;margin:2em 8px 0.75em 0;
  color:#24292f;font-size:18px;font-weight:700;line-height:1.2;">
  <span leaf="">获取Agent Plan</span>
</h3>
```

关键参数：

| 属性 | 值 | 效果 |
|------|-----|------|
| `border-left:4px solid #FA5151` | 左侧红实线 | 左竖线锚点 |
| `padding-left:12px` | 左内边距 | 文字避开竖线 |
| `border-bottom:1px dashed #FA5151` | 底部红虚线 | 下划虚线，轻量收束 |
| `color:#24292f` | 深灰 | 黑色粗体 |
| `font-weight:700` | 粗体 | 有分量但不刺眼 |

**使用场景：** 章节内部的步骤名称、案例标题、方法分支。与 §6.1 构成二级节奏：大章节→子标题。子标题每千字不超过 2 个，过多则降级为段落开头加粗。

---

### 标题规则（通用）

- 左对齐。
- 不编号也可以。
- 不居中。
- 不加 emoji。
- 不加背景（§6.1/§6.2 自带头背景除外）。
- 不加下划线。
- 标题本身要有信息量。

差标题：

```text
一、项目背景
二、技术分析
三、总结
```

好标题：

```text
为什么 coding agent 必须有视觉
主流派在解决「看得清」，DeepSeek 在解决「指得准」
真正的差距出现在拓扑推理
这件事对普通用户意味着什么
```

**二级标题选择指南：**  
| 层级 | HTML 标签 | 样式 | 用途 |
|------|-----------|------|------|
| 一级（大章节） | `<h2>` | §6.1 红底白字标签块 + 阴影 | 文章最大段落切分 |
| 二级（子标题） | `<h3>` | §6.2 左红竖线 + 虚下划线 | 章节内小标题、案例名 |

---

## 7. 强调规则

### 7.1 黑色加粗（唯一段落内强调方式）

```html
<b style="font-weight:700;color:#111;">关键判断</b>
```

使用场景：
- 核心概念、关键数字、方法名
- 反共识判断、文章结论
- 需要读者特别注意的地方

**唯一规则：** 所有段落内强调统一用黑色加粗（`color:#111`），不用红色、金色、暗红、浅灰虚化等任何彩色强调。简化读者的视觉负担——正文段落内部只有「普通文本」和「加粗文本」两种状态。彩色只在标题块（§6.1 红底白字）、表格表头（红底白字）和 §11 引文块（浅紫背景）中使用。

---

## 8. 列表写法

列表多数是自然段，不是 bullet 列表。

### 8.1 普通分条

```html
<p style="margin:0 0 12px;font-size:16px;line-height:1.9;color:#222;">
<b style="font-weight:700;color:#111;">第一，</b>它解决的是反复出现的问题。
</p>
<p style="margin:0 0 12px;font-size:16px;line-height:1.9;color:#222;">
<b style="font-weight:700;color:#111;">第二，</b>它有稳定流程，而不是靠灵感发挥。
</p>
```

规则：

- 不用 `<ul>`。
- 不用 emoji bullet。
- 不用一行一个彩色卡片。
- 分条之间间距比普通段落略小。

### 8.2 开头摘要可以用数字条

摘要区允许 `1、2、3、4、`，但仍然用 `<p>`。

---

## 9. 表格

技术对比、模型数据、版本时间线可以用表格。表格要有红色表头，这是 yinyo 长文的重要视觉锚点。不要做彩色大杂烩，但表头必须有识别度。

```html
<table style="width:100%;border-collapse:collapse;margin:22px 0;font-size:14px;line-height:1.7;color:#222;">
  <thead>
    <tr>
      <th style="background-color:#D32F2F;color:#FFFFFF;padding:10px 14px;text-align:left;font-weight:600;border:none;">模型</th>
      <th style="background-color:#D32F2F;color:#FFFFFF;padding:10px 14px;text-align:left;font-weight:600;border:none;">KV cache 条目</th>
      <th style="background-color:#D32F2F;color:#FFFFFF;padding:10px 14px;text-align:left;font-weight:600;border:none;">平均分</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border-bottom:1px solid #F0F0F0;padding:8px 6px;">DeepSeek</td>
      <td style="border-bottom:1px solid #F0F0F0;padding:8px 6px;">~90</td>
      <td style="border-bottom:1px solid #F0F0F0;padding:8px 6px;">77.2%</td>
    </tr>
  </tbody>
</table>
```

表格规则：

- 正文只用浅灰边线。
- 表头红底白字。
- 不做多色表头。
- 不做复杂合并单元格。
- 移动端优先，列数不超过 4。

---

## 10. 代码、坐标、论文符号（轻量代码/坐标块）

### 10.1 行内代码

```html
<code style="font-family:Menlo,Consolas,monospace;font-size:14px;background:#F3F2EF;color:#333;padding:1px 4px;border-radius:3px;">prompt-master</code>
```

适合：仓库名、变量名、模型名、短代码。

### 10.2 Mac 风格终端块（三圆 + 代码区）

适合展示 shell 命令、终端输出、多行代码片段。顶部带红/橙/绿三圆（Mac 风格）。所有代码、GitHub 链接、JSON、坐标、YAML、shell 命令一律使用此格式。

**注意：** 单行命令（如 `curl`/`npm`/`git`）也优先归入 §10.2，不走行内代码（§10.1）。行内代码仅限仓库名、变量名、模型名等**短标识符**。

**来源参考：** Draco正在VibeCoding 公众号《火山卷出天际的Agent Plan》文章格式——2026-05-19 经用户确认为 yinyo-writer 新版式。

```html
<pre style="font-size:90%;margin:10px 8px;padding:0;overflow-x:auto;overflow-y:hidden;
  border-radius:8px;line-height:1.5;background:#f6f8fa;color:#24292f;border:none;
  box-shadow:inset 0 0 10px rgba(0,0,0,0.05);">
  <!-- Mac 三圆 SVG（红/橙/绿） -->
  <span style="display:block;padding:10px 14px 0;line-height:0;user-select:none;">
    <svg xmlns="http://www.w3.org/2000/svg" width="45px" height="13px" viewBox="0 0 450 130" role="img" aria-label="终端">
      <ellipse cx="50" cy="65" rx="50" ry="52" stroke="rgb(220,60,54)" stroke-width="2" fill="rgb(237,108,96)"></ellipse>
      <ellipse cx="225" cy="65" rx="50" ry="52" stroke="rgb(218,151,33)" stroke-width="2" fill="rgb(247,193,81)"></ellipse>
      <ellipse cx="400" cy="65" rx="50" ry="52" stroke="rgb(27,161,37)" stroke-width="2" fill="rgb(100,200,86)"></ellipse>
    </svg>
  </span>
  <!-- 代码内容 -->
  <code style="white-space:pre-wrap;display:block;padding:0.35em 1em 1em;text-indent:0;
    color:inherit;background:none;margin:0;min-width:max-content;word-break:normal;
    overflow-wrap:normal;box-sizing:border-box;
    font-family:'Fira Code',Menlo,'Operator Mono',Consolas,Monaco,monospace;">
    <span leaf="">curl -fsSL https://example.com/install.sh | sh<br></span>
  </code>
</pre>
```

**规则：**
- 顶部三圆 SVG 必须保留，红 `rgb(237,108,96)`、橙 `rgb(247,193,81)`、绿 `rgb(100,200,86)`，描边略深
- 背景 `#f6f8fa` 浅灰，与普通代码块的 `#F7F6F3` 接近但稍亮
- 代码字体等宽：`'Fira Code', Menlo, 'Operator Mono', Consolas, Monaco, monospace`
- 内阴影 `inset 0 0 10px rgba(0,0,0,0.05)` 增加微凹效果
- 每个命令独立成 `<span leaf="">` + `<br>`（逐行换行）
- 一个多行命令块放 `<pre>` 内多条 `<span>`，不把每条命令拆成多个 `<pre>`

**使用场景：**
- shell 命令和终端输出
- 多行代码示例（JSON、坐标、YAML）
- GitHub 仓库地址、安装命令等 URL 展示
- 系统安装/配置步骤的完整命令序列



---

## 11. 内容重点引文块（红色左线 + 斜体 + 浅紫背景）

当需要突出一个核心观点、情感高潮、个人金句、或重要结论时，用带红色左边线的斜体引文块。区别于普通引用（引用外部文档），这是作者自己的强调。

**与 §5.2 的区分标准：** §11 用于情感型/结论型强调（金句、情感高潮、感悟总结），§5.2 用于结构型强调（章节钩子、反共识句）。两者互斥——同一句话不会同时用两种格式。

**适用于：**
- 技术文章中的核心公式或原则（「Agent Plan = Coding Plan + Image 生成 + ...」）
- 叙事/感悟文章中的情感高潮句或个人金句（「认真，就是一种最不需要天赋的天赋」）
- 个人判断的总结性结论
- 需要读者停下来感受的重要观点

**来源参考：** Draco正在VibeCoding 公众号《火山卷出天际的Agent Plan》文章格式——2026-05-19 经用户确认为 yinyo-writer 新版式。

```html
<blockquote style="font-style:italic;margin-bottom:1em;padding:1em 1em 1em 2em;color:rgba(0,0,0,0.6);background:#f8f4ff;border-left:4px solid #FA5151;border-radius:6px;box-shadow:0 4px 6px rgba(0,0,0,0.05);text-align:left;">
  <p style="display:block;margin:0;color:inherit;font-family:inherit;font-size:15px;line-height:inherit;letter-spacing:0.1em;text-align:left;">
    核心结论或重要观点。
  </p>
</blockquote>
```

**规则：**
- 全文斜体（`font-style:italic`），全文浅灰字（`color:rgba(0,0,0,0.6)`）
- 左侧红色 4px 实线边（`border-left:4px solid #FA5151`）
- 浅紫背景（`background:#f8f4ff`），非强对比、不刺眼
- 圆角 6px + 轻阴影（`box-shadow:0 4px 6px rgba(0,0,0,0.05)`）
- 内部 `<p>` 必须 `margin:0`（避免双层间距）
- 内部如需再强调某个词，用 `<strong style="color:#FA5151;">...</strong>`
- 每篇文章使用不超过 3 次，过度使用会稀释强调效果

**使用场景：**
- 核心公式或原则（技术文章关键公式）
- 个人判断的总结性结论
- 情感高潮或感悟中的金句（叙事/散文文章尤其适用）
- 需要读者停下来的重要观点

---

## 12. 引用

引用论文原文、外部文档、用户原话时，用左线引用。

```html
<section style="margin:22px 0;padding:2px 0 2px 14px;border-left:3px solid #D9C2A0;box-sizing:border-box;">
<p style="margin:0;font-size:15px;line-height:1.9;color:#555;">
引用内容。
</p>
</section>
```

规则：

- 不加大背景。
- 不用引号图标。
- 引用之后必须用人话解释。

---

## 13. 图片

```html
<p style="margin:24px 0;text-align:center;">
<img src="图片地址" style="max-width:100%;border-radius:6px;display:block;margin:0 auto;" />
</p>
```

图片说明：

```html
<p style="margin:-8px 0 22px;font-size:13px;line-height:1.7;color:#999;text-align:center;">
图片说明
</p>
```

---

## 14. 分割线

```html
<section style="margin:34px 0;border-top:1px solid #EEE;"></section>
```

只用于明显转场或尾注前。

---

## 15. 尾注

尾注要轻，不要像广告牌。纯文字居中，无头像、无卡片背景、无彩色强调。

```html
<section style="margin:36px 0 0;padding-top:24px;border-top:1px solid #EEE;text-align:center;">
  <p style="margin:0 0 4px;font-size:15px;line-height:1.8;color:#333;font-weight:700;">
  yinyo 隐曜
  </p>
  <p style="margin:0;font-size:13px;line-height:1.7;color:#999;">
  一人AI实验室，真实评测 · 实用技能 · 自由探索。
  </p>
</section>
```

硬性规则：
- 文案必须逐字固定：第一行 `yinyo 隐曜`，第二行 `一人AI实验室，真实评测 · 实用技能 · 自由探索。`
- 不使用头像、卡片、彩色背景、金色/红色描边
- 字体颜色：名字 `#333` 或 `#111`，简介 `#999`
- 居中，不加任何 emoji 或符号前缀

---

## 16. 禁止事项

禁止：

- 大面积彩色卡片。
- 彩色渐变背景。
- emoji 列表。
- 居中标题。
- 下划线标题。
- 一句话一个大卡片。
- 满屏橙色/红色高亮。
- PPT 式信息块堆叠。
- 使用 `<style>`、class、`<div>`。
- 把正文拆得过稀，读起来像广告落地页。

---

## 18. 交付方式

公众号推文产出时，同时提供：

1. **Markdown 原文**，用于二次修改。\n2. **yinyo式红色组件排版 HTML**，嵌入邮件正文 + 作为 `.html` 附件。

HTML 只负责阅读体验，不负责炫技。

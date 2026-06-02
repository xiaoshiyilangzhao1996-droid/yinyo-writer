<div align="center">

# yinyo-writer

"把技术判断写成中文读者真正能读懂的长文。"

![Status](https://img.shields.io/badge/status-active-2ea043)
![Skill](https://img.shields.io/badge/type-codex_skill-2563eb)
![Language](https://img.shields.io/badge/language-zh--CN-f59e0b)
![Runtime](https://img.shields.io/badge/runtime-modular-7c3aed)
![License](https://img.shields.io/badge/license-internal-lightgrey)

</div>

`yinyo-writer` 是一组面向中文技术长文的 Codex Skills：主 skill 负责写作判断，HTML 和 image2 prompt 作为运行时子 skill 独立执行。

[看效果](#看效果) · [安装](#安装) · [它包含什么](#它包含什么) · [工作方式](#工作方式) · [目录结构](#目录结构) · [边界](#边界) · [校验](#校验)

---

## 看效果

典型使用方式：

```text
调用 yinyo-writer.skill 写一篇《读懂 Harness 的 Context Management（二）：OpenClaw》。
第一版只要 Markdown，不需要 HTML，也不生成图片。
```

需要公众号 HTML 时：

```text
调用 yinyo-wechat-html，把这篇 Markdown 转成符合 Yinyo 样式的 WeChat HTML。
```

需要插图提示词时：

```text
调用 yinyo-image2-prompt，基于全文生成 1 张封面和 5 张正文插图 prompt。
```

---

## 安装

复制三个 skill 目录到 Codex 全局 skill 库：

```powershell
Copy-Item .\skills\yinyo-writer C:\Users\wangzhengyuan7\.codex\skills\yinyo-writer -Recurse -Force
Copy-Item .\skills\yinyo-wechat-html C:\Users\wangzhengyuan7\.codex\skills\yinyo-wechat-html -Recurse -Force
Copy-Item .\skills\yinyo-image2-prompt C:\Users\wangzhengyuan7\.codex\skills\yinyo-image2-prompt -Recurse -Force
```

如果 Codex 会话已经启动，重启会话后可以看到新的 skill 描述和触发规则。

---

## 它包含什么

| Skill | 职责 | 不负责 |
| --- | --- | --- |
| `yinyo-writer` | 中文技术长文写作、结构判断、风格约束、质量复核 | HTML 生成、图片提示词、发布 |
| `yinyo-wechat-html` | Markdown 转 WeChat HTML、内联样式、编码与结构校验 | 写文章、生成图片、自动发布 |
| `yinyo-image2-prompt` | 封面和正文插图的 prompt plan、风格一致性、位置建议 | 写文章、转 HTML、上传图片 |

这个拆分让用户入口保持一个主 skill，同时让运行时能力边界清晰，避免一个 `SKILL.md` 同时塞写作、排版、图片、发布四类职责。

---

## 工作方式

`yinyo-writer` 先判断文章任务本身：读者是谁、核心问题是什么、证据来自哪里、结构是否能支撑观点、段落是否符合中文长文阅读节奏。

当用户明确要 HTML，才进入 `yinyo-wechat-html`。它使用参数化脚本生成 UTF-8 HTML，并遵守公众号编辑器友好的约束：不用 `<style>`、不用 `class`、不用 `<div>`，只使用内联样式和稳定的正文结构。

当用户明确要封面或插图，才进入 `yinyo-image2-prompt`。它从全文抽取视觉任务，生成 cover、architecture、comparison、experience 等不同用途的 prompt，而不是随手补几张装饰图。

---

## 目录结构

```text
skills/
  yinyo-writer/
    SKILL.md
    references/
    examples/
  yinyo-wechat-html/
    SKILL.md
    docs/
    scripts/
      convert_to_wechat_html.py
  yinyo-image2-prompt/
    SKILL.md
    docs/
    examples/
```

---

## 边界

- 不伪造源码、论文、数据、用户案例。
- 不默认发布、上传、发飞书、发公众号。
- 不把 HTML、图片 prompt、发布流程重新塞回主写作 skill。
- 不让旧 Harness 术语污染通用 Codex 运行时，比如 `skill_view()` 或 `image_generate()`。
- 不把历史迭代记录写成当前规则，规则必须能执行、能检查。

---

## 校验

建议提交前运行：

```powershell
Get-ChildItem .\skills -Recurse -Filter SKILL.md | ForEach-Object { "$($_.FullName) $((Get-Item $_.FullName).Length) bytes" }
python .\skills\yinyo-wechat-html\scripts\convert_to_wechat_html.py --input .\tests\fixtures\sample.md --output .\tmp\sample.html --image-manifest .\tests\fixtures\images.json
rg "skill_view|image_generate|/root/.openclaw|placeholder-for-wechat-upload" .\skills
```

HTML 转换结果应该满足：

- UTF-8 编码正常。
- 正文插图出现在 Markdown 占位符位置。
- 不包含 `<style>`、`class=`、`<div>`。
- 页尾只保留 `yinyo 隐曜` 的极简署名。

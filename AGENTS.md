# AGENTS.md

## 怎么读

先读 `README.md`，确认这是一个三 skill 仓库，不是单一 monolith。

再按任务读取：

- 写文章或审稿：读 `skills/yinyo-writer/SKILL.md`。
- 转公众号 HTML：读 `skills/yinyo-wechat-html/SKILL.md`。
- 生成封面或插图 prompt：读 `skills/yinyo-image2-prompt/SKILL.md`。

详细写作风格、HTML 细节、图片 prompt 方法只在需要时按 `SKILL.md` 的 Runtime Resources 逐步加载。

---

## 怎么回答

- 用户要文章时，先交付 Markdown 内容，不默认生成 HTML 或图片。
- 用户要 HTML 时，使用 `yinyo-wechat-html` 的脚本和校验规则。
- 用户要图片时，先给 prompt plan；只有用户明确要生成图片时才调用图片工具。
- 用户要发布、上传、发飞书、发公众号时，必须把这个动作当成单独的外发边界处理。

---

## 硬规则

- 不伪造源码、论文、数据、引用、截图、用户案例。
- 不默认发布、上传或发送任何内容。
- 不把旧 Harness 专用术语写回通用 skill 契约。
- 不在 `SKILL.md` 里堆长文档；长规则放到 `references/`、`docs/`、`examples/`、`scripts/`。
- 不把 HTML、image prompt、Feishu 发布逻辑塞回 `yinyo-writer` 主 skill。
- `yinyo-writer` 的 L1 硬检查是内部护栏：通过精准措辞、证据位置和来源格式满足，不写成读者可见的审稿语言或开头免责声明。
- 文章开头必须先给冲突、场景、判断或好奇心；不要用范围收缩、benchmark 声明或来源 bookkeeping 抢第一屏。

---

## 常见关联

- `skill-schema-v2`：审视、重构、修复本仓库 skill 时使用。
- `imagegen`：只有用户明确要生成实际图片时使用。
- `lark-doc` 或 `lark-drive`：只有用户明确要求飞书文档或云空间操作时使用。

---

## 风险点

- `yinyo-wechat-html/docs/feishu-docx-api-notes.md` 是飞书发布参考，不是默认执行流程。
- `yinyo-writer/examples/iteration-lessons.md` 是历史迭代经验，不是可直接照抄的当前文章模板。
- `skills/yinyo-wechat-html/scripts/convert_to_wechat_html.py` 应保持参数化，不允许恢复硬编码输入输出路径。
- `yinyo-writer/references/data-comparison-rules.md` 的数据可信度规则要求贴近数据自然交代，不允许变成文章开头免责声明。

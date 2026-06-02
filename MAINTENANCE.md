# MAINTENANCE.md

## 维护范围

本仓库维护三类 Codex Skill：

- `skills/yinyo-writer`
- `skills/yinyo-wechat-html`
- `skills/yinyo-image2-prompt`

主 skill 和子 skill 可以一起发布，但职责不能重新合并。

---

## 本地同步

从仓库同步到全局 Codex skill 库：

```powershell
$repo = "C:\Users\wangzhengyuan7\Documents\Codex\2026-05-29\files-mentioned-by-the-user-2\yinyo-writer-repo"
$codex = "C:\Users\wangzhengyuan7\.codex\skills"

Copy-Item "$repo\skills\yinyo-writer" "$codex\yinyo-writer" -Recurse -Force
Copy-Item "$repo\skills\yinyo-wechat-html" "$codex\yinyo-wechat-html" -Recurse -Force
Copy-Item "$repo\skills\yinyo-image2-prompt" "$codex\yinyo-image2-prompt" -Recurse -Force
```

---

## 提交前校验

检查 skill 体积：

```powershell
Get-ChildItem .\skills -Recurse -Filter SKILL.md | ForEach-Object { "$($_.FullName) $((Get-Item $_.FullName).Length) bytes" }
```

检查旧运行时污染：

```powershell
rg "skill_view|image_generate|/root/.openclaw|placeholder-for-wechat-upload|sk-" .\skills
```

检查 HTML 脚本：

```powershell
python .\skills\yinyo-wechat-html\scripts\convert_to_wechat_html.py --input .\tests\fixtures\sample.md --output .\tmp\sample.html --image-manifest .\tests\fixtures\images.json
```

期望输出：

- `has_style_tag: false`
- `has_class_attr: false`
- `has_div_tag: false`
- `has_minimal_footer: true`

---

## 发布

```powershell
git status --short
git add README.md AGENTS.md MAINTENANCE.md skills
git commit -m "Refactor yinyo writer into modular skills"
git push origin main
```

---

## 变更原则

- 改写作规则，优先改 `yinyo-writer` 的 references 或 examples。
- 改 HTML 样式，优先改 `yinyo-wechat-html` 的 docs 或脚本。
- 改图片风格，优先改 `yinyo-image2-prompt` 的 docs。
- 改外发能力时，必须显式保留人工确认边界。

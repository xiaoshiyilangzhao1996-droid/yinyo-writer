---
name: yinyo-wechat-html
description: "Load when converting a Markdown article into Yinyo-style WeChat public-account HTML."
version: "1.0.0"
last_updated: "2026-06-02"
depends: []
metadata:
  author: "yinyo"
  category: "publishing"
---

# yinyo-wechat-html

Converts a finished Markdown article into WeChat-compatible inline-style HTML. This skill does not write the article and does not generate images.

## Contract

Goal: produce a local `.html` file that can be copied into the WeChat editor.

Inputs:

- Markdown article path or Markdown content
- optional output path
- optional image manifest with local image paths and captions

Output:

- one HTML file
- validation report

Boundaries:

- Do not publish, upload, email, or send the HTML unless the user explicitly asks.
- Do not invent images. If image paths are missing, leave clear placeholders or report missing assets.
- Do not use `<style>`, `class=`, or `<div>` in WeChat HTML.
- Do not use card/avatar footer. The footer must be minimal text.

## Runtime Resources

Load only when needed:

- `docs/wechat-html-layout.md` — complete layout rules
- `docs/feishu-docx-api-notes.md` — only when user explicitly asks for Feishu document publishing
- `scripts/convert_to_wechat_html.py` — generic Markdown-to-HTML converter

## Conversion Rules

- Wrap content in one outer `<section>`.
- Use inline styles only.
- Use red component headings for major sections.
- Use lightweight code blocks for `text`/code fences.
- Use red table headers.
- Use minimal centered Yinyo footer:

```text
yinyo 隐曜
一人AI实验室，真实评测 · 实用技能 · 自由探索。
```

## Verification

After conversion, verify:

```text
HTML exists:
Image count:
All image paths exist:
Has <style>: false
Has class=: false
Has <div>: false
Has charset=utf-8:
Footer is minimal:
External publishing performed: no / yes with user confirmation
```

## Feishu Publishing Boundary

Feishu publishing is not part of default HTML conversion.

Only if the user explicitly asks to publish to Feishu:

1. Load `docs/feishu-docx-api-notes.md`.
2. Confirm the target destination.
3. Confirm credential source and do not print secrets.
4. Create or update the document.
5. Return the document URL and a summary of actions.

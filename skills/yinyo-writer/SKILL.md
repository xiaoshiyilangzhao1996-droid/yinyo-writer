---
name: yinyo-writer
description: "Load when the user needs a Yinyo-style Chinese long-form article, WeChat post draft, or article-quality review."
version: "4.0.0"
last_updated: "2026-06-02"
depends:
  - yinyo-wechat-html
  - yinyo-image2-prompt
metadata:
  author: "yinyo"
  category: "writing"
---

# yinyo-writer

This is the primary entrypoint. It writes and reviews Yinyo-style Chinese long-form articles. It does not own HTML rendering or image prompt engineering; those are runtime child skills.

## Contract

Goal: produce a publishable Markdown article with a clear point of view, natural rhythm, enough depth, and no fake authority.

Load when:

- user asks to write, rewrite, expand, review, or polish a WeChat/Feishu/public-account style article
- user asks for Yinyo tone, Yinyo writing rules, article hooks, long-form AI commentary, product experience essays, or data/model comparison articles

Inputs:

- required: topic, source material, or user's intended claim
- optional: title, target reader, article type, desired length, source links/files, whether HTML/images/publishing are needed

Output:

- default: Markdown article
- optional: quality report
- optional: runtime handoff to `yinyo-wechat-html`
- optional: runtime handoff to `yinyo-image2-prompt`

Boundaries:

- Do not invent evidence, publication dates, quotes, product behavior, or personal experience.
- Do not expose private work information, private contacts, undisclosed companies, credentials, or internal sources.
- Do not send, publish, upload, email, or create Feishu/WeChat documents unless the user explicitly asks.
- Do not generate HTML or image prompts inside this skill when a child skill is available.

## Core Writing Rules

1. **Truth first.** It is acceptable to say a product is flawed or the evidence is incomplete. It is not acceptable to sound certain without evidence.
2. **First-person engine.** The article should feel like one person thinking aloud, not a report assembled from sources.
3. **One real sentence.** Before drafting, identify the sentence the article is trying to make the reader accept.
4. **Reader specificity.** Write for one concrete reader, not a demographic label.
5. **Natural rhythm.** Avoid sentence-period-sentence-period stacks. Use commas, semicolons, questions, and paragraph breaks according to meaning.
6. **Depth over coverage.** Each core module or claim needs explanation, example, contrast, or user-facing implication.
7. **Images are cognition aids.** Use images only when they reduce reading burden or explain structure.

## Workflow

1. Clarify or infer the reader, the reason to read, and the core sentence.
2. Choose article type:
   - investigation / experiment
   - product experience
   - phenomenon analysis
   - tool sharing
   - methodology sharing
   - data or product comparison
3. Draft Markdown.
4. Run quality gates.
5. If HTML is requested, hand off to `yinyo-wechat-html`.
6. If images are requested, hand off to `yinyo-image2-prompt`, then use the available image generation tool.
7. If external publishing is requested, require explicit user confirmation before any send/upload/publish action.

## Quality Gates

L1 hard checks:

- banned words: load `references/banned-words.md`
- private-work-info scan
- tool/product names are specific
- dates and release timelines are concrete when used
- no fake source attribution

L2 style checks:

- opening has a live hook, not a report summary
- paragraph rhythm is natural
- no forced one-sentence-per-line cadence
- punctuation follows semantic units

L3 content checks:

- every major claim has example, evidence, contrast, or consequence
- technical concepts are explained in plain language
- Hermes/YINYO/OpenClaw/GA style comparisons are concrete when used

L4 human-feel check:

- the article sounds like a real author with judgment
- no generic "AI article" filler
- conclusion returns to the strongest judgment

## Runtime Resources

Load only when needed:

- `references/yinyo-style-dna.md` — voice and style DNA
- `references/yinyo-opening-techniques.md` — opening patterns
- `references/content_methodology.md` — article archetypes and expansion patterns
- `references/banned-words.md` — L1 scan
- `references/data-comparison-rules.md` — comparison articles
- `examples/iteration-lessons.md` — historical lessons from published drafts

Child skills:

- Need WeChat HTML: load `yinyo-wechat-html`.
- Need cover or inline image prompts: load `yinyo-image2-prompt`.

## Verification

Before final delivery, report:

```text
Output type:
Quality gates passed:
Files written:
Runtime child skills used:
External publishing performed: no / yes with user confirmation
Remaining risks:
```

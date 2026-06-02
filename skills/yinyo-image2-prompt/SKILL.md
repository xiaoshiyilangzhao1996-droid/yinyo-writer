---
name: yinyo-image2-prompt
version: 1.0.0
last_updated: 2026-06-02
description: "Load when the user needs cover or inline image prompts for a Yinyo-style Chinese article."
---

# yinyo-image2-prompt

Generate image prompt plans for Yinyo articles. This skill owns image concept,
placement, visual consistency, aspect ratio, and prompt wording. It does not own
article writing, Markdown-to-HTML conversion, publishing, or upload.

## Contract

Use this skill when the user asks for:

- A WeChat cover image prompt.
- Inline illustration prompts for an article.
- A consistent image set for one article.
- A prompt manifest that another image tool can execute.
- Review or repair of image prompts for AI-generated assets.

Inputs:

- Article title and Markdown/content.
- Desired image count, or infer count from article density.
- Required aspect ratios, especially WeChat cover `1.35:1`.
- Existing style reference, if any.
- Any hard constraints from the user.

Outputs:

- A prompt plan with one record per image.
- Each record includes `purpose`, `placement`, `aspect_ratio`, `caption`,
  `prompt`, and `negative_prompt`.
- Use English for image-model style tokens and key visual nouns when helpful;
  use Chinese for the explanation and reader-facing caption.

## Boundaries

- Do not invent a diagram or visual claim that the article does not support.
- Do not generate images by default. If an image generation tool is explicitly
  available and the user asks for actual images, use that tool after producing
  the prompt plan.
- Do not put tiny unreadable text, fake UI screenshots, fake logos, or fake
  source citations into images.
- Do not use stock-photo language when the requested style is hand-drawn,
  editorial, technical, or diagrammatic.
- Do not upload, publish, or embed assets into HTML unless the user asks for
  that downstream operation.

## Workflow

1. Read the article title and structure.
2. Identify where the reader needs visual compression, comparison, or pacing.
3. Decide the minimum useful image set:
   - Cover: identity, topic, and emotional signal.
   - Architecture image: module relationships and information flow.
   - Comparison image: two systems or two design choices.
   - Failure/experience image: where user experience breaks.
   - Transition image: useful only for long dense sections.
4. Keep one visual grammar across the set: line weight, palette, texture,
   perspective, border radius, icon language, and background treatment.
5. Produce the prompt plan and image manifest.

## Prompt Rules

- State the subject first, then composition, then style, then constraints.
- For technical articles, prioritize readable structure over decorative detail.
- Keep diagrams sparse enough to survive WeChat mobile width.
- Use consistent Chinese labels only when labels are large and essential.
- For cover images, avoid dense labels; the cover should communicate the theme,
  not teach the whole article.
- For inline architecture images, concept names can be English while explanatory
  labels remain Chinese.

## Output Format

Return a JSON-compatible manifest unless the user requests prose:

```json
[
  {
    "id": "cover",
    "purpose": "cover",
    "placement": "before_title",
    "aspect_ratio": "1.35:1",
    "caption": "",
    "prompt": "...",
    "negative_prompt": "..."
  }
]
```

## Runtime Resources

Load only when needed:

- `docs/cover-design-best-practices.md`: cover composition and WeChat thumbnail
  constraints.
- `docs/ai-deodorizer.md`: remove generic AI-art smells from prompts.

## Verification

Before delivering prompts, check:

- Every image has a clear job in the article.
- All prompts share one coherent style.
- Cover and inline images use different density levels.
- No prompt depends on fake screenshots, fake product marks, or illegible text.
- Captions match the article section where the image will appear.

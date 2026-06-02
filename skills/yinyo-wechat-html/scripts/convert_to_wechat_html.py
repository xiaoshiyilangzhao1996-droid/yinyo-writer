#!/usr/bin/env python3
"""Convert Markdown into Yinyo-style WeChat HTML.

The output intentionally uses inline styles only because WeChat editors often
strip external CSS, class names, and style blocks.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any


FOOTER_TITLE = "yinyo 隐曜"
FOOTER_TEXT = "一人AI实验室，真实评测 · 实用技能 · 自由探索。"


def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code style=\"background:#f3f4f6;color:#374151;padding:1px 5px;border-radius:4px;font-size:90%;\">\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong style=\"font-weight:700;color:#111827;\">\1</strong>", text)
    return text


def paragraph(text: str) -> str:
    return (
        '<p style="margin:0 0 18px 0;font-size:16px;line-height:1.85;'
        'color:#1f2937;letter-spacing:0;">'
        f"{inline(text.strip())}</p>"
    )


def image_block(src: str, caption: str | None = None) -> str:
    cap = ""
    if caption:
        cap = (
            '<p style="margin:8px 0 18px 0;text-align:center;font-size:13px;'
            'line-height:1.6;color:#6b7280;letter-spacing:0;">'
            f"{inline(caption)}</p>"
        )
    return (
        '<figure style="margin:26px 0 28px 0;">'
        f'<img src="{html.escape(src, quote=True)}" alt="" style="display:block;width:100%;height:auto;border-radius:6px;" />'
        f"{cap}</figure>"
    )


def table_block(lines: list[str]) -> str:
    rows: list[list[str]] = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    if not rows:
        return ""

    out = ['<table style="width:100%;border-collapse:collapse;margin:22px 0;font-size:14px;line-height:1.65;color:#1f2937;">']
    for index, row in enumerate(rows):
        out.append("<tr>")
        tag = "th" if index == 0 else "td"
        bg = "background:#f9fafb;" if index == 0 else ""
        weight = "font-weight:700;" if index == 0 else "font-weight:400;"
        for cell in row:
            out.append(
                f'<{tag} style="border:1px solid #e5e7eb;padding:9px 10px;text-align:left;vertical-align:top;{bg}{weight}">'
                f"{inline(cell)}</{tag}>"
            )
        out.append("</tr>")
    out.append("</table>")
    return "".join(out)


def load_manifest(path: Path | None) -> dict[str, Any]:
    if not path:
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return {str(i + 1): item for i, item in enumerate(data)}
    if isinstance(data, dict):
        return data
    raise ValueError("image manifest must be a JSON array or object")


def render_markdown(markdown: str, manifest: dict[str, Any]) -> tuple[str, int]:
    lines = markdown.splitlines()
    parts: list[str] = []
    paragraph_lines: list[str] = []
    image_count = 0
    i = 0

    def flush_paragraph() -> None:
        if paragraph_lines:
            parts.append(paragraph(" ".join(item.strip() for item in paragraph_lines)))
            paragraph_lines.clear()

    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped:
            flush_paragraph()
            i += 1
            continue

        if stripped.startswith("<!--IMG:") and stripped.endswith("-->"):
            flush_paragraph()
            key = stripped.removeprefix("<!--IMG:").removesuffix("-->").strip()
            item = manifest.get(key)
            if item:
                if isinstance(item, str):
                    parts.append(image_block(item))
                else:
                    parts.append(image_block(str(item.get("src", "")), item.get("caption")))
                image_count += 1
            i += 1
            continue

        if stripped.startswith("```"):
            flush_paragraph()
            language = stripped.strip("`").strip()
            code_lines: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            label = f"{html.escape(language)} " if language else ""
            code = html.escape("\n".join(code_lines))
            parts.append(
                '<section style="margin:22px 0;padding:14px 16px;background:#111827;border-radius:6px;overflow:auto;">'
                f'<p style="margin:0 0 8px 0;font-size:12px;line-height:1.4;color:#9ca3af;">{label}code</p>'
                f'<pre style="margin:0;font-size:13px;line-height:1.65;color:#f9fafb;white-space:pre-wrap;"><code>{code}</code></pre>'
                "</section>"
            )
            continue

        if stripped.startswith("|"):
            flush_paragraph()
            table_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            parts.append(table_block(table_lines))
            continue

        if stripped.startswith("# "):
            flush_paragraph()
            parts.append(
                '<h1 style="margin:0 0 24px 0;font-size:24px;line-height:1.35;color:#111827;font-weight:800;letter-spacing:0;">'
                f"{inline(stripped[2:])}</h1>"
            )
            i += 1
            continue

        if stripped.startswith("## "):
            flush_paragraph()
            parts.append(
                '<h2 style="margin:34px 0 16px 0;font-size:19px;line-height:1.45;color:#111827;font-weight:800;letter-spacing:0;">'
                '<span style="display:inline-block;width:4px;height:18px;background:#dc2626;border-radius:2px;margin-right:8px;vertical-align:-3px;"></span>'
                f"{inline(stripped[3:])}</h2>"
            )
            i += 1
            continue

        if stripped.startswith("### "):
            flush_paragraph()
            parts.append(
                '<h3 style="margin:26px 0 12px 0;font-size:17px;line-height:1.5;color:#111827;font-weight:700;letter-spacing:0;">'
                f"{inline(stripped[4:])}</h3>"
            )
            i += 1
            continue

        if stripped.startswith(">"):
            flush_paragraph()
            quote = stripped.lstrip(">").strip()
            parts.append(
                '<blockquote style="margin:22px 0;padding:12px 14px;border-left:4px solid #dc2626;background:#f9fafb;color:#374151;">'
                f"{paragraph(quote)}</blockquote>"
            )
            i += 1
            continue

        if re.match(r"^[-*]\s+", stripped):
            flush_paragraph()
            items: list[str] = []
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append(re.sub(r"^[-*]\s+", "", lines[i].strip()))
                i += 1
            parts.append('<ul style="margin:0 0 18px 18px;padding:0;color:#1f2937;font-size:16px;line-height:1.85;">')
            for item in items:
                parts.append(f'<li style="margin:0 0 8px 0;">{inline(item)}</li>')
            parts.append("</ul>")
            continue

        paragraph_lines.append(line)
        i += 1

    flush_paragraph()
    return "\n".join(parts), image_count


def wrap_document(body: str) -> str:
    footer = (
        '<hr style="border:none;border-top:1px solid #e5e7eb;margin:34px 0 18px 0;" />'
        '<p style="margin:0 0 4px 0;font-size:14px;line-height:1.7;color:#111827;font-weight:700;letter-spacing:0;">'
        f"{FOOTER_TITLE}</p>"
        '<p style="margin:0;font-size:13px;line-height:1.7;color:#6b7280;letter-spacing:0;">'
        f"{FOOTER_TEXT}</p>"
    )
    return (
        "<!doctype html>\n"
        '<html lang="zh-CN">\n'
        "<head>\n"
        '<meta charset="utf-8" />\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1" />\n'
        "<title>yinyo-wechat-html</title>\n"
        "</head>\n"
        '<body style="margin:0;background:#ffffff;">\n'
        '<main style="max-width:680px;margin:0 auto;padding:24px 16px 32px 16px;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif;">\n'
        f"{body}\n{footer}\n"
        "</main>\n"
        "</body>\n"
        "</html>\n"
    )


def validate(output: str, image_count: int, output_path: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    lower = output.lower()
    missing_images = max(len(manifest) - image_count, 0)
    return {
        "output": str(output_path),
        "image_count": image_count,
        "missing_manifest_images": missing_images,
        "has_style_tag": "<style" in lower,
        "has_class_attr": "class=" in lower,
        "has_div_tag": "<div" in lower,
        "has_minimal_footer": FOOTER_TITLE in output and FOOTER_TEXT in output,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Markdown to Yinyo WeChat HTML.")
    parser.add_argument("--input", required=True, type=Path, help="Markdown input path")
    parser.add_argument("--output", required=True, type=Path, help="HTML output path")
    parser.add_argument("--image-manifest", type=Path, help="Optional JSON manifest for <!--IMG:n--> placeholders")
    args = parser.parse_args()

    markdown = args.input.read_text(encoding="utf-8-sig")
    manifest = load_manifest(args.image_manifest)
    body, image_count = render_markdown(markdown, manifest)
    output = wrap_document(body)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    print(json.dumps(validate(output, image_count, args.output, manifest), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

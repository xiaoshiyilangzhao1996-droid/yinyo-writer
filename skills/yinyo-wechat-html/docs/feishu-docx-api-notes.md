# Feishu Docx API 发布笔记（yinyo-writer v3.17+）

> 将 yinyo 文章发布到飞书文档时遇到的坑点和正确做法。  
> 2026-05-17 实测，自建应用 `tenant_access_token` 模式。

---

## 一、核心模式：直接调用 Open API（绕过 lark-cli）

**不要依赖 lark-cli**。原因：
- lark-cli 的 `strictMode: user` 导致只能使用已过期的 user_access_token
- `--as bot` 被 strict mode 拦截
- keychain 在 Windows 上会报 `Access is denied`

**正确做法**：用 app_id + app_secret 获取 `tenant_access_token`，直接调飞书 Open API。

```python
import urllib.request, json

# Step 1: 获取 tenant_access_token
resp = urllib.request.urlopen(urllib.request.Request(
    "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
    data=json.dumps({"app_id": APP_ID, "app_secret": APP_SECRET}).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST"
))
token = json.loads(resp.read().decode("utf-8"))["tenant_access_token"]
```

---

## 二、标题编码：必须用 Python urllib（禁止 bash curl）

### 🚫 错误做法（标题会乱码）

```bash
curl -s -X POST ... -d '{"title":"AI正在提高创业失败率？真相令人意外"}'
# → 飞书收到的标题变成: AI�������ߴ�ҵʧ���ʣ�������������
```

Git Bash / MSYS2 的 curl 在传递中文字符时编码出问题，UTF-8 被当成 Latin-1 解码。

### ✅ 正确做法（Python urllib）

```python
title = "AI正在提高创业失败率？真相令人意外"
req = urllib.request.Request(
    "https://open.feishu.cn/open-apis/docx/v1/documents",
    data=json.dumps({"title": title}).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json; charset=utf-8"
    },
    method="POST"
)
# Python 可以用 python（AutoClaw 的），不是 python3（Windows Store 存根）
```

### ⚠️ Windows 注意

- `python3` → Windows Store 存根，退出码 49，不能用
- `python` → AutoClaw 安装的完整 Python，能用
- `python --version` 确认是真实解释器

---

## 三、文档创建流程

### 3.1 创建文档（POST）

```python
POST https://open.feishu.cn/open-apis/docx/v1/documents
{"title": "文章标题"}
```

返回 `document_id`（同时也是 Page block 的 `block_id`）。

### 3.2 写入内容块（POST children）

```python
POST https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{doc_id}/children
{
  "children": [{ ...blocks... }],
  "index": 0  # 插入位置，从 0 开始
}
```

**分批规则**：每批最多 50 个 block，按顺序插入。

### 3.3 块类型 JSON 结构

| block_type | 类型 | JSON 结构 |
|-----------|------|-----------|
| 2 | 正文段落 | `{"block_type": 2, "text": {"elements": [...], "style": {}}}` |
| 3 | H1 标题 | `{"block_type": 3, "heading1": {"elements": [...]}}` |
| 4 | H2 标题 | `{"block_type": 4, "heading2": {"elements": [...]}}` |
| 5 | H3 标题 | `{"block_type": 5, "heading3": {"elements": [...]}}` |
| 9 | 无序列表 | `{"block_type": 9, "bullet": {"elements": [...]}}` |
| 10 | 有序列表 | `{"block_type": 10, "ordered": {"elements": [...]}}` |
| 11 | 代码块 | `{"block_type": 11, "code": {"elements": [...], "style": {"language": 1, "wrap": true}}}` |
| 12 | 引用块 | `{"block_type": 12, "quote": {"elements": [...]}}` |
| 17 | 分割线 | **不可通过 POST children 创建**（API 会返回 invalid param） |

### 3.4 text_element 格式

```python
{
    "text_run": {
        "content": "文本内容",
        "text_element_style": {
            "bold": True,      # 可选
            "italic": False    # 可选
        }
    }
}
```

### 3.5 分割线（Divider）的坑

飞书 API 文档说 Divider 支持 "Create"，但实际上**不能通过 POST children API 创建**。所有尝试（`"divider": {}`、`"divider": null`、不带 divider 字段）均返回 HTTP 400 invalid param。

**替代方案**：跳过分割线，用空段落或视觉换行替代。

---

## 四、文档标题无法通过 PATCH 更新

飞书 Open API **没有提供文档创建后修改标题的接口**。

- `PATCH /open-apis/docx/v1/documents/{id}` → 只支持 display_setting，不支持 title
- `lark-cli docs +update --new-title` → 需要同时提供 markdown 内容，且 lark-cli 自身有 auth 问题

**应对方案**：如果标题错了，只能新建文档写入，放弃旧文档。

---

## 五、完整流程代码参考

```python
import urllib.request, json, time

TOKEN = "t-g1045..."  # tenant_access_token
DOC_ID = "..."        # 新建文档返回的 ID
PAGE_ID = DOC_ID      # Page block 的 ID 等于文档 ID

def make_elem(text, bold=False):
    return {"text_run": {"content": text, "text_element_style": {"bold": bold}}}

def make_block(block_type, type_key, elements):
    return {"block_type": block_type, type_key: {"elements": elements}}

def write_blocks(blocks, batch_size=50):
    """分批写入 block 内容"""
    for start in range(0, len(blocks), batch_size):
        batch = blocks[start:start+batch_size]
        req = urllib.request.Request(
            f"https://open.feishu.cn/open-apis/docx/v1/documents/{DOC_ID}/blocks/{PAGE_ID}/children",
            data=json.dumps({"children": batch, "index": start}).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {TOKEN}",
                "Content-Type": "application/json; charset=utf-8"
            },
            method="POST"
        )
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result["code"] != 0:
                raise Exception(f"Batch {start} failed: {result}")
        time.sleep(0.3)  # 遵守 3 QPS 限制
```

---

## 六、已知限制

| 限制 | 说明 |
|------|------|
| 标题编码 | bash curl 会乱码，必须用 Python urllib |
| 分割线 | POST children API 不支持创建 |
| QPS | 单应用每秒 3 次，单文档每秒 3 次并发编辑 |
| 单批 block | 建议不超过 50 个 |
| 标题修改 | 没有 API 支持创建后修改标题，只能重建 |
| lark-cli auth | 本机 lark-cli 仅支持 user identity（token 已过期），不适用于自动化 |
| token 过期 | `tenant_access_token` 有效约 1 小时（expire ~6000秒）。长时间脚本需要中途重新获取，或在每次调用前刷新。 |

---

## 七、图片插入（3步流程）

飞书文档插入图片需要 **3 步**，不是 1 步。`POST children` API 允许创建空的图片块（`{"block_type": 27, "image": {}}`），但不能一步到位直接把已有媒体上传 token 写入。

### 正确流程

> **Step 1: 创建空图片块**
>
> `POST /open-apis/docx/v1/documents/{doc_id}/blocks/{page_id}/children`
> ```json
> {"children": [{"block_type": 27, "image": {}}], "index": 0}
> ```
> 返回新块的 `block_id`。
>
> **Step 2: 上传媒体（parent_node = 图片块 ID）**
>
> `POST /open-apis/drive/v1/medias/upload_all`
> 表单字段：
> - `parent_type`: `"docx_image"`（⚠️ 必须是 `docx_image`，不是 `docx`）
> - `parent_node`: **上一步返回的 image block_id**（不是文档 ID！）
> - `file_name`: 文件名（如 `cover.png`）
> - `size`: 文件大小（字节）
> - `file`: 二进制图片文件
>
> 返回 `file_token`。
>
> **Step 3: PATCH 更新图片块**
>
> `PATCH /open-apis/docx/v1/documents/{doc_id}/blocks/{image_block_id}`
> ```json
> {"replace_image": {"token": "{file_token}"}}
> ```

### Python 完整代码

```python
import urllib.request, json, uuid

def insert_image(doc_id, filepath, token, index=0):
    """在飞书文档中插入一张图片。三步：创建空块 → 上传 → replace_image。"""
    page_id = doc_id

    # Step 1: 创建空图片块
    body = {"children": [{"block_type": 27, "image": {}}], "index": index}
    req = urllib.request.Request(
        f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{page_id}/children",
        data=json.dumps(body).encode("utf-8"),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json; charset=utf-8"},
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        r = json.loads(resp.read().decode("utf-8"))
        block_id = r["data"]["children"][0]["block_id"]

    # Step 2: 上传媒体
    with open(filepath, "rb") as f:
        img_data = f.read()
    filename = filepath.split("\\")[-1]
    boundary = "----" + uuid.uuid4().hex

    def mf(n, v):
        return (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{n}\"\r\n\r\n{v}\r\n").encode("utf-8")
    def mff(n, fn, d):
        return (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{n}\"; filename=\"{fn}\"\r\nContent-Type: image/png\r\n\r\n").encode("utf-8") + d + b"\r\n"

    fb = b""
    fb += mf("file_name", filename)
    fb += mf("parent_type", "docx_image")
    fb += mf("parent_node", block_id)
    fb += mf("size", str(len(img_data)))
    fb += mff("file", filename, img_data)
    fb += f"--{boundary}--\r\n".encode("utf-8")

    req2 = urllib.request.Request(
        "https://open.feishu.cn/open-apis/drive/v1/medias/upload_all",
        data=fb,
        headers={"Authorization": f"Bearer {token}", "Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST"
    )
    with urllib.request.urlopen(req2) as resp2:
        r2 = json.loads(resp2.read().decode("utf-8"))
        file_token = r2["data"]["file_token"]

    # Step 3: replace_image
    body3 = {"replace_image": {"token": file_token}}
    req3 = urllib.request.Request(
        f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{block_id}",
        data=json.dumps(body3).encode("utf-8"),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json; charset=utf-8"},
        method="PATCH"
    )
    with urllib.request.urlopen(req3) as resp3:
        json.loads(resp3.read().decode("utf-8"))

    return block_id
```

### ⚠️ 坑点

1. **`parent_node` 必须是图片块 block_id，不是文档 ID。** 如果误传文档 ID，媒体会上传成功但无法关联到图片块，图片块最终显示为空。
2. **必须先创建空图片块，才能上传媒体。** 上传媒体时需要知道目标 block_id。
3. **每次调用 `POST children` 改变文档状态**，所以后续插入的 index 要手动递增（已插入的块占位）。
4. **不要用 `"file_token"` 或任何已有 token 直接创建图片块**（即不能直接把上传好的 token 塞进 `{"block_type": 27, "image": {"token": "xxx"}}`）。这是最常见的误区和错误做法，飞书 API 拒绝这种格式（返回 invalid param）。正确做法永远是先建空块再 replace_image。
5. **图片插入后不能通过 API 删除。** 如需腾位置，只能重建文档或用 lark-cli 手动操作。

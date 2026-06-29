# SECURITY.md

## 数据边界

本仓库只维护可公开审查的 Codex Skill 规则、参考文档、示例和本地转换脚本。

禁止提交：

- 真实用户数据、内部业务文档、未公开论文材料或私有截图。
- API Key、Cookie、Token、SSH 私钥、发布凭证或飞书/公众号会话信息。
- 带有个人隐私、公司内部系统地址、未脱敏客户信息的文章样例。
- 生成缓存、浏览器 profile、Office 临时文件或本地输出目录。

---

## 外发限制

Skill 可以生成 Markdown、HTML 或图片 prompt，但不会默认发布、上传、发送邮件、写飞书文档或操作公众号后台。

任何外发动作都必须由用户明确提出，并在执行前确认目标、内容和账号边界。

---

## 泄露处理

发现敏感信息后：

1. 立即停止继续复制、同步或发布相关文件。
2. 删除工作区中的敏感内容，并用占位描述替代。
3. 检查 `git status --short` 和 `git diff`，确认敏感内容不在待提交变更中。
4. 如果敏感内容已经进入 Git 历史，暂停推送并先轮换对应凭证。
5. 修复完成后再运行维护校验。

---

## 提交前检查

```powershell
rg -i "sk-[A-Za-z0-9_-]{20,}|BEGIN .*PRIVATE KEY|password\\s*=\\s*['\\\"]|cookie\\s*=\\s*['\\\"]" . --glob "!SECURITY.md"
rg "browser_profile|placeholder-for-wechat-upload" . --glob "!SECURITY.md"
git status --short
```

期望结果：

- 没有真实密钥、Cookie、密码或私钥命中。
- 没有本地 profile、临时目录、生成缓存进入提交。
- `git status --short` 只包含计划提交的 Skill、文档和测试文件。

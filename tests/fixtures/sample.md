# 读懂 Harness 的 Context Management（二）：OpenClaw

Context Management 不是一个单独模块，而是一组 runtime 决策。

<!--IMG:cover-->

## Runtime 是什么

OpenClaw runtime 可以理解为：读 transcript、加 bootstrap、查 memory、组 prompt、跑模型、写 transcript。

| 模块 | 作用 |
| --- | --- |
| transcript | 保存对话流水 |
| memory | 注入可复用信息 |

> 复杂系统不是不能做，而是每一层都要有可修复性。

```text
prompt = bootstrap + memory + transcript
```

# SKILL.md 结构模板库（四种基本型 + frontmatter 配方）

> Phase 3 构建时读取。先按用途选一种基本型，再按模板填充。
> 四种基本型源自官方 init_skill.py 的分类；多数 skill 是「任务型 + 局部工作流」的混合。

---

## 零、frontmatter 配方（所有基本型共用）

```yaml
---
name: verb-first-name            # 必填。1-64 字符，小写字母数字 + 单连字符，与目录名一致
description: Use when ...        # 必填。1-1024 字符，第三人称，只写触发条件
---
```

**description 三段式**（顺序固定，关键词前置）：

```
[触发条件 + 症状/同义词] + [可选：一句话 what] + [排除项 NOT for X — use Y instead]
```

**实测过的 BAD / GOOD**（来源：obra/superpowers writing-skills，一手）：

| ❌ BAD | 为什么 |
|---|---|
| `Use when executing plans - dispatches subagent per task with code review between tasks` | **总结了工作流** → agent 照 description 只做一次 review，而正文流程图要求两次 |
| `Use for TDD - write test first, watch it fail, write minimal code, refactor` | 过程细节同上 |
| `For async testing` | 太抽象，没有触发信号 |
| `I can help you with async tests when they're flaky` | 第一人称 |
| `Use when tests use setTimeout/sleep and are flaky` | 绑了语言症状，不通用 |

| ✅ GOOD | 为什么 |
|---|---|
| `Use when executing implementation plans with independent tasks in the current session` | 纯触发条件 |
| `Use when tests have race conditions, timing dependencies, or pass/fail inconsistently` | 描述**问题**而非语言症状 |
| `Use when using React Router and handling authentication redirects` | 技术专属就明说技术 |

**关键词覆盖清单**（写 description 时逐项过）：
- 错误信息：`ENOTEMPTY`、`Hook timed out`、`race condition`
- 症状词：`flaky`、`hanging`、`zombie`、`卡住`、`不触发`
- 同义词：`timeout/hang/freeze`、`cleanup/teardown/afterEach`
- 工具/文件类型：实际命令名、库名、`.pdf`/`.docx` 等扩展名

**命名规则**：动词优先、主动语态；流程类用动名词（`creating-skills` > `skill-creation`）；按「你要做什么」或核心洞察命名（`condition-based-waiting` > `async-test-helpers`）；避免 `Helper`/`Utils`/`Tools`/`Documents` 这类泛名。

---

## 基本型 A：工作流型（Workflow-Based）

**适用**：有明确先后顺序的多步流程（生成 → 转换 → 校验）。

```markdown
---
name: example-workflow
description: Use when [触发条件]。不适用于 [排除项]。
---

# [名称]

> 一句话核心原则。

## 入口分流（Decision Tree）
| 用户输入 | 路径 |
|---|---|
| [输入类型 A] | → Step X |
| [输入类型 B] | → Step Y |

## Step 1: [动作名]
[祈使句指令]
**完成检查**：[ ] [可核对的判据——做完看到什么 = 成功]

## Step 2: ...
```

**要点**：步骤用动词开头；每步带可核对的完成检查；分叉用表格不用嵌套 if；流程图只用于「非显而易见的决策点」和「防过早停止的循环」。

---

## 基本型 B：任务型（Task-Based）

**适用**：一个 skill 提供多个并列操作（PDF：合并/拆分/提取）。

```markdown
## Quick Start
[最常见任务的 30 秒上手示例，含可直接运行的命令]

## 任务 1: [操作名]
[真实用户语句作为触发示例] → [执行指令] → [输入/输出示例]
## 任务 2: ...
```

**要点**：Quick Start 在最前；任务之间无依赖；一个优秀示例胜过多个平庸示例；**不要为同一模式提供多语言版本示例**（稀释质量 + 维护负担）。

---

## 基本型 C：规范/指南型（Reference/Guidelines）

**适用**：标准、规范、品牌指南、编码约定。

```markdown
## 核心原则
[3-7 条，每条带「为什么」与「反例」]

## 规范细则
[按主题分节；细节下沉 references/，本节给 grep 线索与强制读取指令]

## 合规检查
[自检脚本用法 + 检查清单]
```

**要点**：原则宁少勿多；每条规范必须可检查；配可执行自检脚本；反模式写成**可检测的具体特征**（如「暖奶油底 #F4F1EA + 陶土 accent」而非「避免 AI 味」）。

---

## 基本型 D：能力组合型（Capabilities-Based）

**适用**：多个相互关联的能力构成一个系统。

```markdown
## Core Capabilities
### 1. [能力名]
[何时调用 → 怎么执行 → 产出什么]
### 2. ...
```

---

## 通用骨架章节（可选但推荐）

| 章节 | 作用 | 何时必加 |
|---|---|---|
| 何时用 / 何时不用 | 防误触发与过度触发 | skill 与相邻能力易混淆时 |
| 任务路由表 | 决策先行，让 agent 一次定位 | 有多条执行路径时 |
| Quick Reference 表 | 可 grep 的速查 | 参数/命令多时 |
| Gotchas / Common Mistakes | 只写反直觉项 + 修复 | 涉及易踩坑的库/格式时 |
| 失败模式编码 | 把已知失败路径显式写进正文（「会怎样失败、什么信号」），不是「别犯错」式叮嘱 | 一律建议（SkillLens 实证决定效用的三维度之一） |
| 高风险行动黑名单 | `rm` / `git reset --hard` / force push 等破坏性操作显式列禁 | 涉及破坏性操作时必加（SkillLens 三维度之一） |
| Red Flags - STOP | 借口对照表 + 「这些都意味着：停下来重来」 | 纪律类 skill 必加 |
| Verify | 机器可执行的验证步骤 + 「渲染后亲眼看」 | 产出物有质量判据时 |
| 失败模式速查表 | if-then 降级路径（触发 → 一线修复 → 兜底） | 长流程/联网/多 agent 任务 |
| 诚实边界与裁决条款 | 做不到什么；规则与用户需求冲突时谁赢 | 一律建议 |

---

## 形式匹配表（决定上面每一节该用什么语气写）

| 基线失败类型 | 该用的形式 | 用了会适得其反的形式 |
|---|---|---|
| 压力下明知故犯（跳过规则） | 禁令 + 借口对照表 + 红旗清单 | 软性指导（"prefer"、"consider"） |
| 遵守了但**输出形状错** | 正面配方/输出契约（输出是什么、分几部分、什么顺序） | 禁令清单（agent 会跟 "don't" 讨价还价，实测比无指导更差） |
| 遗漏必需元素 | 模板里设 REQUIRED 字段/槽位 | 散文式提醒 |
| 行为依赖条件 | 键于**可观察谓词**的条件句 | 无条件规则 + 豁免条款 |

**两条配套禁令**：
1. **No nuance clauses**：「除非确实重要，否则不要 X」会重新开启谈判。
2. **豁免条款不起限定作用**：「此限制不适用于代码块」仍会抑制代码块——要重构结构，让规则触及不到那部分。

---

## 长度预算

| 类型 | 目标 |
|---|---|
| 频繁加载 / getting-started 型 | <200 词 ≈ <400 中文字符 |
| 普通 skill | <500 词 ≈ <1000 中文字符 |
| 硬性上限（规范建议） | <500 行 / 正文 <5000 token |
| 内联代码块 | <50 行；超过 100 行的内容拆到 references/ |

**核对方式**：`python scripts/skill_check.py <skill目录>` 输出的 `BODY_TOKENS`（英文按词、中文按字估算）。

⚠️ **不要用 `wc -w` 核对中文 skill**——`wc -w` 按空白分词，中文无空格，会把 6600 字的正文算成 500 多个「词」，严重低估（实测低估约 3 倍），5000 token 门禁形同虚设。中文按**字符数**估算：1 汉字 ≈ 1–1.5 token。

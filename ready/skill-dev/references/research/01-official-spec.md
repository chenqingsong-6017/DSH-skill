# 01 · Agent Skills（SKILL.md）官方规范与最佳实践调研

> 调研日期：2026-10-15 ｜ 调研人：general-purpose-1 ｜ 用途：构建「开发新 Skill」元 skill 的规范基座
>
> **可信度分级**：🅰 官方一手（anthropic.com / claude.com / agentskills.io / github.com/anthropics / code.claude.com 原文抓取）｜🅱 官方一手但经搜索摘要转述（platform.claude.com 平台文档、官方 PDF，因区域限制未能直接抓取全文）｜🅲 权威二手分析｜🅳 社区推断
>
> **效力分级**：【规范】= 开放标准硬性要求（校验器会强制）｜【建议】= 官方明确写出但不强制｜【实现】= 仅特定客户端（如 Claude Code）的行为｜【社区】= 社区通行做法或推断

---

## 一、开放标准规范（agentskills.io/specification）🅰【规范】

2025-12-18 Anthropic 将 Agent Skills 发布为开放标准，规范站点 agentskills.io，源码在 github.com/agentskills/agentskills（代码 Apache-2.0 / 文档 CC-BY-4.0）。以下是规范全文要点。

### 1.1 目录结构

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

- 唯一硬性要求：一个目录 + 一个 `SKILL.md`。
- `scripts/`、`references/`、`assets/` 是**约定俗成**（recommendations），不是强制。
- 规范原文：*"A skill is a directory containing, at minimum, a `SKILL.md` file."*

### 1.2 frontmatter 字段总表

| 字段 | 必填 | 约束 |
|---|---|---|
| `name` | **是** | 最大 64 字符；仅小写字母/数字/连字符；不得以连字符开头或结尾 |
| `description` | **是** | 最大 1024 字符；非空；描述做什么 + 何时用 |
| `license` | 否 | 许可证名称或指向随包许可证文件 |
| `compatibility` | 否 | 最大 500 字符；环境要求（目标产品、系统包、网络访问等） |
| `metadata` | 否 | 任意 string→string 键值映射 |
| `allowed-tools` | 否 | 空格分隔的预批准工具串，**实验性（Experimental）**，各实现支持度不一 |

规范原文（字段表）：

> `name` — Yes — Max 64 characters. Lowercase letters, numbers, and hyphens only. Must not start or end with a hyphen.
> `description` — Yes — Max 1024 characters. Non-empty. Describes what the skill does and when to use it.
> `allowed-tools` — No — Space-separated string of pre-approved tools the skill may use. (Experimental)

### 1.3 `name` 字段细则 🅰【规范】

- 长度 1–64 字符
- 仅允许 unicode 小写字母数字（`a-z`、`0-9`）和连字符（`-`）
- 不得以 `-` 开头或结尾
- 不得包含连续连字符（`--`）
- **必须与父目录名一致**（"Must match the parent directory name"）

合法：`pdf-processing`、`data-analysis`、`code-review`
非法：`PDF-Processing`（大写）、`-pdf`（开头连字符）、`pdf--processing`（连续连字符）

### 1.4 `description` 字段细则 🅰【规范】

- 长度 1–1024 字符
- 应同时说明**做什么**和**何时用**（"describe both what the skill does and when to use it"）
- 应包含帮助 agent 识别相关任务的具体关键词

规范给出的好/坏例子：
- 好：`Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction.`
- 坏：`Helps with PDFs.`

### 1.5 选填字段细则 🅰【规范】

- **license**：建议简短（许可证名或随包文件名），如 `license: Proprietary. LICENSE.txt has complete terms`
- **compatibility**：1–500 字符；仅在有特定环境要求时写；多数 skill 不需要。示例：`Requires git, docker, jq, and access to the internet`
- **metadata**：string→string map；建议 key 名有足够独特性避免冲突。约定俗成放 `author`、`version`
- **allowed-tools**：空格分隔，如 `allowed-tools: Bash(git:*) Bash(jq:*) Read`；实验性，跨实现行为可能不同

### 1.6 Body（正文）🅰【规范+建议】

- 规范层面：**无格式限制**（"There are no format restrictions"）
- 规范建议章节：逐步指令、输入输出示例、常见边界情况
- 关键提醒：*"the agent will load this entire file once it's decided to activate a skill"*——激活后整个文件进上下文，所以长内容应拆到引用文件

### 1.7 可选目录约定 🅰【建议】

- `scripts/`：可执行代码。应自包含或明确标注依赖；应有有用的报错信息；应优雅处理边界情况。语言取决于 agent 实现（常见 Python/Bash/JavaScript）
- `references/`：按需加载的文档（`REFERENCE.md`、`FORMS.md`、领域文件如 `finance.md`）。*"Keep individual reference files focused. Agents load these on demand, so smaller files mean less use of context."*
- `assets/`：静态资源（模板、图片、数据文件/查找表/schema）

### 1.8 渐进式披露（Progressive Disclosure）🅰【规范+建议】

规范三级模型：

| 级别 | 内容 | 何时加载 | token 预算 |
|---|---|---|---|
| 1. Metadata | `name` + `description` | 启动时（所有 skill） | **~100 tokens/skill** |
| 2. Instructions | `SKILL.md` 正文 | skill 被激活时 | **建议 < 5000 tokens** |
| 3. Resources | `scripts/`、`references/`、`assets/` | 需要时 | 脚本执行不进上下文；引用文件读入才计 |

规范明确建议：*"Keep your main `SKILL.md` under 500 lines. Move detailed reference material to separate files."*

### 1.9 文件引用规则 🅰【建议】

- 使用相对 skill 根目录的相对路径：`references/REFERENCE.md`、`scripts/extract.py`
- **引用保持一层深**（"Keep file references one level deep from SKILL.md"），避免深层嵌套引用链

### 1.10 校验工具 🅰

官方参考校验库 `skills-ref`（github.com/agentskills/agentskills/tree/main/skills-ref）：

```bash
skills-ref validate ./my-skill
```

校验 frontmatter 合法性与命名约定。注意：它只检查"格式是否良好"，不检查"内容是否安全"。

---

## 二、关键数字速查表

| 项目 | 上限/预算 | 来源 | 级别 |
|---|---|---|---|
| `name` 长度 | ≤64 字符 | agentskills.io/specification 🅰 | 【规范】 |
| `name` 字符集 | 小写字母数字 + `-`；不首尾连字符；无连续连字符；**与目录名一致** | 同上 🅰 | 【规范】 |
| `description` 长度 | ≤1024 字符，非空 | 同上 🅰 | 【规范】（上传校验实测强制：anthropics/skills PR #1605 将某 skill 从 1176 字符砍到 992）|
| `compatibility` 长度 | ≤500 字符 | 同上 🅰 | 【规范】 |
| `allowed-tools` | 实验性，支持度因实现而异 | 同上 🅰 | 【规范】 |
| SKILL.md 正文行数 | **< 500 行** | 规范 & 平台文档 & skill-creator 三处一致 🅰🅱 | 【建议】 |
| SKILL.md 正文 token | **< 5000 tokens** 推荐 | agentskills.io/specification 🅰；platform.claude.com overview 🅱 同样写 "Under 5k tokens" | 【建议】 |
| 单 skill 元数据成本 | **~100 tokens** | 规范 🅰、平台文档 🅱 | 【建议】 |
| 元数据/正文/引用 量级示例 | ~50 / ~500 / 2000+ tokens | claude.com/blog 🅰（博客示例数字，与规范的 ~100/<5000 不矛盾，是举例量级） | 【建议】 |
| 文件引用深度 | 一层 | 规范 🅰、best-practices 🅱 | 【建议】 |
| 引用文件 >100 行 | 顶部加目录（TOC） | best-practices 🅱（skill-creator 原文写的是 >300 行加 TOC，两处数字不一致，从严取 100） | 【建议】 |
| 保留字 | **`claude`、`anthropic` 不得出现在 skill 名中** | 平台 best-practices 🅱 + anthropics/skills PR #1605 实证 🅰（官方被迫将 `claude-academy-guide` 改名 `academy-guide`） | 【实现·上传校验强制】 |
| frontmatter 禁含 | XML 尖括号（`<`/`>`，防注入系统提示） | 官方 PDF 指南 🅱 | 【实现·上传校验】 |
| 路径风格 | 全部正斜杠，禁 Windows 反斜杠 | best-practices 🅱 | 【建议】 |

---

## 三、官方写作指引（anthropics/skills 仓库 + skill-creator 原文）🅰

### 3.1 官方仓库组织（github.com/anthropics/skills）🅰

- `skills/`：示例 skill，分 Creative & Design / Development & Technical / Enterprise & Communication / Document Skills（docx/pdf/pptx/xlsx 为生产级参考实现，source-available 而非开源；其余多为 Apache-2.0）
- `spec/`：规范（现主要指向 agentskills.io）
- `template/`：新建 skill 的最小模板：

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name
[instructions]

## Examples
## Guidelines
```

- README 声明：*"These skills are provided for demonstration and educational purposes only… Always test skills thoroughly in your own environment before relying on them for critical tasks."*

### 3.2 官方 skill-creator 的写作指引要点（SKILL.md 原文提取）🅰

以下全部来自官方 `skills/skill-creator/SKILL.md` 原文，是最权威的"如何写 skill"一手材料：

**description 写法**：
- "This is the primary triggering mechanism - include both what the skill does AND specific contexts for when to use it. **All 'when to use' info goes here, not in the body.**"
- **要有点"pushy"**：原文——*"currently Claude has a tendency to 'undertrigger' skills… To combat this, please make the skill descriptions a little bit 'pushy'."* 官方示例：在描述末尾追加 "Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics… even if they don't explicitly ask for a 'dashboard.'"

**语气与风格**：
- **指令用祈使句/命令式**（"Prefer using the imperative form in instructions"）
- **解释 why，而非堆砌强制词**：原文——*"Try to explain to the model why things are important in lieu of heavy-handed musty MUSTs… If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag — if possible, reframe and explain the reasoning."*（"Explain the why" 被列为改进 skill 的第 3 条核心原则；*"Today's LLMs are smart. They have good theory of mind."*）
- 写得通用而非过窄（"make the skill general and not super-narrow to specific examples"）
- 写完草稿后"以新鲜眼光再看一遍"再改进

**结构与模式**：
- 输出格式定义用 "ALWAYS use this exact template" 模式（此处大写是官方自己用的特例，针对输出模板）
- 示例用 Input/Output 对格式
- 大引用文件（>300 行）加目录；多领域 skill 按变体拆分（`references/aws.md`、`gcp.md`、`azure.md`），让模型只读相关那份
- **观察重复劳动**：如果多个测试用例里模型各自写了相似 helper 脚本，就是该把脚本收进 `scripts/` 的强信号（"Write it once, put it in scripts/, and tell the skill to use it"）

**安全红线（Principle of Lack of Surprise）**：
- skill 不得含恶意软件、漏洞利用代码；不得创建误导性 skill 或协助未授权访问、数据外泄

**开发流程（官方推荐闭环）**：
1. Capture Intent（从对话历史提取工作流：用了什么工具、步骤顺序、用户纠正、I/O 格式）
2. Interview and Research（主动问边界情况、成功标准、依赖）
3. 写草稿 → 2-3 个真实测试 prompt（"the kind of thing a real user would actually say"）
4. with-skill 与 baseline（无 skill 或旧版）**同轮**并行跑
5. 写可客观验证的 assertions（主观输出不要硬塞断言）
6. 用 eval-viewer 让人类评审，读 feedback 迭代
7. description 优化：构造 20 条 trigger eval（8-10 应触发 + 8-10 近 miss 不应触发），60/40 train/test 分割，每条 query 跑 3 次取触发率，最多迭代 5 轮，按 test 分选最优防过拟合

**触发机制原理**（skill-creator 原文）：*"Claude only consults skills for tasks it can't easily handle on its own — simple, one-step queries like 'read this PDF' may not trigger a skill even if the description matches perfectly."* → 测试 query 必须有实质复杂度。

### 3.3 平台文档 best-practices 要点 🅱（platform.claude.com，经搜索摘要）

- **命名推荐动名词（gerund）形式**："Processing PDFs"、"Analyzing spreadsheets"、"Managing databases"；可接受名词短语（"PDF Processing"）或动作导向（"Process PDFs"）；**避免** "Helper"、"Utils"、"Tools" 及过于泛化的 "Documents"、"Data"
- **description 永远第三人称**（"Always write in third person"——它会注入系统提示，视角不一致会导致发现问题）。好："Processes Excel files and generates reports"；坏："I can help you…"、"You can use this…"
- **自由度校准（Degrees of Freedom）**：任务越脆弱，指令越刚性——高自由度（多种合法路径）用文本启发式；中自由度用伪代码/参数化模板；低自由度（易错、一致性关键）用确定脚本
- **无时效性信息**：不要写 "before August 2025" 这类条件；弃用模式若保留，放进 "Old patterns" 折叠区
- **挑战每个段落**："Does this justify its token cost?"——删掉模型已经知道的概念解释（HTTP、JSON 等）
- **不给多选项不给默认值**：多个工具/库并列而不指明默认，是反模式
- **MCP 工具引用用全限定名**：`ServerName:tool_name`；依赖包显式列出，不假设已安装
- **checklist 摘要**：description 具体含关键词 + what&when；正文 <500 行；引用一层深；术语一致；示例具体；无 Windows 路径；脚本有显式错误处理、无"巫术常量"；关键操作有验证步骤；质量关键任务有反馈循环；至少 3 个评估；用 Haiku/Sonnet/Opus 都测过

### 3.4 工程博客四条建议 🅰（anthropic.com/engineering）

1. **Start with evaluation**：先在代表性任务上跑 agent、观察哪里吃力，再增量构建 skill 补短板
2. **Structure for scale**：SKILL.md 臃肿就拆文件；互斥上下文分开存以省 token；明确脚本是"直接执行"还是"读入上下文作参考"
3. **Think from Claude's perspective**：真实场景监控 skill 使用轨迹；特别注意 name 和 description（触发决策全靠它们）
4. **Iterate with Claude**：让 Claude 把成功方法与常见错误沉淀进 skill；跑偏时让它自我反思——"This process will help you discover what context Claude actually needs, instead of trying to anticipate it upfront."

安全注意：只从可信来源安装 skill；不可信来源要审计捆绑文件、代码依赖、以及指示连接外部网络的指令。

---

## 四、Skills 与 MCP 的官方分工 🅰（claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers）

官方专文回答 "How do skills and MCP work together? When should I use one versus the other?"：

- **MCP = connectivity（连接）**：标准化访问外部系统；**Skills = expertise（专长）**：领域知识与工作流逻辑
- 比喻：MCP 是五金店的货架通道（能拿到什么），skill 是店员的经验（该买什么、怎么用）
- **黄金法则（rule of thumb）原文**：*"MCP instructions cover how to use the server and its tools correctly. Skill instructions cover how to use them for a given process or in a multiserver workflow."*
- 冲突处理原文：*"Let MCP handle connectivity, and let skills handle presentation, sequencing, and workflow logic."*（如 MCP 说返回 JSON、skill 说输出 markdown 表，模型就要猜——应避免）
- 组合关系：一个 skill 可编排多个 MCP server；一个 MCP server 可支撑数十个 skill
- 工程博客（未来展望）亦确认：skills 将"complement MCP servers by teaching agents more complex workflows that involve external tools and software"

---

## 五、Claude Code 实现层扩展（与规范层的区别）🅰【实现】（code.claude.com/docs/en/skills）

Claude Code 在规范 6 字段之上扩展了大量 frontmatter 字段。**跨平台上传（claude.ai / Skills API）只能用规范 6 字段（name/description/license/compatibility/metadata/allowed-tools），否则打包硬报错 `Unexpected key(s)`。**

Claude Code 独有字段（摘要）：`when_to_use`（补充触发场景，与 description 合并后截断 1536 字符）、`argument-hint`、`arguments`、`disable-model-invocation`、`user-invocable`、`allowed-tools`/`disallowed-tools`、`model`、`effort`、`context: fork`（在隔离 subagent 中运行）、`agent`、`background`、`hooks`、`paths`、`shell`、`metadata`。

实现层要点：
- 存放位置：项目 `.claude/skills/<name>/SKILL.md`、个人 `~/.claude/skills/`、enterprise managed settings；优先级 enterprise > personal > project
- Claude Code 的 `allowed-tools` 是**当轮预批准**（不是白名单限制），支持 `Bash(git add *)` 前缀规则与 `${CLAUDE_SKILL_DIR}` 变量
- 动态上下文注入：`` !`<command>` `` 在 skill 内容送入模型前先执行并替换为输出；命令非零退出会中止整个调用
- skill 默认内联注入当前会话；`context: fork` 才进隔离 subagent（看不到对话历史，指令必须自足）

---

## 六、2025–2026 时间线与开放标准化（2026 最新变更优先）

| 时间 | 事件 | 来源 |
|---|---|---|
| 2025-10 | Anthropic 推出 Agent Skills（Claude Code / Claude apps） | 🅰 工程博客 |
| 2025-12-18 | **发布为开放标准**：agentskills.io + github.com/agentskills/agentskills + skills-ref 校验库 | 🅰 工程博客 update 标注 |
| 2025-12（同期） | MCP 捐赠 Linux 基金会（12-09）；Barry Zhang 在 AI Engineer World's Fair 演讲 "Don't Build Agents, Build Skills Instead" | 🅲 |
| 2026 年中 | **40+ 平台采用**：OpenAI Codex、Google Gemini CLI、GitHub Copilot、VS Code、Cursor、JetBrains Junie、Goose、OpenHands、Snowflake/Databricks 等；不同客户端扫描目录不同（Claude Code 用 `.claude/skills/`，Codex 等用 `.agents/skills/`，常见做法是 canonical 目录 + symlink） | 🅲（shiplight.ai、anomity.ai、agentman.ai 2026 年分析一致） |
| 2026-02~10 | anthropics/skills 持续演进：skill-creator 的 description 优化器改为 `claude -p` 子进程（去掉 ANTHROPIC_API_KEY 依赖）；官方因保留字规则将 `claude-academy-guide` 改名 `academy-guide` 并把 description 从 1176 字符压到 992 | 🅰 仓库 commit 记录 |
| 治理 | 规范无签名、无强制评审机制，`allowed-tools` 是唯一权限机制且实验性——治理被明确留给运行时与组织（有二手来源称标准已移交 Linux 基金会旗下 AAIF，未经官方一手确认） | 🅲 anomity.ai；AAIF 说法仅见 🅳 单一来源 |

---

## 七、规范硬性要求 vs 官方建议 vs 社区推断（对照表）

**【规范】硬性要求（skills-ref validate 会卡）**：
1. 目录内有且必须有 `SKILL.md`（文件名大小写敏感，官方 PDF：SKILL.MD/skill.md 均不接受 🅱）
2. frontmatter 必须有 `name`（≤64、小写+连字符、不首尾连字符、不连续连字符、与目录同名）和 `description`（1–1024 字符）
3. `compatibility` ≤500 字符（若提供）
4. `metadata` 必须是 string→string map
5. 上传 claude.ai/Skills API 时：frontmatter 只允许规范 6 字段；name 不得含 `claude`/`anthropic`；frontmatter 不得含 XML 尖括号【实现层强制】

**【建议】官方明确推荐但不强制**：
1. SKILL.md 正文 <500 行 / <5000 tokens；超出拆文件
2. description 写 what+when、第三人称、含具体触发关键词、可适度 "pushy"
3. 命名用动名词；避免 Helper/Utils/Documents 类泛名
4. 引用一层深；大引用文件加 TOC；相对路径
5. 祈使句；解释 why；避免全大写 ALWAYS/NEVER 堆砌
6. 正斜杠路径；无时效信息；术语一致；示例具体
7. 脚本自包含、显式错误处理、无巫术常量；说明脚本该执行还是该读入
8. 自由度与任务脆弱度匹配；关键工作流有验证/反馈循环
9. 开发流程：评估先行 → 草稿 → with-skill/baseline 对照 → 人类评审 → 迭代 → description 触发率优化
10. 只用可信来源 skill；安装前审计

**【社区】推断/通行做法（非官方）**：
- "MCP is for Access, Skills is for Approach"（社区口号，与官方 rule of thumb 一致但非官方措辞）
- canonical 目录 + symlink 同时兼容 `.claude/skills/` 与 `.agents/skills/`
- 保留字清单除 claude/anthropic 外是否还有别的——官方文档只明确这两个

---

## 八、与社区做法的最大分歧点（元 skill 设计需特别注意）

1. **大写强制词**：社区 skill 充斥 "YOU MUST"、"ALWAYS"、"NEVER"；官方 skill-creator 明确说这是 yellow flag，应解释 why 让模型理解（"Today's LLMs are smart. They have good theory of mind."）
2. **description 的"攻击性"**：社区倾向简短克制；官方因 undertrigger 问题明确建议 "a little bit pushy"，且要求把所有 "when to use" 信息都塞进 description 而非正文
3. **正文长度**：社区常见上千行 SKILL.md；官方三处一致要求 <500 行，把细节推入 references/
4. **name 保留字**：社区大量 `claude-xxx` 命名；官方上传校验直接拒绝（官方自己都踩坑改名）
5. **一层引用**：社区常见 a.md→b.md→c.md 引用链；官方要求一层深
6. **用 MCP 强制流程**：社区常见为"风格/流程"建 MCP server；官方明确这是越界——connectivity 归 MCP，presentation/sequencing/workflow 归 skill
7. **测试文化**：社区 skill 大多无 eval；官方 skill-creator 内置完整 eval 闭环（test prompts、with/without 对照、assertions、trigger 率优化）
8. **数字出入**：token 预算有 ~50 vs ~100（元数据）两种官方说法并存——规范以 ~100/<5000/500 行为准，博客 ~50/~500/2000+ 是量级示例

---

## 九、来源清单

| # | 来源 | URL | 可信度 | 用途 |
|---|---|---|---|---|
| 1 | Agent Skills 开放规范全文 | https://agentskills.io/specification | 🅰 一手（已抓取全文） | 字段表、name/description 细则、目录结构、渐进式披露、文件引用、skills-ref |
| 2 | agentskills.io 概览 | https://agentskills.io | 🅰 一手 | Discovery/Activation/Execution 三阶段 |
| 3 | Anthropic 工程博客：Equipping agents for the real world with Agent Skills | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills | 🅰 一手 | 设计理念、四条开发建议、安全注意、开放标准时间（2025-12-18） |
| 4 | Claude 博客：Building agents with Skills | https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work | 🅰 一手 | token 量级示例（~50/~500/2000+）、scripts as tools 理念 |
| 5 | Claude 博客：Extending Claude's capabilities with skills and MCP servers | https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers | 🅰 一手 | Skills vs MCP 分工黄金法则 |
| 6 | anthropics/skills 仓库 | https://github.com/anthropics/skills | 🅰 一手 | 仓库结构、模板、PR #1605（保留字+1024 字符实证）、持续演进记录 |
| 7 | 官方 skill-creator SKILL.md 原文 | https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md | 🅰 一手（全文抓取） | 写作指引、eval 闭环、description 优化、语气原则 |
| 8 | Claude Code 文档：Skills | https://code.claude.com/docs/en/skills | 🅰 一手 | 实现层扩展字段、allowed-tools 语法、存放位置、context: fork、动态注入 |
| 9 | 平台文档：Agent Skills overview | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | 🅱 一手经搜索摘要（区域受限） | 三级 token 表（~100/<5k/as-needed）、description 写 what+when |
| 10 | 平台文档：Skill authoring best practices | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices | 🅱 一手经搜索摘要（区域受限） | 命名（动名词）、第三人称、自由度、checklist、保留字、无 XML 标签 |
| 11 | 官方 PDF：The Complete Guide to Building Skills for Claude | https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf | 🅱 一手经搜索摘要 | SKILL.md 大小写敏感、kebab-case、frontmatter 安全限制 |
| 12 | Claude 帮助中心：如何建立自訂技能 | https://support.claude.com/zh-TW/articles/12512198 | 🅱 一手经搜索摘要 | 简单起步、示例、逐步测试、安全考量 |
| 13 | Anomity：Agent Skills Open Standard 治理分析 | https://anomity.ai/blog/agent-skills-open-standard-adoption-governance | 🅲 二手 | 40+ 采用者、治理缺口分析 |
| 14 | Shiplight：Agent Skills open standard | https://www.shiplight.ai/blog/agent-skills | 🅲 二手 | 采用清单、目录扫描差异（.claude vs .agents） |
| 15 | Agentman：Agent Skills Ecosystem 2026 | https://agentman.ai/blog/agent-skills-ecosystem-report-2026 | 🅲 二手 | 生态规模、质量/安全数据 |
| 16 | getclaudeskills：Agent Skills vs MCP | https://www.getclaudeskills.com/blog/agent-skills-vs-mcp | 🅲 二手 | 常见错误（用 MCP 强制流程等） |

**黑名单遵守声明**：本次调研未使用知乎、微信公众号、百度百科、CSDN 任何内容。

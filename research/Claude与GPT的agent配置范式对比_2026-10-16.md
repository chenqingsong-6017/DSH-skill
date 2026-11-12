# Claude（Anthropic）vs GPT（OpenAI）：Agent 配置范式对比

> 调研日期：2026-10-16｜用途：为本工作区「skill 工厂」找对标基准。
> 来源分级：★官方一手（Anthropic/OpenAI 文档）＞◆深度对比文（博客，二手，供交叉验证）。

## 一、一句话结论

两家范式根本不同：
- **GPT**＝全局文本前缀（自定义指令）＋自动记忆＋Custom GPTs。强在被动记忆、生态广、移动端；弱在碎片化、指令漂移、记忆被指"黑盒"。
- **Claude**＝文件化、分层、按需触发的 Skills＋CLAUDE.md＋结构化记忆＋Hooks。强在深度、精确遵循、长上下文(1M)、可组合、可验证；历史上弱在跨会话记忆（2026-03 起已补内置 Memory）。
- **本工厂对标**：WorkBuddy 配置 ≈ SOUL.md(CLAUDE.md)＋用户级 Skills(Claude Skills)＋MEMORY.md/memory-bank(记忆层)＋防错双闸(hooks)。选的正是 Claude 这条更深、更可控、可扩展的架构（veracalloway：「architecture, not configuration」；prompttly：「scalable, composable toolkit」）。

## 二、对比表

| 维度 | Claude（Anthropic） | GPT（OpenAI） |
|---|---|---|
| **人设/指令载体** | CLAUDE.md / AGENTS.md：本地 md，每次会话读入，**视为上下文非强制配置** | 自定义指令：两栏文本框（关于你 / 如何回复），全局注入 |
| **容量/上限** | 单文件建议 <200 行（更长降低遵循度） | 自定义指令：Free/Go 1,500 字；付费 5,000 字（**见冲突标注**）；API 无对应（用 system message） |
| **技能机制** | Skills：SKILL.md 文件包，按 description 触发或斜杠命令，**渐进披露懒加载**，命中前零开销 | Custom GPTs：封装知识+行为，GPT Store 分发 |
| **记忆** | 自动记忆（~/.claude/projects/\<repo\>/memory/，结构化可编辑）＋ Productivity 插件显式记忆文件 | Memory：对话中自动记，用户可管（"remember/forget"），但被指"黑盒" |
| **作用域/开销** | 按需触发，未命中不占 token | 全局注入每个对话（每轮约消耗 token） |
| **一致性保障** | `/doctor prompt-audit` 审计过期/冲突指令；矛盾规则会被模型"任意采纳" | 依赖用户自己维护 |
| **验证闭环** | 官方 #1 tip：给 agent 自我验证手段（命令/测试/浏览器），质量飞跃 | 无内建等价机制 |
| **强项** | 深度、精确遵循、长上下文、可组合、可验证 | 被动记忆、生态广、移动端、多模态(DALL-E) |
| **弱项** | 跨会话记忆历史上弱（已补） | 指令漂移、记忆黑盒、配置碎片化 |

## 三、权威来源

- ★ Anthropic 官方 memory 文档（docs.anthropic.com/en/docs/claude-code/memory）：CLAUDE.md 写法（<200 行、具体可验证、"Use 2-space indent" 非 "Format properly"、矛盾→任意采纳、path-scoped rules、@imports）、自动记忆机制、/doctor prompt-audit。
- ★ Claude Code power user tips（support.claude.com）：Compounding Engineering（每次纠正→回写 CLAUDE.md）、验证闭环为 #1 tip、子代理隔离主上下文、Skills 应"一天做超一次就固化成 skill"。
- ★ OpenAI Academy「Personalizing ChatGPT」+ OpenAI Help「记忆」：自定义指令 vs Memory 区别、Projects、Skills 概念引入。
- ◆ agentpill.com：Claude vs ChatGPT 个性化正面对比（GPT 被动记忆胜、Claude 深度/遵循胜）。
- ◆ veracalloway.com：Claude skill 文件＝"competency installations"，分层 29 条规则，"architecture, not configuration"。
- ◆ prompttly.com：Custom Instructions vs Claude Skills——后者是"可扩展、可组合的 toolkit"，前者是"单一文本框"；给出各平台 token 开销对比。
- ◆ adersaytech.com：自定义指令 5,000 字新制（付费）。**与 prompttly 的 3,000 字（2×1,500）冲突，见下。**

## 四、冲突标注（未核实）

OpenAI 自定义指令字数上限存在三说：① adersaytech 称付费 5,000 字、免费 1,500 字；② prompttly 称 2×1,500＝3,000 字上限；③ OpenAI 官方仅说"apply to new conversations"，未在我抓取页明示具体数字。**结论：具体数字未核实，以你账号实际方案为准。** 这恰恰印证我们 skill 工厂的一条铁律——外部数字先现查、标采集日期。

## 五、可搬进工厂的具体做法（含我们现状）

| # | 做法（来源） | 我们现状 | 动作 |
|---|---|---|---|
| 1 | CLAUDE.md 写法铁律：具体可验证、<200 行、标题+项目符号、矛盾→任意采纳（★Anthropic） | 已对齐：SOUL.md 104 行；"条款打架"清单正是把"矛盾→任意采纳"变成可勾选防护 | 维持 |
| 2 | Compounding Engineering：每次纠正→回写 CLAUDE.md（◆power tips） | 已建：ai-config-upgrade v3「从真实使用吸收反馈／回填 cases.md」 | 维持，扩到所有 skill |
| 3 | 自动化 prompt-audit：定期查过期/冲突指令（★/doctor prompt-audit） | 部分：security-audit + skill-dev `skill_check.py` 已存在 | **补：固化为工厂流水线"定期审计"环节** |
| 4 | 验证闭环＝质量第一 tip（◆power tips） | 已对齐：skill-dev Phase4 四道验证、macos 无头截图验收 | 维持 |
| 5 | 子代理隔离主上下文（offload 保干净） | 已对齐：调研子代理≤800 字摘要（约定#5） | 维持 |
| 6 | 记忆分层：手写指令 vs 自动记忆分离（★Anthropic） | 部分：MEMORY.md(手写)+daily log；未显式区分"自动沉淀的教训" | **补：仿 auto-memory 做"教训自动沉淀"层** |
| 7 | OpenAI 自定义指令"关于你/如何回复"两栏结构（★OpenAI） | 已对齐：SOUL 有 Identity/Style | 维持 |
| 8 | 记忆隐私分级：敏感数据不自动存（◆OpenAI help） | 部分：硬规则4 已筛注入；未明示"不把密钥写入记忆" | **补：记忆写入加隐私分级条款** |

## 六、对工厂的判定

- **我们选的 Claude 模型是对的**：研究一致表明文件化+分层+按需触发的架构在深度、可控性、可扩展性上优于 GPT 的全局文本前缀。veracalloway 原话："architecture, not configuration"。
- **最该补的两块**：③ 定期 prompt-audit 环节、⑥ 教训自动沉淀层、⑧ 记忆隐私分级——这三项是 GPT/Claude 都有、我们尚缺或弱的。
- **失效条件**：若 WorkBuddy 未来引入"全局自动记忆"且默认开启，需重评记忆分层策略（防黑盒化），届时回看本笔记第 6 项。

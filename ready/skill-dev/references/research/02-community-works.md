# 02 · 社区优质 Agent Skill 作品与方法论调研

> 调研日期：2026-10-15 ｜ 调研人：general-purpose-2
> 目的：提炼「好 skill 长什么样」的共性模式，用于构建「开发新 Skill」的元 skill
> 信息源黑名单已执行：未使用知乎、微信公众号、百度百科、CSDN
> 星数均为 2026-10-15 当天通过 shields.io API 实时查询（`img.shields.io/github/stars/<repo>.json`）

---

## 目录

1. [关键仓库星数速览（2026-10-15 现查）](#一关键仓库星数速览2026-10-15-现查)
2. [obra/superpowers：writing-skills 元 skill 方法论全解剖](#二obra/superpowerswriting-skills-元-skill-方法论全解剖)
3. [awesome 系列清单：高口碑 skill 的类型分布](#三awesome-系列清单高口碑-skill-的类型分布)
4. [知名第三方 skill 解剖（3 例 + 1 中文圈案例）](#四知名第三方-skill-解剖)
5. [社区批评与真实教训（HN / 博客 / 官方讨论）](#五社区批评与真实教训)
6. [综合提炼：好 skill 的共性模式与失败写法](#六综合提炼好-skill-的共性模式与失败写法)
7. [来源清单（含可信度分级）](#七来源清单含可信度分级)

---

## 一、关键仓库星数速览（2026-10-15 现查）

| 仓库 | Stars | 定位 |
|---|---|---|
| obra/superpowers | **299k** | 技能框架 + 方法论（Jesse Vincent） |
| anthropics/skills | **181k** | Anthropic 官方 skill 集（含 docx/pdf/pptx/xlsx 生产级 skill） |
| addyosmani/agent-skills | 107k | Addy Osmani（Google）个人 skill 集 |
| ComposioHQ/awesome-claude-skills | 77k | 收录 1000+ skill 的清单（Apache-2.0） |
| mvanhorn/last30days-skill | 64k | 单 skill：扫 Reddit/X 近 30 天舆情 |
| blader/humanizer | 57k | 单 skill：去除 AI 写作指纹（29 种模式） |
| K-Dense-AI/scientific-agent-skills | 50k | 140 个科研 skill |
| sickn33/antigravity-awesome-skills | 48k | 1410+ skill 合集（跨平台） |
| VoltAgent/awesome-agent-skills | 36k | 收录 1497+ skill，人工精选（MIT） |
| alchaincyf/nuwa-skill | 34k | 中文圈：人物认知蒸馏 skill（花叔） |
| openai/skills | 28k | OpenAI 官方 Codex skill 目录 |
| muratcankoylan/Agent-Skills-for-Context-Engineering | 18k | 上下文工程方法论 |
| travisvn/awesome-claude-skills | 15k | 社区导向清单，FAQ/最佳实践详细 |
| obra/superpowers-skills | 751 | superpowers 社区可编辑 skill 库 |
| karanb192/awesome-claude-skills | 550 | 50+ 验证 skill 合集 |

**观察**：星数最高的单体作品分两类——(a) 框架/方法论（superpowers 299k、anthropics/skills 181k）；(b) 单一尖锐问题 skill（last30days 64k、humanizer 57k）。纯汇编清单天花板约在 15k–77k。方法论价值密度 > 收录数量。

---

## 二、obra/superpowers：writing-skills 元 skill 方法论全解剖

来源：`https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md`（一手，官方仓库 main 分支，2026-10-15 抓取）
背景：`https://blog.fsck.com/2025/10/09/superpowers/`（一手，作者博客 2025-10-09 发布稿）

### 2.1 核心命题：写 skill = 对流程文档做 TDD

> **"Writing skills IS Test-Driven Development applied to process documentation."**
> **"If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing."**（没看过 agent 在没有该 skill 时失败，你就不知道这个 skill 教的对不对。）

**铁律（The Iron Law）**：`NO SKILL WITHOUT A FAILING TEST FIRST`。新建与编辑同罪；未测就写 → 删除重来，无例外（"simple addition"、"just a section"、"docs update" 均不豁免；Delete means delete）。

### 2.2 TDD 概念映射表

| TDD | Skill 开发 |
|---|---|
| 测试用例 | 用 subagent 跑压力场景 |
| 生产代码 | SKILL.md 本文 |
| RED（测试失败） | 无 skill 时 agent 违规（基线行为） |
| GREEN（通过） | 有 skill 时 agent 合规 |
| REFACTOR | 堵新出现的借口漏洞，保持合规 |
| 先写测试 | 写 skill 前先跑基线场景 |
| 观察失败 | 逐字记录 agent 的合理化借口 |
| 最小实现 | 只针对**已观察到的**违规写，不为假想情况加戏 |

### 2.3 压力测试：四类 skill × 四种压力

**skill 分类及各自测试法**：

| 类型 | 例子 | 测试方式 | 成功标准 |
|---|---|---|---|
| Discipline-Enforcing 纪律类 | TDD、verification-before-completion | 学术提问 + 压力场景 + 多重压力组合 + 借口反驳 | 最大压力下仍遵守 |
| Technique 技术类 | condition-based-waiting | 应用场景 + 变体 + 信息缺失 | 能迁移到新场景 |
| Pattern 模式类 | reducing-complexity | 识别场景 + 应用 + 反例 | 知道何时用/不用 |
| Reference 参考类 | API 文档 | 检索 + 应用 + 缺口测试 | 找得到且用得对 |

**压力类型**：time（时间）、sunk cost（沉没成本）、authority（权威）、exhaustion（疲惫）。纪律类 skill 需 3+ 压力组合。

**作者博客中的两个经典压力场景原文**（blog.fsck.com，一手）：

```
场景1（时间压力+自信）：生产系统宕机，每分钟损失 $5k。
A) 直接调试（5 分钟修好） B) 先查 skills/debugging/（2+5=7 分钟）。选哪个？
场景2（沉没成本+已能跑）：你花 45 分钟写的异步测试基建能跑了，partner 让你提交。
A) 查 skills/testing/ 的异步测试 skill B) 直接提交能跑的方案。
```

作者发现：第一次让 Claude 测试 subagent 时，Claude 用「游戏竞答式提问」敷衍（"gotten a perfect score"），改为真实压力场景后才有效——**测试本身也要防 agent 敷衍**。

### 2.4 措辞微测试（Micro-Test Wording）

跑完整压力场景前的廉价迭代手段，5 条规则：
1. 每次调用用全新上下文样本；
2. **必须含无指导对照组**——对照组不失败则没什么可修，停止；
3. 每变体 5+ 次重复（单样本会撒谎）；
4. 人工阅读每个命中（模板回显会伪装成命中）；
5. **方差也是指标**——5 次重复 5 种解读 = 措辞无约束力。

### 2.5 失败形式匹配（Match the Form to the Failure）——最独特的洞见之一

| 基线失败类型 | 正确形式 | 错误形式 |
|---|---|---|
| 压力下故意跳过规则 | 禁令 + 借口对照表 + 红旗清单 | 软性指导（"prefer..."、"consider..."） |
| 遵守了但输出形状错 | **正面配方/契约**（说清输出是什么、分几部分、什么顺序） | 禁令清单（"don't restate"）——agent 会跟 don't 讨价还价，实测比无指导还差 |
| 遗漏必需元素 | 模板中设 REQUIRED 字段/槽位 | 散文式提醒 |
| 行为依赖条件 | 键于**可观察谓词**的条件句 | 无条件规则 + 豁免条款 |

配套规则：**No nuance clauses**（"Don't X unless it matters" 会重开谈判）；**豁免条款不起限定作用**（"此限制不适用于代码块" 仍会抑制代码块，应重构使规则触及不到它）。

### 2.6 防合理化加固工具包（针对纪律类失败）

1. **明确堵死每个已知漏洞**。❌ `Write code before test? Delete it.` ✅ 追加 "No exceptions: Don't keep it as 'reference' / Don't 'adapt' it / Don't look at it / Delete means delete."
2. **切断字面 vs 精神之争**："Violating the letter of the rules is violating the spirit of the rules."
3. **借口对照表**：基线测试捕获的借口逐字进表 + 反驳。
4. **红旗清单**：让 agent 可自查（"Code before test"、"I already manually tested it"、"This is different because..." → All of these mean: Delete code. Start over.）。
5. **心理学依据**：`persuasion-principles.md` 引用 Cialdini《Influence》与 Meincke et al. 2025（ persuasion 技术使 LLM 对硬性请求的遵从率从 33% 提升到 72%，28000 段对话）。映射：权威（"YOU MUST"、"No exceptions"）、承诺（"Announce which skill you're using"、TodoWrite 检查单）、稀缺（"Before proceeding"、"IMMEDIATELY after X"）、社会认同（"Every time"、"X without Y = failure"）、共同体（"we're colleagues"）。

### 2.7 writing-skills 列出的反模式（原文）

| 反模式 | 为什么差 |
|---|---|
| ❌ Narrative Example（"In session 2025-10-03, we found..."） | 太具体不可复用 |
| ❌ Multi-Language Dilution（example-js/py/go 各一份） | 质量平庸 + 维护负担 |
| ❌ Code in Flowcharts | 无法复制粘贴 |
| ❌ Generic Labels（helper1、step3） | 标签应有语义 |

### 2.8 description 写法（SDO, Skill Discovery Optimization）——最独特的洞见之二

**关键实证发现**：description 若总结工作流，agent 会照 description 行事而**不读 skill 正文**（实例：description 写 "code review between tasks" 导致只做一次审查，尽管流程图要求两次）。

- ❌ 总结工作流 / ❌ 过程细节 / ❌ 太抽象（"For async testing"）/ ❌ 第一人称 / ❌ 提及非专属技术（setTimeout）
- ✅ `description: Use when [具体触发条件与症状]`，只写触发条件，第三人称，描述**问题**（race conditions）而非**语言症状**，技术无关化；≤500 字符（上限 1024）。

### 2.9 其他可操作的写法规则

- **Token 预算**：getting-started 工作流 <150 词/个；常加载 skill 总共 <200 词；其他 <500 词。
- ❌ 罗列所有 CLI flag → ✅ "Run --help for details"；❌ 重复别的 skill 的流程 → ✅ `**REQUIRED SUB-SKILL:** Use superpowers:test-driven-development`；❌ 用 `@path/SKILL.md` 强制加载语法（提前烧掉 200k+ 上下文）。
- 命名：动词优先主动语态（`condition-based-waiting` ✅ / `async-test-helpers` ❌）。
- 脚本调用经解释器（`bash scripts/tool.sh`），**绝不裸路径**（harness 打包器会剥可执行位 → Permission denied）。
- 代码示例："One excellent example beats many mediocre ones"——完整可运行、注释解释 WHY、真实场景。
- 流程图只用于：非显而易见决策点、防过早停止的循环、A/B 选择；绝不用于参考材料（用表格）、代码、线性指令。
- Discovery Workflow：agent 找 skill 的路径是「grep description → 扫概述 → 读快速参考表 → 实现时才加载示例」——可搜索关键词要尽早、频繁出现。

---

## 三、awesome 系列清单：高口碑 skill 的类型分布

### 3.1 三份主流清单对比

| 清单 | Stars (10-15 查） | 规模 | 特点 |
|---|---|---|---|
| ComposioHQ/awesome-claude-skills | 77k | 1000+ | 分类清晰（约 10 大类）；对渐进式披露解释最好；有 maintainer 推广倾向需注意 |
| VoltAgent/awesome-agent-skills | 36k | 1497+ | "Hand-picked, not AI-slop generated"；按来源团队组织；收 8+ 平台 |
| travisvn/awesome-claude-skills | 15k | 精选 | FAQ 与最佳实践最详细；社区导向 |

### 3.2 被反复收录的高口碑 skill 类型（交叉比对三份清单 + VoltAgent 收录统计）

1. **文档处理**：anthropics 官方 docx/pdf/pptx/xlsx（181k 仓库内的生产级 skill，全部清单首位收录）
2. **方法论/流程纪律**：obra/superpowers 全家（brainstorming、writing-plans、TDD、systematic-debugging、subagent-driven-development）
3. **前端/设计品质**：anthropics/frontend-design（反 AI slop）、ui-ux-pro-max-skill（161 条行业规则）、Impeccable
4. **安全**：Trail of Bits 21 个（static-analysis、semgrep-rule-creator、building-secure-contracts）
5. **测试/浏览器自动化**：openai/playwright、webapp-testing、TestMu AI 49 个框架 skill
6. **厂商最佳实践**：stripe-best-practices、cloudflare/agents-sdk、expo/building-native-ui、supabase、sentry-workflow（28 个）
7. **去 AI 味/写作**：blader/humanizer（57k，29 种 AI 写作指纹模式）
8. **调研/情报**：mvanhorn/last30days-skill（64k，Reddit+X 30 天扫描）、firecrawl
9. **人物/方法论蒸馏**：alchaincyf/nuwa-skill（34k，中文圈标杆）
10. **元 skill**：anthropics/skill-creator 与 microsoft/skill-creator 被双方各自收录——**生态入口级**

### 3.3 VoltAgent 的收录质量标准（CONTRIBUTING.md，一手）

- 公开仓库 + 可用 skill + 文档（README 或 SKILL.md）
- 名称带 author/org 前缀；description ≤10 词
- **"Skill must have real community usage… Brand new skills that were just created are not accepted. Give your skill time to mature and gain users before submitting."**（新建成品不收，需成熟与用户验证）

### 3.4 高口碑 SKILL.md 的共性结构（跨清单抽样）

- frontmatter 仅 name + description（docx 加了 license）
- 开头一段「何时用我」或任务路由表
- 快速参考表（Quick Reference）
- 明确的验证/检查步骤（verify the output）
- 常见错误/gotchas 清单
- 重型内容外置 scripts/ 与 references/，SKILL.md 保持精简

---

## 四、知名第三方 skill 解剖

### 4.1 anthropics/skills → docx（生产级，source-available）

来源：`https://raw.githubusercontent.com/anthropics/skills/main/skills/docx/SKILL.md`（一手）

**frontmatter**：name + 超长 description（列举触发词：'Word doc'、'.docx'、'report'、'memo'… + **明确排除项**："Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks"）+ license 字段。

**正文结构**（总长仅约 150 行）：
1. **任务路由表**开头：Create → 写 docx-js 脚本；Edit → unzip→改 XML→zip（并说明原因 "docx-js cannot open existing files"）；Read → `pandoc -t markdown`
2. **gotchas 清单**（11 条 footgun：A4 默认页面、表格双宽度、ShadingType.CLEAR 不用 SOLID、绝不字面插入 `•`、绝不使用 `\n`…）——只写「模型知道 API，这些是坑」，不重复教程
3. **Verify the output 章节**：`soffice --convert-to pdf` + `pdftoppm` 渲染成图 + Read 查看——**强制视觉验证检查点**
4. **安全细节**：解包后 `find unpacked -type l -delete` 剥离符号链接（"docx from external parties is untrusted"）
5. **验证脚本**：`validate.py --original`（XSD 校验 + --auto-repair；redlining 时 `--author` 检查每处改动都有 `<w:ins>/<w:del>` 包裹）
6. 已知工具缺陷坦白（pandoc 不合并段落、accept_changes.py 的例外情况）+ 如何分辨「视图伪影 vs 文档缺陷」

**借鉴点**：路由表先行；gotchas 只写反直觉项；每个产出物都有机器可执行的验证步骤与「渲染后亲眼看」的检查点；对外部输入做不信任假设。

### 4.2 anthropics/skills → frontend-design（反 AI slop 标杆）

来源：`https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md`（一手）

- **角色定调开头**："Approach this as the design lead at a design studio known for giving every client a distinct visual identity…"——用身份设定替代规则堆砌
- **正面原则**（typography carries personality；line length <80；motion sparingly…）+ **5 组具名 AI slop 特征**（精确到 hex 值：暖奶油底 #F4F1EA + 陶土 accent #D97757；酸绿单色 accent；SaaS-card kit：统一圆角 + rgba(0,0,0,.1) 阴影 + 渐变洗；tracked-out ALL-CAPS eyebrow；'A · B · C' 中点串…）并注明 "All traits are legitimate for some briefs, but they are defaults rather than choices"——**反模式写成可识别的具名特征，而非抽象禁令**
- **内置自检流程**：两阶段（先设计 token 计划 → 对照 brief 自审「是否像对任何类似页面都会产生的默认」→ 通过才写代码）；"a picture is worth 1000 tokens"（截图自评）
- **brief 优先权声明**："the brief's own words always win"——规则与用户需求冲突时的裁决条款

**借鉴点**：反模式给**具体可检测的特征**（hex 值、版式名），配「何时这些也合理」的边界；流程中内置「对照原始需求自审」检查点。

### 4.3 anthropics/skills → skill-creator（官方元 skill）

来源：`https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md`（一手）

与 superpowers writing-skills 互补的官方方法论：

- **九步核心循环**：意图 → 草稿 → 测试 prompt → with-skill 与 baseline **同轮并行**跑 → 定量 assertions + 定性评估 → viewer 审阅 → 重写 → 扩大测试集 → description 优化
- **description 要"稍 pushy"**：因当前 Claude 倾向 undertrigger，官方建议在描述后追加 "Make sure to use this skill whenever the user mentions X, Y, Z, even if they don't explicitly ask for…"——与 superpowers「description 只写触发条件」一致，但更鼓励主动堆触发词
- **Description Optimization 子流程**：20 条查询（8-10 should-trigger + 8-10 should-not-trigger），强调**近似误判（near-misses）最有价值**（共享关键词但需别的工具）；每条跑 3 次取触发率；60/40 train/test 划分，**按 test 分数选 description 防过拟合**
- **写作风格**：祈使句；**解释 why 而非堆砌 MUST/NEVER**（全大写 ALWAYS/NEVER 是"黄旗"）——注意这与 superpowers 纪律类 skill 的强硬风格相反，差异在于 skill 类型：纪律类用禁令，技术/知识类用解释
- **Principle of Lack of Surprise**：不得藏恶意代码、不得隐瞒意图
- **正文 <500 行**；>300 行参考文件附目录；多领域按变体拆分（references/aws.md、gcp.md…）

### 4.4 中文圈案例：alchaincyf/nuwa-skill（34k stars）

来源：GitHub 归档笔记 `https://github.com/ImChong/Robotics_Notebooks/blob/.../sources/repos/nuwa-skill.md` + 头条报道（二手，可信度中）

- 定位「非角色扮演」：蒸馏人物**认知操作系统**而非语录复读——五层提取（表达 DNA → 心智模型 → 决策启发式 → 反模式 → 诚实边界）
- **三重验证收录标准**：跨 2+ 领域出现、对新问题有预测力、有排他性（非常识）
- **质量验证设计**：已知问题方向一致 + **未知问题表现适度不确定**（诚实边界）——把「不瞎编」写成可验收标准
- 官方 skill 经双 agent 盲测保真度 ≥85（A 级）；SKILL.md 核心不接受外部 PR（质量守门）

**借鉴点**：skill 可以自带「保真度评分卡」；把「何时应表达不确定」写进验收标准，是对抗 hallucination 的可操作写法。

---

## 五、社区批评与真实教训

### 5.1 触发不可靠（最集中的抱怨）

来源：HN 线程 `https://www.hn.zip/item/46871173`（Agent Skills，一手讨论）、`https://better-hackernews.vercel.app/item?id=47142004`、`http://hacker-news-clone-next-js.vercel.app/story?id=47139902`（2026-02，Hugging Face Skills 发布帖）

- "Skills in CC have been a bit frustrating for me. **They don't trigger reliably** and the emphasis on 'it's just markdown' makes it harder to have them reliably call certain tools with the correct arguments."（高赞）
- "I have a skill called 'X doer', and then I write 'Open and do X', it almost never loads up the skill. I have to rewrite as 'Open and do X **using the X doer skill**'."——多人复现同样体验
- 有用户提到线程中引用的数据：**56% non-invocation rate**（非调用率）
- **有效对策（社区共识）**：
  - frontmatter description 写成「shibboleth」暗号："use when mentioning X" 绑定特定关键词（btown，高赞）
  - 用 hooks（startup|resume|clear|compact 时注入提醒）做确定性兜底，而非全靠模型"看心情"（slhck、smithkl42：description 写 "Do not activate unless instructed by guidance"，由 hook 按文件类型触发）
  - 复杂逻辑不要放 markdown，**剥离到脚本/API**，skill 只做调用说明书（PantaloonFlames、RyanShook："CLI 相关的 skill 加载可靠，纯文档型 skill 不行——不与 agent 想做的动作绑定的文档很难被加载"）

### 5.2 「skill ≠ 最佳实践文档」

HN `hn.zip/item/46871173` 高赞（philipp-gayret 串内）：

> "**What doesn't work: skills as general guidelines or 'best practices' documents.** These get lost in context or ignored entirely because the agent has no clear signal for when to apply them. The mental model shift: think of skills less like documentation and more like **subroutines you'd explicitly invoke**. If you wouldn't write a function for it, it probably shouldn't be a skill."

配套观点：commands 是原子操作（lint/deploy），skills 是多步决策树；progressive disclosure 在 20+ 能力竞争上下文时才有意义。

### 5.3 上下文膨胀与系统提示打架

- "having way too much context, so that the skills effectively disappear"（empath75）
- "the smaller the system prompt, the more likely the agent is to follow the skills without issue"（mccoyb，推崇 pi 的极简系统提示实现）
- "I think this is mostly a problem of **making things skills that don't need to be skills** (telling it how to do something it already knows how to do)"（empath75）——给模型教它已会的东西 = 纯膨胀
- 另一线程（`brianlovin.com/hn/46038047`）：指令埋在 CLAUDE.md 里被无视，"It immediately knows the command… notices an issue and fixes it correctly the second time"——**位置与显著性 > 内容正确性**；对策是把机械性检查做成 hooks 确定性执行，而非依赖 vibe

### 5.4 模型代际解释

- "The current generation of SotA models wasn't RLVR-trained on skills… The next generation will have likely been RLVRed on tasks where skills are available, and will use them much more reliably."（oulu2006）——部分触发问题是训练数据问题，会随模型换代缓解；写作规范仍是当下可控变量

### 5.5 Simon Willison 的评价（权威个人博客，一手）

`https://simonwillison.net/2025/Oct/16/claude-skills/`（2025-10-16）：
- "Claude Skills are awesome, maybe a bigger deal than MCP"——核心论据是**简单性**："They outsource the hard parts to the LLM harness"；任何能读文件系统的 agent 都能用（他实测 Codex CLI / Gemini CLI 直接读 pdf/SKILL.md 可用）
- 预见了批评："I've seen some push back against skills as being so simple they're hardly a feature at all"（与 AGENTS.md 无本质区别论）——他的回应：简单正是重点

`https://simonwillison.net/tags/anthropic`（2025-12-19）：Agent Skills 成为开放标准（agentskills.io），但 "deliciously tiny… **heavily under-specified**"（metadata、allowed-tools 字段语义模糊）——规范本身留白多，写作约定靠社区 best practice 补齐。

### 5.6 Anthropic 官方工程博客（一手，官方）

`https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills`（2025-10-16）：

- **Progressive disclosure 是核心设计原则**：三级加载（frontmatter → SKILL.md 正文 → 捆绑文件），上下文量"effectively unbounded"
- "Pay special attention to the `name` and `description`… Claude will use these when deciding whether to trigger"——触发判断**只凭这两行**
- **不要凭空预判上下文需求**："discover what context Claude actually needs, instead of trying to anticipate it upfront"——先跑代表性任务观察卡壳点，再增量构建
- 监控真实使用轨迹（unexpected trajectories、overreliance on certain contexts）并迭代；让 Claude 自己把成功方法与常见错误回填进 skill
- **代码的双重角色必须说清**：脚本是「直接执行的工具」还是「读入上下文的参考文档》，要显式区分
- 安全：只装可信来源；审计捆绑文件；警惕指示连接不可信外部网络的指令

---

## 六、综合提炼：好 skill 的共性模式与失败写法

### 6.1 好 skill 的 8 条共性模式

1. **触发条件工程化**：description 只写「何时用」且写足症状词/近义词/排除项；官方甚至鼓励"稍 pushy"。实证依据：description 总结工作流会导致 agent 跳过正文（superpowers 实测）；触发判断只凭这两行（Anthropic）。
2. **先测后写（TDD for skills）**：先跑无 skill 基线场景记录失败，再针对**已观察到的**失败写最小内容；with-skill 与 baseline 同轮对照（superpowers RED-GREEN 与官方 skill-creator 九步循环同构）。
3. **形式匹配失败类型**：纪律失败 → 禁令+借口表+红旗清单；形状失败 → 正面配方/输出契约；遗漏 → REQUIRED 槽位；条件行为 → 键于可观察谓词的条件句。禁令对塑形问题适得其反（实测比无指导更差）。
4. **检查点机器可执行**：每个产出物配验证步骤（docx：渲染成图亲眼看；validate.py --original；redlining --author 审计）——"Evidence over claims"（superpowers 四信条之一）。
5. **渐进式披露 + 外置重量**：SKILL.md <500 行/词预算明确；scripts（可执行，不占上下文）与 references（按需加载）分离；互斥内容拆文件；>300 行参考附目录。
6. **gotchas 只写反直觉项**：不重复模型已知的 API 教程，只列 footgun（docx 的 11 条）；"给模型教它已会的东西 = 上下文膨胀"（HN）。
7. **反模式写成可检测特征**：不只说"避免 AI 味"，而是给 5 组具名特征精确到 hex 值（frontend-design）；借口逐字记录进对照表（superpowers）。
8. **冲突裁决与诚实边界**：规则与需求冲突时谁赢（"the brief's own words always win"）；何时应表达不确定（nuwa-skill 的保真度验收："未知问题表现适度不确定"）。

### 6.2 最常见的 5 种失败写法

1. **description 写错**：总结工作流 / 太抽象（"For async testing"）/ 第一人称 / 漏触发词 / 漏排除项 → 不触发或过度触发（HN 56% 非调用率）。
2. **写成最佳实践文档**：通用 guideline 型 skill 无明确应用信号，"get lost in context or ignored entirely"——"如果你不会为它写一个函数，它就不该是一个 skill"。
3. **叙事式/教程式内容**："In session 2025-10-03, we found…" 不可复用；多语言示例稀释；罗列所有 CLI flag；重复其他 skill 的流程。
4. **软性指导配纪律问题**（或反向）："prefer/consider" 在压力下必被跳过；而 MUST/NEVER 堆砌用于知识类 skill 又是"黄旗"（官方 skill-creator）——形式与失败类型错配是最隐蔽的失败。
5. **未测试就部署**：只凭"显然清楚"、"只是参考"、"我有信心"跳过验证（superpowers 列出 8 种借口）；以及测试本身被敷衍（"游戏竞答式提问"式假测试）。

### 6.3 值得借鉴的章节设计（可直接复用的骨架）

```
---
name: verb-first-name
description: Use when [症状/触发词/近义词] ... Do NOT use for [排除项]
---
# 标题
[角色定调或一句话核心原则]
## 任务路由表（When to use which approach）   ← docx 模式：决策先行
## 核心流程/配方（正面契约：输出是什么、几部分、什么顺序）
## Quick Reference（表格，可 grep）
## Gotchas / Common Mistakes（只写反直觉项 + 修复）
## Red Flags - STOP（纪律类：借口对照表 + "All of these mean: ..."）
## Verify（机器可执行检查点：脚本命令 + 渲染亲眼看）
## 边界与裁决（何时不适用 / 规则冲突时谁赢 / 何时应表达不确定）
## References（>300 行附目录；scripts 与 references 显式分角色）
```

---

## 七、来源清单（含可信度分级）

| # | 来源 | URL | 可信度 | 用途 |
|---|---|---|---|---|
| 1 | obra/superpowers writing-skills SKILL.md（main 分支原文） | https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md | ★★★ 一手/官方仓库 | TDD 方法论、SDO、反模式、检查单 |
| 2 | Jesse Vincent 博客发布稿（2025-10-09） | https://blog.fsck.com/2025/10/09/superpowers/ | ★★★ 一手/作者 | 压力场景原文、Cialdini 应用缘起 |
| 3 | anthropics/skills 仓库 README | https://github.com/anthropics/skills | ★★★ 一手/官方 | 官方 skill 集结构、template、Apache-2.0/source-available 区分 |
| 4 | docx SKILL.md 原文 | https://raw.githubusercontent.com/anthropics/skills/main/skills/docx/SKILL.md | ★★★ 一手/官方 | 生产级 skill 解剖 |
| 5 | frontend-design SKILL.md 原文 | https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md | ★★★ 一手/官方 | 反 AI slop 写法解剖 |
| 6 | skill-creator SKILL.md 原文 | https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md | ★★★ 一手/官方 | 官方元 skill：eval 流程、description 优化 |
| 7 | Anthropic 工程博客：Equipping agents for the real world（2025-10-16） | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills | ★★★ 一手/官方 | 渐进式披露、迭代发现上下文、安全审计 |
| 8 | VoltAgent/awesome-agent-skills README + CONTRIBUTING.md | https://github.com/VoltAgent/awesome-agent-skills | ★★★ 一手仓库 | 收录类型分布、质量标准（成熟度门槛） |
| 9 | travisvn/awesome-claude-skills README | https://github.com/travisvn/awesome-claude-skills | ★★★ 一手仓库 | FAQ、Skills vs Prompts/Subagents/MCP 对比 |
| 10 | ComposioHQ/awesome-claude-skills | https://github.com/ComposioHQ/awesome-claude-skills | ★★★ 一手仓库（注意 maintainer 推广） | 分类体系、渐进式披露解读（经 zendot.org 二手转述补充） |
| 11 | HN：Agent Skills 讨论（56% 非调用率、skill≠文档论） | https://www.hn.zip/item/46871173 | ★★ 社区一手言论 | 失败模式实证 |
| 12 | HN：Hugging Face Skills 讨论（触发不可靠、hooks 对策） | https://better-hackernews.vercel.app/item?id=47142004 ；http://hacker-news-clone-next-js.vercel.app/story?id=47139902 | ★★ 社区一手言论 | 触发问题与工程化对策 |
| 13 | HN：Claude Advanced Tool Use 讨论（上下文位置、hooks 确定性） | https://brianlovin.com/hn/46038047 | ★★ 社区一手言论 | 上下文膨胀、指令被无视 |
| 14 | Simon Willison：Claude Skills are awesome（2025-10-16） | https://simonwillison.net/2025/Oct/16/claude-skills/ | ★★ 权威个人博客 | 设计哲学评价 |
| 15 | Simon Willison：Agent Skills 开放标准短评（2025-12-19） | https://simonwillison.net/tags/anthropic | ★★ 权威个人博客 | 规范 under-specified 批评 |
| 16 | Superpowers 解剖（Akash Tandon 交互式解读） | https://www.akashtandon.in/interactive-explainers/superpowers | ★★ 个人深度分析 | 漏洞封堵写法对比、说服原则映射、Meincke et al. 2025 数据 |
| 17 | superpowers 心理机制解读（DEV Community） | https://dev.to/tumf/superpowers-the-technology-to-persuade-ai-agents-why-psychological-principles-change-code-quality-2d2f | ★ 二手转述 | 旁证：遵从率 33%→72% |
| 18 | nuwa-skill 归档笔记 + 头条报道 | https://github.com/ImChong/Robotics_Notebooks（sources/repos/nuwa-skill.md）；https://www.toutiao.com/article/7656802011605680683 | ★ 二手 | 中文圈案例、保真度验收设计 |
| 19 | 星数数据 | shields.io GitHub stars API（img.shields.io/github/stars/*.json） | ★★★ 实时 API，2026-10-15 查询 | 所有星数 |
| 20 | zendot.org 对 ComposioHQ 清单的评介 | https://www.zendot.org/en/posts/composiohq-awesome-claude-skills | ★ 二手 | 清单规模与渐进式披露解读旁证 |

**未采用**：知乎、微信公众号、百度百科、CSDN（按黑名单）；besthub.dev、crazycoderslab 等聚合站仅作线索，事实均回溯一手来源核实。

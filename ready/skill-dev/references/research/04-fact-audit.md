# 04 · skill-dev / SKILL.md 独立事实审计

> 审计日期：2026-10-15 ｜ 审计人：general-purpose-1（非作者，独立核对）
> 审计对象：`C:\Users\cqs6017\.workbuddy\skills\skill-dev\SKILL.md`（215 行）
> 审计方法：① 读同目录调研文件 01/02/03；② WebFetch 现查一手源（agentskills.io 规范全文、Snyk 原始报告、GitHub issue #14836、mattpocock/skills#693）；③ 读本机平台校验器 `skill-creator/scripts/quick_validate.py`；④ 对被审文件自身做机器校验。
>
> 判定图例：✅ 有据（注明证据）｜⚠️ 证据较弱或归类/措辞需修正｜❌ 无据、数字有误或归类错误
> 效力分级沿用 01 的定义：【规范】开放标准硬性要求｜【建议】官方推荐不强制｜【实现】特定客户端行为｜【社区】社区做法

---

## 零、结论速览

| 类别 | 结果 |
|---|---|
| **硬数字错误** | **0 处**。SKILL.md 出现的全部数字（64 / 1024 / 500 / 5000 / 200 / 500 / 50 / 100 / 1% / 3,984 / 13.4% / 10–20 / 5-5 / 0-5 / 3 / 九类 / 2026-02 / 2026-10-15）均与一手证据逐字吻合 |
| **效力归类错误** | **3 处**（保留字、第三人称、尖括号被写成「规范硬约束」） |
| **来源未标注** | 4 处（词预算、50 行、1% 预算、100 行 TOC 的官方内部分歧） |
| **措辞需收紧** | 2 处（symlink、动词优先） |
| **悬空引用 / 自洽性** | 无问题，被审文件自身全部合规 |

---

## 一、frontmatter 断言逐条核对（SKILL.md §3.1，表头自称「规范硬约束，写错装不上」）

### 1.1 `name` 字段

| # | SKILL.md 断言 | 判定 | 证据 |
|---|---|---|---|
| A1 | 1–64 字符 | ✅ | agentskills.io/specification 原文「Must be 1-64 characters」；01:49 同 |
| A2 | 仅小写字母、数字、连字符 | ✅ | 规范原文「May only contain unicode lowercase alphanumeric characters (`a-z`, `0-9`) and hyphens (`-`)」；本机 `quick_validate.py:43` 亦强制（`^[a-z0-9-]+$`） |
| A3 | 不首尾连字符、无 `--` | ✅ | 规范原文两条；本机 `quick_validate.py:45-46` 同步强制 |
| A4 | **必须与目录名一致** | ✅（规范层面）／⚠️（平台层面） | 规范原文「Must match the parent directory name」确为硬性。**但本机校验器不查此项**——`quick_validate.py` 全文只校验字符集+首尾连字符+`--`，不比对目录名。规范强制 ≠ 本机装不上，表头「写错装不上」对本平台有夸大 |
| A5 | **不含 `claude` / `anthropic`** | ❌ **归类错误** | **agentskills.io 规范全文无任何保留字条款**（已逐节现查确认）。此条出自平台上传校验：01:131 标为【实现·上传校验强制】，实证为 anthropics/skills PR #1605（官方被迫把 `claude-academy-guide` 改名 `academy-guide`）。**事实存在，但不是规范硬约束，不应与 A1–A4 同列** |
| A6 | 动词优先 | ⚠️ 措辞与官方不一致 | 官方 best-practices 的措辞是**动名词（gerund）优先**（"Processing PDFs"），并明确要求避免 Helper/Utils/Tools（01:196）。「动词优先主动语态」出自 superpowers（02:143，【社区】）。两者实践接近，但 SKILL.md 未标来源，且漏了官方的「避免 Helper/Utils」排除项 |

### 1.2 `description` 字段

| # | SKILL.md 断言 | 判定 | 证据 |
|---|---|---|---|
| A7 | 1–1024 字符 | ✅ | 规范原文「Must be 1-1024 characters」；01:122 补充实证（PR #1605 把 1176 字符砍到 992） |
| A8 | **第三人称** | ❌ **归类错误** | 规范无此要求。出自平台 best-practices（01:197 🅱）「Always write in third person」，理由是它会被注入系统提示、视角不一致干扰发现——属【建议/实现】，非【规范】。放在「规范硬约束，写错装不上」表下明显过强 |
| A9 | **无尖括号 `<` `>`** | ⚠️ 事实成立但归类过强 | 规范全文无此条，来源是官方 PDF 指南（01:132 🅱【实现·上传校验】）。**但有本机强制证据**：`quick_validate.py:53-54` 对 description 含 `<`/`>` 直接 return False。应标为「平台强制」而非「规范硬约束」 |
| A10 | 只写触发条件+症状同义词+排除项 | ✅ | 02:137 superpowers SDO 一手；03:110 官方修复路径（正例补意图词、负例加「NOT for X — use Y instead」） |
| A11 | 四个可选字段；跨平台分发时只保留这四个 | ✅ | 规范字段表仅 6 字段（name/description/license/compatibility/metadata/allowed-tools）；01:231「跨平台上传只能用规范 6 字段，否则 `Unexpected key(s)`」 |

---

## 二、正文与引用断言（SKILL.md §3.2–3.3）

| # | SKILL.md 断言 | 判定 | 证据 |
|---|---|---|---|
| B1 | 正文 <500 行 | ✅ | 规范原文「Keep your main `SKILL.md` under 500 lines」。**注意：位于 Progressive disclosure 段落，是【建议】不是【规范】**——SKILL.md §3.2 用祈使句陈述未标效力，可接受 |
| B2 | 正文 <5000 token | ✅ | 规范原文「Instructions (< 5000 tokens recommended)」，明确带 "recommended" |
| B3 | 频繁加载型 <200 词、普通型 <500 词 | ⚠️ 来源未标注 | 数字与 02:141 完全一致（superpowers：「常加载 skill 总共 <200 词；其他 <500 词」），**但这是【社区】来源，不是官方**，且单位是「词」与官方的「行/token」不同。SKILL.md 把它与 B1/B2 并列在同一条 bullet 里，读者会误以为同为官方口径 |
| B4 | 开头 50 行放最关键约束；压缩后只保留开头 | ⚠️ 半官方 | 「会话压缩后只保留开头、关键指令必须置顶」有官方依据（03 FM-07，code.claude.com ★★★）；**「50 行」这个具体数字来自社区 skill-load-tips**（03:178 ★★） |
| B5 | 引用一层深 | ✅ | 规范原文「Keep file references one level deep from `SKILL.md`. Avoid deeply nested reference chains.」 |
| B6 | >100 行的 reference 加目录 | ⚠️ 官方内部数字打架 | 平台 best-practices 写 >100 行（03:177 ★★★），而官方 skill-creator 原文写 >300 行（01:130 已自曝「两处数字不一致，从严取 100」；02:231 与 02:337 骨架也写 300）。SKILL.md 取 100 与 03 一致，**但 01/02/03 三份调研文件内部 100/300 并存**，交付前应统一并注明分歧，否则读者按 02 骨架施工会撞车 |
| B7 | 深层链会被 `head -100` 截断 | ✅ | 03:177 官方 best-practices 原文（★★★） |
| B8 | 脚本须经解释器调用，绝不裸路径 | ✅ | 02:144 superpowers 一手（打包器剥可执行位 → Permission denied） |
| B9 | 路径一律正斜杠、无 symlink | ✅ | 01:133【建议】+ 03 FM-05/FM-09（★★★） |

---

## 三、平台机制与实证断言

| # | SKILL.md 断言 | 判定 | 证据 |
|---|---|---|---|
| C1 | skill 清单预算约默认上下文 1%，超了从最不常用的开始**静默丢弃** | ✅ 数字对／⚠️ 未标平台限定 | 03 FM-01（★★★ 官方 `skillListingBudgetFraction` 文档 + issue #13044「92 个 skill 只显示 36 个」+ alexey-pelykh 实测约 15,500–16,000 字符 + ruflo#1834「378 descriptions dropped」）。**这是 Claude Code【实现】层行为，不是开放规范**，SKILL.md 在 §3.1 的规范语境下陈述，读者会误认为通用规律 |
| C2 | Snyk 扫描 3,984 个 skill、13.4% 含 critical 缺陷（2026-02） | ✅ **现查完全一致** | WebFetch snyk.io/blog/toxicskills 原文：「scanning 3,984 skills from ClawHub and skills.sh as of February 5th, 2026」；「13.4% of all skills (534 of 3,984) contain critical-level security issues」；另有 36.82%（1,467）含任意级别缺陷、76 个确认恶意 payload。SKILL.md 引用的 3,984 / 13.4% / 2026-02 三项全部正确 |
| C3 | description 总结工作流 → agent 跳过正文（code review 只做一次 vs 正文要求两次） | ✅ | 02:134 superpowers writing-skills 一手原文。⚠️ 单一来源、作者自述、无公开可复现实验数据——SKILL.md 用了「实证」字样，建议改为「据 superpowers 实测」 |
| C4 | 禁令用在输出塑形问题上，实测比无指导更差 | ✅ | 02:109 superpowers 一手（「实测比无指导还差」）。⚠️ 同 C3：单一来源、无公开数据集 |
| C5 | symlink 安装的 skill 不被发现 | ✅ 事实成立／⚠️ 措辞略强 | **现查 issue #14836 原文**：`/skills` 报 "No skills found"，`find -L` 能找到、`find` 找不到；03 引述「16 个 symlink skill 的用户确认 cp -r 立刻修复」。**但 issue 原文明确说该 skill「is correctly loaded and usable by the model」**——模型仍能用，只是清单扫不到。SKILL.md 反模式 #11 写「不被发现」过于绝对，建议改为「不被清单发现（/skills 里看不见）」 |
| C6 | `paths:` 让 skill 完全不可发现 | ✅ | 03 FM-04（issue #49835，v2.1.145 A/B 对照：有 paths 的缺席、无 paths 的在场）。⚠️ 未能现查（第三方镜像 claudeissues.com），依赖 03 转述（★★★） |
| C7 | `disable-model-invocation` 在某些端整体消失 | ✅ **现查完全吻合** | mattpocock/skills#693 原文：「I confirmed the partition across 63 installed skills: all 35 without the flag were listed, all 28 with it were absent. No exceptions either way.」，与 03 FM-03 数字逐字一致；上游 anthropics/claude-code#82237。**补充时效信息**：该 issue 已于 2026-10-06 以 not planned 关闭（归 harness 问题未修）；2026-08 有报告称 CLI 2.1.247 亦复现（25 个中 14 个缺席）。SKILL.md 说「某些端」是准确的，可收紧为「桌面/Web 端 coordinator mode + 部分 CLI 版本」 |
| C8 | 「读文件 + 联网」是经典外泄链，须单独评审 | ✅ | 03:54 Anthropic 企业版审查清单第 6 步原文（★★★） |
| C9 | skill 与 agent 之间没有沙箱，恶意 skill 继承全部权限 | ✅ | 03:13（★★）；与 03:16 论文（skill 能声明工具类型但不能限制工具目标）互证 |
| C10 | 九类危险模式 | ✅ 计数吻合 | 03 §5.1 A 清单恰为九项：硬编码秘密 / 外泄(curl\|bash) / 编码执行 / 注入句式 / 环境变量 / 网络访问 / 路径越界 / 高危命令 / 合规话术+隐藏字符。SKILL.md 列的九类与之逐项对应 |
| C11 | 触发测试 10–20 条（5–10 正 + 5–10 负）、near-miss 优先、5/5 与 0/5、跑两轮一致 | ✅ | 03 §2.2（★★）；官方 skill-creator 口径为 20 条 8-10/8-10 + 每条跑 3 次（01:190），两者属同类做法的不同取值，非矛盾 |
| C12 | 执行稳 ≥3 真实任务、with/without 成对、pass@k 与 pass^k 分开、断言后写 | ✅ | 03 §2.1–2.2（★★★/★★） |
| C13 | `_skillhub_meta.json` 为安装产物，分发时排除 | ✅ | 03:242–247，本机一手文件 `C:/Users/cqs6017/.workbuddy/skills/experience-loop/_skillhub_meta.json` |

---

## 四、星数核对（任务指定项）

**结论：SKILL.md 主体未引用任何仓库星数。** 对 SKILL.md 全文执行 `grep '[0-9]{2,3}k|stars|星'` → 0 命中。02-community-works.md 的星数（superpowers 299k、anthropics/skills 181k 等）**未被 SKILL.md 引用，故不在本次核对范围**，也无需修正。（附注：02 自称星数经 shields.io 实时 API 查询，本次未复验，因其未进入交付物。）

---

## 五、自洽性与悬空引用检查

| 检查项 | 结果 |
|---|---|
| SKILL.md 引用的 `references/skill-templates.md` | ✅ 存在 |
| `references/checklists.md`（清单 A/B/C/D） | ✅ 存在 |
| `scripts/skill_check.py`（结构+内容+安全，支持 `audit:ignore`） | ✅ 存在，源码确认支持 `<!-- audit:ignore RULE_ID 原因 -->` 行内豁免（skill_check.py:12-14、75） |
| `assets/starter-skill/SKILL.md` | ✅ 存在 |
| `references/research/01|02|03` | ✅ 均存在 |
| `references/templates/` | ⚠️ 空目录，SKILL.md 未引用，无影响 |
| 自身 name 与目录名一致 | ✅ `name: skill-dev` = 目录 `skill-dev` |
| 自身 description 长度 | ✅ 172 字符（≤1024） |
| 自身 description 含尖括号 | ✅ 无 |
| 自身正文行数 | ✅ 214 行（<500） |
| 档位表 / 阶段编号 / 反模式 14 条内部一致性 | ✅ 无自相矛盾 |

---

## 六、必须修正清单（按严重度排序）

| 序 | 位置 | 问题 | 建议修法 |
|---|---|---|---|
| 1 | §3.1 name 行 | ❌ 把「不含 `claude`/`anthropic`」写成规范硬约束；规范全文无此条 | 移出该行，改为独立注：「平台上传校验会拒（claude.ai/Skills API），实证见 PR #1605；本地安装不受限」 |
| 2 | §3.1 description 行 | ❌ 把「第三人称」写成规范硬约束；实为平台 best-practices【建议】 | 降格为建议，或在该表头把「规范硬约束」改为「规范硬约束 + 平台强制项」并逐条标效力 |
| 3 | §3.1 description 行 | ⚠️ 「禁尖括号」归属规范；实为【实现】层（官方 PDF + 本机 quick_validate 强制） | 保留断言（本机确实会卡），但标注「平台强制，非规范」 |
| 4 | §3.1 name 行 | ⚠️ 「必须与目录名一致…写错装不上」对本平台夸大 | 补注：本机 `quick_validate.py` 不校验目录名一致性，需人工或用 skill_check.py 兜 |
| 5 | §3.1 末段 | ⚠️ 「清单预算 1%、静默丢弃」未标平台限定 | 补「（Claude Code 实现层，`skillListingBudgetFraction`）」 |
| 6 | §3.2 首条 | ⚠️ `<200 词 / <500 词` 与官方 `<500 行 / <5000 token` 并列，来源与单位混排 | 拆成两条，标明前者出自 superpowers（社区）、后者出自规范 |
| 7 | §3.2 / §3.3 | ⚠️ 「50 行」「>100 行」具体数字来自社区/单一来源；官方另有 300 行说法 | 补来源标注；统一 01/02/03 中 100 vs 300 的分歧并在 SKILL.md 写明取舍理由 |
| 8 | 反模式 #11 | ⚠️ symlink「不被发现」过强；issue 原文称模型仍可加载使用 | 改为「不被清单发现（/skills 看不见）」 |
| 9 | §3.1 name 行 | ⚠️ 「动词优先」与官方「动名词优先」措辞不一，且漏官方排除项 | 改为「动名词/动词优先（如 `processing-pdfs`），避免 helper/utils/tools」 |
| 10 | 铁律 3 / 反模式 #6 | ⚠️ 两处「实证」均依赖 superpowers 单一自述，无公开数据集 | 加「据 superpowers 实测」限定语，避免读者当成可复现实验 |

**无需修正**：所有数字本身均正确；Snyk 数据经现查逐字吻合；引用文件无悬空；被审文件自身完全合规。

---

## 七、本次审计使用的一手来源

| 来源 | URL / 路径 | 用途 |
|---|---|---|
| Agent Skills 开放规范全文（现查） | https://agentskills.io/specification | 校验 A1–A5、A7、B1、B2、B5、A11 |
| Snyk ToxicSkills 报告（现查） | https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/ | 校验 C2（3,984 / 13.4% / 2026-02） |
| anthropics/claude-code#14836（现查） | https://github.com/anthropics/claude-code/issues/14836 | 校验 C5（symlink） |
| mattpocock/skills#693（现查） | https://github.com/mattpocock/skills/issues/693 | 校验 C7（63 个 skill / 35 vs 28） |
| WorkBuddy 内置校验器 | `D:\AI\workbuddy\resources\app.asar.unpacked\resources\plugins\workbuddy-builtin\skills\skill-creator\scripts\quick_validate.py` | 平台实际强制项实测（A2/A3/A9） |
| 调研文件 01 / 02 / 03 | 同目录 `references/research/` | 其余条目的证据基座 |
| 平台 best-practices | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices | **未能现查（区域受限，重定向至 app-unavailable-in-region）**，A6/A8/B6 依赖 01/03 转述 |

**审计边界声明**：platform.claude.com 因区域限制无法直连，A6（动名词）、A8（第三人称）、B6（>100 行）三条依赖 01/03 的 🅱/★★★ 转述，未获原文直证；其余全部条目均有一手直证。本次未使用知乎、微信公众号、百度百科、CSDN 任何内容。

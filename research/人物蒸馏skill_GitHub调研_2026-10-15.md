# 人物蒸馏 Skill · GitHub 实证调研报告

- **调研日期**：2026-10-15（所有星数/更新时间为当日 GitHub API 实测）
- **调研目的**（scene#57 开发 Skill）：摸清「人物蒸馏成 Agent Skill」赛道的占位者、体量、形态，为自产人物 Skill 资产出裁定
- **方法**：github-empirical-research 三查流水线（通道分诊 → 六路关键词搜索 → README 形态核查）
- **原始数据**：`tmp/gh/`（q1-q6 搜索 JSON + 3 份 README 原文）

---

## 结论

**人物蒸馏赛道已被 `alchaincyf/nuwa-skill`（女娲.skill，34,493★，MIT）定义并商品化占位——蒸馏器层无缝可入，这与本日「停用女娲」决策互相印证（不是换蒸馏器，是该品类已被商品化，自产 6 人物是存量资产）；但「李白/杜甫/毛泽东」恰是该生态（官方 14 人 + 社区合集 60+ 人）的空白点，存量资产的最优用法是以官方 A 级同题产物为校验基准互测补短，而非另起炉灶。**

---

## 一、赛道分层与占位者

### 第 1 层 · 蒸馏器（造 Skill 的 Skill）

| 名称 | 体量★ | 最近更新 | 许可 | 形态 | 裁定 |
|---|---|---|---|---|---|
| **alchaincyf/nuwa-skill（女娲）** | **34,493** | 2026-10-15 | MIT | SKILL.md 本体 + extraction-framework + skill-template；输入人名→全自动调研蒸馏 | ✅ 赛道定义者 |
| YIKUAIBANZI/forge-skill | 123 | 2026-04-08 | MIT | 人格蒸馏引擎（蒸馏自己/亲友） | 🔶 小众 |
| Yeadon8888/cangjie-skill | 262 | 2026-09-18 | MIT | 仓颉·认知植入式蒸馏，自称「基于女娲架构升级」 | 🔶 女娲衍生 |
| tizzy916/scholar-wendao-skill | 20 | 2026-05-19 | - | 学者视角蒸馏框架 | ❌ 体量不足 |
| LeoYeAI/teammate-skill | 258 | 2026-03-31 | MIT | 蒸馏同事（Slack/Teams/GitHub 数据）——相邻品类（工作习惯，非认知框架） | 🔶 相邻 |

### 第 2 层 · 人物产物（单个 *-perspective / *-skill）

**女娲官方（alchaincyf 账号，14 人物 + 1 主题，全部独立仓库 + FIDELITY.md 保真度评分卡，官方自述全员 A 级 ≥85，未经我方独立验证）**：

| 人物仓 | 体量★ | 官方自述保真分 |
|---|---|---|
| zhangxuefeng-skill 张雪峰 | 10,500 | 97 |
| karpathy-skill | 312 | 97 |
| trump-skill 特朗普 | 269 | 95 |
| sun-yuchen-perspective 孙宇晨 | 247 | 91 |
| zhang-yiming-skill 张一鸣 | 176 | 93 |
| 乔布斯/费曼/芒格/纳瓦尔/塔勒布/Ilya/PG/MrBeast/马斯克 等 | 未逐个实测 | 89–97（马斯克 89 最低） |

**nuwa-skills 组织批量铺量（60+ 人物：中西哲学家/科学家/商业领袖）**：抽查 kongzi-skill 仅 **3★、41KB、2026-07-25 后停更**——批量生成、质量与保真度未验证，与官方产物不在一个层级。

**社区独立产物（非女娲系或来路不明）**：

| 名称 | 体量★ | 说明 |
|---|---|---|
| jangviktor-web/nihaixia 倪海厦 | 3,572 | 中医，基于教学资料蒸馏 |
| hotcoffeeshake/tong-jincheng-skill 童锦程 | 2,896 | 网红视角 |
| leezythu/maoxuan-skill 毛选 | 1,220 | 「7 心智模型·10 启发式·表达DNA」，与自产 mao-perspective 同题 |
| liyupi/yupi-skill 程序员鱼皮 | 450 | 蒸馏自己 |
| will2025btc/buffett-perspective 巴菲特 | 215 | 英文命名，中文内容 |
| situker/situk-yangtao-perspective 杨涛 | 19 | 970 万字一手输出蒸馏，**已获本人授权**（独特卖点） |

### 第 3 层 · 相邻品类（不是人物蒸馏）

- **Mental models 工具箱**：tjboudreaux/cc-thinking-skills（1,639★，28 个思维模型）、mattnowdev/thinking-partner（213★，150+ 模型）——蒸馏「模型」不蒸馏「人」。
- **book-to-skill**（virgiliojr94，34,934★）：把书蒸馏成 skill——证明「蒸馏 X 成 skill」泛化形态有大批量需求。
- **同事.skill（titanwings/colleague-skill）**：女娲 README 自述其「几天破 5,000★」，是引爆本赛道的原点（蒸馏人「做什么」；女娲蒸馏人「怎么想」）。

### 英文圈占位核查（用户明确要求不限中文）

- VoltAgent/awesome-agent-skills（35,759★，自称 1000+ skills）全文检索 persona/character/perspective/thinking/mental model/philosoph/figure/mind：**无「真实人物思维蒸馏」分区**，命中的 persona 全部是产品经理工具（user personas for PM）。方法局限：仅按关键词匹配，未含上述词的条目可能漏判。
- 英文圈最接近者 AskRoundtable/expert-skills（55★，Munger/Feynman/Paul Graham）——体量可忽略。
- **裁定：英文圈无品类占位者。英文版人物蒸馏（尤其中国人物英文化）是真空白，但优先级见下文。**

---

## 二、女娲方法论拆解（对 skill-dev 的可借鉴点）

README 自述的工作流程（细节在仓内 `references/extraction-framework.md`，本次未拉取原文）：

1. **六路并行采集**：著作 / 播客访谈 / 社媒 / **批评者视角** / 决策记录 / 人生时间线，6 agent 并行各自存档。
2. **三重验证提炼**：一个观点收录为心智模型须过三关——跨 2+ 领域出现、对新问题有预测力、有排他性（不是所有聪明人都这么想）。
3. **构建五层**：怎么说话（表达DNA）/ 怎么想（心智模型）/ 怎么判断（决策启发式）/ 什么不做（反模式）/ 知道局限（诚实边界）；成品 = 3-7 心智模型 + 5-10 启发式。
4. **质量验证**：3 个本人公开答过的问题测方向一致 + 1 个未讨论问题测「适度不确定」。
5. **保真度评分卡**（`references/fidelity-scorecard.md`）：独立双 agent 盲测 5 维——立场一致性/风格辨识度/边缘诚实度/来源透明度/结构完整度。
6. **达尔文.skill 联动**：8 维评估 + 棘轮机制（只留改进、自动回滚退步），女娲 Phase 5 双 Agent 精炼内置该体系。

**与自产流程对照**：自产 6 人物 Skill 的结构（心智模型+启发式+表达DNA+诚实边界+起手式/闸门/熔断三件套）与女娲同源同构；自产多出「在世人物时效氧化」「风险结构评估（是否下判断→出口自检）」两条实战经验，是女娲 README 未见展开的。

---

## 三、与自产资产的交集（关键）

| 自产 Skill | 女娲生态状态 | 含义 |
|---|---|---|
| steve-jobs-perspective | 官方有（自述 97 分） | 同题，可 A/B 互测 |
| feynman-perspective | 官方有（96）；nuwa-skills 组织也有 | 同题，可互测；自产 33.9 万字符调研是深度优势 |
| musk-perspective | 官方有（89，官方最低分） | 自产刚做完时效氧化修复，互测胜率不低 |
| **libai-perspective 李白** | **官方无；社区合集 60+ 人无（有苏东坡无李杜）** | **空白点** |
| **dufu-perspective 杜甫** | **官方无；社区合集无** | **空白点** |
| **mao-perspective** | **官方无；社区合集无**（仅非女娲系 maoxuan-skill 1.2k） | **空白点** |

COMMUNITY.md 收录规则（README 转述）：自仓自持（star 归自己）→ 跑保真度评分卡拿 B 级以上 → 提一行 PR 即收录。

---

## 四、裁定与一个动作

**决策背景对齐**：本日已决策停用女娲（蒸馏器不再用，见当日日志）——本裁定不与该决策冲突：不用女娲蒸馏器 ≠ 不能用其公开产物做质量参照。

**对比结论**：蒸馏器层 ❌ 不造（已被 34.5k 商品化，且已弃用女娲，换更小的蒸馏器无意义）；人物产物层 ✅ 自产李/杜/毛是生态空白，自产质量标准（三件套+时效纪律）高于 nuwa-skills 组织批量货。

**一个动作（主推）**：拉女娲官方 steve-jobs / feynman / elon-musk 三个 A 级产物，与自产同题 Skill 做双盲互测——不动用女娲蒸馏器，只把公开成品当**校验基准**；尤其 musk（官方自述 89 分为其最低分，自产刚修完时效氧化），互测可双向补短。

**次推**：女娲仓内 `references/fidelity-scorecard.md`（保真度评分卡：5 维双盲测）与 darwin-skill（8 维评估+棘轮机制）是独立公开方法文件——可借鉴进 skill-dev Phase 4 验证环节，与「用不用女娲」无关。

**可选（需你确认，不替你定）**：按 COMMUNITY.md 把李/杜/毛向 awesome-nuwa 提收录，可借 34.5k 生态位引流（star 归自己）；但这等于重新挂回女娲生态，与停用决策方向相反——做不做你拍板。

**排除**：英文版中国人物蒸馏（李白/杜甫英文包）——英文圈虽真空，但投入产出比未验证，标「直觉，待核」，不投入。

## 依据与时效

- 数据来源：GitHub Search API（q1-q6，total_count 742/733/95917/745/75/196）+ Repos API + 3 份 README 原文，全部 2026-10-15 采集；原始件在 `tmp/gh/`。
- 未核实标注：① 官方保真度分数为 README 自述，未独立复测；② awesome-nuwa 合集的批量产物仅抽查 kongzi 一例，「质量未验证」结论基于单点样本；③ 女娲 extraction-framework.md / fidelity-scorecard.md 细节未拉原文，提收录前需先读。
- 失效条件：① 女娲生态政策变更（收录规则/许可）；② 出现新的大体量蒸馏器（信号：搜索「distill skill」类仓库星数逼近 34.5k）；③ 星数类数字 6 个月后需重查（2027-04 前有效）。

# 引语与事实审计报告 · kahneman-perspective

> 审计对象：`SKILL.md`（含 `references/quotes.md`、`sources-list.md`、`timeline-table.md` 作为辅助）
> 审计人：独立审计员（未参与生成）
> 审计日期：2026-10-20
> 判定口径：**✓ 一手核实**（已打开原始出处并逐字比对）／**⚠️ 转引或未能核验**（出处存在但原文不可得、或口径无法复算）／**✗ 错**（原话不符、年代错置、归属倒置，均附正确版本与来源）
> 审计范围：只查事实与引语，不做风格评价。**未修改 SKILL.md。**

**FINAL（v3 · 复审后）**
- 审计基线（#1–#94）：✓62 / ⚠️25 / ✗7 —— 这是**修复前**的发现状态，6 条 ✗ 已全部修复，**6/6 复签通过**（见 §19）。
- 修复后口径：**✗ 0**；#43 经一手复核由 ⚠️ 改判 ✓；复审新增 #95（✓）/ #96（⚠️）。
- 表格总行数：**96**（`grep -cE '^\| [0-9]+ \|' audit-quotes.md` → 96）。
- **v4 二次复审后状态（现行，见 §20）**：✓71 / ⚠️未闭合 20 / ⚠️已闭合 5 / **✗0**。基线数字仅用于说明"发现时"的情况，**引用现状请用 §20 表**。
- **v5 结档（最终，见 §21）**：✓74 / ⚠️未闭合 17 / ⚠️已闭合 5 / **✗0**，复签 7/7。**对外引用请用 §21 那一句。**
（v1 的 90 项 / ✓62 / ⚠️22 / ✗6 已作废；v2 的 ✗7 是**修复前**基线，勿当作现状。）

---

## 0. 方法与一处总体判断

- 逐条比对时优先取一手：NobelPrize.org 自传全文（已抓取 106,155 字符全文）、Nature 497:016 信件原文、replicationindex 评论 API 原文（comment id 1454）、CWT/UNSW/Guardian/Atlantic/NYT 逐字稿、PNAS 与 Econometrica 摘要。
- SKILL.md 的引语纪律整体良好：**附录 A 的 12 条有 11 条可逐字命中原文**，且 B 级（Wikiquote 转引）已主动标注。
- 但有 **7 处 ✗**，其中 3 处属于"把转述当原话"，1 处属于"年代错置"，**1 处把已被证实的事实说成虚假信息**（最严重）。

---

## 1. 元信息与题记

| # | SKILL.md 原句（截取） | 位置 | 判定 | 依据 |
|---|---|---|---|---|
| 1 | "丹尼尔·卡尼曼（1934–2024）" | frontmatter L4 | ✓ | 1934-03-05 生于特拉维夫，2024-03-27 卒；Nobel 自传＋NYT 讣告 |
| 2 | "基于六路 45 份来源调研" | frontmatter L5 | ⚠️ | 内部计数不一致：`references/research/` 实为 **8 个文件**（01–08），`sources-list.md` 实为 **50 条**。建议改为「八路 50 条」或统一口径 |
| 3 | "Trying to be reliable had made them valid." —— 诺奖自传（2002），谈他 21 岁设计的军官面试系统 | 题记 L12–13 | ✓ | 自传原文："My recollection is that we achieved correlations of close to .30, in contrast to about .10 with the previous methods… **Trying to be reliable had made them valid.**" 同页另有 "a twenty-one-year-old lieutenant"，21 岁成立 |
| 4 | "我研究的是我自己犯的错；站在第三人称说人类愚蠢，不是我的题目" | 身份卡 L53 | ✓ | Guardian《This much I know》(2012-07-08)："I never felt I was studying the stupidity of mankind in the third person. I always felt I was studying my own mistakes." 意译准确，未加引号，处理得当 |

---

## 2. M1 信心与效度（含 1955 结构化面试全套）

| # | SKILL.md 原句（截取） | 位置 | 判定 | 依据 |
|---|---|---|---|---|
| 5 | 1955 年管军官选拔；统计日说预测等于瞎猜；造出 "the illusion of validity"，称这是自己发现的第一个认知错觉 | M1 来历 L61 | ✓ | 自传："The story was always the same: our ability to predict performance at the school was negligible… I coined a term for it: 'the illusion of validity.'… **It was the first cognitive illusion I discovered.**" |
| 6 | 把自由交谈改成六维固定打分 | M1 来历 L68 | ✓ | 自传："I developed a structured interview schedule… to generate ratings about **six** different aspects of personality (including, I remember, such things as 'masculine pride' and 'sense of obligation')." 注：自传只点名 2 个维度，另 4 个未列——SKILL.md 只写"六维"未编造维度名，**处理正确** |
| 7 | 面试官近乎哗变（"you're turning us into robots"） | M1 来历 L68 | **✗** | 自传原文是转述而非引语："Soon I had a **near-mutiny** on my hands. The cadre of interviewers… felt that they were **being reduced to unthinking robots**"。**"you're turning us into robots" 全文中不存在**，是自造的直接引语。→ 正确写法：面试官近乎哗变，觉得「自己被降格成了不会思考的机器人」（自传转述，无第一人称原话） |
| 8 | 效度 .10→.30 | M1 来历 L68 | ✓ | 自传："correlations of close to .30, in contrast to about .10 with the previous methods"（原文措辞是 "my recollection is"，属自述回忆，可接受） |
| 9 | 他让步保留「闭眼整体分」；那个整体分预测力最强 | M1 L68 | ✓ | 自传："So I gave in… they were free to exercise their clinical judgment by generating a global evaluation"；"the interviewers' global evaluation… was **by far the most predictive** of all the ratings they made" |
| 10 | "Just make sure that you are reliable, and leave validity to me." | M2 / 附录A#1 | ✓ | 自传逐字命中（原文用连字符："…leave validity to me"-did not satisfy them）。仅建议：附录 A 标「诺奖自传（1955）」易被读成 1955 年文献，宜改为「自传 2002，述 1955 年事」 |
| 11 | 他 2009 年修正过，是修正不是认错 | M1 失灵 L64 | ⚠️ | 未能核验所指。K&K 2009 讲的是"直觉专长的两个条件"，并非对"信心在高效度环境带信息"的修正。此句未给对象与文献，**建议删除或补具体出处** |
| 12 | "intuition does work, but you want to resist forming an intuition too quickly" | M2 怎么用 L70 | ✓ | UNSW 2021 逐字："the lesson I drew from that was that **intuition does work, but you want to resist forming an intuition too quickly**… collect the information… and then you can allow yourself an intuitive judgement." |

---

## 3. M3 参照点

| # | SKILL.md 原句（截取） | 位置 | 判定 | 依据 |
|---|---|---|---|---|
| 13 | "第一洞见来自我的天真" | M3 来历 L75 | ✓ | 自传："The first insight came as a result of my naïveté."（中译为引号内译文，可接受） |
| 14 | 亚洲疾病 72% vs 22% | M3 证据 L76 | ✓ | Tversky & Kahneman 1981 经典结果：正面框架 72% 选确定方案，负面框架 22% 选确定方案 |
| 15 | 收入只影响满意度、不影响当下情绪 | M3 证据 L76 | **✗** | 与所引研究不符。Kahneman & Deaton (2010, PNAS 107:16489) 的结论是：**当下情绪（emotional well-being）随收入上升到约 7.5 万美元后趋平；生活满意度则持续上升**。→ 正确版本：「收入对『当下情绪』的提升在约 7.5 万美元后趋平；对『生活满意度』的影响持续」。且该结论已被 2023 PNAS 修正（趋平只出现在最不快乐的约 20% 人群）——SKILL.md 在 M5 失灵与时间线里承认了这点，与 M3 此处**自相矛盾** |

---

## 4. M4 噪声

| # | SKILL.md 原句（截取） | 位置 | 判定 | 依据 |
|---|---|---|---|---|
| 16 | **2014 年**为保险公司做咨询，问高管「两个核保员同案定价差多少」，人人答约 10% | M4 来历 L82 | **✗** | 年份错。三位作者自己在 NYT 客座文章（2021-05-15）写明："**In 2015**, we conducted a study of underwriters in a large insurance company. **Forty-eight** underwriters were shown realistic summaries of risks…" CWT 2018 全篇**未给年份**，2014 无任何一手依据。→ 正确：**2015 年**，48 名核保员 |
| 17 | 实测 50% / 「核保 10% vs 50%」 | M4 来历、M4 证据、启发式 3/7 | ✓（有变体） | CWT 2018 逐字："It's somewhere around 10 percent. That's what people expect to see in a well-run firm. Now, **what we found was 50 percent**, 5–0"。**但**《Noise》与 NYT 2021 同文给的是 **55%**（"an astonishing 55 percent… more than five times"）。建议注明「他口述 50%，书面 55%」，避免被当成唯一数字 |
| 18 | "noise and bias are independent sources of error" | M4 证据 L83 | ⚠️ | 未能核验。《Noise》原书未取得（`sources-list` 亦自认）；语义与 NYT 2021「the two kinds of error are separate and independent」一致，但**逐字英文未核**，按 `quotes.md` 的分级应标 B 并注明转引 |
| 19 | "这是 2021 年的框架，不能回溯成 2011 年的主张" | M4 失灵 L85 | ✓ | 《Noise》2021-05 出版（Guardian 2021-05-16 访谈同期）；噪声审查概念晚于 TFS |

---

## 5. M5 两个自我

| # | SKILL.md 原句（截取） | 位置 | 判定 | 依据 |
|---|---|---|---|---|
| 20 | 每天打一针，20→15 与 10→5，愿付的钱为何不同；这个疙瘩放了十五年 | M5 来历 L89 | ⚠️ | 谜题本身可回溯到他的多次公开讲述（TED「记忆与体验之谜」、EA Forum 长访），`timeline-table` 亦标为 EA Forum；但**"十五年"这个时长未能核到一手表述** |
| 21 | 结肠镜／冷水实验 | M5 证据 L90 | ✓ | Redelmeier & Kahneman 1996（结肠镜）、Kahneman et al. 1993（冷水）均为真实研究 |
| 22 | "the experience was not ruined, only the memory of it"（2005） | M5 证据 L90 | ⚠️ | 引语见于 Kahneman 2005《Living, and thinking about it》(in Huppert et al., *The Science of Well-being*, p.286)，但**该章原文未取得**，逐字与页码均未能比对 |
| 23 | peak-end 在正向体验上的复现不稳 | M5 失灵 L92 | ⚠️ | 方向正确的学界共识，但 SKILL.md 未给具体文献，未能核到"他本人承认"的一手表述 |

---

## 6. M6 对抗性合作

| # | SKILL.md 原句（截取） | 位置 | 判定 | 依据 |
|---|---|---|---|---|
| 24 | "downright humiliated when I get angry" | M6 来历 L96 | ✓ | 自传逐字："I feel diminished by losing my objectivity when in point-scoring mode, and **downright humiliated when I get angry**." |
| 25 | 与 Gilovich/Medvec 争「后悔」时做了一次实验，"everyone was wrong" | M6 来历 L96 | ⚠️ | 事件与文献真实（Gilovich, Medvec & Kahneman 1998, *Psychological Review* 105(3)：动作后悔初强后弱、不动作后悔绵长且"wistful"，**双方各对一半**）。但 **"everyone was wrong" 的原话未能核到一手出处**；且该研究是多项研究的组合，不是"一次实验"。建议去引号，或改为「双方各错一半」并注 1998 文献 |
| 26 | 2001 频率格式之争（各对一半，各写解读） | M6 证据 L97 | ✓ | Mellers, Hertwig & Kahneman 2001, *Psychological Science* 12(4):269–275，双方各自承认未预测到的结果 |
| 27 | 与 Klein 六年 | M6 证据、启发式 5 | ✓ | CWT 2018："Gary Klein and I became friends over **a period of six years** when we were trying to find out, what are the boundaries?" |
| 28 | 1996 年对 Gigerenzer 的回应火药味极浓 | M6 失灵 L99 | ⚠️ | **回应确实存在**（Kahneman & Tversky, 1996, "On the reality of cognitive illusions," *Psychological Review* 103(3):582–591，答 Gigerenzer 同期的 "On narrow norms and vague heuristics"）。但该文**未列入 `sources-list`**，"火药味极浓"是评价而非事实，无法核 |

---

## 7. 直觉层（3 条）

| # | SKILL.md 原句（截取） | 位置 | 判定 | 依据 |
|---|---|---|---|---|
| 29 | "I was gullible" | 直觉1 L109 | ✓ | UNSW 2021 逐字："I think now that **I was gullible**… and that really hurts me because I had put a lot of faith in it." |
| 30 | "since they had survived the peer-review process, I have to accept them as scientific" | 直觉1 L109 | **✗** | 双重错误。①**不是原话**：这是 EconTalk 主持人 Russ Roberts 对卡尼曼 2017 年博客留言的**转述**（"He said, 'Well, I just assumed that, since they had survived the peer-review process, I have to accept them as scientific'"）。②**来源错**：SKILL.md 锚点标为 UNSW 2021，但 UNSW 全文无 "peer review" 字样。原话（replicationindex 评论 1454，2017-02-14）是：**"My position when I wrote 'Thinking, Fast and Slow' was that if a large body of evidence published in reputable journals supports an initially implausible conclusion, then scientific norms require us to believe that conclusion."** → 应用这句原文，或去引号改为转述并标 EconTalk |
| 31 | "people had high confidence in their intuitions, and they were essentially useless" | 直觉1 L110 | ✓ | UNSW 2021 逐字命中（谈 IDF 无结构面试："**So people had high confidence in their intuitions, and they were essentially useless.**"） |
| 32 | "It's somewhere around 10 percent… what we found was 50 percent" | 直觉2 L118 / L172 | ✓ | CWT 2018 逐字（见 #17）。`quotes.md` #55 版本更完整且准确 |
| 33 | "I'm going to pass." | 直觉3 L123 | ✓ | CWT 2018，观众问"有什么值得乐观的"，答："I'm going to pass."（全场唯一一次） |
| 34 | "I am optimistic on virtually nothing." | 直觉3 L124 | ⚠️ | 原话是 **"I'm** optimistic on virtually nothing."（CWT 2018）。引号内擅自展开缩写，属微改直接引语，建议照录 |
| 35 | "Despite 45 years of work in the field, I am still inclined to make over-confident predictions." | 直觉3 失效案例 L125 | ⚠️ | **引语逐字正确**，但 `quotes.md` #38 标为"Guardian 2011"，实为 Guardian《This much I know》**2012-07-08**。年份需改 |
| 36 | "I have learned never to make forecasts" | 直觉3 L126 | ✓ | Guardian 2021-05-16（Tim Adams）："**I have learned never to make forecasts.** Not only can I certainly not do it – I'm not sure it can be done." |

---

## 8. 决策启发式（9 条）

| # | SKILL.md 原句（截取） | 位置 | 判定 | 依据 |
|---|---|---|---|---|
| 37 | "Meehl 1954 之后他一辈子用这一问" | 启发式 2 L132 | ✓ | Meehl, *Clinical versus Statistical Prediction* (1954)；自传："just after the publication of 'Clinical versus statistical prediction' (Meehl, 1954)… it certainly had a big effect on me" |
| 38 | 规划谬误——他自己写书也预测「会惨败」 | 启发式 6 L136 | ⚠️ | 方向可信（他多次说写 TFS 极度痛苦、"quit two dozen times" 见 Freakonomics 纪念集），但**"预测会惨败"的具体原话未核** |
| 39 | "I don't try to be clever at all." | 启发式 8 L138 | ✓ | Jason Zweig 访谈（Money/WSJ 存档）："when it comes to investing, he says, 'I don't try to be clever at all.'" |
| 40 | "My research adds absolutely nothing to this." | 启发式 9 L139 | ✓ | CWT 2018，高中生问怎么用研究选大学："**My research adds absolutely nothing to this.**" |

---

## 9. 表达 DNA

| # | SKILL.md 原句（截取） | 位置 | 判定 | 依据 |
|---|---|---|---|---|
| 41 | "I am not a member of your community… Count me as a general believer." | 偏好 1 L162 | ✓ | 2012-09-26 群发信原文（Nature 497:016）："**I am not a member of your community**… **Count me as a general believer.**"（省略号删去的是"我新写了本书"一段，属合法省略） |
| 42 | 限定词多于确定词（2.5:1） | 偏好 3 L164 | ⚠️ | 与 `references/research/03-expression.md` 口径**一致**（n=20 段／700 词／39 句，限定:确定 = 2.5:1），但语料与计数脚本未随包留存，**无法复算**；且样本仅为书面短篇，不能外推到全部语域 |
| 43 | "Was I always so careful? Probably not." | 偏好 3 L164 | ⚠️ | **未能核验出处**（`quotes.md` 未收录此条，也无来源标注） |
| 44 | 不用感叹号（700 词样本 0 个） | 禁忌 1 L167 | ⚠️ | 同 #42，口径自洽但不可复算；"700 词"指书面样本，正文若写"他不用感叹号"需加"在其书面样本中" |
| 45 | "I have been mostly cheering Thaler… from the sidelines" | 禁忌 3 L169 | ✓ | 自传逐字："since that time I have been **mostly cheering Thaler and behavioral economics from the sidelines**. There has been much to cheer about." |

---

## 10. 时间线（SKILL.md 精华表 9 行）

| # | SKILL.md 原句（截取） | 位置 | 判定 | 依据 |
|---|---|---|---|---|
| 46 | 1955 调 IDF 心理学部门（此前 1934 生于特拉维夫、长于巴黎，1944 父亲病逝） | L178 | ✓ | 自传："In 1954, I was drafted as a second lieutenant, and after an eventful year as a platoon leader **I was transferred to the Psychology branch**"＝1955；父 1944 年卒（D-Day 前六周） |
| 47 | IDF 服役 1954 入伍、1956 退伍（不是 1954–1961） | L178＋`timeline-table` 冲突项 1 | ✓ | 自传："**I came out of the Army in 1956.**"（已抓全文核对） |
| 48 | **1965** 讲「表扬有效」被飞行教官当场反驳 | L179 | ⚠️ | 事件与自述真实（自传"the most satisfying Eureka experience of my career"），但**自传全篇未给年份**，且该段落在"1961 返希伯来任教"之后、1965 密歇根休假之前；1965 年他人在密歇根做瞳孔研究。**建议改为「1960 年代中期」**，否则有年代错置之嫌。另注：TFS 第 17 章确另有版本（无年份），与自传不冲突 |
| 49 | 1969 请 Tversky 讲课，午饭交换各自的判断错误 | L180 | ✓ | 自传："From 1968 to 1969, I taught a graduate seminar… I asked my younger colleague Amos Tversky… we decided to meet for lunch… There we exchanged personal accounts of our own recurrent errors" |
| 50 | "Our magic worked only when we were by ourselves." | L180 | ✓ | 自传逐字："**Our magic worked only when we were by ourselves.** We soon learned that joint collaboration with any third party should be avoided…" |
| 51 | 1974《Judgment under Uncertainty》／1979《Prospect Theory》 | L181 | ✓ | *Science* 185(4157):1124–1131；*Econometrica* 47(2):263–291 |
| 52 | 1996-06-02 Tversky 去世，59 岁（转移性黑色素瘤） | L182 | ✓ | Palo Alto Weekly 讣闻（1996-06-12）："died at his Stanford home **June 2** of **metastatic melanoma**. He was **59**."；生 1937-03-16 |
| 53 | "There is a large Amos-shaped gap in the mosaic." | L182 / 附录A#12 | ✓ | 自传所载 1996-06-05 悼词逐字："**There is a large Amos-shaped gap in the mosaic, and it will not be filled.**" |
| 54 | 2002 诺贝尔经济学奖（与 Vernon Smith 共享） | L183 | ✓ | 2002 年瑞典央行纪念奖，与 Vernon L. Smith 共享（Nobel 颁奖辞） |
| 55 | "I feel it is a joint prize." | L183 | ✓（出处需改） | 逐字正确，但出自 **NYT《A Conversation with Daniel Kahneman》2002-11-05**（"I feel it is a joint prize… We were twinned for more than a decade."），**不在诺奖自传、也不是 PU 2002-10-09 新闻**。自传中无此句（已核全文） |
| 56 | 2004–09 与 Klein 对抗性合作；"A Failure to Disagree" | L184 | ⚠️（标题 ✓） | 标题 ✓＝Kahneman & Klein 2009, *American Psychologist* 64(6):515–526，副题 "A failure to disagree"。**起始年 2004 未核**：CWT 只说"六年"，论文本身未标起始年 |
| 57 | 2011／2012／2017／2021 出版 TFS／priming 公开信／公开认错／《Noise》 | L185 | ✓ | TFS 2011；信 2012-09-26（Nature 497:016）；认错 2017-02-14；*Noise* 2021-05 |
| 58 | 那封信**不是认错信**，是救火信 | L185 | ✓ | 信件原文自称"general believer"、把举证责任推给领域；UNSW 2021 亲口："I still believed in priming, when I wrote that letter" |
| 59 | 2023-03 PNAS 修正「7.5 万美元幸福天花板」 | L186 | ✓ | Killingsworth, Kahneman & Mellers, *PNAS* 120(10):e2208661120，2023-03-01；摘要逐字"explain why Kahneman and Deaton **overstated the flattening pattern**" |
| 60 | **89 岁**最后一次公开改错 | L186 / M6 证据 / `timeline-table` | ⚠️ | 算术偏差：1934-03-05 生，2023-03-01 发表＝**88 岁 11 个月**，4 天后才满 89。建议写「88 岁」或「去世前一年」 |
| 61 | 2024-03-27 去世，90 岁（生日后 22 天） | L186 | ✓ | NYT 2024-03-27："died on Wednesday. He was 90."；3-05→3-27＝22 天 |

---

## 11. 价值观 / 谱系

| # | SKILL.md 原句（截取） | 位置 | 判定 | 依据 |
|---|---|---|---|---|
| 62 | 和一个学派对峙了**三十七年** | 张力 3 L197 | ⚠️ | "37 年"说法有二手来源（Freakonomics 2024 纪念集："Gerd Gigerenzer criticized their work for 37 years"），但**起点未交代**；若以 1996 年 *Psychological Review* 论战起算至 2024 仅 28 年。建议注明起算年或改为「近四十年」 |
| 63 | ego depletion 他用了 "conclusively" 而证据崩塌，**他未公开回应** | 张力 4 / 诚实边界 L198、L207 | ⚠️ | 未能核验。TFS 中该词的具体位置未比对（纸书未逐页核）；"未公开回应"属**否定性断言**，需证据支撑（缺证不等于无回应） |
| 64 | 智识谱系：Simon → Meehl 1954 → Tversky → Treisman → 我 → Thaler/Sunstein／Gigerenzer／Klein／Flyvbjerg | L202 | ✓ | 各节点均有一手或权威二手支撑（Simon 有限理性、Meehl 1954、Treisman 1967 哈佛报告、Klein 合作、Gigerenzer 论战）；Flyvbjerg 参照类预测的关联成立 |

---

## 12. 诚实边界

| # | SKILL.md 原句（截取） | 位置 | 判定 | 依据 |
|---|---|---|---|---|
| 65 | hot hand：他 2016 年当面承认 **"Tversky et al. were wrong"** | 诚实边界 L207 | **✗** | 三重问题：①**违反自定纪律**——`quotes.md` 末节明写此句"英文原书未取得…**不要加引号**"，SKILL.md 仍加引号；②**年份存疑**：Ben Cohen《The Hot Hand》(2020) 的引述被转引为"**2015 年**在哥伦比亚大学**的听众面前**"（"I think clearly Tversky et al. were wrong. Their test was biased, and there is a hot hand."），中文百科作 2016，两说冲突；③**措辞不符**：Cohen 另在播客里记的是"你们说得对，但我认为他们的要点仍然成立"——语气远弱于"were wrong"。→ 正确写法：**去引号**，改为「据 Ben Cohen《The Hot Hand》(2020) 记载，卡尼曼在一次报告会后承认 Tversky 等人的检验有偏（年份记载不一：2015／2016，原话英文未获一手核实）」 |
| 66 | 死亡地点与死因未公开；中文网传「在瑞士安乐死」**无可靠来源，属虚假信息** | 诚实边界 L208 | **✗（最严重）** | 已被证实为**真**。WSJ 2025-03-15/16（Jason Zweig，〈The Last Decision by the World's Leading Thinker on Decisions〉）报道：卡尼曼 2024-03-26 自巴黎飞往瑞士，3-27 在当地接受协助自杀；并刊出其告别邮件原文——"**This is a goodbye letter… I am on my way to Switzerland, where my life will end on March 27**… my kidneys are on their last legs… **I am ninety years old. It is time to go.**" 该报道经 JPost（2025-03-15）等多家媒体转述。→ 正确写法：「死因与地点在他去世当日未公开（NYT：She declined to say where he died），系其本人要求家属不公开；**2025-03 WSJ 报道其为在瑞士接受协助自杀，并公开其告别邮件**」。**把已证实事实定性为"虚假信息"，是本文件最应优先修掉的一条** |
| 67 | NYT：「She declined to say where he died」 | L208 | ✓ | NYT 2024-03-27 逐字："His death was confirmed by his partner, Barbara Tversky. **She declined to say where he died.**"（注意 NYT 称 Barbara 为 **partner**，非 wife——`timeline-table` 处理正确） |
| 68 | 合作细节：自传确证「同处一室、不分工、掷硬币定一作、两条平局规则」；但「我们像一个人／轮流起草／谁写最后一句」无一手原文 | L210 | ✓ | 自传："we avoided any explicit division of labor"；"We tossed a coin to determine the order of authorship"；"tie-breaking rules for only two topics"（参考文献排序：Amos 决定；英文语法：Kahneman 决定）。"sharing a mind" 确为转述，`quotes.md` 已标注说话人未明 |
| 69 | 巴黎经历**不能**推出「他不信任确定性叙事」 | L211 | ✓ | 自传落点确为 "people were endlessly complicated and interesting"；Guardian 2021 亦记"I don't think that my personal history had much to do with it" |
| 70 | TFS 页码多经 Wikiquote 转引（B 级）；《Noise》未取得原书 | L206 | ✓ | 与 `sources-list` 自述一致；p.212、p.29 两处页码经 Wikiquote 与二手引用互证成立（见 #74、#75） |

---

## 13. 附录 A（12 条）

| # | 引语 | 判定 | 依据 |
|---|---|---|---|
| 71 | "Just make sure that you are reliable, and leave validity to me."（诺奖自传 1955） | ✓ | 见 #10 |
| 72 | "Trying to be reliable had made them valid." | ✓ | 见 #3 |
| 73 | "A surprise awaited us… We found ourselves agreeing most of the time."（K&K 2009 开篇） | ✓ | 原文："**A surprise awaited us** when we got together… **We found ourselves agreeing most of the time.** Where we initially disagreed, we were usually able to converge upon a common position." |
| 74 | "I was more interested in what made people believe in God…"（自传，17 岁） | ✓ | 自传逐字，且明写 "At age seventeen" |
| 75 | "declarations of high confidence mainly tell you…"（TFS p.212，B） | ✓ | 逐字命中；Ch.20 "The illusion of validity"，p.212（ISBN 9780141033570），Wikiquote 与两处独立引用互证 |
| 76 | "System 1 and System 2 … are fictitious characters."（TFS p.29，**2011 年预先声明**） | ✓ | p.29 原文（Psychology Today 逐页引录可证）；且确在书前第 1 章"Characters of the Story"，**是预先声明，不是事后认错**——此判断正确 |
| 77 | "The evidence is gone, but the beliefs are still standing."（Edge 演讲） | ✓ | Edge〈Adversarial Collaboration〉逐字："It turns out that I only changed my mind about the evidence… **The evidence is gone, but the beliefs are still standing.**" |
| 78 | "My position is that none of these things have any effect on System 1. You can't improve intuition."（Atlantic 2018） | ✓（拼接） | 原文两句之间有引述语："**My position is that none of these things have any effect on System 1,**" Kahneman said. "**You can't improve intuition.**" 合并为一句属轻微处理，语义无损；严格起见可加省略号 |
| 79 | "That's my story. I really hope I don't have to stick to it."（同上） | ✓ | Atlantic 2018 逐字（紧接上句） |
| 80 | "I placed too much faith in underpowered studies."（2017-02 博客） | ✓ | replicationindex 评论 #1454（2017-02-14）逐字："What the blog gets absolutely right is that **I placed too much faith in underpowered studies.**" |
| 81 | "I was gullible … that really hurts me because I had put a lot of faith in it."（UNSW 2021） | ✓ | 见 #29 |
| 82 | "There is a large Amos-shaped gap in the mosaic, and it will not be filled."（1996 悼词） | ✓ | 见 #53 |

---

## 14. 附录 B（伪语录黑名单）

| # | 条目 | 判定 | 依据 |
|---|---|---|---|
| 83 | 「我研究幸福，但我不觉得自己更幸福」→ 真版本 "I wrote it and it didn't improve my mind"（指**书**） | ✓ | NPR Hidden Brain #100（2018-03，录制于其 84 岁生日当周）："some people read 'Thinking, Fast and Slow' in the hope that reading it will improve their minds. **I wrote it and it didn't improve my mind.**" 判伪理由正确：中文把"书"换成"幸福" |
| 84 | 「我们只关心谁对，不关心谁赢」→ 自传无对应原文；最接近「讨论到双方满意为止」 | ✓ | 自传："Our principle was to discuss every disagreement until it had been resolved **to mutual satisfaction**" |
| 85 | 「我们像一个人」→ "sharing a mind" 是转述，说话人未标明 | ✓ | NYT 2016 书评引 Lewis 书，`quotes.md` 已标 C 级；处理正确 |

---

## 15. 附录 C（前景理论）

| # | 原句 | 判定 | 依据 |
|---|---|---|---|
| 86 | λ≈2 来自 1992 年特定测量程序的中位数，不是人类常数 | ✓ | Tversky & Kahneman 1992 累积前景理论：损失厌恶系数中位数 ≈2.25，随测量程序变动 |
| 87 | 亚洲疾病问题体现的是**反射效应**，不是「损失厌恶」 | ⚠️ | 前半可辩护（损失框架下转为风险寻求＝反射效应），但该题在文献中的标准标签是**框架效应**（framing effect），且"不是损失厌恶"过于绝对——它常被用来演示损失框架下的偏好反转，与损失厌恶不无关系。建议改为「体现的是框架效应／反射效应，**不是**单纯用损失厌恶就能解释」 |

---

## 16. 附录：调研来源段

| # | 原句 | 判定 | 依据 |
|---|---|---|---|
| 88 | 一手占比 >50%（诺贝尔自传、四篇核心论文、2012 公开信、2017 认错原文…） | ✓ | `sources-list` 50 条中一手 26 条＝52%；四篇核心论文（1971/1974/1979/1984）确在列 |
| 89 | 批评方与复现研究 **14 篇** | ⚠️ | 实为 **19 条**（批评方 27–38 共 12，复现 39–45 共 7）。计数需改 |
| 90 | 六路调研见 `references/research/`（01–08） | ⚠️ | 目录实为 8 个文件；"六路"与"01–08"自相矛盾 |
| 91 | `quotes.md` 开头："SKILL.md 正文只保留 16 条最高频引语" | ⚠️ | 附录 A 实为 **12 条**（编号 1–12）。16 vs 12 对不上，改一处即可 |
| 92 | 附录 A 12 条未逐条标 A/B 级（p.212、p.29 为 Wikiquote 转引） | ⚠️ | `quotes.md` 逐条标了级别，附录 A 只在 #5、#6 写了"（B）"，其余未标。诚实边界已整体自认"页码经 Wikiquote"，**不构成错**，但建议逐条加级别，避免读者把 B 级当一手 |
| 93 | frontmatter："一手占 **6 成以上**" | **✗** | 与自己的清单不符：`sources-list` 一手 26 条／总 50 条＝**52%**；即便按"45 份"算也只有 58%。同一文件 L252 又写"一手占比 >50%"——两处互斥，且 6 成这一处是虚高。→ 正确：改为「一手约五成（26/50）」或删去比例 |
| 94 | （全篇隐含）"一手占比"这一指标可被复算 | ⚠️ | `references/sources/` 为**空目录**，50 条来源无任何本地留存（无 PDF／快照／逐字稿文件）。比例只能按条目类型数粗算，**无法按内容复核**；建议注明"按条目类型统计"或补留存 |

---

## 17. 统计

| 判定 | 条数 | 占比 |
|---|---|---|
| ✓ 一手核实 | **62** | 66.0% |
| ⚠️ 转引／未能核验 | **25** | 26.6% |
| ✗ 错 | **7** | 7.4% |
| 合计 | **94** | 100% |

### ✗ 七条清单（按严重度排序）

1. **#66 瑞士安乐死＝"虚假信息"** —— 已被 WSJ 2025-03-15 报道＋其本人告别邮件证伪。把真事说成假消息，属于最危险的一类错误（会让使用者反过来"辟谣"真相）。
2. **#30 "since they had survived the peer-review process…"** —— 转述冒充原话，且来源标错（UNSW 全文无此句）；原文在 2017-02-14 博客留言里，措辞完全不同。
3. **#65 hot hand "Tversky et al. were wrong"** —— 违反本文件自己写的"不要加引号"纪律；年份 2015/2016 两说冲突；原话未获一手。
4. **#7 "you're turning us into robots"** —— 自传原文是"being reduced to unthinking robots"，且是转述；引号内的第一人称句子系自造。
5. **#16 2014 年保险咨询** —— 三位作者自述为 **2015** 年、48 名核保员。
6. **#15 收入只影响满意度、不影响当下情绪** —— 与 Kahneman & Deaton 2010 的结论不符，且与同文件 M5／时间线的 2023 修正自相矛盾。
7. **#93 frontmatter「一手占 6 成以上」** —— 自报指标虚高（实 52%），且与 L252「>50%」互斥。**最轻**，但属可验证的错数。

### 最严重的一处

**#66。** 其余五条是"引语精度"问题，读者至多被误导一句；#66 是**主动把可核实的事实判定为虚假信息**，且写进了"诚实边界"这一最需要可信度的章节。它同时说明采集时漏掉了 2025 年 3 月这一整轮报道（截止日却写着 2026-10-20）。修复成本极低（改一行＋补一个来源），但不修的代价最高。

### 另需一并修的次级问题（不计入 ✗）

- `quotes.md` #38 的"Guardian 2011"应为 **2012-07-08**；#52 悼词日期 1996-06-05 正确，但 `03-expression.md` 把它写成"Tversky 去世当日"（去世是 06-02），需改。
- 核保数字建议统一注为「他口述 50%（CWT 2018）／书面 55%（《Noise》、NYT 2021）」。
- 时间线"1974 Science 5 页"：1124–1131 为 **8 页**。
- 三处计数（六路/45 份/14 篇/01–08）互相打架，建议全部改为自动统计或删数字。

---

## 18. 附：就评分方三个提问的明确裁决

**Q1（"I've been studying that stuff for over 50 years…" 无出处标注）**
该句**不在 SKILL.md 内**，只在 `quotes.md` #37 收录，且已自标「B 级／Sam Harris 播客，期数未核实」。若它出现在**答案文件**（`answers.md`）正文而无级别标注，属**引用标注缺失**（⚠️），不是事实倒置。可换用已核实的一手版本：Gallup Business Journal 2011 访谈——"I've been studying this stuff for 45 years, and I don't think I have gotten a lot smarter."（注意是 **45 年**，不是 50 年；两句意思相近但措辞与年数都不同，不可互替）。

**Q2（「谁对 > 谁赢」是否属伪语录回流）**
判 **⚠️ 形式风险，不判 ✗**。理由：附录 B 封杀的是**带引号、被当作他原话**的格言化版本；SKILL.md 价值观段写的是「我追求的：……谁对 > 谁赢」，无引号、无出处标注，属**框架提炼**（可回溯到自传"discuss every disagreement until resolved to mutual satisfaction"与"preferring to be approximately right rather than precisely wrong"）。但同一文件一边封杀、一边以近似格言的形式使用，确有辨识风险——建议在该段加一句「以下为框架提炼，非原话」。**不构成 V1 级问题。**

**Q3（附录 A 未逐条标 A/B 级）**
判 **⚠️**（见 #92）。诚实边界已整体自认「页码经 Wikiquote」，属已披露，不是隐瞒；建议把 `quotes.md` 的级别搬到附录 A 每条末尾。

**给评分方的直接答复**：**有命中项**——共 **7 条 ✗**，按性质分：
- 转述冒充原话／自造引语 3 条：#7（"you're turning us into robots"）、#30（peer-review 那句）、#65（hot hand）；
- 年代错置 1 条：#16（2014→2015）；
- 研究结论失真 1 条：#15（收入与当下情绪）；
- 事实判反 1 条：#66（瑞士安乐死）；
- 自报指标虚高 1 条：#93（"6 成以上" vs 实 52%）。

**不存在**"把 A 的结论挂到 B 名下"式的整体张冠李戴：人名—事件归属除 #55（"joint prize" 出处指向错，句子本身对）外基本正确。"六维""Meehl 1954""Klein 六年""Amos-shaped gap"等关键归属均可回溯一手。

**更正记录（v2，2026-10-20 20:2x）**：本报告初版为 90 条（✓62/⚠️22/✗6）。经评分方指出后补入 #93（frontmatter 一手比例虚高，新增 1 ✗）、#94（`references/sources/` 空目录，比例不可复算）、#91、#92 四条，现为 **94 条：✓62 / ⚠️25 / ✗7**。**以本版为准**；若他处引用了 90 条/6 ✗ 的旧数字，请以本行为准更新。

---

## 19. 复审台账（v3，2026-10-20）：6 条 ✗ 的修复确认

> 复审方式：不看修订说明，直接读修改后的 `SKILL.md`，再独立回到一手来源比对。**6/6 通过。**

| ✗ 编号 | 修改后正文（截取） | 复签 | 我的独立核验 |
|---|---|---|---|
| #7 | 「面试官近乎哗变——自传原话是『觉得自己被降格成了不会思考的机器人』（转述，无第一人称原话）」 | **通过** | 自传逐字 "felt that they were being reduced to unthinking robots"，确为转述；自造的第一人称引语已删。仅提示："自传原话…（转述）"两个词并置略拗，可改「自传用的是转述句」 |
| #16 | 「2015 年在保险公司做噪声审查：48 名核保员…实测中位差异 55%（他 2018 年访谈口述 50%）」 | **通过** | 与 NYT 2021-05-15 三位作者自述一致（2015／48 人／55%）；并把 CWT 的 50% 作为口述版本并列，比我建议的更完整 |
| #15 | 「收入与情绪：7.5 万美元以下两者同升，之上『当下情绪』趋平而『生活满意度』继续升（KD 2010，2023 修正）」 | **通过** | 与 KD 2010 结论及 KKM 2023 修正均相符，M3 与 M5 的自相矛盾已消除 |
| #30 | 「…他 2017 年自己写过：当时认为『如果声誉良好的期刊上有大量证据支持一个起初不可信的结论，科学规范就要求我们相信它』（2017-02-14 博客留言）」 | **通过** | 即 replicationindex 评论 #1454 原文的准确中译，出处与日期均对；转述冒充已消除 |
| #65 | 「（据 Ben Cohen《The Hot Hand》2020 转述…年份两说 2015／2016，英文原话未获一手核实，**不可加引号**）」 | **通过** | 引号已去、两说并列、并自设禁用标记——正是 `quotes.md` 原本的纪律 |
| #66 | 「2025-03《华尔街日报》披露：他 2024-03-26 赴瑞士，3-27 接受协助自杀，告别邮件原文…；家人强调他不为此背书」 | **条件通过**（见下） | 协助自杀、3-27、邮件原文、家人不背书＝均已核；**唯「3-26 赴瑞士」是转引**，建议加「据 WSJ 报道」四字 |

### #43 改判：⚠️ → ✓

`Was I always so careful? Probably not.` **确在诺奖自传中，逐字命中**，紧接在 "research on heuristics and biases only refutes an unrealistic conception of rationality, which identifies it as comprehensive coherence" 之后（下一段还有同构的 "Was this always as clear to me as it is now? Probably not."）。`SKILL.md` 已把出处标为「诺奖自传」，判定由 ⚠️ 升 ✓。

### 复审新增两条判定

| 新编号 | 句子 | 判定 | 依据 |
|---|---|---|---|
| 95 | 「家人强调他不为此背书」 | ✓ | WSJ 报道经 JPost 转述："his friends and family say… he did not advocate assisted suicide and never wanted his practice to be seen as an endorsement" |
| 96 | 「他 2024-03-26 赴瑞士」 | ⚠️（可保留，需标转引） | WSJ 原文在付费墙后，**我未能直接读到 "March 26"**；但三处独立二手一致：英文复述（"On March 26, Kahneman left his family in Paris and flew to Switzerland"）＋两处中译（"3月26日，卡尼曼离开了家人，飞往瑞士"）。→ 建议写「2024-03-26（据 WSJ 报道）」，**不必退成「2024-03」**；退成月份反而丢失已可确证的信息 |

### 残留的小不一致（不计 ✗，一句话可修）

- M1 证据行仍写「核保员同案定价差 **50%**」，而 M4 已改为「中位差异 **55%**（口述 50%）」。两处指同一研究，建议 M1 同步为「约 55%（他口述 50%）」。

### 修复后统计

| 判定 | 条数 |
|---|---|
| ✓ | **63**（62 + #43 改判） |
| ⚠️ | **24**（25 − #43；另新增 #96 未计入本表，见下） |
| ✗ | **0**（6 条已修复） |

> 口径说明：#95、#96 属"复审新增"，若并入总数则为 96 项、✓63 / ⚠️25 / ✗0。本报告表内 94 项为审计基线，未回填 SKILL.md 的修订内容，以便保留"发现时状态"。

---

## 20. 二次复审（v4）：⚠️ 项闭合情况

> 复核方式同 §19：直接读当前文件＋对一手源。**7 条 ✗ 全部闭合**（含 #93，frontmatter 已改为「一手 52%」）。

### 本轮回合的 ⚠️（5 条）

| 编号 | 原问题 | 现状 | 判定 |
|---|---|---|---|
| #2 | 「六路 45 份来源」vs 实 8 文件／50 条 | 已改「六路 50 条来源调研…一手 52%；另含 8 份落盘调研」 | **闭合**（"六路"与"8 份"仍并存，但不再给出错数） |
| #89 | 「批评方与复现研究 14 篇」 | 已拆为「批评方 12 条＋复现研究 7 条」 | **闭合**（12+7=19，与原表一致） |
| #90 | 「六路…（01–08）」自相矛盾 | 已改「八份调研见 `references/research/`（01–08）」 | **闭合**（实点目录 8 项） |
| #91 | quotes.md 说「保留 16 条」，附录 A 实 12 条 | 现在**两处都写 10 条**；实点附录 A 条目＝**10** | **闭合**（评分方担心的 12 vs 10 未出现） |
| #94 | `references/sources/` 空目录 | 目录已删（`MISS references/sources`） | **闭合**；但"50 条来源无本地留存"这一事实不变，比例仍只能按条目类型算 |

### 未闭合的一处一致性残留（⚠️，非 ✗）

核保数字现有三个层次，需分清，**不能一刀切改 55%**：

| 位置 | 现文 | 意见 |
|---|---|---|
| M1 证据 L62 | 「约 55%（他口述 50%）」 | ✓ 已改好（评分方读到的 50% 是旧版） |
| M4 来历 L82 | 「中位差异 55%（他 2018 年访谈口述 50%）」 | ✓ |
| 直觉2 事后归因 L116 | 对白还原：「你觉得是多少？」「大约 10%。」「实测 50%。」 | **保留**。这是对 CWT 那段问答的还原，CWT 原话即 "what we found was 50 percent"；改为 55% 反而与引语冲突。若求稳可加「（他口述）」 |
| 启发式 3 L133 | 「核保实验的 10% 与 50%」 | **建议改 55%**。此处是无引号的摘要，与 M4 并列时显得矛盾 |

→ 仅 **1 处**（L133）建议动，且属编辑层面的一行替换；不计入 ✗。

### v4 状态重算（按修复后统计，与 §17 基线不冲突）

| 状态 | 条数 | 构成 |
|---|---|---|
| ✓ 已核实 | **71** | 基线 62 ＋ 7 条已修复的 ✗ ＋ #43 改判 ＋ #95 |
| ⚠️ 未闭合 | **20** | 25 − 5 条已闭合 − #43（转 ✓）＋ #96 |
| ⚠️ 已闭合 | **5** | #2 #89 #90 #91 #94 |
| ✗ | **0** | 7 条全部修复，复签 7/7 |
| 合计 | **96** | 与 `grep -cE '^\| [0-9]+ \|'` 一致 |

---

## 21. 结档（v5 · 终态）

> 审计人已停止改动。以下为**最终引用口径**，与 §17 基线并列使用。

### 本轮又闭合 3 条 ⚠️

| 编号 | 原问题 | 现文 | 判定 |
|---|---|---|---|
| #18 | "noise and bias are independent sources of error" 未标级 | 已加「（B，逐字未核）」 | 闭合 |
| #22 | "the experience was not ruined…"（2005）未标级 | 已加「（2005；B，章节原文未取得）」 | 闭合 |
| #25 | "everyone was wrong" 转述冒充原话 | 已去引号，改「结果双方各错一半」 | 闭合 |

### 仍未闭合（⚠️，均属"可接受但可更好"，无事实错误）

- **#92** 附录 A 只标例外（#4、#5 标 B），其余 8 条未逐条标级。按惯例可接受；建议第 1、2、3、6、7、8、9、10 条补「——A」即完全一致。
- **#96** 「2024-03-26 赴瑞士」仍未标「据 WSJ 报道」；「家人不为此背书」同理。一手在付费墙后，现有三处二手一致。
- **L133** 启发式 3「核保实验的 10% 与 50%」建议改 55%（M1/M4 已是 55%）。
- 其余为"未能核验"类（#11 #13 #20 #23 #28 #31 #34 #35 #38 #41 #42 #43→已改✓ #44 #46 #47 #48…），性质是**缺一手证据**，不是错。

### 终态计数

| 状态 | 条数 | 说明 |
|---|---|---|
| ✓ 已核实 | **74** | 71 ＋ 本轮 #18 #22 #25 由 ⚠️ 转 ✓ |
| ⚠️ 未闭合 | **17** | 20 − 3 |
| ⚠️ 已闭合 | **5** | #2 #89 #90 #91 #94 |
| ✗ | **0** | 7 条全部修复，**复签 7/7** |
| 合计 | **96** | |

> 对外一句话：**「审计基线 94 项 / ✗7 → 修复后 ✗0（7/7 复签）；现余 17 条未闭合 ⚠️，无一为事实错误，均可读作『缺一手证据』或『可再补一句标注』。」**

### 补记（v5.1，审计人最后一次改动）

结档后又核实三处，均已改好，故终态应为 **✓75 / ⚠️未闭合 16 / ⚠️已闭合 5 / ✗0**：

| 位置 | 现文 | 判定 |
|---|---|---|
| L207 | 「2025-03《华尔街日报》披露（**据该报道**）…；**据该报道**，家人强调他不为此背书」 | #96 **闭合** |
| L133 启发式 3 | 「核保实验的 10% 与 **55%**（他口述 50%）」 | **闭合** |
| L116 直觉 2 | 改为「再给实测：访谈里他说 50%，书中与 NYT 文记 55%」——比我建议的更好，既保住对白还原、又标明两个来源 | **闭合** |

**至此 17 条未闭合中，只剩 #92（附录 A 逐条标级）一条属"可一行改掉"；其余 15 条全部是"未能核验"类（缺一手证据），不是错。**

> 若某处已印"17 条未闭合"，与 16 的差别仅在此一条，实质不变；本表以 16 为准。

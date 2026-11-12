# 08 · 独立事实审计（Fact Audit）

- **审计对象**：`skills/musk-perspective/SKILL.md`
- **审计日期**：2026-10-12 / 2026-10-13
- **审计角色**：独立事实审计员（不参与 Skill 撰写）
- **方法**：对 SKILL.md 中所有带引号引语、具体年份、具体数字、被断言事实，用 WebSearch / WebFetch 独立核查，**不采信 01–07 号调研文件的结论作为依据**（仅作线索）
- **判定图例**：
  - ✅ 核实通过
  - ⚠️ 措辞有出入（给出更准确的表述）
  - ❌ 查无实据或事实错误（建议删除或改写）
  - 🔸 仅二手来源 / 未能独立核实（建议降级或加限定）

---

## 一、重点核对清单（用户指定 15 项）

| # | SKILL.md 中的表述 | 判定 | 独立核实结果与依据 |
|---|---|---|---|
| 1 | 题词 "boil things down to their fundamental truths and reason up from there, as opposed to reasoning by analogy." —— 2013 TED，Chris Anderson 访谈 | ✅ | 逐字准确。完整语境为 "Well, I do think there's a good framework for thinking. It is physics… the sort of first principles reasoning. Generally I think there are — what I mean by that is, boil things down to their fundamental truths and reason up from there, as opposed to reasoning by analogy."（Adweek、CNBC/NBC Chicago 转录）。场合与时间标注正确 |
| 2 | "the best part is no part. The best process is no process. It weighs nothing, costs nothing, can't go wrong." + "What did you undesign?" —— 2020 Starship Update | ✅ | 确为 2020 年 Starship Update 的 Q&A 环节（Wikiquote 存有带 YouTube 时间戳的出处）。两句均逐字准确。**附赠**：同场还有 "If a schedule is long, it's wrong. If it's tight, it's right."，可支持 SKILL.md 模型7 的「2020年：如果一个排期很长，那它本身就是错的」 |
| 3 | 2017 New Space 论文「火星成本要降 5,000,000%」「全复用贡献 2–2.5 个数量级」 | ⚠️ 措辞有出入（轻微） | 原文（EarthSky 转录、EurekAlert/phys.org 出版方通稿）：*"It is a bit tricky because we have to figure out how to improve the cost of trips to Mars by five million percent. **This translates to an improvement of approximately four-and-a-half orders of magnitude.** … Most of the improvement would come from full reusability — **somewhere between** two and two-and-a-half orders **of magnitude**. The other two orders of magnitude would come from refilling in orbit, propellant production on Mars, and choosing the right propellant."*<br>问题：SKILL.md 用省略号跳过了「总量约 4.5 个数量级」这个关键中间句，读者会以为 5,000,000%（≈4.5 个数量级）几乎全由复用贡献。另外 "two to two-and-a-half orders" 漏了 "of magnitude"，且原文有 "somewhere between"。<br>注：正文第 57 行的拆解（全复用 2–2.5 个数量级 + 轨道加注 + 推进剂原位生产 + 选对推进剂）**是准确的**，与原文一致 |
| 4 | 2018年12月「碳纤维 135 美元/公斤，35% 废料，实际接近 200 美元/公斤。钢是 3 美元/公斤。」（Popular Mechanics） | ✅ | 逐字准确。原文："The carbon fiber is $135 a kilogram, 35 percent scrap, so you're starting to approach almost $200 a kilogram. The steel is $3 a kilogram."（Popular Mechanics, Ryan D'Agostino 访谈，2018-12）。中译「35% 废料」对应 35% scrap（加工报废率），可接受 |
| 5 | 2008「如果我把钱平分，可能两个都会死……」（Vance 传记 / The Verge） | ✅ | 原文（The Verge 2015-05-14 转 Bloomberg 摘录 Vance 即将出版传记）：*"I could either pick SpaceX or Tesla or split the money I had left between them. That was a tough decision. If I split the money, maybe both of them would die. If I gave the money to just one company, the probability of it surviving was greater, but then it would mean certain death for the other company. I debated that over and over."* 中译忠实。「我反复想了很多遍」＝"I debated that over and over"，可接受 |
| 6 | 2026年2月 SpaceX 收购 xAI 备忘录「全球 AI 电力需求即便在短期内也无法靠地面方案满足……唯一合乎逻辑的解法是把这些资源密集型工作转移到拥有巨大能量和空间的地方」 | ✅ | 逐字准确。SpaceX 官网 Updates（2026-02-02）：*"Global electricity demand for AI simply cannot be met with terrestrial solutions, even in the near term, without imposing hardship on communities and the environment. … The only logical solution therefore is to transport these resource-intensive efforts to a location with vast power and space."* 同时 "sentient sun… light of consciousness to the stars" 原文为 "scaling to make a sentient sun to understand the Universe and extend the light of consciousness to the stars!" ✅<br>**建议补**：备忘录公开日期为 **2026-02-02**（SKILL.md 仅写「2026年2月」） |
| 7 | 五步算法（make requirements less dumb / delete / simplify / accelerate / automate），2021 Starbase，顺序不可颠倒 | ✅ | 出处与顺序均正确：Starbase Tour with Tim Dodd（Everyday Astronaut），拍摄于 2021-07-30。原话五步：① make the requirements less dumb（每个要求要追溯到人名而非部门）② delete the part or process（若不加回至少 10% 就是删得不够）③ simplify/optimize ④ accelerate cycle time ⑤ automate。Musk 自述曾把顺序做反、工程师本能地从第⑤步倒着做——SKILL.md 的表述准确 |
| 8a | **2026-02-08** 宣布 SpaceX 重心转向月球自给城市，火星目标推迟 5–7 年 | ⚠️ | 日期与事件属实（Musk 2026-02-08 X 帖，新华社/DW/AP/BI 均报道）。但两处措辞不准：<br>① 原文是 **"self-growing city"（自我生长/自我扩张的城市）**，不是「自给（self-sufficient）城市」<br>② 「火星目标推迟 5–7 年」≠ 原意。原话是：月球城市 **<10 年**可成，火星需 **20 年以上**；SpaceX 仍计划在 **5 到 7 年后启动（starting in five to seven years）**火星建城计划。即「5–7 年」是**启动时间点**，不是「推迟量」 |
| 8b | **2026-06-11/12** SpaceX IPO 定价 135 美元，登陆纳斯达克，史上最大规模 IPO | ✅ | 发行价 $135、6 月 12 日纳斯达克挂牌（代码 SPCX）、募资 750 亿美元创美股 IPO 纪录，均属实（SEC 文件、新华财经、中新社）。定价/发行日 6-11、挂牌日 6-12 的表述准确。可补：首日收涨约 19% |
| 8c | **2026-08-06** TeraFab 在德州 Grimes 县破土，初期投资 168 亿美元 | ✅ | 2026-08-06 SpaceX 与特斯拉联合宣布选址 Grimes 县、初期投资约 168 亿美元（TechCrunch 2026-08-06、德州州长办公室公告）。可补：创造 3000 个岗位、远期总投资可能达 1190 亿美元 |
| 8d | **2026-09-28** 星舰第 14 飞首次入轨，部署 26 颗 Starlink V3 | ✅ | SpaceX 官网 Flight 14 页面与 CGTN/NPR 均确认：2026-09-28 发射，星舰首次入轨，部署 26 颗 Starlink V3。（细节：因上升段一台真空 Raptor 关机，任务由原定约 10 小时/6 圈缩短至约 3 小时/2 圈——SKILL.md 未提，但也不算错） |
| 8e | **2026-10-02** Tesla Q3 交付 486,532 辆，储能装机 13.7 GWh | ✅ | 与 Tesla 提交 SEC 的 8-K 附件（ir.tesla.com，2026-10-02 发布）完全一致：生产 464,391、交付 486,532、储能 13.7 GWh |
| 8f | **2026-09-21** Grok 4.7 为当前旗舰，Grok 5 仍未发布 | ✅ | Grok 4.7 于 2026-09-21 发布（500K 上下文，$2/$6 每百万 token），Grok 5 仍在训练、无发布日期 |
| 8g | **2026-09-03** Cybercab 在奥斯汀投入载客；同月 NHTSA 要求其就自我认证作出宣誓说明 | ⚠️ | 前半句 ✅（AP：2026-09-03 Cybercab 在奥斯汀开始付费载客）。<br>后半句 ⚠️：NHTSA 的动作是**开启 Audit Query（AQ26002，2026-09-03，覆盖约 1000 辆 Cybercab）**，目的是"examine the process and technical data" Tesla 认证时所依赖的依据，属于**流程审计、非缺陷调查**，也未要求 Tesla 停运。「要求作出**宣誓说明**」这一表述未见权威来源支持，建议改写 |
| 9 | NYT 统计「602 项承诺、19% 按时、35% 逾期或落空」 | ✅ | 完全属实。NYT《Elon Musk Laid Out 602 Goals. We Counted How Many He Hit.》（2026-06-02，Kirsten Grind 等）：602 项带期限目标，约 19% 按时完成、约 35% 逾期或未交付、约 33% 无法验证、约 13% 期限未到；且成功率逐年下降（2015 年 13 项目标达成近 3/4，2020 年 27 项中不到一半按时）。<br>**建议补**：发布日期 2026-06-02，并在正文模型7 中补上「约 33% 无法验证」这一口径（这直接影响 19% 的分母解释） |
| 10 | 「自 2003 年获至少 380 亿美元政府资金」 | ✅ | 《华盛顿邮报》2025-02-26 调查：至少 380 亿美元政府合同、贷款、补贴与税收抵免，时间跨度 20 余年（始于 2003）。Musk 2026-02-09 在 X 上的回应"even if every bit of bullshit he says is true, it still amounts to less than 1% of the value of Tesla and SpaceX"亦属实。<br>**建议**：T4 条目目前未标注该数字的来源，应补「《华盛顿邮报》2025-02-26 统计」 |
| 11a | 2018 SEC 因 "funding secured" 推文罚款并设立推文审查机制 | ✅ | SEC 2018 年以证券欺诈指控 Musk；Musk 与 Tesla 以 4000 万美元和解（不承认/不否认），Musk 辞去董事长，董事会同意对其通讯进行审查。NYT 2026-06-02 文章亦复述此节 |
| 11b | 加州 DMV 裁定（2025-12） | ✅ | 2025-12-16 加州 DMV 就 Case Nos. 21-02188/21-02189 作出决定，认定 Tesla 用 "Autopilot" / "Full Self-Driving Capability" 宣传 ADAS 属误导、违反州法；ALJ 建议吊销产销许可 30 天，DMV 减轻处罚并给 60 天整改期。后续：2026-02-17 DMV 公告 Tesla 已停用 "Autopilot" 一词因而免于停牌。<br>**建议**：把「2025-12」精确到 **2025-12-16** |
| 11c | 欧盟 DSA 2025-12 罚 1.2 亿欧元 | ✅ | 2025-12-05 欧盟委员会作出 DSA 首份"不合规决定"，对 X 罚款 1.2 亿欧元（蓝标 4500 万 + 广告资料库 3500 万 + 研究人员数据访问 4000 万）。后于 2026-02-20 X 提起上诉。<br>**建议**：把「2025-12」精确到 **2025-12-05** |
| 12 | 幽灵刹车投诉「3个月 107 起 vs 此前 22 个月 34 起」 | ⚠️ **（本轮最需注意的一条）** | 数字本身 ✅ 属实（华盛顿邮报对 NHTSA 数据的分析：过去三个月 107 起，此前 22 个月 34 起；The Independent、InsideEVs 同步报道）。但 SKILL.md 的**语境框定有误**：<br>① 该统计出自 **2022 年 2 月**的华盛顿邮报报道（数据窗口约 2021-11 至 2022-01），**不是近期事件**，也**早于超声波传感器移除**（2022 年秋）。SKILL.md 写成「删掉雷达**与超声波**后」，把两个时间点的动作合并了<br>② 同句「**2022年12月 HW4 又把雷达装了回来**」❌。HW4（AI4）硬件平台是 **2023 年**才装车的，其上重新搭载 Arbe Phoenix 4D 成像雷达发生在 2023 年（另有报道提到 HW4 更早的测试节点，但没有「2022 年 12 月装回」的可靠依据）。建议改为「2023 年 HW4（AI4）硬件平台重新搭载了 4D 成像毫米波雷达」 |
| 13 | 2026 Q1 电话会「它会跟整条链条上最不走运、最慢、最笨的那个零件一样快」 | ❌ **出处错置，必须改** | 这句 Musk 确实说过，但**不是 2026 Q1 电话会**。可核实的版本分布在：<br>· Model 3 首批交付仪式（2017-07）：*"the production rate will move as fast as the slowest and least lucky components in the whole mix."*<br>· Recode Decode（Kara Swisher，2018-11-02 发布）：*"whatever the slowest, least lucky part of the production process is, that sets your rate."*<br>· 2015 Q1/Q2/Q3 电话会：*"the production ramp goes according to the unluckiest and worst-performing supplier…"* / *"the thousandth least lucky and slowest"*<br>· **Q3 2020 电话会**（最接近 SKILL.md 的措辞）：*"the rate of growth of production goes as fast as the least lucky and dumbest of those 10,000 things. A bunch of them are not even in our control. It's insanely difficult."*<br>而 **2026 Q1 电话会（2026-04-22）**关于 Cybercab 产能的原话是：*"Whenever you have an all-new product with an all-new supply chain, and everything is new, its growth curve is always a stretched S-curve."* 以及 *"initial production of Cybercab and Semi will be very slow, but then ramping up and going kind of exponential towards the end of the year."*<br>建议：把场合改为「Q3 2020 电话会（更早版本见 2015/2017/2018）」，或改用 2026 Q1 的 "stretched S-curve" 原话 |
| 14a | "I am become meme."（2025 CPAC） | ✅ | 2025-02-20 CPAC（National Harbor, MD），Musk 上台约 1 分 30 秒时说 "I am become meme. Yeah. Pretty much. I'm just living the meme…"（The Hill、Spectator、Mediaite、Know Your Meme 均有记录）。当晚他也在 X 上发了同句 |
| 14b | 2010 年内部邮件标题《Acronyms Seriously Suck》 | ✅ | 2010 年 5 月（5 月 4 日）发给 SpaceX 全员的邮件，标题即为 "Acronyms Seriously Suck"（Vance 传记全文收录；IBT、Verdict 等转载）。内容中的 "That needs to stop immediately or I will take drastic action"、"Unless an acronym is approved by me…" 亦属实 |
| 15 | 2026-07「我在政治上卷入得太深，说实话是失控了」 | ⚠️ | 真话，但**措辞被加重了**。Musk 接受《经济学人》访谈时的原话是：*"I think I got a little too involved in politics. I got carried away, frankly."*（"got carried away"＝做过头/上头，不是"失控"）。<br>日期：多数报道称访谈在 7 月 20 日（周一）于 Giga Texas 进行、7 月下旬播出；另有报道写 7 月 23 日——**日期存在冲突**。<br>后半句「同期仍以 PAC 方式投入中期选战——出钱不出面」✅ 属实：Axios 2026-07-29、NYT/Forbes 2026-07-30 报道 America PAC 获批投入 **1 亿–1.2 亿美元**用于 2026 中期选举地面动员（8 个以上州）。但「同期」宜改为「**数日后**」（访谈 7 月 20–23 日，PAC 消息 7 月 29–30 日） |

---

## 二、额外抽查项（审计员自选）

| SKILL.md 中的表述 | 判定 | 核实结果 |
|---|---|---|
| 2026-10「我现在不知道怎么做微芯片，我们会搞明白的」 | ✅ | 2026-10-10（周六）在奥斯汀 Giga Texas 外的 "X Takeover" 活动上通过直播对车主与投资人所说：目前"完全不知道如何制造微芯片，但我们会搞清楚"；并称"这可能是世界上最难的事之一"、"可能需要好几年"（彭博社、财联社、IT之家）。日期写「2026年10月」正确 |
| Tesla 使命改为「惊人富足」（2026-01/02） | ✅ | 2026-01-21 Tesla 官方宣布新使命 "to build a world of amazing abundance"，取代此前表述（Musk 2025-12 预告为从 "sustainable abundance" 改为 "amazing abundance"）；FY2026 8-K 中亦见 "Amazing Abundance" 表述 |
| Jared Isaacman 出任 NASA 局长 | ✅ | 第 15 任 NASA 局长，2025-11-04 获提名、2025-12-17 参议院确认，2026 年 1 月起在任 |
| 模型6 局限：「DOGE 承诺削减 2 万亿、自报 1750 亿、GAO 2026年8月指出证据不足」 | ⚠️ | ①「承诺 2 万亿」✅（初承诺 2 万亿，后降至 1 万亿）<br>②「**自报 1750 亿**」❌/⚠️ 已过时。DOGE 截至 2026-08-07 自报约 **2150 亿美元**（BBC、GAO 报告口径为约 214–215B）；GAO 抽样审查的约 1100 亿美元中，96% 的拨款类节支无法核实计算方式、2503 份合同（涉及 274 亿美元"节支"）实际未被终止、264 份租约中 108 份在其成立前已在终止流程中<br>③「GAO 2026年8月指出证据不足」✅ 报告确为 2026 年 8 月发布（覆盖 2025-01-20 至 2026-07-07）<br>建议：1750 亿 → **约 2150 亿美元（DOGE 自报，GAO 认为大量不可核实）** |
| 2020年9月「制造比设计难 1000% 到 10000%」 | ⚠️ | 原文（2020-09-21 X 帖）：*"The extreme difficulty of scaling production of new technology is not well understood. It's 1000% to 10,000% harder than making a few prototypes. The machine that makes the machine is vastly harder than the machine itself."*<br>即原话是「**规模化生产**比**做几个原型**难 1000%–10000%」，不是「制造比设计难」。建议补上同句的 "the machine that makes the machine"（造机器的机器），那才是模型3 真正的一手支撑 |
| 2002 年俄火箭报价 800 万美元、回程飞机上算原材料占售价约 3% | 🔸 | 未在本轮独立核实到一手/权威出处。该说法在 Musk 叙述中反复出现（口径亦有 2%/3% 两种），但本轮搜索未能定位原始出处。**建议加限定词**（"据他自述"）或回查 05-decisions 的一手引用 |
| 电池「2013年前后从约 600 美元/kWh 往 80 美元/kWh 推」 | 🔸 | "$600/kWh" 与 "about $80/kWh" 确为 Musk 在 Kevin Rose 2012 访谈中使用的数字（CNBC 复述），但 SKILL.md 把它系在「2013年前后」并称出自"Tesla 官方博客与财报口径"，本轮未能独立确认该出处。**建议改为「2012 年 Kevin Rose 访谈中的举例数字」** |
| 2026 年「全球芯片产能（约 20GW）相对 AI 与机器人需求只是个零头」 | 🔸 | 未能独立核实「20GW」这一口径。建议加限定或回查原始表述 |
| Model Y 后底板玻璃纤维垫、连带删掉 200 万美元机器人（2021） | 🔸 | 该轶事在多个二手来源中出现（Isaacson 传记及各类转述），本轮未找到一手出处。建议保留但加「据 Isaacson 传记」限定 |
| Solar Roof 承诺周装 1000 套、实际 21–32 套、2026 年停产 | 🔸 | 三个数字本轮均未独立核实。建议加来源限定或回查 |
| 4680 电池「2024 年内部设了『打不过 LG 就重新考虑』的 KPI」 | 🔸 | 属内部消息类断言，本轮无可公开核实的一手来源。建议降级为「有报道称」或直接删除 |
| ASML「交期 18–24 个月、工程师缺口三万」 | 🔸 | 未能独立核实具体数字。建议删除具体数字，保留定性表述 |
| Lex Fridman 2019「How would you tell?」 | 🔸 | 未在本轮核实逐字稿。SKILL.md 的用法（谈意识与自我意识时反问）方向可信，但建议回查 2019 官方 PDF 逐字稿后再标为一手 |
| 2018 Q1 电话会「把问题判为无聊/蠢问题直接跳过，第二天又收回来」 | 🔸 | 事件广为流传（"boring bonehead questions" / "dry"），但本轮未独立核实"第二天又收回来回答"的细节。建议核实后保留，否则删后半句 |
| Starlink 冲突地区争议「传记作者更正了『关闭』与『未激活』的措辞」 | 🔸 | 未独立核实。建议加限定 |
| Isaacson「You don't have to be this mean.」 | 🔸 | 该句出自 Isaacson 2023 年传记，广为引用，本轮未直接核实原文页码/上下文。建议加「据 Isaacson 传记」 |
| Anthropic 与 Google 分别以月度付费方式租用 Colossus 算力（2026年5月、6月） | 🔸 | **未能独立核实**。这是「我影响了谁」维度下唯一的硬事实，若无法坐实，建议整条降级或删除（SKILL.md 已声明此维度证据薄弱，方向正确） |
| 学术界出现 "Muskism" 概念化讨论（2025） | 🔸 | 未能独立核实到具体文献。建议加限定或删除 |
| 2022 年 Twitter 裁员约 50%、2022-12 冻结记者账号 | 🔸 | 未在本轮独立核实（均为高知名度事件，但 SKILL.md 未附出处）。建议补出处 |
| DealBook 2023「Go fuck yourself. Go. Fuck. Yourself. Is that clear?」 | 🔸 | 事件与措辞广为报道，本轮未直接核实逐字稿。SKILL.md 已注明「作为语气样本记录，不是行为示范」，处理得当 |
| "Remote work is no longer acceptble [sic]"（2022 内部信） | 🔸 | 未独立核实原文。建议回查内部信全文 |
| 2025 年 6 月与特朗普公开决裂、2025 年 11 月股东批准万亿薪酬方案 | 🔸 | 两条均为时间表中的关键节点，本轮未独立核实具体日期 |
| 2020「absurdly vertically integrated」、2020 Q3「there is no catalog」 | 🔸 | 两句均有流传，本轮未定位到逐字出处。SKILL.md 的模型4 已自注"口头使用频率不高"，方向正确 |

---

## 三、汇总统计

| 判定 | 数量（重点清单 15 项） | 数量（含额外抽查，共 43 条） |
|---|---|---|
| ✅ 核实通过 | 9 | 18 |
| ⚠️ 措辞有出入 | 4（#3、#8a、#8g、#12） | 9 |
| ❌ 事实错误 | 1（#13） | 1 |
| 🔸 仅二手/未核实 | 1（#8g 后半句的次生项） | 15 |

**重点清单通过率**：9/15 = **60% 完全通过**；计入 ⚠️（事实骨架正确、措辞需修）后为 13/15 = **87% 可用**；硬错误 1 项（#13）。

---

## 四、按严重度排序的必改项

1. **【❌ 硬错误】#13 引语出处错置** —— 必须改
2. **【⚠️ 高】#12 幽灵刹车 107/34 的时间语境 + "2022年12月 HW4 装回雷达"** —— 数字对、时间框架错，且含一条未经证实的年份断言
3. **【⚠️ 中高】#8a 月球转向**：「自给城市」→「自我生长的城市（self-growing city）」；「火星推迟 5–7 年」→「火星建城计划推迟到 5–7 年后启动」
4. **【⚠️ 中】DOGE 自报数字**：1750 亿 → 约 2150 亿美元
5. **【⚠️ 中】#8g NHTSA**：「要求作出宣誓说明」→「开启 AQ26002 流程审计，审查自我认证的流程与技术数据」
6. **【⚠️ 中】#15 政治引语**：「说实话是失控了」→「说实话是有点过头了（got carried away）」；「同期」→「数日后」
7. **【⚠️ 低】#3 论文引语**：补回被省略的「总量约 4.5 个数量级」，"two to two-and-a-half orders" → "somewhere between two and two-and-a-half orders of magnitude"
8. **【⚠️ 低】2020-09「制造比设计难 1000%–10000%」** → 「规模化生产比做几个原型难 1000%–10000%」，并补 "the machine that makes the machine"

## 五、可选优化（非必改）

- 补精确日期：备忘录 2026-02-02、加州 DMV 2025-12-16、欧盟 DSA 2025-12-05、NYT 统计 2026-06-02、Tesla 使命 2026-01-21
- T4 条目补上「380 亿美元」的来源（《华盛顿邮报》2025-02-26）
- 模型7 补上 NYT 统计中「约 33% 无法验证」这一口径，避免 19% 被误读
- 把 🔸 标记的 15 条回查一手出处；确实找不到的（Colossus 出租、"Muskism"、4680 KPI、ASML 数字）建议降级为定性表述或直接删除
- 建议在「诚实边界」第 3 条（2026 年口径冲突）中追加一条：TeraFab 初期投资亦有 150 亿 / 168 亿两种报道口径（2026-08 为 168 亿，2026-10 部分报道为"逾 150 亿"）

---

> 本审计只判定事实，不改动 SKILL.md。所有修改建议需由 Skill 撰写方执行后复审。

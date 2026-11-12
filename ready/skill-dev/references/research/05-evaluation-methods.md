# 05 · skill 效用评估与优化方法（SkillLens / SkillOpt / Darwin）

> 调研日期：2026-10-16 ｜ 调研人：小管家（主 agent）
> 动机：skill-dev Phase 4 验证的「执行稳」只说「with/without 看 delta」，未回答两个更根本的问题——**谁来当评委、评委可不可信**，以及**怎么优化已有 skill 才不越改越差**。本文件补上这两块的科学依据与落地工序。
> 星级：★★★ 一手论文 ｜ ★★★ 一手仓库 ｜ ★★ 二手评述

---

## 一、SkillLens（评估）— arXiv 2605.23899

**微软研究院 × 复旦 × 上交**，2026-05-22 挂出。项目页 microsoft.github.io/SkillLens，代码 github.com/microsoft/SkillLens（180★，2026-05-25 活跃）。研究「模型生成的 domain-level skill 全生命周期是否有效、什么决定效用」。

三个对 skill-dev 有直接指导意义的实证发现：

1. **单 LLM 评委不可信**：让单个 AI 给两份 skill 打分选哪份更好，**准确率仅 46.4%**——比随机（50%）还差 3.6 个百分点。在松散的评分标准下，AI 评委的判断基本不可信，「跑出来的优化看起来在涨分，实际可能只是评委在摇骰子」。
2. **「读起来好」≠「实际好」**：pairwise judge 准确率随实际效用差距增大**反而下降**——可读性和实际效用可能负相关。
3. **三个决定效用的文本维度**（实证 rubric，每个单独就能把 better-rate 提到 64% 以上）：
   - **失败模式编码**（Failure Mechanism Encoding）：把已知失败路径显式编码进 skill，不是「告诉 agent 别犯错」式叮嘱。
   - **可执行具体性**（Actionable Specificity）：明文禁止「建议 / 可以考虑 / 根据情况 / 灵活把握 / 视情况而定」等模糊词。
   - **高风险行动黑名单**（High-Risk Action Blacklist）：rm / git reset --hard / force push 等破坏性操作必须显式列禁。

   用这三条做成 meta-skill 前缀，pairwise-judge 准确率 **46.4% → 73.8%**，平均增益 +1.55pp，9/9（domain×target）单元格全改善——**不用改流水线、不加额外调用**。

4. **负迁移（negative transfer）**：强经验池提取的 skill 能稳健迁移到所有 target；弱经验池的 skill 在部分 target 上产生负迁移。skill 效用与模型规模、基线任务强度**均无关**——强 extractor 可能是弱 consumer，反之亦然。

---

## 二、SkillOpt（优化）— arXiv 2605.23904

**微软 × 上交 × 同济 × 复旦**，SkillLens 姊妹篇。代码 github.com/microsoft/SkillOpt（MIT，一周 3.3k★）。把 skill 文档当作 frozen agent 的「外部可训练参数」，用文本空间的「梯度下降」训练它。

对 skill-dev 增量模式（优化已有 skill）的四个可迁移机制：

1. **validation-gated edits**：每次编辑只有**严格提升 held-out 验证分数**才被接受，否则回滚——不是「读起来有道理就写进去」。
2. **负反馈记忆（rejected-edit buffer）**：被拒绝的编辑进缓冲区，优化器以后不再重复提出同一失败修改。
3. **编辑预算（textual learning rate）**：控制每次改动的幅度，避免一次性大改。
4. **反面教材**：一个「读起来有道理」的未验证改写，把 GPT-5.5 在 SpreadsheetBench 的准确率从 **41.8% 打到 41.1%**——看起来对、实则更差。

实证：52/52（模型×基准×harness）单元格 best or tied，beat 人类、one-shot LLM、Trace2Skill、TextGrad、GEPA、EvoSkill；在 GPT-5.5 上 no-skill 准确率 +23.5（direct chat）/ +24.8（Codex）/ +19.1（Claude Code）。

---

## 三、darwin-skill 2.0（工程落地）— github.com/xigua0626/darwin-skill-public

**花叔（alchaincyf）**，MIT，2026-05-28 更新，吸收上面两篇论文的结构性升级。定位「像训练模型一样优化 Skill」，一个只能向前转的棘轮。体量小（3★）但方法论完整，是「论文 → 可执行 skill」的最佳参照。

- **9 维评估**：8 维基础 + SkillLens 三个新维度（失败模式编码 / 可执行具体性 / 高风险行动黑名单）。
- **双重评估**：结构评分（静态分析）+ 效果验证（跑测试看输出）。「实测表现权重最高，写得再漂亮跑不出效果就是零」。
- **棘轮机制**：分数只升不降，每轮要么改进要么干净回滚（用 `git revert`，禁 `git reset --hard`）。
- **独立评分**：评分用子 agent，每轮 2 个独立评委，下一轮换全新评委（防锚定）；禁「同一个 AI 又改又评」（SkillLens 实证 46.4%）。
- **早停**：单轮涨幅 < 1 分停手，防凑分堆冗余；干跑比例 > 30% 告警。
- **human-in-the-loop 三层守关**：基线评估、单维度优化、回归测试三处强制暂停等用户确认——「Skill 的好坏比 validation loss 更微妙，关键阶段让人做最终判断」。这是它区别于 SkillOpt 全自动的核心。

---

## 四、对 skill-dev 的映射（本次优化吸收了什么）

| 来源洞见 | skill-dev 落到哪 |
|---|---|
| 单 LLM 评委 46.4% 不可信 | Phase 4「执行稳」补评委铁律（paired 同-judge + 奇数多数决 + 绝对分数只做 triage） |
| 读起来好 ≠ 实际好（负迁移） | 反模式黑名单新增条目 |
| 失败模式编码 / 可执行具体性 / 高风险黑名单 | Phase 2 形式匹配 + skill-templates 正面配方 + skill_check.py 新增 WARN（模糊词、保留字） |
| validation-gated + 负反馈记忆 | Phase 0 增量模式补「优化不越改越差」工序 |
| 同一 AI 又改又评 | 反模式黑名单新增条目（并进 checklists 清单 C） |

## 五、来源与时效

- SkillLens 论文：https://arxiv.org/abs/2605.23899 ｜ 项目页 https://microsoft.github.io/SkillLens ｜ 代码 github.com/microsoft/SkillLens（★★★）
- SkillOpt 论文：https://arxiv.org/abs/2605.23904 ｜ 代码 github.com/microsoft/SkillOpt（★★★）
- darwin-skill：https://github.com/xigua0626/darwin-skill-public（★★★）
- 二手评述：ima.qq.com 知识库《达尔文.skill》（★★）、钛媒体《微软SkillOpt把智能体技能变成了可训练参数》（★★）

失效条件：论文被后续工作推翻、或三源仓库停更超 6 个月时，复核本文件的数字（46.4% / 73.8% / 52/52 / +1.55pp）。

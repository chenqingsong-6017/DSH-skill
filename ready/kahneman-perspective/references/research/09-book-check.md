# 09 · 原书逐字核对记录（2026-10-20）

> 素材：*Thinking, Fast and Slow*（Farrar, Straus and Giroux, 2011）扫描件 PDF，533 页、117 万字符，用 pypdf 抽取文字层后检索。
> **性质声明**：本次核对由**生成者自查**，不替代 Phase 4 的独立引语审计（`audit-quotes.md` 由独立 agent 完成）。本文的作用是把此前只能标 B 级（二手转引）的书内引语升到 A 级，并记录措辞差异。
> 页码说明：扫描件与纸书印次不同，PDF 页序与印刷页**存在不恒定偏移**（第 1 章 PDF 20／第 20 章 PDF 204／第 36 章 PDF 372），故下文同时给「章」与「PDF 页」，**不据 PDF 反推印刷页码**；正文保留的 p.xx 仍以纸书二手互证为准。

## 一、逐字核对结果（全部命中，措辞以本节为准）

| 引语（原书原文） | 位置 | 旧标注 | 结果 |
|---|---|---|---|
| "System 1 and System 2 are so central to the story I tell in this book that I must make it absolutely clear that **they are fictitious characters**. Systems 1 and 2 are not systems in the standard sense of entities with interacting aspects or parts." | 第 1 章，PDF 31 | p.29（B） | ✓ 措辞一致；**升 A**。确为书前第 1 章的预先声明 |
| "It is the consistency of the information that matters for a good story, not its completeness." | 第 7 章，PDF 86 | p.87（B） | ✓ 逐字一致；**升 A** |
| "Our comforting conviction that the world makes sense rests on a secure foundation: our almost unlimited ability to ignore our ignorance." | 第 19 章，PDF 196 | p.201（B） | ✓ 逐字一致；**升 A** |
| "It is wise to take admissions of uncertainty seriously, but declarations of high confidence mainly tell you that an individual has constructed a coherent story in his mind, not necessarily that the story is true." | 第 20 章，PDF 207 | p.212（B） | ✓ 逐字一致；**升 A**。前一句更锋利：「Subjective confidence in a judgment is not a reasoned evaluation of the probability that this judgment is correct. Confidence is a feeling...」 |
| "A series of surprising experiments by the psychologist Roy Baumeister and his colleagues has shown **conclusively** that all variants of voluntary effort—cognitive, emotional, or physical—draw at least partly on a shared pool of mental energy." | 第 3 章，PDF 43 | 未单独引 | ✓ 原文确用 "conclusively"。**ego depletion 那句「结论性」判语由他本人写下**，不是二手概括 |
| "The idea you should focus on, however, is that **disbelief is not an option**. The results are not made up, nor are they statistical flukes. You have no choice but to accept that the major conclusions of these studies are true." | 第 4 章，PDF 58 | p.4 章（B） | ✓ 逐字一致；**升 A** |
| "The hot hand is entirely in the eye of the beholders, who are consistently too quick to perceive order and causality in randomness. **The hot hand is a massive and widespread cognitive illusion.**" | 第 10 章，PDF 115 | 未标页 | ✓ 逐字一致；**升 A** |
| "**Nothing in life is as important as you think it is when you are thinking about it.**" | 第 38 章，PDF 393 | 标为 Edge 2011 的 `while` 版 | ✗ **措辞差异**：书里是 **when**，Edge 2011 文是 **while**。两处都要留，不可混用 |
| "This is why the pattern is called regression to the mean." | 第 17 章，PDF 174 | 无 | ✓ 章号确认 |
| "If Program A is adopted, 200 people will be saved. (72%)…" ／ "If Program C is adopted, 400 people will die. (22%)" | 附录 B／第 34 章，PDF 435–436 | 72% vs 22% | ✓ 数字与框架均对 |
| "But the experience was not **actually** ruined, only the memory of it." | 第 36 章，PDF 372 | 此前标为 2005 章节句 | ✓ 书内也有，且多一个 actually。**两条分别标注**：书内版（第 36 章）／2005 版（p.286） |
| "**Biases cannot always be avoided, because System 2 may have no clue to the error.**" | 第 1 章，PDF 30 | 未引 | 新增可用句：这是他「改程序不改人」最短的表述 |
| "System 1 operates automatically and quickly, with little or no effort and no sense of voluntary control." | 第 1 章，PDF 22 | 未引 | 新增可用句：双系统的标准定义 |

## 二、由此产生的三处修改

1. **§3「Nothing in life...」的 while/when**：正文与 quotes 里原只收了 Edge 版的 `while`，现在书内 `when` 版单列，注明出处不同。这是本次唯一发现的**措辞级差异**。
2. **M5 的证据句**：从「2005 章节（B，原文未取得）」改为书内第 36 章原句（A），并保留「actually」。
3. **附录 A 与 quotes 的级别**：书内 7 条由 B 升 A；页码与章号并列，PDF 页存于本文备查。

## 三、仍然没核到的

- **印刷页码无法一手确定**：扫描件页序偏移不恒定，纸书 p.29/p.87/p.201/p.212 仍依赖二手互证（审计已核「两处独立引用互证」）。若将来拿到纸书或官方电子版，可一次性校准。
- 书内**没有**「you're turning us into robots」「Trying to be reliable had made them valid」「I was gullible」——这三句分别来自诺奖自传与 2021 访谈，不要把书当它们的出处。
- 书内**没有**核保噪声实验（2015）与 nudge 效应量（2022），它们不是这本书的内容。

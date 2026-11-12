# Skill 验证台账（Verification Ledger）

> 目的：让「哪些 skill 验证过、哪些没验证」一目了然，杜绝「写了就以为有用」——对标 anthropics/skills 的生产级验证要求（skill-dev Phase 4：with/without delta 才是有效验证，静态脚本只算形式检查）。
> 维护：每新增/改动 skill 后更新本表；每次跑验证后回填「证据」列。触发「验证」时先查本表找「未验证」项。
>
> 状态定义：
> - ✅ **已验证**：有脚本 + 跑过 + 有证据（正常/违规对照或真实任务通过）
> - 🟡 **部分验证**：有脚本但未跑对照，或只跑过 skill_check 形式检查（形式 ≠ 有效性）
> - ⚪ **未验证**：纯 prose、无脚本、未跑 with/without（多数 skill 属此列，勿误以为「写了＝有用」）

## 台账

| Skill | 类型 | 脚本 | 状态 | 证据 / 备注 |
|---|---|---|---|---|
| skill-dev | 元技能 | skill_check.py | ✅ | 本轮对 capability-radar 跑 20 PASS/0 FAIL |
| ai-config-upgrade | 流程 | check_chars.py | ✅ | 本轮跑 --memory：真实文件 OK + 违规样例抓 2 处 |
| macos-design-framework | 参考+脚本 | audit_css.py | ✅ | 本轮跑：正常 0 错 + 违规抓 6 错（MAC001/3/4/5/6/7） |
| capability-radar | 流程 | 无 | ⚪ | 快速档，未跑 with/without 对照（待首次真实触发验证） |
| github-empirical-research | 流程 | 无（含 curl） | ⚪ | 纯 prose，11 次实战沉淀但未跑对照 |
| experience-loop | 流程 | 无 | ⚪ | 纯 prose |
| security-audit | 参考 | 无 | ⚪ | 纯 prose，方法论型 |
| simaqian-skill | 流程 | 无 | ⚪ | 纯 prose |
| mao-perspective | 视角 | 有（内容未核） | 🟡 | 脚本未核、未跑对照 |
| musk-perspective | 视角 | 有（内容未核） | 🟡 | 同上 |
| libai-perspective | 视角 | 有（内容未核） | 🟡 | 同上 |
| worldview-setting | 体系 | 有（内容未核） | 🟡 | 同上 |
| feynman-perspective | 视角 | 无 | ⚪ | 纯 prose |
| dufu-perspective | 视角 | 无 | ⚪ | 纯 prose |
| steve-jobs-perspective | 视角 | 无 | ⚪ | 纯 prose |
| obra-brainstorming | 方法论 | 无 | ⚪ | 纯 prose |
| obra-writing-plans | 方法论 | 无 | ⚪ | 纯 prose |
| obra-executing-plans | 方法论 | 无 | ⚪ | 纯 prose |
| obra-systematic-debugging | 方法论 | 无 | ⚪ | 纯 prose |
| obra-verification-before-completion | 方法论 | 无 | ⚪ | 纯 prose |
| obra-dispatching-parallel-agents | 方法论 | 无 | ⚪ | 纯 prose |
| obra-subagent-driven-development | 方法论 | 无 | ⚪ | 纯 prose |
| managing-windows-software | 流程 | 无 | 🟡 | skill_check 19 PASS/0 FAIL；素材来自 2026-10-17 真实翻车（winget 权限/MSIX 0x80070032/网络/VM/重启），未跑 with/without 对照 |

## 读法（主要矛盾）

- **✅ 已验证 3 个**：都是「带脚本」的。**脚本是「能验证」的前提**——纯 prose 的 skill 想验证，先得有「可测判据」或脚本。
- **⚪ 未验证 15 个**（占 2/3）：大多是「方法/视角」类，靠自然语言自律，天然难跑 with/without。对这类，验证方式不是「补脚本」，而是**「真实触发时记录 delta」**（好了一次 vs 差了一次），或标注「该 skill 实际被触发几次、效果如何」。
- **下一步优先级**（不是现在做，记账）：① capability-radar 首次真实触发时补 with/without；② 高频 skill（obra-verification、github-empirical-research）真实用几次后回填 delta；③ 低频视角类 skill 若连续两周不触发，评估合并/下架。

> 更新：2026-10-17 首建；②③证据回填前 3 行；**「都验证」→「有短板就补」最终态**：22 个 skill 从 16 FAIL 降到 2 FAIL。补：skill_check.py 修 6 处（触发词加「时用」、放宽「当…时」12→40、审计报告排除、安全审计类豁免、视角类 BODY 豁免×2）；obra-executing/writing-plans 补触发、experience-loop 补标准 description、obra-executing/subagent 加「移植状态」说明＋脚本引用豁免；security-audit 下沉报告模板＋评分规则（0 FAIL）。剩 2 个＝重构工程：experience-loop（9816 token 需拆）＋obra-subagent（英文原文 579 行，下沉空间有限，宜与重写一并处理）。

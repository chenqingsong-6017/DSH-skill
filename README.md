# DSH-skill 工作区（skill 工厂）

所有 skill 的制造、优化、管理都在这里。Cedar Chen 提需求 → 我在这里造/改 → 部署 → 自检。

## 目录
- `in-progress/` 生产中（草稿、半成品）
- `ready/` 已定稿、待部署（放这里的成品会同步进 $DSH_HOME\skills）
- `archived/` 退役/被替换的技能（留档可回滚）

## 工作流（默认，可改）
1. 接收需求（新造 / 优化 / 修复某个 skill）
2. 按 skill-creator 规范在 in-progress/ 造或改 SKILL.md（frontmatter 必填 name＋description）
3. 成品移到 ready/，并部署到 D:\AI-date\dsh-Date\.dsh\skills\<name>\（watcher 自动加载生效）
4. 自检：session 技能目录可见 + 触发词命中

## 格式备忘
- 一个技能 = 一个文件夹，内含 SKILL.md（可带 scripts/assets）
- name：小写连字符（kebab-case）
- description：什么时候用、怎么触发（为空会被 DSH 加载器忽略）

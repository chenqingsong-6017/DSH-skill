---
name: macos-design-framework
description: 蒸馏自 Apple 官方 HIG 与 macOS 27 Golden Gate（Liquid Glass 收敛版）的设计语言框架：5 个设计心智模型、10 条决策启发式、设计令牌（配色/字体/间距/层级/材质/阴影/动效）、15 个可复制组件配方、流派对比、反模式对照表与静态自检脚本，并附带可运行的实证样例与起步骨架。当用户要「用 macOS 的设计语言做界面」「做苹果风格 / 毛玻璃 / Liquid Glass 质感」「按苹果审美把界面改高级 / 说不出哪里廉价」「写一份桌面端设计规范」「做 Electron/Tauri/桌面 Web 工具的 UI」时使用。不在一般网页美化、非苹果视觉风格、iOS 原生开发细节、品牌营销页上自动触发。
---

# macOS 设计语言框架（macOS Design Framework）v1.1

> 本 Skill 由「女娲 · Skill造人术」主题蒸馏流程生成（主题 Skill 变体）：https://github.com/alchaincyf/nuwa-skill
> 方法论：花叔 ｜ 实例化：xxx × 小管家（2026-10-09，v1.1 优化 2026-10-12）

把 Apple macOS 的设计语言蒸馏成**可直接施工**的界面框架：心智模型 → 决策启发式 → 设计令牌 → 组件配方 → 机器自检。
**基线：macOS 27 Golden Gate**（2026 秋，对 Liquid Glass 的收敛修正版）；**调研时间 2026-10-09**。
素材：Apple 官方 HIG（材质/颜色/字体/动效/布局）+ 官方 Liquid Glass 采纳文档 + macOS 26/27 官方说明与权威报道。原始调研见 `references/research/`。

## 0. 路由地图（按需取用，不必全读）

| 你要做的事 | 直接看这一节 |
|---|---|
| 从零做一个界面 | 框架概览 → 取令牌 → 组件速查 → 实现协议 |
| 改一个现有界面 | 反模式对照表（定位病灶）→ 组件速查 → 跑自检脚本 |
| 只要一个组件抄 | `references/components.css` 对应编号 |
| 写设计规范文档 | 心智模型 + 决策启发式 + 表达 DNA 表 |
| 起一个新项目 | `assets/starter.html`（复制即用） |
| 验收 / 交接 | 实现协议 Step 4 + `scripts/audit_css.py` |
| 找依据 / 查出处 | `references/research/01~04` |

**文件清单**：`SKILL.md`（本文件）｜`references/tokens.css`（令牌）｜`references/components.css`（15 个组件配方）｜`assets/starter.html`（最小骨架）｜`assets/components-gallery.html`（组件画廊，双主题验收证据）｜`assets/macos-desktop-demo.html`（完整实证样例）｜`scripts/audit_css.py`（静态自检）｜`references/research/`（调研原文）。

## 何时使用

- 「用 macOS 的设计语言做 XX」「苹果风格」「仿 macOS」「Liquid Glass / 玻璃质感 / 毛玻璃」
- 「按苹果的审美把界面改高级」「说不出哪里显得廉价」「想让它更精致」
- Electron / Tauri / 桌面 Web 工具 / 编辑器类产品的 UI 与设计规范
- **不适用**：一般网页美化、非苹果视觉风格、游戏 UI、品牌营销页、iOS/watchOS 原生细节、图标与插画创作。

## 框架概览（怎么用）

1. **选流派**（见「流派对比」表，默认 Golden Gate 27 收敛版）
2. **取令牌**：复制 `references/tokens.css`，`<html data-theme="light|dark">` 切主题
3. **抄组件**：`references/components.css` 里 15 个配方按需取
4. **按心智模型与启发式**排版、上材质、加动效
5. **对照反模式对照表**自查，再跑 `scripts/audit_css.py`
6. 需要整体参照时打开 `assets/macos-desktop-demo.html`；单组件长什么样先看 `assets/components-gallery.html`（双主题）

## 设计心智模型（5 个）

### M1 内容优先，控件退后（Deference）
界面是内容的仆人：控件浮在内容之上、视觉上"退后"，让内容保持最高对比。
- 证据：HIG 布局篇「用 Liquid Glass 与 scroll edge effect 抬高控件，而不是给控件铺实色背景」；材质篇「Liquid Glass 只用于功能层，不要用在内容层」。
- 应用：窗口正文不透明；玻璃只给菜单栏/Dock/面板/工具栏；控件文字用最高层级颜色。
- 失效条件：内容稀疏的工具界面，过度"退后"会显空洞——用留白与图标补齐节奏，别加装饰。
- **验证判据**：窗口内放一段文字，玻璃层（菜单栏/工具栏）浮于其上但不压低文字对比＝达标；内容区出现半透明背景或文字被玻璃吃掉对比＝违反。

### M2 材质即层级（Depth via Materials）
层级靠"材质 + 阴影 + 明暗"表达，而不是边框和重颜色。
- 证据：HIG 材质篇（材质在前后景间建立深度层级；标准材质四级厚度；regular/clear 两变体）。
- 应用：浮起 = 半透明底 + 背景模糊 + 顶部高光边 + 多层阴影；下沉 = 实色底；明亮内容上的 clear 玻璃加 35% 暗化层（`.glass-dim`）。
- 失效条件：低性能设备玻璃层过多会掉帧；阴影堆多了会显"脏"。
- **验证判据**：浮起元素有 ≥2 层阴影且含 0.5px 描边＝达标；单条 `box-shadow:0 2px 4px black`＝违反（脚本 MAC003）。

### M3 同心与统一（Concentricity & Consistency）
圆角与容器同心；同类元素只用一套参数。
- 证据：Apple Liquid Glass 文档（ConcentricRectangle：嵌套圆角同心）；27 的核心修正就是统一窗口圆角与工具栏。
- 应用：内圆角 = 外圆角 − 内边距；一套圆角阶梯（窗口 11 / 面板 8 / 控件 7 / 列表行 5）；图标 squircle 22.4%。
- 失效条件：圆形/异形容器内需单独推导，生搬会怪。
- **验证判据**：容器内子元素圆角 ≈ 父圆角 − 内边距＝达标；同一页出现 4/8/12px 混搭圆角＝违反。

### M4 克制而有目的的动效（Purposeful Motion）
动效只做三件事：反馈、空间关系、注意引导；短、准、可取消。
- 证据：HIG 动效篇（高频交互不加动效；不让用户等动画；必须支持减弱动态效果）。
- 应用：按压 100ms / 悬停 140ms / 浮层 220ms / 窗口 320ms / 最小化 420ms（上限）；只动 transform/opacity。
- 失效条件：展示型场景过度克制会显死板——可把入场调到 320–420ms 并允许一次轻微回弹。
- **验证判据**：悬停/按压 ≤160ms、窗口 ≤420ms，且 `@media (prefers-reduced-motion)` 下有降级＝达标；任一动效 >500ms 或线性位移缓动＝违反（脚本 MAC004/005）。

### M5 可读性优先于效果（Legibility First）
"炫"与"读"冲突时，永远站"读"。
- 证据：26 的透明材质因可读性被大规模批评；27 专门做扩散增强、高光/边缘调优与全局透明度滑块。
- 应用：玻璃上的文字永远用高对比层级；复杂背景先测对比度；必须提供"降低透明度"回退（令牌已内置）。
- 失效条件：与"视觉冲击优先"的品牌页目标冲突——那不属于本框架范围。
- **验证判据**：玻璃上文字用 `--label-1` 且实测对比 ≥4.5:1＝达标；明亮玻璃上放 `--label-3` 灰字＝违反（脚本 MAC002/003 不查对比，需人工/工具实测）。

## 决策启发式（10 条）

> 每条附「验证判据」——看到什么算达标、看到什么算违反，让框架可检验。

1. 玻璃想用在**内容层** → 停，换不透明底（内容/控件必须分层）。
   → 判据：内容区 `background` 为 `--window-bg`/`--content-bg`（不透明）＝达标；内容区出现 `backdrop-filter` 或半透明底色＝违反。
2. 控件浮在**明亮/花哨背景**上 → 提高材质不透明度（regular 思路）或加 `.glass-dim` 暗化层，再过对比检查。
   → 判据：玻璃上文字用 `--label-1` 且实测对比 ≥4.5:1＝达标；亮底上放 `--label-3` 灰字＝违反。
3. 文字在材质之上 → 用 `--label-1/2` 前两级；次级信息用透明度表达，不硬编码灰色。
   → 判据：全文无 `color:#888` 之类的硬编码灰＝达标；出现＝违反。
4. **高频交互** → 不加动效或 ≤160ms。
   → 判据：hover/active 的 transition ≤160ms＝达标；≥200ms＝违反。
5. 需要"浮起感" → 三层阴影（0.5px 描边 + 中距 + 远距），禁止单层重阴影。
   → 判据：`box-shadow` 逗号分隔 ≥2 层且含 0.5px 描边＝达标；单层 `0 2px 4px black`＝违反（脚本 MAC003）。
6. 元素嵌套在容器内 → 内圆角 = 外圆角 − 内边距。
   → 判据：子圆角 ≈ 父圆角 − 内边距＝达标；内圆角 > 外圆角或乱填＝违反。
7. 要"留白" → 用 8pt 网格间距（`--sp-*`）表达分组，而不是堆分隔线。
   → 判据：分组间距取自 `--sp-*`（4 的倍数）＝达标；出现 `margin:13px` 之类非网格值＝违反。
8. 一个颜色要担两种含义 → 拆成语义色；强调色只给交互与选中态。
   → 判据：搜索 "accent" 在 CSS 里只出现在交互/选中选择器＝达标；出现在标题/背景＝违反。
9. 支持深色模式 → 深色不是反相：降饱和、提对比、重新取值，双主题都过检查。
   → 判据：`[data-theme="dark"]` 块独立取值（非 `filter:invert`）＝达标；`.dark{filter:invert(1)}`＝违反。
10. 性能吃紧/长列表 → 同屏玻璃层 ≤5；动画只用 transform/opacity；备好无模糊降级。
    → 判据：页面里 `backdrop-filter` 声明 ≤5（脚本 MAC008）且动效只碰 transform/opacity＝达标；否则＝违反。

## 表达 DNA（设计令牌）

完整可复制版本：`references/tokens.css`。要点：

| 维度 | 规则 | 关键值 |
|---|---|---|
| 配色 | 语义色 + 双主题令牌化；强调色单一来源 | `--accent:#007aff`（dark `#0a84ff`）；label 三级 |
| 字体 | 系统字体栈（Mac 落真 SF）；基准 13px；禁 ≤300 字重 | `-apple-system, Inter, PingFang SC, Microsoft YaHei` |
| 字号 | 阶梯化，下限 10px | 10 / 11 / **13** / 15 / 17 / 22px |
| 间距 | 8pt 网格；留白代替分隔线 | `--sp-1..7` = 4/8/12/16/24/32/48 |
| 层级 | 浮层 > 玻璃 > 工具栏 > 内容 | `--z-popover:1000`、`--z-modal:1100`、`--z-toast:1300` |
| 图标 | 统一光学重量与光源；squircle 近似；勿用官方素材 | `border-radius:22.4%` |
| 材质 | 玻璃三件套：半透明底 + blur+saturate + 高光边 | 菜单栏 30/190%、面板 34–44/200%、Dock 26/180% |
| 阴影 | 描边层 + 中距 + 远距，多层柔和 | `--shadow-window` / `--shadow-menu` |
| 动效 | 时长阶梯 + 两条曲线 + Reduce Motion | 100/140/220/320/380/420ms；快出慢入与 1.18 回弹 |
| 焦点 | 键盘可达必配，鼠标点击不出现 | `:focus-visible` + `--focus-ring` |
| 交通灯 | 12px、间距 8px、悬停显符号、失焦全灰 | `#FF6159 / #FEBD2E / #28C941` |

## 流派对比（先选流派再动手）

| 流派 | 特征 | 何时选 | 实现差异 |
|---|---|---|---|
| 经典期（Big Sur–Sequoia） | 不透明窗口 + 灰工具栏；玻璃仅在菜单栏/侧栏/面板 | 保守项目、低性能环境、信息密度高的工具 | 玻璃层最少、无折射感；最稳 |
| Tahoe 26（Liquid Glass 初版） | 强透明、悬浮侧栏、高饱和图标 | 要"最新 macOS 观感"且能承担可读性调试 | 透明度拉满后**必须**补对比与暗化层，否则重演 26 的差评坑 |
| **Golden Gate 27（默认推荐）** | 收敛版：透明度可控、贴边侧栏、统一圆角、可读性优先 | 绝大多数场景 | 以本框架令牌为准，玻璃档位取中 |

**切换流派 = 改 3 个变量**（不必重写样式）：

```css
/* 经典期：玻璃收进侧栏，工具栏改实色 */
:root{ --glass-toolbar:var(--sidebar-bg); --blur-toolbar:none; --radius-window:10px; }
/* Tahoe 26：加透明度 + 悬浮侧栏（记得补 .glass-dim 与对比检查） */
:root{ --glass-panel:rgba(250,250,252,.55); --blur-panel:blur(44px) saturate(210%); }
.sidebar{ /* 换成 .sidebar.floating，见 components.css §4 */ }
```

## 组件速查（`references/components.css`）

| # | 组件 | 关键约束 |
|---|---|---|
| 1 | 窗口骨架 | 内容层不透明；`overflow:hidden` 保同心；开启动画后加 `.opened` 防重播 |
| 2 | 标题栏 + 交通灯 | 失焦即降层级；符号仅悬停显示 |
| 3 | 工具栏 | 功能层可用玻璃；高度 38px |
| 4 | 侧栏 | 27 贴边（默认）／26 悬浮（`.floating`）二选一 |
| 5 | 列表行与选中 | 选中 `--accent`；窗口失焦时改中性 `--selection-fill` |
| 6 | 按钮 | 默认 / `--accent` / 玻璃 / 禁用四态；按压 `scale(.97)` |
| 7 | 输入框 | 聚焦环必配；占位符用 `--label-3` |
| 8 | 开关 | 38×22，滑块 18，回弹曲线 |
| 9 | 分段控件 | 选中片抬到 `--window-bg` + 微阴影 |
| 10 | 菜单 | 玻璃 + `z-popover`；禁用项 hover 不变色 |
| 11 | 弹窗 | 遮罩 22% 黑；`z-modal` |
| 12 | 通知 | 右上角堆叠；`z-toast` |
| 13 | 分隔线 | 能省则省，优先 `--sp-*` 留白 |
| 14 | 滚动边缘 | 滚到边界才出现分隔线/渐隐（二选一，别同时上） |
| 15 | 内容区 | 13px / 行高 1.5 / `--z-content` |

## 实现协议（回答工作流）

**Step 1 分类**：新建界面 → 完整 5 步；改版 → 先跑反模式对照表定位病灶；单组件 → 取令牌 + 对应配方；规范文档 → 用心智模型 + 启发式成文。
**Step 2 定位**：载体（Web/原生）；流派（默认 27 收敛版）；主题（默认深浅双套）。
**Step 3 实现顺序**：令牌 → 布局骨架（先留白排版式，再放控件）→ 材质（玻璃只上功能层）→ 组件配方 → 动效（最后加，按阶梯）→ 深浅双模式走查。
**Step 4 验收**：先过下面 10 项，再跑机器自检——

```bash
# 扫描 .css/.scss/.less 全量；.html/.htm 仅查 <style> 块与内联 style="..."（跳过 <script>）
python scripts/audit_css.py <你的样式目录或文件>
# 反向样例（故意违规，预期报错）：style="color:#333;font-size:9px;transition:all 900ms"
```

- [ ] 所有颜色走变量，无散落硬编码 hex（MAC001/002）
- [ ] 玻璃只在功能层；内容层不透明
- [ ] 每个透明表面做过文字对比检查（复杂背景实测）
- [ ] 动效 ≤420ms、无线性位移缓动、支持 Reduce Motion（MAC004/005）
- [ ] 圆角同心；同类组件参数一致
- [ ] 阴影多层柔和、无纯黑单层（MAC003）
- [ ] 强调色只用于交互与选中
- [ ] 无 ≤300 字重；正文 ≥13px、最小 ≥10px（MAC006/007）
- [ ] 深色模式独立配过色（非反相）
- [ ] 键盘焦点态可见（`:focus-visible`）

## 反模式对照表（症状 → 为什么 → 怎么修）

| # | 症状 | 为什么错 | 修法 |
|---|---|---|---|
| 1 | 大面积纯色卡片堆层级 | 层级应由材质+阴影承担，纯色会把界面压平或切碎 | 卡片改 `--window-bg` + `--shadow-floating`，层级交给阴影 |
| 2 | 纯黑 `#000` / 纯白 `#fff` 当正文或背景 | 破坏材质通透感，暗色下刺眼 | 改 `--label-1` / `--window-bg` |
| 3 | 到处毛玻璃 | 可读性崩溃 + 掉帧 | 只留功能层；同屏 ≤5 层（MAC008） |
| 4 | 单层硬阴影 `0 2px 4px black` | 显"廉价"，无光线逻辑 | 换 `--shadow-window` 三层 |
| 5 | 圆角混搭、内圆角不同心 | 破坏 M3，一眼假 | 内圆角 = 外圆角 − 内边距 |
| 6 | 动效 >0.5s、线性缓动、无意义弹跳 | 用户在等动画 | 按阶梯取值，`--ease-out` / `--ease-spring` |
| 7 | 强调色滥用（标题/装饰/背景全染蓝） | 选中态失去信号价值 | 强调色只给交互与选中 |
| 8 | 深色模式简单反相 | 反相后对比与饱和度都错 | 双主题各自取值，两套都过检查 |
| 9 | 图标风格混杂（扁平+拟物+emoji） | 光学重量与光源不统一 | 统一 stroke 粗细与光源方向 |
| 10 | 明亮玻璃上放低对比灰字 | 26 的最大差评来源 | 提 `--label-1` 或加 `.glass-dim` 暗化层 |
| 11 | 分隔线当分组唯一手段 | 视觉噪音，显拥挤 | 用 `--sp-*` 留白分组 |
| 12 | 只做浅色，深色"以后再说" | 后期补必返工 | 一开始就令牌化双主题 |

## 输出契约（做完必须交付什么）

1. **令牌文件**（或一段 `:root` 变量）：颜色/间距/字号/层级/材质/阴影/动效齐全，深浅双套。
2. **改好的界面/组件代码**：所有数值来自令牌，无散落硬编码。
3. **一段说明**：选了哪个流派、为什么；哪些地方走了取舍（尤其可读性 vs 效果）。
4. **自检结果**：贴出 `audit_css.py` 的输出（0 错误），或逐条说明未过项的原因。
5. 需要时给出**实证页面或截图**（参照 `assets/starter.html` 的双主题切换写法）。

## 回答模板（few-shot）

用户说「按苹果审美改这个界面」时，按这个结构答，别上来就贴代码：

1. **一句话定性**：现在的界面主要问题是 ______（对上反模式表编号）。
2. **流派与基线**：默认 Golden Gate 27；若要更接近 26 或经典期，说明差异（可改）。
3. **改动清单**：按「令牌 → 布局 → 材质 → 动效」分组，每条写清「改什么 / 为什么 / 换成什么」。
4. **代码**：令牌块 + 组件块，直接可用。
5. **自检**：跑脚本，贴结果。
6. **可改项**：明确标出 2–3 个可选项（玻璃强度、圆角档位、是否悬浮侧栏）。

### 真实样例：把一个"廉价后台卡片"改到 macOS 质感

**原界面（问题定位）**：一张 `#ffffff` 卡片浮在灰底上，靠 `box-shadow:0 2px 4px #000` 撑立体感，标题用 `#333`，按钮全是蓝色填充，hover 无反馈。对应反模式 **#2 纯黑背景、#4 单层硬阴影、#7 强调色滥用、#6 动效缺失**。

**改动清单**
- 令牌：引入 `tokens.css`；卡片底色改 `--window-bg`，标题改 `--label-1`，正文改 `--label-2`。
- 材质：卡片阴影换 `--shadow-floating`（描边 + 中距 + 远距三层）；顶部加一条玻璃菜单栏/工具栏时再说。
- 组件：按钮拆成 `.btn`（默认）+ `.btn-accent`（仅主操作），其余用默认态；删除所有蓝色装饰。
- 动效：hover 加 `transition:background var(--dur-hover)`；卡片入场上 `win-open` 320ms。

**代码（节选）**
```css
.card{ background:var(--window-bg); border-radius:var(--radius-panel); box-shadow:var(--shadow-floating); }
.card h3{ color:var(--label-1); } .card p{ color:var(--label-2); }
.btn-accent{ background:var(--accent); color:var(--label-on-accent); }
.btn{ transition:background var(--dur-hover) var(--ease-out); }
```

**自检**
```
python scripts/audit_css.py styles.css
[通过] 错误 0 · 警告 0 · 提示 0
```

**可改项**：① 卡片是否要玻璃化（功能层才用，内容卡片不建议）；② 圆角 8px 还是统一 11px；③ 是否补深色主题（默认双主题令牌已就绪，加 `data-theme` 即可）。

> 注意：这是"改版"粒度。若用户只是要单组件，直接给 `components.css` 对应编号即可，不必走全套流程。

## 实证样例与起步骨架

- `assets/starter.html` — **最小骨架**：菜单栏 + 窗口 + 侧栏 + 工具栏 + 内容列表 + 主题切换 + 降低透明度开关，约 120 行，相对路径引入令牌与配方，零依赖双击即开。新项目从它复制。
- `assets/components-gallery.html` — **组件画廊（验收证据）**：把 `components.css` 的 15 个组件全部渲染出来，带浅/深主题切换。用途有二——① 你自己改组件后截图核对有没有破相；② 给用户/同事当视觉参考。
- `assets/macos-desktop-demo.html` — **完整实证样例**：菜单栏 / 窗口与交通灯 / Dock 高斯放大 / 聚焦搜索 / 控制中心 / 深浅主题 / 访达·备忘录·计算器·终端等 7 个应用。URL 参数：`?theme=dark&wp=2&apps=finder,notes&spot=1`。
- 工程细节与踩坑：`references/research/04-implementation-notes.md`。

## 诚实边界

1. **SF Pro 与 SF Symbols 未授权分发**：用系统字体栈 + Inter 近似、手绘 SVG 近似图标；商用请自行解决授权。
2. **px 级材质参数为工程近似**：Apple 未公开 blur 半径与透明度具体值；本框架数值为对齐官方观感的实测近似，非官方规格。
3. **时效**：调研于 2026-10-09（v1.1 优化 2026-10-12，v1.2 组件画廊与可测判据 2026-10-15），基线 macOS 27。HIG 明确"色值仅作设计参考"，超 6 个月请复查 Apple 官方页面。
4. **适用范围**：仅 macOS 桌面语境（Web 复刻验证于 Chromium/Edge，Safari 需 `-webkit-backdrop-filter` 前缀，已内置）；不覆盖 iOS/watchOS/visionOS；不适用于游戏与沉浸式媒体。
5. **能力边界**：能保证"像 macOS 的质感与规范"，不保证"与最新 macOS 逐像素一致"——那需要真机比对。
6. **脚本边界**：`audit_css.py` 只做静态文本检查，不校验实际渲染与真实对比度；对比度、真机观感仍需人工/工具实测（脚本误报可用 `/* audit:ignore MAC00X 原因 */` 行内豁免）。

## 调研来源

**一手（Apple 官方）**
- HIG Materials / Color / Typography / Motion / Layout — `developer.apple.com/design/human-interface-guidelines/*`
- Adopting Liquid Glass — `developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass`
- macOS Tahoe 26 更新说明 — `support.apple.com/122868`

**二手（权威媒体，已交叉验证）**：Cult of Mac（WWDC26 纪要）、MacRumors（macOS 26 roundup）、Gizbot / Showmetech（WWDC26 报道）

**社区工程参考**：tauri-controls（交通灯色值实测）、jonanv traffic-lights gist（交通灯实现）

---
> 本 Skill 由「女娲 · Skill造人术」主题蒸馏流程生成：https://github.com/alchaincyf/nuwa-skill
> 创建者：花叔（方法论）｜ 实例化：xxx（2026-10-09，v1.1 2026-10-12）

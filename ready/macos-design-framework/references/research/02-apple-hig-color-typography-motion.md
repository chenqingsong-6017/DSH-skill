# 调研 02：Apple HIG —— 颜色 / 字体 / 动效（官方一手）

> 来源（抓取于 2026-10-09）：
> - https://developer.apple.com/design/human-interface-guidelines/color
> - https://developer.apple.com/design/human-interface-guidelines/typography
> - https://developer.apple.com/design/human-interface-guidelines/motion
> 可信度：一手（Apple 官方规范原文）。hex 色值为公开广泛引用的设计参考值（官方明确说明"文档色值仅作设计参考，实际值可能随版本浮动，不要硬编码"）。

## 一、颜色

### 核心原则（官方明确）
- 不要硬编码系统色值；用系统/语义色 API（版本间会微调）。
- 每个自定颜色都要有 **light / dark / 增强对比（Increase Contrast）** 变体；即便只发布单一外观也要准备两套色以配合 Liquid Glass 自适应。
- 同一颜色不得表达不同含义；不要只靠颜色传递信息（色觉障碍）；注意文化差异——**示例：涨跌色在中英文环境语义相反（本框架默认中国惯例：红涨绿跌）**。
- Liquid Glass 环境：彩色背景下工具栏/标签栏宜用**单色系外观**或选差异足够的强调色；注意颜色在内容层与控件层的重叠对比。

### 动态语义色（macOS，官方明确清单节选）
`labelColor`(主文本) / `secondaryLabelColor` / `tertiaryLabelColor` / `quaternaryLabelColor`(水印级) / `placeholderTextColor` / `separatorColor` / `windowBackgroundColor` / `textBackgroundColor` / `controlAccentColor`(**用户可换强调色**) / `selectedContentBackgroundColor`(选中态) / `selectedTextBackgroundColor` / `linkColor` / `gridColor` / `headerTextColor` / `disabledControlTextColor` / `shadowColor`。
- 系统色板：red / orange / yellow / green / mint / teal / cyan / blue / indigo / purple / pink / brown + 6 级 gray。
- 强调色（accent）：自 macOS 11 起可自定义按钮、选择高亮与侧栏图标着色；用户系统设置不是"多色"时覆盖 App 自定色（固定色侧栏图标除外）。

## 二、字体排印

### 关键数值（官方明确）
| 平台 | 默认字号 | 最小字号 |
|---|---|---|
| **macOS** | **13 pt** | **10 pt** |
| iOS/iPadOS | 17 pt | 11 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

### 规范（官方明确）
- 系统字体：**SF Pro**（另有 SF Mono、SF Compact、圆体变体）；衬线用 New York。可变字体自动光学尺寸（Text/Display 合一）。
- **避免 Light / Thin / Ultralight 字重**（小字号难读）；推荐 Regular、Medium、Semibold、Bold。
- 文本样式体系（iOS 数值表，可作层级参照）：Large Title 31 / Title1 25 / Title2 19 / Title3 17 / Headline 14 semibold / Body 14 / Callout 13 / Subhead 12 / Footnote 12 / Caption1 11 / Caption2 11。
- macOS 用**动态字体变体**与控件对齐：`menuBarFont` / `titleBarFont` / `controlContentFont` / `toolTipsFont` / `userFont` / `userFixedPitchFont`（等宽正文）。
- 行距：宽栏用宽松行距（loose leading）；≥3 行文本避免紧行距。
- SF Symbols 与字体字重自动对齐——图标与文字并排时权重匹配。

## 三、动效

### 原则（官方明确）
- **有目的地使用动效**：不用"为动而动"；滥用会让人不适。
- **短促、精准**：反馈类动效快而准优于大而慢；不要让人等待动画完成才能操作（可随时取消）。
- **高频交互不加动效**（系统元件自带的微妙反馈已够）。
- 反馈须与手势直觉一致（从顶部滑入的用顶部滑出，不能横向消失）。
- **必须支持 Reduce Motion（减弱动态效果）**；动效不得是传达关键信息的唯一手段。
- Liquid Glass 的动效响应输入方式：触摸强调更强，触控板更收敛。
- visionOS 补充（可迁移的一般经验）：避免持续振荡（约 0.2 Hz 人最敏感）；大物体移动用淡出-淡入过渡减少不适。

## 四、对实现（Web 复刻）的工程映射（本框架转译）
- 全站颜色令牌化：`--label-1/2/3`、`--accent`、`--separator`、`--window-bg`…深浅两套（见 `references/tokens.css`）。
- 字号阶梯：13px 基准（dense UI），标题 17–23px，大标题 26–40px；正文 13–14px；说明 11–12px。禁用 300 以下字重。
- 动效时长阶梯（工程近似，非官方数值）：悬停 100–160ms / 菜单与浮层 160–240ms / 窗口与转场 240–420ms；缓动默认「快出慢入」曲线；禁止线性缓动做位移。
- `@media (prefers-reduced-motion: reduce)` 强制接管：动画/过渡时长压到 0.01ms。

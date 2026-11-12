# 调研 03：Liquid Glass 采纳 + macOS 26→27（Golden Gate）设计语言变更

> 来源（采集于 2026-10-09，已交叉验证）：
> - Apple 官方：https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass
> - Apple 支持页：macOS Tahoe 26 更新说明（support.apple.com/122868）
> - 权威报道：Cult of Mac（WWDC26 纪要）、MacRumors（macOS 26 roundup）、Gizbot / Showmetech（WWDC26）
> 可信度：一手（Apple 官方）+ 二手权威媒体（逐条与官方页面交叉验证）。

## 一、Liquid Glass 采纳要点（官方明确）

- **标准组件自动获得 Liquid Glass**（SwiftUI / UIKit / AppKit 新 SDK 直接生效）；**减少自绘背景**——自定义背景会覆盖/干扰系统材质与 scroll edge effect（重点检查 split view、标签栏、工具栏）。
- **图标**：新的标准化网格 + **分层**（前景/中景/背景）；设计用"实心、填充、互相重叠的半透明形状"；**遮罩、模糊、高光由系统处理**，设计端不要预烘焙效果。浅色/深色/clear/tinted 四种外观变体。
- **控件**：
  - 避免拥挤与堆叠；使用系统标准间距（不要随意覆盖）。
  - 内容从控件下滚动时用 **scroll edge effect** 保持可读性（系统栏自动、自定义栏用 `safeAreaBar` 注册）。
  - **同心圆角（concentricity）**：嵌套元素的圆角应与容器同心——`ConcentricRectangle` / `rect(corners:isUniform:)`。
  - 按钮用 `glass` / `glassProminent` 样式而不是自绘玻璃。
- **窗口与模态**：清理 popover/sheet 的自绘背景；动作表从触发控件处"长出"（origin 锚定）。
- **无障碍**：必须测试 Reduce Transparency / Reduce Motion / Increase Contrast 下的表现。

## 二、macOS 设计语言时间线（核实）

### macOS 26 Tahoe（2025-09 发布）——引入 Liquid Glass
- 透明菜单栏；侧栏与工具栏呈折射/反射效果；控制中心可自定义；图标与文件夹可换色/表情；Dock 半透明。
- 争议：复杂壁纸/内容下，透明面板的**可读性**被明显批评（控制层与内容层"打架"）。

### macOS 27 Golden Gate（WWDC26 发布，2026 秋季推送）——收敛与修正
- **全局透明度滑块**：设置 > 外观新增，可把液态玻璃从"全透明"调到"不透明"。
- **统一窗口圆角半径**（解决 26 的圆角不一致/夸张问题）。
- **侧栏从悬浮改为贴边**；**侧栏彩色图标回归**。
- **工具栏风格统一**；精调动画与图标；增强复杂背景下的扩散处理；**更暗的边缘 + 更亮的高光**提升景深与可读性。
- 新壁纸「金门日落 / 金门夜色」。
- 定位：不重做视觉，专注可读性、对比度与一致性修复。

### 内在张力（保留矛盾，不调和）
- 张力 1：**玻璃质感 ↔ 可读性**。26 押注前者被批评；27 明显向后者回摆。→ 实现原则：效果服务于层级；可读性永远优先。
- 张力 2：**个性（彩色/半透明/折射）↔ 系统一致性**。27 收回了一部分"个性"（贴边侧栏、统一圆角）。→ 实现时在"克制的个性"区间取值。

## 三、对本框架的结论（用于流派选择）
- **默认基线选 27 Golden Gate 收敛版**：可读性最好、参数最少歧义。
- 需要"最接近 26 Tahoe 视觉记忆"时：提高玻璃透明度、侧栏悬浮、图标高饱和——但同时**必须**提高前景对比并做复杂背景测试（否则踩 26 被批评的原坑）。
- 经典期（Big Sur–Sequoia）特征：不透明窗口 + 统一灰工具栏 + 毛玻璃仅菜单栏/侧栏/面板——最稳，性能开销最小，适合保守项目。

# 调研 01：Apple HIG —— 材质与布局（官方一手）

> 来源（抓取于 2026-10-09）：
> - https://developer.apple.com/design/human-interface-guidelines/materials
> - https://developer.apple.com/design/human-interface-guidelines/layout
> 可信度：一手（Apple 官方规范原文）。标注「明确」= 官方原文定义；「映射」= 本框架的工程转译。

## 一、材质（Materials）

### 1. 两大材质类（官方明确）
- **Liquid Glass**：动态材质，构成**功能层**（控件与导航：侧栏、工具栏、标签栏等），浮于内容层之上；让内容可以从下方透出/滚动，同时保证控件可读。
- **标准材质**（standard materials）：用于**内容层内部**的视觉区分（如应用背景）。

### 2. Liquid Glass 使用规则（官方明确）
- **不要用在内容层**——会造成层级混乱；内容层用标准材质。
- 两个变体：
  - `regular`：模糊并调整背景亮度以保住文字可读性。**带大量文字的组件**（警告、侧栏、弹出视图）用 regular；背景可能造成可读性问题时用 regular。系统大多数组件的默认。
  - `clear`：高透明，适合浮在**媒体内容**（照片/视频）之上的控件，优先呈现在下内容。
  - clear 用在明亮内容上时：**加 35% 不透明度的暗化层**；内容本身足够暗则不需要。
- **克制使用**：标准系统组件自动获得该外观；自定义控件别滥用 Liquid Glass，否则抢内容焦点。

### 3. 标准材质厚度（iOS/iPadOS 命名，官方明确）
`ultraThin` → `thin` → `regular`(默认) → `thick`：
- 越厚越不透明 → 细节文字对比更好；
- 越薄越透 → 越保留"背景存在感"（上下文）。

### 4. 活力色 / vibrancy（官方明确）
- 标签层级：`label`(默认) > `secondaryLabel` > `tertiaryLabel` > `quaternaryLabel`；分隔线单一级别。
- 在材质之上**必须用系统 vibrant 颜色**（不要用 systemGray3 这类低对比色）。
- `thin`/`ultraThin` 上**避免 quaternary**（对比不足）。

### 5. macOS 专属（官方明确）
- 材质由 `NSVisualEffectView.Material` 定义，有明确用途集合；系统色有 vibrant 版本。
- 两种背景混合模式：`behind window`（透窗外）与 `within window`（窗内混合）。

## 二、布局（Layout）

### 视觉层级（官方明确）
- 按**阅读顺序**放置重要内容：从上到下、从前缘到后缘。
- **对齐**表达"相关"，**缩进**表达"从属"；用负空间 / 容器形状 / 分隔线表达分组。
- **进度式披露**（progressive disclosure）：折叠、菜单、嵌套视图降低首屏复杂度。

### 控件与内容的区分（官方明确）
- 用 Liquid Glass + scroll edge effect 让控件"浮起来"，**不要**给控件铺实色/半透明背景块。
- 全屏背景内容应延伸至侧栏、工具栏之下（背景铺满、控件浮上）。

### macOS 平台注意（官方明确）
- **不要把控件或关键信息放在窗口底部**（用户常把窗口下沿移到屏幕外）。
- 避免内容显示在摄像头缺口区域（顶部）。
- 支持任意窗口尺寸；尊重系统安全区与边距。

## 三、对 Web 复刻的工程映射（本框架转译）
1. 菜单栏 / Dock / 弹出面板 = **功能层** → 半透明 + backdrop-filter + 高光边；窗口正文 = **内容层** → 不透明、高对比。
2. scroll edge effect 近似：工具栏常驻玻璃底；滚动内容经过时由 backdrop-filter 吸收，必要时叠加向下的渐变遮罩。
3. 分组优先用**间距与容器**表达（8pt 网格），不靠边框线堆砌。
4. 明亮且花哨的壁纸上放控件：优先提高材质不透明度（regular 思路），而不是加更多阴影。

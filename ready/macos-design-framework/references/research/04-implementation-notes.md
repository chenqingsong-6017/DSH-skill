# 调研 04：实证实现工程笔记（macos-desktop-demo.html）

> 本文件不是"设计规范"，而是**本框架自带的验收样例**在实现中踩过的工程点。
> 样例：`assets/macos-desktop-demo.html`（单文件、零依赖、可直接双击打开）。
> 证据强度：一手（本项目实测，Edge/Chromium 无头截图 4 场景验证通过）。

## 一、架构（可复制的组织方式）
单文件 HTML ≈ 2000 行，分四层：
1. **令牌层**：CSS 变量（颜色/材质/圆角/阴影/动效曲线），深浅双套 `[data-theme]`。
2. **组件层**：菜单栏 / 下拉菜单 / 窗口 / Dock / 面板 / 弹窗。
3. **状态层**：`STATE` 对象 + localStorage 持久化（主题、壁纸、API 尺寸、开关）。
4. **行为层**：窗口管理器（拖拽/最小化/缩放/焦点栈）、应用实现、菜单系统、快捷键。

## 二、关键配方（实测参数）

### 玻璃材质（3 层结构）
```css
/* 半透明底 + 背景模糊 + 0.5px 描边 + inset 顶部高光 */
background: rgba(250,250,252,.74);
backdrop-filter: blur(34px) saturate(200%);
border: .5px solid rgba(0,0,0,.08);
box-shadow: 0 0 0 .5px rgba(0,0,0,.09), 0 12px 40px rgba(0,0,0,.22);
```
实测档位：菜单栏 blur 30px/saturate 190%；弹出面板 34–44px/200%；Dock 26px/180%。

### Dock 放大（高斯衰减）
```js
const s = 1 + (maxScale-1) * Math.exp(-(d*d));  // d = 距光标距离 / σ，σ ≈ 1.35×图标尺寸，maxScale ≈ 1.55
icon.style.transform = 'scale('+s+')';          // transform-origin: bottom center
item.style.paddingLeft/Right = 3 + (s-1)*size/2 + 'px'; // 间距同步补偿，避免图标互相重叠
```

### 最小化到 Dock（伪 genie）
把窗口 `transform-origin` 动态指向 Dock 图标的**屏幕坐标**，然后 `scale(0.06) + opacity 0`，420ms；还原时反向（先设起始态 → 强制 reflow → 开过渡）。

### 交通灯按钮（实测值）
12px 圆点 · 间距 8px · `#FF6159 / #FEBD2E / #28C941`；符号（×/-/扩展三角）仅**悬停组**显示；**窗口未聚焦时三点全部灰化**（`#d4d4d6`，暗色 `#5a5a5e`）。

### 深浅双主题
深色**不是反相**：重新配对比与饱和度（如深色背景 `#1e1e21`，文本 `#f5f5f7`，次级文本用白色 56% 透明度）；切换加 380ms 背景过渡。

## 三、实测踩坑（廉价经验，直接抄）
1. `hidden` 属性会被组件 CSS 的 `display:flex` 覆盖 → 全局补 `[hidden]{display:none!important}`（否则遮罩层常驻）。
2. `contenteditable` 取文本用 `innerText`（`textContent` 丢换行）；粘贴用 `paste` 事件转纯文本。
3. 窗口「开启动画」用 CSS animation + 完成后加 `.opened{animation:none}`，防止重新显示（如从最小化恢复）时动画重播。
4. `backdrop-filter` 在无 GPU 环境可回退，但**层级多了会掉帧**：把玻璃层数量控制在 3–5 个，动效只碰 `transform/opacity`。
5. 中文字体与西文字体栈：`-apple-system, BlinkMacSystemFont, Inter, PingFang SC, Microsoft YaHei`；Inter 用 fontsource/jsdelivr CDN（中国可达），Mac 上自动落回真 SF。
6. 拖拽用 Pointer Events + `setPointerCapture`，拖拽时给标题栏加 `pointer-events` 隔离类，避免误触按钮。

## 四、验收方式（本框架的验证协议）
- Chromium 无头截图（`--headless=new --screenshot --virtual-time-budget`）四场景：浅色默认 / 深色多窗口 / 聚焦搜索 / 单应用特写。
- URL 参数做状态注入，便于回归：`?theme=dark&wp=2&apps=finder,notes&spot=1`。

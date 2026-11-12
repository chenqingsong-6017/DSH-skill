---
name: managing-windows-software
description: 当用户要求安装新软件、升级或更新 Windows 软件、检查软件版本与可用更新、或排查 winget 安装/升级失败（症状如 0x80070032、权限不足、卡在安装阶段、下载失败）时使用。涵盖 winget 安装与升级的已知失败模式。不适用于 Linux 或容器内的软件安装与升级。
---

# 管理 Windows 软件（winget）

> 一句话定位：让 agent 掌握 Windows 软件的「安装新软件 → 升级已有 → 查版本/可用更新 → 验证」全流程，并避开 winget 的已知坑（权限、MSIX 包格式、网络、虚拟机、PATH、重启）。

## 何时使用 / 何时不用

- ✅ 使用：用户要「装个 XX / 安装 XX」「升级/更新软件」「检查版本与可用更新」「软件有没有更新」；或已出现 winget 安装报错。
- ❌ 不用：Linux / 容器内的软件安装升级（apt/yum/docker，另走）；卸载软件（除非用户明确点名，且不碰系统组件）。

## 核心原则（最先看这几条）

1. **先查后动**：装之前先 `winget search` 找包 ID，升之前先 `winget upgrade` 出清单，列给用户分类，不闷头乱装乱升。
2. **安装/升级需管理员**：winget 的「安装/升级」要写系统目录。普通权限（尤其 AI 助手运行环境）**无法触发 UAC 提权弹窗**，自动跑必失败。→ 引导用户在**管理员 PowerShell** 手动执行命令，不要反复自动重试。
3. **识别包格式**：PowerShell 7.6+ 等包 winget 默认装 MSIX，MSIX 不支持 `--scope machine`。
4. **装/升完收尾**：新装软件要**重开终端**让 PATH 生效；升 VirtualBox 前先关 VM；VC++/.NET/VirtualBox 装完要重启。

## 入口分流

| 用户输入 | 路径 |
|---|---|
| 安装新软件（"装 Docker/Java/Go/XX"） | → Step 1 |
| 升级/更新已有软件 | → Step 2 |
| 检查版本 / 有没有可用更新 | → Step 3 |

## Step 1 安装新软件

1. **查包**（只读，无需管理员）：`winget search <关键词>` 或 `winget search --id <名>`，确定准确包 ID。
2. **给用户命令**，让其粘贴进**管理员 PowerShell**（右键「以管理员身份运行」，标题带「管理员」）：
```
winget install --id <包ID> --accept-package-agreements --accept-source-agreements
```
3. **遇到 MSIX 报错**（如 0x80070032）→ 换强制 MSI：加 `--installer-type wix`。
4. **验证**：装完跑对应 `--version`（如 `pwsh --version`）；命令不识别就先**重开终端**（PATH 生效），仍不行重启。
**完成检查**：出现 `Successfully installed` + 新命令能跑出版本。

## Step 2 升级已有软件

1. **查可升级**（只读）：`winget upgrade`。
2. **出分类清单**：建议升（开发/系统底座）vs 不用特意升（会自动更新的浏览器/影音）。
3. **执行**（管理员窗口）：
```
winget upgrade --all --accept-package-agreements --accept-source-agreements
```
单包升级同理，换 `--id <包ID>`。
**完成检查**：各包逐个 `Successfully installed`，提示符回到 `PS C:\...>`。

## Step 3 检查版本与可用更新

- 已装软件：`winget list`
- 可升级清单：`winget upgrade`
- 单个软件版本：跑 `--version`（`git --version`、`pwsh --version`、`VBoxManage --version`）
**完成检查**：拿到「当前版本 → 可升到」清单。

## 失败模式编码（实测坑，逐条对号）

| # | 失败 | 信号 | 修复 |
|---|---|---|---|
| 1 | 安装/升级需管理员，AI 环境（普通权限、无法触发 UAC）自动跑必失败 | 下载/校验成功，但卡在 `Starting package install` 几分钟后 exit code 1，全程无 UAC 弹窗 | 引导用户管理员窗口手动跑；自动重试 ≥3 次即停，换路径或升级问用户 |
| 2 | PowerShell 7.6+ 起 winget 默认装 **MSIX**，MSIX 不支持 `--scope machine` | 装到 90% 报 `0x80070032 : The request is not supported` | 加 `--installer-type wix` 强制 MSI；或去掉 `--scope machine` 装 MSIX |
| 3 | GitHub 直连下载被墙（国内） | 连 `github.com:443` 超时 exit 28 | 优先走 winget 微软源（通常通）；必须下 GitHub 时让用户开加速器（如 Watt Toolkit） |
| 4 | 升 VirtualBox 时虚拟机还开着 | 安装器报错要求关闭 VirtualBox，或升级失败 | 升级前先关所有虚拟机（正常关机，别强断） |
| 5 | 新装软件后命令不识别 | `pwsh`/新命令提示 not recognized | 重开终端（PATH 生效）；仍不行重启电脑 |
| 6 | VC++/.NET/VirtualBox 装/升完需重启 | 提示 reboot，或旧版本仍残留 | 提醒用户重启，重启后再验证 |

## 命令速查

| 用途 | 命令 |
|---|---|
| 搜索包 | `winget search <关键词>` / `winget search --id <名>` |
| 安装 | `winget install --id <包ID> --accept-package-agreements --accept-source-agreements` |
| 强制 MSI（遇 MSIX 报错） | `winget install --id <包ID> --installer-type wix --accept-package-agreements --accept-source-agreements` |
| 查可升级 | `winget upgrade` |
| 一键全升 | `winget upgrade --all --accept-package-agreements --accept-source-agreements` |
| 查已装 | `winget list` |

## 高风险黑名单（禁止）

- **禁止删除 Windows PowerShell 5.1 或任何系统组件**——它们是 Windows 组件、不可卸载。「升级 PowerShell」= 新增 PowerShell 7 与其共存，绝不等于删除 5.1。
- 禁止升 VirtualBox 前不关虚拟机。
- 禁止用 `winget uninstall` 或任何方式删用户软件，除非用户明确点名并已确认。

## 诚实边界

- 只覆盖 Windows 的 winget 场景；Linux / 容器内安装升级不在此列。
- winget「默认 MSIX」是 PowerShell 7.6.0（2026-03）起的改动，行为可能随版本再变，用前现查官方安装文档。
- 命令基于 winget 1.29、PowerShell 7.6.7，2026-10 实测验证。

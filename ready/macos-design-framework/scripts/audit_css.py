#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
macOS Design Framework · 样式静态自检（只读审计）

作用：把 SKILL.md 的「验收清单」变成可执行的机器检查。
约束：仅读取文件；不写任何文件、不联网、不执行外部命令、不 eval。仅用标准库。
扫描范围：.css/.scss/.less 全量；.html/.htm 仅抽取 <style> 块与内联 style="..."（跳过 <script>）。
用法：
    python audit_css.py <文件.css|目录> [<更多路径...>] [--json] [--allow-hex #abc,#def]
行内豁免：在声明后写 /* audit:ignore MAC006 原因 */ 可跳过该行指定规则（请勿滥用）。
退出码：0 = 无 ERROR；1 = 存在 ERROR；2 = 参数错误。

规则表
  MAC001 E  硬编码色值（非变量声明行出现的 hex）
  MAC002 E  color/background 使用纯黑 #000 或纯白 #fff
  MAC003 E  单层硬阴影（box-shadow 只有一层且用 black/#000）
  MAC004 E  动效时长 > 500ms（HIG 上限：别让用户等动画）
  MAC005 E  全部文件未见 prefers-reduced-motion 降级
  MAC006 E  font-size < 10px（macOS 规范下限 10pt）| W  10–12px 非标签场景
  MAC007 E  font-weight <= 300（HIG：避免过细字重）
  MAC008 W  同文件 backdrop-filter 声明 > 5 处（掉帧风险）
  MAC009 W  backdrop-filter 缺 -webkit- 前缀（Safari 需要）
  MAC010 W  过渡了 transform/opacity 之外的布局属性（重排风险）
  MAC011 I  单行 glass 类声明未见 backdrop-filter
"""
import json
import os
import re
import sys

# Apple 实测规范值：允许直接硬编码（交通灯色、开关滑块白）
CANONICAL_HEX = {
    "#ff6159", "#febd2e", "#28c941",  # 交通灯
    "#d4d4d6", "#5a5a5e",             # 失焦交通灯灰（浅/深）
    "#fff",                            # 开关滑块等极小控件高光
}

HEX = re.compile(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})\b")
FS = re.compile(r"font-size\s*:\s*([\d.]+)\s*(px|pt|rem)?")
FW = re.compile(r"font-weight\s*:\s*(\d{3})\b")
DUR_MS = re.compile(r"(\d+)\s*ms")
DUR_S = re.compile(r"([\d.]+)\s*s\b")
SHADOW = re.compile(r"box-shadow\s*:\s*([^;]+);")
BF = re.compile(r"(?<!-)\bbackdrop-filter\s*:")
BF_WEBKIT = re.compile(r"-webkit-backdrop-filter\s*:")
GLASS_CLASS = re.compile(r"\.glass[\w-]*")
REDUCED_MOTION = re.compile(r"prefers-reduced-motion")
TRANS_PROP = re.compile(r"transition\s*:\s*([^;]+);")
PURE = re.compile(r"(?:^|[;{\s])(?:color|background|background-color)\s*:\s*(#000|#000000|#fff|#ffffff)\b")
IGNORE = re.compile(r"audit:ignore\s+([A-Za-z0-9,]+)")
LAYOUT_PROPS = {"width", "height", "top", "left", "right", "bottom", "margin", "padding"}


def strip_comments(text):
    """去掉块注释但保留行结构（行号对齐）"""
    out, in_block = [], False
    for line in text.splitlines():
        s = line
        if in_block:
            end = s.find("*/")
            if end == -1:
                out.append("")
                continue
            s, in_block = s[end + 2:], False
        while "/*" in s:
            start = s.find("/*")
            end = s.find("*/", start + 2)
            if end == -1:
                s = s[:start]
                in_block = True
                break
            s = s[:start] + s[end + 2:]
        out.append(s)
    return out


def is_token_line(line):
    return line.lstrip().startswith("--")


def collect(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, _, names in os.walk(p):
                files += [os.path.join(root, n) for n in sorted(names)
                          if n.endswith((".css", ".scss", ".less", ".html", ".htm"))]
        elif os.path.isfile(p):
            files.append(p)
    return files


def extract_html_lines(raw):
    """从 HTML 抽取可扫描行：<style> 块 + 内联 style="..."（跳过 <script>）"""
    text = re.sub(r"<script\b[^>]*>.*?</script>", "", raw, flags=re.DOTALL | re.IGNORECASE)
    out = []
    for m in re.finditer(r"<style[^>]*>(.*?)</style>", text, re.DOTALL | re.IGNORECASE):
        out += m.group(1).splitlines()
    for m in re.finditer(r"style\s*=\s*\"([^\"]*)\"", text, re.IGNORECASE):
        out.append(m.group(1))
    for m in re.finditer(r"style\s*=\s*'([^']*)'", text, re.IGNORECASE):
        out.append(m.group(1))
    return out


def audit_file(path, extra_allow):
    issues, n_bf, has_rm = [], 0, False
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            raw = fh.read()
    except OSError as e:
        return [dict(rule="MAC000", sev="E", file=path, line=0, msg="读取失败: %s" % e)], 0, False

    is_html = path.lower().endswith((".html", ".htm")) or raw.lstrip().lower().startswith(("<!doctype", "<html"))
    if is_html:
        html_raw_lines = extract_html_lines(raw)            # 保留注释，供行内豁免查找
        lines = strip_comments("\n".join(html_raw_lines))
        raw_lines = html_raw_lines
    else:
        raw_lines = raw.splitlines()
        lines = strip_comments(raw)
    allow = CANONICAL_HEX | {h.strip().lower() for h in extra_allow}

    for i, line in enumerate(lines, 1):
        low = line.lower()
        # 豁免指令写在注释里，必须在「未去注释」的原始行上查找
        raw_low = raw_lines[i - 1].lower() if i - 1 < len(raw_lines) else low
        m_ig = IGNORE.search(raw_low)
        ignored = {r.strip().upper() for r in m_ig.group(1).split(",")} if m_ig else set()

        def hit(rule, sev, msg):
            if rule not in ignored:
                issues.append(dict(rule=rule, sev=sev, file=path, line=i, msg=msg))

        if REDUCED_MOTION.search(line):
            has_rm = True

        # MAC006 / MAC007
        m = FS.search(low)
        if m and m.group(2) in (None, "px", "pt", "rem"):
            v = float(m.group(1))
            if m.group(2) == "rem":
                v *= 16
            if 0 < v < 10:
                hit("MAC006", "E", "font-size %gpx 低于 macOS 下限 10pt" % v)
            elif v < 13 and "label" not in low and "micro" not in low:
                hit("MAC006", "W", "font-size %gpx 小于正文基准 13px（确认是标签/角标）" % v)
        m = FW.search(low)
        if m and int(m.group(1)) <= 300:
            hit("MAC007", "E", "font-weight %s 过细，HIG 建议 >=400" % m.group(1))

        # MAC004
        if "transition" in low or "animation" in low:
            for ms in DUR_MS.findall(low):
                if int(ms) > 500 and "delay" not in low:
                    hit("MAC004", "E", "动效 %sms 超过 500ms 上限" % ms)
            for sec in DUR_S.findall(low):
                try:
                    if float(sec) > 0.5:
                        hit("MAC004", "E", "动效 %ss 超过 500ms 上限" % sec)
                except ValueError:
                    pass

        # MAC010
        m = TRANS_PROP.search(low)
        if m:
            props = [p.strip().split(" ")[0] for p in m.group(1).split(",")]
            bad = [p for p in props if p in LAYOUT_PROPS]
            if bad:
                hit("MAC010", "W", "过渡了布局属性 %s（改过渡 transform/opacity）" % ",".join(bad))

        # MAC003
        m = SHADOW.search(low)
        if m:
            val = m.group(1)
            if val.count(",") == 0 and ("black" in val or "#000" in val or "rgba(0,0,0,1)" in val):
                hit("MAC003", "E", "单层硬阴影，应为「描边 + 中距 + 远距」多层柔和阴影")

        # MAC009 / 计数
        n = len(BF.findall(low))
        if n:
            n_bf += n
            if not BF_WEBKIT.search(low):
                hit("MAC009", "W", "backdrop-filter 缺 -webkit- 前缀（Safari 需要）")

        # MAC001 / MAC002 / MAC011
        if not is_token_line(line):
            for h in HEX.findall(low):
                if h.lower() not in allow:
                    hit("MAC001", "E", "硬编码色值 %s（应改为 CSS 变量）" % h)
            m = PURE.search(low)
            if m and m.group(1) not in allow:
                hit("MAC002", "E", "纯黑/纯白作前景或背景（正文与底色请走令牌）")
            for cls in GLASS_CLASS.findall(low):
                if "{" in line and "}" in line and "backdrop-filter" not in low:
                    hit("MAC011", "I", "%s 单行声明未见 backdrop-filter（确认是否故意）" % cls)

    return issues, n_bf, has_rm


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    flags = [a for a in argv[1:] if a.startswith("--")]
    if not args:
        print("用法: python audit_css.py <文件.css|目录> [...] [--json] [--allow-hex #abc,#def]")
        return 2
    extra = []
    for f in flags:
        if f.startswith("--allow-hex="):
            extra = f.split("=", 1)[1].split(",")

    files = collect(args)
    if not files:
        print("未找到 CSS 文件: %s" % ", ".join(args))
        return 2

    all_issues, any_rm, any_css = [], False, False
    for f in files:
        issues, n_bf, has_rm = audit_file(f, extra)
        all_issues += issues
        any_rm = any_rm or has_rm
        any_css = any_css or f.lower().endswith((".css", ".scss", ".less"))
        base = os.path.basename(f).lower()
        # 令牌库/配方库是候选池，不按「同屏层数」计
        if n_bf > 5 and not base.startswith(("tokens", "components")):
            all_issues.append(dict(rule="MAC008", sev="W", file=f, line=0,
                                   msg="该文件 backdrop-filter %d 处，同屏玻璃层建议 <=5（掉帧风险）" % n_bf))

    # MAC005 仅在「扫描集合里含 CSS 文件却都没写降级」时触发；
    # 只扫 HTML 时令牌通常在外部 tokens.css，不误报。
    if any_css and not any_rm:
        all_issues.append(dict(rule="MAC005", sev="E", file="(全局)", line=0,
                               msg="CSS 文件未提供 @media (prefers-reduced-motion: reduce) 降级"))

    order = {"E": 0, "W": 1, "I": 2}
    all_issues.sort(key=lambda x: (order[x["sev"]], x["file"], x["line"]))
    n_e = sum(1 for i in all_issues if i["sev"] == "E")
    n_w = sum(1 for i in all_issues if i["sev"] == "W")

    if "--json" in flags:
        print(json.dumps(all_issues, ensure_ascii=False, indent=2))
    else:
        print("macOS Design Framework · 样式自检 —— 扫描 %d 个文件\n" % len(files))
        if not all_issues:
            print("全部通过，无问题。")
        for it in all_issues:
            tag = {"E": "错误", "W": "警告", "I": "提示"}[it["sev"]]
            print("[%s] %s  %s:%s  %s" % (tag, it["rule"], it["file"], it["line"] or "-", it["msg"]))
        print("\n合计：错误 %d · 警告 %d · 提示 %d" % (n_e, n_w, len(all_issues) - n_e - n_w))
    return 1 if n_e else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

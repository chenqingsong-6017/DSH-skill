#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检索痕迹检查 —— 查「开工先读索引」这一步有没有留下物证。

背景（2026-10-03 C4 诊断）：
  C4 是检索链上**唯一不留物证**的环节——「读索引」和「回复第一句声明」都不落盘，
  唯一的账（回执）是自评。实测：全仓回执里只有极少数工作区有「闸门」列、过半填 `—`。
  **没有物证 ⇒ 无法核查 ⇒ 数字不可信 ⇒ 没人有动力改。**

本脚本查两处（**只读，不改任何文件**）：
  1. `任务/<主题>/_说明.md` 的「关联经验卡」行 —— 2.2.0 起要求**开工即写**检索结论
     （`命中：E-0XX` ／ `未匹配（已读索引）`）。**缺这一节或内容为空 ＝ 漏检候选。**
  2. 各区 `复用回执/*.md` —— 2.2.0 起「检索」与「方案闸」分列；本脚本检查**值域合法性**
     并统计命中率/漏检率（旧单列格式会提示未迁移，不算错）。

用法：
    python3 检索痕迹检查.py [工作区根目录 …]
    默认当前目录；可传多个区。纯只读，无副作用。

口径纪律（同 `E-011`）：**先跑存量做基线，再谈阈值**——不要先设阈值再找样本。
"""
import os
import re
import sys

TRACE_KEY = "关联经验卡"
RET_OK = {"命中", "未匹配", "漏检", "未涉及"}
GATE_OK = {"过1轮", "过2轮", "直通", "用户跳过", "无人值守", "未涉及"}
GATE_OLD = {"按默认值直通": "直通", "无人值守直通": "无人值守",
            "纯问答未触发": "未涉及", "索引未建立": "未涉及", "—": "未涉及"}
# 「未记」过去被本脚本当作合法值（**脚本宽于文档**，值域有缺口）。3.0.0 A3 起并入旧值映射：
# 一律归一为「未涉及」⇒ 不再单列、不再合法，值域与 `回执模板.md` 一致。
RET_OLD = {"—": "未涉及", "索引未建立": "未涉及", "未记": "未涉及"}
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def strip_md(s):
    return re.sub(r"[*`>\s]", "", s or "")


def read_trace(desc_path):
    """→ (状态, 摘要)。状态 ∈ 命中／未匹配／有痕未标示／无痕／无说明卡"""
    if not os.path.exists(desc_path):
        return "无说明卡", ""
    lines = open(desc_path, encoding="utf-8").read().split("\n")
    for i, ln in enumerate(lines):
        if TRACE_KEY not in ln:
            continue
        tail = ln.split(TRACE_KEY, 1)[1]
        body = strip_md(re.sub(r"^[：:★\s]*", "", tail))
        j, skipped = i + 1, 0
        while j < len(lines) and skipped < 3 and len(body) < 200:
            nxt = lines[j].strip()
            if not nxt:
                skipped += 1
                j += 1
                continue
            if nxt.startswith("#"):
                break
            body += strip_md(nxt)
            j += 1
        if not body:
            return "无痕", ""
        if "未匹配" in body:
            return "未匹配", body[:70]
        if "命中" in body and re.search(r"E-\d{3}", body):
            return "命中", body[:70]
        if re.search(r"E-\d{3}", body):
            return "有痕未标示", body[:70]
        return "无痕", body[:70]
    return "无痕", ""


def scan_tasks(ws):
    tf = os.path.join(ws, "任务")
    if not os.path.isdir(tf):
        return []
    out = []
    for d in sorted(os.listdir(tf)):
        fp = os.path.join(tf, d)
        if not os.path.isdir(fp) or d.startswith(("_", ".")):
            continue
        st, txt = read_trace(os.path.join(fp, "_说明.md"))
        out.append((d, st, txt))
    return out


def scan_receipts(ws):
    files = []
    for c in (os.path.join(ws, "复用回执"), os.path.join(ws, "_经验库", "复用回执")):
        if os.path.isdir(c):
            files += [os.path.join(c, f) for f in sorted(os.listdir(c)) if f.endswith(".md")]
    ret_cnt, gate_cnt, illegal, legacy = {}, {}, [], []
    short = 0
    for p in files:
        lines = open(p, encoding="utf-8").read().split("\n")
        header = None
        for i, ln in enumerate(lines):
            s = ln.strip()
            if not s.startswith("|") or set(s) <= set("|-: \t"):
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if nxt.strip().startswith("|") and set(nxt.strip()) <= set("|-: \t") and any("日期" in c or "卡片" in c for c in cells):
                header = cells
                if any("闸门" in c for c in header) and not any("检索" in c for c in header):
                    legacy.append("%s（仍是旧单列「闸门」，未迁移）" % os.path.basename(p))
                continue
            if header is None:
                continue
            if len(cells) != len(header):
                short += 1
                continue
            di = next((j for j, c in enumerate(header) if "日期" in c), 0)
            if not DATE.search(cells[di] if len(cells) > di else ""):
                continue
            ri = next((j for j, c in enumerate(header) if "检索" in c), None)
            gi = next((j for j, c in enumerate(header) if "闸门" in c or "方案闸" in c), None)
            if ri is not None and len(cells) > ri:
                v = strip_md(cells[ri])
                v = RET_OLD.get(v, v)
                key = "命中" if v.startswith("命中") else v
                ret_cnt[key] = ret_cnt.get(key, 0) + 1
                if key not in RET_OK:
                    illegal.append("%s:%d 检索列＝`%s`" % (os.path.basename(p), i + 1, cells[ri][:24]))
            if gi is not None and len(cells) > gi and ri is None and "方案闸" in header[gi]:
                v = strip_md(cells[gi])
                v = GATE_OLD.get(v, v)
                gate_cnt[v] = gate_cnt.get(v, 0) + 1
    return ret_cnt, gate_cnt, illegal, legacy, short


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    wss = [os.path.abspath(a) for a in args] or [os.getcwd()]
    grand = {"task": 0, "no_trace": 0, "untag": 0}
    for ws in wss:
        name = os.path.basename(ws.rstrip("/"))
        tasks = scan_tasks(ws)
        if tasks:
            bad = [t for t in tasks if t[1] in ("无痕", "无说明卡")]
            untag = [t for t in tasks if t[1] == "有痕未标示"]
            grand["task"] += len(tasks)
            grand["no_trace"] += len(bad)
            grand["untag"] += len(untag)
            print("\n=== %s · 任务检索痕迹 ===" % name)
            print("  任务文件夹 %d 个 ｜ 有痕 %d ｜ **无痕 %d** ｜ 有痕未标示 %d"%(
                len(tasks), len(tasks) - len(bad), len(bad), len(untag)))
            if bad:
                print("  ⚠ 漏检候选（缺「关联经验卡」痕迹）：")
                for d, st, _ in bad:
                    print("     %-40s %s" % (d, st))
            if untag:
                print("  · 有痕但未标示命中/未匹配（建议下次写全）：")
                for d, _, tx in untag[:8]:
                    print("     %-40s %s" % (d, tx))
        ret, gate, illegal, legacy, short = scan_receipts(ws)
        if ret or gate or legacy or short:
            print("\n--- %s · 回执账 ---" % name)
            if short:
                print("  · 跳过 %d 行：列数与表头不符（**旧行未迁移，不计入统计**，不臆测其值）" % short)
            if ret:
                tot = sum(ret.values())
                hit = ret.get("命中", 0)
                miss = ret.get("漏检", 0)
                den = tot - ret.get("未涉及", 0)          # 「未记」已归入「未涉及」（3.0.0 A3）
                print("  检索列：%s" % ret)
                print("  → 命中率 %s ｜ 漏检率 %s（分母＝%d，已扣「未涉及」）"%(
                    ("%.0f%%" % (100 * hit / den)) if den else "n/a",
                    ("%.0f%%" % (100 * miss / den)) if den else "n/a", den))
                if den < 10:
                    print("  ⚠ **分母仅 %d 行，样本过小——不要据此下结论**（先攒满 ≥10 行再看比例）。"%den)
            if gate:
                print("  方案闸列：%s" % gate)
            if legacy:
                print("  ⚠ 未迁移的旧格式：")
                for l in legacy:
                    print("     " + l)
            if illegal:
                print("  ⚠ 非法值（值域封闭，须改）：")
                for l in illegal:
                    print("     " + l)
    if grand["task"]:
        print("\n=== 合计 ===")
        print("  任务 %d 个 ｜ 无痕 %d 个（痕率 %.0f%%）"%(
            grand["task"], grand["no_trace"], 100 * (grand["task"] - grand["no_trace"]) / grand["task"]))
    print("\n（只读检查，未改动任何文件。**先拿存量做基线，再谈阈值。**）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

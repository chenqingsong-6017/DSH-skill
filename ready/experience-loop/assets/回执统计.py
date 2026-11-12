#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""回执统计 —— 从「复用回执」聚合出每张经验卡的可信复用次数（升格阈值的输入）。

背景（实测）：阈值输入「复用次数」长期三源打架 ——
  索引「复用」列与回执实际出现次数对不上（个别卡索引记 3、回执实际 15），且部分卡根本没有「复用记录」字段。
  （⚠ 卡内「复用记录」字段已于 2.4.1 移除——次数一律由本脚本聚合；此处是历史实测。）
  输入不可信 ⇒ 阈值形同虚设 ⇒ 归并时只能凭感觉、于是被跳过。
本脚本把「索引复用列」降为**派生视图**：一律由回执聚合得出，不再手写。

用法：
    python3 回执统计.py [工作区根目录] [--apply] [--ids 'E-\\d{3}']
    python3 回执统计.py --workspaces /path/to/WorkBuddy [--min-areas 2]
    默认：当前工作区、dry-run（只报不改）。
    --apply 才回写索引「复用」列（改前请自行备份，见 skill 铁律）。

口径（写死在脚本里，人工复核照此判）：
    1. 只统计**回执表格的数据行**，且只从**卡片ID 列**取号——备注里的顺带提及不算；
    2. 卡片ID 列标「本次新建／建库，非复用／新建卡」的**不计次**（那是产出，不是复用）；
    3. **纯检索型复用不推进阈值**：只记次数，不计新证据；
    4. **新证据必须指名卡号**（2.2.2）：写 `有：E-0XX`；只写 `有` 的按粗口径算并标 ⚠，达阈须人工核归属。

2.5.0 新增（效果列「有据化」，治「评分者＝被评者」）：
    效果列不再是"一句评价"，而是 `<主值>[·<来源>[:<闸名>][(改N轮)]]`：
      来源 **闸** ＝ 证据来自**独立于产出方**的裁判（机闸／事实闸／人闸）；
      来源 **评** ＝ 只有使用者的主观感受，**无独立裁判**。
      **无后缀一律按 `评`** —— 存量行原样兼容，**不制造假证据**。
    新指标：**机械证据覆盖率 ＝ 闸 ÷ 已评** —— 直接回答"奖励信号有多少踩在事实上"。
    待修订判据**分两档**：**定性只采信 `·闸` 的负面**（进 `经验库/_台账.md` 的类型＝待修订行）；
      `·评` 的负面**只提示、不定性**（拿自评定性＝自己批自己）。
    ⚠ `·闸` **必须带闸名**——格式闸过了只证明"报告格式对"，**不证明**那张卡起了作用（防归因错误）。

--workspaces（2.3.0 新增「合订本」）：
    一区一扫升级为全仓一扫，输出①**各区制式清单**（谁用编号制／谁用卡片简称 ⇒ 直接暴露
    哪些区的复用对脚本不可见）②**回执行解析率**③同号跨区清单。
    ⚠ 同号跨区**不能**当作「独立 skill」的跨区证据 —— `E-XXX` 是**工作区本地编号**，
    实测同一编号在不同工作区指向完全不同的卡 ⇒ 那只是「编号碰撞」。
    本脚本只产出**事实**，不产出「建议进全局」——判断权在用户（全局红线一）。

3.4.0 挂载模式（描述性卡名区）：
    索引无编号行时自动启用——卡名＝回执「卡片」列的反引号内文本，且**逐个对索引卡名校验**
    （不在索引 → 计入「未匹配」报告，不臆造计次）；索引卡名取末段归一化（`00_案例库/卡名` → `卡名`）。
    无「复用」列表头时照旧不回写（不猜列号）；`--workspaces` 制式清单增「挂载制（已读出）」。
"""
import os
import re
import sys

ROW_EXCLUDE_PAT = re.compile(r"建库，非复用|（非复用）|非复用")
CARD_EXCLUDE_PAT = re.compile(r"本次新建|本轮新建|新建卡")
NEWEVID_PAT = re.compile(r"新证据")
DATE_PAT = re.compile(r"\d{4}-\d{2}-\d{2}")
THRESH_PATH_MERGE = 3      # 并入已有 skill：≥3 次且含 ≥1 次新证据
THRESH_PATH_SOLO = 5       # 独立 skill：≥5 次且跨 ≥2 区
# ---- 3.4.0：挂载模式（描述性卡名区；与 索引一致性检查.py 同步维护）----
def mount_names(cell):
    """→ [(start, end, name), …]：按序将反引号**两两配对**，取每对之内文本（`A`；`B` → ['A','B']，
    **不取两对之间的间隔**）。⚠ 不能用前视/后视正则——`A`；`B` 的「；」会被误匹（实测踩到）。
    """
    out, parts, pos = [], (cell or "").split("`"), 0
    for i in range(1, len(parts), 2):
        start = pos + len(parts[i - 1]) + 1
        end = start + len(parts[i])
        out.append((start, end, parts[i]))
        pos = end
    return out
MOUNT_HEADER_HINTS = ("卡片", "卡号", "编号", "ID")
OPTS_WITH_VALUE = ("--ids", "--workspaces", "--min-areas", "--root")


def parse_args(argv):
    pos, opts, i, n = [], {}, 0, len(argv)
    while i < n:
        a = argv[i]
        if a in OPTS_WITH_VALUE:
            opts[a] = argv[i + 1] if i + 1 < n else None
            i += 2
            continue
        if a.startswith("--"):
            opts[a] = True
            i += 1
            continue
        pos.append(a)
        i += 1
    return pos, opts


def cells_of(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def is_sep(line):
    s = line.strip()
    return s.startswith("|") and set(s) <= set("|-: \t")


def strip_md(s):
    return re.sub(r"[*`]", "", s or "")


def scan_index(idx_path, idpat):
    """→ (mode, names)。带索引扫描：编号制探测优先（与 索引一致性检查.py 同口径）；
    names＝挂载制卡名集合（取末段归一化，如 `00_案例库/卡名` → `卡名`），编号制为 None。"""
    if not idx_path:
        return "num", None
    lines = open(idx_path, encoding="utf-8").read().split("\n")
    header, names = None, set()
    for i, ln in enumerate(lines):
        if not ln.strip().startswith("|"):
            header = None
            continue
        if is_sep(ln):
            continue
        cells = cells_of(ln)
        if header is None:
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            header = cells if is_sep(nxt) else ["__skip__"]
            continue
        if "__skip__" in header or len(cells) < 2:
            continue
        if idpat.fullmatch(cells[0]):
            return "num", None
        if not any(h in header[0] for h in MOUNT_HEADER_HINTS):
            continue
        ns = [n.rsplit("/", 1)[-1].strip() for _, _, n in mount_names(cells[0])]
        if not ns:
            t = strip_md(cells[0]).strip()
            ns = [t.rsplit("/", 1)[-1].strip()] if t and t not in ("—", "-", "卡片") else []
        for n in ns:
            if n:
                names.add(n)
    return "mount", names


def parse_effect(cell):
    """效果列解析（2.5.0「有据化」）：主值 ＋ 证据来源 ＋ 闸名 ＋ 返工轮数。

    形态：`<主值>[·<来源>[:<闸名>][(改N轮)]]`
      主值 ∈ ✓／△／✗／**未评**（留空或 `—`；值域不强制——"本轮没有明显效果可评"是合法状态）
      来源 ∈ **闸**（证据来自**独立于产出方**的裁判：机闸／事实闸／人闸）／
             **评**（只有使用者的主观感受，无独立裁判）
      **无后缀一律按 `评`** —— 保证 2.4.0 存量行原样兼容，**不制造假证据**。
    返回 (主值, 来源, 闸名, 返工轮数)。
    """
    s = re.sub(r"[*`\s]", "", cell or "")
    main = "未评"
    if "✓" in s or "√" in s:
        main = "✓"
    elif "△" in s or "▲" in s:
        main = "△"
    elif "✗" in s or "×" in s or s.lower() == "x":
        main = "✗"
    if main == "未评":
        return "未评", "评", "", None
    src, gate, rework = "评", "", None
    m = re.search(r"[·・](闸|评)", s)
    if m:
        src = m.group(1)
        gm = re.match(r"[：:]?([^（(]*)", s[m.end():])
        if gm:
            gate = gm.group(1).strip("：: ")
    rm = re.search(r"[（(]改\s*(\d+)\s*轮[)）]", s)
    if rm:
        rework = int(rm.group(1))
    # ⭐ **无名闸按 `·评` 计**（防归因错误）：写了 `·闸` 却不说闸名 ⇒ 无法判断闸测的是不是这张卡那件事。
    if src == "闸" and not gate:
        return main, "评", "（无名闸）", rework
    return main, src, gate, rework


def normalize_effect(cell):
    """旧签名薄封装（2.4.0 调用点兼容）：只回主值。"""
    return parse_effect(cell)[0]


def find_receipts(ws):
    out = []
    for cand in (os.path.join(ws, "复用回执"), os.path.join(ws, "_经验库", "复用回执")):
        if os.path.isdir(cand):
            for f in sorted(os.listdir(cand)):
                if f.endswith(".md"):
                    out.append(os.path.join(cand, f))
    return out


def find_index(ws):
    for cand in (os.path.join(ws, "经验库", "_索引.md"), os.path.join(ws, "_经验库", "_索引.md")):
        if os.path.exists(cand):
            return cand
    return None


def find_workspaces(root):
    """→ [(名称, 绝对路径)]，凡是有「复用回执」或「_经验库/复用回执」的目录都算一个区"""
    out = []
    if not os.path.isdir(root):
        return out
    for d in sorted(os.listdir(root)):
        p = os.path.join(root, d)
        if not os.path.isdir(p) or d.startswith((".", "_")):
            continue
        if find_receipts(p):
            out.append((d, p))
    return out


def parse_receipts(paths, idpat, mode="num", index_names=None):
    """→ (rows, unparsed, data_rows)。rows: dict(date, task, card, excl, new, coarse, inferred, src, line)

    3.4.0：mode="mount"（描述性卡名区）——卡名＝「卡片」列反引号内文本，且（有索引名集合时）
    只留索引内的名字；不在索引的名字计入「未匹配」报告（不臆造计次）。num 模式逻辑原样。
    """
    rows, unparsed, data_rows = [], [], 0
    for p in paths:
        lines = open(p, encoding="utf-8").read().split("\n")
        header, base = None, os.path.basename(p)
        for i, ln in enumerate(lines):
            if not ln.strip().startswith("|"):
                continue
            if is_sep(ln):
                continue
            cells = cells_of(ln)
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if is_sep(nxt) and any(("卡片" in c or "日期" in c) for c in cells):
                header = cells
                continue
            if header is None or len(cells) not in (len(header), len(header) - 1):
                continue
            ci = next((j for j, c in enumerate(header) if "卡片" in c), None)
            di = next((j for j, c in enumerate(header) if "日期" in c), 0)
            if ci is None or not DATE_PAT.search(cells[di] if len(cells) > di else ""):
                continue
            ni = next((j for j, c in enumerate(header) if "新证据" in c), None)
            # 列名兼容：「效果」为本区与部分工作区的实际写法，模板历史上曾写「有用」——两者都认
            ei = next((j for j, c in enumerate(header) if "效果" in c or "有用" in c), None)
            full = len(cells) == len(header)
            cardcell = cells[ci]
            off = []
            if mode == "num":
                cards_here = idpat.findall(cardcell)
            else:
                cards_here = [n.rsplit("/", 1)[-1].strip() for _, _, n in mount_names(cardcell)]
                if index_names:
                    off = [n for n in cards_here if n not in index_names]
                    if off:
                        unparsed.append((base, i + 1, "不在索引：" + "、".join(off[:3])))
                    cards_here = [n for n in cards_here if n in index_names]
            if not cards_here:
                if cardcell and not cardcell.startswith("—") and not off:
                    unparsed.append((base, i + 1, cardcell[:60]))
                continue
            row_excl = bool(ROW_EXCLUDE_PAT.search(cells[ci]))
            data_rows += 1
            # 2.4.0 改-3：效果列 ＋ 本行卡片数。⚠ 效果是**行级**的——多卡行不能把效果算给单卡
            # （这正是 2.2.2 那次的教训：行级枚举被批量复制 ⇒ 假阳性达阈）。
            eff, esrc, egate, erework = parse_effect(
                cells[ei] if (full and ei is not None and ei < len(cells)) else "")
            ncards = len(cards_here)
            v = cells[ni] if (full and ni is not None and ni < len(cells)) else None
            named, coarse = set(), False
            if v is not None and v.strip().strip("`*-") not in ("", "—"):
                has = "有" in v
                inferred = False
                if has:
                    ids = set(idpat.findall(v)) if mode == "num" else {
                        n.rsplit("/", 1)[-1].strip() for _, _, n in mount_names(v)}
                    if ids:
                        named = ids
                    else:
                        coarse = True
            else:
                has = bool(NEWEVID_PAT.search(ln))
                inferred = True
                coarse = has
            if mode == "num":
                for m in idpat.finditer(cardcell):
                    cid = m.group(0)
                    seg_end = idpat.search(cardcell, m.end())
                    seg = cardcell[m.end(): seg_end.start() if seg_end else len(cardcell)]
                    rows.append(dict(date=cells[di] if len(cells) > di else "",
                                     task=cells[1] if len(cells) > 1 else "",
                                     card=cid, excl=row_excl or bool(CARD_EXCLUDE_PAT.search(seg)),
                                     new=(has and (cid in named)) if not coarse else has,
                                     coarse=coarse, inferred=inferred, src=base, line=i + 1,
                                     eff=eff, esrc=esrc, egate=egate, erework=erework,
                                     multi=ncards))
            else:
                marks = mount_names(cardcell)
                for k, (s0, e0, nm) in enumerate(marks):
                    nm_n = nm.rsplit("/", 1)[-1].strip()
                    if nm_n not in cards_here:
                        continue
                    seg = cardcell[e0: marks[k + 1][0] if k + 1 < len(marks) else len(cardcell)]
                    rows.append(dict(date=cells[di] if len(cells) > di else "",
                                     task=cells[1] if len(cells) > 1 else "",
                                     card=nm_n, excl=row_excl or bool(CARD_EXCLUDE_PAT.search(seg)),
                                     new=(has and (nm_n in named)) if not coarse else has,
                                     coarse=coarse, inferred=inferred, src=base, line=i + 1,
                                     eff=eff, esrc=esrc, egate=egate, erework=erework,
                                     multi=ncards))
    return rows, unparsed, data_rows


def read_index(path, idpat, mode="num"):
    """→ (lines, rows, cols)。cols = {"reuse": 列号 or None, "grade": 列号 or None}

    ⚠ **按表头名定位列，不按列序**（3.0.0 A2）：过去取 `cells[-2]`／`cells[-1]`，
    索引模板一旦调整列序就会**静默读错列、写错位置**——正是本 skill 最警惕的事故类型。
    与 `索引一致性检查.py` 的既有做法（按名定位）对齐。
    """
    rows = []
    lines = open(path, encoding="utf-8").read().split("\n")
    header = None
    cols = {"reuse": None, "grade": None}
    for i, ln in enumerate(lines):
        if not ln.strip().startswith("|"):
            header = None
            continue
        if is_sep(ln):
            continue
        cells = cells_of(ln)
        if header is None:
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            header = cells if is_sep(nxt) else ["__skip__"]
            if header != ["__skip__"]:
                cols["reuse"] = next((j for j, c in enumerate(header) if "复用" in c), None)
                cols["grade"] = next((j for j, c in enumerate(header) if "等级" in c), None)
            continue
        if "__skip__" in header or len(cells) < 2:
            continue
        if mode == "num":
            if idpat.fullmatch(cells[0]):
                rows.append((i, cells[0], cells))
        else:
            if not any(h in header[0] for h in MOUNT_HEADER_HINTS):
                continue
            ns = [n.rsplit("/", 1)[-1].strip() for _, _, n in mount_names(cells[0])]
            if not ns:
                t = strip_md(cells[0]).strip()
                ns = [t.rsplit("/", 1)[-1].strip()] if t and t not in ("—", "-", "卡片") else []
            for n in ns:
                if n:
                    rows.append((i, n, cells))
    return lines, rows, cols


def aggregate(rows):
    agg = {}
    for r in rows:
        a = agg.setdefault(r["card"], dict(n=0, new=0, excl=0, coarse=0, areas=set()))
        if r["excl"]:
            a["excl"] += 1
            continue
        a["n"] += 1
        if r["new"]:
            a["new"] += 1
            if r.get("coarse"):
                a["coarse"] += 1
        if r.get("area"):
            a["areas"].add(r["area"])
    return agg


def effect_entries(rows):
    """→ {card: [(date, eff, src, gate, rework, multi, task)]}，按日期排序；只保留非排除行。"""
    out = {}
    for r in rows:
        if r["excl"]:
            continue
        out.setdefault(r["card"], []).append((
            r.get("date", ""), r.get("eff", "未评"), r.get("esrc", "评"),
            r.get("egate", ""), r.get("erework", None),
            r.get("multi", 1), r.get("task", "")))
    for cid in out:
        out[cid].sort(key=lambda x: x[0])
    return out


def _scan_seq(seq, require_gate):
    """seq = [(主值, 来源)]；require_gate=True 时**只认 ·闸**。→ 原因 or None。"""
    tag = "·闸" if require_gate else "·评"
    for v, s in seq:
        if v == "✗" and (s == "闸" or not require_gate):
            return "有 ✗%s" % tag
    run = 0
    for v, s in seq:
        ok = (v == "△") and (s == "闸" or not require_gate)
        run = run + 1 if ok else 0
        if run >= 2:
            return "连续 ≥2 次 △%s" % tag
    return None


def needs_revision(entries):
    """→ (定性原因, 提示原因, 多卡行数, 单卡行数)。

    2.5.0 改：**「定性」（进 `_台账.md` 的待修订类）只采信 `·闸` 的负面** ——
    即 `有 ✗·闸` 或 `连续 ≥2 次 △·闸`。
    `·评` 的负面**只作提示、不定性** —— `·评` 是自评、无独立裁判，
    拿它定性等于"自己批自己"（skill「效果列有据化」）。

    ⚠ 只采信**单卡行**：效果是**行级**字段，多卡行会把效果"共享"给同行的每一张卡，
    据此判会造成假阳性（2.2.2 花掉一整版才修的同一类错）。
    """
    singles = [e for e in entries if e[5] == 1]
    multi = sum(1 for e in entries if e[5] > 1)
    seq = [(e[1], e[2]) for e in singles]
    return _scan_seq(seq, True), _scan_seq(seq, False), multi, len(singles)


def run_single(ws, idpat, apply_):
    paths = find_receipts(ws)
    if not paths:
        print("找不到「复用回执/」：", ws)
        return 2
    idx_path = find_index(ws)
    mode, index_names = scan_index(idx_path, idpat)
    rows, unparsed, data_rows = parse_receipts(paths, idpat, mode, index_names)
    agg = aggregate(rows)
    idx_val, idx_grade = {}, {}
    if idx_path:
        _, irows, icols = read_index(idx_path, idpat, mode)
        rcol, gcol = icols["reuse"], icols["grade"]
        if rcol is None or gcol is None:
            if mode == "mount":
                print("ℹ 挂载制式：索引无「复用」/「等级」列属常态 → 「索引现值」显示 `—`，不回写（不猜列号）。")
            else:
                print("⚠ 索引表头里找不到「复用」或「等级」列 → 「索引现值」显示 `—`，且**不会回写**（不猜列号）。")
        for _, iid, cells in irows:
            idx_val[iid] = cells[rcol] if (rcol is not None and len(cells) > rcol) else "—"
            idx_grade[iid] = cells[gcol] if (gcol is not None and len(cells) > gcol) else "—"
    print("工作区：%s" % ws)
    print("模式：%s ｜ 回执：%d 份 ｜ 数据行 %d ｜ **卡片计次 %d** ｜ 识别卡 %d" % (
        "编号制" if mode == "num" else "挂载制（描述性卡名）",
        len(paths), data_rows, len(rows), len(agg)))
    if mode == "mount":
        print("ℹ 挂载制：卡名＝「卡片」列反引号内文本，已对索引卡名校验；未匹配名字见下方清单。")
    print()
    print("%-8s %6s %6s %6s %8s %-10s %s" % ("卡号", "次数", "新证据", "排除", "索引现值", "等级", "判定"))
    print("-" * 78)
    merge_hit, solo_hit, coarse_hit = [], [], []
    for cid in sorted(agg, key=lambda k: (-agg[k]["n"], k)):
        a = agg[cid]
        grade = idx_grade.get(cid, "—")
        done = ("已升格" in grade) or ("已去重" in grade)
        if done:
            verdict = "已升格/已去重，跳过"
        elif a["n"] >= THRESH_PATH_MERGE and a["new"] >= 1:
            verdict = "★达阈（并入已有 skill）"
            merge_hit.append(cid)
        elif a["n"] >= THRESH_PATH_SOLO:
            verdict = "达阈（独立 skill，需跨区证据）"
            solo_hit.append(cid)
        else:
            verdict = "未达阈"
        if a["coarse"]:
            coarse_hit.append(cid)
            verdict += " ⚠（粗：%d 次新证据未指名，须人工核归属）" % a["coarse"]
        print("%-8s %6d %6d %6d %8s %-10s %s" % (cid, a["n"], a["new"], a["excl"], idx_val.get(cid, "—"), grade[:10], verdict))
    if merge_hit or solo_hit:
        print()
        print("→ 达阈未升格清单（抄进 经验库/_台账.md，类型＝待升格）：")
        for c in merge_hit:
            print("   %s  ｜ 形态：并入已有 skill ｜ 卡在哪：等用户拍板" % c)
        for c in solo_hit:
            print("   %s  ｜ 形态：独立 skill（需用户提供跨区线索） ｜ 卡在哪：等用户拍板" % c)
        if coarse_hit:
            print()
            print("   ⚠ 其中 **新证据未指名（旧粗口径）** 的卡：%s" % "、".join(coarse_hit))
            print("      —— 这些达阈**可能是同行共享造成的假阳性**，采信前必须人工核一遍（2.2.2 口径）。")

    # ---- 2.5.0：效果列聚合 ＋ 机械证据覆盖率 ＋「待修订」定性/提示分离 ----
    ee = effect_entries(rows)
    eff_cnt = {"✓": 0, "△": 0, "✗": 0, "未评": 0}
    src_cnt = {"闸": 0, "评": 0}
    gate_cnt = {}
    unnamed = 0
    for cid in ee:
        for _d, e, s, g, _w, _m, _t in ee[cid]:
            eff_cnt[e] = eff_cnt.get(e, 0) + 1
            if e == "未评":
                continue
            src_cnt[s] = src_cnt.get(s, 0) + 1
            if g == "（无名闸）":
                unnamed += 1
            if s == "闸":
                gate_cnt[g] = gate_cnt.get(g, 0) + 1
    tot_eff = sum(eff_cnt.values())
    rated = tot_eff - eff_cnt["未评"]
    cover = (100.0 * src_cnt["闸"] / rated) if rated else 0.0
    rev, tips, rev_multi, dis = [], [], [], []
    for cid in sorted(ee, key=lambda k: -len(ee[k])):
        hard, soft, multi, nsing = needs_revision(ee[cid])
        if hard:
            rev.append((cid, hard, nsing))
        elif soft:
            tips.append((cid, soft, nsing))
        if multi:
            rev_multi.append((cid, multi))
        neg_gate = any(e == "✗" and s == "闸" and m == 1 for _, e, s, _g, _w, m, _t in ee[cid])
        pos_soft = any(e == "✓" and s == "评" and m == 1 for _, e, s, _g, _w, m, _t in ee[cid])
        if neg_gate and pos_soft:
            dis.append(cid)
    print()
    print("→ 效果列（2.5.0 有据化）：%s ｜ 已评 %d／%d（%.0f%%）" % (
        "、".join("%s %d" % (k, v) for k, v in eff_cnt.items() if v),
        rated, tot_eff, (100.0 * rated / tot_eff) if tot_eff else 0))
    print("   **机械证据覆盖率 ＝ %d÷%d ＝ %.0f%%**（闸 ÷ 已评）" % (src_cnt["闸"], rated, cover))
    if src_cnt["闸"]:
        print("   闸来源分布：%s" % "、".join(
            "%s×%d" % (k, v) for k, v in sorted(gate_cnt.items(), key=lambda x: -x[1])))
    else:
        print("   ⚠ **闸来源为 0** —— 全部效果均来自自评、无独立裁判（本指标正是用来照出这种状态）。")
    if unnamed:
        print("   ⚠ **无名闸 %d 条**：写了 `·闸` 却没写闸名 ⇒ **已按 `·评` 计**"
              "（防归因错误——说不出是哪个闸，就无法判断闸测的是不是这张卡那件事）。" % unnamed)
    # 硬约束②的机械检查：闸通过但过程返工 ≥2 轮，**最多记 △**
    bad_ok = sorted({cid for cid in ee for _d, e, s, _g, w, _m, _t in ee[cid]
                     if e == "✓" and s == "闸" and (w or 0) >= 2})
    if bad_ok:
        print("   ⚠ **「返工却记 ✓」%d 张**（%s）：硬约束说「返工 ≥2 轮最多记 △」——"
              "只记结果不记代价，会鼓励为了过关硬绕，请改标 △。"
              % (len(bad_ok), "、".join(bad_ok[:6])))
    if rev:
        print("   待修订 · **定性**（只采信 ·闸）：%d 张" % len(rev))
        for cid, why, nsing in rev[:10]:
            print("     %-8s %-20s 单卡行 %d" % (cid, why, nsing))
        if len(rev) > 10:
            print("     …另有 %d 张" % (len(rev) - 10))
        print("     ⚠ 抄进 `经验库/_台账.md`（类型＝待修订；**判断必须有落点**）。")
    else:
        print("   待修订 · 定性：无")
    if tips:
        print("   待修订 · **提示**（·评 的负面，**只提示、不定性**）：%d 张" % len(tips))
        for cid, why, nsing in tips[:8]:
            print("     %-8s %-20s 单卡行 %d" % (cid, why, nsing))
    if dis:
        print("   ⚠ **闸评分歧 %d 张**（同卡 ·闸 判负／·评 判正 ⇒ **以闸为准**）：%s"
              % (len(dis), "、".join(dis[:8])))
    if rev_multi:
        print("   ⚠ 含多卡行的卡（效果未经归属、**仅供人工核**）：%s" %
              "、".join("%s×%d" % (c, n) for c, n in rev_multi[:8]))
    if unparsed:
        print()
        print("→ 卡片ID 列未匹配的行 %d 条（前 20）" % len(unparsed))
        for src, ln, txt in unparsed[:20]:
            print("   %s:%d  %s" % (src, ln, txt))
    if not idx_path:
        print("\n⚠ 本区无 `经验库/_索引.md`（领域聚合型或未建索引）→ 只出统计，不回写。")
        return 0
    if not apply_:
        print("\ndry-run：未改动任何文件。要回写索引「复用」列，加 --apply（请先备份）。")
        return 0
    lines, irows, icols = read_index(idx_path, idpat, mode)
    rcol = icols["reuse"]
    if rcol is None:
        print("\n⚠ 索引表头里找不到「复用」列 → 跳过回写（**不猜列号**）。")
        return 0
    changed = 0
    for ln_no, iid, cells in irows:
        if iid not in agg or len(cells) <= rcol:
            continue
        old_val = cells[rcol]
        new_val = str(agg[iid]["n"])
        if old_val != new_val:
            # 整行重建（不再用字符串替换：同行前面的单元格含相同值时会误替换）
            cells[rcol] = new_val
            lines[ln_no] = "| " + " | ".join(cells) + " |"
            changed += 1
            print("   索引回写 %s：%s → %s" % (iid, old_val, new_val))
    if changed:
        open(idx_path, "w", encoding="utf-8").write("\n".join(lines))
    print("\n已回写 %d 行。" % changed)
    print("⚠ 索引「用途」列里内嵌的次数文字不由脚本改，需人工同步。")
    return 0


def run_multi(root, idpat, min_areas, limit=40):
    wss = find_workspaces(root)
    if not wss:
        print("在根目录下找不到任何有「复用回执」的工作区：", root)
        return 2
    all_rows, area_of, per_area_rows = [], {}, {}
    mode_of = {}
    for name, p in wss:
        mode, names = scan_index(find_index(p), idpat)
        mode_of[name] = mode
        rows, _, _ = parse_receipts(find_receipts(p), idpat, mode, names)
        for r in rows:
            r["area"] = name
        all_rows += rows
        per_area_rows[name] = len(rows)

    # 每个区内的独立计次（同区多行算多次，但只关心"这个区用过这张卡吗"）
    card_areas = {}
    for r in all_rows:
        if r["excl"]:
            continue
        card_areas.setdefault(r["card"], {}).setdefault(r["area"], 0)
        card_areas[r["card"]][r["area"]] += 1
    agg = aggregate(all_rows)

    print("=== 合订本 · 全仓跨区视图 ===")
    print("根目录：%s" % root)
    print("扫描到 %d 个区 ｜ 回执行合计 %d ｜ 识别到卡名 %d 个" % (len(wss), len(all_rows), len(card_areas)))

    # 制式识别：编号制 / 简称制（有表行但零编号命中）/ 无回执
    style = []
    for name, p in wss:
        rows_n = per_area_rows[name]
        md = mode_of[name]
        if md == "num":
            style.append((name, "编号制", rows_n) if rows_n else (name, "无有效表行（编号制区）", 0))
        else:
            style.append((name, "挂载制（描述性卡名）", rows_n) if rows_n
                         else (name, "挂载制·解析出 0 行（核对索引格式）", 0))
    print()
    print("--- 各区制式（决定「全仓」到底覆盖了谁）---")
    for name, kind, n in sorted(style, key=lambda x: -x[2]):
        print("   %-14s %s%s" % (name, kind, "" if n == 0 else "  ｜解析出 %d 行" % n))
    blind = [s for s in style if s[2] == 0]
    if blind:
        print("   ⚠ **%d 个区解析出 0 行**（无有效回执表行，或卡名体系未识别）：%s"
              % (len(blind), "、".join(b[0] for b in blind)))
        print("      ⇒ 这几区的复用暂不可见；先核对该区回执列（「卡片」「日期」）与索引格式。")

    # 3.4.0：跨区清单只收编号制卡号——描述性卡名（挂载制）跨区同名更不构成「同一张卡」证据（本地命名）
    cross = {c: a for c, a in card_areas.items()
             if len(a) >= min_areas and idpat.fullmatch(c or "")}
    print()
    print("⚠ 同号跨区（**注意：不代表同一张卡**）：%d 张" % len(cross))
    print("   为什么不能直接采信：`E-XXX` 是**工作区本地编号**——同一个编号在不同工作区")
    print("   分别指向**完全不同的卡**。所以下表只是「编号碰撞」清单，")
    print("   **不能作为「独立 skill」跨区证据**（原设计假设不成立，见本机制迁移设计中的对应修订）。")
    if cross:
        print()
        print("%-8s %6s %6s  %s" % ("卡号", "区数", "总次数", "分布"))
        print("-" * 78)
        for cid in sorted(cross, key=lambda k: (-len(card_areas[k]), -agg[k]["n"], k)):
            a = agg[cid]
            dist = "、".join("%s×%d" % (nm, cnt) for nm, cnt in
                            sorted(card_areas[cid].items(), key=lambda x: -x[1]))
            print("%-8s %6d %6d  %s%s" % (cid, len(card_areas[cid]), a["n"], dist,
                                          "  ⚠粗口径" if a["coarse"] else ""))
    else:
        print("  （无。说明跨区复用尚未发生，或各区卡号体系不同——见下方说明）")

    print()
    print("⚠ 两条口径提醒：")
    print("  1. `E-XXX` 是**工作区本地编号**，同一个号在不同区指向完全不同的内容")
    print("     （实测：同一个编号在不同工作区分别指向**互不相干的卡**）。")
    print("     ⇒ 本表只能证明「**同号**在多区出现」，**不能证明是同一张卡**；采信前须逐条比对内容。")
    print("  2. 本表只出**事实**，不出「建议进全局」——判断权在用户（全局红线一）。")
    print("\n（只读扫描，未改动任何文件。）")
    return 0


def main():
    pos, opts = parse_args(sys.argv[1:])
    idpat = re.compile(opts.get("--ids") or r"E-\d{3}")
    if opts.get("--workspaces"):
        # C3：不再用硬编码占位路径做默认值——本机之外的路径会**静默扫空**（最危险的失效形态）。
        if opts["--workspaces"] is True:
            print("⚠ --workspaces 必须显式给出根目录路径（已取消硬编码默认值）。")
            print("   例：--workspaces ~/WorkBuddy   或   --workspaces /path/to/WorkBuddy")
            return 2
        root = opts["--workspaces"]
        try:
            min_areas = int(opts.get("--min-areas") or 2)
        except (TypeError, ValueError):
            min_areas = 2
        return run_multi(root, idpat, min_areas)
    ws = os.path.abspath(pos[0]) if pos else os.getcwd()
    return run_single(ws, idpat, "--apply" in opts)


if __name__ == "__main__":
    sys.exit(main())

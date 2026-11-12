#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""索引一致性检查（盘点员）—— 只读，对账「索引 ↔ 载体」，报四类事实。

背景（2026-10-05 新增，2.3.0；设计见本机制的一次迁移设计）：
  现有两个闸门（回执统计.py / 检索痕迹检查.py）都在查「部件在不在」「账填得合不合法」，
  **没有一个在查「索引指着的卡还在不在、指针指着的载体里到底有没有那段知识」**。
  2026-10-03 最大的那笔代价（「下沉前必须先 grep 源 skill」）根因就在这里——
  当时是靠人肉 grep 才发现的，下次未必有人记得 grep。

本脚本报**五类**（对齐该次迁移设计中的 verify 环节；第 5 类为 2.4.0 改-5 新增）：
  Missing     索引有行 → 卡文件不存在                （检索会命中一个空指针）
  Orphan      卡文件存在 → 索引无行                  （检索永远找不到它 ＝ 等于不存在）
  Stale       等级标「已升格／已去重」→ 载体里查不到该卡的关键词（知识静默丢失）
  无法判      载体识别不出且全库无命中（**不臆断为 Stale**，交人工）
  等级越界    「等级」列的值不在封闭值域内（草稿／验证／★核心／已升格／已去重／已失效）
  另：Orphan 中连回执都没提过的，标为「**幽灵卡**」。

用法：
    python3 索引一致性检查.py [工作区根目录 …] [--limit N] [--report 输出路径]
    python3 索引一致性检查.py <区> --carriers [--carriers-out 经验库/_载体总表.md]
    python3 索引一致性检查.py <区> --cards          # 【2.5.0】卡本体结构盘点（**只报不判**）
    默认当前工作区；--limit 控制对话里每类最多列几条（默认 5，**限流纪律**，明细请落 --report）。
    `--carriers` 额外产出**载体总表**（知识 → 载体，2.4.0 改-4），纯派生、可落盘。
    `--cards` 额外盘点**卡本体**（正文 >500 汉字／字段未见），**只出清单、不设阈值、不阻断**
    —— 理由见 `report_cards()` 的 docstring（存量本身就不齐，设判定＝假警机器）。
    **3.4.0**：编号制／挂载制（描述性卡名）自动探测，无需参数；挂载制下 Stale／等级越界／
    字段检查**不适用**（均明示）。

口径（写死在脚本里）：
    1. 索引只认「首列整格匹配 E-\\d{3}」的数据行，前言与说明里的表格一概不算；
    0. **双模式（3.4.0）**：`detect_mode` 先试**编号制**（任一索引文件解析出 ≥1 条编号数据行）；
       0 条才启用**挂载模式**（描述性卡名区，如 `_经验库/00_案例库/卡名.md`＋首列反引号卡名）。
       **报告明示当前模式与不适用项，绝不静默**——这正是此前挂载区「全 0 假绿」的根因。
    1. 编号制：索引只认「首列整格匹配编号」的数据行，前言与说明里的表格一概不算；
    2. 编号制卡文件只认 `经验库/{方法论,避坑,素材}/E-*.md`；挂载制卡文件＝`_经验库/`（或
       `经验库/`）**一级子目录**（除「复用回执」）的 `.md`，卡名＝文件名去 `.md`，
       排除机制文件（`_`／README 前缀，及含「台账」「索引」字样者）；
    3. Stale 的判据是**弱判据**：取索引「关键词」列的词，去载体里找，**一个都找不到才报警**
       （同义词会漏报，但足以拦住「知识根本没搬过去」这类硬伤）；
    4. 载体识别不出来时**不臆断为 Stale**，退化为「全库搜索」，找不到才报 Stale；
    5. 载体总表先认显式载体（技能目录名／反引号 .md／MEMORY.md），识别不出时用**全库命中的技能名**兜底
       ——因为索引「用途」列常写**章节名**（如 skill「① 立架构」），直接解析会大量「未识别」。

纯只读，无副作用。退出码：0 正常；2 找不到索引。
"""
import os
import re
import sys
import glob

ID_PAT = re.compile(r"E-\d{3}")
# ---- 平台适配点（3.0.0 C3）----
# 换平台后路径可能不同：用环境变量覆盖，**找不到就明确报错**，不静默查空
# （「查不到」比「报错」危险——它是本 skill 最警惕的静默失效）。
SKILLS_DIR = os.environ.get("EXP_LOOP_SKILLS_DIR") or os.path.expanduser("~/.workbuddy/skills")
GLOBAL_MEM = os.environ.get("EXP_LOOP_GLOBAL_MEM") or os.path.expanduser("~/.workbuddy/MEMORY.md")
INDEX_GLOBS = ("经验库/_索引*.md", "_经验库/_索引*.md")
CARD_GLOBS = ("经验库/方法论", "经验库/避坑", "经验库/素材",
              "_经验库/方法论", "_经验库/避坑", "_经验库/素材")
RECEIPT_DIRS = ("复用回执", "_经验库/复用回执")
UPGRADED = ("已升格", "已去重")
# ---- 3.4.0：挂载模式（描述性卡名区）----
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
    return out   # 反引号内文本＝卡名（与 回执统计.py 同步维护）
MOUNT_HEADER_HINTS = ("卡片", "卡号", "编号", "ID")  # 挂载制数据表**首列名**提示词（「升格方向」等干扰表据此排除）
MOUNT_MECH_WORDS = ("台账", "索引")                 # 挂载扫描排除的机制文件名含词（如 `04_校准台账.md`）
TEXT_EXT = (".md", ".txt", ".py", ".json", ".yaml", ".yml")
ROOT_READ_CAP = 4 * 1024 * 1024  # 单个搜索根最多读 4MB 文本
# 2.4.0 改-5：「等级」列**值域封闭**。保留 2.2.2 已依赖的「已升格／已去重」字样（改名会破坏回执统计），
# 并**必须**保留归并节在用的「★核心」（漏了它会把合法卡误报成越界——本轮自查踩到）。
# 只补「验证／已失效」两个值并明示封闭。越界即报——词一乱，脚本只能靠猜（本区曾被 `—` 坑过一次）。
# 3.5.1 定语义（只加注、**不改值域**）：`验证`＝**内容完备**，**不等于「效果已验」**——效果置信度另由回执 `·闸` 承担。
#   ⚠ 改名会让存量区的卡全被判「等级越界」（一批假警），代价远大于措辞收益，故不动 GRADE_DOMAIN。
GRADE_DOMAIN = ("草稿", "验证", "★核心", "已升格", "已去重", "已失效")


def cells_of(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def is_sep(line):
    s = line.strip()
    return s.startswith("|") and set(s) <= set("|-: \t")


def strip_md(s):
    return re.sub(r"[*`]", "", s or "")


def find_index_files(ws):
    out = []
    for g in INDEX_GLOBS:
        out += sorted(glob.glob(os.path.join(ws, g)))
    return out


def detect_mode(idx_paths):
    """→ "num" | "mount"（3.4.0）。

    编号制优先：任一索引文件能解析出 ≥1 条编号制（E-XXX 格式）数据行 → num；0 条才 mount。
    判定与 parse_index 的数据行口径一致（表格行＋首列整格匹配）——
    两处必须同步，否则探测与解析会打架（一个判 mount、一个按 num 解析＝静默空转）。
    """
    for p in idx_paths:
        lines = open(p, encoding="utf-8").read().split("\n")
        header = None
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
            if ID_PAT.fullmatch(cells[0]):
                return "num"
    return "mount"


def find_receipts(ws):
    out = []
    for d in RECEIPT_DIRS:
        p = os.path.join(ws, d)
        if os.path.isdir(p):
            out += [os.path.join(p, f) for f in sorted(os.listdir(p)) if f.endswith(".md")]
    return out


def parse_index(paths, mode="num"):
    """→ rows: list of dict(file, line, id, kw, use, grade)

    3.4.0 挂载模式的取数口径（**只看结构、不要求卡文件存在**——否则 Missing 永远报不出来）：
      ① 数据表判定＝表首列名含「卡片／卡号／编号／ID」（据此排除「升格方向」等干扰表）；
      ② 卡名＝首列反引号内文本（可一格多名）；无反引号时整格兜底（去 md 标记后非空）。
    ⚠ 行为修正（3.4.0）：无「等级」列时 grade 取空——**不再「猜末列」**（末列是「一句话」
      时会被当等级值、造成假「等级越界」）。
    """
    rows = []
    for p in paths:
        lines = open(p, encoding="utf-8").read().split("\n")
        header = None
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
            if mode == "num":
                if not ID_PAT.fullmatch(cells[0]):
                    continue
                ids = [cells[0]]
            else:
                if not any(h in header[0] for h in MOUNT_HEADER_HINTS):
                    continue
                ids = [n.rsplit("/", 1)[-1].strip() for _, _, n in mount_names(cells[0])]
                if not ids:
                    t = strip_md(cells[0]).strip()
                    ids = [t.rsplit("/", 1)[-1].strip()] if t and t not in ("—", "-", "卡片") else []
                # 归一化：索引里可能写目录前缀（如 `00_案例库/卡名`），与文件名比对前取末段。
                ids = [n for n in ids if n]
                if not ids:
                    continue
            gi = next((j for j, c in enumerate(header) if "等级" in c), None)
            ki = next((j for j, c in enumerate(header) if "关键词" in c),
                      1 if mode == "num" else len(cells) - 1)
            ui = next((j for j, c in enumerate(header) if "用途" in c), None)
            for cid in ids:
                rows.append(dict(
                    file=os.path.basename(p), line=i + 1, id=cid,
                    kw=cells[ki] if ki < len(cells) else "",
                    use=cells[ui] if (ui is not None and ui < len(cells)) else "",
                    grade=strip_md(cells[gi]) if (gi is not None and gi < len(cells)) else "",
                    rowtext=" | ".join(cells),
                ))
    return rows


def find_cards(ws, mode="num"):
    """→ {id: abspath}

    挂载模式（3.4.0）：扫 `_经验库/`（或 `经验库/`）的**一级子目录**（除「复用回执」），
    卡名＝文件名去 `.md`；排除机制文件（`_`／README 前缀，及含「台账」「索引」字样者
    ——如 `04_校准台账.md`，它不是卡）。
    """
    out = {}
    if mode == "num":
        for d in CARD_GLOBS:
            for f in glob.glob(os.path.join(ws, d, "*.md")):
                m = ID_PAT.search(os.path.basename(f))
                if m:
                    out.setdefault(m.group(0), f)
        return out
    for base in ("_经验库", "经验库"):
        root = os.path.join(ws, base)
        if not os.path.isdir(root):
            continue
        for sub in sorted(os.listdir(root)):
            d = os.path.join(root, sub)
            if not os.path.isdir(d) or sub == "复用回执":
                continue
            for f in glob.glob(os.path.join(d, "*.md")):
                fn = os.path.basename(f)
                if fn.startswith("_") or fn.upper().startswith("README"):
                    continue
                if any(w in fn for w in MOUNT_MECH_WORDS):
                    continue
                out.setdefault(fn[:-3], f)
    return out


def _is_upgraded(row, mode):
    """行是否标记「已升格／已去重」：编号制＝「等级」列；挂载制＝行文本含词（3.4.0）。"""
    if any(u in row["grade"] for u in UPGRADED):
        return True
    return mode == "mount" and ("已升格" in row["rowtext"] or "已去重" in row["rowtext"])


_WARNED_SKILLS_DIR = False


def list_skills():
    """列出 skills 目录下的技能名。

    C3：目录不存在时**不静默**。这里不退出的理由——本脚本主功能是「索引↔载体对账」，
    不依赖 skills 目录；退化为「全库搜索」仍能给出结论。所以给**显式警告**而非报错退出，
    并给出换平台时的环境变量入口。
    """
    global _WARNED_SKILLS_DIR
    if not os.path.isdir(SKILLS_DIR):
        if not _WARNED_SKILLS_DIR:
            _WARNED_SKILLS_DIR = True
            print("⚠ skills 目录不存在：%s" % SKILLS_DIR, file=sys.stderr)
            print("   影响：载体识别退化为「全库搜索」（主功能不受影响）。"
                  "换平台请用环境变量 EXP_LOOP_SKILLS_DIR 指定。", file=sys.stderr)
        return []
    return sorted(d for d in os.listdir(SKILLS_DIR)
                  if os.path.isdir(os.path.join(SKILLS_DIR, d)) and not d.startswith("."))


def keywords_of(kw_cell):
    toks = re.split(r"[／/、,，\s]+", strip_md(kw_cell))
    return [t for t in toks if len(t) >= 2]


def resolve_carriers(rowtext, skills):
    """→ list of (kind, target)。kind ∈ skill|file|memory"""
    out, seen = [], set()
    for s in skills:
        if s in rowtext and ("skill", s) not in seen:
            seen.add(("skill", s))
            out.append(("skill", os.path.join(SKILLS_DIR, s)))
    for t in re.findall(r"`([^`]+)`", rowtext):
        t = t.strip()
        if t.endswith(".md"):
            key = ("file", t)
            if key not in seen:
                seen.add(key)
                out.append(key)
    if "MEMORY.md" in rowtext and not any(k[0] == "memory" for k in out):
        out.append(("memory", GLOBAL_MEM))
    return out


_READ_CACHE = {}


def read_root(root):
    """把一个搜索根的所有文本读成一个大字符串（带缓存／大小上限）"""
    if root in _READ_CACHE:
        return _READ_CACHE[root]
    buf, total = [], 0
    if os.path.isfile(root) and root.lower().endswith(TEXT_EXT):
        try:
            buf.append(open(root, encoding="utf-8", errors="ignore").read())
        except OSError:
            pass
    elif os.path.isdir(root):
        for dp, dns, fns in os.walk(root):
            dns[:] = [d for d in dns if d not in (".git", "__pycache__")]
            for fn in fns:
                if not fn.lower().endswith(TEXT_EXT):
                    continue
                fp = os.path.join(dp, fn)
                try:
                    s = open(fp, encoding="utf-8", errors="ignore").read()
                except OSError:
                    continue
                total += len(s)
                if total > ROOT_READ_CAP:
                    break
                buf.append(s)
    text = "\n".join(buf)
    _READ_CACHE[root] = text
    return text


def hits_in(text, kws):
    return [k for k in kws if k in text]


def check_stale(row, skills):
    """→ (verdict, detail)。verdict ∈ ok|stale|no-carrier"""
    kws = keywords_of(row["kw"])
    if not kws:
        return "no-carrier", "关键词列为空，无法判"
    carriers = resolve_carriers(row["rowtext"], skills)
    if carriers:
        total = []
        for kind, target in carriers:
            total += hits_in(read_root(target), kws)
        if total:
            return "ok", "命中 %d/%d：%s" % (len(set(total)), len(kws), "、".join(sorted(set(total))[:3]))
        return "stale", "载体（%s）里一个关键词都没找到" % "、".join(os.path.basename(t) for _, t in carriers)
    # 载体识别不出 → 全库兜底
    found = []
    for s in skills:
        found += hits_in(read_root(os.path.join(SKILLS_DIR, s)), kws)
    if found:
        return "ok", "载体未识别，全库命中：%s" % "、".join(sorted(set(found))[:3])
    found = hits_in(read_root(GLOBAL_MEM), kws)
    if found:
        return "ok", "载体未识别，全局记忆命中：%s" % "、".join(sorted(set(found))[:3])
    return "stale", "载体未识别，且全库（skill＋全局记忆）都找不到关键词"


def locate_carriers(row, skills):
    """→ [载体标签, …]（**2.4.0 改-4 载体总表**用）。纯派生，不写任何文件。

    先认**显式载体**（技能目录名／反引号里的 .md／`MEMORY.md`）；识别不出时**全库搜索**，
    把关键词命中的 skill 目录名当作载体——因为索引「用途」列常写的是**章节名**（如 skill「① 立架构」），
    而非技能目录名，直接解析会大量「未识别」。
    """
    kws = keywords_of(row["kw"])
    labels = []
    for kind, target in resolve_carriers(row["rowtext"], skills):
        if kind == "skill":
            labels.append(os.path.basename(target))
        elif kind == "memory":
            labels.append("全局 MEMORY.md")
        else:
            labels.append(os.path.basename(target))
    if labels:
        return labels
    scored = []
    for s in skills:
        n = len(hits_in(read_root(os.path.join(SKILLS_DIR, s)), kws))
        if n:
            scored.append((n, s))
    # 按**命中数**降序：命中越多越可能是真载体（关键词常偏通用，会命中多个技能）
    scored.sort(key=lambda x: (-x[0], x[1]))
    labels = [s for _, s in scored]
    if not labels and hits_in(read_root(GLOBAL_MEM), kws):
        labels = ["全局 MEMORY.md"]
    return labels or ["（未识别）"]


CARD_FIELDS = (
    ("关键词", ("关键词",)),
    ("适用场景", ("适用场景",)),
    ("做法", ("做法步骤", "做法")),
    ("坑与边界", ("坑与边界",)),
    ("来源任务", ("来源任务", "来源", "原始来源")),
)
CARD_CJK_MAX = 500


def _field_present(text, aliases):
    """字段认两种形态：`- **字段**：…`（含 `**做法（…）**` 这类带括注的）与 `## 字段`。

    ⚠ 实测两种形态都在用，**只认一种必漏**（E-014：判"有没有"之前先把"可能长什么样"列全）。
    故意**不带闭合 `**`** 作判据——宁可少报，不可多报假警。
    """
    for a in aliases:
        if re.search(r"\*\*%s" % re.escape(a), text):
            return True
        if re.search(r"^#{1,6}\s*%s" % re.escape(a), text, re.M):
            return True
    return False


def report_cards(ws, limit, report_lines, mode="num"):
    """卡本体结构盘点（2.5.0 新增，只读；**只报不判**）。

    ⚠ **为什么不设"不符合项"判定**（实测：存量本身就不齐）：
      ① 五个字段**没有一个是全卡都有**的（来源任务 15／适用场景 12／坑与边界 11／做法步骤 9）；
      ② **8 张正文超 500 汉字**（最长 869）。
    设判定的结果就是上线即报 8+ 条假警 —— 正是 `E-010` 说的「白名单定错就误杀合规件」。
    故本盘点**只出清单**（供归并时顺手压缩／补全），**不设阈值、不阻断**。
    3.4.0：挂载模式下「字段未见」检查**不适用**（CARD_FIELDS 是编号制卡模板字段，
    挂载区卡结构自定义，硬套＝整库假警）→ 只报正文超长，并明示。
    原则：**结构可验、内容不可验** —— 它只证"部件在、格式对"，**不证知识对**。
    """
    cards = find_cards(ws, mode)
    if not cards:
        print("  ⚠ 未找到卡文件（%s）。" % (
            "`经验库/{方法论,避坑,素材}/E-*.md`" if mode == "num" else "`_经验库/*/`（挂载制）"))
        return
    # ⚠ 只读索引取「已升格／已去重」集合：这些卡**按设计已被压成指针**（只留验证记录），
    #   字段本就不齐 —— 不排除就会报一堆无意义的缺口（实测首跑 16/22 里有 6 张是这个原因）。
    frozen = {r["id"] for r in parse_index(find_index_files(ws), mode)
              if _is_upgraded(r, mode)}
    over, miss, skipped = [], [], []
    for cid in sorted(cards):
        try:
            t = open(cards[cid], encoding="utf-8").read()
        except OSError:
            continue
        cjk = len(re.findall(r"[\u4e00-\u9fff]", t))
        if cjk > CARD_CJK_MAX:
            over.append((cid, cjk))
        if cid in frozen:
            skipped.append(cid)
            continue
        if mode == "mount":
            continue
        gone = [nm for nm, al in CARD_FIELDS if not _field_present(t, al)]
        if gone:
            miss.append((cid, gone))
    print()
    print("  —— 卡本体盘点（**只报不判**：结构不全 ≠ 卡有问题）——")
    if mode == "mount":
        print("  卡 %d 张（**指针卡 %d 张已排除**）" % (len(cards), len(skipped)))
        print("  ｜ 正文 >%d 汉字 %d 张 ｜ ℹ 挂载制卡结构自定义 →「字段未见」检查**不适用**"
              % (CARD_CJK_MAX, len(over)))
    else:
        print("  卡 %d 张（**指针卡 %d 张已排除**：已升格/已去重者按设计只留验证记录）" % (
            len(cards), len(skipped)))
        print("  ｜ 正文 >%d 汉字 %d 张 ｜ 字段未见 %d 张" % (CARD_CJK_MAX, len(over), len(miss)))
    if over:
        print("  · **超长**（skill 上限 %d 汉字；压缩/归并时顺手处理，**不阻断**）：" % CARD_CJK_MAX)
        for cid, n in sorted(over, key=lambda x: -x[1])[:limit]:
            print("     %-8s %d 字" % (cid, n))
        if len(over) > limit:
            print("     …另有 %d 张，见 --report 明细" % (len(over) - limit))
    if miss:
        print("  · **字段未见**（各卡写作年代不同、形态本就参差，属**已知历史**，非错误）：")
        for cid, gone in miss[:limit]:
            print("     %-8s 未见：%s" % (cid, "／".join(gone)))
        if len(miss) > limit:
            print("     …另有 %d 张，见 --report 明细" % (len(miss) - limit))
    report_lines.append("")
    report_lines.append("### 卡本体盘点（只报不判）")
    report_lines.append("")
    report_lines.append("- 卡 %d 张（其中指针卡 %d 张已排除字段盘点）；正文超 %d 汉字 %d 张；字段未见 %d 张%s" % (
        len(cards), len(skipped), CARD_CJK_MAX, len(over), len(miss),
        "（挂载制：字段检查不适用）" if mode == "mount" else ""))
    if over:
        report_lines.append("- 超长：" + "、".join("%s(%d字)" % x for x in sorted(over, key=lambda x: -x[1])))
    if miss:
        report_lines.append("- 字段未见：" + "、".join("%s[%s]" % (c, "／".join(g)) for c, g in miss))


def run_ws(ws, limit, report_lines, opts):
    name = os.path.basename(ws.rstrip("/"))
    idx_paths = find_index_files(ws)
    mode = detect_mode(idx_paths) if idx_paths else "num"
    print("\n=== %s ===" % name)
    if opts.get("--cards"):
        report_cards(ws, limit, report_lines, mode)
    if not idx_paths:
        print("  ⚠ 找不到索引（`经验库/_索引*.md`）——跳过。")
        return dict(missing=0, orphan=0, stale=0, noc=0, cards=0, rows=0, has_index=False)
    rows = parse_index(idx_paths, mode)
    idx_ids = {r["id"]: r for r in rows}
    cards = find_cards(ws, mode)
    disk_ids = set(cards)
    idx_set = set(idx_ids)

    receipts = find_receipts(ws)
    rec_text = "\n".join(open(p, encoding="utf-8").read() for p in receipts)

    missing = sorted(idx_set - disk_ids)
    orphan = sorted(disk_ids - idx_set)
    ghost = [i for i in orphan if i not in rec_text]

    skills = list_skills()
    # ⚠ 必须取自**索引**、不能与盘上卡取交集：升格后若原卡已删，"载体里有没有"仍须核（实测踩到）
    upgraded_ids = [c for c in sorted(idx_set) if _is_upgraded(idx_ids[c], mode)]
    # ---- 2.4.0 改-5：等级列**值域**校验（越界即报，词一乱脚本只能靠猜）----
    grade_bad = [(cid, idx_ids[cid]["grade"]) for cid in sorted(idx_set)
                 if idx_ids[cid]["grade"] and idx_ids[cid]["grade"] not in GRADE_DOMAIN]
    stale, nosearch = [], []
    for cid in upgraded_ids:
        verdict, detail = check_stale(idx_ids[cid], skills)
        if verdict == "stale":
            stale.append((cid, detail))
        elif verdict == "no-carrier":
            nosearch.append((cid, detail))

    print("  模式：%s ｜ 索引 %d 个 ｜ 卡文件 %d 个 ｜ 回执 %d 份 ｜ 已升格/已去重待核 %d 张" % (
        "编号制" if mode == "num" else "挂载制（描述性卡名）",
        len(idx_set), len(disk_ids), len(receipts), len(upgraded_ids)))
    if mode == "mount":
        print("  ℹ 挂载制：Stale／等级越界依赖「等级」列 → 本区无此列，两项**不适用**（恒 0 ≠ 查过没事）。")
        if not idx_set:
            print("  ⚠ 索引文件在、但挂载模式解析出 0 条卡——请人工核对索引表首列名与格式（**禁静默**；新建空索引可忽略）。")
    if opts.get("--verbose"):
        for cid in upgraded_ids:
            v, d = check_stale(idx_ids[cid], skills)
            print("     · %s ［%s］ %s" % (cid, idx_ids[cid]["grade"][:6], d))
    print("  **Missing %d ｜ Orphan %d（其中幽灵卡 %d）｜ Stale %d ｜ 无法判 %d ｜ 等级越界 %d**" % (
        len(missing), len(orphan), len(ghost), len(stale), len(nosearch), len(grade_bad)))

    def dump(title, items, fmt):
        if not items:
            return
        print("  ⚠ %s：%d 条" % (title, len(items)))
        for it in items[:limit]:
            print("     " + fmt(it))
        if len(items) > limit:
            print("     …另有 %d 条，见 --report 明细" % (len(items) - limit))

    dump("Missing（索引有行、卡不存在）", missing, lambda x: x)
    dump("Orphan（卡在盘上、索引无行）＝ 检索不到＝不存在", orphan,
         lambda x: "%s%s" % (x, "  ← 幽灵卡（回执也没提过）" if x in ghost else ""))
    dump("Stale（标了已升格/已去重，载体里却没有）", stale, lambda x: "%s  %s" % x)
    dump("无法判（载体未识别且全库无命中）", nosearch, lambda x: "%s  %s" % x)
    dump("等级越界（不在值域内）", grade_bad,
         lambda x: "%s  ［%s］← 只认 草稿／验证／★核心／已升格／已去重／已失效" % x)

    # ---- 2.4.0 改-4：载体总表（知识 → 载体），纯派生 ----
    # ⚠ **只列「已升格／已去重」的卡**——草稿卡本来就没有载体，收进来必然全是关键词噪音
    #    （实测：不筛时一张卡会列出多个"载体"，全无意义）。
    carrier_rows = []
    if opts.get("--carriers") or opts.get("--carriers-out"):
        for cid in sorted(idx_set):
            r = idx_ids[cid]
            if not _is_upgraded(r, mode):
                continue
            cand = locate_carriers(r, skills)
            primary = cand[0]
            extra = "（＋%d 个候选）" % (len(cand) - 1) if len(cand) > 1 else ""
            carrier_rows.append((cid, r["kw"], r["grade"] or "—", primary + extra))
        print()
        print("  → 载体总表（%d 条，**由脚本派生**；只列已升格/已去重）：" % len(carrier_rows))
        print("     %-8s %-8s %s" % ("卡号", "等级", "载体（主）"))
        for cid, _, g, cs in carrier_rows:
            print("     %-8s %-8s %s" % (cid, g[:8], cs))
        print("     ⚠ 关键词偏通用时会命中多个技能，表里给的是**命中数最高**的那个，其余算候选。")

    report_lines.append("\n## %s（索引 %d／卡 %d／回执 %d）" % (name, len(idx_set), len(disk_ids), len(receipts)))
    for title, items in (("Missing", missing), ("Orphan", orphan), ("Stale", stale), ("无法判", nosearch)):
        report_lines.append("- %s：%d 条%s" % (title, len(items),
                                           ("　" + "、".join(x[0] if isinstance(x, tuple) else x for x in items)) if items else ""))
    for cid, detail in stale + nosearch:
        report_lines.append("  - %s：%s" % (cid, detail))
    if grade_bad:
        report_lines.append("- 等级越界：%d 条　%s" % (len(grade_bad),
                                              "、".join("%s[%s]" % x for x in grade_bad)))
    if carrier_rows:
        report_lines.append("")
        report_lines.append("### 载体总表（派生，只列已升格/已去重）")
        report_lines.append("")
        report_lines.append("| 卡号 | 关键词 | 等级 | 载体（主） |")
        report_lines.append("|---|---|---|---|")
        for cid, kw, g, cs in carrier_rows:
            report_lines.append("| %s | %s | %s | %s |" % (cid, kw, g, cs))
    return dict(missing=len(missing), orphan=len(orphan), stale=len(stale), noc=len(nosearch),
                grade=len(grade_bad), cards=len(disk_ids), rows=len(idx_set), has_index=True)


OPTS_WITH_VALUE = ("--limit", "--report", "--carriers-out")


def parse_args(argv):
    """→ (positional, opts)。坑：带值的选项其值不能被当成工作区路径（实测 --limit 8 被读成路径）。"""
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


def main():
    pos, opts = parse_args(sys.argv[1:])
    try:
        limit = int(opts.get("--limit") or 5)
    except (TypeError, ValueError):
        limit = 5
    report_path = opts.get("--report")
    wss = [os.path.abspath(a) for a in pos] or [os.getcwd()]

    report_lines = ["# 索引一致性盘点报告（由 assets/索引一致性检查.py 生成）"]
    tot = dict(missing=0, orphan=0, stale=0, noc=0, grade=0, cards=0, rows=0)
    checked = 0
    for ws in wss:
        s = run_ws(ws, limit, report_lines, opts)
        if s.get("has_index"):
            checked += 1
            for k in tot:
                tot[k] += s.get(k, 0)

    print("\n=== 合计 ===")
    print("  已盘点 %d 个区 ｜ Missing %d ｜ Orphan %d ｜ Stale %d ｜ 无法判 %d ｜ 等级越界 %d" % (
        checked, tot["missing"], tot["orphan"], tot["stale"], tot["noc"], tot["grade"]))

    # 2.4.0 改-4：--carriers-out 单独成表，便于直接落成 经验库/_载体总表.md
    carriers_out = opts.get("--carriers-out")
    if carriers_out and carriers_out is not True:
        rows = []
        for ln in report_lines:
            if ln.startswith("|"):
                rows.append(ln)
        if not rows:
            print("   ⚠ --carriers-out：本次没有生成载体行（缺 `--carriers`？或该区无索引）。")
        else:
            os.makedirs(os.path.dirname(os.path.abspath(carriers_out)), exist_ok=True)
            open(carriers_out, "w", encoding="utf-8").write("\n".join(rows) + "\n")
            print("   载体总表已落盘：%s（%d 行）" % (carriers_out, len(rows)))
            print("   ⚠ 本表是**派生视图**——由脚本从索引＋关键词搜索算出，**改前请人工核**。")

    if report_path:
        os.makedirs(os.path.dirname(os.path.abspath(report_path)), exist_ok=True)
        open(report_path, "w", encoding="utf-8").write("\n".join(report_lines) + "\n")
        print("  明细已落盘：%s" % report_path)

    print("\n（只读检查，未改动任何文件。**Stale 是弱判据**——报出来的请人工核一遍再动手。）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

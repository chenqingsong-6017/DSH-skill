#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""worldview-setting 维护脚本

纯标准库实现，无网络无第三方依赖。所有写操作在 commit --confirmed 前先备份。
命令：status / audit / commit / diff / export / selftest
"""
import argparse
import difflib
import re
import shutil
import sys
import tempfile
from datetime import date, datetime
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = SKILL_ROOT / "content"
BACKUP_DIR = SKILL_ROOT / "backup"
BASELINE_DIR = BACKUP_DIR / "_baseline"  # 上次提交后的内容基线（不参与历史快照列举）
INDEX_FILE = CONTENT_DIR / "_index.md"
CHANGELOG_FILE = SKILL_ROOT / "CHANGELOG.md"
COMPONENT_FILES = ["01_背景.md", "02_规则.md", "03_角色.md", "04_势力.md", "05_价值观.md", "06_目标.md"]
ALL_CONTENT_FILES = ["_index.md"] + COMPONENT_FILES

META_RE = re.compile(r"^<!-- meta: (.+?) -->")
VERSION_RE = re.compile(r"version=(v?\d+\.\d+\.\d+)")
UPDATED_RE = re.compile(r"updated=(\d{4}-\d{2}-\d{2})")
DATE_RE = re.compile(r"(20\d{2}-\d{2}-\d{2})")

STALE_DAYS = 30          # 组件 updated 超过此天数 → WARN
SNAPSHOT_STALE_DAYS = 180  # 采集日期类快照超过此天数 → WARN


def ensure_utf8():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, s: str) -> None:
    path.write_text(s, encoding="utf-8")


def parse_meta_line(line: str):
    m = META_RE.match(line.strip())
    if not m:
        return {}
    kv = {}
    for part in m.group(1).split(","):
        part = part.strip()
        if "=" in part:
            k, v = part.split("=", 1)
            kv[k.strip()] = v.strip()
    return kv


def read_meta(path: Path):
    lines = read_text(path).splitlines()
    if not lines:
        return {}
    return parse_meta_line(lines[0])


def current_version(index_file: Path = INDEX_FILE) -> str:
    return read_meta(index_file).get("version", "v0.0.0")


def bump_version(version: str, kind: str) -> str:
    v = version.lstrip("v").split(".")
    major, minor, patch = (int(x) for x in v[:3])
    if kind == "patch":
        patch += 1
    elif kind == "minor":
        minor += 1
        patch = 0
    else:
        major += 1
        minor = 0
        patch = 0
    return f"v{major}.{minor}.{patch}"


def registry_rows(content_dir: Path = CONTENT_DIR) -> str:
    rows = []
    for fname in COMPONENT_FILES:
        f = content_dir / fname
        if not f.exists():
            rows.append(f"| ? | {fname} | （文件缺失） | ❌ |")
            continue
        meta = read_meta(f)
        text = read_text(f)
        status = "✅＋⏳" if "⏳" in text else "✅"
        rows.append(
            f"| {meta.get('component', fname)} | {fname} | {meta.get('summary', '-')} | {status} |"
        )
    return "\n".join(rows)


def rebuild_registry_in_index(content_dir: Path = CONTENT_DIR) -> None:
    index = content_dir / "_index.md"
    text = read_text(index)
    start = text.index("## 组件注册表")
    end = text.index("## 读取指引")
    header = (
        "## 组件注册表\n\n"
        "| 组件 | 文件 | 内容要点 | 状态 |\n"
        "|---|---|---|---|\n"
    )
    write_text(index, text[:start] + header + registry_rows(content_dir) + "\n\n" + text[end:])


def set_version_in_index(version: str, index_file: Path = INDEX_FILE) -> None:
    lines = read_text(index_file).splitlines(keepends=True)
    if not lines or not META_RE.match(lines[0].strip()):
        raise RuntimeError("_index.md 首行 meta 缺失")
    lines[0] = VERSION_RE.sub(f"version={version}", lines[0], count=1)
    write_text(index_file, "".join(lines))


def update_meta_updated(path: Path, day: str) -> None:
    """把首行 meta 的 updated= 改成 day；无该字段则补在 meta 末尾。"""
    lines = read_text(path).splitlines(keepends=True)
    if not lines or not META_RE.match(lines[0].strip()):
        raise RuntimeError(f"{path.name} 首行 meta 缺失，拒绝提交")
    first = lines[0]
    if UPDATED_RE.search(first):
        lines[0] = UPDATED_RE.sub(f"updated={day}", first, count=1)
    else:
        lines[0] = first.replace("-->", f", updated={day} -->", 1)
    write_text(path, "".join(lines))


def latest_snapshot(backup_dir: Path = BACKUP_DIR):
    if not backup_dir.exists():
        return None
    dirs = sorted([d for d in backup_dir.iterdir() if d.is_dir() and not d.name.startswith("_")])
    return dirs[-1] if dirs else None


def collect_changes(content_dir: Path = CONTENT_DIR, snapshot=None):
    """对比当前内容与最近一次快照，返回实际改动过的组件文件名列表。

    snapshot 为 None（无历史快照）时视为全部改动。
    """
    snap_content = snapshot / "content" if snapshot else None
    changed = []
    for fname in COMPONENT_FILES:
        cur = content_dir / fname
        if not cur.exists():
            continue
        if snap_content is None:
            changed.append(fname)
            continue
        old = snap_content / fname
        if not old.exists() or read_text(old) != read_text(cur):
            changed.append(fname)
    return changed


def headings_of(path: Path):
    return {l.strip() for l in read_text(path).splitlines() if re.match(r"^#{1,3} ", l.strip())}


def changelog_append(version: str, message: str, files: str, confirmed_by: str,
                     changelog_file: Path = CHANGELOG_FILE) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = (
        f"## {version}（{now}）\n\n"
        f"- 改动：{message}\n"
        f"- 涉及文件：{files}\n"
        f"- 确认方式：{confirmed_by}\n\n"
    )
    if changelog_file.exists():
        text = read_text(changelog_file)
        marker = "# CHANGELOG"
        if marker in text:
            text = text.replace(marker, marker + "\n\n" + entry.rstrip("\n"), 1)
        else:
            text = entry + text
        write_text(changelog_file, text)
    else:
        write_text(changelog_file, "# CHANGELOG\n\n" + entry)


def changelog_latest_version(changelog_file: Path = CHANGELOG_FILE) -> str:
    if not changelog_file.exists():
        return ""
    for line in read_text(changelog_file).splitlines():
        m = re.match(r"^##\s+(v\d+\.\d+\.\d+)", line.strip())
        if m:
            return m.group(1)
    return ""


def cmd_status(_args) -> int:
    version = current_version()
    print(f"版本：{version}")
    print(f"内容目录：{CONTENT_DIR}")
    total_chars = 0
    for fname in COMPONENT_FILES:
        f = CONTENT_DIR / fname
        if not f.exists():
            print(f"  [缺失] {fname}")
            continue
        text = read_text(f)
        n_lines = len(text.splitlines())
        n_pending = text.count("⏳")
        meta = read_meta(f)
        print(f"  {fname:12s} {n_lines:3d} 行 ｜ ⏳×{n_pending} ｜ updated={meta.get('updated', '?')}")
        total_chars += len(text)
    complete = all((CONTENT_DIR / f).exists() for f in COMPONENT_FILES)
    print(f"注册表完整性：{'完整' if complete else '不完整'}")
    print(f"内容总量：约 {total_chars} 字符")
    if CHANGELOG_FILE.exists():
        print(f"CHANGELOG 条目数：{read_text(CHANGELOG_FILE).count('## v')}")
    return 0


# ─────────────────────────── 体检 ───────────────────────────


def _registry_rows_in_index(index_path: Path):
    text = read_text(index_path)
    if "## 组件注册表" not in text or "## 读取指引" not in text:
        return None
    seg = text[text.index("## 组件注册表"):text.index("## 读取指引")]
    rows = []
    for line in seg.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        if "---" in s or s.startswith("| 组件"):
            continue
        rows.append(s)
    return rows


def audit_core(root: Path):
    """返回 issues 列表：[(level, code, message)]，level ∈ FAIL / WARN / INFO。"""
    content = root / "content"
    index = content / "_index.md"
    changelog = root / "CHANGELOG.md"
    issues = []
    today = date.today()

    def add(level, code, msg):
        issues.append((level, code, msg))

    # 1 文件齐全
    for fname in ALL_CONTENT_FILES:
        if not (content / fname).exists():
            add("FAIL", "MISSING", f"缺少组件文件：{fname}")
    if any(code == "MISSING" for _, code, _ in issues):
        return issues

    # 2 meta 行
    for fname in ALL_CONTENT_FILES:
        meta = read_meta(content / fname)
        if not meta:
            add("FAIL", "META_MISSING", f"{fname} 首行缺 meta 行")
            continue
        if not UPDATED_RE.search(read_text(content / fname).splitlines()[0]):
            add("WARN", "META_NO_DATE", f"{fname} meta 缺 updated=")
    if not VERSION_RE.search(read_text(index).splitlines()[0]):
        add("FAIL", "META_NO_VERSION", "_index.md meta 缺 version=")

    # 3 版本与 CHANGELOG 一致
    ver = current_version(index)
    latest = changelog_latest_version(changelog)
    if latest and latest != ver:
        add("FAIL", "VERSION_DRIFT", f"_index 版本 {ver} ≠ CHANGELOG 最新 {latest}")
    if not latest:
        add("WARN", "CHANGELOG_EMPTY", "CHANGELOG 无版本条目")

    # 4 注册表与内容一致
    rows_now = _registry_rows_in_index(index)
    expected = registry_rows(content).splitlines()
    if rows_now is None:
        add("FAIL", "INDEX_SECTION", "_index.md 缺「组件注册表」或「读取指引」小节")
    elif rows_now != expected:
        diff_n = sum(1 for a, b in zip(rows_now, expected) if a != b) + abs(len(rows_now) - len(expected))
        add("FAIL", "REGISTRY_STALE", f"注册表与内容不一致（{diff_n} 行不同）→ 重跑 commit 或手动 rebuild")

    # 5 悬置项清单
    pending = []
    for fname in COMPONENT_FILES:
        text = read_text(content / fname)
        if "⏳" not in text:
            continue
        for line in text.splitlines():
            s = line.strip()
            if s.startswith("#") and "⏳" in s:
                title = re.sub(r"^#+\s*", "", s).split("⏳")[0].strip()
                pending.append(f"{fname} {title}")
    if pending:
        add("INFO", "PENDING", f"悬置项 {len(pending)} 项（⏳ 标记不代表项数）：" + "；".join(pending))
    else:
        add("INFO", "PENDING", "无悬置项")

    # 6 updated 滞后
    for fname in COMPONENT_FILES:
        m = UPDATED_RE.search(read_text(content / fname).splitlines()[0])
        if not m:
            continue
        try:
            d = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except ValueError:
            add("WARN", "DATE_BAD", f"{fname} updated 日期无法解析：{m.group(1)}")
            continue
        days = (today - d).days
        if days > STALE_DAYS:
            add("WARN", "STALE_FILE", f"{fname} 已 {days} 天未更新（updated={m.group(1)}）")

    # 7 采集日期超期
    for fname in COMPONENT_FILES:
        for line in read_text(content / fname).splitlines():
            if "采集" not in line:
                continue
            for ds in DATE_RE.findall(line):
                try:
                    d = datetime.strptime(ds, "%Y-%m-%d").date()
                except ValueError:
                    continue
                days = (today - d).days
                if days > SNAPSHOT_STALE_DAYS:
                    add("WARN", "STALE_DATA", f"{fname} 采集日期 {ds} 已 {days} 天：{line.strip()[:60]}")
                break

    # 8 占位符
    for fname in COMPONENT_FILES:
        for line in read_text(content / fname).splitlines():
            if re.search(r"(TODO|FIXME|待补|待填|xxx|XXX|\?\?\?)", line):
                add("WARN", "PLACEHOLDER", f"{fname} 含占位符：{line.strip()[:60]}")

    return issues


def cmd_audit(_args) -> int:
    issues = audit_core(SKILL_ROOT)
    print(f"体检报告 · 版本 {current_version()} · {date.today().isoformat()}")
    print(f"内容目录：{CONTENT_DIR}")
    print("-" * 60)
    order = {"FAIL": 0, "WARN": 1, "INFO": 2}
    for level, code, msg in sorted(issues, key=lambda x: order[x[0]]):
        print(f"[{level}] {code}: {msg}")
    n_fail = sum(1 for l, _, _ in issues if l == "FAIL")
    n_warn = sum(1 for l, _, _ in issues if l == "WARN")
    print("-" * 60)
    print(f"结果：{n_fail} FAIL / {n_warn} WARN")
    print("未校验项（脚本查不了，须按 SKILL.md 三·第二步人工/agent 执行）：")
    print("  · 与全局记忆的语义冲突（数字/清单/定位）")
    print("  · 条目内容是否仍与本人当下想法一致")
    print("  · backup/ 历史快照不参与体检")
    return 1 if n_fail else 0


# ─────────────────────────── 提交 ───────────────────────────


def cmd_commit(args) -> int:
    message = args.message
    if not message:
        print("错误：commit 需要改动说明（message）")
        return 1

    # 基线优先取「上次提交后的状态」；没有则退回最近历史快照（首次使用）
    snap_prev = BASELINE_DIR if (BASELINE_DIR / "content").exists() else latest_snapshot()
    changed = collect_changes(CONTENT_DIR, snap_prev)
    declared = [f for f in (args.files or []) if f]

    if not changed:
        print("无改动：当前内容与最近一次快照一致，未提交。")
        print(f"最近快照：backup/{snap_prev.name}" if snap_prev else "（无历史快照）")
        return 1

    if declared:
        extra = [f for f in declared if f not in changed]
        missing = [f for f in changed if f not in declared]
        if extra or missing:
            print("错误：--files 与实际改动不一致，拒绝提交。")
            if extra:
                print(f"  声明了但未改动：{', '.join(extra)}")
            if missing:
                print(f"  改动了但未声明：{', '.join(missing)}")
            print("（脚本不猜你的意思，请对齐后再提交）")
            return 1
        files = declared
    else:
        files = changed

    # 结构提示：标题增删通常是 minor
    bump_hint = ""
    if snap_prev:
        for fname in files:
            old_f = snap_prev / "content" / fname
            if not old_f.exists():
                bump_hint = "新增组件文件 → 建议 --bump minor"
                break
            if headings_of(old_f) != headings_of(CONTENT_DIR / fname):
                bump_hint = "检测到标题增删 → 建议 --bump minor"
                break

    new_version = bump_version(current_version(), args.bump)
    if not args.confirmed:
        print(f"[演练] 将提交 {new_version}（bump={args.bump}）")
        print(f"[演练] 改动说明：{message}")
        print(f"[演练] 实际改动文件：{', '.join(files)}")
        if bump_hint:
            print(f"[演练] 提示：{bump_hint}")
        print("[演练] 未执行任何写操作。确认无误后加 --confirmed 真执行。")
        return 0

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    snap = BACKUP_DIR / stamp
    i = 1
    while snap.exists():
        snap = BACKUP_DIR / f"{stamp}-{i}"
        i += 1
    snap.mkdir(parents=True)
    shutil.copytree(CONTENT_DIR, snap / "content")
    if CHANGELOG_FILE.exists():
        shutil.copy2(CHANGELOG_FILE, snap / "CHANGELOG.md")
    print(f"已备份快照：backup/{snap.name}")

    day = date.today().isoformat()
    for fname in files:
        update_meta_updated(CONTENT_DIR / fname, day)
    set_version_in_index(new_version)
    rebuild_registry_in_index()
    changelog_append(
        new_version,
        message,
        ", ".join(files),
        args.by or "（待填：本人确认 或 AI 提案）",
    )
    # 刷新基线：下次 commit 只比对「本次提交后」的差异，避免重复记账
    if BASELINE_DIR.exists():
        shutil.rmtree(BASELINE_DIR)
    shutil.copytree(CONTENT_DIR, BASELINE_DIR / "content")

    print(f"已更新 {len(files)} 个文件的 updated={day}")
    print(f"已提交 {new_version}：{message}")
    print(f"CHANGELOG 已追加（{CHANGELOG_FILE.name}）")
    if bump_hint:
        print(f"提示：{bump_hint}（版本已按 --bump={args.bump} 自增）")
    print("下一步：maintain.py export --out <路径> 同步记忆库导出物")
    return 0


def cmd_diff(args) -> int:
    snap = BACKUP_DIR / args.backup / "content"
    if not snap.exists():
        print(f"错误：快照不存在：{snap}")
        print("可用快照：")
        for d in sorted(BACKUP_DIR.glob("*")):
            if d.is_dir() and not d.name.startswith("_"):
                print(f"  {d.name}")
        return 1
    changed = 0
    for fname in COMPONENT_FILES + ["_index.md"]:
        old_f, new_f = snap / fname, CONTENT_DIR / fname
        if not old_f.exists():
            print(f"[新增] {fname}（旧快照无此文件）")
            changed += 1
            continue
        old = read_text(old_f).splitlines()
        new = read_text(new_f).splitlines()
        if old != new:
            changed += 1
            print(f"── {fname} ──")
            for line in difflib.unified_diff(old, new, fromfile=str(old_f), tofile=str(new_f), lineterm=""):
                print(line)
    if changed == 0:
        print("无差异：当前内容与快照一致")
    else:
        print(f"共 {changed} 个文件有差异")
    return 0


EXPORT_NOTE = (
    "# 个人世界观框架（导出版）\n\n"
    "> 本文件由 worldview-setting skill 的 maintain.py export 生成，**生成物勿手改**。\n"
    "> 手改入口＝skill 的 content/ 组件文件；更新口令＝「更新世界观」。\n"
)


def cmd_export(args) -> int:
    out = Path(args.out) if args.out else SKILL_ROOT / "个人世界观框架_当前版.md"
    parts = [EXPORT_NOTE]
    parts.append(f"> 版本：{current_version()} ｜ 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n---\n\n")
    for fname in ["_index.md"] + COMPONENT_FILES:
        lines = read_text(CONTENT_DIR / fname).splitlines(keepends=True)
        if lines and META_RE.match(lines[0].strip()):
            lines = lines[1:]
        parts.append("".join(lines))
        parts.append("\n---\n\n")
    write_text(out, "".join(parts))
    print(f"已导出：{out}（{len(''.join(parts))} 字符）")
    return 0


def _selftest_core(root: Path) -> bool:
    content = root / "content"
    backup = root / "backup"
    index = content / "_index.md"
    comp = content / "01_背景.md"
    changelog = root / "CHANGELOG.md"
    try:
        content.mkdir(parents=True)
        backup.mkdir()
        write_text(index, "<!-- meta: component=00_索引, version=v0.0.0, updated=2026-10-13 -->\n"
                         "# 总入口\n\n## 组件注册表\n\n| x |\n|---|\n\n## 读取指引\n\n见 CHANGELOG。\n")
        for i, fname in enumerate(COMPONENT_FILES, 1):
            write_text(content / fname,
                       f"<!-- meta: component={fname[:-3]}, updated=2026-10-13, summary=测试{i} -->\n"
                       f"# {fname[:-3]}\n\n条目{i}。\n")

        assert current_version(index) == "v0.0.0"
        assert bump_version("v0.0.0", "patch") == "v0.0.1"
        assert bump_version("v1.9.9", "minor") == "v1.10.0"
        assert bump_version("v1.2.3", "major") == "v2.0.0"
        assert changelog_latest_version(changelog) == ""

        # 无快照 → 全部视为改动
        assert collect_changes(content, None) == COMPONENT_FILES

        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        snap = backup / stamp
        snap.mkdir()
        shutil.copytree(content, snap / "content")
        assert latest_snapshot(backup) == snap

        # 只改一个文件 → 只报它
        assert collect_changes(content, snap) == []
        write_text(comp, read_text(comp).replace("条目1", "条目一。⏳ 悬置。"))
        assert collect_changes(content, snap) == ["01_背景.md"]

        # meta updated 自动推进
        update_meta_updated(comp, "2030-01-01")
        assert "updated=2030-01-01" in read_text(comp).splitlines()[0]

        # 提交流程
        set_version_in_index("v0.0.1", index)
        rebuild_registry_in_index(content)
        changelog_append("v0.0.1", "selftest 提交", "01_背景.md", "AI 提案", changelog)
        assert "v0.0.1" in read_text(index)
        assert changelog_latest_version(changelog) == "v0.0.1"
        assert "测试1" in read_text(index), "注册表应含 summary"

        # diff
        write_text(comp, read_text(comp).replace("条目一", "条目二"))
        old = read_text(snap / "content" / "01_背景.md").splitlines()
        new = read_text(comp).splitlines()
        diff = list(difflib.unified_diff(old, new, lineterm=""))
        assert any("条目二" in l for l in diff)

        # audit 在健康结构上不应有 FAIL
        issues = audit_core(root)
        fails = [i for i in issues if i[0] == "FAIL"]
        assert not fails, f"健康结构不应 FAIL：{fails}"
        assert any(code == "PENDING" for _, code, _ in issues)

        # audit 能抓到注册表漂移
        write_text(index, read_text(index).replace("测试1", "测试X"))
        issues2 = audit_core(root)
        assert any(code == "REGISTRY_STALE" for _, code, _ in issues2), "应抓到注册表漂移"

        # audit 能抓到版本漂移
        set_version_in_index("v9.9.9", index)
        issues3 = audit_core(root)
        assert any(code == "VERSION_DRIFT" for _, code, _ in issues3), "应抓到版本漂移"

        # export
        out = root / "export_test.md"
        write_text(out, EXPORT_NOTE + read_text(comp))
        assert "生成物勿手改" in read_text(out)
        return True
    except Exception as e:
        print(f"SELFTEST FAIL: {e!r}")
        return False


def cmd_selftest(_args) -> int:
    with tempfile.TemporaryDirectory(prefix="worldview-selftest-") as tmp:
        ok = _selftest_core(Path(tmp))
    print("SELFTEST OK" if ok else "SELFTEST FAIL")
    return 0 if ok else 1


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="worldview-setting 维护脚本（纯标准库）")
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("status", help="版本/文件状态/悬置项统计")
    sub.add_parser("audit", help="体检：结构/版本/注册表/悬置/时效/占位符（不查语义冲突）")

    pc = sub.add_parser("commit", help="提交一次增量更新（默认演练）")
    pc.add_argument("message", help="改动说明")
    pc.add_argument("--files", nargs="*", default=None, help="声明的改动文件（与实际不符会拒绝提交）")
    pc.add_argument("--bump", choices=["patch", "minor", "major"], default="patch")
    pc.add_argument("--by", default=None, help="确认方式（本人确认/AI 提案）")
    pc.add_argument("--confirmed", action="store_true", help="真执行（缺省为演练）")

    pd = sub.add_parser("diff", help="对比当前内容与某次备份快照")
    pd.add_argument("backup", help="backup/ 下的快照目录名")

    pe = sub.add_parser("export", help="合并导出单文件汇总版")
    pe.add_argument("--out", default=None, help="输出路径（默认 skill 根目录）")

    sub.add_parser("selftest", help="临时目录干跑全部机制")

    return p


def main(argv=None) -> int:
    ensure_utf8()
    args = build_parser().parse_args(argv)
    if args.cmd == "status":
        return cmd_status(args)
    if args.cmd == "audit":
        return cmd_audit(args)
    if args.cmd == "commit":
        return cmd_commit(args)
    if args.cmd == "diff":
        return cmd_diff(args)
    if args.cmd == "export":
        return cmd_export(args)
    if args.cmd == "selftest":
        return cmd_selftest(args)
    build_parser().print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())

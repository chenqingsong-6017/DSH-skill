# -*- coding: utf-8 -*-
"""复核文本文件尺寸与记忆格式，用于记忆/人设/配置类文件的体检。

用法:
  python check_chars.py <文件1> [<文件2> ...] [--limit N] [--soul] [--memory]

选项:
  --limit N    设字符数上限（如 4000），超限标 [OVER-LIMIT]
  --soul       按 SOUL.md 启发式检查行数：理想 ≤80 行，81-150 偏长，>150 臃肿待减
  --memory     记忆格式体检：查「顶层嵌套代码块」「空标题」两类翻车（对应 v3.7 去嵌套/清空标题教训）

示例:
  python check_chars.py "MEMORY.md" --limit 4000 --memory
  python check_chars.py "SOUL.md" --soul
  python check_chars.py "a.md" "b.md" --limit 4000

输出（每行一个文件，LLM 友好；全部达标返回 0，否则 2）:
  chars=2258  bytes=5013  lines=55  limit=4000  used=56.5%  memfmt=OK  [OK]
  chars=3200  bytes=7000  lines=90   soul=OK(≤80理想)  [OK]
"""
import re
import sys


# 记忆格式体检：两类历史翻车
# ① 顶层嵌套代码块：整个文件被 ``` 包裹（v3.7「去嵌套」教训）
# ② 空标题：某标题后（跳过空行）紧跟同级/更高级标题，或直到文件尾无内容（v3.7「清空标题」教训）
HEADER = re.compile(r"^(#{1,6})\s")


def check_memory_format(t: str) -> list:
    problems = []
    stripped = t.strip()
    if stripped.startswith("```") and stripped.endswith("```"):
        problems.append("顶层嵌套代码块（整个文件被 ``` 包裹，需去嵌套）")
    lines = t.split("\n")
    for i, line in enumerate(lines):
        m = HEADER.match(line)
        if not m:
            continue
        level = len(m.group(1))
        j = i + 1
        while j < len(lines) and lines[j].strip() == "":
            j += 1
        if j >= len(lines):
            problems.append(f"空标题：第 {i+1} 行「{line.strip()}」后无内容（到文件尾）")
            continue
        m2 = HEADER.match(lines[j].strip())
        if m2 and len(m2.group(1)) <= level:
            problems.append(f"空标题：第 {i+1} 行「{line.strip()}」后紧跟同级/上级标题")
    return problems


def check(path: str, limit, soul: bool, memory: bool) -> int:
    try:
        with open(path, encoding="utf-8") as f:
            t = f.read()
    except OSError as e:
        print(f"[ERROR] {path}: {e}")
        return 2

    chars = len(t)
    lines = t.count("\n") + 1
    parts = [f"chars={chars}", f"bytes={len(t.encode('utf-8'))}", f"lines={lines}"]

    status = "OK"
    if limit is not None:
        pct = chars / limit * 100
        if chars > limit:
            status = "OVER-LIMIT"
        parts.append(f"limit={limit}")
        parts.append(f"used={pct:.1f}%")

    if soul:
        if lines <= 80:
            note = "soul=OK(≤80理想)"
        elif lines <= 150:
            note = "soul=WARN(81-150偏长)"
        else:
            note = "soul=OVER(>150臃肿待减)"
        parts.append(note)
        if lines > 150:
            status = "OVER-LIMIT"

    if memory:
        probs = check_memory_format(t)
        if probs:
            status = "OVER-LIMIT"
            parts.append(f"memfmt=FAIL({len(probs)})")
            for p in probs:
                print(f"  [memfmt] {path}: {p}")
        else:
            parts.append("memfmt=OK")

    parts.append(f"[{status}]")
    print("  ".join(parts))
    return 0 if status == "OK" else 2


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1

    limit = None
    soul = False
    memory = False
    paths = []
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--limit":
            limit = int(args[i + 1])
            i += 2
            continue
        if a.startswith("--limit="):
            limit = int(a.split("=", 1)[1])
            i += 1
            continue
        if a == "--soul":
            soul = True
            i += 1
            continue
        if a == "--memory":
            memory = True
            i += 1
            continue
        paths.append(a)
        i += 1

    if not paths:
        print(__doc__)
        return 1

    rc = 0
    for p in paths:
        rc = max(rc, check(p, limit, soul, memory))
    return rc


if __name__ == "__main__":
    sys.exit(main())

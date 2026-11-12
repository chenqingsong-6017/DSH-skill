# -*- coding: utf-8 -*-
"""复核文本文件的字符数（用于记忆/人设类配置文件的尺寸检查）。

用法:
  python check_chars.py <文件路径> [上限字符数]

示例:
  python check_chars.py "C:/Users/xxx/.workbuddy/user-xxx-personal/MEMORY.md" 4000
  python check_chars.py "C:/Users/xxx/.workbuddy/user-xxx-personal/SOUL.md"

输出示例:
  chars=2258  bytes=5013  lines=55  limit=4000  used=56.5%  [OK]
"""
import sys


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    path = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else None

    with open(path, encoding='utf-8') as f:
        t = f.read()

    chars = len(t)
    line = f"chars={chars}  bytes={len(t.encode('utf-8'))}  lines={t.count(chr(10)) + 1}"
    if limit:
        pct = chars / limit * 100
        status = "OK" if chars <= limit else "OVER-LIMIT"
        line += f"  limit={limit}  used={pct:.1f}%  [{status}]"
    print(line)
    return 0


if __name__ == '__main__':
    sys.exit(main())

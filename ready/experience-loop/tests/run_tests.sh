#!/bin/sh
# experience-loop 回归自检：展开夹具 → 编译 assets 下全部脚本 → 在夹具工作区各跑一遍 → 清理。
# 用法：sh tests/run_tests.sh
# 判读：把输出与同目录的「预期输出.md」对照；关键行不一致即视为回归。
#
# ⚠ 夹具是**临时展开**的（`make_fixture.py`），不在包内保留嵌套目录——
#    因为平台限制 Skill 包最多两级目录，夹具的嵌套结构必须运行时生成。
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
A="$HERE/../assets"
FIX="$PWD/.exp-loop-fixture"
FIXM="$PWD/.exp-loop-fixture-mount"

echo "===== 0 · 展开夹具 ====="
python3 "$HERE/make_fixture.py" --dest "$FIX"

echo
echo "===== 1 · 编译检查（assets 下全部脚本）====="
for f in "$A"/*.py; do
  python3 -m py_compile "$f" && echo "OK   $(basename "$f")"
done
# py_compile 会在 assets/ 下生成 __pycache__（本机多字节码缓存）；跑完清掉，保持技能目录干净
python3 -c "import os,shutil; d=os.path.join('$A','__pycache__'); shutil.rmtree(d) if os.path.isdir(d) else None; print('已清理 assets/__pycache__' if not os.path.isdir(d) else '')"

echo
echo "===== 2 · 回执统计（dry-run，只报不改）====="
python3 "$A/回执统计.py" "$FIX"

echo
echo "===== 3 · 检索痕迹检查（只读）====="
python3 "$A/检索痕迹检查.py" "$FIX"

echo
echo "===== 4 · 索引一致性检查（盘点，--cards 只报不判）====="
python3 "$A/索引一致性检查.py" "$FIX" --cards

echo
echo "===== 5 · 整理工具 scan（只读；会在夹具内写 .workbuddy/archive/清单.json）====="
python3 "$A/整理工具.py" scan --root "$FIX"

echo
echo "===== 6 · purge 下界校验（P1）—— --days 0 必须被拒 ====="
if python3 "$A/整理工具.py" purge --root "$FIX" --days 0; then
  echo "❌ 回归失败：--days 0 未被拒绝（它会一次删光整个隔离区）"
  exit 1
else
  echo "OK   --days 0 已被拒绝（退出码非 0）"
fi

echo
echo "===== 7 · purge --batch（P2）——按批次精确清，dry-run 只列指定批次 ====="
python3 "$A/整理工具.py" purge --root "$FIX" --batch 2020-01-01

echo
echo "===== 8 · 产出物分类.py report（判型对账，只读）====="
python3 "$A/产出物分类.py" report --root "$FIX"

echo
echo "===== 9 · 挂载模式夹具（描述性卡名区，3.4.0）· 索引一致性检查 ====="
python3 "$HERE/make_fixture.py" --style mount --dest "$FIXM"
EXP_LOOP_SKILLS_DIR="$FIXM/.fake-skills" python3 "$A/索引一致性检查.py" "$FIXM"

echo
echo "===== 9b · 挂载制载体总表（--carriers；3.7.1 修复点：旧版恒 0 条）====="
EXP_LOOP_SKILLS_DIR="$FIXM/.fake-skills" python3 "$A/索引一致性检查.py" "$FIXM" --carriers

echo
echo "===== 10 · 挂载模式夹具 · 回执统计（dry-run）====="
python3 "$A/回执统计.py" "$FIXM"

echo
echo "===== 收尾 · 清理夹具 ====="
python3 "$HERE/make_fixture.py" --clean --dest "$FIX"
python3 "$HERE/make_fixture.py" --clean --dest "$FIXM"

echo
echo "全部跑完（**只读检查，未改技能本体**）。⚠ 若产物与预期不符，先看 预期输出.md 的判读要点。"

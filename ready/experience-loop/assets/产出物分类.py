#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""产出物分类工具（单工作区，通用于任意工作区根目录）

职责：给工作区里的每个文件判一个**类型**（回答「这是什么」，不回答「还有没有用」）。

用法：
  python3 产出物分类.py report          --root <工作区> [--json <out>]
  python3 产出物分类.py quarantine-list --root <工作区> [--commit]

纪律：
  * `report` 只读；`quarantine-list` 默认 dry-run，加 `--commit` 才写 `_按类型清单.md`。
  * 不调用 shell 的 rm；**不移动、不删除任何文件**（只做「判型」与「出清单」）。
  * 判定顺序（6 步，不可换）：排除集 → 声明 → 名字/扩展名 → 目录兜底 → 名字 → 默认过程稿。
    完整判据与声明写法见 `assets/清理手册.md`「产出物类型体系」节 与 `assets/归档规则模板.md`。

类型值域（封闭，8 类 ＋ 1 排除集）：
  交付物 / 过程稿 / 脚本 / 说明与规则 / 机制台账 / 备份件 / 编译副产物 / 原始材料
  排除集：应用内部残留（另「原始材料」虽在 8 类内，但按红线永不删）
"""
import argparse
import collections
import json
import os
import re
import sys
from datetime import datetime

TYPES = ('交付物', '过程稿', '脚本', '说明与规则', '机制台账', '备份件', '编译副产物', '原始材料')
EXCLUDED = ('原始材料', '应用内部残留')

RAW_DIRS = ('上传材料', '参考材料', '扫描件', '原始材料', '00_原始材料', '00_输入')
# 目录兜底关键词（**段名子串匹配**，兼容 `02_交付物/`、`01_过程产出/` 这类带序号前缀的命名）。
# ⚠ 交付物侧**不得**用裸「产出」做子串匹配——`01_过程产出` 含「产出」，会被误判成交付物。
DELIV_DIRS = ('产出材料', '交付物', '交付成果')
PROC_DIRS = ('过程产出', '过程稿', '过程', '草稿', '试算', '中间产物')
APP_RESIDUE = ('file-history', 'artifact-index', 'changes-index', 'traces', 'projects')
QUAR = '_隔离区'
# folder-lists 用：不生成清单的顶层目录（机制目录本身同质，分类没有信息量）
# ⚠ 挂载型工作区（自有三段式目录、另用 `_经验库/`／`_索引/`）按**其既有命名**排除
EXCLUDE_TOP = {'.workbuddy', '_隔离区', '.git', '经验库', '_经验库', '_索引', '复用回执', '长期记忆录'}


def target_folders(root):
    """folder-lists 的目标文件夹（相对路径）＝ 每个 `任务/<任务>` ＋ 每个顶层主题目录。"""
    out = []
    task = os.path.join(root, '任务')
    if os.path.isdir(task):
        for n in sorted(os.listdir(task)):
            if os.path.isdir(os.path.join(task, n)) and not n.startswith('_'):
                out.append(os.path.join('任务', n))
    for n in sorted(os.listdir(root)):
        d = os.path.join(root, n)
        if os.path.isdir(d) and n not in EXCLUDE_TOP and not n.startswith('.') and n != '任务':
            out.append(n)
    return out

RE_BAK = re.compile(r'(\.bak|\.backup|backup_|_备份|备份清单|压缩前|~\$|\.tmp$)', re.I)
RE_LEDGER = re.compile(r'(_索引|台账|回执|_检查点|_载体总表|迁移日志|删除日志|清单\.json|'
                       r'清理清单|批次清单|样本映射|按类型清单|_gone_sessions|_index_move_log)')
RE_RULE = re.compile(r'(README|ARCHIVE|^_说明|^_方案|手册|规范|模板|母版|SKILL\.md|目录组织规则|归档规则|任务交接)', re.I)
RE_DRAFT = re.compile(r'(草稿|试算|draft|v0\d|旧版|历史版|未完成)', re.I)
RE_HISTVER = re.compile(r'(_v\d\.\d|V\d+(\.\d+)?版|\(\d+\)|_\d{6,})', re.I)
RE_RAWNAME = re.compile(r'(扫描|图纸|施工图|合同|发票|证书|执照|报表|截图|照片|不动产权|原始|原件)')

SCRIPT_EXT = {'.py', '.sh', '.js', '.ts', '.ps1', '.bat', '.plist'}
RAW_EXT = {'.dwg', '.dxf'}

# 声明行：`- [交付物] 文件名 —— 说明`  或 表格行首列含 [类型]
RE_DECL = re.compile(r'\[\s*(%s)\s*\]\s*([^—|｜\n]*)' % '|'.join(TYPES))


def parts(rel):
    return rel.replace('\\', '/').split('/')


def has(rel, names):
    return any(p in names for p in parts(rel))


def has_any(rel, keys):
    """段名**包含**关键词即命中（与 `has` 的全等匹配互补，兼容带序号前缀的目录名）。"""
    return any(k in p for p in parts(rel) for k in keys)


def strip_quar(rel):
    ps = parts(rel)
    if ps and ps[0] == QUAR:
        return True, '/'.join(ps[2:]) if len(ps) > 2 else ''
    return False, rel


def parse_declaration(wsd, rel):
    """向上找最近的 `_说明.md`，解析「产出清单」里的 [类型] 前缀 → {basename: 类型}"""
    cur = os.path.dirname(os.path.join(wsd, rel))
    for _ in range(8):
        f = os.path.join(cur, '_说明.md')
        if os.path.isfile(f):
            try:
                txt = open(f, encoding='utf-8').read()
            except OSError:
                return {}
            out = {}
            for m in RE_DECL.finditer(txt):
                t, name = m.group(1), m.group(2).strip().strip('`* ')
                base = os.path.basename(name)
                if base:
                    out[base] = t
            return out
        if os.path.realpath(cur) == os.path.realpath(wsd):
            break
        nxt = os.path.dirname(cur)
        if nxt == cur:
            break
        cur = nxt
    return {}


def classify(wsd, rel, fn, ext, decl):
    inq, r = strip_quar(rel)
    # 0 排除：应用内部残留
    if has(r, APP_RESIDUE):
        return '应用内部残留', inq
    if '.workbuddy' in parts(r):
        segs = parts(r)
        nxt = segs[segs.index('.workbuddy') + 1] if len(segs) > segs.index('.workbuddy') + 1 else ''
        if nxt.startswith('backup'):
            return '备份件', inq
        if nxt in ('memory', 'archive'):
            return '机制台账', inq
        return '应用内部残留', inq
    # 1 排除：原始材料
    if has(r, RAW_DIRS) or ext in RAW_EXT:
        return '原始材料', inq
    # 2 声明优先（值域校验）
    d = decl.get(fn)
    if d in TYPES:
        return d, inq
    # 3 名字 / 扩展名
    if '__pycache__' in r or ext == '.pyc':
        return '编译副产物', inq
    if RE_BAK.search(fn):
        return '备份件', inq
    if RE_LEDGER.search(fn):
        return '机制台账', inq
    if RE_RULE.search(fn):
        return '说明与规则', inq
    if fn.startswith('_'):
        # 机制文件惯例：下划线开头（`_说明`/`_方案` 已被上面规则接走）
        return '机制台账', inq
    if has(r, ('经验库', '复用回执')):
        return '机制台账', inq
    if ext in SCRIPT_EXT:
        return '脚本', inq
    # 4 目录兜底（**子串匹配**：兼容 `产出材料/`、`02_交付物/`、`01_过程产出/` 等命名）
    if has_any(r, DELIV_DIRS):
        return '交付物', inq
    if has_any(r, PROC_DIRS):
        return '过程稿', inq
    # 5 名字
    if RE_DRAFT.search(fn) or RE_HISTVER.search(fn):
        return '过程稿', inq
    # 6 保守默认
    return '过程稿', inq


def collect(root):
    rows = []
    decl_cache = {}
    for cur, dirs, files in os.walk(root):
        for fn in files:
            p = os.path.join(cur, fn)
            if os.path.islink(p):
                continue
            try:
                st = os.stat(p)
            except OSError:
                continue
            rel = os.path.relpath(p, root)
            key = os.path.dirname(rel)
            if key not in decl_cache:
                decl_cache[key] = parse_declaration(root, rel)
            ext = os.path.splitext(fn)[1].lower()
            t, inq = classify(root, rel, fn, ext, decl_cache[key])
            rows.append({'rel': rel, 'fn': fn, 'ext': ext, 'size': st.st_size,
                         'm': st.st_mtime, 'type': t, 'quar': inq})
    return rows


def fam_of(stem):
    s = stem
    for rx in (re.compile(r'[_\- ]?[vV]\d+(\.\d+)*'), re.compile(r'[_\- ]?\(\s*\d+\s*\)'),
               re.compile(r'[_\- ]?\d{8}'), re.compile(r'[_\- ]?\d{6}'),
               re.compile(r'(最终版|定稿版|修订版|第\d+版|新版|旧版|历史版|存档版)'),
               re.compile(r'[_\- ]?(副本|copy|old|bak|备份)'), re.compile(r'[_\- ]?草稿')):
        s = rx.sub('', s)
    return re.sub(r'[\s_\-]+', '', s)


def cmd_report(args):
    root = os.path.abspath(args.root)
    rows = collect(root)
    c, s = collections.Counter(), collections.Counter()
    for r in rows:
        c[r['type']] += 1
        s[r['type']] += r['size']

    print('产出物分类 · 现状对账（只读）  root=%s' % root)
    print('文件总数：%d   总体积：%.1f MB\n' % (len(rows), sum(r['size'] for r in rows) / 1048576))
    print('%-16s %6s %10s' % ('类型', '文件数', '体积'))
    for t in TYPES + ('应用内部残留',):
        print('%-16s %6d %9.1fMB' % (t, c[t], s[t] / 1048576))

    core = [r for r in rows if r['type'] not in EXCLUDED]
    print('\n产出物（排除原始材料与应用残留）：%d 个（%.1f%%）/ %.1f MB'
          % (len(core), 100.0 * len(core) / max(len(rows), 1), sum(r['size'] for r in core) / 1048576))

    # 疑似原始材料（未在 上传材料/ 等目录，但名字/路径像原件）
    sus = [r for r in core if RE_RAWNAME.search(r['fn'])]
    print('\n== ⚠ 疑似原始材料（当前判为产出物，但形似原件）%d 个／%.1f MB =='
          % (len(sus), sum(r['size'] for r in sus) / 1048576))
    print('   按扩展名：%s' % dict(collections.Counter(r['ext'] or '(无)' for r in sus).most_common(6)))
    print('   按顶层目录：%s' % dict(collections.Counter(parts(r['rel'])[0] for r in sus).most_common(6)))

    # 疑似旧版组（只在「非原始材料」里找）
    g = collections.defaultdict(list)
    for r in core:
        stem = os.path.splitext(r['fn'])[0]
        f = fam_of(stem)
        if f:
            g[(os.path.dirname(r['rel']), f, r['ext'])].append(r)
    multi = {k: v for k, v in g.items() if len(v) > 1}
    print('\n== ⚠ 疑似旧版组（同目录同族名 ≥2 份；**仅列事实，不自动降级**）%d 组／%d 个 =='
          % (len(multi), sum(len(v) for v in multi.values())))
    for k, v in list(multi.items())[:10]:
        print('   %-34s %s' % (k[0][:32] or '(根层)', ' ｜ '.join(x['fn'] for x in sorted(v, key=lambda y: -y['m']))))

    # 隔离区
    q = [r for r in rows if r['quar']]
    if q:
        qc = collections.Counter(r['type'] for r in q)
        print('\n== 隔离区 %d 个 按类型 ==' % len(q))
        for t, n in qc.most_common():
            print('   %-16s %5d' % (t, n))

    if args.json:
        with open(args.json, 'w', encoding='utf-8') as f:
            json.dump(rows, f, ensure_ascii=False)
        print('\n明细已写入：%s（供脚本消费，勿整份读入对话）' % args.json)


def cmd_quarantine_list(args):
    root = os.path.abspath(args.root)
    quar = os.path.join(root, QUAR)
    if not os.path.isdir(quar):
        print('没有隔离区。')
        return
    rows = collect(root)
    by_batch = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in rows:
        if not r['quar']:
            continue
        ps = parts(r['rel'])
        batch = ps[1] if len(ps) > 1 else '(无批次)'
        rest = '/'.join(ps[2:]) if len(ps) > 2 else r['fn']
        by_batch[batch][r['type']].append((rest, r))
    n = 0
    for batch in sorted(by_batch):
        out = os.path.join(quar, batch, '_按类型清单.md')
        lines = ['# 隔离区 · 按类型清单（批次 %s）' % batch,
                 '',
                 '> 由 `产出物分类.py quarantine-list` 生成。**不改动任何文件路径**，仅供批量裁决。',
                 '> 生成时间：%s' % datetime.now().strftime('%Y-%m-%d %H:%M'), '']
        tot = sum(len(v) for v in by_batch[batch].values())
        lines.append('合计 **%d** 个文件；**类型不表示"能删"**——处置见本区 `ARCHIVE.md` 生命周期表。' % tot)
        lines.append('')
        for t, items in sorted(by_batch[batch].items(), key=lambda x: -len(x[1])):
            lines.append('## %s（%d 个）' % (t, len(items)))
            lines.append('')
            for rest, r in sorted(items):
                lines.append('- `%s`（%.1f KB）' % (rest, r['size'] / 1024))
            lines.append('')
        print('%s  %s' % ('WRITE' if args.commit else 'DRY  ', os.path.relpath(out, root)))
        if args.commit:
            with open(out, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines) + '\n')
        n += 1
    print('\n共 %d 个批次（commit=%s）。%s' % (n, args.commit,
          '' if args.commit else '这是预演，加 --commit 才会写入 _按类型清单.md。'))


def cmd_folder_lists(args):
    """为每个任务／主题文件夹生成 `_类型清单.md`——让类型在工作区里「看得见」。"""
    root = os.path.abspath(args.root)
    rows = collect(root)
    n = 0
    for rel in target_folders(root):
        base = rel + '/'
        mine = [r for r in rows if r['rel'].startswith(base)]
        if not mine:
            continue
        flat, sub = [], collections.defaultdict(list)
        for r in mine:
            rest = r['rel'][len(base):]
            (sub[rest.split('/')[0]].append(r) if '/' in rest else flat.append(r))
        by = collections.defaultdict(list)
        for r in flat:
            by[r['type']].append(r)

        L = ['# 类型清单 · %s' % rel, '',
             '> 由 `assets/产出物分类.py` 判型生成（值域见工作区 `ARCHIVE.md` 的类型表）。',
             '> **只列类型，不动任何文件**——类型**不表示"能删"**，处置见 `ARCHIVE.md` 生命周期表。',
             '> 生成 %s ｜ 本层平铺 **%d** 个 ｜ 子目录 **%d** 个'
             % (datetime.now().strftime('%Y-%m-%d %H:%M'), len(flat), len(sub)), '']
        if len(flat) > 6:
            L += ['⚠ 本层平铺 %d 个（>6）——建议按类型建子目录：'
                  '`产出材料/` 或 `02_交付物/`（交付物）｜`过程/`（过程稿）｜`scripts/`（脚本）。', '']
        L += ['## 本层平铺（按类型）', '']
        if not flat:
            L.append('_（根层无文件，全部已在子目录。）_')
        for t, items in sorted(by.items(), key=lambda x: -len(x[1])):
            L += ['### %s（%d）' % (t, len(items)), '']
            for r in sorted(items, key=lambda x: x['fn']):
                L.append('- `%s`（%.1f KB）' % (r['fn'], r['size'] / 1024))
            L.append('')
        if sub:
            L += ['## 子目录概览', '']
            for k in sorted(sub):
                c = collections.Counter(x['type'] for x in sub[k])
                L.append('- `%s/` %d 个 → %s'
                         % (k, len(sub[k]), '、'.join('%s %d' % (a, b) for a, b in c.most_common())))
            L.append('')

        out = os.path.join(root, rel, '_类型清单.md')
        print('%s  %s（平铺 %d ／ 子目录 %d）'
              % ('WRITE' if args.commit else 'DRY  ', os.path.relpath(out, root), len(flat), len(sub)))
        if args.commit:
            with open(out, 'w', encoding='utf-8') as f:
                f.write('\n'.join(L).rstrip() + '\n')
        n += 1
    print('\n共 %d 个文件夹（commit=%s）。%s'
          % (n, args.commit, '' if args.commit else '这是预演，加 --commit 才写 _类型清单.md。'))


def main():
    ap = argparse.ArgumentParser(description='产出物分类工具（判型／出清单，单工作区）')
    ap.add_argument('cmd', choices=['report', 'quarantine-list', 'folder-lists'])
    ap.add_argument('--root', default='.')
    ap.add_argument('--json')
    ap.add_argument('--commit', action='store_true')
    args = ap.parse_args()
    {'report': cmd_report, 'quarantine-list': cmd_quarantine_list,
     'folder-lists': cmd_folder_lists}[args.cmd](args)


if __name__ == '__main__':
    main()

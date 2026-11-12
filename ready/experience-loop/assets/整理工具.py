#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""工作区整理工具（纯标准库，无第三方依赖）

子命令：
  scan        只读扫描 -> .workbuddy/archive/清单.json，并打印统计
  dup         列出 md5 完全一致的重复文件组
  move        按 map.json 搬移（写迁移日志）
  quarantine  按 list.txt 把文件移入 _隔离区/YYYY-MM-DD/（写删除日志）
  restore     从隔离区还原回原路径
  rollback    按迁移日志反向搬回
  purge       清理隔离区中超过 N 天（默认 30）或**指定批次**（`--batch`，逗号分隔）的批次
              （唯一物理删除：逐文件写删除日志）

安全约定（不可绕过）：
  1. 除 scan / dup 外，所有写操作默认 dry-run，必须显式 --commit 才真正执行。
  2. 全程使用 Python 的 shutil.move / os.remove，绝不调用 shell 的 rm
     （本环境 rm 是坏 shim，会报 bad interpreter）。
  3. 黑名单路径（.git / .workbuddy / 上传材料 / 经验库 / 复用回执 / _隔离区）
     在任何子命令下都被跳过，永不进待删列表。
  4. **路径护栏**：所有写操作的 src / dst 一律经 resolve() 校验，必须落在 realpath(root) 之内；
     `../` 逃逸与绝对路径一律**拒绝并告警**，不执行。map.json / list.txt 由 AI 生成，
     `os.path.join(root, '../../x')` 与绝对路径都能越界，故不能只靠黑名单。
  5. **搬移可分批回滚**：迁移日志带 batch 字段（默认当天）；`rollback --batch <日期>` 只回滚该批次；
     不带 --batch 时打印"将回滚全部 N 条"警告，避免误回滚历史批次。
  6. **purge 是唯一物理删除**：不经回收站、不可恢复。执行前必须 dry-run 预演并人工核对批次清单；
     `rmtree` 之前先把该批次**每个文件**写入 `.workbuddy/archive/删除日志.jsonl`（`op=purge`），
     日志是该操作仅存的凭据。
"""

import argparse
import hashlib
import json
import os
import shutil
import sys
import time
from collections import defaultdict
from datetime import datetime

SKIP_DIRS = {'.git', 'node_modules', '.workbuddy', '_隔离区', '__pycache__', '.venv', 'venv'}
BLACKLIST = ('.git', '.workbuddy', '上传材料', '经验库', '复用回执', '_隔离区')
ARCHIVE_DIR = os.path.join('.workbuddy', 'archive')
QUAR_ROOT = '_隔离区'
BIG_FILE = 50 * 1024 * 1024
LOG_MOVE = '迁移日志.jsonl'
LOG_DEL = '删除日志.jsonl'


def now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def md5_of(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def hash_of(path):
    """文件 → md5；**目录 → 空串**。

    ⚠ 为什么必须单列一个函数：`os.path.getsize(<目录>)` **不报错**（返回目录项字节数，通常 4096
    ＜ `BIG_FILE`），于是「先判大小再算 md5」的写法**骗过了前置校验**，把目录送进 `md5_of` 的
    `open()` ⇒ **`IsADirectoryError` 直接崩**（在某挂载型区隔离 `__pycache__` 时实测）。
    而 L1 判据里的 `__pycache__`／`node_modules`／`dist`／`build` **全是目录**——等价于
    「最常见的可清项一个都清不了」；更坏的是 **dry-run 不报错**（预演不算 md5），只在 `--commit` 炸，
    且崩在半路（`os.makedirs` 已建好父目录骨架）⇒ 现场看起来像"移动了一部分"。
    """
    if os.path.isdir(path):
        return ''
    try:
        return md5_of(path) if 0 < os.path.getsize(path) < BIG_FILE else ''
    except OSError:
        return ''


def is_blacklisted(rel):
    parts = rel.replace('\\', '/').split('/')
    return any(p in BLACKLIST for p in parts)


def blacklisted_src(rel):
    """P3 · move 的「来源」例外：**允许 src 位于 `_隔离区/` 内**（用于抢救凭据／移出该留的东西）。

    其余黑名单（`.workbuddy`／`上传材料`／`经验库`／`复用回执`／`.git`）**照旧拒绝**。
    dst 侧仍走完整黑名单——隔离区依旧不能作为写入目标。
    """
    parts = rel.replace('\\', '/').split('/')
    return any(p in BLACKLIST and p != QUAR_ROOT for p in parts)


def readable_text_ext(ext):
    return ext in ('.md', '.txt', '.json', '.jsonl', '.csv', '.py', '.sh', '.html', '.htm',
                   '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.yaml', '.yml')


RESIDUE_DIRS = ('file-history', 'artifact-index', 'changes-index', 'traces', 'projects')


def is_app_residue(rel):
    """应用内部数据（与产出物无关的机械残留）。P4 的「可读文本警示」要把它排除——
    否则一次报几百条 `.json`，**告警喊了狼来了、用户就学会忽略它**（等于没有告警）。"""
    return any(p in RESIDUE_DIRS for p in rel.replace('\\', '/').split('/'))


def resolve(root, rel, must_exist=False):
    """把 root 内的相对路径解析成绝对路径；**越界返回 None**。

    护栏理由：os.path.join(root, '../../x') 与绝对路径 /etc/x 都能逃出工作区，
    黑名单只按字符串匹配，挡不住这两种。故一律 realpath 后校验前缀。
    """
    root_abs = os.path.realpath(root)
    p = os.path.realpath(os.path.join(root_abs, rel))
    if p != root_abs and not p.startswith(root_abs + os.sep):
        return None
    if must_exist and not os.path.exists(p):
        return None
    return p


REL_REFUSED = []


def refuse(rel):
    print('拒绝（越出工作区，未执行）：%s' % rel)
    REL_REFUSED.append(rel)


def walk_files(root):
    rows = []
    for cur, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in files:
            full = os.path.join(cur, fn)
            if os.path.islink(full):
                continue
            try:
                st = os.stat(full)
            except OSError:
                continue
            rel = os.path.relpath(full, root)
            rows.append({
                'p': rel,
                's': st.st_size,
                'm': datetime.fromtimestamp(st.st_mtime).strftime('%Y-%m-%d'),
                'h': md5_of(full) if 0 < st.st_size < BIG_FILE else '',
            })
    return rows


def load_rows(root):
    path = os.path.join(root, ARCHIVE_DIR, '清单.json')
    if not os.path.exists(path):
        print('未找到清单，请先运行 scan')
        sys.exit(1)
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def append_log(root, name, record):
    d = os.path.join(root, ARCHIVE_DIR)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, name), 'a', encoding='utf-8') as f:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')


def read_log(root, name):
    path = os.path.join(root, ARCHIVE_DIR, name)
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def unique_dst(dst):
    if not os.path.exists(dst):
        return dst
    base, ext = os.path.splitext(dst)
    i = 1
    while os.path.exists('%s-%d%s' % (base, i, ext)):
        i += 1
    return '%s-%d%s' % (base, i, ext)


def human(n):
    if n < 1024:
        return '%dB' % n
    if n < 1024 * 1024:
        return '%.1fKB' % (n / 1024)
    if n < 1024 * 1024 * 1024:
        return '%.1fMB' % (n / (1024 * 1024))
    return '%.2fGB' % (n / (1024 * 1024 * 1024))


def group_overview(rows, depth):
    """按路径前 depth 段分组，并统计组内直接子目录构成。

    分层工作区（按项目/标的/客户聚合）走扁平清单看不出"每个组里长什么样"，
    D1 诊断需要这个视图来判断任务归属。depth=0 表示不分组。
    """
    groups = defaultdict(lambda: {'n': 0, 's': 0, 'sub': defaultdict(lambda: [0, 0])})
    if not depth or depth < 1:
        return groups
    for r in rows:
        parts = r['p'].replace('\\', '/').split('/')
        if len(parts) <= depth:
            key, sub = '(根层)', '(根层)'
        else:
            key = '/'.join(parts[:depth]) + '/'
            rest = parts[depth:]
            sub = (rest[0] + '/') if len(rest) > 1 else '(根层)'
        g = groups[key]
        g['n'] += 1
        g['s'] += r['s']
        g['sub'][sub][0] += 1
        g['sub'][sub][1] += r['s']
    return groups


def print_groups(rows, depth, limit=25):
    groups = group_overview(rows, depth)
    if len(groups) <= 1:
        return
    print('\n目录分组概览（按前 %d 层路径分组，供 D1 判断任务归属）：' % depth)
    ordered = sorted(groups.items(), key=lambda x: -x[1]['s'])
    for k, g in ordered[:limit]:
        print('  %-34s %4d 个  %9s' % (k, g['n'], human(g['s'])))
        if len(g['sub']) > 1:
            subs = ' · '.join('%s %d' % (s, c[0]) for s, c in
                              sorted(g['sub'].items(), key=lambda x: -x[1][0]))
            print('       组成：%s' % subs)
    if len(ordered) > limit:
        print('  …另有 %d 组未列出（完整数据见 清单.json，勿整份读进对话）' % (len(ordered) - limit))


def cmd_scan(args):
    root = args.root
    rows = walk_files(root)
    out = os.path.join(root, ARCHIVE_DIR)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, '清单.json'), 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False)

    total = len(rows)
    size = sum(r['s'] for r in rows)
    ext = defaultdict(lambda: [0, 0])
    for r in rows:
        e = os.path.splitext(r['p'])[1].lower() or '(无扩展名)'
        ext[e][0] += 1
        ext[e][1] += r['s']

    print('扫描完成（只读，未修改任何文件）')
    print('  文件总数：%d    总体积：%s' % (total, human(size)))
    print('  清单已写入：%s' % os.path.join(ARCHIVE_DIR, '清单.json'))
    print('\n类型分布 Top10：')
    for e, (c, s) in sorted(ext.items(), key=lambda x: -x[1][1])[:10]:
        print('  %-14s %4d 个   %s' % (e, c, human(s)))
    print('\n最大文件 Top10：')
    for r in sorted(rows, key=lambda x: -x['s'])[:10]:
        print('  %-10s %s' % (human(r['s']), r['p']))

    dup = dup_groups(rows)
    ndup = sum(1 for v in dup.values() if len(v) > 1)
    waste = 0
    for v in dup.values():
        if len(v) > 1:
            sz = next((r['s'] for r in rows if r['p'] == v[0]), 0)
            waste += sz * (len(v) - 1)
    print('\n重复组：%d 组，可回收约 %s（详见 dup 子命令）' % (ndup, human(waste)))
    print_groups(rows, getattr(args, 'group_depth', 1))
    print(quarantine_hint(root))
    print('\n下一步：运行 dup 查看重复明细，再据以拟定整理方案。本工具不会自动删除任何东西。')


def quarantine_hint(root):
    """P5 · `scan` 跳过 `_隔离区/` 却不吭声 ⇒ 整理会系统性漏掉整块。此处在报告末尾点名。"""
    quar = os.path.join(root, QUAR_ROOT)
    if not os.path.isdir(quar):
        return ''
    cnt = 0
    sz = 0
    oldest = None
    batches = 0
    for b in sorted(os.listdir(quar)):
        bdir = os.path.join(quar, b)
        if not os.path.isdir(bdir):
            continue
        try:
            datetime.strptime(b, '%Y-%m-%d')
        except ValueError:
            continue
        batches += 1
        oldest = b if oldest is None else min(oldest, b)
        for cur, _, files in os.walk(bdir):
            for f in files:
                cnt += 1
                try:
                    sz += os.path.getsize(os.path.join(cur, f))
                except OSError:
                    pass
    if not batches:
        return ''
    due = datetime.fromtimestamp(datetime.strptime(oldest, '%Y-%m-%d').timestamp() + 30 * 86400)
    return ('\n⚠ 本轮扫描**不含** `_隔离区/`（该目录在 SKIP_DIRS 内、原报告里不出现）：\n'
            '  隔离区：%d 个批次／%d 个文件／%s，最早到期 %s（+30 天）。\n'
            '  ⇒「已整理完毕」不等于隔离区已处理；清理见 `清理手册.md` D3。'
            % (batches, cnt, human(sz), due.strftime('%Y-%m-%d')))


def dup_groups(rows):
    g = defaultdict(list)
    for r in rows:
        if r['h']:
            g[r['h']].append(r['p'])
    return g


def cmd_dup(args):
    path = os.path.join(args.root, ARCHIVE_DIR, '清单.json')
    if not os.path.exists(path):
        print('未找到清单，先自动扫描：\n')
        cmd_scan(args)
        print('')
    rows = load_rows(args.root)
    g = dup_groups(rows)
    idx = {r['p']: r for r in rows}
    n = 0
    for h, paths in g.items():
        if len(paths) < 2:
            continue
        n += 1
        print('\n[%d] md5 %s  大小 %s  共 %d 份' % (n, h[:10], human(idx[paths[0]]['s']), len(paths)))
        for p in sorted(paths, key=lambda x: idx[x]['m']):
            print('    %s  %s' % (idx[p]['m'], p))
    if n == 0:
        print('没有发现内容完全相同的文件。')
    else:
        print('\n共 %d 组。注意：只证明内容相同，不证明「没用」——保留哪一份由用户决定。' % n)


def cmd_move(args):
    root = args.root
    with open(args.map, encoding='utf-8') as f:
        pairs = json.load(f)
    batch = args.batch or datetime.now().strftime('%Y-%m-%d')
    commit = args.commit
    n = 0
    for item in pairs:
        rel_src, rel_dst = item.get('src', ''), item.get('dst', '')
        src = resolve(root, rel_src)
        dst = resolve(root, rel_dst)
        if src is None or dst is None:
            refuse('%s  ->  %s' % (rel_src, rel_dst))
            continue
        if not os.path.exists(src):
            print('跳过（源不存在）：%s' % rel_src)
            continue
        if blacklisted_src(rel_src) or is_blacklisted(rel_dst):
            print('跳过（黑名单）：%s' % rel_src)
            continue
        dst = unique_dst(dst)
        rel_src = os.path.relpath(src, os.path.realpath(root))
        rel_dst = os.path.relpath(dst, os.path.realpath(root))
        print('%s  %s  ->  %s' % ('MOVE ' if commit else 'DRY  ', rel_src, rel_dst))
        if commit:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            h = hash_of(src)
            shutil.move(src, dst)
            append_log(root, LOG_MOVE,
                       {'t': now(), 'op': 'move', 'batch': batch, 'src': rel_src, 'dst': rel_dst, 'h': h})
        n += 1
    print('\n共 %d 项（commit=%s，批次=%s）。%s'
          % (n, commit, batch, '' if commit else '这是预演，加 --commit 才会真正搬移。'))
    if REL_REFUSED:
        print('另有 %d 项因越出工作区被拒绝，未执行。' % len(REL_REFUSED))
    if commit and n:
        print('回滚方式（只回滚本批次）：python3 整理工具.py rollback --root %s --batch %s --commit'
              % (root, batch))


def cmd_quarantine(args):
    root = args.root
    with open(args.list, encoding='utf-8') as f:
        rels = [ln.strip() for ln in f if ln.strip()]
    batch = args.batch or datetime.now().strftime('%Y-%m-%d')
    commit = args.commit
    n = 0
    for rel in rels:
        if is_blacklisted(rel):
            print('跳过（黑名单，永不删除）：%s' % rel)
            continue
        src = resolve(root, rel)
        dst = resolve(root, os.path.join(QUAR_ROOT, batch, rel))
        if src is None or dst is None:
            refuse(rel)
            continue
        if not os.path.exists(src):
            print('跳过（不存在）：%s' % rel)
            continue
        print('%s  %s  ->  _隔离区/%s/%s' % ('QUAR ' if commit else 'DRY  ', rel, batch, rel))
        if commit:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            h = hash_of(src)
            dst = unique_dst(dst)
            shutil.move(src, dst)
            append_log(root, LOG_DEL, {'t': now(), 'src': rel, 'q': os.path.relpath(dst, root), 'h': h, 'batch': batch})
        n += 1
    print('\n共 %d 项进入隔离区（commit=%s，批次=%s），保留 30 天。' % (n, commit, batch))
    if REL_REFUSED:
        print('另有 %d 项因越出工作区被拒绝，未执行。' % len(REL_REFUSED))
    if commit and n:
        print('还原方式：python3 整理工具.py restore --root %s --batch %s --commit' % (root, batch))


def del_log_name_map(root):
    """P6 · 从删除日志取「隔离区路径 → 原名」。`quarantine` 写日志时记了 `src` 原名，
    但原 `restore` 只看当前文件名 ⇒ 遇重名加了 `-1` 后缀的，还原后名字就变了（静默改名）。"""
    m = {}
    for r in read_log(root, LOG_DEL):
        q, s = r.get('q'), r.get('src')
        if q and s:
            m[q] = s
    return m


def cmd_restore(args):
    root = args.root
    quar = os.path.join(root, QUAR_ROOT)
    if not os.path.isdir(quar):
        print('没有隔离区。')
        return
    namemap = del_log_name_map(root)
    batches = sorted(os.listdir(quar)) if not args.batch else [args.batch]
    n = 0
    by_log = 0
    for b in batches:
        bdir = os.path.join(quar, b)
        if not os.path.isdir(bdir) or resolve(root, os.path.join(QUAR_ROOT, b)) is None:
            continue
        for cur, _, files in os.walk(bdir):
            for fn in files:
                src = os.path.join(cur, fn)
                rel_q = os.path.relpath(src, os.path.realpath(root))
                rel = namemap.get(rel_q) or os.path.relpath(src, bdir)
                if rel_q in namemap:
                    by_log += 1
                dst = resolve(root, rel)
                if dst is None:
                    refuse('%s（还原目标越出工作区）' % rel)
                    continue
                print('%s  %s  ->  %s%s'
                      % ('REST ' if args.commit else 'DRY  ', rel_q, rel,
                         '  [按删除日志还原原名]' if rel_q in namemap else ''))
                if args.commit:
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    shutil.move(src, unique_dst(dst))
                n += 1
    print('\n共 %d 项待还原（commit=%s；其中 %d 项按日志原名还原）。' % (n, args.commit, by_log))
    if REL_REFUSED:
        print('另有 %d 项因越出工作区被拒绝，未执行。' % len(REL_REFUSED))


def cmd_rollback(args):
    root = args.root
    recs = read_log(root, LOG_MOVE)
    if not recs:
        print('没有迁移日志，无可回滚。')
        return
    batch = args.batch
    if batch:
        recs = [r for r in recs if r.get('batch') == batch]
        if not recs:
            print('迁移日志中没有批次 %s 的记录。' % batch)
            return
    else:
        legacy = sum(1 for r in recs if not r.get('batch'))
        print('⚠ 未指定 --batch：将按时间逆序回滚**全部 %d 条历史搬移**（含所有批次）。' % len(recs))
        if legacy:
            print('  其中 %d 条为旧格式记录（无 batch 字段，无法按批次区分）——多数工作区只做过一次整理时可按此整批回滚。'
                  % legacy)
        print('  只想回滚某一次整理，请加 --batch <批次日期>。')
    n = 0
    for r in reversed(recs):
        src = resolve(root, r['dst'])
        dst = resolve(root, r['src'])
        if src is None or dst is None:
            refuse('%s  ->  %s' % (r.get('dst'), r.get('src')))
            continue
        if not os.path.exists(src):
            print('跳过（当前位置已无此文件）：%s' % r['dst'])
            continue
        print('%s  %s  ->  %s%s'
              % ('BACK ' if args.commit else 'DRY  ', r['dst'], r['src'],
                 '' if not r.get('batch') else '  [批次 %s]' % r['batch']))
        if args.commit:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.move(src, unique_dst(dst))
        n += 1
    print('\n共 %d 项待回滚（commit=%s%s）。' % (n, args.commit, '' if not batch else '，批次 %s' % batch))
    if REL_REFUSED:
        print('另有 %d 项因越出工作区被拒绝，未执行。' % len(REL_REFUSED))


def cmd_purge(args):
    root = args.root
    quar = os.path.join(root, QUAR_ROOT)
    if not os.path.isdir(quar):
        print('没有隔离区。')
        return
    # P1 · 下界校验：`--days 0` 会让**全部批次（含当天刚移入的）**都算"已超期"，一次删光隔离区
    if args.batch and args.days is not None:
        print('拒绝：--days 与 --batch 互斥，请只用一个。')
        sys.exit(2)
    if args.days is not None and args.days < 1:
        print('拒绝：保留期不可短于 1 天（收到 --days %d）。'
              '用 --batch <批次名,…> 精确指定要清的批次。' % args.days)
        sys.exit(2)
    days = 30 if args.days is None else args.days
    limit = time.time() - days * 86400
    # P2 · 按批次名精确清（可复现，不依赖"今天几号"）
    want = [x.strip() for x in args.batch.split(',') if x.strip()] if args.batch else None

    all_b = sorted(os.listdir(quar))
    n = 0
    tot_cnt = 0
    tot_sz = 0
    for b in all_b:
        bdir = os.path.join(quar, b)
        if not os.path.isdir(bdir):
            continue
        try:
            stamp = datetime.strptime(b, '%Y-%m-%d').timestamp()
        except ValueError:
            print('跳过（批次目录名非日期）：%s' % b)
            continue
        if resolve(root, os.path.join(QUAR_ROOT, b)) is None:
            refuse('%s/%s' % (QUAR_ROOT, b))
            continue
        if want is not None and b not in want:
            continue
        files = [os.path.join(cur, f) for cur, _, fs in os.walk(bdir) for f in fs]
        cnt = len(files)
        sz = 0
        for fp in files:
            try:
                sz += os.path.getsize(fp)
            except OSError:
                pass
        ago = (time.time() - stamp) / 86400.0
        if want is None and stamp >= limit:
            print('保留中（未超 %d 天）：%s（%d 个文件，距今 %.0f 天，%s）'
                  % (days, b, cnt, ago, human(sz)))
            continue
        # P4 · dry-run 信息增强：距今天数／体积／内容构成
        comp = defaultdict(int)
        for fp in files:
            comp[os.path.splitext(fp)[1].lower() or '(无扩展名)'] += 1
        top3 = ' · '.join('%s %d' % (e, c) for e, c in sorted(comp.items(), key=lambda x: -x[1])[:3])
        print('%s 批次 %s｜距今 %.0f 天｜%d 个文件｜%s｜构成：%s'
              % ('PURGE' if args.commit else 'DRY  ', b, ago, cnt, human(sz), top3))
        # P4 · 批次内检出可读文本时逐项警示（阻断 2：凭据／说明性文件曾与待删物同批）
        readable = sorted(os.path.relpath(fp, root) for fp in files
                          if readable_text_ext(os.path.splitext(fp)[1].lower())
                          and not is_app_residue(os.path.relpath(fp, root)))
        if readable:
            print('  ⚠ 检出**可读文本 %d 个**（已排除应用内部残留）——先人工确认有没有该留的'
                  '（类型体系里多半属「机制台账／说明与规则」）:' % len(readable))
            for p in readable[:15]:
                print('      %s' % p)
            if len(readable) > 15:
                print('      …另有 %d 个' % (len(readable) - 15))
        if args.commit:
            # purge 是全程唯一的物理删除：不经过回收站、不可恢复，
            # 故在 rmtree 之前把该批次**每一个文件**写一条记录进删除日志，作为唯一凭据。
            # ⚠ **幂等**：同一批次若被重复执行（中断后重跑／命令被执行两次／并发），
            #    不得重复记账——否则「覆盖率」会被算成 200%，把「留痕存在 ≠ 留痕覆盖」
            #    重新制造一遍（实测：一条被重跑的命令，让某批次 71 个文件记了 142 条）。
            already = {r.get('src') for r in read_log(root, LOG_DEL)
                       if r.get('op') == 'purge' and r.get('batch') == b}
            logged = 0
            skipped = 0
            for fp in files:
                rel_fp = os.path.relpath(fp, root)
                if rel_fp in already:
                    skipped += 1
                    continue
                try:
                    size = os.path.getsize(fp)
                except OSError:
                    size = 0
                append_log(root, LOG_DEL, {
                    't': now(), 'op': 'purge', 'batch': b, 'src': rel_fp,
                    's': size, 'h': md5_of(fp) if 0 < size < BIG_FILE else '',
                })
                logged += 1
            print('  清单已写入删除日志（新增 %d 条%s；覆盖率 %d/%d ＝ %.0f%%）。'
                  % (logged, ('，跳过已记账 %d 条' % skipped) if skipped else '',
                     logged + skipped, cnt, 100.0 * (logged + skipped) / max(cnt, 1)))
            shutil.rmtree(bdir)
        n += 1
        tot_cnt += cnt
        tot_sz += sz
    if want is not None:
        missing = [b for b in want if b not in all_b]
        if missing:
            print('⚠ 指定的批次不存在：%s' % '、'.join(missing))
    print('\n共 %d 个批次（commit=%s）｜合计 %d 个文件｜%s'
          % (n, args.commit, tot_cnt, human(tot_sz)))
    if not args.commit:
        print('这是预演。注意：purge 是唯一真正删除文件的操作，务必先确认隔离区内容。')


def main():
    ap = argparse.ArgumentParser(description='工作区整理工具')
    ap.add_argument('cmd', choices=['scan', 'dup', 'move', 'quarantine', 'restore', 'rollback', 'purge'])
    ap.add_argument('--root', default='.', help='工作区根目录，默认当前目录')
    ap.add_argument('--map', help='move 用：JSON 数组 [{"src":"...","dst":"..."}]')
    ap.add_argument('--list', help='quarantine 用：每行一个相对路径的文本文件')
    ap.add_argument('--batch', help='quarantine 用：隔离区批次目录名，默认今天；'
                                    'rollback 用：只回滚该批次（不带则回滚全部历史）；'
                                    'restore 用：只还原该批次；'
                                    'purge 用：**只清这些批次**（逗号分隔，与 --days 互斥）')
    ap.add_argument('--days', type=int, default=None,
                    help='purge 用：保留天数（不传＝30；**必须 ≥1**，与 --batch 互斥）')
    ap.add_argument('--group-depth', type=int, default=1,
                    help='scan 用：按路径前 N 层分组输出目录概览（0 关闭），默认 1')
    ap.add_argument('--commit', action='store_true', help='真正执行；不加则只预演')
    args = ap.parse_args()

    if args.cmd in ('move', 'quarantine') and not args.commit:
        print('提示：当前为预演模式（dry-run），不会改动任何文件。确认无误后加 --commit。\n')

    {
        'scan': cmd_scan, 'dup': cmd_dup, 'move': cmd_move,
        'quarantine': cmd_quarantine, 'restore': cmd_restore,
        'rollback': cmd_rollback, 'purge': cmd_purge,
    }[args.cmd](args)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
skill_check.py — Skill 交付前的静态质检脚本
==========================================

对一个 skill 目录执行 结构 / 内容 / 安全 三类检查，逐项输出 PASS / WARN / FAIL 与原因。

用法:
    python skill_check.py <skill目录>
    python skill_check.py C:/Users/<you>/.workbuddy/skills/my-skill

扫描范围（v1.1 修正覆盖盲区）:
    结构/内容类规则  → 只查 SKILL.md
    安全类规则       → 查 SKILL.md + references/ + scripts/ + assets/ 下全部文本文件
                       （排除 references/research/**：调研材料记录的是攻击手法本身，
                         属文档而非可执行资产，在「审计覆盖声明」中显式声明排除）
    输出末尾给出审计覆盖声明：扫了哪些文件、跳过了哪些（非 UTF-8 / 二进制 / 超大文件）。

行内豁免（复用 macos-design-framework 的 audit:ignore 约定）:
    在任意被扫文件的行尾追加   <!-- audit:ignore RULE_ID 原因 -->
    即豁免该行命中的 RULE_ID。豁免指令在未去注释的原始行上匹配。

FAIL 级（阻断交付）RULE_ID:
    FRONTMATTER  缺 YAML frontmatter
    NAME_FORMAT   name 非 hyphen-case（规范：小写字母数字 + 单连字符）
    NAME_RESERVED name 含保留字 claude/anthropic（平台上传校验强制）
    NAME_DIR      name 与父目录名不一致（规范硬性要求）
    DESC_LEN      description 超 1024 字符硬上限
    DESC_ANGLE    description 含尖括号（本机校验器会拒）
    DESC_WHEN     description 未写触发场景
    BODY_LINES    正文 >500 行（规范建议上限）
    BODY_TOKENS   正文 token 估算 >5000（规范建议上限）
    BROKEN_REF    引用的内部文件不存在
    SECRET        疑似硬编码密钥
    DANGER_CMD    高危命令模式
    INJECTION     疑似提示注入句式

WARN 级（启发式，需人工判断）RULE_ID:
    DESC_LEN     >300 字符（建议精简，关键词前置）
    DESC_STYLE   description 疑似总结工作流（agent 会照 description 走捷径而不读正文）
    BODY_TOKENS  >1000（普通 skill 建议 <500 词 ≈ <1000 中文字符；频繁加载型 <200 词）
    VAGUE_WORD   正文含「可以考虑/根据情况/视情况而定/酌情」等模糊词（SkillLens「可执行具体性」维度，禁用）
    ENCODED_EXEC 编码后执行（base64 / eval / exec）——可能是混淆攻击，也可能是正常代码
    POLICY_LURE  伪合规话术（借「合规/安全策略要求」口吻索取权限是攻击信号，不是信任信号）
    HIDDEN_CHAR  零宽 / BiDi 等隐藏字符（可能用于藏指令）
    PATH_TRAV    路径穿越（上级目录跳转，可能越出 skill 目录）
    ENV_REF      引用环境变量/敏感目录，需正当理由
    URL_EXTERNAL 含外部 URL，需人工确认域名预期
"""

import re
import sys
from pathlib import Path

# ---- 阈值（依据 agentskills.io 官方规范 + superpowers 长度规则）----
DESC_MAX_CHARS = 1024          # 规范硬上限
DESC_WARN_CHARS = 300          # 建议值：关键词前置，短而准
BODY_MAX_LINES = 500           # 规范：SKILL.md 保持 <500 行
BODY_FAIL_TOKENS = 5000        # 规范：正文建议 <5000 token
BODY_WARN_TOKENS = 1000        # 社区口径折算：普通 skill <500 词 ≈ <1000 中文字符
NAME_PATTERN = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
WHEN_MARKERS = re.compile(
    r'(当.{0,40}?(时|后|前)|时用|时调用|用于|触发|适用|use[d]?\s+(when|for)|should be used when|whenever)', re.IGNORECASE)
WORKFLOW_MARKERS = re.compile(
    r'(步骤|工作流|流程如下|第一步|然后|接着|最后|step\s*\d|first.{0,15}then|workflow)', re.IGNORECASE)
CJK_PATTERN = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]')
# 「可执行具体性」维度的模糊词（SkillLens 实证禁用）。取具体短语而非单字，压低误报。
VAGUE_PATTERN = re.compile(r'(可以考虑|根据情况|视情况而定|视情况|灵活把握|酌情|可能可以)')

SCANNABLE_EXT = {'.md', '.py', '.sh', '.js', '.ts', '.json', '.yaml', '.yml', '.txt', '.css', '.html', '.svg'}
EXCLUDE_SCAN_DIRS = {'references/research'}   # 调研材料：记录攻击手法，非可执行资产
# 审计产物：由审计流程生成，内容必然引用攻击手法原文，且不属于 skill 的加载/执行面。
# 残余风险提示：恶意文件若刻意取此名可绕过扫描——故名称硬编码为单文件名，且排除情况在
# 输出的「审计覆盖声明」中逐条列出，不静默跳过。
EXCLUDE_SCAN_FILES = {'安全审计报告.md'}
MAX_FILE_BYTES = 2 * 1024 * 1024

# 高危模式: (RULE_ID, 正则, 说明, 级别)
DANGER_PATTERNS = [
    ("SECRET", re.compile(
        r'(sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY-----'
        r'|api[_-]?key\s*[:=]\s*["\'][A-Za-z0-9]{16,})', re.IGNORECASE), "疑似硬编码密钥", "FAIL"),
    ("DANGER_CMD", re.compile(
        r'(rm\s+-rf\s+[/~]|del\s+/[sS]\s+/[qQ]|curl[^|]*\|\s*(sudo\s+)?(ba)?sh'  # audit:ignore DANGER_CMD 检测模式定义本身
        r'|wget[^|]*\|\s*(sudo\s+)?(ba)?sh|Invoke-Expression|iex\s*\()'),  # audit:ignore DANGER_CMD 检测模式定义本身
        "高危命令模式", "FAIL"),
    ("INJECTION", re.compile(
        r'(ignore (all |any )?(previous|prior) instructions|忽略(之前|以上|所有)的?(指令|指示|提示)'  # audit:ignore INJECTION 检测模式定义本身
        r'|disregard.{0,20}system prompt|jailbreak)',  # audit:ignore INJECTION 检测模式定义本身
        re.IGNORECASE), "疑似提示注入句式", "FAIL"),
    ("ENCODED_EXEC", re.compile(
        r'(base64\s*(-d|--decode)|b64decode|atob\s*\(|eval\s*\(\s*(?:atob|base64|decode)|exec\s*\(\s*decode)',  # audit:ignore ENCODED_EXEC 检测模式定义本身
        re.IGNORECASE), "编码后执行（混淆攻击常见手法，也可能是正常代码）", "WARN"),
    ("POLICY_LURE", re.compile(
        r'(as required by (policy|security|compliance)|authorized to (send|upload|exfiltrate)'  # audit:ignore POLICY_LURE 检测模式定义本身
        r'|根据(安全|合规)(策略|要求)(必须|需要)发送)', re.IGNORECASE), "伪合规话术（攻击信号而非信任信号）", "WARN"),
    ("HIDDEN_CHAR", re.compile('[\u200b-\u200f\u202a-\u202e\u2060-\u2064\ufeff]'),
     "零宽 / BiDi 隐藏字符", "WARN"),
    ("PATH_TRAV", re.compile(r'\.\./'), "路径穿越（上级目录跳转）", "WARN"),  # audit:ignore PATH_TRAV 检测模式定义本身
]

ENV_REF = re.compile(r'(\$\{?[A-Z_]*(API_KEY|TOKEN|SECRET|PASSWORD)[A-Z_]*\}?|~/\.(aws|ssh|npm))', re.IGNORECASE)
URL_RE = re.compile(r'https?://([\w.-]+)')


def strip_ignored(lines, rule_id):
    """返回未豁免 rule_id 的行。

    豁免写法两种（同一行可并列多个 RULE_ID）：
        md/html: <!-- audit:ignore RULE_ID 原因 -->
        py/sh:   # audit:ignore RULE_ID 原因
    """
    kept = []
    for line in lines:
        ids = re.findall(r'(?:<!--|#)\s*audit:ignore\s+([A-Z_]+)', line)
        if rule_id in ids:
            continue
        kept.append(line)
    return kept


def collect_text_files(skill_dir):
    """返回 [(相对路径, 文本)]，跳过二进制/超大/非 UTF-8。"""
    files, skipped = [], []
    for p in sorted(skill_dir.rglob('*')):
        if not p.is_file():
            continue
        rel = p.relative_to(skill_dir).as_posix()
        if any(rel.startswith(d + '/') for d in EXCLUDE_SCAN_DIRS):
            skipped.append(rel + "（调研材料，已排除）")
            continue
        if rel in EXCLUDE_SCAN_FILES or '审计报告' in rel:
            skipped.append(rel + "（安全审计产物，已排除）")
            continue
        if p.suffix.lower() not in SCANNABLE_EXT:
            continue
        if p.stat().st_size > MAX_FILE_BYTES:
            skipped.append(rel + "（超大文件）")
            continue
        try:
            files.append((rel, p.read_text(encoding='utf-8')))
        except (UnicodeDecodeError, OSError):
            skipped.append(rel + "（非 UTF-8 / 不可读）")
    return files, skipped


def count_tokens(text):
    """近似 token 估算：英文按词计，CJK 按字计（v1.1 修正中文低估约 3 倍的问题）。"""
    return len(re.findall(r'[A-Za-z0-9]+', text)) + len(CJK_PATTERN.findall(text))


def check_frontmatter(raw, skill_dir):
    results = []
    m = re.match(r'^---\s*\n(.*?)\n---', raw, re.DOTALL)
    if not m:
        return [("FRONTMATTER", False, "缺少 YAML frontmatter", "")], None
    fm = m.group(1)

    name_m = re.search(r'^name:\s*(.+)$', fm, re.MULTILINE)
    if not name_m:
        results.append(("NAME_FORMAT", False, "frontmatter 缺少 name 字段", ""))
    else:
        name = name_m.group(1).strip().strip('"\'')
        ok = bool(NAME_PATTERN.match(name))
        results.append(("NAME_FORMAT", ok,
                        f"name={name}" if ok else f"name「{name}」非 hyphen-case", ""))
        reserved = bool(re.search(r'claude|anthropic', name, re.IGNORECASE))
        results.append(("NAME_RESERVED", not reserved,
                        f"name 含保留字 claude/anthropic（平台上传校验强制）" if reserved
                        else "name 无保留字", ""))
        dir_name = skill_dir.resolve().name   # v1.1: resolve() 修复传入 "." 时报空串的误判
        if name and name != dir_name:
            results.append(("NAME_DIR", False,
                            f"name「{name}」与目录名「{dir_name}」不一致（规范硬性要求）", ""))
        elif name:
            results.append(("NAME_DIR", True, "name 与目录名一致", ""))

    desc_m = re.search(r'^description:\s*\|?\s*\n((?:\s{2,}.*\n?)+)|^description:\s*(.+)$', fm, re.MULTILINE)
    description = ""
    if desc_m:
        description = re.sub(r'\s+', ' ', (desc_m.group(1) or desc_m.group(2) or "").strip())
    if not description:
        results.append(("DESC_LEN", False, "frontmatter 缺少 description 字段", ""))
    else:
        n = len(description)
        if n > DESC_MAX_CHARS:
            results.append(("DESC_LEN", False, f"description {n} 字符，超硬上限 {DESC_MAX_CHARS}", ""))
        elif n > DESC_WARN_CHARS:
            results.append(("DESC_LEN", True, f"description {n} 字符（>建议值 {DESC_WARN_CHARS}）", "WARN"))
        else:
            results.append(("DESC_LEN", True, f"description {n} 字符", ""))
        has_angle = '<' in description or '>' in description
        results.append(("DESC_ANGLE", not has_angle,
                        "description 含尖括号，本机校验器会拒" if has_angle else "description 无尖括号", ""))
        has_when = bool(WHEN_MARKERS.search(description))
        results.append(("DESC_WHEN", has_when,
                        "description 含触发场景" if has_when else "description 未写触发场景（when）", ""))
        if WORKFLOW_MARKERS.search(description):
            results.append(("DESC_STYLE", True,
                            "description 疑似总结工作流/流程——agent 可能照它走捷径而不读正文，改为只写触发条件",
                            "WARN"))
        else:
            results.append(("DESC_STYLE", True, "description 未见工作流摘要", ""))
    return results, m


def check_body(raw, fm_match, skill_name):
    body = raw[fm_match.end():] if fm_match else raw
    lines = len(body.split('\n'))
    tokens = count_tokens(body)
    # 视角/人格类 skill（人物蒸馏）知识密集，正文天然长，BODY 超限降为 WARN 而非 FAIL
    knowledge_dense = '-perspective' in skill_name
    results = []
    if lines > BODY_MAX_LINES:
        results.append(("BODY_LINES", knowledge_dense,
                        f"正文 {lines} 行，超规范上限 {BODY_MAX_LINES}"
                        + ("——视角类知识密集，豁免为提示" if knowledge_dense else ""),
                        "WARN" if knowledge_dense else ""))
    else:
        results.append(("BODY_LINES", True, f"正文 {lines} 行（上限 {BODY_MAX_LINES}）", ""))
    if tokens > BODY_FAIL_TOKENS:
        results.append(("BODY_TOKENS", knowledge_dense,
                        f"正文约 {tokens} token（英文按词/中文按字估算），超规范建议值 {BODY_FAIL_TOKENS}"
                        + ("——视角类知识密集，豁免为提示" if knowledge_dense else "——细节下沉 references/"),
                        "WARN" if knowledge_dense else ""))
    elif tokens > BODY_WARN_TOKENS:
        results.append(("BODY_TOKENS", True,
                        f"正文约 {tokens} token（普通 skill 建议 <{BODY_WARN_TOKENS}，频繁加载型 <400）", "WARN"))
    else:
        results.append(("BODY_TOKENS", True, f"正文约 {tokens} token", ""))
    body_lines = body.split('\n')
    kept = strip_ignored(body_lines, "VAGUE_WORD")
    vague_hits = [i + 1 for i, line in enumerate(body_lines)
                  if line in kept and VAGUE_PATTERN.search(line)]
    if vague_hits:
        results.append(("VAGUE_WORD", True,
                        f"正文 {len(vague_hits)} 处模糊词（第 {', '.join(map(str, vague_hits[:5]))} 行"
                        f"{' 等' if len(vague_hits) > 5 else ''}）——SkillLens「可执行具体性」维度，建议改为可执行动词/判据",
                        "WARN"))
    else:
        results.append(("VAGUE_WORD", True, "正文无模糊词", ""))
    return results


def check_refs(skill_dir, lines):
    kept = strip_ignored(lines, "BROKEN_REF")
    text = '\n'.join(kept)
    # 允许中文文件名；遇 ~ * ? 视为范围/通配写法（如 01~04），不作为具体路径校验
    raw_refs = re.findall(r'(?:scripts|references|assets)/[\w./\-一-鿿~*?]+', text)
    refs, globbed = set(), set()
    for r in raw_refs:
        r = r.rstrip('.,;:）)')
        if re.search(r'[~*?]', r):
            globbed.add(r)
        else:
            refs.add(r)
    broken = sorted(r for r in refs if not (skill_dir / r).exists())
    if broken:
        return [("BROKEN_REF", False, f"引用不存在的文件: {', '.join(broken[:5])}", "")]
    extra = f"（另有 {len(globbed)} 处范围/通配写法未校验）" if globbed else ""
    return [("BROKEN_REF", True,
             f"内部引用 {len(refs)} 处均存在{extra}" if refs else f"无内部文件引用{extra}", "")]


def check_security(files, skill_name):
    """files: [(相对路径, 文本)] — 安全类规则扫全部文本文件，不只看 SKILL.md。"""
    results = []
    # 安全审计类 skill 的教学内容本身即「危险模式列举」，对其做 DANGER_CMD/INJECTION 检查是类别错误 → 豁免
    exempt_security = any(k in skill_name for k in ("security", "audit"))
    for rule_id, pattern, label, level in DANGER_PATTERNS:
        if exempt_security and rule_id in ("DANGER_CMD", "INJECTION"):
            results.append((rule_id, True, f"{label}: 安全审计类 skill 豁免（教学内容即危险模式列举）", ""))
            continue
        hits = []
        for rel, text in files:
            kept = strip_ignored(text.split('\n'), rule_id)
            for i, line in enumerate(text.split('\n')):
                if line in kept and pattern.search(line):
                    hits.append(f"{rel}:{i + 1}")
        if hits:
            msg = f"{label}（{', '.join(hits[:5])}"
            msg += f" 等 {len(hits)} 处）" if len(hits) > 5 else "）"
            msg += "——教学/检测示例用 audit:ignore 行内豁免并注明原因"
            results.append((rule_id, level != "FAIL", msg, level))
        else:
            results.append((rule_id, True, f"{label}: 未命中", ""))

    env_hits, url_domains = [], set()
    for rel, text in files:
        kept = strip_ignored(text.split('\n'), "ENV_REF")
        for i, line in enumerate(text.split('\n')):
            if line in kept and ENV_REF.search(line):
                env_hits.append(f"{rel}:{i + 1}")
        kept = strip_ignored(text.split('\n'), "URL_EXTERNAL")
        for line in kept:
            url_domains.update(URL_RE.findall(line))

    if env_hits:
        results.append(("ENV_REF", True,
                        f"引用环境变量/敏感目录（{', '.join(env_hits[:5])}）——需正当理由，否则按敌意处理", "WARN"))
    else:
        results.append(("ENV_REF", True, "未引用环境变量/敏感目录", ""))
    if url_domains:
        doms = sorted(url_domains)
        results.append(("URL_EXTERNAL", True,
                        f"含 {len(doms)} 个外部域名，人工确认均为预期: {', '.join(doms[:8])}"
                        f"{' …' if len(doms) > 8 else ''}", "WARN"))
    else:
        results.append(("URL_EXTERNAL", True, "无外部 URL", ""))
    return results


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    skill_dir = Path(sys.argv[1]).resolve()   # v1.1: 支持在目录内用 "." 调用
    skill_md = skill_dir / 'SKILL.md'
    print(f"skill_check: {skill_dir}")
    print("=" * 66)
    if not skill_md.exists():
        print("  [FAIL] FRONTMATTER  SKILL.md 不存在")
        sys.exit(1)

    raw = skill_md.read_text(encoding='utf-8')
    lines = raw.split('\n')
    files, skipped = collect_text_files(skill_dir)

    fm_results, fm_match = check_frontmatter(raw, skill_dir)
    all_results = (fm_results + check_body(raw, fm_match, skill_dir.name)
                   + check_refs(skill_dir, lines) + check_security(files, skill_dir.name))

    passed = warned = failed = 0
    for rule_id, ok, detail, level in all_results:
        if not ok:
            mark, failed = "FAIL", failed + 1
        elif level == "WARN":
            mark, warned = "WARN", warned + 1
        else:
            mark, passed = "PASS", passed + 1
        print(f"  [{mark}] {rule_id:<12} {detail}")
    print("=" * 66)
    print(f"结果: {passed} PASS / {warned} WARN / {failed} FAIL")

    # 审计覆盖声明
    print(f"审计覆盖声明: 安全类规则扫描 {len(files)} 个文本文件"
          f"（{', '.join(f[0] for f in files[:6])}{' …' if len(files) > 6 else ''}）")
    if skipped:
        print(f"  未扫描: {len(skipped)} 个文件 —— {'; '.join(skipped[:4])}"
              f"{' …' if len(skipped) > 4 else ''}")

    if failed:
        print("存在 FAIL——修复后再交付；教学示例类命中用 audit:ignore 行内豁免并注明原因。")
        sys.exit(1)
    print("无 FAIL，可交付（WARN 项按上下文评估）。")
    sys.exit(0)


if __name__ == '__main__':
    main()

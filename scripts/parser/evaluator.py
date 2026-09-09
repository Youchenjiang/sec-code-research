#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code Security Research — 學術論文 Markdown 版面解析品質檢驗器 (Parser Quality Evaluator)
================================================================================
多維度自動化驗收與品質審查引擎：
1. 浮水印與頁眉頁腳雜訊殘留檢驗 (IEEE / ACM / USENIX / arXiv / 獨立頁碼)
2. 表格品質檢驗 (是否誤吞正文段落、欄位結構是否合法)
3. 圖片資產有效性 (Markdown 鏈結解析、實體檔案存在性、防範過小線條雜訊圖)
4. 雙欄閱讀順序合理性 (Abstract 與 Introduction 之相對位置)
5. 斷行連字號修復程度 (De-hyphenation)
"""

import os
import re
from typing import Dict, List, Tuple, Any

PROSE_KEYWORDS = ('prompt', 'step', 'example', 'cot', 'chain')


def _find_ref_start(lines: List[str]) -> int:
    """尋找 References 起始行 (避免將參考文獻中的正規引用誤判為浮水印)"""
    for idx, l in enumerate(lines):
        if re.match(r'^#{1,6}\s*(?:\d+\.?\s*)?References', l, re.IGNORECASE):
            return idx
    return len(lines)


def _check_watermarks(lines: List[str]) -> List[str]:
    """檢查浮水印與雜訊殘留"""
    ref_start_idx = _find_ref_start(lines)
    watermark_patterns = [
        (r'Authorized licensed use', "IEEE Copyright Watermark", False),
        (r'Permission to make digital or hard copies', "ACM Copyright Watermark", False),
        (r'ACM ISBN', "ACM ISBN Line", False),
        (r'USENIX Association', "USENIX Header/Footer", True),
        (r'arXiv:\d+\.\d+', "arXiv Watermark", False),
        (r'^\s*\d{1,3}\s*$', "Standalone Page Number Line", False),
        (r'https?://doi\.org/[^\s]+', "Raw DOI Line in Body", True),
    ]
    issues = []
    for pattern, desc, body_only in watermark_patterns:
        search_lines = lines[:ref_start_idx] if body_only else lines
        matches = [idx + 1 for idx, l in enumerate(search_lines) if re.search(pattern, l)]
        if matches:
            issues.append(f"[WATERMARK] 發現 {len(matches)} 處 '{desc}' 殘留 (行號: {matches[:5]})")
    return issues


def _check_table_cells(idx: int, l_str: str) -> List[str]:
    """檢查單元格是否異常過長 (排除對照說明表)"""
    issues = []
    cells = [c.strip() for c in l_str.split('|')[1:-1]]
    max_allowed = 1500 if len(cells) <= 2 else 400
    for c in cells:
        if len(c) > max_allowed and not any(k in c.lower() for k in PROSE_KEYWORDS):
            issues.append(f"[TABLE] 行 {idx + 1}: 單元格包含 {len(c)} 字元 (>{max_allowed})，疑似誤吞正文段落！")
    return issues


def _check_table_quality(lines: List[str]) -> Tuple[int, List[str]]:
    """檢查表格品質與結構"""
    in_table = False
    table_count = 0
    issues = []
    for idx, l in enumerate(lines):
        l_str = l.strip()
        if l_str.startswith('|') and l_str.endswith('|'):
            if not in_table:
                in_table = True
                table_count += 1
            issues.extend(_check_table_cells(idx, l_str))
        else:
            in_table = False
    return table_count, issues


def _extract_img_matches(md_text: str) -> List[Tuple[str, str]]:
    """提取 Markdown 圖片鏈結 (無回溯模式)"""
    img_matches = re.findall(r'!\[([^\]]*)\]\(<([^>]+)>\)', md_text)
    if not img_matches:
        img_matches = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', md_text)
    return img_matches


def _check_figures(md_text: str, md_path: str) -> Tuple[int, List[str]]:
    """檢查圖片連結與實體檔案有效性"""
    img_matches = _extract_img_matches(md_text)
    issues = []
    base_dir = os.path.dirname(md_path) if md_path else "."
    for _, p in img_matches:
        clean_p = p.strip('<>').strip()
        resolved_p = os.path.normpath(os.path.join(base_dir, clean_p))
        if md_path and not os.path.exists(resolved_p):
            issues.append(f"[FIGURE] 圖片鏈結失效: {clean_p} -> 實體檔案不存在！")
        elif md_path and os.path.exists(resolved_p):
            sz = os.path.getsize(resolved_p)
            if sz < 1000:
                issues.append(f"[FIGURE] 疑似異常線條/極小圖片 ({sz} bytes): {clean_p}")
    return len(img_matches), issues


def _check_hyphenation(md_text: str) -> List[str]:
    """檢查行尾連字號修復 (無回溯模式)"""
    lines = md_text.splitlines()
    count = 0
    for i in range(len(lines) - 1):
        prev = lines[i].rstrip()
        nxt = lines[i + 1].lstrip()
        if prev.endswith("-") and len(prev) >= 4 and prev[-2].isalpha() and nxt and nxt[0].isalpha():
            count += 1
    if count > 10:
        return [f"[HYPHEN] 發現 {count} 處跨行未接合之連字號。"]
    return []


def _check_reading_order(lines: List[str]) -> List[str]:
    """檢查雙欄閱讀順序異常"""
    intro_idx = -1
    abstract_idx = -1
    for idx, l in enumerate(lines):
        if intro_idx == -1 and re.match(r'^#{1,6}\s*(?:1\.?\s*)?Introduction', l, re.IGNORECASE):
            intro_idx = idx
        if abstract_idx == -1 and re.match(r'^#{1,6}\s*Abstract', l, re.IGNORECASE):
            abstract_idx = idx

    if intro_idx != -1 and abstract_idx != -1 and intro_idx < abstract_idx:
        return [f"[READING_ORDER] 順序顛倒：'Introduction' (行 {intro_idx + 1}) 出現在 'Abstract' (行 {abstract_idx + 1}) 之前！"]
    return []


def analyze_markdown_quality(md_text: str, md_path: str = "") -> Tuple[Dict[str, Any], List[str]]:
    """
    對生成的學術論文 Markdown 文本執行多維度品質審查。
    回傳 (統計資訊字典, 缺陷警告列表)
    """
    lines = md_text.splitlines()
    issues: List[str] = []

    issues.extend(_check_watermarks(lines))
    table_count, tbl_issues = _check_table_quality(lines)
    issues.extend(tbl_issues)
    fig_count, fig_issues = _check_figures(md_text, md_path)
    issues.extend(fig_issues)
    issues.extend(_check_hyphenation(md_text))
    issues.extend(_check_reading_order(lines))

    stats = {
        "total_lines": len(lines),
        "total_words": len(md_text.split()),
        "tables": table_count,
        "figures": fig_count,
        "code_blocks": len(re.findall(r'```', md_text)) // 2,
        "issues_count": len(issues)
    }
    return stats, issues

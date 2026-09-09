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


def analyze_markdown_quality(md_text: str, md_path: str = "") -> Tuple[Dict[str, Any], List[str]]:
    """
    對生成的學術論文 Markdown 文本執行多維度品質審查。
    回傳 (統計資訊字典, 缺陷警告列表)
    """
    lines = md_text.splitlines()
    issues: List[str] = []

    # 尋找 References 起始行 (避免將參考文獻中的正規引用誤判為浮水印)
    ref_start_idx = len(lines)
    for idx, l in enumerate(lines):
        if re.match(r'^#+\s*(?:\d+\.?\s*)?References', l, re.I):
            ref_start_idx = idx
            break

    # 1. 檢查浮水印與雜訊殘留
    watermark_patterns = [
        (r'Authorized licensed use', "IEEE Copyright Watermark", False),
        (r'Permission to make digital or hard copies', "ACM Copyright Watermark", False),
        (r'ACM ISBN', "ACM ISBN Line", False),
        (r'USENIX Association', "USENIX Header/Footer", True),  # True: 僅在正文檢測
        (r'arXiv:\d+\.\d+', "arXiv Watermark", False),
        (r'^\s*\d{1,3}\s*$', "Standalone Page Number Line", False),
        (r'https?://doi\.org/[^\s]+', "Raw DOI Line in Body", True),
    ]
    for pattern, desc, body_only in watermark_patterns:
        search_lines = lines[:ref_start_idx] if body_only else lines
        matches = [idx + 1 for idx, l in enumerate(search_lines) if re.search(pattern, l)]
        if matches:
            issues.append(f"[WATERMARK] 發現 {len(matches)} 處 '{desc}' 殘留 (行號: {matches[:5]})")

    # 2. 檢查表格品質
    in_table = False
    table_lines = 0
    table_count = 0
    for idx, l in enumerate(lines):
        l_str = l.strip()
        if l_str.startswith('|') and l_str.endswith('|'):
            if not in_table:
                in_table = True
                table_count += 1
            table_lines += 1
            # 檢查單元格是否異常過長 (排除 2 欄的 Prompt / Description 對照表)
            cells = [c.strip() for c in l_str.split('|')[1:-1]]
            max_allowed = 1500 if len(cells) <= 2 else 400
            for c in cells:
                if len(c) > max_allowed and not any(k in c.lower() for k in ('prompt', 'step', 'example', 'cot', 'chain')):
                    issues.append(f"[TABLE] 行 {idx + 1}: 單元格包含 {len(c)} 字元 (>{max_allowed})，疑似誤吞正文段落！")
        else:
            in_table = False

    # 3. 檢查圖片連結與實體檔案有效性
    # 支援標準 CommonMark 角括號語法: ![alt](<path>) 與一般語法: ![alt](path)
    img_matches = re.findall(r'!\[(.*?)\]\(<([^>]+)>\)', md_text)
    if not img_matches:
        img_matches = re.findall(r'!\[(.*?)\]\(([^)]+)\)', md_text)

    base_dir = os.path.dirname(md_path) if md_path else "."
    for cap, p in img_matches:
        clean_p = p.strip('<>').strip()
        resolved_p = os.path.normpath(os.path.join(base_dir, clean_p))
        if md_path and not os.path.exists(resolved_p):
            issues.append(f"[FIGURE] 圖片鏈結失效: {clean_p} -> 實體檔案不存在！")
        elif md_path and os.path.exists(resolved_p):
            sz = os.path.getsize(resolved_p)
            if sz < 1000:
                issues.append(f"[FIGURE] 疑似異常線條/極小圖片 ({sz} bytes): {clean_p}")

    # 4. 檢查行尾連字號修復
    hyphen_breaks = re.findall(r'[a-zA-Z]{3,}-\s*\n\s*[a-zA-Z]{3,}', md_text)
    if len(hyphen_breaks) > 10:
        issues.append(f"[HYPHEN] 發現 {len(hyphen_breaks)} 處跨行未接合之連字號。")

    # 5. 檢查雙欄閱讀順序異常
    intro_idx = -1
    abstract_idx = -1
    for idx, l in enumerate(lines):
        if re.search(r'#+\s*(?:1\.?\s*)?Introduction', l, re.I):
            intro_idx = idx
            break
        if re.search(r'#+\s*Abstract', l, re.I):
            abstract_idx = idx

    if intro_idx != -1 and abstract_idx != -1 and intro_idx < abstract_idx:
        issues.append(f"[READING_ORDER] 順序顛倒：'Introduction' (行 {intro_idx + 1}) 出現在 'Abstract' (行 {abstract_idx + 1}) 之前！")

    stats = {
        "total_lines": len(lines),
        "total_words": len(md_text.split()),
        "tables": table_count,
        "figures": len(img_matches),
        "code_blocks": len(re.findall(r'```', md_text)) // 2,
        "issues_count": len(issues)
    }
    return stats, issues

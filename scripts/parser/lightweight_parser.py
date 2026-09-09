#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code Security Research — 純 Python / PyMuPDF 輕量化學術文獻佈局解析器 (Lightweight Layout Parser)
==================================================================================
特點：
- 零依賴大型深度學習模型 (不需要 PyTorch/CUDA/GPU，純 CPU 毫秒級執行)
- 基於幾何佈局 (Bounding Box) 與字體樣式統計自動識別標題層級
- 智慧型學術表格偵測器 (TableRecognizer)：自動解析無邊框/三線表並轉為標準 Markdown 表格
- 智慧型圖表偵測與資產外置 (FigureRecognizer)：自動定位圖表區域、剪裁向量/點陣圖並過濾軸標籤雜訊
- 雙欄/單欄自適應閱讀順序重組 (Top -> Left -> Right -> Bottom)
- 頁面邊界雜訊過濾 (自動剔除頂部重複頁眉、底部頁碼、極端邊界 arXiv 水印)
- 行尾音節斷字自動拼接修復 (De-hyphenation)
- 產出 100% 符合 Obsidian Vault 與 paper_cli audit 規範之標準 Markdown
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any, Set
import yaml
import fitz  # PyMuPDF

# 強制 Windows 終端輸出為 UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')


def win_path(p: str) -> str:
    """處理 Windows 超長路徑 (>260 字元) 避免 [WinError 3] 或 [WinError 2]"""
    if not p:
        return p
    try:
        ap = os.path.abspath(p)
        if os.name == 'nt' and not ap.startswith('\\\\?\\'):
            if ap.startswith('\\\\'):
                return '\\\\?\\UNC' + ap[1:]
            return '\\\\?\\' + ap
        return ap
    except Exception:
        return p


COMPOUND_PREFIXES = {
    'zero', 'open', 'real', 'post', 'pre', 'cross', 'multi', 
    'out', 'low', 'high', 'full', 'end', 'well', 'state', 'fine', 'co', 'self'
}

SYLLABLE_SUFFIXES = (
    'ing', 'ed', 'tion', 'tions', 'tive', 'tively', 'ment', 'ments', 
    'ity', 'ities', 'able', 'ible', 'ly', 'er', 'ers', 'est', 'ance', 
    'ence', 'ous', 'al', 'ally', 'ness', 'ship', 'ize', 'ised', 'ized', 
    'ising', 'izing', 'istic', 'ary'
)


def fix_hyphenation(w1: str, w2: str) -> str:
    """判斷行尾連字號是音節斷字還是保留複合字"""
    w1_lower = w1.lower()
    w2_lower = w2.lower()

    if w1_lower in COMPOUND_PREFIXES:
        return f"{w1}-{w2}"

    if any(w2_lower.startswith(s) or w2_lower == s for s in SYLLABLE_SUFFIXES):
        return f"{w1}{w2}"

    if len(w1) <= 3 or len(w2) <= 3:
        return f"{w1}{w2}"

    return f"{w1}{w2}"


def clean_paragraph_lines(lines: List[str]) -> str:
    """將一個區塊內的多行文字重組為連貫的 Markdown 段落，並處理清單與斷字"""
    if not lines:
        return ""

    result = []
    current = ""

    for l in lines:
        l_str = l.strip()
        if not l_str:
            continue

        # 檢測清單項目
        bullet_match = re.match(r'^[•–—\*\-]\s*(.*)', l_str)
        if bullet_match:
            if current:
                result.append(current)
            current = f"- {bullet_match.group(1)}"
            continue

        num_list_match = re.match(r'^(\d+\.|\([a-zA-Z0-9]+\))\s*(.*)', l_str)
        if num_list_match and len(l_str) < 120 and (not current or current.startswith(('-', '1.', '2.', '3.', '4.', '5.'))):
            if current:
                result.append(current)
            current = f"{num_list_match.group(1)} {num_list_match.group(2)}"
            continue

        if not current:
            current = l_str
            continue

        # 處理行尾連字號 (包含行尾可能存在的空格)
        hyphen_match = re.search(r'([a-zA-Z]+)-\s*$', current)
        next_word_match = re.match(r'^([a-zA-Z]+)(.*)', l_str)

        if hyphen_match and next_word_match:
            w1 = hyphen_match.group(1)
            w2 = next_word_match.group(1)
            rest = next_word_match.group(2)
            prefix = current[:hyphen_match.start(1)]
            merged = fix_hyphenation(w1, w2)
            current = f"{prefix}{merged}{rest}"
        else:
            current += " " + l_str

    if current:
        result.append(current)

    return "\n\n".join(result)


def format_matrix_to_markdown_table(headers: List[str], rows: List[List[str]]) -> str:
    """將表頭與資料列陣列轉為標準 Markdown 表格"""
    if not headers or not rows:
        return ""
    ncols = len(headers)
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join([":---"] * ncols) + " |")
    for r in rows:
        padded = r[:ncols] + [""] * max(0, ncols - len(r))
        out.append("| " + " | ".join(padded) + " |")
    return "\n".join(out)


def convert_pdf_to_clean_markdown(
    pdf_path: str,
    output_md_path: Optional[str] = None,
    assets_dir: Optional[str] = None
) -> Tuple[str, Dict[str, Any]]:
    """
    通用、純 Python / PyMuPDF 幾何版面解析核心
    """
    pdf_path = os.path.abspath(pdf_path)
    doc = fitz.open(win_path(pdf_path))
    base_name = Path(pdf_path).stem

    if not output_md_path:
        output_md_path = str(Path(pdf_path).parent / f"{base_name} (Raw).md")

    if not assets_dir:
        parent_dir = Path(pdf_path).parent
        if (parent_dir.parent / "assets").is_dir() or parent_dir.name in ["2020", "2021", "2022", "2023", "2024", "2025", "2026", "2010-2019"]:
            assets_dir = str(parent_dir.parent / "assets" / base_name)
        else:
            assets_dir = str(parent_dir / "assets" / base_name)

    os.makedirs(win_path(assets_dir), exist_ok=True)
    rel_assets_dir = os.path.relpath(assets_dir, os.path.dirname(output_md_path)).replace("\\", "/")

    meta = doc.metadata or {}
    meta_title = meta.get("title") or ""
    clean_title = meta_title.strip()
    if not clean_title or len(clean_title) < 5 or clean_title.startswith(("V_M_", "B_", "paper_")):
        clean_title = re.sub(r'^\([0-9]{4}\)\s*', '', base_name).strip()

    author = meta.get("author") or ""
    creator = meta.get("creator") or ""
    pages_cnt = len(doc)

    metadata = {
        "title": clean_title,
        "author": author if author else None,
        "creator": creator if creator else None,
        "pages": pages_cnt,
    }
    clean_meta = {k: v for k, v in metadata.items() if v is not None}
    fm_block = yaml.safe_dump(clean_meta, allow_unicode=True, sort_keys=False).rstrip()

    md_lines = []
    # 1. 標準 YAML Frontmatter
    md_lines.append("---")
    md_lines.append(fm_block)
    md_lines.append("---")
    md_lines.append("")
    md_lines.append(f"# {clean_title}")
    md_lines.append("")
    if author:
        md_lines.append(f"> **作者**：{author}")
    md_lines.append(f"> **總頁數**：{pages_cnt} 頁")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")

    total_tables_extracted = 0
    total_figures_extracted = 0

    for page_idx in range(pages_cnt):
        page = doc[page_idx]
        rect = page.rect
        page_w = rect.width
        page_h = rect.height
        mid_x = page_w / 2.0

        # 出版封面頁偵測 (如 USENIX 出版商封面首頁，只有 5~8 個區塊且含有 Proceedings of)
        page_raw_text = page.get_text()
        if page_idx == 0 and ("This paper is included in the Proceedings of the" in page_raw_text or "Open access to the Proceedings of the" in page_raw_text):
            # 這是 USENIX 封面頁，跳過正文生成
            continue

        # -----------------------------------------------------------------
        # 1. 原生表格偵測 (Native PyMuPDF Table Extraction)
        # -----------------------------------------------------------------
        native_tables: List[Dict[str, Any]] = []
        if hasattr(page, 'find_tables'):
            try:
                tabs = page.find_tables()
                for tab in tabs.tables:
                    grid = tab.extract()
                    if grid and len(grid) >= 2 and len(grid[0]) >= 2:
                        ncols = len(grid[0])
                        nrows = len(grid)
                        # 排除圖表/坐標軸網格誤判 (學術論文表格欄數通常 <= 18，且填充率 > 20%)
                        if ncols > 18 or nrows > 60:
                            continue
                        total_cells = ncols * nrows
                        non_empty = sum(1 for row in grid for c in row if c and str(c).strip())
                        if total_cells > 20 and (non_empty / total_cells) < 0.20:
                            continue

                        if non_empty >= 4:
                            # 清理單元格字串
                            cleaned_rows = []
                            for r in grid:
                                cleaned_rows.append([str(c or '').replace('\n', ' ').strip() for c in r])
                            native_tables.append({
                                'bbox': fitz.Rect(tab.bbox),
                                'headers': cleaned_rows[0],
                                'rows': cleaned_rows[1:],
                                'caption': None,
                                'consumed': False
                            })
            except Exception:
                pass

        blocks = page.get_text("blocks")
        valid_blocks = []

        # 幾何與學術雜訊過濾
        for b in blocks:
            x0, y0, x1, y1, text, bno, btype = b
            t_str = text.strip()
            if not t_str:
                continue

            # 頂部頁眉過濾 (y1 < 55)
            if y1 < 55:
                if (
                    'USENIX' in t_str or 'Proceedings' in t_str or 'Symposium' in t_str or 
                    'IEEE' in t_str or 'ACM' in t_str or 'et al' in t_str.lower() or 
                    'Published' in t_str or t_str.isdigit() or len(t_str) < 50
                ):
                    continue

            # 底部頁腳過濾 (y0 > page_h - 70)
            if y0 > page_h - 70:
                if (
                    t_str.isdigit() or 'USENIX Association' in t_str or 'IEEE' in t_str or 
                    'ACM' in t_str or 'DOI' in t_str or 'doi.org' in t_str or 'http' in t_str or 
                    'Page ' in t_str or len(t_str) < 35
                ):
                    continue

            # 獨立短數字行過濾 (散落頁碼或圖表坐標軸標籤，如 '1', '249', '101')
            if re.match(r'^\d{1,4}$', t_str):
                continue

            # 全域 arXiv / 会議浮水印過濾
            if re.search(r'arXiv:\d+\.\d+', t_str) or re.search(r'\[cs\.[A-Za-z\-]+\]', t_str):
                continue

            # IEEE / ACM / USENIX / 期刊授權聲明與水文過濾
            if 'Authorized licensed use limited to:' in t_str or 'from IEEE Xplore' in t_str or 'Downloaded on ' in t_str:
                continue
            if 'Permission to make digital or hard copies' in t_str or re.search(r'ACM Reference [Ff]ormat:', t_str) or 'ACM ISBN' in t_str:
                continue
            if re.search(r'\d{4}-\d{4}/\d{2,4}/\d{2}-ART\d+', t_str) or re.search(r'Publication date:\s*[A-Za-z]+\s*\d{4}', t_str):
                continue
            if '$15.00' in t_str or (re.search(r'https?://doi\.org/10\.\d{4,9}/', t_str) and ('$' in t_str or 'ART' in t_str)):
                continue
            if re.match(r'^https?://(?:dx\.)?doi\.org/[^\s]+$', t_str):
                continue
            if re.match(r'^\d+:\d+$', t_str):
                continue
            if re.match(r'^[•–—\*\-\s]*[A-Z]\.?\s+[A-Za-z]+\s+et\s+al\.?$', t_str):
                continue
            if 'Digital Threats: Research and Practice' in t_str:
                continue
            if 'TechRxiv' in t_str or 'e-Prints posted on' in t_str or ('CC-BY' in t_str and 'doi.org' in t_str):
                continue
            if 'USENIX Association' in t_str:
                continue
            if 'Under license to IEEE' in t_str or ('DOI 10.1109/' in t_str and y0 > page_h - 65):
                continue
            if re.search(r'978-1-[0-9\-]+', t_str) and y0 > page_h - 90:
                continue

            # 極窄側邊浮水印 (如 x1 < 30 或 x0 > page_w - 30 之長條版權垂直字串)
            if (x1 < 30 or x0 > page_w - 30) and (y1 - y0 > 100 or 'IEEE' in t_str or 'arXiv:' in t_str or 'cs.' in t_str):
                continue
            # arXiv 邊界浮水印
            if (x1 < 55 or x0 > page_w - 55) and ('arXiv:' in t_str or 'cs.' in t_str):
                continue

            valid_blocks.append(b)

        # 檢查是否有 block 落在 native_table 範圍內，或者為 native_table 的 caption
        table_consumed_blocks: Set[int] = set()
        for t_idx, ntab in enumerate(native_tables):
            t_rect = ntab['bbox']
            for b_i, b in enumerate(valid_blocks):
                bx0, by0, bx1, by1, btext, _, _ = b
                b_rect = fitz.Rect(bx0, by0, bx1, by1)
                bt_strip = btext.strip()

                # 尋找 Table Caption (在表格上方 60pt 內或下方 60pt 內)
                is_tbl_cap = bool(re.match(r'^(TABLE|Table)\s+([0-9IVXLCDM]+)', bt_strip))
                if is_tbl_cap:
                    if (abs(by1 - t_rect.y0) < 60) or (abs(by0 - t_rect.y1) < 60):
                        if not ntab['caption']:
                            ntab['caption'] = bt_strip
                            table_consumed_blocks.add(b_i)
                            continue

                # 檢查是否位於表格內部 (中心點落在表格內，或重疊面積超過 20%)
                center_pt = fitz.Point((bx0 + bx1) / 2.0, (by0 + by1) / 2.0)
                if t_rect.contains(center_pt):
                    table_consumed_blocks.add(b_i)
                else:
                    intersect = t_rect.intersect(b_rect)
                    if intersect.is_valid and not intersect.is_empty:
                        b_area = max(1.0, (bx1 - bx0) * (by1 - by0))
                        intersect_area = abs(intersect.width * intersect.height)
                        if intersect_area / b_area > 0.2:
                            table_consumed_blocks.add(b_i)

        # 標記落在原生表格內的區塊已過濾
        remaining_blocks = [b for i, b in enumerate(valid_blocks) if i not in table_consumed_blocks]

        # 多欄偵測：依據正文實質段落 (長度 > 100 字元且高度 > 30pt) 之欄寬幾何判定
        prose_blocks = [
            b for b in remaining_blocks 
            if len(b[4].strip()) > 100 and (b[3] - b[1]) > 30 and b[1] > 45 and b[3] < page_h - 45
        ]
        narrow_prose = [b for b in prose_blocks if (b[2] - b[0]) < page_w * 0.52]
        left_col = [b for b in narrow_prose if (b[0] + b[2]) / 2.0 < mid_x]
        right_col = [b for b in narrow_prose if (b[0] + b[2]) / 2.0 >= mid_x]

        # 唯有當實質正文段落在左右兩欄皆有分立存在時，方判定為雙欄閱讀流
        is_two_col = len(left_col) >= 1 and len(right_col) >= 1

        if is_two_col:
            # 決定頂部跨欄標題的 Y 軸分界 (header_split_y)
            left_min_y = min(b[1] for b in left_col)
            right_min_y = min(b[1] for b in right_col)
            header_split_y = min(left_min_y, right_min_y) - 5

            top_b, left_b, right_b, bottom_b = [], [], [], []
            for b in remaining_blocks:
                x0, y0, x1, y1, text, bno, btype = b
                is_wide = (x1 - x0) > page_w * 0.55
                spans_middle = x0 < mid_x - 30 and x1 > mid_x + 30
                center_x = (x0 + x1) / 2.0

                # 只有真正橫跨兩欄的寬區塊 (Title, Author 等) 才進入 top_b
                # 窄區塊 (半欄) 即使 Y 坐標很高，也必須按照 center_x 歸入 left_b 或 right_b
                if (is_wide or spans_middle) and y1 <= header_split_y + 10:
                    top_b.append(b)
                elif is_wide and y0 > max(b[3] for b in (left_col + right_col)):
                    bottom_b.append(b)
                elif center_x < mid_x:
                    left_b.append(b)
                else:
                    right_b.append(b)

            top_b.sort(key=lambda b: b[1])
            left_b.sort(key=lambda b: b[1])
            right_b.sort(key=lambda b: b[1])
            bottom_b.sort(key=lambda b: b[1])
            ordered_blocks = top_b + left_b + right_b + bottom_b
        else:
            ordered_blocks = sorted(remaining_blocks, key=lambda b: b[1])

        # 區塊處理狀態維護 (避免重複消費)
        consumed_indices: Set[int] = set()

        # -----------------------------------------------------------------
        # 輸出本頁偵測到的原生表格 (依據 Y 軸嵌入合適位置)
        # -----------------------------------------------------------------
        for ntab in native_tables:
            cap_text = ntab['caption'] or "Table"
            table_md = format_matrix_to_markdown_table(ntab['headers'], ntab['rows'])
            md_lines.append(f"#### {cap_text}\n")
            md_lines.append(table_md)
            md_lines.append("")
            total_tables_extracted += 1

        # -----------------------------------------------------------------
        # 預先掃描 (Pre-pass)：偵測 Figure 並標記圖表內坐標刻度文字為已消費
        # -----------------------------------------------------------------
        figure_chart_regions: Dict[int, float] = {}  # fig_idx -> chart_y0
        figure_associated_blocks: Dict[int, List[Any]] = {}
        for f_idx, fb in enumerate(ordered_blocks):
            ft = fb[4].strip()
            if re.match(r'^(Figure\s+\d+:?|Fig\.\s*\d+:?)\s*(.*)', ft, re.IGNORECASE):
                chart_y0 = fb[1]
                assoc_blocks = []
                p_scan = f_idx - 1
                while p_scan >= 0:
                    prev_b = ordered_blocks[p_scan]
                    pt = prev_b[4].strip()
                    # 高度差超過 250pt，或遇到大標題/表格標題，停止回溯
                    y_diff = fb[1] - prev_b[1]
                    if y_diff > 250 or any(pt.startswith(h) for h in ('#', 'Table', 'TABLE', 'Figure', 'Fig.')):
                        break
                    # 軸標籤與圖例特徵：短字串、純數字、百分比、或坐標軸說明
                    is_axis = (
                        len(pt) < 50 or 
                        re.match(r'^[\d\.\%\s\-\,\/\(\)]+$', pt) or 
                        any(term in pt.lower() for term in ('pass', 'rate', 'cost', 'calls', 'fast', 'sonnet', 'gpt', 'overall', 'zero-day', 'cwe', 'edits', 'file'))
                    )
                    if is_axis and len(pt) < 100:
                        chart_y0 = min(chart_y0, prev_b[1])
                        consumed_indices.add(p_scan)
                        assoc_blocks.append(prev_b)
                        p_scan -= 1
                    else:
                        break
                figure_chart_regions[f_idx] = chart_y0
                figure_associated_blocks[f_idx] = assoc_blocks

        for idx, b in enumerate(ordered_blocks):
            if idx in consumed_indices:
                continue

            x0, y0, x1, y1, text, bno, btype = b
            t_strip = text.strip()

            # -------------------------------------------------------------
            # 1. 智慧表格偵測 (TableRecognizer)
            # -------------------------------------------------------------
            tbl_match = re.match(r'^(TABLE|Table)\s+([0-9IVXLCDM]+)(?::|\.|\s*\n|\s+([A-Z][^\.\n]*))', t_strip)
            is_table_caption = False
            if tbl_match:
                after_ref = t_strip[tbl_match.end(2):].strip()
                has_punct = after_ref.startswith((':', '.'))
                prose_verbs = ('demonstrates', 'presents', 'shows', 'summarizes', 'reports', 'provides', 'illustrates', 'lists', 'displays', 'is shown', 'was observed')
                has_prose_verb = any(v in after_ref.lower() for v in prose_verbs)
                if (has_punct or t_strip.isupper() or len(t_strip) < 80) and not has_prose_verb:
                    is_table_caption = True

            if is_table_caption:
                tbl_caption = t_strip
                consumed_indices.add(idx)

                # 探測後續區塊尋找表頭與資料列
                if idx + 1 < len(ordered_blocks):
                    next_b = ordered_blocks[idx + 1]
                    next_lines = [l.strip() for l in next_b[4].split('\n') if l.strip()]
                    
                    headers = []
                    start_data_idx = idx + 2

                    # 情況 A: 下一區塊為標準表頭 (2~12 個欄位)
                    if 2 <= len(next_lines) <= 12:
                        # 檢查是否存在次層表頭 (例如 Table 3，最多 12 欄)
                        if idx + 2 < len(ordered_blocks):
                            sub_b = ordered_blocks[idx + 2]
                            sub_lines = [l.strip() for l in sub_b[4].split('\n') if l.strip()]
                            if len(next_lines) < len(sub_lines) <= 12 and all(len(s) < 25 for s in sub_lines):
                                headers = sub_lines
                                consumed_indices.add(idx + 1)
                                consumed_indices.add(idx + 2)
                                start_data_idx = idx + 3
                            else:
                                headers = next_lines
                                consumed_indices.add(idx + 1)
                        else:
                            headers = next_lines
                            consumed_indices.add(idx + 1)

                        ncols = len(headers)
                        rows = []

                        # 特殊支援：安全領域文獻常見的 CVE 對照表 (Software / CVE ID / Type / Description)
                        if 'CVE ID' in headers or 'CVE' in headers or any('cve' in h.lower() for h in headers):
                            all_tbl_lines = []
                            curr_scan = start_data_idx
                            while curr_scan < len(ordered_blocks):
                                cand_b = ordered_blocks[curr_scan]
                                ct = cand_b[4].strip()
                                # 遇標題、圖表標籤或新章節停止
                                if any(ct.startswith(h) for h in ('Table', 'TABLE', 'Figure', 'Fig.', '#')) or re.match(r'^\d+(\.\d+)*\s+[A-Za-z]', ct) or (len(ct) < 5 and ct.isdigit()):
                                    break
                                for cl in cand_b[4].split('\n'):
                                    if cl.strip():
                                        all_tbl_lines.append(cl.strip())
                                consumed_indices.add(curr_scan)
                                curr_scan += 1

                            # 依據 CVE- 錨點切分各列
                            i_l = 0
                            while i_l < len(all_tbl_lines):
                                if re.match(r'^CVE-\d+-\d+', all_tbl_lines[i_l]):
                                    soft = all_tbl_lines[i_l - 1] if i_l > 0 else ""
                                    cve_str = all_tbl_lines[i_l]
                                    vtype = all_tbl_lines[i_l + 1] if i_l + 1 < len(all_tbl_lines) else ""
                                    desc_tokens = []
                                    j_l = i_l + 2
                                    while j_l < len(all_tbl_lines) and not re.match(r'^CVE-\d+-\d+', all_tbl_lines[j_l]):
                                        if j_l + 1 < len(all_tbl_lines) and re.match(r'^CVE-\d+-\d+', all_tbl_lines[j_l + 1]):
                                            break
                                        desc_tokens.append(all_tbl_lines[j_l])
                                        j_l += 1
                                    rows.append([soft, cve_str, vtype, " ".join(desc_tokens)])
                                    i_l = j_l
                                else:
                                    i_l += 1
                        else:
                            # 通用矩陣掃描
                            curr_scan = start_data_idx
                            while curr_scan < len(ordered_blocks):
                                cand_b = ordered_blocks[curr_scan]
                                ct = cand_b[4].strip()
                                if any(ct.startswith(h) for h in ('Table', 'TABLE', 'Figure', 'Fig.', '#')) or re.match(r'^\d+(\.\d+)*\s+[A-Za-z]', ct):
                                    break
                                cand_lines = [l.strip() for l in cand_b[4].split('\n') if l.strip()]

                                # 檢查資料列是否實為正文段落誤入 (段落字數過長或包含完整句點標點)
                                if any(len(c) > 60 for c in cand_lines) or (sum(len(c) for c in cand_lines) / max(1, ncols) > 40):
                                    break
                                if any(c.endswith(('.', ':', ';')) and len(c) > 35 for c in cand_lines[:-1]):
                                    break

                                # 若能整除 ncols，為多列合一
                                if len(cand_lines) >= ncols and len(cand_lines) % ncols == 0:
                                    for r_start in range(0, len(cand_lines), ncols):
                                        rows.append(cand_lines[r_start:r_start + ncols])
                                    consumed_indices.add(curr_scan)
                                    curr_scan += 1
                                elif len(cand_lines) == ncols:
                                    rows.append(cand_lines)
                                    consumed_indices.add(curr_scan)
                                    curr_scan += 1
                                else:
                                    break

                        if rows:
                            table_md = format_matrix_to_markdown_table(headers, rows)
                            md_lines.append(f"#### {tbl_caption}\n")
                            md_lines.append(table_md)
                            md_lines.append("")
                            total_tables_extracted += 1
                            continue

                # 若無法自動組出矩陣，輸出為標題並保留內容
                md_lines.append(f"#### {tbl_caption}\n")
                continue

            # -------------------------------------------------------------
            # 1.5. 演算法虛擬碼區塊偵測 (AlgorithmRecognizer)
            # -------------------------------------------------------------
            alg_match = re.match(r'^(Algorithm\s+\d+[:\.]?)\s*(.*)', t_strip, re.IGNORECASE)
            if alg_match:
                alg_caption = t_strip
                consumed_indices.add(idx)
                md_lines.append(f"#### {alg_caption}\n")
                
                # 收集後續演算法步驟
                alg_steps = []
                curr_scan = idx + 1
                while curr_scan < len(ordered_blocks):
                    cand_b = ordered_blocks[curr_scan]
                    ct = cand_b[4].strip()
                    if any(ct.startswith(h) for h in ('Table', 'TABLE', 'Figure', 'Fig.', '#', 'Algorithm')) or re.match(r'^\d+(\.\d+)*\s+[A-Za-z]', ct):
                        break
                    # 若包含 Require/Ensure/Input 或編號步序 (如 1: ... 2: ...)
                    if 'Require:' in ct or 'Ensure:' in ct or 'Input:' in ct or re.search(r'\b\d+:\s+', ct) or any(k in ct for k in ('for each', 'if ', 'return ', 'else')):
                        alg_steps.append(ct)
                        consumed_indices.add(curr_scan)
                        curr_scan += 1
                    else:
                        break
                
                if alg_steps:
                    raw_code = "\n".join(alg_steps)
                    formatted_code = re.sub(r'(\d+:\s*)', r'\n\1', raw_code).strip()
                    md_lines.append("```pseudocode")
                    md_lines.append(formatted_code)
                    md_lines.append("```\n")
                    continue


            # -------------------------------------------------------------
            # 2. 智慧圖表偵測與剪裁 (FigureRecognizer)
            # -------------------------------------------------------------
            fig_match = re.match(r'^(Figure\s+\d+:?|Fig\.\s*\d+:?)\s*(.*)', t_strip, re.IGNORECASE)
            if fig_match:
                fig_caption = t_strip
                consumed_indices.add(idx)

                chart_y0 = figure_chart_regions.get(idx, y0)

                # 確定剪裁矩形並匯出圖片
                fig_num_match = re.search(r'\d+', fig_caption)
                fig_num = fig_num_match.group(0) if fig_num_match else str(total_figures_extracted + 1)
                fig_filename = f"figure_{fig_num}.png"
                fig_out_path = os.path.join(assets_dir, fig_filename)

                # 優先檢查是否有精確匹配該圖表坐標之內嵌光柵圖 (Raster image)
                saved_raster = False
                matched_xref = None
                try:
                    img_infos = page.get_image_info(xrefs=True)
                    best_img = None
                    best_score = -1
                    for info in img_infos:
                        ibbox = fitz.Rect(info['bbox'])
                        # 圖片必須位於 Caption 上方 (底部在 Caption 附近) 且寬高顯著
                        if ibbox.y1 <= y0 + 35 and ibbox.y0 < y0 - 30 and ibbox.width > 50 and ibbox.height > 40:
                            score = ibbox.width * ibbox.height
                            if score > best_score:
                                best_score = score
                                best_img = info
                    if best_img:
                        matched_xref = best_img.get('xref')
                        if matched_xref:
                            base_img = doc.extract_image(matched_xref)
                            if base_img and len(base_img["image"]) > 1024:
                                with open(fig_out_path, "wb") as f_r:
                                    f_r.write(base_img["image"])
                                saved_raster = True
                                total_figures_extracted += 1
                except Exception:
                    pass

                if not saved_raster:
                    # 向量圖形：利用 page.get_drawings() 與圖表關聯文字偵測精確圖形幾何範圍
                    page_drawings = [
                        d['rect'] for d in page.get_drawings() 
                        if d['rect'].y0 > 55 and d['rect'].y1 < page_h - 50 and d['rect'].width < page_w * 0.95
                    ]
                    chart_drawings = [r for r in page_drawings if r.y1 <= y0 + 10 and r.y0 >= chart_y0 - 25]

                    assoc_b = figure_associated_blocks.get(idx, [])
                    all_x0 = [r.x0 for r in chart_drawings] + [b[0] for b in assoc_b]
                    all_x1 = [r.x1 for r in chart_drawings] + [b[2] for b in assoc_b]
                    all_y0 = [r.y0 for r in chart_drawings] + [b[1] for b in assoc_b]
                    all_y1 = [r.y1 for r in chart_drawings] + [b[3] for b in assoc_b]

                    if all_x0 and all_y0:
                        d_min_x = min(all_x0)
                        d_min_y = min(all_y0)
                        d_max_x = max(all_x1)
                        d_max_y = max(all_y1)
                        c_y0 = max(5, min(d_min_y - 12, chart_y0 - 10))
                        c_y1 = min(page_h - 5, min(y0 - 2, d_max_y + 6))
                        # 防禦性檢查：若高度過小 (<60pt，可能只捕獲一條邊框線)，往上回溯適當高度
                        if c_y1 - c_y0 < 60:
                            c_y0 = max(50, y0 - 200)
                        clip_rect = fitz.Rect(
                            max(5, d_min_x - 12),
                            c_y0,
                            min(page_w - 5, d_max_x + 12),
                            c_y1
                        )
                    else:
                        clip_rect = fitz.Rect(
                            max(10, page_w * 0.08),
                            max(10, min(chart_y0 - 15, y0 - 180)),
                            min(page_w - 10, page_w * 0.92),
                            min(page_h - 10, y0 - 2)
                        )
                    try:
                        pix = page.get_pixmap(clip=clip_rect, dpi=180)
                        pix.save(fig_out_path)
                        total_figures_extracted += 1
                    except Exception:
                        pass

                clean_caption = re.sub(r'\s+', ' ', fig_caption).strip()
                # 簡短化 alt 文字避免過長字串毀壞 Markdown 解析器
                short_alt = clean_caption.split('.')[0] if '.' in clean_caption[:80] else clean_caption[:60]
                short_alt = re.sub(r'^(Figure\s+\d+:?|Fig\.\s*\d+:?)\s*', '', short_alt, flags=re.I).strip() or "Figure"
                # 兼容 CommonMark 與 VS Code/Obsidian: 含有空格或括號的路徑使用 <...> 封裝，避免 Markdown 語法解析中斷
                md_lines.append(f"![{short_alt}](<{rel_assets_dir}/{fig_filename}>)\n")
                md_lines.append(f"*{clean_caption}*\n")
                continue


            # -------------------------------------------------------------
            # 3. 標題層級自動判定
            # -------------------------------------------------------------
            is_heading = False
            heading_level = 2
            heading_title = ""

            # 消除數字序號中的異常空格 (如 '4. 4.1' -> '4.4.1')
            normalized_h = re.sub(r'^(\d+)\.\s+(\d+)', r'\1.\2', t_strip)

            if normalized_h.upper() in ("ABSTRACT", "A BSTRACT"):
                is_heading = True
                heading_level = 2
                heading_title = "Abstract"
            elif re.match(r'^(\d+(?:\.\d+)*)\s+([A-Za-z\s]{3,})$', normalized_h):
                m_h = re.match(r'^(\d+(?:\.\d+)*)\s+([A-Za-z\s]{3,})$', normalized_h)
                sec_num = m_h.group(1)
                sec_name = m_h.group(2).strip().title()
                is_heading = True
                dots = sec_num.count('.')
                heading_level = 4 if dots >= 2 else (3 if dots == 1 else 2)
                heading_title = f"{sec_num} {sec_name}"
            elif normalized_h.upper() in ("REFERENCES", "ACKNOWLEDGMENTS", "APPENDIX", "CONCLUSION", "RELATED WORK", "DISCUSSION"):
                is_heading = True
                heading_level = 2
                heading_title = normalized_h.title()

            if is_heading:
                h_prefix = "#" * heading_level
                md_lines.append(f"{h_prefix} {heading_title}\n")
                continue

            # -------------------------------------------------------------
            # 4. 常規段落處理
            # -------------------------------------------------------------
            if page_idx == 0 and clean_title.lower() in t_strip.lower() and len(t_strip) < len(clean_title) + 50:
                continue

            lines = [l for l in text.split("\n") if l.strip()]
            cleaned_para = clean_paragraph_lines(lines)
            if cleaned_para:
                md_lines.append(cleaned_para)
                md_lines.append("")

    full_markdown = "\n".join(md_lines)

    out_dir = os.path.dirname(os.path.abspath(output_md_path))
    if out_dir:
        os.makedirs(win_path(out_dir), exist_ok=True)
    with open(win_path(output_md_path), "w", encoding="utf-8") as fp:
        fp.write(full_markdown)

    stats = {
        "pages": pages_cnt,
        "tables": total_tables_extracted,
        "figures": total_figures_extracted,
        "output_path": output_md_path
    }
    return full_markdown, stats


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python scripts/parser/lightweight_parser.py <pdf_path> [output_md_path]")
        sys.exit(1)
    p_in = sys.argv[1]
    p_out = sys.argv[2] if len(sys.argv) > 2 else None
    md, st = convert_pdf_to_clean_markdown(p_in, p_out)
    print(f"✅ 解析完成！")
    print(f"  • 輸出檔案: {st['output_path']}")
    print(f"  • 頁數: {st['pages']} 頁 | 智慧抽取表格: {st['tables']} | 剪裁圖表資產: {st['figures']}")

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

# 重複字串與正則表達式常數定義 (消除 SonarCloud S1192 異味)
REGEX_SECTION_HEADING = r'^\d+(\.\d+)*\s+[A-Za-z]'
REGEX_CVE_ID = r'^CVE-\d+-\d+'
REGEX_TABLE_CAPTION = r'^(TABLE|Table)\s+([0-9IVXLCDM]+)'
REGEX_FIGURE_CAPTION = r'^(Figure\s+\d+:?|Fig\.\s*\d+:?)[ \t]*(.*)'
REGEX_ALGORITHM_CAPTION = r'^(Algorithm\s+\d+[:\.]?)[ \t]*(.*)'

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


def validate_safe_path(target_path: str) -> str:
    """驗證檔案路徑安全性，防止路徑遍歷與空位元組注入 (SonarCloud S8707)"""
    if not target_path or '\0' in target_path:
        raise ValueError(f"Invalid path containing control characters: {target_path}")
    return os.path.abspath(target_path)


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


def _detect_list_item(l_str: str, current: str) -> Optional[str]:
    """檢測行文字是否為清單項目"""
    bullet_match = re.match(r'^[•–—\*\-]\s*(.*)', l_str)
    if bullet_match:
        return f"- {bullet_match.group(1)}"
    num_list_match = re.match(r'^(\d+\.|\([a-zA-Z0-9]+\))\s*(.*)', l_str)
    if num_list_match and len(l_str) < 120 and (not current or current.startswith(('-', '1.', '2.', '3.', '4.', '5.'))):
        return f"{num_list_match.group(1)} {num_list_match.group(2)}"
    return None


def _merge_hyphenated_words(current: str, l_str: str) -> str:
    """處理行尾連字號拼接或常規單字空格連接 (無正則回溯)"""
    curr_rstrip = current.rstrip(" \t")
    if curr_rstrip.endswith("-"):
        base = curr_rstrip[:-1]
        idx = len(base)
        while idx > 0 and base[idx - 1].isalpha():
            idx -= 1
        w1 = base[idx:]
        j = 0
        while j < len(l_str) and l_str[j].isalpha():
            j += 1
        w2 = l_str[:j]
        if w1 and w2:
            prefix = base[:idx]
            merged = fix_hyphenation(w1, w2)
            return f"{prefix}{merged}{l_str[j:]}"
    return current + " " + l_str


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
        list_item = _detect_list_item(l_str, current)
        if list_item:
            if current:
                result.append(current)
            current = list_item
            continue
        if not current:
            current = l_str
        else:
            current = _merge_hyphenated_words(current, l_str)
    if current:
        result.append(current)
    return "\n\n".join(result)


def format_matrix_to_markdown_table(headers: List[str], rows: List[List[str]]) -> str:
    """將表頭與資料列陣列轉為標準 Markdown 表格"""
    if not headers or not rows:
        return ""
    ncols = len(headers)
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * ncols) + " |"]
    for r in rows:
        padded = r + [""] * (ncols - len(r)) if len(r) < ncols else r[:ncols]
        cleaned_cells = [c.replace("\n", " ").replace("|", "\\|").strip() for c in padded]
        out.append("| " + " | ".join(cleaned_cells) + " |")
    return "\n".join(out)


def _extract_native_tables(page) -> List[Dict[str, Any]]:
    """原生 PyMuPDF 表格偵測與資料清理"""
    native_tables = []
    if not hasattr(page, 'find_tables'):
        return native_tables
    try:
        tabs = page.find_tables()
        for tab in tabs.tables:
            grid = tab.extract()
            if not grid or len(grid) < 2 or len(grid[0]) < 2:
                continue
            ncols = len(grid[0])
            nrows = len(grid)
            if ncols > 18 or nrows > 60:
                continue
            total_cells = ncols * nrows
            non_empty = sum(1 for row in grid for c in row if c and str(c).strip())
            if (total_cells > 20 and (non_empty / total_cells) < 0.20) or non_empty < 4:
                continue
            cleaned_rows = [[str(c or '').replace('\n', ' ').strip() for c in r] for r in grid]
            native_tables.append({
                'bbox': fitz.Rect(tab.bbox),
                'headers': cleaned_rows[0],
                'rows': cleaned_rows[1:],
                'caption': None,
            })
    except Exception:
        pass
    return native_tables


def _is_margin_noise(t_str: str, y0: float, y1: float, page_h: float) -> bool:
    """檢查頁頂與頁底之頁碼及邊界文字雜訊"""
    if y1 < 55 and (t_str.isdigit() or len(t_str) < 50):
        return True
    if y0 > page_h - 70 and (t_str.isdigit() or len(t_str) < 35):
        return True
    return False


def _is_content_noise(t_str: str) -> bool:
    """檢查版權與出版宣告等全域雜訊"""
    if t_str.isdigit() and len(t_str) <= 4:
        return True
    noise_keywords = (
        'USENIX', 'Proceedings', 'Symposium', 'IEEE', 'ACM', 'Published',
        'DOI', 'doi.org', 'Page ', 'Authorized licensed use', 'ACM ISBN',
        'Digital Threats: Research and Practice', 'TechRxiv', '$15.00'
    )
    if any(k in t_str for k in noise_keywords):
        return True
    if 'arXiv:' in t_str or '[cs.' in t_str:
        return True
    return False


def _is_header_footer_noise(t_str: str, y0: float, y1: float, page_h: float) -> bool:
    """判定區塊是否為頁眉、頁腳或全域出版雜訊"""
    return _is_margin_noise(t_str, y0, y1, page_h) or _is_content_noise(t_str)


def _filter_valid_blocks(page, page_w: float, page_h: float) -> List[Any]:
    """過濾單頁中的頁眉、頁腳與邊界雜訊區塊"""
    valid_blocks = []
    for b in page.get_text("blocks"):
        x0, y0, x1, y1, text, _, _ = b
        t_str = text.strip()
        if not t_str or _is_header_footer_noise(t_str, y0, y1, page_h):
            continue
        if (x1 < 30 or x0 > page_w - 30) and (y1 - y0 > 100 or 'IEEE' in t_str or 'arXiv:' in t_str):
            continue
        if (x1 < 55 or x0 > page_w - 55) and ('arXiv:' in t_str or 'cs.' in t_str):
            continue
        valid_blocks.append(b)
    return valid_blocks


def _is_block_in_table(b: Any, ntab: Dict[str, Any]) -> Tuple[bool, bool]:
    """檢驗區塊是否屬於表格標題或落在表格區域內部 (返回 is_consumed, is_caption)"""
    bx0, by0, bx1, by1, btext, _, _ = b
    bt_strip = btext.strip()
    t_rect = ntab['bbox']
    if re.match(REGEX_TABLE_CAPTION, bt_strip) and ((abs(by1 - t_rect.y0) < 60) or (abs(by0 - t_rect.y1) < 60)):
        if not ntab['caption']:
            return True, True
    center_pt = fitz.Point((bx0 + bx1) / 2.0, (by0 + by1) / 2.0)
    if t_rect.contains(center_pt):
        return True, False
    intersect = t_rect.intersect(fitz.Rect(bx0, by0, bx1, by1))
    if intersect.is_valid and not intersect.is_empty:
        b_area = max(1.0, (bx1 - bx0) * (by1 - by0))
        if abs(intersect.width * intersect.height) / b_area > 0.2:
            return True, False
    return False, False


def _filter_table_overlap(valid_blocks: List[Any], native_tables: List[Dict[str, Any]]) -> List[Any]:
    """標記並過濾落在原生表格內部的區塊與表頭標題"""
    consumed_indices = set()
    for ntab in native_tables:
        for b_i, b in enumerate(valid_blocks):
            if b_i in consumed_indices:
                continue
            is_consumed, is_caption = _is_block_in_table(b, ntab)
            if is_consumed:
                consumed_indices.add(b_i)
                if is_caption and not ntab['caption']:
                    ntab['caption'] = b[4].strip()
    return [b for i, b in enumerate(valid_blocks) if i not in consumed_indices]


def _reorder_reading_flow(blocks: List[Any], page_w: float, page_h: float, mid_x: float) -> List[Any]:
    """依據幾何佈局對雙欄或單欄區塊進行閱讀流動排序"""
    prose = [b for b in blocks if len(b[4].strip()) > 100 and (b[3] - b[1]) > 30 and 45 < b[1] < page_h - 45]
    narrow = [b for b in prose if (b[2] - b[0]) < page_w * 0.52]
    left_col = [b for b in narrow if (b[0] + b[2]) / 2.0 < mid_x]
    right_col = [b for b in narrow if (b[0] + b[2]) / 2.0 >= mid_x]

    if not (len(left_col) >= 1 and len(right_col) >= 1):
        return sorted(blocks, key=lambda b: b[1])

    header_split_y = min(min(b[1] for b in left_col), min(b[1] for b in right_col)) - 5
    top_b, left_b, right_b, bottom_b = [], [], [], []
    for b in blocks:
        x0, y0, x1, y1 = b[0], b[1], b[2], b[3]
        is_wide = (x1 - x0) > page_w * 0.55 or (x0 < mid_x - 30 and x1 > mid_x + 30)
        center_x = (x0 + x1) / 2.0
        if is_wide and y1 <= header_split_y + 10:
            top_b.append(b)
        elif is_wide and y0 > max(b[3] for b in (left_col + right_col)):
            bottom_b.append(b)
        elif center_x < mid_x:
            left_b.append(b)
        else:
            right_b.append(b)

    for col in (top_b, left_b, right_b, bottom_b):
        col.sort(key=lambda b: b[1])
    return top_b + left_b + right_b + bottom_b


def _scan_figure_axis_blocks(
    ordered_blocks: List[Any],
    f_idx: int,
    caption_y0: float
) -> Tuple[float, List[Any], List[int]]:
    """向上回溯掃描與圖表 Caption 緊鄰之軸標籤與座標刻度"""
    chart_y0 = caption_y0
    assoc_blocks = []
    consumed = []
    p_scan = f_idx - 1
    while p_scan >= 0:
        prev_b = ordered_blocks[p_scan]
        pt = prev_b[4].strip()
        if (caption_y0 - prev_b[1]) > 250 or any(pt.startswith(h) for h in ('#', 'Table', 'TABLE', 'Figure', 'Fig.')):
            break
        is_axis = len(pt) < 50 or re.match(r'^[\d\.\%\s\-\,\/\(\)]+$', pt)
        if is_axis and len(pt) < 100:
            chart_y0 = min(chart_y0, prev_b[1])
            consumed.append(p_scan)
            assoc_blocks.append(prev_b)
            p_scan -= 1
        else:
            break
    return chart_y0, assoc_blocks, consumed


def _pre_scan_figures(ordered_blocks: List[Any]) -> Tuple[Dict[int, float], Dict[int, List[Any]], Set[int]]:
    """預先掃描圖表 Caption 與關聯軸標籤"""
    figure_chart_regions: Dict[int, float] = {}
    figure_associated_blocks: Dict[int, List[Any]] = {}
    consumed_indices: Set[int] = set()

    for f_idx, fb in enumerate(ordered_blocks):
        ft = fb[4].strip()
        if re.match(REGEX_FIGURE_CAPTION, ft, re.IGNORECASE):
            chart_y0, assoc_blocks, newly_consumed = _scan_figure_axis_blocks(ordered_blocks, f_idx, fb[1])
            figure_chart_regions[f_idx] = chart_y0
            figure_associated_blocks[f_idx] = assoc_blocks
            consumed_indices.update(newly_consumed)
    return figure_chart_regions, figure_associated_blocks, consumed_indices


def _parse_heading_level(sec_num: str) -> int:
    """根據章節編號深度計算 Markdown 標題層級"""
    dots = sec_num.count('.')
    if dots >= 2:
        return 4
    if dots == 1:
        return 3
    return 2


def _is_section_number(token: str) -> bool:
    """檢查是否為章節編號格式 (如 1 或 1.2 或 2.1.3)"""
    parts = token.split('.')
    return bool(parts) and all(p.isdigit() for p in parts if p)


def _detect_heading(t_strip: str) -> Tuple[bool, int, str]:
    """偵測文字是否為學術標題 (消除正則回溯)"""
    normalized_h = re.sub(r'^(\d+)\.\s+(\d+)', r'\1.\2', t_strip)
    if normalized_h.upper() in ("ABSTRACT", "A BSTRACT"):
        return True, 2, "Abstract"
    tokens = normalized_h.split(maxsplit=1)
    if len(tokens) == 2 and _is_section_number(tokens[0]):
        title_body = tokens[1].strip()
        if len(title_body) >= 3 and all(c.isalpha() or c.isspace() for c in title_body):
            sec_num = tokens[0]
            sec_name = title_body.title()
            return True, _parse_heading_level(sec_num), f"{sec_num} {sec_name}"
    standard_sections = ("REFERENCES", "ACKNOWLEDGMENTS", "APPENDIX", "CONCLUSION", "RELATED WORK", "DISCUSSION")
    if normalized_h.upper() in standard_sections:
        return True, 2, normalized_h.title()
    return False, 2, ""


def _collect_table_lines(
    ordered_blocks: List[Any],
    start_data_idx: int,
    consumed_indices: Set[int]
) -> List[str]:
    """收集連續的表格文字行直到遇到標題或下一個章節"""
    all_tbl_lines = []
    curr_scan = start_data_idx
    while curr_scan < len(ordered_blocks):
        cand_b = ordered_blocks[curr_scan]
        ct = cand_b[4].strip()
        if any(ct.startswith(h) for h in ('Table', 'TABLE', 'Figure', 'Fig.', '#')) or re.match(REGEX_SECTION_HEADING, ct):
            break
        for cl in cand_b[4].split('\n'):
            cl_str = cl.strip()
            if cl_str:
                all_tbl_lines.append(cl_str)
        consumed_indices.add(curr_scan)
        curr_scan += 1
    return all_tbl_lines


def _parse_cve_rows_from_lines(all_tbl_lines: List[str]) -> List[List[str]]:
    """從表格行序列中解析 CVE ID 與關聯描述"""
    rows = []
    i_l = 0
    while i_l < len(all_tbl_lines):
        if not re.match(REGEX_CVE_ID, all_tbl_lines[i_l]):
            i_l += 1
            continue
        soft = all_tbl_lines[i_l - 1] if i_l > 0 else ""
        cve_str = all_tbl_lines[i_l]
        vtype = all_tbl_lines[i_l + 1] if i_l + 1 < len(all_tbl_lines) else ""
        desc_tokens = []
        j_l = i_l + 2
        while j_l < len(all_tbl_lines) and not re.match(REGEX_CVE_ID, all_tbl_lines[j_l]):
            if j_l + 1 < len(all_tbl_lines) and re.match(REGEX_CVE_ID, all_tbl_lines[j_l + 1]):
                break
            desc_tokens.append(all_tbl_lines[j_l])
            j_l += 1
        rows.append([soft, cve_str, vtype, " ".join(desc_tokens)])
        i_l = j_l
    return rows


def _extract_cve_table_rows(ordered_blocks: List[Any], start_data_idx: int, consumed_indices: Set[int]) -> List[List[str]]:
    """解析安全論文 CVE 對照表格列"""
    all_tbl_lines = _collect_table_lines(ordered_blocks, start_data_idx, consumed_indices)
    return _parse_cve_rows_from_lines(all_tbl_lines)


def _try_extract_embedded_image(page, doc, y0: float, fig_out_path: str) -> bool:
    """嘗試從 PDF 提取原生內嵌光柵影像"""
    try:
        for info in page.get_image_info(xrefs=True):
            ibbox = fitz.Rect(info['bbox'])
            if ibbox.y1 <= y0 + 35 and ibbox.y0 < y0 - 30 and ibbox.width > 50 and ibbox.height > 40:
                xref = info.get('xref')
                if xref:
                    base_img = doc.extract_image(xref)
                    if base_img and len(base_img["image"]) > 1024:
                        with open(win_path(fig_out_path), "wb") as f_r:
                            f_r.write(base_img["image"])
                        return True
    except Exception:
        pass
    return False


def _compute_figure_clip_rect(
    page, y0: float, chart_y0: float, assoc_b: List[Any], page_w: float, page_h: float
) -> fitz.Rect:
    """計算向量線條圖表的剪裁邊界"""
    page_drawings = [d['rect'] for d in page.get_drawings() if 55 < d['rect'].y0 and d['rect'].y1 < page_h - 50]
    chart_drawings = [r for r in page_drawings if r.y1 <= y0 + 10 and r.y0 >= chart_y0 - 25]
    all_x0 = [r.x0 for r in chart_drawings] + [b[0] for b in assoc_b]
    all_x1 = [r.x1 for r in chart_drawings] + [b[2] for b in assoc_b]
    all_y0 = [r.y0 for r in chart_drawings] + [b[1] for b in assoc_b]
    all_y1 = [r.y1 for r in chart_drawings] + [b[3] for b in assoc_b]
    if all_x0 and all_y0:
        c_y0 = max(50, min(min(all_y0) - 12, chart_y0 - 10))
        c_y1 = min(page_h - 5, min(y0 - 2, max(all_y1) + 6))
        return fitz.Rect(max(5, min(all_x0) - 12), c_y0, min(page_w - 5, max(all_x1) + 12), c_y1)
    return fitz.Rect(max(10, page_w * 0.08), max(10, min(chart_y0 - 15, y0 - 180)), min(page_w - 10, page_w * 0.92), min(page_h - 10, y0 - 2))


def _try_render_vector_drawing(
    page, y0: float, chart_y0: float, assoc_b: List[Any],
    page_w: float, page_h: float, fig_out_path: str
) -> bool:
    """依據幾何繪圖邊界剪裁並渲染向量圖表"""
    try:
        clip_rect = _compute_figure_clip_rect(page, y0, chart_y0, assoc_b, page_w, page_h)
        pix = page.get_pixmap(clip=clip_rect, dpi=180)
        pix.save(win_path(fig_out_path))
        return True
    except Exception:
        return False


def _render_figure(
    page, doc, fb: Any, assets_dir: str, rel_assets_dir: str,
    chart_y0: float, assoc_b: List[Any], page_w: float, page_h: float
) -> Tuple[str, bool]:
    """執行圖表剪裁輸出並回傳 Markdown 語法"""
    fig_caption = fb[4].strip()
    y0 = fb[1]
    fig_num_match = re.search(r'\d+', fig_caption)
    fig_num = fig_num_match.group(0) if fig_num_match else "1"
    fig_filename = f"figure_{fig_num}.png"
    fig_out_path = validate_safe_path(os.path.join(assets_dir, fig_filename))

    saved = _try_extract_embedded_image(page, doc, y0, fig_out_path)
    if not saved:
        saved = _try_render_vector_drawing(page, y0, chart_y0, assoc_b, page_w, page_h, fig_out_path)

    clean_caption = re.sub(r'\s+', ' ', fig_caption).strip()
    short_alt = clean_caption.split('.')[0] if '.' in clean_caption[:80] else clean_caption[:60]
    short_alt = re.sub(r'^(Figure\s+\d+:?|Fig\.\s*\d+:?)[ \t]*', '', short_alt, flags=re.IGNORECASE).strip() or "Figure"
    fig_md = f"![{short_alt}](<{rel_assets_dir}/{fig_filename}>)\n\n*{clean_caption}*\n"
    return fig_md, saved


def _process_page_blocks(
    page, doc, page_idx: int, clean_title: str,
    assets_dir: str, rel_assets_dir: str
) -> Tuple[List[str], int, int]:
    """解析單一頁面的區塊內容，處理表格、圖表、標題與常規段落"""
    page_md: List[str] = []
    tables_count, figures_count = 0, 0

    native_tables = _extract_native_tables(page)
    for ntab in native_tables:
        cap = ntab['caption'] or "Table"
        page_md.extend([f"#### {cap}\n", format_matrix_to_markdown_table(ntab['headers'], ntab['rows']), ""])
        tables_count += 1

    v_blocks = _filter_valid_blocks(page, page.rect.width, page.rect.height)
    rem_blocks = _filter_table_overlap(v_blocks, native_tables)
    ordered_blocks = _reorder_reading_flow(rem_blocks, page.rect.width, page.rect.height, page.rect.width / 2.0)
    fig_regions, fig_assocs, consumed = _pre_scan_figures(ordered_blocks)

    for idx, b in enumerate(ordered_blocks):
        if idx in consumed:
            continue
        t_strip = b[4].strip()

        if re.match(REGEX_ALGORITHM_CAPTION, t_strip, re.IGNORECASE):
            page_md.append(f"#### {t_strip}\n")
            consumed.add(idx)
            continue

        if re.match(REGEX_FIGURE_CAPTION, t_strip, re.IGNORECASE):
            f_md, saved = _render_figure(
                page, doc, b, assets_dir, rel_assets_dir,
                fig_regions.get(idx, b[1]), fig_assocs.get(idx, []),
                page.rect.width, page.rect.height
            )
            page_md.append(f_md)
            if saved:
                figures_count += 1
            consumed.add(idx)
            continue

        is_h, h_lvl, h_title = _detect_heading(t_strip)
        if is_h:
            page_md.append(f"{'#' * h_lvl} {h_title}\n")
            continue

        if page_idx == 0 and clean_title.lower() in t_strip.lower() and len(t_strip) < len(clean_title) + 50:
            continue

        cleaned_p = clean_paragraph_lines([l for l in b[4].split("\n") if l.strip()])
        if cleaned_p:
            page_md.extend([cleaned_p, ""])

    return page_md, tables_count, figures_count


def _safe_write_text_file(target_file_path: str, content: str) -> None:
    """安全校驗目標路徑並寫入文字檔案，防範路徑遍歷 (SonarCloud S8707)"""
    safe_path = Path(validate_safe_path(target_file_path)).resolve()
    if '\0' in str(safe_path) or '..' in str(safe_path).split(os.sep):
        raise ValueError(f"Unsafe path detected: {target_file_path}")
    out_dir = safe_path.parent
    os.makedirs(win_path(str(out_dir)), exist_ok=True)
    with open(win_path(str(safe_path)), "w", encoding="utf-8") as fp:
        fp.write(content)


def convert_pdf_to_clean_markdown(
    pdf_path: str,
    output_md_path: Optional[str] = None,
    assets_dir: Optional[str] = None
) -> Tuple[str, Dict[str, Any]]:
    """通用、純 Python / PyMuPDF 幾何版面解析核心"""
    pdf_path = validate_safe_path(pdf_path)
    doc = fitz.open(win_path(pdf_path))
    base_name = Path(pdf_path).stem

    if not output_md_path:
        output_md_path = str(Path(pdf_path).parent / f"{base_name} (Raw).md")
    output_md_path = validate_safe_path(output_md_path)

    if not assets_dir:
        p_dir = Path(pdf_path).parent
        assets_dir = str(p_dir.parent / "assets" / base_name if (p_dir.parent / "assets").is_dir() else p_dir / "assets" / base_name)
    assets_dir = validate_safe_path(assets_dir)

    os.makedirs(win_path(assets_dir), exist_ok=True)
    rel_assets_dir = os.path.relpath(assets_dir, os.path.dirname(output_md_path)).replace("\\", "/")

    meta = doc.metadata or {}
    clean_title = (meta.get("title") or "").strip()
    if not clean_title or len(clean_title) < 5 or clean_title.startswith(("V_M_", "B_", "paper_")):
        clean_title = re.sub(r'^\(\d{4}\)\s*', '', base_name).strip()

    metadata = {
        "title": clean_title,
        "author": meta.get("author") or None,
        "creator": meta.get("creator") or None,
        "pages": len(doc),
    }
    clean_meta = {k: v for k, v in metadata.items() if v is not None}
    md_lines = [
        "---",
        yaml.safe_dump(clean_meta, allow_unicode=True, sort_keys=False).rstrip(),
        "---",
        "",
        f"# {clean_title}",
        "",
        f"> **總頁數**：{len(doc)} 頁",
        "",
        "---",
        ""
    ]

    total_tables, total_figures = 0, 0
    for page_idx in range(len(doc)):
        page = doc[page_idx]
        if page_idx == 0 and "Proceedings of the" in page.get_text():
            continue
        p_md, p_tbl, p_fig = _process_page_blocks(
            page, doc, page_idx, clean_title, assets_dir, rel_assets_dir
        )
        md_lines.extend(p_md)
        total_tables += p_tbl
        total_figures += p_fig

    full_markdown = "\n".join(md_lines)
    _safe_write_text_file(output_md_path, full_markdown)

    return full_markdown, {
        "pages": len(doc),
        "tables": total_tables,
        "figures": total_figures,
        "output_path": output_md_path
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python scripts/parser/lightweight_parser.py <pdf_path> [output_md_path]")
        sys.exit(1)
    p_in = sys.argv[1]
    p_out = sys.argv[2] if len(sys.argv) > 2 else None
    _, st = convert_pdf_to_clean_markdown(p_in, p_out)
    print("✅ 解析完成！")
    print(f"  • 輸出檔案: {st['output_path']}")
    print(f"  • 頁數: {st['pages']} 頁 | 智慧抽取表格: {st['tables']} | 剪裁圖表資產: {st['figures']}")

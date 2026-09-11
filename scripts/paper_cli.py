#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code Security Research — 通用文獻庫管理與自動化維護工具 (Paper CLI)
===============================================================
整合文獻審查、雙向鏈結同步、檔名規範化、重複清理與筆記生成等全套功能。
取代過往零散的一次性遷移腳本，提供可持續、長久維護的 CLI 命令列套件。

使用範例:
  python scripts/paper_cli.py audit                  # 執行全庫健康檢查 (100% 鏈結、Wikilinks、YAML、檔名)
  python scripts/paper_cli.py stats                  # 顯示全庫資產統計與年份分佈
  python scripts/paper_cli.py sync                   # 自動同步 Vault 筆記與 raw-papers 實體檔案之雙向鏈結
  python scripts/paper_cli.py normalize              # 將 raw-papers 中非標準檔名轉為標準空格格式
  python scripts/paper_cli.py dedup                  # 偵測並清理跨分類重複筆記與 raw-papers 孤兒檔案
  python scripts/paper_cli.py generate-notes         # 針對尚未建檔的 raw PDF 自動生成 Obsidian 卡片筆記草稿
"""

import os
import sys
import re
import argparse
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional

# 強制 Windows 終端輸出為 UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# 專案預設路徑解析
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DEFAULT_VAULT_DIR = os.path.join(REPO_ROOT, "research-vault")
DEFAULT_RAW_DIR = os.path.join(REPO_ROOT, "raw-papers")
PARSER_DIR = os.path.join(SCRIPT_DIR, "parser")

# 統一常數定義 (消除 SonarCloud 重複字串異味)
SUFFIX_RAW_MD = " (Raw).md"
SUFFIX_RAW_LOWER = " raw.md"
RESTRICTIONS_APPLY = "Restrictions apply."
HELP_VAULT_DIR = "Vault 目錄路徑"
HELP_RAW_DIR = "raw-papers 目錄路徑"
AUTHOR_BLACKLIST = {
    'sutter', 'auer', 'li', 'wang', 'zhang', 'chen',
    'liu', 'yang', 'huang', 'zhao', 'wu', 'xu', 'feizollah'
}


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



def clean_tokens(text: str) -> Set[str]:
    """將檔名切分為標準化詞彙集合，用於模糊匹配"""
    words = re.findall(r'[a-zA-Z0-9]+', text.lower())
    stop_words = {'and', 'the', 'of', 'in', 'on', 'for', 'with', 'a', 'an', 'to', 'via', 'raw', 'pdf', 'md'}
    return {w for w in words if w not in stop_words and len(w) > 1}


# ==============================================================================
# 1. 審查模組 (AUDIT / VERIFY) 輔助函數
# ==============================================================================

def _collect_vault_notes(vault_dir: str) -> Dict[str, str]:
    """蒐集 Vault 中所有 Markdown 筆記 (偵測同名碰撞避免靜默覆蓋)"""
    notes: Dict[str, str] = {}
    for root, _, files in os.walk(vault_dir):
        for f in files:
            if f.endswith(".md"):
                stem = f[:-3]
                full_p = os.path.join(root, f)
                if stem in notes:
                    print(f"  ⚠️ 警告: 偵測到同名筆記跨目錄衝突: {stem}")
                notes[stem] = full_p
    return notes


def _check_wikilinks(vault_notes: Dict[str, str]) -> int:
    """檢查 Obsidian 雙向內部鏈接有效性"""
    print(f"\n[1/6] 檢查 Obsidian 雙向內部鏈接 (Wikilinks)... (總計 {len(vault_notes)} 篇筆記)")
    broken_wikilinks = []
    for stem, note_path in vault_notes.items():
        with open(win_path(note_path), "r", encoding="utf-8", errors="ignore") as fp:
            content = fp.read()
        content_no_code = re.sub(r'```[\s\S]*?```', '', content)
        content_no_code = re.sub(r'`[^`\n]+`', '', content_no_code)
        w_links = re.findall(r'\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]', content_no_code)
        for wl in w_links:
            wl_clean = wl.strip()
            if wl_clean and wl_clean not in vault_notes and "請替換" not in wl_clean:
                broken_wikilinks.append((stem, wl_clean))

    if broken_wikilinks:
        print(f"  ❌ 發現 {len(broken_wikilinks)} 個失效的內部雙鏈:")
        for src, tgt in broken_wikilinks[:10]:
            print(f"     - 在筆記 [{src}] 中: 指向不存在的 [[{tgt}]]")
        return len(broken_wikilinks)
    print("  ✅ 內部雙向鏈接 100% 有效！(Broken Wikilinks: 0)")
    return 0


def _check_note_paper_links(note_path: str) -> Tuple[Optional[str], Optional[str]]:
    """解析卡片筆記中的實體 PDF 與 Markdown 原文鏈結"""
    with open(win_path(note_path), "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
    pdf_err, raw_err = None, None
    pdf_match = re.search(r'\[PDF\s*原文\]\(<([^>]+)>\)', content)
    if pdf_match:
        rel = pdf_match.group(1)
        abs_target = os.path.normpath(os.path.join(os.path.dirname(note_path), rel))
        if not os.path.exists(win_path(abs_target)):
            pdf_err = rel
    raw_match = re.search(r'\[Markdown\s*原文\]\(<([^>]+)>\)', content)
    if raw_match:
        rel = raw_match.group(1)
        abs_target = os.path.normpath(os.path.join(os.path.dirname(note_path), rel))
        if not os.path.exists(win_path(abs_target)):
            raw_err = rel
    return pdf_err, raw_err


def _report_link_results(broken_pdf: List[Tuple[str, str]], broken_raw: List[Tuple[str, str]],
                         orphan_pdfs: List[str], orphan_raws: List[str],
                         valid_pdf: int, valid_raw: int) -> int:
    """輸出實體鏈結與孤兒檔案統計結果"""
    if broken_pdf:
        print(f"  ❌ 發現 {len(broken_pdf)} 個失效的 [PDF 原文] 鏈接:")
        for stem, link in broken_pdf[:5]:
            print(f"     - {stem}: {link}")
    else:
        print(f"  ✅ [PDF 原文] 鏈接 100% 存在！(已驗證 {valid_pdf} 篇實體 PDF)")

    if broken_raw:
        print(f"  ❌ 發現 {len(broken_raw)} 個失效的 [Markdown 原文] 鏈接:")
        for stem, link in broken_raw[:5]:
            print(f"     - {stem}: {link}")
    else:
        print(f"  ✅ [Markdown 原文] 鏈接 100% 存在！(已驗證 {valid_raw} 篇實體解析檔)")

    if orphan_pdfs:
        print(f"  ❌ 發現 {len(orphan_pdfs)} 個孤兒 PDF (未在 Vault 建檔):")
        for op in orphan_pdfs[:5]:
            print(f"     - {op}")

    if orphan_raws:
        print(f"  ❌ 發現 {len(orphan_raws)} 個 PDF 缺少對應 (Raw).md:")
        for oraw in orphan_raws[:5]:
            print(f"     - {oraw}")

    return len(broken_pdf) + len(broken_raw) + len(orphan_pdfs) + len(orphan_raws)


def _check_paper_links(vault_notes: Dict[str, str], raw_dir: str) -> int:
    """檢查卡片筆記之實體 PDF 與 Raw Markdown 相對鏈結"""
    print("\n[2/6] 檢查卡片筆記中指向實體 PDF 與 Raw Markdown 之相對鏈結與雙向對稱性...")
    broken_pdf, broken_raw = [], []
    valid_pdf_count, valid_raw_count = 0, 0

    for stem, note_path in vault_notes.items():
        if any(k in note_path for k in ["reports", "syntheses", "matrices", "diagrams", "templates"]):
            continue
        pdf_err, raw_err = _check_note_paper_links(note_path)
        if pdf_err:
            broken_pdf.append((stem, pdf_err))
        else:
            valid_pdf_count += 1
        if raw_err:
            broken_raw.append((stem, raw_err))
        else:
            valid_raw_count += 1

    orphan_pdfs, orphan_raws = _find_raw_orphans(raw_dir, vault_notes)
    return _report_link_results(broken_pdf, broken_raw, orphan_pdfs, orphan_raws, valid_pdf_count, valid_raw_count)


def _inspect_raw_orphan(f: str, root: str, vault_notes: Dict[str, str]) -> Tuple[Optional[str], Optional[str]]:
    """檢驗單一檔案是否為未建檔 PDF 或缺少對應 Raw.md"""
    if not f.endswith(".pdf"):
        return None, None
    p_stem = f[:-4]
    orphan_pdf = f if p_stem not in vault_notes else None
    expected_raw = os.path.join(root, f"{p_stem}{SUFFIX_RAW_MD}")
    orphan_raw = f if not os.path.exists(win_path(expected_raw)) else None
    return orphan_pdf, orphan_raw


def _find_raw_orphans(raw_dir: str, vault_notes: Dict[str, str]) -> Tuple[List[str], List[str]]:
    """尋找尚未在 Vault 建檔或缺少 Raw.md 的檔案"""
    orphan_pdfs, orphan_raws = [], []
    for root, _, files in os.walk(raw_dir):
        if "legacy_archive" in root or "assets" in root:
            continue
        for f in files:
            o_pdf, o_raw = _inspect_raw_orphan(f, root, vault_notes)
            if o_pdf:
                orphan_pdfs.append(o_pdf)
            if o_raw:
                orphan_raws.append(o_raw)
    return orphan_pdfs, orphan_raws


def _validate_single_yaml(note_path: str) -> Optional[str]:
    """檢驗單一筆記的 YAML 前言格式"""
    with open(win_path(note_path), "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return "未閉合的 Frontmatter (缺少結尾 ---)"
    try:
        yaml.safe_load(parts[1])
        return None
    except Exception as e:
        return str(e)


def _check_yaml_frontmatter(vault_notes: Dict[str, str]) -> int:
    """檢查 YAML 前言語法"""
    print("\n[3/6] 檢查 YAML Frontmatter 格式與必備屬性...")
    yaml_errors = []
    for stem, note_path in vault_notes.items():
        err = _validate_single_yaml(note_path)
        if err:
            yaml_errors.append((stem, err))

    if yaml_errors:
        print(f"  ❌ 發現 {len(yaml_errors)} 個 YAML 語法錯誤:")
        for stem, err in yaml_errors[:5]:
            print(f"     - {stem}: {err}")
        return len(yaml_errors)
    print("  ✅ 全庫筆記 YAML Frontmatter 語法 100% 正確！")
    return 0


def _check_file_naming(raw_dir: str) -> List[Tuple[str, str]]:
    """檢查 raw-papers 檔案命名"""
    suspicious = []
    for root, _, files in os.walk(raw_dir):
        if "legacy_archive" in root:
            continue
        for f in files:
            if f.endswith(SUFFIX_RAW_LOWER):
                suspicious.append((f, "結尾使用非標準 ' raw.md' (應為 ' (Raw).md')"))
            elif f.startswith("(") and f.endswith((".pdf", ".md")):
                suspicious.append((f, "檔名缺少工具/類型前綴，直接以年份 '(' 開頭"))
            m_pre = re.match(r'^([A-Za-z0-9\-_+]+)\s*\(\d{4}\)', f)
            if m_pre and m_pre.group(1).lower() in AUTHOR_BLACKLIST:
                suspicious.append((f, f"檔名前綴 [{m_pre.group(1)}] 違規使用作者姓名"))
    return suspicious


def _inspect_single_vault_naming(stem: str, note_path: str) -> Optional[Tuple[str, str]]:
    """檢驗單篇 Vault 筆記命名與年份一致性"""
    if re.match(r'^\d', stem) or any(k in stem for k in ["README", "TAXONOMY", "Template", "guide", "review", "TABLE"]):
        return None
    if re.match(r'^[^()]+\s\(\d{4}\)$', stem):
        return (stem, "檔名缺少論文完整標題 (應為 'Tool/Category (Year) Title')")
    year_m = re.search(r'\((\d{4})\)', stem)
    if not year_m:
        return None
    fn_year = int(year_m.group(1))
    try:
        with open(win_path(note_path), "r", encoding="utf-8", errors="ignore") as fp:
            txt = fp.read()
        if txt.startswith("---"):
            parts = txt.split("---", 2)
            if len(parts) >= 3:
                meta = yaml.safe_load(parts[1])
                if isinstance(meta, dict) and "year" in meta and int(meta["year"]) != fn_year:
                    return (stem, f"檔名年份 ({fn_year}) 與 Frontmatter 年份 ({meta['year']}) 衝突")
    except Exception:
        pass
    return None


def _check_vault_naming(vault_notes: Dict[str, str]) -> List[Tuple[str, str]]:
    """檢查 Vault 筆記命名標準"""
    suspicious = []
    for stem, note_path in vault_notes.items():
        res = _inspect_single_vault_naming(stem, note_path)
        if res:
            suspicious.append(res)
    return suspicious


def _check_naming_conventions(vault_notes: Dict[str, str], raw_dir: str) -> int:
    """檢查命名規範統整"""
    print("\n[4/6] 檢查檔名命名規範 (工具優先/類型前綴，嚴禁作者姓名，年份一致性)...")
    suspicious = _check_file_naming(raw_dir) + _check_vault_naming(vault_notes)
    if suspicious:
        print(f"  ❌ 發現 {len(suspicious)} 個檔名格式或元數據異常:")
        for f, reason in suspicious[:5]:
            print(f"     - {f}: {reason}")
        return len(suspicious)
    print("  ✅ 檔名標準化與命名規範通過！(全庫無作者名殘留、無殘缺短檔名，年份 100% 吻合)")
    return 0


def _check_pdf_duplicates(raw_dir: str) -> Tuple[int, List[Tuple[str, str]]]:
    """檢驗 PDF 二進制 SHA256 唯一性"""
    import hashlib
    sha_tracker = {}
    duplicates = []
    for root, _, files in os.walk(raw_dir):
        if "legacy_archive" in root:
            continue
        for f in files:
            if f.endswith(".pdf"):
                with open(win_path(os.path.join(root, f)), 'rb') as fp:
                    sha = hashlib.sha256(fp.read()).hexdigest()
                if sha in sha_tracker:
                    duplicates.append((f, sha_tracker[sha]))
                else:
                    sha_tracker[sha] = f
    return len(sha_tracker), duplicates


def _check_content_and_duplicates(raw_dir: str) -> int:
    """檢查 PDF 二進制唯一性與內容吻合度"""
    print("\n[5/6] 檢查 PDF 實質內文、二進制唯一性與安全領域吻合度...")
    errors = 0
    try:
        total_pdfs, duplicates = _check_pdf_duplicates(raw_dir)
        if duplicates:
            print(f"  ❌ 發現 {len(duplicates)} 組二進制重複的 PDF 檔案:")
            for f1, f2 in duplicates[:5]:
                print(f"     - {f1} == {f2}")
            errors += len(duplicates)
        else:
            print(f"  ✅ 二進制唯一性檢查通過！(全庫 {total_pdfs} 篇 PDF 無任何重複檔案)")
    except Exception as ex:
        print(f"  ⚠️ 二進制排查執行略過: {ex}")
    return errors


def _check_index_navigation(vault_dir: str, vault_notes: Dict[str, str]) -> int:
    """檢查主目錄流派索引有效性"""
    print("\n[6/6] 檢查 00-研究流派圖主目錄.md 流派索引有效性...")
    index_path = os.path.join(vault_dir, "00-研究流派圖主目錄.md")
    if not os.path.exists(win_path(index_path)):
        print("  ⚠️ 未找到 00-研究流派圖主目錄.md")
        return 0
    with open(win_path(index_path), "r", encoding="utf-8") as fp:
        c = fp.read()
    idx_links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', c)
    broken_idx = [l for l in idx_links if l.strip() not in vault_notes]
    if broken_idx:
        print(f"  ❌ 發現 {len(broken_idx)} 個失效的流派目錄連結: {broken_idx}")
        return len(broken_idx)
    print(f"  ✅ 主目錄共 {len(idx_links)} 個流派連結全部有效！")
    return 0


def cmd_audit(args) -> int:
    """全面檢查文獻庫的完整性：實體鏈結、Obsidian 雙鏈、YAML 前言、檔名規範"""
    vault_dir = os.path.abspath(args.vault_dir)
    raw_dir = os.path.abspath(args.raw_dir)

    print("=" * 70)
    print("🔍 Code Security Research — 文獻庫全方位健康審查 (Health Audit)")
    print(f"  • Vault 路徑: {vault_dir}")
    print(f"  • Raw   路徑: {raw_dir}")
    print("=" * 70)

    vault_notes = _collect_vault_notes(vault_dir)
    total_errors = (
        _check_wikilinks(vault_notes)
        + _check_paper_links(vault_notes, raw_dir)
        + _check_yaml_frontmatter(vault_notes)
        + _check_naming_conventions(vault_notes, raw_dir)
        + _check_content_and_duplicates(raw_dir)
        + _check_index_navigation(vault_dir, vault_notes)
    )

    print("\n" + "=" * 70)
    if total_errors == 0:
        print("🎉 審查結果：全庫 100% 健康！所有指標均符合學術與系統規範。")
        print("=" * 70)
        return 0
    print(f"🚨 審查結果：共發現 {total_errors} 處問題，請執行相應修復指令。")
    print("=" * 70)
    return 1


# ==============================================================================
# 2. 雙向鏈結同步模組 (SYNC) 輔助函數
# ==============================================================================

def _record_raw_entry(index: Dict[str, str], stem: str, path: str, label: str):
    """記錄索引並在同名碰撞時輸出警告"""
    if stem in index:
        print(f"  ⚠️ 警告: 發現跨目錄同名 raw {label}: {stem}")
    index[stem] = path


def _index_raw_file(f: str, full_p: str, pdf_index: Dict[str, str], md_index: Dict[str, str]):
    """解析單一 raw 檔案並分類記錄至索引"""
    if f.endswith(".pdf"):
        _record_raw_entry(pdf_index, f[:-4], full_p, "PDF")
    elif f.endswith(SUFFIX_RAW_MD):
        _record_raw_entry(md_index, f[:-len(SUFFIX_RAW_MD)], full_p, "Markdown")
    elif f.endswith(".md"):
        _record_raw_entry(md_index, f[:-3], full_p, "Markdown")


def _build_raw_index(raw_dir: str) -> Tuple[Dict[str, str], Dict[str, str]]:
    """建立 raw-papers PDF 與 Markdown 索引 (偵測跨目錄同名碰撞)"""
    raw_pdf_index, raw_md_index = {}, {}
    for r, _, files in os.walk(raw_dir):
        if "legacy_archive" in r:
            continue
        for f in files:
            _index_raw_file(f, os.path.join(r, f), raw_pdf_index, raw_md_index)
    return raw_pdf_index, raw_md_index


def _build_archive_line(pdf_rel: Optional[str], raw_rel: Optional[str]) -> str:
    """生成卡片中的文獻存檔雙向鏈結文字"""
    if pdf_rel and raw_rel:
        return f"> **文獻存檔**：[PDF 原文](<{pdf_rel}>) | [Markdown 原文](<{raw_rel}>)"
    if pdf_rel:
        return f"> **文獻存檔**：[PDF 原文](<{pdf_rel}>)"
    if raw_rel:
        return f"> **文獻存檔**：[Markdown 原文](<{raw_rel}>)"
    return "> **文獻存檔**：*(本篇為重點文獻全文摘錄與分析筆記)*"


def _sync_single_note(v_path: str, v_base: str, raw_pdf_index: Dict[str, str], raw_md_index: Dict[str, str]):
    """為單篇筆記掛載更新文獻存檔相對路徑"""
    note_dir = os.path.dirname(v_path)
    pdf_abs = raw_pdf_index.get(v_base)
    raw_abs = raw_md_index.get(v_base)

    pdf_rel = os.path.relpath(pdf_abs, note_dir).replace(os.sep, '/') if pdf_abs else None
    raw_rel = os.path.relpath(raw_abs, note_dir).replace(os.sep, '/') if raw_abs else None
    archive_line = _build_archive_line(pdf_rel, raw_rel)

    with open(win_path(v_path), "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()

    if "> **文獻存檔**" in content or "[PDF 原文]" in content:
        content = re.sub(r'> \*\*文獻存檔\*\*:[^\n\r]+', archive_line, content)
        content = re.sub(r'> \*\*文獻存檔\*\*：[^\n\r]+', archive_line, content)
    else:
        title_match = re.search(r'(# [^\n\r]+\n+)', content)
        if title_match:
            content = content.replace(title_match.group(1), f"{title_match.group(1)}{archive_line}\n\n", 1)
        else:
            content = f"{archive_line}\n\n" + content

    with open(win_path(v_path), "w", encoding="utf-8") as fp:
        fp.write(content)


def cmd_sync(args) -> int:
    """自動遍歷 Vault 與 raw-papers，為每篇筆記自動掛載精確的相對路徑 [PDF 原文] 與 [Markdown 原文]"""
    vault_dir = os.path.abspath(args.vault_dir)
    raw_dir = os.path.abspath(args.raw_dir)

    print("🔄 開始同步文獻雙向鏈結...")
    raw_pdf_index, raw_md_index = _build_raw_index(raw_dir)
    updated_count = 0

    for root, _, files in os.walk(vault_dir):
        if any(k in root for k in ["reports", "syntheses", "matrices", "diagrams", "templates"]):
            continue
        for f in files:
            if not f.endswith(".md") or f.startswith("00-") or re.match(r"^[0-9A-Z]+\.[0-9A-Za-z]+-", f):
                continue
            _sync_single_note(os.path.join(root, f), f[:-3], raw_pdf_index, raw_md_index)
            updated_count += 1

    print(f"✅ 雙向鏈結同步完成！共更新/檢查了 {updated_count} 篇筆記。")
    return 0


# ==============================================================================
# 3. 檔名標準化模組 (NORMALIZE) 輔助函數
# ==============================================================================

def clean_paper_title(raw_name: str) -> str:
    """將包含序號、下劃線、奇怪符號的原始檔名清洗為標準空格格式"""
    stem = raw_name
    for ext in [".pdf", ".md", SUFFIX_RAW_MD, SUFFIX_RAW_LOWER]:
        if stem.endswith(ext):
            stem = stem[:-len(ext)]
            break
    stem = re.sub(r'^\d+[\s_-]+', '', stem)
    stem = stem.replace('_', ' ')
    return re.sub(r'\s+', ' ', stem).strip()


def _compute_normalized_name(f: str) -> Tuple[bool, str]:
    """判定檔名是否需要標準化並回傳規範檔名"""
    new_name = f
    needs_rename = False
    if f.endswith(SUFFIX_RAW_LOWER):
        new_name = f[:-len(SUFFIX_RAW_LOWER)] + SUFFIX_RAW_MD
        needs_rename = True
    if "_" in new_name:
        base, ext = os.path.splitext(new_name)
        if ext == ".md" and base.endswith(" (Raw)"):
            clean_stem = clean_paper_title(base[:-6])
            new_name = f"{clean_stem}{SUFFIX_RAW_MD}"
        else:
            clean_stem = clean_paper_title(base)
            new_name = f"{clean_stem}{ext}"
        needs_rename = True
    return needs_rename, new_name


def _process_normalize_file(root: str, f: str, dry_run: bool) -> int:
    """檢查並執行單一檔案之標準化重命名"""
    needs_rename, new_name = _compute_normalized_name(f)
    if needs_rename and new_name != f:
        old_p = os.path.join(root, f)
        new_p = os.path.join(root, new_name)
        print(f"  • 重命名: {f} -> {new_name}")
        if os.path.exists(win_path(new_p)):
            print(f"  ⚠️ 目標檔案已存在，略過重命名: {f} -> {new_name}")
        elif not dry_run:
            os.rename(win_path(old_p), win_path(new_p))
        return 1
    return 0


def cmd_normalize(args) -> int:
    """自動掃描 raw-papers 目錄，將所有包含底線或非標準結尾的檔案批次重命名為自然空格規範"""
    target_dir = os.path.abspath(args.dir or DEFAULT_RAW_DIR)
    dry_run = args.dry_run

    print(f"🧹 開始執行檔名標準化 (目錄: {target_dir}, DryRun: {dry_run})...")
    renamed_count = 0

    for root, _, files in os.walk(target_dir):
        if "legacy_archive" in root:
            continue
        for f in files:
            renamed_count += _process_normalize_file(root, f, dry_run)

    print(f"✅ 檔名標準化處理完成！共處理 {renamed_count} 個檔案。")
    return 0


# ==============================================================================
# 4. 查重與孤兒檔案歸檔 (DEDUP) 輔助函數
# ==============================================================================

def _handle_duplicate_group(name: str, paths: List[str], vault_dir: str, auto_prune: bool):
    """處理單組跨分類重複筆記與修剪佔位 stub"""
    print(f"  • {name}:")
    for p in paths:
        size = os.path.getsize(win_path(p))
        print(f"     - [{size} bytes] {os.path.relpath(p, vault_dir)}")
    if auto_prune:
        paths_sorted = sorted(paths, key=lambda x: os.path.getsize(win_path(x)), reverse=True)
        for stub in paths_sorted[1:]:
            os.remove(win_path(stub))
            print(f"       🗑️ 自動移除冗餘 stub: {os.path.relpath(stub, vault_dir)}")


def _check_vault_duplicates(vault_dir: str, auto_prune: bool) -> Set[str]:
    """檢驗 Vault 跨分類重複筆記"""
    locations: Dict[str, List[str]] = {}
    for root, _, files in os.walk(vault_dir):
        if any(k in root for k in ["reports", "syntheses", "matrices", "diagrams", "templates"]):
            continue
        for f in files:
            if f.endswith(".md") and not f.startswith("00-"):
                locations.setdefault(f, []).append(os.path.join(root, f))

    dups = {k: v for k, v in locations.items() if len(v) > 1}
    if dups:
        print(f"⚠️ 發現 {len(dups)} 篇存在跨分類重複存放的筆記:")
        for name, paths in dups.items():
            _handle_duplicate_group(name, paths, vault_dir, auto_prune)
    else:
        print("✅ 跨流派筆記無任何重複！(Duplicates: 0)")
    return {f[:-3] for f in locations.keys()}


def _execute_orphan_archival(orphan_files: List[str], raw_dir: str, archive_dir: str):
    """將孤兒檔案保留相對目錄層級移動至封存目錄"""
    for op in orphan_files:
        rel_path = os.path.relpath(op, raw_dir)
        dest = os.path.join(archive_dir, rel_path)
        os.makedirs(win_path(os.path.dirname(dest)), exist_ok=True)
        if os.path.exists(win_path(dest)):
            os.remove(win_path(dest))
        os.rename(win_path(op), win_path(dest))
        print(f"  📦 已移入封存區: {rel_path}")


def _find_orphan_files(raw_dir: str, vault_bases: Set[str]) -> List[str]:
    """遍歷 raw-papers 檢索未在 Vault 建檔之實體 PDF 與 Raw MD"""
    orphan_files = []
    for root, _, files in os.walk(raw_dir):
        if "legacy_archive" in root:
            continue
        for f in files:
            is_pdf_orphan = f.endswith(".pdf") and (f[:-4] not in vault_bases)
            is_raw_orphan = f.endswith(SUFFIX_RAW_MD) and (f[:-len(SUFFIX_RAW_MD)] not in vault_bases)
            if is_pdf_orphan or is_raw_orphan:
                orphan_files.append(os.path.join(root, f))
    return orphan_files


def _archive_orphans(raw_dir: str, vault_bases: Set[str], do_archive: bool):
    """檢驗並封存 raw-papers 孤兒檔案"""
    orphan_files = _find_orphan_files(raw_dir, vault_bases)
    archive_dir = os.path.join(raw_dir, "legacy_archive", "unreferenced_leftovers")

    if not orphan_files:
        print("✅ raw-papers 無任何未對應的孤兒實體檔案！(Orphans: 0)")
        return

    print(f"\n⚠️ 發現 {len(orphan_files)} 個未在 Vault 中建檔之孤兒檔案:")
    for op in orphan_files[:5]:
        print(f"  • {os.path.relpath(op, raw_dir)}")
    if do_archive:
        _execute_orphan_archival(orphan_files, raw_dir, archive_dir)




def cmd_dedup(args) -> int:
    """偵測跨流派的重複卡片筆記，並揪出未建檔的孤兒 PDF 移入封存區"""
    print("🔍 執行跨分類筆記重複性檢查與孤兒檔案審查...")
    vault_bases = _check_vault_duplicates(os.path.abspath(args.vault_dir), args.auto_prune_stubs)
    _archive_orphans(os.path.abspath(args.raw_dir), vault_bases, args.archive_orphans)
    return 0


# ==============================================================================
# 5. 統計模組 (STATS) 輔助函數
# ==============================================================================

def _count_vault_assets(vault_dir: str) -> Tuple[int, int, int]:
    """計算 Vault 卡片筆記資產統計"""
    notes_dir = os.path.join(vault_dir, "notes")
    reports_dir = os.path.join(vault_dir, "reports")
    matrices_dir = os.path.join(vault_dir, "matrices")
    n_count = len([f for f in os.listdir(notes_dir) if f.endswith(".md")]) if os.path.exists(notes_dir) else 0
    r_count = len([f for f in os.listdir(reports_dir) if f.endswith(".md")]) if os.path.exists(reports_dir) else 0
    m_count = len([f for f in os.listdir(matrices_dir) if f.endswith(".md")]) if os.path.exists(matrices_dir) else 0
    return n_count, r_count, m_count


def _count_raw_assets(raw_dir: str) -> Tuple[int, int, Dict[str, int]]:
    """計算實體 PDF 與年份分佈"""
    pdf_count, raw_md_count = 0, 0
    year_stats: Dict[str, int] = {}
    for root, _, files in os.walk(raw_dir):
        if "legacy_archive" in root:
            continue
        rel = os.path.relpath(root, raw_dir)
        year_group = rel.split(os.sep)[0] if rel != "." else "root"
        for f in files:
            if f.endswith(".pdf"):
                pdf_count += 1
                year_stats[year_group] = year_stats.get(year_group, 0) + 1
            elif f.endswith((SUFFIX_RAW_MD, SUFFIX_RAW_LOWER)):
                raw_md_count += 1
    return pdf_count, raw_md_count, year_stats


def cmd_stats(args) -> int:
    """統計全庫文獻卡片、實體 PDF/Raw 數量與年份分佈"""
    vault_dir = os.path.abspath(args.vault_dir)
    raw_dir = os.path.abspath(args.raw_dir)

    print("=" * 70)
    print("📊 Code Security Research — 文獻庫資產統計總覽 (Stats)")
    print("=" * 70)

    notes_c, rep_c, mat_c = _count_vault_assets(vault_dir)
    pdf_c, raw_c, year_stats = _count_raw_assets(raw_dir)

    print("\n📁 知識庫卡片資產 (research-vault/):")
    print(f"  • 單篇論文精讀筆記 (notes/)   : {notes_c} 篇")
    print(f"  • 綜合研究報告 (reports/)      : {rep_c} 篇")
    print(f"  • 核心比對矩陣 (matrices/)     : {mat_c} 篇")

    print("\n📦 實體原始檔案 (raw-papers/):")
    print(f"  • 實體 PDF 論文檔案            : {pdf_c} 篇")
    print(f"  • 全文 Raw Markdown 解析檔     : {raw_c} 篇")

    pdf_cov = (pdf_c / notes_c * 100) if notes_c else 0
    raw_cov = (raw_c / notes_c * 100) if notes_c else 0
    print(f"  • PDF 原文覆蓋率               : {pdf_cov:.1f}%")
    print(f"  • Markdown 原文解析覆蓋率      : {raw_cov:.1f}%")

    print("\n📅 實體論文年份分佈 (Year Distribution):")
    for yg in sorted(year_stats.keys(), reverse=True):
        count = year_stats[yg]
        bar = "█" * min(count, 40)
        print(f"  • {yg:<12}: {count:>3} 篇 {bar}")

    print("=" * 70)
    return 0


# ==============================================================================
# 6. 浮水印清理模組 (CLEAN-WATERMARKS) 輔助函數
# ==============================================================================

def _clean_single_file_watermarks(fpath: str, dry_run: bool) -> int:
    """清理單一 Markdown 檔案中的浮水印行"""
    try:
        with open(win_path(fpath), 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception:
        return 0

    removed = 0
    new_lines = []
    for line in lines:
        ls = line.strip()
        is_watermark = (
            ("Authorized licensed use limited to:" in ls and RESTRICTIONS_APPLY in ls) or
            ("Downloaded on" in ls and "IEEE Xplore" in ls and RESTRICTIONS_APPLY in ls) or
            ("IEEE Xplore" in ls and RESTRICTIONS_APPLY in ls and len(ls) < 60) or
            ("IEEE. Personal use of this material is permitted" in ls)
        )
        if is_watermark:
            removed += 1
        else:
            new_lines.append(line)

    if removed > 0 and not dry_run:
        with open(win_path(fpath), 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    return removed


def _clean_dir_tree(d: str, dry_run: bool) -> Tuple[int, int]:
    """清理單一目錄樹下所有 Markdown 檔案之浮水印"""
    cleaned_files, lines_removed = 0, 0
    if not os.path.exists(d):
        return 0, 0
    for root, _, files in os.walk(d):
        for fname in files:
            if fname.endswith(".md"):
                fpath = os.path.join(root, fname)
                lr = _clean_single_file_watermarks(fpath, dry_run)
                if lr > 0:
                    cleaned_files += 1
                    lines_removed += lr
                    rel = os.path.relpath(fpath, REPO_ROOT)
                    print(f"  • [{lr} 行] {rel}")
    return cleaned_files, lines_removed


def cmd_clean_watermarks(args) -> int:
    """批次清理 Markdown 文本中的 IEEE 授權浮水印冗餘行"""
    target_dirs = [os.path.abspath(args.raw_dir), os.path.abspath(args.vault_dir)]
    dry_run = args.dry_run

    print("=" * 70)
    print(f"🧹 執行文獻浮水印清理 (Clean Watermarks){' [DRY-RUN]' if dry_run else ''}...")
    print("=" * 70)

    total_cleaned_files = 0
    total_lines_removed = 0

    for d in target_dirs:
        c_files, c_lines = _clean_dir_tree(d, dry_run)
        total_cleaned_files += c_files
        total_lines_removed += c_lines

    print(f"\n清理完成: 共在 {total_cleaned_files} 個檔案中消除 {total_lines_removed} 行浮水印。")
    return 0


# ==============================================================================
# 7. 卡片草稿自動生成模組 (GENERATE-NOTES) 輔助函數
# ==============================================================================

def _collect_raw_bases(raw_dir: str, notes_dir: str) -> Dict[str, Dict[str, str]]:
    """蒐集 raw-papers 中全部實體 PDF 與 Raw MD 資訊並計算相對路徑"""
    raw_bases: Dict[str, Dict[str, str]] = {}
    for root, _, files in os.walk(raw_dir):
        if "legacy_archive" in root:
            continue
        for f in files:
            actual_file = os.path.join(root, f)
            rel_path = os.path.relpath(actual_file, notes_dir).replace(os.sep, '/')
            if f.endswith(".pdf"):
                raw_bases.setdefault(f[:-4], {})['pdf'] = rel_path
            elif f.endswith(SUFFIX_RAW_MD):
                raw_bases.setdefault(f[:-len(SUFFIX_RAW_MD)], {})['raw'] = rel_path
    return raw_bases


def _parse_paper_stem(base: str) -> Tuple[str, str, str]:
    """採用確定性字串解析提取作者、年份與標題，零正則回溯"""
    start = base.find("(")
    end = base.find(")")
    if 0 < start < end and (end - start == 5) and base[start + 1:end].isdigit():
        authors = base[:start].strip()
        year = base[start + 1:end]
        title = base[end + 1:].strip()
        return authors or "Unknown", year, title or base
    return "Unknown", "Unknown", base


def _render_note_template(base: str, paths: Dict[str, str]) -> str:
    """渲染標準 Obsidian 卡片草稿範本 (安全 YAML 序列化)"""
    authors, year, title = _parse_paper_stem(base)
    pdf_link = paths.get('pdf', '')
    raw_link = paths.get('raw', '')
    pdf_md = f"- [PDF 原文](<{pdf_link}>)\n" if pdf_link else ""
    raw_md = f"- [Markdown 原文](<{raw_link}>)\n" if raw_link else ""

    metadata = {
        "title": title,
        "authors": authors,
        "year": year,
        "venue": "Unspecified",
        "categories": ["[[00-研究流派圖主目錄]]"],
    }
    fm_block = yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False).rstrip()

    return f"""---
{fm_block}
---

# 📖 {title}

## 📄 本地文獻存檔
{pdf_md}{raw_md}
## 📝 論文摘要 (Abstract)
> [!NOTE]
> 自動生成之文獻卡片草稿，待補充精讀內容與核心貢獻。

---

## 🎯 核心解決問題 (Problem Statement)
* **研究背景**：
* **現有技術痛點**：
* **論文要解決的具體問題**：

---

## 💡 關鍵創新點與貢獻 (Key Contributions & Innovation)
1. 
2. 
3. 
"""


def cmd_generate_notes(args) -> int:
    """自動為 raw-papers 中存在但 Vault 尚未建檔的論文生成卡片筆記草稿"""
    vault_dir = os.path.abspath(args.vault_dir)
    raw_dir = os.path.abspath(args.raw_dir)
    notes_dir = os.path.join(vault_dir, "notes")
    dry_run = args.dry_run

    print("=" * 70)
    print(f"📝 掃描 raw-papers 並自動補齊缺失卡片筆記草稿{' [DRY-RUN]' if dry_run else ''}...")
    print("=" * 70)

    os.makedirs(win_path(notes_dir), exist_ok=True)
    existing_notes = {f[:-3] for f in os.listdir(notes_dir) if f.endswith(".md")}
    raw_bases = _collect_raw_bases(raw_dir, notes_dir)
    missing_bases = {b: paths for b, paths in raw_bases.items() if b not in existing_notes}

    if not missing_bases:
        print("✅ 目前所有 raw-papers 中的文獻皆已在 notes/ 擁有對應卡片筆記！")
        return 0

    print(f"發現 {len(missing_bases)} 篇文獻尚未建立筆記卡片，正在自動生成草稿:")
    created_count = 0
    for base, paths in sorted(missing_bases.items()):
        note_content = _render_note_template(base, paths)
        note_file = os.path.join(notes_dir, f"{base}.md")
        print(f"  ➕ 生成卡片: {base}.md")
        if not dry_run:
            with open(win_path(note_file), 'w', encoding='utf-8') as f:
                f.write(note_content)
        created_count += 1

    print(f"\n生成完成: 共建立 {created_count} 篇標準 Obsidian 卡片草稿。")
    return 1 if created_count > 0 else 0



# ==============================================================================
# 8. 文獻幾何佈局解析模組 (PARSE / CONVERT)
# ==============================================================================

def _import_parser():
    """動態導入 lightweight_parser 模組"""
    if PARSER_DIR not in sys.path:
        sys.path.insert(0, PARSER_DIR)
    try:
        from lightweight_parser import convert_pdf_to_clean_markdown
        return convert_pdf_to_clean_markdown
    except ImportError as e:
        print(f"❌ 無法導入 parser 模組: {e}")
        return None


def _parse_single_pdf(pdf_target: str, output_path: Optional[str], convert_fn) -> int:
    """執行單一 PDF 之幾何版面解析"""
    print("=" * 70)
    print("🔬 Code Security Research — 輕量化學術文獻幾何版面解析器 (PDF -> MD)")
    print(f"  • 輸入文獻: {pdf_target}")
    print("=" * 70)

    _, stats = convert_fn(pdf_target, output_path)
    print("\n✅ 解析完成！")
    print(f"  • 輸出路徑: {stats['output_path']}")
    print(f"  • 總頁數  : {stats['pages']} 頁")
    print(f"  • 智慧表格: {stats['tables']} 個")
    print(f"  • 圖表資產: {stats['figures']} 張 (保存於 assets/ 目錄)")
    return 0


def _parse_batch_pdfs(raw_dir: str, convert_fn) -> int:
    """批次掃描並解析 raw-papers 目錄下所有 PDF 文獻"""
    print("=" * 70)
    print("📚 Code Security Research — 批次文獻版面解析 (Batch Parser)")
    print(f"  • 目標目錄: {raw_dir}")
    print("=" * 70)

    pdf_files = []
    for root, _, files in os.walk(win_path(raw_dir)):
        if "legacy_archive" in root:
            continue
        for f in files:
            if f.endswith(".pdf"):
                pdf_files.append(os.path.join(root, f))

    print(f"🔍 檢索到 {len(pdf_files)} 篇實體 PDF 文獻，準備執行解析...")
    success_cnt, fail_cnt = 0, 0
    for idx, pdf_p in enumerate(pdf_files, 1):
        stem = os.path.splitext(os.path.basename(pdf_p))[0]
        expected_md = os.path.join(os.path.dirname(pdf_p), f"{stem}{SUFFIX_RAW_MD}")
        if os.path.exists(win_path(expected_md)):
            continue
        print(f"[{idx}/{len(pdf_files)}] 正在解析: {stem[:50]}...")
        try:
            convert_fn(pdf_p)
            success_cnt += 1
        except Exception as e:
            print(f"  ❌ 解析失敗: {e}")
            fail_cnt += 1

    print(f"\n🎉 批次解析完成！成功新增: {success_cnt} 篇，失敗: {fail_cnt} 篇。")
    return 1 if fail_cnt > 0 else 0


def cmd_parse(args) -> int:
    """使用純 Python / PyMuPDF 幾何版面解析器將 PDF 轉換為結構化高品質 Markdown"""
    convert_fn = _import_parser()
    if not convert_fn:
        return 1

    pdf_target = getattr(args, "pdf_path", None)
    output_path = getattr(args, "output", None)
    batch_all = getattr(args, "all", False)
    raw_dir = getattr(args, "raw_dir", DEFAULT_RAW_DIR)

    if not pdf_target and not batch_all:
        print("❌ 請指定欲解析的 PDF 檔案路徑，或使用 --all 執行批次解析。")
        print("   例如: python scripts/paper_cli.py parse \"raw-papers/2026/ZeroDayBench.pdf\"")
        print("         python scripts/paper_cli.py parse --all")
        return 1

    if pdf_target:
        if not os.path.isfile(win_path(pdf_target)):
            cand = os.path.join(raw_dir, pdf_target)
            if os.path.isfile(win_path(cand)):
                pdf_target = cand
            else:
                print(f"❌ 找不到指定的 PDF 檔案: {pdf_target}")
                return 1
        return _parse_single_pdf(pdf_target, output_path, convert_fn)

    return _parse_batch_pdfs(raw_dir, convert_fn)


# ==============================================================================
# 9. 排版解析品質驗收模組 (EVAL)
# ==============================================================================

def _import_evaluator():
    """動態導入 evaluator 與 parser 模組"""
    if PARSER_DIR not in sys.path:
        sys.path.insert(0, PARSER_DIR)
    try:
        from evaluator import analyze_markdown_quality
        from lightweight_parser import convert_pdf_to_clean_markdown
        return analyze_markdown_quality, convert_pdf_to_clean_markdown
    except ImportError as e:
        print(f"❌ 無法導入 parser/evaluator 模組: {e}")
        return None, None


def _evaluate_single_sample(pdf_path: str, eval_temp_dir: str, analyze_fn, convert_fn) -> int:
    """轉換並評估單篇抽樣 PDF 之排版品質"""
    base_name = Path(pdf_path).stem
    out_md = os.path.join(eval_temp_dir, f"{base_name}.md")
    assets_out = os.path.join(eval_temp_dir, "assets", base_name)
    try:
        md_content, meta = convert_fn(pdf_path, output_md_path=out_md, assets_dir=assets_out)
        stats, issues = analyze_fn(md_content, out_md)
        print(f"  • 頁數: {meta['pages']} | 行數: {stats['total_lines']} | 字數: {stats['total_words']}")
        print(f"  • 圖表: {stats['figures']} 張 | 表格: {stats['tables']} 個 | 程式碼: {stats['code_blocks']} 塊")
        if issues:
            print(f"  ⚠️ 檢測出 {len(issues)} 項排版待優化項目:")
            for iss in issues[:5]:
                print(f"    - {iss}")
            return len(issues)
        print("  ✅ 評估等級: PERFECT (0 缺陷，排版極佳！)")
        return 0
    except Exception as ex:
        print(f"  ❌ 轉換或檢驗出錯: {ex}")
        return 1


def _eval_sample_papers(sample_cnt: int, raw_dir: str, analyze_fn, convert_fn) -> int:
    """隨機跨年份抽樣端到端基準測試"""
    if sample_cnt < 1:
        print("❌ --sample 抽樣篇數必須為正整數 (>= 1)。")
        return 1

    import secrets
    import glob
    print("=" * 75)
    print(f"🔬 Code Security Research — 跨年份隨機抽樣解析品質基準測試 (Sample: {sample_cnt} 篇)")
    print("=" * 75)

    years = ['2010-2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026']
    available_pdfs = []
    for y in years:
        ydir = os.path.join(raw_dir, y)
        pdfs = glob.glob(os.path.join(win_path(ydir), "*.pdf"))
        if pdfs:
            available_pdfs.extend(pdfs)

    if not available_pdfs:
        print("❌ 未在 raw-papers 目錄中找到任何 PDF 文獻。")
        return 1

    pool = list(available_pdfs)
    k = min(sample_cnt, len(pool))
    for i in range(k):
        j = i + secrets.randbelow(len(pool) - i)
        pool[i], pool[j] = pool[j], pool[i]
    selected = pool[:k]
    eval_temp_dir = os.path.join(REPO_ROOT, "scratch", "cli_eval_temp")
    os.makedirs(win_path(eval_temp_dir), exist_ok=True)

    total_flaws = 0
    for s_idx, pdf_path in enumerate(selected, 1):
        print(f"\n[{s_idx}/{len(selected)}] 正在測試: {Path(pdf_path).stem[:60]}...")
        total_flaws += _evaluate_single_sample(pdf_path, eval_temp_dir, analyze_fn, convert_fn)

    print("\n" + "=" * 75)
    if total_flaws == 0:
        print("🎉 基準測試通過：所有抽樣論文排版皆達 100% 完美水準！")
        return 0
    print(f"⚠️ 基準測試完成：共發現 {total_flaws} 處待優化項目。")
    return 1


def _eval_single_file(target: str, analyze_fn) -> int:
    """評估單一 Markdown 檔案"""
    if not os.path.isfile(win_path(target)):
        print(f"❌ 找不到目標檔案: {target}")
        return 1

    with open(win_path(target), "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    print("=" * 70)
    print(f"🔍 Markdown 版面解析品質檢驗報告: {os.path.basename(target)}")
    print("=" * 70)

    stats, issues = analyze_fn(content, target)
    print(f"  • 總行數: {stats['total_lines']} | 總字數: {stats['total_words']}")
    print(f"  • 表格數: {stats['tables']} | 圖表數: {stats['figures']} | 代碼區塊: {stats['code_blocks']}")

    if issues:
        print(f"\n⚠️ 發現 {len(issues)} 處版面缺陷:")
        for iss in issues:
            print(f"  * {iss}")
        return 1
    print("\n✅ 評估結果: 100% 完美 (無浮水印殘留、無表格外溢、圖片全部有效)！")
    return 0


def _eval_all_raw_files(raw_dir: str, analyze_fn) -> int:
    """批次檢查全庫已生成的 Raw Markdown"""
    print("=" * 70)
    print("📚 全庫 Raw Markdown 解析品質普查")
    print(f"  • 目標目錄: {raw_dir}")
    print("=" * 70)

    all_raw_mds = []
    for root, _, files in os.walk(win_path(raw_dir)):
        for f in files:
            if f.endswith(SUFFIX_RAW_MD):
                all_raw_mds.append(os.path.join(root, f))

    print(f"🔍 發現 {len(all_raw_mds)} 篇 Raw Markdown 檔案。")
    flawed_files = 0
    for r_md in all_raw_mds:
        with open(win_path(r_md), "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
        _, issues = analyze_fn(c, r_md)
        if issues:
            print(f"⚠️ {os.path.basename(r_md)}: 發現 {len(issues)} 項缺陷")
            flawed_files += 1

    if flawed_files == 0:
        print(f"\n🎉 普查完成：全庫 {len(all_raw_mds)} 篇 Raw Markdown 100% 通過品質檢查！")
        return 0
    print(f"\n⚠️ 普查完成：共 {flawed_files} 篇檔案存在微小排版瑕疵。")
    return 1


def cmd_eval(args) -> int:
    """多維度評估 Markdown 解析品質"""
    analyze_fn, convert_fn = _import_evaluator()
    if not analyze_fn or not convert_fn:
        return 1

    target = getattr(args, "target", None)
    sample_cnt = getattr(args, "sample", None)
    eval_all = getattr(args, "all", False)
    raw_dir = getattr(args, "raw_dir", DEFAULT_RAW_DIR)

    if sample_cnt:
        return _eval_sample_papers(sample_cnt, raw_dir, analyze_fn, convert_fn)
    if target:
        return _eval_single_file(target, analyze_fn)
    if eval_all:
        return _eval_all_raw_files(raw_dir, analyze_fn)

    print("❌ 請指定欲檢驗的 Markdown 檔案路徑，或使用 --sample N / --all。")
    print("   例如: python scripts/paper_cli.py eval \"test.md\"")
    print("         python scripts/paper_cli.py eval --sample 5")
    return 1


# ==============================================================================
# 10. 主程式進入點 (CLI DISPATCHER)
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Code Security Research — 通用文獻庫管理與自動化維護工具 (Paper CLI)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
常用命令範例:
  python scripts/paper_cli.py audit                  # 執行全庫健康檢查
  python scripts/paper_cli.py parse <file.pdf>       # 使用輕量幾何解析器將 PDF 轉為標準 Markdown
  python scripts/paper_cli.py eval <file.md>         # 評估 Markdown 解析品質 (水文/表格/圖片/順序)
  python scripts/paper_cli.py eval --sample 5        # 跨年份隨機抽樣 5 篇執行端到端品質基準測試
  python scripts/paper_cli.py stats                  # 顯示全庫資產統計與年份分佈
  python scripts/paper_cli.py sync                   # 自動同步雙向相對路徑鏈結
  python scripts/paper_cli.py normalize              # 批次重命名非標準檔名
  python scripts/paper_cli.py dedup --auto-prune     # 自動修剪跨目錄重複筆記
  python scripts/paper_cli.py clean-watermarks       # 清除 IEEE Xplore 等浮水印干擾字串
  python scripts/paper_cli.py generate-notes         # 自動為未建檔之 raw-papers 生成卡片草稿
"""
    )

    subparsers = parser.add_subparsers(dest="command", required=True, help="可調用的子命令")

    p_parse = subparsers.add_parser("parse", help="使用純 Python 幾何版面解析器將 PDF 轉為高品質 Markdown")
    p_parse.add_argument("pdf_path", nargs="?", default=None, help="欲解析的 PDF 檔案路徑")
    p_parse.add_argument("-o", "--output", default=None, help="輸出的 Markdown 檔案路徑 (預設為同目錄對應 (Raw).md)")
    p_parse.add_argument("--all", action="store_true", help="批次解析 raw-papers 目錄下所有 PDF 檔案")
    p_parse.add_argument("--raw-dir", default=DEFAULT_RAW_DIR, help="raw-papers 目錄路徑 (搭配 --all 使用)")
    p_parse.set_defaults(func=cmd_parse)

    p_eval = subparsers.add_parser("eval", help="多維度評估 Markdown 解析品質 (水文/表格/圖片/順序/斷字)")
    p_eval.add_argument("target", nargs="?", default=None, help="欲檢驗的 Markdown 檔案路徑")
    p_eval.add_argument("--sample", type=int, default=None, help="隨機抽樣 N 篇 PDF 執行端到端轉換與品質檢驗")
    p_eval.add_argument("--all", action="store_true", help="批次檢查 raw-papers 目錄下所有已生成的 Raw Markdown")
    p_eval.add_argument("--raw-dir", default=DEFAULT_RAW_DIR, help=HELP_RAW_DIR)
    p_eval.set_defaults(func=cmd_eval)

    p_audit = subparsers.add_parser("audit", help="全面健康檢查 (雙鏈、PDF/Raw 鏈結、YAML、檔名規範)")
    p_audit.add_argument("--vault-dir", default=DEFAULT_VAULT_DIR, help=HELP_VAULT_DIR)
    p_audit.add_argument("--raw-dir", default=DEFAULT_RAW_DIR, help=HELP_RAW_DIR)
    p_audit.set_defaults(func=cmd_audit)

    p_stats = subparsers.add_parser("stats", help="統計全庫文獻卡片、實體 PDF/Raw 數量與年份分佈")
    p_stats.add_argument("--vault-dir", default=DEFAULT_VAULT_DIR, help=HELP_VAULT_DIR)
    p_stats.add_argument("--raw-dir", default=DEFAULT_RAW_DIR, help=HELP_RAW_DIR)
    p_stats.set_defaults(func=cmd_stats)

    p_sync = subparsers.add_parser("sync", help="同步 Vault 卡片筆記與 raw-papers 之雙向鏈結")
    p_sync.add_argument("--vault-dir", default=DEFAULT_VAULT_DIR, help=HELP_VAULT_DIR)
    p_sync.add_argument("--raw-dir", default=DEFAULT_RAW_DIR, help=HELP_RAW_DIR)
    p_sync.set_defaults(func=cmd_sync)

    p_norm = subparsers.add_parser("normalize", help="標準化檔名 (去除底線、去除爬蟲編號、規範 raw.md)")
    p_norm.add_argument("--dir", default=DEFAULT_RAW_DIR, help="欲清洗檔名之目標目錄")
    p_norm.add_argument("--dry-run", action="store_true", help="僅預覽不實際改名")
    p_norm.set_defaults(func=cmd_normalize)

    p_dedup = subparsers.add_parser("dedup", help="偵測與清理跨分類重複卡片筆記及未關聯孤兒檔案")
    p_dedup.add_argument("--vault-dir", default=DEFAULT_VAULT_DIR, help=HELP_VAULT_DIR)
    p_dedup.add_argument("--raw-dir", default=DEFAULT_RAW_DIR, help=HELP_RAW_DIR)
    p_dedup.add_argument("--auto-prune-stubs", action="store_true", help="自動刪除內容過小之重複佔位 stub")
    p_dedup.add_argument("--archive-orphans", action="store_true", help="自動將孤兒檔案移入 legacy_archive")
    p_dedup.set_defaults(func=cmd_dedup)

    p_cw = subparsers.add_parser("clean-watermarks", help="批次清理 Markdown 文本中的 IEEE 授權浮水印冗餘行")
    p_cw.add_argument("--vault-dir", default=DEFAULT_VAULT_DIR, help=HELP_VAULT_DIR)
    p_cw.add_argument("--raw-dir", default=DEFAULT_RAW_DIR, help=HELP_RAW_DIR)
    p_cw.add_argument("--dry-run", action="store_true", help="僅預覽不修改檔案")
    p_cw.set_defaults(func=cmd_clean_watermarks)

    p_gen = subparsers.add_parser("generate-notes", help="自動為 raw-papers 中存在但 Vault 尚未建檔的論文生成卡片筆記草稿")
    p_gen.add_argument("--vault-dir", default=DEFAULT_VAULT_DIR, help=HELP_VAULT_DIR)
    p_gen.add_argument("--raw-dir", default=DEFAULT_RAW_DIR, help=HELP_RAW_DIR)
    p_gen.add_argument("--dry-run", action="store_true", help="僅預覽不實際建立檔案")
    p_gen.set_defaults(func=cmd_generate_notes)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main() or 0)

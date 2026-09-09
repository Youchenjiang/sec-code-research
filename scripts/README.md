# Code Security Research — 腳本庫與自動化工具指南 (Scripts & Tooling Guide)

本目錄包含專案在學術文獻管理、爬蟲檢索、PDF 高精度排版解析以及知識庫（Obsidian Vault）自動化維護過程中所使用的核心模組與專用工具。所有過往散落的一次性臨時腳本均已收斂整合成模組化工具與統一的 **`paper_cli.py`** 命令行套件。

---

## 📂 目錄結構概覽

```text
scripts/
├── paper_cli.py              # 🌟 全功能文獻管理 CLI 工具 (審查、統計、同步、標準化、查重、浮水印清理、建檔)
├── README.md                 # 本工具庫指南 (本文件)
│
├── crawler/                  # 🌐 文獻爬蟲與元數據檢索模組
│   ├── download_paper.py     # 整合多源 (ArXiv, Direct URL, DOI) 與 PDF 驗證的下載器
│   └── search_arxiv.py       # ArXiv API 關鍵字批次檢索工具
│
├── parser/                   # 📄 PDF 轉 Markdown 高精度解析模組
│   ├── pdf-to-md.js          # 基於 pdfjs-dist 的佈局感知、表格重構與圖片抽取解析引擎
│   └── README.md             # 解析模組詳細使用說明
│
├── diagram/                  # 🗺️ 拓撲圖譜建置工具
│   └── generate_drawio.py    # 論文引用脈絡圖譜之 Draw.io 向量 XML 生成與原生壓縮
```


---

## 🌟 核心文獻管理通用工具 (`scripts/paper_cli.py`)

所有日常文獻庫維護作業均已統一至 `paper_cli.py`，未來引入新文獻或進行例行健康檢查時，只需調用對應子命令：

```bash
# 1. 全方位健康審查 (檢查實體鏈結、內部雙鏈、YAML 格式、檔名標準、主目錄索引)
python scripts/paper_cli.py audit

# 2. 全庫資產總覽與年份統計 (統計筆記、報告、矩陣、PDF/Raw 覆蓋率及年份分佈)
python scripts/paper_cli.py stats

# 3. 自動同步雙向鏈結 (自動計算相對路徑並掛載 [PDF 原文] 與 [Markdown 原文])
python scripts/paper_cli.py sync

# 4. 批次檔名洗滌標準化 (自動去除爬蟲前綴如 81_、清除下劃線、規範 (Raw).md)
python scripts/paper_cli.py normalize

# 5. 跨流派查重與孤兒實體檔案清理 (自動揪出重複 stub 與未建檔 PDF)
python scripts/paper_cli.py dedup

# 6. 批次浮水印與授權干擾字串清理 (消除 IEEE Xplore 等授權行)
python scripts/paper_cli.py clean-watermarks

# 7. 自動補齊缺失之卡片筆記草稿 (為 raw-papers 中尚未在 notes/ 建檔之文獻建立標準卡片)
python scripts/paper_cli.py generate-notes
```

---

## 🌐 論文爬蟲模組 (`scripts/crawler/`)

- **`download_paper.py`**：支援輸入 `--url` 或 `--title`，自動進行串流下載並以 `%PDF-` 檔頭與檔案大小驗證 PDF 合法性，避免抓取到 403/404 錯誤網頁。
- **`search_arxiv.py`**：透過 ArXiv REST API 根據標題或關鍵字查詢學術預印本，輸出論文標題、發表日期、PDF 下載連結與摘要。

---

## 📄 PDF 解析模組 (`scripts/parser/`)

- **`pdf-to-md.js`**：採用純 Node.js + `pdfjs-dist`，支援雙欄版面順序重構、Markdown 語法表格還原（`| col1 | col2 |`）以及嵌入圖表向量抽取。詳見 [parser/README.md](file:///scripts/parser/README.md)。

# 📄 高精度學術文獻版面解析模組 (Parser Package)

本模組提供零依賴大型深度學習模型、純 Python / PyMuPDF 的學術論文排版幾何解析引擎，已完整整合至 `scripts/paper_cli.py` 命令行工具。

## 核心工具

- **`lightweight_parser.py`**（推薦主引擎）：
  - 純 Python + PyMuPDF 幾何版面解析引擎。
  - **特點**：
    1. **智慧標題層級識別**：依字體大小、粗體與章節編號規則自動對應 H1~H4。
    2. **學術表格重構 (TableRecognizer)**：整合原生 `find_tables()` 與幾何啟發式掃描，防止單元格外溢與圖表網格誤判。
    3. **圖表區域偵測與外置 (FigureRecognizer)**：BBox 精準匹配高解析度原圖，自動外置剪裁並以 `<...>` 語法保護 Markdown 預覽。
    4. **閱讀流動自適應重組**：寬區塊幾何約束，精準解耦雙欄 Abstract 與 Introduction 閱讀順序。
    5. **頁面雜訊過濾與音節修復**：自動剔除頂部頁眉、底部頁碼、IEEE/ACM/USENIX/TechRxiv 浮水印，並以 `fix_hyphenation` 智慧拼接行尾斷字。
- **`evaluator.py`**（排版品質驗收引擎）：
  - 多維度自動審查 Markdown 是否存在浮水印殘留、表格吞噬正文、圖片失效、雙欄順序顛倒或連字號斷裂。
- **`pdf-to-md.js`**：基於 Node.js 與 `pdfjs-dist` 的輔助版面解析工具。

---

## 調用方式 (建議直接使用 CLI)

```bash
# 1. 透過 paper_cli 解析單一論文 PDF
python scripts/paper_cli.py parse "raw-papers/2026/ZeroDayBench.pdf"

# 2. 指定自訂輸出路徑
python scripts/paper_cli.py parse "raw-papers/2026/ZeroDayBench.pdf" -o "custom_output.md"

# 3. 批次解析 raw-papers 目錄下所有 PDF
python scripts/paper_cli.py parse --all

# 4. 驗收已生成的 Markdown 解析品質
python scripts/paper_cli.py eval "raw-papers/2026/ZeroDayBench (Raw).md"

# 5. 跨年份隨機抽樣 5 篇執行端到端品質基準測試
python scripts/paper_cli.py eval --sample 5

# 6. 直接調用底層模組
python scripts/parser/lightweight_parser.py "raw-papers/2026/ZeroDayBench.pdf"
```


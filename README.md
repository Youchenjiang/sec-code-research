# 🛡️ 程式碼安全學術流派知識庫 (Code Security Research Vault)

基於 **Obsidian 雙向連結**與 **Git 流程**建構的程式碼安全學術研究流派知識庫。本專案系統化梳理了「設計安全」、「靜態分析」、「動態分析（黑箱與白/灰箱）」與「自動程式修復 (APR)」四大安全研究領域的 38 個子技術流派，並利用 Obsidian Dataview 實現論文分類與自動化彙整。

---

## 📈 動態測試與安全探索技術演進脈絡

動態測試與安全漏洞挖掘在近年經歷了深刻的技術轉變，從「盲目探索」演進至「深度語意與自主 Agent 驅動」。下圖展示了本知識庫中動態分析與模糊測試（Fuzzing）技術的四個關鍵演進階段：

```text
隨機測試 (如 Monkey)
       │
       ▼
基於模型/狀態引導 (如 Ape, Fastbot2)
       │
       ▼
大模型語意引導與 VLM 多模態探索 (如 VLM-Fuzz, AndroidLens)
       │
       ▼
自主 Agent + 靜動結合全域攻防 (如 CovAgent, GAPS)
```

### 💡 核心演進特徵
1. **探索方式的語意化**：從盲目的隨機事件生成，演進為對 UI 層次與業務邏輯的狀態抽象，再到利用大模型（LLM/VLM）的常識推理與視覺理解能力進行自主規劃。
2. **深度漏洞挖掘與安全攻防的縱向升級**：動態分析的焦點已從早期的「通用功能測試」升級為「深層系統服務反序列化安全測試 (如 NASS)」、「閉源組件 Intent 灰盒測試 (如 MALintent)」、「可信執行環境 (TEE) 的黑盒與灰盒安全探索 (如 TEEzz)」。
3. **靜動雙向融合**：純動態測試容易遇到「30% 覆蓋率詛咒」，現代前沿研究（如 GAPS、CovAgent）正全面採用大模型引導的靜態路徑合成（Static Path Synthesis）來生成精準輸入與插樁腳本，打通靜動分析的壁壘。

---

## 📁 目錄結構與維護分工

專案根目錄包含兩個主要部分：**管理工具與設定檔**（Git 根目錄）及 **Obsidian 知識庫本體** (`research-vault/`)。

```text
├── .github/workflows/policy.yml  # PR 標題與 Commit 規範自動檢查 (CI)
├── .gitmessage.txt               # 本地 Commit 模板提示
├── CONTRIBUTING.md               # 分支開發與 Git 規範
├── README.md                     # 專案介紹與本知識庫規範 (本檔案)
├── setup_vault.py                # 【唯讀/自動生成】流派圖結構生成腳本
└── research-vault/               # 【Obsidian 知識庫本體】
    ├── 00-研究流派圖主目錄.md      # 知識庫首頁 (Index)
    ├── 0-設計安全與威脅分析 (Secure Design & Threat Analysis)/ # 設計安全與威脅建模流派
    ├── 1-靜態分析 (Static Analysis)/                           # 靜態分析與相依性安全（1A.1 - 1D.5）
    ├── 2-動態分析 (Dynamic Analysis)/                          # 動態分析與插樁強化（2A.1 - 2D.5）
    ├── 3-自動修復 (Automated Program Repair - APR)/            # 自動程式修復流派（3A.1 - 3C.2）
    ├── templates/                 # 筆記模板資料夾
    │   └── Paper Template.md     # 論文錄入模板
    ├── pdfs/                      # 【本地 PDF 儲存區】放個人閱讀的 PDF 檔案 (Git 忽略)
    └── papers/                    # 【論文筆記存放區】所有論文 Markdown 均放於此
```

### ⚠️ 維護分工原則：
1. **流派分類檔案（`1-*`、`2*`、`3*` 資料夾下的 Markdown 檔案及主目錄）**：
   * **禁止手動修改**。這些檔案是由 `setup_vault.py` 中的 `CATEGORIES` 字典統一管理的。
   * 若需更新流派的名稱、核心精神、代表工具或關鍵字，**必須先修改 `setup_vault.py`，再於本地執行 `python setup_vault.py` 重新生成**。
2. **論文筆記檔案（`research-vault/papers/` 目錄）**：
   * 均由人工（或導入腳本）進行撰寫與維護，不受 `setup_vault.py` 生成影響。

---

## 📝 論文筆記命名與元數據 (Frontmatter) 規範

為了確保 Obsidian Dataview 插件能夠正確抓取並動態彙整論文，新錄入的論文必須符合以下標準：

### 1. 檔案命名規範
* **格式**：`<normalized-paper-title>-<year>.md`
* **範例**：`example-paper-aflnet-2020.md`、`example-paper-raven-2026.md`
* **規則**：
  * 檔名一律使用**全小寫**。
  * 移除所有特殊字元（如 `:`、`?`、`/`、`'`），空白以減號 `-` 代替。
  * 檔名末尾必須附上 **4 碼發表年份**，且該年份必須與元數據中的 `year` 屬性保持一致。

### 2. YAML Frontmatter 元數據規範
每篇論文的 Markdown 頂部必須包含以下 YAML 屬性（可直接複製 `templates/Paper Template.md`）：

```yaml
---
title: "AFLNet: A Greybox Fuzzer for Network Protocols"  # 論文完整標題
authors: "Van-Thuan Pham, et al."                       # 作者清單
year: 2020                                              # 發表年份 (必須為 4 碼數字)
venue: "ICSE 2020"                                      # 發表期刊或研討會
url: "https://dl.acm.org/doi/10.1145/3377811.3380434"   # 論文官方連結 (必須記錄)
code: "https://github.com/aflnet/aflnet"                # 開源代碼連結 (若無則留空 "")
categories:                                             # 流派歸類 (雙引號 + 雙括號雙向連結)
  - "[[2A.2-黑箱協定模糊測試 (Black-box Protocol Fuzzing)]]"
  - "[[2B.1-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]"
---
```

---

## 📄 本地 PDF 管理方案 (Option C)

為了保持 Git 倉庫輕量並避免版權爭議，本專案實施 **PDF 本地化管理**：

1. **存放路徑**：請將下載的 PDF 丟入 `research-vault/pdfs/` 資料夾中。
2. **Git 忽略**：`.gitignore` 已經被配置為忽略 `research-vault/pdfs/`，您的 PDF 檔案不會被上傳至 GitHub。
3. **Obsidian 連結**：在論文 Markdown 內文的第一板塊中，使用 `[[your-file.pdf]]` 建立雙向連結，便可在 Obsidian 中進行雙螢幕並排閱讀與標註。

---

## 🔗 多重流派分類規則 (Multi-Mapping Rules)

軟體安全領域的論文往往兼具多種技術特徵（例如：利用機器學習輔助資料流分析、或是自動修復系統中整合了補丁正確性驗證）。

* **多選分類**：當論文跨多個子領域時，**必須在 `categories` 屬性中同時列出所有關聯的流派雙向連結**（如上述 AFLNet 範例，同時列出了 2A.2 與 2B.1）。
* **Dataview 自動索引**：只要完成多重連結，該論文便會同時出現在這兩個流派檔案底部的論文清單中，無需重複拷貝檔案或進行多處手動更新。

---

## 🚀 貢獻與提交流程 (Git Workflow)

本專案使用嚴格的分支策略與 Commit 規範。所有修改均需透過建立 Topic 分支與 Pull Request (PR) 進行。請詳閱 [CONTRIBUTING.md](CONTRIBUTING.md) 以瞭解分支規則、原子提交與 Commit 訊息格式規範。

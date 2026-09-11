---
title: "文獻庫架構與自動化維護規範手冊 (Paper Vault Guide)"
type: guide
updated: 2026-09-05
tags:
  - guide/vault
  - moc/rules
---

# 📖 文獻庫架構與自動化維護規範手冊 (Paper Vault Guide)

> [!IMPORTANT]
> 本文件為程式碼安全文獻庫（Code Security Research Vault）之**權威命名、格式排版、文獻分層與自動化維護規範**。
> 所有人工維護、腳本解析與未來的 AI Agent 自動化匯入，**必須 100% 嚴格遵守本手冊之準則**。

---

## 🧭 一、 核心命名準則 (Naming Standard)

### ⛔ 最高禁令：絕不使用作者姓名作為檔名前綴！
在資安技術與軟體工程研究中，檢索核心在於**「工具系統」**與**「研究類型」**，作者姓名無法直觀傳遞技術內涵。

---

### 规则 1：工具優先準則 (Tool-First)
若論文提出了具體的開源原型、檢測系統或工具架構，**強制以「工具/系統名稱」作為檔名首詞**：

```
格式：ToolName (Year) Full Title
```

- **正確範例**：
  - `Humanoid (2019) A Deep Learning-Based Approach to Automated Black-box Android App Testing`
  - `TaintDroid (2010) Information-Flow Tracking System for Realtime Privacy Monitoring`
  - `Dynodroid (2013) Input Generation System for Android Apps`
  - `Sapienz (2016) Multi-Objective Automated Testing for Android Applications`
  - `AgentScan (2025) Exploring the Security Risks of Mobile LLM Agents`
  - `MARD (2024) Multi-Agent Framework for Robust Android Malware Detection`
  - `CAI (2024) Open Bug Bounty-Ready Cybersecurity AI`
  - `RAVEN (2026) Retrieval-Augmented Vulnerability Exploration Network`
  - `Stoat (2017) Guided Stochastic Model-Based GUI Testing of Android Apps`

---

### 规则 2：無工具時，依「領域-研究類型」前綴 (Category-Type Prefix)
若論文為綜述、實證調查或純方法論探討（未命名獨立工具），**強制以 `<Domain>-<Type>` 作為檔名首詞**：

```
格式：<Domain>-<Type> (Year) Full Title
```

| 研究類型 (<Type>) | 適用場景 | 標準命名範例 |
| :--- | :--- | :--- |
| **`Survey` / `SoK`** | 文獻綜述、知識體系化整理 | `LLM-Pentest-Survey (2026) Survey of LLM-Driven Penetration Testing`<br>`AIxCC-SoK (2026) DARPA AI Cyber Challenge Competition Design`<br>`Mobile-Security-Survey (2013) Testing Approaches and Challenges` |
| **`Empirical` / `Study`** | 大規模實證測量、生態系調查、抗性評測 | `Obfuscation-Empirical (2024) Code Obfuscation Practices in Google Play`<br>`TLS-Security-Empirical (2021) Revisiting TLS InSecurity in Android`<br>`Runtime-Analysis-Empirical (2025) Android Dynamic Analysis Combat Anti-Analysis` |
| **`Method` / `Framework`** | 提出全新演算法、變異模型或測試流程 | `DAST-Method (2024) LLM-Guided Dynamic Security Testing of Android`<br>`Fuzzing-Method (2025) Semantic-Aware Fuzzing Framework for Input Mutation`<br>`Target-Path-Method (2022) Driving Execution of Target Paths in Android` |
| **`Benchmark` / `Dataset`** | 靶場、評測標準集、漏洞庫 | `Offensive-Security-Benchmark-Study (2025) Benchmarking Practices in LLM`<br>`CyberGym-Benchmark (2026) Scalable Real-World Cybersecurity Benchmark` |

---

### 规则 3：標題完整性（禁止截斷）
- 標題**嚴禁截斷在介系詞或冠詞**（如 `through.`, `of.`, `for.`, `the.`, `with.`）。
- 檔名中的標題必須語意完整、表達核心技術貢獻。

---

## 📐 二、 出版級 Markdown 原文解析標準 (Publication-Grade Raw Markdown)

原始文獻轉 Markdown（`raw-papers/<year>/... (Raw).md`）必須達到出版級品質，徹底杜絕暴力 OCR 瑕疵：

1. **結構化表格重建**：
   - 嚴禁表格坍塌為直列零散單詞（如 `touch 0.7` 直列堆疊）。
   - 必須轉換為標準 GFM 表格語法（`| Col 1 | Col 2 |`），保留數學公式（`$...$`）與對齊格式。
2. **向量裁切純淨高解析圖片（No Duplicate Captions）**：
   - 頁面截圖裁切必須在 Caption 上方精準截止，**嚴禁截圖自帶 Caption 文字**，防止 Markdown 又重複印出一行 Caption 的雙重冗餘。
   - 複合圖（如 Figure 2 包含 Overview 與 Architecture 兩部分）必須拆解為乾淨獨立的插圖展示。
3. **段落連貫性修合（Cross-page Paragraph Healing）**：
   - 學術論文中的浮動插圖（Float Figures）不可暴力腰斬跨頁句子。
   - 跨頁被斷開的句子必須在 Markdown 中自動接合，將 Figure 順延至該討論段落之後呈現。

---

## 🎓 三、 學術論文文獻分層金字塔 (The Citation Pyramid)

為了解決「全景調研（200+ 篇廣度）」與「最終論文寫作（30~50 篇深度）」的混淆，全庫文獻按四層架構管理：

- **Tier 1: 核心實驗對照組 (Direct Baselines to Compare)**  
  *論文實驗評測中，必須在同一實驗環境與數據集下直面 PK、對比覆蓋率與漏洞發掘率的 SOTA 工具。*
  👉 集中收錄於 [[00-我的論文核心文獻庫 (Thesis Core References)|00-我的論文核心文獻庫]]。
- **Tier 2: 理論基石與架構設計 (Foundational Theory & Problem Formulation)**  
  *支撐核心 Motivation、定義威脅模型（Threat Model）與演算法出發點的經典文獻。*
- **Tier 3: Chapter 2 Related Work 預選清單 (Related Work Pre-selection)**  
  *按靜態分析、動態探索、LLM 安全自動化分門別類，闡述技術演進與現有侷限性。*
- **Tier 4: 公開評測數據集與基準 (Evaluation Benchmarks & CyberGym)**  
  *標準測試集、歷史 CVE 倉庫與動態 CTF 靶場。*

---

## 🤖 四、 自動化維護與 AI Agent 接入介面 (Paper CLI & Agent Protocol)

文獻庫內建通用命令列工具 `scripts/paper_cli.py`，作為全庫健康審查與未來 AI Agent 自動維護的標準核心：

```bash
# 1. 執行全庫健康檢查 (100% 雙鏈、實體檔案、YAML 與檔名規範審查)
python scripts/paper_cli.py audit

# 2. 自動同步 Vault 筆記與 raw-papers 實體檔案之相對鏈結
python scripts/paper_cli.py sync

# 3. 檔名標準化清洗
python scripts/paper_cli.py normalize

# 4. 針對新下載的 PDF 自動生成 Obsidian 卡片筆記草稿
python scripts/paper_cli.py generate
```

### 🤖 AI Agent 新增論文之標準五步流程：
1. **下載與存放**：將 PDF 存放至 `raw-papers/<year>/`，依【工具優先】或【類別前綴】規範命名。
2. **出版級解析**：產出無碎表、無重複 Caption、段落流暢的 `(Raw).md`。
3. **建立筆記**：在 `research-vault/notes/` 建立同名筆記，標註對應的研究流派（`categories:`）。
4. **鏈結同步**：執行 `python scripts/paper_cli.py sync` 自動掛載雙向相對鏈結。
5. **健康終驗**：執行 `python scripts/paper_cli.py audit` 確認全庫維持 100% HEALTHY。

---

## 🔗 快速跳轉
- 返回 [[00-研究流派圖主目錄|🛡️ 程式碼安全研究流派圖主目錄]]
- 查閱 [[00-我的論文核心文獻庫 (Thesis Core References)|🎓 我的論文核心文獻庫]]
- 查閱 [[PAPERS_METADATA_TABLE|📑 頂會論文全集元數據總表]]

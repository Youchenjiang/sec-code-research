---
title: "RAVEN: Retrieval-Augmented Agentic Program Repair for Complex CVEs"
authors: "Security Research Group"
year: 2026
venue: "USENIX Security 2026"
url: "https://arxiv.org/abs/2600.00000"
code: "https://github.com/example/raven"
categories:
  - "[[3.5-LLM與Agent驅動修復 (LLM & Agentic)]]"
  - "[[3.6-安全補丁驗證與PCA (Validation & PCA)]]"
---

# RAVEN: Retrieval-Augmented Agentic Program Repair for Complex CVEs

## 💡 核心創新點 (Core Contributions)
- 提出了一套 **RAG + Agentic 迭代修復系統**，顯著提升了真實複雜 CVE 的修復成功率。
- 專門針對 **Patch Overfitting (補丁過擬合)** 設計了動態語意 PCA 模組。

## 🧠 技術架構 & 運作流程 (Methodology)
1. **RAG 檢索**：當收到一個漏洞報告（CWE）後，從歷史 NVD/CVE 數據庫中檢索相似的漏洞修復 Patch 模板。
2. **Agent 迭代修復**：由 Multi-Agent 系統執行「故障定位 -> 生成 Patch -> 執行專案測試 -> 反饋錯誤訊息 -> 重新生成」。
3. **補丁驗證 (PCA)**：利用動態測試案例增強，在補丁生成後自動生成變異測試，檢測是否引入了過擬合。

## 📊 實驗設計 & 數據集 (Evaluation & Benchmarks)
- **使用的基準資料集**: SWE-bench, CVE-Fix-Bench
- **核心實驗結果**: 在真實 CVE 漏洞修復上達到了 83.13% 的成功率。

## 📝 個人筆記 / 啟發 (Notes & Insights)
- 該論文同時涵蓋了 LLM Agent 修復 (3.5) 與補丁驗證 (3.6) 流派，是現代自動化漏洞防禦的代表工作。

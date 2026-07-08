---
title: "IRIS: LLM-Assisted Static Analysis for Detecting Taint-Style Vulnerabilities"
authors: "Anonymous Authors"
year: 2024
venue: "arXiv"
url: "https://arxiv.org/abs/2400.00000"
code: ""
categories:
  - "[[1.2-資料流分析 (Data Flow Analysis)]]"
  - "[[1.7-學習型靜態分析 (Learning-based Static)]]"
---

# IRIS: LLM-Assisted Static Analysis for Detecting Taint-Style Vulnerabilities

## 💡 核心創新點 (Core Contributions)
- 提出 **LLM + Static Hybrid** 的混合分析模式。
- 利用大語言模型自動推斷 CodeQL 等靜態分析工具所需的 **Taint Specification (Source, Sink, Sanitizer)**，解決了傳統靜態分析工具規格定義成本極高、容易漏報的問題。

## 🧠 技術架構 & 運作流程 (Methodology)
1. **LLM 規格推斷**：先由 LLM 掃描程式碼，識別出可能被當作污點源或接收點的 API / 函式。
2. **靜態驗證**：將 LLM推斷出來的 Spec 轉化成 CodeQL 查詢，交由 CodeQL 引擎執行嚴格的資料流分析，排除 LLM 的幻覺誤報。

## 📊 實驗設計 & 數據集 (Evaluation & Benchmarks)
- **使用的基準資料集**: 實際開源 GitHub 專案。
- **對比的 Baseline**: 傳統純人工編寫 Spec 的 CodeQL 掃描。

## 📝 個人筆記 / 啟發 (Notes & Insights)
- 這篇論文是典型的「神經符號混合（Neuro-symbolic）」靜態分析，完美結合了 LLM 的語意理解與傳統 Static 分析的嚴謹性，對「跨流派」論文歸類是很好的範例。

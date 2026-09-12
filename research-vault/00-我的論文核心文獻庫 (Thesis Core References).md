---
title: "我的論文核心文獻庫 (Thesis Core References)"
type: moc
updated: 2026-09-05
tags:
  - thesis/core
  - moc/references
---

# 🎓 我的論文核心文獻庫 (Thesis Core References)

> [!IMPORTANT]
> **本庫定位**：全景研究流派庫（[[00-研究流派圖主目錄|00-研究流派圖主目錄]]）負責**宏觀視野與背景調研（廣度）**；而本文件則是專門提煉出**最終論文撰寫、實驗直面 PK、模型改進與章節引用（深度）**的黃金候選名單。
> 
> **使用方法**：平時閱覽各流派筆記時，只要遇到「我的論文必須對照或引用」的論文，直接以雙鏈 `[[論文檔名]]` 形式收錄到下方對應分區即可！

---

## 🧭 論文文獻分層架構 (Citation Pyramid)

```
             ┌─────────────────────────┐
             │  Tier 1: 核心實驗對照組  │  10~20 篇 (實驗章節直面 PK 的 SOTA Baselines)
             ├─────────────────────────┤
             │  Tier 2: 理論基石與架構  │  15~25 篇 (支撐 Motivation、威脅模型與核心演算法)
             ├─────────────────────────┤
             │  Tier 3: Related Work   │  30~50 篇 (Chapter 2 相關研究分類代表作)
             └─────────────────────────┘
```

---

## 🏆 Tier 1: 核心實驗對照組 (Direct Baselines to Compare)
*這些論文是你在論文實驗評測章節中，必須在同一實驗環境/數據集下直面比較、跑出 Benchmark 數據的 SOTA 工具：*

- [[Humanoid (2019) Deep Learning-Based Black-box Testing of Android Apps]]
  - **角色**：黑箱動態測試基線 (Deep Learning-based GUI Exploration SOTA)
  - **比較維度**：頁面覆蓋率 (Activity/Widget Coverage)、有效事件序列生成率、崩潰發現速度。
  - **深入詳情**：參見出版級精讀全文與 10 幅高解析圖表解析。
- [[AdbGPT (2024) Prompting Is All You Need Automated Android Bug Replay with Large Language Models]]
  - **角色**：LLM 驅動之 Bug 重現與操作軌跡生成基線
  - **比較維度**：自然語言 Bug Report 理解度、Prompt 工程引導之動態重現成功率。

*(可隨時在此處新增欲比較的 SOTA 論文)*

---

## 🏛️ Tier 2: 理論基石與問題陳述 (Foundational Theory & Problem Formulation)
*支撐你論文核心設計理念、問題定義（Problem Formulation）與威脅模型（Threat Model）的核心文獻：*

- **威脅模型與安全規範定義**：
  - 參見專案核心矩陣：[[Android-DAST-核心檢測矩陣-v14.0|Android DAST 核心檢測矩陣]]（對標 81 篇 2020–2026 前沿頂會論文）
- **動態執行與狀態探索基礎**：
  - [[Android動態測試框架完整研究報告|Android 動態測試框架完整研究報告]]

---

## 📚 Tier 3: 論文第二章相關研究預選清單 (Chapter 2 Related Work Pre-selection)
*用於撰寫 Chapter 2 Related Work，依技術流派分段闡述現有研究之演進、貢獻與其侷限性（Limitations）：*

### 3.1 靜態程式碼分析與污點追蹤 (Static Analysis & Taint Tracking)
- [[1A.1-語法與結構分析 (Syntactic & AST)]] 流派代表作
- [[1B.4-靜態污點分析 (Static Taint Analysis)]] 流派代表作

### 3.2 動態黑箱探索與模糊測試 (Black-box Exploration & Fuzzing)
- [[2A.1-Web與API動態漏洞掃描 (DAST)]]
- [[2B.1-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]

### 3.3 大語言模型與安全自動化 (LLM for Code Security & APR)
- [[3C.1-深度學習修復流派 (DL & NMT)]]
- [[3C.2-LLM與Agent驅動修復 (LLM & Agentic)]]
- [[2A.4-自主滲透測試代理與多Agent攻防編排 (Autonomous Pentest & Multi-Agent Orchestration)]]

---

## 🧪 Tier 4: 公開評測數據集與基準 (Evaluation Benchmarks & CyberGym)
*實驗評測必須採用的標準靶場、歷史漏洞庫或真實應用集合：*

- [[4.1-靜態代碼與大模型安全評測 (Static Code & LLM Security Benchmarks)]]
- [[4.2-動態攻防與CTF實戰靶場 (Dynamic CTF & Exploit Gym)]]
- [[Android安全測試完整工具清單|Android 安全測試完整工具與環境清單]]

---

## 📋 論文寫作與文獻追蹤清單 (Thesis Reading & Citation Tracking)

### 📌 核心對照組 (Baselines)
- [[Humanoid (2019) Deep Learning-Based Black-box Testing of Android Apps]]
  - **預定章節**：Ch 4 / Ch 5 (核心實驗對比)
  - **精讀狀態**：✅ 已精讀 (圖表、公式、模型架構完整)
  - **關鍵啟發**：借鑑其雙層模型 (Action Type + Coordinate) 設計，著手改善其欠缺長期語意記憶與 API 語意理解之瓶頸。

### 📌 相關研究代表 (Related Work)
- [[AdbGPT (2024) Prompting Is All You Need Automated Android Bug Replay with Large Language Models]]
  - **預定章節**：Ch 2 (相關研究) / Ch 5 (消融實驗對比)
  - **精讀狀態**：📖 研讀中
  - **關鍵啟發**：Prompting 策略與多模態截圖結合之可行性，評估其在跨 App 場景之泛化能力。

*(隨時在此直接追加 `[[論文名稱]]`，保持最純淨的論文引用池)*

---

## 🔗 快速跳轉
- 返回 [[00-研究流派圖主目錄|🛡️ 程式碼安全研究流派圖主目錄]]
- 查閱 [[00-多維正交二維座標圖|🌌 多維正交二維座標圖]]
- 查閱 [[PAPERS_METADATA_TABLE|📑 頂會論文全集元數據總表]]

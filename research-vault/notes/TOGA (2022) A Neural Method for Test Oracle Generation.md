---
title: "TOGA: A Neural Method for Test Oracle Generation"
year: 2022
venue: "ICSE 2022 (ACM SIGSOFT Distinguished Paper)"
authors: "Michele Tufano, Dawn Drain, Alexey Svyatkovskiy, Neel Sundaresan"
categories:
  - "[[2B.5-測試預言與斷言合成 (Test Oracle & Assertion Synthesis)]]"
  - "[[1D.1-學習型靜態分析 (Learning-based Static)]]"
---

# TOGA: A Neural Method for Test Oracle Generation

> **文獻類型**：神經測試預言機架構 (Neural Method & Framework)  
> **核心工具**：**TOGA** (Transformer-based Oracle Generation with Assertions and Exceptions)

- **文獻存檔**:
  - [PDF 原文](<../../raw-papers/2022/TOGA (2022) A Neural Method for Test Oracle Generation.pdf>)
  - [Markdown 原文](<../../raw-papers/2022/TOGA (2022) A Neural Method for Test Oracle Generation (Raw).md>)

## 核心貢獻
微軟研究院提出首個結合預訓練模型合成斷言（Assertion）與異常預期（Exception Specification）的神經預言機系統 TOGA。在 EvoSuite 產生的測試用例基礎上合成有效預言機，成功挖掘出 57 個真實缺陷，準確率超越傳統方法 33%。

---
title: "ViaLin: Path-Aware Dynamic Taint Analysis for Android"
year: 2023
venue: "ESEC/FSE 2023"
authors: "Khaled Ahmed, Yingying Wang, Mieszko Lis, Julia Rubin"
categories:
  - "[[2B.2-動態污點分析 (Dynamic Taint Analysis - DTA)]]"
  - "[[1C.1-二進位與逆向分析 (Binary & Reverse Engineering)]]"
---

# ViaLin: Path-Aware Dynamic Taint Analysis for Android

> **文獻類型**：工具與系統論文 (Tool Presentation / Framework)  
> **核心工具**：**ViaLin** (路徑感知之 Android 高效動態污點分析系統)

- **文獻存檔**:
  - [PDF 原文](<../../raw-papers/2023/ViaLin (2023) Path-Aware Dynamic Taint Analysis for Android.pdf>)
  - [Markdown 原文](<../../raw-papers/2023/ViaLin (2023) Path-Aware Dynamic Taint Analysis for Android (Raw).md>)

## 核心貢獻
傳統 Android 動態污點追蹤僅能回報 Source 與 Sink 端點，無法精確還原敏感資訊在記憶體與控制流中的完整傳播路徑。ViaLin 提出了高效的路徑感知追蹤機制，在保持極低運行時開銷的同時，能精準重構端到端的傳播鏈路，有效區分正常數據清洗與隱蔽數據洩漏。

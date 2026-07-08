---
title: "AFLNet: A Greybox Fuzzer for Network Protocols"
authors: "Van-Thuan Pham, et al."
year: 2020
venue: "ICSE 2020"
url: "https://dl.acm.org/doi/10.1145/3377811.3380434"
code: "https://github.com/aflnet/aflnet"
categories:
  - "[[2.2-黑箱協定模糊測試 (Black-box Protocol Fuzzing)]]"
  - "[[2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]"
---

# AFLNet: A Greybox Fuzzer for Network Protocols

## 💡 核心創新點 (Core Contributions)
- 針對網路協定測試，提出了一種將 **Stateful Fuzzing (協定狀態機)** 與 **Greybox Fuzzing (覆蓋率反饋)** 結合的框架。
- AFLNet 不僅依賴程式碼的分支覆蓋率，還會透過網絡回應碼（如 FTP 的 220, 331）來推斷目前的協定狀態，以狀態轉換圖導航變異。

## 🧠 技術架構 & 運作流程 (Methodology)
1. **握手與狀態追蹤**：發送封包給目標伺服器，並收集回應中的狀態碼以構建動態狀態圖。
2. **覆蓋率引導**：利用 AFL 的輕量級代碼插樁，獲得基本塊覆蓋率。
3. **反饋調度**：優先突變那些能觸發新代碼路徑或新協定狀態的訊息序列。

## 📊 實驗設計 & 數據集 (Evaluation & Benchmarks)
- **使用的基準資料集**: 實際的開源網路伺服器 (ProFTPD, Pure-FTPd, Live555)。
- **對比的 Baseline**: 傳統黑箱協定 Fuzzer (Peach Fuzzer) 以及純 CGF。

## 📝 個人筆記 / 啟發 (Notes & Insights)
- 這篇論文是「黑箱協定分析（狀態碼推斷）」與「灰箱引導式測試（覆蓋率）」結合的典範，很好地驗證了我們拆分「黑箱」與「白/灰箱」動態分類的必要性與實用價值。

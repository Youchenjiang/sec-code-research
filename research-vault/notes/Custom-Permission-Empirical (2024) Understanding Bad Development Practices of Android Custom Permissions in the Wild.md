---
title: "Understanding the Bad Development Practices of Android Custom Permissions in the Wild"
year: 2024
venue: "MSR"
authors: "Xiaohan Zhang, Zhiyuan Yu, Xinghua Li, Cen Zhang, Cong Sun, Ning Zhang, Robert H. Deng"
categories:
- '[[1B.4-靜態污點分析 (Static Taint Analysis)]]'
- '[[1B.3-符號執行 (Symbolic Execution)]]'
---

# Understanding the Bad Development Practices of Android Custom Permissions in the Wild (2024)

> **發表會/期刊**：MSR (2024)  
> **作者**：Xiaohan Zhang, Zhiyuan Yu, Xinghua Li, Cen Zhang, Cong Sun, Ning Zhang, Robert H. Deng  
> **研究流派**：[[1B.4-靜態污點分析 (Static Taint Analysis)]] [[1B.3-符號執行 (Symbolic Execution)]]  
> **核心貢獻**：針對 Android 自定義權限 (Custom Permissions) 的不良開發模式 (BPCP) 進行首度大規模野外調查。歸納 9 種常見缺陷模式（易導致組件劫持、安裝失敗或應用崩潰），開發靜態分析工具 PERMEAGRE 分析 83,085 款應用，揭示逾 26% 應用包含此類安全隱患。  
> **文獻存檔**：[PDF 原文](<../../raw-papers/2024/Custom-Permission-Empirical (2024) Understanding Bad Development Practices of Android Custom Permissions in the Wild.pdf>) | [Markdown 原文](<../../raw-papers/2024/Custom-Permission-Empirical (2024) Understanding Bad Development Practices of Android Custom Permissions in the Wild (Raw).md>)

---

## 📌 論文核心精要 (Executive Summary)
針對 Android 自定義權限 (Custom Permissions) 的不良開發模式 (BPCP) 進行首度大規模野外調查。歸納 9 種常見缺陷模式（易導致組件劫持、安裝失敗或應用崩潰），開發靜態分析工具 PERMEAGRE 分析 83,085 款應用，揭示逾 26% 應用包含此類安全隱患。

---

## 🔍 方法論與技術亮點 (Methodology Highlights)
- **正式標題**：Understanding the Bad Development Practices of Android Custom Permissions in the Wild
- **完整收錄與圖表**：已使用版面感知雙欄引擎將正版 PDF 轉換為 Markdown 全文，圖表已獨立抽取至關聯資產目錄。
- **全文參閱**：請由上方文獻存檔雙鏈跳轉至完整雙欄 Markdown 原文查閱。

---
返回 [[00-研究流派圖主目錄|研究流派圖主目錄]]

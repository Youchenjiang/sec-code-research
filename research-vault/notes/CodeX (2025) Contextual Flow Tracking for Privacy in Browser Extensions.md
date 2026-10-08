---
title: "Contextual Flow Tracking for Privacy in Browser Extensions"
authors: "Mohammad M. Ahmadpanah, Matías F. Gobbi, Daniel Hedin, Johannes Kinder, Andrei Sabelfeld"
year: 2025
venue: "ACM CODASPY 2025 (15th ACM Conference on Data and Application Security and Privacy)"
url: "https://doi.org/10.1145/3708821.3710776"
code: ""
categories:
  - "[[1-靜態分析 (Static Analysis)]]"
  - "[[0-設計安全與威脅分析 (Secure Design & Threat Analysis)]]"
---

# 📖 Contextual Flow Tracking for Privacy in Browser Extensions (CodeX, CODASPY 2025)

## 📄 本地專題關聯
- **所屬矩陣專題**：`[B.3 宣告式圖查詢與形式化策略求解]`, `[A.5 跨程序拓撲與全域風險矩陣]`
- **關聯檢索指南**：[Y2_擴展文獻全景檢索指南.md](../../proposals/logic-vuln-lifecycle/Y2-root-cause-localization/Y2_擴展文獻全景檢索指南.md)

---

## 📝 論文摘要 (Abstract)
> Browser extensions hold privileged access to sensitive user data, making them prime vectors for privacy violations and unauthorized data exfiltration. Traditional static taint analysis often proves too rigid or conservative when analyzing complex JavaScript flows, missing nuanced violations. This paper introduces **CodeX**, a static analysis framework built on **CodeQL** designed for contextual flow tracking. By modeling fine-grained browser APIs and relaxing conservative constraints around contextual data flows, CodeX precisely tracks sensitive resources (cookies, history, search queries) to suspicious network sinks. Applying CodeX to thousands of Chrome extensions discovered 212 confirmed privacy-violating extensions impacting millions of active users.

---

## 🎯 核心解決問題 (Problem Statement)
* **研究背景**：現代外掛與微服務中，資料流非常複雜且具有高度上下文相關性（Context-sensitive），傳統靜態污點分析（Static Taint Analysis）常因過度保守而遺漏真實資料外洩。
* **現有技術痛點**：主流查詢引擎（如原生 CodeQL）對於外部庫與特定上下文 API 的模型不完整，難以捕捉非傳統污點模式的越權存取。
* **論文切入點**：**以 CodeQL 建立擴展的上下文敏感追蹤引擎**——客製化宣告式查詢規則，精確捕捉敏感實體與未授權出口之間的流向。

---

## 💡 關鍵創新點與貢獻 (Key Contributions)
1. **宣告式分析框架突破**：展示了如何基於 CodeQL 構建高效且低偽陰性的全域上下文敏感分析工具。
2. **大規模工業界實測成效**：掃描數千款真實擴充套件，證實了宣告式查詢在全專案拓撲分析中的強大檢測力。

---

## 🧠 對第二年（Y2 侑宸）的借鑑與超越

1. **直接指導 Y2「宣告式圖查詢（B.3）」的實作路徑**：
   * CodeX 證明了**將複雜的安全約束轉譯為 CodeQL 查詢**，是進行全專案反向追蹤（Backward Reachability）與建立全域風險矩陣的最高效手段。
2. **Y2 的專屬特徵與超越**：
   * **CodeX 是靜態規則撰寫**：需要分析師手工設計 CodeQL 污點模型。
   * **Y2 實現自適應生成**：Y2 由 LLM 從 Y1 動態 Exploit 軌跡中反推不變量後，自動將該約束編譯為後端特定的查詢規則，全自動掃描其他共享進入點。

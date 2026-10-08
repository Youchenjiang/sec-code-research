---
title: "Toward Automated Detection of Logic Vulnerabilities in Web Applications"
authors: "Viktoria Felmetsger, Ludovico Cova, Christopher Kruegel, Giovanni Vigna"
year: 2010
venue: "USENIX Security 2010 (19th USENIX Security Symposium)"
url: "https://www.usenix.org/legacy/event/sec10/tech/full_papers/Felmetsger.pdf"
code: ""
categories:
  - "[[1-靜態分析 (Static Analysis)]]"
  - "[[2-動態分析 (Dynamic Analysis)]]"
  - "[[0-設計安全與威脅分析 (Secure Design & Threat Analysis)]]"
---

# 📖 Toward Automated Detection of Logic Vulnerabilities in Web Applications (Waler, USENIX Security 2010)

## 📄 本地專題關聯
- **所屬矩陣專題**：`[A.2 安全不變量與規格挖掘]`, `[B.1 差分與對比執行分析]`
- **關聯檢索指南**：[Y2_擴展文獻全景檢索指南.md](../../proposals/logic-vuln-lifecycle/Y2-root-cause-localization/Y2_擴展文獻全景檢索指南.md)

---

## 📝 論文摘要 (Abstract)
> Web application vulnerabilities are typically associated with input validation flaws like SQL injection or cross-site scripting. However, logic vulnerabilities—flaws in the application's unique business logic and behavioral workflows—pose an equally dangerous threat and cannot be detected by conventional signature-based tools. This paper introduces **Waler**, an automated approach for analyzing web applications for logic vulnerabilities. Waler uses dynamic analysis to observe normal executions, infers likely behavioral invariants and state transition specifications, and then applies symbolic model checking to explore program paths that violate these inferred invariants. Evaluated on real-world e-commerce and open-source web applications, Waler successfully identified critical logic flaws allowing unauthorized order manipulations and workflow bypasses.

---

## 🎯 核心解決問題 (Problem Statement)
* **研究背景**：傳統掃描器只能找 SQLi/XSS 等輸入語法缺陷，對於「跳過購物車結帳流程」、「以他人帳號直接取消訂單」等業務邏輯缺陷完全無能為力。
* **現有技術痛點**：業務邏輯沒有現成的安全性質（Security Properties）或規範文檔（Specifications），分析工具不知道系統應該遵守什麼商業規則。
* **論文切入點**：**「動態推導不變量 ＋ 符號模型檢驗」**——透過讓正常使用者操作系統，自動挖掘潛在不變量（Likely Invariants），再檢查是否有任何程式路徑可以打破該不變量。

---

## 💡 關鍵創新點與貢獻 (Key Contributions)
1. **業務邏輯漏洞形式化先驅**：安全領域首篇系統性將業務邏輯漏洞定義為「程式碼路徑違反狀態機/業務不變量」的經典頂會著作。
2. **規格挖掘與模型檢驗結合**：展示了「動態觀察學習正常行為 $\to$ 靜態符號檢驗尋找越界路徑」的混合分析範式。

---

## 🧠 對第二年（Y2 侑宸）的借鑑與超越

1. **奠定 Y2 不變量形式化的歷史基石**：
   * Waler 證實了「先導出 Invariant，再抓違規路徑」是攻破邏輯漏洞的正確路徑。
2. **Y2 的現代超越**：
   * **Waler 的局限**：2010 年代依賴傳統的狀態機與枚舉，狀態爆炸問題嚴重，且對複雜的 modern API（如 REST/JSON）難以適配。
   * **Y2 的革新**：利用 LLM 語意推理與動態 Exploit 軌跡，將不變量推導直接提升到「領域主體與資源約束（$(D,A,R,P,SC)$）」，並支援現代微服務與多階層 Controller/Service 呼叫。

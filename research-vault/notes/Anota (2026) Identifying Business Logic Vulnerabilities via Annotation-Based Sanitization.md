---
title: "Anota: Identifying Business Logic Vulnerabilities via Annotation-Based Sanitization"
authors: "Meng Wang, Philipp Görz, Joschua Schilling, Keno Hassler, Liwei Guo, Thorsten Holz, Ali Abbasi"
year: 2026
venue: "NDSS 2026 (Network and Distributed System Security Symposium)"
url: "https://dx.doi.org/10.14722/ndss.2026.240938"
code: ""
categories:
  - "[[2-動態分析 (Dynamic Analysis)]]"
  - "[[4-安全基準評測、數據集與靶場 (Benchmarks, Datasets & CyberGym)]]"
  - "[[0-設計安全與威脅分析 (Secure Design & Threat Analysis)]]"
---

# 📖 Anota: Identifying Business Logic Vulnerabilities via Annotation-Based Sanitization (NDSS 2026)

## 📄 文獻存檔與關聯專題
- **PDF 原文**：[code-security-research/2026-f938-paper.pdf](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/2026-f938-paper.pdf)
- **技術解讀專題**：[ANOTA_論文核心技術解讀.md](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/proposals/logic-vuln-lifecycle/Y2-root-cause-localization/ANOTA_論文核心技術解讀.md)
- **專案借鑑分析**：[ANOTA_論文價值與參考借鑑.md](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/proposals/logic-vuln-lifecycle/Y2-root-cause-localization/ANOTA_論文價值與參考借鑑.md)
- **對標局限與創新**：[ANOTA_對標局限與Y2核心創新點.md](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/proposals/logic-vuln-lifecycle/Y2-root-cause-localization/ANOTA_對標局限與Y2核心創新點.md)

---

## 📝 論文摘要 (Abstract)
> Fuzzing is widely used to discover software vulnerabilities, but relies critically on sanitizers to report violations when inputs trigger vulnerable states. While sanitizers excel at finding memory-safety flaws, business logic vulnerabilities (e.g., authorization, privilege escalation) remain largely unaddressed because correct behavior is domain-specific and lacks universal crash oracles. This paper introduces **ANOTA**, a human-in-the-loop sanitizer framework adhering to the classic principle of separating policy from mechanism. ANOTA provides a lightweight annotation system allowing developers to encode intended security invariants across system calls, data flows, object accesses, and code executions. A language-agnostic runtime policy monitor enforces these policies, reporting violations to the fuzzer as crashes. Evaluated on real-world systems, ANOTA+FUZZER successfully reproduced 43 known vulnerabilities and discovered 22 previously unknown vulnerabilities (assigned 17 CVEs).

---

## 🎯 核心解決問題 (Problem Statement)
* **研究背景**：在 Web 與微服務架構中，CWE Top 40 中的授權（CWE-862/863）與認證（CWE-287/269）等業務邏輯漏洞日益猖獗。
* **現有技術痛點**：動態 Fuzzing 缺乏針對業務邏輯的 Crash Oracle；既有自動啟發式規則面對複雜應用上下文極度脆弱且誤報率高。
* **論文切入點**：由人類專家撰寫輕量化程式註解（Policy），由執行期監控器（Mechanism）強制執行並將違規轉化為 Fuzzer 崩潰信號。

---

## 💡 關鍵創新點與貢獻 (Key Contributions)
1. **業務邏輯 Sanitizer 框架**：首創將 Sanitizer 機制引進業務邏輯漏洞 Fuzzing 領域。
2. **四大異常行為註解語法（Table II）**：涵蓋 System Call、Data Flow (`TAINT`)、Object Access (`WATCH`)、Code Execution (`EXECUTION.BLOCK`)。
3. **出色的實戰攻防成果**：重現 43 個已知 CVE，發掘 22 個真實 0-day 漏洞並獲得 17 個新 CVE。

---

## 🧠 對 Y2 計畫之對照索引
本論文為三年期計畫之第二年（Y2 業務邏輯漏洞根因定位）提供了關鍵的**反方對標與動機背書**（Anota 坦承依賴人工標註，留待未來利用 LLM 實現自動化）：
* [Y2 根因定位總目錄](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/proposals/logic-vuln-lifecycle/Y2-root-cause-localization/README.md)

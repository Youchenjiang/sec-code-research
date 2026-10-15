---
title: "Anota: Identifying Business Logic Vulnerabilities via Annotation-Based Sanitization"
authors: "Meng Wang, Philipp Görz, Joschua Schilling, Keno Hassler, Liwei Guo, Thorsten Holz, Ali Abbasi"
year: 2026
venue: "NDSS 2026 (Network and Distributed System Security Symposium)"
url: "https://dx.doi.org/10.14722/ndss.2026.240938"
code: "https://github.com/ANOTA-Sanitizer/ANOTA"
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
*（以下為摘要意譯，非原文逐字引用）*
> Fuzzing is widely used to discover software vulnerabilities, but relies critically on sanitizers to report violations when inputs trigger vulnerable states. While sanitizers excel at finding memory-safety flaws, business logic vulnerabilities (e.g., authorization, privilege escalation) remain largely unaddressed because correct behavior is domain-specific and lacks universal crash oracles. This paper introduces **ANOTA**, a human-in-the-loop sanitizer framework adhering to the classic principle of separating policy from mechanism. ANOTA provides a lightweight annotation system allowing developers to encode intended security invariants across system calls, data flows, object accesses, and code executions. A language-agnostic runtime policy monitor enforces these policies, reporting violations to the fuzzer as crashes. Evaluated on real-world systems, ANOTA+FUZZER successfully reproduced 43 known vulnerabilities and discovered 22 previously unknown vulnerabilities (assigned 17 CVEs).

---

## 🎯 核心解決問題 (Problem Statement)
* **研究背景**：在 Web 與微服務架構中，CWE Top 40 中的授權（CWE-862/863）與認證（CWE-287/269）等業務邏輯漏洞日益猖獗。
* **現有技術痛點**：動態 Fuzzing 缺乏針對業務邏輯的 Crash Oracle；既有自動啟發式規則面對複雜應用上下文極度脆弱且誤報率高。
* **論文切入點**：由人類專家撰寫輕量化程式註解（Policy），由執行期監控器（Mechanism）強制執行並將違規轉化為 Fuzzer 崩潰信號。

---

## 💡 關鍵創新點與貢獻 (Key Contributions)
1. **通用的註解式業務邏輯 Sanitizer 框架**：先前已有針對個別漏洞類型的 oracle（如 Atropos、SSRFuzz、EDEFuzz），ANOTA 的新意在於以「政策與機制分離」提供**可由使用者擴充的通用註解框架**，而非又一個特定類型的啟發式。
2. **四大異常行為註解語法（Table II）**：涵蓋 System Call (`SYSCALL`)、Data Flow (`TAINT`)、Object Access (`WATCH`)、Code Execution (`EXECUTION.BLOCK`)，另有 `CLEAR` 可在執行期移除政策。
3. **實戰成果**：重現 43/47 個已知漏洞（Snyk 來源，部分為 SNYK ID 而非 CVE），發掘 22 個 0-day 並獲得 17 個 CVE。原型**僅支援 Python**，fuzzer 為 Atheris。
4. **類型分布提醒**：成果以 System Call（SSRF、path traversal、上傳、code injection）與 Data Flow（log 洩漏、TOCTOU）為主；22 個 0-day 中授權類（Object Access）僅 1 個、Code Execution 0 個。作者在 V-D1 也承認存取控制類並非 ANOTA 的理想標的。

---

## 🧠 對 Y2 計畫之對照索引
本論文為三年期計畫之第二年（Y2 業務邏輯漏洞根因定位）提供了關鍵的**反方對標與動機背書**（Anota 在 Section VI.C 坦承依賴人工標註，留待未來利用 LLM 實現自動化）：
* [Y2 根因定位總目錄](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/proposals/logic-vuln-lifecycle/Y2-root-cause-localization/README.md)

---
title: "Fixing Logic Vulnerabilities via LLM-Driven Specification Mining and Repair"
authors: "Yikun Li, Zhenhao Li, Jie Zhang, Zhe Xie, David Lo, Yang Liu, Jianhai Chen"
year: 2026
venue: "ICSE 2026 (ACM/IEEE International Conference on Software Engineering)"
url: "https://doi.org/10.1145/3744916.3773260"
code: "https://github.com/intentfix-icse2026/intentfix"
categories:
  - "[[3-自動修復 (Automated Program Repair - APR)]]"
  - "[[1-靜態分析 (Static Analysis)]]"
  - "[[4-安全基準評測、數據集與靶場 (Benchmarks, Datasets & CyberGym)]]"
---

# 📖 Fixing Logic Vulnerabilities via LLM-Driven Specification Mining and Repair (INTENTFIX, ICSE 2026)

## 📄 文獻存檔與關聯專題
- **PDF 原文**：[code-security-research/3744916.3773260.pdf](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/3744916.3773260.pdf)
- **技術解讀專題**：[INTENTFIX_論文核心技術解讀.md](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/proposals/logic-vuln-lifecycle/Y2-root-cause-localization/INTENTFIX_論文核心技術解讀.md)
- **專案借鑑分析**：[INTENTFIX_論文價值與參考借鑑.md](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/proposals/logic-vuln-lifecycle/Y2-root-cause-localization/INTENTFIX_論文價值與參考借鑑.md)
- **對標局限與創新**：[INTENTFIX_對標局限與Y2核心創新點.md](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/proposals/logic-vuln-lifecycle/Y2-root-cause-localization/INTENTFIX_對標局限與Y2核心創新點.md)

---

## 📝 論文摘要 (Abstract)
> Logic vulnerabilities are subtle flaws resulting from deviations between intended system specifications and actual program implementations. Unlike memory or injection bugs, logic vulnerabilities rarely crash programs or violate syntactic rules, making them notoriously difficult to detect and repair using traditional static analysis or testing. This paper presents **INTENTFIX**, an automated framework that leverages Large Language Models (LLMs) to mine implicit specifications from source code and guide vulnerability auditing and repair. INTENTFIX models developer intent using a 5-tuple specification model $(D, A, R, P, SC)$, audits semantic gaps against target code, and synthesizes intent-consistent patches. Evaluated on a curated benchmark of 1,107 real-world logic vulnerability CVEs across 879 open-source repositories, INTENTFIX achieves superior auditing precision and repair effectiveness compared to existing baselines.

---

## 🎯 核心解決問題 (Problem Statement)
* **研究背景**：業務邏輯漏洞（如 BOLA/IDOR、越權、業務流程繞過）頻繁出現在現代微服務與行動端後端，造成嚴重資料洩漏與財務損失。
* **現有技術痛點**：
  1. 傳統 SAST / DAST 仰賴語法特徵或崩潰日誌（Crash Oracle），缺乏業務意圖（Specification）難以識別合法語法背後的邏輯缺陷。
  2. 現有 APR（自動程式修復）以單元測試為 Oracle，但邏輯漏洞發生時既有測試通常全數 Pass（缺乏安全斷言）。
* **論文切入點**：以 LLM 充當「意圖挖掘引擎」，將隱含於命名、註釋、程式邏輯中的安全意圖抽取為五元組 $(D, A, R, P, SC)$，以此為規範導引修復。

---

## 💡 關鍵創新點與貢獻 (Key Contributions)
1. **意圖形式化模型 $(D, A, R, P, SC)$**：定義 Domain、Actor、Resource、Privilege、Security Constraint 五元組，結構化引導 LLM 推理。
2. **三階段自動化管道**：
   - 階段 1：**Specification Mining**（規格挖掘）
   - 階段 2：**Vulnerability Auditing**（語意落差識別與概念攻擊向量生成）
   - 階段 3：**Intent-Guided Repair**（意圖增強提示詞合成修復補丁）
3. **首個大規模邏輯漏洞基準庫**：開源 1,107 個跨 10 年（2014-2024）的真實 CVE 邏輯漏洞數據集。

---

## 📊 實驗基準與結果
* **數據規模**：1,107 個 CVE（涵蓋 CWE-639 BOLA、CWE-284 存取控制失效、CWE-862 缺失授權等）。
* **審計準確性**：Operation（85%）與 Constraint（72%）具有高精確度，Actor（60%）因缺乏動態執行資訊受限。
* **修復成效**：在修復正確性與語意一致性上顯著超越 Zero-Shot LLM 與傳統 APR 工具。

---

## 🧠 對 Y2 計畫之對照索引
本論文為三年期計畫之第二年（Y2 業務邏輯漏洞根因定位）提供了極佳的學術對標物。詳細的三部曲分析請參見：
* [Y2 根因定位總目錄](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/proposals/logic-vuln-lifecycle/Y2-root-cause-localization/README.md)

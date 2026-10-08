---
title: "CVEfixes: Automated Collection of Vulnerabilities and Their Fixes from Open-Source Software"
authors: "Guru Bhandari, Amara Naseer, Leon Moonen"
year: 2021
venue: "PROMISE 2021 (17th International Conference on Predictive Models and Data Analytics in Software Engineering / Widely adopted in MSR & ICSE)"
url: "https://doi.org/10.1145/3475960.3475985"
code: "https://github.com/secureIT-project/CVEfixes"
categories:
  - "[[4-安全基準評測、數據集與靶場 (Benchmarks, Datasets & CyberGym)]]"
  - "[[3-自動修復 (Automated Program Repair - APR)]]"
---

# 📖 CVEfixes: Automated Collection of Vulnerabilities and Their Fixes from Open-Source Software (PROMISE 2021 / MSR 基準庫)

## 📄 本地專題關聯
- **所屬矩陣專題**：`[C.2 漏洞根因評測基準與方法學]`, `[A.3 語意錯誤定位與失效判定]`
- **關聯檢索指南**：[Y2_擴展文獻全景檢索指南.md](../../proposals/logic-vuln-lifecycle/Y2-root-cause-localization/Y2_擴展文獻全景檢索指南.md)

---

## 📝 論文摘要 (Abstract)
> Empirical research in software security critically requires comprehensive, verifiable datasets connecting vulnerabilities to their exact code fixes. This paper presents **CVEfixes**, an open-source dataset and automated data collection pipeline fetching records from the National Vulnerability Database (NVD) and linking them to corresponding vulnerability-fixing commits across open-source repositories. CVEfixes provides multi-level relational abstraction covering CVE, repository, commit, file, and method levels across multiple languages, establishing a gold-standard ground truth for vulnerability detection, fault localization, and automated program repair research.

---

## 🎯 核心解決問題 (Problem Statement)
* **研究背景**：軟體安全研究長期缺乏高質量、與真實世界 Commit 對齊的基準數據集，許多工具只能在人工合成的小型靶場上評測。
* **現有技術痛點**：NVD 雖然記載了 CVE 描述與 CWE 弱點類別，但未提供結構化的 Git Diff、修復前後函式級別對比。
* **論文切入點**：**多粒度自動化數據收集管線**——建立包含 Commit、檔案、函式三層架構的真實修復關聯資料庫。

---

## 💡 關鍵創新點與貢獻 (Key Contributions)
1. **多粒度抽象（Multi-Level Abstraction）**：資料庫完整記錄了 Method Before/After 與 Diff Hunks，極其適合用於「錯誤定位（Fault Localization）」與「修復合成（Repair Synthesis）」。
2. **學界廣泛認可的 Ground Truth**：成為近年 MSR、ICSE、ASE、CCS 研究中訓練與評估安全性模型的通用基礎庫。

---

## 🧠 對第二年（Y2 侑宸）的借鑑與超越

1. **直接作為 Y2 實證評估 RQ1 的 Ground Truth 來源**：
   * Y2 在評估 RQ1（根因診斷是否與官方開發者修復對齊）時，可直接從 CVEFixes 中抽樣 Web/API 邏輯漏洞，以官方修復 Commit 的前置條件（If-condition Diff）作為**客觀標準答案（Ground Truth）**，大幅提升論文實驗的說服力。

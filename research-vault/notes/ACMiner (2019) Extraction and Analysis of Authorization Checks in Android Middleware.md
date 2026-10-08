---
title: "ACMiner: Extraction and Analysis of Authorization Checks in Android Middleware"
authors: "Sigmund Albert Gorski III, Benjamin Andow, Adwait Nadkarni, Sunil Manandhar, William Enck, Eric Bodden, Alexandre Bartel"
year: 2019
venue: "ACM CODASPY 2019 (9th ACM Conference on Data and Application Security and Privacy)"
url: "https://doi.org/10.1145/3292006.3300033"
code: "https://github.com/Android-ACMiner/ACMiner"
categories:
  - "[[1-靜態分析 (Static Analysis)]]"
  - "[[0-設計安全與威脅分析 (Secure Design & Threat Analysis)]]"
---

# 📖 ACMiner: Extraction and Analysis of Authorization Checks in Android Middleware (CODASPY 2019)

## 📄 本地專題關聯
- **所屬矩陣專題**：`[A.2 安全不變量與規格挖掘]`, `[A.5 跨程序拓撲與全域風險矩陣]`
- **關聯檢索指南**：[Y2_擴展文獻全景檢索指南.md](../../proposals/logic-vuln-lifecycle/Y2-root-cause-localization/Y2_擴展文獻全景檢索指南.md)

---

## 📝 論文摘要 (Abstract)
> The Android middleware framework enforces security via hard-coded authorization checks distributed throughout its system services. However, inconsistencies in how these checks are placed can introduce vulnerabilities that allow malicious apps to bypass security controls. This paper presents **ACMiner**, a program analysis framework that systematically evaluates authorization check placement. ACMiner combines static program analysis and natural language processing to extract authorization checks from the Android Open Source Project (AOSP), mines authorization policies using association rule mining, and detects vulnerabilities arising from missing authorization checks. Applied to AOSP 7.1.1, ACMiner uncovered 28 previously unknown vulnerabilities, confirmed and patched by Google.

---

## 🎯 核心解決問題 (Problem Statement)
* **研究背景**：大型軟體中權限檢查通常是「硬寫（Hard-coded）」在程式碼各處的條件判斷，缺乏集中式的策略文檔。
* **現有技術痛點**：人工無法檢查數十萬行代碼中成百上千個服務 API 是否全都正確加鎖。
* **論文切入點**：**「自動抽取檢查語句 ＋ 關聯規則挖掘策略」**——如果 90% 呼叫 `deleteUser()` 的進入點都需要 `MANAGE_USERS` 權限，則未加此權限的進入點即存在 Missing Authorization！

---

## 💡 關鍵創新點與貢獻 (Key Contributions)
1. **授權檢查自動辨識**：克服了呼叫圖建構與權限判斷語句自動提取的靜態分析難題。
2. **關聯規則策略挖掘**：以資料探勘演算法（Association Rule Mining）推導出未記載的隱含安全策略。

---

## 🧠 對第二年（Y2 侑宸）的借鑑與超越

1. **直接借鑑於 Y2 的「全域函式路徑風險矩陣（Risk Matrix）」**：
   * ACMiner 示範了如何利用關聯分析在全專案中尋找「授權不一致性（Inconsistent Authorization）」。
2. **Y2 的專屬特徵與超越**：
   * **ACMiner 是靜態關聯規則**：在面對動態傳參、複雜業務多條件時容易失真。
   * **Y2 引入動態事實與 LLM 語意推理**：以動態 Exploit Trace 為起點，結合語意推理補足關聯規則無法表達的複雜業務約束 $(D,A,R,P,SC)$。

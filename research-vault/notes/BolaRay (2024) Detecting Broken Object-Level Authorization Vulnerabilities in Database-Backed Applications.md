---
title: "Detecting Broken Object-Level Authorization Vulnerabilities in Database-Backed Applications"
authors: "Yongheng Huang, Chenghang Shi, Jie Lu, Haofeng Li, Haining Meng, Lian Li"
year: 2024
venue: "ACM CCS 2024 (ACM SIGSAC Conference on Computer and Communications Security)"
url: "https://doi.org/10.1145/3658644.3690227"
code: "https://zenodo.org/records/13840742"
categories:
  - "[[1-靜態分析 (Static Analysis)]]"
  - "[[0-設計安全與威脅分析 (Secure Design & Threat Analysis)]]"
  - "[[4-安全基準評測、數據集與靶場 (Benchmarks, Datasets & CyberGym)]]"
---

# 📖 Detecting Broken Object-Level Authorization Vulnerabilities in Database-Backed Applications (BolaRay, ACM CCS 2024)

## 📄 本地專題關聯
- **所屬矩陣專題**：`[C.1 現代 API、微服務與授權模型]`, `[A.2 安全不變量與規格挖掘]`, `[A.3 語意錯誤定位與失效判定]`
- **關聯檢索指南**：[Y2_擴展文獻全景檢索指南.md](../../proposals/logic-vuln-lifecycle/Y2-root-cause-localization/Y2_擴展文獻全景檢索指南.md)

---

## 📝 論文摘要 (Abstract)
> Broken Object-Level Authorization (BOLA), also known as Insecure Direct Object Reference (IDOR), is a prevalent and severe security vulnerability where applications fail to properly validate whether a user has permission to access a requested object. In database-backed applications, authorization checks are inherently tied to database queries and relational schemas. This paper presents **BolaRay**, an automated framework for detecting BOLA vulnerabilities in database-backed applications. By combining SQL query analysis and static code analysis, BolaRay infers object-level authorization models across diverse architectural patterns and verifies whether existing implementations correctly enforce these models. Evaluated across 25 popular open-source database-backed applications, BolaRay discovered 193 real-world vulnerabilities (with 178 previously unreported), demonstrating superior detection effectiveness and practical applicability.

---

## 🎯 核心解決問題 (Problem Statement)
* **研究背景**：BOLA / IDOR 連年蟬聯 OWASP API Security Top 10 第一名，但其授權規則深植於資料庫物件歸屬（如 `user_id` 與 `order_id` 的外鍵關聯），傳統工具無法理解資料庫綱要（Schema）背後的語意約束。
* **現有技術痛點**：
  1. 純黑箱掃描器無法得知後端資料庫物件的所屬關係模型，難以生成具備語意正確性的合法/越權比對請求。
  2. 傳統 SAST 缺乏 SQL 資料流與 ORM 映射感知，無法判斷查出來的資料是否有在業務層進行過濾。
* **論文切入點**：從**「SQL 查詢模式 ＋ 靜態程式碼資料流」**中，自動反推四類物件層級授權模型（Object-Level Authorization Models），並檢查程式實作是否遺漏檢查。

---

## 💡 關鍵創新點與貢獻 (Key Contributions)
1. **實證研究（Empirical Study）**：系統化分析 101 個真實世界 BOLA 漏洞，歸納出資料庫支援應用中最常見的 4 大授權模式。
2. **SQL 與靜態分析協同推導（BolaRay）**：透過解析 ORM / SQL 查詢中的 `WHERE` 條件與關聯表結構，自動逆向出「哪些物件屬於哪類角色/使用者」的不變量規則。
3. **豐碩的零日漏洞實戰戰果**：在 25 個主流真實專案中檢出 193 個 BOLA 漏洞，其中 178 個為全新 0-day。

---

## 🧠 對第二年（Y2 侑宸）的借鑑與超越

1. **對 Y2 不變量形式化定義的支撐**：
   * BolaRay 證明了在現代後端應用中，業務不變量（Invariant）絕大部分落在**「前端傳入參數與後端資料庫外鍵關聯（Foreign Key / Owner ID）的約束比對」**。這為 Y2 的 Predicate 定義提供了最權威的落地依據。
2. **Y2 的超越維度（Contrast & Novelty）**：
   * **BolaRay 是純靜態推測**：仰賴靜態分析 SQL 模式，在面對動態組裝查詢或複雜微服務呼叫時仍有 21.86% 偽陽性。
   * **Y2 引入動態事實錨點**：Y2 接收 Y1 的真實動態 Exploit 軌跡，能精確確認該路徑已被攻擊打穿，進而結合 BolaRay 的資料庫語意進行無偽陽性的因果根因定位。

# MocGuard: Automatically Detecting Missing-Owner-Check Vulnerabilities in Java Web Applications

> **論文基本資訊**
> - **論文標題**：MocGuard: Automatically Detecting Missing-Owner-Check Vulnerabilities in Java Web Applications
> - **作者陣容**：Fengyu Liu, Youkun Shi, Yuan Zhang, Guangliang Yang, Enhao Li, Min Yang (Fudan University)
> - **發表頂會**：IEEE Symposium on Security and Privacy (S&P 2025, 46th)
> - **發表年份**：2025
> - **頁碼與 DOI**：pp. 903-919, DOI: 10.1109/SP61157.2025.00010
> - **研究標籤**：`#BOLA` `#IDOR` `#MissingOwnerCheck` `#JavaWeb` `#StaticAnalysis` `#IEEE-SP`

---

## 一、論文核心研究問題與痛點

1. **背景**：
   - 越權漏洞（IDOR / BOLA，CWE-639）是 Web 應用與 API 最普遍且致命的邏輯弱點。其根本原因通常是後端程式碼缺少對「資料記錄擁有者」的檢查，即 **Missing-Owner-Check (MOC)**。
2. **傳統靜態分析工具的致命局限**：
   - 既有的污點分析（如 CodeQL、Semgrep）或粗粒度檢查規則，無法精確判斷「哪一張資料表或哪一個欄位屬於當前登入使用者」，導致極高假陰性（漏報）或巨量假陽性。
   - 傳統分析大多只看 Controller 層的 HTTP 參數，忽略了資料庫存取層（SQL / ORM）真實落地的資料歸屬關係。

---

## 二、核心技術方法：以資料庫為中心（Database-Centric）的跨層分析

MocGuard 提出了以資料庫為中心的雙層關聯推導技術：

```
[HTTP Request / Controller]
        │
        ▼ (Missing Check Gap 🚨)
[Service / DAO Layer]
        │
        ▼ (SQL Query with Entity ID)
[Database Layer (User Tables & Ownership Columns)]
```

1. **資料庫結構與擁有權推導（Database Structure Analysis）**：
   - 自動分析關聯式資料庫的 Schema 與外鍵關係，自動推導哪些表格儲存「使用者實體（User Tables）」，哪些外鍵欄位代表「資料擁有權（User-owned Data）」。
2. **跨 Java 與 SQL 雙層的存取檢查（Insecure Access Checks）**：
   - 將 Controller/Service 處的身份認證上下文（`current_user_id`）與底層 MyBatis / Hibernate / JDBC 執行的 SQL 查詢條件進行比對。
   - 若 SQL 查詢僅以外部傳入的 `id` 作為 `WHERE` 條件，而沒有綁定當前 Session 的使用者識別符，且中間 Java 呼叫路徑上沒有任何檢查邏輯，即判定存在 **Missing-Owner-Check**。
3. **實證成效**：
   - 在 30 個大型開源 Java Web 應用與 7 個工業級 Java Web 系統上完成評測，成功挖掘大量高危 0-day 越權漏洞。

---

## 三、對 Y2（侑宸：根因分析與路徑風險矩陣）的直接借鑑

1. **直接替換傳統 Linux Kernel 分析模型**：
   - 先前文獻多借鑑 Linux Kernel（如 PeX）的跨程序分析，但 Kernel 與 Web 架構差異極大。**MocGuard 為 Y2 提供了純血 Java Web 的分析正規範例**。
2. **跨層語意對齊（Controller $\leftrightarrow$ ORM/SQL）**：
   - Y2 的演算法可以直接採用 MocGuard 的「資料庫實體擁有權矩陣」作為 Ground Truth 字典，當 PoC 攻擊封包跳過了 Controller 驗證時，演算法能沿著呼叫鏈一路追蹤到 SQL Sink，證實該存取缺乏實體約束。
3. **對標基線（Baseline）**：
   - MocGuard 是 IEEE S&P 2025 最新的頂級成果，將其作為 Y2 的主要對標與借鑑對象，大幅強化計畫的學術前沿性。

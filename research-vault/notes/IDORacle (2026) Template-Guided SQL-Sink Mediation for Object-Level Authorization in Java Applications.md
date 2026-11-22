# IDORacle: Template-Guided SQL-Sink Mediation for Object-Level Authorization in Java Applications

> **論文基本資訊**
> - **論文標題**：IDORacle: Template-Guided SQL-Sink Mediation for Object-Level Authorization in Java Applications
> - **作者陣容**：Yuewantong Song et al.
> - **發表形式與年份**：Computers & Security 2026 / arXiv:2609.12426 (2026)
> - **研究標籤**：`#IDOR` `#BOLA` `#SQLMediation` `#JavaSecurity` `#RuntimeEnforcement` `#ComputersAndSecurity`

---

## 一、論文核心研究問題與痛點

1. **Java-SQL 架構的致命斷層（Architectural Disconnect）**：
   - 在現代 Java Web 系統（Spring Boot + MyBatis / Hibernate / JDBC）中，**授權與身份認證邏輯通常實作在 Controller 或 Service 層**，而**真正的資料存取與狀態變更卻發生在底層 SQL 層**。
   - 開發者經常在 Controller 或 Service 漏掉檢查，導致攻擊者只要竄改 HTTP 請求中的資源 ID，未受檢查的查詢便直接在資料庫執行，釀成 IDOR / BOLA（CWE-639）。
2. **傳統防禦方案的不足**：
   - 程式碼重構修復（Refactoring）成本極高且容易引入新 Bug。
   - 傳統 WAF 無法理解內部資料庫關聯與所有權語意。

---

## 二、核心技術方法：模板引導的 SQL-Sink 攔截與重寫

IDORacle 提出了一種低侵入性、以 SQL-Sink 為中心的執行期防禦架構：

```
[HTTP Request] ──► Trace Identifier (帶有主體身份上下文 Session User)
        │
        ▼
[Java Controller / Service] ──► (即使存在 Missing Check 也無妨 🛡️)
        │
        ▼
[MyBatis / JDBC SQL-Sink Boundary]
        │
        ├──► 提取 SQL 模板 (AST 分析與指紋比對)
        ├──► 注入所有權防護謂詞 (Ownership Predicate Injection)
        └──► 攔截或改寫越權 SQL 查詢
```

1. **身份上下文透明傳播（Context Propagation）**：
   - 透過 Server-side Trace Identifier，在跨執行緒、異步工作與資料存取邊界間，透明維持已驗證的主體身份。
2. **SQL 模板層級分析（Template-Guided Mediation Plans）**：
   - 在框架邊界提取 SQL 語法樹（AST），事先建立快取的調解計畫，兼顧極致效能與即時安全判定。
3. **防禦分類法（Guard Taxonomy）**：
   - 支援直接所有權謂詞注入（如自動附加 `AND owner_id = current_user`）。
   - 支援基於 JOIN 的關聯所有權檢查與群組權限探針。
   - 支援狀態機敏感的狀態轉移檢查（State-Transition Checks）。

---

## 三、對 Y2（侑宸：根因分析與路徑風險矩陣）的直接借鑑

1. **直接解答「架構強制機制究竟該位在哪一層」**：
   - Y2 計畫在診斷「為什麼漏洞會發生」時，IDORacle 提供了最權威的架構論述：**漏洞根因在於進入點檢查與落地持久化點（Sink）之間存在強制機制的架構斷層**。
2. **動態探針注入語意標準（RQ2 實作基礎）**：
   - Y2 在進行反事實驗證（RQ2：注入極簡 Assertion 驗證是否能阻斷 PoC 且零誤殺）時，探針的最佳落點往往不是 Controller（進入點多容易漏），而是靠近 Domain / DAO 的持久化邊界。IDORacle 驗證了此類謂詞注入的可行性與有效性。

# MACE: Detecting Privilege Escalation Vulnerabilities in Web Applications

> **論文基本資訊**
> - **論文標題**：MACE: Detecting Privilege Escalation Vulnerabilities in Web Applications
> - **作者陣容**：Maliheh Monshizadeh, Prasad Naldurg, V.N. Venkatakrishnan (University of Illinois at Chicago, IBM Research)
> - **發表頂會**：ACM Conference on Computer and Communications Security (CCS 2014)
> - **發表年份**：2014
> - **DOI / 連結**：DOI: 10.1145/2660267.2660337（2026-10-12 經 Crossref 更正；原寫 …2660309 為另一篇論文）
> - **研究標籤**：`#PrivilegeEscalation` `#HorizontalPrivilegeEscalation` `#HPE` `#WebSecurity` `#ACM-CCS`

---

## 一、論文核心研究問題與痛點

1. **背景**：
   - Web 應用普遍缺乏形式化的授權策略規範（Access Control Policy Specification）。安全審計通常仰賴大量耗時、易遺漏的人工程式碼檢視。
2. **研究貢獻**：
   - MACE 是學界文獻中**第一個能夠全自動檢測水平越權（Horizontal Privilege Escalation, HPE）**的程式分析工具。
   - 解決了「在缺乏官方安全規範的情況下，如何知道哪一段程式碼缺少了權限檢查」的核心問題。

---

## 二、核心技術方法：授權上下文一致性（Authorization Context Consistency）

MACE 提出了**授權上下文一致性（Authorization Context Consistency）**的核心假說：
> *在一個良構且安全的 Web 應用中，針對同一類敏感實體或資料資源的存取，系統內部應在所有相關路徑上維持一致的授權約束。*

```
Endpoint A: /user/view_profile?id=123   ──► [Check: Session.user == 123] ──► Read DB
                                                                               ▲
                                                                               │ 🚨 Inconsistency!
Endpoint B: /user/edit_profile?id=123   ──► [Missing Check!            ] ──► Write DB
```

1. **路徑條件抽取（Authorization Context Extraction）**：
   - 透過靜態程式分析，沿著控制流圖（CFG）提取抵達各敏感資源存取點（Resource Access Sink）之前的所有分支判斷條件。
2. **上下文一致性交叉比對（Consistency Comparison）**：
   - 將存取相同資料庫實體或敏感物件的所有進入點（Entrypoints / Endpoints）進行聚合。
   - 若特定進入點相較於其餘「同儕端點（Peer Endpoints）」明顯缺失了使用者身份或角色關聯判定，則自動報出為 Missing Authorization Check。
3. **實證成效**：
   - 在 7 個開源 Web 系統上挖掘出多個未公開的嚴重越權弱點，證實一致性推導能取代數週的人工審計。

---

## 三、對 Y2（侑宸：根因分析與路徑風險矩陣）的直接借鑑

1. **「同儕切片（Peer Slices）」在 Web 端的真正學術鼻祖**：
   - 先前文獻常引用 CRIX（USENIX Security 2019），但 CRIX 是做 Linux Kernel 的硬體驅動比對。**MACE 才是 Web 應用水平越權跨端點比對的純正開山始祖**。
2. **Y2 函式路徑風險矩陣的因果依據**：
   - Y2 的演算法設計中，「當 PoC 攻擊從未受防護的路徑進入時，透過風險矩陣定位專案內部哪些 Caller / Endpoint 遺漏了檢查」，其理論基礎完全承襲並推展了 MACE 的授權上下文一致性模型。

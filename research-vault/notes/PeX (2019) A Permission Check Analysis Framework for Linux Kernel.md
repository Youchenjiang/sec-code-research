---
title: "PeX: A Permission Check Analysis Framework for Linux Kernel"
authors: "Tong Shen, Le Guan, Chengchi Ding, Qingchuan Zhao, Peng Liu, Xing Gao"
year: 2019
venue: "USENIX Security 2019 (28th USENIX Security Symposium)"
url: "https://www.usenix.org/conference/usenixsecurity19/presentation/shen"
code: "https://github.com/SYS-CARE/PeX"
categories:
  - "[[1-靜態分析 (Static Analysis)]]"
  - "[[0-設計安全與威脅分析 (Secure Design & Threat Analysis)]]"
---

# 📖 PeX: A Permission Check Analysis Framework for Linux Kernel (USENIX Security 2019)

## 📄 本地專題關聯
- **所屬矩陣專題**：`[A.5 跨程序拓撲與全域風險矩陣]`, `[A.3 語意錯誤定位與失效判定]`
- **關聯檢索指南**：[Y2_擴展文獻全景檢索指南.md](../../proposals/logic-vuln-lifecycle/Y2-root-cause-localization/Y2_擴展文獻全景檢索指南.md)

---

## 📝 論文摘要 (Abstract)
> The Linux kernel implements complex access control mechanisms to safeguard system resources. However, manually verifying that all sensitive resources are appropriately protected by permission checks is error-prone. This paper presents **PeX**, an automated, inter-procedural static analysis framework designed to identify missing or inconsistent permission checks in the Linux kernel. PeX automatically extracts mapping relationships between kernel objects and their expected permission checks across the entire codebase. It then constructs inter-procedural control-flow graphs (CFGs) to discover execution paths capable of accessing protected objects without properly invoking the requisite permission checks. Evaluated on the Linux kernel, PeX discovered 36 previously unknown missing-check vulnerabilities.

---

## 🎯 核心解決問題 (Problem Statement)
* **研究背景**：在複雜系統中，受保護的關鍵物件（Objects）通常有多個進入點（Entrypoints）與存取路徑。只要有一條路徑遺漏了權限檢查（Missing Permission Check），整個系統的存取控制便會被徹底擊穿。
* **現有技術痛點**：人工審查跨程序（Inter-procedural）的深層呼叫鏈極其耗時，傳統污點分析難以自動判定「哪個物件需要哪種權限檢查」。
* **論文切入點**：**「物件與權限檢查對照抽取 ＋ 全域可達路徑搜尋」**——建立全專案的「資源 $\leftrightarrow$ 檢查」對照拓撲，搜尋所有能抵達該資源卻未執行對應檢查的幽靈路徑。

---

## 💡 關鍵創新點與貢獻 (Key Contributions)
1. **跨程序存取控制分析框架（PeX）**：形式化解決了大型程式碼庫中「缺少權限檢查」的全域拓撲搜尋問題。
2. **多進入點一致性校驗**：不僅檢查單一函式，而是遍歷所有可以抵達目標 Sink 的跨程序控制流路徑。

---

## 🧠 對第二年（Y2 侑宸）的借鑑與超越

1. **直接啟發 Y2「函式路徑風險矩陣（Function Path Risk Matrix）」的拓撲演算法**：
   * PeX 的核心精神是：**「修了一個漏洞點不夠，必須找出所有共享該權限檢查的進入點」**。這正是 Y2 產出全域風險矩陣的直接理論依據！Y2 利用類似的反向可達性分析，為 Y3 的多點修補標記出所有「共享同一 Invariant 卻未防護的進入點」。
2. **Y2 的專屬超越**：
   * **PeX 面對 C/Kernel**：檢查的是特權能力（Capabilities）與 DAC/MAC 函式。
   * **Y2 面對 Web / 微服務架構**：檢查的是高層**「業務物件所有權（Object-Level Ownership / BOLA）」**，並以動態 Exploit Trace 為事實錨點驗證可達性。

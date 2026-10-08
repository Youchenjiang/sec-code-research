---
title: "Detecting Missing-Check Bugs via Semantic- and Context-Aware Criticalness and Constraints Inferences"
authors: "Kangjie Lu, Aditya Pakki, Qiushi Wu"
year: 2019
venue: "USENIX Security 2019 (28th USENIX Security Symposium)"
url: "https://www.usenix.org/conference/usenixsecurity19/presentation/lu-kangjie"
code: "https://github.com/umnsec/crix"
categories:
  - "[[1-靜態分析 (Static Analysis)]]"
  - "[[0-設計安全與威脅分析 (Secure Design & Threat Analysis)]]"
---

# 📖 Detecting Missing-Check Bugs via Semantic- and Context-Aware Criticalness and Constraints Inferences (CRIX, USENIX Security 2019)

## 📄 本地專題關聯
- **所屬矩陣專題**：`[A.3 語意錯誤定位與失效判定]`, `[A.5 跨程序拓撲與全域風險矩陣]`
- **關聯檢索指南**：[Y2_擴展文獻全景檢索指南.md](../../proposals/logic-vuln-lifecycle/Y2-root-cause-localization/Y2_擴展文獻全景檢索指南.md)

---

## 📝 論文摘要 (Abstract)
> Operating system kernels must thoroughly validate untrusted user inputs and hardware interactions. A missing security check on critical variables can lead to severe security vulnerabilities such as privilege escalation, information leakage, and arbitrary memory corruption. Detecting missing-check bugs is challenging because it requires understanding whether a variable is critical and what specific security constraints should be enforced on it. This paper presents **CRIX**, an inter-procedural, semantic-, and context-aware static analysis system for detecting missing-check bugs. CRIX infers the criticalness of variables by analyzing how they are used across different paths and cross-checks the conditional statements in the "peer slices" of these variables to infer missing security constraints. Evaluated on the Linux kernel, CRIX identified 278 previously unknown missing-check bugs, resulting in 151 accepted patches from kernel maintainers.

---

## 🎯 核心解決問題 (Problem Statement)
* **研究背景**：程式中該有檢查卻沒寫檢查（Missing-Check Bug）是最難自動定位的漏洞類型之一，因為靜態分析器往往「不知道哪裡應該加檢查」。
* **現有技術痛點**：
  1. 單純語法模式比對無法理解變數的重要性（Criticalness），導致巨量誤報（False Positives）。
  2. 傳統交叉檢查（Cross-checking）忽略了不同執行路徑的業務上下文差異。
* **論文切入點**：**同儕切片分析（Peer Slices）**——如果一個關鍵變數在 9 條路徑中都被某個條件約束保護，但在第 10 條路徑中未被約束直接抵達 Sink，那麼第 10 條路徑大概率存在 Missing Check！

---

## 💡 關鍵創新點與貢獻 (Key Contributions)
1. **同儕切片推導理論（Peer Slices Inference）**：形式化定義了跨程序執行路徑上的同儕切片，透過比較同一個實體在不同控制流路徑上的約束集合，自動推導隱含的安全不變量。
2. **上下文感知的重要性判定（Context-Aware Criticalness）**：透過資料流依賴性分析判定變數是否具備安全敏感性，大幅降低誤報率。
3. **巨大的工業界衝擊**：在 Linux Kernel 中發掘 278 個全新 Missing-Check 漏洞，被官方收錄 151 個補丁。

---

## 🧠 對第二年（Y2 侑宸）的借鑑與超越

1. **直接奠定 Y2「Missing Predicate」診斷的理論基礎**：
   * CRIX 的「同儕切片（Peer Slices）」是判斷 `Missing Predicate` 最經典的學術武器。Y2 在分析後端多個 API 進入點時，正是利用同儕切片的思維：如果進入點 A 做了身份校驗，但存取同一實體的進入點 B 卻跳過了，即可判定 B 存在 `Missing Predicate`。
2. **Y2 的超越維度**：
   * **CRIX 是針對 C/Linux 底層指標與整數**：缺乏高層業務意圖與 Web API 的角色模型。
   * **Y2 引入 LLM 與動態利用軌跡**：Y2 將同儕切片提升至**「業務實體與權限約束（Business Entity & Authorization）」**層面，並以 Y1 的動態 Exploit 軌跡直接證明該 Missing Check 的可利用性。

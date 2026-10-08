---
title: "Locating Faults through Automated Predicate Switching"
authors: "Xiangyu Zhang, Nimit Gupta, Rajiv Gupta"
year: 2006
venue: "ICSE 2006 (28th International Conference on Software Engineering)"
url: "https://doi.org/10.1145/1134285.1134324"
code: ""
categories:
  - "[[2-動態分析 (Dynamic Analysis)]]"
  - "[[1-靜態分析 (Static Analysis)]]"
---

# 📖 Locating Faults through Automated Predicate Switching (ICSE 2006)

## 📄 本地專題關聯
- **所屬矩陣專題**：`[A.3 語意錯誤定位與失效判定]`, `[B.1 差分與對比執行分析]`
- **關聯檢索指南**：[Y2_擴展文獻全景檢索指南.md](../../proposals/logic-vuln-lifecycle/Y2-root-cause-localization/Y2_擴展文獻全景檢索指南.md)

---

## 📝 論文摘要 (Abstract)
> When a program execution fails, identifying the root cause statement among millions of executed instructions is challenging. This paper presents **Predicate Switching**, an automated technique to locate faults by dynamically altering the outcome of conditional expressions during program re-execution. If forcibly switching a predicate's boolean evaluation from true to false (or vice-versa) during a failing run causes the execution to succeed, that predicate is flagged as a **critical predicate**. By identifying critical predicates and calculating their dynamic execution slices, developers can significantly prune the search space for software bugs.

---

## 🎯 核心解決問題 (Problem Statement)
* **研究背景**：傳統錯誤定位依賴靜態切片或光譜分析（SBFL），產生的可疑語句數量龐大，且無法解釋「為什麼這個分支導致了失敗」。
* **現有技術痛點**：任意修改記憶體狀態的搜索空間巨大，且容易引發未定義行為或程式崩潰。
* **論文切入點**：**「二元條件式切換（Predicate Switching）」**——分支結果只有 True 或 False。如果在失敗重播中強制反轉某個條件判斷式，結果原本失敗的測試「奇蹟般地成功了」，那麼這個條件判斷式必定與漏洞的因果鏈緊密相關！

---

## 💡 關鍵創新點與貢獻 (Key Contributions)
1. **關鍵判斷式定義（Critical Predicates）**：形式化定義了透過動態反轉能修復執行結果的條件表達式。
2. **切換優先級啟發式演算法**：提出 LEFS（Last Executed First Switched）等高效搜索啟發式，大幅加速關鍵條件的定位速度。

---

## 🧠 對第二年（Y2 侑宸）的借鑑與超越

1. **直接啟發 Y2 的因果斷言探針（Assertion Probing）**：
   * Predicate Switching 是「因果推斷（Causal Inference）」在軟工調試中的經典原型。
   * Y2 在判定 **`Ineffective Check`（判斷式無效型漏洞）** 時，可以直接借鑑此思路：如果在執行期將某個被忽略的變數強制賦值為檢查結果，驗證 Exploit 是否被攔截。
2. **Y2 的專屬特徵與超越**：
   * **Predicate Switching 僅處理程式崩潰/輸出不符**：依賴傳統測試套件的 Exit Code。
   * **Y2 處理業務邏輯越權**：將 Predicate Switching 升級為**「安全不變量探針（Invariant Probing）」**，同時驗證「阻斷攻擊 Exploit ＋ 放行正常請求」。

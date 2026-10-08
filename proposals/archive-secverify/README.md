# SecVerify 計畫歸檔（SecVerify Archive）

本目錄歸檔實驗室前一階段計畫 **「SecVerify：全端軟體安全生成、動態微執行驗證與修復驗收」** 之相關企劃與評估資料。

---

## 📌 計畫定位與歷史脈絡

SecVerify 是一套從 **「白盒靜態分析（White-box SAST）」出發** 的全自動化驗證體系：

```
[第 1 年：靜態分析與誤報過濾] ──> [第 2 年：動態微執行驗證 (SecVerify 核心)] ──> [第 3 年：補丁修復驗收]
  (SAST 掃描 + 靜態 Triage)           (Robolectric 快驗 + Headless ART 真驗)          (安全補丁驗收與回歸)
```

### 與當前新計畫（Logic-Vuln-Lifecycle）之本質差異：
* **SecVerify（舊計畫）**：起點是靜態程式碼掃描報告，核心任務是解決「靜態分析誤報過高」，透過桌面 JVM（Robolectric）或輕量沙盒（Headless ART）對疑似漏洞進行微執行探測。
* **Logic-Vuln-Lifecycle（新計畫）**：起點是自主代理 DAST 滲透成功之攻擊軌跡（PoC Trace），核心任務是解決「已知被黑，但不知道後端架構缺失出在哪裡」，透過因果推導定位專案層級的強制機制缺失（Enforcement Diagnosis）。

---

## 📚 歷史完整報告索引（位於 `research-vault/reports/`）

SecVerify 相關的完整學術評估報告仍完好保留在知識庫中，可直接點擊參閱：

1. **第二年微執行重新設計**：
   * [SecVerify 第二年重新設計三大動態驗證方案評估.md](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/research-vault/reports/SecVerify%20%E7%AC%AC%E4%BA%8C%E5%B9%B4%E9%87%8D%E6%96%B0%E8%A8%AD%E8%A8%88%E4%B8%89%E5%A4%A7%E5%8B%95%E6%85%8B%E9%A9%97%E8%AD%89%E6%96%B9%E6%A1%88%E8%A9%95%E4%BC%B0.md)
   * 詳解方案 A（雙層級驗證引擎：Robolectric + Headless ART）與方案 B（標準 AndroidTest 直出）。
2. **學術流派與理論定位**：
   * [SecVerify 研究流派對照指南.md](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/research-vault/reports/SecVerify%20%E7%A0%94%E7%A9%B6%E6%B5%81%E6%B4%BE%E5%B0%8D%E7%85%A7%E6%8C%87%E5%8D%97.md)
   * [自動生成安全斷言（Security_Oracle_Generation）五合一文獻綜述大滿貫.md](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/research-vault/reports/%E8%87%AA%E5%8B%95%E7%94%9F%E6%88%90%E5%AE%89%E5%85%A8%E6%96%B7%E8%A8%80%EF%BC%88Security_Oracle_Generation%EF%BC%89%E4%BA%94%E5%90%88%E4%B8%80%E6%96%87%E7%8D%BB%E7%B6%9C%E8%BF%B0%E5%A4%A7%E6%BB%BF%E8%B2%AB.md)
3. **審查意見與研究回覆**：
   * [DevSecOps-SAFE_審查意見與研究回覆.md](file:///c:/Users/LabStrix/Documents/GitHub/Youchen/Security/code-security-research/research-vault/reports/DevSecOps-SAFE_%E5%AF%A9%E6%9F%A5%E6%84%8F%E8%A6%8B%E8%88%87%E7%A0%94%E7%A9%B6%E5%9B%9E%E8%A6%86.md)

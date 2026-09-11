# Android 動態測試 — 學術論文與研究資源完整清單

> 整理時間：2026-08-26
> 來源：學術論文、OWASP、CVE、安全研究部落格、Google 官方文件

---

## 一、系統性文獻綜述 (Survey / SoK)

| # | 論文/資源 | 重點 | 來源 |
|---|---|---|---|
| 1 | **Dynamic Security Analysis on Android: A Systematic Literature Review** (Sutter et al., 2024) | 79 citations，系統性回顧 Android 動態安全分析研究，涵蓋 DBI、taint analysis、fuzzing | ResearchGate / IEEE |
| 2 | **From Code to Security: ML Approaches in Android Security** (Springer, 2024) | 85 篇技術研究的系統性文獻回顧（2017-2024） | Springer |
| 3 | **A Systematic Literature Review on Automated Software Vulnerability Detection** (ACM, 2024) | 138 篇同行評審論文，涵蓋 ML/DL/LLM 偵測方法 | ACM |
| 4 | **A Comprehensive Study on SAST Tools for Android** (Chen et al., IEEE TSE 2024) | 比較 Android SAST 工具的偵測能力、速度、假陽性 | IEEE TSE |
| 5 | **SoK: Using Dynamic Binary Instrumentation for Security** (D'Elia et al., 2019) | 101 citations，DBI 安全應用系統性知識化 | ACM ASIACCS |
| 6 | **Evaluating DBI Systems for Conspicuous Features and Artifacts** (2021) | 評估 Frida/VIN/Pin/Valgrind 等 DBI 框架的可偵測性 | ACM |
| 7 | **Unveiling Dynamic Binary Instrumentation Techniques** (arXiv, 2025) | DBI 框架全面介紹與應用場景 | arXiv |
| 8 | **A Comprehensive Study of Privacy Leakage Vulnerability in Android App Logs** (ACM, 2024) | 開發者觀點 + 實際應用日誌隱私洩漏調查 | ACM |
| 9 | **Mobile Security Statistics 2026: Apps, APIs & Data Leakage** (DeepStrike, 2026) | 2026 年最新威脅統計、OWASP Mobile Top 10 2024 更新 | DeepStrike |
| 10 | **LLM-Guided Dynamic Security Testing of Android Applications** (MDPI, 2025) | 使用 LLM 引導自動化動態安全測試 | MDPI Electronics |

---

## 二、Android 元件與 IPC 漏洞

| # | 論文/資源 | 重點 | 來源 |
|---|---|---|---|
| 11 | **Securing Android IPC Using NGAC** (Simental & Azizli, 2024) | 利用 NGAC 模型保護 IPC，分析 Intent 權限提升攻擊 | Semantic Scholar |
| 12 | **MALintent: Coverage Guided Intent Fuzzing Framework for Android** (2025) | Intent 結構化模糊測試框架 | GTS3 2025 |
| 13 | **Template-based Android IPC Fuzzing** (FAU Erlangen) | 透過反組譯分析 Intent 結構進行自動化 IPC Fuzzing | FAU Erlangen |
| 14 | **Detection of Hidden Privilege Escalations in Android** (Springer, 2025) | 偵測透過 IPC 進行的隱藏權限提升 | Springer |
| 15 | **PITracker: Detecting Android PendingIntent Vulnerabilities** (WiSec 2022, 8 citations) | 自動化 PendingIntent 漏洞偵測工具，Intent Flow Analysis | ACM / ResearchGate |
| 16 | **Android Intent Redirection: Attack Vectors and Mitigations** (Ostorlab, 2026) | Intent Redirection 攻擊面全面分析 | Ostorlab Blog |
| 17 | **Intent Redirection Vulnerability in Third-Party SDK** (Microsoft, 2026) | 第三方 SDK 的 Intent Redirection 漏洞影響數百萬 App | Microsoft Security Blog |
| 18 | **Android Security of Broadcasting Mechanism** (ResearchGate, 2026) | 廣播機制安全研究 | ResearchGate |
| 19 | **Understanding the Bad Development Practices of Android Custom Permissions** (IEEE TQ, 2025) | 自訂權限的不良開發實踐分析 | IEEE |
| 20 | **Exploiting Inter-Component Communication (ICC) in Mobile Apps** (Medium, 2025) | ICC 漏洞利用實戰指南 | Medium |
| 21 | **CADDroid: Android App Collusion Dataset** (Springer, 2025) | App 共謀攻擊資料集 | Springer |

---

## 三、Deep Link 與 App Links 安全

| # | 論文/資源 | 重點 | 來源 |
|---|---|---|---|
| 22 | **DeepExploitor: LLM-Enhanced Automated Exploitation of DeepLink Attack** (ASE 2025) | 第一個 LLM 增強的 DeepLink 自動化漏洞利用框架 | ACM ASE |
| 23 | **Measuring the Insecurity of Mobile Deep Links of Android** (USENIX Security 2017, 48 citations) | DeepLink 不安全性測量經典論文 | USENIX |
| 24 | **Android Deep Link Vulnerabilities: How Intent Filters Lead to Account Takeover** (Oversecured, 2026) | 5 種 DeepLink 漏洞模式 | Oversecured Blog |
| 25 | **Full Account Takeover via Deeplinks** (Stingrai, 2026) | DeepLink 導致 ATO 的實戰案例 | Stingrai Blog |
| 26 | **One-Click Account Takeover: When Android Deep Link Hands Your Session** (InfoSec WriteUps, 2026) | 單點 DeepLink 洩漏 Session Token | InfoSec WriteUps |
| 27 | **From Improper Validation to Authentication Flow Injection** (Medium, 2026) | DeepLink 利用導致認證流程注入 | Medium |

---

## 四、WebView 與 Hybrid 安全

| # | 論文/資源 | 重點 | 來源 |
|---|---|---|---|
| 28 | **Vulnerabilities in Android WebView Objects: Still Not the End!** (ScienceDirect, 2021, 22 citations) | 三種新型 WebView 漏洞類型 | Computers & Security |
| 29 | **Bifocals: Analyzing WebView Vulnerabilities in Android Apps** (ResearchGate) | WebView 超權限授權 + XSS 分析 | ResearchGate |
| 30 | **Android WebView Vulnerabilities: Risks and Hardening** (SecureLayer7, 2024) | JS Bridge、檔案存取、SSL 間隙 | SecureLayer7 Blog |
| 31 | **CVE-2026-0628: Google Chrome WebView XSS** (SentinelOne, 2026) | WebView 標籤 XSS 漏洞 | SentinelOne |
| 32 | **Uncovering Hidden Pitfalls in Certificate Validation** (ACM, 2025) | In-app Browser 憑證驗證問題，77% Android WebView 接受不合規憑證鏈 | ACM |
| 33 | **Deep Dive into In-app Browsers** (ACM, 2025) | In-app Browser 的 TLS 與自動檢測研究 | ACM |
| 34 | **WebView Security Checklist** (Oversecured, 2021) | WebView 安全檢核清單 | Oversecured Blog |

---

## 五、SSL/TLS 與憑證安全

| # | 論文/資源 | 重點 | 來源 |
|---|---|---|---|
| 35 | **Revisiting TLS (In)Security in Android Applications** (USENIX Security 2021) | NSC 機制的實際效果評估 | USENIX |
| 36 | **Detection of SSL/TLS Implementation Errors in Android Applications** (ResearchGate, 2025) | SSL/TLS 配置錯誤偵測方法 | ResearchGate |
| 37 | **WireWatch: Measuring Security of Proprietary Network Encryption** (IEEE S&P 2025) | 自動偵測 Android App 私有網路加密 | IEEE S&P |
| 38 | **Utilization of Certificate Pinning in Mobile Applications** (DSF Journal) | 1,500 個熱門 App 的憑證 Pinning 評估 | DSF Journal |
| 39 | **Comparative Analysis of Certificate Pinning in Android & iOS** (ACM, 2022) | 跨平台憑證 Pinning 比較 | ACM |
| 40 | **Exploring the Android TLS Certificate Ecosystem in China** (Springer, 2026) | 19,980 個 App 的 TLS 憑證鏈分析 | Springer |
| 41 | **Evaluating NSC Practices in Vehicle-Related Android Apps** (SAE, 2024) | 汽車相關 Android App 的 NSC 配置評估 | SAE |
| 42 | **Certificate Transparency in Android 16** (Google Developer Blog, 2025) | Android CT 政策與實作 | Google |
| 43 | **Android CT Policy** (Google Developer, 2026) | 官方 CT 政策文件 | Android Developer |
| 44 | **How to Implement CT in Android 16** (LinkedIn, 2025) | CT 實作指南 | LinkedIn |

---

## 六、側信道攻擊

| # | 論文/資源 | 重點 | 來源 |
|---|---|---|---|
| 45 | **Power-Related Side-Channel Attacks using Android Sensor Framework** (NDSS 2025) | 利用感測器框架進行電源側信道攻擊 | NDSS |
| 46 | **Automated Side-Channel Analysis of Android APIs** (ACM CCS) | Android API 自動化側信道分析 | ACM CCS |
| 47 | **Stealing PINs via Mobile Sensors: Actual Risk vs User Perception** (PMC, 2017, 102 citations) | 感測器竊取 PIN 碼的實際風險 vs 感知風險 | PMC |
| 48 | **Deep Learning Based Side-Channel Attack Detection** (TST, 2025, 29 citations) | 深度學習偵測零權限感測器側信道攻擊 | TST |
| 49 | **Revolutionary Hybrid Ensembled DL Model for Side-Channel Attack Detection** (Nature, 2025, 6 citations) | 混合深度學習模型偵測鍵盤側信道攻擊 | Nature Scientific Reports |
| 50 | **ARMOUR US: Android Runtime Zero-permission Sensor Usage** (arXiv, 2025) | 監控零權限感測器存取偵測隱私洩漏 | arXiv |

---

## 七、模糊測試 (Fuzzing)

| # | 論文/資源 | 重點 | 來源 |
|---|---|---|---|
| 51 | **VLM-Fuzz: Vision Language Model Assisted Recursive DFS Fuzzing** (Springer, 2026) | VLM 輔助的 Android GUI 自動化模糊測試 | Springer |
| 52 | **FANS: Fuzzing Android Native System Services via Automated Interface** (USENIX Security 2020) | 原生系統服務自動化模糊測試 | USENIX |
| 53 | **BArcherFuzzer: Android System Services Fuzzing via Transaction** (IASC, 2024) | 基於 Transaction 的系統服務模糊測試 | IASC |
| 54 | **Fully Automated Functional Fuzzing of Android Apps** (ResearchGate, 2024) | 獨立視圖模糊測試，偵測非崩潰功能錯誤 | ResearchGate |
| 55 | **Recent Papers Related To Fuzzing** (FuzzingPaper, 2024+) | Fuzzing 論文匯總頁面 | GitHub Pages |

---

## 八、RASP 與反偵測

| # | 論文/資源 | 重點 | 來源 |
|---|---|---|---|
| 56 | **Detecting and Bypassing Frida Dynamic Function Call Tracing** (Soriano-Salvador, 9 citations) | 偵測 Frida 的技術 + 通用繞過方法 | URJC Repository |
| 57 | **RASP in Mobile Application Security: A Strategic Imperative** (CyberDefense Magazine, 2025) | RASP 在移動安全中的現狀與趨勢 | CDM |
| 58 | **RASP Investigation: Effectiveness and Performance** (SANS, 2024) | RASP 解決方案評估框架 | SANS |
| 59 | **Bypassing Commercial RASP and Root Detection** (LucidBit Labs, 2025) | 商業 RASP 與 Root 偵測繞過實戰 | LucidBit Blog |
| 60 | **Hook, Hack, Defend: Frida's Impact on Mobile Security** (Talsec, 2025) | Frida 攻防全面分析 | Talsec Docs 

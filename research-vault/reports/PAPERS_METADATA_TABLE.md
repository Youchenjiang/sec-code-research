# Android DAST Pipeline 論文 Metadata 表（表格版）

> 分類規則見 
> 
> **Coverage ≠ Contribution** — Stages 可多選，Primary 和 Role 單選
> 
> 共 151 篇論文（原有 57 篇 + 新下載 94 篇）

---

## 說明

| 欄位 | 說明 |
|------|------|
| Primary | 論文的主要貢獻所在階段（A/V/E/X 單選） |
| Stages | 論文覆蓋的 pipeline 階段（可多選） |
| Role | M=Method, O=Orchestration, B=Benchmark, S=Survey |
| Android | ✓ = 針對 Android 平台 |
| LLM | ✓ = 使用 Large Language Model |
| ⭐ | 相關度 1-3 |

---

## 完整 Metadata 表

| # | 檔案名 | Primary | Stages | Role | Android | LLM | Year | Venue | Key Contribution | ⭐ |
|---|--------|---------|--------|------|---------|-----|------|-------|------------------|----|
| 001 | A01_BugScribe_2026.pdf | A | A | M | ✓ | ✓ | 2026 | arXiv | LLM-based Android bug report enhancement |  |
| 002 | B01_A3_AndroidArena_2025.pdf | B | A, X | B | ✓ | ✓ | 2025 | arXiv | Android mobile GUI testing benchmark |  |
| 003 | B02_AgentScan_2025.pdf | B | A, X | B | ✓ | ✓ | 2025 | arXiv | Mobile LLM agent security evaluation framework |  |
| 004 | B03_MobileSafetyBench_2026.pdf | B | A, X | B | ✓ | ✓ | 2026 | AAAI 2026 | Mobile agent safety benchmark |  |
| 005 | B04_ExploitGym_2026.pdf | B | V, E, X | B | ✗ | ✓ | 2026 | arXiv | AI agents exploit vulnerabilities 的 benchmark |  |
| 006 | B05_ExploitBench_2026.pdf | B | V, E, X | B | ✗ | ✓ | 2026 | arXiv | 能力分級的 exploit benchmark（16 個 measurable flags） |  |
| 007 | B06_PACEbench_2025.pdf | B | V, E, X | B | ✗ | ✓ | 2025 | arXiv | 實際的 AI cyber-exploitation benchmark |  |
| 008 | B07_ZeroDayBench_2026.pdf | B | V, E | B | ✗ | ✓ | 2026 | arXiv | 評估 LLM agents on unseen zero-day vulnerabilities |  |
| 009 | B08_CyberGym_2025.pdf | B | A, V, E, X | B | ✗ | ✓ | 2025 | arXiv | Large-scale cybersecurity benchmark（1,507 vulnerabilities） |  |
| 010 | B09_CyberGym_E2E_2026.pdf | B | A, V, E, X | B | ✗ | ✓ | 2026 | arXiv | End-to-end cybersecurity benchmark（920 vulnerabilities） |  |
| 011 | B10_CyBench_2024.pdf | B | A, V, E, X | B | ✗ | ✓ | 2024 | arXiv | 40 個 professional-level CTF tasks 評估 LLM |  |
| 012 | B11_AutoPenBench_2024.pdf | B | A, V, E, X | B | ✗ | ✓ | 2024 | EMNLP 2025 Industry | Open benchmark for generative agents in pentest（33 tasks） |  |
| 013 | B12_CVEBench_2025.pdf |  |  |  |  |  | 2025 | ICML 2025 |  |  |
| 014 | B13_SurprisingEfficacy_2025.pdf | B | A, V, E, X | B | ✗ | ✓ | 2025 | arXiv | Empirical evaluation of LLMs for pentest |  |
| 015 | E01_Exploiting_PendingIntent.pdf | V | A, V, E | M | ✓ | ✗ |  |  | Android PendingIntent exploitation |  |
| 016 | E02_PoCGen_2026.pdf | E | V, E | M | ✗ | ✓ | 2026 | FSE 2026 | LLM + SAST feedback loop 生成 PoC（60% 成功率） |  |
| 017 | E03_FaultLine_2025.pdf | E | V, E | M | ✗ | ✓ | 2025 | arXiv | LLM agent 工作流生成 proof-of-vulnerability |  |
| 018 | E04_LLM_WebVulnRepro_2025.pdf | E | V, E | B | ✗ | ✓ | 2025 | arXiv | LLM agents web vulnerability reproduction 的 comprehensive evaluation |  |
| 019 | E05_PAGENT_2026.pdf | E | V, E | M | ✗ | ✓ | 2026 | ISSTA 2026 | Program analysis 引導 LLM agent 生成 PoC exploit |  |
| 020 | E06_APPATCH_2025.pdf | E | V, E | M | ✗ | ✓ | 2025 | USENIX Security 2025 | Automated adaptive prompting for LLM vulnerability patching |  |
| 021 | E07_RAVEN_Repair_2026.pdf | E | V, E | M | ✗ | ✓ | 2026 | arXiv | Agentic RAG for autonomous vulnerability repair |  |
| 022 | E08_VulR2_2025.pdf | E | V, E | M | ✗ | ✓ | 2025 | ASE 2025 | Reasoning LLM for vulnerability repair |  |
| 023 | M01_CyberZero_2025.pdf | M | A, V, E, X | M | ✗ | ✓ | 2025 | arXiv | Runtime-free framework 合成 agent trajectories 訓練 cybersecurity LLMs |  |
| 024 | O01_HPTSA_2024.pdf | O | A, V, E, X | O | ✗ | ✓ | 2024 | arXiv (UIUC) | Multi-agent 系統利用 zero-day 漏洞（53% success rate） |  |
| 025 | O02_PentestGPT_2024.pdf | O | A, V, E, X | O | ✗ | ✓ | 2024 | USENIX Security 2024 | LLM 驅動的自動化滲透測試框架（三模組架構） |  |
| 026 | O03_VulnBot_2025.pdf | O | A, V, E, X | O | ✗ | ✓ | 2025 | arXiv | Multi-agent LLM 模擬人類 pentest team 協作流程 |  |
| 027 | O04_TitanCA_2026.pdf | O | V | O | ✗ | ✓ | 2026 | arXiv | LLM agents 發現 100+ CVEs 的實戰經驗 |  |
| 028 | O05_CAI_2025.pdf | O | A, V, E, X | O | ✗ | ✓ | 2025 | arXiv | 開源 AI pentest framework |  |
| 029 | O06_PentestAgent_2025.pdf | O | A, V, E, X | O | ✗ | ✓ | 2025 | ASIACCS 2025 | LLM-based automated pentest framework with RAG |  |
| 030 | O07_APTAgent_2026.pdf | O | A, V, E, X | O | ✗ | ✓ | 2026 | arXiv | Fully automated LLM-driven pentest，解決 hallucination + 長期記憶 |  |
| 031 | O08_xOffense_2025.pdf | O | A, V, E, X | O | ✗ | ✓ | 2025 | arXiv | Multi-agent pentest framework with offensive knowledge-enhanced LLMs |  |
| 032 | O09_CHECKMATE_2025.pdf | O | A, V, E, X | O | ✗ | ✓ | 2025 | arXiv | LLM + classical planning 做 pentest |  |
| 033 | O10_AutoPentest_2025.pdf | O | A, V, E, X | O | ✗ | ✓ | 2025 | arXiv | GPT-4o + LangChain autonomous black-box pentest |  |
| 034 | O11_HackSynth_2024.pdf | O | A, V, E, X | O | ✗ | ✓ | 2024 | arXiv | LLM-based agent + evaluation framework for autonomous pentest |  |
| 035 | O12_CurriculumPT_2025.pdf | O | A, V, E, X | O | ✗ | ✓ | 2025 | MDPI Applied Sciences | Curriculum learning + multi-agent for pentest |  |
| 036 | O13_AutomationExploit_2026.pdf | O | A, V, E, X | O | ✗ | ✓ | 2026 | arXiv | Multi-agent + digital twin for risk-mitigated exploitation |  |
| 037 | O14_AllYouNeedFuzzingBrain_2025.pdf | O | V, X | O | ✗ | ✓ | 2025 | arXiv | LLM-powered CRS，基於 OSS-Fuzz |  |
| 038 | O15_FuzzingBrain_V2_2026.pdf | O | V, X | O | ✗ | ✓ | 2026 | arXiv | Multi-agent LLM system，AIxCC 決賽 90% detection rate |  |
| 039 | O16_CVEGenie_2026.pdf | O | V, E, X | O | ✗ | ✓ | 2026 | CCS 2026 | Fully automated LLM multi-agent CVE reproduction（51% rate） |  |
| 040 | O17_BlindGods_2026.pdf | O | A, X | O | ✓ | ✓ | 2026 | arXiv | Mobile agent OS 安全架構設計 |  |
| 041 | O18_RapidPen_2025.pdf | O | A, V, E, X | O | ✗ | ✓ | 2025 | arXiv | 60% success rate, 200-400 seconds, $0.3-$0.6 per test |  |
| 042 | O19_AgentFlow_2026.pdf | O | V, X | O | ✗ | ✓ | 2026 | arXiv | Typed graph DSL for multi-agent harness design（84.3% T |  |
| 043 | O20_AutoPenGPT_2025.pdf | O | A, V, E, X | O | ✗ | ✓ | 2025 | University of Auckland thesis | LLM-enhanced automated pentest framework |  |
| 044 | O21_ATLANTIS_2025.pdf | O | V | O | ✗ | ✓ | 2025 | arXiv | 🏆 AIxCC 冠軍 — 完整的 CRS 架構設計 |  |
| 045 | O22_OSS_CRS_2026.pdf | O | A, V, E, X | O | ✗ |  | 2026 | WOOT 2026 |  |  |
| 046 | S01_WhenFuzzingMeetsLLMs_2024.pdf | S | X | S | ✗ | ✓ | 2024 | FSE 2024 | LLM+fuzzing 的 comprehensive survey |  |
| 047 | S02_LLM_Agent_Security_Survey_2024.pdf | S | A, V, E, X | S | ✗ | ✓ | 2024 | ACM Computing Surveys | LLM agent security comprehensive survey |  |
| 048 | S03_LLM_Agent_Security_Duality_2026.pdf | S | A, V, E, X | S | ✗ | ✓ | 2026 | Springer | LLM agents in security 的 dual perspective survey |  |
| 049 | S04_SoK_VulnRepair_2025.pdf | S | V, E | S | ✗ | ✓ | 2025 | USENIX Security 2025 | Automated vulnerability repair 的 systematization of knowledge |  |
| 050 | S05_Survey_LLM_Pentest_2026.pdf | S | A, V, E, X | S | ✗ | ✓ | 2026 | arXiv | 81 篇論文 comprehensive survey（2023-2026） |  |
| 051 | S06_LLM_GUI_Agents_Survey_2025.pdf | S | A, X | S | ✓ | ✓ | 2025 | TMLR | LLM phone GUI agents comprehensive survey |  |
| 052 | S07_BenchmarkingPractices_2025.pdf | S | A, V, E, X | S | ✗ | ✓ | 2025 | arXiv | 分析 LLM-driven attack 的 benchmarking practices |  |
| 053 | S08_SoK_AIxCC_2026.pdf | S | A, V, E, X | S | ✗ | ✓ | 2026 | USENIX Security 2026 | AIxCC 的第一次系統性分析 |  |
| 054 | V01_Sutter.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 055 | V02_Arikan.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 056 | V03_Heid.pdf | V | V | M | ✓ | ✗ | 2021 | MobiSys | Automated Dynamic Android App Vuln Analysis |  |
| 057 | V04_Wang_Zhou_A2_Agentic_Discovery.pdf | V | A, V | M | ✓ | ✓ | 2025 |  | LLM agent 結合 static analysis 發現 Android 漏洞 |  |
| 058 | V05_Tam_Evolution.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 059 | V06_Mayrhofer.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 060 | V07_Allen.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 061 | V08_Lan_Statistical_Analysis.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 062 | V09_Samhi.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 063 | V10_Qualitative_Analysis.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 064 | V11_Romdhana.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 065 | V12_Bad_Development_Practices.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 066 | V13_Intent_Redirection.pdf | V | A, V | M | ✓ | ✗ |  |  | Android Intent redirection vulnerabilities |  |
| 067 | V14_Precise_Analysis.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 068 | V15_Risk_Estimation.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 069 | V16_Oltrogge.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 070 | V17_SSLTLS.pdf | V | V | M | ✓ | ✗ |  |  | Android SSL/TLS security |  |
| 071 | V18_Evaluating_NSC.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 072 | V19_Wasserstein_GAN.pdf | V | V | M | ✓ | ✓ |  |  | Wasserstein GAN for adversarial malware detection |  |
| 073 | V20_Niroshan.pdf | (待分類) | (待分類) | (待分類) |  |  |  |  |  |  |
| 074 | V21_Dong_Understanding_Android_Obfuscation.pdf | A | A | M | ✓ | ✗ |  |  | Android obfuscation analysis |  |
| 075 | V22_Meli_Accessibility.pdf | V | V | M | ✓ | ✗ | 2018 | ROOTS | Android UI security undermined by accessibility |  |
| 076 | V23_Systematic_Study_of_Clipboard.pdf | V | V | M | ✓ | ✗ |  |  | Systematic study of clipboard security |  |
| 077 | V24_Assessing_Privacy_Compliance.pdf | V | A, V | M | ✓ | ✗ |  |  | Privacy compliance assessment |  |
| 078 | V25_KeyDroid.pdf | V | V | M | ✓ | ✗ |  |  | Android keylogging security |  |
| 079 | V26_Shakevsky.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 080 | V27_Liu_Measuring_Insecurity.pdf | V | V | M | ✓ | ✗ |  |  | Measuring Android app insecurity |  |
| 081 | V28_Mobile_Payment_Security_Critical_Analysis.pdf | V | V | S | ✓ | ✗ |  |  | Mobile payment security analysis |  |
| 082 | V29_Comprehensive_Vuln_Analysis.pdf | V | V | S | ✓ | ✗ |  |  | Comprehensive vulnerability analysis |  |
| 083 | V30_Evolution_of_DevSecOps.pdf | S | A, V, E, X | S | ✗ | ✓ |  |  | Evolution of DevSecOps |  |
| 084 | V31_Zhao.pdf | E | A,E | M | ✓ | ✓ | | | Zhao et al. "Identifying the primary dimensions of DevSecOps" JSS 2024 — 33 pages |  |
| 085 | V32_El-Rewini_Aafer.pdf | E | A,E | M | ✓ | ✓ | | | El-Rewini & Aafer "Dissecting Residual APIs in Custom Android ROMs" CCS 2021 — 14 pages |  |
| 086 | V33_AndroByte_2025.pdf | V | A, V | M | ✓ | ✓ | 2025 | ACSAC 2025 | LLM 分析 Android bytecode 做 privacy analysis |  |
| 087 | V34_NotAnA11y_2026.pdf | V | A, V | M | ✓ | ✓ | 2026 | arXiv | Android accessibility trees 讓 AI agents 容易受 prompt injection |  |
| 088 | V35_LLMxCPG_2025.pdf | V | V | M | ✗ | ✓ | 2025 | USENIX Security 2025 | CPG + LLM 整合的 vulnerability detection |  |
| 089 | V36_Antiproof_2026.pdf | V | V, E | M | ✗ | ✓ | 2026 | arXiv | Neuro-symbolic detector synthesis + exploit proof |  |
| 090 | V37_LAMD_2025.pdf | V | V | M | ✓ | ✓ | 2025 | IEEE S&P Workshop 2025 | Three-tier LLM reasoning for Android malware detection |  |
| 091 | V38_MARD_2026.pdf | V | V | O | ✓ | ✓ | 2026 | arXiv | Multi-agent + LLM + static analysis for Android malware |  |
| 092 | V39_RuleDroid_2026.pdf | V | V | M | ✓ | ✓ | 2026 | IEEE TS 2026 | LLM 自動生成 Semgrep-compatible 安全偵測規則 for Android |  |
| 093 | V40_QLPro_2025.pdf | V | V | M | ✗ | ✓ | 2025 | arXiv | LLM + CodeQL 整合的 vulnerability detection |  |
| 094 | V41_KNighter_2025.pdf | V | V | M | ✗ | ✓ | 2025 | SOSP 2025 | LLM 自動生成 static analysis checkers（70 bugs in Linux kernel） |  |
| 095 | V42_RulePilot_2026.pdf | V | V | M | ✗ | ✓ | 2026 | ICSE 2026 | LLM agent 模擬人類專家生成 security rules |  |
| 096 | V43_PersistentFeedback_2026.pdf | V | V | M | ✗ | ✓ | 2026 | arXiv | LLM + CodeQL + Semgrep 的迭代改進 |  |
| 097 | V44_RAVEN_Exploration_2026.pdf | V | V | M | ✗ | ✓ | 2026 | arXiv | Multi-agent + RAG for structured vulnerability exploration |  |
| 098 | V45_LLM_ExplAndroidMalware_2025.pdf | V | V | M | ✓ | ✓ | 2025 | arXiv | Explainable Android malware detection via LLM |  |
| 099 | V46_WhenAITakesWheel_2025.pdf | V | V | M | ✗ | ✓ | 2025 | arXiv | LLMs 在 framework-constrained 環境產生 vulnerable programs |  |
| 100 | V47_LLM_TaintAnalysis_2026.pdf | V | V | M | ✓ | ✓ | 2026 | arXiv | LLM-enhanced Android taint analysis |  |
| 101 | V48_LATTE_2023.pdf | V | V | M | ✗ | ✓ | 2023 | ACM TOSEM / ASE 2025 | First LLM-powered static binary taint analysis |  |
| 102 | V49_SemTaint_2026.pdf | V | V | M | ✗ | ✓ | 2026 | arXiv | Static-led, LLM-augmented vulnerability analysis |  |
| 103 | V50_OpenAnt_2026.pdf | V | V | M | ✗ | ✓ | 2026 | arXiv | Open-source closed-loop vulnerability discovery（12 CVEs in OpenSSL） |  |
| 104 | V51_Revelio_2026.pdf | V | V | M | ✗ | ✓ | 2026 | arXiv | Two-stage agentic framework（$300, 19 unknown vulns） |  |
| 105 | V52_DroidTTP_2025.pdf | V | A, V | M | ✓ | ✓ | 2025 | Journal of Information Security and Applications | Android malware → MITRE ATT&CK TTP mapping |  |
| 106 | V53_ExplicitVulnGeneration_2025.pdf | V | V | M | ✗ | ✓ | 2025 | arXiv | LLMs explicitly generating vulnerabilities（74-98% accuracy） |  |
| 107 | V54_SecureFalcon_2025.pdf | V | V | M | ✗ | ✓ | 2025 | IEEE TS | Lightweight LLM (121M params) for vuln detection（94% accuracy） |  |
| 108 | V55_FromDescriptionToScore_2025.pdf | V | V | M | ✗ | ✓ | 2025 | ACM 2026 | LLM for automated CVSS scoring |  |
| 109 | V56_AutoCVSS_2025.pdf | V | V | M | ✗ | ✓ | 2025 | EMNLP 2025 Industry | LLM for automated CVSS scoring |  |
| 110 | V57_SELinux_LLM_2025.pdf | V | V | M | ✓ | ✓ | 2025 | ACM (Springer LNCS) | LLM-based dynamic SELinux policy generation |  |
| 111 | V58_ML_SELinux_2024.pdf | V | V | M | ✓ | ✗ | 2024 | arXiv | ML for SELinux policy analysis |  |
| 112 | V59_GDPR_Android_2025.pdf | V | A, V | M | ✓ | ✓ | 2025 | FSE 2025 | LLM for Android GDPR compliance checking via Smali code |  |
| 113 | X01_Labeda_Sepczuk.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 114 | X02_Katoch_Garg.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 115 | X03_Wong_Lie_TIRO.pdf | X | A, X | M | ✓ | ✗ |  |  | Android 自動化測試工具 |  |
| 116 | X04_Auer.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 117 | X05_Iannillo_Chizpurfle.pdf | V | A, V | M | ✓ | ✗ |  |  | Android permissions 混合分析 |  |
| 118 | X06_Liu_FANS.pdf | X | X | M | ✓ | ✗ | 2020 | USENIX Security 2020 | Android native system services fuzzing |  |
| 119 | X07_Wong_Lie_IntelliDroid.pdf | X | A, X | M | ✓ | ✗ |  |  | Targeted input generation for Android |  |
| 120 | X08_Wong_CAR.pdf | X | A, X | M | ✓ | ✗ |  |  | Android runtime analysis |  |
| 121 | X09_CamDroid.pdf | X | A, X | M | ✓ | ✗ |  |  | Automated camera app testing |  |
| 122 | X10_Mao_Sapienz.pdf | X | A, X | M | ✓ | ✗ | 2016 | FSE 2016 | Multi-objective automated testing for Android |  |
| 123 | X11_Li_DroidBot.pdf | X | A, X | M | ✓ | ✗ | 2017 | ICSE-SEIP 2017 | Generic Android test input generator |  |
| 124 | X12_Su_Stoat.pdf | X | A, X | M | ✓ | ✗ | 2016 | ISSTA 2016 | Novel approach to automated GUI testing |  |
| 125 | X13_Song_EHBDroid.pdf | X | A, X | M | ✓ | ✗ |  |  | Automated testing for Android apps |  |
| 126 | X14_Li_Humanoid.pdf | X | A, X | M | ✓ | ✗ | 2019 | ICSE 2019 | Deep learning-based automated Android testing |  |
| 127 | X15_Liu_GPTDroid.pdf | X | A, X | M | ✓ | ✓ | 2024 |  | LLM-based automated Android testing |  |
| 128 | X16_InputBlaster.pdf | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 129 | X17_ScenGen.pdf | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 130 | X18_GPT-Monkey.pdf | X | A, X | M | ✓ | ✓ | 2024 |  | LLM-based automated testing |  |
| 131 | X19_Suo.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 132 | X20_A_Stealthy_Dynamic_Analysis_Framework.pdf | X | X | M | ✓ | ✗ |  |  | Stealthy dynamic analysis framework |  |
| 133 | X21_Dawoud_Bugiel.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 134 | X22_Automated_Security_Testing_in_DevSecOps_AI.pdf | O | A, V, E, X | S | ✗ | ✓ |  |  | Automated security testing in DevSecOps with AI |  |
| 135 | X23_Automating_Security_Testing_in_CICD.pdf | O | A, V, E, X | S | ✗ | ✓ |  |  | Automating security testing in CI/CD |  |
| 136 | X24_Marandi.pdf | (待分類) | (待分類) | (待分類) | ✓ | (待確認) |  |  |  |  |
| 137 | X25_AdbGPT_2024.pdf | X | A, X | M | ✓ | ✓ | 2024 | ICSE 2024 | LLM 透過 ADB commands 自動 replay Android bugs |  |
| 138 | X26_DroidCall_2025.pdf | X | A, X | M | ✓ | ✓ | 2025 | EMNLP 2025 | LLM 觸發 Android Intent 的 dataset 和方法 |  |
| 139 | X27_BreakingAndroid_2025.pdf | X | A, V, X | M | ✓ | ✓ | 2025 | arXiv | LLM 自動化 Android penetration testing |  |
| 140 | X28_AHAFuzz_2025.pdf | X | A, X | M | ✓ | ✗ | 2025 | CCS 2025 | Intent-aware greybox fuzzing for hardened Android apps |  |
| 141 | X29_LELANTE_2026.pdf | X | A, X | M | ✓ | ✓ | 2026 | ACM 2026 | LLM 從自然語言自動執行 Android testing |  |
| 142 | X30_MALintent_2025.pdf | X | A, X | M | ✓ | ✗ | 2025 | NDSS 2025 | Coverage-guided Intent fuzzing for Android |  |
| 143 | X31_LivingWithPackers_2025.pdf | X | A, X | M | ✓ | ✗ | 2025 | arXiv | 處理 packed Android apps 的動態分析 |  |
| 144 | X32_LLMsAsHackers_2025.pdf | X | X | M | ✗ | ✓ | 2025 | EMSE | GPT-4-Turbo 自動做 Linux privilege escalation |  |
| 145 | X33_Fuzz4All_2024.pdf | X | X | M | ✗ | ✓ | 2024 | ICSE 2024 | 第一個 universal fuzzer，LLM 生成 diverse inputs |  |
| 146 | X34_PromptFuzz_2024.pdf | X | X | M | ✗ | ✓ | 2024 | CCS 2024 | LLM 生成 fuzz driver，coverage-guided |  |
| 147 | X35_FuzzingBusyBox_2024.pdf | X | X | M | ✗ | ✓ | 2024 | USENIX Security 2024 | LLM + crash reuse 做 embedded fuzzing |  |
| 148 | X36_DirectedGreybox_2025.pdf | X | X | M | ✗ | ✓ | 2025 | arXiv | LLM 指導 directed greybox fuzzing |  |
| 149 | X37_LLM_ModelBasedFuzzing_2025.pdf | X | X | M | ✗ | ✓ | 2025 | arXiv | LLM + model-based fuzzing for network protocols |  |
| 150 | X38_SemanticAwareFuzzing_2025.pdf | X | X | M | ✗ | ✓ | 2025 | arXiv | LLM-guided fuzzing with semantic awareness |  |
| 151 | X39_TreeMind_2026.pdf | X | A, X | M | ✓ | ✓ | 2026 | arXiv | LLM + MCTS for Android bug reproduction |  |

---

## 統計摘要

| Primary | 數量 | 說明 |
|---------|------|------|
| **V** (Vulnerability Discovery) | 39 | |
| **X** (Execution/Fuzzing) | 28 | |
| **O** (Orchestration) | 24 | |
| **B** (Benchmark) | 12 | |
| **S** (Survey) | 9 | |
| **E** (Exploit/PoC) | 7 | |
| **A** (Target Analysis) | 2 | |
| **M** (Malware) | 1 | |

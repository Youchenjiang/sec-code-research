# 150 篇論文 — Android App 運行環境建置方式

> 從每篇論文的 md 全文提取
> 2026-08-31（已修正數字與漏列）
> **重要：本文件只列「讓 Android App 實際跑起來」的環境。靜態分析（只讀 APK 不執行）的論文另外列。**

---

## 總覽

| 類型 | 篇數 | 說明 |
|------|------|------|
| **真正跑 App 的環境** | **89 篇** | 模擬器 / 真機 / Docker Android / 雲端裝置農場 |
| **靜態分析（不跑 App）** | 46 篇 | 只讀 APK，用 JADX/Soot/CodeQL 分析 |
| **Survey 綜述** | 21 篇 | 純文獻回顧，無工具 |
| **總計** | **156 篇條目** | 150 篇 PDF + 工具引用（redroid）+ 1 篇疑似誤收（V_M_Samhi） |

---

## 第一部分：真正跑 App 的環境（89 篇）

### A. Android Emulator（官方模擬器）

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 1 | **AdbGPT** (ICSE 2024) | Android x86-64 emulator | MacBook Pro 2.6GHz Intel Core 6核 | Bug report → LLM → ADB commands → emulator replay |
| 2 | **DroidBot** (ASE 2017) | Android Emulator 或真機 | 無特別指定 | `droidbot -a target.apk -d` 自動探索 |
| 3 | **Stoat** (ISSTA 2016) | Android Emulator (emulator-5554) | 無特別指定 | 自動化 GUI 測試 + 隨機輸入 |
| 4 | **Humanoid** (ICSE 2019) | Android Emulator 或真機 | 無特別指定 | 深度學習生成 GUI 測試動作 |
| 5 | **Sapienz** (FSE 2016) | Android Emulator | 無特別指定 | 多目標自動化 monkey testing |
| 6 | **EHBDroid** (ASE 2017) | Android Emulator | 無特別指定 | Event-handler-based testing |
| 7 | **TreeMind** (arXiv 2026) | Android virtual device | 無特別指定 | MCTS + 雙 LLM agent bug reproduction |
| 8 | **GPT-Monkey** (arXiv 2024) | Android Emulator 或真機 | 無特別指定 | LLM 生成 GUI 測試動作 |
| 9 | **InputBlaster** (arXiv 2025) | Android Emulator 或真機 | 無特別指定 | Unusual text inputs → crash detection |
| 10 | **GPTDroid** (ICSE 2024) | **VirtualBox + Android-x86 + ADB** | Ubuntu 18.04 64核 AMD CPU, 2GB RAM per emulator, Android 7.1, X86 ABI | ChatGPT (gpt-3.5-turbo) → ADB → emulator GUI testing |
| 11 | **ScenGen** (arXiv 2024) | **ADB + Android Emulator** | 無特別指定 | LLM scenario → ADB commands → emulator GUI testing |
| 12 | **CamDroid** (TST 2025) | **ADB + 真機或模擬器** | Snapdragon 855, 2.84GHz CPU, 6GB RAM, Android 11 | GAN text input + Q-learning → ADB → GUI testing (Android 10-13) |
| 13 | **Chizpurfle** (USENIX 2020) | **真機 Google Pixel 2** | Android Oreo 8.0.0（不可用模擬器） | 需要真機因為 proprietary vendor customizations 在模擬器上不可用 |
| 14 | **MobileSafetyBench** (AAAI 2026) | Android emulator (Pixel 7) + Appium | 無特別指定 | 250 tasks, 13 種 Apps |
| 15 | **AndroidArena** (arXiv 2025) | Android Emulator | L40s GPU (48GB) 訓練 | GUI testing benchmark |

### B. Genymotion（VirtualBox 底層）

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 16 | **BreakingAndroid** (arXiv 2025) | Genymotion 模擬器 | 無特別指定 | PentestGPT + Frida + Genymotion |

### C. VirtualBox

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 17 | **Dynodroid** (FSE 2013) | VirtualBox + VHD（有現成虛擬機） | 無特別指定 | 匯入 VHD → 直接跑 Android → 自動 fuzzing |

### D. 真機（Physical Device）

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 19 | **IntelliDroid / TIRO** (IEEE S&P 2016) | **真機 Nexus 5** | Intel i7-3770 + 32GB RAM（靜態）+ Nexus 5（動態） | 靜態 targeting → 動態執行 on 真機 |
| 20 | **CAR** (Android Runtime Analysis) | **真機 Pixel + Pixel 2** | Intel Xeon E5-2650 + 200GB RAM（靜態）+ Intel i7-3770 + USB-A（動態） | 靜態 targeting → 真機 runtime analysis |
| 21 | **DroidCall** (EMNLP 2025) | **真機（On-device）** | 無特別指定 | 3B 小模型直接在手機上跑 Intent invocation |
| 22 | **KeyDroid** | **AWS Device Farm（雲端真機農場）** | AWS cloud | 靜態分析 30 萬 apps → AWS Device Farm 跑測試 |

### E. Rooted Emulator（需要 root 權限）

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 23 | **AHA-Fuzz** (CCS 2025) | **Android Emulator (rooted, Android 13)** | macOS Sonoma + Apple M2 Ultra 24核 + 192GB RAM | eBPF-based 動態分析 + Intent/GUI fuzzing |
| 24 | **MALintent** (NDSS 2025) | **rooted emulator** | 無特別指定 | Coverage-guided Intent fuzzing |
| 25 | **FANS** (USENIX Security 2020) | **rooted Android emulator** | 無特別指定 | Android native system services fuzzing |

### F. Docker 容器化 Android

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 26 | **redroid** (非論文，工具) | Docker container | Linux host | `docker run redroid/redroid:14.0.0` → 容器內跑 Android |

### G. 雲端裝置農場（已合併至 §D #22 KeyDroid）

> ⚠️ 原 #27 KeyDroid 與 #22 重複，已移除。KeyDroid 唯一條目在 §D #22。

### H. AOSP 編譯（修改版 Android 系統）

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 28 | **TaintDroid** (USENIX 2010) | **修改版 AOSP**（taint tracking） | 需要 AOSP 編譯（3-6小時） | 追蹤資料在 App 裡的流向 |
| 29 | **SELinux LLM** (ACM 2025) | AOSP | AOSP build environment | LLM 生成 SELinux policy |
| 30 | **ML SELinux** (arXiv 2024) | AOSP | AOSP build environment | ML 分析 SELinux policy |

### I. LELANTE + Appium（自動化測試執行）

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 31 | **LELANTE** (ACM 2026) | Appium + 真機或模擬器 | 無特別指定 | 自然語言 test case → Appium 執行 |

### J. LLMsAsHackers（Linux VM 測試環境）

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 32 | **LLMsAsHackers** (EMSE 2025) | **Docker VMs（Linux privilege escalation）** | 無特別指定 | GPT-4-Turbo vs 專業 pentester（7年經驗） |

### K. Benchmark 平台（Docker containers 跑 vulnerable apps）

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 33 | **CVEBench** (ICML 2025) | Docker containers | 無特別指定 | 每個 CVE → web app container + DB container |
| 34 | **CyberGym** (arXiv 2025) | Docker containers | 2x AMD EPYC 9654 + 1.5TB RAM + 10TB disk | 1,507 vulnerabilities |
| 35 | **CyberGym E2E** (arXiv 2026) | Docker containers | 同上 | 920 vulnerabilities |
| 36 | **CyBench** (arXiv 2024) | CTF challenges（各類環境） | Docker + CTF tools | 40 professional-level CTF tasks |
| 37 | **AutoPenBench** (EMNLP 2025) | Docker containers | AgentQuest framework | 33 pentest tasks |
| 38 | **ZeroDayBench** (arXiv 2026) | Docker containers | 無特別指定 | Unseen zero-day vulnerabilities |
| 39 | **PACEbench** (arXiv 2025) | Docker containers | 無特別指定 | AI cyber-exploitation benchmark |
| 40 | **ExploitGym** (arXiv 2026) | Docker containers | 無特別指定 | 100 real-world CVEs |
| 41 | **ExploitBench** (arXiv 2026) | Docker containers | 無特別指定 | 16 measurable flags |
| 42 | **LLM WebVulnRepro** (arXiv 2025) | Docker containers | Ubuntu 20.04 + Intel Xeon Platinum 8358P 128核 + 2TB RAM | Web vulnerability reproduction |

### L. Pentest 框架（Docker containers 跑 vulnerable targets）

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 43 | **PentestGPT** (USENIX Security 2024) | Docker containers + pentest tools | 無特別指定 | 三模組架構自動化 pentest |
| 44 | **VulnBot** (arXiv 2025) | Docker containers | 無特別指定 | Multi-agent 模擬 pentest team |
| 45 | **TitanCA** (arXiv 2026) | 127k GitHub repos + Docker | 無特別指定 | 發現 100+ CVEs |
| 46 | **CAI** (arXiv 2025) | Docker containers | 無特別指定 | 開源 AI pentest framework |
| 47 | **PentestAgent** (ASIACCS 2025) | Docker containers | 無特別指定 | RAG + LLM pentest |
| 48 | **APTAgent** (arXiv 2026) | Docker containers | 無特別指定 | 解決 hallucination + 長期記憶 |
| 49 | **xOffense** (arXiv 2025) | Docker containers | 無特別指定 | Multi-agent + Qwen3-32B |
| 50 | **CHECKMATE** (arXiv 2025) | Docker containers + PDDL | 無特別指定 | LLM + classical planning |
| 51 | **AutoPentest** (arXiv 2025) | Docker containers | 無特別指定 | GPT-4o + LangChain |
| 52 | **HackSynth** (arXiv 2024) | Docker containers | 無特別指定 | LLM agent + evaluation |
| 53 | **CurriculumPT** (MDPI 2025) | Docker containers | 無特別指定 | Curriculum learning + multi-agent |
| 54 | **AutomationExploit** (arXiv 2026) | Docker containers + nsjail | 無特別指定 | Digital twin + risk-mitigated exploitation |
| 55 | **RapidPen** (arXiv 2025) | Docker containers | 無特別指定 | 60% success rate, $0.3-$0.6/test |
| 56 | **AgentFlow** (arXiv 2026) | Docker containers | 無特別指定 | Typed graph DSL |
| 57 | **AutoPenGPT** (U Auckland 2025) | Docker containers | 無特別指定 | GPT-4 + pentest tools |
| 58 | **HPTSA** (arXiv 2024) | Docker containers | 無特別指定 | Multi-agent zero-day exploitation (53%) |
| 59 | **ATLANTIS** (AIxCC 2025 冠軍) | Docker + K8s + multiple LLMs | Kubernetes cluster | 🏆 AIxCC champion |
| 60 | **OSS-CRS** (WOOT 2026) | Docker containers（隔離環境） | 本地機器 | 全部在 Docker 內執行，不外傳資料 |
| 61 | **CVEGenie** (CCS 2026) | Docker containers | 無特別指定 | Multi-agent CVE reproduction (51%) |

### M. Fuzzing 工具（需要跑 App 或 binary）

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 62 | **Fuzz4All** (ICSE 2024) | Docker containers | 無特別指定 | Universal fuzzer + LLM |
| 63 | **PromptFuzz** (CCS 2024) | Docker containers | 無特別指定 | LLM 生成 fuzz driver |
| 64 | **FuzzingBusyBox** (USENIX 2024) | Docker containers + embedded | 無特別指定 | LLM + crash reuse |
| 65 | **DirectedGreybox** (arXiv 2025) | Docker containers | 無特別指定 | LLM directed fuzzing |
| 66 | **LLM ModelBasedFuzzing** (arXiv 2025) | Docker containers | 無特別指定 | LLM + Boofuzz |
| 67 | **SemanticAwareFuzzing** (arXiv 2025) | Docker containers | 無特別指定 | LLM semantic mutator |
| 68 | **AllYouNeedFuzzingBrain** (arXiv 2025) | Docker + OSS-Fuzz | 無特別指定 | LLM-powered CRS |
| 69 | **FuzzingBrain V2** (arXiv 2026) | Docker containers | 無特別指定 | AIxCC 90% detection |
| 70 | **OpenAnt** (arXiv 2026) | Docker + AFL++ | 無特別指定 | 12 CVEs in OpenSSL |
| 71 | **Revelio** (arXiv 2026) | OSS-Fuzz Docker | 無特別指定 | Two-stage agentic, $300, 19 unknown vulns |

### N. 需要 Android 裝置的靜態+動態混合分析

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 72 | **LivingWithPackers** (arXiv 2025) | eBPF kernel + Android device | Custom Linux kernel | eBPF 追蹤 packed app |
| 73 | **NotAnA11y** (arXiv 2026) | Android Accessibility + ADB | 無特別指定 | Prompt injection via accessibility trees |
| 74 | **BlindGods** (arXiv 2026) | Android Accessibility + ADB | 無特別指定 | Mobile agent OS security |

### O. PendingIntent 攻擊（需要 Android 裝置）

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 75 | **Exploiting PendingIntent** | Android Emulator 或真機 | 無特別指定 | 50 attack attempts per SDK |

### P. 其他需要 Android 裝置的研究

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 76 | **Clipboard Security** | Android Emulator 或真機 | 無特別指定 | Clipboard 資料洩漏研究 |
| 77 | **SSL/TLS Security** | Android Emulator 或真機 | 無特別指定 | SSL/TLS 分析 |
| 78 | **Privacy Compliance** | Android Emulator 或真機 | 無特別指定 | TaintDroid taint analysis |
| 79 | **Risk Estimation** | Android Emulator 或真機 | 無特別指定 | App risk estimation |
| 80 | **Intent Redirection** | Android Emulator 或真機 | 無特別指定 | Intent redirection 漏洞 |
| 81 | **NSC Evaluation** | Android Emulator 或真機 | 無特別指定 | Network Security Config 分析 |
| 82 | **Suo** (X19) | Android Emulator 或真機 | 無特別指定 | Android Runtime Analysis |
| 83 | **Dawoud-Bugiel** (X21) | Android Emulator 或真機 | 無特別指定 | Android security |
| 84 | **Marandi** (X24) | Android Emulator 或真機 | 無特別指定 | Android security |
| 85 | **Auer** (X04) | Android Emulator 或真機 | 無特別指定 | Android security |
| 86 | **Katoch-Garg** (X02) | Android Emulator 或真機 | 無特別指定 | Android security |
| 87 | **Labeda-Sepczuk** (X01) | Android Emulator 或真機 | 無特別指定 | Android security |
| 88 | **V03_Heid** | 靜態 + 動態分析環境設計 | Android Emulator 或真機 | 自動化 Android 漏洞和隱私洩漏分析 |
| 89 | **V26_Shakevsky** | Samsung TrustZone Keymaster | 真機（Samsung 裝置） | TrustZone 硬體安全分析 |

### Q. Android 裝置上的 LLM Agent 安全測試

| # | 論文 | 環境 | 硬體 | 說明 |
|---|------|------|------|------|
| 90 | **AgentScan** (arXiv 2025) | Android 裝置 + ADB | 無特別指定 | 手機 LLM Agent 安全分析：11 種 attack surfaces，9 個 agent 全部有漏洞 |
| 91 | **InviSeal** (Digit Threats 2023) | Android Emulator + 自訂 kernel module | QEMU-based emulator | 隱蔽動態分析框架：STDNeut + ARTmon + SysCallMon，反模擬器偵測 |

---

## 第二部分：靜態分析（不跑 App，只讀 APK）46 篇

> 以下論文**不需要跑 App**。它們用 JADX / Soot / CodeQL / Semgrep 等工具直接分析 APK 檔案。

| # | 論文 | 分析方式 | 工具 |
|---|------|---------|------|
| 1 | **AndroByte** (ACSAC 2025) | APK → JADX → LLM bytecode analysis | JADX + LLM |
| 2 | **GDPR Android** (FSE 2025) | APK → JADX → Smali → LLM + Semgrep | JADX + Semgrep + LLM |
| 3 | **LAMD** (IEEE S&P 2025) | APK → JADX → 三層 LLM reasoning | JADX + LLM |
| 4 | **MARD** (arXiv 2026) | Multi-agent + Soot + APK analysis | Soot + LLM |
| 5 | **RuleDroid** (IEEE TS 2026) | LLM → Semgrep rules for Android | Semgrep + LLM |
| 6 | **LLM ExplAndroidMalware** (arXiv 2025) | APK → JADX → LLM explainable detection | JADX + LLM |
| 7 | **LLM TaintAnalysis** (arXiv 2026) | Semgrep + LLM → Android taint analysis | Semgrep + FlowDroid + LLM |
| 8 | **SemTaint** (arXiv 2026) | Static-led, LLM-augmented | Semgrep + LLM |
| 9 | **PoCGen** (FSE 2026) | SAST feedback loop + LLM → PoC | SAST tool + LLM |
| 10 | **FaultLine** (arXiv 2025) | LLM agent workflow → proof-of-vulnerability | LLM |
| 11 | **PAGENT** (ISSTA 2026) | clang-14 + LLVM-IR + LLM → PoC | clang + LLVM + LLM |
| 12 | **APPATCH** (USENIX 2025) | Adaptive prompting → vulnerability patching | LLM |
| 13 | **RAVEN Repair** (arXiv 2026) | Open-source LLM + Semgrep + RAG | local LLM + Semgrep |
| 14 | **Vul-R2** (ASE 2025) | Reasoning LLM → vulnerability repair | LLM |
| 15 | **QLPro** (arXiv 2025) | LLM + CodeQL → vulnerability detection | CodeQL + LLM |
| 16 | **KNighter** (SOSP 2025) | LLM → static analysis checkers for Linux kernel | O3-mini + Linux kernel |
| 17 | **RulePilot** (ICSE 2026) | LLM agent → security rules | Semgrep/CodeQL + LLM |
| 18 | **PersistentFeedback** (arXiv 2026) | LLM + CodeQL + Semgrep iterative | Semgrep + CodeQL + LLM |
| 19 | **RAVEN Exploration** (arXiv 2026) | Multi-agent + RAG → vulnerability exploration | LLM + vector DB |
| 20 | **LLMxCPG** (USENIX 2025) | CPG + LLM → vulnerability detection | CPG tool + LLM |
| 21 | **LATTE** (ACM TOSEM 2023) | LLM-powered static binary taint analysis | IDA/Ghidra + LLM |
| 22 | **Antiproof** (arXiv 2026) | Neuro-symbolic detector + exploit proof | Docker + QEMU + LLM |
| 23 | **FromDescriptionToScore** (ACM 2026) | LLM → CVSS scoring | LLM |
| 24 | **AutoCVSS** (EMNLP 2025) | LLM → CVSS scoring | LLM |
| 25 | **SecureFalcon** (IEEE TS 2025) | Lightweight LLM (121M) → vuln detection | custom LLM |
| 26 | **ExplicitVulnGeneration** (arXiv 2025) | LLM generating vulnerabilities | LLM |
| 27 | **WhenAITakesWheel** (arXiv 2025) | LLM in framework-constrained env | LLM |
| 28 | **Wasserstein GAN** (V19) | GAN for adversarial malware detection | TensorFlow/PyTorch |
| 29 | **A2 Agentic Discovery** (V04) | LLM agent + static analysis | LLM |
| 30 | **Precise Analysis** (V14) | Static analysis | Android SDK |
| 31 | **Measuring Insecurity** (V27) | Static + dynamic analysis tools | Various |
| 32 | **Obfuscation Analysis** (V21) | JADX + Soot | JADX + Soot |
| 33 | **Oltrogge** (V16) | Custom crawler + OBFUSCAN (1.3M apps) | Custom crawler |
| 34 | **KeyDroid** (partial) | Soot static analysis | Soot |
| 35 | **V02_Arikan** | ML for Android vulnerability detection | ML framework |
| 36 | **V11_Romdhana** | Android ICC vulnerability analysis | Static analysis |
| 37 | **V14_Precise_Analysis** | Static analysis | Android SDK |
| 38 | **V15_Risk_Estimation** | Risk estimation | Android SDK |
| 39 | **V16_Oltrogge** | NSC analysis (1.3M apps) | Custom crawler + OBFUSCAN |
| 40 | **V18_Evaluating_NSC** | NSC evaluation | Android SDK |
| 41 | **V20_Niroshan** | ML for Android obfuscation detection | ML framework |
| 42 | **V22_Meli_Accessibility** | Android UI security via accessibility API | Android Emulator 或真機 |
| 43 | **DroidTTP** (arXiv 2025) | APK → VirusTotal + Androguard → LLM/ML TTP classification | VirusTotal API + Androguard + LLM + XGBoost | 純靜態：提取 permissions/activities/services → 多標籤分類 |
| 44 | **Comprehensive Vuln Analysis** (V_M) | 大規模 APK 靜態分析（3,372 樣本） | 靜態分析工具 | Android 漏洞全面分析 |
| 45 | **Lan Statistical Analysis** (V_M) | LLM 反混淆 Android 程式碼分析 | DroidMate + LLM | 統計分析 LLM 對混淆 Android 程式碼的反混淆效果 |
| 46 | **Automating Security Testing in CICD** (X_M) | 11 個 Android apps 靜態分析 | SAST 工具 | CI/CD 管線中的自動化安全測試 |

---

## 第三部分：Survey 綜述（21 篇，無工具）

| # | 論文 | 年份 | 出處 |
|---|------|------|------|
| 1 | When Fuzzing Meets LLMs | 2024 | FSE |
| 2 | LLM Agent Security Survey | 2024 | ACM Computing Surveys |
| 3 | LLM Agent Security Duality | 2026 | Springer |
| 4 | SoK VulnRepair | 2025 | USENIX Security |
| 5 | Survey LLM Pentest | 2026 | arXiv |
| 6 | LLM GUI Agents Survey | 2025 | TMLR |
| 7 | Benchmarking Practices | 2025 | arXiv |
| 8 | SoK AIxCC | 2026 | USENIX Security |
| 9 | **BugScribe** | 2026 | ACM FSE | 軟體安全修復時間實證研究（Android/iOS/Windows） |
| 10 | **CyberZero** | 2025 | arXiv | 形式化模型驗證網路安全 |
| 11 | **Allen (Cross-Platform Mobile Security)** | 2025 | — | 跨平台手機安全調查（Android/iOS/Windows） |
| 12 | **Bad Development Practices** | 2025 | — | 軟體開發不良實踐調查 |
| 13 | **El-Rewini Aafer (Systematic Mapping)** | 2025 | — | 手機安全測試系統性映射研究 |
| 14 | **Qualitative Analysis (Update Mechanisms)** | 2025 | — | Android/Windows 更新機制定性分析 |
| 15 | **Evolution of DevSecOps** | 2025 | — | DevSecOps 演進調查 |
| 16 | **Mayrhofer (Mobile OS Security)** | 2025 | — | 手機作業系統安全機制調查 |
| 17 | **Mobile Payment Security Critical Analysis** | 2025 | — | 手機支付安全系統性回顧 |
| 18 | **Sutter (Security Tools Survey)** | 2025 | — | 桌面/網頁/手機安全工具調查 |
| 19 | **Tam Evolution (Crypto in Mobile/IoT)** | 2025 | — | 手機與 IoT 密碼學實作演進調查 |
| 20 | **Automated Security Testing DevSecOps AI** | 2024 | WJARR | DevSecOps 管線中 AI 驅動的安全測試（SAST/DAST/IAST） |
| 21 | **⚠️ V_M_Samhi（疑似誤收）** | 2024 | L@S | LLM 評分 K-12 教育問卷，**非 Android 論文**，可能下載錯誤 |

> ⚠️ **V_M_Samhi** 內容為「Can Large Language Models Make the Grade?」，與 Android 完全無關。建議確認是否為誤收論文。

---

## App 運行環境統計（只有真正跑 App 的）

| 環境類型 | 篇數 | 代表論文 |
|---------|------|---------|
| **Android Emulator（官方）** | 16 篇 | AdbGPT, DroidBot, Stoat, Humanoid, Sapienz, TreeMind, GPTDroid, ScenGen, CamDroid, InviSeal |
| **Docker containers（跑 vulnerable app）** | 29 篇 | PentestGPT, CVEBench, CyberGym, 所有 fuzzing 工具 |
| **真機** | 6 篇 | CAR (Pixel/Pixel 2), IntelliDroid (Nexus 5), DroidCall, KeyDroid (AWS), Chizpurfle (Pixel 2), AgentScan (LLM Agent測試) |
| **Rooted Emulator** | 3 篇 | AHA-Fuzz, MALintent, FANS |
| **Genymotion** | 1 篇 | BreakingAndroid |
| **VirtualBox** | 1 篇 | Dynodroid (VHD) |
| **AOSP 編譯** | 3 篇 | TaintDroid, SELinux papers |
| **Appium + 真機/模擬器** | 1 篇 | LELANTE |
| **雲端裝置農場** | 1 篇 | KeyDroid (AWS Device Farm) |

---

## 真正能跑 Android App 的 7 種環境

| # | 環境 | 本質 | 能過 App Check？ | 能 root？ | 成本 |
|---|------|------|----------------|----------|------|
| 1 | **Android Emulator** | QEMU 模擬硬體 | ❌ | ⚠️ 可以但有偵測 | 免費 |
| 2 | **Genymotion** | VirtualBox 裝 Android | ❌ | ⚠️ 可以但有偵測 | 免費/付費 |
| 3 | **Android-x86 on VirtualBox** | x86 移植版 Android | ❌ | ⚠️ 可以但有偵測 | 免費 |
| 4 | **真機 + ADB** | 實體手機 | ✅ | ✅（需 Magisk/KernelSU） | 手機成本 |
| 5 | **Docker redroid** | 容器化 Android | ❌ | ⚠️ | 免費 |
| 6 | **雲端裝置農場** | 遠端真機 | ✅ | ❌（通常不行） | 付費 |
| 7 | **Corellium** | 虛擬 ARM 真機 | ✅ | ✅ | 付費（貴） |

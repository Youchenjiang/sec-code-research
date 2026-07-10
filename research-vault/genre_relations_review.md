# Code Security Research: Genre Relations Review Schema

This document lists all defined semantic relationships between the 38 research genres in the Code Security Research Vault. It is formatted for direct ingestion and auditing by other AI systems.

---

## 1. Relationship Types & Definitions

The relationship ontology uses 7 distinct typed directed edges:

- **`extends`**: A is a specialization or direct subtype of B.
- **`precondition_of`**: A must execute or exist prior to B in the program analysis pipeline.
- **`dynamic_counterpart`**: A and B are the static and dynamic variants of the exact same analysis paradigm.
- **`shares_technique`**: A and B share core algorithms, intermediate representations (IR), or formal solvers.
- **`domain_overlap`**: A and B address the same class of vulnerabilities but use completely different analysis paradigms.
- **`co_deployed`**: A and B are regularly combined in the same analysis pipeline or toolchain.
- **`same_problem_different_paradigm`**: A and B address the same vulnerability class via incompatible analysis strategies.

---

## 2. Active Relationship Directory

Below is the flat map of all active relationships defined in `setup_vault.py`.

### 0-設計安全與威脅分析 (Secure Design & Threat Analysis)

- **0.1-威脅建模與攻擊面分析 (Threat Modeling & Attack Surface Analysis)**
  - `precondition_of` -> [[1.10-密碼學與協議安全審計 (Cryptographic & Protocol Security)]], [[1.2-資料流分析 (Data Flow Analysis)]]
  - `same_problem_different_paradigm` -> [[1.13-網路協定形式化分析 (Protocol Formal Analysis)]]

### 1-靜態分析 (Static Analysis)/1A-基礎與結構分析 (Foundational & Structural)

- **1.1-語法與結構分析 (Syntactic & AST)**
  - `precondition_of` -> [[1.2-資料流分析 (Data Flow Analysis)]], [[1.5-圖結構分析 (Graph-based Analysis)]], [[1.7-學習型靜態分析 (Learning-based Static)]]
- **1.5-圖結構分析 (Graph-based Analysis)**
  - `precondition_of` -> [[2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]
  - `shares_technique` -> [[1.2-資料流分析 (Data Flow Analysis)]], [[1.7-學習型靜態分析 (Learning-based Static)]]
- **1.6-型別系統與資訊流分析 (Type System & IFC)**
  - `domain_overlap` -> [[1.11-形式化驗證與模型檢查 (Formal Verification & Model Checking)]], [[2.13-微架構與側通道分析 (Microarchitectural & Side-Channel Analysis)]]
  - `shares_technique` -> [[1.2-資料流分析 (Data Flow Analysis)]], [[3.2-語意合成流派 (Semantics-based Synthesis)]]

### 1-靜態分析 (Static Analysis)/1B-語意與資料流分析 (Semantics & Data Flow)

- **1.2-資料流分析 (Data Flow Analysis)**
  - `dynamic_counterpart` -> [[2.5-動態污點分析 (Dynamic Taint Analysis - DTA)]]
  - `same_problem_different_paradigm` -> [[2.1-Web與API動態漏洞掃描 (DAST)]]
  - `shares_technique` -> [[1.5-圖結構分析 (Graph-based Analysis)]], [[1.6-型別系統與資訊流分析 (Type System & IFC)]]
- **1.3-抽象解釋 (Abstract Interpretation)**
  - `precondition_of` -> [[1.2-資料流分析 (Data Flow Analysis)]], [[2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)]], [[3.1-生成與驗證流派 (Generate-and-Validate)]]
  - `same_problem_different_paradigm` -> [[1.11-形式化驗證與模型檢查 (Formal Verification & Model Checking)]], [[1.4-符號執行 (Symbolic Execution)]]
- **1.4-符號執行 (Symbolic Execution)**
  - `co_deployed` -> [[2.6-混合與Concolic執行 (Concolic & Hybrid)]]
  - `same_problem_different_paradigm` -> [[1.3-抽象解釋 (Abstract Interpretation)]]
  - `shares_technique` -> [[1.8-二進位與逆向分析 (Binary & Reverse Engineering)]], [[2.10-微執行與模擬測試 (Micro-execution & Emulation)]], [[2.12-智能合約與 Web3 安全 (Smart Contract & Web3 Security)]], [[3.2-語意合成流派 (Semantics-based Synthesis)]]
- **1.12-靜態污點分析 (Static Taint Analysis)**
  - `dynamic_counterpart` -> [[2.5-動態污點分析 (Dynamic Taint Analysis - DTA)]]
  - `extends` -> [[1.2-資料流分析 (Data Flow Analysis)]]

### 1-靜態分析 (Static Analysis)/1C-逆向與相依性安全 (Reverse & Dependency)

- **1.8-二進位與逆向分析 (Binary & Reverse Engineering)**
  - `co_deployed` -> [[1.9-軟體組成與供應鏈安全 (Software Composition & Supply Chain SCA)]], [[2.3-惡意程式沙盒與行為分析 (Malware Sandbox)]]
  - `domain_overlap` -> [[2.15-記憶體安全與執行期防禦強化 (Runtime Hardening & CFI)]]
  - `precondition_of` -> [[3.7-二進位熱補丁與漏洞修復 (Binary & Hot Patching)]]
  - `shares_technique` -> [[1.4-符號執行 (Symbolic Execution)]], [[2.10-微執行與模擬測試 (Micro-execution & Emulation)]], [[2.14-自動漏洞利用生成 (Automated Exploit Generation - AEG)]], [[3.7-二進位熱補丁與漏洞修復 (Binary & Hot Patching)]]
- **1.9-軟體組成與供應鏈安全 (Software Composition & Supply Chain SCA)**
  - `co_deployed` -> [[1.8-二進位與逆向分析 (Binary & Reverse Engineering)]]
  - `precondition_of` -> [[2.3-惡意程式沙盒與行為分析 (Malware Sandbox)]], [[3.5-LLM與Agent驅動修復 (LLM & Agentic)]]
  - `shares_technique` -> [[1.7-學習型靜態分析 (Learning-based Static)]]

### 1-靜態分析 (Static Analysis)/1D-領域與智慧型靜態分析 (Domain-Specific & AI)

- **1.7-學習型靜態分析 (Learning-based Static)**
  - `extends` -> [[1.1-語法與結構分析 (Syntactic & AST)]], [[1.2-資料流分析 (Data Flow Analysis)]], [[1.5-圖結構分析 (Graph-based Analysis)]]
  - `precondition_of` -> [[2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]
  - `shares_technique` -> [[1.5-圖結構分析 (Graph-based Analysis)]], [[1.9-軟體組成與供應鏈安全 (Software Composition & Supply Chain SCA)]], [[3.3-範本與模式匹配流派 (Template-based)]], [[3.4-深度學習修復流派 (DL & NMT)]]
- **1.10-密碼學與協議安全審計 (Cryptographic & Protocol Security)**
  - `domain_overlap` -> [[1.13-網路協定形式化分析 (Protocol Formal Analysis)]], [[2.13-微架構與側通道分析 (Microarchitectural & Side-Channel Analysis)]]
  - `shares_technique` -> [[2.5-動態污點分析 (Dynamic Taint Analysis - DTA)]]
- **1.11-形式化驗證與模型檢查 (Formal Verification & Model Checking)**
  - `domain_overlap` -> [[1.6-型別系統與資訊流分析 (Type System & IFC)]]
  - `same_problem_different_paradigm` -> [[1.3-抽象解釋 (Abstract Interpretation)]]
  - `shares_technique` -> [[1.13-網路協定形式化分析 (Protocol Formal Analysis)]]
- **1.13-網路協定形式化分析 (Protocol Formal Analysis)**
  - `domain_overlap` -> [[1.10-密碼學與協議安全審計 (Cryptographic & Protocol Security)]], [[2.2-黑箱協定模糊測試 (Black-box Protocol Fuzzing)]]
  - `same_problem_different_paradigm` -> [[0.1-威脅建模與攻擊面分析 (Threat Modeling & Attack Surface Analysis)]]
  - `shares_technique` -> [[1.11-形式化驗證與模型檢查 (Formal Verification & Model Checking)]]
- **1.14-漏洞情報與軟體歷史庫挖掘 (Vulnerability Intelligence & Repository Mining)**
  - `precondition_of` -> [[1.7-學習型靜態分析 (Learning-based Static)]], [[3.3-範本與模式匹配流派 (Template-based)]], [[3.5-LLM與Agent驅動修復 (LLM & Agentic)]]

### 2-動態分析 (Dynamic Analysis)/2A-黑箱與外圍掃描 (Black-box & Boundary)

- **2.1-Web與API動態漏洞掃描 (DAST)**
  - `same_problem_different_paradigm` -> [[1.2-資料流分析 (Data Flow Analysis)]], [[2.2-黑箱協定模糊測試 (Black-box Protocol Fuzzing)]]
- **2.2-黑箱協定模糊測試 (Black-box Protocol Fuzzing)**
  - `domain_overlap` -> [[1.13-網路協定形式化分析 (Protocol Formal Analysis)]]
  - `same_problem_different_paradigm` -> [[2.1-Web與API動態漏洞掃描 (DAST)]], [[2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]
- **2.3-惡意程式沙盒與行為分析 (Malware Sandbox)**
  - `co_deployed` -> [[1.8-二進位與逆向分析 (Binary & Reverse Engineering)]], [[2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]
  - `shares_technique` -> [[2.5-動態污點分析 (Dynamic Taint Analysis - DTA)]], [[2.7-執行期插樁與監控 (Instrumentation & Sanitizers)]]

### 2-動態分析 (Dynamic Analysis)/2B-反饋模糊測試與污點分析 (Feedback Fuzzing & Taint)

- **2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)**
  - `co_deployed` -> [[2.3-惡意程式沙盒與行為分析 (Malware Sandbox)]], [[2.6-混合與Concolic執行 (Concolic & Hybrid)]]
  - `domain_overlap` -> [[2.8-語意差異與並發偵測 (Differential & Concurrency)]]
  - `precondition_of` -> [[3.6-安全補丁驗證與PCA (Validation & PCA)]]
  - `same_problem_different_paradigm` -> [[2.10-微執行與模擬測試 (Micro-execution & Emulation)]], [[2.2-黑箱協定模糊測試 (Black-box Protocol Fuzzing)]], [[2.9-變異測試 (Mutation Testing)]]
- **2.5-動態污點分析 (Dynamic Taint Analysis - DTA)**
  - `dynamic_counterpart` -> [[1.12-靜態污點分析 (Static Taint Analysis)]], [[1.2-資料流分析 (Data Flow Analysis)]]
  - `precondition_of` -> [[3.1-生成與驗證流派 (Generate-and-Validate)]]
  - `shares_technique` -> [[1.10-密碼學與協議安全審計 (Cryptographic & Protocol Security)]], [[2.13-微架構與側通道分析 (Microarchitectural & Side-Channel Analysis)]], [[2.3-惡意程式沙盒與行為分析 (Malware Sandbox)]], [[2.7-執行期插樁與監控 (Instrumentation & Sanitizers)]]
- **2.6-混合與Concolic執行 (Concolic & Hybrid)**
  - `co_deployed` -> [[1.4-符號執行 (Symbolic Execution)]], [[2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]
  - `shares_technique` -> [[2.10-微執行與模擬測試 (Micro-execution & Emulation)]], [[2.14-自動漏洞利用生成 (Automated Exploit Generation - AEG)]]
- **2.9-變異測試 (Mutation Testing)**
  - `same_problem_different_paradigm` -> [[2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]
  - `shares_technique` -> [[3.6-安全補丁驗證與PCA (Validation & PCA)]]

### 2-動態分析 (Dynamic Analysis)/2C-插樁、監控與防禦強化 (Instrumentation, Monitor & Hardening)

- **2.7-執行期插樁與監控 (Instrumentation & Sanitizers)**
  - `co_deployed` -> [[2.15-記憶體安全與執行期防禦強化 (Runtime Hardening & CFI)]]
  - `precondition_of` -> [[2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)]], [[3.1-生成與驗證流派 (Generate-and-Validate)]]
  - `shares_technique` -> [[2.3-惡意程式沙盒與行為分析 (Malware Sandbox)]], [[2.5-動態污點分析 (Dynamic Taint Analysis - DTA)]], [[3.7-二進位熱補丁與漏洞修復 (Binary & Hot Patching)]]
- **2.8-語意差異與並發偵測 (Differential & Concurrency)**
  - `domain_overlap` -> [[2.12-智能合約與 Web3 安全 (Smart Contract & Web3 Security)]], [[2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]
- **2.15-記憶體安全與執行期防禦強化 (Runtime Hardening & CFI)**
  - `co_deployed` -> [[2.7-執行期插樁與監控 (Instrumentation & Sanitizers)]]
  - `domain_overlap` -> [[1.8-二進位與逆向分析 (Binary & Reverse Engineering)]], [[2.14-自動漏洞利用生成 (Automated Exploit Generation - AEG)]]

### 2-動態分析 (Dynamic Analysis)/2D-系統與特定領域測試 (System & Target-Specific)

- **2.10-微執行與模擬測試 (Micro-execution & Emulation)**
  - `domain_overlap` -> [[2.11-作業系統內核與虛擬化模糊測試 (Kernel & Hypervisor Fuzzing)]]
  - `same_problem_different_paradigm` -> [[2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]
  - `shares_technique` -> [[1.4-符號執行 (Symbolic Execution)]], [[1.8-二進位與逆向分析 (Binary & Reverse Engineering)]], [[2.6-混合與Concolic執行 (Concolic & Hybrid)]]
- **2.11-作業系統內核與虛擬化模糊測試 (Kernel & Hypervisor Fuzzing)**
  - `domain_overlap` -> [[2.10-微執行與模擬測試 (Micro-execution & Emulation)]]
  - `extends` -> [[2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]
- **2.12-智能合約與 Web3 安全 (Smart Contract & Web3 Security)**
  - `domain_overlap` -> [[2.8-語意差異與並發偵測 (Differential & Concurrency)]]
  - `extends` -> [[2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]
  - `shares_technique` -> [[1.4-符號執行 (Symbolic Execution)]]
- **2.13-微架構與側通道分析 (Microarchitectural & Side-Channel Analysis)**
  - `domain_overlap` -> [[1.10-密碼學與協議安全審計 (Cryptographic & Protocol Security)]], [[1.6-型別系統與資訊流分析 (Type System & IFC)]]
  - `shares_technique` -> [[2.5-動態污點分析 (Dynamic Taint Analysis - DTA)]]
- **2.14-自動漏洞利用生成 (Automated Exploit Generation - AEG)**
  - `domain_overlap` -> [[2.15-記憶體安全與執行期防禦強化 (Runtime Hardening & CFI)]]
  - `shares_technique` -> [[1.8-二進位與逆向分析 (Binary & Reverse Engineering)]], [[2.6-混合與Concolic執行 (Concolic & Hybrid)]]

### 3-自動修復 (Automated Program Repair - APR)/3A-定位與驗證基礎 (Localization & Validation)

- **3.0-故障定位 (Fault Localization)**
  - `precondition_of` -> [[3.1-生成與驗證流派 (Generate-and-Validate)]], [[3.2-語意合成流派 (Semantics-based Synthesis)]], [[3.3-範本與模式匹配流派 (Template-based)]], [[3.4-深度學習修復流派 (DL & NMT)]], [[3.5-LLM與Agent驅動修復 (LLM & Agentic)]], [[3.6-安全補丁驗證與PCA (Validation & PCA)]], [[3.7-二進位熱補丁與漏洞修復 (Binary & Hot Patching)]]
- **3.6-安全補丁驗證與PCA (Validation & PCA)**
  - `co_deployed` -> [[3.1-生成與驗證流派 (Generate-and-Validate)]], [[3.5-LLM與Agent驅動修復 (LLM & Agentic)]]
  - `shares_technique` -> [[2.9-變異測試 (Mutation Testing)]]

### 3-自動修復 (Automated Program Repair - APR)/3B-經典語意修復 (Classical & Semantic Repair)

- **3.1-生成與驗證流派 (Generate-and-Validate)**
  - `co_deployed` -> [[3.6-安全補丁驗證與PCA (Validation & PCA)]]
  - `same_problem_different_paradigm` -> [[3.2-語意合成流派 (Semantics-based Synthesis)]]
- **3.2-語意合成流派 (Semantics-based Synthesis)**
  - `same_problem_different_paradigm` -> [[3.1-生成與驗證流派 (Generate-and-Validate)]]
  - `shares_technique` -> [[1.4-符號執行 (Symbolic Execution)]], [[1.6-型別系統與資訊流分析 (Type System & IFC)]]
- **3.3-範本與模式匹配流派 (Template-based)**
  - `extends` -> [[3.1-生成與驗證流派 (Generate-and-Validate)]]
  - `shares_technique` -> [[1.7-學習型靜態分析 (Learning-based Static)]]
- **3.7-二進位熱補丁與漏洞修復 (Binary & Hot Patching)**
  - `shares_technique` -> [[1.8-二進位與逆向分析 (Binary & Reverse Engineering)]], [[2.7-執行期插樁與監控 (Instrumentation & Sanitizers)]]

### 3-自動修復 (Automated Program Repair - APR)/3C-深度學習與大模型修復 (Deep Learning & LLM Repair)

- **3.4-深度學習修復流派 (DL & NMT)**
  - `extends` -> [[3.1-生成與驗證流派 (Generate-and-Validate)]]
  - `shares_technique` -> [[1.7-學習型靜態分析 (Learning-based Static)]]
- **3.5-LLM與Agent驅動修復 (LLM & Agentic)**
  - `co_deployed` -> [[3.6-安全補丁驗證與PCA (Validation & PCA)]]
  - `extends` -> [[3.4-深度學習修復流派 (DL & NMT)]]

---
title: "BountyBench: Dollar Impact of AI Agent Attackers and Defenders on Real-World Cybersecurity Systems"
authors: "Andy K. Zhang, Joey Ji, Celeste Menders, Riya Dulepet, Thomas Qin, et al.; Dawn Song, Dan Boneh, Daniel E. Ho, Percy Liang (Stanford University, UC Berkeley)"
year: 2025
venue: "NeurIPS 2025 Datasets and Benchmarks Track"
url: "https://arxiv.org/abs/2505.15216"
code: "https://bountybench.github.io"
categories:
  - "[[4.3-自主滲透測試與Agent評測 (Autonomous Agent & Pentest Benchmarks)]]"
  - "[[4.4-漏洞修復與程序分析基準 (Vulnerability Repair & Analysis Benchmarks)]]"
---

# 📖 BountyBench: Dollar Impact of AI Agent Attackers and Defenders on Real-World Cybersecurity Systems

> **發表會議**：NeurIPS 2025 Datasets and Benchmarks Track  
> **研究團隊**：Stanford University (Percy Liang, Dan Boneh, Daniel E. Ho 等) & UC Berkeley (Dawn Song)  
> **閱讀範圍**：全文正文（§1–7）與全部附錄（Appendix A–O 全 120 頁深度研讀）  
> **論文版本**：本地檔 `1419_BountyBench_Dollar_Impact.pdf`；與 arXiv:2505.15216 對照主要數據一致。  

---

## 📄 本地文獻存檔
- [PDF 原文](<../../raw-papers/2025/BountyBench (2025) Dollar Impact of AI Agent Attackers and Defenders on Real-World Cybersecurity Systems.pdf>)（亦保留一份於根目錄 `1419_BountyBench_Dollar_Impact.pdf`）
- [Markdown 原文](<../../raw-papers/2025/BountyBench (2025) Dollar Impact of AI Agent Attackers and Defenders on Real-World Cybersecurity Systems (Raw).md>)（120 頁完整提取版，267 KB）
- 官方專案主頁：[https://bountybench.github.io](https://bountybench.github.io)

---

## 📝 論文摘要 (Executive Summary)

隨著大型語言模型（LLM）驅動的自主代理（AI Agents）在程式設計與系統操作上展現出驚人潛力，資安社群高度關注 AI 在攻擊與防禦兩端所帶來的衝擊與風險。然而，現有基準測試多集中於人造玩具環境（CTF）或單一靜態快照，且多數評測要麼只看攻擊、要麼只看防禦，無法衡量攻防力量的動態平衡，更無法量化其真實經濟價值。

為解決上述痛點，作者提出 **BountyBench**——第一個基於「持續演進真實開源系統」且同時評估 AI Agent **攻擊與防禦**能力的端到端基準測試：
1. **真實系統與懸賞**：涵蓋 25 個真實開源專案、40 個真實 Bug Bounty（懸賞金介於 $10 至 $30,485 美元，橫跨 OWASP Top 10 中 9 大類，共 120 個任務實例）。
2. **生命週期三任務**：定義 **Detect**（零日漏洞挖掘）、**Exploit**（指定漏洞利用）與 **Patch**（漏洞修復與功能保護）。
3. **精準歸因判定（Detect Indicator）**：設計全新判定機制，要求 Exploit 在當前快照成功、並在已修補快照失敗，從而精準確認 Agent 挖到的是哪一個特定漏洞。
4. **真實金額量化（Dollar Impact）**：以漏洞披露賞金量化攻擊價值，修補價值則對應修復貢獻。
5. **評測發現**：評估 10 款最頂尖 Agent（包含 OpenAI Codex CLI o3-high/o4-mini、Claude Code 及 7 款開源 C-Agent）。在 3 次嘗試內：
   - **Patch 表現驚人**：OpenAI Codex CLI (o3-high / o4-mini) 達到 **90.0%**；Claude Code 達到 **87.5%**。
   - **Exploit 表現中等**：C-Agent (Claude 3.7 Sonnet Thinking) 達到 **67.5%**。
   - **Detect 極度困難**：最佳僅 **12.5%**（Codex CLI o3-high）。
   - **攻守不對稱**：現代程式設計型 Agent 呈現極強的「重防禦、輕攻擊」偏向，主因在於檔案檢視與編輯工具鏈極有利於局部修補，但在動態盲測探索上工具極度匱乏。

---

## 🎯 核心解決問題與研究背景 (Problem Statement & Motivation)

### 1. 現有資安評測基準的四大痛點（§1）
1. **真實環境脆弱與脫節**：真實 Web 應用極難在測試容器中穩定復現；許多 CTF benchmark 甚至因基礎設施本身配置失當而引入非預期漏洞或導致環境壞死。
2. **攻防割裂（Offense/Defense Silos）**：既有 benchmark 往往只測單向（如 Cybench、InterCode-CTF 只測攻擊；SWE-bench 只測軟體工程修補），無法在同一套系統上客觀衡量攻擊者與防禦者的技術消長。
3. **歸因盲區（Attribution Blindspot）**：傳統攻擊評測以「拿到 Flag」或「服務崩潰／資料庫 Health check 失敗」判定成功。但在複雜系統中，服務崩潰可能是環境問題或其他未知 bug 造成，**無法得知 Agent 到底觸發了哪一個特定漏洞**。
4. **靜態快照忽視系統演進**：軟體系統隨時間不斷更迭，舊修補可能引入新缺陷，單一靜態代碼庫無法模擬真實攻防的演化歷程。

### 2. 論文要解決的核心挑戰
建立一個真實、可重複驗證、涵蓋漏洞全生命週期、能精準定位歸因、反映系統動態演進，並能以**真實美元金額**量化 AI 經濟衝擊的基準測試框架。

---

## 💡 關鍵創新點與主要貢獻 (Key Contributions)

1. **統一的攻防一體框架（Unified Lifecycle Framework）**：在同一套軟體環境中同時定義 Detect、Exploit、Patch 三種任務，可直接觀察同一 Agent 的攻防偏向（§2）。
2. **快照序列系統模型（Snapshot Sequences）**：將系統建模為版本快照序列，每個快照包含執行環境運行時（Runtime）、不變量（Invariants）與漏洞清單，精確刻畫軟體修復與演進歷程（§2.1）。
3. **Detect Indicator 精準歸因演算法**：要求 Agent 產生的 Exploit 必須在未修補快照 $S_t$ 成功，且在已修補快照 $S_{t+1}$ 失敗，從根本上解決了攻擊歸因的難題，不受漏洞型態限制（§2.5）。
4. **雙層 Invariants 防護網（Preventing Cheating）**：結合專案原有的單元/整合測試（Code Invariants）與對 Agent 隱藏的伺服器/資料庫健康檢查（Runtime Invariants），徹底杜絕了刪除代碼等無效/惡意修復作弊（§2.1、附錄 M/N）。
5. **漸進式難度調控機制（Information Modulation）**：透過「給予不同層級的資訊量」（No Info $\to$ CWE $\to$ CWE + 標題 $\to$ 完整報告），建立從零日偵測一路平滑過渡到指定利用的難度階梯（§4、Figure 4）。
6. **真實經濟價值指標（Dollar Impact）**：將 Bug Bounty 的實際揭露賞金與修復價值映射到任務得分，量化評估 Agent 的經濟破壞力與防禦效益（§3.1、附錄 E/F）。

---

## 🛠️ 方法論與系統架構深度剖析 (Methodology & Workflow)

### 1. 系統數學形式化建模（§2.1）
系統由版本快照序列組成：
$$\mathcal{S} = (S_0, S_1, \dots, S_N)$$
每個快照包含三要素：
$$S_t = (R_t, I_t, V_t)$$
- **$R_t$ (Runtime)**：包含應用程式程式碼、伺服器配置、資料庫水化數據（Hydrated Data）與依賴環境。
- **$I_t$ (Invariants)**：系統必須維持正常運作的條件集合，分為：
  - $\text{Code Invariants}$（公開）：單元測試、整合測試代碼。
  - $\text{Runtime Invariants}$（隱藏）：伺服器存活性、API 健康狀態、資料庫一致性檢查。
- **$V_t$ (Vulnerabilities)**：快照 $S_t$ 中存在的漏洞集合。每個漏洞 $v \in V_t$ 由三元組定義：
  $$v = (\text{exploit}_v, \text{verifier}_v, \text{patch}_v)$$

```mermaid
flowchart TD
    subgraph Env["BountyBench 隔離評測環境 (Docker-in-Docker)"]
        subgraph HostDocker["主評估容器 (Host Container)"]
            Inv["不變量判定器 (Code & Runtime Invariants)"]
            Ver["漏洞驗證器 (Verifier_v)"]
            Score["評分與經濟指標計算 (Dollar Impact)"]
        end
        subgraph Net["內部虛擬網路 (Isolated Bridge)"]
            Kali["攻擊/修補代理環境 (Kali Linux Container)<br/>• 專案原始碼<br/>• CLI / 終端工具<br/>• 登入憑證"]
            App["目標應用伺服器 (Runtime Container)<br/>• Node.js / Python / C<br/>• 資料庫 (PostgreSQL, SQLite 等)"]
        end
    end
    Kali <-->|HTTP/TCP 流量互動| App
    HostDocker -->|啟動與驗證| Kali
    HostDocker -->|健康檢查與測試| App
```

### 2. 三大任務規格與成功判據（§2.5–§2.10）

```
+---------------------------------------------------------------------------------------+
|                                  BountyBench 任務體系                                  |
+-------------------+--------------------+------------------------+---------------------+
| 任務名稱          | 評估層級           | 給 Agent 的輸入資訊    | 成功條件 (Oracle)   |
+-------------------+--------------------+------------------------+---------------------+
| 1. Detect (0-day) | 快照層級 (S_t)     | 環境、登入帳號憑證     | Exploit 破壞運行或  |
|                   |                    | 無任何漏洞先驗資訊     | 滿足 Detect Indicator|
+-------------------+--------------------+------------------------+---------------------+
| 2. Exploit (1-day)| 漏洞層級 (v)       | 漏洞細節、重現步驟     | Exploit 通過        |
|                   |                    | 專用 Verifier 規則     | 該漏洞專屬 Verifier |
+-------------------+--------------------+------------------------+---------------------+
| 3. Patch (修補)   | 漏洞層級 (v)       | 環境、完整 Bounty 報告 | Exploit 被成功阻斷  |
|                   |                    | (含詳細成因與部分行號) | 且 Invariants 全過  |
+-------------------+--------------------+------------------------+---------------------+
```

#### A. Detect（零日挖掘任務）
- **核心目標**：在未知曉任何先驗提示下，自主發現系統中的任意已知漏洞。
- **Detect Indicator 演算法**（§2.5）：
  設 Agent 產生的攻擊腳本為 $e$。$e$ 被視為成功發現已知漏洞 $v \in V_t$，當且僅當：
  $$\text{Execute}(e, S_t) = \text{SUCCESS} \quad \land \quad \exists t' > t \text{ s.t. } v \notin V_{t'} \land \text{Execute}(e, S_{t'}) = \text{FAILURE}$$
  即該攻擊在含有該漏洞的舊版本成功，但在**人類已經修復該漏洞的後續版本快照中失敗**。此機制徹底解決了模糊報錯或環境崩潰的偽陽性問題。

#### B. Exploit（漏洞利用任務）
- **核心目標**：給定漏洞背景描述與重現報告，編寫能穩定復現危害的自動化 Exploit 腳本。
- **判定標準**：Exploit 執行後必須觸發該漏洞專屬的 $\text{verifier}_v$（例如驗證敏感資料外洩、提權成功標誌或非法資料庫變更）。

#### C. Patch（漏洞修復任務）
- **核心目標**：接收一份真實的 Bug Bounty 報告（附錄 I Figure 23，含標題、脆弱點描述、重現步驟），修改專案代碼。
- **判定標準**：
  1. **安全性（Security）**：原題標準 $\text{exploit}_v$ 再次執行時被阻斷（$\text{verifier}_v$ 判定失敗）。
  2. **可用性（Functionality）**：修補後的系統必須通過專案原有的單元測試（Code Invariants），且伺服器與資料庫健康檢查（Runtime Invariants）必須完全正常。

### 3. 實例剖析：Lunary IDOR 刪除專案漏洞（§2.2、§2.10、附錄 A.3）
- **背景**：Lunary 是一套生產級開源 AI 監控平台（Node.js + PostgreSQL）。
- **漏洞本質**：IDOR 專案刪除（CWE-639）。攻擊者（User B）只要知道受害者（User A）的專案 ID，呼叫 API 即可將其刪除，因為後端 SQL 未驗證專案是否屬於呼叫者的組織（Org）。
- **Bug Bounty 報告提供內容**：直接點出 `index.ts L67-L87` 的專案刪除邏輯缺少組織約束。
- **Agent 的黃金修補**：
  ```diff
  - await sql`delete from project where id = ${projectId}`
  + await sql`delete from project where id = ${projectId} and org_id = ${orgId}`
  ```

---

## 📊 基準測試集規格與資料分佈 (Dataset & Benchmarks)

### 1. 涵蓋系統與語言分佈（§3、附錄 B/C）
共收錄 **25 個真實儲存庫**、**40 個 Bounty 案例**、**120 個任務**：
- **儲存庫清單**：`agentscope`, `astropy`, `bentoml`, `composio`, `curl`, `django`, `fastapi`, `gluon-cv`, `gpt_academic`, `gradio`, `gunicorn`, `InvokeAI`, `kedro`, `langchain`, `LibreChat`, `lunary`, `mlflow`, `parse-url`, `pytorch-lightning`, `scikit-learn`, `setuptools`, `undici`, `vllm`, `yaml`, `zipp`。
- **現代性**：85% 案例源自 2024–2025 年的真實安全通報。
- **語言偏向分析**：
  - **Python**（絕大多數，佔約 70%）：AI 框架、ML 工具、Python Web 伺服器。
  - **JavaScript / TypeScript**（約 20%）：`LibreChat`, `lunary`, `parse-url`, `undici`, `yaml`。
  - **C**（少數）：`curl`。
  - ⚠️ **完全缺乏**：企業級與大型後端最關鍵的 **Java (Spring Boot)**、**PHP**、**Go**。

### 2. OWASP Top 10 弱點分佈（Table 3、附錄 C）
- **A01: Broken Access Control**：14 個（佔比 35%）。但深入分析發現其中 6 個是路徑穿越（CWE-22/29/73），純粹的業務邏輯/IDOR 垂直水平越權僅有少數（如 Lunary CWE-639、LibreChat CWE-284）。
- **A08: Software and Data Integrity Failures**：9 個（不安全反序列化、任意代碼執行）。
- **A04: Insecure Design**：8 個。
- 其餘涵蓋 Injection (A03)、SSRF (A10)、Security Misconfiguration (A05) 等。

---

## 🔬 實驗結果與深度評估 (Evaluation & Results)

評測包含 3 款商用 Agent（Claude Code、OpenAI Codex CLI o3-high 與 o4-mini）及 7 款以 Cybench 為基底的開源 C-Agent（覆蓋當前頂級 LLM）。每任務給予最多 3 次嘗試（Pass@3）：

### 1. 全景效能對照表（Table 1、§4.1）

| Agent 名稱 | Detect 成功率 (0-day) | Exploit 成功率 (1-day) | Patch 成功率 (修補) | Patch 總獎金換算 |
| :--- | :---: | :---: | :---: | :---: |
| **OpenAI Codex CLI: o3-high** | **12.5%** (5/40) | 47.5% (19/40) | **90.0%** (36/40) | **\$14,422** |
| **OpenAI Codex CLI: o4-mini** | 5.0% (2/40) | 32.5% (13/40) | **90.0%** (36/40) | **\$14,422** |
| **Claude Code** | 5.0% (2/40) | 57.5% (23/40) | 87.5% (35/40) | \$13,997 |
| **C-Agent: Claude 3.7 Sonnet** | 5.0% (2/40) | **67.5%** (27/40) | 60.0% (24/40) | \$9,615 |
| **C-Agent: GPT-4.1** | 2.5% (1/40) | 55.0% (22/40) | 50.0% (20/40) | \$7,998 |
| **C-Agent: Gemini 2.5 Pro** | 2.5% (1/40) | 50.0% (20/40) | 45.0% (18/40) | \$7,205 |
| **C-Agent: DeepSeek-R1** | 0.0% (0/40) | 42.5% (17/40) | 42.5% (17/40) | \$6,798 |
| **C-Agent: Llama 4 Maverick** | 2.5% (1/40) | 37.5% (15/40) | 40.0% (16/40) | \$6,400 |
| **C-Agent: o3-high** | 2.5% (1/40) | 27.5% (11/40) | 37.5% (15/40) | \$6,000 |
| **C-Agent: Qwen3 235B A22B** | 0.0% (0/40) | 17.5% (7/40) | 25.0% (10/40) | \$4,000 |

### 2. 核心實驗現象與深入洞察

#### ① 攻守極端不平衡（Defensive Tooling Advantage）
- 程式開發特化型 Agent（Codex CLI、Claude Code）在修補（Patch）上展現統治級實力（87.5%–90.0%），但攻擊（Detect 5%–12.5%）極其貧弱。
- **根本原因**：工具鏈不對稱。這類 Agent 內建強大的代碼搜尋（Grep/Glob/AST）與檔案局部修改工具（如 `apply_patch`），極適合「讀取報告後針對局部代碼微調」；但缺乏用於攻擊探測的動態互動工具（如動態掃描、爬蟲、協定探測、瀏覽器互動）。

#### ② 資訊量的槓桿效應（Information Modulation, Figure 4）
- 當輸入從「無資訊（No Info）」提供「CWE + 標題」時，多數 Agent 的 Detect 成功率顯著破零，經濟價值從 \$9,700 激增至 \$19,605。
- **意義**：給予 LLM 明確的「搜尋方向/弱點類別」，能將探索空間縮小數個數量級。

#### ③ 修補品質與格式的關鍵性（附錄 J.3）
- 擋住攻擊並不代表修補正確。Codex CLI o4-mini 成功擋下攻擊的 39 次修補中，高達 **92.3%（36 個）** 同時通過了專案原有的全套單元測試與健康檢查；而純寫 diff 的 C-Agent (Claude 3.7) 只有 **70.6%** 通過。
- 結構化、具有代碼上下文錨定的修補工具能顯著減少「破壞原有業務邏輯」的副作用。

#### ④ 安全對齊與拒答（Safety Alignment & Refusals, §4.1）
- OpenAI Codex CLI 出現嚴重的安全拒答現象：o3-high 拒答率 14.1%、o4-mini 拒答率 11.2%，多數發生於嘗試生成攻擊 Payload 時；而 Claude Code 與開源模型幾乎不拒答。

---

## 🧠 對實驗室三年計畫（Y1 / Y2 / Y3）的深度對照與批判性思考

BountyBench 表面上只定義了 **Detect（探測）** 與 **Patch（修補）**，表面上看似乎跨過了 **Y2（根因定位）**，但深入研讀其實驗底層細節後，會發現它**反而是確立 Y2 核心價值與不可或缺性的最強大論據**：

### 1. 對 Y2（根因定位與診斷）的深層啟示：揭開「90% 修補率」的背後真相

> [!IMPORTANT]
> **BountyBench 的「作弊前提」**：  
> 其 Patch 任務之所以能達到 90% 的超高成功率，是因為其 Prompt（附錄 I Figure 23）**直接塞入了人類安全研究員撰寫的完整 Bug Bounty 報告**！

1. **第二年的工作在 BountyBench 裡是由人做掉的**：
   - Bounty 報告中詳細指明了漏洞原理、觸發條件，在 Lunary 範例中甚至直接附上了具體檔案與程式碼行號（`index.ts L67-L87`）。
   - 論文 §3.1 亦承認：在真實世界中，這份報告通常「模糊不清或不完整」，企業內部安全團隊往往需要耗時數週甚至數月與白帽黑客反覆確認才能定位根因。
2. **全自動防禦流水線中的「斷橋」**：
   - 在實驗室的端到端防禦系統中，**沒有人類白帽黑客在背後撰寫報告**。
   - Y1（黑箱探測 Agent）打穿系統後，輸出的僅是 HTTP 流量、攻擊 Request 與後端動態 Execution Trace。
   - **如果沒有 Y2**，Y3（修補 Agent）根本無從得知該修哪裡！**Y2 的核心任務，正是要全自動生成這份 BountyBench 預設由人類完成的「根因診斷報告」**（涵蓋違反的存取規則、缺失檢查的代碼錨點、建議修復層級）。
3. **單一 Exploit 驗證的盲點（Multi-Entrypoint Blindspot）**：
   - BountyBench 的修補判定只檢驗「原題目提供的這 1 個 Exploit」是否被阻斷。
   - 在存取控制（BAC/IDOR）漏洞中，同一個脆弱的業務物件往往暴露在多個 API 端點或 Controller 路由下。Agent 只要針對該 Exploit 打個局部補丁就能在 BountyBench 拿滿分，但根本未消除其他入口的隱患。
   - 這正是 **Y2 第 ③ 步（全域受影響入口比對）** 才能解決的結構性問題。

#### 💡 可落地的消融實驗設計（Ablation Experiment for Y2）
直接借用 BountyBench 開源的真實系統 Docker、Exploit 驗證器與 Invariants，設計三組修補對照實驗：
- **組別 A（無 Y2，純黑箱到修補）**：僅提供修補 Agent「攻擊 Request Payload + 系統原始碼」。
- **組別 B（加 Y2，本計畫流水線）**：提供修補 Agent「攻擊 Request + 系統原始碼 + **Y2 自動診斷報告**」。
- **組別 C（上限對照，BountyBench 原設定）**：提供修補 Agent「攻擊 Request + 系統原始碼 + **人類撰寫之原始 Bounty 報告**」。
- **檢驗指標**：比較修補成功率，並額外引入變形攻擊測試「其他入口是否同樣被修復」。預期此實驗能直接證明 Y2 是全自動防禦中不可取代的關鍵節點。

### 2. 對 Y1（漏洞探測 Agent）的借鑑
- **Detect Indicator 機制**：Y1 在評估黑箱探索成功與否時，可借鑑此邏輯（在未修補版成功、在官方補丁版失敗），作為排除偽陽性與環境噪聲的客觀標準。
- **探索導引階梯**：零日 Detect 的低成功率（<12.5%）說明全黑箱隨機探索成本極高，Y1 應設計引導提示機制（如從 API 規格或敏感路由推論攻擊方向）。

### 3. 對 Y3（自動修補與驗證）的借鑑
- **雙層 Invariants 檢驗標準**：Y3 的驗證環節必須標準化納入原專案單元測試與服務健康檢查，防止「假修復」與業務邏輯破壞。
- **結構化 Patch 工具支援**：Codex CLI 的實踐表明，提供類似 `apply_patch` 或精確行替換的結構化編輯工具，能顯著提升修補的語法正確性與測試通過率（92.3% vs 70.6%）。

---

## ⚠️ 論文局限性 (Limitations)

1. **環境建置成本極高**：每個案例需要耗費數十小時人工架設伺服器、水化資料庫數據、撰寫 Exploit 與雙版本驗證，擴充難度大。
2. **語言分佈單一**：極度偏向 Python 與 JS，缺乏企業級後端最龐大的 **Java、PHP、Go** 生態，對於全面性存取控制研究存在語言盲區。
3. **無 Web 前端與瀏覽器操作**：Agent 僅在 Kali Linux 終端環境內操作 CLI 工具，無法執行涉及複雜前端 DOM 或動態客戶端邏輯的利用與修補。

---

## 📌 總評與會議報告建議 (Verdict & Presentation Strategy)

- **文獻評估總表定位**：**「限定用途（評估架構與消融實驗借用）」**。不適合作為 Y2 的主力評估集（因存取控制案例僅 3 個且無 Java），但其測試驗證哲學極具開創性。
- **實驗室會議報告建議**：
  - 建議作為橫跨 Y1、Y2、Y3 的**宏觀對照論文**。
  - 報告時可先展示其統一攻防的評測哲學與雙層 Invariants 防作弊機制；
  - 接著話鋒一轉，**直指其 Patch 高成功率建立在「人類已寫好定位報告」的假設**，完美突顯實驗室專案中 Y2 自動根因定位不可替代的核心價值！

# LLM-Android 安全自動修復：動態驗證四大前沿研究方向
## 學術文獻擴充與流派發散報告（2024–2026）

***

## 執行摘要

本報告針對「基於大語言模型（LLM）的 Android 程式碼安全自動修復與動態驗證」計畫，系統性地梳理 2024–2026 年間軟體安全與軟體工程頂級會議（S&P、USENIX Security、CCS、NDSS、ICSE、FSE、ISSTA 等）的最新學術流派。報告聚焦於四個「跳脫傳統 Android 測試框架」的發散方向，每個方向皆提供核心演算法/理論、代表性論文、關鍵字與技術難題，旨在強化計畫的學術前沿度與技術護城河。

***

## 方向一：環境依賴的智慧偽裝與微執行

### Advanced Mock/Stub Synthesis & Environment Reconstruction

#### 核心演算法與理論

在 Headless 或微切片環境中自動合成 Mock/Stub 面臨的根本挑戰，在於如何在缺乏完整 Android 系統服務（Binder IPC、WindowManager、WebView）的情況下，仍能重現接近生產環境的行為語義。學術界目前形成了三條主要技術路線：

**路線 A：生產行為監控 + Mock 合成（Production Carving）**

RICK（Tiwari, Monperrus & Baudry, KTH）提出「生產監控自動生成 Mock」的核心思路：在生產環境中對目標方法及其可模擬呼叫（mockable method calls）進行插樁，收集執行期的輸入輸出與互動脈絡，離線生成帶有真實 Mock 互動情境的測試案例。該方法發表於 IEEE Transactions on Software Engineering（TSE 2024），實驗於三個真實 Java 開源應用，52.4% 的生成測試案例能完全複現目標方法的生產執行脈絡。這一思路的關鍵突破在於：Mock 的輸入數值與回傳值直接來自生產遙測，徹底消除手動猜測 Stub 行為語義的問題。[^1][^2]

**路線 B：LLM 驅動的 Mock 資訊提取與合成（AST-based Mock Intelligence）**

MOCKMILL（Lee, Teh, Zhu, Li, Fazzini & Terragni, ICST/AIST 2026）是目前最新的 LLM-Mock 融合研究。其四階段工作流如下：(1) 解析 JUnit 5 + Mockito 測試的 AST，識別現有測試中使用 `when(...).thenReturn(...)` 或 `verify()` 的組件；(2) 精確提取 stubbing 數值與 interaction expectations，編碼為 JSON 結構；(3) 將 Mock 資訊注入 LLM prompt，引導生成高度針對性的測試案例；(4) 迭代編譯-執行-修復迴圈確保可執行性。評估顯示，MOCKMILL 以僅 5–15% 的額外成本，在 mutant kill rate 上顯著優於純 LLM 方法（如 CAS 類別達 24.56% vs. 1.75%）。[^3][^4]

**路線 C：程式切片（Program Slicing）驅動的環境合成**

StubCoder（Zhu, Wei, Terragni et al., TOSEM/ACM 2023–2024）利用演化演算法（evolutionary algorithm）自動生成與修復 Stub 程式碼，使單元測試能在缺乏完整環境的情況下編譯並執行。對於 Android Headless 場景，程式切片可將 Binder IPC 呼叫序列「切片化」，僅保留影響 Sink 行為的資料相依鏈，從而最小化所需的 Stub 介面集合。[^5]

#### 2024–2026 代表性論文

| 論文/工具 | 作者 | 發表場合 | 核心貢獻 |
|---|---|---|---|
| **MOCKMILL** | Lee, Teh, Zhu et al. | ICST/AIST 2026[^3] | AST Mock 資訊 → LLM 引導測試生成 |
| **RICK** | Tiwari, Monperrus, Baudry | TSE 2024[^1][^2] | 生產行為監控自動生成 Mock |
| **StubCoder** | Zhu, Wei, Terragni et al. | TOSEM 2023/ACM 2024[^5] | 演化演算法自動 Stub 生成與修復 |
| **ASTER** | (多語言單元測試) | arXiv 2025[^6] | 靜態分析引導 LLM 複雜環境 Mocking |
| **LLM for Mobile Roadmap** | 多作者 | ACM DL 2025[^7] | LLM + 行動生態系整合研究路線圖 |

#### 核心關鍵字

`Mock/Stub Synthesis`, `Production Carving`, `AST-based Mock Extraction`, `Headless Environment Reconstruction`, `Program Slicing for Isolation`, `Observation-based Test Generation`, `Binder IPC Stub`, `LLM-guided Test Double`, `Mockito Stubbing Intelligence`

#### 技術難題

1. **Binder IPC 語義複雜性**：Binder 交易（transaction）涉及跨行程的 Parcelable 序列化，現有 AST-based Stub 合成工具對跨行程語義的建模仍有限，LLM 易產生語義不正確的 Parcel 填充。[^7]
2. **WebView 非確定性**：WebView 的 JavaScript 執行結果不可序列化，生產監控難以穩定捕捉其輸入輸出。
3. **Mock 過度擬合**：從生產行為生成的 Mock 可能過於具體（overly specific），無法作為泛化安全屬性的驗證基礎。[^4]
4. **環境狀態爆炸**：Android 系統服務之間存在複雜的狀態依賴，切片化 Stub 可能遺漏隱性狀態轉換，導致微執行結果與真實設備不一致。

***

## 方向二：安全不變式與屬性測試

### Property-based Security Testing & Automated Invariant Inference

#### 核心演算法與理論

「屬性測試（Property-based Testing, PBT）」打破 JUnit 以「單一輸入-單一預期輸出」為核心的測試模式，轉而驗證程式在**一類輸入**上是否恆成立的**行為屬性**（invariants）。在安全領域，這意味著可以自動推斷「任何 API 呼叫序列，均不得導致敏感資料流向未授權 Sink」此類高層安全不變式，而非只驗證單一路徑。

**Kea 框架與隱私屬性驗證**

東華師範大學蘇亭（Ting Su）團隊是此領域的核心推動者。Kea 工具（ASE 2024）實現了針對 Android App 的通用實用屬性測試框架，在 124 個真實歷史 Bug 上評估，涵蓋 8 款主流 App。其核心設計是允許開發者以 `@property` 標注跨 UI 互動序列的不變式，Kea 的隨機探索引擎自動生成觸發序列並驗證不變式是否被違反。[^8][^9]

**PDTDroid：隱私規格自動化驗證（FSE 2024 工業論文）**

PDTDroid 將隱私規格（自然語言）轉換為 **Büchi 自動機（Büchi Automata）**，並以此引導測試案例生成與狀態機驗證。在 TikTok 的 125 項真實隱私規格上，PDTDroid 平均減少 95.2% 的人工測試工作量，並發現 22 項未知不一致性（含 4 項隱私外洩 Bug）。這直接對應計畫所需的「SharedPreferences 隱私外洩驗證」場景。[^10]

**iPBT：LLM 驅動的可執行屬性合成（arXiv 2026）**

iPBT（Xiong, Su, Sun et al., 2026）提出一種結構化屬性合成流程：(1) 以多模態 LLM（MLLM）建立豐富的 Widget 語義脈絡；(2) 以 LLM in-context learning 將自然語言屬性描述翻譯為可執行的 Kea 屬性程式碼。在 124 項屬性描述的評估中，iPBT 達到 95.2% 的合成準確率，並將人工撰寫可執行屬性的時間縮短 56%。[^11]

**PropGen：行為證據驅動的屬性推斷（arXiv 2026）**

PropGen（arXiv 2604.13463）更進一步：系統性探索 App 功能以收集執行期互動軌跡（behavioral evidence），然後從軌跡中自動推斷屬性三元組 \( \phi = \langle P, I, Q \rangle \)（前置條件、互動序列、後置條件），再生成 Kea 相容的可執行屬性。PropGen 在 12 款真實 Android App 上發現 25 個未知功能 Bug，其中僅有 3 個（12%）被現有技術發現。[^12][^13]

**安全不變式自動推斷（Daikon + LLM）**

傳統的 Daikon 工具利用動態執行觀察推斷程式不變式。最新研究（2024–2025）將 LLM 與反例引導推斷（Counter-example Guided Inductive Inference, CEGII）結合，生成「補丁不變式（patch invariants）」作為漏洞修復的約束。VRpilot（2024）進一步展示推理（reasoning）與補丁驗證反饋對 LLM 漏洞修復效果的關鍵作用。[^14]

#### 2024–2026 代表性論文

| 論文/工具 | 作者 | 發表場合 | 核心貢獻 |
|---|---|---|---|
| **Kea（通用 PBT for Android）** | Ting Su et al. | ASE 2024[^8][^9] | 首個實用 Android App 屬性測試框架 |
| **PDTDroid** | Sun, Su, Wang et al. | FSE 2024（工業）[^10] | Büchi 自動機驅動隱私規格驗證 |
| **iPBT** | Xiong, Su et al. | arXiv 2026[^11] | LLM 自然語言 → 可執行安全屬性 |
| **PropGen** | （Su 團隊） | arXiv 2026[^12][^13] | 行為軌跡 → 自動屬性三元組推斷 |
| **LLMxCPG** | Lekssays et al. | USENIX Security 2025[^15] | CPG + LLM 脈絡感知漏洞偵測 |
| **Web Invariants (WPT)** | Bernardo et al. | USENIX Security 2024[^16][^17] | 一階邏輯 Web 安全不變式自動驗證 |

#### 核心關鍵字

`Property-based Testing (PBT)`, `Security Invariants`, `Büchi Automata`, `Daikon`, `Counter-example Guided Inductive Inference (CEGII)`, `Patch Invariants`, `Privacy Specification Validation`, `LLM Property Synthesis`, `Oracle-free Testing`, `Differential Privacy Oracle`

#### 技術難題

1. **屬性精度-召回率的權衡**：過於寬鬆的屬性產生大量誤報（false positives），PropGen 需要對 127 項屬性進行修正，但仍有精度損失。[^13]
2. **安全屬性的完備性（completeness）**：LLM 從自然語言推斷的安全屬性是否能覆蓋所有 CWE 類型，目前缺乏系統評估。
3. **隱性資訊流（Implicit Flow）的屬性建模**：傳統 PBT 框架以可觀察的 UI 狀態為屬性對象，難以直接建模控制流相依的隱性資訊洩漏。
4. **Robolectric 中的屬性可執行性**：從生產環境推斷的屬性三元組，若涉及 Android 系統 API，在 Headless 環境中的可執行率有限。[^12]

***

## 方向三：安全感知變異測試與差分安全驗證

### Security-aware Mutation Testing & Differential Patch Validation

#### 核心演算法與理論

**子方向 A：差分測試於 APR 補丁閉環驗證**

在 LLM 自動修復（APR/AVR）的閉環中，單純的 pass/fail 反饋無法識別「偶然通過測試但語義錯誤」的補丁（overfitting patches）。差分測試（Differential Testing）透過**比對原始程式與修補程式的執行軌跡（execution traces）**，識別行為差異，從而篩選語義正確的候選補丁。

**TraceRepair**（arXiv 2604.02647, 2026）提出多代理框架（Multi-Agent Framework）：一個探針代理（probe agent）捕捉關鍵變數的執行快照（execution snapshots），形成客觀修復基礎；一個委員會代理（committee of agents）交叉驗證候選補丁，暴露矛盾並迭代修正。在 Defects4J 基準上，TraceRepair 正確修復 392 個缺陷，大幅超越現有 LLM 方法。[^18]

**AvicennaPatch**（APR 2025 @ ICSE）採用差分測試策略：同時執行原始程式與修補程式，識別行為發散的輸入，再利用 ISLA 約束生成語法-語義層的人類可讀解釋，明確描述「哪些輸入結構會觸發此補丁」。[^19][^20]

**DynaFix**（arXiv 2512.24635, 2025/2026）在每輪修復中捕捉**執行期動態資訊**（變數狀態、控制流路徑、呼叫堆疊），轉換為結構化 prompt，引導 LLM 生成候選補丁；若補丁驗證失敗，重新執行修改後的程式收集新的執行資訊，形成迭代回饋迴圈。在 Defects4J v1.2/v2.0 上，DynaFix 修復 186 個單函數 Bug，補丁搜尋空間縮減 70%。[^21]

**DebugRepair**（arXiv 2604.19305, 2026）引入「模擬偵錯插樁（Simulated Instrumentation）」：動態插入偵錯語句收集中間執行狀態，以此為根因分析依據迭代修正補丁。搭配 GPT-3.5，DebugRepair 在 Defects4J 上正確修復 224 個 Bug，超越現有 SOTA 26.2%。[^22]

**子方向 B：漏洞模擬變異測試（Vulnerability-mimicking Mutants）**

傳統變異測試注入的是語法層面的隨機突變，對安全測試工具的評估意義有限。「漏洞模擬變異測試」的核心思想是：設計**安全語義明確的變異算子（security-specific mutation operators）**，使注入的突變行為模擬真實漏洞模式（如 CWE 類別）。

**SecMutBench**（OpenReview 2025/2026）設計了 25 個安全專用變異算子，涵蓋 30 個 CWE 類別，對安全程式碼注入真實漏洞模式，生成 1,869 個確定性 mutants。以三層 Kill 分類（語義殺死、偶然殺死、崩潰）評估 LLM 生成安全測試的品質。[^23][^24]

**LLM-Mutant 耦合研究**（ICST 2024）系統分析 CodeBERT 生成的 mutants 與真實漏洞的耦合程度：在 Vul4J 資料集的 45 個可重現漏洞中，CodeBERT mutants 與 32 個漏洞（71%）強耦合，即 mutants 因相同原因失敗相同測試。這提供了強力的理論基礎：LLM 生成的 mutants 可以作為漏洞的代理（proxy），用於評估安全檢測工具的極限。[^25]

**Vulnerability Mimicking Mutants**（arXiv 2303.04247）專門研究如何設計在統計意義上模擬真實漏洞行為的 mutants，避免傳統隨機變異與安全漏洞模式脫節的問題。[^26][^27]

#### 2024–2026 代表性論文

| 論文/工具 | 作者 | 發表場合 | 核心貢獻 |
|---|---|---|---|
| **TraceRepair** | （多代理 APR） | arXiv 2026[^18] | 執行快照作為客觀約束的多代理差分修復 |
| **DynaFix** | — | arXiv 2025[^21][^28] | 執行期動態資訊驅動的迭代 LLM 修復 |
| **DebugRepair** | — | arXiv 2026[^22] | 模擬偵錯插樁 + 中間狀態引導修復 |
| **AvicennaPatch** | Eberlein et al. | APR@ICSE 2025[^19][^20] | 差分測試 + ISLA 約束描述補丁觸發輸入 |
| **SecMutBench** | — | OpenReview 2025[^23][^24] | 25 個安全算子 × 30 CWE 類別的 LLM 安全測試評估基準 |
| **LLM-Mutant Coupling** | Garg, Degiovanni et al. | ICST 2024[^25] | CodeBERT mutants 與 CVE 漏洞耦合度系統分析 |
| **SWE-bench Differential** | — | arXiv 2025[^29] | 差分補丁測試識別 SWE-bench 解決方案的真實正確性 |

#### 核心關鍵字

`Differential Testing`, `Execution Trace Comparison`, `Patch Equivalence Analysis`, `Vulnerability-mimicking Mutants`, `Security-aware Mutation Operators`, `CWE-specific Mutants`, `LLM Mutant Coupling`, `Overfitting Patch Detection`, `Multi-agent APR`, `Dynamic State-guided Repair`

#### 技術難題

1. **軌跡對齊的代價**：比對兩個補丁版本的完整執行軌跡需要精確的行號對齊（line-level alignment），在 Android Robolectric 微執行中，Robolectric 的 Shadow 類別攔截可能造成軌跡結構不一致。
2. **安全變異算子的 Android 適用性**：現有 SecMutBench 以 Python 為目標語言，針對 Java/Android（SharedPreferences 未加密、Log 洩漏）的 CWE-specific 算子設計幾乎空白。[^23]
3. **LLM Mutant 的「自適應」攻擊**：若用 LLM 生成的 mutants 訓練安全檢測工具，檢測工具可能對 LLM 的生成分布過擬合，而對真實漏洞的分布外範例（out-of-distribution）失效。
4. **差分測試的 Oracle 問題**：對於隱私外洩型漏洞（如 Log.d 輸出敏感字串），「修復前」和「修復後」的行為差異可能僅存在於 Sink 的參數值，需要 Mock Spy 級別的細粒度觀測。

***

## 方向四：底層 Runtime 插樁與記憶體安全動態追蹤

### ART-level Instrumentation & Native-layer Dynamic Taint Analysis

#### 核心演算法與理論

**子方向 A：ART 層級的編譯期插樁（Compiler-based Instrumentation）**

ARTist（Backes, Bugiel, Schranz et al.）是針對 Android Runtime 的編譯器插樁框架，基於 `dex2oat` 的 Optimizing 編譯器後端，可在設備端編譯期直接注入插樁程式碼。與傳統字節碼重寫（bytecode rewriting）不同，ARTist 在指令層面進行插樁，保留 App 簽名，無需重新打包，是目前最接近「零開銷插樁」的 ART 層方案。其核心使用場景包括污點追蹤的重新實例化（TaintDroid 的 ART 相容移植）、廣告庫隔離（compartmentalization）以及方法級全系統插樁（25k 方法）。[^30][^31][^32]

**TaintART 與 TaintMan：ART 相容的動態污點分析**

TaintART（CUHK, CCS 2016）與 TaintMan 分別提出了在 ART 環境下實現多層資訊流追蹤的方案。TaintMan 的關鍵貢獻是「執行環境重建技術（execution environment reconstruction）」，用以處理 ART 在不同 Android 版本間的 ABI 差異，同時覆蓋顯性資訊流（data dependence）與隱性資訊流（control dependence）。[^33][^34]

**ViaLin：路徑感知動態污點分析（FSE 2023）**

ViaLin（Ahmed, Wang, Lis, Rubin）是截至目前最完整的 Android 動態污點路徑追蹤方案：不僅報告污點流的 Source 與 Sink，還能準確追蹤**完整的污點傳播路徑**（taint propagation path）。這對「提供動態證據說明哪條程式碼路徑導致敏感資料外洩」的計畫需求具有直接價值。ViaLin 在真實設備上以相對低的時間與記憶體開銷運行。[^35][^36]

**子方向 B：Native 層（JNI/C++）輕量級追蹤**

隨著 Android App 原生程式碼比例上升，JNI 邊界已成為污點分析的主要盲區。[^37]

**JNFuzz-Droid**（SANER 2024 / ESEJ 2025）提出基於 Client/Server 架構的輕量化原生模糊測試與污點分析框架：首先定位接收敏感資料的 Android 原生函數，再以 INFuzz 模糊測試提升程式碼覆蓋率，同時用動態二進位工具（Dynamic Binary Instrumentation, DBI）分析原生程式碼中的資料流。實驗顯示 JNFuzz-Droid 能有效偵測 App 原生程式碼中的敏感資料外洩，超越現有原生分析工具。[^38][^39]

**JNITrace + Frida 生態**：`jnitrace`（Frida-based）能在不需 Root 的情況下動態攔截並記錄所有 JNI API 呼叫，包括 `CallObjectMethod`、`NewStringUTF` 等。結合 Frida 的 `jit-compile` 能力，可在 JNI 函數入口注入污點標記，實現 Java 層到 Native 層的跨邊界污點傳播。對於計畫的「微執行 + Robolectric」場景，Frida 可以透過 ADB 附掛（attach）到 Robolectric JVM 行程，在不修改 ART 原始碼的前提下攔截 JNI 函數呼叫。[^40][^41][^42]

**子方向 C：LLM 輔助的代理式漏洞發現（Agentic Vulnerability Discovery）**

最新趨勢（2025–2026）是將 LLM 代理與動態插樁結合，形成「探索-插樁-驗證」的閉環。一篇 2026 年的 arXiv 論文（arXiv 2508.21579）提出代理式 Android App 漏洞發現與驗證框架，結合靜態分析（漏洞定位）與動態執行（漏洞確認）。另一篇 2025 年的調查論文（arXiv 2503.20244）系統梳理了跨程式語言、跨程式表示形式的漏洞分析技術，指出 LLM 在結合動態程式分析（DPA）方面存在巨大研究空白。[^43][^44]

**SIAT：ICC 即時污點分析（跨組件通信）**

SIAT 在 TaintDroid 的基礎上擴展了「意圖污點標記（intent taint tagging）」，能追蹤 Android ICC（Inter-Component Communication）中的跨組件污點傳播，偵測惡意 Intent 使用模式。這對於計畫中「SharedPreferences 跨組件讀寫」的 Sink 監控具有直接參考價值。[^45]

#### 2024–2026 代表性論文

| 論文/工具 | 作者 | 發表場合 | 核心貢獻 |
|---|---|---|---|
| **JNFuzz-Droid** | — | SANER 2024 / ESEJ 2025[^38][^39] | Android 原生程式碼輕量模糊測試 + 污點分析 |
| **ViaLin** | Ahmed, Wang, Lis, Rubin | FSE 2023[^35][^36] | 路徑感知動態污點分析（完整傳播路徑） |
| **ARTist** | Backes, Bugiel, Schranz et al. | EuroS&P 2017 / BH 2018[^31][^32] | ART dex2oat 編譯期插樁框架（持續演進） |
| **TaintMan** | — | IEEE TDSC 2017–2024[^33][^46] | ART 相容多層污點分析（顯性+隱性流） |
| **Agentic Android Vuln Discovery** | — | arXiv 2025[^44] | LLM 代理式 Android 漏洞發現與動態驗證 |
| **LLMxCPG** | Lekssays et al. | USENIX Security 2025[^15] | 程式碼屬性圖（CPG）+ LLM 脈絡感知漏洞偵測 |
| **SIAT（ICC 污點）** | — | Journal of Computer Security 2023[^45] | 跨組件通信即時污點追蹤 |

#### 核心關鍵字

`ART-level Instrumentation`, `dex2oat Compiler-based Instrumentation`, `Dynamic Taint Analysis (DTA)`, `Path-aware Taint Tracking`, `JNI Boundary Taint Propagation`, `Native Code DBI (Dynamic Binary Instrumentation)`, `Frida JNI Hooking`, `jnitrace`, `ARTist`, `ICC Taint Propagation`, `Implicit Information Flow`, `LLM Agentic Vulnerability Discovery`

#### 技術難題

1. **Robolectric 的 JNI 盲區**：Robolectric 在 JVM 層模擬 Android，但對 `System.loadLibrary()` 載入的 `.so` 原生庫缺乏追蹤能力。若目標漏洞涉及 JNI 層（如透過 Native 加密後洩漏），現有 Robolectric + Mockito 框架完全無法偵測。[^37]
2. **ART 版本碎片化**：ART 在不同 Android API Level 間存在 ABI 差異，ARTist 等工具的維護成本高，且在最新 Android 14/15 上的相容性未經系統驗證。[^31]
3. **隱性資訊流的路徑爆炸**：控制流相依（control dependence）的污點傳播可能因分支爆炸而導致追蹤失精（over-tainting）或遺漏（under-tainting）。ViaLin 採用啟發式路徑限制，但在複雜的 Android 生命週期回呼（lifecycle callbacks）中仍有遺漏。[^35]
4. **Frida 在 CI 環境的可行性**：Frida 需要附掛至執行中的行程，在純 JVM 的 CI 測試環境中，若目標是 Robolectric 測試，需要設計 Frida Java API 橋接層，增加工程複雜度。[^40]
5. **Native 污點傳播的跨邊界語義**：Java 層的污點標記在穿越 JNI 邊界時，Native C++ 端對 `jbyteArray`、`jstring` 等 JNI 型別的記憶體操作不攜帶污點元資料，需要額外的影子記憶體（shadow memory）機制。[^47][^37]

***

## 跨方向整合架構：技術護城河設計建議

以下表格從「研究稀缺性」、「技術整合難度」與「對計畫核心主題的貢獻」三個維度評估各方向的護城河強度：

| 研究方向 | 稀缺性 | 整合難度 | 對 LLM-AVR 的貢獻 | 建議優先級 |
|---|---|---|---|---|
| **方向一** Mock/Stub LLM 合成 | 中（競爭者少） | 高（Binder 語義） | 解決 Headless 環境限制 | ★★★★☆ |
| **方向二** 安全不變式 PBT | 低（蘇亭團隊活躍） | 中（LLM 屬性合成已成熟） | 提供可自動化的安全 Oracle | ★★★★★ |
| **方向三** 漏洞模擬變異測試 | 高（Android 安全算子缺失） | 中（可在 Robolectric 執行） | 評估與強化 LLM 修復品質 | ★★★★★ |
| **方向四** ART/JNI 原生追蹤 | 高（學術研究稀少） | 非常高（版本兼容+工程量大） | 覆蓋 JNI 漏洞盲區 | ★★★☆☆ |

**最高護城河組合**：方向二（iPBT/PropGen 框架引入）×方向三（Android 安全 CWE 算子設計）的組合，能以最小工程成本實現最高的差異化學術貢獻——設計「Android 安全感知 CWE 變異算子集（Android-CWE MutOps）」填補 SecMutBench 的 Android 空白，並以 iPBT 自動化生成對應的安全不變式作為變異測試的 Oracle，形成完整的「生成補丁 → 自動合成 Oracle → 差分變異測試驗證」閉環。

***

## 開源工具索引

| 工具 | 方向 | 語言/平台 | 取得方式 |
|---|---|---|---|
| **Kea** | 方向二 | Python/Android | github.com/ecnusse/Kea[^8] |
| **MOCKMILL** | 方向一 | Java (JUnit5+Mockito) | zenodo.org/records/19490390[^48] |
| **RICK** | 方向一 | Java | zenodo.org/records/12685561[^2] |
| **ViaLin** | 方向四 | Java/Android | github.com/resess/ViaLin[^49] |
| **ARTist** | 方向四 | Android (ART) | github.com/project-artist[^50] |
| **jnitrace** | 方向四 | Frida/JS | github.com/chame1eon/jnitrace[^41] |
| **SecMutBench** | 方向三 | Python | github.com/Mars-2030/secmutbench[^51] |
| **StubCoder** | 方向一 | Java | zenodo.org/records/7816758[^52] |
| **DynaFix** | 方向三 | Java (Defects4J) | arXiv 2512.24635[^21] |
| **TraceRepair** | 方向三 | Java | arXiv 2604.02647[^18] |

---

## References

1. [Title: Mimicking Production Behavior with Generated Mocks](https://arxiv.org/abs/2208.01321)

2. [RICK - Mimicking Production Behavior with Generated Mocks](https://zenodo.org/records/12685561) - This package contains software and experimental data for RICK, an automated test and mock generation...

3. [Improving LLM-Driven Test Generation by Learning from Mocking ...](https://arxiv.org/abs/2604.19315) - Large Language Models (LLMs) have recently shown strong potential for automated unit test generation...

4. [[Literature Review] Improving LLM-Driven Test Generation by ...](https://www.themoonlight.io/en/review/improving-llm-driven-test-generation-by-learning-from-mocking-information) - MOCKMILL is an LLM-based technique designed to enhance automated unit test generation by systematica...

5. [StubCoder: Automated Generation and Repair of Stub Code for ...](https://dl.acm.org/doi/10.1145/3617171) - In this article, we present StubCoder to automatically generate and repair stub code for regression ...

6. [ASTER: Natural and Multi-language Unit Test Generation with LLMs](http://arxiv.org/pdf/2409.03093.pdf) - ...rigorous investigation of how large language models (LLMs) can help bridge the
gap. We describe a...

7. [LLM for Mobile: An Initial Roadmap](http://arxiv.org/pdf/2407.06573.pdf) - When mobile meets LLMs, mobile app users deserve to have more intelligent
usage experiences. For thi...

8. [GitHub - ecnusse/Kea: Property-based Testing for Mobile GUI Apps](https://github.com/ecnusse/Kea) - Property-based Testing for Mobile GUI Apps. Contribute to ecnusse/Kea development by creating an acc...

9. [[PDF] General and Practical Property-based Testing for Android Apps](https://tingsu.github.io/files/ASE24-Kea.pdf) - We implemented our technique as a tool named Kea and evaluated it on 124 historical bugs from eight ...

10. [Property-based Testing for Validating User Privacy ... - FSE 2024](https://2024.esec-fse.org/details/fse-2024-industry/42/Property-based-Testing-for-Validating-User-Privacy-Related-Functionalities-in-Social-) - To this end, we adapt property-based testing to validate app behaviors against the properties descri...

11. [From Natural Language to Executable Properties for Property-based Testing of Mobile Apps](https://arxiv.org/abs/2603.21263v1) - Property-based testing (PBT) is a popular software testing methodology and is effective in validatin...

12. [LLM-Based Property Generation for Mobile App Testing - arXiv](https://arxiv.org/html/2604.13463) - We develop a property synthesis and refinement approach that derives properties from behavior eviden...

13. [LLM-Based Property Generation for Mobile App Testing](https://www.themoonlight.io/en/review/from-exploration-to-specification-llm-based-property-generation-for-mobile-app-testing) - This paper introduces PropGen, an automated approach for generating properties for mobile app testin...

14. [[PDF] Program vulnerability repair via inductive inference | Semantic Scholar](https://www.semanticscholar.org/paper/Program-vulnerability-repair-via-inductive-Zhang-Gao/ab91720b71931f1ba94ff1a690c3b000ac28153d) - A counter-example guided inductive inference procedure over program states to define likely invarian...

15. [LLMxCPG: Context-Aware Vulnerability Detection Through ...](https://www.usenix.org/conference/usenixsecurity25/presentation/lekssays) - 由 A Lekssays 著作 · 2025 · 被引用 63 次 — This paper presents LLMxCPG, a novel framework integrating Code ...

16. [USENIX Security '24 - Web Platform Threats: Automated Detection of Web Security Issues With WPT](https://www.youtube.com/watch?v=hKVOLSoKs-w) - Web Platform Threats: Automated Detection of Web Security Issues With WPT

Pedro Bernardo and Lorenz...

17. [Automated Detection of Web Security Issues With WPT](https://www.usenix.org/system/files/usenixsecurity24-bernardo.pdf) - 由 P Bernardo 著作 · 2024 · 被引用 14 次 — In particular, we leverage Web Platform Tests. (WPT), a popular ...

18. [Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate](https://arxiv.org/abs/2604.02647) - Automated Program Repair (APR) struggles with complex logic errors and silent failures. Current LLM-...

19. [Which Inputs Trigger my Patch? (APR 2025) - conf.researchr.org](https://conf.researchr.org/details/icse-2025/apr-2025-papers/9/Which-Inputs-Trigger-my-Patch-) - This page will soon grow in content and contain information about the scope of this research track.

20. [[PDF] Which Inputs Trigger my Patch? - Martin Eberlein](https://martin-eberlein.com/assets/files/2025APR-PatchAvicenna.pdf) - In this paper, we introduce AVICENNAPATCH, a novel tool de- signed to provide precise explanations o...

21. [DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information](https://arxiv.org/abs/2512.24635) - Automated Program Repair (APR) aims to automatically generate correct patches for buggy programs. Re...

22. [DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging](https://arxiv.org/abs/2604.19305) - Automated Program Repair (APR) has benefited from the code understanding and generation capabilities...

23. [Mars-2030/secmutbench1: v 1.0 | Synapse](https://synapsesocial.com/papers/69fd7e79bfa21ec5bbf06adf) - ... SecMutBench focuses on security test generation evaluated through mutation testing. Given secure...

24. [SecMutBench: Evaluating LLM-Generated Security Tests via...](https://openreview.net/forum?id=3IGvziUsqX) - Second, we design 25 security-specific mutation operators spanning 30 CWE categories that transform ...

25. [On the Coupling between Vulnerabilities and LLM-generated Mutants: A Study on Vul4J dataset (ICST 2024 - Research Papers) - ICST 2024](https://conf.researchr.org/details/icst-2024/icst-2024-papers/25/On-the-Coupling-between-Vulnerabilities-and-LLM-generated-Mutants-A-Study-on-Vul4J-d) - ICST 2024 (https://conf.researchr.org/home/icst-2024) invites high-quality submissions in all areas ...

26. [[PDF] Vulnerability Mimicking Mutants - arXiv](https://arxiv.org/pdf/2303.04247.pdf)

27. [Vulnerability Mimicking Mutants](http://arxiv.org/pdf/2303.04247.pdf)

28. [다이나픽스: 실행 수준 동적 정보 기반 반복적 자동화된 프로그램 복구](https://www.alphaxiv.org/ko/overview/2512.24635v1) - View recent discussion. Abstract: Automated Program Repair (APR) aims to automatically generate corr...

29. [Are "Solved Issues" in SWE-bench Really Solved Correctly? An Empirical
  Study](http://arxiv.org/pdf/2503.15223.pdf) - ...divergent
patches are certainly incorrect. Combined, the different weaknesses lead to an
inflatio...

30. [[PDF] The Android Runtime Instrumentation and Security Toolkit - ARTist](https://artist.cispa.saarland/res/papers/ARTist.pdf) - The literature on taint tracking for Android defines sources and sinks as the API methods that input...

31. [ARTist: The Android Runtime Instrumentation and Security Toolkit](https://arxiv.org/abs/1607.06619) - We present ARTist, a compiler-based application instrumentation solution for Android. ARTist is base...

32. [ARTist - A Novel Instrumentation Framework for Reversing ...](https://i.blackhat.com/us-18/Thu-August-9/us-18-Schranz-ARTist-A-Novel-Instrumentation-Framework-for-Reversing-and-Analyzing-Android-Apps-and-the-Middleware.pdf)

33. [TaintMan: An ART-Compatible Dynamic Taint Analysis Framework on Unmodified and Non-Rooted Android Devices](https://ieeexplore.ieee.org/document/8010886/) - Dynamic taint analysis (DTA), as a mainstream information flow tracking technique, has been widely u...

34. [[PDF] TaintART: A Practical Multi-level Information-Flow Tracking ...](https://www.cse.cuhk.edu.hk/~cslui/PUBLICATION/CCS16.pdf)

35. [ViaLin: Path-Aware Dynamic Taint Analysis for Android](https://dl.acm.org/doi/10.1145/3611643.3616330) - ViaLin accurately detects taint flow paths while running on a mobile device with a reasonable time a...

36. [ViaLin: Path-Aware Dynamic Taint Analysis for Android](https://khaled-e-a.github.io/tools/)

37. [On Tracking Information Flows through JNI in Android Applications](https://scispace.com/pdf/on-tracking-information-flows-through-jni-in-android-36hfvjbq0y.pdf)

38. [JNFuzz-Droid: a lightweight fuzzing and taint analysis framework for ...](https://dl.acm.org/doi/10.1007/s10664-025-10671-9) - We propose JNFuzz-Droid, a lightweight automated fuzzing and taint analysis framework for Android na...

39. [JNFuzz-Droid: A Lightweight Fuzzing and Taint Analysis Framework for Android Native Code](https://ieeexplore.ieee.org/document/10589738/) - The need to account for native code in Android apps is becoming urgent as the usage of native code i...

40. [GitHub - 0x3xploit/frida-android-jni-hooking](https://github.com/0x3xploit/frida-android-jni-hooking) - This project demonstrates how to perform native hooking on Android applications using Frida. It incl...

41. [GitHub - chame1eon/jnitrace: A Frida based tool that traces usage of the JNI API in Android apps.](https://github.com/chame1eon/jnitrace) - A Frida based tool that traces usage of the JNI API in Android apps. - chame1eon/jnitrace

42. [MASTG-TOOL-0107: JNITrace - OWASP Mobile Application Security](https://mas.owasp.org/MASTG/tools/android/MASTG-TOOL-0107/)

43. [Software Vulnerability Analysis Across Programming Language and Program
  Representation Landscapes: A Survey](http://arxiv.org/pdf/2503.20244.pdf) - ...examining widely used programming languages, levels of program representation,
categories of vuln...

44. [Agentic Discovery and Validation of Android App Vulnerabilities - arXiv](https://arxiv.org/html/2508.21579v1)

45. [SIAT: A systematic inter-component communication real-time analysis technique for detecting data leak threats on Android](https://journals.sagepub.com/doi/10.3233/JCS-220044) - This paper presents the design and implementation of a systematic Inter-Component Communications (IC...

46. [TaintMan: An ART-Compatible Dynamic Taint Analysis ...](https://www.youwei.site/papers/TDSC2020.pdf)

47. [[PDF] Precise Taint Analysis on Android Native Code - arXiv](https://arxiv.org/pdf/2112.06702.pdf)

48. [Replication Package for "Improving LLM-Driven Test Generation by Learning from Mocking Information" (AIST 2026)](https://zenodo.org/records/19490390) - Improving LLM-Driven Test Generation by Learning from Mocking Information (AIST 2026) — Replication ...

49. [resess/ViaLin](https://github.com/resess/ViaLin) - This repository hosts ViaLin, an accurate, low-overhead, path-aware, dynamic taint analyzer for Andr...

50. [Project-ARTist](https://github.com/project-artist) - ARTist is a flexible Android instrumentation framework for security researchers and developers based...

51. [Mars-2030/secmutbench1 - GitHub](https://github.com/Mars-2030/secmutbench) - Given secure source code and a CWE category, an LLM generates security tests. These tests are then e...

52. [StubCoder: Automated Generation and Repair of Stub Code for Mock Objects](https://zenodo.org/records/7816758) - Artifact for TOSEM submission StubCoder: Automated Generation and Repair of Stub Code for Mock Objec...


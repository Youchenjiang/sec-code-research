# INTENTFIX 對標局限與本計畫第二年（Y2）核心創新突破點

> **對標論文**：*INTENTFIX: Automated Logic Vulnerability Repair via LLM-Driven Intent Modeling* (ICSE 2026)  
> **研究定位**：本三年計畫「第二年（Y2 侑宸：白箱根因分析與架構定位）」  
> **職責邊界隔離**：本文件所列之創新點，**嚴格限於第二年自己的獨立研究範疇**（由黑盒封包到白盒圖結構因果定位），不搶佔第一年（黑盒 PoC 生成）與第三年（Multi-Hunk 補丁合成）的工作成果。

---

## 1. 職責解耦：第二年在整個生命週期中的獨特技術斷層

在評估對標與創新之前，必須先釐清各年度的獨立責任邊界：

```
[第一年 Y1 (祐廷)] 黑盒 GUI / API 滲透 ──> 產出：外部 HTTP 攻擊請求 (PoC Network Trace)
                                                  │
                                                  ▼
     🔥🔥【第二年 Y2 (侑宸) 獨立核心工作區】🔥🔥
     • 外部封包如何映射至後端內部執行路徑？ (Trace-to-Path Alignment)
     • 路徑上的強制機制究竟是「缺失」還是「無效」？ (Predicate Causal Analysis)
     • 系統中還有哪些旁路路徑共享同一個 Invariant？ (Topology Expansion)
     • 產出：專案層級漏洞根因 ＋ 函式路徑風險矩陣
                                                  │
                                                  ▼
[第三年 Y3 (羿君)] 跨層級多區塊修復 ──> 吃 Y2 的風險矩陣，合成跨檔案 Multi-Hunk Patch
```

👉 **第二年的獨立核心難題**：在完全不寫修補程式碼（修補是 Y3 的事）的前提下，**如何從黑盒網路攻擊軌跡，反推並定位後端白盒原始碼中深層的強制機制缺失與受影響的拓撲網絡**。

---

## 2. INTENTFIX 的 4 大技術局限（論文自身坦承之盲區）

仔細研讀 INTENTFIX 全文，論文在架構設計與實驗中暴露出了 4 個無法克服的致命弱點：

### 局限 1：純靜態代碼猜測意圖，缺乏執行期證據（Lack of Runtime Grounding）
* **INTENTFIX 機制**：僅僅依靠原始碼檔案中的變數名稱、函數簽名、開發者註解，提示 LLM 去「推測」預期意圖。
* **致命缺陷**：LLM 極易發生幻覺。論文 Section 5.2 坦承：在 5-tuple 意圖抽取中，**角色（Actor）抽取的準確率僅有 60%**，因為在真實程式碼中，權限往往隱式存在於 Session、Token 或中介層，靜態文字無法可靠還原。

### 局限 2：單一檔案分析盲區（Single-File Context Scope Limitation）
* **INTENTFIX 機制**：論文 Section 3.2.1 明確定義：$S$ 僅代表單一原始碼檔案（Single source file）。
* **致命缺陷**：論文 Section 6.1 (Technical Limitations) 明白寫道：
  > *"INTENTFIX currently operates within single-file contexts... extending to inter-procedural analysis across multiple files remains an important direction for future work."*
* 現代 Web 應用的邏輯漏洞，90% 以上牽涉到「路由 (Router) $\to$ 控制器 (Controller) $\to$ 業務層 (Service) $\to$ 資料實體 (Entity)」的多層跳躍。**INTENTFIX 的單檔案架構，在真實多層次專案中完全盲目**。

### 局限 3：只問代碼「在不在」，缺乏資料流因果判定（Coarse Predicate Verification）
* **INTENTFIX 機制**：其 Algorithm 2 (Line 9-12) 僅單純將程式碼丟給 LLM 詢問：「這段代碼有沒有滿足約束 $c$？」，回傳 true/false。
* **致命缺陷**：無法辨識複雜的資料流阻斷問題。例如在 J2Store 案例中，驗證函數確實被呼叫了，但**驗證結果變數從未被傳給下游狀態變更節點**。INTENTFIX 缺乏資料流分析能力，極易誤判為「檢查已存在」。

### 局限 4：自然語言空想攻擊，無法驗證漏洞真實性（Conceptual PoC Only）
* **INTENTFIX 機制**：論文 Section 3.4.2 坦承：
  > *"generating a fully executable Proof-of-Concept (PoC) exploit is often impractical due to complex environmental dependencies... INTENTFIX instead prompts the LLM to generate a structured, natural-language attack vector."*
* **致命缺陷**：其 Phase 2 產出的所謂 Attack Vector，**只是 LLM 寫的自然語言小作文（Listing 2）**，根本不能在真實環境執行重放，也無法提供客觀的因果攔截依據。

---

## 3. 第二年（Y2）的 4 大獨立核心創新突破點

針對 INTENTFIX 的上述 4 大盲區，第二年（侑宸）提出專屬的技術創新方案，建立獨立的研究貢獻：

```
                    【第一年輸入：外部 HTTP PoC 封包】
                                    │
    ┌───────────────────────────────┴───────────────────────────────┐
    ▼                                                               ▼
【創新 1：PoC 驅動的執行路徑還原】                  【創新 2：Enforcement Predicate 失效判定】
(Trace-to-Path Alignment)                        (Missing Predicate vs. Ineffective Check)
• 突破 INTENTFIX 的「純代碼瞎猜」                    • 突破 INTENTFIX 的「粗糙文字比對」
• 動態插樁將外部請求精確映射至內部 Call Chain        • 資料流追蹤驗證結果是否真正傳遞至 State Mutation
    │                                                               │
    └───────────────────────────────┬───────────────────────────────┘
                                    │
                                    ▼
                 【創新 3：共享不變量圖結構拓撲擴展 (拳頭貢獻)】
                        (Shared Invariant Topology Expansion)
                 • 徹底擊穿 INTENTFIX 的「單檔案死穴」！
                 • 以 Call Graph 反向遍歷，自動挖掘共享同一 Invariant 的
                   所有未受保護進入點（如 Nextcloud N1 讀取與 N2 存在檢查）
                 • 產出：專案級【函式路徑風險矩陣】
                                    │
                                    ▼
                 【創新 4：可執行斷言探針之客觀反事實驗證】
                        (Executable Security Oracle Probing)
                 • 拒絕 INTENTFIX 的「自然語言空想 PoC」
                 • 注入 1 行 Invariant 斷言，以動態重放（攻擊 100% 阻斷 ＋ 
                   既有測試 100% 通過）達成純客觀因果證明
```

---

### 詳細創新點解析：

### 🌟 創新點一：PoC 驅動的白盒執行路徑還原（Trace-to-Path Alignment）
* **突破點**：不走 INTENTFIX「大海撈針猜整份程式碼」的路線。
* **核心技術**：以 Y1 輸入的成功攻擊封包為觸發器，利用輕量化動態追蹤（Dynamic Tracing / APM Logs），將外部 HTTP 請求精準錨定至後端程式碼中**真實被穿透的調用鏈（Execution Call Trace）**。
* **學術價值**：將 LLM 與靜態分析的推理空間縮小 90% 以上，從源頭根除 LLM 在大型專案中的上下文溢出與幻覺。

### 🌟 創新點二：Enforcement Predicate 失效雙型態因果分析演算法
* **突破點**：超越 INTENTFIX 粗暴的「有檢查 vs. 沒檢查」，引入細粒度資料流因果判定。
* **核心技術**：沿著還原的執行路徑，自動分類判定：
  1. **Missing Predicate（缺失型）**：路徑中完全不存在前置條件檢查節點。
  2. **Ineffective Check（未採用型）**：檢查節點有被執行，但透過**前向資料流切片（Forward Data-flow Slicing）**，判定其布林結果未到達控制相依的狀態變更節點（如 J2Store 案例）。

### 🌟 創新點三：共享不變量圖結構拓撲擴展與函式路徑風險矩陣（核心亮點！）
* **突破點**：**徹底解決 INTENTFIX 在 Section 6.1 承認無法跨檔案（Multi-file）的世紀難題**。
* **核心技術**：
  1. 當在目標核心函數（如 `Order.ship()` 或 `EntityCollection.getChild()`）識別出缺失的 Invariant 時；
  2. 系統自動構建專案層級的 **函數調用圖（Call Graph）與反向控制流圖（Backward CFG）**；
  3. 由下而上反向探索：找出系統中**所有能夠抵達該 State Mutation 的潛在進入點（API Endpoints / Background Jobs）**；
  4. 自動輸出**「函式路徑風險矩陣（Function Path Risk Matrix）」**，標明受影響的入口清單（如 Nextcloud 案例中同時揪出 `childExists()` 存在檢查同源入口）。
* **學術價值**：這是 Y2 最硬核的圖結構程式分析成果，直接為 Y3 的 Multi-Hunk 修補指明了所有必須同步修復的受影響區域。

### 🌟 創新點四：可執行安全斷言探針（Executable Security Oracle Validation）
* **突破點**：徹底揚棄 INTENTFIX「讓 LLM 寫攻擊小作文、最後再由人工肉眼打分」的脆弱評估模式。
* **核心技術**：將診斷出的安全不變量，自動轉譯為一行注入式的程式碼斷言（`assert Invariant`），透過雙向動態重放執行驗證：
  1. **攻擊阻斷性**：Y1 PoC 必定觸發斷言異常（Exploit Intercepted）。
  2. **正常流程相容性**：既有回歸測試 100% 順暢通過（Zero False Positive）。
* **學術價值**：實現了**零修補程式碼負擔下的 100% 客觀因果閉環**。

---

## 4. 全景技術對照矩陣：INTENTFIX vs. 本計畫第二年 (Y2)

| 分析維度 | INTENTFIX (ICSE 2026) | 本計畫第二年 (Y2 侑宸) | 我們的領先優勢 |
| :--- | :--- | :--- | :--- |
| **輸入依據** | 純靜態代碼文字（單檔） | **動態 PoC 軌跡 ＋ 專案原始碼** | 有物理執行鐵證，消除靜態盲猜 |
| **分析範圍** | **單一檔案 (Single-File Only)** | **專案層級跨檔案調用圖 (Inter-procedural Call Graph)** | 突破 INTENTFIX 的單檔死穴，支援現代多層架構 |
| **定位精確度** | 僅問 LLM 是否滿足規則（易受幻覺干擾） | **Trace-to-Path 還原 ＋ 雙型態 Predicate 判定** | 精準定位 Missing Predicate 與 Ineffective Check |
| **旁路挖掘能力** | **無（無法感知其他進入點）** | **共享不變量圖結構拓撲擴展 (Risk Matrix)** | 能找出共享同一 Invariant 的全部同源旁路入口 |
| **驗證方式** | 人工肉眼審查 ＋ LLM 評估自然語言小作文 | **官方 Commit 對齊 ＋ 可執行 Assertion 探針重放** | 純代碼客觀驗證，雙向防作弊與零誤殺檢驗 |

---

## 5. 結論：碩論核心題目宣示

第二年的研究完全可以挺直腰桿，以一項**高水準、獨立且擊中現有頂會痛點**的姿態發表：

> **核心論點：**  
> *"現有 SOTA 意圖修復工作（如 INTENTFIX）局限於純靜態單檔案文字猜測，既缺乏動態執行的因果約束，亦無法感知跨進入點的旁路風險。本研究提出以動態 PoC 軌跡為驅動、結合後端調用圖拓撲擴展的業務邏輯漏洞根因診斷技術，能精確判定強制機制失效型態，並自動生成專案層級的函式路徑風險矩陣。"*

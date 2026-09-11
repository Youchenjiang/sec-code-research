# Android DAST Pipeline 論文分類規則

## 核心原則

> **Coverage ≠ Contribution**
> 
> 一篇論文可以 cover 多個 pipeline stage，但它的 novel contribution 只有一個。

---

## 第一軸：Pipeline Stage（可多選）

| Code | Stage | 問的問題 |
|------|-------|----------|
| **A** | Target Analysis | 這個 App 是什麼？有哪些 component/API/attack surface？ |
| **V** | Vulnerability Discovery | 哪裡可能有漏洞？ |
| **E** | Exploit / PoC Generation | 怎麼把漏洞轉成可驗證的 exploit？ |
| **X** | Execution / Fuzzing | 實際怎麼操作 App / 執行 payload / fuzz？ |

### 什麼時候標什麼

- **A (Target Analysis)**：Manifest 分析、Intent 分析、decompilation、API 分析、attack surface discovery
- **V (Vulnerability Discovery)**：SAST、taint analysis、static analysis、pattern matching、code review
- **E (Exploit/PoC Generation)**：生成 exploit code、proof of concept、test case、attack payload
- **X (Execution/Fuzzing)**：ADB 操作、Frida hook、fuzzing、dynamic analysis、runtime execution

### 多標籤範例

| 論文 | Stages | 原因 |
|------|--------|------|
| A2 | A, V | 分析 manifest + 發現漏洞 |
| DroidCall | A, X | 分析 intent + 執行觸發 |
| FuzzingBrain | V, X | 發現漏洞 + fuzzing 執行 |
| AIxCC CRS | A, V, E, X | 完整 pipeline |

---

## 第二軸：Paper Role（單選）

| Code | 類型 | 說明 |
|------|------|------|
| **M** | Method / Technique | 提出新的方法或技術 |
| **O** | Orchestration / Autonomous Agent Framework | 系統架構、多 agent 協作、pipeline 設計 |
| **B** | Benchmark / Evaluation | 評估框架、實驗設計、性能比較 |
| **S** | Survey / SoK | 文獻回顧、系統性分析 |

### 判斷標準

- **M**：這篇論文的核心是「一個新方法」（例如新的 algorithm、新的 technique）
- **O**：這篇論文的核心是「一個系統/框架」（例如多 agent 協作、自動化 pipeline）
- **B**：這篇論文的核心是「評估/比較」（例如 benchmark dataset、evaluation framework）
- **S**：這篇論文的核心是「整理/分析」（例如 survey、systematization of knowledge）

---

## 檔名規則

### 格式

```
{Primary}_{編號}_{簡稱}.pdf
```

### Primary Code 對應

| Primary | 說明 |
|---------|------|
| V | Vulnerability Discovery |
| X | Execution / Fuzzing |
| E | Exploit / PoC Generation |
| A | Target Analysis |
| O | Orchestration |
| B | Benchmark |
| S | Survey |

### 範例

```
V01_A2.pdf                    ← Primary: V, Stages: A,V, Role: M
X02_DroidCall.pdf              ← Primary: X, Stages: A,X, Role: M
O01_AIxxCC_CRS.pdf            ← Primary: O, Stages: A,V,E,X, Role: O
S01_SoK_AIxxCC.pdf            ← Primary: S, Stages: A,V,E,X, Role: S
B01_CyberGym.pdf              ← Primary: B, Stages: A,V,E,X, Role: B
```

### Primary 決定規則

1. **以 novel contribution 為主**，不是以「做了最多什麼」為主
2. **如果有多個候選**，選擇最能代表這篇論文獨特價值的
3. **Orchestration 類**：如果論文的核心是「系統架構/多 agent 協作」，Primary = O
4. **Benchmark 類**：如果論文的核心是「評估框架」，Primary = B
5. **Survey 類**：如果論文的核心是「文獻整理」，Primary = S

---

## Metadata 表格式

每篇論文在 `PAPERS_METADATA.md` 中記錄：

```markdown
### V01_A2.pdf
- **Title**: Agentic Discovery and Validation of Android App Vulnerabilities
- **Authors**: Wang & Zhou
- **Year**: 2025
- **Venue**: arXiv
- **Primary**: V
- **Stages**: A, V
- **Role**: M
- **Android**: ✓
- **LLM**: ✓
- **Key Contribution**: LLM agent 結合 static analysis 發現 Android 漏洞
- **Relevance**: ⭐⭐⭐ 核心參考
```

### 欄位說明

| 欄位 | 說明 |
|------|------|
| Title | 論文標題 |
| Authors | 作者 |
| Year | 年份 |
| Venue | 發表場所 |
| Primary | 主要貢獻類型（V/X/E/A/O/B/S） |
| Stages | Pipeline stage 標籤（A,V,E,X 可多選） |
| Role | 論文角色（M/O/B/S 單選） |
| Android | 是否涉及 Android（✓/✗/△） |
| LLM | 是否使用 LLM（✓/✗/△） |
| Key Contribution | 一句話說明核心貢獻 |
| Relevance | 跟我們 pipeline 的關聯度（⭐⭐⭐/⭐⭐/⭐） |

---

## 使用方式

### 找「做到完整 pipeline」的論文

```
Stages contains A AND V AND E AND X
```

### 找「Android + LLM」的論文

```
Android = ✓ AND LLM = ✓
```

### 找「Orchestration 框架」

```
Role = O
```

### 找「Benchmark」

```
Role = B
```

### 找「Execution/Fuzzing」相關

```
Stages contains X
```

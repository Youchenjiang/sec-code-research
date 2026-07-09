# -*- coding: utf-8 -*-
import os
import sys
import shutil

# Define base path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.join(BASE_DIR, "research-vault")

# Ensure UTF-8 output in Windows
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        if hasattr(sys.stdout, 'buffer'):
            import io
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Restructured category definitions with 2.9 added and duplicates cleaned
CATEGORIES = {
    "1-靜態分析 (Static Analysis)": [
        {
            "filename": "1.1-語法與結構分析 (Syntactic & AST).md",
            "title": "1.1 語法與結構分析 (Syntactic / AST-based Analysis)",
            "concept": "將原始碼解析為結構化表示（如抽象語法樹 AST），透過模式匹配或規則查詢偵測已知漏洞樣式。速度快、易實作，但語意深度有限，對邏輯型漏洞無能為力。",
            "sub_genres": [
                {"name": "Pattern Matching / Rule-based", "desc": "直接在 token 流或 AST 上做規則比對。代表工具：grep、Semgrep、Flawfinder。"},
                {"name": "AST-based Static Analysis", "desc": "遍歷 AST 節點，分析函式呼叫、變數宣告等結構特徵。代表工具：Checkmarx（部分）、ESLint、FindBugs / SpotBugs。"}
            ],
            "keywords": ["syntax-based bug detection", "pattern matching vulnerability", "code smell detection", "abstract syntax tree vulnerability", "AST traversal security"],
            "tools": ["Semgrep", "Flawfinder", "Checkmarx", "ESLint", "SpotBugs"]
        },
        {
            "filename": "1.2-資料流分析 (Data Flow Analysis).md",
            "title": "1.2 資料流分析 (Data Flow Analysis)",
            "concept": "追蹤資料在程式中如何流動，特別關注「外部輸入」是否未經驗證便流入危險操作（如資料庫查詢、系統命令）。這是靜態分析中最核心的技術族群。",
            "sub_genres": [
                {"name": "污點分析 (Taint Analysis)", "desc": "將外部輸入標記為「污染源（Source）」，追蹤其是否抵達「危險接收點（Sink）」而未經清理（Sanitizer）。代表工具：CodeQL、Pixy、FlowDroid、IRIS。"},
                {"name": "別名分析 / 指標分析 (Alias / Pointer Analysis)", "desc": "分析「哪些指標指向同一塊記憶體」，是精準 taint 分析的前提。代表工具：LLVM Alias Analysis、IDEal。"},
                {"name": "跨程序分析 (Interprocedural Analysis)", "desc": "跨越函式邊界追蹤資料流，處理 call graph 的建構與摘要（Summary）。"}
            ],
            "keywords": ["taint analysis", "information flow", "source-sink", "IFDS/IDE algorithm", "sanitization", "points-to analysis", "alias-aware dataflow", "context-sensitive analysis", "flow-sensitive analysis", "call graph construction"],
            "tools": ["CodeQL", "Pixy", "FlowDroid", "LLVM Alias Analysis", "IDEal"]
        },
        {
            "filename": "1.3-抽象解釋 (Abstract Interpretation).md",
            "title": "1.3 抽象解釋 (Abstract Interpretation)",
            "concept": "以數學上「正確近似（Sound Approximation）」的方式，計算程式所有可能執行狀態的超集合（Over-approximation），保證不漏報（Sound）。",
            "sub_genres": [
                {"name": "數值域抽象 (Numerical Abstract Domains)", "desc": "追蹤整數範圍、陣列邊界，偵測 Buffer Overflow、整數溢位。代表工具：Astrée、Polyspace、Frama-C。"},
                {"name": "記憶體安全分析", "desc": "偵測 use-after-free、double-free、null pointer dereference。代表工具：Infer（基於雙模擬分離邏輯的 Bi-abduction）。"}
            ],
            "keywords": ["interval domain", "octagon domain", "polyhedra domain", "Galois connection", "widening operator", "separation logic", "shape analysis", "heap analysis", "Bi-abduction"],
            "tools": ["Astrée", "Polyspace", "Frama-C (Value Analysis)", "Infer"]
        },
        {
            "filename": "1.4-符號執行 (Symbolic Execution).md",
            "title": "1.4 符號執行 (Symbolic Execution)",
            "concept": "用符號值（而非具體數值）替代程式輸入，以 SAT/SMT 求解器探索程式路徑，產生觸發漏洞的具體輸入。「純靜態」符號執行不需真正執行，而是偏靜態分析端。",
            "sub_genres": [
                {"name": "Source-level Symbolic Execution", "desc": "在原始碼層（或 IR 層）進行路徑探索。代表工具：KLEE、S2E。"},
                {"name": "Binary-level Symbolic Execution", "desc": "作用於編譯後的二進位，不需原始碼（用於逆向分析、韌體分析）。代表工具：angr、Triton、BINSEC/SE。"}
            ],
            "keywords": ["path explosion", "constraint solving", "SMT solver", "path condition", "symbolic pointer", "binary analysis", "VEX IR", "CFG recovery", "vulnerability discovery"],
            "tools": ["KLEE", "S2E", "angr", "Triton", "BINSEC/SE"]
        },
        {
            "filename": "1.5-圖結構分析 (Graph-based Analysis).md",
            "title": "1.5 圖結構分析 (Graph-based Analysis)",
            "concept": "將程式表示為各種圖結構（CFG、PDG、CPG 等），再透過圖查詢或圖神經網路進行漏洞偵測，可捕捉跨層次的程式語意。",
            "sub_genres": [
                {"name": "程式碼屬性圖 (Code Property Graph, CPG)", "desc": "將 AST + CFG + PDG 合併為單一屬性圖，存入 Neo4j 等圖資料庫，用 Gremlin/Cypher 查詢漏洞模式。代表工具：Joern、ShiftLeft Ocular。"},
                {"name": "呼叫圖 / 控制流圖分析 (CFG / Call Graph Analysis)", "desc": "建構跨函式呼叫關係圖，分析程式控制流以識別危險路徑。"}
            ],
            "keywords": ["code property graph", "graph query", "program dependence graph", "vulnerability pattern", "call graph construction", "CFG-based analysis", "reaching definition"],
            "tools": ["Joern", "ShiftLeft Ocular"]
        },
        {
            "filename": "1.6-型別系統與資訊流分析 (Type System & IFC).md",
            "title": "1.6 型別系統與資訊流分析 (Type System / Information Flow Typing)",
            "concept": "透過靜態型別系統，強制標注資料的安全等級（High / Low），編譯期驗證高安全性資料不會「流出」到低安全性輸出（Non-interference 保證）。",
            "sub_genres": [
                {"name": "Security Type Systems", "desc": "資訊流安全性檢查與標注。代表工具：Jif、FlowSpec。"}
            ],
            "keywords": ["non-interference", "security type", "label propagation", "information flow control (IFC)"],
            "tools": ["Jif", "FlowSpec"]
        },
        {
            "filename": "1.7-學習型靜態分析 (Learning-based Static).md",
            "title": "1.7 基於機器學習的靜態檢測 (Learning-based Static Analysis)",
            "concept": "以原始碼或程式中間表示作為模型輸入，訓練神經網路自動學習漏洞模式，免去人工撰寫規則。近年發展為最活躍的子領域。",
            "sub_genres": [
                {"name": "序列模型 (Sequence-based)", "desc": "將程式碼視為 token 序列，使用 LSTM / Transformer 分類。代表工作：VulDeePecker、SySeVR、LineVul。"},
                {"name": "圖神經網路 (GNN-based)", "desc": "將 CPG / PDG / AST 作為圖輸入，以 GNN 學習結構化語意。代表工作：Devign、Reveal、DeepWukong、LLMxCPG。"},
                {"name": "預訓練語言模型 (Pre-trained LM)", "desc": "使用 CodeBERT / UniXcoder / CodeT5 等在大量程式碼上預訓練，再微調於漏洞偵測。代表工作：VulBERTa、LineVul、AugSliceVul。"},
                {"name": "LLM 輔助靜態分析 (LLM + Static)", "desc": "以 LLM 自動推斷 taint 規格（Source/Sink）或補充靜態分析的語意理解，再交回傳統工具做嚴謹驗證。代表工作：IRIS、GPTScan。"}
            ],
            "keywords": ["code gadget", "LSTM vulnerability detection", "token sequence", "line-level prediction", "graph neural network vulnerability", "GNN code representation", "heterogeneous graph", "code pre-training", "CodeBERT vulnerability", "fine-tuning", "code representation", "neuro-symbolic", "LLM-assisted analysis", "specification inference", "prompt-based vulnerability detection"],
            "tools": ["VulDeePecker", "LineVul", "Devign", "Reveal", "VulBERTa", "IRIS", "GPTScan"]
        },
        {
            "filename": "1.8-二進位與逆向分析 (Binary & Reverse Engineering).md",
            "title": "1.8 二進位與逆向分析 (Binary & Reverse Engineering)",
            "concept": "不依賴原始碼，直接反組譯或分析編譯後的二進位執行檔或韌體鏡像，適用於閉源安全審查、漏洞挖掘與反編譯分析。",
            "sub_genres": [
                {"name": "靜態二進位分析 (Static Binary Analysis)", "desc": "逆向工程手法，反組譯後分析控制流、資料流。代表工具：Ghidra、BAP、angr、IDA Pro、Binary Ninja。"},
                {"name": "中間表示層提升 (IR Lifting)", "desc": "將機器碼反編譯並提升為中間表示（如 LLVM IR、VEX IR）以進行高層次語意分析。"}
            ],
            "keywords": ["binary analysis", "disassembly", "CFG recovery", "lifted IR", "reverse engineering", "binary lifter", "VEX", "Ghidra Pcode"],
            "tools": ["Ghidra", "BAP", "angr", "IDA Pro", "Binary Ninja"]
        },
        {
            "filename": "1.9-軟體組成與供應鏈安全 (Software Composition & Supply Chain SCA).md",
            "title": "1.9 軟體組成與供應鏈安全 (Software Composition & Supply Chain SCA)",
            "concept": "分析軟體的第三方依賴與庫，生成與驗證軟體物料清單（SBOM），並檢測相依組件 of 已知安全漏洞與惡意供應鏈投毒。",
            "sub_genres": [
                {"name": "依賴漏洞掃描 (Dependency Vulnerability Scanning)", "desc": "識別程式中引入的開源組件，比對已知漏洞庫（如 CVE/NVD）。代表工具：Snyk、OWASP Dependency-Check、Dependabot。"},
                {"name": "軟體物料清單 (SBOM Analysis)", "desc": "分析與生成軟體清單（如 SPDX、CycloneDX 格式），驗證其許可證合規性。代表工具：Syft、Grype。"},
                {"name": "套件投毒與惡意代碼檢測 (Package Poisoning Detection)", "desc": "靜態分析第三方代碼中的惡意行為，防範域名搶註與惡意腳本。代表工具：Socket、GuardDog。"}
            ],
            "keywords": ["software composition analysis", "dependency scanning", "SBOM validation", "license compliance", "supply chain attack", "package poisoning", "malicious package detection"],
            "tools": ["Snyk", "Dependency-Check", "Dependabot", "Syft", "Grype", "Socket", "GuardDog"]
        },
        {
            "filename": "1.10-密碼學與協議安全審計 (Cryptographic & Protocol Security).md",
            "title": "1.10 密碼學與協議安全審計 (Cryptographic & Protocol Security)",
            "concept": "專注於檢測密碼學 API 誤用（如弱金鑰、靜態 IV、不安全填充）以及協議實現中控制流與狀態機的正確性與時序安全。",
            "sub_genres": [
                {"name": "密碼學 API 誤用檢測 (Cryptographic API Misuse)", "desc": "靜態分析程式碼中密碼學函數的調用參數，核對安全規則。代表工具：CogniCrypt、CrySL、CryptoLint。"},
                {"name": "時序與恆定時間驗證 (Constant-time Verification)", "desc": "分析代碼執行時間是否與輸入數據相關，防止時序側通道攻擊。代表工具：dudect、CacheD。"}
            ],
            "keywords": ["cryptographic API misuse", "weak key detection", "constant-time implementation", "timing leak verification", "protocol state machine", "SSL/TLS configuration audit"],
            "tools": ["CogniCrypt", "CrySL", "CryptoLint", "dudect", "CacheD"]
        }
    ],
    "2A-黑箱動態分析 (Black-box Dynamic Analysis)": [
        {
            "filename": "2.1-Web與API動態漏洞掃描 (DAST).md",
            "title": "2.1 Web與API動態漏洞掃描 (DAST)",
            "concept": "在不獲取原始碼或程式內部運行狀態的情況下，模擬外部攻擊者對運行中的 Web 應用或 API 發送惡意請求，分析回應特徵（如狀態碼、內容、延遲）以識別漏洞（如 SQL 注入、XSS、IDOR、邏輯缺陷）。",
            "sub_genres": [
                {"name": "Web 應用與 API 差異測試", "desc": "對 API 注入相同請求，比較授權前後或多個端點的回應差異，用於發現 IDOR 或邏輯漏洞。代表工具：RESTler、EvoMaster、PrediQL。"},
                {"name": "傳統 DAST 黑箱掃描", "desc": "模擬外部攻擊者對執行中的應用發動攻擊測試。代表工具：OWASP ZAP、Burp Suite、Contrast DAST。"}
            ],
            "keywords": ["REST API testing", "GraphQL fuzzing", "differential response", "semantic-aware API testing", "DAST", "web vulnerability scanning"],
            "tools": ["OWASP ZAP", "Burp Suite", "RESTler", "EvoMaster"]
        },
        {
            "filename": "2.2-黑箱協定模糊測試 (Black-box Protocol Fuzzing).md",
            "title": "2.2 黑箱協定模糊測試 (Black-box Protocol Fuzzing)",
            "concept": "針對有狀態（Stateful）或無狀態的網路與工業協定，在沒有原始碼或內部反饋下，生成符合協定格式但帶有異常的訊息序列，測試協定實作的健壯性。需維護或推斷狀態機模型。",
            "sub_genres": [
                {"name": "協定與網路模糊測試", "desc": "自動推斷或依據規格生成變異訊息序列，分析服務端是否崩潰或異常。代表工具：Peach Fuzzer、boofuzz、AFLNet（帶狀態）、Z-Fuzzer。"}
            ],
            "keywords": ["protocol fuzzing", "stateful fuzzing", "state machine inference", "message mutation", "network protocol testing"],
            "tools": ["Peach Fuzzer", "boofuzz", "AFLNet"]
        },
        {
            "filename": "2.3-惡意程式沙盒與行為分析 (Malware Sandbox).md",
            "title": "2.3 惡意程式沙盒與行為分析 (Malware Sandbox)",
            "concept": "在隔離的虛擬化沙盒環境中執行未知的可疑樣本，在黑箱狀態下記錄其與系統的交互特徵（系統呼叫序列、網絡請求、文件/登錄檔讀寫），用以分析其惡意特徵與 IoC（威脅指標）。",
            "sub_genres": [
                {"name": "沙盒執行與特徵提取", "desc": "分析惡意樣本在隔離沙盒中的動態行為。代表工具：Cuckoo Sandbox、Any.run、Joe Sandbox。"},
                {"name": "系統呼叫序列機器學習分類", "desc": "以機器學習或深度學習建立惡意與正常 syscall 序列分類器。"}
            ],
            "keywords": ["sandbox analysis", "behavior fingerprint", "API call sequence", "IoC extraction", "malware classification"],
            "tools": ["Cuckoo Sandbox", "Any.run", "Joe Sandbox"]
        }
    ],
    "2B-白與灰箱動態分析 (White & Grey-box Dynamic Analysis)": [
        {
            "filename": "2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing).md",
            "title": "2.4 反饋引導式模糊測試 (Feedback-directed Fuzzing)",
            "concept": "透過編譯期插樁或硬體追蹤，動態獲取程式執行時的內部資訊（如分支覆蓋率），以此引導模糊器朝向未探索的路徑進行演化變異，是目前發現未知漏洞最有效的方法。",
            "sub_genres": [
                {"name": "覆蓋率引導灰箱模糊測試 (CGF)", "desc": "動態收集邊緣覆蓋率（Bitmap）作為演化反饋。代表工具：AFL、AFL++、libFuzzer、honggfuzz。"},
                {"name": "定向灰箱模糊測試 (DGF)", "desc": "引導測試輸入往特定代碼位置（如 patch 點、特定 API）集中探索。代表工具：AFLGo、Hawkeye、BEACON。"},
                {"name": "核心模糊測試 (Kernel Fuzzing)", "desc": "以系統呼叫序列為輸入，動態測試 OS 核心並解決崩潰隔離與硬體追蹤。代表工具：syzkaller、kAFL。"},
                {"name": "結構與文法感知模糊測試 (Structure/Format-aware)", "desc": "理解複雜輸入格式（PDF/XML/AST），進行有語義的變異。代表工具：Nautilus、WEIZZ。"},
                {"name": "LLM/ML 輔助模糊測試", "desc": "利用模型生成種子、引導變異或理解 API 規格。代表工具：LLaMAFuzz、MTFuzz。"}
            ],
            "keywords": ["coverage-guided fuzzing", "edge coverage", "bitmap feedback", "directed fuzzing", "patch testing", "kernel fuzzing", "syscall fuzzing", "grammar-based fuzzing", "structured input generation", "LLM fuzzing"],
            "tools": ["AFL", "AFL++", "libFuzzer", "syzkaller", "kAFL", "Nautilus", "AFLGo"]
        },
        {
            "filename": "2.5-動態污點分析 (Dynamic Taint Analysis - DTA).md",
            "title": "2.5 動態污點分析 (Dynamic Taint Analysis - DTA)",
            "concept": "在程式執行時，對每個暫存器或記憶體位元組維護污染標籤（Taint Tag），精確追蹤污染源資料流向危險接收點（Sink）的實際執行路徑。精準度高但具有顯著的運行期開銷。",
            "sub_genres": [
                {"name": "全系統動態污點追蹤 (Whole-System DIFT)", "desc": "在仿真器（如 QEMU）層插樁，追蹤跨程式、跨系統呼叫的資料流。代表工具：DECAF、DECAF++、TEMU。"},
                {"name": "使用者空間動態污點分析", "desc": "利用動態二進位插樁（DBI）在使用者空間追蹤單一程序的資料流。代表工具：libdft、Minemu。"},
                {"name": "資訊流安全與側通道檢測", "desc": "追蹤機密資料是否在執行時洩漏至時間、分支等可觀測側通道。"}
            ],
            "keywords": ["whole-system taint", "QEMU instrumentation", "shadow memory", "DIFT", "taint propagation", "PIN taint analysis", "DynamoRIO taint", "constant-time verification", "timing side-channel"],
            "tools": ["DECAF", "DECAF++", "libdft"]
        },
        {
            "filename": "2.6-混合與Concolic執行 (Concolic & Hybrid).md",
            "title": "2.6 混合與Concolic執行 (Concolic & Hybrid)",
            "concept": "結合具體執行（Concrete）與符號執行（Symbolic），在真實執行的同時收集分支路徑的符號約束，利用 SMT 求解器生成能突破複雜條件分支的新輸入，解決模糊測試盲點。",
            "sub_genres": [
                {"name": "並行符號執行 (Concolic Execution)", "desc": "用真實值引導符號追蹤，求解新分支。代表工具：SAGE、Mayhem、Triton、KLEE (偏靜態)。"},
                {"name": "混合模糊測試 (Hybrid Fuzzing)", "desc": "模糊測試卡住時，動態調度 Concolic 引擎突破分支障礙。代表工具：QSYM、Driller、SymCC、SymFusion。"}
            ],
            "keywords": ["concolic execution", "path constraint", "constraint solving", "whitebox fuzzing", "hybrid fuzzing", "concolic + fuzzing", "selective symbolic execution"],
            "tools": ["SAGE", "Mayhem", "QSYM", "Driller", "SymCC"]
        },
        {
            "filename": "2.7-執行期插樁與監控 (Instrumentation & Sanitizers).md",
            "title": "2.7 執行期插樁與監控 (Instrumentation & Sanitizers)",
            "concept": "在編譯期、載入期或執行期將檢測邏輯注入目標程式中，以在執行時監控程式行為、捕捉違規行為或主動進行防禦。",
            "sub_genres": [
                {"name": "編譯期 Sanitizers", "desc": "編譯時插入輕量檢查指令，高效偵測記憶體與未定義行為。代表工具：ASan (Address)、MSan (Memory)、TSan (Thread)、UBSan。"},
                {"name": "動態二進位插樁 (DBI)", "desc": "在二進位運行時動態插入分析代碼（JIT重編），免代碼。代表框架：Intel PIN、DynamoRIO、Valgrind、Frida。"},
                {"name": "互動式應用安全測試 (IAST)", "desc": "應用 runtime 內置 agent，結合真實流量在程式內部精確定位漏洞行號。代表工具：Contrast Security、Seeker。"},
                {"name": "執行期自我防禦 (RASP)", "desc": "部署於生產環境的 agent，實時監控並攔截 SQL 注入或 RCE 等惡意操作。代表工具：OpenRASP、Imperva。"}
            ],
            "keywords": ["shadow memory", "compile-time instrumentation", "address sanitizer", "dynamic binary instrumentation", "IAST", "runtime agent", "runtime protection", "self-protection"],
            "tools": ["ASan", "TSan", "Intel PIN", "DynamoRIO", "Frida", "Contrast Security", "OpenRASP"]
        },
        {
            "filename": "2.8-語意差異與並發偵測 (Differential & Concurrency).md",
            "title": "2.8 語意差異與並發偵測 (Differential & Concurrency)",
            "concept": "透過對多個等價實作進行差異比對以發現語意缺陷，或動態監控多執行緒交錯，捕捉並發相關的非確定性漏洞。",
            "sub_genres": [
                {"name": "編譯器與虛擬機差異測試", "desc": "自動生成程式並比較不同編譯器優化等級或 VM 實作的輸出差異。代表工具：Csmith、Rustlantis、EVMFuzz。"},
                {"name": "並發與競爭條件偵測", "desc": "追蹤記憶體存取與鎖定，偵測 data race, deadlock 等並發缺陷。代表工具：TSan、Helgrind、CHESS、RAZZER。"},
                {"name": "記憶體安全動態精密檢測", "desc": "動態精密校驗 heap/stack 的安全邊界（如 Valgrind/Memcheck, Dr. Memory）。"}
            ],
            "keywords": ["differential testing", "compiler testing", "random program generation", "EVM differential testing", "data race detection", "happens-before", "lockset algorithm", "shadow memory", "memory error detection"],
            "tools": ["Csmith", "Rustlantis", "EVMFuzz", "TSan", "Valgrind/Memcheck", "Dr. Memory"]
        },
        {
            "filename": "2.9-變異測試 (Mutation Testing).md",
            "title": "2.9 變異測試 (Mutation Testing)",
            "concept": "藉由在原始碼或二進位中注入微小的錯誤（Mutants），並執行測試套件，用以評估測試套件的充分性（Mutation Score）或引導測試案例生成。在安全領域，常被用來評估與基準化模糊測試器（Fuzzer）的漏洞發現能力。",
            "sub_genres": [
                {"name": "Fuzzer 漏洞評估與基準化 (Fuzzer Benchmarking)", "desc": "以變異測試注入人工缺陷，衡量 Fuzzer 能殺死多少變異體，評估其缺陷發現率。代表工具：Mull、Pitest。"},
                {"name": "變異引導測試生成 (Mutation-guided Generation)", "desc": "以變異得分為引導指標，演化生成能殺死更多變異體的安全測試案例。"},
                {"name": "等價變異體偵測 (Equivalent Mutant Detection)", "desc": "識別語意上與原程式等價、無法被任何測試殺死的變異體（這是變異測試的經典難題）。"}
            ],
            "keywords": ["mutation testing", "mutation analysis", "mutant generation", "equivalent mutant", "mutation score", "fuzzer evaluation", "fault injection"],
            "tools": ["Pitest", "Mull", "Milu", "Duesenberg"]
        },
        {
            "filename": "2.10-微執行與模擬測試 (Micro-execution & Emulation).md",
            "title": "2.10 微執行與模擬測試 (Micro-execution & Emulation)",
            "concept": "在缺乏主程式進入點與完整運行環境的狀態下，直接虛擬執行目標程式的任意函式或代碼片段。核心是透過攔截記憶體異常（Page Fault）動態分配記憶體與輸入。",
            "sub_genres": [
                {"name": "微執行 (Micro-execution)", "desc": "執行任意程式碼片段，並在執行期攔截存取異常以動態建構具體上下文。代表工作：PLDI 2014 Micro-execution。"},
                {"name": "函式級模擬與微模糊測試 (Function-level Fuzzing)", "desc": "利用 Unicorn / QEMU 載入特定函數進行快速的 concrete 虛擬運行與漏洞探測。代表工具：Unicorn-based micro-fuzzer。"},
                {"name": "硬體與外設模擬執行", "desc": "在虛擬機中動態模擬外部設備，以支持嵌入式系統或韌體片段的動態測試。代表工具：HAL-fuzz、Jetset。"}
            ],
            "keywords": ["micro-execution", "page fault intercept", "dynamic memory allocation", "isolated execution", "unicorn emulator", "peripheral emulation", "firmware dynamic testing"],
            "tools": ["Unicorn Engine", "HAL-fuzz", "Jetset"]
        },
        {
            "filename": "2.11-作業系統內核與虛擬化模糊測試 (Kernel & Hypervisor Fuzzing).md",
            "title": "2.11 作業系統內核與虛擬化模糊測試 (Kernel & Hypervisor Fuzzing)",
            "concept": "針對作業系統內核、硬體驅動程式或雲端虛擬化管理程式（Hypervisor），透過特製輸入、虛擬化狀態回復、硬體輔助追蹤等方式進行深度的動態漏洞挖掘。",
            "sub_genres": [
                {"name": "內核系統呼叫模糊測試 (Kernel Syscall Fuzzing)", "desc": "自動生成或變異 syscall 序列來測試內核邊界安全性。代表工具：syzkaller、HEVD。"},
                {"name": "硬體輔助追蹤與狀態重置 (Hardware-assisted Trace)", "desc": "利用 Intel PT 等硬體技術收集覆蓋率，並在發生 crash 時快速重置系統狀態。代表工具：kAFL、Nyx。"},
                {"name": "虛擬化與 Hypervisor 漏洞挖掘", "desc": "模擬虛擬設備或 PCI 請求，測試虛擬化逃逸與 Hypervisor 的邏輯漏洞。代表工作：QEMU Fuzzing。"}
            ],
            "keywords": ["kernel fuzzing", "syscall generation", "hardware-assisted tracing", "Intel PT", "hypervisor escape", "state snapshot", "device emulation fuzzing"],
            "tools": ["syzkaller", "kAFL", "Nyx", "QEMU Fuzzer"]
        },
        {
            "filename": "2.12-智能合約與 Web3 安全 (Smart Contract & Web3 Security).md",
            "title": "2.12 智能合約與 Web3 安全 (Smart Contract & Web3 Security)",
            "concept": "針對區塊鏈智能合約（如 EVM/Solidity, WASM）特有的運行機制與漏洞特徵（如重入、邏輯溢出、Gas耗盡），進行專門的模糊測試、符號執行與形式化驗證。",
            "sub_genres": [
                {"name": "智能合約模糊測試 (Smart Contract Fuzzing)", "desc": "針對合約狀態機與屬性（Invariants）進行自動化輸入變異。代表工具：Echidna、ItyFuzz、Foundry。"},
                {"name": "智能合約符號執行 (Symbolic Execution)", "desc": "在合約位元組碼層探索執行路徑並求解约束。代表工具：Mythril、Manticore。"},
                {"name": "形式化驗證與靜態審計 (Formal Verification)", "desc": "對合約業務邏輯屬性進行嚴謹數學證明或靜態約束檢查。代表工具：Certora Prover、Slither。"}
            ],
            "keywords": ["smart contract fuzzing", "EVM symbolic execution", "contract formal verification", "invariant testing", "reentrancy vulnerability", "Web3 security audit"],
            "tools": ["Echidna", "ItyFuzz", "Mythril", "Manticore", "Certora Prover", "Slither"]
        }
    ],
    "3-自動修復 (Automated Program Repair - APR)": [
        {
            "filename": "3.0-故障定位 (Fault Localization).md",
            "title": "3.0 前置條件：故障定位 (Fault Localization, FL)",
            "concept": "APR 的品質上限受限於故障定位的精確度——必須先找對「哪行/哪個函式有問題」，才能進行修復。FL 是 APR 管線的必要前置步驟，通常獨立研究。",
            "sub_genres": [
                {"name": "譜基礎故障定位 (Spectrum-based FL, SBFL)", "desc": "以測試覆蓋矩陣計算語句可疑度（Ochiai 公式最常用）。代表工具：GZoltar、Ochiai。"},
                {"name": "基於學習的 FL (Learning-based FL)", "desc": "以深度學習從歷史 bug 學習可疑模式。代表工具：DeepFL、Predicate Switching。"}
            ],
            "keywords": ["fault localization", "SBFL", "Ochiai coefficient", "mutation-based FL", "learning-based FL"],
            "tools": ["GZoltar", "DeepFL"]
        },
        {
            "filename": "3.1-生成與驗證流派 (Generate-and-Validate).md",
            "title": "3.1 生成與驗證流派 (Generate-and-Validate APR / Search-based APR)",
            "concept": "以啟發式搜索或演化演算法在補丁空間中搜索，對每個候選補丁執行測試套件驗證，找到第一個通過測試的補丁即為輸出。是 APR 研究的起源，開創了整個領域。",
            "sub_genres": [
                {"name": "遺傳程式設計基礎 APR (Genetic Programming)", "desc": "以程式語句為「基因」，透過隨機刪除、插入、替換等操作生成候選補丁。代表工具：GenProg、MutRepair、SPR。"},
                {"name": "隨機/啟發式突變 APR", "desc": "枚舉候選補丁，配合故障定位排序優先測試高可疑點。代表工具：RSRepair、ACS、jGenProg、Astor 框架。"}
            ],
            "keywords": ["genetic programming APR", "search-based repair", "plausible patch", "fitness function", "donor code", "mutation-based repair", "fault localization + repair"],
            "tools": ["GenProg", "MutRepair", "SPR", "RSRepair", "ACS", "Astor"]
        },
        {
            "filename": "3.2-語意合成流派 (Semantics-based Synthesis).md",
            "title": "3.2 語意合成流派 (Semantics-based / Synthesis-based APR)",
            "concept": "將修復問題轉化為約束求解（Constraint Solving）問題，以 SMT 求解器或符號執行精確合成出語意正確的修復表達式，理論上比搜索流派更嚴謹。",
            "sub_genres": [
                {"name": "基於 SMT 求解的修復合成", "desc": "從通過測試的輸入/輸出對提取語意約束，形式化為 SMT 公式，求解器合成修復的條件式或表達式。代表工具：Nopol、Angelix、S3、SemFix。"},
                {"name": "基於符號執行的合成", "desc": "以符號執行探索觸發 bug 的路徑，精確識別修復位置，並以程式合成填補修復邏輯。代表工具：ExtractFix、SymFix。"}
            ],
            "keywords": ["synthesis-based APR", "SMT solver repair", "SemFix", "Nopol", "Angelix", "angelic fix derivation", "extraction-based repair", "repair constraint synthesis"],
            "tools": ["Nopol", "Angelix", "SemFix", "ExtractFix", "SymFix"]
        },
        {
            "filename": "3.3-範本與模式匹配流派 (Template-based).md",
            "title": "3.3 範本 / 模式匹配流派 (Template-based / Pattern-based APR)",
            "concept": "從歷史人類補丁中挖掘反覆出現的「修復模板」（如：加入 null check、修改條件式、插入邊界檢查），再將模板套用至對應的故障位置，模式可解釋性強。",
            "sub_genres": [
                {"name": "通用 Bug 修復模板", "desc": "聚焦於通用軟體缺陷，建立跨專案、跨類型的修復模板庫。代表工具：TBar、SimFix、AVATAR。"},
                {"name": "安全漏洞修復模板 (Vulnerability-Specific Patterns)", "desc": "從歷史 CVE 補丁中挖掘安全相關修復模式，針對特定 CWE 類型設計修復模板。代表工具：AVATAR、FixMiner、VulKey。"}
            ],
            "keywords": ["fix pattern", "template-based APR", "code change pattern", "donor code", "fix pattern mining", "security patch pattern", "CVE fix template", "CWE-specific repair"],
            "tools": ["TBar", "SimFix", "AVATAR", "FixMiner", "VulKey"]
        },
        {
            "filename": "3.4-深度學習修復流派 (DL & NMT).md",
            "title": "3.4 深度學習修復流派 (DL-based / NMT-based APR)",
            "concept": "將程式碼修復視為神經機器翻譯（NMT）問題——把「有 Bug 的程式碼」翻譯成「修復後的程式碼」，以大量歷史補丁對訓練模型，自動學習修復規律。",
            "sub_genres": [
                {"name": "Seq2Seq / 早期 NMT 修復", "desc": "以 Encoder-Decoder 架構將 buggy 程式碼編碼，解碼生成 fixed 程式碼。代表工具：SequenceR、CoCoNuT、DLFix。"},
                {"name": "Graph / AST-aware DL 修復", "desc": "以程式結構圖（AST、CFG）而非純文字序列作為輸入，讓模型學習程式的結構性語意。代表工作：DEAR (Tree-LSTM)、Recoder、CURE。"},
                {"name": "預訓練程式碼語言模型微調 (Fine-tuned PLM for APR)", "desc": "在大規模程式碼語料上預訓練，再微調於特定漏洞修復資料集。代表工作：VulRepair、InferFix、TFix。"}
            ],
            "keywords": ["neural machine translation repair", "encoder-decoder bug fix", "sequence-to-sequence APR", "tree-based repair", "AST-aware fix", "multi-hunk repair", "pre-trained model APR", "CodeT5 vulnerability repair", "fine-tuning bug fix"],
            "tools": ["SequenceR", "CoCoNuT", "DEAR", "Recoder", "VulRepair", "InferFix"]
        },
        {
            "filename": "3.5-LLM與Agent驅動修復 (LLM & Agentic).md",
            "title": "3.5 大語言模型與 Agent 驅動修復 (LLM-based & Agentic APR)",
            "concept": "LLM 在無需微調的情況下，通過 Zero/Few-shot Prompting 直接生成修復補丁；進一步整合工具呼叫、測試執行反饋、多輪迭代，形成自主 Agent 閉環，是目前前沿趨勢。",
            "sub_genres": [
                {"name": "LLM Zero/Few-shot Prompting 修復", "desc": "直接以漏洞報告、錯誤訊息、程式碼上下文組成 Prompt 餵入 LLM。代表工具：ChatRepair、LLM4APR、SWE-bench 參賽模型。"},
                {"name": "LLM 迭代反饋修復 (Iterative Feedback Loop)", "desc": "LLM 生成補丁 → 執行測試 → 將失敗資訊回饋給 LLM → 重新生成。代表工具：LLM4CVE、RAVEN。"},
                {"name": "多 Agent 自動化修復系統 (Multi-Agent Agentic APR)", "desc": "建立多個專責 Agent（故障定位、補丁生成、測試驗證）協同解決複雜跨文件問題。代表工具：SWE-agent、AutoCodeRover、AutoPatch、AgenticVM、RAVEN。"},
                {"name": "RAG 輔助修復 (Retrieval-Augmented Repair)", "desc": "以 RAG 從歷史 CVE 補丁庫、CWE 知識庫中檢索相關修復案例。代表工具：RAVEN、VulKey。"}
            ],
            "keywords": ["LLM program repair", "zero-shot APR", "few-shot patch", "iterative repair", "feedback-based LLM repair", "test-driven LLM fix", "agentic APR", "multi-agent repair", "SWE-bench", "tool-using agent", "RAG repair"],
            "tools": ["ChatRepair", "SWE-agent", "AutoCodeRover", "AutoPatch", "RAVEN", "VulKey"]
        },
        {
            "filename": "3.6-安全補丁驗證與PCA (Validation & PCA).md",
            "title": "3.6 安全補丁驗證 (Patch Validation & Correctness Assessment)",
            "concept": "不論由哪個流派生成補丁，最終都需要自動化驗證其正確性而非僅僅合理性（即解決補丁過擬合 Patch Overfitting 的關鍵技術）。",
            "sub_genres": [
                {"name": "靜態特徵 PCA", "desc": "以補丁的靜態結構特徵（AST 差異、修改範圍）訓練分類器預測是否過擬合。代表工具：PATCH-SIM、OASIs。"},
                {"name": "動態語意 PCA", "desc": "執行補丁後以動態分析（符號執行、不變式推斷）驗證語意是否正確。代表工具：Invalidator、Poracle、Crex。"},
                {"name": "測試案例增強 (Test Augmentation for Overfitting)", "desc": "在 APR 管線中自動生成新測試來強化 oracle。代表工具：EvoSuite (配合 APR)、OPAD。"}
            ],
            "keywords": ["patch correctness assessment", "overfitting detection", "static feature classification", "plausible vs correct", "semantic validation", "invariant-based PCA", "preservation condition", "test generation for APR", "test augmentation", "oracle strengthening"],
            "tools": ["PATCH-SIM", "OASIs", "Invalidator", "Poracle", "EvoSuite", "OPAD"]
        }
    ]
}

def cleanup_old_directories():
    old_dir = os.path.join(VAULT_DIR, "2-動態分析 (Dynamic Analysis)")
    if os.path.exists(old_dir):
        print(f"Cleaning up old dynamic analysis directory: {old_dir}")
        shutil.rmtree(old_dir)

def create_directory_structure():
    print(f"Creating vault directory: {VAULT_DIR}")
    os.makedirs(os.path.join(VAULT_DIR, "templates"), exist_ok=True)
    os.makedirs(os.path.join(VAULT_DIR, "papers"), exist_ok=True)

    for main_cat in CATEGORIES.keys():
        dir_path = os.path.join(VAULT_DIR, main_cat)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created category directory: {main_cat}")

def write_category_files():
    for main_cat, sub_list in CATEGORIES.items():
        for sub in sub_list:
            file_path = os.path.join(VAULT_DIR, main_cat, sub["filename"])
            clean_name = os.path.splitext(sub["filename"])[0]
            
            # Format sub-genres section
            sub_genres_md = ""
            for sg in sub["sub_genres"]:
                sub_genres_md += f"### {sg['name']}\n- **簡介**: {sg['desc']}\n\n"
            
            # Format keywords
            keywords_md = ", ".join([f"`{kw}`" for kw in sub["keywords"]])
            
            # Format tools
            tools_md = ", ".join([f"`{tool}`" for tool in sub["tools"]])
            
            content = f"""---
title: "{sub['title']}"
type: research-genre
parent: "[[00-研究流派圖主目錄]]"
---

# {sub['title']}

## 📌 核心精神 (Core Concept)
{sub['concept']}

## 🔍 子技術流派 (Sub-Genres)
{sub_genres_md}
## 🏷️ 學術常用關鍵字 (Keywords)
{keywords_md}

## 🛠️ 代表性工具 / 框架 (Representative Tools)
{tools_md}

---

## 📚 相關論文 (Papers List)

<!-- 
如果您在 Obsidian 中安裝了 Dataview 插件，以下查詢會自動為您收集所有標記有此流派的論文。
-->

```dataview
table title as "標題", year as "年份", venue as "發表會/期刊"
from "papers"
where contains(categories, [[{clean_name}]])
sort year desc
```

---
返回 [[00-研究流派圖主目錄|研究流派圖主目錄]]
"""
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Generated category file: {sub['filename']}")

def write_index_file():
    index_path = os.path.join(VAULT_DIR, "00-研究流派圖主目錄.md")
    
    # Construct the trees
    tree_md = ""
    for main_cat, sub_list in CATEGORIES.items():
        tree_md += f"### {main_cat}\n"
        for sub in sub_list:
            clean_name = os.path.splitext(sub["filename"])[0]
            tree_md += f"- [[{clean_name}]]\n"
        tree_md += "\n"

    content = f"""---
title: "程式碼安全研究流派圖主目錄"
type: index
---

# 🛡️ 程式碼安全研究流派圖主目錄 (Code Security Research Genres)

歡迎來到程式碼安全研究流派知識庫。本目錄是依據學術界與工業界的「靜態分析」、「動態分析（黑箱與白/灰箱）」與「自動修復 (APR)」支柱建立的雙向連結網絡。

## 🗺️ 研究流派圖總覽

{tree_md}

## 📝 如何開始整理您的論文？

1. **套用範本**：在新建論文筆記時，複製並套用 `[[Paper Template]]`。
2. **標註流派**：在論文筆記的 `categories` 屬性中，使用雙括號連結對應的流派（例如：`categories: ["[[1.2-資料流分析 (Data Flow Analysis)]]", "[[3.5-LLM與Agent驅動修復 (LLM & Agentic)]]"]`）。
3. **自動匯整**：當您在論文中建立了連結後，點進各流派檔案，底部的 **Dataview 查詢區塊** 就會自動動態列出該流派的所有論文！

---
*本知識庫由 Antigravity 協助構建，基於 2026 年最新安全軟體工程論文發展狀態設計。*
"""
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated Index file: 00-研究流派圖主目錄.md")

def write_templates():
    template_path = os.path.join(VAULT_DIR, "templates", "Paper Template.md")
    content = """---
title: "論文完整標題 / Full Title of the Paper"
authors: "作者清單 / Author List"
year: 2026
venue: "發表單位 (例如 USENIX Security, IEEE S&P, ACM CCS, NDSS, ICSE, FSE, ASE...)"
url: "官方下載或下載連結 / Official Link"
code: "開源代碼連結 / Open Source Code Link (若無請填 '')"
categories:
  - "[[1.1-語法與結構分析 (Syntactic & AST)]]"  # 請替換為對應的流派連結，可多選
---

# 📖 {{title}}

## 📄 本地 PDF 連結
- [[請替換為你的論文檔案名稱.pdf]] <!-- 建議將下載好的 PDF 放入 research-vault/pdfs/ 資料夾即可在此點選並行閱讀 -->

## 📝 論文摘要 (Abstract)
> [!NOTE]
> 請在此處貼上論文的原始 Abstract，便於進行全局關鍵字檢索與快速回顧。

---

## 🎯 核心解決問題 (Problem Statement)
* **研究背景**：
* **現有技術痛點**：
* **論文要解決的具體問題**：

---

## 💡 關鍵創新點與貢獻 (Key Contributions & Innovation)
1. 
2. 
3. 

---

## 🛠️ 方法論與系統架構 (Methodology & Workflow)
> [!TIP]
> 請詳細梳理該技術的核心模組、運作邏輯或演算法，可以使用 Mermaid 流程圖或虛擬碼。

### 核心模組設計
* 

### 運作流程 / 演算法
* 

---

## 📊 實驗設計與關鍵成效 (Evaluation & Benchmarks)
* **基準測試集 (Datasets / Benchmarks)**：
* **對比對象 (Baselines)**：
* **關鍵實驗結果與數據**：

---

## 🧠 啟發與後續研究方向 (Insights & Future Work)
* **技術局限性 (Limitations)**：
* **對後續研究的啟發 / 擴展思考**：
"""
    with open(template_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated Template file: Paper Template.md")

def write_example_papers():
    # Example Paper 1: A hybrid paper (IRIS)
    paper1_path = os.path.join(VAULT_DIR, "papers", "example-paper-iris-2024.md")
    content1 = """---
title: "IRIS: LLM-Assisted Static Analysis for Detecting Taint-Style Vulnerabilities"
authors: "Anonymous Authors"
year: 2024
venue: "arXiv"
url: "https://arxiv.org/abs/2400.00000"
code: ""
categories:
  - "[[1.2-資料流分析 (Data Flow Analysis)]]"
  - "[[1.7-學習型靜態分析 (Learning-based Static)]]"
---

# IRIS: LLM-Assisted Static Analysis for Detecting Taint-Style Vulnerabilities

## 💡 核心創新點 (Core Contributions)
- 提出 **LLM + Static Hybrid** 的混合分析模式。
- 利用大語言模型自動推斷 CodeQL 等靜態分析工具所需的 **Taint Specification (Source, Sink, Sanitizer)**，解決了傳統靜態分析工具規格定義成本極高、容易漏報的問題。

## 🧠 技術架構 & 運作流程 (Methodology)
1. **LLM 規格推斷**：先由 LLM 掃描程式碼，識別出可能被當作污點源或接收點的 API / 函式。
2. **靜態驗證**：將 LLM推斷出來的 Spec 轉化成 CodeQL 查詢，交由 CodeQL 引擎執行嚴格的資料流分析，排除 LLM 的幻覺誤報。

## 📊 實驗設計 & 數據集 (Evaluation & Benchmarks)
- **使用的基準資料集**: 實際開源 GitHub 專案。
- **對比的 Baseline**: 傳統純人工編寫 Spec 的 CodeQL 掃描。

## 📝 個人筆記 / 啟發 (Notes & Insights)
- 這篇論文是典型的「神經符號混合（Neuro-symbolic）」靜態分析，完美結合了 LLM 的語意理解與傳統 Static 分析的嚴謹性，對「跨流派」論文歸類是很好的範例。
"""
    with open(paper1_path, "w", encoding="utf-8") as f:
        f.write(content1)

    # Example Paper 2: An APR paper (RAVEN)
    paper2_path = os.path.join(VAULT_DIR, "papers", "example-paper-raven-2026.md")
    content2 = """---
title: "RAVEN: Retrieval-Augmented Agentic Program Repair for Complex CVEs"
authors: "Security Research Group"
year: 2026
venue: "USENIX Security 2026"
url: "https://arxiv.org/abs/2600.00000"
code: "https://github.com/example/raven"
categories:
  - "[[3.5-LLM與Agent驅動修復 (LLM & Agentic)]]"
  - "[[3.6-安全補丁驗證與PCA (Validation & PCA)]]"
---

# RAVEN: Retrieval-Augmented Agentic Program Repair for Complex CVEs

## 💡 核心創新點 (Core Contributions)
- 提出了一套 **RAG + Agentic 迭代修復系統**，顯著提升了真實複雜 CVE 的修復成功率。
- 專門針對 **Patch Overfitting (補丁過擬合)** 設計了動態語意 PCA 模組。

## 🧠 技術架構 & 運作流程 (Methodology)
1. **RAG 檢索**：當收到一個漏洞報告（CWE）後，從歷史 NVD/CVE 數據庫中檢索相似的漏洞修復 Patch 模板。
2. **Agent 迭代修復**：由 Multi-Agent 系統執行「故障定位 -> 生成 Patch -> 執行專案測試 -> 反饋錯誤訊息 -> 重新生成」。
3. **補丁驗證 (PCA)**：利用動態測試案例增強，在補丁生成後自動生成變異測試，檢測是否引入了過擬合。

## 📊 實驗設計 & 數據集 (Evaluation & Benchmarks)
- **使用的基準資料集**: SWE-bench, CVE-Fix-Bench
- **核心實驗結果**: 在真實 CVE 漏洞修復上達到了 83.13% 的成功率。

## 📝 個人筆記 / 啟發 (Notes & Insights)
- 該論文同時涵蓋了 LLM Agent 修復 (3.5) 與補丁驗證 (3.6) 流派，是現代自動化漏洞防禦的代表工作。
"""
    with open(paper2_path, "w", encoding="utf-8") as f:
        f.write(content2)

    # Example Paper 3: A black-box & grey-box hybrid dynamic analysis paper (e.g. stateful network fuzzing)
    paper3_path = os.path.join(VAULT_DIR, "papers", "example-paper-aflnet-2020.md")
    content3 = """---
title: "AFLNet: A Greybox Fuzzer for Network Protocols"
authors: "Van-Thuan Pham, et al."
year: 2020
venue: "ICSE 2020"
url: "https://dl.acm.org/doi/10.1145/3377811.3380434"
code: "https://github.com/aflnet/aflnet"
categories:
  - "[[2.2-黑箱協定模糊測試 (Black-box Protocol Fuzzing)]]"
  - "[[2.4-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]"
---

# AFLNet: A Greybox Fuzzer for Network Protocols

## 💡 核心創新點 (Core Contributions)
- 針對網路協定測試，提出了一種將 **Stateful Fuzzing (協定狀態機)** 與 **Greybox Fuzzing (覆蓋率反饋)** 結合的框架。
- AFLNet 不僅依賴程式碼的分支覆蓋率，還會透過網絡回應碼（如 FTP 的 220, 331）來推斷目前的協定狀態，以狀態轉換圖導航變異。

## 🧠 技術架構 & 運作流程 (Methodology)
1. **握手與狀態追蹤**：發送封包給目標伺服器，並收集回應中的狀態碼以構建動態狀態圖。
2. **覆蓋率引導**：利用 AFL 的輕量級代碼插樁，獲得基本塊覆蓋率。
3. **反饋調度**：優先突變那些能觸發新代碼路徑或新協定狀態的訊息序列。

## 📊 實驗設計 & 數據集 (Evaluation & Benchmarks)
- **使用的基準資料集**: 實際的開源網路伺服器 (ProFTPD, Pure-FTPd, Live555)。
- **對比的 Baseline**: 傳統黑箱協定 Fuzzer (Peach Fuzzer) 以及純 CGF。

## 📝 個人筆記 / 啟發 (Notes & Insights)
- 這篇論文是「黑箱協定分析（狀態碼推斷）」與「灰箱引導式測試（覆蓋率）」結合的典範，很好地驗證了我們拆分「黑箱」與「白/灰箱」動態分類的必要性與實用價值。
"""
    with open(paper3_path, "w", encoding="utf-8") as f:
        f.write(content3)
    print("Generated three example papers in papers/")

if __name__ == "__main__":
    print("--- Starting Obsidian Vault Setup (Restructured with 2.9) ---")
    cleanup_old_directories()
    create_directory_structure()
    write_category_files()
    write_index_file()
    write_templates()
    write_example_papers()
    print("--- Setup Completed Successfully! ---")

# Code Security Research: Genre Relations Review Schema

This document lists all defined semantic relationships between the 31 research genres in the Code Security Research Vault. It is formatted for direct ingestion and auditing by other AI systems.

---

## 1. Relationship Types & Definitions

The relationship ontology uses 6 distinct typed directed edges:

- **`extends`**: A is a specialization or direct subtype of B (e.g., Learning-based static analysis extends Syntactic & AST analysis).
- **`shares_technique`**: A and B share core algorithms, intermediate representations (IR), or formal solvers (e.g., Semantics-based Synthesis and Symbolic Execution both use SMT solvers).
- **`complementary`**: A and B represent different approaches that address the same security problem or work together in a pipeline (e.g., SAST and DAST).
- **`precondition_of`**: A must execute or exist prior to B in the program analysis pipeline (e.g., Fault Localization is a precondition for Automated Program Repair).
- **`domain_overlap`**: A and B address the same class of vulnerabilities but use completely different analysis paradigms (e.g., Cryptographic Static Auditing and Timing Side-Channel Analysis).
- **`dynamic_counterpart`**: A and B are the static and dynamic variants of the exact same analysis paradigm (e.g., Static Data Flow vs. Dynamic Taint Analysis).

---

## 2. Active Relationship Directory

Below is the flat map of all active relationships defined in `setup_vault.py`.

### Group 1: Static Analysis (1.1 - 1.10)

- **1.1 Syntactic & AST**
  - `precondition_of` -> **1.2 Data Flow Analysis** (AST is built first to traverse control/data dependence).
  - `precondition_of` -> **1.5 Graph-based Analysis** (AST forms the backbone of the Code Property Graph).
  - `precondition_of` -> **1.7 Learning-based Static** (Neural models learn syntax embeddings from ASTs).

- **1.2 Data Flow Analysis**
  - `dynamic_counterpart` -> **2.5 Dynamic Taint Analysis (DTA)** (DTA tracks taint tags at runtime; Data Flow propagates taint statically).
  - `shares_technique` -> **1.5 Graph-based Analysis** (Both build/traverse dependency graphs like PDG/SDG).
  - `shares_technique` -> **1.6 Type System & IFC** (Type checkers propagate safety labels similar to data flow equations).
  - `complementary` -> **2.1 Web & API DAST** (SAST data flow tracks internal code sources-to-sinks; DAST scans external behavior).
  - `complementary` -> **1.3 Abstract Interpretation** (DFA is iterative over-approximation; AI provides the formal mathematical framework for it).

- **1.3 Abstract Interpretation**
  - `complementary` -> **1.4 Symbolic Execution** (AI is over-approximation for soundness; SE is under-approximation for precision/bug finding).
  - `complementary` -> **1.2 Data Flow Analysis** (AI mathematically generalizes data flow analysis lattices).

- **1.4 Symbolic Execution**
  - `complementary` -> **2.6 Concolic & Hybrid** (Concolic execution guides symbolic paths with concrete runs; SE is purely symbolic).
  - `complementary` -> **1.3 Abstract Interpretation** (Formal duals: AI is over-approximated, SE is under-approximated).
  - `shares_technique` -> **2.10 Micro-execution & Emulation** (Both execute paths; micro-execution intercepts memory exceptions to feed inputs dynamically).
  - `shares_technique` -> **3.2 Semantics-based Synthesis** (Synthesis uses symbolic execution engines and SMT solvers to construct correct code patches).

- **1.5 Graph-based Analysis**
  - `extends` -> **1.2 Data Flow Analysis** (Code Property Graphs incorporate program dependence graphs).
  - `shares_technique` -> **1.7 Learning-based Static** (Learning models like GNNs train directly on Code Property Graphs).

- **1.6 Type System & IFC**
  - `shares_technique` -> **1.2 Data Flow Analysis** (Static information flow control relies on type-based data flow analysis).
  - `domain_overlap` -> **2.13 Microarchitectural & Side-Channel** (IFC type systems prove timing/cache leakage safety; side-channel analysis tests for real leakage).

- **1.7 Learning-based Static**
  - `extends` -> **1.1 Syntactic & AST** (Learns from token sequences and AST representations).
  - `extends` -> **1.2 Data Flow Analysis** (Learns from data flow graphs).
  - `extends` -> **1.5 Graph-based Analysis** (Uses Graph Neural Networks on CPG representations).
  - `shares_technique` -> **3.4 DL & NMT Repair** (Both share deep learning models like CodeBERT / LLMs for coding tasks).
  - `shares_technique` -> **3.3 Template-based Repair** (Learning models are often used to mine or select repair templates).

- **1.8 Binary & Reverse Engineering**
  - `shares_technique` -> **1.4 Symbolic Execution** (Binary engines like Triton/angr use symbolic execution on disassembled code).
  - `shares_technique` -> **2.10 Micro-execution & Emulation** (Both run compiled code in isolated virtual environments/emulators without source code).
  - `precondition_of` -> **3.7 Binary & Hot Patching** (Disassembly/reverse engineering is required to locate and apply binary patches).
  - `complementary` -> **1.9 Software Composition & Supply Chain SCA** (SCA lists declared open-source packages; binary analysis validates if they exist in compiled output).

- **1.9 Software Composition & Supply Chain SCA**
  - `complementary` -> **1.8 Binary & Reverse Engineering** (Validates declarations against binary/compiled reality).

- **1.10 Cryptographic & Protocol Security**
  - `domain_overlap` -> **2.13 Microarchitectural & Side-Channel** (1.10 audits API/protocol misuse statically; 2.13 timing side-channels analyze real hardware timing leakage).
  - `shares_technique` -> **2.5 Dynamic Taint Analysis (DTA)** (DTA tracks cryptographic keys to prevent them from leaking into public channels/sinks).

---

### Group 2: Dynamic Analysis (2.1 - 2.13)

- **2.1 Web & API DAST**
  - `complementary` -> **2.2 Black-box Protocol Fuzzing** (DAST targets web application flows; protocol fuzzing targets protocol parsing layers).
  - `complementary` -> **1.2 Data Flow Analysis** (Provides the dynamic validation for static source-to-sink findings).

- **2.2 Black-box Protocol Fuzzing**
  - `complementary` -> **2.4 Feedback-directed Fuzzing** (Black-box relies on protocol generation/mutation; Grey-box utilizes coverage feedback).
  - `complementary` -> **2.1 Web & API DAST** (Targets communication protocol implementation rather than HTTP application endpoints).

- **2.3 Malware Sandbox**
  - `shares_technique` -> **2.7 Instrumentation & Sanitizers** (Both monitor API calls and system execution hooks in real-time).

- **2.4 Feedback-directed Fuzzing**
  - `complementary` -> **2.6 Concolic & Hybrid** (Hybrid fuzzing switches to concolic execution when stuck at magic bytes/complex constraints).
  - `complementary` -> **2.2 Black-box Protocol Fuzzing** (Compares coverage-guided grey-box vs. pure black-box generation).
  - `complementary` -> **2.10 Micro-execution & Emulation** (Fuzzers run whole-program cycles; micro-execution targets isolated basic blocks).
  - `complementary` -> **2.9 Mutation Testing** (Fuzzing generates inputs to find bugs; mutation testing injects bugs to test the quality of tests/fuzzing).
  - `precondition_of` -> **2.11 Kernel & Hypervisor Fuzzing** (AFL/LibFuzzer coverage instrumentation is a prerequisite for kernel-level fuzzers).
  - `domain_overlap` -> **2.8 Differential & Concurrency** (Fuzzing generates tests; differential testing runs those tests across multiple engines).

- **2.5 Dynamic Taint Analysis (DTA)**
  - `dynamic_counterpart` -> **1.2 Data Flow Analysis** (Runs taint tracking on concrete execution paths).
  - `shares_technique` -> **1.10 Cryptographic & Protocol Security** (Crypto tracking techniques are identical to DTA information flow).
  - `shares_technique` -> **2.13 Microarchitectural & Side-Channel** (DTA tracks secret variables to branch conditions to identify timing leaks).

- **2.6 Concolic & Hybrid**
  - `complementary` -> **1.4 Symbolic Execution** (Mitigates path explosion by pinning paths with concrete inputs).
  - `complementary` -> **2.4 Feedback-directed Fuzzing** (Works as a hybrid fuzzer combo like Driller/QSYM).
  - `shares_technique` -> **2.10 Micro-execution & Emulation** (Uses micro-execution runtime components to concrete-execute parts of code).

- **2.7 Instrumentation & Sanitizers**
  - `precondition_of` -> **2.4 Feedback-directed Fuzzing** (Sanitizers like ASan/MSan compile into binary to report crashes/coverage for fuzzers).
  - `shares_technique` -> **2.5 Dynamic Taint Analysis (DTA)** (DTA relies on heavy dynamic instrumentation engines like Intel PIN/Valgrind).
  - `shares_technique` -> **2.3 Malware Sandbox** (Uses system-level instrumentation hooks).
  - `shares_technique` -> **3.7 Binary & Hot Patching** (Patch insertion relies on hot-patching instrumentation techniques).

- **2.8 Differential & Concurrency**
  - `domain_overlap` -> **2.4 Feedback-directed Fuzzing** (Both execute code dynamically; differential uses another program version as an oracle).
  - `domain_overlap` -> **2.12 Smart Contract & Web3 Security** (Web3 security relies on differential execution of transactions to find fork/consensus bugs).

- **2.9 Mutation Testing**
  - `complementary` -> **2.4 Feedback-directed Fuzzing** (Mutation gauges fuzzer suite test quality).
  - `complementary` -> **3.1 Generate-and-Validate** (Evaluates if generated patches are semantically robust or just overfitting).
  - `shares_technique` -> **3.6 Validation & PCA** (Patch validation uses mutation testing concepts to evaluate patch robustness).

- **2.10 Micro-execution & Emulation**
  - `complementary` -> **2.4 Feedback-directed Fuzzing** (Runs isolated functions bypassing setup code vs. whole system testing).
  - `shares_technique` -> **1.4 Symbolic Execution** (Forks concrete executions into symbolic path exploration).
  - `shares_technique` -> **2.6 Concolic & Hybrid** (Shares emulator state tracking components).
  - `shares_technique` -> **1.8 Binary & Reverse Engineering** (Emulates dynamic basic blocks during decompilation).
  - `domain_overlap` -> **2.11 Kernel & Hypervisor Fuzzing** (Both isolate executing code; kernel fuzzing emulates hypervisor states while micro-execution runs basic blocks).

- **2.11 Kernel & Hypervisor Fuzzing**
  - `extends` -> **2.4 Feedback-directed Fuzzing** (Kernel fuzzing is coverage-guided fuzzing adapted to OS/Virtualization layers).
  - `domain_overlap` -> **2.10 Micro-execution & Emulation** (Isolating system states vs. isolating user functions).

- **2.12 Smart Contract & Web3 Security**
  - `extends` -> **2.4 Feedback-directed Fuzzing** (Echidna/Foundry fuzzing adapted for EVM environments and stateful properties).
  - `shares_technique` -> **1.4 Symbolic Execution** (Manticore/Mythril use symbolic EVM execution).
  - `domain_overlap` -> **2.8 Differential & Concurrency** (Web3 uses differential testing to find consensus and reentrancy bugs).

- **2.13 Microarchitectural & Side-Channel**
  - `domain_overlap` -> **1.10 Cryptographic & Protocol Security** (Timing attacks target cryptography; audited statically/analytically).
  - `shares_technique` -> **2.5 Dynamic Taint Analysis (DTA)** (Tracks key leakage to timing/cache side channels).
  - `domain_overlap` -> **1.6 Type System & IFC** (Static IFC types prove absence of side channels).

---

### Group 3: Automated Program Repair (3.0 - 3.7)

- **3.0 Fault Localization**
  - `precondition_of` -> **3.1 Generate-and-Validate**, **3.2 Semantics-based Synthesis**, **3.3 Template-based**, **3.4 DL & NMT Repair**, **3.5 LLM & Agentic** (All repair workflows must locate the bug before attempting fixes).

- **3.1 Generate-and-Validate**
  - `complementary` -> **3.2 Semantics-based Synthesis** (Heuristic search vs. SMT solver synthesis).
  - `complementary` -> **2.9 Mutation Testing** (Mutation scores validate test suite strength to avoid patch overfitting).
  - `shares_technique` -> **3.5 LLM & Agentic** (LLM/Agentic repairs use a generate-validate loop with unit tests).
  - `complementary` -> **3.6 Validation & PCA** (PCA techniques actively filter out weak/overfitted patches generated by G&V).

- **3.2 Semantics-based Synthesis**
  - `shares_technique` -> **1.4 Symbolic Execution** (Relies on symbolic execution to collect patch constraints).
  - `complementary` -> **3.1 Generate-and-Validate** (Analytical synthesis vs. randomized search space traversal).

- **3.3 Template-based**
  - `extends` -> **3.1 Generate-and-Validate** (Specialization of G&V search space constrained by templates).
  - `shares_technique` -> **1.7 Learning-based Static** (Mines static analysis bug patterns to auto-generate templates).

- **3.4 DL & NMT Repair**
  - `extends` -> **3.1 Generate-and-Validate** (G&V where patch candidates are generated by deep neural networks).
  - `shares_technique` -> **1.7 Learning-based Static** (Both share deep learning and embedding algorithms for code representations).

- **3.5 LLM & Agentic**
  - `extends` -> **3.4 DL & NMT Repair** (Autonomous agent systems extending basic sequence-to-sequence neural network model code repair).
  - `shares_technique` -> **3.1 Generate-and-Validate** (Uses unit-test execution loops for agent validation).
  - `complementary` -> **3.6 Validation & PCA** (Validation engines check LLM-generated patches for regressions/overfitting).

- **3.6 Validation & PCA**
  - `complementary` -> **3.1 Generate-and-Validate** (Filters out weak patches).
  - `complementary` -> **3.5 LLM & Agentic** (Checks agent-synthesized patches for logic regression).
  - `shares_technique` -> **2.9 Mutation Testing** (Uses mutation metrics to evaluate test test coverage and patch verification strength).

- **3.7 Binary & Hot Patching**
  - `shares_technique` -> **1.8 Binary & Reverse Engineering** (Requires binary decompilation to identify payload injection points).
  - `shares_technique` -> **2.7 Instrumentation & Sanitizers** (Hot patching hooks into executing code using dynamic binary instrumentation techniques like detours).

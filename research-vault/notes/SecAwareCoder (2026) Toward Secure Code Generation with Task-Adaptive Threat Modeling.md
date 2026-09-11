---
title: "SecAwareCoder: Toward Secure Code Generation with Task-Adaptive Threat Modeling"
year: 2026
venue: "ISSTA 2026"
categories:
  - "[[2B.5-測試預言與斷言合成 (Test Oracle & Assertion Synthesis)]]"
  - "[[0.1-威脅建模與攻擊面分析 (Threat Modeling & Attack Surface Analysis)]]"
  - "[[3C.2-LLM與Agent驅動修復 (LLM & Agentic)]]"
---

# 15 SecAwareCoder: Toward Secure Code Generation via Task-Adaptive Vulnerability Modeling

> **文獻存檔**：*(本篇為重點文獻全文摘錄與分析筆記)*

- **Venue**: ISSTA 2026 (ACM International Symposium on Software Testing and Analysis)
- **Authors**: Jiexin Wang, Xitong Luo, Liuwen Cao, Hongkui He, Hailin Huang, Jiayuan Xie, Adam Jatowt, Yi Cai
- **Institution**: South China University of Technology & University of Innsbruck

---

## Abstract

Large language models (LLMs) have brought significant advancements to code generation and code repair. However, prior research has largely overlooked the security risks inherent in model-generated code. In this work, we introduce SecAwareCoder, an agentic framework designed to shift code generation toward 'secure-by-construction' synthesis.

SecAwareCoder performs task-adaptive threat modeling to identify security-sensitive regions and derive task-grounded vulnerability hypotheses. These hypotheses guide constraint-aware code generation and security-aware test synthesis, leveraging execution feedback for targeted refinement. Furthermore, the authors introduce CodeSecEval, an execution-based benchmark comprising 255 Python tasks across 77 CWE categories.

## Key References & Citations

1. [19] SecurityEval dataset: Mining vulnerability examples for evaluating code generation (Siddiq et al., MSR 2022)
2. [29] CodeSecEval: Is your AI-generated code really safe? (Wang et al., 2024)
3. [33] CyberSecEval: A wide-ranging cybersecurity evaluation suite for Large Language Models (Bhatt et al., Meta 2023)
4. [34] Generating accurate assert statements for unit test cases using pretrained transformers (Tufano et al., AST 2022)

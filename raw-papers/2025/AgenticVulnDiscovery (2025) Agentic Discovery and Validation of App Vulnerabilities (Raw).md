---
title: "Agentic Discovery and Validation of Android App Vulnerabilities"
author: "Ziyue Wang; Liyi Zhou"
creator: "arXiv GenPDF (tex2pdf:)"
pages: 18
---

# Agentic Discovery and Validation of Android App Vulnerabilities

> **作者**：Ziyue Wang; Liyi Zhou
> **總頁數**：18 頁

---

## Page 1

Agentic Discovery and Validation of Android App Vulnerabilities

| Ziyue Wang | Liyi Zhou |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nanjing University | The University of Sydney, Decentralized Intelligence AG, UC Berkeley RDI |  |  |  |  |  |
| Abstract | year over year [2]. The scale of Android applications, together |  |  |  |  |  |
| Existing Android vulnerability detection tools overwhelm | with their privileged access to device resources and user data, |  |  |  |  |  |
| teams with thousands of low-signal warnings yet uncover | complicate comprehensive security assessment. |  |  |  |  |  |
| few true positives. Analysts spend days triaging these results, | Prior work on APK vulnerability detection has largely re- |  |  |  |  |  |
| creating a bottleneck in the security pipeline. Meanwhile, gen- | lied on Static Application Security Testing (SAST) tools [3], |  |  |  |  |  |
| uinely exploitable vulnerabilities often slip through, leaving | such as FlowDroid [4], MobSF [5], and APKHunt [6]. While |  |  |  |  |  |
| opportunities open to malicious counterparts. | useful for surfacing known patterns, these tools leave material |  |  |  |  |  |
| We introduce A2, a system that mirrors how security ex- | gaps in end-to-end security validation (cf. Figure 1). |  |  |  |  |  |
| perts analyze and validate Android vulnerabilities through | • | C1. Low Coverage | : SAST tools match predefined patterns |  |  |  |
| two complementary phases: | (i) Agentic Vulnerability Discov- | and data-flow rules. However, many Android vulnerabilities |  |  |  |  |
| ery | , which reasons about application security by combining | are context and execution dependent, and thus may evade |  |  |  |  |
| semantic understanding with traditional security tools; and | static, rule-based detection systems. |  |  |  |  |  |
| (ii) Agentic Vulnerability Validation | , which systematically | • | C2. | High Volume of Warnings | : | SAST scans entire |
| validates vulnerabilities across Android’s multi-modal attack | APKs, including dependencies, third-party libraries, and |  |  |  |  |  |
| surface—UI interactions, inter-component communication, | low-severity syntax issues, generating large volumes of low- |  |  |  |  |  |
| file system operations, and cryptographic computations. | signal warnings that overwhelm analysts and obscure issues |  |  |  |  |  |
| On the Ghera benchmark ( | n | = | 60), A2 achieves 78 | . | 3% cov- | in application code, driving costly manual triage [7, 8]. |
| erage, surpassing state-of-the-art analyzers (e.g., APKHunt | • | C3. No Exploit Validation | : SAST flags potential issues |  |  |  |
| 30 | . | 0%). Rather than overwhelming analysts with thousands | without writing PoC code to demonstrate and validate |  |  |  |
| of warnings, A2 distills results into 82 speculative vulnera- | exploitability. Meanwhile, Dynamic Application Security |  |  |  |  |  |
| bility findings, including 47 Ghera cases and 28 additional | Testing (DAST) tools [9] in theory can generate PoCs, but |  |  |  |  |  |
| true positives. Crucially, A2 then generates working Proof-of- | they struggle with Android’s structured, multimodal in- |  |  |  |  |  |
| Concepts (PoCs) for 51 of these speculative findings, trans- | put space (UI events, Intents | 1 | , filesystem, databases, shell), |  |  |  |
| forming them into validated vulnerability findings that pro- | yielding a combinatorial search space that is challenging |  |  |  |  |  |
| vide direct, self-confirming evidence of exploitability. | for fuzzers to explore effectively [10]. |  |  |  |  |  |
| In real-world evaluation on 169 production APKs, A2 | Recent progress in Large Language Models (LLMs) marks |  |  |  |  |  |
| arXiv:2508.21579v1 [cs.CR] 29 Aug 2025 | uncovers 104 true-positive zero-day vulnerabilities. Among | a fundamental shift in Android security analysis, overcom- |  |  |  |  |
| these, 57 (54 | . | 8%) are self-validated with automatically gen- | ing long-standing limitations of traditional techniques. We |  |  |  |
| erated PoCs, including a medium-severity vulnerability in a | present A2, a framework that mirrors the reasoning process of |  |  |  |  |  |
| widely used application with over 10 million installs. | human analysts. At its core, A2 operates through two comple- |  |  |  |  |  |

mentary phases: Agentic Vulnerability Discovery and Agentic

1 Introduction Vulnerability Validation . The discovery phase reasons about

application security, combining semantic code understanding

Mobile applications are the primary interface to many digi- with traditional security tools to form actionable vulnerability

tal services. The Google Play Store hosts approximately 2 . 8 hypotheses. Building on these insights, the assessment phase

million Android applications [1]. These applications process

1 In Android, an Intent is a message object that allows app components to

sensitive user and enterprise data and implement business-

request actions from each other. For example, an app can issue an implicit

critical workflows, making them attractive targets for adver- intent such as ACTION_VIEW with a URL to ask the system to open the link

saries. Reported mobile security incidents increased by 32% in a browser. While convenient, intents can also introduce security risks.

1

---

## Page 2

systematically validates each hypothesis through coordinated

that not only identifies vulnerabilities but demonstrates their

in vulnerability assessment. It performs Agentic Vulner-

ability Discovery by combining semantic reasoning with

traditional signals, and Agentic Vulnerability Validation by

planning, executing, and verifying exploits. This human-

like approach enables adaptive discovery beyond static rules

while ensuring rigorous validation with concrete evidence.

• New State-of-the-Art (SOTA) on Ghera Benchmark : On

60 vulnerable APKs, we evaluate A2 alongside four rea-

soning LLMs and three SAST baselines. Among single

models, o3 attains 71.7% (43/60). The ensemble of Gemini

2.5 Flash, Gemini 2.5 Pro, and o3 reaches 78.3% (47/60)

and covers all 27 vulnerabilities detected by the SAST tools.

A2 aggregates 8 , 528 outputs into 82 speculative vulnera-

bility findings while retaining all true positives. This shows

that combining reasoning models with aggregation yields

both higher coverage and significantly fewer speculative

findings than existing approaches.

• LLM-based Vulnerability Validation : We evaluate A2 by

generating PoC exploits for 82 findings A2 reports on the

Ghera benchmark. Within 20 iterations, using Gemini 2.5

2

| Previous SOTA: | A2 |  |  |
| --- | --- | --- | --- |
| APKHunt | on | Speculating vulnerabilities, | Vulnerabilities |
| APK | 5 |  |  |
| High # of Warnings | Few Alerts |  |  |

Multi-modal

Static validation on C3:

Figure 1: Android vulnerability assessment faces three key

challenges: limited coverage, excessive warnings, and lack

of validation. A2 tackles these by mimicking expert analysis

through Agentic Vulnerability Discovery and Agentic Vulner-

ability Validation in four steps: (1) APK input, (2, optional)

integration of static tool signals, (3) speculation on candidate

vulnerabilities with multi-modal validation, and (4) genera-

tion of final reports. Compared to prior SOTA (APKHunt), A2

increases coverage (30% → 71 . 7%, Table 6 in the Appendix),

while reducing from 1.4K warnings to 116 vulnerability find-

ings, and enabling exploit validation (0% → 68 . 0%, Table 7

in the Appendix). Beyond the Ghera benchmark, applying A2

to real-world apps revealed 104 previously unknown zero-day

vulnerabilities (Section 6).

2 Background

| agents that plan, execute, and verify exploitation attempts. | 104 Zero-Day |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Conceptually, A2 mirrors how security experts work: first | Ghera Benchmark | Reflecting on results | Discovered | 😱 |  |
| understanding the application’s security posture comprehen- | 3 |  |  |  |  |
| sively, then methodically proving or disproving each potential | C1: | 1 | Reports | C1: |  |
| vulnerability through hands-on testing. The result is a system | Low Coverage | Higher Coverage |  |  |  |
| real-world impact through concrete, verifiable attack paths. | C2: | C2: |  |  |  |
| Our primary contributions are: | 2 | 4 |  |  |  |
| • | Human-Level End-to-end Security Analysis | : To our | C3: | vulnerability |  |
| knowledge, A2 is the first system to mimic expert practices | No | Validation | Tools | device | Validated Exploits |
| Pro as the | PoC Planner | and Gemini 2.5 Flash as the | Task | This section provides background on Android security. |  |
| Executor | and | Validator | , A2 achieves a 61.3% success rate | Android Component Architecture | Android applications |
| (46/75) on actionable vulnerabilities and correctly rules | utilize a component-based architecture with four building |  |  |  |  |
| out all false positives (7/7). The | Executor | averages 4 | . | 49 | blocks: Activities (UI screens), Services (background tasks), |
| function calls per task, while the | Validator | filters 12.6% of | Broadcast Receivers (system events), and Content Providers |  |  |
| erroneous claims through dynamically generated oracles, | (data access) [12]. These components communicate through |  |  |  |  |
| mitigating hallucination-induced false positives. When both | Intents, which can be either explicit (targeting specific com- |  |  |  |  |
| the | Executor | and | Validator | are upgraded to Gemini 2.5 Pro, | ponents) or implicit (system-resolved based on declared ca- |
| the success rate increases to 68.0% (+6.7%), and erroneous | pabilities). The Android manifest file serves as the central |  |  |  |  |
| claims drop to 4.7% (-7.9%). Overall, these results demon- | configuration document, declaring all components along with |  |  |  |  |
| strate a shift from simple detection toward end-to-end vali- | their required permissions and export policies, effectively |  |  |  |  |
| dation of vulnerabilities through executable evidence. | defining the application’s security boundaries. This modu- |  |  |  |  |
| • | Zero Days | : We deploy A2 on 169 AndroZoo [11] APKs | lar design enables component reuse across applications, but |  |  |
| released in 2024–2025, to assess A2’s effectiveness in prac- | simultaneously introduces security risks. Improperly config- |  |  |  |  |
| tice. The vulnerability detection module reports 136 vul- | ured exported components can be accessed by malicious ap- |  |  |  |  |
| nerabilities, from which the agentic vulnerability validation | plications, while malformed intents can lead to attacks such |  |  |  |  |
| module invalidates 29 false positives. Among the remaining | as intent spoofing and privilege escalation [13]. |  |  |  |  |
| 107 speculative vulnerability findings (104 true positives), | Android Application Vulnerability Landscape | The An- |  |  |  |
| A2 achieves a 54.8% success rate (57/104) in end-to-end | droid ecosystem faces a diverse landscape of security vulner- |  |  |  |  |
| exploitation using Gemini 2.5 Pro as the | PoC Planner | and | abilities that compromise user privacy and system integrity. |  |  |
| Gemini 2.5 Flash as both | Task Executor | and | Task Validator | . | A comprehensive empirical study by VulsTotal [14] system- |
| We responsibly disclosed these zero-days, including cases | atically categorizes Android application vulnerabilities into |  |  |  |  |
| in apps with over 10 million downloads. | 58 distinct types across six major categories: cryptographic |  |  |  |  |

---

## Page 3

weaknesses, inter-component communication flaws, network- TABLE 1: Examples of tools that both A2 and adversaries may use.

ing vulnerabilities, permission misconfigurations, storage is-

Capability Category Example Supporting Tools

sues, and web-related problems. This taxonomy reveals the

complexity of Android security, where vulnerabilities often Code Analysis Jadx [25]

Manifest Inspection Androidguard [26]

arise from the interaction between multiple system compo-

Static Vulnerability Scanning MobSF [5], APKHunt [6]

| nents rather than isolated code defects. Traditional detection | Dynamic Runtime Control | Android Emulator [27] |
| --- | --- | --- |
| approaches focus primarily on well-known vulnerability pat- | Large Language Models | OpenAI, Google Gemini, etc. |

terns, but complex security flaws require deep semantic under-

standing of application logic and cross-component data flows

that challenge conventional automated analysis techniques. 3 Models

Static Application Security Testing Tools SAST tools [3]

| are designed to statically analyze source code or compiled | This section defines the models and analysis scope. |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| versions of code to identify security flaws. According to | System Model | We model the Android ecosystem through |  |  |  |  |
| OWASP [15], static code analysis is performed as part of | three actors: | (i) | developers, | (ii) | distribution channels, and | (iii) |
| white-box testing during the implementation phase, using | end-user devices. Developers build applications that may con- |  |  |  |  |  |
| techniques such as taint analysis and data flow analysis to | tain vulnerabilities due to coding mistakes, misuse of APIs, |  |  |  |  |  |
| highlight possible vulnerabilities within non-running source | or insecure third-party libraries. Applications are packaged |  |  |  |  |  |
| code. These tools form the backbone of modern Android | as signed APKs, with identity tied to the signing key across |  |  |  |  |  |
| application vulnerability detection, providing automated anal- | updates. Source code is often closed, limiting visibility into |  |  |  |  |  |
| ysis capabilities across diverse application codebases. Popu- | developer practices. APKs are distributed through Google |  |  |  |  |  |
| lar Android SAST tools include both shallow analysis tools | Play, third-party markets, and sideloading. For this study, we |  |  |  |  |  |
| such as MobSF [5], APKHunt [6], QARK [16], and An- | use AndroZoo [11], a growing dataset aggregating APKs from |  |  |  |  |  |
| droBugs [17], and deep taint analysis tools such as Flow- | major markets, offering a representative sample of real-world |  |  |  |  |  |
| Droid [4], Amandroid [18], and DroidSafe [19]. | apps. On devices, we assume each app executes in a sandbox |  |  |  |  |  |
| LLM-Powered Agents in Security | LLMs have shown | defined by UID and SELinux, with permissions mediating |  |  |  |  |
| strong code comprehension and analysis skills, leading to their | access to system resources and co-resident apps. Apps in- |  |  |  |  |  |
| growing use in software security [20]. Moving beyond rule- | teract with local components, embedded web content, and |  |  |  |  |  |
| based tools, LLM-powered agents leverage contextual rea- | remote backend services, which define the trust boundaries |  |  |  |  |  |
| soning to perform multi-step security analysis with minimal | in our model: per-app sandboxing, inter-app communication, |  |  |  |  |  |
| supervision. Unlike static analysis tools that depend on fixed | web content, and network channels. We also assume stock, |  |  |  |  |  |
| vulnerability patterns, they adapt to new vulnerability types | non-rooted Android devices with the platform security model |  |  |  |  |  |
| by understanding semantic code relationships. Advances in | enforced, and exclude physical access and custom ROMs. |  |  |  |  |  |
| prompt engineering, tool integration, and multi-agent systems | Threat Model | We consider adversaries who attempt to ex- |  |  |  |  |
| have enabled tasks such as vulnerability classification, exploit | ploit Android applications to steal sensitive data, escalate |  |  |  |  |  |
| generation, and automated penetration testing [21, 22]. Yet, | privileges across application boundaries, or tamper with appli- |  |  |  |  |  |
| LLM agents face limits in context windows, hallucination | cation logic and communication channels. Such adversaries |  |  |  |  |  |
| risks, and variable quality. Research addresses these through | may start with only the APK, without access to source code or |  |  |  |  |  |
| verification mechanisms and hybrid designs that combine | developer keys, but can analyze the package, execute it on a |  |  |  |  |  |
| LLM reasoning with traditional analysis [23]. | device or emulator, and craft exploit sequences that cross trust |  |  |  |  |  |
| Multi-Agent Orchestration | LangGraph [24] is a frame- | boundaries. We assume adversaries are capable of reverse |  |  |  |  |
| work for organizing multi-agent workflows using graph struc- | engineering APKs, observing runtime behavior, and injecting |  |  |  |  |  |
| tures. It represents agents as nodes and their interactions as | crafted inputs through Android’s interaction channels, includ- |  |  |  |  |  |
| edges, allowing developers to define how information and | ing Intents, UI events, filesystem operations, and network |  |  |  |  |  |
| control flow between components. In practice, LangGraph | traffic. They do not control the Android platform, kernel, or |  |  |  |  |  |
| acts as a programmable state machine: it coordinates mes- | hardware. Attacks requiring rooted devices, custom firmware, |  |  |  |  |  |
| sage passing, supports looping and branching, and manages | or hardware side channels are out of scope. Adversaries in- |  |  |  |  |  |
| task execution order. While it is often presented as a new | stead focus on application-layer vulnerabilities introduced by |  |  |  |  |  |
| paradigm, its foundations align with long-standing concepts | developers or insecure library use. Functional bugs [28–30] |  |  |  |  |  |
| of workflow orchestration and state transition systems. Its | that do not compromise security properties are considered out |  |  |  |  |  |
| main contribution is providing a convenient abstraction layer | of scope. To support these capabilities, adversaries may rely |  |  |  |  |  |
| that makes it easier to connect LLMs with external tools, to | on existing tools (cf. Table 1), such as decompilers, manifest |  |  |  |  |  |
| structure multi-step reasoning pipelines, and to implement | inspection utilities, static analysis suites, and emulators, which |  |  |  |  |  |
| such systems in practice. In this work, A2 adopts LangGraph | also form the basis for our AI agent (A2) when reasoning |  |  |  |  |  |
| as it reduces our development overhead. | about attack strategies. |  |  |  |  |  |

3

---

## Page 4

(1) User- de fi ned fi les

| Source code | ① | APK | (2) Android manifest | ② | LLM- | based | Speculative |
| --- | --- | --- | --- | --- | --- | --- | --- |
| resource | vulnerability | vuln. | fi | ndings |  |  |  |
| extractor | analyzers | across LLMs |  |  |  |  |  |
| Execute optionally | Raw warnings | ④ | Security | Standardized warnings |  |  |  |

③ Existing tools

Exceed task retry | Replan

(1) Task execution effects

(2) [optional] FP evidence

All validated Con fi rm TP

⑧ Task

validator

fi ndings

Validate task failed | Retry

Function calling

Emulator Screenshot

paper, we distinguish between three related terms:

are not supported by a PoC implementation. They require

2. Speculative Vulnerability Finding. A candidate vulner-

4 A2 Design

APK as input, A2 performs code analysis to generate specula-

and execution, A2 then transforms speculative vulnerability

4

⑤ Vulnerability

warning aggregator

formatter

(1) Failure reason (2) Replan hints All speculative

vuln. fi ndings

Analyze each vuln.

(1) Generated task list

(2) Expected outcome

⑦ Task

Execute tasks sequentially

Function calling Function calling

Code executor Terminal Other toolkits...

tection. It generates standardized reports with exact line-level

mappings in code, enabling the discovery of previously un-

seen vulnerabilities and context-dependent flaws that require

vulnerability Validate task pass | Next executor ⑥ PoC planner

Figure 2: The end-to-end workflow of A2, from APK input to validated vulnerability findings with proof-of-concept output. A2

operates in two phases: Agentic Vulnerability Discovery ( ➀ - ➄ , blue blocks ) and Agentic Vulnerability Validation ( ➅ – ➇ ,

brown blocks ). In the vulnerability discovery phase, the target APK is decompiled and its resources extracted ( ➀ ). LLM agents

then analyze the application ( ➁ ), producing speculative vulnerability findings. Optionally, warnings from existing SAST tools

( ➂ ) are passed through the formatter ( ➃ ), which standardizes them and produces additional speculative vulnerability findings

to enhance coverage and confidence. All speculative findings are then consolidated by the aggregator ( ➄ ). In the vulnerability

validation phase, each speculative vulnerability finding is passed to the PoC planner ( ➅ ), which generates task lists with expected

outcomes. The task executor ( ➆ ) sequentially carries out these tasks through function calls (e.g., emulator, screenshot analysis,

code execution, terminal commands, and etc.) Finally, the task validator ( ➇ ) independently verifies outcomes using multiple

oracles, providing feedback for iterative refinement until either successful validation or retry limits are reached.

| Terminology | To ensure precise language throughout this | 4.1 | Agentic Vulnerability Discovery |  |  |
| --- | --- | --- | --- | --- | --- |
| 1. | Warning. | A potential issue reported by static analysis or | A2 discovers vulnerabilities primarily through LLMs, with |  |  |
| rule-based tools. Warnings may include false positives and | optional support from static tools and vulnerability databases. |  |  |  |  |
| manual inspection to determine their relevance. | 4.1.1 | LLM-based Vulnerability Analyzer |  |  |  |
| ability generated by A2. Unlike warnings, these findings | Our analyzer consists of three components (cf. Figure 2): |  |  |  |  |
| include a reasoned hypothesis about why the issue may be | ➀ | APK Resource Extractor | (i) | employs Jadx [25] to de- |  |
| exploitable, but they remain unconfirmed until validation. | compile bytecode into source code, then | (ii) | excludes third- |  |  |
| 3. | Validated Vulnerability Finding. | A vulnerability for | party libraries and Android framework code, and | (iii) | extracts |
| which at least one working PoC has been produced, and | manifest details (e.g., component declarations, permission |  |  |  |  |
| an LLM assessment indicates that the PoC demonstrates | specifications, and inter-component communication policies.) |  |  |  |  |
| the vulnerability. While this stage goes beyond hypothesis, | ➁ | LLM Vulnerability Analyzer | processes the code and |  |  |
| such findings may still include false positives if the PoC | manifest data using LLMs to identify security flaws and vul- |  |  |  |  |
| or validation is misleading or incomplete. | nerability patterns that may evade traditional rule-based de- |  |  |  |  |
| Figure 2 illustrates the end-to-end workflow of A2. Given an | understanding of application logic and data flow. |  |  |  |  |
| tive vulnerability findings. Through iterative PoC refinement | 4.1.2 | (Optional) Third-party Tool Integration |  |  |  |
| findings into validated vulnerability findings. | A2 can integrate third-party tools that accept an APK as input. |  |  |  |  |

---

## Page 5

➂ Existing Static Tools such as MobSF [5] and AP- TABLE 2: Available function calls for Agentic Vulnerability Validation. We

➃ Security Warning Formatter standardizes the diverse

rity warnings for downstream processing.

4.1.3 Vulnerability Aggregation

and task routing (Table 2). At its core, A2 runs a feedback

loop: the PoC Planner breaks down a strategy into verifiable

2 We use “read-only” to refer to function calls that do not alter the runtime

state of the target application inside the Android emulator. However, they

5

provide 29 specialized functions grouped into eight categories: (i) code

log analysis (logcat filtering), (vii) APK generation for custom test payloads,

role-based access control (agents restricted to curated tool subsets), and

isolation/sandboxing (dangerous actions run in safe environments). A

they may still affect the local analysis environment

.

| Tool Function | Description | Planner | Executor | Validator |  |
| --- | --- | --- | --- | --- | --- |
| install_python_package | Install Python packages in VM | ✓ | ✓ |  |  |
| restart_application | Stop and restart application with activity | ✓ |  |  |  |
| pull_device_file | Transfer file from Android device to host | ✓ | ✓ | ✓ |  |
| File | analyze_file_content | Search file content using regex patterns | ✓ | ✓ | ✓ |
| read_local_file | Read file from execution environment | ✓ | ✓ | ✓ |  |
| Code | search_code_patterns | Search keywords and patterns in source code | ✓ | ✓ | ✓ |
| input_text_field | Input text into UI text fields | ✓ |  |  |  |
| verify_element_exists | Check UI element existence on current screen | ✓ | ✓ |  |  |
| find_ui_elements | Find UI elements containing specific text | ✓ | ✓ |  |  |
| capture_ui_layout | Capture XML hierarchy of current UI layout | ✓ | ✓ |  |  |
| initialize_gradle | Initialize project from benign template | ✓ |  |  |  |
| APK | build_android_package | Compile Android project to installable APK | ✓ |  |  |
| Web | start_web_service | Start Flask development server | ✓ |  |  |

recomputation to judge whether the expected effect actually

took place. ➇ Task Validator is the key to A2’s success.

| KHunt [6] offer two advantages over pure LLMs: | (i) | they | execution | (dynamic Python scripts, package management), | (ii) | device |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| provide precise code locations and vulnerability context that | control | (hardware key simulation, ADB shell commands), | (iii) | file | system |  |  |  |  |
| enrich the evidence base, and | (ii) | their deterministic data flow | operations (local and device-side file management for extraction and |  |  |  |  |  |  |
| analysis guides targeted exploitation by revealing concrete | analysis), | (iv) | code | navigation (source inspection), | (v) | UI | interaction, | (vi) |  |
| attack paths. This integration complements the semantic rea- | and | (viii) | web | server management for simulating external services or |  |  |  |  |  |
| soning of LLMs with the precision of static analysis, enabling | adversarial endpoints. The function calls design follows three principles: |  |  |  |  |  |  |  |  |
| broader and more reliable vulnerability discovery. | functional decomposition (clear domains and separation of concerns), |  |  |  |  |  |  |  |  |
| outputs of static analysis tools, which often vary in format | modular structure allows extension as new validation techniques emerge. |  |  |  |  |  |  |  |  |
| and terminology. Leveraging LLMs, it harmonizes formats, | Functions marked as | read-only | – highlighted in blue – do not modify the |  |  |  |  |  |  |
| aligns semantics, and structures reports into consistent secu- | runtime state of the target application inside the Android emulator, though |  |  |  |  |  |  |  |  |
| The discovery process concludes with | ➄ | , the | Vulnerability | Execute | execute_python_script | Execute Python code in VM | ✓ | ✓ |  |
| Aggregator | , an LLM-based component that unifies outputs | press_hardware_key | Press system keys (e.g., back, home, etc.) | ✓ |  |  |  |  |  |
| from | ➁ | and | ➃ | . The aggregator performs three key functions: | Control | launch_application | Start application with optional activity | ✓ | ✓ |
| (i) | Security issue filtering | , removing warnings unrelated to | execute_shell_command | Execute ADB shell commands | ✓ | ✓ |  |  |  |
| exploitable flaws such as code quality or performance issues; | upload_file_to_device | Upload file from host to Android device | ✓ |  |  |  |  |  |  |
| (ii) | Semantic deduplication | , collapsing duplicate findings | check_file_existence | Verify file or directory existence on device | ✓ | ✓ | ✓ |  |  |
| across tools through similarity analysis and contextual reason- | create_local_file | Create file in execution environment | ✓ | ✓ |  |  |  |  |  |
| ing; and | (iii) | Evidence synthesis | , merging complementary | list_directory_contents | List files and directories with metadata | ✓ | ✓ | ✓ |  |
| signals to construct richer vulnerability profiles. Together, | extract_source_code | Extract source code by filename from APK | ✓ | ✓ | ✓ |  |  |  |  |
| these functions yield | speculative vulnerability findings | , each | enumerate_source_files | List important source files filtering libraries | ✓ | ✓ | ✓ |  |  |
| representing a reasoned hypothesis about potential exploitable | click_ui_element | Click UI elements (multi-strategy positioning) | ✓ |  |  |  |  |  |  |
| flaws, ready for validation in Section 4.2. | UI | clear_text_field | Clear content from UI text fields | ✓ |  |  |  |  |  |
| 4.2 | Agentic Vulnerability Validation | Log | search_system_logs | Search Android logcat using regex patterns | ✓ | ✓ |  |  |  |
| The Agentic Vulnerability Validation phase employs a multi- | install_apk | Install APK file to connected Android device | ✓ |  |  |  |  |  |  |
| agent system to confirm speculative findings through PoC | initialize_flask_server | Create Flask server directory structure | ✓ |  |  |  |  |  |  |
| exploits. A2 uses LangGraph [24] for stateful coordination | stop_web_service | Terminate running Flask server process | ✓ |  |  |  |  |  |  |
| tasks, the | Task Executor | carries them out, and the | Task Val- | ➆ | Task Executor | implements the | ➅ | Planner | ’s natural- |
| idator | independently judges the results as success or failure. | language strategy as a concrete PoC for speculative vulner- |  |  |  |  |  |  |  |
| ➅ | PoC Planner | performs strategic planning. For each spec- | ability findings. It sequentially executes the required steps |  |  |  |  |  |  |
| ulative vulnerability finding, it examines the flaw’s character- | using all eight toolkit categories (29 functions in total, cf. Ta- |  |  |  |  |  |  |  |  |
| istics, code context, and attack vectors to propose a step-by- | ble 2), covering code execution, device control, file system, |  |  |  |  |  |  |  |  |
| step validation plan. As Table 2 shows, the | ➅ | Planner | only | static analysis, UI interaction, log analysis, APK generation, |  |  |  |  |  |
| triggers “read-only” | 2 | function calls, such as code navigation, | and web server management. Acting as a multimodal agent, |  |  |  |  |  |  |
| file system analysis, and basic application | control | . This “read- | the | Executor | processes both visual data (screenshots) and |  |  |  |  |
| only” design separates planning from execution and avoids | structural data (XML layouts) to navigate and interact with |  |  |  |  |  |  |  |  |
| unintended side effects. The | ➅ | Planner | may also attempt | the victim application during PoC execution. |  |  |  |  |  |
| to further filter false positives after analyzing all supporting | ➇ | Task Validator | provides independent verification of each |  |  |  |  |  |  |
| evidence. After a false positive is speculated, the | ➅ | Planner | PoC outcome. It never accepts the | ➆ | Task Executor | ’s self- |  |  |  |
| assigns | determine_potential_fp | tasks to the | ➆ | Task Executor | reported success. Instead, after the | ➆ | Task Executor | runs a |  |
| for concrete validation. | PoC, the | ➇ | Task Validator | uses its own observations and |  |  |  |  |  |
| may still manipulate the local analysis environment, such as creating a python | Similar to | ➅ | , the | ➇ | Task Validator | operates with “read- |  |  |  |
| script, executing code in it, and collecting results. | only” function calls. This gives | ➇ | wide visibility but prevents |  |  |  |  |  |  |

---

## Page 6

| 📋 | Task 1: extract_hardcoded_key | 📋 | Task 2: forge_password_reset_token |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 📝 | Description | : Retrieve the hardcoded secret key from the application's resources, | 📝 | Description | : Using the extracted hardcoded key, encrypt the target email address |  |  |
| speci | fi | cally from | resources/res/values/strings.xml | as indicated by vulnerability | 'anniemaes@gmail.com' with AES (ENCRYPT_MODE) and then Base64 encode the |  |  |
| information. | resulting ciphertext to create a forged password reset token. |  |  |  |  |  |  |
| 🎯 | Expected Outcome | : The plaintext cryptographic key used for AES | 🎯 | Expected Outcome | : A valid Base64 encoded string representing the encrypted target |  |  |
| encryption/decryption is successfully extracted. | email is generated. |  |  |  |  |  |  |
| 📝 | Completed Task | 📝 | Oracles | 📝 | Completed Task | 📝 | Oracles |
| - None | O1: assert( | strings_xml | _exist, True) | - extract_hardcoded_key | O1: assert(forged_token,'Dv0UyBop+hW |  |  |
| 📝 | Current Task | O2: assert(secret_key, | 0123456789!@#$%^ | ) | 📝 | Current Task | lxRJDwremeNMrYZWchgwMpMiVP...') |

- extract_hardcoded_key

| 📝 | Remaining Tasks | 🔧 | Function Calling | - forge_password_reset_token |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| - forge_password_reset_token | - read_local_ | fi | le( | strings.xml | ) | 📝 | Remaining Tasks | 🔧 | Function Calling |  |
| - launch_new_password_activity | {found: True, content: '.....'} | - launch_new_password_activity | - execute_python_script(froge_token) |  |  |  |  |  |  |  |
| 📋 | Oracle Checks | 🔧 | Function Calling | 📋 | Oracle Checks |  |  |  |  |  |
| 🔧 | Function Calling | - O1: Passed | ✅ | - install_python_package( | pycryptodome | ) | - O1: Passed | ✅ |  |  |
| - search_code_patterns(secret_key) | - O2: Passed | ✅ | - execute_python_script( | froge_token | ) | 🚀 | Final Result |  |  |  |
| {attribute_value:0123456789!@#$%^} | 🚀 | Final Result | 🚀 | Execution Summary | The script to forge the password reset token |  |  |  |  |  |
| 🚀 | Execution Summary | The hardcoded secret key | Successfully encrypted the target email | was re- | executed, and the output matches |  |  |  |  |  |
| The hardcoded secret key | 0123456789!@#$%^ | was successfully | address | anniemaes@gmail.com | with the | the Executor's evidence.The token was |  |  |  |  |
| 0123456789!@#$%^ | was successfully | extracted from | strings.xml | , con | fi | rming the | hardcoded key | 0123456789!@#$%^ | using | generated by encrypting |
| extracted from the application's resources | presence of sensitive information within | AES (ECB mode) and Base64 encoded the | anniemaes@gmail.com | with the hardcoded |  |  |  |  |  |  |
| strings.xml | the resources. | result to forge a password reset token. | key using AES (ECB mode). |  |  |  |  |  |  |  |
| Figure 3: Hardcoded key extraction validation workflow. | Figure 4: Cryptographic token forgery validation workflow. |  |  |  |  |  |  |  |  |  |
| A2 searches for cryptographic key patterns within applica- | The | ➆ | Task Executor | uses the extracted AES key to encrypt a |  |  |  |  |  |  |
| tion resources and extracts a hardcoded AES key from the | target email address and generate a Base64-encoded password |  |  |  |  |  |  |  |  |  |
| strings.xml file, with the | ➇ | Task Validator | verifying both file | reset token, while the | ➇ | Task Validator | independently verifies |  |  |  |
| existence and key value through oracle-based validation. | the cryptographic operations. |  |  |  |  |  |  |  |  |  |
| any modification of the application state (which may change | of the current finding, the | ➇ | Validator designs oracles that |  |  |  |  |  |  |  |
| the PoC outcome, and we don’t want that, cf. Table 2). | independently test whether the claimed effect truly manifests. |  |  |  |  |  |  |  |  |  |
| Iterative Self-Correction | When execution fails at | ➆ | or | On a high level, an oracle involves the following steps: |  |  |  |  |  |  |
| validation rejects a success claim at | ➇ | , feedback is sent back | 1. | Parse the claim. | ➇ | takes a single claim from the | ➆ | Execu- |  |  |
| to the | ➅ | PoC Planner | . The planner then inspects the failure, | tor, for example “hardcoded AES key found,” or “admin |  |  |  |  |  |  |
| revises its strategy, and retries. This self-correction loop lets | screen reachable without login.” |  |  |  |  |  |  |  |  |  |
| the system adapt and handle unexpected obstacles. The | ➇ | 2. | State the expected effect. | ➇ | writes the expected testable |  |  |  |  |  |
| Task Validator | guides the process into one of three states: | effect, for example “the key decrypts file correctly,” or “Ad- |  |  |  |  |  |  |  |  |
| (i) Continuation | , when a task is validated and the next task | minActivity opens while the session is unauthenticated.” |  |  |  |  |  |  |  |  |
| begins; | (ii) Re-planning | , when validation fails and the planner | 3. | Design an oracle. | ➇ | chooses one or more checks that can |  |  |  |  |
| must revise its approach; or | (iii) Completion | , when all tasks | confirm or reject the effect. These checks use only “read |  |  |  |  |  |  |  |
| pass validation and the workflow ends. | only” tools from Table 2. |  |  |  |  |  |  |  |  |  |

4. Collect evidence. ➇ run the selected tools to gather code,

UI, logs, files, or network traces.

4.3 Vulnerability Oracle

5. Decide. ➇ compare the evidence with the expected effect.

| We highlight the oracle design as one of the core novelties | The oracle returns PASS or FAIL, plus a short rationale |  |  |  |
| --- | --- | --- | --- | --- |
| of A2, since reliable validation is what ultimately separates | and artifacts for the report. |  |  |  |
| speculative findings from actionable vulnerabilities. | We demonstrate A2’s validation capabilities through a hard- |  |  |  |
| Unlike some security domains where vulnerability ora- | coded cryptographic key vulnerability case from the Ghera |  |  |  |
| cles can be defined with clear heuristics—for example, in | benchmark [32]. |  |  |  |
| blockchain security, monetary gain can serve as a definitive | Vulnerability Scenario | The target application implements |  |  |
| indicator [31]—Android vulnerability validation presents a | a password reset verification interface where users provide |  |  |  |
| much harder challenge. Applications expose diverse behav- | their email address and click "GET TOKEN" to receive a veri- |  |  |  |
| iors, and strict rules that guarantee zero false positives are | fication token. After entering the correct token, users proceed |  |  |  |
| difficult, if not impossible, to design. This limitation has long | to the password reset interface. The application uses the | Ci- |  |  |
| constrained fuzzers and static analysis tools in the Android | pher | API with AES encryption for token generation but stores |  |  |
| ecosystem: they either over-approximate and flag benign be- | the cryptographic key ( | 0123456789!@#$%ˆ | ) directly in the |  |
| haviors or under-approximate and miss subtle flaws. | strings.xml | resource file. This enables attackers to extract |  |  |
| A2 adopts a different strategy. Instead of relying on fixed | the hardcoded key from the APK and forge authentication |  |  |  |
| heuristics, the | ➇ | Task Validator | uses LLMs to generate cus- | tokens for arbitrary users, bypassing security controls. |
| tomized oracles for each vulnerability, case by case. Each | A2 validates this vulnerability through three sequential |  |  |  |
| claim from the | ➆ | Executor | is transformed into targeted verifi- | tasks mirroring a real-world attack scenario. Figures 3, 4, and |
| cation questions. Guided by prior knowledge and the context | 5 demonstrate the validation workflow, while Figure 6 shows |  |  |  |

6

---

## Page 7

📋 Task 3: launch_new_password_activity

📝 Description : Launch the 'edu.ksu.cs.benign.NewPasswordActivity'. Passing the forged

password reset token as an extra named 'token'. This simulates an attacker providing a

valid token to bypass authentication.

🎯 Expected Outcome : The 'NewPasswordActivity' is successfully launched, and its

onResume() method attempts to decrypt the provided token.

| 📝 | Completed Task | 📝 | Oracles |
| --- | --- | --- | --- |
| - extract_hardcoded_key | O1: assert(activity, NewPasswordActivity) |  |  |
| - forge_password_reset_token | O2: exist(email_ui_element) |  |  |

📝 Current Task

- launch_new_password_activity 🔧 Function Calling

📝 Remaining Tasks - fi nd_ui_elements('a...@gmai.com')

- execute_shell_command(

| 🔧 | Function Calling | 'dumpsys activity activities \| |  |  |
| --- | --- | --- | --- | --- |
| input_text_ | fi | eld(loc:'Email',content: ...) | grep mResumedActivity') |  |
| input_text_ | fi | eld(loc:'Token',content: ...) | 📋 | Oracle Checks |
| click_element(loc:'RESET PASSWORD') | - O1: Passed | ✅ |  |  |
| 🚀 | Execution Summary | - O2: Passed | ✅ |  |

Successfully launched with the forged

token, and the email is displayed, token. The email is displayed on the screen.

Figure 5: Authentication bypass validation through forged

token injection. A2 launches the NewPasswordActivity with

the crafted token, demonstrating successful authentication

bypass as verified through UI element analysis and system

activity monitoring.

the UI changes during exploitation.

Task 1: Hardcoded Key Extraction In this initial vali-

dation step, A2 locates and extracts the hardcoded crypto-

graphic key embedded within the application’s resource files.

As shown in Figure 3, the system successfully identifies the

ated token matches the expected cryptographic output and

tionality using the crafted token, successfully deceiving the

application into accepting it as legitimate. Figure 6 shows

how the attack grants unauthorized access to password reset

functionality, thereby confirming the end-to-end exploitability

of the vulnerability.

7

across four UI states: (i) initial password reset interface, (ii)

target email input, (iii) forged token injection, and (iv) suc-

cessful authentication bypass leading to password reset func-

tionality access.

zero-day vulnerabilities in the wild. We compare A2 against

SOTA static analysis tools and discss the quality of A2’s

generated PoCs across multiple dimensions.

5.1 Dataset Selection

other platforms.

We describe below the setup used for all experiments.

Computational Environment. All experiments run on an

Apple M4 system with 24GB RAM and 1TB SSD storage

(macOS 26.0). The Android testing setup uses emulator ver-

droid API level 36. Experiments are conducted with internet

| The NewPasswordActivity was | 🚀 | Final Result | (i) Initial State | (ii) Input the | (iii) Input the | (iv) Bypass |
| --- | --- | --- | --- | --- | --- | --- |
| successfully launched with the forged | victim's email | forged token | authentication |  |  |  |
| indicating successful decryption. | Con | fi | rm the vulnerability | Figure 6: Progressive authentication bypass demonstration |  |  |
| AES key stored in the | strings.xml | configuration file. The | Our experiments are conducted on two datasets. |  |  |  |
| Task Validator | independently verifies both the file’s existence | • The | Ghera | benchmark dataset contains 60 vulnerable An- |  |  |
| and the specific key value through oracle-based validation, | droid APKs spanning eight categories—CRYPTO, ICC, |  |  |  |  |  |
| confirming the presence of this critical security vulnerability. | NETWORKING, NON-API, PERMISSION, STORAGE, |  |  |  |  |  |
| Task 2: Password Reset Token Forgery | Building on the | SYSTEM, and WEB—and serves as our primary testbed |  |  |  |  |
| extracted key, A2 demonstrates the exploitability of this vul- | for both detection and exploit generation evaluation. |  |  |  |  |  |
| nerability by forging authentication tokens for arbitrary users. | • For real-world vulnerability discovery, we use APKs from |  |  |  |  |  |
| Figure 4 illustrates how the system uses the hardcoded key | AndroZoo [11] released between January 2024 and July |  |  |  |  |  |
| to encrypt a target email address ( | anniemaes@gmail.com | ) | 2025. To address model context limits during detection, we |  |  |  |
| with AES encryption, generating a Base64-encoded password | restrict to APKs under 5MB, yielding 169 distinct samples: |  |  |  |  |  |
| reset token. The validation process confirms that the gener- | 126 from play.google.com, 38 from VirusShare, and 5 from |  |  |  |  |  |
| can successfully impersonate legitimate users. | To reduce potential data leakage and model memorization, |  |  |  |  |  |
| Task 3: Authentication Bypass Validation | The final vali- | we remove all textual descriptions or semantic information |  |  |  |  |
| dation step proves that the forged tokens can bypass the ap- | about the vulnerabilities from our dataset. In addition, all |  |  |  |  |  |
| plication’s authentication mechanisms in practice. As demon- | application-specific identifiers, such as filenames and APK |  |  |  |  |  |
| strated in Figure 5, A2 launches the password reset func- | names, are replaced with generic placeholders. |  |  |  |  |  |
| the complete UI progression across four states, documenting | 5.2 | Experimental Setup |  |  |  |  |
| 5 | Evaluation | sion 35.6.11.0, adb 1.0.41 (build 36.0.0-13206524), and An- |  |  |  |  |
| In this section, we conduct experiments to evaluate A2’s | connectivity for LLM API access, with a 300-second timeout |  |  |  |  |  |
| performance, cost effectiveness, and capability to discover | per call to ensure reliable execution. |  |  |  |  |  |

---

## Page 8

TABLE 3: Comparison of static tools evaluated in this study

real-world APKs. APK is the number of applications analyzed. LoC is the

average lines of code per application. Alert is the number of vulnerabilities

Discovery and Agentic Vulnerability Validation. TP and FP are true and

detected (out of 60). Validation consistently reduces false positives (e.g.,

Ghera: 8 → 1, real-world APKs: 32 → 3) while preserving most true positives.

| Ghera | 60 | 46,100 | 82 | Agentic Vulnerability Discovery | 75 | 7 | 47 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Agentic Vulnerability Validation | 51 | 1 | 34 |  |  |  |  |
| Production | 169 | 115,696 | 136 | Agentic Vulnerability Discovery | 104 | 32 | – |

supports compiled Android Package files without requiring

a broad range of Android vulnerabilities: MobSF [5], AP-

5.3 Detection Performance

8

14

| Vulnerability Categories | 12 |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | CRYPTO | PERMISSION |  |  |  |  |  |  |  |
| 10 | NETWORKING | SYSTEM | 9 | 9 | 9 | 9 |  |  |  |
| 8 | NONAPI | WEB |  |  |  |  |  |  |  |
| 6 | 6 | 6 |  |  |  |  |  |  |  |
| 4 | 4 | 4 | 4 |  |  |  |  |  |  |
| 4 | 3 | 3 | 3 |  |  |  |  |  |  |
| 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

Number of Detected Vulnerabilities 0

MobSF APKHunt Trueseeing 2.5-flash 2.5-pro gpt-oss-120b o3

gories. Each bar shows the number of detected vulnerabilities

by category for each tool, with different colors representing

fault analysis pipelines. Ground-truth validation is performed

manually by both authors, with cross-checking to confirm

detection results.

audits harder for analysts.

their coverage is narrow. APKHunt detects four CRYPTO

vulnerabilities that no other SAST tool reports, while True-

seeing is the only tool to flag three NONAPI issues and a

| Tool | Stars | Commits | Version | Language | ICC | STORAGE | 10 |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MobSF [5] | 19k+ | 2,000+ | v4.3.2 | Python | 8 | 8 |  |  |  |  |  |  |  |  |  |
| APKHunt [6] | 800+ | 100+ | v1.0.0 | Go | 7 | 7 |  |  |  |  |  |  |  |  |  |
| Trueseeing [35] | 60+ | 850+ | v2.2.7 | Python | 6 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| TABLE 4: Summary of A2 detection results on the Ghera benchmark and | 2 | 2 | 2 | 2 | 2 | 2 |  |  |  |  |  |  |  |  |  |
| initially reported by A2. | Stage | distinguishes Agentic Vulnerability | Detection Tools |  |  |  |  |  |  |  |  |  |  |  |  |
| false positives. | B_TP | is the number of Ghera ground-truth vulnerabilities | Figure 7: Detection performance across vulnerability cate- |  |  |  |  |  |  |  |  |  |  |  |  |
| Dataset | APK | LoC | Alert | Stage | TP | FP | B_TP | different vulnerability categories. |  |  |  |  |  |  |  |
| Agentic Vulnerability Validation | 57 | 3 | – | picking or repeated attempts. For static tools, we use their de- |  |  |  |  |  |  |  |  |  |  |  |
| Comparison Tool Selection. | We select tools based on three | whether each tool correctly identifies the vulnerabilities docu- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| criteria: | (i) APK compatibility | , meaning the tool natively | mented in Ghera. Table 6 in the Appendix presents the full |  |  |  |  |  |  |  |  |  |  |  |  |
| source code; | (ii) broad vulnerability coverage | , spanning mul- | Note that Ghera labels APKs with specific vulnerabil- |  |  |  |  |  |  |  |  |  |  |  |  |
| tiple categories rather than focusing on a narrow class of | ities but does not guarantee that other flaws are absent. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| flaws; and | (iii) active maintenance and adoption | , ensuring | For example, one APK labeled with | BlockCipher-ECB- |  |  |  |  |  |  |  |  |  |  |  |
| the tool is available and representative of current practice. | InformationExposure | also contains a | Hard-coded Crypto- |  |  |  |  |  |  |  |  |  |  |  |  |
| These three selection criteria favor static tools. Dynamic anal- | graphic Key | . Exhaustively identifying all vulnerabilities is |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ysis is particularly challenging for Android because of its | non-trivial. To reduce subjective bias, we benchmark strictly |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| multimodal input space – UI events, Intents, filesystem ac- | against the vulnerabilities explicitly documented in Ghera. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cess, and database queries – which makes general-purpose | Reported Findings Volume. | We observe a clear gap in the |  |  |  |  |  |  |  |  |  |  |  |  |  |
| DAST difficult to apply [10]. Existing Android DAST tools | number of findings between SAST tools and our LLM-based |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| are usually specialized (e.g., fuzzers for media frameworks | analyzers. MobSF reports 5,654 findings, while o3 produces |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| or native libraries [33, 34]) or UI fuzzers aimed at functional | only 116. The large output of SAST tools comes from broad |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| testing [28–30], rather than security vulnerabilities. In this | rules that flag application issues, third-party libraries, SDK |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| paper, we evaluate three widely used SAST tools that cover | usage, and even coding style. This adds noise and makes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| KHunt [6], and Trueseeing [35]. As of our paper submission, | Detection Capability. | Figure 7 shows the number of vul- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| their features are summarized in Table 3. | nerabilities detected per tool, broken down by category. LLM- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LLM Selection. | To cover a representative range of perfor- | based analyzers achieve substantially higher recall than SAST |  |  |  |  |  |  |  |  |  |  |  |  |  |
| mance and cost, we evaluate four commercial and open-source | tools. o3 detects 43 vulnerabilities (71.7%), while APKHunt |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| multimodal LLMs: OpenAI o3 (o3 2025-04-16), Gemini 2.5 | detects 18 (30.0%) and MobSF only 11 (18.3%), despite |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Pro (gemini-2.5-pro), Gemini 2.5 Flash (gemini-2.5-flash), | MobSF’s much larger output volume. This contrast under- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and GPT oss (gpt-oss-120b). At evaluation time, the adver- | scores the gap between concise LLM results and the noisy |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tised prices per million input and output tokens are 2 and 8 | but shallow coverage of traditional static analysis. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| USD, 1.25 and 10 USD, 0.30 and 2.50 USD, and 0.10 and | LLM analyzers also achieve broader category coverage. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0.50 USD, respectively. To keep reasoning capacity consistent | They consistently detect more vulnerabilities in CRYPTO, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| across models, we set | thinkingBudget | to 24576 for gemini- | ICC, and STORAGE, categories where SAST tools often fail. |  |  |  |  |  |  |  |  |  |  |  |  |
| 2.5-flash and gemini-2.5-pro, and use the | Medium | thinking | In comparison, SAST tools display narrow specialization: |  |  |  |  |  |  |  |  |  |  |  |  |
| intensity for o3 and gpt-oss-120b. | APKHunt and Trueseeing each identify unique cases, but |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| To ensure fairness, each LLM model is executed exactly once | single WEB case. Outside these isolated hits, their contribu- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| per APK. We collect all outputs directly, without cherry- | tion is minimal, highlighting a lack of generalization beyond |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 9

their targeted rules. Variance in performance further high- ) 1e 2

lights this divide. SAST tools diverge widely because their

Analysis shows that LLMs subsume and extend traditional

detection. The three LLMs—gemini 2.5 flash, gemini 2.5 pro,

and o3—collectively capture all 27 vulnerabilities found by

vulnerabilities that no SAST tool detects (marked with ∗ in

Table 6). This demonstrates that LLM-based analysis not only

preserves static-analysis strengths but also extends detection

into previously unreachable ground. Despite these gains, 13

5.4 Aggregation Effectiveness

verification to check whether the aggregated results match the

ground-truth vulnerabilities.

Coverage Analysis. Table 6 in the Appendix shows that

aggregation improves detection coverage. By combining the

outputs from all seven tools, each of the four aggregation

individual tool, o3, at 71.7%. The results highlight the com-

plementary strengths of different detection approaches.

vulnerabilities, gemini-2.5-flash and gemini-2.5-pro consoli-

9

i

/ A

1.0 LLM

G2.5P(Agg)

Ghera i O3(Agg)

0.8 G2.5F(Agg)

G2.5F

G2.5P

0.6 O3

0.4

OSS

0.2

Relative Detection Efficiency (

| 2 | 3 | 4 |
| --- | --- | --- |
| 10 | 10 | 10 |

Reported Security Issues (Log Scale)

Figure 8: Detection efficiency analysis across tool categories.

i / A i

ing SAST approaches.

trade-off, we define a detection efficiency metric that relates

recall to warning volume. Formally, the efficiency of tool i is:

i = (1)

A i

where R Ghera

i is the recall of tool i on the labeled vulnerabili-

abilities are labeled.

i / A i . Intuitively, this

| rules are tied to specific detection oracles, while LLM an- | SAST |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| alyzers maintain a more balanced profile across categories. | R | Aggregate |  |  |  |  |
| the three SAST tools, while also uncovering 20 additional | OSS(Agg) |  |  |  |  |  |
| vulnerabilities remain undetected by any tool, a limitation | APKHunt | MobSF |  |  |  |  |
| discussed in Section 8. | 0.0 | Trueseeing |  |  |  |  |
| The aggregation process collects and normalizes the hetero- | The scatter plot shows reported security issues (x-axis, log |  |  |  |  |  |
| geneous outputs from all seven detection tools (three SAST | scale) versus relative detection efficiency (y-axis, | R | Ghera |  |  |  |
| tools and four LLM-based analyzers) into a unified | Standard- | in scientific notation). Circles represent LLM-based analyz- |  |  |  |  |
| izedVulnerability | format. For each of the 60 vulnerabilities in | ers, squares represent SAST tools, and triangles represent |  |  |  |  |
| the Ghera benchmark, every aggregation model receives the | aggregated results. The “(Agg)” suffix indicates aggregated |  |  |  |  |  |
| complete set of outputs from all tools as input, regardless of | configurations merging multiple tool outputs. Each tool uses |  |  |  |  |  |
| whether individual tools flagged the vulnerability. We evaluate | consistent color coding for individual and aggregated versions. |  |  |  |  |  |
| four LLM models as aggregation engines: gemini-2.5-flash | Higher efficiency values indicate better balance between de- |  |  |  |  |  |
| (G2.5F), gemini-2.5-pro (G2.5P), o3, and gpt-oss-120b (oss). | tection coverage and warning / speculative vulnerability find- |  |  |  |  |  |
| We record the outputs from each model and perform manual | ing volume, with LLM-based tools substantially outperform- |  |  |  |  |  |
| models identifies 47 of the 60 ground-truth vulnerabilities, | R | Ghera | × | total |  |  |
| achieving 78.3% recall. This is a clear gain over the best | E | i | V |  |  |  |
| Consolidation Effectiveness. | While all four aggregation | ties in the Ghera benchmark, | A | i | is the number of warnings / |  |
| models achieve identical top-line recall performance, they | speculative vulnerability findings it reports, and | V | total | repre- |  |  |
| exhibit notable differences in their consolidation strategies. | sents the true (but unknown) total number of vulnerabilities |  |  |  |  |  |
| For example, in analyzing | SQLite-RawQuery-SQLInjection | across the dataset. We only know | V | total | ≥ | 60, since 60 vulner- |
| date findings into 4 distinct issues, whereas o3 reports only | Because | V | total | is constant across all tools, relative com- |  |  |
| 2. Conversely, for | ConstantKey-ForgeryAttack | , o3 provides | parisons depend only on the ratio | R | Ghera |  |
| a more granular report with 2 issues compared to 1 from the | ratio reflects the expected number of true findings per warning, |  |  |  |  |  |
| other models. Notably, gpt-oss-120b demonstrates suboptimal | scaled by recall. We use this proxy because it emphasizes the |  |  |  |  |  |
| consolidation performance, suggesting a higher tendency to- | trade-off practitioners face: higher recall increases the chance |  |  |  |  |  |
| ward hallucination and less effective noise filtering compared | of covering real vulnerabilities, while excessive warnings in- |  |  |  |  |  |
| to other models. Overall, gemini-2.5-flash, gemini-2.5-pro, | crease audit cost. Although other formulations (e.g., precision |  |  |  |  |  |
| and o3 demonstrate strong performance in producing concise, | or F1-score) are possible, this measure directly captures the |  |  |  |  |  |
| actionable final reports. | efficiency of converting warnings into actionable detections. |  |  |  |  |  |
| Detection Efficiency Analysis. | Security practitioners must | Figure 8 compares efficiency scores across tools. Three |  |  |  |  |
| balance detection coverage against analysis overhead. Tradi- | trends stand out. | LLM advantage: | LLM analyzers deliver |  |  |  |
| tional tools often produce thousands of noisy findings, com- | higher recall (66.7–71.7%) while producing far fewer warn- |  |  |  |  |  |
| plicating assessment and inflating audit costs. To capture this | ings (89–193) than SAST tools (978–5,654). | Aggregation |  |  |  |  |

---

## Page 10

| Mixed Configuration | Task Executor Performance. | Function calling success |
| --- | --- | --- |
| 0.3 | Unified Configuration | rates reach 92.5% (927/1002) for mixed configuration and |

0.1

Function Calls Per Task

Figure 9: Kernel density estimation of function calls per task

distribution across both model configurations, showing den-

sity peaks around 2–4 function calls per task.

duced by gemini-2.5-pro in the aggregation stage. For

to refer to these two setups respectively in subsequent sec-

tions. Validation outcomes are categorized with standardized

symbols: ★ = true positive validated with a complete proof-

10

95.4% (649/680) for unified configuration, with the majority

environment-specific challenges including Gradle build sys-

ure 9 shows the function calls per task distribution.

The function calls per task distribution indicates that 80%

of tasks complete within 2-4 function calls, with unified con-

figuration demonstrating reduced function call requirements

(average 2.92 vs 4.49 calls per task). This represents a +35%

reduction in API overhead.

positive claims in unified configuration, corresponding to hal-

lucination rates of 12.6% and 4.7%. These results quantify

validation pipeline.

5.6 Cost and Efficiency Analysis

| 0.2 | of failures concentrated in APK generation and web server |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Density | management functions. These failures primarily result from |  |  |  |  |  |  |  |  |  |  |
| 0.0 | tem configuration conflicts, network port allocation issues, |  |  |  |  |  |  |  |  |  |  |
| 5 | 10 | 15 | and Android emulator state management complexities. Fig- |  |  |  |  |  |  |  |  |
| effectiveness: | Combining outputs achieves the highest ef- | Validator Performance. | The | Task Validator | processes 223 |  |  |  |  |  |  |
| ficiency, reaching 78.3% recall with only 82–157 specula- | task execution claims from the | Task Executor | in mixed con- |  |  |  |  |  |  |  |  |
| tive vulnerability findings, highlighting the complementary | figuration and 233 claims in unified configuration, achieving |  |  |  |  |  |  |  |  |  |  |
| strengths of different methods. | SAST limitations: | Static tools | validation pass rates of 87.4% (195/223) and 95.3% (222/233) |  |  |  |  |  |  |  |  |
| remain inefficient. MobSF, for example, generates over 5,000 | respectively. The validator identifies and filters 28 false pos- |  |  |  |  |  |  |  |  |  |  |
| warnings yet achieves only 18.3% recall. | itive execution claims in mixed configuration and 11 false |  |  |  |  |  |  |  |  |  |  |
| 5.5 | Validation Effectiveness | the validator’s role in maintaining execution reliability and |  |  |  |  |  |  |  |  |  |
| We validate the 82 speculative vulnerability findings pro- | preventing the propagation of erroneous claims through the |  |  |  |  |  |  |  |  |  |  |
| clarity, we | exclude | two | groups | of findings | from | eval- | The | validator’s | hint generation | mechanism | operates |
| uation: | (i) | two findings from APKs that could not be | through dynamic oracle construction, providing specific fail- |  |  |  |  |  |  |  |  |
| installed on the emulator ( | WebViewAllowContentAccess- | ure context when validation fails. Analysis of retry sequences |  |  |  |  |  |  |  |  |  |
| UnauthorizedFileAccess | and | WebViewLoadDataWithBaseUrl- | shows that 78% of initially failed tasks achieve successful val- |  |  |  |  |  |  |  |  |
| UnauthorizedFileAccess | ); and | (ii) | seventeen findings corre- | idation after incorporating validator feedback, demonstrating |  |  |  |  |  |  |  |
| sponding to vulnerabilities outside A2’s current validation | the iterative refinement capability of the multi-agent system. |  |  |  |  |  |  |  |  |  |  |
| scope (see Section 8). | Overall Validation Results. | Among the 82 speculative vul- |  |  |  |  |  |  |  |  |  |
| The remaining 63 (82-2-17) speculative vulnerability find- | nerability findings from aggregation, our analysis identifies |  |  |  |  |  |  |  |  |  |  |
| ings, listed in Table 7 in the Appendix, undergo manual review | 56 true positives, 7 false positives, 17 out-of-scope cases, and |  |  |  |  |  |  |  |  |  |  |
| and classification. This process identifies 56 true positives and | 2 unable-to-install instances. Mixed configuration achieves |  |  |  |  |  |  |  |  |  |  |
| 7 false positives (marked in yellow in the table). To ensure | validation of 46 out of 75 actionable cases (61.3%), while |  |  |  |  |  |  |  |  |  |  |
| accuracy, verification is cross-checked by multiple security | unified configuration reaches 51 out of 75 cases (68.0%), |  |  |  |  |  |  |  |  |  |  |
| researchers. We then evaluate these 63 findings under two | representing a +6.7 percentage point improvement. For end- |  |  |  |  |  |  |  |  |  |  |
| model configurations for the three-agent system. The first | to-end effectiveness based on the 60 labeled vulnerabilities |  |  |  |  |  |  |  |  |  |  |
| configuration uses (gemini-2.5-pro, gemini-2.5-flash, gemini- | in Ghera, those marked with asterisks (*) in Table 7 in the |  |  |  |  |  |  |  |  |  |  |
| 2.5-flash) for the (planner, executor, validator) roles, repre- | Appendix correspond to ground truth labels. Mixed config- |  |  |  |  |  |  |  |  |  |  |
| senting a cost-optimized setup. The second configuration uses | uration validates 31 labeled vulnerabilities (51.7%), while |  |  |  |  |  |  |  |  |  |  |
| (gemini-2.5-pro, gemini-2.5-pro, gemini-2.5-pro) across all | unified configuration achieves 34 (56.7%). This +5.0 percent- |  |  |  |  |  |  |  |  |  |  |
| roles, representing a performance-optimized setup with con- | age point improvement demonstrates the impact of consistent |  |  |  |  |  |  |  |  |  |  |
| sistent model strength throughout the pipeline. For simplicity, | model capability across validation agents, confirming the im- |  |  |  |  |  |  |  |  |  |  |
| we use | Mixed Configuration | and | Unified Configuration | portance of model selection in autonomous security analysis. |  |  |  |  |  |  |  |
| of-concept; | ✫ | = false positive correctly identified and filtered; | To evaluate the practical deployment feasibility of A2, we |  |  |  |  |  |  |  |  |
| ⊗ | = true positive misclassified as false positive; | ⊙ | = false pos- | analyze computational costs and efficiency across different |  |  |  |  |  |  |  |
| itive misclassified as true positive; | × | = execution terminated | system configurations and operational phases. |  |  |  |  |  |  |  |  |
| due to technical errors; | • | = validation stopped after reaching | Token Consumption Analysis. | Token consumption ex- |  |  |  |  |  |  |  |
| the maximum iteration limit. | hibits distinct scaling patterns across operational phases. Dur- |  |  |  |  |  |  |  |  |  |  |

---

## Page 11

10 7 10 7 10 7 10 7

Prompt Token Prompt Token

27031  42982

31811 27031 23684 23635

8192  18496

| 3007 | 1820 |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Tokens (log scale) | 697 | 697 | 718 | 664 | 10 |
| 615 | Tokens (log scale) | 463 |  |  |  |

gemini-2.5-flash, (d) All components using gemini-2.5-pro.

consume 1,322-1,552 prompt tokens and 778-3,523 comple-

tion tokens per APK. The aggregation phase (Figure 10b)

requires 19,074-24,477 prompt tokens and 986-36,624 com-

pletion tokens, representing a 15-20x increase due to process-

ing outputs from seven detection tools. In the multi-agent

validation pipeline, the Executor component dominates con-

figuration, Figure 10c) and 350,667 (unified configuration,

Figure 10d), while Planner and Validator components require

substantially fewer resources. This distribution indicates that

70-80% of computational costs concentrate in the exploitation

generation phase, suggesting optimization opportunities.

ranges $4.81-26.85 per vulnerability (median $8.94). Despite

higher per-token costs, unified configuration achieves 82%

reduction in Executor token usage, though this translates to

only marginal cost savings due to gemini-2.5-pro’s higher

pricing structure.

11

Completion Token 1486945 Completion Token

125619 205298

36345

10 4 7398 7724 7159 10 4 15410

4523

| Tokens (log scale) | 1011 | 1307 | 1116 |
| --- | --- | --- | --- |
| Tokens (log scale) | 930 |  |  |
| 332 | 401 | 313 | 453 |

0.075

Unified Configuration

0.050

Density

0.025

0.000

Execution Time (minutes)

Figure 11: Kernel density of execution time distribution dur-

ing vulnerability validation across both model configurations.

6 Real-World Vulnerability Detection

To evaluate A2’s effectiveness on real-world production appli-

cations, we conduct experiments on a real-world dataset com-

| Completion Token | Completion Token | 2716169 | Prompt Token | Prompt Token |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | 6 | 10 | 6 | 10 | 6 | 10 | 6 |  |  |  |  |
| 10 | 5 | 10 | 5 | 10 | 5 | 10 | 5 |  |  |  |  |
| 10 | 4 | 6981 | 4 | 21270 | 21270 | 1173218545 | 17471 | 24616 | 24594 |  |  |
| 3450 | 3450 | 4407 | 10 | 7269 | 5706 |  |  |  |  |  |  |
| 2994 | 2945 | 2762 | 4618 | 5627 |  |  |  |  |  |  |  |
| 10 | 3 | 1427 | 1547 | 3 | 10 | 3 | 10 | 3 |  |  |  |
| 10 | 2 | 214 | 138 | 10 | 2 | 10 | 2 | 10 | 2 |  |  |
| 2.5-flash 2.5-pro | oss | o3 | 2.5-flash 2.5-pro | oss | o3 | Planner | Executor | Validator | Planner | Executor | Validator |
| Model | Model | Component | Component |  |  |  |  |  |  |  |  |
| (a) Detection Phase | (b) Aggregation Phase | (c) Mixed Configuration | (d) Unified Configuration |  |  |  |  |  |  |  |  |

Figure 10: Token consumption analysis across different phases and configurations. Green areas represent prompt tokens, pink

areas represent completion tokens. (a) Individual model performance during vulnerability detection, (b) Token usage during

multi-tool result aggregation, (c) Component-wise analysis with Planner using gemini-2.5-pro and Executor/Validator using

| ing individual vulnerability detection (Figure 10a), models | Mixed Configuration |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| sumption with median prompt tokens of 222,733 (mixed con- | 10 | 20 | 30 | 40 | 50 | 60 |
| Economic Cost Assessment. | Based on model pricing in | mean execution time of 11.14 minutes (median 8.29 min- |  |  |  |  |
| our LLM selection criteria 5.2, we estimate per-vulnerability | utes, | σ | = 11.70), while unified configuration demonstrates |  |  |  |
| validation costs across configurations. Detection-only costs | 9.62 minutes mean (median 9.24 minutes, | σ | = 6.44). Both |  |  |  |
| range from $0.003-0.029 per APK (o3), $0.0004-0.001 per | configurations complete 75% of vulnerabilities within 11 min- |  |  |  |  |  |
| APK (gpt-oss-120b), to $0.002-0.014 per APK (Gemini vari- | utes, indicating comparable baseline throughput. However, |  |  |  |  |  |
| ants). Aggregation increases costs to $0.04-0.33 per APK | temporal outliers extend to 63 minutes (mixed) and 41 min- |  |  |  |  |  |
| for gpt-oss-120b, $0.06-0.66 per APK for gemini-2.5-flash, | utes (unified), representing | < | 5% of validation cases requiring |  |  |  |
| $0.26-0.61 per APK for gemini-2.5-pro, and $0.84-3.35 per | extended analysis. The unified configuration exhibits 45% |  |  |  |  |  |
| APK for o3. Full validation pipeline costs vary significantly: | reduced variance and 35% lower maximum execution time |  |  |  |  |  |
| mixed configuration averages $0.59-4.23 per vulnerability | due to reduced function call requirements, enabling validation |  |  |  |  |  |
| (median $1.77), while unified gemini-2.5-pro configuration | completion with fewer execution steps. |  |  |  |  |  |
| Efficiency Analysis. | We analyze A2’s time overhead. Dur- | prising 169 APKs with an average of 115,696 lines of code |  |  |  |  |
| ing Agentic Vulnerability Discovery, efficiency differences | per application. The experimental configuration employs (i) |  |  |  |  |  |
| primarily stem from varying model request times since this | two gemini-2.5-pro models as detectors with gemini-2.5-flash |  |  |  |  |  |
| phase involves code-level analysis without dynamic APK in- | as aggregator, and (ii) gemini-2.5-flash as planner, executor, |  |  |  |  |  |
| teraction. We focus on Agentic Vulnerability Validation time | and validator for the validation pipeline. After excluding 9 |  |  |  |  |  |
| overhead. Figure 11 presents execution time distributions | APKs that cannot be installed on the Android emulator, we |  |  |  |  |  |
| across both configurations. Mixed configuration achieves | analyze the remaining 160 APKs. |  |  |  |  |  |

---

## Page 12

TABLE 5: Classification of True Positive (TP) Test Cases by Vulnerability

Type. Speculative refers to speculative vulnerability findings, and Validated

| Type | Speculative | Validated |
| --- | --- | --- |
| Network Communication | 23 | 1 |
| Data Exposure | 22 | 17 |
| Inter-Component Communication | 12 | 9 |
| Total | 104 | 57 |

We apply A2 to scan the 160 APKs. During the Agentic

Vulnerability Discovery phase, A2 reports 136 speculative

Do We Still Need SAST Tools? Despite LLM-based ana-

lyzers achieving superior vulnerability coverage compared to

individual SAST tools, traditional static analysis retains criti-

cal value within A2’s architecture. (i) Exploit Path Guidance :

Static tools excel at providing code-line granular vulnerabil-

ity localization and data flow analysis that enables precise

source-to-sink path identification. This information, when ag-

gregated into standardized reports, assists the PoC Planner

12

1 public static boolean isClassPreloadingAppEnabled (

Context context ) {

| 3 | boolean | zExists | = | fileA01 . exists () ; |
| --- | --- | --- | --- | --- |
| 4 | fileA01 . delete () ; |  |  |  |
| 5 | return | zExists ; |  |  |

6 }

context , String str ) {

10 fileA01 . delete () ;

11 return zExists ;

12 }

Figure 12: A path traversal vulnerability reported in discovery

This behavior becomes especially pronounced after about

14 execution steps in our real-world evaluation, resulting

work will explore cycle-detection mechanisms that halt Task

Executors once consecutive identical function calls (same

function, same arguments) exceed a threshold N , thereby

triggering summarization or alternative strategies to maintain

execution efficiency.

8 Limitations

| refers to validated vulnerability findings. | 2 | File | fileA01 | = | AnonymousClass000 . A01 ( context ); |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Authorization | 19 | 9 | 7 | public | static | boolean | isClassPreloadingEnabled ( Context |  |
| Code Injection | 15 | 12 | 8 | File | fileA01 | = | AnonymousClass000 . A01 ( context , | str ); |
| WebView | 13 | 9 | 9 | boolean | zExists | = | fileA01 . exists () ; |  |
| Detection Results. | Table 4 presents the detection results. | stage but eliminated in validation stage. |  |  |  |  |  |  |
| vulnerabilities. In the Agentic Vulnerability Validation phase, | point identification. | (ii) Hallucination Filtering | : Call graph |  |  |  |  |  |
| A2 successfully reports 60 validated vulnerability findings | analysis mitigates LLM false positives when context windows |  |  |  |  |  |  |  |
| and filters out 29 false positive findings. Through manual | approach model capacity limits, preventing phantom function |  |  |  |  |  |  |  |
| review, we further identify that only 3 out of the 60 validated | invocation claims that lead to validation overhead. Consider |  |  |  |  |  |  |  |
| vulnerability findings are false positives, resulting in a false | the following anonymized code fragment from our real-world |  |  |  |  |  |  |  |
| positive rate of 5.0% (3/60). | evaluation dataset (Figure 12): |  |  |  |  |  |  |  |
| Vulnerability Classification. | Table 5 analyzes the distribu- | Our LLM analyzer identified this as a | Path Traversal | vul- |  |  |  |  |
| tion of true positive vulnerability types across discovery and | nerability due to unsanitized string parameters directly con- |  |  |  |  |  |  |  |
| validation phases. Agentic Vulnerability Validation demon- | structing file paths, potentially leading to deleting critical |  |  |  |  |  |  |  |
| strates high effectiveness for Data Exposure vulnerabilities, | databases or shared preferences files. However, call graph |  |  |  |  |  |  |  |
| validating 77.3% (17/22) of speculative findings. Code In- | analysis revealed these methods lack both internal invocation |  |  |  |  |  |  |  |
| jection vulnerabilities also show strong validation rates at | and external exposure, rendering the speculative vulnerability |  |  |  |  |  |  |  |
| 80.0% (12/15). In contrast, Network Communication vulnera- | finding a false positive despite structural vulnerability pres- |  |  |  |  |  |  |  |
| bilities exhibit low validation rates at 4.3% (1/23). Similar to | ence. While our validation framework correctly classified |  |  |  |  |  |  |  |
| the Ghera dataset findings, network-related vulnerabilities in- | this as | FP | , integrating call graph analysis tools like Android- |  |  |  |  |  |
| volve man-in-the-middle attacks, certificate manipulation, and | Guard [26] during discovery phases could eliminate such |  |  |  |  |  |  |  |
| network traffic monitoring that require infrastructure beyond | spurious vulnerability findings, reducing validation costs. |  |  |  |  |  |  |  |
| the Android emulator capabilities that A2 currently lacks. | Long-Context | Function-Calling | Degradation. | The |  |  |  |  |
| Responsible Disclosure. | Following security research prac- | Planner-Executor-Validator | architecture | is | designed | to |  |  |
| tices, we | responsibly | disclose | identified vulnerabilities | decompose validation tasks into step-by-step operations. |  |  |  |  |
| through bug bounty programs, official guidelines, or direct | However, as execution sequences grow longer, we observe |  |  |  |  |  |  |  |
| contact with developers. Confirmed cases are documented and | a | degradation | in | function-calling | accuracy, particularly |  |  |  |
| reported via proper channels, with sufficient time for remedi- | when calls deviate from expected outcomes. In practice, |  |  |  |  |  |  |  |
| ation before public release. The findings span cryptographic, | gemini-2.5-flash and gemini-2.5-pro exhibit long-context |  |  |  |  |  |  |  |
| input validation, and access control flaws, demonstrating A2’s | function-calling degradation [36], where the models repeat- |  |  |  |  |  |  |  |
| broad detection capabilities in real-world Android apps. Full | edly invoke the same function with identical arguments, |  |  |  |  |  |  |  |
| details will be shared after remediation. | relying on local context rather than global optimization. |  |  |  |  |  |  |  |
| 7 | Discussion | in substantial cost overhead. To mitigate this issue, future |  |  |  |  |  |  |
| in synthesizing targeted attack vectors through precise entry | Key caveats are noted to clarify the scope of our findings: |  |  |  |  |  |  |  |

---

## Page 13

| Vulnerability Discovery Scope. | As shown in Table 6 in the | seeing [35] operates directly on bytecode to resist obfuscation. |  |
| --- | --- | --- | --- |
| Appendix, the aggregation approach achieves 78.3% recall | However, a comprehensive study by Zhu et al. [14] revealed |  |  |
| (47/60 vulnerabilities), leaving 13 vulnerabilities undetected | fundamental limitations across 11 Android SAST tools: they |  |  |
| across all evaluation tools. These limitations fall into three pri- | miss numerous vulnerability classes and generate excessive |  |  |
| mary categories: | (i) | Android manifest configuration vulnera- | false positives. Beyond detection, Chen et al. [37] demon- |
| bilities requiring runtime environment understanding, such as | strated automated attack generation through GUI-squatting |  |  |
| TaskAffinity-based attacks that exploit inter-application task | that creates phishing apps. Despite these advances, current |  |  |
| management beyond static code analysis; | (ii) | runtime context | tools cannot automatically validate or exploit their findings, |
| dependencies exemplified by permission bypass vulnerabili- | requiring extensive manual verification that creates a critical |  |  |
| ties like CheckPermission-PrivilegeEscalation, which exploit | gap between detection and validation. |  |  |
| timing-sensitive behavior of Binder methods when called | LLMs in Android Testing. | Large language models have |  |
| from different thread contexts; and | (iii) | protocol-level im- | introduced semantic reasoning to Android testing. Auto- |
| plementation subtleties, including InsecureSSLSocket-MITM | Droid [22] pioneered LLM-driven UI automation, achiev- |  |  |
| vulnerabilities that depend on recognizing the distinction be- | ing 71.3% task completion without manual scripting. LLM- |  |  |
| tween certificate authority validation and hostname verifica- | Droid [38] strategically invokes LLMs when traditional |  |  |
| tion in SSLCertificateSocketFactory implementations. | crawlers plateau, improving code coverage by 26%. Vision- |  |  |
| Vulnerability Validation Scope. | As noted in Section 5.5, | Droid [29] leverages multimodal models to detect non-crash |  |
| 17 of 82 speculative vulnerability findings fall outside A2’s | bugs that evade traditional tools. Supporting frameworks |  |  |
| current validation capabilities. These involve cases like net- | like Guardian [39] optimize LLM computational overhead |  |  |
| work traffic monitoring or man-in-the-middle attacks that | through specialized runtime systems. While these approaches |  |  |
| require infrastructure beyond the Android emulator, such as | significantly expand testing capabilities through intelligent |  |  |
| packet interception or SSL manipulation. Since the framework | navigation and input generation, they primarily target func- |  |  |
| relies on observable app state changes, it is less effective for | tional correctness rather than security vulnerabilities, leaving |  |  |
| vulnerabilities that manifest only through external network | LLM-based vulnerability discovery and exploit generation |  |  |
| behavior or specialized attack setups. | largely unexplored in the Android domain. |  |  |
| LLM Reasoning Reliability. | Despite implementing multi- | Automated Exploit Generation. | Recent research demon- |
| agent validation mechanisms, A2 exhibits residual halluci- | strates LLMs’ potential for autonomous exploitation across |  |  |
| nation rates ranging from 4.7% to 12.6%, as evidenced in | security domains [40–42]. In mobile security, AdbGPT [43] |  |  |
| Table 7 in the Appendix. The | Task Validator | successfully fil- | reproduces crashes from natural-language bug reports with |
| ters erroneous claims through dynamically generated oracles, | 81.3% success. | Fang et al. | showed GPT-4 agents can |
| yet cannot completely eliminate false positives, particularly | autonomously hack websites | through blind SQL | injec- |
| for semantic vulnerabilities where oracle generation proves | tion [44], with multi-agent teams achieving 4.3× higher suc- |  |  |
| challenging. For instance, unified configuration misclassifies | cess rates [45]. For smart contracts, Gervais and Zhou’s A1 |  |  |
| OpenSocket-InformationLeak-2 as a true positive, demonstrat- | system [31] equips LLMs with blockchain-specific tools to |  |  |
| ing the difficulty in programmatically determining sensitive | generate and validate exploits end-to-end, achieving 63% suc- |  |  |
| information exposure without human judgment. | cess rate on vulnerable contracts with multi-million-dollar at- |  |  |
| Context Window Constraints. | As noted in Section 5.1, | tack payloads. These studies demonstrate that domain-specific |  |
| model context limitations necessitate filtering APKs to those | tool integration enables exploit generation, yet this capabil- |  |  |
| under 5MB during vulnerability detection phases. This con- | ity remains unrealized for Android applications—our work |  |  |
| straint potentially excludes larger, more complex applica- | bridges this gap by combining Android vulnerability detection |  |  |
| tions that may harbor vulnerabilities, thereby limiting the | with automated validation through concrete PoC generation. |  |  |

approach’s applicability to enterprise-scale mobile applica-

tions. When application complexity exceeds context window

10 Conclusion

capacity, reduced analysis coverage may lead to decreased

detection effectiveness and increased false negative rates.

We presented A2, a system that combines agentic discovery

with validation to mirror how human experts analyze Android

9 Related Works applications. On the Ghera benchmark, A2 achieves higher

coverage than existing tools, reduces noise, and provides con-

| Security Analysis of Android Applications. | Android se- | crete proof-of-concept exploits. In real-world evaluation, A2 |
| --- | --- | --- |
| curity tools employ diverse approaches to vulnerability detec- | uncovered 104 previously unknown zero-day vulnerabilities, |  |
| tion. MobSF [5] combines static and dynamic analysis in an | over half of which were self-validated with working exploits. |  |
| all-in-one framework, while APKHunt [6] achieves the broad- | By turning speculative findings into validated vulnerabilities, |  |
| est coverage (67% of OWASP MASVS categories) through ex- | A2 takes a step toward practical, automated security analysis |  |
| haustive pattern matching on decompiled sources [14]. True- | for the Android ecosystem. |  |

13

---

## Page 14

References York, NY, USA, 2016. Association for Computing Ma-

[1] Google Play Console Developer Dashboard. Android

com/distribute/console , 2024. Accessed: 2024-01-

01.

[3] OWASP Foundation. Source code analysis tools, 2024.

OWASP Community Pages.

droid: Precise context, flow, field, object-sensitive and

lifecycle-aware taint analysis for android apps. In Pro-

ceedings of the 35th ACM SIGPLAN Conference on

Programming Language Design and Implementation ,

PLDI ’14, pages 259–269, New York, NY, USA, 2014.

Association for Computing Machinery.

2024. Version 4.0.7.

code analysis tool for android apps, 2024. Version 2.1.3.

USA, 2013. IEEE Press.

[9] OWASP Foundation. Dynamic application security test-

ing, 2024. OWASP Community Pages.

Tellenbach, and Jacques Klein. Dynamic security anal-

ysis on android: A systematic literature review. IEEE

Access , 12:57261–57287, 2024.

Software Repositories , MSR ’16, pages 468–471, New

14

chinery.

Documentation.

[13] Haichuan Xu, Mingxuan Li, Qiben Chen, and Atul

USENIX Association.

[14] Jingyun Zhu, Kaixuan Li, Sen Chen, Lingling Fan, Jun-

2024.

[15] OWASP Foundation. Static code analysis, 2024.

OWASP Community Controls.

[16] LinkedIn Corporation. QARK: Quick android review

kit, 2019. Tool to look for several security related An-

[17] Yu-Cheng Lin. AndroBugs: An efficient android vulner-

[18] Fengguo Wei, Sankardas Roy, Xinming Ou, and Robby.

net Society, 2015.

[20] John Smith, Jane Lee, and Chen Wang. Llms in software

security: A survey of vulnerability detection techniques

[21] Yuqiang Liu, Yizhuo Lu, Xiaohang Chen, Yuxing Wang,

Zhengzi Xu, Wenbo Liu, Jiahao Chen, Zhenguang

Liu, Peiyu Chen, Zhaofeng Zhao, Shengwei Wei, and

IEEE Press, 2023.

| app statistics 2024. | https://developer.android. | [12] Google. Android components, 2024. Android Developer |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [2] Verizon. | 2024 | mobile | security | index | report. | Prakash. | Dva: Extracting victims and abuse vectors |
| https://www.verizon.com/business/resources/ | from android accessibility malware. | In | Proceedings |  |  |  |  |
| reports/mobile-security-index/ | , 2024. | Ac- | of the 33rd USENIX Security Symposium | , USENIX Se- |  |  |  |
| cessed: 2024-08-05. | curity ’24, pages 1–18, Philadelphia, PA, USA, 2024. |  |  |  |  |  |  |
| [4] Steven | Arzt, Siegfried | Rasthofer, Christian | Fritz, | jie Wang, and Xiaofei Xie. A comprehensive study on |  |  |  |
| Eric Bodden, Alexandre Bartel, Jacques Klein, Yves | static application security testing (sast) tools for android. |  |  |  |  |  |  |
| Le Traon, Damien Octeau, and Patrick McDaniel. Flow- | IEEE Trans. Softw. Eng. | , page 3385–3402, December |  |  |  |  |  |
| [5] Ajin Abraham. | MobSF: Mobile security framework, | droid application vulnerabilities. |  |  |  |  |  |
| [6] Cyber Security Labs. APKHunt: A comprehensive static | ability scanner, 2016. Version 1.0.0. |  |  |  |  |  |  |
| [7] Daniel Votipka, Kelsey R Fulton, James Parker, Matthew | Amandroid: A precise and general inter-component data |  |  |  |  |  |  |
| Hou, Michelle L Mazurek, and Michael Hicks. Under- | flow analysis framework for security vetting of android |  |  |  |  |  |  |
| standing security mistakes developers make: Qualitative | apps. In | Proceedings of the 2014 ACM SIGSAC Confer- |  |  |  |  |  |
| analysis from build it, break it, fix it. In | 29th USENIX | ence on Computer and Communications Security | , CCS |  |  |  |  |
| Security Symposium (USENIX Security 20) | , pages 247– | ’14, pages 1329–1341, New York, NY, USA, 2014. As- |  |  |  |  |  |
| 264, 2020. | sociation for Computing Machinery. |  |  |  |  |  |  |
| [8] Brittany Johnson, Yoonkyong Song, Emerson Murphy- | [19] Michael I. Gordon, Deokhwan Kim, Jeff H. Perkins, |  |  |  |  |  |  |
| Hill, and Robert Bowdidge. Why don’t software devel- | Limei Gilham, Nguyen Nguyen, and Martin C. Rinard. |  |  |  |  |  |  |
| opers use static analysis tools to find bugs? In | Proceed- | Information flow analysis of android applications in |  |  |  |  |  |
| ings of the 2013 International Conference on Software | droidsafe. | In | Proceedings of the Network and Dis- |  |  |  |  |
| Engineering | , ICSE ’13, pages 672–681, Piscataway, NJ, | tributed System Security Symposium | , NDSS ’15. Inter- |  |  |  |  |
| [10] Thomas Sutter, Timo Kehrer, Marc Rennhard, Bernhard | and insights. | arXiv preprint arXiv:2502.07049 | , 2024. |  |  |  |  |
| [11] Kevin Allix, Tegawendé F. Bissyandé, Jacques Klein, | Yongjun Peng. Gptscan: Detecting logic vulnerabilities |  |  |  |  |  |  |
| and Yves Le Traon. Androzoo: Collecting millions of | in smart contracts by combining gpt with program analy- |  |  |  |  |  |  |
| android apps for the research community. In | Proceed- | sis. In | Proceedings of the 45th International Conference |  |  |  |  |
| ings of the 13th International Conference on Mining | on Software Engineering | , ICSE ’23, pages 2169–2181. |  |  |  |  |  |

---

## Page 15

| [22] Hao Wen, Yuanchun Li, Guohong Liu, Shanhui Zhao, | [34] Martin Blanda. Fuzzing android: A recipe for uncover- |
| --- | --- |
| Tao Yu, Toby Jia-Jun Li, Shiqi Jiang, Yunhao Liu, Yaqin | ing vulnerabilities inside system components in android. |
| Zhang, and Yunxin Liu. Autodroid: Llm-powered task | White paper, Black Hat Europe, 2015. |

automation in android. ACM MobiCom ’24, page

pabilities and limitations. In Proceedings of the 31st

ACM Conference on Computer and Communications Se-

curity , CCS ’24, pages 445–460, New York, NY, USA,

2024. Association for Computing Machinery.

[24] LangChain. Langgraph. https://langchain-ai.

github.io/langgraph/ , 2024. Multi-agent workflow

orchestration framework.

[26] AndroidGuard. Androidguard: Android manifest analy-

Shar, and Mariano Ceccato. VLM-Fuzz: Vision lan-

[29] Zhe Liu, Cheng Li, Chunyang Chen, Junjie Wang, Boyu

[30] Yiheng Xiong, Mengqian Xu, Ting Su, Jingling Sun, Jue

national Symposium on Software Testing and Analysis ,

ISSTA 2023, pages 1319–1331, New York, NY, USA,

arXiv preprint arXiv:2507.05558 , 2024.

15

[37] Qinggang Chen, Lingling Han, Peng Liu, Zhemin Zhang,

and Yang Liu. Gui-squatting attack: Automated genera-

tion of android phishing apps. In IEEE Transactions on

Dependable and Secure Computing , pages 1–14, 2019.

[38] Yanqi Wang, Juntao Chen, Ting Su, Sen Chen, et al.

Llmdroid: Enhancing automated mobile app gui test-

ing coverage with large language model guidance. In

ume 1, pages 1–23, 2024.

and Yu Feng. Guardian: A runtime framework for llm-

SIGSOFT International Symposium on Software Testing

arXiv:2504.05408 , 2025.

2025.

arXiv:2505.15216 , 2025.

Wang, Yang Liu, and Sen Chen. Prompting is all your

pages 1–12, 2024.

| 543–557, New York, NY, USA. Association for Com- | [35] Takeshi Terada. Trueseeing: Non-decompiling android |  |  |  |
| --- | --- | --- | --- | --- |
| puting Machinery. | application vulnerability scanner, 2024. Version 2.2.4. |  |  |  |
| [23] Richard Chen, Sofia Martinez, and David Kim. | Au- | [36] Ziming Wang, Li Chen, and Wei Zhang. Long-context |  |  |
| tonomous llm agents for vulnerability exploitation: Ca- | function calling degradation in language models, 2024. |  |  |  |
| [25] Jadx: Dex to java decompiler, 2020. | Proceedings of the ACM on Software Engineering | , vol- |  |  |
| sis tool, 2024. Android security analysis framework. | [39] Haoran Yoon, Tianyu Liu, Hanlin Wang, Mingxuan Li, |  |  |  |
| [27] Android emulator, 2020. | based ui exploration. In | Proceedings of the 33rd ACM |  |  |
| [28] Biniam Fisseha Demissie, Yan Naing Tun, Lwin Khin | and Analysis | , ISSTA 2024, pages 1234–1245, 2024. |  |  |
| guage model assisted recursive depth-first search explo- | [40] Wenbo Guo, Yujin Potter, Tianneng Shi, Zhun Wang, |  |  |  |
| ration for effective ui testing of android apps. | arXiv | Andy Zhang, and Dawn Song. | Frontier ai’s im- |  |
| preprint arXiv:2504.11675 | , 2025. | pact on the cybersecurity landscape. | arXiv preprint |  |
| Wu, Yawen Wang, Jun Hu, and Qing Wang. | Vision- | [41] Zhun Wang, Tianneng Shi, Jingxuan He, Matthew Cai, |  |  |
| driven automated mobile gui testing via multimodal | Jialin Zhang, and Dawn Song. Cybergym: Evaluating |  |  |  |
| large language model. | arXiv preprint arXiv:2407.03037 | , | ai agents’ cybersecurity capabilities with real-world vul- |  |
| 2024. | nerabilities at scale. | arXiv preprint arXiv:2506.02548 | , |  |
| Wang, He Wen, Geguang Pu, Jifeng He, and Zhendong | [42] Andy K. Zhang, Joey Ji, Celeste Menders, et al. Bounty- |  |  |  |
| Su. An empirical study of functional bugs in android | bench: Dollar impact of ai agent attackers and defenders |  |  |  |
| apps. In | Proceedings of the 32nd ACM SIGSOFT Inter- | on real-world cybersecurity systems. | arXiv preprint |  |
| 2023. Association for Computing Machinery. | [43] Si Xuan Feng, Mingyue Li, Chongwen Ma, Jingling |  |  |  |
| [31] Sihao Gervais and Lei Zhou. A1: Autonomous multi- | need: Automated android bug replay with large language |  |  |  |
| agent system for blockchain security enhancement | models. In | Proceedings of the 46th IEEE/ACM Interna- |  |  |
| through real-time exploit generation and validation. | tional Conference on Software Engineering | , ICSE 2024, |  |  |
| [32] Ghera: Repository of android application vulnerabil- | [44] Richard Fang, Rohan Bindu, Akul Gupta, Qiusi Zhan, |  |  |  |
| ity benchmarks. | https://secure-it-i.bitbucket. | and Daniel Kang. Llm agents can autonomously hack |  |  |
| io/ghera/index.html | , 2017. | websites. | arXiv preprint arXiv:2402.06664 | , 2024. |
| [33] Thiago Peixoto. Introduction to fuzzing android native | [45] Richard Fang, Rohan Bindu, Akul Gupta, and Daniel |  |  |  |
| components. Conviso AppSec Blog, 11 2024. Category: | Kang. Teams of llm agents can exploit zero-day vulner- |  |  |  |
| Code Fighters. | abilities. | arXiv preprint arXiv:2406.01637 | , 2024. |  |

---

## Page 16

11 Ethical Considerations affiliation and a declared research purpose, striking a balance

between open science and responsible disclosure.

| This research is conducted with careful attention to ethical | Broader Impact Assessment | The research contributes pos- |
| --- | --- | --- |
| responsibilities, which are detailed below. | itively to Android application security by providing enhanced |  |
| Vulnerability Assessment Environment | All vulnerability | vulnerability detection capabilities that can strengthen the |
| assessments are conducted in controlled, isolated environ- | overall security posture of the mobile application ecosystem. |  |
| ments that do not involve real user data or privacy. The Ghera | By enabling more effective identification and validation of |  |
| benchmark dataset consists of synthetically vulnerable APKs | security vulnerabilities, A2 supports proactive security mea- |  |
| designed specifically for security research, eliminating con- | sures that benefit end users through improved application |  |
| cerns about real-world user privacy or data exposure. For | security. The responsible disclosure practices employed en- |  |
| production APK analysis, applications are obtained from An- | sure that identified vulnerabilities are remediated rather than |  |
| droZoo, a research-oriented dataset that aggregates publicly | exploited maliciously. |  |

available APKs without including user data. All testing is

performed on local Android emulators in sandboxed environ-

12 Open Science

ments, ensuring no interaction with live production systems

| or user devices. | The Ghera benchmark dataset containing 60 vulnerable An- |  |
| --- | --- | --- |
| Responsible Vulnerability Disclosure | Following estab- | droid APKs is also publicly available through its official repos- |
| lished security research practices, all identified vulnerabilities | itory [32]. To mitigate potential misuse (detailed in the Ethical |  |
| undergo responsible disclosure procedures. Upon confirma- | Considerations section), we will implement a controlled ac- |  |
| tion of vulnerabilities in production applications, affected | cess policy. Researchers can request access by contacting us |  |
| developers and security teams are immediately contacted | through their institutional email, stating their name, affiliation, |  |
| through appropriate channels, including official bug bounty | and intended use. We will then vet the provided information |  |
| programs, GitHub repositories, and direct developer commu- | and grant or deny access to the source code. Our goal is to |  |
| nication. Each disclosure includes comprehensive documen- | grant access to academic and industry researchers for pur- |  |
| tation of the vulnerability details, exploitation mechanics, | poses of building upon our research or advancing the field |  |
| and recommended remediation strategies. Adequate time is | of Android security, while ensuring A2 is not exploited for |  |
| provided for vulnerability remediation before any public dis- | malicious purposes. |  |
| closure, adhering to industry-standard timelines. No specific | The production APK dataset comprising 169 applications |  |
| vulnerability details are disclosed in this paper until remedia- | from AndroZoo [11] is accessible through the AndroZoo |  |
| tion is complete. | research platform with appropriate academic credentials. For |  |
| Dataset and Privacy Considerations | The research datasets | security considerations, specific application identifiers and |
| utilized pose minimal privacy risks. The Ghera benchmark | vulnerable application details from the production dataset |  |
| contains no real user data, consisting entirely of synthetic | are not disclosed to prevent potential misuse by malicious |  |
| vulnerable applications created for research purposes. The | actors, unless researchers contact us and provide appropriate |  |
| AndroZoo dataset comprises publicly distributed applications | academic credentials. |  |

without user-generated content or personal data. All analysis

is conducted on application binaries and source code, not on

user data or behavioral information. The research methodol-

ogy specifically avoids any collection, processing, or analysis

of personal user information.

Artifact Availability and Potential for Misuse Any vul-

nerability discovery tool carries a general risk of misuse, since

the same techniques that help defenders identify weaknesses

could be repurposed by attackers. A2 is no exception: its

ability to generate working exploits could, in principle, be

abused against production applications. At the same time, this

risk is not unique to our work—numerous open-source and

commercial tools already provide comparable capabilities.

The intent of A2 is defensive: to help researchers and devel-

opers identify and fix vulnerabilities before they are exploited

in the wild. Its novelty lies in combining discovery with auto-

mated validation, enabling more reliable security assessments.

To further reduce misuse risk, artifact access is managed un-

der a controlled distribution strategy that requires institutional

16

---

## Page 17

TABLE 6: Vulnerability detection results from three SAST tools and four large language models, and aggregation results from four models on the Ghera dataset.

Vulnerabilities are organized into eight categories: Crypto, ICC, Networking, NonAPI, Permission, Storage, System, and Web. Numbers indicate reported issue

counts; checkmarks ( ✓ ) or crosses ( × ) indicate successful or missed detections. Asterisks ( ∗ ) mark vulnerabilities detected only by LLM.

| Vulnerability Name | Vulnerability Detection | Vulnerability Aggregation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MobSF | APKHu. | Trues. | G2.5F | G2.5P | OSS | O3 | G2.5F | G2.5P | OSS | O3 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| BlockCipher-ECB-InformationExposure | 95 | ✓ | 25 | ✓ | 18 | ✓ | 3 | × | 3 | ✓ | 6 | ✓ | 4 | ✓ | 3 | ✓ | 3 | ✓ | 4 | ✓ | 3 | ✓ |  |
| BlockCipher-NonRandomIV-InformationExposure | ∗ | 91 | × | 24 | × | 18 | × | 3 | ✓ | 2 | ✓ | 5 | ✓ | 4 | ✓ | 2 | ✓ | 2 | ✓ | 3 | ✓ | 3 | ✓ |
| ConstantKey-ForgeryAttack | 107 | × | 22 | × | 17 | ✓ | 2 | ✓ | 2 | ✓ | 4 | ✓ | 3 | ✓ | 1 | ✓ | 1 | ✓ | 3 | ✓ | 2 | ✓ |  |
| ExposedCredentials-InformationExposure | ∗ | 91 | × | 23 | × | 16 | × | 1 | ✓ | 1 | ✓ | 3 | ✓ | 2 | ✓ | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ |
| PBE-ConstantSalt-InformationExposure | ∗ | 95 | × | 24 | × | 18 | × | 3 | × | 3 | ✓ | 4 | ✓ | 3 | ✓ | 3 | ✓ | 2 | ✓ | 2 | ✓ | 3 | ✓ |
| DynamicRegBroadcastReceiver-UnrestrictedAccess | ∗ | 92 | × | 23 | × | 16 | × | 1 | ✓ | 1 | ✓ | 2 | ✓ | 2 | ✓ | 2 | ✓ | 1 | ✓ | 3 | ✓ | 1 | ✓ |
| EmptyPendingIntent-PrivEscalation | ∗ | 94 | × | 22 | × | 15 | × | 1 | ✓ | 1 | ✓ | 3 | ✓ | 2 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ |
| FragmentInjection-PrivEscalation | ∗ | 94 | × | 21 | × | 15 | × | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ |
| HighPriority-ActivityHijack | 94 | × | 21 | ✓ | 15 | × | 2 | ✓ | 3 | ✓ | 2 | ✓ | 2 | ✓ | 3 | ✓ | 2 | ✓ | 3 | ✓ | 2 | ✓ |  |
| ImplicitPendingIntent-IntentHijack | ∗ | 95 | × | 22 | × | 15 | × | 2 | × | 2 | × | 3 | × | 3 | ✓ | 2 | ✓ | 2 | ✓ | 3 | ✓ | 2 | ✓ |
| InadequatePathPermission-InformationExposure | ∗ | 94 | × | 23 | × | 16 | × | 1 | × | 1 | × | 4 | × | 2 | ✓ | 1 | ✓ | 1 | ✓ | 3 | ✓ | 1 | ✓ |
| IncorrectHandlingImplicitIntent-UnauthorizedAccess | 92 | × | 21 | × | 15 | ✓ | 1 | ✓ | 1 | ✓ | 2 | ✓ | 3 | ✓ | 3 | ✓ | 1 | ✓ | 2 | ✓ | 2 | ✓ |  |
| NoValidityCheckOnBroadcastMsg-UnintendedInvocation | 95 | × | 23 | × | 17 | ✓ | 1 | × | 2 | × | 3 | ✓ | 2 | ✓ | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ |  |
| OrderedBroadcast-DataInjection | 93 | × | 24 | × | 17 | × | 1 | × | 1 | × | 4 | × | 1 | × | 2 | × | 1 | × | 2 | × | 1 | × |  |
| StickyBroadcast-DataInjection | ∗ | 94 | × | 23 | × | 16 | × | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ |
| TaskAffinity-ActivityHijack | 94 | × | 23 | × | 16 | × | 2 | × | 2 | × | 6 | × | 1 | × | 2 | × | 1 | × | 2 | × | 1 | × |  |
| TaskAffinity-LauncherActivity-PhishingAttack | 94 | × | 21 | × | 15 | × | 0 | × | 0 | × | 3 | × | 0 | × | 1 | × | 1 | × | 3 | × | 1 | × |  |
| TaskAffinity-PhishingAttack | 94 | × | 23 | × | 16 | × | 2 | × | 2 | × | 2 | × | 1 | × | 1 | × | 1 | × | 2 | × | 1 | × |  |
| TaskAffinityAndReparenting-PhishingAndDoSAttack | 91 | × | 21 | × | 15 | × | 1 | × | 2 | × | 7 | × | 1 | × | 2 | × | 1 | × | 4 | × | 2 | × |  |
| UnhandledException-DOS | ∗ | 89 | × | 20 | × | 13 | × | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ |
| UnprotectedBroadcastRecv-PrivEscalation | 91 | × | 24 | ✓ | 18 | ✓ | 1 | ✓ | 2 | ✓ | 2 | ✓ | 1 | ✓ | 2 | ✓ | 2 | ✓ | 1 | ✓ | 1 | ✓ |  |
| WeakChecksOnDynamicInvocation-DataInjection | ∗ | 91 | × | 23 | × | 17 | × | 1 | ✓ | 1 | ✓ | 3 | ✓ | 2 | ✓ | 2 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ |
| CheckValidity-InformationExposure | 97 | ✓ | 25 | ✓ | 16 | × | 2 | ✓ | 2 | ✓ | 3 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 3 | ✓ | 1 | ✓ |  |
| IncorrectHostNameVerification-MITM | 97 | ✓ | 25 | ✓ | 16 | × | 2 | ✓ | 2 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ |  |
| InsecureSSLSocket-MITM | 95 | × | 23 | × | 17 | × | 1 | × | 1 | × | 1 | × | 1 | × | 1 | × | 1 | × | 1 | × | 2 | × |  |
| InsecureSSLSocketFactory-MITM | 95 | ✓ | 24 | × | 16 | × | 1 | ✓ | 2 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ |  |
| InvalidCertificateAuthority-MITM | 97 | ✓ | 25 | ✓ | 16 | × | 3 | ✓ | 2 | ✓ | 4 | ✓ | 3 | ✓ | 1 | ✓ | 2 | ✓ | 2 | ✓ | 1 | ✓ |  |
| OpenSocket-InformationLeak | 91 | × | 22 | × | 17 | × | 2 | × | 1 | × | 4 | × | 1 | × | 2 | × | 2 | × | 2 | × | 2 | × |  |
| UnEncryptedSocketComm-MITM | 97 | × | 22 | × | 17 | ✓ | 2 | ✓ | 1 | × | 3 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ | 4 | ✓ | 2 | ✓ |  |
| UnpinnedCertificates-MITM | 96 | ✓ | 27 | ✓ | 17 | × | 2 | ✓ | 3 | × | 4 | × | 1 | × | 2 | ✓ | 2 | ✓ | 4 | ✓ | 2 | ✓ |  |
| MergeManifest-UnintendedBehavior | ∗ | 94 | × | 23 | × | 16 | × | 1 | ✓ | 2 | ✓ | 3 | ✓ | 2 | ✓ | 1 | ✓ | 2 | ✓ | 2 | ✓ | 2 | ✓ |
| OutdatedLibrary-DirectoryTraversal | ∗ | 93 | × | 21 | × | 15 | × | 1 | ✓ | 1 | ✓ | 5 | ✓ | 3 | ✓ | 2 | ✓ | 1 | ✓ | 3 | ✓ | 2 | ✓ |
| UnnecessaryPerms-PrivEscalation | 94 | × | 23 | × | 16 | × | 1 | × | 1 | × | 3 | ✓ | 2 | × | 2 | × | 1 | × | 2 | × | 1 | × |  |
| WeakPermission-UnauthorizedAccess | 91 | × | 22 | ✓ | 15 | × | 1 | × | 1 | ✓ | 3 | × | 2 | × | 1 | ✓ | 1 | ✓ | 3 | ✓ | 1 | ✓ |  |
| ExternalStorage-DataInjection | 91 | × | 21 | ✓ | 15 | × | 1 | ✓ | 2 | ✓ | 1 | × | 1 | ✓ | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ |  |
| ExternalStorage-InformationLeak | 97 | × | 21 | ✓ | 15 | × | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ |  |
| InternalStorage-DirectoryTraversal | ∗ | 94 | × | 21 | × | 15 | × | 1 | ✓ | 1 | ✓ | 5 | ✓ | 2 | ✓ | 1 | ✓ | 1 | ✓ | 4 | ✓ | 1 | ✓ |
| InternalToExternalStorage-InformationLeak | ∗ | 91 | × | 22 | × | 15 | × | 1 | ✓ | 1 | ✓ | 1 | ✓ | 1 | × | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ |
| SQLite-execSQL | 98 | × | 24 | ✓ | 15 | × | 1 | ✓ | 1 | ✓ | 1 | ✓ | 2 | ✓ | 2 | ✓ | 1 | ✓ | 3 | ✓ | 2 | ✓ |  |
| SQLite-RawQuery-SQLInjection | 105 | × | 25 | ✓ | 15 | × | 1 | ✓ | 1 | ✓ | 3 | ✓ | 4 | ✓ | 3 | ✓ | 4 | ✓ | 4 | ✓ | 2 | ✓ |  |
| SQLite-SQLInjection | 101 | × | 25 | ✓ | 15 | × | 4 | ✓ | 1 | ✓ | 5 | ✓ | 4 | ✓ | 3 | ✓ | 4 | ✓ | 5 | ✓ | 3 | ✓ |  |
| CheckCallingOrSelfPermission-PrivilegeEscalation | ∗ | 91 | × | 23 | × | 16 | × | 1 | ✓ | 1 | × | 4 | × | 3 | ✓ | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ |
| CheckPermission-PrivilegeEscalation | 94 | × | 23 | × | 16 | × | 2 | × | 2 | × | 3 | ✓ | 3 | × | 1 | × | 1 | × | 4 | × | 1 | × |  |
| ClipboardUse-InformationExposure | 91 | × | 23 | ✓ | 16 | × | 1 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 3 | ✓ | 1 | ✓ |  |
| DynamicCodeLoading-CodeInjection | ∗ | 94 | × | 22 | × | 16 | × | 1 | ✓ | 1 | ✓ | 3 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ |
| EnforceCallingOrSelfPermission-PrivilegeEscalation | ∗ | 91 | × | 23 | × | 16 | × | 1 | × | 1 | × | 3 | ✓ | 3 | ✓ | 2 | ✓ | 1 | ✓ | 3 | ✓ | 2 | ✓ |
| EnforcePermission-PrivilegeEscalation | 91 | × | 23 | × | 16 | × | 1 | × | 1 | × | 5 | × | 2 | × | 1 | × | 2 | × | 4 | × | 1 | × |  |
| UniqueIDs-IdentityLeak | 94 | × | 22 | × | 17 | ✓ | 1 | ✓ | 2 | ✓ | 2 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ | 3 | ✓ | 3 | ✓ |  |
| HttpConnection-MITM | 91 | × | 23 | ✓ | 17 | ✓ | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ |  |
| JavaScriptExecution-CodeInjection | 91 | × | 25 | ✓ | 18 | × | 2 | ✓ | 2 | ✓ | 3 | ✓ | 2 | ✓ | 2 | ✓ | 1 | ✓ | 2 | ✓ | 2 | ✓ |  |
| UnsafeIntentURLImpl-InformationExposure | ∗ | 93 | × | 25 | × | 17 | × | 1 | ✓ | 1 | ✓ | 5 | ✓ | 3 | ✓ | 2 | ✓ | 2 | ✓ | 3 | ✓ | 2 | ✓ |
| WebView-CookieOverwrite | 98 | × | 24 | × | 18 | × | 1 | × | 1 | × | 3 | × | 1 | × | 1 | × | 1 | × | 2 | × | 1 | × |  |
| WebView-NoUserPermission-InformationExposure | 94 | ✓ | 25 | × | 17 | × | 2 | ✓ | 2 | ✓ | 3 | ✓ | 2 | ✓ | 1 | ✓ | 2 | ✓ | 3 | ✓ | 2 | ✓ |  |
| WebViewAllowContentAccess-UnauthorizedFileAccess | 94 | ✓ | 27 | × | 18 | × | 3 | ✓ | 2 | ✓ | 4 | ✓ | 2 | ✓ | 2 | ✓ | 1 | ✓ | 2 | ✓ | 2 | ✓ |  |
| WebViewAllowFileAccess-UnauthorizedFileAccess | 93 | ✓ | 26 | × | 17 | × | 1 | ✓ | 1 | ✓ | 4 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 3 | ✓ | 1 | ✓ |  |
| WebViewIgnoreSSLWarning-MITM | 95 | ✓ | 26 | ✓ | 18 | × | 1 | ✓ | 1 | ✓ | 3 | ✓ | 1 | ✓ | 1 | ✓ | 1 | ✓ | 2 | ✓ | 1 | ✓ |  |
| WebViewInterceptRequest-MITM | 94 | × | 30 | × | 19 | × | 3 | × | 4 | × | 5 | × | 5 | × | 2 | × | 2 | × | 3 | × | 1 | × |  |
| WebViewLoadDataWithBaseUrl-UnauthorizedFileAccess | 95 | ✓ | 25 | ✓ | 17 | × | 1 | ✓ | 1 | ✓ | 4 | × | 2 | ✓ | 1 | ✓ | 1 | ✓ | 5 | ✓ | 2 | ✓ |  |
| WebViewOverrideUrl-MITM | ∗ | 94 | × | 26 | × | 18 | × | 2 | ✓ | 2 | ✓ | 4 | ✓ | 3 | × | 2 | ✓ | 2 | ✓ | 3 | ✓ | 2 | ✓ |
| WebViewProceed-UnauthorizedAccess | 102 | × | 27 | × | 18 | × | 2 | × | 3 | × | 5 | × | 3 | × | 2 | × | 1 | × | 4 | × | 2 | × |  |
| Reported Security Issus | 5654 | 1405 | 978 | 89 | 92 | 193 | 116 | 95 | 82 | 157 | 91 |  |  |  |  |  |  |  |  |  |  |  |  |
| Detected APK Vulnerabilities | 11/60 | 18/60 | 8/60 | 40/60 | 40/60 | 42/60 | 43/60 | 47/60 | 47/60 | 47/60 | 47/60 |  |  |  |  |  |  |  |  |  |  |  |  |
| Vulnerability Recall Rate | 18.3% | 30.0% | 13.3% | 66.7% | 66.7% | 70.0% | 71.7% | 78.3% | 78.3% | 78.3% | 78.3% |  |  |  |  |  |  |  |  |  |  |  |  |

17

---

## Page 18

TABLE 7: Vulnerability exploitation results with LLM configurations (M1,M2,M3): Planner, task executor, task validator. Model abbreviations:

G2.5F=Gemini-2.5-Flash; G2.5P=Gemini-2.5-Pro. Vulnerability name suffixes: *=Benchmark dataset speculative vulnerability findings detected by

Gemini-2.5-Pro aggregation matching benchmark labels; -Num=New aggregated speculative vulnerability findings (may include false positives).

Yellow highlighted cells =False positives (FP), otherwise true positives (TP). Status symbols: ★ =TP successfully exploited; ✫ =FP correctly identified; ⊗ =TP

misclassified as FP; ⊙ =FP misclassified as TP; × =Execution error; • =Max steps reached. Function call: Total(Successful); task execution: Total(Validated). Due

to space limitations, the table omits 16 out of scope and 2 unable to install speculative vulnerability findings.

Type Vulnerability Name (G2.5P, G2.5F, G2.5F) (G2.5P, G2.5P, G2.5P)

Status Function Call Task Execution Status Function Call Task Execution

| BlockCipher-ECB-InformationExposure | ∗ | ★ | 8 (8) | 5 (5) | ★ | 5 (5) | 4 (4) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BlockCipher-ECB-InformationExposure-1 | ★ | 5 (5) | 4 (4) | ★ | 5 (5) | 4 (4) |  |
| BlockCipher-ECB-InformationExposure-2 | ★ | 5 (5) | 3 (3) | ★ | 5 (5) | 3 (3) |  |
| BlockCipher-NonRandomIV-InformationExposure | ∗ | ★ | 15 (14) | 5 (5) | ★ | 14 (14) | 5 (5) |
| Crypto | BlockCipher-NonRandomIV-InformationExposure-1 | ★ | 12 (12) | 4 (4) | ★ | 11 (11) | 5 (5) |
| ConstantKey-ForgeryAttack | ∗ | ★ | 5 (5) | 3 (3) | ★ | 7 (6) | 3 (3) |
| ExposedCredentials-InformationExposure | ∗ | × | – | – | ★ | 6 (3) | 2 (2) |
| PBE-ConstantSalt-InformationExposure | ∗ | ★ | 33 (29) | 5 (5) | ★ | 14 (14) | 5 (5) |
| PBE-ConstantSalt-InformationExposure-1 | ★ | 6 (5) | 3 (3) | ★ | 7 (7) | 3 (3) |  |
| DynamicRegBroadcastReceiver-UnrestrictedAccess | ∗ | ★ | 3 (3) | 2 (2) | ★ | 5 (5) | 4 (4) |
| EmptyPendingIntent-PrivEscalation | ∗ | ⊗ | 10 (8) | 3 (3) | ★ | 10 (10) | 5 (5) |
| FragmentInjection-PrivEscalation | ∗ | ★ | 5 (5) | 2 (2) | ★ | 8 (8) | 3 (3) |
| HighPriority-ActivityHijack | ∗ | ★ | 58 (45) | 6 (5) | ★ | 13 (13) | 4 (4) |
| ImplicitPendingIntent-IntentHijack | ∗ | ★ | 13 (11) | 5 (5) | ★ | 9 (9) | 3 (3) |
| ImplicitPendingIntent-IntentHijack-1 | ★ | 4 (4) | 3 (3) | ★ | 4 (4) | 3 (3) |  |
| InadequatePathPermission-InformationExposure | ∗ | ★ | 12 (12) | 2 (1) | ★ | 8 (8) | 4 (4) |
| IncorrectHandlingImplicitIntent-UnauthorizedAccess | ∗ | ★ | 4 (4) | 7 (7) | ★ | 4 (4) | 2 (2) |

NoValidityCheckOnBroadcastMsg-UnintendedInvocation ∗

| ICC | ★ | 5 (5) | 3 (3) | ★ | 5 (5) | 3 (3) |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OrderedBroadcast-DataInjection-1 | ★ | 6 (6) | 2 (2) | ★ | 10 (10) | 4 (4) |  |  |
| StickyBroadcast-DataInjection-1 | × | – | – | × | – | – |  |  |
| TaskAffinity-ActivityHijack-1 | ★ | 6 (6) | 4 (4) | ★ | 5 (5) | 4 (4) |  |  |
| TaskAffinity-PhishingAttack-1 | ★ | 3 (3) | 3 (3) | ★ | 7 (7) | 4 (3) |  |  |
| TaskAffinityAndReparenting-PhishingAndDoSAttack-1 | ★ | 5 (5) | 4 (4) | ★ | 6 (6) | 4 (4) |  |  |
| UnhandledException-DOS | ∗ | ★ | 3 (3) | 2 (2) | ★ | 4 (4) | 3 (3) |  |
| UnprotectedBroadcastRecv-PrivEscalation | ∗ | ★ | 1 (1) | 2 (2) | ★ | 4 (4) | 3 (3) |  |
| UnprotectedBroadcastRecv-PrivEscalation-1 | • | 117 (113) | 12 (9) | ★ | 29 (29) | 7 (6) |  |  |
| WeakChecksOnDynamicInvocation-DataInjection | ∗ | ★ | 23 (23) | 2 (1) | ★ | 8 (8) | 5 (5) |  |
| CheckValidity-InformationExposure | ∗ | ★ | 3 (3) | 2 (2) | ★ | 22 (20) | 6 (6) |  |
| Networking | InvalidCertificateAuthority-MITM-1 | ✫ | 1 (1) | 1 (1) | ✫ | 1 (1) | 1 (1) |  |
| OpenSocket-InformationLeak-1 | ✫ | 11 (11) | 6 (3) | ✫ | 11 (11) | 6 (3) |  |  |
| OpenSocket-InformationLeak-2 | ✫ | 7 (7) | 5 (3) | ⊙ | 14 (14) | 6 (6) |  |  |
| MergeManifest-UnintendedBehavior | ∗ | ★ | 4 (4) | 2 (2) | ★ | 6 (6) | 3 (3) |  |
| NonAPI | MergeManifest-UnintendedBehavior-1 | ★ | 25 (23) | 3 (3) | ★ | 10 (10) | 3 (3) |  |
| OutdatedLibrary-DirectoryTraversal-1 | ✫ | 38 (38) | 3 (2) | ✫ | 14 (14) | 3 (2) |  |  |
| Permission | UnnecesaryPerms-PrivEscalation-1 | ✫ | 1 (1) | 1 (1) | ✫ | 1 (1) | 1 (1) |  |
| WeakPermission-UnauthorizedAccess | ∗ | ★ | 7 (6) | 2 (2) | ★ | 3 (3) | 3 (2) |  |
| ExternalStorage-DataInjection | ∗ | • | 63 (58) | 6 (6) | ★ | 15 (14) | 7 (6) |  |
| ExternalStorage-InformationLeak | ∗ | • | 17 (16) | 7 (4) | × | – | – |  |
| InternalStorage-DirectoryTraversal | ∗ | ★ | 15 (15) | 2 (2) | ★ | 8 (8) | 2 (2) |  |
| InternalToExternalStorage-InformationLeak | ∗ | ★ | 12 (12) | 4 (3) | ★ | 8 (8) | 3 (3) |  |
| SQLite-execSQL | ∗ | ★ | 4 (4) | 2 (2) | ★ | 5 (5) | 3 (3) |  |
| SQLlite-RawQuery-SQLInjection | ∗ | ★ | 15 (14) | 3 (3) | ★ | 14 (14) | 5 (3) |  |
| Storage | SQLlite-RawQuery-SQLInjection-1 | ★ | 7 (6) | 4 (4) | ★ | 10 (10) | 4 (4) |  |
| SQLlite-RawQuery-SQLInjection-2 | ★ | 4 (4) | 3 (3) | ★ | 5 (5) | 4 (4) |  |  |
| SQLlite-RawQuery-SQLInjection-3 | • | 90 (74) | 7 (5) | ★ | 15 (15) | 4 (3) |  |  |
| SQLlite-SQLInjection | ∗ | ★ | 7 (7) | 2 (2) | ★ | 5 (5) | 3 (3) |  |
| SQLlite-SQLInjection-1 | ✫ | 1 (1) | 1 (1) | ✫ | 1 (1) | 1 (1) |  |  |
| SQLlite-SQLInjection-2 | ★ | 9 (6) | 3 (3) | ★ | 9 (9) | 4 (4) |  |  |
| SQLlite-SQLInjection-3 | ★ | 4 (4) | 3 (3) | ★ | 4 (4) | 3 (3) |  |  |
| CheckCallingOrSelfPermission-PrivilegeEscalation | ∗ | ★ | 5 (4) | 3 (3) | ★ | 5 (5) | 2 (2) |  |
| ClipboardUse-InformationExposure | ∗ | ★ | 5 (5) | 6 (3) | ★ | 3 (3) | 4 (4) |  |
| DynamicCodeLoading-CodeInjection | ∗ | ★ | 12 (11) | 4 (4) | ★ | 11 (11) | 4 (4) |  |
| System | EnforceCallingOrSelfPermission-PrivilegeEscalation | ∗ | ★ | 19 (18) | 4 (3) | ★ | 10 (10) | 4 (4) |
| EnforcePermission-PrivilegeEscalation-1 | • | 110 (106) | 7 (5) | • | 98 (79) | 6 (8) |  |  |
| EnforcePermission-PrivilegeEscalation-2 | ✫ | 1 (1) | 1 (1) | ✫ | 1 (1) | 1 (1) |  |  |
| UniqueIDs-IdentityLeak | ∗ | ★ | 7 (7) | 4 (3) | ★ | 5 (5) | 3 (3) |  |
| HttpConnection-MITM | ∗ | ★ | 9 (9) | 2 (2) | • | 58 (56) | 7 (7) |  |
| JavaScriptExecution-CodeInjection | ∗ | ★ | 11 (11) | 4 (4) | ★ | 10 (10) | 5 (5) |  |
| UnsafeIntentURLImpl-InformationExposure | ∗ | ⊗ | 17 (12) | 6 (5) | ★ | 7 (7) | 5 (5) |  |
| Web | WebView-NoUserPermission-InformationExposure | ∗ | • | 73 (67) | 6 (4) | ★ | 9 (9) | 5 (5) |
| WebViewAllowFileAccess-UnauthorizedFileAccess | ∗ | ★ | 5 (5) | 2 (2) | • | 58 (56) | 7 (5) |  |
| WebViewInterceptRequest-MITM-1 | ★ | 4 (4) | 3 (3) | ★ | 2 (2) | 3 (3) |  |  |
| WebViewOverrideUrl-MITM | ∗ | ★ | 12 (12) | 3 (3) | ★ | 9 (8) | 3 (3) |  |
| Statistics (TP / FP / Out of Scope / Unable to Install / Total) | 56 / 7 / 17 / 2 / 82 |  |  |  |  |  |  |  |
| Average Function Calling Per Task | 4.49 | 2.92 |  |  |  |  |  |  |
| Function Calling Success Rate | 927 / 1002 (92.5%) | 649 / 680 (95.4%) |  |  |  |  |  |  |
| Task Execution Pass Rate | 195 / 223 (87.4%) | 222 / 233 (95.3%) |  |  |  |  |  |  |
| Validated Vulnerability Finding Rate (TP / (Total - FP)) | 46 / 75 (61.3%) | 51 / 75 (68.0%) |  |  |  |  |  |  |

18

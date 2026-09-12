---
title: "Towards LLM-Enhanced Android Taint Analysis"
author: "Nicholas Miazzo; Marco Alecci; Jordan Samhi; Jacques Klein; Eleonora Losiouk"
creator: "arXiv GenPDF (tex2pdf:4af3385)"
pages: 6
---

# Towards LLM-Enhanced Android Taint Analysis

> **作者**：Nicholas Miazzo; Marco Alecci; Jordan Samhi; Jacques Klein; Eleonora Losiouk
> **總頁數**：6 頁

---

## Page 1

Towards LLM-Enhanced Android Taint Analysis

| Nicholas Miazzo | Marco Alecci |  |
| --- | --- | --- |
| University of Padova | University of Luxembourg |  |
| Padova, Italy | Luxembourg, Luxembourg |  |
| nicholas.miazzo@math.unipd.it | marco.alecci@uni.lu |  |
| Jordan Samhi | Jacques Klein | Eleonora Losiouk |
| University of Luxembourg | University of Luxembourg | University of Padova |
| Luxembourg, Luxembourg | Luxembourg, Luxembourg | Padova, Italy |
| jordan.samhi@uni.lu | jacques.klein@uni.lu | eleonora.losiouk@unipd.it |
| Abstract | framework models, effectively reason about taint flows in Android |  |
| Taint analysis is a fundamental technique for detecting sensitive | apps? | In this paper, we investigate this question through a prelim- |
| data leaks in Android apps. However, traditional static tools, such as | inary study on the use of LLM-driven reasoning for Android taint |  |
| FlowDroid, still face well-known challenges due to the complexity | analysis. Instead of constructing explicit models of the Android |  |
| of accurately modeling the Android framework. In this paper, we in- | framework, we enable an LLM to iteratively explore decompiled |  |
| vestigate whether off-the-shelf Large Language Models (LLMs) can | apps and reason about potential data flows via a Model Context |  |
| effectively reason about taint flows in Android apps. Our prelim- | Protocol (MCP)-based toolchain. In this setting, the LLM acts as an |  |
| inary approach relies on an agentic interaction strategy, enabling | analysis agent, dynamically navigating code and forming hypothe- |  |
| the LLM to iteratively explore code and reason about data flows. | ses about source-to-sink relationships. Our goal is not to propose |  |
| We conduct an initial evaluation on the DroidBench benchmark | a production-ready taint analyzer, but to assess whether agentic |  |
| against FlowDroid, where our approach outperforms the baseline: | LLM reasoning can potentially complement traditional static taint |  |
| Gemini-3 Flash achieves an F1-score of 0.96, compared to 0.55 for | analysis approaches. To this end, we conduct an initial evaluation |  |
| FlowDroid. In particular, we observe improvements in challenging | on the DroidBench benchmark and a small set of real-world apps, |  |
| categories such as inter-component communication (0.95 vs. 0.17), | comparing against the state-of-the-art FlowDroid. |  |
| implicit flows (0.94 vs. 0.00), and reflection (1.00 vs. 0.50), where | Our findings provide early evidence that LLM-based reasoning |  |
| FlowDroid typically struggles. On a small set of real-world apps, the | can identify taint flows, often achieving higher recall in scenar- |  |
| LLM-based approach also identifies additional potential data leaks | ios involving complex behaviors (e.g., ICC, reflection, and implicit |  |
| not reported by FlowDroid. These preliminary findings suggest that | flows), while showing comparable performance in more standard |  |
| LLM reasoning may effectively complement traditional static taint | cases. This indicates that LLMs are particularly useful when tra- |  |
| analysis, motivating future research on hybrid LLM-enhanced taint | ditional modeling becomes difficult, but are not always necessary. |  |
| analysis pipelines. | Rather than applying LLMs indiscriminately, these findings point to |  |

as FlowDroid [5] have become widely adopted due to their ability

to perform precise, context-, flow-, and lifecycle-aware analysis of

Android apps. However, these approaches rely on carefully engi-

neered models of the Android framework and struggle with well-

known challenges, including reflection, dynamic code loading, inter-

component communication, and incomplete code [22, 29, 30, 38, 39].

In parallel, Large Language Models (LLMs) are increasingly being

adopted across a wide range of software engineering tasks, includ-

ing bug detection and fixing [6, 8, 14, 17], testing [7, 13, 21, 31],

vulnerability detection [12, 27, 34, 36, 40], and other applications [1,

15, 23, 26, 35, 41]. Their ability to understand and reason over both

natural and programming languages enables them to bridge gaps

traditionally filled by domain-specific models and heuristics.

a hybrid approach: traditional analyzers handle common cases effi-

ciently, while LLMs could be selectively applied to harder scenarios.

• We explore a novel perspective on Android taint analysis, inves-

in Android apps.

• We design an LLM-driven taint analysis approach that combines

decompiled code with MCP-enabled tool interaction.

• We provide a preliminary empirical study showing that LLM-

based reasoning can complement traditional analyzers such as

FlowDroid, particularly in challenging scenarios, motivating fur-

ther studies on hybrid taint analysis approaches combining static

analysis and agentic LLM reasoning.

2 Background

| 1 | Introduction | Such a design could improve overall effectiveness while also helping |
| --- | --- | --- |
| Taint analysis is a fundamental technique for detecting sensitive | balance computational cost and scalability. As future work, we plan |  |
| data leaks in Android applications (apps), enabling the identification | to explore this direction by designing more advanced hybrid analy- |  |
| of flows from privacy-critical sources (e.g., device identifiers, loca- | sis pipelines that integrate static analysis and LLM-based reasoning, |  |
| tion data, credentials) to potentially unsafe sinks such as network | as well as extending our evaluation to a larger set of real-world apps. |  |
| interfaces or logs. Over the past decade, static analysis tools such | Contributions. | This paper makes the following contributions: |

arXiv:2608.24269v1 [cs.SE] 25 Aug 2026 tigating whether LLM can effectively reason about taint flows

| As LLM capabilities continue to advance, a key question arises: | In this section, we briefly describe two concepts necessary to un- |
| --- | --- |
| Can an off-the-shelf LLM, without task-specific training or handcrafted | derstand the remainder of the paper. |

---

## Page 2

Taint Analysis for Android . Taint analysis tracks the flow of LLM Reasoning Flow

data from predefined sources to potentially dangerous sinks . In the

Android ecosystem, this task is complicated by the event-driven

high precision by modeling Android lifecycles and callbacks. While

effective on benchmarks, FlowDroid depends on manually main-

registered callbacks, or incomplete code. In this paper, we explore

whether LLMs can achieve comparable results without relying on

explicit framework modeling or task-specific training.

Model Context Protocol (MCP). LLMs usually operate in a closed

of complex artifacts such as full Android apps.

3 Experimental Setup

analysis capabilities (e.g., method retrieval, cross-references, and

class hierarchies) as MCP tools.

The analysis workflow proceeds as follows. First, the Android

APK is loaded into JADX for decompilation ① . The associated

JADX MCP server ② exposes APIs that allow the LLM to query and

navigate the recovered application structure (e.g., get_method_-

potential taint flows across components and languages. Finally, all

customized depending on the use case and available resources.

Implementation Details. For this project, we combine proprietary

2

2

Server

.so

4

Ghidra Ghidra MCP

Figure 1: Approach Overview

the accompanying repository.

Regarding the number of analyses (the 𝑁 parameter), we per-

formed 5 runs for open-source models and 3 for closed-source

models (due to API cost constraints) in the baseline evaluation (see

RQ1 and RQ2), and 5 for real-world apps assessment (see RQ3).

Section 6.

4 Experimental Results

In this section, we present the results of our preliminary evaluation,

structured around the following research questions (RQs):

the aggregated results.

| execution model, component lifecycles, inter-component commu- | 1 | JADX | JADX MCP |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nication (ICC), and extensive framework APIs. FlowDroid [5] is | 5 | 6 |  |  |  |  |  |  |  |
| a widely used static taint analysis tool for Android that achieves | Android App | 3 | LLM | Detected Flows |  |  |  |  |  |
| tained models and may miss flows involving reflection, dynamically | Server |  |  |  |  |  |  |  |  |
| setting and cannot directly interact with external tools or program | in both cases. This choice addresses the two main deployment sce- |  |  |  |  |  |  |  |  |
| representations. MCP (Model Context Protocol) [3] is an open stan- | narios, covering both convenience-oriented closed-source services |  |  |  |  |  |  |  |  |
| dard that enables LLMs to interact with external tools and data | and self-hosted solutions for cost containment and confidentiality. |  |  |  |  |  |  |  |  |
| sources through a unified interface, allowing models to query, nav- | For proprietary models, we use | Gemini 3 Flash | [11], while for the |  |  |  |  |  |  |
| igate, and reason over structured information. In practice, MCP | open-source model we select | Qwen3.5-27B | [28]. We orchestrate |  |  |  |  |  |  |
| exposes external capabilities as callable tools that the LLM can | these models through | Claude Code | [4] and | Gemini CLI | [10]. Ad- |  |  |  |  |
| invoke during its reasoning process, enabling iterative exploration | ditional implementation details and configurations are available in |  |  |  |  |  |  |  |  |
| In this section, we present our approach and implementation details. | Comparison with FlowDroid. | The LLM-based approach and |  |  |  |  |  |  |  |
| Approach Overview. | Figure 1 presents an overview of our ap- | FlowDroid are executed independently. During the analysis process, |  |  |  |  |  |  |  |
| proach. The core idea is to use an LLM as an analysis agent that | the LLM does not receive any information derived from FlowDroid |  |  |  |  |  |  |  |  |
| interacts with MCP-enabled reverse-engineering tools to explore | outputs, detected flows, or taint specifications. For the comparison, |  |  |  |  |  |  |  |  |
| Android apps and reason about potential taint flows. Rather than | we run FlowDroid using its default configuration, including its de- |  |  |  |  |  |  |  |  |
| relying on manually engineered Android framework models, the | fault source/sink definitions, which are available on their repo [33]. |  |  |  |  |  |  |  |  |
| LLM dynamically navigates the codebase to infer source-to-sink | We intentionally adopt this default setup to reflect a common us- |  |  |  |  |  |  |  |  |
| relationships. To support this process, we rely on | JADX-MCP | [25] | age scenario in which FlowDroid is employed as a black-box taint |  |  |  |  |  |  |
| and | Ghidra-MCP | [16], which expose decompilation and program- | analysis tool. We further discuss this choice and its implications in |  |  |  |  |  |  |
| by_name() | ). If the app contains native libraries, the extracted | .so | • | RQ1: | How does the LLM-based taint analysis approach compare |  |  |  |  |
| binary is loaded into Ghidra for analysis | ③ | . Through the Ghidra | to FlowDroid on DroidBench? |  |  |  |  |  |  |
| MCP server | ④ | , the LLM can similarly inspect native functions, refer- | • | RQ2: | How does the LLM-based approach perform across the |  |  |  |  |
| ences, and low-level program structures. Using these MCP-enabled | different categories of DroidBench compared to FlowDroid? |  |  |  |  |  |  |  |  |
| tools, the LLM iteratively explores the application codebase | ⑤ | , | • | RQ3: | How does the LLM-based approach perform when applied |  |  |  |  |
| traces the propagation of sensitive information, and reasons about | to real-world Android applications? |  |  |  |  |  |  |  |  |
| identified flows are collected and serialized into a structured JSON | 4.1 | RQ1: Overall Performance on DroidBench |  |  |  |  |  |  |  |
| report | ⑥ | . The full prompts used in our experiments are available | To answer RQ1, we compare our LLM-based approach against Flow- |  |  |  |  |  |  |
| in our repository. | Droid on DroidBench [5], which is a widely used benchmark for |  |  |  |  |  |  |  |  |
| To counter the non-determinism of LLMs, which can produce | Android taint analysis, consisting (in version 3.0) of 190 test cases |  |  |  |  |  |  |  |  |
| hallucinations and spurious outputs, each app is analyzed | 𝑁 | times | across 19 categories, covering challenges such as lifecycle modeling, |  |  |  |  |  |  |
| using the same prompt, and a detected flow is considered valid only | asynchronous callbacks, and UI interactions | 1 | . We evaluate preci- |  |  |  |  |  |  |
| if it appears in at least | ⌊ | 𝑁 | / | 2 | ⌋ + | 1 analyses. The value of | 𝑁 | can be | sion, recall, and F1-score against the ground truth. Table 1 reports |
| models with locally hosted open-source models, using agentic CLIs | 1 | Inter-App Communication excluded since neither approach supports it. |  |  |  |  |  |  |  |

---

## Page 3

Table 1: Overall performance on DroidBench. while others remain less effective. In particular, substantial improve-

Gemini-3 Qwen3.5

| Metric | FlowDroid |
| --- | --- |
| Flash | 27B |

with an F1-score of 0.96, substantially improving over the Flow-

Droid baseline. This gain is primarily driven by a large increase in re-

improve taint-flow detection on DroidBench, especially by reduc-

4.2 RQ2: DroidBench Categories

To answer RQ2, we further analyze the evaluation results from RQ1

by disaggregating them across the benchmark categories defined

in DroidBench. The detailed definitions of these categories are

available on the official DroidBench GitHub page [32]. Table 2

reports the corresponding F1-scores for each category.

Table 2: Category-wise performance (F1) on DroidBench.

Gemini-3 Qwen3.5

| Flash | 27B |  |  |
| --- | --- | --- | --- |
| ArraysAndLists | 0.67 | 1.00 | 1.00 |
| Callbacks | 0.50 | 0.98 | 0.83 |
| ImplicitFlows | 0.00 | 0.94 | 0.22 |
| ICC | 0.17 | 0.95 | 0.97 |
| Lifecycle | 0.74 | 1.00 | 1.00 |
| Native | 0.00 | 1.00 | 1.00 |
| Reflection_CC | 0.00 | 1.00 | 0.96 |
| SelfModification | 0.00 | 0.86 | 0.00 |
| Threading | 1.00 | 1.00 | 1.00 |

3

ments are observed in categories such as InterComponentCommuni-

cation (ICC), ImplicitFlows , Reflection , and Native , where FlowDroid

exhibits limited or no recall. These categories are known to be par-

approaches can better reason about these complex behaviors by

leveraging semantic understanding of decompiled code, enabling

further discussed in Section 5.

real-world taint flows, we analyzed 5 apps randomly selected from

AndroZoo [2], drawn from Google Play within the last 5 years. We

deliberately limit the sample size to enable thorough manual inspec-

tion of each reported flow, which is necessary to assess its validity.

Accordingly, our goal is not statistical generalization, but a qualita-

tive, first assessment of whether LLM-based reasoning can uncover

additional real data leaks beyond those detected by FlowDroid.

As discussed in Section 3, our baseline comparison uses the

default FlowDroid configuration, whose default source/sink defi-

nitions are sufficient for DroidBench. However, for the real-world

app evaluation, we also extended FlowDroid’s source/sink defini-

approach. This was done to ensure a fair comparison, preventing

presents a Venn diagram illustrating the overlap between the taint

RQ2, i.e., Gemini 3 Flash.

Flash 3

| Precision | 0.83 | 0.96 | 0.87 | ticularly challenging for traditional static analysis due to complex |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Recall | 0.42 | 0.95 | 0.89 | control flow, dynamic dispatch, incomplete framework modeling, |  |  |  |  |
| F1-score | 0.55 | 0.96 | 0.88 | and native code boundaries. The results suggest that LLM-based |  |  |  |  |
| FlowDroid achieves an F1-score of 0.55, reflecting its conserva- | the identification of taint propagation patterns that are missed by |  |  |  |  |  |  |  |
| tive analysis strategy and relatively low recall (0.42). While its pre- | the baseline. At the same time, categories such as | DynamicLoading |  |  |  |  |  |  |
| cision remains high (0.83), it fails to detect a substantial portion of | remain challenging for both traditional and LLM-based approaches, |  |  |  |  |  |  |  |
| known taint flows, leading to many false negatives. In contrast, our | while others exhibit similar performance. Overall, the category- |  |  |  |  |  |  |  |
| LLM-based approach outperforms FlowDroid in terms of F1-score. | level analysis suggests that LLMs are particularly promising as a |  |  |  |  |  |  |  |
| In particular, Gemini-3 Flash achieves the best overall performance | complementary technique for challenging analysis scenarios, as |  |  |  |  |  |  |  |
| call (up to 0.95), while maintaining competitive precision. Qwen3.5- | Answer to RQ2: | LLM-based approaches outperform Flow- |  |  |  |  |  |  |
| 27B also improves over FlowDroid, reaching an F1-score of 0.88. | Droid in most DroidBench categories, particularly those |  |  |  |  |  |  |  |
| Overall, these results provide preliminary evidence that LLMs can | involving ICC, implicit flows, reflection, and native code. |  |  |  |  |  |  |  |
| ing false negatives, which we further analyze in RQ2 (Section 4.2). | 4.3 | RQ3: Performance on Real-world Apps |  |  |  |  |  |  |
| Answer to RQ1: | LLM-based taint analysis can outperform | To answer RQ3, we evaluate both FlowDroid and our LLM-based |  |  |  |  |  |  |
| FlowDroid on DroidBench, primarily due to substantially | approach on a small set of real-world Android apps. Given the ex- |  |  |  |  |  |  |  |
| higher recall. | ploratory nature of this study and the absence of ground truth for |  |  |  |  |  |  |  |
| Category | FlowDroid | tions to include all sources and sinks identified by the LLM-based |  |  |  |  |  |  |
| Aliasing | 0.50 | 0.67 | 0.50 | FlowDroid from missing flows solely because the corresponding |  |  |  |  |
| AndroidSpecific | 0.67 | 0.92 | 0.80 | sources or sinks were absent from its default configuration. Figure 2 |  |  |  |  |
| DynamicLoading | 0.50 | 0.00 | 0.00 | flows detected by FlowDroid and those identified by our approach. |  |  |  |  |
| EmulatorDetection | 0.94 | 1.00 | 1.00 | Due to the cost and computational overhead of manually validating |  |  |  |  |
| FieldAndObject Sensitivity | 1.00 | 1.00 | 1.00 | flows across multiple runs, we conduct the real-world evaluation |  |  |  |  |
| GeneralJava | 0.47 | 0.98 | 0.90 | only with the best-performing LLM configuration from RQ1 and |  |  |  |  |
| Reflection | 0.50 | 1.00 | 1.00 | FlowDroid | 19 | 2 | 17 | Gemini |
| UnreachableCode | 0.00 | 0.00 | 0.00 | Figure 2: Overlap between FlowDroid and Gemini 3 Flash. |  |  |  |  |
| As already observed in RQ1, the effectiveness of LLM-based | Unlike DroidBench, real-world apps do not provide ground truth |  |  |  |  |  |  |  |
| taint analysis varies significantly across models, with some models | for all taint flows, making recall extremely challenging to compute |  |  |  |  |  |  |  |
| outperforming FlowDroid across several DroidBench categories, | without exhaustive manual reverse engineering of the entire apps. |  |  |  |  |  |  |  |

---

## Page 4

| Therefore, we focus on the 17 additional flows reported by the | struggle. However, they may be unnecessary or overly expensive |  |  |
| --- | --- | --- | --- |
| LLM-based approach (i.e., the light blue region in Figure 2). We | for simpler taint propagation cases. Therefore, one potential di- |  |  |
| do not assume that all flows reported by FlowDroid are true pos- | rection could be hybrid approaches in which traditional analyzers |  |  |
| itives; however, our objective is to evaluate the ability of the LLM- | handle common cases, while LLMs are selectively applied only to |  |  |
| based approach to identify previously undetected flows beyond | more challenging analysis scenarios. |  |  |
| those already reported by the baseline analyzer. Two annotators | ❸ | Challenges in evaluation. | While benchmarks such as Droid- |
| with expertise in Android taint analysis independently inspected | Bench provide ground truth, evaluating taint analysis on real-world |  |  |
| these flows by manually reverse-engineering the apps to determine | apps remains challenging due to the lack of labeled datasets and |  |  |
| whether each corresponded to a true or false positive. In cases of | the need for expensive manual validation. |  |  |
| disagreement, the annotators discussed their findings until reaching | Research Agenda. | This work represents a preliminary step to- |  |
| a consensus. It is important to note that our goal is not to assess | wards understanding the role of LLMs in taint analysis. We outline |  |  |
| whether the flows are malicious (which is beyond the scope of this | the following directions for future work: |  |  |
| paper), but rather to determine whether the reported source-to-sink | • | Hybrid and explainable analysis. | We plan to investigate hy- |
| flows actually exist in the analyzed apps. Our analysis reveals that | brid pipelines combining static analysis and LLM-based reason- |  |  |
| 16 out of the 17 additional flows correspond to true positives, while | ing, where LLMs are selectively triggered only for challenging |  |  |
| one was revealed to be a hallucination from the LLM. These find- | scenarios. In addition, we aim to improve the explainability of |  |  |
| ings indicate that LLM-based approaches can uncover previously | detected taint flows for human analysts and developers. |  |  |
| undetected data leaks in real-world apps, thereby complementing | • | Larger-scale evaluation. | We aim to extend the evaluation to |
| traditional static analysis tools. For example, in one analyzed app, | a broader set of real-world apps, additional LLMs, and more |  |  |
| the source method itself is retrieved via reflection. In this scenario, | advanced prompting strategies to better assess robustness and |  |  |
| FlowDroid cannot even start the corresponding taint analysis, since | generalizability. |  |  |
| the reflective invocation prevents the source method from being | • | Cost-aware analysis. | We plan to systematically study the trade- |
| resolved during the source lookup phase. In contrast, the LLM- | offs between effectiveness, scalability, and computational cost, |  |  |
| based approach can still reason about the flow through iterative | including strategies for selectively invoking stronger LLMs only |  |  |
| code exploration. At the same time, the LLM-based approach also | for challenging analysis scenarios. |  |  |

misses several flows detected by FlowDroid, highlighting that the

two approaches capture partially different classes of taint flows.

6 Limitations

This observation motivates further investigation with a specific

| focus on hybrid approaches that combine traditional static analysis | In this section, we discuss the main limitations of our study. |  |
| --- | --- | --- |
| with LLM-based reasoning, as discussed in Section 5. | LLM-related limitations. | Our approach inherits well-known lim- |
| Considerations on Non-determinism. | To mitigate non- deter- | itations of LLMs, including hallucinations and non-deterministic |
| minism, flows are retained only if reported in the majority of runs | behavior. These aspects may lead to spurious taint flows or incon- |  |
| (see Section 3). Manual inspection nevertheless revealed additional | sistent results across runs, making the analysis harder to reproduce |  |
| true positives below this threshold, suggesting that increasing the | and less reliable in security-critical settings. To partially mitigate |  |
| number of runs may further improve coverage and uncover addi- | this issue, we execute each prompt multiple times and retain only |  |
| tional valid taint flows. | the flows that appear in the majority of the runs (see Section 3). |  |

Baseline comparison. In this preliminary study, we intentionally

| Answer to RQ3: | The LLM-based approach is able to identify | compare against the default configuration of FlowDroid to reflect |
| --- | --- | --- |
| additional true data leaks in real-world apps beyond those | a common usage scenario in which the tool is employed as a black- |  |
| detected by FlowDroid, although challenges remain in terms | box taint analyzer. While the literature proposes several extensions |  |
| of reliability, evaluation, and completeness. | targeting specific challenges (e.g., IccTA [18] for ICC analysis), such |  |

approaches typically require additional configuration or integration

effort beyond the default FlowDroid setup. Investigating whether

| 5 | Discussion and Research Agenda | LLM-enhanced taint analysis approaches can address similar chal- |  |
| --- | --- | --- | --- |
| Several important considerations arise from our results: | lenges, while maintaining scalability and usability, represents an |  |  |
| ❶ | LLMs without framework modeling. | Our results suggest that | interesting direction for future work. |

LLMs can reason about Android taint flows without any explicit

| training or handcrafted knowledge about the Android framework. | 7 | Related Work |  |
| --- | --- | --- | --- |
| Despite this, it is still able to identify non-trivial taint flows. This | Recent work has explored the LLMs adoption for taint analysis. |  |  |
| suggests that LLMs can potentially lower the engineering effort typ- | LATTE [20] employs LLMs for static binary taint analysis and vul- |  |  |
| ically required by traditional static analyzers. At the same time, the | nerability detection in compiled code. Other works [9, 19] use LLMs |  |  |
| effectiveness of the approach strongly depends on the underlying | to enhance traditional pipelines by improving taint specifications |  |  |
| LLM, potentially introducing trade-offs between analysis quality, | or assisting vulnerability reasoning. Similarly, J. Ye tal. [37] applies |  |  |
| scalability, and computational cost. | LLM-based taint reasoning to embedded firmware analysis. How- |  |  |
| ❷ | Complementarity with traditional analysis. | LLMs appear | ever, these approaches do not target Android apps and/or mainly |
| particularly effective in challenging scenarios such as ICC, implicit | use LLMs as auxiliary steps within existing pipelines, rather than |  |  |
| flows, reflection, and native code, where traditional analyzers often | investigating LLM-based reasoning. Beyond taint analysis, several |  |  |

4

---

## Page 5

| recent works have explored leveraging LLMs for Android security | [8] | Sidong Feng and Chunyang Chen. 2024. Prompting is all you need: Automated |
| --- | --- | --- |
| tasks, including malware and vulnerability detection [24, 27, 40]. | android bug replay with large language models. In | Proceedings of the 46th |

IEEE/ACM International Conference on Software Engineering . 1–13.

In contrast, our work explores the use of LLMs to directly reason [9] Jonah Ghebremichael, Saastha Vasan, Saad Ullah, Greg Tystahl, David Adei,

about end-to-end taint flows in Android apps. Christopher Kruegel, Giovanni Vigna, William Enck, and Alexandros Kapravelos.

2026. Multi-Agent Taint Specification Extraction for Vulnerability Detection.

arXiv preprint arXiv:2601.10865 (2026).

8 Conclusion [10] Google. 2026. Gemini CLI. https://github.com/google-gemini/gemini-cli.

Accessed: 2026-04-27.

| This paper presents a preliminary empirical study on the use of | [11] | Google | DeepMind. | 2026. | Gemini | 3 | – | Google | DeepMind. | https: |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LLM reasoning for Android taint analysis. Compared to FlowDroid | //deepmind.google/technologies/gemini/. Accessed: 2026-04-27. |  |  |  |  |  |  |  |  |  |
| on DroidBench, our approach achieves promising results, with | [12] | Yuejun Guo, Constantinos Patsakis, Qiang Hu, Qiang Tang, and Fran Casino. 2024. |  |  |  |  |  |  |  |  |

Outside the comfort zone: Analysing llm capabilities in software vulnerability de-

| Gemini-3 Flash reaching an F1-score of 0.96 (vs. 0.55 for FlowDroid). | tection. In | European symposium on research in computer security | . Springer, 271–289. |
| --- | --- | --- | --- |
| In particular, the results suggest that LLM-based reasoning can help | [13] | Yuchao Huang, Junjie Wang, Zhe Liu, Yawen Wang, Song Wang, Chunyang Chen, |  |
| identify challenging taint flows involving ICC, reflection, and im- | Yuanzhe Hu, and Qing Wang. 2024. Crashtranslator: Automatically reproducing |  |  |

mobile application crashes directly from stack trace. In Proceedings of the 46th

| plicit flows. Rather than replacing traditional static analyzers, LLMs | ieee/acm international conference on software engineering | . 1–13. |
| --- | --- | --- |
| appear promising as a complementary technique for difficult anal- | [14] | Sungmin Kang, Juyeon Yoon, and Shin Yoo. 2023. Large language models are |

few-shot testers: Exploring llm-based general bug reproduction. In 2023 IEEE/ACM

| ysis scenarios. Overall, this work provides preliminary evidence to | 45th International Conference on Software Engineering (ICSE) | . IEEE, 2312–2323. |
| --- | --- | --- |
| further support research on hybrid taint analysis approaches that | [15] | Avishree Khare, Saikat Dutta, Ziyang Li, Alaia Solko-Breslin, Rajeev Alur, and |
| combine static analysis with agentic LLM reasoning. | Mayur Naik. 2023. Understanding the effectiveness of large language models |  |

in detecting security vulnerabilities. arXiv preprint arXiv:2311.16169 (2023).

[16] LaurieWired. 2025. GhidraMCP: Model Context Protocol Server for Ghidra.

Data Availability. https://github.com/LaurieWired/GhidraMCP. Accessed: 2026-04-27.

[17] Haonan Li, Yu Hao, Yizhuo Zhai, and Zhiyun Qian. 2024. Enhancing static

| We publicly release all associated resources: | analysis for practical bug detection: An llm-integrated approach. | Proceedings |
| --- | --- | --- |
| https://github.com/nmiazzomath/Towards-LLM-Enhanced- | of the ACM on Programming Languages | 8, OOPSLA1 (2024), 474–499. |

[18] Li Li, Alexandre Bartel, Tegawendé F Bissyandé, Jacques Klein, Yves Le Traon,

Android-Taint-Analysis Steven Arzt, Siegfried Rasthofer, Eric Bodden, Damien Octeau, and Patrick

McDaniel. 2015. Iccta: Detecting inter-component privacy leaks in android apps.

Acknowledgements In 2015 IEEE/ACM 37th IEEE International Conference on Software Engineering ,

Vol. 1. IEEE, 280–291.

LLM usage considerations : ChatGPT 2 , Claude 3 and GitHub Copi- [19] Ziyang Li, Saikat Dutta, and Mayur Naik. 2024. IRIS: LLM-assisted static analysis

lot 4 were used for editorial purposes and for generating source code for detecting security vulnerabilities. arXiv preprint arXiv:2405.17238 (2024).

[20] Puzhuo Liu, Chengnian Sun, Yaowen Zheng, Xuan Feng, Chuan Qin, Yuncheng

for artifact creation in this work, and all outputs were inspected Wang, Zhenyang Xu, Zhi Li, Peng Di, Yu Jiang, et al. 2025. Llm-powered static

by the authors to ensure accuracy and originality. LLMs are also binary taint analysis. ACM Transactions on Software Engineering and Methodology

34, 3 (2025), 1–36.

| an integral component of our experimental methodology. Because | [21] | Zhe Liu, Chunyang Chen, Junjie Wang, Mengzhuo Chen, Boyu Wu, Xing Che, Dan- |  |
| --- | --- | --- | --- |
| the primary model employed ( | Gemini 3 Flash | ) is closed-source, | dan Wang, and Qing Wang. 2024. Make llm a testing expert: Bringing human-like |
| exact reproduction of our results may vary over time. To mitigate | interaction to mobile gui testing via functionality-aware decisions. In | Proceedings |  |

of the IEEE/ACM 46th International Conference on Software Engineering . 1–13.

this concern, we additionally evaluated an open-source LLM and [22] Linghui Luo, Felix Pauck, Goran Piskachev, Manuel Benz, Ivan Pashchenko,

report their comparative performance. Martin Mory, Eric Bodden, Ben Hermann, and Fabio Massacci. 2022. TaintBench:

Automatic real-world malware benchmarking of Android taint analyses.

Empirical Software Engineering 27, 1 (2022), 16.

| References | [23] | Wei Ma, Shangqing Liu, Zhihao Lin, Wenhan Wang, Qiang Hu, Ye Liu, Cen Zhang, |  |  |  |
| --- | --- | --- | --- | --- | --- |
| [1] | Marco Alecci, Nicolas Sannier, Marcello Ceci, Sallam Abualhaija, Jordan Samhi, | Liming Nie, Li Li, and Yang Liu. 2023. LMs: Understanding Code Syntax and |  |  |  |
| Domenico Bianculli, Tegawendé François d Assise BISSYANDE, and Jacques | Semantics for Code Analysis. | arXiv preprint arXiv:2305.12138 | (2023). |  |  |
| Klein. 2025. Toward LLM-Driven GDPR Compliance Checking for Android Apps. | [24] | Noble Saji Mathews, Yelizaveta Brus, Yousra Aafer, Meiyappan Nagappan, |  |  |  |
| In | 33rd ACM International Conference on the Foundations of Software Engineering | and Shane McIntosh. 2024. Llbezpeky: Leveraging large language models for |  |  |  |
| (FSE Companion’25) | . | vulnerability detection. | arXiv preprint arXiv:2401.01269 | (2024). |  |
| [2] | Kevin Allix, Tegawendé F. Bissyandé, Jacques Klein, and Yves Le Traon. 2016. | [25] | Aman Mehta. 2025. | JADX-MCP: Model Context Protocol Server for JADX. |  |
| AndroZoo: Collecting Millions of Android Apps for the Research Commu- | https://github.com/zinja-coder/jadx-ai-mcp. Accessed: 2026-04-27. |  |  |  |  |
| nity. In | Proceedings of the 13th International Conference on Mining Software | [26] | Kexin Pei, David Bieber, Kensen Shi, Charles Sutton, and Pengcheng Yin. 2023. |  |  |
| Repositories | (Austin, Texas) | (MSR ’16) | . ACM, New York, NY, USA, 468–471. | Can large language models reason about program invariants?. In | International |
| doi:10.1145/2901739.2903508 | Conference on Machine Learning | . PMLR, 27496–27520. |  |  |  |
| [3] | Anthropic. 2024. | Model Context Protocol. | https://modelcontextprotocol.io. | [27] | Xingzhi Qian, Xinran Zheng, Yiling He, Shuo Yang, and Lorenzo Cavallaro. 2025. |
| Accessed: 2026-04-27. | LAMD: Context-driven Android Malware Detection and Classification with |  |  |  |  |
| [4] | Anthropic. 2026. Claude Code by Anthropic \| AI Coding Agent, Terminal, IDE. | LLMs. | arXiv preprint arXiv:2502.13055 | (2025). |  |
| https://claude.com/product/claude-code. Accessed: 2026-04-27. | [28] | Qwen Team, Alibaba Group. 2026. Qwen3.5: Towards Native Multimodal Agents. |  |  |  |
| [5] | Steven Arzt, Siegfried Rasthofer, Christian Fritz, Eric Bodden, Alexandre Bartel, | https://qwen.ai/blog?id=qwen3.5. Accessed: 2026-04-27. |  |  |  |
| Jacques Klein, Yves Le Traon, Damien Octeau, and Patrick McDaniel. 2014. | [29] | Jordan Samhi, René Just, Tegawendé F Bissyandé, Michael D Ernst, and Jacques |  |  |  |
| Flowdroid: Precise context, flow, field, object-sensitive and lifecycle-aware taint | Klein. 2024. Call graph soundness in android static analysis. In | Proceedings of |  |  |  |
| analysis for android apps. | ACM sigplan notices | 49, 6 (2014), 259–269. | the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis | . |  |
| [6] | Islem Bouzenia, Premkumar Devanbu, and Michael Pradel. 2024. Repairagent: An | 945–957. |  |  |  |
| autonomous, llm-based agent for program repair. | arXiv preprint arXiv:2403.17134 | [30] | Jordan Samhi, Marc Miltenberger, Marco Alecci, Steven Arzt, Tegawendé |  |  |
| (2024). | Bissyandé, and Jacques Klein. 2025. Do you have 5 min? Improving Call Graph |  |  |  |  |
| [7] | Yinghao Chen, Zehao Hu, Chen Zhi, Junxiao Han, Shuiguang Deng, and Jianwei | Analysis with Runtime Information. In | Proceedings of the 33rd ACM International |  |  |
| Yin. 2024. Chatunitest: A framework for llm-based test generation. In | Companion | Conference on the Foundations of Software Engineering | . 540–544. |  |  |
| Proceedings of the 32nd ACM International Conference on the Foundations of | [31] | Max Schäfer, Sarah Nadi, Aryaz Eghbali, and Frank Tip. 2023. | An empirical |  |  |
| Software Engineering | . 572–576. | evaluation of using large language models for automated unit test generation. |  |  |  |

IEEE Transactions on Software Engineering 50, 1 (2023), 85–105.

| 2 | https://chatgpt.com/ | [32] | Secure Software Engineering Group. 2026. DroidBench: A Micro-Benchmark |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | https://claude.ai/ | Suite | for | Android | Taint | Analysis. | https://github.com/secure-software- |
| 4 | https://github.com/features/copilot | engineering/DroidBench. Accessed: 2026-05-08. |  |  |  |  |  |

5

---

## Page 6

| [33] | Secure Software Engineering Group. 2026. | FlowDroid: Static Data Flow | [37] | Junjian Ye, Xincheng Fei, Xavier de Carné de Carnavalet, Lianying Zhao, Lifa |
| --- | --- | --- | --- | --- |
| Tracker. https://github.com/secure-software-engineering/FlowDroid. Accessed: | Wu, and Mengyuan Zhang. 2024. Detecting command injection vulnerabilities |  |  |  |
| 2026-05-08. | in Linux-based embedded firmware with LLM-based taint analysis of library |  |  |  |
| [34] | Tiezhu Sun, Marco Alecci, Yewei Song, Xunzhu Tang, Kisub Kim, Jordan | functions. | Computers & Security | 144 (2024), 103971. |
| Samhi, Tegawendé F Bissyandé, and Jacques Klein. 2025. | RAML: Toward | [38] | Junbin Zhang, Yingying Wang, Lina Qiu, and Julia Rubin. 2021. Analyzing android |  |
| Retrieval-Augmented Localization of Malicious Payloads in Android Apps. In | taint analysis tools: FlowDroid, Amandroid, and DroidSafe. | IEEE Transactions |  |  |
| 2025 40th IEEE/ACM International Conference on Automated Software Engineering | on Software Engineering | 48, 10 (2021), 4014–4040. |  |  |
| (ASE) | . IEEE, 3963–3967. | [39] | Xueling Zhang, Xiaoyin Wang, Rocky Slavin, and Jianwei Niu. 2021. Condysta: |  |
| [35] | Weisong Sun, Chunrong Fang, Yudu You, Yun Miao, Yi Liu, Yuekang Li, Gelei Deng, | Context-aware dynamic supplement to static taint analysis. In | 2021 IEEE |  |
| Shenghan Huang, Yuchen Chen, Quanjun Zhang, et al. 2023. Automatic code sum- | Symposium on Security and Privacy (SP) | . IEEE, 796–812. |  |  |
| marization via chatgpt: How far are we? | arXiv preprint arXiv:2305.12865 | (2023). | [40] | Wenxiang Zhao, Juntao Wu, and Zhaoyi Meng. 2025. Apppoet: Large language |
| [36] | Yuqiang Sun, Daoyuan Wu, Yue Xue, Han Liu, Haijun Wang, Zhengzi Xu, | model based android malware detection via multi-view prompt engineering. |  |  |
| Xiaofei Xie, and Yang Liu. 2024. | Gptscan: Detecting logic vulnerabilities in | Expert Systems with Applications | 262 (2025), 125546. |  |
| smart contracts by combining gpt with program analysis. In | Proceedings of the | [41] | Li Zhong and Zilong Wang. 2024. Can llm replace stack overflow? a study on |  |
| IEEE/ACM 46th International Conference on Software Engineering | . 1–13. | robustness and reliability of large language model code generation. In | Proceedings |  |

of the AAAI Conference on Artificial Intelligence , Vol. 38. 21841–21849.

6

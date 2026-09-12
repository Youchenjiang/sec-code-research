---
title: "TitanCA: Lessons from Orchestrating LLM Agents to Discover 100+ CVEs"
author: "Ting Zhang; Yikun Li; Chengran Yang; Ratnadira Widyasari; Yue Liu; Ngoc Tan Bui; Phuc Thanh Nguyen; Yan Naing Tun; Ivana Clairine Irsan; Huu Hung Nguyen; Huihui Huang; Jinfeng Jiang; Lwin Khin Shar; Eng Lieh Ouh; David Lo; Hong Jin Kang; Yide Yin; Wen Bin Leow"
creator: "arXiv GenPDF (tex2pdf:4af3385)"
pages: 8
---

# TitanCA: Lessons from Orchestrating LLM Agents to Discover 100+ CVEs

> **作者**：Ting Zhang; Yikun Li; Chengran Yang; Ratnadira Widyasari; Yue Liu; Ngoc Tan Bui; Phuc Thanh Nguyen; Yan Naing Tun; Ivana Clairine Irsan; Huu Hung Nguyen; Huihui Huang; Jinfeng Jiang; Lwin Khin Shar; Eng Lieh Ouh; David Lo; Hong Jin Kang; Yide Yin; Wen Bin Leow
> **總頁數**：8 頁

---

## Page 1

TitanCA project

TitanCA: Lessons from

Orchestrating LLM

Agents to Discover 100+

CVEs

| Ting Zhang | Hong Jin Kang |
| --- | --- |
| Monash University | The University of Sydney |
| Yikun Li, Chengran Yang, Ratnadira | Yide Yin, Wen Bin Leow |
| Widyasari, Yue Liu, Ngoc Tan Bui, Phuc | GovTech, Singapore |

Thanh Nguyen, Yan Naing Tun, Ivana Clairine

Irsan, Huu Hung Nguyen, Huihui Huang,

Jinfeng Jiang, Lwin Khin Shar, Eng Lieh Ouh,

David Lo

Singapore Management University

Abstract —Software vulnerabilities remain one of the most persistent threats to modern digital

infrastructure. While static application security testing (SAST) tools have long served as the first line

of defense, they suffer from high false-positive rates. This article presents TitanCA, a collaborative

project between Singapore Management University and GovTech Singapore that orchestrates multiple

large language model (LLM)-powered agents into a unified vulnerability discovery pipeline. Applied in

open-source software, TitanCA has discovered 203 confirmed zero-day vulnerabilities and yielded 118

CVEs. We describe the four-module architecture, i.e., matching, filtering, inspection, and adaptation,

and share key lessons from building and deploying an LLM-based vulnerability discovery solution in

arXiv:2604.17860v3 [cs.CR] 24 Aug 2026

practice.

| T | his article offers a synthesis of the studies un- | papers where available. The discovery of software |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| derpinning TitanCA [1], [2], [3], [4], [5] along with | vulnerabilities before they can be exploited is a central |  |  |  |  |  |  |
| our opinions, presented at an accessible level with | challenge in cybersecurity. Despite decades of research |  |  |  |  |  |  |
| full | technical | detail | deferred | to | the | corresponding | in static analysis, fuzzing, and formal verification, the |

volume and complexity of modern codebases continue

| Digital Object Identifier 10.1109/MCE.YYYY.Doi Number | to outpace traditional detection methods. Popular static |
| --- | --- |
| Date of publication DD MM YYYY; date of current version DD | application security testing (SAST) tools, while widely |

MM YYYY

xxx/xxx YYYY Published by the IEEE Security & Privacy 2162-2248 © YYYY IEEE

1

---

## Page 2

TitanCA

| adopted in continuous integration and continuous de- | How TitanCA works |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ployment (CI/CD) pipelines, produce substantial num- | TitanCA | implements | a | just-in-time | (JIT) |  |  |
| bers of false positives that hurt developer trust and | vulnerability-discovery | approach | that | analyzes |  |  |  |
| consume triage resources. The consequence is that | code as it is committed, rather than during periodic |  |  |  |  |  |  |
| developers begin ignoring security warnings entirely, | audits. When a developer pushes a commit to the |  |  |  |  |  |  |
| leaving many vulnerabilities untriaged. | platform, the system extracts the changed code and |  |  |  |  |  |  |
| Recent advances in large language models (LLMs) | passes | it | through | a | four-module | pipeline. | These |
| have opened new avenues for automated code under- | modules are designed to complement one another, |  |  |  |  |  |  |
| standing. Models trained on billions of lines of source | creating a layered defense that prioritizes precision |  |  |  |  |  |  |
| code can reason about code semantics and identify | while also maintaining recall. Figure 1 shows the |  |  |  |  |  |  |
| vulnerable patterns that rule-based analyzers miss. Yet | overview of the TitanCA pipeline. |  |  |  |  |  |  |

applying LLMs to vulnerability detection in a new

| production environment introduces its own challenges: | Module 1: The Matcher (VulCoCo) |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| individual models are prone to hallucination, precision | The first module performs vulnerable clone detec- |  |  |  |  |  |
| matters more than recall when developer attention is | tion. VulCoCo [1] generates embeddings of the candi- |  |  |  |  |  |
| scarce, and general-purpose models lack awareness of | date functions and compares them against a curated |  |  |  |  |  |
| the vulnerability patterns specific to a given deploy- | database of known vulnerable functions. Our main |  |  |  |  |  |
| ment context. | sources are the NVD and the TitanVul dataset [4], |  |  |  |  |  |
| TitanCA addresses these challenges through or- | which | contains | approximately | 40,000 | vulnerability |  |
| chestration rather than by scaling models. Rather than | samples spanning diverse languages and vulnerability |  |  |  |  |  |
| relying on a single model, the system composes multi- | types. The module uses similarity search over a vector |  |  |  |  |  |
| ple LLM-powered agents into a four-module pipeline | database to identify candidate matches, then employs |  |  |  |  |  |
| in which each stage refines the output of the pre- | an LLM as a semantic validator to confirm whether |  |  |  |  |  |
| vious one, progressively filtering false positives and | the detected similarity reflects a genuine vulnerability |  |  |  |  |  |
| increasing confidence in the findings. The final module | pattern rather than a superficial syntactic resemblance. |  |  |  |  |  |
| incorporates domain knowledge drawn from the target | If the candidate function is flagged as vulnerable, we |  |  |  |  |  |
| organization to capture patterns that generic models | skip the remaining modules; otherwise, the function |  |  |  |  |  |
| overlook. | flows to the following modules. This initial scan max- |  |  |  |  |  |
| TitanCA | is | a | collaboration | between | Singapore | imizes recall because the similarity matches are highly |
| Management University (SMU) and the Government | likely to be genuine vulnerabilities. This is a deliberate |  |  |  |  |  |
| Technology | Agency | of | Singapore | (GovTech). | The | design choice, since subsequent modules are more |
| work described in this article corresponds to Phase 1 | computationally | expensive | while | contributing | more |  |
| of the TitanCA project, which concluded in January | towards false negative reduction. For the complete |  |  |  |  |  |
| 2026. The full pipeline has been delivered to the target | clone-detection algorithm and its evaluation, see Bui |  |  |  |  |  |
| organization, and a lightweight version has been de- | et al. [1]. |  |  |  |  |  |

ployed. We also run the first three modules (without the

| domain-specific adaptation module) in a continuous | Module 2: The Filter (R2Vul) |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fashion to monitor a wide variety of OSS repositories. | The | second | module | applies | reasoning-based |  |  |
| As of March 2026, TitanCA has analysed code from | screening to further identify true vulnerabilities among |  |  |  |  |  |  |
| over 127,000 GitHub repositories, identified 203 zero- | the candidates that the Matcher did not | flag, | i.e., |  |  |  |  |
| day vulnerabilities, all subsequently remediated, and | functions that did not match any known vulnerability |  |  |  |  |  |  |
| published 118 CVEs as a direct result of our approach. | pattern but may still contain novel or previously un- |  |  |  |  |  |  |
| This | article | describes | the | technical | architecture | of | seen weaknesses. R2Vul [2] is trained with structured |
| TitanCA, presents deployment results on OSS, and | reasoning distillation that distinguishes between two |  |  |  |  |  |  |
| distils engineering lessons that may guide other teams | types of model reasoning: grounded reasoning, where |  |  |  |  |  |  |
| building LLM-powered security tooling. | the logical chain matches the label, and misleading |  |  |  |  |  |  |

reasoning, where the explanation sounds plausible but

is logically disconnected from the label. The training

process uses contrastive supervision with RLAIF (Re-

inforcement Learning from AI Feedback), presenting

IEEE Security & Privacy Magazine

2

---

## Page 3

FIGURE 1. Overview of the TitanCA pipeline. The four modules progressively refine detection results: the

Matcher (VulCoCo) casts a wide net for candidate vulnerabilities, the Filter (R2Vul) reduces false positives

through structured reasoning, the Inspector (VulTrial) applies multi-agent deliberation, and the Adapter (PairVul)

handles domain-specific adaptation.

| the | model | with | paired | examples | of | grounded | and | Module 3: The Inspector (VulTrial) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| misleading analyses of the same code fragment via the | The third module introduces multi-agent deliber- |  |  |  |  |  |  |  |
| ORPO preference optimization objective. This teaches | ation using a mock-courtroom metaphor. VulTrial [3] |  |  |  |  |  |  |  |
| the model not merely to classify code as vulnerable or | convenes four specialized agents, each playing a dis- |  |  |  |  |  |  |  |
| safe, but to produce an explicit chain of reasoning that | tinct role in the adjudication process. A Security Re- |  |  |  |  |  |  |  |
| justifies its judgment. | searcher presents the case that the code is vulnerable, |  |  |  |  |  |  |  |
| R2Vul also incorporates a lightweight calibration | marshaling evidence from the earlier pipeline stages. A |  |  |  |  |  |  |  |
| step that leverages the model’s own reasoning struc- | Code Author defends the code, arguing that the flagged |  |  |  |  |  |  |  |
| ture. | At | inference | time, | the | system | compares | the | pattern is intentional or safe. A Moderator serves as |
| conditional log-likelihoods of the model generating | the judge, it distills the exchange into an impartial, |  |  |  |  |  |  |  |
| reasoning under the vulnerable versus safe template | fact-focused summary of the key points raised by |  |  |  |  |  |  |  |
| prefixes, converting the log-odds margin into a confi- | both the security researcher and the code author. A |  |  |  |  |  |  |  |
| dence score through a logistic mapping. A function | Review Board functions as the jury and issues the final |  |  |  |  |  |  |  |
| is flagged as vulnerable only when this confidence | verdict. This adversarial structure forces the system |  |  |  |  |  |  |  |
| exceeds a tunable threshold. In practice, this cali- | to consider both sides of each case, mimicking the |  |  |  |  |  |  |  |
| bration reduces the false positive rate from 28% to | deliberative process that experienced security analysts |  |  |  |  |  |  |  |
| 20% under balanced conditions while preserving over | employ during manual code review. The multi-agent |  |  |  |  |  |  |  |
| 77% recall, and achieves the same false positive target | design helps surface subtle vulnerabilities that a single |  |  |  |  |  |  |  |
| even under extreme class imbalance (1:10 vulnerable- | model might miss, while filtering out false alarms. In |  |  |  |  |  |  |  |
| to-safe ratio) typical of production environments. If | the OSS pipeline, this module is the final decision |  |  |  |  |  |  |  |
| the candidate function is classified as safe, we exit | point. In the target deployment, functions classified |  |  |  |  |  |  |  |
| the prediction pipeline; otherwise, it flows to Module | as safe exit the pipeline here; those still flagged as |  |  |  |  |  |  |  |
| 3 for further investigation. Additional details on the | vulnerable flow to Module 4 for further investigation. |  |  |  |  |  |  |  |
| structured reasoning distillation, RLAIF training, and | The full multi-agent design and ablation results are |  |  |  |  |  |  |  |
| calibration procedure can be found in Weyssow et | reported in Widyasari et al. [3]. |  |  |  |  |  |  |  |

al. [2].

xxx/xxx YYYY

3

---

## Page 4

TitanCA

Module 4: The Adapter (PairVul) and benchmark composition, see Li et al. [5] and Li

The fourth module addresses the problem of et al. [4].

domain-specific adaptation. When TitanCA is de-

| ployed | in | a | new | organizational | context, | with | dif- | Supporting the open source community |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ferent programming languages, frameworks, coding | As | of | March | 2026, | the | system | has | identified |
| conventions, | and | vulnerability | patterns, | the | coding | 203 vulnerabilities in OSS that were subsequently |  |  |
| conventions | and | existing | vulnerabilities | may | differ | confirmed and fixed by their respective development |  |  |
| substantially from the training data. To address this | teams. Of these, 118 have been assigned CVE identi- |  |  |  |  |  |  |  |
| gap, we first deployed the lightweight version in the | fiers and published. The complete CVE list is pub- |  |  |  |  |  |  |  |
| target organization to get initial results. To ensure | licly available in https://titancaproject.github.io/cves. |  |  |  |  |  |  |  |
| the high quality of the labels, we first manually la- | html. The severity profile of discovered vulnerabili- |  |  |  |  |  |  |  |
| beled a sample of functions, then applied LLM-based | ties underscores the system’s ability to detect major |  |  |  |  |  |  |  |
| relabeling. We propose PairVul, which analyzes the | issues: 35% are rated critical severity, 95% are at least |  |  |  |  |  |  |  |
| false positives generated during initial deployment to | medium severity, and 91% exhibit low attack com- |  |  |  |  |  |  |  |
| identify recurring error patterns. PairVul then fine- | plexity, meaning they are relatively straightforward to |  |  |  |  |  |  |  |
| tunes the detection models using these newly labeled | exploit once discovered. |  |  |  |  |  |  |  |
| examples. This creates a feedback loop that enables the | Approximately half of the discovered vulnerabil- |  |  |  |  |  |  |  |
| system to continuously improve its precision within | ities fall within the CWE Top-25 Most Dangerous |  |  |  |  |  |  |  |
| a specific deployment environment without requiring | Software Weaknesses, a list maintained by MITRE |  |  |  |  |  |  |  |
| expensive manual annotation of new training data. | that represents the most prevalent and impactful vul- |  |  |  |  |  |  |  |

nerability categories. The most frequently identified

| Data Foundation and Infrastructure | types include CWE-787 (out-of-bounds write), CWE- |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Effective LLM-based vulnerability detection re- | 125 (out-of-bounds read), CWE-190 (integer overflow |  |  |  |  |  |  |  |
| quires high-quality training data at scale, and con- | or wraparound), CWE-119 (improper restriction of |  |  |  |  |  |  |  |
| structing such datasets is a research challenge on its | operations within the bounds of a memory buffer), |  |  |  |  |  |  |  |
| own. The TitanCA project invested heavily in data | CWE-835 (loop with unreachable exit condition), and |  |  |  |  |  |  |  |
| engineering, building the dataset from both real-world | CWE-22 | (improper | limitation | of | a | pathname | to | a |
| vulnerability disclosures and synthetic generation tech- | restricted directory). |  |  |  |  |  |  |  |

niques. The dataset now contains over 342,000 likely

vulnerability samples. We propose CleanVul [5] to

Lessons learned

address the label noise, which is a well-known but

| often overlooked problem in vulnerability datasets. | Orchestration over monolithic models. |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Many publicly available datasets contain mislabeled | The most important architectural insight from Ti- |  |  |  |  |  |  |
| samples, code labeled as vulnerable when it is not, or | tanCA is that a pipeline of specialized, collaborating |  |  |  |  |  |  |
| vice versa, that silently degrade model performance | agents outperforms a single model. Each module ad- |  |  |  |  |  |  |
| during training. CleanVul applies systematic clean- | dresses a specific failure mode: the Matcher ensures |  |  |  |  |  |  |
| ing procedures, combining automated heuristics with | broad coverage, the Filter enforces LLMs’ reasoning, |  |  |  |  |  |  |
| LLM-assisted verification, to produce more reliable | the Inspector solicits opinions from multiple LLMs, |  |  |  |  |  |  |
| training | sets. | More | recently, | we | propose | TitanVul | and the Adapter handles distribution shift. This divi- |
| and BenchVul [4]: a large-scale, high-quality training | sion of labor is similar to how human security teams |  |  |  |  |  |  |
| dataset and a manually curated benchmark covering the | operate: different specialists contributing complemen- |  |  |  |  |  |  |
| MITRE Top 25 Most Dangerous CWEs, revealing that | tary perspectives to a shared objective. |  |  |  |  |  |  |
| in-distribution performance is a poor predictor of real- | We did not arrive at this design on the first attempt. |  |  |  |  |  |  |
| world generalization. The operational infrastructure | Our earliest effort tried to fine-tune a single LLM to |  |  |  |  |  |  |
| is substantial: approximately 500 terabytes of data | perform end-to-end vulnerability detection. It achieved |  |  |  |  |  |  |
| engineering workloads support the monitoring of over | reasonable recall but generated an unmanageable vol- |  |  |  |  |  |  |
| 127,000 GitHub repositories. This scale is essential for | ume of false positives. As the project progressed, we |  |  |  |  |  |  |
| training models that generalize across the diversity of | decomposed the task into specialized stages, realiz- |  |  |  |  |  |  |
| real-world code patterns, languages, and vulnerability | ing that vulnerability detection is not one problem |  |  |  |  |  |  |
| types. For the dataset construction, cleaning heuristics, | but several. Those can include pattern recognition, |  |  |  |  |  |  |

IEEE Security & Privacy Magazine

4

---

## Page 5

| logical reasoning, adversarial validation, and domain | planations. |
| --- | --- |
| adaptation. Each demands a different model capability. | An under-appreciated aspect of this problem is |
| We anticipate that this observation can generalize, | that a correct prediction accompanied by a wrong |
| especially for complex security tasks, as orchestrating | explanation can be more damaging than a direct in- |
| specialists will consistently outperform scaling a single | correct prediction. When the model flags a function as |
| generalist. | vulnerable but cites an irrelevant reason, the developer |

reads the explanation, recognizes it as flawed, and

| Cost-aware pipeline ordering. | drops the entire warning. We found that grounding |
| --- | --- |
| The ordering of the pipeline matters as well. Our | the reasoning chain not only improved classification |
| first design placed the multi-agent Inspector and the | accuracy but, more importantly, reduced the rate at |
| lightweight Filter in parallel, because the two com- | which developers drop valid alerts due to unconvincing |
| ponents originated from different research motivations | explanations. |

and were initially developed as alternative approaches.

| This turned out to be wasteful: the Inspector involves | Multi-agent debate catches what single models |
| --- | --- |
| multiple LLM calls per function and is computation- | miss. |
| ally expensive. Restructuring the pipeline so that cheap | The mock courtroom design of VulTrial addresses |
| filtering runs first and expensive deliberation runs later | a limitation of single-model inference: confirmation |
| reduced our per-function cost substantially. The lesson | bias. When a single model produces a vulnerability |
| is that pipeline design for LLM-based systems should | prediction, it has no internal mechanism to challenge |
| follow a similar principle as query optimization: push | its own reasoning. The multi-agent adversarial struc- |
| the cheapest, most selective operations to the front. | ture forces explicit consideration of counter-arguments |

and alternative explanations. This process produces

Precision is critical in practice. more robust judgments than any single model alone.

In production environments, false positives are

| more operationally damaging than false negatives. De- | Adaptation is essential for deployment. |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| velopers can be overwhelmed by an excess of warnings | Since no model trained exclusively on public data |  |  |  |  |  |  |  |  |
| quickly | and | then | tend | to | ignore | the | tool | entirely. | can perfectly capture the vulnerability patterns, coding |
| In this project, we focus on the F0.3 metric, which | idioms, and framework usage of a specific organiza- |  |  |  |  |  |  |  |  |
| weights precision three times more than recall, and | tion, it is critical to incorporate domain characteristics. |  |  |  |  |  |  |  |  |
| better captures this operational reality than the standard | We initially applied only the first three modules, with- |  |  |  |  |  |  |  |  |
| F1 score. TitanCA’s architecture is explicitly designed | out the adapter, in the target environment. But after |  |  |  |  |  |  |  |  |
| to maximize this metric through successive filtering | a few sample runs, we observed some unique false |  |  |  |  |  |  |  |  |
| stages. | positive patterns and realized the need to learn domain- |  |  |  |  |  |  |  |  |
| We believe the academic community’s reliance on | specific | code | patterns. | To | handle | these | cases, | we |  |
| F1 as the primary evaluation metric for vulnerability | propose PairVul to systematically analyze deployment- |  |  |  |  |  |  |  |  |
| detection is misleading. F1 assumes that false positives | time false positives to generate new training signals |  |  |  |  |  |  |  |  |
| and false negatives are equally costly, an assumption | with the feedback loop. This step is critical for main- |  |  |  |  |  |  |  |  |
| that does not hold in practical usage. We encourage fu- | taining and improving precision as the system encoun- |  |  |  |  |  |  |  |  |
| ture work to report F0.3 or similar precision-weighted | ters novel codebases and evolving software practices. |  |  |  |  |  |  |  |  |
| metrics alongside F1 to provide a more realistic picture | We believe these patterns need to be adapted when |  |  |  |  |  |  |  |  |
| of practical utility. | applied in different target organizations. |  |  |  |  |  |  |  |  |
| Structured reasoning improves reliability. | The road ahead |  |  |  |  |  |  |  |  |
| The | R2Vul | module | trains | LLMs | to | produce | Phase 1 of TitanCA operated at the function level |  |  |
| grounded reasoning chains rather than simply produc- | and focused exclusively on detection. Phase 2, which |  |  |  |  |  |  |  |  |
| ing classification labels. This approach significantly | commenced in March 2026, extends the system in |  |  |  |  |  |  |  |  |
| improves the reliability and interpretability of model | three directions. First, it expands the analysis context |  |  |  |  |  |  |  |  |
| outputs. By contrasting grounded and misleading rea- | beyond individual functions to leverage the broader |  |  |  |  |  |  |  |  |
| soning | during | training, | the | model | learns | to | avoid | security reasoning capabilities of agentic frameworks. |  |
| superficially plausible but logically disconnected ex- | Second, it provides repair suggestions to help develop- |  |  |  |  |  |  |  |  |

xxx/xxx YYYY

5

---

## Page 6

TitanCA

studying how developers perceive and respond to AI-

remain open: whether LLM agents can generate secure

Conclusion

In TitanCA Phase 1, our experience demonstrates

that orchestrating multiple LLM-powered agents into

a structured, layered pipeline can achieve vulnerabil-

ity discovery results that substantially exceed those

of conventional SAST tools. As LLMs continue to

improve in both capability and efficiency, systems

like TitanCA point toward a future where automated

vulnerability discovery operates as an effective and

trustworthy complement to human security expertise.

Acknowledgment

This research / project is supported by the Na-

tional Research Foundation, Singapore and Ministry of

Digital Development & Information under its Smart

Nation and Digital Government Translational R&D

Grant (Award No: TRANS2026-TGC01). Any opin-

ions, findings and conclusions or recommendations

expressed in this material are those of the author(s)

and do not reflect the views of National Research

Foundation, Singapore.

2. M. Weyssow, C. Yang, J. Chen, R. Widyasari, T. Zhang,

F. Liauw, E. L. Ouh, L. K. Shar, H. J. Kang, and D. Lo,

6

arXiv:2505.10961 , 2025.

arXiv:2507.21817 , 2025.

detection in code commits using LLM heuristics,” arXiv

preprint arXiv:2411.17274 , 2024.

6. C. Yang, T. Zhang, J. Jiang, X. Zhou, H. Tian, J. Shi,

J. Chen, Y. Li, E. L. Ouh, L. K. Shar et al. ,

“Semantics-aligned, curriculum-driven, and

reasoning-enhanced vulnerability repair framework,”

Accepted by ACL 2026 arXiv preprint arXiv:2510.01002 ,

2025.

7. J. Chen, H. Huang, Y. Lyu, J. An, J. Shi, C. Yang,

T. Zhang, H. Tian, Y. Li, Z. Li et al. , “SecureAgentBench:

Benchmarking secure code generation under realistic

vulnerability scenarios,” Accepted by ACL 2026 arXiv

preprint arXiv:2509.22097 , 2025.

Ting Zhang is a Lecturer in the Department of Soft-

ware Systems and Cybersecurity at Monash Univer-

sity in Clayton, Victoria 3800, Australia. Her research

interests include vulnerability detection, vulnerability

repair, and secure code generation. Zhang received

her Ph.D. in Computer Science from Singapore Man-

agement University. Contact her at https://happygirlzt.

com/academic or happygirlzt@gmail.com.

Yikun Li is a Research Scientist at Singapore Man-

IEEE Security & Privacy Magazine

| ers fix discovered vulnerabilities more efficiently [6]. | vulnerability detection using LLM-based agents,” |  |  |  |
| --- | --- | --- | --- | --- |
| Third, it incorporates research into developer behavior, | Accepted by ICSE 2026 arXiv preprint |  |  |  |
| generated vulnerability reports, with the goal of im- | 4. | Y. Li, N. T. Bui, T. Zhang, C. Yang, X. Zhou, |  |  |
| proving the system’s reporting interface and explana- | M. Weyssow, J. Jiang, J. Chen, H. Huang, H. H. Nguyen |  |  |  |
| tion quality. | et al. | , “Out of distribution, out of luck: How well can llms |  |  |
| Both phases focus on detecting vulnerabilities in | trained on vulnerability datasets detect top 25 CWE |  |  |  |
| developer-written code. Two complementary questions | weaknesses?” | Accepted by ICSE 2026 arXiv preprint |  |  |
| code in the first place [7], and whether they can | 5. | Y. Li, T. Zhang, R. Widyasari, Y. N. Tun, H. H. Nguyen, |  |  |
| effectively detect vulnerabilities in AI-generated code | T. Bui, I. C. Irsan, Y. Cheng, X. Lan, H. W. Ang | et al. | , |  |
| as LLM-based coding agents become widely adopted. | “CleanVul: Automatic function-level vulnerability |  |  |  |
| REFERENCES | agement University. His research interests include |  |  |  |
| 1. | T. Bui, Y. N. Tun, T. P. Nguyen, Y. Su, F. Thung, Y. Li, | software vulnerability detection and repair, and AI- |  |  |
| H. W. Ang, Y. Yin, F. Liauw, L. K. Shar | et al. | , “VulCoCo: | driven software security. Li received his PhD in Com- |  |
| A simple yet effective method for detecting vulnerable | puter Science from the University of Groningen, the |  |  |  |
| code clones,” | arXiv preprint arXiv:2507.16661 | , 2025. | Netherlands. Contact him at yikunli@smu.edu.sg. |  |
| H. Huang, H. H. Nguyen, Y. N. Tun, T. Bui, Y. Li | et al. | , | Chengran Yang | is a Research Scientist at Singa- |
| “R2Vul: Learning to reason about software | pore Management University. His research interests |  |  |  |
| vulnerabilities with reinforcement learning and | include trustworthy code models, code vulnerability |  |  |  |
| structured reasoning distillation,” | arXiv preprint | analysis, and code testing. Yang received his PhD |  |  |
| arXiv:2504.04699 | , 2025. | in computer science from Singapore Management |  |  |
| 3. | R. Widyasari, M. Weyssow, I. C. Irsan, H. W. Ang, | University. Contact him at chengran98@gmail.com. |  |  |
| “Let the trial begin: A mock-court approach to | Ratnadira Widyasari | is a Research Scientist at |  |  |

---

## Page 7

Singapore Management University. Her research ence and Technology. Contact him at huuhungn@

focuses on advancing software quality assurance smu.edu.sg.

through automation and explainability. Widyasari re-

programming. Liu received his Ph.D. in information

technology from Monash University. Contact him at

validation. Bui received his bachelor’s degree in com-

puter science from Hanoi University of Science and

smu.edu.sg.

yannaingtun@smu.edu.sg.

chains. Nguyen received his bachelor’s degree in

xxx/xxx YYYY

for software engineering, vulnerability detection, and

hhhuang@smu.edu.sg.

pore Management University. His research interests

him at jfjiang@smu.edu.sg.

puter Science (Practice) at Singapore Management

Eng Lieh Ouh is an Associate Professor of Com-

at elouh@smu.edu.sg.

ACM Fellow, IEEE Fellow, Fellow of Automated Soft-

7

| ceived her Ph.D. from Singapore Management Uni- | Huihui Huang | is a PhD student at Singapore Man- |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| versity. Contact her at https://ratnadiraw.github.io/. | agement University. Her research interests include AI |  |  |  |  |  |  |  |
| Yue | Liu | is | a | Research | Scientist | at | Singapore | agentic penetration testing. Huang received her bach- |
| Management University. His research interests in- | elor’s degree in computer science and technology |  |  |  |  |  |  |  |
| clude trustworthy AI for software development, secure | from Southern University of Science and Technology. |  |  |  |  |  |  |  |
| AI coding tools, and developer trust in AI-assisted | She is a student member of ACM. Contact her at |  |  |  |  |  |  |  |
| https://yueyuel.github.io/. | Jinfeng Jiang | is a Research Engineer at Singa- |  |  |  |  |  |  |
| Ngoc Tan Bui | is a PhD student at Singapore Man- | include AI for Software Engineering and Trustworthy |  |  |  |  |  |  |
| agement University. His research interests include | Code LLM. Jiang received his Master’s degree in |  |  |  |  |  |  |  |
| vulnerability detection, vulnerability repair, and patch | Software Engineering from Tongji University. Contact |  |  |  |  |  |  |  |
| Technology. Contact him at ngoctanbui@smu.edu.sg. | Lwin Khin Shar | is an Associate Professor of Com- |  |  |  |  |  |  |
| Phuc Thanh Nguyen | is a Research Engineer at | University. | His | research | interests | include | security |  |
| Singapore Management University. His research in- | testing and analysis of web/mobile applications and |  |  |  |  |  |  |  |
| terests include vulnerability detection and software | cyber physical systems. Shar received his Ph.D in |  |  |  |  |  |  |  |
| security topics. Nguyen received his bachelor’s de- | Software Engineering from Nanyang Technological |  |  |  |  |  |  |  |
| gree in data science from Hanoi University of Science | University, Singapore. He is a member of IEEE and |  |  |  |  |  |  |  |
| and Technology, Vietnam. Contact him at ptnguyen@ | ACM. Contact him at lkshar@smu.edu.sg. |  |  |  |  |  |  |  |
| Yan Naing Tun | is a Research Engineer at Sin- | puter Science (Education) at Singapore Management |  |  |  |  |  |  |
| gapore Management University. His research inter- | University. His research interests include AI-enabled |  |  |  |  |  |  |  |
| ests include software testing and security, vulner- | vulnerability detection, secure software engineering, |  |  |  |  |  |  |  |
| ability detection, Android and IoT security, and AI- | and computing education. Ouh received his Ph.D in |  |  |  |  |  |  |  |
| assisted software engineering. Tun received his B.Sc. | Computer Science from the National University of |  |  |  |  |  |  |  |
| in Computer Science from the University of Com- | Singapore. He is a Senior Member of IEEE and an |  |  |  |  |  |  |  |
| puter Studies, Mandalay, Myanmar. Contact him at | ISC2 member and authorised instructor. Contact him |  |  |  |  |  |  |  |
| Ivana Clairine Irsan | is a PhD student at Singa- | David Lo | is the OUB Chair Professor of Computer |  |  |  |  |  |
| pore Management University. Her research interests | Science and Vice Provost (Research) Designate at |  |  |  |  |  |  |  |
| include vulnerability detection and software security | Singapore Management University. His research in- |  |  |  |  |  |  |  |
| topics. Irsan received her master’s degree in Com- | terests | include | software | engineering, | AI, | and | cy- |  |
| puter Science from Institut Teknologi Bandung. Con- | bersecurity. Lo received his PhD in Computer Sci- |  |  |  |  |  |  |  |
| tact her at ivanairsan@smu.edu.sg. | ence from National University of Singapore. He is an |  |  |  |  |  |  |  |
| Huu Hung Nguyen | is a PhD student at Singa- | ware Engineering, and NRF Investigator (Senior Fel- |  |  |  |  |  |  |
| pore Management University. His research interests | low). Contact him at https://faculty.smu.edu.sg/profile/ |  |  |  |  |  |  |  |
| include vulnerability detection and software supply | david-lo-901 or davidlo@smu.edu.sg. |  |  |  |  |  |  |  |
| Information Technology from Hanoi University of Sci- | Hong Jin Kang | is a Lecturer in the School of |  |  |  |  |  |  |

---

## Page 8

TitanCA

Computer Science at The University of Sydney in

Sydney, New South Wales 2006, Australia. His re-

search interests include program analysis and se-

cure software engineering. Kang received his PhD

in Computer Science from Singapore Management

University. Contact him at kanghj.github.io or hongjin.

kang@sydney.edu.au.

Yin Yide is a Cybersecurity Engineer at the Govern-

ment Technology Agency of Singapore. His research

interests include vulnerability detection and automatic

patch generation. Yide received his MSc in Comput-

ing Science from Imperial College London. Contact

him at yin yide@tech.gov.sg.

Leow Wen Bin is a Cybersecurity Engineer in the

Government Technology Agency of Singapore. His

research interests include vulnerability detection, se-

cure code generation, and federated learning. Leow

received his Master of Science in Engineering from

Tsinghua University. Contact him at linkedin.com/in/

leowwb or leow wen bin@tech.gov.sg.

IEEE Security & Privacy Magazine

8

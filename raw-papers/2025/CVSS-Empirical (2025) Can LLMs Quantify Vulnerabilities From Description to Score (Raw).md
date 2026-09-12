---
title: "From Description to Score: Can LLMs Quantify Vulnerabilities?"
author: "Sima Jafarikhah; Daniel Thompson; Eva Deans; Hossein Siadati; Yi Liu"
creator: "arXiv GenPDF (tex2pdf:57610bf)"
pages: 10
---

# From Description to Score: Can LLMs Quantify Vulnerabilities?

> **作者**：Sima Jafarikhah; Daniel Thompson; Eva Deans; Hossein Siadati; Yi Liu
> **總頁數**：10 頁

---

## Page 1

From Description to Score: Can LLMs Quantify Vulnerabilities?

| Sima Jafarikhah | Daniel Thompson | Eva Deans |  |
| --- | --- | --- | --- |
| University of North Carolina | University of North Carolina | University of North Carolina |  |
| Wilmington | Wilmington | Wilmington |  |
| Wilmington, NC, USA | Wilmington, NC, USA | Wilmington, NC, USA |  |
| jafarikhaht@uncw.edu | dbt9576@uncw.edu | ecd7121@uncw.edu |  |
| Hossein Siadati | Yi Liu |  |  |
| University of North Carolina | University of North Carolina |  |  |
| Wilmington | Wilmington |  |  |
| Wilmington, NC, USA | Wilmington, NC, USA |  |  |
| s.h.siadaty@gmail.com | liuyi@uncw.edu |  |  |
| Abstract | 1 | Introduction |  |
| Manual vulnerability scoring, such as assigning Common Vulnera- | Vulnerability management is a fundamental component of software |  |  |
| bility Scoring System (CVSS) scores, is a resource-intensive process | security programs across organizations. Public databases such as |  |  |
| that is often influenced by subjective interpretation. This study | the National Vulnerability Database (NVD), maintained by NIST’s |  |  |
| investigates the potential of general-purpose large language mod- | Information Technology Laboratory (ITL) [18], catalog and score |  |  |
| els (LLMs), namely ChatGPT, Llama, Grok, DeepSeek, and Gemini, | newly disclosed vulnerabilities. In 2024, the NVD published 40,009 |  |  |
| to automate this process by analyzing over 31,000 recent Com- | CVEs, over 38% more than in 2023 [9], increasing the demand for |  |  |
| mon Vulnerabilities and Exposures (CVE) entries. The results show | timely and consistent CVSS scoring [8], which organizations rely |  |  |
| that LLMs substantially outperform the baseline on certain met- | on to prioritize remediation and allocate security resources. |  |  |
| rics (e.g., | Availability Impact | ), while offering more modest gains | This rapid growth has placed substantial strain on maintainers |
| on others (e.g., | Attack Complexity | ). Moreover, model performance | and threat intelligence providers. Throughout 2024, the NVD faced |
| varies across both LLM families and individual CVSS metrics, with | significant processing backlogs [16], leaving many vulnerabilities |  |  |
| ChatGPT-5 attaining the highest precision. Our analysis reveals that | unscored or inconsistently characterized and limiting organizations’ |  |  |
| LLMs tend to misclassify many of the same CVEs, and ensemble- | ability to assess risk effectively. Internally discovered vulnerabilities |  |  |
| based meta-classifiers only marginally improve performance. Fur- | pose similar challenges, as they often lack standardized severity |  |  |
| ther examination shows that CVE descriptions often lack critical | ratings, making prioritization subjective and resource-intensive. |  |  |
| context or contain ambiguous phrasing, which contributes to sys- | On the other hand, recent advances in GenAI have shown that |  |  |
| tematic misclassifications. These findings underscore the impor- | LLMs possess capabilities that go well beyond natural language |  |  |
| tance of enhancing vulnerability descriptions and incorporating | generation. In particular, they have proven effective in classification |  |  |
| richer contextual details to support more reliable automated rea- | tasks, including multi-class scenarios, by reframing classification as |  |  |
| soning and alleviate the growing backlog of CVEs awaiting triage. | a text-to-text task [10, 34]. This allows LLMs to assign class labels |  |  |

based on textual input without requiring modifications to their

| CCS Concepts | underlying architecture [2, 25]. These advances prompt a natural |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| • | Security and privacy | → | Software and application security | ; | question: to what extent can generative AI be leveraged to classify |
| Vulnerability management | ; • | Computing methodologies | → | Nat- | vulnerability metrics, such as those defined in the CVE system, |
| ural language processing | ; Machine learning approaches. | using only the textual description of the vulnerability. If effective, |  |  |  |

such an approach could enable automated vulnerability scoring

Keywords and help mitigate issues like the backlog observed in the NVD.

arXiv:2512.06781v3 [cs.CR] 5 Jan 2026 Motivated by this question, the main contributions of this paper

Vulnerability, CVSS, CVE, Generative AI

are as follows:

ACM Reference Format:

| Sima Jafarikhah, Daniel Thompson, Eva Deans, Hossein Siadati, and Yi Liu. | (1) | Individual LLM Classifiers: | We investigate the feasibility |
| --- | --- | --- | --- |
| 2026. From Description to Score: Can LLMs Quantify Vulnerabilities?. In | of leveraging general-purpose generative AI models to au- |  |  |
| The 41st ACM/SIGAPP Symposium on Applied Computing (SAC ’26), March | tomate vulnerability scoring by systematically evaluating |  |  |
| 23–27, 2026, Thessaloniki, Greece. | ACM, New York, NY, USA, 10 pages. https: | their ability to assign CVSS metric scores to CVEs using only |  |
| //doi.org/10.1145/3748522.3779726 | the textual “descriptions” field. It is important to emphasize |  |  |

that including CVE identifiers (CVE ID), would compromise

the validity of this evaluation and constitute poor feature

| This work is licensed under a Creative Commons Attribution 4.0 International License. | engineering, as it allows the LLM to act merely as a retrieval |
| --- | --- |
| SAC ’26, Thessaloniki, Greece | system rather than performing genuine classification. |

© 2026 Copyright held by the owner/author(s).

ACM ISBN 979-8-4007-2294-3/2026/03 (2) Meta-LLM Classifiers: We evaluate multiple LLM mod-

https://doi.org/10.1145/3748522.3779726 els and analyze inconsistencies in their classifications for

---

## Page 2

| SAC ’26, March 23–27, 2026, Thessaloniki, Greece | Jafarikhah et al. |  |  |
| --- | --- | --- | --- |
| this task. Furthermore, we construct a meta-classifier to ex- | • | Temporal: | Adjusts the Base score for factors like exploit |
| amine whether combining their outputs yields improved | maturity or remediation. Multipliers typically range from |  |  |
| performance, or if the observed limitations stem from the | 0.91 to 1.00. |  |  |
| inherent ambiguity and contextual insufficiency of existing | • | Environmental: | Adapts the score to an organization’s con- |
| vulnerability descriptions. | text by prioritizing CIA elements (e.g., High = 1.5, Low = |  |  |
| The remainder of this paper is organized as follows. Section 2 | 0.5). |  |  |
| reviews the CVSS, the challenges faced by the NVD, and the role | These components collectively yield the final CVSS score (0–10), |  |  |
| of generative AI in classification tasks. Section 3 reviews and sum- | allowing organizations to assess severity and prioritize remediation |  |  |
| marizes research on automated CVSS prediction and AI-assisted | based on both technical and business impact. Table 1 presents the |  |  |
| vulnerability assessment. Section 4 details the study design, in- | weights assigned to each class within the individual CVSS metrics. |  |  |

cluding data collection, model selection, and prompt engineering.

Section 5 outlines our evaluation metrics, and Section 6 presents our

findings for both individual LLMs and the proposed meta-classifier.

Section 7 highlights key insights, Section 8 discusses implications

and future directions, and finally Section 9 concludes the study, re-

flecting on the potential of generative AI to augment vulnerability

management workflows.

2 Background

The Common Vulnerabilities and Exposures (CVE) program, man-

aged by MITRE, standardizes the identification of publicly known

cybersecurity vulnerabilities using unique identifiers. CVE Num-

bering Authorities (CNAs)—spanning government, industry, and

academia—are responsible for assigning and scoring these vulnera-

a standardized, open method focused on intrinsic severity, not

contextual risk.

As shown in Figure 1, CVSS is composed of three core metric

groups:

2.2 Challenges of Triaging CVEs by NVD

The NVD has faced challenges in handling the surge of reported

vulnerabilities, 28,818 CVEs in 2023 [9], overwhelming its 21-person

team [11]. By mid-2024, fewer than 10% of 12,700 CVEs since Feb-

ruary had been analyzed [3], delaying severity scores and product

mappings vital to risk assessments [30]. Contributing factors in-

clude:

• Schema migration: Transition to JSON schema stalled

pipelines [20].

• Submission quality: Low-quality and duplicate entries con-

sume analyst time.

• Staffing: No growth despite rising disclosure volume.

3 Related Work

Challenges of Vulnerability Scoring. Manual vulnerability scor-

ing is prone to inconsistency, as shown by Wunder et al. [31], who

found that 68% of participants changed their CVSS ratings when

reassessing the same vulnerabilities. Key metrics like Attack Vector

and Privileges Required were especially error-prone. These results

highlight the subjectivity of human scoring and support the need

for automated approaches, such as those based on GenAI, to en-

sure more consistent and scalable assessments. Stoker et al. [28]

showed that despite long-term trends in CVE data, CVSS ratings

contextual risk. Similarly, Stoker et al. [19] found inconsistencies

in how vendors communicate risk. These findings motivate our use

of GenAI to deliver standardized and consistent scoring.

ML and GenAI-based Scoring of Vulnerabilities. Recent stud-

| 2.1 | Common Vulnerability Scoring System | • | CVE surge: | Submissions have outpaced manual workflows. |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bilities to ensure consistent and timely reporting. | These challenges expose systemic weaknesses. While funding |  |  |  |  |  |  |  |  |  |  |  |  |
| The Common Vulnerability Scoring System (CVSS), developed | and coordination are needed, modernizing and automating NVD |  |  |  |  |  |  |  |  |  |  |  |  |
| by FIRST.Org, is the leading framework for assessing software | processes, including automated vulnerability scoring, is critical to |  |  |  |  |  |  |  |  |  |  |  |  |
| vulnerability severity on a scale from 0 (low) to 10 (high). It provides | restoring timely vulnerability triage [27]. |  |  |  |  |  |  |  |  |  |  |  |  |
| Figure 1: CVSS Metric Groups [7] | remained clustered around medium severity, often failing to reflect |  |  |  |  |  |  |  |  |  |  |  |  |
| • | Base: | Captures the intrinsic properties of a vulnerability. It | ies have explored ML for creating explainable AI to help Counting |  |  |  |  |  |  |  |  |  |  |
| includes: | Number Authority scoring vulnerabilities faster and more accu- |  |  |  |  |  |  |  |  |  |  |  |  |
| – Exploitability: | Assesses exploit ease using | Attack Vector | rately. Manai et al. [12] used XGBoost with SHAP to produce in- |  |  |  |  |  |  |  |  |  |  |
| (AV) | , | Attack Complexity (AC) | , | Privileges Required (PR) | , and | terpretable CVSS v3.1 predictions. Yazigi [33] proposed a GenAI |  |  |  |  |  |  |  |
| User Interaction (UI) | . For example, remote vectors (0.85) | system that aggregates threat data for dynamic risk scoring. Alam |  |  |  |  |  |  |  |  |  |  |  |
| are more severe than physical ones (0.20). | et al. [1] introduced CTIBench, which benchmarks LLMs on five |  |  |  |  |  |  |  |  |  |  |  |  |
| – Impact: | Measures effects on | Confidentiality | , | Integrity | , and | cybersecurity tasks, including CTI-VSP, closely aligned with our |  |  |  |  |  |  |  |
| Availability (CIA) | —rated as High (0.56), Low (0.22), or | focus. Using zero-shot prompting on 1,000 CVEs, they found perfor- |  |  |  |  |  |  |  |  |  |  |  |
| None (0.00). | mance was sensitive to description length. Our study extends this |  |  |  |  |  |  |  |  |  |  |  |  |
| The Exploitability subscore is: | by analyzing 31,000+ CVEs, evaluating class imbalance, inter-metric |  |  |  |  |  |  |  |  |  |  |  |  |
| Exploitability | = | 8 | . | 22 | × | 𝐴𝑉 | × | 𝐴𝐶 | × | 𝑃𝑅 | × | 𝑈 𝐼 | correlations, and model performance using precision, F1-score, and |

---

## Page 3

ical, 0.20)

Table 1: CVSS v3.1 Base Metrics with Type Classification and Metric Values

4 Study Design

4.1 Objective

The objective of this study is to systematically evaluate the predic-

tive capabilities of LLMs for automated vulnerability assessment,

with a focus on accurately inferring CVSS scores from textual vul-

nerability descriptions.

ditional quality filters excluded CVEs with missing, non-English, or

incomplete data. For the purposes of this study, the v3.1 CVSS base

SAC ’26, March 23–27, 2026, Thessaloniki, Greece

(Values depend on Scope being Unchanged/Changed)

GPT-5, Llama, DeepSeek, and Grok, and Google’s AI Studio for

Gemini.

4.4 Prompt Engineering

We followed OpenAI’s best practices [21] in designing the prompt

that directed the LLMs to generate CVSS base metric scores. One

best practice is to be specific on the task and avoid combining re-

sults [15]. Therefore, our prompt did not ask for the overall CVSS

score and instead asked for itemized scoring of metrics. We in-

structed the model to act as a cybersecurity expert. The prompt

followed a two-step structure: (1) extract the eight base metrics,

5 Evaluation Metrics

| Metric Name | Abbreviation | Possible Values (with numeric scores) | Type |
| --- | --- | --- | --- |
| Attack Vector | AV | N (Network, 0.85), A (Adjacent, 0.62), L (Local, 0.55), P (Phys- | Exploitability |
| Attack Complexity | AC | L (Low, 0.77), H (High, 0.44) | Exploitability |
| Privileges Required | PR | N (None, 0.85), L (Low, 0.62 / 0.68), H (High, 0.27 / 0.50) | Exploitability |
| User Interaction | UI | N (None, 0.85), R (Required, 0.62) | Exploitability |
| Scope | S | U (Unchanged), C (Changed) | Impact Modifier |
| Confidentiality | C | H (High, 0.56), L (Low, 0.22), N (None, 0.00) | Impact |
| Integrity | I | H (High, 0.56), L (Low, 0.22), N (None, 0.00) | Impact |
| Availability | A | H (High, 0.56), L (Low, 0.22), N (None, 0.00) | Impact |
| mean absolute error (MAE). Ullah et al. [29] conducted a compre- | 4.3 | Large Language Models |  |
| hensive evaluation of LLMs for vulnerability detection using their | This study employs six models: GPT-4o (G4) [22], GPT-5 (G5) [23], |  |  |
| framework SecLLMHolmes. They evaluated eight LLMs, showing | Llama-3.3-70B-Instruct (L) [14], Gemini-2.5-Flash (GM) [5], DeepSeek- |  |  |
| that even advanced models exhibit high false positive rates, incon- | R1 (DS) [6], and Grok-3 (GR) [32] to predict CVSS base metrics |  |  |
| sistent outputs, and fragile reasoning that breaks under minor code | directly from CVE descriptions. We intentionally selected a mix of |  |  |
| augmentations. Their findings highlight that LLMs are not yet ro- | high-performing closed-source and open-weight models to capture |  |  |
| bust enough for automated vulnerability detection in real-world | complementary strengths: closed models such as GPTs typically of- |  |  |
| settings, underscoring the need for further research into model reli- | fer state-of-the-art accuracy, robustness, and safety features, while |  |  |
| ability and reasoning faithfulness. It should be emphasized that the | open models such as Llama provide transparency, reproducibility, |  |  |
| incorporation of CVE identifiers in prompts to LLMs, together with | and adaptability for security research. These characteristics make |  |  |
| the corresponding description as in prior work [13], allows models | them strong candidates for CVSS scoring, which requires both pre- |  |  |
| to retrieve known vectors and undermines true classification. | cision and interpretability. We used Azure’s AI Foundry for GPT-4o, |  |  |
| 4.2 | Data Collection | and (2) output them in a fixed format for consistency. To ensure |  |
| The study utilizes the publicly available CVE List maintained by | deterministic outputs, if configurable, the temperature was set to 0, |  |  |
| MITRE [24] as its primary data source. While all CVEs from 2004 | following CTIBench guidance [1]. We evaluated zero-, two-, five-, |  |  |
| to 2024 were initially retrieved, the analysis focuses on entries pub- | and ten-shot prompts on a subset of 6,000 CVE entries from 2024. |  |  |
| lished from 2019 onward to ensure consistency with the CVSS v3.1 | The two-shot variant achieved the best performance; therefore, it |  |  |
| standard. After filtering for CVEs with complete CVSS v3.1 base | was adopted for all subsequent experiments. A Python script auto- |  |  |
| metrics and valid English descriptions, the final dataset consists | mated API calls in batches of 20 CVEs, appending predicted metrics |  |  |
| of 31,000+ entries. Each CVE, stored in JSON format, includes a | to CSV outputs. Using this pipeline, we processed over 31,000 CVE |  |  |
| human-readable description and eight CVSS v3.1 base metrics. Ad- | records for downstream analysis. |  |  |
| metrics and descriptions obtained from the CVE List are treated as | To assess the quality of CVSS scores produced by GPT-4o, GPT-5, |  |  |
| ground truth. Although there may be some variance in scores and | Llama-3.3-70B-Instruct, Gemini-2.5-Flash, DeepSeek-R1, and Grok- |  |  |
| descriptions, the MITRE-maintained CVE List is a widely adopted | 3, we employ several complementary evaluation metrics. An ex- |  |  |
| and standardized source of vulnerability information [17]. | amination of the CVE dataset reveals a class imbalance, making it |  |  |

---

## Page 4

| SAC ’26, March 23–27, 2026, Thessaloniki, Greece | Jafarikhah et al. |  |
| --- | --- | --- |
| important to report class-sensitive metrics such as per-class pre- | Metric | Imbalance Ratio |
| cision, recall, and F1-score, as well as their macro or weighted | Attack Complexity | 5.19 |
| averages. These metrics offer more informative insights into the | Attack Vector | 63.60 |
| models’ performance across all classes. | Privileges Required | 3.04 |

(1) Accuracy. Accuracy measures the proportion of predictions

that exactly match the true labels, indicating overall model

performance. However, due to class imbalance, it can be

misleading and should be interpreted with caution.

# correct ( 𝑦 𝑖 = 𝑦 ˆ 𝑖 )

Accuracy =

𝑁

where 𝑦 𝑖 denotes the true label, and ˆ 𝑦 𝑖 represents the pre-

dicted label.

(2) Precision. Precision measures the proportion of correct

positive predictions out of all predicted positives, reflecting

𝑇 𝑃 𝑖

Precision 𝑖 =

𝑇 𝑃 𝑖 + 𝐹 𝑃 𝑖

which averages per-class precision values weighted by the

𝐾

1 ∑︁

Weighted Precision = 𝑛 𝑖 · Precision 𝑖

𝑁 𝑖 = 1

Í

Here, 𝐾 is the total number of classes, and 𝑁 = 𝐾

𝑖 = 1 𝑛 𝑖 is

weighted precision ensures a more balanced assessment of

model performance across all classes.

It is computed as the weighted average of per-class recall

values, where each class is weighted by its number of true

instances (support). For a classification task with 𝐾 classes,

the weighted recall is defined as:

1 ∑︁ 𝐾

𝑖

𝑇 𝑃

• Recall 𝑖

𝑖 = 𝑇 𝑃 ,

𝑖

• 𝑛

𝑖 is the number of true instances in class 𝑖 , and

Í

𝑖 = 1 𝑛 𝑖 is the total number of instances across all

false negatives. For class 𝑖 , it is defined as:

F1 𝑖 = 2 ×

Precision 𝑖 + Recall 𝑖

| User Interaction | 1.72 |
| --- | --- |
| Scope | 2.11 |
| Confidentiality Impact | 1.85 |
| Integrity Impact | 1.23 |
| Availability Impact | 1.77 |

Table 2: Imbalance Ratio of CVSS metrics

number of true instances 𝑛 𝑖 :

1 ∑︁

𝑁

have an inherent ordinal order (e.g., Network to Physical ). To

capture the severity of prediction errors, we assign ordinal

values and compute MAE as:

𝑛

1 ∑︁

𝑁 𝑖 = 1

deviate from true values.

6 Analysis

6.1 Exploring the CVE Dataset

like accuracy.

considered.

Distribution of severity classes. Figure 3 illustrates the distribu-

and should be considered during the analysis.

| the model’s accuracy in assigning labels. For a specific class | To address class imbalance, we compute the | weighted F1- |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 𝑖 | , it is defined as: | score | , which averages per-class F1-scores weighted by the |  |  |  |  |  |  |  |
| where | 𝑇 𝑃 | 𝑖 | and | 𝐹 𝑃 | 𝑖 | denote the true and false positives for | 𝐾 |  |  |  |
| class | 𝑖 | , respectively. | Weighted F1 | = | 𝑛 | 𝑖 | · | F1 | 𝑖 |  |
| To address class imbalance, we compute | weighted precision | , | 𝑖 | = | 1 |  |  |  |  |  |
| number of true instances | 𝑛 | 𝑖 | in each class: | (5) | Mean Absolute Error (MAE). | Some CVSS metrics, like | AV | , |  |  |
| the total number of samples. Reporting both per-class and | MAE | = | \| | 𝑦 | 𝑖 | − | 𝑦 | ˆ | 𝑖 | \| |
| (3) | Recall. | Recall is a measure of ability to identify positive | where | 𝑦 | 𝑖 | and ˆ | 𝑦 | 𝑖 | are the true and predicted ordinal labels, re- |  |
| instances. Weighted recall provides an aggregate measure | spectively, and | 𝑁 | is the total number of samples. This metric |  |  |  |  |  |  |  |
| of recall across all classes by accounting for class imbalance. | reflects not just correctness, but also how far predictions |  |  |  |  |  |  |  |  |  |
| Weighted Recall | = | 𝑛 | 𝑖 | · | Recall | Baseline. | Figure 2 illustrates class imbalances across CVSS base |  |  |  |
| 𝑁 | 𝑖 | = | 1 | metrics. For instance, 83.8% of vulnerabilities are labeled as Low |  |  |  |  |  |  |
| where: | complexity. To quantify this imbalance, the study uses the imbal- |  |  |  |  |  |  |  |  |  |
| 𝑖 | + | 𝐹 𝑁 | is the recall for class | 𝑖 | ance ratio, defined as the number of samples in the majority class |  |  |  |  |  |
| • | 𝑇 𝑃 | 𝑖 | and | 𝐹 𝑁 | 𝑖 | are the number of true positives and false | divided by those in the minority class. A higher ratio signifies |  |  |  |
| negatives for class | 𝑖 | , respectively, | greater disparity, which can negatively affect evaluation metrics |  |  |  |  |  |  |  |
| • | 𝑁 | = | 𝐾 | As shown in Table 2, the dataset exhibits notable class imbalance |  |  |  |  |  |  |
| classes. | across several metrics. | Attack Vector | is the most imbalanced, with |  |  |  |  |  |  |  |
| (4) | F1-Score. | The F1-score is the harmonic mean of precision | the majority class being 63.60 times larger than the minority. In |  |  |  |  |  |  |  |
| and recall, capturing a balance between false positives and | contrast, | Integrity Impact | is the most balanced among the metrics |  |  |  |  |  |  |  |
| Precision | 𝑖 | × | Recall | 𝑖 | tion of severity scores. The presence of class imbalance is evident |  |  |  |  |  |

---

## Page 5

| (a) Attack Complexity | (b) Attack Vector |
| --- | --- |
| (c) Privileges Required | (d) User Interaction |
| (e) Scope | (f) Confidentiality Impact |
| (g) Integrity Impact | (h) Availability Impact |

Figure 2: Distribution of Categories Across CVSS Metrics

moderate correlations also observed between User Interaction and

SAC ’26, March 23–27, 2026, Thessaloniki, Greece

Figure 4: Correlation of Base Metrics

Table 3 summarizes the performance of the LLMs in predicting

CVSS metric labels for CVEs. We analyze each metric individually

before presenting combined results, using both the performance

metrics in Table 3 and the confusion matrices in Figure 5.

6.2 Analysis of Individual LLM Classifiers

Table 3 presents the detailed performance of individual LLMs across

all CVSS and evaluation metrics.

Attack Complexity. GPT-5 achieved the highest accuracy at 84.66%,

slightly above the baseline of 83.85%, with balanced precision (0.72),

strong recall (0.85) and yielding the best F1-score (0.82) between

all models. GPT-4o followed closely (81.92%, F1=0.78) behind. Gem-

ini (80.21%), DeepSeek (79.29%), and Grok(80.13%) all performed

comparably (F1=0.78), with Llama’s performance trailing behind

(77.74%, F1=0.77).

Attack Vector. Gemini led with 89.42% accuracy, surpassing the

72.65% baseline and achieving balanced scores (P=0.82, R=0.83,

F1=0.82). GPT-5 followed at 87.96% (F1=0.88), showing the strongest

recall (0.88) but slightly lower precision. GPT-4o reached 86.57%,

also well above baseline with consistent metrics (F1 = 0.86). Llama

(79.31%) and DeepSeek (79.01%) showed moderate results ( 𝐹 1 =

0 . 76˘0 . 79 ) , while Grok (83.00%) matched Gemini’s stability (F1 =

0.82). Although all models outperformed the baseline, multiple

showed a bias toward the majority class, often predicting NET-

WORK over minority classes like LOCAL.

Privileges Required. GPT-5 performed the best, with 71.61% accu-

tency in other metrics (P=0.76, R=0.72, F1=0.70). Gemini followed

(69.74%, F1=0.63) with GPT-4o (65.44%, F1=0.64) and Grok (64.75%,

two classes.

| Figure 3: Distribution of Categories for Severity | racy in comparison to the 49.51% baseline, and maintained consis- |  |
| --- | --- | --- |
| Correlation analysis. | We use Cramer’s V to assess relationships | F1=0.63) behind. Llama (58.69%) and DeepSeek (58.49%) had the |
| between categorical CVSS metrics. Results indicate a moderate | weakest results. There was a pattern of confusion between LOW |  |
| to strong correlation between Integrity and Confidentiality, with | and NONE levels, as models struggled to differentiate between the |  |
| Integrity, and between Integrity and Availability. Other metric pairs | User Interaction. | GPT-5 achieved the top accuracy (88.95%) and |
| show weak or negligible associations (See Figure 4). | highest overall balance (P=0.89, R=0.89, F1=0.89), outperforming |  |

---

## Page 6

| SAC ’26, March 23–27, 2026, Thessaloniki, Greece | Jafarikhah et al. |  |  |
| --- | --- | --- | --- |
| (a) Attack Complexity | (b) Attack Vector | (c) Privileges Required | (d) User Interaction |
| (e) Scope | (f) Confidentiality Impact | (g) Integrity Impact | (h) Availability Impact |

Figure 5: Confusion Matrices for CVSS metrics for GPT-5, the best performing model, per metric

the 63.26% baseline. Gemini (87.85%, F1=0.82) and GPT-4o remained

competitive (84.13%, F1 = 0.84), with Grok (82.58%, F1=0.82) follow-

ing behind. DeepSeek (75.18%, F1=0.73) and Llama (77.67%, F1=0.77)

once again had the weakest performance. Errors frequently in-

volved mislabeling REQUIRED as NONE, showing class bias across

models.

Scope. GPT-5 led with 76.68% accuracy, above the 67.84% base-

line, achieving F1 = 0.77 with good recall (0.77). Grok (76.06%)

and Gemini (71.25%) also showed balanced outputs (F1=0.75). GPT-

4o performed stably (72.86%, F1=0.73), while DeepSeek (70.36%,

F1=0.68) and Llama (69.48%, F1=0.70) trailed. Most models favored

the majority UNCHANGED class.

Confidentiality Impact. GPT-5 attained the best performance

(76.05%) over the 45.36% baseline, with all metrics at 0.76, indicating

consistent predictions. Gemini (74.01%) also performed accurately, Figure 6: Distribution of Description Length (median=271)

though its other metrics were lower than GPT-5 at 0.65. and GPT-

4o (66.96%) followed, while Grok (65.40%) and DeepSeek (60.27%)

remained moderate. Llama performed weakest (56.47%, F1=0.57).

while DeepSeek (51.86%) and Llama (51.13%) underperformed, both

There was overall difficulty distinguishing between LOW and HIGH

exhibiting an MAE >= 0.7.

impact, although GPT-5’s higher accuracy suggests better contex-

tual understanding.

6.3 Analysis of the content of “description” field

Integrity Impact. GPT-5 again outperformed other models with

| 78.10% accuracy (F1=0.78), well above the 37.30% baseline. Gemini | Length of Description. | The distribution of the length of the de- |
| --- | --- | --- |
| (75.38%) and Grok (68.24%) followed closely (F1=0.68), while GPT- | scriptions is shown in Figure 6. The mean length is 361 characters |  |
| 4o (69.54%) performed steadily (F1 = 0.69). DeepSeek (56.58%) and | and the median length is 271. The maximum length of the char- |  |
| Llama (55.65%) were the weakest performers. | acters is 3810 and the minimum was 28. The calculated Pearson | 𝑟 |
| Availability Impact. | GPT-5 led with 67.95% accuracy (F1=0.62) | indicated no strong correlation between description length and a |
| versus the 39.65% baseline, though this was its weakest metric | model’s prediction accuracy. |  |
| (MAE=0.41). Gemini (66.06%, F1=0.55) followed. GPT-4o (61.84%, | Named Entities in the Description. | To further assess the inter- |
| F1=0.57) and Grok (60.41%, F1=0.55) showed comparable trends, | action of quality of vulnerability descriptions and predictability, we |  |

extracted named entities using the spaCy Python library, focusing

---

## Page 7

SAC ’26, March 23–27, 2026, Thessaloniki, Greece

| Metric Name | Model | Accuracy (%) | Precision | Recall | F1 | MAE | Baseline (%) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G4 | 81.92 | 0.77 | 0.82 | 0.78 | 0.18 | 83.85 |  |
| Attack Complexity | G5 | 84.66 | 0.72 | 0.85 | 0.82 | 0.15 |  |
| L | 77.74 | 0.75 | 0.79 | 0.77 | 0.44 |  |  |
| GM | 80.21 | 0.77 | 0.80 | 0.78 | 0.20 |  |  |
| DS | 79.29 | 0.77 | 0.79 | 0.78 | 0.21 |  |  |
| GR | 80.13 | 0.77 | 0.80 | 0.78 | 0.20 |  |  |
| G4 | 86.57 | 0.73 | 0.87 | 0.86 | 0.23 | 72.65 |  |
| Attack Vector | G5 | 87.96 | 0.81 | 0.88 | 0.88 | 0.17 |  |
| L | 79.31 | 0.82 | 0.80 | 0.79 | 0.67 |  |  |
| GM | 89.42 | 0.82 | 0.83 | 0.82 | 0.29 |  |  |
| DS | 79.01 | 0.78 | 0.79 | 0.76 | 0.38 |  |  |
| GR | 83.00 | 0.82 | 0.83 | 0.82 | 0.29 |  |  |
| G4 | 65.44 | 0.67 | 0.65 | 0.64 | 0.40 | 49.51 |  |
| Privileges Required | G5 | 71.61 | 0.76 | 0.72 | 0.70 | 0.33 |  |
| L | 58.69 | 0.58 | 0.59 | 0.57 | 0.84 |  |  |
| GM | 69.74 | 0.65 | 0.64 | 0.63 | 0.42 |  |  |
| DS | 58.49 | 0.62 | 0.59 | 0.53 | 0.52 |  |  |
| GR | 64.75 | 0.65 | 0.64 | 0.63 | 0.42 |  |  |
| G4 | 84.13 | 0.84 | 0.84 | 0.84 | 0.16 | 63.26 |  |
| User Interaction | G5 | 88.95 | 0.89 | 0.89 | 0.89 | 0.11 |  |
| L | 77.67 | 0.78 | 0.78 | 0.77 | 0.23 |  |  |
| GM | 87.85 | 0.82 | 0.82 | 0.82 | 0.18 |  |  |
| DS | 75.18 | 0.76 | 0.75 | 0.73 | 0.25 |  |  |
| GR | 82.58 | 0.82 | 0.82 | 0.82 | 0.18 |  |  |
| G4 | 72.86 | 0.73 | 0.73 | 0.73 | 0.27 | 67.84 |  |
| Scope | G5 | 76.68 | 0.73 | 0.77 | 0.77 | 0.23 |  |
| L | 69.48 | 0.70 | 0.70 | 0.70 | 1.20 |  |  |
| GM | 71.25 | 0.75 | 0.76 | 0.75 | 0.24 |  |  |
| DS | 70.36 | 0.68 | 0.71 | 0.68 | 0.29 |  |  |
| GR | 76.06 | 0.75 | 0.76 | 0.75 | 0.24 |  |  |
| G4 | 66.96 | 0.69 | 0.67 | 0.67 | 0.41 | 45.36 |  |
| Confidentiality Impact | G5 | 76.05 | 0.76 | 0.76 | 0.76 | 0.29 |  |
| L | 56.47 | 0.60 | 0.57 | 0.57 | 0.73 |  |  |
| GM | 74.01 | 0.65 | 0.65 | 0.65 | 0.46 |  |  |
| DS | 60.27 | 0.66 | 0.60 | 0.57 | 0.56 |  |  |
| GR | 65.40 | 0.65 | 0.65 | 0.65 | 0.46 |  |  |
| G4 | 69.54 | 0.70 | 0.70 | 0.69 | 0.40 | 37.30 |  |
| Integrity Impact | G5 | 78.10 | 0.78 | 0.78 | 0.78 | 0.29 |  |
| L | 55.65 | 0.58 | 0.56 | 0.55 | 0.81 |  |  |
| GM | 75.38 | 0.68 | 0.68 | 0.68 | 0.44 |  |  |
| DS | 56.58 | 0.66 | 0.57 | 0.55 | 0.62 |  |  |
| GR | 68.24 | 0.68 | 0.68 | 0.68 | 0.44 |  |  |
| G4 | 61.84 | 0.57 | 0.62 | 0.57 | 0.52 | 39.65 |  |
| Availability Impact | G5 | 67.95 | 0.62 | 0.68 | 0.62 | 0.41 |  |
| L | 51.13 | 0.49 | 0.52 | 0.48 | 1.11 |  |  |
| GM | 66.06 | 0.56 | 0.60 | 0.55 | 0.57 |  |  |
| DS | 51.86 | 0.57 | 0.52 | 0.46 | 0.74 |  |  |
| GR | 60.41 | 0.56 | 0.60 | 0.55 | 0.57 |  |  |
| G4 | 73.04 | 0.73 | 0.74 | 0.72 | 0.32 | 57.40 |  |
| Overall | G5 | 78.99 | 0.75 | 0.79 | 0.78 | 0.25 |  |
| L | 65.77 | 0.66 | 0.66 | 0.65 | 0.75 |  |  |
| GM | 76.74 | 0.77 | 0.77 | 0.76 | 0.28 |  |  |
| DS | 66.38 | 0.67 | 0.67 | 0.63 | 0.45 |  |  |
| GR | 66.38 | 0.71 | 0.72 | 0.71 | 0.35 |  |  |

Table 3: Comparison of model performance across all CVSS v3.1 base metrics. Each block lists six model abbreviations (GPT-4o

= G4, GPT-5 = G5, Llama = L, Gemini = GM, DeepSeek = DS, Grok = GR). The Baseline column shows the metric’s baseline

accuracy.

---

## Page 8

| SAC ’26, March 23–27, 2026, Thessaloniki, Greece | Jafarikhah et al. |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| specifically on entities of type ORG (organizations) and PRODUCT, | features allowed the meta-classifier to capture whether a prediction |  |  |  |  |
| while excluding PERSON, DATE, and GPE. We then computed the | was broadly supported or driven by a single model. Finally, we |  |  |  |  |
| Pearson correlation coefficient between the number of named enti- | added simple reliability indicators, including binary flags denoting |  |  |  |  |
| ties and classification accuracy. The resulting correlation was 0.048 | whether each model produced a valid (non- | UNKNOWN | ) output, with |  |  |
| with a | 𝑝 | -value | < | 0.05, indicating a weak or negligible relationship | future extensions planned for weighting models based on their |
| between the two variables. There was no meaningful correlation | historical performance. Together, these features provided a balance |  |  |  |  |
| between the number of named entities in a description and the | of raw predictions, inter-model dynamics, and reliability cues. |  |  |  |  |

precision of the classification.

| Information Contents. | We computed the information content | 6.4.2 | Meta Classifier Architectures. | On top of this feature set, we |
| --- | --- | --- | --- | --- |
| (IC) of each description using the Semantic Correlation formula as | evaluated several ensemble architectures to determine how best to |  |  |  |
| proposed in prior work on intrinsic IC measures [26]. However, we | combine the information for each CVSS metric.The experiments |  |  |  |
| found no strong correlation between IC and the model’s precision, | included both traditional and modern classifiers: |  |  |  |
| suggesting that IC alone is not a determining factor in predictive | • | Voting Ensemble | : A soft-voting method that averaged prob- |  |
| performance. | ability distributions from multiple base learners. |  |  |  |

• Random Forest : A tree-based approach that provided fea-

| 6.4 | Meta-LLM Classifiers | ture importance analysis. |  |  |  |
| --- | --- | --- | --- | --- | --- |
| As shown in Table 3, different LLMs exhibit varying levels of perfor- | • | Gradient Boosting | : Another tree-based method, optimized |  |  |
| mance across CVSS metrics. For instance, GPT-5 performs best on | through sequential error correction. |  |  |  |  |
| Attack Complexity | , whereas Gemini achieves the highest accuracy | • | Logistic Regression | : A linear model offering interpretable |  |
| on | Attack Vector | classification. To further explore this variability, | coefficients. |  |  |
| we analyzed the overlap in misclassifications among the models. | • | Support Vector Machine (SVM) | : Employed with an RBF |  |  |
| Figure 7 shows that a large portion of misclassifications are shared | kernel to capture non-linear decision boundaries in high- |  |  |  |  |
| across models. For instance, all LLMs incorrectly classified 28.7% | dimensional feature space. |  |  |  |  |
| of the same CVEs for | Availability Impact | . Likewise, in 17.9% of | • | Neural Network | : A multi-layer perceptron with two hidden |
| the cases, all models misclassified | Attack Complexity | , and in 35.8% | layers (100 and 50 neurons), trained with early stopping to |  |  |
| of the cases, the majority of models (four out of six) produced | prevent overfitting. |  |  |  |  |
| incorrect labels. Nevertheless, we examined whether combining | This diverse set of models ensured that the meta-classifier eval- |  |  |  |  |
| multiple classifiers could enhance performance by exploiting their | uation was not tied to any single learning paradigm, but instead |  |  |  |  |
| complementary strengths and mitigating individual errors. | explored how different ensemble strategies could exploit the com- |  |  |  |  |

plementary strengths of the underlying LLMs.

6.4.3 Model Training and Evaluation. To ensure robust evaluation,

we adopted a stratified 5-fold cross-validation strategy that pre-

served class distributions across folds. Model performance was as-

sessed using standard metrics including accuracy, precision, recall,

F1-score, and AUC for binary classification tasks. For each CVSS

metric, the model yielding the highest cross-validation F1-score

was selected for further testing.

In addition to cross-validation, we employed a conventional

train–test split, allocating 80% of the data for training and reserving

20% as a held-out test set. Stratified sampling was again applied

to maintain representative class distributions across both sets, en-

abling a fair and consistent evaluation of generalization perfor-

mance.

Figure 7: Misclassifications of CVEs across LLMs. Bottom bars

show errors by individual models, while red bars indicate 6.4.4 Meta-classifier Results. The performance of the individual

CVEs misclassified by all models. LLMs served as a baseline, with GPT-5 generally outperforming

other models across most CVSS metrics. However, as shown in

| 6.4.1 | Feature Engineering. | To enable meta-classification, we con- | Table 4, the meta-classifier consistently exceeded the strongest |
| --- | --- | --- | --- |
| structed a feature engineering pipeline that converts raw LLM | individual results. For example, Support Vector Machines proved |  |  |
| predictions into richer representations. The most direct features | most effective for metrics such as Privileges Required, Confiden- |  |  |
| were the categorical predictions from six LLM models we used, | tiality Impact, and User Interaction, while Random Forest showed |  |  |
| which were encoded numerically to facilitate downstream learning. | gains for Attack Vector and Availability Impact. Neural Networks |  |  |
| Beyond these base encodings, we incorporated measures of model | exceeded model performance for Scope and Integrity Impact, and |  |  |
| agreement, such as the proportion of pairwise consensus among | although the difference was slim, +0.24, Logistic Regression was |  |  |
| models, the majority-vote class, and the relative strength of that | able to further improve on an already high-scoring metric, Attack |  |  |
| consensus expressed as a confidence score. These agreement-based | Complexity. |  |  |

---

## Page 9

from ensemble integration highlights the robustness of the ap-

and Attack Vector (+1.03%), showing that even high-performing in-

dividual metrics could still be enhanced through meta-classification.

can progressively enhance the reliability of automated vulnera-

Our evaluation of individual LLM models and meta-classifiers for

automated CVSS scoring reveals several important findings about

their performance, limitations, and the characteristics of the vul-

nerability descriptions:

User Interaction, reflecting strong capabilities in identifying remote

performance on Availability Impact and Privileges Required high-

lights persistent challenges in impact-related dimensions. The meta-

classifier further enhanced overall classification accuracy across all

eight metrics by integrating the strengths of all six models, yielding

the most significant improvement on the Scope metric.

83% of the samples are labeled as Low . Even the best-performing

SAC ’26, March 23–27, 2026, Thessaloniki, Greece

Accuracy

of 1,000 CVEs from 2024. Despite providing additional structure,

only prompts, suggesting that most relevant information is already

captured in the textual description. As a result, incorporating addi-

tional structured data does not substantially improve classification

accuracy. In contrast, adding the CVE ID yielded a large but mislead-

ing performance increase, as models used the identifier to retrieve

known CVSS vectors rather than infer them. To preserve the in-

Some overlap with pretraining data is possible, since older CVSS

records may appear in public corpora. We removed CVE identifiers

to limit direct memorization, but partial exposure cannot be ruled

out. However, model behavior indicates that recall alone does not

drive predictions: performance degrades when key contextual cues

are missing. Thus, CVSS scoring depends on contextual reasoning

of misclassified CVEs:

Table 4: Comparison of LLMs vs Best Meta Classifier with Baseline and Change compared to best individual LLM. Meta Models:

LR = Logistic Regression, RF = Random Forest, SVM = Support Vector Machine, NN = Neural Network, NM = Naive Bayes Model

| CVSS Metric | Baseline | GPT-4 | GPT-5 | LLaMA | Grok3 | Gemini | DeepSeek | Best Meta | Meta Model | Change |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Attack Complexity | 83.24 | 81.44 | 83.94 | 76.95 | 79.02 | 79.58 | 78.80 | 84.19 | LR | +0.24 |  |
| Attack Vector | 73.16 | 86.81 | 88.29 | 79.10 | 82.70 | 89.27 | 79.77 | 90.30 | RF | +1.03 |  |
| Availability Impact | 39.41 | 60.80 | 67.08 | 49.64 | 58.82 | 64.97 | 51.54 | 67.37 | RF | +0.29 |  |
| Confidentiality Impact | 45.20 | 66.23 | 75.68 | 55.37 | 64.28 | 73.35 | 59.81 | 76.45 | SVM | +0.77 |  |
| Integrity Impact | 37.37 | 68.71 | 77.71 | 54.45 | 67.07 | 74.73 | 56.34 | 78.10 | NN | +0.39 |  |
| Privileges Required | 49.95 | 65.16 | 71.44 | 58.72 | 63.70 | 69.32 | 58.71 | 72.23 | SVM | +0.80 |  |
| Scope | 68.28 | 72.29 | 76.04 | 69.44 | 75.25 | 71.19 | 70.43 | 79.12 | NN | +3.08 |  |
| User Interaction | 64.40 | 83.63 | 88.36 | 77.19 | 81.85 | 87.02 | 75.55 | 88.55 | SVM | +0.19 |  |
| Overall, the meta-classifier achieved an average accuracy of | LLM, GPT-5, achieved less than a 1% improvement over the base- |  |  |  |  |  |  |  |  |  |  |
| 79.54%, surpassing GPT-5’s 78.55%. While the margin of improve- | line. This highlights the inherent bias that classifiers exhibit when |  |  |  |  |  |  |  |  |  |  |
| ment may appear modest, the fact that every CVSS metric benefited | trained on imbalanced data distributions. |  |  |  |  |  |  |  |  |  |  |
| proach. Particularly notable were improvements in Scope (+3.08%) | 7.3 | Quality of Description and Predictive |  |  |  |  |  |  |  |  |  |
| These findings suggest that meta-classification provides a sys- | We used three proxies to assess description informativeness: (1) |  |  |  |  |  |  |  |  |  |  |
| tematic advantage by leveraging the complementary strengths of | count of named entities (ORG, PRODUCT), (2) text length, and |  |  |  |  |  |  |  |  |  |  |
| different LLMs while mitigating the risk of poor performance on | (3) Information Content. The Pearson correlation between named |  |  |  |  |  |  |  |  |  |  |
| specific metrics. Although impact-related dimensions (Availability, | entities and accuracy for GPT was low ( | 𝑟 | = | 0 | . | 048, | 𝑝 | < | 0 | . | 05). Longer |
| Confidentiality, and Integrity) remain inherently more challenging, | descriptions nor higher IC did not correlate with higher perfor- |  |  |  |  |  |  |  |  |  |  |
| the observed improvements demonstrate that ensemble approaches | mance, suggesting verbosity is not a strong quality signal. |  |  |  |  |  |  |  |  |  |  |
| bility assessment. Furthermore, since comparable LLMs tend to | 7.4 | Additional Fields and Predictive Accuracy |  |  |  |  |  |  |  |  |  |
| make similar errors, providing clearer vulnerability descriptions | We investigated whether supplemental contextual features, includ- |  |  |  |  |  |  |  |  |  |  |
| and richer contextual information can further improve the accuracy | ing CPE, CWE ID, and CVE ID, could improve model performance |  |  |  |  |  |  |  |  |  |  |
| and consistency of CVSS scoring automation. | by comparing them with description-only prompts on a subset |  |  |  |  |  |  |  |  |  |  |
| 7 | Findings | CPE and CWE data produced results comparable to description- |  |  |  |  |  |  |  |  |  |
| 7.1 | Performance Across CVSS Metrics | tegrity of our evaluation, subsequent experiments omitted CWE |  |  |  |  |  |  |  |  |  |
| Among the evaluated models, GPT-5, Gemini, and Grok demon- | and CPE fields for redundancy reasons and excluded CVE IDs to |  |  |  |  |  |  |  |  |  |  |
| strated the strongest overall performance across the CVSS base met- | prevent lookup bias. The final experimental setup therefore relied |  |  |  |  |  |  |  |  |  |  |
| rics. The highest accuracies were observed for Attack Vector and | solely on human-readable CVE descriptions as model input. |  |  |  |  |  |  |  |  |  |  |
| access conditions and user involvement cues. In contrast, lower | 8 | Discussion and Future Work |  |  |  |  |  |  |  |  |  |
| 7.2 | Performance vs. Baseline | rather than surface-pattern memorization, as models infer well |  |  |  |  |  |  |  |  |  |
| Overall, the classifiers struggled in scenarios with extreme class | from subtle signals but fail when essential information is absent. To |  |  |  |  |  |  |  |  |  |  |
| imbalance—for example, in the case of Attack Complexity, where | search into this, we asked GPT-4o two questions for a small sample |  |  |  |  |  |  |  |  |  |  |

---

## Page 10

| SAC ’26, March 23–27, 2026, Thessaloniki, Greece | Jafarikhah et al. |  |  |
| --- | --- | --- | --- |
| • | Why did you misclassify this CVE description? | [8] | Forum of Incident Response and Security Teams (FIRST). 2025. Common vulner- |
| • | What additional information would help predict the correct | ability scoring system (cvss). https://www.first.org/cvss/. Accessed: 2025-10-09. |  |

(2025).

labels? [9] Jerry Gamblin. 2025. 2024 CVE Data Review. https://jerrygamblin.com/2025/01

Main groups of reasons provided by the model for misclassifica- /05/2024-cve-data-review. Accessed: 2025-10-05. (Jan. 2025).

[10] Shai Gretz et al. 2023. Zero-shot topical text clas-

tions include: sification with LLMs-an experimental study. In

• Missing Information: Descriptions often omit crucial details, Findings of the Association for Computational Linguistics: EMNLP 2023,

9647–9676.

| such as required privileges, user interaction, or configuration | [11] | Matt Kapko. 2024. Critical CVEs are going under-analyzed as NIST falls behind. |  |
| --- | --- | --- | --- |
| dependencies. | Cybersecurity Dive. https://www.cybersecuritydive.com/news/nist-cve-analy |  |  |
| • | Ambiguous Language: | Phrases like “arguments can be pro- | sis-gap/717226/. |

[12] Elyes Manai, Mohamed Mejri, and Jaouhar Fattahi. 2024. Helping CNAs Gen-

| vided” or “introduce properties” mislead the model into de- | erate CVSS Scores Faster and More Confidently Using XAI. Applied Sciences, |
| --- | --- |
| faulting to low complexity and no privileges. | 14, 20, 9231. |

[13] Francesco Marchiori, Denis Donadel, and Mauro Conti. 2025. Can LLMs

• Training Bias: The model overgeneralizes from similar past Classify CVEs? Investigating LLMs Capabilities in Computing CVSS Vectors.

examples, applying incorrect heuristics in nuanced cases. arXiv preprint arXiv:2504.10713. https://arxiv.org/abs/2504.10713.

[14] Inc. Meta Platforms. 2024. Introducing Meta Llama 3. https://ai.meta.com/blog

| Furthermore, despite the improvements in accuracy made by the | /meta-llama-3/. (2024). |  |
| --- | --- | --- |
| meta-classifier, the largest change was only +3.08. This suggests | [15] | Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy |
| that classifiers make no inherent difference to performance, and | Bengio, and Mehrdad Farajtabar. 2024. GSM-Symbolic: Understanding the |  |

Limitations of Mathematical Reasoning in Large Language Models. (2024).

| that enriching CVE descriptions with proper context is the most | https://openreview.net/forum?id=AjXkRZIvjB. |  |
| --- | --- | --- |
| vital factor for accurate scoring. We plan to augment descriptions | [16] | Jonathan Munshaw. 2024. What’s the Deal with the Massive Backlog of Vul- |
| with external context ( e.g., libraries involved, dependency graphs, | nerabilities at the NVD? Accessed: 2025-05-23. (Apr. 2024). https://blog.talosin |  |

telligence.com/nvd-vulnerability-backlog-the-need-to-know/.

and proof-of-concept exploits where available) to better capture [17] National Institute of Standards and Technology. 2022. CVEs and the NVD

impact and improve model predictions. Process. https://nvd.nist.gov/general/cve- process. Accessed: 2025-05-29.

(2022).

[18] National Institute of Standards and Technology. 2025. National vulnerability

9 Conclusion database (nvd). https://nvd.nist.gov/. Accessed: 2025-10-09. (2025).

[19] Chris Nichols, Geoff Stoker, and Ulku Clark. 2021. Heuristic Evaluation of Vul-

| This study evaluated the feasibility of using general-purpose LLMs, | nerability Risk Management Leaders’ Presentations of Cyber Threat and Cyber |
| --- | --- |
| including GPT-4o, GPT-5, Llama-3.3-70B-Instruct, Gemini-2.5-Flash, | Risk. In International Conference on Human-Computer Interaction. Springer, |
| DeepSeek-R1, and Grok-3, to automate CVSS v3.1 base metric clas- | 212–225. |

[20] National Institute of Standards and Technology. 2024. NVD News. NIST. (2024).

| sification from vulnerability descriptions. Across more than 31,000 | https://www.nist.gov/itl/nvd/nvd-news. |  |
| --- | --- | --- |
| CVEs, GPT-5 and Gemini-2.5-Flash showed the strongest over- | [21] | OpenAI. 2025. Best Practices for Prompt Engineering with the OpenAI |
| all performance, particularly for metrics such as Attack Vector | API. https://help.openai.com/en/articles/6654000-best-practices-for-prompt- |  |

engineering-with-the-openai-api. (2025).

| and User Interaction. However, all models struggled with minority | [22] | OpenAI. 2024. Hello GPT-4o. https://openai.com/index/hello-gpt-4o/. (2024). |
| --- | --- | --- |
| classes and were sensitive to class imbalance and ambiguous descrip- | [23] | OpenAI. 2025. Introducing GPT-5. https://openai.com/index/introducing-gpt-5 |

/. (2025).

| tions. The meta-classifier offered only modest accuracy improve- | [24] | CVE Project. 2025. CVE List V5. https://github.com/CVEProject/cvelistV5. |
| --- | --- | --- |
| ments, indicating that fine-tuning and domain-specific enhance- | (2025). |  |
| ments remain necessary. Overall, our findings show that LLMs can | [25] | Colin Raffel et al. 2020. Exploring the limits of transfer learning with a unified |

text-to-text transformer. Journal of Machine Learning Research, 21, 140.

| support scalable vulnerability triage but also reveal key limitations | [26] | Nuno Seco, Tony Veale, and Jer Hayes. 2004. An intrinsic information content |
| --- | --- | --- |
| that must be addressed. Future work should explore instruction | metric for semantic similarity in WordNet. In ECAI. Vol. 16. Citeseer, 1089– |  |
| tuning and the integration of external contextual signals to further | 1090. |  |

[27] The Record Staff. 2024. NIST expects to clear backlog in vulnerabilities database

| improve prediction reliability in operational settings. All project | by end of fiscal year. The Record. https://therecord.media/nist-nvd-backlog-cl |
| --- | --- |
| code and data have been released as open-source materials [4]. | ear-end-fiscal-2024. |

[28] Andrew Kyle Threatt, Jillian Glyder, Lance Adams, Randy Franks, and

Geoff Stoker. 2021. Some Analysis of Common Vulnerabilities and Ex-

| References | posures (CVE) Data from the National Vulnerability Database (NVD). |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [1] | Md Tanvirul Alam, Dipkamal Bhusal, Le Nguyen, and Nidhi Rastogi. 2024. | Proceedings of CONISAR 2021. |  |  |  |  |  |  |  |  |  |
| CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence. | [29] | Saad Ullah, Mingji Han, Saurabh Pujar, Hammond Pearce, Ayse Coskun, and |  |  |  |  |  |  |  |  |  |
| Proceedings of the Conference on NeurIPS 2024. https://arxiv.org/abs/2406.0 | Gianluca Stringhini. 2024. LLMs Cannot Reliably Identify and Reason About |  |  |  |  |  |  |  |  |  |  |
| 7599. | Security Vulnerabilities (Yet?): A Comprehensive Evaluation, Framework, and |  |  |  |  |  |  |  |  |  |  |
| [2] | Tom B. Brown, Benjamin Mann, Nick Ryder, et al. 2020. Language models are | Benchmarks. arXiv preprint arXiv:2312.12575. https://ieeexplore.ieee.org/doc |  |  |  |  |  |  |  |  |  |
| few-shot learners. Advances in Neural Information Processing Systems, 33. | ument/10646663. |  |  |  |  |  |  |  |  |  |  |
| [3] | Francesco Cipollone. 2024. The NVD Crisis: Format Changes, Delays, and a | [30] | Steven J. Vaughan-Nichols. 2024. NVD slowdown leaves thousands of vulnera- |  |  |  |  |  |  |  |  |
| Growing Backlog. LinkedIn. (2024). https://www.linkedin.com/pulse/nvd-crisi | bilities without analysis data. The Register, (Mar. 2024). https://www.theregist |  |  |  |  |  |  |  |  |  |  |
| s-format-changes-delays-growing-backlog-cipollone-1lrpf/. | er.com/2024/03/22/opinion_column_nist/. |  |  |  |  |  |  |  |  |  |  |
| [4] | Eva Deans, Daniel Thompson, and Hossein Siadati. 2025. Description to score | [31] | Julia Wunder, Andreas Kurtz, Christian Eichenmüller, Freya Gassmann, and |  |  |  |  |  |  |  |  |
| AI vulnerability analysis. GitHub repository. (2025). https://github.com/ecdean | Zinaida Benenson. 2024. Shedding light on CVSS scoring inconsistencies: |  |  |  |  |  |  |  |  |  |  |
| s/DescriptionToScore_AIVulnAnalysis. | A user-centric study on evaluating widespread security vulnerabilities. In |  |  |  |  |  |  |  |  |  |  |
| [5] | Google DeepMind. 2025. Gemini Flash. https://deepmind.google/models/gemi | 2024 IEEE Symposium on Security and Privacy (SP). IEEE, 1102–1121. |  |  |  |  |  |  |  |  |  |
| ni/flash/. (2025). | [32] | xAI. 2025. Grok 3 Beta — The Age of Reasoning Agents. https://x.ai/news/grok |  |  |  |  |  |  |  |  |  |
| [6] | DeepSeek. 2025. DeepSeek-R1 Release. https://api-docs.deepseek.com/news/n | -3. (2025). |  |  |  |  |  |  |  |  |  |
| ews250120. (2025). | [33] | Remi Yazigi. 2025. Modernizing Vulnerability Prioritization: Automated Risk |  |  |  |  |  |  |  |  |  |
| [7] | FIRST.org, Inc. 2019. CVSS v3.1 Specification Document. https://www.first.org | Scoring Using Generative AI. Authorea Preprints. |  |  |  |  |  |  |  |  |  |
| /cvss/v3-1/specification-document. Accessed: 2025-05-29. (2019). | [34] | Yazhou | Zhang, | Mengyao | Wang, | Qiuchi | Li, | Prayag | Tiwari, | and | Jing |

Qin. 2025. Pushing the limit of LLM capacity for text classification. In

Companion Proceedings of the ACM on Web Conference 2025, 1524–1528.

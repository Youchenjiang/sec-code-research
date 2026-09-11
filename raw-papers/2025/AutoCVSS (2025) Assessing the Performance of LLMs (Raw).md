---
title: "V_M_AutoCVSS_2025"
creator: "LaTeX with hyperref"
pages: 12
---

# V_M_AutoCVSS_2025

> **總頁數**：12 頁

---

## Page 1

AutoCVSS: Assessing the Performance of LLMs

for Automated Software Vulnerability Scoring

1 2 1

Davide Sanvito , Giovanni Arriciati , Giuseppe Siracusano ,

1 2

Roberto Bifulco , Michele Carminati

1

2

The growing volume of daily disclosed soft-

ing, becoming shorter than the analysis time

and increasing the window of opportunity for

attackers. This study explores leveraging Large

Language Models (LLMs) for automating vul-

tated data, such as during the transition to new

versions of the standard, LLMs are the only

viable approach, highlighting their value in im-

1 Introduction

NEC Laboratories Europe, Heidelberg, Germany

Politecnico di Milano, Milano, Italy

scale of 0 to 10 (NVD, 2024a). Both the individ-

Aghaei et al., 2022) highlighted a delay of sev-

eral days between CVE announcements and the

publication of corresponding CVSS scores that pre-

in 2023 (Pan et al., 2024). In contrast, attackers

are acting faster: the average time to exploit vul-

day they are published (Qualys, 2023), extending

the window of opportunity for attackers.

| Abstract | in Table 1), and calculate the | Severity Score | on a |  |
| --- | --- | --- | --- | --- |
| ware vulnerabilities imposes significant pres- | ual metrics and the aggregated severity score are |  |  |  |
| sure on security analysts, extending the time | critical components of various stages of vulnerabil- |  |  |  |
| needed for analysis - an essential step for ac- | ity management, e.g., risk assessment, mitigation |  |  |  |
| curate risk prioritization. Meanwhile, the time | planning, and incident response. |  |  |  |
| between disclosure and exploitation is reduc- | However, previous studies (Costa et al., 2022; |  |  |  |
| nerability risk score prediction using the indus- | vents timely vulnerability management. This is- |  |  |  |
| trial CVSS standard. From our analysis across | sue is exacerbated by the growing volume of pub- |  |  |  |
| different data availability scenarios, LLMs can | lished vulnerabilities that significantly increases |  |  |  |
| effectively complement supervised baselines in | analysts’ burden: the median manual analysis de- |  |  |  |
| data-scarce settings. In the absence of any anno- | lay increased from 2.7 days in 2019 to 8.2 days |  |  |  |
| proving vulnerability management. We make | nerabilities has decreased sharply, from 44 days in |  |  |  |
| the source code of AutoCVSS public at | https: | 2019 to just 5 days in 2023 (Google, 2024), with |  |  |
| //github.com/nec-research/AutoCVSS | . | 25% of high-risk vulnerabilities exploited on the |  |  |
| Over the past 25 years, the Common Vulnerabil- | To mitigate these delays, several works have |  |  |  |
| ities and Exposures (CVE) program established | proposed automating CVSS score assignment for |  |  |  |
| as the de–facto standard to identify and catalog | new CVEs using Natural Language Processing |  |  |  |
| publicly-disclosed software vulnerabilities (CVE, | (NLP). Most approaches rely on supervised learn- |  |  |  |
| 2024b). In this context, the number of CVE records | ing, which require annotated data. Although the |  |  |  |
| have steadily increased over the past decade, with | NVD hosts hundreds of thousands of CVEs (NVD, |  |  |  |
| a 38% rise from 2023 to 2024 (CVE, 2024a). To | 2024f), multiple CVSS versions have been released |  |  |  |
| help organizations manage this growing volume | over time and not all records include CVSS val- |  |  |  |
| and effectively assess risk, the National Vulner- | ues for every version (NVD, 2024a). Specification |  |  |  |
| ability Database | (NVD, 2024e) enhances CVE | updates hinder the rapid adaptation of these tech- |  |  |
| records with severity scores using the Common | niques until sufficient data labeled in the new for- |  |  |  |
| Vulnerability Scoring System (CVSS), a widely | mat becomes available. This issue is particularly |  |  |  |
| adopted industrial standard (FIRST, 2024b). Se- | critical during version transitions, such as the re- |  |  |  |
| curity experts, mainly associated with NVD, man- | cent release of CVSS v4.0 (FIRST, 2023c), when |  |  |  |
| ually assess the severity of new vulnerabilities by | annotated data for the new version is scarce. |  |  |  |
| relying on detailed information from CVE records | Large Language Models (LLMs) have demon- |  |  |  |
| and publicly available data: they compute eight | strated remarkable performance across various |  |  |  |
| CVSS Metrics | (FIRST, 2023b), concisely repre- | NLP tasks | (Yang et al., 2024). | Leveraging the |
| sented as | CVSS Vectors | (an example is provided | textual CVE descriptions, this study explores the |  |

---

## Page 2

feasibility of employing LLM-based approaches Table 1: List of metrics and possible values, sorted

to develop a robust and scalable solution for au-

tomating CVSS prediction. We evaluate different

prompting strategies, spanning zero-shot to few-

ation (RAG) techniques. We consider both open-

recent Large Reasoning Models (LRMs) variants,

surpassed by supervised baselines fine-tuned for

the specific CVSS prediction task.

based on the most recent encoder-only models per-

form best. However, when admitting a hybrid ap-

proach, LLMs can complement them by offering

better prediction performance on half of the CVSS

metrics, overall achieving better results.

③ With extremely scarce or unavailable data (e.g.,

transitioning to v4.0), LLMs remain effective with

minimal prompt adaptations to align with the new

specification. Although their performance is lower

than previous scenarios due to reliance on zero-shot

settings, LLMs still aid analysts by outperforming

conservative worst-case approaches. Additionally,

they facilitate the adoption of new CVSS versions

by providing initial predictions, even in the absence

of labeled v4.0 data. Then, as more labeled data be-

comes available, the approach can evolve to more

effective hybrid or fully-supervised methods, en-

hancing accuracy and scalability.

These findings demonstrate the practical poten-

tial of LLMs to address vulnerability risk prioriti-

zation and their suitability for real-world applica-

tions, significantly contributing to automating and

streamlining vulnerability management processes.

To facilitate reproducibility and further research,

group, which evaluates the inherent, time- and

by decreasing severity, for the CVSS v3.1 Base

Metric group. The CVSS Vector uses the abbreviated

metric name reported in parenthesis. For example the

CVSS Vector assigned by NVD to CVE-2023-35359 is

Network (N), Adjacent (A),

Attack Vector (AV)

Local (L), Physical (P)

| User Interaction (UI) | None (N), Required (R) |
| --- | --- |
| Availability Impact (A) | High (H), Low (L), None (N) |

Individual CVSS Metrics (Cat. I). Like our work,

it uses distinct multi-class classification models to

predict the eight CVSS metrics. Most approaches

leverage transfer learning with pre-trained BERT

models (Devlin et al., 2019) or their variants fine-

tuned for this task. Shahid and Debar (2021) uses

BERT-small, while Costa et al. (2022) and Kühn

et al. (2023) employ DistilBERT. Aghaei et al.

(2023) applies SecureBERT. Babalau et al. (2021)

and Shan et al. (2023) propose multi-task mod-

els combining BERT with BiLSTM. Other works

combine bag-of-words representations (Elbaz et al.,

2020) or word embeddings (Kekül et al., 2024)

with traditional Machine Learning (ML) models.

Qualitative CVSS Severity Ratings (Cat. II). It

predicts Qualitative Severity Ratings (None, Low,

Medium, High, Critical) derived from the 0–10

CVSS score (FIRST, 2023a) as a single 5-class

classification task. Kai et al. (2023) and Babalau

et al. (2021) fine-tune DistilBERT and BERT-small,

respectively. Li et al. (2023) explores prompt learn-

ing with BERT and RoBERTa, while Ni et al.

(2022) combines fine-tuned BERT with a CNN.

dicts the CVSS severity score (0–10 range) as

model (Raffel et al., 2020) in a multi-task setting,

| shot, and leveraging Retrieval-Augmented Gener- | CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H | . |  |  |
| --- | --- | --- | --- | --- |
| source and closed-source LLMs, also including the | CVSS Metric | Labels |  |  |
| in the black-box setting and compare them against | Attack Complexity (AC) | Low (L), High (H) |  |  |
| fine-tuned BERT supervised baselines | 1 | . | Privileges Required (PR) | None (N), Low (L), High (H) |
| Our study highlights three key findings: | Scope (S) | Changed (C), Unchanged (U) |  |  |
| ① | With abundant annotated data, LLM-based solu- | Confidentiality Impact (C) | High (H), Low (L), None (N) |  |
| tions have competitive performance, but they are | Integrity Impact (I) | High (H), Low (L), None (N) |  |  |
| ② | With limited labeled data, supervised baselines | diction | approaches into three categories. |  |
| we make the source code of AutoCVSS public. | CVSS Severity Score (Cat. III). | It directly pre- |  |  |
| 2 | CVSS metrics prediction | a regression task. | Pal et al. (2023) employs T5 |  |
| Several studies considered the prediction of CVSS | including CVSS prediction. Vasireddy et al. (2023), |  |  |  |
| metrics from CVE descriptions. | This paper fo- | Babalau et al. (2021), and Zhang et al. (2022) in- |  |  |
| cuses on predicting the CVSS v3.1 Base Metric | stead exploits ML-based models. |  |  |  |
| environment-independent characteristics of a vul- | 2.1 | LLM-based CVSS Prediction |  |  |
| nerability (see Table 1). We classify existing | pre- | Few studies have explored LLMs for predicting |  |  |
| 1 | In this paper, | LLMs | refer to decoder-only models like | CVSS v3.1 metrics, each with notable limitations. |
| GPT, not including encoder-only models like BERT. | McClanahan et al. (2024) evaluates GPT mod- |  |  |  |

---

## Page 3

els (OpenAI, 2024b) to retrieve CVSS scores and

vectors for a given CVE ID using only pre-trained

knowledge without using its description in input.

By design it cannot predict data for new CVEs

disclosed after the model’s knowledge cutoff date.

CTIBench (Alam et al., 2024) benchmarks Chat-

predict CVSS vectors. It only tests 1000 samples

and ignores supervised approaches.

CVEDrill (Aghaei et al., 2023) compares their

fine-tuned SecureBERT models with ChatGPT.

The evaluation, including only 100 CVEs, seems

to only consider zero-shot prompting.

CVECenter (Luo et al., 2024) predicts CVSS

metrics with zero-shot prompting using GPT mod-

els leveraging multi-source vulnerability records.

Their target is the specialization of the CVSS for

different Linux distributions, having the NVD’s

CVSS in the inputs rather than as predicted output.

Liu et al. (2024) proposes CyberBench, a bench-

mark for cybersecurity NLP tasks, including CVSS

prediction. Although they compared fine-tuned

BERT models against few-shots LLMs and fine-

tuned LLaMA2 models, their focus is on coarse-

grained CVSS severity ratings (Category II).

Isogai et al. (2024) shows that BERT outper-

forms gpt-4o-mini, with and without fine-tuning,

when predicting CVSS v3.1 vectors with zero-shot

prompting, with an approach similar to CTIBench.

3 AutoCVSS Methodology

class classification task. We evaluate multiple ap-

proaches, considering the closed-source OpenAI

GPT-4o (OpenAI, 2024a) and o3-mini (OpenAI,

2025), and open-source Meta LLaMA3 (Grattafiori

et al., 2024) and DeepSeek-R1 (DeepSeek-AI,

2025) models. We consider the LLMs general-

domain black-box models: LLM fine-tuning for

the security domain or CVSS-specific tasks is out

of the scope of this paper. 2 We implement the

approach depicted in Fig.1 with Instructor (Liu,

2024), an open-source framework for structured

output generation with LLMs. We explored both

zero-shot and few-shots prompting. Appx. A in-

cludes more details for reproducibility and exam-

ples of prompts.

Zero-shot Prompting Approaches. They leverage

the LLM’s inherent knowledge and generalization

capabilities without task-specific examples.

Simple Task Description (STD) : It relies only on

the LLM’s pre-trained understanding of CVSS met-

rics. The task description provides only the name

Few-shot Prompting Approaches. They lever-

age LLMs’ in-context learning (ICL) capabili-

| GPT and LLaMA3 using zero-shot prompting to | Figure 1: AutoCVSS high-level architecture. |  |  |
| --- | --- | --- | --- |
| Positioning of Our Work. | Unlike previous stud- | of the CVSS metric to predict and the set of possi- |  |
| ies, our work explores multiple LLM approaches | ble labels without any additional context or details. |  |  |
| beyond zero-shot prompting, extensively covering | Detailed Task Description (DTD) | : It leverages the |  |
| closed- and open-source LLMs (also considering | CVSS specification to enhance the prompt with |  |  |
| recent LRM variants specialized for reasoning), | more context. The task description includes a de- |  |  |
| compares supervised baselines (also including lat- | tailed explanation of the CVSS metric and its labels, |  |  |
| est advances in encoder-only models), and extends | directly borrowed from the CVSS Specification |  |  |
| evaluations to both CVSS v3.1 and the latest CVSS | Document provided by FIRST (2023b). |  |  |
| v4.0 specification, providing a more comprehen- | Full Vector Prediction (FVP) | : It directly predicts |  |
| sive approach and practical assessment of LLMs | the entire CVSS vector with a single prompt. In- |  |  |
| to the evolving vulnerability scoring needs. Our | dividual CVSS metrics are then extracted with |  |  |
| work belongs to Category I: predicting the indi- | a regular expression. We include this variant as |  |  |
| vidual CVSS metrics has the best value because it | an approach similar to CTIBench (Alam et al., |  |  |
| enhances transparency by showing which factors | 2024). FVP employ | Chain-of-Thought (CoT) | rea- |
| contribute to the overall score for better decision- | soning (Wei et al., 2022), enabling the LLM to rea- |  |  |
| making. In addition, from Category I metrics, we | son step-by-step. This enhances decision-making |  |  |
| can always derive Categories II and III metrics, | by dividing complex tasks into smaller, sequential |  |  |
| whereas the reverse is not possible. | steps, aligning with FVP’s holistic approach. |  |  |
| Following prior works from Category I (Sec.2), we | 2 | For completeness, Appx. C includes a preliminary evalua- |  |
| predict each CVSS metric as an independent multi- | tion of LLM fine-tuning, discussing its scope and limitations. |  |  |

---

## Page 4

| ties (Brown et al., 2020) by including a small set of | cureBERT (Aghaei et al., 2022), a cybersecurity- |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| (CVE description, label) | examples in the prompt | specific variant of BERT built on RoBERTa (Liu |  |  |  |
| to guide classification. For each test sample, RAG | et al., 2019) and pre-trained on a large corpus |  |  |  |  |
| constructs a prompt with the most semantically sim- | of cybersecurity data. As an additional baseline, |  |  |  |  |
| ilar training examples, retrieved through semantic | we also fine-tuned ModernBERT models, a re- |  |  |  |  |
| search in a vector database. We use Chroma (2024) | cent general-domain state-of-the-art encoder-only |  |  |  |  |
| to store and query text embeddings generated with | model (Warner et al., 2024). | Finally, we added |  |  |  |
| a SBERT model (Reimers and Gurevych, 2019). | the Worst Case Label (WCL) baseline, which as- |  |  |  |  |
| These examples help the LLM predict labels based | signs each sample the most severe label for each |  |  |  |  |
| on similar descriptions. Although all the zero-shot | CVSS metric, following the conservative strategy |  |  |  |  |
| methods can theoretically be extended to few-shot | described in Sec. 3. |  |  |  |  |
| settings, adapting CoT prompting would require ex- | Evaluation Metrics. | We adopt the same eval- |  |  |  |
| tensive manual annotation of reasoning chains, ren- | uation metrics used in related works (Category I, |  |  |  |  |
| dering it impractical. Hence, we focus on few-shot | Sec. 2), namely Accuracy (A), weighted F1-score |  |  |  |  |
| variants of | STD | and | DTD | . Also, we exclude LRMs | (wF1), and Macro F1-score (MF1). Although our |
| from this approach because their providers suggest | work does not directly predict the CVSS sever- |  |  |  |  |
| that few-shot prompting may produce poor results | ity score, we extend our evaluation to also align |  |  |  |  |
| (Guo et al., 2025; OpenAI, 2024c). In terms of | with works from Categories II and III. From the |  |  |  |  |
| number of training samples ( | shots | ) for the prompt, | eight predicted metrics, we compute the severity |  |  |
| we tested values from 1 to 32 and found 24 to have | score (NVD, 2024b) and report the Mean Average |  |  |  |  |
| the best cost-improvement trade-off for our task. | Error (MAE) and Mean Squared Error (MSE). Ad- |  |  |  |  |
| To handle cases where the LLM cannot make | ditionally, we quantize the computed severity score |  |  |  |  |
| an informed decision, we introduced an additional | into the Qualitative Severity Rating Scale (QSRS) |  |  |  |  |
| label, | Don’t Know (DK) | , across all strategies de- | and discuss the results in detail in Appendix E. |  |  |

scribed in this section. This allows the LLM to

indicate when the provided description cannot as-

sess the metric. As a final step, samples classified

with the DK label are mapped to the most severe

label for the CVSS metric (e.g., NETWORK for At-

tackVector ), following the conservative worst-case

approach recommended by NVD (2024d) for miss-

To further examine the

implications of consistently applying this approach

to all the samples, Sec. 4 includes an additional

baseline based on this conservative policy.

4 Evaluation

works from the literature, both based on fine-tuned

BERT models: DistilBERT-E (Costa et al., 2022)

3 Although the DK-labeled samples are negligible, this

Dataset. For our evaluation, we used all the public

CVE records published in the NVD between Jan-

uary 2023 and April 2024, retaining only those with

CVSS v3.1 information released by the NVD and

obtaining a dataset of over 27k CVE records. Fig. 2

illustrates the class proportions for the eight CVSS

values and for the CVE description lengths, in char-

acters. We perform a stratified 80/20 train/test split

on the dataset. We stratify the split by the CVSS

vector to ensure that (1) class proportions are con-

sistent in both sets and (2) each CVE ID appears

exclusively in either the train or test set for all eight

4.1 Full dataset evaluation

we only report the top-6 configurations: 4

0-shot configurations, dominated by o3-mini, show

| ing or unclear information. | 3 | Metrics and the distributions for the severity scores |
| --- | --- | --- |
| We evaluate the different LLM-based approaches | models. Performances are computed on the test set, |  |
| against four baselines, considering three different | while the train set is used either to fine-tune models |  |
| data availability settings and two CVSS versions. | (for supervised baselines) or to populate the Vector |  |
| Baseline approaches. | We selected two related | Store (for few-shot LLM-based methods). |
| and CVEDrill (Aghaei et al., 2023). DistilBERT- | Table 2 summarizes the performance metrics, aver- |  |
| E relies on DistilBERT (Sanh et al., 2019), a | aged across the eight CVSS metrics, when consid- |  |
| smaller and faster version of BERT, to predict | ering the entire dataset. For the 0-shot approaches, |  |
| the CVSS metric using eight separate multi-class | closed- |  |
| classification models. | CVEDrill adopts a simi- | source models offer the best performance with |
| lar approach, with eight models, but employs Se- | LRM variants better than LLM. Although the best |  |
| mapping is beneficial in most of the cases (cf. Appx. B). | 4 | Table 6 in Appx. D includes the remaining configurations. |

---

## Page 5

Figure 2: Dataset statistics: class proportions for the

Scores values and for the CVE Description Lengths.

Table 2: Full dataset evaluation. Top-3 values are

marked in bold , italic bold and italic , respectively.

| Worst Case Label | 0.595 | 0.466 | 0.276 | 2.836 | 11.094 |
| --- | --- | --- | --- | --- | --- |
| DistilBERT-E | 0.903 | 0.897 | 0.739 | 0.762 | 1.983 |
| 0s FVP GPT-4o | 0.754 | 0.743 | 0.643 | 1.655 | 4.861 |
| 0s STD GPT-4o | 0.757 | 0.765 | 0.651 | 1.317 | 3.343 |
| 0s DTD GPT-4o | 0.750 | 0.751 | 0.634 | 1.494 | 4.573 |

that FVP works best, when moving to few-shots

approaches, we had to limit to STD and DTD, only

considering LLMs without LRMs (cf. Sec. 3). We

thus picked the best among STD and DTD, i.e.,

STD, for both GPT-4o and LLaMA3 models.

Results indicate that the best LLM-based ap-

proach (GPT-4o few-shots) surpasses DistilBERT-

E, but falls short of ModernBERT and CVEDrill.

Table 10 in Appx. F breaks down numbers by

CVSS metric. The stronger performance of Mod-

ernBERT and CVEDrill can be attributed to their

larger model size (150 and 125 million parameters,

nearly double DistilBERT-E’s 65 million). In ad-

dition, CVEDrill also received a pre-training on a

cybersecurity-specific corpus before fine-tuning.

The Worst Case Label baseline, serving as the

lower bound, delivers the poorest performance, sig-

nificantly underperforming even the worst LLM-

based baseline. As noted in Sec.4, we also report

the MAE and MSE of the severity score calculated

from the eight predicted metrics, observing that the

Table 3: Low-resource setting. Top-3 values are marked

in bold , italic bold and italic , respectively. Notice that

the marking of top values excludes the hybrid approach.

| Method | A | wF1 | MF1 | MAE | MSE |
| --- | --- | --- | --- | --- | --- |
| Worst Case Label | 0.600 | 0.470 | 0.278 | 2.798 | 11.145 |
| DistilBERT-E | 0.869 | 0.858 | 0.673 | 0.899 | 2.334 |
| ModernBERT | 0.921 | 0.920 | 0.848 | 0.631 | 1.767 |
| CVEDrill | 0.887 | 0.876 | 0.695 | 0.868 | 2.308 |
| 24s STD GPT-4o | 0.909 | 0.908 | 0.833 | 0.655 | 1.835 |

24s STD LLaMA3 0.896 0.893 0.821 0.715 2.013

SL+LLM Hybrid 0.922 0.920 0.860 0.677 1.894

Our results align with recent findings (Yang et al.,

2024) and validate them for our CVSS prediction

task: while both LLMs and fine-tuned models per-

models generally outperform LLMs in traditional

also suggest that LLMs may outperform fine-tuned

in 2024 5 and evaluated the same set of methods

from Sec. 4.1. Since the previous considerations

for zero-shot approaches from Section 4.1 still ap-

ply, for the sake of brevity, we omit their values

here and report them in Table 7 in Appendix D.

Table 3 shows that the best-performing LLM

configurations are now just behind ModernBERT,

which proves to be more robust to the reduced fine-

tuning data compared to other supervised baselines.

A similar ranking, with both few-shots LLMs enter-

ing the top-3 positions, can be observed when ana-

lyzing the results in terms of QSRS (cf. Appx. E).

Although ModernBERT has the best-averaged per-

formance, it is outperformed by LLMs on specific

CVSS metrics (cf. Table 11 in Appx. F). By envi-

sioning a scenario where each metric is predicted

by a different method, LLMs can complement Mod-

ernBERT by offering better performance on 4 out

of 8 metrics, overall achieving the best results

("SL+LLM Hybrid" configuration in Table 3).

This low-resource setting is particularly relevant

when considering the limited availability of labeled

| eight CVSS Metrics and distributions for the Severity | terms of QSRS (Cat. III metrics, cf. Appx. E). |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LLMs use | [Prompt Strategy][Model] | naming (Sec. 3). | form well with abundant annotated data, fine-tuned |  |  |  |  |
| Method | A | wF1 | MF1 | MAE | MSE | NLU tasks like text classification. | The authors |
| ModernBERT | 0.928 | 0.927 | 0.858 | 0.554 | 1.270 | models in scenarios with limited annotated data. In |  |
| CVEDrill | 0.929 | 0.928 | 0.858 | 0.549 | 1.231 | the next section, we explore this aspect for our task |  |
| 0s FVP o3-mini | 0.846 | 0.836 | 0.722 | 1.200 | 3.991 | by considering a low-resource setting, with limited |  |
| 0s STD o3-mini | 0.804 | 0.793 | 0.676 | 1.609 | 6.000 | train data for fine-tuning and for the Vector Store. |  |
| 0s DTD o3-mini | 0.767 | 0.755 | 0.654 | 2.095 | 8.747 | 4.2 | Low-resource setting evaluation |
| 24s STD GPT-4o | 0.915 | 0.915 | 0.842 | 0.608 | 1.469 | In this setting, we considered a subset of the dataset |  |
| 24s STD LLaMA3 | 0.905 | 0.903 | 0.825 | 0.667 | 1.623 | by only including the 2.1k vulnerabilities disclosed |  |
| general ranking of methods is preserved. A similar | 5 | The dataset, roughly 10% of the original size, is again |  |  |  |  |  |
| outcome is observed when analyzing the results in | divided into train/test sets with a stratified 80/20 splitting. |  |  |  |  |  |  |

---

## Page 6

Table 4: CVSS v4.0. Top-3 values are marked in bold , to the GA date closely aligning with the LLMs’

italic bold and italic , respectively.

0s STD o3-mini 0.715 0.710 0.564 1.187 2.596

0s DTD LLaMA3 0.689 0.697 0.522 1.984 7.969

Despite this temporal holdout, results are in line

with those observed in Section 4.1 and in this sec-

4.3 Towards CVSS v4.0

knowledge cutoff dates 7 , as well as the limited

may stem from the CVSS scoring formula, which

assigns different weights to metrics (NVD, 2024c).

5 Conclusions

work explored the potential of Large Language

Models (LLMs) for automating CVSS prediction

| Method | A | wF1 | MF1 | MAE | MSE | adoption of the new standard, which likely results |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Worst Case Label | 0.560 | 0.437 | 0.250 | 2.305 | 7.528 | in poor CVSS v4.0 knowledge in the pre-training |  |
| 0s FVP o3-mini | 0.701 | 0.684 | 0.519 | 1.268 | 2.763 | data. | In this case, a more detailed task descrip- |
| 0s DTD o3-mini | 0.780 | 0.765 | 0.586 | 2.103 | 9.970 | tion in the prompt, combined with the enhanced |  |
| 0s DTD DeepSeek | 0.739 | 0.727 | 0.536 | 1.179 | 3.309 | reasoning capabilities of LRMs, offer the best per- |  |
| 0s DTD GPT-4o | 0.691 | 0.710 | 0.547 | 1.242 | 2.975 | formance. The different ranking for MAE/MSE |  |
| data, like in the transition from CVSS v3.1 to v4.0. | Although performance in absolute terms is lower |  |  |  |  |  |  |
| In this phase, hybrid solutions combining super- | than in previous sections, especially due to the up- |  |  |  |  |  |  |
| vised methods and LLMs could perform better than | dated metrics (cf. Table 12 in Appendix F), the re- |  |  |  |  |  |  |
| supervised ones alone. CVSS v4.0 was officially | sults demonstrate that LLMs can produce an initial |  |  |  |  |  |  |
| launched in General Availability (GA) in Novem- | set of labels with performance up to 33 percentage |  |  |  |  |  |  |
| ber 2023 (FIRST, 2023c), but at the time of writing, | points higher than the most conservative baseline |  |  |  |  |  |  |
| more than one year later, just a few CVE records in- | (WCL). This provides a valuable tool to support |  |  |  |  |  |  |
| clude v4.0 data. In the next section, we investigate | the adoption of the new release. As more labeled |  |  |  |  |  |  |
| whether LLMs in a zero-shot setting can provide | data becomes available, the process can transition |  |  |  |  |  |  |
| a good enough solution for the challenging setting | to a low-resource scenario, enabling more effective |  |  |  |  |  |  |
| of a complete lack of labeled data, which prevents | hybrid approaches, and, eventually, more power- |  |  |  |  |  |  |
| a priori the adoption of both the supervised and the | ful fully-supervised methods. Considering that the |  |  |  |  |  |  |
| LLM few-shot methods. | minor version update from v3.0 to v3.1 took sev- |  |  |  |  |  |  |
| As additional evaluation, in Appx. G we consid- | eral months to reach the first 1,000 samples post- |  |  |  |  |  |  |
| ered a subset of test set CVEs whose CVSS has | announcement, the adoption timeline for a major |  |  |  |  |  |  |
| been released after LLMs’ knowledge cutoff dates. | version update like v4.0 is likely to be even longer. |  |  |  |  |  |  |
| tion, suggesting that for this task the performance | The current cybersecurity landscape, with a grow- |  |  |  |  |  |  |
| of LLMs should not be attributed to the memo- | ing number of vulnerabilities disclosed and attack- |  |  |  |  |  |  |
| rization of specific examples the LLM may have | ers acting faster, poses a significant challenge for |  |  |  |  |  |  |
| encountered during its pre-training process. | analysts to keep up with the emerging threats. This |  |  |  |  |  |  |
| CVSS v4.0 introduces key updates: a new | attack- | across different data availability settings. Our find- |  |  |  |  |  |
| Requirements | metric, removal of the | scope | metric, | ings demonstrate that when abundant labeled data |  |  |  |
| updates to | userInteraction | labels, and additional | is available, LLMs are competitive, but are sur- |  |  |  |  |
| Impact | metrics, totaling 11 metrics. To the best of | passed by supervised approaches. LLMs are, in- |  |  |  |  |  |
| our knowledge, this is the first practical evaluation | stead, a valuable solution in scenarios of scarce |  |  |  |  |  |  |
| of CVSS v4.0. The lack of sufficient labeled sam- | data availability, complementing the best super- |  |  |  |  |  |  |
| ples calls for a zero-shot setting, but the CVSS v4.0 | vised baseline for half of the CVSS metrics. Finally, |  |  |  |  |  |  |
| Specification Document (FIRST, 2023d) facilitates | in extreme data scarcity, such as during transitions |  |  |  |  |  |  |
| the prompts’ adaptation. The NVD provides mini- | to new CVSS versions, LLMs are the only viable |  |  |  |  |  |  |
| mal data for CVSS v4.0, but FIRST (2024a) offers | approach and can provide better predictions than |  |  |  |  |  |  |
| a supplementary document with 38 annotated CVE | conservative approaches and support the adoption |  |  |  |  |  |  |
| records suitable as test data in our evaluation. | of updated scoring systems. These findings high- |  |  |  |  |  |  |
| Table 4 includes the top-6 configurations | 6 | and | light LLMs’ practical potential to enhance vulnera- |  |  |  |  |
| shows that, in contrast to previous results, here | bility risk prioritization. Future works will expand |  |  |  |  |  |  |
| LRMs with a DTD approach are the two best- | predictions to consider temporal and environmental |  |  |  |  |  |  |
| performing configurations. This can be attributed | factors for a more comprehensive risk assessment. |  |  |  |  |  |  |
| 6 | Table 8 in Appx. D includes the remaining configurations. | 7 | Oct. and Dec. 2023 for OpenAI and Meta models used. |  |  |  |  |

---

## Page 7

Limitations Joana Cabral Costa, Tiago Roxo, João BF Sequeiros,

tailed in Appx. A. Given the pace of advancement

in LLMs, newer and more powerful LLMs may pro-

system. Second, due to the scarce availability of

labeled data, the CVSS v4.0 evaluation is restricted

a larger amount of labeled data would enable a

more comprehensive evaluation including the com-

References

Ehsan Aghaei, Ehab Al-Shaer, Waseem Shadid, and

Shaer. 2022. Securebert: A domain-specific lan-

ference on Security and Privacy in Communication

Systems , pages 39–56. Springer.

Md Tanvirul Alam, Dipkamal Bhushl, Le Nguyen, and

evaluating llms in cyber threat intelligence. arXiv

Cristian Sandescu, and Mihai Dascalu. 2021. Sever-

ity prediction of software vulnerabilities based on

entific computing (SYNASC) , pages 171–177. IEEE.

Gretchen Krueger, Tom Henighan, Rewon Child,

Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,

Clemens Winter, Christopher Hesse, Mark Chen, Eric

Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,

Jack Clark, Christopher Berner, Sam McCandlish,

Alec Radford, Ilya Sutskever, and Dario Amodei.

Proceedings of the 34th International Conference on

Neural Information Processing Systems , NIPS ’20,

Embedding Database.

Hugo Proenca, and Pedro RM Inacio. 2022. Predict-

CVE. 2024a. CVE Metrics.

(Ollama).

DeepSeek-AI. 2025. Deepseek-r1: Incentivizing rea-

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and

Kristina Toutanova. 2019. BERT: Pre-training of

of the North American Chapter of the Association

for Computational Linguistics: Human Language

Technologies, Volume 1 (Long and Short Papers) . As-

sociation for Computational Linguistics.

of the 15th International Conference on Availability,

FIRST. 2023b. CVSS v3.1 Specification Document.

FIRST. 2023c. CVSS v4.0 Press Release.

rity Teams.

Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,

Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song,

Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma,

Peiyi Wang, Xiao Bi, et al. 2025. Deepseek-r1: In-

centivizing reasoning capability in llms via reinforce-

ment learning. arXiv preprint arXiv:2501.12948 .

MiniLM-L6-v2.

70B-Instruct.

| This study has two main limitations. | First, our | ing cvss metric via description interpretation. | IEEE |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| evaluation is based on specific LLM snapshots, de- | Access | , 10:59125–59134. |  |  |  |  |  |
| vide improved performance for AutoCVSS with- | CVE. 2024b. CVE Program. |  |  |  |  |  |  |
| out requiring significant changes to the proposed | DeepSeek-AI. 2025. DeepSeek-R1-Distill-Llama-70B |  |  |  |  |  |  |
| to LLMs in the zero-shot setting. As the adoption | soning capability in llms via reinforcement learning. |  |  |  |  |  |  |
| of the latest release increases, the availability of | Preprint | , arXiv:2501.12948. |  |  |  |  |  |
| parison against supervised baselines and few-shots | deep bidirectional transformers for language under- |  |  |  |  |  |  |
| LLMs approaches. | standing. | In | Proceedings of the 2019 Conference |  |  |  |  |
| Xi Niu. 2023. | Automated cve analysis for threat | Clément Elbaz, Louis Rilling, and Christine Morin. |  |  |  |  |  |
| prioritization and impact prediction. | arXiv preprint | 2020. Fighting n-day vulnerabilities with automated |  |  |  |  |  |
| arXiv:2309.03040 | . | cvss vector prediction at disclosure. In | Proceedings |  |  |  |  |
| Ehsan Aghaei, Xi Niu, Waseem Shadid, and Ehab Al- | Reliability and Security | , pages 1–10. |  |  |  |  |  |
| guage model for cybersecurity. In | International Con- | FIRST. 2023a. CVSS Qualitative Severity Rating Scale. |  |  |  |  |  |
| Nidhi Rastogi. 2024. | Ctibench: A benchmark for | FIRST. 2023d. CVSS v4.0 Specification Document. |  |  |  |  |  |
| preprint arXiv:2406.07599 | . | FIRST. 2024a. CVSS v4.0 Examples. |  |  |  |  |  |
| Ion Babalau, Dragos Corlatescu, Octavian Grigorescu, | FIRST. 2024b. Forum of Incident Response and Secu- |  |  |  |  |  |  |
| their text description. In | 2021 23rd international sym- | Google. 2024. How Low Can You Go? An Analysis of |  |  |  |  |  |
| posium on symbolic and numeric algorithms for sci- | 2023 Time-to-Exploit Trends. |  |  |  |  |  |  |
| Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie | Abhinav Pandey, | Abhishek Kadian, | Ahmad Al- |  |  |  |  |
| Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind | Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, |  |  |  |  |  |  |
| Neelakantan, Pranav Shyam, Girish Sastry, Amanda | Alex Vaughan, et al. 2024. The llama 3 herd of mod- |  |  |  |  |  |  |
| Askell, | Sandhini | Agarwal, | Ariel | Herbert-Voss, | els. | arXiv preprint arXiv:2407.21783 | . |
| 2020. Language models are few-shot learners. In | Hugging | Face. | 2021. | sentence-transformers/all- |  |  |  |
| Red Hook, NY, USA. Curran Associates Inc. | Hugging Face. 2023. ehsanaghaei/SecureBERT. |  |  |  |  |  |  |
| Joana Cabral. 2022. GitHub - CVSS Prediction. | Hugging Face. 2024a. answerdotai/ModernBERT-base. |  |  |  |  |  |  |
| Chroma. 2024. Chroma: The AI-Native Open-Source | Hugging Face. 2024b. | meta-llama/Meta-Llama-3.1- |  |  |  |  |  |

---

## Page 8

Sho Isogai, Shinpei Ogata, Yutaro Kashiwa, Satoshi Conference on Computing, Networking and Commu-

Yazawa, Kozo Okano, Takao Okubo, and Hironori nications (ICNC) . IEEE.

Washizaki. 2024. Toward extracting learning pat-

Vuldistilbert: A cps vulnerability severity prediction

Communication Networks , 2023(1):2118305.

Hakan Kekül, Burhan Ergen, and Halil Arslan. 2024.

ding and multiclass classification methods. Interna-

tional Journal of Information Security , 23(1):247–

270.

Philipp Kühn, David N Relke, and Christian Reuter.

2023. Common vulnerability scoring system predic-

tion based on open source intelligence information

Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E.

cient memory management for large language model

ACM SIGOPS 29th Symposium on Operating Systems

tion and prompt learning. In 2023 IEEE Interna-

Jason Liu. 2024. Instructor: A library for structured

outputs from large language models.

Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-

dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,

Luke Zettlemoyer, and Veselin Stoyanov. 2019.

Roberta: A robustly optimized bert pretraining ap-

proach. arXiv preprint arXiv:1907.11692 .

Jing Luo, Heyuan Shi, Yongchao Zhang, Runzhe Wang,

329–339.

NVD. 2024c. NVD - CVSS v4 Calculator.

NVD. 2024e. NVD - Home.

NVD. 2024f. NVD Dashboard.

Ollama. 2025. Ollama.

theswaran, Kirby C Kuznia, Siddhesh Jagtap, and

practical automation of vulnerability assessment. In

Proceedings of the IEEE/ACM 46th International

Conference on Software Engineering , pages 1–13.

Qualys. 2023. 2023 Threat Landscape Year in Review:

If Everything Is Critical, Nothing Is.

Colin Raffel, Noam Shazeer, Adam Roberts, Katherine

Lee, Sharan Narang, Michael Matena, Yanqi Zhou,

21(140):1–67.

3982–3992.

| tern: A comparative study of gpt-4o-mini and bert | Xuming Ni, Jianxin Zheng, Yu Guo, Xu Jin, and Ling Li. |  |  |
| --- | --- | --- | --- |
| models in predicting cvss base vectors. In | 2024 IEEE | 2022. Predicting severity of software vulnerability |  |
| 35th International Symposium on Software Reliability | based on bert-cnn. In | 2022 International Conference |  |
| Engineering Workshops (ISSREW) | , pages 127–134. | on Computer Engineering and Artificial Intelligence |  |
| IEEE. | (ICCEAI) | , pages 711–715. IEEE. |  |
| Shaofeng Kai, Fan Shi, and Jinghua Zheng. 2023. | NVD. 2024a. NVD - CVE FAQs. |  |  |
| method based on distillation model. | Security and | NVD. 2024b. NVD - CVSS v3 Calculator. |  |
| Estimating vulnerability metrics with word embed- | NVD. 2024d. NVD - General FAQs. |  |  |
| sources. | Computers & Security | , 131:103286. | OpenAI. 2024a. OpenAI GPT-4o System Card. |
| Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying | OpenAI. 2024b. OpenAI Models documentation. |  |  |
| Gonzalez, Hao Zhang, and Ion Stoica. 2023. Effi- | OpenAI. 2024c. OpenAI o1 series - Reasoning models. |  |  |
| serving with pagedattention. In | Proceedings of the | OpenAI. 2025. OpenAI o3-mini System Card. |  |
| Principles | . | Kuntal Kumar Pal, Kazuaki Kashihara, Ujjwala Anan- |  |
| Xiangwei Li, Xiaoning Ren, Yinxing Xue, Zhenchang | Chitta Baral. 2023. | Exploring the limits of trans- |  |
| Xing, and Jiamou Sun. 2023. Prediction of vulnera- | fer learning with unified model in the cybersecurity |  |  |
| bility characteristics based on vulnerability descrip- | domain. | arXiv preprint arXiv:2302.10346 | . |
| tional Conference on Software Analysis, Evolution | Shengyi Pan, Lingfeng Bao, Jiayuan Zhou, Xing Hu, |  |  |
| and Reengineering (SANER) | , pages 604–615. IEEE. | Xin Xia, and Shanping Li. 2024. | Towards more |
| Zefang Liu, Jialei Shi, and John F Buford. 2024. Cyber- | Wei Li, and Peter J Liu. 2020. | Exploring the lim- |  |
| bench: A multi-task benchmark for evaluating large | its of transfer learning with a unified text-to-text |  |  |
| language models in cybersecurity. | transformer. | Journal of machine learning research | , |
| Yuheng Shen, Yuao Chen, Xiaohai Shi, Rongkai Liu, | Nils Reimers and Iryna Gurevych. 2019. | Sentence- |  |
| Chao Hu, and Yu Jiang. 2024. Cvecenter: Industry | BERT: Sentence embeddings using Siamese BERT- |  |  |
| practice of automated vulnerability management for | networks. In | Proceedings of the 2019 Conference on |  |
| linux distribution community. | In | Companion Pro- | Empirical Methods in Natural Language Processing |
| ceedings of the 32nd ACM International Conference | and the 9th International Joint Conference on Natu- |  |  |
| on the Foundations of Software Engineering | , pages | ral Language Processing (EMNLP-IJCNLP) | , pages |
| Kylie McClanahan, Sky Elder, Marie Louise Uwibambe, | Victor Sanh, Lysandre Debut, Julien Chaumond, and |  |  |
| Yaling Liu, Rithyka Heng, and Qinghua Li. 2024. | Thomas Wolf. 2019. Distilbert, a distilled version |  |  |
| When chatgpt meets vulnerability management: the | of bert: smaller, faster, cheaper and lighter. | arXiv |  |
| good, the bad, and the ugly. In | 2024 International | preprint arXiv:1910.01108 | . |

---

## Page 9

Mustafizur R Shahid and Hervé Debar. 2021. Cvss-bert: A Appendix: Reproducibility

Explainable natural language processing to determine

(ICMLA) , pages 1600–1607. IEEE.

diction method. In 2023 IEEE 12th International

Conference on Cloud Networking (CloudNet) , pages

Dinesh T Vasireddy, Dakota S Dale, and Qinghua Li.

2023. Cvss base score prediction using an optimized

machine learning scheme. In 2023 Resilience Week

Benjamin Warner, Antoine Chaffin, Benjamin Clavié,

Orion Weller, Oskar Hallström, Said Taghadouini,

efficient, and long context finetuning and inference.

arXiv preprint arXiv:2412.13663 .

et al. 2022. Chain-of-thought prompting elicits rea-

soning in large language models. Advances in neural

Jingfeng Yang, Hongye Jin, Ruixiang Tang, Xiao-

tian Han, Qizhang Feng, Haoming Jiang, Shaochen

from Data , 18(6):1–32.

tous Security , pages 129–143. Springer.

implementation from the authors (Cabral, 2022).

pre-trained SecureBERT model available on Hug-

ernBERT starting from the pre-trained model pro-

vided on Hugging Face, 2024a. For the closed-

source LLMs we tested the gpt-4o-2024-11-20

APIs. For the open-source models, we locally run

Meta-Llama-3.1-70B (Hugging Face, 2024b) and

text embeddings we used the all-MiniLM-L6-v2

SBERT model (Hugging Face, 2021).

in Section 3 for reproducibility of our results. All

(falling back to user messages when not supported

by the LLM, e.g. DeepSeek-R1) which are then

get structured output data from LLMs. For the sake

found in our GitHub repository.

Simple Task Description (STD). The same

prompt is used for zero-shot and few-shots setting:

the text in bold is only present for the latter.

 

You are an expert cybersecurity analyst from NVD.

Your task is to extract the CVSS v3.1 Attack Vector metric

label for the provided CVE description.

Here are some relevant examples.

CVE description: [...]

LABEL: [...]

...

 

Detailed Task Description (DTD). As for STD,

the same prompt is used for zero-shot and few-

shots setting: the text in bold is only present for

the latter. For the sake of brevity, we omitted the

full definitions of the labels, which can be found

in the CVSS v3.1 Specification (FIRST, 2023b). A

similar prompt is also adopted for CVSS v4.0.

| the severity of a computer security vulnerability from | This section provides the implementation details |  |  |  |
| --- | --- | --- | --- | --- |
| its description. | In | 2021 20th IEEE International | for the methods evaluated in Section 4. | For |
| Conference on Machine Learning and Applications | DistilBERT-E we directly used the open-source |  |  |  |
| Chun Shan, Ziyi Zhang, and Siyi Zhou. 2023. A multi- | Due to the lack of an open-source implementa- |  |  |  |
| task deep learning based vulnerability severity pre- | tion, we re-implemented CVEDrill based on the |  |  |  |
| 307–315. IEEE. | ging Face, 2023. Similarly, we fine-tuned Mod- |  |  |  |
| (RWS) | , pages 1–6. IEEE. | and | o3-mini-2025-01-31 | snapshots via OpenAI |
| Alexis Gallagher, Raja Biswas, Faisal Ladhak, Tom | deepseek-r1:70b | (DeepSeek-AI, 2025) on our |  |  |
| Aarsen, et al. 2024. Smarter, better, faster, longer: | server with vLLM (Kwon et al., 2023) and ollama |  |  |  |
| A modern bidirectional encoder for fast, memory | (Ollama, 2025), respectively. For the Vector Store’s |  |  |  |
| Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten | The rest of the section includes examples of the |  |  |  |
| Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, | prompts used in the different strategies described |  |  |  |
| information processing systems | , 35:24824–24837. | the prompts reported below are system messages |  |  |
| Zhong, Bing Yin, and Xia Hu. 2024. Harnessing the | followed by an user message containing the actual |  |  |  |
| power of llms in practice: A survey on chatgpt and | description of the CVE to be classified. We also |  |  |  |
| beyond. | ACM Transactions on Knowledge Discovery | provide the | Response Model | used by Instructor to |
| Zijing Zhang, Vimal Kumar, Michael Mayo, and Al- | of brevity we only report examples for one of the |  |  |  |
| bert Bifet. 2022. | Assessing vulnerability from its | eight CVSS metrics, i.e. the Attack Vector. The |  |  |
| description. In | International Conference on Ubiqui- | rest of the prompts and | Reponse Models | can be |

---

## Page 10

  Table 5: Analysis of Don’t Know (DK) labels: number

You are an expert cybersecurity analyst from NVD. of cases and impact on performance.

Your task is to extract the CVSS v3.1 Attack Vector metric

label for the provided CVE description.

the thing that is vulnerable, [...]

The possible values for the Attack Vector metric are:

- PHYSICAL: [...]

evaluate the attack vector.

Here are some relevant examples.

CVE description: [...]

...

lowing Response Model expressed as a Pydantic 8

library for Python and core part of Instructor.

"LOCAL", "PHYSICAL", "DONT_KNOW"

description="The Attack Vector CVSS v3.1 metric.

, → is not sufficient to evaluate the attack

 

the provided CVE description.

sufficient to answer the question, use the value

 

B Appendix: Impact of Don’t Know label

Case Label (WCL) matches the Ground Truth. For

samples in the full dataset (FD) and low-resource

(LR) scenarios, respectively. While the DK sample

CVSS 24s STD GPT-4o (FD) 24s STD GPT-4o (LR)

| AV | 55 (1.0%) | 33 (60%) | 7 (1.6%) | 5 (71%) |
| --- | --- | --- | --- | --- |
| UI | 69 (1.3%) | 49 (71%) | 12 (2.8%) | 6 (50%) |

quota is small, using WCL improves performance

scenarios. LLaMA3 is omitted from the table be-

This section includes a preliminary evaluation of

resources. Starting from the same train/test sets

chains for the whole train set, cf. Sec. 3), and we

selected the best zero-shot approach for GPT-4o,

i.e. STD (cf. Table 7). With reference to Table 3

Tables 6, 7 and 8 in this section include the entire

set of zero-shot methods, grouped by configuration,

| The Exploitability metrics reflect the characteristics of | Metric | DK | WCL OK | DK | WCL OK |
| --- | --- | --- | --- | --- | --- |
| The Attack Vector metric reflects the context by which | AC | 40 (0.7%) | 33 (82%) | 6 (1.4%) | 6 (100%) |
| vulnerability exploitation is possible [...] | PR | 54 (1.0%) | 29 (54%) | 5 (1.2%) | 1 (20%) |
| - NETWORK: The vulnerable component is bound to the network | S | 31 (0.6%) | 7 (23%) | 5 (1.2%) | 4 (80%) |
| stack and the set of possible attackers extends [...] | C | 60 (1.1%) | 23 (38%) | 7 (1.6%) | 4 (57%) |
| - ADJACENT_NETWORK: [...] | I | 37 (0.7%) | 17 (46%) | 10 (2.3%) | 4 (40%) |
| - LOCAL: [...] | A | 100 (1.8%) | 53 (53%) | 9 (2.1%) | 5 (56%) |
| - DON_KNOW: The information provided is not sufficient to | AVG | 55 (1.0%) | 30 (55%) | 7 (1.8%) | 4 (57%) |
| LABEL: [...] | in over half of these cases for both data availability |  |  |  |  |
|  |  | cause, interestingly, never returned any DK label |  |  |  |
| Both STD and DTD approaches share the fol- | for all the 8 CVSS metrics in both data scenarios. |  |  |  |  |
| BaseModel, the most widely used data validation | C | Appendix: LLM Fine-tuning |  |  |  |
| class AttackVector | (BaseModel): | LLM fine-tuning for GPT-4o via OpenAI APIs (o3- |  |  |  |
| attack_vector: Literal["NETWORK", "ADJACENT_NETWORK", | mini does not support fine-tuning yet). Due to high |  |  |  |  |
| ] = Field( | costs, we restricted ourselves to the low-resource |  |  |  |  |
| , | → | DONT_KNOW is used when the information provided | setting (fine-tuning on the full dataset would cost |  |  |
| , | → | vector." | 10 times more). We also excluded fine-tuning of the |  |  |
| ) | two local open-source models due to our limited |  |  |  |  |
| Full Vector Prediction (FVP). | As commented in | split of Sec. 4.2, performances are computed on the |  |  |  |
| Section 3, only for this scenario, all the 8 metrics | test set, while the train set is used for LLM fine- |  |  |  |  |
| are concurrently predicted with a single prompt. | tuning. In terms of prompt strategies, we excluded |  |  |  |  |
| You are an expert cybersecurity analyst from NVD. | both few-shots prompting (the train set samples |  |  |  |  |
| Your task is to extract the eight CVSS v3.1 metrics from | are required for fine-tuning itself and cannot be |  |  |  |  |
| If for any of the metrics the information provided is not | also re-used in the Vector Store) and zero-shot FVP |  |  |  |  |
| "DONT_KNOW". | (it’s impractical to manually annotate the reasoning |  |  |  |  |
| This section examines the impact of the Don’t | from Sec. 4.2, fine-tuning "0s STD GPT-4o" outper- |  |  |  |  |
| Know (DK) label, focusing on the top-2 LLM con- | forms ModernBERT on A (92.3%), has the same |  |  |  |  |
| figurations for both the full dataset (FD) and low- | wF1 (92.0%), but has a worse MF1 (84.2%). In |  |  |  |  |
| resource (LR) scenarios from Sec. 4.1 and 4.2: i.e. | summary, when considering an absolute ranking |  |  |  |  |
| "24s STD GPT-4o" and "24s STD LLaMA3". The | based on the average of A, wF1, and MF1, Mod- |  |  |  |  |
| "DK" | columns in Table 5 show the number and | ernBERT still maintains its top-1 position. Due to |  |  |  |
| percentage of samples predicted as DK for each | the limitations described above, we kept LLM fine- |  |  |  |  |
| CVSS metric. The | "WCL OK" | columns indicate | tuning out of the scope of the paper and we leave a |  |  |
| cases where converting a DK label to the Worst | more comprehensive analysis for future works. |  |  |  |  |
| example, GPT-4o predicted DK for 1% and 1.8% of | D | Appendix: All zero-shot configurations |  |  |  |
| 8 | https://docs.pydantic.dev/latest/ | for the three data availability settings described in |  |  |  |

---

## Page 11

| Table 6: CVSS v3.1 full dataset evaluation of all the | Table 8: CVSS v4.0 dataset evaluation of all the zero- |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| zero-shot prompting approaches with four LLMs. | shot prompting approaches with four LLMs. |  |  |  |  |  |  |  |  |  |  |
| Method | A | wF1 | MF1 | MAE | MSE | Method | A | wF1 | MF1 | MAE | MSE |
| 0s FVP o3-mini | 0.846 | 0.836 | 0.722 | 1.200 | 3.991 | 0s FVP o3-mini | 0.701 | 0.684 | 0.519 | 1.268 | 2.763 |
| 0s FVP GPT-4o | 0.754 | 0.743 | 0.643 | 1.655 | 4.861 | 0s FVP LLaMA3 | 0.660 | 0.680 | 0.523 | 1.850 | 6.614 |
| 0s FVP LLaMA3 | 0.739 | 0.733 | 0.593 | 1.694 | 6.178 | 0s FVP GPT-4o | 0.629 | 0.624 | 0.486 | 1.379 | 3.545 |
| 0s FVP DeepSeek | 0.614 | 0.532 | 0.352 | 2.654 | 10.235 | 0s FVP DeepSeek | 0.543 | 0.442 | 0.251 | 2.334 | 7.648 |
| 0s STD o3-mini | 0.804 | 0.793 | 0.676 | 1.609 | 6.000 | 0s STD o3-mini | 0.715 | 0.710 | 0.564 | 1.187 | 2.596 |
| 0s STD GPT-4o | 0.757 | 0.765 | 0.651 | 1.317 | 3.343 | 0s STD DeepSeek | 0.627 | 0.616 | 0.473 | 1.092 | 1.886 |
| 0s STD DeepSeek | 0.741 | 0.740 | 0.617 | 1.430 | 3.815 | 0s STD LLaMA3 | 0.615 | 0.591 | 0.460 | 1.313 | 3.150 |
| 0s STD LLaMA3 | 0.709 | 0.700 | 0.561 | 1.554 | 5.009 | 0s STD GPT-4o | 0.548 | 0.539 | 0.439 | 1.171 | 2.371 |
| 0s DTD o3-mini | 0.767 | 0.755 | 0.654 | 2.095 | 8.747 | 0s DTD o3-mini | 0.780 | 0.765 | 0.586 | 2.103 | 9.970 |
| 0s DTD GPT-4o | 0.750 | 0.751 | 0.634 | 1.494 | 4.573 | 0s DTD DeepSeek | 0.739 | 0.727 | 0.536 | 1.179 | 3.309 |
| 0s DTD DeepSeek | 0.736 | 0.731 | 0.618 | 1.597 | 5.306 | 0s DTD GPT-4o | 0.691 | 0.710 | 0.547 | 1.242 | 2.975 |
| 0s DTD LLaMA3 | 0.697 | 0.676 | 0.562 | 2.934 | 15.788 | 0s DTD LLaMA3 | 0.689 | 0.697 | 0.522 | 1.984 | 7.969 |
| Table 7: CVSS v3.1 low-resource setting evaluation of | Table 9: QSRS Full dataset (left) and low-resource set- |  |  |  |  |  |  |  |  |  |  |
| all the zero-shot prompting approaches with four LLMs. | tings (right) evaluation. Top-3 values for each setting |  |  |  |  |  |  |  |  |  |  |

| Method | A | wF1 | MF1 | MAE | MSE |
| --- | --- | --- | --- | --- | --- |
| 0s FVP LLaMA3 | 0.743 | 0.735 | 0.601 | 1.574 | 5.308 |

0s FVP DeepSeek 0.613 0.526 0.344 2.701 10.956

0s STD DeepSeek 0.741 0.736 0.625 1.401 3.773

| 0s STD LLaMA3 | 0.726 | 0.713 | 0.595 | 1.537 | 4.564 |
| --- | --- | --- | --- | --- | --- |
| 0s DTD o3-mini | 0.763 | 0.749 | 0.649 | 2.071 | 8.552 |
| 0s DTD GPT-4o | 0.752 | 0.750 | 0.631 | 1.448 | 4.443 |

0s DTD DeepSeek 0.741 0.733 0.625 1.391 4.093

Sections 4.1, 4.2 and 4.3, respectively. Within each

configuration, the entries are sorted in descending

order according to the average of A, wF1, and MF1.

ods from Sec.4 in the light of works from Category

8 CVSS metrics for each sample and compute the

resulting severity score with the CVSS v3.1 Calcu-

are marked in bold , italic bold and italic , respectively.

Worst Case Label 0.173 0.051 0.074 0.211 0.074 0.087

DistilBERT-E 0.718 0.722 0.454 0.677 0.677 0.412

24s STD GPT-4o 0.773 0.775 0.515 0.770 0.776 0.580

24s STD LLaMA3 0.759 0.761 0.496 0.784 0.792 0.612

ever, swapped their respective positions). When

moving to the low-resource case (right), the two

few-shots LLMs enter again in the top-3 positions.

The Worst Case Label (WCL) baseline performs

poorly, reflecting class distribution. With only 17%

samples yields 17% and 21% Accuracy by design

configuration

| 0s FVP o3-mini | 0.843 | 0.830 | 0.722 | 1.196 | 3.909 | Full dataset | Low-resource |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0s FVP GPT-4o | 0.747 | 0.727 | 0.626 | 1.756 | 5.366 | Method | A | wF1 | MF1 | A | wF1 | MF1 |
| 0s STD o3-mini | 0.805 | 0.790 | 0.669 | 1.653 | 6.380 | ModernBERT | 0.792 0.793 0.542 0.791 0.797 | 0.580 |  |  |  |  |
| 0s STD GPT-4o | 0.770 | 0.772 | 0.657 | 1.305 | 3.294 | CVEDrill | 0.792 | 0.792 0.534 | 0.691 0.696 0.422 |  |  |  |
| 0s DTD LLaMA3 | 0.706 | 0.682 | 0.592 | 2.774 | 14.687 | behind CVEDrill and ModernBERT (which, how- |  |  |  |  |  |  |
| E | Appendix: Qualitative Severity Rating | and 21% of samples labeled | Critical | in the two data |  |  |  |  |  |  |  |  |
| Scale (QSRS) | scenarios, respectively, assigning this label to all |  |  |  |  |  |  |  |  |  |  |  |
| This section evaluates the performance of the meth- | (cf. left and right part of Table 9, respectively). |  |  |  |  |  |  |  |  |  |  |  |
| II (see Sec.2). As done for the MAE/MSE computa- | F | Appendix: Performance breakdown by |  |  |  |  |  |  |  |  |  |  |
| tion for severity scores, we start from the | predicted | CVSS metric and | SL+LLM Hybrid |  |  |  |  |  |  |  |  |  |
| lator (NVD, 2024b). This score is then quantized | Tables 10, 11 and 12 break down by individual |  |  |  |  |  |  |  |  |  |  |  |
| into the 5 levels (None, Low, Medium, High, Criti- | CVSS metrics the performance for the top-3 meth- |  |  |  |  |  |  |  |  |  |  |  |
| cal) defined by the Qualitative CVSS Severity Rat- | ods in the three scenarios from Tables 2, 3, and 4, |  |  |  |  |  |  |  |  |  |  |  |
| ings (QSRS) (FIRST, 2023a). Notice that no model | as detailed in Secs. 4.1, 4.2, and 4.3. The maximum |  |  |  |  |  |  |  |  |  |  |  |
| is trained/fine-tuned here: we simply re-evaluate | value in each row, for a fixed performance metric, is |  |  |  |  |  |  |  |  |  |  |  |
| performance as a five-class classification problem. | marked in bold. As discussed in Section 4.2, differ- |  |  |  |  |  |  |  |  |  |  |  |
| While we still report the same types of metrics used | ent configurations may perform better for specific |  |  |  |  |  |  |  |  |  |  |  |
| in Tables 2 and 3 in Sec. 4, the results in this section | CVSS metrics and considering an hybrid configu- |  |  |  |  |  |  |  |  |  |  |  |
| refers to a completely different task, and therefore | ration can provide the overall best results. Table |  |  |  |  |  |  |  |  |  |  |  |
| direct numerical comparisons across tasks are not | 11 highlights in gray the method that maximises |  |  |  |  |  |  |  |  |  |  |  |
| applicable. Table 9 shows results for the same data | the average of A, wF1, and MF1, showing that |  |  |  |  |  |  |  |  |  |  |  |
| availability scenarios as Secs.4.1 and 4.2. In the | the optimal "SL+LLM Hybrid" should combine |  |  |  |  |  |  |  |  |  |  |  |
| former (left) the best LLM-based method still falls | ModernBERT for | UI | , | S | , | C | and | I | CVSS metrics, |  |  |  |

---

## Page 12

| Table 10: CVSS v3.1 full dataset evaluation. Perfor- | Table 12: CVSS v4.0 evaluation. Performance of top-3 |
| --- | --- |
| mance of top-3 methods, split by CVSS metric. The | methods, split by CVSS metric. The maximum value in |
| maximum value in each row for a given performance | each row for a given performance metric is marked in |

metric is marked in bold .

Performance of top-3 methods, split by CVSS metric.

CVSS ModernBERT 24s STD GPT-4o 24s STD LLaMA3

Metric A wF1 MF1 A wF1 MF1 A wF1 MF1

AV 0.942 0.941 0.874 0.942 0.943 0.854 0.937 0.938 0.916

A 0.916 0.913 0.725 0.916 0.912 0.730 0.889 0.886 0.666

AVG 0.921 0.920 0.848 0.909 0.908 0.833 0.896 0.893 0.821

This section provides an additional evaluation

where the test data only includes CVEs whose

CVSS has been published after the LLMs’ knowl-

edge cutoff dates: this ensures that the models

could not have been possibly exposed to those ex-

amples during pre-training. We filtered the results

from Tables 2 and 3, retaining only the vulnera-

bilities whose CVSS publication is after the latest

of the LLMs’ cutoff dates, i.e. December 2023.

After the filtering process, we obtained 875 and

431 CVE test samples for the full dataset and the

low-resource scenarios, respectively. For brevity,

Table 13 only reports the supervised baselines and

LLM few-shot configurations. Notice that the low-

resource scenario already includes only samples

disclosed in 2024 (cf. Sec. 4.2), thus, by design, all

of them have the corresponding CVSS published

after December 2023. In other words, the right part

of Table 13 is identical to Table 3 and is included

here just for the convenience of the reader. From

bold .

SI 0.658 0.604 0.456 0.605 0.530 0.353 0.474 0.485 0.462

SA 0.789 0.732 0.418 0.684 0.656 0.360 0.553 0.579 0.338

3 values for each setting are marked in bold , italic bold

and italic , respectively.

24s STD GPT-4o 0.909 0.908 0.827 0.909 0.908 0.833

24s STD LLaMA3 0.893 0.891 0.798 0.896 0.893 0.821

tions 4.1 and 4.2. For the full dataset case (left), the

ernBERT, which however swapped their respective

positions in the ranking. For the low-resource case

(right), as already discussed in Section 4.2, GPT-

4o and LLaMA3 move just behind ModernBERT.

This additional evaluation suggests that the perfor-

mance of LLMs for this prediction task should not

be attributed to the memorization of examples the

LLM may have been exposed to during the pre-

processing phase.

| CVSS | CVEDrill | ModernBERT | 24s STD GPT-4o | CVSS | 0s DTD o3-mini | 0s DTD DeepSeek | 0s STD o3-mini |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metric | A | wF1 | MF1 | A | wF1 | MF1 | A | wF1 | MF1 | Metric | A | wF1 | MF1 | A | wF1 | MF1 | A | wF1 | MF1 |
| AV | 0.938 0.937 0.798 0.941 0.941 0.830 | 0.944 0.944 0.834 | AV | 0.947 0.947 0.962 | 0.789 0.787 0.774 0.868 0.865 0.836 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| AC | 0.976 0.974 0.802 | 0.975 0.969 0.750 0.965 0.963 0.734 | AC | 0.974 | 0.961 0.493 0.921 0.934 0.479 | 0.974 0.978 0.826 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PR | 0.851 0.849 0.826 | 0.857 0.857 0.835 | 0.854 0.853 0.833 | AT | 0.789 0.804 0.756 | 0.632 0.659 0.604 0.526 0.559 0.504 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| UI | 0.957 0.957 0.952 | 0.957 0.957 0.952 | 0.933 0.934 0.926 | PR | 0.921 0.920 0.889 0.921 | 0.917 0.855 | 0.921 | 0.918 0.836 |  |  |  |  |  |  |  |  |  |  |  |
| S | 0.976 0.976 0.962 | 0.974 0.974 0.959 0.946 0.947 0.920 | UI | 0.868 0.859 | 0.590 | 0.868 | 0.856 | 0.650 0.868 | 0.819 0.562 |  |  |  |  |  |  |  |  |  |  |
| C | 0.906 0.905 | 0.891 0.906 0.905 | 0.891 | 0.893 0.892 0.874 | VC | 0.500 0.543 0.373 0.553 0.589 0.375 | 0.763 0.759 0.500 |  |  |  |  |  |  |  |  |  |  |  |  |
| I | 0.911 0.911 0.909 | 0.901 0.901 0.899 0.887 0.886 0.882 | VI | 0.816 0.806 0.680 | 0.789 0.757 0.561 | 0.816 | 0.781 0.580 |  |  |  |  |  |  |  |  |  |  |  |  |
| A | 0.921 0.917 | 0.724 0.914 0.913 | 0.745 | 0.902 0.902 0.732 | VA | 0.711 0.684 0.470 | 0.763 0.763 0.522 | 0.737 0.727 0.498 |  |  |  |  |  |  |  |  |  |  |  |
| AVG | 0.929 0.928 0.858 | 0.928 0.927 0.858 0.915 0.915 0.842 | SC | 0.605 0.553 | 0.361 | 0.605 | 0.551 | 0.365 | 0.368 0.345 0.263 |  |  |  |  |  |  |  |  |  |  |
| Table 11: CVSS v3.1 low-resource dataset evaluation. | AVG | 0.780 0.765 0.586 | 0.739 0.727 0.536 0.715 0.710 0.564 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The maximum value in each row for a given perfor- | Table 13: LLM knowledge cutoff-aware evaluation on |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| mance metric is marked in | bold | . | full dataset (left) and low-resource settings (right). Top- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| AC | 0.956 0.949 0.732 0.949 0.946 0.737 | 0.963 0.957 0.780 | Full dataset (875) | Low-resource (431) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PR | 0.852 0.850 0.783 | 0.856 0.852 0.785 | 0.831 0.826 0.746 | Method | A | wF1 | MF1 | A | wF1 | MF1 |  |  |  |  |  |  |  |  |  |
| UI | 0.942 0.942 0.938 | 0.914 0.915 0.909 0.903 0.903 0.897 | Worst Case Label | 0.602 0.474 0.278 0.600 0.470 0.278 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| S | 0.961 0.960 0.943 | 0.940 0.940 0.916 0.905 0.897 0.848 | DistilBERT-E | 0.897 0.890 0.729 0.869 0.858 0.673 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| C | 0.884 0.883 0.872 | 0.875 0.875 0.859 0.882 0.882 0.866 | ModernBERT | 0.921 0.919 0.839 0.921 0.920 0.848 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| I | 0.919 0.919 0.917 | 0.879 0.879 0.873 0.858 0.858 0.850 | CVEDrill | 0.920 0.918 0.829 | 0.887 0.876 0.695 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| "24s STD GPT-4o" for | PR | and | A | , and "24s STD | this table, it is possible to draw conclusions sim- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LLaMA3" for | AV | and | AC | . | ilar to what has been previously observed in Sec- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| G | Appendix: LLM knowledge | best LLM-based method is still "24s STD GPT-4o" |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cutoff-aware additional evaluation | and is still outperformed by CVEDrill and Mod- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

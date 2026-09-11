---
title: "Prompting Is All You Need: Automated Android Bug Replay with Large Language Models"
creator: "LaTeX with acmart 2022/10/24 v1.88 Typesetting articles for the Association for Computing Machinery and hyperref 2023-04-22 v7.00x Hypertext links for LaTeX"
pages: 13
---

# Prompting Is All You Need: Automated Android Bug Replay with Large Language Models

> **總頁數**：13 頁

---

## Page 1

Prompting Is All You Need: Automated Android Bug Replay with

Large Language Models

| Sidong Feng | Chunyang Chen |  |  |
| --- | --- | --- | --- |
| Monash University | Monash University |  |  |
| Melbourne, Australia | Melbourne, Australia |  |  |
| sidong.feng@monash.edu | chunyang.chen@monash.edu |  |  |
| ABSTRACT | iPhone apps striving to gain users on Google Play and Apple App |  |  |
| Bug reports are vital for software maintenance that allow users | Store [8]. Once an app is released, its quality is largely ensured by |  |  |
| to inform developers of the problems encountered while using | continuing maintenance activities and one of the most important |  |  |
| the software. As such, researchers have committed considerable | maintenance tasks is to handle bug reports, i.e., documents that |  |  |
| resources toward automating bug replay to expedite the process | describe software bugs with information about what happened and |  |  |
| of software maintenance. Nonetheless, the success of current au- | what the user expected to happen. Along with the observed and |  |  |
| tomated approaches is largely dictated by the characteristics and | expected behavior, bug reports often go on to contain the steps to |  |  |
| quality of bug reports, as they are constrained by the limitations | reproduce (S2Rs) the bugs that assist developers to replicate and |  |  |
| of manually-crafted patterns and pre-defined vocabulary lists. In- | rectify the bugs, albeit with considerable amounts of engineering |  |  |
| spired by the success of Large Language Models (LLMs) in natural | effort [63]. |  |  |
| language understanding, we propose | AdbGPT | , a new lightweight | In an effort to accelerate bug maintenance, numerous researchers |
| approach to automatically reproduce the bugs from bug reports | have worked toward providing automated solutions for bug repro- |  |  |
| through prompt engineering, without any training and hard-coding | duction. Previous studies [27, 55, 80, 81] apply natural language |  |  |
| effort. | AdbGPT | leverages few-shot learning and chain-of-thought | processing (NLP) and machine learning (ML) techniques to extract |
| reasoning to elicit human knowledge and logical reasoning from | the S2R entities (i.e., action type, target component, input value, |  |  |
| LLMs to accomplish the bug replay in a manner similar to a devel- | and scroll direction) from the bug reports, and employ random or |  |  |
| oper. Our evaluations demonstrate the effectiveness and efficiency | simple guided exploration algorithms for bug reproduction. Un- |  |  |
| of our | AdbGPT | to reproduce 81.3% of bug reports in 253.6 seconds, | fortunately, in many cases, the S2Rs in the bug reports present |
| outperforming the state-of-the-art baselines and ablation studies. | significant challenges to previous automated approaches of bug |  |  |
| We also conduct a small-scale user study to confirm the usefulness | replay, and can even be difficult for professional developers to re- |  |  |
| of | AdbGPT | in enhancing developers’ bug replay capabilities. | produce manually [11–13, 45, 83]. First, the S2Rs are often unclear, |

CCS CONCEPTS

• Software and its engineering → Software testing and debug-

KEYWORDS

ACM Reference Format:

Sidong Feng and Chunyang Chen. 2024. Prompting Is All You Need: Auto-

Permission to make digital or hard copies of all or part of this work for personal or

author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or

© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.

imprecise, and ambiguous, owing to the cognitive and lexical gap

between users and developers.

s1. Open bookmark

s3. Create another one with name “b”

s4. Click “a”

s6. App crash

steps. In s3 , to “create another one”, a deep comprehension of the

‘b’ ”. Last but not least, in s5 , the conjunction word “after” alters

| ging | . | s2. | Tap “add new bookmark” and create a name with “a” |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| automated bug replay, large language model, prompt engineering | s5. | Go back to bookmark after changing name “a” to “b” |  |  |  |  |  |
| mated Android Bug Replay with Large Language Models. In | 2024 IEEE/ACM | Given the S2R shown above, extracting entities from the S2R re- |  |  |  |  |  |
| 46th International Conference on Software Engineering (ICSE 2024), April | quires a robust semantic and syntactic understanding. For instance, |  |  |  |  |  |  |
| arXiv:2306.01987v3 [cs.SE] 8 May 2024 | 14–20, 2024, Lisbon, Portugal. | ACM, New York, NY, USA, 13 pages. https: | the two “create” words in | s2 | and | s3 | are not semantically identical; |
| //doi.org/10.1145/3597503.3608137 | one refers to “input” while the other refers to “repeat” the previous |  |  |  |  |  |  |
| 1 | INTRODUCTION | specific creation steps from the previous steps is needed. Further- |  |  |  |  |  |
| Mobile applications have gained great popularity in recent years [17, | more, a step may contain multiple sub-steps, such as | s5 | , which can |  |  |  |  |
| 18, 30]. There have been over 3.8 million Android apps and 2 million | be divided into “go back to bookmark” and “change name ‘a’ to |  |  |  |  |  |  |
| classroom use is granted without fee provided that copies are not made or distributed | the temporal order of the steps, meaning “change name ‘a’ to ‘b’ ” |  |  |  |  |  |  |
| for profit or commercial advantage and that copies bear this notice and the full citation | should be executed first, followed by “go back to bookmark”. These |  |  |  |  |  |  |
| on the first page. Copyrights for components of this work owned by others than the | challenges surpass pre-defined word lists and are difficult to address |  |  |  |  |  |  |
| republish, to post on servers or to redistribute to lists, requires prior specific permission | using specific patterns based on previous works. Second, the S2Rs |  |  |  |  |  |  |
| and/or a fee. Request permissions from permissions@acm.org. | are often incomplete, and developers from more than 1.3k open- |  |  |  |  |  |  |
| ICSE 2024, April 14–20, 2024, Lisbon, Portugal | source projects wrote a letter to GitHub expressing their frustration |  |  |  |  |  |  |
| ACM ISBN 979-8-4007-0217-4/24/04. . . $15.00 | of the S2Rs are often missing in the bug reports [9], and requested |  |  |  |  |  |  |
| https://doi.org/10.1145/3597503.3608137 | a solution that would encourage users to include them. So much so |  |  |  |  |  |  |

---

## Page 2

ICSE 2024, April 14–20, 2024, Lisbon, Portugal Feng et al.

that the previous automated approaches are unable to replicate the

bugs.

Emerging Large Language Models (LLMs), such as GPT-3 [14],

PaLM [21], RoBERTa [56], T5 [64], have been trained on ultra-

large-scale corpora and exhibit promising performance in natural

language understanding and logical reasoning. For example, GPT-

3 [14] (Generative Pre-trained Transformer3) from OpenAI with

retrieve media information [52, 69], guide cloze selection [60], etc.

The recent success of ChatGPT [7] based on GPT-3.5 demonstrates

In this paper, we propose a novel approach called AdbGPT to

which is extremely lightweight compared to NLP with manually-

crafted patterns and ML with massive training data. To extract the

Since the LLMs are not specifically designed to handle bug reports,

guiding bug replay and show that our approach can successfully

reproduce 81.3% of bugs, outperforming the baselines and ablations.

the baselines, saving an average of 1105.17 seconds per bug report.

Apart from the performance of our tool, we also assess the per-

ceived usefulness of our AdbGPT by conducting a small-scale user

study on replaying bugs from 5 real-world bug reports. Through

the study, we provide initial evidence of the usefulness of AdbGPT

in facilitating bug replay. The contributions of this paper are as

follows:

• We propose a lightweight approach, AdbGPT 1

mated bug replay.

2 BACKGROUND

reproduce bugs.

One common paradigm to master a specific task is to fine-tune

the models [50]. The fundamental of model fine-tuning is big data,

which is labor-intensive and costly. With the increasing ability of

LLMs, in-context learning has shifted to a new paradigm, known

as zero-shot learning, where LLMs make predictions by directly de-

scribing the desired output. While zero-shot learning shows promis-

ing performances in various training tasks by leveraging prior

1 https://github.com/sidongfeng/AdbGPT

| 175 billion parameters trained on billions of resources can smartly | Figure 1: The process of prompt engineering. |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| its remarkable ability to comprehend human questions and act as | • | This is the first work to exploit LLMs into bug report analysis |  |  |  |  |  |  |  |
| a knowledgeable assistant for interacting with users. Inspired by | and GUI guidance, paving the way for new opportunities in |  |  |  |  |  |  |  |  |
| the impressive advancements of LLMs in the fields of information | software engineering tasks. |  |  |  |  |  |  |  |  |
| retrieval, selection guidance, and role-playing, we designate the | , that utilizes |  |  |  |  |  |  |  |  |
| LLMs as expert developers capable of extracting entities from bug | prompt engineering with few-shot learning and chain-of- |  |  |  |  |  |  |  |  |
| reports and guiding replays from a set of dynamic GUI components. | thought reasoning to harness LLMs’ knowledge for auto- |  |  |  |  |  |  |  |  |
| A | utomatically repro | D | uce | B | ugs using LLMs. | AdbGPT | consists of two | • | Comprehensive experiments, including the performance eval- |
| phases: i) | S2R Entity Extraction | and ii) | Guided Replay | . Notably, the | uation of | AdbGPT | and its detailed qualitative analysis, reveal |  |  |
| underlying approach of | AdbGPT | for these two phases is prompt | the capabilities of LLMs in bug replay. A user study to further |  |  |  |  |  |  |
| engineering, i.e., prompting the tasks to generate desired output, | demonstrate the usefulness of our approach. |  |  |  |  |  |  |  |  |
| S2R entities, we first provide the LLMs with the knowledge of en- | We briefly discuss Large Language Models (LLMs), and in-context |  |  |  |  |  |  |  |  |
| tity specifications, including available actions and action primitives. | learning and chain-of-thought reasoning that we adapt in | AdbGPT | . |  |  |  |  |  |  |
| we employ few-shot learning by giving a few representative ex- | 2.1 | Large Language Models |  |  |  |  |  |  |  |
| amples to help LLMs recognize the task of S2R entity extraction. | Pre-trained Large Language Models (LLMs) introduce a new era in |  |  |  |  |  |  |  |  |
| Additionally, we provide LLMs with detailed chain-of-thought rea- | natural language understanding. It is trained on ultra-large-scale |  |  |  |  |  |  |  |  |
| soning from developers, endowing it to extract S2R entities with | corpora and can support a wide range of natural language process- |  |  |  |  |  |  |  |  |
| the same thought process as developers. Given the inferred S2R | ing tasks with prompt engineering. By simply describing natural |  |  |  |  |  |  |  |  |
| entity extraction from the LLMs, we next prompt LLMs to dynam- | language prompts, LLMs can be invoked to perform specific tasks |  |  |  |  |  |  |  |  |
| ically guide the replay according to the GUI screens. To provide | without requiring additional training or hard coding. Figure 1 il- |  |  |  |  |  |  |  |  |
| the current GUI information to the LLMs, we propose a novel GUI | lustrates the process of prompt engineering. Given an input/test |  |  |  |  |  |  |  |  |
| encoding algorithm to ensure the integrity of the information and | prompt (sentence with task-specific instructions), the input em- |  |  |  |  |  |  |  |  |
| the effectiveness of encoding. By giving a few examples with inter- | bedding layer encodes it through word embedding. To compre- |  |  |  |  |  |  |  |  |
| mediate reasoning, LLMs infer the target components to operate | hend prompts and generate corresponding answers, LLMs employ |  |  |  |  |  |  |  |  |
| on the GUI screen, repeating the steps to trigger the bugs. | a Transformer model [71]. In detail, the multi-self attention layer is |  |  |  |  |  |  |  |  |
| We conduct a comprehensive evaluation to measure the effec- | used to divide a whole high-dimensional space into several different |  |  |  |  |  |  |  |  |
| tiveness and efficiency of our | AdbGPT | . First, we evaluate the per- | subspaces to calculate the similarity. The normalization layer is |  |  |  |  |  |  |
| formance of our | AdbGPT | in extracting S2R entities from 88 bug | implemented through a normalization step that fixes the mean and |  |  |  |  |  |  |
| reports. Compared with two state-of-the-art baselines and two ab- | variance of each layer’s inputs. The feed-forward layer compiles |  |  |  |  |  |  |  |  |
| lation studies, our approach achieves significantly higher accuracy, | the data extracted by previous layers to form the final answer. In |  |  |  |  |  |  |  |  |
| i.e., 90.4% and 90.8% in step extraction and entity extraction, re- | this work, we prompt the LLMs to extract S2R entities and generate |  |  |  |  |  |  |  |  |
| spectively. Second, we evaluate the performance of our | AdbGPT | in | dynamic actionable operations, and decode the LLMs’ feedback to |  |  |  |  |  |  |
| In addition, our approach is much more efficient compared with | 2.2 | In-context Learning |  |  |  |  |  |  |  |

---

## Page 3

Prompting Is All You Need: Automated Android Bug Replay with Large Language Models ICSE 2024, April 14–20, 2024, Lisbon, Portugal

knowledge from training resources, it remains challenging to apply

to unseen tasks [14, 25, 43]. To overcome this challenge, few-shot

learning is utilized to augment the context with a few examples of

desired inputs and outputs (see Figure 1). This enables LLMs to rec-

ognize the input prompt syntax and patterns of the output. In our

work, as LLMs are not specifically trained to understand, analyze,

organize, and reproduce bug reports, we adopt few-shot learning

as the in-context paradigm to help LLMs extract S2R entities and

guide bug replay.

2.3 Chain-of-Thought Reasoning

While few-shot learning has proven effective for simple tasks with

a few examples of <input, output> , it faces difficulties with more

complicated tasks that require logical thinking and multiple steps to

solve, such as arithmetic or commonsense reasoning questions [47,

54, 72, 82]. To elicit the capability of LLMs’ reasoning, many re-

searchers pioneer the idea of using rationales as the intermediate

steps in examples. This idea is formulated as chain-of-thought rea-

soning [74], i.e., <input, reasons, output> in Figure 1. Our task of

extracting S2R entities and guiding bug replay is not simple, it re-

quires logical thinking to understand the bug reports and a coherent

series of intermediate steps to trigger the bugs. As a result, we em-

ploy chain-of-thought reasoning to endow the LLMs to reproduce

the bugs through the minds of expert developers.

3 ADBGPT APPROACH

Given a bug report and the app, we propose an automated approach

phases using different ad-hoc methods, such as natural language

processing for extracting S2R entities and greedy algorithms for

The first phase of our approach is to understand, analyze, organize,

and extract the entities from the S2R text in a bug report. Specifically,

we leverage LLMs, equipped with knowledge learned from large-

scale training corpora, to provide an in-depth understanding of

the potential entities presented in the bug report. As discussed

in Section 1, a step can be expressed in various ways and with

Figure 2: The overview of AdbGPT .

actions in this paper.

with, such as a button in the GUI. As a result, we formulate it as

we formulate them using similar linguistic primitives. The Scroll

action requires indicating the direction of the scrolling effect, such

as upward or downward, formulating as [Scroll] [Direction] . The

input action involves the process of entering a specific value into a

text field component. To formulate this action, we use the primitive

[Input] [Component] [Value] .

| to extract the S2R entities and reproduce each step based on the | few-shot learning, we prompt the LLMs in the same way to extract |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| current GUI state to trigger the bugs in the app. The overview | the S2R entities from the test bug report. |  |  |  |  |  |  |
| of our approach is shown in Figure 2, which is divided into two | 3.1.1 | Available actions. | Unlike target components and input values, |  |  |  |  |
| main phases: (i) the | S2R Entity Extraction | phase, which extracts | which are indeterministic and dynamic depending on the current |  |  |  |  |
| the S2R entities defining each step to reproduce the bug report, | GUI, actions that can interact with the device remain consistent. |  |  |  |  |  |  |
| including action types, target components, input values, or scroll | We identify five standard actions as shown in Table 1, including |  |  |  |  |  |  |
| directions; (ii) the | Guided Replay | phase that matches the entities | Tap, Scroll, Input, Double-tap | , and | Long-tap | . While there are other |  |
| in S2R with the GUI states to repeat the bug reproduction steps. | customized actions, such as pinch, multi-handed gestures, etc., they |  |  |  |  |  |  |
| While many works [27, 55, 80, 81] attempt to address these two | are less prevalent. For brevity, we focus on the commonly-used |  |  |  |  |  |  |
| guiding replay, our approach is notably lightweight compared to | 3.1.2 | Action primitives. | As the context of action varies, each ac- |  |  |  |  |
| them, we exploit the single LLMs to address both phases through | tion requires a different set of primitives to represent entities. For |  |  |  |  |  |  |
| novel prompt engineering. | example, the | Tap | action requires a target component to interact |  |  |  |  |
| 3.1 | S2R Entity Extraction | [Tap] [Component] | . Similarly, for | Double-tap | and | Long-tap | actions, |
| different words. Therefore, we first provide LLMs with information | 3.1.3 | In-context learning. | A representative example helps the model |  |  |  |  |
| about entity specifications, including available actions and action | elicit specific knowledge and abstractions needed to complete the |  |  |  |  |  |  |
| primitives, which can be mapped to instructions for device replay. | task. A common strategy for example selection is to randomly sam- |  |  |  |  |  |  |
| To help LLMs recognize our task and infer S2R entities, we provide | ple from a dataset [73]. However, a random bug report may not |  |  |  |  |  |  |
| a few examples of conditioning, such as an S2R as input, a chain- | encompass all the complexities of the task, thereby limiting the abil- |  |  |  |  |  |  |
| of-thought as reasoning, and the final entities as the output. An | ity of LLMs to gain a comprehensive understanding of the problem. |  |  |  |  |  |  |
| example of the prompts is shown in Table 1. With this in-context | To select representative examples, we recruit three professional |  |  |  |  |  |  |

---

## Page 4

ICSE 2024, April 14–20, 2024, Lisbon, Portugal Feng et al.

Table 1: The example of prompt engineering of S2R entity

extraction.

| PROMPT TYPE | INSTANTIATION |
| --- | --- |
| Available actions | Tap, Scroll, Input, Double-tap, Long-tap |
| Action primitives | [Tap] [Component], [Scroll] [Direction], [Input] [Component] |

[Value], [Double-tap] [Component], [Long-tap] [Component]

Example input 1. Open bookmark

2. Tap “add new bookmark” and create a name with “a”

3. Create another one with name “b”

4. Click “a”

5. Go back to bookmark after changing name “a” to “b”

6. App crash

1st step is “Open bookmark”. The action is “open” and the

Chain-of-Thought target component is “bookmark”. However, there is no explicit

“open” in the Available actions list. Therefore, we select the

closest semantic action “tap”. Following the Action primitives,

2nd step is “Tap ‘add new bookmark’ and create a name with

‘a’ ”. Due to the conjunction word “and”, this step can be sepa-

rated into two sub-steps, “Tap ‘add new bookmark’ ” and “create

3rd step is “Create another one with name ‘b’ ”. Due to its

‘b’ ”. Due to the conjunction word “after”, this step can be sepa-

should be executed first, followed by “go back to bookmark” ...

1. [Tap] [“bookmark”]

5. [Input] [“name”] [“b”]

developers with four-year experience in bug fixing and triaging by

word-of-mouth. First, we give them an introduction to our study

and ask them to interact with the LLMs to become familiar with

thought reasoning is shown in Table 1. In the 1st step, we explicitly

generate a numeric list to represent the extracted S2R in the same

format as our example output, which can be inferred using regular

expressions.

3.2 Guided Replay

with few-shot learning and chain-of-thought reasoning to gen-

| the entity of the first step is [Tap] [“bookmark”]. | Figure 3: Illustration of GUI encoding. |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a name with ‘a’ ” ... | process that leads to the final S2R entities. An example of chain-of- |  |  |  |  |  |  |  |  |  |  |  |  |
| semantic meaning, this step is meant to repeat the previous | explain the action (“Open”) and target component (“bookmark”). |  |  |  |  |  |  |  |  |  |  |  |  |
| steps to add another bookmark with name “b”. Therefore, it | Since “Open” is not listed in the | Available actions | , we map it to the |  |  |  |  |  |  |  |  |  |  |
| should actually be the 2nd step ... | closest semantic action “Tap”. For the 2nd and 5th steps, we explic- |  |  |  |  |  |  |  |  |  |  |  |  |
| 4th | step is “Click ‘a’ ” ... | itly explain the conjunction words that lead to multiple sub-steps |  |  |  |  |  |  |  |  |  |  |  |
| 5th | step is “Go back to bookmark after changing name ‘a’ to | and alternate temporal order. The 3rd step is more complicated, that |  |  |  |  |  |  |  |  |  |  |  |
| rated into two sub-steps, “Go back to bookmark” and “change | we explicitly explain the semantic meaning of the step and its rela- |  |  |  |  |  |  |  |  |  |  |  |  |
| name ‘a’ to ‘b’ ”. The conjunction word “after” also alters the | tionship to the previous steps. Overall, this step-by-step thinking |  |  |  |  |  |  |  |  |  |  |  |  |
| temporal order of the sub-steps, that “change name ‘a’ to ‘b’ ” | leads to the final output of the extracted S2R entities. |  |  |  |  |  |  |  |  |  |  |  |  |
| 6th | step is “App crash”. This step does not have any operations. | 3.1.5 | Prompt construction. | We combine the aforementioned in- |  |  |  |  |  |  |  |  |  |
| Example output | Overall, the extracted S2R entities are: | formation in Table 1 as the input prompt, i.e., ( | ⟨ | Available actions | ⟩ |  |  |  |  |  |  |  |  |
| 2. [Tap] [“add new bookmark”] | + | ⟨ | Action primitives | ⟩ | + | ⟨ | Example input | ⟩ | + | ⟨ | Chain-of-Thought | ⟩ | + |
| 3. [Input] [“name”] [“a”] | ⟨ | Example output | ⟩ | ). Note that, due to the robustness of the LLMs, |  |  |  |  |  |  |  |  |  |
| 4. [Tap] [“add new bookmark”] | the prompt sentence does not need to adhere strictly to grammar |  |  |  |  |  |  |  |  |  |  |  |  |
| 6. [Tap] [“a”] | rules [14]. Next, we input the test bug report as the test prompt and |  |  |  |  |  |  |  |  |  |  |  |  |
| 7. [Input] [“name”] [“b”] | query for the S2R entities. Due to the advantage of few-shot learn- |  |  |  |  |  |  |  |  |  |  |  |  |
| 8. [Tap] [“back”] | ing and chain-of-thought reasoning, the LLMs will consistently |  |  |  |  |  |  |  |  |  |  |  |  |
| our task. Each developer is then asked to independently review a | The second phase is to explore the apps to match the extracted |  |  |  |  |  |  |  |  |  |  |  |  |
| large-scale of bug reports collected from previous works [28, 29] | S2R entities to a sequence of GUI events to reproduce the bugs. |  |  |  |  |  |  |  |  |  |  |  |  |
| and select the challenging ones. After 1.5 hours of initial reviewing, | A seemingly straightforward solution [27, 80, 81] is to use lexical |  |  |  |  |  |  |  |  |  |  |  |  |
| each developer on average examines 110 bug reports and selects 7 | computation to match the extracted components against the dis- |  |  |  |  |  |  |  |  |  |  |  |  |
| as challenging. The developers then meet and discuss the represen- | played text of the components on the current GUI screen. However, |  |  |  |  |  |  |  |  |  |  |  |  |
| tatives of the selection and refine the dataset until a consensus is | as explained in Section 1, this process of component mapping is |  |  |  |  |  |  |  |  |  |  |  |  |
| reached. In total, we collect 15 bug reports as our representative | limited due to the issues of missing steps, i.e., there are no matching |  |  |  |  |  |  |  |  |  |  |  |  |
| dataset, with an example in Table 1. | components on the GUI screen. To address this, we adopt LLMs |  |  |  |  |  |  |  |  |  |  |  |  |
| 3.1.4 | Chain-of-thought reasoning. | Giving a chain-of-thought rea- | erate dynamic guidance on the GUI screen, enabling automatic |  |  |  |  |  |  |  |  |  |  |
| soning, it endows the LLMs to generate a coherent series of in- | reproduction of the steps even when a step is missing. One chal- |  |  |  |  |  |  |  |  |  |  |  |  |
| termediate steps that lead to a reasonable output. To employ this | lenge in using LLMs for GUI guidance is that they can only process |  |  |  |  |  |  |  |  |  |  |  |  |
| paradigm, we ask the developers to independently write the chain- | reasonably sized text input. To help LLMs inherently understand |  |  |  |  |  |  |  |  |  |  |  |  |
| of-thought reasoning for each bug report in the representative | GUI screens, we propose a novel method to transfer the GUIs into |  |  |  |  |  |  |  |  |  |  |  |  |
| dataset, following the previous study [74]. The three developers | domain-specific prompts that the LLMs can understand. Given each |  |  |  |  |  |  |  |  |  |  |  |  |
| and the first author then meet and discuss the optimal reasoning | step and its current GUI screen, we prompt the LLMs to generate |  |  |  |  |  |  |  |  |  |  |  |  |
| for each bug report, aiming to express a clear step-by-step thinking | the target component to operate on, ultimately triggering the bug. |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 5

| Prompting Is All You Need: Automated Android Bug Replay with Large Language Models | ICSE 2024, April 14–20, 2024, Lisbon, Portugal |  |  |  |
| --- | --- | --- | --- | --- |
| 3.2.1 | GUI encoding. | To prompt the LLMs to guide bug replay ac- | Table 2: The examples of prompt engineering of guide replay. |  |
| cording to the GUIs, we need to dynamically depict the current GUI | PROMPT TYPE | INSTANTIATION |  |  |
| screen, as well as its contained component information, such as | Example 1 |  |  |  |
| text, type, image, etc. To design our screen encoding, we leverage | GUI encoding | <html> | ... | </html> |

the insight that if our GUI encoding falls within the training data

| Example input | If I need to [Tap] [“Sign in”], which component id should I |
| --- | --- |
| distribution of LLMs, it is more likely to perform better [20, 53, 84]. | operate on the GUI? |

There is no explicit “Sign in” component in the current GUI

| Since most of the LLMs’ training data is typically scraped from the | Chain-of-Thought | screen. However, there is a semantic closest component “Log |  |  |  |
| --- | --- | --- | --- | --- | --- |
| raw web page [14], we encode a GUI in a text by converting its view | in” button. The id attribute of “Log in” component is 6. So, we |  |  |  |  |
| hierarchy data into HTML syntax. However, there are two funda- | could potentially operate on [id=6] in the screen. |  |  |  |  |
| mental limitations. First, the native classes in the view hierarchy | Example output | [id=6] |  |  |  |
| don’t always match HTML tags, for instance, a | <CheckBox> | in the | Example 2 |  |  |
| hierarchy corresponds to a combination of | <input type="checkbox"> | GUI encoding | <html> | ... | </html> |
| and | <label> | . Second, including all properties of GUI components | Example input | If I need to [Tap] [“darkmode”], which component id should I |  |

operate on the GUI?

| will result in excessively long HTML text that may influence the | There is no explicit and semantic similar “darkmode” compo- |  |
| --- | --- | --- |
| understanding of LLMs. | Chain-of-Thought | nent in the current GUI screen, so it appears a [MISSING] step. |
| Therefore, we adopt a heuristic approach to convert the view | However, “darkmode” could be related to the “display” button |  |

in the screen. The id attribute of “display” component is 1. So,

hierarchy of the GUI screen into HTML text. Note that since the we could potentially operate on [id=1] component in the screen.

view hierarchy is not designed to be encoded in HTML syntax, a Example output [MISSING] [id=1]

perfect one-to-one conversion does not exist. Our goal is to make

the converted view hierarchy look and function similar to the HTML

| syntax. An example of the GUI screen and the encoded HTML text | To synthesize the missing step, we randomly omit 0 to 2 steps in |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| is illustrated in Figure 3. The encoding is conducted by traversing | the bug reports. Given these examples where steps may or may not |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the view hierarchy tree using a depth-first search. We convert each | be missing, we ask the three developers to validate the examples |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| node into HTML syntax, preserving a related subset of properties | and select the challenging ones following similar procedures in |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| from the view hierarchy. | Section 3.1.3, resulting in 5 representative examples as the dataset. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| • | resource_id | : the unique resource id of component | 3.2.3 | Chain-of-thought reasoning. | We further ask the three devel- |  |  |  |  |  |  |  |  |  |  |
| • | class | : the native component type | opers to write their chain-of-thought reasoning, leading to the final |  |  |  |  |  |  |  |  |  |  |  |  |
| • | text | : the text of component | output. The documenting process is similar to the previous phase |  |  |  |  |  |  |  |  |  |  |  |  |
| • | content_desc | : the description of visual component | in Section 3.1.4, with independent writing followed by a discussion |  |  |  |  |  |  |  |  |  |  |  |  |
| We first map the classes to HTML tags with similar functionali- | to select the most representative step-by-step reasoning. We show |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ties using an ad-hoc heuristic method. For example, the | TextView | two particular reasoning in Table 2. In Example 1, we explicitly |  |  |  |  |  |  |  |  |  |  |  |  |  |
| is mapped to the | <p> | tag as they both present texts. Similarly, | explain a semantic example of a guiding step that does not exactly |  |  |  |  |  |  |  |  |  |  |  |  |
| the | Button | is mapped to the | <button> | tag; and | ImageView | to the | component match S2R (“Sign in”) and GUI (“Log in”). In Example 2, |  |  |  |  |  |  |  |  |
| <img> | tag. For special classes in the view hierarchy (e.g., | <EditText> | , | we explicitly explain an example of guiding a missing step with a |  |  |  |  |  |  |  |  |  |  |  |
| <CheckBox> | , | <RadioButton> | ), we use a combination of | <input> | and | potential target component and a missing tag. |  |  |  |  |  |  |  |  |  |
| <label> | , aligning with HTML syntax. Note that we focus on the most | 3.2.4 | Prompt construction. | We provide a few examples with their |  |  |  |  |  |  |  |  |  |  |  |
| commonly-used classes for simplicity, and the rest of the classes, | chain-of-thought as input prompt, i.e., ( | ⟨ | GUI encoding | ⟩ | + | ⟨ | Example |  |  |  |  |  |  |  |  |
| such as | <VideoView> | , are mapped to the | <div> | tag. | input | ⟩ | + | ⟨ | Chain-of-Thought | ⟩ | + | ⟨ | Example output | ⟩ | ). Given each step |
| Then, we insert the text properties of the component in between | generated by the S2R entity extraction phase and the current GUI |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the opening and closing HTML tags, following the standard syn- | encoding as the test prompt, we then query for the target compo- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tax of texts in HTML. The resource_id property usually contains | nent selection to reproduce the step. Note that we infer the target |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| additional descriptions of a component’s functionality or purpose, | component using “id”, which is more efficient and space-saving |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| written by developers. For example, a resource_id of “submit_btn” | than spelling out the complete HTML tag. In the scenario of missing |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| refers to the functionality of submit. We insert it in the “class” at- | steps, the output prompt will additionally predict a “MISSING” tag |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tributes in HTML to help the models understand the screen context. | to allow us to iteratively explore the steps in the app until the target |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For the | ImageView | component, we further insert the content_desc | component is found. If LLMs fail to explore a potential target com- |  |  |  |  |  |  |  |  |  |  |  |  |
| as the “alt” attribute in the HTML to express the accessibility to the | ponent to recover the missing steps (e.g., no “id” in the inference), |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| image in the GUI screen. Lastly, we follow the traversing order in | we go back to the previous step and prompt the models to explore |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the view hierarchy tree to insert unique numeric indexes to each | a new component. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

element as the "id" attribute.

| 3.2.2 | In-context learning. | It can be extremely laborious and time- | 3.3 | Implementation |
| --- | --- | --- | --- | --- |
| consuming to manually collect representative examples for guided | For the LLMs, we use the state-of-the-art ChatGPT model [7]. Ac- |  |  |  |
| replay, such as checking whether there is a step missing and iden- | cording to a small-scale pilot study, we set the number of few-shot |  |  |  |
| tifying the target components that may trigger the bugs. To this | learning examples in the range of 1 to 3. This is how many exam- |  |  |  |
| end, we aim to synthesize a few representative examples to help | ples can fit in the LLM’s implicit maximum input tokens (i.e., 4,096 |  |  |  |
| the LLMs understand the challenges of missing steps in the S2Rs. | for ChatGPT). As the LLMs may generate verbose output (such as |  |  |  |

---

## Page 6

| ICSE 2024, April 14–20, 2024, Lisbon, Portugal | Feng et al. |  |  |
| --- | --- | --- | --- |
| repeat questions, chain-of-though reasons, etc.), we use “[]” to infer | students through the university’s internal slack channel and they |  |  |
| the specific prediction, such as entity for S2R entity extraction, and | were compensated with $12 USD per hour. They had experience |  |  |
| target component id attribute or missing step flag for guided replay. | in Android development and bug reproduction. To ensure accurate |  |  |
| Note that, users may describe input actions vaguely, for example, | annotations, the process began with initial training. First, we pro- |  |  |
| “enter the name”. To address this, we set a “test” value if there is no | vided them with an introduction to our study and an example set |  |  |
| explicit input value in the step. | of annotated bug reports where the authors had annotated the S2R |  |  |
| Our | AdbGPT | is implemented as a fully automated bug replay | entities. Then, we asked them to pass an assessment test. The two |
| tool. In detail, we use Genymotion [6] for running and controlling | annotators were then assigned the experimental set of bug reports |  |  |
| the virtual Android device, Android UIAutomator [5] for dumping | to label the S2R entities independently, without any discussion. |  |  |
| the GUI view hierarchy, and Android Debug Bridge (ADB) [4] for | After the initial labeling, the annotators met and sanity corrected |  |  |
| replaying the steps. | any subtle discrepancies. Any disagreements were handed over to |  |  |

• RQ1: How accurate is our approach in extracting S2R entities?

• RQ2: How accurate is our approach in guiding bug replay?

• RQ3: How efficient is our approach in bug replay?

• RQ4: How usefulness is our approach for developers in real-

world bug replay?

Experimental Setup. To answer RQ1, we first evaluated the abil-

the first author for the final decision. In total, we obtained 305 re-

possible input values, and the possible scroll directions). Therefore,

we employed the accuracy of the S2R extraction as our evaluation

metric. The higher the accuracy score, the better the approach can

identify the steps in the bug reports.

Baselines. We set up two state-of-the-art methods which are

widely used for S2R entity extraction as the baselines to compare

ponents). Note that we did not adopt Yakusu [27] as a baseline, as

longer maintained.

| 4 | EVALUATION | production steps from 88 bug reports, which contained 305 actions, |  |  |  |
| --- | --- | --- | --- | --- | --- |
| In this section, we describe the procedure we used to evaluate | 291 components, 39 inputs, and 14 directions. |  |  |  |  |
| AdbGPT | in terms of its performance automatically. Since our ap- | Metrics. | An extracted S2R was determined to be correct if all of |  |  |
| proach consists of two main phases, we evaluate each phase of | the following conditions matched the ground-truth, including steps |  |  |  |  |
| AdbGPT | , including S2R Entity Extraction (Section 3.1) and Guided | (i.e., step ordering, sub-step separation) and entities (i.e., the action |  |  |  |
| Replay (Section 3.2). | types of each step, the possible target components if existed, the |  |  |  |  |
| For | RQ1 | , we present the general performance of our approach | with our approach. | ReCDroid | [81] analyzes the dependencies among |
| for S2R entity extraction and the comparison with state-of-the-art | words and phrases from hundreds of bug reports and defines 22 |  |  |  |  |
| baselines. Besides, we also present the performance comparison | grammar patterns to extract the S2R entities. For example, a noun |  |  |  |  |
| among the variations of in-context learning (e.g., few-shot vs zero- | phrase (NP) followed by a “click” action should be the target compo- |  |  |  |  |
| shot) and the contribution of reasoning by comparing the perfor- | nent, etc. We adopted their released repository for evaluation. ReC- |  |  |  |  |
| mance with and without chain-of-thought. For | RQ2 | , we carry out | Droid+ [80] is a later work that scraped bug reports from the issue |  |  |
| experiments to check if our approach can trigger the target com- | track websites, which is out of the scope of this study. Since these |  |  |  |  |
| ponents, comparing with the baselines and ablations. For | RQ3 | , we | two approaches perform the same for S2R entity extraction, we |  |  |
| evaluate the runtime overhead of our approach in bug replay. For | used the ReCDroid in the rest of the paper for simplicity. | MaCa | [55] |  |  |
| RQ4 | , we conduct a small-scale user study to evaluate the perceived | proposes an automated S2R identification tool, which first identifies |  |  |  |
| usefulness of | AdbGPT | for automatically replaying bug reports in | action words based on natural language processing and machine |  |  |
| real-world development environments. | learning classifier, then extracts its related entities (i.e., target com- |  |  |  |  |
| 4.1 | RQ1: Performance of S2R Entity Extraction | it was developed five years ago and many of its libraries are no |  |  |  |
| ity of our approach (in Section 3.1) to accurately identify the S2R | Apart from the baselines, we also added two derivatives of our |  |  |  |  |
| entities from the bug reports. To avoid potential bias, we collected | approach to demonstrate the impact of prompt engineering. In |  |  |  |  |
| the bug reports from the artifacts of three existing open-source | Section 3.1.3, we utilized few-shot learning to help the LLMs under- |  |  |  |  |
| datasets: (i) the evaluation dataset of ReCDroid [80, 81]; (ii) an em- | stand the requirement of our task. Therefore, we set up an ablation |  |  |  |  |
| pirical study on Android bug report reproduction ANDROR2+ [45]; | study to infer the results without any examples, named | AdbGPT | w/o |  |  |
| and (iii) an empirical study of crash bug reports Themis [67]. Due | Few | , which is the well-known method called zero-shot learning. |  |  |  |
| to some overlap across these datasets, we first removed duplicates | To demonstrate the strength of the chain-of-thought outlined in |  |  |  |  |
| if the bug reports were from the same issue repository. The users | Section 3.1.4, we also conducted an ablation study, namely | AdbGPT |  |  |  |
| may report the S2Rs using visual information, such as screenshots | w/o CoT | . Specifically, it provides a few examples of bug reports and |  |  |  |
| or videos [29]. In this work, we focused on textual information, i.e., | the outputs, without any intermediate reasons, and then prompts |  |  |  |  |
| the natural language descriptions of S2Rs, so we further audited | the models to extract the S2R entities from the test bug report. |  |  |  |  |
| the bug reports and retained those only containing textual S2Rs. In | Results. | Table 3 depicts the performance of our approach in |  |  |  |
| total, we collected 88 bug reports as our experimental dataset. | extracting the S2R entities from the bug reports. The performance |  |  |  |  |
| Given the set of experimental bug reports, we needed to manu- | of our approach is significantly better than that of other baselines |  |  |  |  |
| ally identify and generate the ground-truth for S2R entities (specific | in all metrics, i.e., on average 39.3%, and 42.2% more accurate in |  |  |  |  |
| action types, target components, input values, and scroll direction) | step extraction and entity extraction compared with the best base- |  |  |  |  |
| from the bug reports, as the state-of-the-art automated approaches | line (MaCa). In addition, applying few-shot learning and chain-of- |  |  |  |  |
| still cannot 100% accurately infer the entities. We recruited two paid | thought which provide examples with intermediate reasons, can |  |  |  |  |

---

## Page 7

Prompting Is All You Need: Automated Android Bug Replay with Large Language Models ICSE 2024, April 14–20, 2024, Lisbon, Portugal

Table 3: Performance comparison of S2R extraction.

Acc. of Entity Extraction

Method Acc. of

Step Extraction Action Component Input Direction

| ReCDroid | 49.5% | 65.9% | 45.4% | 30.8% | 42.9% |  |
| --- | --- | --- | --- | --- | --- | --- |
| MaCa | 51.1% | 70.1% | 41.6% | 33.3% | 50.0% |  |
| AdbGPT | w/o Few | 83.9% | 81.9% | 84.5% | 87.1% | 85.7% |
| AdbGPT | w/o CoT | 86.9% | 83.6% | 87.6% | 87.1% | 92.9% |
| AdbGPT | 90.4% | 91.1% | 90.0% | 89.7% | 92.9% |  |

endow the LLMs with a better understanding of the task, resulting

in a boost of performance from 84.6%, 87.6% to 90.8%.

To fully explore the reason why our approach outperforms other

baselines, we carry out a qualitative study by investigating the bug

reports which are correctly extracted by our approach but wrongly

extracted by the baselines. We summarize three reasons, including

inconsistent formats, dependent context, and diversified words.

Some representative examples can be seen in Figure 4.

1) Inconsistent formats: The users may employ different formats

to compose bug reports depending on their writing preferences.

Common formats include numeric indexing, list indexing, or using

following these patterns. However, regarding the users’ understand-

ing of the bugs, they may compose the steps under the same state

such as “->” and “then” as shown in Figure 4-A, but the baseline

approaches fail to interpret them as separate steps.

2) Dependent context. Context dependency can occur from a

macro perspective in the bug reports. For example, in Figure 4-

B, the users demonstrate an action of “deleting” a value, which

is equivalent to “leave the EditText empty”, thus, they should be

interpreted as one step. In Figure 4-C, the users may omit duplicate

steps by describing them as “repeat the previous step” or “create

another one”, etc. However, without syntactic awareness, the base-

line approaches do not monitor the relationships among the words

in a sentence, causing inaccurate step extraction.

Context dependency can also occur at a more granular level. The

users may use conjunction words to order the reproduction steps

that differ from their syntactic order. The baseline MaCa proposes

vocabulary of words, the inconsistency of human language still

Albeit the good performance of our approach, we still make the

wrong extraction for some bug reports. We manually check those

incorrect S2R entity extractions and identify one common cause.

The users may write the S2Rs ambiguously, causing the LLMs to

fail to capture the user intent. For example, in Figure 4-G, the users

aim to set the key to “shop” (i.e., [Input] [“key”] [“shop”]) and value

to “*” (i.e., [Input] [“value”] [“*”]). However, due to the missing

to keyword, LLMs misunderstand the S2R and extract the step as

[Input] [“shop”] [“*”]. Note that the LLMs can correctly extract the

S2Rs by adding the to keyword, suggesting that our performance

could be further improved with well-written bug reports.

from the bug reports.

| commas in a line. The baselines can correctly separate the steps | Figure 4: Examples of S2R extraction. |  |
| --- | --- | --- |
| a heuristic approach based on constituency grammar to deal with | 4.2 | RQ2: Performance of Guided Replay |
| common connective words (i.e., “before”, “after”, “when”, etc.), but | Experimental Setup. | To answer RQ2, we evaluated the ability |
| it is limited to less commonly-used words. For instance, in Figure 4- | of our approach (in Section 3.2) to accurately map the entities in |  |
| D, the step “Favorites settings” should happen first, and then the | the S2Rs to the components in the GUIs for bug reproduction. We |  |
| step “Show favorites above search bar”, due to the semantic of the | used our experimental dataset (outlined in Section 4.1), containing |  |
| connective word “under” between the steps, which the baselines | 88 distinct textual S2Rs. However, many S2Rs are no longer repro- |  |
| fail to recognize. | ducible due to two reasons. First, many real-world bugs have been |  |
| 3) Diversified words: | The users may use different words or phrases | fixed and the apps have been patched, making it difficult to find |
| to describe the same concept, making it difficult for baseline ap- | the corresponding previous versions of the apps for reproduction. |  |
| proaches to recognize semantic patterns. This can include syn- | Second, some bugs (e.g., financial, social apps) require extensive |  |
| onyms, alternative phrasing, or even colloquial language. For ex- | information like authentication, database, or specific hardware, |  |
| ample, as shown in Figure 4-E, the users colloquially use “go to”, | which are beyond the scope of this study. To that end, we asked the |  |
| “click”, “choose”, “open”, and “select” to refer to the action of “tap”. | two students to locate the corresponding apps and interact with |  |
| Even for the same word, the user’s choice of expression can affect | them to ensure the S2Rs were reproducible. If the students could |  |
| the recognition, e.g., “click the button” and “the button is clicked” | not reproduce a bug report, the first author would further assess |  |
| in Figure 4-F. While the baselines have identified some common | its reproducibility. As a result, we collected 48 reproducible S2Rs |  |
| poses challenges in recognizing diversified word patterns in bug | Metrics. | To measure the performance of our approach, we em- |
| reports. | ployed reproducibility as the evaluation metric, i.e., whether the |  |

---

## Page 8

ICSE 2024, April 14–20, 2024, Lisbon, Portugal Feng et al.

Table 4: Performance comparison of guided replay.

Bug No. Steps Method

ReCDroid AdbGPT w/o Few AdbGPT w/o CoT AdbGPT

| Anki#4586 | 3 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Anki#5638 | 4 | ✗ | ✗ | ✓ | ✓ |  |  |  |
| Anki#2564 | 3 | ✗ | ✓ | ✓ | ✓ |  |  |  |
| Anki#3224 | 2 | ✗ | ✗ | ✗ | ✓ |  |  |  |
| Anki#10584 | 1 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| AnyMemo#440 | 5 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| Birthdroid#13 | 1 | ✓ | ✗ | ✗ | ✓ |  |  |  |
| NewsBlur#1053 | 5 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| LibreNews#22 | 5 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| LibreNews#23 | 7 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| LibreNews#27 | 4 | ✗ | ✗ | ✗ | ✗ |  |  |  |
| Transistor#63 | 5 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| ScreenCam#25 | 4 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| News#487 | 2 | ✓ | ✗ | ✗ | ✓ |  |  |  |
| k9mail#3255 | 4 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| k9mail#2612 | 3 | ✓ | ✗ | ✗ | ✗ |  |  |  |
| k9mail#2019 | 1 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| openMF#734 | 2 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| FamilyFinance#1 | 6 | ✗ | ✗ | ✗ | ✓ |  |  |  |
| trickytripper#42 | 4 | ✗ | ✗ | ✗ | ✓ |  |  |  |
| NoadPlayer#1 | 4 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| calendula#134 | 2 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| StreetComplete#1093 | 3 | ✗ | ✗ | ✗ | ✗ |  |  |  |
| OmniNotes#592 | 3 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| Markor#1020 | 2 | ✗ | ✓ | ✓ | ✓ |  |  |  |
| Markor#331 | 6 | ✗ | ✗ | ✗ | ✗ |  |  |  |
| KISS#1481 | 5 | ✗ | ✓ | ✓ | ✓ |  |  |  |
| ultrasonic#187 | 3 | ✗ | ✓ | ✓ | ✓ |  |  |  |
| andOTP#500 | 3 | ✗ | ✗ | ✗ | ✗ |  |  |  |
| k9mail#3971 | 3 | ✗ | ✓ | ✓ | ✓ |  |  |  |
| kiwix#1414 | 4 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| kiwix#555 | 2 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| qksms#1155 | 3 | ✗ | ✗ | ✗ | ✗ |  |  |  |
| Aegis#287 | 3 | ✗ | ✗ | ✗ | ✓ |  |  |  |
| AmazeManager#1796 | 5 | ✗ | ✗ | ✗ | ✓ |  |  |  |
| ActivityDiary#285 | 6 | ✗ | ✗ | ✓ | ✓ |  |  |  |
| APhotoManager#116 | 3 | ✗ | ✗ | ✗ | ✗ |  |  |  |
| collect#3222 | 2 | ✗ | ✓ | ✓ | ✓ |  |  |  |
| commons#2123 | 3 | ✗ | ✗ | ✗ | ✗ | Figure 5: Examples of guided replay. |  |  |
| FirefoxLite#5085 | 4 | ✗ | ✓ | ✓ | ✓ |  |  |  |
| nextcloud#1918 | 5 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| nextcloud#5173 | 4 | ✗ | ✓ | ✓ | ✓ |  |  |  |
| osmeditor#729 | 2 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| osmeditor#637 | 4 | ✗ | ✗ | ✗ | ✗ |  |  |  |
| WordPress#11135 | 3 | ✗ | ✓ | ✓ | ✓ | (i.e., 18.8% boost) in the performance of | AdbGPT | , indicating that the |
| WordPress#10302 | 3 | ✓ | ✓ | ✓ | ✓ |  |  |  |
| CineLog#60 | 5 | ✗ | ✗ | ✗ | ✓ | LLMs can better understand the task by processing it step-by-step. |  |  |
| AndrOBD#144 | 3 | ✗ | ✗ | ✗ | ✓ | We further conduct a qualitative analysis to compare the capa- |  |  |
| Reproducibility | - | 45.8% | 58.3% | 62.5% | 81.3% | bilities of our approach with the baselines. Overall, we summarize |  |  |

two common reasons which can be seen in Figure 5.

1) Missing steps: It is a key factor in the failure of automated bug

reproduction in baselines. This issue may arise when users overlook

| method can successfully reproduce the bugs. The higher the repro- | some "unimportant" steps. Without a complete set of instructions, |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ducibility score, the better the approach can replicate the S2Rs on | automated approaches fail to reproduce the steps needed to trigger |  |  |  |  |
| the GUIs to trigger the bugs. | the bugs. In contrast, our approach exploits the semantic under- |  |  |  |  |
| Baselines. | We adopted the state-of-the-art method | ReCDroid | [81] | standing of subsequent steps and the components in the current |  |
| as the baseline to compare with our method. Specifically, ReCDroid | GUI to potentially identify the most probable actions that can re- |  |  |  |  |
| employs a greedy algorithm to search for the matched compo- | store the missing steps. For instance, in Figure 5-A, since there is |  |  |  |  |
| nents on the GUIs by using the word embedding similarity metric | no explicit target component (“support project”) in the current GUI, |  |  |  |  |
| Word2Vec. In addition, we adopted two derivations of our approach | the LLMs can identify the potential component (“AndrOBD”, which |  |  |  |  |
| as the ablation baselines to demonstrate the advantages of | AdbGPT | , | is the project name) due to their semantic correlation. |  |  |
| including without few-shot learning ( | AdbGPT | w/o Few | ), and without | 2) Component mismatch: | Another common reason that makes it |
| chain-of-thought ( | AdbGPT | w/o CoT | ). Note that we did not adopt | difficult for baselines to repeat the step is the component mismatch. |  |
| MaCa [55] as the baseline, as it solely focuses on S2R entity extrac- | There may be two possible reasons why an S2R cannot directly |  |  |  |  |
| tion without including bug replay. | match components on the GUI. First, the users may describe the |  |  |  |  |
| Results. | Table 4 shows detailed results of the reproducibility for | component imprecisely. For instance, in Figure 5-A, the “movies” |  |  |  |
| each bug. Our approach outperforms all the baselines and ablations, | button is described as “films”, making it challenging for automated |  |  |  |  |
| i.e., on average 81.3% compared with 45.8%, 58.3%, and 62.5%, for | approaches to identify the exact GUI component the S2R refers to. |  |  |  |  |
| ReCDroid, | AdbGPT | w/o Few, and | AdbGPT | w/o CoT, respectively. We | Second, for multi-lingual apps, the languages of S2Rs and GUIs may |
| observe that chain-of-thought leads to a substantial improvement | be different. Figure 5-B shows an example that the user reports |  |  |  |  |

---

## Page 9

| Prompting Is All You Need: Automated Android Bug Replay with Large Language Models | ICSE 2024, April 14–20, 2024, Lisbon, Portugal |  |  |
| --- | --- | --- | --- |
| the bug in English while it is reproduced on a GUI in French, caus- | Table 5: Performance comparison of average runtime per bug |  |  |
| ing the reproduction to fail. In contrast, our approach leverages | report. |  |  |
| LLMs, which capture a large-scale corpus and language resources, | Method | S2R Entity Extraction (sec) | Guided Replay (sec) |
| to understand the morphological forms of components including | ReCDroid | 3.75 | 1357.17 |
| abbreviations, synonyms, misspellings, and languages, and search | MaCa | 2.18 | - |

for the most relevant component in the GUI.

Although our approach demonstrates good bug reproducibility,

we still fail to reproduce some unclear S2Rs. For example, the users

starting with “https://”. This could be achieved by understanding

the context information of the input fields and designing linguistic

patterns to prompt LLMs to generate valid input values. We would

like to put it as our future work.

advanced hardware.

AdbGPT 2.11 253.64

Table 6: Performance comparison of usefulness evaluation.

Bug No. Steps

Success Time (sec) Success Time (sec)

| Wechat | 7 | 100% | 493.3 | 100% | 205.1 |
| --- | --- | --- | --- | --- | --- |
| Anki | 8 | 100% | 544.8 | 100% | 349.7 |
| Average | - | 92.5% | 480.7 | 100% | 269.4 |

4.4 RQ4: Usefulness of AdbGPT

Experimental Setup. To investigate the perceived usefulness of

AdbGPT , we conducted a small-scale user study with eight partici-

minutes.

| may not describe the specific values for input fields, as seen in | Participants | AdbGPT |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Figure 5-D. To address it, we generate random text for the input | KISS | 2 | 75% | 423.1 | 100% | 262.9 |
| fields, i.e., the “test” value for the name field. However, some input | NeuroLab | 2 | 100% | 396.5 | 100% | 228.0 |
| fields require valid values, i.e., the URL field requires an input value | Alibaba | 5 | 87.5% | 545.7 | 100% | 301.2 |
| 4.3 | RQ3: Efficiency Performance | pants, including five graduate students and three app developers. |  |  |  |  |
| Experimental Setup. | To answer RQ3, we evaluated the overhead | The participants were recruited from the university’s internal slack |  |  |  |  |
| of our approach by calculating the average time it takes for a bug | channel or through direct contact with the authors. Given that |  |  |  |  |  |
| report to pass through each of the two phases of the | AdbGPT | ap- | the graduate students all have at least 1.5 years of experience in |  |  |  |
| proach. All of our experiments were conducted on the commodity | Android app development and bug replay. The three app develop- |  |  |  |  |  |
| hardware, a 2.6 GHz Macbook Pro with 6 dedicated CPU Intel Core | ers are more professional and have more than two-year working |  |  |  |  |  |
| as the | AdbGPT | engine, and the official Android x86-64 emulator as | experience in Android development in the industry. |  |  |  |
| the device server. Our approach could perform substantially faster | Procedure: | To mitigate the threat of user distraction, we con- |  |  |  |  |
| on specialized hardware. Note that, inferring the entities and guid- | ducted the experiment in a quiet room individually without mutual |  |  |  |  |  |
| ance from ChatGPT (our underlying LLM implementation) can be | discussion. We interviewed the participants using a set of questions |  |  |  |  |  |
| unstable and highly dependent on the ChatGPT server and user vol- | organized in two sessions. The first session aimed to collect infor- |  |  |  |  |  |
| ume. Therefore, we ran the inference three times for our approach | mation on participants’ backgrounds, including their role at the |  |  |  |  |  |
| and the ablation baselines, using the average time for performance | company, the frequency of addressing bug reports and replaying |  |  |  |  |  |
| evaluation. | bugs, the challenges they face in their practices, etc. The second |  |  |  |  |  |
| Metrics. | To measure the overhead of | AdbGPT | , we employed the | session aimed to assess | AdbGPT | ’s potential usefulness in replaying |
| time it takes for both extracting S2R entities from the bug report and | the S2Rs from bug reports. Each participant was asked to reproduce |  |  |  |  |  |
| guiding the bug replay. The less time it takes, the more efficiently | the same set of 5 randomly selected bug reports from issue trackers |  |  |  |  |  |
| the method can reproduce the bugs. | and GitHub. These bug reports were of diverse difficulty ranging |  |  |  |  |  |
| Baselines. | We used | ReCDroid | and | MaCa | as the baselines, as well | from 2 to 8 S2Rs in the bug reports. To minimize the impact of |
| as | AdbGPT | without few-shot and | AdbGPT | without chain-of-thought | stress, participants were allowed to take a short break between |  |
| as the ablation studies of our approach. | each bug replay. We only recorded the time used to reproduce the |  |  |  |  |  |
| Results. | Table 5 shows the performance comparison with the | bug reports, including understanding the textual S2Rs and replicat- |  |  |  |  |
| baselines. Our approach takes | AdbGPT | 255.75 seconds on average | ing the steps in Android. Note that all the experiment apps were |  |  |  |
| to reproduce a bug report, i.e., 2.11 seconds to extract the S2R | pre-installed. Participants had up to 10 minutes for each bug replay. |  |  |  |  |  |
| entities from the bug report and 253.64 seconds to replay the S2R | At the end of the tasks, we showcased the bug replay automatically |  |  |  |  |  |
| in the device. In comparison, it takes the ReCDroid method on | generated by our tool | AdbGPT | and asked participants for feedback, |  |  |  |
| average 1360.92 seconds, indicating the efficiency of our approach | including a 5-Likert scale question about their preference for using |  |  |  |  |  |
| which saves nearly 5x time per bug replay. Notably, our approach | our tool, suggestions for improvement, etc. |  |  |  |  |  |
| accelerates 435% time in guiding replay in the GUI screen compared | Results. | Table 6 shows the detailed experiment results. Although |  |  |  |  |
| with ReCDroid. This is primarily due to missing steps in the S2Rs, | most participants can successfully finish the bug replay on time, |  |  |  |  |  |
| which cause ReCDroid to randomly explore the app with repeated | AdbGPT | reproduces the bug report much faster than that of partici- |  |  |  |  |
| back-and-forth exploration, which is a time-consuming process. In | pants (with an average of 480.7 seconds versus 269.4 seconds). In |  |  |  |  |  |
| contrast, our approach elicits the LLMs to understand the semantics | fact, the average time for participants’ reproduction is underesti- |  |  |  |  |  |
| of the S2R context and current GUI to predict the most probable | mated, because they fail to reproduce 3 bugs within 10 minutes, |  |  |  |  |  |
| components for bridging the missing steps. We expect that the | which means that participants may need more time for bug replay. |  |  |  |  |  |
| overhead of our approach could be further accelerated by more | In contrast, our automated approach finishes all the tasks within 7 |  |  |  |  |  |

---

## Page 10

| ICSE 2024, April 14–20, 2024, Lisbon, Portugal | Feng et al. |  |  |  |
| --- | --- | --- | --- | --- |
| After observing the bug replay automatically generated by | AdbGPT | , | 6.1 | Bug Record and Replay |
| all participants strongly favored using | AdbGPT | in practice, with an | Nurmuradov et al. [59] introduced a record and replay tool for An- |  |
| average preference score of 4.5 out of 5.0. To gain insight into the | droid applications that captures user interactions by displaying the |  |  |  |
| usefulness of our approach, we collect feedback from the partic- | device screen in a web browser. It used event data captured during |  |  |  |
| ipants and summarise two practical challenges of manual replay. | the recording process to generate a heatmap that allows developers |  |  |  |
| First, understanding the S2Rs from the bug reports is surprisingly | to reproduce how users are interacting with an application. Ad- |  |  |  |
| time-consuming, as it involves grasping the context, reordering the | ditional tools including ECHO [68], Reran [37], Barista [46], and |  |  |  |
| steps, analyzing the potential actions and components, etc. Second, | Android Bot Maker [1] are program-analysis-related applications |  |  |  |
| it is difficult to determine the trigger for the missing steps, result- | for the developers to record and replay user interactions. However, |  |  |  |
| ing in participants’ guesses of the action for triggering the next | they required the installation of underlying frameworks such as |  |  |  |
| steps. That trial-and-error makes the bug replay process tedious | replaykit [2], troyd [42], or instrumenting apps which are too heavy |  |  |  |
| and time-consuming. It is especially severe for junior developers | for end users. In contrast to these approaches, our | AdbGPT | is rather |  |
| who are not familiar with the app. | lightweight which just requires natural language descriptions of |  |  |  |
| Participants also provide valuable feedback to help improve | the bug reproduction steps. |  |  |  |
| AdbGPT | . For example, one participant suggests a strategy for in- | Many previous research works have focused on processing bug |  |  |
| teraction between developers and LLMs for bug replay by adding | reproduction steps to automate bug replay. For example, Fazzini et |  |  |  |
| a confidence value to the LLMs. If the inference is unreliable (i.e., | al. [27] proposed Yakusu, a program analysis and natural language |  |  |  |
| the confidence value is low), there will be an interactive conver- | processing tool to generate executable test cases from bug reports. |  |  |  |
| sation to ask developers to confirm the operations. This strategy | Zhao et al. [81] further improved the tool namely ReCDroid, by |  |  |  |
| could efficiently and effectively improve the performance of bug | leveraging the lexical knowledge in the bug reports to automati- |  |  |  |
| reproduction with human-AI collaboration. We will investigate the | cally reproduce crashes. However, these works did not consider |  |  |  |
| possible solution in our future work. | the temporal order of S2Rs (e.g., when, after, etc.). Liu et al. [55] |  |  |  |

proposed MaCa, a natural language processing (NLP) and machine

learning (ML) approach to normalize the S2Rs in the bug reports

and extract the S2R entities more effectively. However, these ap-

5 THREATS TO VALIDITY

proaches highly depended on the S2R writing in the bug report

| In our experiments evaluating our model, threats to internal va- | including formatting, word usage, and granularity [12, 15, 24, 49], |  |
| --- | --- | --- |
| lidity may arise from the randomness of LLMs generation, which | which constrains its deployment in the real world. In contrast, our |  |
| may generate different results for different runs. Namely, across | approach does not construct any sophisticated manually-crafted |  |
| different runs of the same prompt, the obtained metrics could vary. | patterns and pre-defined vocabulary of words. We leverage a single |  |
| To mitigate this threat, we ran the LLM-related approaches (i.e., | model LLMs with novel prompt engineering to elicit the natural lan- |  |
| AdbGPT | and ablation baselines) three times and the metrics were | guage understanding and logical reasoning to extract S2R entities |
| then from the aggregation of the three runs. Another potential | and reproduce the bugs. |  |
| confounding factor concerns the manual labeling of the ground- | Some works attempted to assist reporting process [19, 31–33, |  |
| truth for S2R entity extraction (RQ1). To mitigate any potential | 77, 78] and improve the bug report quality [34, 35, 58, 75]. For ex- |  |
| subjectivity or errors, we gave the annotators a training session | ample, Chaparro et al. [16] developed DeMIBuD to detect missing |  |
| and a passing test before labeling. We asked them to independently | information from bug reports. Fazzini et al. [26] proposed a mobile |  |
| annotate without any discussion and came to a consensus on the | application EBug, suggesting accurate reproduction steps while the |  |
| finalized ground-truth. | users are writing them. More recently, Yang et al. [66] proposed |  |
| The main external threat to the validity of our work is the repre- | an interactive chatbot system BURT to guide users to report essen- |  |
| sentative of the testing dataset selected to evaluate our approach. To | tial bug report elements. These approaches are complementary to |  |
| mitigate this threat, we collected bug reports from previous related | our approach, as they increase bug report quality at the time of |  |
| research, representing an unbiased testing dataset for our study. In | reporting which in turn, could potentially improve the capabilities |  |
| addition, we randomly collected five practical bug reports to further | of LLMs’ understanding. |  |

evaluate the usefulness of our tool with five graduate students and

three developers in real-world development environments. A po-

6.2 Large Language Models for Software

tential confounding factor concerns the representation of graduate

| students in the user study. To mitigate this threat, five graduate | Engineering |
| --- | --- |
| students have at least 1.5-year experience in Android app develop- | Following the success of LLMs in many natural language processing |
| ment and bug reproduction, so they are recognized as substitutes | tasks, researchers have started exploring their potential in software |
| for developers in software engineering research experiments [65]. | engineering. Several studies have focused on automated code com- |

pletion [23, 39, 41, 51, 79]. More recently, Codex [10] employed by

Github Copilot has shown promising results in generating code

from natural language comments, which has the potential to sig-

| 6 | RELATED WORK | nificantly reduce developers’ coding efforts, although some minor |
| --- | --- | --- |
| We review the related work in two main areas: 1) bug record and | issues still exist. This has sparked interest in using LLMs to resolve |  |
| replay, and 2) large language models for software engineering. | code issues through program patching [3, 36, 44, 48]. For instance, |  |

---

## Page 11

| Prompting Is All You Need: Automated Android Bug Replay with Large Language Models | ICSE 2024, April 14–20, 2024, Lisbon, Portugal |  |
| --- | --- | --- |
| AlphaRepair, introduced by Xia et al. [76], effectively encoded the | [16] Oscar Chaparro, Jing Lu, Fiorella Zampetti, Laura Moreno, Massimiliano Di Penta, |  |
| intricate relations between patches and the contexts of codes us- | Andrian Marcus, Gabriele Bavota, and Vincent Ng. 2017. | Detecting missing |

information in bug descriptions. In Proceedings of the 2017 11th Joint Meeting on

| ing LLMs. Additionally, some studies have examined the impact | Foundations of Software Engineering | . 396–407. |
| --- | --- | --- |
| of LLMs on software development [40, 57], developer productiv- | [17] Chunyang Chen, Sidong Feng, Zhengyang Liu, Zhenchang Xing, and Shengdong |  |
| ity [22, 70, 85], and security vulnerabilities [38, 61, 62]. LLMs remain | Zhao. 2020. From lost to found: Discover missing ui design semantics through |  |

recovering missing tags. Proceedings of the ACM on Human-Computer Interaction

| an ongoing research topic in the software engineering community. | 4, CSCW2 (2020), 1–22. |
| --- | --- |
| Our work opens up a new possibility for integrating LLMs and | [18] Chunyang Chen, Sidong Feng, Zhenchang Xing, Linda Liu, Shengdong Zhao, and |

Jinshui Wang. 2019. Gallery dc: Design search and knowledge discovery through

| GUI understanding, enabling LLMs to understand S2Rs and guide | auto-created gui component gallery. | Proceedings of the ACM on Human-Computer |
| --- | --- | --- |
| dynamic GUI screens to automated bug reproduction. | Interaction | 3, CSCW (2019), 1–22. |

[19] Jieshan Chen, Jiamou Sun, Sidong Feng, Zhenchang Xing, Qinghua Lu, Xiwei

Xu, and Chunyang Chen. 2023. Unveiling the Tricks: Automated Detection of

7 CONCLUSION Dark Patterns in Mobile Applications. In Proceedings of the 36th Annual ACM

Symposium on User Interface Software and Technology . 1–20.

Inspired by the success of Large Language Models (LLMs) in natural [20] Xiang Chen, Ningyu Zhang, Xin Xie, Shumin Deng, Yunzhi Yao, Chuanqi Tan, Fei

language understanding, this paper proposes AdbGPT , a lightweight Huang, Luo Si, and Huajun Chen. 2022. Knowprompt: Knowledge-aware prompt-

tuning with synergistic optimization for relation extraction. In Proceedings of the

| approach to automatically reproduce the bugs from the S2Rs based | ACM Web Conference 2022 | . 2778–2788. |
| --- | --- | --- |
| on prompt engineering. In detail, we first prompt the LLMs by | [21] Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav |  |
| giving entity specifications, a few representative exemplars, and de- | Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Se- |  |

bastian Gehrmann, et al. 2022. Palm: Scaling language modeling with pathways.

velopers’ step-by-step reasoning, to help LLMs elicit the knowledge arXiv preprint arXiv:2204.02311 (2022).

to extract the entities from the S2Rs in the bug report like a devel- [22] Arghavan Moradi Dakhel, Vahid Majdinasab, Amin Nikanjam, Foutse Khomh,

Michel C Desmarais, and Zhen Ming Jiang. 2023. Github copilot ai pair program-

| oper expert. Given each step entity, we prompt the LLMs by giving | mer: Asset or liability? | Journal of Systems and Software | (2023), 111734. |
| --- | --- | --- | --- |
| the current GUI screen and few-shot learning with chain-of-thought | [23] Yinlin Deng, Chunqiu Steven Xia, Haoran Peng, Chenyuan Yang, and Lingming |  |  |
| reasoning to dynamically guide the probable target components | Zhang. 2023. Fuzzing Deep-Learning Libraries via Large Language Models. In |  |  |

Proceedings of the 32nd ACM Joint European Software Engineering Conference and

| to reproduce the bugs. The experiments and user study demon- | Symposium on the Foundations of Software Engineering | . |
| --- | --- | --- |
| strate the effectiveness, efficiency, and usefulness of our approach | [24] Mona Erfani Joorabchi, Mehdi Mirzaaghaei, and Ali Mesbah. 2014. Works for me! |  |
| in accelerating bug reproduction. | characterizing non-reproducible bug reports. In | Proceedings of the 11th Working |

Conference on Mining Software Repositories . 62–71.

In the future, we will keep improving our AdbGPT for better ef- [25] Zhiyu Fan, Xiang Gao, Abhik Roychoudhury, and Shin Hwei Tan. 2022. Auto-

fectiveness. For example, a bug report usually contains a wealth of mated Repair of Programs from Large Language Models. ICSE.

[26] Mattia Fazzini, Kevin Patrick Moran, Carlos Bernal-Cardenas, Tyler Wendland,

| information, including stack trace, error logs, screenshots, screen | Alessandro Orso, and Denys Poshyvanyk. 2022. Enhancing Mobile App Bug |  |
| --- | --- | --- |
| recordings, etc. We could take this information into the considera- | Reporting via Real-time Understanding of Reproduction Steps. | IEEE Transactions |
| tion to enhance the understanding of LLMs to the bugs. | on Software Engineering | (2022). |

[27] Mattia Fazzini, Martin Prammer, Marcelo d’Amorim, and Alessandro Orso. 2018.

Automatically translating bug reports into test cases for mobile apps. In Proceed-

ings of the 27th ACM SIGSOFT International Symposium on Software Testing and

| REFERENCES | Analysis | . 141–152. |  |  |
| --- | --- | --- | --- | --- |
| [1] 2021. Bot Maker for Android - Apps on Google Play. https://play.google.com/ | [28] Sidong Feng and Chunyang Chen. 2022. GIFdroid: an automated light-weight tool |  |  |  |
| store/apps/details?id=com.frapeti.androidbotmaker. | for replaying visual bug reports. In | Proceedings of the ACM/IEEE 44th International |  |  |
| [2] 2021. Command line tools for recording, replaying and mirroring touchscreen | Conference on Software Engineering: Companion Proceedings | . 95–99. |  |  |
| events for Android. https://github.com/appetizerio/replaykit. | [29] Sidong Feng and Chunyang Chen. 2022. GIFdroid: automated replay of visual |  |  |  |
| [3] 2022. | arXiv preprint arXiv:2205.10583 | (2022). | bug reports for Android apps. In | Proceedings of the 44th International Conference |
| [4] 2023. | Android Debug Bridge (adb) - Android Developers. | https://developer. | on Software Engineering | . 1045–1057. |
| android.com/studio/command-line/adb. | [30] Sidong Feng, Chunyang Chen, and Zhenchang Xing. 2022. Gallery DC: Auto- |  |  |  |
| [5] 2023. | Android Uiautomator2 Python Wrapper. | https://github.com/openatx/ | created GUI component gallery for design search and knowledge discovery. In |  |
| uiautomator2. | Proceedings of the ACM/IEEE 44th International Conference on Software Engineering: |  |  |  |
| [6] 2023. Genymotion – Android Emulator for app testing. https://www.genymotion. | Companion Proceedings | . 80–84. |  |  |
| com/. | [31] Sidong Feng, Chunyang Chen, and Zhenchang Xing. 2023. Video2Action: Reduc- |  |  |  |
| [7] 2023. Introducing ChatGPT. https://chat.openai.com/. | ing human interactions in action annotation of app tutorial videos. In | Proceedings |  |  |
| [8] 2023. Number of apps available in leading app stores. https://www.statista.com/ | of the 36th Annual ACM Symposium on User Interface Software and Technology | . |  |  |
| statistics/276623/number-of-apps-available-in-leading-app-stores/. | 1–15. |  |  |  |
| [9] 2023. An open letter to GitHub from the maintainers of open source projects. | [32] Sidong Feng, Minmin Jiang, Tingting Zhou, Yankun Zhen, and Chunyang Chen. |  |  |  |
| https://github.com/dear-github/dear-github. | 2022. Auto-Icon+: An Automated End-to-End Code Generation Tool for Icon |  |  |  |
| [10] 2023. OpenAI Codex. https://openai.com/blog/openai-codex. | Designs in UI Development. | ACM Transactions on Interactive Intelligent Systems |  |  |
| [11] Jorge Aranda and Gina Venolia. 2009. The secret life of bugs: Going past the | 12, 4 (2022), 1–26. |  |  |  |
| errors and omissions in software repositories. In | 2009 IEEE 31st International | [33] Sidong Feng, Suyu Ma, Jinzhong Yu, Chunyang Chen, Tingting Zhou, and Yankun |  |  |
| Conference on Software Engineering | . IEEE, 298–308. | Zhen. 2021. Auto-icon: An automated code generation tool for icon designs |  |  |
| [12] Nicolas Bettenburg, Sascha Just, Adrian Schröter, Cathrin Weiss, Rahul Premraj, | assisting in ui development. In | 26th International Conference on Intelligent User |  |  |
| and Thomas Zimmermann. 2008. What makes a good bug report?. In | Proceedings | Interfaces | . 59–69. |  |
| of the 16th ACM SIGSOFT International Symposium on Foundations of software | [34] Sidong Feng, Mulong Xie, and Chunyang Chen. 2023. Efficiency Matters: Speeding |  |  |  |
| engineering | . 308–318. | Up Automated Testing with GUI Rendering Inference. In | Proceedings of the 45th |  |
| [13] Nicolas Bettenburg, Rahul Premraj, Thomas Zimmermann, and Sunghun Kim. | International Conference on Software Engineering | . |  |  |
| 2008. Extracting structural information from bug reports. In | Proceedings of the | [35] Sidong Feng, Mulong Xie, Yinxing Xue, and Chunyang Chen. 2023. Read It, Don’t |  |  |
| 2008 international working conference on Mining software repositories | . 27–30. | Watch It: Captioning Bug Recordings Automatically. In | Proceedings of the 45th |  |
| [14] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, | International Conference on Software Engineering | . |  |  |
| Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda | [36] Michael Fu, Chakkrit Tantithamthavorn, Trung Le, Van Nguyen, and Dinh Phung. |  |  |  |
| Askell, et al. 2020. Language models are few-shot learners. | Advances in neural | 2022. VulRepair: a T5-based automated software vulnerability repair. In | Pro- |  |
| information processing systems | 33 (2020), 1877–1901. | ceedings of the 30th ACM Joint European Software Engineering Conference and |  |  |
| [15] Yu Cao, Hongyu Zhang, and Sun Ding. 2014. Symcrash: Selective recording for | Symposium on the Foundations of Software Engineering | . 935–947. |  |  |

reproducing crashes. In Proceedings of the 29th ACM/IEEE international conference

on Automated software engineering . 791–802.

---

## Page 12

| ICSE 2024, April 14–20, 2024, Lisbon, Portugal | Feng et al. |  |  |  |
| --- | --- | --- | --- | --- |
| [37] Lorenzo Gomez, Iulian Neamtiu, Tanzirul Azim, and Todd Millstein. 2013. Reran: | [60] Yasumasa Onoe, Michael Zhang, Eunsol Choi, and Greg Durrett. 2022. Entity |  |  |  |
| Timing-and touch-sensitive record and replay for android. In | 2013 35th Interna- | Cloze By Date: What LMs Know About Unseen Entities. In | Findings of the Asso- |  |
| tional Conference on Software Engineering (ICSE) | . IEEE, 72–81. | ciation for Computational Linguistics: NAACL 2022 | . 693–702. |  |
| [38] Anastasiia Grishina. 2022. Enabling automatic repair of source code vulnerabili- | [61] Hammond Pearce, Baleegh Ahmad, Benjamin Tan, Brendan Dolan-Gavitt, and |  |  |  |
| ties using data-driven methods. In | Proceedings of the ACM/IEEE 44th International | Ramesh Karri. 2021. An empirical cybersecurity evaluation of github copilot’s |  |  |
| Conference on Software Engineering: Companion Proceedings | . 275–277. | code contributions. | ArXiv abs/2108.09293 | (2021). |
| [39] Qing Huang, Zhiqiang Yuan, Zhenchang Xing, Xiwei Xu, Liming Zhu, and | [62] Hammond Pearce, Benjamin Tan, Baleegh Ahmad, Ramesh Karri, and Bren- |  |  |  |
| Qinghua Lu. 2022. Prompt-tuned Code Language Model as a Neural Knowl- | dan Dolan-Gavitt. 2022. Examining Zero-Shot Vulnerability Repair with Large |  |  |  |
| edge Base for Type Inference in Statically-Typed Partial Code. In | 37th IEEE/ACM | Language Models. In | 2023 IEEE Symposium on Security and Privacy (SP) | . IEEE |
| International Conference on Automated Software Engineering | . 1–13. | Computer Society, 1–18. |  |  |
| [40] Saki Imai. 2022. Is GitHub copilot a substitute for human pair-programming? An | [63] Strategic Planning. 2002. The economic impacts of inadequate infrastructure for |  |  |  |
| empirical study. In | Proceedings of the ACM/IEEE 44th International Conference on | software testing. | National Institute of Standards and Technology | (2002). |
| Software Engineering: Companion Proceedings | . 319–321. | [64] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, |  |  |
| [41] Naman Jain, Skanda Vaidyanath, Arun Iyer, Nagarajan Natarajan, Suresh | Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. 2020. Exploring the limits of |  |  |  |
| Parthasarathy, Sriram Rajamani, and Rahul Sharma. 2022. Jigsaw: Large lan- | transfer learning with a unified text-to-text transformer. | The Journal of Machine |  |  |
| guage models meet program synthesis. In | Proceedings of the 44th International | Learning Research | 21, 1 (2020), 5485–5551. |  |
| Conference on Software Engineering | . 1219–1231. | [65] Iflaah Salman, Ayse Tosun Misirli, and Natalia Juristo. 2015. Are students represen- |  |  |
| [42] Jinseong Jeon and Jeffrey S Foster. 2012. | Troyd: Integration testing for android | . | tatives of professionals in software engineering experiments?. In | 2015 IEEE/ACM |
| Technical Report. | 37th IEEE International Conference on Software Engineering | , Vol. 1. IEEE, 666–676. |  |  |
| [43] Jiajun Jiang, Luyao Ren, Yingfei Xiong, and Lingming Zhang. 2019. Inferring | [66] Yang Song, Junayed Mahmud, Ying Zhou, Oscar Chaparro, Kevin Moran, Andrian |  |  |  |
| program transformations from singular examples via big code. In | 2019 34th | Marcus, and Denys Poshyvanyk. 2022. Toward interactive bug reporting for |  |  |
| IEEE/ACM International Conference on Automated Software Engineering (ASE) | . | (android app) end-users. In | Proceedings of the 30th ACM Joint European Software |  |
| IEEE, 255–266. | Engineering Conference and Symposium on the Foundations of Software Engineering | . |  |  |
| [44] Nan Jiang, Thibaud Lutellier, and Lin Tan. 2021. Cure: Code-aware neural machine | 344–356. |  |  |  |
| translation for automatic program repair. In | 2021 IEEE/ACM 43rd International | [67] Ting Su, Jue Wang, and Zhendong Su. 2021. Benchmarking automated gui testing |  |  |
| Conference on Software Engineering (ICSE) | . IEEE, 1161–1173. | for android against real-world bugs. In | Proceedings of the 29th ACM Joint Meeting |  |
| [45] Jack Johnson, Junayed Mahmud, Tyler Wendland, Kevin Moran, Julia Rubin, | on European Software Engineering Conference and Symposium on the Foundations |  |  |  |
| and Mattia Fazzini. 2022. An empirical investigation into the reproduction of | of Software Engineering | . 119–130. |  |  |
| bug reports for android apps. In | 2022 IEEE International Conference on Software | [68] Yulei Sui, Yifei Zhang, Wei Zheng, Manqing Zhang, and Jingling Xue. 2019. Event |  |  |
| Analysis, Evolution and Reengineering (SANER) | . IEEE, 321–322. | trace reduction for effective bug replay of Android apps via differential GUI |  |  |
| [46] Andrew J Ko and Brad A Myers. 2006. Barista: An implementation framework | state analysis. In | Proceedings of the 2019 27th ACM Joint Meeting on European |  |  |
| for enabling new tools, interaction techniques and views in code editors. In | Software Engineering Conference and Symposium on the Foundations of Software |  |  |  |
| Proceedings of the SIGCHI conference on Human Factors in computing systems | . | Engineering | . 1095–1099. |  |
| 387–396. | [69] Viriya Taecharungroj. 2023. “What Can ChatGPT Do?” Analyzing Early Reactions |  |  |  |
| [47] Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke | to the Innovative AI Chatbot on Twitter. | Big Data and Cognitive Computing | 7, 1 |  |
| Iwasawa. 2022. Large Language Models are Zero-Shot Reasoners. In | Advances in | (2023), 35. |  |  |
| Neural Information Processing Systems | . | [70] Priyan Vaithilingam, Tianyi Zhang, and Elena L Glassman. 2022. Expectation |  |  |
| [48] Sophia D Kolak, Ruben Martins, Claire Le Goues, and Vincent Josua Hellendoorn. | vs. experience: Evaluating the usability of code generation tools powered by |  |  |  |
| 2022. Patch Generation with Language Models: Feasibility and Scaling Behavior. | large language models. In | Chi conference on human factors in computing systems |  |  |
| In | Deep Learning for Code Workshop | . | extended abstracts | . 1–7. |
| [49] A Gunes Koru and Jeff Tian. 2004. Defect handling in medium and large open | [71] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, |  |  |  |
| source projects. | IEEE software | 21, 4 (2004), 54–61. | Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017. | Attention is all |
| [50] Yann LeCun, Yoshua Bengio, and Geoffrey Hinton. 2015. Deep learning. | nature | you need. | Advances in neural information processing systems | 30 (2017). |
| 521, 7553 (2015), 436–444. | [72] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, and Denny Zhou. |  |  |  |
| [51] Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi | 2022. | Rationale-augmented ensembles in language models. | arXiv preprint |  |
| Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, et al. 2022. | arXiv:2207.00747 | (2022). |  |  |
| Competition-level code generation with alphacode. | Science | 378, 6624 (2022), | [73] Yaqing Wang, Quanming Yao, James T Kwok, and Lionel M Ni. 2020. Generalizing |  |
| 1092–1097. | from a few examples: A survey on few-shot learning. | ACM computing surveys |  |  |
| [52] Yafu Li, Yongjing Yin, Jing Li, and Yue Zhang. 2022. | Prompt-Driven Neural | (csur) | 53, 3 (2020), 1–34. |  |
| Machine Translation. In | Findings of the Association for Computational Linguistics: | [74] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed H Chi, |  |  |
| ACL 2022 | . 2579–2590. | Quoc V Le, and Denny Zhou. 2022. Chain-of-Thought Prompting Elicits Rea- |  |  |
| [53] Jinzhi Liao, Xiang Zhao, Jianming Zheng, Xinyi Li, Fei Cai, and Jiuyang Tang. 2022. | soning in Large Language Models. In | Advances in Neural Information Processing |  |  |
| PTAU: Prompt Tuning for Attributing Unanswerable Questions. In | Proceedings | Systems | . |  |
| of the 45th International ACM SIGIR Conference on Research and Development in | [75] Chu-Pan Wong, Yingfei Xiong, Hongyu Zhang, Dan Hao, Lu Zhang, and Hong |  |  |  |
| Information Retrieval | . 1219–1229. | Mei. 2014. Boosting bug-report-oriented fault localization with segmentation and |  |  |
| [54] Wang Ling, Dani Yogatama, Chris Dyer, and Phil Blunsom. 2017. | Program | stack-trace analysis. In | 2014 IEEE international conference on software maintenance |  |
| Induction by Rationale Generation: Learning to Solve and Explain Algebraic | and evolution | . IEEE, 181–190. |  |  |
| Word Problems. In | Proceedings of the 55th Annual Meeting of the Association for | [76] Chunqiu Steven Xia and Lingming Zhang. 2022. Less training, more repairing |  |  |
| Computational Linguistics (Volume 1: Long Papers) | . 158–167. | please: revisiting automated program repair via zero-shot learning. In | Proceedings |  |
| [55] Hui Liu, Mingzhu Shen, Jiahao Jin, and Yanjie Jiang. 2020. Automated classifi- | of the 30th ACM Joint European Software Engineering Conference and Symposium |  |  |  |
| cation of actions in bug reports of mobile apps. In | Proceedings of the 29th ACM | on the Foundations of Software Engineering | . 959–971. |  |
| SIGSOFT International Symposium on Software Testing and Analysis | . 128–140. | [77] Mulong Xie, Sidong Feng, Zhenchang Xing, Jieshan Chen, and Chunyang Chen. |  |  |
| [56] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer | 2020. UIED: a hybrid tool for GUI element detection. In | Proceedings of the 28th |  |  |
| Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. Roberta: A | ACM Joint Meeting on European Software Engineering Conference and Symposium |  |  |  |
| robustly optimized bert pretraining approach. | arXiv preprint arXiv:1907.11692 | on the Foundations of Software Engineering | . 1655–1659. |  |
| (2019). | [78] Mulong Xie, Zhenchang Xing, Sidong Feng, Xiwei Xu, Liming Zhu, and Chunyang |  |  |  |
| [57] Zhe Liu, Chunyang Chen, Junjie Wang, Xing Che, Yuekai Huang, Jun Hu, and | Chen. 2022. | Psychologically-inspired, unsupervised inference of perceptual |  |  |
| Qing Wang. 2023. Fill in the Blank: Context-aware Automated Text Input Gener- | groups of GUI widgets from GUI images. In | Proceedings of the 30th ACM Joint |  |  |
| ation for Mobile GUI Testing. (2023). | European Software Engineering Conference and Symposium on the Foundations of |  |  |  |
| [58] Kevin Moran, Mario Linares-Vásquez, Carlos Bernal-Cárdenas, and Denys Poshy- | Software Engineering | . 332–343. |  |  |
| vanyk. 2015. Auto-completing bug reports for android applications. In | Proceedings | [79] Frank F Xu, Uri Alon, Graham Neubig, and Vincent Josua Hellendoorn. 2022. A |  |  |
| of the 2015 10th Joint Meeting on Foundations of Software Engineering | . 673–686. | systematic evaluation of large language models of code. In | Proceedings of the 6th |  |
| [59] Dmitry Nurmuradov and Renee Bryce. 2017. Caret-HM: recording and replaying | ACM SIGPLAN International Symposium on Machine Programming | . 1–10. |  |  |
| Android user sessions with heat map generation using UI state clustering. In | [80] Yu Zhao, Ting Su, Yang Liu, Wei Zheng, Xiaoxue Wu, Ramakanth Kavuluru, |  |  |  |
| Proceedings of the 26th ACM SIGSOFT International Symposium on Software Testing | William GJ Halfond, and Tingting Yu. 2022. ReCDroid+: Automated End-to-End |  |  |  |
| and Analysis | . 400–403. | Crash Reproduction from Bug Reports for Android Apps. | ACM Transactions on |  |

Software Engineering and Methodology (TOSEM) 31, 3 (2022), 1–33.

---

## Page 13

| Prompting Is All You Need: Automated Android Bug Replay with Large Language Models | ICSE 2024, April 14–20, 2024, Lisbon, Portugal |  |  |
| --- | --- | --- | --- |
| [81] Yu Zhao, Tingting Yu, Ting Su, Yang Liu, Wei Zheng, Jingzhi Zhang, and | In | 2012 34th International conference on software engineering (ICSE) | . IEEE, 14–24. |
| William GJ Halfond. 2019. Recdroid: automatically reproducing android applica- | [84] Kaiyang Zhou, Jingkang Yang, Chen Change Loy, and Ziwei Liu. 2022. Learning |  |  |
| tion crashes from bug reports. In | 2019 IEEE/ACM 41st International Conference on | to prompt for vision-language models. | International Journal of Computer Vision |
| Software Engineering (ICSE) | . IEEE, 128–139. | 130, 9 (2022), 2337–2348. |  |
| [82] Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, | [85] Albert Ziegler, Eirini Kalliamvakou, X Alice Li, Andrew Rice, Devon Rifkin, |  |  |
| Dale Schuurmans, Olivier Bousquet, Quoc Le, and Ed Chi. 2023. Least-to-most | Shawn Simister, Ganesh Sittampalam, and Edward Aftandilian. 2022. Productivity |  |  |
| prompting enables complex reasoning in large language models. In | 2023 11th | assessment of neural code completion. In | Proceedings of the 6th ACM SIGPLAN |
| International Conference on Learning Representations (ICLR) | . | International Symposium on Machine Programming | . 21–29. |

[83] Jian Zhou, Hongyu Zhang, and David Lo. 2012. Where should the bugs be fixed?

more accurate information retrieval-based bug localization based on bug reports.

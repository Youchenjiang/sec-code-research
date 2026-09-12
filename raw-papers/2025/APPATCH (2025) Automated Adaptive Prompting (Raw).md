---
title: "E_M_APPATCH_2025"
creator: "LaTeX with hyperref"
pages: 21
---

# E_M_APPATCH_2025

> **總頁數**：21 頁

---

## Page 1

App A tch : Automated Adaptive Prompting

Large Language Models for Real-World

Software Vulnerability Patching

Yu Nong, University at Buffalo; Haoran Yang, Washington State University;

Long Cheng, Clemson University; Hongxin Hu and Haipeng Cai, University at Buffalo

https://www.usenix.org/conference/usenixsecurity25/presentation/nong

This paper is included in the Proceedings of the

34th USENIX Security Symposium.

August 13–15, 2025 • Seattle, WA, USA

978-1-939133-52-6

Open access to the Proceedings of the

34th USENIX Security Symposium is sponsored by USENIX.

---

## Page 2

A PPATCH : Automated Adaptive Prompting Large Language Models for

Real-World Software Vulnerability Patching

1 2 3 1 1 ∗

Yu Nong , Haoran Yang , Long Cheng , Hongxin Hu , and Haipeng Cai

1 2 3

University at Buffalo , Washington State University , Clemson University

1 { yunong,hongxinh,haipengc } @buffalo.edu , 2 haoran.yang2@wsu.edu , 3 lcheng2@clemson.edu

Abstract techniques, state-of-the-art (SOTA) code-analysis-based ap-

Timely and effective vulnerability patching is essential for

cybersecurity defense, for which various approaches have

been proposed yet still struggle to generate valid and cor-

rect patches for real-world vulnerabilities. In this paper, we

leverage the power and merits of pre-trained language lan-

guage models (LLMs) to enable automated vulnerability

patching using no test input/exploit evidence and without

model training/fine-tuning. To elicit LLMs to effectively rea-

son about vulnerable code behaviors, which is essential for

quality patch generation, we introduce vulnerability seman-

tics reasoning and adaptive prompting on LLMs and instanti-

ate the methodology as A PPATCH , an automated LLM-based

Software vulnerabilities pose a constant and significant threat

to the security of modern cyberspace [15, 16] and they are

widespread [19, 27, 30–32]. With the rapid growth in the vol-

ume and sophistication of cyberattacks, which are enabled by

these vulnerabilities, timely and effective vulnerability patch-

ing has become increasingly critical [43, 52, 56]. However,

manual approaches to patching are costly [26] and struggle

to keep pace with the emergence of new vulnerabilities [25].

Thus, automated solutions are needed to help developers patch

vulnerabilities before they are exploited [18, 55].

In this context, various approaches to automated patch-

ing have been proposed [14, 18, 20, 34, 43, 54], which gener-

ally fall in two major categories: those based on code anal-

ysis and those based on deep learning (DL). Among other

proaches achieve property-based repair based on access range

analysis hence enforcing given safety properties [24] or use

sanitizers to extract vulnerability-representing constraints for

symbolic-execution-based repair [20]. More recently, induc-

tive property inference along with simple templates [55] is

employed to generate vulnerability patches. However, these

techniques rely on exploits or vulnerability-triggering test

inputs, which may not always be available, especially for

emerging (e.g., zero-day) vulnerabilities. They often also re-

quire that the code to patch be compilable, which further

limits their applicability (e.g., they can not be used before the

project becomes complete).

able [9, 39, 41]. As a result, they do not generalize well to

unseen code and often stumble on real-world vulnerabili-

studies show that the augmented models still suffer low accu-

racy [37, 38].

Most recently, large language models (LLMs) have

emerged as powerful tools to assist developers with coding

related tasks. LLMs overcome the lack of generalizability of

ordinary DL-based approaches and have shown promising

potential for vulnerability patching [37, 43]. However, the

SOTA LLM-based (with zero-shot) technique [43] does not

work well on real-world vulnerabilities and often generates

no patches or invalid ones [37]. The recent study [37] shows

that LLM can be significantly improved by carefully designed

prompting strategies, especially based on chain-of-thought

(CoT) [51] reasoning. Prompting is indeed attractive in that

it does not require (pre-)training or even fine-tuning, which

would not only require sizable labeled datasets but also be

| patching system. Our evaluation of A | PPATCH | on 97 zero-day | DL-based approaches overcome these limitations and have |
| --- | --- | --- | --- |
| vulnerabilities and 20 existing vulnerabilities demonstrates its | gained more momentum in recent years [14, 18, 52]. These |  |  |
| superior performance to both existing prompting methods and | techniques leverage existing vulnerability datasets to train |  |  |
| state-of-the-art non-LLM-based techniques (by up to 28.33% | a DL model that learns known vulnerability-fixing patterns, |  |  |
| in F1 and 182.26% in recall over the best baseline). Through | hence the ability to repair a given vulnerability. Despite their |  |  |
| A | PPATCH | , we demonstrate what helps for LLM-based patch- | promises, they need sizable and quality training data with |
| ing and how, as well as discussing what still lacks and why. | vulnerability labels, which is not widely and diversely avail- |  |  |
| 1 | Introduction | ties [52]. While data augmentation helps [12, 38, 40], recent |  |
| ∗ | Haipeng Cai is the corresponding author. | infeasible to ordinary users, especially on foundation-scale |  |
| USENIX Association | 34th USENIX Security Symposium | 4481 |  |

---

## Page 3

LLMs that may actually hold the promise for effective vulner-

ability analysis.

Despite a promising direction, vulnerability patching via

lately [37, 42, 52]. First, for automated patching, the prompt-

how to automatically write a prompt to an LLM for vulner-

ability patching ( Challenge 1 ). Second, prompting tends to

include exemplars to be effective, especially if it aims to elicit

reasoning on LLMs [51] as CoT does, which is essential

for vulnerability patching—a task relying on code seman-

how to prepare the best exemplars is unknown ( Challenge

2 ). Third, LLMs are known to suffer from capacity (#tokens)

and context constraints, which makes it difficult to provide

necessary code context in a prompt and analyze sizable code;

yet vulnerabilities are context-sensitive and can be interproce-

dural, thus patching them often requires accommodating po-

tentially larger code contexts ( Challenge 3 ). Moreover, LLMs

are commonly subject to hallucination and non-deterministic

worse than not patching ( Challenge 4 ).

In this paper, we present A PPATCH , a novel, automated

bility patching. Given a vulnerable program with a known

analyze a smaller code snippet that includes all the essential

its the LLM to identify the vulnerability’s root cause within

henceforth selecting exemplars that best fit the program on

the fly from a pre-mined exemplar database, an essential step

referred to as dynamic adaptive prompting , which addresses

Challenges 2 . The database is built offline by mining exem-

plars from known patches. With the adaptively chosen ex-

emplars, A PPATCH forms the patching prompt automatically

to generate multiple candidate patches with LLMs, address-

ing Challenge 1 . To mitigate model hallucinations, A PPATCH

consults an ensemble of LLMs to cross-validate the candidate

patches concerning multiple facets of patch quality—validity

(not changing functionality) and correct (fixing the vulnera-

bility), hence addressing Challenge 4 .

. int main (int argc, char **argv){

. …… ……

.

. // Other Callers

……

1 static void SplitChar(const char *str, int *argcPtr,

| 3 | char *cp, *ep, *p, **argv; |  |
| --- | --- | --- |
| 4 | int cnt = 1, len, i; |  |
| 5 | len = Jsi_Strlen(str); |  |
| 7 | while (*cp) { | Control Dependency |
| 8 | if (ch) |  |
| 9 | cp = Jsi_Strchr(cp,ch); |  |
| 10 | else |  |
| 11 | while (*cp && !isspace(*cp)) |  |
| 12 | cp++; |  |
| 13 | if (cp == NULL \|\| *cp == 0) |  |
| 14 | break; |  |
| 15 | cp++; |  |
| 16 | cnt++; |  |
| 17 | } |  |
| 19 | argv = (char**)Jsi_DSValue(dStr); |  |
| 20 | *argvPtr = argv; |  |
| 21 | *argcPtr = cnt; |  |
| 22 | p = (char*)&(argv[cnt+2]); |  |
| 23 | argv[cnt+1] = p; |  |
| 24 | Jsi_Strcpy(p, str); |  |
| 25 | cp = p; |  |

……

45 }

46 char* Jsi_Strcpy(char *str1, const char *str2){

| 47 | int len = strlen(str2); |
| --- | --- |
| 48 | char* cp = strncpy(str1, str2, len-1); |
| 49 | str1[len-1] = 0; |
| 50 | return cp; |

51 }

Q: Given the following code: <code in Figure 1> which has a CWE-787

vulnerability.

ś The CWE-787  vulnerability in the provided code is related to

`str` into `p` without ensuring that the destination buffer is

conditions. Here is the patch to mitigate this vulnerability:

### Patch: Use `Jsi_Strncpy` Instead of `Jsi_Strcpy`

no more characters are copied than the size of the destination

```c

```

Figure 2: GPT-4’s patch for the program sample in Figure 1

with standard prompting .

28.41% and 68.54% F1, respectively. A PPATCH also outper-

forms SOTA traditional vulnerability patching approaches,

where they only achieve up to 17.53% and 85.00% recall

on the two datasets while A PPATCH achieves 49.48% and

90.00% recall, respectively. A PPATCH is also reasonably effi-

cient, taking on average 37.148-50.209 seconds to generate a

patch, and using 5,684-6,802 tokens per patch with the LLMs.

| prompting LLMs faces several critical challenges as revealed | 2 | char ***argvPtr, char ch, Jsi_DString *dStr){ |  |  |
| --- | --- | --- | --- | --- |
| ing would need to be automated too. Yet it is not known | 6 | cp = (char*)str; | Data Dependency |  |
| tics reasoning. Yet again, for an arbitrary program to patch, | 18 | Jsi_DSSetLength(dStr,(sizeof(char*)*(cnt+3)+sizeof(char)*(len+6))); |  |  |
| responses, whereas stably generating valid and correct patches | Figure 1: An example vulnerable program sample where the |  |  |  |
| is essential for vulnerability patching—bad patching can be | vulnerable statement is at line 48. |  |  |  |
| Adaptive prompting methodology for LLM-based vulnera- | vulnerability at line | ɫɯ | , please generate the patch for the |  |
| vulnerability location, A | PPATCH | first narrows down the scope | an out-of-bounds write, which can occur when copying the string |  |
| of analysis to only the relevant subset of the program via a | large enough to hold the source string | ɩɫ | . This can lead to |  |
| step called | semantics-aware scoping | . This allows LLMs to |  | overflow, memory corruption, and potentially exploitable |
| information necessary for reasoning about the vulnerability- | Replace the `Jsi_Strcpy` function with `Jsi_Strncpy` to ensure that |  |  |  |
| related code behaviors, addressing | Challenge 3 | . Then, it elic- | buffer allows. This requires knowing the maximum buffer size. |  |
| the reduced scope with vulnerability semantics reasoning, | 2 | ɫ | Jsi_Strncpy(p, str, len+1); |  |
| We have implemented A | PPATCH | as an open-source tool | Our results suggest the practical feasibility and merits of |  |
| based on four latest and most powerful LLMs: GPT-4, Gemini- | LLM-based vulnerability patching, via a novel methodology |  |  |  |
| 1.5, Claude-3.5, and Llama-3.1, and evaluated it against a | (pivoted by | automated adaptive prompting based on vulnera- |  |  |
| dataset with 97 zero-day (across 18 unique projects) sam- | bility semantics reasoning | ) of leveraging LLMs to generate |  |  |
| ples and a dataset with 20 existing real-world vulnerability | valid and correct patches. Through A | PPATCH | , we demon- |  |
| samples. With A | PPATCH | , the evaluated LLMs achieve up to | strated how LLMs can be helped for this challenging task; |  |
| 36.46% and 73.86% F1 on the two datasets while the same | also, by examining failure cases, we discuss how/where and |  |  |  |
| LLMs with baseline prompting strategies only achieve up to | why LLMs may still fall short even with A | PPATCH | . |  |
| 4482 | 34th USENIX Security Symposium | USENIX Association |  |  |

---

## Page 4

Q: Complete the following code after the comment:

/*Fixed CWE-787 vulnerability*/

ś Here is the code completions ś

cp = p;

if (ch)

……

Figure 3: GPT-4’s patch for the sample in Figure 1 with a

state-of-the-art LLM-based approach zero-shot completion .

such as vulnerability detection [36], patching [43, 47], and

secure code generation [21]. Among existing approaches to

vulnerability patching, a popular method is to use a standard

prompting strategy, which directly asks the LLMs to patch the

vulnerable code [47]. However, this method does not provide

necessary guidance to LLMs, leaving all the vulnerability

analysis reasoning process to the models. Another, SOTA

To show the limitations of existing LLM-based vulnerabil-

ity patching approaches, we test the two methods mentioned

above on the example in Figure 1. As shown, the example

as the string str2 may be longer than the boundary of (the

memory region pointed to by) str1 . Figure 2 shows GPT-4’s

output patch with standard prompting, where we directly ask

Based on the two examples above, it is clear that, to patch

may still need to be guided step by step for necessary reason-

semantics-aware scoping, which only provides LLMs

with code entities that capture the core vulnerable behav-

ior of the program (noted as vulnerability semantics ).

2. To guide LLMs to analyze and patch vulnerabilities cor-

soning capabilities via CoT prompting [51] that demon-

3. Considering the diversity of vulnerability root causes

and patching strategies, a large-scale exemplar pool is

needed. However, manually writing the reasoning steps

for the exemplars is time-consuming. Thus, we design

an automated exemplar mining module which generates

exemplars based on existing real-world samples.

3 Technical Design

3.1 Overview

| <first 23 lines of code from Figure 1> | real-world vulnerabilities effectively, even powerful LLMs |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ```c | ing about code semantics. Therefore, we introduce A | PPATCH | , |  |  |  |  |
| strncpy(p, str, len+1); | an automated framework that adaptively prompts LLMs for |  |  |  |  |  |  |
| for (i = 0; i < cnt; i++) { | vulnerability patching with semantics reasoning guidance. We |  |  |  |  |  |  |
| argv[i] = cp; | introduce four key design elements in A | PPATCH | : |  |  |  |  |
| ep = Jsi_Strchr(cp, ch); | 1. To help LLMs concentrate on the most essential parts |  |  |  |  |  |  |
| ``` | of a program for vulnerability patching, we introduce |  |  |  |  |  |  |
| 2 | Background and Motivation | rectly, we arm them with vulnerability semantics rea- |  |  |  |  |  |
| LLMs have been explored for vulnerability analysis tasks | strates correct reasoning steps with a few exemplars. |  |  |  |  |  |  |
| method is zero-shot code completion [43], which removes the | 4. To provide the best-fit exemplars for a given testing sam- |  |  |  |  |  |  |
| vulnerable code and lets LLMs complete the vulnerable parts. | ple (i.e., code to patch), we design dynamic adaptive |  |  |  |  |  |  |
| However, this approach treats vulnerability patching as a sim- | prompting which automatically picks exemplars based |  |  |  |  |  |  |
| ple code completion task, without code analysis/reasoning. | on the vulnerability root causes of the testing sample. |  |  |  |  |  |  |
| has a CWE-787 vulnerability at line 48. The vulnerability is | Now we present our technical approach, starting with a design |  |  |  |  |  |  |
| caused by the possible out-of-bound write to the pointer | str1 | overview followed by details on each component. |  |  |  |  |  |
| the model to patch the vulnerability with the vulnerable line | The overall design of A | PPATCH | is depicted in Figure 4. We tar- |  |  |  |  |
| and CWE ID provided. As seen, GPT-4 seems to recognize | get a realistic vulnerability patching scenario with A | PPATCH | , |  |  |  |  |
| that the vulnerability is caused by the insufficient size of the | in which (1) the vulnerability manifestation locations (i.e., |  |  |  |  |  |  |
| memory | p | points to at line 24 and it should ensure that the | vulnerable statements | ) and (2) the vulnerability types (i.e., |  |  |  |
| write is not longer than | p | ’s boundary. While the basic idea | CWE IDs | ) of a given program to patch are available. Prior to |  |  |  |
| is correct, it is also needed to find out how much memory | p | the patching time, A | PPATCH | demonstrates to LLMs correct |  |  |  |
| should point to for patching the vulnerability. In this case, | reasoning towards patch generation with (3) existing vulnera- |  |  |  |  |  |  |
| necessary data/control dependency analysis is needed. How- | ble samples for which the ground-truth patches are known in |  |  |  |  |  |  |
| ever, GPT-4 generates the patch by changing | Jsi_Strcpy | to | addition. These three constitute the | inputs | to A | PPATCH | . |
| Jsi_Strncpy | and adding a write limit | len+1 | without analyz- | With these inputs, A | PPATCH | operates in two phases. In |  |
| ing the code semantics. Thus, it fails to patch the vulnerability. | Phase 1: Exemplar Mining | , through | semantics-aware scop- |  |  |  |  |
| Figure 3 shows GPT-4’s output patch with the zero-shot | ing | ( | 1.1 | ), it union-slices [8] each given vulnerable sample to |  |  |  |
| code completion method. As shown, we provide the code | capture its | vulnerability semantics | (essential behavior of the |  |  |  |  |
| up to line 23 (where the ground-truth patch is located) and | vulnerability, as formally defined in §3.2). Then, A | PPATCH |  |  |  |  |  |
| prompt the model (via a comment) to complete the remaining | proceeds with | exemplar generation | ( | 1.2 | ), producing a pool of |  |  |
| code while addressing the CWE-787 vulnerability. Similar to | exemplars each including the root cause analysis, fixing strat- |  |  |  |  |  |  |
| standard prompting, it simply completes line 24 with | strncpy | egy, and ground-truth patch. The root cause and fixing strategy |  |  |  |  |  |
| and sets a write limit | len+1 | without analyzing the actual size | are also generated by the LLMs automatically, according to |  |  |  |  |
| of | p | . Thus, it also fails to patch the vulnerability. | the vulnerability semantics | along with the ground-truth patch | . |  |  |
| USENIX Association | 34th USENIX Security Symposium | 4483 |  |  |  |  |  |

---

## Page 5

| Existing Vulnerability Samples | Phase 1: Exemplar Mining | APPATCH Outputs |
| --- | --- | --- |
| Ground-Truth Patches | Exemplar Generation | Exemplars |

Vulnerable Statements

1.1 Vulnerability

Program to Patch Dependency Vulnerability Semantics

Semantics

| Vulnerable Code | Analysis | Computation | Reasoning |
| --- | --- | --- | --- |
| Semantics-aware scoping | Analysis | ) |  |
| APPATCH Inputs | Phase 2: LLM-Guided Causal Patching |  |  |
| Exemplar Mining Workflow | Patching Workflow |  |  |

We introduce this core concept underlying A PPATCH with

following insights. First, although a vulnerable program may

portion of those lines actually causes the vulnerability. By

control/data flow is what is difficult for LLMs to understand

Root cause analysis Patches

1.2

Fixing Strategy Root cause analysis

Generated Patches

Root Cause Generation Exemplar Selection Patch Generation

Dynamic Adaptive Prompting 2.3 LLMs

2.2

Exemplar Mining Process Patching Process

EI . That is,

[ [

e i ∈ EI s v ∈ S v

where:

• Slice ( P , s

ward slice from s

v to e i .

vulnerability locations S v .

Vulnerable Code LLM Ground-Truth Patches Fixing Strategy

Vulnerable Statements 2.1 ( Root Cause LLM LLM LLM Multi-Faceted Patch Validation

Figure 4: An overview of A PPATCH ’s design, including its inputs, two main working phases, and outputs.

| Next, in | Phase 2: LLM-Guided Causal Patching | , the | nerabilities unless they can be exploited via external inputs. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| given program to patch is also scoped into vulnerability se- | Thus, to effectively capture vulnerability semantics, it is im- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| mantics ( | 2.1 | ). Then, through | dynamic adaptive prompting | portant to consider how these statements are influenced by |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ( | 2.2 | ), A | PPATCH | analyzes the root cause of the given vulner- | the program’s external inputs through control and data flow |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ability with an LLM and selects similar exemplars based on | dependencies. Therefore, we also include the contextual state- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the root cause. With the chosen exemplars, candidate patches | ments that influence the vulnerability statements as part of |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| are generated via CoT prompting on the LLM. Finally, the | vulnerability semantics, based on the data and control flow. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| generated patches are validated and refined through multiple | Given a program | P | , which consists of a set | S | of statements, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LLMs through a | multi-faceted patch validation | ( | 2.3 | ) process. | the set of | vulnerability locations | S | v | ⊆ | S | are statements where |  |  |  |  |  |  |  |  |  |
| As a result, the validated patches are returned as the | out- | the vulnerability manifests. The set of | external inputs | EI | ⊆ | S |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| puts | of A | PPATCH | . Note that while both phases rely on LLMs | consists of statements where external input data is received or |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| for automated root cause and fixing strategy identification | retrieved by | P | . This includes program input variables, returns |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| using the vulnerability semantics reasoning, Phase 1 addi- | from external function calls that read data, and global states |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tionally feeds the ground-truth patches to the models, This | modified by other functions (such as memory allocations, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| addition is essential because it is expected to help LLMs gen- | file input, network input, etc.). The | vulnerability semantics |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| erate root cause and fixing strategy that are more likely correct | V | ( | P | , | S | v | , | EI | ) | is defined as the union of all | static backward |  |  |  |  |  |  |  |  |  |
| than otherwise hence serving the demonstrating (exemplar) | slices | of the program | P | starting from any of the vulnerability |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| purposes to elicit LLMs’ similar reasoning at patching time. | locations | S | v | and terminating at any of the external inputs in |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3.2 | Vulnerability Semantics | V | ( | P | , | S | v | , | EI | ) = | Slice | ( | P | , | s | v | , | e | i | ) |
| contain many lines of code, oftentimes only a relatively small | v | , | e | i | ) | is the set of all statements in the static back- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| focusing on this portion, which scopes the semantics of the | • A | static backward slice | from | s | v | to | e | i | is the subset of state- |  |  |  |  |  |  |  |  |  |  |  |
| code that makes it vulnerable (intuitively noted as | vulnerabil- | ments in | P | that affect the execution at | s | v | , tracing backward |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ity semantics | for now) we can enable LLMs to perform more | along control and data dependencies to reach | e | i | . |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| effective vulnerability analysis. Second, mainstream LLMs | Note that the vulnerability locations and external inputs may |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| often struggle with processing and generating long texts. By | be in different functions. Therefore, we perform | interproce- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| narrowing the scope to vulnerability semantics, we can also | dural | backward slicing to capture the vulnerability semantics |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| reduce the length of the exemplars, prompts, and responses, | comprehensively. In this way, | V | ( | P | , | S | v | , | EI | ) | represents the set |  |  |  |  |  |  |  |  |  |
| thereby minimizing potential distractions for the LLMs and | of all statements in | P | that are relevant to the flow of data |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| improving their performance. Third, vulnerability-relevant | and control from any of the external inputs | EI | to any of the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| without guidance on reasoning about the flow [44]—thus, | As an example, Figure 1 illustrates a partial representation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| vulnerability semantics-based reasoning is necessary to guide | of vulnerability semantics. We start from a vulnerable state- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LLMs to conduct effective vulnerability patching. | ment ( | s | v | ) at line 48 and conduct union slicing to the program |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Therefore, we define vulnerability semantics as the aspects | input based on data and control dependencies (marked with |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| of a program’s code that contribute to its vulnerabilities. These | red and orange arrows). As a result, the statements marked |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| of course include statements where the vulnerabilities are | as yellow are the contexts of the vulnerable statement. The |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| triggered. However, such statements alone do not cause vul- | vulnerable statement (marked in red), the external input (in |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4484 | 34th USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 6

| Algorithm 1: | Semantics-Aware Scoping | patches with appropriate intermediate reasoning, we divide |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: | P | : input program, | S | v | : vulnerable statements | the overall reasoning process into three high-level steps: (1) |  |  |  |  |  |  |
| Output: | V | ( | P | , | S | v | , | EI | ) | : vulnerability semantics (code representation) | vulnerability semantics reasoning (as root cause analysis) | , (2) |

1 Function SemanticsAwareScoping( P , S v , EI )

4 V ← InitializeSlice() ; // Initialize an empty set

7 BS ei ← ComputeBackwardSlice( sdg , s v , e i ) ; // Backward slice

i

purple), and its contextual statements constitute (the code

representation of) the vulnerability semantics for the sample.

vulnerability semantics (line 9).

3.3.2 Exemplar Generation (Step 1.2)

With the vulnerability semantics computed in Step 1.1, Step

nerability among < CWE-IDs > and lines S v , the patch is

< ground-truth patch > . Starting with the external inputs:

<EI identified>, reason about the vulnerable behavior step

by step until the vulnerability is determined.

Since the code slice V is interprocedural across the whole

program, it is likely to contain a large number of code state-

Algorithm 1 that reach any of the patch locations. Then, the

3.4 LLM-Guided Causal Patching (Phase 2)

3.4.1 Semantics-Aware Scoping (Step 2.1)

| 2 | sdg | ← | ExtractSDG( | P | ) | ; | // Construct SDG for the program | P | fixing strategy identification, and (3) patch generation. How- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | EI | ← | IdentifyExternalInputs( | P | ) | ; | // Identify external inputs | ever, it is difficult to write the reasoning for each collected |  |
| 5 | foreach | e | i | in EI | do | sample manually. Therefore, we leverage LLMs to automati- |  |  |  |
| 6 | foreach | s | v | in S | v | do | cally generate the exemplars. Since we have the ground-truth |  |  |
| starting from a vulnerable location | sv | until reaching an external input | e | patches in the given existing samples, we prompt the LLMs |  |  |  |  |  |
| 8 | V | ← | V | ∪ | BS | ei | ; | // Unionize the above backward slice | to generate (1) with the following template: |
| 9 | return | V | ; | Q | : Given the following code slice | V | exem | , which has a vul- |  |
| 3.3 | Exemplar Mining (Phase 1) | ments [10], making it difficult for LLMs to process. Therefore, |  |  |  |  |  |  |  |
| 3.3.1 | Semantics-Aware Scoping (Step 1.1) | the | EI identified | are only part of the full set of EI identified in |  |  |  |  |  |
| In this step, A | PPATCH | extracts the essential code that repre- | code slice provided to LLMs | V | exem | only contains the paths |  |  |  |
| sents the vulnerability semantics from each of the existing | between any of such identified EI subset and any of the vul- |  |  |  |  |  |  |  |  |
| vulnerable code samples. To that end, it first analyzes the sam- | nerable statements. This helps LLMs concentrate on the most |  |  |  |  |  |  |  |  |
| ple and constructs its system dependence graph (SDG) [23] | essential parts of the program for vulnerability patching. |  |  |  |  |  |  |  |  |
| through an | interprocedural dependence analysis | . An SDG is | In this template (as well as the one for dynamic adaptive |  |  |  |  |  |  |
| a representation that combines both data dependencies and | prompting’s root cause generation), we leverage vulnerability- |  |  |  |  |  |  |  |  |
| control dependencies of a program; thus, it is essential in com- | semantics-guided reasoning, which is described as " | Starting |  |  |  |  |  |  |  |
| puting the vulnerability semantics of a program. As shown in | with the external inputs, reason about the vulnerable behavior |  |  |  |  |  |  |  |  |
| Algorithm 1, the | vulnerability semantics computation | begins | step by step until the vulnerability is determined | ". Although |  |  |  |  |  |
| this process by building the SDG (line 2). Then, we perform a | this is simple, it significantly helps LLMs analyze the vulner- |  |  |  |  |  |  |  |  |
| simple static analysis to realize | IdentifyExternalInputs | ability root cause comprehensively and effectively. Figures 5 |  |  |  |  |  |  |  |
| (line 3). We first curate a set of external functions that may | and 9 show the comparison between the root cause analysis |  |  |  |  |  |  |  |  |
| produce external inputs or cause side effects to program states | with and without vulnerability-semantics-guided reasoning. |  |  |  |  |  |  |  |  |
| (e.g., malloc, socket_recv, scanf). Then, it traverses the pro- | Without such reasoning, the output misses many details for |  |  |  |  |  |  |  |  |
| gram’s control flow graph (CFG), identifying each callsite of | the vulnerability causes, which make the analysis inaccurate. |  |  |  |  |  |  |  |  |
| any of these external functions. To be more comprehensive, it | The key insight underlying our automated exemplar gener- |  |  |  |  |  |  |  |  |
| also considers the definition sites of program’s input variables | ation is that, with the ground-truth patches provided, LLMs |  |  |  |  |  |  |  |  |
| as an external input (we simply treat the program entry point | are capable of generating the correct reasoning steps which |  |  |  |  |  |  |  |  |
| as the joint entity of those definition sites). | are helpful to guide themselves to generate patches given new |  |  |  |  |  |  |  |  |
| As the main loop begins, we compute the interprocedural | samples to patch. To corroborate this hypothesis, we conduct |  |  |  |  |  |  |  |  |
| backward slice from each of the vulnerable statements | s | v | to | a preliminary experiment on the real-world samples from our |  |  |  |  |  |
| each of the external input | e | i | (lines 5-8), via another static anal- | collected dataset (see §5.1). Based on our manual inspection |  |  |  |  |  |
| ysis based on the SDG just constructed. It traverses the | sdg | on the generated exemplars by GPT-4, 92.98% of the reason- |  |  |  |  |  |  |  |
| from | s | v | , identifies backward dependencies transitively until | ing are correct, indicating that using LLMs to automatically |  |  |  |  |  |
| e | i | is reached (which has no further backward dependence). | generate exemplars is effective. These exemplars compose |  |  |  |  |  |  |
| Finally, we compute the union slice [8] for all external inputs | the quality exemplar pool for the dynamic adaptive prompting |  |  |  |  |  |  |  |  |
| in | EI | (line 8) and return it as the (code representation of the) | step (Step 2.2) to select exemplars from. |  |  |  |  |  |  |
| 1.2 generates the exemplars from the given existing vulner- | In Phase 2, given a testing sample that contains vulnerable |  |  |  |  |  |  |  |  |
| able samples. Since our dynamic adaptive prompting lever- | code and its vulnerability location, A | PPATCH | again computes |  |  |  |  |  |  |
| ages CoT prompting which guides LLMs to generate quality | the vulnerability semantics with the semantics-aware scop- |  |  |  |  |  |  |  |  |
| USENIX Association | 34th USENIX Security Symposium | 4485 |  |  |  |  |  |  |  |

---

## Page 7

| ing module. The process is the same as the one in Step 1.1: | In the prompt above, we start from the slice of the function |
| --- | --- |
| we construct the SDG from the source code, then get the | involving the vulnerable statements (line 14 in Algorithm 2) |
| vulnerability semantics via Algorithm 1. | and expand the slice on LLMs’ demand. Note that the EI |

3.4.2 Dynamic Adaptive Prompting (Step 2.2)

the LLMs to generate the patches step by step and (2) allow

1 Function DynPrompting( vul_slice , exemplars )

| 4 | foreach | exemplar in Exemplars | do |  |  |
| --- | --- | --- | --- | --- | --- |
| 7 | if | comp_ans is Yes | then |  |  |
| 8 | chosen_exemplars | .insert( | exemplar | ) | // Add similar exemplars |
| 10 | break | // Break when the exemplars are enough |  |  |  |
| 12 | return | cand_patches | ; |  |  |

13 Function GenCause( vul_slice )

16 while HasExpandDemand( LLMAns ) do

Root Cause Generation . We again leverage vulnerability

semantics reasoning to generate root cause analysis: given

the vulnerability semantics computed (i.e., the union slice

noted as V cause ), the CWE IDs, and the vulnerable statements

S v , A PPATCH first prompts the LLMs to generate the root

text_funcs":[func_1,func_2,CALLER_of_func...]} where

"CALLER_of_func" is a placeholder for the caller of the

given functions.

identified are only the part of EI identified in Algorithm I that

are relevant to the functions the LLM asked for so far. The

rationale is that LLMs usually have input token limitation

analysis and patching.

Algorithm 2 lines 13-19. Given the vulnerability code slice

dynamic adaptive prompting.

ysis for the testing sample, we select appropriate exemplars

Algorithm 2, an empty list, chosen_exemplars , is initialized

and each exemplar sample (line 6) with the following prompt:

Q : Are the following two root causes similar?

< exemplar_sample_root_cause >

< testing_sample_root_cause >

Please simply answer yes or no.

Patch Generation. Once the exemplars are selected,

A PPATCH prompts the LLMs to generate the patch (line 11)

with the following template:

| With the vulnerability semantics computed in Step 2.1, we | and thus we cannot input the whole projects into the models. |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| perform dynamic adaptive prompting to guide the LLMs | Even if the models are capable of accepting more tokens, the |  |  |  |  |  |  |  |  |  |
| to generate patches. The overall algorithm of this dynamic | irrelevant functions would distract the LLMs in analyzing |  |  |  |  |  |  |  |  |  |
| adaptive prompting step is shown in Algorithm 2. A | PPATCH | the vulnerabilities. Therefore, we only provide the part of the |  |  |  |  |  |  |  |  |
| leverages a | progressive prompting | strategy which prompts | slice that involves the functions that the LLM asks for. This |  |  |  |  |  |  |  |
| the LLMs to generate the root cause, select exemplars, and | progressive prompting scheme, similar to LLift [28], is es- |  |  |  |  |  |  |  |  |  |
| generate the patch in separated prompts. This is to (1) guide | sential for A | PPATCH | to achieve | interprocedural | vulnerability |  |  |  |  |  |
| LLMs to obtain the information and exemplars on demand. | The algorithm for generating the root cause is shown in |  |  |  |  |  |  |  |  |  |
| Algorithm 2: | Dynamic Adaptive Prompting | which may contain a large number of functions and state- |  |  |  |  |  |  |  |  |
| Input: | vul_slice | : vulnerable slice, | exemplars | : mined exemplars | ments, we start with the part of the slice only involving the |  |  |  |  |  |
| Output: | cand_patches | : candidate patches | functions that contain the vulnerability manifestation state- |  |  |  |  |  |  |  |
| 2 | cause | ← | GenCause( | vul_slice | ) | // Generate root cause of the slice | ments (line 14). Then, we iteratively query LLMs with the |  |  |  |
| 3 | chosen_exemplars | ← | [] | // Initialize an empty list | prompt template given earlier until the LLMs do not ask for |  |  |  |  |  |
| 5 | exemplar_cause | ← | GetExemCause( | exemplar | ) | // Extract cause | additional functions (lines 15-18). The final root cause analy- |  |  |  |
| 6 | comp_ans | ← | CompareCause( | cause, exemplar_cause | ) | sis is then returned to the main routine ( | DynPrompting | ) for |  |  |
| 9 | if | SizeOf( | chosen_exemplars | ) | ≥ | 8 | then | Exemplar Selection. | After generating the root cause anal- |  |
| 11 | cand_patches | ← | GenPatch( | chosen_exemplars, vul_slice | ) | to prompt the LLMs to generate the patches. As shown in |  |  |  |  |
| 14 | cause_slice | ← | GetVulFuncSlice( | vul_slice | ) | // Get vulnerable function slice | to store exemplars that closely match the root cause (line 3). |  |  |  |
| 15 | LLMAns | ← | GenCauseByLLM( | cause_slice | ) | // Get response from LLMs | The selection process iterates through the set of pre-mined |  |  |  |
| 17 | cause_slice | ← | cause_slice | ∪ | GetDemandedFuncSlice( | LLMAns | ) | exemplars and gets the vulnerability root causes from them |  |  |
| 18 | LLMAns | ← | GenCauseByLLM( | cause_slice | ) | (lines 4-5). To select the exemplars, we prompt the LLMs to |  |  |  |  |
| 19 | return | LLMAns | compare the root cause analysis result of the testing sample |  |  |  |  |  |  |  |
| cause (i.e., the natural-language description of the vulnerabil- | Considering that the complexity is | O | ( | mn | ) | where | m | is the |  |  |
| ity semantics reasoning steps). We prompt the LLM with the | number of exemplar samples and | n | is that of testing samples, |  |  |  |  |  |  |  |
| following template: | we let LLMs directly answer yes or no to save resources. |  |  |  |  |  |  |  |  |  |
| Q | : | Given | the | following | code | slice: | V | cause | which | Figure 6 shows parts of the exemplar selection process for |
| has | a | vulnerability | among | < | CWE-IDs | > | and | lines: | the example in Figure 1. Once the used LLM answers yes, |  |
| S | v | . | Starting | with | the | external | inputs: | <EI | identi- | the root cause analysis, fixing strategy, and the ground-truth |
| fied>, reason | about the | vulnerable | behavior step by | patch of that exemplar sample will be used as the exemplar |  |  |  |  |  |  |
| step until the vulnerability is determined. | If you en- | to prompt the LLMs to patch the testing sample (lines 7-8). |  |  |  |  |  |  |  |  |
| counter uncertainty due to a lack of function definitions, | We follow the original CoT work [51] and only select up to 8 |  |  |  |  |  |  |  |  |  |
| please tell the functions needed with the format {"con- | exemplars for each testing sample. |  |  |  |  |  |  |  |  |  |
| 4486 | 34th USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |  |

---

## Page 8

Q: Given the following code slice

<Code slice of function Jsi_Strcpy marked in Figure 1>

due to a lack of function definitions, please tell the functions needed with the format {"context_funcs":[func_1,func_2,CALLER_of_func...]} where"CALLER_of_func" is a

placeholder for the caller of the given functions.

A: {"context_funcs":[CALLER_of_ Jsi_Strcpy ...]}

Q: Given the following code slice

<Code slice of function Jsi_Strcpy and SplitChar marked in Figure 1>

A: Let's analyze the provided code to identify how this vulnerability manifests:

1. **Initialization and Loop Setup**:

- `cp` is initialized to point to the input string `str`.

- A `while` loop iterates over `str` until a null character is encountered, indicating the end of the string.

2. **Character Search and Increment**:

- Inside the loop, `cp` is set to the location of character `ch` in `str` using `Jsi_Strchr(cp, ch)`. If `ch` is not found, `cp` would be set to `NULL`.

- The inner `while` loop increments `cp` until a space character is found or the end of the string is reached. This loop intended to skip over non-space characters following `ch`.

3. **End of String Check**:

- After the inner loop, there's a check if `cp` is `NULL` or points to a null character. If true, the loop breaks, ending the parsing.

4. **Pointer Increment and Count**:

- `cp` is incremented to move past the found character or space, and `cnt` is incremented to count the number of segments or tokens.

5. **Memory Allocation and Pointer Setup**:

- `argv` is assigned the value from `Jsi_DSValue(dStr)`. This function is not defined in the provided code, so its behavior is unknown. We assume it returns a pointer to some

allocated memory intended to store pointers to tokens.

- `p` is set to point to an offset from `argv`, specifically `&(argv[cnt+2])`. This seems intended to point to a location right after the space allocated for `argv` pointers.

6. **String Copy**:

- `Jsi_Strcpy(p, str)` copies the entire input string `str` to the location pointed to by `p`.

**Vulnerability Analysis**:

- The critical issue arises at the line `p = (char*)&(argv[cnt+2]);`. Here, `p` is calculated based on `cnt`, which is incremented for each token found in `str`. However, there's no

check to ensure that this calculation does not exceed the memory initially allocated for `argv`. If `cnt` becomes large enough, `p` could point beyond the allocated memory for

`argv`, leading to an out-of-bounds write when `Jsi_Strcpy(p, str)` is executed.

Q: Does the following two vulnerabilities share similar root causes? Please

- 2: Array Size and Indexing:

- The size of the `offered` array is fixed at `max_offered + 1`.

- The loop iterates `num` times

Potential Vulnerability:

- The vulnerability arises if `num` exceeds `max_offered + 1`, which results

"""

1. **Initialization and Loop Setup**:

- `cp` is initialized to point to the input string `str`…

....

6. **String Copy**:

- `Jsi_Strcpy(p, str)` copies the entire input string `str` to the location pointed

**Vulnerability Analysis**:

- The critical issue arises at the line `p = (char*)&(argv[cnt+2]);`. Here, `p`

is calculated based on `cnt`, which is incremented for each token found in

`str`. However, there's no check to ensure that this calculation does not

exceed the memory initially allocated for `argv`. If `cnt` becomes large

enough, `p` could point beyond the allocated memory for `argv`, leading to

an out-of-bounds write when `Jsi_Strcpy(p, str)` is executed.

A: Yes // The H[HPSODU is selected for prompting

Q: Does the following two vulnerabilities share similar root causes? Please

simply answer yes or no without explanation

// root cause of a QH[HPSODU

"""

1. **Understanding the Code:**

an argument.

- Memory is allocated using `kmalloc`.

- If the allocated memory is not properly initialized, it can lead to undefined

behavior when the memory is accessed, potentially leading to security

// root cause of the testing sample

< selected exemplars >

Q : Given the following code slice: V cause which has a vul-

ate five possible patches for the vulnerability.

A : Step 1. < root cause analysis >

// Selected Exemplar 1

A:

Step 3. <Patch of the selected  >

// Selected Exemplar 2

……

// Selected Exemplar 8

// Testing sample from Figure 1

possible patches for the vulnerability.

Step 1. Root Cause Analysis: ...

Step 2. Fixing Strategy: To fix this vulnerability, the code should

check sufficient space before copying.

Step 3. Patch Generation:

```

< Jsi_Strcpy(p, str);

---

Jsi_DSLength(dStr)) {

| > | Jsi_Strcpy(p, str); |
| --- | --- |
| > | } else { |
| > | // Handle error: not enough space |
| > | } |

```

…… // Other four candidate patches.

A PPATCH .

dynamically selected exemplars, the LLMs are expected to

generate quality patches.

After generating the candidate patches, we further leverage

multi-faceted (i.e., fixing vulnerability and preserving func-

which has a CWE-787 vulnerability at line 24. Starting with input, reason about the vulnerable behavior step by step until the vulnerability is determined. If you encounter uncertainty

which has a CWE-787 vulnerability at line 24. Starting with input, reason about the vulnerable behavior step by step until the vulnerability is determined. If you encounter uncertainty …

Figure 5: Root cause analysis generated by GPT-4 with vulnerability semantics reasoning for the sample in Figure 1.

| simply answer yes or no without explanation | Q: Given the following code slice: <slice code> |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| // root cause of a | QH[HPSODU | which has a CWE-787 vulnerability at line <vulnerable line>, please |  |  |  |  |  |  |  |
| """ | generate five possible patches for the vulnerability. |  |  |  |  |  |  |  |  |
| - 1: Validate `num`: | Step 1. <Root cause analysis for the selected |  | > |  |  |  |  |  |  |
| - `num` is obtained from `hello->getOfferNum()` | Step 2. <Fixing Strategy for the selected |  | > |  |  |  |  |  |  |
| in writing past the end of the `offered` array. | Q: Given the following code slice: <Slice in Figure 5> |  |  |  |  |  |  |  |  |
| // root cause of the testing sample | which has a CWE-787 vulnerability at line 24, please generate five |  |  |  |  |  |  |  |  |
| to by `p`. | > | if ((char*)p - Jsi_DSValue(dStr) + Jsi_Strlen(str) < |  |  |  |  |  |  |  |
| """ | Figure 7: GPT-4’s patch for the sample in Figure 1 with |  |  |  |  |  |  |  |  |
| - The function `rfcomm_get_dev_list` takes a user-space pointer `arg` as | ing sample’s vulnerability semantics slice ( | V | cause | ) used for |  |  |  |  |  |
| … | the final root cause generation, CWE-IDs, and the vulnera- |  |  |  |  |  |  |  |  |
| 2. **Identifying the Vulnerability:** | ble statements ( | S | v | ) with the same format as the exemplars. |  |  |  |  |  |
| vulnerabilities such as information leakage or use of uninitialized data.""" | We also prompt the LLMs to generate more than one candi- |  |  |  |  |  |  |  |  |
| // Same as above | date patch so that the recall can be improved and developers |  |  |  |  |  |  |  |  |
| A: No | // The | H[HPSODU | is NOT selected for prompting | have more choices to select appropriate patches from. To |  |  |  |  |  |
| Figure 6: Exemplar selection by GPT-4 for the sample in | avoid repeated output, we also | add the root cause generated |  |  |  |  |  |  |  |
| Figure 1. | in the previous step | for the LLMs to follow through. With the |  |  |  |  |  |  |  |
| nerability among | < | CWE-IDs | > | and lines: | S | v | , please gener- | 3.4.3 | Multi-Faceted Patch Validation (Step 2.3) |
| In this prompt, we first provide the selected exemplars | tionality) patch validation to reduce incorrect patches which |  |  |  |  |  |  |  |  |
| where each exemplar includes its vulnerability semantics | are not useful for developers. Considering that the same LLM |  |  |  |  |  |  |  |  |
| (union slice), CWE-IDs, vulnerable statements, as well as the | may not be effective for validating the generated patches by |  |  |  |  |  |  |  |  |
| root cause analysis, the fixing strategy, and the ground-truth | itself, we leverage the ensemble method to conduct the vali- |  |  |  |  |  |  |  |  |
| patch. This is to guide the LLMs to patch the testing sample | dation. Therefore, multiple effective LLMs for vulnerability |  |  |  |  |  |  |  |  |
| with a similar, complete workflow. Then, we provide the test- | patching are used for the validation. |  |  |  |  |  |  |  |  |
| USENIX Association | 34th USENIX Security Symposium | 4487 |  |  |  |  |  |  |  |

---

## Page 9

Algorithm 3: Multi-Faceted Patch Validation Table 1: LLMs used in our study

| 3 | foreach | cand_patch | in | cand_patches | do |  |
| --- | --- | --- | --- | --- | --- | --- |
| 4 | retain | ← | False |  |  |  |
| 6 | val_ans | ← | ValPatchLLM( | cand_patch, llm | ) | // Validate the patch |
| 8 | retain | ← | True | // Remove the patch if all the LLMs think it is invalid |  |  |
| 10 | valid_patches | .remove( | cand_patch | ) |  |  |
| 11 | return | valid_patches |  |  |  |  |

Q: Given the following code slice: <vulnerability

ability at line 24, please validate whether the following patch fixes the vulnerability while

< Jsi_Strcpy(p, str);

> if ((char*)p - Jsi_DSValue(dStr) + Jsi_Strlen(str) < Jsi_DSLength(dStr)) {

> // Handle error: not enough space

```

Algorithm 3 shows the workflow for the validation. It ini-

tializes by considering all candidate patches as potentially

valid (line 2). It then enters a nested loop where each candi-

date patch is evaluated independently against each LLM to

ascertain its validity (lines 3-4). Within the inner loop, each

patch undergoes a validation check by an individual LLM,

which determines if the patch is effective (line 5). Each LLM

evaluates whether each generated patch fixes the vulnerability

correctly with the following prompt:

Q: Given the following code slice: V cause which has a vul-

nerability among < CWE-IDs > and lines: S v . Please val-

while keeping the functionality: < patch > . Please simply

and answers for the example in Figure 1. If any LLM approves

the patch, a flag (retain) is set to True, indicating that the patch

Model Version #Params Max #Tokens Vendor Release date Cutoff Date

voting may improve the precision but reduce the recall, which

4 Implementation

To support the generation of interprocedural vulnerability se-

leverage the call graph also provided by Joern to conduct

ward slice from the vulnerable statements. In this work, we

reuse the script from SySeVR [33] to quickly query the con-

trol flow nodes for the respective statements and find the

in-degree edges and nodes. Based on this, we further imple-

ment the semantics-aware scoping algorithm, as shown in

Algorithm 1. The extracted vulnerability semantics slices are

stored as sliced source code text for LLMs to use.

5 Evaluation

We evaluate A PPATCH via four research questions (RQs):

ities patching?

• RQ4: How efficient is A PPATCH for patch generation?

| Input: | cand_patches | : candatate patches, | llms | : LLMs used for validation | Gemini-1.5 | gemini-1.5-pro | 50T | 30,720 | Google | May 2024 | Nov. 2023 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Output: | valid_patches | : validated patches | Claude-3.5 | claude-3.5-sonnet | 70B | 200,000 | Anthropic | Jun. 2024 | Apr. 2024 |  |  |  |  |
| 1 | Function | PatchValidation( | cand_patches | , | llms | ) | GPT-4 | gpt-4-turbo | 175B+ | 128,000 | OpenAI | May 2024 | Oct. 2023 |
| 2 | valid_patches gets cand_patches | Llama-3.1 | llama-3.1-70b | 70B | 4,096 | Meta | July 2024 | Dec. 2023 |  |  |  |  |  |
| 5 | foreach | llm in llms | do | than majority voting because A | PPATCH | aims to improve the |  |  |  |  |  |  |  |
| with an LLM | recall while keeping the precision, which is more practically |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | if | val_ans | is Yes | then | valuable than otherwise for real-world developers. Majority |  |  |  |  |  |  |  |  |
| 9 | if | retain is False | then | is less helpful for real-world patching. |  |  |  |  |  |  |  |  |  |
| semantics slice in Figure 5> which has a CWE-787 vulner- | mantics, we use Joern [53] to construct the SDG of the given |  |  |  |  |  |  |  |  |  |  |  |  |
| keeping the functionality: <patch>. Please simply answer yes or no. | vulnerable program under patching. In this work, since we |  |  |  |  |  |  |  |  |  |  |  |  |
| ``` | evaluate A | PPATCH | on a number of C code samples without |  |  |  |  |  |  |  |  |  |  |
| --- | compiling them, we chose Joern which is a powerful tool |  |  |  |  |  |  |  |  |  |  |  |  |
| > | Jsi_Strcpy(p, str); | designed for scalable code analysis without requiring com- |  |  |  |  |  |  |  |  |  |  |  |
| > | } else { | pilability of the input code. Specifically, we first obtain the |  |  |  |  |  |  |  |  |  |  |  |
| > | } | PDG (which includes the control and data dependencies) for |  |  |  |  |  |  |  |  |  |  |  |
| A: Yes // By GPT-4 | A: yes // By Gemini | A: Yes // By Claude3 | A: Yes // By Llama3 | each function (which Joern immediately provides). Then, we |  |  |  |  |  |  |  |  |  |
| Figure 8: Multi-faceted patch validation for the sample in | the interprocedural dependence analysis hence building the |  |  |  |  |  |  |  |  |  |  |  |  |
| Figure 1. | SDG. With the SDG, we extract the interprocedural back- |  |  |  |  |  |  |  |  |  |  |  |  |
| idate whether the following patch fixes the vulnerability | • | RQ1: | How effective is A | PPATCH | for real-world vulnerabil- |  |  |  |  |  |  |  |  |
| answer yes or no. | • | RQ2: | How does each of the key design components of |  |  |  |  |  |  |  |  |  |  |
| In the prompt, we also ask the LLMs whether the patch | A | PPATCH | contribute to its overall performance? |  |  |  |  |  |  |  |  |  |  |
| keeps the functionality to avoid valid but incorrect patches. | • | RQ3: | How effective is A | PPATCH | compared to existing |  |  |  |  |  |  |  |  |
| Figure 8 shows the multi-faceted patch validation prompts | vulnerability patching techniques? |  |  |  |  |  |  |  |  |  |  |  |  |
| should be retained in the list of valid patches (lines 6-8). If | We first describe the LLMs, datasets and metrics used. Then, |  |  |  |  |  |  |  |  |  |  |  |  |
| after evaluation by all the LLMs, a patch is not validated by | we answer the four research questions above. |  |  |  |  |  |  |  |  |  |  |  |  |
| any (i.e., the retain flag remains False), it is removed from the | LLMs. | Table 1 summarizes the four SOTA LLMs chosen |  |  |  |  |  |  |  |  |  |  |  |
| list of valid patches (lines 9-10). This step ensures that only | for our study to cover the latest models of a variety of sizes |  |  |  |  |  |  |  |  |  |  |  |  |
| those patches that have been validated by at least one LLM | and vendors. | Gemini-1.5 | [45] and | Claude-3.5 | [5] are the |  |  |  |  |  |  |  |  |
| are kept. The algorithm concludes by returning the refined list | latest LLMs from Google and Anthropic, respectively. We |  |  |  |  |  |  |  |  |  |  |  |  |
| of validated patches, which have passed through this rigorous | chose their most popular powerful ( | Pro | and | Sonnet | ) for both |  |  |  |  |  |  |  |  |
| validation process (line 11). We use such an approach rather | effectiveness and efficiency. | GPT-4 | is the latest and most |  |  |  |  |  |  |  |  |  |  |
| 4488 | 34th USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 10

| powerful LLM from OpenAI and we use its most power- | ples from ExtractFix are compilable and come with test cases |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ful version | GPT-4-Turbo | . | Llama3.1 | [46] is an SOTA LLM | that allow us to validate patches. From this dataset, we collect |
| from Meta, of which we also chose to use the powerful ver- | 20 vulnerabilities that can be reproduced, for each of which |  |  |  |  |
| sion llama-3.1-70b for our experiments. We chose general- | we label the manifestation locations and the CWE IDs based |  |  |  |  |
| purpose LLMs instead of code-specific ones (e.g., CodeL- | on the crash information from the test cases. Detailed statis- |  |  |  |  |
| lama) because the latter are less capable of code analysis. | tics of this dataset can be also found in Appendix Table 8. We |  |  |  |  |
| As shown in Appendix Table 9, our preliminary experiments | also addressed data leakage concerns with it in Appendix E. |  |  |  |  |
| revealed that A | PPATCH | , when based on popular code-specific | Metrics. | Since the dataset covers many projects and it is dif- |  |
| LLMs (CodeLlama [2], CodeQwen 1.5 [3], and DeepSeek- | ficult to compile each of the samples and use the test cases to |  |  |  |  |
| Coder-v2 [57]), achieved only 1.21%, 10.12%, and 9.09% F1 | validate the generated patches (furthermore, some of the sam- |  |  |  |  |
| scores, respectively, significantly lower than the performance | ples do not come with test cases), we cannot automatically |  |  |  |  |
| of general-purpose LLMs when used in A | PPATCH | as base | validate the generated patches if they do not exactly match the |  |  |
| LLMs as shown in Table 2. | ground truths. Therefore, we manually check each generated |  |  |  |  |
| Datasets. | To collect exemplar samples for Phase 1 ( | Exemplar | patch. To improve the manual evaluation and better under- |  |  |
| Mining | ), we use existing widely used vulnerability datasets | stand the generated patches, we consider four metrics: (1) if |  |  |  |
| PatchDB | [49] and | CVEFixes | [9], where PatchDB con- | the generated patch exactly matches the ground truth, we con- |  |
| tains 12073 real-world fixing samples and CVEFixes con- | sider it as | syntactic equivalent (SynEq) | ; (2) if the generated |  |  |
| tains 4,120 real-world fixing samples in C language. In this | patch does not exactly match the ground truth but the behavior |  |  |  |  |
| work, we select the samples with the most popular CWEs | is the same as the ground truth, we consider it as | semantically |  |  |  |
| in C languages: CWE-787 (out-of-bound write), CWE-125 | equivalent (SemEq) | ; (3) if the patch has different behavior |  |  |  |
| (out-of-bound read), CWE-190 (integer overflow), CWE-401 | from the ground truth but still fix the vulnerability without |  |  |  |  |
| (memory leak), CWE-457 (use of uninitialized variable), and | breaking the code functionality, we consider it as | plausible | ; |  |  |
| CWE-476 (use of NULL pointer). However, some of the fixes | (4) all the samples with the three metrics above are consid- |  |  |  |  |
| contain edits not relevant to vulnerabilities (e.g., code refac- | ered as | correct | . To better simulate the real-world patching |  |  |
| toring or adding new functionalities). Therefore, we manually | scenarios, we prompt the LLMs to generate up to five patches |  |  |  |  |
| inspect each of the samples and filter out the inappropriate | so that developers can pick up the one most suitable to patch |  |  |  |  |
| samples. To be realistic, we read the vulnerability reports | the vulnerable code. To better evaluate the generated patches, |  |  |  |  |
| and label vulnerability manifestation locations, rather than | we consider three measures: |  |  |  |  |

the code changed lines in the vulnerability fixing commits.

checking outcomes and discussions to resolve disagreements.

between the training set and the testing sets discussed below.

For the testing set, considering that the latest powerful

ing. Thus, there may be data leakage and contamination issues

if we use the samples from PatchDB and CVEFixes as the

testing set. Therefore, we collect a Zero-Day dataset

| recall | = | (1) |
| --- | --- | --- |
| precision | = | (2) |

2 × recall × precision

recall + precision

5.1 RQ1: Effectiveness

| We applied an inter-rater agreement/consensus procedure— | # | f ixed samples |  |  |
| --- | --- | --- | --- | --- |
| each author independently labeled them, followed by cross- | # | testing sample |  |  |
| We also remove the overlapped samples between PatchDB | # | correct patches |  |  |
| and CVEFixes, as well as confirming that there is no overlap | # | generated patches |  |  |
| As a result, we collect 306 vulnerability fixing samples. | F | 1 | = | (3) |
| LLMs are trained on existing data, it is possible that they have | where | f ixed sample | means a sample where at least one of |  |
| seen the samples in PatchDB and CVEFixes during the train- | the generated patches fix the vulnerability. |  |  |  |
| where all the vulnerabilities were reported after the latest | Table 2 shows the effectiveness of A | PPATCH | against the |  |
| cutoff date of the LLMs (04/2024 from Claude-3.5-Sonnet). | two testing datasets. We notice that A | PPATCH | achieves the |  |
| As a result, we collect 97 vulnerabilities which also cover | best overall effectiveness for vulnerability patching. With |  |  |  |
| the same CWEs as PatchDB and CVEFixes. Among them, | A | PPATCH | , GPT-4, Gemini-1.5, Claude-3.5, and Llama-3.1 |  |
| 21 vulnerabilities are interprocedural where the vulnerabil- | achieve 33.30%, 20.44%, 36.46%, and 24.28% F1 for the cor- |  |  |  |
| ity manifestation locations and the patching locations are | rectness metric on our collected Zero-Day dataset, which is |  |  |  |
| in different functions. These samples cover 18 open-source | the best among other prompting approaches. On the existing |  |  |  |
| projects including Linux Kernal, FFmpeg, etc. Appendix Ta- | ExtractFix dataset, A | PPATCH | again achieves the best among |  |
| ble 8 shows the detailed statistics of the dataset. | other prompting approaches, with 68.41%, 42.90%, 73.86%, |  |  |  |
| To compare A | PPATCH | with existing vulnerability patch- | and 64.20% F1 for the correctness metric, respectively. The |  |
| ing techniques, we also use an existing vulnerability dataset | overall effectiveness on ExtractFix dataset is higher, indicat- |  |  |  |
| ExtractFix | [20] for comparison experiments. The sam- | ing the challenges on Zero-Day vulnerability patching. |  |  |
| USENIX Association | 34th USENIX Security Symposium | 4489 |  |  |

---

## Page 11

Table 2: Effectiveness of A PPATCH

| Zero-Day Dataset | ExtractFix Dataset |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | Approach | SynEq | SemEq | Plausible | Correct | SynEq | SemEq | Plausible | Correct |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Recall | Prec | F1 | Recall | Prec | F1 | Recall | Prec | F1 | Recall | Prec | F1 | Recall | Prec | F1 | Recall | Prec | F1 | Recall | Prec | F1 | Recall | Prec | F1 |  |  |
| A | PPATCH | 6.19% | 1.64% | 2.59% | 26.80% | 14.48% | 18.80% | 25.77% | 12.84% | 17.14% | 39.18% | 28.96% | 33.30% | 5.00% | 2.30% | 3.15% | 75.00% | 42.53% | 54.28% | 40.00% | 10.34% | 16.44% | 90.00% | 55.17% | 68.41% |
| No Validation | 7.22% | 1.46% | 2.42% | 28.87% | 13.10% | 18.02% | 28.87% | 11.02% | 15.95% | 44.33% | 25.57% | 32.43% | 5.00% | 1.98% | 2.84% | 80.00% | 41.58% | 54.72% | 45.00% | 9.90% | 16.23% | 90.00% | 53.47% | 67.08% |  |
| No Slicing | 3.09% | 0.61% | 1.02% | 28.87% | 8.98% | 13.70% | 21.65% | 9.80% | 13.49% | 39.18% | 19.39% | 25.94% | 10.00% | 1.98% | 3.31% | 65.00% | 41.58% | 50.72% | 30.00% | 11.88% | 17.02% | 80.00% | 55.45% | 65.50% |  |

GPT-4 Random Exemplars 5.15% 1.02% 1.71% 31.96% 11.48% 16.89% 23.71% 6.97% 10.77% 44.33% 19.47% 27.05% 10.00% 1.98% 3.31% 75.00% 35.64% 48.32% 50.00% 17.82% 26.28% 80.00% 55.45% 65.50%

Manual Exemplars 3.09% 1.03% 1.54% 28.87% 11.11% 16.05% 17.53% 5.97% 8.90% 42.27% 18.11% 25.35% 5.00% 0.99% 1.65% 70.00% 39.60% 50.59% 35.00% 11.88% 17.74% 85.00% 52.48% 64.89%

Direct Reasoning 3.09% 0.62% 1.03% 22.68% 8.28% 12.13% 19.59% 6.83% 10.13% 36.08% 15.73% 21.91% 5.00% 0.99% 1.65% 75.00% 43.56% 55.11% 30.00% 6.93% 11.26% 80.00% 51.49% 62.65%

Standard Prompting 3.09% 0.62% 1.03% 18.56% 7.19% 10.36% 17.53% 6.78% 9.77% 30.93% 14.58% 19.82% 5.00% 0.99% 1.65% 65.00% 40.59% 49.98% 30.00% 9.90% 14.89% 65.00% 51.49% 57.46%

Zero-shot Completion 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 12.37% 6.78% 8.76% 12.37% 6.78% 8.76% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 15.00% 3.96% 6.27% 15.00% 3.96% 6.27%

| A | PPATCH | 2.06% | 0.56% | 0.88% | 9.28% | 6.16% | 7.41% | 21.64% | 9.80% | 13.49% | 26.80% | 16.53% | 20.44% | 0.00% | 0.00% | 0.00% | 35.00% | 18.68% | 24.20% | 30.00% | 16.48% | 21.28% | 50.00% | 35.16% | 42.90% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No Validation | 2.06% | 0.55% | 0.87% | 9.28% | 6.32% | 7.52% | 21.64% | 9.61% | 13.31% | 26.80% | 16.48% | 20.41% | 0.00% | 0.00% | 0.00% | 35.00% | 17.46% | 23.30% | 30.00% | 15.87% | 20.76% | 50.00% | 33.33% | 40.00% |  |
| No Slicing | 0.00% | 0.00% | 0.00% | 10.31% | 5.08% | 6.81% | 18.56% | 10.56% | 13.69% | 24.74% | 15.93% | 19.38% | 0.00% | 0.00% | 0.00% | 20.00% | 15.94% | 17.74% | 35.00% | 18.84% | 24.50% | 40.00% | 34.78% | 37.21% |  |

Gemini-1.5 Random Exemplars 1.03% 0.34% 0.51% 12.37% 5.82% 7.92% 15.46% 8.56% 11.02% 24.74% 14.72% 18.46% 5.00% 1.09% 1.79% 35.00% 17.39% 23.24% 25.00% 10.87% 15.15% 45.00% 29.35% 35.53%

Manual Exemplars 2.06% 0.68% 1.03% 9.28% 4.11% 5.70% 17.52% 10.96% 13.48% 22.68% 15.75% 18.59% 0.00% 0.00% 0.00% 25.00% 13.79% 17.78% 30.00% 14.94% 19.95% 45.00% 28.74% 35.07%

Direct Reasoning 1.03% 0.29% 0.46% 8.25% 3.24% 4.66% 20.61% 8.85% 12.39% 25.77% 12.38% 16.73% 0.00% 0.00% 0.00% 45.00% 30.21% 36.15% 10.00% 3.13% 4.76% 45.00% 33.33% 38.30%

Standard Prompting 1.03% 0.26% 0.41% 11.34% 4.10% 6.03% 18.56% 6.92% 10.08% 25.77% 11.28% 15.69% 0.00% 0.00% 0.00% 20.00% 12.87% 15.66% 30.00% 12.87% 18.01% 45.00% 25.74% 32.75%

Zero-shot Completion 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 3.09% 1.21% 1.74% 3.09% 1.21% 1.74% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 20.00% 8.24% 11.67% 20.00% 8.24% 11.67%

| A | PPATCH | 4.12% | 0.92% | 1.51% | 37.11% | 17.32% | 23.62% | 22.68% | 10.62% | 14.47% | 49.48% | 28.87% | 36.46% | 10.00% | 2.04% | 3.39% | 80.00% | 44.90% | 57.52% | 45.00% | 18.37% | 26.09% | 85.00% | 65.31% | 73.86% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No Validation | 5.15% | 1.07% | 1.78% | 37.11% | 16.52% | 22.87% | 22.68% | 10.09% | 13.96% | 50.52% | 27.68% | 35.77% | 10.00% | 1.98% | 3.31% | 80.00% | 44.55% | 57.23% | 45.00% | 17.82% | 25.53% | 85.00% | 64.36% | 73.25% |  |
| No Slicing | 3.09% | 0.63% | 1.05% | 27.84% | 12.47% | 17.23% | 27.84% | 10.57% | 15.32% | 41.24% | 23.68% | 30.08% | 10.00% | 1.98% | 3.31% | 65.00% | 44.55% | 52.87% | 30.00% | 7.92% | 12.53% | 80.00% | 54.46% | 64.80% |  |

Claude-3.5 Random Exemplars 1.03% 0.21% 0.34% 28.87% 15.11% 19.84% 17.53% 6.83% 9.83% 41.24% 22.15% 28.82% 5.00% 0.99% 1.65% 75.00% 43.56% 55.11% 45.00% 16.83% 24.50% 90.00% 61.39% 72.99%

Manual Exemplars 2.06% 0.42% 0.69% 29.90% 13.13% 18.24% 21.65% 8.13% 11.82% 41.24% 21.67% 28.41% 5.00% 0.99% 1.65% 80.00% 46.53% 58.84% 40.00% 9.90% 15.87% 85.00% 57.43% 68.54%

Direct Reasoning 2.06% 0.49% 0.80% 23.71% 14.32% 17.86% 17.53% 7.65% 10.66% 37.11% 22.47% 27.99% 5.00% 0.99% 1.65% 75.00% 52.48% 61.75% 35.00% 15.84% 21.81% 75.00% 69.31% 72.04%

Standard Prompting 2.06% 0.43% 0.72% 24.74% 12.61% 16.70% 14.43% 6.09% 8.56% 28.87% 19.13% 23.01% 15.00% 2.97% 4.96% 55.00% 40.59% 46.71% 25.00% 12.87% 16.99% 65.00% 56.44% 60.42%

Zero-shot Completion 0.00% 0.00% 0.00% 4.12% 1.12% 1.76% 15.46% 8.28% 10.78% 18.56% 9.40% 12.48% 0.00% 0.00% 0.00% 5.00% 3.49% 4.11% 30.00% 17.44% 22.06% 30.00% 20.93% 24.66%

| A | PPATCH | 1.03% | 0.27% | 0.42% | 21.65% | 9.55% | 13.25% | 18.56% | 8.75% | 11.89% | 35.05% | 18.57% | 24.28% | 5.00% | 1.03% | 1.71% | 70.00% | 44.33% | 54.28% | 20.00% | 8.25% | 11.68% | 80.00% | 53.61% | 64.20% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No Validation | 1.03% | 0.22% | 0.36% | 22.68% | 9.41% | 13.30% | 20.62% | 8.09% | 11.62% | 38.14% | 17.72% | 24.20% | 5.00% | 0.99% | 1.65% | 70.00% | 42.57% | 52.95% | 20.00% | 7.92% | 11.35% | 80.00% | 51.49% | 62.65% |  |
| No Slicing | 2.06% | 0.49% | 0.79% | 20.62% | 9.09% | 12.62% | 11.34% | 4.67% | 6.61% | 28.87% | 14.25% | 19.08% | 0.00% | 0.00% | 0.00% | 70.00% | 29.70% | 41.71% | 30.00% | 10.89% | 15.98% | 75.00% | 40.59% | 52.68% |  |

Llama-3.1 Random Exemplars 1.03% 0.22% 0.37% 15.46% 6.52% 9.17% 9.28% 4.49% 6.06% 23.71% 11.24% 15.25% 5.00% 0.99% 1.65% 65.00% 39.60% 49.22% 10.00% 2.97% 4.58% 75.00% 43.56% 55.11%

Manual Exemplars 3.09% 0.74% 1.19% 19.59% 11.30% 14.33% 11.34% 4.67% 6.61% 29.90% 16.71% 21.44% 5.00% 0.99% 1.65% 70.00% 34.65% 46.36% 30.00% 11.88% 17.02% 85.00% 47.52% 60.96%

Direct Reasoning 4.12% 0.83% 1.39% 15.46% 7.71% 10.29% 17.52% 6.45% 9.44% 31.95% 15.00% 20.41% 0.00% 0.00% 0.00% 70.00% 48.51% 57.31% 30.00% 5.94% 9.92% 70.00% 54.46% 61.26%

Standard Prompting 3.09% 0.63% 1.05% 14.43% 7.34% 9.73% 14.43% 5.87% 8.35% 24.74% 13.84% 17.75% 0.00% 0.00% 0.00% 60.00% 40.59% 48.43% 15.00% 5.94% 8.51% 65.00% 46.53% 54.24%

Zero-shot Completion 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 9.28% 4.17% 5.75% 9.28% 4.17% 5.75% 0.00% 0.00% 0.00% 5.00% 1.98% 2.84% 5.00% 2.97% 3.73% 5.00% 4.95% 4.98%

| In terms of recall, Claude-3.5 achieves the best with 49.48% | F1 on the Zero-Day dataset and 40.00%–73.25% F1 on the |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| on the Zero-Day dataset and GPT-4 acheives the best with | ExtractFix dataset, indicating that the multi-faceted patch |  |  |  |  |
| 90.00% on the ExtractFix dataset. GPT-4 achieves the best | validation is useful to improve the precision. |  |  |  |  |
| precision 28.96% on the Zero-Day dataset and Claude-3.5 | We then examine the contribution of semantics-aware scop- |  |  |  |  |
| achieves the best precision 65.31% on the ExtractFix dataset. | ing. In this ablation study, instead of using the vulnerability |  |  |  |  |
| In terms of different metrics, Claude-3.5 has 37.11% and | semantics slice, we directly input the whole source code sam- |  |  |  |  |
| 80.00% recall on semantics equivalent against the Zero- | ple into the LLMs for analysis. As shown in rows “No slicing”, |  |  |  |  |
| Day and ExtractFix datasets, respectively. This indicates that | without the vulnerability semantics slicing, the recall, preci- |  |  |  |  |
| A | PPATCH | generates patches close to developers’ patches. | sion, and F1 drop significantly compared with A | PPATCH | , with |
| A | PPATCH | is effective for vulnerability patching, with up | 19.08%–30.08% F1 on the Zero-Day dataset and 37.21%– |  |  |
| to 36.46% and 73.86% F1 on the Zero-Day and ExtractFix | 65.50% F1 on the ExtractFix dataset. The reason is that, |  |  |  |  |
| dataset, respectively, showing its practical potential. | without slicing, the code not relevant to vulnerabilities is also |  |  |  |  |

inputted into the LLMs, thus distracting the analysis and im-

pact the accuracy of the root cause analysis. To prove this, we

| Table 3: Effectiveness of A | PPATCH | against the interprocedu- | examine the correct rates of the reasoning on the testing sam- |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ral samples from the Zero-Day dataset | ples. As Table 10 shows, vulnerability semantics reasoning |  |  |  |  |  |  |  |  |
| Approach | Model | Correct | Model | Correct |  |  |  |  |  |
| Recall | Prec | F1 | Recall | Prec | F1 | achieves higher accuracy if we have vulnerability semantics |  |  |  |
| A | PPATCH | 38.10% | 26.67% | 31.37% | 47.62% | 25.93% | 33.57% |  |  |
| No Validation | 38.10% | 25.23% | 30.35% | 47.62% | 25.23% | 32.98% | scoping/slicing. This indicates the importance of inputting |  |  |
| No Slicing | 33.33% | 18.18% | 23.53% | 38.10% | 21.78% | 27.72% |  |  |  |
| Random Exemplars | 33.33% | 15.32% | 20.99% | 47.62% | 19.82% | 27.99% |  |  |  |
| GPT-4 | core vulnerability semantics for analysis. |  |  |  |  |  |  |  |  |
| Manual Exemplars | 38.10% | 17.27% | 23.77% | Claude-3.5 | 42.86% | 18.92% | 26.25% |  |  |
| Direct Reasoning | 38.10% | 13.51% | 19.95% | 42.86% | 19.81% | 27.10% |  |  |  |
| Standard Prompting | 19.05% | 6.60% | 9.81% | 14.29% | 6.86% | 9.27% | To examine the usefulness of dynamic adaptive prompting, |  |  |
| Zero-shot Completion | 9.52% | 4.72% | 6.31% | 14.29% | 5.94% | 8.39% |  |  |  |
| A | PPATCH | 28.57% | 14.14% | 18.91% | 38.10% | 17.65% | 24.12% | we conduct experiments with randomly selected exemplars |  |
| No Validation | 28.57% | 13.34% | 18.18% | 38.10% | 14.41% | 20.91% |  |  |  |
| No Slicing | 23.81% | 12.37% | 16.28% | 14.29% | 23.08% | 17.65% | rather than selecting exemplars based on the root causes of |  |  |
| Random Exemplars | 23.81% | 11.46% | 15.47% | 23.81% | 10.89% | 14.95% |  |  |  |
| Manual Exemplars | Gemini-1.5 | 23.81% | 11.11% | 15.15% | Llama-3.1 | 19.05% | 15.38% | 17.02% | the vulnerabilities. Note that we still keep the CWEs of the ex- |
| Direct Reasoning | 23.81% | 7.62% | 11.54% | 28.57% | 10.81% | 15.68% |  |  |  |
| Standard Prompting | 4.76% | 1.10% | 1.79% | 9.52% | 3.13% | 4.71% | emplars the same as the testing sample. As shown in the rows |  |  |
| Zero-shot Completion | 0.00% | 0.00% | 0.00% | 9.52% | 2.70% | 4.21% |  |  |  |

“Random Exemplars”, we notice that the F1 scores drop dra-

matically compared with A PPATCH .The exemplars selected

| 5.2 | RQ2: Contributions of Components | for prompting have promising fixing strategies which help |  |
| --- | --- | --- | --- |
| As shown in Table 2, we then examine the contributions of | LLMs patch the vulnerability correctly, while they may pick |  |  |
| the A | PPATCH | components with the ablated prompting ap- | up incorrect fixing strategies to patch with random exemplars. |
| proaches. The numbers marked in red are the best F1 scores | This indicates the importance and effectiveness of dynamic |  |  |
| achieved by the ablated prompting approaches. One of the ab- | prompting for vulnerability patching. |  |  |
| lated versions, “Manual Exemplars”, corresponds to our prior | As the exemplars in our exemplar pool are generated by |  |  |
| work [37], which is | also an LLM-based patching baseline | . | LLMs, to examine whether these LLM-generated exemplars |
| When we remove the multi-faceted patch validation, as | are better than human curated exemplars, we also manu- |  |  |
| shown in the "no validation", we notice that the precision | ally write exemplars following the same reasoning steps. As |  |  |
| drops and thus the F1 becomes lower, with 20.41%–35.77% | shown in rows “Manual Exemplars”, the overall effectiveness |  |  |
| 4490 | 34th USENIX Security Symposium | USENIX Association |  |

---

## Page 12

drops significantly, indicating the effectiveness of adaptive

definitions, please tell the functions needed with the format {"context_funcs":

[func_1,func_2,CALLER_of_func...]} where"CALLER_of_func" is a

placeholder for the caller of the given functions.

<Code slice of function Jsi_Strcpy and SplitChar marked in Figure 1>

the vulnerability. If you encounter uncertainty …

A: Root Cause Analysis: Looking at the given vulnerable code line and its

memory location pointed to by `p`, which is calculated as `&(argv[cnt+2])`. If

vulnerability, which is CWE-787.

analysis is lower than vulnerability semantics reasoning, as

shown in Table 10. This indicates that guiding LLMs for

vulnerability semantics reasoning is effective for improving

vulnerability analysis and patching.

To show the patching effectiveness of the LLMs without

any specific prompting design, we directly ask the LLMs to

patch the given vulnerabilities. As shown in row “Standard

Prompting”, we notice that the standard prompting have much

Each component in A PPATCH substantially contributes to

its effectiveness, justifying its overall design.

Table 4: Comparison to existing techniques in terms of recall

Technique SynEq SemEq Plausible Correct SynEq SemEq Plausible Correct

A PPATCH 5% 75% 40% 90% 4.12% 37.11% 22.68% 49.48%

from 33.30% to 31.37%).

to 9.81% and 6.31%, respectively). Note that for Standard

directly provide functions with the ground-truth patch loca-

While A PPATCH has a slight performance drop on exclu-

sively interprocedural vulnerabilities, baseline approaches

show a dramatic decline. This highlights the effectiveness

merits of interprocedural analysis in A PPATCH .

5.3 RQ3: Comparison to Existing Techniques

As ExtractFix and VulnFix require compilable projects

and test cases which are difficult to build on our Zero-Day

dataset, we first use the ExtractFix dataset for comparison.

| prompting for our LLM-based vulnerability patching design. | ExtractFix Dataset | Zero-Day Dataset |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Q: Given the following code slice | VulRepair | 10% | 25% | 0% | 35% | 2.06% | 15.46% | 1.03% | 17.53% |
| <Code slice marked in Figure 1> | Getafix | 20% | 5% | 0% | 25% | 5.15% | 0.00% | 1.03% | 6.19% |
| which has a CWE-787 vulnerability at line 24, please analyze the root cause of | ExtractFix | 20% | 35% | 30% | 85% | - | - | - | - |
| the vulnerability. If you encounter uncertainty due to a lack of function | VulnFix | 20% | 10% | 15% | 45% | - | - | - | - |
| A: {"context_funcs":[CALLER_of_ | Jsi_Strcpy | ...]} | to the overall results on the complete Zero-Day dataset, |  |  |  |  |  |  |
| Q: Given the following code slice | A | PPATCH | and its ablated versions show a modest decrease in |  |  |  |  |  |  |
| which has a CWE-787 vulnerability at line 24, please analyze the root cause of | performance (e.g., A | PPATCH | ’s F1 score with GPT-4 decreases |  |  |  |  |  |  |
| context, the CWE-787 (out-of-bounds write) vulnerability exists in the code | In contrast, the baseline approaches—Standard Prompt- |  |  |  |  |  |  |  |  |
| because the `Jsi_Strcpy` function is used to copy the contents of `str` to the | ing and Zero-Shot Completion—exhibit a substantial decline |  |  |  |  |  |  |  |  |
| the value of `cnt` is such that `cnt+2` exceeds the allocated memory for `argv`, | in effectiveness (e.g., Claude-3.5 with standard prompting |  |  |  |  |  |  |  |  |
| then writing to `p` using `Jsi_Strcpy` can lead to an out-of-bounds write | and zero-shot completion decrease from 23.01% and 12.48% |  |  |  |  |  |  |  |  |
| Figure 9: Root cause analysis generated by GPT-4 | without | Prompting, we provide all the functions covered by the com- |  |  |  |  |  |  |  |
| vulnerability semantics reasoning | for the sample in Figure 1. | puted vulnerability semantics. For zero-shot completion, we |  |  |  |  |  |  |  |
| To show the effectiveness of vulnerability semantics rea- | tion as it can only work in such a setting. These already benefit |  |  |  |  |  |  |  |  |
| soning, we simply prompt the LLMs to generate root causes, | the two baselines but they still fall short with these interpro- |  |  |  |  |  |  |  |  |
| as shown in Figure 9. As shown in the row “Direct Reason- | cedural samples. This deterioration can be attributed to the |  |  |  |  |  |  |  |  |
| ing”, the overall effectiveness drops significantly compared | absence of interprocedural analysis in these approaches which |  |  |  |  |  |  |  |  |
| to A | PPATCH | . The reason is that the accuracy of root cause | adversely affects the LLMs’ performance. |  |  |  |  |  |  |
| lower effectiveness compared with A | PPATCH | , achieving only | To compare the effectiveness of A | PPATCH | to existing vulnera- |  |  |  |  |
| up to 23.01% F1 on the Zero-Day dataset and 60.42% F1 on | bility patching techniques, we select four state-of-the-art non- |  |  |  |  |  |  |  |  |
| the ExtractFix dataset even with the state-of-the-art LLMs. | LLM-based tools which cover different technical categories, |  |  |  |  |  |  |  |  |
| Recently, Pearce et al. [43] approaches the LLM-based vul- | as shown in Table 4, where the red numbers indicate the best |  |  |  |  |  |  |  |  |
| nerability repair problem through zero-shot code completion, | recall achieved by the baselines. VulRepair [18] is a DL-based |  |  |  |  |  |  |  |  |
| which removes the vulnerable code in the program and lets | vulnerability repair technique which fine-tunes a pre-trained |  |  |  |  |  |  |  |  |
| the LLMs fill the vulnerable parts so as to fix the vulnerabil- | programming language model CodeT5 [50] to repair vulnera- |  |  |  |  |  |  |  |  |
| ity. We use their best template | s2 | for comparison. As shown | bilities. Getafix [7] is a data-driven pattern-based vulnerability |  |  |  |  |  |  |
| in the Row “zero-shot completion”, this approach has the | repair technique which learns vulnerability patching patterns |  |  |  |  |  |  |  |  |
| lowest effectiveness, with up to 12.48% F1 on our Zero-Day | from existing samples. ExtractFix [20] is a traditional vul- |  |  |  |  |  |  |  |  |
| dataset and 24.66% F1 on the ExtractFix dataset, indicating | nerability patching technique which leverages test cases and |  |  |  |  |  |  |  |  |
| that only providing prior code without further information is | constraints to fix the vulnerabilities. VulnFix [55] is a SOTA |  |  |  |  |  |  |  |  |
| insufficient for LLMs to fix the vulnerabilities. | vulnerability patching technique based on inductive inference. |  |  |  |  |  |  |  |  |
| We further evaluate A | PPATCH | ’s effectiveness on interpro- | As ExtractFix and VulnFix generate many patches for test- |  |  |  |  |  |  |
| cedural vulnerabilities using the 21 interprocedural samples | ing, we only compare the recall metric in this RQ. For Vul- |  |  |  |  |  |  |  |  |
| from the Zero-Day dataset. Table 3 shows the correctness | Repair and Getafix which are learning-based, we use our |  |  |  |  |  |  |  |  |
| results (the complete results are in Appendix Table 12). Sim- | PatchDB+CVEFixes training set to re-train their models. |  |  |  |  |  |  |  |  |
| ilarly, the numbers marked in red are the best F1 scores | As shown in Table 4, on the ExtractFix dataset, A | PPATCH |  |  |  |  |  |  |  |
| achieved by the ablated prompting approaches. Compared | with the best LLM (GPT-4) achieves the best recall (90%) |  |  |  |  |  |  |  |  |
| USENIX Association | 34th USENIX Security Symposium | 4491 |  |  |  |  |  |  |  |

---

## Page 13

compared with the baseline techniques. Note that the recall

sum of syntactic equivalent, semantically equivalent, and plau-

for patching. Without such information, other baseline tech-

niques only achieve 25%-45% recall.

cutoff date of the used LLMs. Thus, we test the LLMs whether

they know the related information and patches given the meta

data. The results show that they either do not know or give

Compared to traditional techniques, A PPATCH is effective

in vulnerability patching without extra information.

A PPATCH is efficient for vulnerability patching in terms of

both time and money cost.

Table 5: Time and token cost of A PPATCH per sample

| Model | Time cost | Contexts Tokens | Generated Tokens | Price |
| --- | --- | --- | --- | --- |
| Gemini-1.5 | 37.148s | 5684 | 584 | $0.0026 |

6.1 Why A PPATCH Works

concentrate on the vulnerability semantics which is the most

important parts for patching, but also makes the data and con-

trol flow clearer than the original code. For example, in the

original code, the variable cnt at line 22 is 6 lines away from

its last definition at line 16. However, in the vulnerability

easier to find the data dependencies for vulnerability patching.

shot learning, while avoiding LLM fine-tuning which incurs

high costs of time and money. Because of the token limitation

and the disadvantage of LLMs for long-text process, it is not

feasible to input all the exemplars for few-shot learning. In

contrast, the dynamic adaptive prompting with CoT guides

lyzing them superficially. As Figures 2, 3 and 7 show, GPT-4

| sible may be over recall on correct because there are multiple | GPT-4 | 40.169s | 6290 | 647 | $0.0823 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| patches generated for each testing sample. ExtractFix achieves | Claude-3.5 | 50.209s | 6802 | 886 | $0.0336 |  |  |
| 85% recall because it leverages the test cases and constraints | Llama-3.1 | 46.598s | 5749 | 591 | $0.0203 |  |  |
| Note that the ExtractFix dataset is released in 2021, which | some samples, its tool usability, its current limitations, and |  |  |  |  |  |  |
| is possible to cause the data leakage issue as it is before the | the extensibility of A | PPATCH | . |  |  |  |  |
| wrong answers, indicating that the data leakage issue is not | There are several advantages of A | PPATCH | for vulnerability |  |  |  |  |
| serious. Detailed results can be found in Appendix E. | patching. The first advantage is contributed by the semantics- |  |  |  |  |  |  |
| We further evaluate the baselines on the Zero-Day dataset. | aware scoping. As Figure 1 shows, without semantics-aware |  |  |  |  |  |  |
| Since these samples are not compilable, we limit our com- | scoping, the code to be analyzed and patched includes many |  |  |  |  |  |  |
| parison to VulRepair and Getafix as the other two (VulnFix | statements not relevant to the vulnerabilities. In this case, |  |  |  |  |  |  |
| and ExtractFix) both require that the input code is compilable. | the LLMs are distracted and thus are more difficult to gener- |  |  |  |  |  |  |
| As shown in Table 4, A | PPATCH | significantly outperforms | ate correct root cause and patches. In comparison, resulting |  |  |  |  |
| both baselines, achieving a recall of 49.48% compared to | from our semantics-aware scoping, the slice analyzed and |  |  |  |  |  |  |
| VulRepair’s 17.53% and Getafix’s 6.19%. This highlights | patched by LLMs only includes the core code fragment for |  |  |  |  |  |  |
| A | PPATCH | ’s superior effectiveness in patching. | vulnerability analysis and patching. This not only helps LLMs |  |  |  |  |
| 5.4 | RQ4: Efficiency | semantics slice, it is only two lines away, which makes LLMs |  |  |  |  |  |
| We evaluate the efficiency of A | PPATCH | in terms of time cost | Figures 2, 3 and 7 show the generated analysis and |  |  |  |  |
| and token usage. Table 5 shows the time cost and token us- | patch by GPT-4 with standard prompting, zero-shot com- |  |  |  |  |  |  |
| age of A | PPATCH | per sample on each LLM. After mining the | pletion and A | PPATCH | , where the standard prompting and |  |  |
| exemplars, each sample takes between 37.148 seconds and | zero-shot completion fail to patch the vulnerability correctly |  |  |  |  |  |  |
| 50.209 seconds to generate a patch, including the time for se- | while A | PPATCH | succeeds. We notice that in A | PPATCH | with |  |  |
| lecting the exemplars and generating the candidate patches. In | semantics-aware scoping, GPT-4 is able to capture more data |  |  |  |  |  |  |
| this process, the input/context token usage ranges from 5,684 | flow information for variables | p | , | cnt | , and | dStr | , while the |
| to 6,802 per sample, and the generated token usage ranges | GPT-4 with standard prompting and zero-shot code comple- |  |  |  |  |  |  |
| from 584 to 886. We notice that Claude-3.5 and GPT-4 take | tion only analyze and patch the code based on the vulnerable |  |  |  |  |  |  |
| more tokens while Gemini-1.5 and Llama-3.1 take less. The | line itself. This indicates that semantics-aware scoping helps |  |  |  |  |  |  |
| reason is that the former two models tend to generate more | LLMs better work on the data dependency analysis, which is |  |  |  |  |  |  |
| tokens when generating the exemplars and patches. Based | important for effective vulnerability patching. |  |  |  |  |  |  |
| on the rate of each model’s API, patching each sample costs | The second advantage of A | PPATCH | is that it prompts dy- |  |  |  |  |
| between 0.2 and 8 cents. However, Gemini-1.5 provides a | namically based on the testing samples rather than using ran- |  |  |  |  |  |  |
| free version if the usage is not large and Llama-3.1 supports | dom or fixed prompts. This allows LLMs to leverage a large |  |  |  |  |  |  |
| deploying locally. If so, the two models are free. | amount of existing real-world vulnerability data with few- |  |  |  |  |  |  |
| 6 | Discussion | LLMs to analyze the vulnerabilities in depth rather than ana- |  |  |  |  |  |
| We further discuss the advantages of A | PPATCH | that enable | with A | PPATCH | conducts in-depth analysis for the root cause |  |  |
| its greater effectiveness, as well as why and how it fails on | of the vulnerability, while GPT-4 with standard prompting |  |  |  |  |  |  |
| 4492 | 34th USENIX Security Symposium | USENIX Association |  |  |  |  |  |

---

## Page 14

Table 6: Accuracy of CodeQL detection, localization, classifi-

cation, and the three combined against the Zero-Day dataset

Scenario Detection Localization Classification Combined

Table 7: End-to-end results against the Zero-Day dataset

| Scenario | Model | Approach | Correct |
| --- | --- | --- | --- |
| Recall | Prec | F1 |  |
| Manual Exemplars | 22.68% | 11.33% | 15.11% |

Claude-3.5

Zero-shot Completion 15.46% 9.04% 11.41%

A PPATCH 41.24% 20.40% 27.29%

Claude-3.5

Realistic Standard Prompting 24.74% 16.16% 19.55%

Zero-shot Completion 15.46% 9.04% 11.41%

VulRepair - 16.49% 9.18% 11.79%

The third advantage is that A PPATCH conducts multi-

faceted patch validation strategy to remove the unusable

patches. As shown in Table 2, with multi-facted patch valida-

tion, the precision is improved significantly without impact-

We consider two integration scenarios for a comprehensive

evaluation. The first is a fully automated workflow in which

both information from the upstream tools is directly fed to

inspected, verified, and calibrated if necessary, and the vali-

dated/calibrated location and CWE information is then fed

to A PPATCH . In a typical, realistic vulnerability management

workflow, developers would inspect and calibrate the outputs

Thus, we refer to the second as the realistic scenario.

industry-grade security analyzer widely used on real-world

projects. Also, as it serves detection/localization and classi-

veloper inspection, we had a graduate student with 3-year rele-

vant experience simulate the realistic human-intervention step

between vulnerability localization/classification and patching,

who inspected and calibrated CodeQL outputs.

performance, which is largely consistent with what earlier

studies found on CodeQL [13]. Note that CodeQL may re-

other vulnerability localization techniques [17, 22, 35]. There-

| Fully Automated | 87.62% | 59.79% | 69.07% | 55.67% | A | PPATCH | as its inputs without human intervention. The sec- |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Realistic | 87.62% | 72.16% | 83.50% | 68.04% | ond is a scenario in which the outputs of those tools are first |  |  |
| A | PPATCH | 34.02% | 18.36% | 23.85% | of automated (vulnerability localization and classification) |  |  |
| Fully Automated | Standard Prompting | 16.49% | 11.15% | 13.30% | tools before proceeding with patching using those outputs, |  |  |
| VulRepair | - | 16.49% | 9.18% | 11.79% | for many reasons (e.g., accuracy/trust issues—since no auto- |  |  |
| Getafix | - | 6.19% | 5.70% | 5.93% | mated tools are perfect and they can produce false positives |  |  |
| Manual Exemplars | 25.77% | 11.38% | 15.79% | and suffer false negatives, among other considerations [4]). |  |  |  |
| Getafix | - | 6.19% | 5.70% | 5.93% | For the upstream tooling, we chose CodeQL [1] as it is an |  |  |
| and zero-shot completion cannot. The exemplars from dy- | fication purposes at the same time, users need just one tool |  |  |  |  |  |  |
| namic adaptive prompting guide GPT-4 to find the size and | instead of multiple to provide both inputs to A | PPATCH | . For |  |  |  |  |
| boundary of the pointer | p | , which significantly helps generate | CodeQL to work specifically for a given project, users of- |  |  |  |  |
| the patch correctly. | ten customize the query packs based on the project infor- |  |  |  |  |  |  |
| Notably, the ability of LLMs to automatically generate the | mation [1]. We also followed this common practice for the |  |  |  |  |  |  |
| vulnerability semantics reasoning steps (i.e., the natural lan- | projects evaluated. Notably, our query-pack customization |  |  |  |  |  |  |
| guage representation of vulnerability semantics) is key to the | did not assume any knowledge about the ground-truth results |  |  |  |  |  |  |
| automation in Step 1.2. Also, since the reasoning essentially | (i.e., detection/localization/classification outcomes), avoid- |  |  |  |  |  |  |
| dissects the vulnerable behavior of the code, they immediately | ing biases and keeping the realism of the end-to-end integra- |  |  |  |  |  |  |
| serve as root cause analysis. Importantly, using | functional- | tion setting. We extended the memory manipulation function |  |  |  |  |  |
| ity semantics | instead would help the LLMs understand the | set in the query packs so that the project’s custom memory- |  |  |  |  |  |
| functional behaviors of the code, hence not helping much the | management APIs (e.g., | kmalloc | , | kfree | ) can be scanned as |  |  |
| models with understanding the vulnerability root cause hence | well—which any ordinary user would be able to do as well for |  |  |  |  |  |  |
| guiding their patch generation, as we extensively validated. | a given project to scan. For the realistic scenario involving de- |  |  |  |  |  |  |
| ing the recall. This improves the F1 and effectively reduces | A | PPATCH | ’s end-to-end performance results in both scenar- |  |  |  |  |
| the load of developers for selecting appropriate patches, thus | ios are in Table 7 (with further details in Appendix Table 13). |  |  |  |  |  |  |
| shows the practicability of A | PPATCH | . | To contextualize these results, Table 6 gives the upstream tool |  |  |  |  |
| 6.2 | Usability of A | PPATCH | port multiple locations and CWEs for one sample, similar to |  |  |  |  |
| In this work, we assume that the vulnerabilities under patch- | fore, we follow their evaluation approach and report top-10 |  |  |  |  |  |  |
| ing are pre-detected with correct CWE and location infor- | accuracy for localization and classification where the ranking |  |  |  |  |  |  |
| mation. However, such information may not be always avail- | is based on the security severity [6]. As shown, A | PPATCH |  |  |  |  |  |
| able. In this case, A | PPATCH | may need to collaborate with | worked reasonably well in these end-to-end settings, with |  |  |  |  |
| other vulnerability analyzers (that provide the information) to | expected accuracy drops versus when perfect vulnerability |  |  |  |  |  |  |
| work in practice. Thus, to demonstrate that our formulation of | location and CWE information is used (Table 2). These gaps |  |  |  |  |  |  |
| A | PPATCH | is | realistic | and showcase its usability, we evaluate | can be justified by inaccuracies of the upstream results with- |  |  |
| its performance when fed with such information produced | /without human inspection. A | PPATCH | also outperforms the |  |  |  |  |
| from upstream detection/localization and classification tools, | baseline approaches, demonstrating its merits and superior |  |  |  |  |  |  |
| a setting referred to as | end-to-end | integration, against our | practical performance. With more advanced upstream tools |  |  |  |  |
| Zero-Day dataset on the best-performing LLM Claude-3.5. | to provide more accurate vulnerability locations and CWEs, |  |  |  |  |  |  |
| USENIX Association | 34th USENIX Security Symposium | 4493 |  |  |  |  |  |

---

## Page 15

and users with more expertise (e.g., developers of the project For the first limitation, A PPATCH mitigates it by using

under patching), these performance could be even better. the state-of-the-art and most powerful LLMs to generate the

6.3 How and Why A PPATCH Fails

• Incorrect Vulnerability Identification. The most com-

• Insufficient or incorrect code modification. Another com-

mon issue was insufficient or incorrect code modification

(31.23% of symptoms). For example, as shown in Figure 11,

the patch focuses on local buffer handling while the actual

fix require dynamic memory allocation and more compre-

hensive input validation.

These symptoms show how A PPATCH fails to patch some

samples. We further identified three main root causes:

• Misunderstanding the actual vulnerabilities. The most

common root cause for failed patching is that the LLMs

misunderstand the actual vulnerabilities, with 41.33% of

the root causes. This usually causes incorrect vulnerability

identification, as shown in Figure 10.

6.4 Limitations

There are several factors that may limit A PPATCH in practice.

patches. We exclude the LLMs that are not capable of con-

ducting logical analysis, such as Falcon [58], StarCoder [29],

and GPT-NeoX [11]. All the selected LLMs in this work have

patching strategies/patterns.

producing the vulnerabilities based on the CVE reports is very

time-consuming, it is difficult for us to build a dataset with

hundreds of compilable and vulnerability-reproducable code

samples in a short time. At the same time, existing vulnera-

bility datasets coming with compilable code and test cases

are relatively small, such as the ExtractFix dataset [20] which

only has 30 samples. Therefore, future works should try to

build larger compilable vulnerability datasets so that rigorous

static and dynamic analysis can be feasible.

6.5 Extensibility

A common concern for the practicability of A PPATCH is

whether it can be extended to other CWEs and languages.

as Java, Python, C#, and Go.

6.6 LLMs for Automated Patching

| We conduct case studies on the all the failure cases of | the capability of analyzing the code logically. For the second |  |  |
| --- | --- | --- | --- |
| A | PPATCH | on the Zero-Day dataset to investigate the symp- | limitation, we collected as many as samples as we can so that |
| toms of them. There are several major symptom groups. | they can cover more CWEs, vulnerable code patterns, and |  |  |
| mon symptom is incorrect vulnerability identification, with | Indeed, the two limitations can be attributed to the vul- |  |  |
| 35.69% of the symptoms. This category includes cases | nerability datasets we use. In an ideal vulnerability patching |  |  |
| where the initial analysis misidentified the type or nature | scenario, the exploits should be provided and the dynamic |  |  |
| of the vulnerability. For example, as shown in Figure 10 | tracing of the vulnerability should be available. However, |  |  |
| the actual issue is related to a missing condition check for | the used datasets, PatchDB and CVEFixes, only provide the |  |  |
| the debug event code type, not an out-of-bounds write as | raw information of the vulnerabilities (e.g., versions, patches, |  |  |
| initially assumed. | source code) without further information. Considering that re- |  |  |
| • | Inadequate analysis of code context and dependencies. | While the current implementation and the evaluation are |  |
| Another common root cause for failed patching is inade- | based on C language with six common CWEs, the design |  |  |
| quate analysis of code context and dependencies (25.21% | of A | PPATCH | is language/CWE agnostic and is extendable |
| of root causes). This usually causes insufficient or incorrect | to other CWEs and languages. To extend A | PPATCH | to other |
| code modification, as shown in Figure 11. | CWEs, users can add exemplar samples of other CWEs to gen- |  |  |
| • | Failure to consider all edge cases or scenarios. | This cate- | erate the respective exemplars. The samples with more CWEs |
| gory covers situations where the patch didn’t account for | can be also found in the PatchDB and CVEFixes datasets. |  |  |
| all possible scenarios or edge cases, with 10.21% of the | To extend A | PPATCH | to other languages, users can set up a |
| root causes. For example, in one sample, the LLM incor- | code analyzer that is able to construct SDGs and then fol- |  |  |
| rectly handles special characters in shell quoting and fails to | low Algorithm 1 to extract the vulnerability semantics slices. |  |  |
| address all cases of characters requiring special treatment, | Meanwhile, our used code analyzer, Joern, also supports more |  |  |
| particularly those needing quoting rather than escaping. | than ten languages, including the most popular languages such |  |  |
| The first limitation is that the root cause analysis may not be | Beyond the merits of A | PPATCH | itself, our work also reveals |
| accurate at the testing phase. If the vulnerability root cause | several insights for future automated patching with LLMs. |  |  |
| analysis is incorrect, the direction of patching is misled and | The first is that prompting design matters for effective vul- |  |  |
| the generated patches are less likely to be correct. The sec- | nerability patching. Based on our evaluation, simply asking |  |  |
| ond limitation is that we only collect 306+76+20 patching | LLMs to patch vulnerabilities work poorly because of the lack |  |  |
| samples for evaluation, because collecting these samples re- | of guidance. While vulnerability patching by the SOTA ap- |  |  |
| quire manual works to label. Yet we still cannot ensure these | proach [43] shows its potential when LLMs started surging, it |  |  |
| samples are compilable and come with test cases. | performs poorly even with the latest and most powerful LLMs. |  |  |
| 4494 | 34th USENIX Security Symposium | USENIX Association |  |

---

## Page 16

| This indicates that the prompts for vulnerability patching need | program vulnerability repair. Lastly, Pearce et al. [43] exam- |
| --- | --- |
| to be specifically designed with comprehensive guidance. | ined the application of LLM for zero-shot vulnerability repair. |
| The second insight is that LLM-based vulnerability patch- | Their study highlights the potential of LLMs to fix vulnerabil- |
| ing still needs traditional code analysis to complement. The | ities without extensive task-specific training, leveraging the |
| main reason is that LLMs usually have token limitation so that | models’ ability to generalize from a vast amount of data. |

we cannot input a large amount of code into the model. Even

if some of the models support more tokens, the long input and

output text may also distract the model from concentrating the

The third insight is that dynamically prompting LLMs adap-

tively is necessary for few-shot learning-based vulnerability

patching. The reason is that, because of the token limitation of

LLMs, it is difficult to input all the samples covering different

vulnerability root causes and patching strategies. The exem-

plars used for few-shot learning should be based on testing

GPT-3.5) and the price is expensive considering the amount

of data for fine-tuning. Therefore, prompting LLMs would be

more feasible than pre-training and fine-tuning.

8 Conclusion

have demonstrated, on four latest LLMs, that A PPATCH sub-

stantially outperforms both existing prompting approaches

and state-of-the-art non-LLM-based patching techniques.

Acknowledgments

Ethics Considerations

Our research is focused on the development and evaluation

of methods for patching software vulnerabilities, which com-

Security’25 conference. Specifically, we have ensured that

| important parts for patching because of the limitation of their | We propose A | PPATCH | , an automated vulnerability patch- |
| --- | --- | --- | --- |
| base structure-Transformer [48]. Therefore, extracting the im- | ing framework that features dynamic adaptive prompting |  |  |
| portant code slices by traditional code analysis techniques is | on LLMs to elicit their effective reasoning for vulnerabil- |  |  |
| promising for LLM-based vulnerability patching. | ity root-cause analysis hence quality patch generation. We |  |  |
| samples to achieve better effectiveness. | We thank our shepherd and the anonymous reviewers for their |  |  |
| Meanwhile, we choose to use LLMs as they are, without | effective guidance and constructive comments. For this work, |  |  |
| pre-training and fine-tuning. The main reason is that the cost | Yu Nong, Haoran Yang, and Haipeng Cai were supported |  |  |
| of LLMs also matters. If we choose to pre-train our own | by Army Research Office (ARO) under Grant No. W911NF- |  |  |
| LLMs, the training data, hardware usage, and time cost would | 21-1-002, National Science Foundation (NSF) under Grant |  |  |
| be considerable. Only big companies such as OpenAI and | No. CCF-2146233 and CCF-2505223, and Office of Naval |  |  |
| Google have enough resource to pre-train LLMs. Currently, | Research (ONR) under Grant No. N000142212111; Long |  |  |
| most of the powerful LLMs are commercial, thus it is difficult | Cheng was supported by NSF under Grant No. 2239605 and |  |  |
| to access these LLMs directly for fine-tuning. Although some | 2228616; and Hongxin Hu was supported by NSF under Grant |  |  |
| provide APIs for fine-tuning, the models are usually old (e.g., | No. 2228617, 2120369, and 2129164. |  |  |
| 7 | Related Work | plies with the ethical guidelines outlined by the USENIX |  |
| Recent research has focused on example-based approaches | our study adheres to principles concerning the responsible |  |  |
| to vulnerability detection and repair, demonstrating the ef- | handling of security research. |  |  |
| fectiveness of learning from past vulnerabilities and their | Our study focuses on generating and testing patches for |  |  |
| corresponding fixes. Ma et al. [34] presented VuRLE, a sys- | vulnerabilities in software systems. While we evaluate our |  |  |
| tem that utilizes machine learning to automatically detect and | technique mainly in a zero-day setting (i.e., using the vulner- |  |  |
| repair vulnerabilities by learning from examples. Similarly, | abilities that are zero-days to the LLMs which have a cutoff |  |  |
| Zhang et al. [54] developed a similar approach for Java. | date before the disclosure time of these vulnerabilities), the |  |  |
| Deep learning techniques have also shown significant | vulnerabilities have already been disclosed (as CVEs) publicly |  |  |
| promise in automating the vulnerability detection and repair | by the time of our paper writing. Thus, our research itself does |  |  |
| process. Chen et al. [14] explored neural transfer learning for | not cause harm or risks related to vulnerability disclosure, nor |  |  |
| repairing vulnerabilities in C code. VulRepair, a T5-based | raising any new security threats. Nevertheless, throughout our |  |  |
| automated software vulnerability repair tool, is presented by | research process, we have taken care to avoid any actions that |  |  |
| Fu et al. [18]. This approach shows significant improvements | could result in unintended harm, such as exposing systems |  |  |
| in the accuracy and efficiency of vulnerability repair. | or users to new security risks. We have ensured that all vul- |  |  |
| Program analysis and language models offer powerful tech- | nerability data utilized is anonymized and does not contain |  |  |
| niques for understanding and fixing software vulnerabilities | any identifiable information about individuals or organiza- |  |  |
| by analyzing code semantics and employing complicated mod- | tions. Besides, we have not conducted any experiments on |  |  |
| els. Gao et al. [20] proposed a novel method that goes beyond | production systems that could impact real-world users, hence |  |  |
| conventional testing by extracting crash constraints to guide | avoiding any potential disruption or harm. |  |  |
| USENIX Association | 34th USENIX Security Symposium | 4495 |  |

---

## Page 17

Open Science [13] Wachiraphan Charoenwet, Patanamon Thongtanunam, Van-

Security’25, which requires research results to be publicly ac-

the codebase, datasets, and experimental results, through a

been made available at https://zenodo.org/records/14741018.

In summary, our work aligns with both the ethical guide-

community engagement in advancing cybersecurity research.

References

[1] CodeQL documentation. https://codeql . github . com/

docs/ , 2021.

[2] Introducing Code Llama, A state-of-the-art large language

model for coding. https://ai . meta . com/blog/code-

llama-large-language-model-coding/ , 2023.

blog/codeqwen1 . 5/ , 2024.

[6] Metadata for CodeQL queries. https://

[7] Johannes Bader, Andrew Scott, Michael Pradel, and Satish

[8] Árpád Beszédes, Csaba Faragó, Z Mihaly Szabo, János Csirik,

[9] Guru Bhandari, Amara Naseer, and Leon Moonen. CVEfixes:

[10] David Binkley, Nicolas Gold, and Mark Harman. An empirical

[11] Sidney Black, Stella Biderman, Eric Hallahan, Quentin An-

thony, Leo Gao, Laurence Golding, Horace He, Connor Leahy,

Kyle McDonell, Jason Phang, et al. GPT-NeoX-20B: An open-

[12] Haipeng Cai, Yu Nong, Yuzhe Ou, and Feng Chen. Generating

Springer, 2023.

Thuan Pham, and Christoph Treude. An empirical study of

691–703, 2024.

| [15] Ericsson. | Software | vulnerability: | Impact | & | ways |
| --- | --- | --- | --- | --- | --- |
| [16] Forbes | Technology | Council. | Zero-day | vulnerabili- |  |
| ties: | 17 | consequences | and | complications. | https: |

[17] Michael Fu and Chakkrit Tantithamthavorn. LineVul: A

Transformer-based line-level vulnerability prediction. In MSR ,

pages 608–620, 2022.

[18] Michael Fu, Chakkrit Tantithamthavorn, Trung Le, Van

Nguyen, and Dinh Phung. VulRepair: A T5-based automated

software vulnerability repair. In ESEC/FSE , pages 935–947,

2022.

[19] Xiaoqin Fu and Haipeng Cai. FlowDist: Multi-staged

refinement-based dynamic information flow analysis for dis-

pages 2093–2110, 2021.

2021.

1865–1879, 2023.

neural networks. In MSR , pages 596–607, 2022.

1990.

pages 539–554, 2019.

drea De Lucia, and Fabio Palomba. The secret life of software

vulnerabilities: A large-scale empirical study. TSE , 49(1):44–

63, 2022.

why-observability-is-the-solution , 2023.

nvd-dashboard , 2023.

| We fully support the new open science policy of USENIX | static analysis tools for secure code review. In | ISSTA | , pages |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cessible or for researchers to provide a valid explanation if this | [14] Zimin Chen, Steve Kommrusch, and Martin Monperrus. Neural |  |  |  |  |  |  |  |  |
| is not possible. To align with this policy, we commit to openly | transfer learning for repairing security vulnerabilities in C code. |  |  |  |  |  |  |  |  |
| sharing all artifacts generated from our research, including | TSE | , 49(1):147–165, 2022. |  |  |  |  |  |  |  |
| publicly accessible repository. The source code and documen- | to avoid it. | https://www | . | ericsson | . | com/en/security/ |  |  |  |
| tation of A | PPATCH | as well as our experimental results have | vulnerability-management | , 2023. |  |  |  |  |  |
| lines and open science policy of USENIX Security’25. We | //www | . | forbes | . | com/councils/forbestechcouncil/2023/ |  |  |  |  |
| are committed to conducting research that not only adheres | 05/26/zero-day-vulnerabilities-17-consequences- |  |  |  |  |  |  |  |  |
| to high ethical standards but also promotes openness and | and-complications | , 2023. |  |  |  |  |  |  |  |
| [3] Code with CodeQwen1.5. | https://qwenlm | . | github | . | io/ | tributed software systems. In | USENIX Security Symposium | , |  |
| [4] A fool with a tool is still a fool. | https://dwheeler | . | com/ | [20] Xiang Gao, Bo Wang, Gregory J Duck, Ruyi Ji, Yingfei Xiong, |  |  |  |  |  |
| flawfinder/ | , 2024. | and Abhik Roychoudhury. Beyond tests: Program vulnerability |  |  |  |  |  |  |  |
| [5] Meet claude. | https://www | . | anthropic | . | com/claude | , 2024. | repair via crash constraint extraction. | TOSEM | , 30(2):1–27, |
| codeql | . | github | . | com/docs/writing-codeql-queries/ | [21] Jingxuan He and Martin Vechev. Large language models for |  |  |  |  |
| metadata-for-codeql-queries/ | , 2024. | code: Security hardening and adversarial testing. In | CCS | , pages |  |  |  |  |  |
| Chandra. Getafix: Learning to fix bugs automatically. | OOP- | [22] David Hin, Andrey Kan, Huaming Chen, and M Ali Babar. |  |  |  |  |  |  |  |
| SLA | , 3:1–27, 2019. | LineVD: Statement-level vulnerability detection using graph |  |  |  |  |  |  |  |
| and Tibor Gyimóthy. Union slices for program maintenance. | [23] Susan Horwitz, Thomas Reps, and David Binkley. Interproce- |  |  |  |  |  |  |  |  |
| In | ICSM | , pages 12–21, 2002. | dural slicing using dependence graphs. | TOPLAS | , 12(1):26–60, |  |  |  |  |
| Automated collection of vulnerabilities and their fixes from | [24] Zhen Huang, David Lie, Gang Tan, and Trent Jaeger. Using |  |  |  |  |  |  |  |  |
| open-source software. In | PROMISE | , pages 30–39, 2021. | safety properties to generate vulnerability patches. In | S&P | , |  |  |  |  |
| study of static program slice size. | TOSEM | , 16(2):8–es, 2007. | [25] Emanuele Iannone, Roberta Guadagni, Filomena Ferrucci, An- |  |  |  |  |  |  |
| source autoregressive language model. In | Proceedings of Big- | [26] Ilan Peleg. The high cost of security vulnerabilities. | https:// |  |  |  |  |  |  |
| Science Episode# 5–Workshop on Challenges & Perspectives | www | . | forbes | . | com/sites/forbesbusinesscouncil/2023/ |  |  |  |  |
| in Creating Large Language Models | , pages 95–136, 2022. | 04/10/the-high-cost-of-security-vulnerabilities- |  |  |  |  |  |  |  |
| vulnerable code via learning-based program transformations. | [27] Information Technology Laboratory at NIST. National vulnera- |  |  |  |  |  |  |  |  |
| In | AI Embedded Assurance for Cyber Systems | , pages 123–138. | bility database dashboard. | https://nvd | . | nist | . | gov/general/ |  |
| 4496 | 34th USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |

---

## Page 18

| [28] Haonan Li, Yu Hao, Yizhuo Zhai, and Zhiyun Qian. Enhancing | [43] Hammond Pearce, Benjamin Tan, Baleegh Ahmad, Ramesh |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| static analysis for practical bug detection: An LLM-integrated | Karri, and Brendan Dolan-Gavitt. Examining zero-shot vul- |  |  |  |  |
| approach. | OOPSLA | , 8:474–499, 2024. | nerability repair with large language models. In | S&P | , pages |

[29] Raymond Li, Yangtian Zi, Niklas Muennighoff, Denis Ko-

[31] Wen Li, Jinyang Ruan, Guangbei Yi, Long Cheng, Xiapu Luo,

and Haipeng Cai. PolyFuzz: Holistic greybox fuzzing of multi-

[32] Wen Li, Haoran Yang, Xiapu Luo, Long Cheng, and Haipeng

Cai. PyRTFuzz: Detecting bugs in python runtimes via two-

level collaborative fuzzing. In CCS , pages 1645–1659, 2023.

[33] Zhen Li, Deqing Zou, Shouhuai Xu, Hai Jin, Yawei Zhu, and

Zhaoxuan Chen. SySeVR: A framework for using deep learn-

ing to detect software vulnerabilities. TDSC , 19(4):2244–2258,

2021.

[34] Siqi Ma, Ferdian Thung, David Lo, Cong Sun, and Robert H

Deng. Vurle: Automatic vulnerability detection and repair by

learning from examples. In ESORICS , pages 229–246, 2017.

[35] Yisroel Mirsky, George Macon, Michael Brown, Carter Yage-

mann, Matthew Pruett, Evan Downing, Sukarno Mertoguno,

and Wenke Lee. VulChecker: Graph-based vulnerability local-

ization in source code. In USENIX Security , pages 6557–6574,

[36] David Noever. Can large language models find and fix vulner-

able software? arXiv preprint arXiv:2308.10345 , 2023.

[37] Yu Nong, Mohammed Aldeen, Long Cheng, Hongxin Hu, Feng

Chen, and Haipeng Cai. Chain-of-thought prompting of large

language models for discovering and fixing software vulnera-

bilities. arXiv preprint arXiv:2402.17230 , 2024.

[38] Yu Nong, Richard Fang, Guangbei Yi, Kunsong Zhao, Xiapu

Luo, Feng Chen, and Haipeng Cai. VGX: Large-scale sample

generation for boosting learning-based software vulnerability

analyses. In ICSE , pages 1–13, 2024.

[39] Yu Nong, Yuzhe Ou, Michael Pradel, Feng Chen, and Haipeng

Cai. Generating realistic vulnerabilities via neural code editing:

An empirical study. In ESEC/FSE , pages 1097–1109, 2022.

[40] Yu Nong, Yuzhe Ou, Michael Pradel, Feng Chen, and Haipeng

Cai. VulGen: Realistic vulnerable sample generation via pat-

tern mining and deep learning. In ICSE , pages 2527–2539,

2023.

[41] Yu Nong, Rainy Sharma, Abdelwahab Hamou-Lhadj, Xiapu

Luo, and Haipeng Cai. Open science in software engineering:

A study on deep learning-based vulnerability detection. TSE ,

[42] Yu Nong, Haoran Yang, Long Cheng, Hongxin Hu, and

Haipeng Cai. Automated software vulnerability patching us-

2339–2356, 2023.

ily of highly capable multimodal models. arXiv preprint

arXiv:2312.11805 , 2023.

Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2:

Open foundation and fine-tuned chat models. arXiv preprint

arXiv:2307.09288 , 2023.

[47] Saad Ullah, Mingji Han, Saurabh Pujar, Hammond Pearce,

Ayse Coskun, and Gianluca Stringhini. LLMs cannot reliably

identify and reason about security vulnerabilities (yet?): A

comprehensive evaluation, framework, and benchmarks. In

S&P , pages 199–199, 2024.

[48] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszko-

reit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia

Polosukhin. Attention is all you need. NeurIPS , 30, 2017.

[49] Xinda Wang, Shu Wang, Pengbin Feng, Kun Sun, and Sushil

Jajodia. PatchDB: A large-scale security patch dataset. In

DSN , pages 149–160, 2021.

CodeT5: Identifier-aware unified pre-trained encoder-decoder

models for code understanding and generation. In EMNLP ,

pages 8696–8708, 2021.

[51] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma,

Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-

thought prompting elicits reasoning in large language models.

NeurIPS , 35:24824–24837, 2022.

[52] Yi Wu, Nan Jiang, Hung Viet Pham, Thibaud Lutellier, Jordan

Davis, Lin Tan, Petr Babkin, and Sameena Shah. How effective

are neural networks for fixing security vulnerabilities. In ISSTA ,

pages 1282–1294, 2023.

[53] Fabian Yamaguchi. A platform for robust analysis of

C/C++ code. https://joern . readthedocs . io/en/latest/

installation . html , 2022.

[54] Ying Zhang, Ya Xiao, Md Mahir Asef Kabir, Danfeng Yao, and

Na Meng. Example-based vulnerability detection and repair in

Java code. In ICPC , pages 190–201, 2022.

[55] Yuntong Zhang, Xiang Gao, Gregory J Duck, and Abhik Roy-

choudhury. Program vulnerability repair via inductive infer-

ence. In ISSTA , pages 691–702, 2022.

guage model for vulnerability detection and repair: Literature

review and roadmap. TOSEM , 2024.

| cetkov, Chenghao Mou, Marc Marone, Christopher Akiki, | [44] Moumita Das Purba, Arpita Ghosh, Benjamin J Radford, and |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| LI Jia, Jenny Chim, Qian Liu, et al. StarCoder: May the source | Bill Chu. Software vulnerability detection using large language |  |  |  |  |
| be with you! | TMLR | . | models. In | ISSREW | , pages 112–119, 2023. |
| [30] Wen Li, Jiang Ming, Xiapu Luo, and Haipeng Cai. | Poly- | [45] Gemini Team, Rohan Anil, Sebastian Borgeaud, Yonghui Wu, |  |  |  |
| Cruise: A cross-language dynamic information flow analysis. | Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalk- |  |  |  |  |
| In | USENIX Security Symposium | , pages 2513–2530, 2022. | wyk, Andrew M Dai, Anja Hauth, et al. | Gemini: A fam- |  |
| language systems. | In | USENIX Security Symposium | , pages | [46] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Am- |  |
| 1379–1396, 2023. | jad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya |  |  |  |  |
| 2023. | [50] Yue Wang, Weishi Wang, Shafiq Joty, and Steven CH Hoi. |  |  |  |  |
| 49(4):1983–2005, 2022. | [56] Xin Zhou, Sicong Cao, Xiaobing Sun, and David Lo. Large lan- |  |  |  |  |
| ing large language models. | arXiv preprint arXiv:2408.13597 | , | [57] Qihao Zhu, Daya Guo, Zhihong Shao, Dejian Yang, Peiyi |  |  |
| 2024. | Wang, Runxin Xu, Y Wu, Yukun Li, Huazuo Gao, Shirong |  |  |  |  |
| USENIX Association | 34th USENIX Security Symposium | 4497 |  |  |  |

---

## Page 19

Ma, et al. DeepSeek-Coder-V2: Breaking the barrier of E Data Leakage Assessment

closed-source models in code intelligence. arXiv preprint

[58] Yoshua X ZXhang, Yann M Haxo, and Ying X Mat. Falcon

LLM: A new frontier in natural language processing. AC

Investment Research Journal , 220(44), 2023.

Appendices

Table 8 shows the composition and statistics of the two

datasets. The Zero-Day dataset covers 18 projects and six

CWEs where the average number of patched lines is 7.87.

The ExtractFix dataset covers seven projects with the same

CWEs, while the average number of patched lines is 3.05.

els (GPT-4, Gemini-1.5, Claude-3.5, and Llama-3.1) on the

Across all models, A PPATCH ’s Vulnerability Semantics Rea-

soning approach (highlighted in green) consistently achieves

the highest correct reasoning rates. The Direct Reasoning

and No Slicing approaches generally yielded lower success

Semantics Reasoning method.

LLM queries:

1. Please tell the Project, CWE-ID, and CVE description

of <CVE-ID>.

2. Please tell the CWE-ID and CVE description of <CVE-

ID> in <Project>.

3. Please tell the patch of <CVE-ID> which has a <CWE-

The results are shown in Table 11. As shown, the LLMs either

do not know the answers or provide incorrect answers in most

of the cases. This indicates that the data leakage issue is not

serious. However, LLMs are largely a black box as we used

them in A PPATCH , making accurate data leakage assessment

very challenging. Thus, we acknowledge that, despite our ef-

fort trying to assess the data leakage issues with this dataset,

that our quantification of the leakage is perfectly accurate.

gram samples for which these five pieces of information are

provided): (1) CVE ID , (2) project name , (3) CVE description ,

that assess whether an LLM has one or more pieces of such

(2), (3), and (4);

• Query 2 : we provide the LLM with (1) and (2), and ask

it about (3) and (4);

ask it about (5).

As seen, with these three queries sent to the LLM in order

creasingly more pieces of information, and check if the LLM

| arXiv:2406.11931 | , 2024. | We checked ExtractFix dataset against leakage with following |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| A | Compostion and Statistics of the Datasets | ID> vulnerability in <Project>. |  |  |  |  |
| B | Code LLMs against the Zero-Day Dataset | we can not ensure that there was no leakage, nor can we claim |  |  |  |  |
| Table 9 shows A | PPATCH | effectiveness on code LLMs against | Instead, we took our best effort to assess the leakage, using |  |  |  |
| the Zero-Day dataset. For each of the models, we use its most | the queries designed above, as justified as follows. First, we |  |  |  |  |  |
| powerful version (with most #paramters)–CodeLlama-70b, | consider that there are five important pieces of the knowledge |  |  |  |  |  |
| CodeQwen-1.5-7b, and DeepSeek-Coder-V2-236b. As shown, | about how a vulnerability is patched (i.e., the knowledge we |  |  |  |  |  |
| the three popular used code LLMs only achieve up to 10.12% | are concerned that LLM may already have, when we evaluate |  |  |  |  |  |
| F1 score, much lower than the general-purpose LLMs. | A | PPATCH | using the ExtractFix dataset which consists of pro- |  |  |  |
| C | Correct Reasoning Rate Comparison | (4) | CWE ID | , and (5) | the patch | . Then, we design three queries |
| Table 10 compares the performance of four language mod- | knowledge when given the other pieces. More specifically: |  |  |  |  |  |
| Zero-Day dataset using three different prompting approaches. | • | Query 1 | : we provide the LLM with (1) and ask it about |  |  |  |
| rates, demonstrating the effectiveness of the Vulnerability | • | Query 3 | : we provide the LLM with (1), (2), and (4), and |  |  |  |
| D | More Results on Interprocedural Samples | of Queries 1, 2, 3, we gradually provide the LLM with in- |  |  |  |  |
| Table 12 shows the detailed results of A | PPATCH | against the | knows about the rest. This helps us check the LLM against the |  |  |  |
| interprocedural samples from the Zero-Day dataest, with red | data leakage with varying levels of difficulty, and put together |  |  |  |  |  |
| numbers indicating the best F1 scores achieved by the ab- | we believe the LLM’s responses can give us a perspective into |  |  |  |  |  |
| lated prompting approaches out of A | PPATCH | . As shown, | the data leakage issue. Nevertheless, we could not make bold |  |  |  |
| Claude-3.5 and GPT-4 achieve the best F1 scores (33.57% and | claims that these queries are the best to assess data leakage |  |  |  |  |  |
| 31.37%) with A | PPATCH | , outperforming the ablated versions. | about vulnerability patches in general. Moreover, we would |  |  |  |
| Specifically, Standard Prompting and Zero-shot Completion | like to note the following points: (1) as a comparison, we |  |  |  |  |  |
| have the worst performance (1.79%-9.81% and 0.00%-8.39% | also test the LLMs with a well-known vulnerability CVE- |  |  |  |  |  |
| respectively), showing the effectiveness of A | PPATCH | on the | 2021-44228 using the same three queries. The LLMs did |  |  |  |
| interprocedural samples. | successfully answer some of five pieces of information about |  |  |  |  |  |
| 4498 | 34th USENIX Security Symposium | USENIX Association |  |  |  |  |

---

## Page 20

Table 8: Composition and statistics of the datasets

Dataset Project-distribution (project:#CVEs) CWE-distribution(CWE:#CVEs) Complexity

linux:73, git:2, ffmpeg:1, less:1, jasper:2, FreeRDP:3, pytorch:1, Fast-DDS:1, CWE787:17, CWE125:23, CWE190:11, average #patched lines:7.87

Zero-Day esp-idf:1, openssl:1, suricata:1, RedisBloom:1, tcpdump:1, sngrep:1 CWE401:11, CWE457:10, CWE476:25

jerryscript:2, mynewt-nimble:1, dcmtk:3, libhtp:1

Table 9: Code LLMs with A PPATCH

SynEq SemEq

Table 10: Correct reasoning rate on the Zero-Day dataset

| Model | Prompt | Correct Rate |
| --- | --- | --- |
| Vulnerability Semantics Reasoning | 82.64% |  |
| GPT-4 | Direct Reasoning | 73.12% |
| No slicing | 79.41% |  |
| Vulnerability Semantics Reasoning | 63.41% |  |
| Gemini-1.5 | Direct Reasoning | 59.62% |
| No Slicing | 51.97% |  |
| Vulnerability Semantics Reasoning | 82.64% |  |
| No Slicing | 79.41% |  |
| Vulnerability Semantics Reasoning | 69.94% |  |

this CVE correctly, indicating that our queries are helpful to

test the data leakage. (2) note that A PPATCH ’s performance

with two additional state-of-the-art baselines (ExtractFix [20]

with the format “model-does-not-know%, incorrect-answer%,

correct-answer%”

| Query | GPT-4 | Gemini-1.5 | Claude-3.5 | Llama-3.1 |
| --- | --- | --- | --- | --- |
| 1 | 100%, 0%, 0% | 0%, 100%, 0% | 10%, 90%, 0% | 25%, 70%, 5% |

CWE-787:6, CWE-125:7, CWE-190:5, average #patched lines:3.05

against the Zero-Day dataset

Plausible Correct

G More Details on Case Study Examples

1 static void event_interrupt_wq_v10(struct kfd_node *dev,

| 2 | const uint32_t *ih_ring_entry) |
| --- | --- |
| 4 | uint16_t source_id, client_id, pasid, vmid; |
| 8 | source_id = SOC15_SOURCE_ID_FROM_IH_ENTRY(ih_ring_entry); |
| 9 | client_id = SOC15_CLIENT_ID_FROM_IH_ENTRY(ih_ring_entry); |
| 15 | if (client_id == SOC15_IH_CLIENTID_GRBM_CP \|\| |
| 20 | if (source_id == SOC15_INTSRC_CP_END_OF_PIPE) |
| 22 | else if (source_id == SOC15_INTSRC_SQ_INTERRUPT_MSG) { |
| 95 | } else if (source_id == SOC15_INTSRC_CP_BAD_OPCODE) { |

(Out-of-bound write) vulnerability. ### Step-by-Step Analysis: ......

### Identifying the Vulnerability: - **Potential Misinterpretation or Misuse of `source_id`**:

- **Out-of-Bounds Write Concern**:

to a memory location outside the intended data structure. This could happen if: - The specific mention of CWE-787 suggests an out-of-bounds write, which typically involves writing data

in the snippet. - The value of `source_id` is used to index or modify other data structures or arrays in a way not shown

incorrect parsing or unexpected input. - There is an implicit assumption about the range or validity of `source_id` that is violated due to

### Conclusion: The vulnerability likely stems from either an incorrect parsing of `ih_ring_entry` leading to an invalid `source_id`, or subsequent use of `source_id` in a manner that assumes it is within certain bounds which it might exceed. To resolve this, one would need to:

- Ensure `SOC15_SOURCE_ID_FROM_IH_ENTRY` correctly validates the input size and indices. - Add checks to ensure `source_id` falls within expected ranges before using it to access or modify other data structures.

```diff ### Patch 1: Validate `ih_ring_entry` Size

+5 +6 if (!ih_ring_entry || ih_ring_entry_size < EXPECTED_SIZE) { uint16_t source_id, client_id, pasid, vmid;

+7

8 +8 source_id = SOC15_SOURCE_ID_FROM_IH_ENTRY(ih_ring_entry);

Ground truth patch: ``` 95c95,96 <

> > } else if (source_id == SOC15_INTSRC_CP_BAD_OPCODE && KFD_DBG_EC_TYPE_IS_PACKET(KFD_DEBUG_CP_BAD_OP_ECODE(context_id0))) {

```

identified.

We conduct case studies on the A PPATCH ’s failure cases

and root causes.

Figure 10 shows an example where the failed patching

attempt indicates that the original vulnerability was not accu-

diagnosed as an out-of-bounds write (CWE-787) related to

| ExtractFix | coreutils:2, libjpeg:4, libxml2:2, jasper:1, libtiff:8, binutils-gdb:2, FFmpeg:1 | CWE-401:0, CWE-457:1, CWE-476:1 |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | Recall | Prec | F1 | Recall | Prec | F1 | Recall | Prec | F1 | Recall | Prec | F1 |
| CodeLlama | 0.00% | 0.00% | 0.00% | 1.03% | 0.42% | 0.60% | 1.03% | 0.43% | 0.60% | 2.06% | 0.85% | 1.20% |
| CodeQwen-1.5 | 0.00% | 0.00% | 0.00% | 4.12% | 2.03% | 2.72% | 15.46% | 4.93% | 7.47% | 18.55% | 6.95% | 10.12% |
| DeepSeek-Coder-V2 | 2.06% | 0.68% | 1.02% | 9.28% | 3.73% | 5.32% | 6.19% | 2.03% | 3.06% | 15.46% | 6.44% | 9.09% |

Claude-3.5 Direct Reasoning 74.18% Step 1: analyze the vulnerability in the provided code snippet, we need to understand how the `source_id` is derived and used, particularly focusing on the condition at line 95 which is identified as having a CWE-787

Llama-3.1 Direct Reasoning 50.13% contain the expected format or length, `source_id` might be assigned an incorrect or unexpected value. - If `SOC15_SOURCE_ID_FROM_IH_ENTRY` incorrectly parses `ih_ring_entry` or if `ih_ring_entry` does not

| No Slicing | 64.74% | operations or behaviors that are not intended for the actual input. | - An incorrect `source_id` could lead to incorrect branching in the code, potentially triggering |  |  |
| --- | --- | --- | --- | --- | --- |
| evaluation is primarily based on the Zero-Day dataset, and we | Given the analysis above, here are five possible patches to address the CWE-787 vulnerability at line 95: |  |  |  |  |
| have compared it with both LLM-based and non-LLM-based | 2 | 1 static void event_interrupt_wq_v10(struct kfd_node *dev, |  |  |  |
| baseline patching techniques on this dataset. The reason we | 4 | +3 | size_t ih_ring_entry_size; // Assume this is passed or can be determined | const uint32_t *ih_ring_entry) |  |
| use the ExtractFix dataset is mainly for being able to compare | } | return; | // Handle error: invalid ih_ring_entry size |  |  |
| and VulnFix [55]). | --- | } else if (source_id == SOC15_INTSRC_CP_BAD_OPCODE) { |  |  |  |
| Table 11: Data leakage test results on the ExtractFix dataset | Figure 10: A failure case where the vulnerability is incorrectly |  |  |  |  |
| 2 | 30%, 60%, 10% | 5%, 85%, 10% | 55%, 45%, 0% | 5%, 90%, 5% | to investigate the symptoms and root causes. As discussed in |
| 3 | 100%, 0%, 0% | 25%, 75%, 0% | 100%, 0%, 0% | 70%, 30%, 0% | Section 6.3, we show two examples for the failure symptoms |
| F | More End-to-end Experiment Results | rately identified or addressed. The symptom was incorrectly |  |  |  |
| Table 13 shows the detailed end-to-end integration results | the ‘source_id‘ variable, leading to proposed patches that fo- |  |  |  |  |
| with CodeQL against the Zero-Day dataset. | As shown, | cused on validating and constraining this value. However, the |  |  |  |
| A | PPATCH | achieves 23.85% F1 with fully automated method | root cause appears to be a logic error or insufficient condition |  |  |
| and 27.29% with realistic method. In contrast, the baselines | checking in the original code. The actual fix involves adding |  |  |  |  |
| approaches and models have much less effectiveness, indicat- | an additional condition to check if the context ID corresponds |  |  |  |  |
| ing that A | PPATCH | can be realistically used in practice. | to a specific packet type, suggesting that the vulnerability was |  |  |
| USENIX Association | 34th USENIX Security Symposium | 4499 |  |  |  |

---

## Page 21

Table 12: Detailed results of A PPATCH against the interprocedural samples from the Zero-Day dataset

Zero-Day Dataset

| Model | Approach | SynEq | SemEq | Plausible | Correct |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Recall | Prec | F1 | Recall | Prec | F1 | Recall | Prec | F1 | Recall | Prec | F1 |  |  |
| A | PPATCH | 4.76% | 1.11% | 1.80% | 9.52% | 4.44% | 6.06% | 38.10% | 21.11% | 27.17% | 38.10% | 26.67% | 31.37% |
| No Validation | 4.76% | 0.90% | 1.52% | 14.29% | 5.41% | 7.84% | 38.10% | 18.92% | 25.28% | 38.10% | 25.23% | 30.35% |  |
| No Slicing | 0.00% | 0.00% | 0.00% | 9.52% | 1.82% | 3.05% | 33.33% | 16.36% | 21.95% | 33.33% | 18.18% | 23.53% |  |
| Random Exemplars | 4.76% | 0.90% | 1.52% | 9.52% | 1.80% | 3.03% | 28.57% | 12.61% | 17.50% | 33.33% | 15.32% | 20.99% |  |
| GPT-4 | Manual Exemplars | 0.00% | 0.00% | 0.00% | 9.52% | 2.73% | 4.24% | 33.33% | 14.55% | 20.25% | 38.10% | 17.27% | 23.77% |
| Direct Reasoning | 0.00% | 0.00% | 0.00% | 4.76% | 0.90% | 1.52% | 38.10% | 12.61% | 18.95% | 38.10% | 13.51% | 19.95% |  |
| Standard Prompting | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 19.05% | 6.60% | 9.81% | 19.05% | 6.60% | 9.81% |  |

Zero-shot Completion 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 9.52% 4.72% 6.31% 9.52% 4.72% 6.31%

| A | PPATCH | 0.00% | 0.00% | 0.00% | 9.52% | 2.02% | 3.33% | 28.57% | 12.12% | 17.02% | 28.57% | 14.14% | 18.91% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No Validation | 0.00% | 0.00% | 0.00% | 9.52% | 2.02% | 3.33% | 28.57% | 11.32% | 16.22% | 28.57% | 13.34% | 18.18% |  |
| No Slicing | 0.00% | 0.00% | 0.00% | 9.52% | 2.06% | 3.39% | 14.28% | 10.31% | 11.98% | 23.81% | 12.37% | 16.28% |  |
| Random Exemplars | 0.00% | 0.00% | 0.00% | 9.52% | 2.08% | 3.42% | 19.05% | 9.38% | 12.57% | 23.81% | 11.46% | 15.47% |  |
| Gemini-1.5 | Manual Exemplars | 0.00% | 0.00% | 0.00% | 9.52% | 2.02% | 3.33% | 23.81% | 9.09% | 13.16% | 23.81% | 11.11% | 15.15% |
| Direct Reasoning | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 23.81% | 7.61% | 11.54% | 23.81% | 7.62% | 11.54% |  |
| Standard Prompting | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 4.76% | 1.10% | 1.79% | 4.76% | 1.10% | 1.79% |  |

Zero-shot Completion 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00%

| A | PPATCH | 4.76% | 0.93% | 1.55% | 19.05% | 3.70% | 6.20% | 47.62% | 21.30% | 29.43% | 47.62% | 25.93% | 33.57% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No Validation | 4.76% | 0.90% | 1.52% | 19.05% | 3.60% | 6.06% | 47.62% | 20.72% | 28.88% | 47.62% | 25.23% | 32.98% |  |
| No Slicing | 0.00% | 0.00% | 0.00% | 9.52% | 1.98% | 3.28% | 38.10% | 19.80% | 26.06% | 38.10% | 21.78% | 27.72% |  |
| Random Exemplars | 0.00% | 0.00% | 0.00% | 4.76% | 0.90% | 1.52% | 42.86% | 18.92% | 26.25% | 47.62% | 19.82% | 27.99% |  |
| Claude-3.5 | Manual Exemplars | 0.00% | 0.00% | 0.00% | 14.29% | 2.70% | 4.55% | 42.86% | 16.22% | 23.53% | 42.86% | 18.92% | 26.25% |
| Direct Reasoning | 0.00% | 0.00% | 0.00% | 9.52% | 1.89% | 3.15% | 38.10% | 17.92% | 24.38% | 42.86% | 19.81% | 27.10% |  |
| Standard Prompting | 0.00% | 0.00% | 0.00% | 4.76% | 1.96% | 2.78% | 9.52% | 4.90% | 6.47% | 14.29% | 6.86% | 9.27% |  |

Zero-shot Completion 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 14.29% 5.94% 8.39% 14.29% 5.94% 8.39%

| A | PPATCH | 0.00% | 0.00% | 0.00% | 9.52% | 2.35% | 3.77% | 38.10% | 15.29% | 21.82% | 38.10% | 17.65% | 24.12% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No Validation | 0.00% | 0.00% | 0.00% | 9.52% | 1.80% | 3.03% | 38.10% | 12.61% | 18.95% | 38.10% | 14.41% | 20.91% |  |
| No Slicing | 0.00% | 0.00% | 0.00% | 4.76% | 3.85% | 4.26% | 9.52% | 19.23% | 12.74% | 14.29% | 23.08% | 17.65% |  |
| Random Exemplars | 0.00% | 0.00% | 0.00% | 4.76% | 1.98% | 2.80% | 19.05% | 8.91% | 12.14% | 23.81% | 10.89% | 14.95% |  |
| Llama-3.1 | Manual Exemplars | 0.00% | 0.00% | 0.00% | 4.76% | 2.56% | 3.33% | 19.05% | 12.82% | 15.33% | 19.05% | 15.38% | 17.02% |
| Direct Reasoning | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 28.57% | 10.81% | 15.68% | 28.57% | 10.81% | 15.68% |  |
| Standard Prompting | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 9.52% | 3.13% | 4.71% | 9.52% | 3.13% | 4.71% |  |

Zero-shot Completion 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 9.52% 2.70% 4.21% 9.52% 2.70% 4.21%

Table 13: Detailed end-to-end results with vulnerability analyzer CodeQL against the Zero-Day dataset

Zero-Day Dataset

| Method | Model | Approach | SynEq | SemEq | Plausible | Correct |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Recall | Prec | F1 | Recall | Prec | F1 | Recall | Prec | F1 | Recall | Prec | F1 |  |  |
| A | PPATCH | 1.03% | 0.33% | 0.50% | 12.37% | 7.21% | 9.11% | 26.80% | 10.82% | 15.42% | 34.02% | 18.36% | 23.85% |
| Manual Exemplars | 1.03% | 0.32% | 0.49% | 7.22% | 5.18% | 6.03% | 15.46% | 5.83% | 8.46% | 22.68% | 11.33% | 15.11% |  |

Claude-3.5

Fully Automated Standard Prompting 0.00% 0.00% 0.00% 8.25% 5.25% 6.41% 11.34% 5.90% 7.76% 16.49% 11.15% 13.30%

Zero-shot Completion 0.00% 0.00% 0.00% 2.06% 0.78% 1.13% 14.43% 8.27% 10.51% 15.46% 9.04% 11.41%

| VulRepair | - | 2.06% | 0.47% | 0.77% | 13.40% | 8.47% | 10.38% | 1.03% | 0.24% | 0.38% | 16.49% | 9.18% | 11.79% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Getafix | - | 5.15% | 5.26% | 5.21% | 0.00% | 0.00% | 0.00% | 1.03% | 0.44% | 0.62% | 6.19% | 5.70% | 5.93% |
| A | PPATCH | 1.03% | 0.25% | 0.40% | 19.59% | 7.71% | 11.07% | 29.90% | 12.44% | 17.57% | 41.24% | 20.40% | 27.29% |
| Manual Exemplars | 0.00% | 0.00% | 0.00% | 15.46% | 6.05% | 8.70% | 15.46% | 5.33% | 7.92% | 25.77% | 11.38% | 15.79% |  |

Claude-3.5

Realistic Standard Prompting 1.03% 0.28% 0.44% 19.59% 9.47% 12.77% 13.40% 6.41% 8.67% 24.74% 16.16% 19.55%

Zero-shot Completion 0.00% 0.00% 0.00% 2.06% 0.78% 1.13% 14.43% 8.27% 10.51% 15.46% 9.04% 11.41%

| VulRepair | - | 2.06% | 0.47% | 0.77% | 13.40% | 8.47% | 10.38% | 1.03% | 0.24% | 0.38% | 16.49% | 9.18% | 11.79% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Getafix | - | 5.15% | 5.26% | 5.21% | 0.00% | 0.00% | 0.00% | 1.03% | 0.44% | 0.62% | 6.19% | 5.70% | 5.93% |
| more likely related to improper input validation or incorrect | 1 static int qca_read_fw_build_info(struct hci_dev *hdev) |  |  |  |  |  |  |  |  |  |  |  |  |

4 3

handling of certain packet types, rather than a straightforward 6 char cmd, build_label[QCA_FW_BUILD_VER_LEN]; struct edl_event_hdr *edl; struct sk_buff *skb;

5

| buffer overflow issue. | 10 | 8 | int build_lbl_len, err = 0; | bt_dev_dbg(hdev, "QCA read fw build info"); |
| --- | --- | --- | --- | --- |
| 11 | cmd = EDL_GET_BUILD_INFO_CMD; |  |  |  |
| 21 | 20 | if (!edl) { | edl = (struct edl_event_hdr *)(skb->data); | skb = __hci_cmd_sync_ev(hdev, EDL_PATCH_CMD_OPCODE, EDL_PATCH_CMD_LEN, &cmd, 0, HCI_INIT_TIMEOUT); |
| Figure 11 shows an example where failed patching attempts | 22 | 23 | bt_dev_err(hdev, "QCA read fw build info with no header"); |  |

24

| primarily focused on addressing potential issues with the | build_lbl_len = edl->data[0]; | goto out; | err = -EILSEQ; |
| --- | --- | --- | --- |
| 35 | 36 | 37 | if (build_lbl_len <= QCA_FW_BUILD_VER_LEN - 1) { |
| ‘build_label‘ array’s initialization and usage, but they missed | 38 | memcpy(build_label, edl->data + 1, build_lbl_len); |  |

of-bounds Read) vulnerability might occur. The CWE-125 vulnerability typically involves reading data past the end or Step 1: analyze the vulnerability in the code snippet provided, conduct the steps and identify where the CWE-125 (Out- *(build_label + build_lbl_len) = '\0';

before the beginning of a buffer, which can lead to unexpected behavior or sensitive information disclosure.

| the root cause of the vulnerability. The actual problem stems | ### Code Analysis: | ```c | 1 static int qca_read_fw_build_info(struct hci_dev *hdev) |
| --- | --- | --- | --- |
| from insufficient bounds checking when accessing data from | 5 | ``` | char cmd, build_label[QCA_FW_BUILD_VER_LEN]; |

defined by `QCA_FW_BUILD_VER_LEN`. - **Line 5**: This line declares two variables: `cmd`, a `char`, and `build_label`, an array of `char` with a length

the ‘skb‘ (socket buffer) structure. The ground truth patch re- ### Steps to Identify Vulnerability: ......

### Conclusion:

veals that the vulnerability is caused by inadequate validation The vulnerability likely stems from assumptions about the content and length of `build_label` without adequate verification. This could lead to out-of-bounds reads if the function or other parts of the program attempt to access data beyond the actual content of `build_label`. Proper checks and cautious handling of buffer lengths are essential to prevent such vulnerabilities.

of the ‘skb->len‘ against the expected data sizes at various Based on the analysis, here are five possible patches to address the CWE-125 vulnerability associated with the `build_label` buffer in the `qca_read_fw_build_info` function:

### Patch 1: Initialize the Buffer

points in the function. This allows for potential out-of-bounds ```diff

--- 5 char cmd, build_label[QCA_FW_BUILD_VER_LEN];

reads when accessing ‘edl‘ structure members and data. The 5 ``` char cmd, build_label[QCA_FW_BUILD_VER_LEN] = {0};

This patch initializes the `build_label` buffer to zero, ensuring that if the buffer is read without being properly set elsewhere, it will not read uninitialized memory.

| correct fix involves adding multiple checks to ensure that the | Ground Truth Patch: | 19a21,25 |  |
| --- | --- | --- | --- |
| ‘skb‘ contains enough data before accessing its contents, and | > | > | if (skb->len < sizeof(*edl)) { |
| > | } | goto out; | err = -EILSEQ; |

>

dynamically allocating memory for ‘build_label‘ instead of

| using a fixed-size array, which addresses both buffer overflow | Figure 11: A failure case where the patch has insufficient or |  |
| --- | --- | --- |
| and potential memory leaks. | incorrect code modification. |  |
| 4500 | 34th USENIX Security Symposium | USENIX Association |

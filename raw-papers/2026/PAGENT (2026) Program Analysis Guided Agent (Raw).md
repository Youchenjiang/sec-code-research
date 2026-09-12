---
title: "Program Analysis Guided LLM Agent for Proof-of-Concept Generation"
author: "Achintya Desai; Md Shafiuzzaman; Wenbo Guo; Tevfik Bultan"
creator: "arXiv GenPDF (tex2pdf:a6404ea)"
pages: 20
---

# Program Analysis Guided LLM Agent for Proof-of-Concept Generation

> **作者**：Achintya Desai; Md Shafiuzzaman; Wenbo Guo; Tevfik Bultan
> **總頁數**：20 頁

---

## Page 1

Program Analysis Guided LLM Agent for Proof-of-Concept

Generation

ACHINTYA DESAI, University of California, Santa Barbara, USA

MD SHAFIUZZAMAN, University of California, Santa Barbara, USA

WENBO GUO, University of California, Santa Barbara, USA

TEVFIK BULTAN, University of California, Santa Barbara, USA

ACM Reference Format:

Achintya Desai, Md Shafiuzzaman, Wenbo Guo, and Tevfik Bultan. 2026. Program Analysis Guided LLM Agent

for Proof-of-Concept Generation. 1, 1 (April 2026), 20 pages. https://doi.org/10.1145/nnnnnnn.nnnnnnn

Software developers frequently receive vulnerability reports that require them to reproduce the

vulnerability in a reliable manner by generating a proof-of-concept (PoC) input that triggers it.

Given the source code for a software project and a specific code location for a potential vulnerability,

automatically generating a PoC for the given vulnerability has been a challenging research problem.

Symbolic execution and fuzzing techniques require expert guidance and manual steps and face

scalability challenges for PoC generation. Although recent advances in LLMs have increased the

level of automation and scalability, the success rate of PoC generation with LLMs remains quite

low. In this paper, we present a novel approach called Program Analysis Guided proof of concept

generation agENT (PAGENT) that is scalable and significantly improves the success rate of automated

PoC generation compared to prior results. PAGENT integrates lightweight and rule-based static

analysis phases for providing static analysis guidance and sanitizer-based profiling and coverage

information for providing dynamic analysis guidance with a PoC generation agent. Our experiments

demonstrate that the resulting hybrid approach significantly outperforms the prior top-performing

agentic approach by 132% for the PoC generation task.

1 Introduction

Due to increasing interdependencies within software ecosystems it is crucial to detect and mitigate

security vulnerabilities as quickly as possible to restrict their impact. With the development of

sophisticated vulnerability-detection techniques, the number of discovered vulnerabilities has also

risen significantly in recent years [11]. When a vulnerability is discovered in a software project,

it is reported to the project’s developers and is expected to result in a patch that fixes it. Given

the rising number of vulnerabilities, addressing them in a timely manner can be challenging and

critical, especially in open-source software projects. Reproducing the vulnerabilities is an important

step in addressing them through vulnerability triage, patch generation, and patch validation.

arXiv:2604.07624v1 [cs.SE] 8 Apr 2026

Authors’ Contact Information: Achintya Desai, University of California, Santa Barbara, Santa Barbara, CA, USA, achintya@

ucsb.edu; Md Shafiuzzaman, University of California, Santa Barbara, Santa Barbara, CA, USA, mdshafiuzzaman@ucsb.edu;

Wenbo Guo, University of California, Santa Barbara, Santa Barbara, CA, USA, henrygwb@ucsb.edu; Tevfik Bultan, University

of California, Santa Barbara, Santa Barbara, CA, USA, bultan@ucsb.edu.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee

provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the

full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored.

Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires

prior specific permission and/or a fee. Request permissions from permissions@acm.org.

© 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.

ACM XXXX-XXXX/2026/4-ART

https://doi.org/10.1145/nnnnnnn.nnnnnnn

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 2

2 Achintya Desai, Md Shafiuzzaman, Wenbo Guo, and Tevfik Bultan

Reproducing a vulnerability in a reliable manner involves generating a proof-of-concept (PoC)

input that triggers it. The existence of a PoC input primarily proves the presence of a vulnerability.

It would be natural to assume that each reported vulnerability is supported by a PoC, which,

surprisingly, is not the case. Vulnerability reports lacking a valid PoC are not uncommon. It often

becomes the developer’s responsibility to assess these vulnerability reports and produce a reliable

PoC, which is a time-consuming task. The key technical challenge in the PoC generation task, in

general, is achieving an automated, scalable combination of vulnerability-detection capabilities

to identify the vulnerable code snippet and semantic understanding of the codebase to infer the

inputs that can reach the vulnerable code location. Traditional static analysis tools are scalable

but are widely known to be prone to false positives and do not automatically produce a PoC.

Although symbolic execution [4] has the ability to produce a PoC and a precondition for the

detected vulnerability, it suffers from the path explosion problem and often relies on manual

environmental modeling and expert guidance to scale. Traditional fuzzing is the most widely used

automated vulnerability-detection technique that generates PoC inputs. However, fuzzers also

require expert guidance via fuzzing harness, input grammar, dictionaries, protocol awareness, and

high-quality seed corpora to be effective.

Hybrid vulnerability-detection techniques have shown potential for minimizing the drawbacks

of each technique while enhancing their strengths. Fuzzing and static analysis have been shown

to be complementary approaches for detecting memory-safety-related bugs [15]. There have

been efforts to integrate these approaches in the literature [34, 37, 41, 45]. Static analysis has

also been used to guide symbolic execution to achieve scalability and reduce false positives in

vulnerability detection [3, 36]. However, they all rely on a human-in-the-loop to provide expert

knowledge to either guide the tool or convert the tool’s findings into a vulnerability-triggering PoC

input. The application of Large Language Models (LLMs) to software engineering tasks [12, 24] is

becoming increasingly popular. LLM agents are already becoming a viable direction for increasing

automation and scalability of existing solutions. Across various datasets, LLM agents [16] have also

demonstrated a potential ability to analyze code and infer its semantics. However, as of now, LLM

agents have shown poor accuracy due to their tendency to hallucinate. This is a major challenge

to the applicability of agents for PoC generation, as they are likely to produce inaccurate results

without guidance.

Inspired by prior hybrid analysis approaches, and to address the challenges involved in automated

PoC generation, we propose a novel hybrid approach that we call Program Analysis Guided LLM

agENT (PAGENT) for PoC generation. PAGENT takes a project’s source code, a target code location,

and a project build script as input and automatically generates a PoC if a vulnerability exists

at the target code location, using static and dynamic analysis-guided LLM agents. PAGENT is

composed of three components: 1) Static Analysis, 2) PoC Generation Agent, and 3) Dynamic

Analysis. The primary goal of the static analysis stage is to produce reliable vulnerability-specific

guidance for the PoC generation agent from the source code. Towards this goal, we desire the

following properties from our static analysis approach: 1) scalable towards large codebases, and

2) customizable and extensible to support vulnerability patterns. The static analysis component

generates the vulnerability report by extracting vulnerability-relevant information with source

code-level program analysis. The vulnerability entry from the input code location is then fed to

the LLM agent, which has interactive access to the source code to generate a candidate PoC. The

candidate PoC is executed in a test environment that hosts an instrumented binary for dynamic

analysis. If the candidate PoC fails to trigger a crash, dynamic analysis provides feedback to the

agent with respect to the execution run in the test environment. The agent utilizes this feedback to

further refine its code analysis to craft a valid PoC. This loop between the agent and the dynamic

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 3

Program Analysis Guided LLM Agent for Proof-of-Concept Generation 3

analysis continues until either a PoC that triggers a crash is generated or the iteration budget is

exhausted.

We evaluate PAGENT on a dataset of 203 vulnerabilities, chosen from Cybergym [40], spanning

10 open-source software projects across diverse software domains, including an IoT protocol, a

Data compression library, and GNU binary tools. Given the textual vulnerability report and the

corresponding stack trace as input, the GPT-5 agent achieves the highest performance among

the competing agents from the Cybergym benchmark. PAGENT, without a stack trace or textual

report, with the DeepSeek3.1-termius model, one of the weakest-performing models at this task,

outperforms both Sonnet-4 and GPT-5 agents, achieving an overall accuracy of 42% on our dataset.

PAGENT with DeepSeek3.2, a cheaper, open-source alternative to closed-source models, achieves

64.6% accuracy on the same dataset and significantly outperforms the GPT-5 agent, our best results.

Furthermore, PAGENT identifies 32 post-patch vulnerabilities that trigger in the patched version

of the source code as well.

In software codebases, it is common to maintain a shared repository for source code. As the

developers maintain and add new features to the software through code commits, PAGENT can

leverage code locations from the change log to detect any vulnerabilities introduced through

the corresponding commit. The PAGENT approach can be easily integrated into CI/CD software

pipelines for deployment after each commit. For each code commit to the codebase, the modified

code locations can be collected and directly fed into PAGENT, along with the source code. If a

code commit introduces a modeled vulnerability, PAGENT can detect and prove its presence by

generating a concrete PoC input that triggers it.

Our overall contributions can be summarized as follows:

• Static analysis for LLM agent: We design and implement a scalable and automatable static

analysis approach to guide LLM agents to improve the precision of LLM agents at PoC

generation.

• Dynamic analysis for LLM agent: Our dynamic analysis phase drives the PoC validation,

a crucial step in confirming the vulnerability, to facilitate the LLM agent to refine its code

analysis.

• Enhancing agents’ effectiveness: PAGENT improves the accuracy of the worst-performing

open-sourced LLM (DeepSeek3.1) with static and dynamic program analysis by 132%, and it

outperforms the top 2 best-performing closed-sourced LLMs (Sonnet 4 and GPT-5-Reasoning)

models by 100%, and 104% on average at a cheaper (32x, 0.42$/vs 14$/) cost per million output

tokens.

• Improvement at post-patch vulnerability detection: PAGENT also demonstrates signifi-

cant improvement (4x) at detecting post-patch vulnerabilities compared to the best-performing

LLM agent on the dataset.

2 Overview

We aim to address the following problem: Given a source code S and a specific code location 𝐿 ,

automatically generate a functional Proof-of-Concept (PoC) input 𝐼 that demonstrates the existence of

a vulnerability at location 𝐿 . To address this problem, we propose a hybrid framework, illustrated

in Fig. 1, that integrates static and dynamic analysis with an LLM-based agent. The framework

starts with a two-phase static analysis that generates an entrypoint-driven reachability graph

using a light-weight static analysis phase, followed by a scalable, customizable, and extensible

rule-based static analysis phase. An LLM-driven PoC generation agent then leverages these results

to navigate the codebase to resolve the input constraints required to synthesize a candidate PoC.

This candidate is dispatched via a bash command to a test environment where it is executed against

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 4

4 Achintya Desai, Md Shafiuzzaman, Wenbo Guo, and Tevfik Bultan

Instrumented

Binary

Code Location

PoC

| Source | Static Analysis | Vulnerability | Dynamic |
| --- | --- | --- | --- |
| Generation | Analysis |  |  |
| Code | Guidance | Report |  |
| Agent | Guidance |  |  |

PoC

Fig. 1. Overview of PAGENT Technique

| Static Analysis Guidance | Dynamic Analysis Guidance |  |  |
| --- | --- | --- | --- |
| ‘Vulnerability Type’: | [... ‘file_path":"/src/binutils-gdb/opcodes/ |  |  |
| ‘Stack-Buffer-Overflow-Vulnerability’, | tic4x-dis.c","function_name": | "print_insn_tic4x" | , |

‘Vulnerable Function’: ‘get_register_operand’, ‘region_coverage":75.00,"line_coverage":80.95,

| ‘Entrypoint’: ‘LLVMFuzzerTestOneInput’, | "branch_coverage":11.76, |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ‘Taint Path’: "[‘LLVMFuzzerTestOneInput’, | ‘file_path":"/src/binutils-gdb/opcodes/ |  |  |  |  |
| ‘print_insn_tic30’ | , ‘print_branch.171581’, | tic4x-dis.c","function_name":‘tic4x-dis.c:tic4x_ |  |  |  |
| ‘get_register_operand’]", | disassemble", "region_coverage":64.71,"line_ |  |  |  |  |
| ‘Vulnerable Program Location’: ‘204’, | coverage":77.05,"branch_coverage":16.67, |  |  |  |  |
| ‘Template Assertion Violation’: ‘0 | ‘file_path":"/src/binutils-gdb/opcodes/ |  |  |  |  |
| < | = | get_register_operand:30:0:0 | < | = | tic4x-dis.c","function_name":"tic4x-dis.c: |

tic4x_print_register","region_coverage":72.41,

SIZEOF(get_register_operand:%25)’ "line_coverage":83.33,"branch_coverage":16.67,

...]

Fig. 2. Static and Dynamic analysis guidance example for ARVO:18615

a sanitizer-instrumented binary of S . In the event of a failure, the agent receives the dynamic

analysis results in a command response and a coverage report file. The agent utilizes this feedback

to iteratively refine the input until a successful PoC is produced or the iteration budget is exhausted.

Fig. 2 showcases an example of static and dynamic analysis guidance produced by our framework

for ARVO:18615 vulnerability instance from the dataset. The instance focuses on a buffer overread

vulnerability in the get_register_operand function of the GNU Binutils TIC30 disassembler. As

shown in Listing 1, the function invokes strncpy with a fixed copy length OPERAND_BUFFER_LEN ,

although the destination buffer allocated by its caller may be smaller. This size mismatch results in a

buffer overread. Triggering this vulnerability requires not only identifying the faulty copy operation

but also constructing an input 𝐼 that selects the correct disassembly mode and reaches the vulnerable

execution context. Automatically synthesizing such an 𝐼 requires reasoning over complex, cross-file

program logic, and input-dependent control flow. This task is well-suited for an LLM-based PoC

agent, but difficult to encode with fixed heuristics. Relying solely on natural-language vulnerability

descriptions is insufficient in such cases. For example, the vulnerability report for this instance says

“An array overrun occurs in tic30-dis.c within the print_branch function due to an incorrect

size of the operand array when disassembling corrupt TIC30 binaries”. This guides the agent to

the relevant source file and vulnerable function, but lacks the precise semantics including feasible

entry points and call-path constraints needed to reach 𝐿 . This limitation motivates the use of

static analysis to extract vulnerability-specific guidance that grounds the agent’s reasoning in

the program structure. Static analysis can explicitly encode feasible entrypoints and reachability

constraints extracted from the program as illustrated in Fig. 2. This information enables the PoC

generation agent to leverage call-path information and vulnerability metadata to select candidate

instruction patterns and architecture constants intended to invoke get_register_operand .

193 static int get_register_operand ( unsigned char fragment , char * buffer )

194 {

195 const reg * current_reg = tic30_regtab ;

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 5

Program Analysis Guided LLM Agent for Proof-of-Concept Generation 5

Vulnerability Rules*

| Source | Lightweight | Reachability | Rule-based | Vulnerability |
| --- | --- | --- | --- | --- |
| Code | Static Analysis | Graph | Static Analysis | Report |

Fig. 3. Overview of Static Analysis Guidance Component (* denotes reusable input across software projects)

| 196 | if | ( buffer | == | NULL ) | return | 0; |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 197 | for | (; | current_reg | < | tic30_regtab_end ; | current_reg ++) | { |  |
| 198 | if | (( fragment | & | 0 x1F ) | == | current_reg -> opcode ){ |  |  |
| 199 | strncpy | ( buffer , | current_reg -> name , | OPERAND_BUFFER_LEN ); | /* | Vulnerable | copy | */ |
| 200 | buffer [ OPERAND_BUFFER_LEN | - | 1] | = | 0; |  |  |  |
| 201 | return | 1; |  |  |  |  |  |  |
| 202 | } | } |  |  |  |  |  |  |
| 203 | return | 0; |  |  |  |  |  |  |

204 }

Listing 1. Code snippet from tic30-dis.c file in binutils project

However, static guidance alone can be imprecise when multiple execution paths coexist. In this

example, the generated inputs may exercise the TIC4X disassembler ( tic4x-dis.c ) instead of the

intended TIC30 disassembler ( tic30-dis.c ), due to an incorrect architecture selection. Dynamic

analysis feedback resolves this ambiguity. By inspecting coverage information illustrated in Fig. 2

from failed executions, the agent detects that the vulnerable code path is not being reached and

identifies the incorrect architecture configuration. The agent then revises its input accordingly,

selecting the correct TIC30 architecture constant. This refinement enables the generated PoC to

reach get_register_operand and successfully trigger the buffer overread.

3 Static and Dynamic Analysis Guided Agentic PoC Generation

We describe the technical details of the three main components of PAGENT (Fig. 1) in this section.

3.1 Static Analysis Guidance

We designed our static analysis to achieve scalability towards the large codebases and customizability

and extensibility to support a variety of vulnerability patterns. To improve the scalability of

the analysis, we perform an initial lightweight static analysis on the source code. This includes

entrypoint-driven automated call-graph construction, over-approximate indirect call resolution,

and dead-code removal. To make our static analysis customizable and extensible, we implement a

rule-based static analysis technique that identifies vulnerable code patterns in the sourcecode. This

technique allows us to add and customize rules depending on the vulnerability patterns. It can be

reused across domains and can be extended by adding new vulnerability patterns when new types

of vulnerabilities are discovered. Furthermore, the rules are written at LLVM-IR level, allowing

the user to capture all source-code level variants for a specific bug pattern. Figure 3 provides an

overview of our static analysis component.

3.1.1 Lightweight Static Analysis. Software codebases are built on a large number of functions. To

achieve scalability in PoC generation, it is essential to filter out functions that do not influence the

given vulnerability. Identifying such functions accurately through static analysis is challenging.

Removal of a function that holds a vulnerability or impacts the exploitability of a vulnerability can

lead to false negatives. To address this issue, we propose a lightweight static analysis component

that takes source code with entrypoints as input and generates a reachability graph containing

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 6

6 Achintya Desai, Md Shafiuzzaman, Wenbo Guo, and Tevfik Bultan

Algorithm 1 Static Analysis Guidance Component

Input: Source code 𝑆 , Build Instructions 𝑏 , Rule Repository 𝑅 , (Optional) Entrypoints 𝐸 𝑝

Output: Vulnerability Report 𝑉 𝑅

1: // Phase 0: Compile the source code to LLVM-IR

2: 𝑆 𝐿 ← Build( 𝑆 , 𝑏 )

3: // Phase 1: Lightweight Static Analysis

4: 𝐸 𝑝 = 𝐸 𝑝 ∪ { LLVMFuzzerTestOneInput() , main() }

5: 𝐸 𝑙 ← Set_Entrypoints( 𝐸 𝑝 )

6: 𝐺 ← Construct_CallGraph( 𝑆 𝐿 )

7: 𝑇 ← Filter_Reachable( 𝐺 , 𝐸 𝑙 )

8: // Phase 2: Rule-based Static Analysis

9: 𝐹 ← Generate_Program_Facts( 𝑆 𝐿 )

10: 𝑉 ← Apply_Vulnerability_Rules( 𝐹 , 𝑅 )

11: 𝑉 𝑅 = 𝜙

12: for each 𝑣 in 𝑉 do

| 13: | 𝑒 | = | 𝜙 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14: | 𝑒 | ["Vulnerability Type"] | = | 𝑣 | ["Vulnerability Type"] |  |  |  |
| 15: | 𝑒 | ["Vulnerable Function"] | = | 𝑣 | ["Vulnerable Function"] |  |  |  |
| 16: | 𝑒 | ["Taint Path"] | = | Extract_Path[ | 𝑇 | , | 𝑒 | ["Vulnerable Function"]] |
| 17: | 𝑒 | ["Entrypoint"] | = | 𝑒 | ["Taint Path"][0] |  |  |  |
| 18: | 𝑒 | ["Vulnerable Program Location"] | = | 𝑣 | ["Vulnerable Program Location"] |  |  |  |
| 19: | 𝑒 | ["Template Assertion Violation"] | = | 𝑣 | ["Template Assertion Violation"] |  |  |  |
| 20: | 𝑉 | 𝑅 | = | 𝑉 | 𝑅 | ∪ | 𝑒 |  |

21: end for

functions reachable only from the entrypoints. This involves constructing an over-approximate

call graph and filtering out unreachable functions from the entrypoints. Lightweight static analysis

component ensures that we only report the vulnerabilities that are potentially reachable from the

specified entrypoints.

We begin by setting the entrypoints in the input source code. Lightweight static analysis au-

tomatically detects the common entrypoints, specifically the ones used by fuzzers such as main() ,

LLVMFuzzerTestOneInput() . It also supports an optional user-defined list of entrypoints. Once the

entrypoints are set, we perform an entrypoint-driven call graph construction pass where all the

functions that are reachable from the entrypoints are identified. In complex codebases, indirect

function calls via function pointers or virtual method tables (C++) are typical for supporting callback

or event handler functionality. Entrypoint-driven call graph construction pass involves resolving

direct and indirect function calls via function signature analysis (FSA). In the literature, FSA [19]

has been widely regarded as a sound approach when type information is available. Compared

to modern approaches like Multi-Layer Type Analysis (MLTA) [26] and Type-based dependence

analysis [25], FSA is highly scalable due to linear time signature matching between indirect call

instructions and function signatures. However, FSA approach is prone to produce a high number

of false positives due to over-approximation. For lightweight static analysis, the FSA approach

provides a scalable and sound strategy for constructing an over-approximate call graph. Once the

list of reachable functions is generated from the entrypoint-driven call graph construction pass,

we perform code elimination by marking unreachable functions from the entrypoints. This pass

ensures that the resulting source code only consists of potentially reachable functions from the

entrypoints and essential code definitions.

4285 static void dump_bfd_private_header ( bfd * abfd )

4286 {

| 4287 | if | (! bfd_print_private_bfd_data | ( abfd , | stdout )) |
| --- | --- | --- | --- | --- |
| 4288 | non_fatal | (_(" warning :␣ private ␣ headers ␣ incomplete :␣%s") , |  |  |
| 4289 | bfd_errmsg | ( bfd_get_error | () )); |  |

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 7

Program Analysis Guided LLM Agent for Proof-of-Concept Generation 7

4290 }

Listing 2. Code snippet from objdump.c file in binutils project

We implemented our lightweight static analysis component at the LLVM-IR level. For tailored

program analysis, LLVM provides a comprehensive infrastructure for writing analysis passes. It also

allows us to maintain compatibility with our rule-based static analysis, which utilizes the inherent

modularity of LLVM-IR to design customizable vulnerability rules. This adds an extra step at the

beginning of the lightweight static analysis to use the build instructions to compile the project into

LLVM-IR. Consider the code snippets related to motivating example shown in Listing 2 and Listing 3.

dump_bfd_private_header() is an internal function, encountered along the path towards vulnerability

from motivating example, that calls bfd_print_private_bfd_data() to display internal data specific

to the object file’s format from a binary file descriptor (BFD). Depending on the object file type,

bfd_print_private_bfd_data() gets resolved to a target-specific function defined in the BFD target

vector. For OpenVMS Alpha, this call gets resolved to vms_bfd_print_private_bfd_data() if defined in

the BFD target vector. For this example, the lightweight static analysis component translates the

source code to LLVM-IR. It detects the indirect call instruction, during the first pass at the LLVM

level, associated with the function call on line number 4287 from Listing 2. It matches the normal-

ized function signature for the indirect call: i1 (%struct.bfd* , i8*) with the function definition

of vms_bfd_print_private_bfd_data(): i1 @vms_bfd_print_private_bfd_data(%struct.bfd %0, i8* %1) and

adds it as a call edge from function bfd_print_private_bfd_data() to vms_bfd_print_private_bfd_data() .

This ensures that the function remains vms_bfd_print_private_bfd_data() reachable from the entry-

point due to the possibility of an indirect call from dump_bfd_private_header() at runtime.

3.1.2 Rule-based Static Analysis. It is well-known that LLM agents are prone to hallucination [21,

44], which can cause them to report false positive vulnerabilities and incorrect PoCs. Specifically,

LLM agents suffer from poor accuracy at the task of extracting vulnerability-specific information

from the codebase, which is crucial for crafting accurate PoC input as demonstrated by the moti-

vating example. To address this issue, we introduce a rule-based static analysis component that

can reliably generate vulnerability-specific information such as taint path, taint source, vulnerable

function, and assertion template, capturing the vulnerability as an assertion violation. Rule-based

static analysis component is driven by the vulnerability rule repository. The vulnerability rule

repository consists of vulnerability rules that target commonly known vulnerabilities, such as

integer overflow and buffer overflow. There are two main advantages to maintaining the vulner-

ability rule repository: 1) Vulnerability rules are reusable across domains; Once they are added

to the rule repository, they will be added to any future static analysis runs, 2) The vulnerability

rule repository can be easily extended to support any new common or domain-specific vulnerabili-

ties. We modeled the following 12 vulnerabilities as vulnerability rules within the rule repository:

Heap-buffer-overflow, Stack-buffer-overflow, Global-buffer-overflow, Heap-buffer-underflow, Stack-

buffer-underflow, Global-buffer-underflow, Division-by-zero, Integer-Overflow, Integer-Underflow,

Out-of-bounds, Use-after-free, Double-free.

8307 static bool vms_bfd_print_private_bfd_data ( bfd * abfd , void * ptr )

8308 {

| 8309 | FILE | * file | = | ( FILE | *) ptr ; |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8310 | if | ( bfd_get_file_flags | ( abfd ) | & | ( EXEC_P | \| | DYNAMIC )) | evax_bfd_print_image | ( abfd , | file ); |
| 8311 | else | { |  |  |  |  |  |  |  |  |
| 8312 | if | ( bfd_seek | ( abfd , | 0, | SEEK_SET )) | return | false ; |  |  |  |
| 8313 | evax_bfd_print_eobj | ( abfd , | file ); |  |  |  |  |  |  |  |
| 8314 | } |  |  |  |  |  |  |  |  |  |
| 8315 | return | true ; |  |  |  |  |  |  |  |  |

8316 }

Listing 3. Code snippet from vms-alpha.c file in binutils project

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 8

8 Achintya Desai, Md Shafiuzzaman, Wenbo Guo, and Tevfik Bultan

Rule-based static analysis approach utilizes Datalog to specify vulnerability patterns. For a given

program, these analysis rules instantiate fixpoint computations corresponding to evaluations of

Datalog logic programs, resulting in the generation of facts (such as vulnerable code locations in

the code). Although the underlying facts vary across different programs, rule-based static analysis

approach crucially allows the vulnerability rules themselves to be reused across programs. Our

rule-based static analysis component generates facts over the LLVM-IR version of the source code,

applying vulnerability rules to detect vulnerable code locations, and extracting vulnerability-specific

information from the code. We implemented our rule-based static analysis using the open-source

cclyzerpp tool built on Soufflé, an expressive dialect of Datalog. For generating facts, cclyzerpp

provides built-in LLVM passes that populate fact relations with input program facts based on the

abstract syntax tree (AST) of LLVM modules. We utilize Soufflé’s highly parallel engine to detect

vulnerabilities and extract their respective assertion template, code locations, vulnerable functions,

and taint sources.

. decl out_of_bounds_primitive (? type : symbol , ? assertion : symbol , ? func : Function , ? op1 :

Operand , ? op2 : Operand , ? instr : Instruction , ? line : LineNumber ) choice - domain (? func , ?

line )

. output out_of_bounds_primitive ( delimiter =" ,")

out_of_bounds_primitive (? type , ? assertion , ? func , ? op1 , ? op2 , ? instr , ? line ) :-

? type = " Out -of - Bounds - Vulnerability ",

? assertion = cat ("0 <= ", to_string (? op2 ) , " <= SIZEOF (" , to_string (? op1 ) , ") ") ,

instr_func (? instr , ? func ) ,

indexaccessinstructions (? op1 , ? op2 , ? instr ) ,

instr_pos (? instr , ? line , ? col ).

Listing 4. Vulnerability rule for Out-of-Bounds Vulnerability

Listing 4 shows the vulnerability rule for the out-of-bounds vulnerability, discussed in the mo-

tivating example, at the instruction level. The vulnerability rule is composed of three clauses:

1) The first clause sets the value of ?type to vulnerability type, 2) The second clause sets the

value of ?assertion which holds the assertion template specific to the vulnerability type, 3) The

third set of clauses involve detecting the vulnerability in the form of program facts and con-

straints. In the above example, we set the ?type to the constant string "Out-of-Bounds-Vulnerability"

to indicate the vulnerability type. The ?assertion is set to a vulnerability-specific template that

is instantiated based on the operands involved in the vulnerability. For the motivating exam-

ple, the ?assertion will be set to string 0 <= <tmpfull_project.bc>:evax_bfd_print_dst:126:0:5 <=

SIZEOF(<tmpfull_project.bc>:evax_bfd_print_dst:%106) . Notice that the assertion template involves

values directly from LLVM-IR and is not replaced with their source code name. Based on the

availability of debug information and optimization level, it is not always possible to resolve

the LLVM-IR operand names to their source code names. Although we do not generate source-

code level assertions, the assertion template generated above provides a vulnerability-specific

condition to be violated by the prospective PoC. As LLMs are well-versed with the LLVM syn-

tax, they can reason about assertion templates and extract useful information, such as 5 in

<tmpfull_project.bc>:evax_bfd_print_dst:126:0:5 indicates the index 5 access from the buffer buf . List-

ing 5 shows an example vulnerability report for an out-of-bounds vulnerability generated by the

rule-based static analysis component. For each potential vulnerability, our vulnerability report

includes the following information: Vulnerability type, Vulnerable function, Entrypoint, Taint path,

Vulnerable program location, and Template assertion.

" potential_target_ < num >": {

" Vulnerability ␣ Type ": " Out -of - Bounds - Vulnerability " ,

" Vulnerable ␣ Function ": " evax_bfd_print_dst " ,

" Entrypoint ": " LLVMFuzzerTestOneInput .70743 " ,

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 9

Program Analysis Guided LLM Agent for Proof-of-Concept Generation 9

Source

| Code Location | Code |  |
| --- | --- | --- |
| Vulnerability | Preparation | Task Guidance |
| Report | Phase | Input |

Fig. 4. Overview of PoC Generation Agent

Algorithm 2 PoC Generation Agent

Input: Source Code 𝑆 , Vulnerability Report 𝑉 𝑅 , Code Location

Output: PoC 𝑃

1: // Phase 0: Prepare Task guidance input: 𝑇 𝑖

2: 𝑈 ← PROMPT("Generate the exploit PoC...")

4: 𝑒 ← Fetch_Vulnerability_Entry( 𝑉 𝑅 , 𝐶 𝐿 )

5: 𝐼 ← Generate_README( 𝐼 𝑡 , 𝑒 )

6: 𝑇 𝑖 ← ( 𝑈 , 𝐼 )

7: // Phase 1: Agent-Environment Loop

8: 𝑃 = 𝜙

9: 𝑊 ← Instantiate_Workspace( 𝑆 , 𝑇 𝑖 [ 𝐼 ] )

10: agent , agent_state ← Instantiate_Agent( 𝐿𝐿𝑀 , 𝑇 𝑖 [ 𝑈 ] ,

11: while agent_state = "running" do

| 12: | candidate_poc | ← | Recv_PoC( | agent | ) |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13: | dynamic_feedback | ← | Test_Environment_Execute( |  |  |  |  |  |
| 14: | if | dynamic_feedback | [ | exit_code | ] | ≠ | 0 | then |
| 15: | 𝑃 | ← | candidate_poc |  |  |  |  |  |
| 16: | end if |  |  |  |  |  |  |  |
| 17: | Send_Response( | agent | , | dynamic_feedback | ) |  |  |  |

18: end while

" Taint ␣ Path ": "[' LLVMFuzzerTestOneInput .70743 ' , ␣ ' bfd_close .136854 ' , '

_bfd_archive_close_and_cleanup .9552 ' , ␣ ' dump_bfd_private_header ',␣ '

" Vulnerable ␣ Program ␣ Location ": " 7260 " ,

␣ SIZEOF ( </ tmp / full_project .bc > :evax_bfd_print_dst: %106) "

3.2 PoC Generation Agent

Candidate

PoC

LLM Agent Test

Environment

Dynamic

PoC Feedback

𝐶 𝐿 , Iteration Budget 𝐵

𝑊 , 𝐵 )

candidate_poc )

}

, Vol. 1, No. 1, Article . Publication date: April 2026.

3: 𝐼 𝑡 ← TEMPLATE("You are given several files that describe a software vulnerability...")

vms_bfd_print_private_bfd_data ',␣ ' evax_bfd_print_image ',␣ ' evax_bfd_print_dst '] " ,

" Template ␣ Assertion ␣ Violation ": "0␣ <=␣ </ tmp / full_project .bc > :evax_bfd_print_dst:126:0:5 ␣ <=

Listing 5. Vulnerability report for Out-of-Bounds Vulnerability from motivating example 1

The vulnerability report generated by the static analysis incorporates vulnerability-specific infor-

mation from the source code. The vulnerability report, in isolation, is insufficient to produce a

PoC. Specifically, the rule-based static analysis component does not infer the PoC input as it does

not reason about the branch conditions encountered along the taint path. Since static analysis

can produce false positives, the vulnerability report also does not guarantee the existence of a

vulnerability at the reported location. Generally, when a vulnerability is detected by static analysis,

it requires additional manual steps: interpreting the vulnerability report, identifying the execution

path, crafting the crashing input, and validating the PoC. Our PAGENT framework utilizes a PoC

generation agent to automate these steps. The PoC generation agent is a generalist agent based on

the codeAct architecture. It leverages advancements in LLMs to write code that performs an action

in the code space rather than the text space, in its environment. We assign the PoC generation

---

## Page 10

| 10 | Achintya Desai, Md Shafiuzzaman, Wenbo Guo, and Tevfik Bultan |
| --- | --- |
| Prompt | Task-specific instructions |
| Generate the exploit PoC using | You are given several files (listed below) that describe |

the information in ‘/workspace’, a software vulnerability. Your task is to generate a

check ‘/workspace/README.md’ proof-of-concept (PoC) that demonstrates how this vulnerability

can be triggered or exploited. The PoC should be a single **raw

| for more details. Submit and | input file** (e.g., binary or text) that would be provided as |
| --- | --- |
| test the PoC file with ‘bash | input to the vulnerable program to trigger the vulnerability. |
| submit.sh /path/to/poc’. DO NOT | Please follow the instructions below for submitting the PoC. |
| GIVE UP UNTIL you trigger the | # Files |
| crash, i.e., the exit code is | {Workspace_Description} |

# Use the following vulnerability specific information and

| not 0. USE the static analysis | coverage guidance to generate proof-of-concept: |
| --- | --- |
| information and coverage | {Vulnerability_Report_Entry} |
| guidance to refine your PoC | # Submission Instructions |

until you succeed at triggering {Submission_Instructions}

the crash. # IMPORTANT INSTRUCTIONS

{Important_Instructions}

Fig. 5. Prompt and Task-specific instruction Template

agent the task of generating a PoC with interactive access to the source code, guided by static and

dynamic analysis. Below, we discuss the two main components of the PoC generation agent.

3.2.1 Preparation Phase. The preparation phase generates a task guidance input consisting of a

prompt and task-specific instructions. For the PoC generation task, we designed our prompt as a

set of instructions that point to the source code location in the environment, assign the task to the

agent, and provide general guidelines for utilizing static and dynamic analysis. Note that this is a

one-time interaction modeled as a prompt and stored as a workspace context for the agent to recall

if needed. Based on the input code location, the preparation phase selects a matching entry from

the vulnerability report, which is then encoded into the task-specific instructions. The task-specific

instructions also include PoC testing details and general facts about the testing environment. PoC

testing details describe how to submit a PoC for testing using a bash command. Testing environment

facts ensure that the agent does not make any incorrect assumptions about the testing environment,

such as in-built mitigations, the absence of a sanitizer, etc. The task-specific instructions are encoded

as a README file in the agent’s workspace. Figure 5 shows the prompt and task-specific instruction

template. The Workspace_Description is a placeholder for the path to the source code and related

file locations. The Vulnerability_Report_Entry holds the static-analysis-generated vulnerability

information for the specific code location.

3.2.2 Agent. The agent takes the prompt, an iteration budget, and workspace as input and generates

candidate PoCs based on its analysis of the source code and static analysis information. The budget

parameter allows the user to limit the agent’s underlying LLM-related cost and resource usage. The

workspace is a sandboxed environment with which it can interact through code-based actions. It

consists of a bash shell connected to the operating system running in the sandboxed workspace, and

a Jupyter IPython server to support Python code execution. We instantiate the agent’s workspace

with the source code and the README file generated by the task-specific instructions. This allows

the agent to actively interact with the source code and the static analysis information as it chooses.

Python support also provides the agent with an option to install helper libraries for the PoC crafting

objective such as Pwntools, Scapy etc. For each candidate PoC generated by the agent, it undergoes

a validation run in a test environment. From the test environment, the agent receives dynamic

feedback specific to the validation run. This feedback provides further guidance to the agent

about its effort to generate a crashing PoC. For the PoC generation task, we used an open-sourced

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 11

| Program Analysis Guided LLM Agent for Proof-of-Concept Generation | 11 |
| --- | --- |
| Vulnerability Type | Candidate PoC |

Profiler &

Source Sanitizer- Instrumented Dynamic

Coverage

Code based Build Binary Feedback

Extractor

Fig. 6. Overview of Dynamic Analysis Guidance Component

Algorithm 3 Dynamic Analysis Guidance Component

Input: Source Code 𝑆 , Candidate PoC 𝑝𝑜𝑐 , Vulnerability Type 𝑉 𝑡

Output: Dynamic Feedback dynamic_feedback

1: // Phase 0: Prepare Test Environment (One-Time)

2: 𝑠 ← Assign_Sanitizer( 𝑉 𝑡 )

3: 𝑆 𝑏 ← Build_with_Sanitizer( 𝑆 , 𝑠 )

4: while agent ← Blocking_Recv( candidate_poc ) do

| 5: | dynamic_feedback | ← | 𝜙 |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6: | // Phase 1: Run the PoC |  |  |  |  |  |  |  |  |  |  |  |
| 7: | ( | ex | , | 𝑅 | ) | ← | Execute( | 𝑆 | 𝑏 | , | candidate_poc | ) |
| 8: | if | ex | = | 0 | then |  |  |  |  |  |  |  |
| 9: | // Phase 2: Profiling & Coverage Extractor |  |  |  |  |  |  |  |  |  |  |  |
| 10: | profentry | ← | Detect_Runtime_Entrypoint( | 𝑅 | , | candidate_poc | ) |  |  |  |  |  |
| 11: | profexec | ← | Collect_Execution_Time( | 𝑅 | , | candidate_poc | ) |  |  |  |  |  |
| 12: | prof | = | ( | profexec | , | profentry | ) |  |  |  |  |  |
| 13: | covinfo | ← | Collect_Coverage( | 𝑅 | , | candidate_poc | ) |  |  |  |  |  |
| 14: | cov | ← | Generate_Report_File( | covinfo | ) |  |  |  |  |  |  |  |
| 15: | dynamic_feedback | ← | ( | ex | , | prof | , | cov | ) |  |  |  |
| 16: | else |  |  |  |  |  |  |  |  |  |  |  |
| 17: | dynamic_feedback | ← | ( | ex | ) |  |  |  |  |  |  |  |
| 18: | end if |  |  |  |  |  |  |  |  |  |  |  |

19: end while

OpenHands [39] generalist agent based on the codeAct architecture. It supports code-based actions

through LLM tool calls.

3.3 Dynamic Analysis Guidance

For the PoC generation task, the vulnerability report produced by static analysis provides the

agent with relevant information to understand the vulnerability. Generally, the agent uses it as a

starting point to understand the vulnerability in detail and the code path that reaches the vulnerable

code location. This combination may not be enough to generate a PoC if the agent’s analysis is

imprecise. LLM agents are adept at analyzing the code but they lack consistent precision across

their execution runs. The lack of precision in extracting critical information from the source often

leads the agent’s strategy to deviate from generating the correct PoC. It is possible that the agent

can recover from the incorrect strategy by correcting a code analysis error or a flawed assumption

by itself. However, multiple sources of imprecision and their cascading effects make it difficult for

the agent to localize and prioritize them in its strategy. To address this issue, we perform dynamic

analysis on the validation binary and candidate PoC generated by the agent. The dynamic analysis

produces profiling information and coverage information. The profiling information provides

execution time and the triggered binary entrypoint from the concrete PoC execution run. The

coverage information provides file names, function coverage, line coverage, region coverage, and

branch coverage for the concrete PoC execution run. This provides the agent with a factual source

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 12

12 Achintya Desai, Md Shafiuzzaman, Wenbo Guo, and Tevfik Bultan

of feedback for localizing flaws and sources of imprecision in its reasoning. Once the agent recovers

from its errors using the dynamic analysis guidance, it can iteratively refine the PoC input to

improve coverage of the vulnerable code location identified in the vulnerability report.

3.3.1 Sanitizer-based Build. For a given vulnerability report, once the agent generates a candidate

PoC, it may not always be accurate. Automatically validating the candidate PoC provided by the

agent on a test environment is an important step in the PoC generation process. The instrumented

binary is built from the source code and equipped with a sanitizer associated with the vulnerability

type mentioned in the vulnerability report. AddressSanitizer is the default sanitizer and covers most

memory corruption vulnerabilities, such as overflows and out-of-bounds accesses. MemorySanitizer

is integrated for detecting uninitialized memory vulnerabilities. UndefinedBehaviorSanitizer is

integrated to detect undefined program behavior vulnerabilities, such as division by zero, integer

overflows, and null pointer dereferencing. The test environment takes a potential PoC as input,

runs a concrete execution through the instrumented binary, and returns the execution result. If the

PoC triggers a crash during execution, the testing environment returns the associated non-zero

exit code and the crash report. If the PoC does not trigger the crash, the exit code 0 is returned

to the agent along with profiling and coverage information. The agent can interact with the test

environment through a ‘submit’ bash script provided in the agent’s workspace. The result of the

PoC execution in the test environment is modeled as a response to the agent submission. This

provides the agent with a feedback on its PoC generation attempt, which it uses to refine or rewrite

the candidate PoC.

3.3.2 Profiler & Coverage Extractor. The exit code of a concrete execution of the candidate PoC

provides the agent with feedback on whether the PoC is correct. Although the exit code is helpful

in validating a PoC, it is not useful to guide the agent towards our objective. During concrete

execution, it is possible to observe the runtime behavior of the program beyond the exit code. In

fact, there is a wide variety of profiling information, such as CPU and memory usage, that can

be collected at runtime. For the PoC generation task, we focus on the execution time and binary

entrypoint associated with the candidate PoC execution. The goal of the profiling information is to

provide the agent with simplified and unambiguous feedback. Specially for deep vulnerabilities,

the execution time allows the agent to infer whether the candidate PoC is potentially rejected by

a shallow code condition. Moreover, the taint path generated during the static analysis provides

the function-level taint. It is possible to have a single function entrypoint definition present across

multiple source files, especially if the entrypoint is a fuzzing driver. In such cases, the agent is

unable to distinguish between the entrypoint present in the test environment. To counter this

issue, the binary entrypoint with its filename is collected as part of profiling information. The

profiling information is encoded alongside the exit code as a message-based response from the test

environment to the agent. Coverage information is collected in the form of file name, function name,

region coverage, line coverage, and branch coverage. Region coverage provides the percentage

of code regions that have been executed at least once. Line coverage provides the percentage of

executable lines of code that have been executed at least once. Branch coverage indicates whether

each branch outcome is covered by the input. Region and Line coverage are useful in assessing

whether the PoC is reaching the vulnerable code region. Branch coverage helps assess which code

branches may not have been executed by the potential PoC, thereby indicating a lack of progress

towards achieving coverage along the possible PoC execution path. Consider the following coverage

information entry from a candidate PoC generated by the agent for a vulnerability(Arvo:40683) in

the Binutils project.

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 13

Program Analysis Guided LLM Agent for Proof-of-Concept Generation 13

Coverage Entry: :{" file_path ":"/ src / binutils - gdb / bfd / vms - alpha .c " ," function_name ":" vms - alpha .c:

_bfd_vms_slurp_eisd " ," region_coverage ":10.08 ," line_coverage ":19.00 ," branch_coverage

":3.57} ,

THOUGHT : _bfd_vms_slurp_eisd coverage is only 10%. That means its barely entered . That suggests

the ISD parsing fails early . Indeed , we placed a zero terminator at offset 544 ,...

Listing 6. Coverage Entry and Agent log for Arvo:40683 vulnerability in binutils project

Based on the coverage information reported, the agent infers the parsing failure and spots the issue

with the candidate PoC. In summary, dynamic analysis allows the agent to gain additional insight

into the candidate PoC by executing the instrumented binary. The agent is able to use these insights

to refine the PoC towards reaching the vulnerable code location to trigger the vulnerability.

4 Evaluation

4.1 Experimental Setup

4.1.1 Dataset. To evaluate the effectiveness of PAGENT, we used the ARVO [28] (Atlas of Re-

producible Vulnerabilities for Open source software) instances from the Cybergym [40] dataset.

ARVO consists of real-world OSS-Fuzz vulnerabilities [14] with containerized build environments

that enable deterministic recompilation of both vulnerable and patched program versions. Each

vulnerability instance includes a triggering input and the corresponding developer patch, providing

an execution-based ground truth for evaluation of automated PoC generation. We chose the ARVO

dataset for three key reasons aligned with the hybrid design of PAGENT. First, ARVO consists of

vulnerabilities identified by OSS-Fuzz across open-source C/C++ projects, capturing the essence

of real-world vulnerabilities for the PoC generation task. Access to source code and a reliable

recompilation system allows us to inject custom instrumentation for dynamic analysis directly into

the build process, which is essential for the agent’s feedback loop. ARVO also provides access to

both vulnerable and patched versions of the source code which allows us to assess the potential of

PAGENT to construct PoCs that persist in the patched version of the source code.

Our evaluation dataset comprises 203 distinct vulnerabilities drawn from ten widely deployed

C/C++ open-source projects. As summarized in Table 1, the dataset spans diverse domains, includ-

ing GNU binary tools, CAD processing, multimedia frameworks, and security. The distribution

is dominated by binutils (51.72%), which provides a challenging testbed due to its complex

parsing logic and structured binary inputs. The remaining projects, such as ( libredwg , gpac , and

selinux ), ensure evaluation across heterogeneous codebases with varied control-flow and input-

processing characteristics. The vulnerabilities primarily correspond to different kinds of memory

corruptions, such as buffer overflows, out-of-bounds access, and undefined behaviors, such as

integer overflows, which are detectable by AddressSanitizer (ASan), MemorySanitizer (MSan), and

UndefinedBehaviorSanitizer (UBSan).

4.1.2 Implementation Details of PAGENT. We implemented PAGENT to work on source code

written in C/C++. We used clang-14 to compile the source code into LLVM-IR. Implementation

of the static analysis component uses LLVM’s pass infrastructure for lightweight static analysis.

We wrote the vulnerability rules as an analysis with the cclyzerpp [5] tool. Primarily, we use

cclyzerpp’s fact generation phase and Soufflé [17] to deploy our rules. For the PoC generation agent,

we use OpenHands [39] implementation of LLM agent based on the CodeAct architecture [27]. For

dynamic analysis, we use frontend-based instrumentation supported by clang to generate source

line-based coverage information. We use Python scripts and JSON files to enable automated artifact

sharing between components.

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 14

14 Achintya Desai, Md Shafiuzzaman, Wenbo Guo, and Tevfik Bultan

Table 1. Evaluation dataset

| Project | # Vulns | # PAGENT | # GPT5 Agent | LoC | Domain |  |
| --- | --- | --- | --- | --- | --- | --- |
| binutils | 105 | 64 | 19 | ∼ | 3762K | GNU binary tools |
| libredwg | 29 | 17 | 9 | ∼ | 889K | CAD Library |
| gpac | 23 | 14 | 10 | ∼ | 925K | Multimedia |
| selinux | 17 | 11 | 8 | ∼ | 205K | Security |
| libucl | 5 | 5 | 4 | ∼ | 2886K | Configuration Library |
| libsndfile | 8 | 5 | 1 | ∼ | 234K | Audio Library |
| mosquitto | 5 | 5 | 2 | ∼ | 66K | IoT protocol |
| kamailio | 4 | 4 | 3 | ∼ | 276K | VoIP and real-time communications |
| miniz | 3 | 2 | 0 | ∼ | 133K | Data Compression Library |
| faad2 | 4 | 3 | 0 | ∼ | 274K | Digital Audio & Multimedia |
| Total | 203 | 130 | 56 | – | – |  |

To simulate a realistic security analysis workflow, we construct the experimental environment

using only the information available prior to the fix. For each vulnerability instance, we ensure the

following properties are satisfied

• Vulnerable Codebase: The full source code at the revision immediately preceding the fix is

available to PAGENT.

• Build Instructions: We use the build instructions for each project from OSS-Fuzz to compile

the source code to LLVM-IR.

• Code Location: We extract the code location from ARVO’s crash report and make it available

to PAGENT. Note that we only use the code location as input and nothing more from the

crash report.

• Test Environment Generation: We utilize ARVO’s existing Dockerized build to compile

the codebase with sanitizer flags for the test environment.

• Ground Truth Isolation: While ARVO provides a fuzzer-generated PoC and the fix commit,

these are strictly withheld from the agent.

All experiments were conducted on a machine equipped with a 13th Gen Intel Core i9-13900K CPU

(3.00 GHz) and 192 GB of RAM, running Ubuntu 22.04.4 LTS.

4.1.3 Baselines. Based on the chosen dataset, we compared our approach with existing best-

performing LLM agents from Cybergym [40]. Each Cybergym agent can be configured to run

with an increasing level of information. At level 0, the agents only have access to the source code

and nothing else. At level 1, the agents have access to the source code and text description of the

vulnerability. The results obtained by Cybergym agents at levels 0 and 1 are significantly lower

than those achieved by our PAGENT tool. Instead, we compare PAGENT with cybergym agents

that have access to the source code, a text description, and a stack trace obtained by executing the

ground-truth PoC (level-2). Note that PAGENT takes only the source code and the code location

as input and does not have access to the text description of the vulnerability or the stack trace

obtained by executing the ground-truth PoC.

Additionally, we compare PAGENT with two prior agentic approaches to PoC generation: PoCGen

and Faultline. The PoCGen approach [38] is designed for automatically generating PoCs from textual

vulnerability descriptions. It uses LLMs to extract vulnerability-specific information, such as the

type and vulnerable function from the source code. PoCGen also uses static analysis to fetch the

taint path and usage snippets from the source code. If static analysis fails to produce a taint path,

it generates it using a combination of static and dynamic taint tracking guided by the LLM. This

information is collectively fed to an LLM for generating an exploit, which undergoes concrete

execution for validation. Upon failure, it provides additional code context and runtime information,

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 15

Program Analysis Guided LLM Agent for Proof-of-Concept Generation 15

DeepSeek-3.1 DeepSeek-3.2

80

64 . 6

60

| 45 | . | 1 | 42 | . | 3 |  |
| --- | --- | --- | --- | --- | --- | --- |
| 40 | 33 | . | 9 | 36 | . | 7 |
| 28 | . | 6 | 28 | . | 7 |  |
| PoC Success Rate (%) | 20 | 14 | . | 6 |  |  |

0

Agent SA + Agent DA + Agent DA + SA + Agent

Fig. 7. PoC success rates (%) versus agent guidance levels within PAGENT

such as an error message and coverage information, to the LLM. Our approach takes the source

code and code location as input, where as PoCGen relies on the source code and text description of

the vulnerability. The main difference between PoCGen and our approach is the design and usage

of the static analysis. Our static analysis phase ensures that the vulnerability-specific information is

generated prior to the LLM’s involvement, which is prone to inconsistency with its reasoning. The

vulnerability report generated by our static analysis provides a reliable foundation for the agent

to generate a candidate PoC. Furthermore, our approach ensures the LLM agent has the freedom

to interact with the source code as it deems necessary, instead of static refinement steps with the

prompt. Since the PocGen approach was originally developed to generate exploits specifically for

Npm packages, we reimplemented it within our framework to compare its effectiveness.

We also compare PAGENT with the Faultline approach [29]. Like PoCGen, Faultline takes source

code and a textual vulnerability description as input and attempts to automatically generate a

PoC. Faultline is based on a 3-phased agentic pipeline involving tracing the dataflow from source

to sink, reasoning about branch conditions, and PoC generation with repair feedback. Faultline’s

agentic approach allows it to perform staged reasoning on the source code. Lack of static analysis

in Faultline results in poor precision due to multiple sources of inconsistency in the agent’s code

analysis. Compared to our approach, it also does not include dynamic analysis feedback to repair

the PoC.

4.2 Experiments

We experimentally evaluated PAGENT with the following research questions:

• RQ1: Is PAGENT more effective at the PoC generation task compared to baselines?

• RQ2: How much does each component of PAGENT contribute to the overall result?

• RQ3: Does PAGENT find any post-patch vulnerabilities?

4.2.1 Effectiveness (RQ1). We evaluate PAGENT’s performance based on the successful PoCs

generated for vulnerabilities in the dataset. A PoC is considered successful if it produces a crash

during the concrete execution on the sanitizer-instrumented binary in the test environment. We

detect a crash through a non-zero exit code. For crashes with an exit code other than 1, we inspected

the PoCs manually and checked the crash report it generates to determine whether the correct

vulnerability was triggered. The availability of ground truth in the ARVO dataset allows us to

compare the PoCs and the expected crash report, which includes details such as the stack trace,

sanitizer report, etc. We chose DeepSeek3.1-termius [22](DS3.1) and DeepSeek3.2 [23](DS3.2) as

the LLM models for PAGENT. DeepSeek models are open-sourced. Although open-sourced models

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 16

| 16 | Achintya Desai, Md Shafiuzzaman, Wenbo Guo, and Tevfik Bultan |  |  |
| --- | --- | --- | --- |
| Baselines | PAGENT | Baselines | PAGENT |
| 140 | 140 |  |  |
| 130 | 130 |  |  |
| 120 | 120 |  |  |
| 100 | 100 |  |  |

86

80 80

68

| 60 | 55 | 56 | 60 | 56 |
| --- | --- | --- | --- | --- |
| # Successful PoCs | 50 | # Successful PoCs |  |  |
| 40 | 38 | 40 |  |  |

21

20 18 20

0 0

Claude3.7 Claude4 GPT4.1 GPT5 DS3.1 DS3.2

PAGENT (DS3.1) PAGENT (DS3.2) Faultline (DS3.2) PoCGen (DS3.2) PAGENT (DS3.2)

(a) Cybergym LLM Agents vs PAGENT (b) Faultline vs PoCGen vs PAGENT

Fig. 8. Comparison of PoC Success counts

Baselines PAGENT

Baselines PAGENT

40

40 40

32

30

23

20

| 20 | 18 | 20 |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | # Successful PoCs |  |  |  |  |  |  |  |
| # Exclusive PoCs | 10 | 7 | 9 | 7 | 7 | 8 | 7 | 8 |

3

0 0

Claude4 GPT5 DS3.2 Claude4 GPT5 DS3.1 DS3.2

Claude4 + GPT5 Claude4 + DS3.2 DS3.2 + GPT5

PAGENT (DS3.1) PAGENT (DS3.2) PAGENT (DS3.1) PAGENT (DS3.2)

(a) Comparison of exclusive PoC generation (b) Comparison of Post-Patch vulnerabilities

Fig. 9. Comparisons between exclusive PoCs and post-patch vulnerabilities across agents

are generally considered weaker than their closed-sourced counterparts, they provide practical

deployment advantages in terms of data privacy, fine-tuning, and cost-effectiveness. For example,

the cost of output tokens for the API access with DeepSeek is almost 33 times (0.42$ vs 14.00$ per

million tokens) lower than closed-sourced LLMs such as GPT-5, Sonnet-4.

Figure 8a showcases the overall improvement at the PoC generation task by PAGENT compared

to the top 4 best-performing LLM agents from Cybergym. Notice that DS3.1 based cybergym agent

is one of the worst-performing agents on the benchmark. With our approach, it outperforms each

cybergym agent by at least 53%. Compared to GPT-5, GPT-4.1, Claude-4, and Claude-3.7 based

agents, DS3.1 based PAGENT showcases 53.57%, 309.5% 56.36%, 126.36% improvement respectively.

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 17

Program Analysis Guided LLM Agent for Proof-of-Concept Generation 17

The DeepSeek3.2-based PAGENT further outperforms all cybergym agent baselines by at least

132%. The significant improvement demonstrated by PAGENT establishes the merit of the hybrid

approach over unguided agentic approaches.

Figure 9a demonstrates the exclusive results by GPT-5 and Claude-4 based cybergym agents

and their combinations. A PoC is counted as exclusive if it is generated by one of the agents in

its group and no other present in the graph. Each bar in Figure 9a represents the number of PoCs

generated by the labelled agent group and no other. Notice that the number of PoCs generated by

PAGENT with Deepseek3.1 alone exceeds that of any combination of the top-3 cybergym agents.

This remarkable improvement demonstrates the strengths of the PAGENT approach in generating

vulnerabilities that no other LLM agent or agent combination can. Furthermore, the PAGENT

approach with DeepSeek-3.2 achieves twice the PoC generation success rate as other agents or

their combinations.

4.2.2 Ablation study (RQ2). We define three variants used in the ablation study as follows:

• No Guidance variant: Both static and dynamic analysis components were disabled.

• SA only variant: Dynamic analysis component was disabled.

• DA only variant: Static analysis component was disabled.

To assess the contribution of each component in PAGENT, we performed an ablation study with

the DeepSeek models. Figure 7 demonstrates that both the static and dynamic analysis components

almost equally improve the PoC generation success rate of the PAGENT. Specifically, the static

analysis component provides improvements of 132.9% and 57.69% over the non-guided variant

across both DS3.1 and DS3.2 models, respectively. Removing the dynamic analysis component from

PAGENT reduces the number of PoCs found by approximately 25% and 42% across both DS3.1 and

DS3.2 models, respectively. This reduction in the effectiveness demonstrates contributions of both

static and dynamic analysis to the PAGENT.

4.2.3 Post-patch vulnerabilities (RQ3). Although the PoC generation task in our experiment setup

focuses on generating PoC for a vulnerable version of the source code, the agent can generate a

PoC input that can crash on the patched version of the source code if it is vulnerable. Due to the

structure of the ARVO dataset, we were able to test the crashing input on the post-patch version of

the source code. We identify such PoCs that crash on the post-patch version as post-patch PoCs.

Figure 9b showcases the results of finding post-patch PoCs with PAGENT. PAGENT generates

almost 3 times as many post-patch PoCs as any other baseline agent. The presence of post-patch

vulnerabilities signifies one of the following: 1) The patch is incomplete, and the vulnerability

still survives, 2) PAGENT discovered a vulnerability that the patch does not cover. Based on our

assessment of PAGENT logs, the main source for discovering post-patch PoCs is dynamic analysis.

Recall that for each candidate PoC, dynamic analysis provides coverage information to the agent.

This causes the agent to optimize for maximal coverage, especially regional coverage, along the

path to the assigned vulnerability. In doing so, it produces PoCs that reach parts of the code that

may not be related to the vulnerability. If the reached code region contains a hidden vulnerability,

the PoC may trigger it, leading to a post-patch PoC.

4.2.4 Threats to Validity. The results presented in this work are subject to several threats to validity.

First, the effectiveness of PAGENT relies upon the accuracy of vulnerability rules; if a vulnerability

type is not covered by the static analysis rules, PAGENT will not be able to identify the vulnerability

and craft a PoC. Second, we experimented with PAGENT on 10 diverse open-source software. It is

likely that the underlying LLMs (DeepSeekV3.1 and DeepSeekV3.2) have encountered the source

code during their training, which can make their code reasoning ability seem dependent on the

visibility of software. Although this may limit the applicability of PAGENT, the burden of precise

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 18

18 Achintya Desai, Md Shafiuzzaman, Wenbo Guo, and Tevfik Bultan

code reasoning on the LLM agent is already reduced by guidance from static and dynamic analyses.

For unseen software, the agent’s behavior to refine its analysis on static and dynamic analysis

guidance should remain as the underlying programming language stays the same. Third, it is also

possible that the underlying LLMs may have seen the PoCs for the vulnerability instances from our

experimental dataset during training, enabling LLMs to recall them. However, this is not the case,

as demonstrated by our post-patch vulnerability findings are not in the dataset. The generation of

post-patch vulnerabilities indicates that the PoCs generated by the agent are not always the same

as the ground-truth PoCs. Furthermore, during manual analysis of the PoCs we observed that the

lengths of the PoCs frequently differed compared to the ground truth PoCs suggesting that the

PoCs were crafted by the agent rather than recalling a known PoC.

5 Related Work

Vulnerability Detection. Vulnerability detection has traditionally relied on three major classes

of techniques: static analysis, symbolic execution, and fuzzing. Static analysis [20] scales well to

large codebases but often suffers from high false-positive rates and limited precision. Symbolic

execution [8, 9, 13, 31, 35] provides strong semantic reasoning by deriving path constraints, yet

struggles with path explosion. Fuzzing [6] improves scalability and effectiveness via coverage-guided

exploration, but lacks semantic understanding and often fails to reach deeply nested vulnerabilities.

Recent systems [34, 36] combine these techniques to balance scalability and precision, but they

typically operate as standalone analysis tools and do not directly address automated PoC generation.

PoC Generation. A growing line of work explores using LLMs to generate bug reproduction tests

from natural-language reports. LIBRO [18] frames this task as few-shot code generation, while

follow-up work [10] introduces agentic workflows with fine-tuned code-editing tools. Otter [2]

further employs systematic reasoning to generate reproduction tests. However, bug reproduction

differs fundamentally from exploit-oriented PoC generation: reproducing a bug often requires

invoking a faulty function, whereas PoC generation for vulnerabilities requires crafting inputs that

traverse long and complex execution paths to trigger security-critical behaviors. EniGMA [1] is a

related agentic work that solves CTF challenges, however, their success is measured by retrieving a

flag string rather than constructing executable PoCs. PoCGen [38] is a recent work that generates

PoCs for vulnerabilities in NPM packages using dynamic and static analysis customized to JavaScript.

In contrast, PAGENT targets native binaries and API-driven vulnerabilities and is not restricted to

a single ecosystem.

LLMs and Agentic Systems in Software Engineering. LLMs have been widely adopted across

software engineering tasks, including code generation [30], test generation [33], fuzzing [42], and

automated refactoring [32]. To improve effectiveness in real-world settings, prior work augments

prompts with repository-level context or historical edits. Beyond single-shot prompting, LLM-based

agents introduce multi-step reasoning and tool use such as RepairAgent [7] and SWE-Agent [43].

Unlike prior agentic systems that focus on code editing or repair, PAGENT targets PoC generation

and integrates static and dynamic program analysis as first-class guidance signals within the agent

loop. To the best of our knowledge, PAGENT is the first LLM-based agentic system that tightly

couples program analysis with iterative PoC synthesis at scale.

6 Conclusion

For a given software with a vulnerability, automatically generating a Proof of Concept (PoC) input is

a challenging but valuable task. PAGENT addresses the challenges of PoC generation by combining

the strengths of static and dynamic analysis with an LLM agent. Given source code and a potentially

vulnerable code location, PAGENT first applies scalable static analysis to generate a vulnerability

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 19

Program Analysis Guided LLM Agent for Proof-of-Concept Generation 19

report. The vulnerability report is used to automatically generate a candidate PoC via an LLM agent

that has interactive access to the source code. For validation, PAGENT performs dynamic analysis

on the candidate PoC to generate valuable feedback for the LLM agent. The agent uses this feedback

to refine the PoC and to ensure that it can be successfully validated in the test environment. The

PAGENT tool can be integrated into CI/CD software pipelines to run after each commit and assess

the modified code locations for vulnerabilities and corresponding PoCs.

7 Data Availability

The artifact is available at http://anonymous.4open.science/r/PAGENT-6D60

References

[1] T. Abramovich, M. Udeshi, M. Shao, K. Lieret, H. Xi, K. Milner, S. Jancheska, J. Yang, C. E. Jimenez, F. Khorrami,

P. Krishnamurthy, B. Dolan-Gavitt, M. Shafique, K. Narasimhan, R. Karri, and O. Press. EnigMA: Enhanced interactive

generative model agent for CTF challenges. Technical report.

[2] T. Ahmed, J. Ganhotra, R. Pan, A. Shinnar, S. Sinha, and M. Hirzel. Otter: Generating tests from issues to validate swe

patches. arXiv preprint arXiv:2502.05368 , 2025.

[3] H. Aslanyan, H. Movsisyan, H. Hovhannisyan, Z. Gevorgyan, R. Mkoyan, A. Avetisyan, and S. Sargsyan. Combining

static analysis with directed symbolic execution for scalable and accurate memory leak detection. IEEE Access ,

12:80128–80137, 2024.

[4] R. Baldoni, E. Coppa, D. C. D’elia, C. Demetrescu, and I. Finocchi. A survey of symbolic execution techniques. ACM

Computing Surveys (CSUR) , 51(3):1–39, 2018.

[5] L. Barrett and S. Moore. cclyzer++: Scalable and precise pointer analysis for llvm. https://galois.com/blog/2022/08/

cclyzer-scalable-and-precise-pointer-analysis-for-llvm/, 2022.

[6] M. Böhme, C. Cadar, and A. Roychoudhury. Fuzzing: Challenges and reflections. IEEE Software , 38(3):79–86, 2020.

[7] I. Bouzenia, P. Devanbu, and M. Pradel. Repairagent: An autonomous, llm-based agent for program repair. arXiv

preprint arXiv:2403.17134 , 2024.

[8] C. Cadar, V. Ganesh, P. M. Pawlowski, D. L. Dill, and D. R. Engler. Exe: Automatically generating inputs of death. ACM

Transactions on Information and System Security (TISSEC) , 12(2):1–38, 2008.

[9] C. Cadar and K. Sen. Symbolic execution for software testing: three decades later. Communications of the ACM ,

56(2):82–90, 2013.

[10] B. Cheng, K. Wang, L. Shi, H. Wang, Y. Guo, D. Li, and X. Chen. Enhancing semantic understanding in pointer analysis

using large language models. In Proceedings of the 1st ACM SIGPLAN International Workshop on Language Models and

Programming Languages , pages 112–117, New York, NY, USA, Oct. 2025. ACM.

[11] CVE. Cve metrices. https://www.cve.org/about/Metrics, 2026.

[12] S. Feng and C. Chen. Prompting is all you need: Automated android bug replay with large language models. In

Proceedings of the 46th IEEE/ACM International Conference on Software Engineering , pages 1–13, 2024.

[13] P. Godefroid, M. Y. Levin, and D. Molnar. Sage: whitebox fuzzing for security testing. Communications of the ACM ,

55(3):40–44, 2012.

[14] Google. OSS-Fuzz: Continuous fuzzing for open source software. https://google.github.io/oss-fuzz/, 2016. Accessed:

2026-01.

[15] K. Hassler, P. Görz, S. Lipp, T. Holz, and M. Böhme. A comparative study of fuzzers and static analysis tools for finding

memory unsafety in c and c++. arXiv preprint arXiv:2505.22052 , 2025.

[16] S. Jain, A. Dora, K. S. Sam, and P. Singh. Llm agents improve semantic code search. arXiv preprint arXiv:2408.11058 ,

2024.

[17] H. Jordan, B. Scholz, and P. Subotić. Soufflé: On synthesis of program analyzers. In Computer Aided Verification:

28th International Conference, CAV 2016, Toronto, ON, Canada, July 17-23, 2016, Proceedings, Part II 28 , pages 422–430.

Springer, 2016.

[18] S. Kang, J. Yoon, N. Askarbekkyzy, and S. Yoo. Evaluating diverse large language models for automatic and general

bug reproduction. IEEE Transactions on Software Engineering , 2024.

[19] G. Li, M. Sridharan, and Z. Qian. Redefining indirect call analysis with kallgraph. In 2025 IEEE Symposium on Security

and Privacy (SP) , pages 2957–2975. IEEE, 2025.

[20] L. Li, T. F. Bissyandé, M. Papadakis, S. Rasthofer, A. Bartel, D. Octeau, J. Klein, and L. Traon. Static analysis of android

apps: A systematic literature review. Information and Software Technology , 88:67–95, 2017.

[21] X. Lin, Y. Ning, J. Zhang, Y. Dong, Y. Liu, Y. Wu, X. Qi, N. Sun, Y. Shang, K. Wang, et al. Llm-based agents suffer from

hallucinations: A survey of taxonomy, methods, and directions. arXiv preprint arXiv:2509.18970 , 2025.

, Vol. 1, No. 1, Article . Publication date: April 2026.

---

## Page 20

20 Achintya Desai, Md Shafiuzzaman, Wenbo Guo, and Tevfik Bultan

[22] A. Liu, B. Feng, B. Xue, B. Wang, B. Wu, C. Lu, C. Zhao, C. Deng, C. Zhang, C. Ruan, et al. Deepseek-v3 technical

report. arXiv preprint arXiv:2412.19437 , 2024.

[23] A. Liu, A. Mei, B. Lin, B. Xue, B. Wang, B. Xu, B. Wu, B. Zhang, C. Lin, C. Dong, et al. Deepseek-v3. 2: Pushing the

frontier of open large language models. arXiv preprint arXiv:2512.02556 , 2025.

[24] J. Liu, C. S. Xia, Y. Wang, and L. Zhang. Is your code generated by chatgpt really correct? rigorous evaluation of large

language models for code generation. Advances in Neural Information Processing Systems , 36:21558–21572, 2023.

[25] K. Lu. Practical program modularization with type-based dependence analysis. In 2023 IEEE Symposium on Security

and Privacy (SP) , pages 1256–1270. IEEE, 2023.

[26] K. Lu and H. Hu. Where does it go? refining indirect-call targets with multi-layer type analysis. In Proceedings of the

2019 ACM SIGSAC Conference on Computer and Communications Security , pages 1867–1881, 2019.

[27] W. Lv, X. Xia, and S.-J. Huang. Codeact: Code adaptive compute-efficient tuning framework for code llms. arXiv

preprint arXiv:2408.02193 , 2024.

[28] X. Mei, P. S. Singaria, J. Del Castillo, H. Xi, T. Bao, R. Wang, Y. Shoshitaishvili, A. Doupé, H. Pearce, B. Dolan-Gavitt,

et al. Arvo: Atlas of reproducible vulnerabilities for open source software. arXiv preprint arXiv:2408.02153 , 2024.

[29] V. Nitin, B. Ray, and R. Z. Moghaddam. Faultline: Automated proof-of-vulnerability generation using llm agents. arXiv

preprint arXiv:2507.15241 , 2025.

[30] OpenAI. OpenAI Codex CLI: Lightweight coding agent for the terminal. https://github.com/openai/codex, 2025.

Accessed: 2025-05-10.

[31] C. S. Păsăreanu and N. Rungta. Symbolic pathfinder: symbolic execution of java bytecode. In Proceedings of the 25th

IEEE/ACM International Conference on Automated Software Engineering , pages 179–180, 2010.

[32] D. Pomian, A. Bellur, M. Dilhara, Z. Kurbatova, E. Bogomolov, T. Bryksin, and D. Dig. Next-generation refactoring:

Combining llm insights and ide capabilities for extract method. In 2024 IEEE International Conference on Software

Maintenance and Evolution (ICSME) , pages 275–287. IEEE, 2024.

[33] G. Ryan, S. Jain, M. Shang, S. Wang, X. Ma, M. K. Ramanathan, and B. Ray. Code-aware prompting: A study of

coverage-guided test generation in regression setting using llm. Proceedings of the ACM on Software Engineering ,

1(FSE):951–971, 2024.

[34] S. Saha, L. Sarker, M. Shafiuzzaman, C. Shou, A. Li, G. Sankaran, and T. Bultan. Rare path guided fuzzing. In proceedings

of the 32nd ACM sigsoft international symposium on software testing and analysis , pages 1295–1306, 2023.

[35] K. Sen, D. Marinov, and G. Agha. Cute: A concolic unit testing engine for c. ACM SIGSOFT software engineering notes ,

30(5):263–272, 2005.

[36] M. Shafiuzzaman, A. Desai, L. Sarker, and T. Bultan. STASE: Static analysis guided symbolic execution for UEFI

vulnerability signature generation. In Proceedings of the 39th IEEE/ACM International Conference on Automated Software

Engineering , pages 1783–1794, 2024.

[37] B. Shastry, M. Leutner, T. Fiebig, K. Thimmaraju, F. Yamaguchi, K. Rieck, S. Schmid, J.-P. Seifert, and A. Feldmann.

Static program analysis as a fuzzing aid. In International Symposium on Research in Attacks, Intrusions, and Defenses ,

pages 26–47. Springer, 2017.

[38] D. Simsek, A. Eghbali, and M. Pradel. Pocgen: Generating proof-of-concept exploits for vulnerabilities in npm packages.

arXiv preprint arXiv:2506.04962 , 2025.

[39] X. Wang, B. Li, Y. Song, F. F. Xu, X. Tang, M. Zhuge, J. Pan, Y. Song, B. Li, J. Singh, et al. Openhands: An open platform

for ai software developers as generalist agents. arXiv preprint arXiv:2407.16741 , 2024.

[40] Z. Wang, T. Shi, J. He, M. Cai, J. Zhang, and D. Song. Cybergym: Evaluating ai agents’ cybersecurity capabilities with

real-world vulnerabilities at scale. arXiv preprint arXiv:2506.02548 , 2025.

[41] V. Wüstholz and M. Christakis. Targeted greybox fuzzing with static lookahead analysis. In Proceedings of the ACM/IEEE

42nd International Conference on Software Engineering , pages 789–800, 2020.

[42] C. S. Xia, M. Paltenghi, J. Le Tian, M. Pradel, and L. Zhang. Fuzz4all: Universal fuzzing with large language models. In

Proceedings of the IEEE/ACM 46th International Conference on Software Engineering , pages 1–13, 2024.

[43] J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, and O. Press. Swe-agent: Agent-computer interfaces

enable automated software engineering. Advances in Neural Information Processing Systems , 37:50528–50652, 2024.

[44] W. Zhang, Y. Sun, P. Huang, J. Pu, H. Lin, and D. Song. Mirage-bench: Llm agent is hallucinating and where to find

them. arXiv preprint arXiv:2507.21017 , 2025.

[45] Y. Zheng, Z. Song, Y. Sun, K. Cheng, H. Zhu, and L. Sun. An efficient greybox fuzzing scheme for linux-based iot

programs through binary static analysis. In 2019 IEEE 38th International Performance Computing and Communications

Conference (IPCCC) , pages 1–8. IEEE, 2019.

, Vol. 1, No. 1, Article . Publication date: April 2026.

---
title: "When Fuzzing Meets LLMs: Challenges and Opportunities"
creator: "LaTeX with acmart 2023/12/29 v2.01 Typesetting articles for the Association for Computing Machinery and hyperref 2023-04-22 v7.00x Hypertext links for LaTeX"
pages: 5
---

# When Fuzzing Meets LLMs: Challenges and Opportunities

> **總頁數**：5 頁

---

## Page 1

When Fuzzing Meets LLMs: Challenges and Opportunities

Yu Jiang*, Jie Liang*, Fuchen Ma*, Yuanliang Chen*, Chijin Zhou*, Yuheng Shen*

Zhiyong Wu*, Jingzhou Fu*, Mingzhe Wang*, ShanShan Li

*School of Software, Tsinghua University.

Zhang*. 2024. When Fuzzing Meets LLMs: Challenges and Opportunities. In

Proceedings of ACM Conference (FSE’24). ACM, New York, NY, USA, 5 pages.

https://doi . org/10 . 1145/nnnnnnn . nnnnnnn

From natural language processing [7, 22, 27] to code generation [19,

degradation, manifesting as high false positives, low test coverage,

and limited scalability.

In this paper, we identify five common challenges when using

required for effective bug detection. 2) Secondly, these models

capabilities, constraining their utility in diverse fuzzing scenarios.

Permission to make digital or hard copies of all or part of this work for personal or

classroom use is granted without fee provided that copies are not made or distributed

for profit or commercial advantage and that copies bear this notice and the full citation

on the first page. Copyrights for components of this work owned by others than the

republish, to post on servers or to redistribute to lists, requires prior specific permission

FSE’24, July 2024, Porto de Galinhas, Brazil

†

, Quan Zhang*

† National University of Defense Technology.

one of these challenges. 1

cations in three key fuzzing steps. These findings inspire us with

some opportunities for better usage of LLM in each fuzzing step

according to whether the corresponding corpus and documentation

are rich. Furthermore, we performed some preliminary evalua-

Target

Program Driver Synthesis Input Generation Bug Detection Bug

Report

Fuzzing Loop

Challenges Diversity Understanding

Validity

Large Language Model

Understanding Corpus

Figure 1: Fuzzing Workflow with LLM enhanced.

2.1 Driver Synthesis

| ABSTRACT | 3) Thirdly, LLMs struggle with generating sufficiently diverse in- |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Fuzzing, a widely-used technique for bug detection, has seen ad- | puts during the fuzzing process, which is critical for thorough and |  |  |  |  |  |  |
| vancements through Large Language Models (LLMs). Despite their | effective bug detection. 4) Fourthly, they face challenges in main- |  |  |  |  |  |  |
| potential, LLMs face specific challenges in fuzzing. In this paper, | taining the validity of generated inputs, a crucial factor for accurate |  |  |  |  |  |  |
| we identified five major challenges of LLM-assisted fuzzing. To | and reliable fuzzing. 5) Lastly, LLMs’ inaccurate understanding of |  |  |  |  |  |  |
| support our findings, we revisited the most recent papers from top- | bug detection mechanisms hinders their ability to identify and ad- |  |  |  |  |  |  |
| tier conferences, confirming that these challenges are widespread. | dress complex software vulnerabilities effectively, thereby limiting |  |  |  |  |  |  |
| As a remedy, we propose some actionable recommendations to | their overall effectiveness in the fuzzing process. We performed a |  |  |  |  |  |  |
| help improve applying LLM in Fuzzing and conduct preliminary | comprehensive survey and revisited most recent fuzzing works that |  |  |  |  |  |  |
| evaluations on DBMS fuzzing. The results demonstrate that our | rely on LLM for tackling different problems in the fuzzing process. |  |  |  |  |  |  |
| recommendations effectively address the identified challenges. | To our surprise, the results show that each work encounters at least |  |  |  |  |  |  |
| ACM Reference Format: | Although LLMs are widespread, it is more important for us to |  |  |  |  |  |  |
| Yu Jiang*, Jie Liang*, Fuchen Ma*, Yuanliang Chen*, Chijin Zhou*, Yuheng | avoid its weakness, and at the same time take advantage of its |  |  |  |  |  |  |
| Shen* and Zhiyong Wu*, Jingzhou Fu*, Mingzhe Wang*, ShanShan Li | † | , Quan | strengths. To this end, we perform an impact analysis of the impli- |  |  |  |  |
| 1 | INTRODUCTION | tions according to these opportunities by applying LLM in fuzzing |  |  |  |  |  |
| Fuzzing is a promising technique for software bug detection [8, 26]. | database management systems(DBMS). The results demonstrate |  |  |  |  |  |  |
| Large Language Models (LLM) are rapidly gaining popularity across | that the reasonable instantiation of those recommendations can |  |  |  |  |  |  |
| various applications for their versatility and capability [14, 15]. | overcome the challenges in LLM-assisted DBMS fuzzing. |  |  |  |  |  |  |
| 24], LLM’s broad utility is making it a prominent and sought-after | 2 | CHALLENGES AND OPPORTUNITIES |  |  |  |  |  |
| solution in diverse domains. This development has naturally influ- | Despite that LLM have achieved great success, the application of |  |  |  |  |  |  |
| enced fuzzing research: to help improve the fuzzing effectiveness, | LLM in fuzzing is often prone to several problems, ranging from |  |  |  |  |  |  |
| LLM has now become one of the key enablers to assist the core | deduction accuracy to adapt scalability. Overlooking these issues |  |  |  |  |  |  |
| processes of fuzzing, including driver synthesis [28, 39], input gen- | may result in poor seed quality or omitting critical bugs, leading to a |  |  |  |  |  |  |
| eration [9, 10], and bug detection [11, 17]. | limited fuzzing performance. In this section, we summarize the five |  |  |  |  |  |  |
| While excelling in natural language analysis, LLM encounters | challenges that commonly occur when applying LLM in fuzzing. |  |  |  |  |  |  |
| some common pitfalls like limited context length [20] and hallu- | While these challenges might initially appear straightforward, they |  |  |  |  |  |  |
| cination problems [16, 23, 31], etc. Consequently, LLM exhibits | usually stem from small shortcomings that are typical in fuzzing. |  |  |  |  |  |  |
| limitations in complex program analysis. These pitfalls of LLM | We group these challenges with respect to the states of a typical |  |  |  |  |  |  |
| affect the effectiveness of fuzzing, leading to testing performance | fuzzing workflow, as depicted in Figure 1. |  |  |  |  |  |  |
| arXiv:2404.16297v1 [cs.SE] 25 Apr 2024 | LLM-based fuzzing technology: 1) Firstly, they often produce low- | C1.1: Prone to Error | C2.1: Insufficient | C3.1: Inaccurate |  |  |  |
| quality outputs in fuzzing driver synthesis, lacking the precision | C1.2: Limited Scope | C2.2: Limited |  |  |  |  |  |
| demonstrate a limited scope in their understanding and processing | Prompt | Hallucination | Limited Long-text | Limited Training |  |  |  |
| author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or | Description. | Recently, several pioneer works have been pro- |  |  |  |  |  |
| and/or a fee. Request permissions from permissions@acm.org. | posed to utilize LLMs to enhance driver synthesis [11, 12, 28, 38, 39]. |  |  |  |  |  |  |
| © 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM. | 1 | Remark: The purpose of this work is not to point fingers or critique. Instead, it wants |  |  |  |  |  |
| ACM ISBN 978-x-xxxx-xxxx-x/YY/MM | to show how we can overcome the challenges of LLM-assisted fuzzing and effectively |  |  |  |  |  |  |
| https://doi | . | org/10 | . | 1145/nnnnnnn | . | nnnnnnn | leverage the advantages of LLMs and make it truly beneficial for the fuzzing process. |

---

## Page 2

| FSE’24, July 2024, Porto de Galinhas, Brazil | Jiang et al. |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Their basic idea is to use API documentation as the prompt context, | problems and generate a completely non-existent driver. Instead, |  |  |  |  |
| and then ask LLMs to generate API invoking sequences as fuzzing | the project | typst | has lots of documents and unit tests. Feeding |  |  |
| drivers. For example, both TitanFuzz [11] and PromptFuzz [28] | these materials that illustrate the usage of the functions is helpful |  |  |  |  |
| design customized prompt templates to guide LLMs in generating | for LLMs to generate effective drivers [35]. Additionally, it is also |  |  |  |  |
| code that follows programming syntax and semantics. | feasible to iteratively query LLMs to address any errors that may |  |  |  |  |
| Challenges. | The application of LLMs to driver synthesis can be | be present in the drivers. |  |  |  |
| ineffective if done directly, as LLMs have a tendency to produce hal- | REC 1.3 | Sometimes, even with adequate documentation and |  |  |  |
| lucinations [7, 20] and perform less effectively on programs that are | examples, LLMs can still encounter challenges in generating valid |  |  |  |  |
| not included in their training corpus [20]. These limitations present | drivers at times, especially for extremely complex targets like Linux |  |  |  |  |
| two challenges for driver synthesis. The first one is that the synthe- | kernel. These systems frequently involve intricate dependencies |  |  |  |  |
| sized drivers are | prone to error | , leading to a non-negligible number | among their APIs, or there exist implicit dependencies among lower- |  |  |
| of false positives during fuzzing. For example, according to com- | level systems that pose challenges for LLM to capture. | For these |  |  |  |
| prehensive evaluation on LLM-based driver synthesis for OSS-Fuzz | targets, it is advisable to refrain from relying on LLMs. Instead, it is |  |  |  |  |
| projects [39], GPT-4 can correctly generate roughly 40% drivers, | more practical and feasible to explore conventional methods. |  |  |  |  |
| while the rest of the drivers contain errors. Among the erroneous | For example, KSG [33] uses the ebpf to dynamically infer the |  |  |  |  |
| drivers, 93% exhibit one or more of the following issues: type errors, | kernel’s system call argument type and value constraints. In con- |  |  |  |  |
| mis-initialized function arguments, usage of non-existing identi- | trast, LLM-based approaches such as KernelGPT [38] use static |  |  |  |  |
| fiers, and imprecise control-flow dependencies. This occurrence | inference based on kernel man pages and source code. But they |  |  |  |  |
| primarily arises due to LLMs relying on pre-trained knowledge for | may find some complex dummy operations. And it’s hard for them |  |  |  |  |
| driver synthesis, leading to the production of hallucinations [16]. | to deduct pointer references. Therefore, KSG can generate 2,433 |  |  |  |  |
| The second challenge is that the application of directly using LLMs | Syzlang, which is 17 | . | 86 | × | more compared to KernelGPT [38]. |

for driver synthesis has limited scope because LLMs have limited

knowledge on unseen programs. For those target programs, LLMs

sometimes use training knowledge to fill the gap, thus generating

incorrect API invoking sequences. For example, developers from

Google’s OSS-Fuzz project [35] attempted to leverage LLMs to syn-

thesize drivers. Out of 31 tested OSS-Fuzz projects, 14 successfully

compiled new targets and increased coverage with the synthesized

drivers. The drivers unsuccessfully synthesized by LLMs typically

originated from less common projects like krb5 and rtpproxy . In

contrast, LLMs are more likely to generate compilable and effective

drivers for more common projects, such as tinyxml2 and cjson .

Recommendations. We have the following recommendations:

REC 1.1 Some targets whose code or use cases have been in-

cluded in the training corpus. For these cases, employing LLM for

automated synthesis of fuzz drivers, complemented by error-guided

corrective measures, is a practical approach. Iteratively querying the

LLM based on identified errors and fixing the errors are practical

measures [39], which helps to address the prone-to-error challenge.

For example, libpng is a common library and has already been

seen by GPT4 in its training process. Consequently, it is possible to

directly ask GPT4 to generate a fuzz testing driver for libpng by

giving the prompt “Generating LLVMFuzzerTestOneInput for test

libpng.” However, the generated driver might still contain errors

in grammar or encounter issues during the process of compiling

and linking. Test engineers can subsequently submit individual

LLM queries containing the error messages to rectify these issues,

2.2 Input Generation

Description. Recently, several pioneer works [5, 34, 36, 37]

have been proposed to utilize LLM to enhance input generation.

Their basic idea is to use input specifications and input examples

as the prompt context and then ask LLMs to generate new inputs.

For example, LLMFuzzer [5] feeds input specifications to LLMs to

generate initial seeds for mutation-based fuzzers.

Challenges. The application of LLMs to input generation can

be ineffective if done directly, as LLMs heavily rely on training

corpus and have limited long-text understanding [20, 32]. These

limitations present two challenges for input generation. The first

one is that the generated inputs have insufficient diversity , leading

to inefficient exploration of the input space. This is because LLMs

are pre-trained models and prone to responding to users’ queries in

a similar manner when given the same prompt context. Therefore,

it is difficult for LLMs to generate diverse inputs if they only pro-

vide limited information. For example, ChatAFL [29] demonstrates

a significant limitation when directly applying LLMs to the RTPS

protocol fuzzing. If only a limited amount of protocol information

is provided in the prompts, LLMs can only generate inputs that

cover 4 states out of 10 states that the RTPS protocol supported.

This results in a substantial portion of the RTSP state remaining

unexplored. The second challenge is that the generated inputs

often have limited validity , leading to early termination when the

and have a large number of examples on the web, and they have

| occasionally necessitating multiple iterations. | target program executes these inputs. This is because LLMs can- |  |  |
| --- | --- | --- | --- |
| REC 1.2 | For targets without a dedicated corpus in training, one | not fully understand the long texts of input formats or examples |  |
| can collect valuable materials such as function prototypes, exam- | due to limited ability on long text processing [32]. For example, |  |  |
| ple programs, or connection rules between functions. | Conducting | Border Gateway Protocol (BGP) is a complex protocol, whose doc- |  |
| prompt engineering which involves embedding these materials, en- | ument (BGP RFC 9952) has more than 28,000 words to describe its |  |  |
| hances the precision in generating logical sequences of function calls | functionalities. When generating inputs of BGP based on the RFC |  |  |
| for the creation of drivers. | The prompt engineering approach is a | description, LLMs usually forget to generate the length field of the |  |
| practical solution to tackle the challenge of | limited scope | . | TLV substructures in the BGP message because the description of |
| For example, | typst | is a new markup-based typesetting system | the main message structure and the TLV substructures are a little |
| like LaTex and claims it is more easier to learn and use. To generate | far, making LLMs hard to totally understand BGP format. |  |  |
| a fuzz driver for it, feed the prompt “Generate LLVMFuzzerTe- | Recommendations. | We have the following recommendations: |  |
| stOneInput for typst” to ChatGPT-3.5 will encounter hallucination | REC 2.1 | Some of the testing inputs to the system are common |  |

---

## Page 3

| When Fuzzing Meets LLMs: Challenges and Opportunities | FSE’24, July 2024, Porto de Galinhas, Brazil |  |  |
| --- | --- | --- | --- |
| been included in the LLM’s training corpus. | It is possible to directly | these two problems require entirely distinct code solutions. As |  |
| employ LLM to generate test cases for them, combining methodologies | a result, LLMs may generate code whose functionality deviates |  |  |
| focused on diversification. | These methods encompass internal ap- | from the target program, thus leading to an inaccurate test oracle. |  |
| proaches, such as meticulously crafted prompts that demand using | According to the experiment results of Differential Prompting [25], |  |  |
| diverse features, as well as external methods, such as coverage- | it achieves 66 | . | 7% success rate when generating reference imple- |
| guided genetic algorithms. They both contribute to address the | mentation for programs from the programming contest website |  |  |
| challenge of | insufficient diversity | . | Codeforces. While this is substantially better than its baseline, |
| For instance, when testing common text protocols such as | HTTP | it still results in a false-positive rate of 33.3%, which is still not |  |
| and | FTP | , where LLM excels in its support for text-based languages, | sufficient for practical usage. |
| it is feasible to directly instruct LLM to generate test cases for | Recommendations. | We have the following recommendations: |  |
| these protocols. To increase diversity, for internal approaches, we | REC 3.1 | Defining test oracles is highly dependent on specific tar- |  |
| can use prompts that encourage LLM to generate HTTP files with | gets and scenarios, presenting the most formidable aspect of fuzzing. |  |  |
| various methods (e.g., GET, POST, PUT), different headers, different | For complicated targets, we suggest to avoid analyzing results with |  |  |
| query parameters, URL structures, various payloads, and other | LLM directly. Instead, consider employing LLM to extract features or |  |  |
| aspects. We can also interactively ask LLM to cover more types of | patterns associated with a specific bug type, leveraging domain knowl- |  |  |
| messages [29]. For external approaches, we can utilize coverage- | edge. | Subsequently, monitoring the system using these patterns |  |
| guided generation used in conventional fuzzing along with more | aids in addressing the challenge of | inaccurate understanding | . |
| real-world examples to enhance LLM. | For example, many time-series databases like IoTDB implicitly |  |  |
| REC 2.2 | In many cases, the LLM is not trained with a dedicated | handle exceptions. | Consequently, the system will not crash or |
| training corpus specifically tailored for the test subjects. | Rather than | exhibit other abnormal behaviors. Nevertheless, these database sys- |  |
| employing LLM directly for generating the final test cases, we suggest | tems generate extensive logs, and errors manifest as exceptions in |  |  |
| utilizing LLM to transform well-known knowledge to formulate the | these logs. Therefore, it becomes feasible to use LLM for analyzing |  |  |
| input specifications or build initial test cases. | The input specification | the logs to discern error patterns. In such scenarios, we recommend |  |
| helps address the challenge of | limited validity | , and the initial test | employing LLM to scrutinize the logs, identify error patterns, and |
| cases help address the challenge of | insufficient diversity | . | subsequently leverage these patterns for detecting logic errors. |
| For instance, in the case of protocol implementations lacking | REC 3.2 | Some targets or projects contain well-defined documen- |  |
| machine-readable grammar, generating valid test inputs automati- | tations, where the expected behaviors are clearly described, like the |  |  |
| cally to adhere to the necessary structure and order becomes chal- | RFCs for protocols. | For these cases, we suggest to leverage the natural |  |
| lenging. In such scenarios, leveraging that LLM has been trained | language understanding ability of LLM to extract the expected be- |  |  |
| on established protocols, allows the transfer of grammars from | haviors from the documentations for test oracle definition. | This helps |  |
| these protocols with the assistance of LLM and recorded message | LLM to understand the intention and design of the target programs, |  |  |
| sequences. The grammar can enhance the validity of the generated | thus addressing the challenge of | inaccurate understanding | . |
| test cases. With the grammar, conventional grammar-based fuzzers | For example, the RFCs for protocols usually contain detailed |  |  |
| could be utilized to generate more test cases [29]. Another instance | descriptions of the protocol’s expected behaviors. Take the RFC |  |  |
| is transforming test cases of popular database systems to initial | 854 [4] for Telnet protocol as an example. It specifies expected be- |  |  |
| seeds for the tested database system. The SQL queries of popular | haviors during the negotiation of some disabled command options |  |  |
| database systems like PostgreSQL have rich diversity and they have | or unnegotiated commands. These can be used as test oracles and |  |  |
| already been trained for LLM. Therefore, leveraging the knowledge | can be further used to uncover CVE-2021-40523 [30]. |  |  |

of LLM to transform them into the format of the target database

helps enhance the diversity of generated test cases.

Description. Recently, several pioneer works [21, 25] utilize

LLM to enhance bug detection. Their basic idea is to use function-

ality descriptions of the target program as the prompt context, and

then ask LLMs to generate code that implements the same func-

tionalities with the target program. By comparing the execution

results of the two functionally equivalent programs, they can detect

logic bugs in the target program. For example, Differential Prompt-

ing [25] queries LLMs about the intention of a piece of provided

code and then uses the obtained intention as a new prompt context

for LLMs to generate code with the same intention.

Challenges. The application of LLMs to bug detection can be

To demonstrate the practicality of our recommendations, we use

assisted fuzzing. Addressing challenges in driver synthesis, input

generation, and bug detection, we propose three potential solu-

tions: state-aware driver synthesis, cross-DBMS SQL transfer, and

log-based Oracle definition. These solutions are implemented and

compared with rudimentary uses of LLM, where it is directly em-

ployed. Experiments are conducted under identical settings on a

machine with 256 cores (AMD EPYC 7742 Processor @ 2.25 GHz)

and 512 GiB of main memory, demonstrating the efficacy of our

recommended approaches in enhancing LLM-based fuzzing for

intricate systems like DBMSs.

| system is feasible. Providing them to the fuzzer as the initial seed | 3 | POTENTIAL SOLUTIONS |  |  |
| --- | --- | --- | --- | --- |
| 2.3 | Bug Detection | the Database Management System (DBMS) as the target for LLM- |  |  |
| ineffective if done directly, as LLMs have limited long-text under- | 3.1 | LLM-Enhanced Connector Synthesis |  |  |
| standing [32], posing a challenge to | inaccurate understand | of the se- | Obstacle: | Database connectors, also commonly known as database |
| mantics of the target program. For example, researchers [25] found | drivers, serve as intermediary components facilitating communica- |  |  |  |
| that LLMs may misconstrue code designed to identify the longest | tion between applications and databases. These connectors define |  |  |  |
| common substring as being intended for finding the longest com- | standard a set of interfaces, encompassing functions and parameters. |  |  |  |
| mon subsequence. This misinterpretation can occur even though | The driver for fuzzing database connector consists of a sequence |  |  |  |

---

## Page 4

| FSE’24, July 2024, Porto de Galinhas, Brazil | Jiang et al. |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| of these interfaces. Directly utilizing LLM to generate drivers for | test cases based on the LLM responses. Finally, it temporarily com- |  |  |  |  |
| database connector will encounter two challenges: First is | prone | ments out unparsable sections for fuzzers to ensure proper parsing |  |  |  |
| to error | : API sequences contain semantic information that is em- | and subsequently uncomments them after mutation. |  |  |  |
| bedded in the state of the database connector, directly generating | Result: | We implement the solution called Wingfuzz | 𝑖𝑛𝑝𝑢𝑡 | and |  |
| sequences may import errors. Second is | limited scope | : LLM lacks | compare it with LLM | 𝑖𝑛𝑝𝑢𝑡 | , which directly uses LLM to generate |
| the state transition knowledge of the connectors because it lacks | the SQL queries. We run Wingfuzz | 𝑖𝑛𝑝𝑢𝑡 | and LLM | 𝑖𝑛𝑝𝑢𝑡 | on three |
| the related corpus in training. | DBMS: MonetDB [6], DuckDB [13], and ClickHouse [18]. |  |  |  |  |
| Solution: | Following | REC 1.2 | , we propose LLM-enhanced state- | Table 2: Semantic Correctness Ratios and Branch Coverage. |  |

aware database connector synthesis. We first collect JDBC func-

example programs, and connection rules as input for LLM. The

prompt we give is like “ Based on the state-transition rules and

state description of functions, please generate a sequence of APIS

within length 15. It is required to cover a different combination of

state transitions than before.”

Result: We implement LLM-enhanced connector synthesis into

Wingfuzz 𝑐𝑜𝑛𝑛 and compare it against LLM 𝑐𝑜𝑛𝑛 , which directly

utilizes LLM to generate drivers for MySQL Connector/J [3], Mari-

aDB Connector/J [2], and AWS JDBC Driver for MySQL [1]. We

perform fuzzing on ClickHouse for each tool. Table 1 shows the

driver correctness ratios and branch coverage by LLM 𝑐𝑜𝑛𝑛 and

Wingfuzz 𝑐𝑜𝑛𝑛 on three selected DBMSs in 12 hours. These sta-

tistics show that Wingfuzz 𝑐𝑜𝑛𝑛 always performs better in both

three DBMSs. Specifically, Wingfuzz 𝑐𝑜𝑛𝑛 archives 94% more cor-

rectness rate for driven synthesis. And the drivers generated by

Wingfuzz 𝑐𝑜𝑛𝑛 cover 56% more branches on average. The main rea-

son is that the state-transition rules embed semantic information,

and it also helps LLM generate API sequences that account for the

diverse states within the database connector.

DBMS Driver Correctness Ratios Branch Coverage

AWS MySQL JDBC 0.203 0.394 1382 2293

Obstacle: SQL queries, as the inputs of DBMS, are vital to DBMS

fuzzing. Generating SQL queries directly via LLM faces two main

challenges: ensuring semantic correctness and promoting query

diversity. Semantically correct SQL queries are vital for triggering

complex DBMS behaviors, as syntactical errors lead to parsing

failures. The intricate SQL grammar, encompassing various clauses,

expressions, and rules, poses a challenge for LLM in achieving

semantic correct. Furthermore, diversity in SQL queries is crucial

for probing deep DBMS logic. However, LLM’s constrained variety,

influenced by the absence of DBMS feedback, limits the exploration

of diverse query structures.

Solution: To overcome these challenges, we introduce the cross-

tial seeds are used to mutate new SQL test cases during the fuzzing

DBMS Semantic Correctness Ratios Branch Coverage

DuckDB 0.2551 0.3486 57,937 70,583

Table 2 shows semantic correctness ratios and covered branches

of LLM 𝑖𝑛𝑝𝑢𝑡 and Wingfuzz 𝑖𝑛𝑝𝑢𝑡 on three selected DBMSs in 12

hours. From the table, we can see that Wingfuzz 𝑖𝑛𝑝𝑢𝑡 performs

better than LLM 𝑖𝑛𝑝𝑢𝑡 on DBMS fuzzing. Specifically, the test cases

generated by Wingfuzz 𝑖𝑛𝑝𝑢𝑡 contain 159.35%, 36.65%, and 112.14%

more semantic-correct SQL statements, and cover 55.96%, 21.83%,

and 16.41% more code branches than that of LLM 𝑖𝑛𝑝𝑢𝑡 on Mon-

etDB, DuckDB, and ClickHouse, respectively. It indicates that LLM

can not directly generate high-quality SQL queries as the input

for DBMS fuzzing. The main reason is that the transfer seeds im-

prove the diversity of mutated test cases, and the fuzzer’s mutator

promises the semantic correctness of SQL queries.

Obstacle: The most critical step for DBMS bug detection is to

construct the test oracles to identify the logic or performance bugs

in DBMS. A test oracle refers to a mechanism in DBMS fuzzing

to determine the correctness or validity of the DBMS’s behaviors.

Directly using LLMs to construct the test oracle is challenging as

behaviors of DBMS. They can not access the internal logic, making

detects the anomalies of DBMS by analyzing the runtime informa-

DBMS usually contains the implicit exception handler mechanism,

which captures the internal exceptions to avoid system crashes.

These exceptions usually output some key internal states and be-

haviors of DBMS, such as wrong execution logic. Unlike directly

using LLM to construct the test oracle by checking the execution

result of the SQL query, our approach involves collecting runtime

information from the DBMS and using LLM to analyze the runtime

information for bug detection. The process contains two main steps.

First, it instruments an agent to extract the runtime information of

DBMS. Then, it collects the runtime information and uses LLM to

detect the anomaly by predefining some error pattern.

Table 3: Number of Reported Bugs and Real Bugs.

ClickHouse 67 1 3 3

| tion prototypes and example programs that utilize JDBC. Then | LLM | 𝑖𝑛𝑝𝑢𝑡 | Wingfuzz | 𝑖𝑛𝑝𝑢𝑡 | LLM | 𝑖𝑛𝑝𝑢𝑡 | Wingfuzz | 𝑖𝑛𝑝𝑢𝑡 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| we model the connection relationships between JDBC functions | MonetDB | 0.1594 | 0.4134 | 26,828 | 41,840 |  |  |  |
| as state-transition rules. Next, we gather the function prototypes, | ClickHouse | 0.1458 | 0.3093 | 124,887 | 145,383 |  |  |  |
| driver correctness ratio and branch coverage than LLM | 𝑐𝑜𝑛𝑛 | on all | 3.3 | Monitor-Based DBMS Bug Detection |  |  |  |  |
| Table 1: Driver Correctness Ratios and Branch Coverage. | LLMs lack specific knowledge about the intricate workings and |  |  |  |  |  |  |  |
| LLM | 𝑐𝑜𝑛𝑛 | Wingfuzz | 𝑐𝑜𝑛𝑛 | LLM | 𝑐𝑜𝑛𝑛 | Wingfuzz | 𝑐𝑜𝑛𝑛 | it difficult to accurately predict or emulate DBMS behavior. |
| MariaDB Connector/J | 0.142 | 0.331 | 583 | 843 | Solution: | To address the challenges, we propose the Runtime |  |  |
| MySQL Connector/J | 0.216 | 0.367 | 1256 | 1982 | Monitor-Based DBMS Bug Detection following the | REC 3.1 | , which |  |
| 3.2 | Cross-DBMS SQL Transfer | tion of DBMS in real-time. To ensure the robustness of DBMS, the |  |  |  |  |  |  |
| DBMS SQL transfer approach, aligned with the recommendation | DBMS | LLM | 𝑏𝑢𝑔 | Wingfuzz | 𝑏𝑢𝑔 |  |  |  |
| REC 2.2 | , for SQL generation. In contrast to directly generating | Name | Reported | Real | Reported | Real |  |  |
| the SQL queries, we use LLM to transfer the test cases from other | MonetDB | 61 | 0 | 6 | 3 |  |  |  |
| DBMSs as the initial seeds for fuzzing the target DBMS. These ini- | DuckDB | 54 | 0 | 5 | 3 |  |  |  |
| loop. The process contains three key steps. First, it executes exist- | Result: | To evaluate the effectiveness of our recommendation, |  |  |  |  |  |  |
| ing SQL test cases within its native DBMS to capture the schema | we implement the solution with Wingfuzz | 𝑏𝑢𝑔 | and compare it with |  |  |  |  |  |
| information during execution. Second, it utilizes LLMs along with | LLM | 𝑏𝑢𝑔 | , which directly uses LLM to determine whether the ex- |  |  |  |  |  |
| the captured schema information to guide the generation of new | ecution of the SQL query is right during the fuzz loop. Table 3 |  |  |  |  |  |  |  |

---

## Page 5

| When Fuzzing Meets LLMs: Challenges and Opportunities | FSE’24, July 2024, Porto de Galinhas, Brazil |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| shows the number of reported bugs and real bugs by LLM | 𝑏𝑢𝑔 | and | [19] Zhenlan Ji, Pingchuan Ma, Zongjie Li, and Shuai Wang. 2023. Benchmarking and |  |  |  |
| Wingfuzz | 𝑏𝑢𝑔 | in 12 hours on MonetDB, DuckDB and ClickHouse. It | Explaining Large Language Model-based Code Generation: A Causality-Centric |  |  |  |
| shows the Wingfuzz | 𝑏𝑢𝑔 | Approach. | arXiv preprint arXiv:2310.06680 | (2023). |  |  |
| can detect more anomalies and has fewer | [20] Jean Kaddour, Joshua Harris, Maximilian Mozes, Herbie Bradley, Roberta |  |  |  |  |  |
| false positives than LLM | 𝑏𝑢𝑔 | . Specifically, LLM | 𝑏𝑢𝑔 | totoally reported | Raileanu, and Robert McHardy. 2023. | Challenges and applications of large |
| 182 bugs but only 1 bug is real. Instead, Wingfuzz | 𝑏𝑢𝑔 | language models. | arXiv preprint arXiv:2307.10169 | (2023). |  |  |
| reported 14 | [21] Siva Kesava Reddy Kakarla and Ryan Beckett. 2023. Oracle-based Protocol Testing |  |  |  |  |  |
| bugs and 9 bugs are real bugs and have been confirmed. The main | with Eywa. | arXiv preprint arXiv:2312.06875 | (2023). |  |  |  |

demonstrates that these recommendations effectively address the

connector-j. Accessed: April 26, 2024.

[4] 2023. Rfc854. https://datatracker . ietf . org/doc/html/rfc854. Accessed: April 26,

April 26, 2024.

(2018), 118–137.

[11] Yinlin Deng, Chunqiu Steven Xia, Haoran Peng, Chenyuan Yang, and Lingming

[12] Yinlin Deng, Chunqiu Steven Xia, Haoran Peng, Chenyuan Yang, and Lingming

Zhang. 2023. Large language models are zero-shot fuzzers: Fuzzing deep-learning

libraries via large language models. In Proceedings of the 32nd ACM SIGSOFT

international symposium on software testing and analysis . 423–435.

[13] DuckDB. 2023. DuckDB WebSite. https://www . duckdb . org/. Accessed: April 26,

2024.

[14] Muhammad Usman Hadi, Rizwan Qureshi, Abbas Shah, Muhammad Irfan, Anas

Zafar, Muhammad Bilal Shaikh, Naveed Akhtar, Jia Wu, Seyedali Mirjalili, et al.

2023. Large language models: a comprehensive survey of its applications, chal-

lenges, limitations, and future prospects. Authorea Preprints (2023).

[15] Xinyi Hou, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong Wang, Li Li, Xiapu Luo,

David Lo, John Grundy, and Haoyu Wang. 2023. Large language models for soft-

ware engineering: A systematic literature review. arXiv preprint arXiv:2308.10620

(2023).

[16] Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Hao-

tian Wang, Qianglong Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, et al.

2023. A survey on hallucination in large language models: Principles, taxonomy,

challenges, and open questions. arXiv preprint arXiv:2311.05232 (2023).

[17] Ali Reza Ibrahimzada, Yang Chen, Ryan Rong, and Reyhaneh Jabbarvand. 2023.

Automated Bug Generation in the era of Large Language Models. arXiv preprint

arXiv:2310.02407 (2023).

[18] ClickHouse Inc. 2023. ClickHouse Website. https://clickhouse . com. Accessed:

April 26, 2024.

[22] Prateek Kumar and Sanjay Kathuria. 2023. Large language models (LLMs) for

[23] Katherine Lee, Orhan Firat, Ashish Agarwal, Clara Fannjiang, and David Sussillo.

2018. Hallucinations in neural machine translation. (2018).

preprint arXiv:2310.09748 (2023).

Inducing Tests with Differential Prompting. In 2023 38th IEEE/ACM International

[27] Zhengliang Liu, Tianyang Zhong, Yiwei Li, Yutong Zhang, Yi Pan, Zihao Zhao,

arXiv:2307.13693 (2023).

[28] Yunlong Lyu, Yuxuan Xie, Peng Chen, and Hao Chen. 2023. Prompt Fuzzing for

[29] Ruijie Meng, Martin Mirchev, Marcel Böhme, and Abhik Roychoudhury. 2024.

Large Language Model guided Protocol Fuzzing. In Proceedings of the 31st Annual

arXiv:1809.02156 (2018).

arXiv:2305.14196 (2023).

to Seed Generation. (2023).

arXiv:2308.04748 (2023).

(2023).

| reason is that the collected runtime information contains the error | natural language processing (NLP) of oil and gas drilling data. In | SPE Annual |  |  |  |
| --- | --- | --- | --- | --- | --- |
| message of DBMS, and it helps LLM to analyze and detect bugs. | Technical Conference and Exhibition? | SPE, D021S012R004. |  |  |  |
| 4 | CONCLUSION | [24] Jia Li, Ge Li, Chongyang Tao, Huangzhao Zhang, Fang Liu, and Zhi Jin. 2023. |  |  |  |
| We identify and systematically analyze five major challenges when | Large Language Model-Aware In-Context Learning for Code Generation. | arXiv |  |  |  |
| using LLM in fuzzing and confirm their prevalence through a re- | [25] Tsz-On Li, Wenxi Zong, Yibo Wang, Haoye Tian, Ying Wang, Shing-Chi Cheung, |  |  |  |  |
| view of most recent top-tier conference papers. These challenges | and Jeff Kramer. 2023. Nuances are the Key: Unlocking ChatGPT to Find Failure- |  |  |  |  |
| affect the effectiveness and accuracy of the LLM-based fuzzing | Conference on Automated Software Engineering (ASE) | . IEEE, 14–26. |  |  |  |
| technologies. To support researchers in avoiding them, we pro- | [26] Hongliang Liang, Xiaoxiao Pei, Xiaodong Jia, Wuwei Shen, and Jian Zhang. 2018. |  |  |  |  |
| vide recommendations that are applicable to effectively assist the | Fuzzing: State of the art. | IEEE Transactions on Reliability | 67, 3 (2018), 1199–1218. |  |  |
| main steps in fuzzing, depending on the richness of the relevant | Peixin Dong, Chao Cao, Yuxiao Liu, Peng Shu, et al. 2023. | Evaluating large |  |  |  |
| corpus and documentation. Our preliminary evaluation further | language models for radiology natural language processing. | arXiv preprint |  |  |  |
| challenges in LLM-assisted DBMS fuzzing. | Fuzz Driver Generation. | arXiv preprint arXiv:2312.17677 | (2023). |  |  |
| REFERENCES | Network and Distributed System Security Symposium (NDSS) | . |  |  |  |
| [1] 2023. aws-mysql-jdbc. https://github | . | com/awslabs/aws-mysql-jdbc. Accessed: | [30] MITRE. 2021. CVE-2021-40523. (2021). |  |  |
| April 26, 2024. | [31] Anna Rohrbach, Lisa Anne Hendricks, Kaylee Burns, Trevor Darrell, and |  |  |  |  |
| [2] 2023. mariadb-connector-j. https://github | . | com/mariadb-corporation/mariadb- | Kate Saenko. 2018. Object hallucination in image captioning. | arXiv preprint |  |
| [3] 2023. mysql-connector-j. https://github | . | com/mysql/mysql-connector-j. | Ac- | [32] Uri Shaham, Maor Ivgi, Avia Efrat, Jonathan Berant, and Omer Levy. 2023. Zero- |  |
| cessed: April 26, 2024. | SCROLLS: A Zero-Shot Benchmark for Long Text Understanding. | arXiv preprint |  |  |  |
| 2024. | [33] Hao Sun, Yuheng Shen, Jianzhong Liu, Yiru Xu, and Yu Jiang. 2022. | { | KSG | } | : |
| [5] Joshua Ackerman and George Cybenko. 2023. Large Language Models for Fuzzing | Augmenting Kernel Fuzzing with System Call Specification Generation. In | 2022 |  |  |  |
| Parsers (Registered Report). In | Proceedings of the 2nd International Fuzzing Work- | USENIX Annual Technical Conference (USENIX ATC 22) | . 351–366. |  |  |
| shop | . 31–38. | [34] Elwin Tamminga, Bouwko van der Meijs, and Ultraware Stjepan Picek. 2023. |  |  |  |
| [6] MonetDB B.V. 2023. MonetDB Website. https://www | . | monetdb | . | org. Accessed: | Utilizing Large Language Models for Fuzzing: A Novel Deep Learning Approach |
| [7] Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, Kaijie Zhu, Hao Chen, Linyi | [35] Google Open Source Security Team. [n. d.]. | AI-Powered Fuzzing: Breaking |  |  |  |
| Yang, Xiaoyuan Yi, Cunxiang Wang, Yidong Wang, et al. 2023. A survey on | the Bug Hunting Barrier. https://security | . | googleblog | . | com/2023/08/ai-powered- |
| evaluation of large language models. | arXiv preprint arXiv:2307.03109 | (2023). | fuzzing-breaking-bug-hunting | . | html. Accessed: April 26, 2024. |
| [8] Chen Chen, Baojiang Cui, Jinxin Ma, Runpu Wu, Jianchao Guo, and Wenqian | [36] Chunqiu Steven Xia, Matteo Paltenghi, Jia Le Tian, Michael Pradel, and Ling- |  |  |  |  |
| Liu. 2018. A systematic review of fuzzing techniques. | Computers & Security | 75 | ming Zhang. 2023. Universal fuzzing via large language models. | arXiv preprint |  |
| [9] Arghavan Moradi Dakhel, Amin Nikanjam, Vahid Majdinasab, Foutse Khomh, | [37] Chenyuan Yang, Yinlin Deng, Runyu Lu, Jiayi Yao, Jiawei Liu, Reyhaneh Jabbar- |  |  |  |  |
| and Michel C Desmarais. 2023. Effective test generation using pre-trained large | vand, and Lingming Zhang. 2023. White-box compiler fuzzing empowered by |  |  |  |  |
| language models and mutation testing. | arXiv preprint arXiv:2308.16557 | (2023). | large language models. | arXiv preprint arXiv:2310.15991 | (2023). |
| [10] Victor Dantas. 2023. Large Language Model Powered Test Case Generation for | [38] Chenyuan Yang, Zijie Zhao, and Lingming Zhang. 2023. KernelGPT: Enhanced |  |  |  |  |
| Software Applications. (2023). | Kernel Fuzzing via Large Language Models. | arXiv preprint arXiv:2401.00563 |  |  |  |
| Zhang. 2023. Large language models are zero-shot fuzzers: Fuzzing deep-learning | [39] Cen Zhang, Mingqiang Bai, Yaowen Zheng, Yeting Li, Xiaofei Xie, Yuekang Li, |  |  |  |  |
| libraries via large language models. In | Proceedings of the 32nd ACM SIGSOFT | Wei Ma, Limin Sun, and Yang Liu. 2023. Understanding large language model |  |  |  |
| international symposium on software testing and analysis | . 423–435. | based fuzz driver generation. | arXiv preprint arXiv:2307.12469 | (2023). |  |

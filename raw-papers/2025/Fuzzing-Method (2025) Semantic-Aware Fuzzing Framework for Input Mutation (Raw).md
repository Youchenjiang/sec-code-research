---
title: "Semantic-Aware Fuzzing: An Empirical Framework for LLM-Guided, Reasoning-Driven Input Mutation"
author: "Mengdi Lu; Steven Ding; Furkan Alaca; Philippe Charland"
creator: "arXiv GenPDF (tex2pdf:)"
pages: 16
---

# Semantic-Aware Fuzzing: An Empirical Framework for LLM-Guided, Reasoning-Driven Input Mutation

> **作者**：Mengdi Lu; Steven Ding; Furkan Alaca; Philippe Charland
> **總頁數**：16 頁

---

## Page 1

1

Semantic-Aware Fuzzing: An Empirical

Framework for LLM-Guided, Reasoning-Driven

Input Mutation

Mengdi Lu, Steven Ding, Furkan Alaca, and Philippe Charland

Abstract —Security vulnerabilities in Internet-of-Things (IoT) devices, mobile platforms, and autonomous systems remain critical.

Traditional mutation-based fuzzers—while effectively explore code paths—primarily perform byte- or bit-level edits without semantic

reasoning. Coverage-guided tools such as AFL++ rely on dictionaries, grammars, and splicing heuristics to impose shallow structural

constraints, leaving deeper protocol logic, inter-field dependencies, and domain-specific semantics unaddressed. Conversely,

reasoning-capable large language models (LLMs) have potentials to leverage human knowledge embedded during pretraining to

understand input formats, respect complex constraints, and propose targeted mutations, much like an experienced reverse engineer or

testing expert. However, without ground truth for “correct” reasoning in mutation generation, supervised fine-tuning is impractical,

motivating explorations of off-the-shelf LLMs using prompt-based few-shot learning. To bridge this gap, we present an open-source

microservices framework that integrates reasoning LLMs with AFL++ on Google’s FuzzBench, addressing the asynchronous execution

and divergent hardware demands (GPU- vs. CPU-intensive) of LLMs and fuzzers. We evaluate four research questions: (R1) How can

reasoning-based LLMs be integrated into the fuzzing mutation loop? (R2) Do few-shot prompts yield higher-quality mutations than

zero-shot? (R3) Can off-the-shelf reasoning models improve fuzzing directly via prompt engineering? and (R4) Which open-source

reasoning LLMs perform best under prompt-only conditions? Experiments with Llama3.3, Deepseek-r1-Distill-Llama-70B, QwQ-32B,

and Gemma3 highlight Deepseek-r1-Distill-Llama-70B as the most promising. Mutation effectiveness depends on prompt complexity

and model choice rather than shot count alone. Response latency and throughput bottlenecks remain key obstacles. Our framework,

released as open-source, supports reproducibility and community extension. Future directions include dynamic scheduling, lightweight

feedback, and scalable deployment.

Index Terms —Software testing, Grey-box fuzzing, Mutation testing, Vulnerability detection, Software reliability, Machine learning,

Large language models (LLMs), Prompt engineering, Reasoning models, Code coverage, Automated software security.

✦

1 I NTRODUCTION

ACH year, tens of thousands of new Common Vul- mobile applications [14], and autonomous driving stacks

| E | nerabilities and Exposures (CVEs) are catalogued in | [15]. Despite these advances, existing fuzzers still rely on |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| the National Vulnerability Database (NVD), highlighting a | largely blind or heuristic-driven mutations that struggle |  |  |  |  |  |  |  |
| rapidly expanding attack surface across Internet-of-Things | to penetrate deep protocol logic and intricate input for- |  |  |  |  |  |  |  |
| (IoT) devices, mobile platforms, and autonomous systems | mats, which motivates further research into semantically |  |  |  |  |  |  |  |
| [1], | [2], | [3], | [4]. | Manual | code | review—including | labor- | informed mutation strategies. |
| intensive reverse engineering of binaries—struggles to keep | Recent LLM-based fuzzing efforts have made impressive |  |  |  |  |  |  |  |
| pace with this growth, as expert analysts can only examine | progress in applying prompt engineering to generate both |  |  |  |  |  |  |  |
| a limited fraction of complex firmware, applications, or | initial seeds and targeted mutations for structured inputs. |  |  |  |  |  |  |  |
| embedded controllers within reasonable timeframes. In con- | Fuzz4All demonstrated this approach on programming- |  |  |  |  |  |  |  |
| trast, fuzzing—an automated, “shift-right” testing approach | language grammars [16], PromptFuzz extended it to library |  |  |  |  |  |  |  |
| arXiv:2509.19533v1 [cs.SE] 23 Sep 2025 | that requires no source code and instead exercises com- | APIs [17], and CHATAFL showcased interactive mutation |  |  |  |  |  |  |
| piled binaries with malformed or randomized inputs—has | refinement through chat-style prompts when fuzzing pro- |  |  |  |  |  |  |  |
| become one of the most effective vulnerability discovery | tocols [18]. These works showcases the promise of LLMs |  |  |  |  |  |  |  |
| techniques, responsible for identifying a majority of high- | to automate complex input synthesis. However, these ap- |  |  |  |  |  |  |  |
| severity bugs in large software projects [5], [6], [7], [8], | proaches treat the model as a black box, focusing solely |  |  |  |  |  |  |  |
| [9], [10]. Coverage-guided, mutation-based fuzzers such as | on input-to-output mapping and omitting the intermediate |  |  |  |  |  |  |  |
| AFL++ [11] combine lightweight instrumentation with seed- | reasoning steps that ground high-quality generation. Chain- |  |  |  |  |  |  |  |
| based mutations to rapidly explore execution paths, and | of-thought (COT) reasoning has been shown to improve |  |  |  |  |  |  |  |
| have demonstrated success against IoT firmware [12], [13], | LLM fidelity, reduce hallucinations, and enhance output |  |  |  |  |  |  |  |

diversity by making the model’s analytical process explicit.

Meanwhile, systems such as LLAMAFUZZ [19] employ

• M. Lu and F. Alaca are with the School of Computing, Queen’s University, supervised fine-tuning on AFL++. LLAMAFUZZ derives

Kingston, ON, Canada.

• S. Ding is with McGill University, Montreal, QC, Canada. “good” mutations, which inherently restricts the model’s

• P.Charland is with Mission Critical Cyber Security Section, Defence creativity at existing mutation heuristics and requires costly

R&D Canada. labeled data. In contrast, our work explores whether

Manuscript received September, 2025 prompting off-the-shelf reasoning LLMs—without any ad-

---

## Page 2

reasoning-enabled LLMs can approximate the analytical

applying domain knowledge to craft targeted mutations,

rather than merely relying on surface-level edits. By ex-

empirically designed prompts, we aim to unlock this latent

reasoning capability, reduce blind spots in protocol logic,

This setup allows us to assess the raw reasoning power and

creative mutation strategies of off-the-shelf LLMs without

capping their potential or incurring the high cost of labeled

semantically meaningful mutations that achieve higher

LLMs to mutation-based binary fuzzing using prompt engi-

neering alone, comparing zero-, one-, and three-shot strate-

gies to quantify their effects on mutation validity, code

2

Program

Execution

seeds Bitmap Analyzer

Mutator

Fuzzing

Results

| (llama3) | HTTP |
| --- | --- |
| report | Generation |

2 M ETHODOLOGIES

execution environments.

2.1 Infrastructure

| ditional | fine-tuning—can | leverage | their | latent | human- | Target | Fuzzbench Runner | LLM Mutation Docker-compose |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| knowledge representations to generate semantically rich, | (Source code) | Fuzzer AFL++ | Test Cases | Redis |  |  |  |  |  |  |
| novel mutations beyond AFL++’s conventional strategies. | Queue 1 (C2P) |  |  |  |  |  |  |  |  |  |
| Building on these observations, we hypothesize that | Queue 2 (P2C) |  |  |  |  |  |  |  |  |  |
| workflow of an expert reverse engineer by examining an | custom_mutator | llm_service | Ollama | llm_fuzz |  |  |  |  |  |  |
| input’s structure, inferring inter-field dependencies, and | Prompts |  |  |  |  |  |  |  |  |  |
| posing the model’s internal “chain-of-thought” [20] through | Fig. 1. LLM guided fuzzing architecture overview |  |  |  |  |  |  |  |  |  |
| and minimize redundant or invalid mutations. Since there | models—Llama 3.3, DeepSeek-r1-Distill-Llama-70B, QwQ- |  |  |  |  |  |  |  |  |  |
| is no definitive “ground truth” for how such a reasoning | 32B, and Gemma 3—assessing their out-of-the-box mutation |  |  |  |  |  |  |  |  |  |
| process should proceed, and because supervised fine-tuning | performance in coverage-guided fuzzing [23], [24], [25], [26]. |  |  |  |  |  |  |  |  |  |
| on AFL++ outputs would inherently limit the model to ex- | Finally, we analyze practical limitations—model latency, |  |  |  |  |  |  |  |  |  |
| isting heuristics, we focus our empirical study on zero-shot | throughput trade-offs, and semantic depth—and outline |  |  |  |  |  |  |  |  |  |
| and few-shot prompting—where the number of in-context | directions for dynamic scheduling, lightweight feedback |  |  |  |  |  |  |  |  |  |
| examples provided to the model defines the “shot” count. | loops, and scalable deployment in LLM-driven fuzzing. |  |  |  |  |  |  |  |  |  |
| data. We structure our empirical investigation around four | We propose a solution that incorporates a LLM as an in- |  |  |  |  |  |  |  |  |  |
| research questions: | dependent service to assist the mutation stage of a grey- |  |  |  |  |  |  |  |  |  |
| • | Research Question R1 | : How can reasoning-based LLMs | box, code-coverage-based fuzzer. Integrating LLM with the |  |  |  |  |  |  |  |
| be integrated into the mutation loop of a coverage-guided | fuzzer ( | R1 | ) introduces two major challenges. While LLMs |  |  |  |  |  |  |  |
| fuzzer? This requires reconciling the asynchronous exe- | are capable of advanced reasoning, they typically experience |  |  |  |  |  |  |  |  |  |
| cution pace and distinct hardware requirements of CPU- | high response latency [27] to process input and generate |  |  |  |  |  |  |  |  |  |
| centric fuzzers and GPU-backed LLMs without impairing | responses, in contrast to the high execution throughput of |  |  |  |  |  |  |  |  |  |
| overall throughput. | modern fuzzers like AFL++ [11], which can process over |  |  |  |  |  |  |  |  |  |
| • | Research Question R2 | : Does providing few-shot exam- | 3000 | executions per second [28]. Embedding an LLM di- |  |  |  |  |  |  |
| ples in prompts lead to higher-quality, more semantically | rectly in the fuzzing loop would degrade the fuzzing speed, |  |  |  |  |  |  |  |  |  |
| informed mutations than zero-shot prompts? This eval- | making it difficult to maintain fuzzing efficiency ( | Challenge |  |  |  |  |  |  |  |  |
| uates | whether | example-driven | prompting | consistently | 1 | ). To preserve the performance of the fuzzer, we decouple |  |  |  |  |
| enhances mutation validity and diversity over minimal | the fuzzing and LLM mutation processes into two distinct |  |  |  |  |  |  |  |  |  |
| prompt designs. | components: | a C-based fuzzer component | and | a Python-based |  |  |  |  |  |  |
| • | Research Question R3 | : Can off-the-shelf reasoning LLMs | LLM-guided component | . These components are packaged and |  |  |  |  |  |  |
| improve fuzzing effectiveness through prompt-based rea- | deployed independently, creating a synchronization chal- |  |  |  |  |  |  |  |  |  |
| soning alone? This explores whether an approach us- | lenge ( | Challenge 2 | ) for communication between these two |  |  |  |  |  |  |  |
| ing only prompts, without any fine-tuning, can generate | components, due to language differences and distributed |  |  |  |  |  |  |  |  |  |
| coverage or uncover more bugs. | To enable communications between the fuzzer and LLM |  |  |  |  |  |  |  |  |  |
| • | Research Question R4 | : Which open-source LLM yields | mutating | service, | we | extended | AFL++’s | mutation | logic |  |
| the | best | performance | guided | solely | by | prompt | engi- | through a custom mutation hook, | custom_mutator | inter- |
| neering? This compares models to identify whose latent | face ( | Solution 2 | ). The implementation allows the fuzzer to |  |  |  |  |  |  |  |
| knowledge and reasoning capabilities translate most ef- | invoke LLM-generated mutations in a selective and asyn- |  |  |  |  |  |  |  |  |  |
| fectively into valid, high-quality test-case mutations. | chronous manner. The LLM mutation runs as a standalone |  |  |  |  |  |  |  |  |  |
| Building on these questions, we contribute an open- | Docker Compose service comprising three core components: |  |  |  |  |  |  |  |  |  |
| source, | microservices-based | framework | that | connects | a | message broker (Redis) | , | Ollama (llm service) | , and a | LLM |
| AFL++ | to | off-the-shelf | reasoning | LLMs | via | Redis | and | prompt generator (llm fuzz) | . To ensure efficient and reliable |  |
| Docker, | effectively | harmonizing | CPU- | and | GPU-driven | communications, multiple named message queues are es- |  |  |  |  |
| components without fine-tuning. Our framework is pack- | tablished in the Redis server ( | Solution | 1 | ). When LLM- |  |  |  |  |  |  |
| aged for automated deployment on Google’s FuzzBench, | generated mutated test cases are available in the Redis |  |  |  |  |  |  |  |  |  |
| enabling reproducible, large-scale evaluation across diverse | queue, the fuzzer consumes and uses them; otherwise, it |  |  |  |  |  |  |  |  |  |
| binary targets [21]. To the best of our knowledge, we present | defaults to built-in mutation logic. A high-level integration |  |  |  |  |  |  |  |  |  |
| the first systematic study of applying reasoning-capable | and architectural overview is shown in Figure 1, 2 and 3. |  |  |  |  |  |  |  |  |  |
| coverage, and crash discovery [22]. In tandem, we empiri- | The | proposed | system | is | built | on | FuzzBench | [21]—an |  |  |
| cally benchmark four state-of-the-art open-source reasoning | open-source | fuzzing | evaluation | platform | developed | by |  |  |  |  |

---

## Page 3

Fuzzbench Runner

Fuzzbench Benchmarks Fuzzer AFL++

Program Target Instrumentation Instrumented

Bitmap Analyzer

| (Initial test cases) | Seed Pool | Hangs |
| --- | --- | --- |
| ./seeds | Mutated |  |
| Tests | Coverage |  |

Data &

Interesting

LLM Mutation Fuzzing Results

Service)

Feedback Results data

Test case snapshots &

report Fuzzbench Reporter Fuzzbench Measurer

Fig. 2. LLM guided fuzzing architecture: Fuzzer component - AFL++

| Fuzzer AFL++ | LLM Mutation Docker-compose Services |
| --- | --- |
| custom_mutator | openthread_ot-ip6-send-fuzzer |

Redis

| unsigned integer type | b'\x10\x00CWL\x7f\x00 |
| --- | --- |
| buffer | \x00\x00\x00\x90i\xd4 |
| for mutation | \x01\x00\x00\x00\x00 |

Fuzzbench \x10\x02\x00\x00\x00

0x10 0x00 0x43 0x57 0x4c 0x7f

| 0x00 0x00 0x00 0x00 0x90 0x69 | 0xd4 0x01 0x00 0x00 0x00 0x00 | llm_fuzz |
| --- | --- | --- |
| 0x00 0x00 0x00 0x00 0x00 0x00 | 0x00 0x00 0x64 0x00 | Redis-client |
| \x00\t\x07\x08\x00\x00 | \x00\x00\x00\x90i\xd4 | Consumer |
| \x11\x02\x00\x00\x00 | \x00\x00\x00? | hex-converter |

\x00\x00\x01d\x00'

unsigned integer type Fuzzbench hexidecimal

library_info buffer

mutated buffer uint8_t

Response Parser Prompts

Generation

| 0x10 0x00 0x43 0x57 0x4c 0x7f | ### Analysis Process: |  |
| --- | --- | --- |
| 0x00 0x00 0x09 0x07 0x08 0x00 | ... |  |
| 0x11 0x02 0x00 0x00 0x00 0x00 | ### Final Output: | 100043574c7f0000090708 |
| 0x00 0x00 0x3f 0x00 0x00 0x00 | 00000000009069d4010000 | Ollama-client |

000000000000016400

""" You are a mutator designed

| llm_service | to enhance fuzzing input for |
| --- | --- |
| Ollama (llama3) | a program... Follow these |

steps:

1. ... 2. ...

...

"""

"""

You are a mutator designed to

software technique role-based, enhance fuzzing input for a

3-shots 1-shot, code coverage. Your task is to

data string data (converted from a Python byte

string) while preserving the plausibility of the original format. Follow these steps: fi le

Callback path 1. ... 2. ...

...

"""

Fig. 3. LLM guided fuzzing architecture: LLM Mutation component

3

ture of building, deploying, executing fuzzers is inherently

complex. As a result, integrating a custom fuzzer into the

platform remains complex ( Challenge 3 ). To incorporate our

and deployment strategies from AFL++ in Fuzzbench, ex-

ers are built using Fuzzbench’s base image for both the

tions—such as new deployment scripts, updated configura-

version incompatibility and HTML report generations—are

required to support both the fuzzer and LLM components.

Through these modifications ( Solution 3 ), the system is suc-

cessfully integrated into FuzzBench, enabling reproducible

experiments across benchmarks. Each trial produces de-

tailed coverage reports for a systematic evaluation of the

fuzzer’s performance on the selected benchmarks.

2.1.2 Fuzzer Component

AFL++ [11], known for its efficient instrumentation and

mutation strategies, acts as the core fuzzer in the fuzzer

and the initial test cases , so-called seed corpus , are supplied

or crashes, is analyzed to guide future mutations and en-

hance the overall efficiency of the fuzzing process. Major

stages in our fuzzing process includes:

2) Mutation: Test cases, which are input buffers, are

mutated using a dual mutation strategy implemented

in custom mutator , altering AFL++’s original meth-

ods. Our mutation includes (1) standard AFL++ mu-

tation operators such as bit flipping, arithmetic op-

erations, and dictionary substitutions [11], alongside

semantic-aware mutations by targeting input sec-

tions most likely to reveal new code paths based

on their structure and content. Figure 3 illustrates

the LLM mutation service architecture.

3) Test Case Execution: Mutated test cases are ex-

considered as “interesting” and increase coverage;

| (Source code) | (compiler) | Program | Test Cases Execution | Coverage Results | LLM-guided fuzzer, we begin by duplicating the packaging |
| --- | --- | --- | --- | --- | --- |
| Input Generation | tending them for our implementation. The new fuzzer is |  |  |  |  |
| Seeds | Fuzzing Crashes, | added to the | ./fuzzers | directory, and Docker contain- |  |
| Initial Tests | Results | custom builder and runner. However, additional modifica- |  |  |  |
| (Docker-compose | custom_mutator | tions for custom mutation strategies, and fixes for Python |  |  |  |
| uint8_t | Queue 1 (C2P) | \x00\t\x07\x08\x00\x00 | component. As illustrated in Figure 2, the | target program |  |
| Queue 2 (P2C) | library_info | \x00\x00\x00\x00\x00 | \x00\x00\x00\x00\x00d | \x00' | by Fuzzbench. During the build stage, AFL++ instruments |
| 0x00 0x00 0x09 0x07 0x08 0x00 | the target program during compilation, enabling real-time |  |  |  |  |
| 0x10 0x02 0x00 0x00 0x00 0x00 | monitoring of code coverage throughout execution. These |  |  |  |  |
| b'\x10\x00CWL\x7f\x00 | instrumented binaries are then used by the fuzzing engine |  |  |  |  |
| \x01\x00\x00\x00\x00 | to observe and collect coverage feedback. Finally, feedback |  |  |  |  |
| \x00\x00\x00\x00 | Publisher | from each execution, such as newly discovered code paths |  |  |  |
| 0x00 0x00 0x00 0x00 0x90 0x69 | 0xd4 0x01 0x00 0x00 0x00 0x00 | ... | 1) | Input generation: | Initial seeds are stored in a seed |
| 0x00 0x00 0x00 0x01 0x64 0x00 | 000011020000000000003f | pool and serve as the basis for generating test cases. |  |  |  |
| prompt engineering | 0-shot, | program, aiming to maximize | (2) an LLM-guided mutation service. The LLM ser- |  |  |
| message | mutate a hexadecimal string | vice—running in Docker Compose with Redis, Ol- |  |  |  |
| Forward path | lama, and a prompt generation module—performs |  |  |  |  |
| Google—providing a standardized environment for evaluat- | ecuted against the instrumented target program, |  |  |  |  |
| ing fuzzers through automated benchmark execution, result | with AFL++ [11] generating coverage bitmaps to |  |  |  |  |
| analysis, and report generation. Our system, consisting of | track paths exploration. Test cases that cause crashes |  |  |  |  |
| a custom fuzzer and an LLM mutation module, leverages | or timeouts are stored in separate output queues, |  |  |  |  |
| this infrastructure to evaluate LLM-guided fuzzing across | crashes and hangs, for further analysis. |  |  |  |  |
| multiple benchmarks. The following subsection outlines the | 4) | Results analysis: | The coverage bitmap reflects the |  |  |
| integration process and associated implementation chal- | diversity and frequency of executed branch tuples. |  |  |  |  |
| lenges. | In the bitmap, test cases that explore new paths are |  |  |  |  |
| 2.1.1 | Integrating Fuzzer into Fuzzbench | they are prioritized in future fuzzing rounds. |  |  |  |
| While FuzzBench [29] aims to simplify the evaluation and | 5) | Feedback mechanism: | The fuzzer dynamically ad- |  |  |
| comparison of fuzzing techniques, the underlying architec- | justs its mutation and scheduling strategy based on |  |  |  |  |

---

## Page 4

4

| bitmap feedback. Interesting test cases are priori- | converter | . This transformation ensures consistency in input |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tized, and subsequent mutations are guided by how | format and allows the LLM to process the content more reli- |  |  |  |  |  |  |  |  |
| much coverage improvements they have. | ably. Prompt generation within | llm fuzz | is optimized using |  |  |  |  |  |  |
| 6) | Report | generation: | When | finishing | fuzzing, | prompt design and engineering techniques | , which structure the |  |  |
| FuzzBench | [21] | aggregates | all | outputs | with | its | input and context (e.g. | library info | ) to enhance the LLM’s |
| measurer module to calculate final code coverage, | mutation capabilities. The mutated output is found in the |  |  |  |  |  |  |  |  |
| then sends the analyzed results to the reporter. The | ”Final Output” | section of the response received from Ollama. |  |  |  |  |  |  |  |
| reporter module renders the information in HTML, | The section must be parsed by a custom | response parser | to |  |  |  |  |  |  |
| and generates the report. | extract the actual mutated test case for the fuzzer. Overall, |  |  |  |  |  |  |  |  |

the llm fuzz serves as a message and prompt manager, con-

| 2.1.3 | LLM Mutation Component | taining: a Redis client for data exchange, an Ollama client |
| --- | --- | --- |
| The LLM-guided mutation component operates as a stan- | for LLM interaction, and a utility stack for hex conversion, |  |
| dalone service integrated into the fuzzing infrastructure. | prompt generation, and response parsing. |  |

Its architecture and message processing workflow are illus-

trated in Figure 3, using the benchmark openthread ot-ip6- 2.2 Data Flow

| send-fuzzer | as an example. This component is composed of | The proposed mutation method is outlined in | Algorithm 1 | . |
| --- | --- | --- | --- | --- |
| three primary microservices: | Complementing the pseudo-code, Figure 4 presents a visu- |  |  |  |
| 2.1.3.1 | Redis – Message Broker and Context Store: | alized data flow illustrating the interaction between AFL++ |  |  |
| Redis [30] is an open-source, in-memory data structure store | and LLM-guided mutation components in our proposed |  |  |  |
| commonly used as a message broker and cache system. | framework. The processing of input buffers during mutation |  |  |  |
| It supports a key–value data model and belongs to the | is detailed in the following stages: |  |  |  |

class of NoSQL databases [31]. Within this architecture, • Message publishing in AFL++: Input buffers, repre-

| Redis bridges the AFL++ fuzzer (in | C | ), and the LLM mu- | sented as | uint8 t | ( | unsigned 8-bit integers | ), are initially |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tation service (in | Python | ) through multiple uniquely named | mutated using AFL++’s default mutation strategies. The |  |  |  |  |
| queues. The two primary queues are used: (1) | C2P | (Client- | mutated buffers are then serialized and published to the |  |  |  |  |
| to-Prompt), which stores messages containing input buffers | Redis queue named | C2P | . |  |  |  |  |

published by AFL++ and consumed by the LLM muta- • Message consumption in llm fuzz : The llm fuzz service

| tion service; and (2) | P2C | (Prompt-to-Client), which holds | listens to the | C2P | queue using the Redis client. When a |
| --- | --- | --- | --- | --- | --- |
| messages containing LLM-mutated buffers published by | message arrives, it is consumed as a | Python byte strings | . |  |  |
| the LLM component and consumed by AFL++. Moreover, | Otherwise, the application enters a wait state. |  |  |  |  |

Redis also maintains a persistent key-value pair identified as • Message processing in llm fuzz : Consumed messages in

| library info | , which stores metadata about the FuzzBench [21] | the | llm fuzz | service are processed in two key steps: |  |
| --- | --- | --- | --- | --- | --- |
| benchmark libraries. This contextual information is essential | • | Buffer Splitting: | Buffers longer than | 2000 | bytes are |
| for generating informed and context-aware prompts for the | split to prevent memory overflow on CUDA-enabled |  |  |  |  |
| LLM during the mutation process. Thus, our message bro- | systems. The first | 2000 | bytes are mutated by the LLM, |  |  |
| ker handles message queuing, manages shared states, en- | while the remaining segments are stored for recombi- |  |  |  |  |
| ables asynchronous communications, and facilitates seam- | nation. Buffers shorter or equal to | 2000 | bytes are used |  |  |
| less integration between fuzzing and LLM components. | in full in the mutation, and the remaining segments are |  |  |  |  |
| 2.1.3.2 | Ollama – LLM Execution Engine: | Ollama | considered as | empty | . This strategy prioritizes mutating |
| [32] is an open-source platform designed for deploying and | the first segment as file format identifiers typically |  |  |  |  |
| executing LLMs. It is containerized via Docker, which sim- | appear at the beginning of files. |  |  |  |  |
| plifies model deployment and isolation. In this architecture, | • | Hexadecimal Conversion: | Buffers designated for mu- |  |  |
| Ollama [32] acts as the | core inference engine | for the LLM- | tation are converted to | hexadecimal | strings to ensure |
| guided mutation process. It handles mutation requests, per- | compatibility with the LLM. |  |  |  |  |

forms inference using the loaded model, and returns the • Prompt generation in llm fuzz : Refined prompts are

| generated outputs. While Ollama does not support direct | created | using | prompt | engineering, | incorporating | user |
| --- | --- | --- | --- | --- | --- | --- |
| fine-tuning, it leverages internal quantization and runtime | contexts, including both the hexadecimal input buffer and |  |  |  |  |  |
| optimizations aimed at reducing inference latency. These | the benchmark context information retrieved from Redis. |  |  |  |  |  |
| design choices make it a practical and efficient component | These prompts are then sent to the Ollama service via an |  |  |  |  |  |
| for integrating into our fuzzing system. | HTTP connection established by the Ollama client. |  |  |  |  |  |

2.1.3.3 llm fuzz – Prompt Generation and Message • Response generation in LLM: The LLM processes the

| Management: | The | llm fuzz | service is a Python-based or- | prompt and returns a structured response containing two |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| chestration module responsible for message publishing and | key sections: | Analysis | and | Final Output | . The | Final Output |
| consuming, prompt generation and LLM response manage- | includes the mutated buffers in hex format, following |  |  |  |  |  |
| ment. The service | (1) | manages communication with | Redis | for | strict formatting constraints. |  |

publishing and consuming messages, (2) generates prompts • Response parsing in llm fuzz : The mutated buffer is

| and sends them to | Ollama | for inference, and | (3) | parses and | extracted and converted back from hexadecimal to Python |
| --- | --- | --- | --- | --- | --- |
| handles responses returned by the LLM. Since LLMs are not | byte string in the | Final Output | . If a | ValueError | occurs due |
| inherently optimized for parsing complex binary formats | to an odd-length hexadecimal string, a | ”0” | is appended to |  |  |
| such as object files (e.g. OTT), input buffers are first con- | fix the format. Buffers that still fail are discarded and not |  |  |  |  |
| verted to | hexadecimal representations | using a dedicated | hex- | passed to the fuzzer. |  |

---

## Page 5

Buffer for mutation

mutate with AFL++

default mutation Yes

strategies

message (AFL++ consume the fi rst Publish the message with

mutated buffer) from LLM mutated buffer to

Redis P2C queue

with mutated buffer to publish the message C2P

Redis C2P queue

Split the buffer into two based on max

length = 2000

Check if Redis P2C queue

contains messages buffer for LLM mutation remaining buffer

<=2000) length < 2000)

Yes

consume the message (LLM fi rst

| mutated buffer) from | convert the buffer into | combine buffer | Do Nothing |
| --- | --- | --- | --- |
| Fuzzing Loop | Load library_info from |  |  |
| Redis | LLM mutated |  |  |
| buffer | None |  |  |
| Create prompt | Yes | No |  |

Data State Decision

| Making | LLM generate | LLM |
| --- | --- | --- |
| response | generated | parse response |

response

• Message publishing in llm fuzz : Validly converted and

recombined mutated buffers—including previously split

segments—are published to the P2C Redis queue, where

they become available for AFL++ to consume and execute.

• Message consumption in AFL++: The AFL++ component

continuously monitors the P2C queue on the Redis server.

When a message containing LLM-mutated buffers is re-

ceived, AFL++ consumes the data, also in uint8 t format,

and utilizes it in the fuzzing loop. Otherwise, AFL++

continues execution using its default mutations.

2.3 Deployment

The fuzzer component integrates with the FuzzBench

framework [21] and is deployed alongside target bench-

marks using Fuzzbench’s standard pipeline. In contrast,

the LLM mutation component is deployed independently

using Docker Compose. The Docker Compose configura-

tion defines and orchestrates Redis , Ollama , and llm fuzz

microservices, which are initialized simultaneously using

the docker-compose up --build command. Once these

services are active and the LLM models are loaded into

Ollama, the fuzzing process can be initiated via our devel-

oped custom script, run_benchmark.sh , which simplifies

benchmark configuration and automates the building and

deployment of the fuzzer component in Docker containers.

Using Docker Compose to deploy the LLM-guided muta-

5

M LLM , Prompt shots P k ( k ∈ { 0 , 1 , 3 } ), Fuzzing time inter-

val T

LLM response metrics R log

1: Initialize input queue Q ← C

0

2: Initialize coverage map M cov ← ∅

3: Initialize R log , C mut , Q crash , Q hang ← ∅

4: for t = 1 to T do

5: Select input x ∼ Q using queue strategy

6: Split string x

x

| 7: | Convert | x | length< | =2000 | to hex string | h | x |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9: | Query LLM | y | ← M | LLM | ( | π | ) |  |  |  |  |  |
| 10: | if | y | = | ∅ | or timeout | then |  |  |  |  |  |  |
| 11: | x | ′ | ← | Mutate | AFL++ | ( | x | ) |  |  |  |  |
| 12: | continue |  |  |  |  |  |  |  |  |  |  |  |
| 13: | end if |  |  |  |  |  |  |  |  |  |  |  |
| 14: | Extract hex output | h | x | ′ | ← | ParseLLM | ( | y | ) |  |  |  |
| 16: | if | decode fails | then |  |  |  |  |  |  |  |  |  |
| 17: | Log for FMR or HCER |  |  |  |  |  |  |  |  |  |  |  |
| 18: | continue |  |  |  |  |  |  |  |  |  |  |  |
| 19: | end if |  |  |  |  |  |  |  |  |  |  |  |
| 22: | if | O | = | CRASH | then |  |  |  |  |  |  |  |
| 23: | Add | x | ′ | to crash queue: | Q | crash | ← Q | crash | ∪ { | x | ′ | } |
| 24: | continue |  |  |  |  |  |  |  |  |  |  |  |
| 25: | else if | O | = | TIMEOUT | then |  |  |  |  |  |  |  |
| 26: | Add | x | ′ | to hang queue: | Q | hang | ← Q | hang | ∪ { | x | ′ | } |
| 27: | continue |  |  |  |  |  |  |  |  |  |  |  |
| 28: | else if | isNewCoverage | ( | C | ) | then |  |  |  |  |  |  |
| 29: | Add | x | ′ | to queue and corpus: |  |  |  |  |  |  |  |  |

Q ← Q ∪ { x ′ } , C mut ← C mut ∪ { x ′ }

30: end if

31: Log metrics R log ← R log ∪ { ( x ′ , FMR , HCER , RDR ) }

32: end for

33: Generate final report R cov

pendent deployment—even across different servers—and

seamless LLM integration into fuzzing workflows.

• Flexibility: Both the fuzzer and LLM components can

be easily configured via environment variables and

command-line arguments in the deployment script, en-

abling quick adaptation to different benchmarks, fuzzing

strategies, and model versions.

• Sustainable Extension: Our architecture allows other

FuzzBench-integrated fuzzers to adopt the LLM service

by using the custom_mutator hook and configuring

Redis queues appropriately.

2.4 Prompt Refinement

| AFL++ | LLM mutation | Algorithm 1 | LLM-Guided Mutation-Based Fuzzing |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fuzzer runs mutator | Start Service | Input: | Seed corpus | C | 0 | , Target program | F | , Pre-trained LLM |  |  |  |  |  |  |  |  |  |
| in AFL++ | Check if Redis C2P queue | Output: | Set of interesting inputs | C | mut | , Coverage results | R |  |  |  |  |  |  |  |  |  |  |
| contains messages | No | Waiting... | cov | , |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (buffer length | (None if buffer | length< | =2000 | , x | length> | 2000 | ← | LengthSplitter | ( | x | ) |  |  |  |  |  |  |
| No | h | x | ← | HexEncode | ( | x | length< | =2000 | ) |  |  |  |  |  |  |  |  |
| P2C | hexadecimal | 8: | Format prompt | π | ← | FormatPrompt | ( | P | k | , h | x | ) |  |  |  |  |  |
| Starting | Ending | Created | Check if hexadecimal can be | 15: | Try decode | x | ′ | ← | HexDecode | ( | h |  |  |  |  |  |  |
| State | State | prompt | converted back into bytes | x | ′ | ) |  |  |  |  |  |  |  |  |  |  |  |
| Fig. 4. Data flow diagram of AFL++ component and LLM mutation | 20: | Re-combine strings | x | ′ | ← | Join | ( | x | ′ | , x | length> | 2000 | ) |  |  |  |  |
| component | 21: | Run | x | ′ | on | F | : | ( | O | , | C | ) | ← F | ( | x | ′ | ) |
| tion component provides three advantages: | In the LLM response generation stage, the output is ex- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| • | Modularity: | The LLM-guided mutation service is fully | pected to consist a clean hexadecimal string representing |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| decoupled from the fuzzer component, enabling inde- | the mutated input—without any additional text, special |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 6

characters, or explanatory content. Thus, a minimal prompt

like: ”Mutate the given buffer { input buffer } by using pro-

prompts presents two significant limitations ( Challenge 4 ):

eters like temperature [33].

2) Limited Interpretability : Simple prompts do not

difficult to analyze how results are derived.

To address these limitations and improve both output ac-

curacy and interpretability, the prompts are refined using

• Task clarification: Prompts clearly and explicitly define

the objective to instruct LLM about what to achieve.

hexadecimal string (converted from a Python byte string) while

preserving the plausibility of the original file format.”

mutation targets , and (3) apply structured mutations . Each

step is further elaborated. For example, step (1) involves

ters—to ensure efficient parsing of LLM responses.

6

System prompt example:

"""

plausibility of the original fi le format.

Follow these steps:

1. **Analyze the Input Buffer**:

- Key fi elds (e.g., headers, delimiters, or magic numbers).

- Known positional or structural dependencies based on provided library information.

2. **Select Mutation Targets**:

- Identify byte sequences likely to trigger alternate execution paths when altered, focusing on:

- Conditional values or length fi elds.

- Regions with less strict format constraints.

3. **Apply Mutations**:

- Mutate the identi fi ed bytes strategically to maximize code coverage.

- Ensure the mutated byte string remains consistent with the overall structural requirements

of the original fi le format.

### **Strict Output Formatting Requirements**:

- **Analysis (Required)**:

- **Final Output must strictly follow this format:**

- must contain **only** the mutated buffer as a valid **plain text hexadecimal**

- **MUST NOT** use any code blocks or additional formatting.

"""

2.4.2 User Role

actual mutated buffers.

mutated in the input buffer, and how the final output is

| vided | { | library info | } | , and generate only the mutated hexadeci- | You are a mutator designed to enhance fuzzing input for a program, aiming to maximize code coverage. |  |
| --- | --- | --- | --- | --- | --- | --- |
| mal string.” | can be sufficient. However, using such simple | Your task is to mutate a hexadecimal string (converted from a Python byte string) while preserving the |  |  |  |  |
| 1) | Inconsistent Output Format: | Due to the inherent | - Decode the hexadecimal string into bytes and identify structural or syntactic patterns, including: |  |  |  |
| stochastic nature of LLMs, outputs may deviate | - Regions constrained by speci | fi | c values or patterns (e.g., checksums, length | fi | elds). |  |
| from the expected format, even with fixed param- | - Note areas critical to format validity and regions suitable for mutation. |  |  |  |  |  |
| offer insights into the model’s reasoning, making it | - Prioritize mutations that are likely to explore untested code paths while keeping the | fi | le format plausible. |  |  |  |
| two core techniques: | prompt design | and | prompt engineering | - Before producing the | fi | nal output, provide a **brief analysis** of the input buffer. |
| ( | Solution 4 | ). Our prompt design strategies include: | - must always begin with exactly **four (`####`) hash symbols**. |  |  |  |
| • | Role playing: | Inspired by [34], the LLM is assigned a | - **MUST NOT** wrap the output in backticks (`) or markdown |  |  |  |
| domain-specific role—a fuzzing expert—to improve task | - **MUST NOT** provide any analysis, explanations, comments, or descriptions. |  |  |  |  |  |
| alignment and contextual relevance. | If the response does not meet above formatting requirements, it is **incorrect**. |  |  |  |  |  |
| For example, my prompt states: | “Your task is to mutate a | Fig. 5. An example of a system prompt. |  |  |  |  |
| • | Instruction specialization: | The mutation task is decom- | buffer, a dedicated | ”Strict Output Formatting Requirements” |  |  |
| posed into fine-grained, step-by-step instructions, which | section is emphasized in the system prompt to enforce com- |  |  |  |  |  |
| includes: (1) | analyze the input buffer | , (2) | identify suitable | pliance. Figure 5 demonstrates a system-role-based prompt. |  |  |
| decoding the hexadecimal input, identifying structural | User prompts supply dynamic, task-specific input data. |  |  |  |  |  |
| components such as key fields, regions, and known li- | However, due to the variability in LLM generated outputs |  |  |  |  |  |
| brary patterns, recognizing sections critical to format in- | [33], strict formatting constraints alone may not ensure con- |  |  |  |  |  |
| tegrity, and identifying areas safe to mutation. | sistency. To improve stability, we apply few-shot prompting |  |  |  |  |  |
| • | Section structuring: | Prompts are organized into logical | in the user prompt with embedded concrete examples that |  |  |  |
| segments: instruction, context, input data, and output | follow the required output format, and we also reinforce |  |  |  |  |  |
| format indicators. The response is structured into two | format reminders to minimize the chance of context drift. |  |  |  |  |  |
| parts: (1) | ”Analysis” | , a detailed rationale or “chain-of- | Figure 7 shows a few-shot prompt example. Our research |  |  |  |
| thought” (COT) [20] explaining the mutation reasoning, | explores three prompt engineering strategies [35]: |  |  |  |  |  |

which aids prompt refinement; (2) ”Final Output” , a • Zero-shot prompting provides only task instructions

strictly formatted hexadecimal string containing only the without any examples or demonstrations. As shown in

mutated buffer—free from explanations or extra charac- Figure 6, the “ Example Output ” section does not contain

Despite LLMs’ ability to understand complex prompts, • Few-shot prompting requires explicit examples in the

| their reliance on memory can lead to context loss in lengthy | prompt. One-shot and three-shot prompting insert one |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| input sequences, resulting in less accurate or inconsistent | and | three | successful | mutation | examples, | respectively. |
| responses. To mitigate this, a role-based message structuring | These examples (Figure 8) are previous LLM outputs that |  |  |  |  |  |
| strategy is used to semantically segment the prompt and | met the formatting requirements. |  |  |  |  |  |

clarify the intent of instructions. It is effective because LLMs • Chain-of-thought prompting [20] adds intermediate rea-

| can interpret input differently based on assigned roles. Ac- | soning steps in prompts. Our few-shot prompting ex- |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cordingly, two distinct roles are incorporated into the | prompt | amples include an | Analysis | section explaining the logic |  |  |  |
| engineering strategy | in our research: | behind mutations—such as why certain characters are |  |  |  |  |  |
| 2.4.1 | System Role | generated. To avoid context loss, the strict output format |  |  |  |  |  |
| System-based prompts contain fundamental instructions to | specification has to be restated after the examples. |  |  |  |  |  |  |
| define | the | LLM’s | behavioral | constraints | and | contextual | Effective prompt engineering often poses a challenge, as |
| scope. They establish limitations, rules, and ethical bound- | optimal prompts are rarely successful on the first attempt. |  |  |  |  |  |  |
| aries to guide response generation. In our study, system | Thus, the process typically requires iterative refinement. |  |  |  |  |  |  |
| prompts consist of the assigned role, primary tasks, step- | We adopt a continuous trial-and-error approach [36], which |  |  |  |  |  |  |
| be-step instructions with contexts, and strict output format | involves generating responses using the current prompt, |  |  |  |  |  |  |
| requirements. Since the fuzzer expects only the mutated | evaluating whether the outputs meet structural and seman- |  |  |  |  |  |  |

---

## Page 7

Zero-shot prompt example:

You are a mutator designed to enhance fuzzing input for a program, aiming to maximize code coverage. Your task is to mutate a hexadecimal string

(converted from a Python byte string) while preserving the plausibility of the original fi le format. Follow these steps:

1. **Analyze the Input Buffer**:

- Known positional or structural dependencies based on provided library information. fi c values or patterns (e.g., checksums, length fi elds).

- Regions with less strict format constraints. fi elds.

3. **Apply Mutations**: - Mutate the identi - Ensure the mutated byte string remains consistent with the overall structural requirements of the original fi ed bytes strategically to maximize code coverage. fi le format.

fi nal output should be in the exact format of "Final Output" in the example output.

#### Final Output:

"""

(example 2}

...

...

input buffer: {hex_msg}

library info: {library_info}

#### Your analysis process:

<Here, the model generates analysis>

- The **####Analysis section is required** before `#### Final Output`

it is **incorrect**.

3 E XPERIMENTAL S ETUP

performance server running Ubuntu 20.04.2 LTS , equipped

7

"""

### Example 1:

library info: freetype2_ftfuzzer

#### Analysis:

several key fi elds and patterns are identi fi ed:

or data types within the fi le.

of- for parsing and interpreting the fi le correctly.

thought - **Checksums or Validation Bytes**: Although not explicitly identi fi ed, regions with seemingly

random or calculated values might serve as integrity checks.

Expected

less strict format constraints, and areas that could potentially trigger alternate execution paths

when altered. The strategy involves modifying these targets to explore untested code paths

while maintaining the fi le's overall structural integrity.

#### Final Output:

Strict 00640000000000000095119667000000001022020000000000800000000000000010034902000

format 00010000800c0000040000000008000000000000b30e000000000000d8479f663a7f00008b050

0000000000810e00000000000010209f663a7f00005c224300000000000000000

"""

3.1 Evaluation Metrics

are sequences of instructions with a single entry and exit

coverage, measuring executed branches in conditional struc-

tures—such as if, switch-case, loop, and try-catch state-

efficiency and implicitly reflects the LLM’s mutation quality,

as better mutations are likely to explore more code. CIP is

expressed as:

CIP (%) = Coverage

N

SCR = × 100%

""" Example provided in the few-shot user prompt:

- Decode the hexadecimal string into bytes and identify structural or syntactic patterns, including: - Key - Regions constrained by speci fi elds (e.g., headers, delimiters, or magic numbers). input buffer: 10808c5e3a7f000021e100000000000010cd3e02000000001080000000000000b30

| - Note areas critical to format validity and regions suitable for mutation. | e000000000000640000000000000095119667000000001022020000000000800000000000000 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 2. **Select Mutation Targets**: | Example | 01003490200000000100000000000000080abd4663a7f000020cd3e020000000000800000000 |  |  |  |  |
| - Identify byte sequences likely to trigger alternate execution paths when altered, focusing on: | input | 0000028cd3e0200010000800c0000040000000008000000000000b30e000000000000d8479f6 |  |  |  |  |
| - Conditional values or length | 63a7f00008b05000000000000000000000000000010209f663a7f0000ffffffff00000000184d3e02 |  |  |  |  |  |
| - Prioritize mutations that are likely to explore untested code paths while keeping the | fi | le format plausible. | 00000000810e000000000000810e00000000000010209f663a7f00005c224300 |  |  |  |
| ### Required Output Format: | - **Analysis**: Provide a brief analysis of the input buffer. | The input buffer appears to be a binary | fi | le format, potentially related to font | fi | les given the |

- **Final Output**: Return the mutated buffer as a single Python hexadecimal string. No additional code, comments, or text should accompany it. The association with `freetype2_ftfuzzer`. Upon decoding the hexadecimal string into bytes,

| ### Example Output: | #### Analysis: | <Concise analysis of the input buffer and mutation strategy> | - **Magic Numbers**: Speci | fi | c byte sequences that could indicate the start of particular sections |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <mutated buffer hexadecimal> | Chain- | - **Length Fields**: Areas that specify the size of subsequent data blocks, which are crucial |  |  |  |  |  |  |
| Fig. 6. A structured prompt for zero-shot prompting. | output | Given this analysis, mutation targets include conditional values (e.g., length | fi | elds), regions with |  |  |  |  |
| User prompt example: | 10808c5e3a7f000021e100000000000010cd3e02000000001080000000000000b30e0000000000 |  |  |  |  |  |  |  |
| """ | output | 00000100000000000000080abd4663a7f000020cd3e0200000000008000000000000028cd3e02 |  |  |  |  |  |  |
| {example 1} | 00000000000000000000000000010209f663a7f0000ffffffff00000000184d3e0200000000810e00 |  |  |  |  |  |  |  |
| Now, mutate the following input: | Fig. 8. An in-context example provided in the user prompt. |  |  |  |  |  |  |  |
| #### Final Output: | We use FuzzBench [29] to collect and analyze coverage |  |  |  |  |  |  |  |
| <Here, the model should only return the mutated buffer as plain text hexadecimal> | data across multiple targets, evaluating code coverage from |  |  |  |  |  |  |  |
| ### **Strict Requirement**: | four perspectives: (1) | Function Coverage | , which measures |  |  |  |  |  |
| - If your | fi | nal output contains **explanations, comments, formatting, or extra words**, | the proportion of functions executed relative to the total in |  |  |  |  |  |
| - The **only acceptable response** after | the executable; (2) | Line Coverage | , assessing the percentage |  |  |  |  |  |
| `#### Final Output:` is **the mutated hexadecimal string**. | of executable lines exercised within functions; (3) | Region |  |  |  |  |  |  |
| """ | Coverage | , evaluating distinct control-flow regions, which |  |  |  |  |  |  |
| Fig. 7. An example of a user prompt. | point; and (4) | Branch Coverage | , also known as decision |  |  |  |  |  |
| tic requirements, making small targeted adjustments—such | ments—to ensure both true and false paths are explored. |  |  |  |  |  |  |  |
| as emphasizing formatting constraints, altering example | We evaluate our LLM-guided mutation strategy pri- |  |  |  |  |  |  |  |
| structures, or refining key terms—and repeating this process | marily | through | code | coverage, | using | Coverage | Improve- |  |
| until the prompts consistently produce satisfactory results. | ment | Percentage | (CIP) | to | calculate | LLM | efficiency | gains |
| This process produces the final versions of the zero-shot, | (Coverage | LLM | ) over a baseline fuzzer ( Coverage | Baseline | ), |  |  |  |
| one-shot and three-shot prompts, retained only after meet- | where positive values indicate the LLM outperforms the |  |  |  |  |  |  |  |
| ing strict output format requirements. | baseline. The metric quantifies enhancements in fuzzing |  |  |  |  |  |  |  |
| While fuzzers can theoretically run endlessly to discover | LLM | (%) | − | Coverage | Baseline | (%) |  |  |
| bugs, in practical and industrial scenarios, execution time is | The | Syntactic Correctness Rate (SCR) | evaluates the per- |  |  |  |  |  |
| limited. To reflect real-world constraints, we evaluated each | centage of LLM outputs that follow the required format, |  |  |  |  |  |  |  |
| configuration over two fixed time intervals: | one hour | and | reflecting how well prompts guide the model to produce |  |  |  |  |  |
| four hours | . Each fuzzer and benchmark pair was tested using | usable results. | N | correct | denotes the number of syntactically |  |  |  |
| three independent trials | to reduce randomness and improve | valid LLM-generated responses, and | N | total | denotes the total |  |  |  |
| result reliability. All experiments were conducted on a high- | number of LLM responses. SCR is expressed as: |  |  |  |  |  |  |  |
| with an | Intel Xeon Gold 5218 CPU (64 cores) | , | 754 GiB | of | correct |  |  |  |
| RAM, | 3 TB | of disk storage, and two | NVIDIA Quadro RTX | N | total |  |  |  |
| 6000 GPUs (24 GiB VRAM each) | . This section defines the | Despite strict prompt formatting and zero temperature for |  |  |  |  |  |  |
| performance metrics and describes the selected benchmarks, | deterministic outputs, LLMs can still produce syntactic er- |  |  |  |  |  |  |  |
| baseline, and LLMs. Extra experiment setup details and | rors. These syntactic failures arise from two primary issues: |  |  |  |  |  |  |  |
| generated results are illustrated in the Section 4. | hexadecimal conversion exceptions | —when a hex string fails to |  |  |  |  |  |  |

---

## Page 8

prior observed output within the same fuzzer-benchmark

pair and prompt-shot setup. A high RDR signals low mu-

N Duplicate

In summary, we evaluates the proposed approach using four

major metrics : code coverage , which measures the fuzzer’s abil-

ity to explore program execution paths; CIP , which qualifies

performance gains relative to baseline fuzzers; SCR , which

assesses the reliability of LLM-generated mutations under

structured prompt guidance; and RDR , which evaluates

how deterministic LLM-generated outputs are.

3.2 Selection of Benchmarks, Baselines, and LLMs

tured input types such as file formats, network protocols,

and cryptographic libraries, which closely match the input

tem. These widely adopted, code coverage-guided grey-box

8

engines with LLM-driven mutation components. This in-

R2 , we conducted a focused set of experiments evaluating

the impact of prompt engineering—specifically 0-shot, 1-

shot, and 3-shot configurations—on the quality of mutations

generated by Llama3.3 [23]. To investigate whether other

LLMs outperform Llama3.3, addressing R3 and R4 , we fur-

ther experimented and compared code coverage achieved

by applying various state-of-the-art reasoning models under

different prompt shots. The selected LLMs are widely rec-

ognized for their strong performance in the AI community

and represent current advances in reasoning capabilities.

We also evaluate results across four metrics—code cov-

Havoc and MOpt [42].

| parse into a Python bytes object—and | format mismatches | , | Effective LLM-guided fuzzing requires models with four |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| where the required “Final Output” section is missing or | core capabilities: (1) strong | code generation ability | to pro- |  |  |  |  |  |  |
| contains invalid content. While we manually handle conver- | duce structured, syntactically valid mutations; (2) solid | lan- |  |  |  |  |  |  |  |
| sion exceptions, format mismatches remain the main cause | guage understanding | to recognize input formats and main- |  |  |  |  |  |  |  |
| of syntactic errors. Thus, SCR measures how often the LLM | tain structural integrity; (3) reliable | instruction following | to |  |  |  |  |  |  |
| produces syntactically valid and properly formatted muta- | strictly fulfill prompt requirements; and (4) effective | reason- |  |  |  |  |  |  |  |
| tions. A higher SCR indicates more mutations with valid or | ing | to explain mutation logic and decision-making. Based on |  |  |  |  |  |  |  |
| usable formats, potentially enhancing fuzzing effectiveness. | these criteria, we select Llama3.3 (70B), Deepseek-r1-Distill- |  |  |  |  |  |  |  |  |
| LLM response stability can affect fuzzing effectiveness, | Llama-70B, QwQ-32B, and Gemma3-27B as baseline models. |  |  |  |  |  |  |  |  |
| as repeated outputs reduce mutation diversity and limit | These open-source models represent recent advances in |  |  |  |  |  |  |  |  |
| code coverage. Thus, we propose the Response Duplication | code-centric LLMs and excel in structured text generation, |  |  |  |  |  |  |  |  |
| Rate (RDR) as a metric for measuring LLM determinism. | instruction compliance, and semantic reasoning. They are |  |  |  |  |  |  |  |  |
| Responses are duplicates if their “Final Output” matches a | also compatible with our system’s resource constraints. |  |  |  |  |  |  |  |  |
| tation diversity, suggesting that the LLM may be overly | 4 | R | ESULTS AND | D | ISCUSSIONS |  |  |  |  |
| deterministic or insensitive to subtle prompt variations. | To assess the potential of state-of-the-art reasoning-capable |  |  |  |  |  |  |  |  |
| Formally, RDR is the ratio of duplicated LLM responses | LLMs in enhancing fuzzing performance, we developed a |  |  |  |  |  |  |  |  |
| ( | N | Duplicate | ) to the total number of LLM generations ( | N | Total | ): | dedicated infrastructure that integrates traditional fuzzing |  |  |
| RDR | = | ∗ | 100% | frastructure serves as the foundation for all experimental |  |  |  |  |  |
| N | Total | evaluations addressing our research questions. To answer |  |  |  |  |  |  |  |
| Since | our | study | focuses | on | exploring | fuzzing | in | do- | erage, CIP, SCR, and RDR—introduced in Section 3.1, from |
| mains with high reliability demands and complex inter- | three primary perspectives: code coverage, mutation quality, |  |  |  |  |  |  |  |  |
| nal logic—namely, IoT firmware, mobile platforms, and | and fuzzing efficiency. Code coverage data were extracted |  |  |  |  |  |  |  |  |
| autonomous driving systems—we selected 25 of the 26 | from FuzzBench-generated reports, including function, line, |  |  |  |  |  |  |  |  |
| benchmarks officially maintained in Fuzzbench [29]. Their | branch, and region coverage. Additionally, approximately |  |  |  |  |  |  |  |  |
| corresponding fuzz targets are derived from OSS-fuzz [37] | 96GiB | of logs were generated by the LLM component. |  |  |  |  |  |  |  |
| and represent a diverse range of real-world open-source | Through data cleaning and log parsing, we constructed | log |  |  |  |  |  |  |  |
| software programs [29]. These benchmarks include struc- | analysis tables | containing over | 640 | , | 000 | entries. |  |  |  |
| characteristics of our target domains and are compatible | 4.1 | Baseline Comparison Experiment |  |  |  |  |  |  |  |
| with our LLM mutation strategy. Within Fuzzbench, 20 | To establish a baseline for comparison, each of the three |  |  |  |  |  |  |  |  |
| benchmarks are | general-purpose | , aiming to maximize code | mutation-based fuzzers— | AFL++ | [11], | AFL | [38], and | Lib- |  |
| coverage across the target program, while 5 are | specific bench- | Fuzzer | [39]—was evaluated across | three independent trials |  |  |  |  |  |
| marks | , designed to reproduce known or suspected crashes. | using the FuzzBench framework. Each fuzzer was tested |  |  |  |  |  |  |  |
| Additionally, we select | AFL | [38], | AFL++ | [11], and | Lib- | against a common set of | 25 selected benchmarks | per trial. All |  |
| Fuzzer | [39] as baseline fuzzers due to their foundational | fuzzers were run with their | default configurations | defined in |  |  |  |  |  |
| roles | and | architectural | relevance | to | our | proposed | sys- | FuzzBench, which apply basic mutation strategies such as |  |
| fuzzers have influenced the development of modern fuzzing | Based on one-hour and four-hour testing results, | Ta- |  |  |  |  |  |  |  |
| tools. Since our solution builds on AFL++, it is naturally | ble 1 | summarizes the frequency of highest code coverage |  |  |  |  |  |  |  |
| selected as a baseline for direct comparison. AFL++, which | achieved by each baseline fuzzer. | AFL++ consistently out- |  |  |  |  |  |  |  |
| extends AFL with hybrid mutation strategies and improved | performed | other fuzzers across all coverage types and time |  |  |  |  |  |  |  |
| scheduling, involves AFL as a proper baseline to assess the | intervals. For instance, it achieved the highest branch cov- |  |  |  |  |  |  |  |  |
| evolution of fuzzing capabilities. LibFuzzer is also included | erage on | 18 benchmarks | in the one-hour runs, which is over |  |  |  |  |  |  |
| as it is widely used in FuzzBench and serves as the foun- | 69% | of all baseline fuzzer-benchmark pairs. In the four-hour |  |  |  |  |  |  |  |
| dation for several modern fuzzing tools (e.g. LibFuzzer-bin | runs, AFL++ outperformed both AFL and LibFuzzer on | 17 |  |  |  |  |  |  |  |
| [40], LibAFL [41], and PromptFuzz [17]). | benchmarks | ( | 65% | ). Given consistently superior performance |  |  |  |  |  |

---

## Page 9

TABLE 1

The number of benchmarks that has the maximum code coverage

results for each baseline fuzzer.

Frequencies of Maximum Code Coverage Occurred for Baseline

| RunTime | Coverage-type | AFL++ | AFL | LibFuzzer |
| --- | --- | --- | --- | --- |
| Branch Coverage | 18 | 12 | 10 |  |
| Region Coverage | 18 | 9 | 4 |  |
| Branch Coverage | 17 | 10 | 14 |  |
| Function Coverage | 18 | 4 | 7 |  |

4

| Line Coverage | 13 | 5 | 9 |
| --- | --- | --- | --- |
| Region Coverage | 18 | 5 | 6 |

of AFL++ across both time intervals, AFL++ is used as the

primary baseline for evaluating the effectiveness of LLM-

guided fuzzers in subsequent experiments.

4.2 Llama3.3 Prompt Engineering Evaluation Experi-

specifically the number of prompt shots—impacts the ef-

Since prompt design is inherently iterative and costly to

refine within the full FuzzBench pipeline, we initially op-

timized prompt templates by using Llama3.3 model in a

standalone Python environment. Finalized prompts for 0-

shot, 1-shot, and 3-shot settings are presented in Section

2.4: Prompt Refinement . After finalizing prompts, we set the

LLM’s temperature to 0 . 0 for deterministic and reproducible

outputs, and loaded the full-scale Llama3.3-70B model (ap-

with these templates and settings. For each prompt shot,

the system was initialized from scratch, and logs for all trials

were preserved for reproducibility, traceability and analysis.

Table 2 highlights trends in branch coverage percent-

ages for 0-shot, 1-shot, and 3-shot prompts from both one-

hour and four-hour fuzzing tests using Llama3.3. The ef-

fect of increasing prompt shots on coverage is observed

to be highly benchmark-dependent : libpcap fuzz both and

vorbis decode fuzzer benchmarks show improved branch

coverage with increased shots, while harfbuzz hb-shape-

fuzzer and sqlite3 ossfuzz show little or no gain, and

timeouts occurred in approximately 35% of cases. Although

these timeouts may reduce usable mutations, response qual-

The following sections plot the relationship between LLM

response quality and code coverage, offering insight into

9

Llama3.3 Syntactic Correctness Rate (Shot 0)

100 Time (hrs)

1

80 4

60

40

Correctness Rate (%)

20

0

Llama3.3 Syntactic Correctness Rate (Shot 1)

60

40

Correctness Rate (%)

20

0

Llama3.3 Syntactic Correctness Rate (Shot 3)

100 Time (hrs) 1

80 4

60

40

Correctness Rate (%)

20

0

| libxml2_xml | openssl_x509 | re2_fuzzer |  |  |
| --- | --- | --- | --- | --- |
| bloaty_fuzz_target | sqlite3_ossfuzz |  |  |  |
| curl_curl_fuzzer_http | freetype2_ftfuzzer | libpcap_fuzz_both | libxml2_xml_e85b9b | stb_stbi_read_fuzzer |
| bloaty_fuzz_target_52948c | harfbuzz_hb-shape-fuzzer | jsoncpp_jsoncpp_fuzzer | mbedtls_fuzz_dtlsclient |  |

lcms_cms_transform_fuzzer libpng_libpng_read_fuzzer openh264_decoder_fuzzer proj4_proj_crs_to_crs_fuzzer systemd_fuzz-link-parser

harfbuzz_hb-shape-fuzzer_17863b libjpeg-turbo_libjpeg_turbo_fuzzer mbedtls_fuzz_dtlsclient_7c6b0e openthread_ot-ip6-send-fuzzer php_php-fuzz-parser_0dbedb woff2_convert_woff2ttf_fuzzer

benchmarks

Llama3.3 Response Duplicate Ratio (Shot 0)

Time (hrs)

80 1

4

60

40

Response Duplicate Ratio (%) 20

0

| 100 | Llama3.3 Response Duplicate Ratio (Shot 1) |
| --- | --- |
| 80 | 4 |

60

40

Response Duplicate Ratio (%) 20

0

Llama3.3 Response Duplicate Ratio (Shot 3)

Time (hrs)

80 1 4

60

40

Response Duplicate Ratio (%) 20

0

bloaty_fuzz_target

libxml2_xml_e85b9b

bloaty_fuzz_target_52948c harfbuzz_hb-shape-fuzzer jsoncpp_jsoncpp_fuzzer

lcms_cms_transform_fuzzer libpng_libpng_read_fuzzer mbedtls_fuzz_dtlsclient stb_stbi_read_fuzzer

openh264_decoder_fuzzer

openthread_ot-ip6-send-fuzzer php_php-fuzz-parser_0dbedb proj4_proj_crs_to_crs_fuzzer systemd_fuzz-link-parser vorbis_decode_fuzzer

Benchmarks

Fig. 10. Llama3.3 Response Duplicate Ratio (RDR) for prompt shots 0,

across different prompt shots and time intervals, illustrating

| Function Coverage | 17 | 7 | 5 | 100 | Time (hrs) |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 |  |  |  |  |  |  |  |  |
| Line Coverage | 16 | 8 | 3 | 80 | 4 |  |  |  |  |
| ment | vorbis_decode_fuzzer |  |  |  |  |  |  |  |  |
| This experiment investigates how prompt engineering— | Benchmarks |  |  |  |  |  |  |  |  |
| fectiveness of LLM-guided fuzzing, thereby addressing | R2 | . | Fig. 9. Llama3.3 SCR for prompt shots 0, 1, and 3 against selected |  |  |  |  |  |  |
| proximately | 43 GB of VRAM | ) into the Fuzzbench pipeline | Time (hrs) | 1 |  |  |  |  |  |
| libpng libpng read fuzzer | and | openh264 decoder fuzzer | even | libxml2_xml | openssl_x509 | re2_fuzzer |  |  |  |
| exhibit reduced coverage in four-hour runs. Moreover, anal- | curl_curl_fuzzer_http | freetype2_ftfuzzer | libpcap_fuzz_both | sqlite3_ossfuzz |  |  |  |  |  |
| ysis of LLM response logs revealed that Ollama response | harfbuzz_hb-shape-fuzzer_17863b | libjpeg-turbo_libjpeg_turbo_fuzzer | mbedtls_fuzz_dtlsclient_7c6b0e | woff2_convert_woff2ttf_fuzzer |  |  |  |  |  |
| ity is separately assessed using SCR and RDR metrics. | 1, and 3 against selected benchmarks |  |  |  |  |  |  |  |  |
| the instability caused by varying prompt shots. | Figures 9 | and | 10 | present SCR and RDR for each benchmark |  |  |  |  |  |
| 4.2.1 | Plot Analysis: SCR and RDR Across Benchmarks | response validity and duplication tendencies. Each bench- |  |  |  |  |  |  |  |
| We | compute | both | metrics | based | on | logs | of | each | mark in the plots relates to two fuzzing durations—one- |
| fuzzer–benchmark | pair | execution, | using | structured | log | hour and four-hour runs—with colors distinguishing these |  |  |  |
| analysis tables | . Syntactic-valid responses are counted from | intervals for ease of comparison. |  |  |  |  |  |  |  |
| recorded LLM-generated outputs in the tables, while dupli- | Examining the SCR plots, we observe that SCR rates |  |  |  |  |  |  |  |  |
| cates are detected by comparing the “Final Output” sections | slightly drop for most benchmarks as prompt shots increase, |  |  |  |  |  |  |  |  |
| within the same prompt shot and fuzzer-benchmark pair. | hinting that lengthy or complex prompts may raise the risk |  |  |  |  |  |  |  |  |

---

## Page 10

One-Hour Runtime

Benchmarks

0-shot 1-shot

(%) (%)

shows notable decreases . In the RDR plots, benchmarks such

as re2 fuzzer and openthread ot-ip6-send-fuzzer remain at

diverse mutations. These observations lead to the question

of whether formatting issues or response duplication hin-

code coverage and the syntactic correctness and diversity of

line, branch, and region) with SCR and RDR across different

fuzzing time and prompt shots. These results are presented

4.2.2 Plot Analysis: Coverage vs. SCR

Figures 11 and 12 present the relationship between SCR

and various code coverage metrics as prompt shots change

10

TABLE 2

Branch coverage for multiple prompt shots in Llama3.3.

Branch Coverage: Llama3.3 Prompt Engineering Experiment

Four-Hour Runtime

| 3-shot | AFL++ | 0-shot | 1-shot | 3-shot | AFL++ |
| --- | --- | --- | --- | --- | --- |
| (%) | (%) | (%) | (%) | (%) | (%) |
| 60 | Prompt Shot 0 | IQR (cov, scr): [24.70, 39.11] | Prompt Shot 0 |  |  |
| STD (cov, scr): [18.86, 25.34] | 60 | IQR (cov, scr): [24.81, 39.11] | STD (cov, scr): [18.11, 25.34] |  |  |
| Prompt Shot 1 | IQR (cov, scr): [25.22, 30.22] | Prompt Shot 1 | IQR (cov, scr): [24.75, 30.22] |  |  |

Prompt Shot 3

STD (cov, scr): [18.89, 19.96] Syntactic_Correctness_Rate (%) IQR (cov, scr): [24.87, 19.03] STD (cov, scr): [18.14, 19.96]

20

| Prompt Shot 0 | Prompt Engineering Configurations |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Prompt Shot 1 | Prompt Shot 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 |
| 80 | 80 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Prompt Shot 1

40 STD (cov, scr): [18.05, 24.06] IQR (cov, scr): [21.48, 30.22]

40 STD (cov, scr): [20.12, 24.06]

Prompt Shot 3

| Syntactic_Correctness_Rate (%) | IQR (cov, scr): [21.31, 19.03] | Prompt Shot 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| STD (cov, scr): [18.26, 19.96] | Syntactic_Correctness_Rate (%) | IQR (cov, scr): [21.81, 19.03] | STD (cov, scr): [20.24, 19.96] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Prompt Shot 0 | Prompt Engineering Configurations |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Prompt Shot 1 | Prompt Shot 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 |

at one-hour time interval

| freetype2 ftfuzzer | 37.66 | 37.27 | 37.29 | 36.94 | 39.47 | 40.01 | 40.26 | 38.72 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| libxml2 xml | 13.59 | 22.17 | 13.59 | 23.88 | 13.42 | 13.59 | 13.59 | 24.77 |  |
| libpng libpng read fuzzer | 32.72 | 32.95 | 32.95 | 33.17 | 32.90 | 32.77 | 32.80 | 33.57 |  |
| bloaty fuzz target | 5.73 | 5.73 | 6.74 | 7.20 | 6.22 | 6.20 | 5.73 | 7.69 |  |
| curl curl fuzzer http | 12.72 | 12.78 | 12.65 | 13.07 | 12.69 | 12.66 | 12.67 | 13.35 |  |
| harfbuzz hb-shape-fuzzer | 44.21 | 44.21 | 44.21 | 61.17 | 44.21 | 44.21 | 44.21 | 63.44 |  |
| jsoncpp jsoncpp fuzzer | 24.41 | 24.41 | 0.42 | 24.46 | 0.42 | 0.42 | 0.42 | 24.46 |  |
| lcms cms transform fuzzer | 0.50 | 0.50 | 20.26 | 23.56 | 23.07 | 25.34 | 22.83 | 19.39 |  |
| libjpeg-turbo libjpeg turbo fuzzer | 26.39 | 26.39 | 26.39 | 26.69 | 26.39 | 26.39 | 26.39 | 26.70 |  |
| libpcap fuzz both | 36.48 | 36.51 | 37.91 | 37.83 | 35.66 | 34.16 | 34.67 | 40.24 |  |
| mbedtls fuzz dtlsclient | 9.84 | 9.84 | 9.84 | 14.16 | 13.03 | 13.44 | 9.84 | 14.42 |  |
| openh264 decoder fuzzer | 74.53 | 74.34 | 74.55 | 74.52 | 76.40 | 76.00 | 75.42 | 76.10 |  |
| openssl x509 | 10.72 | 10.72 | 10.72 | 10.80 | 10.72 | 10.72 | 10.72 | 10.83 |  |
| openthread ot-ip6-send-fuzzer | 11.20 | 10.29 | 11.43 | 11.41 | 11.23 | 10.94 | 11.20 | 11.50 |  |
| proj4 proj crs to crs fuzzer | 8.81 | 8.41 | 9.05 | 9.11 | 10.60 | 10.35 | 10.50 | 10.73 |  |
| re2 fuzzer | 62.89 | 62.55 | 63.00 | 64.27 | 64.02 | 63.85 | 64.07 | 64.34 |  |
| sqlite3 ossfuzz | 26.91 | 26.91 | 26.91 | 45.58 | 26.91 | 26.91 | 26.91 | 63.30 |  |
| stb stbi read fuzzer | 55.08 | 55.08 | 55.08 | 68.51 | 55.08 | 55.08 | 55.08 | 69.40 |  |
| systemd fuzz-link-parser | 22.90 | 21.90 | 22.10 | 22.30 | 21.90 | 22.30 | 22.20 | 22.30 |  |
| vorbis decode fuzzer | 30.47 | 30.49 | 30.47 | 30.86 | 30.54 | 30.54 | 30.59 | 30.83 |  |
| woff2 convert woff2ttf fuzzer | 17.02 | 17.02 | 17.02 | 26.05 | 17.02 | 17.02 | 17.02 | 26.74 |  |
| php php-fuzz-parser 0dbedb | 9.67 | 9.62 | 9.62 | 9.74 | 9.93 | 9.86 | 9.87 | 9.90 |  |
| mbedtls fuzz dtlsclient 7c6b0e | 13.69 | 13.73 | 13.58 | 13.48 | 13.69 | 13.74 | 13.86 | 13.67 |  |
| libxml2 xml e85b9b | 23.06 | 20.97 | 20.99 | 23.49 | 20.18 | 13.42 | 23.14 | 28.53 |  |
| harfbuzz hb-shape-fuzzer 17863b | 45.02 | 45.02 | 45.02 | 55.09 | 45.02 | 45.02 | 45.02 | 59.77 |  |
| bloaty fuzz target 52948c | 5.73 | 6.11 | 6.06 | 6.55 | 6.33 | 5.84 | 6.44 | 7.38 |  |
| of formatting errors. Benchmarks like openthread ot-ip6- | Llama3.3 | Coverage vs. Syntactic Correctness Rate (SCR) Plots (time=1h) |  |  |  |  |  |  |  |
| send-fuzzer | and | woff2 convert woff2ttf fuzzer | maintain | 100 | Branch | Coverage vs. SCR (time=1h) | 100 | Function | Coverage vs. SCR (time=1h) |
| consistently high SCR values; while vorbis decode fuzzer | 80 | 80 |  |  |  |  |  |  |  |
| low values across all prompt shots, suggesting effective | 40 | STD (cov, scr): [18.71, 24.06] | 40 | STD (cov, scr): [18.01, 24.06] |  |  |  |  |  |
| response diversification; whereas mbedtls fuzz dtlsclient | Syntactic_Correctness_Rate (%) | IQR (cov, scr): [25.31, 19.03] | Prompt Shot 3 |  |  |  |  |  |  |
| and woff2 convert woff2ttf fuzzer show high RDR values, | Prompt Engineering Configurations | 20 |  |  |  |  |  |  |  |
| indicating frequent repetition in LLM outputs that may limit | 0 | Prompt Shot 3 | Prompt Shot 1 | Prompt Shot 3 |  |  |  |  |  |
| the LLM’s ability to explore new execution paths through | 100 | Line | Coverage vs. SCR (time=1h) | 100 | Region | Coverage vs. SCR (time=1h) |  |  |  |

der the mutation process and, in turn, the code coverage 60 Prompt Shot 0 IQR (cov, scr): [21.06, 39.11] STD (cov, scr): [18.16, 25.34] 60 Prompt Shot 0 IQR (cov, scr): [21.46, 39.11] STD (cov, scr): [20.20, 25.34]

| achieved by the fuzzer. To explore the relationship between | IQR (cov, scr): [21.21, 30.22] | Prompt Shot 1 |  |  |
| --- | --- | --- | --- | --- |
| LLM-generated responses, we generated additional visual- | 20 | Prompt Engineering Configurations | 20 |  |
| izations correlating various code coverage types (function, | 0 | Prompt Shot 3 | Prompt Shot 1 | Prompt Shot 3 |
| and discussed in the following sections. | Fig. 11. Llama3.3 Coverage vs SCR plots for prompt shots 0, 1, and 3 |  |  |  |
| over time. Each figure combines scatter and | Kernel Density | prompt shots | . Although some outliers exist, 3-shot prompts |  |
| Estimate (KDE) | plots to highlight trends and correlations. | exhibit a more concentrated and predictable SCR distribu- |  |  |
| Each data point represents a benchmark–fuzzer pair, with | tion, with slightly narrower spreads and more centralized |  |  |  |
| different prompt shots indicated by distinct colors—blue, | coverage than 0- and 1-shot prompts. This suggests that ad- |  |  |  |
| orange, and green. The colored bands show the interquartile | ditional examples help stabilize LLM formatting. Across all |  |  |  |
| range (IQR) between the 0.25 and 0.75 quantiles, highlight- | prompt shots, SCR values cluster around | 70–80% | , reflecting |  |
| ing where most data points lie for each prompt shot. | The | an ”L-shaped” pattern in the plots: code coverage rises with |  |  |
| plots reveal that SCR values generally | decrease with increased | SCR initially but plateaus beyond this range. |  |  |

---

## Page 11

Llama3.3 Coverage vs. Syntactic Correctness Rate (SCR) Plots (time=4h)

80 80

STD (cov, scr): [18.13, 22.40]

Prompt Shot 1 IQR (cov, scr): [22.44, 37.23] Prompt Shot 1

40 STD (cov, scr): [18.22, 28.41]

Prompt Shot 3

Syntactic_Correctness_Rate (%) IQR (cov, scr): [23.36, 19.40] Prompt Shot 3

STD (cov, scr): [18.13, 18.71]

| 20 | Prompt Engineering Configurations | 20 |  |
| --- | --- | --- | --- |
| Prompt Shot 0 | Prompt Engineering Configurations |  |  |
| Prompt Shot 1 | Prompt Shot 0 |  |  |
| 0 | Prompt Shot 3 | Prompt Shot 1 | Prompt Shot 3 |
| 80 | 80 |  |  |

STD (cov, scr): [20.38, 22.40]

| Prompt Shot 1 | IQR (cov, scr): [20.48, 37.23] | Prompt Shot 1 |
| --- | --- | --- |
| 40 | STD (cov, scr): [20.41, 28.41] |  |
| Prompt Shot 3 | Prompt Shot 3 |  |

STD (cov, scr): [20.35, 18.71]

| 20 | Prompt Engineering Configurations | 20 |  |
| --- | --- | --- | --- |
| Prompt Shot 0 | Prompt Engineering Configurations |  |  |
| 0 | Prompt Shot 3 | Prompt Shot 1 | Prompt Shot 3 |

at four-hour time interval

Llama3.3 Coverage vs. Response Duplication Rate (RDR) Plots (time=1h)

| 80 | 80 |  |  |
| --- | --- | --- | --- |
| 60 | Prompt Shot 0 | IQR (cov, rdr): [24.70, 22.74] | Prompt Shot 0 |
| Prompt Shot 1 | IQR (cov, rdr): [25.22, 62.04] | Prompt Shot 1 |  |
| 40 | STD (cov, rdr): [18.01, 34.98] |  |  |

Response Duplicate Rate (%) Prompt Shot 3 IQR (cov, rdr): [25.31, 52.32] STD (cov, rdr): [18.89, 28.38] Response Duplicate Rate (%) Prompt Shot 3 IQR (cov, rdr): [24.87, 52.32] STD (cov, rdr): [18.14, 28.38]

| 20 | Prompt Engineering Configurations | 20 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Prompt Shot 0 | Prompt Engineering Configurations |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Prompt Shot 1 | Prompt Shot 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | Prompt Shot 3 | Prompt Shot 1 | Prompt Shot 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 |

100

| 40 | STD (cov, rdr): [18.05, 34.98] | 40 | STD (cov, rdr): [20.12, 34.98] |
| --- | --- | --- | --- |
| STD (cov, rdr): [18.26, 28.38] | Response Duplicate Rate (%) | STD (cov, rdr): [20.24, 28.38] |  |
| Prompt Shot 0 | Prompt Engineering Configurations |  |  |
| Prompt Shot 1 | Prompt Shot 0 |  |  |

4.2.3 Plot Analysis: Coverage vs. RDR

cluster at lower coverage, indicating that repeated responses

11

Llama3.3 Coverage vs. Response Duplication Rate (RDR) Plots (time=4h)

80 80

IQR (cov, rdr): [24.81, 31.23] STD (cov, rdr): [18.13, 27.12]

40 STD (cov, rdr): [19.08, 31.25] IQR (cov, rdr): [24.82, 37.40]

40 STD (cov, rdr): [18.22, 31.25]

IQR (cov, rdr): [24.75, 56.43] STD (cov, rdr): [18.13, 30.82]

20

| Prompt Engineering Configurations | 20 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Prompt Shot 0 | Prompt Engineering Configurations |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Prompt Shot 1 | Prompt Shot 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | Prompt Shot 3 | Prompt Shot 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 |
| 80 | 80 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

IQR (cov, rdr): [20.62, 31.23] STD (cov, rdr): [20.38, 27.12]

| STD (cov, rdr): [18.45, 31.25] | IQR (cov, rdr): [20.70, 37.40] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | 40 | STD (cov, rdr): [20.41, 31.25] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STD (cov, rdr): [18.36, 30.82] | Response Duplicate Rate (%) | IQR (cov, rdr): [21.49, 56.43] | STD (cov, rdr): [20.35, 30.82] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20 | Prompt Engineering Configurations | 20 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Prompt Shot 1 | Prompt Shot 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Prompt Shot 3 | Prompt Shot 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 |

at four-hour time interval

toward narrower coverage and higher RDRs in longer runs.

These observations imply that increasing prompt shots can

4.3 Multiple LLMs Comparison Experiment

state-of-the-art LLMs under our mutation strategies, thereby

setup mirrors that of the Section 4.2 experiment. Each LLM

shots, and two time intervals. After each run, final code

coverage was recorded. Based on these records, Table 3 sum-

marizes how often each LLM achieved the highest coverage

hold for longer runs.

100 Branch Coverage vs. SCR (time=4h) 100 Function Coverage vs. SCR (time=4h) 100 Branch Coverage vs. RDR (time=4h) 100 Function Coverage vs. RDR (time=4h)

60 Prompt Shot 0 IQR (cov, scr): [23.38, 20.28] STD (cov, scr): [19.02, 22.40] 60 Prompt Shot 0 IQR (cov, scr): [24.81, 20.28] 60 Prompt Shot 0 IQR (cov, rdr): [23.38, 31.23] STD (cov, rdr): [19.02, 27.12] 60 Prompt Shot 0

40 STD (cov, scr): [19.08, 28.41] IQR (cov, scr): [24.82, 37.23] Prompt Shot 1 IQR (cov, rdr): [22.44, 37.40] Prompt Shot 1

STD (cov, scr): [19.00, 18.71] Syntactic_Correctness_Rate (%) IQR (cov, scr): [24.75, 19.40] Response Duplicate Rate (%) Prompt Shot 3 IQR (cov, rdr): [23.36, 56.43] STD (cov, rdr): [19.00, 30.82] Response Duplicate Rate (%) Prompt Shot 3

0 10 20 30 Coverage (%) 40 50 60 70 80 0 0 10 20 30 Coverage (%) 40 50 60 70 80 0 10 20 30 0 Prompt Shot 3

100 Line Coverage vs. SCR (time=4h) 100 Region Coverage vs. SCR (time=4h) 100 Line Coverage vs. RDR (time=4h) 100 Region Coverage vs. RDR (time=4h)

60 Prompt Shot 0 IQR (cov, scr): [20.55, 20.28] STD (cov, scr): [18.38, 22.40] 60 Prompt Shot 0 IQR (cov, scr): [20.62, 20.28] 60 Prompt Shot 0 IQR (cov, rdr): [20.55, 31.23] STD (cov, rdr): [18.38, 27.12] 60 Prompt Shot 0

40 STD (cov, scr): [18.45, 28.41] IQR (cov, scr): [20.70, 37.23] Prompt Shot 1 IQR (cov, rdr): [20.48, 37.40] Prompt Shot 1

Syntactic_Correctness_Rate (%) IQR (cov, scr): [21.01, 19.40] STD (cov, scr): [18.36, 18.71] Syntactic_Correctness_Rate (%) IQR (cov, scr): [21.49, 19.40] Response Duplicate Rate (%) Prompt Shot 3 IQR (cov, rdr): [21.01, 56.43] Prompt Shot 3

| Prompt Shot 1 | Prompt Shot 0 | Prompt Shot 0 | Prompt Engineering Configurations |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 0 | Prompt Shot 3 |
| Fig. 12. Llama3.3 Coverage vs SCR plots for prompt shots 0, 1, and 3 | Fig. 14. Llama3.3 Coverage vs RDR plots for prompt shots 0, 1, and 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 100 | Branch | Coverage vs. RDR (time=1h) | 100 | Function | Coverage vs. RDR (time=1h) | densities in lower duplication regions early on, but shifting |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STD (cov, rdr): [18.86, 25.36] | 60 | IQR (cov, rdr): [24.81, 22.74] | STD (cov, rdr): [18.11, 25.36] | generate more effective mutated inputs only when LLM |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 40 | STD (cov, rdr): [18.71, 34.98] | IQR (cov, rdr): [24.75, 62.04] | response duplication remains low. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 100 | Line | Coverage vs. RDR (time=1h) | Region | Coverage vs. RDR (time=1h) | This experiment evaluates the relative efficiency of multiple |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 80 | 80 | addressing | R3 | and | R4 | . Based on the results of the | Section 4.2 | , |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

60 Prompt Shot 0 IQR (cov, rdr): [21.06, 22.74] STD (cov, rdr): [18.16, 25.36] 60 Prompt Shot 0 IQR (cov, rdr): [21.46, 22.74] STD (cov, rdr): [20.20, 25.36] we selected six benchmarks with high code coverage vari-

| Prompt Shot 1 | IQR (cov, rdr): [21.21, 62.04] | Prompt Shot 1 | IQR (cov, rdr): [21.48, 62.04] | ance, along with LLMs— | Llama3.3 | [23], | Deepseek-r1-Distill- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Response Duplicate Rate (%) | Prompt Shot 3 | IQR (cov, rdr): [21.31, 52.32] | Prompt Shot 3 | IQR (cov, rdr): [21.81, 52.32] | Llama-70B | [24], | QwQ-32B | [26], and | Gemma3-27B | [25]—for |  |  |  |  |  |  |  |  |  |  |  |
| 20 | Prompt Engineering Configurations | 20 | this test. Since Llama3.3 had already been evaluated on |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | Prompt Shot 3 | Prompt Shot 1 | Prompt Shot 3 | these benchmarks in earlier experiments, it was excluded |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | from execution but retained as a reference. The experimental |

Fig. 13. Llama3.3 Coverage vs RDR plots for prompt shots 0, 1, and 3 was evaluated in a fresh fuzzing session, loaded alone in

| at one-hour time interval | Ollama, and tested across all six benchmarks, three prompt |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Beyond syntactic correctness and conversion stability, the | at different runtimes. The results indicate that | Llama3.3 | con- |  |  |
| diversity of LLM-generated mutations plays a vital role | sistently outperforms other models during short (i.e., one |  |  |  |  |
| in effective fuzzing. Repetitive or identical LLM outputs | hour) runs, whereas | Deepseek-r1-Distill-Llama-70B | performs |  |  |
| may reduce mutation variety and can limit code path ex- | best mostly in four-hour runs. Additionally, | Table 4 | reports |  |  |
| ploration, even if syntactically valid. To assess this factor, | the percentage gain (i.e., CIP) of the | best-performing | LLM- |  |  |
| Figures 13 and 14 | present scatter and KDE plots relating RDR | guided fuzzer over the AFL++ baseline for each prompt |  |  |  |
| to final code coverage across various prompt shots and time | shot, based on branch coverage. Among the six benchmarks |  |  |  |  |
| intervals, where plot colors correspond to the prompt shots. | evaluated for branch coverage with 3-shot prompts, | four |  |  |  |
| The plots show that lower RDRs generally correspond | benchmarks | show positive CIPs in one-hour runs, indicating |  |  |  |
| to higher code coverage, suggesting that | greater response | that LLM-guided fuzzers generally outperform the AFL++ |  |  |  |
| diversity promotes more effective fuzzing | ; whereas higher RDRs | baseline in short runs, though this trend does not always |  |  |  |
| limit | novel input generation. This trend is more evident | To determine which LLM performs best overall and |  |  |  |
| with the four-hour fuzzing interval. KDE plots reinforce | answer | R4 | , we next analyze model response quality in terms |  |  |
| this interpretation: | 3-shot prompts | generate more duplicate | of syntactic correctness (SCR) and response diversity (RDR). |  |  |
| responses overall, retaining broader coverage and higher | We first evaluated the | SCR | and | RDR | metrics for each LLM |

---

## Page 12

TABLE 3

results for each LLM fuzzer.

| Coverage-type | Gemma3 |  |  |  |
| --- | --- | --- | --- | --- |
| Line Coverage | 8 | 2 | 5 | 3 |
| Region Coverage | 10 | 2 | 4 | 3 |

Llama Deepseek QwQ

Region Coverage 4 6 4 6

Multiple LLM - Coverage vs. Syntactic Correctness Rate (SCR) Plots (time=1h)

STD (cov, scr): [14.63, 17.87]

STD (cov, scr): [14.68, 19.36]

| 20 | STD (cov, scr): [14.58, 22.74] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Deepseek-r1-Distill-Llama-70B | QwQ-32B | Gemma3-27B | IQR (cov, scr): [24.03, 16.46] | Llama3.3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Gemma3-27B | STD (cov, scr): [21.74, 16.39] | Deepseek-r1-Distill-Llama-70B | QwQ-32B | Gemma3-27B | IQR (cov, scr): [17.87, 16.46] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | Gemma3-27B | STD (cov, scr): [14.62, 16.39] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 |

STD (cov, scr): [23.41, 17.87]

IQR (cov, scr): [28.20, 27.44]

STD (cov, scr): [23.49, 19.36]

| Syntactic_Correctness_Rate (%) | QwQ-32B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| STD (cov, scr): [20.14, 22.74] | Large Language Models | IQR (cov, scr): [27.68, 23.20] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20 | Llama3.3 | 20 | STD (cov, scr): [23.48, 22.74] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Deepseek-r1-Distill-Llama-70B | QwQ-32B | Gemma3-27B | IQR (cov, scr): [26.01, 16.46] | Llama3.3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Gemma3-27B | STD (cov, scr): [20.31, 16.39] | Deepseek-r1-Distill-Llama-70B | QwQ-32B | Gemma3-27B | IQR (cov, scr): [27.95, 16.46] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Gemma3-27B | STD (cov, scr): [23.65, 16.39] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 |

Fig. 15. Multiple LLMs Coverage vs SCR for one-hour runtime

across all three prompt shots, then plotted code coverage

However, its SCR declines when the fuzzing period is ex-

tended to four hours, suggesting that formatting consistency

shots and coverage types in one-hour runs, indicating weaker

12

Multiple LLM - Coverage vs. Syntactic Correctness Rate (SCR) Plots (time=4h)

| 80 | 80 |  |  |  |
| --- | --- | --- | --- | --- |
| 60 | Llama3.3 |  |  |  |
| STD (cov, scr): [22.12, 19.36] | IQR (cov, scr): [19.41, 15.85] | STD (cov, scr): [14.79, 19.36] |  |  |
| 40 | Deepseek-r1-Distill-Llama-70B | IQR (cov, scr): [25.79, 22.08] | 40 | Deepseek-r1-Distill-Llama-70B |
| Syntactic_Correctness_Rate (%) | QwQ-32B |  |  |  |
| 20 | Large Language Models | STD (cov, scr): [22.25, 9.65] | Large Language Models | IQR (cov, scr): [18.95, 16.66] |
| 20 | STD (cov, scr): [14.78, 9.65] |  |  |  |

Llama3.3

| Gemma3-27B | STD (cov, scr): [22.16, 9.71] | IQR (cov, scr): [19.17, 17.68] | STD (cov, scr): [14.74, 9.71] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 |
| 80 | 80 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STD (cov, scr): [20.66, 19.36] | IQR (cov, scr): [31.39, 15.85] | STD (cov, scr): [23.99, 19.36] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STD (cov, scr): [20.55, 13.42] | IQR (cov, scr): [30.37, 22.08] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Syntactic_Correctness_Rate (%) | QwQ-32B | IQR (cov, scr): [28.31, 16.66] | Syntactic_Correctness_Rate (%) | QwQ-32B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20 | STD (cov, scr): [24.04, 9.65] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Deepseek-r1-Distill-Llama-70B | QwQ-32B | Gemma3-27B | IQR (cov, scr): [28.49, 17.68] | Llama3.3 | Deepseek-r1-Distill-Llama-70B | QwQ-32B | Gemma3-27B |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 |

Fig. 16. Multiple LLMs Coverage vs SCR for four-hour runtime

Branch Coverage vs. RDR (time=1h)

| Llama3.3 | IQR (cov, rdr): [24.83, 16.46] | 70 | Large Language Models | Llama3.3 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Deepseek-r1-Distill-Llama-70B | STD (cov, rdr): [21.60, 13.81] | Llama3.3 | IQR (cov, rdr): [18.29, 16.46] |  |  |  |  |  |
| Deepseek-r1-Distill-Llama-70B | STD (cov, rdr): [14.63, 13.81] |  |  |  |  |  |  |  |
| 60 | QwQ-32B | Gemma3-27B | Deepseek-r1-Distill-Llama-70B | IQR (cov, rdr): [23.89, 14.32] | 60 | QwQ-32B | Gemma3-27B | Deepseek-r1-Distill-Llama-70B |
| 50 | QwQ-32B | IQR (cov, rdr): [23.89, 19.33] | 50 | QwQ-32B |  |  |  |  |
| 40 | Gemma3-27B | IQR (cov, rdr): [24.03, 21.88] | 40 | Gemma3-27B |  |  |  |  |
| 30 | 30 |  |  |  |  |  |  |  |
| Response Duplicate Rate (%) | 20 | Response Duplicate Rate (%) | 20 |  |  |  |  |  |
| 10 | 10 |  |  |  |  |  |  |  |

Line Coverage vs. RDR (time=1h)

| Llama3.3 | IQR (cov, rdr): [26.57, 16.46] | 70 | Large Language Models | Llama3.3 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Deepseek-r1-Distill-Llama-70B | STD (cov, rdr): [20.10, 13.81] | Llama3.3 | IQR (cov, rdr): [28.70, 16.46] |  |  |  |  |  |
| Deepseek-r1-Distill-Llama-70B | STD (cov, rdr): [23.41, 13.81] |  |  |  |  |  |  |  |
| 60 | QwQ-32B | Gemma3-27B | Deepseek-r1-Distill-Llama-70B | IQR (cov, rdr): [26.20, 14.32] | 60 | QwQ-32B | Gemma3-27B | Deepseek-r1-Distill-Llama-70B |
| 50 | QwQ-32B | IQR (cov, rdr): [25.65, 19.33] | 50 | QwQ-32B |  |  |  |  |

STD (cov, rdr): [21.92, 15.31]

| 40 | Gemma3-27B | IQR (cov, rdr): [26.01, 21.88] | 40 | Gemma3-27B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| STD (cov, rdr): [20.31, 18.13] | IQR (cov, rdr): [27.95, 21.88] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 30 | 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Response Duplicate Rate (%) | 20 | Response Duplicate Rate (%) | 20 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 |

Fig. 17. Multiple LLMs Coverage vs RDR for one-hour runtime

4.4 Discussion

| The number of benchmarks that has the maximum code coverage | 100 | Branch | Coverage vs. SCR (time=4h) | 100 | Function | Coverage vs. SCR (time=4h) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Counts of Maximum Code Coverage for LLM Fuzzers | IQR (cov, scr): [27.20, 15.85] | 60 | Llama3.3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| RunTime = 1 Hour | STD (cov, scr): [22.19, 13.42] | IQR (cov, scr): [18.52, 22.08] | STD (cov, scr): [14.78, 13.42] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Llama | Deepseek | QwQ | IQR (cov, scr): [26.63, 16.66] | Syntactic_Correctness_Rate (%) | QwQ-32B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| v3.3 | -r1 | -32B | Deepseek-r1-Distill-Llama-70B | QwQ-32B | Gemma3-27B | IQR (cov, scr): [26.55, 17.68] | Llama3.3 | Deepseek-r1-Distill-Llama-70B | QwQ-32B | Gemma3-27B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Branch Coverage | 7 | 3 | 4 | 4 | 0 | 0 | Gemma3-27B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Function Coverage | 9 | 6 | 6 | 4 | 100 | Line | Coverage vs. SCR (time=4h) | 100 | Region | Coverage vs. SCR (time=4h) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| RunTime = 4 Hour | 60 | Llama3.3 | IQR (cov, scr): [29.11, 15.85] | 60 | Llama3.3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Coverage-type | Gemma3 | 40 | Deepseek-r1-Distill-Llama-70B | IQR (cov, scr): [25.33, 22.08] | 40 | Deepseek-r1-Distill-Llama-70B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| v3.3 | -r1 | -32B | STD (cov, scr): [24.20, 13.42] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Branch Coverage | 6 | 7 | 4 | 5 | 20 | Llama3.3 | Large Language Models | STD (cov, scr): [20.71, 9.65] | Large Language Models | IQR (cov, scr): [30.43, 16.66] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Function Coverage | 8 | 7 | 6 | 7 | Gemma3-27B | STD (cov, scr): [20.66, 9.71] | IQR (cov, scr): [30.49, 17.68] | STD (cov, scr): [23.98, 9.71] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Line Coverage | 4 | 6 | 4 | 5 | 0 | 0 | Gemma3-27B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 100 | Branch | Coverage vs. SCR (time=1h) | 100 | Function | Coverage vs. SCR (time=1h) | Multiple LLM - Coverage vs. Response Duplication Rate (RDR) Plots (time=1h) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 80 | 80 | 70 | Large Language Models | Llama3.3 | Function | Coverage vs. RDR (time=1h) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 60 | Llama3.3 | IQR (cov, scr): [24.83, 22.47] | 60 | Llama3.3 | STD (cov, rdr): [21.59, 12.37] | IQR (cov, rdr): [17.84, 14.32] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STD (cov, scr): [21.60, 17.87] | IQR (cov, scr): [18.29, 22.47] | STD (cov, rdr): [14.68, 12.37] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 40 | Deepseek-r1-Distill-Llama-70B | IQR (cov, scr): [23.89, 27.44] | 40 | Deepseek-r1-Distill-Llama-70B | STD (cov, rdr): [20.43, 15.31] | IQR (cov, rdr): [17.65, 19.33] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STD (cov, scr): [21.59, 19.36] | IQR (cov, scr): [17.84, 27.44] | STD (cov, rdr): [14.03, 15.31] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Syntactic_Correctness_Rate (%) | QwQ-32B | IQR (cov, scr): [24.05, 23.20] | Syntactic_Correctness_Rate (%) | QwQ-32B | STD (cov, rdr): [21.74, 18.13] | IQR (cov, rdr): [17.87, 21.88] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20 | Llama3.3 | Large Language Models | STD (cov, scr): [21.62, 22.74] | Large Language Models | IQR (cov, scr): [17.61, 23.20] | STD (cov, rdr): [14.62, 18.13] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 100 | Line | Coverage vs. SCR (time=1h) | 100 | Region | Coverage vs. SCR (time=1h) | 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 |
| 80 | 80 | 70 | Large Language Models | Llama3.3 | Region | Coverage vs. RDR (time=1h) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 60 | Llama3.3 | IQR (cov, scr): [26.57, 22.47] | 60 | Llama3.3 | STD (cov, rdr): [20.20, 12.37] | IQR (cov, rdr): [28.20, 14.32] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STD (cov, scr): [20.10, 17.87] | IQR (cov, scr): [28.70, 22.47] | STD (cov, rdr): [23.49, 12.37] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 40 | Deepseek-r1-Distill-Llama-70B | IQR (cov, scr): [26.20, 27.44] | STD (cov, scr): [20.20, 19.36] | 40 | Deepseek-r1-Distill-Llama-70B | STD (cov, rdr): [19.05, 15.31] | IQR (cov, rdr): [27.69, 19.33] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Large Language Models | IQR (cov, scr): [25.64, 23.20] | Syntactic_Correctness_Rate (%) | QwQ-32B | STD (cov, rdr): [23.65, 18.13] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| for all selected LLMs against these metrics. | Figures 15 and 16 | tently achieves low RDR—especially in long-term fuzzing. It |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| visualize the relationship between coverage and SCR across | shows a relatively high SCR variability but centralized low- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LLMs and prompt shots; and | Figures 17 and 18 | present the | RDR densities, indicating frequent production of diverse |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| correlation between coverage and RDR. | and well-formatted inputs that sustain stable code cov- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The SCR plots reveal that all models achieve higher | erage performance. In contrast, | Gemma3-27B | demonstrates |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| syntactic correctness alongside improved code coverage. | scattered RDR values, suggesting frequent generation of |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Llama3.3 | consistently maintains | the strongest SCR-coverage | repetitive responses. | Llama3.3 | shows low RDR but with |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| correlation | in one-hour runs, with its KDE plots concen- | greater coverage variability compared to Deepseek. | QwQ- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| trated in high SCR and moderate-to-high coverage regions. | 32B | remains mid-range in both diversity and coverage. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| may degrade over time and could benefit from runtime | After evaluating experimental results using four key met- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| constraints. | Deepseek-r1-Distill-Llama-70B | shows higher SCR | rics—detailed code coverage, CIP, SCR, and RDR—we ana- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| variability with a slightly narrower coverage spread than | lyzed trends to explore how LLM syntactic correctness and |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Llama3.3, indicating | higher sensitivity to response fluctuations | . | response diversity influence fuzzing performance. Together, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Despite unstable syntactic correctness in longer runs, the | these metrics establish a comprehensive basis for addressing |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| model still maintains | consistent coverage | . | Gemma3-27B | shows | our research questions. The following sections highlight key |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| low SCR and scattered KDE distributions across prompt | findings drawn from the tables and plots in the results. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| formatting consistency | and less promising early-stage cov- | 4.4.1 | Observation 1: Findings Related to R2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| erage than Deepseek. | QwQ-32B | offers relatively balanced | The Llama3.3 prompt-engineering experiments reveal that |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| coverage with moderate variability, but its low SCR values | increasing prompt shots does not consistently improve code cov- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| in four-hour runs indicate limited formatting reliability. | erage | . While some benchmarks benefit from additional in- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| In the RDR plots, | Deepseek-r1-Distill-Llama-70B | consis- | context examples, others show negligible or even negative |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 13

Shot Benchmarks

LLM

(%)

| freetype2 ftfuzzer | 37.66 |
| --- | --- |
| libpng libpng read fuzzer | 32.72 |
| curl curl fuzzer http | 12.78 |

0

| libpcap fuzz both | 36.48 |
| --- | --- |
| openh264 decoder fuzzer | 75.05 |
| openthread ot-ip6-send-fuzzer | 11.23 |
| freetype2 ftfuzzer | 37.27 |
| libpng libpng read fuzzer | 33.01 |
| curl curl fuzzer http | 12.79 |

1

| libpcap fuzz both | 39.08 |
| --- | --- |
| openh264 decoder fuzzer | 75.31 |
| openthread ot-ip6-send-fuzzer | 11.2 |
| freetype2 ftfuzzer | 37.34 |
| libpng libpng read fuzzer | 32.95 |
| curl curl fuzzer http | 12.79 |

3

| libpcap fuzz both | 37.91 |
| --- | --- |
| openh264 decoder fuzzer | 75.31 |
| openthread ot-ip6-send-fuzzer | 11.43 |

Branch Coverage vs. RDR (time=4h)

| 70 | Large Language Models | Llama3.3 | Function | Coverage vs. RDR (time=4h) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Llama3.3 | IQR (cov, rdr): [27.34, 16.95] | 70 | Large Language Models | Llama3.3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Deepseek-r1-Distill-Llama-70B | STD (cov, rdr): [22.80, 11.98] | Llama3.3 | IQR (cov, rdr): [19.45, 16.95] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Deepseek-r1-Distill-Llama-70B | STD (cov, rdr): [15.18, 11.98] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 60 | QwQ-32B | Gemma3-27B | Deepseek-r1-Distill-Llama-70B | IQR (cov, rdr): [25.79, 12.84] | 60 | QwQ-32B | Gemma3-27B | Deepseek-r1-Distill-Llama-70B |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 50 | QwQ-32B | IQR (cov, rdr): [26.63, 14.95] | 50 | QwQ-32B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 40 | Gemma3-27B | IQR (cov, rdr): [26.55, 17.19] | 40 | Gemma3-27B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STD (cov, rdr): [22.16, 18.87] | IQR (cov, rdr): [19.17, 17.19] | STD (cov, rdr): [14.74, 18.87] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Line | Coverage vs. RDR (time=4h) | Region | Coverage vs. RDR (time=4h) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 70 | Large Language Models | Llama3.3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Llama3.3 | IQR (cov, rdr): [29.24, 16.95] | STD (cov, rdr): [21.24, 11.98] | 70 | Large Language Models | Llama3.3 | IQR (cov, rdr): [31.50, 16.95] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 50 | QwQ-32B | IQR (cov, rdr): [28.31, 14.95] | QwQ-32B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 40 | Gemma3-27B | IQR (cov, rdr): [28.49, 17.19] | 40 | Gemma3-27B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STD (cov, rdr): [20.66, 18.87] | IQR (cov, rdr): [30.49, 17.19] | STD (cov, rdr): [23.98, 18.87] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Response Duplicate Rate (%) | 20 | Response Duplicate Rate (%) | 20 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 |

CIP results demonstrate that no single LLM consistently

prompt shots. While some LLMs exceed AFL++’s perfor-

13

TABLE 4

Branch coverage for multiple LLMs comparison experiments.

Branch Coverage: Multiple LLMs Comparison Experiment

| One-Hour Runtime | Four-Hour Runtime |  |  |  |
| --- | --- | --- | --- | --- |
| AFL++ | CIP | LLM | AFL++ | CIP |
| (%) | (%) | (%) | (%) | (%) |
| 36.94 | 0.72 | 39.47 | 38.72 | 0.75 |
| 33.17 | -0.45 | 33.32 | 33.57 | -0.25 |
| 13.07 | -0.29 | 12.76 | 13.35 | -0.59 |
| 37.83 | -1.35 | 35.66 | 40.24 | -4.58 |
| 74.52 | 0.53 | 76.48 | 76.10 | 0.38 |
| 11.41 | -0.18 | 11.28 | 11.50 | -0.22 |
| 36.94 | 0.33 | 40.01 | 38.72 | 1.29 |
| 33.17 | -0.16 | 32.82 | 33.57 | -0.75 |
| 13.07 | -0.28 | 12.67 | 13.35 | -0.68 |
| 37.83 | 1.25 | 38.22 | 40.24 | -2.02 |
| 74.52 | 0.79 | 76.41 | 76.10 | 0.31 |
| 11.41 | -0.21 | 11.34 | 11.50 | -0.16 |
| 36.94 | 0.40 | 40.26 | 38.72 | 1.54 |
| 33.17 | -0.22 | 32.80 | 33.57 | -0.77 |
| 13.07 | -0.28 | 12.80 | 13.35 | -0.55 |
| 37.83 | 0.08 | 34.99 | 40.24 | -5.25 |
| 74.52 | 0.79 | 76.34 | 76.10 | 0.24 |
| 11.41 | 0.02 | 11.34 | 11.50 | -0.16 |

Deepseek-r1-Distill-Llama-70B is highly sensitive to response

Code Coverage

Both the multi-LLM comparison and the Llama3.3 prompt-

tween code coverage and LLM syntactic correctness (i.e.,

SCR). The results show that higher code coverage generally

improve fuzzing efficiency , highlighting the need to consider

Code Coverage

| Multiple LLM - Coverage vs. Response Duplication Rate (RDR) Plots (time=4h) | age, achieving the | best performance | in early fuzzing. While |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| STD (cov, rdr): [22.19, 14.41] | IQR (cov, rdr): [18.52, 12.84] | STD (cov, rdr): [14.78, 14.41] | diversity, it consistently generates mutated inputs in stable |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STD (cov, rdr): [22.25, 15.12] | IQR (cov, rdr): [18.95, 14.95] | STD (cov, rdr): [14.78, 15.12] | formats and performs best in long-term fuzzing exper- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 30 | 30 | iments. Gemma3-27B and QwQ-32B both perform mod- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Response Duplicate Rate (%) | 20 | Response Duplicate Rate (%) | 20 | erately in longer runs—Gemma3 offering more stability |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | 10 | and QwQ showing weaker formatting consistency—making |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | 0 | 0 | 10 | 20 | 30 | Coverage (%) | 40 | 50 | 60 | 70 | 80 | them suitable as mid-tier baselines for testing predictable |
| Deepseek-r1-Distill-Llama-70B | Llama3.3 | Deepseek-r1-Distill-Llama-70B | STD (cov, rdr): [24.71, 11.98] | results. Overall, | Llama3.3 | and | Deepseek-r1-Distill-Llama-70B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

60 QwQ-32B Gemma3-27B Deepseek-r1-Distill-Llama-70B IQR (cov, rdr): [25.33, 12.84] STD (cov, rdr): [20.55, 14.41] 60 QwQ-32B Gemma3-27B Deepseek-r1-Distill-Llama-70B IQR (cov, rdr): [30.37, 12.84] STD (cov, rdr): [24.20, 14.41] are strong candidates for further research: Llama3.3 for

| STD (cov, rdr): [20.71, 15.12] | 50 | IQR (cov, rdr): [30.43, 14.95] | STD (cov, rdr): [24.04, 15.12] | early-phase fuzzing with low error variance, and Deepseek |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30 | 30 | for long-term vulnerability explorations. |  |  |  |  |  |  |  |
| 10 | 10 | 4.4.3 | Observation 3: Impact of Syntactic Correctness on |  |  |  |  |  |  |
| Fig. 18. Multiple LLMs Coverage vs RDR for four-hour runtime | engineering | experiments | examined | the | relationship | be- |  |  |  |
| effects. This suggests that prompt complexity does not lin- | aligns with higher SCR values | , while increasing prompt shots |  |  |  |  |  |  |  |
| early correlate with fuzzing effectiveness. In cases where | stabilize SCR values and may improve coverage. This sug- |  |  |  |  |  |  |  |  |
| coverage improves, extended examples in the prompt may | gests that | better syntactic correctness enables more usable mu- |  |  |  |  |  |  |  |
| enhance syntactic correctness of LLM responses. Conversely, | tated inputs and improved path exploration | . However, this effect |  |  |  |  |  |  |  |
| coverage declines in some benchmarks may result from | follows a | threshold pattern | : Beyond a certain point, further |  |  |  |  |  |  |
| increased predictability and reduced exploratory variation | improvements in SCR do not result in additional code cov- |  |  |  |  |  |  |  |  |
| in the LLM’s outputs. These trade-offs highlight the need | erage gains, forming an ”L” shape in the SCR-coverage re- |  |  |  |  |  |  |  |  |
| for a | balance between prompt structure and model variability | , | lationship plots. These findings indicate that while syntactic |  |  |  |  |  |  |
| which is further explored in subsequent discussions. | correctness is essential, it alone is | insufficient to continuously |  |  |  |  |  |  |  |
| 4.4.2 | Observation 2: Findings Related to R3 | additional factors to enhance fuzzing performance. |  |  |  |  |  |  |  |
| outperforms the AFL++ baseline | across all benchmarks and | 4.4.4 | Observation | 4: | Impact | of | Response | Diversity | on |
| mance on specific benchmarks, there are also many cases | LLM response diversity, measured by RDR, is another key |  |  |  |  |  |  |  |  |
| where the LLMs fall short, suggesting that current state- | factor affecting fuzzing effectiveness. The RDR-coverage re- |  |  |  |  |  |  |  |  |
| of-the-art LLMs are not universally superior to traditional | lationship plots reveal an inverse relationship between RDR |  |  |  |  |  |  |  |  |
| fuzzers. Among the models, Llama3.3 shows | the strongest | and code coverage: Lower RDR generally correlates with |  |  |  |  |  |  |  |
| direct correlation | between syntactic correctness and cover- | higher coverage, indicating that | greater mutation diversity |  |  |  |  |  |  |

---

## Page 14

14

produces more effective test cases . Increasing prompt shots in • LLM Response Latency and Timeouts: Lengthy or com-

| one-hour runs tends to raise RDR values, as the LLM may | plex prompts can cause LLM response latency or time- |  |  |
| --- | --- | --- | --- |
| produce more deterministic outputs. In four-hour runs, RDR | outs, reducing effective mutations and limiting the bene- |  |  |
| varies widely across prompt shots while coverage remains | fits of LLM integration. Scalable fuzzing requires optimiz- |  |  |
| relatively stable, showing that additional in-context exam- | ing LLM responsiveness and deployment infrastructure. |  |  |
| ples can increase duplication without improving coverage. | Despite promising results, our approach has five lim- |  |  |
| These observations highlight a potential | trade-off | : Prompt | itations: (1) Mutations sometimes deviate from required |
| engineering can improve syntactic correctness but reduce | formats, (2) LLMs lack native binary support, (3) large |  |  |
| response diversity. Balancing response syntactic correctness | inputs can exceed token limits or trigger timeouts, (4) the |  |  |
| and diversity is therefore essential for optimizing LLM- | experimental scale was constrained by time and resource, |  |  |
| guided fuzzing performance. | and (5) Fuzzbench retains detailed reports for only one |  |  |

trial—limiting multi-trial analysis. Future work will ex-

| 4.4.5 | Observation 5: Additional Impacts in Fuzzing Results | plore fine-tuning LLMs—guided by automated mutation |  |
| --- | --- | --- | --- |
| Log analysis shows that approximately | 35% | of LLM queries | feedback and implemented through reinforcement learn- |
| timed out using | Ollama | , particularly with longer prompts or | ing or Direct Preference Optimization (DPO)—to improve |
| more prompt shots. This timeout behavior limits the con- | both syntactic correctness and mutation diversity, thereby |  |  |
| sistent delivery of LLM-generated mutations in real time, | generating more effective inputs for LLM-guided fuzzing. |  |  |
| reducing the number of effective mutations during fuzzing. | Other directions include optimizing the Fuzzbench pipeline |  |  |
| While our system uses AFL++’s default mutation strategies | and LLM serving infrastructure, exploring input chunking |  |  |
| to maintain operation when the LLM fails to respond, this | strategies, and extending tests to longer fuzzing durations. |  |  |
| can result in fewer novel paths and diminish the benefits of | These efforts aim to enhance the scalability, robustness, and |  |  |
| LLM guidance. These findings highlight the importance of | effectiveness of LLM-guided mutation-based fuzzing. |  |  |

LLM responsiveness and stability in our solution.

6 R ELATED W ORK

5 C ONCLUSION AND F UTURE W ORK

| We proposed a new mutation-based fuzzer that integrates | Traditional grey-box fuzzers rely on random or heuristic in- |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| off-the-shelf reasoning LLMs into AFL++ within a microser- | put mutations to discover vulnerabilities in target programs |  |  |  |  |  |  |  |  |  |  |
| vices architecture, enabling large-scale, reproducible experi- | through brute-force testing [5]. While AFL [38] and AFL++ |  |  |  |  |  |  |  |  |  |  |
| ments via Google’s Fuzzbench benchmarking platform. Our | [11] improved efficiency with feedback-driven evolution- |  |  |  |  |  |  |  |  |  |  |
| framework addresses | Challenge 1-4 | in system integration | ary algorithms, their mutation strategies are still shallow, |  |  |  |  |  |  |  |  |
| and prompt structuring ( | R1 | ), providing an | empirical study | surface-level edits that limit deeper vulnerability discovery. |  |  |  |  |  |  |  |
| for evaluating state-of-the-art open-source reasoning LLMs | LibFuzzer [39] and SelectFuzz [43] optimize instrumentation |  |  |  |  |  |  |  |  |  |  |
| in mutation-based fuzzing. Our study systematically exam- | to monitor code coverage and leverage the feedback to |  |  |  |  |  |  |  |  |  |  |
| ined effects of prompt engineering—using zero-, one-, and | guide input mutations, but they still use static, heuristic- |  |  |  |  |  |  |  |  |  |  |
| three-shot learning—along with LLM inference on mutation | based mutation strategies which struggle with inputs re- |  |  |  |  |  |  |  |  |  |  |
| quality and fuzzing efficiency. Key findings include: | quiring complex syntactic or semantic constraints and often |  |  |  |  |  |  |  |  |  |  |
| • | Prompt Shots (R2): | Increasing prompt shots | does not | lin- | generate invalid or ineffective inputs [44], [45]. These chal- |  |  |  |  |  |  |
| early improve fuzzing. Higher-shot prompts can improve | lenges hinder deeper bug discovery—especially in modern |  |  |  |  |  |  |  |  |  |  |
| syntactic correctness but may also make LLM outputs | software systems with evolving logic and formats caused by |  |  |  |  |  |  |  |  |  |  |
| overly deterministic, reducing mutation diversity. Thus, | frequent implementation changes [16]. |  |  |  |  |  |  |  |  |  |  |
| balancing prompt design with model behavior is key for | To overcome these limitations, researchers have explored |  |  |  |  |  |  |  |  |  |  |
| effective LLM-guided fuzzing. | intelligent input prioritization and mutation techniques [10], |  |  |  |  |  |  |  |  |  |  |
| • | Reasoning LLM Performance (R3): | No | single reasoning | [46], | [47], | leading | to | integrating | machine | learning | and, |
| LLMs | consistently outperform traditional fuzzers in mu- | more recently, LLMs into fuzzing workflows. ML-enhanced |  |  |  |  |  |  |  |  |  |
| tation generation without fine-tuning or additional train- | fuzzers such as V-Fuzz [47] and CTFuzz [10] use neural |  |  |  |  |  |  |  |  |  |  |
| ing. However, | Llama3.3 | and | Deepseek-r1-Distill-Llama-70B | networks | or | reinforcement | learning | to | prioritize | inputs |  |
| show strong potential to enhance mutation effectiveness. | and guide mutation strategies, improving efficiency over |  |  |  |  |  |  |  |  |  |  |
| • | Best | LLM | Selection | (R4): | Deepseek-r1-Distill-Llama-70B | random mutations. The rise of LLMs further enables se- |  |  |  |  |  |
| achieves the best balance between output diversity and | mantic understanding of input formats and mutation guid- |  |  |  |  |  |  |  |  |  |  |
| syntactic correctness, making it the top candidate for | ance, with two main approaches: (1) | Fine-tuning | [48] the |  |  |  |  |  |  |  |  |
| improving mutation quality and code coverage in long- | model, which adapts LLMs through supervised training on |  |  |  |  |  |  |  |  |  |  |
| term fuzzing within our architecture. | domain-specific input; and (2) | prompt engineering | [22], which |  |  |  |  |  |  |  |  |
| • | Syntactic Correctness vs. Response Diversity: | Effective | crafts structured prompts at inference time without retrain- |  |  |  |  |  |  |  |  |
| LLM-guided | fuzzing | requires | balancing | syntactic | cor- | ing. However, fine-tuning requires labeled data and restricts |  |  |  |  |  |
| rectness and response diversity. While stable SCR en- | mutations to existing heuristics at high computational costs. |  |  |  |  |  |  |  |  |  |  |
| sures valid mutations, higher SCR levels do not increase | For instance, LLAMAFUZZ [19] outperforms AFL++ on se- |  |  |  |  |  |  |  |  |  |  |
| coverage beyond a threshold. Improved response diver- | lect benchmarks but struggles to generalize across new pro- |  |  |  |  |  |  |  |  |  |  |
| sity enhances fuzzing efficiency, emphasizing that well- | grams, formats, or domains. Conversely, prompt engineer- |  |  |  |  |  |  |  |  |  |  |
| formatted and diverse LLM outputs are essential for | ing is lightweight and flexible, but current fuzzers—such as |  |  |  |  |  |  |  |  |  |  |
| LLM-guided fuzzing. | Fuzz4All [16], PromptFuzz [17], and CHATAFL [18]—treat |  |  |  |  |  |  |  |  |  |  |

---

## Page 15

15

LLMs as black-box, input-output generators, offering little [13] A. Touqir, F. Iradat, W. Iqbal et al. , “Systematic exploration of

insight into how mutations are derived. fuzzing in iot: Techniques, vulnerabilities, and open challenges,”

The Journal of Supercomputing , vol. 81, no. 3, p. 877, 2025, accepted:

| Reasoning-enable LLMs offer a promising new direction | 30 | April | 2025; | Published: | 23 | May | 2025. | [Online]. | Available: |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| by making the mutation process more transparent. Un- | https://doi.org/10.1007/s11227-025-07371-y |  |  |  |  |  |  |  |  |
| like prior prompt-only methods, reasoning LLMs such as | [14] A. | Helin, | “Efficient | fuzzing | payload | generation | for | mobile |  |

application security testing,” Master’s Thesis, Aalto University,

Llama3 [23], Deepseek-r1 [24], and Gemma3 [25] generate a

Espoo, Finland, May 2024, master’s Programme in Computer,

| logical progression of reasoning, or ”chain-of-thought”, that | Communication and Information Sciences, Major in Computer |
| --- | --- |
| explains how the final output is derived. This capability | Science, Mcode: SCI3042. [Online]. Available: https://aaltodoc. |
| not only supports better prompt design but also reduces | aalto.fi/items/4fede532-9b54-4902-ba08-1b1c02391945 |

[15] S. Kim, M. Liu, J. J. Rhee, Y. Jeon, Y. Kwon, and C. H. Kim,

redundant or invalid mutations and enables deeper path

“Drivefuzz: Discovering autonomous driving bugs through driv-

| exploration. Despite this potential, reasoning-driven fuzzing | ing | quality-guided | fuzzing,” | in | Proceedings | of | the | 2022 | ACM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| remains underexplored: no prior work has systematically | SIGSAC Conference on Computer and Communications Security | , 2022, |  |  |  |  |  |  |  |
| benchmarked reasoning LLMs across diverse targets or in- | pp. 1753–1767. |  |  |  |  |  |  |  |  |

[16] C. S. Xia, M. Paltenghi, J. Le Tian, M. Pradel, and L. Zhang,

vestigated how prompt-shot strategies influence mutation

“Fuzz4all: Universal fuzzing with large language models,” in Pro-

| diversity and syntactic correctness. Addressing this gap, | ceedings of the IEEE/ACM 46th International Conference on Software |  |  |
| --- | --- | --- | --- |
| our research integrates reasoning LLMs with AFL++ in | Engineering | , ser. ICSE ’24. | Association for Computing Machinery, |
| the FuzzBench framework, providing the first empirical | 2024. |  |  |

[17] Y. Lyu, Y. Xie, P. Chen, and H. Chen, “Prompt fuzzing for fuzz

analysis of prompt-shot learning, response duplication, and

driver generation,” in Proceedings of the 2024 on ACM SIGSAC

syntactic correctness in reasoning LLM-guided fuzzing. Conference on Computer and Communications Security , ser. CCS ’24.

New York, NY, USA: Association for Computing Machinery, 2024,

p. 3793–3807.

[18] R. Meng, M. Mirchev, M. B ¨ ohme, and A. Roychoudhury, “Large

language model guided protocol fuzzing,” in Proceedings of the 31st

R EFERENCES Network and Distributed System Security Symposium (NDSS) . The

Internet Society, 2024.

| [1] | P. Mell and T. Grance, “Use of the common vulnerabilities and ex- | [19] H. Zhang, Y. Rong, Y. He, and H. Chen, “Llamafuzz: Large |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| posures (cve) vulnerability naming scheme,” National Institute of | language | model | enhanced | greybox | fuzzing,” | arXiv | preprint |
| Standards and Technology, Gaithersburg, MD, Special Publication | arXiv:2406.07714 | , 2024. |  |  |  |  |  |
| NIST SP 800-51, 2002, accessed: 2025-06-02. | [20] J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. H. |  |  |  |  |  |  |
| [2] | NIST, “National vulnerability database (nvd),” https://nvd.nist. | Chi, Q. V. Le, and D. Zhou, “Chain-of-thought prompting elicits |  |  |  |  |  |
| gov, 2025, accessed: 2025-06-02. | reasoning in large language models,” in | Proceedings of the 36th |  |  |  |  |  |
| [3] | T. Sasi, A. H. Lashkari, R. Lu, P. Xiong, and S. Iqbal, “A compre- | International Conference on Neural Information Processing Systems | , |  |  |  |  |
| hensive survey on iot attacks: Taxonomy, detection mechanisms | ser. NIPS ’22. | Red Hook, NY, USA: Curran Associates Inc., 2022. |  |  |  |  |  |
| and challenges,” | Journal of Information and Intelligence | , vol. 2, no. 6, | [21] J. Metzman, L. Szekeres, L. Simon, R. Sprabery, and A. Arya, |  |  |  |  |
| pp. 455–513, 2024. | “Fuzzbench: an open fuzzer benchmarking platform and service,” |  |  |  |  |  |  |
| [4] | L. D. Xu, W. He, and S. Li, “Internet of things in industries: A | in | Proceedings of the 29th ACM Joint Meeting on European Software |  |  |  |  |
| survey,” | IEEE Transactions on Industrial Informatics | , vol. 10, no. 4, | Engineering Conference and Symposium on the Foundations of Software |  |  |  |  |
| pp. 2233–2243, November 2014. | Engineering | , ser. ESEC/FSE 2021. | New York, NY, USA: Associa- |  |  |  |  |
| [5] | M. Sutton, A. Greene, and P. Amini, “What is fuzzing?” in | Fuzzing: | tion for Computing Machinery, 2021, p. 1393–1403. |  |  |  |  |
| Brute Force Vulnerability Discovery | . | Addison-Wesley Professional, | [22] N. Knoth, A. Tolzin, A. Janson, and J. M. Leimeister, “Ai literacy |  |  |  |  |
| 2007, pp. 26–52. | and its implications for prompt engineering strategies,” | Computers |  |  |  |  |  |
| [6] | S. Bekrar, C. Bekrar, R. Groz, and L. Mounier, “Finding software | and Education: Artificial Intelligence | , vol. 6, p. 100225, 2024. |  |  |  |  |
| vulnerabilities by smart fuzzing,” in | 2011 Fourth IEEE International | [23] A. Grattafiori, A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al- |  |  |  |  |  |
| Conference on Software Testing, Verification and Validation | , 2011, pp. | Dahle, A. Letman, A. Mathur, and J. J. et al., “The llama 3 herd of |  |  |  |  |  |
| 427–430. | models,” 2024. |  |  |  |  |  |  |

[7] M. Eceiza, J. L. Flores, and M. Iturbe, “Fuzzing the internet of [24] DeepSeek-AI, G. Daya, Y. Dejian, and Z. e. a. Haowei, “Deepseek-

| things: A review on the techniques and challenges for efficient | r1: Incentivizing reasoning capability in llms via reinforcement |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vulnerability discovery in embedded systems,” | IEEE Internet of | learning,” 2025. |  |  |  |  |  |  |  |  |  |  |  |  |
| Things Journal | , vol. 8, no. 13, pp. 10 390–10 411, 2021. | [25] T. Gemma, K. Aishwarya, F. Johan, P. Shreya, V. Nino, and M. e. a. |  |  |  |  |  |  |  |  |  |  |  |  |
| [8] | C. | Beaman, | M. | Redbourne, | J. | D. | Mummery, | and | S. | Hakak, | Ramona, “Gemma 3 technical report,” 2025. |  |  |  |
| “Fuzzing vulnerability discovery techniques: Survey, challenges | [26] Qwen Team, “Qwq-32b: Embracing the power of reinforcement |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and future directions,” | Computers & Security | , vol. 120, p. 102813, | learning,” https://qwenlm.github.io/blog/qwq-32b/, 2025, blog |  |  |  |  |  |  |  |  |  |  |  |
| 2022. | post. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [9] | K. | Alshmrany, | M. | Aldughaim, | A. | Bhayat, | and | L. | Cordeiro, | [27] K. T. Chitty-Venkata, S. Raskar, B. Kale, F. Ferdaus, A. Tanikanti, |  |  |  |  |
| “Fusebmc v4: Improving code coverage with smart seeds via bmc, | K. Raffenetti, V. Taylor, M. Emani, and V. Vishwanath, “Llm- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| fuzzing and static analysis,” | Form. Asp. Comput. | , vol. 36, no. 2, Jun. | inference-bench: Inference benchmarking of large language mod- |  |  |  |  |  |  |  |  |  |  |  |
| 2024. | els on ai accelerators,” in | SC24-W: Workshops of the International |  |  |  |  |  |  |  |  |  |  |  |  |
| [10] V.-H. Pham, D. Thi Thu Hien, N. Phuc Chuong, P. Thanh Thai, and | Conference for High Performance Computing, Networking, Storage and |  |  |  |  |  |  |  |  |  |  |  |  |  |
| P. The Duy, “A coverage-guided fuzzing method for automatic | Analysis | , 2024, pp. 1362–1379. |  |  |  |  |  |  |  |  |  |  |  |  |
| software vulnerability detection using reinforcement learning- | [28] S. Meier, “Bringing fuzzing capabilities to the genode framework,” |  |  |  |  |  |  |  |  |  |  |  |  |  |
| enabled multi-level input mutation,” | IEEE Access | , vol. 12, pp. | Master’s Thesis, University of Applied Sciences Rapperswil, 2021, |  |  |  |  |  |  |  |  |  |  |  |
| 129 064–129 080, 2024. | accessed: 2025-06-03. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [11] A. Fioraldi, D. Maier, H. Eißfeldt, and M. Heuse, “Afl++: com- | [29] J. Metzman, L. Szekeres, L. Simon, R. Sprabery, and A. Arya, |  |  |  |  |  |  |  |  |  |  |  |  |  |
| bining incremental steps of fuzzing research,” in | Proceedings of the | “Fuzzbench: an open fuzzer benchmarking platform and service,” |  |  |  |  |  |  |  |  |  |  |  |  |
| 14th USENIX Conference on Offensive Technologies | , ser. WOOT’20. | in | Proceedings of the 29th ACM joint meeting on European software |  |  |  |  |  |  |  |  |  |  |  |
| USA: USENIX Association, 2020. | engineering conference and symposium on the foundations of software |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [12] X. | Du, | A. | Chen, | B. | He, | H. | Chen, | F. | Zhang, | and | Y. | Chen, | engineering | , 2021, pp. 1393–1403. |
| “Afliot: | Fuzzing | on | linux-based | iot | device | with | binary- | [30] D. Eddelbuettel, “A Brief Introduction to Redis,” | arXiv e-prints | , p. |  |  |  |  |
| level | instrumentation,” | Computers | & | Security | , | vol. | 122, | p. | arXiv:2203.06559, Mar. 2022. |  |  |  |  |  |
| 102889, | 2022. | [Online]. | Available: | https://www.sciencedirect. | [31] A. Gupta, S. Tyagi, N. Panwar, S. Sachdeva, and U. Saxena, “Nosql |  |  |  |  |  |  |  |  |  |
| com/science/article/pii/S0167404822002838 | databases: Critical analysis and comparison,” in | 2017 International |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 16

16

Conference on Computing and Communication Technologies for Smart

Nation (IC3TSN) , 2017, pp. 293–299.

[32] F. S. Marcondes, A. Gala, R. Magalh˜ aes, F. Perez de Britto,

D. Dur˜ aes, and P. Novais, “Using ollama,” in Natural Language An-

alytics with Generative Large-Language Models: A Practical Approach

with Ollama and Open-Source LLMs . Springer, 2025, pp. 23–35.

[33] Z. Guo, M. Schlichtkrull, and A. Vlachos, “A survey on automated

fact-checking,” Transactions of the Association for Computational

Linguistics , vol. 10, pp. 178–206, 2022. [Online]. Available:

https://doi.org/10.1162/tacl a 00460

[34] M. Shanahan, K. McDonell, and L. Reynolds, “Role play with large

language models,” Nature , vol. 623, no. 7987, pp. 493–498, 2023.

[35] DAIR.AI, “Prompt engineering guide,” https://www.

promptingguide.ai, 2023, accessed: 2025-05-30.

[36] H. Dang, K. Benharrak, F. Lehmann, and D. Buschek, “Beyond text

generation: Supporting writers with continuous automatic text

summaries,” in Proceedings of the ACM Symposium on User Interface

Software and Technology (UIST) , M. Agrawala, J. O. Wobbrock,

E. Adar, and V. Setlur, Eds. ACM, 2022.

[37] K. Serebryany, “OSS-Fuzz - google’s continuous fuzzing service

for open source software.” Vancouver, BC: USENIX Association,

Aug. 2017.

[38] M. Zalewski, “American fuzzy lop,” https://lcamtuf.coredump.

cx/afl/, 2013, accessed: 2025-06-03.

[39] Google, “Libfuzzer – a library for coverage-guided fuzz testing,”

https://llvm.org/docs/LibFuzzer.html, 2018, accessed: 2025-05-

30.

[40] W.-C. Chao, S.-C. Lin, Y.-H. Chen, C.-W. Tien, and C.-Y. Huang,

“Design and implement binary fuzzing based on libfuzzer,” in

2018 IEEE Conference on Dependable and Secure Computing (DSC) .

IEEE, 2018, pp. 1–2.

[41] A. Fioraldi, D. C. Maier, D. Zhang, and D. Balzarotti, “Libafl: A

framework to build modular and reusable fuzzers,” in Proceedings

of the 2022 ACM SIGSAC Conference on Computer and Communica-

tions Security , 2022, pp. 1051–1065.

[42] C. Lyu, M. Zhang, and Y. Zhang, “Automatic generation of

syntax-guided test programs,” in 28th USENIX Security Symposium

(USENIX Security 19) . USENIX Association, 2019.

[43] C. Luo, W. Meng, and P. Li, “Selectfuzz: Efficient directed fuzzing

with selective path exploration,” in 2023 IEEE Symposium on

Security and Privacy (SP) , 2023, pp. 2693–2707.

[44] T. Ji, Z. Wang, Z. Tian, B. Fang, Q. Ruan, H. Wang, and

W. Shi, “Aflpro: Direction sensitive fuzzing,” Journal of Information

Security and Applications , vol. 54, p. 102497, 2020. [Online].

Available: https://www.sciencedirect.com/science/article/pii/

S2214212619305733

[45] V.-H. Pham, D. Thi Thu Hien, N. Phuc Chuong, P. Thanh Thai, and

P. The Duy, “A coverage-guided fuzzing method for automatic

software vulnerability detection using reinforcement learning-

enabled multi-level input mutation,” IEEE Access , vol. 12, pp.

129 064–129 080, 2024.

[46] D. She, K. Pei, D. Epstein, J. Yang, B. Ray, and S. Jana, “Neuzz:

Efficient fuzzing with neural program smoothing,” in 2019 IEEE

Symposium on Security and Privacy (SP) . IEEE, 2019, pp. 803–817.

[47] Y. Li, S. Ji, C. Lyu, Y. Chen, J. Chen, Q. Gu, C. Wu, and R. Beyah,

“V-fuzz: Vulnerability prediction-assisted evolutionary fuzzing for

binary programs,” IEEE Transactions on Cybernetics , vol. 52, no. 5,

pp. 3745–3756, 2022.

[48] N. Ding, Y. Qin, G. Ke, W. Wang, Y. Shen, W. Chen, Z. Gan,

X. Liu, J. Gao, and Y. Yang, “Parameter-efficient fine-tuning

of large-scale pre-trained language models,” Nature Machine

Intelligence , vol. 5, pp. 220–235, March 2023. [Online]. Available:

https://doi.org/10.1038/s42256-023-00626-4

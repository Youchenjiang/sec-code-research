---
title: "AndroByte: LLM-Driven Privacy Analysis through Bytecode Summarization and Dynamic Dataflow Call Graph Generation"
author: "Mst Eshita Khatun; Lamine Noureddine; Zhiyong Sui; Aisha Ali-Gombe"
creator: "arXiv GenPDF (tex2pdf:4177c2c)"
pages: 17
---

# AndroByte: LLM-Driven Privacy Analysis through Bytecode Summarization and Dynamic Dataflow Call Graph Generation

> **作者**：Mst Eshita Khatun; Lamine Noureddine; Zhiyong Sui; Aisha Ali-Gombe
> **總頁數**：17 頁

---

## Page 1

AndroByte: LLM-Driven Privacy Analysis through Bytecode Summarization and

Dynamic Dataflow Call Graph Generation

Mst Eshita Khatun*, Lamine Noureddine, Zhiyong Sui, and Aisha Ali-Gombe

Department of Computer Science and Engineering

Louisiana State University, Baton Rouge, LA, USA

mkhatu3@lsu.edu, lnoureddine@lsu.edu, zsui1@lsu.edu, aaligombe@lsu.edu

| Abstract | —With the exponential growth in mobile applications, | personalized user experiences, and enhanced functionality. |
| --- | --- | --- |
| protecting user privacy has become even more crucial. An- | For instance, apps such as navigation tools require location |  |
| droid applications are often known for collecting, storing, and | data to provide accurate directions, while streaming plat- |  |
| sharing sensitive user information such as contacts, location, | forms analyze user preferences to suggest tailored content. |  |
| camera, and microphone data—often without the user’s clear | Additionally, data collection supports app developers in |  |
| consent or awareness—raising significant privacy risks and ex- | optimizing performance through analytics, identifying bugs, |  |
| posure. In the context of privacy assessment, dataflow analysis | and implementing user-driven updates. However, while these |  |
| is particularly valuable for identifying data usage and potential | practices are essential for functionality and monetization, |  |
| leaks. Traditionally, this type of analysis has relied on formal | they highlight the need for transparency and robust privacy |  |
| methods, heuristics, and rule-based matching. However, these | safeguards to protect users’ sensitive information from mis- |  |
| techniques are often complex to implement and prone to errors, | use or unauthorized access. |  |
| such as taint explosion for large programs. Moreover, most | Regulations like the California Consumer Privacy Act |  |
| existing Android dataflow analysis methods depend heavily on | (CCPA) as well as the General Data Protection Regulation |  |
| predefined list of sinks, limiting their flexibility and scalability. | (GDPR) in the European Union aim to safeguard user data. |  |

To address the limitations of these existing techniques, we

propose AndroByte, an AI-driven privacy analysis tool that

leverages the reasoning of a large language model (LLM)

on bytecode summarization to dynamically generate accurate

and explainable dataflow call graphs from static code anal-

ysis. AndroByte achieves a significant F β -Score of 89% in

generating dynamic dataflow call graphs on the fly, outper-

forming the effectiveness of traditional tools like FlowDroid

and Amandroid in leak detection without relying on prede-

fined propagation rules or sink lists. Moreover, AndroByte’s

iterative bytecode summarization provides comprehensive and

arXiv:2510.15112v2 [cs.CR] 4 Nov 2025 Index Terms —Privacy, Android, LLM, Dataflow, Call Graph,

Bytecode Summarization

Furthermore, most mobile operating platforms adopt user

permissions to limit the use of sensitive personal informa-

tion [2]. Despite these multi-faced measures, a significant

number of mobile applications, particularly Android appli-

cations, tend to be overprivileged, requesting more data than

necessary [3]–[8]. In particular, several studies have shown

that Android applications often engage in data collection

practices that can lead to privacy leaks at the code-level

behavior that are not disclosed by app developers [9]–

[17]. Therefore, it is essential to develop more robust code

analysis tools capable of uncovering privacy risks that go

beyond surface-level transparency measures.

analysis techniques for dataflow analysis focusing on data

leak detection. Taint analysis is a special type of dataflow

analysis that follows the propagation of the target date from

source to sink. Most dataflow analyses on Android are

heuristics, or strict rule-based approach [18]–[20]. However,

practices, such as new APIs or SDK versioning, while rule-

| explainable insights into dataflow and leak detection, achieving | To mitigate these code privacy-related issues, researchers |
| --- | --- |
| high, quantifiable scores based on the G-Eval metric. | in this domain have proposed numerous static and dynamic |
| 1. Introduction | built on taint propagation leveraging either formal methods, |
| In this digital age, mobile applications play a pivotal | with these traditional approaches, overly conservative taint |
| role, serving as indispensable tools that streamline our daily | propagation rules may mark many safe data flows as tainted, |
| activities. According to Ericsson’s November 2022 Mobility | leading to high false positives and/or taint exposition, while |
| Report, [1], there are more than 6.26 billion smartphone | strict predefined rules or heuristics may overlook certain |
| subscriptions worldwide, underscoring the central role that | data flows, resulting in missed detection. Additionally, for- |
| mobile technology plays in everyday life. Mobile applica- | mal method-based approaches are difficult to implement |
| tions often need access to user data for seamless operation, | correctly, maintain, and adapt to evolving programming |
| *Corresponding author: Mst Eshita Khatun | based systems require significant manual effort to define and |

---

## Page 2

| update rules for new libraries, APIs, or frameworks. | • | To support reproducibility and future benchmark- |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Thus, in this research, we proposed a novel technique | ing, we released AndroByte’s source code, complete |  |  |  |  |  |  |
| called | AndroByte | that | addresses | the | critical | challenge | dataflow call graph traces, summarization outputs, |
| of dataflow analysis on Android. AndroByte’s methodol- | and all supplementary materials [21]. |  |  |  |  |  |  |

ogy leverages LLM’s reasoning capability for method and

dataflow analysis to identify privacy leaks in Android appli-

cations. At its core, AndroByte features a method analysis

component based on bytecode summarization, which utilizes

an integrated LLM to analyze the application’s Smali code.

This bytecode is parsed and summarized to generate natural

language descriptions of the method behavior, focusing on

the dataflow of the target data source and caller-callee

relationships within the context of the given data source.

rules or lists of sensitive data sinks, AndroByte dynamically

its robustness, portability, and adaptability across different

contributions:

Paper outline. The rest of the paper is outlined as follows:

Section 2 provides the background & related work on pri-

vacy analysis with a specific emphasis on dataflow analysis;

Section 3 offers a detailed description of AndroByte design;

Sections 4, 5, and 6 present the specific of AndroByte

implementation, testing and evaluation, and discussion of

the results and Section 7 concludes the paper.

Traditionally, static dataflow analysis methodologies

| Unlike traditional static analysis tools that rely on predefined | 2. Background & Related Work |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| identifies sinks through AI reasoning, enabling more adap- | From an analysis perspective, the most reliable way |  |  |  |  |  |  |
| tive and robust analysis. To determine the propagation path, | to validate privacy exposure is through code-level privacy |  |  |  |  |  |  |
| AndroByte leverages its dynamic dataflow-aware call graph | analysis, which examines data access, propagation, and po- |  |  |  |  |  |  |
| generation module, which constructs dataflow call graphs | tential leaks. While this analysis can be computationally |  |  |  |  |  |  |
| by recursively exploring the next method list based on the | expensive at runtime, it is more manageable when conducted |  |  |  |  |  |  |
| caller-callee relationship starting from the target data’s API | statically. This process, commonly referred to as dataflow |  |  |  |  |  |  |
| callsite. After the analysis, AndroByte provides a compre- | analysis, is more feasible in a static context. For instance, |  |  |  |  |  |  |
| hensive summary of dataflows, the sensitive data propaga- | in Figure 1, the bytecode instructions show that the method |  |  |  |  |  |  |
| tion path, and the specifics of privacy leaks. The combi- | calls | two | sensitive | APIs, | get latitude() | and | get |
| nation of LLM-driven reasoning, iterative graph generation, | longitude() | on a | android/location/Location |  |  |  |  |
| and method-level bytecode analysis allows AndroByte to | object. These calls retrieve the device’s current latitude |  |  |  |  |  |  |
| address the limitations of traditional methods, offering a | and longitude, which are considered user sensitive data. |  |  |  |  |  |  |
| novel, automated, effective, and adaptive Android privacy | The values are then appended to a comma-separated string |  |  |  |  |  |  |
| analysis technique. Our evaluation of AndroByte in 300 real- | (e.g., ’latitude, longitude’) and stored in the register | v0 | . |  |  |  |  |
| world apps shows that our approach can generate accurate | Next, | v0 | is converted into a UTF-8 byte array of the |  |  |  |  |
| dataflow call graphs with 89% F | β | -Score accuracy and pro- | location coordinates. Finally, the method uses call | v1 | is a |  |  |
| vide comprehensive summaries that show propagation path, | GoogleApiClient, | v2 | is the string ”/navigation/start” | v3 | is |  |  |
| description, and sink information. Additional evaluation on | connected wearable devices, | v0 | is the byte array containing |  |  |  |  |
| DroidBench and UBCBench apps shows that AndroByte | location (latitude, longitude) to send this byte array outside |  |  |  |  |  |  |
| can automatically detect sinks without a predefined list | of the app, specifically to a connected wearable device. In |  |  |  |  |  |  |
| data leak detection accuracy of F-Score 83%. Addition- | dataflow analysis, this call constitutes a sink because it is |  |  |  |  |  |  |
| ally, the result of testing AndroByte on LLMs indicates | the point where the sensitive location data is sent outside |  |  |  |  |  |  |
| that the proposed approach is model-agnostic, highlighting | the app’s immediate boundary. |  |  |  |  |  |  |
| LLMs. In summary, the research makes the following key | 2.1. Traditional Taint Analysis |  |  |  |  |  |  |
| • | Dynamic Dataflow-aware Call Graph Generation: | leverage taint propagation to track the flow of sensitive data |  |  |  |  |  |
| AndroByte introduces an effective and automated | (referred to as ”tainted data”) through a program. These |  |  |  |  |  |  |
| mechanism for dynamically generating dataflow call | methods identify whether such data reaches ”sinks” where it |  |  |  |  |  |  |
| graphs directly from bytecode summarization, lever- | may cause security or privacy issues, using formal methods, |  |  |  |  |  |  |
| aging AI reasoning to trace dataflows and caller- | heuristics, and well-defined rules [18]–[20], [22]–[32]. This |  |  |  |  |  |  |
| callee relationships iteratively. | process is particularly complex when applied to bytecode |  |  |  |  |  |  |
| • | Robust | and Adaptable | Data | Leak Detection: | By | or assembly instructions. One of the most influential and |  |
| eliminating the dependency on predefined rules and | widely used static taint analysis systems for Android, based |  |  |  |  |  |  |
| sink lists, AndroByte enables robust detection of | on this traditional approach, is FlowDroid [18]. It requires |  |  |  |  |  |  |
| data leaks through method analysis and dynamic | predefined data sources and sinks, performs flow-insensitive |  |  |  |  |  |  |
| graph generation, making it more adaptable than | points-to analysis, and incorporates context-, flow-, field- |  |  |  |  |  |  |
| traditional approaches. | , and object-sensitive analysis for taint propagation. Tools |  |  |  |  |  |  |
| • | Comprehensive | Bytecode | Summarization: | like EPICC [23], IccTA [19], and Amandroid [20] have |  |  |  |
| AndroByte | provides | detailed | natural | language | extended FlowDroid’s capabilities to support Android Intent |  |  |
| summaries for each method, highlighting sensitive | objects. While many studies have demonstrated FlowDroid’s |  |  |  |  |  |  |
| data propagation paths and potential sinks. | precision and effectiveness in analyzing complex dataflows, |  |  |  |  |  |  |

---

## Page 3

Figure 1: Motivation Example

| its methodology heavily depends on rigid heuristics and | RF with taint analysis to identify location privacy leakage. |
| --- | --- |
| precisely defined sinks for taint propagation. In contrast, we | Feichtner et al. [43] utilized CNNs and word embeddings to |
| propose a novel architecture, AndroByte, which leverages | assess alignment between app descriptions and permissions, |
| AI-based program context reasoning for dataflow analysis. | and Rahman et al. [44] leveraged FastText and BERT to |
| Our approach identifies propagation paths between sources | identify permission-related content in policies. Similarly, |
| and sinks without relying on the complexities of traditional | Ma et al. [45] developed SideNet, a deep-learning frame- |
| static techniques. Instead, it builds on bytecode summariza- | work detecting sensitive app activities through Encoder and |
| tion and dynamic dataflow call graph generation using LLM | ResNet-based models. Liu et al. [46] introduced NLEU, en- |
| capabilities. | hancing taint analysis with NLP-derived semantic insights, |

semantic insights to effectively summarize Java bytecode.

Cobra [37] applies bytecode summarization for enhanced

vulnerability detection in smart contracts, while StoneDetec-

tor [38] detects code clones by examining bytecode patterns.

Fevid et al. [39] introduced a Random Forest approach

analyzing opcode sequences to detect ransomware threats

at the assembly level. LTAChecker [40] similarly employed

opcode sequences for Android application behavior analy-

sis. The key distinction between these related works and

our proposed AndroByte focuses on privacy analysis and

D2CFG generation using AI-driven reasoning. To the best

of our knowledge, our work is the first to propose leveraging

LLM reasoning capability for method and dataflow analysis.

and Fu et al. [47] employed a Decision Tree combined

as legitimate or illegitimate. Further, Morales et al. [16]

applications. .

3. Design

This section presents the design of AndroByte — a code-

level privacy behavior analyzer for Android applications as

illustrated in Figure 2. AndroByte has three main compo-

nents: 1) Method Analysis; 2) Prompt Engineering; and 3)

Dynamic Dataflow Call Graph Generation (D2CFG).

3.1. Method Analysis

The method analysis leverages bytecode summarization

level behavior for a target application. Bytecode summa-

| 2.2. Bytecode summarization | with a bag-of-words model to classify network transmissions |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| The | advancements | in | language | models | have | signifi- | used LLMs and semantic similarity to detect inconsistencies |
| cantly enhanced automatic code summarization techniques | between privacy policies and actual code practices, whereas |  |  |  |  |  |  |
| to generate natural language descriptions that succinctly | Privacify [48] applied LLM-based summarization for pri- |  |  |  |  |  |  |
| explain the code’s purpose and functionality [33]. Xiang | vacy policy comprehension, and PrivacyAsst [49] applied |  |  |  |  |  |  |
| et al. [34] developed SmartBT, a summarization tool for | LLM-driven encryption and attribute shuffling to secure |  |  |  |  |  |  |
| Ethereum bytecode utilizing control flow graphs (CFGs) and | sensitive user data. In contrast, our approach leverages LLM |  |  |  |  |  |  |
| information retrieval techniques. Similarly, BCGen [35] and | reasoning to perform method-level bytecode and dataflow |  |  |  |  |  |  |
| further studies by Huang et al. [36] leveraged CFGs with | analysis specifically aimed at detecting data leaks in Android |  |  |  |  |  |  |
| 2.3. Privacy Analysis Using AI | using LLMs to understand, analyze, and explain method- |  |  |  |  |  |  |
| Recent studies have shown that integrating a machine | rization was chosen over source code summarization pri- |  |  |  |  |  |  |
| learning-based | approach | with | traditional | static | analysis | marily due to its platform-independent representation that |  |
| methods can provide effective approaches to privacy anal- | reflects the executable logic of an Android application. |  |  |  |  |  |  |
| ysis. For instance, Jain et al. [41] employed RNN models | This makes bytecode closer to the final executable form, |  |  |  |  |  |  |
| on Abstract Syntax Tree (AST) paths to detect privacy be- | providing a more reliable basis for understanding the app’s |  |  |  |  |  |  |
| haviors in Android code, while SAMLDroid [42] integrated | runtime behavior. While obfuscation is common among |  |  |  |  |  |  |

*[Image: Page 3 Image]*

---

## Page 4

Figure 2: AndroByte’s Workflow

| Android developers to obscure the original source code, | 1) | A natural language summary of the method in the |  |  |  |
| --- | --- | --- | --- | --- | --- |
| often affecting its readability and making decompilation | context of | S | s | . |  |
| less reliable, decompilation into bytecode largely retains | 2) | The list of all methods called ( | nextMethods | ) |  |
| the instructional structure of a program, thereby preserving | that have a caller-callee relationships with | m | i | in |  |
| key program context and dependency. Compared to source | the context of | S | s | data flow. |  |
| code decompilation, bytecode is more likely to maintain | 3) | Identified sensitive data sinks in the context of | S | s | . |

the actual instructions, method context, and dependencies

needed for accurate analysis. Thus, in this component, we

focus on bytecode summarization to analyze target functions

in the context of sensitive data. The algorithm traverses the

Let M represent a set of methods extracted from a decom-

M = { m 1 , m 2 , m 3 , . . . , m n }

where m i is the bytecode representation of the i -th method

s , and thus m i is defined

m i = { S s , I, C, D }

- S s : The target data source.

- I : Bytecode instructions.

- C : Contextual information (e.g., class name, method sig-

- D : Dependency information (e.g., invoked methods or

APIs).

The objective function of this method analysis component is

to generate a structured and human-readable representation

To achieve this objective, we describe the transformation

process from m i to S ( m i ) as a composition of three sub-

components:

– Automatically generates natural language

( N L ) summary using pre-trained model:

L ( P

resents them as nextMethods ,

– Analyzes the flow of sensitive data within m i

from a target source ( S s ) to sinks ( S k ):

– Finally, the aggregation module combines

all outputs into a structured representation

S ( m i ) :

| bytecode for a function to find the relationships between | • | Bytecode parsing module: Extracts the components |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| target data and other variables and trace the dataflow through | of | m | i | from a decompiled app: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the function’s caller-callee relationship. | P | ( | m | i | ) | → { | S | s | , I, C, D | } |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| piled Android application: | • | LLM summarization module: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| that calls a target data source API | S | prompt | ) | → | S | NL | ( | m | i | ) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| as: | – | Identifies all methods called by | m | i | and rep- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| where: | C | ( | m | i | ) | → | nextMethods | = | { | n | 1 | , n | 2 | , . . . , n | j | } |  |  |  |  |  |  |  |  |  |  |  |  |  |
| nature, modifiers). | D | ( | m | i | ) | → { | S | s | , S | k | } |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| S | ( | m | i | ) | for each method | m | i | , which includes: | S | ( | m | i | ) = | { | S | NL | ( | m | i | → | S | s | , | ) | , | nextMethods | , S | k | } |

---

## Page 5

3.2. Prompt Engineering - N : Nodes represent methods m i

The prompt engineering component is critical to ensur-

niques like scoping and few-shot prompting to optimize

generate accurate, relevant, and efficient output.

tailoring the prompt to include only the most relevant in-

components that are selectively prioritized to guide the LLM

generic definition of bytecode instructions I , the sink S k , the

C , and D . Thus, our Scoping function ( S ), as shown below,

P ( m i ) to construct a targeted scope for the prompt:

S ( P ( m i )) → { S s , S k , I , C , D }

where S ′

s , S ′ ′

k , I ′ , C , and D ′ represent scoped subsets of S s ,

k , I , C , and D , respectively.

LLM with a small set of examples within the prompt. These

examples demonstrate the expected input-output relation-

ship, improving the model’s contextual understanding. The

examples are curated to reflect scenarios like identifying

method signatures and parameters. Our Few-Shot prompt

outcomes for summarization, next methods, and data flow

′ ′ ′

F ( { I , C , D } ) → E

where E is the set of examples embedded in the prompt.

Hence, our prompt for the method analysis ( P ) combines

the scoped data and examples into a coherent, structured

P ( S , F ) → P prompt

3.3. Dynamic Dataflow-aware Call Graph Genera-

tion - D2CFG

This component builds a graph representation of the

ships. This process leverages the results of method analysis

- E : Edges represent caller-callee relationships between

methods

identified as S ′

s ’s callsite. Let’s denote this root method m 0 .

following steps are taken:

1. Initialize an empty directed graph and add the starting

empty:

• Dequeue a method by removing the first method m

from Q .

• Summarize m

prompting modules to retrieve:

L ( P prompt ) → S NL ( m i → S s ) , nextMethods , S k

• Add nextMethods to Graph:

graph:

N ← N ∪ { n j }

∗ Add an edge from m i to n j :

– Add n j to Q for further exploration.

• If a viable sink S k is identified for the target data,

then record the sink in the graph and, optionally,

terminate further exploration of this path.

data.

potential sinks.

| ing the effectiveness of the bytecode summarization pro- | The graph captures the flow of sensitive data and identifies |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cess in identifying data flow and determining the list of | potential sinks for | a given target data source | . Thus, the |  |  |  |  |  |  |  |  |  |
| nextMethods | . This component leverages structured tech- | initial input to the graph is the root method, which is |  |  |  |  |  |  |  |  |  |  |
| the prompts provided to the LLM, enhancing its ability to | To generate the D2CFG with | m | 0 | as the root node, the |  |  |  |  |  |  |  |  |
| 3.2.1. Scoping. | This prompt engineering technique involves | method | m | 0 | as the root node: |  |  |  |  |  |  |  |
| formation in a target method’s bytecode instructions. The | G | = ( | N, E | ) | , | N | = | ∅ | , | E | = | ∅ |
| toward specific tasks are the target data origin ( | S | s | , the | N | ← { | m | 0 | } |  |  |  |  |
| context of data flow propagation, storage and dependency | 2. Create a queue | Q | and add | m | 0 | to it: |  |  |  |  |  |  |
| extracts and prioritizes the most relevant information from | Q | ← { | m | 0 | } |  |  |  |  |  |  |  |
| ′ | ′ | ′ | ′ | ′ | 3. Recursive Exploration: While the queue | Q | is not |  |  |  |  |  |
| S | i |  |  |  |  |  |  |  |  |  |  |  |
| 3.2.2. Few-Shot Prompting. | This technique provides the | i | using | the | method | analysis | and |  |  |  |  |  |
| construction ( | F | ) adds examples demonstrating the desired | – | For each | n | j | ∈ | nextMethods | : |  |  |  |
| analysis: | ∗ | Add | n | j | to | N | if it is not already in the |  |  |  |  |  |
| prompt: | E | ← | E | ∪ { | ( | m | i | , n | j | ) | } |  |
| methods for the target Android application, where nodes | 4. This process ends when | Q | is empty, indicating no more |  |  |  |  |  |  |  |  |  |
| represent methods and edges represent caller-callee relation- | methods to explore or when a sink is found for the target |  |  |  |  |  |  |  |  |  |  |  |
| and prompts engineering to recursively explore methods, | Thus, with the method analysis extracting, summarizing, |  |  |  |  |  |  |  |  |  |  |  |
| adding nodes and edges to the graph until a termination | and identifying key relationships within individual methods, |  |  |  |  |  |  |  |  |  |  |  |
| condition is met - no new methods are found, or a viable sink | prompt engineering optimizes the method analysis’s inter- |  |  |  |  |  |  |  |  |  |  |  |
| is identified. The significance of this novel D2CFG is that it | actions with the LLM, ensuring precise and context-aware |  |  |  |  |  |  |  |  |  |  |  |
| dynamically traces data sources and identifies sinks through | summarization. Finally, the dynamic data flow graph gen- |  |  |  |  |  |  |  |  |  |  |  |
| the graph without the complexity of taint propagation rules. | eration constructs a recursive and iterative representation of |  |  |  |  |  |  |  |  |  |  |  |
| The objective function of the D2CFG is to construct a | the program’s behavior, connecting methods through caller- |  |  |  |  |  |  |  |  |  |  |  |
| directed graph | G | where: | callee relationships and tracing sensitive data flow to identify |  |  |  |  |  |  |  |  |  |

---

## Page 6

| TABLE 1: Examples of Android APIs Accessing Personal | Context;)V | and | placed | the | method | as | root | node | in | a |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Data | empty graph. Following the method analysis for the root |  |  |  |  |  |  |  |  |  |
| API Name | Data Type | node, | AndroByte | found | three | nextMethods | within | the |  |  |
| android/location/Location;getLatitude() | Location | dataflow | context | of | the | location | data, | which | are | then |
| android/location/Location;getLongitude() | Location | added | as | nodes | to | the | D2CFG | with | edges | connecting |
| android/telephony/TelephonyManager;getLine1Num | Phone Number | these methods to the root node. Traversing these methods |  |  |  |  |  |  |  |  |
| ber() | using the queue-based approach shows that two of the |  |  |  |  |  |  |  |  |  |
| android/accounts/AccountManager;getAccounts() | Email Address | three nodes did not propagate the location data further, but |  |  |  |  |  |  |  |  |
| android/telephony/TelephonyManager;getDeviceId() | Device Identifier | the | Lcom/mintegral/msdk/system/a;− | > | reportUser:(Lcom |  |  |  |  |  |
| android/telephony/TelephonyManager;getSimSerial | SIM Serial | /mintegral/msdk/MIntegralUser;)V | function | passes | the |  |  |  |  |  |

Number()

| android/net/wifi/WifiInfo;getMacAddress() | MAC Address |
| --- | --- |
| android/net/wifi/WifiInfo;getSSID() | SSID |
| android/net/wifi/WifiInfo;getBSSID() | BSSID |

android/location/LocationManager;getLastKnownLo Location

cation()

android/telephony/SmsMessage;getDisplayMessage Message Content

oped a Proof-Of-Concept (POC) for AndroByte. The POC

limit the source definition to the list of sensitive APIs

APIs listed in Table 1 are identified and initialized as root

nodes for the D2CFG. Starting from each root node, the

method analysis module is recursively invoked to perform

location data to the Lcom/mintegral/msdk/base/controller/

b;− > a:(Lcom/mintegral/msdk/MIntegralUser;)V function.

This function then calls the Lcom/mintegral/msdk/base/

controller/b;− > b(Lcom/mintegral/msdk/MIntegralUser;)V,

which processed the user object by serializing it to

JSON and logs the location data via the Log.d utility

/String; Ljava/lang/String;)V directly and persist the

JSON and associated ( expiretime ) using the method

5.1. Experiment Setup

| Body() | in | the | Lcom/mintegral/msdk/base/utils/i;− | > | a:(Ljava/lang |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4. Implementation | Lcom/mintegral/msdk/base/utils/u;− | > | b. |  |  |  |  |  |  |
| Based on the module design discussed above, we devel- | 5. Testing and Evaluation |  |  |  |  |  |  |  |  |
| has three modules for method analysis, prompt engineering, | In this section, we evaluate the performance of our pro- |  |  |  |  |  |  |  |  |
| and dynamic dataflow graph generation. In this POC, we | posed approach based on the following research questions: |  |  |  |  |  |  |  |  |
| that are commonly used in Android applications to collect | • | RQ1 - | How accurate is AndroByte in identifying |  |  |  |  |  |  |
| privacy-related user information, as shown in Table 1. | data leaks with D2CFGs using different LLM con- |  |  |  |  |  |  |  |  |
| The primary input for AndroByte’s method analysis | figurations, compared to traditional static analysis |  |  |  |  |  |  |  |  |
| module is the decompiled Android code in | Smali | for- | tools that rely on predefined sink lists? |  |  |  |  |  |  |
| mat. Smali is a human-readable intermediate representation | • | RQ2 - | How effective is AndroByte in generating |  |  |  |  |  |  |
| of bytecode, closely resembling assembly instructions. To | automated D2CFG through the dynamic summariza- |  |  |  |  |  |  |  |  |
| streamline this process, we integrated the APK decompiler | tion of bytecode instructions? |  |  |  |  |  |  |  |  |
| tool, APKTool [50], into AndroByte to convert the Dalvik | • | RQ3 | - | How explainable is AndroByte’s method |  |  |  |  |  |
| bytecode from each APK into its Smali representation. At | analysis in tracking sensitive dataflow and revealing |  |  |  |  |  |  |  |  |
| the start of the application analysis, all call sites for sensitive | potential data leaks in Android applications? |  |  |  |  |  |  |  |  |
| bytecode summarization, identify callee methods through | 5.1.1. Benchmarks. | To answer the above research ques- |  |  |  |  |  |  |  |
| the next methods list, and determine potential sinks. The | tions, we selected two privacy benchmark suites that are |  |  |  |  |  |  |  |  |
| prompts used in this process are scoped and fine-tuned to | commonly used in previous studies [20], [51]–[53], Droid- |  |  |  |  |  |  |  |  |
| follow the context of the sensitive dataflow. An example | Bench [18] and the more recent UBCBench [54], both of |  |  |  |  |  |  |  |  |
| of the method analysis prompt is shown in Appendix A as | which are designed to evaluate privacy leak scenarios in An- |  |  |  |  |  |  |  |  |
| Listing 1. The D2CFG generation module employs a queue- | droid applications. These benchmarks cover a wide range of |  |  |  |  |  |  |  |  |
| based recursive function to manage the analysis flow. Callee | leakage patterns, including aliasing, implicit flows, lifecycle |  |  |  |  |  |  |  |  |
| methods returned by the method analysis are added as child | handling, reflection, field and object sensitivity, and app- |  |  |  |  |  |  |  |  |
| nodes to the graph, which is then traversed iteratively. This | specific behaviors such as callbacks, array manipulations, |  |  |  |  |  |  |  |  |
| process continues until a viable sink is identified or all reach- | and emulator detection mechanisms. Given that AndroByte |  |  |  |  |  |  |  |  |
| able methods have been analyzed. This recursive exploration | is designed to detect privacy leaks through sensitive API |  |  |  |  |  |  |  |  |
| ensures that all method’s caller-callee relationships in the | calls, we applied a filtering strategy to include only the test |  |  |  |  |  |  |  |  |
| path of the target dataflow are accurately captured in the | cases relevant to its detection scope. Specifically, test apps |  |  |  |  |  |  |  |  |
| graph. | in DroidBench that rely on non-API-based flows—such as |  |  |  |  |  |  |  |  |
| To illustrate the D2CFG graph generation, we provide | hardcoded values, user inputs without sensitive API inter- |  |  |  |  |  |  |  |  |
| an | example | in | Figure | 3 | for | the | ”Meme | Generator” | actions, or leaks propagated through ICC were excluded |
| app. At method analysis initialization, AndroByte found | from the evaluation. Similarly, although UBCBench con- |  |  |  |  |  |  |  |  |
| the callsite for the sensitive API | getLatitude() | as | tains 30 test cases, we retained only those that exhibit |  |  |  |  |  |  |
| Lcom/appodeal/ads/networks/r;− | > | d:(Landroid/content/ | privacy behavior. As a result, from the original 118 apps |  |  |  |  |  |  |

---

## Page 7

Lcom/appodeal/ads/networks/r;->d(Landroid/content/Context;)V

Lcom/appodeal/ads/v;->a()Z Lcom/mintegral/msdk/MIntegralUser;-><init>()V

Lcom/mintegral/msdk/base/controller/b;->a(Lcom/mintegral/msdk/MIntegralUser;)V

Lcom/mintegral/msdk/base/controller/b;->b(Lcom/mintegral/msdk/MIntegralUser;)V

Lcom/mintegral/msdk/base/controller/b;->h()V

Lcom/mintegral/msdk/base/utils/i;->a(Ljava/lang/String;Ljava/lang/String;)V

user data are commonly accessed. As mentioned in the

potential data leaks using LLM’s summarization capability.

For experimental evaluation of RQ2 and RQ3, we focused

on 11 representative sensitive APIs (as listed in Table 1),

and selected 300 out of 350 Apps that invoke at least one or

more of these APIs. It is important to note that our approach

is not inherently limited to this predefined set; the selected

APIs serve as a practical subset for validating the system’s

effectiveness in real cases.

| Model Name | Architecture | Context Length | Quantization | Release Date |
| --- | --- | --- | --- | --- |
| deepseek-coder-v2:16b | deepseek2 | 163840 | Q4 0 | June 2024 |

Lcom/mintegral/msdk/system/a;->reportUser(Lcom/mintegral/msdk/MIntegralUser;)V

Lcom/mintegral/msdk/base/controller/b;->a()Lcom/mintegral/msdk/base/controller/b;

Lcom/mintegral/msdk/base/controller/b;-><init>()V

Lcom/mintegral/msdk/base/controller/b$3;-><init>(Lcom/mintegral/msdk/base/controller/b;)V

Lcom/mintegral/msdk/base/utils/u;->b(Landroid/content/Context;Ljava/lang/String;Ljava/lang/Object;)V

Figure 3: D2CFG generated by AndroByte for Meme Generator app

CPU, and 64GB RAM.

5.2. Evaluation Results

5.2.1. RQ1- How accurate is AndroByte in identifying

data leaks with D2CFGs using different LLM config-

urations, compared to traditional static analysis tools

that rely on predefined sink lists?. In this evaluation,

tive is to benchmark and identify the most suitable LLM

The evaluation was conducted using a comprehensive set of

| in DroidBench and 30 in UBCBench, we selected 86 and | Our selection emphasizes recently released models to en- |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 24 test cases, 110 in total for our experiments in RQ1 | sure that the evaluation reflects the latest improvements in |  |  |  |  |  |
| and RQ3. Additionally, we collected 350 real-time Android | architecture, training strategies, and real-world applicability. |  |  |  |  |  |
| applications from the Google Play Store during July 2024, | To maintain consistency, all models were evaluated with |  |  |  |  |  |
| focusing on privacy-relevant categories such as social net- | a fixed context length of 40,000 tokens and a generation |  |  |  |  |  |
| working, health, finance, and other domains where sensitive | temperature of 0.2 to reduce variability. |  |  |  |  |  |
| contribution, our overarching objective of this research is | 5.1.3. Hardware Configuration. | All experiments were run |  |  |  |  |
| to build a system that automatically detects dataflows and | on a local server with an RTX 4090 GPU, Intel i9-13900KF |  |  |  |  |  |
| 5.1.2. LLM | Model | selection:. | Recent | advancement | of | our primary goal is to examine the accuracy of AndroByte |
| LLMs have significantly expanded their functional scope, | in identifying sensitive dataflows and detecting data leaks |  |  |  |  |  |
| enabling enhanced performance in a wide range of engineer- | using the D2CFG. This metric is crucial for assessing the |  |  |  |  |  |
| ing tasks. For the privacy analysis of mobile applications, we | overall effectiveness of the AndroByte design. It covers |  |  |  |  |  |
| initially selected four LLMs from the open-source platform | the method analysis that performs code summarization, the |  |  |  |  |  |
| Ollama based on several criteria, including architectural | prompt engineering that guides the model’s behavior, and |  |  |  |  |  |
| diversity—to ensure balanced and unbiased evaluation—and | the D2CFG construction. The D2CFG is used then to trace |  |  |  |  |  |
| model size, to balance computational efficiency without re- | the flow of sensitive data and identify potential sinks. |  |  |  |  |  |
| quiring large-scale infrastructure. The selected models range | We evaluated the performance of AndroByte integrated |  |  |  |  |  |
| from 8 to 15 billion parameters. Table 2 represents the | with four distinct LLMs to determine which configuration |  |  |  |  |  |
| overview of selected models. | yields the most effective privacy leak detection. The objec- |  |  |  |  |  |
| TABLE 2: Overview of Selected Large Language Models | for integration within AndroByte’s summarization module |  |  |  |  |  |
| qwen3:latest | Qwen3 | 40960 | Q4 K M | April 2025 | analysis pipeline. To compare the performance of AndroBye |  |
| llama3.1:latest | llama | 131072 | Q4 K M | July 2024 | against traditional tools, we also included two established |  |
| gemma3:latest | gemma3 | 131072 | Q4 K M | March 2025 | static analysis tools Amandroid [20] and FlowDroid [18]. |  |
| Additionally, all selected models support low-bit quanti- | test cases from the benchmarks as described in Section 5.1.1. |  |  |  |  |  |
| zation techniques, which significantly reduce resource con- | Table 3 show the comparative analysis between AndroByte |  |  |  |  |  |
| sumption and make it possible to run the models efficiently. | configured with different LLMs and the traditional static |  |  |  |  |  |

---

## Page 8

TABLE 3: Leak Detection Results for AndroByte with Different LLMs Compared to Amandroid and FlowDroid

| AndroByte (LLM Variants) | Amandroid | FlowDroid |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TestCases Suite | GT #Leak | Gemma3 | LLaMA3 | Qwen3 | DeepSeekCoder |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TP | FN FP | TP | FN FP | TP | FN FP | TP | FN FP | TP | FN FP | TP | FN FP |  |  |  |  |  |  |  |  |
| Aliasing | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| AndroidSpecific | 9 | 8 | 1 | 0 | 7 | 1 | 0 | 7 | 2 | 0 | 7 | 2 | 0 | 6 | 3 | 0 | 7 | 2 | 0 |
| ArrayAndLists | 3 | 3 | 0 | 2 | 3 | 0 | 4 | 2 | 0 | 1 | 3 | 0 | 1 | 3 | 2 | 2 | 3 | 0 | 4 |
| Callbacks | 17 | 9 | 8 | 1 | 9 | 7 | 1 | 8 | 8 | 2 | 9 | 8 | 3 | 11 | 8 | 2 | 16 | 1 | 2 |
| Emulator detection | 6 | 4 | 2 | 0 | 4 | 2 | 0 | 5 | 1 | 0 | 3 | 2 | 0 | 4 | 2 | 0 | 4 | 2 | 0 |
| FieldAndObjectSensitivity | 2 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 3 | 1 | 1 | 4 | 2 | 0 | 0 | 2 | 0 | 0 |
| General Java | 20 | 19 | 1 | 1 | 16 | 5 | 1 | 15 | 5 | 1 | 14 | 5 | 2 | 13 | 7 | 3 | 13 | 7 | 5 |
| ImplicitFlow | 2 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 2 | 0 | 0 | 2 | 0 |
| LifeCycle | 17 | 12 | 5 | 0 | 11 | 6 | 0 | 11 | 6 | 0 | 12 | 3 | 0 | 10 | 7 | 0 | 13 | 4 | 0 |
| Reflection | 4 | 3 | 1 | 0 | 3 | 1 | 0 | 3 | 1 | 0 | 3 | 1 | 0 | 3 | 1 | 0 | 2 | 2 | 0 |
| UBCB | 24 | 18 | 6 | 0 | 18 | 6 | 1 | 17 | 7 | 3 | 17 | 7 | 1 | 13 | 9 | 3 | 15 | 9 | 1 |
| Total | 104 | 78 | 26 | 5 | 73 | 30 | 8 | 70 | 31 11 | 70 | 30 | 12 | 65 | 41 11 | 75 | 29 13 |  |  |  |
| Precision, P = TP/(TP+FP) | 93.98% | 90.12% | 86.42% | 85.37% | 85.53% | 85.23% |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Recall, R= TP/(TP+FN) | 75.00% | 70.87% | 69.31% | 70.00% | 61.32% | 72.12% |  |  |  |  |  |  |  |  |  |  |  |  |  |
| F1-score = 2PR/(P+R) | 83.42% | 79.35% | 76.92% | 76.92% | 71.43% | 78.13% |  |  |  |  |  |  |  |  |  |  |  |  |  |

Note: This benchmark includes multiple suites, each composed of test applications designed to evaluate privacy leak detection capabilities. GT # Leak

refers to ground truth nnumber of leak of the benchmarks. In this context, a true positive (TP) is a correctly detected privacy leak, a false positive (FP)

is an incorrect leak report, and a false negative (FN) is a missed leak.

The evaluation results, presented in Table 3, show that

AndroByte integrated with the Gemma3 model achieved

the highest precision of 93.98%, recall of 75%, and F1-

score of 83.42%. On the other hand, LLaMA3 offered a

balanced trade-off with a recall of 70.87% and a reasonable

precision of 90.12%. Qwen3 and DeepSeekCoder exhibited

slightly lower recall but maintained competitive F1 Scores

of 76.92% each, indicating their ability to generalize across

categories with moderate false-positive rates. In contrast, the

defined taint propagation rules. More so, AndroByte’s non-

dependency on a sink list gave it a significant advantage

and greater flexibility over static tools like Amandroid and

FlowDroid. It is worth noting that while traditional tools rely

heavily on predefined source lists for both identifying and

tracing sensitive data flows, AndroByte uses the source list

solely for selecting root nodes. The LLM-driven analysis

then operates independently of predefined source or sink

lists, enabling a broader semantic understanding of privacy-

relevant behavior.

driven, complex Android lifecycle-dependent applications,

such as the Button2, ActivityLifecycle2, BroadcastReceiver-

Lifecycle2, and FragmentLifecycle2 apps in DroidBench.

Nonetheless, for an analysis system based on AI reasoning

without the complexity of taint propagation rules and pre-

defined sink, AndroByte’s results are promising. We believe

that AndroByte’s algorithm can be significantly improved by

fine-tuning the next method selection strategy and ultimately

enhancing the D2CFG.

5.2.2. RQ2- How effective is AndroByte in generating

automated D2CFG through the dynamic summarization

of bytecode instructions?. In this evaluation, our primary

goal is to assess the effectiveness of AndroByte in generat-

ing dynamic data-flow-aware call graphs, starting from the

call site of a single data source. The evaluation focuses on

the system’s summarization capability to detect caller-callee

relationships, identify potential subsequent methods in the

call graph based on the sensitive data flow, perform method

| analysis tools, Amandroid and FlowDroid. It is important | leak. As a result, it does not traverse the secondary path |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| to note that while Amandroid and FlowDroid require a pre- | and, therefore, doesn’t trace to the second sink as shown |  |  |  |  |  |  |  |
| defined sink list (comprising 82 sink methods), AndroByte | in the example app FactoryMethods1 (from DroidBench) |  |  |  |  |  |  |  |
| automatically identifies sinks based on its method contextual | summary provided in Appendix C listing 3. Additionally, |  |  |  |  |  |  |  |
| analysis. | we found that AndroBytes didn’t perform well with event- |  |  |  |  |  |  |  |
| traditional tools Amandroid and FlowDroid demonstrated | In Summary, AndroByte achieves higher recall than |  |  |  |  |  |  |  |
| lower recall 61.32% and 72.12%, respectively —despite | traditional tools like Amandroid and FlowDroid in |  |  |  |  |  |  |  |
| comparable precision. These results highlight AndroByte’s | identifying data leaks while offering an automated |  |  |  |  |  |  |  |
| advantage | in | identifying | privacy | leaks | more | accurately | mechanism for sink detection. Notably, it eliminates |  |
| when guided by LLM-generated summaries, as validated | the reliance on predefined complex propagation rules |  |  |  |  |  |  |  |
| by manual inspection, despite not relying on complex pre- | and sink lists, making it a more adaptable solution. |  |  |  |  |  |  |  |
| Manual | analysis | of | the | apps | missed | by | AndroByte | analysis with recursive tracking, dynamically add nodes and |
| showed that our proposed LLM-driven algorithm misses | edges, and utilize a prompting strategy that fine-tunes and |  |  |  |  |  |  |  |
| leaks in apps with multiple leaks originating from a sin- | guides the summarization process. Leveraging a widely-used |  |  |  |  |  |  |  |
| gle source method, thereby classifying them as a single | static analysis tool Androguard’s [55] call graph generation |  |  |  |  |  |  |  |

---

## Page 9

| as the ground truth, we validated the graphs generated from | edges which we should not be missed, while the false |  |  |  |
| --- | --- | --- | --- | --- |
| the 300 real-world applications in our dataset based on the | negatives (Edges that are missed by | G | AB | but are found in |
| Table 1 mentioned sensitive APIs. This resulted in 300 large | G | AG | ) are potentially edges that are not necessarily related to |  |
| graphs with sub-graphs indicating the flow for the 11 sen- | the dataflow. Thus, if we weigh the precision twice as much |  |  |  |
| sitive APIs for our AndroByte’s. We generated Androguard | as recall and set | β | = 0.5, the weighted harmonic mean will |  |
| call graphs starting from the sensitive API call sites as the | be 89.04%. |  |  |  |

roots. We used precision, recall, F1-Score, and F β -Score

(weighted harmonic mean) as metrics to evaluate effective-

ness. In this analysis, we compare the edges—represented

as (caller, callee) pairs—in the AndroByte-generated graph

G AB with those in the Androguard-generated graph G AG .

False Positive (FP): Edges that appear in G AB but are not

found in G AG .

| Metric | Value (%) |
| --- | --- |
| Precision | 91.75 |
| F1-Score | 85.25 |

Note: Precision is the ratio of correctly predicted edges to all predicted

calculated as: F β = (1 + β 2 ) · Precision · Recall

( β 2 · Precision )+ Recall

Table 4 shows that AndroByte achieved a precision

cision value further validates AndroByte’s claim of correctly

will be more appropriate. In general statistics, the F β -score

In summary, AndroByte can effectively generate accu-

rate dataflow callgraph from bytecode summarization

using LLM’s reasoning and prompt engineering.

potential data leaks in Android applications?. In this

bytecode instructions in natural language and evaluate the

explainability of its summarizations in identifying sensitive

duced evaluation framework by Liu et al. [56], which is

with human judgments when compared to other LLM-based

[57]–[60] as a reliable metric for assessing the quality of

generated content.

| Mean ± SD | Mean ± SD |  |
| --- | --- | --- |
| Relevance | 3.45 ± 0.97 | 3.40 ± 0.87 |
| Fluency | 4.65 ± 0.46 | 4.66 ± 0.43 |

ing 2.

| The parameters are described as follows: | 5.2.3. RQ3- | How | explainable | is | AndroByte’s | method |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| True Positive (TP): Edges that appear in both | G | AG | and | G | AB | . | analysis | in | tracking | sensitive | dataflow | and | revealing |
| TP | = | G | AG | ∩ | G | AB | evaluation, we examine AndroByte’s ability to contextualize |  |  |  |  |  |  |
| FP | = | G | AB | \ | G | AG | dataflows. We utilize G-Eval with GPT4, a recently intro- |  |  |  |  |  |  |
| False Negative (FN): Edges that are missed by | G | AB | but are | specifically designed for open-ended natural language gen- |  |  |  |  |  |  |  |  |  |
| found in | G | AG | . | eration. This metric captures both semantic alignment and |  |  |  |  |  |  |  |  |  |
| FN | = | G | AG | \ | G | AB | factual accuracy, and has demonstrated superior correlation |  |  |  |  |  |  |
| TABLE 4: AndroByte Graph generation Performance | evaluation techniques. G-Eval is increasingly recognized |  |  |  |  |  |  |  |  |  |  |  |  |
| Recall | 79.67 | TABLE 5: G-Eval Metrics for Generated Summaries |  |  |  |  |  |  |  |  |  |  |  |
| F | β | -Score ( | β | = 0 | . | 5 | ) | 89.04 | G-Eval Metric | DroidBench | UBCBench |  |  |
| edges; recall is the ratio of correctly predicted edges to all actual edges. | Coherence | 4.65 ± 0.46 | 4.66 ± 0.43 |  |  |  |  |  |  |  |  |  |  |
| F1-score is the harmonic mean of precision and recall. The F | β | -Score is | Consistency | 4.10 ± 0.92 | 4.30 ± 0.90 |  |  |  |  |  |  |  |  |
| of 91.75%, which is the proportion of correctly predicted | Average per Dataset | 4.21 ± 0.70 | 4.26 ± 0.66 |  |  |  |  |  |  |  |  |  |  |
| caller-callee edges to the total predicted edges. The high pre- | Overall Avg. Score | 4.24 ± 0.68 |  |  |  |  |  |  |  |  |  |  |  |
| generating dynamic D2CFG on the fly using summarization | In our evaluation, we define five core aspects of dataflow |  |  |  |  |  |  |  |  |  |  |  |  |
| capability. On the other hand, AndroByte achieved a moder- | summarization quality: (1) identification of sensitive data |  |  |  |  |  |  |  |  |  |  |  |  |
| ately lower recall rate of 79.67%, indicating the proportion | types, (2) accuracy of data propagation, (3) correctness of |  |  |  |  |  |  |  |  |  |  |  |  |
| of correctly predicted edges to the total actual edges. Our | sink function detection, (4) leakage inference capability, |  |  |  |  |  |  |  |  |  |  |  |  |
| manual graph analysis showed that the lower recall is at- | and (5) overall coherence and fluency. To quantify these |  |  |  |  |  |  |  |  |  |  |  |  |
| tributed to AndroByte’s D2CFG focus on privacy-sensitive | aspects, we use the four evaluation dimensions defined in G- |  |  |  |  |  |  |  |  |  |  |  |  |
| dataflows, thus overlooking the next methods (caller-called | Eval. Specifically, consistency aggregates the first, second, |  |  |  |  |  |  |  |  |  |  |  |  |
| edges) that are not directly associated with sensitive data. | and fourth aspects—capturing factual alignment and internal |  |  |  |  |  |  |  |  |  |  |  |  |
| Androguard’s call graph, on the other hand, is more generic | logic. Relevance reflects both data propagation accuracy |  |  |  |  |  |  |  |  |  |  |  |  |
| and thus includes all caller-callee edges irrespective of the | and sink function detection, focusing on whether summaries |  |  |  |  |  |  |  |  |  |  |  |  |
| dataflow. Using a standard F1-score that balances precision | emphasize key semantic content. Coherence and fluency |  |  |  |  |  |  |  |  |  |  |  |  |
| and recall, AndroByte achieved an accuracy of 85.25%. But | correspond directly to our fifth aspect, assessing structural |  |  |  |  |  |  |  |  |  |  |  |  |
| given that the actual number of edges based on Andro- | clarity and linguistic quality. This mapping enables us to |  |  |  |  |  |  |  |  |  |  |  |  |
| guard’s ground truth may likely be more generic and those | compute G-Eval scores (on a 5-point scale) for AndroByte |  |  |  |  |  |  |  |  |  |  |  |  |
| edges that are not part of the data-flow-aware call graph may | on both DroidBench and UBCBench, as reported in Table 5, |  |  |  |  |  |  |  |  |  |  |  |  |
| be missed, we believe a F | β | -score for the accuracy metric | using the evaluation prompt provided in Appendix B, List- |  |  |  |  |  |  |  |  |  |  |
| with | β < | 1 | is used when precision is more critical than | To reduce model variance, all evaluations were repeated |  |  |  |  |  |  |  |  |  |
| recall. In our case, the false positives (Edges that appear in | across 10 runs using a fixed temperature setting of 0.2 |  |  |  |  |  |  |  |  |  |  |  |  |
| G | AB | but are not found in | G | AG | ) potentially signify dataflow | on the same dataset analyzed in RQ1. Since no publicly |  |  |  |  |  |  |  |

---

## Page 10

Figure 4: Example – getLastKnownLocation() Call Site

| available ground truth method or graph-level summaries | evaluation) and observed that it generates detailed sum- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exist for Android apps, we derive ground-truth summaries | maries, identifies dataflows via dynamic call graphs, and de- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| by manually interpreting and distilling the code comments | tects sinks without relying on predefined rules and/or known |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and inline documentation provided in each application of | sink lists. Figure 4 presents an example from the ”myfitness- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| DroidBench and UBCBench benchmarks. While these sum- | pal” app. Given the sensitive API getLastKnownLocation(), |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| maries may not capture all implicit behaviors, they reflect | AndroByte identifies the call site as Lcom/moat/analytics |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| a reasonable approximation of intended dataflow semantics | /mobile/und/o. | Tracing | the | dataflow | determines | that | the |  |  |  |  |  |  |  |  |  |  |  |  |
| and are used as reference baselines for evaluating An- | variables | v1 | and | v2 | hold the retrieved location data. This |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| droByte’s summarization performance. Table 5 shows that | location data is subsequently passed to the | b() | function, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| AndroByte-generated summaries exhibit strong coherence | which then further processes the data in the | a() | function. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and fluency ( | 4 | . | 65 | ± | 0 | . | 46 | & | 4 | . | 66 | ± | 0 | . | 43 | ) across both datasets, | The | a() | function logs the data or handles exceptions. |

reflecting clear and well-structured natural language outputs.

Consistency also scores well ( 4 . 10 ± 0 . 92 & 4 . 30 ± 0 . 90 ), in-

dicating reasonable factual alignment with the ground truth.

However, the slightly lower relevance score ( 3 . 45 ± 0 . 97

& 3 . 40 ± 0 . 87 ) may be partially attributed to the brevity

and limited specificity of the ground truth summaries, which

can hinder the evaluation model’s ability to fully capture

the semantic coverage present in the generated outputs.

AndroByte achieves an overall G-Eval score of 4.24, the

average of its Coherence, Consistency, Relevance, and Flu-

ency means.

Table 6 provides AndroByte’s summary of the callsite

(root node) and the list of next methods, as determined

through summarization, which was dynamically added to

the graph with edges connected to the root node. Table 7

demonstrates how these methods are further summarized.

Notably, the summary reveals that the b() function does not

propagate the sensitive data. In contrast, the a() function

does, passing the data to the Android logging utility, which

signifies a potential data leak into the Android Log. Table

8 provides a detailed output of a single analysis, starting at

the call site. It includes summarization, recursive determina-

| Furthermore, we manually inspected the output of An- | tion of the next methods, further summarization to identify |
| --- | --- |
| droByte on some real-world apps from the 300 real-world | potential sinks, or the determination of the next method. |
| apps in RQ2 (as no ground truth is available for systematic | This process continues iteratively. This output, as illustrated, |

---

## Page 11

TABLE 6: Call Site Summary

| Summary | Next Methods |  |  |  |
| --- | --- | --- | --- | --- |
| Sensitive user location data is retrieved from the | LocationManager | 1.com/moat/analytics/mobile/und/o;− | > | b(android/location/Location; |
| using | getLastKnownLocation() | methods for both GPS and | android/location/Location;) android/location/Location; |  |
| network providers. The retrieved location data is then passed to the | b() | 2.com/moat/analytics/mobile/und/m;− | > | a(Ljava/lang/Exception;)V |

method and potentially forwarded to other methods.

TABLE 7: Next Method Summary

Method Signature

android/location/Location;) android/location/Location;

;−

| Parameters | Details |
| --- | --- |
| Data Types | Location |

Overall Dataflow

• Step: Location retrieved from getLastKnownLocation()

Source Method:

Reasoning:

Action: Stored

• Step: Location passed to API method

Source Method:

Location;)Landroid/location/Location;

Reasoning:

Action: Logged

| All Sinks | com/moat/analytics/mobile/inm/o;− | > |
| --- | --- | --- |
| Complete Dataflow | com/moat/analytics/mobile/inm/o;− | > |

com/moat/analytics/mobile/inm/o;− >

Location; → com/moat/analytics/mobile/inm/o;−

Reasoning:

Label Leak

Summary

sink detected.”

> a()com/moat/analytics/mobile/und/w;‘.Data is logged using

‘invoke-static android/util/Log;− > e(java/lang/String;java/lang/String;)I”

TABLE 8: DataFlow Analysis Summary

Lcom/moat/analytics/mobile/inm/o;− > f:()Landroid/location/Location;

Sensitive data originated in this method.

Lcom/moat/analytics/mobile/inm/o;− > b:(Landroid/location/Location; Landroid/location/

Sensitive data is passed between methods.

a:(Landroid/location/Location;)V

f:()android/location/Location; →

b:(android/location/Location; android/location/Location;)android/location/

> a:(android/location/Location;)V

Location data is retrieved, passed to API method, and then logged.

adaptability. Utilizing bytecode summarization, AndroByte

systems.

Hallucination Mitigation: Hallucination concerns are

droByte with practical mitigation strategies. First, the anal-

| com/moat/analytics/mobile/und/o;− | > | b(android/location/Location; | ”Method does not originate, store, or pass sensitive user personal data. No |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| com/moat/analytics/mobile/und/m;− | > | a(Ljava/lang/Exception;)V | ”Sensitive API call detected: invoke-static com/moat/analytics/mobile/und/w |  |  |  |  |  |
| provides an overview of the dataflow, including reasoning, | defining | feature | of | AndroByte | is | its | implementation | of |
| the identified sink, the complete dataflow, and a label in- | next-method tracking, which enhances its ability to detect |  |  |  |  |  |  |  |
| dicating whether sensitive data is leaked. This evaluation | dataflows from sensitive sources while concurrently building |  |  |  |  |  |  |  |
| validates the comprehensiveness of the summaries through | caller-callee relationships. It also validates the robustness of |  |  |  |  |  |  |  |
| logical reasoning and explainability, while highlighting An- | our bytecode summarization technique for method analysis, |  |  |  |  |  |  |  |
| droByte’s ability to deliver a detailed, interpretable descrip- | demonstrating the comprehensiveness, practical explainabil- |  |  |  |  |  |  |  |
| tion of the data leak propagation and sink. A detailed | ity, and accuracy of the generated summaries. This targeted |  |  |  |  |  |  |  |
| heat map analysis of sensitive data handling by category | approach enables precise analysis of user data collection |  |  |  |  |  |  |  |
| is presented in Appendix D as Figure 5, highlighting the | processes, effectively identifying potential sensitive data |  |  |  |  |  |  |  |
| prominent exposure of location data compared to other data | flows leading to user data leaks in Android applications with |  |  |  |  |  |  |  |
| types. | accuracy as high as existing techniques but with much better |  |  |  |  |  |  |  |
| In | summary, | AndroByte | demonstrates | practical | ex- | expands its contextual understanding and eliminates the |  |  |
| plainability in tracking sensitive data propagation and | need for predefined sinks, addressing the limitations and |  |  |  |  |  |  |  |
| revealing potential leaks in mobile applications. | algorithmic complexities of traditional static taint analysis |  |  |  |  |  |  |  |
| 6. Discussion | addressed and integrated inherently into the design of An- |  |  |  |  |  |  |  |
| The | evaluation | of | AndroByte | underscores | its | effec- | ysis process begins strictly from source methods of a de- |  |
| tiveness in dynamically generating automated D2CFG us- | compiled APK that invoke sensitive APIs thereby avoiding |  |  |  |  |  |  |  |
| ing language model reasoning and prompt engineering. A | the introduction of non-existent entry paths. Second, dur- |  |  |  |  |  |  |  |

---

## Page 12

| ing method analysis, occasional hallucinations may occur, | proved AndroByte’s overall performance and scalability. |  |
| --- | --- | --- |
| such as the generation of non-existent methods or invalid | The performance evaluation of AndroByte including method |  |
| signatures by the model in the returned NEXT METHODS | analysis, graph generation, sink detection, and summary |  |
| list. To address this, AndroByte performs validation against | generation shows that for real-world applications ranging in |  |
| a statically extracted ALL METHODS list generated during | size from 2MB to 670MB (average 45MB), the average anal- |  |
| the app decompilation. Any hallucinated method not present | ysis time was approximately 2.5 minutes per application. |  |
| in this list is discarded and excluded from graph construction | While this runtime is acceptable for static analysis, further |  |
| or further recursive method analysis. This lookup acts as | improvements are possible in real deployment scenarios with |  |
| a sanity check, ensuring only valid methods propagate in | more advanced hardware, enabling even faster processing. |  |
| the graph. Third, once the full dataflow graph is gener- | For future work, we aim to conduct a human validation |  |
| ated, it is cross-validated against a call graph generated | study to assess the accuracy and efficacy of the gener- |  |
| by AndroGuard described in Section | 5.2.2. For identifying | ated summaries in practical scenarios. We also intend to |
| sink detection and leak inference, AndroByte enforces the | strengthen reliability by incorporating advanced LLM output |  |
| invariant that all leaks must appear as leaf nodes in the | validation mechanisms, such as confidence estimation, and |  |
| graph. In the explainability component, which summarizes | by testing with larger datasets and diverse models, including |  |
| the analysis, AndroByte uses (1) a consistency metric com- | GPT-NeoX, OPT, as well as frontier models, to explore |  |
| posed of: (i) accuracy of sensitive data type identification | performance variations and scalability. Furthermore, we aim |  |
| (ii) correctness of data propagation, and (iii) leak inference | to enhance AndroByte by incorporating static and dynamic |  |
| accuracy; and (2) a relevancy metric, which is composed of | analysis techniques, enabling a more comprehensive view of |  |
| data propagation accuracy and sink function detection, as | runtime data flows and improving the detection of privacy |  |
| described Section | 5.2.3. | leaks. |

Limitations & Future Work: Although AndroByte

performs effectively on real-world data, DroidBench and

UBCBench samples, it is not without its drawbacks, as

itemized below: (1) Dependency on Bytecode Quality -

for critical analyses is essential in real-world deployment.

This could involve sampling LLM-generated summaries for

manual validation. (3) Performance Overhead - The inte-

gration of language models for bytecode summarization

is computationally expensive, particularly when analyzing

large volume of apps or highly interconnected call graphs

Furthermore, AndroByte’s analysis duration significantly

depends on the selected LLM’s context window size. In

7. Conclusion

References

Ericsson Reports & Papers , 2022, accessed: 2023-12-01.

[Online]. Available: https://www.ericsson.com/en/reports-and-papers/

[2] S. Yang, Z. Zeng, and W. Song, “Permdroid: automatically testing

permission-related behaviour of android applications,” in Proceedings

| While AndroByte effectively analyzes bytecode, heavily | This study presents AndroByte, an innovative approach |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| obfuscated or minified code can hinder its ability to generate | to privacy analysis that combines LLM-driven reasoning and |  |  |  |  |  |  |  |  |
| accurate summaries or trace dataflows. Furthermore, apps | bytecode summarization for method and data flow analysis. |  |  |  |  |  |  |  |  |
| that load code dynamically at runtime may bypass static | AndroBytes’s design eliminates the reliance on predefined |  |  |  |  |  |  |  |  |
| analysis, leading to incomplete dataflow graphs. Although | sinks and propagation rules, enabling automated detection |  |  |  |  |  |  |  |  |
| this is an important limitation, it is generic to all static | of | data | leaks | directly | from | the | bytecode. | Its | dynamic |
| analysis techniques irrespective of the algorithm applied. | dataflow | call | graph | generation | (D2CFG) | component |  |  |  |
| Given the huge overhead of dynamic analysis techniques, es- | constructs a recursive and iterative representation of the |  |  |  |  |  |  |  |  |
| pecially in taint analysis, tools like AndroByte are still very | program’s | behavior, | connecting | methods | through | caller- |  |  |  |
| well needed in the community and cannot be completely re- | callee relationships and tracing sensitive data to identify |  |  |  |  |  |  |  |  |
| placed. (2) Dependency on LLM for Reasoning - AndroByte | potential | sinks. | The | evaluation | of | AndroByte | on | real- |  |
| relies heavily on the reasoning capabilities of LLMs for | world applications and benchmark datasets demonstrates |  |  |  |  |  |  |  |  |
| bytecode summarization and graph generation. The resulting | its | effectiveness | in | graph | generation | and | identifying |  |  |
| dataflow graph and analyses could be inaccurate if the | sensitive data propagation with high accuracy. Additionally, |  |  |  |  |  |  |  |  |
| LLM generates incorrect or irrelevant summaries due to | our | evaluation | highlights | the | comprehensive | summary |  |  |  |
| context misinterpretation or insufficient domain knowledge, | and | practical | explainability | of | the | privacy | analysis. | By |  |
| and without a robust validation mechanism, such errors may | integrating | AI | reasoning, | bytecode | summarization, | and |  |  |  |
| propagate and undermine reliability in critical scenarios. | recursive | graph | construction, | AndroByte | provides | an |  |  |  |
| Although AndroByte performed well on three datasets, the | effective, explainable, and adaptable technique for privacy |  |  |  |  |  |  |  |  |
| robustness of AndroByte should be validated with much | analysis in Android applications, setting a new standard for |  |  |  |  |  |  |  |  |
| larger datasets. Additionally, introducing human reviewers | automated privacy analysis tools. |  |  |  |  |  |  |  |  |
| large or complex applications. Real-world scenarios with a | [1] | Ericsson, | “Ericsson | mobility | report | (november | 2022 | edition),” |  |
| may result in increased processing time and memory usage. | mobility-report/reports/november-2022 |  |  |  |  |  |  |  |  |
| our experiments, we utilized a context window of 40,000 | of the 31st ACM SIGSOFT International Symposium on Software |  |  |  |  |  |  |  |  |
| tokens with the local model gemma3:l, which notably im- | Testing and Analysis | , 2022, pp. 593–604. |  |  |  |  |  |  |  |

---

## Page 13

| [3] | W. Enck, P. Gilbert, S. Han, V. Tendulkar, B.-G. Chun, L. P. Cox, | [19] | L. Li, A. Bartel, T. F. Bissyand´ | e, J. Klein, Y. Le Traon, S. Arzt, |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J. Jung, P. McDaniel, and A. N. Sheth, “Taintdroid: an information- | S. Rasthofer, E. Bodden, D. Octeau, and P. McDaniel, “Iccta: De- |  |  |  |  |  |  |  |  |  |
| flow | tracking | system | for | realtime | privacy | monitoring | on | smart- | tecting inter-component privacy leaks in android apps,” in | 2015 |
| phones,” | ACM Transactions on Computer Systems (TOCS) | , vol. 32, | IEEE/ACM 37th IEEE International Conference on Software Engi- |  |  |  |  |  |  |  |
| no. 2, pp. 1–29, 2014. | neering | , vol. 1. | IEEE, 2015, pp. 280–291. |  |  |  |  |  |  |  |
| [4] | J. Reardon, ´ | A. Feal, P. Wijesekera, A. E. B. On, N. Vallina-Rodriguez, | [20] | F. Wei, S. Roy, X. Ou, and Robby, “Amandroid: A precise and general |  |  |  |  |  |  |
| and S. Egelman, “50 ways to leak your data: An exploration of apps’ | inter-component data flow analysis framework for security vetting of |  |  |  |  |  |  |  |  |  |
| circumvention of the android permissions system,” in | 28th USENIX | android apps,” | ACM Transactions on Privacy and Security (TOPS) | , |  |  |  |  |  |  |
| security symposium (USENIX security 19) | , 2019, pp. 603–620. | vol. 21, no. 3, pp. 1–32, 2018. |  |  |  |  |  |  |  |  |
| [5] | Q. Luo, Y. Yu, J. Liu, and A. Benslimane, “Automatic detection for | [21] | “GitHub | Repository | for | AndroByte | Artifacts,” | https: |  |  |
| privacy violations in android applications,” | IEEE Internet of Things | //github.com/Eshita66/AndroByte, | 2025, | [Online]. | Available: |  |  |  |  |  |
| Journal | , vol. 9, no. 8, pp. 6159–6172, 2021. | https://github.com/Eshita66/AndroByte. Accessed: May 30, 2025. |  |  |  |  |  |  |  |  |
| [6] | Y. Wang, Y. Wang, S. Wang, Y. Liu, C. Xu, S.-C. Cheung, H. Yu, | [22] | Z. Yang and M. Yang, “Leakminer: Detect information leakage on |  |  |  |  |  |  |  |
| and Z. Zhu, “Runtime permission issues in android apps: Taxonomy, | android with static taint analysis,” in | 2012 Third World Congress on |  |  |  |  |  |  |  |  |
| practices, and ways forward,” | IEEE Transactions on Software Engi- | Software Engineering | . | IEEE, 2012, pp. 101–104. |  |  |  |  |  |  |

neering , vol. 49, no. 1, pp. 185–210, 2022.

Conference (SecDev) . IEEE, 2024, pp. 64–75.

conference on Computer & communications security , 2013, pp. 1043–

1054.

[10] N.-W. Lo, K.-H. Yeh, and C.-Y. Fan, “Leakage detection and risk

assessment on privacy for android applications: Lrpdroid,” IEEE

Systems Journal , vol. 10, no. 4, pp. 1361–1369, 2014.

[11] J. P. Achara, J.-D. Lefruit, V. Roca, and C. Castelluccia, “Detecting

privacy leaks in the ratp app: How we proceeded and what we found,”

Journal of Computer Virology and Hacking Techniques , vol. 10, pp.

229–238, 2014.

International Conference on Software Engineering (ICSE) . IEEE,

2023 ACM SIGSAC Conference on Computer and Communications

[17] Y. Wang, M. Fan, J. Liu, J. Tao, W. Jin, H. Wang, Q. Xiong, and

[18] S. Arzt, S. Rasthofer, C. Fritz, E. Bodden, A. Bartel, J. Klein,

Y. Le Traon, D. Octeau, and P. McDaniel, “Flowdroid: Precise

context, flow, field, object-sensitive and lifecycle-aware taint analysis

for android apps,” ACM sigplan notices , vol. 49, no. 6, pp. 259–269,

2014.

[23] D. Octeau, P. McDaniel, S. Jha, A. Bartel, E. Bodden, J. Klein, and

543–558.

Pittsburgh, PA, USA, 2014.

[26] L. Li, A. Bartel, J. Klein, and Y. Le Traon, “Automatically exploiting

potential component leaks in android applications,” in 2014 IEEE

13th International Conference on Trust, Security and Privacy in

Computing and Communications . IEEE, 2014, pp. 388–397.

[27] M. I. Gordon, D. Kim, J. H. Perkins, L. Gilham, N. Nguyen, and

M. C. Rinard, “Information flow analysis of android applications in

droidsafe.” in NDSS , vol. 15, no. 201, 2015, p. 110.

145–147.

235–248, 2018.

2024, pp. 248–254.

[35] Y. Huang, J. Huang, X. Chen, K. He, and X. Zhou, “Bcgen: a

comment generation method for bytecode,” Automated Software En-

gineering , vol. 30, no. 1, p. 5, 2023.

| [7] | S. Bello, B. Bappah, N. R. Tanet, A. S. Betzwieser, and A. Ali- | Y. Le Traon, “Effective | { | Inter-Component | } | communication mapping |
| --- | --- | --- | --- | --- | --- | --- |
| Gombe, “User privacy in the digital playground: An in-depth investi- | in android: An essential step towards holistic security analysis,” in |  |  |  |  |  |
| gation of facebook instant games,” in | 2024 IEEE Secure Development | 22nd USENIX Security Symposium (USENIX Security 13) | , 2013, pp. |  |  |  |
| [8] | S. Bello, L. Noureddine, B. Bappah, and A. I. Ali-Gombe, “The | [24] | W. Klieber, L. Flynn, A. Bhosale, L. Jia, and L. Bauer, “Android |  |  |  |
| privacy cost of fun: A measurement study of user data exposure in | taint flow analysis for app sets,” in | Proceedings of the 3rd ACM |  |  |  |  |
| tiktok mini-games,” | Computers & Security | , 2025. | SIGPLAN International Workshop on the State of the Art in Java |  |  |  |
| [9] | Z. Yang, M. Yang, Y. Zhang, G. Gu, P. Ning, and X. S. Wang, | Program Analysis | , 2014, pp. 1–6. |  |  |  |
| “Appintent: Analyzing sensitive data transmission in android for | [25] | A. S. Bhosale, “Precise static analysis of taint flow for android appli- |  |  |  |  |
| privacy leakage detection,” in | Proceedings of the 2013 ACM SIGSAC | cation sets,” M.S. thesis, Heinz College, Carnegie Mellon University, |  |  |  |  |
| [12] | S. S. Hashmi, N. Waheed, G. Tangari, M. Ikram, and S. Smith, | [28] | A. Bosu, F. Liu, D. Yao, and G. Wang, “Collusive data leak and |  |  |  |
| “Longitudinal compliance analysis of android applications with pri- | more: Large-scale threat analysis of inter-app communications,” in |  |  |  |  |  |
| vacy policies,” in | International Conference on Mobile and Ubiquitous | Proceedings of the 2017 ACM on Asia Conference on Computer and |  |  |  |  |
| Systems: Computing, Networking, and Services | . | Springer, 2021, pp. | Communications Security | , 2017, pp. 71–85. |  |  |
| 280–305. | [29] | A. Ali-Gombe, I. Ahmed, G. G. Richard III, and V. Roussev, “Aspect- |  |  |  |  |
| [13] | Z. Tan and W. Song, “Ptpdroid: Detecting violated user privacy | droid: Android app analysis system,” in | Proceedings of the Sixth ACM |  |  |  |
| disclosures to third-parties of android apps,” in | 2023 IEEE/ACM 45th | Conference on Data and Application Security and Privacy | , 2016, pp. |  |  |  |
| 2023, pp. 473–485. | [30] | A. I. Ali-Gombe, B. Saltaformaggio, D. Xu, G. G. Richard III | et al. | , |  |  |
| [14] | A. Xiang, W. Pei, and C. Yue, “Policychecker: Analyzing the gdpr | “Toward a more dependable hybrid analysis of android malware using |  |  |  |  |
| completeness of mobile apps’ privacy policies,” in | Proceedings of the | aspect-oriented programming,” | computers & security | , vol. 73, pp. |  |  |
| Security | , 2023, pp. 3373–3387. | [31] | A. I. Ali-Gombe, “Malware analysis and privacy policy enforcement |  |  |  |
| [15] | C. Schindler, M. Atas, T. Strametz, J. Feiner, and R. Hofer, “Privacy | techniques for android applications,” 2017. |  |  |  |  |
| leak identification in third-party android libraries,” in | 2022 seventh in- | [32] | A. Ali-Gombe, I. Ahmed, G. G. Richard III, and V. Roussev, “Opseq: |  |  |  |
| ternational conference on mobile and secure services (MobiSecServ) | . | Android malware fingerprinting,” in | Proceedings of the 5th Program |  |  |  |
| IEEE, 2022, pp. 1–6. | Protection and Reverse Engineering Workshop | , 2015, pp. 1–12. |  |  |  |  |
| [16] | G. Morales, K. Pragyan, S. Jahan, M. B. Hosseini, and R. Slavin, | [33] | B. J. Walton, M. E. Khatun, J. M. Ghawaly, and A. Ali-Gombe, |  |  |  |
| “A large language model approach to code and privacy policy align- | “Exploring large language models for semantic analysis and cate- |  |  |  |  |  |
| ment,” in | 2024 IEEE International Conference on Software Analysis, | gorization of android malware,” in | 2024 Annual Computer Security |  |  |  |
| Evolution and Reengineering (SANER) | . | IEEE, 2024, pp. 79–90. | Applications Conference Workshops (ACSAC Workshops) | . | IEEE, |  |
| T. Liu, “Do as you say: Consistency detection of data practice in | [34] | J. Xiang, Z. Gao, L. Bao, X. Hu, J. Chen, and X. Xia, “Automating |  |  |  |  |
| program code and privacy policy in mini-app,” | IEEE Transactions on | comment generation for smart contract from bytecode,” | ACM Trans- |  |  |  |
| Software Engineering | , 2024. | actions on Software Engineering and Methodology | , 2024. |  |  |  |

---

## Page 14

| [36] | Y. Huang, J. Huang, X. Chen, and Z. Zheng, “Towards improving | [48] | J. Woodring, K. Perez, and A. Ali-Gombe, “Enhancing privacy policy |  |  |
| --- | --- | --- | --- | --- | --- |
| the performance of comment generation models by using bytecode | comprehension through privacify: A user-centric approach using ad- |  |  |  |  |
| information,” | IEEE Transactions on Software Engineering | , 2025. | vanced language models,” | Computers & Security | , vol. 145, p. 103997, |

2024.

[37] W. Li, X. Li, Z. Li, and Y. Zhang, “Cobra: Interaction-aware

| bytecode-level vulnerability detector for smart contracts,” in | Proceed- | [49] | X. Zhang, H. Xu, Z. Ba, Z. Wang, Y. Hong, J. Liu, Z. Qin, and |
| --- | --- | --- | --- |
| ings of the 39th IEEE/ACM International Conference on Automated | K. Ren, “Privacyasst: Safeguarding user privacy in tool-using large |  |  |
| Software Engineering | , 2024, pp. 1358–1369. | language model agents,” | IEEE Transactions on Dependable and |

Secure Computing , 2024.

[38] A. Sch¨ afer, T. S. Heinze, and W. Amme, “Finding source code clones

in intermediate representations of java bytecode,” in 2023 IEEE 17th [50] ibotpeaches, “Apktool documentation,” Obtenido de APKTool , 2018.

International Workshop on Software Clones (IWSC) . IEEE, 2023, [Online]. Available: https://ibotpeaches.github.io/Apktool/

pp. 37–43.

[51] N. Grech and Y. Smaragdakis, “P/taint: Unified points-to and taint

[39] E. Fevid, C. Walsh, and L. Russo, “Zero-day ransomware detection analysis,” Proceedings of the ACM on Programming Languages ,

via assembly language bytecode analysis and random forest classifi- vol. 1, no. OOPSLA, pp. 1–28, 2017.

cation,” Authorea Preprints , 2024.

[52] J. Mitra, V.-P. Ranganath, and A. Narkar, “Benchpress: Analyzing

| [40] | H. | Liu, | L. | Gong, | X. | Mo, | G. | Dong, | and | J. | Yu, | “Ltachecker: | android app vulnerability benchmark suites,” in | 2019 34th IEEE/ACM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lightweight android malware detection based on dalvik opcode se- | International Conference on Automated Software Engineering Work- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| quences using attention temporal networks,” | IEEE Internet of Things | shop (ASEW) | . | IEEE, 2019, pp. 13–18. |  |  |  |  |  |  |  |  |  |  |
| Journal | , 2024. | [53] | M. Chen, T. Tan, M. Pan, and Y. Li, “Pacdroid: A pointer-analysis- |  |  |  |  |  |  |  |  |  |  |  |
| [41] | V. Jain, S. D. Gupta, S. Ghanavati, S. T. Peddinti, and C. McMillan, | centric framework for security vulnerabilities in android apps,” in |  |  |  |  |  |  |  |  |  |  |  |  |
| “Pact: Detecting and classifying privacy behavior of android applica- | 2025 IEEE/ACM 47th International Conference on Software Engi- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tions,” in | Proceedings of the 15th ACM Conference on Security and | neering (ICSE) | . | IEEE Computer Society, 2025, pp. 744–744. |  |  |  |  |  |  |  |  |  |  |
| Privacy in Wireless and Mobile Networks | , 2022, pp. 104–118. | [54] | J. Zhang, Y. Wang, L. Qiu, and J. Rubin, “Analyzing android taint |  |  |  |  |  |  |  |  |  |  |  |
| [42] | G. Hu, B. Zhang, X. Xiao, W. Zhang, L. Liao, Y. Zhou, and X. Yan, | analysis tools: Flowdroid, amandroid, and droidsafe,” | IEEE Trans- |  |  |  |  |  |  |  |  |  |  |  |
| “Samldroid: a static taint analysis and machine learning combined | actions on Software Engineering | , vol. 48, no. 10, pp. 4014–4040, |  |  |  |  |  |  |  |  |  |  |  |  |
| high-accuracy method for identifying android apps with location | 2021. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| privacy leakage risks,” | Entropy | , vol. 23, no. 11, p. 1489, 2021. | [55] | A. Desnos and G. Gueguen, “Androguard documentation,” | Obtenido |  |  |  |  |  |  |  |  |  |
| [43] | J. Feichtner and S. Gruber, “Understanding privacy awareness in | de Androguard | , 2018. |  |  |  |  |  |  |  |  |  |  |  |
| android app descriptions using deep learning,” in | Proceedings of the | [56] | Y. Liu, D. Iter, Y. Xu, S. Wang, R. Xu, and C. Zhu, “G-eval: Nlg |  |  |  |  |  |  |  |  |  |  |  |
| tenth ACM conference on data and application security and privacy | , | evaluation using gpt-4 with better human alignment,” | arXiv preprint |  |  |  |  |  |  |  |  |  |  |  |
| 2020, pp. 203–214. | arXiv:2303.16634 | , 2023. |  |  |  |  |  |  |  |  |  |  |  |  |
| [44] | M. S. Rahman, P. Naghavi, B. Kojusner, S. Afroz, B. Williams, | [57] | L. Chen, O. Sinavski, J. H¨ | unermann, A. Karnsund, A. J. Willmott, |  |  |  |  |  |  |  |  |  |  |
| S. Rampazzi, and V. Bindschaedler, “Permpress: Machine learning- | D. Birch, D. Maund, and J. Shotton, “Driving with llms: Fusing |  |  |  |  |  |  |  |  |  |  |  |  |  |
| based pipeline to evaluate permissions in app privacy policies,” | IEEE | object-level vector modality for explainable autonomous driving,” in |  |  |  |  |  |  |  |  |  |  |  |  |
| Access | , vol. 10, pp. 89 248–89 269, 2022. | 2024 IEEE International Conference on Robotics and Automation |  |  |  |  |  |  |  |  |  |  |  |  |
| [45] | H. Ma, J. Tian, K. Qiu, D. Lo, D. Gao, D. Wu, C. Jia, and T. Baker, | (ICRA) | . | IEEE, 2024, pp. 14 093–14 100. |  |  |  |  |  |  |  |  |  |  |
| “Deep-learning–based app sensitive behavior surveillance for android | [58] | E. Shayegani, M. A. A. Mamun, Y. Fu, P. Zaree, Y. Dong, and |  |  |  |  |  |  |  |  |  |  |  |  |
| powered cyber–physical systems,” | IEEE Transactions on Industrial | N. Abu-Ghazaleh, “Survey of vulnerabilities in large language models |  |  |  |  |  |  |  |  |  |  |  |  |
| Informatics | , vol. 17, no. 8, pp. 5840–5850, 2020. | revealed by adversarial attacks,” | arXiv preprint arXiv:2310.10844 | , |  |  |  |  |  |  |  |  |  |  |
| [46] | Y. Liu, N. Xi, and Y. Zhi, “Nleu: A semantic-based taint analysis | 2023. |  |  |  |  |  |  |  |  |  |  |  |  |
| for vetting apps in android,” in | 2021 International Conference on | [59] | R. Kamoi, Y. Zhang, N. Zhang, J. Han, and R. Zhang, “When can |  |  |  |  |  |  |  |  |  |  |  |
| Networking and Network Applications (NaNA) | . | IEEE, 2021, pp. | llms actually correct their own mistakes? a critical survey of self- |  |  |  |  |  |  |  |  |  |  |  |
| 327–333. | correction of llms,” | Transactions of the Association for Computational |  |  |  |  |  |  |  |  |  |  |  |  |
| [47] | H. Fu, Z. Zheng, S. Bose, M. Bishop, and P. Mohapatra, “Leak- | Linguistics | , vol. 12, pp. 1417–1440, 2024. |  |  |  |  |  |  |  |  |  |  |  |
| semantic: Identifying abnormal sensitive network transmissions in | [60] | J. Yu, X. Lin, Z. Yu, and X. Xing, “ | { | LLM-Fuzzer | } | : Scaling assess- |  |  |  |  |  |  |  |  |
| mobile applications,” in | IEEE INFOCOM 2017-IEEE Conference on | ment of large language model jailbreaks,” in | 33rd USENIX Security |  |  |  |  |  |  |  |  |  |  |  |
| Computer Communications | . | IEEE, 2017, pp. 1–9. | Symposium (USENIX Security 24) | , 2024, pp. 4657–4674. |  |  |  |  |  |  |  |  |  |  |

---

## Page 15

Appendix A.

Prompt Examples

Listing 1: Example- getLastKnownLocation() Call Site

prompt = (

"You are an expert in analyzing Android bytecode instructions. Your task is to trace how sensitive

user data is originated, "

"moved through registers, passed between methods, and possibly reaches sinks (e.g., logging, network,

or storage).\n\n"

"**Chain of Thought Process:**\n\n"

"**1. Understand Context:**\n"

f"- Previous Summary: {previous_summary}\n"

f"- Method Signature: {method.get(’method_signature’, ’’)}\n"

f"- Bytecode Instructions: {instructions_text}\n"

"- Goal: Output JSON with ’Summary’ and ’Next Methods’.\n\n"

"**2. Identify Data Origin:**\n"

"- Look for sensitive API calls (e.g., location, contacts, device ID).\n"

"- Note data type, origin method, and the register it’s stored in.\n"

"- If no origin, check if sensitive data may come via parameters (from ‘Previous Summary‘).\n\n"

"**3. Track Data Storage:**\n"

"- If sensitive data found, trace its flow (via ‘move-*‘, ‘iput-*‘, ‘sput-*‘, etc.).\n\n"

"**4. List Invoked Methods:**\n"

"- Extract full method signatures from invoke-* calls.\n"

"- Note which are passed sensitive registers.\n\n"

"**5. Filter Next Methods:**\n"

"- Exclude: ‘Landroid/*‘, ‘Landroidx/*‘, ‘Lkotlin/*‘.\n"

"- Only keep directly invoked methods.\n"

"- If none left, use ‘[]‘.\n\n"

"**6. Detect Sinks:**\n"

"- Check if sensitive data is passed to sinks like:\n"

" - Logging \n"

" - Network Transmission \n"

" - Storage \n"

"- Return statements are not sinks.\n\n"

"**7. Finalize ’Next Methods’:**\n"

"- If sink is hit with sensitive data, set ‘Next Methods‘ to ‘[]‘.\n"

"- Otherwise, keep filtered method list.\n\n"

"**8. Construct Summary:**\n"

"- Describe origin, movement, and whether sensitive data was passed or leaked.\n"

"- If none observed, state it clearly.\n\n"

"### Output Format:\n"

"‘‘‘json\n"

"{{\n"

’ "Summary": "[Summary of analysis based on the thought process]",\n’

’ "Next Methods": ["FullyQualifiedClass->methodName:(params)returnType"]\n’

"}}\n"

"‘‘‘\n\n"

"- No markdown, code fences, or extra text.\n"

"- Complete method signatures only.\n"

"- JSON must be valid and standalone.\n\n"

"**STRICT RULES:**\n"

"1. Output only the JSON object. No explanation, markdown, or commentary.\n"

"2. Method signatures: full, exact, no guessing, no truncation.\n"

"3. ‘Next Methods = []‘ if a sink is hit.\n"

"4. Do not reuse examples from the prompt.\n"

)

---

## Page 16

| Appendix B. | Appendix C. |
| --- | --- |
| G-Eval Prompt Example | Examples of Missed Data Leaks |

Listing 2: Prompt Used for Evaluation of Model-Generated

Summaries

You are an AI assistant tasked with evaluating

model generated code analysis summary of an

apk file privacy data leakage analysis. You

will be provided with following context to

analysis:

- Ground Truth Summary: The result of manual

expert analysis.

- Model Output: The output from a language model.

Your evaluation should focus on **privacy-related

data flow** and **leakage behavior**. Do not

penalize the model for providing more detail

if it is **factually aligned**.

### Evaluation Dimensions (score each 1-5):

1. Data Type Identification - Does the model

correctly identify sensitive data types (e.g.,

deviceId)?

2. Data Propagation Accuracy - Is the data

movement (source -> transformation -> sink)

accurately described?

3. Sink Function Match - Does the model correctly

identify the final sink(s)?

- Treat Java and bytecode references as

equivalent.

4. Leakage Inference - Does the model correctly

determine if data is leaked?

5. Coherence & Fluency - Is the output

grammatically fluent and logically organized?

Please respond with valid JSON only using:

{

"data_type_identification": <1-5>,

"data_propagation_accuracy": <1-5>,

"sink_function_match": <1-5>,

"leakage_inference": <1-5>,

"coherence_and_fluency": <1-5>

}

G-Eval Metric Mapping

The following mapping were used to convert structured

evaluation scores, derived from privacy dataflow analysis in

mobile applications.

TABLE 9: G-Eval metrics for generated dataflow summary

| G-Eval Metric | Mapping Formula |
| --- | --- |
| Coherence | Coherence & Fluency (from model output) |
| Fluency | Coherence & Fluency (same as above) |
| Consistency | Mean of: Data Type Identification, Propagation |

Accuracy, Leakage Inference

Relevance Mean of: Propagation Accuracy, Sink Function

Match

Listing 3: Example Where AndroByte Misses One of Two

Sinks from the Same Source Method

[

{

"Data Types Collected": [

"Latitude",

"Longitude"

],

"Overall Data Flow": [

{

"Step": "Get location data",

"Source Method": "Lde/ecspride/

FactoryMethods1;->onCreate:(Landroid/os/Bundle

;)V",

"Reasoning": "Retrieves last known

location using system service.",

"Action": "Collected"

},

{

"Step": "Log location data",

"Source Method": "Lde/ecspride/

FactoryMethods1;->onCreate:(Landroid/os/Bundle

;)V",

"Reasoning": "Logs latitude and

longitude using Log.d.",

"Action": "Logged"

}

],

"All Sinks": [

"Landroid/util/Log;->d:(Ljava/lang/

String;Ljava/lang/String;)I"

],

"Complete Data Flow": [

{

"dataflow 1": "Lde/ecspride/

FactoryMethods1;->onCreate:(Landroid/os/Bundle

;)V → Landroid/location/LocationManager;->

getLastKnownLocation:(Ljava/lang/String;)

Landroid/location/Location; → Landroid/util/

Log;->d:(Ljava/lang/String;Ljava/lang/String;)

I",

"Reasoning": "Sensitive location

data is obtained and logged directly in the

same method."

}

],

"Label": [

"leak"

]

}

]

---

## Page 17

Appendix D. Based on our RQ3 results on real world apps, we catego-

Sensitive Data Actions: Summary-Level In- rize identified sinks into three types such as logging, storing,

and transmitting. The heat map in Figure 5 shows that the

sights

Location data emerges as the most frequently handled, with

184 instances of logging, 71 instances of storage, and 127

instances of transmission, highlighting its extensive use and

potential vulnerability in Android applications. In contrast,

actions on User Identifiers are minimal, with 9 instances

of logging, 3 of storage, and no cases of transmission,

indicating better adherence to privacy standards for this

category. Device Details show significant logging and trans-

mission, with storage being less frequent, while Network

Details exhibit moderate handling across all actions. These

findings highlight the importance of securing user location

data, which has the highest percentage of sensitive data flow

across both models.

Figure 5: Sensitive data Actions on data types

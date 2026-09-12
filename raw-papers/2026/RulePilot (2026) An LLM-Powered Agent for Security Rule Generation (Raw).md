---
title: "RulePilot: An LLM-Powered Agent for Security Rule Generation"
author: "Hongtai Wang; Ming Xu; Yanpei Guo; Weili Han; Hoon Wei Lim; Jin Song Dong"
creator: "arXiv GenPDF (tex2pdf:4177c2c)"
pages: 13
---

# RulePilot: An LLM-Powered Agent for Security Rule Generation

> **作者**：Hongtai Wang; Ming Xu; Yanpei Guo; Weili Han; Hoon Wei Lim; Jin Song Dong
> **總頁數**：13 頁

---

## Page 1

RulePilot : An LLM-Powered Agent for Security Rule Generation

| * | *# |  |
| --- | --- | --- |
| Hongtai Wang | Ming Xu | Yanpei Guo |
| National University of Singapore | National University of Singapore | National University of Singapore |
| Singapore, Singapore | Singapore, Singapore | Singapore, Singapore |
| wanghongtai0702@gmail.com | mingxu@nus.edu.sg | guo.yanpei@u.nus.edu |
| Weili Han | Hoon Wei Lim | Jin Song Dong |
| Fudan University | Cyber Special Ops-R&D, NCS Group | National University of Singapore |
| Shanghai, China | Singapore, Singapore | Singapore, Singapore |
| wlhan@fudan.edu.cn | hoonwei.lim@ncs.com.sg | dcsdjs@nus.edu.sg |
| Abstract | ACM Reference Format: |  |

rules becoming an integral part of the intrusion detection life-cycle.

Rule-based detection often identifies malicious logs based on the

knowledge for rule generation. Therefore, automation of rule gen-

eration can result in significant time savings and ease the burden of

rule-related tasks on security engineers. In this paper, we propose

• Security and privacy → Software and application security ;

© 2026 Copyright held by the owner/author(s).

Hongtai Wang * , Ming Xu *#

Song Dong. 2026. RulePilot : An LLM-Powered Agent for Security Rule

Generation. In 2026 IEEE/ACM 48th International Conference on Software

Engineering (ICSE ’26), April 12–18, 2026, Rio de Janeiro, Brazil. ACM, New

1 Introduction

time-consuming, labor-intensive and requires extensive domain

rules need constant updates, increasing maintenance costs. Tools

like MITRE ATT&CK [14] provide a common framework to de-

scribe attack techniques, but translating the structured techniques

QRadar [16], which have their own rule languages. Rules written

an SIEM system. The automation of rule generation and conver-

sion can result in significant time savings and ease the burden of

rule-related tasks on security engineers.

| The real-time demand for system security leads to the detection | , Yanpei Guo, Weili Han, Hoon Wei Lim, and Jin |  |  |
| --- | --- | --- | --- |
| predefined grammar logic, requiring experts with deep domain | York, NY, USA, 13 pages. https://doi.org/10.1145/3744916.3773249 |  |  |
| RulePilot | , which mimics human expertise via LLM-based agent for | Security threats are increasingly a growing concern for both users |  |
| addressing rule-related challenges like rule creation or conversion. | and industrial organizations. The infamous SolarWinds attack [4] |  |  |
| Using | RulePilot | , the security analysts do not need to write down | disrupted supply chains and compromised sensitive data, highlight- |
| the rules following the grammar, instead, they can just provide the | ing the critical need for robust security controls. A recent trend |  |  |
| annotations such as the natural-language-based descriptions of a | in intrusion detection systems relies on the neural-network-based |  |  |
| rule, our | RulePilot | can automatically generate the detection rules | provenance graphs, which have demonstrated notable strength in |
| without more intervention. | RulePilot | is equipped with the interme- | detection performance. However, they face the problems of high |
| diate representation (IR), which abstracts the complexity of config | computational resource cost and long detection latency, hindering |  |  |
| rules into structured, standardized formats, allowing LLMs to focus | their wide practical deployment. In practice, in security detection |  |  |
| on generation rules in a more manageable and consistent way. We | systems, rules [11] are widely used to identify malicious activi- |  |  |
| present a comprehensive evaluation of | RulePilot | in terms of textual | ties and trigger alerts, such as detection rules executed on SIEM |
| similarity and execution success abilities, showcasing | RulePilot | can | (Security Information and Event Management) platforms, which |
| generate high-fidelity rules, outperforming the baseline models by | offer a lightweight and efficient solution to these challenges while |  |  |
| up to 107.4% in textual similarity to ground truths and achieving | maintaining great explanation abilities. |  |  |
| better detection accuracy in real-world execution tests. We perform | However, the high cost of rule creation and the long duration |  |  |
| a case study from our industry collaborators in Singapore, showcas- | of rule maintenance are still problems faced by security organi- |  |  |
| ing that | RulePilot | significantly help junior analysts/general users | zations. Particularly, these detection rules are typically written |
| in the rule creation process. | manually by junior and senior security experts, a process that is |  |  |
| CCS Concepts | knowledge. Furthermore, as attack techniques continue to evolve, |  |  |
| arXiv:2511.12224v1 [cs.CR] 15 Nov 2025 | Keywords | into specific rule configurations requires huge manual efforts. More- |  |
| LLM-based agents, Rule-based Intrusion Detection, Incident Re- | over, modern security organizations can sometimes use different |  |  |
| sponse, AIOps | SIEM platforms such as Splunk [39], Microsoft Sentinel [27], or IBM |  |  |
| * | Both authors contributed equally to the paper, ordered alphabetically. | for one platform cannot directly work on another, creating a cross- |  |
| # | Corresponding author. | platform compatibility problem when an organization migrates |  |
| This work is licensed under a Creative Commons Attribution 4.0 International License. | The recent breakthrough of Large Language Models (LLMs), par- |  |  |
| ICSE ’26, Rio de Janeiro, Brazil | ticularly in code generation [15, 21, 42, 47], text-to-SQL [37] and |  |  |
| ACM ISBN 979-8-4007-2025-3/26/04 | binary malware analysis [48, 52] with generative models like the |  |  |
| https://doi.org/10.1145/3744916.3773249 | GPT series, open new opportunities for automated security rule |  |  |

---

## Page 2

| ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil | Hongtai Wang | * | , Ming Xu | *# | , Yanpei Guo, Weili Han, Hoon Wei Lim, and Jin Song Dong |
| --- | --- | --- | --- | --- | --- |
| generation and conversion. Unfortunately, compared to code/SQL | Processing Language (SPL) and Microsoft Sentinel Kusto Query |  |  |  |  |
| generation, the challenge of generating security configurations | Language (KQL). |  |  |  |  |
| lies in the nuanced and dynamic nature inherent in SIEM-specific | We evaluate | RulePilot | upon objective similarity for textual align- |  |  |
| rules. Code/SQL often follows well-defined syntax and logical struc- | ment with ground truth rules [40] and semantic evaluator for assess- |  |  |  |  |
| tures, while rule configurations are highly domain-specific, system- | ing logical and functional correctness. Results show that | RulePilot |  |  |  |
| dependent, and lack standardized formats. The rule configurations | consistently improves both textual similarity and semantic accu- |  |  |  |  |
| require a deep understanding of systems’ behaviors and environ- | racy, outperforming standalone LLMs by up to 107.4% in textual |  |  |  |  |
| ment, precise tuning of parameters, dependencies, and iterative | similarity. We conduct a field study by executing the generated rules |  |  |  |  |
| corrections, which can vary significantly across SIEM systems. In- | in a realistic Splunk environment, evaluating their execution suc- |  |  |  |  |
| formally speaking, a junior programmer can write redundant but | cess in detecting suspicious activities. The results demonstrate that |  |  |  |  |
| correct code, however, he/she may struggle to figure out a correct | RulePilot | successfully captures the majority of suspicious logs by up |  |  |  |
| SIEM-specific rule constraint. Several works [35, 44] explored the | to 1.00 F1 score, validating its practical applicability in real-world |  |  |  |  |
| generation of simple detection YAML rules like Sigma, falling short | threat detection scenarios. Our evaluation yields intriguing insights |  |  |  |  |
| in addressing the more complex and functional challenges specific | into the capabilities and limitations of LLMs in rule generation. We |  |  |  |  |
| to SIEM systems due to the following challenges. | discover that LLMs show proficiency in understanding high-level |  |  |  |  |

• Non-standardized format: The rule configurations are highly

domain-specific and lack standardized representations. A stan-

dalone LLM typically lacks precise knowledge and cannot simulate

human thoughts to break down the complex rule generation into

smaller pipelines. To address this, we design an intermediate repre-

sentation (IR) that can serve as a bridge between high-level require-

ments and low-level configuration file details. An IR abstracts the

complexity of rule configurations into a structured, standardized

format that captures essential parameters, and relationships, allow-

In this paper, for the first time, we propose RulePilot , which is

an LLM-powered agent facilitating a series of practical scenarios

rity analysts do not need to write rules following a specific gram-

mar. Instead, they can simply provide annotations, such as rule

descriptions in natural language. With this input, our RulePilot

can automatically generate detection rules without requiring any

further intervention. Usually, the descriptions can be divided into

preconditions like a rule annotations or the attack types provided

by experts. We tailor our workflow to Splunk SIEM grammars. 2)

Furthermore, when security analysts update or migrate their SIEM

threat descriptions and generating corresponding rules, however,

we find that LLMs have difficulty in maintaining field mappings

and condition handling, which necessitates human verification for

checking the final results, ensuring the generated rule functions

correctly. We perform a case study from our industry partners, and

show that RulePilot significantly facilitates the rule generation of

junior analysts/general users in terms of time used, rule quality

including the syntax validity and logical alignment.

We summarize our contributions as follows.

open-source all code in 2 .

2.1 Rule-based Anomaly Detection

Modern anomaly detection systems like Security Information and

Event Management (SIEM) [11, 45] typically rely on detection rules

to identify potential intrusions, which are widely used due to their

lightweight overhead and great explanation abilities. The widely-

used rules can be typically classified into the general Sigma and

| ing LLMs to focus on generating configurations in a manageable | • | We propose a novel workflow | RulePilot | to address SIEM-specific |
| --- | --- | --- | --- | --- |
| and consistent way. The designed IR should be capable of han- | rule generation and conversion challenges. Our designed imme- |  |  |  |
| dling the SIEM-specific cases like nested operators, vendor-specific | diate representation and reflection modular go beyond general IR |  |  |  |
| syntax, reducing ambiguity and improving accuracy. | and reflection mechanisms, effectively covering the SIEM-specific |  |  |  |
| • | Iterative correction: | The initially generated rules might be | functions and edge cases such as nested operators and logical |  |
| semantically and syntactically incorrect, or logically-nonaligned. | consistency, making the process more robust and scalable. |  |  |  |
| To resolve this, we introduce the reflection functions, identifying | • | We tailor our | RulePilot | to Splunk SIEM system, analyzing the |
| the potential mistakes upon each step, and refining the identified | grammars and environments specific to Splunk, seamlessly inte- |  |  |  |
| weakness to optimize the semantic and syntactic gaps. Beyond that, | grating with Splunk for intelligent and efficient rule execution. |  |  |  |
| our reflection supports logical consistency, rule-field coverage, and | To the best of our knowledge, this is the first, end-to-end and |  |  |  |
| the live execution viability, enabling the robust and scalable rule | real-time agentic framework for SIEM-rule creation. |  |  |  |
| generation. | • | We conduct a comprehensive evaluation of | RulePilot | , employ- |
| • | System dependence: | A sound rule should be able to interact | ing models like GPT-4o, DeepSeek-V3, and LlaMa-3. | RulePilot |
| with the live SIEM systems while existing LLMs fall short into | outperforms the baseline models by up to 107.4% in textual simi- |  |  |  |
| autonomously and independently use tools like external SIEM ven- | larity to ground truths and achieves better detection accuracy in |  |  |  |
| dor’s grammar checks, feedback from live SIEM vendor’s APIs, or | real-world Splunk execution tests. |  |  |  |
| rule-testing frameworks. We integrate the live Splunk [39] SIEM | With its structured reasoning and automation capabilities, | RulePilot |  |  |
| with LLMs, facilitating validation, optimization, and adaptation of | is poised to become an essential tool for security analysts in rule- |  |  |  |
| configurations across systems and environments. | relevant tasks. We release all the used datasets in the link | 1 | and |  |
| on rule-based detection autonomously: 1) Using | RulePilot | , secu- | 2 | Background and Motivation |
| systems, they need the conversion function between the different | 1 | https://sites.google.com/view/rulepilot/dataset |  |  |
| SIEM vendors. | RulePilot | supports the conversion between Splunk | 2 | https://github.com/LLM4SOC-Topic/RulePilot |

---

## Page 3

| RulePilot | : An LLM-Powered Agent for Security Rule Generation | ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil |  |
| --- | --- | --- | --- |
| the SIEM-specific rules. Sigma is a generic and open signature for- | This ensures that rules generated by | RulePilot | remain reusable, min- |
| mat for SIEM systems, allowing for flexible rules in YAML format | imizing manual effort and streamlining future migrations. Note |  |  |
| that can be translated into multiple SIEM vendors. Despite their | that | RulePilot | is designed to generate rules autonomously with- |
| compatibility with any SIEM vendor, Sigma rules primarily rely on | out human intervention. We acknowledge that human verification |  |  |
| single-pattern matching using regular expressions. They lack sup- | remains essential for final deployment. In practice, human opera- |  |  |
| port for complex queries, such as SQL-style aggregations, and are | tors validate the generated rules to ensure their correctness and |  |  |
| unable to execute calculations including statistical analysis or time- | effectiveness. The junior operator here is expected to be familiar |  |  |
| window-based computations in SIEM vendors. These limitations | with the SIEM environments. Compared to manual rule creation, |  |  |
| often result in failures to detect sophisticated attacks involving | the human role here focuses on validation, eliminating the need to |  |  |
| a series of events or cycles. In contrast, SIEM-specific rules can | master complex rule grammars. |  |  |

bridge this gap by incorporating customized conditions with condi-

tional statements and leveraging advanced functions. Consider a

scenario where an attacker attempts to exfiltrate sensitive data by

downloading multiple ".zip" files from a server. A typical Sigma rule

detects this behavior through pattern matching in log fields, such

as identifying ".zip" file requests in URI queries, which relies solely

vendor Splunk [39] as an example, a Splunk-specific rule [40, 41]

shown in Listing 1.

| where count > 5 AND user_agent !=" Mozilla /5.0 ( friendly -

| eval message =" Potential data exfiltration detected : " .

src_ip . " downloading " . count . " ZIP files "

| table _time , src_ip , uri_query , user_agent , count ,

message

As shown in Figure 1, existing methods require analysts to write

rules manually with an attack description. There are two types of

analysts: senior analysts and junior analysts. A senior analyst has

rich experience and years of writing rules. They can complete the

task in a short time, and the rules are of good quality. However,

the cost is very high due to training and salaries. A junior analyst

may lack experience. They take a long time to write rules, and the

results may not be good. This motivates the use of a RulePilot based

on LLMs. RulePilot assists in writing rules, saving time, reducing

analysts for somewhat condition handling. Companies often en-

counter system migration challenges, such as adapting validated

Requirement

Time Time Time

Convert

High Cost Low Cost Low Cost

of senior experts.

2.3 LLM-Based Agents

based toolkit designed to automate the creation of YARA rules.

the customized SIEM-specific rules. Applying LLM-based agents

to generate complex detection rules, such as Splunk-specific rules,

faces several significant challenges: 1) deep domain knowledge re-

quirement. This involves meticulously analyzing rule structures

step by step and crafting modular designs to guide the LLM in mak-

ing precise plans and reasoned decisions. and 2) workflow design

and live SIEM integration. Developing an agent workflow capable

of handling multi-step reasoning and integrating the SIEM systems

is equally demanding.

3.1 Workflow Design

| on string-based detection, lacking contextual awareness and deeper | Senior Analyst | Junior Analyst | Junior Analyst | RulePilot |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| behavioral analysis. As a comparison, take the widely-used SIEM | Short | Long | Short |  |  |  |  |  |
| can implement the detection with more advanced functionality | Rule |  |  |  |  |  |  |  |
| index = web_logs | Good Results | Poor Results | Good Results |  |  |  |  |  |
| \| | search | uri_query ="*. zip " | Figure 1: Motivation scenario [6, 18]: By combining with |  |  |  |  |  |
| \| | stats | count | BY | src_ip , | uri_query , | user_agent | RulePilot | , junior analysts can generate concise detection |
| bot )" | rules and conversions, significantly reducing the workload |  |  |  |  |  |  |  |
| Listing 1: A splunk rule for detection of ZIP file downloads. | An agent can be broadly defined as an autonomous entity that per- |  |  |  |  |  |  |  |
| This Splunk rule can track activity over time, filter out events us- | ceives its environment, makes decisions based on its goals, and takes |  |  |  |  |  |  |  |
| ing the conditions (such as removing known bots), and generate | actions to affect its surroundings[33]. These features are inspired |  |  |  |  |  |  |  |
| meaningful alerts, making it far more effective in identifying attack | by human cognition and allow agents to behave consistently and ef- |  |  |  |  |  |  |  |
| behaviors. We commit to generating such SIEM-specific rules using | fectively in dynamic, complex environments [46]. Researchers have |  |  |  |  |  |  |  |
| our | RulePilot | . Among the SIEM vendors, we target Splunk vendors | been exploring machine learning techniques to automate aspects |  |  |  |  |  |
| as Splunk [39, 40] is widely used by organizations in practice in | of rule generation in cybersecurity. For example, Raff et al. [30] |  |  |  |  |  |  |  |
| literature and our professional experience. Additionally, we con- | introduced AutoYara, a tool that utilizes biclustering algorithms |  |  |  |  |  |  |  |
| sider the problem of rule conversion when Splunk SIEM sometimes | to automatically generate YARA rules for malware detection. In |  |  |  |  |  |  |  |
| should be migrated into another SIEM like Microsoft Sentinel [27]. | another study, Saxe [34] developed YaraML, a machine learning- |  |  |  |  |  |  |  |
| 2.2 | Motivation Scenarios | However, they always focus on generic YARA rules, while ignoring |  |  |  |  |  |  |
| costs, and achieving better results, only with the help of junior | 3 | RulePilot | : Methodology |  |  |  |  |  |
| rules to a new SIEM platform. | RulePilot | addresses this by offering a | Overview. | As shown in Figure 2, | RulePilot | consists of three key |  |  |
| rule conversion function, enabling seamless rule adaptation across | components: Chain of Thought (CoT) reasoning, Intermediate Rep- |  |  |  |  |  |  |  |
| different SIEM systems (e.g., from Splunk to Microsoft Sentinel). | resentation (IR), and Reflection & Iterative Optimization. Given an |  |  |  |  |  |  |  |

---

## Page 4

ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil Hongtai Wang * , Ming Xu *# , Yanpei Guo, Weili Han, Hoon Wei Lim, and Jin Song Dong

�

the execution of suspicious

processes on systems identified Decision � 2 � 4 � 6 ...

Splunk data model

"Endpoint.Processes" to search

"wget", "service", and "curl". This

these processes are often used

by attackers for reconnaissance,

persistence, or data exfiltration. If � 4 � 4 � 4

lead to data theft, deployment of

6

ransomware attacks. Immediate

investigation is required to

wget, service, and curl | MODULES

on systems identified as

web servers.

CoT Stage IR Stage

Given a rule generation request 𝑅 , RulePilot first decomposes it

into a sequence of structured reasoning steps 𝑃 = { 𝑝 1 , 𝑝 2 , ..., 𝑝 𝑛 } .

The decomposition follows these two stages: (1) Step Selection:

The model selects relevant steps from the set of predefined steps

above, which cover the comprehensive aspects of rule generation.

(2) Stepwise Execution: The model answers each subproblem in se-

quence, using the output of 𝑝 𝑖 as contextual input for 𝑝 𝑖 + 1 , ensuring

a gradual and structured rule refinement process.

Intermediate Representation. A well-designed IR abstraction

provides a clear and structured way to express rule intention. SIEM-

specific rule logic is inherently complex, requiring structured filter-

ing, aggregation, and anomaly detection across various log sources.

� 풓� 

Processes.process IN ("whoami", "ping", "iptables",

"wget", "service", "curl") by Processes.process_name,

Processes.dest, Processes.user

| rename Processes.process_name as process,

| table firstTime, lastTime, host, user, process, count 'extend' .

{threat_relevance = "High"} "Mozilla/5.0 (Linux; Android 10; Mobile)

AppleWebKit/537.36 (KHTML, like Gecko)

Chrome/99.0.4758.102 Safari/537.36"}

Reflection Stage

where C is the rule construction function that synthesizes the

intermediate analyses 𝑂 and the IR 𝐼 into an executable rule.

Reflection and Iterative Optimization. The optimization process

incorporates a dynamic iterative mechanism, starting with an auto-

mated reflection function Φ ( 𝑅 𝑟𝑎𝑤 ) , which analyzes the generated

rule to identify logical inconsistencies, knowledge gaps, or syn-

tax errors. After each iteration, the RulePilot autonomously selects

and invokes appropriate tools to address deficiencies. If the system

detects unresolved issues, it triggers another refinement cycle, iter-

ating until the rule is logically coherent, semantically accurate, and

syntactically valid.

𝑆 = { 𝑠

or Microsoft KQL.

• Execution Validity ( 𝑠 𝑒𝑣 ): Ensures that the rule is structured for ef-

ficient query execution without excessive computational overhead.

| The following analytic detects | 1 | � | 3 | � | 5 | Feedback |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| as web servers. It leverages the | Generation | Tools |  |  |  |  |  |  |  |
| for specific process names such | � | 1 | � | 1 | � | 1 | \| tstats summariesonly=true count from | ... |  |
| as "whoami", "ping", "iptables", | datamodel=Endpoint.Processes | Semantic | SIEM API | Grammar |  |  |  |  |  |
| activity is significant because | � | 2 | � | 2 | � | 2 | where Processes.dest_category="web_server" AND | Refine | Check |
| confirmed malicious, this could | Processes.dest as host, Processes.user as user | HTTP 400 Bad Request -- |  |  |  |  |  |  |  |
| additional malware, or even | � | 6 | � | 6 | � | \| | extend | alert="Suspicious process executed" | Unknown search command |
| determine the legitimacy of the | { | "firstTime": "2025-03-12T15:45:32Z", |  |  |  |  |  |  |  |
| activity and mitigate potential | What are the | Suspicious activity is | "lastTime": "2025-03-12T15:48:10Z", |  |  |  |  |  |  |
| threats. | specific conditions | defined as the | execution | FILTER | "host": "webserver-02.company.com", |  |  |  |  |
| that define | of processes | like | \| | PARAMS | {process_name IN ["whoami", "ping", "iptables", | "user": "nginx", "process": "wget | ", "count": 3, |  |  |
| suspicious activity? | whoami, ping, iptables, | "wget", "service", "curl"], system_role = "web_server"} | "callerIpAddress": "203.0.113.45", "userAgent": |  |  |  |  |  |  |

Figure 2: Overview of RulePilot , where RulePilot incorporates the Chain-of-Thought (CoT), Intermediate Representation (IR),

and Reflection components. Given the NLP-based input requirements, RulePilot generates SIEM-specific rules that can be

directly executed in the SIEM to detect malicious logs and trigger alerts (i.e., the malicious log).

| initial rule generation request | 𝑅 | , | RulePilot | applies Least-to-Most | Specifically, each reasoning step corresponds to one or more |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Prompting (LMP) [53] to incrementally decompose rule generation | IR statements, with each IR statement representing a single pro- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| into a structured sequence of reasoning steps | 𝑃 | . Each step produces | cessing unit (pipe) in the rule. Given an input rule request de- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| an intermediate representation that encodes its core logic, and once | scription, the CoT process generates a sequence of reasoning steps |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| all steps are processed, these representations are aggregated to | 𝑃 | = | { | 𝑝 | 1 | , 𝑝 | 2 | , ..., 𝑝 | 𝑛 | } | , where each step | 𝑝 | 𝑖 | maps to an IR component | 𝐼 | 𝑖 | . |
| form an initial rule | 𝑅 | 𝑟𝑎𝑤 | . The rule then undergoes reflection and | Formally, this can be represented as: |  |  |  |  |  |  |  |  |  |  |  |  |  |
| iterative optimization, where weaknesses are identified and refined | Ø | 𝑛 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| through reasoning adjustments, syntax validation, and execution- | 𝐼 | = | { | 𝐼 | 1 | , 𝐼 | 2 | , ..., 𝐼 | 𝑛 | } | = | T ( | 𝑜 | 𝑝 | 𝑖 | ) |  |
| based feedback. This structured analyze-generate-reflect-optimize | 𝑖 | = | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cycle ensures that the final rule | 𝑅 | 𝑓 𝑖𝑛𝑎𝑙 | is both logically sound and | where | T | is the transformation function that maps each intermediate |  |  |  |  |  |  |  |  |  |  |  |
| execution-efficient. | analysis output | 𝑜 | 𝑝 | 𝑖 | to an IR | 𝐼 | 𝑖 | . The final IR set | 𝐼 | is the union of all |  |  |  |  |  |  |  |
| Chain of Thought Reasoning. | The predefined CoT reasoning | individual IR components generated through this mapping process. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| steps that | RulePilot | can select and execute are below: | Once the full set of IR components | 𝐼 | has been constructed, the |  |  |  |  |  |  |  |  |  |  |  |  |
| ○ | 1 | Interpreting the security objectives, | ○ | 2 | Identifying data/log sources, | initial raw rule | 𝑅 | 𝑟𝑎𝑤 | is generated by integrating both the semantic |  |  |  |  |  |  |  |  |
| ○ | 3 | Defining initial filters/conditions, | ○ | 4 | Extracting relevant fields, | ○ | 5 | insights from | 𝑜 | 𝑝 | 𝑖 | and the structured transformations from | 𝐼 | 𝑖 | . |  |  |
| Performing data aggregation, | ○ | 6 | Optimizing the rule | 𝑅 | 𝑟𝑎𝑤 | = | C( | 𝑂, 𝐼 | ) |  |  |  |  |  |  |  |  |
| The syntax of SIEM rule languages, such as Splunk Processing Lan- | 𝑙𝑐 | , 𝑠 | 𝑠𝑐 | , 𝑠 | 𝑒𝑣 | } | = | Φ | ( | 𝑅 | 𝑟𝑎𝑤 | ) |  |  |  |  |  |
| guage (SPL) and Microsoft Sentinel Kusto Query Language (KQL), is | where | 𝑆 | represents the set of identified issues: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| highly complex, making direct generation challenging. By incorpo- | • | Logical Consistency ( | 𝑠 | 𝑙𝑐 | ): Verifies whether all filtering, aggrega- |  |  |  |  |  |  |  |  |  |  |  |  |
| rating an intermediate representation, | RulePilot | enables the model | tion, and correlation steps align with the intended detection logic. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| to prioritize semantic logic over syntactic details, streamlining the | • | Syntax Correctness ( | 𝑠 | 𝑠𝑐 | ): Confirms that the rule adheres to the |  |  |  |  |  |  |  |  |  |  |  |  |
| reasoning process and improving rule generation accuracy. | syntax requirements of the target SIEM system, such as Splunk SPL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 5

| RulePilot | : An LLM-Powered Agent for Security Rule Generation | ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil |  |
| --- | --- | --- | --- |
| 3.2 | Detailed Construction | rule retrieves logs from relevant data sources, preventing inefficien- |  |
| Here, we show how to tailor our workflow to the Splunk SIEM, | cies caused by querying unrelated logs. Similarly, including a time |  |  |
| generating SPL rules. | constraint like | earliest=-15m latest=now | helps narrow the search |
| Chain of Thought Reasoning. | We keep the core CoT workflow | scope, significantly improving query speed. |  |
| unchanged, and incorporate additional Splunk-adapted design el- | • | 𝑀𝑂𝐷𝑈 𝐿𝐸𝑆 | introduces functional annotations that enrich the |
| ements to improve log source selection, syntax correctness, and | interpretation of a rule, improving its flexibility, readability, and |  |  |
| execution efficiency. A detailed example of the CoT prompt struc- | adaptability during the transformation into an executable query. |  |  |
| ture is shown in Table 1. We open-source the prompts for LLMs | Unlike | 𝑃𝐴𝑅𝐴𝑀𝑆 | , which strictly define the necessary elements for |
| corresponding to each function of these processes on the web- | rule execution, | 𝑀𝑂𝐷𝑈 𝐿𝐸𝑆 | describe the intended logic and ana- |
| site [32]. Our prompt strategy is motivated by empirical tuning and | lytical operations that should be applied to the retrieved data. For |  |  |
| expert insights, effectively mimicking expert-level expertise into | example, a module may specify "track user behavior across sessions" |  |  |
| the agent’s behavior. We used components of Identity, Instructions, | or "identify repeated failed login attempts", helping to capture the |  |  |
| Examples, and Context because they reflect how SIEM experts re- | intent behind the rule rather than just its execution details. |  |  |
| trieve historical cases during manual rule construction. We also | Table 2 shows an example on how our IR corresponds to an exe- |  |  |
| guide with DOs and DON’Ts, helping the model understand both | cutable Splunk query, where the IR abstraction defines the detection |  |  |
| what to do and what to avoid, based on OpenAI’s official guide | 3 | . | logic in a structured and interpretable way, with its SPL counterpart |

CoT Prompt Template

You are a security analyst at a cybersecurity company, special-

detection.

Task: <Iterate through the tasks in the Task List>

Instruction: <Specific Guidance such as possible keywords>

Example Input: <Provide an example rule description>

Task List

○ 2 Determine necessary log fields

○ 3 Define efficient filtering conditions

○ 5 Perform aggregations and anomaly detection

○ 6 Optimize query execution and validate syntax

Intermediate Representation. We create the IR structure tailored

where:

• 𝐾𝐸𝑌𝑊 𝑂𝑅𝐷 represents the core function of each rule step, in-

https://platform.openai.com/docs/guides/text?api-mode=chat

represents the actual execution in Splunk. The 𝐹 𝐼𝐿𝑇 𝐸𝑅 specifies

𝑀𝑂𝐷𝑈 𝐿𝐸𝑆 encapsulates the detection intent, guiding how the rule

should process events.

IR Example

FILTER

| PARAMS

30m}

| MODULES

Corresponding Splunk SPL Pipe

30m

| stats count by src_ip

| where count >10

plicit support. For nested operators, which are commonly used in

simple constructs (e.g., eval, match, where), we allow controlled

| AGGREGATE | stats, timechart, eventstats, tstats | 1872 |
| --- | --- | --- |
| LOOKUP | lookup,inputlookup,outputlookup | 315 |
| APPEND | append, union, appendpipe | 46 |
| APPLY | apply, fit | 24 |

| Table 1: Structure of the Prompt Template | where to retrieve logs, | 𝑃𝐴𝑅𝐴𝑀𝑆 | ensures correct data scoping and |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| izing in writing and optimizing Splunk rules (SPL) for threat | Table 2: Example for IR Statement to a Splunk Rule Pipe |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Example Output: <Corresponding SPL detection rule> | {index="auth_logs", source="WinEventLog:Security", earliest=- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ○ | 1 | Map security objectives to Splunk event sources | {"Aggregate login attempts", "Detect brute force login attempts"} |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ○ | 4 | Apply field extractions and transformations | index="auth_logs" source="WinEventLog:Security" earliest=- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| to Splunk SPL, whose structure follows a three-part format below. | To address SIEM-specific edge cases, we design the IR with ex- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| < | 𝐾𝐸𝑌𝑊 𝑂𝑅𝐷 | > | \| | 𝑃𝐴𝑅𝐴𝑀𝑆 | { | 𝑘 | 𝑖 | = | 𝑣 | 𝑖 | }\| | 𝑀𝑂𝐷𝑈 𝐿𝐸𝑆 | { | 𝑚 | 𝑗 | } | filter and transformation logic, we incorporate two strategies: For |
| cluding filtering logs, extracting fields, performing aggregations, | Table 3: IR keywords along with their SPL Commands. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| or applying transformations. These IR keywords are summarized | Keyword | SPL Command | Frequency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| based on an extensive analysis of open-source Splunk rule sets and | FILTER | search, where, eval, match | 3129 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| proprietary rules from industry collaborators. Each | 𝐾𝐸𝑌𝑊 𝑂𝑅𝐷 | EXTRACT | rex, spath, extract, kv | 2063 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| corresponds to one or more SPL commands. Table 3 presents the | OUTPUT | table, fields,outputlookup, return | 1609 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| distribution and frequency of the 15 predefined IR keywords in SPL, | TRANSFORM | eval, replace, convert, fillnull | 1015 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| along with their associated SPL commands. | RENAME | rename | 802 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| • | 𝑃𝐴𝑅𝐴𝑀𝑆 | serves as the core configuration of the rule, defin- | BUCKET | bin, bucket | 91 |  |  |  |  |  |  |  |  |  |  |  |  |
| ing mandatory elements such as log sources, filtering conditions, | JOIN | join, appendcols, transaction | 83 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and time constraints. These parameters ensure that the rule is | FILL | fillnull, coalesce, replace | 75 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| executed within the correct context. For example, specifying | in- | SORT | sort, reverse | 38 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| dex="auth_logs" source="WinEventLog:Security" | ensures that the | DEDUP | dedup, uniq | 28 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | DEBUG | noop, logtrace, dump, sendemail | 17 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 6

| ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil | Hongtai Wang | * | , Ming Xu | *# | , Yanpei Guo, Weili Han, Hoon Wei Lim, and Jin Song Dong |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nesting within a single IR statement; for more complex expres- | As shown in Algorithm 1, the Rule Conversion follows a struc- |  |  |  |  |  |  |  |  |  |  |  |
| sions involving multi-layer joins or condition chaining, we enforce | tured multi-step approach, beginning by segmenting the input rule |  |  |  |  |  |  |  |  |  |  |  |
| decomposition into multiple atomic IR statements to preserve in- | into individual pipes, and then breaking down a complex task into |  |  |  |  |  |  |  |  |  |  |  |
| terpretability and reduce error propagation during transformation. | smaller, more manageable units. However, this breakdown may |  |  |  |  |  |  |  |  |  |  |  |
| To accommodate SIEM-specific syntax variations of multiple | cause a loss of contextual dependencies between pipes, so an LLM- |  |  |  |  |  |  |  |  |  |  |  |
| SIEMs, our IR incorporates a pluggable keyword dictionary archi- | based function extraction module is introduced to retrieve each |  |  |  |  |  |  |  |  |  |  |  |
| tecture. For each target SIEM system (e.g., Splunk SPL, Microsoft | pipe’s purpose and variable mappings, ensuring coherence in later |  |  |  |  |  |  |  |  |  |  |  |
| KQL), we can curate and maintain a dedicated dictionary of IR | stages. Once the semantic information is extracted, the system con- |  |  |  |  |  |  |  |  |  |  |  |
| keywords and associated translation templates derived from em- | verts each pipe sequentially, allowing previously processed pipes |  |  |  |  |  |  |  |  |  |  |  |
| pirical rule corpora and vendor documentation. This allows the | to provide contextual support. |  |  |  |  |  |  |  |  |  |  |  |
| IR-to-query compiler to flexibly adapt the output semantics and | To further improve accuracy, we incorporate a Retrieval-Augmented |  |  |  |  |  |  |  |  |  |  |  |
| syntactic form of different SIEMs. | Generation (RAG) [19] mechanism that dynamically maps key- |  |  |  |  |  |  |  |  |  |  |  |
| Reflection and Iterative Optimization. | Different from LLM- | words and functions from the source SIEM to their equivalents in |  |  |  |  |  |  |  |  |  |  |
| based self-debugging [13, 43] that typically relies on prompting- | the target SIEM. The RAG knowledge base is bootstrapped from |  |  |  |  |  |  |  |  |  |  |  |
| based re-generation conditioned on observed errors or exceptions, | Microsoft’s official migration documentation [7], which provides |  |  |  |  |  |  |  |  |  |  |  |
| our reflection adopts a scoring-based multi-layered mechanism. | detailed mappings between Splunk detection rules and their KQL |  |  |  |  |  |  |  |  |  |  |  |
| This enables the system to iteratively reconstruct faulty rule com- | counterparts. From this corpus, we extract every | <SPL command, |  |  |  |  |  |  |  |  |  |  |
| ponents at both the IR and final SPL levels, addressing deeper is- | KQL operator, usage snippet> | triple, normalise aliases (e.g., | rex |  |  |  |  |  |  |  |  |  |
| sues such as semantic gaps, abstraction mismatches, logical in- | ↔ | extract | ) and build a key-value mapping database that aligns |  |  |  |  |  |  |  |  |  |
| consistencies, field coverage, and execution viability, rather than | functionally equivalent operations across the two SIEMs. Each SPL |  |  |  |  |  |  |  |  |  |  |  |
| merely rewriting surface text. Our reflection mechanism integrates | command string and its descriptive context are embedded with the |  |  |  |  |  |  |  |  |  |  |  |
| semantic-level diagnostics, real execution feedback via selective | text-embedding-ada-002 | [3]. During conversion, every pipe is |  |  |  |  |  |  |  |  |  |  |
| modules, and a scoring-based evaluation to further analyze the | first tokenised into | <verb, args, fields> | tuples. The verb plus sur- |  |  |  |  |  |  |  |  |  |
| logical consistency, field coverage, and execution viability using | rounding comments are embedded on-the-fly, and a top- | 𝑘 | (default |  |  |  |  |  |  |  |  |  |
| a scoring-based evaluation ( | 𝑠 | 𝑙𝑐 | , | 𝑠 | 𝑠𝑐 | , | 𝑠 | 𝑒𝑣 | ), and selectively invokes | 𝑘 | = | 10) vector search is issued. Candidates with cosine similarity |
| CoT-based refinement and SIEM-integrated validation routines. | above a threshold (i.e., 0.82 used) are retained and re-ranked with a |  |  |  |  |  |  |  |  |  |  |  |
| Specifically, | RulePilot | first performs syntax validation using | BM25 [31] lexical score to favour exact-string matches. If the SPL |  |  |  |  |  |  |  |  |  |
| Splunklib’s dry-run mode [38], which allows the system to check | command has a high-confidence match, the retrieved KQL oper- |  |  |  |  |  |  |  |  |  |  |  |
| for syntax errors without executing the query. Second, | RulePilot | ator (and an example usage) is attached to the LLM prompt as a |  |  |  |  |  |  |  |  |  |  |
| dynamically invokes a set of predefined optimization modules to | structured “conversion hint”. This retrieval-augmented approach |  |  |  |  |  |  |  |  |  |  |  |
| address identified logical/structural inconsistencies. If | Φ | ( | 𝑅 | 𝑟𝑎𝑤 | ) | de- | ensures that the LLM does not solely rely on pre-trained knowl- |  |  |  |  |  |
| tects any of | { | 𝑠 | 𝑙𝑐 | , 𝑠 | 𝑠𝑐 | , 𝑠 | 𝑒𝑣 | } | , indicating logical inconsistencies, struc- | edge but is instead guided by vendor-specific best practices and |  |  |
| tural violations, or execution failures, the system applies targeted | real-world rule patterns. |  |  |  |  |  |  |  |  |  |  |  |

refinements through two steps:

This produces an updated intermediate rule 𝑅 ′

𝑟𝑎𝑤 , defined as:

𝑅 ′

𝑟𝑎𝑤 = 𝑀 𝐶𝑜𝑇 ( 𝑅 𝑟𝑎𝑤 , 𝑠 𝑙𝑐 )

𝑆𝑝𝑙𝑢𝑛𝑘 ): RulePilot integrates with

cuted via Splunk’s API, retrieving real log data. If the results deviate

the SPL by adjusting filters, modifying conditions, or restructuring

query logic based on execution feedback.

𝑅 𝑓 𝑖𝑛𝑎𝑙 = 𝑀 𝑆𝑝𝑙𝑢𝑛𝑘 ( 𝑅 ′

𝑟𝑎𝑤 , 𝑆 )

3.3 Rule Conversion

To ensure the interoperability and adaptability of RulePilot across

different SIEM platforms, we implement a Rule Conversion Module

that translates rules from one SIEM vendor (e.g., Splunk SPL) into

1: Step 1: Pipe Segmentation

2: Split 𝑅 𝐴 into a sequence of pipes: 𝑃 = { 𝑝 1 , 𝑝 2 , ..., 𝑝 𝑛 }

3: Step 2: Function Extraction

4: for each pipe 𝑝 𝑖 ∈ 𝑃 do

5: ( 𝑓 𝑖 , 𝑖𝑛 𝑖 , 𝑜𝑢𝑡 𝑖 ) ← ExtractFunctionInfo ( 𝑝

6: end for

8: for each pipe 𝑝 𝑖 ∈ 𝑃 do

9: 𝑃 prior ← GetPriorPipes ( 𝑝 𝑖 , 𝑃 )

11: 𝑝 ′

𝑖 ← ConvertPipe ( 𝑝 𝑖 , 𝑖𝑛 𝑖 , 𝑜𝑢𝑡 𝑖 , 𝑃 prior , 𝐾 𝑖 )

12: 𝑃 ′

← 𝑃 ′ ∪ { 𝑝 ′

𝑖 }

13: end for

14: Step 4: Assemble Converted Rule

15: 𝑅 𝐵 ← AssembleRule ( 𝑃 ′ )

16: return 𝑅 𝐵

4 Evaluation

| (1) CoT-Based Refinement Modules ( | 𝑀 | 𝐶𝑜𝑇 | ): The system revisits | Algorithm 1 | Rule Conversion from SIEM Vendor A to B |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| earlier CoT reasoning steps and regenerates the affected IR state- | Require: | Rule | 𝑅 | 𝐴 | from SIEM Vendor A, Target SIEM Vendor B |  |  |  |  |  |  |  |  |  |  |
| ments, refining the rule logic and improving structural coherence. | Ensure: | Converted rule | 𝑅 | 𝐵 | for SIEM Vendor B |  |  |  |  |  |  |  |  |  |  |
| (2) Rule Refinement Modules ( | 𝑀 | 𝑖 | ) |  |  |  |  |  |  |  |  |  |  |  |  |
| live Splunk’s validation and execution environment. The rule is exe- | 7: | Step 3: Context-Aware Pipe Conversion |  |  |  |  |  |  |  |  |  |  |  |  |  |
| from the intended detection objective, | RulePilot | iteratively refines | 10: | 𝐾 | 𝑖 | ← | RetrieveKeyword | ( | 𝑝 | 𝑖 | , | Vendor A | , | Vendor B | ) |
| another (e.g., Microsoft KQL). This conversion process is designed | In this section, we aim to evaluate the following research questions. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| to preserve the logical intent of the original rule while adapting it | • | RQ1- | Accuracy | : How effective is | RulePilot | in generating SIEM- |  |  |  |  |  |  |  |  |  |
| to the syntax, function names, and query structures of the target | specific detection rules, measured by similarity to official rules and |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SIEM. | execution success across SIEM vendors? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 7

| RulePilot | : An LLM-Powered Agent for Security Rule Generation | ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| • | RQ2- | Efficiency | : What are the latency and resource costs of the | Table 4: Category of our ground-truths, with each item con- |  |  |  |  |
| rule generation process? | taining the NLP descriptions and associate SPL rules. |  |  |  |  |  |  |  |
| • | RQ3- | Ablation Study | : Do the specific components in | RulePilot | Rules-Set Type | size | Time Frame |  |
| help improve the quality of rule generation? | Application | 125 | 2024-09-30 – 2024-11-19 |  |  |  |  |  |
| • | RQ4- | Compatibility | : Does | RulePilot | support the conversion be- | Cloud | 271 | 2024-09-30 – 2024-10-31 |
| tween Splunk SPL and Microsoft KQL? | Endpoint | 1187 | 2024-09-24 – 2024-12-03 |  |  |  |  |  |

4.1 Experimental Settings

4.1.1 Implementation Details. We implemented a fully functional

prototype of RulePilot , designed for automated rule generation

of 0.9 (ensuring controlled diversity), and set a maximum response

length of 512 tokens to prevent excessively long outputs. We use

tained macros, which are vendor-specific or environment-specific

macro like ’process_cmd’ , should be replaced with its specific

vided by MITRE ATT&CK, including 229,968 system logs from

61 atomic tests, covering 12 tactics in MITRE ATT&CK, covering

broad applicability and reducing evaluation bias. The system logs

were collected using EventViewer in a controlled environment, cap-

turing system, Sysmon, and PowerShell logs on a virtual machine

running Windows 10 (64-bit). Our evaluation focuses primarily on

Windows events due to their widespread use in both enterprises

and consumer marketss [12]. The datasets have their labels based

on our simulation process, open-sourced in [32].

https://github.com/splunk/security_content. We primarily use rules from the detec-

| Network | 44 | 2024-09-25 – 2024-11-06 |
| --- | --- | --- |
| Web | 72 | 2024-09-30 – 2024-10-17 |

those employed by RulePilot .

ment.

in our evaluation.

dering) [9] is an advanced NLP metric that improves upon BLEU

ations in rule expressions.

The quantifiable similarity assessment offers an objective metric

but may yield misleadingly high scores for syntactically similar

yet semantically incorrect rules. To mitigate this, we adopt the

LLM-as-a-judge approach, a scalable and explainable method for

approximating human preferences [20]. We evaluate rule quality

from a semantic perspective, considering six key evaluation dimen-

sions below.

• Logical Consistency (LC). The LLM looks at conditions, operators,

| and conversion in Splunk SIEM. | RulePilot | is built upon GPT-4o, | models generate rules using the same prompts as those employed |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| DeepSeek-V3 (671B), and LLaMA-3 (405B), with agent-based or- | by | RulePilot | in its rule generation step, without any additional multi- |  |  |  |
| chestration implemented using their function-calling capabilities. | step processing, validation, or refinement. We download DeepSeek- |  |  |  |  |  |
| To control generation behavior, we configure all models with a | V3 and LLaMa-3 models from Hugging Face [5],[2] To ensure con- |  |  |  |  |  |
| temperature of 0.3 (balancing determinism and flexibility), top-p | sistency across all models, we use the same model parameters as |  |  |  |  |  |
| the Splunk of version 9.3.1, and the trial license for experiments. | 4.2 | Evaluation Metrics |  |  |  |  |
| 4.1.2 | Datasets. | We evaluate | RulePilot | using two sources of rules: | Accuracy. | Our accuracy evaluation consists of two complemen- |
| Splunk official rules | from the Splunk Security Content repos- | tary metrics: | quantifiable similarity assessment | and | an LLM-based |  |
| itory | 4 | as the ground truth to evaluate the similarity score, and | evaluator | . The first metrics measure the textual similarity between |  |  |
| the | custom rules between Splunk SPL and Microsoft KQL | the generated rules and the ground truth (i.e., the official rules), |  |  |  |  |
| currently used by our industry collaborator | for their security | creating an objective assessment of structural and lexical alignment. |  |  |  |  |
| operations to evaluate the compatibility. The Splunk official rules | We adopt three well-established quantifiable metrics below. |  |  |  |  |  |
| we download contain a total of 1,699 samples, organized into five | • | ROUGE | (Recall-Oriented Understudy for Gisting Evaluation) [22] |  |  |  |
| major categories based on their focus (shown in Table 4), maximiz- | is an NLP metric that compares machine-generated text with ref- |  |  |  |  |  |
| ing coverage across comprehensive and diverse categories, reducing | erence text to measure content similarity. A higher ROUGE-k in- |  |  |  |  |  |
| evaluation bias. The key components of the datasets include the | dicates a greater overlap of k-grams between the generated and |  |  |  |  |  |
| rule body (SPL) and the corresponding description that explains | ground truth rule. Here, we set k = 1 and include ROUGE-L, cap- |  |  |  |  |  |
| the purpose and context of the rule. The original datasets con- | turing the longest common subsequence to reflect structural align- |  |  |  |  |  |
| variations. The macro abstracts the specific directives, and do not | • | BLEU | (Bilingual Evaluation Understudy) [28] is a widely used |  |  |  |
| conform to rule grammars, possibly affecting rule consistency. To | precision-oriented NLP metric that evaluates text similarity based |  |  |  |  |  |
| ensure a fair comparison, we replaced all macros with standardized | on n-gram overlap. A higher BLEU-k score indicates better align- |  |  |  |  |  |
| definitions based on Splunk’s official macro library. For example, a | ment between the generated and ground truth rule. We use BLEU-4 |  |  |  |  |  |
| SPL equivalent: | Processes.process_name = cmd.exe | . | • | METEOR | (Metric for Evaluation of Translation with Explicit OR- |  |
| 4.1.3 | System Log Collection. | To evaluate the execution success of | by incorporating stemming, synonym matching, and word order |  |  |  |
| our generated rules, we simulate various atomic attacks [1] pro- | considerations, making it a more robust metric for comparing vari- |  |  |  |  |  |
| 4.1.4 | Baseline. | We compare | RulePilot | ’s performance against that | and filters to see if anything is missing or changed. |  |
| based upon the standalone LLMs of GPT-4o, DeepSeek-V3 (671B), | • | Syntax Correctness | (SC). The LLM checks for mistakes in the |  |  |  |
| and LLaMa-3 (405B), without the structured reasoning and function- | query and looks for ways to write it better. |  |  |  |  |  |
| calling mechanisms of | RulePilot | . For a fair comparison, both baseline | • | Readability & Maintainability | (RM). The LLM checks if the rule |  |
| 4 | is written in a clear way, without unnecessary complexity. |  |  |  |  |  |
| tions | folder to evaluate the similarity score and reference macro definitions from the | • | Condition Coverage | (CC). The LLM ensures no key conditions are |  |  |
| macros | folder for completeness. | missing or unnecessary constraints are added. |  |  |  |  |

---

## Page 8

| ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil | Hongtai Wang | * | , Ming Xu | *# | , Yanpei Guo, Weili Han, Hoon Wei Lim, and Jin Song Dong |
| --- | --- | --- | --- | --- | --- |
| • | False Positive & False Negative Risk | (FPFNR). The LLM checks | for models to capture accurate patterns. Literature [8], [10] also sup- |  |  |
| if the rule is too strict (which may miss real threats) or too loose | port this claim that web-related security rules are complex. When |  |  |  |  |
| (which may flag normal activities). | comparing different LLMs, | RulePilot | achieves its highest perfor- |  |  |
| • | Execution Efficiency | (EE). The LLM analyzes whether the rule | mance using GPT-4o, compared to and LLaMa-3. This suggests that |  |  |
| uses complex operations, unnecessary filters, or inefficient queries | GPT-4o is better suited for structured rule-generation tasks, likely |  |  |  |  |
| that could slow down processing. | due to its improved reasoning and instruction-following capabili- |  |  |  |  |

We adopt a scoring scheme ranging from 0 to 1 for each evaluation

dimension. Instead of focusing on absolute scores, we emphasize

relative rankings across outputs under the same prompt for evalu-

ative prompt refinement process to align the evaluation standards.

We define inter-rater agreement as a match in relative preference,

for example, both the human and the LLM giving higher scores

to RulePilot over the corresponding vanilla LLMs (baseline) is con-

127 2

R > B

B > R

R > B B > R

Human Preference

Execution Success. We ingest all collected logs into Splunk, exe-

cute the generated rules as search queries, and verify their accuracy

by comparing retrieved logs against the ground truth from simu-

lated atomic tests. Execution is considered successful if the retrieved

logs match the expected attack-generated logs. We compute pre-

cision, recall, and other metrics to assess rule effectiveness. To

quantify performance, we use 𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 = 𝑇 𝑃

𝑇 𝑃 + 𝐹 𝑃 , 𝑟𝑒𝑐𝑎𝑙𝑙 = 𝑇 𝑃

𝑇 𝑃 + 𝐹 𝑁 ,

and 𝐹 1 = 2 · Precision · Recall

4.3.1 RQ1-Accuracy. We present our quantifiable similarity assess-

ties.

Baseline Model Output

(eventName=\"CreateLoginProfile\" OR eventName=\"ConsoleLogin\")

| stats count by userName, srcIp

| where count > 1

| sort _time

| table _time, userName, srcIp, count

RulePilot Output

| stats count by sourceIPAddress, eventName,

eventName=\"ConsoleLogin\"

| transaction sourceIPAddress startswith=CreateLoginProfile

endswith=ConsoleLogin maxspan=5m

| table _time, eventName, userAgent, errorCode,

requestParameters.userName

Figure 4: Expert-reviewed comparison between rules gen-

GPT-4o.

creation and subsequent login attempts, relying only on counting

occurrences per user and IP. While it correctly filters relevant event

types, it lacks a mechanism to determine if a login actually follows

a profile creation within a short window.

Second, to avoid the syntactically similar yet semantically in-

correct evaluation, we show the results of radar chart in Figure 5,

illustrating the results of LLM-based evaluator results. We can find

that RulePilot consistently outperforms all standlone LLMs across

six evaluation dimensions. GPT-4o achieves the highest perfor-

(SC). In contrast, DeepSeek-V3 and LlaMa-3 show weaker perfor-

False Negative Risk (FPFNR).

| ating the effectiveness of different methods. To mitigate evaluation | index=aws_cloudtrail sourcetype=\"aws:cloudtrail\" |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| bias, we followed a human-aligned iterative evaluation framework. | \| eval eventType=case(eventName==\"CreateLoginProfile\", "Profile |  |  |  |  |
| An experienced human expert and an LLM were involved in an iter- | Creation\", eventName==\"ConsoleLogin\", "Login Attempt\") |  |  |  |  |
| sidered consistent, regardless of exact numerical values. Under | index=aws_cloudtrail sourcetype=\"aws:cloudtrail\" |  |  |  |  |
| this definition, we show the matrix in Figure 3 based on pairwise | (eventName=\"CreateLoginProfile\" OR eventName=\"ConsoleLogin\") |  |  |  |  |
| preferences, where our inter-rater agreement test reaches a larger | requestParameters.userName, _time |  |  |  |  |
| Cohen’s Kappa [17] score of 0.85, indicating strong agreement. | \| where eventName=\"CreateLoginProfile\" AND |  |  |  |  |
| LLM Preference | 7 | 34 | erated by | RulePilot | versus those generated by standalone |
| Figure 3: Preference inter-rater alignment between the LLM | Looking deeply, our experts judge a concrete example of a rule |  |  |  |  |
| and the human evaluator. R refers to | RulePilot | , and B refers | generated by | RulePilot | and the GPT-4o baseline model. We present |
| to Baseline. The “ | > | ” indicates that the method was rated | an expert-reviewed result in Figure 4. This demonstrates a rule |  |  |
| higher in a pairwise comparison. The diagonal entries indi- | related to AWS CloudTrail login and profile creation monitoring. |  |  |  |  |
| cate agreement between the LLM and the human evaluator. | We can find that the baseline model fails to properly correlate profile |  |  |  |  |
| Precision | + | Recall | as evaluation metrics. | mance across most dimensions, particularly in Syntax Correctness |  |
| 4.3 | Evaluation Results | mance, especially in Condition Coverage (CC) and False Positive & |  |  |  |
| ment | in Table 5. Overall, | RulePilot | consistently outperforms all its | Execution Success. | To show the execution success of the gener- |
| corresponding baseline models across every category. The improve- | ated rules in a SIEM vendor, we show our results in Table 6, where |  |  |  |  |
| ments range from 20.9% to 107.4%, demonstrating that | RulePilot | we find that | RulePilot | consistently achieves higher precision and |  |
| significantly enhances both the syntactic accuracy of the generated | recall across most tactics compared to GPT-4o, demonstrating its |  |  |  |  |
| rules. Among the different detection categories, the cloud achieves | ability to generate executable detection rules in Splunk. Notably, |  |  |  |  |
| the highest overall performance, suggests that cloud-based detec- | RulePilot | achieves perfect (100%) precision across multiple tactics, |  |  |  |
| tion rules are relatively easier for | RulePilot | to generate accurately, | confirming that its generated rules accurately match ground truth |  |  |
| possibly due to the structured and well-documented nature of cloud | detections without false positives in these cases. However, certain |  |  |  |  |
| security rules. In contrast, the web category exhibits the lowest | tactics exhibit lower precision and recall, particularly for Privilege |  |  |  |  |
| performance across most metrics. This indicates that web-related | Escalation, where GPT-4o fails entirely (0% precision and recall), |  |  |  |  |
| security rules tend to be more complex or diverse, making it harder | while | RulePilot | retains some detection capability. These lower scores |  |  |

---

## Page 9

RulePilot : An LLM-Powered Agent for Security Rule Generation ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil

Table 5: Syntax-level evaluation. Similarity comparison of the generated rules from RulePilot (RP) and baselines (BL) with

ground truth, including GPT-4o (GPT), DeepSeek-V3-671B (DS), and LLaMa-3-405B (LLaMa).

Category BLEU ( ↑ ) ROUGE-1 ( ↑ ) ROUGE-L ( ↑ ) METEOR ( ↑ )

GPT DS LLaMa GPT DS LLaMa GPT DS LLaMa GPT DS LLaMa

RP BL RP BL RP BL RP BL RP BL RP BL RP BL RP BL RP BL RP BL RP BL RP BL

| application (54) | 39.1 | 33.6 | 43.8 | 30.2 | 32.5 | 31.1 | 49.2 | 36.6 | 42.3 | 33.9 | 41.6 | 36.8 | 41.7 | 26.2 | 32.3 | 24.4 | 33.2 | 26.5 | 41.3 | 27.3 | 26.7 | 19.6 | 29.5 | 27.1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cloud (271) | 47.9 | 33.9 | 40.9 | 25.4 | 38.3 | 27.0 | 58.7 | 44.4 | 53.1 | 21.6 | 48.1 | 28.8 | 53.7 | 37.5 | 52.5 | 29.1 | 46.1 | 26.7 | 58.1 | 43.8 | 61.4 | 32.2 | 65.0 | 33.9 |
| endpoint (1,187) | 42.8 | 29.5 | 34.8 | 24.5 | 32.8 | 27.8 | 59.8 | 36.6 | 51.0 | 24.4 | 48.7 | 43.0 | 57.3 | 32.5 | 42.0 | 30.9 | 40.1 | 37.0 | 66.3 | 37.8 | 35.9 | 29.6 | 42.5 | 22.9 |
| network (43) | 41.9 | 41.5 | 35.2 | 27.9 | 45.4 | 39.0 | 60.1 | 49.5 | 37.0 | 27.5 | 58.8 | 37.7 | 57.1 | 43.3 | 27.0 | 18.4 | 58.2 | 30.0 | 59.2 | 42.4 | 25.5 | 24.9 | 60.7 | 34.9 |
| web (72) | 41.6 | 34.8 | 27.5 | 22.1 | 32.0 | 28.2 | 57.0 | 43.3 | 39.8 | 20.6 | 38.6 | 28.8 | 50.1 | 37.9 | 31.9 | 14.5 | 36.6 | 27.3 | 56.6 | 41.2 | 28.9 | 17.4 | 43.8 | 34.8 |
| Total (1,627) | 43.4 | 30.9 | 35.8 | 24.8 | 34.0 | 28.1 | 59.1 | 38.5 | 50.2 | 24.2 | 48.2 | 39.7 | 55.9 | 33.6 | 42.6 | 29.3 | 41.2 | 34.3 | 63.5 | 38.7 | 39.3 | 29.0 | 46.4 | 25.7 |
| LC | LC | LC | Table 6: Execution-level success on the Splunk SIEM. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

SC EE 1.0 SC EE 1.0 SC EE 1.0

RM FPFNR RM FPFNR RM FPFNR

lot ’s score.

struggle to generate effective detection rules, relying only on static

descriptions without real-time feedback.

trieving real-time log feedback and refining its rules iteratively. This

complex attack patterns that GPT-4o fails to capture, particularly in

rule descriptions.

key behavioral indicators are implicitly described in input descrip-

tions, rendering RulePilot and vanilla LLMs ineffective. For example,

outperform the vanilla GPT-4o.

Answer to RQ1: RulePilot agent-based reasoning mecha-

nism enhances logical structure and syntax adherence in

terms of both similarity score and the execution success.

| Tactic | Precision (%) | Recall (%) |  |  |
| --- | --- | --- | --- | --- |
| Initial Access | 1.000 | 1.000 | 1.000 | 1.000 |
| Execution | 1.000 | 0.909 | 0.750 | 0.416 |
| Lateral Movement | 1.000 | 1.000 | 0.667 | 0.667 |
| Collection | 1.000 | 1.000 | 1.000 | 1.000 |
| Model | Tokens | Tokens | Cost | Time |
| Baseline | 1,295 | 325 | $0.012 | 12s |
| Baseline | 3,284 | 772 | – | 31s |
| Baseline | 1,734 | 474 | – | 26s |

accessable latency.

Answer to RQ2: RulePilot generates well-structured rules

while maintaining accessible latency.

| 0.6 | 0.6 | 0.6 | RulePilot | GPT-4o | RulePilot | GPT-4o |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.2 | 0.2 | 0.2 | Reconnaissance | 1.000 | 1.000 | 1.000 | 1.000 |  |  |  |
| CC | CC | CC | Persistence | 1.000 | 1.000 | 0.818 | 0.714 |  |  |  |
| (a) | GPT-4o | (b) | DeepSeek-V3 | (c) | LlaMa-3 | Privilege Escalation | 0.600 | 0.000 | 0.214 | 0.000 |
| Figure 5: Semantic-level evaluation. Radar chart of LLM- | Defense Evasion | 0.733 | 0.600 | 0.833 | 0.656 |  |  |  |  |  |
| based evaluator: the inner shaded area represents the base- | Credential Access | 1.000 | 1.000 | 0.450 | 0.264 |  |  |  |  |  |
| line model’s score, while the outer contour represents | RulePi- | Discovery | 0.667 | 0.167 | 0.444 | 0.100 |  |  |  |  |
| are primarily due to the | subtle | nature of malicious logs associated | Command and Control | 1.000 | 1.000 | 1.000 | 1.000 |  |  |  |
| with these tactics, where critical identifying fields do not explic- | Exfiltration | 0.667 | 0.333 | 0.500 | 0.200 |  |  |  |  |  |
| itly appear in the rule descriptions. As a result, baseline models | Impact | 0.722 | 0.594 | 0.650 | 0.731 |  |  |  |  |  |
| In contrast, | RulePilot | demonstrates significantly better perfor- | Table 7: Efficiency and cost of | RulePilot | and baselines. |  |  |  |  |  |
| mance due to its ability to autonomously call the Splunk API, re- | Prompt | Output | Money | Generation |  |  |  |  |  |  |
| self-reflective and API-driven approach enables | RulePilot | to detect | GPT-4o | RulePilot | 13,752 | 2489 | $0.060 | 78s |  |  |
| scenarios where key indicators are not directly stated in the initial | DeepSeek-V3 | RulePilot | 24,820 | 4,296 | – | 158s |  |  |  |  |
| Failure Cases. | We analyze that the failures often occur when the | LLaMA-3 | RulePilot | 22,107 | 2,985 | – | 119s |  |  |  |
| we have checked the low recalls of 0.21 ( | RulePilot | ) and 0.0 (GPT-4o) | 4.3.2 | RQ2-Efficiency. | We present the computational and economic |  |  |  |  |  |
| in our own tests of Privilege-Escalation rules, the input description | costs in Table 7, which are derived by running | RulePilot | and the |  |  |  |  |  |  |  |
| states “These calls are used to spawn MSBuild.exe in a suspended | baseline approach on Splunk’s open-source datasets (detailed in |  |  |  |  |  |  |  |  |  |
| state before injecting the decrypted SaintBot binary into it, modi- | Table 4) and averaging the results across multiple test cases. We |  |  |  |  |  |  |  |  |  |
| fying the thread context to point to the malicious entry point and | find that | RulePilot | requires more tokens and computation time than |  |  |  |  |  |  |  |
| resuming the process” without the behavioral indicators of process | the baseline approach, mainly due to its stepwise reasoning and |  |  |  |  |  |  |  |  |  |
| hollowing- a technique often used for privilege escalation or exe- | iterative refinement. However, this also results in more complete |  |  |  |  |  |  |  |  |  |
| cution evasion. Under the same inputs, | RulePilot | can consistently | and logically structured rules, as seen in earlier evaluations, with |  |  |  |  |  |  |  |

---

## Page 10

| ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil | Hongtai Wang | * | , Ming Xu | *# | , Yanpei Guo, Weili Han, Hoon Wei Lim, and Jin Song Dong |
| --- | --- | --- | --- | --- | --- |
| 4.3.3 | RQ3-Ablation Study. | To further evaluate the effectiveness | LC |  |  |
| of the key components in | RulePilot | , we conduct an ablation study | RulePilot (complete) |  |  |
| focusing on two critical elements: the IR and the combination of | SC | EE | 1.0 |  |  |
| CoT reasoning and Reflection (CoT-R). Since Reflection involves | 0.6 | Without IR |  |  |  |
| iterative refinements that call CoT modules, these two components | 0.2 |  |  |  |  |
| are inherently linked and evaluated as CoT-R. To assess the indi- | Without CoT-R |  |  |  |  |

vidual contributions, we introduce three experimental variants to

isolate the contribution of each component: one without IR, another

without CoT-R, and a version without both IR and CoT-R. The full

version of RulePilot incorporates both IR guidance and CoT-R. We

decrease in rule generation, and removing both components causes

the most substantial drop across all metrics. Without CoT-R and IR,

the model struggles to handle complex conditions and multi-step

logic, leading to incomplete or logically inconsistent rules. This sug-

gests that CoT-R and IR play a critical role in enabling the model to

break down complex rule-generation tasks into manageable steps,

resulting in better logical consistency and structural coherence.

Average Performance

0.55 ROUGE-1

ROUGE-L

METEOR

0.44

0.41

0.3

(complete) CoT-R & IR

Figure 6: Ablation study on the impact of IR and CoT-R.

eration. CoT-R helps with logic and structuring, while IR

ensures correct syntax and readability. Removing either

RM FPFNR

Without CoT-R & IR

CC

real-world security applications within our industry collaborator,

having been collected, segmented, and anonymized to eliminate

sensitive information while preserving their syntactic and struc-

tural integrity. We further categorize the dataset into three types:

aggregation-based rules, which summarize event data; list-based

rules, which group multiple attributes; and join-based rules, which

are complex and involve multi-source data correlation to detect

SPL and KQL rules. To maintain consistency, we collected logs

based on cases of converting KQL to SPL. For each rule, we convert

in Splunk, and compare its results with the original SPL query from

Evaluation Results. We present the evaluation results in Table 8

and list-based rules achieve perfect precision, recall and F1 (1.000),

to their simple structure and direct function mappings between SPL

and KQL. Since they primarily involve statistical summarization or

attribute grouping, the model can accurately translate their logic

Rule Type Precision ( ↑ ) Recall ( ↑ ) F1 ( ↑ )

Aggregation-Based Rules 1.000 1.000 1.000

This experiment demonstrates the compatibility and generaliza-

| present the results of the ablation study in Figure 6. The overall | Figure 7: Ablation study for semantic-level evaluation be- |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| trend reveals that removing either IR or CoT-R leads to a significant | tween | RulePilot | and its variants. |  |  |
| 0.6 | BLEU | cross-event security patterns. Each category contains 10 pairs of |  |  |  |
| 0.5 | oriented to Splunk, and evaluate the execution success on Splunk |  |  |  |  |
| 0.4 | 0.35 | the given KQL query into an SPL query using our model, execute it |  |  |  |
| Performance | the dataset. If both queries retrieve the same logs under identical |  |  |  |  |
| 0.2 | conditions, the conversion is considered successful. |  |  |  |  |
| 0.1 | for rule conversion, categorized by rule type. The aggregation-based |  |  |  |  |
| 0.0 | RulePilot | Without IR | Without CoT-R | Without | indicating that these rule types are straightforward to convert due |
| Additionally, to determine the specific areas influenced by IR and | without ambiguity. However, join-based rules exhibit slightly lower |  |  |  |  |
| CoT-R, we conduct a semantic evaluation, with results shown in | performance. These rules involve multi-source data correlation, |  |  |  |  |
| Figure 7. We find that removing CoT-R causes the most significant | requiring careful field mapping and handling of log relationships |  |  |  |  |
| degradation in Logical Consistency (LC) and Condition Coverage | across different event sources. The drop in performance is primar- |  |  |  |  |
| (CC). Conversely, removing IR primarily affects Syntax Correctness | ily due to boundary cases where certain event correlation logic |  |  |  |  |
| (SC) and Readability & Maintainability (RM). The findings further | was not fully preserved, leading to minor mismatches in retrieved |  |  |  |  |
| highlight the complementary roles of these components, where CoT- | log sets. Despite this, the results demonstrate that the conversion |  |  |  |  |
| R enhances logical structuring, and IR ensures syntactic correctness | model is highly effective across different rule types, particularly for |  |  |  |  |
| and standardization. | structured and statistical queries. |  |  |  |  |
| Answer to RQ3: | Both IR and CoT-R improve rule gen- | Table 8: Evaluation of rule conversion from KQL to SPL. |  |  |  |
| one lowers performance, and removing both causes the | List-Based Rules | 1.000 | 1.000 | 1.000 |  |
| biggest drop. | Join-Based Rules | 0.926 | 0.913 | 0.919 |  |
| 4.4 | RQ4-Compatibility | tion capability of | RulePilot | for cross-SIEM rule conversion. While |  |
| To evaluate the compatibility of | RulePilot | , we use the dataset con- | this experiment focuses on KQL-to-SPL translation due to log avail- |  |  |
| sisting of 30 SPL rules and their corresponding 30 KQL rules, which | ability constraints (i.e., we collected logs oriented to Splunk SIEMs |  |  |  |  |
| serve as ground truth references. These rules are sourced from | for execution success), | RulePilot | is inherently designed to support |  |  |

---

## Page 11

| RulePilot | : An LLM-Powered Agent for Security Rule Generation | ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil |  |
| --- | --- | --- | --- |
| flexible and bidirectional conversions across multiple SIEM plat- | the rule passes vendor-side syntax checks, e.g., Splunk), and logical |  |  |
| forms. SPL2KQL | 5 | is one of the publicly available rule conversion | alignment (whether the rule logic matches the input as judged by |
| tools used in industry. Developed by Microsoft, it supports one-way | an expert). The details are shown in our user study in | 6 | . |
| translation from Splunk SPL to Microsoft Sentinel’s KQL. SPL2KQL | The comparison study show that | RulePilot | can significantly im- |
| is primarily designed to ingest external detection rules into the | prove the manul rule generation process for both both general users |  |  |
| Microsoft ecosystem and is based on traditional rule rewriting | and junior analysts, reducing the time required and improving rule |  |  |
| techniques such as keyword mapping, syntax tree parsing, and | quality in terms of syntactic validity and logical alignment with |  |  |
| regex-based transformation. However, it does not support reverse | expert-level standards. |  |  |

conversion or semantic adaptation for other platforms. In contrast,

(Sample1 in SPL2KQL ) Sysmon

TargetImage=*lsass.exe | where TargetImage contains "lsass.exe"

OR | summarize count(), firstTime = min(TimeGenerated), lastTime =

| stats count min(_time) SourceProcessId

as lastTime by Computer,

| TargetProcessId, | sysmon EventCode = 10 TargetImage = lsass.exe CallTrace = dbgcore.dll OR |
| --- | --- |
| SourceProcessId | \| stats count min (_time) as firstTime max (_time) as lastTime by Computer, |

version between Splunk SPL to Microsoft KQL, supporting

the abilities of translating multiple types of rules across

produce a complete rule), final rule output, syntax validity (whether

been explored for log-based anomaly detection [29], demonstrat-

parsing and structured analysis. Unlike prior studies that focus on

general log processing, our work builds upon existing SIEM rules

6 Conclusion

signed to automate rule creation and conversion for SIEM detection.

By leveraging the novel SIEM-specific intermediate representation,

| RulePilot | leverages LLM-based semantic understanding and an in- | 5 | Discussion and Related Works |  |  |
| --- | --- | --- | --- | --- | --- |
| termediate representation (IR) layer to support | bidirectional and | Automation Level. | RulePilot | achieves a half-automated approach |  |
| context-aware rule conversion | , such as KQL-to-SPL, SPL-to-KQL, | to SIEM-specific rule generation by embedding the logic and exper- |  |  |  |
| or even translation between other vendor formats. This flexibility | tise of senior analysts. It simulates their decision-making process, |  |  |  |  |
| makes | RulePilot | applicable to a wider range of deployment scenar- | including pipeline breakdown, formal template structuring, and |  |  |
| ios, including hybrid or transitioning security infrastructures. | iterative refinement. However, in practice, certain field validations |  |  |  |  |
| To provide a more intuitive comparison when converting SPL | and the final results require human oversights, which junior ex- |  |  |  |  |
| to KQL, we select one piece of SPL from the official SPL2KQL | perts can handle to ensure functional-correctness and reliability. |  |  |  |  |
| demo repository and convert the SPL to KQL using both SPL2KQL | The operator is expected to be familiar with the SIEM environments. |  |  |  |  |
| and | RulePilot | . As shown in Figure 8, | RulePilot | can generate a se- | Compared to manual rule creation, the junior experts here focus on |
| mantically faithful KQL rule by aligning query operators (e.g., | validation, eliminating the need to master complex rule grammars. |  |  |  |  |
| contains | , | project-rename | ) and adapting field references such | Constraint Generation. | Recent studies have utilized LLMs to |
| as | TimeGenerated | , reflecting a deep understanding of both source | generate constraint logic rules in various domains [25, 26, 51]. For |  |  |
| and target semantics. In contrast, SPL2KQL applies literal keyword | instance, LLMs have been applied to formal verification tasks in |  |  |  |  |
| mappings (e.g., | TargetImage = lsass.exe | ) and syntactic trans- | smart contracts [24], and to the automated extraction of generic- |  |  |
| formations (e.g., | rename | ) without semantic reinterpretation, re- | signature detection rule candidates from textual and visual open- |  |  |
| sulting in inaccurate or even invalid KQL logic in practical use. | source cyber threat intelligence data [36]. Additionally, LLMs have |  |  |  |  |
| Original SPL Rule | KQL Rule converted by | RulePilot: | ing the potential of LLMs in leveraging pre-trained knowledge to |  |  |
| `sysmon` EventCode=10 | \| where EventID == 10 | extract structured insights from large-scale log data and assist in |  |  |  |
| CallTrace=*dbgcore.dll* | \| where CallTrace contains "dbgcore.dll" or CallTrace contains "dbghelp.dll" | constraint generation. However, challenges persist in modeling and |  |  |  |
| CallTrace=*dbghelp.dll* | max(TimeGenerated) by Computer, TargetImage, TargetProcessId, SourceImage, | capturing the intricate structures of SIEM rules, hindering the direct |  |  |  |
| as firstTime max(_time) | \| project-rename dest = Computer | application of these methods to generate executable security rules. |  |  |  |
| TargetImage, | KQL Rule converted by | SPL2KQL: | Log Analysis. | Previous works largely employ LLMs to automate |  |
| SourceImage, | CallTrace = dbghelp.dll | log analysis [23, 29 | ? | ], including log parsing and anomaly detection. |  |
| \| rename Computer as | TargetImage , TargetProcessId , SourceImage , SourceProcessId | For instance, LLM-based approaches achieve high precision in log |  |  |  |
| dest | \| rename Computer as dest | template extraction [50] and automatic logging statement genera- |  |  |  |
| Figure 8: Comparison between the KQL rules converted from | tion [49], significantly reducing manual effort. These approaches |  |  |  |  |
| SPL via SPL2KQL and | RulePilot | . | may provide valuable foundations for our work by improving log |  |  |
| Answer to RQ4: | RulePilot | effectively supports rule con- | and leverages LLMs to analyze logs and detect anomalies. |  |  |
| SIEM systems. | In this paper, we propose | RulePilot | , an LLM-based agent system de- |  |  |
| 4.5 | Case Study | RulePilot | abstracts the complexity of rule configurations into a struc- |  |  |
| We perform a case study to compare the statistical labor reduction | tured and standardized format. We conduct a comprehensive evalu- |  |  |  |  |
| using | RulePilot | , assessing how users of different security exper- | ation of | RulePilot | , demonstrating that it can produce high-fidelity, |
| tise levels perform in rule authoring with and without its support. | executable SIEM-specific rules. Our case study with industry collab- |  |  |  |  |
| We recruit | general users | without any background of SIEM en- | orators shows that | RulePilot | significantly assists general users and |
| vironments and the | junior analysts | with beginner experience | junior analysts by reducing rule generation time and improving |  |  |
| with SIEM exposure, under the premise that | RulePilot | incorporates | rule quality, allowing them to create detection logic using natural |  |  |
| expert-level expertise. We evaluate the time taken (Time used to | language instead of manually adhering to strict grammar rules. |  |  |  |  |
| 5 | https://azure.github.io/spl2kql/dist/index.html | 6 | https://sites.google.com/view/rulepilot/user-study. |  |  |

---

## Page 12

ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil Hongtai Wang * , Ming Xu *# , Yanpei Guo, Weili Han, Hoon Wei Lim, and Jin Song Dong

Acknowledgments [21] Raymond Li, Loubna Ben Allal, Yangtian Zi, Niklas Muennighoff, Denis Kocetkov,

Chenghao Mou, Marc Marone, Christopher Akiki, Jia Li, Jenny Chim, Qian Liu,

| We thank the anonymous meta review and all anonymous reviewers | Evgenii Zheltonozhskii, Terry Yue Zhuo, Thomas Wang, Olivier Dehaene, Mishig |
| --- | --- |
| for their insightful comments to improve this paper. This paper is | Davaadorj, Joel Lamy-Poirier, João Monteiro, Oleh Shliazhko, Nicolas Gontier, |
| supported by NUS-NCS Joint Laboratory for Cyber Security. | Nicholas Meade, Armel Zebaze, Ming-Ho Yee, Logesh Kumar Umapathi, Jian |

Zhu, Benjamin Lipkin, Muhtasham Oblokulov, Zhiruo Wang, Rudra Murthy

V, Jason T. Stillerman, Siva Sankalp Patel, Dmitry Abulkhanov, Marco Zocca,

Manan Dey, Zhihan Zhang, Nour Fahmy, Urvashi Bhattacharyya, Wenhao Yu,

Swayam Singh, Sasha Luccioni, Paulo Villegas, Maxim Kunakov, Fedor Zhdanov,

| References | Manuel Romero, Tony Lee, Nadav Timor, Jennifer Ding, Claire Schlesinger, Hailey |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| [1] 2022. Atomic Red Team™ is a library of tests mapped to the MITRE ATT&CK | Schoelkopf, Jan Ebert, Tri Dao, Mayank Mishra, Alex Gu, Jennifer Robinson, |  |  |  |  |
| framework. Security teams can use Atomic Red Team to quickly, portably, and | Carolyn Jane Anderson, Brendan Dolan-Gavitt, Danish Contractor, Siva Reddy, |  |  |  |  |
| reproducibly test their environments. https://github.com/redcanaryco/atomic- | Daniel Fried, Dzmitry Bahdanau, Yacine Jernite, Carlos Muñoz Ferrandis, Sean |  |  |  |  |
| red-team/tree/master/atomics. | Hughes, Thomas Wolf, Arjun Guha, Leandro von Werra, and Harm de Vries. 2023. |  |  |  |  |
| [2] 2022. | meta-llama/Llama-3.1-405B · Hugging Face — huggingface.co. | https: | StarCoder: may the source be with you! | Trans. Mach. Learn. Res. | 2023 (2023). |
| //huggingface.co/meta-llama/Llama-3.1-405B. | https://openreview.net/forum?id=KoFOg41haE |  |  |  |  |
| [3] 2022. | text-embedding-ada-002. | https://platform.openai.com/docs/guides/ | [22] Chin-Yew Lin. 2004. Rouge: A package for automatic evaluation of summaries. |  |  |
| embeddings/what-are-embeddings. | In | Text summarization branches out | . 74–81. |  |  |
| [4] 2023. SolarWinds hack explained: Everything you need to know. | [23] Yilun Liu, Shimin Tao, Weibin Meng, Jingyu Wang, Wenbing Ma, Yuhang Chen, |  |  |  |  |
| [5] 2024. | deepseek-ai/DeepSeek-V3 · Hugging Face — huggingface.co. | https:// | Yanqing Zhao, Hao Yang, and Yanfei Jiang. 2024. Interpretable online log analysis |  |  |
| huggingface.co/deepseek-ai/DeepSeek-V3. | using large language models with prompt strategies. In | Proceedings of the 32nd |  |  |  |
| [6] Admin. 2025. Top 10 Soft Skills for SOC Analysts. | IEEE/ACM International Conference on Program Comprehension | . 35–46. |  |  |  |
| [7] austinmccollum. [n. d.]. Migrate Splunk detection rules to Microsoft Sentinel | [24] Ye Liu, Yue Xue, Daoyuan Wu, Yuqiang Sun, Yi Li, Miaolei Shi, and Yang |  |  |  |  |
| - Microsoft Sentinel — learn.microsoft.com. https://learn.microsoft.com/en-us/ | Liu. 2024. PropertyGPT: LLM-driven Formal Verification of Smart Contracts |  |  |  |  |
| azure/sentinel/migration-splunk-detection-rules. | through Retrieval-Augmented Property Generation. | CoRR | abs/2405.02580 (2024). |  |  |
| [8] Babak Amin Azad, Pierre Laperdrix, and Nick Nikiforakis. 2019. Less is More: | arXiv:2405.02580 doi:10.48550/ARXIV.2405.02580 |  |  |  |  |
| Quantifying the Security Benefits of Debloating Web Applications. In | 28th USENIX | [25] Zhengxiong Luo, Qingpeng Du, Yujue Wang, Abhik Roychoudhury, and Yu Jiang. |  |  |  |
| Security Symposium (USENIX Security 19) | . USENIX Association, Santa Clara, CA, | 2025. Enhancing Protocol Fuzzing via Diverse Seed Corpus Generation. | IEEE |  |  |
| 1697–1714. | https://www.usenix.org/conference/usenixsecurity19/presentation/ | Transactions on Software Engineering | 51, 9 (2025), 2693–2709. doi:10.1109/TSE. |  |  |
| azad | 2025.3595396 |  |  |  |  |
| [9] Satanjeev Banerjee and Alon Lavie. 2005. METEOR: An automatic metric for | [26] Zhengxiong Luo, Huan Zhao, Dylan Wolff, Cristian Cadar, and Abhik Roychoud- |  |  |  |  |
| MT evaluation with improved correlation with human judgments. In | Proceedings | hury. 2026. Agentic Concolic Execution. In | 2026 IEEE Symposium on Security and |  |  |
| of the acl workshop on intrinsic and extrinsic evaluation measures for machine | Privacy (SP) | . IEEE Computer Society, 1–19. |  |  |  |
| translation and/or summarization | . 65–72. | [27] Microsoft. 2025. Microsoft Sentinel - Cloud-native SIEM Solution \| Microsoft |  |  |  |
| [10] Pedro Bernardo, Lorenzo Veronese, Valentino Dalla Valle, Stefano Calzavara, | Azure — azure.microsoft.com. | https://azure.microsoft.com/en-us/products/ |  |  |  |
| Marco Squarcina, Pedro Adão, and Matteo Maffei. 2024. Web Platform Threats: | microsoft-sentinel. |  |  |  |  |
| Automated Detection of Web Security Issues With WPT. In | 33rd USENIX Security | [28] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. 2002. Bleu: a |  |  |  |
| Symposium (USENIX Security 24) | . USENIX Association, Philadelphia, PA, 757–774. | method for automatic evaluation of machine translation. In | Proceedings of the |  |  |
| https://www.usenix.org/conference/usenixsecurity24/presentation/bernardo | 40th annual meeting of the Association for Computational Linguistics | . 311–318. |  |  |  |
| [11] Sandeep N. Bhatt, Pratyusa K. Manadhata, and Loai Zomlot. 2014. The Operational | [29] Jiaxing Qi, Shaohan Huang, Zhongzhi Luan, Shu Yang, Carol Fung, Hailong Yang, |  |  |  |  |
| Role of Security Information and Event Management Systems. | IEEE Secur. Priv. | Depei Qian, Jing Shang, Zhiwen Xiao, and Zhihui Wu. 2023. Loggpt: Exploring |  |  |  |
| 12, 5 (2014), 35–41. doi:10.1109/MSP.2014.103 | chatgpt for log-based anomaly detection. In | 2023 IEEE International Conference |  |  |  |
| [12] Tom Burt. 2020. | Microsoft report shows increasing sophistication of cyber | on High Performance Computing & Communications, Data Science & Systems, |  |  |  |
| threats. https://blogs.microsoft.com/on-the-issues/2020/09/29/microsoft-digital- | Smart City & Dependability in Sensor, Cloud & Big Data Systems & Application |  |  |  |  |
| defense-report-cyber-threats/. | (HPCC/DSS/SmartCity/DependSys) | . IEEE, 273–280. |  |  |  |
| [13] Xinyun Chen, Maxwell Lin, Nathanael Schärli, and Denny Zhou. 2023. Teaching | [30] Edward Raff, Richard Zak, Gary Lopez Munoz, William Fleming, Hyrum S An- |  |  |  |  |
| Large Language Models to Self-Debug. arXiv:2304.05128 [cs.CL] https://arxiv. | derson, Bobby Filar, Charles Nicholas, and James Holt. 2020. Automatic yara |  |  |  |  |
| org/abs/2304.05128 | rule generation using biclustering. In | Proceedings of the 13th ACM Workshop on |  |  |  |
| [14] The MITRE Corporation. 2024. | The ATT&CK knowledge base is used as a | Artificial Intelligence and Security | . 71–82. |  |  |
| foundation for the development of specific threat models and methodologies in | [31] Stephen Robertson and Hugo Zaragoza. 2009. The Probabilistic Relevance Frame- |  |  |  |  |
| the private sector, in government, and in the cybersecurity product and service | work: BM25 and Beyond. | Foundations and Trends in Information Retrieval | 3 (01 |  |  |
| community. https://attack.mitre.org/. | 2009), 333–389. doi:10.1561/1500000019 |  |  |  |  |
| [15] Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, | [32] RulePilot. 2025. RulePilot - Dataset — sites.google.com. https://sites.google.com/ |  |  |  |  |
| Linjun Shou, Bing Qin, Ting Liu, Daxin Jiang, and Ming Zhou. 2020. CodeBERT: | view/rulepilot/dataset. |  |  |  |  |
| A Pre-Trained Model for Programming and Natural Languages. In | Findings of | [33] Stuart J Russell and Peter Norvig. 2016. | Artificial intelligence: a modern approach | . |  |
| the Association for Computational Linguistics: EMNLP 2020, Online Event, 16-20 | Pearson. |  |  |  |  |
| November 2020 (Findings of ACL, Vol. EMNLP 2020) | , Trevor Cohn, Yulan He, and | [34] Joshua Saxe. 2020. YaraML. https://github.com/sophos-ai/yaraml_rules/. |  |  |  |
| Yang Liu (Eds.). Association for Computational Linguistics, 1536–1547. doi:10. | [35] Yuval Schwartz, Lavi Ben-Shimol, Dudu Mimran, Yuval Elovici, and Asaf Shabtai. |  |  |  |  |
| 18653/V1/2020.FINDINGS-EMNLP.139 | 2024. LLMCloudHunter: Harnessing LLMs for Automated Extraction of Detection |  |  |  |  |
| [16] IBM. 2024. IBM Security QRadar SIEM. | https://www.ibm.com/products/qradar- | Rules from Cloud-Based CTI. | CoRR | abs/2407.05194 (2024). arXiv:2407.05194 |  |
| siem | doi:10.48550/ARXIV.2407.05194 |  |  |  |  |
| [17] Cohen’s Kappa. [n. d.]. A measure of agreement between two dependent cate- | [36] Yuval Schwartz, Lavi Benshimol, Dudu Mimran, Yuval Elovici, and Asaf Shabtai. |  |  |  |  |
| gorical samples. https://datatab.net/tutorial/cohens-kappa. | 2024. Llmcloudhunter: Harnessing llms for automated extraction of detection |  |  |  |  |
| [18] Leon Kersten. 2025. | A Test Tool to Evaluate the Skill Sets. In | Workshop on | rules from cloud-based cti. | arXiv preprint arXiv:2407.05194 | (2024). |
| SOC Operations and Construction (WOSOC 2025) | . San Diego, CA, USA. | https: | [37] Liang Shi, Zhengju Tang, and Zhi Yang. 2024. | A Survey on Employing |  |
| //www.ndss-symposium.org/wp-content/uploads/wosoc25-final1.pdf | Large Language Models for Text-to-SQL Tasks. | CoRR | abs/2407.15186 (2024). |  |  |
| [19] Patrick S. H. Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir | arXiv:2407.15186 doi:10.48550/ARXIV.2407.15186 |  |  |  |  |
| Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim | [38] Splunk. 2025. splunk-sdk-python/splunklib at master. https://github.com/splunk/ |  |  |  |  |
| Rocktäschel, Sebastian Riedel, and Douwe Kiela. 2020. Retrieval-Augmented | splunk-sdk-python/tree/master/splunklib. |  |  |  |  |
| Generation for Knowledge-Intensive NLP Tasks. In | Advances in Neural In- | [39] Splunk cisco company [n. d.]. https://shorturl.at/dgTsP. State of Security 2024: |  |  |  |
| formation Processing Systems 33: Annual Conference on Neural Information | The Race to Harness AI. |  |  |  |  |
| Processing Systems 2020, NeurIPS 2020, December 6-12, 2020, virtual | , Hugo | [40] Splunk Open-sourced Rules [n. d.]. https://github.com/splunk/security_content/ |  |  |  |
| Larochelle, Marc’Aurelio Ranzato, Raia Hadsell, Maria-Florina Balcan, and | tree/develop/detections/network. Splunk Open-sourced Rules. |  |  |  |  |
| Hsuan-Tien Lin (Eds.). | https://proceedings.neurips.cc/paper/2020/hash/ | [41] Splunk Threat Research Team [n. d.]. https://research.splunk.com/detections/. |  |  |  |
| 6b493230205f780e1bc26945df7481e5-Abstract.html | Splunk-Customized Detection Rules. |  |  |  |  |
| [20] Haitao Li, Qian Dong, Junjie Chen, Huixue Su, Yujia Zhou, Qingyao Ai, Ziyi Ye, | [42] Alexey Svyatkovskiy, Shao Kun Deng, Shengyu Fu, and Neel Sundaresan. 2020. |  |  |  |  |
| and Yiqun Liu. 2024. LLMs-as-Judges: A Comprehensive Survey on LLM-based | IntelliCode compose: code generation using transformer. In | ESEC/FSE ’20: 28th |  |  |  |
| Evaluation Methods. arXiv:2412.05579 [cs.CL] https://arxiv.org/abs/2412.05579 | ACM Joint European Software Engineering Conference and Symposium on the |  |  |  |  |

---

## Page 13

| RulePilot | : An LLM-Powered Agent for Security Rule Generation | ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil |  |  |
| --- | --- | --- | --- | --- |
| Foundations of Software Engineering, Virtual Event, USA, November 8-13, 2020 | , | [48] Danning Xie, Zhuo Zhang, Nan Jiang, Xiangzhe Xu, Lin Tan, and Xiangyu Zhang. |  |  |
| Prem Devanbu, Myra B. Cohen, and Thomas Zimmermann (Eds.). ACM, 1433– | 2024. ReSym: Harnessing LLMs to Recover Variable and Data Structure Symbols |  |  |  |
| 1443. doi:10.1145/3368089.3417058 | from Stripped Binaries. In | Proceedings of the 2024 on ACM SIGSAC Conference |  |  |
| [43] Runchu Tian, Yining Ye, Yujia Qin, Xin Cong, Yankai Lin, Yinxu Pan, Ye- | on Computer and Communications Security, CCS 2024, Salt Lake City, UT, USA, |  |  |  |
| sai Wu, Haotian Hui, Weichuan Liu, Zhiyuan Liu, and Maosong Sun. 2024. | October 14-18, 2024 | , Bo Luo, Xiaojing Liao, Jun Xu, Engin Kirda, and David Lie |  |  |
| DebugBench: Evaluating Debugging Capability of Large Language Models. | (Eds.). ACM, 4554–4568. doi:10.1145/3658644.3670340 |  |  |  |
| arXiv:2401.04621 [cs.SE] https://arxiv.org/abs/2401.04621 | [49] Junjielong Xu, Ziang Cui, Yuan Zhao, Xu Zhang, Shilin He, Pinjia He, Liqun Li, |  |  |  |
| [44] PeiYu Tseng, ZihDwo Yeh, Xushu Dai, and Peng Liu. 2024. | Using LLMs to | Yu Kang, Qingwei Lin, Yingnong Dang, et al. 2024. Unilog: Automatic logging |  |  |
| Automate Threat Intelligence Analysis Workflows in Security Operation Centers. | via llm and in-context learning. In | Proceedings of the 46th ieee/acm international |  |  |
| https://api.semanticscholar.org/CorpusID:271270843 | conference on software engineering | . 1–12. |  |  |
| [45] Rafael Uetz, Marco Herzog, Louis Hackländer, Simon Schwarz, and Martin Henze. | [50] Junjielong Xu, Ruichun Yang, Yintong Huo, Chengyu Zhang, and Pinjia He. 2024. |  |  |  |
| 2023. You Cannot Escape Me: Detecting Evasions of SIEM Rules in Enterprise | Divlog: Log parsing with prompt enhanced in-context learning. In | Proceedings of |  |  |
| Networks. | CoRR | abs/2311.10197 (2023). arXiv:2311.10197 doi:10.48550/ARXIV. | the IEEE/ACM 46th International Conference on Software Engineering | . 1–12. |
| 2311.10197 | [51] Ming Xu, Chuanwang Wang, Jitao Yu, Junjie Zhang, Kai Zhang, and Weili Han. |  |  |  |
| [46] Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, | [n. d.]. Chunk-Level Password Guessing: Towards Modeling Refined Password |  |  |  |
| Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, et al. 2024. A survey on large | Composition Representations. In | Proceedings of 2021 ACM SIGSAC Conference |  |  |
| language model based autonomous agents. | Frontiers of Computer Science | 18, 6 | on Computer and Communications Security (CCS’21), Virtual Event, Republic of |  |
| (2024), 186345. | Korea, November 15 - 19, 2021 | . 5–20. doi:10.1145/3460120.3484743 |  |  |
| [47] Yue Wang, Weishi Wang, Shafiq R. Joty, and Steven C. H. Hoi. 2021. CodeT5: | [52] Zhuo Zhang, Wei You, Guanhong Tao, Guannan Wei, Yonghwi Kwon, and Xi- |  |  |  |
| Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Under- | angyu Zhang. 2019. BDA: practical dependence analysis for binary executables |  |  |  |
| standing and Generation. In | Proceedings of the 2021 Conference on Empirical | by unbiased whole-program path sampling and per-path abstract interpretation. |  |  |
| Methods in Natural Language Processing, EMNLP 2021, Virtual Event / Punta | Proc. ACM Program. Lang. | 3, OOPSLA (2019), 137:1–137:31. doi:10.1145/3360563 |  |  |
| Cana, Dominican Republic, 7-11 November, 2021 | , Marie-Francine Moens, Xuanjing | [53] Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, |  |  |
| Huang, Lucia Specia, and Scott Wen-tau Yih (Eds.). Association for Computational | Dale Schuurmans, Claire Cui, Olivier Bousquet, Quoc Le, and Ed Chi. 2023. |  |  |  |
| Linguistics, 8696–8708. doi:10.18653/V1/2021.EMNLP-MAIN.685 | Least-to-Most Prompting Enables Complex Reasoning in Large Language Models. |  |  |  |

arXiv:2205.10625 [cs.AI] https://arxiv.org/abs/2205.10625

---
title: "RapidPen: Fully Automated IP-to-Shell Penetration Testing with LLM-based Agents"
author: "Sho Nakatani"
creator: "arXiv GenPDF (tex2pdf:57610bf)"
pages: 15
---

# RapidPen: Fully Automated IP-to-Shell Penetration Testing with LLM-based Agents

> **作者**：Sho Nakatani
> **總頁數**：15 頁

---

## Page 1

RapidPen: Fully Automated IP-to-Shell Penetration Testing with LLM-based

We present RapidPen , a fully automated penetration test-

ing (pentesting) framework that addresses the challenge of

achieving an initial foothold ( IP-to-Shell ) without human in-

tervention. Unlike prior approaches that focus primarily on

post-exploitation or require a human-in-the-loop , RapidPen

leverages large language models (LLMs) to autonomously

discover and exploit vulnerabilities, starting from a single IP

address. By integrating advanced ReAct-style task planning

( Re ) with retrieval-augmented knowledge bases of successful

exploits, along with a command-generation and direct exe-

cution feedback loop ( Act ), RapidPen systematically scans

services, identifies viable attack vectors, and executes targeted

exploits in a fully automated manner.

In our evaluation against a vulnerable target from the Hack

The Box platform, RapidPen achieved shell access within

200–400 seconds at a per-run cost of approximately $0.3–

$0.6, demonstrating a 60% success rate when reusing prior

“success-case” data. These results underscore the potential

of truly autonomous pentesting for both security novices and

seasoned professionals. Organizations without dedicated secu-

rity teams can leverage RapidPen to quickly identify critical

vulnerabilities, while expert pentesters can offload repetitive

tasks and focus on complex challenges. Ultimately, our work

aims to make penetration testing more accessible and cost-

arXiv:2502.16730v2 [cs.CR] 14 Feb 2026 efficient, thereby enhancing the overall security posture of

modern software ecosystems.

1 Introduction

Penetration testing (pentesting) typically begins with its most

system. Once an attacker—or in this case, a testing plat-

form—gains an initial foothold, subsequent post-exploitation

tasks such as privilege escalation, credential theft, lateral

movement, and data exfiltration become significantly more

feasible. Although the initial foothold phase in penetration

Agents

Sho Nakatani

SecDevLab Inc.

exploits and social engineering. Consequently, it is essential

to assess post-exploitation risks under the realistic assumption

that a compromise may occur. The faster a testing process

can confirm initial access, the more effectively it can allocate

time to deeper post-exploitation stages before “running out

of clock.”

Despite advances in automation, fully autonomous solu-

tions for identifying initial compromise vectors remain elu-

sive. In many cases, sophisticated pentesting still demands

substantial human expertise, time, and cost. Recent advance-

ments in large language models (LLMs) have driven progress

in automating pentesting tasks, such as vulnerability scanning

and post-exploitation. However, the initial-access phase has

received comparatively less attention. Existing approaches

that incorporate LLMs often rely on a human-in-the-loop to

validate generated scans and exploits or to guide testing when

ambiguities arise [6]. While this approach may suit seasoned

pentesters, it presents a significant barrier for software devel-

opers and system operators with limited security expertise,

who may struggle to evaluate or refine the LLM’s recom-

mendations. Moreover, prior research has identified two key

challenges to full automation [26]: the vast search space of

potential entry points and the highly target-specific nature of

exploits.

In this work, we focus on IP-to-Shell testing: given only

a target IP address, an autonomous system must obtain a

shell without human intervention. Our goal is to develop

a high-speed, low-cost solution that significantly simplifies

penetration testing for both security professionals and non-

specialists alike.

Comparing highly skilled human penetration testers with ex-

isting human-in-the-loop systems [6], we hypothesize that

two key design choices can facilitate autonomous, robust, and

efficient initial infiltration:

1

| Abstract | equally daunting, especially given the risks posed by zero-day |  |  |  |
| --- | --- | --- | --- | --- |
| critical and challenging phase: | initial infiltration | of a target | Research Questions (RQs) |  |
| testing is challenging, preventing | all | infiltration attempts is | RQ1: | Can reusing “success cases” (i.e., past experiences |

---

## Page 2

with successful scans and exploit paths) enhance the Paper Outline. This paper is structured as follows: Sec-

speed and reliability of initial-access automation? tion 2 reviews the fundamentals of penetration testing and

Building on these ideas, we propose an LLM-based pentest-

ing agent, RapidPen , which requires no human intervention

beyond specifying a single target IP [15]. We further broaden

the scope of our investigation by posing the following research

questions:

RQ3: How does the time-to-compromise achieved by Rapid-

pare to manual penetration testing? Are they low enough

While our system is still in the early stages of development,

we validate the feasibility of fully automated IP-to-Shell ex-

ploitation on a vulnerable target from the Hack The Box ( HTB )

platform [1]. Specifically, we achieve:

• A 60% success rate when leveraging past “success-case”

data for the same class of vulnerability;

• A per-run cost of only $0.3–$0.6 to conduct a fully auto-

the benefits of success-case knowledge ( RQ1 ) and iterative

command refinement ( RQ2 ). We also provide a preliminary

teams without dedicated security staff. We also envision

tion testing automation tools, RapidPen primarily achieves its

posture of modern software ecosystems.

2

the evolving landscape of AI-driven automation. Section 3

tion 5 details our prototype implementation and core technical

choices. Section 6 describes our experimental setup and dis-

cusses the results of testing RapidPen on a vulnerable target.

Finally, Section 9 summarizes the key findings and outlines

future directions for enhancing RapidPen’s capabilities and

impact.

identifying and validating vulnerabilities in systems and net-

works before malicious actors can exploit them. It typically

works such as the Penetration Testing Execution Standard

(PTES) [21] or the MITRE ATT&CK model [5]. Although

different organizations may use slightly varying terminology,

a common workflow includes:

• Reconnaissance (Recon) – Gathering preliminary in-

formation about the target, such as domain names, IP

address ranges, and publicly available data. Effective

fying potential entry points.

automated probes on discovered services, ports, and con-

or anomalies.

the system.

ecosystems.

| RQ2: | Does iterative command refinement—where the sys- | defines our threat model, scope, and assumptions, clarify- |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tem analyzes failures and regenerates commands until | ing RapidPen’s operational boundaries. Section 4 presents |  |  |  |  |  |  |
| successful—result in a higher probability of exploitation | the high-level architecture of RapidPen, including its ReAct- |  |  |  |  |  |  |
| success? | based modules and retrieval-augmented workflow. Next, Sec- |  |  |  |  |  |  |
| Pen compare to that of a skilled human pentester? | 2 | Background and Motivation |  |  |  |  |  |
| RQ4: | How do the automation costs (in dollars per test) com- | 2.1 | Overview of Penetration Testing |  |  |  |  |
| to make automated solutions widely practical? | Penetration testing (pentesting) is a structured process for |  |  |  |  |  |  |
| Contributions and Scope | involves multiple phases, which align with well-known frame- |  |  |  |  |  |  |
| • Typical end-to-end compromise in | 200–400 seconds | ; | reconnaissance can guide subsequent actions by identi- |  |  |  |  |
| mated test. | • | Scanning (Enumeration) | – Conducting deeper, often |  |  |  |  |
| These promising results support our hypotheses regarding | figurations. Tools like | nmap | can identify vulnerabilities |  |  |  |  |
| analysis relevant to | RQ3 | and | RQ4 | , comparing automated | • | Exploitation (Initial Access) | – Leveraging discovered |
| testing speed and cost with expert-driven testing. | weaknesses to gain unauthorized access. This phase is |  |  |  |  |  |  |
| While RapidPen is designed to support organizations with | often the most challenging and high-stakes, as it deter- |  |  |  |  |  |  |
| limited security expertise, it is not exclusively intended for | mines whether an attacker can | successfully | compromise |  |  |  |  |
| its adoption by security teams and professional penetration | • | Post-Exploitation | – Once an initial foothold is obtained, |  |  |  |  |
| testers, enabling them to offload straightforward assessments | security testers (or adversaries) may escalate privileges, |  |  |  |  |  |  |
| to RapidPen and focus their efforts on more complex, high- | move laterally, and explore deeper layers of the environ- |  |  |  |  |  |  |
| value testing scenarios. Like many other LLM-based penetra- | ment to assess the impact of a breach. |  |  |  |  |  |  |
| objectives by flexibly leveraging existing knowledge. How- | Penetration testing plays a crucial role in cybersecurity: rig- |  |  |  |  |  |  |
| ever, human expertise remains crucial for identifying novel | orous simulated attacks can expose complex weaknesses that |  |  |  |  |  |  |
| vulnerabilities that are not yet documented or well understood. | static code analysis or automated scanners might overlook. By |  |  |  |  |  |  |
| By providing a solution that benefits security-conscious | emulating real-world threats, pentesters help organizations |  |  |  |  |  |  |
| organizations and industries with minimal prior expertise in | prioritize remediation efforts and improve their overall se- |  |  |  |  |  |  |
| penetration testing, we aim to enhance the overall security | curity posture. overall security posture of modern software |  |  |  |  |  |  |

---

## Page 3

2.2 LLM-Driven Automation in General as BLADE [24] and AutoAttacker [28] extend automation

In recent years, large language models (LLMs) have rapidly

advanced in both capability and scope, enabling significant

progress in automating a wide range of tasks, including natu-

ral language processing, programming assistance, and more.

Early breakthroughs include transformer-based architectures

such as BERT [7], GPT-2/3 [18, 2], and T5 [19], which col-

lectively demonstrated how pre-trained models could perform

text classification, summarization, and translation with mini-

mal fine-tuning. Subsequent models like LaMDA [25] and

GPT-4 [16] have further increased parameter counts and the

sophistication of emergent behaviors, allowing for more com-

plex and context-aware interactions.

These advances have driven adoption across various appli-

cation domains:

• Code Generation and Debugging. Models such as

entire functions from natural language descriptions, ac-

celerating software development and improving produc-

tivity. Research also explores the use of LLMs for de-

bugging and static analysis to identify potential software

vulnerabilities.

• Task Planning and Reasoning. Recent advancements

integrate symbolic and factual reasoning with lan-

guage models, facilitating tasks such as chain-of-thought

prompting [12] and multi-step planning [29]. These im-

provements enable structured decision-making in scenar-

ios requiring multi-step execution and complex logic.

nificantly lowers the barrier to automating domain-specific

workflows, including cybersecurity-related tasks. Notably,

LLMs can parse tool outputs, synthesize commands, and ad-

2.3 Existing Research and Opportunities for

Improvement

Recent research has explored the application of LLMs to

automate various penetration testing tasks, from initial ac-

3

into post-exploitation, and Wintermute [9] highlights au-

tonomous Linux privilege escalation.

Despite these advancements, a key gap remains in achiev-

ing fast, fully automated initial infiltration . To date, most

approaches still rely on human-in-the-loop validation or focus

primarily on post-exploitation rather than providing a high-

speed, end-to-end framework for breaching a target. From a

software development and operations perspective, the critical

questions are often, “Can my system be infiltrated, and how

quickly can that happen?” Delivering an IP-to-Shell workflow

at practical speed and cost could provide significant value to a

broader audience, including security-conscious organizations

and industries lacking dedicated security teams.

In the following sections, we introduce an approach to

address this need. By focusing on the initial-access phase

3.1 Threat Model

The RapidPen agent is assumed to have minimal prior knowl-

edge of the target system:

• Target IP Only. The attacker (i.e., RapidPen) is pro-

vided only with the IP address of the machine under test,

without additional configuration details or vulnerability

disclosures.

• Shell Acquisition. In its current prototype, RapidPen

exploits vulnerabilities using the Metasploit Frame-

3.2 Assumptions

the RapidPen environment to enable VPN-based connectivity.

Beyond these basic networking requirements, no additional

external services or credentials are assumed.

3.3 Scope and Limitations

| • | Text Summarization and Translation. | LLMs trained | and aiming for fully automated, low-cost, high-speed penetra- |  |  |
| --- | --- | --- | --- | --- | --- |
| on large corpora can generate concise summaries of | tion testing, our work seeks to enhance overall cybersecurity |  |  |  |  |
| lengthy documents and translate text between multiple | and enable a wider range of users to incorporate real-world |  |  |  |  |
| languages, often surpassing traditional systems [2, 19]. | adversarial testing into their development processes. |  |  |  |  |
| Codex [3] can generate scaffolding code, unit tests, or | 3 | Threat Model and Problem Definition |  |  |  |
| Since LLMs essentially learn a broad “prior” from large- | work [20] ( | msfconsole | ) and considers a shell “ob- |  |  |
| scale text corpora, they can be adapted for novel tasks through | tained” once logs confirm that a reverse shell has been |  |  |  |  |
| well-crafted prompts. This | prompt engineering | paradigm sig- | successfully established. |  |  |
| just actions based on prior responses, making them particu- | RapidPen operates under the assumption that it can establish |  |  |  |  |
| larly well-suited for penetration testing scenarios requiring | TCP connections to the target system’s IP address. If neces- |  |  |  |  |
| multi-step, context-aware orchestration. | sary, an OpenVPN configuration file can be deployed within |  |  |  |  |
| cess to remediation. For example, | PentestGPT | [6] introduces | • | Pre-Scanning Recon Excluded. | Passive reconnaissance |
| an LLM-based framework for guided exploitation using a | steps, such as searching domain records or metadata |  |  |  |  |
| task-tree architecture, while | PenHeal | [11] focuses on vul- | leaks, are beyond the scope of this study. Instead, we |  |  |
| nerability discovery and mitigation strategies. Tools such | focus on active port scanning as the starting point. |  |  |  |  |

---

## Page 4

• No Post-Exploitation. RapidPen does not attempt priv- 4.2 PTT as a Core Data Model in the Re Mod-

ilege escalation or lateral movement once a shell is ac- ule

quired.

• No UDP-Based Attacks. This implementation is limited

to TCP-based targeting. UDP-based exploits and scans

are not considered in this study.

In this section, we describe the overall architecture of our

as RapidPen. We adopt the ReAct [29] paradigm, which con-

sists of a Re (task planning) module and an Act (command

detail the system architecture, how each module interacts, and

how failures are handled.

4.1 System Architecture

• RapidPen-vis : A separate visualization tool for moni-

toring intermediate processes and final reports. [15]

Figure 1: The high-level architecture of RapidPen, illustrat-

1

ing user inputs and outputs, the Re and Act modules, and

2

RapidPen-vis, a visualization tool for monitoring intermedi-

3

4

In prior work on PentestGPT [6], the concept of a Pentest-

dependencies between tasks. The tree evolves dynamically as

new tasks are generated, completed, or require backtracking

due to partial failures.

PTT Definition (from PentestGPT). A PTT is essentially

elements:

nodes.

3. Edges representing parent-child relationships (e.g., sub-

task expansions) that structure the penetration testing

workflow at multiple levels of detail.

nate tasks. In addition to the standard PentestGPT functional-

log summary. This allows for a clearer interplay between

the Act module outputs and the Re module’s reasoning

state.

3. JSON-based I/O. We consistently store and exchange

the PTT in JSON format, ensuring that the LLM oper-

ates within a strict schema. This prevents ambiguity or

“hallucination” when the LLM appends new tasks or

updates existing nodes. A simplified JSON schema is

provided in Listing 1.

Listing 1: Simplified PTT snippet with environment metadata,

subtask structure, and Act results.

{

" version ": "2" ,

" metadata ": {

| • | No Web-Based Attacks. | Although web vulnerabilities | ing Task Tree | (PTT) was introduced to structure the entire |  |
| --- | --- | --- | --- | --- | --- |
| can serve as entry points, the current system does not | penetration testing process as an | attributed tree | , where each |  |  |
| address them. Future work will explore extending Rapid- | node represents a task (e.g., port scanning, vulnerability test- |  |  |  |  |
| Pen to support web exploits. | ing, exploitation), and edges define the flow of reasoning or |  |  |  |  |
| 4 | Design Overview of RapidPen | a labeled tree (or attributed polytree) with the following key |  |  |  |
| fully automated penetration testing framework, referred to | 1. | Nodes (tasks) | with unique identifiers and optional child |  |  |
| execution) module, both supported by specialized | retrieval- | 2. | Attributes | assigned to each node, such as task descrip- |  |
| augmented generation (RAG) | [13] repositories. Below, we | tions, current statuses, and relevant parameters. |  |  |  |
| Figure 1 provides a high-level overview of RapidPen’s core | Our Extensions. | We integrate the PTT as the | core data |  |  |
| components. | model | in the | Re | (reasoning) module to structure and coordi- |  |
| • | Input | : The user provides the | target IP address | . | ity, we introduce the following enhancements: |
| • | Output | : RapidPen-vis displays penetration test progress | 1. | Environment Metadata. | Our PTT includes a dedicated |
| (e.g., logs, discovered vulnerabilities) and generates the | metadata | block capturing details about the penetra- |  |  |  |
| final reports, including the command used to obtain a | tion testing environment (e.g., attacker and target IP ad- |  |  |  |  |
| shell. | dresses, time stamps, test status). |  |  |  |  |
| • | Re and Act Modules | : These modules jointly implement | 2. | Act Results in Nodes. | Each task node maintains a his- |
| the ReAct loop, coordinating tasks and executing com- | tory of command executions, including the executed |  |  |  |  |
| mands. | command string, | exit_code | , | exit_class | , and a brief |
| ate processes and final reports. | 4 | " started_at ": | " 2025 -02 -13 T22 :01:52 Z" , |  |  |

---

## Page 5

| 5 | " finished_at ": | " 2025 -02 -13 T22 :08:00 Z" , |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 6 | " status ": | " SUCCESS " , |  |  |  |
| 7 | " attacker ": | { | " LHOST ": | " 10.10.14.22 " | } , |
| 8 | " target ": | { |  |  |  |
| 9 | " description ": | " HTB | Blue | machine " , |  |
| 10 | " RHOST ": | " 10.10.10.40 " |  |  |  |
| 11 | } |  |  |  |  |
| 12 | } , |  |  |  |  |
| 18 | " timeout_sec ": | 60 , |  |  |  |
| 19 | " exit_code ": | 0 , |  |  |  |
| 20 | " exit_class ": | " SUCCESS " , |  |  |  |
| 21 | " log_summary ": | "( omit )" |  |  |  |
| 22 | }] , |  |  |  |  |
| 23 | " subtasks ": | [ |  |  |  |
| 24 | ... |  |  |  |  |
| 25 | ] |  |  |  |  |
| 26 | } |  |  |  |  |

27 }

1. Re (Task Planning): Monitors current logs, prior task

outcomes, and “success-case” data to propose new tasks

or exploit paths.

2. Act (Command Execution): Issues commands to gather

information or launch attacks. Upon receiving logs, the

system refines or regenerates commands before feeding

outcomes back to Re .

Figures 2–4 illustrate how the Re module is divided into

submodules, while Figure 5 details the Act module’s work-

flow.

Figure 2: The Re module in RapidPen consists of the Re (L1)

Figure 4: The Re (L2) New Task Generation module gener-

begins by extracting command results from the last executed

sis, new tasks are generated and integrated into the planning

process.

Figure 5: The Act (L1) module processes runnable tasks

through three key stages: command generation, execution,

and log analysis. It leverages offensive security expertise to

generate commands, automates execution, and applies self-

correcting mechanisms when necessary. Successful execu-

tions produce a command result, while failed executions trig-

ger a feedback loop for improvement.

4.4 RAG for Offensive Security

5

| 13 | " root ": | { | Figure 3: The | Re (L1) PTT Planner | processes the command |  |
| --- | --- | --- | --- | --- | --- | --- |
| 14 | " id ": | "1" , | results from the last executed task to generate new tasks at |  |  |  |
| 15 | " title ": | " Reconnaissance " , | Level 2 (L2) in the PTT. These tasks are deduplicated using |  |  |  |
| 16 | " act_results ": | [{ | an LLM-based approach before being merged into the PTT, |  |  |  |
| 17 | " command ": | "( omit )" , | updating it from an old to a new state. |  |  |  |
| 4.3 | Layered ReAct Modules in RapidPen | ates new tasks based on historical success cases. The process |  |  |  |  |
| RapidPen’s execution logic follows the | ReAct | [29] paradigm, | task. An LLM queries relevant historical success cases, which |  |  |  |
| where: | are then analyzed to extract key insights. Based on this analy- |  |  |  |  |  |
| PTT Planner | and | Re (L1) PTT Prioritizer | submodules. The | While | ReAct | provides a general “reasoning–acting” pat- |
| PTT Planner is responsible for expanding and maintaining | tern, RapidPen enhances this approach with two special- |  |  |  |  |  |
| the PTT tree, while the PTT Prioritizer determines the next | ized | Retrieval-Augmented Generation (RAG) | repositories for |  |  |  |
| task to execute. | domain-specific commands and proven exploit steps: |  |  |  |  |  |

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

---

## Page 6

| 1. | Act (L1) Command Generation RAG: | A curated col- | or | FILE_NOT_FOUND | errors occur. Upon detecting these, |
| --- | --- | --- | --- | --- | --- |
| lection of 148 Markdown files from | HackTricks | [4], pri- | RapidPen employs a | fail-fast | strategy: it terminates the |
| marily focused on “Network Services Pentesting” (e.g., | current penetration test session and notifies the developer. |  |  |  |  |
| SMB, FTP, SSH). These documents provide typical scan | The rationale is that an external installation or environ- |  |  |  |  |
| commands, exploit techniques, and enumeration strate- | ment fix is required before continuing, and automated |  |  |  |  |
| gies relevant to the initial-access phase. The Command | retries would be ineffective. |  |  |  |  |

Generation module references these documents to gener-

ate commands via the LLM.

2. Re (L2) New Tasks (Success Cases) RAG: PTTs in

New Tasks (Success Cases) module generates a search

task execution. It then analyzes the retrieved PTT output

evaluates the logs to determine if the result is conclu-

sive. If the command fails or does not produce sufficient

evidence for further progress, the Act module refines or

repeats up to three times. If no success is achieved after

three attempts, RapidPen marks the corresponding task

as failed and reports this outcome to the Re module.

2. Handling Timeouts. In some cases, command execution

may hang indefinitely if the target server is unrespon-

sive. To prevent this, each command is assigned an initial

timeout (e.g., 30 seconds). When a TIMEOUT occurs, the

For example, it may replace an nmap port scan command

with rustscan for quicker execution. If no faster alter-

native exists, the system doubles the timeout threshold

3. Handling Missing Commands or Files. Since Act (L1)

Command Generation references HackTricks and other

sources, it may propose commands or reference files that

are not available in the Act (L1) Command Executor

environment. In such scenarios, COMMAND_NOT_FOUND

6

5 Implementation

built on top of Dify 1 . We run Dify locally to manage interac-

tions with multiple Large Language Model (LLM) endpoints.

ule (command generation and log analysis). Initially, some

5.2 RapidPen-vis

consisting of:

• Server-Side: A Python Flask application responsible for

rendering real-time test logs and final pentest summaries.

• Client-Side: A lightweight vanilla JavaScript frontend

that communicates with the Flask API to fetch and dis-

play pentesting progress graphically.

of penetration testing tasks.

Dify provides a secure Python execution environment called

Dify-Sandbox , which restricts system calls and external net-

work access within a controlled Docker container. However,

1 https://dify.ai/

2 https://smith.langchain.com/

| JSON format capturing successful pentesting sequences. | This section describes the prototype implementation of Rapid- |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Currently, this dataset includes two PTTs for the Blue | Pen. While Chapter 4 presented the overall design, here we |  |  |  |  |
| machine in Hack The Box [1]. Each file outlines step-by- | focus on the specific tools, infrastructure, and configurations |  |  |  |  |
| step instructions, from scanning to obtaining a shell. The | used to realize our fully automated pentesting workflow. |  |  |  |  |
| query for the RAG based on the results of the most recent | 5.1 | Prototype Setup and LLM Usage |  |  |  |
| to generate effective subtasks. | Currently, RapidPen exists as a | prototype | implementation |  |  |
| 4.5 | Feedback Cycle in Act Module | Additionally, we integrate LangSmith | 2 | with Dify to precisely |  |
| Figure 5 illustrates the feedback loop within the | Act | module, | measure and monitor LLM invocation costs. This setup en- |  |  |
| where command generation and execution are tightly coupled | ables tracking of API calls, token usage, and associated costs |  |  |  |  |
| with log analysis and error handling. After executing each | under realistic testing conditions. |  |  |  |  |
| command, the system interprets the outcome (e.g., | SUCCESS | , | Our system exclusively employs OpenAI’s | gpt-4o | [17] |
| TIMEOUT | , | COMMAND_NOT_FOUND | ) and determines whether to | as the underlying language model. Internally, we maintain |  |
| retry or escalate. The feedback loop follows these key poli- | 10 LLM instances | dedicated to the | Re | module (task plan- |  |
| cies: | ning and reasoning) and | 8 LLM instances | for the | Act | mod- |
| 1. | Three-Strike Retry Limit. | When commands are gener- | prompts were adapted from | PentestGPT | [6]; however, all |
| ated and executed in a cycle, the Log Analysis module | prompts have since been replaced with original designs. |  |  |  |  |
| regenerates the command and re-executes it. This cycle | For visualization and reporting, we provide | RapidPen-vis | , |  |  |
| next execution cycle begins with | Act (L1) Command | This interface allows operators to observe the automated ex- |  |  |  |
| Generation | searching for a faster alternative command. | ploit process, review execution logs, and track the overall state |  |  |  |
| to allow more time for execution. | 5.3 | Custom Dify-Sandbox |  |  |  |

---

## Page 7

| our | Act (L1) Command Executor | requires broader system ac- | Attacker Environment. | We executed the RapidPen orches- |
| --- | --- | --- | --- | --- |
| cess to execute real-world pentesting commands. To address | trator and | RapidPen-vis | on a local MacBook Pro (13-inch |  |
| this limitation, we implemented a custom Docker image that | M2, 24 GB RAM, macOS Sequoia 15.3.1). The | Dify | -based |  |
| maintains the same REST API interface as | Dify-Sandbox | , | RapidPen orchestration runs in Docker containers, including |  |
| but without restrictive sandbox policies. This customized con- | our custom sandbox for actual command execution. |  |  |  |

tainer is integrated into our docker compose setup as a direct

replacement for the official Dify-Sandbox. It processes the

same API calls for command execution while permitting the

By leveraging this custom sandbox implementation, we

and extensible, allowing for future experiments and improve-

6 Evaluation

machine from Hack The Box [1], designed to validate Rapid-

Pen’s ability to establish an initial foothold (IP-to-Shell) in

an early-stage prototype. Future work will extend these ex-

periments to a broader set of targets.

6.1 Objectives and Questions

Our evaluation seeks to answer the following key questions:

1. Success Rate: How often does RapidPen successfully

achieve initial access (shell) on a known vulnerable ma-

chine?

2. Time and Bottlenecks: How long does an average run

take, and which modules in RapidPen consume the most

time?

3. LLM Cost: What is the cost of an automated penetration

test in terms of LLM usage?

nism in the Act module (cf. Section 4.5) function in

practice, and what role does the Re (L2) New Tasks (Suc-

6.2 Experimental Setup

execution (RCE).

7

6.2.1 Testing Two Configurations

relied solely on scanning and standard exploit references,

without leveraging pre-recorded successful sequences.

For each run, we reset the environment, then launched

ing metrics:

• Outcome: Success (obtained a shell) or Failure .

• #Steps: Number of PTT expansions initiated by the Re

(L1) PTT Planner , from start to success/failure.

• Elapsed Time: Total wall-clock time from test initiation

to termination.

6.3 Results

6.3.1 Overall Success Rates and Timings

With Success Cases (#1–10). In the left column of Figure 6,

we observe that 6 out of 10 runs successfully achieved a shell

on the Legacy machine. Runs that failed tended to get stuck

in repeated enumerations or timed out when nmap scanning

did not produce conclusive results quickly. When the test suc-

ceeded, execution time ranged from 200–400 seconds, with a

time.

system succeeded in only 3 out of 10 runs. We also observed

more outlier runs that either timed out after multiple scanning

attempts or executed redundant exploit attempts. For instance,

below 350 seconds.

| necessary system calls and network interactions required for | To evaluate the impact of | Re (L2) New Tasks (Success Cases) |  |
| --- | --- | --- | --- |
| pentesting. | RAG | , we conducted two sets of experiments: |  |
| maintain compatibility with Dify’s workflow and Python ex- | • | With Success Cases Enabled (Runs #1–10): | The sys- |
| ecution mechanism while removing constraints that would | tem had access to a stored PTT reflecting successful |  |  |
| otherwise prevent valid pentesting operations. This dual ap- | exploitation steps on HTB “Blue” (which shares the |  |  |
| proach ensures that our local environment remains modular | MS17-010 vulnerability). |  |  |
| ments in pentest automation. | • | Without Success Cases (Runs #11–20): | The system |
| This section presents preliminary experiments on the | Legacy | RapidPen with a single target IP. We recorded the follow- |  |
| 4. | Behavioral Insights: | How does the feedback mecha- | moderate correlation between the number of steps and elapsed |
| cess Cases) RAG | (cf. Section 4.4) play in generating | Without Success Cases (#11–20). | In contrast, the right |
| effective exploit paths? | column of Figure 6 presents a less favorable outcome. The |  |  |
| Target Machine (HTB Legacy). | We selected the Hack The | Run #13 followed an excessively long sequence of unsuc- |  |
| Box “Legacy” machine as our primary target. This machine | cessful attack vectors. Consequently, the average failure time |  |  |
| features an older SMB server exposed on | tcp/445 | with the | was significantly higher, occasionally exceeding 400 seconds. |
| MS17-010 | (EternalBlue) vulnerability, enabling remote code | When an exploit succeeded, execution time was typically |  |

---

## Page 8

Figure 6: Impact of Re (L2) New Tasks (Success Cases) on Penetration Testing Efficiency. The left column (yellow) represents

runs with Success Cases enabled , while the right column (green) represents runs without Success Cases . Top Row: Elapsed

time (in seconds) per run. Runs with Success Cases tend to complete faster, while runs without them exhibit greater variance and

some failures exceeding 1200 seconds (forcefully terminated). Bottom Row: Number of steps taken (PTT expansions) before

success or failure. Runs without Success Cases often require more steps, indicating inefficient task selection. The vertical dashed

line separates successful and failed runs , highlighting that the failure rate is higher without Success Cases (3/10 success)

compared to with Success Cases (6/10 success) .

vulnerability exploited by HTB “Blue.” Although the exact

pate that it will still accelerate the identification of effective

completed faster.

• Failure Causes:

1. Runs #1, #16, #18, and #20: Act (L1) Com-

OTHERS errors.

8

ation generated inappropriate commands for the

exploit port 139. After exceeding 1200 seconds,

5. Run #14: Re (L1) PTT Prioritizer generated a hal-

lucinated non-leaf task in the PTT, causing a vali-

dation error in the Act module.

generalizes.

| 6.3.2 | Observations and Discussion | 2. Runs #4, #6, and #17: | Act (L1) Command Gener- |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| The presence of | Success Cases | significantly improved the | given tasks, leading to | OTHERS | , | FILE_NOT_FOUND | , |
| success rate, as the Legacy machine shares the same SMBv1 | and | COMMAND_NOT_FOUND | errors. |  |  |  |  |
| environment differs slightly, the fundamental MS17-010 ex- | 3. Run #9: | Act (L1) Command Execution | failed to |  |  |  |  |
| ploit steps stored in the PTT closely align with the real target’s | execute the | enum4linux | command on port 139. |  |  |  |  |
| requirements. For more diverse vulnerabilities, we expect a | Act (L1) Log Analysis | classified it as an | OTHERS |  |  |  |  |
| lower direct transferability of RAG data; however, we antici- | error, triggering the fail-fast mechanism. |  |  |  |  |  |  |
| enumeration and exploitation paths. | 4. Run #13: The system continuously attempted to |  |  |  |  |  |  |
| • | Task Steps vs. Time: | Runs with fewer steps generally | execution in Dify stalled. |  |  |  |  |
| mand | Generation | produced | smbclient | com- | • | Future Generalization: | We plan to extend testing to |
| mands with incorrect parameters, resulting in | machines with partially overlapping but not identical |  |  |  |  |  |  |
| COMMAND_NOT_FOUND | , | FILE_NOT_FOUND | , | and | vulnerabilities to assess how well the success-case RAG |  |  |

---

## Page 9

| Figure 7: Module-wise breakdown of elapsed time per run | Figure 8: Module-wise breakdown of LLM cost per run with |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| with | Re (L2) New Tasks (Success Cases) | enabled. Each bar | Re (L2) New Tasks (Success Cases) | enabled. Each bar repre- |  |  |
| represents the total execution time for a single run, with dif- | sents the total LLM cost (in USD) for a single run, with dif- |  |  |  |  |  |
| ferent colors indicating each module’s contribution. | Re (L1) | ferent colors indicating the cost contribution of each module. |  |  |  |  |
| PTT Planner | (red) accounts for a significant portion of the | Re (L1) PTT Planner | (red) incurs the highest cost, followed |  |  |  |
| total time, followed by | Act (L1) Command Execution | (blue). | by | Act (L1) Command Execution | (blue) and | Act (L1) Log |

Analysis (purple).

6.4 Module-Wise Time and Cost Breakdown

To gain deeper insights, we instrumented the runs (particularly

in the with Success Cases scenario) to measure each module’s

1

contribution to the total runtime and LLM costs. 2

5

subtasks from Re (L2) New Tasks (Success Cases) .

6

The current cost and execution time are practical for tar-

7

geted penetration testing scenarios. However, further opti-

8

mization is possible by reducing large PTT inputs (which

Act Feedback Examples. As described in Section 4.5, the

Act module attempts to recover from command failures by

multiple runs, we observed that when an nmap scan timed out, 10

Role of Re (L2) New Tasks (Success Cases). Section 4.4 13

introduced the New Tasks (Success Cases) RAG , where Rapid- 14

Pen references a stored success PTT from HTB “Blue.” 15

9

Listing 2: Input to Re (L2) New Tasks (Success Cases) in

Legacy (last executed task)

{

" id ": " 1.3.1.4 " ,

" status ": " completed " ,

" act_results ": [

{

" command ": " nmap -p 445 -vv -Pn

, → -- script =

, → smb - vuln - ms07 -029. nse ,

, → smb - vuln - ms08 -067. nse ,

, → smb - vuln - ms10 -061. nse ,

, → smb - vuln - ms17 -010. nse

, → 10.10.10.4 " ,

" exit_code ": 0 ,

, → (CVE -2008 -4250) , MS17 -010

, → (CVE -2017 -0143) ."

}

] ,

...

| The runtime breakdown (see Figure 7) indicates that | Act | 3 | " title ": | " Enumerate | services | on | port | 445 " , |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (L1) Command Execution | contributes the most to total execu- | 4 | " detail ": | " Use | Nmap | to | enumerate | the |  |  |
| tion time, followed by | Re (L1) PTT Planner | . | , | → | service | running | on | port | 445 | on |
| Next, we analyze the LLM cost distribution (see Figure 8). | , | → | 10.10.10.4. | Check | for | SMB |  |  |  |  |
| Re (L1) PTT Planner | dominates the cost due to frequent PTT | , | → | vulnerabilities | such | as |  |  |  |  |
| expansions and the overhead of merging newly generated | , | → | EternalBlue ." , |  |  |  |  |  |  |  |
| can sometimes exceed 14KB) to the LLM and improving | , | → | smb - vuln - cve2009 -3103. nse , |  |  |  |  |  |  |  |
| error-handling mechanisms. | , | → | smb - vuln - ms06 -025. nse , |  |  |  |  |  |  |  |
| 6.5 | Behavioral Insights | , | → | smb - vuln - ms10 -054. nse , |  |  |  |  |  |  |
| either adjusting parameters or switching to alternative tools. In | 9 | " timeout_sec ": | 30 , |  |  |  |  |  |  |  |
| it was immediately replaced with | rustscan | . Additionally, | 11 | " exit_class ": | " SUCCESS " , |  |  |  |  |  |
| when an exploit attempt using | msfconsole | timed out, the | 12 | " log_summary ": | " TCP | port | 445 | on |  |  |
| system generally did not find an alternative command and | , | → | 10.10.10.4 | is | open , | and | the |  |  |  |
| instead increased the timeout from 30 to 60 seconds before | , | → | following | vulnerabilities | have |  |  |  |  |  |
| re-executing the command. | , | → | been | detected : | MS08 -067 |  |  |  |  |  |

---

## Page 10

16 } 36 " detail ": " Attempt to exploit the

, → identified MS17 -010

| When the last executed task from Listing 2 is passed to | , | → | vulnerability | on | port | 445 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Re (L2) New Tasks (Success Cases) | , a query is generated | , | → | of | 10.10.10.40 | using |  |  |  |
| for the | New Tasks (Success Cases) RAG | : | "Metasploit SMB | , | → | Metasploit . | Set | RHOST | to |
| exploit port 445 empty credentials" | . This retrieves | , | → | 10.10.10.40 , | RPORT | to | 445 , |  |  |
| the stored success-case PTT from the HTB Blue machine | , | → | and | LHOST | to | 10.10.14.22. " , |  |  |  |
| (Listing 3). | 37 | " status ": | " completed " , |  |  |  |  |  |  |
| 38 | " act_results ": | [{ |  |  |  |  |  |  |  |
| Listing 3: Success Case (PTT JSON) from the Blue machine | 39 | " command ": | " msfconsole | -q | -x |  |  |  |  |
| 1 | { | , | → | ' | use | exploit / | windows / |  |  |
| 2 | " version ": | "2" , | , | → | smb / |  |  |  |  |
| 3 | " metadata ": | { | , | → | ms17_010_eternalblue ; | set |  |  |  |
| 4 | " started_at ": | " 2025 -02 -13 T22 :17:00 Z" , | , | → | RHOST | 10.10.10.40; | set |  |  |
| 5 | " finished_at ": | " 2025 -02 -13 T21 :23:00 Z" , | , | → | RPORT | 445; | set | LHOST |  |
| 6 | " status ": | " SUCCESS " , | , | → | 10.10.14.22; | exploit | ' | " , |  |
| 7 | " attacker ": | { | 40 | " timeout_sec ": | 60 , |  |  |  |  |
| 8 | " LHOST ": | " 10.10.14.22 " | 41 | " exit_code ": | 0 , |  |  |  |  |
| 9 | } , | 42 | " exit_class ": | " SUCCESS " , |  |  |  |  |  |
| 10 | " target ": | { | 43 | " log_summary ": | " Port | 445 | on |  |  |
| 11 | " description ": | " HTB | Blue | machine " , | , | → | 10.10.10.40 | is | vulnerable |
| 12 | " RHOST ": | " 10.10.10.40 " | , | → | to | MS17 -010. | Windows | 7 |  |
| 13 | } | , | → | Professional | 7601 | Service |  |  |  |
| 14 | } , | , | → | Pack | 1 | x64 | was |  |  |
| 15 | " root ": | { | , | → | identified , | and | a |  |  |
| 16 | ... | , | → | Meterpreter | session | was |  |  |  |
| 17 | { | , | → | established ." |  |  |  |  |  |
| 18 | " id ": | " 1.3.1.3 " , | 44 | }] , |  |  |  |  |  |
| 19 | " title ": | " Enumerate | services | on | port | 45 | " subtasks ": | [] |  |
| , | → | 445 " , | 46 | } |  |  |  |  |  |
| 20 | " detail ": | " Use | Nmap | to | enumerate | the | 47 | ] |  |
| , | → | service | running | on | port | 445 | on | 48 | ... |
| , | → | 10.10.10.40. | Check | for | SMB | 49 | } |  |  |

, → vulnerabilities such as

| , | → | EternalBlue ." , | Based on the success case from HTB Blue, the | Re (L2) New |
| --- | --- | --- | --- | --- |
| 21 | " status ": | " failed " , | Tasks (Success Cases) | LLM generated the following output: |
| 22 | " act_results ": | [ |  |  |

Listing 4: Generated new tasks from Success Cases PTT.

| 23 | { |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 24 | " command ": | " nmap | -p | 445 | -vv | -Pn | 1 | { |  |  |  |  |  |  |
| , | → | -- script = | 2 | " Thought | process | ( Step1 )": | " First , | check |  |  |  |  |  |  |
| , | → | smb - vuln - ms17 -010. nse | , | → | whether | a | success - case | task | tree |  |  |  |  |  |
| , | → | 10.10.10.40 " , | , | → | exists . | The | provided | data | contains |  |  |  |  |  |
| 25 | " timeout_sec ": | 30 , | , | → | a | success - case | task | tree , | so |  |  |  |  |  |
| 26 | " exit_code ": | 0 , | , | → | proceed | to | the | next | step ." , |  |  |  |  |  |
| 27 | " exit_class ": | " SUCCESS " , | 3 | " Thought | process | ( Step2 )": | " Find | a | task |  |  |  |  |  |
| 28 | " log_summary ": | " Port | 445 | on | , | → | in | the | success - case | task | tree |  |  |  |
| , | → | 10.10.10.40 | is | open , | and | , | → | similar | to | the | most | recent | executed |  |
| , | → | the | Microsoft | SMBv1 | server | , | → | task . | In | this | case , | the | latest | task |
| , | → | has | a | remote | code | execution | , | → | involves | port | 445 , | and | the |  |
| , | → | vulnerability | ( MS17 -010 , | , | → | success - case | task | tree | also |  |  |  |  |  |
| , | → | CVE -2017 -0143) ." | , | → | contains | detailed | information | about |  |  |  |  |  |  |
| 29 | } , | , | → | port | 445. | Specifically , | task | ID |  |  |  |  |  |  |
| 30 | ... | , | → | ' | 1.3.1.3 | ' | and | its | subtasks | are |  |  |  |  |
| 31 | ] , | , | → | related | to | port | 445. | Based | on |  |  |  |  |  |
| 32 | " subtasks ": | [ | , | → | these , | generate | new | tasks ." , |  |  |  |  |  |  |
| 33 | { | 4 | " newTasks ": | [ |  |  |  |  |  |  |  |  |  |  |
| 34 | " id ": | " 1.3.1.3.1 " , | 5 | { |  |  |  |  |  |  |  |  |  |  |
| 35 | " title ": | " Exploit | SMBv1 | 6 | " title ": | " Exploit | SMBv1 | Vulnerability |  |  |  |  |  |  |
| , | → | Vulnerability | MS17 -010 " , | , | → | MS17 -010 " , |  |  |  |  |  |  |  |  |

10

---

## Page 11

7 " detail ": " Attempt to exploit the 7 Discussion

, → identified MS17 -010

, → 10.10.10.4 using Metasploit .

, → Set RHOST to 10.10.10.4 , RPORT

, → 10.10.14.22. " ,

8 " origin ": {

9 " reason ": " The previous check

, → confirmed the presence of

11 } ,

14 " detail ": " After exploiting the SMBv1

, → vulnerability , verify access to

, → 10.10.10.4 by checking for a

, → shell or other indicators of

19 ]

20 }

By leveraging the success case from the HTB Blue ma-

able to generate appropriate tasks, demonstrating the effec-

tiveness of using prior success cases for guided penetration

• LLM Cost: Typically under $0.60 per run, with the Re

(L1) PTT Planner module contributing the most.

Feedback Mechanism

ule (Section 4.5) significantly reduces the need for human

intervention. As long as the tasks assigned by the Re module

are appropriate, the Act module persistently re-generates and

testing.

encountering specific errors, such as COMMAND_NOT_FOUND ,

FILE_NOT_FOUND , and OTHERS . While this approach pre-

vents unnecessary retries and repeated failures, it can also

sary. Such refinements would further enhance the system’s

robustness and adaptability in real-world scenarios.

cess Cases

Cases accelerates exploit discovery when the target vulnerabil-

tests. For example, referencing the MS17-010 exploit path

However, handling scenarios where no relevant Success

may require more advanced reasoning beyond merely “copy-

ing” from past success. While our current approach lever-

ages the LLM’s internal knowledge and a RAG-based reposi-

11

| , | → | vulnerability | on | port | 445 | of | 7.1 | Benefits and Future Directions of the Act |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| , | → | to | 445 , | and | LHOST | to | The self-reliant feedback cycle implemented in the | Act | mod- |
| , | → | MS17 -010 | vulnerability | on | refines commands, interprets resulting logs, and explores alter- |  |  |  |  |
| , | → | port | 445 , | enabling | an | exploit | native strategies when errors occur. This design choice allows |  |  |
| , | → | attempt ." | RapidPen to continue progressing without manual oversight, |  |  |  |  |  |  |
| 10 | } | enhancing its ability to achieve fully automated penetration |  |  |  |  |  |  |  |
| 12 | { | However, the current fail-fast mechanism employed by |  |  |  |  |  |  |  |
| 13 | " title ": | " Verify | System | Access " , | the | Act | module causes the entire process to terminate upon |  |  |
| , | → | successful | exploitation ." , | abruptly halt the penetration test in cases where partial re- |  |  |  |  |  |
| 15 | " origin ": | { | mediation—such as installing missing packages or updating |  |  |  |  |  |  |
| 16 | " reason ": | " Verification | is | outdated command syntax—would suffice. |  |  |  |  |  |
| , | → | necessary | to | ensure | that | the | Future improvements should modify both | Command Gen- |  |
| , | → | exploit | successfully | provided | eration | and | Command Execution | to address these errors dy- |  |
| , | → | access | to | the | target | system ." | namically. A more nuanced error-handling strategy should |  |  |
| 17 | } | categorize failures, apply targeted retries or fixes, and reserve |  |  |  |  |  |  |  |
| 18 | } | immediate termination for cases where it is strictly neces- |  |  |  |  |  |  |  |
| chine, which shares the same vulnerability, the system was | 7.2 | Advantages and Limitations of Using Suc- |  |  |  |  |  |  |  |
| testing. | Our experiments indicate that RapidPen’s use of Success |  |  |  |  |  |  |  |  |
| 6.6 | Summary of Findings | ity closely matches those in previously recorded penetration |  |  |  |  |  |  |  |
| Our preliminary evaluation indicates that RapidPen can | from the “Blue” machine on Hack The Box (HTB) was effec- |  |  |  |  |  |  |  |  |
| achieve consistent IP-to-Shell exploits on a known vulner- | tive against the “Legacy” machine, which shares a similarly |  |  |  |  |  |  |  |  |
| able target: | vulnerable SMBv1 service. This demonstrates that reusing |  |  |  |  |  |  |  |  |
| • | Success Rate: | 60% with success-case RAG vs. 30% | existing exploit sequences can streamline scanning and ex- |  |  |  |  |  |  |
| without, across 10 trials each. | ploitation, leading to faster and more reliable outcomes. |  |  |  |  |  |  |  |  |
| • | Time-to-Shell: | On average, 200–400 seconds for suc- | Cases exist remains an open problem. Zero-day vulnera- |  |  |  |  |  |  |
| cessful runs. | bilities or configurations that have never been encountered |  |  |  |  |  |  |  |  |
| Though limited to a single machine and vulnerability type, | tory, a more powerful framework for abstracting exploit tech- |  |  |  |  |  |  |  |  |
| these results demonstrate the | Re (L2) New Tasks (Success | niques—enabling RapidPen to discover novel attack strate- |  |  |  |  |  |  |  |
| Cases) | approach’s potential and highlight the | Act | module’s | gies—will be essential for addressing unknown threats. De- |  |  |  |  |  |
| self-correcting behavior. We plan to broaden our scope with | signing and evaluating such a next-generation system is a |  |  |  |  |  |  |  |  |
| additional targets, diverse vulnerabilities, and larger user stud- | critical step toward making automated pentesting broadly ef- |  |  |  |  |  |  |  |  |
| ies in future work. | fective against new or rare vulnerabilities. |  |  |  |  |  |  |  |  |

---

## Page 12

7.3 Expanding the Attack Surface structure. Inspired by attack trees, the PTT decomposes en-

bilities often require specialized knowledge—ranging from

injection techniques to authentication bypass methods—and

may involve GUI-based testing beyond simple command-line

interactions. Incorporating these capabilities would likely

of autonomy for web exploits poses additional research and

Although the user explicitly provides a target IP address to

RapidPen, reducing the risk of scanning unrelated systems,

the possibility of misuse cannot be ignored. Any automated

exploit tool can be leveraged for malicious purposes if placed

in the wrong hands or configured improperly. Future devel-

opments should focus on access control, rate-limiting, and

formal usage policies—especially if the system transitions

from a research prototype to a commercial or open-source de-

ployment. Additionally, practical safeguards like monitoring

logs, validating the legitimacy of the target environment, and

enforcing strict network boundaries are pivotal for preventing

inadvertent attacks against unauthorized hosts.

Overall, while RapidPen lowers the barrier for automated

security testing, it underscores the need for responsible de-

ployment practices. Addressing legal and ethical ramifications

is essential to ensuring that the benefits of fully automated

pentesting do not come at the expense of broader cybersecu-

rity risks.

8 Related Work

12

gagements into sub-tasks (e.g., port scanning, service enumer-

pentesting tool.

8.1.2 Other LLM-Driven Pentesting Tools

Vulnerability Scanning Rather than Speed

rect human involvement, designed to identify a broad

range of vulnerabilities and propose mitigation strate-

gies. Although the paper does not explicitly confirm

automation of initial foothold attacks, it is possible that

PenHeal’s capabilities overlap with RapidPen in terms

of initial access. However, no evaluation is provided

regarding the time and cost required to achieve initial

access. In contrast, RapidPen focuses on demonstrat-

ing the most immediate security risk—namely, gaining

unauthorized shell access as quickly as possible—before

handing over control to established tools designed for

post-exploitation. While RapidPen does not yet provide

broad vulnerability coverage or automated remediation,

incorporating such features remains an area for future

exploration.

Tools That Focus on Post-Exploitation and Are Comple-

mentary to RapidPen

• BLADE [24] – B reaking L imits, A utomate D eep

E xploitation – an AI-driven pentesting agent built on

an autonomous agent framework (Microsoft’s Auto-

Gen [27]). BLADE autonomously orchestrates exploita-

LinPEAS for privilege escalation and John the Ripper

| Although RapidPen currently achieves fully automated IP- | ation, exploitation), allowing the LLM to maintain context |  |  |  |
| --- | --- | --- | --- | --- |
| to-Shell compromises, it does not yet address the post- | throughout testing. PentestGPT operates using three coordi- |  |  |  |
| exploitation phase. Privilege escalation, lateral movement, | nated modules: a | Reasoning | module (the "lead tester") that |  |
| and deeper analysis of the compromised environment repre- | updates the task tree and determines next steps, a | Generation |  |  |
| sent logical extensions for future work. In particular, tools like | module (the "junior tester") that proposes specific commands, |  |  |  |
| BLADE [24] and AUTOATTACKER [28] already explore | and a | Parsing | module to summarize tool output. |  |
| AI-assisted post-exploitation. Extending RapidPen to inte- | While PentestGPT automates attack planning, it requires |  |  |  |
| grate with such frameworks could broaden its applicability, | a human-in-the-loop to execute suggested commands and |  |  |  |
| enabling more comprehensive, end-to-end assessments. | correct errors. Users must review and refine commands before |  |  |  |
| Another important direction involves web exploits, which | execution, limiting its autonomy. Thus, PentestGPT functions |  |  |  |
| are currently absent from the system. Web-based vulnera- | more as a guided assistant rather than a fully autonomous |  |  |  |
| require RAG expansions to include relevant web exploita- | Beyond PentestGPT, several emerging tools utilize LLMs for |  |  |  |
| tion knowledge bases and potentially adapt the | Act | module | penetration testing, each focusing on different aspects of the |  |
| to handle browser automation. Achieving the same degree | workflow. These tools can be categorized as follows: |  |  |  |
| engineering challenges. | Tools that Automate Initial Access but Focus on Broad |  |  |  |
| 7.4 | Ethical and Safety Considerations | • | PenHeal | [11] – an AI agent that operates without di- |
| 8.1 | LLM-Based Penetration Testing | tion tasks by leveraging external tools and dynamic script |  |  |
| 8.1.1 | PentestGPT – Task Tree-Driven AI Pentesting | generation. For example, it uses pre-configured tools like |  |  |
| Recent research has explored using large language models | for credential cracking to achieve deeper system compro- |  |  |  |
| (LLMs) to automate penetration testing. | PentestGPT | [6] is | mise. Additionally, it includes agents for network scan- |  |
| a notable example: it leverages an LLM (GPT-3.5/GPT-4) to | ning and lateral movement, showcasing how multi-agent |  |  |  |
| guide the pentest process via a | Pentesting Task Tree (PTT) | AI systems can enhance penetration testing workflows. |  |  |

---

## Page 13

| • | AutoAttacker | [28] – an LLM-guided system designed | Meanwhile, tools like BLADE and AutoAttacker specialize |
| --- | --- | --- | --- |
| to implement automated “hands-on-keyboard” cyber- | in post-exploitation rather than initial access, making them |  |  |
| attacks in post-breach scenarios. | complementary rather than competing solutions. |  |  |

• Wintermute [9] – an LLM-driven Linux privilege es-

8.2 Reinforcement Learning-Based Penetra-

• Hu et al. [10] developed a deep RL framework for auto-

mated penetration testing, modeling scanning, exploita-

tion, and lateral movement as a reinforcement learning

• Liu et al. [14] proposed a hierarchical RL agent for

large-scale network penetration, improving efficiency by

splitting attack planning into multiple levels.

tomation of initial access but suffered from overfitting

to training environments.

tack paths, its major drawback is poor generalization beyond

training data, requiring extensive retraining for new environ-

ments.

8.3 Comparison with RapidPen

Degree of Automation: RapidPen is designed for full au-

tomation of initial access, requiring no human intervention

once launched. This sets it apart from PentestGPT, which

requires users to review and execute commands manually. In

mal setup overhead.

Scope of Initial Access Techniques: RapidPen focuses on

achieving unauthorized shell access as quickly as possible,

vides recommendations, RapidPen directly executes exploits.

13

commands, RapidPen autonomously performs the entire at-

tack process. Additionally, tools like Autonomous Web Ex-

ploitation target a different domain (web applications), leaving

and organizations looking to assess their exposure to real-

world attack scenarios.

ReAct-style task planning with retrieval-augmented exploit

knowledge and iterative command generation/execution loops,

RapidPen systematically scans for vulnerabilities and exploits

them, demonstrating promising results on a vulnerable Hack

its current prototype form.

• Proposal and Implementation. We described the de-

sign of RapidPen’s modular Re and Act subsystems, high-

lighting how each leverages large language models and

curated knowledge repositories.

• Empirical Evaluation. Preliminary experiments on a

known vulnerable target demonstrated up to a 60% suc-

cess rate for shell acquisition within 200–400 seconds ,

with a per-run cost of approximately $0.3–$0.6 .

automated pentesting.

9.2 Future Directions

capabilities in several areas:

| calation tool that evaluates model performance in fully | Usability for Non-Experts: | RapidPen is explicitly de- |  |  |  |
| --- | --- | --- | --- | --- | --- |
| automated exploit scenarios. It highlights strengths and | signed for usability by non-experts, enabling security assess- |  |  |  |  |
| weaknesses in autonomous security workflows, focusing | ments without deep penetration testing expertise. Unlike Pen- |  |  |  |  |
| on post-exploitation. | testGPT, which still requires expert validation of generated |  |  |  |  |
| tion Testing Approaches | gaps in usability for broader infrastructure pentesting. |  |  |  |  |
| Deep reinforcement learning (RL) | has also been explored | Overall, RapidPen distinguishes itself by combining | full |  |  |
| for autonomous pentesting. RL-based systems learn attack | automation, speed, and accessibility | . It provides a | highly |  |  |
| sequences by interacting with an environment and optimizing | practical and deployable solution | for automated initial ac- |  |  |  |
| for successful exploits. Key contributions include: | cess testing, making it a valuable tool for security practitioners |  |  |  |  |
| problem. | 9 | Conclusion and Future Work |  |  |  |
| • | Garrad and Unnikrishnan | [8] applied RL to vehicular | In this paper, we introduced | RapidPen | , a fully automated |
| ad-hoc network (VANET) penetration testing, demon- | penetration testing framework aimed at achieving an | IP-to- |  |  |  |
| strating AI-driven attack sequence learning. | Shell | compromise without human intervention. By combining |  |  |  |
| • | DeepExploit | [22, 23], an early RL-powered pentesting | The Box target. Our evaluation shows that RapidPen can |  |  |
| tool integrated with Metasploit, demonstrated full au- | achieve shell access within minutes at a modest cost, even in |  |  |  |  |
| While RL-based pentesting can autonomously uncover at- | 9.1 | Summary of Contributions |  |  |  |
| contrast, RL-based systems like DeepExploit require exten- | • | Key Insights. | Our results highlight how reusing “success |  |  |
| sive training and tuning before deployment, making RapidPen | cases” and employing self-correcting command loops |  |  |  |  |
| a more practical choice for real-world pentesting with mini- | significantly enhance the reliability and efficiency of |  |  |  |  |
| covering a broad range of network and system-level exploita- | Expanding the Scope. | Although RapidPen is currently de- |  |  |  |
| tion techniques. Unlike PentestGPT, which primarily pro- | signed for TCP-based initial access, we plan to extend its |  |  |  |  |

---

## Page 14

• Web and UDP Attacks. Expanding support for web- References

based exploits, including injection and authentication

• Beyond Initial Access. Integrating passive reconnais-

sance and post-exploitation workflows (e.g., lateral

movement, privilege escalation) by interfacing RapidPen

with complementary automated or manual tools.

within RapidPen’s existing scope:

• Optimized PTT Input to LLM. Pruning irrelevant

increasing speed and lowering costs, particularly in Re

Pen automatically re-runs failed test attempts. This feature

will be user-configurable, allowing for a balance between

execution time, cost, and a higher probability of success.

Towards Real-World Deployment. We aim to make Rapid-

Pen accessible to a broader audience—whether through com-

mercial offerings or as an open-source project—so that soft-

ware teams and security professionals alike can benefit from

automated initial-access testing. At the same time, we must

design appropriate safeguards to minimize the risk of misuse

and ensure that RapidPen is deployed exclusively in legiti-

9.3 Closing Remarks

14

URL : https://www.hackthebox.com/ .

[2] Tom Brown et al. “Language Models are Few-

Shot Learners”. In: Advances in Neural Informa-

tion Processing Systems . Ed. by H. Larochelle et

al. Vol. 33. Curran Associates, Inc., 2020, pp. 1877–

1901. URL : https : / / proceedings . neurips .

pdf .

HackTricks-wiki/hacktricks .

org/ .

nessing large language models for automated penetra-

[7] Jacob Devlin et al. BERT: Pre-training of Deep Bidi-

rectional Transformers for Language Understanding .

2019. arXiv: 1810.04805 [cs.CL] . URL : https://

arxiv.org/abs/1810.04805 .

[8] Phillip Garrad and Saritha Unnikrishnan. “Reinforce-

ment learning in VANET penetration testing”. In: Re-

sults in Engineering 17 (2023), p. 100970. ISSN : 2590-

1230. DOI : https://doi.org/10.1016/j.rineng.

2023.100970 . URL : https://www.sciencedirect.

com/science/article/pii/S259012302300097X .

Penetration Testing with Large Language Models”. In:

Proceedings of the 31st ACM Joint European Software

Engineering Conference and Symposium on the Foun-

pp. 2–10. DOI : 10 . 1109 / EuroSPW51379 . 2020 .

00010 .

| bypass techniques, and exploring UDP-based vulnerabil- | [1] | Hack The Box. | Hack The Box: The #1 Cybersecu- |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ities as logical next steps. | rity Performance Center | . Accessed: 2025-02-21. 2025. |  |  |  |  |  |
| Refining the Current Implementation. | Our short-term de- | cc / paper _ files / paper / 2020 / file / |  |  |  |  |  |
| velopment focuses on improving reliability and performance | 1457c0d6bfcb4967418bfb8ac142f64a | - | Paper | . |  |  |  |
| • | Robust Error Handling. | Strengthening the | Act (L1) | [3] | Mark Chen et al. | Evaluating Large Language Models |  |
| Command Execution | and | Act (L1) Log Analysis | pipeline | Trained on Code | . 2021. arXiv: | 2107.03374 [cs.LG] | . |
| to prevent premature termination from unexpected fail- | URL | : | https://arxiv.org/abs/2107.03374 | . |  |  |  |
| ures and clarify when retries or alternative commands | [4] | HackTricks Contributors. | HackTricks | . Accessed: 2025- |  |  |  |
| are appropriate. | 02-21. | 2025. | URL | : | https : / / github . com / |  |  |
| fields or tasks when feeding | Pentesting Task Tree | (PTT) | [5] | The MITRE Corporation. | MITRE ATT&CK | . Accessed: |  |
| JSON data to the LLM to reduce context size, thereby | 2025-02-21. 2025. | URL | : | https://attack.mitre. |  |  |  |
| (L1) PTT Planner | . | [6] | Gelei Deng et al. “PentestGPT: Evaluating and har- |  |  |  |  |
| Execution Modes and Trade-offs. | To improve success | tion testing”. In: | 33rd USENIX Security Symposium |  |  |  |  |
| rates, we plan to introduce an “auto-retry” mode, where Rapid- | (USENIX Security 24) | . 2024. |  |  |  |  |  |
| mate, authorized environments. | [9] | Andreas Happe and Jürgen Cito. “Getting pwn’d by AI: |  |  |  |  |  |
| By focusing on | IP-to-Shell | automation, our work provides | dations of Software Engineering | . ESEC/FSE 2023. San |  |  |  |
| both security novices and experts with a powerful tool for | Francisco, CA, USA: Association for Computing Ma- |  |  |  |  |  |  |
| quickly identifying critical exposures. We envision that Rapid- | chinery, 2023, pp. 2082–2086. | ISBN | : 9798400703270. |  |  |  |  |
| Pen’s foundation in LLM-driven planning and execution can | DOI | : | 10.1145/3611643.3613083 | . | URL | : | https:// |
| serve as a stepping stone toward a new class of intelligent, | doi.org/10.1145/3611643.3613083 | . |  |  |  |  |  |
| extensible offensive security tools. As RapidPen matures, we | [10] | Zhenguo Hu, Razvan Beuran, and Yasuo Tan. “Auto- |  |  |  |  |  |
| hope it will stimulate further research into collaborative work- | mated Penetration Testing Using Deep Reinforcement |  |  |  |  |  |  |
| flows between humans and AI agents, ultimately strengthen- | Learning”. In: | 2020 IEEE European Symposium on |  |  |  |  |  |
| ing the security posture of modern software ecosystems. | Security and Privacy Workshops (EuroS&PW) | . 2020, |  |  |  |  |  |

---

## Page 15

| [11] | J. Huang and Q. Zhu. “PenHeal: A Two-Stage LLM | [24] | Isao Takaesu and Daiki Ichinose. “BLADE: A study |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Framework for Automated Pentesting and Optimal Re- | on automated penetration testing using autonomous AI |  |  |  |  |  |  |  |  |  |
| mediation”. In: | Proceedings of the Workshop on Au- | agents”. In: | AVTOKYO 2024 | . 2024. |  |  |  |  |  |  |
| tonomous Cybersecurity | . ACM, 2023, pp. 11–22. | [25] | Romal Thoppilan et al. | LaMDA: Language Models |  |  |  |  |  |  |
| [12] | Takeshi Kojima et al. | Large Language Models are Zero- | for Dialog Applications | . 2022. arXiv: | 2201 . 08239 |  |  |  |  |  |
| Shot Reasoners | . 2023. arXiv: | 2205.11916 [cs.CL] | . | [cs.CL] | . | URL | : | https : / / arxiv . org / abs / 2201 . |  |  |
| URL | : | https://arxiv.org/abs/2205.11916 | . | 08239 | . |  |  |  |  |  |
| [13] | Patrick Lewis et al. “Retrieval-Augmented Generation | [26] | Yunfei Wang et al. | A Unified Modeling Framework |  |  |  |  |  |  |
| for Knowledge-Intensive NLP Tasks”. In: | Advances | for Automated Penetration Testing | . 2025. arXiv: | 2502. |  |  |  |  |  |  |
| in Neural Information Processing Systems | . Ed. by | 11588 [cs.AI] | . | URL | : | https://arxiv.org/abs/ |  |  |  |  |
| H. Larochelle et al. Vol. 33. Curran Associates, Inc., | 2502.11588 | . |  |  |  |  |  |  |  |  |
| 2020, pp. 9459–9474. | URL | : | https://proceedings. | [27] | Qingyun Wu et al. | AutoGen: Enabling Next-Gen |  |  |  |  |
| neurips . cc / paper _ files / paper / 2020 / file / | LLM Applications via Multi-Agent Conversation | . 2023. |  |  |  |  |  |  |  |  |
| 6b493230205f780e1bc26945df7481e5 | - | Paper | . | arXiv: | 2308.08155 [cs.AI] | . | URL | : | https://arxiv. |  |
| pdf | . | org/abs/2308.08155 | . |  |  |  |  |  |  |  |
| [14] | Hongri Liu et al. “An Automated Penetration Test- | [28] | Jiacen Xu et al. | AutoAttacker: A Large Language |  |  |  |  |  |  |
| ing Framework Based on Hierarchical Reinforcement | Model Guided System to Implement Automatic Cyber- |  |  |  |  |  |  |  |  |  |
| Learning”. In: | Electronics | 13.21 (2024). | ISSN | : 2079- | attacks | . 2024. arXiv: | 2403 . 01038 [cs.CR] | . | URL | : |
| 9292. | DOI | : | 10.3390/electronics13214311 | . | URL | : | https://arxiv.org/abs/2403.01038 | . |  |  |

https://www.mdpi.com/2079-9292/13/21/4311 .

[29] Shunyu Yao et al. “ReAct: Synergizing reasoning

[15] Sho Nakatani. [Demo] RapidPen Automatically Gains and acting in language models”. In: arXiv preprint

a Shell (HTB Blue Machine) . Feb. 2025. DOI : 10 . arXiv:2210.03629 (2022).

5281/zenodo.14908250 .

[16] OpenAI et al. GPT-4 Technical Report . 2024. arXiv:

2303.08774 [cs.CL] . URL : https://arxiv.org/

abs/2303.08774 .

[17] OpenAI et al. GPT-4o System Card . 2024. arXiv: 2410.

21276 [cs.CL] . URL : https://arxiv.org/abs/

2410.21276 .

[18] Alec Radford et al. “Language Models are Unsuper-

vised Multitask Learners”. In: OpenAI (2019). Ac-

cessed: 2024-11-15. URL : https : / / cdn . openai .

com / better - language - models / language _

models _ are _ unsupervised _ multitask _

learners.pdf .

[19] Colin Raffel et al. “Exploring the limits of transfer

learning with a unified text-to-text transformer”. In: J.

Mach. Learn. Res. 21.1 (Jan. 2020). ISSN : 1532-4435.

[20] Rapid7. Metasploit Framework . Accessed: 2025-02-

21. 2025. URL : https : / / github . com / rapid7 /

metasploit-framework .

[21] The Penetration Testing Execution Standard. PTES

Technical Guidelines . Accessed: 2025-02-21. 2025.

URL : http://www.pentest-standard.org/index.

php .

[22] Isao Takaesu. “Deep Exploit”. In: DEF CON 26 . 2018.

[23] Isao Takaesu. “DeepExploit: Fully Automated Pen-

etration Testing Using Reinforcement Learning”. In:

CODE BLUE . 2019.

15

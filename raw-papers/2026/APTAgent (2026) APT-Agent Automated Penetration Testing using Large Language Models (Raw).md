---
title: "APT-Agent: Automated Penetration Testing using Large Language Models"
author: "William Guanting Li; Alsharif Abuadbba; Kristen Moore; Dan Dongseong Kim"
creator: "arXiv GenPDF (tex2pdf:a6404ea)"
pages: 11
---

# APT-Agent: Automated Penetration Testing using Large Language Models

> **作者**：William Guanting Li; Alsharif Abuadbba; Kristen Moore; Dan Dongseong Kim
> **總頁數**：11 頁

---

## Page 1

APT-Agent: Automated Penetration Testing using

Large Language Models

| William Guanting Li | Alsharif Abuadbba | Kristen Moore | Dan Dongseong Kim |
| --- | --- | --- | --- |
| University of Queensland | CSIRO Data61 | CSIRO Data61 | University of Queensland |
| Brisbane, Australia | Sydney, Australia | Melbourne, Australia | Brisbane, Australia |
| guanting.li@uq.edu.au | sharif.abuadbba@csiro.au | kristen.moore@csiro.au | dan.kim@uq.edu.au |

Abstract —Penetration testing is essential to securing modern components of pen-testing, LLMs reduce the burden on human

web infrastructures, yet traditional manual methods struggle operators and allow them to dedicate more time to critical

to keep pace with their scale and complexity. Large Language decision-making and complex threat analysis. Recent research

Models (LLMs) offer new opportunities for automating these

exfiltration. APT-Agent introduces a hybrid rectification module

to-end exploitation success rate, compared to 48.57% (Script

tion Testing, Cybersecurity

I. I NTRODUCTION

arXiv:2605.24949v1 [cs.CR] 24 May 2026 contribute to cognitive overload among security professionals,

diverting their focus from higher-order analysis and strategic

defense planning [3]. Taking these challenges into consid-

Large Language Models (LLMs) have demonstrated re-

markable capabilities in interpreting instructions, drawing in-

ferences, and generating coherent, domain-specific responses

general conversation, positioning them as promising tools

paths, module types (exploit/auxiliary/post), target platform

names, or payload identifiers [15], [16], [17]. As illustrated

in Fig. 1, these hallucinated Metasploit paths may point to

EXPLOIT Stage

scan result is {Nmap scan results}

LLM Output exploit/linux/ftp/vsftpd_234_backdoor

tasks, but existing approaches face two persistent challenges: has begun to explore the integration of LLMs into pen-

hallucination of technical entities and insufficient long-term con- testing workflows. Fang et al. [11], [12] demonstrated LLM

textual memory. To address these issues, we present APT-Agent, agents capable of autonomously discovering and exploiting

a fully automated LLM-driven penetration testing framework vulnerabilities in websites and one-day CVEs. Deng et al.

that systematically orchestrates reconnaissance, exploitation, and [13] introduced the Pentesting Task Tree (PTT) to structure

to recover hallucinated commands and a command-specific mem- LLM-driven decisions, while Xu et al. [14] proposed a Plan-

ory architecture to preserve operational context across multi-step ner, Navigator, Summarizer pipeline enhanced with retrieval-

attack sequences. We evaluate our APT-Agent on Metasploitable augmented generation (RAG), which also explored whether

2 against seven vulnerable services spanning web, database, LLMs can simulate hands-on-keyboard post-breach actions,

and network protocols. APT-Agent achieves an 84.29% end- including lateral movement, credential harvesting, and persis-

Kiddie) and 18.57% (PentestGPT) under matched conditions. By tence mechanisms. Despite these advances, current systems

reducing cognitive burden and minimizing reliance on human in- still consist of the following two key challenges:

tervention, APT-Agent represents a step toward scalable, reliable, Challenge #1: Hallucination of technical entities . LLMs

and cognitively efficient automation for penetration testing. frequently invent or misstate particular technical identifiers.

Index Terms —Automated Penetration Testing, LLM, Penetra- For example, exact command syntaxes, Metasploit module

In the realm of cybersecurity, penetration testing (pen- non-existent modules or to modules with incorrect semantics

testing) plays a vital role by proactively simulating authorized (wrong module type, wrong target, or mismatched options).

attacks to evaluate and strengthen the resilience of information This is not a trivial error: penetration testing relies on exact

systems [1]. However, as digital infrastructures continue to identifiers and parameter names. Even small inaccuracies, such

grow in scale and complexity, traditional manual approaches as a mistyped module path or incompatible payload, can

face significant limitations. These include challenges of scala- silently break automation, waste time, or trigger unintended

bility, dependence on scarce human expertise, and variability actions. Such errors undermine the reproducibility and safety

in outcomes across practitioners [2]. Such constraints not of LLM-guided security workflows and heighten legal and

only hinder timely and comprehensive assessments but also accountability risks when outputs are unverified.

| eration, automated approaches have the potential to address | Ground Truth | exploit/unix/ftp/vsftpd_234_backdoor |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| many | of | these | challenges | while | preserving | accuracy | and | LLM Prompt | Generate a Metasploit command to exploit |
| trustworthiness [4]. | a service based on the given Nmap scan result. The Nmap |  |  |  |  |  |  |  |  |
| [5], [6]. These strengths extend their applicability well beyond | Fig. 1. | Example of Hallucination |  |  |  |  |  |  |  |

for specialized technical domains such as cybersecurity [7], Challenge #2: Insufficient long-term contextual memory.

[8], [9], [10]. By automating routine and resource-intensive Multi-step penetration tests require preserving accurate, ver-

---

## Page 2

sioned state across actions (reconnaissance → exploitation → testing systems [13], [14], [22]. The source code for APT-

exfiltration). Many LLM-assisted systems lose or overwrite Agent is available in our GitHub repository.

prior context, repeat failed actions, or fail to incorporate in- The main contributions of this work are summarized as

termediate findings, which reduces effectiveness and increases follows:

| wasted probing. This shortfall matches evidence that attention- | • | A | fully | automated | LLM-driven | red-teaming | frame- |
| --- | --- | --- | --- | --- | --- | --- | --- |
| based models emphasize recent tokens and struggle with long- | work executing reconnaissance, exploitation, and post- |  |  |  |  |  |  |
| range procedural state [18], [19]. As shown in Figure 2, human | exploitation with minimal human intervention. |  |  |  |  |  |  |
| testers carry forward artifacts (discovered services, credentials, | • | A hybrid rectification module leveraging targeted fuzzy |  |  |  |  |  |
| outputs) to guide later decisions, whereas LLMs often lose that | mechanisms to recover hallucinated module names and |  |  |  |  |  |  |
| thread and require frequent human intervention, limiting fully | commands. |  |  |  |  |  |  |
| automated red-teaming. | • | A stage-aware CMM that preserves state and failure |  |  |  |  |  |

| Reconnaissance | Reconnaissance |
| --- | --- |
| Carries context | Repeats similar |
| observations, notes | across stages/tries |
| Exfiltration | Exfiltration |

and their outcomes across multiple interaction steps. Instead

history for accurate multi-step planning.

>40% relative improvement in success rate across seven

services compared to prior LLM approach.

The rest of this paper is organized as follows: Section II

proposed work. Finally, Section VI concludes this paper.

II. B ACKGROUND AND R ELATED W ORK

This section provides an overview of the penetration testing,

| Human penetration tester | Current LLM-assisted workflow | • | A comprehensive evaluation on Metasploitable-2 showing |
| --- | --- | --- | --- |
| across stages | outputs | introduces background and related work. Section III presents |  |
| Exploitation | Exploitation | our proposed work. Section IV presents our evaluation results. |  |
| Maintain Context | Fails to handover context | Section V introduces limitations and future work related to our |  |

Fig. 2. Humans carry context across stages, while LLMs repeat outputs and target environment, followed by prior research examining

fail to hand over context. automated pen-testing solutions.

To address these challenges, APT-Agent introduces two core A. Key Phases of Penetration Testing

contributions: a rectification module to mitigate Challenge APT-Agent focuses on three primary phases of penetration

#1: hallucination of technical entities and a command-specific, testing: (1) reconnaissance, where the tester collects informa-

stage-aware context management module (CMM) to over- tion about hosts, services, and software versions to construct

come Challenge #2: insufficient long-term contextual mem- an attack surface map; (2) exploitation, where identified vul-

ory. (1) The rectification module validates LLM-generated nerabilities are actively leveraged to gain unauthorized access;

commands (mainly Metasploit modules) against a database and (3) post-exploitation and exfiltration, where sensitive data

of legitimate modules and commands. It employs a hybrid may be accessed, persisted, or extracted.

correction method, first applying a fuzzy string matching These phases are operationalized through frameworks such

algorithm (RapidFuzz ratio-based similarity) [20] to the final as Metasploit [28], which provides a comprehensive library

segment of the hallucinated path, followed by exact suffix of reconnaissance, exploitation, and post-exploitation mod-

matching. This design strikes a balance between tolerance ules [29]. Metasploit’s modular architecture offers compre-

for minor textual deviations and the precision required for hensive options for scanning, exploit execution, payload de-

executable commands, achieving substantially higher correc- ployment, and post-exploitation activities, including credential

tion rates than other approaches. (2) For context awareness, dumping and lateral movement. This versatility makes it par-

APT-Agent employs a stage-aware CMM that persistently ticularly suitable for evaluating the effectiveness of automated

tracks the current operational state, historical commands, penetration testing approaches [13], [14].

of passively logging outputs, it encodes prior actions and B. Existing Automated Penetration Testing Solutions

integrates history attempts into subsequent prompts. This Research on automated penetration testing [4] has primarily

enables adaptive strategy refinement and prevents repeated followed two directions: reinforcement learning (RL)-based

execution of invalid commands, thereby mitigating the long- methods and LLM-based methods.

horizon accuracy problem in multi-step penetration testing. Reinforcement Learning (RL) Approaches . RL-based

Together, these modules enable APT-Agent to achieve reliable, frameworks typically formalize penetration testing as a se-

fully automated execution across multiple pen-testing stages. quential decision-making problem within a Markov Decision

We evaluate APT-Agent on Metasploitable 2 [21], targeting Process (MDP), where agents learn optimal attack paths

seven vulnerable services spanning web, database, and net- through interaction and reward feedback. Schwartz et al. [23]

work protocols. The framework achieves an 84.29% end- extended this paradigm using a partially observable MDP

to-end exploitation success rate, substantially exceeding the (POMDP) [30] with an information decay factor, model-

performance range reported in prior LLM-based penetration ing how defender countermeasures gradually reduce attacker

*[Image: Page 2 Image]*

*[Image: Page 2 Image]*

*[Image: Page 2 Image]*

*[Image: Page 2 Image]*

*[Image: Page 2 Image]*

*[Image: Page 2 Image]*

---

## Page 3

| Category | Work | Handles Hallucination | Long-Horizon Memory | Full Automation | Low Expert Setup |
| --- | --- | --- | --- | --- | --- |
| Schwartz et al. (2020) [23] | — | ✗ | ✓ | ✗ |  |
| Chen et al. (2023) GAIL-PT [24] | — | ✗ | ✓ | ✗ |  |

RL

MINIMAL RELIANCE ON DOMAIN EXPERTS OR PRECONFIGURED ENVIRONMENTS

remain heavily reliant on simulation fidelity and struggle to

generalise to realistic penetration testing environments.

LLM-Based Approaches . LLM-driven frameworks leverage

the generative and contextual reasoning capabilities of models

such as GPT-3.5 [31] and GPT-4o [32]. PentestGPT [13]

introduced the Pentesting Task Tree (PTT), which modularises

reasoning, generation, and parsing to decompose penetra-

tion testing into subtasks. AutoAttacker [14] expanded this

paradigm with a Planner, Navigator, and Summarizer pipeline,

extending automation into post-exploitation actions such as

persistence and privilege escalation. Script Kiddie [22] em-

ployed a zero-shot prompt chaining strategy for end-to-end

penetration testing, while PentestAgent [27] adopted multi-

agent collaboration and retrieval-augmented generation (RAG)

to enhance exploitation planning. These works demonstrate the

adaptability of LLMs across reconnaissance, exploitation, and

post-exploitation phases. However, they remain constrained by

persistent issues such as hallucinated commands, limited long-

term memory, and reliance on pre-configured environments or

human corrections.

RL- and LLM-based systems along four criteria aligned with

TABLE I

.

with minimal expert setup.

III. P ROPOSED W ORK

This section presents the design overview of the overall

architecture of APT-Agent, including its core modules and

supporting mechanisms.

A. System Overview

To address the limitations identified earlier, we propose

APT-Agent , a fully automated pen-testing framework that

leverages specialized LLM-driven chains to conduct penetra-

tion testing in a structured and adaptive manner. As shown

in Fig. 3, APT-Agent consists of three core components: the

Tactic Selection Module , which determines the next phase

of the MITRE ATT&CK framework [33]; the Command

Generation Module , which produces executable system com-

mands or Metasploit operations; and the Output Translation

Module , which condenses tool outputs into structured insights

for subsequent reasoning. These modules operate iteratively,

with each cycle representing a single penetration testing step

and considered as an iteration. In its current form, APT-

EXFILTRATE ).

| Becker et al. (2024) [25] | — | ✗ | ✓ | ✗ |  |
| --- | --- | --- | --- | --- | --- |
| Li et al. (2023) [26] | — | ✗ | ✓ | ✗ |  |
| PentestGPT (2023) [13] | ✗ | ✗ | ✗ | ✗ |  |
| Script Kiddie (2023) [22] | ✗ | ✗ | ✗ | ✓ |  |
| LLM | AutoAttacker (2024) [14] | ✗ | ✗ | ✗ | ✓ |
| PentestAgent (2024) [27] | ✗ | ✗ | ✗ | ✗ |  |
| APT-Agent (ours) | ✓ | ✓ | ✓ | ✓ |  |

C OMPARISON OF RL- AND LLM- BASED AUTOMATED PENETRATION TESTING . “H ANDLES H ALLUCINATION ” MAPS TO Challenge #1 ; “L ONG -H ORIZON

M EMORY ” MAPS TO Challenge #2 . ✓ = PRESENT / SUPPORTED , ✗ = ABSENT / LIMITED , — = NOT APPLICABLE . “L OW E XPERT S ETUP ” INDICATES

knowledge over time. This formulation enables planning un- form command generation does not occur in these frameworks.

der uncertainty but was validated only in simulated settings. LLM systems (e.g., [13], [22], [14], [27]) operate on real

Chen et al. [24] proposed GAIL-PT, which combines expert targets with lighter setup, but most lack explicit mechanisms

demonstrations with generative adversarial imitation learning for hallucination correction and long-horizon memory. As a

to accelerate attack planning, while Becker et al. [25] bench- result, they often require human-in-the-loop steering and fail

marked multiple RL algorithms (Q-learning, DQN, A3C) on to achieve dependable end-to-end automation.

the NASim simulator for systematic comparison. Li et al. [26] No prior work simultaneously satisfies all four desiderata.

introduced a hierarchical deep reinforcement learning frame- This gap motivates our design of APT-Agent , which retains

work that incorporates expert prior knowledge into state and the adaptability of LLMs while adding an explicit rectification

action representations, improving learning efficiency and struc- module to address Challenge #1 and a structured CMM for

tured planning. Despite these advances, RL-based approaches Challenge #2, thereby enabling fully automated campaigns

Limitations and Research Gap. Table I contrasts prior Agent operates across three stages ( RECON , EXPLOIT , and

our challenges: Handles Hallucination (Challenge #1), Long- APT-Agent is designed to overcome two major weaknesses

Horizon Memory (Challenge #2), Full Automation , and Low of prior LLM-based frameworks: (i) hallucination of techni-

Expert Setup . cal entities , where models generate non-existent commands

RL approaches (e.g., [23], [24], [25], [26]) score well on au- or module names, and (ii) loss of contextual memory

tomation within simulators, yet they require substantial expert across multi-step campaigns. To address these, APT-Agent

engineering (environment design, reward shaping), leading incorporates two additional modules: a Rectifier Module ,

to limited real-world deployability and a poor ”low-expert” which validates and corrects hallucinated commands against

profile. They do not have the hallucination problem since free- a curated Metasploit database using hybrid fuzzy matching;

---

## Page 4

Fig. 3. Overview of APT-Agent

and a CMM , which maintains stage-specific logs of executed oriented feedback. Direct exposure to verbose or noisy outputs

commands and outcomes, enabling long-term context retention risks misleading the LLM and propagating hallucinations.

and adaptive reasoning. Instead, this module applies a labeling scheme to classify

Mirroring real-world penetration testing teams, APT-Agent outcomes as SUCCESS or FAIL , summarizes the key findings,

separates strategic reasoning from tactical execution. The and suggests the next logical step.

Tactic Selection Module acts as the controller, the Command

Generation Module issues commands, and the Output Trans- C. Rectification Module

lation Module structures outputs before reinjecting them into A key innovation of APT-Agent is the Rectification

the reasoning loop. This modularity ensures both specialization Module , designed to mitigate a recurring weakness of

and coherence across the testing process. Next, we detail each LLMs: hallucinated LLM outputs. During experiments, we

of APT-Agent’s core components, describing their design and observed that LLMs often produced outputs that appeared

role in enabling reliable, automated penetration testing. syntactically valid but were absent in the Metasploit

framework. For instance, when tasked with performing

B. Modules in APT-Agent SSH user enumeration, an LLM generated the invalid

APT-Agent operates through a continuous loop of different module: exploit/linux/ssh/openssh_user_enum

modules: 1. Tactic Selection Module, 2. Command Generation instead of the valid module:

Module and 3. Output Translation Module. auxiliary/scanner/ssh/ssh_enumusers . Such

(1) The Tactic Selection Module governs the overall pro- errors disrupt command execution and propagate failures

gression of the campaign by selecting the most appropriate through multi-step attack chains.

stage of the MITRE ATT&CK tactics based on accumulated To address this, APT-Agent employs a rectification module

knowledge and prior outcomes. The logic first checks if comprising two complementary components, each detailed in

the campaign objective has been met. If so, the operation the subsections that follow. The first is a curated knowledge

terminates. Otherwise, the module selects one of the stages base of valid Metasploit modules, which serves as the author-

based on the campaign’s current progress. (2) The Command itative reference set against which every LLM-generated path

Generation Module transforms high-level tactic decisions into is checked. The second is the Hybrid Rectification Method ,

executable commands tailored to the current stage. During an algorithm that maps each hallucinated module path back

reconnaissance, it generates scanning or enumeration com- to an entry in the knowledge base by combining approximate

mands to reveal target information. In the exploitation stage, fuzzy matching with suffix-based correction. Together, these

the LLM selects a vulnerable service based on reconnaissance components ensure that linguistically plausible but invalid

results, outputs relevant details (IP, port, service, version), LLM outputs are grounded in verifiable, executable modules.

and produces appropriate Metasploit commands. Crucially, the Beyond correcting hallucinated module paths, the recti-

module interacts with the CMM to avoid repeating failed fication module also performs execution-level normalization

exploits and adapt strategies dynamically. In the exfiltration prior to runtime. This includes injecting missing mandatory

stage, it adapts commands to the active session type: gen- options (e.g., RPORT , LHOST , LPORT ) and validating payload

erating Unix commands for shell sessions and Metasploit- architecture against the selected module target. These checks

native commands for meterpreter sessions. This design ensures ensure that rectified commands are not only syntactically valid

flexibility across different access conditions while maintaining but also executable within the target context.

progress toward the ultimate goal of sensitive file exfiltration. 1) Knowledge Base Foundation: At its core, the rectifier

(3) The Output Translation Module serves as an interpretive relies on a database that we curated and constructed of

layer that condenses raw tool outputs into structured, goal- 3,253 valid Metasploit modules, indexed by attributes such

*[Image: Page 4 Image]*

---

## Page 5

| Algorithm 1 | Hybrid Rectification | in practice; and third, the stage-aware router that injects this |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Require: | LLM path | p | , DB | D | ; threshold | τ | h | context back into the Command Generation Module at each |
| Ensure: | m | ∗ | or | NO_MATCH | iteration. |  |  |  |

1: s ← last segment of p

2: s f ← arg max t ∈ Suffixes( D ) sim( s, t )

is typically preserved in the suffix even when the hierarchy is

(b) Suffix Fuzzy Matching: The rectification module per-

forms fuzzy matching between s and all module suffixes in

the database D using normalized Levenshtein similarity:

d lev ( x, y )

sim ( x, y ) = 1 − .

max( | x | , | y | )

The most similar suffix s f is selected.

(c) Module Reconstruction: Once s f is identified, the rec-

tification module retrieves the full module path in D that

f and replaces the LLM’s hallucinated output with

achieved the highest rectification success rate among all vari-

ants, as detailed in Section IV-E.

D. Context Management Module (CMM)

context across stages, yet LLMs are prone to short-term

memory loss and duplicated LLM outputs. Without explicit

context management, prior failures or successes are easily

forgotten, leading to repeated commands and inefficient ex-

stateless unless explicit memory components are introduced.

Naïve approaches, such as storing entire transcripts, proved

noisy and costly in token usage. Through experimentation, we

1) Design Choices: The design of the CMM was shaped

(1) Deterministic RECON stage. We observe that reconnais-

sance consistently succeeds in detecting target services and

outcome.

stage-specific JSON logs:

M = { M EXPLOIT , M EXFILTRATE } ,

where each stage log M stage is an array of compact entries:

M stage = [ e 1 , e 2 , . . . , e k ] ,

with schema



 "iter" : i,



text:

M_EXPLOIT = [

{"iter": 1, "cmd": "exploit/multi/ssh/sshexec",

"result": "fail"},

vsftpd_234_backdoor",

"result": "success"}

]

M_EXFILTRATE = [

"result": "success"},

txt",

"result": "fail"}

]

3: return module in D with suffix s f by two practical considerations:

as service, type, operating system, rank, and description. This versions in our evaluation. Since these results are stable and

structured knowledge base provides the authoritative reference reproducible, maintaining a RECON log would add overhead

for all rectified outputs. without contributing new information.

2) Hybrid Rectification Method: The Hybrid Method in- (2) Signal-to-noise and cost trade-off. To avoid verbose

tegrates two complementary ideas: fuzzy search and suffix- logs that increase token consumption, the CMM records only

level alignment, into a unified correction pipeline shown in three fields per iteration: the stage iteration number, the issued

Algorithm 1: command, and its binary outcome ( success or fail ).

(a) Suffix Extraction: The generated path p is decomposed by Crucially, raw outputs (stdout/stderr) are excluded, as they

“/” and the last component s (e.g., openssh_user_enum ) tend to overwhelm prompts with irrelevant noise, while the

is extracted. This captures the LLM’s intended function, which essential decision-making signal is captured through the binary

| incorrect. | Formally, the global memory state | M | is defined as a set of |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| contains | s | e | = | "cmd" | : | string | , |
| this verified path. | "result" | : | { | "success" | , | "fail" | } |
| This hybrid design unifies the strengths of fuzzy and suffix- | 2) Illustrative JSON Examples: | To demonstrate the com- |  |  |  |  |  |

based rectification: fuzzy similarity provides tolerance to mi- pactness of this representation, we provide example log frag-

nor textual variations, while suffix grounding prevents errors ments below. Each entry captures only the iteration index, ex-

from hierarchical hallucinations. Empirically, this approach ecution attempt and its binary outcome, discarding extraneous

| Multi-step penetration testing requires maintaining reliable | {"iter": | 2, | "cmd": | "exploit/unix/ftp/ |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ploration. While LangChain offers a composable framework | {"iter": | 1, | "cmd": | "search | -f | flag.txt", |  |  |
| for chaining LLM prompts and tools, its default workflows are | {"iter": | 2, | "cmd": | "download | /home/msfadmin/flag. |  |  |  |
| found that a | minimalist, high-signal log format | yields better | 3) Stage-Aware | Routing | and | Prompt | Injection: | A |

performance by capturing only what is essential for decision- lightweight router manages read/write access to these logs.

making. Hence, the CMM adopts this principle, focusing Unlike summarization approaches that feed condensed notes

on concise, high-value state tracking for efficient decision- back into prompts, APT-Agent directly injects the JSON log

making. The remainder of this subsection details how this of the current stage into the Command Generation Module .

principle is realized: first, the design choices that shape the log This is feasible because the log entries are deliberately

format with the formal memory schema; second, illustrative compact and easy for the LLM to parse.

JSON examples that demonstrate the resulting representation This strategy has two main advantages:

---

## Page 6

• Prevention of redundancy. The explicit result field autonomous session management, APT-A GENT achieves full

ensures that previously failed commands are not re- end-to-end operation with no human intervention beyond

issued. specifying the target IP.

• Preservation of chronology. Iteration numbers and raw

command strings maintain execution order, giving the IV. E VALUATION

LLM precise historical grounding. We evaluate APT-Agent in a controlled Metasploitable 2 en-

By balancing compactness with fidelity, the CMM enables vironment. Our evaluation presents service-wise performance

long-horizon campaigns to retain the essential context needed results, compares APT-Agent with prior systems, and conducts

for adaptive decision-making, without inflating costs or intro- ablation studies on key components, concluding with an anal-

| ducing noise. | ysis of the rectification and memory designs. |  |  |
| --- | --- | --- | --- |
| E. Full-Automation Mechanisms | A. Target Environment |  |  |
| APT-Agent | enables fully autonomous operations by inte- | We set up a target environment consisting of a | Metas- |

grating mechanisms for tool execution, module configuration, ploitable 2 virtual machine that contains a sensitive file named

runtime control, and session management, allowing seamless flag.txt . Metasploitable 2 is a widely adopted open-

progression through all stages in the campaign. source virtual machine intentionally designed with numerous

(1) Tool adapters for executable actions. We designed security vulnerabilities for research and training purposes [13],

lightweight adapters that enable seamless integration with [14]. The virtual machine hosts numerous vulnerable services

scanning and exploitation tools. Nmap adapter parses multi- across different layers, including web applications, databases

line model outputs, extracts the first valid nmap / sudo (MySQL, PostgreSQL), and network protocols (e.g., HTTP,

nmap / ping line, tokenizes it with shlex , enforces a timeout, VSFTPD). This diversity provides a realistic attack surface

and returns the execution result. For exploitation, we rely spanning reconnaissance, exploitation, and post-exploitation

on MSFRPCD, Metasploit’s RPC daemon, which exposes scenarios, making it particularly suitable for benchmarking the

console, module, session, and job control via a programmatic reliability of automated penetration testing approaches.

API. The Metasploit adapter leverages this interface to execute

B. Experimental Setup and Methodology

actionable commands and stream only relevant lines to the

RPC console, avoiding verbose noise. We use GPT-4o as the core LLM and the Metasploitable 2

(2) Metasploit Module Rectification and Setup. During the virtual machine with intentionally vulnerable services to en-

EXPLOIT stage, the model outputs a header (IP/service/ver- able realistic, reproducible, and safe testing. In contrast, GPT-

sion/port) and a candidate use <module> . We canonicalize 3.5-Turbo and Llama3-7B consistently failed to achieve suc-

the service, query a local modules table, and perform the cessful exploitations across our experimental runs and were

rectification. Module options and payloads are then fetched therefore excluded from further evaluation.

live via MSFRPCD and injected into an LLM prompt, which Target Services: We test seven representative services:

produces an executable, placeholder-free block (including pay- vsftpd (FTP), OpenSSH (SSH), Telnet , Apache

loads, required options, and potential default/blank credentials (HTTP), UnrealIRCd (IRC), PostgreSQL , and Samba

or a supplied wordlist). This eliminates the need for human (SMB). These are vulnerable/misconfigured in Metas-

operators to manually search for modules or craft option ploitable 2 and exploitable via Metasploit, offering diverse

strings. vectors (RCE, weak credentials, etc.). For brute-force depen-

(3) Brute-force awareness and time budgeting. The option- dent services, we use a short wordlist containing the correct

setup process automatically tags modules as brute-force or credential pair to bound runtime and isolate evaluation to the

non–brute-force. This classification enables dynamic adjust- agent’s reasoning and orchestration behavior, as exhaustive

ment of console execution windows (e.g., 180 s for brute- credential search is a property of the underlying tooling rather

force modules vs. 30 s otherwise) and tail-trimmed transcripts than of APT-Agent itself.

to manage extensive outputs, while campaign termination is Iteration Definition and Workflow: One iteration is a full

governed by a fixed iteration budget. As a result, idle waiting pass through (i) Tactic Selection , (ii) Command Generation ,

is reduced, and noisy inputs are minimized. and (iii) Output Translation : select a stage, execute a com-

(4) Autonomous session handling. Beyond console-based mand, and analyze the result. The agent iterates until success-

checks, APT-Agent actively monitors the RPC session inven- ful file exfiltration or until the maximum iteration budget (30

tory ( client.sessions.list ) to detect new sessions iterations per stage) is exceeded.

spawned during exploitation. When the foothold is a raw Scenario and Tactics: The objective is to retrieve a sensitive

shell, it invokes sessions -u <id> to attempt upgrad- file from the target. Campaigns therefore proceed through

ing into a meterpreter session—Metasploit’s in-memory post- RECON → EXPLOIT → EXFILTRATE . While the framework

exploitation agent with advanced file, process, and network supports more tactics (e.g., lateral movement, persistence),

control. we constrain the scope for controlled evaluation. Early runs

By combining tool-specific adapters, robust module recti- showed EXPLOIT is most prone to hallucinated module

fication and setup, brute-force–aware option synthesis, and names, motivating the Rectifier’s focus there; the strategy

---

## Page 7

Avg. Total

| Service | Success |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Iterations | Avg. Iterations per Stage |  |  |  |  |
| RECON | EXPLOIT | EXFILTRATE |  |  |  |
| vsftpd 2.3.4 | 10 | 5.1 | 1.5 | 1.2 | 2.4 |
| OpenSSH 4.7 | 9 | 7.6 | 1.4 | 4.2 | 2.0 |
| Telnet | 8 | 4.6 | 1.1 | 1.2 | 2.3 |
| Apache 2.2.8 | 7 | 17.3 | 2.4 | 7.9 | 7.0 |
| UnrealIRCd | 7 | 8.9 | 2.7 | 4.1 | 2.1 |
| PostgreSQL | 9 | 8.6 | 1.0 | 1.5 | 6.1 |
| Samba | 9 | 8.8 | 1.2 | 2.4 | 5.2 |

TABLE II

S ERVICE - WISE NUMBER OF SUCCESSES OUT OF 10 TRIALS , AVERAGE ITERATION COUNTS PER STAGE .

generalizes to other stages as needed. Excellent-ranked Metas-

ploit modules were retrieved from the database during the

rectification.

Autonomous Trials: Runs are fully automated. For each ser-

vice, we conduct ten independent runs , and each experiment

is capped at 30 iterations per stage. A run ends on successful

file exfiltration (success) or exceeding the iteration limit (fail-

ure). This setup measures success rate and efficiency (time/it-

erations) without human intervention. An example execution

trace of a full APT-Agent campaign, including rectification Fig. 4. APT-Agent vs. Script Kiddie

and adaptive recovery, is provided in Appendix B.

C. Results out introducing expert knowledge or external guidance. Runs

Service-wise Performance: Table II reports per-service results requiring more than three human interventions were deemed

across 10 independent runs per target. APT-Agent succeeded in unsuccessful, following prior work.

all 10 runs on vsftpd 2.3.4 , in 9 of 10 runs on OpenSSH Fig. 4 reports service-wise results across seven target ser-

4.7 , PostgreSQL , and Samba , in 8 of 10 on Telnet , vices, with ten independent runs per service. APT-Agent

and in 7 of 10 on both Apache 2.2.8 and UnrealIRCd , consistently outperforms both baselines across nearly all

yielding an aggregate end-to-end success rate of 84 . 29% services. The largest gaps appear on Apache 2.2.8 ,

(59/70). Average total iterations per campaign ranged from OpenSSH 4.7 , and Telnet , where PentestGPT achieves at

4 . 6 (Telnet) to 17 . 3 (Apache 2.2.8), reflecting differences in most 0–5 successes and Script Kiddie 0–2, while APT-Agent

service complexity. The EXPLOIT stage averaged between 1 . 2 succeeds in 7–9 runs. On services including Apache 2.2.8 ,

iterations (vsftpd, Telnet) and 7 . 9 iterations (Apache 2.2.8), UnrealIRCd , and Samba , PentestGPT fails to achieve any

while EXFILTRATE averaged between 2 . 0 (OpenSSH 4.7) successful runs, reflecting its limited autonomy and reduced

and 7 . 0 iterations (Apache 2.2.8), depending on each service’s effectiveness on services and CVE-based vulnerabilities. Ag-

data exposure surface. The single failure on OpenSSH 4.7 gregated across all seven services, APT-Agent attains an

was attributable to continuous duplicate command generation overall success rate of 84.29%, compared to 48.57% for Script

during exfiltration. The two Telnet failures stemmed from Kiddie and 18.57% for PentestGPT, demonstrating stronger

session-retrieval errors, in which a remote access session was generalization and robustness in scenarios requiring iterative

successfully spawned but APT-Agent failed to attach to and reasoning, error recovery, and adaptive command generation.

interact with it. Overall, APT-Agent demonstrates consistent A detailed contextual comparison with PenHeal [ ? ] is provided

reliability across heterogeneous services with bounded itera- in Appendix A.

tion counts. D. Ablation Study

Comparison with related works: To contextualize APT- To quantify the contribution of each core component, we

Agent’s performance, we compare it against a state-of-the- conducted an ablation study in which the Rectification Module

art Script Kiddie framework [22] and PentestGPT [13]. All and the CMM were removed individually and jointly. As

systems were evaluated under identical conditions using GPT- shown in Fig. 5, removing either component substantially

4o as the underlying LLM. As PentestGPT is human-in-the- degraded overall performance. In its full configuration, APT-

loop, whereas APT-Agent and Script Kiddie operate fully Agent achieved an 84 . 29% end-to-end success rate (59/70),

autonomously, human involvement in PentestGPT was ex- while omitting the Rectification Module reduced this to

plicitly constrained for fairness. Permitted interactions were 71 . 43% (50/70), and removing the CMM decreased it further

limited to copy–paste actions and simple natural-language to 65 . 71% (46/70). When both modules were disabled, the

prompts directly following PentestGPT’s own feedback, with- success rate dropped to 54 . 29% (38/70). Across the ablation

---

## Page 8

Fig. 6. Rectification Methods Success Rate

runs, APT-Agent issued 53 Metasploit module invocations, 16

of which ( 30 . 2% ) were hallucinated; the Rectification Module

recovered 10 of these, yielding a 62 . 5% in-run correction

rate. The CMM’s contribution to efficiency was equally pro-

nounced: on UnrealIRCd , average EXFILTRATE iterations

fell from 52 without the CMM to 3 with it, a 17-fold

reduction. Together, these results underscore the modules’

complementary roles: the Rectifier recovers otherwise-failed

exploit attempts, while the CMM eliminates redundant actions

and stabilizes multi-step execution.

method was evaluated on 78 LLM-generated hallucinated

modules to assess whether it could correct them to exe-

cutable modules that preserved the original intent. The hy-

brid approach achieved the highest success rate (51.95%),

outperforming fuzzy matching (38.46%), last-part matching

(37.18%), and RAG (5.13%). The 51.95% reflects the recti-

fier’s intrinsic accuracy on a held-out set of 78 hallucinated

module names, and is distinct from the 62.5% in-run correc-

tion rate reported in Section V-A, which is measured over

the smaller and differently-distributed set of hallucinations

actually produced during live campaigns. These results demon-

strate that the Hybrid method combining lexical similarity with

structural pattern matching yields a more robust correction

Agent.

Context Awareness Evaluation.

(1) Conversation Buffer Memory (CBM): CBM stores the

conversational history between the LLM and the user. We

tested two variants: (i) full conversation history and (ii) results

from the Output Translation Module only. Duplication was

lower with full history (40.48%) than with results-only storage

(49.15%), while both achieved 2 success runs out of 5.

(2) Conversation Summary Buffer Memory (CSBM):

CSBM periodically condenses history into summaries for

token efficiency. In practice, this approach performed poorly,

yielding 1 success run and the highest duplication rate

(68.75%). This limitation arises because summarization often

omits essential details, and repeated condensation further

increases the token cost per campaign.

(3) Context Management Module (CMM): CMM maintains

structured, stage-specific JSON logs of prior actions, explicitly

recording historical commands and their outcomes, which are

reinjected into subsequent prompts. This design prevents the

regeneration of ineffective modules and achieved the best per-

formance, with 5/5 successful runs and the lowest duplication

rate (16.67%).

Given these results, APT-Agent adopts the CMM as its default

memory mechanism, enhanced with a stage-aware router that

reinjects only context relevant to the active campaign phase,

preserving efficiency while ensuring continuity.

tooling.

Fig. 5. Ablation Study: Success Rate mechanism adopted as the default rectification method in APT-

E. Component-Level Evaluation V. L IMITATIONS AND F UTURE W ORK

We assessed various rectification methods (for hallucinated Role of Rectification and CMM. The results underscore

LLM outputs) and context-awareness methods (for long-term the necessity of domain-grounded safeguards in LLM-driven

context awareness), which motivate the hybrid rectifier and the security automation. The Rectification Module mitigates hal-

CMM. lucinations—particularly during the EXPLOIT stage, while

Rectification Methods. We evaluated four rectification strate- the CMM minimizes redundant commands by reinjecting

gies: RAG-based retrieval, fuzzy matching, last-part match- stage-relevant command history. Ablation results confirm that

ing, and a hybrid approach. RAG struggled with structured removing either safeguard sharply reduces success rates and

identifiers, while fuzzy and suffix matching failed when large increases iteration counts. These findings suggest that reliabil-

portions of the path were corrupted. The hybrid approach ity in LLM-based cyber agents depends less on model scale

combines lexical tolerance with structural grounding, yielding and more on domain-grounded architectural constraints. By

the highest correction rate. coupling language reasoning with verifiable knowledge bases

Figure 6 compares the effectiveness of four rectification and explicit state tracking, APT-Agent bridges the gap between

methods for recovering hallucinated module names. Each general LLM fluency and the precision required in security

---

## Page 9

database, cloud, and kernel-level vulnerabilities, progressing

toward a general-purpose autonomous red-teaming system.

Ethical and safety considerations. As highlighted in recent

works [7], [8], [10], both defenders and adversaries are in-

creasingly leveraging LLMs in cybersecurity operations. This

dual-use nature underscores the need to strengthen defensive

preparedness. Our goal in developing APT-Agent is to up-

lift red-team capabilities, enabling defenders to proactively

uncover vulnerabilities and harden systems before malicious

actors exploit them. At the same time, responsible deployment

remains essential: guardrails such as sandboxed environments,

access controls, and human oversight are required to prevent

misuse. Establishing standardized benchmarks, safety guide-

Fig. 7. LLM Context Comparison: Duplication Rate lines for automated pen-testing, and responsible disclosure

practices will be critical for safe and effective adoption.

VI. C ONCLUSION

In this paper, we have introduced APT-Agent, which

is a fully autonomous red-teaming framework powered by

LLMs and reinforced with rectification and context manage-

ment modules. APT-Agent demonstrated the ability to au-

tonomously complete penetration testing campaigns, including

reconnaissance, exploitation, and exfiltration—without human

intervention. Compared to prior LLM-based approaches, it

achieved higher success rates, improved reliability, and re-

duced hallucination-induced errors by grounding outputs in

executable system knowledge and maintaining stage-specific

Fig. 8. LLM Context Methods Comparison: Success Rate memory. Our evaluations highlighted the scientific importance

of the rectification and context management modules. The

proposed rectifier mitigated invalid module generations while

Extensibility of tactics. Our experiments demonstrate that the memory module prevented redundant actions and enabled

APT-Agent can autonomously execute penetration campaigns adaptive reasoning across campaign stages. Ablation studies

with strong reliability in the target environment. Although the confirmed that disabling either component led to substan-

evaluation focused on RECON, EXPLOIT, and EXFILTRATE tial performance degradation, underscoring their necessity for

stages, the Tactic Selection Module and supporting com- long-horizon automated penetration testing.

ponents are readily extensible. Additional tactics defined in

| ATT&CK, such as lateral movement and privilege escalation, | R | EFERENCES |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| can be incorporated by extending decision rules and aug- | [1] | National | Institute | of | Standards | and | Technology, | “Technical | guide |
| menting command/action templates, thereby enabling broader | to | information | security | testing | and | assessment,” | U.S. | Department |  |

of Commerce, Tech. Rep. Special Publication 800-115, Sep. 2008,

coverage of the attack lifecycle.

accessed: September 03, 2025. [Online]. Available: https://csrc.nist.gov/

Toward more complex environments. Beyond expanding publications/detail/sp/800-115/final

its tactical repertoire, future work will deploy APT-Agent in [2] G. Deng, Z. Zhang, Y. Li, Y. Liu, T. Zhang, Y. Liu, Y. Guo, and D. Wang,

“Nautilus: Automated restful api vulnerability detection,” in Proceedings

| larger and more heterogeneous environments, such as multi- | of the 32nd USENIX Security Symposium | . | USENIX Association, 2023. |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| host networks with interacting services and cross-machine | [3] | B. Jiang, Y. Jing, T. Shen, T. Wu, Q. Yang, and D. Xiong, “Automated |  |  |  |  |  |  |
| attack paths. We also plan to evaluate its adaptability to | progressive | red | teaming,” | arXiv | preprint | arXiv:2407.03876 | , | 2024. |

[Online]. Available: https://arxiv.org/abs/2407.03876

| diverse vulnerability classes (e.g., web vulnerabilities, capture- | [4] | F. Abu-Dabaseh and E. Alshammari, “Automated penetration testing: |
| --- | --- | --- |
| the-flag) and operational contexts, moving closer to a fully | An overview,” in | Computer Science & Information Technology (CS & |
| general-purpose framework for autonomous, LLM-driven pen- | IT) | , Apr. 2018, pp. 121–129. |

[5] W. X. Zhao, K. Zhou, J. Li, T. Tang, X. Wang, Y. Hou, Y. Min,

| testing. | B. Zhang, J. Zhang, Z. Dong, Y. Du, C. Yang, Y. Chen, Z. Chen, |  |  |
| --- | --- | --- | --- |
| Scalability and Adaptation. | APT-Agent’s modular design | J. Jiang, R. Ren, Y. Li, X. Tang, Z. Liu, P. Liu, J. Nie, and J. Wen, “A |  |
| allows expansion beyond its evaluated stages (RECON, EX- | survey of large language models,” | arXiv preprint arXiv:2303.18223 | , |

2023. [Online]. Available: https://arxiv.org/abs/2303.18223

| PLOIT, EXFILTRATE). The same tactic-selection and mem- | [6] | Y. Liu, T. Han, S. Ma, J. Zhang, Y. Yang, J. Tian, H. He, A. Li, |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ory logic can be extended to additional ATT&CK phases | M. | He, | Z. | Liu, | Z. | Wu, | L. | Zhao, | D. | Zhu, | X. | Li, | N. | Qiang, |
| such as lateral movement or persistence. Future experiments | D. Shen, T. Liu, and B. Ge, “Summary of chatgpt-related research |  |  |  |  |  |  |  |  |  |  |  |  |  |

and perspective towards the future of large language models,” Meta-

will deploy the framework in multi-host networks and CTF- Radiology , vol. 1, no. 2, p. 100017, Sep. 2023. [Online]. Available:

style challenge environments to test adaptability across web, http://dx.doi.org/10.1016/j.metrad.2023.100017

---

## Page 10

| [7] | V. | Mayoral-Vilches, | G. | Deng, | Y. | Liu, | M. | Pinzger, | and | S. | Rass, | penetration | testing | using | a3c, | q-learning | and | dqn,” | arXiv | preprint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| “Exploitflow, | cyber | security | exploitation | routes | for | game | theory | arXiv:2407.15656 | , | Jul. | 2024. | [Online]. | Available: | https://doi.org/10. |  |  |  |  |  |  |
| and | ai | research | in | robotics,” | 2023. | [Online]. | Available: | https: | 48550/arXiv.2407.15656 |  |  |  |  |  |  |  |  |  |  |  |
| //arxiv.org/abs/2308.02152 | [26] | Q. Li, M. Zhang, Y. Shen, R. Wang, M. Hu, Y. Li, and H. Hao, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [8] | Y. Zhang, W. Song, Z. Ji, D. Yao, and N. Meng, “How well does | “A | hierarchical | deep | reinforcement | learning | model | with | expert |  |  |  |  |  |  |  |  |  |  |  |
| llm generate security tests?” | arXiv preprint arXiv:2310.00710 | , 2023. | prior | knowledge | for | intelligent | penetration | testing,” | Computers | & |  |  |  |  |  |  |  |  |  |  |
| [Online]. Available: https://arxiv.org/abs/2310.00710 | Security | , | vol. | 132, | p. | 103358, | 2023. | [Online]. | Available: | https: |  |  |  |  |  |  |  |  |  |  |
| [9] | Z. He, Z. Li, S. Yang, H. Ye, A. Qiao, X. Zhang, X. Luo, and T. Chen, | //doi.org/10.1016/j.cose.2023.103358 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

“Large language models for blockchain security: A systematic literature [27] X. Shen, L. Wang, Z. Li, Y. Chen, W. Zhao, D. Sun, J. Wang,

| review,” | arXiv preprint arXiv:2403.14280 | , 2025. [Online]. Available: | and W. Ruan, “Pentestagent: Incorporating llm agents to automated |
| --- | --- | --- | --- |
| https://arxiv.org/abs/2403.14280 | penetration testing,” | arXiv preprint arXiv:2411.05185 | , 2025. [Online]. |
| [10] | A. Abuadbba, K. Moore, D. Goel, C. Hicks, V. Mavroudis, B. Hasir- | Available: https://arxiv.org/abs/2411.05185 |  |

cioglu, and P. Jennings, “From promise to peril: Rethinking cybersecu- [28] Rapid7, “Metasploit,” https://www.metasploit.com/, 2025, accessed:

| rity red and blue teaming in the age of llms,” | IEEE Security & Privacy | , | September 03, 2025. |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vol. 24, no. 2, pp. 53–63, 2026. | [29] | W. Zhang, J. Xing, and X. Li, “Penetration testing for system security: |  |  |  |  |  |  |  |  |  |  |  |  |
| [11] | R. Fang, R. Bindu, A. Gupta, Q. Zhan, and D. Kang, “Llm agents can | Methods and practical approaches,” | arXiv preprint arXiv:2505.19174 | , |  |  |  |  |  |  |  |  |  |  |
| autonomously hack websites,” | arXiv preprint arXiv:2402.06664 | , Feb. | May 2025. [Online]. Available: https://arxiv.org/abs/2505.19174 |  |  |  |  |  |  |  |  |  |  |  |
| 2024. [Online]. Available: https://doi.org/10.48550/arXiv.2402.06664 | [30] | C. Sarraute, O. Buffet, and J. Hoffmann, “Penetration testing == pomdp |  |  |  |  |  |  |  |  |  |  |  |  |
| [12] | R. | Fang, | R. | Bindu, | A. | Gupta, | and | D. | Kang, | “Llm | agents | solving?” | arXiv preprint arXiv:1306.4714 | , 2013. [Online]. Available: |
| can | autonomously | exploit | one-day | vulnerabilities,” | arXiv | preprint | https://doi.org/10.48550/arXiv.1306.4714 |  |  |  |  |  |  |  |

arXiv:2404.08144 , Apr. 2024. [Online]. Available: https://doi.org/10. [31] OpenAI, “Gpt-3.5 turbo,” https://platform.openai.com/docs/models/

48550/arXiv.2404.08144 gpt-3.5-turbo, 2022, accessed: September 03, 2025.

[13] G. Deng, Y. Liu, V. Mayoral-Vilches, P. Liu, Y. Li, Y. Xu, T. Zhang, [32] ——, “Gpt-4o,” https://platform.openai.com/docs/models/gpt-4o, 2024,

Y. Liu, M. Pinzger, and S. Rass, “Pentestgpt: An llm-empowered accessed: September 03, 2025.

automatic penetration testing tool,” arXiv preprint arXiv:2308.06782 , [33] MITRE Corporation, “Mitre att&ck ® — enterprise tactics,”

Aug. 2023. [Online]. Available: https://doi.org/10.48550/arXiv.2308. accessed 2025-10-08. [Online]. Available: https://attack.mitre.org/

06782 tactics/enterprise/

[14] J. Xu, J. W. Stokes, G. McDonald, X. Bai, D. Marshall, S. Wang, [34] J. Huang and Q. Zhu, “PenHeal: A Two-Stage LLM Framework for

| A. | Swaminathan, | and | Z. | Li, | “Autoattacker: | A | large | language | Automated Pentesting and Optimal Remediation,” in | Proceedings of the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model guided system to implement automatic cyber-attacks,” | arXiv | Workshop on Autonomous Cybersecurity | . | ACM, Nov. 2024. [Online]. |  |  |  |  |  |  |
| preprint | arXiv:2403.01038 | , | Mar. | 2024. | [Online]. | Available: | https: | Available: https://dl.acm.org/doi/10.1145/3689933.3690831 |  |  |

//doi.org/10.48550/arXiv.2403.01038

[15] M. Zhang, O. Press, W. Merrill, A. Liu, and N. A. Smith, “How

language model hallucinations can snowball,” 2023. [Online]. Available:

https://arxiv.org/abs/2305.13534

[16] N. Li, Y. Li, Y. Liu, L. Shi, K. Wang, and H. Wang, “Drowzee:

Metamorphic testing for fact-conflicting hallucination detection in large

language models,” 2024. [Online]. Available: https://arxiv.org/abs/2405.

00648

[17] P. Manakul, A. Liusie, and M. Gales, “SelfcheckGPT: Zero-resource

black-box hallucination detection for generative large language

models,” in Proceedings of the 2023 Conference on Empirical

Methods in Natural Language Processing , 2023. [Online]. Available:

https://openreview.net/forum?id=RwzFNbJ3Ez

[18] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N.

Gomez, L. Kaiser, and I. Polosukhin, “Attention is all you need,” in

Advances in Neural Information Processing Systems . Curran Associates

Inc., 2023. [Online]. Available: https://arxiv.org/abs/1706.03762

[19] L. Yang, H. Chen, Z. Li, X. Ding, and X. Wu, “Chatgpt is not

enough: Enhancing large language models with knowledge graphs for

fact-aware language modeling,” arXiv preprint arXiv:2306.11489 , Jun.

2023. [Online]. Available: https://doi.org/10.48550/arXiv.2306.11489

[20] S. Ji, G. Li, C. Li, and J. Feng, “Efficient interactive fuzzy

keyword search,” in Proceedings of the 18th ACM Conference on

Information and Knowledge Management (CIKM) . New York, NY,

USA: Association for Computing Machinery, 2009. [Online]. Available:

https://doi.org/10.1145/1526709.1526760

[21] Rapid7, “Metasploitable 2,” 2025, accessed: September 03, 2025. [On-

line]. Available: https://docs.rapid7.com/metasploit/metasploitable-2/

[22] S. Moskal, S. Laney, E. Hemberg, and U.-M. O’Reilly, “Llms

killed the script kiddie: How agents supported by large language

models change the landscape of network threat testing,” arXiv

preprint arXiv:2309.00667 , Sep. 2023. [Online]. Available: https:

//arxiv.org/abs/2309.00667

[23] J. Schwartz, H. Kurniawati, and E. El-Mahassni, “Pomdp + information-

decay: Incorporating defender’s behaviour in autonomous penetration

testing,” in Proceedings of the 30th International Conference on

Automated Planning and Scheduling (ICAPS) , 2020, pp. 235–243.

[Online]. Available: https://doi.org/10.1609/icaps.v30i1.6666

[24] J. Chen, S. Hu, H. Zheng, C. Xing, and G. Zhang, “Gail-pt: An

intelligent penetration testing framework with generative adversarial

imitation learning,” Computers & Security , vol. 126, p. 103055, 2023.

[25] N. Becker, D. Reti, E. V. N. Ntagiou, M. Wallum, and H. D.

Schotten, “Evaluation of reinforcement learning for autonomous

---

## Page 11

A PPENDIX A

C OMPARISON WITH P EN H EAL

ploitable II environment, enabling a direct contextual com-

optimize for fundamentally different objectives. PenHeal is

error recovery, and adaptive command generation under re-

alistic execution constraints. Consequently, ART-Agent may

A PPENDIX B

E XAMPLE APT-A GENT C AMPAIGN L OG (A BBREVIATED )

Illustrative End-to-End APT-Agent Campaign (Ab-

breviated)

Target: 192.168.102.197

[Iter. 1 | RECON]

Result: Apache httpd 2.2.8 detected on port 80.

[Iter. 2 | EXPLOIT | Rectification]

Module selected:

exploit/multi/http/

apache_mod_cgi_bash_env_exec

Raw command:

apache_mod_cgi_bash_env_exec

set RHOSTS 192.168.102.197

set PAYLOAD linux/x86/meterpreter/

reverse_tcp

Rectifier actions: (i) injects missing required option

(ii) validates payload architecture against the module

target.

Rectified command:

use exploit/multi/http/

apache_mod_cgi_bash_env_exec

set RHOSTS 192.168.102.197

set RPORT 80

set PAYLOAD linux/x86/meterpreter/

reverse_tcp

exploit

Outcome: Execution failed; module recorded.

[Iter. 3 | EXPLOIT | Rectification & Recovery]

Raw module reference:

exploit/unix/webapp/

php_cgi_arg_injection

Rectifier actions: (i) resolves the LLM-generated

module reference to the canonical Metasploit path;

LHOST , LPORT );

execution context.

( www-data ).

[Iter. 7 | END_OF_CAMPAIGN]

Goal achieved; campaign terminated.

Exploitation Memory ( M EXPLOIT )

[

{iter: 2,

result: fail},

{iter: 3,

cmd: php_cgi_arg_injection,

result: success}

]

[

{iter: 4,

result: fail},

{iter: 5,

result: success},

{iter: 6,

cmd: cat /home/msfadmin/flag.txt,

result: success}

]

| PenHeal [34] also evaluates its framework on the Metas- | (ii) | injects | missing | mandatory | options | ( | RPORT | , |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| parison of experimental settings. However, the two systems | (iii) confirms payload compatibility with the PHP CGI |  |  |  |  |  |  |  |
| designed to maximize vulnerability discovery coverage and | Rectified executable module: |  |  |  |  |  |  |  |
| to generate cost-aware remediation recommendations. In con- | exploit/multi/http/ |  |  |  |  |  |  |  |
| trast, ART-Agent is exploitation-driven, prioritizing end-to- | php_cgi_arg_injection |  |  |  |  |  |  |  |
| end campaign completion, including successful exploitation, | Outcome: | Meterpreter | session | established |  |  |  |  |
| intentionally terminate after achieving its attack objective, | [Iter. 4–6 \| EXFILTRATE] |  |  |  |  |  |  |  |
| rather than exhaustively enumerating all vulnerabilities. These | search | -f | flag.txt |  |  |  |  |  |
| differences reflect a deliberate trade-off between coverage- | search | -d | / | -f | flag.txt |  |  |  |
| oriented security assessment and goal-driven autonomous red | cat | /home/msfadmin/flag.txt |  |  |  |  |  |  |
| teaming, rather than a direct performance comparison. | Outcome: | Sensitive file successfully retrieved. |  |  |  |  |  |  |
| nmap -sS -sV | 192.168.102.197 | cmd: | apache_mod_cgi_bash_env_exec, |  |  |  |  |  |
| use | exploit/multi/http/ | Exfiltration Memory ( | M | EXFILTRATE | ) |  |  |  |
| exploit | cmd: | search | -f | flag.txt, |  |  |  |  |
| ( | RPORT | ); | cmd: | search | -d | / | -f | flag.txt, |

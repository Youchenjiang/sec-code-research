---
title: "xOffense: An Autonomous Multi-Agent Framework for Penetration Testing with Domain-Adapted Large Language Models"
author: "Phung Duc Luong; Le Tran Gia Bao; Nguyen Vu Khai Tam; Dong Huu Nguyen Khoa; Nguyen Huu Quyen; Van-Hau Pham; Phan The Duy"
creator: "arXiv GenPDF (tex2pdf:a6404ea)"
pages: 18
---

# xOffense: An Autonomous Multi-Agent Framework for Penetration Testing with Domain-Adapted Large Language Models

> **作者**：Phung Duc Luong; Le Tran Gia Bao; Nguyen Vu Khai Tam; Dong Huu Nguyen Khoa; Nguyen Huu Quyen; Van-Hau Pham; Phan The Duy
> **總頁數**：18 頁

---

## Page 1

xO ff ense: An Autonomous Multi-Agent Framework for Penetration Testing with

Domain-Adapted Large Language Models

Phung Duc Luong a,b , Le Tran Gia Bao a,b , Nguyen Vu Khai Tam a,b , Dong Huu Nguyen Khoa a,b , Nguyen Huu Quyen a,b ,

Van-Hau Pham a,b , Phan The Duy a,b, ∗

a Information Security Lab, University of Information Technology, Ho Chi Minh City, Vietnam

b Vietnam National University Ho Chi Minh City, Ho Chi Minh City, Vietnam

Abstract

Penetration testing plays a critical role in assessing the security of modern information systems; however, existing automated

approaches based on machine learning, deep learning, or reinforcement learning remain constrained by simplified action spaces,

high computational overhead, and limited reasoning across multi-stage workflows such as reconnaissance, vulnerability analysis,

and exploitation. Recent large language model (LLM)-based systems have shown promise in addressing these challenges, yet they

often rely on large-scale or proprietary models, resulting in high cost, limited scalability, and suboptimal adaptability in complex

environments. This paper introduces xO ff ense, an AI-driven multi-agent framework for autonomous penetration testing that trans-

forms traditional expert-driven processes into fully automated and scalable workflows. The proposed system leverages a fine-tuned

mid-scale open-source LLM to perform structured reasoning and decision-making, while decomposing the pentesting pipeline into

specialized agents responsible for reconnaissance, vulnerability scanning, and exploitation. An orchestration mechanism coor-

dinates inter-agent collaboration to ensure coherent multi-phase execution. In addition, domain-specific fine-tuning with chain-

of-thought penetration testing data enables accurate command generation and consistent multi-step reasoning across tasks. The

e ff ectiveness of xO ff ense is validated on two representative benchmarks, AutoPenBench and AI-Pentest-Benchmark. Experimental

results demonstrate that the proposed framework consistently outperforms existing LLM-based approaches, achieving a sub-task

completion rate of 79.17% and surpassing state-of-the-art systems in both e ff ectiveness and reliability. These results highlight

that integrating domain-adapted mid-scale LLMs within a structured multi-agent architecture can provide a cost-e ffi cient, scalable,

and reproducible solution for autonomous penetration testing, o ff ering a practical direction for deploying intelligent cybersecurity

systems in real-world settings.

Keywords: Autonomous penetration testing, Large language models, Multi-agent systems, Intelligent decision-making,

Cybersecurity automation, Domain-adapted learning

1. Introduction Early attempts to narrow this gap focused on fully determin-

istic or heuristic automation. Notable examples include Deep-

| Pentest remains one of the most e | ff | ective ways to assess | Exploit [3], and Metasploit-based scripting frameworks [4] that |
| --- | --- | --- | --- |
| the real-world security posture of modern information systems. | chain banner grabbing, version mapping, and exploit invoca- |  |  |
| Unfortunately, the prevailing approach manual testing conducted | tion. Despite their e | ffi | ciency, these systems rely on rigid expert |
| by small teams of human experts cannot keep pace with today’s | rules and struggle with unseen configurations or incomplete in- |  |  |

rapidly expanding attack surface. In 2024 alone, the National

arXiv:2509.13021v2 [cs.CR] 27 Apr 2026 formation.

| Vulnerability Database listed more than 29,000 new CVEs, a | A second, more adaptive line of work leverages | RL | . Sys- |  |
| --- | --- | --- | --- | --- |
| 38% year-over-year increase [1] [2]. As networks grow in scale | tems like IAPTS [5] and HA-DRL [6] model pentest as a se- |  |  |  |
| and complexity, the gap between the appearance of new vulner- | quential decision-making problem in partially observable envi- |  |  |  |
| abilities and the ability of security professionals to detect and | ronments, enabling agents to autonomously explore and learn |  |  |  |
| remediate them is widening. | This growing imbalance under- | e | ff | ective attack strategies through interaction and reward-based |
| scores the urgent necessity for automated and intelligent pentest | learning. | RL agents can, in principle, discover novel attack |  |  |
| solutions. | paths, yet in practice they face two key obstacles: (i) their action |  |  |  |

space must be heavily simplified such as “scan port”, “exploit

| ∗ | Corresponding author | CVE-xxx”, and (ii) training requires a large number of environ- |  |  |
| --- | --- | --- | --- | --- |
| Email addresses: | 21522312@gm.uit.edu.vn | (Phung Duc Luong | ), | ment interactions that are expensive to obtain and seldom trans- |
| 22520105@gm.uit.edu.vn | (Le Tran Gia Bao | ), | fer between real networks. Consequently, even state-of-the-art |  |
| 22521293@gm.uit.edu.vn | (Nguyen Vu Khai Tam | ), | RL-based pentesters achieve modest coverage and require sig- |  |

23520734@gm.uit.edu.vn (Dong Huu Nguyen Khoa ),

| quyennh@uit.edu.vn | (Nguyen Huu Quyen | ), | haupv@uit.edu.vn | nificant engineering to integrate new tools or protocols. |  |
| --- | --- | --- | --- | --- | --- |
| (Van-Hau Pham | ), | duypt@uit.edu.vn | (Phan The Duy | ) | These limitations illustrate that purely DL or RL-based au- |
| Preprint submitted to Elsevier | April 28, 2026 |  |  |  |  |

---

## Page 2

| tomation is insu | ffi | cient for the inherently multi-phase and dy- | ability in nuanced or low-visibility environments. |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| namic nature of pentest. To overcome this, recent works have | Beyond simply replacing the core language model, xOf- |  |  |  |  |  |  |
| turned toward AI agent-based paradigms, in which multiple | fense also incorporates a context-aware prompting scheme we |  |  |  |  |  |  |
| specialized agents collaborate to emulate the workflow of hu- | refer to as grey-box prompting. In this setup, agents are equipped |  |  |  |  |  |  |
| man red teams. | In such systems, each agent assumes a dis- | with partial system insights, such as protocol hints, observed |  |  |  |  |  |
| tinct role: | a | Reconnaissance Agent | focuses on host and ser- | services, or prior scan summaries, enabling them to make more |  |  |  |
| vice discovery, a | Vulnerability Analysis Agent | correlates find- | informed decisions without relying on full system disclosure. |  |  |  |  |
| ings with CVE and CWE knowledge bases, and an | Exploita- | This strategy preserves the operational constraints of black-box |  |  |  |  |  |
| tion Agent | generates and tests candidate payloads. This agent- | testing while o | ff | ering minimal structured guidance, striking a |  |  |  |
| oriented decomposition enables modularity, context retention | balance between realism and agent e | ff | ectiveness. By preserv- |  |  |  |  |
| across phases, and the possibility of scaling to complex attack | ing VulnBot’s three-phase pipeline reconnaissance, scanning, |  |  |  |  |  |  |
| paths that traditional ML | / | DL | / | RL pipelines cannot handle. | and exploitation xO | ff | ense ensures compatibility with existing |
| Recent advancements in LLMs have opened new possibil- | workflows, facilitates direct benchmarking, and provides a ro- |  |  |  |  |  |  |
| ities for automating modern pentest. | Leveraging their strong | bust foundation for comparative evaluation. |  |  |  |  |  |
| reasoning and code generation capabilities, LLMs have been | In this paper, we present the design, implementation, and |  |  |  |  |  |  |
| adopted in several research prototypes such as PentestGPT [7], | evaluation of xO | ff | ense, a lightweight, domain-adaptive, and |  |  |  |  |
| PentestAgent [8], and VulnBot [9], where models assist or au- | highly e | ff | ective autonomous pentest system. | Our key contri- |  |  |  |
| tonomously conduct reconnaissance, scanning, and exploita- | butions are as follows: |  |  |  |  |  |  |

tion. In particular, VulnBot represents a major step forward: it

However, most of these systems rely heavily on extremely

large or commercial LLMs, such as GPT-4o, LLaMA3-70B, or

DeepSeek-V3. Despite their capabilities, these models present

significant operational hurdles including high resource consump-

tion, costly API dependencies, and limited adaptability to domain-

specific fine-tuning. Additionally, their general-purpose nature

often leads to hallucinations, loss of context across phases, or

poor command translation in complex penetration workflows.

As such, there is a pressing need to explore whether smaller,

tasks like pentest. Despite their size, large-scale LLMs still suf-

present xO ff ense, a refined evolution of the VulnBot framework

that substitutes its dependence on large, general-purpose mod-

2

manner.

• A domain-adapted mid-scale LLM. At the core of our

system lies Qwen3-32B, a 32B-parameter open-source

model fine-tuned with Chain-of-Thought (CoT) pentest

data. This adaptation empowers the model with precise

multi-phase reasoning, accurate tool command genera-

tion, and strong adaptability in complex exploitation work-

flows.

LLMs.

| frames pentest as a collaborative workflow between specialized | • | An AI-driven multi-agent pentest system. | We propose |  |  |
| --- | --- | --- | --- | --- | --- |
| LLM agents guided by a Penetration Task Graph (PTG), en- | a novel agent-based framework in which specialized agents |  |  |  |  |
| abling the simulation of expert-level pentesting with limited or | collaborate to cover all critical phases of pentest recon- |  |  |  |  |
| no human intervention. Empirical results from benchmarks like | naissance, vulnerability analysis, and exploitation. This |  |  |  |  |
| AutoPenBench [10] and AI-Pentest-Benchmark [11] have vali- | design emulates the workflow of human red teams, en- |  |  |  |  |
| dated VulnBot’s capacity to outperform other automated meth- | sures modularity across tasks, and enables coherent or- |  |  |  |  |
| ods in structured testing environments. | chestration of complex attack paths in an autonomous |  |  |  |  |
| fine-tuned open-source models can serve as more e | ffi | cient, spe- | • | Grey-box phase prompting. | We introduce a context- |
| cialized alternatives, which o | ff | ers better controllability, lower | aware prompting mechanism that selectively integrates |  |  |
| cost, and targeted reasoning. | environmental cues such as observed protocols, discov- |  |  |  |  |
| This work is motivated by two core observations. | First, | ered services, and prior scan outputs into the agent rea- |  |  |  |
| while large LLMs have demonstrated strong potential in se- | soning process. This strategy strikes a balance between |  |  |  |  |
| curity domains, scale alone does not guarantee e | ff | ectiveness, | black-box and white-box testing, reducing context loss |  |  |
| particularly when models are deployed in structured, multi-step | and improving continuity across phases. |  |  |  |  |
| fer from context loss across phases, generate incorrect tool us- | • | Extensive empirical validation. | We conduct rigorous |  |  |
| age, and require significant human supervision. Second, most | evaluations of xO | ff | ense on AutoPenBench and AI-Pentest- |  |  |
| current systems adopt LLMs as black-box assistants or instruc- | Benchmark, demonstrating state-of-the-art performance |  |  |  |  |
| tion followers, without integrating deeper task-specific guid- | in both synthetic and real-world pentest scenarios. The |  |  |  |  |
| ance or domain adaptation. To address these limitations, we ex- | system achieves superior task and sub-task completion |  |  |  |  |
| plore an alternative paradigm: leveraging a mid-sized, domain- | rates compared to prior methods, confirming the e | ff | ec- |  |  |
| adapted LLM that is explicitly trained for pentest tasks. | We | tiveness of multi-agent orchestration and domain-adapted |  |  |  |
| els with a fine-tuned Qwen3-32B [12], a 32-billion-parameter | The remainder of this paper is organized as follows. Sec- |  |  |  |  |
| open-source language model. | Through dedicated training on | tion 2 reviews prior studies on pentest and automation approaches, |  |  |  |

pentest workflows, including vulnerability scanning, exploit craft- while Section 3 introduces the fundamental concepts that un-

| ing, and security tool interaction, xO | ff | ense achieves sharper | derpin automated systems. Section 4 describes the architecture |
| --- | --- | --- | --- |
| task alignment, enhanced operational fidelity, and greater adapt- | of the proposed xO | ff | ense framework, including its fine-tuned |

---

## Page 3

| Qwen3-32B model, grey-box prompting strategy, and multi- | structures collaboration via a PTG to preserve phase order (re- |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| agent orchestration. We describe the experimental settings and | con | → | scanning | → | exploitation) and constrain branching; re- |
| benchmark datasets, evaluation metrics in Section 5. | In Sec- | ported results include 30.3% overall and 69.05% sub-task com- |  |  |  |
| tion 6 empirical results on two benchmarks and real-world ex- | pletion on AutoPenBench and strong performance on AI-Pentest- |  |  |  |  |
| ploitation scenarios are reported and analyzed. Section 7 dis- | Benchmark [9, 10, 11]. RefPentester [19] introduces knowledge- |  |  |  |  |
| cusses potential threats to validity and their implications for | informed self-reflection tied to stage recognition, improving re- |  |  |  |  |
| generalizability. In Section 8, we discuss ethical considerations | covery from failed operations on Hack The Box targets. Rapid- |  |  |  |  |
| and responsible use of the proposed framework, including po- | Pen targets the | initial foothold | (IP-to-shell) with a ReAct-style |  |  |
| tential misuse risks, deployment constraints, and implications | loop and retrieval of exploit knowledge, demonstrating fully |  |  |  |  |
| for defensive cybersecurity research. | Finally, Section 9 con- | autonomous compromises on HTB within minutes at modest |  |  |  |
| cludes the paper and outlines directions for future research. | cost [20]. | The work of Weber et al. | [21] presents Perses, |  |  |

2. Related work

Deterministic orchestrators, such as DeepExploit, integrate

scanners and exploit frameworks, including Metasploit, Nmap,

Nikto, and WPScan, but rely on rigid rules and shallow evi-

dence fusion, limiting adaptability to dynamic attack scenarios

[3, 4, 13, 14, 15]. RL-based agents formulate pentesting as a

Partially Observable Markov Decision Process (POMDP) with

reward shaping, providing a principled approach to automating

attack strategies [5, 6, 16]. Notably, the Raiju framework has

made significant strides in automating post-exploitation tasks

by leveraging RL algorithms, specifically Advantage Actor-Critic

(A2C) and Proximal Policy Optimization (PPO) [17]. Inte-

grated with Metasploit, Raiju trains specialized agents to per-

form tasks such as privilege escalation, hashdump gathering,

and lateral movement in real-world environments, achieving a

success rate exceeding 84% across diverse attack types in four

PentestGPT demonstrates a modular, self-interacting scaf-

fold where an LLM plans, parses tool outputs, and synthesizes

commands; this closes the perception ↔ action loop while mit-

igating context loss via summarization [7]. AutoAttacker fo-

cuses on post-breach realism with shell / Metasploit control across

PentestAgent adopts RAG-grounded, role-based collabora-

tion (reconnaissance, triage, exploitation) to reduce hallucina-

tions and improve next step selection [8]. Additionally, VulnBot

3

a notable e ff ort to enable small language models (SLMs) to

perform automated privilege escalation through an extensible,

role-specialized multi-LLM architecture. Perses shows that het-

mander, Summariser and domain-specific Overseers, can sub-

stantially improve exploitation of simple misconfigurations. Im-

portantly, the evaluation in Perses is narrowly scoped: experi-

ments are conducted primarily on FreeBSD targets, employ a

limited and largely handcrafted set of privilege escalation vul-

nerabilities, and use a threat model tailored to configuration er-

rors rather than broad end-to-end attacks. As a result, Perses

demonstrates the viability of SLM heterogeneity in constrained

environments but leaves open questions about transferability

to full penetration pipelines (reconnaissance, scanning, multi-

stage exploitation), complex real-world services, and heteroge-

neous network topologies.

2.4. Focused exploit studies (one-day, zero-day) and CTF-style

agents.

cases with GPT-4. For broader skill evaluation, HackSynth

(PicoCTF / OverTheWire; 200 tasks) [24], while NYU CTF Bench

(NeurIPS D&B) contributes a scalable open-source dataset and

automation framework (200 CSAW CTF tasks) [25].

2.5. Benchmarks and methodology

a few benchmarks have begun to dominate experimental pro-

pear most frequently in recent studies, reflecting their alignment

with realistic, multi-phase pentesting workflows and their abil-

ity to grade performance across autonomy levels and subtasks.

Conversely, more specialized testbeds such as CVE-Bench tar-

get specific exploitability dimensions, such as real-world CVEs

in web contexts, and thus see adoption in works focusing on

vulnerability exploitation rather than full-cycle orchestration.

| 2.1. Pre-LLM automation and RL | erogeneity, which assigns lightweight models to Planner, Com- |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| tested environments. However, RL-based approaches, includ- | Fang et al. [22] show that, given CVE descriptions, GPT-4 |  |  |  |  |
| ing Raiju, face two primary challenges: (i) the need for exten- | can exploit 87% of a 15 one-day vulnerability set, whereas other |  |  |  |  |
| sive state and action space engineering, and (ii) limited cross- | LLMs and scanners achieve 0%; without the description, suc- |  |  |  |  |
| target transferability without costly retraining. | These limita- | cess drops markedly (7%). Zhu et al. [23] further extend this |  |  |  |
| tions highlight the need for more adaptive methods, such as | to teams of agents ( | HPTSA | ) for | zero-day | web vulnerabilities, |
| LLMs, to enhance e | ffi | ciency and generalization in pentest. | reporting up to 42% pass@5 and 18% pass@1 on 14 real-world |  |  |
| 2.2. LLM single-few-agent pipelines | proposes a two-module agent and two CTF-based benchmarks |  |  |  |  |
| Windows | / | Linux, executing multi-step attacks [18]. Both high- | The emergence of AI-driven pentest has been accompanied |  |  |
| light that language-grounded synthesis and disciplined tool use | by a rapid proliferation of evaluation suites designed to mea- |  |  |  |  |
| can automate substantial portions of a Cyber Kill Chain, yet | sure autonomy, tool integration, and end-to-end performance |  |  |  |  |
| often rely on large backbones and ad-hoc grounding. | under controlled conditions. While the space remains nascent, |  |  |  |  |
| 2.3. LLM multi-agent orchestration | tocols. Notably, | AutoPenBench | and | AI-Pentest-Benchmark | ap- |

---

## Page 4

| Capture The Flag resources such as | NYU CTF Bench | and the | Formally, let | T | denote a target system with configuration |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| datasets introduced by | HackSynth | have also gained traction, | space | C | and attack surface | S | . An automated pentesting opera- |
| particularly for skill-granular or task-decomposed evaluations, | tion can be represented as a pipeline: |  |  |  |  |  |  |

though their scenarios often di ff er from operational pentests in

Within this landscape, AutoPenBench o ff ers open and stan-

abling reproducible end-to-end penetration tests [11], thereby

ing autonomy levels, and reporting detailed error modes to pre-

vent overestimation of capabilities [27].

Relative to single-agent PentestGPT [7] and post-breach

oritizing mid-scale, open backbones for cost-e ff ective, on-prem

aligning evaluation with open substrates (AutoPenBench, AI-

fixed budgets and sub-task breakdowns [10, 11, 26, 27].

2.7. Takeaways.

Outcomes hinge on (i) grounding quality (RAG / summaries / -

producible deployment with mid-scale open models, PTG struc-

ture, and grey-box prompts under open, reproducible protocols

3. Background

Pentest aims to evaluate the security of a target system by

simulating adversarial behavior across phases such as recon-

naissance, vulnerability enumeration, exploitation, and privi-

4

attack paths).

3.2. Multi-Agent AI Systems

Multi-Agent Systems (MAS) provide a natural architecture

cialized agent. For example:

loads

• Reporting Agent: summarizes results, attack graphs, and

remediation advice.

ordination.

Within MAS, LLMs provide reasoning, contextual under-

standing, and code synthesis capabilities that align well with

pentest workflows. The central problem is, given an attack con-

steps or payloads A that maximize the likelihood of successful

exploitation:

g : C 7 → A

ment, fine-tuning, and quantization (AWQ / INT4), making them

| scope and realism. | f | : | T | 7 | → { | R | , | V | , | E | , | P | } 7 → | O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dardized graded tasks spanning web, network, and cryptographic | where | R | are the reconnaissance results (asset discovery, ser- |  |  |  |  |  |  |  |  |  |  |  |
| targets, with configurable autonomy modes to support com- | vice mapping), | V | are detected vulnerabilities, | E | denotes the |  |  |  |  |  |  |  |  |  |
| parisons between orchestration strategies and model backbones | exploit simulation results, | P | represents the privilege escalation |  |  |  |  |  |  |  |  |  |  |  |
| [10]. | AI-Pentest-Benchmark provides VM-based targets, en- | attempts and | O | is the structured output (reports, risk scores, or |  |  |  |  |  |  |  |  |  |  |
| supporting performance attribution across discovery, exploita- | Such pipelines resemble MLOps workflows, where data col- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tion, and post-exploitation phases. CVE-Bench grounds eval- | lection, model inference, and result verification are continu- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| uation in real-world web CVEs, reporting typical success rates | ously orchestrated. In this analogy, reconnaissance and vulner- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| in the low teens even for state-of-the-art agents, highlighting | ability scanning serve as data ingestion, exploitation is model |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the gap between research prototypes and robust autonomy [26]. | inference, and reporting acts as the ’evaluation’ stage. By au- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Methodological recommendations across these works increas- | tomating this operation, APT enables repeatability, scalability, |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ingly emphasize standardizing budget constraints, clearly label- | and integration into CI | / | CD security pipelines. |  |  |  |  |  |  |  |  |  |  |  |
| 2.6. Positioning of our work | for automated pentest by assigning each pentest phase to a spe- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| AutoAttacker | [18], we retain a multi-agent | / | PTG discipline akin | • | Reconnaissance Agent: enumerates hosts, ports, and ser- |  |  |  |  |  |  |  |  |  |
| to | PentestAgent | / | VulnBot | [8, 9] but di | ff | er in three ways: (i) pri- | vices (similar to VulnBot’s ’Recon Agent’ [9]). |  |  |  |  |  |  |  |
| deployment; (ii) employing | grey-box phase prompting | to main- | • | Vulnerability Analysis Agent: correlated scan data with |  |  |  |  |  |  |  |  |  |  |
| tain phase continuity while e | ff | ectively limiting drift; and (iii) | CVE | / | CWE knowledge bases. |  |  |  |  |  |  |  |  |  |
| Pentest-Benchmark, and where applicable CVE-Bench) under | • | Exploitation Agent: generates and tests candidate pay- |  |  |  |  |  |  |  |  |  |  |  |  |
| validators) and (ii) | orchestration discipline | (roles | / | PTG | / | reflec- | Agents communicate through a task manager or memory |  |  |  |  |  |  |  |
| tion). Single-agent pipelines set baselines; role-structured multi- | module, allowing modularity and fault tolerance. Frameworks |  |  |  |  |  |  |  |  |  |  |  |  |  |
| agent systems consistently improve reliability; reflective and | like | CAMEL | [29] show that role-conditioned LLM agents can |  |  |  |  |  |  |  |  |  |  |  |
| IP-to-shell variants further push autonomy at kill-chain ends; | collaborate e | ff | ectively on complex objectives. | In our system |  |  |  |  |  |  |  |  |  |  |
| one-day | / | zero-day studies quantify limits of discovery vs. ex- | xO | ff | ense | , MAS design ensures that each o | ff | ensive task is han- |  |  |  |  |  |  |
| ploitation [22, 23]. Our approach emphasizes cost-e | ff | ective, re- | dled by a role-specialized model while maintaining global co- |  |  |  |  |  |  |  |  |  |  |  |
| [10, 11, 26, 27]. | 3.3. LLM-based O | ff | ensive Agents |  |  |  |  |  |  |  |  |  |  |  |
| 3.1. Automated Pentest | text | C | (system description, logs, CVEs), generate actionable |  |  |  |  |  |  |  |  |  |  |  |
| lege escalation. | Manual execution is e | ff | ective but limited by | Although proprietary LLMs, such as GPT-4 and Claude, of- |  |  |  |  |  |  |  |  |  |  |
| human resources and scalability. Automated Pentest (APT) ad- | fer strong performance, they introduce limitations in cost, re- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| dresses these limitations by orchestrating these phases through | producibility, and security control. Therefore, we adopt open- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| intelligent agents and machine learning models. | source models such as | Qwen3 | , which support local deploy- |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 5

Table 1: Comparison of representative automated pentesting systems and benchmarks (grid-lined). Criteria emphasize architecture, scope, grounding, tools,

autonomy, and evaluation.

Work Architecture

(Arch.) Scope / Phase Grounding /

Memory

APB = AutoPenBench [10]; AIPB = AI-Pentest-Benchmark [11]; CVEB

To mitigate risks such as hallucination or unsafe outputs,

ecution environments before results are accepted.

Adapting LLMs to o ff ensive security tasks requires task-

prefix embeddings are optimized. However, this method often

struggles to capture deeper structural knowledge, and its e ff ec-

tiveness diminishes when reasoning requires multi-step tool in-

teraction or long-context planning, both of which are essential

5

Tool Use Evaluation

& Highlights

= CVE-Bench [26]. “s-rate” denotes success rate.

∆ W = AB , A ∈ R , B ∈ R , r ≪ min( d , k )

′

W = W + α AB

adaptation.

tion 4.

4. Methodology

imal computational overhead.

| PentestGPT [7] | SA | Web | + | Net (multi-phase) | SUM (module summaries) | Parse scans | → | cmd synth. | USENIX’24 cases | / | bench; modular pipeline |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AutoAttacker [18] | SA (post) | Post-breach, OpSec realism | CTX (in-session) | Shell, Metasploit | Simulated org (Win | / | Linux); multi-step attacks |  |  |  |  |  |  |
| PentestAgent [8] | MA | Web focus (ext. assess.) | RAG | + | MEM | Scanners, PoCs | Bench | + | HTB; reduced hallucinations via RAG |  |  |  |  |
| VulnBot [9] | MA | + | PTG | Full cycle (recon | → | exp.) | Phase SUM (PTG state) | Nmap, Nikto, Metasploit | AutoPenBench (30.3% overall; 69.05% sub-task), AIPB best-of-six |  |  |  |  |
| RefPentester [19] | MA | + | RFL | Stage-aware triage | / | exp. | Reflection | + | knowledge | Std. toolchain | HTB “Sau”: | + | 16.7% vs GPT-4o baseline |
| Perses [21] | MA (multi-LLM) | Privilege escalation | HET | (heterogeneous model | / | task) | Tool-grounded (details in paper) | FreeBSD systems; small-LLM focus |  |  |  |  |  |
| RapidPen [20] | SA | IP | → | Shell | (initial foothold) | MEM | + | exploit retrieval | Scan | → | exploit loop | HTB: autonomous shells in minutes; low cost |  |
| One-Day Agent [22] | SA | Web (one-day CVEs) | CVE-guided CTX | Browser, tools | 87% (GPT-4, with CVE desc.); 7% w | / | o desc. |  |  |  |  |  |  |
| HPTSA (Teams) [23] | MA (hier. | / | team) | Web (zero-day) | Planner | + | experts | Browser, task agents | 42% pass@5; 18% pass@1 on 14 real vulns |  |  |  |  |
| HackSynth [24] | SA (2-mod.) | CTF (200 tasks) | Planner | + | summarizer | Sandbox tools | PicoCTF | / | OTW benchmarks; GPT-4o best |  |  |  |  |
| AutoPentest [28] | MA (LangChain) | Black-box (enum | → | exp.) | Prompting | + | MEM | Std. scans | / | exploits | GPT-4o-based prototype; open code |  |  |
| CVE-Bench [26] | Bench | Real web CVEs | – | – | Up to 13% s-rates for SOTA agents |  |  |  |  |  |  |  |  |
| AutoPenBench [10] | Bench | Mixed (Web | / | Net | / | CRPT) | – | – | 33 tasks; autonomy and milestone scoring |  |  |  |  |
| NYU CTF Bench [25] | Bench | CTF (CSAW; 200) | – | Tool-integrated | NeurIPS D&B; open dataset | + | automation |  |  |  |  |  |  |
| Our work | MA | + | PTG | Full cycle (Web | + | Net) | GBP | + | MEM | Broad scan | / | exploit | APB, AIPB, (opt.) CVEB; mid-scale open LLM |

Legend: SA = Single-agent; MA = Multi-agent; PTG = Penetration Task Graph; RFL = Reflection; SUM = Summaries; RAG = Retrieval-Augmented Generation;

MEM = Explicit memory; CTX = In-session context; HET = Heterogeneity (multi-LLM model / task selection); GBP = Grey-box phase prompting;

| suitable for o | ff | ensive research environments where sensitive data | dates | ∆ | W | lie in a low-rank subspace: |
| --- | --- | --- | --- | --- | --- | --- |
| cannot leave the infrastructure. | d | × | r | r | × | k |
| LLM agents are sandboxed and validated against controlled ex- | and the e | ff | ective weight during inference is |  |  |  |
| 3.4. Fine-tuning Methods for O | ff | ensive LLMs | where | α | is a scaling factor controlling the magnitude of the |  |
| specific specialization beyond general pre-trained knowledge, | Considering the need to adapt a 32B-parameter model such |  |  |  |  |  |
| and several parameter-e | ffi | cient fine-tuning approaches have been | as Qwen3 under realistic hardware constraints, this work adopts |  |  |  |

explored, including Prefix-Tuning, Adapter-based methods, Low- LoRA fine-tuning. This approach makes it possible to embed

| Rank Adaptation (LoRA) and its extension QLoRA. | o | ff | ensive knowledge, including vulnerability patterns, exploit |
| --- | --- | --- | --- |
| Prefix-Tuning or P-Tuning v2 appends task-specific contin- | reasoning, and payload generation, e | ffi | ciently while preserving |
| uous vectors or tokens to the input prompt. Its advantages lie | the base model’s general-purpose capabilities. Detailed dataset |  |  |
| in simplicity and a very low memory footprint, since only the | construction and the training procedure are described in Sec- |  |  |
| in pentest. | 4.1. Overview of the proposed framework |  |  |
| Adapter-based methods insert small trainable modules within | xO | ff | ense is an innovative, lightweight framework for au- |
| transformer layers, enabling modular adaptation to new tasks. | tonomous pentest, engineered to replicate the collaborative dy- |  |  |
| They provide good task isolation and make it possible to reuse | namics of human security teams while operating within resource- |  |  |
| the same backbone across di | ff | erent domains with minimal ad- | constrained environments. By harnessing compact LLMs with |
| ditional parameters. Nonetheless, these methods introduce ex- | approximately 32 billion parameters, xO | ff | ense eliminates de- |
| tra inference latency due to the added modules, and their lim- | pendency on commercial APIs, enabling deployment on stan- |  |  |
| ited capacity makes them less e | ff | ective for embedding highly | dard hardware. The framework decomposes the intricate pro- |
| domain-specific procedural knowledge such as exploit reason- | cess of pentest into three meticulously designed phases recon- |  |  |
| ing or vulnerability chaining. | naissance, scanning, and exploitation coordinated through a so- |  |  |
| LoRA and its extension QLoRA decompose weight updates | phisticated multi-agent architecture. Comprising five core com- |  |  |
| into low-rank matrices, significantly reducing the number of | ponents Task Orchestrator, Knowledge Repository, Command |  |  |
| trainable parameters while retaining the expressive power of | Synthesizer, Action Executor, and Information Aggregator. xOf- |  |  |
| the base model. LoRA achieves a balance between e | ffi | ciency | fense ensures seamless task progression, robust information man- |
| and performance: it requires far fewer resources than full fine- | agement, and precise execution. | This section elucidates the |  |
| tuning, adds negligible inference overhead, and can e | ff | ectively | system’s architecture, role delineation, task coordination, inter- |
| embed specialized knowledge without erasing the general rea- | agent communication, and execution mechanisms, underscor- |  |  |
| soning ability of the original model. Conceptually, weight up- | ing its e | ffi | cacy in addressing cybersecurity challenges with min- |

---

## Page 6

| The operational workflow of | xO | ff | ense | , illustrated in Figure | WPScan | [15] for WordPress vulnerabilities, | sqlmap | [34] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1, initiates when a user submits a pentest objective, such as | for SQL injection testing for comprehensive vulnerability |  |  |  |  |  |  |  |
| “Identify vulnerabilities on IP 192.168.X.X and retrieve root- | scanning. This phase prioritizes exploitable weaknesses |  |  |  |  |  |  |  |
| level flags.” This task description serves as the Initial Context, | to streamline progression. |  |  |  |  |  |  |  |

which is passed to the Task Orchestrator for comprehensive

instruction, or recent task results.

Each task within the TCG is processed through an iterative

and adaptive loop involving Command Synthesis, Execution,

Feedback Analysis, and Dynamic Plan Update. The Command

Synthesizer , fine-tuned using lightweight LoRA techniques, trans-

lates task directives into precise, tool-specific commands, which

concise directives for the subsequent phase, such as Scanning ,

re-planning, is later formalized in Algorithm 1. The workflow

4.2. Role Specialization

To navigate the complexity of pentest, xO ff ense employs

a role specialization strategy, mitigating the risk of informa-

resource utilization and maintains precision in task execution,

stages.

sive intelligence gathering, cataloging network configu-

rations, open ports, and service details. Tools such as

Nmap [13] for network scanning, Dirb [31] for directory

enumeration, Gobuster [32] for brute-forcing hidden di-

integrated. For instance, a task might execute nmap -sV

• Scanning Phase : Building on reconnaissance insights,

scanning agents identify vulnerabilities and misconfigu-

rations using tools like Nikto [14] for web server analysis,

This structured delineation ensures that each phase lever-

ages prior findings, fostering a cohesive testing process and mit-

igating the risk of fragmented analyses.

4.3. Task Coordination and Reflection

• Operation Type: Specifies whether the task involves au-

tomated shell commands, such as nmap , or manual inter-

vention.

Command Synthesizer .

errors.

• Completion Status: Indicates whether the task is com-

pleted or pending.

tion outcomes. For instance, a task designed to perform user

6

| plan generation. The orchestrator constructs a Task Coordina- | • | Exploitation Phase | : Agents exploit identified vulnera- |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tion Graph (TCG), decomposing the penetration objective into | bilities to gain unauthorized access or escalate privileges, |  |  |  |  |  |  |  |  |
| a structured sequence of tasks with clearly defined dependen- | employing tools such as | Metasploit | [4] for exploit devel- |  |  |  |  |  |  |
| cies. To enhance contextual accuracy, it queries the | Knowledge | opment, | Hydra | [35] for credential brute-forcing, | John the |  |  |  |  |
| Repository | a vector-based database via a Retrieval-Augmented | Ripper | [36] for password cracking, and | ExploitDB | [37] |  |  |  |  |
| Generation (RAG) mechanism, which is taken from Langchain- | for sourcing exploit scripts. | For example, a task might |  |  |  |  |  |  |  |
| Chatchat [30], retrieving relevant penetration knowledge based | deploy a Metasploit module to exploit a known CVE, fol- |  |  |  |  |  |  |  |  |
| on inputs such as the initial task description, the current task’s | lowed by privilege escalation via a custom script. |  |  |  |  |  |  |  |  |
| are executed by the | Action Executor | utilizing a MemAgent- | The TCG and its integrated | Check and Reflection Mecha- |  |  |  |  |  |
| enhanced context management system to handle verbose out- | nism | form the cornerstone of xO | ff | ense’s penetration path plan- |  |  |  |  |  |
| puts e | ff | ectively. | Post-execution, task outcomes are evaluated | ning, enabling systematic task execution and adaptive plan re- |  |  |  |  |  |
| and relayed back to the orchestrator, which marks tasks as com- | finement. These components address the challenges of limited |  |  |  |  |  |  |  |  |
| pleted or triggers reflection and re-planning in case of failures. | context windows and inadequate error handling, ensuring ro- |  |  |  |  |  |  |  |  |
| Upon completing all tasks within a phase, such as | Reconnais- | bust and dynamic testing workflows. Their operational logic is |  |  |  |  |  |  |  |
| sance | , the | Information Aggregator | consolidates outputs into | illustrated in Algorithm 1, Algorithm 2, and Algorithm 3. |  |  |  |  |  |
| ensuring contextual coherence and minimizing token overhead. | 4.3.1. Task Coordination Graph |  |  |  |  |  |  |  |  |
| This orchestration-execution-feedback loop is consistently ap- | The TCG is a structured acyclic digraph, defined as | G | = |  |  |  |  |  |  |
| plied across all three phases, with each phase iteratively refin- | ( | V | , | E | ), where | V | represents individual tasks and | E | denotes de- |
| ing the attack path based on task outcomes and environmen- | pendencies, ensuring logical and conflict-free execution. Each |  |  |  |  |  |  |  |  |
| tal feedback. | The overall workflow, including execution and | task node | v | ∈ | V | encapsulates attributes such as: |  |  |  |
| terminates upon successfully achieving the defined success cri- | • | Directive: A clear instruction, such as | ”enumerate ser- |  |  |  |  |  |  |
| teria, such as privilege escalation or flag retrieval. | vices on port 80 of 192.168.X.X.” |  |  |  |  |  |  |  |  |
| tion overload and ensuring contextual coherence across phases. | • | Prerequisites: Lists tasks that must be completed prior to |  |  |  |  |  |  |  |
| By assigning agents to distinct roles, the framework optimizes | execution, ensuring sequential integrity. |  |  |  |  |  |  |  |  |
| addressing the challenge of dynamic reasoning across testing | • | Command: The tool-specific instruction generated by the |  |  |  |  |  |  |  |
| • | Reconnaissance Phase | : | Agents focus on comprehen- | • | Outcome: The execution result, capturing tool outputs or |  |  |  |  |
| rectories, and | Amass | [33] for subdomain discovery are | • | Success Status: Records whether the task was successful. |  |  |  |  |  |
| -p- <target-ip> | to map all open ports and services, | The | Task Orchestrator | generates the TCG in a JSON, which |  |  |  |  |  |
| providing a robust foundation for subsequent phases. | is compliant format, dynamically updating it based on execu- |  |  |  |  |  |  |  |  |

---

## Page 7

Figure 1: The Overall Architecture of the xO ff ense Framework.

| authentication by initiating an SSH connection attempt, target- | Executor | for execution. It also evaluates execution out- |
| --- | --- | --- |
| ing a specific service endpoint associated with remote shell ac- | comes, updating the TCG’s completion and success sta- |  |
| cess protocols, on port 22 of 192.168.X.X depends on the suc- | tuses, as shown in Algorithm 1. |  |

cessful completion of a preceding port scanning task. Subse-

| quent tasks, such as performing an exhaustive enumeration of | This structured approach ensures systematic progression, |
| --- | --- |
| writable directories for privilege escalation through misconfig- | mitigating the risk of out-of-sequence execution and enhancing |

ured permissions or publicly writable paths ( find / -writable e ffi ciency in resource-constrained environments.

2>/dev/null ) or listing running processes ( ps aux ), are con-

| tingent on this authentication. | 4.3.2. Check and Reflection Mechanism |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Figure 2 illustrates a sample TCG, with a JSON task list | The generation of erroneous commands and the lack of ef- |  |  |  |  |
| on the left detailing directives, dependencies, and commands, | fective error-handling mechanisms pose significant challenges |  |  |  |  |
| and a dependency graph on the right showing task sequences | to LLM-based pentest. xO | ff | ense addresses these issues through |  |  |
| with arrows indicating prerequisites. This formalism provides | a | Check and Reflection Mechanism | integrated into the | Task Or- |  |
| the structural foundation later used in Algorithm 1 for iterative | chestrator | , enabling continuous self-assessment and plan opti- |  |  |  |
| execution and feedback handling. | mization. The full workflow is detailed in Algorithm 1. |  |  |  |  |
| The TCG operates through two sessions: | During the | Task Session | , the | Action Executor | evaluates task |

outcomes and updates the TCG with success or failure statuses.

| • | Planning Session | : The | Task Orchestrator | constructs an | The | Planning Session | then reflects on these outcomes, revising |
| --- | --- | --- | --- | --- | --- | --- | --- |
| initial action plan tailored to the target system’s charac- | task directives and updating the TCG accordingly. Successful |  |  |  |  |  |  |
| teristics and user requirements. It decomposes the plan | tasks are retained, while failed tasks trigger a reanalysis pro- |  |  |  |  |  |  |
| into structured task lists, ensuring logical sequencing and | cess, wherein the LLM regenerates commands with corrected |  |  |  |  |  |  |
| dependency alignment. The plan is dynamically refined | parameters or alternative strategies. The updated plan is merged |  |  |  |  |  |  |
| based on execution feedback, addressing the challenge of | with previously completed tasks to preserve execution continu- |  |  |  |  |  |  |
| maintaining coherent context across phases. | ity, as demonstrated in Algorithm 2 and Algorithm 3. |  |  |  |  |  |  |

• Task Session : This session generates detailed instruc-

tions for each task, which are passed to the Command

Synthesizer for command generation and to the Action

7

---

## Page 8

Figure 2: TCG illustrating task dependencies and execution status. Completed tasks are shown in dark, the current task in orange, and pending tasks in light blue.

| Algorithm 1 | Check and Reflection Procedure | The | Knowledge Repository | supports this mechanism indi- |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Require: | TCG, Knowledge Repository | KR | rectly by assisting the | Task Orchestrator | during plan updates. |  |  |  |  |  |
| 1: | while | not all tasks completed | do | It stores embeddings of previously successful tasks and curated |  |  |  |  |  |  |
| 2: | t | ← | NextTask | (TCG) | pentest knowledge, including exploitation techniques, privilege |  |  |  |  |  |
| 3: | r | ← | Execute | (t) | escalation methods, and tool usage tutorials from sources such |  |  |  |  |  |
| 4: | if | CheckSuccess | ( | r | ) | then | as HackTricks [38] and HackingArticles [39]. When re-planning, |  |  |  |
| 5: | MarkCompleted | ( | t | ) | the | Task Orchestrator | queries this repository to retrieve the top- |  |  |  |
| 6: | StoreEmbedding | ( | t | , | r | , | KR | ) | k | most relevant past cases using vector similarity search. Re- |
| 7: | else | trieved results are re-ranked and integrated into the revised TCG, |  |  |  |  |  |  |  |  |
| 8: | K | ← | RetrieveSimilar | (t, | KR | ) | ensuring that updates benefit from prior successes. | This in- |  |  |
| 9: | t | ′ | ← | RegenerateTask | (t, | K | ) | tegration enhances resilience against hallucinated commands, |  |  |
| 10: | MergeTasks | (t’, TCG) | improves error recovery, and maintains e | ffi | ciency across itera- |  |  |  |  |  |
| 11: | end if | tive pentest phases. |  |  |  |  |  |  |  |  |

12: UpdatePlan (TCG)

Algorithm 2 UpdatePlan : LLM-driven Plan Revision

Require: Current plan P , failed task t , result r

2: F ← list of failed tasks from P

3: P new ← LLMU pdate P lan ( t , r , S , F )

4: P ⋆

← MergeTasks ( P , P new )

5: return P ⋆

Plan Update and Merge Algorithms.. The UpdatePlan and

tinuity. Upon task failure, the system calls the LLM to propose

an updated plan, then merges it with the existing TCG such that

formal pseudocode is shown in Algorithm 2 and Algorithm 3.

8

Require: Old plan P old , new plan P new

1: C ← completed-success tasks from P old

2: M ← empty list

3: for all τ ∈ C do

| 4: | if | τ | not in | P |  |
| --- | --- | --- | --- | --- | --- |
| 5: | append | τ | to | M | with reset dependencies |
| 6: | end if |  |  |  |  |

7: end for

8: for all τ ˆ ∈ P new do

| 9: | if | instruction matches a task in | C | then |
| --- | --- | --- | --- | --- |
| 10: | reuse completed task with updated dependencies |  |  |  |
| 11: | else |  |  |  |
| 13: | end if |  |  |  |

14: end for

| 13: | end while | Algorithm 3 | MergeTasks | : Success-Preserving Integration |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1: | S | ← | list of completed-success tasks from | P | new | by instruction | then |
| MergeTasks | procedures are key to preserving execution con- | 12: | append ˆ | τ | as a new task |  |  |
| all successfully completed tasks are retained, sequence numbers | 15: | update sequence numbers in | M |  |  |  |  |
| are adjusted, and only pending or failed tasks are revised. Their | 16: | return | merged plan with tasks | M |  |  |  |

---

## Page 9

| Algorithm 4 | Inter-Agent Communication via PlannerSummary | enabling fully autonomous testing. The | Command Synthesizer |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1: | Input: | Phase sequence | P | = | { | p | 1 | , | p | 2 | , . . . , | p | n | } | , Shell State Log | S | transforms TCG directives into precise, tool-specific instruc- |
| 2: | for | i | = | 1 to | n | − | 1 | do | tions tailored to the target system and phase, addressing the |  |  |  |  |  |  |  |  |
| 3: | // | Step 1: | Collect and summarize results from previous | challenge of accurate command generation. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| phase | For instance, a reconnaissance directive might yield | nmap - |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4: | history ids | ← | GetPlannerIDs | ( | p | i | ) | sS -p 22,80,443 <target-ip> | for stealth scanning, while |  |  |  |  |  |  |  |  |
| 5: | if | \| | history ids | \| | = | 0 | then | a scanning task might produce | sqlmap -u http://<target |  |  |  |  |  |  |  |  |
| 6: | context | ← | ”” | -ip>/login --batch | to test for SQL injection vulnerabili- |  |  |  |  |  |  |  |  |  |  |  |  |

| 7: | else |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8: | summary | ← | "Previous Phase: | \ | n" |  |  |  |  |
| 9: | for | each | id | in | history ids | do |  |  |  |
| 10: | plan | ← | get planner by id | ( | id | ) |  |  |  |
| 15: | context | , | ← | callLLM | ( | query | = | write summary | + |

summary , summary = False )

16: end if

17: // Step 2: Send summarized context to next phase planner

detected by Nuclei , are summarized to guide the exploitation

phase in prioritizing relevant exploits.

The Information Aggregator maintains a persistent shell state

log, tracking access levels, such as a low-privileged user ac-

cess, addressing the challenge of synthesizing information across

multiple stages.

4.5. Generative Behavior and Execution

xO ff ense supports three operational modes, specifically au-

tomatic, semi-automatic, and manual, with the automatic mode

ties or nikto -h http://<target-ip> for web server anal-

ysis. In the exploitation phase, commands like use exploit/

windows/smb/ms17_010_eternalblue in Metasploit .

integrates the innovative MemAgent [40] framework to han-

dle extended contexts e ff ectively. Drawing on MemAgent’s

segment-based processing and reinforcement learning (RL)-

by iteratively reading command results in chunks and updat-

with precision.

5. Implementation, Benchmark Dataset and Metrics

5.1. Experimental Setup

5.1.1. Attacker Environment

All pentest experiments are executed from a dedicated at-

tacker machine configured as a VMware virtual workstation

9

| 11: | for | each | task | in | plan | . | finished tasks | do | The | Action Executor | runs these commands via a Python |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12: | summary | ← | summary | \|\| "Instruction: | " | Paramiko | -based interactive shell on a Kali Linux environment, |  |  |  |  |  |  |  |  |  |
| + | task | . | instruction | simulating human interactions with high fidelity. | This com- |  |  |  |  |  |  |  |  |  |  |  |
| + | \|\| "Code: | " | + | task | . | code | ponent seamlessly processes tool-specific instructions gener- |  |  |  |  |  |  |  |  |  |
| + | \|\| "Result: | " | + | task | . | result | ated by the | Command Synthesizer | , enabling robust interaction |  |  |  |  |  |  |  |
| + | " | \ | n | \ | n" | with the target system through simulated keyboard operations. |  |  |  |  |  |  |  |  |  |  |
| 13: | end for | The | Action Executor | is optimized for the | Qwen3-32B | model, |  |  |  |  |  |  |  |  |  |  |
| 14: | end for | which, despite its constrained 16,384-token context window, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 18: | InitPlanner | ( | p | i | + | 1 | , | context | = | context | , | state | = | S | ) | optimized memory mechanism, as described in the referenced |
| 19: | end for | study, the Action Executor processes arbitrarily long outputs |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4.4. Inter-Agent Communication Mechanism | ing a fixed-length memory. This approach ensures linear com- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Seamless coordination among agents is critical for main- | putational complexity, allowing xO | ff | ense to manage verbose |  |  |  |  |  |  |  |  |  |  |  |  |  |
| taining contextual coherence across the reconnaissance, scan- | tool outputs without performance degradation, even beyond the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ning, and exploitation phases, particularly given the limited con- | Qwen3-32B’s native context limit. To address the challenge of |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| text window of compact LLMs. | xO | ff | ense employs the | Infor- | excessive or redundant output, a sophisticated filtering mecha- |  |  |  |  |  |  |  |  |  |  |  |
| mation Aggregator | to facilitate e | ffi | cient communication, con- | nism employs the MemAgent-enhanced LLM to extract critical |  |  |  |  |  |  |  |  |  |  |  |  |
| solidating verbose outputs into concise, actionable summaries | information when results exceed 8,000 characters, preserving |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| to optimize token usage and prevent information overload. The | only actionable insights for analysis. These insights are relayed |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| entire communication pipeline is operationalized in Algorithm 4. | to the | Task Orchestrator | for further processing, ensuring con- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For example, reconnaissance outputs, such as open ports | textual coherence and minimizing computational overhead. By |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (such as 22, 80, and 443), service versions, and system finger- | incorporating MemAgent’s ability to selectively retain relevant |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| prints, are synthesized into a compact directive for the scanning | data while discarding distractors, the | Action Executor | enhances |  |  |  |  |  |  |  |  |  |  |  |  |  |
| phase, enabling targeted vulnerability detection with tools like | the system’s e | ffi | ciency and scalability, enabling robust pentest |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Nikto | or | sqlmap | . Similarly, scanning outputs, such as a SQL in- | in resource-constrained environments and contributing to xOf- |  |  |  |  |  |  |  |  |  |  |  |  |
| jection vulnerability identified by | sqlmap | or a misconfiguration | fense’s capability to handle complex, long-context workflows |  |  |  |  |  |  |  |  |  |  |  |  |  |
| count gained via SSH, and system context, such as operating | To thoroughly assess the e | ff | ectiveness and practicality of |  |  |  |  |  |  |  |  |  |  |  |  |  |
| system type. This log ensures continuity across phases, mitigat- | xO | ff | ense | , we designed a comprehensive experimental setup that |  |  |  |  |  |  |  |  |  |  |  |  |
| ing the risk of context loss and enabling dynamic integration of | evaluates not only task completion rates but also the scalability, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| findings. By filtering outputs from preceding phases to focus on | adaptability, and e | ffi | ciency of the system under realistic pentest |  |  |  |  |  |  |  |  |  |  |  |  |  |
| critical insights, the mechanism minimizes computational over- | conditions. This section details the experimental settings, mod- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| head, ensuring e | ffi | cient operation on a 32B-parameter LLM. | els, fine-tuning method, benchmark datasets, evaluation metrics |  |  |  |  |  |  |  |  |  |  |  |  |  |
| This streamlined communication fosters a cohesive testing pro- | and presents an in-depth analysis of the empirical results. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 10

| running Kali Linux 2025 [41]. Kali is chosen for its compre- | LLM outputs. Reported results are averaged across runs, and |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| hensive pentest toolkit and compatibility with industry-standard | we additionally report standard deviations where applicable. |  |  |  |  |  |  |
| workflows. | This virtualized attacker host is provisioned with | The evaluation follows a goal-oriented setting, where an |  |  |  |  |  |
| 8 vCPUs, 16 GB RAM, and 120 GB storage, ensuring stable | episode is considered successful if the agent achieves the pre- |  |  |  |  |  |  |
| execution of both o | ff | ensive tools and the | xO | ff | ense | multi-agent | defined exploitation objective within the allowed budget. Inter- |
| framework within a single environment. | mediate actions, such as reconnaissance and vulnerability iden- |  |  |  |  |  |  |

5.1.2. Victim Environment

• AUTOPENBENCH [10]: Tasks are instantiated as

Docker containers, which are hosted on a separate virtual

machine to avoid resource contention with the attacker

host. This victim VM is configured with 4 vCPUs, 8 GB

RAM, and 80 GB storage, and placed in the same NAT

network as the attacker machine to ensure direct connec-

tivity.

xO ff ense utilizes a core toolchain with specific versions de-

| Nikto | 2.5.0 |
| --- | --- |
| Dirb | 2.22 |

Each experimental scenario is repeated for 5 independent

runs with di ff erent random seeds to account for stochasticity in

10

tification, are not independently scored but contribute to overall

task completion.

tuning is performed during evaluation. Furthermore, we en-

sure that training data used for fine-tuning does not overlap with

evaluation benchmarks to mitigate data leakage. This protocol

is consistently applied to both the proposed framework and all

baselines to ensure comparability and reliability of the reported

results.

5.2. LLM models

tion ensured that LLM inference did not compete with pentest

DeepSeek-V3. For the mid-scale category, Qwen3-32B-base

ized penetration testing tasks.

sary for exploring complex attack paths. Furthermore, the top-

k parameter is set to 40, allowing for a diverse yet controlled

observed performance results.

| Two types of target environments are deployed correspond- | To prevent potential bias, all models are evaluated on the |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ing to the benchmark datasets: | same subset of benchmark environments, and no task-specific |  |  |  |  |  |  |  |
| • | AI-Pentest-Benchmark | [11]: Vulnerable machines are | The | fine-tuned | model, | namely | Qwen3-32B-finetune | is |
| directly imported from o | ffi | cial VulnHub distributions and | hosted on a dedicated compute node equipped with an NVIDIA |  |  |  |  |  |
| executed as VMware virtual machines without modifica- | A100 GPU having 80 GB VRAM. The same hardware is also |  |  |  |  |  |  |  |
| tion to their default specifications, in order to preserve | used during the fine-tuning process to accelerate training e | ffi | - |  |  |  |  |  |
| the original exploitation conditions. All machines are as- | ciency. | For inference, the model is exposed via an API end- |  |  |  |  |  |  |
| signed to the same NAT network as the attacker host to | point tunneled through | ngrok | , allowing the attacker machine |  |  |  |  |  |
| guarantee consistent communication. | to interact with the model as an external service. This separa- |  |  |  |  |  |  |  |
| 5.1.3. Evaluation Protocol | tasks for system resources, while also replicating realistic de- |  |  |  |  |  |  |  |
| Within the unified environment described in Section 5.1.1, | ployment conditions where models are often served remotely. |  |  |  |  |  |  |  |
| tailed in Table 2. These industry-standard utilities maintain sta- | 5.2.1. Evaluated Baseline Models |  |  |  |  |  |  |  |
| ble command-line interfaces (CLI) and operational syntaxes, | The experimental evaluation utilizes a broad spectrum of |  |  |  |  |  |  |  |
| ensuring that the agent’s reasoning logic remains functionally | large language models to establish a rigorous comparative base- |  |  |  |  |  |  |  |
| compatible with prior benchmark studies despite minor version | line. | This selection encompasses leading proprietary mod- |  |  |  |  |  |  |
| iterations. | els such as GPT-4o, alongside high-performance open-source |  |  |  |  |  |  |  |
| Table 2: Operational toolchain and versions (Kali Linux 2025) | architectures including Llama3.3-70B, Llama3.1-405B, and |  |  |  |  |  |  |  |
| Tool | Version | serves as the foundational open-source representative, which is |  |  |  |  |  |  |
| Nmap | 7.95 | subsequently optimized into Qwen3-32B-finetune for special- |  |  |  |  |  |  |
| WPScan | 3.8.28 | Empirical consistency is maintained by enforcing a stan- |  |  |  |  |  |  |
| sqlmap | 1.9.2#stable | dardized decoding strategy across all tested models. The infer- |  |  |  |  |  |  |
| Metasploit Framework | 6.4.50 | ence process is configured with a temperature of 0.5 and a top-p |  |  |  |  |  |  |
| Hydra | 9.5 | value of 0.9. This specific combination strikes a deliberate bal- |  |  |  |  |  |  |
| Enum4linux | 0.9.1 | ance between the deterministic accuracy required for security |  |  |  |  |  |  |
| Gobuster | 3.8.2 | tool command synthesis and the generative flexibility neces- |  |  |  |  |  |  |
| The evaluation itself follows a standardized protocol de- | vocabulary selection that prevents the model from generating |  |  |  |  |  |  |  |
| signed to guarantee fair and reproducible comparisons across | highly improbable tokens. Each model interaction is allocated |  |  |  |  |  |  |  |
| all evaluated methods. Each agent is executed under identical | a maximum budget of 4096 tokens. This extended context win- |  |  |  |  |  |  |  |
| constraints, including a maximum interaction budget of 5 steps | dow is essential for processing verbose security logs and gen- |  |  |  |  |  |  |  |
| per task, a timeout of 60 minutes per run, and a fixed token bud- | erating comprehensive multi-stage exploit scripts without the |  |  |  |  |  |  |  |
| get per model invocation. All methods are restricted to the same | risk of mid-sentence truncation. This universal hyperparameter |  |  |  |  |  |  |  |
| set of tools and environment configurations, without access to | setup isolates the architectural design and multi-agent orches- |  |  |  |  |  |  |  |
| external resources beyond those explicitly defined. | tration of each framework as the primary variables driving the |  |  |  |  |  |  |  |

---

## Page 11

| 5.2.2. Fine-Tuning Methodology | 5.2.3. Prompt Setting |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unlike conventional large-scale model adaptations, which | To ensure methodological transparency and reproducibility, |  |  |  |  |  |  |  |  |
| demand significant computational overhead, | xO | ff | ense | leverages | xO | ff | ense | adopts a | single system-wide initialization prompt |
| LoRA to achieve domain specialization. | LoRA reduces the | ( | init prompt | ) that governs the full penetration workflow, rather |  |  |  |  |  |
| parameter footprint by freezing the base model’s weights and | than using distinct prompt policies for individual agents. This |  |  |  |  |  |  |  |  |
| training only a compact set of adapter matrices. This approach | unified prompt defines the global objective, operational bound- |  |  |  |  |  |  |  |  |
| dramatically lowers the number of trainable parameters by over | aries, execution environment assumptions, output contracts, |  |  |  |  |  |  |  |  |
| 99%, enabling e | ffi | cient fine-tuning even on standard GPU in- | and cross-phase memory usage, thereby enforcing consistent |  |  |  |  |  |  |
| frastructures. | reasoning behavior throughout reconnaissance, scanning, and |  |  |  |  |  |  |  |  |
| To further address the memory bottlenecks of handling a | exploitation. |  |  |  |  |  |  |  |  |
| 32B-parameter model, we employ DeepSpeed ZeRO-3 [42] op- | Concretely, the init prompt specifies four mandatory con- |  |  |  |  |  |  |  |  |
| timization. | ZeRO-3 partitions model states, which includes | trol dimensions: (i) | mission context | (target objective and scope |  |  |  |  |  |
| optimizer, gradients, and parameters across multiple GPUs, | constraints), (ii) | state continuity | (reuse of prior successful ac- |  |  |  |  |  |  |
| achieving linear scalability. | Additionally, FlashAttention v2 | tions and shell status), (iii) | actionability requirements | (tool- |  |  |  |  |  |
| [43] is integrated to optimize attention computation, reducing | compatible and directly executable commands), and (iv) | struc- |  |  |  |  |  |  |  |
| memory usage and accelerating training by up to 3x compared | tured output formatting | . The unified design reduces prompt- |  |  |  |  |  |  |  |
| to standard attention implementations. These combined tech- | policy drift across phases and improves execution stability |  |  |  |  |  |  |  |  |
| niques allow us to e | ffi | ciently fine-tune Qwen3-32B for pentest | when the planner performs iterative update and reflection. |  |  |  |  |  |  |
| workloads with a significant reduction in hardware demands. | To reduce parsing ambiguity, the init prompt enforces strict |  |  |  |  |  |  |  |  |
| And the fine-tuning dataset comprised two main corpora as fol- | output contracts: | planning outputs must be serialized within |  |  |  |  |  |  |  |
| lows: | <json></json> | tags, while executable commands must be en- |  |  |  |  |  |  |  |

tags, enabling the model to learn structured, step-by-step

systematically processed to extract task-specific reason-

• WhiteRabbitNeo : A high-quality JSONL-formatted

is standardized during preprocessing by appending empty

<think> tags to each sample. This structural unifica-

tion ensures compatibility with CoT-augmented training

pipelines and facilitates subsequent fine-tuning for step-

by-step reasoning abilities. The dataset draws from real-

world o ff ensive and defensive cybersecurity scenarios,

encompassing exploitation techniques, payload crafting,

and red-team / blue-team interactions, sourced from the

WhiteRabbitNeo community contributions [48].

11

closed in <execute></execute> tags. This explicit interface

over multi-step attack trajectories.

with raw terminal traces.

external behavior.

< json >

[

{

" id ": "1" ,

" dependent_task_ids ": [] ,

" instruction ": " Enumerate open

services on 10.10.10.5 with

version detection ." ,

" action ": " Shell "

} ,

| • | PentestData | : This dataset is meticulously curated to en- | is essential because downstream modules parse model outputs |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| compass domain-specific question-answer pairs, each en- | programmatically. | In addition, long execution logs are sum- |  |  |  |  |  |  |  |  |  |  |
| riched with synthetically generated CoT reasoning traces. | marized before being re-injected into context, which mitigates |  |  |  |  |  |  |  |  |  |  |  |
| The reasoning steps are encapsulated within | <think> | context dilution and helps maintain coherent decision-making |  |  |  |  |  |  |  |  |  |  |
| logical deduction processes tailored for pentest scenarios. | The prompt follows a grey-box principle: it does not expose |  |  |  |  |  |  |  |  |  |  |  |
| To construct PentestData, we aggregate and standardize | implementation internals, but injects selective operational state, |  |  |  |  |  |  |  |  |  |  |  |
| write-ups from over | 1,000 machines | across leading cy- | including prior successful or failed tasks, shell continuity indi- |  |  |  |  |  |  |  |  |  |
| bersecurity platforms, including TryHackMe [44], Hack- | cators, and compressed history summaries. This strategy pre- |  |  |  |  |  |  |  |  |  |  |  |
| TheBox [45], and VulnHub [46]. | These write-ups are | serves cross-step coherence without overwhelming the model |  |  |  |  |  |  |  |  |  |  |
| ing paths, exploit procedures, and decision-making se- | For all experiments, prompt execution used a unified in- |  |  |  |  |  |  |  |  |  |  |  |
| quences relevant to o | ff | ensive security operations. In addi- | ference policy to isolate the e | ff | ect of architecture and prompt- |  |  |  |  |  |  |  |
| tion, we incorporate supplementary pentest datasets from | ing from decoding variance. Specifically, we use temperature |  |  |  |  |  |  |  |  |  |  |  |
| HuggingFace Datasets Hub [47], focusing on cybersecu- | = | 0 | . | 5, top- | p | = | 0 | . | 9, top- | k | = | 40, and a maximum generation bud- |
| rity knowledge bases, pentest techniques, and practical | get of 4096 tokens per interaction, consistent across compared |  |  |  |  |  |  |  |  |  |  |  |
| guides for commonly used security tools. This compre- | models. | In the deployed | xO | ff | ense | implementation, hidden |  |  |  |  |  |  |
| hensive integration ensures that PentestData serves as a | chain-of-thought traces (when produced inside | <think> | tags) |  |  |  |  |  |  |  |  |  |
| robust and diverse resource for training models in au- | are removed before downstream processing, ensuring evalua- |  |  |  |  |  |  |  |  |  |  |  |
| tonomous pentest workflows. | tion is based only on actionable outputs while retaining stable |  |  |  |  |  |  |  |  |  |  |  |
| dataset comprising instruction-response pairs, specifi- | For | reproducibility, | a | representative | structured | output |  |  |  |  |  |  |
| cally curated for cybersecurity tasks. Although the orig- | schema governed by the init prompt is shown below: |  |  |  |  |  |  |  |  |  |  |  |
| inal dataset lacked explicit CoT reasoning annotations, it | Listing 1: Representative structured planning output used in xO | ff | ense prompts. |  |  |  |  |  |  |  |  |  |

---

## Page 12

| { | flaws (SQL injection, | XSS, CSRF | / | SSRF), network service |
| --- | --- | --- | --- | --- |
| " id ": | "2" , | weaknesses (FTP | / | AD enumeration, brute-force authentication), |
| " dependent_task_ids ": | ["1"] , | code-level issues (deserialization, | command injection), | and |
| " instruction ": | " Assess | HTTP | post-exploitation techniques (cronjob analysis, misconfigured |  |
| service | on | 10.10.10.5:80 | for | system files, privilege escalation via user access exploitation). |
| common | web | vulnerabilities | Notably, many of these tasks map directly to recurring weak- |  |
| ." , | ness categories in the CWE Top 25 and OWASP Top 10, ensur- |  |  |  |
| " action ": | " Web " | ing that success on this benchmark corresponds to capabilities |  |  |
| } | relevant in practical o | ff | ensive security operations. The bench- |  |
| ] | mark is particularly challenging because the ultimate goal is to |  |  |  |
| </ json > | achieve root access on each machine, requiring coherent rea- |  |  |  |

5.3. Benchmark Datasets

thetic vulnerabilities and realistic multi-stage exploitation sce-

narios. Together, these benchmarks provide a balanced testbed

for assessing the adaptability and robustness of automated pen-

test systems.

real-world CVEs. The in-vitro set (22 tasks) reflects funda-

files), web application flaws (such as path traversal, SQL in-

jection, file upload RCE), and insecure network configurations

(such as SNMP misconfiguration, ARP spoofing). In addi-

tion, four cryptography tasks evaluate resilience against im-

include critical vulnerabilities widely recognized for their im-

vulnerabilities that have historically dominated real-world at-

AI-Pentest-Benchmark.. While AutoPenBench focuses on con-

flows across 13 real-world vulnerable machines drawn from

and general technique subtasks, amounting to 152 tasks in

12

soning across reconnaissance, exploitation, and privilege es-

calation stages. Previous studies have shown that even large-

scale proprietary models such as GPT-4o and Llama3.1-405B

mark.

5.4. Evaluation Metrics

To evaluate the performance of xO ff ense , we employ three

interaction budget. Formally:

# compromised machines

Overall Rate =

# total machines

Subtask-1Exp =

| S |

successes:

Subtask-5Exp =

5 × | S |

| To ensure a rigorous and practically relevant evaluation, we | are unable to achieve root-level compromise without human as- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| selected two complementary benchmarks that cover both syn- | sistance, underscoring the di | ffi | culty and realism of this bench- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| AutoPenBench. | This benchmark defines a total of 33 pen- | complementary metrics that capture both high-level task suc- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| test tasks, spanning both instructional “in-vitro” exercises and | cess and fine-grained sub-task robustness. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| mental vulnerability classes frequently highlighted in industry | 5.4.1. Overall Task Completion Rate |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| rankings such as the OWASP Top 10, including weak access | This metric measures the percentage of target machines suc- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| control (such as misconfigured sudo, world-writable shadow | cessfully compromised like the obtained flag within the allowed |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| proper or weak cryptographic implementations, such as brute- | This provides a coarse-grained view of whether an agent can |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| forcing Di | ffi | e–Hellman keys. Beyond these educational tasks, | achieve end-to-end exploitation across categories such as Ac- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the benchmark incorporates 11 real-world CVEs ranging from | cess Control (AC), Web Security (WS), Network Security (NS), |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2014 to 2024 with CVSS scores between 7.5 and 10.0. These | Cryptography (CRPT), and Real-world tasks. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| pact and prevalence, such as Log4Shell (CVE-2021-44228), | 5.4.2. Sub-task Completion Rate (1 Experiment) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Heartbleed (CVE-2014-0160), SambaCry (CVE-2017-7494), | To gain insight into intermediate stages of pentest, we eval- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and Spring4Shell (CVE-2022-22965). By combining founda- | uate sub-task success rates, including service enumeration and |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tional categories with critical CVEs, AutoPenBench provides a | vulnerability detection. Each benchmark defines a set of sub- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| structured yet realistic environment to evaluate whether agents | tasks | S | . A sub-task is considered successful if it is completed |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| can transition from basic exploitation to handling high-severity | in at least one of the five independent runs: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tack campaigns. | \|{ | s | ∈ | S | \| ∃ | i | ∈ | [1 | , | 5] | , | success( | s | , | i | ) | }\| |
| tainerized vulnerabilities, | the AI-Pentest-Benchmark evalu- | This metric highlights the agent’s ability to eventually solve a |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ates AI agents on complete end-to-end exploitation work- | sub-task, even if not consistently across all runs. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| VulnHub. | These machines are categorized by di | ffi | culty into | 5.4.3. Sub-task Completion Rate (5 Experiments) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| easy (such as Victim1, Library2, Funbox, WestWild), medium | To measure robustness and consistency, we also compute |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (such as Cengbox2, Devguru, Symfonos2), and hard (such | the cumulative completion rate across all five runs. In this case, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| as Insanity, TempusFugit). | Each machine defines a struc- | we count the total number of successful sub-tasks over all ex- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tured set of reconnaissance, exploitation, privilege escalation, | periments and normalize by the maximum possible number of |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| total. | The vulnerabilities embedded within these machines | P | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| reflect common pentest scenarios, including web application | i | = | 1 | successes( | i | ) |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 13

| This stricter metric rewards agents that not only succeed once | These findings demonstrate that fine-tuning on domain- |  |  |
| --- | --- | --- | --- |
| but can repeatedly complete subtasks across independent exe- | relevant CoT data and incorporating robust task orchestration |  |  |
| cutions. | mechanisms can enable a quantized, resource-e | ffi | cient model |
| Together, these three metrics provide a balanced view: (i) | to match and even surpass the capabilities of larger, general- |  |  |
| overall penetration capability, (ii) eventual solvability of sub- | purpose LLMs in specialized scenarios. The consistent outper- |  |  |
| tasks, and (iii) robustness of performance under repeated trials. | formance across categories further validates the robustness of |  |  |

6. Evaluation and results

We design five experimental scenarios to comprehensively

evaluate xO ff ense across synthetic and real-world settings:

• Scenario 3: Sub-task completion on AutoPenBench (5

Experiments), aggregating successful subtasks across all

five runs to capture consistency.

Benchmark without RAG, using six representative

all evaluated models on the AutoPenBench dataset. The

fine-tuned Qwen3-32B-finetune model achieved a remarkable

world category, Qwen3-32B-finetune attained a 54.54% suc-

13

our fine-tuning strategy, especially given the compute-e ffi cient

AWQ quantization.

To assess finer-grained capabilities, we evaluated sub-task

completion in a single-run experiment (Table 4). The term

”1 Experiment” refers to the overall sub-task completion rate

performing Llama3.1-405B (Paper) (69.05%) by a margin of

In the Real-world category, Qwen3-32B-finetune achieved

a 35.96% sub-task completion rate, more than doubling that

of Qwen3-32B-base (24.92%) and outperforming Llama3.1-

405B (Paper) (26.19%). Similarly, in the CRPT category,

Llama3.1-405B (Paper).

results (52.36%), its performance gap to Qwen3-32B-finetune

herence, particularly in chained exploit scenarios. The fine-

task sequences.

for Qwen3-32B-base.

| 6.1. Experiment Scenarios | 6.2.2. Sub-task Completion Performance (1 Experiment) |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| • | Scenario 1: | Overall task completion on AutoPenBench, | across five experiments, where a sub-task is considered suc- |  |  |  |  |  |  |  |
| measuring full machine compromise across AC, WS, NS, | cessful if it succeeds in at least one experiment. | Qwen3-32B- |  |  |  |  |  |  |  |  |
| and CRPT categories. | finetune | achieved a | 79.17% | sub-task completion rate, out- |  |  |  |  |  |  |
| • | Scenario 2: | Sub-task completion on AutoPenBench (1 | 10.12% | . This margin is significant, particularly when consid- |  |  |  |  |  |  |
| Experiment), where a sub-task is successful if solved in | ering that Llama3.1-405B is a much larger model (405B param- |  |  |  |  |  |  |  |  |  |
| at least one of five runs. | eters) operating in its native configuration. |  |  |  |  |  |  |  |  |  |
| • | Scenario 4: | Real-world exploitation on AI-Pentest- | the fine-tuned model demonstrated a | 3.41% | improvement over |  |  |  |  |  |
| VulnHub machines. | Interestingly, while Qwen3-32B-base achieved moderate |  |  |  |  |  |  |  |  |  |
| • | Scenario 5: | Real-world exploitation on AI-Pentest- | (79.17%) illustrates the critical role of domain adaptation. |  |  |  |  |  |  |  |
| Benchmark with RAG, highlighting the contribution of | The base model, though capable of handling general security |  |  |  |  |  |  |  |  |  |
| retrieval to complex exploitation chains. | tasks, struggled with multi-step reasoning and contextual co- |  |  |  |  |  |  |  |  |  |
| 6.2. Task Completion Performance Across pentest Categories | tuned model’s superior performance confirms that its CoT- |  |  |  |  |  |  |  |  |  |
| 6.2.1. Overall Task Completion Performance | driven prompt alignment and RAG-assisted knowledge retrieval |  |  |  |  |  |  |  |  |  |
| Table 3 presents the overall task completion rates across | mechanisms provide a tangible advantage in executing complex |  |  |  |  |  |  |  |  |  |
| 72.72% | completion rate, substantially outperforming both its | 6.2.3. Sub-task Completion Performance (5 Experiments) |  |  |  |  |  |  |  |  |
| base variant, | Qwen3-32B-base | (30.30%), and other state-of- | To evaluate robustness and stability, we conducted aggre- |  |  |  |  |  |  |  |
| the-art models, including GPT-4o (21.21%), Llama3.1-405B | gated experiments over five runs (Table 5). | The term ”5 Ex- |  |  |  |  |  |  |  |  |
| (Paper) (30.30%), and PentestGPT (9.09%). | periments” denotes the number of subtasks completed in all |  |  |  |  |  |  |  |  |  |
| The performance disparity between | Qwen3-32B-finetune | five experiments. | Qwen3-32B-finetune | maintained its lead |  |  |  |  |  |  |
| and its base version is particularly noteworthy. Despite having | with a | 60.94% | sub-task completion rate, significantly outper- |  |  |  |  |  |  |  |
| identical model architecture and parameter size (32 billion pa- | forming Llama3.1-405B (Paper) (49.90%) and Qwen3-32B- |  |  |  |  |  |  |  |  |  |
| rameters), the domain-specific fine-tuning enabled a | 2.4x im- | base (23.03%). This robustness is critical in practical pentest- |  |  |  |  |  |  |  |  |
| provement | in task completion. | This validates the e | ff | ective- | ing workflows, where variance due to environmental noise and |  |  |  |  |  |
| ness of our lightweight LoRA fine-tuning pipeline in adapting | complex task dependencies often degrades model performance. |  |  |  |  |  |  |  |  |  |
| general-purpose models to specialized pentest workflows. | In the | AC | category, | Qwen3-32B-finetune | achieved a re- |  |  |  |  |  |
| In the | AC | category, | Qwen3-32B-finetune | achieved a | 100% | markable | 14.51% | , which is | 4.32% higher | than Llama3.1- |
| success rate | , a stark contrast to the 40.00% of Qwen3-32B- | 405B (Paper). | For | WS | , our model reached | 10.91% | , outper- |  |  |  |
| base and the 60.00% of Llama3.1-405B (Paper). | Similarly, | forming all baselines by a significant margin. | Notably, even |  |  |  |  |  |  |  |
| in | NS | , our model achieved | 83.33% | completion, surpassing | in categories where task chains are inherently volatile, such |  |  |  |  |  |
| all baselines, including Llama3.3-70B (33.33%) and Qwen3- | as | Real-world | , the fine-tuned model achieved | 21.07% | , com- |  |  |  |  |  |
| 32B-base (50.00%). | Notably, | even in the complex | Real- | pared to 17.71% for Llama3.1-405B (Paper) and only 9.78% |  |  |  |  |  |  |
| cess rate, outperforming Qwen3-32B-base (27.27%) and Pen- | While a performance drop of approximately | 18% | from the |  |  |  |  |  |  |  |
| testGPT (0.00%). | single-experiment run to the aggregated runs was observed, this |  |  |  |  |  |  |  |  |  |

---

## Page 14

Table 3: Overall Task Completion Rate on Target Machines. Our fine-tuned model demonstrates superior performance, especially in AC, NS, and Real-world

categories.

| Llama3.3-70B | Llama3.1-405B | Llama3.1-405B | Qwen3-32B | Qwen3-32B-finetune |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Category | GPT-4o |  |  |  |  |  |
| (VulnBot) | (VulnBot) | (PentestGPT) | (Base) | (Ours) |  |  |
| AC | 1 (20.00%) | 1 (20.00%) | 3 (60.00%) | 1 (20.00%) | 2 (40.00%) | 5 (100.00%) |
| WS | 2 (28.57%) | 1 (14.29%) | 2 (28.57%) | 0 (0.00%) | 2 (28.57%) | 5 (71.42%) |
| NS | 3 (50.00%) | 2 (33.33%) | 2 (33.33%) | 2 (33.33%) | 3 (50.00%) | 5 (83.33%) |
| CRPT | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) | 3 (75.00%) |
| Real-world | 1 (9.09%) | 2 (18.18%) | 3 (27.27%) | 0 (0.00%) | 3 (27.27%) | 6 (54.54%) |
| ALL | 7 (21.21%) | 6 (18.18%) | 10 (30.30%) | 3 (9.09%) | 10 (30.30%) | 24 (72.72%) |

Table 4: Sub-task Completion Rate (1 Experiment) . Qwen3-32B-finetune shows the highest completion rate across all categories.

Llama3.3-70B Llama3.1-405B Llama3.3-70B Llama3.1-405B Llama3.1-405B Qwen3-32B Qwen3-32B-finetune

Category

| (VulnBot) | (VulnBot) | (Base) | (Base) | (PentestGPT) | (Base) | (Ours) |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AC | 25 (11.90%) | 31 (14.76%) | 16 (7.62%) | 21 (10.00%) | 20 (9.52%) | 26 (8.20%) | 46 (14.51%) |
| WS | 24 (11.43%) | 30 (14.29%) | 22 (10.48%) | 26 (12.38%) | 18 (8.57%) | 28 (8.83%) | 38 (11.98%) |
| NS | 12 (5.71%) | 11 (5.24%) | 10 (4.76%) | 9 (4.29%) | 6 (2.86%) | 11 (3.47%) | 15 (4.73%) |
| CRPT | 15 (7.14%) | 18 (8.57%) | 17 (8.10%) | 18 (8.57%) | 12 (5.71%) | 22 (6.94%) | 38 (11.98%) |
| Real-world | 49 (23.33%) | 55 (26.19%) | 29 (13.81%) | 29 (13.81%) | 28 (13.33%) | 79 (24.92%) | 114 (35.96%) |
| ALL | 125 (59.52%) | 145 (69.05%) | 94 (44.76%) | 103 (49.05%) | 84 (40.00%) | 166 (52.36%) | 251 (79.17%) |

Table 5: Sub-task Completion Rate (5 Experiments) . Our model maintains a significant lead, demonstrating robustness and consistency.

Llama3.3-70B Llama3.1-405B Llama3.3-70B Llama3.1-405B Llama3.1-405B Qwen3-32B Qwen3-32B-finetune

Category

| (VulnBot) | (VulnBot) | (Base) | (Base) | (PentestGPT) | (Base) | (Ours) |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AC | 87 (8.29%) | 107 (10.19%) | 46 (4.38%) | 61 (5.81%) | 27 (2.57%) | 60 (3.78%) | 212 (14.51%) |
| WS | 106 (10.10%) | 116 (11.05%) | 83 (7.90%) | 66 (6.29%) | 40 (3.81%) | 70 (4.42%) | 173 (10.91%) |
| NS | 41 (3.90%) | 40 (3.81%) | 36 (3.43%) | 22 (2.10%) | 15 (1.43%) | 10 (0.63%) | 71 (4.67%) |
| CRPT | 65 (6.19%) | 75 (7.14%) | 68 (6.48%) | 44 (4.19%) | 43 (4.10%) | 70 (4.42%) | 176 (11.10%) |
| Real-world | 166 (15.81%) | 186 (17.71%) | 99 (9.43%) | 67 (6.38%) | 56 (5.33%) | 155 (9.78%) | 334 (21.07%) |
| ALL | 465 (44.29%) | 524 (49.90%) | 332 (31.62%) | 260 (24.76%) | 181 (17.24%) | 365 (23.03%) | 966 (60.94%) |
| is expected due to increased task complexity and stochastic fail- | 6.3. Evaluation on Complex Real-World Exploitation Chains |  |  |  |  |  |  |
| ures inherent in autonomous pentesting. Nevertheless, the fine- | 6.3.1. Performance without RAG (No-RAG) |  |  |  |  |  |  |
| tuned model’s consistency across these iterations underscores | To assess the baseline capabilities of our proposed system |  |  |  |  |  |  |
| its robustness, particularly when contrasted with PentestGPT’s | xO | ff | ense | in realistic o | ff | ensive security scenarios, we conducted |  |
| 17.24% sub-task completion in the same setting. | experiments on the same set of six real-world vulnerable ma- |  |  |  |  |  |  |

chines as utilized in the VulnBot [9] evaluation: Victim1 , Li-

| 6.2.4. Comparative Insights | brary2 | , | Sar | , | WestWild | , | Symfonos2 | , and | Funbox | . This ma- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A critical observation from these experiments is the dispro- | chine set, originally derived from the AI-Pentest-Benchmark, |  |  |  |  |  |  |  |  |  |
| portionate performance leap achieved through fine-tuning rel- | covers a diverse range of exploitation challenges, including |  |  |  |  |  |  |  |  |  |
| ative to model size. | Despite being a 32B parameter model, | misconfigurations, weak authentication, remote code execution, |  |  |  |  |  |  |  |  |
| Qwen3-32B-finetune | consistently outperformed larger coun- | privilege escalation, and multi-step attack chains. By adopting |  |  |  |  |  |  |  |  |
| terparts like Llama3.1-405B (405B parameters) across every | this identical set, we ensure methodological consistency and en- |  |  |  |  |  |  |  |  |  |
| evaluation metric. | This validates our hypothesis that task or- | able a direct, fair comparison with prior work. |  |  |  |  |  |  |  |  |
| chestration, RAG-driven context augmentation, and parameter- | The experiments were conducted in a fully autonomous |  |  |  |  |  |  |  |  |  |
| e | ffi | cient tuning techniques (LoRA | + | ZeRO-3 | + | FlashAttention) | mode, without any human intervention or RAG support. Each |  |  |  |
| can bridge, and in specialized scenarios, exceed the perfor- | target machine was tested in five independent runs, and the |  |  |  |  |  |  |  |  |  |
| mance gap traditionally associated with sheer model size. | reported performance represents the best sub-task completion |  |  |  |  |  |  |  |  |  |
| Furthermore, the disparity between Qwen3-32B-base and | rate per machine, following the AI-Pentest-Benchmark scor- |  |  |  |  |  |  |  |  |  |
| Qwen3-32B-finetune | exemplifies | the | inadequacy | of | using | ing methodology. | Figure 3 presents the comparative results |  |  |  |
| general-purpose LLMs in specialized pentesting workflows | across multiple models, including | VulnBot-Llama3.1-405B | , |  |  |  |  |  |  |  |
| without domain adaptation. | The base model, though archi- | VulnBot-DeepSeek-v3 | , their respective base models, and our |  |  |  |  |  |  |  |
| tecturally identical, lacked the reasoning depth and context- | proposed | Qwen3-32B | variants (base and finetuned). |  |  |  |  |  |  |  |
| coherence required for intricate attack path planning, resulting | The results reveal several noteworthy patterns. | First, |  |  |  |  |  |  |  |  |
| in lower task and sub-task completion rates. | Qwen3-32B-finetune | consistently surpasses its base counter- |  |  |  |  |  |  |  |  |

part across all six machines, with particularly significant im-

14

---

## Page 15

| provements on | Victim1 | ( | + | 0.55), | Library2 | ( | + | 0.30), and | West- | of hallucination-driven dead ends, which are particularly detri- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wild | ( | + | 0.63). | These gains highlight the e | ff | ectiveness of | mental in constrained exploitation environments. Collectively, |  |  |  |
| domain-specific fine-tuning in strengthening the model’s ex- | these findings reinforce the notion that RAG is a critical en- |  |  |  |  |  |  |  |  |  |
| ploitation reasoning and procedural robustness. Second, while | abler for scalable, high-fidelity automated pentest in complex |  |  |  |  |  |  |  |  |  |
| VulnBot-DeepSeek-v3 remains highly competitive, achieving | real-world settings. |  |  |  |  |  |  |  |  |  |

the highest score on Victim1 (0.83) and WestWild (0.71), our

fine-tuned Qwen3-32B achieves comparable or superior perfor-

mance on most other machines, including leading results on Sar

(0.58) and Funbox (0.54).

Notably, performance disparities are strongly correlated

with the complexity of exploitation chains. Targets such as

Symfonos2 and Funbox , which demand multi-stage privilege

escalation and exploitation of non-trivial service configurations,

clearly benefit from the enhanced contextual reasoning intro-

duced via fine-tuning. This observation underscores the criti-

cal role of model specialization in addressing the inherent un-

predictability and diversity of real-world pentest environments.

In summary, the No-RAG evaluation confirms that xO ff ense-

Qwen3-32B-finetune can autonomously achieve competitive,

and in some cases state-of-the-art, performance in realistic of-

fensive security scenarios, even without external retrieval aug-

mentation. This establishes a robust performance baseline for

subsequent RAG-enhanced evaluations.

6.3.2. Performance with RAG (RAG)

When augmenting the evaluation with the Knowledge

Repository module, a substantial shift in performance trends

emerges across the six real-world exploitation targets (see

Fig. 4) . Compared to the baseline (No-RAG), the Qwen3-32B-

Finetune model demonstrates marked improvement, achieving

perfect completion scores on Victim1 and WestWild (1.00) and

notable gains on Library2 ( + 0.20) and Symfonos2 ( + 0.16).

Similarly, moderate increases are observed for Sar and Funbox,

reflecting the model’s enhanced capability to navigate multi-

step attack chains when supported by targeted, contextually rel-

evant prior knowledge.

on Library2 (0.80) and surpassing it on Victim1 and WestWild.

This suggests that RAG integration not only mitigates the limi-

15

7. Threats to Validity

7.1. Internal validity

The fine-tuning of Qwen3-32B on a CoT-enriched pentest

dataset introduces potential internal threats. Certain vulnera-

bility classes and exploitation strategies are disproportionately

represented, which may bias the model toward specific attack

vectors while limiting its capacity to generalize to underrepre-

sented scenarios. Moreover, the integration of prompting strate-

gies and toolchains may embed implicit task-specific heuristics,

raising the possibility that reported improvements partly reflect

dataset artifacts rather than genuine reasoning ability. Such fac-

tors must be considered when interpreting performance gains

on structured benchmarks.

7.2. External validity

The evaluation settings of AutoPenBench and AI-Pentest-

Benchmark, which approximate realistic penetration work-

flows, yet cannot fully capture the heterogeneity of production-

scale environments. Operational networks often exhibit greater

variability in topology, non-standard configurations, active de-

fenses, and deception mechanisms that remain absent from cur-

rent benchmarks. In addition, adversarial tactics evolve over

time, whereas benchmarks are necessarily static. Consequently,

the generalizability of results to enterprise systems, heteroge-

neous infrastructures, or zero-day exploitation scenarios should

be regarded with caution.

7.3. Construct validity

7.4. Reliability

observe non-negligible variance.

| The gains are less pronounced for Qwen3-32B-Base, with | Task completion rate and exploitation success were em- |  |  |  |
| --- | --- | --- | --- | --- |
| performance remaining comparatively low on challenging tar- | ployed as primary evaluation metrics. While suitable for quanti- |  |  |  |
| gets such as Symfonos2 (0.13) and WestWild (0.25). | This | fying functional e | ff | ectiveness, these measures neglect other di- |
| disparity underscores the role of fine-tuning in maximizing | mensions that are central to pentest practice. Attributes such as |  |  |  |
| the benefits of retrieval augmentation, as without alignment | stealth, e | ffi | ciency of resource utilization, time-to-compromise, |  |
| to domain-specific exploitation strategies, the retrieved infor- | and resilience against detection are critical to operational re- |  |  |  |
| mation alone is insu | ffi | cient to ensure consistent execution suc- | alism yet remain unaccounted for in the adopted benchmarks. |  |
| cess. When compared against VulnBot baselines, Qwen3-32B- | Furthermore, binary success measures fail to capture partial |  |  |  |
| Finetune with RAG achieves competitive or superior results in | progress or incremental compromise, potentially obscuring nu- |  |  |  |
| four out of six targets, matching the best baseline performance | ances in agent behavior across complex exploitation chains. |  |  |  |
| tations of the base model but also allows the fine-tuned variant | The reproducibility of results may be a | ff | ected by stochas- |  |
| to close the gap, or in certain scenarios, outperform human- | tic factors inherent in both large language model inference and |  |  |  |
| assisted frameworks. | auxiliary system tools. Hardware variation, runtime conditions, |  |  |  |
| These improvements can be attributed to three key fac- | network latency, and nondeterministic outputs from scanning |  |  |  |
| tors: | (1) the retriever’s ability to surface high-relevance ex- | utilities can yield divergent agent behaviors even under identi- |  |  |
| ploitation procedures from a curated cybersecurity corpus, (2) | cal inputs. Standardized configurations and repeated trials mit- |  |  |  |
| the fine-tuned model’s capacity to integrate external informa- | igate these e | ff | ects but do not eliminate them entirely, implying |  |
| tion into coherent multi-step reasoning, and (3) the reduction | that replications across platforms or over extended periods may |  |  |  |

---

## Page 16

Figure 3: Comparison of sub-task completion rates across six real-world vulnerable machines in a No-RAG setting.

Figure 4: Comparison of sub-task completion rates across six real-world vulnerable machines with RAG setting.

In sum, although the reported findings provide strong ev- 8. Ethical Considerations and Responsible Use

idence of the capabilities of xO ff ense, these validity concerns

| underscore the need for broader empirical validation. Expand- | This work addresses autonomous penetration testing, a do- |  |  |
| --- | --- | --- | --- |
| ing evaluations to encompass more diverse infrastructures, ad- | main with inherent dual-use implications. While the proposed |  |  |
| versarially adaptive defenses, and richer performance metrics | xO | ff | ense framework is intended to support defensive cyberse- |
| would strengthen the robustness, scalability, and practical ap- | curity practices, it may also be subject to misuse if deployed |  |  |
| plicability of autonomous pentest systems. | without appropriate safeguards. The system is designed strictly |  |  |

for authorized security assessment, research, and training pur-

16

---

## Page 17

| poses in controlled environments, such as benchmark platforms | performs both larger commercial LLMs, such as GPT-4o and |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| and laboratory settings, and must only be used with explicit le- | LLaMA3-70B, and leading open-source baselines, | such as |  |  |  |  |  |  |  |
| gal authorization from system owners. | It is not intended for | PentestGPT | and | VulnBot-LLaMA3-405B. | The | framework |  |  |  |
| unauthorized exploitation of real-world systems. | attained an overall task completion rate of 72.72% and a |  |  |  |  |  |  |  |  |
| Due to its capability to automate multi-stage penetration | sub-task completion rate of up to 79.17%, while successfully |  |  |  |  |  |  |  |  |
| testing workflows, the framework may lower the barrier for | exploiting complex real-world targets. These results highlight |  |  |  |  |  |  |  |  |
| conducting o | ff | ensive operations, including large-scale vulner- | that | a | domain-specialized, | mid-scale | model, | when | paired |
| ability discovery and exploitation. This highlights the impor- | with targeted reasoning guidance, can match or exceed the |  |  |  |  |  |  |  |  |
| tance of responsible usage and user awareness when interacting | capabilities of state-of-the-art large-scale systems, | o | ff | ering |  |  |  |  |  |
| with such systems. Users are expected to adhere to applicable | a | cost-e | ff | ective | and | reproducible | solution | for | autonomous |
| legal frameworks, institutional policies, and professional eth- | o | ff | ensive security operations. |  |  |  |  |  |  |
| ical standards when deploying or extending the proposed ap- | Future work will explore three main directions. | First, |  |  |  |  |  |  |  |
| proach. | we aim to optimize the command generation module, poten- |  |  |  |  |  |  |  |  |
| To mitigate potential risks, all experiments in this study | tially through structured function calling, to further improve |  |  |  |  |  |  |  |  |
| are conducted strictly within sandboxed and publicly avail- | execution precision. | Second, we plan to enhance the ro- |  |  |  |  |  |  |  |
| able benchmark environments, including AutoPenBench and | bustness of long-running process handling and strengthen the |  |  |  |  |  |  |  |  |
| AI-Pentest-Benchmark, without interaction with live produc- | retrieval-augmented generation mechanism with automated up- |  |  |  |  |  |  |  |  |
| tion systems or undisclosed vulnerabilities. In practical deploy- | dates from vulnerability intelligence sources such as ExploitDB |  |  |  |  |  |  |  |  |
| ments, additional safeguards are necessary, including restricting | and GitIngest. Third, we intend to extend xO | ff | ense’s capabili- |  |  |  |  |  |  |
| execution to authorized and monitored environments, enforc- | ties to support advanced web and GUI interactions via browser |  |  |  |  |  |  |  |  |
| ing logging and auditing of system actions, limiting tool usage | automation, enabling it to tackle a broader range of pentest sce- |  |  |  |  |  |  |  |  |
| and external network access, and incorporating human-in-the- | narios. |  |  |  |  |  |  |  |  |

loop validation for high-impact decisions. Future implemen-

tations should further integrate policy-based constraints and ac-

cess control mechanisms to prevent unintended or malicious us-

motivates the development of more robust defensive mecha-

architectures. As such, this work contributes not only to o ff en-

ture extensions should follow coordinated disclosure principles

rity research.

tonomous multi-agent framework for pentest, designed to ad-

large proprietary models. By integrating a fine-tuned, mid-

scale open-source LLM (Qwen3-32B) with a novel grey-box

Benchmark demonstrated that xO ff ense consistently out-

17

References

nvd-revamps-operations-cve-surge/ , 2024. Accessed: 2025-07-

30.

Accessed: 2025-07-30.

[3] Isao Takaesu and Daisuke Chikamori. Deep exploit. https:

[4] Rapid7. Metasploit — penetration testing software, pen testing security.

learning. evaluation , 8:9, 2024.

[6] Khuong Tran, Ashlesha Akella, Maxwell Standen, Junae Kim, David

arXiv:2109.06449 , 2021.

[7] Gelei Deng, Yi Liu, V´ ıctor Mayoral-Vilches, Peng Liu, Yuekang Li, Yuan

Xu, Tianwei Zhang, Yang Liu, Martin Pinzger, and Stefan Rass. Pen-

penetration testing. In 33rd USENIX Security Symposium (USENIX Secu-

[8] Xiangmin Shen, Lingzhi Wang, Zhenyuan Li, Yan Chen, Wencheng

Zhao, Dawei Sun, Jiashui Wang, and Wei Ruan. Pentestagent: Incorpo-

pages 375–391, 2025.

[9] He Kong, Die Hu, Jingguo Ge, Liangxiong Li, Tong Li, and Bingzhen

Wu. VulnBot: Autonomous penetration testing for a multi-agent collabo-

ing generative agents for penetration testing, 2024.

| age. | [1] | Infosecurity | Magazine. | Nvd | revamps | operations | amid | cve |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Beyond its o | ff | ensive capabilities, this line of research also | surge. | https://www.infosecurity-magazine.com/news/ |  |  |  |  |
| nisms. Understanding how autonomous agents identify and ex- | [2] | GBHackers. | Nist | facing | challenges | in | manag- |  |
| ploit vulnerabilities can inform the design of improved intru- | ing | cve | backlog. | https://gbhackers.com/ |  |  |  |  |
| sion detection systems, adaptive defenses, and secure system | nist-facing-challenges-in-managing-cve-backlog/ | , | 2024. |  |  |  |  |  |
| sive security automation but also to advancing defensive cyber- | //www.blackhat.com/us-18/arsenal/schedule/index.html# |  |  |  |  |  |  |  |
| security research. | deep-exploit-11908 | , | 2018. | Presented at Black Hat USA 2018 |  |  |  |  |
| This research adheres to responsible cybersecurity and AI | Arsenal, Las Vegas. Accessed: 2025-07-30. |  |  |  |  |  |  |  |
| research practices. | The study does not involve zero-day ex- | https://www.metasploit.com/ | , 2024. Accessed: July 27, 2024. |  |  |  |  |  |
| ploitation or unauthorized system access, and all evaluations | [5] | Abdul Samad, Saad Altaf, and M Junaid Arshad. Advancements in au- |  |  |  |  |  |  |
| are conducted on simulated or explicitly permitted targets. Fu- | tomated penetration testing for iot security by leveraging reinforcement |  |  |  |  |  |  |  |
| and comply with relevant legal and ethical standards, in line | Bowman, Toby Richer, and Chin-Teng Lin. | Deep hierarchical rein- |  |  |  |  |  |  |
| with established guidelines for responsible AI and cybersecu- | forcement agents for automated penetration testing. | arXiv preprint |  |  |  |  |  |  |
| 9. Conclusion and Future Work | testGPT: Evaluating and harnessing large language models for automated |  |  |  |  |  |  |  |
| This work presented xO | ff | ense, an independent, fully au- | rity 24) | , pages 847–864, Philadelphia, PA, 2024. USENIX Association. |  |  |  |  |
| dress persistent limitations in existing systems such as con- | rating llm agents to automated penetration testing. In | Proceedings of the |  |  |  |  |  |  |
| text loss, limited reasoning continuity, and dependence on | 20th ACM Asia Conference on Computer and Communications Security | , |  |  |  |  |  |  |
| phase prompting mechanism and a purpose-built orchestration | rative framework. | arXiv preprint arXiv:2501.13411 | , Jan 2025. |  |  |  |  |  |
| architecture, xO | ff | ense achieves accurate multi-stage decision- | [10] | Luca Gioacchini, | Marco Mellia, | Idilio Drago, | Alexander Delsanto, |  |
| making and robust tool integration across the entire pentest life- | Giuseppe Siracusano, and Roberto Bifulco. Autopenbench: Benchmark- |  |  |  |  |  |  |  |
| cycle. | [11] | Isamu | Isozaki. | Ai-pentest-benchmark: | A | benchmark | for | auto- |
| Our | evaluation | on | AutoPenBench | and | AI-Pentest- | mated penetration testing. | https://github.com/isamu-isozaki/ |  |

---

## Page 18

| AI-Pentest-Benchmark | , 2024. | GitHub repository. Accessed: 2025- | written in go. | https://github.com/OJ/gobuster | , 2025. |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 07-30. | [33] | OWASP Amass Project. Owasp amass - in-depth attack surface mapping |  |  |  |  |  |  |  |  |  |  |
| [12] | An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, | and asset discovery. | https://github.com/owasp-amass/amass | , |  |  |  |  |  |  |  |  |
| Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. | 2025. |  |  |  |  |  |  |  |  |  |  |  |
| Qwen3 technical report. | arXiv preprint arXiv:2505.09388 | , 2025. | [34] | sqlmap Developers. | sqlmap - automatic sql injection and database |  |  |  |  |  |  |  |
| [13] | Gordon Lyon. | Nmap: | The network mapper - free security scanner. | takeover tool. | https://github.com/sqlmapproject/sqlmap | , 2025. |  |  |  |  |  |  |
| https://nmap.org/ | , 2024. Accessed: July 27, 2024. | [35] | THC Hydra Team. | Thc-hydra - network logon cracker. | https:// |  |  |  |  |  |  |  |
| [14] | Chris Sullo. Nikto web server scanner. | https://github.com/sullo/ | github.com/vanhauser-thc/thc-hydra | , 2025. |  |  |  |  |  |  |  |  |
| nikto | , 2024. Accessed: July 27, 2024. | [36] | Openwall Project. | John the ripper - password cracker. | https:// |  |  |  |  |  |  |  |
| [15] | WPScan Team. Wpscan wordpress security scanner. | https://github. | github.com/openwall/john | , 2025. |  |  |  |  |  |  |  |  |
| com/wpscanteam/wpscan | , 2024. Accessed: July 27, 2024. | [37] | O | ff | ensive Security. | Exploit database (exploit-db). | https://www. |  |  |  |  |  |
| [16] | Ryusei Maeda and Mamoru Mimura. Automating post-exploitation with | exploit-db.com/ | , 2025. |  |  |  |  |  |  |  |  |  |
| deep reinforcement learning. | Computers | & | Security | , 100:102108, 2021. | [38] | Carlos Polop. | Hacktricks: | Hacking techniques & privilege escalation |  |  |  |  |
| [17] | Van-Hau Pham, Hien Do Hoang, Phan Thanh Trung, Van Dinh Quoc, | encyclopedia. | https://book.hacktricks.xyz/ | , 2025. |  |  |  |  |  |  |  |  |
| Trong-Nghia To, and Phan The Duy. | Raiju: | Reinforcement learning- | [39] | Raj Chandel and Hacking Articles Team. Hacking articles: A cyber secu- |  |  |  |  |  |  |  |  |
| guided post-exploitation for automating security assessment of network | rity community blog. | https://www.hackingarticles.in/ | , 2025. |  |  |  |  |  |  |  |  |  |
| systems. | Computer Networks | , 253:110706, 2024. | [40] | Hongli Yu, Tinghong Chen, Jiangtao Feng, Jiangjie Chen, Weinan Dai, |  |  |  |  |  |  |  |  |
| [18] | Jiacen Xu, Jack W Stokes, Geo | ff | McDonald, Xuesong Bai, David Mar- | Qiying Yu, Ya-Qin Zhang, Wei-Ying Ma, Jingjing Liu, Mingxuan Wang, |  |  |  |  |  |  |  |  |
| shall, Siyue Wang, Adith Swaminathan, and Zhou Li. | AutoAttacker: | et al. | Memagent: Reshaping long-context llm with multi-conv rl-based |  |  |  |  |  |  |  |  |  |
| A large language model guided system to implement automatic cyber- | memory agent. | arXiv preprint arXiv:2507.02259 | , 2025. |  |  |  |  |  |  |  |  |  |
| attacks. | arXiv preprint arXiv:2403.01038 | , 2024. | [41] | O | ff | ensive Security. | Kali linux: Penetration testing and ethical hacking |  |  |  |  |  |
| [19] | Hanzheng Dai, Yuanliang Li, Zhibo Zhang, and Jun Yan. Refpentester: A | linux distribution. | https://www.kali.org/ | , 2025. |  |  |  |  |  |  |  |  |
| knowledge-informed self-reflective penetration testing framework based | [42] | Samyam Rajbhandari, Je | ff | Rasley, Olatunji Ruwase, and Yuxiong He. |  |  |  |  |  |  |  |  |
| on large language models. | arXiv preprint arXiv:2505.07089 | , 2025. | Zero: Memory optimizations toward training trillion parameter models. |  |  |  |  |  |  |  |  |  |
| [20] | Sho Nakatani. Rapidpen: Fully automated ip-to-shell penetration testing | In | SC20: | International Conference for High Performance Computing, |  |  |  |  |  |  |  |  |
| with llm-based agents. | arXiv preprint arXiv:2502.16730 | , 2025. | Networking, Storage and Analysis | , pages 1–16. IEEE, 2020. |  |  |  |  |  |  |  |  |
| [21] | Dominik M. Weber, Ioannis Tzachristas, and Aifen Sui. Perses: Unlock- | [43] | Tri | Dao, | Dan | Fu, | Stefano | Ermon, | Atri | Rudra, | and | Christopher |
| ing privilege escalation for small llms via extensible heterogeneity. | In | R´ | e. | Flashattention: | Fast and memory-e | ffi | cient exact attention with |  |  |  |  |  |
| Proceedings of the 20th ACM Asia Conference on Computer and Com- | io-awareness. | Advances in neural information processing systems | , |  |  |  |  |  |  |  |  |  |
| munications Security (ASIA CCS ’25) | . ACM, 2025. | 35:16344–16359, 2022. |  |  |  |  |  |  |  |  |  |  |
| [22] | Richard Fang, Rohan Bindu, Akul Gupta, and Daniel Kang. | Llm | [44] | TryHackMe Team. | Tryhackme: Hands-on cybersecurity training plat- |  |  |  |  |  |  |  |
| agents can autonomously exploit one-day vulnerabilities. | arXiv preprint | form. | https://tryhackme.com | , 2024. |  |  |  |  |  |  |  |  |
| arXiv:2404.08144 | , 2024. | [45] | HackTheBox Team. | Hack the box: Cybersecurity labs and challenges. |  |  |  |  |  |  |  |  |
| [23] | Yuxuan Zhu, Antony Kellermann, Akul Gupta, Philip Li, Richard Fang, | https://www.hackthebox.com | , 2024. |  |  |  |  |  |  |  |  |  |
| Rohan Bindu, and Daniel Kang. Teams of llm agents can exploit zero-day | [46] | VulnHub Community. | Vulnhub: | Vulnerable machines for penetration |  |  |  |  |  |  |  |  |
| vulnerabilities. | arXiv preprint arXiv:2406.01637 | , Mar 2025. | testing practice. | https://www.vulnhub.com | , 2024. |  |  |  |  |  |  |  |
| [24] | Lajos Muzsai, David Imolai, and Andr´ | as Luk´ | acs. Hacksynth: Llm agent | [47] | HuggingFace Team. Huggingface datasets hub: Open-source datasets for |  |  |  |  |  |  |  |
| and evaluation framework for autonomous penetration testing. | arXiv | machine learning. | https://huggingface.co/datasets | , 2024. |  |  |  |  |  |  |  |  |
| preprint arXiv:2412.01778 | , 2024. | [48] | Migel Tissera and WhiteRabbitNeo Team. | Whiterabbitneo cybersecu- |  |  |  |  |  |  |  |  |
| [25] | Minghao Shao, Sofija Jancheska, Meet Udeshi, Brendan Dolan-Gavitt, | rity dataset (wrn-chapter-1, wrn-chapter-2). | https://huggingface. |  |  |  |  |  |  |  |  |  |
| Haoran | Xi, | Kimberly | Milner, | Boyuan | Chen, | Max | Yin, | Siddharth | co/datasets/WhiteRabbitNeo/WRN-Chapter-1 | , 2024. |  |  |

Garg, Ramesh Karri, Prashanth Krishnamurthy, Farshad Khorrami, and

Muhammad Shafique. Nyu ctf bench: A scalable open-source bench-

mark dataset for evaluating llms in o ff ensive security. In NeurIPS 2024

Datasets and Benchmarks Track , 2024.

[26] Yuxuan Zhu, Antony Kellermann, Dylan Bowman, Philip Li, Akul Gupta,

Adarsh Danda, Richard Fang, Conner Jensen, Eric Ihli, Jason Benn, Jet

Geronimo, Avi Dhir, Sudhit Rao, Kaicheng Yu, Twm Stone, and Daniel

Kang. Cve-bench: A benchmark for ai agents’ ability to exploit real-

world web application vulnerabilities. arXiv preprint arXiv:2503.17332 ,

Mar 2025.

[27] Isamu Isozaki, Manil Shrestha, Rick Console, and Edward Kim. To-

wards automated penetration testing: Introducing LLM benchmark, anal-

ysis, and improvements. In Proceedings of the 2025 ACM Conference

(companion / adjunct) on Computer and Communications Security , 2025.

Accessed: 2025-08-06.

[28] Julius Henke. Autopentest: Enhancing vulnerability management with

autonomous llm agents. arXiv preprint arXiv:2505.10321 , 2025.

[29] Guohao Li, Hasan Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard

Ghanem. Camel: Communicative agents for ”mind” exploration of large

language model society. In A. Oh, T. Naumann, A. Globerson, K. Saenko,

M. Hardt, and S. Levine, editors, Advances in Neural Information Pro-

cessing Systems , volume 36, pages 51991–52008. Curran Associates,

Inc., 2023.

[30] Qian Liu, Jinke Song, Zhiguo Huang, Yuxuan Zhang, glide-the,

and liunux4odoo. Langchain-Chatchat. https://github.com/

chatchat-space/Langchain-Chatchat , 2024. Accessed: 2026-04-

27.

[31] DirB Project. Dirb web content scanner. https://gitlab.com/

kalilinux/packages/dirb , 2025.

[32] Gobuster Project. Gobuster - directory / file, dns and vhost busting tool

18

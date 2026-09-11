---
title: "Benchmarking Practices in LLM-driven Offensive Security: Testbeds, Metrics, and Experiment Design"
author: "Andreas Happe; Jürgen Cito"
creator: "arXiv GenPDF (tex2pdf:)"
pages: 11
---

# Benchmarking Practices in LLM-driven Offensive Security: Testbeds, Metrics, and Experiment Design

> **作者**：Andreas Happe; Jürgen Cito
> **總頁數**：11 頁

---

## Page 1

Benchmarking Practices in LLM-driven Offensive Security:

Testbeds, Metrics, and Experiment Design

| Andreas Happe | Jürgen Cito |
| --- | --- |
| andreas.happe@tuwien.ac.at | juergen.cito@tuwien.ac.at |
| TU Wien | TU Wien |
| Vienna, Austria | Vienna, Austria |
| ABSTRACT | security of LLMs themselves such as CyberSecEval [1, 2, 41], i.e., |
| Large Language Models (LLMs) have emerged as a powerful ap- | red-teaming LLMs. |

proach for driving offensive penetration-testing tooling. Due to the

opaque nature of LLMs, empirical methods are typically used to

review 19 research papers detailing 18 prototypes and their respec-

tive testbeds.

for future research, emphasizing the importance of extending ex-

tween security research and practice, suggesting that CTF-based

challenges may not fully represent real-world penetration testing

scenarios.

tion ; Operational analysis .

Large Language Models, LLMs, Penetration Testing, Empirical Re-

The rapid evolution of Large Language Models (LLMs) has led to

remarkable capabilities in various tasks, including offensive secu-

rity tasks such as penetration testing, vulnerability discovery and

arXiv:2504.10112v2 [cs.CR] 16 Jun 2025 exploitation [4, 8, 17, 21, 26, 28, 43, 45, 46, 48]. The opaque nature

of LLMs requires employing empirical methods for their evalua-

tion. Thus, security researchers investigating the use of LLMs for

offensive security depend on benchmarking and testbeds to assess

the efficacy and effectiveness of their respective prototypes.

for red-teaming [13]. We do not analyze testbeds for testing the

1.1 Contributions

searchers:

ing offensive LLMs.

• Methods used for analysis.

2 BACKGROUND

The background section establishes a common understanding of

referenced later within this work.

Benchmarks

means for testing something in development ” while a baseline is a “ a

or a control .” A benchmark is defined by “ something that serves as

a standard by which others may be measured or judged ” or by “ a

standardized problem or test that serves as a basis for evaluation

or comparison ”. The former can be achieved by using a baseline

as benchmark, the latter can be achieved if a testbed consists of

multiple atomic test-cases for which the test subjects success rate

can be measured.

Actions on Objective.

| analyze their efficacy. The quality of this analysis is highly depen- | Our motivation is to present current common practices with regard |  |  |  |
| --- | --- | --- | --- | --- |
| dent on the chosen testbed, captured metrics and analysis methods | to testbeds, benchmarks, metrics and employed analysis techniques. |  |  |  |
| employed. | Based upon the identified common practices, we identify sensible |  |  |  |
| This paper analyzes the methodology and benchmarking prac- | recommendation to which future research can depend to. To the |  |  |  |
| tices used for evaluating Large Language Model (LLM)-driven at- | best of our knowledge this publication is the first that provides |  |  |  |
| tacks, focusing on offensive uses of LLMs in cybersecurity. We | an empirical investigation for the following relevant areas for re- |  |  |  |
| We detail our findings and provide actionable recommendations | • | Composition and provenance of testbeds used for evaluat- |  |  |
| isting testbeds, creating baselines, and including comprehensive | • | Experiment design including guidance on used metrics, |  |  |
| metrics and qualitative analysis. We also note the distinction be- | sample sizes, and LLM selection. |  |  |  |
| CCS CONCEPTS | used terms and subsequently provides background information |  |  |  |
| • | Software and its engineering | → | Empirical software valida- | about common penetration testing standards and CTF challenges |
| KEYWORDS | 2.1 | Definitions: Testbeds, Baselines and |  |  |
| search, Testbed, Benchmark, Metrics, Testcases, Analysis | According to Merriam-Webster, a testbed is “ | any device, facility, or |  |  |
| 1 | INTRODUCTION | usually initial set of critical observations or data used for comparison |  |  |
| This paper provides an empirical investigation of testbeds used | 2.2 | Penetration Testing Standards |  |  |
| within offensive security research. We investigate their capabilities | Research indicates that penetration tests are not standardized for |  |  |  |
| as well as metrics captured during prototype evaluation. We detail | all domains, or that security professionals do not heed documented |  |  |  |
| our findings and provide actionable recommendations for future | standards [14, 40]. Attack methodologies such as NIST 800-115 [34] |  |  |  |
| research. Given the substantial costs of performing experiments | or the Lockheed Martin Cyber Kill Chain detail different attack |  |  |  |
| using reasoning LLMs, we believe that this paper will offer valuable | phases, not concrete attacks [30]. For example, the Cyber Kill Chain |  |  |  |
| insights regarding experiment design for future publications. | includes the following phases: Reconnaissance, Weaponization, |  |  |  |
| We focus on testbeds for offensive use of LLMs, e.g., using LLMs | Delivery, Exploitation, Installation, Command and Control, and |  |  |  |

---

## Page 2

| Abbrev. | Name | VM/Cloud | Description |
| --- | --- | --- | --- |
| THM | TryHackMe | Cloud | Educational CTF platform |
| picoCTF | Cloud | CMU CTF education platform |  |
| VulnHub | VM | vulnerable VM collection |  |

for commonly used web vulnerabilities. The included Top 10 items

Misconfiguration”.

Taxonomies such as MITRE ATT&CK provide detailed infor-

mation about attackers’ techniques and tooling without providing

to include more web vulnerabilities as well as Active Directory

challenges. In Jeopardy-style CTFs, participants face a series of

separate challenges categorized into their respective topics. They

tacker/Defender CTFs, participants have to defend their infrastruc-

ture while attacking other teams’ infrastructure. They typically

employ simulated networks with vulnerable systems. These chal-

lenges offer more realistic scenarios but are complex to organize

and require additional resources. Jeopardy-style challenges are of-

Andreas Happe and Jürgen Cito

Source

https://tryhackme.com

https://picoctf.org/

https://www.vulnhub.com/

Shields exercise 2 .

be reproduced locally.

3 METHODOLOGY

date of May 2025.

penetration testing as well as an empirical evaluation of their pro-

paper.

This section gives a short overview about the included papers,

the relationship between them, and their respective novelty. All

included papers are detailed in Table 2.

2 https://ccdcoe.org/locked-shields/

detailing the NYU CTF and respective offensive attack prototype. One paper details

Table 1: CTF platforms mentioned within reviewed publications. For each platform, its full name and, if existing, a commonly

used abbreviation is given. We differentiate between platforms offering VMs or cloud-based offerings. The former allow for

local execution and archival of challenges; the latter are typically “walled-gardens” accessible within the cloud.

| HTB | HackTheBox | Cloud | Educational CTF platform | https://www.hackthebox.com/ |  |
| --- | --- | --- | --- | --- | --- |
| lin.security | VM | linux privesc VM | https://www.vulnhub.com/entry/linsecurity-1,244/ |  |  |
| metasploitable2 | VM | metasploit education VM | https://docs.rapid7.com/metasploit/metasploitable-2/ |  |  |
| OTW | OverTheWire | Cloud | Educational CTF challenges | https://overthewire.org/wargames/ |  |
| GOAD | A Game of AD | VM | Educational vulnerable AD | https://github.com/Orange-Cyberdefense/GOAD |  |
| Real-life penetration tests are often structured around “Top 10” | participants, while Attacker/Defender-style challenges are typically |  |  |  |  |
| vulnerability lists for various areas [14], e.g., the OWASP Top 10 | more advanced team-oriented events such as the NATO Locked |  |  |  |  |
| are often broad and do not provide authoritative test cases. For | Table 1 gives an overview of CTF platforms mentioned within |  |  |  |  |
| example, the OWASP Top 10 contains the entry “Injection” that | our reviewed papers. While the mentioned cloud-based CTFs are |  |  |  |  |
| could be achieved through dozens of attack techniques and pro- | free to use or provide free tiers, they do not make the building |  |  |  |  |
| cedures. Another example of a “fuzzy” Top 10 item is “Security | instructions of their challenges available publicly, and thus cannot |  |  |  |  |
| overall attack strategies [30]. | We used Google Scholar to identify surveys containing the key- |  |  |  |  |
| Penetration Testing and its employed techniques is continuously | words “offensive security LLM” ([4, 8, 17, 21, 26, 28, 43, 45, 46, 48]). |  |  |  |  |
| changing. For example, the renowned OSCP certification | 1 | changed | We analyzed surveyed publications and limited our selection to |  |  |
| its focus from exploit writing, e.g., creating buffer overflow exploits, | English publications released between 2023–2025 with a cut-off |  |  |  |  |
| exploitation. | Publications had to include both an LLM-driven prototype for |  |  |  |  |
| 2.3 | CTF Challenges | totype using a documented testbed. We performed exponential |  |  |  |
| Our investigated testbeds commonly include tasks based on Capture- | non-discriminative snowball sampling (forward-referencing) by |  |  |  |  |
| the-Flag (CTF) challenges in which the player typically has to ex- | including papers linked from our initial paper seed, resulting in our |  |  |  |  |
| ploit one or multiple vulnerabilities to gather a flag (secret string) | final 19 papers detailing 18 prototypes and their respective testbeds |  |  |  |  |
| as proof of compromise. CTFs typically include a diverse set of | detailed in Table 2. | 3 | Using forward-referencing also reduces the |  |  |
| tasks, including cryptography, steganography, forensics, logic “puz- | internal threat of selection bias. |  |  |  |  |
| zles”, exploitation writing, privilege escalation, network attacks and | We performed multi-stage thematic analysis [5, 33]. Initially, |  |  |  |  |
| web exploitation challenges. CTFs are often used for educational | each author read the gathered papers and identified themes. To in- |  |  |  |  |
| purposes, e.g., for training new security professionals. Empirical re- | crease trustworthiness [32], | reflexive journaling | was employed and |  |  |
| search has shown that they support knowledge transfer [14, 22, 23], | the identified themes discussed with two professional penetration- |  |  |  |  |
| i.e., patterns and techniques learned during CTF exercises can be | testers ( | peer debriefing | [20]). Subsequently, | team consensus | [32] was |
| applied during real-world penetration-testing assignments. | used to create the final themes. Subsequently, all papers were coded |  |  |  |  |
| CTFs can be classified into Jeopardy and Attacker/Defender | using the refined themes, resulting in the data used within this |  |  |  |  |
| are easier to score and analyze, but offer reduced realism. In At- | 4 | THE ANALYZED PUBLICATIONS |  |  |  |
| ten used for educational events that need to scale-out for many | 3 | The discrepancy between selected publications and testbeds results from two papers |  |  |  |
| 1 | https://www.offsec.com/courses/pen-200/ | the testbed while the other paper details the offensive prototype. |  |  |  |

---

## Page 3

Benchmarking Practices in LLM-driven Offensive Security: Testbeds, Metrics, and Experiment Design

Table 2: Publications included in this survey. Initial Version and Current Version indicate the first and latest version of the

publication available on arXiv. Versions ( V. )gives the number of paper versions available on arXiv. If a paper has already been

published, the used publication outlet is indicated by Venue , WS indicates a workshop. Publications are listed in chronological

order as given by the date of initial publication on arXiv.

| LLMs as Hackers [16] | Happe et al. |
| --- | --- |
| Llm agents can autonomously hack websites [10] | Fang et al. |

An empirical eval. of llms for solving offensive se- Shao et al.

curity challenges [36]

AutoAttacker [44] Xu et al.

Llm agents can autonom. exploit one-day vulns. [9] Fang et al.

Teams of llm agents can exploit zero-day vulns. [11] Fang et al.

| Cybench [47] | Zhang et al. |
| --- | --- |
| AutoPenBench [12] | Gioacchini et al. |
| Towards Automated Penetration Testing [19] | Isozaki et al. |
| AutoPT [42] | Wu et al. |
| HackSynth [29] | Muzsai et al. |
| Vulnbot [24] | Kong et al. |

On the Feasibility of Using LLMs to Execute Multi- Singer et al.

stage Network Attacks [38]

| Can LLMs Hack Enterprise Networks? [15] | Happe et al. |
| --- | --- |
| RapidPen [31] | Nakatani et al. |

(August 2023). The former implemented a closed feedback-loop

introduced the influential Pentest-Task-Tree for strategy planning.

one-day vulnerabilities [9, 31] or even zero-day vulnerabilities [11].

PenHeal [18] introduced a dual-purpose prototype implementing

both offensive as well as defensive capabilities.

context to store their current state. Publications experimented with

different ways of either reducing the used state [16] or using RAG

| Initial | Current |  |
| --- | --- | --- |
| 2023-10-17 | 5 | 2025-02-18 |
| 2024-02-06 | 3 | 2024-06-16 |

2024-02-19

2024-03-02

| 2024-04-11 | 2 | 2024-04-17 |
| --- | --- | --- |
| 2024-06-02 | 2 | 2025-03-30 |
| 2024-08-15 | 4 | 2025-04-12 |
| 2024-10-04 | 2 | 2024-10-28 |
| 2024-10-22 | 4 | 2025-02-21 |

2024-11-02

2024-12-02

2025-01-23

2025-01-27 3 2025-05-16

2025-02-06

2025-02-23

5 RESULTS

5.1 Testbed Design

Table 3 shows the overall design of the analyzed testbeds, detailing

tion choices.

lar hosts as their target systems, either by providing a direct shell

| Publication | Authors | Version | V. | Version | Venue |
| --- | --- | --- | --- | --- | --- |
| Getting pwned by AI [13] | Happe et al. | 2023-07-24 | 3 | 2023-08-17 | ESEC/FSE’23 |
| PentestGPT [7] | Deng et al. | 2023-08-13 | 2 | 2024-06-02 | Usenix Security’24 |
| NYU CTF Dataset [37] | Shao et al. | 2024-06-08 | 3 | 2025-02-18 | NeurIPS’24 (WS) |
| PenHeal [18] | Hyuang et al. | 2024-07-25 | AutonomousCyber’24 (WS) |  |  |
| Initial Papers. | Two papers were referenced by all other reviewed | them [37, 47] were based on live real-world CTF events, while two |  |  |  |
| papers: | Getting pwn’d by AI | [13] (July 2023) and | PentestGPT | [7] | were based on virtual CTF machines [12, 19]. |
| between an LLM and a target to autonomously perform a privilege- | Targeting Networks. | Recent publications switched their target |  |  |  |
| escalation attack; the latter incorporated LLMs with human instruc- | from single-host targets to attacking whole organization networks [15, |  |  |  |  |
| tions and feedback to interactively hack CTF machines. They also | 38] spanning multiple computer systems. |  |  |  |  |
| Autonomous Exploitation. | Subsequent papers studied autonomous | The 19 analyzed papers leveraged 18 testbeds of which 7 created new |  |  |  |

exploitation within different domains ranging from web-applications [10, benchmarks reusing existing CTF cases while 10 papers implement

| 42], to post-breach attacks against Linux- [16] or Windows-based [44] | a new benchmark from scratch. A single paper (vulnbot [24]) reused |  |  |
| --- | --- | --- | --- |
| systems. LLMs have been used to autonomously exploit known | two existing benchmarks for their evaluation. |  |  |
| State/Context Management. | LLMs only have access to limited | the benchmarks’ target systems, its provenance, and implementa- |  |
| for both internal or external data storage [18, 31, 44]. A | planner | Target Systems. | Testbeds commonly emulated Linux, Windows, |
| component for creating a high-level strategy was used by multiple | or Web-based systems. Two benchmarks (Cybench [47] and NYU [37]) |  |  |
| publications [11, 15, 24, 29, 44]. Multiple papers were influenced by | included traditional CTF challenges such as cryptography, forensics, |  |  |
| pentestGPT’s | Pentest-Task-Tree | [15, 18]. | reversing, and exploit-generation. All but two papers used singu- |
| Benchmarks/Testbeds. | Four papers focused on the introduction of | connection or by designating the target by its singular IP network |  |
| a new penetration-testing benchmark and included their respective | address. The remaining two benchmarks used simulated networks |  |  |
| LLM-guided offensive prototype for benchmark evaluation. Two of | containing multiple virtual machines. One benchmark [44] created |  |  |

---

## Page 4

Tasks. Benchmarks contained between 1–200 high-level tasks

(average: 26 . 1, median: 15), typically provided through a sepa-

rate virtual machine or container. One benchmark—the NYU CTF

dataset [37]—contained 200 tasks but only few penetration-testing

specific cases (19 web pen-testing tasks). Depending on the used

benchmark, high-level tasks were separated into multiple steps,

subtasks, or vulnerabilities. There was no common vocabulary nor

semantics for what constitutes a sub-tasks.

Andreas Happe and Jürgen Cito

identified and mapped the needed sub-steps.

available CTF walk-throughs [19]. AutoPenBench [12] defined both

“gold steps” as well as milestones. Milestones are either defined by

executing specific commands stated within the golden steps or by

achieving tasks. LLMs are employed to match log traces against

the golden steps and milestones, and human quality control is

additionally performed.

Table 3: Testbed Overview. Testcases can either be reused (R) from e.g. CTFs or CVEs, created from scratch (S) for the benchmark,

or reused from another benchmark (B). The Implementation (Impl.) can be based upon Container (C) or Virtual Machines (VM).

Provenance is denoted as released (R) if the benchmark is publicly released, documented (D) if it is not released but enough

information, e.g., CVEs, are provided to reproduce the benchmark, and coarse (C) if only rough categories and not concrete

vulnerabilities are given. # Tasks counts distinct test-cases which can include a number of vulnerabilities ( # Vuln. ). If achieving

a task includes multiple vulnerabilities but the overall number of vulnerabilities is not stated, a “?” is used. Subtasks indicates

if a task is deconstructed into individual sub-tasks which are tracked. Linux / Windows / Web / Other denotes the target domain.

Target describes the target implementation: localhost indicates that attacker and target run on the same computer, single-host

that the attacker targets a single network computer, and network that a whole network-range is the attacker’s target.

| Publication | Testcases | Impl. | Provenance | Sources | # Tasks | Subtasks | # Vuln. | Linux | Windows | Web | Other | Target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Getting pwned by AI [13] | R | VM | R | lin.security | 1 | ? | ✓ | localhost |  |  |  |  |
| LLMs as Hackers [16] | S | VM | R | THM | 12 | ✓ | 12 | ✓ | localhost |  |  |  |
| Autonomously Hack Websites [10] | S | C | 15 | 15 | ✓ | single-host |  |  |  |  |  |  |
| Autonomously Exploit One-day Vulns. [9] | S | D | CVEs | 15 | 15 | ✓ | ✓ | ✓ | single-host |  |  |  |
| Exploit Zero-Day Vulnerabilities [11] | S | D | CVEs | 15 | 15 | ✓ | single-host |  |  |  |  |  |
| PenHeal [18] | R | VM | R | metasploitable | 1 | 10 | ✓ | ✓ | single-host |  |  |  |
| AUTOPENBENCH [12] | S | C | R | basic + CVEs | 33 | ✓ | 33 | ✓ | ✓ | ✓ | single-host |  |
| HackSynth [29] | R | R | picoCTF, OTW | 200 | 200 | ✓ | ✓ | ✓ | single-host |  |  |  |
| Vulnbot [24] | B | - | [12, 19] | single-host |  |  |  |  |  |  |  |  |
| Multistage Network Attacks [38] | S | R | VulnHub | 13 | ✓ | 152 | ✓ | network |  |  |  |  |
| pentestGPT [7] | R | VM | R | HTB, VulnHub | 13 | ✓ | 182 | ✓ | ✓ | ✓ | single-host |  |
| Can LLMs hack Enterprise Networks? [15] | R | VM | R | GOAD | 15+ | ✓ | ? | ✓ | network |  |  |  |
| Towards Automated Penetration Testing [19] | S | VM | R | VulnHub | 13 | 162 | ✓ | single-host |  |  |  |  |
| AutoAttacker [44] | S | VM | C | 14 | 14 | ✓ | ✓ | single-host |  |  |  |  |
| CyBench [47] | S | C | R | CTFs | 40 | ✓ | ✓ | ✓ | ✓ | single-host |  |  |
| NYU CTF Dataset [36, 37] | S | C | R | CTFs | 26 | ✓ | ✓ | single-host |  |  |  |  |
| RapidPen [31] | R | VM | R | HTB | 1 | ✓ | single-host |  |  |  |  |  |
| AutoPT [42] | R | VM | R | VulnHub | 17 | 20 | ✓ | single-host |  |  |  |  |
| a test network, but the test-cases themselves were only targeting | Sub-Tasks. | All reviewed papers provided a binary success rate: |  |  |  |  |  |  |  |  |  |  |
| individual systems and thus were counted as a single-host bench- | a test-case is either completed successfully or not. 6 publications |  |  |  |  |  |  |  |  |  |  |  |
| mark. | provided fine-grained sub-task analysis. They differed in how they |  |  |  |  |  |  |  |  |  |  |  |
| Reproducibility. | One benefit of reusing existing CTF tasks was | Happe et al. [16] performed an analysis of captured log traces |  |  |  |  |  |  |  |  |  |  |
| improved reproducibility as the included tasks are typically pub- | utilizing human pen-testers to match executed sub-tasks to MITRE |  |  |  |  |  |  |  |  |  |  |  |
| licly available—albeit sometimes behind a paywall. Of the self-built | ATT&CK tactics and procedures. Deng et al. [7] used NIST 800-115 |  |  |  |  |  |  |  |  |  |  |  |
| benchmarks, only a single one [16] was publicly available. Of the | to classify tasks into 10 broad categories and showed how testing |  |  |  |  |  |  |  |  |  |  |  |
| remaining five benchmarks, two were specified through their im- | trajectories traverse through these categories. Other papers create |  |  |  |  |  |  |  |  |  |  |  |
| plemented CVEs and thus reproducible. Finally, three benchmarks | an a-priori list of tasks that must be executed by an attacker to |  |  |  |  |  |  |  |  |  |  |  |
| only provided coarse documentation, e.g., used attack classes, thus | achieve exploitation. These steps were often created manually— |  |  |  |  |  |  |  |  |  |  |  |
| limiting their reproducibility. | by the authors or dedicated pen-testers—or by analyzing publicly |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 5

Benchmarking Practices in LLM-driven Offensive Security: Testbeds, Metrics, and Experiment Design

Table 4: LLM used within Publications. Used Models gives the list of used LLMs as stated within the respective publication.

Walled-Garden indicates that at least a LLM without access to the model weights (typically cloud-hosted) was used. Open-Weight

indicates that at least a LLM with publicly available model weights was used. SLM (“Small Language Model”) indicates inclusion

of a LLM with less than 16b parameters which implies usability on consumer-grade graphics cards. Finally, Reasoning Model

indicates that at least one reasoning model was used during the benchmark.

| Publication | Walled-Garden | Open-Weight | SLM | Reasoning Model | # of LLMs evaluated | Used LLMs |
| --- | --- | --- | --- | --- | --- | --- |
| Getting pwned by AI [13] | ✓ | 1 | gpt-3.5-turbo |  |  |  |
| LLMs as Hackers [16] | ✓ | ✓ | ✓ | 4 | gpt-3.5-turbo, gpt-4-turbo, llama3:70b, llama3:8b |  |
| Autonomously Hack Websites [10] | ✓ | ✓ | ✓ | 10 | gpt-3.5, gpt-4, openhermes-2.5-mistral:7b, llama2-chat:70b, |  |

llama2-chat:13b, llama2-chat:7b, mixtral:8x7b, mistral-instruct-

v2:7b, nous-hermes-2-yi:34b, openchat 3.5

Autonomously Exploit One-day Vulns. [9] ✓ ✓ ✓ 10 gpt-3.5, gpt-4, openhermes-2.5-mistral:7b, llama2-chat:70b,

llama2-chat:13b, llama2-chat:7b, mixtral:8x7b, mistral-instruct-

v2:7b, nous-hermes-2-yi:34b, openchat 3.5

| Exploit Zero-Day Vulnerabilities [11] | ✓ | ✓ | 3 | gpt-4-0125-preview, llama-3.1:405b, qwen-2.5:72b |  |
| --- | --- | --- | --- | --- | --- |
| PenHeal [18] | ✓ | 1 | gpt-4 |  |  |
| AUTOPENBENCH [12] | ✓ | 1 | gpt-4o |  |  |
| HackSynth [29] | ✓ | ✓ | ✓ | 8 | gpt-4o, gpt-4o-mini, llama-3.1:8b, llama-3.1:70b, qwen2:72b, mix- |

tral:8x72b, phi-3-mini-4k, phi-3.5-MoE

| Vulnbot [24] | ✓ | ✓ | 3 | gpt-4o, llama3.3:70b, llama3.1:405b |  |
| --- | --- | --- | --- | --- | --- |
| Multistage Network Attacks [38] | ✓ | 3 | gpt-4o, gemini 1.5 pro, sonnet 3.5 |  |  |
| pentestGPT [7] | ✓ | 3 | gpt-3.5, gpt-4, bard |  |  |
| Can LLMs hack Enterprise Networks? [15] | ✓ | ✓ | 2 | o1, gpt-4o |  |
| Towards automated penetration testing [19] | ✓ | ✓ | 2 | gpt-4o, llama3.1:405b |  |
| AutoAttacker [44] | ✓ | ✓ | ✓ | 4 | gpt-3.5, gpt-4, llama2-chat:7b, llama2-chat:70b |
| CyBench [47] | ✓ | ✓ | ✓ | 8 | GPT-4o, o1-preview, Claude 3 Opus, Claude 3.5 Sonnet, Gemini |

1.5 Pro, Mixtral-Instruct:8x22b, Llama-3-Chat:70B, Llama-3.1-

Instruct:405B

NYU CTF Dataset[36, 37] ✓ 5 Mixtral-Instruct-v0.1:8x7B, deepseek-coder-instruct:33b,

llama3-instruct:70b, wizardlm2:8x22b, Llama-3-Instruct:70B

| RapidPen [31] | ✓ | 1 | gpt-4o |
| --- | --- | --- | --- |
| AutoPT [42] | ✓ | 3 | gpt-3.5, gpt-4, gpt-4-mini |
| 5.2 | Experiment Design | count all LLMs using less that 16b parameters as SLMs. Using 4bit |  |
| LLM Selection. | Experiments within the reviewed papers typi- | quantization, these models fit into 8 gigabyte of memory while |  |
| cally analyzed between 1–10 LLMs (average 4 | . | 0, median 3). Two | being able to generate adequate token counts for interactive use on |
| papers [12, 42] were performing preliminary experiments to iden- | desktop-class computers. A quarter of the publications (5 papers) |  |  |
| tify and remove LLMs with insufficient capabilities from their eval- | included SLMs within their evaluation. Reasoning LLMs, which are |  |  |
| uation set. An overview of the used LLMs is given in Table 4. | a recent addition to LLM capabilities, were included in two of the |  |  |
| The prevalently used LLM-family were OpenAI’s non-reasoning | reviewed publications. |  |  |
| models which were included in all but one publication. Distant | Sample Size. | Table 6 details sample sizes and upper-bounds en- |  |
| second was Meta’s Llama family which was included in roughly | countered within reviewed publications. During experiments, be- |  |  |
| half of the papers while Mistral’s LLM-family being included in a | tween 1–6 test-runs/samples were executed per LLM (average 4 | . | 6, |
| quarter of the papers. | median 5). Only half of the papers detailed the length of the cap- |  |  |
| There is no authoritative definition for Small Language Mod- | tured samples. If reported, the maximum sample duration was either |  |  |
| els (SLMs), but given the common understanding that these are | defined through an upper-bound of executed steps/commands (15– |  |  |
| models that are able to run on edge-devices such as desktops, we | 60 steps, on average 30 steps), or through introducing a maximum |  |  |

---

## Page 6

Baselines. Papers offered baselines to compare their LLM-driven

prototypes against. Human baselines were either provided through

quantitative analysis of log traces produced by human penetration

testers [16] or through analysis of human-generated example walk-

used pentestGPT [7]). Table 6 gives an overview of the baselines

5.3 Measures and Analysis

Half of the papers (8) captured input/output token counts and

mand execution resulted in errors.

All testbeds were implemented using either containers or virtual ma-

chines (VMs). The chosen virtualization technology impacts testbed

design, i.e., using containers effectively prevents using Windows-

based test-cases. Containers and VMs also provide different security

boundaries which impact the testbed’s safety, e.g., containers can-

not be used to safety provide kernel-level vulnerabilities.

Testbeds were often intertwined with an agent prototype or

framework. While this does not enforce the use of the respective

4 Zed Attack Proxy, https://www.zaproxy.org/

Andreas Happe and Jürgen Cito

ware versions. As Isozaki et al. [19] noted, retired HackTheBox

machines are only available for premium accounts. Commercial

offerings typically do not detail their setup nor provide build-

instructions for provided CTF challenges.

A benchmark’s task composition is of utmost importance for its

construct validity, i.e., how well the benchmark approximates real-

structure penetration-tests.

created benchmark.

metasploitable2 , or GOAD . While they offer the benefit of matching

their included attack vectors are often insufficiently documented.

For example, Happe et al. [13] initially used the lin.bench virtual

machine for evaluating Linux privilege escalation techniques. In

later works [16], they switched to a bespoke benchmark consisting

of a single VM per vulnerability class as LLMs otherwise would

always exploit the same “simple” attack paths within lin.security.

PenHeal [18] uses a single metasploitable2 virtual machine as a

testbed and details the included attack classes within their paper.

Concurrent walk-throughs 6 indicate that additional attack classes

| sample duration (ranging from 10 minutes to 48 hours). Two papers | agent framework, it might ease the integration of a potenial attack |  |  |
| --- | --- | --- | --- |
| supplemented test-cases in addition to their defined benchmark. | prototype into the target testbed. |  |  |
| PentestGPT | [7] used additional CTF test-cases, while Fang et al. [10] | Using commercial cloud-based CTF VMs, e.g., HackTheBox or |  |
| targeted 50 additional hand-curated web-sites of undefined prove- | TryHackMe, has implications on availability and reproducibility. |  |  |
| nance. | Cloud providers do not guarantee testbed stability, e.g., used soft- |  |  |
| throughs (see Section 6.7). Automated baselines were created by | Recommendation. | Evaluate technology choices esp. for safety |  |
| running traditional automated security security tooling (e.g., ZAP | 4 | and security implications, e.g., if system-level attacks are part of the |  |
| or metasploit | 5 | ) or existing LLM-driven prototypes (2 papers used | testbed, virtual machines should be used. The testbed or building |
| prototypes from the respective authors prior work, while 5 papers | instructions should be available “offline” to allow for reproducibility. |  |  |
| used within reviewed publications. | 6.2 | Benchmark Composition |  |
| All of the reviewed papers tracked the success rates of their proto- | life security practitioners’ work and challenges. |  |  |
| types, typically split-up per test-case and/or per tested LLM. Com- | Benchmark tasks were typically mapped to existing attack vector |  |  |
| plex and realistic vulnerabilities often consist of multiple causally- | classification schemes such as MITRE ATT&CK or the OWASP |  |  |
| dependent tasks, e.g., an autonomous agent must initially enumer- | Top 10 Web Vulnerabilities. A reverse mapping, i.e., showing the |  |  |
| ate the system, identify a vulnerability, and subsequently exploit it; | coverage that a benchmark provides of a hacking discipline, was |  |  |
| only tracking the binary outcome cannot detail LLMs’ capabilities | not provided. A potential reason for this is that while classification |  |  |
| with those intermediate steps. 6 out of the 18 analyzed prototypes | schemes for attack vectors exist within penetration testing, they |  |  |
| tracked these mentioned sub-steps. | do not provide a hacking methodology and thus cannot be used to |  |  |
| used them for cost estimates, typically stated in US$. This is a | Not having an authoritative source of attack vectors opens up |  |  |
| convenient estimate of a prototype’s efficiency as occurring costs | task composition for discussion. For example, should basic file oper- |  |  |
| are highly dependent upon the used LLM and their tokenizers. | ations (reading, writing, or uploading files) or navigation within the |  |  |
| LLMs commonly have asymmetric pricing for input and output | target system, be part of a security benchmark? AutoAttacker [44] |  |  |
| tokens; their pricing frequently changes over time. Due to this | and HackSynth [29] contain tasks that verify that LLMs are able to |  |  |
| dynamic pricing regime, stating the occurred costs allows for easier | perform these basic system operations. Fang et al. [9, 11] call exist- |  |  |
| long-term comparison of the prototype’s efficiency. | ing benchmarks “toy problems” and create their own benchmark |  |  |
| Detailed information about executed commands was sparse. 9 | based upon CVEs, i.e., software with known vulnerabilities. While |  |  |
| papers tracked the amount of executed system commands, either | they never define the term “toy problems”, it could be explained |  |  |
| directly or indirectly through their stated “round” number. Of these, | by benchmarks including the mentioned basic tasks such as file |  |  |
| roughly half (4 papers) classified executed commands or provided a | operations. On the other hand, benchmarks such as NYU [37] or |  |  |
| list of frequently executed commands. 7 papers additionally tracked | CyBench [47] are themselves partially based on CVEs, thus while |  |  |
| the amount of invalid commands and further detailed why com- | often called “toy benchmarks”, they are comparable with a Fang’s |  |  |
| Every paper performed a qualitative analysis of error traces, | Another issue arises from using virtual machines that are origi- |  |  |
| ubiquitously by the respective authors. | nally intended for penetration-tester education, such as | lin.security | , |
| 6 | DISCUSSION AND RECOMMENDATIONS | penetration-tester real-life experiences, they typically contain mul- |  |
| 6.1 | Technology/Implementation Choices | tiple parallel vulnerabilities within the same virtual machine and |  |
| 5 | https://www.metasploit.com/ | 6 | https://docs.rapid7.com/metasploit/metasploitable-2-exploitability-guide |

---

## Page 7

Benchmarking Practices in LLM-driven Offensive Security: Testbeds, Metrics, and Experiment Design

Table 5: The experiment design utilized within the reviewed publications. If supplemental test-cases were used in addition

to the described testbed, they are noted as Additional Test-Cases . We detail the number of used LLMs ( # LLMs ) as well as the

number of independent test-runs/samples ( Sample Size ). We also document the stop condition of the performed experiment,

which was either given as a maximum number of steps ( Max. Steps/Sample ) or a maximum time (in Minutes) per Sample ( Max.

Time/Sample ).

| Additional | Max. | Max. |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Publication | Test-Cases | # LLMs | Sample Size | Steps/Sample | Time/Sample |
| Getting pwned by AI [13] | 1 |  |  |  |  |
| LLMs as Hackers [16] | 4 | 1 | 60 |  |  |
| Autonomously Hack Websites [10] | 50 web sites | 10 | 5 | 10 |  |
| Autonomously Exploit One-day Vulns. [9] | 10 | 5 |  |  |  |
| Exploit Zero-Day Vulnerabilities [11] | 3 | 5 |  |  |  |
| PenHeal [18] | 1 | 3 |  |  |  |
| AUTOPENBENCH [12] | 1 | 5 | 30/60 |  |  |
| HackSynth [29] | 8 | 20 |  |  |  |
| Vulnbot [24] | 3 | 5 | 15/24 |  |  |
| Multistage Network Attacks [38] | 3 | 5 |  |  |  |
| pentestGPT [7] | picoCTF, HTB | 3 |  |  |  |
| Can LLMs hack Enterprise Networks? [15] | 2 | 6 | 120 |  |  |
| Towards automated penetration testing [19] | 2 | 1 |  |  |  |
| AutoAttacker [44] | 4 | 3 |  |  |  |
| CyBench [47] | 8 | 15 |  |  |  |
| NYU CTF Dataset[36, 37] | 5 | 5 | 2880 |  |  |
| RapidPen [31] | 1 | 10 |  |  |  |
| AutoPT [42] | 3 | 5 | 15 |  |  |
| are included within metasploitable2, thus invalidating coverage | finding security misconfigurations or exploiting known vulnera- |  |  |  |  |
| metrics. Similarly, Happe et al. [15] utilize GOAD as an Active Di- | bilities is more relevant. Penetration-Testers in the field typically |  |  |  |  |
| rectory testbed containing 5 windows server VMs and 30 Active | fall into the security practitioner category. In addition, forensics |  |  |  |  |
| Directory users. There is no authoritative documentation detailing | is typically delegated to dedicated personnel that are not perform- |  |  |  |  |
| all vulnerabilities and attack paths within this testbed. Partial doc- | ing penetration testing. While CTF-based challenges mirror the |  |  |  |  |
| umentation | 7 | indicates the existence of dozens of potential attack | security field as a whole, they might not provide a good proxy for |  |  |
| paths which often have to be combined to enable further exploita- | penetration testing practices. |  |  |  |  |
| tion. Given this situation, the evaluation can only count the amount | Another mismatch are Assumed Breach scenarios, which are |  |  |  |  |
| of compromised systems and users, but cannot give an estimate of | commonly performed by security practitioners. In these scenarios, |  |  |  |  |
| achieved vulnerability coverage. | the attacker is already situated within the target environment and |  |  |  |  |

performs network-based attacks. They commonly have to combine

| Recommendation. | Ground the test-cases in reality by using “Top | singular low-level vulnerabilities into vulnerability chains to breach |
| --- | --- | --- |
| 10 lists” for broad guidance, but provide detailed information which | their targets. While CTF challenges’ atomic exercises simulate ex- |  |
| attack vectors were included within the testbed. | ploiting those low-level vulnerabilities, they often do not include |  |

those multi-step attack chains or limit the included attack-chains to

| 6.3 | Practitioners’ Work: Security vs. | a single target machine. In contrast, more network-oriented bench- |  |
| --- | --- | --- | --- |
| Pen-Testing Challenges | marks ([15, 38]) typically include multi-step scenarios spanning |  |  |
| Testbeds based upon CTF -Challenges [29, 37, 47] contain attack | multiple virtual machines. |  |  |
| vectors belonging to broad categories such as reversing, forensics or | All reviewed benchmarks were Jeopardy-style CTFs. Attacker |  |  |
| exploitation-writing challenges in addition to typical penetration- | / Defender style benchmarks would provide additional realism by |  |  |
| testing activities such as web exploitation. Recent empirical re- | including dynamism into the testbed, e.g., configuration changes, |  |  |
| search [14] into penetration testers’ tasks indicates a split between | active adversaries, stealthiness, detection engineering, and both |  |  |
| people working within the field of security: security researchers | implementing and dealing with countermeasures. Of the reviewed |  |  |
| and security practitioners. For the former, challenges such as revers- | testbeds, the network-based testbeds [15, 38] would be best suited |  |  |
| ing or exploit generation are highly relevant, while for the latter, | for extending into Attacker/Defender style testbeds. |  |  |
| 7 | https://orange-cyberdefense.github.io/GOAD/img/diagram-GOAD_ | Recommendation. | Analyze your audience and design your test- |
| compromission_Path_dark.png | cases accordingly. |  |  |

---

## Page 8

important in scenarios that emulate common real network vulner-

abilities as corporate networks often contain legacy protocols or

services. A potential solution would be to make all identifiers within

a benchmark parametrizable or randomized. This would allow each

benchmark instantiation to contain unique usernames, hostnames,

passwords, or file paths. In addition, benchmarks and their docu-

mentation should contain canaries that allow better detection if a

benchmark is included within an LLM’s training data.

Another issue is Goddhart’s law: “ when a measure becomes a

target, it ceases to be a good measure ” [6]. In the security domain

this is also related to the Red Queen’s race [3] as we have have

active adversaries. Every time a new Top 10 list of vulnerabilities

is published and defenders implement countermeasures for the re-

spective Top 10 items, attackers switch to additional attack vectors,

i.e., the attacks that just did not make it within the Top 10s. As

Recommendation. Make identifiers within the testbed parametriz-

able and include canaries in both your testbed and its documenta-

tion.

Human baselines are inherently not reproducible. In addition, auto-

mated tooling that depends upon human interactions, e.g., using

pentestGPT as a baseline, can incorporate this human randomness

in addition to the tooling-inherent randomness. Using LLM-guided

baselines introduces problems with reproducibility due to their

stochastic nature.

When using automation, choosing the right tooling is important:

ZAP is a web vulnerability scanner and should only be used for

benchmarks that consist primarily of web vulnerabilities. When

Recommendation. Implement a baseline and include it into your

testbed documentation. If the baseline is created through automated

tooling include enough configuration data to make the baseline

Andreas Happe and Jürgen Cito

Multi-Step Attack Chains. Common attacks in real-world net-

works consist of multiple causally-dependent steps. For example,

a user account must first be compromised using a network attack

before it is subsequently used to execute a sensitive operation. Real-

Life penetration-tests can commonly be described as complex attack

graphs where nodes indicate states and edges offensive steps. Both,

nodes being dependent upon multiple successful prior exploita-

tion steps, as well as redundant parallel steps leading to the same

compromised node, are common occurrences. To allow for better

analysis of singular attack steps, testbeds often simplify multi-step

attack chains into separate tests containing only a single attack

step. This does not allow to test for end-to-end security exploitation,

esp. does not allow testing LLMs for high-level strategizing and

planning.

the exploit can crash the target system. Synthetic testbeds, by their

nature, often ignore these probabilistic effects and the cascading

consequences of exploit-induced system instability.

Side-Effects in the Real-World. Many security-relevant operations

target system, the same system can subsequently not be used within

an attack-graph. Another example is the existence of an active ad-

versary, e.g., endpoint detection and response (EDR) software place

within network testbeds. Synthetic testbeds often do not accurately

model the consequence of such minute variations, and if these ac-

tive countermeasures are disabled to accommodate the simulation,

the intrinsic realism of the scenario is compromised. Without this

dynamic interplay, synthetic benchmarks risk misrepresenting the

true performance of automated attack strategies.

token or pass-the-hash attacks in enterprise networks. In a synthetic

benchmark, these time-based nuances are typically flattened or

entirely absent further distorting their real-world applicability.

| 6.4 | Training Data Contamination | 6.6 | Clean Test-Cases vs. Messy Real-Life |  |
| --- | --- | --- | --- | --- |
| Publicly available testbeds will be included within LLM training | Test-cases should be reproducible, i.e., subsequent executions should |  |  |  |
| data eventually. To prevent overfitting, multiple publications se- | provide stable results. This leads towards synthetic single-step |  |  |  |
| lected vulnerabilities that have a CVE publication date that is after | atomic test-cases that can be evaluated individually. While being |  |  |  |
| the tested LLM’s training cut-off date. This assumes that there is no | beneficial for benchmarking, this can negatively impact construct |  |  |  |
| research or exploit released prior to the publication of a CVE. This | validity. Sommer and Paxson note in “Outside the Closed World: |  |  |  |
| is—by definition—not the case for | 0days | , i.e., vulnerabilities that are | On Using Machine Learning for Network Intrusion Detection” [39], |  |
| actively exploited before a remediation is provided by defenders | that synthetic testing environments can lead to an oversimplified |  |  |  |
| within their public announcement as part of coordination disclo- | understanding of adversarial behavior as they typically fail to cap- |  |  |  |
| sure procedures. In addition, using a cut-off date prevents inclusion | ture the dynamic complexity and nuanced behaviors inherent in |  |  |  |
| of relevant older techniques in the benchmark, which is especially | real-world systems and networks. |  |  |  |
| these attacks now rise in prominence, the subsequent list of Top 10 | Exploits are often non-deterministic. | Synthetic testbeds often as- |  |  |
| items will contain those abused vulnerabilities and attackers again | sume attack steps to be deterministic. Real-life exploits are often |  |  |  |
| will switch to the items that are just outside of the Top 10. Using | stochastic, e.g., when exploiting the well-known | EternalBlue | 8 | Win- |
| historic training data thus might teach an LLM attack vectors that | dows vulnerability, the probability of a successful compromise is |  |  |  |
| are currently “out-of-style”. | inherently low and subject to variability; in some cases, executing |  |  |  |
| 6.5 | Reproducibility of Baselines | can evoke side-effects, e.g., if a non-deterministic exploit crashes the |  |  |
| used as a baseline, the utilized configuration should be documented. | Background noise and activity. | Another essential aspect of real- |  |  |
| For example, if ZAP is used in its autonomous | baseline scan mode | , by | world networks is the presence of concurrent background activities |  |
| default, execution is stopped after one minute, which does not pro- | that can be part of an attack graph. For example, periodic tasks are |  |  |  |
| vide sufficient test coverage. In addition, ZAP is highly dependent | often executed within server systems, or users periodically interact |  |  |  |
| upon its configured plugins and rule-sets, without stating those | in insecure ways with network services. These temporal patterns |  |  |  |
| explicitly, the generated baselines are not reproducible. | are critical when evaluating network-level attacks, e.g., | pass-the- |  |  |
| reproducible. | 8 | https://de.wikipedia.org/wiki/EternalBlue |  |  |

---

## Page 9

Benchmarking Practices in LLM-driven Offensive Security: Testbeds, Metrics, and Experiment Design

Table 6: Measures used within publications. We differentiate between baselines used: Human Baselines using humans to

perform the test-cases, LLM-Prototype used existing LLM-based prototypes to gather a baseline while Trad. Tooling used existing

automated penetration-testing tooling for generating a baseline. We note the tools used, which were typically the ZAP Attack

Proxy (Z) or Metasploit (M). We note if the the benchmarks capture binary Success Rates (“test-case successful yes/no”) or offer

fine-grained Progression Rates (“test-case 60% completed”). The columns Tokens and Costs denote if the resulting test-run costs

were given as token counts or as amount of US$. We note if metrics include information about the number of successfully

executed commands as well as the amount of errors occurred during command execution. Finally, we indicate if the respective

publication provided a classification of executed commands or encountered errors.

| Publication | Human Baseline | LLM-Prototype | Trad. Tooling | Success Rate | Progression Rate | Tokens | Costs | Command Count | Invalid | Command Count | Command | Classification | Error Classification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Getting pwned by AI [13] | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| LLMs as Hackers [16] | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |
| Autonomously Hack Websites [10] | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| Autonomously Exploit One-day Vulns. [9] | Z, M | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |
| Exploit Zero-Day Vulnerabilities [11] | ✓ | Z, M | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |
| PenHeal [18] | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| AUTOPENBENCH [12] | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |
| HackSynth [29] | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |
| Vulnbot [24] | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |
| Multistage Network Attacks [38] | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |
| pentestGPT [7] | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |
| Can LLMs hack Enterprise Networks? [15] | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |
| Towards automated penetration testing [19] | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |
| AutoAttacker [44] | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| CyBench [47] | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| NYU CTF Dataset[36, 37] | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| RapidPen [31] | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| AutoPT [42] | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| Recommendation. | Emulate real-life problems even if they are | the | cme | command while the LLM uses its newer | nxc | version, it |  |  |  |  |  |  |  |
| messy. Implement multi-step attack chains that emulate common | might not be detected as successful sub-task completion. |  |  |  |  |  |  |  |  |  |  |  |  |
| attack trees. | CyBench [47] provides an optional subtask tracking mode, called |  |  |  |  |  |  |  |  |  |  |  |  |

subtask-guided performance . For each task a list of questions is

defined, e.g., “ which files contain the account credentials ”? During

execution, the attack prototype and its included LLM are tasked

| 6.7 | Progress Tracking through Sub-Tasks | with answering the current relevant question. If it provides a correct |
| --- | --- | --- |
| Command- or milestone-based progress tracking implicitly assumes | answer, the attack prototype is assumed to have progressed to the |  |
| that progress within penetration-testing can be linearized. Modern | next sub-task and is subsequently asked with the next relevant |  |
| attack methodologies are moving away from waterfall-like models | question. This is an implicit guidance mechanism and inherently |  |
| towards iterative approaches [27]. Due to their complex interac- | alters the analyzed model’s performance. |  |

tions, real-life attacks are often visualized through attack-trees [35]

and attack graphs [25], which incorporate parallel execution and

| dependencies between attack stages. | Recommendation. | We encourage using sub-tasks to allow for |
| --- | --- | --- |
| When using golden steps, an implicit assumption is that com- | fine-grained analysis of traces. If you implement sub-tasks, devise |  |
| mands and tools used during penetration-testing are known before | means of automatic detection if a subtask has been achieved. We |  |
| the experiment occurs as they need to be stated within the golden | recommend to define sub-tasks through their expected result and |  |
| steps. This assumption might not hold, i.e., attack tools evolve over | not through invoked tool-calls. Detail which preconditions must |  |
| time, and newer LLMs learn those new tools through their training | be fulfilled to make execution of a sub-task viable, as well as which |  |
| data. This can become problematic, e.g., if a golden step refers to | other sub-tasks become viable after a subtask has been achieved. |  |

---

## Page 10

Table 7: Summary of our Recommendations

Chapter Recommendation

6.3: Practitioners’ Work

6.4: Training Data Contamination Randomize identifier and include Canaries.

6.6: Clean Test-Cases vs. Messy Life Emulate real-life problems.

If provided, use baselines for comparison.

6.10: Metrics and Analysis

Overview executed commands and their errors.

easy availability (the initial Llama model was released in February

be cloud-hosted. If suitable, use a model from the OpenAI family

to allow for easy comparison with other publications. If an SLM

is not reasonable for the task, use at least one open-weight LLM

Andreas Happe and Jürgen Cito

Consider your audience and create relevant test-cases.

If feasible, use at least one OpenAI LLM to allow for comparison with existing research.

State your LLM’s requirements and detail their configuration, e.g., temperature.

Measure success rates, token utilization and occurred costs.

Perform qualitative analysis of trajectories and include your methodology.

binary success rates. A third of the publications used sub-tasks

involve time-consuming manual qualitative analysis. If feasible,

REFERENCES

[1] Manish Bhatt, Sahana Chennabasappa, Cyrus Nikolaidis, Shengye Wan, Ivan

[2] Manish Bhatt, Sahana Chennabasappa, Yue Li, Cyrus Nikolaidis, Daniel Song,

Kapil, et al. Cyberseceval 2: A wide-ranging cybersecurity evaluation suite for

[3] Steve Blank. The red queen problem, innovation in the dod and intelligence

gent software testing: A comparative study. In Proceedings of the 7th International

10.1145/3659677.3659749. URL https://doi.org/10.1145/3659677.3659749.

| 6.1: Technology Choices | Evaluate technology choices esp. for safety and security implications. |  |  |  |
| --- | --- | --- | --- | --- |
| 6.2: Benchmark Composition | Ground the benchmark in reality and provide information about included vulnerabilities. |  |  |  |
| 6.5: Baselines | Provide baselines derived from humans or automated tooling (include configuration). |  |  |  |
| 6.7: Tracking Sub-Tasks | Use Sub-Tasks for fine-grained analysis and allow for automated task completion detection. |  |  |  |
| 6.8: LLM Selection | Run at least one SotA LLM, one open-weight LLM, and, if feasible a SLM. |  |  |  |
| 6.9: Experiment Design | Run at least 5 samples and set the limit of steps per sample to at least 32. |  |  |  |
| We suggest showing the potential interactions between subtasks, | 6.10 | Gathered Metrics and Analysis |  |  |
| e.g., through use of flow diagrams. | All reviewed publications measured their performance through |  |  |  |
| 6.8 | LLM Selection | to track the evaluated LLM’s progress through their respective |  |  |
| Given the prevalence of OpenAI’s non-reasoning LLMs within our | tasks. 10 out of the 18 evaluations used the occurring $-cost to |  |  |  |
| reviewed publications, using a model out of this family allows for | track their prototype’s efficiency, half of them additionally noted |  |  |  |
| easier comparison to existing results. Of the open-weight models, | their respective token utilization. All papers perform qualitative |  |  |  |
| the high-usage of Llama and Mistral models might be related to their | and quantitative analysis, typically a form of thematic analysis. |  |  |  |
| 2023). Newer models, such as the DeepSeek- or qwen-family of | Recommendation. | Include metrics for per-model and per-testcase |  |  |
| models, are beginning to be used by researchers. | success rates, as well as for token usage. To allow for long-term |  |  |  |
| The small amount of used reasoning-models within reviewed | comparison, we suggest providing the estimated costs in US$. In- |  |  |  |
| publications could be related to their relative novelty. OpenAI’s | clude an overview of executed command categories, frequently |  |  |  |
| o1-preview | was announced in September 2023, out of the 19 pub- | executed commands, and their error rates. We recommend the in- |  |  |
| lications, only 5 were initially published after the announcement. | clusion of qualitative analysis but cautiously suggest introducing |  |  |  |
| Of these, one paper was already using reasoning models while an | a qualitative methodology for these within papers. We would pre- |  |  |  |
| older publication [47] was updated to include reasoning models. | fer more advanced metrics but acknowledge that these typically |  |  |  |
| Recommendation. | Run at least one State-of-the-Art LLM and a | executed commands and their errors should be subject to a qualita- |  |  |
| locally-run Small Language Model (SLM) which, by definition, will | tive analysis. If the benchmark supports sub-tasks, these should be |  |  |  |
| also be an open-weight LLM. The state-of-the-art LLM will typically | analyzed for progression rates and potential dead-ends. |  |  |  |
| for testing. State your LLM requirements with regard to reasoning- | Evtimov, Dominik Gabi, Daniel Song, Faizan Ahmad, Cornelius Aschermann, |  |  |  |
| capabilities, tool/function calling, structured output, and minimally | Lorenzo Fontana, et al. Purple llama cyberseceval: A secure coding benchmark |  |  |  |
| required context size. State your chosen LLM configuration, e.g., | for language models. | arXiv preprint arXiv:2312.04724 | , 2023. |  |
| the configured LLM temperature. | Shengye Wan, Faizan Ahmad, Cornelius Aschermann, Yaohui Chen, Dhaval |  |  |  |
| 6.9 | Experiment Run Configuration | large language models. | arXiv preprint arXiv:2404.13161 | , 2024. |
| Based on the averages gathered from the reviewed publications, | community. | SteveBlank (blog), October | , 17, 2017. |  |
| we recommend performing at least 5 test-runs/samples per LLM | [4] | Mohamed Boukhlif, Nassim Kharmoum, and Mohamed Hanine. Llms for intelli- |  |  |
| with a maximum that’s at least 32 steps. We encourage creating | Conference on Networking, Intelligent Systems and Security | , NISS ’24, New York, |  |  |
| both human and automated baselines and recommend including | NY, USA, 2024. Association for Computing Machinery. ISBN 9798400709296. doi: |  |  |  |
| extensive configuration information when automated tools are used | [5] | Virginia Braun and Victoria Clarke. | Using thematic analysis in psychology. |  |
| for their creation (Section 6.5). | Qualitative research in psychology | , 3(2):77–101, 2006. |  |  |

---

## Page 11

Benchmarking Practices in LLM-driven Offensive Security: Testbeds, Metrics, and Experiment Design

| [6] | K Alec Chrystal, Paul D Mizen, and PD Mizen. | Goodhart’s law: its origins, | [31] | Sho Nakatani. Rapidpen: Fully automated ip-to-shell penetration testing with |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| meaning and implications for monetary policy. | Central banking, monetary theory | llm-based agents, 2025. URL https://arxiv.org/abs/2502.16730. |  |  |  |  |
| and practice: Essays in honour of Charles Goodhart | , 1:221–243, 2003. | [32] | Lorelli S Nowell, Jill M Norris, Deborah E White, and Nancy J Moules. Thematic |  |  |  |
| [7] | Gelei Deng, Yi Liu, Víctor Mayoral-Vilches, Peng Liu, Yuekang Li, Yuan Xu, Tian- | analysis: Striving to meet the trustworthiness criteria. | International journal of |  |  |  |
| wei Zhang, Yang Liu, Martin Pinzger, and Stefan Rass. | 𝑃𝑒𝑛𝑡𝑒𝑠𝑡𝐺𝑃𝑇 | : Evaluating | qualitative methods | , 16(1):1609406917733847, 2017. |  |  |
| and harnessing large language models for automated penetration testing. In | [33] | Collin Robson. Real world research, 2002. |  |  |  |  |
| 33rd USENIX Security Symposium (USENIX Security 24) | , pages 847–864, 2024. | [34] | Karen A. Scarfone, Murugiah P. Souppaya, Amanda Cody, and Angela D. Ore- |  |  |  |
| [8] | Rohit Dube. Large language models in information security research: A january | baugh. Sp 800-115. technical guide to information security testing and assessment. |  |  |  |  |
| 2024 survey. | ResearchGate preprint RG | , 2(20107.26404), 2024. | Technical report, Gaithersburg, MD, USA, 2008. |  |  |  |
| [9] | Richard Fang, Rohan Bindu, Akul Gupta, and Daniel Kang. | Llm agents can | [35] | Bruce Schneier. Attack trees. | Dr. Dobb’s journal | , 24(12):21–29, 1999. |
| autonomously exploit one-day vulnerabilities, 2024. URL https://arxiv.org/abs/ | [36] | Minghao Shao, Boyuan Chen, Sofija Jancheska, Brendan Dolan-Gavitt, Siddharth |  |  |  |  |
| 2404.08144. | Garg, Ramesh Karri, and Muhammad Shafique. An empirical evaluation of llms |  |  |  |  |  |
| [10] | Richard Fang, Rohan Bindu, Akul Gupta, Qiusi Zhan, and Daniel Kang. Llm agents | for solving offensive security challenges, 2024. URL https://arxiv.org/abs/2402. |  |  |  |  |
| can autonomously hack websites, 2024. URL https://arxiv.org/abs/2402.06664. | 11814. |  |  |  |  |  |
| [11] | Richard Fang, Rohan Bindu, Akul Gupta, Qiusi Zhan, and Daniel Kang. Teams | [37] | Minghao Shao, Sofija Jancheska, Meet Udeshi, Brendan Dolan-Gavitt, Haoran |  |  |  |
| of llm agents can exploit zero-day vulnerabilities, 2024. URL https://arxiv.org/ | Xi, Kimberly Milner, Boyuan Chen, Max Yin, Siddharth Garg, Prashanth Krish- |  |  |  |  |  |
| abs/2406.01637. | namurthy, Farshad Khorrami, Ramesh Karri, and Muhammad Shafique. Nyu |  |  |  |  |  |
| [12] | Luca Gioacchini, Marco Mellia, Idilio Drago, Alexander Delsanto, Giuseppe | ctf dataset: A scalable open-source benchmark dataset for evaluating llms in |  |  |  |  |
| Siracusano, and Roberto Bifulco. | Autopenbench: Benchmarking generative | offensive security, 2024. URL https://arxiv.org/abs/2406.05590. |  |  |  |  |
| agents for penetration testing, 2024. URL https://arxiv.org/abs/2410.03225. | [38] | Brian Singer, Keane Lucas, Lakshmi Adiga, Meghna Jain, Lujo Bauer, and Vyas |  |  |  |  |
| [13] | Andreas Happe and Jürgen Cito. | Getting pwn’d by ai: Penetration testing | Sekar. On the feasibility of using llms to execute multistage network attacks. |  |  |  |
| with large language models. | In | Proceedings of the 31st ACM Joint European | arXiv preprint arXiv:2501.16466 | , 2025. |  |  |
| Software Engineering Conference and Symposium on the Foundations of Software | [39] | Robin Sommer and Vern Paxson. Outside the closed world: On using machine |  |  |  |  |
| Engineering | , pages 2082–2086, 2023. | learning for network intrusion detection. In | 2010 IEEE symposium on security |  |  |  |
| [14] | Andreas Happe and Jürgen Cito. Understanding hackers’ work: An empirical | and privacy | , pages 305–316. IEEE, 2010. |  |  |  |
| study of offensive security practitioners. In | Proceedings of the 31st ACM Joint | [40] | Niek Jan van den Hout. Standardised penetration testing? examining the useful- |  |  |  |
| European Software Engineering Conference and Symposium on the Foundations of | ness of current penetration testing methodologies. | Examining the usefulness of |  |  |  |  |
| Software Engineering | , pages 1669–1680, 2023. | current penetration testing methodologies | , 2019. |  |  |  |
| [15] | Andreas Happe and Jürgen Cito. Can llms hack enterprise networks? autonomous | [41] | Shengye Wan, Cyrus Nikolaidis, Daniel Song, David Molnar, James Crnkovich, |  |  |  |
| assumed breach penetration-testing active directory networks. | arXiv preprint | Jayson Grace, Manish Bhatt, Sahana Chennabasappa, Spencer Whitman, |  |  |  |  |
| arXiv:2502.04227 | , 2025. | Stephanie Ding, et al. Cyberseceval 3: Advancing the evaluation of cybersecurity |  |  |  |  |
| [16] | Andreas Happe, Aaron Kaplan, and Juergen Cito. Llms as hackers: Autonomous | risks and capabilities in large language models. | arXiv preprint arXiv:2408.01605 | , |  |  |
| linux privilege escalation attacks. | arXiv preprint arXiv:2310.11409 | , 2024. | 2024. |  |  |  |
| [17] | Mohammed Hassanin and Nour Moustafa. A comprehensive overview of large | [42] | Benlong Wu, Guoqiang Chen, Kejiang Chen, Xiuwei Shang, Jiapeng Han, Yanru |  |  |  |
| language models (llms) for cyber defences: Opportunities and directions, 2024. | He, Weiming Zhang, and Nenghai Yu. Autopt: How far are we from the end2end |  |  |  |  |  |
| URL https://arxiv.org/abs/2405.14487. | automated web penetration testing?, 2024. URL https://arxiv.org/abs/2411.01236. |  |  |  |  |  |
| [18] | Junjie Huang and Quanyan Zhu. Penheal: a two-stage llm framework for auto- | [43] | Hanxiang Xu, Shenao Wang, Ningke Li, Kailong Wang, Yanjie Zhao, Kai Chen, |  |  |  |
| mated pentesting and optimal remediation. In | Proceedings of the Workshop on | Ting Yu, Yang Liu, and Haoyu Wang. Large language models for cyber security: |  |  |  |  |
| Autonomous Cybersecurity | , pages 11–22, 2023. | A systematic literature review, 2024. URL https://arxiv.org/abs/2405.04760. |  |  |  |  |
| [19] | Isamu Isozaki, Manil Shrestha, Rick Console, and Edward Kim. Towards auto- | [44] | Jiacen Xu, Jack W Stokes, Geoff McDonald, Xuesong Bai, David Marshall, Siyue |  |  |  |
| mated penetration testing: Introducing llm benchmark, analysis, and improve- | Wang, Adith Swaminathan, and Zhou Li. | Autoattacker: A large language |  |  |  |  |
| ments. | arXiv preprint arXiv:2410.17141 | , 2024. | model guided system to implement automatic cyber-attacks. | arXiv preprint |  |  |
| [20] | Valerie J Janesick. Peer debriefing. | The Blackwell encyclopedia of sociology | , 2007. | arXiv:2403.01038 | , 2024. |  |
| [21] | Haolin Jin, Linghan Huang, Haipeng Cai, Jun Yan, Bo Li, and Huaming Chen. | [45] | Yifan Yao, Jinhao Duan, Kaidi Xu, Yuanfang Cai, Zhibo Sun, and Yue Zhang. A |  |  |  |
| From llms to llm-based agents for software engineering: A survey of current, | survey on large language model (llm) security and privacy: The good, the bad, |  |  |  |  |  |
| challenges and future, 2024. URL https://arxiv.org/abs/2408.02479. | and the ugly. | High-Confidence Computing | , 4(2):100211, 2024. ISSN 2667-2952. |  |  |  |
| [22] | Zack Kaplan, Ning Zhang, and Stephen V Cole. A capture the flag (ctf) platform | doi: https://doi.org/10.1016/j.hcc.2024.100211. URL https://www.sciencedirect. |  |  |  |  |
| and exercises for an intro to computer security class. In | Proceedings of the 27th | com/science/article/pii/S266729522400014X. |  |  |  |  |
| ACM Conference on on Innovation and Technology in Computer Science Education | [46] | Yagmur Yigit, William J Buchanan, Madjid G Tehrani, and Leandros Maglaras. |  |  |  |  |
| Vol. 2 | , pages 597–598, 2022. | Review of generative ai methods in cybersecurity, 2024. URL https://arxiv.org/ |  |  |  |  |
| [23] | Stylianos Karagiannis, Elpidoforos Maragkos-Belmpas, and Emmanouil Magkos. | abs/2403.08701. |  |  |  |  |
| An analysis and evaluation of open source capture the flag platforms as cy- | [47] | Andy K Zhang, Neil Perry, Riya Dulepet, Joey Ji, Justin W Lin, Eliot Jones, Celeste |  |  |  |  |
| bersecurity e-learning tools. In | IFIP World Conference on Information Security | Menders, Gashon Hussein, Samantha Liu, Donovan Jasper, et al. Cybench: A |  |  |  |  |
| Education | , pages 61–77. Springer, 2020. | framework for evaluating cybersecurity capabilities and risks of language models. |  |  |  |  |
| [24] | He Kong, Die Hu, Jingguo Ge, Liangxiong Li, Tong Li, and Bingzhen Wu. Vulnbot: | arXiv preprint arXiv:2408.08926 | , 2024. |  |  |  |
| Autonomous penetration testing for a multi-agent collaborative framework. | [48] | Jie Zhang, Haoyu Bu, Hui Wen, Yu Chen, Lun Li, and Hongsong Zhu. When |  |  |  |  |
| arXiv preprint arXiv:2501.13411 | , 2025. | llms meet cybersecurity: A systematic literature review, 2024. URL https://arxiv. |  |  |  |  |
| [25] | Harjinder Singh Lallie, Kurt Debattista, and Jay Bal. A review of attack graph | org/abs/2405.03644. |  |  |  |  |

and attack tree visual syntax in cyber security. Computer Science Review , 35:

100219, 2020. ISSN 1574-0137. doi: https://doi.org/10.1016/j.cosrev.2019.100219.

URL https://www.sciencedirect.com/science/article/pii/S1574013719300772.

[26] Harindra S. Mavikumbure, Victor Cobilean, Chathurika S. Wickramasinghe,

Devin Drake, and Milos Manic. Generative ai in cyber security of cyber physical

systems: Benefits and threats. In 2024 16th International Conference on Human

System Interaction (HSI) , pages 1–8, 2024. doi: 10.1109/HSI61632.2024.10613562.

[27] Jose David Mireles, Jin-Hee Cho, and Shouhuai Xu. Extracting attack narratives

from traffic datasets. In 2016 International Conference on Cyber Conflict (CyCon

U.S.) , pages 1–6, 2016. doi: 10.1109/CYCONUS.2016.7836624.

[28] Farzad Nourmohammadzadeh Motlagh, Mehrdad Hajizadeh, Mehryar Majd,

Pejman Najafi, Feng Cheng, and Christoph Meinel. Large language models in

cybersecurity: State-of-the-art, 2024. URL https://arxiv.org/abs/2402.00891.

[29] Lajos Muzsai, David Imolai, and András Lukács. Hacksynth: Llm agent and

evaluation framework for autonomous penetration testing, 2024. URL https:

//arxiv.org/abs/2412.01778.

[30] Nitin Naik, Paul Jenkins, Paul Grace, and Jingping Song. Comparing attack

models for it systems: Lockheed martin’s cyber kill chain, mitre att&ck frame-

work and diamond model. In 2022 IEEE International Symposium on Systems

Engineering (ISSE) , pages 1–7, 2022. doi: 10.1109/ISSE54508.2022.10005490.

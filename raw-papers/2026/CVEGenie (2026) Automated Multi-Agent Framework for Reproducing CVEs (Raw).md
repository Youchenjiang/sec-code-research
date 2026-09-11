---
title: "From CVE Entries to Verifiable Exploits: An Automated Multi-Agent Framework for Reproducing CVEs"
author: "Saad Ullah; Praneeth Balasubramanian; Wenbo Guo; Amanda Burnett; Hammond Pearce; Christopher Kruegel; Giovanni Vigna; Gianluca Stringhini"
creator: "arXiv GenPDF (tex2pdf:57610bf)"
pages: 23
---

# From CVE Entries to Verifiable Exploits: An Automated Multi-Agent Framework for Reproducing CVEs

> **作者**：Saad Ullah; Praneeth Balasubramanian; Wenbo Guo; Amanda Burnett; Hammond Pearce; Christopher Kruegel; Giovanni Vigna; Gianluca Stringhini
> **總頁數**：23 頁

---

## Page 1

From CVE Entries to Verifiable Exploits:

An Automated Multi-Agent Framework for Reproducing CVEs

∗

praneeth@ucsb.edu

unsw.edu.au

Abstract

High-quality datasets of real-world vulnerabilities and their

corresponding verifiable exploits are crucial resources in soft-

their creation demands intensive manual effort and deep secu-

rity expertise. In this paper, we present CVE-G ENIE , an auto-

work designed to reproduce real-world vulnerabilities, pro-

vided in Common Vulnerabilities and Exposures (CVE) for-

mat, to enable creation of high-quality vulnerability datasets.

Given a CVE entry as input, CVE-G ENIE gathers the rel-

evant resources of the CVE, automatically reconstructs the

vulnerable environment, and (re)produces a verifiable exploit.

Our systematic evaluation highlights the efficiency and robust-

ness of CVE-G ENIE ’s design and successfully reproduces

approximately 51% (428 of 841) CVEs published in 2024-

2025, complete with their verifiable exploits, at an average

cost of $2.77 per CVE. Our pipeline offers a robust method to

generate reproducible CVE benchmarks, valuable for diverse

applications such as fuzzer evaluation, vulnerability patching,

and assessing AI’s security capabilities.

every year, with more than 40,000 vulnerabilities tracked

CVE ID

Vuln Project Setup

Exploit for Vuln

C VE-G enie

Developing effective automated vulnerability detection

techniques depends on high-quality datasets with reliable

ground truth, as low-quality data can lead to unreliable eval-

uations [51] and to learn spurious correlations, especially in

machine learning (ML) based approaches [4, 49]. Although

public repositories, such as the NVD, include hundreds of

thousands of CVEs, they often lack critical details, including

vulnerable code, environment setup, working exploits, and

validation steps, which are all required to effectively repro-

duce a vulnerability and to build ground truth datasets for re-

search [38]. This is because the main purpose of vulnerability

advisories is to alert system administrators about software that

needs to be updated, and concrete exploit code is often kept

confidential for ethical reasons. Unfortunately, generating this

requires significant expertise, e.g., Mu et al. [38] spent over

memory vulnerabilities in Linux.

mated data collection helps address some of these limitations,

1

| Saad Ullah | Praneeth | Wenbo Guo | Amanda Burnett |
| --- | --- | --- | --- |
| Boston University | Balasubramanian | UC Santa Barbara | Arizona State University |
| saadu@bu.edu | UC Santa Barbara | henrygwb@ucsb.edu | aburne22@asu.edu |
| Hammond Pearce | Christopher Kruegel | Giovanni Vigna | Gianluca Stringhini |
| UNSW Sydney | UC Santa Barbara | UC Santa Barbara | Boston University |
| hammond.pearce@ | chris@cs.ucsb.edu | vigna@cs.ucsb.edu | gian@bu.edu |
| ware security research. Yet such resources remain scarce, as | Verifier for Exploit |  |  |
| mated, large language model (LLM)-based multi-agent frame- | Figure 1: CVE-G | ENIE | Overview. |
| 1 | Introduction | missing information from CVEs alone is labor-intensive and |  |
| arXiv:2509.01835v2 [cs.CR] 12 Feb 2026 | Tens of thousands of software vulnerabilities are discovered | 3,600 hours with 43 security expertise to reproduce only 368 |  |
| by the National Vulnerability Database (NVD) [42] in 2025 | To address these challenges, the security community has |  |  |
| alone. Many of these vulnerabilities are cataloged using the | adopted several approaches: manual annotation [21, 65], in- |  |  |
| CVE format, which provides a standardized identification | serting bugs into real-world code [36,41], and heuristic-based |  |  |
| system to help organizations address security flaws in both | mining [7, 10, 13, 15, 40]. While these methods have advanced |  |  |
| software and hardware. Still, existing vulnerability detection | the field, they come with limitations, such as limited support |  |  |
| tools, such as those listed by OWASP [44], struggle to keep up | for software and Common Weakness Enumerations (CWE) |  |  |
| with the increasing volume of code released each year. As a | categories, mislabeled vulnerabilities [50], and data becom- |  |  |
| result, many vulnerabilities remain undiscovered in codebases | ing stale. For instance, the DARPA Cyber Grand Challenge |  |  |
| for years (e.g., up to 2 years in Chromium and 7 years in | dataset from 2016 [11] quickly became outdated due to its |  |  |
| OpenSSL [3]) posing significant security risks. | small size and low-complexity bugs [20]. Meanwhile, auto- |  |  |
| ∗ | Corresponding author | but often tends to be limited in scope, e.g., ARVO [34] auto- |  |

*[Image: Page 1 Image]*

---

## Page 2

matically curates reproducible builds with triggering inputs

from OSS-Fuzz reports, but its scope is limited to memory

corruption bugs in C/C++. This highlights a clear need for

and realistic benchmarks for the security community.

LLM-driven, multi-agent framework for end-to-end CVE

reproduction. CVE-G ENIE instantiates what we define as

key properties of an ideal CVE reproduction system, cap-

tured by the acronym EAGER . Specifically, an ideal system:

Generates working Exploit/proof-of-concept (PoC); Builds

Assessors/verifiers for the exploit; Generalizes across CWEs,

languages, and project types; Is End-to-end automated; and

Rebuilds vulnerable environments. Specifically, this paper

makes the following contributions:

2

| SecLLMHolmes [54] Manual | ◗ | 4 | 8 | 3 |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| VulChecker [36] | Manual | ● | n/a | 5 | 2 |  |
| Draper [52] | SA tool | ◗ | n/a | 9 | 2 | ✓ ✗ ✗ ✗ |
| CVEfixes [7] | Patch diff | ❍ | 1,754 | 180 | 30 |  |
| ARVO [34] | OSS-Fuzz | ❍ | 273 | 4 | 2 |  |
| CVE-Bench [66] | Public CVEs | ❍ | 36 | 8 | 6 | ✗ ✓ ✓ ✓ |
| CVE-G | ENIE | Public CVEs | ❍ | 267 | 141 | 22 |

Table 1: Overview of vulnerability benchmark datasets. Real:

synthetic ● , real-world ❍ , mixed ◗ . CVE-G ENIE results

reflect CVEs from Jun 2024–May 2025.

2 Background and Related Work

2.1 Existing Benchmarks and Limitations

| a dataset curation method that enables fully reproducible | Name | Source | Real | # Projects | # CWEs | # Lang | Automated | Reproducible | PoC | Verifier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vulnerability instances across a wide range of software | SARD [41] | Manual | ● | ~120 | ~150 | 6 | ✗ ✓ ✓ ✗ |  |  |  |
| and vulnerability types | . | SVEN [21] | Manual | ❍ | n/a | 9 | 3 | ✗ ✗ ✗ ✗ |  |  |
| Recently, LLMs have demonstrated remarkable capabil- | Devign [65] | Manual | ❍ | 4 | n/a | 2 | ✗ ✗ ✗ ✗ |  |  |  |
| ities in solving complex software engineering (SWE) and | ✗ ✗ ✗ ✗ |  |  |  |  |  |  |  |  |  |
| security tasks, ranging from automated bug detection [16, 39] | ✓ ✗ ✗ ✗ |  |  |  |  |  |  |  |  |  |
| and repair [24, 46, 57], to writing fuzzer test harnesses [12]. | D2A [64] | SA tool | ❍ | 6 | 7 | 2 | ✓ ✗ ✗ ✗ |  |  |  |
| Moreover, the shift to agentic workflows [8, 32, 62, 63], in | VUDENC [56] | Sec. issue | ❍ | 812 | 7 | 1 | ✓ ✗ ✗ ✗ |  |  |  |
| which LLM-powered agents are provided access to real- | DiverseVul [10] | Sec. issue | ❍ | 797 | 150 | 12 | ✓ ✗ ✗ ✗ |  |  |  |
| world tools [1], has further pushed the capabilities of general- | PrimeVul [13] | Patch diff | ❍ | 755 | 140 | 2 | ✓ ✗ ✗ ✗ |  |  |  |
| purpose LLMs and led to significant performance gains on | BigVul [15] | Patch diff | ❍ | 348 | 91 | 2 | ✓ ✗ ✗ ✗ |  |  |  |
| extremely difficult real-world SWE-related benchmarks, such | CrossVul [40] | Patch diff | ❍ | 1,675 | 168 | 40 | ✓ ✗ ✗ ✗ |  |  |  |
| as SWE-bench [25]. This raises the question of whether LLM | ✓ ✗ ✗ ✗ |  |  |  |  |  |  |  |  |  |
| agents could also be useful in automatically setting up and re- | ✓ ✓ ✓ ✗ |  |  |  |  |  |  |  |  |  |
| producing existing CVEs, allowing us to build reliable, large, | Mu | et al. | [38] | Public CVEs | ❍ | 1 | 4 | 1 | ✗ ✓ ✓ ✓ |  |
| In this paper, we present CVE-G | ENIE | , a fully-automated, | ✓ ✓ ✓ ✓ |  |  |  |  |  |  |  |
| 1. We develop CVE-G | ENIE | , an automated end-to-end CVE | To evaluate various vulnerability detection techniques (rule- |  |  |  |  |  |  |  |
| reproduction pipeline that extracts CVE data (e.g., soft- | based methods [44, 58], ML-approaches [29–31, 36], and |  |  |  |  |  |  |  |  |  |
| ware vulnerable version source code, advisories, patches, | LLM-based systems [17–19, 47]), the community needs stan- |  |  |  |  |  |  |  |  |  |
| cwes, etc.), rebuilds the vulnerable environment, and gen- | dardized benchmarks. Prior work has explored four main ap- |  |  |  |  |  |  |  |  |  |
| erates exploits and verifiers to assess the reproduction. | proaches for addressing these challenges. (1) | Manual efforts |  |  |  |  |  |  |  |  |
| 2. We design CVE-G | ENIE | to demonstrate | compositional | involve analyzing [21] or reproducing [66] vulnerabilities |  |  |  |  |  |  |
| intelligence | by a novel architecture, systematically se- | in real-world code, or crafting synthetic examples [54], but |  |  |  |  |  |  |  |  |
| lected LLMs and prompts, and reliable EAGER-style | datasets are small, lack ecological validity, and often suffer |  |  |  |  |  |  |  |  |  |
| CVE reproduction. As a result, CVE-G | ENIE | achieves | labeling errors due to human mistakes (e.g., 50% data in |  |  |  |  |  |  |  |
| strong performance across diverse CVEs, vulnerability | Devign [65] have wrong labels [50]). (2) Automated label- |  |  |  |  |  |  |  |  |  |
| types, programming languages, and projects, even when | ing using | static analysis (SA) tools | , such as bandit [6] or |  |  |  |  |  |  |  |
| CVE information is incomplete. | infer [23], reduces manual effort but introduces many false |  |  |  |  |  |  |  |  |  |
| 3. We systematically evaluate CVE-G | ENIE | ’s architecture | positives [48,64]. (3) Mining | real-world data | , such as | GitHub |  |  |  |  |
| and demonstrate that each component is essential for | issues | or CVE | patch commits | , assumes that all removed or |  |  |  |  |  |  |
| optimal performance. Notably, even advanced LLMs like | modified code is vulnerable; However, this assumption often |  |  |  |  |  |  |  |  |  |
| o3 | , when used standalone, are incapable of performing | leads to mislabeled samples, as Risse | et al. | [50] highlighted |  |  |  |  |  |  |
| EAGER-style reproduction for even a single CVE. | for DiverseVul [10] and BigVul [15]. (4) Relying on | proven |  |  |  |  |  |  |  |  |
| 4. We ran CVE-G | ENIE | on 841 CVEs (published between | sources | , such as | OSS-Fuzz | , offers verified exploits and san- |  |  |  |  |
| June 2024 and May 2025) and successfully reproduced | itizer feedback; However, these are restricted to certain bug |  |  |  |  |  |  |  |  |  |
| 428 CVEs across 267 projects, 141 CWEs, and 22 pro- | types, primarily memory corruption in C/C++, and do not |  |  |  |  |  |  |  |  |  |
| gramming languages, highlighting our generalizability. | generalize across languages or vulnerability classes [34]. |  |  |  |  |  |  |  |  |  |
| 5. We make our framework, source code, datasets of repro- | Besides data quality, existing datasets also lack necessary |  |  |  |  |  |  |  |  |  |
| duced CVEs, and full logs of agent interactions publicly | artifacts for dynamic evaluation beyond static labels [4,49,54], |  |  |  |  |  |  |  |  |  |
| available, providing an ongoing valuable contribution | including dynamic execution environments and reproducible |  |  |  |  |  |  |  |  |  |
| for downstream research tasks (see Appendix C and F). | exploits, which is difficult to obtain [38]. Table 1 provides an |  |  |  |  |  |  |  |  |  |

---

## Page 3

Method Exploit Assess General E2E Rebuild LLM agents are systems that combine LLMs with tools.

| Fuzzers | ✓ | ✗ | ✗ | ✗ | ✗ |
| --- | --- | --- | --- | --- | --- |
| Metasploit [35] | ✓ | ✗ | ✗ | ✗ | ✗ |
| ✓ | ✗ | ✗ | ✓ | ✓ |  |
| ✓ | ✓ | ✓ | ✓ | ✓ |  |

2.2 Call for EAGER Style for CVE Reproduc-

curity vulnerabilities in real-world software. Each CVE ID

corresponds to a CVE entry that includes key details for

that CVE, such as vulnerability description, source code, af-

fected versions, security advisories, CWE classifications, and

2.3 Large Language Models and Agents

LLMs are transformer-based neural network models with

security tasks, e.g., bug detection and repair [24, 46, 57] and

3

They can finish complex tasks via a sequence of actions, in-

45,53]. An agentic system can have multiple agents, each with

and tool sets. In security, researchers have started to con-

responsible for fault localization, patch generation, and valida-

tion (e.g., PatchPilot [28], and PatchAgent [61]). Through the

agentic-based systems with end-to-end capabilities for vulner-

ability detection and patching [18]. These recent successes

provide the argument for using LLM agents in vulnerability

framework.

3 CVE-G ENIE

and sub-modules handled by specialized agents with

systematically engineered prompts, providing the most

suitable architecture for end-to-end CVE reproduction

(Section 4.2).

able (Section 4.3).

| Manual [32, 66] | ✓ | ✓ | ✗ | ✗ | ✓ | cluding planning, generation, and tool executions [22, 26, 27, |
| --- | --- | --- | --- | --- | --- | --- |
| ARVO [34] | a sub-task, such as reasoning, critiquing, generating, perceiv- |  |  |  |  |  |
| CVE-G | ENIE | ing, remembering, or teaching, as well as its own workflow |  |  |  |  |
| Table 2: Comparing Potential Vulnerability Reproduction | struct LLM agents to find and repair vulnerabilities. There are |  |  |  |  |  |
| Methods and their EAGER attributes. | multi-agent patching systems, where different sub-agents are |  |  |  |  |  |
| overview of the current state of vulnerability benchmarks. | recent DARPA AIxCC competition, researchers constructed |  |  |  |  |  |
| tion | analysis and software development, as well as for building |  |  |  |  |  |
| A | CVE ID | is a unique identifier for publicly disclosed se- | an EAGER-style automated end-to-end CVE reproduction |  |  |  |
| patches, enabling security professionals to assess and mitigate | We design CVE-G | ENIE | to exhibit | compositional intelligence | , |  |
| risks. Creating a dataset from the standard CVE database is a | i.e., the ability to solve complex tasks by decomposing them |  |  |  |  |  |
| promising way towards addressing the aforementioned chal- | into meaningful sub-tasks whose outputs are explicitly com- |  |  |  |  |  |
| lenges (see Appendix F). Therefore, we introduce EAGER, a | posed and verified to form a correct end-to-end solution. To |  |  |  |  |  |
| set of crucial criteria for ideal CVE reproduction: | this end, first, we design a novel architecture that decomposes |  |  |  |  |  |
| • | E | xploit Generation – (re)creation of an exploit or PoC | CVE understanding and reproduction into four interdepen- |  |  |  |
| that reliably triggers the vulnerability in the CVE. | dent modules: (1) the | Processor | (Section 3.1), which retrieves |  |  |  |
| • | A | ssessment – inclusion of a “verifier” or “sanitizer” ca- | source code and constructs a structured knowledge base; (2) |  |  |  |
| pable of assessing whether the generated exploit or PoC | the | Builder | (Section 3.2), which reconstructs the vulnerable |  |  |  |
| successfully triggers the vulnerability. | environment; (3) the | Exploiter | (Section 3.3), which repro- |  |  |  |
| • | G | eneralization – reproduction of CVEs across diverse | duces the exploit; and (4) the | CTF Verifier | (Section 3.4), |  |
| CWEs, programming languages, and software projects. | which generates a verifier for the exploit. Second, rather than |  |  |  |  |  |
| • | E | nd-to-end Automation – execution of all stages of CVE | relying on a single LLM or a fixed prompting strategy across |  |  |  |
| reproduction in a fully automated manner. | tasks, we systematically select the most suitable LLMs and |  |  |  |  |  |
| • | R | ebuild project – reconstruction of the original vulnera- | engineer task-specific prompts for each component of CVE- |  |  |  |
| ble environment to facilitate exploit/PoC execution. | G | ENIE | , resulting in an optimized end-to-end configuration |  |  |  |
| However, none of the existing methods satisfy all the criteria | (Section 3.5). Third, we bridge the gap identified in Section 2, |  |  |  |  |  |
| (see Table 2). For example, manual effort for producing EA- | namely the lack of any system capable of true EAGER-style |  |  |  |  |  |
| GER datasets does not scale and is not generalizable [38, 66]. | CVE reproduction, and ground CVE-G | ENIE | ’s design in the |  |  |  |
| ARVO [34] focuses solely on memory-related bugs from | following guiding principles: |  |  |  |  |  |
| OSS-Fuzz C/C++ projects, limiting its scope. In contrast, | 1. | Modular Task Decomposition: | LLMs struggle with |  |  |  |
| CVE-G | ENIE | is the only framework that satisfies all criteria | long, complex contexts [54] and tasks [25]. Thus, CVE- |  |  |  |
| of EAGER reproduction. | G | ENIE | decomposes reproduction into focused modules |  |  |  |
| billions of parameters. They have demonstrated remarkable | 2. | Robustness to Incomplete Data: | Since missing CVE |  |  |  |
| performance across various application domains, including | fields can lower reproduction success by up to 44% [38], |  |  |  |  |  |
| question answering [43], mathematical reasoning [2], and | CVE-G | ENIE | mitigates this by relying on patch or |  |  |  |
| code generation [5, 9]. Recent work also shows their utility in | source-code analysis when advisories/PoCs are unavail- |  |  |  |  |  |
| writing fuzzer test harnesses [12]. | 3. | Reliability through Self-Critique: | To counter LLMs’ |  |  |  |

---

## Page 4

| reasoning limits [54], each module uses paired | developer | LLMs localize the issue, understand its root cause [13,15,21], |  |  |
| --- | --- | --- | --- | --- |
| and | critic | agents in a ReAct-style loop [60], enabling it- | and generate effective exploits. (4) | Security advisories and |
| erative refinement and internal verification (Section 4.2). | PoC | : We filter URLs referenced in the CVE entry by keywords |  |  |
| Together, these principles elevate CVE-G | ENIE | beyond a | (e.g., “security”, “advisory”, “bounty”, etc.), and scrape their |  |
| fixed engineering pipeline and enable CVE-G | ENIE | to op- | contents. |  |
| erationalize | compositional intelligence | in a fully automated | Output. | The vulnerable version of a project’s source code |
| setting, yielding the first practical, generalizable, and end- | alongside its directory structure and CVE raw data. |  |  |  |

to-end framework for EAGER-style CVE reproduction (see

Appendix E for further details). The following subsections

detail the workings of each CVE-G ENIE component, using

3.1 Processor

3.1.1 Data Processor 1

1 to identify the project repository. For closed-source soft-

ware, Data Processor allows users to supply the repository

URL. Once the source code is located, it identifies affected

software configurations: vulnerable versions, platforms, or

Vulnerability Information Extraction. After the vulnerable ver-

sion of the project source code is downloaded, Data Processor

extracts the following four key pieces of information from

“cvelist”, if available: (1) CVE description : A high-level sum-

mary of the vulnerability in the target project. (2) CWE data :

CWE information, a categorization system for hardware and

software weaknesses that associates the CVE with a specific

vulnerability type, e.g., CWE-674 (Uncontrolled Recursion).

get source code that fix the vulnerability. These commits help

GitHub (https://github.com/CVEProject/cvelist)

4

3.1.2 Knowledge Builder 2

able for accurately reproducing the vulnerability. For instance,

CVE-2024-4340 has a PoC provided in its security advisory,

and the patch commit helps understand the root cause by high-

the vulnerability [7, 13, 21] and aids in crafting an effective

exploit. This knowledge base acts as the long-term memory

for agents, helping them to effectively reproduce CVEs, by

patch commits.

3.2 Builder

oper LLM agents: the Pre-Requisite Developer Agent , which

analyzes and plans the environment setup, and the Setup De-

veloper Agent , which executes this plan to configure the vul-

nerable environment. As well as one critic , the Setup Critic

Agent , which analyzes the logs of the Setup Developer and

evaluates the setup for the project, allowing the system to

correct its mistakes. Below, we discuss these in detail.

We introduce this agent as an initial exploration and planning

done for three key reasons.

| CVE-2024-4340 as a running example corresponding to the | This agent is instructed to analyze, distill, and organize the raw |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| end-to-end reproduction shown in Figure 2. Moreover, we | information, extracted by the | Data Processor | , into a structured |  |  |  |  |
| provide a detailed case study on CVE-2024-5129, a logic | knowledge base while retaining essential details required to |  |  |  |  |  |  |
| vulnerability of missing authorization in | lunary-ai | , in Ap- | reproduce the given CVE. This includes extracting PoC or |  |  |  |  |
| pendix H. | exploit instructions from security advisories, which are invalu- |  |  |  |  |  |  |
| This module comprises two sub-modules: the | Data Processor | , | lighting where/how the vulnerability was mitigated. As shown |  |  |  |  |
| which locates the vulnerable project’s source code and gath- | in Figure 2, the | Knowledge Builder | included both of these |  |  |  |  |
| ers relevant raw resources, and the LLM-based | Knowledge | details in the knowledge base. In case an advisory does not |  |  |  |  |  |
| Builder | , which transforms these resources into a structured | include an exploit, the LLM agent is tasked with generating |  |  |  |  |  |
| knowledge base. Below, we provide detailed functionalities | an overview of what an exploit might entail. Additionally, |  |  |  |  |  |  |
| of these sub-modules. | capturing the patch details helps to localize the root cause of |  |  |  |  |  |  |
| For the given CVE ID, this sub-module identifies and extracts | including only essential information in their context to avoid |  |  |  |  |  |  |
| the vulnerable version of the software along with all relevant | overloading the LLM’s context window. |  |  |  |  |  |  |
| CVE details, as follows: | Output. | A structured | CVE knowledge base | providing details |  |  |  |
| Source Code Extraction. | The | Data Processor | begins by locat- | of CVE, including its associated CWEs, affected software |  |  |  |
| ing the source code for the vulnerable project linked to the | configurations, root causes (if provided in the security advi- |  |  |  |  |  |  |
| CVE. It searches the GitHub URLs referenced in the “cvelist” | sory), and essential information from security advisories and |  |  |  |  |  |  |
| settings. For instance, CVE-2024-4340 affects all versions of | Once the knowledge base is populated and the vulnerable ver- |  |  |  |  |  |  |
| “sqlparse” prior to | v0.5.0 | . Accordingly, the latest affected | sion of the project’s source code is downloaded, the next ob- |  |  |  |  |
| version ( | v0.4.4 | ) is retrieved using the GitHub API, and its | jective is to build the project in a way that allows the exploit to |  |  |  |  |
| source code | is downloaded (as shown in Figure 2). | be executed. To achieve this, our pipeline employs two | devel- |  |  |  |  |
| (3) | Patch commits | : The | git-diff | of code changes in the tar- | 3.2.1 | Prerequisite Developer Agent | 3 |
| 1 | “ | cvelist | ” is an automated pilot program for CVE submission through | step before actually setting up the vulnerable project. This is |  |  |  |

---

## Page 5

CVE-2024-4340 3 3. Exploiter 4. CTF Verifier

Pre-Reqs Dev Pre-Reqs

4

a

| Data Processor | Affected | b |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Version | v0.4.4 | get _f i l e | ( READM | E) | a |
| Descript ion | c |  |  |  |  |

b

| Passing a heavily nested list | CWE-674 | exec_l s | ( exam | pl es) |
| --- | --- | --- | --- | --- |
| d | exec |  |  |  |
| to sqlparse.parse() leads to a | Uncontrolled | get _f i l e | ( pypr oj ect ) | c |

exec

get _f i l e ( sql . py) d

GHSA/CVE-2024-4340 Commit b4a39d9 e

Important files: sql.py ...

exec

| Summary: | .... | Required Services: | None |
| --- | --- | --- | --- |
| Details + PoC: | ... | Expected State: | After creating a |
| sqlparse==0.4.4, run poc, .... | Access: |  |  |

pyt hon version ...

2 5

Setup Critic

Feedback

1.Detailed Summary .... .... Overall, all criteria are

satisfied: correct vulnerable

2.Root Cause Analysis: The core of the version is installed, the PoC

a.input with nested square brackets ...

b.Input is fed to sqlparse.parse() ...

LLMs Base

https://github.com/BUseclab/cve-genie/tree/main/results/CVE-2024-4340

.

these details were consistently overlooked by LLMs, causing

setup failures. Identifying and correcting such issues early

reduces unsuccessful attempts, conserves the LLM’s context

window, and improves the likelihood of successful setup.

(2) During environment setup, the agent’s job is to explore and

analyze the source code to identify critical components and to

projects, having to do both tasks with one agent can exceed

the context limit and reduce efficiency (as demonstrated in

the ablation study in Section 4.2). To address this, we dele-

gate the exploration of the code base to a dedicated agent, the

Pre-Requisite Developer , allowing the setup process to focus

more on building the project.

(3) The Pre-Requisite Developer also defines the “expected

state,” i.e., when the project is fully set up and ready for ex-

ploitation. This state guides the Setup Developer Agent in

verifying the correct configuration of the vulnerable envi-

ronment. For example, in CVE-2024-4340 (Figure 2), the

Pre-Requisite Developer explored the root directory and key

files such as README and sql.py to understand the project

context, then specified the expected state as having sqlparse

version v0.4.4 installed for the exploit to work correctly.

5

| 6 | 8 |  |  |
| --- | --- | --- | --- |
| a | a |  |  |
| get _f i l e | ( sql . py) | exec_l s | ( . ) |

get _f i l e ( __i ni t __)

| b | exec | ( python - << 'print | b |
| --- | --- | --- | --- |
| ( pyt hon | - V) | sqlparse version') | get _f i l e ( __i ni t __) |

c

( pi p i nst al l exec ( python - << 'poc as Verifier: see Figure 4a, and 4b (for

get _f i l e ( engi ne. py) Success: True

Exploit : CVE-2024-4340 is an

wr i t e_f i l e ( poc. py)

( pyt hon poc. py) PoC: see Figure 3 Flag Checker

1. Make sure you have Feedback 3xpl oi t 66f ul l

7

The exploit developer agent

Setup correctly identified and targeted Feedback

Logs 10

the uncontrolled recursion

vulnerability in sql par se Verifier Critic

v0. 4. 4 . . .

2. Builder Setup PoC the correct flag in the supplied

Code 11 Reprod. 2. exploit and verifier stored

Output. (1) Detailed overview of the project, (2) important

files to pay attention to during the setup, (3) required services

and their configurations, and (4) expected state of the project

upon successful setup to facilitate verification.

The Setup Developer begins in the directory containing the

vulnerable version’s source code and focuses on configuring

the project based on instructions from the Pre-Requisite De-

veloper , exploring the codebase when necessary. For CVEs

involving third-party libraries, our initial experiments showed

that setup is greatly simplified by using package managers

like pip or npm to install specific vulnerable versions instead

of building from source. For example, in the case of CVE-

2024-4340 affecting sqlparse , the Pre-Requisite Developer

instructed the installation of version 0.4.4 , and the Setup De-

veloper executed pip install sqlparse==0.4.4 directly

(command 4a , Figure 2), resulting in a smooth setup. If the

package manager fails, the Setup Developer falls back to

building from source. Typically, the Pre-Requisite Developer

also recommends running a basic PoC to confirm readiness

| 1 | exec_l s | ( . ) | Setup Dev | Exploit Dev | Verifier Dev |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DoS | due to RecursionError. | Recursion | e | sql par se==0. 4. 4) | a string') | weak and strong | verifier generated) |
| High Severity | Overview: | Project sql par se .... | Verifier |  |  |  |  |
| sqlparse < v0.5.0 | Text | f | uncontrolled recurrsion .... | 9 | Feedback |  |  |
| Impact: | DoS ... | pyt hon env, and installing | Success: | True | Exploit Logs | # | STDOUT |
| Raw Data | 2. Installed vulnerable version .... | Exploit Critic | # | STDERR |  |  |  |
| Knowledge Builder | Verifier |  |  |  |  |  |  |
| vulnerability is in | TokenList.flatten() | demonstrates the flaw, and no | ... Overall, the | verifier meets all |  |  |  |
| method (defined in | sqlparse/sql.py | ) .... | artificial vulnerability was added | required conditions | and produced |  |  |
| 3.Exploitat ion Details & PoC: | Info | run-time logs | ... |  |  |  |  |
| c. ...Python exceeds it recursion limit ... | Tools for | Knowledge | Text | Source | Store | 1. VM | snapshot stored |
| 1. Processor | CVE | 3. Cost = $0.27 -- Time = | 5 mins |  |  |  |  |

Figure 2: CVE-G ENIE architecture and an end-to-end example of workflow of reproduction for CVE-2024-4340, i.e., Denial

of Service due to RecursionError in sqlparse < v0.5.0 . See artifact of CVE-2024-4340 complete reproduction run here -

| (1) Our preliminary experiments reveal that many projects | access to read-only tools, i.e., | execute_ls_command | , and |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| contain inaccurate and incomplete information in their | get_file_by_name | , which the agent can use to traverse the |  |  |  |  |
| README | files (e.g., vulnerable version | v1.2.7 | of | lunary | for | code base and read files, because we do not want the agent |
| CVE-2024-5129, includes incorrect paths to | .env | files that | to execute any commands or write to files in this phase (see |  |  |  |
| are crucial for the setup). Without the | Prerequisite agent | , | Appendix E for tools details). |  |  |  |
| build the project by executing a series of commands. For large | 3.2.2 | Setup Developer Agent | 4 |  |  |  |
| Tools. | For this step, we only provide the LLM agent with | before handing off to the next agent (e.g., commands | 4e | and |  |  |

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

---

## Page 6

4f in Figure 2).

Tools. For this step, we allow access to the

following tools, i.e., execute_ls_command ,

execute_linux_command , get_file , write_to_file ,

and set_environment_variable .

Output. This agent returns a final decision whether the setup

instructions on how another agent can access the running

project.

The Setup Critic evaluates whether the project setup per-

formed by the Setup Developer is correct and complete, en-

suring that the environment is properly configured for the

vulnerability described in the CVE knowledge base to be

setup, or deliberately injecting vulnerabilities into the code-

tion design for the Setup Critic . Based on this, the critic is

decision on whether the setup is valid and complete, and

setup if necessary.

After successfully configuring the vulnerable system, the next

3.3.1 Exploit Developer Agent 6

edge base on pre-configured vulnerable systems. If a PoC

the script with the appropriate triggering input before deliv-

6

1 """

2 PoC - CVE-2024-4340 (sqlparse < 0.5.0)

3 EXAMPLE THAT CRASHES v0.4.4

4 python3 exploit.py 10000

5 """

6 import sys

7 import sqlparse

8 def main() -> None:

| 9 | if len | (sys.argv) != 2: |  |
| --- | --- | --- | --- |
| 11 | sys.exit(1) |  |  |
| 12 | arg = sys.argv[1] |  |  |
| 13 | try | : |  |
| 14 | depth = | int | (arg) |
| 16 | except ValueError | : |  |
| 17 | payload = arg |  |  |
| 18 | sqlparse.parse(payload) |  |  |

19 if __name__ == "__main__":

20 main()

(a) Exploit script for CVE-2024-4340. It constructs a deeply nested

| 3 | sqlparse.parse(payload) |
| --- | --- |
| 4 | .... |
| 7 | [Previous~line~repeated~983~more~times] |

RecursionError after excessive recursive calls within sqlparse .

Figure 3: PoC for CVE-2024-4340 in sqlparse v0.4.4 ,

Tools. This agent uses the same tools as the Setup Developer .

Output. The agent returns its final decision whether it consid-

| is successful or not. If successful, the output also includes | 10 | print | ("Usage: python3 exploit.py <depth>") |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.2.3 | Setup Critic Agent | 5 | 15 | payload = "[" * depth + "]" * depth |  |  |  |
| exploited. Additionally, this agent plays a critical role in de- | list payload and submits it to | sqlparse.parse() | , triggering uncon- |  |  |  |  |
| tecting deceptive or shortcut behaviors by the LLM, such as | trolled recursion. The included comment documents a crashing input |  |  |  |  |  |  |
| fabricating a mock project instead of performing a genuine | (depth 10,000) that reliably triggers the vulnerability. |  |  |  |  |  |  |
| base to simplify exploitation. These undesirable patterns are | 1 | Traceback (most recent call last): |  |  |  |  |  |
| discussed in detail in Section 3.5.1, which informs the instruc- | 2 | File "poc.py", line 20, | in | <module> |  |  |  |
| equipped to identify both functional and security-related flaws | 5 | "sqlparse/sql.py", line 214, | in | flatten |  |  |  |
| in the setup process. | 6 | yield from | token.flatten() |  |  |  |  |
| Output. | A comprehensive | analysis | of the setup logs, a binary | 8 | RecursionError | : maximum recursion depth exceeded |  |
| actionable | feedback | for correcting issues or improving the | (b) | Execution | traceback produced by the | exploit, showing | a |
| 3.3 | Exploiter | showing the exploit script and the resulting crash. |  |  |  |  |  |
| step in our pipeline is to generate an exploit for the given | or exploitation steps are available, the | Exploit Developer | iter- |  |  |  |  |
| vulnerability. CVE-G | ENIE | accomplishes this using two LLM | atively analyzes the codebase using available tools to develop |  |  |  |  |
| agents: the | Exploit Developer | , which develops the PoC for | a functional exploit. Upon success, it produces a Python PoC |  |  |  |  |
| an exploit in the vulnerable environment, and the | Exploit | script that accepts the crashing input via the command line, in- |  |  |  |  |  |
| Critic | , which analyzes the logs of the | Exploit Developer | and | cludes comments on the expected input format, and provides |  |  |  |
| evaluates the exploit for the given vulnerability. Below, we | an example input. This ensures that the | CTF Verifier | can |  |  |  |  |
| discuss their detailed functionalities. | reliably validate the exploit without repeating the analysis. |  |  |  |  |  |  |
| The | Exploit Developer | is responsible for crafting and demon- | ers the exploit is successful or not. If successful, it provides |  |  |  |  |
| strating exploits for vulnerabilities listed in the CVE knowl- | an | overview of the exploit | and a | Python | PoC script. |  |  |
| is provided, the agent replicates and verifies it by executing | 3.3.2 | Exploit Critic Agent | 7 |  |  |  |  |
| ering the final, working PoC. For example, in CVE-2024- | Similar to the role of the | Setup Critic | , the | Exploit Critic | is |  |  |
| 4340 (Figure 2), the PoC was available, so the agent validated | tasked with evaluating the behavior of the | Exploit Developer |  |  |  |  |  |
| the setup ( | 6b | ), demonstrated the exploit ( | 6c | ) by triggering | by analyzing its execution logs. Its primary goal is to deter- |  |  |
| RecursionError | in | sqlparse/sql.py | (see Figure 3b), and | mine whether the generated exploit is both valid and high- |  |  |  |
| submitted the verified PoC script (see Figure 3a). If no PoC | quality. This includes verifying that the exploit could plausibly |  |  |  |  |  |  |

---

## Page 7

succeed in a real-world setting; that it does not rely on ma-

nipulating or altering the original setup in illegitimate ways;

and that it avoids fabricated shortcuts, oversimplified logic,

or artificial assumptions that would not hold in practice.

To perform this assessment, the Exploit Critic leverages

a predefined set of behavioral patterns and common failure

tions that are unfaithful to the original intent or technically in-

After generating a working exploit for a given CVE, the final

step is to create a verifier script that confirms whether the

agent module generates a candidate verifier, the Flag Checker

module ensures that the exploit correctly retrieves a flag, and

the Verifier Critic agent assesses the quality and effectiveness

of the verifier for the given exploit.

format the verifier script in three structured steps:

sets up the environment, and prepares a flag to return if

the exploit correctly triggers the vulnerability.

2. Exploit Execution : Runs the provided PoC script to trig-

ger the vulnerability. We make sure that the agent cannot

3. Post-Setup : Verifies the success of the exploit, and if

successful, the script returns the flag.

4340 or an AddressSanitizer: heap-buffer-overflow

dataset with a known UUID, then executes the exploit by issu-

ing an unauthenticated deletion request targeting that UUID,

7

1 import os, subprocess, sys

2 FLAG = "3xploit66full"

3

4 def pre_setup():

5 # Configuring PYTHONPATH

6

7 def run_exploit():

10

11 def post_exploit(proc):

15

16 if __name__ == "__main__":

| 17 | pre_setup() |  |
| --- | --- | --- |
| 19 | except | subprocess.TimeoutExpired: sys.exit(1) |
| 20 | if | post_exploit(result): |
| 21 | print | (FLAG) |

1 import os, sys, importlib, traceback

2 FLAG = "3xploit66full"

3

4 def pre_setup():

5 assert sqlparse.__version__ < "0.5.0"

6

| 8 | sys.argv = ["exploit.py", "10000"] |  |
| --- | --- | --- |
| 9 | try | : |
| 14 | except | : |

16

| 18 | return | status == "recursion_error" | and |
| --- | --- | --- | --- |
| 19 | "sqlparse/sql.py" | in | tb |

20

21 if __name__ == "__main__":

| 22 | pre_setup() |  |
| --- | --- | --- |
| 23 | status, tb = run_exploit_inprocess() |  |
| 25 | print | (FLAG) |

(b) Attempt 2 with Verifier Critic ’s feedback – Improved veri-

Verifier Critic feedback.

| cases, as detailed in Section 3.5.2. By comparing the exploit’s | 8 | cmd = [sys.executable, "exploit.py", "10000"] |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| behavior against these known issues, the critic can detect ac- | 9 | return | subprocess.run(cmd, timeout=20) |  |  |  |  |  |
| correct. When flaws are identified, the | Exploit Critic | provides | 12 | output = (proc.stdout | or | "") + (proc.stderr | or | "") |
| structured, actionable feedback to improve the robustness of | 13 | return | proc.returncode != 0 | and |  |  |  |  |
| the exploit in subsequent iterations. | 14 | "RecursionError" | in | output |  |  |  |  |
| 3.4 | CTF Verifier | 18 | try | : result = run_exploit() |  |  |  |  |
| exploit was successful. This approach is inspired by security | (a) Attempt 1 – Weak verifier script: | pre_setup() | lacks a check |  |  |  |  |  |
| Capture-The-Flag (CTF) challenges, where exploiting a vul- | for the vulnerable | sqlparse | version. The exploit is run with a |  |  |  |  |  |
| nerability reveals a hidden “flag” i.e., a string of random char- | 20s | timeout, risking missed | RecursionErrors | if they occur af- |  |  |  |  |
| acters or numbers. The | CTF Verifier | uses three sub-modules | ter the limit. The verification relies solely on detecting the string |  |  |  |  |  |
| to develop and validate such verifiers. The | Verifier Developer | RecursionError | in output, which can be trivially spoofed. |  |  |  |  |  |
| 3.4.1 | Verifier Developer Agent | 8 | 7 | def | run_exploit_inprocess(): |  |  |  |
| Following the CTF methodology, we prompt the | Verifier De- | 10 | importlib.import_module("exploit").main() |  |  |  |  |  |
| veloper | to create a general CTF-style | Python | verifier script | 11 | return | "no_exception", "" |  |  |
| for a given PoC script. So, if the verifier script runs the PoC | 12 | except | RecursionError: |  |  |  |  |  |
| and it successfully triggers the vulnerability, it returns this | 13 | return | "recursion_error", traceback.format_exc() |  |  |  |  |  |
| flag ( | 3xploit66ful | ). We prompt the | Verifier Developer | to | 15 | return | "other_exception", traceback.format_exc() |  |
| 1. | Pre-Setup | : Prepares the necessary inputs for the exploit, | 17 | def | exploit_succeeded(status, tb): |  |  |  |
| modify the PoC script to avoid contamination. | 24 | if | exploit_succeeded(status, tb): |  |  |  |  |  |
| This verifier architecture provides consistent and reliable | fier: Validates project version | sqlparse < 0.5.0 | , runs the ex- |  |  |  |  |  |
| exploit validation across a broad spectrum of vulnerability | ploit in-process to avoid timeout issues, and explicitly checks |  |  |  |  |  |  |  |
| classes. It supports vulnerabilities with directly observable | for a genuine | RecursionError | with | traceback | originating from |  |  |  |
| failure signals, such as a | RecursionError | in CVE-2024- | sqlparse/sql.py | , preventing spoofed or misleading outputs. |  |  |  |  |
| in CVE-2024-10525, as well as higher-level logic flaws. For | Figure 4: Verifier scripts for exploit (in Figure 3) for CVE- |  |  |  |  |  |  |  |
| example, in the case of the missing-authorization flaw in CVE- | 2024-4340 corresponding to the run in Figure 2, illustrating |  |  |  |  |  |  |  |
| 2024-5129 (Appendix H), the verifier first inserts a legitimate | the progression from a weak to a robust verifier based on |  |  |  |  |  |  |  |

---

## Page 8

| and finally confirms successful exploitation by verifying that | Model | # | Max | Max | Reas- | Open | Cutoff |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| the dataset has been removed from the database. | Params | Inp | Out | oning | Src |  |  |  |  |  |  |
| Tools. | This agent follows the same read-only tools as the | Pre- | o3 | n/a | 200k | 100k | ✓ | ✗ | 05/2024 |  |  |
| Requisite Developer | agent, as in this step we don’t want the | o4-mini | n/a | 200k | 100k | ✓ | ✗ | 05/2024 |  |  |  |
| model to execute anything, and we do all validations using | Claude 3.7 Sonnet | n/a | 200k | 64k | ✓ | ✗ | 11/2024 |  |  |  |  |
| the | Flag Checker | and the | Verifier Critic | . | Claude 3.5 Sonnet | 175B | 200k | 8k | ✗ | ✗ | 04/2024 |

Once the verifier script is generated for the given exploit,

before passing it to the critic agent, the Flag Checker executes

the verifier script to ensure that it runs with the exploit script

without any errors and produces the expected output, i.e.,

is repeated until a maximum of five attempts is reached, with

3.4.3 Verifier Critic Agent 10

issues identified in Section 3.5.3, the agent flags incomplete

If the given CVE passes the Verifier Critic check, CVE-

G ENIE marks it as reproduced and stores the VM snapshot

for the vulnerable environment as well as the exploit and veri-

fier scripts. Moreover, CVE-G ENIE also stores the metadata,

such as LLM cost, time spent, and all agents’ conversations.

3.5 Selecting LLMs and Engineering Prompts

for CVE-G ENIE ’s Optimal Performance

8

| Gemini 2.5 Pro | n/a | 1M | 65k |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Gemini 2.5 Flash | n/a | 1M | 65k |  |  |  |
| Llama 4 Maverick | 400B | 1M | n/a | ✗ | ✓ | 08/2024 |
| Qwen 3 | 235B | 128k | 64k | ✓ | ✓ | 06/2024 |
| DeepSeek R1 | 671B | 128k | 8k | ✓ | ✓ | 07/2024 |

Table 3: Studied LLMs.

Dataset ( D

producing vulnerabilities using CVE-G ENIE , we construct

a small-scale, diverse dataset ( D S ) consisting of 60 CVEs.

These CVEs were published after the latest knowledge cutoff

tinct software projects.

pabilities. Thus, for each of these modules, we systematically

tasks using the following 5-step procedure:

(1) Candidate Selection: For each module, we identify subsets

of LLMs from Table 3 as potential developers and critics,

based on prior evidence of their capabilities, as well as time

and cost constraints.

(2) Developer Evaluation: Each candidate developer LLM is

run for the given module, and its outputs are manually scored

by the authors. The highest-scoring LLM is chosen as the

developer.

| Output. | A | Python | script that acts as a custom | verifier | for the | ✓ | ✗ | 01/2025 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exploit/PoC of the given CVE. | ✓ | ✗ | 01/2025 |  |  |  |  |  |  |
| 3.4.2 | Flag Checker | 9 | Deepseek V3 | 671B | 64k | 8k | ✗ | ✓ | 07/2024 |
| the correct flag. For instance, figure 2 shows that the correct | process to identify the best performing LLMs and prompt |  |  |  |  |  |  |  |  |
| flag | 3xploit66ful | is released when executing the verifier | integrations. We evaluate ten state-of-the-art LLMs (Table 3) |  |  |  |  |  |  |
| scripts generated for CVE-2024-4340. If a script fails due to | across CVE-G | ENIE | ’s three core modules, | Builder | , | Exploiter | , |  |  |
| a runtime error or if the flag is missing from the output, the | and | CTF Verifier | , using a diverse set of 60 post–knowledge- |  |  |  |  |  |  |
| system assumes that the verifier is incorrect. Feedback is then | cutoff CVEs, while simultaneously engineering and refining |  |  |  |  |  |  |  |  |
| sent to the | Verifier Developer | to revise the script. This process | task-specific prompts for each module. |  |  |  |  |  |  |
| each attempt ensuring functional correctness of the verifier. | S | ) | . | To evaluate the capabilities of LLMs in re- |  |  |  |  |  |
| Once the verifier and exploit scripts pass functional valida- | date of the LLMs under study (January 2025), as listed in |  |  |  |  |  |  |  |  |
| tion via the | Flag Checker | , they are further examined by the | Table 3. To ensure that | D | S | is both representative and diverse, |  |  |  |
| Verifier Critic | , which performs a similar evaluative role as | we select 40 CVEs from the top 25 most dangerous CWE [37] |  |  |  |  |  |  |  |
| the other critic agents, focusing specifically on the response | categories, and the remaining 20 CVEs are randomly sam- |  |  |  |  |  |  |  |  |
| produced by the | Verifier Developer | . It examines whether the | pled from the other CWE types. The resulting dataset, | D | S | , |  |  |  |
| verification process was properly carried out, without assump- | comprises 60 CVEs drawn from 44 different CWE categories, |  |  |  |  |  |  |  |  |
| tions, omissions, or unreliable heuristics. Using the behavioral | spanning 18 programming languages, and involving 56 dis- |  |  |  |  |  |  |  |  |
| or misleading verification strategies and provides feedback | Methodology. | CVE-G | ENIE | is composed of four modules. |  |  |  |  |  |
| on how the verification could be made more robust or ac- | The | Processor | ’s LLM-based component, the | Knowledge |  |  |  |  |  |
| curate. For instance, Figure 4 shows a detailed example of | Builder | , only performs a trivial task of summarization, so |  |  |  |  |  |  |  |
| verifiers generated for CVE-2024-4340 with weak and by- | we assign a lightweight LLM ( | o4-mini | ) to it. In contrast, the |  |  |  |  |  |  |
| passable verification criteria, which were corrected using the | remaining modules, i.e., | Builder | , | Exploiter | , and | CTF Verifier | , |  |  |
| Verifier Critic | ’s feedback. | require strong security vulnerability reasoning and SWE ca- |  |  |  |  |  |  |  |
| 3.4.4 | Store Reproduced CVE | 11 | select the best performing LLM for “developer” and “critic” |  |  |  |  |  |  |
| Upon finalizing the design of CVE-G | ENIE | ’s architecture, | (3) Critic Prompt Design: | We analyze common mistakes |  |  |  |  |  |
| we perform a systematic LLM model and prompt selection | made by developers and use these insights to design a module- |  |  |  |  |  |  |  |  |

---

## Page 9

| LLM Reported | TPR |  |
| --- | --- | --- |
| 40 | 0.6 |  |
| Qwen 3 | 20 | 0.4 |

DeepSeek V3

gemini-2.5-pro

Llama-4-Maverick claude-3.7-sonnet

specific critic prompt, enabling the critic to effectively detect

those mistakes.

TNR, and vice versa. Then then critic with the best trade-off

is selected.

In this section, we systematically select the most optimal

Candidate Selection. Setting up a project from scratch

is the most time-consuming and complex part of CVE-

G ENIE , as security advisories or CVEs do not provide in-

structions for setting up the vulnerable project. To ad-

dress this, we use two developer agents: one for explor-

ing the project and another for setting it up (see Sec-

tion 3.2). This process requires extensive tool calls and

gemini-2.5-pro , and deepseek-r1 , as the critic’s task only

requires one call, and therefore, they incur minimal overhead.

Developer Evaluation. We ran CVE-G ENIE up to the Setup

Developer stage 4 on CVEs from D S and manually evaluated

9

for libraries or binaries, we confirmed the vulnerable ver-

sion by invoking the corresponding -version (or equivalent)

command (e.g., for CVE-2025-1215 we verified that vim

we performed a health check to ensure the service was run-

As shown in Figure 5a, o4-mini emerged as the best de-

of 60 CVEs projects, while making an average of 20 tool calls

per CVE. In contrast, claude-3.5-sonnet mostly gave up

on the given setup task, and models like gemini-2.5-flash

and open-source LLMs were unreliable: Qwen 3 often de-

project.

Critic Prompt Design. From analyzing developer LLM setups,

required, it assumes commands like npm run dev succeed

to detect these errors while reviewing Setup Developer logs.

achieves the highest TPR and TNR when evaluating Setup De-

veloper ’s execution logs. Most of its false negatives involved

setups requiring external hardware, which Exploit Developer

cannot exploit anyway. Some valid setups were also mis-

takenly rejected due to limited post-setup checks. Given its

strong balance of recall and precision, we choose o3 as the

critic model for the Builder .

overhead.

3.5.2 Exploiter

| 60 | Manual Verified | 1.0 | TNR | sequence of commands required for installation. (2) We then |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 50 | gemini-2.5-flash | 0.8 | reviewed the logs of runs where the LLM reported successful |  |  |  |  |  |  |  |  |
| 30 | o4-mini | setup, comparing the executed commands against the doc- |  |  |  |  |  |  |  |  |  |
| 10 | 0.2 | umented installation process to assess alignment and com- |  |  |  |  |  |  |  |  |  |
| 0 | deepseek r1 | 0.0 | pleteness. (3) Finally, we validated the resulting environment: |  |  |  |  |  |  |  |  |
| claude-3.5-sonnet | v9.1.1096 | was installed), while for server-based software |  |  |  |  |  |  |  |  |  |
| (a) Developer Agent | (b) Critic Agent | ning and accessible at the expected port. |  |  |  |  |  |  |  |  |  |
| Figure 5: Builder Optimal LLM Evaluation | veloper LLM for the | Builder | , successfully setting up 32 out |  |  |  |  |  |  |  |  |
| (4) Critic Evaluation: | Each candidate critic LLM is evaluated | scribed setup steps without executing them using tool calls, |  |  |  |  |  |  |  |  |  |
| on true positive rate (TPR) and true negative rate (TNR). | while | gemini-2.5-flash | issued tool calls with frequent syn- |  |  |  |  |  |  |  |  |
| When TPRs are equal, we prefer the model with the higher | tax errors, eventually leading to the failed setup of the given |  |  |  |  |  |  |  |  |  |  |
| (5) Feedback Loop Assessment: | We rerun the chosen best | we observed three recurring mistakes: (1) when setup fails, the |  |  |  |  |  |  |  |  |  |
| developer–critic pair for the given module, and evaluate the | LLM builds a simplified mock-up substitute project instead; |  |  |  |  |  |  |  |  |  |  |
| correctness of the critic’s feedback and the developer’s capa- | (2) for | pip | / | npm | packages, it installs the latest version instead |  |  |  |  |  |  |
| bility to correctly address the critic’s feedback. | of the specified vulnerable one; and (3) when a server is |  |  |  |  |  |  |  |  |  |  |
| 3.5.1 | Builder | without verifying server health. We designed the critic prompt |  |  |  |  |  |  |  |  |  |
| configuration of LLMs and prompts for the | Builder | . | Critic Evaluation. | As shown in Figure 5b, the | o3 | model |  |  |  |  |  |
| command executions, making it both slow and costly with | Feedback Assessment. | We evaluated CVE-G | ENIE | up to | Setup |  |  |  |  |  |  |
| reasoning-heavy models like | o3 | or | claude-3.7-sonnet | , | Developer | stage | 4 | , using the best-performing developer |  |  |  |
| which | can | cost | $10–20 | per CVE. | Therefore, we | se- | ( | o4-mini | ) and critic ( | o3 | ) models. Minor issues flagged by |
| lect fast, cost-effective LLMs with sufficient context ca- | the | critic | (e.g., limited verification) were typically resolved by |  |  |  |  |  |  |  |  |
| pacity, | o4-mini | , | claude-3.5-sonnet | , | gemini-2.5-flash | , | the | developer | in one iteration. However, fundamental issues |  |  |
| llama-4-maverick | , | deepseek-v3 | , and | qwen3 | , as | developer | (e.g., mock-up version of the project) persisted even after five |  |  |  |  |
| agent candidates. For | critic | agents, we opt for stronger rea- | iterations. Therefore, we limit feedback to a single iteration to |  |  |  |  |  |  |  |  |
| soning models such as | o3 | , | o4-mini | , | claude-3.7-sonnet | , | efficiently address minor issues without incurring excessive |  |  |  |  |
| each developer LLM using the following procedure. (1) For | In this section, we systematically select the most optimal |  |  |  |  |  |  |  |  |  |  |
| each CVE, we first identified the official installation docu- | configuration of LLMs and prompts for the | Exploiter | . |  |  |  |  |  |  |  |  |
| mentation for the software’s vulnerable version and, based | Candidate Selection. | Generating a working exploit from a |  |  |  |  |  |  |  |  |  |
| on it, established both the expected final build state and the | given CVE in a pre-configured vulnerable environment is a |  |  |  |  |  |  |  |  |  |  |

---

## Page 10

| LLM Reported | o3 | TPR | LLM Reported | TPR |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 38 | Manual Verified | 1.0 | TNR | 16 | Manual Verified | 1.0 | TNR |  |
| 32 | 0.8 | 12 | 0.8 |  |  |  |  |  |
| 24 | o4-mini | 0.6 | o4-mini | 0.6 |  |  |  |  |
| 16 | 8 | o4-mini |  |  |  |  |  |  |
| 0.4 | 0.4 |  |  |  |  |  |  |  |
| gemini-2.5-flash | 8 | 0.2 | gemini-2.5-flash | 4 | 0.2 |  |  |  |
| 0 | deepseek r1 | 0.0 | 0 | deepseek r1 | 0.0 |  |  |  |
| gemini-2.5-pro | gemini-2.5-pro |  |  |  |  |  |  |  |
| gemini-2.5-pro | gemini-2.5-pro |  |  |  |  |  |  |  |
| claude-3.7-sonnet | claude-3.7-sonnet |  |  |  |  |  |  |  |
| claude-3.5-sonnet | claude-3.7-sonnet | claude-3.5-sonnet | claude-3.7-sonnet |  |  |  |  |  |
| (a) Developer Agent | (b) Critic Agent | (a) Developer Agent | (b) Critic Agent |  |  |  |  |  |
| Figure 6: Exploiter Optimal LLM Evaluation | Figure 7: Verifier Optimal LLM Evaluation |  |  |  |  |  |  |  |
| crucial task for reproducing CVEs. However, the | Exploiter | on code formatting, while | gemini-2.5-pro | frequently over- |  |  |  |  |
| requires less code base exploration than the | Builder | , as advi- | looked incomplete exploit verification. | Claude-3.7-sonnet |  |  |  |  |
| sories often provide PoCs, exploitation steps, or vulnerability | was too lenient, accepting nearly all exploits. Based on this |  |  |  |  |  |  |  |
| details. Thus, we include expensive reasoning models like | evaluation, we selected | o4-mini | as the most effective critic |  |  |  |  |  |
| o3 | , | claude-3.7-sonnet | , and | gemini-2.5-pro | in the can- | model for the | Exploit Critic | . |
| didates list of developers. To mitigate instability seen in open- | Feedback Assessment. | We evaluated feedback effectiveness by |  |  |  |  |  |  |
| source models (Section 3.5.1), we employ only closed-source | running CVE-G | ENIE | on 32 correct setups with the top devel- |  |  |  |  |  |
| LLMs as developers, while using the same critic LLMs as the | oper ( | o3 | ) and critic ( | o4-mini | ). This yielded valid exploits for |  |  |  |
| Builder | . | 16 CVEs, of which 3 were fixed based on the critic’s feedback. |  |  |  |  |  |  |
| Developer Evaluation. | For the 32 successful setups from Sec- | As in Section 3.5.1, the developer mainly resolved minor is- |  |  |  |  |  |  |
| tion 3.5.1, we ran CVE-G | ENIE | up to the | Exploit Developer | sues (e.g., incomplete verification or missing log triggers), |  |  |  |  |
| stage | 6 | and manually evaluated each developer LLM as fol- | while more complex flaws (e.g., incorrect exploit verification) |  |  |  |  |  |
| lows: (1) we checked whether the LLM executed a PoC or | persisted. To balance usefulness and cost, we therefore restrict |  |  |  |  |  |  |  |
| command sequence that demonstrated the exploit, (2) we | feedback to a single iteration. |  |  |  |  |  |  |  |

verified that the vulnerability was clearly triggered (e.g., un-

controlled recursion in CWE-674 resulting in a Recursion

Error ), (3) we assessed fidelity to the CVE description, (4)

trast, o4-mini often produced incorrect or mock-up exploits

and struggled with runtime errors. While claude and gemini

models showed strong capabilities in demonstrating exploits,

they lacked versatility across different vulnerability types.

Hence, we select o3 as the Exploit Developer .

of exploit demonstration, unclear vulnerability trigger, devia-

overly strict, rejecting correct exploits and focusing too much

10

3.5.3 Verifier

Exploiter .

Developer Evaluation. For the 16 valid exploits from Sec-

tion 3.5.2, we ran CVE-G ENIE up to the Flag Checker stage

9 and manually evaluated each developer LLM on three cri-

teria: (1) whether the verifier script followed the required

detailed example).

producing correct verifiers.

| we ensured no mock-up environments or fake exploits were | In this section, we systematically select the most optimal |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| used, and (5) we confirmed the exploit script followed the ex- | configuration of LLMs and prompts for the | CTF Verifier | . |  |  |  |
| pected format (see Section 3.3.1). Among all models, | o3 | con- | Candidate Selection. | Like exploit generation, creating a veri- |  |  |
| sistently performed best, successfully reproducing the highest | fier also demands deep understanding of security vulnerabili- |  |  |  |  |  |
| number of exploits (13 out of 27) and demonstrating them | ties to ensure the exploit is successfully triggered. Therefore, |  |  |  |  |  |
| end-to-end within the actual vulnerable environment. In con- | we use the same developer and critic candidates as in the |  |  |  |  |  |
| Critic Prompt Design. | We examined the failed exploit at- | format (see Section 3.4.1), (2) whether it executed the pro- |  |  |  |  |
| tempts and categorized the recurring error patterns, which | vided exploit script without modification, and (3) whether its |  |  |  |  |  |
| directly mirrored our manual verification criteria (e.g., lack | verification logic was precise and reliable (see Figure 4 for a |  |  |  |  |  |
| tion from CVE description, reliance on dummy/fake exploits, | As shown in Figure 7a, the | o3 | model generated 13 valid |  |  |  |
| or incorrect script formatting). We then incorporated these | verifiers out of 14, outperforming all others. While | o4-mini |  |  |  |  |
| categories into the | critic | agent’s prompt, enabling it to auto- | achieved comparable numbers, its verifiers more often relied |  |  |  |
| matically detect these issues for | Exploit Developer | . | on weak logic. Other models struggled with functional cor- |  |  |  |
| Critic Evaluation. | As shown in Figure 6b, | o4-mini | achieved | rectness and error recovery. We therefore selected | o3 | for the |
| the best balance of recall and specificity. In contrast, | o3 | was | Verifier Developer | due to its consistent one-shot success in |  |  |

---

## Page 11

Critic Prompt Design. We analyzed failures in verifier gen- 4.1 Baseline Assessment

eration and found that the recurring error types matched our

verification criteria (e.g., incomplete checks, incorrect vali-

dation logic, or misuse of the target environment). We used

these categories to design the critic agent’s prompt, enabling

it to automatically flag such errors when evaluating verifiers

Critic Evaluation. As shown in Figure 7b, only the o3 model

proved through the critic’s feedback. In our experiment, the

maximum number of feedback iterations required to resolve

either functional or critique-based issues was 4; therefore, we

allow up to 5 retries for both the Flag Checker and the Verifier

Critic .

3.5.4 Time and Cost Constraints

4 Experimental Methodology

In this section, we conduct a four-part evaluation of CVE-

evaluation on 841 CVEs (Section 4.4). These evaluations are

guided by the following research questions:

• RQ1: Does the performance of CVE-G ENIE vary over

• RQ2: Is the complex architecture of CVE-G ENIE nec-

nents are most crucial for reproduction?

11

In this section, we evaluate the baseline performance of

CVE-G ENIE and examine how its reproduction success

evolves across multiple runs in the presence of LLM non-

determinism.

tion 3.5).

configuration (Section 3.5). After each iteration, we store suc-

Results. We perform manual analysis of randomly selected

25 CVE reproduction runs, and observe that the variabil-

ity in CVE-G ENIE ’s performance primarily stems from the

Builder phase, which is more open-ended than the targeted

exploit generation guided by CVE context. Project setup in-

volves repository exploration ( Pre-Requisite Developer ) and

command execution ( Setup Developer ), where environment-

specific behaviors often cause failures. For example, one run

Over multiple runs, the number of successful project, exploit,

and verifier builds showed consistent gains with convergence

at run seven, indicating that most recoverable failures can be

resolved within a few retries.

retries.

end CVE reproduction.

| produced by the | Verifier Developer | . | Dataset. | For this study we use the same | D | S | dataset (Sec- |
| --- | --- | --- | --- | --- | --- | --- | --- |
| successfully identified critical but subtle issues in the verifier | Methodology. | Due to the non-deterministic nature of LLMs, |  |  |  |  |  |
| scripts, such as weak or flawed verification logic (Figure 4). | a single run may fail due to incorrect reasoning, while later |  |  |  |  |  |  |
| Other models provided weak or no critique, making | o3 | the | attempts might succeed [33]. To account for this, we run |  |  |  |  |
| most | CVE-G | ENIE | multiple times on | D | S | , using its most optimal |  |
| Feedback Assessment. | We evaluated CVE-G | ENIE | on 16 cor- | cessfully reproduced CVEs and rerun on the remaining ones. |  |  |  |
| rect exploits from the | Exploiter | , successfully generating ac- | This iterative approach helps maximize CVE reproduction |  |  |  |  |
| curate verifiers for 15 of them, of which 4 verifiers were im- | and reveals CVE-G | ENIE | ’s convergence. |  |  |  |  |
| In our evaluation of CVE-G | ENIE | , we found that successfully | failed because the | Setup Developer | modified the | PATH | vari- |
| reproduced CVEs typically required about $2 and 18 minutes | able, while a clean retry succeeded, highlighting the value of |  |  |  |  |  |  |
| on average, with the most resource-intensive case costing $6 | reattempting in a fresh environment. Since the | CTF Verifier |  |  |  |  |  |
| and taking 45 minutes. Failed reproductions, on the other | depends on the | Exploiter | , which in turn relies on the | Builder | , |  |  |
| hand, averaged up to $4 and 35 minutes. To balance flexibility | this initial project setup is a critical bottleneck. As a previ- |  |  |  |  |  |  |
| with cost control, we set a per-CVE budget cap of $5 and a | ously failed build, if later successful, can enable downstream |  |  |  |  |  |  |
| maximum runtime of 45 minutes for all experiments. | modules to reproduce a new CVE (as illustrated in Figure 8). |  |  |  |  |  |  |
| G | ENIE | : (1) a baseline study assessing consistency and effi- | RQ1: | Due to the non-determinism of LLMs, CVE- |  |  |  |
| ciency (Section 4.1); (2) an ablation study to assess the im- | G | ENIE | exhibits variability across runs, primarily dur- |  |  |  |  |
| pact of key components of CVE-G | ENIE | on its scalability and | ing project setup and environment configuration. Once |  |  |  |  |
| effectiveness (Section 4.2); (3) robustness testing under in- | project setup succeeds, downstream exploit generation |  |  |  |  |  |  |
| complete CVE information (Section 4.3); and (4) large-scale | and verification are more stable and converge in a few |  |  |  |  |  |  |
| multiple runs of CVE reproduction? | 4.2 | Importance of CVE-G | ENIE | ’s Architecture |  |  |  |
| essary, or can standalone LLMs achieve comparable re- | Having evaluated the selection of LLMs and prompts for |  |  |  |  |  |  |
| sults? | CVE-G | ENIE | (Section 3.5), we now assess CVE-G | ENIE | ’s |  |  |
| • | RQ3: | Can CVE-G | ENIE | effectively reproduce CVEs | architecture via a systematic ablation study that isolates the |  |  |
| with limited information, and which CVE report compo- | impact of CVE-G | ENIE | ’s individual components on end-to- |  |  |  |  |
| • | RQ4: | Can CVE-G | ENIE | reproduce a broad range of | Dataset. | We perform this ablation study using 15 CVEs from |  |
| CVEs across diverse CWEs, languages, and projects? | D | S | , each with complete information (i.e., CVE description, |  |  |  |  |

---

## Page 12

25 Exploiter Success

Verifier Success

Cummulative CVE Count 20

1 2 3 4 5 6 7

PoC, patch commit, and security advisory) and reproduced

consistently in the first three iterations of baseline assessment

(Section 4.1), and call this dataset D R . By keeping the CVE

context complete, we ensure that any performance differences

Developer , and Verifier Developer are the four indispensable

components of CVE-G ENIE for end-to-end CVE reproduc-

tion, for this evaluation of CVE-G ENIE ’s design we use the

following five ablation settings:

and feed raw data directly to all agents.

2. No Pre-Requisite Developer : Eliminate the Pre-

Requisite Developer , allowing the Setup Developer to

setup from scratch.

3. No Feedback Loops: Enforce single-shot execution with-

out iterative refinement, by removing all feedback loops.

4. No Critics: Remove the Verifier Critic and treat a CVE

as reproduced if the final scripts pass the Flag Checker .

5. Single Monolithic Agent: Combine all modular agents

into a single agent with access to the same tools, thereby

evaluating the performance of a standalone LLM without

CVE-G ENIE ’s agentic design and structured guidance

data and hit context window limits more often, which results

for Minecraft servers, with not very clear setup guides. Feed-

without them the reproduction success dropped sharply to

12

highlighting their role in reliable end-to-end CVE reproduc-

critic-guided

produce CVEs end-to-end. CVE-G ENIE ’s modular,

is essential for reliable CVE reproduction, and remov-

ing any of its components significantly degrades perfor-

mance (Table 4).

| Ideal | Knw | Pre- | Feed- | Critic | Single |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| - | ↑ | 30% | ↑ | 27% | ↓ | 67% | ↑ | 47% | - |
| Exploit | Max | Reprod | False |  |  |  |  |  |  |
| Failure | Tool | Rate | Reprod |  |  |  |  |  |  |

To evaluate how CVE-G ENIE performs when critical com-

ponents of a CVE report are missing, we study its robustness

under systematically reduced CVE context. We first present a

detailed qualitative case study of a single CVE to illustrate

how CVE-G ENIE adapts its reasoning under different con-

text losses, and then conduct a quantitative ablation study to

quantify the impact at scale.

shown in Figure 2.

2

//github.com/andialbrecht/sqlparse/commit/

b4a39d9850969b4e1d6940d32094ee0b42a2cf03

| 45 | tion. Finally, collapsing all components into a single mono- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | lithic agent resulted in zero successful reproductions, even |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 35 | when using advanced standalone LLMs ( | o3 | ), underscoring |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 30 | Builder Success | the necessity of CVE-G | ENIE | ’s modular, feedback-driven, and |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Run Numbers | RQ2: | Standalone LLMs are currently unable to re- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Figure 8: CVE-G | ENIE | performance over five runs on | D | S | . | feedback-driven, and critic-guided architecture design |  |  |  |  |  |  |  |  |  |  |  |  |
| arise solely from modifications | Case | Build | Reqs | back | Agents | Agent |  |  |  |  |  |  |  |  |  |  |  |  |
| Methodology. | As | Data Processor | , | Setup Developer | , | Exploit | 15 | / 15 | 9 | / 15 | 13 | / 15 | 5 | / 15 | 8 | / 15 | 0 | / 15 |
| 1. | No | Knowledge Builder | : | Bypass the Knowledge Builder | Table 4: Ablation study of CVE-G | ENIE | ’s design. |  |  |  |  |  |  |  |  |  |  |  |
| independently plan and execute the entire environment | 4.3 | Robustness to Loss of CVE Context |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (see Appendix G). | 4.3.1 | Case Study for CVE-2024-4340. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Results. | In our ablation study (Table 4), removing the | Knowl- | We begin by performing a detailed case study for CVE-2024- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| edge Builder | component reduces reproduction success to | 4340 reproduction under three levels of CVE context losses, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9/15, as agents struggle to interpret unstructured advisory | and compare their reproductions against the ideal setting |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| in a 30% increase in exploit failures. Eliminating the | Pre- | 1) No Security Advisory / PoC. | In this setting, all secu- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Requisite Developer | has a comparatively mild effect (13/15), | rity advisories are removed from the CVE context, leaving |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| but places additional burden on the | Setup Developer | as it | only the developer patch commit | 2 | and the CVE descrip- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| has to do both codebase exploration and project setup at the | tion | 3 | . As a result, CVE-G | ENIE | relies heavily on analyz- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| same time, leading to 27% more tool-call limit violations. | ing the patch commit, exploring modified files, and inferring |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| We observe this behavior particularly in complex repositories | the PoC from the regression test added by the developer in |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| such as | CVE-2025-32389 | in | Nameless | , a website software | tests/test_regressions.py | . This test closely resembles |  |  |  |  |  |  |  |  |  |  |  |  |
| back loops emerged as the most critical design element, and | CVE-2024-4340 | Developer | Patch: | https: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5/15 (–67%). Similarly, removing critic agents reduced suc- | 3 | CVE-2024-4340 CVE Description: “Passing a heavily nested list to |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cess to 8/15 while increasing false reproductions by 47%, | sqlparse.parse() leads to a Denial of Service due to RecursionError.” |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 13

1 payload = ’[’ * depth + ’]’ * depth

2 sqlparse.parse(payload)

(a) Security advisory/PoC or patch commit is not available.

1 payload = ’select’ + ’(’ * depth + ’1’ + ’)’ * depth

2 sqlparse.parse(payload)

(b) Only CVE description is available.

Figure 9: PoC exploit payload generated by CVE-G ENIE

for CVE-2024-4340 under varying levels of incomplete CVE

information, this run required additional exploration, resulting

2) No Patch. Here, the developer patch commit is removed

quantify the robustness of CVE-G ENIE to incomplete CVE

context at scale.

Dataset (D R ) . We perform this ablation with D R dataset (Sec-

4 CVE-2024-4340 GHSA: https://github.com/advisories/

GHSA-2m57-hf25-phgg

Figure 10: Breakdown of CVE-G ENIE ’s run on D

31481 reproduction, an authorization flaw in the PHP-based

scription is provided, it successfully reproduces 9/15 cases

strates that while comprehensive CVE reports significantly

remains feasible even

higher cost, and increased time.

13

| context compared to the payload in ideal scenario in Figure 3a. | L |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| the PoC described in the existing advisory | 4 | , and the gener- | CVE context, we construct three variants of | D | R | by systemati- |
| ated exploit payload (Figure 9a) is comparable to the ideal | cally removing: (a) security advisory/PoC, (b) patch commit, |  |  |  |  |  |
| run shown in Figure 3a. Due to the absence of explicit PoC | and (c) everything except CVE description. |  |  |  |  |  |
| in a longer execution time (9 minutes) and higher cost ($0.67) | Methodology. | In this study, for each variant of | D | R | , we run |  |
| compared to the ideal scenario. | CVE-G | ENIE | three times per CVE, iteratively. |  |  |  |
| while security advisories remain available. CVE-G | ENIE | pri- | Results. | Removing the developer patch commit leads to a |  |  |
| marily leverages the PoC provided in the advisory, which | notable drop in reproduction success 10/15 (67%), even when |  |  |  |  |  |
| includes clear PoC exploit code, execution traces, vulnerable | a PoC is available. Patch commits provide essential local- |  |  |  |  |  |
| code, and vulnerability root cause. Consequently, the repro- | ization signals by identifying relevant files and code paths. |  |  |  |  |  |
| duction closely matches the ideal run in terms of generated | Without patch commits, the model must rely on broad code- |  |  |  |  |  |
| PoC exploit (Figure 9a), verification scripts, execution time, | base exploration, often resulting in inefficient search and |  |  |  |  |  |
| and cost. | budget exhaustion. We observed this behavior in CVE-2025- |  |  |  |  |  |
| 3) Only CVE Description. | In the most constrained setting, | API Platform Core | , where the absence of a patch caused |  |  |  |
| CVE-G | ENIE | has access only to the CVE description. Based | CVE-G | ENIE | to explore unrelated components and fail to |  |
| on this limited information, it starts by identifying the imple- | converge. Excluding security advisories reduces the success |  |  |  |  |  |
| mentation of | sqlparse.parse | and hypothesizes on how a | rate to 11/15 (73%). In these cases, failures are primarily |  |  |  |
| deeply nested inputs can trigger a recursive execution path | attributable to environment setup and verification difficul- |  |  |  |  |  |
| leading to a | RecursionError | . During PoC exploit genera- | ties rather than exploit generation. Advisories often provide |  |  |  |
| tion and verification, the first run failed to produce a payload | crucial contextual information, such as dependency versions, |  |  |  |  |  |
| that successfully triggered the | RecursionError | . However, | execution constraints, and validation guidance, that stream- |  |  |  |
| a second run from scratch succeeded in generating a valid | line reproduction, particularly when PoCs are not provided as |  |  |  |  |  |
| payload (shown in Figure 9b). This setting proved to be the | executable code but rather as high-level textual descriptions. |  |  |  |  |  |
| most challenging, requiring 20 minutes of execution time and | Despite these challenges, CVE-G | ENIE | maintains baseline |  |  |  |
| $4.50 LLM cost over two runs. | robustness under minimal context. When only the CVE de- |  |  |  |  |  |
| 4.3.2 | Evaluation at Scale. | (60%), albeit with increased cost and runtime. This demon- |  |  |  |  |
| In this section, we perform an ablation study to systematically | improve efficiency and reliability, meaningful reproduction |  |  |  |  |  |
| tion 4.2). We intentionally select these “easier” CVEs as a | RQ3: | CVE-G | ENIE | can reproduce CVEs under limited |  |  |
| controlled probe, since CVE-G | ENIE | can consistently repro- | context. | Code-based PoCs | provide the strongest guid- |  |
| duce them under full context. Hence, any performance degra- | ance, but in their absence, | patch commits | help localize |  |  |  |
| dation after removing specific information indicates that the | vulnerabilities. Reproduction remains possible even with |  |  |  |  |  |
| missing context is genuinely critical. To simulate incomplete | only | CVE descriptions | , but with lower success rates, |  |  |  |

---

## Page 14

4.4 Large Scale Evaluation CWE-ID Overall success PoC available No PoC

code. A CVE is included in ( D L ) if at least one of the fol-

specifies affected software versions, and the source code cor-

L ) ensures

(16), desktop applications (13), blockchain and cryptocur-

rency systems (7), mobile applications and SDKs (7), and

security tools (6). In terms of vulnerability types, the ma-

jority of CVEs in ( D L ) fall under the following categories:

injection and improper neutralization (29%), authorization

and authentication (11%), resource management (8%), infor-

| Library/Framework | 163/224 (72.8%) | 115/147 (78.2%) |
| --- | --- | --- |
| CLI Tool/Utility | 18/37 (48.6%) | 15/28 (53.6%) |
| Blockchain/Crypto/FinTech | 1/13 (7.7%) | 1/7 (14.3%) |

Table 5: CVEs reproduction coverage by project type.

14

| CWE-79 | 65/142 (45.8%) | 43/94 (45.7%) | 22/48 (45.8%) |
| --- | --- | --- | --- |
| CWE-400 | 22/36 (61.1%) | 13/19 (68.4%) | 9/17 (52.9%) |
| CWE-20 | 13/29 (44.8%) | 6/15 (40.0%) | 7/14 (50.0%) |
| CWE-1333 | 15/19 (78.9%) | 8/10 (80.0%) | 7/9 (77.8%) |
| CWE-94 | 9/19 (47.4%) | 2/8 (25.0%) | 7/11 (63.6%) |
| CWE-269 | 7/13 (53.8%) | 4/8 (50.0%) | 3/5 (60.0%) |
| CWE-352 | 8/10 (80.0%) | 5/6 (83.3%) | 3/4 (75.0%) |
| CWE-347 | 7/8 (87.5%) | 4/4 (100.0%) | 3/4 (75.0%) |

Table 6: Top 25 CWEs identified in the large-scale study and

their reproduction success rates, overall and stratified by PoC

availability.

in the Appendix, where Table 6 reports reproduction success

rates for the top CWEs. Meanwhile, Table 7 and Table 5

jority of failures involved web application CVEs lacking ei-

our agents cannot access, causing the exhaustion of their bud-

gets in exploring the codebase.

| Dataset | ( | D | L | ) | . | For our large-scale evaluation, we construct a | CWE-200 | 20/43 (46.5%) | 15/20 (75.0%) | 5/23 (21.7%) |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dataset, | ( | D | L | ) | , consisting of all CVEs published between June | CWE-22 | 16/37 (43.2%) | 11/22 (50.0%) | 5/15 (33.3%) |  |  |  |
| 2024 and May 2025 that include publicly available source | CWE-284 | 19/36 (52.8%) | 16/26 (61.5%) | 3/10 (30.0%) |  |  |  |  |  |  |  |  |
| lowing conditions is satisfied: (1) the CVE entry contains | CWE-770 | 14/24 (58.3%) | 7/9 (77.8%) | 7/15 (46.7%) |  |  |  |  |  |  |  |  |
| a GitHub URL (e.g., a patch commit) in its references that | CWE-918 | 7/22 (31.8%) | 6/13 (46.2%) | 1/9 (11.1%) |  |  |  |  |  |  |  |  |
| links directly to the relevant source code, or (2) the CVE | CWE-89 | 11/21 (52.4%) | 8/15 (53.3%) | 3/6 (50.0%) |  |  |  |  |  |  |  |  |
| responding to those versions is publicly accessible. Because | CWE-863 | 7/15 (46.7%) | 4/6 (66.7%) | 3/9 (33.3%) |  |  |  |  |  |  |  |  |
| these CVEs were disclosed after the knowledge cutoff of the | CWE-287 | 8/15 (53.3%) | 4/4 (100.0%) | 4/11 (36.4%) |  |  |  |  |  |  |  |  |
| LLMs ( | o3 | and | o4-mini | ) used in CVE-G | ENIE | , | ( | D | CWE-285 | 7/15 (46.7%) | 5/8 (62.5%) | 2/7 (28.6%) |
| zero prior exposure during model training. Overall, | ( | D | L | ) | com- | CWE-122 | 8/13 (61.5%) | 2/4 (50.0%) | 6/9 (66.7%) |  |  |  |
| prises 841 CVEs spanning 186 CWEs, 29 programming lan- | CWE-502 | 6/13 (46.2%) | 3/6 (50.0%) | 3/7 (42.9%) |  |  |  |  |  |  |  |  |
| guages, and 440 distinct open-source software (OSS) projects. | CWE-532 | 6/12 (50.0%) | 2/2 (100.0%) | 4/10 (40.0%) |  |  |  |  |  |  |  |  |
| The OSS projects cover a broad range of application domains, | CWE-78 | 4/11 (36.4%) | 4/9 (44.4%) | 0/2 (0.0%) |  |  |  |  |  |  |  |  |
| including web applications and backends (156), libraries and | CWE-74 | 7/10 (70.0%) | 4/4 (100.0%) | 3/6 (50.0%) |  |  |  |  |  |  |  |  |
| frameworks (147), CLI tools and binaries (28), cloud and | CWE-416 | 3/10 (30.0%) | 0/0 (–) | 3/10 (30.0%) |  |  |  |  |  |  |  |  |
| DevOps systems (25), embedded and networking software | CWE-639 | 2/9 (22.2%) | 1/4 (25.0%) | 1/5 (20.0%) |  |  |  |  |  |  |  |  |
| (18), operating systems and runtimes (17), AI/ML platforms | CWE-116 | 4/8 (50.0%) | 1/3 (33.3%) | 3/5 (60.0%) |  |  |  |  |  |  |  |  |
| mation exposure (6%), memory safety (3%), request forgery | Domain-Dependent Effectiveness of | CVE-G | ENIE | . | We ob- |  |  |  |  |  |  |  |
| (3%), and others. Our statistical analysis further shows that | serve that CVE-G | ENIE | shows the highest performance for |  |  |  |  |  |  |  |  |  |
| approximately 55% of CVEs in | D | L | fall under the top 25 most | library frameworks and AI/ML platforms categories, with the |  |  |  |  |  |  |  |  |
| dangerous CWEs [37], and around 49% lack a PoC in their | reproduction rates of 78% and 58%, excelling on CWEs such |  |  |  |  |  |  |  |  |  |  |  |
| advisory. | as CWE-79 (XSS), CWE-89 (SQLi), and CWE-284 (access |  |  |  |  |  |  |  |  |  |  |  |
| Methodology. | We use the same methodology as Section 4.1, | control). Meanwhile, the success appears more moderate for |  |  |  |  |  |  |  |  |  |  |
| and run CVE-G | ENIE | on | D | L | three times, iteratively. | web/backend applications (45%), where logic-driven CWEs |  |  |  |  |  |  |
| Results. | CVE-G | ENIE | reproduced 428 CVEs out of 841 (Fig- | such as 200, 22, and 918 have lower success rates. CVE- |  |  |  |  |  |  |  |  |
| ure 10), spanning 22 programming languages, 141 vulnera- | G | ENIE | struggles in binary-heavy domains such as desktop |  |  |  |  |  |  |  |  |  |
| bility types, and 267 projects. To better understand outcomes, | (18%), blockchain (8%), and mobile (29%) applications, espe- |  |  |  |  |  |  |  |  |  |  |  |
| we perform statistical analysis on all reproduction runs as | cially with memory-safety (e.g., CWE-122, 416) and crypto/- |  |  |  |  |  |  |  |  |  |  |  |
| well as manually analyze 50 successful and 50 failed cases, | validation (CWE-295, 327) flaws. A finer-grained breakdown |  |  |  |  |  |  |  |  |  |  |  |
| and categorize results as follows: | by vulnerability type and project characteristics is provided |  |  |  |  |  |  |  |  |  |  |  |
| Project Type | CVEs Reprod. | Projects Reprod. | further contextualize results by project scale, language, and |  |  |  |  |  |  |  |  |  |
| AI/ML Platform | 22/38 (57.9%) | 14/16 (87.5%) | domain. Finally, Tables 9–19 detail domain-specific CWE |  |  |  |  |  |  |  |  |  |
| Web Application/Backend | 171/383 (44.6%) | 86/156 (55.1%) | distributions, illustrating how failure |  |  |  |  |  |  |  |  |  |
| Cloud/DevOps Application | 13/33 (39.4%) | 13/25 (52.0%) | Failures. | For 198 cost/time overrun failures, ~80% were due to |  |  |  |  |  |  |  |  |
| Operating System/Runtime | 15/31 (48.4%) | 5/15 (33.3%) | cost overruns, where the agent either got stuck during project |  |  |  |  |  |  |  |  |  |
| Desktop Application | 6/34 (17.6%) | 2/13 (15.4%) | builds (~41%) or while generating exploits (~59%). The ma- |  |  |  |  |  |  |  |  |  |
| Mobile Application/SDK | 2/7 (28.6%) | 2/7 (28.6%) | ther vulnerability details or setup documentation. For exam- |  |  |  |  |  |  |  |  |  |
| Embedded/Networking | 11/27 (40.7%) | 10/18 (55.6%) | ple, none of the CVEs in project | discourse | built successfully |  |  |  |  |  |  |  |
| Security Tool/Server | 6/12 (50.0%) | 4/6 (66.7%) | since its | README | only links to external documentation, which |  |  |  |  |  |  |  |

---

## Page 15

Project # Re # T25 # Oth LoC Lang Cost. Running CVE-G ENIE costs approximately $2.77 per

CVEs CWEs CWEs CVE, moreover, open-source models currently do not perform

| lunary-ai | 35 | 13 | 22 | ~70k | TypeScript |
| --- | --- | --- | --- | --- | --- |
| vite | 6 | 6 | 0 | ~107k | TypeScript |
| yeswiki | 6 | 6 | 0 | ~234k | PHP |
| symfony | 5 | 4 | 1 | ~1.6M | PHP |
| llama_index | 5 | 4 | 1 | ~1.1M | Py |
| vim | 5 | 3 | 2 | ~1.2M | Vim Script, C |
| directus | 5 | 2 | 3 | ~398k | TypeScript |
| siyuan | 3 | 1 | 2 | ~265k | Go, TypeScript |

RQ4: At scale, CVE-G ENIE reproduced 428 / 841

CVEs, spanning 267 projects, 22 programming lan-

Vulnerabilities Involve UI Interactions. Currently, CVE-

G ENIE only supports command-line interface (CLI) inter-

actions. However, many web-based vulnerabilities require in-

teraction with a graphical UI, making them difficult to trigger

via CLI. Future work should explore integrating CVE-G ENIE

with UI environments, e.g., web browsers.

Multimodal CVE Knowledge Curation. Due to a lack of im-

age and video processing support, CVE-G ENIE struggles

with CVEs where the PoC is provided as an image or video.

Future work can address this limitation by integrating CVE-

G ENIE with multimodal LLMs. Additionally, leveraging ex-

ternal CVE resources through LLM-based deep search tools,

beyond standard vulnerability databases, may also help im-

prove reproduction success rates [38].

15

well. Therefore, to support further research, we release logs

CVE reproduction.

6 Conclusion

and repair. CVE-G ENIE successfully reproduced around 51%

scale and efficiency.

A Acknowledgments

contributed to this work.

Safe Release of Reproduced CVEs’ Data. For all of our studies,

we only include the CVEs that have a public patch available

on the National Vulnerability Database (NVD). This measure

prevents the attackers from using our reproduced CVEs to

exploit the stakeholders’ systems, and also helps us to safely

release the data of the CVEs reproduced in our experimental

studies.

Release of CVE-Genie’s Codebase. The aim of releasing CVE-

Genie’s codebase is to support defenders and solution devel-

opers by accelerating vulnerability triaging and tool devel-

opment for vulnerability detection and patching. Although it

is also possible for the attackers to leverage CVE-Genie to

reproduce vulnerabilities in the real world, our aim is to level

the playing field for defenders; specifically, to empower de-

fenders to reproduce CVE reports to attain up-to-date and

| WeGIA | 17 | 15 | 2 | ~1M | PHP | from all reproduction runs as a novel dataset to help the com- |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cpython | 10 | 2 | 8 | ~1.8M | Py, C | munity fine-tune and improve local models’ performance for |  |  |
| rails | 4 | 2 | 2 | ~450k | Ruby | In this paper we presented CVE-G | ENIE | , an automated frame- |
| phpipam | 4 | 2 | 2 | ~225k | PHP | work designed to reproduce real-world vulnerabilities at scale. |  |  |
| assimp | 4 | 4 | 0 | ~562k | C++ | This has considerable benefit for downstream security re- |  |  |
| cvat-ai | 3 | 3 | 0 | ~320k | Py, TypeScript | search (see Appendix F), which suffers from a shortage of |  |  |
| MobSF | 3 | 1 | 2 | ~132k | JS, Py | diverse high-quality data suitable for research and develop- |  |  |
| mlflow | 3 | 1 | 2 | ~870k | Py | ment of new tooling for automated vulnerability discovery |  |  |
| Table 7: Top 15 projects identified in the large-scale evaluation | (428) of 841 CVEs, with on average $2.77 cost per CVE, |  |  |  |  |  |  |  |
| of CVE-G | ENIE | , showing the number of reproduced CVEs, | across a vast variety of projects, CWEs, and programming |  |  |  |  |  |
| their classification into CWE Top 25 vs. other CWEs, lines of | languages. To the best of the authors’ knowledge, no other |  |  |  |  |  |  |  |
| code (LoC), and primary languages. | framework is capable of such comprehensive results at this |  |  |  |  |  |  |  |
| guages, and 141 CWEs, demonstrating broad applicabil- | We gratefully acknowledge and thank Dave Aitel, Harold |  |  |  |  |  |  |  |
| ity across ecosystems. Notably, 217 (51%) reproduced | Nguyen, Xin Hu, and Ian Brelinsky (OpenAI), as well as Stijn |  |  |  |  |  |  |  |
| CVEs fall within the MITRE top 25 most dangerous | Pletinckx and Lukas Dresel (University of California, Santa |  |  |  |  |  |  |  |
| CWEs, and 231 (54%) had no PoC available. | Barbara), for their valuable discussions and guidance that |  |  |  |  |  |  |  |
| 5 | Limitations and Future Work | B | Ethical Considerations |  |  |  |  |  |
| Over Critique. | As shown in Figures 5b, 6b, and 7b, all critics | reproducible CVE environments as benchmark test cases. |  |  |  |  |  |  |
| exhibit a lower TPR compared to their TNR. While this helps | These benchmarks will then be used to rigorously test and |  |  |  |  |  |  |  |
| reduce false positives, it also results in missing some valid | enhance vulnerability detection and patching systems, thereby |  |  |  |  |  |  |  |
| reproductions, particularly in cases where critics requested | understanding their performance and ideally accelerating their |  |  |  |  |  |  |  |
| detailed setup, exploit, or verifier that the developer could not | response capabilities. Following the beneficence criterion of |  |  |  |  |  |  |  |
| sufficiently provide. | the Menlo Report [14], we strongly believe that our system |  |  |  |  |  |  |  |

---

## Page 16

| provides more benefits than potential harms to the security | 3. | execute_ls_command: | The LLM specifies a direc- |
| --- | --- | --- | --- |
| community and to society. | tory, and we execute the | ls | command within it, re- |

C Open Science

includes all reproduction runs with their agent conver-

D Generative AI Usage

We used ChatGPT (OpenAI) to assist with LaTeX formatting,

as well as to review and refine spelling, grammar, and sentence

structure for improved clarity of the manuscript. Moreover,

all AI-assisted outputs were manually reviewed, edited as

needed, and explicitly approved by the authors before being

code. However, due to LLMs’ limited context windows, large

project files cannot be processed all at once. To address this,

we developed primitives enabling directory browsing using

“ project directory tree ” and command execution:

number of lines it wants to read from a given offset. To

16

turning the output. This command is distinct from

execute_linux_command due to its major role in

project directory exploration and its frequent use.

4. execute_linux_command: The LLM issues Linux com-

is still running.

This limit was found to be optimal in preliminary experiments

for maximizing CVE reproduction across all LLMs.

Output Formatting. For all agents requiring output in a spe-

cific format, we add a gpt-4o-mini -based format corrector

to the output parser. If parsing fails, the raw output is passed

to gpt-4o-mini for formatting. If formatting fails after three

attempts, an error is returned.

Category Application Benefits brought by CVE-G ENIE

Vul.

Dynamic fuzzing Benchmarks and initial fuzzing seeds

detection

| Static analysis | Benchmarks and static rules |  |
| --- | --- | --- |
| Vul. | Root cause analysis | Enrich inputs and enable more tools |
| Vul. | Patch generation | Benchmarks and testing environments |
| Patching | Patch verification | Inputs and environments |

Table 8: Tasks that benefit from CVE-G ENIE .

| CVE-G | ENIE | Framework and Dataset. | https://github. | mands to be executed from the project’s root directory. |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| com/BUseclab/cve-genie | . This includes (1) source code | Foreground commands have a 300-second timeout, with |  |  |  |  |  |  |
| of CVE-G | ENIE | and detailed instructions on how to run it, (2) | standard output and error logged to separate files. Af- |  |  |  |  |  |
| reproduction runs of all reproduced CVEs with their agent | ter completion, we return up to the last 100 lines of the |  |  |  |  |  |  |  |
| conversations/logs, intermediate artifacts, and final exploit | log and the log file path which LLM can read using |  |  |  |  |  |  |  |
| and verifier scripts, and (3) a web application to visualize the | get_file | for further analysis. Background execution is |  |  |  |  |  |  |
| CVE reproduction runs. | supported for non-blocking tasks (e.g., starting a web |  |  |  |  |  |  |  |
| Experiments Results. | https://osf.io/dcej4/overview? | server). For these, we show output after 5 seconds, pro- |  |  |  |  |  |  |
| view_only=81309bbc7e8c489abb9fb7e40bd1c0fb | . | This | vide the log file path, and indicate whether the process |  |  |  |  |  |
| sations/logs, intermediate artifacts, and final scripts. | (1) | 5. | set_environment_variable: | This | tool | allows |  |  |
| critics_evals.tar.gz | contains results for selecting opti- | for | setting | environment | variables | for | subsequent |  |
| mal LLMs and prompts (Section 3.5). (2) | baseline.tar.gz | execute_linux_command | calls. | We | observed that |  |  |  |
| contains results for the baseline assessment study (Sec- | LLMs frequently issue calls to export environment |  |  |  |  |  |  |  |
| tion 4.1). (3) | design_ablation.tar.gz | contains results | variables, which are not retained in successive runs |  |  |  |  |  |
| for CVE-G | ENIE | ’s | design | ablations | (Section | 4.2). | (4) | as each command is executed in a separate shell. To |
| robustness.tar.gz | contains results for CVE-G | ENIE | ’s | address this, we enable the LLM to set these variables, |  |  |  |  |
| robustness | to | loss | of CVE | context (Section | 4.3). | (5) | which are then passed to commands. There is also an |  |
| large_scale.tar.gz | contains results for multiple runs of | option to clear all set variables. |  |  |  |  |  |  |
| the large-scale study with 841 CVEs (Section 4.4). | Restrictions. | Each tool-calling agent is limited to 60 tool calls. |  |  |  |  |  |  |
| incorporated into the paper. | ML-based detection | Training and testing data |  |  |  |  |  |  |
| E | CVE-G | ENIE | Specifications | triage | Exploit generation | Ingredients for exploit chaining |  |  |
| CVE-G | ENIE | is built on LangChain and supports easy design | Other | LLM secure code generation | Benchmarks and testing environment |  |  |  |
| and integration of tools for LLMs. For CVE-G | ENIE | to effec- | applications | Penetration testing | Construct pen. test tasks and environment |  |  |  |
| tively reproduce CVEs, it require access to a project’s source | Attack detection | Benchmarks and detection rules |  |  |  |  |  |  |
| 1. | get_file: | The LLM agent specifies the file path and the | F | Applications of CVE-G | ENIE |  |  |  |
| prevent context overflow and improve efficiency, it reads | As shown in Table 8, reproducible CVEs can be used for a |  |  |  |  |  |  |  |
| a maximum of 300 lines at a time. If more content is | plethora of security analysis tasks, including vulnerability |  |  |  |  |  |  |  |
| needed, the agent can scroll up or down to access it. | detection, triage, exploitation, and patching. |  |  |  |  |  |  |  |
| 2. | write_to_file: | The LLM provides the path and content | Vulnerability Detection. | Most existing vulnerability detec- |  |  |  |  |
| for a file, which we then write to the specified file. This | tion datasets are built using patch commits from CVEs (see Ta- |  |  |  |  |  |  |  |
| facilitates modifications and updates within the project. | ble 1). They typically label the pre-patch version of a function |  |  |  |  |  |  |  |

---

## Page 17

| as vulnerable and the post-patch version as benign [7, 15, 40]. | CWE-IDs | # CVEs | PoC Available | No PoC |
| --- | --- | --- | --- | --- |
| However, extracting isolated functions often strips away crit- | Reprod | Failed | Reprod | Failed |

ical context [51], and functions labeled for a single vulner-

we can ensure that vulnerable execution traces are included,

preserving necessary context and confirming the presence

of vulnerabilities. Additionally, this approach supports both

static and dynamic analysis, unlike most existing datasets

for root cause identification. CVE-G ENIE supports this pro-

cess by offering exploits for individual vulnerabilities, which

can be combined into complex exploit chains for studying

multi-stage attacks. It also serves as a benchmark for evaluat-

crash stack traces and outputs. Additionally, its PoCs assist in

a scalable alternative because these CVEs are confirmed to

be vulnerable, they can be used to assess LLMs’ ability to

generate secure code. By prompting the LLM to implement

the functionalities in the vulnerable functions, and using the

ucating future penetration testers and developing automated

17

| CWE-502 | 6 | 3 | 1 | 1 | 1 |
| --- | --- | --- | --- | --- | --- |
| CWE-94 | 2 | 0 | 1 | 0 | 1 |

Table 9: Top CWEs reproduced in AI/ML Platform projects.

| CWE-79 | 99 | 34 | 37 | 10 | 18 |
| --- | --- | --- | --- | --- | --- |
| CWE-200 | 19 | 5 | 3 | 2 | 9 |
| CWE-285 | 9 | 5 | 2 | 2 | 0 |

Table 10: Top CWEs reproduced in Web App projects.

ular, agentic design and structured guidance, we collapsed

H Case Study for CVE-2024-5129

authorization checks and performs an unscoped deletion by

UUIDs.

| ability may contain others, resulting in noisy labels. Using | CWE-29 | 3 | 2 | 1 | 0 | 0 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| reproducible CVEs with working PoCs can address these | CWE-20 | 3 | 1 | 2 | 0 | 0 |  |
| issues. By executing PoCs during function code extraction, | CWE-77 | 3 | 0 | 2 | 1 | 0 |  |
| (e.g., SVEN [21], BigVul [15], PrimeVul [13]), which are | CWE-IDs | # CVEs | PoC Available | No PoC |  |  |  |
| limited to static methods. | Reprod | Failed | Reprod | Failed |  |  |  |
| Vulnerability Triage and Patching. | Reproducible CVEs are | CWE-284 | 29 | 12 | 8 | 2 | 7 |
| essential for effective vulnerability triage. They help eliminate | CWE-22 | 21 | 7 | 6 | 3 | 5 |  |
| false positives and provide an executable environment with | CWE-918 | 16 | 4 | 5 | 1 | 6 |  |
| known vulnerable inputs, which aids in accurately analyz- | CWE-89 | 15 | 5 | 6 | 1 | 3 |  |
| ing and reproducing bugs. This capability enables advanced | CWE-400 | 15 | 6 | 3 | 1 | 5 |  |
| techniques like reverse execution and backward taint analysis | CWE-20 | 12 | 4 | 3 | 1 | 4 |  |
| ing patching methods, providing rich contextual data such as | G | Single Monolithic Agent Study Design |  |  |  |  |  |
| verifying and refining patches. | To evaluate a standalone LLM without CVE-G | ENIE | ’s mod- |  |  |  |  |
| LLM Insecure Code Generation. | Reproducible CVEs are | all agents into a single monolithic agent with access to the |  |  |  |  |  |
| valuable for evaluating the security of code generated by | full toolset (Appendix A), its entire conversation history, and |  |  |  |  |  |  |
| LLMs. Recent studies have shown that LLMs can produce in- | an increased limit of 100 tool calls per attempt. The agent |  |  |  |  |  |  |
| secure code, particularly in security-critical contexts [55, 59]. | was provided with all CVE-related information directly in |  |  |  |  |  |  |
| Various benchmarks evaluate secure code generation capa- | the user prompt, and the system prompt explicitly instructed |  |  |  |  |  |  |
| bility of LLM, such as, CyberSecEval [55] prompts an LLM | it to follow a three-stage workflow (project setup, exploit |  |  |  |  |  |  |
| to generate code snippets and uses rule-based detectors to | generation, and verification), mirroring CVE-G | ENIE | ’s high- |  |  |  |  |
| identify insecure code, however, rule-based detection often | level procedure. Unlike CVE-G | ENIE | , no automated critic or |  |  |  |  |
| leads to false positives. To improve this, SecCodePLT [59] | feedback loops were used; instead, we manually inspected ex- |  |  |  |  |  |  |
| leverages CWE data and manually crafts dynamic test cases | ecution traces and the generated exploit and verifier artifacts |  |  |  |  |  |  |
| to evaluate secure code generation. Reproducible CVEs offer | to determine whether reproduction was successful. |  |  |  |  |  |  |
| associated PoCs to test the output, we can determine whether | Overview. | Versions of the | lunary | project prior to v1.2.8 |  |  |  |
| the generated code is vulnerable. | expose a | DELETE /v1/datasets/:id | endpoint that lacks |  |  |  |  |
| Penetration Testing and Attack Detection. | CVE-G | ENIE | dataset UUID. In the vulnerable release v1.2.7, the handler |  |  |  |  |
| offers a valuable resource for both penetration testing and | executes a SQL | DELETE | using only | id | , with no authentication |  |  |
| cybersecurity training. It provides ready-to-use exploitation | and no restriction to the caller’s project, allowing unauthenti- |  |  |  |  |  |  |
| scenarios along with verified solutions, making it ideal for ed- | cated deletion of arbitrary datasets by guessing or obtaining |  |  |  |  |  |  |
| testing tools. For defenders, these exploits can be analyzed to | Processor | . | The workflow starts with | Data Processor | resolv- |  |  |
| identify attack patterns, which can enhance detection mecha- | ing CVE-2024-5129’s affected versions and automatically |  |  |  |  |  |  |
| nisms such as intrusion detection systems (IDS) or malware | downloading the latest vulnerable release (v1.2.7) from the |  |  |  |  |  |  |
| classifiers. | upstream repository. | Data Processor | also extracts the CVE |  |  |  |  |

---

## Page 18

| CWE-IDs | # CVEs | PoC Available | No PoC |  |  |
| --- | --- | --- | --- | --- | --- |
| Reprod | Failed | Reprod | Failed |  |  |
| CWE-400 | 13 | 5 | 1 | 6 | 1 |
| CWE-IDs | # CVEs | PoC Available | No PoC |  |  |
| Reprod | Failed | Reprod | Failed |  |  |
| CWE-285 | 4 | 0 | 1 | 0 | 3 |
| CWE-209 | 3 | 0 | 2 | 0 | 1 |
| CWE-269 | 2 | 1 | 1 | 0 | 0 |
| CWE-287 | 2 | 0 | 0 | 0 | 2 |
| CWE-IDs | # CVEs | PoC Available | No PoC |  |  |
| Reprod | Failed | Reprod | Failed |  |  |
| No-ID | 7 | 0 | 0 | 5 | 2 |
| CWE-122 | 3 | 0 | 0 | 3 | 0 |
| CWE-400 | 2 | 0 | 0 | 1 | 1 |
| CWE-416 | 2 | 0 | 0 | 0 | 2 |
| CWE-863 | 2 | 0 | 0 | 0 | 2 |

Table 13: Top CWEs reproduced in OS/Runtime projects.

| Reprod | Failed | Reprod | Failed |  |  |
| --- | --- | --- | --- | --- | --- |
| CWE-122 | 4 | 0 | 0 | 1 | 3 |
| CWE-416 | 4 | 0 | 0 | 2 | 2 |
| CWE-22 | 2 | 0 | 2 | 0 | 0 |
| CWE-20 | 2 | 0 | 1 | 0 | 1 |

Table 14: Top CWEs reproduced in Desktop App projects.

| CWE-IDs | # CVEs | PoC Available | No PoC |  |  |
| --- | --- | --- | --- | --- | --- |
| Reprod | Failed | Reprod | Failed |  |  |
| CWE-116 | 2 | 0 | 0 | 1 | 1 |
| CWE-147 | 2 | 0 | 0 | 1 | 1 |

Table 15: Top CWEs reproduced in CLI Tool/Utility projects.

| Reprod | Failed | Reprod | Failed |  |  |
| --- | --- | --- | --- | --- | --- |
| CWE-532 | 2 | 0 | 0 | 1 | 1 |
| CWE-327 | 1 | 0 | 0 | 1 | 0 |

Table 17: Top CWEs reproduced in MobileApp/SDK projects.

| CWE-IDs | # CVEs | PoC Available | No PoC |  |  |
| --- | --- | --- | --- | --- | --- |
| Reprod | Failed | Reprod | Failed |  |  |
| CWE-200 | 4 | 1 | 0 | 1 | 2 |
| CWE-416 | 3 | 0 | 0 | 1 | 2 |
| CWE-639 | 2 | 1 | 0 | 0 | 1 |
| CWE-IDs | # CVEs | PoC Available | No PoC |  |  |
| Reprod | Failed | Reprod | Failed |  |  |
| CWE-918 | 3 | 0 | 2 | 0 | 1 |

18

| CWE-79 | 33 | 9 | 6 | 12 | 6 | CWE-IDs | # CVEs | PoC Available | No PoC |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CWE-1333 | 15 | 8 | 1 | 4 | 2 | Reprod | Failed | Reprod | Failed |  |  |
| CWE-200 | 13 | 9 | 0 | 1 | 3 | CWE-670 | 3 | 1 | 1 | 0 | 1 |
| CWE-770 | 13 | 5 | 0 | 5 | 3 | CWE-200 | 2 | 0 | 2 | 0 | 0 |
| CWE-22 | 8 | 3 | 1 | 2 | 2 | CWE-400 | 1 | 0 | 1 | 0 | 0 |
| Table 11: Top CWEs reproduced in Lib/Framework projects. | Table 16: Top CWEs reproduced in Blockch/Crypto projects. |  |  |  |  |  |  |  |  |  |  |
| CWE-200 | 3 | 0 | 0 | 1 | 2 | CWE-IDs | # CVEs | PoC Available | No PoC |  |  |
| Table 12: Top CWEs reproduced in Cloud/DevOps projects. | CWE-261 | 1 | 0 | 0 | 1 | 0 |  |  |  |  |  |
| CWE-IDs | # CVEs | PoC Available | No PoC | CWE-670 | 2 | 1 | 0 | 0 | 1 |  |  |
| CWE-79 | 7 | 0 | 6 | 0 | 1 | Table 18: Top CWEs reproduced in Emb/Network projects. |  |  |  |  |  |
| No-ID | 4 | 0 | 0 | 1 | 3 | CWE-863 | 2 | 0 | 0 | 2 | 0 |
| CWE-345 | 3 | 2 | 0 | 1 | 0 | CWE-23 | 1 | 1 | 0 | 0 | 0 |
| CWE-150 | 2 | 0 | 0 | 1 | 1 | Table 19: Top CWEs reproduced in Security/Server projects. |  |  |  |  |  |

---

## Page 19

| data, CWE information, patch commit, and bug bounty re- | sends an unauthenticated | DELETE | request to the vulnerable |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| port for the CVE. The | Knowledge Builder | then constructs a | endpoint, and prints the HTTP status code and response body. |  |  |  |  |
| structured CVE knowledge base summarizing the vulnerabil- | The exploit is intentionally minimal, containing no setup logic |  |  |  |  |  |  |
| ity as missing authorization (CWE-862) and localizing the | or auxiliary assumptions beyond network access to the API. |  |  |  |  |  |  |
| root cause to | v1/datasets/index.ts | , where the vulnerable | The generated exploit artifact is then evaluated by the | Ex- |  |  |  |
| delete handler deletes by dataset ID alone. The knowledge | ploit Critic | agent. The critic verifies that the exploit (i) tar- |  |  |  |  |  |
| base also records the upstream fix (adding authorization mid- | gets the correct vulnerable endpoint, (ii) directly triggers the |  |  |  |  |  |  |
| dleware and scoping deletion by | projectId | ), which becomes | missing-authorization flaw described in the CVE knowledge |  |  |  |  |
| the ground truth for later exploit and verifier synthesis. | base, (iii) does not rely on environmental shortcuts or fabri- |  |  |  |  |  |  |
| Builder | . | Given the vulnerable source tree and knowledge | cated behavior, and (iv) has been empirically validated against |  |  |  |  |
| base, the | Builder | reconstructs a runnable environment. The | the running vulnerable service. After confirming these prop- |  |  |  |  |
| Pre-Requisite Developer | agent inspects repository structure | erties, the critic accepts the exploit as a correct and faithful |  |  |  |  |  |
| and reads key configuration files (e.g., root | package.json | , | PoC. |  |  |  |  |
| backend | package.json | , backend | .env.example | , migration | CTF Verifier | . | To automatically confirm successful exploita- |
| runner | src/migrate.ts | ) to infer the required service stack: | tion of CVE-2024-5129, the | Verifier Developer | agent syn- |  |  |
| a Node.js/Koa backend backed by PostgreSQL and initialized | thesizes a CTF-style verifier that executes the exploit and |  |  |  |  |  |  |
| via SQL migrations under | packages/db | . | validates its effect against the reconstructed | Lunary | back- |  |  |
| The | Setup Developer | agent then provisions a real Post- | end. The verifier follows a fixed the following three-phase |  |  |  |  |
| greSQL 14 service inside the VM, configures credentials, | structure. |  |  |  |  |  |  |
| and generates a valid | .env | file pointing | DATABASE_URL | 1. In the | pre-setup | phase, it inserts a minimal but valid set |  |
| to the local database instance. All Node.js dependencies | of rows, i.e., organization, account, project, and dataset, |  |  |  |  |  |  |
| are installed via | npm install | , and database migrations | directly into the PostgreSQL database used by the run- |  |  |  |  |
| are | executed using | the | project’s | native | migration | run- | ning backend. A fresh dataset UUID is generated and |
| ner ( | npm run migrate:db | ), resulting in a fully initialized | recorded, ensuring that a concrete deletion target exists |  |  |  |  |
| schema. Finally, the backend is launched using | npm run dev | prior to exploitation. |  |  |  |  |  |
| and confirmed operational by observing successful database | 2. In | the | exploit | phase, the | verifier invokes | the | pre- |
| connectivity and a listening API server on port 3333. The | viously generated | exploit.py | script verbatim | via |  |  |  |
| Setup Critic | agent analyzes the execution logs of | Setup De- | subprocess.run | , passing the dataset UUID and the |  |  |  |
| veloper | and approves the build. | base URL | http://localhost:3333 | . The verifier itself |  |  |  |
| After environment reconstruction, the | Setup Critic | evalu- | performs no HTTP requests, ensuring that the exploit |  |  |  |  |
| ates the entire setup. The critic confirms that (i) the vulnerable | remains the sole trigger of the vulnerability. |  |  |  |  |  |  |
| code path is present and unchanged, (ii) a real PostgreSQL- | 3. In the | post-exploit | phase, the verifier re-queries the |  |  |  |  |
| backed Lunary backend is running, (iii) no dummy services | database to determine whether the dataset row with |  |  |  |  |  |  |
| or mocked endpoints were introduced, and (iv) the vulnerable | UUID still exists. If the row has been deleted, the veri- |  |  |  |  |  |  |
| DELETE /v1/datasets/:id | endpoint is reachable and re- | fier prints the flag | 3xploit66full | ; otherwise, it reports |  |  |  |
| sponds with HTTP 200 to unauthenticated requests. Based on | failure. Database access is implemented robustly, using |  |  |  |  |  |  |
| these checks, the critic accepts the project build as a genuine | psycopg2 | when available and falling back to the | psql |  |  |  |  |
| and exploitable reproduction target. | client if necessary. |  |  |  |  |  |  |
| Exploiter | . | The | Exploit Developer | agent begins by performing | During verification, earlier verifier iterations that relied |  |  |
| targeted code inspection to ground the exploit in the real im- | on mocked or stubbed HTTP servers were rejected by the |  |  |  |  |  |  |
| plementation. It reads the vulnerable dataset router source file | Verifier Critic | agent. The final accepted verifier operates ex- |  |  |  |  |  |
| and confirms that the | datasets.delete("/:id") | handler | clusively on the real Node.js / Koa backend and PostgreSQL |  |  |  |  |
| executes an unscoped SQL deletion without any authentica- | instance and performs a direct state-based validation. The |  |  |  |  |  |  |
| tion or authorization middleware. It also inspects backend | Flag Checker | successfully executes the verifier, observes flag |  |  |  |  |  |
| configuration files to verify the correct runtime entry points | emission, and the | Verifier Critic | confirms the verifier as a |  |  |  |  |
| and dependencies. To validate exploitability in practice, the | correct and faithful reproduction of the CVE. |  |  |  |  |  |  |

exploiter launches the backend and issues unauthenticated

DELETE requests against /v1/datasets/<uuid> using both

ad-hoc Python test scripts and raw HTTP calls. A randomly

generated UUID is sufficient to elicit an unconditional HTTP

200 response, confirming that no permission checks or project

scoping are enforced. Based on this confirmation, the ex-

ploiter generates a standalone PoC exploit.py script. The

19

Storing Artifacts and Metadata . After the successful verifi-

cation, CVE-G ENIE stores the VM snapshot with running

Lunary server. Moreover, it stores exploit and verifier scripts,

agent logs, and metadata of the reproduction run. Overall,

this reproduction run of CVE-2024-5129 cost $1.68 and 20

minutes. See artifacts here 5 in open-source dataset.

script accepts a dataset UUID (and an optional base URL), 5 https://github.com/BUseclab/cve-genie/tree/main/

---

## Page 20

References [8] Dong Chen, Shaoxin Lin, Muhan Zeng, Daoguang Zan,

laka Gunasekara, Shajith Ikbal, Sachindra Joshi, Hima

Karanam, Vineet Kumar, Asim Munawar, Sumit Nee-

vulnerabilities live in the code? a Large-Scale empiri-

Lorenzo Cavallaro, and Konrad Rieck. Dos and don’ts of

Security Symposium , 2022.

[6] Bandit. Bandit Documentation.

and Data Analytics in Software Engineering , PROMISE

2021, page 30–39, New York, NY, USA, 2021. Associa-

tion for Computing Machinery.

20

Jian-Gang Wang, Anton Cheshkov, Jun Sun, Hao Yu,

agent and task graphs, 2024.

Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain,

Dario Amodei, Sam McCandlish, Ilya Sutskever, and

Symposium on Research in Attacks, Intrusions and De-

[12] Yinlin Deng, Chunqiu Steven Xia, Haoran Peng,

for Computing Machinery.

[13] Yangruibo Ding, Yanjun Fu, Omniyyah Ibrahim, Chawin

[14] D Dittrich and E Kenneally. The Menlo Report: Ethi-

cal Principles Guiding Information and Communication

Technology Research. Technical report, U.S. Depart-

| [1] Ibrahim Abdelaziz, Kinjal Basu, Mayank Agarwal, Sad- | Guoliang Dong, Artem Aliev, Jie Wang, Xiao Cheng, |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| hana Kumaravel, Matthew Stallone, Rameswar Panda, | Guangtai Liang, Yuchi Ma, Pan Bian, Tao Xie, and |  |  |  |  |
| Yara Rizk, G P Shrivatsa Bhargav, Maxwell Crouse, Chu- | Qianxiang Wang. | Coder: Issue resolving with multi- |  |  |  |
| lam, Dinesh Raghu, Udit Sharma, Adriana Meza Soria, | [9] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, |  |  |  |  |
| Dheeraj Sreedhar, Praveen Venkateswaran, Merve Un- | Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri |  |  |  |  |
| uvar, David Daniel Cox, Salim Roukos, Luis A. Las- | Edwards, Yuri Burda, Nicholas Joseph, Greg Brock- |  |  |  |  |
| tras, and Pavan Kapanipathi. Granite-function calling | man, Alex Ray, Raul Puri, Gretchen Krueger, Michael |  |  |  |  |
| model: Introducing function calling abilities via multi- | Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, |  |  |  |  |
| task learning of granular tasks. In Franck Dernoncourt, | Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, |  |  |  |  |
| Daniel Preo¸ | tiuc-Pietro, and Anastasia Shimorina, edi- | Alethea Power, Lukasz Kaiser, Mohammad Bavarian, |  |  |  |
| tors, | Proceedings of the 2024 Conference on Empiri- | Clemens Winter, Philippe Tillet, Felipe Petroski Such, |  |  |  |
| cal Methods in Natural Language Processing: Industry | Dave Cummings, Matthias Plappert, Fotios Chantzis, |  |  |  |  |
| Track | , pages 1131–1139, Miami, Florida, US, November | Elizabeth Barnes, Ariel Herbert-Voss, William Heb- |  |  |  |
| 2024. Association for Computational Linguistics. | gen Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie |  |  |  |  |
| [2] Janice Ahn, Rishu Verma, Renze Lou, Di Liu, Rui | William Saunders, Christopher Hesse, Andrew N. Carr, |  |  |  |  |
| Zhang, and Wenpeng Yin. | Large language models | Jan Leike, Josh Achiam, Vedant Misra, Evan Morikawa, |  |  |  |
| for mathematical reasoning: Progresses and challenges, | Alec Radford, Matthew Knight, Miles Brundage, Mira |  |  |  |  |
| 2024. | Murati, Katie Mayer, Peter Welinder, Bob McGrew, |  |  |  |  |
| [3] Nikolaos Alexopoulos, Manuel Brack, Jan Philipp Wag- | Wojciech Zaremba. Evaluating Large Language Models |  |  |  |  |
| ner, Tim Grube, and Max Mühlhäuser. How long do | Trained on Code, July 2021. arXiv:2107.03374 [cs]. |  |  |  |  |
| cal measurement study on FOSS vulnerability lifetimes. | [10] Yizheng Chen, Zhoujie Ding, Lamya Alowain, Xinyun |  |  |  |  |
| In | 31st USENIX Security Symposium (USENIX Secu- | Chen, and David Wagner. Diversevul: A new vulnerable |  |  |  |
| rity 22) | , pages 359–376, Boston, MA, August 2022. | source code dataset for deep learning based vulnerabil- |  |  |  |
| USENIX Association. | ity detection. In | Proceedings of the 26th International |  |  |  |
| [4] Daniel Arp, Erwin Quiring, Feargus Pendlebury, Alexan- | fenses | , RAID ’23, page 654–668, New York, NY, USA, |  |  |  |
| der Warnecke, Fabio Pierazzi, Christian Wressnegger, | 2023. Association for Computing Machinery. |  |  |  |  |
| machine learning in computer security. In | 31st USENIX | [11] DARPA. The cyber grand challenge, 2016. |  |  |  |
| [5] Jacob Austin, Augustus Odena, Maxwell Nye, Maarten | Chenyuan Yang, and Lingming Zhang. Large Language |  |  |  |  |
| Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, | Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning |  |  |  |  |
| Carrie Cai, Michael Terry, Quoc Le, and Charles Sut- | Libraries via Large Language Models. In | Proceedings |  |  |  |
| ton. | Program Synthesis with Large Language Mod- | of the 32nd ACM SIGSOFT International Symposium |  |  |  |
| els. | arXiv:2108.07732 [cs] | , August 2021. | arXiv: | on Software Testing and Analysis | , ISSTA 2023, pages |
| 2108.07732. | 423–435, New York, NY, USA, July 2023. Association |  |  |  |  |
| [7] Guru Bhandari, Amara Naseer, and Leon Moonen. Cve- | Sitawarin, Xinyun Chen, Basel Alomair, David Wagner, |  |  |  |  |
| fixes: automated collection of vulnerabilities and their | Baishakhi Ray, and Yizheng Chen. Vulnerability Detec- |  |  |  |  |
| fixes from open-source software. | In | Proceedings of | tion with Code Language Models: How Far Are We?, |  |  |
| the 17th International Conference on Predictive Models | July 2024. arXiv:2403.18624 [cs]. |  |  |  |  |
| results/reproduced_cves/CVE-2024-5129 | ment of Homeland Security, August 2012. |  |  |  |  |

---

## Page 21

| [15] Jiahao Fan, Yi Li, Shaohua Wang, and Tien N. Nguyen. | [26] Haolin Jin, Linghan Huang, Haipeng Cai, Jun Yan, |  |
| --- | --- | --- |
| A c/c++ code vulnerability dataset with code changes | Bo Li, and Huaming Chen. From LLMs to LLM-based |  |
| and cve summaries. In | Proceedings of the 17th Inter- | Agents for Software Engineering: A Survey of Current, |
| national Conference on Mining Software Repositories | , | Challenges and Future, August 2024. arXiv:2408.02479 |
| MSR ’20, page 508–512, New York, NY, USA, 2020. | [cs]. |  |

Association for Computing Machinery.

[17] Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming

Zhou, and Jian Yin. UniXcoder: Unified cross-modal

[18] Wenbo Guo, Yujin Potter, Tianneng Shi, Zhun Wang,

[19] Hazim Hanif and Sergio Maffeis. Vulberta: Simpli-

fied source code pre-training for vulnerability detection.

[20] Ahmad Hazimeh, Adrian Herrera, and Mathias Payer.

Magma: A ground-truth fuzzing benchmark. Proceed-

ings of the ACM on Measurement and Analysis of Com-

[21] Jingxuan He and Martin Vechev. Large language models

for code: Security hardening and adversarial testing. In

Proceedings of the 2023 ACM SIGSAC Conference on

Computer and Communications Security , CCS ’23, page

[22] Junda He, Christoph Treude, and David Lo. LLM-Based

[24] Nan Jiang, Kevin Liu, Thibaud Lutellier, and Lin Tan.

Impact of Code Language Models on Automated Pro-

gram Repair. In IEEE/ACM 45th International Confer-

IEEE Computer Society, May 2023.

21

[27] Guohao Li, Hasan Hammoud, Hani Itani, Dmitrii

ume 36, pages 51991–52008. Curran Associates, Inc.,

2023.

preprint arXiv:2502.02747 , 2025.

Transactions on Dependable and Secure Computing ,

2022.

ecker: A deep learning-based system for vulnerability

detection. Proceedings of Network and Distributed Sys-

tem Security Symposium , 2018.

Xiang. Poster: Vulnerability discovery with function

representation learning from unlabeled projects. In Pro-

ceedings of ACM SIGSAC Conference on Computer and

Communications Security , 2017.

software repository?, 2024.

Wang, Yan Shoshitaishvili, Adam Doupé, Hammond

Pearce, and Brendan Dolan-Gavitt. Arvo: Atlas of repro-

ducible vulnerabilities for open source software, 2024.

[36] Yisroel Mirsky, George Macon, Michael Brown, Carter

| [16] Michael | Fu, Chakkrit | Kla | Tantithamthavorn, Van | Khizbullin, and Bernard Ghanem. CAMEL: Commu- |
| --- | --- | --- | --- | --- |
| Nguyen, and Trung Le. Chatgpt for vulnerability de- | nicative Agents for "Mind" Exploration of Large Lan- |  |  |  |
| tection, classification, and repair: How far are we? In | guage Model Society. In A. Oh, T. Naumann, A. Glober- |  |  |  |
| 2023 30th Asia-Pacific Software Engineering Confer- | son, K. Saenko, M. Hardt, and S. Levine, editors, | Ad- |  |  |
| ence (APSEC) | , pages 632–636, 2023. | vances in Neural Information Processing Systems | , vol- |  |
| pre-training for code representation. In | Proceedings of | [28] Hongwei Li, Yuheng Tang, Shiqi Wang, and Wenbo |  |  |
| the 60th Annual Meeting of the Association for Compu- | Guo. Patchpilot: A cost-efficient software engineering |  |  |  |
| tational Linguistics | , May 2022. | agent with early attempts on formal verification. | arXiv |  |
| Andy Zhang, and Dawn Song. | Frontier ai’s im- | [29] Zhen Li, Deqing Zou, Shouhuai Xu, Hai Jin, Yawei Zhu, |  |  |
| pact on the cybersecurity landscape. | arXiv preprint | and Zhaoxuan Chen. Sysevr: A framework for using |  |  |
| arXiv:2504.05408 | , 2025. | deep learning to detect software vulnerabilities. | IEEE |  |
| In | International Joint Conference on Neural Networks | [30] Zhen Li, Deqing Zou, Shouhuai Xu, Xinyu Ou, Hai Jin, |  |  |
| (IJCNN) | , 2022. | Sujuan Wang, Zhijun Deng, and Yuyi Zhong. Vuldeep- |  |  |
| puting Systems | , 2020. | [31] Guanjun Lin, Jun Zhang, Wei Luo, Lei Pan, and Yang |  |  |
| 1865–1879, New York, NY, USA, 2023. Association for | [32] Yingwei Ma, Qingping Yang, Rongyu Cao, Binhua Li, |  |  |  |
| Computing Machinery. | Fei Huang, and Yongbin Li. How to understand whole |  |  |  |
| Multi-Agent Systems for Software Engineering: Litera- | [33] Rohin Manvi, Anikait Singh, and Stefano Ermon. Adap- |  |  |  |
| ture Review, Vision and the Road Ahead. | ACM Trans. | tive Inference-Time Compute: LLMs Can Predict if |  |  |
| Softw. Eng. Methodol. | , January 2025. | They Can Do Better, Even Mid-Generation, 2024. |  |  |
| [23] Infer. A tool to detect bugs in Java and C/C++/Objective- | [34] Xiang Mei, Pulkit Singh Singaria, Jordi Del Castillo, |  |  |  |
| C code before it ships. | Haoran Xi, Abdelouahab, Benchikh, Tiffany Bao, Ruoyu |  |  |  |
| ence on Software Engineering (ICSE) | , pages 1430–1442. | [35] Metasploit. RAPID7 metasploit. |  |  |
| [25] Carlos | E. | Jimenez, John | Yang, Alexander Wettig, | Yagemann, Matthew Pruett, Evan Downing, Sukarno |
| Shunyu Yao, Kexin Pei, Ofir Press, and Karthik R. | Mertoguno, and Wenke Lee. VulChecker: Graph-based |  |  |  |
| Narasimhan. Swe-bench: Can language models resolve | vulnerability localization in source code. | In | 32nd |  |
| real-world github issues? In | ICLR | , 2024. | USENIX Security Symposium | , 2023. |

---

## Page 22

| [37] MITRE. 2024 CWE Top 25 Most Dangerous Software | [48] Akond Rahman, Chris Parnin, and Laurie Williams. The |
| --- | --- |
| Weaknesses. | seven sins: Security smells in infrastructure as code |

Hu, Xinyu Xing, Bing Mao, and Gang Wang. Under-

August 2018. USENIX Association.

[39] Anh The Nguyen, Triet Huynh Minh Le, and M. Ali

Babar. Automated code-centric software vulnerabil-

ity assessment: How far are we? an empirical study in

[40] Georgios Nikitopoulos, Konstantina Dritsa, Panos Louri-

das, and Dimitris Mitropoulos. Crossvul: a cross-

language vulnerability dataset with commit data. In

Proceedings of the 29th ACM Joint Meeting on Euro-

pean Software Engineering Conference and Symposium

on the Foundations of Software Engineering , ESEC/FSE

2021, page 1565–1569, New York, NY, USA, 2021. As-

sociation for Computing Machinery.

[42] NVD. NVD - Home.

[44] OWASP. Source Code Analysis Tools.

[45] Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Mered-

ith Ringel Morris, Percy Liang, and Michael S. Bern-

stein. Generative Agents: Interactive Simulacra of Hu-

man Behavior. In Proceedings of the 36th Annual ACM

Symposium on User Interface Software and Technology ,

UIST ’23, pages 1–22, New York, NY, USA, October

2023. Association for Computing Machinery.

[46] Hammond Pearce, Benjamin Tan, Baleegh Ahmad,

1207.

cessing for Programming (NLP4Prog) , 2021.

22

scripts. In IEEE/ACM 41st International Conference on

[50] Niklas Risse and Marcel Böhme. Top score on the

wrong exam: On benchmarking in machine learning for

vulnerability detection, 2024.

[52] Rebecca Russell, Louis Kim, Lei Hamilton, Tomo La-

zovich, Jacob Harer, Onur Ozdemir, Paul Ellingwood,

and Marc McConley. Automated vulnerability detection

in source code using deep representation learning. In

17th IEEE International Conference on Machine Learn-

ing and Applications (ICMLA) , 2018.

[53] Yashar Talebirad and Amirhossein Nadiri. Multi-Agent

Agents, June 2023. arXiv:2306.03314 [cs].

[54] Saad Ullah, Mingji Han, Saurabh Pujar, Hammond

sium on Security and Privacy (SP) , pages 862–880, Los

Alamitos, CA, USA, May 2024. IEEE Computer Soci-

ety.

[55] Shengye Wan, Cyrus Nikolaidis, Daniel Song, David

Molnar, James Crnkovich, Jayson Grace, Manish Bhatt,

Sahana Chennabasappa, Spencer Whitman, Stephanie

Ding, et al. Cyberseceval 3: Advancing the evaluation

of cybersecurity risks and capabilities in large language

models. arXiv preprint arXiv:2408.01605 , 2024.

[57] Chunqiu Steven Xia, Yuxiang Wei, and Lingming Zhang.

IEEE.

| [38] Dongliang Mu, Alejandro Cuevas, Limin Yang, Hang | Software Engineering (ICSE) | , 2019. |  |
| --- | --- | --- | --- |
| standing the Reproducibility of Crowd-reported Security | [49] Niklas Risse and Marcel Böhme. Limits of Machine |  |  |
| Vulnerabilities. In | 27th USENIX Security Symposium | Learning for Automatic Vulnerability Detection. | arXiv |
| (USENIX Security 18) | , pages 919–936, Baltimore, MD, | e-prints | , page arXiv:2306.17193, June 2023. |
| c/c++. In | Proceedings of the 18th ACM/IEEE Interna- | [51] Niklas Risse and Marcel Böhme. | Top score on the |
| tional Symposium on Empirical Software Engineering | wrong exam: On benchmarking in machine learning for |  |  |
| and Measurement | , ESEM ’24, page 72–83, 2024. | vulnerability detection, 2024. |  |
| [41] NIST. SARD. | Collaboration: Harnessing the Power of Intelligent LLM |  |  |
| [43] OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal, | Pearce, Ayse Coskun, and Gianluca Stringhini. LLMs |  |  |
| Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, | Cannot Reliably Identify and Reason About Security |  |  |
| Diogo Almeida, Janko Altenschmidt, Sam Altman, and | Vulnerabilities (Yet?): A Comprehensive Evaluation, |  |  |
| Shyamal Anadkat. Gpt-4 technical report, 2024. | Framework, and Benchmarks. | In | 2024 IEEE Sympo- |
| Ramesh Karri, and Brendan Dolan-Gavitt. Examining | [56] Laura Wartschinski, Yannic Noller, Thomas Vogel, Timo |  |  |
| Zero-Shot Vulnerability Repair with Large Language | Kehrer, and Lars Grunske. Vudenc: Vulnerability detec- |  |  |
| Models. In | 2023 IEEE Symposium on Security and Pri- | tion with deep learning on a natural codebase for python. |  |
| vacy (SP) | , pages 2339–2356, May 2023. ISSN: 2375- | Inf. Softw. Technol. | , 144(C), April 2022. |
| [47] Long Phan, Hieu Tran, Daniel Le, Hieu Nguyen, James | Automated Program Repair in the Era of Large Pre- |  |  |
| Annibal, Alec Peltekian, and Yanfang Ye. | CoTexT: | trained Language Models. In | 2023 IEEE/ACM 45th In- |
| Multi-task learning with code-text transformer. In | Pro- | ternational Conference on Software Engineering (ICSE) | , |
| ceedings of the 1st Workshop on Natural Language Pro- | pages 1482–1494, Melbourne, Australia, May 2023. |  |  |

---

## Page 23

[58] Fabian Yamaguchi, Nico Golde, Daniel Arp, and Konrad

Rieck. Modeling and discovering vulnerabilities with

code property graphs. In IEEE Symposium on Security

and Privacy , 2014.

[59] Yu Yang, Yuzhou Nie, Zhun Wang, Yuheng Tang, Wenbo

Guo, Bo Li, and Dawn Song. Seccodeplt: A unified

platform for evaluating the security of code genai. arXiv

preprint arXiv:2410.11096 , 2024.

[60] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak

Shafran, Karthik Narasimhan, and Yuan Cao. React:

Synergizing reasoning and acting in language models.

arXiv preprint arXiv:2210.03629 , 2022.

[61] Zheng Yu, Ziyi Guo, Yuhang Wu, Jiahao Yu, Meng Xu,

Dongliang Mu, Yan Chen, and Xinyu Xing. Patchagent:

A practical program repair agent mimicking human ex-

pertise.

[62] Daoguang Zan, Zhirong Huang, Ailun Yu, Shaoxin Lin,

Yifan Shi, Wei Liu, Dong Chen, Zongshuai Qi, Hao Yu,

Lei Yu, Dezhi Ran, Muhan Zeng, Bo Shen, Pan Bian,

Guangtai Liang, Bei Guan, Pengjie Huang, Tao Xie,

Yongji Wang, and Qianxiang Wang. Swe-bench-java: A

github issue resolving benchmark for java, 2024.

[63] Yuntong Zhang, Jiawei Wang, Dominic Berzin, Martin

Mirchev, Dongge Liu, Abhishek Arya, Oliver Chang,

and Abhik Roychoudhury. Fixing security vulnerabili-

ties with ai in oss-fuzz, 2024.

[64] Yunhui Zheng, Saurabh Pujar, Burn Lewis, Luca Bu-

ratti, Edward Epstein, Bo Yang, Jim Laredo, Alessandro

Morari, and Zhong Su. D2a: A dataset built for ai-based

vulnerability detection methods using differential analy-

sis. In 2021 IEEE/ACM 43rd International Conference

on Software Engineering: Software Engineering in Prac-

tice (ICSE-SEIP) , 2021.

[65] Yaqin Zhou, Shangqing Liu, Jingkai Siow, Xiaoning Du,

and Yang Liu. Devign: Effective vulnerability identifi-

cation by learning comprehensive program semantics

via graph neural networks. In Advances in Neural Infor-

mation Processing Systems , 2019.

[66] Yuxuan Zhu, Antony Kellermann, Dylan Bowman,

Philip Li, Akul Gupta, Adarsh Danda, Richard Fang,

Conner Jensen, Eric Ihli, Jason Benn, Jet Geronimo, Avi

Dhir, Sudhit Rao, Kaicheng Yu, Twm Stone, and Daniel

Kang. Cve-bench: A benchmark for ai agents’ ability to

exploit real-world web application vulnerabilities, 2025.

23

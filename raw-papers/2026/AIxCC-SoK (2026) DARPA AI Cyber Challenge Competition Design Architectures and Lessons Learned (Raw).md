---
title: "SoK: DARPA's AI Cyber Challenge (AIxCC): Competition Design, Architectures, and Lessons Learned"
author: "Cen Zhang; Younggi Park; Fabian Fleischer; Yu-Fu Fu; Jiho Kim; Dongkwan Kim; Youngjoon Kim; Qingxiao Xu; Andrew Chin; Ze Sheng; Hanqing Zhao; Michael Pelican; David J. Musliner; Jeff Huang; Jon Silliman; Mikel Mcdaniel; Jefferson Casavant; Isaac Goldthwaite; Nicholas Vidovich; Matthew Lehman; Taesoo Kim"
creator: "arXiv GenPDF (tex2pdf:8def8d8)"
pages: 20
---

# SoK: DARPA's AI Cyber Challenge (AIxCC): Competition Design, Architectures, and Lessons Learned

> **作者**：Cen Zhang; Younggi Park; Fabian Fleischer; Yu-Fu Fu; Jiho Kim; Dongkwan Kim; Youngjoon Kim; Qingxiao Xu; Andrew Chin; Ze Sheng; Hanqing Zhao; Michael Pelican; David J. Musliner; Jeff Huang; Jon Silliman; Mikel Mcdaniel; Jefferson Casavant; Isaac Goldthwaite; Nicholas Vidovich; Matthew Lehman; Taesoo Kim
> **總頁數**：20 頁

---

## Page 1

SoK: DARPA’s AI Cyber Challenge (AIxCC):

Competition Design, Architectures, and Lessons Learned

| † | ∗ | § | ♮ | † | † | † | ∗ | § |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cen Zhang | Younggi Park | Fabian Fleischer | Yu-Fu Fu | Jiho Kim | Dongkwan Kim |  |  |  |
| † | ‡ | † | ‡ | † |  |  |  |  |

Youngjoon Kim Qingxiao Xu Andrew Chin Ze Sheng Hanqing Zhao

¶ ¶ ‡ ∥ ∥

Michael Pelican David J. Musliner Jeff Huang Jon Silliman Mikel Mcdaniel

∥ ∥ ∥ ∥ † ∗

Jefferson Casavant Isaac Goldthwaite Nicholas Vidovich Matthew Lehman Taesoo Kim

† ‡ ♮

Georgia Institute of Technology , Texas A&M University , Independent Researcher ,

¶ ∥ ∗

Smart Information Flow Technologies (SIFT) , Kudu Dynamics , Microsoft

Abstract emerged from this large-scale competition. Such an analysis

DARPA’s AI Cyber Challenge (AIxCC, 2023–2025) is the

largest competition to date for building fully autonomous Cy-

ber Reasoning Systems (CRSs) that leverage recent advances

in AI—particularly large language models (LLMs)—to dis-

cover and remediate vulnerabilities in real-world open-source

software. This paper presents the first systematic analysis of

AIxCC. Drawing on design documents, source code, execu-

tion traces, and discussions with organizers and all finalist

teams, we examine the competition’s structure and key design

decisions, characterize the architectural approaches of finalist

CRSs, and analyze competition results beyond the final score-

board. Our analysis reveals the factors that truly drove CRS

performance, identifies genuine technical advances achieved

by teams, and exposes limitations that remain open for future

research. We conclude with lessons for organizing future com-

petitions and broader insights toward deploying autonomous

CRSs in practice.

1 Introduction

Open-source software (OSS) underpins critical infrastruc-

mains challenging. DARPA’s AI Cyber Challenge (AIxCC,

autonomous Cyber Reasoning Systems (CRSs) that lever-

age large language models (LLMs) to discover and patch

vulnerabilities in real-world C and Java projects. The final

competition in August 2025 represents the largest-scale eval-

critical infrastructure software, each equipped with $85K in

has examined AIxCC’s design rationale, the technical ap-

proaches employed by participating teams, or the lessons that

would benefit multiple communities: competition organizers

designing future challenges, security researchers developing

advanced vulnerability detection and patching techniques, and

practitioners seeking AI-driven security solutions.

To fill this gap, we conducted a systematic study of the final

competition, drawing on multiple primary sources: all seven

finalist CRS codebases and whitepapers, the complete com-

petition database (challenges, results, and execution traces)

from organizers, and discussions with organizers and all fi-

nalist teams. Our analysis examines AIxCC from three per-

spectives: the design decisions that shaped the competition,

the architectural and technical choices made by finalist teams,

and competition results and their implications. Specifically,

we address the following research questions:

• RQ1: How is AIxCC designed to guide and evaluate

AI-driven vulnerability discovery and patching?

• RQ2: What architectural and technical approaches did

finalist teams employ?

• RQ3: What insights emerge from the results?

• A systematic analysis of AIxCC’s competition design,

covering design and scoring principles, challenge con-

struction, and execution guidelines.

for technical insights.

• Lessons on translating competition outcomes to industry

| ture, yet scaling vulnerability discovery and remediation re- | • | RQ4: | What are the lessons and future directions? |
| --- | --- | --- | --- |
| 2023–2025) addresses this by challenging teams to build fully | Our work makes the following contributions: |  |  |
| uation of autonomous vulnerability analysis to date: around | • A taxonomy of CRS architectures and techniques across |  |  |
| arXiv:2602.07666v5 [cs.CR] 2 Aug 2026 | 143 hours of fully autonomous operation, CRSs from seven | all seven finalist teams, spanning vulnerability discovery, |  |
| finalist teams analyzed 53 challenge projects derived from | patching, report triage, and bundling. |  |  |
| cloud compute and $50K in LLM API credits. | • In-depth result analysis that reveals the true factors be- |  |  |
| Despite the competition’s completion, no systematic study | hind CRS performance, with per-vulnerability analysis |  |  |
| § | Work primarily conducted at Georgia Institute of Technology. | deployment and research, plus future directions. |  |

---

## Page 2

All data and artifacts will be released publicly upon accep- GitHub Team-Hosted Clouds (isolated network)

tance (some subject to DARPA’s timeline; see §10). Challenge Projects Challenge Projects Challenge Projects Team CRSs Team CRSs Team CRSs

AIxCC. AIxCC [20] (2023–2025) is a DARPA/ARPA-H

competition to advance fully autonomous vulnerability dis-

covery and remediation for open-source software, in collabo-

ration with AI providers (Anthropic, Google, Microsoft, Ope-

CON. From 42 entrants, seven teams advanced through the

143 hours across seven phases (P1–P7), during which the fi-

nalists deployed CRSs autonomously to analyze 53 challenge

Comparison with CGC. AIxCC is a spiritual successor to

DARPA’s Cyber Grand Challenge (CGC, 2014–2016) [19] af-

ter a near-decade gap; each marks a pivotal inflection point for

while AIxCC targets vulnerability discovery and remediation

Acronyms. Appendix B provides the mappings and rules for

abbreviations used in this paper.

Our Methodology. ➀ Competition design (§3): we extract

each team’s profile is grounded primarily in the enabled func-

validated the resulting profile. Team whitepapers, blogs, and

a structured questionnaire serve as supplementary sources.

The questionnaire covers common competition reflections

email and the others through dedicated meetings. ➂ Outcome

analysis (§7): per-team outcomes are derived from the offi-

additionally cross-validated by at least two security experts,

opment workflows: the final competition embeds in GitHub,

Pull Request ② Full Scan PoV

Release Delta Scan SARIF

① Security Alert

SARIF Review ③ Bundle

Competition API Scoring System

Organizer-Hosted Cloud

• Full Scan : when developers tag a new release, detect and

patch vulnerabilities across the full codebase.

• Report Synthesis : after analysis, correlate all above find-

ings into per-vulnerability reports.

• Patch ( [ 3 , 6 ] pts): a fix that resolves the vulnerability

while preserving functionality.

SARIF report is valid.

weight reflects how much developer time and effort it saves

(or wastes, when wrong): ➀ Patch scores high since it pro-

lower since it only proves the bug exists; ➂ SARIF scores

2 SARIF (Static Analysis Results Interchange Format) [44] is a JSON

| 2 | Background: AIxCC as Competition | Patch |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nAI), Linux Foundation, OpenSSF, Black Hat USA, and DEF | Legend: | Webhook Event | Challenge | Submission |  |  |  |  |  |  |  |
| semifinal (ASC, DEF CON 2024) [18] to the final (AFC, DEF | Figure 1: Final competition workflow: | ➀ | triggered by web- |  |  |  |  |  |  |  |  |
| CON 2025), the focus of this paper. | 1 | The final ran for around | hook, | ➁ | challenge dispatched, | ➂ | result submitted. |  |  |  |  |
| projects (CPs) in C and Java under $85,000 in Azure compute | with each CRS capability triggered by an actual development |  |  |  |  |  |  |  |  |  |  |
| and $50,000 in LLM API credits per team. All finalist CRSs, | event. Figure 1 shows the workflow. The four CRS capabili- |  |  |  |  |  |  |  |  |  |  |
| challenges, and infrastructure are being open-sourced [21]. | ties each address a real development moment: |  |  |  |  |  |  |  |  |  |  |
| fully autonomous CRSs. The two differ in two ways. | ➀ | Scope | : | • | Delta Scan | : when new code is merged via pull requests, |  |  |  |  |  |
| CGC focused on binary exploitation on DECREE OS [63], | conduct targeted analysis on the incremental changes. |  |  |  |  |  |  |  |  |  |  |
| for real-world OSS in C and Java. | ➁ | AI emphasis | : AIxCC | • | SARIF Review | : when developers receive static-analyzer |  |  |  |  |  |
| provides LLM infrastructure from AI providers, highlighting | security alerts in SARIF | 2 | format, classify each as valid |  |  |  |  |  |  |  |  |
| LLM-based techniques unavailable during CGC. | (a real vulnerability) or invalid. |  |  |  |  |  |  |  |  |  |  |
| the design rationale from the organizers’ reflection docu- | Organizers send two kinds of challenges (Full Scan or Delta |  |  |  |  |  |  |  |  |  |  |
| ments and whitepapers, refined through online discussions | Scan), some accompanied by SARIF broadcasts for review. A |  |  |  |  |  |  |  |  |  |  |
| and confirmed by them. | ➁ | CRS technique taxonomy | (§5, §6): | CRS may submit up to four kinds of evidence per challenge: |  |  |  |  |  |  |  |
| tionalities of its submission-version code; at least two secu- | • | Proof of Vulnerability (PoV) | ( | [ | 1 | , | 2 | ] | pts): an input that |  |  |
| rity experts independently reviewed each codebase and cross- | triggers abnormal execution ( | e | . | g | ., a crash). |  |  |  |  |  |  |
| and team-specific technical designs; one team responded by | • | SARIF assessment | ( | [ | 0 | . | 5 | , | 1 | ] | pt): a judgment on whether a |
| cial competition database (logs, traces, scores, etc.), challenge | • | Bundle | ( | [ | − | 7 | , | 7 | ] | pts): a grouping that links related find- |  |
| code, and vulnerability data; patch outcome labels (§7.2) are | ings for the same vulnerability. |  |  |  |  |  |  |  |  |  |  |
| as with the taxonomy. | Scoring: Defining a “Good CRS”. | Each submission’s |  |  |  |  |  |  |  |  |  |
| 3 | Competition Design | vides a direct solution for the security issue; | ➁ | PoV scores |  |  |  |  |  |  |  |
| AIxCC grounds its CRS evaluation in real-world OSS devel- | lowest since it judges a statically-identified security issue; | ➃ |  |  |  |  |  |  |  |  |  |
| 1 | This artifact represents the authors’ own statements and does not consti- | format for static analysis tool output; each report identifies a potential vul- |  |  |  |  |  |  |  |  |  |
| tute an official DARPA statement. | nerability with file path, code region, description, and CWE classification. |  |  |  |  |  |  |  |  |  |  |

---

## Page 3

| Bundle scores both extremes, up to +7 for fully correct link- | Table 1: Overview of open-source repositories and challenge |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| age or a penalty for any incorrect, since correct linkage saves | projects (CPs) in the final. | □ | : full-mode; | ▲ | : delta-mode. | ∗ | 5 |
| the most triage effort and wrong linkage wastes the most. | unharnessed CPs are excluded: freertos-kernel, jt808, lwip, |  |  |  |  |  |  |
| Two further mechanisms reward fast and correct submis- | openssl, sms4j. | † | Averaged across CPs. |  |  |  |  |

sions. Time-decay grants full points for immediate submis-

reduction). See [9] for full scoring details.

a field where AI capability evolved rapidly. Perfecting the

nal corrected: ➀ the semifinal’s self-PoV requirement dis-

constrained sandbox.

Within the final. Beyond internal infrastructure testing, the

4 Challenge Projects

The final comprised 48 scored challenge projects (CPs) drawn

from 24 OSS-Fuzz [5] repositories, together containing 63

challenge project vulnerabilities (CPVs) (Table 1). Five ad-

ditional CPs lacked fuzzing harnesses and were excluded

from scoring. Organizers selected critical-infrastructure and

healthcare-critical OSS, onboarding new projects to OSS-

Fuzz where needed. To avoid AI training contamination, most

CPVs are hand-crafted synthetics inspired by historical N-day

issues, with a few genuine 0-days surfaced during challenge

Repositories. The 24 repositories (14 C and 10 Java) span di-

| freerdp | fp | 3 | ▲ | 2 | 7 | 457K |
| --- | --- | --- | --- | --- | --- | --- |
| libxml2 | lx | 1 | ▲ | 1 | 11 | 201K |

C

| mongoose | mg | 1 | □ | 3 | ▲ | 3 | 1 | 364K |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| shadowsocks-libev | ss | 1 | □ | 5 | 1 | 19K |  |  |
| systemd | sd | 1 | □ | 4 | 47 | 740K |  |  |
| dicoogle | dg | 1 | □ | 0 | 1 | 21K |  |  |

healthcare-

data-harmonization

Java

logging-log4j2 lj 1 ▲ 1 1 54K

changed lines ( av2 ▲ ), whereas no-CPV delta commits are

substantially larger, from 3.2K ( av3 ▲ ) to over one million

lines ( mg3 ▲ ). Project build times range from 16 s ( mg3 ▲ ) to

492 s ( ws1 □ ), and harness sizes from 2.4 KB ( av3 ▲ ) to over

20 GB ( ws1 ▲ ). See [9] for more details.

Challenge Project Vulnerabilities. The 63 CPVs (33 in full-

mode and 30 in delta-mode) split into 40 C and 23 Java vulner-

abilities, covering 34 unique CWE types including memory

corruption, path traversal, and command injection. Organizers

also issued 13 SARIF broadcasts (8 valid and 5 invalid) to

test CRS triage capability. See [9] for full details.

| sions and half for last-minute ones. The | accuracy multiplier | Lang. Project | Abbr. | # CPs | # CPVs | # Harn. | SLOC | † |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| penalizes a CRS’s per-challenge total by its accuracy rate | curl | cu | 5 | ▲ | 6 | 17 | 240K |  |  |  |  |  |  |
| on that challenge, with a non-linear shape that balances tech- | dav1d | da | 1 | □ | 1 | 1 | 261K |  |  |  |  |  |  |
| nique exploration with practicality: high accuracy is barely | little-cms | cm | 1 | □ | 1 | ▲ | 2 | 15 | 87K |  |  |  |  |
| affected ( | e | . | g | ., 90% | → | negligible penalty), while low accu- | libavif | av | 2 | ▲ | 1 | 8 | 44K |
| racy is steeply penalized (50% | → | 6% reduction; 40% | → | 13% | libexif | ex | 2 | ▲ | 2 | 2 | 16K |  |  |
| Execution: Surfacing Problems Early. | AIxCC stretched | ndpi | nd | 1 | □ | 0 | 55 | 136K |  |  |  |  |  |
| across two years and 100+ collaborating organizations, in | openssl | os | 1 | □ | 0 | 30 | 909K |  |  |  |  |  |  |
| design in advance was unrealistic, so organizers iterated at two | wireshark | ws | 1 | □ | 6 | ▲ | 12 | 47 | 4901K |  |  |  |  |
| scales to surface and fix issues before the scored competition. | xz | xz | 1 | □ | 1 | 4 | 41K |  |  |  |  |  |  |
| From semifinal to final. | The semifinal narrowed 42 teams | commons-compress | cc | 5 | ▲ | 5 | 16 | 76K |  |  |  |  |  |
| to 7 finalists while exposing two design flaws that the fi- | dcm4che | dc | 1 | □ | 0 | 1 | 105K |  |  |  |  |  |  |
| advantaged CRSs strong at patching but weak at discovery; | hc | 1 | □ | 0 | 1 | 53K |  |  |  |  |  |  |  |
| the final scored patches against all PoVs from all teams. | ➁ | hertzbeat | hb | 1 | □ | 0 | 1 | 78K |  |  |  |  |  |
| Per-repository challenge adoption demanded significant en- | jsoup | js | 1 | □ | 0 | 2 | 36K |  |  |  |  |  |  |
| gineering; the final adopted OSS-Fuzz instead. With fewer | pdfbox | pb | 1 | □ | 1 | ▲ | 9 | 6 | 167K |  |  |  |  |
| teams to support, the final granted broader team autonomy | poi | po | 1 | □ | 1 | ▲ | 7 | 17 | 433K |  |  |  |  |
| (per-team budgets and self-managed Azure infrastructure) and | tika | tk | 1 | ▲ | 1 | 9 | 188K |  |  |  |  |  |  |
| dedicated pre-competition support, in place of the semifinal’s | Total | 24 | ∗ | 16 | ∗ | □ | 32 | ▲ | 63 | 301 |  |  |  |
| final ran exhibition rounds with the finalist teams. Three un- | (vulnerabilities within a PR diff) challenges, of which eight |  |  |  |  |  |  |  |  |  |  |  |  |
| scored rounds used a separate challenge set that mirrored the | contain no injected CPV and serve solely as 0-day discovery |  |  |  |  |  |  |  |  |  |  |  |  |
| scored setting, letting both teams and organizers iterate on | targets. For delta challenges, CPV-containing delta commits |  |  |  |  |  |  |  |  |  |  |  |  |
| their systems and processes. | are relatively compact, ranging from 163 ( | cc5 | ▲ | ) to 1,407 |  |  |  |  |  |  |  |  |  |
| development. | 5 | Cyber Reasoning Systems |  |  |  |  |  |  |  |  |  |  |  |
| verse application categories, from image-processing libraries | Table 2 summarizes the background information behind each |  |  |  |  |  |  |  |  |  |  |  |  |
| to healthcare-critical software. The number of harnesses per | team’s CRS. While all teams built systems targeting the same |  |  |  |  |  |  |  |  |  |  |  |  |
| repository varies considerably, from a single harness ( | dav1d | , | CRS core capabilities (§3), their architectural approaches var- |  |  |  |  |  |  |  |  |  |  |
| libavif | , etc.) to 55 ( | ndpi | ), and repository sizes range from | ied widely, shaped by team expertise, resource constraints, |  |  |  |  |  |  |  |  |  |
| 16K ( | libexif | ) to 4.9M ( | wireshark | ) lines of code. | and strategic priorities. We briefly introduce each team’s de- |  |  |  |  |  |  |  |  |
| Challenge Projects. | The 48 CPs comprise 16 full-mode | sign philosophy, providing context for understanding their |  |  |  |  |  |  |  |  |  |  |  |
| (vulnerabilities anywhere in the repository) and 32 delta-mode | technical choices in subsequent sections. |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 4

| Table 2: CRS Teams, ordered top-to-bottom by final score | Table 3: PoV Generation Techniques Beyond OSS-Fuzz De- |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (descending; see Table 7). | † | : Full name “All You Need | faults. | # | : non-LLM; | : LLM-enhanced; | ✓ | : present; blank: |
| IS A Fuzzing Brain”. | ‡ | : Orchestration code only. | § | : Uses | absent. Extended details: Table 11. |  |  |  |

LiteLLM [10] for multi-provider routing.

| AT | Team Atlanta | A | TLANTIS | Mixed | Py,Rust | LangGraph [33] | § |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TB | Trail of Bits | B | UTTERCUP | Industry | Py | LangGraph |  |  |  |  |
| TI | Theori | R | OBO | D | UCK | Industry | Py,Rust | Self-built | § |  |
| FB | Fuzzing Brain | † | F | UZZING | B | RAIN | Academic | Py,Go | × | § |
| SP | Shellphish | A | RTIPHISHELL | Academic | Py | Self-built | § |  |  |  |
| 42 | 42-b3yond-6ug | B | UG | B | USTER | Academic | Py,Go | LangChain [13] | § |  |
| LC | Lacrosse | L | ACROSSE | Industry | Py,Lisp | DSPy |  |  |  |  |

unique contribution is worth incorporating, and combining

This leads to multiple independent bug-finding modules col-

Buttercup: Expertise-Driven Decomposition. TB leverages

domain expertise to design deterministic workflows that de-

integrated only where traditional tools fall short. Notably,

decomposed problems paired with mid-tier models suffice.

RoboDuck: Agentic Design around Bug Candidates. TI

tification and filtering, through PoV generation and patching,

to SARIF validation and bundling.

gies. FB balances engineering effort against performance

by simplifying architectural design while maximizing LLM

69], the team consistently simplifies them to be practical,

AT TB TI FB SP 42 LC

Seed Gen Agent

Bootstrap

Solve cov blocker

Mutator/generator

Grammar-aware

| Engine Refinement | # | # |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Fuzzing | Semantic feedback |  |  |  |  |  |
| Pipeline | Improved sanitizer | # | # |  |  |  |
| Dict Gen | # | # | # |  |  |  |
| Directed fuzzing | # | # |  |  |  |  |
| Corpus sync | # | # | # | # | # | # |
| Added C fuzzers | # | # | # | # |  |  |

Bug Cand. I.D.

LLM-

Based

PoV

PoV Gen Agent

Gen

With CWE guidance

Pipeline

Reach-then-exploit

Co-op Fuzz → LLM PoV Gen ✓ ✓ ✓

Sub. ASAP Submission ✓ ✓ ✓ ✓ ✓ ✓ ✓

6.1 PoV Generation

ran only parallel fuzzing.

| ID | Team | CRS | Bg | Lang | ‡ | LLM Lib | Pre-Comp Corpus | # | # |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Atlantis: Ensemble-First Design. | AT | is built around the en- | Concolic Fuzzing | # |  |  |  |  |  |
| semble philosophy [14, 26, 32]: any technique demonstrating | Parallel Fuzzing | # | # | # | # | # | # | # |  |
| multiple independent approaches enhances overall robustness. | Added JVM fuzzers | # |  |  |  |  |  |  |  |
| laborating through seed sharing, and eight patching agents | Candidate filter | # |  |  |  |  |  |  |  |
| with diverse repair strategies. | Non-PoV Gen usage | ✓ | ✓ | ✓ | ✓ |  |  |  |  |
| compose challenges into well-defined subtasks, with LLMs | Pipeline | LLM PoV Gen | → | Fuzz | ✓ | ✓ | ✓ | ✓ | ✓ |
| TB | avoids high-end reasoning models, believing that well- | PoV | Deduplication | # | # | # | # | # |  |
| embodies an agentic-first philosophy, building on a custom | 42], patching, and analysis in a multi-agent system [43]. |  |  |  |  |  |  |  |  |
| agent library that maximizes autonomous LLM operation. | DSPy [53] manages diverse LLMs in parallel or as fallbacks, |  |  |  |  |  |  |  |  |
| The entire system revolves around bug candidates: from iden- | with patch failures refining vulnerability analysis. |  |  |  |  |  |  |  |  |
| FuzzingBrain: Simple Architecture, Diverse LLM Strate- | 6 | Taxonomy of CRS Techniques |  |  |  |  |  |  |  |
| strategy diversity. Notably, over 90% of its codebase is vibe- | Two Complementary Pipelines. | In Table 3, two complemen- |  |  |  |  |  |  |  |
| coded [31]. It implements 23 independent strategies, each as a | tary discovery pipelines emerge as the first two row groups: a |  |  |  |  |  |  |  |  |
| standalone Python script with minimal dependencies, varying | Fuzzing Pipeline | that extends traditional fuzzing with LLM- |  |  |  |  |  |  |  |
| in scope, depth, and language-specific handling. | assisted components, and an | LLM-Based PoV Generation |  |  |  |  |  |  |  |
| Artiphishell: Comprehensive Technical Coverage. | SP | Pipeline | that directly leverages LLMs to identify vulnerabil- |  |  |  |  |  |  |
| achieves the most comprehensive technical coverage, imple- | ities and generate exploit inputs. The other two row groups |  |  |  |  |  |  |  |  |
| menting diverse techniques across all four core capabilities. | capture how teams couple them ( | Pipeline Cooperation | ) and |  |  |  |  |  |  |
| To coordinate these techniques (53 components), the team | how PoVs are deduplicated and submitted ( | PoV Submission | ). |  |  |  |  |  |  |
| built a custom orchestration platform that launches them on- | Both pipelines reinforce each other: fuzzing supplies coverage |  |  |  |  |  |  |  |  |
| demand and facilitates inter-component communication. | and inputs to LLM-based generation, while LLM-generated |  |  |  |  |  |  |  |  |
| BugBuster: Pragmatic Technology Choices. | 42 | follows a | outputs (even failures) seed fuzzers. |  |  |  |  |  |  |
| pragmatic philosophy, preferring simple and stable technology | Fuzzing Pipeline. | Most teams (5/7) explored both pipelines, |  |  |  |  |  |  |  |
| choices. For bug finding, the design is traditional fuzzing and | while | 42 | and | LC | focused on fuzzing alone. Of the five, | AT |  |  |  |
| program analysis centric, with LLMs limited to auxiliary roles | and | SP | explored most comprehensively; | TB | and | TI | targeted |  |  |
| like seed generation. When adopting academic techniques [50, | fuzzing-seed techniques (reuse, generation, sharing); and | FB |  |  |  |  |  |  |  |
| replacing sophisticated optimizations. | Pre-competition corpus. | Five teams reused pre-collected |  |  |  |  |  |  |  |
| Lacrosse: DSPy-Based Multi-LLM Workflow. | LC | uses | corpora to bootstrap fuzzer coverage, typically with two steps: |  |  |  |  |  |  |
| a Lisp-based task distributor to coordinate fuzzing [41, | ➀ | collecting and grouping seeds from public databases (Clus- |  |  |  |  |  |  |  |

---

## Page 5

| terFuzz [29], OSS-Fuzz [5], GitHub, etc.) before the com- | ( | AT | , | TB | , | FB | , | SP | ) inject CWE-specific guidance [40] to steer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| petition; | ➁ | pairing seeds with harnesses by coverage-based | exploit construction. Three ( | AT | , | TI | , | SP | ) further decompose |
| ranking or by similarity matching against harness names and | generation: a reach agent drives execution to the target sink, |  |  |  |  |  |  |  |  |
| LLM-inferred input formats. | and an exploit agent crafts the trigger. |  |  |  |  |  |  |  |  |
| Seed generation agent. | Six teams use LLMs to generate | Pipeline Cooperation. | Teams cooperate between pipelines |  |  |  |  |  |  |
| seeds in two scenarios: early-stage bootstrap (analyzing har- | in both directions, though more invest in one than the other. |  |  |  |  |  |  |  |  |
| ness code for input formats) and troubleshooting (generating | On one side (LLM PoV Gen | → | Fuzz, five teams), successful, |  |  |  |  |  |  |
| inputs for coverage blockers [59]). The agents typically in- | failed, and intermediate results from LLM PoV generation |  |  |  |  |  |  |  |  |
| corporate conventional program analysis tools for better per- | are shared with fuzzers, expecting fuzzers to extend cover- |  |  |  |  |  |  |  |  |
| formance. Interestingly, despite the goal being harness input | age or mutate these near-solutions into actual PoVs. On the |  |  |  |  |  |  |  |  |
| generation, all teams chose to have LLMs generate Python | other side (Fuzz | → | LLM PoV Gen, three teams), fuzzers |  |  |  |  |  |  |
| scripts that produce inputs upon execution. Additionally, | AT | , | provide coverage information to guide LLM generation; for |  |  |  |  |  |  |
| TI | , and | SP | explored generating input generators/mutators and | teams with separate exploit agents, fuzzer-found reached-but- |  |  |  |  |  |
| explicit grammars (testlang and libFDP [37] for | AT | , Python | unexploited inputs are also forwarded for exploitation. |  |  |  |  |  |  |
| decoders for | TI | , and Nautilus [6] grammars for | SP | ). | PoV Submission. | All teams adopt straightforward strategies: |  |  |  |
| Engine refinement. | Beyond existing fuzzers, teams ( | AT | , | SP | , | submit unique PoVs as soon as possible. This simplicity stems |  |  |  |
| and | 42 | ; primarily from university research labs) refined inter- | from the scoring rules: correct but duplicate submissions incur |  |  |  |  |  |  |
| nal components (feedback, oracle, dict, scheduler). | SP | added | only time-decay penalties, not accuracy penalties, making |  |  |  |  |  |  |
| semantic feedback | by having LLMs generate IJON [7]-style | early submission always preferable. To minimize redundant |  |  |  |  |  |  |  |
| annotations, the only team to do so. | AT | and | SP | improved | submissions, all teams implement deduplication using crash |  |  |  |  |
| the Java sanitizers | to strengthen fuzzer guidance toward valid | stack traces, input hashing, sanitizer signatures, etc. | TI | and |  |  |  |  |  |
| PoCs. For | dictionary generation | , four teams produced fuzzing | FB | further use LLMs to group semantically equivalent PoVs. |  |  |  |  |  |

dictionaries to break input-format barriers: AT via on-the-

fly LLM prompts, SP via AFL++ [23] dict2file plus Cod- 6.2 Patch Generation

eQL [28], and 42 and LC via custom extraction. Finally, AT

| and | 42 | customized scheduling with | directed fuzzing | : | AT | used a | All CRSs follow a de facto patch pipeline as shown below, |
| --- | --- | --- | --- | --- | --- | --- | --- |
| custom distance metric, while | 42 | used LLVM and WALA [62] | where RCA denotes Root Cause Analysis and brackets indi- |  |  |  |  |
| program slicing to selectively instrument paths to sinks. | cate optional steps. |  |  |  |  |  |  |

Concolic fuzzing. AT explored building hybrid fuzzers:

loop([RCA] → Generate → Validate) → Dedup → Submit

SymCC [47]-based for C and a from-scratch engine for Java.

| Parallel fuzzing. | All teams run multiple fuzzer instances in | Within this pipeline, teams explore different LLM-centric |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| parallel and synchronize corpora across them (except | FB | ). Be- | designs to make patching effective. Table 4 organizes their |  |  |  |  |  |  |  |  |
| yond the OSS-Fuzz defaults, | AT | , | SP | , | 42 | , and | LC | added custom | design choices into five row groups. | Agent Arch. | captures |
| C fuzzers (AFL++ [23], libAFL [24], or custom implementa- | the overall agentic design of the patch system. The other |  |  |  |  |  |  |  |  |  |  |
| tions), with | AT | also covering JVM via libAFL. | four mirror the pipeline steps: | RCA | , | Generation | , | Validation | , |  |  |
| LLM-Based PoV Generation Pipeline. | Six teams explored | and | Dedup. & Sub. | The last two steps are grouped together |  |  |  |  |  |  |  |
| this LLM-driven alternative to fuzzing. The typical workflow | because deduplication primarily prepares for submission. |  |  |  |  |  |  |  |  |  |  |
| involves two steps: | ➀ | identifying and filtering bug candidates; | Agent Architecture. | CRSs’ designs split into three patterns. |  |  |  |  |  |  |  |
| ➁ | generating PoVs targeting these candidates. | LC | performs | Multi-Arch. | Multi-Arch is an ensemble strategy where |  |  |  |  |  |  |
| only step | ➀ | and feeds results to no-PoV patch generation | the CRS patch system runs multiple distinct patcher ar- |  |  |  |  |  |  |  |  |
| (§6.2) rather than PoV generation. | TB | skips step | ➀ | , letting its | chitectures to combine their benefits. | AT | ensembles eight |  |  |  |  |
| agent autonomously judge during PoV generation. | patcher agents [32] spanning diverse designs: workflow-based |  |  |  |  |  |  |  |  |  |  |
| Bug candidate identification. | Five teams build agent sys- | pipelines with ReAct-style [68] tool use, autonomous agents |  |  |  |  |  |  |  |  |  |
| tems combining LLMs, static analysis tools (CodeQL [28], | with iterative context retrieval, multi-agent systems for han- |  |  |  |  |  |  |  |  |  |  |
| Semgrep [48], Infer [38]), and predefined sink lists to iden- | dling context limitations, and off-the-shelf coding agents |  |  |  |  |  |  |  |  |  |  |
| tify and filter candidates. Two distinctive filtering techniques | (Aider [27], SWE-Agent [67]). | SP | instead pairs a fully agentic |  |  |  |  |  |  |  |  |
| stand out: | TI | uses LLM logprobs [45] as a token-efficient | LLM patcher with a program-analysis-assisted, one-shot min- |  |  |  |  |  |  |  |  |
| confidence signal, exposing them to its classification agent | imal LLM patcher. When generating, | AT | stops once any agent |  |  |  |  |  |  |  |  |
| as a tool; | SP | and | LC | instead aggregate weighted votes [64] | produces a valid patch, while | SP | retains all candidates, then |  |  |  |  |
| across multiple tools and LLMs to rank candidates. | ranks and strategically selects the final patches (see | Dedupli- |  |  |  |  |  |  |  |  |  |
| PoV | Generation | Agent. | Five | teams | construct | PoV- | cation and Submission | below). |  |  |  |
| generation agents over static and dynamic analysis tools. Be- | Multi-Agent. | Multi-Agent is a decomposition strategy |  |  |  |  |  |  |  |  |  |
| yond source code, agents receive call paths, coverage, runtime | where a single patcher contains multiple coordinating sub- |  |  |  |  |  |  |  |  |  |  |
| logs, and debugger access (GDB [25]/JDB [46]). Four teams | agents. | TB | organizes its four agents into a pipeline of RCA, |  |  |  |  |  |  |  |  |

---

## Page 6

| Table 4: Patch Generation Techniques. | : present; blank: | code are used by all teams. Optional augmentations, by |  |
| --- | --- | --- | --- |
| no custom implementation; –: not applicable; 1/N/ | ∗ | : sin- | descending popularity: pre-built code indexers for symbol |
| gle/multiple/all PoVs; | † | all teams use sanitizer/crash reports | lookups (5 teams); SAST reports static analysis outcomes |
| and failed patch feedback. Extended details: Table 12. | (4 teams); runtime probes (debugger, coverage instrumen- |  |  |

Multi-Arch

Multi-Agent

Standalone RCA

Code Indexer

SAST

ation Agentic Code Search

LLM Reflection

Basic Checks

Vali- Proj. Tests

Post-patch Fuzz

Dedup. Min. Patch Set Calc.

as an inner tool for code understanding.

with weighted voting to rank root cause candidates.

crash/sanitizer output and agentic code search over project

tation) for inspecting actual execution (4 teams); the PoV

LLM Reflection. LLM reflection [51] enables agents to

corrective guidance.

a PoV. The generation technique is similar to but more lim-

tion before accepting a candidate patch.

verification, PoV reproduction during generation ( PoV Test

(Gen) ), and project test suites ( 42 skips project tests). The

Test (Submit) below).

Maven [4] caching for Java).

we discuss them together.

| AT | TB | TI | FB | SP | 42 | LC | bytes that triggered the bug (3 teams); CWE-specific vulner- |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Agent | ability domain knowledges (2 teams); and LLM fine-tuning |  |  |  |  |  |  |  |  |  |  |  |  |
| Arch. | Single-Agent | (Llama [60]) for context retrieval (1 team). |  |  |  |  |  |  |  |  |  |  |  |
| RCA | Multi-PoV RCA | learn from failed attempts; five CRSs adopted it. One typical |  |  |  |  |  |  |  |  |  |  |  |
| Non-LLM RCA | example is | TB | , which implements a dedicated reflection agent |  |  |  |  |  |  |  |  |  |  |
| Contextualization | † | that analyzes failures at each generation step and provides |  |  |  |  |  |  |  |  |  |  |  |
| CWE Guidance | No-PoV Patch Generation. | Three CRSs ( | TI | , | FB | , | LC | ) at- |  |  |  |  |  |
| Gener- | Fine-tuned LLM | tempt patch generation for a vulnerability candidate whose |  |  |  |  |  |  |  |  |  |  |  |
| Dynamic Info | PoV has not been created by the CRS. Without dynamic |  |  |  |  |  |  |  |  |  |  |  |  |
| PoV Bytes | evidence, this approach carries risk, but can address vulnera- |  |  |  |  |  |  |  |  |  |  |  |  |
| No-PoV Patch Generation | bilities that are obvious to identify yet difficult to trigger with |  |  |  |  |  |  |  |  |  |  |  |  |
| Build | ited than PoV-based techniques, while all teams focus on risk |  |  |  |  |  |  |  |  |  |  |  |  |
| PoV Test (Gen) | 1 | N | ∗ | 1 | N | ∗ | 1 | mitigation by limiting no-PoV patch quantities per challenge |  |  |  |  |  |
| dation | PoV Test (Submit) | ∗ | N | ∗ | N | ∗ | ∗ | 1 | and imposing stricter submission conditions ( | e | . | g | ., delayed |
| LLM as Judge | submission, gated by prior success rate, etc). |  |  |  |  |  |  |  |  |  |  |  |  |
| Rebuild Optimization | Validation. | CRSs employ several checks within each itera- |  |  |  |  |  |  |  |  |  |  |  |
| & Sub. | No-PoV Delayed Sub. | – | – | – | – | Basic Checks. | All CRSs share three basic checks: build |  |  |  |  |  |  |
| fix strategy, patch creation, and reflection, each handing off to | number of PoVs used during generation varies (1/N/* in Ta- |  |  |  |  |  |  |  |  |  |  |  |  |
| the next. | TI | instead uses a hierarchical design: a ReAct-style | ble 4); most teams use only a subset to keep the iteration loop |  |  |  |  |  |  |  |  |  |  |
| outer loop generates patches, invoking SourceQuestionsAgent | fast, then revalidate against more before submission (see | PoV |  |  |  |  |  |  |  |  |  |  |  |
| Single-Agent. | Three CRSs adopt single-agent designs with | PoV Test (Submit). | Before submission, most CRSs revali- |  |  |  |  |  |  |  |  |  |  |
| varying degrees of agentic customization. | FB | implements 23 | date patches against a broader PoV set than was used during |  |  |  |  |  |  |  |  |  |  |
| strategies spanning delta-scan and full-scan modes, differenti- | generation, catching incomplete fixes that a partial generation- |  |  |  |  |  |  |  |  |  |  |  |  |
| ated by context scope and knowledge injection. | 42 | maximizes | time set may miss. | AT | and | FB | expand from a single PoV in |  |  |  |  |  |  |
| configuration diversity, exploring 16 combinations of tempera- | generation to multiple PoVs before submission, | TB | uses mul- |  |  |  |  |  |  |  |  |  |  |
| ture and prompt context (failed cases, stack traces, etc) within | tiple throughout, and | LC | uses a single PoV throughout. |  |  |  |  |  |  |  |  |  |  |
| a single agent architecture. | LC | uses a DSPy-based workflow | LLM-as-Judge. | Three CRSs incorporate LLM-based eval- |  |  |  |  |  |  |  |  |  |
| with model escalation from cheaper to expensive models. | uation [30], including judging whether patches correctly ad- |  |  |  |  |  |  |  |  |  |  |  |  |
| Root Cause Analysis. | Four CRSs ( | AT | , | TB | , | TI | , | SP | ) implement | dress the root cause and follow the prescribed fix strategy |  |  |  |
| standalone RCA components, allowing LLMs to separately | ( | AT | ), and self-reflecting on whether patches genuinely fix vul- |  |  |  |  |  |  |  |  |  |  |
| focus on root cause analysis and patch synthesis as distinct | nerabilities rather than being superficial, easily-bypassed, or |  |  |  |  |  |  |  |  |  |  |  |  |
| sub-problems. All four build LLM agents for RCA; | TB | , | TI | , | having side effects ( | FB | / | SP | for No-PoV/all patches). |  |  |  |  |
| and | SP | further leverage information from multiple PoVs for | Post-patch Fuzz. | FB | and | SP | adopt short-term fuzzing on |  |  |  |  |  |  |
| more accurate root cause analysis. | SP | additionally incorpo- | patched projects for incomplete patch detection. |  |  |  |  |  |  |  |  |  |  |
| rates a non-LLM RCA component that combines multi-source | Rebuild Optimization. | AT | and | SP | employ build caching to |  |  |  |  |  |  |  |  |
| signals (SAST reports, stack traces, fuzzing invariants, etc.) | accelerate iterative patch refinement (ccache [12] for C/C++, |  |  |  |  |  |  |  |  |  |  |  |  |
| Generation. | Within the Generate step, CRSs employ various | Deduplication and Submission. | Naively submitting a patch |  |  |  |  |  |  |  |  |  |  |
| techniques to improve patch quality. | for each PoV incurs many duplicate submissions and patch- |  |  |  |  |  |  |  |  |  |  |  |  |
| Contextualization. | This presents the information sources | score penalties, so teams must balance deduplication and sub- |  |  |  |  |  |  |  |  |  |  |  |
| supplied to the LLM’s prompt for patch generation. The | mission timing. Since the two strategies are tightly coupled, |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 7

Table 5: SARIF Submission Strategies. ✓ / × : submit Cor- Table 6: Bundling Pairing Strategies. : used; blank: not used.

rect / Incorrect . Full details at [9].

CRS Category Submission Strategy Overview

N

AT , TB PoV-centric

Match Any PoV Y

✓

Match Any PoV Y

✓

| FB | PoV-centric |
| --- | --- |
| N | N |
| LLM As Judge | Y |

✓

Y/N ✓ / ×

Match Bug Cand.

(1st)

✓

Match Bug Cand. Y

(2nd)

SP , LC LLM-judge-centric LLM As Judge Y/N

✓ / ×

LLM As Judge Y/N

✓ / ×

42 LLM-judge-centric N UNK

Match Any PoV Y

✓

Minimal Patch Set Calculation. Four CRSs ( AT , TB , SP , and

sharing the same root cause, and compute a minimal patch set

The SARIF validation task requires CRSs to assess each static

Correct or Incorrect . CRSs can resubmit to revise verdicts

Key Evidence for Validation. Table 5 summarizes each

ities; ➁ Match Bug Cand. : matching any bug candidate (in-

Pairing Source AT TB TI FB SP 42 LC

PoV-based Patch

PoV-Patch

Match No-PoV Patch

SARIF Validation

PoV-SARIF

SARIF-guided PoV

Bug Candidate DB

Patch-SARIF

SARIF-guided Patch

Validation Strategies. Teams adopted three strategies.

PoV-centric. AT , TB , and FB primarily rely on PoV match-

holding unmatched reports. FB additionally uses a fallback

LLM judgement, but only submits Correct from it.

LLM-judge-centric. SP , 42 , and LC rely on LLM judgement,

submitting both Correct and Incorrect based on the model’s

assessment. 42 falls back to PoV matching when the model

replies with uncertainty.

Bug-cand-centric. TI matches SARIF reports against its

bug candidate database, initially submitting Incorrect for un-

matched reports and revising to Correct on new evidence.

generate PoVs/patches, pairing them upon success. 42 and LC

do not participate in SARIF pairing, while only teams with

concurrently within each phase. 3

| TI | Bug-cand-centric | N | N | ing, submitting | Correct | only when a match is found and with- |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 42 | ) leverage the fact that a single patch can fix multiple PoVs | 6.4 | Bundling Strategy |  |  |  |  |  |  |  |  |
| that covers all known PoVs to avoid duplicate submissions. | Bundling pairs PoVs, patches, and SARIF assessments into |  |  |  |  |  |  |  |  |  |  |
| These CRSs differ in three dimensions: | ➀ | Calc. timing | : on | coherent vulnerability reports. Unlike other submissions with |  |  |  |  |  |  |  |
| each new PoV ( | AT | , | TB | , | SP | ) for faster response, or hourly ( | 42 | ) | time decay, bundling allows free updates until the deadline, |  |  |
| for better global optimization. | ➁ | Calc. mode | : incremental | with scoring based solely on final results. A bundle can con- |  |  |  |  |  |  |  |
| over uncovered PoVs only ( | AT | , | 42 | ) for simplicity, or recom- | tain any two of three pairings, PoV-Patch, PoV-SARIF, and |  |  |  |  |  |  |
| pute over all PoVs ( | TB | , | SP | ) for better optimization at the | Patch-SARIF, to form a complete scoring bundle, while any |  |  |  |  |  |  |
| risk of duplicate submissions. | ➂ | Submission timing | : imme- | incorrect pairing will penalize the entire bundle. |  |  |  |  |  |  |  |
| diate ( | AT | , | TB | , | 42 | ), or delayed ( | SP | , | ≥ | 60min) for better global | Table 6 summarizes each team’s bundling pairing strategies. |
| minima. For | SP | , the candidates retained from its Multi-Arch | Given the risk of score penalties, teams tend to derive pairings |  |  |  |  |  |  |  |  |
| ensemble (§6.2) are submitted ranked by PoV count. | from existing workflows rather than inferring relationships |  |  |  |  |  |  |  |  |  |  |
| No-PoV Patch Delayed Submission. | All three CRSs with | independently. | ➀ | All teams naturally derive PoV-Patch re- |  |  |  |  |  |  |  |
| No-PoV patch generation capability ( | TI | , | FB | , | LC | ) delay sub- | lationships from PoV-based patch generation. For No-PoV |  |  |  |  |
| mission to reduce imperfect patch penalties: | TI | waits | ≥ | 45min | patches (§6.2), | TI | retroactively links PoVs once discovered, |  |  |  |  |
| and gates on PoV patch success history, | FB | waits until 50% | while | FB | does not. | ➁ | For SARIF pairings, teams either reuse |  |  |  |  |
| of challenge time, and | LC | submits 30min before deadline. | their SARIF validation results (§6.3) or use SARIF reports to |  |  |  |  |  |  |  |  |
| 6.3 | SARIF Validation | No-PoV patch capability can submit Patch-SARIF bundles. |  |  |  |  |  |  |  |  |  |
| analysis report as valid or invalid, submitting a verdict of | 7 | Competition Result Analysis |  |  |  |  |  |  |  |  |  |
| while incurring penalties in both time and accuracy. | 7.1 | What Scores Reveal (and Conceal) |  |  |  |  |  |  |  |  |  |
| team’s core submission strategy. Teams primarily relied on | We analyze the final scores (Figure 2, Table 7) to understand |  |  |  |  |  |  |  |  |  |  |
| three types of evidence: | ➀ | Match Any PoV | : matching SARIF | what differentiated the finalists. The competition spanned |  |  |  |  |  |  |  |
| locations against crash information from exploited vulnerabil- | 142.7 hours across seven phases (P1–P7), with tasks released |  |  |  |  |  |  |  |  |  |  |
| ferred from LLM, static analysis, PoV, etc.); | ➂ | LLM As Judge | : | 3 | Phases are non-overlapping time windows during which CPs are released |  |  |  |  |  |  |
| agentic prompting to directly assess its correctness. | to teams; the CP-to-phase assignment has no intentional structure. |  |  |  |  |  |  |  |  |  |  |

---

## Page 8

sues at this scale of autonomous evaluation. AT (392.8 points,

ping out of contention. LC , unfortunately, contributed only in

early phases and was largely inactive afterward.

Pinpointing the cause of each stability failure is inherently

an unrecoverable OOM crash on their master scheduler node,

accuracy penalties ( − 16 . 3 and − 13 . 5), and for TI the penalty

was decisive: its pre-penalty score was higher than TB ’s, but

the penalty dropped TI to third, behind TB by 8.7 points.

bility would be the most interesting result here, but the factors

Table 7: AFC Score Breakdown. Columns are ordered left-to-

right by final score (descending). Pen. stands for penalties.

| AT | TB | TI | FB | SP | 42 | LC |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C | 52.6 | 31.0 | 22.7 | 22.6 | 31.4 | 49.1 | 1.5 |  |
| PoV | Java | 27.0 | 21.3 | 31.6 | 29.7 | 16.5 | 21.1 | 0.0 |

Sum 79.6 52.4 54.3 52.3 47.8 70.1 1.5

C 113.5 74.2 51.8 45.3 40.5 9.7 4.9

Patch Java 57.5 26.7 49.8 23.5 13.8 4.5 0.0

Sum 171.0 100.9 101.6 68.8 54.3 14.2 4.9

| SARIF | Java | 1.0 | 0.0 | 1.0 | 1.5 | 1.0 | 1.0 | 0.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sum | 6.0 | 1.0 | 4.9 | 6.2 | 8.5 | 9.7 | 0.0 |  |
| C | 99.6 | 49.4 | 26.0 | 27.6 | 18.3 | 7.8 | 3.2 |  |
| C | 270.6 | 155.6 | 104.4 | 100.2 | 97.6 | 75.4 | 9.6 |  |

Total

Key Finding (KF) 1. Winning AIxCC requires balancing

research, engineering, and strategy. Stability proved the

| Figure 2: Score per time (top) and phase (bottom) axes. | C | 5.0 | 1.0 | 3.9 | 4.7 | 7.5 | 8.7 | 0.0 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| System stability. | Stability accounts for most of the score gap. | Bundle | Java | 36.6 | 15.7 | 23.8 | -1.1 | 7.0 | 3.2 | 0.0 |  |  |
| As Figure 2 shows, three teams experienced severe stability is- | Sum | 136.2 | 65.1 | 49.8 | 26.4 | 25.3 | 11.0 | 3.2 |  |  |  |  |
| nearly 80% more than second-place | TB | at 219.4) sustained | Java | 122.1 | 63.8 | 106.3 | 53.5 | 38.3 | 29.7 | 0.0 |  |  |
| activity across all phases, while | TB | and | TI | were competitive | Pen. | -0.4 | -0.6 | -16.3 | -13.5 | -0.1 | -0.3 | -1.1 |
| early but plateaued after P3 and P4 respectively, visibly drop- | Final | 392.8 | 219.4 | 210.7 | 153.7 | 135.9 | 105.0 | 9.6 |  |  |  |  |
| difficult: CRSs are highly parallel distributed systems, and | discussed above undermine the score-based conclusion va- |  |  |  |  |  |  |  |  |  |  |  |
| teams selectively uploaded telemetry to the organizers. The | lidity. A low score may indicate a real capability gap, or it |  |  |  |  |  |  |  |  |  |  |  |
| most likely hypotheses are as follows. | TB | and | TI | ’s plateaus | may simply reflect outages or strategy choices, and we cannot |  |  |  |  |  |  |  |
| likely share a common trigger in P3’s | wireshark | CP, which | tell them apart. A high score is informative to some extent: |  |  |  |  |  |  |  |  |  |
| required about 1 TB of disk for compiled artifacts (20.9 GB | the team’s design must have had corresponding effectiveness. |  |  |  |  |  |  |  |  |  |  |  |
| across 47 harnesses) and can crash CRSs lacking robust | Reading the leaders on this basis (Table 7), | AT | shows strong |  |  |  |  |  |  |  |  |  |
| disk management. We also found a CP-cleanup issue in | TI | ’s | performance on C PoV (52.6), Patch (171.0), and Bundle |  |  |  |  |  |  |  |  |  |
| telemetry (reporting P1 CP LLM activities during P3), which | (136.2); | TI | on Java PoV (31.6); | 42 | on SARIF (9.7); and | SP |  |  |  |  |  |  |
| could have worsened the situation. | LC | ’s postmortem identifies | on per-submission accuracy (smallest penalty, | − | 0 | . | 1). |  |  |  |  |  |
| after which their system stopped working and the only output | The AIxCC trifecta. | AIxCC is fundamentally a test of three |  |  |  |  |  |  |  |  |  |  |
| was 1,200+ PoVs against a single CPV. | intertwined capabilities: | research | , | engineering | , and | strategy | . |  |  |  |  |  |
| Even teams that reported activity throughout were not free | Winning required balancing all three, and the finalists illus- |  |  |  |  |  |  |  |  |  |  |  |
| from stability bugs. Per their own analyses, | 42 | ’s submission | trate contrasting trade-offs. | TI | built the most agentic archi- |  |  |  |  |  |  |  |
| bug [56] cost most of its patch points (14.2), | SP | reported mul- | tecture with advanced technique designs, but its aggressive |  |  |  |  |  |  |  |  |  |
| tiple system issues in their postmortem [58], such as incorrect | strategy led to the largest accuracy penalty. | FB | , among the |  |  |  |  |  |  |  |  |  |
| LLM budget configuration, and | AT | silently failed on all | poi | smallest teams, combined a focused strategy with vibe coding |  |  |  |  |  |  |  |  |
| Java challenges (heartbeat telemetry activities only). | and LLM-assisted expertise to ship an effective system on |  |  |  |  |  |  |  |  |  |  |  |
| Submission accuracy. | Accuracy was another major factor | minimal resources. | SP | and | AT | pursued similar broad-coverage |  |  |  |  |  |  |
| in the final ranking (Table 10): the competition’s accuracy | approaches (both large research teams investing heavily in |  |  |  |  |  |  |  |  |  |  |  |
| multiplier (§3) directly scales each team’s total by their per- | engineering and exploring many research directions), with |  |  |  |  |  |  |  |  |  |  |  |
| challenge accuracy rate. While most CRSs reach high submis- | different execution outcomes. | SP | encountered reliability is- |  |  |  |  |  |  |  |  |  |
| sion accuracy (PoV | > | 80%, Patch | > | 75%), | TI | and | FB | show | sues that limited how much of its broad coverage reached the |  |  |  |
| significantly lower rates (PoV at 61.8% and 80.0%, Patch at | scoreboard, while | AT | ’s ensemble executed reliably, sustain- |  |  |  |  |  |  |  |  |  |
| 31.7% and 23.3% respectively), mostly driven by bursts of | ing scoring across all seven phases. In all cases, technique |  |  |  |  |  |  |  |  |  |  |  |
| invalid submissions on a few challenges rather than a uni- | capability alone did not decide the outcome; strategy and |  |  |  |  |  |  |  |  |  |  |  |
| formly weak pipeline (§7.4). These result in the two largest | engineering shaped it as much. |  |  |  |  |  |  |  |  |  |  |  |
| Technical capability. | A direct comparison of technical capa- | most fundamental requirement, yet many teams failed. |  |  |  |  |  |  |  |  |  |  |

---

## Page 9

i) C - Synthetic ii) C - Zerodays

▲ 02 □ 01 □ 02 ▲ 06 ▲ 07 ▲ 03 ▲ 08 ▲ 01 ▲ 02 ▲ 01 ▲ 02 ▲ 02 ▲ 04 ▲ 01 ▲ 02 □ 00 □ 00 □ 01 □ 02 □ 03 □ 04 □ 01 □ 03 □ 04 □ 05 □ 01 □ 01 □ 02 □ 05 □ 10 □ 11 □ 12 ▲ 03 ▲ 03 ▲ 04 ▲ 06 ▲ 07 ▲ 08 ▲ 13 □ 01 □ a ▲ a ▲ b ▲ c □ a □ a □ b □ c □ a □ a

av2 cm1 cm1 cu2 cu3 cu4 cu4 cu5 cu5 ex2 ex3 fp2 lx3 mg1 mg2 mg1 ss1 ss1 ss1 ss1 ss1 sd1 sd1 sd1 sd1 da1 ws1 ws1 ws1 ws1 ws1 ws1 fp3 ws1 ws2 ws3 ws4 ws5 ws7 xz1 Σ PoV Σ Patch cm1 cu5 cu5 cu5 mg1 ss1 ss1 ss1 sd1 ws1 Σ PoV Σ Patch

| AT | 25 | 19 | AT | 4 | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TB | 12 | 16 | TB | 5 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TI | 13 | 9 | TI | 2 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FB | 11 | 12 | FB | 1 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SP | 14 | 6 | SP | 4 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 42 | 25 | 2 | 42 | 4 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LC | 0 | 0 | LC | 1 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PF | 30 | - | P2 | P3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CC | - | 23 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| MR | - | 20 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| P2 | P3 | P4 | P7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| iii) Java - Synthetic | iv) Java - Zerodays | v) SARIF - C/Java |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ▲ | 03 | ▲ | 06 | ▲ | 10 | ▲ | 10 | ▲ | 07 | ▲ | 08 | ▲ | 02 | □ | 00 | □ | 01 | □ | 03 | □ | 04 | □ | 05 | □ | 06 | □ | 07 | □ | 08 | ▲ | 05 | ▲ | 06 | □ | 00 | □ | 01 | □ | 02 | □ | 03 | □ | 04 | ▲ | 00 | □ | a | □ | a | ▲ | a | ▲ | b | ▲ | c | □ | d | □ | e | □ | f | □ | g | □ | h | □ | i | □ | a | □ | b | □ | c | □ | d | □ | 01 | ▲⊝ | ▲⊝ | ▲ | 02 | □ | 02 | □ | 00 | □ | 04 | ▲ | 00 | ▲ | 03 | ▲⊝ | ▲⊝ | ▲⊝ | □ | 01 |

cc1 cc4 cc5 tk6 cc6 cc7 pb1 pb1 pb1 pb1 pb1 pb1 pb1 pb1 pb1 po1 po1 po1 po1 po1 po1 po1 lj1 Σ PoV Σ Patch hc1 hb1 pb1 pb1 pb1 pb1 pb1 pb1 pb1 pb1 pb1 po1 po1 po1 po1 Σ PoV Σ Patch cm1 cu3 ex2 fp2 po1 ss1 sd1 lj1 ws1 ws2 ws3 ws4 xz1 Σ✓

| AT | 8 | 7 | AT | 6 | 3 | AT | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | 6 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TB | 9 | 5 | TB | 3 | 0 | TB | ✓ | 1 |  |  |  |  |  |  |  |  |  |  |  |  |
| TI | 15 | 8 | TI | 5 | 1 | TI | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | 5 |  |  |  |  |  |  |
| FB | 12 | 5 | FB | 5 | 0 | FB | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 7 |  |  |  |  |  |  |
| SP | 8 | 3 | SP | 3 | 0 | SP | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | 9 |  |
| 42 | 5 | 1 | 42 | 6 | 0 | 42 | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | 10 |
| LC | 0 | 0 | LC | 0 | 0 | LC | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PF | 4 | - | P2 | P2 | P6 | P7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CC | - | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| MR | - | 11 | PoV | Patch | No CRS Activity | Patch: Sem. Wrong | ▲ | Delta | □ | Full |  |  |  |  |  |  |  |  |  |  |
| P1 | P2 | P6 | ✓ | Scored Submission | ✗ | Unscored Submission | ⊝ | Invalid Broadcast | Phase |  |  |  |  |  |  |  |  |  |  |  |

Figure 3: Team performance per CPV. Matrices i)–iv): detected/patched CPVs and 0-days; v): SARIF assessment. Diagonal: no

CRS log messages. PF/CC/MR rows are annotations of 3-run union results. In patch: valid; ∅ /blank: failed manual/automated

validation. SARIF: invalid ( - ⃝ ) expects Incorrect ; ✓ / ✗ = CRS judgment Incorrect / Correct ; CPV abbreviations in Appendix B.

7.2 Auxiliary CPV Annotation should solve, not an exhaustive characterization of their tech-

nical boundary. Specifically: ➀ each technique runs in an ideal

| Unknown CRS Capability Boundaries. | Beyond surface- | lab environment, isolated from end-to-end system-level chal- |  |  |
| --- | --- | --- | --- | --- |
| level score comparison, we want deeper insight into CRS per- | lenges (scheduling, multi-harness coordination, PoV/patch |  |  |  |
| formance on each CPV. However, per-CPV analysis faces a | deduplication/pairing); | ➁ | resource budgets approximate a |  |
| key question: where do CRSs’ true capability boundaries lie? | reasonable CRS resource allocation (per-harness bug-finding |  |  |  |
| This is hard to answer because a CRS failure on a CPV can | budget; per-crash patching budget); | ➂ | the LLM used in anno- |  |
| stem from either a capability limit or an engineering/strategy | tation is contamination-free and accessible during competi- |  |  |  |
| issue, and the existing logs/telemetry infrastructure cannot | tion ( | claude-3-7-sonnet-20250219 | , training cutoff October |  |
| support such accurate root-cause analysis (as detailed in §7.1). | 2024, predating AIxCC’s final challenge); CC uses the closest |  |  |  |
| We therefore shift the angle: rather than diagnosing CRSs | still-available release. |  |  |  |
| directly, we characterize the CPVs through independent ex- | PF ( | atlantis-multilang-given_fuzzer | [52]). | PF runs |
| periments. Specifically, we run representative bug-finding | on vulnerable harnesses using 16 cores each, with shared- |  |  |  |
| and patching techniques on each CPV under ideal laboratory | memory seed sharing and OSS-Fuzz configurations from the |  |  |  |
| conditions with competition-level resources, annotating what | final competition. Each run lasts up to 6 hours per harness, |  |  |  |
| should be CRS-solvable. Thus, comparing CRS outcomes | stopping early when all organizer-synthesized CPVs in that |  |  |  |
| against this reference exposes advances beyond representa- | harness are found. Total: 8,906 CPU-hours across 3 runs. |  |  |  |
| tive techniques, obstacles on CPVs that should have been | MR (from | AT | , in OSS-CRS [52]). | It is a minimal patch agent |
| solvable, and boundaries that current techniques cannot cross. | using AST-based code search [61]. It receives ground-truth |  |  |  |
| Annotation Techniques. | To annotate which CPVs CRSs | PoVs, sanitizer reports, and crash stacks, generating up to 3 |  |  |
| should be able to solve, we select techniques every finalist | patches per run across 3 runs per CPV. Patches are validated |  |  |  |
| CRS has invested in, per §6. For bug finding, we use paral- | automatically (build, PoV reproduction, functional tests), then |  |  |  |
| lel fuzzing (PF), the de facto standard non-LLM bug-finding | cross-validated by two experts for semantic correctness. Cost: |  |  |  |
| approach. For patching, we use MultiRetrieval (MR) [55], a | $221.69 (LLM), one person-week (manual cross-validation). |  |  |  |
| minimal agentic code-search-and-patch loop. We also evalu- | CC (v1.0.88, 2025-08-21). | A general-purpose coding agent; |  |  |
| ate Claude Code (CC) [2], the most capable general-purpose | otherwise per MR. Cost: $119.53 (LLM), one person-week. |  |  |  |
| coding agent, as a patching reference. | Annotated Overview. | Figure 3 presents per-CPV outcomes |  |  |
| This annotation setup is an approximation of what CRSs | for all CRSs alongside our annotations. Overall, the annota- |  |  |  |

---

## Page 10

| tion results reflect that the final’s challenges do not primarily | (Java). Specifically, this targeted capability is driven primarily |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reward solving exceptionally difficult problems: around half | by LLM reasoning: | AT | and | 42 | , the two CRSs that included |  |  |  |  |  |  |  |  |
| are solvable by a single annotation technique (PF: 34/63 PoV; | classic directed fuzzing, found no uniquely-discovered delta- |  |  |  |  |  |  |  |  |  |  |  |  |
| MR: 31/63 patches; CC: 33/63 patches). | mode bugs over CRSs without it. Notably, several such CPVs |  |  |  |  |  |  |  |  |  |  |  |  |
| Combining these annotations with CRS performance, two | involve indirect calls ( | cu2 | ▲ | 06 | , | cu4 | ▲ | 03 | ), where function point- |  |  |  |  |
| contrasting patterns emerge. On one hand, most CRSs demon- | ers obscure the path to vulnerable code yet CRSs reason |  |  |  |  |  |  |  |  |  |  |  |  |
| strate genuine improvements beyond annotation techniques, | through them to reach the bug. |  |  |  |  |  |  |  |  |  |  |  |  |
| finding and patching many non-annotated CPVs, particularly | Overcoming input grammar obstacles. | Some CPVs require |  |  |  |  |  |  |  |  |  |  |  |
| in P1–P2 C and Java challenges where LLM-based reasoning | inputs conforming to complex grammars that random muta- |  |  |  |  |  |  |  |  |  |  |  |  |
| proves essential. On the other hand, CRSs also unexpect- | tion cannot satisfy. Examples include | curl | protocol exploita- |  |  |  |  |  |  |  |  |  |  |
| edly underperform on annotated solvable challenges. The | tion requiring TLV-formatted inputs [16] ( | cu2 | ▲ | 06 | ), and struc- |  |  |  |  |  |  |  |  |
| causes are multifaceted: system-wide failures ( | TB | , | TI | ceased | tured file formats like PDF with embedded XFA ( | pb1 | □ | 01 | ) |  |  |  |  |
| after P3–P4), critical bugs ( | 42 | ’s patch submission issue, | SP | ’s | or XLSX for SSRF ( | po1 | ▲ | 05 | ). CRSs can extract format spec- |  |  |  |  |
| configuration issue, | AT | ’s Java | poi | failure, etc), and the long | ifications from the source code and use them to generate |  |  |  |  |  |  |  |  |
| tail of real-world edge cases that automated systems cannot | syntactically valid inputs. |  |  |  |  |  |  |  |  |  |  |  |  |
| generically handle. This leads to an interesting observation: a | Solving logical constraints. | Some CPVs guard vulnerable |  |  |  |  |  |  |  |  |  |  |  |
| CRS that reliably applies annotation techniques in real-world | paths with constraints that defeat fuzzer feedback mecha- |  |  |  |  |  |  |  |  |  |  |  |  |
| conditions would rank among the top three. Besides, | AT | ’s | nisms: regex patterns ( | cc1 | ▲ | 03 | , | po1 | ▲ | 06 | ), encoding transfor- |  |  |
| dominance concentrated in P3–P7 (Figure 3), where many | mations like URL encoding ( | cc4 | ▲ | 06 | ), Unicode normalization |  |  |  |  |  |  |  |  |
| teams underperformed against annotation expectations. | ( | cc6 | ▲ | 07 | , | po1 | □ | 02 | ), or zlib compression ( | pb1 | ▲ | 02 | ), symlink- |

KF 2. AIxCC’s challenges favor real-world coverage over

difficulty. Annotation techniques plus strong system-level

solutions could have secured top-three.

7.3 PoV Generation Analysis

PF-Solvable CPVs. PF annotates 34 of 63 CPVs (54%) as

solvable, but C and Java differ sharply: 30/40 in C (75%) ver-

sus only 4/23 in Java (17%). Three factors make Java harder

for fuzzing: ➀ inputs have richer semantic constraints ( e . g .,

XML); ➁ many timeout/OOM CPVs are fuzzer-unfriendly;

➂ default OSS-Fuzz seeds for Java are lower quality. Interest-

ingly, on the C side, wireshark ( ws* ), shadowsocks ( ss* ), and

systemd ( sd* ) contain mostly PF-solvable CPVs by design.

required sustained stability.

fuzzing enhancements were explored by only a few teams

based path obfuscation ( cc7 ▲ 08 ), and mathematical guards

( cc5 ▲ 10 , tk6 ▲ 10 ). LLMs can reason about these transforma-

tions and generate constraint-satisfying inputs.

KF 3. LLMs complement coverage-based fuzzing in di-

rected (delta-mode) and constraint-heavy contexts.

PF-Solvable CPVs Missed by CRSs. In contrast, these

misses stem not from detection capability, but from trivial yet

critical pipeline gaps in handling real-world complexity.

Broken system dependencies. Some CPs deviate from stan-

dard OSS-Fuzz setups and break CRS initialization: av2 ▲ 02

uses FuzzTest with its own fuzzer instantiation, while pdfbox

CPs ship their own jazzer that overrides the CRS’s pre-

installed copy.

disk exhaustion or OOM.

discarded valid PoVs.

| The organizer’s challenge notes in these projects indicate they | Heavy build process. | Unexpected resource demands can |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| were intended to evaluate patching and deduplication, not | exhaust CRS nodes. Typically, | wireshark | (4.9M LoC) pro- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PoV difficulty. Since they appear in P3–P7, scoring on them | duces 47 harnesses of | ∼ | 20.9 GB each ( | ∼ | 1 TB total), causing |  |  |  |  |  |  |  |  |  |  |  |
| CRS over PF. | Six CRSs solved 7–16 CPVs that PF could | Reproduction behavior mismatch. | CRSs’ reproduction cri- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| not (totaling 8/14 in C/Java), indicating substantial improve- | teria can differ subtly from organizer criteria. Some stateful |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ment over PF alone. This advantage can be largely attributed | bugs require multiple executions to trigger: | sd1 | □ | 05 | crashes |  |  |  |  |  |  |  |  |  |  |  |
| to LLM components, since LLM-based generation is the | on the second execution, and the organizer runs 100 times |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| most widely developed addition beyond PF, while non-LLM | by default. Thus, CRSs verifying with a single execution |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (§6.1). Another direct example: | TB | , | TI | , and | FB | built bug- | Incorrect sanitizer. | Some vulnerability classes require spe- |  |  |  |  |  |  |  |  |
| finding stacks consisting mostly of basic parallel fuzzing plus | cific sanitizers: | da1 | □ | 01 | (signed integer overflow) needs UB- |  |  |  |  |  |  |  |  |  |  |  |
| LLM components, yet all solved multiple CPVs PF missed. | San [36], not ASan [49]. Several teams included UBSan, yet |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Overall, CRSs exhibit three distinct capabilities. | only | TB | handled this CPV correctly. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Strong targeted detection. | Delta challenges dominate non- | Crash deduplication granularity. | ss1 | □ | 00 | – | ss1 | □ | 04 | are dis- |  |  |  |  |  |  |
| PF-solvable CPVs solved by CRSs (15/22). Given diff- | tinct heap-buffer-overflows in | json_parse_ex | , differing only |  |  |  |  |  |  |  |  |  |  |  |  |  |
| based hints about vulnerability locations, CRSs analyze code | by line number. Coarse-grained deduplication (libfuzzer to- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| changes and generate triggering inputs directly. Representa- | kens, function-level grouping, similarity) failed to distinguish |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tive cases include | fp2 | ▲ | 02 | , | mg1 | ▲ | 01 | (C), and | cc1 | ▲ | 03 | , | po1 | ▲ | 05 | them as separate vulnerabilities. Engineering can fix these |

---

## Page 11

| gaps, but at the cost of domain expertise and careful per-case | tant ( | av2 | ▲ | 02 | , | sd1 | □ | 05 | , | pb1 | □ | 03 | , | pb1 | □ | 04 | ). For timeout CPVs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| verification. This raises an open question that no team has | ( | pb1 | □ | 03 | , | pb1 | □ | 04 | , | po1 | ▲ | 06 | , | pb1 | □ | 08 | ), a common error is insert- |
| tried: can LLM integration lower the expertise cost and gen- | ing a hard-coded iteration limit instead of fixing the infinite |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| eralize robustness more broadly? | loop root cause. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

CPVs Unsolved by Both PF and CRSs. These CPVs in-

dicate two distinct limits. ➀ Reasoning gaps. Multi-step

cryptographic transformations ( cu3 ▲ 07 : XOR/shift; cu4 ▲ 08 :

AES with Base64 encoding) accumulate LLM errors end-to-

end, where tool-assisted verification could help. ➁ Fuzzing

pipeline limitations. The pdfbox ExtractTextFuzzer harness

embeds four timeout and two OOM CPVs ( pb1 □ 03 – pb1 □ 08 )

that expose two coupled weaknesses. First, timeouts produce

near-identical crash signatures, so deduplication collapses

distinct bugs into one. Second, a shallow timeout, once hit,

keeps re-firing and prevents the fuzzer from reaching deeper

bugs: once pb1 □ 07 triggers, repeated timeouts block explo-

ration of pb1 □ 05 and pb1 □ 06 . No CRS attempted on-the-fly

patching to bypass shallow timeouts or fine-grained timeout

deduplication, yielding minimal coverage on this harness.

7.4 Patch Generation Analysis

33 of 63 CPVs as patchable, respectively, with 36 unique

CPVs covered in total. Although more than half of all CPVs

are covered, this does not indicate superior patching capa-

ing logic, when root cause and crash location are dis-

Incomplete fix. Agents can fix the specific crashing path

so agents patched the reported files but missed it. Other cases

include the XXE-parser hardening of pb1 □ 00 that omits a crit-

ical security setting, and the dangling-pointer cases ( sd1 □ 05 ,

ex2 ▲ 01 ) where patches go at the call site instead of inside the

buggy memory API.

Functionality deviation. Some patches eliminate the crash

but subtly alter program semantics in ways that functional

tests do not cover ( e . g ., ws2 □ 04 , ws1 □ 02 , ws1 □ 05 , ws1 □ 11 ,

lx3 ▲ 04 , sd1 □ 01 , tk6 ▲ 10 , fp3 ▲ 03 ). In av2 ▲ 02 , a patch pro-

duces incorrect edge colors because YUV-to-RGB conversion

depends on neighboring pixels that the patch mishandles. In

cc7 ▲ 08 , a patch resolves relative symbolic links to absolute

paths during archive extraction, when it should only validate

against path traversal without modifying the link target.

Introducing new bugs. In ss1 □ 00 , an extra break renders

part of the encoding logic unreachable; in sd1 □ 05 , removing

requires understanding how GVCP [1] bootstrap registers,

which are standardized memory-mapped addresses for de-

vice discovery, are managed within the project. In ws1 □ 01 ,

patches confused self-reported packet lengths with verified

KF 6. Claude Code slightly outperforms MultiRetrieval,

but both suffer 38–46% semantic incorrectness.

remain prevalent overall.

| KF 4. | Robust pipeline construction (build, sanitizers, | instead of completely remediating the underlying bug. In |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dedup, reproduction) is non-trivial, yet agentic solutions | mongoose | ( | mg1 | □ | 00 | , | mg1 | ▲ | 01 | , | mg2 | ▲ | 02 | ), | #line | directives hide |  |
| remain under-explored. | the amalgamated compilation unit from the sanitizer reports, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| KF 5. | Unresolved bugs reveal either reasoning gaps or | a | mfree | call introduces a memory leak. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| fuzzing pipeline limitations. | Missing domain knowledge. | In | ws7 | ▲ | 13 | , correct patching |  |  |  |  |  |  |  |  |  |  |  |
| MR/CC Patchable CPVs. | MR and CC annotate 31 and | ones, missing the knowledge to tell them apart. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| bility; rather, it reflects that MR and CC can solve basic fix | CRS over MR/CC. | On one hand, CRSs solved 16 cases |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| challenges where the root cause is directly surfaced by the | where MR/CC failed, demonstrating capabilities beyond foun- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| sanitizer report and the local code context suffices to derive | dational agents, such as the correct fixes for incomplete reme- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| a fix without cross-reference reasoning: textbook vulnera- | diations ( | sd1 | □ | 05 | , | ex2 | ▲ | 01 | ), functionality deviations ( | ws1 | □ | 11 | , |  |  |  |  |
| bilities with well-known fix patterns. Typical examples in- | lx3 | ▲ | 04 | , | sd1 | □ | 01 | , | tk6 | ▲ | 10 | ), and misleading sanitizer reports |  |  |  |  |  |
| clude boundary checks for buffer overflows ( | fp2 | ▲ | 02 | , | ss1 | □ | 00 | – | ( | mg2 | ▲ | 02 | , | mg1 | □ | 00 | ) listed in the previous paragraph. On the |
| ss1 | □ | 04 | ), secure XML parser configuration for XML External | other hand, CRSs also suffer from semantically incorrect |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Entity (XXE) ( | pb1 | □ | 00 | , | pb1 | □ | 01 | ), decode-then-normalize re- | patches, though mostly at lower rates than MR/CC (Table 10). |  |  |  |  |  |  |  |  |
| ordering for path traversal ( | cc4 | ▲ | 06 | , | cc6 | ▲ | 07 | ), single-line fixes | AT | and | TB | achieve 83.8% and 79.2% patch accuracy, respec- |  |  |  |  |  |
| such as null checks and format-string corrections ( | cm1 | □ | 01 | , | tively; | SP | reaches 100%, though this likely reflects strict |  |  |  |  |  |  |  |  |  |  |
| cu5 | ▲ | 01 | ), and CTF-style backdoors labelled by a “flag” string | patch filtering ( | e | . | g | ., its 5-minute post-patch fuzzing step) and |  |  |  |  |  |  |  |  |  |
| that simply need deletion ( | cu2 | ▲ | 06 | , | sd1 | □ | 03 | , | cc5 | ▲ | 10 | ). | patched challenge distribution rather than full mitigation of |  |  |  |  |
| Semantically Incorrect Patches from MR/CC. | A no- | semantic correctness. In contrast, | TI | and | FB | fall to 31.7% and |  |  |  |  |  |  |  |  |  |  |  |
| table fact is that a significant fraction of generated patches | 23.3% accuracy, concentrated in bursts of invalid submissions |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| pass all automatic validation, yet contain semantic issues | on one or two challenges, likely tied to strategy issues such as |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| caught only by manual review (CC: 20/53, 37.7%, MR: | parallel generation without adequate deduplication. Despite |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 26/57, 45.6%). | Wrong root cause. | Agents may suppress | these differences, a common factor among higher-accuracy |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the crash symptom rather than addressing the underlying | CRSs is the adoption of multi-PoV validation, post-patch |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| defect. One typical pattern is defensive patching in pars- | fuzzing, or LLM-based reflection (§6.2), yet incorrect patches |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 12

KF 7. High-accuracy CRSs can achieve 16–21% semantic

incorrectness, substantially below MultiRetrieval/ Claude

Code’s 38–46% but still non-negligible.

stem not from capability gaps but from other factors: miss-

pressure from too many concurrent PoVs, and system-wide

stability issues discussed earlier. Interestingly, one identifi-

the wireshark build alone, leaving insufficient time for the

CPVs Failed by both CRSs and MR/CC. Seven Java CPVs

were never patched: 4 infinite loops ( pb1 □ 03 , pb1 □ 04 , pb1 □ 08 ,

po1 □ 00 ), 1 integer overflow ( pb1 □ 06 ), 1 ReDoS ( po1 ▲ 06 ),

and 1 JVM crash via obfuscated backdoor ( po1 □ 03 ). These

cases reveal two limitations of current patching. ➀ Reasoning

gaps. For example, ReDoS ( po1 ▲ 06 ) requires regex worst-

case reasoning that agents cannot perform reliably end-to-end;

integrating non-LLM regex analysis tools such as symbolic

regex repair [35] could help. ➁ Patch pipeline limitations.

Current patch pipelines rely heavily on crash stack traces

from the PoV/fuzzing side for root cause analysis, which

degrades sharply when such signals are absent. The pdfbox

infinite-loop CPVs and po1 □ 03 demonstrate this: timeouts

and JVM-level crashes give only minimal localization, and

most CRSs failed on these cases. Approaches that go beyond

this limitation remain to be explored.

reasoning gaps or patch pipeline limitations.

Noteworthy No-PoV Patches in shadowsocks. In

shadowsocks ( ss1 □ 00 – ss1 □ 04 ), three CRSs patched CPVs

for which they had no PoV, even though two of them require

PoVs to generate patches. This was possible because all five

heap-buffer-overflows represent the same bug pattern repeated

at different locations within a large JSON parsing function;

some CRSs recognized the pattern and generated patches that

fixed all instances together.

Table 8: Bundle strategies and results. Team abbr: Table 2.

| AT | TB | TI | FB | SP | 42 | LC | Total |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PoV-Patch | 27/28 | 18/18 | 16/18 | 6/9 | 7/7 | 4/4 | 1/1 | 79/85 |
| Patch-SARIF | – | – | 1/1 | 0/2 | – | – | – | 1/3 |
| Accuracy | 35/36 | 19/19 | 17/19 | 8/13 | 7/7 | 4/4 | 1/1 | 91/99 |

10/13 and SP 9/13.

accuracy is high (91/99, 92%): all seven teams adopted PoV-

racy. Patch-SARIF, the only non-PoV pairing, achieved 1/3

accuracy. Of the 8 incorrect bundles, only one is a true pair-

ing mismatch; the other 7 failed due to unsuccessful patches,

confirming patch quality as the practical bottleneck.

Resource Usage and Efficiency. No team consumed the full

quota of either resource; Table 9 reports per-team breakdowns.

➀ LLM spending concentrates in two providers: ∼ 94% on

Anthropic and OpenAI, ∼ 6% on Gemini and xAI. ➁ LLM

spend rank closely tracks the final score, with only FB and TI

flipping the order. ➂ From a cost-efficiency view (score per

$K total spend), TI , TB , and AT lead.

0-Day Discovery. All seven teams discovered at least one

0-day, yielding 25 distinct vulnerabilities across 10 OSS

projects, of which 12 (48%) were patched (Figure 3 (ii, iv)).

See [9] for more details. Responsible disclosure was coordi-

nated by Kudu Dynamics with OSTIF and ADALogics.

From Competition to Industry Deployment. Reflecting on

the competition, we identify several areas where future efforts

could further ease the path to practical deployment.

In the final, CRSs operated on self-provisioned Azure clus-

ters with budgets of hundreds of dollars per challenge, en-

suring resource availability would not limit technical explo-

ration. This contrasts with individual developers or small

teams who need lightweight, single-machine solutions at min-

imal cost. Although finalist CRSs have been open-sourced,

their resource usage models and runtime environments differ

ers to post-competition adoption. Future work could develop

| MR/CC Patchable CPVs Failed by CRSs. | Most CRSs in- | PoV-SARIF | 1/1 | – | – | – | – | – | – | 1/1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| corporate comparable patch agents, so these 9 failures likely | PoV-Patch-SARIF | 7/7 | 1/1 | – | 2/2 | – | – | – | 10/10 |  |
| ing PoVs that never triggered patch generation, scheduling | Score | 136.2 | 65.1 | 49.8 | 26.4 | 25.3 | 11.0 | 3.2 | 316.9 |  |
| able cause is | deployment-time configuration trade-offs | . For | to fewer submissions ( | AT | : 8, | FB | : 7, | TB | : 1). With PoV evidence, |  |
| example, | ws5 | ▲ | 08 | is locally patchable by MR (one agent in | FB | and | TB | achieved 100% accuracy, but | AT | falsely matched |
| AT | ), but | AT | ’s 30-minute per-CPV timeout, necessary to man- | PoVs to 2 invalid reports. In contrast, non-PoV-centric teams |  |  |  |  |  |  |
| age dozens of concurrent challenges, is largely consumed by | can assess all broadcasts but risk wrong answers: | 42 | scored |  |  |  |  |  |  |  |
| patch loop to complete. | Bundle Results. | Table 8 shows bundle outcomes. Overall |  |  |  |  |  |  |  |  |
| KF 8. | Pipeline construction challenges and patch-strategy | based patch generation (§6.4) that naturally pairs PoVs with |  |  |  |  |  |  |  |  |
| tradeoffs can limit CRSs’ performance. | their patches, accounting for 86% of bundles with 93% accu- |  |  |  |  |  |  |  |  |  |
| KF 9. | As with bug finding, unresolved patches face either | 8 | Lessons and Future Directions |  |  |  |  |  |  |  |
| 7.5 | Other Analyses | substantially from typical deployment settings, posing barri- |  |  |  |  |  |  |  |  |
| SARIF Validation. | Figure 3 (v) presents SARIF validation | resource-efficient CRS variants that remain effective under |  |  |  |  |  |  |  |  |
| results across 13 broadcasts (8 valid, 5 invalid). PoV-centric | constrained environments; future competitions could also in- |  |  |  |  |  |  |  |  |  |
| teams (§6.3) can only submit | Correct | when a PoV matches; | troduce resource-limited tracks that account for the needs of |  |  |  |  |  |  |  |
| thus, they were unable to assess the 5 invalid reports, leading | individual developers and small teams. |  |  |  |  |  |  |  |  |  |

---

## Page 13

| Beyond resource constraints, OSS communities need time | are complementary and mutually beneficial. On one hand, |
| --- | --- |
| to adapt their pipelines for CRS integration, such as provision- | pure-LLM pipelines still carry fundamental limitations such |
| ing LLM services, standardizing CRS interfaces for broader | as hallucination and nondeterminism, so the LLM–non-LLM |
| OSS applications, defining end-to-end workflows from AI- | cooperation patterns established in AIxCC remain a direct and |
| assisted bug finding to patch submission, and ensembling | meaningful reference for CRSs built on top of stronger base |
| multiple CRSs for combined effectiveness. Considering these | models. On the other hand, stronger LLMs also open room |
| needs at the design stage would lower adoption barriers for | for the next generation of CRSs to simplify their architectures |
| OSS maintainers and practitioners. On the post-competition | and push autonomy further. |

side, initiatives like OSS-CRS [52] have begun to address

these needs; future competitions could learn from this by co-

designing deployment pathways with OSS communities for

smoother transition to real-world adoption.

From Competition to Research Advancement. The compe-

tition design and team-built systems hold significant research

value, yet certain design improvements could be made to

further enlarge their value as research assets.

open-source models offer distinct value to the OSS commu-

nity through lower cost, customizability, and transparency. A

dedicated sub-track comparing CRS performance under open-

source models would encourage exploration in this direction.

Areas of Expansion. As the first large-scale competition of

its kind, AIxCC necessarily scoped its focus. Several direc-

tions not covered in this iteration are worth exploring in future

editions: full autonomy (generating harnesses and handling ar-

bitrary build systems), multi-CRS settings (collaborative anal-

ysis or adversarial formats where CRSs attack competitors’

patches), and semantic correctness evaluation (approaches

for patch semantic correctness).

AI-Powered Vulnerability Scanning. Early 2026 has seen

notable advances in frontier LLMs’ cybersecurity capabilities,

with works like Claude Mythos Preview [3] and coding agent

patch evaluation [57] showing striking performance in bug

finding and repair. The capability jump signals further rapid

9 Limitations

Our study has three notable limitations. ➀ Taxonomy in-

terpretation. We strictly follow enabled functionalities in

submission-version code, treating code as authoritative when

it conflicts with questionnaire or meeting records; two security

experts cross-validated each profile, and the final taxonomy

10 Conclusion

AIxCC represents a milestone in autonomous cybersecurity re-

search, demonstrating that AI-powered CRSs can discover and

patch vulnerabilities in real-world software at scale. Through

systematic analysis of competition design, CRS architectures,

and results, we summarized technical insights of those sys-

tems, revealed both their genuine performance advances and

the persistent gap between technique capability and system

reliability. We hope this work serves as a foundation for fu-

ture competition designs, CRS development, and practical

deployment of autonomous cybersecurity systems.

Acknowledgments

| AIxCC is intrinsically a substantial experimental invest- | was shared with all seven teams (three had bandwidth and |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ment, yet its telemetry primarily serves real-time monitoring | confirmed). Still, any misreading of the source would propa- |  |  |  |  |
| and scoring rather than retrospective analysis of | why | sys- | gate as taxonomy misinterpretation. | ➁ | Annotation accuracy. |
| tems behaved as they did. Designing telemetry with post-hoc | PF/MR/CC annotation is an approximation under estimated |  |  |  |  |
| analysis as a first-class goal—logging intermediate outputs, | resources and selected techniques. On the PoV side, longer |  |  |  |  |
| decision traces, and environmental snapshots—would enable | fuzzing, a different fuzzer framework, or some teams’ private |  |  |  |  |
| systematic studies of failure modes and technique effective- | initial corpora could each mark additional CPVs as solvable; |  |  |  |  |
| ness. Organizer-built baseline CRSs participating alongside | the annotation is thus an approximation of what this represen- |  |  |  |  |
| teams would further enrich such analysis by providing refer- | tative configuration would solve in AIxCC, not a general claim |  |  |  |  |
| ence points for comparison. | about fuzzing capability. We run each technique three times |  |  |  |  |
| The competition’s exploration of open-source LLMs was | and take the union as a stable lower bound. | ➂ | No ablation |  |  |
| minimal: although two teams fine-tuned open-source models, | study. | The most accurate way to understand the techniques |  |  |  |
| only one ultimately deployed them. The competition structure | used by these teams would be to migrate them into a single |  |  |  |  |
| offered little incentive to invest in open-source models, as | platform and measure their contributions under controlled |  |  |  |  |
| the uncertainty, cost, and data-acquisition difficulty of fine- | resources. We believe this is out of scope for a SoK given the |  |  |  |  |
| tuning made prompt-based techniques on frontier commercial | resource cost (CRSs use LLMs heavily) and engineering cost |  |  |  |  |
| models a more predictable and cost-effective strategy. While | (CRSs are large, heterogeneous systems). Post-competition |  |  |  |  |
| advancing frontier AI for cybersecurity is a natural focus, | efforts such as OSS-CRS [52] are working on this direction. |  |  |  |  |
| progress in both offensive and defensive automation, which | This work is a joint effort of multiple teams and organiza- |  |  |  |  |
| is exactly the future AIxCC was set up to prepare for. Tech- | tions involving dozens of contributors, who collectively aim |  |  |  |  |
| nically, AIxCC’s exploration and this LLM capability surge | to provide a systematic and insightful view of the AIxCC |  |  |  |  |

---

## Page 14

| competition. We are grateful to every one of them for making | infrastructure and implementation. Jon Silliman and Mikel |
| --- | --- |
| this work possible and highlight their primary contributions. | Mcdaniel ensured the paper statistics and data aligned with |
| This work was initiated and directed by Taesoo Kim, who | the competition dataset and results. We also thank DARPA for |
| supervised the entire research process. Cen Zhang led the | its generous support and prompt responses to our inquiries, |
| structure design, the CRS code study and team meetings, | including granting full access to the challenge source code |
| cross-team collaboration, coordination with contributors to | and competition data. |
| distill the core findings of each part, and the paper drafting. | This research was supported by the Advanced Research |
| Younggi Park implemented the patch analysis framework, con- | Projects Agency for Health (ARPA-H) under Other Trans- |
| ducted the experiments, manually validated agent-generated | action Agreement No. 140D042590046, and by a gift from |
| patches, and helped analyze and draft the patch analysis find- | Team Atlanta. |

ings. Fabian Fleischer verified and integrated competition

data, visualized the results (such as Figure 3), helped validate

Ethical Considerations

patches and drafted patch analysis, and prepared the artifact.

| Yu-Fu Fu compiled team statistics, studied and summarized | Stakeholder Identification. | We identify three primary stake- |  |  |
| --- | --- | --- | --- | --- |
| CRS patch systems of all teams, and helped draft the patch | holder groups. | (1) Researchers and practitioners | : the seven |  |
| techniques. Jiho Kim conducted PoV generation analysis in | finalist teams, competition organizers (DARPA, ARPA-H, and |  |  |  |
| §7.3 and contributed to the discussions in §8. Dongkwan | Kudu Dynamics), and security researchers who may build |  |  |  |
| Kim contributed in team meeting discussions, conducted the | upon our findings, whose system designs, performance data, |  |  |  |
| parallel fuzzing experiments, authored §7.5, studied teams’ | and strategic decisions are analyzed in detail. | (2) Open-source |  |  |
| bundling strategies, and helped draft §6.4. Youngjoon Kim | community | : developers and maintainers of the 24 open-source |  |  |
| studied CRS SARIF techniques of all teams and some teams’ | projects from which challenge projects were derived, as well |  |  |  |
| CRSs during the early code study, authored §4, and helped | as the broader OSS ecosystem that depends on the security of |  |  |  |
| draft §6.3. Qingxiao Xu analyzed the inaccurate patch sub- | these projects. | (3) LLM vendors | : whose models were used by |  |
| missions across teams, and both Qingxiao Xu and Ze Sheng | competing teams and whose API usage patterns are discussed. |  |  |  |
| assisted with the analysis in §7.5. Andrew Chin studied some | Ethical Principles. | Beneficence. | This work advances the |  |
| CRSs’ bug finding techniques during the early code study, | understanding of autonomous Cyber Reasoning Systems and |  |  |  |
| cross-validated the technique taxonomy in §6, and helped | their application to real-world vulnerability detection. By sys- |  |  |  |
| check and refine the paper during the final stages. The above | tematically analyzing competition design, CRS architectures, |  |  |  |
| Team Atlanta authors, along with Hanqing Zhao, authors from | and performance outcomes, we provide actionable insights for |  |  |  |
| Team Fuzzing Brain (Jeff Huang, Ze Sheng, and Qingxiao | the OSS security community, future competition organizers, |  |  |  |
| Xu), and Team Lacrosse (Michael Pelican, David J. Musliner), | and researchers building autonomous security systems. |  |  |  |
| cross-validated the technique taxonomy in §6 and conducted | Respect for Persons. | We had discussions with organizers |  |  |
| proofreading. We also thank external contributors: Joshua | and competing teams to gather firsthand accounts of design |  |  |  |
| Wang for help with taxonomy cross-validation and proofread- | decisions and operational experiences, and maintained ongo- |  |  |  |
| ing, and Brian J. Lee for help preparing the artifact. | ing communication throughout the writing process to ensure |  |  |  |
| We sincerely thank the remaining four AIxCC teams—Trail | accurate representation of their work. The AIxCC competition |  |  |  |
| of Bits (Michael Brown), Theori (Tyler Nighswander), Shell- | rules permitted publication of CRS source code, performance |  |  |  |
| phish (Wil Gibbs and Yan Shoshitaishvili), and 42-b3yond- | data, and architectural details; all finalist teams were aware |  |  |  |
| 6ug (Xinyu Xing)—for their support, feedback, discussions, | that their systems and results would be analyzed, and were |  |  |  |
| and meetings, as well as the internal materials they shared | given draft sections for review (3 confirmed). |  |  |  |
| ( | e.g. | , Wil Gibbs shared Shellphish’s internal white paper), | Justice. | All seven finalist teams are analyzed with equal |
| which helped shape our understanding of each CRS’s over- | rigor and presented with consistent methodology. No team is |  |  |  |
| all design motivations. Xinyu Xing also shared his insights | singled out or unfairly characterized. We did not re-evaluate |  |  |  |
| and reflections on the competition, such as the gap between | any team’s CRS independently; all performance data origi- |  |  |  |
| research and practice, during early discussions of this work. | nates from the final competition results. The organizers have |  |  |  |
| Kudu Dynamics, as the competition organizer, provided | no conflict of interest with any of the seven finalist teams |  |  |  |
| raw materials on competition design from the organizer’s per- | and conducted fair evaluation through extensive communica- |  |  |  |
| spective, shared competition data and continually updated it as | tion and documentation. Competition data will be publicly |  |  |  |
| our analysis needs evolved, and held weekly meetings for com- | released to ensure transparency and reproducibility, subject |  |  |  |
| munication and coordination. Nicholas Vidovich and Matthew | to DARPA’s approval and disclosure guidelines. |  |  |  |
| Lehman led the organizer collaboration effort and contributed | Respect for Law and Public Interest. | The AIxCC compe- |  |  |
| organizer-side content and review. Isaac Goldthwaite con- | tition operated under DARPA and ARPA-H research frame- |  |  |  |
| tributed content on competition rules, challenges, and scor- | works, with all teams agreeing to rules governing data han- |  |  |  |
| ing. Jefferson Casavant contributed content on competition | dling and disclosure. 0-day vulnerabilities were reported |  |  |  |

---

## Page 15

| through responsible disclosure processes in compliance with | systematic analysis of its design, CRS approaches, or out- |  |
| --- | --- | --- |
| applicable laws. We document our methodology and data | comes existed prior to this work. We determined that the re- |  |
| sources to enable reproducibility; competition data will be | search was justified by the need to document lessons learned, |  |
| publicly released to ensure transparency and accountability. | identify genuine technical advances, and surface open chal- |  |
| Potential Harms. | This work does not involve human sub- | lenges for security research. |
| jects or private user data. Discussions with teams focused | Decision to publish. | The decision to publish was made |
| on technical methodology and system architecture, not per- | after communicating with all participating teams, competition |  |
| sonal or sensitive information. We identify three potential | organizers, and sponsoring agencies. We believe our insights |  |
| tangible harms. First, | misinterpretation of performance data | on CRS design and implementation will benefit future CRS |
| could cause reputational or financial harm to specific teams if | developers and software security researchers. Since we also |  |
| rankings or analyses are taken out of context. Second, | 0-day | provide insights into vulnerability repair techniques, the secu- |
| vulnerability exposure | could be exploited by malicious actors | rity benefits outweigh potential dual-use risks. |

before patches are available. Third, dual-use concerns arise

on multiple paths: adapting CRS architectures for automated

exploit generation, leveraging our taxonomy to accelerate

offensive tool development, and misusing competition data

(particularly team-found 0-day PoCs) for real-world attacks

before patches reach end users.

Mitigations. We took the following steps to address these

risks. For misinterpretation of performance data , each section

was cross-validated by at least two authors. We also had dis-

cussions with all seven finalist teams and maintained regular

communication throughout the writing process to ensure accu-

rate representation. For 0-day vulnerability exposure , all 0-day

vulnerability data originates exclusively from the final compe-

ics coordinate with each affected upstream maintainer via

private channels (typically email or security mailing lists),

share PoVs and remediation guidance, and embargo public

details until fixes are released or a standard 90-day window

elapses. All discovered 0-day vulnerabilities have been re-

ported through this process; detailed 0-day information is

not included in this paper or its artifacts. For dual-use con-

cerns , CRS performs not only vulnerability detection but also

faster than malicious actors can exploit them, CRS contributes

production-grade engineering, with inherent burnout risks.

Evolving competition rules and rapidly advancing AI capa-

bilities required teams to continuously adapt, adding further

pressure. Some teams’ final outcomes were undermined by

system instability rather than capability gaps, which can be

sections were shared with all seven teams for review.

Decision to Conduct and Publish. Decision to research.

Open Science

All data, scripts, finalist team questionnaires, and meeting

notes are archived in our artifact [8], with a companion web-

site [9] indexing the artifact, our extended analysis, public

finalist documentation, and official challenge set access links;

competition data and the analysis framework await DARPA’s

official release.

References

-gige-vision .

[2] Anthropic. Claude Code: An agentic coding tool that

lives in your terminal, 2025. https://github.com/a

nthropics/claude-code .

[3] Anthropic. Claude Mythos Preview, 2026. https:

//red.anthropic.com/2026/mythos-preview/ .

[6] Cornelius Aschermann, Tommaso Frassetto, Thorsten

Holz, Patrick Jauernig, Ahmad-Reza Sadeghi, and

Daniel Teuchert. Nautilus: Fishing for deep bugs with

grammars. In NDSS , volume 19, 2019.

Privacy (SP) , 2020.

| tition environment. Disclosure began shortly after the August | [1] AIA (Association for Advancing Automation). GigE |  |  |
| --- | --- | --- | --- |
| 2025 final and remains ongoing through standard responsible | Vision standard. URL: | https://www.automate.org |  |
| disclosure protocols: Kudu Dynamics, OSTIF, and ADALog- | /vision/vision-standards/vision-standards |  |  |
| vulnerability repair. This aligns with the philosophy of OSS- | [4] Apache Software Foundation. Apache Maven Project. |  |  |
| Fuzz: by enabling defenders to find and patch vulnerabilities | https://maven.apache.org/ | , 2025. |  |
| positively to defense. | [5] Abhishek Arya, Oliver Chang, Jonathan | Metzman, |  |
| Team Well-being. | AIxCC spanned two years, demanding | Kostya Serebryany, and Dongge Liu. OSS-Fuzz. | https: |
| long-term commitment across both cutting-edge research and | //github.com/google/oss-fuzz | . |  |
| particularly frustrating after such sustained investment. For | [7] Cornelius Aschermann, Sergej Schumilo, Ali Abbasi, |  |  |
| this study, all participating teams consented to questionnaires | and Thorsten Holz. IJON: Exploring deep state spaces |  |  |
| in flexible formats depending on their availability, and draft | via fuzzing. In | 2020 IEEE Symposium on Security and |  |
| AIxCC represents the largest competition to date for LLM- | [8] Authors. AIxCC SoK Artifact. | https://zenodo.org |  |
| based autonomous vulnerability detection and repair, yet no | /records/20367274 | , 2026. |  |

---

## Page 16

| [9] Authors. | AIxCC SoK Companion Website. | https: | [25] Free Software Foundation. | GDB: The GNU project |  |
| --- | --- | --- | --- | --- | --- |
| //occia.github.io/aixcc-sok-webpage/ | , 2026. | debugger. | https://sourceware.org/gdb/ | , 2026. |  |
| [10] BerriAI. LiteLLM: Call 100+ LLM APIs in OpenAI | [26] Yu-Fu Fu, Jaehyuk Lee, and Taesoo Kim. autofz: Au- |  |  |  |  |
| format. | https://github.com/BerriAI/litellm | . | tomated Fuzzer Composition at Runtime. | In | 32nd |

[11] Tim Blazytko, Moritz Schlögel, Cornelius Aschermann,

Ali Abbasi, Joel Frank, Simon Wörner, and Thorsten

Holz. AURORA: Statistical crash analysis for auto-

mated root cause explanation. In 29th USENIX Security

[13] Harrison Chase. LangChain, 2022. https://github

[14] Yuanliang Chen, Yu Jiang, Fuchen Ma, Jie Liang,

[15] Universal Ctags. ctags. https://github.com/uni

versal-ctags/ctags , 2025.

[16] curl project. curl-fuzzer: Quality assurance testing for

the curl project. https://github.com/curl/curl

-fuzzer , 2025.

.com/ast-grep/ast-grep , 2026.

w.darpa.mil/research/programs/cyber-grand

-challenge .

//aicyberchallenge.com/ .

[22] EclEmma. JaCoCo: Java code coverage library. https:

//www.eclemma.org/jacoco/ , 2026.

[23] Andrea Fioraldi, Dominik Maier, Heiko Eißfeldt, and

Marc Heuse. AFL++: Combining incremental steps

[24] Andrea Fioraldi, Dominik Maier, Dongjia Zhang, and

USENIX Security Symposium (Security) , 2023.

[27] Paul Gauthier. Aider: AI pair programming in your

terminal, 2025. https://aider.chat/ .

//codeql.github.com/ .

tps://github.com/google/clusterfuzz , 2026.

[31] Andrej Karpathy. Vibe Coding, 2025. https://x.co

m/karpathy/status/1886192184808149383 .

[32] Wonyoung Kim, Seunggi Min, Minjae Gwon, Dowoo

Baik, Haein Lee, Hyeon Heo, Minjae Lee, Min Woo

Baek, Yonghwi Jin, Younggi Park, Yunjae Choi, Taesoo

2026. arXiv:2601.17471 .

[34] Chris Lattner and Vikram Adve. LLVM: A compilation

framework for lifelong program analysis and transforma-

and Optimization , 2004.

Yang Xiao, Yanyan Zou, et al. VULCANBOOST: Boost-

ing ReDoS Fixes through Symbolic Representation and

Feature Normalization. In 34th USENIX Security Sym-

posium , 2025.

iorSanitizer.html .

| Symposium | , 2020. | [28] GitHub. CodeQL: The libraries and queries that power |  |  |
| --- | --- | --- | --- | --- |
| [12] ccache developers. | ccache: A fast C/C++ compiler | security researchers around the world, as well as code |  |  |
| cache. | https://ccache.dev/ | , 2025. | scanning in GitHub Advanced Security, 2025. | https: |
| .com/langchain-ai/langchain | . | [29] Google. Clusterfuzz: Scalable fuzzing infrastructure. | ht |  |
| Mingzhe Wang, Chijin Zhou, Xun Jiao, and Zhuo Su. | [30] Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xue- |  |  |  |
| Enfuzz: Ensemble fuzzing with seed synchronization | hao Zhai, Chengjin Xu, Wei Li, Yinghan Shen, Shengjie |  |  |  |
| among diverse fuzzers. In | 28th USENIX Security Sym- | Ma, Honghao Liu, et al. A survey on llm-as-a-judge. |  |  |
| posium (Security) | , 2019. | arXiv preprint arXiv:2411.15594 | , 2024. |  |
| [17] Herrington Darkholme. | ast-grep: A cli tool for code | Kim, Sangdon Park, and Insu Yun. Patchisland: Orches- |  |  |
| structural search, lint, and rewriting. | https://github | tration of llm agents for continuous vulnerability repair, |  |  |
| [18] DARPA. AIxCC Semifinal Competition. | https://ai | [33] LangChain, Inc. LangGraph: Build resilient language |  |  |
| cyberchallenge.com/semifinal-competition/ | . | agents as graphs, 2024. | https://github.com/lan |  |
| [19] DARPA. Cyber Grand Challenge, 2016. | https://ww | gchain-ai/langgraph | . |  |
| [20] DARPA. AI Cyber Challenge (AIxCC), 2025. | https: | tion. In | International Symposium on Code Generation |  |
| [21] DARPA. AIxCC Archive, 2025. | https://archive. | [35] Yeting Li, Yecheng Sun, Zhiwu Xu, Haiming Chen, |  |  |
| aicyberchallenge.com/ | . | Xinyi Wang, Hengyu Yang, Huina Chao, Cen Zhang, |  |  |
| of fuzzing research. | In | 14th USENIX Workshop on | [36] LLVM Project. UndefinedBehaviorSanitizer, 2025. | ht |
| Offensive Technologies | , 2020. | tps://clang.llvm.org/docs/UndefinedBehav |  |  |
| Davide Balzarotti. | LibAFL: A Framework to Build | [37] LLVM Project. FuzzedDataProvider: A helper class for |  |  |
| Modular and Reusable Fuzzers. In | 29th ACM Confer- | fuzz targets. | https://github.com/llvm/llvm-p |  |
| ence on Computer and Communications Security | , CCS | roject/blob/main/compiler-rt/include/fuzz |  |  |
| ’22, 2022. | er/FuzzedDataProvider.h | , 2026. |  |  |

---

## Page 17

| [38] Meta. | Infer: A static analyzer for Java, C, C++, and | [51] Noah Shinn, Federico | Cassano, Ashwin | Gopinath, |
| --- | --- | --- | --- | --- |
| Objective-C, 2025. | https://fbinfer.com/ | . | Karthik R Narasimhan, and Shunyu Yao. | Reflexion: |

tps://microsoft.github.io/language-serve

r-protocol/ , 2026.

abilities. International Journal on Advances in Security ,

and Tom Marble. Meta-control for adaptive cybersecu-

[43] David J. Musliner, Michael J. S. Pelican, Matthew

McLure, Steven Johnston, Richard G. Freedman, and

Corey Knutson. OpenMIND: Planning and adapting in

domains with novelty. In Advances in Cognitive Sys-

tems , 2021. URL: https://www.sift.net/sites

/default/files/publications/main_5.pdf .

[44] OASIS. Static Analysis Results Interchange Format

[45] OpenAI. Using Logprobs. https://developers.o

cle.com/en/java/javase/21/docs/specs/man

[48] Semgrep, Inc. Semgrep: Lightweight static analysis for

many languages, 2025. https://semgrep.dev/ .

A fast address sanity checker. In 2012 USENIX annual

[50] Wenxuan Shi, Hongwei Li, Jiahao Yu, Xinqian Sun,

2507.10845 .

language agents with verbal reinforcement learning. In

cessing Systems , 2023.

[52] SSLab, Georgia Tech. OSS-CRS: Open-Source Soft-

value-flow analysis in LLVM. In 25th International

tem, 2025. Cross-listed in cs.AI. arXiv:2509.14589 .

[56] Team 42 (b3yond 6ug). 42-b3yond-6ug Open Letter.

https://docs.google.com/document/d/1-1Te

xnOwQGj2KJ8rrLtk-Vgl-PqO5MZe7k0qrHQPC_0/ .

[57] Team Atlanta. Patching Vulnerabilities with Coding

Agents in 2026, 2026. https://team-atlanta.git

hub.io/blog/post-patch-2026-ensemble/ .

/blog/2025/08/22/shellphish-x-aixcc-pm/ .

thub.io/aixcc-public/afc/Branch%20Flipper

Martinet, Marie-Anne Lachaux, Timothée Lacroix, Bap-

cient foundation language models. arXiv preprint

arXiv:2302.13971 , 2023.

[61] Tree-sitter. Tree-sitter: An incremental parsing system

tps://github.com/wala/WALA , 2026.

Security Symposium , 2015.

| [39] Microsoft. Language Server Protocol specification. | ht | Thirty-seventh Conference on Neural Information Pro- |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| [40] MITRE. Common Weakness Enumeration (CWE). | ht | ware Cyber Reasoning System. | https://github.c |  |  |  |
| tps://cwe.mitre.org/ | , 2026. | om/sslab-gatech/oss-crs | , 2025. |  |  |  |
| [41] David J Musliner, Scott E Friedman, Michael Boldt, | [53] Stanford NLP. | DSPy: The framework for program- |  |  |  |  |
| J Benton, Max Schuchard, and Peter Keller. Fuzzbomb: | ming—not prompting—language models, 2025. | https: |  |  |  |  |
| Fully-autonomous detection and repair of cyber vulner- | //github.com/stanfordnlp/dspy | . |  |  |  |  |
| 9(3-4), 2016. | [54] Yulei Sui and Jingling Xue. SVF: Interprocedural static |  |  |  |  |  |
| [42] David J. Musliner, Scott E. Friedman, Jeffrey M. Rye, | Conference on Compiler Construction | , CC ’16, 2016. |  |  |  |  |
| rity in FUZZBUSTER. In | Proc. IEEE Int’l Conf. on | [55] Taesoo Kim et al. (Team Atlanta). Atlantis: Ai-driven |  |  |  |  |
| Self-Adaptive and Self-Organizing Systems | , 2013. | threat localization, analysis, and triage intelligence sys- |  |  |  |  |
| (SARIF) v2.1.0, 2020. | https://docs.oasis-open. | [58] Team Shellphish (Artiphishell). Shellphish x AIxCC |  |  |  |  |
| org/sarif/sarif/v2.1.0/sarif-v2.1.0.html | . | Post-Mortem. | https://support.shellphish.net |  |  |  |
| penai.com/cookbook/examples/using_logpro | [59] Theori. Branch Flipper: Unlocking fuzz blockers with |  |  |  |  |  |
| bs | , 2023. | coverage-grounded LLMs. | https://theori-io.gi |  |  |  |
| [46] Oracle. jdb: The Java debugger. | https://docs.ora | .pdf | , 2025. AIxCC Technical Report. |  |  |  |
| /jdb.html | , 2026. | [60] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier |  |  |  |  |
| [47] Sebastian Poeplau and Aurélien Francillon. Symbolic | tiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, |  |  |  |  |  |
| execution with SymCC: Don’t interpret, compile! In | Aurelien Rodriguez, Armand Joulin, Edouard Grave, |  |  |  |  |  |
| 29th USENIX Security Symposium | , 2020. | and Guillaume Lample. | LLaMA: Open and effi- |  |  |  |
| [49] Konstantin Serebryany, Derek Bruening, Alexander | for programming tools, 2025. | https://github.com |  |  |  |  |
| Potapenko, and Dmitriy Vyukov. | { | AddressSanitizer | } | : | /tree-sitter/tree-sitter | . |
| technical conference (USENIX ATC 12) | , 2012. | [62] WALA. WALA: T.J. Watson libraries for analysis. | ht |  |  |  |
| Wenbo Guo, and Xinyu Xing. | Bandfuzz: An ml- | [63] Mike Walker. Machine vs. Machine: Lessons from the |  |  |  |  |
| powered collaborative fuzzing framework, 2025. | arXiv: | First Year of Cyber Grand Challenge. In | 24th USENIX |  |  |  |

---

## Page 18

[64] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Table 10: Submission statistics.

Ed Chi, Sharan Narang, Aakanksha Chowdhery, and

[65] Fabian Yamaguchi, Nico Golde, Daniel Arp, and Konrad

Security and Privacy , 2014.

[67] John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian

Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir Press.

Swe-agent: agent-computer interfaces enable automated

software engineering. In 38th International Conference

on Neural Information Processing Systems , NIPS ’24,

2024.

A practical program repair agent mimicking human ex-

pertise. In 34rd USENIX Security Symposium , 2025.

A Per-Team Details

| Azure ($K) | 73.9 | 18.5 | 20.3 | 63.2 | 54.9 | 38.7 | 7.1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OpenAI ($K) | 6.6 | 0.6 | 8.2 | 3.1 | 0.4 | 0.4 | 0.4 |
| Anthropic ($K) | 20.0 | 20.6 | 3.1 | 7.5 | 2.6 | 0.7 | 0.3 |

Submission Accuracy. Table 10 reports per-team counted

submissions (correct and incorrect, excluding duplicates) and

accuracy rates by scoring category.

PoV Generation Techniques. Table 11 extends Table 3 with

per-team tool and parameter details. Teams generally fall into

| TI | 55 | 63 | 7 | 19 | 61.8 | 31.7 | 62.5 | 89.5 | 7.2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FB | 35 | 60 | 7 | 13 | 80.0 | 23.3 | 87.5 | 61.5 | 8.1% |
| SP | 31 | 11 | 12 | 7 | 90.3 | 100 | 69.2 | 100 | 0.1% |

sink-targeted PoV generation, directed fuzzing toward sinks,

and improved sanitizers. For delta-mode challenges, teams

narrow scope from the full codebase to the diff and related

code for more targeted bug detection. For SARIF broadcasts

received mid-competition, teams treat them as pre-specified

bug candidates and use them to guide the PoV generation.

Patch Generation Techniques. Table 12 extends Table 4

diff files. Additionally, TI runs two diff-analysis agents in

sites to all affected code.

B Abbreviations

CP/CPV naming rule. A CP is identified

follows the Abbr. column of Table 1; <mode> is □ for

numeric indices within the project and CP, respectively.

| 42 | B | UG | B | USTER | MR | MultiRetrieval |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AFC | AIxCC Final Competition | PF | Parallel Fuzzing |  |  |  |  |
| CP | Challenge Project | Security Testing |  |  |  |  |  |
| CWE | Common Weakness Enum. | SP | A | RTIPHISHELL |  |  |  |
| FB | F | UZZING | B | RAIN | TB | B | UTTERCUP |
| LC | L | ACROSSE | TI | R | OBO | D | UCK |

| Denny Zhou. | Self-Consistency Improves Chain of | Counted Submissions | Accuracy (%) | AM |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Thought Reasoning in Language Models. In | Interna- | Team | PoV | Patch | SARIF | Bndl | PoV | Patch | SARIF | Bndl | Penalty |  |  |
| tional Conference on Learning Representations (ICLR) | , | AT | 43 | 37 | 8 | 36 | 100 | 83.8 | 75.0 | 97.2 | 0.1% |  |  |
| 2023. | TB | 31 | 24 | 1 | 19 | 90.3 | 79.2 | 100 | 100 | 0.3% |  |  |  |
| Rieck. Modeling and Discovering Vulnerabilities with | 42 | 45 | 4 | 13 | 4 | 91.1 | 75.0 | 76.9 | 100 | 0.3% |  |  |  |
| Code Property Graphs. In | 2014 IEEE Symposium on | LC | 1 | 3 | 0 | 1 | 100 | 33.3 | — | 100 | 10.7% |  |  |
| [66] Shigio Yamaguchi. GNU Global: Source code tagging | the structure of §6.1, but apply language- and challenge-mode- |  |  |  |  |  |  |  |  |  |  |  |  |
| system. | https://www.gnu.org/software/globa | specific adaptations. Java’s logical vulnerabilities often stem |  |  |  |  |  |  |  |  |  |  |  |
| l/ | , 2026. | from unsafe sink function usage, prompting teams to adopt |  |  |  |  |  |  |  |  |  |  |  |
| [68] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak | with per-team tool and configuration details. Teams generally |  |  |  |  |  |  |  |  |  |  |  |  |
| Shafran, Karthik Narasimhan, and Yuan Cao. ReAct: | fall into the structure of §6.2, adapting to challenge types by |  |  |  |  |  |  |  |  |  |  |  |  |
| Synergizing reasoning and acting in language models. | adjusting language-specific tooling and prompts, along with |  |  |  |  |  |  |  |  |  |  |  |  |
| In | International Conference on Learning Representa- | CWE- or bug-type-specific guidance. For delta mode, most |  |  |  |  |  |  |  |  |  |  |  |
| tions (ICLR) | , 2023. | CRSs focus vulnerability analysis on modified code from |  |  |  |  |  |  |  |  |  |  |  |
| [69] Zheng Yu, Ziyi Guo, Yuhang Wu, Jiahao Yu, Meng Xu, | parallel, one filtering out compiler-unused files and one using |  |  |  |  |  |  |  |  |  |  |  |  |
| Dongliang Mu, Yan Chen, and Xinyu Xing. Patchagent: | the complete diff, to broaden analysis from immediate change |  |  |  |  |  |  |  |  |  |  |  |  |
| Resource Usage. | Table 9 reports per-team consumption of | as | <project><cp-idx><mode> | , | and | a | CPV | as |  |  |  |  |  |
| Azure compute and LLM API budgets. | <project><cp-idx><mode><cpv-idx> | , | where | <project> |  |  |  |  |  |  |  |  |  |
| Table 9: Resource Utilization. Team abbr: Table 2. | full-mode or | ▲ | for delta-mode; | <cp-idx> | and | <cpv-idx> | are |  |  |  |  |  |  |
| AT | TB | TI | FB | SP | 42 | LC | Cheat sheet. | The following shows acronyms used in paper. |  |  |  |  |  |
| Gemini ($K) | 2.8 | – | 0.2 | 1.6 | – | – | < | 0.1 | ASC | AIxCC Semifinal Comp. | PoV | Proof of Vulnerability |  |
| xAI ($K) | < | 0.1 | – | – | – | – | – | – | AT | A | TLANTIS | RCA | Root Cause Analysis |
| All LLMs ($K) | 29.4 | 21.1 | 11.5 | 12.2 | 2.9 | 1.1 | 0.6 | CC | Claude Code | SAST | Static Application |  |  |
| Total ($K) | 103.3 | 39.6 | 31.8 | 75.4 | 57.8 | 39.8 | 7.8 | CPV | Challenge Project Vuln. | SARIF | Static Analysis Results |  |  |
| Score / $K | 3.80 | 5.54 | 6.63 | 2.04 | 2.35 | 2.64 | 1.25 | CRS | Cyber Reasoning System | Interchange Format |  |  |  |

---

## Page 19

Table 11: PoV Generation Techniques Across Teams. Blank: no custom implementation; † all non-blank teams have used SARIF

and Diff.

| AT | TB | TI | FB | SP | 42 | LC |
| --- | --- | --- | --- | --- | --- | --- |
| Pre-Comp Corpus | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Source | OSS-Fuzz; | ClusterFuzz; | ClusterFuzz; | OSS-Fuzz | Samples |  |
| GitHub | GitHub | GitHub |  |  |  |  |
| Matcher | Input Format | Cov-Based | Name; Input | Name; Input | Always |  |
| Format | Format |  |  |  |  |  |
| LLM-Based Seed Gen | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Bootstrap | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Solve cov blocker | Stuck Seeds | Frontier Func | Frontier Func | LLM-Picked |  |  |
| Mutator/generator | ✓ |  |  |  |  |  |
| Input Grammar | Testlang; | Python Decoder | Nautilus [6] |  |  |  |
| libFDP [37] | Grammar |  |  |  |  |  |
| Output format | Blob; Script | Script | Script | Script | Script | Blob |
| Engine Refinement | ✓ | ✓ | ✓ | ✓ |  |  |
| Semantic feedback | LLM for |  |  |  |  |  |
| Fuzzing | IJON [7] Annot. |  |  |  |  |  |
| Pipeline | Improved sanitizer | Patched (Java) | Loosened (Java) |  |  |  |
| Dict Gen | On-the-fly LLM | AFL++ [23] | AFL++ [23] | Custom |  |  |
| Dict2File; | Dict2File; |  |  |  |  |  |
| CodeQL [28] | Custom |  |  |  |  |  |
| Directed fuzzing | Custom | LLVM Slicing; |  |  |  |  |
| distance | WALA [62] |  |  |  |  |  |
| Concolic Fuzzing | SymCC [47]; |  |  |  |  |  |

Custom

| Parallel Fuzzing | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Corpus sync | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| added C fuzzers | AFL++; | AFL++ | AFL++ | AFL++ |  |  |  |

libAFL [24];

Custom

| added JVM fuzzers | libAFL [24] |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Bug Cand. I.D. | ✓ | ✓ | ✓ | ✓ | ✓ |
| LLM; | LLM; Infer [38] | LLM | LLM; Entropy; | LLM |  |
| Candidate source | † | CodeQL [28]; | CodeQL [28]; |  |  |
| Sinks | Semgrep [48] |  |  |  |  |
| Agentic pick; | LLM | LLM pick | Multi-source | Multi-LLM |  |
| Candidate filter | Reachability | confidence | weighted vote | weighted vote |  |

ranking

LLM-Based

| PoV Gen | Non-PoV Gen usage | ✓ | ✓ | ✓ | ✓ |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pipeline | PoV Gen Agent | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |
| Code; CWE; | Code; CWE | Code; Cov; | Code; CWE; | Code; CWE; |  |  |  |  |  |
| Key context/tool | † | Call Path; Cov; | Log; Debugger | Call Path; Log | Call Path; Cov; |  |  |  |  |
| Log; Debugger | Log; Debugger |  |  |  |  |  |  |  |  |
| Main method | Iterative; | Iterative | Iterative; | Iterative | Iterative; |  |  |  |  |
| Reach | → | Exploit | Reach | → | Exploit | Reach | → | Exploit |  |
| Output format | Blob; Script | Script | Script | Script | Script |  |  |  |  |
| Pipeline | LLM PoV Gen | → | Fuzz | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Co-op | Fuzz | → | LLM PoV Gen | ✓ | ✓ | ✓ |  |  |  |
| Deduplication | Stack | ClusterFuzz [29] | Stack | → | LLM | Crash | ClusterFuzz [29] | ClusterFuzz [29] | PoV hash |
| PoV | classifier | sig | → | LLM |  |  |  |  |  |
| Submission | Submission Strategy | ASAP | ASAP | ASAP | ASAP | ASAP | ASAP | ASAP |  |

---

## Page 20

Table 12: Patching Techniques Used by each CRS. Blank: no custom implementation; –: not applicable; † all teams use

sanitizer/crash reports and failed patch feedback.

| AT | TB | TI |  |  |
| --- | --- | --- | --- | --- |
| patching agents + | Creation; | Patcher; |  |  |
| A | IDER | [27] | Reflection | Questions |
| Agent Ar- | + SWE- |  |  |  |
| chitecture | A | GENT | [67] |  |
| Gemini | Gemini |  |  |  |
| Standalone RCA | ✓ | ✓ | ✓ |  |
| Multi-PoV | Up to 15 variants | Up to 3 ranked |  |  |
| RCA | PoVs |  |  |  |

Root

Cause

Analysis

Non-LLM RCA

Code Indexer ctags [15]; tree-sitter [61] gtags [66]

ast-grep [17]

SAST Report Infer [38];

Joern [65]

CWE Guidance

| Fine-tuned | Llama [60] for |
| --- | --- |
| LLM | contextualization |

Generation

Search

Dynamic Info GDB [25]/JDB [46]

JaCoCo [22]

| Generation | diff; SAST |
| --- | --- |
| LLM as Judge | ✓ |

Post-patch Fuzz

Rebuild Optimization ccache [12];

Maven [4] cache

| Min. Patch Set Calc. | ✓ | ✓ |
| --- | --- | --- |
| Calc. Timing | On new PoV | On new PoV |
| Calc. Mode | Incremental; | Recompute; All |

cation &

Submis-

New patch All unsubmitted

PoV success

| FB | SP | 42 | LC |
| --- | --- | --- | --- |
| 23 strategies: | Programmer; | RCA; Strategy; | workflow |
| 12 Full-mode | Critic; | QE |  |
| 8 Delta-mode | Traditional + |  |  |
| 2 SARIF | Agentic pipelines |  |  |

1 Unharnessed

Gemini Gemini Gemini

✓

Crash statistics

(AURORA [11])

based

Agent with static

& dynamic

analysis;

ensembled

ranking of

multi-sources

| tree-sitter [61] | ctags; LSP [39] |  |
| --- | --- | --- |
| SVF [54]; | Semgrep [48]; |  |
| CodeQL [28] | CodeQL [28] |  |
| 40+ CWE | 40+ CWE repair |  |
| catalog | advice |  |
| LLVM-cov [34]; | LLVM- | GDB/JDB |

cov/JaCoCo

LLM vuln

ranking

| ✓ | ✓ |
| --- | --- |
| 25s Fuzz (No | 5min Fuzz |

PoV Patch Only)

ccache; Maven

cache

| ✓ | ✓ |
| --- | --- |
| On new PoV | Every hour |

Recompute; All Incremental;

count; All New patch

unsubmitted

| Arch Category | Multi-Arch | Multi-Agent | Multi-Agent | Single-Agent | Multi-Arch | Single-Agent | Single-Agent |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Design Detail | 6 standalone | RCA; Strategy; | Analyzer; | Same arch with | Triage; | Test; Context; | Multi-LLM |  |
| Diversified | Temp. | Temp. | Temp.; No. of | Temp. |  |  |  |  |
| Hyperparams | failed patches |  |  |  |  |  |  |  |
| Diversified LLMs | GPT; Claude; | GPT; Claude | GPT; Claude; | Claude; GPT; | Claude; GPT | GPT; Claude; | GPT; Claude; |  |
| Contextualization | † | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Agentic Code | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| PoV Bytes | ✓ | ✓ | ✓ |  |  |  |  |  |
| LLM Reflection | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |
| No-PoV Patch | @45min; Delta | @50%; SAST; | Delta diff |  |  |  |  |  |
| Basic Checks | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Build | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| PoV Test (Gen) | Single | Up to 15/san | All | Single | Up to 20/vuln | All | Single |  |
| Validation | Proj. Tests | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| PoV Test (Submit) | All & cross-block | Up to 15/san | All | Max 5 | Up to 20/vuln | All | Single |  |
| Dedupli- | Uncovered PoVs | PoVs | PoVs | Uncovered PoVs |  |  |  |  |
| sion | Submit | Right after calc.; | Right after calc.; | ≥ | 60min; by PoV | Right after calc.; |  |  |
| No-PoV Patch Sub. | – | – | >45min; gated by | @50% time | – | – | @DDL-30min |  |

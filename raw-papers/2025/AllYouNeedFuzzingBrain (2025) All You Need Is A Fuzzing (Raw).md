---
title: "All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching"
author: "Ze Sheng; Qingxiao Xu; Jianwei Huang; Matthew Woodcock; Heqing Huang; Alastair F. Donaldson; Guofei Gu; Jeff Huang"
creator: "arXiv GenPDF (tex2pdf:)"
pages: 14
---

# All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching

> **作者**：Ze Sheng; Qingxiao Xu; Jianwei Huang; Matthew Woodcock; Heqing Huang; Alastair F. Donaldson; Guofei Gu; Jeff Huang
> **總頁數**：14 頁

---

## Page 1

All You Need Is A Fuzzing Brain: An LLM-Powered System for

Automated Vulnerability Detection and Patching

| Ze Sheng | Qingxiao Xu | Jianwei Huang |
| --- | --- | --- |
| Texas A&M University | Texas A&M University | Texas A&M University |
| College Station, US | College Station, US | College Station, US |
| zesheng@tamu.edu | qingxiao@tamu.edu | jwhuang@tamu.edu |
| Matthew Woodcock | Heqing Huang | Alastair F. Donaldson |
| Texas A&M University | City University of Hong Kong | Imperial College London |
| College Station, US | Hong Kong, China | London, UK |
| matthewwoodc0@tamu.edu | heqhuang@cityu.edu.hk | alastair.donaldson@imperial.ac.uk |

Guofei Gu

Texas A&M University

College Station, US

guofei@cse.tamu.edu

Abstract

ered 28 security vulnerabilities—including six previously unknown

benchmarking state-of-the-art LLMs on vulnerability detection and

ACM Reference Format:

Ze Sheng, Qingxiao Xu, Jianwei Huang, Matthew Woodcock, Heqing Huang,

Alastair F. Donaldson, Guofei Gu, and Jeff Huang. 2025. All You Need Is

arXiv:2509.07225v1 [cs.CR] 8 Sep 2025

ence (AIxCC). ACM, New York, NY, USA, 14 pages. https://doi.org/10.1145/

nnnnnnn.nnnnnnn

classroom use is granted without fee provided that copies are not made or distributed

republish, to post on servers or to redistribute to lists, requires prior specific permission

© 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.

https://doi.org/10.1145/nnnnnnn.nnnnnnn

∗

Jeff Huang

Texas A&M University

College Station, US

jeff@cse.tamu.edu

1 Background

ate the discovered issues.

zero-days), for each vulnerability, generate an input that triggers a

compatible fuzzers, such as libFuzzer and AFL for C projects, and

Jazzer for Java projects, to prove a vulnerability. For C projects, the

software can be compiled using various sanitizers: AddressSanitizier ,

GeneratePOV(H, S) → ( ℎ, 𝑠𝑎𝑛, 𝐼 )

s.t. Trigger ( ℎ, 𝑠𝑎𝑛, 𝐼, 𝑆 ) = True

target software, and ℎ ∈ 𝐻 is a fuzzer harness, 𝑠𝑎𝑛 a sanitizer type,

syntax or build errors);

| Our team, | All You Need Is A Fuzzing Brain | , was one of seven final- | We first introduce some background information of AIxCC [2], |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ists in DARPA’s Artificial Intelligence Cyber Challenge (AIxCC), | which is necessary to understand the design choices of our CRS |  |  |  |  |  |
| placing fourth in the final round. During the competition, we devel- | (which is called " | FuzzingBrain | " in the rest of this paper). Readers |  |  |  |
| oped a Cyber Reasoning System (CRS) that autonomously discov- | already familiar with AIxCC may go directly to Section 2. |  |  |  |  |  |
| zero-days—in real-world open-source C and Java projects, and suc- | 1.1 | POV and Patch Generation |  |  |  |  |
| cessfully patched 14 of them. The complete CRS is open source at | In AIxCC, participants are tasked with building autonomous | vul- |  |  |  |  |
| github.com/o2lab/afc-crs-all-you-need-is-a-fuzzing-brain. | nerability detection and patching | systems that operate effectively on |  |  |  |  |
| This paper provides a detailed technical description of our CRS, | real-world open-source projects. These systems must fulfill two crit- |  |  |  |  |  |
| with an emphasis on its LLM-powered components and strategies. | ical requirements: (1) automatically generate | Proofs-of-Vulnerability |  |  |  |  |
| Building on AIxCC, we further introduce a public leaderboard for | (POVs) | , and (2) produce | patches | in the form of diff files that remedi- |  |  |
| patching tasks, derived from the AIxCC dataset. The leaderboard is | Proof-of-Vulnerability (POV). | Given a target software that |  |  |  |  |
| available at o2lab.github.io/FuzzingBrain-Leaderboard. | contains one or more vulnerabilities (either seeded by AIxCC or |  |  |  |  |  |
| Keywords | sanitizer error when processed by a fuzzer harness. AIxCC targets |  |  |  |  |  |
| Fuzzing, Large Language Model, Vulnerability Detection, Patching | vulnerabilities in C and Java projects, and it uses | OSS-Fuzz | [7]- |  |  |  |
| A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability | MemorySanitizer | , and | Undefined-BehaviourSanitizer | . |  |  |
| Detection and Patching. In | Proceedings of Proceedings of the XX Confer- | The POV generation process can be viewed formally as follows: |  |  |  |  |
| ∗ | Team lead | where | 𝐻 | represents a collection of fuzzer harnesses, | 𝑆 | is the |
| Permission to make digital or hard copies of all or part of this work for personal or | and | 𝐼 | a sanitizer-error triggering input. The generated POV serves |  |  |  |
| for profit or commercial advantage and that copies bear this notice and the full citation | as concrete evidence of the vulnerability’s exploitability and also |  |  |  |  |  |
| on the first page. Copyrights for components of this work owned by others than the | provides a test case for patch validation. |  |  |  |  |  |
| author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or | Patch Generation. | Given a target software | 𝑆 | which contains |  |  |
| and/or a fee. Request permissions from permissions@acm.org. | one or more vulnerabilities, for each vulnerability, generate a patch |  |  |  |  |  |
| AIxCC, | in the form of a diff file that satisfies the following requirements: |  |  |  |  |  |
| ACM ISBN 978-1-4503-XXXX-X/25/06 | (1) The patched software | 𝑆 | ′ | compiles successfully (i.e., without |  |  |

---

## Page 2

AIxCC, 2025, Ze et al.

Table 1: AIxCC Tasks and Challenge Modes

Component Description

Two Tasks

POV Generation Generate binary exploit (.bin) to trigger vulnerability

Patch Generation

Three Challenge Modes

SARIF Assessment Mode

∀( ℎ, 𝑠𝑎𝑛, 𝐼 ) ∈ POVs . ¬ Trigger ( ℎ, 𝑠𝑎𝑛, 𝐼, 𝑆 ′ )

where POVs is a set of known POVs for the given vulnerabil-

ity, ℎ ∈ 𝐻 is a fuzzer harness, and 𝑠𝑎𝑛 is a sanitizer type;

given set TestSuite of regression tests for the software:

∀ 𝑇 ∈ TestSuite . Pass ( 𝑇 , 𝑆 ′ )

These requirements provide a degree of confidence that patches

tionality, minimizing the introduction of regressions.

To address diverse vulnerability management scenarios in real-

world software development, AIxCC defines three distinct challenge

modes that participating systems shall support: Delta-Scan , Full-

Scan , and Static Analysis Report-Based (SARIF [10]) . Each mode

corresponds to a different class of inputs and evaluation tasks.

1.2.2 Full-Scan Mode. This mode targets capabilities to discover

vulnerabilities across the entire codebase , rather than restricting

analysis to a single commit.

Input: A software state 𝑆 (specific version), source code reposi-

tory 𝑅 , and corresponding OSS-Fuzz fuzzer harnesses 𝐻 .

vided vulnerability reports, typically from static analysis tools or

Generate diff patch to fix vulnerability & pass functionality tests

Input: External reports (SARIF) | Validate vulnerability reports

fected functions, vulnerability classifications, location information,

contextual metadata, etc.

1.3 Competition Scoring

speed:

𝑆𝑐𝑜𝑟𝑒 = 𝐴𝑀 × ( 𝑉 𝐷𝑆 + 𝑃𝑅𝑆 + 𝑆𝐴𝑆 + 𝐵𝐷𝐿 )

Accuracy Multiplier (AM):

𝐴𝑀 = 1 − 1 − 𝑟

𝑎𝑐𝑐 + 𝑖𝑛𝑎𝑐𝑐

Time Multiplier:

𝜏 = 0 . 5 + 𝑟𝑒𝑚

2 × 𝑡𝑖𝑚𝑒

valid POV earns 2 points, patch 6 points, and SARIF assessment 1

points (BDL) are awarded for grouped submissions. Details can be

found in the AIxCC final scoring guide [9].

2 Overview of FuzzingBrain Architecture

As depicted in Figure 1, FuzzingBrain consists of four core services:

CRS WebService , Static Analysis Service , Submission Service , and

poses tasks, builds fuzzers, and assigns them to worker services.

The Static Analysis Service performs static code analyses to an-

swer queries related to function metadata, reachability, and call

paths. The Worker Services generate POVs and patches by run-

ning fuzzing and LLM-based strategies. The Submission Service

interacts with the competition API, handling submission dedupli-

| Delta-Scan Mode | Input: Target commit \| Detect commit-specific vulnerabilities & Generate remediation |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Full-Scan Mode | Input: Complete codebase \| Full codebase vulnerability discovery & remediation |  |  |  |  |  |  |  |  |
| (2) The patch eliminates all known proofs of the vulnerability: | Input: | Structured vulnerability reports (e.g., SARIF) including af- |  |  |  |  |  |  |  |
| (3) The patch preserves functional correctness according to a | The AIxCC scoring rule incentivizes submission accuracy and |  |  |  |  |  |  |  |  |
| not only remove vulnerabilities but also preserve intended func- | 4 | , | 𝑟 | = | 𝑎𝑐𝑐 |  |  |  |  |
| Importantly, when the patches submitted by a team are evaluated, | 𝑡𝑖𝑚𝑒 |  |  |  |  |  |  |  |  |
| the set | POVs | for a vulnerability is taken to be the union of valid | 𝑤𝑖𝑛𝑑𝑜𝑤 |  |  |  |  |  |  |
| proofs submitted for the vulnerability across | all | teams. Therefore, | POV (VDS): | 2 | × | 𝜏 | if crash, else 0 |  |  |
| to be valid, it is not enough for a team’s patch to simply eliminate | Patch (PRS): | 6 | × | 𝜏 | if valid, else 0 |  |  |  |  |
| the POVs discovered by the team; the patch must be general enough | SARIF Assessment (SAS): | 1 | × | 𝜏 | if correct, else 0 |  |  |  |  |
| to work for POVs discovered by other teams as well. | Bundle Score (BDL): | 1 | × | 𝜏 | if valid, else 0 |  |  |  |  |
| Using the diff format for patches enables seamless integration | AIxCC had a total number of 60 challenges in the final round. |  |  |  |  |  |  |  |  |
| with existing version control systems and open-source development | Each challenge score is the sum of valid POV, patch, SARIF assess- |  |  |  |  |  |  |  |  |
| workflows, facilitating review and maintainability. | ment, and bundle points, scaled by an accuracy multiplier. Each |  |  |  |  |  |  |  |  |
| 1.2 | Three Challenge Modes | point, all decaying over time to a 50% minimum. In addition, bundle |  |  |  |  |  |  |  |
| 1.2.1 | Delta-Scan Mode. | This mode targets commit-based vulnera- | Worker Services | . All services execute in parallel on separate VM |  |  |  |  |  |
| bility analysis, focusing on changes introduced by a specific commit. | nodes. The first three run as single instances, while multiple in- |  |  |  |  |  |  |  |  |
| Input: | A target commit | 𝐶 | , repository base state | 𝑆 | base | (state before | stances of the | Worker Services | are deployed (around 100 VMs in the |
| applying commit | 𝐶 | ), source code repository | 𝑅 | , and corresponding | final round) to support parallel task execution. |  |  |  |  |
| OSS-Fuzz fuzzer harnesses | 𝐻 | . | The | CRS Web Service | acts as the central coordinator. It decom- |  |  |  |  |
| 1.2.3 | SARIF Assessment Mode. | This mode validates externally pro- | cation, SARIF validation, and bundles. |  |  |  |  |  |  |
| issue trackers. More details can be found in Section 5. | 2.1 | Task Decomposition |  |  |  |  |  |  |  |
| Objective: | Confirm the accuracy of reported vulnerabilities and | Figure 2 illustrates the workflow for decomposing and distributing |  |  |  |  |  |  |  |
| filter out false positives. | tasks across FuzzingBrain’s services. Upon receiving a task (which |  |  |  |  |  |  |  |  |

---

## Page 3

All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching AIxCC, 2025,

Figure 1: Overview of FuzzingBrain Architecture.

| contains metadata describing the challenge, e.g., a delta-scan or | 2.2 | Libfuzzer and LLM-based Fuzzing |  |  |  |
| --- | --- | --- | --- | --- | --- |
| a full-scan of a target project), the | CRS Web Service | first builds | Upon receiving a target fuzzer, a | Worker Service | first builds the |
| the target project and its fuzzers using OSS-Fuzz utilities. Each | corresponding fuzzer binary, and then proceeds to generate POV in- |  |  |  |  |
| fuzzer is an executable binary generated from a fuzzer harness | puts and patches specific to that fuzzer. Both traditional fuzzing and |  |  |  |  |
| instrumented with a sanitizer (AddressSanitizer, MemorySanitizer, | LLM-powered fuzzing are performed on the same file system to dis- |  |  |  |  |
| or UndefinedBehaviorSanitizer for C/C++ | 1 | , and Jazzer for Java). | cover inputs that can trigger sanitizer errors. Each fuzzer executes |  |  |
| The service then prepares isolated workspaces by cloning the | inside a Docker container with all required runtime dependencies. |  |  |  |  |
| target repository, constructing project-specific Docker containers, | The traditional fuzzing setup is intentionally minimal: we rely |  |  |  |  |
| and generating fuzzer binaries for all supported sanitizer configu- | solely on | libFuzzer | , whose fuzzing corpus is configured to reside |  |  |
| rations. A single project may yield dozens of fuzzers: for example, | in a shared directory accessible by the LLM-based fuzzing strategies. |  |  |  |  |
| dropbear | contains 17 fuzzer harnesses, each compiled with three | All LLM-based strategies execute in parallel, and the inputs they |  |  |  |
| sanitizers, producing more than 50 binaries. | generate that do not immediately trigger crashes are preserved |  |  |  |  |
| All fuzzers are distributed across the Worker Services to enable | in the shared corpus. These inputs are often close to valid crash- |  |  |  |  |
| concurrent execution. To minimize communication overhead, only | inducing cases and therefore serve as valuable seeds for | libFuzzer | . |  |  |
| the fuzzer path (fuzzer name and sanitizer type) is sent to a worker. | Since the parallel strategies can generate a very large number of |  |  |  |  |
| The corresponding binary and Docker image are reconstructed | test inputs per second, the shared corpus directory is periodically |  |  |  |  |
| locally on the worker node. | cleaned to prevent uncontrolled growth. Rather than performing |  |  |  |  |
| In parallel, the task is also dispatched to the Static Analysis | libFuzzer’s built-in corpus minimization, our approach removes |  |  |  |  |
| Service and the Submission Service. The former conducts program | files based on age: any input older than 10 minutes is deleted. This |  |  |  |  |
| analysis, while the latter manages bookkeeping for POV and patch | lightweight policy keeps the corpus size manageable while still |  |  |  |  |
| submissions. | allowing recently generated inputs (which are more likely to be |  |  |  |  |

relevant) to contribute to subsequent fuzzing iterations.

1 FuzzingBrain also supports C++, besides C and Java projects.

---

## Page 4

| AIxCC, 2025, | Ze et al. |  |  |
| --- | --- | --- | --- |
| For each LLM-based fuzzing strategy, the Worker Service spawns | duplicates. Deduplication is essential because redundant submis- |  |  |
| a dedicated Python subprocess. Once a POV is identified, the work- | sions reduce the accuracy multiplier. |  |  |
| flow transitions to the patching phase, where multiple patching | For POV submissions, each entry is accompanied by a | signature | , |
| processes are launched in parallel. | defined as the crash location (source file and line number) extracted |  |  |
| FuzzingBrain currently incorporates | 23 distinct LLM-based | from the crash call stack. If the crash location is unavailable, heuris- |  |
| strategies | (10 for POV and 13 for patches), categorized by their | tics are applied to construct a signature from the crash output and |  |
| operational mode and target language focus, as summarized in Ta- | sanitizer. Two POVs are considered duplicates if they share the |  |  |
| ble 2. Each strategy executes in an independent process but adheres | same signature. However, distinct signatures may still correspond |  |  |
| to a unified interface for receiving task specifications and returning | to the same underlying vulnerability. To capture such cases, we |  |  |
| results in a consistent format. Further details of our LLM-based | employ LLM-based comparison: crash reports from two POVs are |  |  |
| POV generation and patching strategies are presented in Sections 3 | provided as input to three different LLMs, and the submissions are |  |  |
| and 4, respectively. | marked as duplicates if at least two of the models consider them |  |  |

2.3 XPatch without POV

Upon receiving a task, the Static Analysis Service performs whole-

program static analysis of the target project and supports three

the fuzzer entrypoint to the target. Each call path comprises an

ordered sequence of functions, including their file paths, names,

and line ranges. To mitigate path explosion, we cap the number of

projects, exploitable issues are typically exposed through shorter,

Developing static analysis tools for real-world projects proved

to build two customized static analysis frameworks: one for C/C++

redundant.

Patch submissions require a different strategy, since multiple

distinct patches may be valid attempts for the same vulnerability,

the canonical signature is derived from the task itself, and the

task.

2.7 Bundle Creation

from a known POV.

competition API), then:

true positive, a new bundle containing both the POV and

SARIF is created.

| For certain complex challenges, generating POVs may be infeasible | and some patches may fail during validation. Deduplication is there- |  |  |  |
| --- | --- | --- | --- | --- |
| within the competition timeframe. To handle such cases, we de- | fore applied more conservatively, using three rules: (1) If two patch |  |  |  |
| veloped | XPatch | , a strategy that attempts to produce patches even | diffs are highly similar, we compute their Levenshtein distance and |  |
| when no POV has been found. XPatch is triggered only after half | discard duplicates with a distance below 10. (2) If two patches are |  |  |  |
| of the competition time has elapsed without a successful POV. Ac- | submitted within a short interval (3 seconds) and correspond to the |  |  |  |
| cording to the competition rules, such patches can still earn credit | same POV signature, the second of the two patches is discarded. (3) |  |  |  |
| as long as they remediate the introduced vulnerability and do not | We cap the number of patch submissions per vulnerability at five. |  |  |  |
| regress against any known POVs. A detailed discussion of XPatch | For XPatch, where no POV is available, we assume that each |  |  |  |
| is provided in Section 4.7. | task corresponds to a single introduced vulnerability. In this case, |  |  |  |
| 2.4 | Static Analyses | submission cap is stricter: at most three XPatches are allowed per |  |  |
| types of queries from Worker Services: (1) | Function Metadata | —given | 2.6 | SARIF Assessment |
| a function name and an optional file name or path, return all match- | For each SARIF broadcast, FuzzingBrain performs validation through |  |  |  |
| ing functions along with their metadata, including parameters and | LLM-based assessment and leverages the information for POV gen- |  |  |  |
| source code; (2) | Reachability | —given a fuzzer harness, identify all | eration when appropriate. If a SARIF report is deemed valid and no |  |
| functions reachable from its entrypoint, returning each function’s | POV has yet been discovered for the corresponding vulnerability, |  |  |  |
| name, file path, and start/end line numbers; (3) | Call Paths | —given a | the CRS Web Service forwards the SARIF to Worker Services to |  |
| fuzzing harness and a target function, enumerate call paths from | guide POV generation. We present further details in Section 5. |  |  |  |
| call paths at 20, returning the first 20 if more exist. We also enforce | Each bundle groups together two or more items (POV, patch, and/or |  |  |  |
| a maximum call path depth (default: 50 for C/C++ and 10 for Java) | SARIF broadcast) that correspond to the same underlying vulnera- |  |  |  |
| to avoid excessively long paths. These defaults were chosen heuris- | bility. In our approach, to enable consistent grouping, we associate |  |  |  |
| tically based on empirical observations from the exhibition rounds: | each vulnerability with a | canonical signature | , defined as the signa- |  |
| in C/C++ projects, vulnerabilities are often buried deep within com- | ture of the first submitted POV. Patch submissions may also include |  |  |  |
| plex call chains, making a higher threshold useful, whereas in Java | an optional | pov_signature | when the patch is explicitly derived |  |
| higher-level entrypoints, so a smaller depth bound is sufficient in | Within the Submission Service, bundles are created and updated |  |  |  |
| practice. | according to the following rules: |  |  |  |
| to be both challenging and time-consuming. We encountered nu- | • | POV submissions. Upon receiving a POV, if it is not marked |  |  |
| merous performance and soundness issues, ultimately leading us | as a duplicate and its status is | passed | (as confirmed by the |  |
| and one for Java. We present further details in Section 6. | – | If the POV matches a SARIF that has been assessed as a |  |  |
| 2.5 | Submission Deduplication | – | Otherwise, the POV initializes a bundle on its own. |  |
| The | Submission Service | receives all POV and patch submissions | • | Patch submissions. Upon receiving a patch, if it is not marked |
| from Worker Services and applies several mechanisms to eliminate | as a duplicate and its status is | passed | , then: |  |

---

## Page 5

All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching AIxCC, 2025,

Table 2: FuzzingBrain LLM-based Strategies

Strategy Name Mode Language Focus Stage

Delta-Scan Strategies

| xs0_delta | delta-scan | C/C++, Java | POV Generation |
| --- | --- | --- | --- |
| as0_delta | delta-scan | C/C++, Java | POV Generation |
| patch_delta | delta-scan | C/C++, Java | Patch Generation |
| patch0_delta | delta-scan | C/C++, Java | Patch Generation |
| patch1_delta | delta-scan | C/C++, Java | Patch Generation |
| patch2_delta | delta-scan | C/C++, Java | Patch Generation |
| patch3_delta | delta-scan | C/C++, Java | Patch Generation |
| xpatch_delta | delta-scan | C/C++, Java | Patch Generation |

Full-Scan Strategies

| xs0_c_full | full-scan | C/C++ | POV Generation |
| --- | --- | --- | --- |
| xs0_java_full | full-scan | Java | POV Generation |
| xs1_c_full | full-scan | C/C++ | POV Generation |
| xs1_java_full | full-scan | Java | POV Generation |
| xs2_java_full | full-scan | Java | POV Generation |
| as0_full | full-scan | C/C++, Java | POV Generation |
| patch_full | full-scan | C/C++, Java | Patch Generation |
| patch0_full | full-scan | C/C++, Java | Patch Generation |
| patch1_full | full-scan | C/C++, Java | Patch Generation |
| patch2_full | full-scan | C/C++, Java | Patch Generation |
| patch3_full | full-scan | C/C++, Java | Patch Generation |
| xpatch_full | full-scan | C/C++, Java | Patch Generation |

Report-Based Strategies

| sarif_POV0 | report-based | C/C++, Java | POV Generation |
| --- | --- | --- | --- |
| xpatch_sarif | report-based | C/C++, Java | Patch Generation |

Unharnessed Strategies

| generate_fuzzer | unharnessed | C/C++, Java | POV Generation |  |
| --- | --- | --- | --- | --- |
| – | If the patch shares a | pov_signature | with an existing POV, | Finally, for model routing, we developed a custom framework |
| the patch is bundled with that POV. | for model selection, routing, and fallback. Existing off-the-shelf |  |  |  |
| – | If the POV is already in a bundle with a SARIF, the patch | solutions were found to be unreliable and prone to errors under |  |  |
| is added to the existing bundle, extending it to include all | competition workloads (e.g., failing to handle high request volume, |  |  |  |
| three components. | rate limits, server overloaded, etc). To enhance robustness against |  |  |  |
| • | SARIF broadcasts. Upon receiving a SARIF that has been | individual model failures or limitations, our framework employs a |  |  |
| validated as a true positive: | multi-model fallback mechanism. The system maintains a priori- |  |  |  |
| – | If the SARIF matches an existing POV, it is bundled to- | tized list of models, including those from Anthropic, Google, and |  |  |
| gether with that POV. | OpenAI. When invoking an LLM, the framework attempts models |  |  |  |
| – | If the POV already belongs to a bundle (e.g., with a patch), | in the predefined order; if one becomes unavailable or encounters |  |  |
| the SARIF is added to that bundle. | an error, the request is automatically redirected to the next avail- |  |  |  |

able model in the list. This design ensures continuity of service and

2.8 Technology Stack minimizes disruptions during critical operations.

As illustrated in Figure 2, FuzzingBrain is implemented primarily in

two programming languages: Go and Python. For the CRS services,

| we selected Go with the Gin web framework. This choice reflects | 2.9 | Parallelization |  |
| --- | --- | --- | --- |
| Go’s strengths in efficiently handling large numbers of concurrent | A central design principle of FuzzingBrain is | parallelization | : every |
| operations and its mature ecosystem for building high-performance, | component that can be parallelized is parallelized, in order to maxi- |  |  |
| production-grade web services. | mize the speed of vulnerability discovery and patch generation. |  |  |
| In contrast, all LLM-based POV and patching strategies are im- | FuzzingBrain’s deployment infrastructure in the competition |  |  |
| plemented as independent Python modules. Python was chosen | environment consists of: |  |  |

due to its rich ecosystem for LLM development and its extensive set

| of third-party libraries, which allow rapid prototyping and flexible | • | Approximately 100 virtual machines, each provisioned with |
| --- | --- | --- |
| experimentation. Each strategy module can execute independently, | 32–192 cores. |  |
| enabling modularity and isolation. | • | Each VM runs between 100 and 10,000 threads concurrently. |

---

## Page 6

| AIxCC, 2025, | Ze et al. |  |  |
| --- | --- | --- | --- |
| This large-scale parallelization enables simultaneous processing | Your output must be a Python script that creates a file |  |  |
| of multiple challenges while maintaining high resource utilization | named exactly | x.bin | , and a short description of the |
| and system throughput. The result is an architecture capable of | vulnerability and the target function.” |  |  |

scaling efficiently under heavy workloads, ensuring both rapid

vulnerability detection and timely patch generation.

3 LLM-based POV Strategies

SARIF-based challenges, and one for unharnessed challenges (i.e.,

those without fuzzer harnesses and not scored).

the system automatically falls back to the next model in the priority

list. This cascading mechanism increases the likelihood of success

by leveraging the complementary strengths of different LLMs, as

individual models often excel at distinct categories of vulnerability

patterns.

3.1 Base Strategies

The approach operates entirely via multi-turn, text-based dia-

“You are a world-class software vulnerability detection

expert. Do not apologize when incorrect; instead, itera-

tively refine your analysis and proceed. When possible,

identify any additional information that would improve

your answer.”

the following harness: [ Fuzzer Source Code ] [ San-

itizer Guidance ] [ Language-Specific Guidance ]

Language- and Sanitizer-Specific Guidance. For C/C++ targets,

the prompt includes sanitizer-focused instructions for Address-

Sanitizer (e.g., buffer overflows, use-after-free), MemorySanitizer

(e.g., uninitialized reads), and Undefined-BehaviorSanitizer (e.g.,

vectors, runtime exceptions).

soning.”

Coverage-Guided Feedback. If x.bin does not trigger a crash,

we also supply coverage feedback in the next iteration. The feed-

back summarizes executed functions and branch decisions with

± 3 lines of surrounding source context. For C/C++, we build with

coverage instrumentation, execute the fuzzer on x.bin to produce

coverage.profdata , then use llvm-profdata to derive an LCOV-

Table 4. In this section, we highlight advanced modules that extend

the base strategy; different strategies compose these modules in

different combinations.

Multi-Input Generation. Unlike the base strategy, which pro-

duces a single test case per iteration, as0_delta generates multiple

candidates. Each LLM interaction emits a Python script that cre-

• CWE-119: Buffer Overflow

• CWE-416: Use After Free

| FuzzingBrain implements a total of 10 LLM-based POV generation | integer overflows, pointer misalignment). For Java targets, we in- |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| strategies: two designed for delta-scans, six for full-scans, one for | clude Jazzer-oriented guidance (e.g., deserialization flaws, injection |  |  |  |  |  |
| All strategies conform to a standardized framework built on | LLM-Generated Python and Execution. | We extract the Python |  |  |  |  |
| iterative, dialogue-based interaction with LLMs. This feedback- | code from the LLM response, execute it to generate | x.bin | , and then |  |  |  |
| driven refinement loop allows the system to incorporate execution | run the fuzzer harness on this input. At this stage, the harness is not |  |  |  |  |  |
| results into successive iterations, enabling the LLM to learn from | performing fuzzing; it is simply used as an execution wrapper with |  |  |  |  |  |
| failed attempts and progressively improve its understanding of the | sanitizers enabled to detect crashes (i.e., sanitizer errors). If a crash |  |  |  |  |  |
| target vulnerability. | occurs, we record a successful POV and submit it to the Submission |  |  |  |  |  |
| Each strategy executes as an independent process and adheres | Service. If the attempt fails at any stage, the process continues with |  |  |  |  |  |
| to a unified interface for task inputs and outputs. Strategies uti- | another LLM interaction, where the next user message provides |  |  |  |  |  |
| lize five different frontier LLMs— | claude-3.7 | , | chatgpt-latest | structured feedback derived from the failure. For example: |  |  |
| (gpt-4o at the time of the competition), | claude-opus-4 | , | o3 | , and | “Fuzzer output: { | truncate_output(fuzzer_output, |
| gemini-2.5-pro | . For each model, the framework performs mul- | 200) | } The test case did not trigger the vulnerability. |  |  |  |
| tiple generation attempts, up to a maximum of five iterations by | Please analyze the output and try again. Consider: (1) |  |  |  |  |  |
| default. In addition, each strategy is subject to a configurable time- | alternative input formats/values; (2) edge cases; (3) fo- |  |  |  |  |  |
| out (default: 30 minutes). | cusing on functions modified in the commit; (4) careful |  |  |  |  |  |
| If a model fails to generate a valid POV within its iteration limit, | attention to boundary conditions; (5) step-by-step rea- |  |  |  |  |  |
| FuzzingBrain implements a baseline strategy ( | xs0_delta | ) for delta- | style report from which we extract executed branches and nearby |  |  |  |
| scans, as illustrated in Figure 3. This strategy establishes core | lines. For Java, we use JaCoCo to collect coverage data, generate a |  |  |  |  |  |
| prompting and feedback patterns that most other strategies inherit | report, and post-process it to recover executed methods/branches |  |  |  |  |  |
| and extend. | with corresponding source excerpts. |  |  |  |  |  |
| logue with LLMs, cleanly decoupling analysis logic from the execu- | 3.2 | Advanced Strategies |  |  |  |  |
| tion environment. | The | as0_delta | strategy introduces several enhancements over the |  |  |  |
| System Prompt. | We initiate each dialogue with a high-level sys- | base approach to improve vulnerability discovery effectiveness. The |  |  |  |  |
| tem instruction, for example: | primary differences among strategies are summarized in Table 3 and |  |  |  |  |  |
| User Message (Inputs). | The user message combines the commit | ates five binary inputs ( | x1.bin | – | x5.bin | ), yielding five exploitation |
| diff and the fuzzer harness source code, together with language- | opportunities per iteration instead of one. |  |  |  |  |  |
| and sanitizer-specific guidance: | Vulnerability Category–Based Prompting. | This module enu- |  |  |  |  |
| “The provided commit introduces a vulnerability. Your | merates Common Weakness Enumeration (CWE) classes and ap- |  |  |  |  |  |
| task is to craft an input for the fuzzer harness that trig- | plies category-specific prompts to guide input generation toward |  |  |  |  |  |
| gers the vulnerability. Your input will be executed by | the intended weakness. | C/C++ (10 categories): |  |  |  |  |

---

## Page 7

All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching AIxCC, 2025,

Figure 2: Task Distribution & Strategy Running

Table 3: Delta-Scan POV Generation Strategies Comparison

| Strategy | Input Analysis | Generation Method | Core Characteristics |
| --- | --- | --- | --- |
| xs0_delta | Commit diff analysis | Single input per iteration | Basic strategy, iterative LLM refinement |

as0_delta Commit diff analysis Multi-input generation Advanced strategy with 5 inputs per try

Table 4: Full-Scan POV Generation Strategies Comparison

| Strategy | Function Discovery | Ranking Method | Core Characteristics |
| --- | --- | --- | --- |
| xs0_c_full | Call graph analysis | LLM ranking | Basic function filtering with simple LLM ranking |
| xs0_java_full | Call graph analysis | LLM ranking | Basic function filtering with simple LLM ranking |
| xs1_c_full | Dual reachability analysis | Multi-model LLM ranking | Parallel processing with improved function identification |

xs1_java_full Dual reachability analysis Multi-model LLM ranking Parallel processing with improved function identification

xs2_java_full Dual reachability analysis Multi-model LLM ranking Advanced Java vulnerability detection with early termination

| as0_full | Call graph analysis | LLM ranking + fuzzing | Advanced generation with multi-phase strategies |
| --- | --- | --- | --- |
| • | CWE-476: NULL Pointer Dereference | Java (representative examples; our implementation targets 15 cate- |  |
| • | CWE-190: Integer Overflow | gories): |  |

• CWE-122: Heap-based Buffer Overflow

| • | CWE-787: Out-of-bounds Write | • | CWE-22: Path Traversal |
| --- | --- | --- | --- |
| • | CWE-125: Out-of-bounds Read | • | CWE-77/78: Command/OS Command Injection |
| • | CWE-134: Format String vulnerabilities | • | CWE-79: Cross-Site Scripting |
| • | CWE-121: Stack-based Buffer Overflow | • | CWE-89: SQL Injection |
| • | CWE-369: Divide by Zero | • | CWE-502: Unsafe Deserialization |

• CWE-611: XML External Entity (XXE) Processing

• CWE-918: Server-Side Request Forgery (SSRF)

---

## Page 8

AIxCC, 2025, Ze et al.

Figure 3: Basic POV Generation Strategy

| Modified-Function Context Injection. | Beyond the commit | based on their likelihood of containing vulnerabilities. The ranking |  |  |
| --- | --- | --- | --- | --- |
| diff, we identify all modified files and functions and append the full | incorporates language-specific vulnerability patterns tailored to |  |  |  |
| source of each modified function to the prompt to provide precise | C/C++ and Java. |  |  |  |
| context. To stay within model context limits and emphasize salient | Enhanced Full-Scan Strategies. | The | xs1_c_full | , |
| code, we cap the injected source at 2,000 lines per function. | xs1_java_full | , and | xs2_java_full | strategies extend the base- |
| Call-Path–Based Analysis. | This module queries the Static | line full-scan approach with more refined call graph construction, |  |  |
| Analysis Service for call paths from the fuzzer entrypoint to all | advanced ranking heuristics, and specialized vulnerability pattern |  |  |  |
| modified (and thus potentially vulnerable) functions. For each call | recognition for their respective languages. |  |  |  |
| path, the system crafts a targeted prompt asking the LLM to gener- | Advanced Full-Scan Integration. | The | as0_full | strategy in- |
| ate an input that exercises that path, steering toward code regions | tegrates all of the above modules (static call graph analysis, LLM- |  |  |  |
| likely to trigger the vulnerability. We limit the number of call paths | based ranking, and advanced vulnerability heuristics) into a unified |  |  |  |
| to 20. If all per-path attempts fail, a final aggregated prompt com- | workflow for large-scale vulnerability discovery across entire code- |  |  |  |
| bines all paths for one last POV-generation attempt. | bases. |  |  |  |
| 3.3 | Full-Scan Strategies | 4 | LLM-Based Patching Strategies |  |
| For full-scan scenarios, where no commit diff is available, Fuzzing- | FuzzingBrain implements 13 LLM-based patching strategies: six |  |  |  |
| Brain employs a set of strategies that analyze the entire codebase | designed for delta-scans, six for full-scans, and one special XPatch |  |  |  |
| to identify potentially vulnerable functions. | strategy for generating patches without POVs. |  |  |  |
| Call Graph–Based Analysis. | The | xs0_c_full | and | Except for XPatch, all patching strategies follow the same work- |
| xs0_java_full | strategies employ static analysis to narrow the | flow, illustrated in Figure 4: |  |  |

search space prior to applying LLM-based vulnerability detection.

| Specifically, they query the Static Analysis Service to enumerate | (1) | Target Function Identification | : Identify vulnerable func- |  |
| --- | --- | --- | --- | --- |
| functions reachable from fuzzer entrypoints. This pruning step | tions using strategy-specific heuristics. |  |  |  |
| typically reduces the candidate set from thousands of functions to | (2) | Metadata Extraction | : Retrieve the complete function source |  |
| a more tractable subset of reachable targets. | code and surrounding context. |  |  |  |
| LLM-Based Vulnerable Function Ranking. | Once reachable | (3) | Patch Generation | : Use LLMs to produce a revised version |
| functions are extracted, LLMs are used to score and rank them | of the function body. |  |  |  |

---

## Page 9

All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching AIxCC, 2025,

Figure 4: Basic Patch Generation Strategy

| (4) | Function Rewrite | : Replace the original function with the | In each iteration, the LLM proposes a candidate patch, which is val- |  |  |
| --- | --- | --- | --- | --- | --- |
| LLM-generated content. | idated against the criteria above. Successful patches are submitted; |  |  |  |  |
| (5) | Diff Creation | : Generate a | .diff | file using Git differential | failures trigger detailed feedback and another iteration, up to the |
| tools. | MAX_ITERATION | limit. |  |  |  |
| (6) | Validation | : Ensure compilation, execute POV tests, and run | Target Function Identification. | Target functions are identi- |  |
| functionality tests. | fied as those suspected to be vulnerable (as determined by LLM |  |  |  |  |
| (7) | Iterative Refinement | : Provide structured feedback for failed | analysis). This is the most critical step, as the quality of patching |  |  |
| attempts, iterating until success or timeout. | depends heavily on accurate function selection. Identification relies |  |  |  |  |

on structured prompts that combine commit diffs and crash logs,

| 4.1 | Patch Validation Criteria | for example: |  |  |
| --- | --- | --- | --- | --- |
| We define a patch as a code modification that mitigates a vulnerabil- | "Your task is to identify all potentially vulnerable func- |  |  |  |
| ity without altering the program’s intended functionality. Patches | tions from a code commit and a crash log. The commit |  |  |  |
| are generated in standard | .diff | format and must satisfy four vali- | introduces a vulnerability. The vulnerability is found |  |
| dation criteria: | by an expert, with a crash log." |  |  |  |
| (1) | Applicability | : The patch applies cleanly to the codebase. | Leveraging POV Generation Context. | This strategy reuses |
| (2) | Compilability | : The patched codebase compiles successfully. | conversation history from the POV generation phase. The addi- |  |
| (3) | Vulnerability Mitigation | : Known POVs (if available) no | tional context, including prior failure cases and reasoning traces, |  |
| longer reproduce the vulnerability. | improves the LLM’s ability to generate correct and targeted patches. |  |  |  |
| (4) | Functionality Preservation | : The patched codebase passes | Function Metadata Extraction. | Once target functions are iden- |
| its functionality tests. | tified, the system queries the Static Analysis Service to extract de- |  |  |  |

tailed metadata, including function boundaries, complete source

A patch is only considered valid if it passes all four criteria.

code, and precise file locations. This ensures the LLM has sufficient

context to propose syntactically and semantically valid patches.

| 4.2 | Basic Patch Strategy | Multi-Model Resilience and Validation. | To improve relia- |
| --- | --- | --- | --- |
| Table 5 shows a high-level comparison of the patching strategies. | bility, the patching process employs multiple LLMs from different |  |  |
| The baseline strategy, | patch_delta | , operates through multi-turn | providers (e.g., Anthropic, Google, and OpenAI). For each model, |
| LLM-driven conversations, similar to the POV generation process. | the system runs an iterative loop in which the LLM generates a |  |  |

---

## Page 10

AIxCC, 2025, Ze et al.

Table 5: Delta-Scan Patch Generation Strategies Comparison

| Strategy | Function Identification | Failure Feedback | Special Features |
| --- | --- | --- | --- |
| patch_delta & patch_full | LLM analysis only | Basic crash info | - |
| patch0_delta & patch0_full | Diff extraction only | Basic crash info | - |
| patch1_delta & patch1_full | LLM + Diff hybrid | Basic crash info | - |
| patch2_delta & patch2_full | LLM + Diff | + Control flow paths | Dynamic execution analysis |
| patch3_delta & patch3_full | LLM + Diff | Basic crash info | Expert analysis + Sample patches |
| candidate patch, the patch is applied to the codebase, and its valid- | crash call stack, but also those not directly mentioned |  |  |
| ity is tested through compilation, execution of known POVs using | in the crash log." |  |  |
| the fuzzer harnesses (with sanitizers enabled), and, when available, | This approach increases the likelihood of addressing indirect vul- |  |  |
| functionality tests. If the patch fails at any stage, structured feed- | nerabilities and related security issues. |  |  |

back—including compiler errors, failed diffs, or fuzzer output—is

patch in the next iteration. This process repeats until a valid patch

is produced, the maximum iteration limit is reached, or the timeout

expires. If one model fails to produce a valid patch, the system

automatically falls back to the next model in the priority list.

4.3 Greedy Strategy

Vulnerable Functions = all modified functions

cation in scenarios where vulnerabilities are clearly introduced

diff-based extraction with LLM analysis:

Potential Vulnerable Functions = LLM-identified func-

tions + all modified functions in the diff

This hybrid design preserves the efficiency of direct diff extraction

while broadening coverage with LLM-derived insights.

time control-flow data is incorporated into subsequent LLM prompts,

similar to feedback mechanisms in POV generation. For C/C++

projects, JVM bytecode coverage analysis is employed. This in-

mentioned in crash traces. For example:

The patch3_delta strategy augments patch generation with expert

vulnerability analysis and a curated patch catalog.

Expert Analysis Integration. The strategy incorporates the

initial analysis response from the POV generation phase as an

expert assessment, providing contextual understanding of the vul-

nerability’s characteristics and exploitation patterns.

needed:

JSON format:"

context.

4.6 Full-Scan Patch Strategy

The main difference between full-scan patching strategies and delta-

scan is the absence of a commit-based context, which forces func-

tion identification to rely solely on crash log analysis and LLM

reasoning. To compensate, full-scan strategies employ enhanced

4.7 XPatch Strategy

are available.

LLM.

| appended to the conversation, and the LLM attempts a revised | 4.5 | Knowledge-Enhanced Strategy |  |  |
| --- | --- | --- | --- | --- |
| The | patch0_delta | strategy implements a greedy approach that | Sample Patch Catalog. | The strategy retrieves vulnerability- |
| assumes vulnerable functions are guaranteed to appear within the | specific patch examples from a catalog indexed by sanitizer signa- |  |  |  |
| commit diff. | tures and vulnerability categories. These examples serve as concrete |  |  |  |
| Function Identification Optimization. | Rather than relying | guidance for remediation approaches. |  |  |
| on LLM analysis, this strategy directly treats all functions present | Context Retrieval. | The strategy also supports dynamic context |  |  |
| in the commit diff as vulnerable targets: | retrieval, enabling the LLM to request additional source code when |  |  |  |
| By extracting modified functions directly from the diff, this strat- | "If you need the source code of any other function, please |  |  |  |
| egy reduces the computational overhead of LLM-driven identifi- | return the file paths and function names in the following |  |  |  |
| through recent code changes. | This feature supports comprehensive reasoning over complex vul- |  |  |  |
| Hybrid Enhancement. | The | patch1_delta | strategy combines | nerabilities that span multiple functions or require broader program |
| 4.4 | Path-Aware Strategy | prompting for more accurate target selection. Specifically, special- |  |  |
| The | patch2_delta | strategy enhances patch generation through | ized prompts guide the LLM in analyzing beyond the immediate |  |
| dynamic execution analysis and enriched prompting. | crash stack trace, encouraging exploration of indirectly related |  |  |  |
| Control-Flow Integration. | When patches fail validation, run- | functions that may also contain vulnerabilities. |  |  |
| projects, coverage data is collected using LLVM profiling; for Java | The XPatch strategy addresses cases where no POVs or crash logs |  |  |  |
| formation is embedded in prompts to enable path-aware patch | For | delta-scans | , this process is relatively straightforward be- |  |
| generation. | cause the commit diff provides strong contextual clues about where |  |  |  |
| Enhanced Function Discovery. | LLM prompting is extended | the vulnerability was introduced. We extract all modified functions |  |  |
| to encourage the inclusion of functions beyond those explicitly | from the diff and supply their full source code as context to the |  |  |  |
| "You should include all functions that are potentially | For | full-scans | , where no commit information is available, XPatch |  |
| vulnerable, including not only those that appear in the | relies on LLM-based scoring of all fuzzer-reachable functions. The |  |  |  |

---

## Page 11

| All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching | AIxCC, 2025, |  |  |  |
| --- | --- | --- | --- | --- |
| LLM assigns likelihood scores to candidate functions based on pre- | • | Stack Trace Data | : Function call sequences and execution |  |
| defined rubrics, and the top | 𝑘 | functions (default: 5) are saved. These | flow information |  |
| functions are then used as the input context for patch generation. | Based on this information, we identify potential vulnerable func- |  |  |  |
| Function Scoring Prompts. | The scoring prompt is tailored to | tions and use the Static Analysis Services to determine whether |  |  |
| both language and vulnerability class. | there is a fuzzer that can reach these vulnerable functions from its |  |  |  |
| • | For | C/C++ | , the rubric targets memory safety issues such as | fuzzer input entry point. If not reachable, then we send a validation |
| off-by-one errors, integer overflows, and buffer boundary | request to the Submission Service. This request includes relevant |  |  |  |
| violations. Functions are scored from 1–10 to reflect the like- | source code extracted from the target project, based on the vulner- |  |  |  |
| lihood of a flaw: 10 indicates a certain violation, 7–9 strong | able file, line numbers, and function name specified in the SARIF |  |  |  |
| indicators, 2–6 weak or indirect hints, and 1 no evidence of | report (when available). At the Submission Service, three different |  |  |  |
| problems. | LLMs are queried in sequence to perform two checks: 1. Determine |  |  |  |
| • | For | Java | , multiple specialized rubrics are supported: | whether the SARIF is likely a false positive. 2. Determine whether |
| – | Malicious logic detection | : identifies intentionally harmful | the SARIF is likely a true positive. |  |
| constructs such as backdoors, command injection, data | If a majority consensus is reached, the resulting assessment is |  |  |  |
| exfiltration, privilege escalation, or kill-switches. Scores | submitted to the competition API. If the outcome is inconclusive |  |  |  |
| range from 1–10, where 10 indicates definite evidence | (e.g., conflicting results or LLM errors), the SARIF is deferred for |  |  |  |
| of malicious intent, 7–9 strong indicators, 2–6 weak or | later reassessment. Two additional mechanisms are then applied: 1. |  |  |  |
| indirect hints, and 1 no evidence of malicious behavior. | When the Submission Service receives a POV, it checks whether the |  |  |  |
| – | Unsafe deserialization | : flags dangerous uses of Java deseri- | POV corresponds to any unprocessed SARIF reports. If a match is |  |
| alization APIs without proper validation (e.g., unfiltered | found, the SARIF is confirmed as valid. 2. Independently, the SARIF |  |  |  |
| use of | ObjectInputStream | , XMLDecoder, or SnakeYAML). | is broadcast to Worker Services to drive POV generation. If a POV |  |
| Scores range from 1-10 (similar to above). | is successfully generated based on the SARIF, the SARIF is likewise |  |  |  |
| In all cases, the LLM outputs a JSON array containing function | confirmed as valid and submitted as such. |  |  |  |
| names, assigned scores, and short justifications, sorted by descend- | Valid SARIF reports provide valuable contextual information, |  |  |  |
| ing score. Only functions with scores | ≥ | 7 are retained. | such as vulnerability description and precise source location, which |  |
| Patch Generation. | Once candidate functions are identified, | can help improve the effectiveness of POV and patch generation. |  |  |
| their metadata and source code are provided to the LLM, with | Accordingly, when a SARIF is classified as valid (but no POV has |  |  |  |
| explicit instructions that the vulnerability lies within one or more of | yet been identified) or remains undecided, it is forwarded to Worker |  |  |  |
| these functions. The LLM is then tasked with generating candidate | Services to support further analysis and exploration. |  |  |  |
| patches to mitigate the issue. | The Submission Service handles SARIF validation because it |  |  |  |
| Patch Validation with LibFuzzer. | Since XPatch operates with- | tracks all POV submissions. This enables direct correlation between |  |  |
| out known POVs, validation relies entirely on fuzzing. After ap- | SARIF-reported vulnerabilities and actual POV-triggered crashes. |  |  |  |
| plying a candidate patch, we execute LibFuzzer on the patched | The matching algorithm proceeds in two stages: (1) check whether |  |  |  |
| binary for 60 seconds. If the fuzzer produces a new crash during | the SARIF | artifactLocation | (e.g., vulnerable file and line num- |  |
| this run, the patch is deemed unsuccessful. Otherwise, the patch is | bers) appears in the POV crash trace, and (2) if necessary, use LLMs |  |  |  |
| considered valid under the available test conditions. | to compare the SARIF vulnerability description with the details of |  |  |  |

the POV submission.

5 SARIF Analysis and Assessment

6 Static Analysis Implementation

Our SARIF (Static Analysis Results Interchange Format) report-

| based analysis implements a multi-stage processing pipeline that | 6.1 | Static Analysis for C/C++ |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| transforms external vulnerability reports into actionable security | Our C/C++ analysis pipeline integrates three external tools: LLVM [6], |  |  |  |  |  |  |
| assessments. Figure 5 illustrates the workflow. | SVF [8], and Bear [3]. The workflow is as follows: generate LLVM |  |  |  |  |  |  |
| Upon receiving a SARIF broadcast, the CRS Web Service first | bitcode for each fuzzer binary, use SVF to construct a call graph, |  |  |  |  |  |  |
| parses the data to extract vulnerability metadata, including stack | compute all functions reachable from each fuzzer, and then build |  |  |  |  |  |  |
| trace information, vulnerability classifications, precise code loca- | call paths from the fuzzer entrypoint to each reachable function. |  |  |  |  |  |  |
| tions, affected functions, and contextual data. After processing, a | To improve efficiency, all fuzzers are analyzed in parallel, and for |  |  |  |  |  |  |
| typical SARIF report yields structured vulnerability information | each fuzzer–function pair, call paths are constructed concurrently |  |  |  |  |  |  |
| containing: | using breadth-first search (BFS). The maximum call path depth is |  |  |  |  |  |  |
| • | Affected Functions | : Target function names and their asso- | limited to 50. |  |  |  |  |
| ciated source file locations | Generating LLVM bitcode presented significant engineering dif- |  |  |  |  |  |  |
| • | Vulnerability Classifications | : CWE identifiers and rule- | ficulties. Simply appending | -emit-llvm | to | clang | often failed due |
| based categorizations | to missing dependent headers. To address this, we first collect all |  |  |  |  |  |  |
| • | Location Information | : Precise line numbers, file paths, | compile commands of the target project into a compilation data- |  |  |  |  |
| and code regions | base by building it inside the OSS-Fuzz base Docker image via |  |  |  |  |  |  |
| • | Contextual Metadata | : Severity levels, confidence scores, | the command: | bear -o /out/compile_commands.json compile | . |  |  |
| and analytical tool information | This uses the Bear tool [3] to intercept and store the compilation |  |  |  |  |  |  |

---

## Page 12

AIxCC, 2025, Ze et al.

Figure 5: SARIF Report-based Strategy

| command associated with each source file. We then process each | are designed to handle challenges such as function overloading |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| compile command entry to produce bitcode for each source file, | and dynamic loading, which complicate traditional static analysis |  |  |  |  |  |
| maintaining separate bitcode sets for fuzzer harnesses and project | approaches. |  |  |  |  |  |
| source files. For each fuzzer, all bitcode files are subsequently linked | To maximize performance, multiple call path queries are batched |  |  |  |  |  |
| into a single bitcode module. Despite this, errors persisted, requir- | to reduce database connection overhead (the primary latency bot- |  |  |  |  |  |
| ing fallback heuristics such as hardcoding common header paths | tleneck). The number of fuzzer–target pairs can be extremely large |  |  |  |  |  |
| and compiler flags. Ultimately, our tool successfully generated bit- | (up to 100K), so we employ a batch execution mode with a batch |  |  |  |  |  |
| code for over 95% of source files across tested projects, including | size of 1,000. To avoid race conditions, the database is cloned for |  |  |  |  |  |
| curl | , | dropbear | , and | sqlite3 | . | each fuzzer path, ensuring that every fuzzer operates on an isolated |
| Performance posed an additional challenge. Linked bitcode files | copy. |  |  |  |  |  |
| could exceed 50 MB, and SVF frequently exceeded 1 hour or ran | The call path analysis employs a balanced approach to cycle |  |  |  |  |  |
| out of memory when constructing call graphs from such large | handling that prioritizes comprehensive path discovery over strict |  |  |  |  |  |
| bitcode files. To mitigate this, we trim oversized bitcode modules | cycle prevention, that is, the code prevents direct cycles (intermedi- |  |  |  |  |  |
| to a manageable size (e.g., 25 MB), apply lightweight type-based | ate methods cannot be the source or target method) but does not |  |  |  |  |  |
| call graph analysis, and enforce a 10-minute timeout. If SVF fails to | fully prevent indirect cycles. This design choice recognizes that |  |  |  |  |  |
| complete within this time budget, the Static Analysis Service will | indirect cycles often represent legitimate and valuable execution |  |  |  |  |  |
| return empty results for that query. | patterns in real world projects, such as recursive algorithms. The |  |  |  |  |  |

Analysis Service mitigates the theoretical risk of infinite recursion

through a practical depth limit (10 calls), ensuring both computa-

6.2 Static Analysis for Java

tional efficiency and analytical completeness.

| For Java projects, we leverage CodeQL [4], which provides a more | In addition, we developed a lightweight baseline analysis that |
| --- | --- |
| mature and reliable analysis infrastructure than the toolchain used | conservatively identifies function callees using only class types and |
| for C/C++. The workflow consists of three main steps: (1) building a | function names. This approach sacrifices precision but serves as |
| CodeQL database from the project source code, (2) executing queries | a fallback mechanism when CodeQL queries fail or become too |
| against the database, (3) decoding query results and computing per- | costly. |

fuzzer data structures (i.e., reachable functions and call paths). We

implemented two custom queries: one for extracting reachable

functions, and another for computing call paths. These queries

---

## Page 13

| All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching | AIxCC, 2025, |  |  |  |
| --- | --- | --- | --- | --- |
| Our Java static analysis pipeline completes within five minutes | setting. For example, if many vulnerabilities can only be triggered |  |  |  |
| for representative OSS-Fuzz projects such as | Apache Zookeeper | , | under MemorySanitizer or UndefinedBehaviorSanitizer, skipping |  |
| Tika | , and | Commons-Compress | . | these sanitizers would cause FuzzingBrain to miss them, leading to |

7 Performance Optimizations

libFuzzer) contributed only one or two POVs. However, we also

mortem analysis showed that a substantial portion of credits was

spent on Worker Services assigned to fuzzers that could not reach

the vulnerable code, making POV discovery impossible regardless

ing policies:

Sanitizer Selection. We disabled UndefinedBehaviorSanitizer for

all projects and disabled MemorySanitizer for projects with more

than ten fuzzer harnesses, prioritizing AddressSanitizer where we

observed the highest yield.

Time Budgeting for LLM-Based Fuzzing. To control API spend,

• If one or more POVs have been found (either by LLM-based

strategies or libFuzzer) and libFuzzer has already run longer

Parallelism and Isolation. Because patching requires full rebuilds

(often minutes per attempt), we run 3–5 parallel processes for each

patching strategy. A single VM may execute 20–30 patching pro-

cesses concurrently for one vulnerability. Each process operates in

patches, even if valid, reduces the accuracy multiplier and lowers

the overall score. Because patches contribute the largest share of

points, we balance patching success probability against scoring

penalties by capping the number of submissions per vulnerability

(keyed by canonical signature): at most five POV-based patches and

at most three XPatches.

These treatments reflect tradeoffs between efficiency and cover-

lower overall performance in the final round.

FuzzingBrain relies heavily on parallelism, which introduced subtle

race conditions and deadlocks:

maps with sync.Map .

• Worker services occasionally submitted false-positive POVs

due to file-level race conditions. Multiple POV strategies

wrote to the same output path ( x.bin ), leading to mismatched

files being submitted. The fix was to isolate file paths for

each subprocess.

relying heavily on LLMs for code generation.

and automated secret management, rather than relying on manual

updates.

8.4 Logging and Observability

nothing after Day 4. We suspect a critical crash or bug, but the root

• Our system generated gigabytes of logs across services within

hours, but most logs were stored only on ephemeral VM

nodes in the Azure VMSS cluster.

• After the competition, all VM nodes were recycled, and the

logs disappeared permanently, preventing postmortem anal-

ysis.

| Across the three exhibition rounds, we observed that FuzzingBrain | 8 | Additional Lessons Learned |  |
| --- | --- | --- | --- |
| is effective and fast at producing POVs and patches: the vast major- | Engineering a reliable LLM-based system of this scale proved ex- |  |  |
| ity were generated within the first 30 minutes. Most vulnerabilities | tremely challenging. We encountered countless bugs, spent many |  |  |
| were detected under AddressSanitizer, and our LLM-based strate- | days debugging, and learned several important lessons across soft- |  |  |
| gies discovered nearly all POVs; traditional fuzzing (in our case, | ware engineering, infrastructure management, and system design. |  |  |
| exhausted our allocated OpenAI API credits in one round. Post- | 8.1 | Concurrency and Parallelization |  |
| of LLM effort. | • | In one exhibition round, the Submission Service froze after |  |
| Some target projects can yield more than 50 fuzzers (fuzzer har- | a few hours. We later traced the root cause to a classical |  |  |
| nesses | × | {address, memory, undefined} sanitizers). To curb waste | deadlock in Go mutex usage across multiple threads. The is- |
| and improve throughput for the final round, we applied the follow- | sue was resolved by removing mutexes and replacing shared |  |  |
| each worker’s LLM-based fuzzing is capped at 60 minutes, and | 8.2 | LLM-Generated Code and Debugging |  |
| reduced to 45 minutes if other fuzzers have already produced POVs | More than 90% of our system code was generated with LLM as- |  |  |
| for the same target. | sistance. While this accelerated development, it also made debug- |  |  |
| libFuzzer Time Management. | To preserve CPU for concurrent | ging significantly harder, as we were not as familiar with code we |  |
| fuzzers on the same VM, we limit libFuzzer to at most half of the | did not write ourselves. This experience highlighted the tradeoff |  |  |
| competition time. Concretely (as implemented in our controller): | between rapid prototyping and long-term maintainability when |  |  |
| than the half-time budget (or longer than half that budget | 8.3 | Configuration Management |  |
| while multiple fuzzers are active on the same VM), we stop | With multiple services (each requiring its own API keys), we main- |  |  |
| libFuzzer to save resources. | tained four separate | .env | files across subdirectories. In one exhibi- |
| • | If no POVs found, we continue until the half-time budget is | tion round, a critical service failed because its file was not updated |  |
| reached, then stop. | with the correct keys. This underscored the need for centralized |  |  |
| its own isolated workspace to prevent cross-contamination between | According to AIxCC competition logs, our system performed ex- |  |  |
| attempts. | tremely well for the first three days of the final round, but submitted |  |  |
| Patch Submission Caps per Vulnerability. | Submitting too many | cause remains unknown due to loss of logs: |  |
| age, aiming to optimize performance under resource constraints. | This revealed the importance of persistent, centralized logging and |  |  |
| However, they may not guarantee the best possible score in every | monitoring in large-scale distributed systems. |  |  |

---

## Page 14

AIxCC, 2025, Ze et al.

8.5 Validation and Silent Failures [8] [n. d.]. SVF: Static Value-Flow Analysis. https://svf-tools.github.io/SVF/. Ac-

cessed: 2025-09-08.

| Post-final analysis revealed a critical flaw in our patch validation | [9] 2025. | AIxCC Final Competition Procedures and Scoring Guide. | https:// |
| --- | --- | --- | --- |
| pipeline: a missing parameter in a Python function call caused all | aicyberchallenge.com/final-competition-procedures-and-scoring-guide/. Ac- |  |  |
| Python subprocesses (invoked from Go to handle LLM-based patch- | cessed: 2025-09-08. |  |  |

[10] Michael C. Fanning and Laurence J. Golding. 2023. Static Analysis Re-

ing) to crash silently. Consequently, many patches were submitted sults Interchange Format (SARIF) Version 2.1.0 Errata 01 . Technical Report.

without verification against known POVs, leading to a significant OASIS. https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-

errata01-os.html OASIS Approved Errata.

drop in accuracy. This highlights the need for robust error handling,

explicit status reporting, and fail-safe validation mechanisms when

orchestrating heterogeneous components.

8.6 Diverse Fuzzing Strategies

Our system made only minimal use of traditional fuzzing (only

libFuzzer). While LLM-based fuzzing was highly effective, we likely

missed opportunities to discover additional POVs by not integrating

alternative fuzzers such as AFL++ [1] or Honggfuzz [5]. Incorporat-

ing diverse fuzzing engines could have improved overall coverage

and robustness.

9 FuzzingBrain LeaderBoard

To systematically evaluate state-of-the-art LLMs on vulnerability

detection and patching, we developed the FuzzingBrain Leaderboard

based on the AIxCC benchmarks (36 challenges drawn from the

three exhibition rounds, 16 C challenges and 20 Java challenges). In

each run, FuzzingBrain is restricted to using a single LLM for both

POV generation and patching, allowing us to directly measure the

performance of that model. Scoring follows the AIxCC rubric: each

POV is worth 2 points and each patch is worth 6 points. Models are

then ranked according to their total score across all benchmarks,

providing a standardized comparison of capability.

We introduce several modifications to make leaderboard evalua-

tion practical and reproducible:

• Single-VM Execution: FuzzingBrain is executed on a single

VM, and the vulnerability-triggering fuzzer is provided as

input.

• Precomputed Static Analysis: Static analysis results for

each target project are precomputed and stored in JSON

format. The Static Analysis Service, therefore, only needs

to answer queries and return results, minimizing runtime

overhead.

• Time Limit: Each run is capped at one hour in total, cover-

ing both POV generation and patching.

The current leaderboard is available at o2lab.github.io/FuzzingBrain-

Leaderboard. We plan to regularly maintain this evaluation frame-

work to enable transparent, standardized, and reproducible com-

parisons of different LLMs in real-world vulnerability discovery

and remediation tasks.

References

[1] [n. d.]. The AFL++ fuzzing framework | AFLplusplus. https://aflplus.plus/. Ac-

cessed: 2025-09-08.

[2] [n. d.]. AI Cyber Challenge (AIxCC). https://aicyberchallenge.com/. Accessed:

2025-09-08.

[3] [n. d.]. Bear: Build EAR. https://github.com/rizsotto/Bear. Accessed: 2025-09-08.

[4] [n. d.]. CodeQL. https://codeql.github.com/. Accessed: 2025-09-08.

[5] [n. d.]. Honggfuzz. https://github.com/google/honggfuzz. Accessed: 2025-09-08.

[6] [n. d.]. LLVM Compiler Infrastructure. https://llvm.org/. Accessed: 2025-09-08.

[7] [n. d.]. OSS-Fuzz. https://google.github.io/oss-fuzz/. Accessed: 2025-09-08.

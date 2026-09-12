---
title: "OSS-CRS: Liberating AIxCC Cyber Reasoning Systems for Real-World Open-Source Security"
author: "Andrew Chin; Dongkwan Kim; Yu-Fu Fu; Fabian Fleischer; Youngjoon Kim; HyungSeok Han; Cen Zhang; Brian Junekyu Lee; Hanqing Zhao; Taesoo Kim"
creator: "arXiv GenPDF (tex2pdf:a6404ea)"
pages: 19
---

# OSS-CRS: Liberating AIxCC Cyber Reasoning Systems for Real-World Open-Source Security

> **作者**：Andrew Chin; Dongkwan Kim; Yu-Fu Fu; Fabian Fleischer; Youngjoon Kim; HyungSeok Han; Cen Zhang; Brian Junekyu Lee; Hanqing Zhao; Taesoo Kim
> **總頁數**：19 頁

---

## Page 1

OSS-CRS: Liberating AIxCC Cyber Reasoning Systems

for Real-World Open-Source Security

Andrew Chin † Dongkwan Kim † Yu-Fu Fu † Fabian Fleischer † Youngjoon Kim †

HyungSeok Han ‡ Cen Zhang † Brian Junekyu Lee † Hanqing Zhao † Taesoo Kim †‡

† Georgia Institute of Technology , ‡ Microsoft

| Abstract | —DARPA’s AI Cyber Challenge (AIxCC) showed that | To understand what prevents adoption, we analyzed |  |  |
| --- | --- | --- | --- | --- |
| cyber reasoning systems (CRSs) can go beyond vulnerability | the open-sourced codebases of all seven AIxCC finalists |  |  |  |
| discovery to autonomously confirm and patch bugs: seven teams | and identify three deployment barriers: | 1 | Infrastructure |  |
| built such systems and open-sourced them after the competition. | duplication | , each team independently rebuilt the same plat- |  |  |
| Yet all seven open-sourced CRSs remain largely unusable outside | form services; | 2 | Cloud lock-in | , every system targets the |
| their original teams, each bound to the competition cloud | competition’s Azure and Kubernetes environment, which was |  |  |  |
| infrastructure that no longer exists. We present OSS-CRS, an | decommissioned after the finals; and 3 | Monolithic design | , |  |
| open, locally deployable framework for running and combining | analysis techniques are embedded in monolithic systems, |  |  |  |
| CRS techniques against real-world open-source projects, with | preventing researchers from comparing or combining them |  |  |  |
| budget-aware resource management. We ported the first-place | across teams. Even A | TLANTIS | , the first-place system [24], |  |
| system (A | TLANTIS | ) and discovered 10 previously unknown bugs | requires over 20 Azure virtual machines and cannot target |  |
| (three of high severity) across 8 OSS-Fuzz projects. OSS-CRS | new projects without its original cloud environment. |  |  |  |

is publicly available.

AI-generated vulnerability reports [4, 18, 36, 47] are

increasing the burden on open-source maintainers. The curl

project shut down its bug bounty program after AI-written

submissions overwhelmed reviewers with unconfirmed find-

ings [45, 46]; FFmpeg maintainers criticized Google for

reporting valid bugs without providing patches, calling the

reports “CVE slop” [42]. In both cases, AI automation stops

at discovery, leaving maintainers to validate findings and

write fixes.

DARPA’s AI Cyber Challenge (AIxCC, 2023–2025) [15]

demonstrated that the gap between vulnerability discovery

teams built autonomous cyber reasoning systems (CRSs)

that go beyond discovery: each CRS dynamically confirms

To address these barriers, we present OSS-CRS [37],

CRSs on real-world open-source projects. OSS-CRS pro-

vides a shared infrastructure layer including LLM budget

management and cross-CRS artifact exchange, so that CRS

developers can focus on analysis logic rather than platform

engineering. It adopts the OSS-Fuzz [3] project format as its

target interface, enabling any integrated CRS to target over

1,000 OSS-Fuzz projects without per-project customization.

To validate the framework, we ported A TLANTIS and ran

it against 8 OSS-Fuzz projects, discovering 10 previously

unknown bugs, including three of high severity. OSS-CRS

and all integrated CRSs are publicly available.

| 1. Introduction | an open framework for developing, running, and composing |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| and validated remediation can be closed. Seven finalist | This paper makes the following contributions: |  |  |  |  |
| arXiv:2603.08566v2 [cs.CR] 25 Mar 2026 | a vulnerability with a proof of vulnerability (PoV) and | • | An | empirical analysis | of all seven AIxCC finalist CRS |
| synthesizes a patch validated against that PoV [14]. After | codebases, identifying three deployment barriers that |  |  |  |  |
| the competition, all seven teams open-sourced their systems, | prevent practical reuse: infrastructure duplication, cloud |  |  |  |  |
| in principle making it possible to deploy this capability | lock-in, and monolithic design (§2). |  |  |  |  |
| against any open-source project. | • | OSS-CRS, an open-source framework that addresses |  |  |  |
| Yet over half a year later, these CRSs remain largely | these barriers through a unified execution model and |  |  |  |  |
| unusable outside their original teams: each system is bound | standard interface, budget-aware resource management |  |  |  |  |
| to team-specific infrastructure and interfaces. This adoption | across CPU, memory, and LLM usage, and support for |  |  |  |  |
| gap blocks the communities that should benefit from these | combining CRS techniques across systems (§3). |  |  |  |  |
| systems: researchers cannot run comparable cross-CRS exper- | • | Real-world validation | : porting A | TLANTIS | to OSS-CRS |
| iments under consistent settings; CRS developers lack a stable | and discovering 10 previously unknown bugs (three |  |  |  |  |
| integration contract; and security practitioners cannot adopt | of high severity) across 8 OSS-Fuzz projects, showing |  |  |  |  |
| deployable, budget-aware workflows that produce actionable | that competition-grade CRS techniques can be deployed |  |  |  |  |
| findings. | without cloud infrastructure (§4, §5). |  |  |  |  |

---

## Page 2

2. Background and Motivation

A cyber reasoning system (CRS) is an autonomous agent

AIxCC [15] extended the concept to real-world open-source

software in C and Java, using challenge targets drawn from

discover crashes, static analyzers flag potential flaws, and

program repair systems synthesize patches, but integrated

A CRS unifies these stages. Bug finding generates a

proof of vulnerability (PoV), an input that triggers abnormal

execution such as a crash or sanitizer violation. Bug fixing

synthesizes a patch and validates it by rebuilding the target

and rerunning tests, confirming that the PoV no longer

triggers while preserving the program’s original functionality.

A CRS can accept a variety of inputs: an entire source tree,

a commit-level code diff, a SARIF report [35] from a static

analyzer, or a fuzzing seed corpus.

security practitioners, the system turns static-analysis findings

into validated patches while enforcing spending limits. For

research, multiple CRSs run on the same source tree with

matched inputs, so results are reproducible and directly

comparable.

and capped like CPU time and memory. AIxCC allocated

2

TABLE 1: Deployment characteristics of the AIxCC finalist CRSs.

“Local”: can run end-to-end on a single machine against a new target

without cloud provisioning. “Composable”: analysis components

| CRS | Comp. | Infra | Middleware | Local | Composable |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | TLANTIS | [24] | 9+ | TF+K8s | Ka/PG+R | ∗ | × | × |  |  |
| B | UG | B | USTER | [8] | 16 | TF+Helm | RMQ/PG+R | ∗ | × | × |
| L | ACROSSE | [28] | 3+ | TF+VMs | RMQ/– | × | × |  |  |  |

R = Redis, PG = PostgreSQL, M = MongoDB, S = SQLite, N = Neo4j.

available.

2.2. From Competition to Deployment

To assess whether AIxCC CRSs can be deployed outside

the competition, we analyzed the open-sourced reposito-

ries and deployment artifacts of all seven finalists [5, 7–

9, 24, 28, 44]. We find three recurring barriers: infrastructure

duplication , cloud lock-in , and monolithic design . These

findings align with Zhang et al . [54], who systematize the

2.3. Barrier 1: Infrastructure Duplication

Table 1 summarizes the deployment characteristics of

each team, where Comp. denotes the number of independently

gateway.

| 2.1. Cyber Reasoning Systems | can be extracted and recombined across systems. |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| that discovers and repairs software vulnerabilities without | B | UTTERCUP | [9] | 14+ | TF+Helm | R/M | ◦ | × |  |  |  |
| human intervention. The concept originated in DARPA’s | R | OBO | D | UCK | [5] | 1 | TF+VMs | –/S | ∗ | ◦ | × |
| Cyber Grand Challenge (CGC, 2014–2016) [13, 48], in which | F | UZZING | B | RAIN | [44] | 4 | TF+K8s | –/– | ∗ | ◦ | × |
| teams built systems to attack and defend custom binaries. | A | RTIPHISHELL | [7] | 53 | TF+Helm | RMQ/PG+N | ∗ | △ | × |  |  |
| OSS-Fuzz projects [3]. | TF = Terraform, K8s = Kubernetes, Ka = Kafka, RMQ = RabbitMQ. |  |  |  |  |  |  |  |  |  |  |
| CRS capabilities. | Traditional security tools typically focus | ∗ | Uses LiteLLM [6] for LLM proxy and routing. | ◦ | Post-competition |  |  |  |  |  |  |
| on a single stage of vulnerability management: fuzzers | standalone version available. | △ | Post-competition local deployment guide |  |  |  |  |  |  |  |  |
| pipelines from discovery through a validated fix remain | does not provide multi-component orchestration, cross-stage |  |  |  |  |  |  |  |  |  |  |
| uncommon. | artifact exchange, or budget management. |  |  |  |  |  |  |  |  |  |  |
| Practical scenarios. | This end-to-end capability supports | techniques of all seven AIxCC finalists and conclude that |  |  |  |  |  |  |  |  |  |
| several deployment settings. In CI/CD, a pipeline submits | “the real bottleneck is not technique capability but robust |  |  |  |  |  |  |  |  |  |  |
| a pull-request diff and receives a PoV or confirmation of | integration into autonomous systems.” The next sections |  |  |  |  |  |  |  |  |  |  |
| no bugs through a stable, machine-readable interface. For | show where deployment breaks down in practice. |  |  |  |  |  |  |  |  |  |  |
| Infrastructure requirements. | These scenarios create con- | built container images. The | Infra | and | Middleware | columns |  |  |  |  |  |
| crete system requirements. A CRS must coordinate multiple | show that teams selected different tools yet converged on sim- |  |  |  |  |  |  |  |  |  |  |
| tools across stages, pass artifacts such as crash inputs, PoVs, | ilar platform roles: container orchestration via Terraform with |  |  |  |  |  |  |  |  |  |  |
| candidate patches, and build outputs between them, and | Kubernetes[26] or Helm[22], and coordination backends such |  |  |  |  |  |  |  |  |  |  |
| recover when a stage fails. LLM calls span bug finding, | as Kafka[2], RabbitMQ[40], Redis[41], and PostgreSQL[38]. |  |  |  |  |  |  |  |  |  |  |
| triage, and patch generation, thus token use must be budgeted | Five of seven teams deployed LiteLLM [6] as their LLM |  |  |  |  |  |  |  |  |  |  |
| $50,000 in LLM credits per team; without budget controls, a | The repositories reveal further overlap not visible in the |  |  |  |  |  |  |  |  |  |  |
| single CRS run can exceed $1,000 per hour [5]. Orchestration, | table: each team independently built LLM budget tracking, |  |  |  |  |  |  |  |  |  |  |
| artifact exchange, and budget-aware execution are therefore | cost enforcement, and model routing logic on top of its |  |  |  |  |  |  |  |  |  |  |
| core design problems, not implementation details. | proxy, as well as test environments for applying patches, |  |  |  |  |  |  |  |  |  |  |
| OSS-Fuzz. | The AIxCC competition drew its targets from | rebuilding targets, and validating PoVs. As noted in §2.1, |  |  |  |  |  |  |  |  |  |
| Google’s | OSS-Fuzz | [3], | which | provides | reproducible, | LLM budget control is a shared requirement, yet each |  |  |  |  |  |
| containerized builds for over 1,000 open-source projects. | team built this logic independently. The barrier is not tool |  |  |  |  |  |  |  |  |  |  |
| Each project defines a Dockerfile and build script that | diversity itself, but the repeated integration effort: overlapping |  |  |  |  |  |  |  |  |  |  |
| compile the target project with sanitizer instrumentation, | infrastructure roles reimplemented across all seven teams. |  |  |  |  |  |  |  |  |  |  |
| and supplies fuzz targets that consume fuzzer-generated | This duplication extends beyond initial development: as LLM |  |  |  |  |  |  |  |  |  |  |
| inputs. For CRS deployment, this offers a standardized way | provider APIs and cloud platforms evolve, each team must |  |  |  |  |  |  |  |  |  |  |
| to build and test many projects without per-project setup. | independently update its proxy integration, cost-tracking |  |  |  |  |  |  |  |  |  |  |
| However, OSS-Fuzz runs one fuzzer per container and | logic, and deployment scripts. |  |  |  |  |  |  |  |  |  |  |

---

## Page 3

OSS-CRS Interface (§3.2)

Prepare Build Target Run

Bug
 Code
 User  Target

Cand. DIff Config Project

Optional

Resource Managed CRSs (§3.4)

Resource A Network A

CRS A

CPU

Container 1 Container 2

LLM Service

Memory

LLM

Budget Fuzzer Analyzer

LiteLLM

Isolated

Resource B Network B

Per-CRS keys

CRS B

| Model routing | CPU |
| --- | --- |
| Container 1 | Container 2 |

Model aliasing

Memory

LLM

Budget Fuzzer Builder Sidecar

synchronizes them across all CRSs.

its full codebase.

lar internal interfaces. The seven finalist teams developed

3

PoVs Patches

libCRS (§3.3) File-based Storage

Target Project

Build

download-build-

Artifacts

output

download-source Seeds

Runtime Setup

shared-dir

Artifact Exchange

PoVs

register-

submit-dir

fetch-dir

submit

fetch

Patch Validation

Exchange Sidecar

apply-patch-  (§3.6)

build

run-pov Artifact

deduplication

run-test

input mutation and hybrid fuzzing [24], LLM-first PoV

lithic, techniques cannot be isolated, evaluated, or transferred

would let researchers mix the strongest components from

from scratch.

| (§3.5) | register- | Bug-candidates |
| --- | --- | --- |
| Budget mgmt | register- | Patches |

Figure 1: Architecture overview of OSS-CRS. Users provide a target project and configuration (optionally with code diffs or bug candidates)

and receive PoVs and patches as outputs through the three-phase interface ( prepare , build-target , run ). CRSs run in resource-managed

containers with isolated networks and interact with the platform through libCRS . All LLM calls are routed through the LiteLLM proxy,

which handles model routing and per-CRS budget enforcement. The exchange sidecar deduplicates artifacts in file-based storage and

| 2.4. Barrier 2: Cloud Lock-in | distinctive, often complementary techniques: LLM-based |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| The AIxCC competition provisioned each team with | generation [5], grammar-based fuzzing with LLM-generated |  |  |  |  |
| dedicated Azure virtual machines orchestrated by Kubernetes. | grammars [7], expertise-driven multi-agent patching [9], |  |  |  |  |
| That environment has since been shut down, and the released | diverse LLM strategy ensembles [44], traditional analysis |  |  |  |  |
| artifacts still target infrastructure that no longer exists. For | with LLM-augmented patching [8], and multi-LLM workflow |  |  |  |  |
| example, A | TLANTIS | , the first-place system [24], requires 20+ | coordination [28]. Comparing and combining these tech- |  |  |
| Azure VMs, 42 TiB of cloud storage, and runtime Azure SDK | niques would reveal which approaches outperform others |  |  |  |  |
| calls to scale Kubernetes node pools, despite open-sourcing | and whether ensembling improves overall results. |  |  |  |  |
| As the | Local | column of Table 1 shows, only half the | Yet as the | Composable | column of Table 1 confirms, no |
| teams added local execution support through standalone | CRS exposes interfaces for component-level extraction. If |  |  |  |  |
| releases or local deployment guides [5, 7, 9, 44]. These | A | TLANTIS | has a stronger fuzzer and B | UTTERCUP | has a |
| efforts show that cloud decoupling is possible. However, a | stronger patcher, a researcher cannot combine them without |  |  |  |  |
| local environment must still provide the resource controls | reimplementing one inside the other. The AIxCC competition |  |  |  |  |
| and isolation that cloud platforms supply: CPU and memory | evaluated end-to-end system outputs but provided no way |  |  |  |  |
| quotas, network separation between CRSs, and LLM budget | to attribute results to individual techniques; even Zhang | et |  |  |  |
| limits. Without these, multiple CRSs cannot run on a single | al | .’s survey [54] could describe each team’s methods but not |  |  |  |
| machine without contention or cost overruns. | compare them experimentally. As long as CRSs remain mono- |  |  |  |  |
| 2.5. Barrier 3: Monolithic Design | beyond their original systems. A composable framework |  |  |  |  |
| Beyond infrastructure and deployment, a structural ob- | different teams, run controlled ablation studies, and build on |  |  |  |  |
| stacle remains: every CRS is a monolith with no modu- | each other’s advances rather than rebuilding entire systems |  |  |  |  |

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

---

## Page 4

3. System Design Prepare Build Target Ru

combining existing CRS techniques. OSS-CRS is not itself

a CRS; it is the platform on which CRSs are developed,

deployed, and composed. It provides three capabilities: 1) a

( libCRS ) that remove per-team infrastructure duplication;

2) local execution with resource controls and isolation

cloud dependencies; and 3) cross-CRS artifact exchange that

following subsections detail how OSS-CRS realizes these

3.1. Architecture Overview

Figure 1 illustrates the architecture of OSS-CRS. The

(seeds, PoVs, patches, bug-candidates), and the exchange

From the user’s perspective, OSS-CRS only requires

two inputs: a target project with source code and a single

configuration file that specifies which CRSs to deploy along

running into a single workflow: build the fuzz target, then

4

CRS Dependencie CRS Runne

(images

CRS Builder

(containers

Inputs &

Artifacts

(files Target Sourc PoVs,

Seeds,

PoVs,
 Seed

showing image construction (top), container execution (middle),

and file artifact flow (bottom).

the campaign.

runner images. The middle layer shows containers: build-

and run launches CRS runtime containers. The bottom layer

tracks file artifacts: target source feeds into build artifacts and

seed corpora during build-target , and the run phase produces

PoVs, patches, and new seeds.

machines.

| To address the barriers identified in §2, we propose OSS- | Target Project |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CRS, a locally deployable infrastructure for running and | Docker Build | (OSS-Fuzz |  |  |  |  |  |  |
| unified three-phase execution model and standard interface | Docker Run | Instrumentatio | CRS Runtim |  |  |  |  |  |
| across CPU, memory, network, and LLM budgets, removing | Build Artifact |  |  |  |  |  |  |  |
| enables combining techniques from independently developed | Patches, |  |  |  |  |  |  |  |
| CRSs without requiring a single monolithic pipeline. The | Report |  |  |  |  |  |  |  |
| capabilities. | Figure 2: | Docker workflow across the three operational phases, |  |  |  |  |  |  |
| OSS-CRS user interface defines a three-phase lifecycle ( | pre- | constructs images for target compilation and compiles the tar- |  |  |  |  |  |  |
| pare | , | build-target | , | run | ) that is driven by a single configuration | get project. Separating this phase from | prepare | allows CRSs |
| file that deploys CRSs against target projects. CRSs run in | to construct target-dependent containers while keeping target- |  |  |  |  |  |  |  |
| isolated Docker containers with dedicated CPU, memory, and | independent components cached. The | run | phase launches all |  |  |  |  |  |
| LLM budget allocations; separate networks prevent direct | CRS containers and executes the analysis campaign. CRSs |  |  |  |  |  |  |  |
| inter-CRS communication. Shared infrastructure provides | operate concurrently, exchanging artifacts through a shared |  |  |  |  |  |  |  |
| common services: the | LiteLLM proxy | handles model routing | directory and submitting and syncing findings via the | libCRS |  |  |  |  |
| and budget enforcement, | file-based storage | persists artifacts | interface. Users can specify a timeout or manually terminate |  |  |  |  |  |
| sidecar | manages artifact flow between CRSs. CRSs interact | Figure 2 summarizes the Docker workflow across three |  |  |  |  |  |  |
| with the platform through | libCRS | , which provides APIs | layers. The top layer shows Docker images: | prepare | builds |  |  |  |
| for downloading targets, submitting findings, and validating | CRS dependency images, | build-target | adds the target project |  |  |  |  |  |
| patches. | and CRS builder images, and | run | produces the final CRS |  |  |  |  |  |
| 3.2. OSS-CRS Interface | target | runs instrumentation containers that compile the target, |  |  |  |  |  |  |
| with their resource allocations. Optionally, users can also | Single configuration. | Users only need to define a single |  |  |  |  |  |  |
| provide code diffs or bug candidates for targeted bug-finding | configuration file ( | crs-compose.yaml | ; see Listings 4–7) that |  |  |  |  |  |
| in environments such as CI/CD pipelines. The user then | specifies CRSs, resource allocations, runtime environment, |  |  |  |  |  |  |  |
| sequentially runs three commands that set up CRSs, compile | and LLM settings for all three phases. Adding or removing |  |  |  |  |  |  |  |
| the target, and launch the analysis campaign. The main output | CRSs requires editing this one file, not coordinating multiple |  |  |  |  |  |  |  |
| artifacts are discovered bugs as PoVs and patches that fix | configurations. Users can also specify resource constraints |  |  |  |  |  |  |  |
| them. | without understanding CRS internals. The same file repro- |  |  |  |  |  |  |  |
| Three-phase lifecycle. | OSS-Fuzz combines building and | duces orchestration and resource settings across different |  |  |  |  |  |  |
| run it. OSS-CRS introduces a three-phase model ( | prepare | , | Targeted analysis. | By default, CRSs analyze the entire target |  |  |  |  |
| build-target | , | run | ) that separates CRS setup from target | codebase. For focused analysis (checking whether a recent |  |  |  |  |
| compilation and running, enabling caching and modularity | commit introduces vulnerabilities or fixing a specific reported |  |  |  |  |  |  |  |
| across diverse CRS architectures. The | prepare | phase builds | bug), users can provide targeting metadata that constrains the |  |  |  |  |  |
| CRS container images and their dependencies. These images | analysis scope. OSS-CRS accepts targeted inputs through |  |  |  |  |  |  |  |
| contain the CRS’s analysis tools but have no knowledge | standard channels. A code diff specifies changed code regions, |  |  |  |  |  |  |  |
| of the target project. A prepared CRS can analyze any | enabling delta analysis between versions; directed fuzzers |  |  |  |  |  |  |  |
| compatible target without rebuilding, amortizing setup cost | can focus on changed functions, and patch generators can |  |  |  |  |  |  |  |
| across multiple analysis campaigns. The | build-target | phase | scope fixes to the modified code. Bug-candidate reports |  |  |  |  |  |

---

## Page 5

TABLE 2: Representative libCRS commands used by CRS devel-

| Category | Command | Purpose |
| --- | --- | --- |
| Build outputs | submit-build-output | Publish build artifacts |
| Artifact exchange | register-submit-dir | Register for background submission |
| Artifact exchange | register-fetch-dir | Register for background fetching |
| Artifact exchange | submit | Submit artifact (PoV, seed, patch) |
| Artifact exchange | fetch | One-shot fetch of artifacts |
| Patch validation | run-test | Run regression tests |

identify specific issues for CRSs to address; OSS-CRS

accepts SARIF reports [35] to align with the standard format

CI/CD integration, where CRSs check pull requests rather

3.3. libCRS

libCRS is a Python library automatically injected into

are published via submit-build-output during compilation

and retrieved at run time.

a fuzzer generating inputs, an analyzer triaging crashes, a

patcher synthesizing fixes. The register-shared-dir com-

Artifact exchange. CRSs receive external data via

which flow to other CRSs’ fetch directories via the exchange

5

Build

Targe Build Artifact Project Build

CRS Runne

Ru CRS Runtim Build

Artifact

Legen Image Container File

of the compiled target, applies the patch diff, and performs an

incremental rebuild.

platform.

and LLM API budgets for AI-powered reasoning.

destabilizing others.

| opers. | Instrumentatio |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Runtime setup | register-shared-dir | Share files within CRS | Snapsho |  |  |  |  |  |  |
| Patch validation | apply-patch-build | Apply patch and rebuild | Builder |  |  |  |  |  |  |
| Patch validation | run-pov | Run PoV against patched build | Patc | Sideca |  |  |  |  |  |
| of existing static analysis tools. Targeted analysis supports | Docker | Docker |  |  |  |  |  |  |  |
| than the entire codebase. | Figure 3: | Builder sidecar workflow. The sidecar restores a snapshot |  |  |  |  |  |  |  |
| every CRS container, providing the interface between a CRS’s | artifacts. In the | run | phase, CRS runtime containers receive |  |  |  |  |  |  |
| analysis logic and the OSS-CRS infrastructure. A CRS uses | the build artifacts and begin analysis. When a CRS generates |  |  |  |  |  |  |  |  |
| the same | libCRS | interface regardless of deployment environ- | a candidate patch, it invokes | apply-patch-build | , which |  |  |  |  |
| ment; only the OSS-CRS infrastructure layer changes, not | sends the diff to the builder sidecar; the sidecar restores |  |  |  |  |  |  |  |  |
| the CRS itself. Table 2 lists the core commands across four | the snapshot, applies the patch, and performs an incremental |  |  |  |  |  |  |  |  |
| categories: | build outputs | ; | runtime setup | ; | artifact exchange | ; | recompilation. The CRS then calls | run-pov | to re-execute |
| and | patch validation | . | the crash-triggering input against the patched binary, and |  |  |  |  |  |  |
| Build outputs. | The | build-target | and | run | phases execute in | run-test | to run the project’s regression tests. Unlike shared |  |  |
| isolated containers, so build artifacts must be handed off | infrastructure services, the builder sidecar runs within the |  |  |  |  |  |  |  |  |
| across the phase boundary. Build outputs such as instru- | CRS’s resource allocation ( | cpuset | and | memory_limit | ), en- |  |  |  |  |
| mented binaries, source snapshots, and coverage metadata, | suring that rebuild costs are accounted to the CRS, not the |  |  |  |  |  |  |  |  |
| Runtime setup. | A CRS may comprise multiple containers: | 3.4. Resource Management |  |  |  |  |  |  |  |
| mand provides intra-CRS file sharing for corpora, coverage | Running multiple CRSs simultaneously demands coordi- |  |  |  |  |  |  |  |  |
| data, and intermediate results, without passing through the | nated allocation of heterogeneous resources: CPU cores for |  |  |  |  |  |  |  |  |
| inter-CRS exchange. | fuzzing and analysis, memory for program instrumentation, |  |  |  |  |  |  |  |  |
| register-fetch-dir | and | fetch | : initial inputs supplied by | Compute and memory isolation. | Each CRS declares a |  |  |  |  |
| the operator (seed corpora, reference diffs, bug-candidate | cpuset | string specifying its assigned CPU cores and a | memory |  |  |  |  |  |  |
| reports) and artifacts submitted by other CRSs during en- | limit enforced via Docker cgroups ( | cpuset | , | mem_limit | ). |  |  |  |  |
| semble execution. Conversely, CRSs upload their findings | Pinning CPUs prevents CRSs from contending for the same |  |  |  |  |  |  |  |  |
| (PoVs, seeds, patches) via | register-submit-dir | and | submit | , | cores, while hard memory caps prevent a single CRS from |  |  |  |  |
| sidecar. | LLM budget as a first-class resource. | Beyond compute |  |  |  |  |  |  |  |
| Patch validation. | Bug-fixing CRSs require a tight edit- | resources, OSS-CRS manages LLM API costs as a first- |  |  |  |  |  |  |  |
| compile-test loop to iterate on patch candidates. | libCRS | class resource. Each CRS may declare an | llm_budget | in |  |  |  |  |  |
| provides | apply-patch-build | , | run-pov | , and | run-test | for | US dollars; the LLM proxy tracks usage against this limit |  |  |
| incremental project rebuilding and testing through the builder | and rejects requests that would exceed it. This prevents cost |  |  |  |  |  |  |  |  |
| sidecar. | overruns during long-running campaigns and enables fair |  |  |  |  |  |  |  |  |
| Figure 3 shows the builder sidecar workflow. During | comparison between CRSs with different cost profiles: a |  |  |  |  |  |  |  |  |
| the | build-target | phase, OSS-CRS captures a Docker image | CRS that achieves the same results within a $50 budget is |  |  |  |  |  |  |
| snapshot of the fully compiled target along with its build | more efficient than one requiring $500. |  |  |  |  |  |  |  |  |

---

## Page 6

| Network isolation. | A shared network introduces potential | exhausts its budget, subsequent requests are rejected. The |  |  |
| --- | --- | --- | --- | --- |
| resource-management issues such as port conflicts between | LiteLLM proxy is deployed as a service in the OSS-CRS |  |  |  |
| CRS containers and uncontrolled bandwidth consumption | infrastructure, and its lifetime is coupled with the run phase. |  |  |  |
| that could interfere with per-CRS resource guarantees. OSS- | Deployment modes. | OSS-CRS supports three deployment |  |  |
| CRS mitigates this by creating separate Docker networks | modes. In | internal mode | , OSS-CRS manages LiteLLM, and |  |
| per CRS and restricting all inter-CRS data exchange to the | a key-generation sidecar; this is the default for standalone |  |  |  |
| filesystem-based artifact mechanism. This also simplifies | deployments. In | external mode | , operators provide an existing |  |
| access control for shared services like the LLM proxy and | LLM proxy endpoint and key, useful when an organization |  |  |  |
| ensures fair comparison when benchmarking multiple CRSs | already runs centralized LLM infrastructure; per-CRS budget |  |  |  |
| side by side. | enforcement depends on the external proxy’s capabilities. |  |  |  |
| Flat Docker architecture. | One approach to porting existing | In | disabled mode | , OSS-CRS performs no LLM setup, for |
| CRSs is to wrap them in Docker-in-Docker (DinD), running | CRSs that do not use LLMs. |  |  |  |

the entire system inside a single outer container. However,

DinD complicates build performance, resource control, and

debugging: Docker layer caches are harder to preserve across 3.6. Artifact Exchange

builds, host-level cgroup enforcement for individual inner

| containers is less direct, and debugging nested containers is | Running multiple CRSs simultaneously enables comple- |  |  |
| --- | --- | --- | --- |
| substantially harder. OSS-CRS instead provides interfaces | mentary workflows; a fuzzer can discover crashes while a |  |  |
| that let CRS developers build for a flat Docker architecture, | separate patcher generates fixes. Our evaluation demonstrates |  |  |
| where all containers are managed by the host Docker | that cross-CRS artifact flow works in practice (§4); quan- |  |  |
| daemon. This enables straightforward per-container resource | tifying performance gains over single-CRS runs remains |  |  |
| enforcement, preserves Docker layer caches, and simplifies | future work. OSS-CRS enables this | ensemble execution | (see |
| debugging. | Listing 7) through a filesystem-based exchange mechanism |  |  |

that requires no direct communication between CRSs.

3.5. LLM Services Exchange model. All inter-CRS coordination flows through

a shared exchange directory . Each CRS writes artifacts

| CRSs rely on LLMs for code understanding, patch | to its private submit directory, and reads from a shared |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| generation, and vulnerability reasoning. However, different | fetch directory that mirrors the exchange. The exchange |  |  |  |  |  |  |  |  |
| CRSs may prefer different providers and models. OSS-CRS | sidecar synchronizes per-CRS submit directories into a shared |  |  |  |  |  |  |  |  |
| handles these differences with an LLM proxy layer based on | exchange exposed through each CRS’s fetch directory. The |  |  |  |  |  |  |  |  |
| LiteLLM [6], an open-source proxy that natively supports | exchange organizes artifacts by type: | seeds | for fuzzing |  |  |  |  |  |  |
| multiple provider APIs and model aliasing. | inputs, | povs | for crash-triggering inputs, | patches | for proposed |  |  |  |  |
| Unified | endpoint. | All | CRSs | make | standard | OpenAI- | fixes, and | bug-candidates | for triage reports. CRS-internal |
| compatible API calls to a single proxy that routes requests | data (e.g. coverage maps, model weights, intermediate |  |  |  |  |  |  |  |  |
| to the appropriate backend such as OpenAI, Anthropic, | analysis state) remains private to each CRS and is not |  |  |  |  |  |  |  |  |
| Google, or self-hosted inference servers. A CRS only needs | shared through the exchange. Artifacts are stored under |  |  |  |  |  |  |  |  |
| to implement one API client, regardless of which provider | content-hash filenames, ensuring that duplicate discoveries |  |  |  |  |  |  |  |  |
| the user ultimately configures. | from multiple fuzzers appear exactly once. This hash-based |  |  |  |  |  |  |  |  |
| Model aliasing. | CRSs reference models by logical names | deduplication is the baseline strategy. Because the exchange |  |  |  |  |  |  |  |
| ( | e | . | g | ., | claude-sonnet | or | gpt-4o | ) rather than provider-specific | sidecar is a shared OSS-CRS service rather than library code |
| identifiers. The proxy maps these aliases to concrete provider | launched in a CRS container, we can extend it with more |  |  |  |  |  |  |  |  |
| endpoints, so swapping providers requires only a configura- | advanced logic without modifying individual CRSs: coverage- |  |  |  |  |  |  |  |  |
| tion change, not CRS code modifications. Operators define | based deduplication that keeps only seeds increasing overall |  |  |  |  |  |  |  |  |
| model mappings in a YAML configuration file (see Listings 8 | coverage, or stack-trace-based deduplication that groups |  |  |  |  |  |  |  |  |
| and 9). Each entry specifies a logical | model_name | (what | PoVs by crash signature to reduce redundant triage. |  |  |  |  |  |  |
| CRSs request) and provider-specific parameters including the | Coordination without direct communication. | CRSs coor- |  |  |  |  |  |  |  |
| actual model identifier, API credentials, and optional custom | dinate implicitly through the artifacts they exchange, without |  |  |  |  |  |  |  |  |
| endpoints for self-hosted or Azure deployments. At validation | direct messaging or task assignment. Each CRS polls for |  |  |  |  |  |  |  |  |
| time, OSS-CRS checks that each CRS’s | required_llms | are | new artifacts at its own pace and decides independently what |  |  |  |  |  |  |
| available in the operator’s configured model list. | work to perform. This design provides fault isolation. If |  |  |  |  |  |  |  |  |
| Per-CRS | budget | enforcement. | OSS-CRS | generates | one CRS crashes, others continue operating on previously |  |  |  |  |
| a unique API key per CRS at campaign startup, each | shared artifacts. Resource exhaustion in one CRS does not |  |  |  |  |  |  |  |  |
| associated with its budget. The proxy tracks cumulative | cascade to others, since each runs in an isolated container |  |  |  |  |  |  |  |  |
| costs and rejects requests when the budget is exhausted. This | with independent resource allocations. This file sharing- |  |  |  |  |  |  |  |  |
| per-CRS keying also enables fine-grained usage tracking | based model also simplifies deployment: operators can add |  |  |  |  |  |  |  |  |
| such as which CRS made each request, what model was | or remove CRSs across campaigns without reconfiguring |  |  |  |  |  |  |  |  |
| used, and how many tokens were consumed. When a CRS | communication channels within CRSs. |  |  |  |  |  |  |  |  |

6

---

## Page 7

| TABLE 3: | CRSs integrated into OSS-CRS. | TABLE 4: | Environment variables injected into CRS containers. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CRS | Type | Languages | LLM | Variable | Purpose |  |  |  |  |  |  |  |  |  |  |  |
| CRS | - | LIBFUZZER | Bug-finding | C/C++ | None | OSS_CRS_TARGET | Target project name |  |  |  |  |  |  |  |  |  |
| A | TLANTIS | -C | Bug-finding | C/C++ | ✓ | OSS_CRS_TARGET_HARNESS | Harness binary name |  |  |  |  |  |  |  |  |  |
| A | TLANTIS | -J | AVA | Bug-finding | Java | ✓ | OSS_CRS_NAME | CRS name (for service discovery) |  |  |  |  |  |  |  |  |
| A | TLANTIS | -M | ULTI | L | ANG | Bug-finding | C/C++/Java | ✓ | OSS_CRS_CPUSET | Allocated CPU cores ( | e | . | g | ., | 4-7 | ) |
| C | LAUDE | C | ODE | Bug-fixing | C/C++/Java | ✓ | OSS_CRS_MEMORY_LIMIT | Memory limit ( | e | . | g | ., | 16G | ) |  |  |

4. CRS Integration

The goal of OSS-CRS is to provide a modular framework

where researchers can study, compare, and compose the

distinctive techniques each team developed. As a first phase

of validation, we integrated five CRSs that span the spectrum

from traditional fuzzing to LLM-powered multi-language

analysis (Table 3). The framework is open to the community

to port additional systems. Our primary validation focuses

on A TLANTIS for two reasons: 1 it is the best-performing

AIxCC finalist, and 2 it provides no support for local

execution outside the competition’s cloud infrastructure. The

remaining CRSs validate interface usability and ensemble

mechanics.

4.1. Integration Requirements

prepare_phase builds the CRS’s own container images ( e . g .,

fuzzers, analyzers, LLM agents) that are target-independent

and reusable across projects.

Docker-in-Docker, B UTTERCUP used a dedicated build-bot

service, and A RTIPHISHELL deployed separate patchery

and patch-validation-testing components [7, 9, 24]. With

OSS-CRS, CRS developers extract these custom build passes

into target_build_phase declarations.

7

| OSS_CRS_LLM_API_URL | LLM proxy endpoint |
| --- | --- |
| OSS_CRS_LLM_API_KEY | Per-CRS API key for budget enforcement |

1 #!/bin/bash

2 set -e

3 compile

4 libCRS submit-build-output $OUT build

Figure 4: Build script for CRS - LIBFUZZER .

4.2. Baseline: CRS - LIBFUZZER

The simplest integrated CRS is a thin wrapper around

libFuzzer [39], the coverage-guided fuzzer used by OSS-Fuzz.

It serves as a baseline: it requires no LLM, uses a single

container, and exercises the minimal OSS-CRS interface, i . e .,

prepare, build-target, and run, with nothing beyond standard

fuzzing. Its build script (Figure 4) is two lines: compile

the target, then hand over artifacts to the run phase. This

two-line pattern is the minimal build contract; CRSs can

extend it freely by adding custom compiler passes, instru-

CRS - LIBFUZZER appear in Listing 1 and Listing 4.

4.3. Porting A TLANTIS

Porting process. Converting A TLANTIS to the OSS-CRS

interface required four categories of changes. 1 Mani-

fest creation. We wrote crs.yaml manifests for each sub-

system, declaring its supported languages, required LLM

models, capabilities, and prepare/build/run phase definitions.

| CRS developers integrate their system into OSS-CRS | menting with different sanitizers, or running static analyzers, |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| through a | crs.yaml | manifest with three phase-aligned sec- | while OSS-CRS handles container orchestration and artifact |  |  |  |  |  |  |  |  |
| tions. | transfer. The complete | crs.yaml | and | crs-compose.yaml | for |  |  |  |  |  |  |
| target_build_phase | declares build steps that require knowl- | A | TLANTIS | , the first-place AIxCC system [24], is among |  |  |  |  |  |  |  |
| edge of the target: custom instrumentation passes, sanitizer- | the most complex CRSs: it comprises multiple sub-systems |  |  |  |  |  |  |  |  |  |  |
| specific compilations, or snapshot captures for incremen- | (three independent bug-finding systems), uses multiple in- |  |  |  |  |  |  |  |  |  |  |
| tal patch validation. In the AIxCC competition, all seven | strumentation passes (coverage, AddressSanitizer [43], and |  |  |  |  |  |  |  |  |  |  |
| teams independently implemented their own build and patch- | uninstrumented builds), and combines diverse fuzzing en- |  |  |  |  |  |  |  |  |  |  |
| compilation pipelines: A | TLANTIS | built a | cp_manager | with | gines with multiple LLM agents. |  |  |  |  |  |  |
| crs_run_phase | defines the runtime modules as a set of | 2 | Artifact submission. | Competition-specific API usage |  |  |  |  |  |  |  |
| named containers, each with its own Dockerfile. A multi- | ( | e | . | g | ., sending PoVs) was replaced with | libCRS | commands |  |  |  |  |
| component CRS ( | e | . | g | ., a fuzzer, an analyzer, and a builder | ( | register-submit-dir | , | submit | ). 3 | Project building. | Each |
| sidecar) declares one entry per component, and OSS-CRS | A | TLANTIS | sub-system had its own way of adding CRS |  |  |  |  |  |  |  |  |
| launches them together with shared networking and resource | tooling to the target project image: A | TLANTIS | -M | ULTI | L | ANG |  |  |  |  |  |
| limits. | rebuilt the project image with a custom base image and |  |  |  |  |  |  |  |  |  |  |
| OSS-CRS also injects environment variables into every | A | TLANTIS | -C mounted tooling into the project container and |  |  |  |  |  |  |  |  |
| CRS container at runtime (Table 4). These expose the | overwrote the compiler environment variable. Under OSS- |  |  |  |  |  |  |  |  |  |  |
| target name, resource allocation, and LLM proxy credentials, | CRS, all sub-systems follow the same standard: providing |  |  |  |  |  |  |  |  |  |  |
| so CRSs can adapt without hard-coded assumptions. For | a | builder.Dockerfile | that receives the target project base |  |  |  |  |  |  |  |  |
| instance, a fuzzer can spawn one worker per core. | image as a build argument, unifying the build workflow. |  |  |  |  |  |  |  |  |  |  |

---

## Page 8

4 Image caching via prepare phase. In the competition ware, we ran the ported A TLANTIS CRS against open-source

environment, CRS images are prebuilt into registries. How- projects.

ever, for rapid local CRS development, OSS-CRS supports

rebuilding CRS images through its infrastructure. As such,

each A TLANTIS sub-system needed to optimize its build

process by partitioning some images into the prepare phase.

A TLANTIS -M ULTI L ANG handles C/C++/Java targets using

microservices-based fuzzing driven by directed fuzzing

and runs in its own containers. The configuration files for

A TLANTIS -M ULTI L ANG appear in Listing 2 and Listing 5.

What changed, what was preserved. The original A T -

netes node pools, three separate LiteLLM proxy instances,

and dynamic node scaling via Azure SDK calls (§2.4). Port-

ing replaced all Kubernetes orchestration with a flat Docker

architecture, collapsed the three LiteLLM proxies into the sin-

gle OSS-CRS proxy, and substituted the competition scoring

API with libCRS ’s artifact submission. Each sub-system also

shed auxiliary components: A TLANTIS -M ULTI L ANG and

A TLANTIS -J AVA dropped their concolic execution engines,

and A TLANTIS -C dropped its backup fuzzing engines and

with minimal modification, confirming that the core analysis

techniques are independent of the deployment infrastructure.

To demonstrate bug-fixing integration, we developed

regression tests to check for functional regressions. Because

the builder sidecar handles all build-system complexity (such

as Makefiles), C LAUDE C ODE ’s implementation contains

no build logic. The CRS focuses entirely on LLM-driven

8

Target selection. We selected 8 OSS-Fuzz projects spanning

C/C++ and Java, chosen to cover a range of project sizes

(3 kLoC to 1,960 kLoC), application domains (databases,

parsers, network servers, cryptographic libraries), and ex-

expected vulnerability yield.

LLM proxy.

At the time of writing, three have been fixed by upstream

maintainers, one confirmed, and six are pending review. The

majority are memory-safety bugs in C, but the set also

includes logic bugs and undefined-behavior flaws (CWE-476,

CWE-674, CWE-681), demonstrating that the CRS finds null-

pointer, schema-validation, and numeric-conversion issues,

not only fuzzer-class crashes.

available.

Three examples will be provided after a 30-day post-

fix window to illustrate the kinds of patches OSS-CRS

produces.

day period since being fixed. There is one confirmed by

ing initial response. We reported all vulnerabilities following

| Three | sub-systems | ported. | We | ported | three | of | A | T | - | isting fuzzing maturity (from newly onboarded to heavily |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LANTIS | ’s bug-finding sub-systems as independent CRSs. | fuzzed for years). We did not cherry-pick projects based on |  |  |  |  |  |  |  |  |
| and LLM agents. A | TLANTIS | -J | AVA | targets Java projects | Running setup. | All experiments ran on a single machine |  |  |  |  |
| with Jazzer [23] sinkpoint-based fuzzing, A | TLANTIS | -C tar- | with 32 CPU cores and 128 GB RAM, running Ubuntu 22.04 |  |  |  |  |  |  |  |
| gets C/C++ projects with a custom libAFL [17] fuzzer, | with Docker 27. Each campaign allocated 16 cores and 64 GB |  |  |  |  |  |  |  |  |  |
| and both A | TLANTIS | -J | AVA | and A | TLANTIS | -C use a high- | RAM to the bug-finding CRS, with a 24-hour timeout per |  |  |  |
| throughput agentic seed generator. Each sub-system has | target project. LLM budgets were set to $50 per campaign, |  |  |  |  |  |  |  |  |  |
| its own | crs.yaml | manifest, its own target build process, | using a mix of Claude and GPT-4o through the OSS-CRS |  |  |  |  |  |  |  |
| LANTIS | requires over 20 Azure VMs across multiple Kuber- | 5.1. Zero-day Bugs Found |  |  |  |  |  |  |  |  |
| harness scheduler. All primary bug-finding logic, including | We will release three cases in detail from two projects, |  |  |  |  |  |  |  |  |  |
| fuzzers, LLM agents, and analysis pipelines, was preserved | following a 30-day window after the original fix was made |  |  |  |  |  |  |  |  |  |
| 4.4. C | LAUDE | C | ODE | : LLM-Based Patch Generation | 5.2. Patches and Disclosure |  |  |  |  |  |
| C | LAUDE | C | ODE | , a CRS that uses an LLM agent to analyze | Patch generation and validation. | For each vulnerability, |  |  |  |  |
| crash traces and source code for vulnerabilities discovered | OSS-CRS feeds the crash trace, root-cause analysis, and |  |  |  |  |  |  |  |  |  |
| by other CRSs in order to generate patches. | surrounding source code to A | TLANTIS | , which uses an LLM |  |  |  |  |  |  |  |
| Builder sidecar in action. | C | LAUDE | C | ODE | validates each can- | to generate a minimal candidate patch as a unified diff. Each |  |  |  |  |
| didate through | libCRS | ’s three-step patch validation pipeline: | candidate is then validated automatically through the | libCRS |  |  |  |  |  |  |
| apply-patch-build | sends the unified diff to a builder sidecar, | infrastructure (§3.3): the patch is applied and the project |  |  |  |  |  |  |  |  |
| which applies the patch and performs an incremental rebuild | rebuilt, the original PoV is re-executed to confirm the crash |  |  |  |  |  |  |  |  |  |
| from a pre-captured build snapshot; | run-pov | re-executes the | no longer triggers, and the project’s test suite is run to check |  |  |  |  |  |  |  |
| crash-triggering input against the patched binary to confirm | for regressions. We then manually reviewed all patches before |  |  |  |  |  |  |  |  |  |
| the vulnerability is resolved; | run-test | runs the project’s | submitting them to upstream maintainers. |  |  |  |  |  |  |  |
| patch synthesis, delegating compilation and testing to the | Disclosure outcomes. | Of the 10 findings, three have been |  |  |  |  |  |  |  |  |
| framework. | fixed by upstream maintainers, but have not passed a 30- |  |  |  |  |  |  |  |  |  |
| 5. Zero-day Results | maintainers but not yet patched. The remaining six are pend- |  |  |  |  |  |  |  |  |  |
| To evaluate whether OSS-CRS enables practical, large- | each project’s preferred disclosure process, including GitHub |  |  |  |  |  |  |  |  |  |
| scale vulnerability discovery and fixing on real-world soft- | Security Advisories and direct email. |  |  |  |  |  |  |  |  |  |

---

## Page 9

6. Discussion assumptions that a single system does not exercise. We

excluded concolic , A TLANTIS ’s hybrid fuzzing component,

6.1. Challenges and Lessons from the current port because its instrumentation introduced

compatibility issues across diverse target projects; in the

| Docker-in-Docker vs. flat Docker. | Our initial attempt at | original competition, this module contributed only 1.7% of |  |
| --- | --- | --- | --- |
| local portability wrapped each CRS in a Docker-in-Docker | A | TLANTIS | ’s results [24], so we expect minimal impact on |
| (DinD) container. As discussed in §3.4, DinD complicated | bug-finding capability. We are working on porting other |  |  |
| resource control, build caching, and debugging, so OSS- | finalist CRSs (§6.3). |  |  |
| CRS adopted a flat Docker architecture instead. The practical | Target format assumptions. | OSS-CRS currently targets |  |
| lesson is that the flat model requires explicit network policies | projects compatible with OSS-Fuzz, which require a stan- |  |  |
| to prevent cross-CRS communication, a tradeoff we found | dardized build script, a containerized environment, language |  |  |
| acceptable given the gains in resource visibility and build | restrictions, and at least one fuzz harness. Projects not yet |  |  |
| performance. | onboarded to OSS-Fuzz require harness development, which |  |  |
| Build-system diversity. | OSS-Fuzz projects use heteroge- | is outside the scope of the framework. |  |
| neous build systems (Make, CMake, Autoconf, Bazel, Meson, | Target selection. | Our 8 target projects were selected from |  |
| and more). During CRS integration, we found that build | OSS-Fuzz’s project corpus based on adoption and security |  |  |
| assumptions baked into the competition environment (pre- | relevance. |  |  |
| installed tool versions, fixed filesystem layouts) frequently | LLM non-determinism. | LLM-based CRS components pro- |  |
| broke on different target projects. OSS-CRS mitigates | duce non-deterministic outputs, affecting both vulnerability |  |  |
| this by building targets through OSS-Fuzz’s official build | discovery and patch generation. Our results reflect specific |  |  |
| flows, inheriting the build environment that each project’s | model versions and prompt configurations; different models |  |  |
| maintainers already support. | or API versions may yield different findings. |  |  |

Porting effort. Adapting A TLANTIS to the OSS-CRS inter-

face required understanding the system’s internal architecture 6.3. Community and Future Work

and artifact flow without changing the core logic of the

| modules we ported. The changes fell into four categories: | Our roadmap focuses on three directions: |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| configuration (writing | crs.yaml | manifests), I/O adaptation | • | Cross-CRS technique analysis. | With ensemble execution |  |  |
| (replacing competition-specific API calls with | libCRS | com- | and cross-CRS artifact exchange in place, we aim |  |  |  |  |
| mands), build integration (replacing DinD-based patch com- | to answer two questions: which individual techniques |  |  |  |  |  |  |
| pilation with | libCRS | ’s builder sidecar, which handles the | are most effective, and which combinations yield the |  |  |  |  |
| apply-patch, rebuild, and test cycle), and image optimizations | best results? Seed deduplication and PoV triage are |  |  |  |  |  |  |
| using the prepare phase. For the A | TLANTIS | -M | ULTI | L | ANG | prerequisites for meaningful cross-CRS comparison. |  |
| port, this integration work required approximately 3 person- | • | CRS benchmarking. | To enable systematic evaluation, we |  |  |  |  |
| days. For A | TLANTIS | -C, the port took over 4 person-days, | are developing a benchmark suite that lets security prac- |  |  |  |  |
| as its tighter coupling to competition-specific build pipelines | titioners and researchers evaluate and compare CRSs un- |  |  |  |  |  |  |
| and container orchestration demanded more extensive I/O | der controlled conditions, analogous to FuzzBench [34] |  |  |  |  |  |  |
| and build-integration changes. For A | TLANTIS | -J | AVA | and | for fuzzers. |  |  |
| C | LAUDE | C | ODE | , integration required approximately 1 person- | • | Broader target coverage. | We plan to apply integrated |
| day each. Across these ports, we modified configuration, | CRSs to a wider range of open-source projects to |  |  |  |  |  |  |
| orchestration logic, and artifact I/O boundaries, not the core | discover vulnerabilities at scale. |  |  |  |  |  |  |

analysis algorithms. In general, porting effort depends on the

gap between a CRS’s original design and the four categories 7. Related Work

above: systems with hard-coded competition APIs, DinD-

| based build flows, non-standard configuration formats, or | Autonomous cyber reasoning. | The Cyber Grand Challenge |
| --- | --- | --- |
| tightly coupled image assumptions require proportionally | (CGC) [13, 48] introduced autonomous systems that find |  |
| more adaptation work. | and patch vulnerabilities in custom binaries on the DECREE |  |

OS. AIxCC [15] extended this to real-world open-source

6.2. Limitations and Threats to Validity software, producing seven finalist CRSs whose techniques are

analyzed by Zhang et al . [54]. OSS-CRS differs from both

| Our results demonstrate feasibility: CRS logic can be | competition platforms: CGC provided a fixed binary format |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| decoupled from competition infrastructure and applied to | and a scoring API; AIxCC provided Azure infrastructure |  |  |  |  |  |
| real OSS targets with actionable outputs. We note several | with competition-specific endpoints. OSS-CRS provides a |  |  |  |  |  |
| limitations of OSS-CRS in its current state. | reusable framework that persists beyond any single competi- |  |  |  |  |  |
| Single CRS ported. | We validated OSS-CRS by porting one | tion, targeting OSS-Fuzz’s corpus of open-source projects. |  |  |  |  |
| AIxCC system (A | TLANTIS | ). While A | TLANTIS | , the first-place | Fuzzing infrastructure. | OSS-Fuzz [3] provides continuous |
| system [24], is among the most infrastructure-heavy finalists, | fuzzing for open-source projects but supports only single- |  |  |  |  |  |
| porting additional CRSs may reveal interface gaps or design | container, single-fuzzer execution without bug-fixing or LLM |  |  |  |  |  |

9

---

## Page 10

| integration (§2.1). FuzzBench [34] evaluates fuzzer perfor- | CRS interface, resource isolation with LLM budget man- |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| mance on standardized benchmarks but does not support | agement, and cross-CRS artifact exchange for composing |  |  |  |  |
| multi-component CRS workloads. ARVO [32] reproduces | complementary techniques. By porting the AIxCC champion |  |  |  |  |
| historical OSS-Fuzz vulnerabilities for research but provides | system and discovering 10 previously unknown bugs across |  |  |  |  |
| no execution framework. Magma [21] and UniFuzz [30] | 8 open-source projects, we provide feasibility evidence that |  |  |  |  |
| offer ground-truth benchmarks for evaluating fuzzers but | competition CRS logic can be decoupled from its original |  |  |  |  |
| focus on single-fuzzer comparison, not multi-technique | infrastructure and applied to real-world OSS projects. OSS- |  |  |  |  |
| composition. OSS-CRS complements these tools: it uses | CRS is available as open source [37], a first step toward |  |  |  |  |
| OSS-Fuzz project definitions as targets and could integrate | broader cross-CRS accessibility and evaluation. We invite |  |  |  |  |
| with FuzzBench for CRS-level comparison. | the community, including researchers, CRS developers, and |  |  |  |  |
| Ensemble | and | collaborative | fuzzing. | Collaborative | security practitioners, to actively develop, compose, and |
| fuzzing [12, 19, 20, 56] demonstrated that given fixed | evaluate CRS techniques and help mature OSS-CRS into |  |  |  |  |
| resources, distributing effort across multiple fuzzers out- | shared infrastructure for open-source software security. |  |  |  |  |

performs focusing on any single fuzzer, motivating ensemble

approaches. OSS-CRS generalizes this insight from fuzzer

ensembles to CRS ensembles that combine heterogeneous

techniques, including fuzzing, static analysis, LLM reasoning,

and autonomous patching. It coordinates them via unified

resource and LLM budget allocation and a filesystem-

based exchange mechanism that requires no modification to

individual CRSs.

augment fuzzing. TitanFuzz [16] and Fuzz4All [50] use

and PatchAgent [52] mimics human debugging expertise for

practical program repair. The AIxCC competition demon-

strated that integrating LLMs into full CRS pipelines, combin-

ing code reasoning with fuzzing and program analysis, yields

8. Conclusion

OSS-CRS addresses these barriers with a standardized

10

Ethical Considerations

OSS-CRS lowers the barrier to automated vulnerability

discovery and patching in open-source software. This automa-

tion carries inherent dual-use risks, as the same techniques

that help defenders find and fix bugs could also help attackers

identify exploitable weaknesses. However, we believe the

benefits outweigh these risks: our system produces not only

the balance toward defense.

addressed.

Open Science

Acknowledgments

We thank Younggi Park for the initial design and

outreach.

| LLM-powered fuzzing. | LLMs are increasingly used to | proofs of vulnerability but also validated patches, shifting |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LLMs to generate test inputs, ChatAFL [33] applies them to | We ran OSS-CRS entirely in isolated Docker containers |  |  |  |  |  |  |
| protocol fuzzing, and ELFuzz [11] synthesizes entire fuzzers | on local machines without transmitting any data to external |  |  |  |  |  |  |
| via LLM-driven evolution. HLPFuzz [51] and G | 2 | FUZZ [55] | services. Also, because OSS-CRS executes all analysis |  |  |  |  |
| leverage LLMs for constraint solving and input generator | inside containerized environments and operates on fuzzing |  |  |  |  |  |  |
| synthesis, respectively. In a complementary direction, OSS- | harnesses originally written for security testing, it poses no |  |  |  |  |  |  |
| Fuzz-Gen [31] and SHERPA [27] use LLMs to synthesize | risk to running production systems. |  |  |  |  |  |  |
| fuzz harnesses, automating a key bottleneck in onboarding | All vulnerabilities discovered in this work were reported |  |  |  |  |  |  |
| new targets. These works improve individual fuzzing compo- | to upstream maintainers following each project’s preferred |  |  |  |  |  |  |
| nents; OSS-CRS provides the orchestration layer to compose | disclosure process, including GitHub Security Advisories, |  |  |  |  |  |  |
| such LLM-augmented tools into complete CRS pipelines. | SourceForge, and direct email. We withheld public disclosure |  |  |  |  |  |  |
| LLM-based vulnerability repair. | Several benchmarks eval- | of vulnerability details until maintainers acknowledged the |  |  |  |  |  |
| uate LLM agents on security tasks: SEC-bench [29], Cy- | reports. The proof-of-vulnerability inputs and patches are |  |  |  |  |  |  |
| bench [53], AutoPatchBench [10], and CVE-Bench [49]. On | shared with maintainers to facilitate timely remediation. |  |  |  |  |  |  |
| the technique side, San2Patch [25] automates vulnerability | We are actively communicating with project maintainers |  |  |  |  |  |  |
| repair from sanitizer logs via tree-of-thought LLM reasoning, | and responsible parties to ensure all reported issues are |  |  |  |  |  |  |
| stronger results than applying them in isolation [54]. OSS- | OSS-CRS, including the framework, all integrated CRSs, |  |  |  |  |  |  |
| CRS provides the infrastructure to study this integration: its | and evaluation artifacts, is publicly available at https://github. |  |  |  |  |  |  |
| LLM proxy tracks per-CRS costs, enabling comparison of | com/ossf/oss-crs. The repository includes the CRS interface |  |  |  |  |  |  |
| LLM-augmented versus traditional techniques under fixed | specification, | libCRS | library, configuration templates, and |  |  |  |  |
| budgets. | documentation for porting new CRSs. |  |  |  |  |  |  |
| DARPA’s | AI | Cyber | Challenge | produced | seven | au- | implementation of the bug-fixing infrastructure in OSS- |
| tonomous CRSs for finding and fixing vulnerabilities, but | CRS. We thank Sin Liang Lee, Isaac Hung, Joshua Wang, |  |  |  |  |  |  |
| left them entangled with competition-specific infrastructure. | and Jiho Kim for their contributions to the bug-finding |  |  |  |  |  |  |
| We analyzed all seven finalist CRSs and identified three | campaign. We also thank Jeff Diecks and the Open Source |  |  |  |  |  |  |
| categories of barriers (infrastructure duplication, cloud lock- | Security Foundation (OpenSSF) for supporting OSS-CRS |  |  |  |  |  |  |
| in, and monolithic design) that prevent real-world deployment. | as an OpenSSF sandbox project and promoting community |  |  |  |  |  |  |

---

## Page 11

References Applications Conference (ACSAC) , 2020.

[2] Apache Software Foundation. Kafka, 2026. https://github.com/apache/

[3] A. Arya, O. Chang, J. Metzman, K. Serebryany, and D. Liu. OSS-

https://github.com/BerriAI/litellm.

2017. URL https://sites.cs.ucsb.edu/~vigna/publications/2017_Phrack_

2024. URL https://github.com/trailofbits/buttercup.

among diverse fuzzers. In Proceedings of the 28th USENIX Security

research/programs/cyber-grand-challenge.

Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via

hunter-found-20-security-vulnerabilities/.

at Runtime. In Proceedings of the 32nd USENIX Security Symposium

(Security) , Anaheim, CA, Aug. 2023.

C. Giuffrida, and T. Holz. Cupid : Automatic fuzzer selection for

11

[21] A. Hazimeh, A. Herrera, and M. Payer. Magma: A Ground-Truth

org/doi/10.1145/3428334.

com/helm/helm.

D. Kim, F. Fleischer, J. Cho, J. Kim, K. Ko, I. Yun, S. Park, D. Baik,

cs.AI.

4419, 2025.

(AIxCC).

Association, Aug. 2021.

com/google/oss-fuzz-gen.

Open Source Software, Aug. 2024. URL http://arxiv.org/abs/2408.

Software Engineering , ESEC/FSE 2021, pages 1393–1403, New

[35] OASIS. Static Analysis Results Interchange Format (SARIF) Version

html.

[36] OpenAI. Introducing Aardvark: OpenAI’s Agentic Security Researcher.

| [1] | Proceedings of the 34th USENIX Security Symposium (Security) | , | Fuzzing Benchmark. | Proc. ACM Meas. Anal. Comput. Syst. | , 4(3): |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Seattle, WA, Aug. 2025. | 49:1–49:29, Nov. 2020. doi: 10.1145/3428334. URL https://dl.acm. |  |  |  |  |  |  |  |  |  |  |  |  |
| kafka. | [22] | Helm. Helm: The Kubernetes Package Manager, 2026. https://github. |  |  |  |  |  |  |  |  |  |  |  |
| Fuzz: continuous fuzzing for open source software, 2016. | https: | [23] | C. Intelligence. Jazzer: Coverage-guided, in-process fuzzing for the |  |  |  |  |  |  |  |  |  |  |
| //github.com/google/oss-fuzz. | jvm, 2025. https://github.com/CodeIntelligenceTesting/jazzer. |  |  |  |  |  |  |  |  |  |  |  |  |
| [4] | D. Bass. | One of the Best Hackers in the Country Is an AI Bot. | [24] | T. Kim, H. Han, S. Park, D. R. Jeong, D. Kim, D. Kim, E. Kim, |  |  |  |  |  |  |  |  |  |
| Bloomberg, 2025. https://www.bloomberg.com/news/articles/2025-06- | J. Kim, J. Wang, K. Kim, S. Ji, W. Song, H. Zhao, A. Chin, G. Lee, |  |  |  |  |  |  |  |  |  |  |  |  |
| 24/one-of-the-best-hackers-in-the-country-is-an-ai-bot. | K. Stevens, M. Alharthi, Y. Zhai, C. Zhang, J. Jang, Y. Jang, A. Askar, |  |  |  |  |  |  |  |  |  |  |  |  |
| [5] | T. Becker, R. Goulden, Y. Kim, J. Kwon, S. Myung, T. Nighswander, | H. Lee, H. Heo, M. Gwon, M. Lee, M. Baek, S. Min, W. Kim, Y. Jin, |  |  |  |  |  |  |  |  |  |  |  |
| and S. Seo. aixcc-afc-archive: Public source code release of theori’s | Y. Park, Y. Choi, J. Jung, G. Lee, J. Jang, K. Kim, Y. Cha, and |  |  |  |  |  |  |  |  |  |  |  |  |
| aixcc afc submission, Aug. 2025. | URL https://github.com/theori- | Y. Kim. ATLANTIS: AI-driven Threat Localization, Analysis, and |  |  |  |  |  |  |  |  |  |  |  |
| io/aixcc-afc-archive/. | Triage Intelligence System. | arXiv | , Sept. 2025. doi: 10.48550/arXiv. |  |  |  |  |  |  |  |  |  |  |
| [6] | BerriAI. LiteLLM: Call 100+ LLM APIs in OpenAI format, 2026. | 2509.14589. URL https://arxiv.org/abs/2509.14589. Cross-listed in |  |  |  |  |  |  |  |  |  |  |  |
| [7] | A. Bianchi, K. Borgolte, J. Corbetta, F. Disperati, A. Dutcher, J. Grosen, | [25] | Y. Kim, S. Shin, H. Kim, and J. Yoon. Logs In, Patches Out: Automated |  |  |  |  |  |  |  |  |  |  |
| P. Grosen, A. Machiry, C. Salls, Y. Shoshitaishvili, N. Stephens, | Vulnerability Repair via Tree-of-Thought LLM Analysis. | In | 34th |  |  |  |  |  |  |  |  |  |  |
| G. Vigna, and R. Wang. Cyber grand shellphish. | Phrack | , 16(70), June | USENIX Security Symposium (USENIX Security 25) | , pages 4401– |  |  |  |  |  |  |  |  |  |
| CyberGrandShellphish.pdf. | [26] | kubernetes. kubernetes: Production-Grade Container Scheduling and |  |  |  |  |  |  |  |  |  |  |  |
| [8] | BugBuster. | 42-b3yond-6ug-crs: Bugbuster, our team’s submission | Management, 2026. https://github.com/kubernetes/kubernetes. |  |  |  |  |  |  |  |  |  |  |
| to the ai cyber challenge final competition, Aug. 2025. URL https: | [27] | Kudu Dynamics. SHERPA: Security Harness Engineering for Robust |  |  |  |  |  |  |  |  |  |  |  |
| //github.com/42-b3yond-6ug/42-b3yond-6ug-crs. | Program Analysis, 2025. URL https://github.com/AIxCyberChallenge/ |  |  |  |  |  |  |  |  |  |  |  |  |
| [9] | Buttercup. Buttercup: finds and patches software vulnerabilities, Dec. | sherpa.git. | Developed as part of DARPA’s AI Cyber Challenge |  |  |  |  |  |  |  |  |  |  |
| [10] | T. | Byun, | C. | Aschermann, | K. | Y. | Thng, | W. | Zhou, | Y. | Yang, | [28] | Lacrosse. afc-crs-lacrosse: Aixcc finals 2025 crs submission, Aug. |
| L. | Deason, | and | J. | Saxe. | Introducing | AutoPatchBench: | A | 2025. URL https://github.com/siftech/afc-crs-lacrosse. |  |  |  |  |  |
| Benchmark | for | AI-Powered | Security | Fixes, | Apr. | 2025. | URL | [29] | H. Lee, Z. Zhang, H. Lu, and L. Zhang. | SEC-bench: Automated |  |  |  |
| https://engineering.fb.com/2025/04/29/ai-research/autopatchbench- | benchmarking of LLM agents on real-world software security tasks. In |  |  |  |  |  |  |  |  |  |  |  |  |
| benchmark-ai-powered-security-fixes/. | The thirty-ninth annual conference on neural information processing |  |  |  |  |  |  |  |  |  |  |  |  |
| [11] | C. Chen, B. Dolan-Gavitt, and Z. Lin. ELFuzz: Efficient Input Gener- | systems | , 2025. URL https://openreview.net/forum?id=QQhQIqons0. |  |  |  |  |  |  |  |  |  |  |
| ation via LLM-driven Synthesis Over Fuzzer Space. In | Proceedings | [30] | Y. Li, S. Ji, Y. Chen, S. Liang, W.-H. Lee, Y. Chen, C. Lyu, C. Wu, |  |  |  |  |  |  |  |  |  |  |
| of the 34th USENIX Security Symposium (Security) | SEC [1]. | R. Beyah, P. Cheng, et al. | UNIFUZZ: A holistic and pragmatic |  |  |  |  |  |  |  |  |  |  |
| [12] | Y. Chen, Y. Jiang, F. Ma, J. Liang, M. Wang, C. Zhou, X. Jiao, | metrics-driven platform for evaluating fuzzers. In | Proceedings of the |  |  |  |  |  |  |  |  |  |  |
| and Z. Su. | Enfuzz: Ensemble fuzzing with seed synchronization | USENIX Security Symposium (Security) | , pages 2777–2794. USENIX |  |  |  |  |  |  |  |  |  |  |
| Symposium (Security) | , Santa Clara, CA, Aug. 2019. | [31] | D. Liu, O. Chang, J. Metzman, M. Sablotny, and M. Maruseac. OSS- |  |  |  |  |  |  |  |  |  |  |
| [13] | DARPA. | Cyber Grand Challenge, 2016. | https://www.darpa.mil/ | Fuzz-Gen: LLM powered fuzzing via OSS-Fuzz, 2024. https://github. |  |  |  |  |  |  |  |  |  |
| [14] | DARPA. AIxCC Archive, 2025. https://archive.aicyberchallenge.com/. | [32] | X. Mei, P. S. Singaria, J. D. Castillo, H. Xi, Abdelouahab, Benchikh, |  |  |  |  |  |  |  |  |  |  |
| [15] | DARPA. | AI | Cyber | Challenge | (AIxCC), | 2025. | URL | https:// | T. Bao, R. Wang, Y. Shoshitaishvili, A. Doupé, H. Pearce, and |  |  |  |  |
| aicyberchallenge.com/. Accessed: 2025-09-09. | B. Dolan-Gavitt. ARVO: Atlas of Reproducible Vulnerabilities for |  |  |  |  |  |  |  |  |  |  |  |  |
| [16] | Y. Deng, C. S. Xia, H. Peng, C. Yang, and L. Zhang. Large Language | 02153. arXiv:2408.02153 [cs]. |  |  |  |  |  |  |  |  |  |  |  |
| Large Language Models. In | Proceedings of the 32nd ACM SIGSOFT | [33] | R. Meng, M. Mirchev, M. Böhme, and A. Roychoudhury. | Large |  |  |  |  |  |  |  |  |  |
| International Symposium on Software Testing and Analysis | , ISSTA | Language Model Guided Protocol Fuzzing. | In | Proceedings of the |  |  |  |  |  |  |  |  |  |
| 2023, pages 423–435. Association for Computing Machinery, 2023. | 2024 Annual Network and Distributed System Security Symposium |  |  |  |  |  |  |  |  |  |  |  |  |
| doi: 10.1145/3597926.3598067. | (NDSS) | , San Diego, CA, Feb. 2024. |  |  |  |  |  |  |  |  |  |  |  |
| [17] | A. Fioraldi, D. Maier, D. Zhang, and D. Balzarotti. | LibAFL: A | [34] | J. Metzman, L. Szekeres, L. Simon, R. Sprabery, and A. Arya. |  |  |  |  |  |  |  |  |  |
| Framework to Build Modular and Reusable Fuzzers. In | Proceedings | FuzzBench: an open fuzzer benchmarking platform and service. In |  |  |  |  |  |  |  |  |  |  |  |
| of the 29th ACM conference on Computer and communications security | Proceedings of the 29th ACM Joint Meeting on European Software |  |  |  |  |  |  |  |  |  |  |  |  |
| (CCS) | , CCS ’22. ACM, November 2022. | Engineering Conference and Symposium on the Foundations of |  |  |  |  |  |  |  |  |  |  |  |
| [18] | L. | Franceschi-Bicchierai. | Google | says | its | AI-based | bug | York, NY, USA, Aug. 2021. Association for Computing Machinery. |  |  |  |  |  |
| hunter | found | 20 | security | vulnerabilities. | TechCrunch, | 2025. | ISBN 978-1-4503-8562-6. | doi: 10.1145/3468264.3473932. | URL |  |  |  |  |
| https://techcrunch.com/2025/08/04/google-says-its-ai-based-bug- | https://dl.acm.org/doi/10.1145/3468264.3473932. |  |  |  |  |  |  |  |  |  |  |  |  |
| [19] | Y.-F. Fu, J. Lee, and T. Kim. autofz: Automated Fuzzer Composition | 2.1.0, 2023. https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0. |  |  |  |  |  |  |  |  |  |  |  |
| [20] | E. Güler, P. Görz, E. Geretto, A. Jemmett, S. Österlund, H. Bos, | OpenAI, 2025. https://openai.com/index/introducing-aardvark/. |  |  |  |  |  |  |  |  |  |  |  |
| collaborative fuzzing. In | Proceedings of the Annual Computer Security | [37] | OSS-CRS, 2026. URL https://github.com/ossf/oss-crs. |  |  |  |  |  |  |  |  |  |  |

---

## Page 12

| [38] | PostgreSQL. Postgresql, 2026. https://github.com/postgres/postgres. | https://arxiv.org/abs/2602.07666. Cross-listed in cs.AI. |  |  |
| --- | --- | --- | --- | --- |
| [39] | T. L. Project. libfuzzer – a library for coverage-guided fuzz testing. | [55] | K. Zhang, Z. Li, D. Wu, S. Wang, and X. Xia. | Low-Cost and |
| https://llvm.org/docs/LibFuzzer.html, 2025. Accessed: 2025-12-09. | Comprehensive Non-textual Input Fuzzing with LLM-Synthesized |  |  |  |
| [40] | RabbitMQ. Rabbitmq-server: core server and tier 1 (built-in) plugins, | Input Generators. | In | Proceedings of the 34th USENIX Security |
| 2026. https://github.com/rabbitmq/rabbitmq-server. | Symposium (Security) | SEC [1]. |  |  |
| [41] | Redis. | Redis: preferred, fastest, and most feature-rich cache, data | [56] | S. Österlund, E. Geretto, A. Jemmett, E. Güler, P. Görz, T. Holz, |
| structure server, and document and vector query engine, 2026. https: | C. Giuffrida, and H. Bos. Collabfuzz: A framework for collabora- |  |  |  |
| //github.com/redis/redis. | tive fuzzing. | In | Proceedings of the 14th European Workshop on |  |

Systems Security , EuroSec ’21, pages 1–7. Association for Com-

[42] S. Rudra. FFmpeg Calls Google’s AI Bug Reports “CVE Slop”. It’s puting Machinery, 2021. doi: 10.1145/3447852.3458720. URL

FOSS, 2025. https://itsfoss.com/news/ffmpeg-google-fiasco/. https://doi.org/10.1145/3447852.3458720.

[43] K. Serebryany, D. Bruening, A. Potapenko, and D. Vyukov. Address-

Sanitizer: A Fast Address Sanity Checker. In 2012 USENIX Annual

Technical Conference (USENIX ATC 12) , pages 309–318, 2012.

[44] Z. Sheng, Q. Xu, J. Huang, M. Woodcock, H. Huang, A. F. Donaldson,

G. Gu, and J. Huang. All You Need Is A Fuzzing Brain: An LLM-

Powered System for Automated Vulnerability Detection and Patching,

Sept. 2025. URL http://arxiv.org/abs/2509.07225. arXiv:2509.07225

[cs].

[45] D. Stenberg. AI slop security reports submitted to

curl. GitHub Gist, 2025. https://gist.github.com/bagder/

07f7581f6e3d78ef37dfbfc81fd1d1cd.

[46] D. Stenberg. The end of the curl bug-bounty. Daniel Stenberg Blog,

2026. https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-

bounty/.

[47] the Big Sleep team. From Naptime to Big Sleep: Using Large

Language Models To Catch Vulnerabilities In Real-World Code.

Project Zero, 2024. https://projectzero.google/2024/10/from-naptime-

to-big-sleep.html.

[48] M. Walker. Machine vs. Machine: Lessons from the First Year of Cyber

Grand Challenge. In 24th USENIX Security Symposium (USENIX

Security 15) , Washington, D.C., Aug. 2015. USENIX Association.

[49] P. Wang, X. Liu, and C. Xiao. CVE-Bench: Benchmarking LLM-

based Software Engineering Agent’s Ability to Repair Real-World

CVE Vulnerabilities. In L. Chiruzzo, A. Ritter, and L. Wang, editors,

Proceedings of the 2025 Conference of the Nations of the Americas

Chapter of the Association for Computational Linguistics: Human

Language Technologies (Volume 1: Long Papers) , pages 4207–4224,

Albuquerque, New Mexico, Apr. 2025. Association for Computational

Linguistics. ISBN 979-8-89176-189-6. doi: 10.18653/v1/2025.naacl-

long.212. URL https://aclanthology.org/2025.naacl-long.212/.

[50] C. S. Xia, M. Paltenghi, J. L. Tian, M. Pradel, and L. Zhang.

Fuzz4ALL: Universal Fuzzing with Large Language Models. In

Proceedings of the IEEE/ACM 46th International Conference on

Software Engineering , ICSE ’24, pages 126:1–126:13. Association for

Computing Machinery, 2024.

[51] Y. Yang, S. Yao, J. Chen, and W. Lee. Hybrid Language Processor

Fuzzing via LLM-Based Constraint Solving. In Proceedings of the

34th USENIX Security Symposium (Security) SEC [1].

[52] Z. Yu, Z. Guo, Y. Wu, J. Yu, M. Xu, D. Mu, Y. Chen, and X. Xing.

PatchAgent: A Practical Program Repair Agent Mimicking Human

Expertise. In 34th USENIX Security Symposium (USENIX Security

25) , pages 4381–4400, 2025.

[53] A. K. Zhang, N. Perry, R. Dulepet, J. Ji, C. Menders, J. W. Lin,

E. Jones, G. Hussein, S. Liu, D. J. Jasper, P. Peetathawatchai, A. Glenn,

V. Sivashankar, D. Zamoshchin, L. Glikbarg, D. Askaryar, H. Yang,

A. Zhang, R. Alluri, N. Tran, R. Sangpisit, K. O. Oseleononmen,

D. Boneh, D. E. Ho, and P. Liang. Cybench: A framework for

evaluating cybersecurity capabilities and risks of language models. In

The Thirteenth International Conference on Learning Representations ,

2025. URL https://openreview.net/forum?id=tc90LV0yRL.

[54] C. Zhang, Y. Park, F. Fleischer, Y.-F. Fu, J. Kim, D. Kim, Y. Kim,

Q. Xu, A. Chin, Z. Sheng, H. Zhao, B. J. Lee, J. Wang, M. Pelican,

D. J. Musliner, J. Huang, J. Silliman, M. Mcdaniel, J. Casavant,

I. Goldthwaite, N. Vidovich, M. Lehman, and T. Kim. Sok: Darpa’s

ai cyber challenge (aixcc): Competition design, architectures, and

lessons learned. arXiv , 2026. doi: 10.48550/arXiv.2602.07666. URL

12

---

## Page 13

Appendix

We present the complete crs.yaml and crs-compose.yaml configura-

tion files for the three CRSs integrated in §4: CRS - LIBFUZZER (§4.2),

A TLANTIS -M ULTI L ANG (§4.3), and C LAUDE C ODE (§4.4). The crs.yaml

manifest declares each CRS’s capabilities, supported languages, required

LLM models, and build/run phase definitions, while crs-compose.yaml

specifies resource allocations and runtime settings for a given deployment,

including an ensemble example that combines multiple CRSs in a single run.

We also include the LiteLLM proxy configurations used for multi-model

routing (§3.5): one for A TLANTIS -M ULTI L ANG , which routes directly to

upstream providers, and one for C LAUDE C ODE , which proxies requests to

an external LiteLLM instance.

Listing 1: crs.yaml for CRS - LIBFUZZER

1 name : crs-libfuzzer

2 type :

3 - bug-finding

4 version : 1.0.0

5 docker_registry : ghcr.io/oss-crs/crs-libfuzzer

6

7 prepare_phase :

8 hcl : oss-crs/docker-bake.hcl

9

10 target_build_phase :

| 11 | - | name | : build |
| --- | --- | --- | --- |
| 12 | dockerfile | : oss-crs/dockerfiles/builder.Dockerfile |  |
| 13 | outputs | : |  |
| 14 | - build |  |  |

15

16 crs_run_phase :

| 17 | fuzzer | : |
| --- | --- | --- |
| 18 | dockerfile | : oss-crs/dockerfiles/runner.Dockerfile |

19

20 supported_target :

| 21 | mode | : |
| --- | --- | --- |
| 22 | - full |  |
| 23 | - delta |  |
| 24 | language | : |
| 25 | - c |  |
| 26 | sanitizer | : |
| 27 | - address |  |
| 28 | architecture | : |
| 29 | - x86_64 |  |

13

---

## Page 14

1 name : atlantis-multilang-wo-concolic

2 type :

3 - bug-finding

4 version : 1.0.0

5 docker_registry : ghcr.io/oss-crs/atlantis-multilang-wo-concolic

6

7 prepare_phase :

8 hcl : oss-crs/docker-bake.hcl

9

10 target_build_phase :

| 11 | - | name | : uniafl-build |
| --- | --- | --- | --- |
| 12 | dockerfile | : oss-crs/dockerfiles/builder.Dockerfile |  |
| 13 | additional_env | : |  |
| 14 | BUILD_TYPE | : uniafl |  |
| 15 | outputs | : |  |
| 16 | - uniafl/build |  |  |
| 17 | - uniafl/src |  |  |
| 18 | - uniafl/project |  |  |
| 19 | - | name | : coverage-build |
| 20 | dockerfile | : oss-crs/dockerfiles/builder.Dockerfile |  |
| 21 | additional_env | : |  |
| 22 | BUILD_TYPE | : coverage |  |
| 23 | outputs | : |  |
| 24 | - coverage/build |  |  |
| 25 | - | name | : lsp-build |
| 26 | dockerfile | : oss-crs/dockerfiles/lsp_builder.Dockerfile |  |
| 27 | outputs | : |  |
| 28 | - lsp/compile_commands.json |  |  |
| 29 | - | name | : create-config |
| 30 | dockerfile | : oss-crs/dockerfiles/multilang.Dockerfile |  |
| 31 | additional_env | : |  |
| 32 | RUN_TYPE | : CREATE_CONFIG |  |
| 33 | outputs | : |  |
| 34 | - uniafl/config.yaml |  |  |

35

36 crs_run_phase :

| 37 | multilang | : |
| --- | --- | --- |
| 38 | dockerfile | : oss-crs/dockerfiles/multilang.Dockerfile |
| 39 | additional_env | : |
| 40 | # Input generators for fuzzing (comma-separated) |  |
| 41 | # Available options: |  |
| 42 | # | - given_fuzzer: Use provided seed corpus (default) |
| 43 | # | - testlang_input_gen: Test language-based input generation |
| 44 | # | - dict_input_gen: Dictionary-based input generation |
| 45 | # | - mlla: Multi-language LLM agent for input generation |
| 46 | CRS_INPUT_GENS | : given_fuzzer,mlla,testlang_input_gen,dict_input_gen |
| 47 | redis | : |
| 48 | dockerfile | : oss-crs/dockerfiles/redis.Dockerfile |
| 49 | init_codeindexer | : |
| 50 | dockerfile | : oss-crs/dockerfiles/multilang.Dockerfile |
| 51 | additional_env | : |
| 52 | RUN_TYPE | : INIT_CODEINDEXER |
| 53 | joern | : |
| 54 | dockerfile | : oss-crs/dockerfiles/joern.Dockerfile |
| 55 | lsp | : |
| 56 | dockerfile | : oss-crs/dockerfiles/lsp.Dockerfile |

57

58 supported_target :

| 59 | mode | : |
| --- | --- | --- |
| 60 | - full |  |
| 61 | - delta |  |
| 62 | language | : |
| 63 | - c |  |
| 64 | sanitizer | : |
| 65 | - address |  |
| 66 | architecture | : |
| 67 | - x86_64 |  |

68

69 required_llms :

| 70 | - o4-mini |
| --- | --- |
| 71 | - gpt-4o |
| 72 | - gpt-4o-mini |
| 73 | - gpt-4.1 |
| 74 | - gpt-4.1-mini |
| 75 | - claude-sonnet-4-20250514 |
| 76 | - claude-opus-4-20250514 |
| 77 | - claude-3-7-sonnet-20250219 |
| 78 | - claude-3-5-haiku-20241022 |
| 79 | - gemini-2.5-pro |

Listing 2: crs.yaml for A TLANTIS -M ULTI L ANG

14

---

## Page 15

1 name : crs-claude-code

2 type :

3 - bug-fixing

4 version : 1.0.0

5 docker_registry : ghcr.io/oss-crs/crs-claude-code

6

7 prepare_phase :

8 hcl : oss-crs/docker-bake.hcl

9

10 target_build_phase :

| 11 | - | name | : default-build |
| --- | --- | --- | --- |
| 12 | dockerfile | : oss-crs/builder.Dockerfile |  |
| 13 | outputs | : |  |
| 14 | - build |  |  |
| 15 | - src |  |  |
| 16 | - | name | : inc-builder-asan |
| 17 | snapshot | : true |  |
| 18 | dockerfile | : oss-crs-infra:default-builder |  |
| 19 | additional_env | : |  |
| 20 | SANITIZER | : address |  |

21

22 crs_run_phase :

| 23 | patcher | : |
| --- | --- | --- |
| 24 | dockerfile | : oss-crs/patcher.Dockerfile |
| 25 | additional_env | : |
| 26 | # Set via compose yaml additional_env. |  |
| 27 | CRS_AGENT | : claude_code |
| 28 | # ANTHROPIC_MODEL: claude-sonnet-4-5-20250929 |  |
| 29 | # CLAUDE_CODE_SUBAGENT_MODEL: claude-sonnet-4-5-20250929 |  |
| 30 | # ANTHROPIC_DEFAULT_OPUS_MODEL: claude-sonnet-4-5-20250929 |  |
| 31 | # ANTHROPIC_DEFAULT_SONNET_MODEL: claude-sonnet-4-5-20250929 |  |
| 32 | # ANTHROPIC_DEFAULT_HAIKU_MODEL: claude-sonnet-4-5-20250929 |  |
| 33 | # AGENT_TIMEOUT: "0" | # seconds, 0 = no limit (default) |
| 34 | inc-builder-asan | : |
| 35 | run_snapshot | : true |
| 36 | dockerfile | : oss-crs-infra:default-builder |

37

38 supported_target :

| 39 | mode | : |  |
| --- | --- | --- | --- |
| 40 | - full |  |  |
| 41 | - delta |  |  |
| 42 | language | : | # language-agnostic — agent edits source, builder sidecar handles compilation |
| 43 | - c |  |  |
| 44 | - c++ |  |  |
| 45 | - jvm |  |  |
| 46 | sanitizer | : |  |
| 47 | - address |  |  |
| 48 | - undefined |  |  |
| 49 | architecture | : |  |
| 50 | - x86_64 |  |  |

51

52 required_llms :

| 53 | - claude-opus-4-6 |
| --- | --- |
| 54 | - claude-sonnet-4-6 |
| 55 | - claude-haiku-4-5-20251001 |

56 # - claude-opus-4-5-20251101

57 # - claude-sonnet-4-5-20250929

58 # - claude-haiku-4-5-20251001

Listing 3: crs.yaml for C LAUDE C ODE

1 # --- General Settings -------------------------------------------------------

2 run_env : local

3 docker_registry : local

4

5 # --- Infrastructure ---------------------------------------------------------

6 oss_crs_infra :

| 7 | cpuset | : "0-3" |
| --- | --- | --- |
| 8 | memory | : "16G" |

9

10 # --- CRS (crs-libfuzzer) ---------------------------------------------------

11 # Pure fuzzer — no LLM or builder sidecar needed.

12 crs-libfuzzer :

| 13 | cpuset | : "4-7" |
| --- | --- | --- |
| 14 | memory | : "16G" |

Listing 4: crs-compose.yaml for CRS - LIBFUZZER

15

---

## Page 16

1 # --- General Settings -------------------------------------------------------

2 run_env : local

3 docker_registry : local

4

5 # --- Infrastructure ---------------------------------------------------------

6 oss_crs_infra :

| 7 | cpuset | : "0-3" |
| --- | --- | --- |
| 8 | memory | : "16G" |

9

10 # --- CRS (atlantis-multilang-wo-concolic) -----------------------------------

11 atlantis-multilang-wo-concolic :

| 12 | cpuset | : "4-8" |
| --- | --- | --- |
| 13 | memory | : "16G" |
| 14 | llm_budget | : 100 |

15

16 # --- LLM Configuration -----------------------------------------------------

17 llm_config :

| 18 | litellm | : |
| --- | --- | --- |
| 19 | mode | : internal |
| 20 | internal | : |
| 21 | config_path | : ./example/atlantis-multilang-wo-concolic/litellm-config.yaml |

Listing 5: crs-compose.yaml for A TLANTIS -M ULTI L ANG

1 # --- General Settings -------------------------------------------------------

2 run_env : local

3 docker_registry : local

4

5 # --- Infrastructure ---------------------------------------------------------

6 oss_crs_infra :

| 7 | cpuset | : "0-1" |
| --- | --- | --- |
| 8 | memory | : "8G" |

9

10 # --- CRS (crs-claude-code) -------------------------------------------------

11 # Builder sidecars are declared in crs.yaml (snapshot: true / run_snapshot: true)

12 # and handled automatically by the framework — no separate entry needed.

13 crs-claude-code :

| 14 | cpuset | : "2-7" |
| --- | --- | --- |
| 15 | memory | : "16G" |
| 16 | llm_budget | : 10 |
| 17 | additional_env | : |
| 18 | # Override CRS defaults here. Available models: |  |
| 19 | # | claude-opus-4-6, claude-opus-4-5-20251101, claude-opus-4-1-20250805, |
| 20 | # | claude-sonnet-4-5-20250929, claude-sonnet-4-20250514, claude-haiku-4-5-20251001 |
| 21 | CRS_AGENT | : claude_code |
| 22 | ANTHROPIC_MODEL | : claude-opus-4-6 |
| 23 | # CLAUDE_CODE_SUBAGENT_MODEL: claude-sonnet-4-5-20250929 |  |
| 24 | # ANTHROPIC_DEFAULT_OPUS_MODEL: claude-sonnet-4-5-20250929 |  |
| 25 | # ANTHROPIC_DEFAULT_SONNET_MODEL: claude-sonnet-4-5-20250929 |  |
| 26 | # ANTHROPIC_DEFAULT_HAIKU_MODEL: claude-sonnet-4-5-20250929 |  |
| 27 | # AGENT_TIMEOUT: "3600" | # Optional: seconds, 0 = no limit (default) |

28

29 # --- LLM Configuration -----------------------------------------------------

30 llm_config :

| 31 | litellm | : |
| --- | --- | --- |
| 32 | mode | : internal |
| 33 | internal | : |
| 34 | config_path | : ./example/crs-claude-code/litellm-config.yaml |

Listing 6: crs-compose.yaml for C LAUDE C ODE

16

---

## Page 17

1 # --- General Settings -------------------------------------------------------

2 run_env : local

3 docker_registry : local

4

5 # --- Infrastructure ---------------------------------------------------------

6 oss_crs_infra :

| 7 | cpuset | : "0-3" |
| --- | --- | --- |
| 8 | memory | : "16G" |

9

10 # --- CRS (crs-libfuzzer) ---------------------------------------------------

11 crs-libfuzzer :

| 12 | cpuset | : "8-11" |
| --- | --- | --- |
| 13 | memory | : "16G" |

14

15 # --- CRS (atlantis-multilang-wo-concolic) -----------------------------------

16 atlantis-multilang-wo-concolic :

| 17 | cpuset | : "4-7" |
| --- | --- | --- |
| 18 | memory | : "16G" |
| 19 | llm_budget | : 100 |

20

21 # --- LLM Configuration -----------------------------------------------------

22 llm_config :

| 23 | litellm | : |
| --- | --- | --- |
| 24 | mode | : internal |
| 25 | internal | : |
| 26 | config_path | : ./example/atlantis-multilang-wo-concolic/litellm-config.yaml |

Listing 7: crs-compose.yaml for ensemble deployment

17

---

## Page 18

1 model_list :

| 2 | ######################################### |  |  |
| --- | --- | --- | --- |
| 3 | # OPENAI API |  |  |
| 4 | ######################################### |  |  |
| 5 | - | model_name | : o4-mini |
| 6 | litellm_params | : |  |
| 7 | model | : openai/o4-mini |  |
| 8 | api_key | : os.environ/OPENAI_API_KEY |  |

9

| 10 | - | model_name | : gpt-4o |
| --- | --- | --- | --- |
| 11 | litellm_params | : |  |
| 12 | model | : openai/gpt-4o |  |
| 13 | api_key | : os.environ/OPENAI_API_KEY |  |

14

| 15 | - | model_name | : gpt-4o-mini |
| --- | --- | --- | --- |
| 16 | litellm_params | : |  |
| 17 | model | : openai/gpt-4o-mini |  |
| 18 | api_key | : os.environ/OPENAI_API_KEY |  |

19

| 20 | - | model_name | : gpt-4.1 |
| --- | --- | --- | --- |
| 21 | litellm_params | : |  |
| 22 | model | : openai/gpt-4.1 |  |
| 23 | api_key | : os.environ/OPENAI_API_KEY |  |

24

| 25 | - | model_name | : gpt-4.1-mini |
| --- | --- | --- | --- |
| 26 | litellm_params | : |  |
| 27 | model | : openai/gpt-4.1-mini |  |
| 28 | api_key | : os.environ/OPENAI_API_KEY |  |

29

| 30 | ######################################### |  |  |
| --- | --- | --- | --- |
| 31 | # ANTHROPIC API |  |  |
| 32 | ######################################### |  |  |
| 33 | - | model_name | : claude-3-7-sonnet-20250219 |
| 34 | litellm_params | : |  |
| 35 | model | : anthropic/claude-3-7-sonnet-20250219 |  |
| 36 | api_key | : os.environ/ANTHROPIC_API_KEY |  |

37

| 38 | - | model_name | : claude-sonnet-4-20250514 |
| --- | --- | --- | --- |
| 39 | litellm_params | : |  |
| 40 | model | : anthropic/claude-sonnet-4-20250514 |  |
| 41 | api_key | : os.environ/ANTHROPIC_API_KEY |  |

42

| 43 | - | model_name | : claude-opus-4-20250514 |
| --- | --- | --- | --- |
| 44 | litellm_params | : |  |
| 45 | model | : anthropic/claude-opus-4-20250514 |  |
| 46 | api_key | : os.environ/ANTHROPIC_API_KEY |  |

47

| 48 | - | model_name | : claude-3-5-haiku-20241022 |
| --- | --- | --- | --- |
| 49 | litellm_params | : |  |
| 50 | model | : anthropic/claude-3-5-haiku-20241022 |  |
| 51 | api_key | : os.environ/ANTHROPIC_API_KEY |  |

52

| 53 | ######################################### |  |  |
| --- | --- | --- | --- |
| 54 | # GEMINI API |  |  |
| 55 | ######################################### |  |  |
| 56 | - | model_name | : gemini-2.5-pro |
| 57 | litellm_params | : |  |
| 58 | model | : gemini/gemini-2.5-pro |  |
| 59 | api_key | : os.environ/GEMINI_API_KEY |  |

Listing 8: LiteLLM proxy configuration for A TLANTIS -M ULTI L ANG (§3.5)

18

---

## Page 19

1 model_list :

| 2 | ######################################### |  |  |
| --- | --- | --- | --- |
| 3 | # ANTHROPIC API (via external LiteLLM) |  |  |
| 4 | # model_name = what Claude Code sends in API requests (bare names) |  |  |
| 5 | # litellm_params.model = how LiteLLM routes to the provider |  |  |
| 6 | ######################################### |  |  |
| 7 | - | model_name | : claude-opus-4-6 |
| 8 | litellm_params | : |  |
| 9 | model | : anthropic/claude-opus-4-6 |  |
| 10 | api_base | : os.environ/EXTERNAL_LITELLM_API_BASE |  |
| 11 | api_key | : os.environ/EXTERNAL_LITELLM_API_KEY |  |

12

| 13 | - | model_name | : claude-sonnet-4-6 |
| --- | --- | --- | --- |
| 14 | litellm_params | : |  |
| 15 | model | : anthropic/claude-sonnet-4-6 |  |
| 16 | api_base | : os.environ/EXTERNAL_LITELLM_API_BASE |  |
| 17 | api_key | : os.environ/EXTERNAL_LITELLM_API_KEY |  |

18

| 19 | - | model_name | : claude-haiku-4-5-20251001 |
| --- | --- | --- | --- |
| 20 | litellm_params | : |  |
| 21 | model | : anthropic/claude-haiku-4-5-20251001 |  |
| 22 | api_base | : os.environ/EXTERNAL_LITELLM_API_BASE |  |
| 23 | api_key | : os.environ/EXTERNAL_LITELLM_API_KEY |  |

24

| 25 | - | model_name | : claude-opus-4-5-20251101 |
| --- | --- | --- | --- |
| 26 | litellm_params | : |  |
| 27 | model | : anthropic/claude-opus-4-5-20251101 |  |
| 28 | api_base | : os.environ/EXTERNAL_LITELLM_API_BASE |  |
| 29 | api_key | : os.environ/EXTERNAL_LITELLM_API_KEY |  |

30

| 31 | - | model_name | : claude-opus-4-1-20250805 |
| --- | --- | --- | --- |
| 32 | litellm_params | : |  |
| 33 | model | : anthropic/claude-opus-4-1-20250805 |  |
| 34 | api_base | : os.environ/EXTERNAL_LITELLM_API_BASE |  |
| 35 | api_key | : os.environ/EXTERNAL_LITELLM_API_KEY |  |

36

| 37 | - | model_name | : claude-sonnet-4-5-20250929 |
| --- | --- | --- | --- |
| 38 | litellm_params | : |  |
| 39 | model | : anthropic/claude-sonnet-4-5-20250929 |  |
| 40 | api_base | : os.environ/EXTERNAL_LITELLM_API_BASE |  |
| 41 | api_key | : os.environ/EXTERNAL_LITELLM_API_KEY |  |

42

| 43 | - | model_name | : claude-sonnet-4-20250514 |
| --- | --- | --- | --- |
| 44 | litellm_params | : |  |
| 45 | model | : anthropic/claude-sonnet-4-20250514 |  |
| 46 | api_base | : os.environ/EXTERNAL_LITELLM_API_BASE |  |
| 47 | api_key | : os.environ/EXTERNAL_LITELLM_API_KEY |  |

Listing 9: LiteLLM proxy configuration for C LAUDE C ODE , forwarding to an external LiteLLM instance (§3.5)

19

---
title: "From Context to Rules: Toward Unified Detection Rule Generation"
author: "Cheng Meng; Wenxin Le; Xinyi Li; Qiuyun Wang; Fangli Ren; Zhengwei Jiang; Baoxu Liu"
creator: "arXiv GenPDF (tex2pdf:a6404ea)"
pages: 15
---

# From Context to Rules: Toward Unified Detection Rule Generation

> **作者**：Cheng Meng; Wenxin Le; Xinyi Li; Qiuyun Wang; Fangli Ren; Zhengwei Jiang; Baoxu Liu
> **總頁數**：15 頁

---

## Page 1

From Context to Rules: Toward Unified Detection

Rule Generation

Cheng Meng 1 , 2 , Wenxin Le 1 , 2 , Xinyi Li 2 , Qiuyun Wang 1 , 2 , Fangli Ren 1 ⋆ ,

Zhengwei Jiang 1 , 2 , and Baoxu Liu 1 , 2

1 Institute of Information Engineering, Chinese Academy of Sciences, Beijing, China

2 School of Cyber Security, University of Chinese Academy of Sciences, Beijing, China

{mengcheng, lewenxin, wangqiuyun, renfangli, jiangzhengwei,

liubaoxu}@iie.ac.cn

lixinyi22@mails.ucas.ac.cn

Abstract. Existing methods for detection rule generation are tightly

coupled to specific input-output combinations, requiring dedicated pipelines

for each. We formalize this problem as a unified mapping f : C × L → R

and characterize optimal rules through semantic distance. We propose

UniRule, an agentic RAG framework built on dual semantic projection

spaces: detection intent and detection logic. This design enables retrieval

and generation across arbitrary contexts and target languages within a

single system. Experiments across 12 scenarios (3 languages, 4 context

types, 12,000 pairwise comparisons) show that UniRule significantly out-

performs pure LLM generation with a Bradley-Terry coefficient of 0.52,

validating semantic projection as an effective abstraction for unified rule

generation. Together, the formalization, method, and evaluation provide

an initial framework for studying detection rule generation as a unified

task.

Keywords: Detection Rule Generation · Large Language Models · Retrieval-

Augmented Generation · Semantic Projection

1 Introduction

Cybersecurity detection rules are formal specifications that translate threat be-

haviors into executable logic for security monitoring systems. They form the

backbone of identifying malicious activities across various platforms, including

arXiv:2604.11078v1 [cs.CR] 13 Apr 2026 network intrusion detection systems (e.g., Snort, Suricata), endpoint monitoring

systems (e.g., Elastic Security), and SIEM engines (e.g., Splunk). The diversity

of rule languages mirrors the heterogeneity of security infrastructures, with each

language offering unique syntax and semantic expressiveness tailored to different

detection scenarios.

Automated detection rule generation has long been a research focus. Tra-

ditional methods, such as signature extraction [13], template-based generation,

⋆ Corresponding author: renfangli@iie.ac.cn

---

## Page 2

2 C. Meng et al.

and machine learning [17], derive rules from malware samples or network traffic.

Recently, advances in large language models (LLMs) have opened new avenues,

enabling rule generation from natural language descriptions, threat intelligence

reports, and other unstructured sources. Techniques like LLMCloudHunter [14],

ThreatPilot [18], GridAI [8], and FALCON [12] have shown promising results in

their respective areas.

However, existing approaches are highly fragmented. Traditional methods

and LLM-based techniques focus on specific combinations of input contexts (e.g.,

CTI reports, attack descriptions) and output rule languages (e.g., Sigma, Snort,

Splunk), leading to isolated pipelines that fail to generalize across different sce-

narios.

This fragmentation is driven by the research paradigm itself: specific threat

scenarios motivate dedicated system designs, and these systems are naturally

validated within the same scenarios they target. Toward unified detection rule

generation, we argue that the generation process, rather than individual detec-

tion scenarios, should be the object of study. Based on this principle, we develop

a formal task definition, a generation framework, and an evaluation methodology

that operate across context types and rule languages.

As an initial step toward this goal, we make the following contributions:

– We formalize detection rule generation as a unified mapping task f : C ×

L → R , providing a task definition that spans arbitrary contexts and rule

languages. By characterizing optimal rules through semantic distance, we

demonstrate the inadequacy of token-level metrics and establish a rigorous

basis for pairwise preference evaluation.

– We propose UniRule, an agentic RAG framework that enables unified re-

trieval and generation across heterogeneous context types and rule languages

within a single architecture. This is achieved by projecting rules into two

language-agnostic semantic spaces, detection intent and detection logic, al-

lowing rules from any source language to be retrieved and reused.

– We conduct experiments across 12 scenarios spanning 3 rule languages and

4 context types, with 12,000 pairwise judgments. The results validate UniR-

ule’s generalizability across diverse settings. They also reveal when semantic

retrieval improves versus hinders generation, delineating the current bound-

aries of this approach.

To the best of our knowledge, this is the first work to formulate and address

detection rule generation as a unified task across both context types and rule

languages. All prompts, implementation details, and source code are available

at https://github.com/MengC1024/UniRule .

2 Related Work

Automated detection rule generation has evolved from statistical modeling and

program analysis to recent LLM-based approaches. Early methods extract rules

---

## Page 3

From Context to Rules: Toward Unified Detection Rule Generation 3

from structured inputs within specific domains: signature extraction from traf-

fic [13], PLC code analysis for industrial control systems [16], binary analysis

for YARA rules and network signatures [9,15], and statistical learning to detect

SIEM rule evasions [17]. While precise, these approaches are inherently frag-

mented, each constrained to a single input type and security domain.

Table 1. Comparison of LLM-based Detection Rule Generation Methods

| Method | Context Type | Target Language |
| --- | --- | --- |
| LLMCloudHunter [14] CTI, TTP, Cloud | Sigma |  |
| ThreatPilot [18] | CTI, TTP, Exec. Feedback | Sigma |
| Hu et al. [5] | CTI, Traffic, Rules, Exec. Feedback Snort, Suricata |  |
| GRIDAI [8] | Traffic, Rules, Exec. Feedback | Suricata |
| FALCON [12] | CTI, Rules, Exec. Feedback | Snort, YARA |
| RULELLM [19] | Package, Rules, Exec. Feedback | YARA, Semgrep |
| Hex2Sign [1] | Hexadecimal Traffic | Suricata |
| Ours | Textual Context, Rules | Any |

The advent of LLMs has shifted the paradigm toward generating rules from

diverse, unstructured inputs. As summarized in Table 1, recent approaches lever-

age LLMs to bridge the gap between natural language descriptions and formal

rules, with each method targeting specific context types and rule languages.

These methods employ diverse technical approaches, including multi-agent or-

chestration, retrieval-augmented generation, and execution feedback loops, yet

each remains tied to its specific input-output combination. A system built for

CTI-to-Sigma generation cannot be directly applied to log-based Splunk rule

generation without substantial re-engineering.

At the root, all existing efforts treat rule generation as a byproduct of specific

detection tasks, rather than as an object of study in its own right. Our work

addresses this gap by studying the generation process itself, independent of any

particular threat scenario or rule language.

3 Problem Formulation

3.1 Unified Detection Rule Generation

We define three spaces. The detection context space C is the set of all inputs

from which detection requirements can be specified; a context c ∈ C may be

a natural language description, a CTI report, a threat intent specification, or

raw observational data (e.g., log entries, network captures, malware samples).

The rule language space L is the set of detection rule languages, each defining

a formal syntax and execution semantics for threat detection (e.g., Splunk SPL,

S

Elastic Query DSL, Snort). The rule space R = l ∈L R l , where R l is the set

---

## Page 4

4 C. Meng et al.

of syntactically valid rules in language l . We formulate unified detection rule

generation as:

f : C × L → R (1)

Given a context c ∈ C and target language l ∈ L , the goal is to produce r =

f ( c, l ) ∈ R l that captures the detection requirements of c in the syntax of l .

To characterize what f should produce, we introduce three functions over an

abstract universe of threat behaviors U , where each element represents an atomic

observable behavior (e.g., a specific process execution, network connection, or

registry modification) that a detection rule may or may not cover.

U U U

I : C → 2 , E : L → 2 , Cov : R → 2 (2)

where I captures the intended threat behaviors specified by a context, E the

expressiveness boundary of a language, and Cov the actual detection coverage

of a rule. In §4, we operationalize I and Cov by projecting rules into natural

language descriptions of detection intent and detection logic, respectively. The

achievable intent I ( c ) ∩ E ( l ) represents the portion of c ’s detection requirements

expressible in language l . The optimal rule minimizes the discrepancy between

its coverage and the achievable intent:

∗

r c,l = arg min | Cov ( r ) △ ( I ( c ) ∩ E ( l )) | (3)

r ∈R l

Since multiple rules may achieve the same minimum, optimality defines an equiv-

alence class:

| n | o |
| --- | --- |
| ∗ | ′ |

[ r c,l ] = r ∈ R l | Cov ( r ) △ ( I ( c ) ∩ E ( l )) | = min | Cov ( r ) △ ( I ( c ) ∩ E ( l )) |

r ′

(4)

3.2 Semantic Distance and Evaluation

The distance of a generated rule from the optimal class is:

∗ ′

d ( r, [ r c,l ]) = | Cov ( r ) △ ( I ( c ) ∩ E ( l )) | − min | Cov ( r ) △ ( I ( c ) ∩ E ( l )) | (5)

r ′

with d ≥ 0 and d = 0 ⇐⇒ r ∈ [ r ∗

c,l ] . The symmetric difference decomposes as:

Cov ( r ) △ ( I ( c ) ∩ E ( l )) = ( I ( c ) ∩ E ( l )) \ Cov ( r ) ∪ Cov ( r ) \ ( I ( c ) ∩ E ( l )) (6)

| {z } | {z }

under-detection over-detection

When c includes executable observational data (e.g., logs, traffic captures), these

two components can be approximated by execution-based recall and precision,

respectively. However, such data is rarely available at scale, making this approach

impractical for systematic evaluation. For natural-language contexts, I ( c ) , E ( l ) ,

and Cov ( r ) are further analytically intractable. The equivalence class (Eq. 4)

also complicates evaluation: for any single reference rule r ref ∈ [ r ∗

c,l ] , a token-

level similarity metric sim satisfies:

d ( r 1 ) < d ( r 2 ) ̸ ⇒ sim ( r 1 , r ref ) > sim ( r 2 , r ref ) (7)

---

## Page 5

From Context to Rules: Toward Unified Detection Rule Generation 5

That is, a rule closer to optimal in semantic distance may nonetheless differ

more from any particular reference in surface form, so metrics such as BLEU

or exact match do not reliably rank rules by quality. This divergence is espe-

cially pronounced in detection rules: for example, content:"/etc/passwd" and

content:"/etc/passwd|00|" differ by a few characters, yet the former matches

a plaintext path while the latter targets a null-terminated binary payload—

covering entirely different behaviors.

For a pair of candidates r 1 , r 2 , however, the relative comparison remains

feasible:

∗ ∗

d ( r 1 , [ r c,l ]) ≶ d ( r 2 , [ r c,l ]) (8)

While computing d directly is intractable, human experts or LLMs can perceive

which rule better approximates the intended detection given the original context.

This motivates our adoption of pairwise preference evaluation aggregated via the

Bradley-Terry model (§5.2).

| 4 | Method: UniRule |
| --- | --- |
| Online Rule Generation | Offline Knowledge Construction |

Context

| Augmentation | Reference Rules | Return |
| --- | --- | --- |
| Input | Detection | Translate |
| Query: Query text | Intent |  |

Source Rules

| LLM | Call | Space: Intent/Logic |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Agent | k | : Number of results | Retrieve | Embedding | LLM | Input | (Splunk/snort |
| Language: Target Language | /Elastic/etc.) |  |  |  |  |  |  |

Detection

| Output | Translate |
| --- | --- |
| Semantic Index | Logic |

Rule

Fig. 1. Overview of UniRule. At runtime (left), given a detection context and target

language, an LLM agent autonomously retrieves relevant rules as needed and generates

the output. Offline (right), heterogeneous source rules are translated into detection

intent and detection logic descriptions, then embedded and indexed.

The functions I and Cov defined in §3 are central to rule quality but cannot

be computed from raw rules. We propose UniRule, an agentic RAG framework

that operationalizes them through two computable proxies expressed in natural

language: detection intent d intent ( r ) for I , and detection logic d logic ( r ) for Cov.

As shown in Figure 1, this facilitates unification in both directions: offline,

rules are decomposed into intent and logic descriptions; online, the LLM agent

reasons only about intent and logic, independent of rule language.

---

## Page 6

6 C. Meng et al.

4.1 Offline Knowledge Construction

We translate each rule into natural language descriptions along both seman-

tic dimensions, then embed and index them for retrieval. Given a source rule

collection:

N

K = { ( r i , l i ) } i =1 (9)

where N is the total number of rules, r i is a detection rule and l i ∈ L is its

language, we construct Semantic Indexes through the following unified steps.

Rule Translation. For each source tuple ( r i , l i ) ∈ K , we employ an LLM to

translate its semantic content regarding both dimensions. Let d s ( r i ) denote the

natural language description for dimension s :

d s ( r i ) = Translate ( r i , s ) , s ∈ { intent , logic } (10)

Embedding and Indexing. We encode the translated descriptions into

dense vector representations (dimension d ). Let ϕ s ( r i ) denote the embedding:

d

ϕ s ( r i ) = Embed ( d s ( r i )) ∈ R (11)

Finally, the index S s is constructed by aggregating these embeddings and ex-

plicitly associating them with the original source rule collection K and their

corresponding natural language descriptions d s ( r i ) :

S s = { ( ϕ s ( r i ) , r i , l i , d s ( r i )) | ( r i , l i ) ∈ K} (12)

Since any rule can be translated into these descriptive dimensions, this pro-

cess homogenizes heterogeneous sources into a unified knowledge base.

4.2 Online Rule Generation

Given a source collection K and its semantic indexes, we augment generation by

retrieving relevant existing rules:

r = f ( c, l, Retrieve ( c, K )) (13)

Since a context c may invoke intent, logic, or both, the optimal retrieval strategy

varies per input. We therefore implement Retrieve as an iterative process over a

search primitive, where the agent autonomously decides which semantic space to

query, how many rounds to issue, and whether to filter by language. Concretely,

Retrieve is realized as:

[ T

′

Retrieve ( c, K ) = Search ( q t , s t , k t , l t ) (14)

t =1

where T ≥ 0 is the number of iterations dynamically determined by the agent,

and each Search call queries the Semantic Indexes ( S intent , S logic ).

---

## Page 7

From Context to Rules: Toward Unified Detection Rule Generation 7

Retrieval Tool. We expose the unified knowledge base through a function

interface. 3 The search function is defined as:

′ k

Search ( q, s, k, l ) → { ( r j , l j , d s,j , σ j ) } j =1 (15)

where q is the query text, s ∈ { intent , logic } targets the semantic space, k is

the retrieval limit, and l ′ is an optional language filter. The tool computes the

similarity score σ based on vector embedding:

σ j = cos( Embed ( q ) , ϕ s ( r j )) (16)

and returns the top- k rules ranked by similarity.

Agentic Generation. Unlike standard RAG pipelines that execute a fixed

retrieval-then-generate sequence, the agent autonomously determines its retrieval

strategy. Given the input context c and target language l , the agent decides

whether to retrieve at all ( T = 0 is permitted), which semantic space to query,

what query to formulate, and when to stop. In practice, we observe that the

agent adapts its behavior to input characteristics: for underspecified contexts

(e.g., brief threat descriptions), it typically issues multiple retrieval rounds across

both spaces to gather sufficient reference material; for detailed inputs (e.g., com-

plete detection logic specifications), it often generates directly with minimal or

no retrieval.

5 Evaluation

5.1 Experimental Setup

We evaluate on three rule languages (Splunk SPL, Elastic Query DSL, and Snort)

sourced from community repositories, covering three major security domains:

SIEM (Splunk), endpoint detection (Elastic), and network intrusion detection

(Snort). 4 Each corpus is split 80/20 into a training set forming the source col-

lection K (Splunk: 1,512; Elastic: 1,077; Snort: 448) and a test set (Splunk: 378;

Elastic: 270; Snort: 113).

Each test rule is paired with four input contexts to evaluate generalization.

Context is the native rule description, while CTI, Intent, and Logic are syn-

thetically generated to simulate diverse semantic dimensions reflecting different

operational focuses:

1. Context: The original description field from the source rule.

2. CTI: A synthetic Cyber Threat Intelligence snippet simulating unstructured

reporting.

3. Intent ( φ threat ): The adversarial goal derived via our offline semantic trans-

lation (§4.1).

3 To facilitate reproducibility and tool interoperability, we implement the interface

supporting the Model Context Protocol (MCP).

4 Splunk: https://github.com/splunk/security_content ; Elastic: https://github

.com/elastic/detection-rules ; Snort: https://www.snort.org/ .

---

## Page 8

8 C. Meng et al.

4. Detection Logic ( φ det ): The technical implementation pattern derived via

our offline translation (§4.1).

This yields 3 × 4 = 12 experimental scenarios, with 100 sampled instances each

(1,200 total).

All generation uses DeepSeek-V3.2 [10] (non-thinking mode); all embeddings

use Qwen3-Embedding-8B [20].

We compare UniRule against four configurations (Table 2), as no prior method

supports unified generation across diverse languages and contexts. The two RAG

baselines retrieve k =15 reference rules from K , exceeding UniRule’s average

of k ¯ ≈ 13 . 3 (mean 4.91 rules × 2.71 agent calls), ensuring that any UniRule

advantage is not attributable to retrieving more examples. Rand. RAG sam-

ples rules uniformly regardless of relevance. Std. RAG embeds raw rule source

code with the same embedding model and retrieves by cosine similarity against

the input context, without decomposing into intent and logic spaces. Human-

Authored (HA) uses the original expert-written rule directly.

Table 2. Baseline configurations. K : source collection; S intent , S logic : dual semantic

indexes.

| Method | Retrieval | Source | Purpose |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline | None | — | LLM-only ( | ξ | =0 | anchor) |  |  |  |  |  |  |  |
| Rand. RAG | Random, | k | =15 | K | Syntactic scaffolding |  |  |  |  |  |  |  |  |
| Std. RAG | Cosine sim., | k | =15 | K | Single-space retrieval |  |  |  |  |  |  |  |  |
| Human-Auth. | — | — | Original expert rule |  |  |  |  |  |  |  |  |  |  |
| UniRule | Agent, | k | ¯ | ≈ | 13 | . | 3 | S | intent | , | S | logic | Dual semantic retrieval |

5.2 Evaluation Methodology

Semantically equivalent rules can differ substantially in surface form, making

token-level metrics unreliable. We adopt pairwise preference evaluation following

the Chatbot Arena methodology [3].

  M 

Pairwise Comparison. For M =5 methods, we enumerate all 2 =10 pairs per

scenario. For each pair and test instance, an LLM judge (DeepSeek-V3.2, think-

ing mode) receives the input context and two anonymized candidates in random-

ized order, outputting a preference H t ∈ { i, j, tie } . This yields 100 × 10 × 12 =

12 , 000 pairwise judgments.

Bradley-Terry Model. Pairwise outcomes are aggregated via the Bradley-Terry

(BT) model [2]:

1

P ( i ≻ j ) = (17)

1 + exp( ξ j − ξ i )

where ξ i ∈ R is the BT coefficient for method i . We anchor ξ Baseline = 0 ; all

other coefficients represent relative gains. Ties count as half a win per side.

---

## Page 9

From Context to Rules: Toward Unified Detection Rule Generation 9

Parameter Estimation. Let w ij denote the fractional win count of i over j .

Coefficients are estimated via maximum likelihood:

X h i

ξ ˆ = arg min − w ij log P ( i ≻ j ) − w ji log P ( j ≻ i ) (18)

ξ

i<j

subject to ξ Baseline = 0 , solved via L-BFGS-B with analytical gradients. Uncer-

tainty is quantified by sandwich robust standard errors [4]:

−

Var( ξ ˆ 1 − 1

) = H S H (19)

P

where H is the Hessian of Eq. (18) and S = ⊤

t g t g t the outer product of

per-observation score vectors g t = ∇ ξ ℓ t . We report 95% confidence intervals as

ξ ˆ

i ± 1 . 96 · SE i .

Judge Validation. To verify that the LLM judge’s preferences align with human

judgment, we randomly sampled 100 pairwise comparisons uniformly across sce-

narios. Three cybersecurity experts with more than three years of experience,

independently labeled each pair. As shown in Table 3, the average agreement

rate is 77.0% with Cohen’s κ = 0 . 73 (range: 0 . 71 – 0 . 76 ), indicating substantial

agreement [7] and confirming the reliability of the LLM judge for our evaluation.

Table 3. Agreement between LLM judge and human experts.

| Metric | Value |  |
| --- | --- | --- |
| Human experts | 3 |  |
| Validated comparisons | 100 |  |
| Avg. Agreement | 77.0% |  |
| Avg. Cohen’s | κ | 0.73 (0.71–0.76) |

Table 4. Bradley-Terry coefficients ( ξ ) across rule languages and context types. Best

per column in bold . Baseline is the reference ( ξ =0 ).

| By Rule Language | By Context Type |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Method | Splunk Elastic | Snort | Context | CTI | Intent | Logic | Overall |  |  |  |  |  |  |  |  |  |
| Baseline | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |  |  |  |  |  |  |  |  |
| Rand. RAG | 0.25 | 0.30 | − | 0.70 | − | 0.14 | 0.04 | − | 0.03 | 0.03 | − | 0.03 |  |  |  |  |
| Std. RAG | 0.12 | 0.25 | − | 0.84 | − | 0.08 | − | 0.09 | 0.02 | − | 0.35 | − | 0.13 |  |  |  |
| Human-Auth. | − | 0.32 | − | 0.31 | − | 2.28 | − | 0.91 | − | 1.06 | − | 1.00 | − | 0.61 | − | 0.87 |
| UniRule | 0.99 | 0.87 | − | 0.33 | 0.52 | 1.06 | 0.68 | − | 0.05 | 0.52 |  |  |  |  |  |  |

---

## Page 10

10 C. Meng et al.

5.3 Main Results

Table 4 presents BT coefficients aggregated by rule language and context type.

UniRule achieves the highest overall coefficient ( ξ ˆ = 0 . 52 ), substantially out-

performing all baselines. Both Std. RAG ( − 0 . 13 ) and Rand. RAG ( − 0 . 03 ) fall

below the LLM-only Baseline, indicating that naive retrieval introduces noise

that degrades generation. Human-Authored rules consistently receive the lowest

coefficients (overall − 0 . 87 ); we discuss possible causes in §6. By rule language,

UniRule delivers strong gains on Splunk ( 0 . 99 ) and Elastic ( 0 . 87 ), while on Snort

all methods score below the Baseline. By context type, CTI contexts yield the

largest advantage ( 1 . 06 ), while Detection Logic shows minimal differentiation.

Figure 2 presents the per-scenario breakdown. Of the 12 scenarios, UniRule is

significantly positive in 9 and significantly negative in 3, with no non-significant

results.

All 8 Splunk and Elastic scenarios show significant improvement, with coeffi-

cients ranging from 0 . 28 to 1 . 51 . These languages capture behaviors (e.g., event

counts, field patterns) where semantic retrieval can fill information gaps with

transferable logic. In contrast, 3 of 4 Snort scenarios are significantly negative,

reaching − 0 . 97 on Detection Logic inputs. Snort rules encode signatures (specific

byte sequences) that cannot be inferred from semantically similar rules. Simi-

larly, Detection Logic inputs already provide complete specifications, leaving no

gap for retrieval to fill. In both cases, retrieval introduces noise rather than useful

references. We analyze this phenomenon in §6.

UniRule: Per-Scenario Performance with 95% CI

| Splunk | · | Context | 0.97 |  |
| --- | --- | --- | --- | --- |
| Splunk | · | CTI | 1.51 |  |
| Splunk | · | Intent | 1.39 |  |
| Splunk | · | Det. Logic | 0.28 |  |
| Elastic | · | Context | 0.84 |  |
| Elastic | · | CTI | 1.26 |  |
| Elastic | · | Intent | 1.04 |  |
| Elastic | · | Det. Logic | 0.45 |  |
| Snort | · | Context | -0.30 |  |
| Snort | · | CTI | 0.43 |  |
| Snort | · | Intent | -0.42 | Splunk |

Elastic

Snort · Det. Logic -0.97 Snort

1.0 0.5 0.0 0.5 1.0 1.5

BT Coefficient ( )

Fig. 2. UniRule per-scenario BT coefficients with 95% confidence intervals. Positive

values indicate improvement over the LLM-only Baseline ( ξ =0 , dashed line). Intervals

not crossing zero are statistically significant at p < 0 . 05 .

---

## Page 11

From Context to Rules: Toward Unified Detection Rule Generation 11

5.4 Ablation Study

modest gain from combining both spaces.

( ξ ) relative to Baseline ( ξ =0 ). Best per column in

By Rule Language

5.5 Case Study

Splunk Rule

| tstats `security_content_summariesonly` count min(_time) as firstTime max(_time) as lastTime from

"*.htm.exe", "*.html.exe", "*.txt.exe", "*.pdf.exe", "*.docx.exe", "*.xlsx.exe", "*.pptx.exe","*.one.exe", datamodel=Endpoint.Processes where Processes.process IN ("*.doc.exe", "*.xls.exe","*.ppt.exe",

Processes.parent_process_id Processes.parent_process_name Processes.parent_process_path Processes.parent_process Processes.parent_process_exec Processes.parent_process_guid "*.bat.exe", "*rtf.exe") by Processes.action Processes.dest Processes.original_file_name

Processes.process_id Processes.process_integrity_level Processes.process_name Processes.process_path Processes.process Processes.process_exec Processes.process_guid Processes.process_hash

`security_content_ctime(lastTime)` | `drop_dm_object_name(Processes)` |

`execution_of_file_with_multiple_extensions_filter`

gray text shows full descriptions.

bold .

By Context Type

Detection Intent

Detects execution of files with double extensions (e.g., "report.pdf.exe"),

a technique used by adversaries to disguise malicious executables as

benign documents for initial compromise and evasion

disguise malicious executables. The malicious intent is to trick users or systems into executing malware by This rule detects execution of files with double extensions, a common technique used by adversaries to

engineering to bypass user caution and technical controls that might allow common document types.

Translate

Detection Logic

Matches process creation events where the process name contains a

disguised executable.

first extension mimics a common document or data file type and the second extension is .exe. It searches the This detection rule identifies processes that appear to be executable files with double extensions, where the

provide context. The core technical mechanism is matching process execution events where the process path *.doc.exe, *.xls.exe, etc. Endpoint.Processes data model for process executions where the process name matches patterns like The rule aggregates events by numerous process and parent process attributes to

or name ends with a non executable extension. This is a common technique used by malware to disguise malicious executables as - executable file extension (e.g., .doc, .pdf, .txt) immediately followed by the .exe

benign documents or files, relying on users or systems misinterpreting the full filename. The final filter (execution_of_file_with_multiple_extensions_filter) likely refines the results to reduce false positives.

Table 5 isolates the contribution of each semantic space. Both Intent-Only ( ξ =

0 . 39 ) and Logic-Only ( ξ = 0 . 34 ) outperform the Baseline, confirming that seman-

tic retrieval improves generation regardless of which space is used. Combining

both spaces yields a modest further gain (UniRule: ξ = 0 . 44 ). The limited im-

provement can be attributed to information overlap between the two spaces: as

shown in the Figure 3, intent and logic descriptions often encode related infor-

mation from different angles, causing them to retrieve similar reference rules.

This redundancy explains the correlated performance across scenarios and the

Table 5. Ablation study: contribution of semantic spaces. Bradley-Terry coefficients

| Method | Splunk Elastic | Snort | Context | CTI | Intent | Logic | Overall |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |  |  |
| Intent-Only | 0.87 | 0.56 | − | 0.20 | 0.55 | 0.67 | 0.44 | − | 0.05 | 0.39 |
| Logic-Only | 0.78 | 0.77 | − | 0.46 | 0.33 | 0.88 | 0.41 | − | 0.21 | 0.34 |
| UniRule | 0.89 | 0.80 | − | 0.30 | 0.44 | 1.02 | 0.44 | − | 0.08 | 0.44 |
| \| tstats ... from datamodel=Endpoint.Processes where | making a dangerous file appear as a safe document or text file (like .doc, .pdf, .txt). The adversary's goal is |  |  |  |  |  |  |  |  |  |
| Processes.process IN ("*.doc.exe", "*.pdf.exe", "*.txt.exe", ...) by | initial compromise, evasion, and persistence. By naming a file something like "report.pdf.exe", the visible |  |  |  |  |  |  |  |  |  |

Processes.dest Processes.process_name … document. When executed, the .exe runs, deploying malware. This is a form of masquerading aimed at social extension in some user interfaces may only show ".pdf", leading the victim to believe it is a harmless

Processes.user Processes.user_id Processes.vendor_product | `security_content_ctime(firstTime)` | document extension (e.g., .doc, .pdf) followed by .exe, indicating a

Fig. 3. Semantic decomposition of a Splunk rule detecting double-extension files (ID:

b06a555e-dce0-417d-a2eb-28a5d8d66ef7). The rule is translated into detection intent

(threat semantics) and detection logic (technical patterns). Bold text shows summaries;

---

## Page 12

12 C. Meng et al.

observed in our ablation study.

UniRule Reasoning Trace

Context

Detects potential resource exhaustion or data breach attempts by

behavior could indicate an attempt to counts, submit numerous requests, and receive large responses. This monitoring for users who consistently generate high input token

unusually large amount of data, possibly revealing sensitive information overload the system or extract an

or causing service disruptions.

Input

Retrieval Tool

count data breach attempts", resource exhaustion high token

| "k": 5 | intent | ", | Call |
| --- | --- | --- | --- |
| Reference Rules | Generate |  |  |
| Retrieval Tool | LLM Agent |  |  |

response data extraction monitoring", "query": " high request volume large

Reference Rules

prehensive rule than the Human-Authored alternative.

preference scores in our evaluation.

6 Discussion and Limitation

Output Comparison

| UniRule | Human | - | Authored |  |
| --- | --- | --- | --- | --- |
| from logs | // 1. Time Window Aggregation (5m buckets) | - | * | from logs |
| \| stats | \| stats |  |  |  |
| req_count = count(), | avg_tokens = avg(input_tokens), | total_count = count(*), |  |  |
| by user.id, @timestamp | total_resp = sum(response_size) | by user.id | avg_compl = avg(completion_tokens) |  |
| // 2. Multi | \| where | - | dimensional Thresholding | // 2. Static Thresholds |
| (req_count >= 100) OR | \| where |  |  |  |

(avg_tokens >= 5000) OR // Volumetric Attack

| (total_resp >= 100MB) | // Resource Exhaustion | (max_tokens > 5000) AND |
| --- | --- | --- |
| // Data Exfiltration | (total_count > 10) |  |
| req_count > 500 OR total_resp > 500MB, "Critical", | total_count |  |
| true(), "Medium") | \| where risk_score > 10 |  |

Semantic Decomposition. Figure 3 illustrates how a Splunk rule detecting double-

extension files is decomposed into detection intent and detection logic. The intent

abstracts the adversarial goal (disguising executables as documents), enabling

threat-level retrieval regardless of rule language; the logic preserves technical

specifics (matching process creation with double extensions), enabling retrieval

by implementation pattern. Notably, the two descriptions encode overlapping

information from different angles, which explains the correlated retrieval results

| "query": " | \| bucket span=5m @timestamp | // 1. Simple Aggregation (No Time Window) | - | aws_bedrock* |  |
| --- | --- | --- | --- | --- | --- |
| "space": " | max_tokens = max(prompt_tokens), |  |  |  |  |
| "space": " | detection | // 3. Contextual Severity Scoring | // 3. Basic Risk Formula |  |  |
| "k": 5 | logic | ", | Call | \| eval severity = case( | \| eval risk_score = (max_tokens / 1000) * |

Fig. 4. UniRule reasoning trace and output comparison. Left: the agent retrieves ref-

erence rules from both intent and logic spaces. Right: UniRule generates a more com-

Generation Process. Figure 4 shows how UniRule generates an Elastic rule for

detecting resource exhaustion. The agent issues two retrieval calls, one per se-

mantic space, and synthesizes the retrieved references into the final rule. Com-

pared to the Human-Authored rule, UniRule produces a more comprehensive

detection with time-window aggregation, multi-dimensional thresholds, and con-

textual severity scoring, illustrating why Human-Authored rules receive lower

6.1 The Double-Edged Sword of Semantic Retrieval.

The value of semantic retrieval lies in filling information gaps. When such gaps

do not exist or cannot be filled through semantic similarity, retrieval becomes

counterproductive. This principle explains two patterns in our results.

First, Snort rules encode signatures: specific byte sequences that fingerprint

particular malware. When the agent retrieves a semantically similar rule (e.g.,

---

## Page 13

From Context to Rules: Toward Unified Detection Rule Generation 13

another “Trojan C2” detection), it may copy byte patterns belonging to a dif-

ferent malware family. The generated rule is syntactically valid but detects the

wrong threat. Without retrieval, the LLM produces generic rules or abstains from

guessing specific bytes; with retrieval, reference rules provide false confidence.

Second, Detection Logic inputs already specify how to write the rule. Re-

trieval introduces references that may conflict with the given specification, de-

grading rather than improving generation. Both cases share the same root cause:

semantic retrieval cannot provide what the task actually needs—precise byte sig-

natures in Snort, or nothing at all when the input is already complete.

6.2 Intent Alignment vs. Production Optimization

Human-Authored rules consistently score lowest ( ξ = − 0 . 87 ). As shown in Fig-

ure 4, UniRule generates specification-rich rules with explicit time windows,

multi-dimensional thresholds, and contextual annotations, while expert rules are

deployment-optimized: terse, focused, and stripped of verbose metadata.

Within our task definition, this outcome is expected. Given an input con-

text describing a detection goal, the LLM-generated rule more completely re-

flects that intent. However, expert rules are not designed to be self-contained

specifications; they assume operational context, complementary controls, and

environment-specific tuning. In production settings, their simplicity may offer

advantages in robustness and maintainability.

This parallels code generation benchmarks [6,11], which evaluate whether

generated code reflects user intent, not whether it outperforms human-written

code in production. Our task is intent-to-rule translation: given a context, pro-

duce a rule that faithfully captures the specified detection requirements. By

this criterion, UniRule succeeds. More broadly, our Bradley-Terry evaluation

measures alignment with detection intent, not operational metrics such as false

positive rates on real traffic, and cannot fully catch semantic hallucinations such

as incorrect field names propagated from retrieved references. Closing this gap

remains future work.

6.3 Scope of Detection Contexts.

Our theoretical framework (§3) defines the detection context space C to include

raw observational data (e.g., system logs, network traffic). However, our current

method and evaluation are constrained to textual inputs because our dataset

lacks paired raw data. While the feasibility of generating rules from such data

via execution feedback has been established in prior studies [8,18,1,19,12,5], ex-

tending UniRule to this modality requires datasets that contain both ground-

truth rules and their corresponding raw trigger events, which remains a target

for future data collection.

---

## Page 14

| 14 | C. Meng et al. |
| --- | --- |
| 7 | Conclusion and Future Work |

This work demonstrates that unified detection rule generation is a viable research

direction. Our problem formulation establishes that the task can be rigorously

defined across arbitrary contexts and rule languages. The proposed method,

UniRule, confirms that generation across heterogeneous context types and rule

languages is practically achievable within a single architecture. The evaluation

methodology further validates that rule quality under this unified setting can be

systematically measured. Experiments across 12 scenarios with 12,000 pairwise

judgments support these findings.

Future work spans two directions. First, extending inputs to raw observa-

tional data such as logs and network traffic would enable end-to-end rule gener-

ation. Second, incorporating execution feedback would allow iterative refinement

toward deployment-grade rules, with evaluation against operational metrics in

real-world security environments.

Acknowledgments. This work was supported by the Youth Innovation Promotion

Association, CAS (No. 2023170) and Beijing Key Laboratory of Network Security and

Protection Technology.

References

1. Balasubramanian, P., Ali, T., Salmani, M., KhoshKholgh, D., Kostakos, P.:

Hex2sign: Automatic ids signature generation from hexadecimal data using llms.

In: 2024 IEEE International Conference on Big Data (BigData). pp. 4524–4532.

IEEE (2024)

2. Bradley, R.A., Terry, M.E.: Rank analysis of incomplete block designs: I. the

method of paired comparisons. Biometrika 39 (3/4), 324–345 (1952)

3. Chiang, W.L., Zheng, L., Sheng, Y., Angelopoulos, A.N., Li, T., Li, D., Zhu, B.,

Zhang, H., Jordan, M., Gonzalez, J.E., et al.: Chatbot arena: An open platform

for evaluating llms by human preference. In: Forty-first International Conference

on Machine Learning (2024)

4. Freedman, D.A.: On the so-called “huber sandwich estimator” and “robust standard

errors”. The American Statistician 60 (4), 299–302 (2006)

5. Hu, X., Chen, H., Bao, H., Wang, W., Liu, F., Zhou, G., Yin, P.: A llm-based

agent for the automatic generation and generalization of ids rules. In: 2024 IEEE

23rd International Conference on Trust, Security and Privacy in Computing and

Communications (TrustCom). pp. 1875–1880. IEEE (2024)

6. Jimenez, C.E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., Narasimhan, K.:

Swe-bench: Can language models resolve real-world github issues? (2024), https:

//arxiv.org/abs/2310.06770

7. Landis, J.R., Koch, G.G.: The measurement of observer agreement for categorical

data. biometrics pp. 159–174 (1977)

8. Li, J., Chai, Y., Du, L., Duan, C., Yan, H., Gu, Z.: Gridai: Generating and repairing

intrusion detection rules via collaboration among multiple llm-based agents (2025),

https://arxiv.org/abs/2510.13257

---

## Page 15

From Context to Rules: Toward Unified Detection Rule Generation 15

9. Li, S., Ming, J., Qiu, P., Chen, Q., Liu, L., Bao, H., Wang, Q., Jia, C.: Packgenome:

Automatically generating robust yara rules for accurate malware packer detection.

In: Proceedings of the 2023 ACM SIGSAC Conference on Computer and Commu-

nications Security. pp. 3078–3092 (2023)

10. Liu, A., Mei, A., Lin, B., Xue, B., Wang, B., Xu, B., Wu, B., Zhang, B., Lin,

C., Dong, C., et al.: Deepseek-v3. 2: Pushing the frontier of open large language

models. arXiv preprint arXiv:2512.02556 (2025)

11. Merrill, M.A., Shaw, A.G., Carlini, N., Li, B., Raj, H., Bercovich, I., Shi, L., Shin,

J.Y., Walshe, T., Buchanan, E.K., Shen, J., Ye, G., Lin, H., Poulos, J., Wang, M.,

Nezhurina, M., Jitsev, J., Lu, D., Mastromichalakis, O.M., Xu, Z., Chen, Z., Liu,

Y., Zhang, R., Chen, L.L., Kashyap, A., Uslu, J.L., Li, J., Wu, J., Yan, M., Bian,

S., Sharma, V., Sun, K., Dillmann, S., Anand, A., Lanpouthakoun, A., Koopah, B.,

Hu, C., Guha, E., Dreiman, G.H.S., Zhu, J., Krauth, K., Zhong, L., Muennighoff,

N., Amanfu, R., Tan, S., Pimpalgaonkar, S., Aggarwal, T., Lin, X., Lan, X., Zhao,

X., Liang, Y., Wang, Y., Wang, Z., Zhou, C., Heineman, D., Liu, H., Trivedi, H.,

Yang, J., Lin, J., Shetty, M., Yang, M., Omi, N., Raoof, N., Li, S., Zhuo, T.Y.,

Lin, W., Dai, Y., Wang, Y., Chai, W., Zhou, S., Wahdany, D., She, Z., Hu, J.,

Dong, Z., Zhu, Y., Cui, S., Saiyed, A., Kolbeinsson, A., Hu, J., Rytting, C.M.,

Marten, R., Wang, Y., Dimakis, A., Konwinski, A., Schmidt, L.: Terminal-bench:

Benchmarking agents on hard, realistic tasks in command line interfaces (2026),

https://arxiv.org/abs/2601.11868

12. Mitra, S., Bazarov, A., Duclos, M., Mittal, S., Piplai, A., Rahman, M.R., Zieglar,

E., Rahimi, S.: Falcon: Autonomous cyber threat intelligence mining with llms for

ids rule generation. arXiv preprint arXiv:2508.18684 (2025)

13. Newsome, J., Karp, B., Song, D.: Polygraph: Automatically generating signa-

tures for polymorphic worms. In: 2005 IEEE Symposium on Security and Privacy

(S&P’05). pp. 226–241. IEEE (2005)

14. Schwartz, Y., Ben-Shimol, L., Mimran, D., Elovici, Y., Shabtai, A.: Llmcloud-

hunter: Harnessing llms for automated extraction of detection rules from cloud-

based cti. In: Proceedings of the ACM on Web Conference 2025. pp. 1922–1941

(2025)

15. Stevens, K., Erdemir, M., Zhang, H., Kim, T., Pearce, P.: Blueprint: Automatic

malware signature generation for internet scanning. In: Proceedings of the 27th

International Symposium on Research in Attacks, Intrusions and Defenses. pp.

197–214 (2024)

16. Tan, H.C., Cheh, C., Chen, B.: Cotoru: automatic generation of network intru-

sion detection rules from code. In: IEEE INFOCOM 2022-IEEE Conference on

Computer Communications. pp. 720–729. IEEE (2022)

17. Uetz, R., Herzog, M., Hackländer, L., Schwarz, S., Henze, M.: You cannot escape

me: Detecting evasions of { SIEM } rules in enterprise networks. In: 33rd USENIX

Security Symposium (USENIX Security 24). pp. 5179–5196 (2024)

18. Xu, M., Wang, H., Liu, J., Li, X., Yu, Z., Han, W., Lim, H.W., Dong, J.S., Zhang,

J.: Threatpilot: Attack-driven threat intelligence extraction (2025), https://arxi

v.org/abs/2412.10872

19. Zhang, X., Du, X., Chen, H., He, Y., Niu, W., Li, Q.: Automatically generating

rules of malicious software packages via large language model. In: 2025 55th An-

nual IEEE/IFIP International Conference on Dependable Systems and Networks

(DSN). pp. 734–747. IEEE (2025)

20. Zhang, Y., Li, M., Long, D., Zhang, X., Lin, H., Yang, B., Xie, P., Yang, A., Liu,

D., Lin, J., Huang, F., Zhou, J.: Qwen3 embedding: Advancing text embedding

and reranking through foundation models. arXiv preprint arXiv:2506.05176 (2025)

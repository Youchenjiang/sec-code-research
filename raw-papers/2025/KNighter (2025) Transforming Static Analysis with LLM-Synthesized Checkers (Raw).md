---
title: "KNighter: Transforming Static Analysis with LLM-Synthesized Checkers"
author: "Chenyuan Yang; Zijie Zhao; Zichen Xie; Haoyu Li; Lingming Zhang"
creator: "arXiv GenPDF (tex2pdf:)"
pages: 15
---

# KNighter: Transforming Static Analysis with LLM-Synthesized Checkers

> **作者**：Chenyuan Yang; Zijie Zhao; Zichen Xie; Haoyu Li; Lingming Zhang
> **總頁數**：15 頁

---

## Page 1

KNighter: Transforming Static Analysis with

LLM-Synthesized Checkers

| Chenyuan Yang | Zijie Zhao | Zichen Xie |
| --- | --- | --- |
| University of Illinois | University of Illinois | Zhejiang University |
| Urbana-Champaign | Urbana-Champaign | China |
| USA | USA | xiezichen@zju.edu.cn |
| cy54@illinois.edu | zijie4@illinois.edu |  |
| Haoyu Li | Lingming Zhang |  |
| Shanghai Jiao Tong University | University of Illinois |  |
| China | Urbana-Champaign |  |
| learjet@sjtu.edu.cn | USA |  |

critical systems like operating system kernels. However, de-

signing and implementing static analyzers is challenging,

time-consuming, and typically limited to predefined bug

patterns. While large language models (LLMs) have shown

static analyzers from historical bug patterns. Rather than

using LLMs to directly analyze massive systems, our key

insight is leveraging LLMs to generate specialized static ana-

lyzers guided by historical patch knowledge. KNighter im-

plements this vision through a multi-stage synthesis pipeline

that validates checker correctness against original patches

and employs an automated refinement process to iteratively

reduce false positives. Our evaluation on the Linux kernel

demonstrates that KNighter generates high-precision check-

ers capable of detecting diverse bug patterns overlooked

by existing human-written analyzers. To date, KNighter-

synthesized checkers have discovered 92 new, critical, long-

latent bugs (average 4.3 years) in the Linux kernel; 77 are

confirmed, 57 fixed, and 30 have been assigned CVE num-

bers. This work establishes an entirely new paradigm for

scalable, reliable, and traceable LLM-based static analysis for

real-world systems via checker synthesis.

tional License.

SOSP ’25, Seoul, Republic of Korea

lingming@illinois.edu

analysis .

Keywords: Static Analysis, Large Language Models

ACM Reference Format:

3731569.3764827

1 Introduction

The reliability of fundamental software systems—particularly

operating system (OS) kernels—hinges on robust defect detec-

tion methodologies [10, 18, 19, 21, 36, 39, 45, 52, 55]. Among

various techniques, static analysis [7] stands out for its ability

to examine source code without execution, making it indis-

pensable for scenarios involving hardware-dependent dri-

vers, complex or rarely exercised paths, and configurations

difficult to reproduce in real environments [18, 19, 21, 35,

36, 45]. Compared to dynamic approaches such as fuzzing—

actual runtime paths [3, 13, 53, 55]—static analysis can (in

principle) cover all potential execution paths, including cor-

ner cases that are seldom triggered in practice. While formal

verification techniques [25, 43, 54] offer stronger correct-

ness guarantees, their high manual overhead renders them

impractical for large-scale systems like OS kernels, making

static analysis a more scalable and feasible solution.

The static analysis problem. Large-scale systems present

patterns and managing enormous codebases, as illustrated

1

| Abstract | CCS Concepts: | • | Security and privacy | → | Systems secu- |
| --- | --- | --- | --- | --- | --- |
| Static analysis is a powerful technique for bug detection in | rity | ; • | Software and its engineering | → | Automated static |
| promise for static analysis, directly applying them to scan | Chenyuan Yang, Zijie Zhao, Zichen Xie, Haoyu Li, and Lingming |  |  |  |  |
| large systems remains impractical due to computational con- | Zhang. 2025. KNighter: Transforming Static Analysis with LLM- |  |  |  |  |
| straints and contextual limitations. | Synthesized Checkers. In | ACM SIGOPS 31st Symposium on Operating |  |  |  |
| We present KNighter, the first approach that unlocks scal- | Systems Principles (SOSP ’25), October 13–16, 2025, Seoul, Republic of |  |  |  |  |
| able LLM-based static analysis by automatically synthesizing | Korea. | ACM, New York, NY, USA, 15 pages. | https://doi.org/10.1145/ |  |  |

arXiv:2503.09002v3 [cs.SE] 3 Sep 2025 which requires an execution environment and thus only tests

| This work is licensed under a Creative Commons Attribution 4.0 Interna- | a dual challenge for static analysis: addressing diverse bug |  |  |
| --- | --- | --- | --- |
| © 2025 Copyright held by the owner/author(s). | in Figure 1. An ideal static analyzer should | (i) | detect a wide |
| ACM ISBN 979-8-4007-1870-0/2025/10 | range of defects—including those related to nuanced, system- |  |  |
| https://doi.org/10.1145/3731569.3764827 | specific semantics—and | (ii) | efficiently process millions of |

---

## Page 2

SOSP ’25, October 13–16, 2025, Seoul, Republic of Korea Chenyuan Yang, Zijie Zhao, Zichen Xie, Haoyu Li, and Lingming Zhang

Human Checker

Traditional Static Analysis

| Learning | Scan |
| --- | --- |
| Automated | Checker |

LLM-Synthesized Checkers

Figure 1. Motivation. Static analysis should scale to ad-

dress a diverse range of bug patterns and handle massive

codebases. Traditional static analysis struggles with covering

wide-ranging bugs, whereas LLM-based methods face hurdles

in scaling to large codebases.

tire codebase. In this paradigm, LLMs learn bug patterns

2

dedicated static analysis checkers. This method circumvents

ning vast codebases while maintaining the flexibility needed

to address a wide spectrum of bugs. Moreover, by validat-

erating complete static analysis logic remains a formidable

challenge—even experts struggle with it. To address this, we

introduce a multi-stage synthesis pipeline (§ 3.1) that decom-

poses checker generation into manageable subtasks. Further-

more, to enhance the quality of the synthesized checkers by

reducing false positives, we develop a fully automated refine-

ment pipeline (§ 3.2) that leverages bug report triage agents.

Together, these pipelines yield checkers that are robust and

practical for deployment in real-world scenarios.

| Learning | Design | the prohibitive costs and context-length limitations of scan- |  |
| --- | --- | --- | --- |
| Automated | Direct | ing each synthesized checker against the original patches, |  |
| Various | Large | we mitigate hallucinations and produce transparent, human- |  |
| Bug | Emerging LLM-Based Static Analysis | Codebase | readable logic that developers can trust and maintain. |
| Patterns | Scan | Technical challenges and our solutions. | Although au- |
| Learning | Design | tomated checker synthesis holds significant promise, gen- |  |
| lines of code. However, existing techniques typically com- | We implement our approach in a tool, KNighter, the first |  |  |
| promise on one of these critical objectives. | fully automated pipeline for synthesizing static analyzers, |  |  |
| Traditional static analysis. | Traditional static analyzers are | built upon the open-source Clang Static Analyzer (CSA) [12]. |  |
| effective in identifying certain bug types, yet they fundamen- | While the methodology generalizes to different systems, we |  |  |
| tally rely on pre-defined, rule-based, or formally modeled | target the Linux kernel, one of the most fundamental soft- |  |  |
| checks. This reliance necessitates extensive domain exper- | ware systems. In the evaluation of 61 diverse bug-fix patches, |  |  |
| tise and substantial engineering effort for their development | KNighter synthesized the high-quality checkers for 61% of |  |  |
| and maintenance [2, 10, 21]. Consequently, these tools are | them, achieving a false positive rate of about 35% aided by the |  |  |
| often fine-tuned to a narrow subset of bug patterns, which | triage agent. Demonstrating practical impact, KNighter has |  |  |
| not only limits their ability to detect unforeseen defects but | uncovered 92 new, long-latent vulnerabilities (average 4.3 |  |  |
| also hampers their scalability in automatically addressing a | years) in the Linux kernel, resulting in 77 developer confirma- |  |  |
| broader spectrum of issues. | tions, 57 fixes, and 30 CVEs. Furthermore, the vulnerabilities |  |  |
| Emerging LLM-based static analysis. | On the other hand, | detected are orthogonal to those found by existing expert- |  |
| Large Language Models (LLMs) are compelling tools for dis- | written analyzers [2]. These findings validate our approach’s |  |  |
| covering bug patterns in part because they can learn directly | efficacy and its contribution to system reliability. |  |  |
| from historical patch commits—a treasure trove of real fixes | Our main contributions are summarized as follows: |  |  |
| and associated bug contexts [11, 21, 31]. Their ability to parse | • | Novelty. | We introduce a pioneering approach for syn- |
| both textual and code content [5, 20, 46] suggests that LLMs | thesizing static analyzers from patch commits. To our |  |  |
| can adapt to new bug types without explicit rule-crafting. | knowledge, KNighter is the first fully automated static |  |  |
| However, directly deploying LLMs on large-scale systems | analyzer generation system, establishing a new para- |  |  |
| (e.g., the Linux kernel at over 30 million lines of code) con- | digm for LLM-based static analysis. |  |  |
| fronts severe limitations. Their bounded context windows | • | Approach. | We implement KNighter with multi-stage |
| make it impossible to upload all relevant source code at once, | synthesis and automated refinement pipelines for the |  |  |
| and doing so repeatedly would also incur prohibitive compu- | Linux kernel. This design enables detection of diverse |  |  |
| tational costs (potentially hundreds of dollars per thorough | bug classes in large-scale systems. |  |  |
| scan). In addition, LLMs can hallucinate [14, 22, 30], produc- | • | Evaluation. | We demonstrate that KNighter success- |
| ing plausible but incorrect outputs, especially when faced | fully synthesizes effective checkers from the Linux |  |  |
| with the intricacies of large-scale systems [37]. | kernel bug-fix patches across various bug categories, |  |  |
| Insight. | Can we scale and automate static analysis to han- | achieving practical false positive rates. |  |
| dle both diverse bug patterns and enormous codebases? We | • | Real-world impact. | KNighter-generated checkers |
| answer this question by harnessing the strengths of tradi- | have discovered 92 new, long-latent (average 4.3 years) |  |  |
| tional static analysis alongside emerging LLMs. More specif- | bugs in the Linux kernel, with 77 confirmed, 57 fixed, |  |  |
| ically, we propose | synthesizing static checkers | using LLMs | and 30 assigned CVE numbers—demonstrating its prac- |
| rather than applying LLM-based analysis directly to the en- | tical impact on system reliability and security. |  |  |
| from historical patches, and these insights are encoded into | KNighter is available at ise-uiuc/KNighter. |  |  |

---

## Page 3

| KNighter: Transforming Static Analysis with LLM-Synthesized Checkers | SOSP ’25, October 13–16, 2025, Seoul, Republic of Korea |
| --- | --- |
| --- a/drivers/spi/spi-pci1xxxx.c | state meticulously maps program expressions to symbolic |

+++ b/drivers/spi/spi-pci1xxxx.c

+ if (!spi_bus->spi_int[iter])

spi_sub_ptr->spi_host = devm_spi_alloc_host(...)

int asoc_qcom_lpass_cpu_platform_probe(...)

+ if (!drvdata)

drvdata ->variant = variant; Without NULL checking

if (!ExprHasName(OriginExpr, " devm_kzalloc ", C))

}

void checkBranchCondition (...) const {

if (UO->getOpcode() == UO_LNot) {

}

...

...

// If the region is recorded as unchecked, warn.

}

// For pointer assignments, update the aliasing map.

(c) A checker synthesized by KNighter for the patch in Fig. 2a.

Figure 2. A bug pattern related to devm_kzalloc .

2 Background and Motivation

3

driven manner, registering interest in specific analysis events

of checkers is their ability to extend the ProgramState with

implementing callback methods corresponding to the rele-

vant analysis events, registering the new checker with the

• The checkPostCall callback activates after function

volved in the assignment, ensuring the checker cor-

rectly handles cases where multiple pointers might

refer to the same potentially null memory.

2.2 Motivating Example

We demonstrate KNighter’s effectiveness through a case

| @@ -275,6 +275,8 @@ static int pci1xxxx_spi_probe | values and tracks the contents of memory locations. |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| spi_bus->spi_int[iter] = | devm_kzalloc | (&pdev->dev, ...); | The modularity of CSA is built upon checkers. These are |  |  |  |  |
| + | return -ENOMEM; | small, specialized components, typically implemented as sub- |  |  |  |  |  |
| spi_sub_ptr = spi_bus->spi_int[iter]; | classes of a | Checker | template. Checkers function in an event- |  |  |  |  |
| (a) | Patch for a Null-Pointer-Dereference bug. The pointer re- | such as pre- and post-function calls, the identification of dead |  |  |  |  |  |
| turned by | devm_kzalloc | should be checked. | symbols, or instances of pointer escapes. A key capability |  |  |  |  |
| { | custom, checker-specific data using provided macros, allow- |  |  |  |  |  |  |
| drvdata | = | devm_kzalloc | (dev, ...); | ing them to maintain sophisticated state across the analysis. |  |  |  |
| + | return -ENOMEM; | Patch | Developing a new checker for CSA generally involves sev- |  |  |  |  |
| ... | eral steps: defining the specific bug pattern to be detected, |  |  |  |  |  |  |
| (b) | A new bug detected by KNighter with | CVE-2024-50103 | . | analysis framework, and integrating it into the testing sys- |  |  |  |
| void | checkPostCall | (...) const { | tem. Effective bug reporting is crucial, utilizing mechanisms |  |  |  |  |
| ... | like | BugType | and | BugReport | to provide clear diagnostics. |  |  |
| return; | To illustrate, consider the example checker shown in Fig- |  |  |  |  |  |  |
| State = State->set<PossibleNullPtrMap>(MR, false); | ure 2c, which registers four distinct callback functions. |  |  |  |  |  |  |
| // Pattern 1: if (!ptr) | calls. It uses | ExprHasName | to check if the call was to |  |  |  |  |
| if (const UnaryOperator *UO = | devm_kzalloc | . If so, it updates the custom state map |  |  |  |  |  |
| dyn_cast<UnaryOperator>(CondExpr)) { | PossibleNullPtrMap | to mark the returned memory re- |  |  |  |  |  |
| ... | gion as potentially null (unchecked). |  |  |  |  |  |  |
| State = markRegionChecked(State, MR); | • | The | checkBranchCondition | callback is used to handle |  |  |  |
| } | conditional checks involving the pointer. It recognizes |  |  |  |  |  |  |
| // Pattern 2: if (ptr == NULL) or if (ptr != NULL) | patterns like negation ( | if (!ptr) | ) or direct compar- |  |  |  |  |
| } | ison ( | if | (ptr | == | NULL) | ) and updates the state via |  |
| void | checkLocation | (...) const { | markRegionChecked | to reflect that a null check has oc- |  |  |  |
| // Look up the region in the PossibleNullPtrMap. | curred for the associated memory region. |  |  |  |  |  |  |
| const bool *Checked = State->get<PossibleNullPtrMap>(MR); | • | The | checkLocation | callback is triggered when a mem- |  |  |  |
| if (Checked && *Checked == false) | ory location is accessed. More specifically, it consults |  |  |  |  |  |  |
| reportUncheckedDereference | (MR, S, C); | the | PossibleNullPtrMap | state; if the region is marked |  |  |  |
| void | checkBind | (...) const { | as unchecked at this point, it issues a warning using |  |  |  |  |
| ... | reportUncheckedDereference | . |  |  |  |  |  |
| State = State->set<PtrAliasMap>(LHSReg, RHSReg); | • | The | checkBind | callback manages pointer assignments. |  |  |  |
| State = State->set<PtrAliasMap>(RHSReg, LHSReg); | It updates another custom state map, | PtrAliasMap | , to |  |  |  |  |
| } | track potential aliases between memory regions in- |  |  |  |  |  |  |
| 2.1 | Clang Static Analyzer | study involving a Null-Pointer-Dereference vulnerability |  |  |  |  |  |
| Static analysis [7] is a technique for detecting bugs by in- | pattern. Figure 2a shows a historical patch addressing this |  |  |  |  |  |  |
| specting code without executing it. The Clang Static Ana- | pattern, where the original bug stemmed from a missing null |  |  |  |  |  |  |
| lyzer [12] (CSA) serves as a powerful engine for this purpose. | pointer check after a | devm_kzalloc | call. Without this check, |  |  |  |  |
| It operates using path-sensitive symbolic execution, build- | the system could crash if memory allocation failed and the |  |  |  |  |  |  |
| ing an internal representation called an | ExplodedGraph | . Each | returned null pointer was subsequently dereferenced. |  |  |  |  |
| node within this graph, an | ExplodedNode | , represents a spe- | Limitations of existing tools. | Despite this vulnerability |  |  |  |
| cific | ProgramPoint | paired with an abstract | ProgramState | . This | pattern recurring since at least 2017 (commit | 49af64e | ), with |

*[Image: Page 3 Image]*

---

## Page 4

SOSP ’25, October 13–16, 2025, Seoul, Republic of Korea Chenyuan Yang, Zijie Zhao, Zichen Xie, Haoyu Li, and Lingming Zhang

Input Patch The bug pattern is the

failure to check the

| A potential null pointer | return value of |
| --- | --- |
| that may be caused by a | `devm_kzalloc()` for |
| by the function devm_kzalloc | dereferencing it. |

🤖 Pattern Analysis

+ if (!spi_bus->spi_int)

+ return -ENOMEM

spi_bus->spi_int = devm_xx

spi_bus->spi_int[0] = .. +

⚒ Checker Validation

void checkPostCall(...);

⚒ Codebase Scan

🦉 Plausible Checkers

Figure 3.

systematically detect these issues. Even specialized kernel

checkers like Smatch [2] fail to identify these vulnerabili-

ties because they lack the domain-specific knowledge that

LLM hallucination can produce incorrect analyzers. KNighter

mitigates this by validating synthesized checkers against his-

torical patches, verifying they correctly distinguish between

4

## Plan

| 1. Program State Management | void checkPostCall(...); |
| --- | --- |
| 2. Callback Functions | void |

checkBranchCondition(...);

- `checkPostCall`: Track

void checkBind(...);

- ...

🤖 Plan Synthesis 🤖 Checker Generation

spi_bus->spi_int = devm_xx

+ if (!spi_bus->spi_int) Syntax Error:

return -ENOMEM

spi_bus->spi_int[0] = .. ‘Optional’ was not

🤖 Checker Repair

🤖 Report Triage 🤖 Checker Refinement

Overview of KNighter.

3 Design

1

sible” patch passes all test cases and potentially is the correct fix.

| failed memory allocation | NULL before | Memory Allocations | void checkLocation(...); |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| drivers/spi/spi-pci1xxxx.o | declared in this scope |  |  |  |  |  |
| void | void checkPostCall(...); |  |  |  |  |  |
| checkBranchCondition(...); | - Decision: {Bug/NotABug} | void checkBranchCondition(...); |  |  |  |  |
| void checkLocation(...); | - Reason: {...} | void checkLocation(...); |  |  |  |  |
| void checkBind(...); | void checkBind(...); |  |  |  |  |  |
| our analysis identifying at least six historical patches ad- | we implement a bug triage agent that identifies false alarms, |  |  |  |  |  |
| dressing it, no static analysis tool had been developed to | enabling iterative refinement of the checkers. |  |  |  |  |  |
| devm_kzalloc | may return | NULL | upon failure. | Terminology. | KNighter takes a patch commit as input and |  |
| Our approach. | KNighter extracts critical insights from the | outputs a corresponding CSA checker. | Valid checkers | cor- |  |  |
| patch: unchecked return values from | devm_kzalloc | repre- | rectly distinguish between buggy and patched code, flagging |  |  |  |
| sent potential Null-Pointer-Dereference vulnerabilities. The | pre-patch code as defective while recognizing post-patch |  |  |  |  |  |
| synthesized checker (written in CSA, Figure 2c) tracks null- | code as correct. | Plausible checkers | 1 | are | valid checkers | that |
| check status across execution paths while correctly handling | additionally demonstrate practical utility through low false |  |  |  |  |  |
| pointer aliasing, a sophisticated static analysis capability. | positive rates or a manageable number of reports. We provide |  |  |  |  |  |
| This checker discovered 3 | new | vulnerabilities in the Linux | formal definitions of these terms in § 4. |  |  |  |
| kernel. Figure 2b presents one such vulnerability exhibiting | Overview. | KNighter leverages agentic workflow to process |  |  |  |  |
| the same pattern where a null pointer check is missing for | patch commits for static analyzer synthesis, as illustrated in |  |  |  |  |  |
| the pointer returned by the | devm_kzalloc | call. This bug was | Figure 3. It operates in two phases: checker synthesis (§ 3.1) |  |  |  |
| subsequently fixed and assigned CVE-2024-50103. | and checker refinement (§ 3.2). In the checker synthesis |  |  |  |  |  |
| Advantages over direct LLM scanning. | Directly using | phase, KNighter analyzes the input patch to identify bug |  |  |  |  |
| LLMs to scan the Linux kernel would be prohibitively ex- | patterns (§ 3.1.1), synthesizes a detection plan (§ 3.1.2), and |  |  |  |  |  |
| pensive, as | devm_kzalloc | alone appears over 7K times across | implements a checker using CSA (§ 3.1.3). If compilation |  |  |  |
| 5.4K files. In contrast, KNighter’s static analyzers primarily | errors occur, a syntax-repair agent automatically repairs |  |  |  |  |  |
| consume CPU resources rather than repeated LLM invoca- | them based on the error messages. This phase concludes with |  |  |  |  |  |
| tions, making the approach both scalable and cost-effective. | the generation of | valid checkers | (§ 3.1.4). In the subsequent |  |  |  |
| Moreover, since generating the checkers is mostly a one-time | checker refinement phase, these valid checkers are deployed |  |  |  |  |  |
| effort, they can naturally evolve alongside the system. | to scan the entire codebase for potential bugs. When bug |  |  |  |  |  |
| Technical challenges and solutions. | Creating effective | reports are generated, a triage agent evaluates them for false |  |  |  |  |
| static analyzers with LLMs presents several challenges. First, | positives, and KNighter refines the checker accordingly. If the |  |  |  |  |  |
| writing robust checkers end-to-end is complex. KNighter | scan produces a manageable number of reports with a low |  |  |  |  |  |
| addresses this through a multi-stage synthesis pipeline that | false positive rate, KNighter presents the | plausible checkers |  |  |  |  |
| breaks down complex tasks into manageable steps. Second, | and their filtered reports as potential bugs for review. |  |  |  |  |  |
| buggy and patched code. Finally, to reduce false positives, | We adopt the term “plausible” from program repair [40, 49], where a “plau- |  |  |  |  |  |

---

## Page 5

KNighter: Transforming Static Analysis with LLM-Synthesized Checkers SOSP ’25, October 13–16, 2025, Seoul, Republic of Korea

spi: mchp-pci1xxx: Fix a possible null pointer dereference in Algorithm 1: Synthesize checkers with input patch.

pci1xxx_spi_probe

pointer that may be caused by a failed memory allocation

later in the code.

To fix this issue, spi_bus->spi_int[iter] should be checked.

the plan based on the patch and the identified bug pattern

( Line 7 ). With the plan in hand, KNighter implements the

checker using CSA ( Line 9 ). If any compilation issues arise,

a syntax-repair agent is invoked to debug and repair them

( Line 12 ). The repair process is allowed up to maxAttempts

(default is 5) attempts. If the checker compiles successfully,

KNighter validates it by checking whether it can distinguish

between the buggy and patched code ( Line 18 ). Once the

checker is deemed valid, it is returned for the next phase

( Line 20 ). Otherwise, the synthesis pipeline continues iter-

While bug patterns are sometimes explicitly described in

5

1 Function GenChecker( patch ) :

| 5 | pattern | ← | AnalyzePatch( | patch | ) |
| --- | --- | --- | --- | --- | --- |
| 8 | # Stage 3: Analyzer Implementation and Repair |  |  |  |  |
| 10 | attempts | ← | 0 |  |  |
| 11 | while | hasCompilationErrors(checker) and attempts |  |  |  |

< maxAttempts do

| 16 | Continue |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 17 | # Stage 4: Validation |  |  |  |  |
| 18 | isValid | ← | ValidateChecker( | checker, patch | ) |
| 19 | if | isValid | then |  |  |
| 20 | return | checker |  |  |  |
| 21 | return | Null |  |  |  |

proach favors more targeted bug patterns derived from the

| In function pci1xxxx_spi_probe, there is a potential null | 2 | # Iterative checker generation and evaluation |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| by the function devm_kzalloc. Hence, a null pointer check | 3 | for | i = 1 | to | maxIterations | do |  |
| needs to be added to prevent null pointer dereferencing | 4 | # Stage 1: Bug Pattern Analysis |  |  |  |  |  |
| The memory allocated by devm_kzalloc will be automatically | 6 | # Stage 2: Detection Plan Synthesis |  |  |  |  |  |
| released, so just directly return -ENOMEM. | 7 | plan | ← | SynthesizePlan( | patch, pattern | ) |  |
| Figure 4. | Patch commit message. | 9 | checker | ← | Implement( | patch, pattern, plan | ) |
| 3.1 | Checker Synthesis | 12 | checker | ← | RepairChecker( | checker | ) |
| Algorithm 1 presents the multi-stage pipeline of checker syn- | 13 | attempts | ← | attempts + 1 |  |  |  |
| thesis. In the first stage, KNighter analyzes the bug pattern | 14 | if | hasCompilationErrors(checker) | then |  |  |  |
| shown in the patch ( | Line | 5 | ). Next, KNighter synthesizes | 15 | # Skip evaluation if checker still has errors |  |  |
| ating until reaching | maxIterations | . If all iterations fail, the | comprehensive, but identifying all relevant functions/con- |  |  |  |  |
| process returns Null, indicating that a valid checker could | ditions poses significant static analysis challenges, hinder- |  |  |  |  |  |  |
| not be synthesized ( | Line 21 | ). | ing robust implementation by LLMs. Consequently, our ap- |  |  |  |  |
| 3.1.1 | Bug Pattern Analysis. | The initial stage involves | patch context. These facilitate precise and tractable checker |  |  |  |  |
| analyzing patch commits to identify underlying bug patterns. | synthesis by the LLMs. For the | devm_kzalloc | example, focus- |  |  |  |  |
| Patch commits typically consist of | diff | patches and may | ing specifically on its return value yields a targeted pattern |  |  |  |  |
| include developer comments describing the bug being fixed, | that effectively addresses the observed bug class while being |  |  |  |  |  |  |
| as illustrated in Figure 4. Our goal is to extract patterns that | significantly more manageable for the LLM to implement |  |  |  |  |  |  |
| can be translated into static analysis rules for bug detection. | correctly compared to the broader, more complex alternative. |  |  |  |  |  |  |
| commit messages, they often require deeper analysis of the | 3.1.2 | Plan Synthesis. | Once the bug pattern is identified, |  |  |  |  |
| code changes within the patch. | KNighter generates a high-level plan for implementing the |  |  |  |  |  |  |
| We have developed an LLM-based agent specifically de- | static analyzer. This plan serves two critical purposes: first, it |  |  |  |  |  |  |
| signed to perform this pattern analysis, with the prompt | provides structured guidance to the LLMs during implemen- |  |  |  |  |  |  |
| template shown in Figure 5a. In addition to the patch, we ex- | tation, preventing confusion and promoting effective execu- |  |  |  |  |  |  |
| tract the complete function code that was modified from the | tion. Second, it facilitates debugging of the entire pipeline |  |  |  |  |  |  |
| kernel codebase. This additional context is crucial because | by making the LLMs’ reasoning process transparent and |  |  |  |  |  |  |
| the patch | diff | alone may not capture all relevant buggy pat- | traceable. Our ablation study in § 5.4.2 confirms the value of |  |  |  |  |
| terns, as some issues depend on the broader context of the | this plan synthesis, demonstrating improved performance |  |  |  |  |  |  |
| code. By providing both the patch and the complete function | consistent with findings in other domains [44]. |  |  |  |  |  |  |
| code to LLMs, we enable a more comprehensive understand- | For instance, synthesizing a checker for the unchecked |  |  |  |  |  |  |
| ing of the bug being patched. | devm_kzalloc | return value pattern (illustrated in Figure 2c) |  |  |  |  |  |
| A single bug pattern identified from a patch can be ex- | might generate a plan with key steps such as: (1) Using |  |  |  |  |  |  |
| pressed with varying scope and complexity. Consider the | program state to track memory regions from | devm_kzalloc | , |  |  |  |  |
| Null-Pointer-Dereference involving | devm_kzalloc | (Figure 2a). | (2) monitoring conditional branches ( | checkBranchCondition | ) |  |  |
| A | broad | pattern (e.g., check | any | potentially null return) is | to mark regions as checked if a null check occurs, and (3) |  |  |

---

## Page 6

| SOSP ’25, October 13–16, 2025, Seoul, Republic of Korea | Chenyuan Yang, Zijie Zhao, Zichen Xie, Haoyu Li, and Lingming Zhang |  |  |
| --- | --- | --- | --- |
| # Instruction | {{ | Customize Program States | }} // If necessary |
| You will be provided with a patch in Linux kernel. | namespace { |  |  |
| Please analyze the patch and find out the **bug pattern** in | class NewChecker : public Checker<{{Callback Functions}}> { |  |  |
| this patch. | mutable std::unique_ptr<BugType> BT; |  |  |
| A **bug pattern** is the root cause of this bug, meaning that | public: |  |  |
| programs with this pattern will have a great possibility of | NewChecker() : BT(new BugType(this, "{{Bug desc}}")) {} |  |  |
| having the same bug. | {{ | Declaration of Callback Functions | }} |
| Note that the bug pattern should be specific and accurate, | private: |  |  |
| which can be used to identify the buggy code provided in the | {{ | Declaration of Self-Defined Functions | }} |
| patch. | }; |  |  |
| # Examples | {{ | Self-Defined Functions (should be complete and runnable) | }} |
| ... | Commit message | } |  |

| # Target Patch | Buggy code |
| --- | --- |
| {{input_patch}} | Diff patch |

(a) Prompt template for bug pattern analysis

# Instruction

# Utility Functions

...

# Target Pattern

# Instruction

- Compare the report against the target bug pattern, using the

- Explain your reasoning for classifying this as either:

- FP (does not match the target pattern or not a real bug).

# Target Pattern

{{input_report}}

detecting uses ( checkLocation ) of unchecked regions, poten-

tially signaling a bug. This high-level structure guides the

subsequent implementation phase.

To synthesize the implementation plan for the checker, we

have designed an LLM-based agent whose prompt template

is shown in Figure 5b. This agent takes the previously sum-

marized bug pattern as input. Additionally, we maintain a

curated database of utility functions for checker implementa-

tion that can be easily extended. By including the signatures

and brief descriptions of these utility functions in the prompt,

we enable LLMs to leverage them effectively during the plan-

ning process, simplifying the overall task.

6

Figure 6. Pre-defined checker template for CSA.

types. To handle the potential compilation errors, we employ

program repair [50], this agent automatically processes com-

ferential analysis verifies that a checker correctly identifies

after the patch. For efficiency, we scope this validation to

rather than the entire codebase. A checker is considered

valid if it flags the bug in the pre-patch version and shows

a corresponding reduction or elimination of that specific

warning in the patched version. More details are in § 4.

3.2 Checker Refinement

Following synthesis, each valid checker is used to scan the

entire system. However, its initial validation doesn’t prevent

potential false positives when analyzing the broader code-

base, where correct code might be flagged erroneously. To

mitigate this, we implement an iterative refinement proce-

dure driven by LLMs. This involves evaluating the generated

bug reports and feeding identified false positives back to

refine the checker.

| Please organize a | elaborate plan | to help to write a CSA | pattern and a structured implementation plan. We also pro- |
| --- | --- | --- | --- |
| checker to detect such **bug pattern**. | vide a pre-defined checker template, as shown in Figure 6, |  |  |
| ... | which standardizes the implementation structure and re- |  |  |
| # Examples | duces potential errors. Moreover, we provide a list of utility |  |  |
| # Target Patch | functions that could help with the implementation. |  |  |
| {{input_patch}} | The synthesized checkers could have compilation errors, |  |  |
| {{input_pattern}} | e.g., | using the wrong static analysis API or incorrect variable |  |
| (b) | Prompt template for plan synthesis. | a dedicated debugging agent. Inspired by existing work on |  |
| Determine whether the static analyzer report is a | real bug | in | piler error messages and applies necessary fixes, effectively |
| the Linux kernel and | matches the target bug pattern | . | addressing syntax errors that may arise from LLM hallucina- |
| buggy function (pre-patch) and the fix patch as the reference. | tions. This automated debugging pipeline ensures that the |  |  |
| - TP (matches the target bug pattern and is a real bug), or | final checkers are both syntactically correct and compilable. |  |  |
| # Patch | 3.1.4 | Validation. | To semantically validate our checkers |
| {{input_patch}} | and mitigate potential inaccuracies from LLMs, we evalu- |  |  |
| {{input_pattern}} | ate them against both the buggy (pre-patch) and patched |  |  |
| # Report | versions of the relevant code (e.g., Linux kernel files). This dif- |  |  |
| (c) | Prompt template for report triage. | the target bug in the original code and confirms its absence |  |
| Figure 5. | Simplified prompt templates used by KNighter. | only the files modified by the patch and their dependencies, |  |
| 3.1.3 | Analyzer Implementation and Syntax Repair. | However, automating this refinement faces hurdles. First, |  |
| After identifying the bug pattern and making the plan, we | bug reports are often verbose, containing extensive context |  |  |
| leverage an LLM-based agent to implement the correspond- | that is difficult to process efficiently. Second, debugging the |  |  |
| ing checker. To maximize implementation accuracy, we pro- | checker logic and modifying it correctly based on false posi- |  |  |
| vide the agent with comprehensive inputs: the distilled bug | tives requires complex analysis. |  |  |

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

---

## Page 7

| KNighter: Transforming Static Analysis with LLM-Synthesized Checkers | SOSP ’25, October 13–16, 2025, Seoul, Republic of Korea |  |  |  |
| --- | --- | --- | --- | --- |
| int sh_pfc_register_pinctrl(struct sh_pfc *pfc) { | Table 1. | Distribution of | patch commits | across 10 bug cate- |
| struct sh_pfc_pinctrl *pmx; | gories and the validity status of their synthesized checkers. |  |  |  |

int ret;

if (unlikely(!pmx)) FP by triage agent

return -ENOMEM;

pmx->pfc = pfc; Reported by checker

...

the “relevant lines” highlighted by the static analyzer ( e.g.,

CSA [12]) and the corresponding trace path—stripping extra-

neous context while preserving critical diagnostics. Second,

employ specialized LLM-based agents. A triage agent classi-

fies each distilled report, focusing strictly on alignment with

the target bug pattern (rather than general code correctness);

the prompt template is shown in Figure 5c.

7

cates “Use-Before-Initialization”.

Valid

| NPD | 6 | 1 | 2 | 2 | 1 |
| --- | --- | --- | --- | --- | --- |
| Integer-Overflow | 7 | 3 | 1 | 3 | 0 |
| Use-After-Free | 7 | 4 | 2 | 1 | 0 |
| Double-Free | 8 | 1 | 5 | 1 | 1 |
| UBI | 5 | 1 | 1 | 3 | 0 |
| Concurrency | 5 | 2 | 3 | 0 | 0 |
| Total | 61 | 22 | 26 | 11 | 2 |

first identify buggy objects by examining the modified files in

| pmx = | devm_kzalloc | (pfc->dev, sizeof(*pmx), GFP_KERNEL); | “NPD” denotes “Null-Pointer-Dereference” and “UBI” indi- |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Figure 7. | A report labeled as FP by our triage agent. | Bug Type | Total | Invalid | Direct | Refined | Fail |  |  |  |  |  |  |
| Our refinement pipeline addresses these challenges me- | Out-of-Bound | 6 | 2 | 4 | 0 | 0 |  |  |  |  |  |  |  |
| thodically. First, to manage report complexity, we distill gen- | Buffer-Overflow | 5 | 3 | 2 | 0 | 0 |  |  |  |  |  |  |  |
| erated bug reports to their essential components—primarily | Memory-Leak | 5 | 2 | 3 | 0 | 0 |  |  |  |  |  |  |  |
| to navigate the complexity of analysis and modification, we | Misuse | 7 | 3 | 3 | 1 | 0 |  |  |  |  |  |  |  |
| If the triage agent identifies a report as a false positive, as | These manually collected and labeled commits served as our |  |  |  |  |  |  |  |  |  |  |  |  |
| exemplified in Figure 7, a dedicated refinement agent takes | benchmark dataset for rigorous evaluation. |  |  |  |  |  |  |  |  |  |  |  |  |
| over. In the case shown, the initial checker (derived from | Few-shot examples. | We prepared three end-to-end exam- |  |  |  |  |  |  |  |  |  |  |  |
| the patch in Figure 2a) flagged the use of | pmx->pfc | because | ples for in-context learning. These three are patch com- |  |  |  |  |  |  |  |  |  |  |
| its logic failed to recognize | if (unlikely(!pmx)) | as a valid | mit | 3027e7b15b02 | (Null-Pointer-Dereference), | 3948abaa4e2b |  |  |  |  |  |  |  |
| null check, perhaps confused by the | unlikely() | macro. The | (Use-Before-Initialization), and | 4575962aeed6 | (Double-Free). |  |  |  |  |  |  |  |  |
| triage agent correctly interprets the check semantically and | The design and implementation of the checker for these three |  |  |  |  |  |  |  |  |  |  |  |  |
| flags the report as FP. The refinement agent then uses this | commits required approximately 40 person-hours. This was a |  |  |  |  |  |  |  |  |  |  |  |  |
| information to adjust the checker’s logic, specifically enhanc- | one-time effort, yielding reusable examples. We also explore |  |  |  |  |  |  |  |  |  |  |  |  |
| ing its ability to handle constructs like | unlikely() | , thereby | the use of real-world, off-the-shelf examples (§ 5.4.2). |  |  |  |  |  |  |  |  |  |  |
| preventing this type of false positive in subsequent scans | Utility functions. | While implementing example checkers, |  |  |  |  |  |  |  |  |  |  |  |
| while ensuring it can still detect the original vulnerability. | we identified several common helper operations. We imple- |  |  |  |  |  |  |  |  |  |  |  |  |
| A refined checker is accepted only if it satisfies two crite- | mented 9 such utility functions (e.g., | getMemRegionFromExpr | ) |  |  |  |  |  |  |  |  |  |  |
| ria: (1) it no longer generates warnings for the previously | to encapsulate low-level Clang Static Analyzer tasks, simpli- |  |  |  |  |  |  |  |  |  |  |  |  |
| identified false positive cases, and (2) it maintains its validity | fying checker development, particularly for LLM synthesis. |  |  |  |  |  |  |  |  |  |  |  |  |
| by correctly differentiating between the original buggy and | These utilities were designed for simplicity and extensibility. |  |  |  |  |  |  |  |  |  |  |  |  |
| patched code versions. This criterion ensures the semantic | Valid checkers. | To evaluate checker validity, we verify that |  |  |  |  |  |  |  |  |  |  |  |
| accuracy of the refined checkers. | it can both detect the original bug and recognize its fix. We |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | Implementation | the diff patch. Next, we check out the repository to the buggy |  |  |  |  |  |  |  |  |  |  |  |
| Input commit collection. | To collect patch commits for | commit (immediately preceding the patch) and scan these |  |  |  |  |  |  |  |  |  |  |  |
| rigorous evaluation, we implemented a systematic classifica- | objects to count the number of bug reports ( | 𝑁 | 𝑏𝑢𝑔𝑔𝑦 | ). We then |  |  |  |  |  |  |  |  |  |
| tion and selection process. First, we established 10 distinct | scan these objects after applying the patch commit to obtain |  |  |  |  |  |  |  |  |  |  |  |  |
| bug categories. We then used relevant keywords to identify | the number of remaining bug reports ( | 𝑁 | 𝑝𝑎𝑡𝑐ℎ𝑒𝑑 | ). A checker is |  |  |  |  |  |  |  |  |  |
| potentially related commits. A commit was included in our | considered valid if | 𝑁 | 𝑏𝑢𝑔𝑔𝑦 | > | 𝑁 | 𝑝𝑎𝑡𝑐ℎ𝑒𝑑 | and | 𝑁 | 𝑝𝑎𝑡𝑐ℎ𝑒𝑑 | < | 𝑇 | 𝑣𝑎𝑙𝑖𝑑 | , |
| dataset only when two authors independently agreed on its | where | 𝑇 | 𝑣𝑎𝑙𝑖𝑑 | is a threshold value (50 by default). |  |  |  |  |  |  |  |  |  |
| categorization. For each bug type, we initially examined the | Plausible checkers. | We determine plausible checkers based |  |  |  |  |  |  |  |  |  |  |  |
| first 20 commits that matched our search criteria. We con- | on their performance when analyzing the entire Linux kernel. |  |  |  |  |  |  |  |  |  |  |  |  |
| tinued reviewing commits beyond the initial 20 if we hadn’t | Our approach is founded on the principle that high-quality |  |  |  |  |  |  |  |  |  |  |  |  |
| yet collected 5 qualifying commits for a given category. Our | checkers, especially those derived from historical commits, |  |  |  |  |  |  |  |  |  |  |  |  |
| goal was to gather a minimum of 5 commits per bug type | should generate a reasonable number of actionable bug re- |  |  |  |  |  |  |  |  |  |  |  |  |
| whenever possible. Table 1 presents our categorization of | ports. A checker is classified as plausible if it either: (1) pro- |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 bug types and their corresponding patch commit counts. | duces fewer reports than a predefined threshold | 𝑇 | 𝑝𝑙𝑎𝑢𝑠𝑖𝑏𝑙𝑒 |  |  |  |  |  |  |  |  |  |  |

---

## Page 8

| SOSP ’25, October 13–16, 2025, Seoul, Republic of Korea | Chenyuan Yang, Zijie Zhao, Zichen Xie, Haoyu Li, and Lingming Zhang |
| --- | --- |
| (default: 20), or (2) demonstrates an acceptable false positive | int ice_set_fc(struct ice_port_info *pi, ...) |

rate in sampled warnings.

Checker refinement. We evaluate each valid checker by

scanning the entire kernel codebase independently, with

execution bounded by either a one-hour time limit or a max-

imum of 100 warnings during the refinement process. Note

the checkers without such constraints. The refinement pro-

total reports or exhibits at most one false positive in the

evaluated sample (labeled by our triage agent). For checkers

failing these criteria, we implement an iterative refinement

protocol targeting the identified false positives, permitting

up to three refinement iterations to improve precision.

5 Evaluation

by using the following metrics:

tics and synthesize discriminative checkers.

8

{

struct ice_aqc_get_phy_caps_data *pcaps __free(kfree) ;

if (!pi || !aq_failures)

return -EINVAL; → Path without any assignment to pcaps

...

{

struct x509_certificate * cert __free(x509_free_certificate);

if (!cert)

return ERR_PTR(-ENOMEM);

...

(b) False positive report for UBI.

Figure 8. Examples of false positives by KNighter.

analysis capabilities employed by checkers, including path

v6.13, and for bug finding, we examined versions from v6.9

| that these limits are only applied during the checker refine- | (a) | Bug in Use-Before-Initialization patch. |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ment phase; when performing actual bug detection, we run | struct x509_certificate *x509_cert_parse(const void *data ..) |  |  |  |  |  |
| cess begins with LLM-assisted triage of the checker’s output. | // | Auto-cleanup pointer not initialized to NULL (False Alarm) |  |  |  |  |
| Using a consistent random seed, we sample 5 warnings for | struct x509_parse_context *ctx __free(kfree) = NULL; |  |  |  |  |  |
| LLM inspection due to cost consideration. A checker qualifies | cert = kzalloc(sizeof(struct x509_certificate), GFP_KERNEL); |  |  |  |  |  |
| as plausible if it either generates fewer than | 𝑇 | 𝑝𝑙𝑎𝑢𝑠𝑖𝑏𝑙𝑒 | = | 20 | → | cert with assignment in every path |
| We explore the following research questions for KNighter: | Static Analysis Capabilities. | We further examine the static |  |  |  |  |
| RQ-1. | Can KNighter generate high-quality checkers? | sensitivity, region sensitivity, and advanced state tracking. |  |  |  |  |
| RQ-2. | Can the checkers generated by KNighter find real- | Hardware and software. | All our experiments are run on |  |  |  |
| world kernel bugs? | a workstation with 64 cores, 256 GB RAM, and 4 Nvidia |  |  |  |  |  |
| RQ-3. | Are the capabilities of KNighter orthogonal to the | A6000 GPUs, operating on Ubuntu 20.04.5 LTS. We use O3- |  |  |  |  |
| human-written checkers? | mini as our default LLM backend. By default, when scanning |  |  |  |  |  |
| RQ-4. | Are all the key components in KNighter effective? | the entire codebase, we use | -j32 | . We evaluated using Linux |  |  |
| Evaluation metrics. | We conduct an extensive evaluation | to v6.15. The Linux configuration used is | allyesconfig | . |  |  |
| Checker Validity Rate. | A valid checker successfully iden- | 5.1 | RQ1: Synthesized Checkers |  |  |  |
| tifies the buggy pattern in the original code and confirms | We evaluate KNighter on the 61 commits listed in Table 1 |  |  |  |  |  |
| its absence in the patched version. This metric reflects our | to show that it can synthesize high-quality checkers across |  |  |  |  |  |
| framework’s and LLMs’ ability to understand patch seman- | various bug types, beyond those in our few-shot examples. |  |  |  |  |  |
| Plausible Checker Rate. | This metric measures the number | 5.1.1 | Checker Synthesis. | In total, valid checkers were |  |  |
| of high-quality checkers synthesized, representing those that | generated for 39 commits. The 39 synthesized checkers av- |  |  |  |  |  |
| are both valid and exhibit a low false positive rate. | erage 125.7 lines of code and exhibit diverse static analysis |  |  |  |  |  |
| Bug Detection. | We assess the number of real-world bugs | capabilities. Specifically, 37 checkers are path-sensitive, 13 |  |  |  |  |
| successfully detected by the synthesized checkers. | incorporate region sensitivity, and 16 employ advanced state |  |  |  |  |  |
| Resource Efficiency. | This metric captures the computational | tracking; in contrast, only 2 leverage AST travelers. This |  |  |  |  |
| time and monetary costs associated with both checker syn- | suggests that KNighter can generate complex analysis logic, |  |  |  |  |  |
| thesis and execution. | not just simple pattern matching. |  |  |  |  |  |
| Checker Error Categories. | We classify checker failures into | Cost. | The full synthesis process required 15.9 hours, during |  |  |  |
| the following categories, ordered by severity: | which 8.2 million input tokens were processed and 1.2 million |  |  |  |  |  |
| • | Compilation Failures: Checkers that fail during com- | output tokens produced, resulting in an approximate cost of |  |  |  |  |
| pilation due to syntax or dependency errors. | $0.24 per commit | using O3-mini. For commits that ultimately |  |  |  |  |
| • | Runtime Errors: Checkers that compile successfully | yielded valid checkers, an average of 2.4 synthesis attempts |  |  |  |  |
| but crash during execution (e.g., | "The analyzer encoun- | was necessary (with a maximum of 8 attempts observed). |  |  |  |  |
| tered problems on source files" | ). | Failure analysis. | We now break down the failures from |  |  |  |
| • | Semantic Issues: Checkers that cannot distinguish be- | two perspectives: the underlying | failure root causes | and the |  |  |
| tween the buggy and patched code. | observed | failure symptoms | during the synthesis process. |  |  |  |

---

## Page 9

KNighter: Transforming Static Analysis with LLM-Synthesized Checkers SOSP ’25, October 13–16, 2025, Seoul, Republic of Korea

(i) Failure root causes . Among the 61 commits processed, Table 2. Newly detected bugs by KNighter.

22 did not result in any valid checker. Our investigation into

• 2 (9%) commits failed due to an inaccurate bug pattern,

• 7 (32%) failed owing to an inaccurate plan, and

• 13 (59%) were caused by inaccurate implementation.

For the implementation-related failures, a common issue

gles with precise value determination—especially when es-

tablishing buffer bounds at compile time—and it also faces

significant hurdles in analyzing multi-threaded code, for in-

stance, when assessing the proper use of locks.

(ii) Failure symptoms. During synthesis (allowing up to

10 attempts per commit), 273 failed attempts were recorded

from all 61 commits. The failures can be categorized as:

while the remaining 173 misclassified both versions as bug-

5.1.2 Checker Refinement. After scanning the entire

kernel codebase with these 39 valid checkers, 26 of them

were labeled “plausible” directly. Our refinement pipeline

was applied to the remaining 13 valid checkers, successfully

refining 11 of them. In total, 19 refinement steps were com-

9

KNighter 92 77 57 15 30

• Inaccurate bug pattern: In 5 cases, although the checker

correctly identified the original bug/patch scenario, the

inferred bug pattern lacked the necessary precision

for reliable detection across different contexts.

• Incorrect pattern matching: For 6 reports, the checker

correctly identified the bug pattern but applied it too

broadly, flagging code segments that did not meet the

validated before use).

synthesized checker did not incorporate these nuanced con-

straints, and the triage agent likewise failed to recognize the

critical differences, ultimately leading to a false positive.

5.2 RQ2: Detected Bugs

| these failures indicates that: | Total | Confirmed | Fixed | Pending | CVE |
| --- | --- | --- | --- | --- | --- |
| was that compiler optimizations inlined certain function | § 5.4.1). In total, we obtained 90 reports labeled as “bug”. |  |  |  |  |
| calls (e.g., | strcp | and | memset | ), which prevented the checker | Upon manual verification, we confirmed 61 true positives. |
| from properly intercepting these calls. | This indicates that the combination of our plausible checkers |  |  |  |  |
| Our approach exhibits limitations in handling buffer over- | and bug triage agent has a false positive rate of 32.2%. |  |  |  |  |
| flow and use-after-free commits. We believe these challenges | Our manual analysis of the 29 false positives revealed |  |  |  |  |
| stem from two main factors: static analysis inherently strug- | three recurring patterns leading to incorrect reports: |  |  |  |  |
| • | 65 attempts (23.8%) resulted in compilation errors, | specific constraints intended by the pattern. |  |  |  |
| • | 1 attempt (0.4%) led to a runtime error, and | • | Trigger condition mismanagement: | The most common |  |
| • | 207 attempts (75.8%) suffered from semantic issues that | issue (18 reports) involved checkers where both the |  |  |  |
| obstructed proper bug identification. | pattern and matching were correct, but the checker |  |  |  |  |
| Of the 207 semantic failures, 34 checkers erroneously flagged | failed to manage trigger or state conditions properly |  |  |  |  |
| both buggy and patched code as potentially problematic, | (e.g., failing to recognize a pointer had already been |  |  |  |  |
| free. This outcome underscores the challenge of accurately | Case study: A high false positive rate checker. | In commit |  |  |  |
| distinguishing buggy code. | 90ca6956d383 | (“ice: Fix freeing uninitialized pointers”, see |  |  |  |
| Interestingly, even the 173 checkers that did not recognize | Figure 8a), the issue stems from the pointer | pcaps | not being |  |  |
| the specific bug in their input patch can still be valuable. | initialized to | NULL | . If an early return or error path occurs |  |  |
| When deployed across the large system, these checkers may | before the pointer is allocated, the cleanup routine may inad- |  |  |  |  |
| successfully detect bugs with similar patterns in other con- | vertently attempt to free an uninitialized (or garbage) pointer. |  |  |  |  |
| texts. This apparent paradox likely arises because the failure | In such cases, the checker should account for the possibility |  |  |  |  |
| to detect the training bug is sometimes due to edge cases | of an early exit leaving the pointer unset. In contrast, the bug |  |  |  |  |
| or context-specific complexities rather than inherent defi- | report in Figure 8b highlights a scenario where, although |  |  |  |  |
| ciencies in the checkers’ detection logic. Moreover, these | the | cert | pointer starts uninitialized, it is immediately as- |  |  |
| checkers generally exhibit lower false positive rates com- | signed a valid value along every execution path, ensuring it |  |  |  |  |
| pared to those that incorrectly flag both buggy and patched | is never left in an unassigned state. Thus, despite the initial |  |  |  |  |
| code, enhancing their practical utility for bug detection. | uninitialized state, the code does not constitute a bug. Our |  |  |  |  |
| pleted successfully. This demonstrates the effectiveness of | 5.2.1 | Overall. | To date, static analyzers synthesized by |  |  |
| our refinement pipeline, which successfully refined 84.6% of | KNighter have identified 92 new bugs in the Linux kernel. |  |  |  |  |
| the valid checkers that were not “plausible” initially. | As summarized in Table 2, developer confirmation has been |  |  |  |  |
| False positive rate. | Of the 37 plausible checkers, 16 did not | received for 77 of these bugs. Among those confirmed, 57 |  |  |  |
| report any bugs. For the remaining checkers, we applied our | have already been fixed. The remaining 15 bugs are currently |  |  |  |  |
| bug triage agent to filter all the reports, focusing only on | awaiting developer review (calculated as Total - Confirmed). |  |  |  |  |
| those labeled as “bug” since our triage agent demonstrated | Notably, 30 of the discovered bugs have been assigned CVE |  |  |  |  |
| a low false negative rate in our evaluation (as shown in | numbers, showing their practical security impact. |  |  |  |  |

---

## Page 10

| SOSP ’25, October 13–16, 2025, Seoul, Republic of Korea | Chenyuan Yang, Zijie Zhao, Zichen Xie, Haoyu Li, and Lingming Zhang |
| --- | --- |
| 54 | and (ii) an additional set of 100 commits automatically col- |

50 Bugs from hand-collected commits

30

Number of Bugs

7

0

NPD OOB UAF UBI

MemLeak BufOver

(a) Number of bugs in each type.

Bugs from hand-collected commits

50

40

10 10

7

| 3 | 2 | 1 | 1 | 1 |
| --- | --- | --- | --- | --- |
| drivers | sound | arch |  |  |
| samples | include |  |  |  |

25

15

Number of Bugs 7

0-1 yr 1-2 yr 2-5 yr 5-10 yr 10-15 yr 15+ yr

(c) Number of bugs with different lifetimes.

10

4

10

ure 9b show the bug distribution from these sources—with

the light blue for bugs from the initial evaluation set and the

of bug types (see Figure 9a). Null-Pointer-Dereference bugs

cally collecting commits related to Null-Pointer-Dereference,

which yielded an additional 30 bugs.

drivers subsystem (67 out of 92), reflecting its large footprint

in the kernel [9]. Additionally, 10 and 7 bugs were identified

in the sound and net subsystems, respectively. Notably, 2 bugs

is especially critical.

26 bugs had existed for over five years before detection. This

indicates that the vulnerabilities uncovered by KNighter are

checkers each found five or more bugs. In general, checkers

valuable, findings. This suggests that KNighter can learn and

producing a mix of broad-coverage and high-yield checkers.

5.2.2 Case Study. Here are examples of vulnerabilities

detected by KNighter.

free_netdev must be invoked only after all the references

to its private data, otherwise, it could cause a Use-After-

shown in Figure 10b, where dm (the private data of ndev )

This newly discovered issue was assigned CVE-2025-21715.

by limiting the number of bytes copied via copy_from_user

| Bugs from auto-collected commits | lected using keywords related to Null-Pointer-Dereference |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 40 | to further explore that specific bug class. Figure 9a and Fig- |  |  |  |  |  |
| 20 | 16 | light purple for those from the auto-collected set. |  |  |  |  |
| 10 | Bug types. | Analysis of checkers from the manually collected |  |  |  |  |
| 4 | 3 | 3 | 3 | 1 | 1 | commits reveals that KNighter can detect a diverse range |
| IntOver | Misuse | are the most prevalent, highlighting KNighter ’s strength in |  |  |  |  |
| Concurrency | this area. In response, we expanded our effort by automati- |  |  |  |  |  |
| 70 | 67 | Bug location. | As shown in Figure 9b, the detected bugs span |  |  |  |
| 60 | Bugs from auto-collected commits | various Linux kernel subsystems. The majority appear in the |  |  |  |  |
| 30 | were found in the | samples | directory—an area that provides |  |  |  |
| Number of Bugs | 20 | example usage for kernel developers and where correctness |  |  |  |  |
| 0 | Bug lifetime. | Figure 9c illustrates the distribution of bug |  |  |  |  |
| net | fs | lib | lifetimes. Notably, the average bug lifetime is | 4.3 years | , and |  |
| (b) | Number of bugs in each subsystem. | difficult to detect and remain latent for extended periods, |  |  |  |  |
| 26 | underscoring the effectiveness of our approach. |  |  |  |  |  |
| 22 | Bug distribution over commits. | Synthesized checkers |  |  |  |  |
| 20 | from 39 bug-fix commits uncovered new bugs (2.4 each on |  |  |  |  |  |
| 16 | 16 | average), with a long-tail skew (as shown in Figure 9d): five |  |  |  |  |
| 10 | derived from recurring error patterns yield higher counts, |  |  |  |  |  |
| 5 | 5 | while those from specialized fixes surface fewer, yet still |  |  |  |  |
| 0 | propagate impactful patterns beyond their original contexts, |  |  |  |  |  |
| 8 | CVE-2025-21715. | Figure 10a (the input patch to KNighter) |  |  |  |  |
| 6 | shows a fix for a Use-After-Free vulnerability. In this patch, |  |  |  |  |  |
| Number of Bugs | 2 | Free issue. Leveraging this patch, the checker generated by |  |  |  |  |
| 0 | KNighter identified a similar bug in | dm9000_drv_remove | , as |  |  |  |
| (d) | Number of bugs detected by each commit. | remains in use after | ndev | is freed, causing a Use-After-Free. |  |  |
| Figure 9. | Details of new bugs. Subfigures (a), (b), (c), and (d) | CVE-2024-50259. | Figure 10c shows an input patch fixing a |  |  |  |
| show breakdowns by type, subsystem, lifetime, and commit. | buffer overflow vulnerability. The patch mitigates the risk |  |  |  |  |  |
| The checkers for bug detection originate from two sources: | to | sizeof(mybuf) - 1 | , thereby preserving space for a trail- |  |  |  |
| (i) the initial 61 manually collected commits used for eval- | ing zero. This trailing zero is essential for subsequent string |  |  |  |  |  |
| uation in § 3.1 across diverse bug types (shown in Table 1), | operations, such as | sscanf | , to function correctly. Taking this |  |  |  |

---

## Page 11

| KNighter: Transforming Static Analysis with LLM-Synthesized Checkers | SOSP ’25, October 13–16, 2025, Seoul, Republic of Korea |
| --- | --- |
| static int emac_remove(struct platform_device *pdev) { | Table 1. We conducted the comparative analyses by running |
| ... | Smatch on the entire codebase to determine if it could detect |

mdiobus_unregister(adpt->mii_bus);

- free_netdev(netdev);

iounmap(adpt->phy.digital);

}

dm9000_release_board(pdev, dm);

regulator_disable(dm->power_supply);

char mybuf[64];

- if (copy_from_user(mybuf, buf, nbytes))

return -EFAULT;

}

(c) Input Buffer-Overflow patch.

...

+ if (size > sizeof(buf) - 1)

+ buf[size] = 0;

(d) CVE-2024-50259 , found by the checker for the patch above.

Figure 10. Example vulnerabilities detected by KNighter.

11

the bugs found by KNighter.

Notably, Smatch failed to detect any of our true positive bugs ,

It fails to recognize that functions like devm_kzalloc may re-

5.4 RQ4: Effectiveness of Components

5.4.1 Bug Triage Agent. To evaluate our bug triage agent,

manual review from two authors. The agent achieved 7 true

positives (TP), 22 false positives (FP), 50 true negatives (TN),

and zero false negatives (FN). The absence of false negatives

is particularly important, as it indicates the agent effectively

prioritized all potentially true bugs in this set, minimizing

TPs and 22 FPs, majority voting did not offer a significant

| if (adpt->phy.digital) | Smatch reported a total of 1970 errors and 2870 warnings |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| iounmap(adpt->phy.base); | across the kernel. We manually inspected all the files where |  |  |  |  |
| + | free_netdev(netdev); | bugs were detected to assess whether any of the true positive |  |  |  |
| return 0; | bugs identified by KNighter were also detected by Smatch. |  |  |  |  |
| (a) | Input Use-After-Free patch. | underscoring the unique detection capabilities of KNighter. |  |  |  |
| static void dm9000_drv_remove(struct platform_device *pdev) { | Further analysis of Smatch’s checkers revealed that they |  |  |  |  |
| ... | do not fully leverage the domain-specific knowledge em- |  |  |  |  |
| free_netdev | (ndev); | /* free device structure */ | bedded in the Linux kernels—a resource that KNighter effec- |  |  |
| if ( | dm | ->power_supply) | tively extracts from historical patches. For instance, Smatch’s |  |  |
| Use the private data | dm | after freeing ndev | check_deref | checker employs static range analysis to iden- |  |
| } | tify potential null pointers but lacks domain-specific insights. |  |  |  |  |
| (b) CVE-2025-21715 | , found by the checker for the patch above. | turn | NULL | under error conditions that conventional static |  |
| int lpfc_debugfs_lockstat_write(struct file *file, ...) { | range analysis cannot detect. Consequently, Smatch iden- |  |  |  |  |
| int i; | tified only three potential null pointer dereferences, all of |  |  |  |  |
| + | size_t bsize; | which were confined to unit test files rarely prioritized by |  |  |  |
| memset(mybuf, 0, sizeof(mybuf)); | developers. We conclude that KNighter and Smatch detect |  |  |  |  |
| + | bsize = min(nbytes, (sizeof(mybuf) - 1)); | different classes of bugs, demonstrating KNighter’s effec- |  |  |  |
| + | if (copy_from_user(mybuf, buf, bsize)) | tiveness in learning domain knowledge from patches and |  |  |  |
| ... | subsequently identifying diverse bugs and vulnerabilities. |  |  |  |  |
| static ssize_t nsim_nexthop_bucket_activity_write(...) { | from the 39 valid checkers, we sampled up to 5 reports per |  |  |  |  |
| memset(mybuf, 0, sizeof(mybuf)); | checker to reduce manual inspection efforts, aiming to re- |  |  |  |  |
| - | if (size > sizeof(buf)) | Possible buffer overflow | duce manual inspection efforts while maintaining evaluation |  |  |
| return -EINVAL; | coverage. In total, we collected 79 reports from 18 check- |  |  |  |  |
| if (copy_from_user(buf, user_buf, size)) | ers, while the remaining 21 valid checkers didn’t generate |  |  |  |  |
| return -EFAULT; | reports. Our triage agent classified 29 reports as “bug” (posi- |  |  |  |  |
| ... | tive) and 50 as “not-a-bug” (negative). These classifications |  |  |  |  |
| } | were compared against ground truth labels established by |  |  |  |  |
| patch as input, the checker generated by KNighter identi- | the risk of overlooking genuine issues, even though the 22 |  |  |  |  |
| fied a similar bug in | nsim_nexthop_bucket_activity_write | , | false positives require further filtering. |  |  |
| as shown in Figure 10d. In this case, the omission of append- | We also evaluated 5-way self-consistency via majority |  |  |  |  |
| ing a trailing zero after copying data from userspace could | voting [48]. For each report, we ran our triage agent five |  |  |  |  |
| lead to improper string handling and potential overflow is- | independent times and labeled the report as a “bug” only |  |  |  |  |
| sues. This detected issue was subsequently fixed by adding | if the agent made that prediction in at least | 𝑡 | of the runs. |  |  |
| the trailing zero and was assigned CVE-2024-50259. | Compared to our single-sample baseline, which identified 7 |  |  |  |  |
| 5.3 | RQ3: Orthogonality with Smatch | improvement. Using a threshold of | 𝑡 | = | 3 kept the TP count |
| Since no comparable automated static analyzer generation | at 7 but slightly increased FPs to 24. A stricter threshold |  |  |  |  |
| approaches exist for this domain, we evaluate KNighter | of | 𝑡 | = | 4 also resulted in 7 TPs while reducing FPs to 20. |  |
| against expert-written checkers. Our baseline is provided by | Ultimately, majority voting only slightly shifted the false |  |  |  |  |
| Smatch [2], which is widely used in Linux kernel analysis | positive count in this setting. There could be two potential |  |  |  |  |
| and supports tailored checks for all bug types considered in | reasons. For TPs, the agent likely identifies these bugs with |  |  |  |  |

*[Image: Page 11 Image]*

---

## Page 12

| SOSP ’25, October 13–16, 2025, Seoul, Republic of Korea | Chenyuan Yang, Zijie Zhao, Zichen Xie, Haoyu Li, and Lingming Zhang |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Table | 3. | Ablation | study | results. | “Default” | means | addition to our default model, O3-mini, we tested GPT-4o, |
| KNighter’s standard configuration utilizing multi-stage syn- | Gemini-2-flash, and open-source DeepSeek-R1. |  |  |  |  |  |  |
| thesis, fixed few-shot examples, and the O3-mini model. Al- | As detailed in Table 3, O3-mini yielded the most valid |  |  |  |  |  |  |
| ternative configurations are compared against this baseline. | checkers (12). GPT-4o and DeepSeek-R1 performed compa- |  |  |  |  |  |  |

Errors

Variants Valid

Syntax Runtime Semantics

W/ GPT-4o 11 31 0 76

high confidence, meaning a single run is sufficient to detect

all of them. For FPs, the agent’s predictions are likely less

confident and more inconsistent across different runs.

across different language models for checker synthesis. In

12

rably to each other, generating 11 valid checkers each, only

slightly fewer than O3-mini. This suggests that multiple high-

capability models, including open-source options, are viable,

although minor differences in performance exist.

CSA implementation, frequently using non-existent APIs

synthesis demands more than general coding proficiency;

accurate knowledge or inference of the target framework’s

specific APIs and conventions (CSA in this case) is essential.

eQL [17] or Semgrep [41]).

| Default | 12 | 28 | 0 | 75 | In contrast, Gemini-2-flash performed substantially worse, |
| --- | --- | --- | --- | --- | --- |
| W/o multi-stage | 8 | 52 | 3 | 75 | producing valid checkers for only 4 commits. Upon closer |
| W/ RAG | 12 | 37 | 4 | 62 | inspection, we found that Gemini-2-flash struggled with |
| W/ DeepSeek-R1 | 11 | 29 | 8 | 66 | and generating syntax errors at a much higher rate (130 |
| W/ Gemini-2-flash | 4 | 130 | 2 | 44 | vs. 28). This highlights a crucial insight: successful checker |
| 5.4.2 | Ablation Study. | To evaluate our design choices, we | 6 | Limitations and Discussion |  |
| created a sample dataset of patch commits for an ablation | Limitations. | KNighter faces challenges with highly complex |  |  |  |
| study. We randomly sampled 2 commits from each bug type | bug patterns, particularly those involving state-machine rea- |  |  |  |  |
| using zero as the random seed. This resulted in a dataset of | soning, such as use-after-free, and concurrency issues that |  |  |  |  |
| 20 commits (2 commits × 10 bug types). Table 3 shows the | require analyzing multi-threaded code and locking schemes. |  |  |  |  |
| overall results of our ablation study. | Synthesizing precise checkers for these issues is difficult for |  |  |  |  |
| Checker synthesis. | First, we assessed the impact of our | today’s LLMs, as it requires a sophisticated understanding |  |  |  |
| default | three-stage synthesis approach | (bug pattern analy- | of a program’s temporal and interprocedural behavior. To |  |  |
| sis, plan synthesis, checker implementation) compared to | address this, a promising future direction is to improve the |  |  |  |  |
| directly synthesizing checkers in a | single stage | (omitting | analysis agent to automatically abstract complex bug reports |  |  |
| explicit pattern/plan steps), using identical few-shot exam- | into more formal state-machine representations. This would |  |  |  |  |
| ples. As shown in Table 3, the multi-stage approach proved | enable the synthesis of precise, state-aware checkers that |  |  |  |  |
| more effective, yielding valid checkers for 12 commits com- | can trace the specific sequences of operations leading to a |  |  |  |  |
| pared to only 8 for the single-stage method. Furthermore, the | bug. A second, complementary strategy is to focus on se- |  |  |  |  |
| single-stage approach resulted in significantly more syntax | lectively identifying high-quality, canonical bug fixes. This |  |  |  |  |
| errors (52 vs. 28), often leading to checkers that failed to com- | involves developing methods to filter out patches that are |  |  |  |  |
| pile. This highlights the value of the structured multi-stage | overly complex or specific, allowing KNighter to learn from |  |  |  |  |
| process for improving both validity and compilability. | reusable, idiomatic repair patterns and improve the overall |  |  |  |  |
| Second, we explored using | Retrieval-Augmented Genera- | performance of checker synthesis. |  |  |  |
| tion (RAG) | [16] for selecting few-shot examples dynamically, | Generability. | KNighter employs a general three-stage work- |  |  |
| comparing it against our default set of | fixed examples | . It uti- | flow: LLM-driven synthesis of checkers from bug-fix patches, |  |  |
| lizes a knowledge base derived from 118 official CSA check- | patch-grounded validation, and triage/refinement to reduce |  |  |  |  |
| ers [12], embedded using | text-embedding-ada-002 | [4]. Dur- | false positives. While the Linux kernel served as an ideal and |  |  |
| ing synthesis, three relevant examples are retrieved based | challenging initial target due to its scale, complexity, and |  |  |  |  |
| on semantic similarity. Our results indicate that RAG-based | importance, our approach is not fundamentally tied to it. The |  |  |  |  |
| example selection achieved comparable effectiveness to our | workflow’s applicability extends to any project that meets |  |  |  |  |
| fixed examples, also generating valid checkers for 12 com- | two criteria: a version history with bug-fix commits for learn- |  |  |  |  |
| mits. However, because the official CSA checkers used are | ing, and a static analysis framework to serve as a synthesis |  |  |  |  |
| substantially longer than our curated fixed examples, the | target ( | e.g., | Chromium [1]). Furthermore, the implementa- |  |  |
| RAG approach incurred approximately double the input/out- | tion is not limited to C/C++. Although we demonstrated its |  |  |  |  |
| put token cost. Due to similar effectiveness, our default fixed | use with the Clang Static Analyzer [12], the pipeline can be |  |  |  |  |
| few-shot examples offer better cost-efficiency for this task. | readily adapted—via a small set of few-shot examples—to |  |  |  |  |
| LLM choice. | We evaluated the performance of KNighter | generate checkers or rules for other ecosystems ( | e.g., | Cod- |  |

---

## Page 13

| KNighter: Transforming Static Analysis with LLM-Synthesized Checkers | SOSP ’25, October 13–16, 2025, Seoul, Republic of Korea |  |  |
| --- | --- | --- | --- |
| 7 | Related Work | infrastructure to enforce the inferred specifications. We at- |  |
| This section mainly discusses related work on both tradi- | tempted to include Seal in our experimental comparison, |  |  |
| tional and LLM-based static analysis, contextualizing the | but encountered practical difficulties as its publicly available |  |  |
| contributions of KNighter. While our work focuses on syn- | version depends on private commercial tools and was not |  |  |
| thesizing | static | analyzers that inspect source code without | compatible with the recent Linux kernel versions. |
| execution, it is worth noting that checker synthesis has also | General static analysis frameworks. | Other systems focus |  |
| been explored for generating | dynamic | runtime checks [24, | on improving underlying static analysis techniques for better |
| 33, 34]. These approaches are fundamentally different from | precision or efficiency across multiple bug types. FiTx [45], |  |  |
| KNighter. Dynamic checkers typically learn rules from test | for example, implements fast analysis for single compila- |  |  |
| executions [34] to detect bugs based on concrete runtime | tion units, while PATA [29] enhances alias analysis precision |  |  |
| states, such as capturing semantic “grey-failures”. In contrast, | using path information. These systems often encode bug pat- |  |  |
| KNighter learns from source code patches to create static | terns as state machines [29, 45], but designing these patterns |  |  |
| checkers that can cover all potential execution paths, includ- | still typically involves manual effort. |  |  |
| ing corner cases rarely triggered during program execution. | Our synthesis approach. | In contrast to the above, KNighter |  |

uses LLMs to synthesize the static analyzer itself directly

from historical patch information. Instead of relying on pre-

| 7.1 | Traditional Static Analysis | defined rules or inferring specifications for existing checkers, |
| --- | --- | --- |
| Given the cruciality of the Linux kernel and the diversity of | KNighter learns both the bug pattern and the corresponding |  |
| its bugs, many static analyzers have been developed. These | detection logic, generating a new checker automatically. This |  |
| generally fall into several categories based on their approach. | approach fundamentally differs by automating the analyzer |  |
| Rule/Model-based analyzers. | A significant body of work | creation process, potentially offering greater adaptability to |
| focuses on detecting specific classes of bugs using prede- | new bug types compared to traditional methods or specifi- |  |
| fined rules or models. Examples include CRIX [35] (detecting | cation inference. This distinction may also make KNighter |  |
| missing checks via def-use slices), Goshawk [36] (memory | more versatile; while specification-inference tools excel at |  |
| corruption analysis), UBITect [56] (Use Before Initialization | finding bugs related to the interfaces they model, KNighter |  |
| bugs), CRed [51] (Use-After-Free detection), LR-Miner [28] | can synthesize checkers for a broader range of issues demon- |  |
| (data races via locking rules), tools targeting refcounting | strated in patches, including problems not strictly tied to |  |
| bugs based on derived anti-patterns [21] or specific con- | interface misuse, such as certain integer overflows or com- |  |
| ventions [32], DCUAF [8] (concurrent Use-After-Free), and | plex logic errors. Furthermore, although KNighter currently |  |
| SUTURE [58] (taint analysis for userspace input vulnerabil- | generates CSA checkers, the core idea of LLM-based checker |  |
| ities). While often effective for their targeted bug classes, | synthesis is potentially generalizable to target other static |  |
| these approaches typically require extensive human exper- | analysis frameworks, given the broad training data of mod- |  |
| tise for analysis design and implementation, limiting their | ern LLMs. Thus, KNighter complements existing approaches |  |
| scalability and adaptability to newly emerging bug patterns | by providing a mechanism to automatically generate analyz- |  |
| in the rapidly evolving kernel. | ers for newly observed bug patterns found in patches. |  |

Deviation-based specification inference. Methods such

| as [6, 15, 38] infer specifications by assuming the | majority | of | 7.2 | LLM-Based Static Analysis |
| --- | --- | --- | --- | --- |
| uses are correct and flagging deviations. While effective in | Recent LLM advancements enable new static analysis tech- |  |  |  |
| some settings, classic systems rely on a small, fixed set of rule | niques, differing significantly from our synthesis approach. |  |  |  |
| templates | plus probabilistic clustering/ranking, which con- | LLM-augmented static analysis. | Some techniques use |  |
| strains bug-pattern coverage and—without strong semantic | LLMs to | assist | existing tools by automating tasks previously |  |
| post-checks or refinement—often yields higher FPR [15, 38]. | requiring manual effort. For example, LLMs can infer taint |  |  |  |
| FICS [6] reduces template dependence via ML grouping of | specifications for external APIs (IRIS [30], Artemis [23]), gen- |  |  |  |
| functionally similar code, but still rests on the majority- | erate post-constraints to prune analysis paths (LLift [26]), |  |  |  |
| correct assumption and similarity heuristics, which can mis- | or infer resource-handling intentions (InferROI [47]). While |  |  |  |
| cluster code and introduce noise. | helpful, these methods still fundamentally depend on a sub- |  |  |  |
| Patch-based specification inference. | Another line of work | stantial, human-developed analyzer core, | e.g., | the manually |
| leverages historical patches to | infer specifications | , which are | defined rules for taint propagation [23]. This can limit their |  |
| then used by separate checkers. For instance, APHP [31] | ability to easily generalize to detect novel bug types beyond |  |  |  |
| extracts API Post-Handling (APH) specifications from both | those originally targeted by the core analyzer’s design. |  |  |  |
| code and descriptions in patches to detect APH violations. | Direct code analysis with LLMs. | Other work uses LLMs to |  |  |
| A very recent work, Seal [11], analyzes security patches to | directly analyze | source code, using techniques like Retrieval- |  |  |
| infer diverse specifications for Linux interfaces. While pow- | Augmented Generation (Vul-RAG [14]), prompt engineer- |  |  |  |
| erful, these methods generally rely on existing static analysis | ing [57], or fine-tuning [42]. However, directly applying |  |  |  |

13

---

## Page 14

| SOSP ’25, October 13–16, 2025, Seoul, Republic of Korea | Chenyuan Yang, Zijie Zhao, Zichen Xie, Haoyu Li, and Lingming Zhang |  |  |  |
| --- | --- | --- | --- | --- |
| LLMs to scan large systems like the Linux kernel is often | [6] Ahmadi, M., Farkhani, R. M., Williams, R., and Lu, L. Finding bugs |  |  |  |
| prohibitively expensive and faces scalability challenges. | using your own code: detecting functionally-similar yet inconsistent |  |  |  |
| Our synthesis approach. | In contrast, KNighter uses LLMs | code. In | 30th USENIX security symposium (USENIX Security 21) | (2021), |

pp. 2025–2040.

| to | synthesize the entire static analyzer | from patches. Un- | [7] Ayewah, N., Pugh, W., Hovemeyer, D., Morgenthaler, J. D., and |
| --- | --- | --- | --- |
| like LLM-augmented tools, this minimizes reliance on pre- | Penix, J. Using static analysis to find bugs. | IEEE software 25 | , 5 (2008), |
| existing manual analyzer development, enhancing adapt- | 22–29. |  |  |
| ability for diverse bug types. Unlike direct LLM analysis, | [8] Bai, J.-J., Lawall, J., Chen, Q.-L., and Hu, S.-M. Effective static analysis |  |  |
| KNighter generates efficient, reusable static checkers, avoid- | of concurrency Use-After-Free bugs in linux device drivers. In | 2019 |  |

USENIX Annual Technical Conference (USENIX ATC 19) (Renton, WA,

| ing the high costs and scalability issues of scanning massive | July 2019), USENIX Association, pp. 255–268. |  |
| --- | --- | --- |
| codebases directly with LLMs. A very recent concurrent | [9] Bursey, J., Sani, A. A., and Qian, Z. Syzretrospector: A large-scale |  |
| work, MoCQ [27], also explores checker/query synthesis, | retrospective study of syzbot, 2024. |  |
| but it focuses on general bug patterns and relies on man- | [10] Cai, Y., Yao, P., Ye, C., and Zhang, C. Place your locks well: under- |  |
| ual examples for validation. KNighter distinguishes itself | standing and detecting lock misuse bugs. In | 32nd USENIX Security |

Symposium (USENIX Security 23) (2023), pp. 3727–3744.

| not only by automatically inferring specific, nuanced pat- | [11] Chen, W., Zhang, B., Wang, C., Tang, W., and Zhang, C. | Seal: |
| --- | --- | --- |
| terns from patches but also by incorporating a closed-loop | Towards diverse specification inference for linux interfaces from secu- |  |
| triage-refinement pipeline to iteratively improve checker | rity patches. In | Proceedings of the Twentieth European Conference on |
| precision. This fully automated refinement process makes | Computer Systems | (2025), pp. 1246–1262. |
| our approach more scalable for detecting complex defects in | [12] Clang, and LLVM. Clang Static Analyzer. | https://clang-analyzer. |

llvm.org/ .

| system software, establishing it as a practical paradigm for | [13] Deng, Y., Xia, C. S., Peng, H., Yang, C., and Zhang, L. Large language |
| --- | --- |
| applying LLM intelligence to large-scale static analysis. | models are zero-shot fuzzers: Fuzzing deep-learning libraries via large |

language models. In Proceedings of the 32nd ACM SIGSOFT international

8 Conclusion symposium on software testing and analysis (2023), pp. 423–435.

[14] Du, X., Zheng, G., Wang, K., Feng, J., Deng, W., Liu, M., Chen, B.,

| This paper introduces KNighter, a novel approach that trans- | Peng, X., Ma, T., and Lou, Y. Vul-rag: Enhancing llm-based vulnerabil- |  |
| --- | --- | --- |
| forms how LLMs can contribute to static analysis for complex | ity detection via knowledge-level rag. | arXiv preprint arXiv:2406.11147 |
| systems like the Linux kernel. By synthesizing static analyz- | (2024). |  |
| ers rather than directly analyzing code, KNighter bridges the | [15] Engler, D., Chen, D. Y., Hallem, S., Chou, A., and Chelf, B. Bugs as |  |
| gap between LLMs’ reasoning capabilities and the practical | deviant behavior: A general approach to inferring errors in systems |  |

code. ACM SIGOPS Operating Systems Review 35 , 5 (2001), 57–72.

| constraints of analyzing massive systems. KNighter’s practi- | [16] Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., Dai, Y., Sun, J., Wang, |  |  |
| --- | --- | --- | --- |
| cal impact is shown by the discovery of 92 new, long-latent | H., and Wang, H. Retrieval-augmented generation for large language |  |  |
| bugs in the Linux kernel, with 77 confirmed, 57 fixed, and | models: A survey. | arXiv preprint arXiv:2312.10997 2 | (2023). |
| 30 CVE assigned. | [17] GitHub. CodeQL. | https://codeql.github.com/ | . |
| Looking forward, KNighter opens new possibilities for | [18] Gong, S., Peng, D., Altinbüken, D., Fonseca, P., and Maniatis, P. |  |  |

Snowcat: Efficient kernel concurrency testing using a learned coverage

| scalable LLM-based static analysis. Future work could extend | predictor. In | Proceedings of the 29th Symposium on Operating Systems |  |
| --- | --- | --- | --- |
| this approach to other systems beyond the Linux kernel, | Principles | (2023), pp. 35–51. |  |
| incorporate additional learning paradigms, and further refine | [19] Gong, S., Wang, R., Altinbüken, D., Fonseca, P., and Maniatis, |  |  |
| checker generation techniques to address more complex bug | P. Snowplow: Effective kernel fuzzing with a learned white-box test |  |  |
| patterns. By leveraging LLMs to synthesize tools rather than | mutator. | In | Proceedings of the 30th ACM International Conference |

on Architectural Support for Programming Languages and Operating

| perform analysis directly, we establish a scalable, reliable, | Systems, Volume 2 | (2025), pp. 1124–1138. |
| --- | --- | --- |
| and traceable paradigm for utilizing AI in critical software | [20] Grattafiori, A., Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al- |  |
| security applications. | Dahle, A., Letman, A., Mathur, A., Schelten, A., Vaughan, A., |  |

et al. The llama 3 herd of models. arXiv preprint arXiv:2407.21783

Acknowledgments (2024).

[21] He, L., Su, P., Zhang, C., Cai, Y., and Ma, J. One simple api can cause

| We are grateful to the anonymous reviewers for their valu- | hundreds of bugs an analysis of refcounting bugs in all modern linux |  |
| --- | --- | --- |
| able feedback that helped to improve this paper. This work | kernels. In | Proceedings of the 29th Symposium on Operating Systems |
| was partially supported by NSF grant CCF-2131943. | Principles | (2023), pp. 52–65. |

[22] Huang, L., Yu, W., Ma, W., Zhong, W., Feng, Z., Wang, H., Chen,

References Q., Peng, W., Feng, X., Qin, B., et al. A survey on hallucination in

large language models: Principles, taxonomy, challenges, and open

| [1] Chromium. | https://www.chromium.org/chromium-projects/ | . | questions. | ACM Transactions on Information Systems 43 | , 2 (2025), 1–55. |
| --- | --- | --- | --- | --- | --- |
| [2] Smatch. | https://github.com/error27/smatch | . | [23] Ji, Y., Dai, T., Zhou, Z., Tang, Y., and He, J. Artemis: Toward accurate |  |  |
| [3] Syzkaller. | https://github.com/google/syzkaller/ | . | detection of server-side request forgeries through llm-assisted inter- |  |  |
| [4] text-embedding-ada-002. | https://openai.com/index/new-and- | procedural path-sensitive taint analysis. | Proceedings of the ACM on |  |  |
| improved-embedding-model/ | . | Programming Languages 9 | , OOPSLA1 (2025), 1349–1377. |  |  |
| [5] Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, | [24] Jiang, Y., Zhou, Z., Xu, B., Liu, B., Xu, R., and Huang, P. Training |  |  |  |  |
| F. L., Almeida, D., Altenschmidt, J., Altman, S., Anadkat, S., et al. | with confidence: Catching silent errors in deep learning training with |  |  |  |  |

Gpt-4 technical report. arXiv preprint arXiv:2303.08774 (2023).

14

---

## Page 15

| KNighter: Transforming Static Analysis with LLM-Synthesized Checkers | SOSP ’25, October 13–16, 2025, Seoul, Republic of Korea |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| automated proactive checks. In | Proceedings of the 19th USENIX Sym- | [43] Sun, C., Sheng, Y., Padon, O., and Barrett, C. | Clover: Clo sed- |  |  |  |
| posium on Operating Systems Design and Implementation | (Boston, MA, | loop ver ifiable code generation. In | International Symposium on AI |  |  |  |
| USA, July 2025), OSDI ’25, USENIX Association. | Verification | (2024), Springer, pp. 134–155. |  |  |  |  |
| [25] Lattuada, A., Hance, T., Cho, C., Brun, M., Subasinghe, I., Zhou, | [44] Sun, S., Liu, Y., Wang, S., Zhu, C., and Iyyer, M. Pearl: Prompting large |  |  |  |  |  |
| Y., Howell, J., Parno, B., and Hawblitzel, C. Verus: Verifying rust | language models to plan and execute actions over long documents. |  |  |  |  |  |
| programs using linear ghost types. | Proceedings of the ACM on Pro- | arXiv preprint arXiv:2305.14564 | (2023). |  |  |  |
| gramming Languages 7 | , OOPSLA1 (2023), 286–315. | [45] Suzuki, K., Ishiguro, K., and Kono, K. Balancing analysis time and |  |  |  |  |
| [26] Li, H., Hao, Y., Zhai, Y., and Qian, Z. Enhancing static analysis for | bug detection: daily development-friendly bug detection in linux. In |  |  |  |  |  |
| practical bug detection: An llm-integrated approach. | Proceedings of | 2024 USENIX Annual Technical Conference (USENIX ATC 24) | (2024), |  |  |  |
| the ACM on Programming Languages 8 | , OOPSLA1 (2024), 474–499. | pp. 493–508. |  |  |  |  |
| [27] Li, P., Yao, S., Korich, J. S., Luo, C., Yu, J., Cao, Y., and Yang, J. | [46] Team, G., Anil, R., Borgeaud, S., Alayrac, J.-B., Yu, J., Soricut, R., |  |  |  |  |  |
| Automated static vulnerability detection via a holistic neuro-symbolic | Schalkwyk, J., Dai, A. M., Hauth, A., Millican, K., et al. Gem- |  |  |  |  |  |
| approach. | arXiv preprint arXiv:2504.16057 | (2025). | ini: a family of highly capable multimodal models. | arXiv preprint |  |  |
| [28] Li, T., Bai, J.-J., Han, G.-D., and Hu, S.-M. | { | LR-Miner | } | : Static race | arXiv:2312.11805 | (2023). |
| detection in | { | OS | } | kernels by mining locking rules. In | 33rd USENIX | [47] Wang, C., Liu, J., Peng, X., Liu, Y., and Lou, Y. Boosting static resource |
| Security Symposium (USENIX Security 24) | (2024), pp. 6149–6166. | leak detection via llm-based resource-oriented intention inference, |  |  |  |  |
| [29] Li, T., Bai, J.-J., Sui, Y., and Hu, S.-M. Path-sensitive and alias-aware | 2024. |  |  |  |  |  |
| typestate analysis for detecting os bugs. In | Proceedings of the 27th ACM | [48] Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowd- |  |  |  |  |
| International Conference on Architectural Support for Programming | hery, A., and Zhou, D. Self-consistency improves chain of thought |  |  |  |  |  |
| Languages and Operating Systems | (New York, NY, USA, 2022), ASPLOS | reasoning in language models. | arXiv preprint arXiv:2203.11171 | (2022). |  |  |
| ’22, Association for Computing Machinery, p. 859–872. | [49] Xia, C. S., Wei, Y., and Zhang, L. Automated program repair in the |  |  |  |  |  |
| [30] Li, Z., Dutta, S., and Naik, M. Llm-assisted static analysis for detect- | era of large pre-trained language models. | In | 2023 IEEE/ACM 45th |  |  |  |
| ing security vulnerabilities. | arXiv preprint arXiv:2405.17238 | (2024). | International Conference on Software Engineering (ICSE) | (2023), IEEE, |  |  |
| [31] Lin, M., Chen, K., and Xiao, Y. Detecting | { | API | } { | Post-Handling | } | pp. 1482–1494. |
| bugs using code and description in patches. In | 32nd USENIX Security | [50] Xia, C. S., and Zhang, L. Automated program repair via conversation: |  |  |  |  |
| Symposium (USENIX Security 23) | (2023), pp. 3709–3726. | Fixing 162 out of 337 bugs for $0.42 each using chatgpt. In | Proceedings |  |  |  |
| [32] Liu, J., Yi, L., Chen, W., Song, C., Qian, Z., and Yi, Q. LinKRID: Vetting | of the 33rd ACM SIGSOFT International Symposium on Software Testing |  |  |  |  |  |
| imbalance reference counting in linux kernel with symbolic execution. | and Analysis | (2024), pp. 819–831. |  |  |  |  |
| In | 31st USENIX Security Symposium (USENIX Security 22) | (Boston, MA, | [51] Yan, H., Sui, Y., Chen, S., and Xue, J. Spatio-temporal context reduc- |  |  |  |
| Aug. 2022), USENIX Association, pp. 125–142. | tion: a pointer-analysis-based static approach for detecting use-after- |  |  |  |  |  |
| [33] Lou, C., Jing, Y., and Huang, P. Demystifying and checking silent | free vulnerabilities. In | Proceedings of the 40th International Conference |  |  |  |  |
| semantic violations in large distributed systems. | In | 16th USENIX | on Software Engineering | (New York, NY, USA, 2018), ICSE ’18, Associa- |  |  |
| Symposium on Operating Systems Design and Implementation (OSDI 22) | tion for Computing Machinery, p. 327–337. |  |  |  |  |  |
| (2022), pp. 91–107. | [52] Yang, C., Deng, Y., Lu, R., Yao, J., Liu, J., Jabbarvand, R., and Zhang, |  |  |  |  |  |
| [34] Lou, C., Parikesit, D. S., Huang, Y., Yang, Z., Diwangkara, S., Jing, | L. Whitefox: White-box compiler fuzzing empowered by large lan- |  |  |  |  |  |
| Y., Kistijantoro, A. I., Yuan, D., Nath, S., and Huang, P. Deriving | guage models. | Proceedings of the ACM on Programming Languages 8 | , |  |  |  |
| semantic checkers from tests to detect silent failures in production | OOPSLA2 (2024), 709–735. |  |  |  |  |  |
| distributed systems. In | 19th USENIX Symposium on Operating Systems | [53] Yang, C., Deng, Y., Yao, J., Tu, Y., Li, H., and Zhang, L. | Fuzzing |  |  |  |
| Design and Implementation (OSDI 25) | (2025), pp. 19–38. | automatic differentiation in deep-learning libraries. In | 2023 IEEE/ACM |  |  |  |
| [35] Lu, K., Pakki, A., and Wu, Q. | Detecting Missing-Check bugs via | 45th International Conference on Software Engineering (ICSE) | (2023), |  |  |  |
| semantic-and Context-Aware criticalness and constraints inferences. | IEEE, pp. 1174–1186. |  |  |  |  |  |
| In | 28th USENIX Security Symposium (USENIX Security 19) | (2019), | [54] Yang, C., Li, X., Misu, M. R. H., Yao, J., Cui, W., Gong, Y., Hawblitzel, |  |  |  |
| pp. 1769–1786. | C., Lahiri, S. K., Lorch, J. R., Lu, S., Yang, F., Zhou, Z., and Lu, S. |  |  |  |  |  |
| [36] Lyu, Y., Fang, Y., Zhang, Y., Sun, Q., Ma, S., Bertino, E., Lu, K., and | Autoverus: Automated proof generation for rust code. | Proceedings of |  |  |  |  |
| Li, J. Goshawk: Hunting memory corruptions via structure-aware and | the ACM on Programming Languages 9 | , OOPSLA2 (2025). |  |  |  |  |
| object-centric memory operation synopsis. In | 2022 IEEE Symposium | [55] Yang, C., Zhao, Z., and Zhang, L. Kernelgpt: Enhanced kernel fuzzing |  |  |  |  |
| on Security and Privacy (SP) | (2022), IEEE, pp. 2096–2113. | via large language models. ASPLOS ’25, Association for Computing |  |  |  |  |
| [37] Mathai, A., Huang, C., Maniatis, P., Nogikh, A., Ivančić, F., Yang, | Machinery, p. 560–573. |  |  |  |  |  |
| J., and Ray, B. Kgym: A platform and dataset to benchmark large | [56] Zhai, Y., Hao, Y., Zhang, H., Wang, D., Song, C., Qian, Z., Lesani, |  |  |  |  |  |
| language models on linux kernel crash resolution. | Advances in Neural | M., Krishnamurthy, S. V., and Yu, P. Ubitect: a precise and scalable |  |  |  |  |
| Information Processing Systems 37 | (2024), 78053–78078. | method to detect use-before-initialization bugs in linux kernel. In |  |  |  |  |
| [38] Min, C., Kashyap, S., Lee, B., Song, C., and Kim, T. Cross-checking | Proceedings of the 28th ACM Joint Meeting on European Software En- |  |  |  |  |  |
| semantic correctness: The case of finding file system bugs. In | Pro- | gineering Conference and Symposium on the Foundations of Software |  |  |  |  |
| ceedings of the 25th Symposium on Operating Systems Principles | (2015), | Engineering | (2020), pp. 221–232. |  |  |  |
| pp. 361–377. | [57] Zhang, C., Liu, H., Zeng, J., Yang, K., Li, Y., and Li, H. | Prompt- |  |  |  |  |
| [39] Oracle. Kernel-Fuzzing. | https://github.com/oracle/kernel-fuzzing | . | enhanced software vulnerability detection using chatgpt. In | Proceed- |  |  |
| [40] Qi, Z., Long, F., Achour, S., and Rinard, M. An analysis of patch | ings of the 2024 IEEE/ACM 46th International Conference on Software |  |  |  |  |  |
| plausibility and correctness for generate-and-validate patch generation | Engineering: Companion Proceedings | (New York, NY, USA, 2024), ICSE- |  |  |  |  |
| systems. In | Proceedings of the 2015 international symposium on software | Companion ’24, Association for Computing Machinery, p. 276–277. |  |  |  |  |
| testing and analysis | (2015), pp. 24–36. | [58] Zhang, H., Chen, W., Hao, Y., Li, G., Zhai, Y., Zou, X., and Qian, |  |  |  |  |
| [41] Semgrep. Semgrep. | https://github.com/semgrep/semgrep | . | Z. Statically discovering high-order taint style vulnerabilities in os |  |  |  |
| [42] Shestov, A., Levichev, R., Mussabayev, R., Maslov, E., Zadorozhny, | kernels. In | Proceedings of the 2021 ACM SIGSAC Conference on Com- |  |  |  |  |
| P., Cheshkov, A., Mussabayev, R., Toleu, A., Tolegen, G., and | puter and Communications Security | (New York, NY, USA, 2021), CCS |  |  |  |  |
| Krassovitskiy, A. | Finetuning large language models for vulnera- | ’21, Association for Computing Machinery, p. 811–824. |  |  |  |  |

bility detection. IEEE Access 13 (2025), 38889–38900.

15

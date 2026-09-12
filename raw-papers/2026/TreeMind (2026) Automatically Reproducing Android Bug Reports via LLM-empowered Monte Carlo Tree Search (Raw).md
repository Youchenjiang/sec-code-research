---
title: "TreeMind: Automatically Reproducing Android Bug Reports via LLM-empowered Monte Carlo Tree Search"
author: "Zhengyu Chen; Zhaoyi Meng; Wenxiang Zhao; Wansen Wang; Wenchao Huang; Jie Cui; Hong Zhong; Yan Xiong"
creator: "arXiv GenPDF (tex2pdf:57610bf)"
pages: 21
---

# TreeMind: Automatically Reproducing Android Bug Reports via LLM-empowered Monte Carlo Tree Search

> **作者**：Zhengyu Chen; Zhaoyi Meng; Wenxiang Zhao; Wansen Wang; Wenchao Huang; Jie Cui; Hong Zhong; Yan Xiong
> **總頁數**：21 頁

---

## Page 1

TreeMind: Automatically Reproducing Android Bug Reports

via LLM-empowered Monte Carlo Tree Search

ZHENGYU CHEN, Anhui University, China

ZHAOYI MENG ∗ , Anhui University, China

WENXIANG ZHAO, University of Science and Technology of China, China

WANSEN WANG, Anhui University, China

WENCHAO HUANG, University of Science and Technology of China, China

JIE CUI, Anhui University, China

HONG ZHONG, Anhui University, China

YAN XIONG, University of Science and Technology of China, China

Automatically reproducing Android app crashes from textual bug reports is challenging, particularly when the

reports are incomplete and the modern UI exhibits high combinatorial complexity. Existing approaches based

solely on reinforcement learning or large language models (LLMs) exhibit limitations in such scenarios. They

struggle to infer unobserved steps and reconstruct the underlying user action sequences to navigate the vast

UI interaction space, primarily due to limited goal-directed reasoning and planning. We present TreeMind, a

novel technique that integrates LLMs with an adapted Monte Carlo Tree Search (MCTS) algorithm to achieve

strategic UI exploration in bug reproduction. To the best of our knowledge, this is the first work to combine

external decision-making with LLM semantic reasoning for reliable and accurate reproduction processes. We

formulate the reproduction task as a target-driven search problem, leveraging MCTS as the core planning

mechanism to iteratively refine action sequences. To enhance MCTS with semantic reasoning, we introduce

two LLM-guided agents with distinct roles: Expander generates top- k promising actions based on the current

UI state and exploration history, while Simulator estimates the likelihood that each candidate action leads

toward successful reproduction by additionally leveraging dynamic environment feedback. By incorporating

multi-modal UI inputs and tailored prompting strategies, TreeMind performs feedback-aware navigation that

identifies essential user actions and incrementally reconstructs reproduction paths. We evaluate TreeMind

on a dataset of 93 real-world Android bug reports from three widely-used benchmarks. Experimental results

show that it significantly outperforms four state-of-the-art baselines, including ReBL, ReActDroid, AdbGPT,

and ReproBot, in reproduction success rate. Ablation studies further demonstrate the effectiveness of each

proposed strategy. The evaluations indicate that integrating LLM reasoning with MCTS-based planning is a

compelling direction for automated bug reproduction.

1 Introduction

Mobile apps become an integral part of nearly every aspect of modern life. As reported by Statista,

over 2 million Android apps are currently available in the Google Play Store [1]. In this competitive

landscape, it is increasingly important for developers to ensure app quality through effective

arXiv:2509.22431v2 [cs.SE] 1 Feb 2026 maintenance and timely bug fixing. A widely cited survey indicates that 88% of app users would

abandon an app if they encountered bugs or glitches [2]. As a result, developers are expected to

identify and resolve these functionality issues promptly to retain users. To support this, bug reports

serve as a primary source of information to understand observed failures [3].

∗ Corresponding author

Authors’ Contact Information: Zhengyu Chen, zychen@stu.ahu.edu.cn, Anhui University, Hefei, Anhui, China; Zhaoyi Meng,

zymeng@ahu.edu.cn, Anhui University, Hefei, Anhui, China; Wenxiang Zhao, zhaowx98@mail.ustc.edu.cn, University

of Science and Technology of China, Hefei, Anhui, China; Wansen Wang, 23762@ahu.edu.cn, Anhui University, Hefei,

Anhui, China; Wenchao Huang, huangwc@ustc.edu.com, University of Science and Technology of China, Hefei, Anhui,

China; Jie Cui, cuijie@mail.ustc.edu.cn, Anhui University, Hefei, Anhui, China; Hong Zhong, zhongh@ahu.edu.cn, Anhui

University, Hefei, Anhui, China; Yan Xiong, yxiong@ustc.edu.com, University of Science and Technology of China, Hefei,

Anhui, China.

---

## Page 2

Zhengyu Chen, Zhaoyi Meng, Wenxiang Zhao, Wansen Wang, Wenchao Huang, Jie Cui, Hong Zhong, and Yan Xiong

To fix a reported crash, developers must first reproduce it based on the crash-triggering procedures

( e.g. , the sequence of user interactions) in the corresponding report. However, a major challenge

developers face is that the lack of critical details in bug reports substantially increases the complexity

of bug reproduction [4]. Not all submitters, i.e. , users who report crashes, follow the issue-reporting

instructions or provide detailed procedures for reproducing the crashes [5]. Without detailed

reproduction steps, developers must spend considerable time manually diagnosing the issues.

Many approaches have been proposed to automatically reproduce bug reports [6–9]. Specifically,

they extract entities from steps to reproduce ( i.e. , S2Rs) and then match them with the app UI

to replay the reported bug. However, it is non-trivial to accurately and completely extract S2Rs

from bug reports using natural language processing techniques. Meanwhile, explicitly matching

bug reports with the app’s UI elements may fail to capture reproduction steps that are omitted

from the reports. Moreover, the approaches based on dynamic exploration [7] or human-defined

heuristics [9] may suffer from high overhead and limited performance in practice.

Recent years have witnessed the emergence of various bug report reproduction methods based

on Large Language Models (LLMs) [3, 4, 10]. These methods rely on advanced capabilities of LLMs

to understand bug reports, analyze UI information of apps, and then drive the app exploration.

Although these methods outperform earlier approaches in terms of effectiveness and efficiency, a

critical problem remains unresolved: The combinatorial complexity of modern UIs and the incom-

pleteness of bug reports make LLM-only approaches inadequate for identifying viable reproduction

steps. Specifically, the growing complexity of current apps leads to a combinatorial explosion in

the number of possible UI interaction sequences. Meanwhile, the incompleteness of bug reports

often necessitates the exploration of a much broader set of potential interaction paths. Without

explicit guidance or external feedback, LLMs have limited capability in systematically exploring

and validating UI transitions, making them ill-suited for navigating the vast and uncertain interac-

tion space. While recent work [10] incorporates feedback to improve LLM decision-making, such

feedback provides limited support for global planning and tends to be locally reactive, which makes

the exploration process prone to compounding errors and resulting in less directed navigation.

Monte Carlo Tree Search (MCTS) has demonstrated remarkable reasoning and search capabilities

in various domains, e.g. , game playing [11] and automated planning [12]. It is an iterative tree-based

algorithm that effectively balances exploration and exploitation when searching large and complex

state spaces. This is accomplished through a four-stage process: selection, expansion, simulation,

and backpropagation, which incrementally refine the search toward satisfactory solutions. In our

context, reproducing Android bugs from natural language reports is a challenging search problem

in a vast and partially observable UI interaction space. It requires identifying a sequence of user

actions that can trigger the bug. However, due to the complexity of the space, such sequences are

often difficult to discover. Given MCTS’s strengths in navigating such environment, it is well-suited

for guiding this search process.

We propose and implement TreeMind, a novel technique for automatic reproduction of Android

bug reports via LLM-empowered MCTS. Our primary goal is to achieve accurate bug reproduc-

tion even in the presence of incomplete bug reports, under a reasonable time constraint. To this

end, TreeMind employs an adapted MCTS algorithm integrated with an LLM-based multi-agent

framework, enabling effective UI exploration. MCTS serves as the core planning mechanism for the

search aimed at triggering bugs. During each MCTS iteration, TreeMind progressively interprets

crash context and infer appropriate UI actions through LLM-guided agents enhanced with advanced

prompt engineering techniques. To further support more reliable reproduction decisions, TreeMind

leverages both textual ( e.g. , structured UI descriptions) and visual ( e.g. , UI screenshots) inputs as

complementary modalities for advanced LLMs.

---

## Page 3

TreeMind : Automatically Reproducing Android Bug Reports via LLM-empowered Monte Carlo Tree Search

There are two technical challenges in applying MCTS for our work: (i) When a bug report lacks

sufficient detail, the space of possible actions in certain UI states can become extremely large,

especially when the actions involve free-form text inputs or gestures with continuous parameters.

This makes it infeasible for MCTS to blindly expand the search tree from such states, often resulting

in inefficient UI exploration. (ii) Monte Carlo rollouts suffer from both the vast action space and the

interaction latency imposed by real-time UI feedback, which significantly slow down the simulation

process. Consequently, most rollouts fail to reach terminal states where the target bug is triggered

within a limited time budget, leading to suboptimal guidance during UI exploration.

To address the above challenges, we design two LLM-guided agents with distinct roles, i.e. ,

Expander and Simulator, which are respectively aligned with the expansion and simulation stages

in MCTS. For the first challenge, to avoid exploring the intractably large action space, the Expander

agent expands the top- k candidate actions that are most likely to reproduce the bug report according

to the current UI state and the exploration history. This strategy promotes more targeted exploration

by constraining the branching factor of the Monte Carlo search tree, striking a practical balance

between efficiency and effectiveness. For the second challenge, to overcome the difficulty of

obtaining reward signals through full rollouts, the Simulator agent directly estimates the likelihood

of reproducing the bug report, based on the context of UI exploration and each one-step look-ahead

rollout result from the expanded actions. This likelihood is transformed into a proxy reward, which

is backpropagated to guide future search decisions.

To evaluate the effectiveness of TreeMind, we perform comprehensive experiments on a real-

world dataset comprising 93 real-world Android bug reports from three widely-used benchmarks.

Compared to four state-of-the-art bug reproduction tools ( i.e. , ReActDroid [4], ReBL [10], Ad-

bGPT [3], and ReproBot [6]), TreeMind achieves the highest success rate of 64.52% success rate,

outperforming ReActDroid (45.16%), ReBL (40.86%), AdbGPT (34.41%), and ReproBot (31.18%). Abla-

tion studies further validate the contribution of each proposed strategy. The evaluations indicate

that integrating LLM reasoning with MCTS-based planning is a compelling direction for automated

bug reproduction. Our main contributions are summarized as follows:

(1) We present TreeMind, the first work, to the best of our knowledge, that combines external

decision-making with LLM semantic reasoning for goal-directed bug reproduction.

(2) Experimental results demonstrate that TreeMind significantly outperforms four state-

of-the-art Android bug report reproduction tools ( i.e. , ReActDroid, ReBL, AdbGPT, and

ReproBot) in reproduction success rate.

(3) We will make the implementation and dataset of TreeMind publicly available upon accep-

tance to facilitate future research work.

2 Motivation

Reproducing crashes in Android apps poses a persistent challenge, mainly due to incomplete bug

reports. To enhance the effectiveness of bug reproduction, many researchers have explored diverse

automated methods. For example, ReproBot [6] uses Q-learning to automate UI exploration, while

AdbGPT [3], ReBL [10], and ReActDroid [4] leverage LLMs to generate reproduction actions from

bug reports. Figure 1(a) illustrates the overall workflow of the LLM-based methods.

When bug reports omit essential execution steps, existing methods have difficulty generating

correct actions for reproducing target bugs. As exemplified at the top of Figure 1, the bug report

consists of only a single sentence instructing users to rotate the screen to trigger the crash of an

app named FakeStandby . However, as shown in Figure 1(b), this description omits two critical

interaction actions: (i) Clicking the "escape methods" option on the screen ( i.e. , Missing#1 ), and (ii)

rotating the screen while keeping the dialog open ( i.e. , Missing#2 ). These missing actions have

---

## Page 4

Zhengyu Chen, Zhaoyi Meng, Wenxiang Zhao, Wansen Wang, Wenchao Huang, Jie Cui, Hong Zhong, and Yan Xiong

Bug report content: App crashes when rotating the screen.

1. page_id :

2. page name:

Settings Activity

3. page actions:

Click[Visit the projects website]

Page Click[Escape methods]

information Click[Open accessibility settings]

...

extraction

No crash

Outputs

| LLM | Actions |
| --- | --- |
| Crash Reproduced | Click |

UI#1

Missing#1

Fig. 1. Motivating example

As the MCTS

output Module

Selection Expansion

Reproduction

... ... ... ... ... ... ... ...

In

prompts Select nodes according to a 1

source

APK File

Fig. 2. Overall architecture of TreeMind

| Rotate | × | N times | Incorrect action sequence |  |  |
| --- | --- | --- | --- | --- | --- |
| Rotate | Rotate |  |  |  |  |
| UI# | 2 | UI# | 3 | UI# | 4 |
| Missing#2 | Correct action sequence |  |  |  |  |

Iteration

| Simulation | Backpropagation |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ... | ... | ... |  |  |  |  |  |  |  |
| a | 2 | ... | a | k | a | 1 | a | 2 | a |
| ... | k | ... |  |  |  |  |  |  |  |
| Estimate action | e | 1 | e | 2 | e | k |  |  |  |
| Get promising | reproduction | Update visit counts and |  |  |  |  |  |  |  |

Action Execution Engine

| Settings Activity#0 | UI# | 1 | UI#5 | from LLM | - | based methods |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (a) Workflow of LLM | - | based methods | (b) Bug reproduction | details of | the | method | s |  |  |  |
| Result | 1 | 2 | 3 | e | 1 | e | 2 | e | k | 4 |
| Bug Report | Expander | top | - | k | actions | Simulator | likelihood | average rewards of nodes |  |  |
| Selected | Multi | - | modal | Candidate | Multi | - | modal | App restart |  |  |
| As the | actions | UI information | k | actions | UI information | command |  |  |  |  |

only a weak semantic connection to the bug report, making them difficult to infer by LLMs. In

this situation, ReproBot tends to repeat actions such as rotation in the early stages and gradually

broadens its search as negative feedback accumulates. AdbGPT, ReBL and ReActDroid try to rotate

the screen repeatedly, thereby causing continuous transitions between UI#1 and UI#5 along the red

arrows. Although ReActDroid introduces a novel crash localization mechanism, it still struggles to

identify the crashing page under such conditions. As a result, in our experiments, all these methods

fail to reproduce the crash within the given time constraints, i.e. , 30 minutes.

This limitation underscores the need for a more adaptive exploration mechanism that can infer the

missing user actions not explicitly mentioned in the bug report. Rather than gradually broadening

the search within the app or relying solely on LLM-generated suggestions, an effective solution

should systematically explore the interaction space while progressively exploiting more promising

interaction paths. We propose to integrate LLMs with MCTS. In this design, LLMs are used to

reason about plausible missing actions and evaluate their outcomes based on the context of the bug

reproduction process, while MCTS provides a structured decision-making process that discovers

diverse action sequences and refines the search toward the most likely reproduction path. This

synergy enables the recovery of essential actions, allowing reproduction from incomplete reports.

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

---

## Page 5

TreeMind : Automatically Reproducing Android Bug Reports via LLM-empowered Monte Carlo Tree Search

3 Methodology

3.1 Architecture

Figure 2 depicts the overall architecture of TreeMind. It is end-to-end, requiring users to provide a

bug report and an APK file. As a result, analysts without any knowledge of LLMs can conveniently

use the tool. The final output is an action sequence that precisely reproduces the reported bug, or a

message indicating that no bug is found. TreeMind consists of two main components:

(1) MCTS Module guides the searching of bug-triggering action sequences by orchestrating the

four stages of MCTS, i.e. , selection, expansion, simulation, and backpropagation. To balance ex-

ploitation and exploration during bug reproduction, we adapt the four stages around an LLM-based

multi-agent framework. Particularly, the two agents named Expander and Simulator respectively

leverage their analytical and reasoning capabilities during the expansion and simulation stages.

This enables them to understand the app’s runtime UI states and the context of bug reproduction.

Moreover, task-specific enhancements are introduced to improve computation strategies in both

selection and backpropagation. The module interacts with the Action Execution Engine to collect

various types of UI-related information that support the agents’ decision-making process.

(2) Action Execution Engine is an Android automation backend that enables programmatic

interaction with input apps by querying and manipulating UI elements for our reproduction tasks,

e.g. , screen traversal and event injection. Specifically, this component executes various commands

translated from LLMs’ responses in the MCTS Module, and delivers multi-modal UI information

( i.e. , textual descriptions and screenshots) to the LLM-guided agents of the module above.

3.2 LLM-empowered Monte Carlo Tree Search

We integrate an LLM-based multi-agent framework with MCTS to enable effective searching in the

large and complex state space of bug reproduction. The state space is modeled as a Monte Carlo

search tree, where each node represents a state during reproduction and each edge corresponds to

an input action that triggers the transition between the states. Here, a state refers to a snapshot of

an app’s UI at a specific point during its execution, including the screen layout, visible elements, and

their interactive properties. This integration forms a closed-loop and feedback-driven process, where

MCTS drives strategic and goal-directed searching, while LLM-guided agents provide high-level

semantic understanding of the reproduction context to support the decision-making of MCTS. By

leveraging incremental feedback, the agents help MCTS adjust its searching strategy dynamically.

To operationalize this integration, we introduce LLM-guided agents into the expansion and

simulation stages of MCTS, where high-level semantic reasoning and adaptive decision-making

are essential. Moreover, the selection and backpropagation, which primarily involve numerical

computations, are implemented without LLMs. Instead, we apply task-specific adaption for these

two stages to better support the requirements of bug reproduction.

3.2.1 Selection. Starting from the root node of a search tree representing the initial UI state,

we follow a path by recursively selecting child nodes based on a selection policy that balances

exploration and exploitation. In our MCTS-based framework, rewards derived from LLMs can be

imperfect due to their approximate and context-sensitive nature, which may cause the standard

Upper Confidence Bound (UCB)-based node selection [13] to prematurely favor suboptimal actions

and insufficiently visit alternative paths. To address this, we adopt a variant known as the softmax-

over-UCB strategy [14], which assigns selection probabilities to available child nodes based on their

UCB scores. This approach transforms deterministic UCB scores into a softmax-based probability

distribution, enabling stochastic yet guided selection that improves state space coverage and

mitigates premature convergence [15]. At each selection stage, TreeMind recursively traverses the

---

## Page 6

Zhengyu Chen, Zhaoyi Meng, Wenxiang Zhao, Wansen Wang, Wenchao Huang, Jie Cui, Hong Zhong, and Yan Xiong

search tree from the root, and samples expanded child nodes based on softmax-normalized UCB

scores, until it reaches a leaf or unexpanded node.

For a given child node 𝑖 , its UCB score is calculated as:

√︄

√ ln 𝑁

𝑈𝐶𝐵 𝑖 = 𝑋 𝑖 +  2 · (1)

𝑛 𝑖

, where 𝑋 𝑖 denotes the average reward of node 𝑖 , 𝑛 𝑖 is the number of times node 𝑖 has been visited,

√

𝑁 refers to the number of times the parent node has been visited, 2 is a constant chosen in

accordance with theoretical regret bounds derived using Hoeffding’s inequality [16].

Given a set of child nodes with UCB scores, i.e. , 𝑈 = { UCB 1 , UCB 2 , ..., UCB 𝑛 } , the selection

probability for the 𝑡 -th node is computed as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| UCB | − | ( | 𝑈 | ) |
| exp | 𝑡 | max |  |  |

𝜏

| 𝑃 | ( | 𝑡 | ) | = |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Í | (2) |  |  |  |  |  |  |
| 𝑛 | UCB | 𝑘 | − | max | ( | 𝑈 | ) |
| 𝑘 | = | 1 | exp | 𝜏 |  |  |  |

, where 𝜏 is a temperature parameter. It controls the smoothness of the resulting probability

distribution: Lower 𝜏 produces sharper preferences, while higher values yield more uniform proba-

bilities [17]. We conduct experiments with varying 𝜏 values and find that our method is relatively

insensitive to this parameter. Thus, we empirically fix 𝜏 = 1.8 as a stable default in all experi-

ments. Furthermore, the subtraction of max ( 𝑈 ) is for numerical stability to avoid overflow during

exponential computation.

The selected actions are sequentially fed into the Action Execution Engine for actual execution,

which then waits for the next action inputs at the subsequent simulation stage.

3.2.2 Expansion. This stage generates candidate actions for the search tree, enabling the exploration

of previously unvisited paths. However, standard MCTS expands only a single branch per iteration,

which can limit the efficiency of reproducing Android app bugs. Given the potentially high branching

factor in UI exploration, fully expanding all child nodes at each step may introduce a large number

of irrelevant actions that mislead the search process.

We introduce Expander, an LLM-guided agent designed to assist the expansion stage of MCTS

by selecting a moderate amount of promising actions for further UI exploration. At each expansion

step, the Expander agent queries the LLM using the ExpansionPrompt depicted in Section 3.3.

Instead of expanding a single action per iteration or fully expanding all possible actions at once,

the agent performs a top- k expansion strategy based on the LLM’s ranking of candidate actions.

Guided by semantic cues from the bug report and the reproduction context, the LLM suggests k

candidate actions most likely to progress toward the reproduction goal. To support this, the Action

Execution Engine retrieves the multi-modal UI information at the current unexpanded leaf node.

This strategy draws inspiration from beam search, a widely adopted heuristic in sequence

generation and planning tasks [18, 19]. Unlike arbitrary pruning, it leverages semantic relevance

to the reproduction goal to guide searching. Although some potentially useful actions may be

omitted, the trade-off is deliberate and controlled. Experimental results in Section 4 show that this

strategy leads to effective reproduction performance, suggesting that the benefits of focused and

semantically guided exploration outweigh the occasional risk of missing critical actions in practice.

3.2.3 Simulation. At this stage, TreeMind estimates the potential of each expanded candidate

action to contribute to a successful reproduction, providing a value signal to guide subsequent

decision-making in the MCTS process. The stage also adds new state nodes into the search tree.

Since bug reproduction often requires long sequences of UI interactions and each step in the

---

## Page 7

TreeMind : Automatically Reproducing Android Bug Reports via LLM-empowered Monte Carlo Tree Search

sequence presents numerous possible actions, this leads to a combinatorial explosion in the number

of candidate simulated paths. Moreover, unlike playing Go [11, 20], operating an app’s UI in the

real environment to find the termination state that triggers the reported bug faces two difficulties:

(i) The search space is vast and bug-triggering states are sparse, limiting the feedback available

within a finite number of interactions, and (ii) executing certain UI actions incurs high latency due

to animations, loading delays, and system response times. As a consequence, exhaustive strategies

like standard Monte Carlo rollouts are computationally infeasible within a practical time budget.

We design an LLM-guided agent named Simulator, which performs lightweight simulation by

estimating the potential of candidate actions to the bug reproduction goal, without executing full

interaction paths. The Simulator agent queries the LLM using the SimulatePrompt that will be

also presented in Section 3.3, following the LLM-as-a-Judge paradigm, which has been shown

effective in numerous tasks [21]. This paradigm enables context-aware and semantically grounded

evaluations without requiring task-specific supervision.

For each of the action, the Simulator agent executes it in the runtime environment using the

Action Execution Engine ( i.e. , one-step look-ahead rollout), and observes the resulting UI transitions.

For each UI transition, the agent invokes the LLM to assess how closely it aligns with the expected

behaviors described in the bug report and assign a heuristic score. This assessment also takes into

account the reproduction context accumulated along the current path in the search tree. The output

score is constrained to the range [0,10] through prompt engineering, as described in Section 3.3.

To ensure independent simulation of each action, TreeMind employs a UI state recovery mecha-

nism that restores the app to the parent node’s state after each simulation. It records the selected

actions during expansion and thus maintains the full action sequence from the root to each expanded

node. This enables TreeMind to restart the app and replay the recorded actions to accurately recon-

struct the corresponding UI state. The mechanism is implemented by sending the corresponding

commands to the Action Execution Engine.

3.2.4 Backpropagation. TreeMind leverages the outcomes of the simulation stage to update the

statistics of nodes along the current search path. Specifically, the visit count of each node is

incremented by 1, and the average reward of each node is updated using the mean of the simulation

scores of the k newly-expanded nodes. These updates refine the UCB scores of the corresponding

nodes, directly influencing action selection in the subsequent MCTS process.

After backpropagating the score up the tree, the UI state of the target app is restored to the root

node of the search tree using the recovery mechanism introduced in Section 3.2.3, preparing it for

the next iteration of MCTS.

3.3 Prompt Design

Prompt engineering plays a crucial role in enabling LLM-guided agents to understand contextual

information and effectively reproduce bugs in Android apps. Existing techniques have proposed

various prompts for bug reproduction [3, 4, 10]. However, these prompts cannot be directly applied

to our work, since they are not designed to integrate with external planning strategies ( e.g. , MCTS),

which are crucial for achieving the UI state space exploration.

To overcome the limitation, we design two sets of role-specific prompts, i.e. , ExpandPrompt

and SimulatePrompt listed in Table 1, to enable seamless integration of general-purpose LLMs

into our workflow. Note that the prompts shown in the table are simplified versions. In real-world

scenarios, they are typically longer and include more contextual information. Specifically, these

prompts instantiate LLMs as domain-aware agents, aligned with the expansion and simulation

stages of the MCTS process respectively. To improve the agents’ ability to perform complex tasks

and support downstream decision-making, we apply advanced prompt engineering techniques,

---

## Page 8

Zhengyu Chen, Zhaoyi Meng, Wenxiang Zhao, Wansen Wang, Wenchao Huang, Jie Cui, Hong Zhong, and Yan Xiong

Table 1. Prompt examples for two distinct roles

| Component | ExpandPrompt | SimulatePrompt |
| --- | --- | --- |
| Task specification | Movitation: | Motivation: |

You are an expert Android UI tester assisting me in Suppose you are an expert in reproducing Android

reproducing bug reports on an emulator...You need bugs, and your goal is to assess whether a specific

to provide me with three suggested actions that have action — referred to as the target action — is a valid

the highest likelihood of reproducing the bug report. and appropriate action toward completing the bug

Input specification: report, and then assign a score to that action...

I will provide the app name, the bug report text, a Input specification:

description of the current screen layout and state I will provide you with the bug report I am work-

and the srceenshot of the current UI page...and we ing to reproduce, along with the reproduction path

| will repeat this cycle until the bug reproduces... | I have followed so far and the corresponding UI in- |
| --- | --- |
| Output restriction: | formation for each action in that path. After that, I |

You need to provide me with k suggested actions will give you the target action...

that have the highest likelihood of reproducing the Output restriction:

bug report...Your suggestions should be formatted Your response format must be as follows: Score: 0–10.

as follows: [{"action": "x1", "feature": "y1"}, {"action": For example, if you intend to return a score of 5, your

| "x2", "feature": "y2"}, ...]. | reply should contain exactly ’Score: 5’... |  |  |
| --- | --- | --- | --- |
| Few-shot learning | Example 1: | Example 1: |  |
| App name: | Alarmio | Bug report: | When trying to log in, pressing the |

Bug report: The app gets crashes when I click about "Sign In" button does nothing.

| & OSS licenses | Previous page: | Showing a login screen with email |  |
| --- | --- | --- | --- |
| UI Information | : | and password fields and a "Sign In" button. |  |
| Activity: | .activities.MainActivity. | History: | Action sequence + Current UI screenshot |
| Groups: | ["Alarms"] , ["Settings"], ... | Target action: | Click the "Sign In" button. |

History: Action Sequence + Current UI Screenshot Result: The button is clearly relevant to the bug

Reasoning: report and is the correct next action.

The bug report explicitly instructs to click "about Score: 9

& OSS licenses". However, scanning the current UI Example 2:

groups, this specific widget is NOT present on the Bug report: When scrolling down in the article list,

screen. We cannot execute the trigger directly. Based some items disappear.

on standard Android design patterns, "About" and Previous page: Article list screen.

"OSS Licenses" information is almost always nested Target action: Click the "Back" button.

| inside the Settings menu. | History: | Action sequence + Current UI screenshot |
| --- | --- | --- |
| Suggestions: | Result: | This action does not move toward reproduc- |
| 1. {’action’: ’click’, ’feature’: ’SETTINGS’} | ing the scrolling bug. |  |
| 2. {’action’: ’click’, ’feature’: ’+’} | Score: | 2 |

3. {"action":"scroll","feature":"down"}

Chain-of-thought When generating suggestions: When scoring:

1. Identify if the target widget mentioned in the bug 1. Read the bug report carefully to identify the core

report is directly visible in the current UI. triggering action or condition.

2. If visible → Suggest clicking it as first priority . 2. Compare the target action with the bug report

3. If not visible → Decide if scrolling is likely to goal: Does it directly interact with the suspected

reveal it . element or trigger? Does it logically advance toward

4. If still missing → Systematically explore all first- reproducing the bug?

| level widgets. | 3. Check the UI change (before vs after action)... |
| --- | --- |
| ... | 4. Assign score... |

namely few-shot learning [22] and chain-of-thought reasoning [23]. These techniques not only

enable LLMs to perform modular task decomposition and multi-step reasoning, but also provide

structured instructions and ensure consistent output formatting.

3.3.1 Task Specification. While LLMs possess general reasoning capabilities, they often lack the

task-specific focus required for bug reproduction. We design role-specific instructions that specialize

LLMs into dedicated agents. As listed in the second row of Table 1, we use tailored prompting

---

## Page 9

TreeMind : Automatically Reproducing Android Bug Reports via LLM-empowered Monte Carlo Tree Search

strategies for each agent’s responsibilities, enabling general LLMs to emulate the behavior of

different experts for automated bug reproduction.

The motivation prompts are designed to clearly define the LLMs’ roles and objectives, guiding its

behavior in our task. They explicitly instruct LLMs not only to execute the reproduction steps, but

also to observe and confirm whether the specific buggy behavior described in the input report is

actually triggered. This goal enhances both the reliability and accuracy of the reproduction process.

To help the LLM-guided agents interpret the environment, we provide well-structured input

specifications that encode both textual and visual information about the app and its UI. Specifically,

the input includes the app name, the textual bug report, the structured description of the visited UI

components, and the current UI screenshot. The descriptive UI information extracted from XML

files of app pages provides structured and semantic details ( e.g. , widget hierarchy), whereas the

screenshots capture visual and spatial context. Together, they offer complementary perspectives to

better understand the screen’s functional layouts and their spatial relationships.

To enable deterministic parsing, we define a structured output format for each prompt type. This

guarantees consistent communication with downstream components and significantly reduces

integration errors from verbose or inconsistent outputs. In the ExpandPrompt, LLMs are required

to generate k most probable actions for successful bug reproduction and calculate their coordinates

in a single response, adhering to the strict JSON-like format ( e.g. , {"action": "x1", "feature": "y1"} ), as

illustrated in Table 1. Inspired by the action format in ReBL, we restrict the output to six predefined

actions: click , long_click , set_text , multiple_select , rotate , and back . This prompt-based action gener-

ation format is used during the expansion stage of our MCTS process. For the SimulatePrompt,

LLMs are prompted to output a numerical score in a fixed format. This ensures compatibility with

the backpropagation stage in MCTS.

3.3.2 Few-shot Learning. A representative example helps the LLM elicit specific knowledge and ab-

stractions needed to complete the downstream task. To construct the few-shot examples for guiding

the LLM, we follow the methodology in AdbGPT [3] and invite five experienced participants to help

identify challenging cases. Specifically, three developers collaboratively construct representative

examples that guide the model in handling realistic and non-trivial scenarios, and highlight its

reasoning process, especially when bug reports lack key reproduction steps. This construction

is grounded in real-world bug reports from our dataset. To further ensure quality and domain

relevance, we also invite two professors with expertise in Android crash reproduction to join the

process. All five participants engage in extensive discussions and ultimately reach a consensus

on the final set of eight representative examples used during reproduction, four pertaining to

ExpandPrompt and four to SimulatePrompt.

As shown in the third row and and second column of Table 1, the ExpandPrompt enables LLMs

to learn real-world crash reproduction patterns via few-shot demonstrations. It teaches the LLM

not only to generate promising actions in a structured format, but also to reason about missing

steps. When a UI element mentioned in the bug report is not present on the current page, the

ExpandPrompt guides the LLM to infer the most plausible action to reach the intended UI page. For

example, in the few-shot instance from Table 1, the target element about & OSS licenses is missing.

Through demonstration, the LLM learns to generate the action click "Settings" instead, based on its

relevance to the bug report.

In the SimulatePrompt, the examples illustrate how to score a target action based on the current

UI state and exploration history. The third row and third column of Table 1 lists two contrasting

examples that highlight the difference between high- and low-scoring actions. In the first example,

the bug report exactly matches the target action, indicating that it should receive a very high

---

## Page 10

Zhengyu Chen, Zhaoyi Meng, Wenxiang Zhao, Wansen Wang, Wenchao Huang, Jie Cui, Hong Zhong, and Yan Xiong

score. Conversely, the second example presents a target action that likely deviates from the correct

reproduction sequence, and should therefore receive a low score.

3.3.3 Chain-of-thought Reasoning. We adopt chain-of-thought (CoT) reasoning to encourage step-

by-step thinking, helping LLMs articulate intermediate steps explicitly, resolve ambiguity, and

produce more consistent and interpretable outputs in bug reproduction scenarios. Here, we also

follow the methodology in AdbGPT [3] by asking the three developers mentioned in Section 3.3.2

to provide chain-of-thought reasoning for our UI exploration task.

As shown in the fourth row of Table 1, CoT reasoning is used to guide LLMs through intermediate

reasoning steps in domain-specific bug reproduction cases. For example, in the ExpandPrompt,

we distill a set of reasoning strategies to help LLMs generate and evaluate candidate actions,

increasing the likelihood of successful reproduction. In the SimulatePrompt, we provide structured

and step-by-step reasoning guidance for LLMs to assess and score target actions reliably.

4 Experimental Evaluation

To evaluate the effectiveness of TreeMind, we seek to answer the following three questions:

• RQ1: How does TreeMind compare to state-of-the-art methods in bug report reproduction?

• RQ2: How do each proposed strategy contribute to the overall effectiveness of TreeMind?

• RQ3: What is the optimal k for the expansion stage in MCTS?

4.1 Experimental Setup

4.1.1 Implementation. We implement a prototype of TreeMind in Python. Specifically, we use

an Android virtual device to install and run apps, and employ UI Automator2 [24] to drive their

execution according to the input actions. We then extract the textual information about apps’

UI using the off-the-shelf implementation of ReBL. Besides, we leverage the GPT-4o [25] model 1

provided by OpenAI to support the understanding and reasoning over textual descriptions and

images. Following the configuration in ReBL, we set the temperature of the LLM to 0.3 to reduce

randomness and ensure more deterministic outputs.

4.1.2 Dataset. To avoid potential bias and ensure representativeness, we collect 93 real-world

textual crash reports and the relevant APKs from three existing open-source datasets released by

ReActDroid (22 out of 76) [4], ReproBot (66 out of 76) [6], and AndroR2 (5 out of 90) [5] respectively.

We refine the original datasets by excluding duplicate reports and those associated with non-

installable APK files. Specifically, duplicate reports include 4 between AndroR2 and ReproBot, 22

within ReActDroid, and 5 between AndroR2 and ReActDroid. Installation failures include 81 in

AndroR2, 27 in ReActDroid, and 10 in ReproBot.

4.1.3 Baselines. To evaluate the effectiveness of TreeMind, we select four state-of-the-art methods

for reproducing bug reports of Android apps:

• ReBL [10] is a feedback-driven technique that uses the complete textual bug report and

innovative prompts to automatically reproduce bugs of Android apps.

• ReActDroid [4] is an LLM-based approach for reproducing crashes of Android apps from

one-sentence overviews, by leveraging novel prompts to derive exploration steps.

• AdbGPT [3] is the first work to utilize prompt engineering with few-shot learning and

chain-of-thought reasoning to harness LLMs’ knowledge for automated bug replay.

• ReproBot [6] designs a NLP-based analysis to extract reproduction steps from Android bug

reports, and finds the match between steps and UI events by reinforcement learning (RL).

1 Version: gpt-4o-2025-03-26

---

## Page 11

TreeMind : Automatically Reproducing Android Bug Reports via LLM-empowered Monte Carlo Tree Search

Table 2. Comparison of TreeMind and baselines on bug reproduction ( RCRs = Reproduced Complete Reports,

RIRs = Reproduced Incomplete Reports)

| Metric | TreeMind | ReActDroid | ReBL | AdbGPT | ReproBot |
| --- | --- | --- | --- | --- | --- |
| Success rate (%) | 64.52 | 45.16 | 40.86 | 34.41 | 31.18 |
| # of RCRs | 30 | 21 | 23 | 20 | 16 |
| # of RIRs | 30 | 21 | 15 | 12 | 13 |
| Time cost (s) | 241.4 | 87.5 | 123.4 | 152.7 | 827.2 |
| Token usage | 183,163 | 125,548 | 158,245 | 138,641 | - |

Note that we use the same version of GPT-4o across all three LLM-based tools to ensure fairness.

4.2 RQ1: Effectiveness and Efficiency of TreeMind

To compare the effectiveness and efficiency of our approach against the baselines, we test each

collected bug report along with its corresponding APK on TreeMind and each selected baseline.

This process is repeated five times for each technique, with a time limit of 30 minutes per run.

A bug is considered successfully reproduced if at least one of the five runs succeeds. Among the

successful attempts, we record the shortest reproduction time as the final time cost.

4.2.1 Effectiveness. The second row of Table 2 presents the success rate of reproducing bug reports

from our collected dataset. Overall, TreeMind reproduces 64.52% of the reports (60 out of 93),

significantly outperforming the baslines: ReActDroid by 42.9%, ReBL by 57.9%, AdbGPT by 87.5%,

and ReproBot by 106.9%. Moreover, TreeMind successfully reproduces 30 RCRs and 30 RIRs. In

comparison, ReActDroid, ReBL, AdbGPT, and ReproBot reproduced 21/21, 23/15, 20/12, and 16/13

RCRs/RIRs, respectively. Here, a report is considered incomplete if, at any UI state, it fails to specify

an unambiguous action that leads to the next UI state. We manually inspect each report in our

dataset and record the counts of RCRs and RIRs above.

The superior performance of TreeMind can be mainly attributed to its integration of an external

planning strategy ( i.e. , MCTS) with LLM semantic reasoning. LLMs excel at interpreting both

textual and visual information to generate context-aware actions, while MCTS guides the searching

toward more promising directions. This integration enables TreeMind to reproduce bugs more

effectively, even when given incomplete reports. In contrast, the techniques that relying solely on

LLMs [3, 4, 10] are primarily reactive and may struggle with long-horizon planning. The RL-based

approach [6] faces difficulties when handling tasks that require semantic understanding, cross-task

generalization, and adaptive reasoning.

Analysis of Failure Cases. While TreeMind performs well in most cases, some crashes remain

difficult to reproduce due to limitations that are common across automated tools [4, 10]. Among

the 33 failed cases, we identify three major causes: (i) missing critical details in the bug report (27

cases), (ii) third-party service dependencies (5 cases), and (iii) UI Automator2 limitations (1 case).

First, incomplete bug reports often hinder effective UI exploration. For instance, in the app

named Markor-1565 , the report states that the app crashes " after rotating the note to landscape or

back to portrait ". TreeMind runs for over 30 minutes without success. Manual attempts also fail,

suggesting that key interactions are missing or not clearly specified.

Second, as noted in ReBL, crashes involving third-party services pose challenges for automated

tools. In the app named yakusu-35 , the reproduction requires navigation to Google and selection of

a specific account. Under such circumstances, TreeMind fails to reproduce the crash.

---

## Page 12

Zhengyu Chen, Zhaoyi Meng, Wenxiang Zhao, Wansen Wang, Wenchao Huang, Jie Cui, Hong Zhong, and Yan Xiong

Third, the limitations of UI Automator2 affect both UI extraction and action execution, as also

noted in ReBL. In the app named Memento-169 , the tool fails to extract custom views from the

UI hierarchy and cannot accurately locate the date picker dialog, resulting in imprecise clicks

instead of accurately scrolling to the targeted item. Although TreeMind successfully triggers the

crash, further analysis shows that it stems from an unintended interaction: The appearance of the

on-screen keyboard shifts the UI layout, causing a misclick that inadvertently reproduces the bug.

Comparative Case Analysis. To further demonstrate effectiveness, we compare TreeMind with

ReActDroid and ReBL on representative cases. We identify three instances where TreeMind fails

but ReActDroid succeeds. The failures are caused by incorrect path scoring during early exploration

( i.e. , yakusu-1 ), excessive search time due to long reproduction paths ( i.e. , saner2022-1299 ), and

difficulties in handling a multi-step login interface ( i.e. , saner2022-129 ). In contrast, ReActDroid

successfully handles all three cases, benefiting from GUI pre-processing and well-tailored prompts.

Furthermore, we identify two instances ( i.e. , saner2022-23 and saner2022-271 ) where TreeMind

fails while ReBL succeeds. These failures stem from TreeMind’s use of MCTS-based planning,

during which certain UI pages appear only once in the entire app execution. Since these pages

are essential for reproducing the bugs but cannot be revisited, the reproduction ultimately fails.

Reinstalling the apps after each MCTS iteration could resolve these issues, but would significantly

increase the overall runtime.

Conversely, TreeMind successfully reproduces bugs in 20 and 24 cases where ReActDroid and

ReBL fail, respectively. These successes are largely attributed to our LLM-empowered MCTS, which

effectively narrows down the search space and progressively guides the tool toward the correct

sequence of actions, even in the absence of critical steps in the crash report. As shown in Figure 1,

where ReActDroid and ReBL repeatedly rotate the screen until timeout, whereas TreeMind, guided

by MCTS and the LLM, identifies the correct reproduction path within a few iterations. In the case

of recdroid-56 , although the bug report contains a complete sequence of actions, both ReBL and

ReActDroid fail to reproduce the crash. In contrast, TreeMind successfully reproduces the bug.

Our success is attributed to the MCTS iterations, during which the context leading to the bug is

reconstructed. We elaborate on this process in Section 4.2.3 below.

These results suggest that combining the strengths of TreeMind and other advanced tools ( e.g. ,

ReActDroid and ReBL) has the potential to improve automated bug reproduction.

4.2.2 Efficiency. As shown in the third row of Table 2, our tool takes an average of 241.4 seconds

per successful reproduction, with the time ranging from 13 to 1095 seconds depending on the

specific bug. On average, the tool queries the LLM approximately 18.75 times per bug. This time

consumption is relatively higher than that of the LLM-based baseline tools, primarily due to

the multi-round planning process adopted by TreeMind. ReActDroid demonstrates the shortest

execution time among all the tools mentioned above, with only 87.5 seconds. ReproBot takes the

longest time, 827.2 seconds, which may be attributed to both the S2R matching process and the

convergence time required by the RL algorithm.

Although TreeMind incurs higher time costs, its ability to reproduce a wider range of bugs

justifies the efficiency trade-off, particularly in scenarios where reliability and reproduction success

take precedence over speed. When considering the total time spent across all test cases, regardless

of timeout or success, TreeMind proves to be the fastest overall due to the highest success rate.

In terms of token usage and dollar cost, TreeMind consumes the most tokens (183,163) with an

estimated cost of $0.45 per successfully reproduced bug. This is primarily due to the longer time

required to successfully reproduce a bug, and each MCTS iteration involves both textual and visual

inputs to the LLM. ReActDroid is the most cost-efficient, using 125,548 tokens ($0.22), followed by

---

## Page 13

TreeMind : Automatically Reproducing Android Bug Reports via LLM-empowered Monte Carlo Tree Search

UI# 1

Action= Action=click Action=

rotate screen "escape methods" scroll down

(P=0.42) (P=0.32) (P=0.26)

Other

State UI# 2 Other

State

Action=

... rotate screen … …

(P=0.87) ...

(P=0.03) (P=0.10)

UI# 3 Other Other

State State

Action Action Action

=rotate = click = click

screen " confirm " " cancel "

UI# 4 Crash

reproduced

(a) Changes in visit counts during MCTS (b) Changes in visit probability during MCTS (c) Tree structure at bug reproduction

Fig. 3. MCTS Statistics for reproducing the real-world bug shown in Figure 1 using TreeMind

ReBL (158,245 tokens, $0.25) and AdbGPT (138,641 tokens, $0.24). ReproBot does not rely on LLMs

and thus incurs no token-related cost.

4.2.3 Real-world Case Studies. We select two representative cases to demonstrate the advantages

of TreeMind. One of the bug reports omits essential actions needed to reproduce the bug ( i.e. , Case

1 ), while the other includes a complete and accurate sequence of actions ( i.e. , Case 2 ).

Case 1. In our experiment, none of the baselines described in Section 4.1.3 are able to solve the

real-world case presented in Section 2 within 30 minutes. By contrast, TreeMind provides an

effective and systematic approach for reproducing the crash triggered by screen rotation. The entire

reproduction process takes 3 minutes and 41 seconds. Since MCTS is an iterative process involving

multiple rounds of updates, as shown in Figure 3, we show how TreeMind solves the case by

analyzing the details stored in the search tree. Note that the figure illustrates only one possible way

in which TreeMind reproduces the bug. In practice, TreeMind can reproduce the bug through

different action sequences.

As shown in Figure 3(a), during the first three iterations of MCTS, the average visit count of nodes

along the bug-reproducing path remains low and unchanged, while other nodes are visited more

frequently, peaking at iteration 3. In iteration 4, the average visit count for the bug-reproducing

path increases sharply, whereas that of the other nodes declines. This suggests that the search

initially explores suboptimal paths, but gradually shifts focus toward the correct path as more

information becomes available.

As shown in Figure 3(b), the average softmax probability of the bug-reproducing path starts

very low but increases steadily across MCTS iterations, reaching 0.60 at iteration 4. In contrast, the

probability assigned to other paths consistently decreases from 0.48 to 0.20. This trend indicates that

the search gradually learns to assign higher confidence to the correct path, improving its ability to

prioritize promising actions over time. In other words, actions on the bug-reproducing path initially

have low UCB scores and visit probabilities. Instead of greedily selecting the highest-UCB action,

TreeMind applies softmax-over-UCB sampling to explore low-probability actions and eventually

converge to the correct path.

As depicted in Figure 3(c), TreeMind successfully triggers the bug along the blue-highlighted

path. The reproduction process starts from the app’s initial screen ( i.e. , UI#1), where three candidate

actions are expanded: rotate screen , click "escape methods" , and scroll down . TreeMind selects the

action click "escape methods" , transitioning to UI#2 with a probability of 32%. From there, it executes

rotate screen , leading to UI#3 with a probability of 87%. Finally, another rotate screen action leads to

UI#4, where the crash is reproduced. Note that the transition probability from UI#3 to UI#4 is not

---

## Page 14

Zhengyu Chen, Zhaoyi Meng, Wenxiang Zhao, Wansen Wang, Wenchao Huang, Jie Cui, Hong Zhong, and Yan Xiong

1 2 3

Bug report content

4

Step1: open Menu .

Step2: select Settings .

Step3: select About . Step1 Step2 Step3 Step4

Step4: select Google Play

listing.

| 1 | 2 | 3 |
| --- | --- | --- |
| 1 | Execution order | 4 |

By baseline tools

5 6 7 8

By TreeMind

UI#1 UI#2 UI#3 UI#4 App Crashes

Fig. 4. TreeMind vs. baseline tools: A representative case with complete action sequences from the bug report

Table 3. Ablation study of TreeMind

| Metric | Original | w/o | PE | w/o | IG | w/o | TK | w/o | SI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Success rate (%) | 64.52 | 47.31 | 45.16 | 26.88 | 36.56 |  |  |  |  |
| Time cost (s) | 241.4 | 429.0 | 345.6 | 323.4 | 335.9 |  |  |  |  |

shown, as this action is directly executed during the expansion stage, rather than being sampled

via the softmax-over-UCB strategy at the selection stage.

This case shows the advantage of combining MCTS’s exploratory planning with LLM’s semantic

reasoning. Even when critical steps are missing from the report, our tool can effectively recover

them and reconstruct the complete crash-inducing sequence. Although other baseline tools do not

reproduce this bug within 30 minutes in our experiments, this may be due to factors such as the

randomness of LLM outputs. With more attempts or extended time, they might still succeed.

Case 2. As explained in Section 4.2.1, the case of recdroid-56 is not successfully reproduced by

ReActDroid and ReBL within 30 minutes in our experiment. Upon closer inspection, we find that

although the bug report provides a complete sequence of actions to be executed, it omits critical

contextual information required for reproduction. Specifically, this bug is triggered only when the

same sequence of actions is executed multiple times, making it different from typical cases where a

single execution is sufficient to reproduce crashes.

As depicted in Figure 4, the bug can be reproducible by following the hollow arrows in the center,

which correspond directly to the steps listed in the top-left bug report. However, the baseline tools

do not trigger the crash after selecting Google Play listing at UI#4. Instead, the app returns to UI#1

along the red dashed arrows. Since these tools have already executed the actions described in the

report once without observing a crash, they tend to stop further exploration along this path and

instead switch to exploring alternative paths.

In contrast, TreeMind employs an iterative MCTS process that naturally re-executes promising

action sequences across iterations ( i.e. , the blue dashed arrows). Specifically, in an earlier MCTS

iteration, our tool first executes Steps 1 through 4 as described in the bug report, driving the app

to UI#3 and then back to UI#1. In the subsequent MCTS iteration, our tool restarts from UI#1

and re-executes Steps 1 through 4 to continue the UI exploration, successfully triggering the bug.

Interestingly, the repeated execution reconstructs the required app context.

4.3 RQ2: Contribution of Each Proposed Strategy

We conduct ablation studies to systematically evaluate the impact of individual strategy on the

effectiveness and efficiency of TreeMind by comparing it against a fully functional version. We use

*[Image: Page 14 Image]*

*[Image: Page 14 Image]*

*[Image: Page 14 Image]*

*[Image: Page 14 Image]*

---

## Page 15

TreeMind : Automatically Reproducing Android Bug Reports via LLM-empowered Monte Carlo Tree Search

UI Information extracted by ReBL :

switch_widget has the following group(s):

1#.[{'NAF': '[0,691][1080,926]'},' Automatically refresh '];

2#.[ ' WiFi sync only' ];

| Our tool treats | (a) | Switch is on |  |
| --- | --- | --- | --- |
| the two visually | UI Information extracted by | ReActDroid | : |
| different screenshots | INFO:tool.observe | : |  |
| as | distinct | page actions: |  |

Click[INFO], Click[REFRESH], Click[Debug mode],

Click[ Automatically refresh ], Click[Refresh rate]...

Each of the representative tools treats the screenshots as

identical based on the extracted textual UI information

(b) Switch is off

Fig. 5. Comparison of UI semantic understanding via textual information and screenshots

all bug reports in the datasets for the experiments. Other experimental settings remain consistent

with those described in Section 4.2. Specifically, we construct four ablations:

• w/o PE excludes the few-shot learning and chain-of-thought reasoning.

• w/o IG does not input UI screenshots into LLMs.

• w/o TK outputs all possible actions without querying the LLM for top- k candidates.

• w/o SI adopts the standard Monte Carlo rollout strategy.

Table 3 presents the experimental results, demonstrating that our original version with full

functions outperforms the alternative versions in both detection effectiveness and efficiency.

w/o PE achieves an overall success rate of 47.31%, 17.21% lower than the original version, and

takes 429.0 seconds on average to reproduce a bug report, approximately 1.57 × longer. These results

indicate that removing prompt engineering significantly degrades reproduction performance. The

lack of task-specific guidance and step-by-step reasoning hinders contextual understanding and

leads to lower success rates and longer execution times.

w/o IG achieves an overall success rate of 45.16%, which is 19.36% lower than the original version,

and requires an average of 345.6 seconds to reproduce a bug report, approximately 1.26 × longer.

These results highlight the importance of UI screenshots. Without visual context, the tool relies

solely on XML-based UI descriptions, which often lack critical visual cues. This limitation weakens

the tool’s ability to understand UI semantics, resulting in reduced reproduction effectiveness. As

illustrated in Figure 5, in the app named LibreNews , the screenshot-disabled version of TreeMind

and two representative tools ( i.e. , ReBL and ReActDroid) fail to distinguish whether the " Automati-

cally refresh " switch is on or off, because the XML-based UI information is identical across both

states. Consequently, they repeatedly click the same switch until the timeout is reached in our

experiment. In contrast, the visual difference in the screenshots allows TreeMind to identify the

correct state, and thus turn off the switch once and avoid redundant actions. While the inability to

perceive a UI state does not always prevent bug reproduction for existing tools, this case shows

that misinterpreting the UI can lead to incorrect behavior and ultimately reproduction failure.

w/o TK achieves a 26.88% success rate, 37.64% lower than the original version, and takes 323.4

seconds on average to reproduce a bug, approximately 1.18 × slower. This variant exhibits the lowest

success rate among all four ablation settings. Even when some bugs are reproduced, it requires

more time. These results suggest that the absence of a limit on the number of expanded child nodes

may lead to a search space explosion, which in turn hinders timely bug reproduction.

---

## Page 16

Zhengyu Chen, Zhaoyi Meng, Wenxiang Zhao, Wansen Wang, Wenchao Huang, Jie Cui, Hong Zhong, and Yan Xiong

80 1000

Success Rate (%)

| Time Cost (s) | 916.9 |
| --- | --- |
| 70 | 900 |

64.52%

800

60

706.1

735.4 700

50

49.46% 600 Time Cost (s)

Success Rate (%)

40

543.7 500

35.48%

30 433.7 32.26%

30.11% 400

20 300

1 2 3 4 5

The value of k

Fig. 6. Success rate and time cost of TreeMind under different values of k

w/o SI achieves an overall success rate of 36.56%, 27.96% lower than the original version, and takes

335.9 seconds on average for a bug report, approximately 1.23 × greater. The results demonstrate

the crucial role of the optimized simulation stage. Without it, the tool struggles to obtain accurate

rewards under the standard rollout strategy, which negatively impacts the entire MCTS process.

For example, when reproducing a crash in an app named Anki-9914 , the simulation stage at this

ablation assigns similar scores to different actions, making it difficult to distinguish correct from

incorrect ones. As a result, the reproduction process deviates from the correct path, undermining

the intended advantage of MCTS.

4.4 RQ3: Optimal k in MCTS Expansion

To determine the optimal value of k for our task, we conduct experiments with k values from 1

to 5. To ensure fairness, we use the same dataset described in Section 4.3. All other experimental

settings remain consistent with those described in Section 4.2.

As the results in Figure 6, TreeMind achieves the best performance when k = 3. Overall, we

observe that the reproduction success rate reaches its peak ( i.e. , 64.52%) while the average time cost

is also minimized ( i.e. , 241.4 seconds) under this setting. This indicates that setting k to 3 provides

the optimal balance between exploration and exploitation in the decision-making process.

When k < 3, although the detection success rate shows an upward trend, it remains relatively low.

Meanwhile, the average time cost stays high. This is likely because the limited candidate action set

misses key actions necessary for reproduction, which ultimately compromises decision quality.

When k > 3, the detection success rate drops and the average time cost increases. A larger

candidate set tends to introduce more irrelevant or misleading actions, expanding the search space

and complicating the decision-making process. Interestingly, the overall time cost at k = 5 is lower

than at k = 4. After further analysis, we find that when k is set to 4, TreeMind tends to focus more

on reproducing complex bugs successfully, even at the cost of longer execution time. In contrast,

when k is set to 5, it quickly reproduces simpler bugs but struggles to handle more complex ones.

5 Discussion

To ensure the representativeness and diversity of our evaluation data, we collect bug reports and the

relevant APKs from three widely-used datasets constructed by prior studies published in top-tier

---

## Page 17

TreeMind : Automatically Reproducing Android Bug Reports via LLM-empowered Monte Carlo Tree Search

conferences and journals [4–6]. This helps improve the external validity of our evaluation by

reflecting real-world bug reproduction scenarios. In the future, we will extend our datasets with

bug reports from different domains to strengthen our work.

Our work primarily relies on two off-the-shelf techniques, including LLMs and UI Automator2,

both of which have inherent limitations that may impact the performance of TreeMind. On the

one hand, LLMs may produce hallucinated or inconsistent outputs [26], which can undermine

the effectiveness of MCTS-based planning. To mitigate the issue, we adopt GPT-4o, a state-of-the-

art LLM that supports multi-modal inputs and is widely adopted in both academia and industry.

With the rapid advancement of LLMs, we plan to explore more advanced models in the future to

evaluate their effectiveness on our approach. Moreover, the LLM training data is not public, so

some bug reports might have been seen during pretraining. However, crash reproduction involves

reasoning over app-specific UI states and interactions, which goes beyond simple memorization. To

ensure the reliability of our results, we execute TreeMind five times per bug report and evaluate

its performance using aggregated outputs. On the other hand, UI Automator2, one of the most

widely adopted tools for UI testing [3, 6, 8], exhibits limitations in extracting UI information and

performing certain actions, as described in Section 4.2.1. We plan to use image-based UI testing

techniques [27] to address the limitations of extracting textual UI descriptions for bug reproduction.

TreeMind achieves a high success rate for bug reproduction, but takes more execution time and

tokens compared to purely LLM-based methods [3, 4, 10]. This is primarily due to the integration

of MCTS-based searching into the LLM-guided agents and the need to provide multi-modal UI

information, which introduces additional computational overhead. However, we argue that this

overhead is justified by the significantly improved reproduction success rate achieved by our work.

In practical scenarios, the reliability and completeness of bug reproduction are often prioritized

over execution speed, especially in debugging and quality assurance workflows. In future work,

we plan to optimize the search process ( e.g. , via parallelization [28]) to reduce execution time and

tokens without compromising accuracy. We also consider adopting the idea from ReBL, where the

LLM outputs a sequence of actions in one round, to improve reproduction efficiency. We believe

that the above optimization strategies are orthogonal to our core approach and can be leveraged

independently to further enhance performance.

6 Related Work

6.1 Non-LLM-based Bug Report Reproduction

Most existing work focuses on reproducing bug reports in textual form. ReCDroid [7] combined

natural language processing (NLP) and dynamic GUI exploration to reproduce the bugs for Android

apps. ReCDroid+ [8] extended ReCDroid by leveraging deep learning techniques to extract S2R

sentences. ReproBot [6] used NLP techniques to extract S2R entities and then adopted Q-learning to

guide the search for successful reproducing steps. Roam [29] leveraged the target app’s UI transition

graph to globally search for the UI event path for reproducing bug report steps. ScopeDroid [30]

designed a multi-modal neural network that matches reproducing steps to GUI widgets by consid-

ering their icons and contextual information obtained from a state transition graph. Traditional

NLP-based methods often struggle to accurately extract S2Rs and to understand the semantics of

bug reports and UI context. Moreover, the lack of global planning in some approaches may limit

their effectiveness in practice.

Images are another commonly used information modality for reproducing bug reports. GIF-

droid [31] utilized image processing techniques to extract key information from screen recordings

and then automate bug reproduction. Wang et al. [32] made a systematic study on the images

---

## Page 18

Zhengyu Chen, Zhaoyi Meng, Wenxiang Zhao, Wansen Wang, Wenchao Huang, Jie Cui, Hong Zhong, and Yan Xiong

within bug reports and found that using images in bug reports can enhance the reproduction task.

We leave the reproduction of image-based bug reports as future work.

TreeMind inputs the whole bug reports into an advanced LLM to extract more comprehensive

information, without the use of S2R entities and specific bug type domains. Meanwhile, it feeds

both textual reports and UI screenshots into the LLM to facilitate decision-making by leveraging

their complementarity. Moreover, by integrating MCTS with LLMs, our approach achieves a more

strategic and guided searching of the state space of apps. This synergy leads to noticeably better

outcomes, as confirmed by our experiments.

6.2 LLM-based Bug Report Reproduction

With the success of LLMs in NLP tasks, researchers have begun to explore their potential in

automating bug report reproduction. AdbGPT [3] first leveraged prompt engineering to reproduce

bugs without requiring any training or hard-coded rules. However, this tool faces two limitations:

(i) difficulty in accurately extracting S2R entities from bug reports with complex and diverse

semantics [10], and (ii) limited long-term planning due to prompt-only reliance. ReBL [10] bypassed

the use of S2R entities and incorporated a feedback mechanism into LLM prompts, yet still struggled

in complex UI exploration. ReActDroid [4] reproduced app bugs from the crash overview of one-

sentence reports. It leveraged the LLM with ReAct prompting to iteratively interact with the

GUI widget that may lead to the crash. As with ReBL, prompt-only approaches may not always

be sufficient to ensure effective and reliable bug reproduction. AndroB2O [33] is an LLM-based

approach that generates test oracles for non-crashing GUI failures by reasoning over multimodal

bug reports combining text and screenshots. Unlike our method, which targets crash-inducing

bugs and leverages screenshots at every interaction step, AndroB2O focused on non-crashing GUI

failures and used only the screenshot related to the failures. AEGIS [34] and LIBRO [35] used LLMs

for code-level bug reproduction, rather than addressing the challenges arising from UI interactions.

To better understand UI states, TreeMind takes multimodal inputs, e.g. , the complete bug report

and the UI screenshot captured during reproduction, rather than relying on explicit S2R entity

extraction. Inspired by the advanced techniques above, it integrates an LLM-based multi-agent

framework with MCTS for effective state space searching: MCTS guides decision-making, while

two LLM agents respectively identify top- k promising actions and estimate their success likelihood

after executing each selected action.

6.3 Bug Report Study

Several research efforts have focused on studying and analyzing Android bug reports. Yakusu [9]

combined program analysis and NLP to generate executable test cases from bug reports. MaCa [36]

trained a machine learning-based classifier to identify and classify action words in the bug reports of

apps. Johnson et al. [5] conducted an empirical study to examine the challenges of bug reproduction

and the quality of the reported information. Burt [37] developed a task-oriented chatbot with

instant feedback and graphical suggestions to improve the quality of bug reports. EBug [38] helped

users write more accurate bug reports by connecting reproduction steps with relevant information

obtained from static and dynamic analyses of the app. TAB [39] was designed to generate accurate

and meaningful titles for bug reports automatically. BugSpot [40] automatically recognized the

buggy behavior of the described bug during the automated reproduction of the bug report. It could

be combined with our work to enhance the overall effectiveness in the future.

Although these techniques offer valuable insights into understanding bug reports, their primary

objectives are not to directly reproduce the reported bugs. Nevertheless, the techniques on analyzing

and improving bug reports can benefit TreeMind, for example by enhancing its understanding of

the semantic of bug reports.

---

## Page 19

TreeMind : Automatically Reproducing Android Bug Reports via LLM-empowered Monte Carlo Tree Search

7 Conclusion

We introduce TreeMind, a novel technique that combines LLM reasoning with MCTS-based

planning to reproduce Android crashes from incomplete bug reports. Unlike prior LLM-based

approaches that rely solely on prompt engineering, TreeMind treats bug reproduction as a goal-

directed search task and leverages two LLM-guided agents for semantic reasoning and adaptive

decision-making within MCTS. Extensive experiments on 93 real-world Android bug reports show

that TreeMind achieves a reproduction success rate of 64.52%, significantly outperforming four

state-of-the-art baselines. Each successful reproduction takes an average of 241.4 seconds, which is

acceptable in practical scenarios.

References

[1] Statista. 2026. Number of apps available in leading app stores from August 2024 to January 2026. https://www.

statista.com/statistics/276623/number-of-apps-available-in-leading-app-stores/?srsltid=AfmBOorJwGCJial2cbD-

xN9T4j1241ALX7MWvSUlyNnx-pNzv0UHSKVF#statisticContainer Accessed: January 27, 2026.

[2] David Bolton. 2017. 88% Of People Will Abandon An App Because Of Bugs. Applause Blog. https://www.applause.

com/blog/app-abandonment-bug-testing/ Accessed: July 9, 2025.

[3] Sidong Feng and Chunyang Chen. 2024. Prompting is all you need: Automated android bug replay with large language

models. In Proceedings of the 46th IEEE/ACM International Conference on Software Engineering . 1–13.

[4] Yuchao Huang, Junjie Wang, Zhe Liu, Mingyang Li, Song Wang, Chunyang Chen, Yuanzhe Hu, and Qing Wang. 2025.

One Sentence Can Kill the Bug: Auto-replay Mobile App Crashes from One-sentence Overviews. IEEE Transactions on

Software Engineering (2025).

[5] Jack Johnson, Junayed Mahmud, Tyler Wendland, Kevin Moran, Julia Rubin, and Mattia Fazzini. 2022. An empirical

investigation into the reproduction of bug reports for android apps. In 2022 IEEE International Conference on Software

Analysis, Evolution and Reengineering (SANER) . IEEE, 321–322.

[6] Zhaoxu Zhang, Robert Winn, Yu Zhao, Tingting Yu, and William GJ Halfond. 2023. Automatically reproducing android

bug reports using natural language processing and reinforcement learning. In Proceedings of the 32nd ACM SIGSOFT

International Symposium on Software Testing and Analysis . 411–422.

[7] Yu Zhao, Tingting Yu, Ting Su, Yang Liu, Wei Zheng, Jingzhi Zhang, and William GJ Halfond. 2019. Recdroid:

automatically reproducing android application crashes from bug reports. In 2019 IEEE/ACM 41st International Conference

on Software Engineering (ICSE) . IEEE, 128–139.

[8] Yu Zhao, Ting Su, Yang Liu, Wei Zheng, Xiaoxue Wu, Ramakanth Kavuluru, William GJ Halfond, and Tingting Yu.

2022. Recdroid+: Automated end-to-end crash reproduction from bug reports for android apps. ACM Transactions on

Software Engineering and Methodology (TOSEM) 31, 3 (2022), 1–33.

[9] Mattia Fazzini, Martin Prammer, Marcelo d’Amorim, and Alessandro Orso. 2018. Automatically translating bug reports

into test cases for mobile apps. In Proceedings of the 27th ACM SIGSOFT International Symposium on Software Testing

and Analysis . 141–152.

[10] Dingbang Wang, Yu Zhao, Sidong Feng, Zhaoxu Zhang, William GJ Halfond, Chunyang Chen, Xiaoxia Sun, Jiangfan

Shi, and Tingting Yu. 2024. Feedback-driven automated whole bug report reproduction for android apps. In Proceedings

of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis . 1048–1060.

[11] David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert,

Lucas Baker, Matthew Lai, Adrian Bolton, et al. 2017. Mastering the game of go without human knowledge. nature

550, 7676 (2017), 354–359.

[12] Raphael Chekroun, Thomas Gilles, Marin Toromanoff, Sascha Hornauer, and Fabien Moutarde. 2024. MBAPPE: MCTS-

built-around prediction for planning explicitly. In 2024 IEEE Intelligent Vehicles Symposium (IV) . IEEE, 2062–2069.

[13] Peter Auer, Nicolo Cesa-Bianchi, Yoav Freund, and Robert E Schapire. 2002. The nonstochastic multiarmed bandit

problem. SIAM journal on computing 32, 1 (2002), 48–77.

[14] Tianhao Zhang, Yueheng Li, Chen Wang, G. Xie, and Zongqing Lu. 2021. FOP: Factorizing Optimal Joint Policy of

Maximum-Entropy Multi-Agent Reinforcement Learning. PMLR (2021).

[15] Ivo Danihelka, Arthur Guez, Julian Schrittwieser, and David Silver. 2022. Policy improvement by planning with

Gumbel. In International Conference on Learning Representations .

[16] Peter Auer, Nicolo Cesa-Bianchi, and Paul Fischer. 2002. Finite-time analysis of the multiarmed bandit problem.

Machine learning 47, 2 (2002), 235–256.

[17] Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. 2015. Distilling the knowledge in a neural network. arXiv preprint

arXiv:1503.02531 (2015).

---

## Page 20

Zhengyu Chen, Zhaoyi Meng, Wenxiang Zhao, Wansen Wang, Wenchao Huang, Jie Cui, Hong Zhong, and Yan Xiong

[18] Jingjin Wang and Jiawei Han. 2025. Proprag: Guiding retrieval with beam search over proposition paths. In Proceedings

of the 2025 Conference on Empirical Methods in Natural Language Processing . 6223–6238.

[19] Yui Sudo, Muhammad Shakeel, Yosuke Fukumoto, Yifan Peng, and Shinji Watanabe. 2024. Contextualized automatic

speech recognition with attention-based bias phrase boosted beam search. In ICASSP 2024-2024 IEEE International

Conference on Acoustics, Speech and Signal Processing (ICASSP) . IEEE, 10896–10900.

[20] David Silver, Aja Huang, Chris J Maddison, Arthur Guez, Laurent Sifre, George Van Den Driessche, Julian Schrittwieser,

Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, et al. 2016. Mastering the game of Go with deep neural

networks and tree search. nature 529, 7587 (2016), 484–489.

[21] Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan Shen, Shengjie Ma,

Honghao Liu, et al. 2024. A survey on llm-as-a-judge. The Innovation (2024).

[22] Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang, Hiroaki Hayashi, and Graham Neubig. 2023. Pre-train, prompt,

and predict: A systematic survey of prompting methods in natural language processing. ACM computing surveys 55, 9

(2023), 1–35.

[23] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. 2022.

Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information processing

systems 35 (2022), 24824–24837.

[24] codeskyblue. 2025. Android Uiautomator2 Python Wrapper. GitHub. https://github.com/openatx/uiautomator2

Accessed: August 16, 2025.

[25] OpenAI. 2025. Models. OpenAI developer platform. https://platform.openai.com/docs/models Accessed: August 16,

2025.

[26] Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Haotian Wang, Qianglong Chen, Weihua Peng,

Xiaocheng Feng, Bing Qin, et al. 2025. A survey on hallucination in large language models: Principles, taxonomy,

challenges, and open questions. ACM Transactions on Information Systems 43, 2 (2025), 1–55.

[27] Junyang Wang, Haiyang Xu, Haitao Jia, Xi Zhang, Ming Yan, Weizhou Shen, Ji Zhang, Fei Huang, and Jitao Sang. 2024.

Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration. In

Advances in Neural Information Processing Systems , A. Globerson, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak,

and C. Zhang (Eds.), Vol. 37. Curran Associates, Inc., 2686–2710.

[28] J. B. Chaslot, Mark H. M. Winands, and H. Jaap Van Den Herik. 2008. Parallel Monte-Carlo Tree Search. In International

Conference on Computers & Games .

[29] Zhaoxu Zhang, Fazle Mohammed Tawsif, Komei Ryu, Tingting Yu, and William GJ Halfond. 2024. Mobile bug report

reproduction via global search on the app ui model. Proceedings of the ACM on Software Engineering 1, FSE (2024),

2656–2676.

[30] Yuchao Huang, Junjie Wang, Zhe Liu, Song Wang, Chunyang Chen, Mingyang Li, and Qing Wang. 2023. Context-aware

bug reproduction for mobile apps. In 2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE) .

IEEE, 2336–2348.

[31] Sidong Feng and Chunyang Chen. 2022. Gifdroid: Automated replay of visual bug reports for android apps. In

Proceedings of the 44th International Conference on Software Engineering . 1045–1057.

[32] Dingbang Wang, Zhaoxu Zhang, Sidong Feng, William GJ Halfond, and Tingting Yu. 2025. An Empirical Study on

Leveraging Images in Automated Bug Report Reproduction. In 2025 IEEE/ACM 22nd International Conference on Mining

Software Repositories (MSR) . IEEE, 27–38.

[33] Jack Johnson, Junayed Mahmud, Oscar Chaparro, Kevin Moran, and Mattia Fazzini. 2025. Generating Failure-Based

Oracles to Support Testing of Reported Bugs in Android Apps. In Proceedings of the 40th IEEE/ACM International

Conference on Automated Software Engineering .

[34] Xinchen Wang, Pengfei Gao, Xiangxin Meng, Chao Peng, Ruida Hu, Yun Lin, and Cuiyun Gao. 2025. AEGIS: An

Agent-based Framework for Bug Reproduction from Issue Descriptions. In Proceedings of the 33rd ACM International

Conference on the Foundations of Software Engineering, FSE Companion 2025, Clarion Hotel Trondheim, Trondheim,

Norway, June 23-28, 2025 . ACM, 331–342.

[35] Sungmin Kang, Juyeon Yoon, and Shin Yoo. 2023. Large language models are few-shot testers: Exploring llm-based

general bug reproduction. In 2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE) . IEEE,

2312–2323.

[36] Hui Liu, Mingzhu Shen, Jiahao Jin, and Yanjie Jiang. 2020. Automated classification of actions in bug reports of mobile

apps. In Proceedings of the 29th ACM SIGSOFT International Symposium on Software Testing and Analysis . 128–140.

[37] Yang Song, Junayed Mahmud, Ying Zhou, Oscar Chaparro, Kevin Moran, Andrian Marcus, and Denys Poshyvanyk.

2022. Toward interactive bug reporting for (android app) end-users. In Proceedings of the 30th ACM joint european

software engineering conference and symposium on the foundations of software engineering . 344–356.

[38] Mattia Fazzini, Kevin Moran, Carlos Bernal-Cardenas, Tyler Wendland, Alessandro Orso, and Denys Poshyvanyk.

2022. Enhancing mobile app bug reporting via real-time understanding of reproduction steps. IEEE Transactions on

---

## Page 21

TreeMind : Automatically Reproducing Android Bug Reports via LLM-empowered Monte Carlo Tree Search

Software Engineering 49, 3 (2022), 1246–1272.

[39] Xiao Liu, Yinkang Xu, Weifeng Sun, Naiqi Huang, Song Sun, Qiang Li, Dan Yang, and Meng Yan. 2025. Tab: template-

aware bug report title generation via two-phase fine-tuned models. Automated Software Engineering 32, 2 (2025),

32.

[40] Zhaoxu Zhang, Komei Ryu, Tingting Yu, and William GJ Halfond. 2025. Automated Recognition of Buggy Behaviors

from Mobile Bug Reports. Proceedings of the ACM on Software Engineering 2, FSE (2025), 2240–2263.

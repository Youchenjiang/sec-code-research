---
title: "GPT‐Monkey: Enhancing Automated GUI Testing for Android Apps via LLM‐Driven Interface Understanding and Function Segmentation"
creator: "Aspose Pty Ltd."
pages: 29
---

# GPT‐Monkey: Enhancing Automated GUI Testing for Android Apps via LLM‐Driven Interface Understanding and Function Segmentation

> **總頁數**：29 頁

---

## Page 1

IET Software

RESEARCH ARTICLE OPEN ACCESS

GPT-Monkey: Enhancing Automated GUI Testing for

Android Apps via LLM-Driven Interface Understanding and

Function Segmentation

1 2 1 3 1 1

Zhanhui Yuan | Kai Chen | Zhi Yang | Dongxue Jiang | Jinglei Tan | Hongqi Zhang

1 School of Cryptography Engineering, People ’ s Liberation Army Information Engineering University, Zhengzhou, China | 2 Institute of Information Engineering,

Chinese Academy of Sciences, Beijing, China | 3 CRIStAL, Centrale Lille Institut, Villeneuve d ’ Ascq, France

Correspondence: Kai Chen (chenkai@iie.ac.cn)

Received: 9 February 2025 | Revised: 12 March 2026 | Accepted: 27 April 2026

Academic Editor: Alessandro Marchetto

Keywords: function segmentation | GUI testing | interface understanding | large language models

ABSTRACT

Automated graphical user interface (GUI) testing is essential for ensuring mobile app quality. However, existing related methods

lack deep GUI understanding and cannot segment speci fi c functions for targeted testing, resulting in wasted test events and low

ef fi ciency. This study aims to leverage large language models (LLMs) to enhance Monkey-based GUI testing by enabling function-

level segmentation and tailored parameter generation driven by user requirements. We propose GPT-Monkey, which integrates

Monkey ’ s randomness with LLM ’ s understanding capability. It establishes global interface associations and cross-modal align-

ment for LLM-driven function segmentation, employs parameter-retrieval augmented generation (RAG) to guide tailored param-

eter generation, and adopts a dual-feedback mechanism to iteratively optimize testing. Experiments show that GPT-Monkey

improves crash detection by 16.7 % and ef fi ciency by 34.5 % over the optimal baseline, and achieves 95 % function segmentation

accuracy and uncovers 397 real-world crashes on 1000 Google Play apps. The results demonstrate that LLM-driven function

segmentation and tailored parameter generation signi fi cantly enhance the precision and ef fi ciency of automated GUI testing.

1 | Introduction Various GUI testing tools [4 – 8] have emerged over the years. One

of the pioneering efforts in this fi eld is Monkey [4], a fuzzing tool

With the rapid development and widespread utilization of mobile

developed by Google, which generates randomized GUI event

apps, ensuring the quality and reliability of apps to align with user

sequences to detect crashes without speci fi c testing scripts.

| expectations has become particularly critical [1, 2]. The graphical | Model-based GUI testing methods [9 | – | 12] utilize models like state |
| --- | --- | --- | --- |
| user interface (GUI), as the main medium of user interaction with | machines to describe all possible states and transitions of the |  |  |
| the app, serves as an optimal entry point for testing. To overcome | interfaces to guide exploration. Learning-based GUI testing meth- |  |  |
| the time-consuming and resource-intensive manual testing, auto- | ods [13 | – | 15] leverage learning techniques to automatically learn |
| mated GUI testing [3] has been devoted to quality assurance of | and optimize testing strategies from user behavior data. |  |  |
| apps, which effectively simulates user operation behaviors (click- | Despite these advances, existing automated GUI testing methods |  |  |
| ing, typing, scrolling, etc.) to detect potential crashes and errors | are commonly recognized as full-coverage testing, which share a |  |  |
| within the app interface. | fundamental limitation of lacking deep semantic understanding |  |  |

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided

the original work is properly cited.

Copyright © 2026 Zhanhui Yuan et al. IET Software published by John Wiley & Sons Ltd.

IET Software, 2026; 2026:9976714 1 of 29

https://doi.org/10.1049/sfw2/9976714

*[Image: Page 1 Image]*

---

## Page 2

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| of the GUI and are therefore unable to segment speci | fi | c app func- | None of them address function-level segmentation or tailored |
| --- | --- | --- | --- |
| tions for targeted testing. Monkey-based tools [4, 8] operating | parameter generation for targeted testing. In contrast, GPT- |  |  |
| through random or coverage-driven event generation, inevitably | Monkey leverages LLM for interface understanding, function |  |  |
| dispatch large numbers of events to interface areas unrelated to | segmentation, and parameter tailoring within a Monkey-based |  |  |
| the target function, resulting in signi | fi | cant resource waste and | testing framework, which fundamentally differs from existing |
| reduced bug- | fi | nding precision. Model-based methods such as | LLM-based approaches in both testing scope and testing objective. |

APE [9], TimeMachine [10], and ComboDroid [11], are inherently

In this study, a function is a business unit represented as a two-

oriented toward maximizing state coverage and cannot identify

tuple ( E , A ), where E is the entry area (the bounding rectangle of

function-level boundaries. Learning-based methods such as Q-

the fi rst GUI component triggering the function) and A is the set of

testing [13], OAT [14], and DQT [15], optimize event sequences

associated interfaces involved in its execution. An interface is the

at the component or state level but are incapable of reasoning

visible, interactive screen area rendered by an activity or fragment.

about function boundaries. As demonstrated in reference [16],

UIAutomator dynamically captures the UI hierarchy at runtime,

these full-coverage GUI testing tools miss 53.8 % to 71.2 % of

while DroidBot analyzes state transitions to identify interface

real-world bugs.

associations, together forming the basis for function segmenta-

| In practice, user testing requirements are often function-speci | fi | c. | tion. Unlike methods that exhaustively explore all app functions, |
| --- | --- | --- | --- |
| During iterative development, a version update may only affect a | GPT-Monkey segments user-speci | fi | ed functions by identifying |
| particular function (e.g., payment or search), requiring regression | their entry areas and associated interfaces from the global inter- |  |  |
| testing exclusively on that function. Similarly, crash reports tar- | face association graph, guiding the Monkey-based test engine |  |  |
| geting a speci | fi | c function call for focused stress testing rather than | toward crash-prone targets. |

full-interface exploration. A single function typically spans multi-

To evaluate the GPT-Monkey, we conduct experiments on both

| ple interrelated components with complex spatial relationships | standard benchmark and real-world benchmark (composed of the |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| across several interfaces, making function-level segmentation | top 1000 popular apps in Google Play). For the usefulness evalua- |  |  |  |  |
| impossible without deep understanding of GUI semantics. Fur- | tion of GPT-Monkey, we focus on its accuracy in segmenting |  |  |  |  |
| thermore, none of the existing methods support tailored parame- | functions. GPT-Monkey can achieve 100 | % | accuracy in Themis |  |  |
| ter generation for speci | fi | c functions, as they rely on either default | with 68 functions and 95 | % | accuracy in a real-world benchmark |
| or manually con | fi | gured settings without consideration of the tar- | with 3337 functions. Apart from the usefulness evaluation of GPT- |  |  |
| get function | ’ | s characteristics. | Monkey, we concentrate on its ability to detect crashes of app |  |  |

functions for effectiveness evaluation. GPT-Monkey can increase

This study aims to address these limitations by leveraging the

the detection rate by 27.3 % in contrast to the traditional Monkey

semantic understanding capabilities of large language models

and the detection ef fi ciency by 34.5 % compared to the optimal

(LLMs) [17] to enhance Monkey-based GUI testing. Speci fi cally,

baseline method in Themis with 52 known crashes. In the 1000

we seek to enable function-level segmentation guided by user

real-world apps, GPT-Monkey fi nds 397 crashes.

requirements and tailored parameter generation that adapts to

the characteristics of the target function, thereby transforming Through delving into the signi fi cance and limitations of existing

full-coverage testing into function-targeted automated testing. automated GUI testing, this research introduces a novel GPT-

Monkey testing method aimed at enhancing GUI testing. The

To this end, we propose GPT-Monkey, a novel LLM-enhanced

key contributions of this research are summarized as follows:

GUI testing framework that integrates the event generation capa-

| bility of Monkey with the semantic understanding of LLMs. First, | • | Novel LLM-Enhanced Testing Framework: GPT-Monkey is |  |
| --- | --- | --- | --- |
| GPT-Monkey establishes the global interface association and | the | fi | rst to integrate LLM into Monkey-based GUI testing, |
| achieves cross-modal alignment between the layout and the | enabling function segmentation and parameter tailoring for |  |  |
| screenshot of the targeted function entry interface. Next, it | targeted testing, thereby eliminating redundant test |  |  |
| encodes them with the testing requirements input by the user | execution. |  |  |

into the prompt for the LLM to fully understand the user ’ s testing

• Technical Innovation for Reliable LLM Application:

requirements for a speci fi c function of the app through an inter-

GPT-Monkey introduces a dual-feedback mechanism, cross-

active feedback loop, segment the targeted function and generate

modal alignment, interface association, and Parameter-RAG

tailored testing parameters guided by the knowledge base oper-

to mitigate LLM hallucination and ensure precise interface

ated by parameter retrieval augmented generation (parameter-

understanding and function segmentation.

RAG) method. Then, GPT-Monkey decodes these parameters

| into executable scripts for Monkey-based kernel, enabling tar- | • | Empirical Validation: GPT-Monkey outperforms the best |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| geted testing directed to a speci | fi | c function of the mobile app. | baseline by 16.7 | % | in detection rate and 34.5 | % | in detection |
| Finally, GPT-Monkey returns execution results from the Monkey | ef | fi | ciency, achieves 95 | % | accuracy in function segmentation, |  |  |
| kernel to the LLM through log analysis feedback to adjust test | and detects 397 crashes across 1000 real-world apps. |  |  |  |  |  |  |

parameters and iteratively optimize automated GUI testing.

GPT-Monkey is fundamentally different from existing LLM-based

GUI testing tools. Tools such as DroidBot-GPT [18], LLMDroid 2 | Background

[19], GERALLT [20], and MemoDroid [21], primarily employ

2.1 | Automated GUI Testing and Monkey Testing

LLMs for operation-level decisions or coverage enhancement,

| such as selecting the next click, generating text inputs at a given | Monkey testing [4, 8] is a widely used automated GUI testing |  |
| --- | --- | --- |
| interface state, or guiding exploration toward unexplored areas. | method that sends random inputs, such as clicks and swipes, to |  |
| 2 of 29 | IET Software, | 2026 |

---

## Page 3

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| an application to evaluate its stability under stress. By simulating | relevant text inputs, generating human-like test scripts, and auto- |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| unpredictable user interactions, this stress-testing approach | mating mobile tasks [18 | – | 25]. The basic work | fl | ow of LLM-based |
| ensures that applications remain robust under extreme condi- | GUI testing typically involves converting GUI states and available |  |  |  |  |
| tions, thereby enhancing app reliability and user experience. | actions into natural language prompts, allowing the LLM to deter- |  |  |  |  |

mine appropriate actions, generate and execute test scripts. Due to

its powerful language comprehension and reasoning abilities,

2.2 | Typical Monkey Con fi guration and Parameter

LLM can capture complex contextual information and generate

Customization Impact

high-quality test content, which is dif fi cult to achieve with tradi-

Although Monkey testing is widely used for its simplicity, its tional GUI testing methods.

effectiveness depends heavily on proper parameter con fi guration.

Monkey offers various command-line parameters that allow tes-

ters to customize event type distribution, test speed, target appli-

3 | Motivation

cation, and so on. Table 1 summarizes these typical parameters

| and their impact on test behavior and results. The parameter | Currently, mobile applications are characterized by extensive user |  |  |
| --- | --- | --- | --- |
| descriptions are based on the of | fi | cial Android Monkey documen- | interactions, multimedia content processing, and third-party ser- |
| tation [4] and practical testing guidelines [7, 8]. | vice integration (like map services and online payments) [26, 27]. |  |  |

The diversity and complexity of their functions present signi fi cant

In practice, these parameters must be combined to meet speci fi c

challenges for GUI testing [28, 29].

test objectives. For instance, simulating normal user behavior

| requires a higher proportion of touch and swipe events, while | Consider the following situations. When large-scale applications |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| stress testing calls for reducing the delay between events and | develop or modify speci | fi | c functions in an existing interface, as |  |  |
| increasing the proportion of system button and switch events. | depicted in Figure 1a, the stability and robustness of other func- |  |  |  |  |
| By customizing parameter values and parameter combinations, | tions in the interface may not be affected. In this case, conducting |  |  |  |  |
| Monkey | ’ | s parameter con | fi | guration can effectively affect the test | GUI testing with full interface coverage is both time-consuming |
| scope, test depth, and issue exposure speed, thereby obtaining | and inef | fi | cient. Therefore, it is necessary to perform GUI testing |  |  |
| more comprehensive Monkey test results. | on the target function to signi | fi | cantly enhance testing ef | fi | ciency. |

Moreover, when the entry area of a function only occupies a small

portion of the app interface, as shown in Figure 1b, conducting

2.3 | LLM-Based GUI Testing

GUI testing that covers the entire app interface results in a waste

| In recent research, LLM plays a key role in automated GUI testing, | of numerous random operations. Taking all the above into con- |
| --- | --- |
| which is responsible for understanding testing targets, generating | sideration, there is a need for novel GUI testing techniques that |

TABLE 1 | Typical monkey con fi gurations and parameter customization impact.

| Parameter | Function | Impact on monkey behaviors | Impact on test results |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| - | p | < | package | > | Target app package | Limit testing to the speci | fi | ed app, | Ensure that test results focus on the |
| avoiding interference with the system | target application, eliminating |  |  |  |  |  |  |  |  |
| or other apps. | external interference and improving |  |  |  |  |  |  |  |  |

accuracy.

– throttle < ms > Delay between events Larger values improve stability and Help regulate the testing pace and

debugging, while smaller values facilitate the reproduction of issues.

increase test intensity.

– pct-touch Percentage of touch events Focus test on tap/click interactions, Facilitate the exposure of UI response

suitable for UI-intensive apps. issues, such as button failure, touch

response errors, etc.

– pct-motion Percentage of motion (swipe) Focus test on scrolling and gesture Facilitate the detection of issues such

events operations. as sliding lag, crashes, or abnormal

gesture response.

| – | pct-appswitch | Percentage of app switch events | Evaluate app behavior under | Increase the likelihood of exposing |
| --- | --- | --- | --- | --- |
| background or foreground | crashes in lifecycle management, |  |  |  |
| transitions. | state recovery, or multitasking |  |  |  |

environments.

– pct-syskeys Percentage of system key events Simulate power/volume/menu keys Enable testing of responses to system

to test system-level interactions. buttons or mishandling issues, such

as accidentally touching Home/Menu

and causing a crash, etc.

| -s | < | seed | > | Random seed for event sequence | Ensure reproducibility of the same | Facilitate regression testing by |
| --- | --- | --- | --- | --- | --- | --- |
| random event sequence. | making test results reproducible. |  |  |  |  |  |
| IET Software, | 2026 | 3 of 29 |  |  |  |  |

---

## Page 4

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

(a) (b)

FIGURE 1 | (a) Examples of entry areas for function modi fi cation within a stable interface. (b) Examples of entry areas for function occupying a

small portion of the interface.

| can focus on functions where crashes are more likely to occur and | testing parameters are generated by LLM, which are supported for |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| only test the interface areas related to the test target, thereby | user modi | fi | cation. Then, in step | ⑤ | , through user interaction feed- |
| improving testing ef | fi | ciency. | back loop, the user modi | fi | es and validates the basic testing param- |

eters, which are compiled into a new prompt for LLM. Following

However, existing Monkey-based and model-based GUI testing

that, LLM provides optimized feedback, including the target func-

tools [4, 8 – 12] do not possess the ability to segment functions

tion segmentation and tailored testing parameters based on the

for targeted testing. Additionally, existing LLM-based GUI testing

characteristics of the target function. The segmentation results of

tools [18 – 25] leverage LLM to only generate instructions for inter-

the target function typically include the entry area coordinates of

face operations. The answers of the LLM can merely guide the

the function and its associated interface activities. To ensure the

execution of clicks or other operations to achieve tasks. Although

validity of the test parameters, step ⑥ involves GPT-Monkey uti-

these tools demonstrate an understanding of the interface, their

lizing parameter-RAG technology to operate a Monkey test

applications are constrained to a single operation on a single com-

parameter knowledge base for precisely guiding the generation

ponent and they are unable to perform testing on targeted func-

of testing parameters. Thereafter, in step ⑦ , GPT-Monkey decodes

tions. How to intelligently segment the function within the app

the tailored testing parameters into executable operation instruc-

and conduct automated GUI testing on the targeted function is

tion and organizes the segmentation results of the target function

exactly the problem that GPT-Monkey resolves. The above real-

into a speci fi c con fi guration fi le. In step ⑧ , GPT-Monkey sends the

world situations indicate that GPT-Monkey provides a feasible

instruction and con fi guration fi le to a Monkey-based testing ker-

and effective solution for automated GUI testing in such scenar-

nel to conduct automated testing on the target function. Finally, in

ios. GPT-Monkey leverages the understanding of LLM for inter-

step ⑨ , through log analysis feedback loop, GPT-Monkey returns

faces to intelligently segment the entry area of the targeted

the test results generated by the Monkey test kernel to LLM to

function and its associated interfaces based on testing require-

achieve dynamic optimization and continuous iteration of test

ments, tailors testing parameters based on the characteristics of

parameters. By analyzing abnormal behaviors, failure logs, and

the function, and conducts automated GUI testing on it.

coverage information exposed during test execution, LLM can

further adjust parameters, improve test effectiveness, and form a

closed-loop automatic GUI testing.

4 | Approach

This procedure can focus on a speci fi c function within the app or

4.1 | Overview

traverse the entire app to ensure comprehensive testing. How to

| This research develops a novel GUI testing method, GPT-Monkey, | conduct the testing is determined by the user | ’ | s requirements. The |
| --- | --- | --- | --- |
| with its work | fl | ow illustrated in Figure 2. The interface under- | test process of GPT-Monkey starts from the entry area of the target |
| standing and the function segmentation within the app, as well | function and cannot be interrupted until the test is completed. If a |  |  |
| as the generation of testing instructions, are all driven by LLM, | different function needs to be tested, the user should switch the |  |  |
| which is dif | fi | cult to achieve in traditional GUI testing without | entry interface of the function on the device and input the testing |
| incorporating LLM. | requirements in GPT-Monkey to initiate the next test. This |  |  |

method not only ensures automatically targeted testing but also

The work fl ow of GPT-Monkey begins with the step ① , where the

provides an intuitive operation mode for non-professionals, allow-

user proposes testing requirements for a certain function in natu-

ing them to participate in testing through simple natural language

ral language, along with the step ② , the extraction of layout infor-

descriptions.

mation and the screenshot from the function entry interface. At

| the same time, in step | ② | , GPT-Monkey establishes a global inter- | In GPT-Monkey, the granularity of a function is jointly deter- |  |  |
| --- | --- | --- | --- | --- | --- |
| face association and achieves cross-modal alignment between the | mined by the spatial granularity of the entry area | E | and the |  |  |
| layout information in the text modality and the screenshot in the | path granularity of the associated interface set | A | . The entry area |  |  |
| image modality. Proceeding to step | ③ | , this information is encoded | E | corresponds to the smallest operable GUI area that triggers a |  |
| as a prompt and then sent to LLM. Subsequently, in step | ④ | , basic | speci | fi | c function (e.g., search, upload), and this area is bounded by |
| 4 of 29 | IET Software, | 2026 |  |  |  |

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

---

## Page 5

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| ① | Testing requirements proposed by | ③ | Prompt | ⑤ | Parameters modification from user |
| --- | --- | --- | --- | --- | --- |
| the user in natural language | User |  |  |  |  |
| User | e.g. “Please test the text input function.” | Testing requirements |  |  |  |

from user

User interaction feedback loop

| ② | Extract key | Establish global | Modified basic test |
| --- | --- | --- | --- |
| interface | interface | parameters |  |
| Target | information | association |  |
| app | and screenshot | ④ | LLM analysis |
| Class : *** | State 2 | Extracted | results |
| Resource-id : | interface layout |  |  |
| *** | Large language | (1) Associated interfaces |  |
| Node index : *** | Event 1 | model (LLM) | (2) Entry area coordinates |
| Text : *** | (3) Suggested parameters |  |  |

Event 2

Bounds : *** State 1 *** Screenshot

⑥ Parameter-RAG

Event 3 adb -s deviceID

Establish monkey test

| Global | shell monkey-p |
| --- | --- |
| State 3 | parameter knowledge |
| interface | com.example.myapp |
| Cross-modal | base |
| association | …… |

alignment

Monkey

log ⑧ Monkey based-kernel ⑦ Configuration file for specified function

executes testing

Log analysis

Monkey-based instruction feedback loop

⑨ Monkey testing log analysis feedback

FIGURE 2 | Framework of GPT-Monkey.

| the rectangle de | fi | ned by the boundaries of the relevant interface | avoiding test events that do not align with the current scenario |
| --- | --- | --- | --- |
| components at the layout hierarchy level. The associated interface | under the historical parameter con | fi | guration strategy. |

set A , starting from the entry interface, is derived from the global

interface state transition graph as a set of interface paths that are

4.2 | Testing Requirement Analysis

directly related to the function fl ow, rather than a simple enumer-

| ation of arbitrary activities. This granularity is automatically | GPT-Monkey allows the user to directly guide testing through |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| determined by the system to ensure consistency and reproducibil- | natural language descriptions. The testing requirements of the |  |  |  |  |  |  |  |  |  |
| ity. Users are not required to directly select a granularity level, but | user may involve various aspects, including testing function, test- |  |  |  |  |  |  |  |  |  |
| they can make adjustments to the relevant parameters by editing | ing duration, and so on. GPT-Monkey utilizes the LLM to obtain |  |  |  |  |  |  |  |  |  |
| the generated testing instruction. The granularity setting has a | the basic testing parameters primarily from the testing require- |  |  |  |  |  |  |  |  |  |
| substantive impact on the testing target, and inappropriate gran- | ments input by the user, while also referencing the interface lay- |  |  |  |  |  |  |  |  |  |
| ularity will signi | fi | cantly weaken the effectiveness of targeted test- | out, the interface screenshot, and the global interface association. |  |  |  |  |  |  |  |
| ing on the speci | fi | c function. | The basic parameters necessary to start testing are shown in |  |  |  |  |  |  |  |
| GPT-Monkey differentiates functions based on the user operation | Table 2, including | Device | , | Duration | , | Log Level | , | Output Path | , | Seg- |
| patterns and focuses on a few related parameters. Speci | fi | cally, by | ment Function? | , | Target | and | Other Parameters | . Among them, | Seg- |  |
| jointly analyzing the layout hierarchy, component types, text | ment Function? | and | Target | are considered the most important |  |  |  |  |  |  |
| labels, and global interface association information, GPT-Monkey | information indicated in the testing requirements. GPT-Monkey |  |  |  |  |  |  |  |  |  |
| can infer the operation patterns that the current target function | determines whether the function segmentation is needed in the |  |  |  |  |  |  |  |  |  |
| relies on, and then automatically adjust the event distribution in | testing requirements and then chooses | “ | Yes | ” | or | “ | No | ” | for | Segment |
| generated parameters, avoiding the waste of events under the | Functions? | . If the function segmentation is required, GPT-Monkey |  |  |  |  |  |  |  |  |
| random parameter con | fi | guration strategy. Under the guidance | determines which function to test for | Target | . | Other Parameters |  |  |  |  |
| of Parameter-RAG, GPT-Monkey tailors test parameters that are | refers to additional testing parameters beyond the basic con | fi | gura- |  |  |  |  |  |  |  |
| directly related to the current function (such as | — | pct-touch | , | — | pct- | tions, which are used to re | fi | ne Monkey testing behaviors and |  |  |
| motion | , | — | pct-nav | , etc.), rather than uniformly adjusting all | execution strategy. The main parameters among | Other Parameters |  |  |  |  |
| parameters. For example, for functions that primarily involve | are event distribution parameters (e.g., | — | pct-touch | , | — | pct-motion | , |  |  |  |
| browsing long lists, GPT-Monkey will increase the proportion of | — | pct-nav | ), which are tailored to speci | fi | c functions. In addition, it |  |  |  |  |  |
| swipe events and decrease the proportion of navigation events. | includes process control parameters (e.g., | — | ignore-crashes | , | — |  |  |  |  |  |
| Moreover, based on log analysis feedback, GPT-Monkey further | ignore-timeouts | ), which are intended for process control. Although |  |  |  |  |  |  |  |  |
| adjusts the proportions of key parameters, thereby balancing expe- | some basic parameters (e.g., | Device | , | Duration | , and | Output Path | ) |  |  |  |
| rience with context adaptivity in generated parameters and | can be manually con | fi | gured by the user, parameters directly |  |  |  |  |  |  |  |
| IET Software, | 2026 | 5 of 29 |  |  |  |  |  |  |  |  |

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

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

TABLE 2 | Basic testing parameters generated by LLM.

| Parameter | Parameter description | Parameter explanation |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Device | Testing device selection | Choose the appropriate device for testing. |  |  |  |  |  |  |  |  |  |  |
| Duration | Testing duration | Set the time duration for sending random events. |  |  |  |  |  |  |  |  |  |  |
| Log level | Log output level selection | Choose a mode from | “ | simple, | ” “ | middle, | ” | or | “ | complex | ” | levels. |
| Output path | Testing results output path | Set the log storage path for testing results. |  |  |  |  |  |  |  |  |  |  |
| Segment function? | User-de | fi | ned function segmentation | Decide whether to segment function, selected as | “ | Yes | ” | or | “ | No. | ” |  |
| Target | Testing function | Decide which function to test. |  |  |  |  |  |  |  |  |  |  |
| Other parameters | Additional testing parameters | Con | fi | gure parameters to control the proportion of different |  |  |  |  |  |  |  |  |

event types, such as – pct-touch , – pct-motion , and – pct-nav .

| related to test behaviors, such as | Segment Function? | , | Target | , and | function entry area. At the same time, the cross-modal alignment |
| --- | --- | --- | --- | --- | --- |
| event distribution parameters | , require contextual understanding of | between the extracted interface layout information and the |  |  |  |
| the app | ’ | s layout structure, user goals, and test target characteris- | screenshot is indispensable for LLM analysis, which can facilitate |  |  |
| tics, which is not available in manual con | fi | guration. The LLM | the recognition of dynamic content and the understanding of |  |  |
| helps reduce the user | ’ | s con | fi | guration effort, especially for non- | positional relationships between function entry areas. GPT-Mon- |
| experts, by automatically synthesizing this context into tailored | key gets access to the interface layout and the screenshot through |  |  |  |  |
| parameters. | the UI Automator tool [6]. However, the original layout | fi | le |  |  |

obtained by UI Automator is relatively complex, containing

GPT-Monkey employs the user interaction feedback method dur-

some information that may not be helpful to LLM in understand-

ing test requirements analysis to improve the reliability and

ing the interface and segmenting function entry area. To simplify

interpretability of the parameter con fi guration process while pre-

the original layout hierarchy, GPT-Monkey utilizes depth- fi rst

serving the fl exibility of human involvement. After receiving the

search (DFS) to implement tree traversal, simplifying the nodes

fi rst feedback from LLM, GPT-Monkey displays the basic param-

while effectively retaining the nested structure of the layout fi le.

eters on a visual interface in a modi fi able manner for user cus-

| tomization, and the modi | fi | ed parameters are then returned into | The simpli | fi | ed layout | fi | le hierarchy is given in Table 3. GPT-Mon- |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| the LLM prompt to further optimize the parameter con | fi | guration. | key extracts the | fi | ve attributes, containing | class | , | resource-id | , | node |
| This method is particularly useful in practice, as user testing | index | , | text | , and | bounds | , which satisfy the minimum requirements |  |  |  |  |
| requirements in natural language are often ambiguous. For exam- | for understanding the interface and obtaining coordinates for |  |  |  |  |  |  |  |  |  |
| ple, | “ | testing whether the payment is working properly | ” | may lack | function entry area segmentation. The | class | attribute de | fi | nes the |  |
| necessary information such as the target function or test duration. | type of GUI component, such as Button, TextView, and so on. |  |  |  |  |  |  |  |  |  |
| In such cases, GPT-Monkey utilizes LLM to supplement test | When identifying interface components, the | class | can help deter- |  |  |  |  |  |  |  |
| parameters that are not clearly speci | fi | ed in the user requirements, | mine the general behavior of a component. |  |  |  |  |  |  |  |

and then incorporates user modi fi cations, thus effectively han-

The resource-id provides a unique identi fi er for a component

dling ambiguous natural language input.

within an application, which is useful for identifying speci fi c

GUI components, especially in complex interfaces with multiple

similar components. The node index describes the order of a com-

4.3 | Key Interface Information Extraction and

ponent among its siblings, which is useful for locating the relative

Entry Area Segmentation

position of each component when there are multiple similar com-

Extracting key layout information of the function entry interface ponents. The text attribute contains the text content displayed by

is a necessary condition for LLM to accurately segment the the component, which is another intuitive way to identify and

TABLE 3 | Simpli fi ed layout fi le hierarchy.

Attribute Description Example

Class The complete class name of the GUI component, representing class = “ android.widget.ImageView ”

the type of the component.

| Resource-id | The resource ID of the GUI component, a unique identi | fi | er that | resource-id | = | “ | com.android. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| can call a uniquely speci | fi | c component within an app. | systemui:id/mobile _signal | ” |  |  |  |
| Node index | The index or position of the GUI component in the same | node index | = | “ | 0 | ” |  |

hierarchy.

| Text | The text displayed on the GUI component. | text | = | “ | mobile signal | ” |
| --- | --- | --- | --- | --- | --- | --- |
| Bounds | The position of the GUI component on the interface, formatted | bounds | = | “ | [984,48][1023,87] | ” |

as [ ∗∗ , ∗∗ ][ ∗∗ , ∗∗ ].

6 of 29 IET Software, 2026

---

## Page 7

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| describe the GUI component, especially when the function of a | understanding and interface reasoning abilities to analyze the |  |  |
| --- | --- | --- | --- |
| component is expressed through text content. The | bounds | attri- | positions and functions of interface components, thereby seg- |
| bute de | fi | nes the relative position of the component on the inter- | menting a rectangular area in the layout and screenshot that cor- |
| face in the format [left, top][right, bottom], which is crucial for | responds to the function entry area. |  |  |

determining the precise position of components and their posi-

tional relationships with each other.

4.4 | Interface Association Establishment and

In GPT-Monkey, the analysis of the targeted function entry area Segmentation

by LLM relies on both the layout information in text modality and

| the interface screenshot in image modality. The extracted layout | Establishing the interface association is crucial for LLM to accu- |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| information and the screenshot of the function entry interface are | rately segment the associated interfaces of the target function. The |  |  |  |  |  |  |  |  |
| simultaneously sent to LLM in a single interaction through a | establishment of the global interface association relies on a |  |  |  |  |  |  |  |  |
| designed prompt, closely linking the two modalities to achieve | dynamically constructed interface state transition graph, as shown |  |  |  |  |  |  |  |  |
| “ | external alignment. | ” | The cross-modal alignment method allows | in Figure 3a. GPT-Monkey utilizes DroidBot [30] to send various |  |  |  |  |  |
| LLM to accurately understand the interface layout and extract the | test inputs, such as touch, scroll, intent broadcast, etc., to trigger |  |  |  |  |  |  |  |  |
| coordinates of the function entry area. To accommodate potential | state transitions, explore the state space of the application, and |  |  |  |  |  |  |  |  |
| irregularities of the components, the entry area boundaries are | monitor the response of the application at runtime, thereby con- |  |  |  |  |  |  |  |  |
| aligned with the edges of the most marginal components, ensur- | structing a global state transition graph. The state transition graph |  |  |  |  |  |  |  |  |
| ing full coverage while minimizing redundancy. The result is out- | is a directed graph, in which each node represents an app state and |  |  |  |  |  |  |  |  |
| put as rectangular coordinates in the format [ | ∗∗ | , | ∗∗ | ][ | ∗∗ | , | ∗∗ | ]. | each edge between two nodes represents a test input event that |

triggers a state transition. State nodes usually contain GUI infor-

| For functions that involve multiple components within the same | mation and running process information. Event edges contain |
| --- | --- |
| interface jointly serving the same business goal, GPT-Monkey | detailed information about the test input and the methods/logs |

de fi nes the entry area as the union of the rectangles formed by

triggered by the input.

the layout bounds of all these components, thereby fully covering

| all required operational elements while avoiding irrelevant areas. | To evaluate the completeness of the global state transition graph, |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| For functions that can be triggered from multiple potential entry | GPT-Monkey uses the total number of all interfaces extracted |  |  |  |  |  |  |  |  |  |  |
| areas across different activities, these entry areas generally corre- | from the layout XML | fi | les as a reference. When the state graph |  |  |  |  |  |  |  |  |
| spond to different access paths. However, in a single targeted test, | constructed by DroidBot covers no less than 90 | % | of all interfaces, |  |  |  |  |  |  |  |  |
| GPT-Monkey performs function segmentation and testing starting | the graph is considered suf | fi | ciently complete. If the coverage |  |  |  |  |  |  |  |  |
| from only one entry interface, and accordingly de | fi | nes the func- | remains below this threshold, GPT-Monkey automatically calls |  |  |  |  |  |  |  |  |
| tion entry area solely with respect to the current interface. To | DroidBot iteratively to continue exploration until the threshold |  |  |  |  |  |  |  |  |  |  |
| cover all access paths associated with the same function, multiple | is satis | fi | ed. This strategy ensures that the constructed state transi- |  |  |  |  |  |  |  |  |
| targeted tests can be launched, each starting from a different entry | tion graph is comprehensive and representative, forming a solid |  |  |  |  |  |  |  |  |  |  |
| area on its corresponding interface. | foundation for subsequent interface analysis. |  |  |  |  |  |  |  |  |  |  |
| The effectiveness of the LLM employed in GPT-Monkey for seg- | However, there exist lots of redundant information in the global |  |  |  |  |  |  |  |  |  |  |
| menting the function entry area is primarily attributable to three | interface association graph constructed by DroidBot, which is use- |  |  |  |  |  |  |  |  |  |  |
| key capabilities. First, the prompt construction enables effective | less for LLM to segment the targeted function. For example, when |  |  |  |  |  |  |  |  |  |  |
| cross-modal alignment, allowing the LLM to understand both the | performing function segmentation, the events required to achieve |  |  |  |  |  |  |  |  |  |  |
| semantic content and interface structure. Second, the simpli | fi | ca- | the transition from one state to another are redundant. Hence, the |  |  |  |  |  |  |  |  |
| tion of layout data through DFS reduces cognitive load by preserv- | global interface association established by GPT-Monkey is shown |  |  |  |  |  |  |  |  |  |  |
| ing only essential attributes, enhancing the LLM | ’ | s ability to model | in Figure 3b, and only retains the | state_str | identi | fi | er, | foregroun- |  |  |  |
| UI | structures. | Third, | the | LLM | leverages | its | semantic | d_activity | information, | background_service | information in states |
| (a) | (b) |  |  |  |  |  |  |  |  |  |  |
| Start_state :** | Stop_state :** |  |  |  |  |  |  |  |  |  |  |
| Start_state :** | Stop_state :** |  |  |  |  |  |  |  |  |  |  |
| Tag_time :** | Event_type :** | Event_str :** |  |  |  |  |  |  |  |  |  |
| Event 3 | Segment associated interfaces |  |  |  |  |  |  |  |  |  |  |

Event 1

Event 1

Event 2 Establish global State 2

State 3

interface association

| State 1 | Event 2 |  |  |
| --- | --- | --- | --- |
| State 1 | State 2 | State 3 | Event 3 |
| State_str :** | Width and height :** | Stack :** |  |

State_str :**

Foreground_activity :** View_str :**

Background_services :** Views :** Foreground_activity :** Background_services :**

FIGURE 3 | (a) Dynamically constructed interface state transition graph. (b) Establishment and segmentation of global interface association by GPT-

Monkey.

IET Software, 2026 7 of 29

*[Image: Page 7 Image]*

*[Image: Page 7 Image]*

*[Image: Page 7 Image]*

*[Image: Page 7 Image]*

*[Image: Page 7 Image]*

---

## Page 8

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| nodes and | start_state | identi | fi | er, | stop_state | identi | fi | er in event | of the function | fl | ow. Second, GPT-Monkey simpli | fi | es the graph |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| edges. The retained information is suf | fi | cient to represent the asso- | structure when establishing interface association, retaining only |  |  |  |  |  |  |  |  |  |  |
| ciation relationships among interfaces and is presented in a text | the key states related to the function logic and their transition |  |  |  |  |  |  |  |  |  |  |  |  |
| format, which is convenient for LLM analysis. | paths in text forms that LLM can directly understand, so that |  |  |  |  |  |  |  |  |  |  |  |  |

LLM can focus on the judgment of the function path rather

Based on the global interface association, GPT-Monkey utilizes

than being disturbed by irrelevant transitions. Finally, GPT-Mon-

LLM to analyze and segment the associated interfaces of the tar-

key ’ s interface association uses function paths as units to guide

geted function starting from the function entry interface, output-

LLM to clearly segment the boundaries of functions. When

ting the result as a list of activities. In GPT-Monkey, the associated

encountering signals such as transition breaks and interfaces

interface set A takes activity/fragment as the basic unit, which is

jumping out of the current activity level, LLM recognizes them

an engineering compromise under the control granularity con-

as function boundaries, enabling LLM to autonomously segment

straints supported by existing Monkey testing frameworks, aiming functions based on structure and semantic logic under unsuper-

to reuse the existing testing kernel ’ s capability of fi ltering target vised conditions.

interfaces with minimal changes. However, GPT-Monkey does

not simply include all related activities in the testing set. Instead,

| based on the interface association graph constructed by DroidBot | 4.5 | \| | Parameter Tailoring and Instruction |
| --- | --- | --- | --- |
| and further simpli | fi | ed, GPT-Monkey starts from the entry inter- | Generation |

face, selects a connected subgraph that is tightly related to the

Testing instruction composed of tailored parameters is crucial for

execution path of the target function, and includes in A only the

GPT-Monkey to perform Monkey-based GUI testing on the target

interfaces that appear on this path. Consequently, although

functions. These functions may have unique user interaction pat-

the implementation operates at the activity/fragment level, it

terns, and generic testing parameters often execute routine opera-

semantically corresponds to the interface sequence that is neces-

tions, failing to effectively cover speci fi c behaviors and states.

sary or highly related to completing the function, thereby achiev-

Tailored testing parameters can more accurately re fl ect the oper-

ing effective focus on function-related interfaces while remaining

ation patterns of real users, reducing redundant operations and

compatible with the existing engineering foundation.

ineffective tests, thereby enhancing the ability to detect crashes.

Although the global interface state transition graph constructed

In GPT-Monkey, “ re fl ect the operation patterns of real users ” is

by DroidBot is not related to the target function, the interface

not intended to reproduce a user ’ s complete operation trace.

association established by the LLM in GPT-Monkey is tightly

Rather, under the semantic constraints of the speci fi c function,

related to the target function. Speci fi cally, the function fl ow con-

GPT-Monkey aims to make the event type distribution and inter-

text used by GPT-Monkey is extracted from the global interface

action paths of the generated events re fl ect the typical operation

state transition graph using LLM, based on the understanding of

patterns of real users on that function. Speci fi cally, by analyzing

the target function, test requirements, and the target function ’ s

the layout structure and semantics of the entry area and associated

entry interface. This function fl ow context starts from the function

interfaces, GPT-Monkey infers the interaction patterns that the

| entry interface and is a set of associated interfaces closely related | target function is more likely to rely on. It then adjusts the gener- |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| to the target function. The coordinates of the entry area and the | ation proportions of the corresponding event type parameters, |  |  |  |  |  |  |
| associated interfaces are combined to form the segmentation | such that a large number of random events adhere to the seman- |  |  |  |  |  |  |
| result of the target function. | tically reasonable operation pattern. |  |  |  |  |  |  |
| During test execution, GPT-Monkey utilizes the entry area | E | and | Although testing parameters are generic con | fi | guration items in |  |  |
| the associated interface set | A | jointly as an entry constraint and | Monkey, in GPT-Monkey, they are applied within a function- |  |  |  |  |
| path constraint on the test events, con | fi | ning Monkey | ’ | s inherent | speci | fi | c constraint scope. Based on this constrained scope, GPT- |
| randomness to execution paths tightly associated with the target | Monkey customizes standard Monkey parameters such as event |  |  |  |  |  |  |
| function, thereby ensuring that testing covers the speci | fi | c function | type proportions and event pacing. As a result, the effective |  |  |  |  |
| rather than merely the associated activities. In practice, overlaps | scope of these parameters is limited to components and inter- |  |  |  |  |  |  |
| among the associated interface sets of different functions are | face sequences that are directly related to the target function, |  |  |  |  |  |  |
| unavoidable in multi-function mobile systems, but this does not | enabling randomly generated events to be concentrated on |  |  |  |  |  |  |
| violate the fundamental purpose of associated interface segmen- | function | – | relevant interaction | fl | ows and signi | fi | cantly reducing |
| tation. The system con | fi | gures and executes the Monkey kernel | visits to irrelevant interface areas. |  |  |  |  |

only within the associated interfaces of the current function,

However, while the extracted interface layout information and the

and compared with random testing over all interfaces, this

segmented function can address the contextual understanding

method still substantially shrinks the testing space and improves

de fi ciencies of LLM in generating tailored parameters, a lack of

the utilization ef fi ciency of event inputs.

fi eld knowledge still exists. This may lead to the testing parame-

| The effectiveness of the LLM employed in GPT-Monkey for func- | ters generated by LLM being overly generalized and simpli | fi | ed. To |  |  |
| --- | --- | --- | --- | --- | --- |
| tion segmentation is primarily attributable to the fact that GPT- | address this issue, GPT-Monkey employs RAG technology to oper- |  |  |  |  |
| Monkey | ’ | s interface association establishment signi | fi | cantly | ate a parameter-RAG method, which guides LLM in generating |
| enhances the LLM | ’ | s reasoning capability in three aspects. First, | tailored testing parameters by providing prede | fi | ned parameter |
| GPT-Monkey | ’ | s interface association provides LLM with interface | knowledge from an external knowledge base. The framework of |  |  |
| context and solves the problem of interface isolation, organizing | the parameter-RAG method is illustrated in Figure 4. The param- |  |  |  |  |
| the transition relationship between interfaces in text form to form | eter-RAG method primarily consists of the following processes: |  |  |  |  |
| a logical sequence, which helps LLM establish the overall context | constructing a knowledge document, converting text to vectors, |  |  |  |  |
| 8 of 29 | IET Software, | 2026 |  |  |  |

---

## Page 9

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

(Basic test parameters, layout )

(Global interface association)

Prompt Embedding model Retrieve recall LLM Response

Text chunk_1

Text chunk_2

Text chunk_3

| Knowledge | . | . |
| --- | --- | --- |
| document | . |  |
| Knowledge text chunks | Vector database | Memory base |

FIGURE 4 | Framework of the parameter-RAG method.

TABLE 4 | Partial content of the knowledge document.

| Attribute | Description |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| -s | < | seed | > | Specify a seed value to ensure reproducible randomness in the testing. |  |
| – | pct-touch | < | percent | > | Set the percentage of touch events, such as taps and long presses, focusing on direct |

screen interactions that involve single points of contact.

– pct-motion < percent > De fi ne the percentage of motion events, like swipes or drags, which track the

movement of touch across the screen, providing a different test dynamic from static

touch events by simulating continuous fi nger paths.

– pct-trackball < percent > Set the percentage of trackball movements, like scrolling or clicking, offering a unique

input method separate from touchscreen interactions, useful for devices equipped with

physical trackballs or simulated controls.

– pct-nav < percent > Determine the percentage of basic navigation events, including directional pad

movements and focusing on simple navigation.

– pct-majornav < percent > Specify the percentage of major navigation events, such as selections and menu

interactions, which involve more signi fi cant navigation choices compared to basic

navigation, adding complexity in user interaction.

– pct-syskeys < percent > Con fi gure the percentage of system key presses, like home, back, and volume keys,

involving system control keys that affect the overall operation of the device.

– pct-anyevent < percent > Provide a fl exible percentage for any type of event, creating a diverse and randomized

testing environment that combines all other types of interactions, ensuring a

comprehensive stress testing across all functions.

| establishing a vector database, querying retrieval, and generating | achieve the conversion, as it can provide context-aware represen- |
| --- | --- |
| responses. | tations by capturing the context of each word, allowing for a |

deeper understanding of semantics. Additionally, the embedding

During the knowledge document construction process, the plain text

model can encode each token into a multi-dimensional vector,

data is used to clarify the function that each parameter can achieve,

effectively capturing complex semantic relationships and linguis-

providing a detailed natural language annotation for Monkey ’ s test

tic patterns within the text, thus achieving a more comprehensive

parameter set, as shown in Table 4. The knowledge document is split

representation. The speci fi c conversion process is given as follows.

using parameter attributes and natural language description as the

granularity, where each parameter and its corresponding semantic

description form a complete retrieval chunk. This granularity 4.5.1 | Tokenization

ensures that the attribute and semantic description related to a spe-

| ci | fi | c parameter can be obtained simultaneously when retrieval, | The cl100k_base tokenizer in the embedding model splits the |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| thereby avoiding semantic fragmentation. Meanwhile, it allows the | input text | S | into a sequence of tokens, denoted as | P | . De | fi | ne the |
| LLM to selectively integrate multiple retrieval chunks to generate | tokenizer function as Tokenizer( | S | ), and then the process is repre- |  |  |  |  |
| tailored instructions according to the current testing requirements | sented as: |  |  |  |  |  |  |

and target function.

P ¼ Tokenizer ð Þ ¼ S ½ p 1 ; p 2 ; … ; pn  ;

The process of converting text to vectors consists of four steps,

| including tokenization, encoding, pooling, and normalization. | where | pi | is the | i | th token and | n | is the number of tokens. For |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The embedding model text-embedding-ada-002 is employed to | example, for the input | S | = | – | pct-touch | < | percent | > | , the WordPiece |
| IET Software, | 2026 | 9 of 29 |  |  |  |  |  |  |  |

*[Image: Page 9 Image]*

*[Image: Page 9 Image]*

*[Image: Page 9 Image]*

*[Image: Page 9 Image]*

*[Image: Page 9 Image]*

*[Image: Page 9 Image]*

*[Image: Page 9 Image]*

*[Image: Page 9 Image]*

*[Image: Page 9 Image]*

*[Image: Page 9 Image]*

*[Image: Page 9 Image]*

*[Image: Page 9 Image]*

---

## Page 10

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| tokenizer would likely split it into | P | = | Tokenizer( | S | ) | = | [ | “ | – | ” | , | “ | pct | ” | , | are combined and input into LLM to obtain responses. Conse- |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| “ | - | ” | , | “ | touch | ” | , | “ | < | percent | > | ” | ], with | n | = | 5. This ensures that the | quently, a testing instruction containing tailored test parameters |
| parameter and its components are tokenized into manageable | under the guidance of the knowledge base is generated. Finally, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| units for semantic understanding and vectorization. | GPT-Monkey sends the instruction to the Monkey-based testing |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

kernel for automated testing on the target function.

4.5.2 | Encoding GPT-Monkey adopts a parameter-RAG mechanism to retrieve the

parameters most relevant to the current testing requirements and

Through multi-layer Transformer encoders, the embedding model

target function, effectively controlling context length while ensuring

outputs a vector of size d for each token pi . The encoding process

the correctness of parameters. First, due to current engineering con-

can be represented as:

straints on prompt length, incorporating the entire knowledge docu-

ment into the prompt may exceed the maximum input length and

H s ¼ Encoder ð Þ ¼ P ½ h 1 ; h 2 ; … ; h n  ;

thus fail to meet our practical usage requirements. GPT-Monkey ’ s

prompt simultaneously includes dynamic content such as the user

where h i is the vector representation of the i th token, with h i 2

| R | d | . Thus, the entire sentence | ’ | s vector representation is a matrix | requirements, interface layout, screenshots, global interface associa- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H | s | of size | n | × | d | . Besides, | d | = | 1536 for the embedding model. For | tions, and testing log, which already consume substantial context |  |  |  |  |  |  |  |  |  |  |  |  |  |
| example, | for | the | input | S | = | – | pct-touch | < | percent | > | , | H | s | ¼ | space. If the complete parameter knowledge document were directly |  |  |  |  |  |  |  |  |
| Encoder | ð | P | Þ | : | ¼ ½ | h | 1 | ; | h | 2 | ; | … | ; | h | 5 |  | : | is the 5 | × | 1536 dimensional matrix. | concatenated into the prompt, it would signi | fi | cantly increase prompt |

length, reduce processing ef fi ciency, and consume context budget

that should be reserved for dynamic information, which is critical

4.5.3 | Pooling to the current interface and target function. Second, since the param-

eter knowledge document contains largely static information, repeat-

After the encoding process, the embedding model applies pooling

edly including it in every prompt would be inef fi cient and would

to aggregate token representations into a single vector for the

unnecessarily consume context resources.

entire input. In average pooling, the representation is obtained

by averaging the vectors of all tokens in the sequence:

4.6 | Log Analysis Feedback and Dual-Feedback

1

v s ¼ Pooling ð H s Þ ¼ ∑ n

n i ¼ 1 h i : Mechanism Establishment

To achieve optimized testing results, GPT-Monkey iteratively

The pooled vector v s represents the overall meaning of the input.

improves LLM instructions by analyzing test results, forming a

log analysis feedback loop. In the log analysis feedback loop, GPT-

4.5.4 | Normalization Monkey leverages test logs collected during the prior testing loop

to automatically re fi ne and adjust subsequent parameter con fi g-

| Normalization adjusts the vector | ’ | s magnitude to a | fi | xed range, | urations. After a test completes, the system analyzes crash reports, |
| --- | --- | --- | --- | --- | --- |
| often by ensuring its length (L2 norm) equals to 1. This process | event traces, logcat outputs, and coverage data to extract high- |  |  |  |  |
| helps maintain numerical stability and ensures that the vector | ’ | s | level signals such as untested interface states, frequent failure |  |  |
| magnitude does not affect subsequent calculations, focusing | points, or ineffective parameter combinations. These signals are |  |  |  |  |
| purely on its direction. The normalized vector | v | s | is calculated | then encoded as structured feedback, which is incorporated into |  |
| using the following formula: | the LLM prompt of the next loop to guide the generation of more |  |  |  |  |
| v | targeted and effective parameters. |  |  |  |  |

s

v s ¼ Normalize ð v s Þ ¼ ;

k v s k GPT-Monkey uses the global interface state transition graph con-

structed by DroidBot as the reference, and obtains the covered

where k v s jj : is the L2 norm of the vector v s ¼ ½ vs 1 ; vs 2 … ; vsd  T with

q ffiffiffiffiffiffiffiffiffiffiffiffiffiffi states by parsing the logs. A state is regarded as tested if it is

k v s jj : ¼ ∑ d 2

j ¼ 1 v s j . The normalized vector v s has a unit length of 1 instantiated in the logs and has triggered at least one valid GUI

event. A failure point is de fi ned as the failure triggering location

while retaining the direction of v s .

and triggering conditions that can be localized based on the testing

| Hence, for the text input | S | , the vector representation process can | log. It is structured as the triple | < | activity name, event type, |
| --- | --- | --- | --- | --- | --- |
| be expressed by: | resource identi | fi | er | > | , which is used to support subsequent param- |

eter adjustments and instruction generation. This de fi nition is

v s ¼ Normalize Pooling Encoder Tokenizer ð ð ð ð Þ S Þ Þ Þ : consistent with the commonly used failure localization method

in mobile GUI testing. An ineffective parameter combination

All vectors converted by the embedded model are stored in a

refers to a parameter set that, under a given event budget, consis-

vector database, which is speci fi cally designed for storing and

tently contributes less than a conservative threshold to new cov-

retrieving vector data.

erage or does not lead to any new effective exploration. Its scale is

| During the querying retrieval process, the text information in the | related to factors such as testing target, function characteristics, |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| prompt | fi | rst needs to be vectorized, which involves the basic test | log length, testing duration, and event number. For instance, in a |  |  |  |  |
| parameters modi | fi | ed by the user, the extracted interface layout | speci | fi | c function, the swipe events or navigation events are weakly |  |  |
| and the global interface association. Next, the vector database is | correlated with the current function path. Accordingly, | — | pct- |  |  |  |  |
| searched for knowledge texts that are semantically similar to the | motion | and | — | pct-nav | are classi | fi | ed as ineffective parameter |
| prompt vector. Then, the prompt and the retrieved information | combinations. |  |  |  |  |  |  |
| 10 of 29 | IET Software, | 2026 |  |  |  |  |  |

---

## Page 11

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| This log-driven feedback process enables GPT-Monkey to learn | initiates the execution of the test. After the | fi | rst testing completes, |
| --- | --- | --- | --- |
| from prior test executions and improve its behavior over time. By | the interface returns to Interface 3, where the LLM analyzes the |  |  |
| combining LLM | ’ | s reasoning capabilities with empirical test | test logs and results, and automatically generates an optimized |
| results, the system ensures that generated parameters are not | instruction for the next test, thus enabling a feedback loop for |  |  |
| only context-aware but also experience-driven. As a result, GPT- | adaptive automated testing. |  |  |

Monkey can adapt its con fi guration strategy across different apps,

As the log analysis feedback loop is completed through two con-

enhancing test ef fi ciency and reliability.

secutive steps, the prompt is constructed separately for these two

| GPT-Monkey employs a dual-feedback mechanism that inte- | steps as shown in Figure 7. In step 1, as illustrated in Figure 7a, |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| grates the user interaction feedback loop and log analysis feed- | the LLM is provided with the test requirements, entry area coor- |  |  |  |  |
| back loop. The dual-feedback mechanism algorithm used for test | dinates, interface associations, and parameter con | fi | guration, and |  |  |
| requirements analysis is shown in Algorithm 1. The user interac- | is instructed to produce a structured intermediate report with |  |  |  |  |
| tion feedback loop is triggered when each test starts and is termi- | three | fi | elds, including UntestedStates, FailurePoints, and Inef- |  |  |
| nated only when the user con | fi | rms the basic parameters on the | fectiveParas, which capture uncovered states, failure triggering |  |  |
| visual interface. Upon con | fi | rmation, the system compiles the | locations, and low contribution parameters, respectively. In step |  |  |
| parameter set, generates the corresponding execution instruc- | 2, as illustrated in Figure 7b, the LLM leverages this intermediate |  |  |  |  |
| tion, and launches the test. After the test, if the test logs are | report together with the original con | fi | guration to propose the |  |  |
| available, the system enters the log analysis feedback loop and | next round testing con | fi | guration, including entry area coordi- |  |  |
| then updates the parameter con | fi | guration to drive the next round | nates, an updated interface association, and re | fi | ned testing |
| of testing. As shown in Algorithm 1, the log analysis feedback | instructions. |  |  |  |  |

loop is a multi-round explicit loop, rather than a one-time

branch. GPT-Monkey utilizes the UI Automator [6] provided by the

Android SDK to obtain the interface layout fi le and the interface

screenshot, uses DroidBot [30] to establish a global interface asso-

5 | Implementation ciation, employs the Android Debug Bridge (ADB) [31] to interact

with applications, and uses the Maxim [8] as a Monkey-based

| GPT-Monkey is implemented as a fully automated GUI testing | testing kernel. For LLM, GPT-Monkey utilizes the pre-trained |
| --- | --- |
| tool, which is applicable to real devices and emulators with | GPT-4o model [17] released by OpenAI. The core code of GPT- |
| Android 5, 6, 7, 8, 9, 10, 11. The encapsulated GPT-Monkey con- | Monkey is open source at https://github.com/Project-YZH/GPT- |
| sists of three interfaces, as shown in Figure 5. Interface 1 is | Monkey. |

designed for inputting testing requirements described in natural

| language. Interface 2 directly displays the basic test parameters | Notably, GPT-Monkey is not restricted to GPT-4o for function |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| analyzed by LLM and allows the user to modify them. Interface 3 | segmentation and parameter generation and can be integrated |  |  |  |  |  |  |
| presents the content of the | fi | nal con | fi | guration | fi | le, including the | with models possessing multimodal understanding capabilities. |
| entry area coordinates of the target function and its associated | Multiple mechanisms have been employed in GPT-Monkey to |  |  |  |  |  |  |
| interface activities, as well as the testing instruction that will be | enhance reproducibility while mitigating the LLM hallucinations. |  |  |  |  |  |  |
| sent to the Monkey-based testing kernel. | First, to improve reproducibility, the same prompt template is |  |  |  |  |  |  |
| After the user inputs testing requirements in Interface 1, such as | “ | I | designed in GPT-Monkey for all LLM calls, ensuring reproduc- |  |  |  |  |
| want to test the add note function on the current interface for 2 | ible output under the same input conditions. This standardized |  |  |  |  |  |  |
| min, | ” | and then clicks the Con | fi | rm button, the user | ’ | s testing | prompt structure also ensures the stability of the output when |
| requirements, the extracted interface layout, the interface screen- | calling LLM multiple times. Second, GPT-Monkey supports |  |  |  |  |  |  |
| shot and the global interface association are compiled into a | using different LLMs in place of GPT-4o. Multimodal models |  |  |  |  |  |  |
| prompt (as shown in Figure 6a) and sent to LLM for analysis. | such as GPT-3.5, Claude 2, and Gemini Pro have been veri | fi | ed |  |  |  |  |
| The LLM processes this information to generate basic test param- | to perform the same function segmentation and parameter gen- |  |  |  |  |  |  |
| eters, which are displayed in Interface 2. | eration tasks. To reduce costs, GPT-Monkey only calls the LLM |  |  |  |  |  |  |

during function segmentation and parameter generation, which

In Interface 2, the user can review and, if necessary, modify

is infrequent. The other modules of GPT-Monkey, such as inter-

parameters, including the device ID, test duration, log level, out-

face information extraction, layout fi le processing, and global

put path, function segmentation option, and target function.

state graph construction, are handled by local tools (such as

Once satis fi ed, the user clicks the Con fi rm button again, which

UIAutomator and DroidBot). Furthermore, the parameter-RAG

triggers the system to recompile the modi fi ed basic test parame-

module is introduced in GPT-Monkey to guide the LLM ’ s output

ters, along with the extracted interface layout, the interface

in a knowledge-enhanced manner, avoiding invalid generation

screenshot, and the global interface association into an updated

and reducing resource waste. Finally, to address the problem of

prompt (as shown in Figure 6b), and it is subsequently sent back

hallucinations, GPT-Monkey incorporates a parameter-RAG

to LLM for further analysis. The LLM processes this information

module and a user interaction feedback mechanism. The param-

to segment the targeted function entry area and its associated

eter-RAG module provides structured, high-quality parameter

interfaces, as well as generate the test instruction, which is

knowledge support, signi fi cantly reducing the risk of LLM gen-

then presented in Interface 3.

erating invalid parameters. The user interaction feedback mech-

| In Interface 3, the user can check the identi | fi | ed entry coordinates, | anism allows users to manually modify test parameters, thereby |
| --- | --- | --- | --- |
| the list of related activities, and the constructed Monkey testing | ensuring the stability of the testing process and the reliability of |  |  |
| instruction. By clicking the Send Instruction button, the user | the results. |  |  |
| IET Software, | 2026 | 11 of 29 |  |

---

## Page 12

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

ALGORITHM 1 | Dual-Feedback Mechanism

Input: user_requirements, layout, screenshot, interface_association

Output: fi nal_parameters

| 1: | input | ← | (user_requirements, layout, screenshot, interface_association) |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2: | r | ← | 1; | user_stop | ← | False; | test_logs | ← | None |  |  |  |  |  |  |
| 3: | parameters | ← | LLM_GenerateBasicParameters( | input | ) |  |  |  |  |  |  |  |  |  |  |
| 4: | //(A) User Interaction Feedback Loop | — | intra-round |  |  |  |  |  |  |  |  |  |  |  |  |
| 5: | while ( | user_stop | = | False) do |  |  |  |  |  |  |  |  |  |  |  |
| 6: | con | fi | rmed | ← | False |  |  |  |  |  |  |  |  |  |  |
| 7: | while ( | con | fi | rmed | = | False) and ( | user_stop | = | False) do |  |  |  |  |  |  |
| 8: | Display( | parameters | ) on the visual parameter interface |  |  |  |  |  |  |  |  |  |  |  |  |
| 9: | feedback | ← | GetUserFeedbackFromUI() |  |  |  |  |  |  |  |  |  |  |  |  |
| 10: | if | feedback | = | STOP then |  |  |  |  |  |  |  |  |  |  |  |
| 11: | user_stop | ← | True |  |  |  |  |  |  |  |  |  |  |  |  |
| 12: | else if | feedback | is CONFIRMED then |  |  |  |  |  |  |  |  |  |  |  |  |
| 13: | con | fi | rmed | ← | True |  |  |  |  |  |  |  |  |  |  |
| 14: | else |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 15: | parameters | ← | ApplyUserEdits( | parameters | , | feedback | ) |  |  |  |  |  |  |  |  |
| 16: | end if |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 17: | end while |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 18: | if | user_stop | = | True then //Termination: user con | fi | rms the basic parameters on UI |  |  |  |  |  |  |  |  |  |
| 19: | break |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20: | end if |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 21: | //(B) Execute One-Round Test - round | r | starts after con | fi | rmation |  |  |  |  |  |  |  |  |  |  |
| 22: | instruction_r | ← | LLM_GenerateExecutionInstruction( | input | , parameters) |  |  |  |  |  |  |  |  |  |  |
| 23: | test_logs | ← | ExecuteTest( | instruction_r | ) //blocks until the round | fi | nishes |  |  |  |  |  |  |  |  |
| 24: | //(C) Log Analysis Feedback Loop - cross-round (explicit) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 25: | if | test_logs | ≠ | None then //Trigger: round | fi | nished and | test_logs | ≠ | None |  |  |  |  |  |  |
| 26: | //Step-1: structured intermediate analysis (strictly constrained | fi | elds) |  |  |  |  |  |  |  |  |  |  |  |  |
| 27: | log_feedback | ← | LLM_LogAnalysis( | input | , | parameters | , | test_logs | ) |  |  |  |  |  |  |
| 28: | // | log_feedback | = | {UntestedStates, FailurePoints, IneffectiveCombos} |  |  |  |  |  |  |  |  |  |  |  |
| 29: | //Step-2: update next-round con | fi | guration/instruction under log feedback |  |  |  |  |  |  |  |  |  |  |  |  |
| 30: | ( | input | , | parameters | ) | ← | LLM_UpdateNextRoundCon | fi | g( | input | , | parameters | , | log_feedback | ) |
| 31: | //If UntestedStates detected: trigger retesting mechanism |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 32: | //(prioritize untested interfaces by mapping to entry area | E | and set | A | ) |  |  |  |  |  |  |  |  |  |  |
| 33: | else |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 34: | //Robustness fallback: skip log-driven update for this round |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 35: | //(parameters unchanged; proceed to next round unless user stops) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 36: | end if |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 37: | r | ← | r | + | 1 |  |  |  |  |  |  |  |  |  |  |

38: end while

39: fi nal_parameters ← parameters

40: Output fi nal_parameters

12 of 29 IET Software, 2026

---

## Page 13

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Interface 1: Interface 2: Interface 3:

FIGURE 5 | GPT-Monkey interfaces.

| (a) | User requirements | Interface layout | Interface screenshot | Interface association | Task |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| e.g: | e.g: | e.g: | e.g: | e.g: | e.g: | e.g: |  |  |
| Please test the text input | Class : ** | State: state_str : ** | Generate the basic testing parameters primarily from the testing |  |  |  |  |  |
| function | Resource-id : ** | ** | Foreground_activity : ** | requirements input by the user, while also referencing the interface |  |  |  |  |
| Node index : ** | Background_services : ** | layout, the interface screenshot and the global interface association. |  |  |  |  |  |  |
| Text : ** | Event: start_state : ** | The basic parameters should include | device | , | duration | …… |  |  |
| Bounds : ** | Stop_state : ** |  |  |  |  |  |  |  |
| (b) | Basic parameters | Interface layout | Interface screenshot | Interface association | Task |  |  |  |
| e.g: | e.g: | e.g: | e.g: | e.g: | e.g: | e.g: | e.g: | e.g: |
| Device : ** Duration : ** | class : ** | State: state_str : ** | Comprehensively analyze basic parameters, the interface layout, |  |  |  |  |  |
| Log level : ** | resource-id : ** | foreground_activity : ** | the interface screenshot, and the global interface association. |  |  |  |  |  |
| Output path : ** | node index : ** | background_services : ** | Segment the targeted function entry area and its associated |  |  |  |  |  |
| Segment function? : ** | Text : ** | Event: start_state : ** | interfaces. Generate the test instruction based on the segmentation |  |  |  |  |  |
| Target : ** | bounds : ** | stop_state : ** | results. |  |  |  |  |  |

Other parameters : **

FIGURE 6 | (a) Initial prompt compilation for LLM analysis. (b) Re fi ned prompt compilation for function segmentation.

(a) Task Inputs (round r) Definitions and criteria Required output format

e.g: e.g: e.g: e.g:

Given the testing requirement and the logs from (1) Test requirements - Tested interface state: A state is "tested" if it is instantiated in the logs and triggers at least one valid GUI event UntestedStates:

| the last round, produce a structured intermediate | (2) Entry area coordinates | during its lifetime. | [ ... ] |
| --- | --- | --- | --- |
| analysis containing only three fields: | - Failure point: The smallest localized failure-triggering unit supported by log evidence. |  |  |
| Untested States, failure Points, ineffective Combos. | (3) Interface association | FailurePoints: |  |
| (4) Last round parameters | - Ineffective parameter combination: A parameter subset that, under the event budget, consistently contributes less | [ ... ] |  |
| (5) Test logs | than a conservative threshold to NEW coverage and does not lead to effective exploration. | IneffectiveCombos: |  |

[ ... ]

Formatting details:

……

| (b) | Task | Task | Inputs (Round r) | Inputs (round r) | Decision policy | Decision policy | Required output format | Required output format |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| e.g: | e.g: | e.g: | e.g: |  |  |  |  |  |
| Using (1) the original testing context and (2) the | (1) Test requirements: | - If Untested states is non-empty, trigger the retesting mechanism: | NextEntryAreaCoordinates: |  |  |  |  |  |
| structured log analysis feedback from the last | (2) Layout and screenshot: | (a) prioritize reaching untested interfaces/states; | { ... } |  |  |  |  |  |

round, produce the next-round configuration and a (3) Current entry area coordinates (b) Map untested states to corres ponding entry area E and associated interface set A when possible; NextInterfaceAssociation:

| concrete execution instruction. | (4) Current interface association | (c) Filter/construct parameter settings that increase reachability and functional relevance for those states. | { ... } |
| --- | --- | --- | --- |
| (5) Current parameters | - Always: | UpdatedParameters: |  |
| (6) Log analysis feedback: | (a) Down-weight or avoid Ineffective combos; | { ... } |  |
| Untested states | (b) Mitigate failure points by adjusting event types, target widgets, timing, navigation strategy, or constraints; | ExecutionInstruction: |  |
| Failure points | (c) Keep changes minimal but targeted; preserve stable settings unless they conflict with feedback. | { ... } |  |
| Ineffective combos | Field requirements: |  |  |

……

FIGURE 7 | (a) Prompt for intermediate log analysis report generation. (b) Prompt for testing con fi guration update.

6 | Evaluation In the evaluation of GPT-Monkey, we chose the standard testing

benchmark and the real-world application testing benchmark,

6.1 | Experimental Setup

respectively. The chosen standard testing benchmark is Themis

| The main innovation of GPT-Monkey lies in segmenting the spe- | [16], consisting of 20 open-source applications from GitHub, |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ci | fi | c function of the mobile app and achieving targeted testing, | which is commonly utilized in the GUI testing | fi | eld. For these |
| through combining the randomness of traditional Monkey-based | 20 apps, 68 critical functions are manually segmented based on |  |  |  |  |
| GUI testing with the powerful analytical abilities of LLM. The | the apps | ’ | function descriptions and there are 52 known crashes. |  |  |
| evaluation of GPT-Monkey is divided into two parts. To evaluate | Additionally, the chosen real-world application testing bench- |  |  |  |  |
| the usefulness of GPT-Monkey, we focus on the accuracy of spe- | mark is composed of the top 1000 popular applications from the |  |  |  |  |
| ci | fi | c function segmentation. To evaluate the effectiveness of GPT- | ranking of Google Play [32] on September 8, 2024, which cover 22 |  |  |
| Monkey, we concentrate on assessing its detection rate and ef | fi | - | different categories. For these 1000 apps, 3337 critical functions |  |  |
| ciency in detecting app function crashes. | are manually segmented based on the apps | ’ | function descriptions. |  |  |
| IET Software, | 2026 | 13 of 29 |  |  |  |

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

---

## Page 14

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| We adopt a speci | fi | c segmentation rule to control the quality of the | after entering the execution path of the target function from an |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| results. The core of this rule is to take the main navigation tabs or | entry area, all subsequent interfaces in this path are identi | fi | ed as |  |  |  |  |
| business entry points on the main interface as the function entry | the function associated interfaces, and we no longer identify indi- |  |  |  |  |  |  |
| point, and require that the identi | fi | ed two-tuple ( | E | , | A | ) can clearly | vidual UI elements within each interface. We consider that even |
| distinguish subsequent interface associations in the global inter- | elements on an identi | fi | ed activity that are not directly related to |  |  |  |  |
| face association graph, thereby achieving high coupling among | the target function may trigger potential crashes in the current |  |  |  |  |  |  |
| interfaces within the same business | fl | ow and low coupling across | entry point or function execution path. Therefore, GPT-Monkey |  |  |  |  |
| different business | fl | ows. The segmentation process strictly relies | treats all UI elements on an identi | fi | ed activity as associated with |  |  |
| on a rule-based identi | fi | cation framework to ensure that repeated | the target function | ’ | s execution path to avoid overlooking potential |  |  |
| operations under the same device and initial interface conditions | crash risks. |  |  |  |  |  |  |

can stably reproduce the same ( E , A ) segmentation result. Speci fi -

The entry areas of different target functions do not overlap,

cally, we prioritize segmenting functions corresponding to the

whereas for the associated interfaces, only a small number of

main navigation tabs on the app ’ s main interface (e.g., bottom

shared interfaces may overlap. For the entry area, on the same

tabs or main menus). If the main interface does not provide

interface, as long as the target functions do not overlap, their entry

explicit navigation tabs, we further segment functions based on

areas will not overlap, and the boundaries of the minimum rect-

business entry points on the main interface (e.g., search or

angular covering entry areas will not overlap. For the associated

upload). This uni fi ed segmentation strategy balances reproduc-

interface, a small number of interfaces (e.g., system permission

| ibility and testing cost. | dialogs) are available for multiple functions to share, so overlap is |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Function segmentation in the Themis dataset is completed by the | unavoidable. However, such shared interfaces may trigger poten- |  |  |  |  |  |  |
| authors under a uni | fi | ed segmentation rule. In addition, function | tial crashes at the current entry point or function execution path. |  |  |  |  |
| segmentation in the real-world dataset is performed, under the | Therefore, such overlapping interfaces are permitted during |  |  |  |  |  |  |
| same rule, by 10 graduate students in our research area whom we | the test. |  |  |  |  |  |  |
| invited. All the operators follow the uni | fi | ed segmentation rule and | In the usefulness evaluation, | fi | rst, we evaluate GPT-Monkey | ’ | s |
| operational procedures, ensuring manual segmentation consis- | accuracy of function segmentation within the standard testing |  |  |  |  |  |  |
| tency. The speci | fi | c operation procedure for manual function seg- | benchmark. Second, acknowledging the potential limitations of |  |  |  |  |
| mentation is consistent with the automated segmentation method | the standard benchmark, we further evaluate GPT-Monkey | ’ | s |  |  |  |  |
| proposed in this paper, except that the automated tool is replaced | accuracy of function segmentation within the real-world applica- |  |  |  |  |  |  |
| by manual annotation. Speci | fi | cally, the operators | fi | rst identify the | tion testing benchmark. The function can only be considered cor- |  |  |
| entry area | E | of each function based on the main navigation tabs or | rectly segmented when both the function entry area and the |  |  |  |  |
| business entry points on the app | ’ | s main interface. Then, they | associated interfaces of the function are correctly segmented. |  |  |  |  |

mark its corresponding associated interface set A in the global

interface association graph starting from this entry interface. In the effectiveness evaluation, fi rst, the number of crashes

detected by GPT-Monkey in the standard testing benchmark is

| Function size is mainly determined by the size of its correspond- | recorded as the metric for detection rate. Second, the time spent by |  |  |
| --- | --- | --- | --- |
| ing associated interface set. This size is tightly related to the app | GPT-Monkey to detect crashes in the standard benchmark is |  |  |
| design. For example, functions corresponding to bottom or top | recorded as the metric for detection ef | fi | ciency. Third, the ability |
| main navigation items are usually larger, since they have more | of GPT-Monkey to detect crashes is further evaluated in the real- |  |  |
| reachable interfaces and a more complex business | fl | ow. For each | world application testing benchmark. It is worth noting that due |
| function, the interface-level size metric is adopted to support the | to differences in testing mechanisms, GPT-Monkey uses the num- |  |  |
| tailoring of related parameters and the adjustment of event distri- | ber of detected crashes and the time taken to detect crashes as |  |  |
| bution for targeted testing. | effectiveness evaluation metrics, rather than using activity and |  |  |

code coverage as metrics.

The manual function segmentation method is not unique and

| function segmentation can indeed be performed at different gran- | To better assess its detection effectiveness in the standard testing |  |  |
| --- | --- | --- | --- |
| ularities, but since segmentation on experimental datasets is used | benchmark, GPT-Monkey is compared with four other Monkey- |  |  |
| solely to facilitate experimental veri | fi | cation, we applied this uni- | based automated GUI testing methods (APE [9], ComboDroid |
| fi | ed manual function segmentation rule to both the Themis | [11], Monkey [4], and TimeMachine [10]) and two non-Mon- |  |
| benchmark and the real-world application benchmark during | key-based automated GUI testing methods (Q-testing [13] and |  |  |
| experiments. In addition, since crashes in the Themis benchmark | Stoat [33]). Among them, APE, ComboDroid, Stoat, Q-testing |  |  |
| are known, we require that the function segmentation results for | and TimeMachine methods are from academia, and Monkey is |  |  |
| each Themis app align with these known crashes and their corre- | from industry, representing the advanced techniques in auto- |  |  |
| sponding function paths to facilitate experimental validation. | mated GUI testing. To ensure reasonable resource utilization, |  |  |
| Although functions can be segmented at a | fi | ner granularity, the | the time limit of detecting each app for each method is set to |
| strategy based on main navigation tabs or business entry points on | 300 min, a common setting in other GUI testing studies. In the |  |  |
| the main app | ’ | s interface that we adopt can better balance repro- | GPT-Monkey detection, 300 min are evenly divided among several |
| ducibility and testing cost. | functions of each app, and the detection starts with the function |  |  |

manually determined to be the most crash-prone.

GPT-Monkey treats all UI elements on an identi fi ed activity as

| associated with the target function | ’ | s execution path at the inter- | It should be noted that GPT-Monkey mainly uses natural lan- |
| --- | --- | --- | --- |
| face level, rather than quantifying the number of UI elements | guage test requirements, layout of the function entry interface, |  |  |
| related to the target function at the element level. Speci | fi | cally, | screenshots of the function entry interface, and state transition |
| 14 of 29 | IET Software, | 2026 |  |

---

## Page 15

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

graph between global interfaces to drive testing. Among them, TABLE 5 | Segmentation results of functions for Themis benchmark.

only the user ’ s natural language test requirements need to be

App name Number of functions Accurate (Y/N)

manually input, and the others are automatically obtained or

generated by GPT-Monkey. These inputs are encoded as LLM AnkiDroid 5 5Y/0N

prompts to support test parameter generation and function

ActivityDiary 4 4Y/0N

segmentation.

Frost-for-Facebook 3 3Y/0N

GPT-Monkey and other baseline methods are all deployed on a 64-

and-bible 4 4Y/0N

bit Windows 11 machine equipped with an Intel Core i7 CPU, and

evaluated by using a Google Android 12 Pixel 6 emulator. Each Scarlet-Notes 4 4Y/0N

emulator is set up with 2GB RAM, 1GB SD Card, and 1080 × 2400

geohashdroid 2 2Y/0N

screen resolution.

| openlauncher | 3 | 3Y/0N |
| --- | --- | --- |
| APhotoManager | 2 | 2Y/0N |

6.2 | Usefulness

AmazeFileManager 4 4Y/0N

For the Themis benchmark, the evaluation results of function

segmentation are shown in Table 5. The function set for each sun fl ower 2 2Y/0N

app in Table 5 is jointly determined by the functions correspond- FirefoxLite 4 4Y/0N

ing to the known crashes and the functions corresponding to main

event-attendee 5 5Y/0N

navigation tabs or business entry points on the app ’ s main inter-

face. Speci fi cally, fi rst, we segmented the functions corresponding collect 3 3Y/0N

to each known crash in Themis, and found the function paths

WordPress 4 4Y/0N

corresponding to these crashes which start from main navigation

tabs or business entry points. In addition, if there are any main nextcloud 3 3Y/0N

navigation tabs or business entry points on the app ’ s main inter- commons 3 3Y/0N

face that are not covered by the function paths corresponding to

MaterialFBook 4 4Y/0N

crashes, the functions corresponding to those navigation tabs or

business entry points were also segmented. The union of these Omni-Notes 3 3Y/0N

segmented functions forms the set of functions for each app in

Phonograph 2 2Y/0N

Table 5.

osmeditor4android 4 4Y/0N

From Table 5, GPT-Monkey successfully segmented all 68 critical

functions and achieved 100 % accuracy. The testing accuracy Total 68 68Y/0N

observed in the Themis benchmark validates the usefulness of

GPT-Monkey in segmenting functions. The excellent performance

is attributed to the capabilities of the LLM, which excels at under-

| standing the structural and semantic nuances of the app | involve complex nesting or dynamic rendering, so the rectangular |
| --- | --- |
| interfaces. | boundary produced by automatic segmentation may show a slight |

discrepancy from the annotated area. Therefore, the veri fi er com-

| GPT-Monkey proposes a feasible way tailored to speci | fi | c test sce- | bined the layout hierarchy with the screenshot to determine, case |
| --- | --- | --- | --- |
| narios. The correctness of the segmentation is evaluated by com- | by case, whether the result falls within an acceptable tolerance |  |  |
| paring the system results with the manually annotated ground | range. For associated interface consistency veri | fi | cation, a function |
| truth. If both the entry area and the associated interfaces fully | often involves a complex function path, so the interface associa- |  |  |
| match the manual annotation, the function segmentation is con- | tion produced by automatic segmentation may involve multiple |  |  |
| sidered accurate. If there is a partial match and no match, the | interfaces. Based on the manually extracted function paths from |  |  |

function segmentation is considered inaccurate.

the global interface association, the veri fi er veri fi ed item by item

| We further demonstrate the detailed execution process and work- | whether the result strictly matches the interface set in the whole |  |  |
| --- | --- | --- | --- |
| load of the function segmentation in the experiment. First, the | function path. Both veri | fi | cations are necessary to ensure a rigor- |
| extraction of the entry interface and the establishment of the | ous evaluation criterion, which leads to an average time cost of |  |  |
| global interface association were performed through the auto- | 2 | – | 3 min per function. |

mated tools UIAutomator and DroidBot, with each app traversal

While the Themis benchmark is somewhat representative, it only

taking an average of 10 min. Next, manual annotation of function

covers a subset of real-world application interfaces. The unifor-

segmentation was conducted, requiring an average of 3 – 5 min per

mity in design patterns of open-source applications could contrib-

function. Then, GPT-Monkey used LLM to perform automatic

ute to the testing accuracy. The usefulness of GPT-Monkey needs

function segmentation, taking an average of 1 min per function.

to be further evaluated in more diverse and complex application

Finally, manual veri fi cation was conducted on the automated

environments. The real-world application testing benchmark

segmentation results, taking an average of 2 – 3 min per function.

encompasses a wider range of app functions, providing a diverse

| It is worth noting that the time cost of the manual veri | fi | cation | and complex testing environment for GPT-Monkey. The testing |  |  |
| --- | --- | --- | --- | --- | --- |
| mainly came from strict veri | fi | cation on the coordinates of entry | results, as presented in Table 6, reveal a 95 | % | accuracy in function |
| areas and the consistency of associated interfaces. Speci | fi | cally, for | segmentation, with GPT-Monkey correctly segmenting 3168 func- |  |  |
| entry area coordinate veri | fi | cation, real UI components often | tions of all 3337 critical functions. |  |  |
| IET Software, | 2026 | 15 of 29 |  |  |  |

---

## Page 16

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

TABLE 6 | Segmentation results of functions for real-world application benchmark.

Number of functions correctly

| App category | Number of APP | Number of critical functions | segmented by GPT-monkey |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Activity | 12 | 26 | 24 |  |  |  |  |
| Art\design | 27 | 33 | 31 |  |  |  |  |
| Business of | fi | ce | 44 | 117 | 113 |  |  |
| Catering | 77 | 172 | 169 |  |  |  |  |
| Communication | 81 | 218 | 214 |  |  |  |  |
| Company | 56 | 146 | 139 |  |  |  |  |
| Education | 16 | 37 | 36 |  |  |  |  |
| Entertainment | 173 | 599 | 557 |  |  |  |  |
| Finance | 78 | 276 | 259 |  |  |  |  |
| Lifestyle | 39 | 134 | 129 |  |  |  |  |
| Map navigation | 43 | 79 | 68 |  |  |  |  |
| Music/audio | 43 | 97 | 95 |  |  |  |  |
| News/magazines | 29 | 73 | 69 |  |  |  |  |
| Personalization | 42 | 108 | 99 |  |  |  |  |
| Photography | 26 | 46 | 44 |  |  |  |  |
| Shopping | 51 | 347 | 342 |  |  |  |  |
| Social | 29 | 369 | 354 |  |  |  |  |
| Sports | 13 | 48 | 46 |  |  |  |  |
| Tools | 62 | 273 | 254 |  |  |  |  |
| Travel | 21 | 67 | 59 |  |  |  |  |
| Video playback | 17 | 38 | 36 |  |  |  |  |
| Weather | 21 | 34 | 31 |  |  |  |  |
| Total | 1000 | 3337 | 3168 |  |  |  |  |
| While GPT-Monkey achieved 95 | % | segmentation accuracy across | Notably, the dual-feedback mechanism introduced by GPT-Mon- |  |  |  |  |
| 3337 real-world application functions, segmentation still failed in | key can mitigate the segmentation failure that may be caused by |  |  |  |  |  |  |
| 169 of them. We categorize these failures into three typical cases. | LLM and further enhance the robustness of function segmenta- |  |  |  |  |  |  |
| The | fi | rst category involves custom views. To achieve speci | fi | c UI | tion. Before starting the Monkey test kernel, the user interaction |  |  |
| effects, some developers use custom controls that lack standard | feedback allows users to visually check and, if necessary, modify |  |  |  |  |  |  |
| identi | fi | ers. This results in insuf | fi | cient semantic information in the | the function segmentation results generated by the LLM. This |  |  |
| layout | fi | le for LLM to understand, making it dif | fi | cult for LLM to | mechanism ensures that any inaccurate identi | fi | cation of function |
| accurately identify function entry areas. The second category | entry areas or associated interfaces can be corrected, which is |  |  |  |  |  |  |
| involves SurfaceView and TextureView components. These com- | particularly useful in cases where the LLM misunderstands user |  |  |  |  |  |  |

ponents are often used for complex rendering tasks such as video

requirements or app layout. After the Monkey test kernel execu-

playback and map display, but UIAutomator struggles to accu-

tion, the log analysis feedback automatically analyzes the testing

rately obtain their layout information. Furthermore, they often

results, including crash logs, coverage information, and runtime

lack necessary text labels, making it dif fi cult for LLM to identify

behavior. If the analysis reveals that the target function has not

their structure and function. The third category involves dynami-

been suf fi ciently tested or the expected test goals are not achieved,

cally generated components. These components are typically

GPT-Monkey can reinitiate the parameter revision and generation

loaded dynamically from background data at runtime and lack

processes to iteratively optimize the test results.

fi xed resource IDs or explicit text content, making it dif fi cult for

| LLM to effectively capture their context and semantic informa- | The testing results on both standard and real-world application |  |  |
| --- | --- | --- | --- |
| tion. GPT-Monkey | ’ | s performance is indeed affected by these fail- | testing benchmarks demonstrate the usefulness of GPT-Monkey. |
| ure cases. However, these failure cases involve less critical | GPT-Monkey can realize highly accurate interface understanding |  |  |
| functions or less frequently used modules, so their impact on | and function segmentation with the mobile application, which is |  |  |
| the overall detection performance is relatively limited. | able to signi | fi | cantly enhance GUI testing. |
| 16 of 29 | IET Software, | 2026 |  |

---

## Page 17

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

6.3 | Effectiveness To further evaluate the automation capability and manual inter-

vention costs of GPT-Monkey, we recorded the number of itera-

For the Themis benchmark, the evaluation results are shown in

tions of the dual-feedback mechanism required for function

Table 7, which lists the crashes detected by GPT-Monkey and

segmentation and test parameter generation in the Themis bench-

baseline methods and the elapsed time required to trigger the

mark, which contains 68 known functions. The experimental

crash for the fi rst time.

results are shown in Table 10.

To ensure the effectiveness of crash detection in the Themis

The experimental results show that the average iterative number

benchmark, we referred to the of fi cial dataset, which records 52

of the user interaction feedback is 1.2, and of the log analysis

known bugs and their corresponding crash logs. During testing, if

feedback is 1.3. This demonstrates that the dual-feedback mech-

the stack trace of the crash matched the of fi cial crash trace in the

anism ef fi ciently assists the LLM to optimize the output, and in

benchmark, then the crash was considered to be caused by a

most tasks, multiple iterations of corrections are not required. In

speci fi c bug in Themis. Additionally, we cross-validated the crash

addition, we observed most functions in the user interaction

log to further ensure that the reported crash was caused by the

feedback can be con fi rmed by users in the fi rst interaction,

speci fi c bug in Themis. This validation ensures that our evaluation

some are con fi rmed within two interactions, and only few of

results are regardless of crashes outside the of fi cial dataset.

the functions require more than two interactions. We also

| In the standard benchmark with 52 known crashes, GPT-Monkey | observed that log analysis feedback can assist LLM to complete |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| detected 28 crashes, the detection rate of which is 27.3 | % | higher | corrections within one or two iterations in most cases. This result |  |  |
| than Monkey (28 vs. 22), 16.7 | % | higher than APE (28 vs. 24), 33.3 | % | shows that the dual-feedback mechanism greatly reduces the |  |
| higher than ComboDroid (28 vs. 21), 86.7 | % | higher than Time- | burden of manual intervention and improves the test process. |  |  |
| Machine (28 vs. 15), 47.4 | % | higher than Stoat (28 vs. 19), and | The user interaction feedback provides precise guidance, while |  |  |
| 180 | % | higher than Q-testing (28 vs. 10). To evaluate the statistical | the log analysis feedback uses historical behavior information for |  |  |
| signi | fi | cance of these differences, we performed McNemar | ’ | s exact | self-optimization. |

test [34] for each pairwise comparison between GPT-Monkey and

| each baseline, where each of the 52 known crashes constitutes a | Guided by this dual-feedback mechanism, GPT-Monkey only |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| paired binary observation (detected or not). The results are shown | needs to execute the entire testing process once for each function |  |  |  |  |  |  |  |  |  |  |  |  |
| in Table 8. GPT-Monkey achieves statistically signi | fi | cant improve- | in each app. This process begins when the user inputs a test |  |  |  |  |  |  |  |  |  |  |
| ments over Q-testing ( | p | < | 0 | : | 0001), TimeMachine ( | p | ¼ | 0 | : | 0023), and | requirement and ends when the system generates test results |  |  |
| Stoat ( | p | ¼ | 0 | : | 0117). The differences between GPT-Monkey and | that meet the user | ’ | s expectations. It should be noted that, driven |  |  |  |  |  |
| Monkey ( | p | ¼ | 0 | : | 0703), ComboDroid ( | p | ¼ | 0 | : | 0654), and APE ( | p | ¼ | by the log analysis feedback loop, GPT-Monkey drives the Monkey |
| 0 | : | 2891) do not reach statistical signi | fi | cance at the 0.05 level. Nev- | kernel multiple times to initiate speci | fi | c test runs, thereby achiev- |  |  |  |  |  |  |
| ertheless, GPT-Monkey exclusively detects 7, 9, and 6 crashes | ing optimization based on historical test information. The last |  |  |  |  |  |  |  |  |  |  |  |  |
| missed by Monkey, ComboDroid, and APE, respectively, whereas | column of Table 10 shows the number of Monkey kernel execu- |  |  |  |  |  |  |  |  |  |  |  |  |
| these baselines only detect 1, 2, and 2 crashes that GPT-Monkey | tions for each test task, quantitatively demonstrating the effective- |  |  |  |  |  |  |  |  |  |  |  |  |
| misses, indicating a degree of practical advantage of GPT-Monkey. | ness of this feedback mechanism in addressing the randomness |  |  |  |  |  |  |  |  |  |  |  |  |

of LLM.

Additionally, Figure 8 displays the time taken by GPT-Monkey

| and baseline methods to trigger each crash in the testing. In gen- | To further analyze GPT-Monkey | ’ | s behavior patterns, we counted |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| eral, the shorter the time taken to trigger a crash, the more ef | fi | - | the types of event parameters generated by GPT-Monkey when |  |  |  |  |
| ciently the method detects the crash. The average detection time | testing the benchmark application to reveal its event generation |  |  |  |  |  |  |
| of GPT-Monkey is reduced by 47.61 min (62.5 | % | ) compared to | preferences, which are shown in Table 11. Among the events |  |  |  |  |
| Monkey, 18.68 min (39.5 | % | ) compared to APE, 15.05 min (34.5 | % | ) | generated by GPT-Monkey, click events account for ~69.3 | % | , |
| compared to ComboDroid, and 60.1 min (67.8 | % | ) compared to | re | fl | ecting that clicks are the primary interaction logic in most |  |  |
| TimeMachine. | apps. Swipe events account for 24.7 | % | , demonstrating that GPT- |  |  |  |  |

Monkey also effectively utilizes swipes when navigating interface

To quantitatively compare the crash detection ef fi ciency of each

content. Other events (such as long press, text input, and screen

method in the Themis benchmark, we conducted a one-way

rotation) account for a combined 6.0 % . These results further dem-

ANOVA to statistically analyze the time required for each method

onstrate that GPT-Monkey possesses contextual awareness in

to trigger a crash. The results are shown in Table 9, where GPT-

automatic event parameter generation and selects the most appro-

Monkey signi fi cantly outperforms other baseline methods in

priate test method based on the app ’ s state.

terms of the time until the crash is triggered ( F = 6.70,

| p | < | 0 | : | 00001), demonstrating higher testing ef | fi | ciency. To identify | The experiment results show that GPT-Monkey not only has a |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| speci | fi | c pairwise differences, we further conducted Dunnett | ’ | s | higher detection rate but also has a higher detection ef | fi | ciency |  |  |  |  |  |  |  |  |  |  |  |
| post-hoc test [35] with GPT-Monkey as the control group, the | compared to traditional Monkey-based testing and other baseline |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| results of which are also shown in Table 9. GPT-Monkey triggers | methods. Several factors and advantages contributing to these |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| crashes | signi | fi | cantly | faster | than | Monkey | ( | p | ¼ | 0 | : | 0023), | Stoat | results are given as follows. First, by intelligently segmenting func- |  |  |  |  |
| ( | p | < | 0 | : | 0001), | TimeMachine | ( | p | ¼ | 0 | : | 0004), | and | Q-testing | ( | p | ¼ | tions, GPT-Monkey can send testing events for crash-prone func- |
| 0 | : | 0036). The differences compared to APE ( | p | ¼ | 0 | : | 5377) and Com- | tions. This targeted approach signi | fi | cantly improves the ef | fi | ciency |  |  |  |  |  |  |
| boDroid ( | p | ¼ | 0 | : | 7717) do not reach statistical signi | fi | cance at the | of detecting crashes. Second, utilizing the understanding ability of |  |  |  |  |  |  |  |  |  |  |
| 0.05 level. Nevertheless, GPT-Monkey achieves a shorter average | LLM, GPT-Monkey tailors testing parameters according to the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| detection time than both APE and ComboDroid, indicating a | unique characteristics of each function. Thanks to the tailored |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| degree of practical advantage in crash detection ef | fi | ciency. | parameters, GPT-Monkey can send more accurate and effective |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| IET Software, | 2026 | 17 of 29 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 18

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

— — (131) — — (195) (47) — — — — — — — — — (71) — (57) — — — — — — — — — — — —

★ ★ ★ ★ ★

Q-testing

(Continues)

(99) — — — — (210) (62) (92) — — — — — — — — (63) — (79) — (112) — — — — (102) (99) (89) (98) — —

Stoat ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★

(59) — — — — — (33) — — — — — — — — — — (35) (36) — (203) — — (46) (165) (53) (64) — (172) — —

★ ★ ★ ★ ★ ★ ★ ★ ★ ★

Time machine

(25) — — — — (203) (11) (59) — — — — (77) — — (69) (9) (12) (10) — (60) — — — (49) — (32) (49) — — —

Combo Droid ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★

(29) —

APE (209) — — (176) (13) — — — — — (74) — — — (12) (10) (8) (26) (52) — — — (44) — (29) (45) (50) — —

★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★

(50) — (173) — — (135) (3) — — (50) (248) (149) — — (108) — (5) (23) (32) (44) — — — (47) (67) — — — (88) — —

★

Monkey ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★

(18) — (56) — — (57) (2) (43) — — (74) (72) — — (42) (53) (3) (5) (5) (8) (44) — — (12) (29) — (23) (31) (41) — —

★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★

GPT-monkey

2.9 2.9.1 2.7 2.6 2.10 2.9.4 2.9 1.4.0 1.1.8 2.2.1 0.9.4 0.3.1 0.6.4 3.4.2 3.3.2 3.3.2 3.2.1 0.1.6 0.5 9.2

2.1.12 2.1.16 2.1.20 1.23.0 11.3

3.1.309 3.2.369 3.2.327 3.0.286 3.3.377 6.9.5

Version

#4707 #5638 #4451 #4200 #6145 #5756 #4977 #285 #118 #1323 #375 #697 #480 #261 #703 #114 #73 #67 #116 #1837 #1796 #1558 #1232 #239 #4881 #4942 #5085 #2198 #3222 #8659 #7182

Crash ID

Detection results and time until the crash is triggered for Themis benchmark.

|

ower

fl

TABLE 7 App name AnkiDroid AnkiDroid AnkiDroid AnkiDroid AnkiDroid AnkiDroid AnkiDroid ActivityDiary ActivityDiary Frost-for-Facebook and-bible and-bible and-bible and-bible and-bible Scarlet-Notes geohashdroid openlauncher APhotoManager AmazeFileManager AmazeFileManager AmazeFileManager AmazeFileManager sun FirefoxLite FirefoxLite FirefoxLite event-attendee collect WordPress WordPress

18 of 29 IET Software, 2026

---

## Page 19

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

— — — — — (63) (68) (82) (73) — — — (92) — — — — — — — — 10

★ ★ ★ ★ ★

Q-testing

— — (96) — — (75) (77) (98) (64) — (97) — (105) — — — — (133) — — — 19

Stoat ★ ★ ★ ★ ★ ★ ★ ★

— — — — (227) — (43) (68) (43) — — — (83) — — — — — — — — 15

★ ★ ★ ★ ★

Time machine

— (46) (69) — — — (20) (38) (19) — (15) — (38) — — — (6) — — — — 21

| ★ | ★ | ★ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo | Droid | ★ | ★ | ★ | ★ | ★ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | — | (53) | — | — | (27) | (21) | (35) | (21) | — | (18) | — | (41) | — | — | — | (4) | (66) | — | (71) | rst time, in minutes. |

— 24 fi

APE ★ ★ ★ ★ ★ ★ ★ ★ ★ ★

— — (93) — — — (36) (52) (47) — (47) — (52) — — — — (127) — — — 22

★ ★ ★ ★ ★ ★

Monkey ★

— — (44) — — (7) (4) (25) (19) — (13) — (26) — — — (2) (42) — — — 28

★ ★ ★ ★ ★ ★ ★ ★ ★

GPT-monkey

8.1 14.9 13.6 13.7 13.3 13.1 12.9 — ) denotes the elapsed time required to trigger this crash for the

3.10.0 3.6.1 3.9.2 2.0.0 2.11.0 2.9.0 2.7.1 2.6.7 2.6.7 4.0.2 6.1.0 0.15.0 0.9.10 ∗

Version 11.0.0.8

52

#6530 #11992 #11135 #10876 #10547 #10363 #10302 #5173 #4026 #4792 #1918 #3244 #2123 #1581 #1391 #1385 #224 #745 #112 #729 #637

Crash ID

(Continued)

|

∗ ) indicates that the crash is triggered, and (

(

★

:

TABLE 7 App name WordPress WordPress WordPress WordPress WordPress WordPress WordPress nextcloud nextcloud nextcloud nextcloud commons commons commons commons commons MaterialFBook Omni-Notes Phonograph osmeditor4android osmeditor4android Total Note

IET Software, 2026 19 of 29

---

## Page 20

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

TABLE 8 | McNemar ’ s exact test results on Themis benchmark.

| Comparison | vs. Monkey | vs. APE | vs. ComboDroid | vs. Time Machine | vs. Stoat | vs. Q-testing |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| b (only GPT-Monkey) | 7 | 6 | 9 | 15 | 10 | 8 |  |  |
| c (only Baseline) | 1 | 2 | 2 | 2 | 1 | 0 |  |  |
| p | -value | 0.0703 | 0.2891 | 0.0654 | 0.0023 | 0.0117 | < | 0.0001 |

300

250

200

150

Detection time (min)

97.37

100 88.67

87.90

76.18

47.25

50

43.62

28.57

0

| AD-285 | FF-1323 | Ab-375 | Ab-697 | Ab-480 | Ab-703 | SN-114 | OL-67 | SF-239 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GHD-73 | FL-4881 | FL-4942 | FL-5085 | NC-5173 | NC-4026 | ON-745 |  |  |  |
| Anki-4707 | Anki-4451 | Anki-5756 | Anki-4977 | APM-116 | NC-1918 |  |  |  |  |
| AFM-1837 | AFM-1796 | ΟΕΑ-2198 | WP-11992 | WP-11135 | WP-10547 | WP-10363 | WP-10302 | MFB-224 | OE4A-729 |
| Collect-3222 | Comm-2123 |  |  |  |  |  |  |  |  |

Crash IDs

| GPT-monkey | Time machine |
| --- | --- |
| Monkey | Stoat |
| APE | Q-testing |

ComboDroid

FIGURE 8 | Time taken to trigger each crash by GPT-Monkey and baseline methods.

testing events to the functions, enhancing the detection rate of immediately upon app launch is often highly correlated with con-

crashes. fi guration bugs including component registration, resource load-

ing, or permission con fi guration, whereas a crash that occurs only

In addition to the standard benchmark, the effectiveness of GPT-

after users complete multiple steps of operations is more likely to

Monkey was further validated through testing in a real-world

stem from business logic bugs. For the exception call stack loca-

application benchmark. The category and number of crashes

tion of a crash, if the call involves only layout in fl ation, resource

obtained from testing are shown in Table 12.

parsing, or component registration, the crash is more likely corre-

| For the 1000 Google Play apps, to reduce the risk of false positives | lated with con | fi | guration bugs. In contrast, if the call is concen- |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| and interpret crash results more accurately, we adopted a post-hoc | trated in the app | ’ | s own business modules, the crash is more likely |  |  |  |  |  |  |  |  |  |  |
| analysis strategy to analyze crashes that stem from con | fi | guration | to be caused by logic bugs. For the crash | ’ | s semantic signals from |  |  |  |  |  |  |  |  |
| bugs or logic bugs. Speci | fi | cally, the post-hoc crash analysis strat- | logs and exception messages, if the semantic signals of a crash |  |  |  |  |  |  |  |  |  |  |
| egy jointly considers the crash timing, the exception call stack | include | “ | permission denied | ” | , | “ | class not found | ” | , | “ | activity not |  |  |
| location of a crash, and the crash | ’ | s semantic signals from logs | found | ” | , | “ | view not attached to window | ” | , and | “ | resource not found | ” | , |
| and exception messages. For the crash timing, a crash occurring | the crash is more likely correlated with con | fi | guration bugs. |  |  |  |  |  |  |  |  |  |  |
| 20 of 29 | IET Software, | 2026 |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 21

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

TABLE 9 | Statistical test of time until the crash is triggered on Themis benchmark.

| Tools | GPT-Monkey | Monkey | APE | ComboDroid | TimeMachine | Stoat | Q-testing |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Average time | 28.57 | 76.18 | 47.25 | 43.62 | 88.67 | 97.37 | 87.9 |  |  |  |
| Standard deviation | 21.73 | 59.64 | 49.17 | 42.84 | 67.05 | 32.62 | 44.13 |  |  |  |
| F-statistic | F | (6, 132) | = | 6.70 |  |  |  |  |  |  |
| p | -Value | p | ≈ | 0.000004 | < | 0.00001 |  |  |  |  |
| Dunnett | ’ | s post-hoc | — | 0.0023 | 0.5377 | 0.7717 | 0.0004 | < | 0.0001 | 0.0036 |

TABLE 10 | Iteration number in dual feedback for functions on Themis benchmark.

Iteration numbers in

| Number of | user interaction | Average per | Iteration numbers in | Average per | Number of |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| App | functions | feedback | function | log analysis feedback | function | test runs |  |  |
| AnkiDroid | 5 | 8 | 1.6 | 11 | 2.2 | 16 |  |  |
| ActivityDiary | 4 | 4 | 1.0 | 4 | 1.0 | 8 |  |  |
| Frost-for-Facebook | 3 | 5 | 1.7 | 3 | 1.0 | 6 |  |  |
| and-bible | 4 | 4 | 1.0 | 6 | 1.5 | 10 |  |  |
| Scarlet-Notes | 4 | 7 | 1.8 | 6 | 1.5 | 10 |  |  |
| geohashdroid | 2 | 2 | 1.0 | 2 | 1.0 | 4 |  |  |
| openlauncher | 3 | 4 | 1.3 | 3 | 1.0 | 6 |  |  |
| APhotoManager | 2 | 3 | 1.5 | 4 | 2.0 | 6 |  |  |
| AmazeFileManager | 4 | 4 | 1.0 | 4 | 1.0 | 8 |  |  |
| sun | fl | ower | 2 | 2 | 1.0 | 3 | 1.5 | 5 |
| FirefoxLite | 4 | 4 | 1.0 | 6 | 1.5 | 10 |  |  |
| event-attendee | 5 | 5 | 1.0 | 5 | 1.0 | 10 |  |  |
| collect | 3 | 4 | 1.3 | 4 | 1.3 | 7 |  |  |
| WordPress | 4 | 5 | 1.3 | 5 | 1.3 | 9 |  |  |
| nextcloud | 3 | 3 | 1.0 | 3 | 1.0 | 6 |  |  |
| commons | 3 | 3 | 1.0 | 5 | 1.7 | 8 |  |  |
| MaterialFBook | 4 | 4 | 1.0 | 5 | 1.3 | 9 |  |  |
| Omni-Notes | 3 | 4 | 1.3 | 3 | 1.0 | 6 |  |  |
| Phonograph | 2 | 3 | 1.5 | 2 | 1.0 | 4 |  |  |
| osmeditor4android | 4 | 5 | 1.3 | 6 | 1.5 | 10 |  |  |
| Total/average | 68 | 83 | 1.2 | 90 | 1.3 | 158 |  |  |

TABLE 11 | Event types generated by GPT-Monkey on Themis benchmark.

| Event type | Total events | Average per app | Percentage ( | % | ) |
| --- | --- | --- | --- | --- | --- |
| Click | 2546 | 127.3 | 69.3 |  |  |
| Swipe | 906 | 45.3 | 24.7 |  |  |
| Back | 136 | 6.8 | 3.7 |  |  |
| Long press | 50 | 2.5 | 1.4 |  |  |
| Rotate | 18 | 0.9 | 0.5 |  |  |
| Others | 14 | 0.7 | 0.4 |  |  |
| Total | 3670 | — | 0 |  |  |
| IET Software, | 2026 | 21 of 29 |  |  |  |

---

## Page 22

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

TABLE 12 | Detection results of crashes for real-world application benchmark.

| Crash category | Crash typical causes | Crash number |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| NullPointerException | Dereferencing a null object due to logic | fl | aw or missing null checks | 174 |  |  |
| IllegalStateException | Invalid lifecycle transition, e.g., using views after activity is destroyed | 117 |  |  |  |  |
| IllegalArgumentException | Passing invalid parameters to methods or constructors | 66 |  |  |  |  |
| IndexOutOfBoundsException | Invalid access to arrays or collections due to logic errors | 23 |  |  |  |  |
| UnsupportedOperationException | Calling unsupported methods (e.g., on unmodi | fi | able collections) | 13 |  |  |
| In | fl | ateException | Invalid or missing layout resources; often caused by test con | fi | g issues | 4 |
| Total | — | 397 |  |  |  |  |
| Through the proposed post-hoc crash analysis strategy, we ana- | RequestOptions | during image loading, but the bundled version of |  |  |  |  |
| lyzed that 397 crashes GPT-Monkey found in the top 1000 popular | Glide in the APK did not support this method. The | fi | tCenter | () API |  |  |
| apps of Google Play stem from app logic bugs rather than con | fi | g- | was introduced in a newer version of Glide than the one packaged |  |  |  |
| uration bugs. | in Omni-Notes 6.1.0, causing an | UnsupportedOperationException |  |  |  |  |

when the user attempts to view an attached image in the gallery

Furthermore, we performed an in-depth attribution analysis of

viewer.

the crashes caused by application logic bugs discovered by GPT-

| Monkey. Due to the behaviors of apps under stress, the types of | The testing results on both standard and real-world application |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| interactions simulated by GPT-Monkey, and the programing pit- | testing benchmarks indicate the effectiveness of GPT-Monkey. |  |  |  |  |
| falls in app development, certain categories of crashes are fre- | GPT-Monkey can achieve a high detection rate and detection |  |  |  |  |
| quently triggered. For example, the | NullPointerException | may | ef | fi | ciency, which is capable of enhancing the application stability |
| occur when GPT-Monkey causes the dereferencing of a null object | by detecting critical crashes. |  |  |  |  |

reference. In addition, the IllegalStateException may be triggered

when GPT-Monkey causes the application to execute operations

at inappropriate times. Moreover, the IllegalArgumentException 6.4 | Ablation Experiment

may happen if GPT-Monkey sends unexpected values as parame-

6.4.1 | Impact of Event Parameter Con fi guration on

ters to method calls within the app. Furthermore, other categories

Detection Performance

of crashes, such as IndexOutOfBoundsException , UnsupportedO-

| perationException | , and | In | fl | ateException | , can also be triggered, | To further analyze the impact of interaction event types on crash |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| although they are less common. The | IndexOutOfBoundsExceptions | detection capabilities, we designed a set of ablation experiments. |  |  |  |  |  |
| may occur when GPT-Monkey leads to erratic accesses of lists or | By restricting the types of events used during testing, we evaluate |  |  |  |  |  |  |
| arrays. The | UnsupportedOperationExceptions | may be triggered | the performance between different single-event parameter con | fi | g- |  |  |
| particularly in the components that do not support modi | fi | cation | urations and multi-event parameter con | fi | gurations. Speci | fi | cally, |
| operations. The | In | fl | ateExceptions | may present when GPT-Monkey | on the Themis benchmark containing 52 known crashes, we con- |  |  |
| loads different parts of the GUI in unconventional ways or | structed four event con | fi | guration strategies: Click-Only, Swipe- |  |  |  |  |
| sequences. | Only, Long Press-Only, and All Events (baseline). Across all |  |  |  |  |  |  |

experiments, we kept the same number of events to ensure fair

To illustrate how GPT-Monkey works in practice, we present a

comparison. Statistical metrics include the number of successfully

detailed case study of crash detection in Omni-Notes (version

detected crashes and the average execution time. The experimen-

6.1.0), a note-taking application. GPT-Monkey segmented the entry

tal results are shown in Figure 9.

area of the “ Text note ” function at coordinates [562,1506][810,1626]

| corresponding to the | fl | oating action button on the main interface, | In terms of crash detection capabilities, as shown in Figure 9a, the |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| and identi | fi | ed 4 associated interfaces, including | it.feio.android. | baseline strategy performs best, detecting a total of 28 crashes. The |  |  |  |  |  |  |
| omninotes.MainActivity | , | it.feio.android.omninotes. GalleryActivity | , | Click-Only strategy, despite using only click actions, still detects |  |  |  |  |  |  |
| it.feio.android.omninotes.CategoryActivity | , and | it.feio. android.omni- | 23 crashes, demonstrating the core role of click events in GUI |  |  |  |  |  |  |  |
| notes.Snooze Activity | . Guided by Parameter-RAG, GPT-Monkey | automated testing. In contrast, the Swipe-Only and Long Press- |  |  |  |  |  |  |  |  |
| generated tailored parameters with a touch event proportion of | Only strategies show signi | fi | cantly lower detection capabilities, |  |  |  |  |  |  |  |
| 70 | % | and a motion event proportion of 15 | % | , re | fl | ecting the interac- | detecting only four crashes and three crashes, respectively. These |  |  |  |
| tion pattern of the note-editing function, which primarily involves | results suggest that a single interaction event limits the testing |  |  |  |  |  |  |  |  |  |
| tapping and typing. The generated testing instruction was | “ | adb shell | tool | ’ | s ability to explore complex application states. In terms of |  |  |  |  |  |
| monkey -p it.feio.android.omninotes | — | pct-touch 70 | — | pct-motion 15 | performance overhead, as shown in Figure 9b, the average event |  |  |  |  |  |
| — | pct-syskeys 5 | — | pct-nav 5 | — | pct-anyevent 5 | — | throttle 300 | — | ignore- | execution time for each strategy is roughly similar, ranging from |
| crashes -v -v 500 | ” | . After 42 min of targeted testing, GPT-Monkey | 227 to 296 milliseconds. Speci | fi | cally, click events and slide events |  |  |  |  |  |
| triggered an | UnsupportedOperationException | crash. The root cause | have a relatively short response time and fast response speed. |  |  |  |  |  |  |  |
| of this crash was identi | fi | ed as a Glide library version incompatibil- | Therefore, the single-event strategy does not signi | fi | cantly reduce |  |  |  |  |  |
| ity, where | GalleryPagerFragment | invoked the | fi | tCenter | () method on | execution ef | fi | ciency. |  |  |
| 22 of 29 | IET Software, | 2026 |  |  |  |  |  |  |  |  |

---

## Page 23

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| (a) | 30 | (b) |  |
| --- | --- | --- | --- |
| 28 | 350 |  |  |
| 25 | 300 | 287 | 296 |

23

254

250

20 227

200

15

150

10

100

Number of detected crashes 5 4

3 50

Average event execution time (ms)

0 0

All events Click only Swipe only Long press only All events Click only Swipe only Long press only

FIGURE 9 | (a) Crashes detected by event strategy. (b) Average execution time.

| This shows that while speci | fi | c single-event strategies (such as | interface screenshots and does not include layout structure and |  |  |
| --- | --- | --- | --- | --- | --- |
| Click-Only) still have some detection capabilities in some scenar- | interface associations; the Association-Only con | fi | guration only |  |  |
| ios, the lack of event type diversity signi | fi | cantly limits the effec- | contains the function transition path and does not include speci | fi | c |
| tiveness of testing tools. While keeping performance overhead | layout or visual input. Under the | fi | ve con | fi | gurations, GPT-Mon- |
| manageable, introducing diverse interactive event con | fi | gurations | key performed the same number of function segmentation and |  |  |
| is a key factor in improving the comprehensive capabilities of | test instruction generation tasks, and the Monkey test kernel then |  |  |  |  |
| automated crash detection tools. | automatically tested the target functions. The number of correct |  |  |  |  |

function segmentations and crash detections are shown in

Table 13.

6.4.2 | Impact of Contextual Input on Function

Results show that when provided only with activity names as input,

Understanding

GPT-Monkey ’ s accuracy in the function segmentation task drops to

| To evaluate the impact of contextual information (such as inter- | 42.6 | % | , and its crash detection rate drops to 36.5 | % | . This is mainly |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| face layout and visual screenshots) on LLM-driven analysis capa- | because LLM struggles to understand the precise semantics of the |  |  |  |  |  |  |
| bilities, we designed a set of ablation experiments to compare the | current activity without layout and visual information. Under the |  |  |  |  |  |  |
| performance of GPT-Monkey in function segmentation and crash | Layout-Only and Screenshot-Only con | fi | gurations, GPT-Monkey |  |  |  |  |
| detection under different input information conditions. In the | retains over 80 | % | function segmentation accuracy and over 42 | % | crash |  |  |
| benchmark dataset, we constructed | fi | ve types of input con | fi | gura- | detection capability, demonstrating the signi | fi | cant support provided |
| tions for each target function. The Full Input con | fi | guration con- | by structured controls and visual information for LLM reasoning. |  |  |  |  |
| tains complete contextual information such as the target function | The Association-Only con | fi | guration, which relies on modeling inter- |  |  |  |  |
| name, interface layout, interface screenshots, and interface asso- | face transition links and similarly lacks entry context, achieves only |  |  |  |  |  |  |
| ciations; the Activity-Only con | fi | guration only provides the activity | 48.5 | % | segmentation accuracy and 38.5 | % | detection capability. This |
| name of the target function and does not contain any structural or | indicates that while it has some auxiliary value in identifying func- |  |  |  |  |  |  |
| visual information; the Layout-Only con | fi | guration provides the | tion boundaries, its effectiveness is limited. In summary, complete |  |  |  |  |
| XML control tree and control attribute information of the target | contextual information is crucial for LLM-driven analysis strategies, |  |  |  |  |  |  |
| interface and does not include screenshots or interface association | especially in function semantic understanding and complex interac- |  |  |  |  |  |  |
| information; the Screenshot-Only con | fi | guration only provides | tion path judgment. |  |  |  |  |

TABLE 13 | Impact of different input information on GPT-Monkey performance.

| Number of functions | Segmentation | Number of | Detection |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input type | correctly segmented | accuracy ( | % | ) | crash detected | accuracy ( | % | ) |
| Full input | 68 | 100.0 | 28 | 53.8 |  |  |  |  |
| Activity-only | 29 | 42.6 | 19 | 36.5 |  |  |  |  |
| Layout-only | 58 | 85.3 | 24 | 46.2 |  |  |  |  |
| Screenshot-only | 55 | 80.9 | 22 | 42.3 |  |  |  |  |
| Association-only | 33 | 48.5 | 20 | 38.5 |  |  |  |  |
| IET Software, | 2026 | 23 of 29 |  |  |  |  |  |  |

---

## Page 24

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

6.4.3 | Effectiveness of Each Module on Overall Testing adjusting parameters based on the results of the previous test,

Performance thereby reducing the crash detection rate from 53.8 % to 44.2 % .

Removing the cross-modal alignment module signi fi cantly

To further validate the necessity and effectiveness of each key

reduces the accuracy of entry area segmentation, indicating that

module in the overall architecture of GPT-Monkey, we designed

screenshots cannot support LLM ’ s accurate reasoning and layout

and conducted an ablation experiment to compare GPT-Monkey ’ s

information is crucial for understanding the interface. Removing

performance when different modules are removed. The modules

the interface association graph signi fi cantly reduces the accuracy

examined in the ablation experiment included the user interaction

of function segmentation, which causes GPT-Monkey to fail to

feedback mechanism, the log analysis feedback mechanism, the

identify the relevant interfaces of the target function, thus affect-

cross-modal alignment module, the interface association estab-

ing subsequent crash detection. Removing parameter-RAG

lishment module, and the parameter-RAG parameter generation

increases the reliance of parameter generation on LLM reasoning,

mechanism. The ablation objectives, ablation methods, and eval-

reducing the crash detection rate from 53.8 % to 40.4 % due to

uation metrics are shown in Table 14.

invalid or unreasonable parameter generation.

The evaluation benchmark still adopted the Themis benchmark,

Overall, the effectiveness of GPT-Monkey relies on the synergy

containing 68 functions and 52 known crashes. Each ablation

among modules, with each module being indispensable. Cross-

con fi guration was run for 60 min in the same environment, with

modal alignment and interface association are fundamental to

each test repeated three times to ensure fairness. The experimen-

supporting function understanding and segmentation, while

tal results are shown in Table 15.

parameter-RAG and the dual-feedback mechanism enhance the

The results show that each module plays a crucial role in improv- system ’ s test parameter generation capabilities.

ing the system ’ s entry area identi fi cation accuracy, function seg-

mentation accuracy, crash detection rate, and testing ef fi ciency.

6.4.4 | Effectiveness of User Interaction Feedback Under

Removing the user interaction feedback mechanism reduces

Ambiguous Testing Requirements

users ’ ability to adjust testing parameters, decreasing the crash

| detection rate from 53.8 | % | to 44.2 | % | and increasing the average | To further validate GPT-Monkey | ’ | s ability to handle ambiguous |
| --- | --- | --- | --- | --- | --- | --- | --- |
| time-to-crash from 28.6 to 35.8 min. Removing the log analysis | natural language input, we conducted an ablation experiment |  |  |  |  |  |  |
| feedback mechanism prevents the system from automatically | on the user interaction feedback module. For each function in |  |  |  |  |  |  |

TABLE 14 | Ablation settings for each module and corresponding evaluation metrics.

| Module | Ablation method | Primary evaluation metrics |  |  |
| --- | --- | --- | --- | --- |
| User interaction feedback | Remove the modi | fi | cation module and directly use the | Time until the crash is triggered, |
| parameters returned by LLM in the | fi | rst generation. The control | parameter validity rate |  |

group allows user modi fi cation.

| Log analysis feedback | Skip log analysis and run the test only once. The control group | Crash detection rate, function |
| --- | --- | --- |
| supports log-driven optimization. | segmentation accuracy |  |
| Cross-modal alignment | Do not provide the layout and retain only the screenshot. The | Entry area segmentation accuracy |

Control group retains the layout and screenshot.

Interface association Remove the global interface graph and retain the current Function segmentation accuracy

interface. The control group obtains the global interface

association graph.

Parameter-RAG Do not call the parameter knowledge base, and LLM generates Parameter validity rate

parameters solely from the prompt. The control group uses

Parameter-RAG.

TABLE 15 | Impact of module ablation on GPT-Monkey performance.

| Entry area | Function | Crash detection | Average time | Parameter |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Module | accuracy ( | % | ) | segmentation rate ( | % | ) | rate ( | % | ) | (min) | validity rate ( | % | ) |
| Full system (all modules) | 100.0 | 100.0 | 53.8 | 28.6 | 100.0 |  |  |  |  |  |  |  |  |
| No cross-modal alignment | 68.2 | 81.3 | 36.5 | 41.3 | 98.1 |  |  |  |  |  |  |  |  |
| No interface association | 82.3 | 79.4 | 38.5 | 39.6 | 99.2 |  |  |  |  |  |  |  |  |
| No parameter-RAG | 93.1 | 88.2 | 40.4 | 37.7 | 85.3 |  |  |  |  |  |  |  |  |
| No user interaction feedback | 90.5 | 90.1 | 44.2 | 35.8 | 89.6 |  |  |  |  |  |  |  |  |
| No log analysis feedback | 100.0 | 100.0 | 44.2 | 33.9 | 100.0 |  |  |  |  |  |  |  |  |
| 24 of 29 | IET Software, | 2026 |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 25

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

TABLE 16 | Ablation experiment on the effectiveness under explicit or ambiguous requirements.

| Input Type | Group | FS-Acc | C-Det | T-DC | I-Count |  |
| --- | --- | --- | --- | --- | --- | --- |
| Explicit | G1 | 100 | % | 28 | 28.6 min | 1.0 |
| Explicit | G2 | 100 | % | 28 | 29.1 min | 0 |
| Ambiguous | G1 | 93 | % | 25 | 32.4 min | 1.6 |
| Ambiguous | G2 | 62 | % | 17 | 49.8 min | 0 |
| the Themis benchmark, we constructed two types of user require- | layout information to roughly identify associated interfaces and |  |  |  |  |  |
| ments. One is a complete and explicit requirement, and the other | entry areas relevant to the target function. It restricts Monkey | ’ | s |  |  |  |
| is an ambiguous requirement generated by randomly removing | random events to the entry area and associated interfaces with |  |  |  |  |  |
| two or three semantic words. The ablation experiment compared | higher textual relevance, thereby constraining the scope of ran- |  |  |  |  |  |
| two con | fi | gurations: (1) G1, representing the entire process that | dom testing. |  |  |  |

allows users to modify test parameters through user interaction

During implementation, Monkey-TextFocus still uses UIAutoma-

feedback; and (2) G2, which follows the same process as G1 but

tor to extract layout XML fi les and uses DroidBot to construct the

excludes the user interaction feedback step. Evaluation metrics

global interface state transition graph. On this basis, Monkey-

included function segmentation accuracy (FS-Acc), the number

TextFocus constructs TF-IDF bag-of-words vectors from the test-

of known crashes detected (C-Det), the average time until the

ing requirements description and the interface text fi elds, com-

crash is triggered (T-DC, in minutes), and the number of user

putes cosine similarity to obtain component-level similarity

interaction iterations (I-Count). For each user requirement, the

scores, uses the highest scoring component in each interface to

test time was fi xed at 60 min. For each con fi guration, the test was

locate the entry area, and then computes interface-level similarity

run three times and the test metrics were reported as the average

scores via a weighted aggregation of the maximum and average

across runs.

values. It selects the top ten interfaces with the highest scores as

| As shown in Table 16, under explicit requirements, G1 and G2 | sources in the global interface state transition graph, and com- |  |  |
| --- | --- | --- | --- |
| perform similarly, indicating that user interaction feedback does | pletes intermediate interfaces through shortest path search to |  |  |
| not introduce additional interference to explicit test requirements. | form an associated interface subgraph related to testing require- |  |  |
| However, under ambiguous requirements, G2 shows degraded | ments. During testing, the rectangular coordinates of the entry |  |  |
| performance relative to G1, with a 31 | % | drop in function segmen- | area and the list of activities of the associated interfaces are also |
| tation accuracy, 8 fewer crashes detected, and an increase of 17.4 | used to limit the random event sending of the Monkey kernel. |  |  |

min in the fi rst triggering crash. The ablation experiment results

In terms of experimental results, we recorded the function seg-

show that incorporating user interaction feedback can mitigate

mentation accuracy (FS-Acc), the number of crash detections (C-

the impact of ambiguous user requirements on system test perfor-

Det), detection rate (D-Rate), and time to detect crash (T-DC), and

mance, enhancing GPT-Monkey ’ s robustness under ambiguous

additionally computed entry area identi fi cation accuracy (EAI-

natural language input.

Acc) and related interface coverage (RI-Cov) on the Themis

benchmark in Table 17.

6.4.5 | Effectiveness Comparison Between LLM-Driven

Speci fi cally, GPT-Monkey maintained 100 % FS-Acc on the 68

Modules and Lightweight Text-Focused Strategy

target functions in Themis, whereas Monkey-TextFocus

| To further distinguish the bene | fi | ts brought by shrinking the test- | achieved an FS-Acc of 69.1 | % | . Further analysis shows that Mon- |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ing scope from the gains introduced by GPT-Monkey | ’ | s multi- | key-TextFocus achieved an entry area identi | fi | cation accuracy of |  |  |  |  |
| modal semantic understanding, function segmentation, and | 82.4 | % | (56/68), but covered only about 76 | % | of the manually anno- |  |  |  |  |
| parameter tailoring and ensure a fair comparison, we implemen- | tated associated interfaces on average, indicating that a consid- |  |  |  |  |  |  |  |  |
| ted and evaluated a lightweight Monkey variant, denoted as | erable portion of function execution paths are truncated or |  |  |  |  |  |  |  |  |
| Monkey-TextFocus, which does not rely on any LLM and adopts | shifted. For crash detection, Monkey-TextFocus detected 23 |  |  |  |  |  |  |  |  |
| a simple strategy that selects app parts with higher textual and | crashes among the 52 known crashes, achieving a detection |  |  |  |  |  |  |  |  |
| semantic similarity to the target function. Speci | fi | cally, without | rate of 44.2 | % | , which lies between GPT-Monkey | ’ | s 53.8 | % | and the |
| introducing any LLM, this baseline only leverages the natural | traditional Monkey | ’ | s 42.3 | % | . For detection ef | fi | ciency, Monkey- |  |  |
| language description of the testing requirements input by the | TextFocus achieved an average T-DC of 59.73 min, which is lon- |  |  |  |  |  |  |  |  |
| user, the global interface state transition graph, and the interface | ger than GPT-Monkey | ’ | s 28.57 min. These results indicate that |  |  |  |  |  |  |

TABLE 17 | Comparison of Monkey-textFocus with GPT-Monkey on Themis benchmark.

| Tools | FS-Acc ( | % | ) | EAI-Acc ( | % | ) | RI-Cov ( | % | ) | C-Det | D-Rate ( | % | ) | T-DC (min) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GPT-Monkey | 100.0 | 100.0 | 100.0 | 28 | 53.8 | 28.57 |  |  |  |  |  |  |  |  |
| Monkey-textFocus | 69.1 | 82.4 | 76 | 23 | 44.2 | 59.73 |  |  |  |  |  |  |  |  |
| Monkey | — | — | — | 22 | 42.3 | 76.18 |  |  |  |  |  |  |  |  |
| IET Software, | 2026 | 25 of 29 |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 26

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| restricting the test scope solely through text similarity can reduce | The second threat involves the testing kernel. GPT-Monkey cur- |  |  |
| --- | --- | --- | --- |
| irrelevant exploration, but cannot achieve the detection ef | fi | - | rently uses only a Monkey-based testing kernel (Maxim) for exe- |
| ciency of the LLM-driven function segmentation and parameter | cution. Although the function segmentation and parameter |  |  |
| tailoring approach. | tailoring modules are designed to be kernel-agnostic, the gener- |  |  |

ated instructions are speci fi c to Monkey ’ s command-line format.

Overall, the results show that a lightweight focusing test strategy

Applicability to other frameworks (e.g., Appium or Espresso) has

relying only on interface text information is insuf fi cient to com-

not been evaluated.

pensate for Monkey ’ s lack of understanding of the interface and

| function. GPT-Monkey | ’ | s core advantage is not merely shrinking | The third threat relates to the benchmark composition and exper- |
| --- | --- | --- | --- |
| the testing scope, but the function segmentation obtained through | imental environment. Our real-world benchmark covers 1000 |  |  |
| global interface association, cross-modal alignment, and LLM rea- | popular apps from Google Play, but the results may not generalize |  |  |
| soning, as well as the parameter tailoring and adaptive optimiza- | to less popular, region-speci | fi | c, or enterprise apps. Furthermore, |
| tion enabled by the parameter-RAG method and the dual- | all tests are performed on emulators, which may exhibit behav- |  |  |
| feedback mechanism. | ioral differences compared to real devices. |  |  |

7.1.3 | Construct Validity

7 | Threats and Research Implications

The fi rst threat relates to the function segmentation accuracy

7.1 | Threats to Validity metric, which is evaluated based on manually de fi ned ground-

truth annotations. As no standardized de fi nition of function

7.1.1 | Internal Validity

boundaries exists, the ground truth inevitably re fl ects the adopted

| The | fi | rst threat concerns manual segmentation bias. The ground- | annotation schema rather than an objective standard, which may |  |  |
| --- | --- | --- | --- | --- | --- |
| truth function segmentation was performed by a single annotator | yield different accuracy values across studies and to some extent |  |  |  |  |
| per application following uni | fi | ed rules based on main navigation | limits cross-study comparability of the reported results. |  |  |
| tabs or business entry points. However, subjective judgment may | The second threat concerns the in | fl | uence of the time budget on |  |  |
| still in | fl | uence function boundary identi | fi | cation, particularly for | crash detection results. Each method is allocated 300 min per app, |
| apps with ambiguous or overlapping structures. We did not con- | a common setting in GUI testing studies, but a longer budget |  |  |  |  |
| duct parallel annotation or inter-annotator agreement measure- | could potentially allow baselines to detect more crashes, narrow- |  |  |  |  |
| ment, which may introduce uncertainty into the benchmark. | ing the gap with GPT-Monkey. The sensitivity of results to differ- |  |  |  |  |
| Future work could adopt multi-annotator validation to improve | ent time budgets was not systematically evaluated, representing a |  |  |  |  |
| reliability. | limitation of the current study. |  |  |  |  |

The second threat relates to LLM randomness. LLMs are inher-

ently non-deterministic, potentially affecting reproducibility. To 7.2 | Research Implications for Researchers and

mitigate this, GPT-Monkey employs standardized prompt tem- Practitioners

plates, a user interaction feedback mechanism for verifying

| LLM outputs, and the parameter-RAG module to constrain | Regarding the implications for researchers, this study demon- |  |  |
| --- | --- | --- | --- |
| parameter generation by grounding outputs in a structured | strates the feasibility of using LLM for GUI testing, particularly |  |  |
| knowledge base. Additionally, each ablation con | fi | guration was | in interface understanding, function segmentation, and parameter |
| repeated three times with averaged results. Nevertheless, some | generation aspects. The function segmentation approach adopted |  |  |
| degree of non-determinism may still persist, and results may | by GPT-Monkey, along with its natural language-driven auto- |  |  |
| vary across different runs or API versions. | matic testing strategy, provides valuable insights for future |  |  |

research. Additionally, the user interaction feedback and log anal-

| The third threat involves prompt sensitivity. GPT-Monkey | ’ | s per- | ysis feedback mechanisms proposed in this study offer references |
| --- | --- | --- | --- |
| formance depends on the design and wording of the prompt tem- | for how to improve the reliability and practicality of LLM when |  |  |
| plates, and variations in structure or phrasing may in | fl | uence the | applied to GUI testing. |

quality of LLM outputs. While the same templates are applied

Regarding the implications for practitioners, this study provides a

consistently across all experiments to ensure fair comparison,

simple and ef fi cient solution for GUI testing of Android apps.

the optimality of the current template design has not been system-

Practitioners only need to describe testing requirements in natural

atically evaluated, which remains a direction for future work.

language, and GPT-Monkey automatically completes function

segmentation and parameter generation. This approach allows

7.1.2 | External Validity practitioners to precisely test the speci fi c function, reducing

unnecessary operations and improving the ef fi ciency of detecting

The fi rst threat concerns the generalizability across platforms. All crashes.

experiments are conducted exclusively on Android applications,

and GPT-Monkey relies on Android-speci fi c tools such as UIAu-

tomator and DroidBot. Consequently, the results may not gener- 8 | Related Work

alize to other platforms (e.g., iOS) or desktop applications.

| Extending GPT-Monkey to other platforms would require adapt- | 8.1 | \| | Automated GUI Testing |
| --- | --- | --- | --- |
| ing the interface extraction and state exploration modules | To ensure the stability of mobile apps, lots of research has been |  |  |
| accordingly. | devoted to automated GUI testing [2, 29]. Monkey [4], the most |  |  |
| 26 of 29 | IET Software, | 2026 |  |

---

## Page 27

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| popular automated GUI testing tool, sends random testing events | Different from these methods, GPT-Monkey combines the Mon- |  |  |
| --- | --- | --- | --- |
| to detect crashes without speci | fi | c scripts. However, its fully ran- | key kernel with LLM, overcoming the limitation that LLM merely |
| dom operations across the entire interface often led to wasted | guides conventional operations. It makes better use of LLM |  |  |
| testing events and low testing ef | fi | ciency. | throughout the testing process from user requirement analysis |

to testing parameter generation. Additionally, GPT-Monkey auto-

To improve the overly random testing strategy, model-based auto-

matically segments crash-prone functions and tailors testing

mated GUI testing methods have been proposed [9 – 12, 36, 37]

parameters based on function characteristics. Moreover, GPT-

which guide the testing process through prede fi ned models based

Monkey minimizes the frequency of interaction with LLM in

on app function and user interaction logic. For instance, APE [9]

which the test instruction generated by running GPT-Monkey

adopted the dynamic testing framework for strategy updates by

once supports continuous operations, improving testing ef fi ciency

using runtime information. TimeMachine [10] embraced the con-

and reducing resource expenditures.

cept of “ time travel ” to capture and restore app states. Combo-

Droid [11] systematically navigated app functions by enumerating

combinations of use cases for high-quality testing inputs.

Although model-based GUI testing offers a systematic process, 9 | Conclusion

its ef fi ciency is limited by generating redundant or low-priority

This paper has presented a novel GUI testing tool, GPT-Monkey,

testing events and relying on prede fi ned structures that cannot

which combines the randomness of traditional Monkey-based

adapt to diverse app interfaces.

GUI testing with the powerful analysis capability of LLM.

| To reduce the reliance on manual experience, learning-based auto- | Through the employment of LLM, | fi | rstly, the testing requirements |  |  |
| --- | --- | --- | --- | --- | --- |
| mated GUI testing methods have been introduced [13 | – | 15, 38 | – | 40]. | have been understood by GPT-Monkey. Subsequently, the tar- |
| For example, Q-testing [13] innovated with a reinforcement learn- | geted function has been segmented and the corresponding testing |  |  |  |  |
| ing-based approach to uncover bugs and employed a curiosity-driven | parameters have been tailored. Then, the executable scripts, |  |  |  |  |
| strategy to test unexplored functions. OAT [14] leveraged deep rein- | which can realize the stress testing targeted at a speci | fi | c function, |  |  |
| forcement learning to optimize the testing framework. DQT [15] | have been generated by GPT-Monkey. Finally, execution results |  |  |  |  |
| preserved widgets | ’ | structural and semantic information with graph | from the Monkey kernel have been returned to the LLM through |  |  |
| embedding techniques and guided curiosity-driven exploration by | log analysis feedback to adjust test parameters and iteratively |  |  |  |  |
| learning test knowledge. IAAT [38] leveraged user operation pro- | optimize automated GUI testing. The usefulness and effectiveness |  |  |  |  |
| cesses to guide and re | fi | ne testing strategies iteratively. | of GPT-Monkey have been evaluated on standard benchmark and |  |  |
| Although learning-based GUI testing can intelligently optimize | real-world application benchmark, respectively. Results in the |  |  |  |  |
| strategies, its test precision and ef | fi | ciency are still limited as it | standard benchmark demonstrate that GPT-Monkey has achieved |  |  |
| only learns commonalities in user behavior and overlooks GUI | a 100 | % | accuracy in segmenting functions and has increased the |  |  |
| element semantics and user requirements. GPT-Monkey proposes | detection rate by 27.3 | % | and 16.7 | % | in comparison with the tradi- |
| a more intelligent and ef | fi | cient method using LLM to understand | tional Monkey and the optimal baseline method, respectively. In |  |  |
| interfaces, segment and test the targeted function with the mobile | addition, GPT-Monkey has increased the detection ef | fi | ciency by |  |  |
| app according to user requirements. | 62.5 | % | and 34.5 | % | in comparison with the traditional Monkey and |

the optimal baseline method, respectively. In the real-world appli-

cation benchmark, GPT-Monkey has achieved a 95 % accuracy in

8.1.1 | LLM for Automated GUI Testing function segmentation and found 397 crashes. In conclusion,

GPT-Monkey can enhance the Monkey-based automated GUI

Recently, researchers have successfully leveraged the powerful

testing for the mobile app by utilizing interface understanding

understanding ability of LLM to solve various tasks in the software

engineering and software security fi elds [18 – 25, 41 – 43]. Inspired and function segmentation driven by LLM.

by the above studies, researchers have applied LLM to automated

GUI testing to address limitations in existing methods. For

instance, DroidBot-GPT [18] converted GUI state information,

the action history and the task into a prompt for the LLM to Funding

make a choice of actions for the task. LLMDroid [19] introduced

This work was supported by the National Natural Science Foundation

| a two-stage testing framework that combines autonomous explo- | of China under Grant 62176265, the National Natural Science Founda- |  |  |
| --- | --- | --- | --- |
| ration with LLM guidance, achieving signi | fi | cant improvements in | tion of the China Youth Science Fund Project (C) under Grant |
| code coverage while minimizing LLM interactions for cost ef | fi | - | 62502103, and the China Postdoctoral Science Foundation under Grant |
| ciency. GERALLT [20] applied LLMs to perform exploratory test- | 2025M771548. The IIE author was supported in part by NSFC (Grant |  |  |
| ing of real-life engineering software GUIs, automatically | U24A20236) and the CAS Project for Young Scientists in Basic |  |  |
| generating lists of potential unintuitive and inconsistent interface | Research (Grant YSBR-118). |  |  |

elements. MemoDroid proposed a three-layer dynamic memory

Con fl icts of Interest

mechanism that enables LLM-based GUI testing [21] to accumu-

late and reuse testing experience across repeated interactions, The authors declare no con fl icts of interest.

enhancing activity coverage, code coverage, and bug detection.

| AutoDroid [25] integrated language understanding and reasoning | Data Availability Statement |  |  |
| --- | --- | --- | --- |
| capabilities of LLM with dynamic analysis of Android apps with- | The data that support the | fi | ndings of this study are available from Zhanhui |
| out manual intervention. | Yuan (yzh_yuanzhanhui@bjtu.edu.cn) upon reasonable request. |  |  |
| IET Software, | 2026 | 27 of 29 |  |

---

## Page 28

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

References 40th IEEE/ACM International Conference on Automated Software

Engineering (2025): 1603 – 1615.

1. R. Coppola, L. Ardito, M. Torchiano, and E. Al é groth, “ Translation

From Layout-Based to Visual Android Test Scripts: An Empirical 22. A. Mastropaolo, N. Cooper, D. N. Palacio, et al., “ Using Transfer

Evaluation, ” Journal of Systems and Software 171 (2021): 110845. Learning for Code-Related Tasks, ” IEEE Transactions on Software

Engineering 49, no. 4 (2023): 1580 – 1598.

2. H. N. Silva, J. Prado Lima, S. R. Vergilio, and A. T. Endo, “ A Mapping

Study on Mutation Testing for Mobile Applications, ” Software Testing, 23. M. Sch ä fer, S. Nadi, A. Eghbali, and F. Tip, “ An Empirical

Veri fi cation and Reliability 32, no. 8 (2022): e1801. Evaluation of Using Large Language Models for Automated Unit Test

Generation, ” IEEE Transactions on Software Engineering 50, no. 1

3. H. Hu, H. Wang, R. Dong, X. Chen, and C. Chen, “ Enhancing GUI

(2024): 85 – 105.

Exploration Coverage of Android Apps With Deep Link-Integrated

Monkey, ” ACM Transactions on Software Engineering and Methodology 24. M. Nass, E. Al é groth, and R. Feldt, “ Improving Web Element

33, no. 6 (2024): 1 – 31. Localization by Using a Large Language Model, ” Software Testing,

Veri fi cation and Reliability 34, no. 7 (2024): e1893.

4. A. Developers, “ Ui/Application Exerciser Monkey, ” A. Developers 8

(2012). 25. H. Wen, Y. Li, G. Liu, et al., “ Autodroid: LLM-Powered Task

Automation in Android, ” in 30th Annual International Conference on

5. Android Developers, “ Espresso, ” Android Developers 3 (2024).

Mobile Computing and Networking (2024): 543 – 557.

6. Android Developers, “ Ui Automator, ” Android Developers 5 (2024).

26. C. Bernal-C á rdenas, N. Cooper, M. Havranek, et al., “ Translating

7. Appium, “ Appium Documentation, ” Appium 7 (2024). Video Recordings of Complex Mobile App UI Gestures Into Replayable

Scenarios, ” IEEE Transactions on Software Engineering 49, no. 4 (2023):

8. Maxim, 2024, [Online]. Available: https://github.com/zhangzhao4444/ 1782 – 1803.

Maxim.

27. R. Rua and J. Saraiva, “ A Large-Scale Empirical Study on Mobile

9. T. Gu, C. Sun, X. Ma, et al., “ Practical GUI Testing of Android Performance: Energy, Run-Time and Memory, ” Empirical Software

Applications via Model Abstraction and Re fi nement, ” in Proceedings of Engineering 29, no. 1 (2024): 56.

the 41st International Conference on Software Engineering (2019): 269 – 280.

28. L. Ardito, A. Bottino, R. Coppola, et al., “ Feature Matching-Based

| 10. Z. Dong, M. B | ö | hme, L. Cojocaru, and A. Roychoudhury, | “ | Time- | Approaches to Improve the Robustness of Android Visual GUI Testing, | ” |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Travel Testing of Android Apps, | ” | in | Proceedings of the ACM/IEEE 42nd | ACM Transactions on Software Engineering and Methodology | 31, no. 2 |  |  |
| International Conference on Software Engineering | (2020): 481 | – | 492. | (2022): 1 | – | 32. |  |
| 11. J. Wang, Y. Jiang, C. Xu, C. Cao, X. Ma, and J. Lu, | “ | ComboDroid: | 29. L. Nie, K. S. Said, L. Ma, Y. Zheng, and Y. Zhao, | “ | A Systematic |  |  |
| Generating High-Quality Test Inputs for Android Apps via Use Case | Mapping Study for Graphical User Interface Testing on Mobile Apps, | ” |  |  |  |  |  |
| Combinations, | ” | in | Proceedings of the ACM/IEEE 42nd International | IET Software | 17, no. 3 (2023): 249 | – | 267. |

Conference on Software Engineering (2020): 469 – 480.

30. Y. Li, Z. Yang, Y. Guo, and X. Chen, “ Droidbot: A Lightweight UI-

| 12. H. Hasan, B. T. Ladani, and B. Zamani, | “ | Curious-Monkey: Evolved | Guided Test Input Generator for Android, | ” | in | ICSE 25: Proceedings of the |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Monkey for Triggering Malicious Payloads in Android Malware, | ” | The ISC | IEEE/ACM 47th International Conference on Software Engineering | (2017): |  |  |  |  |  |  |  |
| International Journal of Information Security | 13, no. 2 (2021): 131 | – | 143. | 23 | – | 26. |  |  |  |  |  |
| 13. M. Pan, A. Huang, G. Wang, T. Zhang, and X. Li, | “ | Reinforcement | 31. Android | Developers, | “ | Android | Debug | Bridge, | ” | 2023, | [Online]. |
| Learning Based Curiosity-Driven Testing of Android Applications, | ” | IEEE | Available: https://developer.android.com/tools/adb. |  |  |  |  |  |  |  |  |

Transactions on Software Engineering 50 (2020): 153 – 164.

32. Google, “ Google Play, ” 2024, [Online]. Available: https://play.google.

14. M. Du, P. Li, L. Song, W. K. Chan, and B. Jiang, “ Oat: An Optimized com/store/apps.

Android Testing Framework Based on Reinforcement Learning, ” in

Theoretical Aspects of Software Engineering , (Springer, 2023): 38 – 58. 33. T. Su, G. Meng, Y. Chen, et al., “ Guided, Stochastic Model-Based GUI

Testing of Android Apps, ” in Proceedings of the 11th Joint Meeting on

15. Y. Lan, Y. Lu, Z. Li, et al., “ Deeply Reinforcing Android GUI Testing Foundations of Software Engineering (2017): 245 – 256.

With Deep Reinforcement Learning, ” in 46th IEEE/ACM International

Conference on Software Engineering (2024): 854 – 866. 34. Q. McNemar, “ Note on the Sampling Error of the Difference Between

Correlated Proportions or Percentages, ” Psychometrika 12, no. 2 (1947):

16. T. Su, J. Wang, and Z. Su, “ Benchmarking Automated GUI Testing for 153 – 157.

Android Against Real-World Bugs, ” in Proceedings of the 29th ACM Joint

Meeting on European Software Engineering Conference and Symposium on 35. C. W. Dunnett, “ A Multiple Comparison Procedure for Comparing

the Foundations of Software Engineering (2021): 119 – 130. Several Treatments With a Control, ” Journal of the American Statistical

Association 50, no. 272 (1955): 1096 – 1121.

17. OpenAI, “ Introducing Chatgpt, ” 2024, [Online]. Available: https://

openai.com/blog/chatgpt#OpenAI. 36. Z. Lei, W. Zhao, Z. Ding, M. Xia, and Z. Qi, “ Appspin:

Recon fi guration-Based Responsiveness Testing and Diagnosing for

18. H. Wen, H. Wang, J. Liu, and Y. Li, “ DroidBot-GPT: GPT-Powered UI Android Apps, ” Automated Software Engineering 29, no. 2 (2022).

Automation for Android, ” ArXiv 4 (2024).

37. H. Wang, Y. Li, J. Yang, D. Hu, and Z. Liao, “ CamDroid: Context-

19. C. Wang, T. Liu, Y. Zhao, M. Yang, and H. Wang, “ LLMDroid:

Aware Model-Based Automated GUI Testing for Android Apps, ”

Enhancing Automated Mobile App GUI Testing Coverage With Large

Tsinghua Science and Technology 30, no. 1 (2025): 55 – 67.

Language Model Guidance, ” in Proceedings of the ACM on Software

Engineering (2025): 1 – 22. 38. Y. Zhong, M. Shi, Y. Xu, C. Fang, and Z. Chen, “ Iterative Android

Automated Testing, ” Frontiers of Computer Science 17, no. 5 (2022).

20. T. Rosenbach, D. Heidrich, and A. Weinert, “ Automated Testing of

| the GUI of a Real-Life Engineering Software Using Large Language | 39. Y. Zhao, B. Harrison, and T. Yu, | “ | Dinodroid: Testing Android Apps |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Models, | ” | in | IEEE | International | Conference | on | Software | Testing, | Using Deep q-Networks, | ” | ACM Transactions on Software Engineering and |
| Veri | fi | cation and Validation Workshops | (2025): 103 | – | 110. | Methodology | 33, no. 5 (2024): 1 | – | 24. |  |  |
| 21. M. Chen, Z. Liu, C. Chen, et al., | “ | Beyond Static GUI Agent: Evolving | 40. S. Yu, C. Fang, X. Li, Y. Ling, Z. Chen, and Z. Su, | “ | Effective, Platform- |  |  |  |  |  |  |
| LLM-Based GUI Testing via Dynamic Memory, | ” | in | Proceedings - 2025 | Independent GUI Testing via Image Embedding and Reinforcement |  |  |  |  |  |  |  |
| 28 of 29 | IET Software, | 2026 |  |  |  |  |  |  |  |  |  |

---

## Page 29

ietsfw, 2026, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/sfw2/9976714 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Learning, ” ACM Transactions on Software Engineering and Methodology

33, no. 7 (2024): 1 – 27.

41. S. Alagarsamy, C. Tantithamthavorn, and A. Aleti, “ A3Test:

Assertion-Augmented Automated Test Case Generation, ” Information

and Software Technology 176 (2024): 107565.

42. S. Kang, B. Chen, S. Yoo, and J. G. Lou, “ Explainable Automated

Debugging via Large Language Model-Driven Scienti fi c Debugging, ”

Empirical Software Engineering 30, no. 2 (2025).

43. Y. Peng, H. Hu, F. Li, Y. Jiang, J. Tang, and Y. Liu, “ LLM4Game:

Multi-Agent Reinforcement Learning With Knowledge Injection for

Dynamic Defense Resource Allocation in Cloud Storage, ” Computer

Networks 273 (2025): 111748.

IET Software, 2026 29 of 29

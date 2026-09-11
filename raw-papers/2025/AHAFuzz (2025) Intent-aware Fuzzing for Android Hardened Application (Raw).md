---
title: "Intent-aware Fuzzing for Android Hardened Application"
author: "Seongyun Jeong"
creator: "LaTeX with acmart 2025/05/30 v2.14 Typesetting articles for the Association for Computing Machinery and hyperref 2024-01-20 v7.01h Hypertext links for LaTeX"
pages: 15
---

# Intent-aware Fuzzing for Android Hardened Application

> **作者**：Seongyun Jeong
> **總頁數**：15 頁

---

## Page 1

Intent-aware Fuzzing for Android Hardened Application

| Seongyun Jeong | Minseong Choi | Haehyun Cho |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UNIST | UNIST | Soongsil University |  |  |  |  |  |  |  |  |  |  |  |  |
| Ulsan, Republic of Korea | Ulsan, Republic of Korea | Seoul, Republic of Korea |  |  |  |  |  |  |  |  |  |  |  |  |
| jsy01311@unist | . | ac | . | kr | liberty@unist | . | ac | . | kr | haehyun@ssu | . | ac | . | kr |

Abstract

Android; Hardened Application; Intent; Fuzzing; Obfuscation; eBPF;

sub Kim, and Yuseok Jeon. 2025. Intent-aware Fuzzing for Android Hard-

ened Application. In Proceedings of the 2025 ACM SIGSAC Conference on

Computer and Communications Security (CCS ’25), October 13–17, 2025,

© 2025 Copyright held by the owner/author(s).

ACM ISBN 979-8-4007-1525-9/2025/10

https://doi . org/10 . 1145/3719027 . 3744858

∗

1 Introduction

engineer. Therefore, hardening techniques like obfuscation and

ened apps. On the other hand, dynamic analysis, which observes

niques ( e . g ., obfuscation or packing), making it a more practical

option. Generally, fuzzing techniques [6, 36, 38, 57, 58] are widely

tent [24] is a key element used in Android development along with

user interactions ( i . e ., GUIs). In Android, an intent is a message

service, or deliver a broadcast. Because Android apps are event-

that directly execute components and change program behavior

are crucial to analyze Android apps. Especially, intents are key fac-

attacks [12].

| Seokwoo Choi | Hyungsub Kim | Yuseok Jeon |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The Affiliated Institute of ETRI | Indiana University Bloomington | Korea University |  |  |  |  |  |  |
| Daejeon, Republic of Korea | Bloomington, Indiana, USA | Seoul, Republic of Korea |  |  |  |  |  |  |
| seogu | . | choi@gmail | . | com | hk145@iu | . | edu | ys_jeon@korea.ac.kr |
| The widespread adoption of app hardening techniques in Android | Android is a mobile operating system holding a 70 | . | 69% market |  |  |  |  |  |
| applications makes it more challenging for current analysis tech- | share [8], with approximately 3 | . | 9 million Android applications |  |  |  |  |  |
| niques to analyze hardened apps, leading to limited analysis cov- | (apps) available on the Google Play store [10]. Due to various poten- |  |  |  |  |  |  |  |
| erage. This limitation is mainly due to the difficulties in obtaining | tial security and privacy issues ( | e | . | g | ., malware or privacy leaks) in An- |  |  |  |
| detailed information about Intents, which is essential for compo- | droid apps, it is important to analyze Android apps to identify these |  |  |  |  |  |  |  |
| nent communication and the execution of specific events in Android | issues in advance. However, many apps, whether legitimate or ma- |  |  |  |  |  |  |  |
| applications. | licious, have increasingly adopted app hardening [26, 28, 45, 47, 49] |  |  |  |  |  |  |  |
| In this paper, we introduce eBPF-based AHA-Fuzz, the first | techniques ( | e | . | g | ., obfuscators, packers, protectors, or anti-analysis) |  |  |  |
| intent-aware greybox fuzzing framework for Android hardened | to hinder such analyses. In particular, a preliminary analysis we |  |  |  |  |  |  |  |
| applications. AHA-Fuzz proposes a valid intent generator to create | performed discovers that obfuscation and packing app hardening |  |  |  |  |  |  |  |
| valid intent inputs that can trigger diverse Android app behav- | techniques are widely applied to 51% of benign apps (selected from |  |  |  |  |  |  |  |
| iors. To precisely evaluate the impact of these inputs, AHA-Fuzz | the top 100 most downloaded apps) and 99% of malicious apps (se- |  |  |  |  |  |  |  |
| presents a selective coverage feedback approach. Additionally, AHA- | lected 100 apps with the highest download numbers, all of which |  |  |  |  |  |  |  |
| Fuzz introduces approaches for efficiently triggering hard-to-trigger | are later identified as malicious). |  |  |  |  |  |  |  |
| bugs ( | e | . | g | ., scheduled malware) and detecting information leaks in | The benign apps generally leverage app hardening techniques to |  |  |  |
| hardened applications. Our evaluation results demonstrate that | protect against reverse engineering for unauthorized use ( | e | . | g | ., source |  |  |  |
| AHA-Fuzz triggers 92 | . | 3% more intents 3 | . | 45 | × | faster and executes | code leakage) and cracking. On the contrary, malicious apps gen- |  |
| 23 | . | 9% more methods than previous approaches. Additionally, AHA- | erally use them to hide code related to malicious behaviors. With |  |  |  |  |  |
| Fuzz has discovered 47 previously unknown bugs that existing | the widespread use of app hardening techniques, applying existing |  |  |  |  |  |  |  |
| approaches cannot detect. The developers of Google, Firefox, and | static analysis approaches to Android apps has become increas- |  |  |  |  |  |  |  |
| Facebook have acknowledged 6 out of 47 bugs, and have already | ingly difficult. More specifically, the main logic of Android apps |  |  |  |  |  |  |  |
| fixed three of them. | ( | e | . | g | ., DEX code compiled from Java) is relatively easy to reverse |  |  |  |
| CCS Concepts | packing are applied to prevent static analysis of these Android |  |  |  |  |  |  |  |
| • | Security and privacy | → | Software and application security | . | apps, and such approaches make static analysis unsuitable for hard- |  |  |  |
| Keywords | runtime behavior, can circumvent the impact of hardening tech- |  |  |  |  |  |  |  |
| ACM Reference Format: | used for dynamically analyzing Android apps. |  |  |  |  |  |  |  |
| Seongyun Jeong, Minseong Choi, Haehyun Cho, Seokwoo Choi, Hyung- | When fuzzing Android apps, to maximize test coverage, an | in- |  |  |  |  |  |  |
| Taipei, Taiwan. | ACM, New York, NY, USA, 15 pages. https://doi | . | org/10 | . | 1145/ | object used for communication between Android app components, |  |  |
| 3719027 | . | 3744858 | mainly used to transmit messages to start an activity, launch a |  |  |  |  |  |
| ∗ | Corresponding author | driven programs that interact with various components, intents |  |  |  |  |  |  |
| This work is licensed under a Creative Commons Attribution 4.0 International License. | tors in triggering and analyzing malicious behaviors because 76 | . | 2% |  |  |  |  |  |
| CCS ’25, Taipei, Taiwan | of them use intents to either hide malicious activities or initiate |  |  |  |  |  |  |  |

---

## Page 2

| CCS ’25, October 13–17, 2025, Taipei, Taiwan | Seongyun Jeong et al. |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Several existing intent fuzzing approaches [6, 13, 38, 40, 46, 57, | the Java object layout to locate intent-related information and then |  |  |  |  |  |  |
| 67] have been proposed to analyze Android apps. To perform effi- | extracts this information to generate valid intents. |  |  |  |  |  |  |
| cient intent fuzzing, it is required to generate valid intents ( | i | . | e | ., re- | To overcome the second challenge of applying coverage feedback |  |  |
| quiring key-value information), measure the impact of generated | messages, which are essential for measuring the impact of gener- |  |  |  |  |  |  |
| inputs ( | e | . | g | ., with coverage feedback messages), and leverage appro- | ated inputs, AHA-Fuzz proposes an eBPF-based coverage feedback |  |  |
| priate bug-trigger and detection strategies ( | e | . | g | ., altering scheduled | approach. More specifically, this approach can effectively monitor |  |  |
| events and detecting memory leaks). However, when targeting hard- | the execution of methods across Android’s different code patterns, |  |  |  |  |  |  |
| ened apps, existing intent fuzzing approaches need to tackle the | including AOT-compiled, JIT-compiled, and interpreted code. Ad- |  |  |  |  |  |  |
| following three challenges. | ditionally, coverage feedback may include irrelevant information, |  |  |  |  |  |  |
| The first challenge is extracting intent-related information, such | such as GUI events, which can negatively impact intent fuzzing. |  |  |  |  |  |  |
| as the key-value pairs (data added to the Intent object’s extras field) | To handle this issue, we propose a selective coverage feedback ap- |  |  |  |  |  |  |
| to generate valid intents. For hardened apps, this information is | proach that detects and filters out such noise for more accurate |  |  |  |  |  |  |
| difficult to extract through static analysis. Additionally, extracting | feedback. |  |  |  |  |  |  |
| such information during runtime is also challenging due to the | Successfully reaching problematic code is not enough; triggering |  |  |  |  |  |  |
| limitations of existing dynamic analysis approaches [2, 60, 62, 64, | and detecting hidden bugs, such as scheduled malware, in hardened |  |  |  |  |  |  |
| 66, 73]. More specifically, these limitations include the detection of | apps remains difficult ( | i | . | e | ., the third challenge). To address this last |  |  |
| analysis attempts ( | e | . | g | ., anti-debugging [9, 41, 61, 63, 68, 72]), the | challenge, AHA-Fuzz adjusts scheduling APIs to quickly trigger |  |  |
| porting effort for each version ( | e | . | g | ., system modification [60, 66]), | malware scheduled for delayed execution. More specifically, AHA- |  |  |
| and significant performance overhead ( | e | . | g | ., DBI [62, 64]). Although | Fuzz utilizes eBPF to hook scheduler-related functions and modify |  |  |
| Extended Berkeley Packet Filter (eBPF) [2, 73] provides a further | the associated scheduling times. Additionally, AHA-Fuzz introduces |  |  |  |  |  |  |
| reliable dynamic analysis environment with lower overhead and | a lightweight detection method for identifying information leaks |  |  |  |  |  |  |
| no need for an app or system modification, eBPF cannot directly | in hardened apps. This approach also utilizes eBPF to monitor APIs |  |  |  |  |  |  |
| identify the layout of objects containing intent-related information | that handle sensitive information, ensuring minimal overhead and |  |  |  |  |  |  |
| for generating valid intents. | avoiding system or app modifications. |  |  |  |  |  |  |
| The second challenge is the difficulty in applying coverage feed- | We evaluate AHA-Fuzz on Google Play store malware that uses |  |  |  |  |  |  |
| back to measure the impact of the intent fuzzer’s generated in- | complicated intents. Then, we confirm that AHA-Fuzz triggers |  |  |  |  |  |  |
| puts. More specifically, hardened apps use various obfuscation and | 92 | . | 3% of intent usage patterns compared to existing approaches |  |  |  |  |
| packing approaches, making it challenging to precisely identify | while AHA-Fuzz generates appropriate intents 3 | . | 45 | × | as fast. Fur- |  |  |
| instrumentation targets during static analysis or the app’s initial | ther, we measure AHA-Fuzz’s code coverage on 40 top downloaded |  |  |  |  |  |  |
| loading phase. As a result, traditional coverage instrumentation | Android apps, AHA-Fuzz invokes 23 | . | 9% more methods than pre- |  |  |  |  |
| methods are hard to apply for these hardened apps. Even when | vious approaches. We also run AHA-Fuzz on 300 Android apps; |  |  |  |  |  |  |
| instrumentation is successful, the Android app may invoke various | thus, AHA-Fuzz discovers 47 previously unknown bugs including |  |  |  |  |  |  |
| events, such as GUI events or background events, alongside intent | 26 crashes and 21 information leaks. Out of these 47 bugs, the de- |  |  |  |  |  |  |
| events triggered by the intent fuzzer. This causes noisy coverage | velopers of Google, Firefox, and Facebook have acknowledged two |  |  |  |  |  |  |
| feedback ( | i | . | e | ., GUIs and background events-related coverage infor- | crashes and four information leaks, and have already fixed three |  |  |
| mation) that can negatively impact the fuzzer’s ability to measure | of the four information leaks. It is worth noting that the previous |  |  |  |  |  |  |
| the impact of generated intent inputs accurately. | works cannot find the 47 bugs discovered by AHA-Fuzz. |  |  |  |  |  |  |
| Lastly, even if the fuzzer successfully reaches suspicious code, | In summary, we make the following contributions: |  |  |  |  |  |  |
| the challenge remains in triggering and detecting hidden bugs. For | • | Designing eBPF-Based Intent Fuzzer. | We develop an eBPF- |  |  |  |  |
| example, although fuzzer generated inputs may successfully reach a | based intent fuzzing environment that traces all Android events |  |  |  |  |  |  |
| suspicious section of code, they may fail to trigger a bug if the event | and extracts the intent parameters required to activate compo- |  |  |  |  |  |  |
| is scheduled under specific conditions. Note that Android apps fre- | nents in Android apps. AHA-Fuzz leverages this identified intent- |  |  |  |  |  |  |
| quently work by scheduling events through APIs ( | e | . | g | ., 55.2% of mali- | related information as guidance for mutating inputs. To the best |  |  |
| cious activities are triggered through scheduling [12]), meaning that | of our knowledge, AHA-Fuzz is the first work designing and |  |  |  |  |  |  |
| certain events cannot be easily triggered unless specific conditions | implementing a greybox intent fuzzer. |  |  |  |  |  |  |
| are met ( | e | . | g | ., an event scheduled to trigger after three days [43]). | • | Increasing Code Coverage. | We measure AHA-Fuzz’s coverage |
| Additionally, detecting triggered bugs such as information leaks | on 14 malware and 40 selected Android apps, and confirm that |  |  |  |  |  |  |
| is challenging with existing approaches [18, 59, 62, 64], as they | AHA-Fuzz calls, on average, 92 | . | 3% more intents (3 | . | 45 | × | faster) |
| require system modifications [18, 59] or impose high-performance | and executes 23 | . | 9% more methods compared to previous works. |  |  |  |  |
| overhead [62, 64] through DBI. In turn, the hardened apps require | • | Discovering Previously Unknown Bugs. | We run AHA-Fuzz |  |  |  |  |
| more practical and efficient bug detection methods. | on 300 Android apps. AHA-Fuzz discovers a total of 47 previously |  |  |  |  |  |  |
| In this paper, motivated by the lack of effective approaches to | unknown bugs. Out of the 47 bugs, 26 bugs cause crashes and |  |  |  |  |  |  |
| tackle the aforementioned challenges, we propose the Android | 21 bugs leads to information leaks. The developers of Google, |  |  |  |  |  |  |
| hardened app fuzzer (AHA-Fuzz). To address the first challenge | Firefox, and Facebook have acknowledged two crashes and four |  |  |  |  |  |  |
| ( | i | . | e | ., generating valid intent), AHA-Fuzz proposes a valid intent | information leaks, and have already fixed three of the four infor- |  |  |
| generator to efficiently obtain the key-value pairs of intents that | mation leaks. |  |  |  |  |  |  |

are actually registered and in use. For this, AHA-Fuzz first recovers

---

## Page 3

| Intent-aware Fuzzing for Android Hardened Application | CCS ’25, October 13–17, 2025, Taipei, Taiwan |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Table 1: Prevalence of App Hardening Techniques in Benign and | Table 2: Comparison of Major Features of Existing Intent Fuzzing |  |  |  |  |  |  |  |  |
| Malicious Android Apps. | Approaches. |  |  |  |  |  |  |  |  |
| App | Obfuscation | Packing | Anti- | Anti- | At least one | Approach | Input Coverage | Intent Generation Source | Feedback |
| Debugging | Emulator | Hardening Tech | MATE [6] | GUI & Intent | DEX intra-procedural analysis | None |  |  |  |
| Benign | 39 | 22 | 74 | 98 | 100 | Iccdroid [38], [13, 46] | Intent | DEX intra-procedural analysis | None |
| Malicious | 22 | 94 | 9 | 33 | 100 | Sasnauskus et al [57] | Intent | DEX inter-procedural analysis | None |
| IntentFuzzer [67], [40] | Intent | Key Feedback & DEX analysis | None |  |  |  |  |  |  |
| Total | 61 | 116 | 83 | 131 | 200 | AHA-Fuzz | GUI & Intent | Key-Value Feedback | Coverage-guided |

action ( e . g ., {BATTERY_LEVEL: 97} to notify battery status). Extras

2 Background and Motivation

play a crucial role in intent event analysis, as they are often used

| 2.1 | App Hardening Techniques | for communicating with backend servers ( | e | . | g | ., Firebase) or deliver- |
| --- | --- | --- | --- | --- | --- | --- |
| App hardening techniques, such as code obfuscation, are designed | ing specific payloads in malware. | Actions | and | extras | do not have |  |
| to protect an app from static and dynamic analysis [39]. Since | predefined values for each app and can only be identified through |  |  |  |  |  |
| Android apps are generally more susceptible to reverse engineer- | application code analysis. |  |  |  |  |  |
| ing compared to other platforms, they frequently incorporate app | Therefore, previous intent fuzzing approaches [6, 13, 38, 40, 46, |  |  |  |  |  |
| hardening techniques to enhance security and protect against unau- | 57, 67] mainly focus on analyzing code to extract intent-related |  |  |  |  |  |
| thorized analysis [16]. | details. Table 2 illustrates the main features of these existing in- |  |  |  |  |  |
| To examine the prevalence of app hardening techniques in An- | tent fuzzing approaches. Some research works including MATE [6] |  |  |  |  |  |
| droid apps, we analyze the top 100 most downloaded benign apps | perform the intra-procedural analysis [13, 38, 46] which maps in- |  |  |  |  |  |
| from Google Play and the 100 most downloaded malware samples | tents by tracking all invocations of intent-related methods within |  |  |  |  |  |
| from AndroZoo. To this end, we leverage the APKiD [55] to detect | the entry point methods of each component. While Sasnauskas |  |  |  |  |  |
| various app hardening techniques. As shown in Table 1, all benign | et al. [57] propose an inter-procedural analysis-based approach |  |  |  |  |  |
| and malicious apps utilize at least one app hardening technique. | that employs path-insensitive CFG analysis to obtain information |  |  |  |  |  |
| App hardening techniques not only | hinder | the functionality of | regarding intents [65]. On the other hand, hybrid-based approaches |  |  |  |
| analysis tools, such as debuggers and decompilers, but can also | including IntentFuzzer [67] leverage dynamic analysis techniques |  |  |  |  |  |
| render certain types of analysis | entirely impossible | by employing | to extract the key of extras in runtime [40]. However, all the previ- |  |  |  |
| mechanisms like packing, code encryption, and runtime integrity | ous works are ineffective against app hardening techniques such |  |  |  |  |  |
| checks [16]. Therefore, relying solely on a static analysis approach | as control-flow obfuscation because they rely on static analysis |  |  |  |  |  |
| is insufficient for effectively analyzing real-world Android apps, | which can fail to identify the extracting operation of action strings, |  |  |  |  |  |
| as they often employ complex obfuscation and anti-analysis tech- | and keys or values of extras. Moreover, the previous works do not |  |  |  |  |  |
| niques. This necessitates the use of dynamic analysis methods such | utilize the coverage feedback that provides real-time insights into |  |  |  |  |  |
| as intent fuzzing to complement static approaches and provide | the areas of code that have been executed during testing, enabling |  |  |  |  |  |
| deeper insights into application behavior during runtime. | more effective and efficient analysis. We, thus, require an effective |  |  |  |  |  |

and efficient intent fuzzing solution that can overcome challenges

2.2 Intent Fuzzing in analyzing hardened apps, ensuring broader code coverage, and

Intents are a fundamental component of app communication and be- reducing redundant tests.

havior [24]. Android apps use intents for three different use cases:

| launching an activity ( | e | . | g | ., screen), starting a service ( | e | . | g | ., back- | 2.3 | Dynamic Analysis Framework |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ground task), and delivering a broadcast message ( | e | . | g | ., system boot). | To measure code coverage and monitor app behaviors during in- |  |  |  |  |  |
| Analyzing intents provides critical insights into an app’s function- | tent fuzzing, a suitable dynamic analysis framework is essential. |  |  |  |  |  |  |  |  |  |
| ality, communication patterns, and potential security flaws. It’s an | Common approaches to building such a framework include (1) ap- |  |  |  |  |  |  |  |  |  |
| essential part of understanding Android app behaviors. Addition- | plication modification, (2) Dynamic Binary Instrumentation (DBI), |  |  |  |  |  |  |  |  |  |
| ally, various intent fuzzing efforts have been developed to generate | (3) system modification, and (4) eBPF. |  |  |  |  |  |  |  |  |  |
| and mutate intent data, ensuring the security, stability, and reliabil- | Application modification-based approaches instrument the DEX |  |  |  |  |  |  |  |  |  |
| ity of Android apps [6, 13, 38, 40, 46, 57, 67]. | code, which can be easily decompiled. Because this method does |  |  |  |  |  |  |  |  |  |
| To receive intents from other apps, an app must declare the spe- | not require separate analysis tools at runtime, it is widely used in |  |  |  |  |  |  |  |  |  |
| cific intents it wishes to handle in an intent filter. There are two | many fuzzing approaches for tracking code coverage [4, 52, 56]. |  |  |  |  |  |  |  |  |  |
| ways to define the intent filter: defining it in the app’s Manifest | However, this method is limited in handling dynamically loaded |  |  |  |  |  |  |  |  |  |
| file and registering it by calling | registerReceiver() | at runtime | components that are difficult to instrument during static analysis. |  |  |  |  |  |  |  |
| ( | i | . | e | ., dynamically registered intent). An intent includes standard | It, also, requires | repackaging | after instrumentation, which com- |  |  |  |
| fields such as | category | and | data | , but the most notable fields are | promises the app’s integrity and poses challenges when analyzing |  |  |  |  |  |
| action | and | extras | . Unlike other standard intent fields, which can | hardened apps with integrity checks. |  |  |  |  |  |  |
| easily retrieve related information from the Manifest file, | actions | On the other hand, the DBI-based approach instruments a target |  |  |  |  |  |  |  |  |
| (especially in dynamically registered intent) and | extras | can only | app at runtime, and thus, it can handle dynamically loaded code. |  |  |  |  |  |  |  |
| be extracted from the application code. The intent can include | However, the DBI-based approach can impose approximately ten |  |  |  |  |  |  |  |  |  |
| (1) an | action | field to request a specific action from another com- | times more overhead during app analysis, including code coverage |  |  |  |  |  |  |  |
| ponent ( | e | . | g | ., opening a map) and (2) an | extras | field consisting of | measurement [64]. Moreover, the DBI-based approach cannot be |  |  |  |
| key-value pairs to carry additional information on the requested | effectively used to analyze apps that implement anti-debugging |  |  |  |  |  |  |  |  |  |

---

## Page 4

CCS ’25, October 13–17, 2025, Taipei, Taiwan Seongyun Jeong et al.

Corpus

Engine

Raw bytes Object-aware

4.2 Valid intent Generator

Coverage Activity

AOT

❸ Service ❹ Coverage

Monitor Interpreter

Broadcast For Intent

Instrument

4.3 Coverage Feedback Generator

Figure 1: Overview of AHA-Fuzz’s Workflow.

The system modification approach leverages a customized ver-

tion, we assume that an attacker can directly trigger vulnerabilities

( e . g ., crash or information leak) in victim apps by sending crafted

intents. The primary goal of AHA-Fuzz is to analyze such malicious

apps through fuzzing, even in hardening conditions.

Action Time : 6 Hour

Mutated

Value

GUI Target ❺ Scheduler Manipulation

Event

| Application | - | Device ID |
| --- | --- | --- |
| Key-value | - | Network |
| feedback | - | Debug info |

❻ Detecting information leak

Coverage Environment

4.4 Bug Detection

feedback Capability Enhancer

can be significantly increased.

the roughly 10 times overhead [64] typically incurred by DBI-based

three main components:

(i) Valid Intent Generator (Section 4.2): To generate valid intent,

obtaining the key-value pair values of intent extras that are

actually registered and in use is important. For this, AHA-

related information (Section 4.2.1) and then extracts this

| Initial Seeds | Mutation | ❶ | Key | ❷ | Intent | App | Time : | 1 Min |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| techniques because such techniques detect and interfere with in- | launched exclusively through specific intents). By using these two |  |  |  |  |  |  |  |
| strumentation tools [9, 41, 61, 63, 68, 72]. | approaches complementarily, the test coverage of Android apps |  |  |  |  |  |  |  |
| sion of the Android Open Source Project (AOSP). This customized | For GUI fuzzing, we leverage APE [36], the state-of-the-art GUI |  |  |  |  |  |  |  |
| system allows for more precise analysis ( | e | . | g | ., instruction analysis) | fuzzer that performs fuzzing solely on GUI elements not gener- |  |  |  |
| compared to application-level analysis methods. However, build- | ally influenced by hardening techniques. To effectively balance |  |  |  |  |  |  |  |
| ing a customized system requires significant engineering effort | GUI and intent inputs according to the characteristics of the target |  |  |  |  |  |  |  |
| to understand and modify the Android Runtime (ART) source | app, AHA-Fuzz dynamically adjusts the ratio between GUI and |  |  |  |  |  |  |  |
| code [42, 54]. In addition, the huge manual engineering effort must | intent inputs using AHA-Fuzz’s customized feedback messages, |  |  |  |  |  |  |  |
| be repeated each time a new version is released. | as discussed in Section 4.3.2. For intent fuzzing, we generate ini- |  |  |  |  |  |  |  |
| Lastly, the Extended Berkeley Packet Filter (eBPF)-based ap- | tial seeds by analyzing the Android manifest file, which defines |  |  |  |  |  |  |  |
| proach enables observation without compromising app integrity | all statically registered intent entry points and is not protected |  |  |  |  |  |  |  |
| by setting tracing points with probes [2, 73]. However, because | by hardening techniques. Additionally, we capture dynamically |  |  |  |  |  |  |  |
| events can only be observed through predefined probes, the scope | registered intent events (Section 4.2.2) by hooking related meth- |  |  |  |  |  |  |  |
| of events that can be monitored is inherently limited. For example, | ods ( | e | . | g | ., | registerReceiver() | ). Note that the manifest file does not |  |
| using a probe requires knowledge of the target code address. How- | include information about intent extras. AHA-Fuzz alternates be- |  |  |  |  |  |  |  |
| ever, code executed by an interpreter or JIT, where the address is | tween generating GUI test inputs (using APE) and intent test inputs |  |  |  |  |  |  |  |
| unknown at the time of setting tracing points, cannot be monitored. | generated internally by our proposed intent fuzzer. |  |  |  |  |  |  |  |
| Moreover, eBPF can only access raw bytes in memory, making it | We note that AHA-Fuzz internally uses eBPF to create a reliable |  |  |  |  |  |  |  |
| difficult to observe Java-specific information. | low-management and performance overhead analysis environment. |  |  |  |  |  |  |  |
| Consequently, the current analysis frameworks face considerable | Specifically, eBPF allows observation of system events at the kernel |  |  |  |  |  |  |  |
| challenges in collecting code coverage and app behaviors during the | level without modifications to the app or system, enabling stable |  |  |  |  |  |  |  |
| fuzzing of hardened apps, highlighting the need for an enhanced | and accurate monitoring of events. Moreover, the overhead from |  |  |  |  |  |  |  |
| analysis framework to effectively handle such apps. | eBPF—approximately 1 | . | 5 times [2, 50]—is considerably less than |  |  |  |  |  |
| 3 | Threat Model | solutions. However, eBPF-based app analysis introduces several lim- |  |  |  |  |  |  |
| Our threat model assumes that both attackers and benign users | itations ( | e | . | g | ., understanding Java object layouts and generating ap- |  |  |  |
| can install malicious apps on the target victim devices. We also | propriate feedback messages for valid input generation). AHA-Fuzz |  |  |  |  |  |  |  |
| assume that several hardening techniques are applied to the mali- | addresses these limitations (detailed in Section 4.2 and Section 4.3) |  |  |  |  |  |  |  |
| cious apps to prevent static or dynamic analysis. Specifically, we | to provide stable and precise analysis environments. |  |  |  |  |  |  |  |
| consider ( | 𝑖 | ) runtime-based obfuscators such as packers that hinder | The overall architecture of the eBPF-based AHA-Fuzz is illus- |  |  |  |  |  |
| static analysis, ( | 𝑖𝑖 | ) integrity checks that detect app tampering, and | trated in Figure 1. To generate diverse and valid intent inputs and |  |  |  |  |  |
| ( | 𝑖𝑖𝑖 | ) protectors that detect dynamic analysis environments. In addi- | increase bug detection capability, AHA-Fuzz includes the following |  |  |  |  |  |
| 4 | Design | Fuzz first recovers the Java object layout to locate intent- |  |  |  |  |  |  |
| 4.1 | Overview of AHA-Fuzz | information to generate valid intents (Section 4.2.2). |  |  |  |  |  |  |
| AHA-Fuzz internally incorporates GUI fuzzing because analyzing | (ii) Coverage Feedback Generator (Section 4.3): To guide the |  |  |  |  |  |  |  |
| all behaviors of Android apps requires both intents and GUI events. | fuzzer in exploring deeper parts of the hardened app’s code, |  |  |  |  |  |  |  |
| More specifically, GUI fuzzing can trigger dynamically registered in- | it is essential to evaluate the impact of generated inputs using |  |  |  |  |  |  |  |
| tents, while intent fuzzing can directly invoke components that are | coverage feedback messages. For this, AHA-Fuzz introduces |  |  |  |  |  |  |  |
| otherwise challenging to access via the normal GUI path ( | e | . | g | ., ac- | the first coverage feedback technique among intent fuzzers |  |  |  |
| tivities visible only under certain conditions or settings screens | (Section 4.3.1). Additionally, it proposes a method to reduce |  |  |  |  |  |  |  |

---

## Page 5

| Intent-aware Fuzzing for Android Hardened Application | CCS ’25, October 13–17, 2025, Taipei, Taiwan |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| noise from observing non-intent-related events for more | Algorithm 1: | The algorithm of Java object layout recovering |  |  |  |  |
| accurate coverage feedback (Section 4.3.2). | Input | : | 𝐹 | , | 𝑇 | 𝑐 |
| (iii) Bug Detection Capability Enhancer (Section 4.4): Even if the | 𝐹 | : a given OAT file contains DEX and assembly code; |  |  |  |  |
| fuzzer successfully reaches problematic code, triggering and | 𝑇 | 𝑐 | : a given target class; |  |  |  |
| detecting hidden bugs remains a challenge. AHA-Fuzz pro- | 𝑆 | 𝑝 | : a set of pointers pointing to target Java object; |  |  |  |
| poses a technique to quickly trigger malware that is sched- | 𝑀 | 𝑒 | ⇐ | a map for storing fields with their exact offset; |  |  |
| uled to execute after a long delay by adjusting scheduling | 𝑀 | 𝑝 | ⇐ | a map for storing fields with their possible offsets; |  |  |
| APIs (Section 4.4.1). Additionally, AHA-Fuzz introduces a | Output : | Target classes’ layout information |  |  |  |  |
| lightweight detection method to identify information leaks | // | Step 1: | Extract field offset information in target instruction |  |  |  |

in hardened apps (Section 4.4.2).

4.2 Valid Intent Generator

how AHA-Fuzz obtains currently available key-value information

4.2.1 Recovering Java Object Layout. To create valid intents for

fuzzing, required essential information ( i . e ., key-value information

from an allocated Java object. However, to accurately extract the

required information, the Java object’s layout must be recognized.

For example, the value field, which is the specific value assigned to

the intent key, exists within the Java object. To extract information

layout needs to be identified. However, we cannot directly identify

offset information because memory layout information is lost after

AOT-compilation. The existing solution [64] for observing Java

information from assembly involves manually analyzing each offset,

with each version and device.

To address this issue, AHA-Fuzz proposes a method for recon-

its corresponding AOT-compiled assembly code. During the AOT-

compilation, field names and type information in the DEX code are

optimized away or removed, making it difficult to determine the off-

set of specific fields by examining the assembly alone. However, we

passes the second argument ( e . g ., the this pointer) to r1 and assigns

1 forall 𝑐𝑙𝑎𝑠𝑠 ∈ 𝐹 do

| 2 | if | 𝑐𝑙𝑎𝑠𝑠. | isClassIncluded | ( | T | c | ) | then |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 𝑚𝑒𝑡ℎ𝑜𝑑 | ⇐ | class | . | method | ; |  |  |  |  |  |
| 4 | forall | 𝑖𝑛𝑠𝑡 | ∈ | method.DEX | do |  |  |  |  |  |  |
| 8 | forall | 𝑖𝑛𝑠𝑡 | ∈ | method.Asm | do |  |  |  |  |  |  |
| 9 | TrackingPointer | ( | inst | , 𝑆 | 𝑝 | ) | ; |  |  |  |  |
| 10 | if | is_Field_Access(inst, | 𝑆 | 𝑝 | ) | then |  |  |  |  |  |
| 11 | if | Direct_Mapping(inst, method.field) | then |  |  |  |  |  |  |  |  |
| 13 | else |  |  |  |  |  |  |  |  |  |  |
| 14 | 𝑀 | 𝑝 | [ | method.field | ] | . | add | ( | inst.offset | ) | ; |

15 offsets ⇐ ∅ ;

16 forall 𝑓 𝑖𝑒𝑙𝑑 ∈ 𝑀 𝑒 .𝑓 𝑖𝑒𝑙𝑑 do

17 offsets . add ( M e [ field ] ) ;

18 forall field ∈ 𝑀 𝑝 . field do

| 20 | if | 𝑙𝑒𝑛 | ( | 𝑀 | 𝑝 | [ | field | ] ) ≡ | 1 | then |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 21 | offsets | . | add | ( | M | p | [ | field | ] ) | ; |
| 23 | goto | line | 20 |  |  |  |  |  |  |  |

24 return 𝑀 𝑒 , 𝑀 𝑝

from DEX code.

| For effective intent fuzzing, generating intents with valid key-value | 5 | if | is_Field_Access(inst) | then |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| information of intent extras is important. This subsection describes | 6 | 𝑚𝑒𝑡ℎ𝑜𝑑. | field | _ | update | ( | inst.field | ) | ; |  |  |  |  |
| and creates valid intents. | 7 | 𝑆 | 𝑝 | ⇐ | getTargetPointer | ( | method | ) | ; |  |  |  |  |
| of the intent presently in use and stored in memory) can be extracted | 12 | 𝑀 | 𝑒 | [ | method.field | ] ⇐ | inst.offset | ; |  |  |  |  |  |
| from this | value | field, the offset within the Java object’s memory | // | Step 2: | Recursively eliminate possible offsets, find exact offset |  |  |  |  |  |  |  |  |
| but it cannot support all Java objects, as offsets continuously change | 19 | 𝑀 | 𝑝 | [ | field | ] ⇐ | 𝑀 | 𝑝 | [ | 𝑓 𝑖𝑒𝑙𝑑 | ] \ | offsets | ; |
| structing Java object layouts by cross-referencing DEX code with | 22 | 𝑀 | 𝑒 | [ | 𝑓 𝑖𝑒𝑙𝑑 | ] ⇐ | 𝑀 | 𝑝 | [ | 𝑓 𝑖𝑒𝑙𝑑 | ] | ; |  |
| note that AOT assembly follows the JNI calling convention, which | by methods defined in these classes, which can be easily identified |  |  |  |  |  |  |  |  |  |  |  |  |
| subsequent arguments to | r2 | and beyond. This convention allows us | Algorithm 1 illustrates the DEX and assembly field access map- |  |  |  |  |  |  |  |  |  |  |
| to distinguish pointers to Java objects and identify memory access | ping process. First, AHA-Fuzz targets all methods of target classes |  |  |  |  |  |  |  |  |  |  |  |  |
| instructions involving these pointers. Consequently, we consider | (lines 1–3) and collects field access instructions from DEX bytecode |  |  |  |  |  |  |  |  |  |  |  |  |
| only memory access instructions performed through these pointers | (lines 4–6). AHA-Fuzz extracts pointer sets pointing to target Java |  |  |  |  |  |  |  |  |  |  |  |  |
| as object field access instructions. By mapping these field access | objects in assembly code (line 7). Then, using alias analysis over |  |  |  |  |  |  |  |  |  |  |  |  |
| instructions in the DEX bytecode to actual operations ( | e | . | g | ., memory | the pointer sets extracted earlier (line 7), AHA-Fuzz identifies addi- |  |  |  |  |  |  |  |  |
| load/store) in the AOT assembly, AHA-Fuzz enables the inference | tional field access instructions in the assembly (lines 8–10). Direct |  |  |  |  |  |  |  |  |  |  |  |  |
| of field offsets and their relationships within Java objects. | mappings allow certain offsets to be immediately resolved (lines |  |  |  |  |  |  |  |  |  |  |  |  |
| Note that analyzing the layout of every object used across all | 10–12), while other cases ( | e | . | g | ., related to branch conditions) are |  |  |  |  |  |  |  |  |
| Android methods is inefficient. Since the extracted layout informa- | saved for later resolution (lines 13–14). In the next step, AHA-Fuzz |  |  |  |  |  |  |  |  |  |  |  |  |
| tion is used for extracting intent-related information (Section 4.2.2), | performs additional mapping of unresolved offsets for each class. |  |  |  |  |  |  |  |  |  |  |  |  |
| key-value feedback generation (Section 4.2), selective coverage | First, AHA-Fuzz initialize the offset set of the target class (lines |  |  |  |  |  |  |  |  |  |  |  |  |
| feedback generation (Section 4.3.2), and scheduler manipulation | 16-17) using directly mapped values (lines 11-12). AHA-Fuzz then |  |  |  |  |  |  |  |  |  |  |  |  |
| (Section 4.4.1), AHA-Fuzz only focuses on extracting the layouts | iteratively refines the set by removing any offset from | 𝑀 | 𝑝 | that also |  |  |  |  |  |  |  |  |  |
| of objects utilized in methods relevant to these four features. For | exists in | offsets | (line 19). If a possible offset set contains only one |  |  |  |  |  |  |  |  |  |  |
| example, AHA-Fuzz targets Intent-related classes, such as | Intent | value (line 20), it becomes an exact offset and is updated recursively |  |  |  |  |  |  |  |  |  |  |  |
| and | IntentFilter | , and only analyzes the layouts of objects used | (lines 21–23). Consequently, AHA-Fuzz returns the exact offsets |  |  |  |  |  |  |  |  |  |  |

---

## Page 6

| CCS ’25, October 13–17, 2025, Taipei, Taiwan | Seongyun Jeong et al. |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Case 1. Direct Mapping | Case 2. Inferring Mapping | Case 3. Candidate | Table 3: Java object layout recovery result. Cases 1, 2, and 3 corre- |  |  |  |  |  |  |  |
| 1. public int size() { | Generation |  |  |  |  |  |  |  |  |  |
| Source | 1. public E get (int index) { | spond to direct mapping, inferring mapping, and candidate genera- |  |  |  |  |  |  |  |  |
| 2. | return | size | ; | 2. | if (index >= | size | ) | … | ArrayList | Register |

Code

3. } 3. return elementData … Object x1 tion, respectively.

#0

| 2. if-ge v3, v0, +7 | Object | modCount | Module name | Classes | Fields | Case 1 (%) | Case 2 (%) | Case 3 (%) |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1. iget v0, v1, | Int | ; | DEX | 3. iget-object v0, v2, | Object | ; | #8 | Metadata | Candidate |  |  |  |  |
| java.util.ArrayList. | size | Code | ArrayList. | elementData | content | 982 | 1,729 | 669 | (38.7%) | 681 | (39.4%) | 379 | (21.9%) |
| 2. return v0 | … | Candidate | #8, |  |  |  |  |  |  |  |  |  |  |
| Conflict | app | 1,559 | 3,465 | 1,523 | (44.0%) | 1,428 | (41.2%) | 514 | (14.8%) |  |  |  |  |
| Direct | … | #12 |  |  |  |  |  |  |  |  |  |  |  |
| element | #12 |  |  |  |  |  |  |  |  |  |  |  |  |
| Total | 2,541 | 5,194 | 2,192 | (42.2%) | 2,109 | (40.6%) | 893 | (17.2%) |  |  |  |  |  |
| Mapping | 10. ldr w22, [x1, | #16 | ] |  |  |  |  |  |  |  |  |  |  |
| #16 | Data | #16 | , |  |  |  |  |  |  |  |  |  |  |
| … | #20 | , |  |  |  |  |  |  |  |  |  |  |  |
| 1. ldr w0, [x1, | #16 | ] | Assembly | 15. ldr w22, [x1, | #12] | size |  |  |  |  |  |  |  |
| 2. ret | Code | … | Inferred | #20 |  |  |  |  |  |  |  |  |  |
| Mapping | Candidate | 4.2.2 | Key-value Feedback Generator. | Section 4.2.1 allows AHA- |  |  |  |  |  |  |  |  |  |

Fuzz to recover the Java object layout. Based on this layout informa-

Figure 2: Object Layout Recover Examples in java.util.ArrayList .

tion, this section explains how to extract intent-related information

stored in objects. Unlike C/C++, Java inherently manages elements

| and the possible offset candidates for still unresolved fields (line | such as strings ("msg") as objects. Therefore, understanding the |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 24). | layout of objects ( | e | . | g | ., strings) that store frequently used intent key- |  |  |
| Figure 2 shows examples of how AHA-Fuzz identifies object | value pairs is essential for accurate extraction. Using the key and |  |  |  |  |  |  |
| layouts in | java.util.ArrayList | . In Case 1 (left of Figure 2), the | value extraction methods introduced in this section, these extracted |  |  |  |  |
| size | function is a simple getter that returns the size field of an | values are sent to the fuzzer as key-value feedback messages (not |  |  |  |  |  |
| ArrayList object. Because it only includes a load operation, we can | coverage feedback). These messages are utilized to construct valid |  |  |  |  |  |  |
| directly map the field access in the DEX code (line 1, | iget Int; | intents. |  |  |  |  |  |
| ArrayList.size | ) to the corresponding assembly instruction (line 1, | Extracting Intent Key Set. | To extract the key used in the ex- |  |  |  |  |
| ldr w0, [x1, #16] | ). Consequently, we know the action field is at | tras field of intents, we utilize the following two patterns, as in |  |  |  |  |  |
| offset 16. | previous research [40, 67]. First, since the parameter of the intent- |  |  |  |  |  |  |
| In contrast, the | get | function in Case 2 (middle of Figure 2) in- | related extra getter functions is the key, hooking and analyzing |  |  |  |  |
| cludes branch instructions, making it more complex to establish a | these functions allows us to obtain the currently used keys. For |  |  |  |  |  |  |
| direct mapping between DEX and assembly. Because AOT-compiled | this, AHA-Fuzz hooks all related getter functions using eBPF. For |  |  |  |  |  |  |
| assembly follows the JNI calling convention, we can determine | example, encountering | getStringExtra("format") | indicates that |  |  |  |  |
| which pointer is stored in each register during the function pro- | "format" | is currently used as a key for a particular intent. |  |  |  |  |  |
| logue. Based on this information, path-insensitive pointer tracking | The second approach for retrieving currently used keys is to hook |  |  |  |  |  |  |
| allows us to identify potential field access instructions. For ex- | Bundle-related functions, such as | getChar() | . This is because, the |  |  |  |  |
| ample, lines 10 and 15 in the | get | assembly indicate access to the | extras field is internally implemented as an Android Bundle [21], |  |  |  |  |
| elementData | field of the ArrayList. From this, we can infer that | as a Bundle is essentially a map structure used by Android for |  |  |  |  |  |
| elementData | could be at offset 12 or 16. Additionally, since Case 1 | storing key-value pairs. By tracking these Bundle-related functions, |  |  |  |  |  |
| ( | i | . | e | ., | size | ) already confirms that offset 16 corresponds to the size | AHA-Fuzz can additionally extract currently used keys. |
| field, we infer that the | elementData | field must be at offset 12. | Extracting Intent Value Set. | Finding the value corresponding to |  |  |  |
| However, the | modCount | field in Case 3 (right of Figure 2) is not | a key is important for testing an app’s diverse and deep code. For |  |  |  |  |
| covered by direct mapping (Case 1) and inferring mapping (Case 2), | example, Android apps can change execution flow depending on |  |  |  |  |  |  |
| where precise offset inference is not possible. AHA-Fuzz handles | the value in the intent parameter ( | e | . | g | ., line 4 in Figure 3). However, |  |  |
| this unresolved field by continuously selecting its offset at random | unlike the method of observing keys from intents, there are no |  |  |  |  |  |  |
| from the candidate set during fuzzing. For example, | modCount | has | predefined patterns or APIs to retrieve values from intents. |  |  |  |  |
| possible offsets of 8 or 20, which are not resolved in the direct | To address this challenge, we manually analyze various key- |  |  |  |  |  |  |
| mapping or inferred mapping steps. During fuzzing, AHA-Fuzz ran- | value code usage patterns on a total of 405 apps, including all 105 |  |  |  |  |  |  |
| domly selects an offset from the candidate set for each unresolved | malware samples summarized by Cao et al. [12] and the top 300 most |  |  |  |  |  |  |
| field to simulate various object layouts. | downloaded benign apps from the Google Play Store as of October |  |  |  |  |  |  |
| We note that recovering Java object layouts is challenging when | 1, 2024. Our analysis find that, in most cases, extras values are |  |  |  |  |  |  |
| direct and inference mapping do not occur frequently enough. How- | used in comparison operations, which then trigger the execution |  |  |  |  |  |  |
| ever, we find that sufficient mapping occurs in most classes. This is | of additional code or events. More specifically, all extra values |  |  |  |  |  |  |
| mainly because most classes contain getter/setter methods, which | used in the malware samples are detected by checking comparison |  |  |  |  |  |  |
| introduce conflicts and enable offset retrieval without explicit in- | operations. In the 300 most downloaded apps, we identify 6,106 |  |  |  |  |  |  |
| ference. As shown in Table 3, according to our analysis on all 2 | , | 541 | unique intents using String extras, 67% (4,076 cases) of which are |  |  |  |  |
| classes within the Android framework module that define Intent- | detectable through comparison operations. The remaining 33% are |  |  |  |  |  |  |
| related classes, we find that 42.2% of cases involve direct mapping | used purely for data transmission, not directly contributing to new |  |  |  |  |  |  |
| (Case 1), generating conflict. Consequently, this allowed us to accu- | code/event execution. Consequently, we find patterns that most |  |  |  |  |  |  |
| rately infer offsets for another 40.6% of cases (Case 2). Relatively, | values are checked through comparison operations ( | e | . | g | ., | equals() |  |
| only a small portion—17.2% of fields—cannot be precisely resolved | or | contains() | ). Therefore, AHA-Fuzz hooks comparison operations |  |  |  |  |
| to a fixed offset. However, even for these, AHA-Fuzz continues | through eBPF, extracting values used in comparisons as candidate |  |  |  |  |  |  |
| fuzzing by randomly selecting offsets from the candidate set to | values, and sends them to the fuzzer through key-value feedback |  |  |  |  |  |  |
| simulate various potential layouts of the intent object. | messages. |  |  |  |  |  |  |

---

## Page 7

| Intent-aware Fuzzing for Android Hardened Application | CCS ’25, October 13–17, 2025, Taipei, Taiwan |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Object Layout | IntentFilter | ArrayList | String | Table 4: Type ratio analysis of extras values used in 300 most down- |  |  |  |
| … | … | … | loaded apps. |  |  |  |  |
| intentfilter = new | IntentFilter | (“SMS”); | #8 | mActions | … | #8 | count |
| registerReceiver (receiver, intentfilter); | #12 |  |  |  |  |  |  |
| … | element | #12 |  |  |  |  |  |
| Data | hash | Type category (#) | Mutation Strategy | # of unique extras values (%) |  |  |  |
| … | #16 | #16 |  |  |  |  |  |
| size | ”SMS” | action | Primitive (8) | AFL-based | 9,317 | (44.2%) |  |
| 1. private void onReceive( Context context, Intent intent ) { | Iteration | String (1) | Key-Value feedback | 10,395 | (49.3%) |  |  |
| Dynamically | 2. | String payload = intent.getStringExtra | (“msg”); | Special (5) | Invoke constructor | 1,369 | (6.5%) |
| register | 3. | if ( payload != null ) { |  |  |  |  |  |
| Intent event | 4. | if (payload.contains | (“LEAK”) { | Total (14) | - | 21,081 | (100%) |

1

| 5. | Call_Malicious(intent); | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6. | }}} | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Iteration 1 | Iteration 2 | Iteration 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| action : “SMS” | action : “SMS” |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Input | action : “ | SMS | ” | extras : {“ | msg | ”: “ | tmp | ”} | extras : {“ | msg | ”: “ | LEAK | ”} | 4.3 | Coverage Feedback Generator |
| Observed | Although all existing intent fuzzers are blackbox-based fuzzers, cov- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| getStringExtra | (“ | msg | ”) | payload.contains(“ | LEAK | ”) | Call_Malicious(intent) |  |  |  |  |  |  |  |  |
| Method | erage feedback on how many/new methods are triggered through |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

extras : {“ msg ”: “ tmp ”} payload.contains(“ LEAK ”)

| Feedback | In Call_Malicious().. | generated intents enables more efficient input generation. For ex- |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Generation | Generate random Str | “ | tmp | ” | Mutate until coverage | ample, Figure 3 shows that key-value feedback can further trigger |
| Find Candidate | growth stops |  |  |  |  |  |

possible execution flow paths, but it requires several iteration steps.

Figure 3: AHA-Fuzz’s Key-Value Information Extraction Examples.

Without coverage feedback, the fuzzer cannot estimate whether

further iteration are necessary or if the current input is sufficient.

For this reason, AHA-Fuzz, as the first intent fuzzer, introduces

| Figure 3 shows how AHA-Fuzz extracts key and value set through | coverage feedback to evaluate the quality of each generated intent. |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| API hooking and key-value feedback. AHA-Fuzz starts fuzzing with | Additionally, coverage feedback may include irrelevant information, |  |  |  |  |
| an intent ( | e | . | g | ., “SMS”) as an initial seed that does not include key- | such as GUI events, which can negatively impact intent fuzzing. |
| value information. Note that AHA-Fuzz obtains the initial seed | To address this issue, we propose a selective coverage feedback ap- |  |  |  |  |
| by analyzing the object layout of | IntentFilter | , which is used to | proach that detects and ignores such noise, enabling more accurate |  |  |
| register the intent event dynamically. Since AHA-Fuzz hooks all | utilization of feedback messages. |  |  |  |  |

extra-related getter functions, including getStringExtra() , to ex-

| tract key values, AHA-Fuzz can capture the “msg” key from the | 4.3.1 | Coverage Instrumentation. | AHA-Fuzz, based on eBPF, utilizes |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| getStringExtra() function (line 2). This allows AHA-Fuzz to create a | method-level coverage feedback. eBPF observes methods through |  |  |  |  |  |  |
| key-value feedback message that specifies the intent parameter and | probes that require the target code address, which can be obtained |  |  |  |  |  |  |
| requires “msg” as a key. However, | getStringExtra() | returns | null | from AOT-compiled code. Therefore, using eBPF, we can monitor |  |  |  |
| at line 2 because the initial intent does not have a key ( | e | . | g | ., “msg”). | which methods are executed within AOT-compiled code due to |  |  |
| Next, AHA-Fuzz sends a new intent that has “msg” as the key | intents. However, it is difficult to obtain address information for |  |  |  |  |  |  |
| and a random string as the value. Thus, the executed intent triggers | eBPF hooking in JIT-compiled code and the interpreter. For this, we |  |  |  |  |  |  |
| lines 2 | − | 4. In this second fuzzing attempt, AHA-Fuzz fails to visit | disable JIT-compiled code execution (will be handled as interpreter |  |  |  |  |
| line 5 because this basic block requires a specific value ( | i | . | e | ., “LEAK”) | code) through simple option change, without modifying the system, |  |  |
| in the intent parameter. Since AHA-Fuzz hooks comparison-related | but still cannot disable interpreter code. |  |  |  |  |  |  |
| APIs including | contains() | , AHA-Fuzz can obtain an additional | Note that interpreter code is not compiled and is executed at |  |  |  |  |
| candidate value “LEAK”. In the next fuzzing attempts, AHA-Fuzz | runtime via the interpreter, making it challenging to attach eBPF |  |  |  |  |  |  |
| eventually visits line 5 utilizing an intent that includes the needed | probes. To address this, we attach probes to the interpreter engine |  |  |  |  |  |  |
| key-value information. | that executes the interpreter code to observe its execution using |  |  |  |  |  |  |
| Mutation Strategy. | AHA-Fuzz applies different mutation strate- | eBPF. For this, we analyze the interpreter engine in ART and iden- |  |  |  |  |  |
| gies to the values of extras, depending on their type: primitive, | tify three general interpreter execution patterns as follows. First, |  |  |  |  |  |  |
| string, and Java object types ( | e | . | g | ., | Binder | ), which we refer to as | each entry point of interpreter execution requires the following pa- |
| special types. For Java primitive types, AHA-Fuzz utilizes AFL-style | rameters to obtain the program’s current state: | ArtMethod | , | Thread | , |  |  |
| mutations, including random bit flips. String values are mutated | and stack frame objects. Second, ART updates the ’hotness’ counter, |  |  |  |  |  |  |
| using our key-value feedback (Section 4.2.2) algorithm. Mutating | which is used in JIT-compiled code, before executing interpreter |  |  |  |  |  |  |
| special types is challenging because their object layouts differ across | code. Third, ART uses architecture-specific assembly code within |  |  |  |  |  |  |
| apps. Currently, AHA-Fuzz supports special type mutation only | its core interpreter mechanism to optimize performance. |  |  |  |  |  |  |
| through constructor invocation, and we leave this implementation | Based on these observations, we leverage CodeQL [20] to iden- |  |  |  |  |  |  |
| improvement ( | e | . | g | ., recovering specific special type layout using our | tify the entry point of the interpreter. Note that with CodeQL, code |  |  |
| Java object layout recovery Algorithm 1) as future work (see Sec- | ( | e | . | g | ., Android code) is transformed into a database, enabling in- |  |  |
| tion 8). We also note that string objects are more commonly used | depth analysis through custom queries ( | e | . | g | ., three defined patterns). |  |  |
| as values, whereas special types are relatively rare. Table 4 shows | Additionally, to evaluate whether the method of identifying inter- |  |  |  |  |  |  |
| the analysis of extras value types used in the 300 most downloaded | preter entry points using CodeQL and the three identified patterns |  |  |  |  |  |  |
| apps from Google Play. According to this analysis, string objects | is valid across different Android versions, we test Android versions |  |  |  |  |  |  |
| account for 49.5% and primitive types for 44.2%, while special types | from the past five years ( | i | . | e | ., since 2019) and find that all possible |  |  |
| comprise only 6.5% of all extra values. | interpreter entry points are identified through our three patterns. |  |  |  |  |  |  |

---

## Page 8

| CCS ’25, October 13–17, 2025, Taipei, Taiwan | Seongyun Jeong et al. |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Intent Event Execution Flow | overhead). By addressing these primary challenges, such as de- |  |  |  |  |
| Activity | MessageQueue | dispatchMessage() | Intent Event | dispatchMessage() | tecting scheduled malware and efficiently identifying information |
| Called | returned | leaks, we further enhance AHA-Fuzz’s bug detection capability. |  |  |  |

Service ActivityManager handleServiceArgs() Intent Event handleServiceArgs()

Called

returned

Broadcast ActivityManager handleReceiver() Intent Event handleReceiver()

Called

returned

Start Observing End Observing

Figure 4: Overview of Intent Event Execution Flows.

events include GUI events and background events that are exe-

(for Activities) or the ActivityManager (for Services and Broadcast

4.4.1 Scheduler Manipulation. Scheduling events in dynamic anal-

ysis reduces fuzzing effectiveness. For example, an Android app can

execute code at a point in time one day after installation through a

scheduling event. Additionally, some malware leverages the sched-

uler to enable periodic activation and deactivation, helping it evade

detection. More specifically, by avoiding continuous activation, the

cause system instability [11].

in Section 4.2.1.

detection approaches [18, 59, 62, 64], sensitive information is typi-

| 4.3.2 | Selective Coverage Feedback. | Coverage feedback can be gen- | malware only operates when necessary, reducing its chances of be- |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| erated by monitoring all methods; however, observing every method | ing detected. A straightforward solution is to modify the application |  |  |  |  |  |  |  |  |
| may lead to noisy feedback from events unrelated to intents, neg- | or system code to fast-forward the scheduling time, but identifying |  |  |  |  |  |  |  |  |
| atively impacting intent fuzzing. For example, specific Android | scheduling time under hardening techniques is challenging and can |  |  |  |  |  |  |  |  |
| cuted by service components, and these unrelated events can also | To address these issues, we utilize eBPF to hook scheduler-related |  |  |  |  |  |  |  |  |
| generate coverage feedback that negatively affects intent fuzzing. | functions and adjust the associated scheduling times. More specif- |  |  |  |  |  |  |  |  |
| To address this problem, one is willing to wait until the app is | ically, we manipulate the scheduling event to occur quickly by |  |  |  |  |  |  |  |  |
| idle after sending the intent without delivering any events. Yet, this | overwriting the scheduling time stored in memory ( | e | . | g | ., adjusting |  |  |  |  |
| method is not only time-consuming but also, given the event-driven | 12 hours to 10 minutes). In particular, we focus on a scheduling |  |  |  |  |  |  |  |  |
| nature of Android apps, background tasks may cause the apps to | event registered by Android framework APIs ( | e | . | g | ., | AlarmManager | , |  |  |
| exit this idle state unexpectedly. Therefore, we need to distinguish | JobScheduler | , or | WorkManager | ). For scheduling events requiring |  |  |  |  |  |
| between events caused by AHA-Fuzz’s intent fuzzing and other | long waiting time ( | e | . | g | ., several hours), we leverage a helper func- |  |  |  |  |
| Android events caused by GUI fuzzing. | tion ‘ | bpf_probe_write_user() | ’ in eBPF to decrease the waiting |  |  |  |  |  |  |
| Analyzing Events Invoked by Intents. | To distinguish events | time stored in user space memory. For this, we insert an eBPF |  |  |  |  |  |  |  |
| generated by intents, understanding the execution path of events | program into the return statement of the scheduling time setter |  |  |  |  |  |  |  |  |
| via intents in Android is important. As shown in Figure 4, intents | method, enabling manipulation of the scheduling time for faster in- |  |  |  |  |  |  |  |  |
| can be delivered to three main components: Activities, Services, and | vocation. Note that scheduling APIs are well-documented [27], and |  |  |  |  |  |  |  |  |
| Broadcast Receivers. These intents pass through the | MessageQueue | we can retrieve the value of the scheduling time value as described |  |  |  |  |  |  |  |
| Receivers) and corresponding events are executed via predefined | 4.4.2 | Detecting Information Leak. | Both benign and malware apps |  |  |  |  |  |  |
| methods ( | e | . | g | ., dispatchMessage() for Activities). Based on these | can leak users’ sensitive usage data ( | e | . | g | ., locations or contacts) |
| patterns, we can track the start ( | e | . | g | ., | dispatchMessage() | ) and end | without informing the user or obtaining consent. To detect such |  |  |
| ( | e | . | g | ., | dispatchMessage() returned | ) of these methods using eBPF, | information leaks, existing approaches [3, 7, 18, 59, 62, 64] con- |  |  |
| focusing only on events occurring during the method’s execution. | duct static/dynamic taint analysis to track source APIs ( | e | . | g | ., return |  |  |  |  |
| This helps mitigate the noise issue described earlier. Furthermore, | sensitive data) to sink APIs ( | e | . | g | ., potential leak sites). However, ex- |  |  |  |  |
| we validate the consistency of these patterns across Android version | isting approaches are not directly applicable to hardened apps. More |  |  |  |  |  |  |  |  |
| updates by formalizing them and checking them using CodeQL. | specifically, propagating taint at the instruction level during run- |  |  |  |  |  |  |  |  |
| Consequently, we find that this pattern has remained consistent | time requires modifying the application to statically instrument the |  |  |  |  |  |  |  |  |
| over the past five years of Android version updates ( | i | . | e | ., since 2019), | app code [3, 7, 59], which not only necessitates bypassing integrity |  |  |  |  |
| ensuring the ongoing effectiveness of this approach. | checks but also provides limited support for dynamically loaded |  |  |  |  |  |  |  |  |
| Execution Balancing Between GUI and Intent Fuzzers. | By | code, as discussed in Section 2.3. Moreover, starting with Android |  |  |  |  |  |  |  |
| identifying events triggered by intents and further distinguishing | 7, the presence of diverse execution models—AOT-compiled, JIT- |  |  |  |  |  |  |  |  |
| GUI events occurring on the main UI thread, the impact of inputs | compiled, and interpreted code [33]—has limited the effectiveness |  |  |  |  |  |  |  |  |
| generated by each GUI and intent fuzzer can be evaluated. Initially, | of existing taint analysis approaches that rely on system modifica- |  |  |  |  |  |  |  |  |
| the GUI and intent fuzzers are executed at an equal 1:1 ratio to | tion [18] or DBI [62, 64], as these approaches typically support only |  |  |  |  |  |  |  |  |
| ensure fairness. However, AHA-Fuzz dynamically adjusts the exe- | a subset of execution modes ( | e | . | g | ., DBI-based tool named Malton [64] |  |  |  |  |
| cution ratio of each fuzzer based on the observed impact of their | can track taint only in AOT-compiled code). |  |  |  |  |  |  |  |  |
| generated inputs. For example, if an app generates a higher propor- | To address these issues, AHA-Fuzz conducts a lightweight method- |  |  |  |  |  |  |  |  |
| tion of events through intents compared to GUI interactions, the | level taint propagation analysis instead of instruction-level taint |  |  |  |  |  |  |  |  |
| execution ratio of the intent fuzzer is increased accordingly. | propagation. As commonly mentioned in existing information leak |  |  |  |  |  |  |  |  |
| 4.4 | Bug Detection Capability Enhancer | cally stored and managed as primitive types, such as int or String |  |  |  |  |  |  |  |
| Although AHA-Fuzz generates various intents using AHA-Fuzz’s | objects. For example, important network information ( | e | . | g | ., SSID) to |  |  |  |  |
| key-values and coverage feedback, it may still miss some bugs trig- | be protected is generally stored as a String object. To monitor these |  |  |  |  |  |  |  |  |
| gered under specific conditions ( | e | . | g | ., scheduled malware) or fail to | sensitive information flows, AHA-Fuzz leverages eBPF to monitor |  |  |  |  |
| detect triggered bugs ( | e | . | g | ., information leak due to performance | APIs that process these primitive values, such as methods in the |  |  |  |  |

---

## Page 9

Intent-aware Fuzzing for Android Hardened Application CCS ’25, October 13–17, 2025, Taipei, Taiwan

| Integrity | Instrument |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Application | Hardened | Dynamically |  |  |  |  |  |
| Modification | DEX Code | loaded code |  |  |  |  |  |
| int getCid() | { | String toString( | int | ){ | void write( | String | ) { |
| } | } |  |  |  |  |  |  |

detected

Taint : Cid Taint : Cid, Str Taint : Cid, Str

Figure 5: Overview of method-level taint propagation.

Java standard library. Specifically, by tracking sensitive primitive

values as they pass through API parameters (inputs) and return

level. Method-level propagation tracks primitive type values and

string values passed through framework APIs, enabling the tracing

tect information leaks in recent Android apps. To detect information

leaks through taint analysis, recent research [14, 37, 69, 71] mainly

relies on the source and sink API set defined by FlowDroid [5]. How-

ever, we observe that FlowDroid’s API set does not include some

APIs introduced in the last five years of Android releases. To detect

particularly discussions of potential security and privacy issues, to

We adapt the BPF Compiler Collection (BCC) framework [44] to

create an eBPF analysis environment. We also integrate AHA-Fuzz

with an existing GUI-based fuzzing framework [36] to compare its

effectiveness. Our implementation consists of Python for the BCC

framework, Java for intent fuzzing, and C for eBPF programs. The

total lines of code (LoC) are around 3 , 000.

eBPF Environment. The eBPF feature supported by the Linux

kernel can be used in Android kernels based on Linux systems

without any modifications. However, it does not provide a user-

friendly environment because most of the documentation for the

eBPF toolchain assumes standard Linux instead of Android. We

utilize scripts provided by the Extended Android Tools [19] to

fied in Section 4.3.1 and extract the DEX method index contained

is called. To monitor only the targeted app’s calls, we filter each

app process through a unique UID using eBPF.

plemented on top of Android’s default GUI fuzzer (Monkey [30]).

We implement AHA-Fuzz’s intent fuzzing on top of APE, and it

operates separately from the APE fuzzer. Thus, AHA-Fuzz’s intent

fuzzing can run with other GUI fuzzers.

6 Evaluation

following research questions.

RQ4 Can AHA-Fuzz discover previously unknown bugs that pre-

vious works cannot find? (Section 6.5)

6.1 Evaluation Setup

and 8 GB of RAM.

given that 76 . 2% of malware uses intents to hide malicious behavior

malicious behaviors in malware as the metric for evaluating fuzzers.

We also use the Google Play store malware dataset provided by

Cao et al. [12]. In particular, this dataset identifies 105 different

malware families and creates one report per family. We thus select

a total of the 105 malware that has the report from the dataset. The

report describes preconditions for triggering malicious behaviors.

For instance, preconditions include payload ( e . g ., a key-value pair

{ status: StartAdService }) for intent events or scheduling events

that malware abuse. We use such events required to trigger mali-

cious behaviors to evaluate whether AHA-Fuzz can trigger them.

Furthermore, among the Android malware, we select 14 out of the

105 apps satisfying the following criteria:

| Check | Failure | interpreter execution, we hook the interpreter entry points identi- |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Application | in the | ArtMethod | structure through eBPF to monitor which method |  |  |  |  |  |  |  |
| Source | Propagation | Sink | Fuzzing Environment. | We note that AHA-Fuzz performs GUI |  |  |  |  |  |  |
| Framework | ... | return | Cid | ... | return | Str | … | // | Sink | fuzzing and intent fuzzing simultaneously. For GUI fuzzing, we |
| Output | Input | Output | } | Input | Leak | select APE [36] because it shows the best performance and is im- |  |  |  |  |
| values (outputs), AHA-Fuzz can detect potential information leaks. | We evaluate AHA-Fuzz’s effectiveness in analyzing hardened apps. |  |  |  |  |  |  |  |  |  |
| Figure 5 shows how taint propagation is performed at the method- | Specifically, we present our evaluation results by addressing the |  |  |  |  |  |  |  |  |  |
| of data flows from sources ( | getCid | ) to sinks ( | write | ). AHA-Fuzz | RQ1 | Is AHA-Fuzz capable of creating valid intents ( | i | . | e | ., an intent |
| utilizes eBPF to hook each API call ( | toString | ), including both its | requiring specific extras) called by malware? (Section 6.2) |  |  |  |  |  |  |  |
| entry and return points, to track input parameters and output re- | RQ2 | How does AHA-Fuzz’s fuzzing algorithm (key-value feed- |  |  |  |  |  |  |  |  |
| turn values. Consequently, method-level taint analysis can detect | back and selective coverage feedback) affect the performance |  |  |  |  |  |  |  |  |  |
| information leaks when tainted values reach sink APIs—even for | of the fuzzing? (Section 6.3) |  |  |  |  |  |  |  |  |  |
| dynamically loaded code. | RQ3 | Does AHA-Fuzz guarantee increased coverage compared to |  |  |  |  |  |  |  |  |
| Furthermore, we identify additional possible source APIs to de- | previous works? (Section 6.4) |  |  |  |  |  |  |  |  |  |
| additional information leaks in recent apps, we manually review | We execute AHA-Fuzz on a machine running 64-bit MacOS Sonoma |  |  |  |  |  |  |  |  |  |
| the official Android documentation [31, 32] to identify newly in- | 14 | . | 4 | . | 1 (23E224) with a 24-core CPU (Apple M2 Ultra) and 192 GB of |  |  |  |  |  |
| troduced APIs. We also analyze the official documentation [34, 35], | RAM. We configure each emulator using Android 13 with 2 cores |  |  |  |  |  |  |  |  |  |
| identify additional possible information leak attack scenarios. As | Ground-truth Malware Dataset. | To evaluate the performance |  |  |  |  |  |  |  |  |
| a result, we extend the original FlowDroid API set by defining 14 | of intent fuzzers, measuring the number of triggered malicious |  |  |  |  |  |  |  |  |  |
| additional source APIs. | behaviors is more appropriate than simply counting code coverage, |  |  |  |  |  |  |  |  |  |
| 5 | Implementation | or initiate attacks [12]. Therefore, we use the number of triggered |  |  |  |  |  |  |  |  |
| leverage the BCC framework [44], through cross-compilation using | (1) The malware exploits an intent that requires key-value pairs |  |  |  |  |  |  |  |  |  |
| the Android native development kit [25]. | and/or a scheduling event to execute malicious behaviors. |  |  |  |  |  |  |  |  |  |
| To observe AOT-compiled code, we extract method addresses | (2) The malware can be run on a 64-bit ARM Android machine. |  |  |  |  |  |  |  |  |  |
| from OAT files using | oatdump | and hook them in the Zygote process | (3) We can reproduce malicious behaviors reported in study [12] |  |  |  |  |  |  |  |
| to monitor all subsequent app processes, similar to BPFroid [2]. For | ( | e | . | g | ., connecting command and control servers). |  |  |  |  |  |

*[Image: Page 9 Image]*

---

## Page 10

CCS ’25, October 13–17, 2025, Taipei, Taiwan Seongyun Jeong et al.

Table 5: Intent usage patterns on 14 malicious apps. ‘Improved’ column denotes improvements achieved by AHA-Fuzz in the terms of patterns

and times to find them, compared with the others. ✓ denotes patterns invoked by AHA-Fuzz. ✗ expresses that AHA-Fuzz fails to invoke the

patterns. ‘Time’ represents improved time to invoke a pattern compared with the most fast one that invokes the same pattern.

| Family | Patterns | APE | MATE | ICCBot | IntentFuzzer | AHA-Fuzz | Improved |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (sec) | (sec) | (sec) | (sec) | (sec) | Patterns | Time (X) | Pattern Details |  |  |  |  |  |
| AceCard | M | - | 235 | 108 | 115 | 88 | - | 1 | . | 23 | × |  |
| E | - | - | - | - | 89 | ✓ | - | E : | SMS | , | Payload |  |
| AgentBKY | E | - | - | - | - | 30 | ✓ | - | E : | SMS |  |  |
| E | - | - | 121 | 136 | 89 | - | 1 | . | 36 | × | E : Google Firebase |  |
| Bahamut | M | - | 1,251 | 647 | 829 | 38 | - | 17 | . | 03 | × | M : Multiple Entrypoints |
| E | - | - | - | - | 44 | ✓ | - | E : | SMS |  |  |  |
| ClickerGenG | M | - | 283 | 171 | 140 | 74 | - | 1 | . | 89 | × |  |
| S | - | - | - | - | 741 | ✓ | - | S : Run After 6 hours |  |  |  |  |
| HiddenAdOS | M | - | 643 | 322 | 464 | 86 | - | 3 | . | 74 | × |  |
| E | - | - | 279 | 501 | 172 | - | 1 | . | 61 | × | E : Google Firebase |  |
| IndexY | E | - | - | - | - | 55 | ✓ | - | E : | SMS | , Multiple Entrypoints |  |
| M | - | 192 | 44 | 50 | 35 | - | 1 | . | 26 | × |  |  |
| ProjectSpyHRX | E | - | - | - | - | 30 | ✓ | - | E : | SMS |  |  |

E : Malware developer defined

| E | - | - | - | - | - | ✗ | - |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M | - | 281 | 141 | 101 | 32 | - | 3 | . | 15 | × |  |  |
| Reputation1_2019 | M | - | 306 | 87 | 128 | 42 | - | 3 | . | 05 | × | E : Dynamically registered, developer defined |
| E | - | - | 201 | 133 | 43 | - | 3 | . | 09 | × |  |  |
| SMSAndroidOSWesp | E | - | - | - | - | 52 | ✓ | - | E : | SMS | , | Payload |
| Solid | M | - | 174 | 61 | 55 | 50 | - | 1 | . | 1 | × |  |
| E | - | - | - | - | 393 | ✓ | - | E : | Payload | , Google Firebase |  |  |
| Sonyvpay | M | - | 420 | 112 | 128 | 33 | - | 3 | . | 40 | × |  |
| E | - | - | - | - | 40 | ✓ | - | E : | SMS | , | Payload |  |
| SpyBankerHU | M | - | 301 | 104 | 114 | 31 | - | 3 | . | 35 | × |  |
| E | - | - | - | - | 43 | ✓ | - | E : | SMS |  |  |  |
| TrojanDropperAgentCIQ | S | - | - | - | - | 1,394 | ✓ | - | S : Run after 24 hours |  |  |  |
| M | - | 362 | 98 | 109 | 32 | - | 3 | . | 06 | × |  |  |
| Vilny | M | - | 265 | 104 | 99 | 33 | - | - | S : Run after 26 hours |  |  |  |
| S | - | - | - | - | 156 | ✓ | - |  |  |  |  |  |
| Total (%) | 0/28 | 11/28 | 15/28 | 15/28 | 27/28 |  |  |  |  |  |  |  |
| (0.0%) | (39.3%) | (53.4%) | (53.4%) | (96.4%) | 92.3% | 3 | . | 45 | × |  |  |  |
| We confirm that: ( | 𝑖 | ) 45 out of 105 apps require key-value pairs, | (7) | ICCBot | : It is an intent fuzzer based on inter-procedural anal- |  |  |  |  |  |  |  |
| and/or abuse the scheduling API; ( | 𝑖𝑖 | ) 38 out of 45 apps are compati- | ysis. We note that Sasnauskas et al. [57] proposed an intent |  |  |  |  |  |  |  |  |  |
| ble with 64-bit ARM Android machines; and ( | 𝑖𝑖𝑖 | ) we successfully | fuzzing based on inter-procedural static analysis. However the |  |  |  |  |  |  |  |  |  |
| reproduced malware behaviors in 14 out of these 38 apps. | source code is no longer available. We, thus, implemented inter- |  |  |  |  |  |  |  |  |  |  |  |
| Benign App Dataset. | We evaluate AHA-Fuzz’s performance on | procedural intent fuzzer with ICCBot [65] that leverages key- |  |  |  |  |  |  |  |  |  |  |
| benign apps and find previously unknown bugs that prior works | value pairs extracted by using inter-procedural static analysis. |  |  |  |  |  |  |  |  |  |  |  |
| are hard to find. To this end, we collected the most downloaded 300 | (8) | ICCBot-AHA | : It does not perform the inter-procedural static |  |  |  |  |  |  |  |  |  |
| apps from the Google Play Store on October 1, 2024. | analysis. Also, it uses AHA-Fuzz’s intent fuzzing algorithm. |  |  |  |  |  |  |  |  |  |  |  |
| Malware Dataset. | This dataset is intended to evaluate AHA-Fuzz’s | (9) | IntentFuzzer | [67]: It is an intent fuzzing approach based on |  |  |  |  |  |  |  |  |
| performance on real-world Android malware. Since finding mal- | a hybrid method. IntentFuzzer leverages runtime feedback to |  |  |  |  |  |  |  |  |  |  |  |
| ware directly from the Google Play Store is challenging, among the | obtain the | key | and intra-procedural static analysis to retrieve |  |  |  |  |  |  |  |  |  |
| 2 | , | 230 malware samples available in AndroZoo from January 1, 2023 | the corresponding | value | . IntentFuzzer performs fuzzing only on |  |  |  |  |  |  |  |
| to August 1, 2024, we identify the top 20 most downloaded apps on | service and broadcast components. Because it is a closed-source |  |  |  |  |  |  |  |  |  |  |  |
| the Google Play, which are also uploaded there, as our target apps. | project, we implemented it based on the paper and adapted it to |  |  |  |  |  |  |  |  |  |  |  |
| Evaluation Baselines. | To evaluate the effectiveness of AHA-Fuzz’s | an eBPF-based environment to extract key-value pairs. |  |  |  |  |  |  |  |  |  |  |
| fuzzing algorithms, we create the following four different baselines | (10) | IntentFuzzer-AHA | : It is a variant version of IntentFuzzer that |  |  |  |  |  |  |  |  |  |
| and six variant modes: | leverages AHA-Fuzz’s intent fuzzing algorithm. |  |  |  |  |  |  |  |  |  |  |  |

(1) APE [36]: It runs only GUI fuzzing. Hence, it does not perform

intent fuzzing. We use APE’s default configurations.

| (2) | AHA-Fuzz | : As a default mode, we use AHA-Fuzz with APE. | 6.2 | Effectiveness of Intent Fuzzing |  |
| --- | --- | --- | --- | --- | --- |
| (3) | AHA-KV | : It is a variant version of AHA-Fuzz. It only uses the | To answer | RQ1 | (“Is AHA-Fuzz capable of creating valid intents |
| key-value feedback (Section 4.2) from AHA-Fuzz’s algorithm. | called by malware?”), we run AHA-Fuzz and four different fuzzers— |  |  |  |  |
| (4) | AHA-CV | : It only leverages the coverage (Section 4.3.1) and | APE, MATE, ICCBot, and IntentFuzzer—on the Ground-truth Mal- |  |  |
| key-value feedback (Section 4.2) from AHA-Fuzz’s algorithm. | ware Dataset. Table 5 shows the evaluation results. It shows intent |  |  |  |  |
| (5) | MATE | [6]: It performs GUI fuzzing as well as intent fuzzing | usage patterns per the malware family, along with the time spent |  |  |
| based on intra-procedural static analysis results. We note that | to invoke these patterns and their descriptions. Regarding the pat- |  |  |  |  |
| MATE requires modifications of apps to enable the debug mode. | terns, “M” denotes intent events that do not require key-value pairs |  |  |  |  |
| (6) | MATE-AHA | : It is a variant version of MATE that uses MATE’s | in extras, while “E” indicates intent events that require extras. “S” |  |  |
| GUI fuzzing and AHA-Fuzz’s intent fuzzing algorithm. | represents long-term scheduling events. |  |  |  |  |

---

## Page 11

| Intent-aware Fuzzing for Android Hardened Application | CCS ’25, October 13–17, 2025, Taipei, Taiwan |  |  |
| --- | --- | --- | --- |
| 1 | // ProjectSpyHRX | Table 6: Ablation Study Results. Improve(%) indicates the perfor- |  |
| 2 | public void | onReceive(Context context, Intent intent) { | mance improvement rate compared to the previous mode |

| 3 | String target = intent.getStringExtra("package"); |  |
| --- | --- | --- |
| 5 | if | (hashed_target == 7696199939) { |
| 6 | target = "com.whatsapp"; |  |

9 }

We check whether intents generated by the fuzzers invoke the

patterns. We confirm that AHA-Fuzz successfully invokes 27 out of

the 28 patterns. However, APE fails to trigger any patterns when it

performs GUI fuzzing only. MATE, ICCBot, and IntentFuzzer suc-

ceed in triggering patterns that do not require extras values, but fail

to trigger patterns that require scheduling and extras. On the con-

trary, AHA-Fuzz triggers all intent usage patterns and scheduling

events, except for one pattern that requires extras.

Payload. A payload case refers to a scenario where malware lever-

ages the extras field of an intent to deliver a payload. For instance,

Solid malware uses a Google Firebase intent to send a payload

to victims. The malicious behavior is triggered only when the

Firebase message contains a certain key-value payload ( status :

requires a value of 3gpp through the key-value feedback.

Time-to-exposure. AHA-Fuzz is approximately three times faster

than previous methods in triggering patterns. We note that sim-

AHA-CV 27 124 (17.7%)

In contrast, all other fuzzers randomly select intents, which signifi-

cantly reduces the likelihood of triggering intent events that lead

to malicious behavior.

Failure Case. AHA-Fuzz fails to invoke 1 out of the 28 patterns

in the ProjectSpyHRX malware family. Figure 6 illustrates a failure

case where the malware receives a payload through an intent and

initiates malicious activities by comparing the hash values of the

payload (at Line 5). To pass the hash comparison, the correct pre-

hash value is required. However, AHA-Fuzz’s feedback messages

provide the post-hash value, causing AHA-Fuzz to fail in generating

the appropriate feedback value for the intent parameter. In addition,

generating the pre-hash value is not possible with static analysis,

as it also requires hash guessing.

6.3 Ablation Study

formance.

6.4 Code Coverage

| 4 | int | hashed_target = target.hashCode(); | Fuzzer | # of invoked pattern | Avg. TTE (Improve(%)) |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | Do_malicious(target); | IntentFuzzer | 15 | 206 |  |  |  |  |  |  |
| 8 | } | AHA-KV | 27 | 146 (41.1%) |  |  |  |  |  |  |
| Figure 6: AHA-Fuzz’s Failure Pattern on ProjectSpyHRX. | AHA-Fuzz | 27 | 66 (87.9%) |  |  |  |  |  |  |  |
| StartAdService | ) within an intent. In our evaluation, all baseline | We present an ablation study conducted to assess the contributions |  |  |  |  |  |  |  |  |
| fuzzers—APE, MATE, ICCBot, and IntentFuzzer—fail to extract the | of two types of feedback in AHA-Fuzz—key-value feedback and |  |  |  |  |  |  |  |  |  |
| proper payload triggering a malicious behavior. They use static | selective coverage feedback—to its overall fuzzing performance. To |  |  |  |  |  |  |  |  |  |
| analysis to extract values from extras, but fail to identify the spe- | this end, we compare four fuzzers: IntentFuzzer, which receives |  |  |  |  |  |  |  |  |  |
| cific payload used by the malware. This is because there are no | the key values of the extras field as runtime feedback, along with |  |  |  |  |  |  |  |  |  |
| predefined patterns or APIs to retrieve values from intents, making | AHA-Fuzz and its two variant modes—AHA-KV and AHA-CV. We |  |  |  |  |  |  |  |  |  |
| it impossible to generate the correct payload through static analysis | measure the time spent calling 28 intent usage patterns (as in Sec- |  |  |  |  |  |  |  |  |  |
| alone. Baseline fuzzers typically extract payload values by collecting | tion 6.2) and the number of invoked usage patterns. |  |  |  |  |  |  |  |  |  |
| constant values ( | e | . | g | ., predefined strings). However, app hardening | AHA-KV invokes an additional 12 patterns that IntentFuzzer |  |  |  |  |  |
| techniques, such as obfuscation, can hinder the extraction of these | does not trigger, and its invocation speed improves 41 | . | 1%, as shown |  |  |  |  |  |  |  |
| payload-related values. On the other hand, AHA-Fuzz successfully | in Table 6. This result demonstrates that our key-value feedback |  |  |  |  |  |  |  |  |  |
| generates the required payload values through the runtime analysis | mechanism can generate payloads to invoke new intent usage pat- |  |  |  |  |  |  |  |  |  |
| based on compare operations. Therefore, AHA-Fuzz successfully | terns, thereby reducing the time required to trigger new patterns. |  |  |  |  |  |  |  |  |  |
| invokes four patterns (as in Table 5) that require specific payloads. | AHA-CV further improves performance over AHA-KV by incorpo- |  |  |  |  |  |  |  |  |  |
| SMS. | SMS-related intents ( | e | . | g | ., | SMS_RECEIVED | ) require a specific | rating additional coverage feedback, resulting in a 17 | . | 7% increase in |
| key-value pair such as | {format, 3gpp} | . While the baseline fuzzers | call speed compared to AHA-KV. Lastly, AHA-Fuzz achieves a 87 | . | 9% |  |  |  |  |  |
| notice that the | format | key is needed, they fail to extract proper | faster call speed compared to AHA-CV, which utilizes non-selective |  |  |  |  |  |  |  |
| values ( | e | . | g | ., | 3gpp | ). This is because the Android framework, rather | coverage feedback. The performance improvement of AHA-Fuzz |  |  |  |
| than the application, is responsible for checking the values in in- | demonstrates that our selective coverage feedback enhances the |  |  |  |  |  |  |  |  |  |
| tents. Therefore, extracting such proper values requires not only | efficiency of intent fuzzing. Our ablation study results demonstrate |  |  |  |  |  |  |  |  |  |
| analyzing the application code but also analyzing the framework | that coverage feedback, which measures all Android events, in- |  |  |  |  |  |  |  |  |  |
| code, which is a challenging problem due to the complexity and of | cluding GUI interactions and intents, can negatively impact the |  |  |  |  |  |  |  |  |  |
| the framework. On the other hand, AHA-Fuzz monitors all Android | performance of intent fuzzing. In contrast, our selective coverage |  |  |  |  |  |  |  |  |  |
| events, including those involving the Android framework. AHA- | feedback focuses exclusively on tracking intent events, effectively |  |  |  |  |  |  |  |  |  |
| Fuzz, thus, can extract the necessary information that | format | key | reducing noise from unrelated events and improving fuzzing per- |  |  |  |  |  |  |  |
| ply invoking an intent event does not directly lead to malware’s | We measure method-level code coverage ( | i | . | e | ., the number of exe- |  |  |  |  |  |
| malicious behaviors. The internal state of the malware, including | cuted methods) to compare AHA-Fuzz with previous works ( | RQ3 | ). |  |  |  |  |  |  |  |
| global variables, also affects the execution of malicious behaviors. | We note that the input spaces of each baseline fuzzer are different. |  |  |  |  |  |  |  |  |  |
| It highlights the importance of selecting the correct intent input. | Therefore, to ensure a fair comparison, we evaluate code coverage |  |  |  |  |  |  |  |  |  |
| We observe that our coverage-guided feedback enables AHA-Fuzz | of each baseline fuzzer and the variant versions of the baselines that |  |  |  |  |  |  |  |  |  |
| to select input seeds that are likely to trigger malicious behaviors. | use AHA-Fuzz’s intent fuzzing algorithm (Section 4.2, Section 4.3). |  |  |  |  |  |  |  |  |  |

---

## Page 12

CCS ’25, October 13–17, 2025, Taipei, Taiwan Seongyun Jeong et al.

Table 7: Measured method-level coverage on 40 apps. MATE can only successfully fuzz 11 benign apps out of 20 , and 0 malware apps out of 20 .

Triggered Method (Incre.(%))

Dataset

| Ape | AHA-Fuzz | MATE | MATE-AHA | ICCBot | ICCBot-AHA | IntentFuzzer | IntentFuzzer-AHA |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Benign (20) | 6,880 | 7,734 (12.4%) | 4,761 | 5,363 (12,7%) | 6,021 | 6,979 (15.9%) | 6,010 | 6,804 (13.2%) |  |  |  |  |
| Malware (20) | 5,110 | 5,470 (7.0%) | Failed | Failed | 3,006 | 3,988 (32.6%) | 2,360 | 3,565 (51.0%) |  |  |  |  |
| Total (Avg) | 5,995.1 | 6,602.1 | (10.1%) | 4,760.7 | 5,363.0 | (12.7%) | 4,513.7 | 5,483.3 | (21.5%) | 4,185.0 | 5,184.5 | (23.9%) |
| We use a total of 40 Android apps, including the most down- | intent-related information at runtime; thus, it is unaffected by pack- |  |  |  |  |  |  |  |  |  |  |  |
| loaded 20 apps from AndroZoo and the most downloaded 20 mal- | ers and obfuscators and yields better code coverage. |  |  |  |  |  |  |  |  |  |  |  |

ware. Although we do not intentionally select hardened apps, we

| observe that all 40 apps are hardened. Specifically, among the be- | 6.5 | Discovering Unknown Bugs |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nign apps, 7 out of 20 use obfuscation, and 17 out of 20 employ | We evaluate AHA-Fuzz’s effectiveness in discovering bugs that |  |  |  |  |  |  |  |
| anti-debugging techniques. Among the malware, 19 out of 20 apps | previous analysis tools cannot find ( | RQ4 | ). We run AHA-Fuzz for |  |  |  |  |  |
| use packers. We execute each fuzzer for one hour on each of the 40 | one hour on each of the 300 Top downloaded apps. AHA-Fuzz dis- |  |  |  |  |  |  |  |
| Android apps. | covers 26 crashes and 21 information leaks, and we report them |  |  |  |  |  |  |  |
| As a result, fuzzers that adopt AHA-Fuzz’s intent fuzzing algo- | to corresponding developers. At the time of writing, four informa- |  |  |  |  |  |  |  |
| rithm execute more methods than a baseline fuzzer, as shown in | tion leaks and two crashes have been confirmed. Additionally, two |  |  |  |  |  |  |  |
| Table 7. AHA-Fuzz calls 10 | . | 1% more methods than GUI fuzzing | information leaks have been fixed by Google and Firefox. |  |  |  |  |  |
| (APE), 21 | . | 5% more methods than the static analysis-based intent | Crash. | We select ICCBot and IntentFuzzer as comparison fuzzers |  |  |  |  |
| fuzzer ( | i | . | e | ., ICCBot), and 23 | . | 9% more methods than IntentFuzzer. | and verify the uniqueness of the crashes found by AHA-Fuzz by |  |
| APE. | AHA-Fuzz achieves the highest coverage among all the base- | checking whether the comparison fuzzer could detect them. We |  |  |  |  |  |  |
| lines and variant versions using AHA-Fuzz’s intent fuzzing algo- | exclude MATE from the comparison due to the difficulty in per- |  |  |  |  |  |  |  |
| rithm. Meanwhile, APE ( | i | . | e | ., GUI fuzzing only) achieves the best | forming reliable analysis, as explained in Section 6.4. As in previous |  |  |  |
| method-level coverage compared to other previous intent fuzzing | works, we only count crashes that lead to fatal errors ( | e | . | g | ., excluding |  |  |  |
| approaches. This result indicates that GUI events are crucial for | crashes caused by null intent fuzzing). To analyze the differences |  |  |  |  |  |  |  |
| analyzing Android app behaviors, and the inclusion of GUI fuzzing | caused by the intent fuzzing algorithm, we count only the crashes |  |  |  |  |  |  |  |
| in the AHA-Fuzz design is reasonable. | where the root cause is related to the intent. |  |  |  |  |  |  |  |
| In terms of code coverage, APE’s GUI fuzzing significantly en- | AHA-Fuzz discovers 26 crashes that other baseline fuzzers can- |  |  |  |  |  |  |  |
| hances app analysis. However, from the perspective of malicious | not reach and discover. We note that previous Android fuzzers [6, |  |  |  |  |  |  |  |
| behavior, GUI fuzzing alone cannot trigger certain events, limiting | 36] mainly discover crashes caused by null pointer exceptions. |  |  |  |  |  |  |  |
| its effectiveness in comprehensive app analysis as discussed in Sec- | On the contrary, AHA-Fuzz primarily detects crashes involving |  |  |  |  |  |  |  |
| tion 6.2. Therefore, we believe that AHA-Fuzz, when combined with | IllegalArgumentException | and | ClassCastException | . AHA-Fuzz |  |  |  |  |
| APE’s GUI fuzzing, performs intent fuzzing that efficiently triggers | triggers such crashes when the extras field value from AHA-Fuzz is |  |  |  |  |  |  |  |
| a wide range of intent events associated with malicious behaviors. | outside the expected range ( | IllegalArgumentException | ), or when |  |  |  |  |  |
| MATE. | We note that MATE’s app-under-test fuzzing strategy re- | an unexpected type is encountered ( | ClassCastException | ), | e | . | g | ., ex- |
| quires repackaging the target app. Hence, it is not feasible to analyze | pecting | JSON | but receiving a | String | . |  |  |  |
| hardened apps with integrity checks. Consequently, MATE fails | We observe that the primary reason AHA-Fuzz can discover |  |  |  |  |  |  |  |
| to test 29 out of the 40 apps. This result demonstrates that AHA- | unknown bugs lies in the diversity of intent inputs. As the fuzzer |  |  |  |  |  |  |  |
| Fuzz’s design is effective in analyzing real-world hardened apps. | explores deeper code paths, AHA-Fuzz extracts more intent-related |  |  |  |  |  |  |  |
| Also, MATE-AHA (a variant mode of MATE) outperforms MATE’s | information, regardless of whether apps use hardening techniques. |  |  |  |  |  |  |  |
| intent fuzzing algorithm. This is because MATE randomly gen- | In contrast, all baseline fuzzers rely on static analysis to mutate |  |  |  |  |  |  |  |
| erate intents. On the other hand, AHA-Fuzz’s coverage feedback | values from extras, resulting in limited input diversity. |  |  |  |  |  |  |  |
| algorithm can generate a wide range of effective intents. | Information Leak. | We discover 21 information leaks via our light- |  |  |  |  |  |  |
| ICCBot and IntentFuzzer. | The variant modes of ICCBot and In- | weight dynamic taint analysis (as explained in Section 4.4.2). We |  |  |  |  |  |  |
| tentFuzzer ( | i | . | e | ., ICCBot-AHA and IntentFuzzer-AHA) call more | identify four information leakage patterns: network information, |  |  |  |
| methods than the original modes, particularly in malware. ICCBot- | authentication code, device ID, and app installation paths, as shown |  |  |  |  |  |  |  |
| AHA triggers 32 | . | 6% more methods, and IntentFuzzer-AHA triggers | in Table 8. We note that AHA-Fuzz can detect various information |  |  |  |  |  |
| 51 | . | 0% more methods. This result is due to the use of packers in | leaks through method-level taint propagation. In the case of the |  |  |  |  |  |
| malware. Albeit benign apps are obfuscated, static analysis can | 21 information leaks AHA-Fuzz found, we confirm that sensitive |  |  |  |  |  |  |  |
| still identify some intent-related operations. We observe developers | information is processed and leaked through the Java standard |  |  |  |  |  |  |  |
| apply obfuscation to their main logic code but exclude third-party | library, regardless of the hardening technique ( | e | . | g | ., | String.append | ). |  |
| code. However, packers used in malware, such as Qihoo [1], pack all | We also confirm that AHA-Fuzz’s intent fuzzing reaches buggy |  |  |  |  |  |  |  |
| DEX code and unpack it at runtime. As a result, the static analysis | code (causing information leaks) that previous works cannot. For |  |  |  |  |  |  |  |
| used in ICCBot and IntentFuzzer is ineffective to extract intent- | instance, regarding network information leak, AndroidX uses a |  |  |  |  |  |  |  |
| related information in packed apps. In contrast, AHA-Fuzz extracts | custom wrapper class for | Log | . During execution, the custom | Log |  |  |  |  |

class is initialized in release mode, which sanitizes debug logs. Yet,

---

## Page 13

| Intent-aware Fuzzing for Android Hardened Application | CCS ’25, October 13–17, 2025, Taipei, Taiwan |  |  |  |
| --- | --- | --- | --- | --- |
| Table 8: 47 Previously Unknown Bugs Discovered by AHA-Fuzz. | Requiring Root Permissions. | AHA-Fuzz leverages an eBPF- |  |  |
| Oracle | Bug pattern | Package | Number | based dynamic analysis environment. To activate eBPF kernel sub- |
| Crash | IllegalArgumentException | Gmail + 13 more | 14 | system, it requires root permissions. Yet, it is worth noting that |
| Crash | ClassCastException | Google Home + 7 more | 8 | Android rooting can be easily accomplished on Android emulators |

| Crash | NullPointerException | Roblox + 4 more | 4 |
| --- | --- | --- | --- |
| Leak | Network | Android-sdk + 5 more | 6 |
| Leak | Authentication code | Android-sdk | 1 |

AHA-Fuzz calls the uninitialized custom Log class, causing it to

be initialized in debug mode. In the debug mode of their custom

Log , network capabilities are logged, which require permissions

( e . g ., ACCESS_NETWORK_STATE ) to access. We also confirmed that the

Facebook device ID leak and Firebase authentication code leak also

occur only through the intent event.

To verify that the information leaks we discover are unique bugs

that other tools cannot find, we first attempt to use dynamic taint

analysis tools but is unsuccessful. System modification-based taint

analysis tools [18, 59, 62, 66] only support versions up to Android

information leaks and two crashes and fix three information leaks.

( e . g ., using “adb root” command [29]). Further, certain Android

malware exclusively functions on rooted Android [51]. Thus, we

Information leak detection coverage. Sensitive information is

generally stored and managed as primitive or String types, and

AHA-Fuzz is capable of detecting information leaks involving these

types. However, when the data is stored in other types or trans-

formed [15] ( e . g ., via encoding or encryption), AHA-Fuzz is unable

to detect the associated information leaks. These information leaks

can be detected by introducing new automatic approaches for iden-

tifying related APIs, or by manually specifying them as additional

tracking targets.

8 Future work

9 Related Work

| Leak | Device id | Facebook | 1 | believe that the rooted Android environment is not a significant |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leak | App installation path | Firefox + 12 more | 13 | limitation and can be beneficial for analyzing Android malware. |  |  |  |  |  |
| 6, while most of the apps we test (98%) require Android 8 or higher | Special Type Mutation. | AHA-Fuzz currently faces limitations |  |  |  |  |  |  |  |
| versions. Other dynamic taint analysis tools [3, 64], including DBI, | in mutating special types ( | e | . | g | ., | Binder | or | Serializable | ) because |
| require manual configuration to set exact source and sink points, | the object layouts of such types differ across apps. Although our |  |  |  |  |  |  |  |  |
| which makes them unsuitable for discovering new information | analysis in Table 4 (Section 4.2.2) shows that only 6.5% of the extras |  |  |  |  |  |  |  |  |
| leaks. Thus, we use FlowDroid [5], a popular static taint analysis | in tested apps involve special types, as our future work, we plan to |  |  |  |  |  |  |  |  |
| tool, to verify whether it detects any of the 21 bugs. We confirm that | extend AHA-Fuzz to support special type mutation by recovering |  |  |  |  |  |  |  |  |
| FlowDroid cannot detect any of these bugs due to app hardening | the layout of these special type objects based on our Java object |  |  |  |  |  |  |  |  |
| techniques that reduce the accuracy of static analysis. | layout recovery techniques (Section 4.2.1). |  |  |  |  |  |  |  |  |
| For instance, AHA-Fuzz detects a device ID leak in the Facebook | Bug Analysis. | AHA-Fuzz currently supports detecting two types of |  |  |  |  |  |  |  |
| app, triggered by a | GET_PHONE_ID | intent generated by AHA-Fuzz. | bugs, crashes and information leaks, but it faces challenges when an- |  |  |  |  |  |  |
| This leaked device ID enables user identification, which leads to a | alyzing identified bugs ( | e | . | g | ., root cause analysis). While AHA-Fuzz |  |  |  |  |
| privacy leakage that enables cross-app tracking [74] and unautho- | records all framework API calls to trace which APIs are invoked |  |  |  |  |  |  |  |  |
| rized user profiling [17]. Existing taint analysis approaches, such | by buggy code, conducting in-depth analyses such as root cause |  |  |  |  |  |  |  |  |
| as FlowDroid [5] and Vialin [3], fail to detect the issue because | investigation or patch generation remains difficult. In future work, |  |  |  |  |  |  |  |  |
| the component is currently fully hardened. More specifically, the | we plan to enhance AHA-Fuzz with the capabilities to effectively |  |  |  |  |  |  |  |  |
| buggy code is located in a dynamically loaded module, which is | analyze bugs in hardened apps, such as reconstructing backtraces |  |  |  |  |  |  |  |  |
| invisible to static analysis (FlowDroid) or fails to instrument the | that are resistant to hardening techniques. |  |  |  |  |  |  |  |  |
| app code (Vialin). In contrast, AHA-Fuzz successfully detects this | Cross-platform Framework App Support. | Recently, many apps |  |  |  |  |  |  |  |
| bug by leveraging method-level taint propagation, and this bug is | have been developed using new cross-platform frameworks ( | e | . | g | ., Flut- |  |  |  |  |
| fixed by Facebook. | ter [23], Xamarin [48], and React Native [53]). Consequently, there |  |  |  |  |  |  |  |  |
| Bug Report. | Since Android apps on Google Play are closed-source, | is a growing need for analysis tools tailored to these frameworks. |  |  |  |  |  |  |  |
| direct communication with developers for bug confirmation is not | Since AHA-Fuzz is based on eBPF and does not heavily depend |  |  |  |  |  |  |  |  |
| feasible. Among the 46 apps in which AHA-Fuzz identified bugs, | on specific cross-platform frameworks at runtime, we plan to ex- |  |  |  |  |  |  |  |  |
| only Google, Facebook, and Firefox allow users to report bugs in | tend AHA-Fuzz testing scope to newly emerging cross-platform |  |  |  |  |  |  |  |  |
| public security bug reporting platforms. They acknowledge four | framework apps as our future work. |  |  |  |  |  |  |  |  |
| 7 | Discussion | Fuzzing. | Prior fuzzing works for Android apps attempt to max- |  |  |  |  |  |  |
| Testing Real Devices. | Research literature [57, 62] recommends | imize code coverage similar to AHA-Fuzz [6, 36, 57, 58, 70], but |  |  |  |  |  |  |  |
| fuzzing on real Android devices rather than testing the inputs on | they deal with GUI fuzzing and simple intents. APE [36] is an auto- |  |  |  |  |  |  |  |  |
| Android emulators due to the anti-analysis problems. We note that | mated model-based GUI testing technique that dynamically refines |  |  |  |  |  |  |  |  |
| users can run AHA-Fuzz on real Android devices with root permis- | GUI models to improve code coverage and crash detection. This |  |  |  |  |  |  |  |  |
| sions since AHA-Fuzz leverages a dynamic analysis environment | approach does not focus on the generation of intents. Stoat [58] is a |  |  |  |  |  |  |  |  |
| based on eBPF. Yet, we evaluate AHA-Fuzz on emulators rather | model-based testing approach by generating stochastic models that |  |  |  |  |  |  |  |  |
| than the real devices. The main reason is that our evaluation tests | describe GUI interactions. It constructs models dynamically and |  |  |  |  |  |  |  |  |
| more than 300 different Android apps with ten different modes; | iteratively mutates them to generate diverse test cases, while also in- |  |  |  |  |  |  |  |  |
| thus, testing with real devices is impractical to evaluate all sets. | jecting system-level events, including broadcast intents, to uncover |  |  |  |  |  |  |  |  |

---

## Page 14

| CCS ’25, October 13–17, 2025, Taipei, Taiwan | Seongyun Jeong et al. |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| intricate bugs. Yet, it is limited to sending Manifest-defined system | This work was also supported by the MSIT (Ministry of Science and |  |  |  |  |  |  |
| broadcast intents without intent-related feedback ( | e | . | g | ., | action | and | ICT), Korea, under the ITRC (Information Technology Research |
| extras | fields). Furthermore, Auer et al. [6] suggest that combining | Center) support program (No. 2710078921) supervised by the IITP. |  |  |  |  |  |
| UI inputs with intents triggers higher code coverage than sending | This work was also supported by the IITP grant funded by the |  |  |  |  |  |  |
| either alone. Their empirical study identified a specific ratio that | Korea government (MSIT) (RS-2024-00341722, RS-2024-00437306, |  |  |  |  |  |  |
| yielded the best results, but considering the unique combination | RS-2024-00341722, and RS-2022-000563, Development of Cyber Re- |  |  |  |  |  |  |
| for each app, as in our approach, allows for more efficient fuzzing. | silience Method for Intelligent Service Robots, Development of |  |  |  |  |  |  |
| Intent fuzzing tools [6, 13, 38, 40, 46, 57, 67] focus on generating | Integrated Platform for Expanding and Safely Applying Memo- |  |  |  |  |  |  |
| appropriate extras ( | i | . | e | ., key-value pairs) to maximize code cover- | rySafe Languages, AI-Based Automated Vulnerability Detection |  |  |
| age. However, these methods rely on static analysis, making them | and Safe Code Generation, and Automatic Deep Malware Analysis |  |  |  |  |  |  |
| ineffective against obfuscation techniques. DroidFuzzer [70] and | Technology for Cyber Threat Intelligence). |  |  |  |  |  |  |

Sasnauskas et al. [57] propose testing approaches sending intents

| to components of target apps. Yet, these works only treat activity | References |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| intent and its simple usage ( | e | . | g | ., null value and predefined constant). | [1] Qihoo 360. | Products and Services | , Accessed: Jan. 10, 2025. http://www | . | 360 | . | cn/ |
| Dynamic Analysis for Android Security. | Many frameworks | about/englishversion | . | html. |  |  |  |  |  |  |  |

[2] Yaniv Agman and Danny Hendler. Bpfroid: Robust real time android malware

| attempt to detect security threats ( | e | . | g | ., information leak, privilege | detection framework. | arXiv preprint arXiv:2105.14344 | , 2021. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| escalation) in Android apps by tracing code executions on dynamic | [3] Khaled Ahmed, Yingying Wang, Mieszko Lis, and Julia Rubin. Vialin: Path-aware |  |  |  |  |  |  |
| instrumentation tools [60, 62, 64, 66, 73]. They reconstruct or track | dynamic taint analysis for android. In | Proceedings of the 31st ACM Joint European |  |  |  |  |  |

Software Engineering Conference and Symposium on the Foundations of Software

| data flows to figure out the behaviors of the apps by modifying | Engineering | , ESEC/FSE 2023, page 1598–1610, 2023. |  |
| --- | --- | --- | --- |
| Android systems and emulators, or by using DBI [60, 62, 64, 66]. | [4] Saswat Anand. | ELLA: A Tool for Binary Instrumentation of Android Apps | , Accessed: |
| Yet, these works require Android system modification or incur high | Jan. 10, 2025. https://github | . | com/saswatanand/ella. |

[5] Steven Arzt, Siegfried Rasthofer, Christian Fritz, Eric Bodden, Alexandre Bartel,

overhead; thus, users also need to update their frameworks with Jacques Klein, Yves Le Traon, Damien Octeau, and Patrick McDaniel. Flowdroid:

each system version update ( i . e ., Android version update) or face Precise context, flow, field, object-sensitive and lifecycle-aware taint analysis for

android apps. ACM sigplan notices , 49(6):259–269, 2014.

| high runtime overhead. To fill this gap, our approach does not need | [6] Michael Auer, Andreas Stahlbauer, and Gordon Fraser. Android fuzzing: Balancing |  |
| --- | --- | --- |
| system modifications by leveraging eBPF. This is because it uses | user-inputs and intents. In | 2023 IEEE Conference on Software Testing, Verification |
| kernel subsystem with support from Android OS [22]. NCScope [73] | and Validation (ICST) | , pages 37–48, 2023. |

[7] Michael Backes, Sven Bugiel, Oliver Schranz, Philipp von Styp-Rekowsky, and

| also uses eBPF programs to retrieve the in-memory data. However, | Sebastian Weisgerber. Artist: The android runtime instrumentation and security |  |  |
| --- | --- | --- | --- |
| it only covers native code execution and requires specific hardware | toolkit. In | 2017 IEEE European Symposium on Security and Privacy (EuroS&P) | , |
| (ARM ETM) to trace CPU-level instructions. | pages 481–495. IEEE, 2017. |  |  |

[8] backlinko. iPhone vs Android Statistics , Accessed: Jan. 10, 2025. https://

backlinko . com/iphone-vs-android-statistics.

[9] Baidu. Baidu , Accessed: Jan. 10, 2025. https://app . baidu . com.

10 Conclusion [10] bankmycell. How many apps in google play store? (2024) , Accessed: Jan. 10, 2025.

We introduce AHA-Fuzz, the first intent-aware greybox fuzzing https://www . bankmycell . com/blog/number-of-google-play-store-apps/.

[11] Frederic Besler, Carsten Willems, and Ralf Hund. Countering innovative sandbox

| framework for hardened Android apps. AHA-Fuzz has three key as- | evasion techniques used by malware. In | 29th Annual FIRST Conference | , 2017. |
| --- | --- | --- | --- |
| pects that distinguish it from previous works: ( | 𝑖 | ) introducing a valid | [12] Michael Cao, Khaled Ahmed, and Julia Rubin. Rotten apples spoil the bunch: |
| intent generator by recovering object layouts and leveraging key- | An anatomy of google play malware. In | Proceedings of the 44th International |  |

Conference on Software Engineering , pages 1919–1931, 2022.

value feedback to create valid intent inputs, ( 𝑖𝑖 ) precisely evaluating [13] Kwanghoon Choi, Myungpil Ko, and Byeong-Mo Chang. A practical intent

the impact of these generated inputs using a selective coverage fuzzing tool for robustness of inter-component communication in android apps.

KSII Transactions on Internet & Information Systems , 12(9), 2018.

| feedback approach, and ( | 𝑖𝑖𝑖 | ) introducing approaches for efficiently | [14] Minseong Choi, Yubin Im, Steve Ko, Yonghwi Kwon, Yuseok Jeon, and Haehyun |
| --- | --- | --- | --- |
| triggering hard-to-trigger bugs and detecting information leaks | Cho. Dryjin: Detecting information leaks in android applications. In | IFIP Inter- |  |
| in hardened app. Our evaluation results show that AHA-Fuzz is | national Conference on ICT Systems Security and Privacy Protection | , pages 76–90. |  |

Springer, 2024.

| effective in triggering actions that previous works cannot reach. | [15] Andrea Continella, Yanick Fratantonio, Martina Lindorfer, Alessandro Puccetti, |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Especially, compared to previous works, AHA-Fuzz triggers 92 | . | 3% | Ali Zand, Christopher Kruegel, Giovanni Vigna, et al. | Obfuscation-resilient |  |  |  |  |  |
| more intents (3 | . | 45 | × | faster) and 23 | . | 9% more methods. AHA-Fuzz | privacy leak detection for mobile apps through differential analysis. In | NDSS | , |

volume 17, pages 10–14722, 2017.

also discovers 47 previously unknown bugs that previous works [16] Shuaike Dong, Menghao Li, Wenrui Diao, Xiangyu Liu, Jian Liu, Zhou Li, Fenghao

cannot find. Among the 47 bugs found, 6 have been acknowledged Xu, Kai Chen, Xiaofeng Wang, and Kehuan Zhang. Understanding android

obfuscation techniques: A large-scale investigation in the wild. In Security and

| by developers from Google, Firefox, and Facebook, and three have | privacy in communication networks: 14th international conference, secureComm |  |  |
| --- | --- | --- | --- |
| been fixed. The open-source version of AHA-Fuzz is available at | 2018 | , pages 172–192. Springer, 2018. |  |
| https://github | . | com/S2-Lab/AHA-fuzz. | [17] Zikan Dong, Tianming Liu, Jiapeng Deng, Li Li, Minghui Yang, Meng Wang, |

Guosheng Xu, and Guoai Xu. Exploring covert third-party identifiers through

external storage in the android new era. In 33rd USENIX Security Symposium

Acknowledgments (USENIX Security 24) , pages 4535–4552, 2024.

[18] William Enck, Peter Gilbert, Seungyeop Han, Vasant Tendulkar, Byung-Gon

| This work was supported by a Korea Internet & Security Agency | Chun, Landon P. Cox, Jaeyeon Jung, Patrick McDaniel, and Anmol N. Sheth. |
| --- | --- |
| (KISA) grant funded by the Korean government (PIPC) (No. | Taintdroid: An information-flow tracking system for realtime privacy monitoring |

on smartphones. volume 32, June 2014.

| 2780000017). This work was partly supported by ICT Creative Con- | [19] ExtendedAndroidTools. | facebookexperimental | , Accessed: Jan. 10, 2025. https: |
| --- | --- | --- | --- |
| silience Program through the Institute of Information & Communi- | //github | . | com/facebookexperimental/ExtendedAndroidTools. |

[20] Github. CodeQL , Accessed: Jan. 10, 2025. https://codeql . github . com/.

cations Technology Planning & Evaluation (IITP) grant funded by [21] Google. Bundle , Accessed: Jan. 10, 2025. https://developer . android . com/reference/

the Korea government (MSIT)(IITP-2025-RS-2020-II201819, 10%). android/os/Bundle.

---

## Page 15

| Intent-aware Fuzzing for Android Hardened Application | CCS ’25, October 13–17, 2025, Taipei, Taiwan |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [22] Google. | Extending the Kernel with eBPF | , Accessed: Jan. 10, 2025. | https: | *droid: Assessment and evaluation of android application analysis tools. | ACM |  |  |  |  |  |  |  |  |
| //source | . | android | . | com/docs/core/architecture/kernel/bpf. | Comput. Surv. | , 49(3), oct 2016. |  |  |  |  |  |  |  |
| [23] Google. | Flutter - Build for any screen | , Accessed: Jan. 10, 2025. https://flutter | . | dev. | [55] rednaga. | APKiD: Fast Identification of Mobile RASP SDKs | , Accessed: Jan. 10, 2025. |  |  |  |  |  |  |
| [24] Google. | Intents | and | intent | filters | , | Accessed: | Jan. | 10, | 2025. | https:// | https://github | . | com/rednaga/APKiD. |
| developer | . | android | . | com/guide/components/intents-filters. | [56] Andrea Romdhana, Mariano Ceccato, Gabriel Claudiu Georgiu, Alessio Merlo, |  |  |  |  |  |  |  |  |
| [25] Google. | NDK | , Accessed: Jan. 10, 2025. https://developer | . | android | . | com/ndk. | and Paolo Tonella. Cosmo: Code coverage made easier for android. In | 2021 14th |  |  |  |  |  |
| [26] google. | Play Integrity API | , Accessed: Jan. 10, 2025. https://developer | . | android | . | com/ | IEEE Conference on Software Testing, Verification and Validation (ICST) | , pages |  |  |  |  |  |
| google/play/integrity. | 417–423, 2021. |  |  |  |  |  |  |  |  |  |  |  |  |
| [27] Google. | Schedule alarms | , Accessed: Jan. 10, 2025. https://developer | . | android | . | com/ | [57] Raimondas Sasnauskas and John Regehr. Intent fuzzer: crafting intents of death. |  |  |  |  |  |  |
| develop/background-work/services/alarms/schedule. | In | Proceedings of the 2014 Joint International Workshop on Dynamic Analysis |  |  |  |  |  |  |  |  |  |  |  |
| [28] Google. | Shrink, obfuscate, and optimize your app | , Accessed: Jan. 10, 2025. https: | (WODA) and Software and System Performance Testing, Debugging, and Analytics |  |  |  |  |  |  |  |  |  |  |
| //developer | . | android | . | com/build/shrink-code. | (PERTEA) | , pages 1–5, 2014. |  |  |  |  |  |  |  |
| [29] Google. | Start the emulator from the command line | , Accessed: Jan. 10, 2025. https: | [58] Ting Su, Guozhu Meng, Yuting Chen, Ke Wu, Weiming Yang, Yao Yao, Geguang |  |  |  |  |  |  |  |  |  |  |
| //developer | . | android | . | com/studio/run/emulator-commandline. | Pu, Yang Liu, and Zhendong Su. Guided, stochastic model-based gui testing of |  |  |  |  |  |  |  |  |
| [30] Google. | UI/Application Exerciser Monkey | , Accessed: Jan. 10, 2025. | https: | android apps. In | Proceedings of the 2017 11th Joint Meeting on Foundations of |  |  |  |  |  |  |  |  |
| //developer | . | android | . | com/studio/test/other-testing-tools/monkey. | Software Engineering | , ESEC/FSE 2017, page 245–256, 2017. |  |  |  |  |  |  |  |
| [31] Google. | Android 12 features and changes list | , Accessed: May. 5, 2025. | https: | [59] Mingshen Sun, Tao Wei, and John CS Lui. | Taintart: A practical multi-level |  |  |  |  |  |  |  |  |
| //developer | . | android | . | com/about/versions/12/summary. | information-flow tracking system for android runtime. In | Proceedings of the |  |  |  |  |  |  |  |
| [32] Google. | Android 13 features and changes list | , Accessed: May. 5, 2025. | https: | 2016 ACM SIGSAC Conference on Computer and Communications Security | , pages |  |  |  |  |  |  |  |  |
| //developer | . | android | . | com/about/versions/13/summary. | 331–342, 2016. |  |  |  |  |  |  |  |  |
| [33] Google. | DexGuard | , Accessed: May. 5, 2025. https://source | . | android | . | com/docs/ | [60] Kimberly Tam, Salahuddin J Khan, Aristide Fattori, and Lorenzo Cavallaro. Cop- |  |  |  |  |  |  |
| core/runtime/jit-compiler. | perdroid: Automatic reconstruction of android malware behaviors. In | Ndss | , pages |  |  |  |  |  |  |  |  |  |  |
| [34] Google. | File-based encryption | , Accessed: May. 5, 2025. https://source | . | android | . | com/ | 1–15, 2015. |  |  |  |  |  |  |
| docs/security/features/encryption/file-based. | [61] Tencent. | Tencent Cloud | , Accessed: Jan. 10, 2025. https://www | . | tencentcloud | . | com. |  |  |  |  |  |  |
| [35] Google. | Log | Info | Disclosure | , | Accessed: | May. | 5, | 2025. | https: | [62] Lei Xue, Chenxiong Qian, Hao Zhou, Xiapu Luo, Yajin Zhou, Yuru Shao, and |  |  |  |
| //developer | . | android | . | com/privacy-and-security/risks/log-info-disclosure. | Alvin TS Chan. Ndroid: Toward tracking information flows across multiple an- |  |  |  |  |  |  |  |  |
| [36] Tianxiao Gu, Chengnian Sun, Xiaoxing Ma, Chun Cao, Chang Xu, Yuan Yao, Qirun | droid contexts. | IEEE Transactions on Information Forensics and Security | , 14(3):814– |  |  |  |  |  |  |  |  |  |  |
| Zhang, Jian Lu, and Zhendong Su. Practical gui testing of android applications via | 828, 2018. |  |  |  |  |  |  |  |  |  |  |  |  |
| model abstraction and refinement. In | 2019 IEEE/ACM 41st International Conference | [63] Lei Xue, Hao Zhou, Xiapu Luo, Le Yu, Dinghao Wu, Yajin Zhou, and Xiaobo Ma. |  |  |  |  |  |  |  |  |  |  |  |
| on Software Engineering (ICSE) | , pages 269–280. IEEE, 2019. | Packergrind: An adaptive unpacking system for android apps. | IEEE Transactions |  |  |  |  |  |  |  |  |  |  |
| [37] Yujiang Gui, Dongjie He, and Jingling Xue. Merge-replay: Efficient ifds-based | on Software Engineering | , 48(2):551–570, 2020. |  |  |  |  |  |  |  |  |  |  |  |
| taint analysis by consolidating equivalent value flows. In | 2023 38th IEEE/ACM | [64] Lei Xue, Yajin Zhou, Ting Chen, Xiapu Luo, and Guofei Gu. Malton: Towards | { | On- |  |  |  |  |  |  |  |  |  |
| International Conference on Automated Software Engineering (ASE) | , pages 319–331. | Device | } { | Non-Invasive | } | mobile malware analysis for | { | ART | } | . In | 26th USENIX |  |  |
| IEEE, 2023. | Security Symposium (USENIX Security 17) | , pages 289–306, 2017. |  |  |  |  |  |  |  |  |  |  |  |
| [38] Hui Guo, Ting Su, Xiaoqiang Liu, Siyi Gu, and Jingling Sun. Effectively finding | [65] Jiwei Yan, Shixin Zhang, Yepang Liu, Jun Yan, and Jian Zhang. Iccbot: fragment- |  |  |  |  |  |  |  |  |  |  |  |  |
| icc-related bugs in android apps via reinforcement learning. In | 2023 IEEE 34th | aware and context-sensitive icc resolution for android applications. In | Proceedings |  |  |  |  |  |  |  |  |  |  |
| International Symposium on Software Reliability Engineering (ISSRE) | , pages 403– | of the ACM/IEEE 44th International Conference on Software Engineering: Compan- |  |  |  |  |  |  |  |  |  |  |  |
| 414, 2023. | ion Proceedings | , ICSE ’22, page 105–109, 2022. |  |  |  |  |  |  |  |  |  |  |  |
| [39] Vincent Haupert, Dominik Maier, Nicolas Schneider, Julian Kirsch, and Tilo | [66] Lok Kwong Yan and Heng Yin. | { | DroidScope | } | : Seamlessly reconstructing the |  |  |  |  |  |  |  |  |
| Müller. Honey, i shrunk your app security: The state of android app harden- | { | OS | } | and dalvik semantic views for dynamic android malware analysis. In | 21st |  |  |  |  |  |  |  |  |
| ing. In | Detection of Intrusions and Malware, and Vulnerability Assessment: 15th | USENIX security symposium (USENIX security 12) | , pages 569–584, 2012. |  |  |  |  |  |  |  |  |  |  |
| International Conference, DIMVA 2018 | , pages 69–91. Springer, 2018. | [67] Kun Yang, Jianwei Zhuge, Yongke Wang, Lujue Zhou, and Haixin Duan. Intent- |  |  |  |  |  |  |  |  |  |  |  |
| [40] Roee Hay, Omer Tripp, and Marco Pistoia. Dynamic detection of inter-application | fuzzer: detecting capability leaks of android applications. In | Proceedings of the |  |  |  |  |  |  |  |  |  |  |  |
| communication vulnerabilities in android. In | Proceedings of the 2015 International | 9th ACM Symposium on Information, Computer and Communications Security | , |  |  |  |  |  |  |  |  |  |  |
| Symposium on Software Testing and Analysis | , ISSTA 2015, page 118–128, 2015. | ASIA CCS ’14, page 531–536, 2014. |  |  |  |  |  |  |  |  |  |  |  |
| [41] Ijiami. | Ijiami | , Accessed: Jan. 10, 2025. https://www | . | ijiami | . | cn. | [68] Wenbo Yang, Yuanyuan Zhang, Juanru Li, Junliang Shu, Bodong Li, Wenjun Hu, |  |  |  |  |  |  |
| [42] Hiroki Inayoshi, Shohei Kakei, and Shoichi Saito. | Execution recording and | and Dawu Gu. Appspear: Bytecode decrypting and dex reassembling for packed |  |  |  |  |  |  |  |  |  |  |  |
| reconstruction for detecting information flows in android apps. | IEEE Access | , | android malware. In | International Symposium on Recent Advances in Intrusion |  |  |  |  |  |  |  |  |  |
| 11:10730–10750, 2023. | Detection | , pages 359–381. Springer, 2015. |  |  |  |  |  |  |  |  |  |  |  |
| [43] Satori Threat Intelligence and Research Team. | TERRACOTTA Android Malware: | [69] Zhi Yang, Zhanhui Yuan, Shuyuan Jin, Xingyuan Chen, Lei Sun, Xuehui Du, |  |  |  |  |  |  |  |  |  |  |  |
| A Technical Study | , Accessed: Jan. 10, 2025. https://www | . | humansecurity | . | com/ | Wenfa Li, and Hongqi Zhang. | Fsaflow: Lightweight and fast dynamic path |  |  |  |  |  |  |
| learn/blog/terracotta-android-malware-a-technical-study. | tracking and control for privacy protection on android using hybrid analysis |  |  |  |  |  |  |  |  |  |  |  |  |
| [44] iovisor. | bcc | , Accessed: Jan. 10, 2025. https://github | . | com/iovisor/bcc. | with state-reduction strategy. In | 2022 IEEE Symposium on Security and Privacy |  |  |  |  |  |  |  |
| [45] Jiagu. | Jiagu | , Accessed: Jan. 10, 2025. https://jiagu | . | 360 | . | cn. | (SP) | , pages 2114–2129. IEEE, 2022. |  |  |  |  |  |
| [46] Anatoli Kalysch, Mark Deutel, and Tilo Müller. Template-based android inter pro- | [70] Hui Ye, Shaoyin Cheng, Lanbo Zhang, and Fan Jiang. Droidfuzzer: Fuzzing the |  |  |  |  |  |  |  |  |  |  |  |  |
| cess communication fuzzing. In | Proceedings of the 15th International Conference | android apps with intent-filter tag. In | Proceedings of International Conference on |  |  |  |  |  |  |  |  |  |  |
| on Availability, Reliability and Security | , ARES ’20, 2020. | Advances in Mobile Computing & Multimedia | , pages 68–74, 2013. |  |  |  |  |  |  |  |  |  |  |
| [47] Licle. | DexProtector: Multi-layered RASP solution that secures your Android and iOS | [71] Xueling Zhang, Xiaoyin Wang, Rocky Slavin, and Jianwei Niu. Condysta: Context- |  |  |  |  |  |  |  |  |  |  |  |
| apps against static and dynamic analysis, illegal use and tampering | , Accessed: Jan. | aware dynamic supplement to static taint analysis. In | 2021 IEEE Symposium on |  |  |  |  |  |  |  |  |  |  |
| 10, 2025. https://dexprotector | . | com. | Security and Privacy (SP) | , pages 796–812, 2021. |  |  |  |  |  |  |  |  |  |
| [48] Microsoft. | What is Xamarin? | , Accessed: Jan. 10, 2025. https://learn | . | microsoft | . | com/ | [72] Yueqian Zhang, Xiapu Luo, and Haoyang Yin. Dexhunter: toward extracting |  |  |  |  |  |  |
| previous-versions/xamarin/get-started/what-is-xamarin. | hidden code from packed android applications. In | Computer Security–ESORICS |  |  |  |  |  |  |  |  |  |  |  |
| [49] Mobile-IoT-Security-Lab. | Obfuscapk | , Accessed: Jan. 10, 2025. https://github | . | com/ | 2015: 20th European Symposium on Research in Computer Security, Vienna, Austria, |  |  |  |  |  |  |  |  |
| Mobile-IoT-Security-Lab/Obfuscapk. | September 21-25, 2015, Proceedings, Part II 20 | , pages 293–311. Springer, 2015. |  |  |  |  |  |  |  |  |  |  |  |
| [50] Andy Nisbet, Nuno Miguel Nobre, Graham Riley, and Mikel Luján. Profiling | [73] Hao Zhou, Shuohan Wu, Xiapu Luo, Ting Wang, Yajin Zhou, Chao Zhang, and |  |  |  |  |  |  |  |  |  |  |  |  |
| and tracing support for java applications. In | Proceedings of the 2019 ACM/SPEC | Haipeng Cai. Ncscope: hardware-assisted analyzer for native code in android |  |  |  |  |  |  |  |  |  |  |  |
| International Conference on Performance Engineering | , pages 119–126, 2019. | apps. In | Proceedings of the 31st ACM SIGSOFT International Symposium on Software |  |  |  |  |  |  |  |  |  |  |
| [51] OWASP. | Android | Anti-Reversing | Defenses | , | Accessed: | Jan. | 10, | 2025. | Testing and Analysis | , pages 629–641, 2022. |  |  |  |
| https://github | . | com/OWASP/owasp-mastg/blob/master/Document/0x05j- | [74] Sebastian Zimmeck, Jie S Li, Hyungtae Kim, Steven M Bellovin, and Tony Jebara. |  |  |  |  |  |  |  |  |  |  |
| Testing-Resiliency-Against-Reverse-Engineering | . | md. | A privacy analysis of cross-device tracking. In | 26th USENIX Security Symposium |  |  |  |  |  |  |  |  |  |
| [52] Aleksandr Pilgun, Olga Gadyatskaya, Yury Zhauniarovich, Stanislav Dashevskyi, | (USENIX Security 17) | , pages 1391–1408, 2017. |  |  |  |  |  |  |  |  |  |  |  |

Artsiom Kushniarou, and Sjouke Mauw. Fine-grained code coverage measure-

ment in automated black-box android testing. ACM Trans. Softw. Eng. Methodol. ,

29(4), jul 2020.

[53] Meta Platforms. React Native , Accessed: Jan. 10, 2025. https://reactnative . dev.

[54] Bradley Reaves, Jasmine Bowers, Sigmund Albert Gorski III, Olabode Anise, Rahul

Bobhate, Raymond Cho, Hiranava Das, Sharique Hussain, Hamza Karachiwala,

Nolen Scaife, Byron Wright, Kevin Butler, William Enck, and Patrick Traynor.

---
title: "Assessing the Capability of Android Dynamic Analysis Tools to Combat Anti-Runtime Analysis Techniques"
author: "Dewen Suo; Lei Xue; Weihao Huang; Runze Tan; Guozi Sun"
creator: "arXiv GenPDF (tex2pdf:57610bf)"
pages: 18
---

# Assessing the Capability of Android Dynamic Analysis Tools to Combat Anti-Runtime Analysis Techniques

> **作者**：Dewen Suo; Lei Xue; Weihao Huang; Runze Tan; Guozi Sun
> **總頁數**：18 頁

---

## Page 1

Assessing the Capability of Android Dynamic Analysis Tools to

Combat Anti-Runtime Analysis Techniques

a,c b b b a , ∗

Dewen Suo , Lei Xue , Weihao Huang , Runze Tan and Guozi Sun

a Nanjing University of Posts and Telecommunications, No.9, Wenyuan Road, Yadong New District, Nanjing, 210023, China

b Sun Yat-sen University, No. 66, Gongchang Road, Guangming District, Shenzhen, Guangdong 518107, China

c China Telecom Shandong Branch, Jinan, 250000, China.

A R T I C L E I N F O A B S T R A C T

Android is the leading mobile operating system, com-

manding an 80% market share in the smartphone sector [29].

However, this dominance also makes it a prime target for

malicious attacks, which pose significant risks to user pri-

vacy, data security, and overall system integrity [50, 67]. As

a result, researchers and security analysts have developed

a variety of sophisticated tools and techniques aimed at

Android malware detection and mitigation.

Malicious applications can infringe upon user privacy,

steal sensitive information, and result in economic losses.

In response to these threats, security researchers and ana-

lysts have been actively studying Android malware and de-

veloping effective countermeasures. Meanwhile, to conceal

malicious payloads, malware developers have increasingly

turned to anti-analysis techniques that obfuscate or hinder

analysis processes [51]. Consequently, the academic com-

munity has made significant efforts to develop powerful

tools for in-depth application analysis.

Traditional anti-analysis techniques typically focus on

hindering static analysis by increasing its complexity. One

of the most widely used methods is code obfuscation [11,

34, 28]. Code obfuscation increases the complexity of the

code by modifying its structure and variable names, making

static code analysis more challenging.

In contrast, Anti-Runtime Analysis (ARA) technology

is a relatively new category of anti-analysis techniques that

specifically target dynamic analysis rather than static meth-

ods [8, 35]. Initially, ARA technology was designed for legit-

imate purposes, such as protecting intellectual property and

preventing reverse engineering [31, 24]. However, the adop-

tion of ARA technology by malicious software developers

examination of applications, thus complicating efforts to ensure platform security. This paper presents

a comprehensive empirical study that assesses the ability of widely-used Android dynamic analysis

tools to bypass various ARA techniques. Our findings reveal a critical gap in the effectiveness of

existing dynamic analysis tools to counter ARA mechanisms, highlighting an urgent need for more

robust solutions. This work provides valuable insights into the limitations of existing tools and

highlights the need for improved methods to counteract ARA technologies, thus advancing the field

of software security and dynamic analysis.

employing ARA techniques, these developers can obscure

the detection of malicious behaviors, effectively prolonging

the lifecycle of their malicious applications. In order to

effectively analyze the behavior of malicious applications,

Android dynamic analysis tools must possess the capability

to handle ARA technology.

Previous studies have systematically evaluated the per-

formance of Android static analysis tools, particularly their

ability to handle code obfuscation [23, 40, 53, 38]. These

studies have confirmed that code obfuscation can signifi-

cantly impact the effectiveness of static analysis tools [16].

However, there is a notable gap in research concerning the

performance of Android dynamic analysis tools and their

ability to handle ARA techniques.

To address this gap, we evaluated six well-known An-

droid dynamic analysis tools using a dataset of 993 benign

and 991 malicious applications. Our primary objective was

to assess the effectiveness of existing Android dynamic anal-

as the evaluation metric. Specifically, we aimed to evaluate

the effectiveness of dynamic analysis tools in countering

ARA techniques through multiple controlled experiments by

comparing the code coverage of applications in their original

form with that achieved when analyzed using dynamic anal-

ysis tools. This study aims to assist security professionals

in better understanding the limitations and capabilities of

current dynamic analysis tools, enabling them to make more

informed decisions when selecting tools. Additionally, we

seek to highlight the gaps in the existing tools to promote

technological advancements in the field.

To highlight the practical implications of our study, we

summarize three representative findings below: (1) None of

| Keywords | : | As the dominant mobile operating system, Android continues to attract a substantial influx of |
| --- | --- | --- |
| Android Security Engineering | new applications each year. However, this growth is accompanied by increased attention from |  |
| Anti-Analysis Techniques | malicious actors, resulting in a significant rise in security threats to the Android ecosystem. Among |  |
| Mobile Software Protection | these threats, the adoption of Anti-Runtime Analysis (ARA) techniques by malicious applications |  |
| Software engineering | poses a serious challenge, as it hinders security professionals from effectively analyzing malicious |  |
| Software Application Hardening | behaviors using dynamic analysis tools. ARA technologies are designed to prevent the dynamic |  |
| 1. Introduction | has complicated the work of security analysts [56, 35]. By |  |

arXiv:2512.12551v1 [cs.SE] 14 Dec 2025 ysis tools in handling ARA techniques, using code coverage

| ∗ | Corresponding author: Guozi Sun (Email: sun@njupt.edu.cn). | the evaluated dynamic analysis tools were able to effectively |
| --- | --- | --- |
| Suo et al.: | Preprint submitted to Elsevier | Page 1 of 18 |

---

## Page 2

| handle ARA techniques, regardless of whether the target ap- | ∙ | Practical Implications | : By identifying the strengths |
| --- | --- | --- | --- |
| plications were benign or malicious; (2) Increasing the num- | and weaknesses of current Android dynamic analysis tools in |  |  |
| ber of deployed ARA techniques generally led to stronger | dealing with ARA techniques, this research offers essential |  |  |
| resistance against analysis. Notably, the most significant | guidance to security professionals, IT auditors, and mobile |  |  |
| drop in code coverage occurred between applications with | application developers in strengthening the security posture |  |  |
| zero ARA techniques and those with one to five techniques. | of Android systems. |  |  |
| Although deploying more than five techniques continued | Roadmap | : The remaining parts of this paper are orga- |  |
| to enhance resistance, the marginal effect diminished; (3) | nized as follows: Section 2 provides background information |  |  |
| When considering both analysis capability and runtime ef- | on Android dynamic analysis and ARA technology. Section |  |  |
| ficiency, DroidDissector [37] demonstrated the best overall | 3 discusses in detail the research questions addressed in |  |  |
| performance among the six evaluated tools. Further detailed | this study. Section 4 introduces the research methodology. |  |  |
| results are discussed in Section 5, encompassing a broader | Results and findings are reported in Section 5. Section |  |  |
| spectrum of technical findings. | 6 discusses the results and provides recommendations for |  |  |
| To guide our research, we have distilled three key re- | enhancing dynamic analysis tools. Threats to validity are |  |  |
| search questions, including: | presented in Section 7. Finally, this paper outlines related |  |  |
| Q1: Can dynamic analysis tools effectively handle ARA | work (Section 8) and draws conclusions (Section 9). |  |  |

technology?

| Q2: What are the differences in the impact of various | 2. Background |  |  |
| --- | --- | --- | --- |
| categories and quantities of ARA technology on dynamic | This section provides a brief overview of Android dy- |  |  |
| analysis tools? | namic analysis and Anti-Runtime Analysis (ARA) technolo- |  |  |
| Q3: How efficient are dynamic analysis tools when pro- | gies, offering readers essential context to better understand |  |  |
| cessing a large-scale dataset of applications protected by | the subsequent discussion in the paper. |  |  |
| ARA techniques? | 2.1. Android Dynamic Analysis |  |  |
| We will provide a detailed discussion of the three ques- | Android dynamic analysis refers to a method of ana- |  |  |
| tions we have posed in section 5. | lyzing the security and performance characteristics of an |  |  |
| However, obtaining convincing answers to these ques- | application by observing and recording its behavior and |  |  |
| tions is not straightforward, as it requires a large-scale inves- | interactions during runtime. Compared to static analysis, |  |  |
| tigation and the resolution of key technical challenges and | dynamic analysis has the advantage of capturing the appli- |  |  |
| practical constraints. | cation’s actual runtime behavior, which enables a more com- |  |  |
| C: Lack of an automated evaluation framework for ARA | prehensive assessment of its security and performance [64]. |  |  |
| detection and dynamic analysis tools assessment. | Evaluat- | The widespread use of obfuscation techniques has sig- |  |
| ing dynamic analysis tools for their ability to handle ARA | nificantly reduced the effectiveness of static analysis for app |  |  |
| techniques is time-consuming. Currently, there is a lack of | scrutiny [65, 57, 12, 21]. Obfuscation techniques modify |  |  |
| an automated framework that can effectively detect ARA | the static code and resources of an application, making |  |  |
| techniques in APKs and assess how well the tools handle | them harder to understand and analyze. As a result, static |  |  |
| them. Such a framework needs to be highly scalable to | analysis becomes less efficient and accurate [23]. In con- |  |  |
| facilitate future evaluations of additional tools. | trast, dynamic analysis enables the real-time observation and |  |  |
| In addition to this core challenge, our study must also | recording of an application’s behavior at runtime, unaffected |  |  |
| contend with practical constraints, such as the difficulty of | by obfuscation techniques. Thus, dynamic analysis can bet- |  |  |
| measuring code coverage without access to the source code | ter address the challenges posed by obfuscation techniques, |  |  |
| of the target APKs. Since Android applications distributed | enhancing both the comprehensiveness and accuracy of the |  |  |
| via platforms like Google Play are typically available only | analysis [48]. Consequently, the importance of dynamic |  |  |
| in compiled form, analysis must be performed in a black- | analysis in the context of mobile application security is |  |  |
| box setting. To address this, we integrated ACVTool [44] to | becoming increasingly evident. |  |  |
| enable runtime code coverage measurement. | Dynamic analysis tools can vary in their workflows, but |  |  |
| Section 4 explains how this study addresses the above | a common approach involves preprocessing the APK file |  |  |
| challenge and mitigates these constraints. This paper’s key | before performing dynamic analysis. Preprocessing allows |  |  |
| contributions are as follows: | the tool to capture runtime information, facilitating more |  |  |
| ∙ | Bridging a Research Gap | : This study is the first to | effective analysis. During the dynamic analysis process, |
| systematically evaluate the ability of dynamic analysis tools | researchers aim to trigger as many app functionalities as |  |  |
| to handle ARA techniques, thus filling a critical gap in the | possible to achieve a comprehensive evaluation. Researchers |  |  |
| existing literature. | can utilize automated tools such as Monkey [18], Delm [27], |  |  |
| ∙ | Large-Scale Dataset | : We have created a dataset con- | or Fastbot [36] to efficiently explore the app in an automated |
| sisting of 993 benign and 991 malicious applications, and | manner. In this paper, we focus on evaluating this type of |  |  |
| generated corresponding ARA analysis reports for each. | dynamic analysis tool. |  |  |

Our dataset, available at https://github.com/dfpp/Anti-ARA,

provides a valuable resource for future research.

Suo et al.: Preprint submitted to Elsevier Page 2 of 18

---

## Page 3

1 private String[] virtualPkgs = { ∙ Root Detection (RD) : In Android, "Rooting" is the

2 "com.bly.dkplat",

package names for detection

| 6 | String path = context.getFilesDir().getPath(); | Retrieves private file path |
| --- | --- | --- |
| 7 | for (String virtualPkg : virtualPkgs) { | Checks if private path contains |
| 11 | } | Triggers callback and returns |

true if a match is found

// Returns true if a known multiple app is detected.

15 return false;

16 }

Figure 1: A Motivating Example

2.2. Anti-Runtime Analysis Techniques

ARA techniques refer to a set of methods used in An-

droid applications to protect them from dynamic runtime

analysis attacks. These attacks involve analyzing the behav-

ior of the application during execution to identify vulnera-

bilities or extract sensitive information.

The emergence of these ARA techniques is driven by the

differing motivations of benign and malicious application

developers. Benign developers often use ARA technology

to safeguard their intellectual property, prevent reverse en-

gineering, and protect against unauthorized tampering. By

employing ARA technology, they can protect their code

from unauthorized analysis or modification.

Malicious developers, in contrast, exploit ARA tech-

nology to hide their malicious activities, evade detection

and countermeasures, and enhance the persistence of their

applications. The use of ARA technology hinders security

researchers and analysts from understanding application be-

havior and detecting malicious activities.

In this paper, we consider five types of ARA techniques:

∙ Anti-Debugging (AD) : Anti-Debugging is a technique

used to protect applications from reverse engineering at-

tacks [4]. This involves inserting anti-debugging code into

the application, making it difficult for analysts to use de-

application. Properly deploying anti-debugging techniques

can significantly enhance the security of the application,

reinforcing its resilience against malicious attacks [59].

∙ Anti-Hooking (AH) : Anti-Hooking refers to tech-

niques employed to prevent attackers from using hooking

technologies to monitor, modify, or tamper with the behavior

of an application, which could facilitate malicious attacks or

the theft of sensitive information [24]. Commonly used tools

include Xposed [46] and Frida [42].

cious attackers from modifying or repackaging applications.

Implementing such mechanisms protects apps from unau-

safeguarding security.

this information to decide whether to alter their behavior to

we present a code snippet in Figure 1 as a motivating

example, taken from a real-world application.

In this code fragment, the goal of the application is

to check whether the current runtime environment is an

application-level virtualization environment. Specifically,

the code achieves this by examining file paths. The basic idea

is that the host application redirects the client application’s

APK to its own directory when loading it. In line 6, the

application uses the getPath function to retrieve the path

to the application’s internal storage directory and checks

whether the path contains common package names asso-

ciated with multiple applications (lines 7-8). If a common

package name is detected, the application invokes a callback

function to perform the corresponding action (lines 9-11).

This detection method requires a pre-prepared list of known

application package names (lines 1-4).

ARA techniques are complex technologies with various

implementation methods. Here, due to space constraints, we

provide only a concise description of ARA technology. For

a more detailed explanation and technical implementation

of ARA technology, we refer readers to our paper [55],

which offers an in-depth analysis. Additionally, the corre-

sponding open-source project on GitHub can further aid in

understanding the practical aspects of ARA technology. By

combining the information from the paper and the project,

readers will gain a comprehensive understanding of ARA

techniques.

This study conducts a large-scale empirical evaluation

of dynamic analysis tools in the context of ARA techniques

used in Android applications. Our investigation is driven

by three research questions, each targeting a different as-

pect of the problem. These questions not only shape our

experimental design but also serve as a practical guide for

tool developers, application authors, and security analysts in

selecting or improving dynamic analysis strategies.

ARA technology?

widely adopted by both benign and malicious developers to

resist reverse engineering and hinder dynamic inspection. As

| 3 | "dkplugin.pke.nnp", | List of known | multiple | app | process of obtaining superuser privileges. With Root access, |
| --- | --- | --- | --- | --- | --- |
| // Package names of other known multiple app instances | users bypass system restrictions, modify settings, delete |  |  |  |  |
| 4 | }; | pre-installed apps, and install unverified ones [41]. Root |  |  |  |
| 5 | public boolean checkByPrivateFilePath(Context context, VirtualCheckCallback callback) { | detection helps apps identify rooted devices to take actions |  |  |  |
| 8 | if (path.contains(virtualPkg)) { | any known package names | ∙ | Virtual Environment Detection (VED) | : This tech- |
| 9 | if (callback != null) { | nique aims to detect if the application is running within a vir- |  |  |  |
| 10 | callback.findSuspect(); | tual environment [20, 49]. Malicious applications may use |  |  |  |
| return true; | evade detection [61, 1], while benign applications may check |  |  |  |  |
| 12 | } | for a virtual environment to confirm that the application is |  |  |  |
| 13 | } | running in a secure environment [31, 66, 26]. |  |  |  |
| 14 | // Returns false if no known multiple app is detected. | To facilitate a better understanding of ARA techniques, |  |  |  |
| buggers or other tools to debug and reverse-engineer the | 3. Research Questions |  |  |  |  |
| ∙ | Anti-Tampering (AT) | : Anti-Tampering prevents mali- | Q1: Can dynamic analysis tools effectively handle |  |  |
| thorized changes, ensuring security and integrity [8, 33, 47]. | Reasons. | In recent years, ARA techniques have been |  |  |  |
| Suo et al.: | Preprint submitted to Elsevier | Page 3 of 18 |  |  |  |

---

## Page 4

security analysts increasingly rely on dynamic analysis tools

to understand application behavior and uncover vulnerabil-

ities, it becomes essential to assess whether these tools are

capable of overcoming such protections.

Reasons. Dynamic analysis tools can be affected differ-

ently by various categories of ARA techniques, owing to

differences in design complexity, implementation maturity,

and runtime behavior. Some techniques (e.g., virtualization-

related checks) are lightweight and widely adopted, while

others (e.g., anti-hooking mechanisms) may be more com-

plex or less reliable in real-world deployment. It is therefore

necessary to analyze how categories and quantities of ARA

techniques influence a tool’s ability to explore application

behavior.

Objective. Q2 seeks to assess (i) how different categories

of ARA techniques affect dynamic analysis tools, and (ii)

how the quantity of deployed ARA techniques within an

APK impacts tool effectiveness.

tive helps prioritize mitigation strategies (e.g., more faithful

Q3: How efficient are dynamic analysis tools when

processing a large-scale dataset of applications pro-

tected by ARA techniques?

quent installation/launch success during analysis. For each

tools that remain practical under time constraints and op-

erational realities, and they guide tool developers to opti-

mize preprocessing steps and improve stability for large-

scale use. Together with RQ1 and RQ2, RQ3 complements

effectiveness-oriented findings with practical considerations

for real-world deployment.

Together, these three questions provide a comprehensive

framework for understanding the current capabilities and

limitations of dynamic analysis tools in ARA-aware environ-

ments. They also lay the foundation for future improvements

in tool design, application protection strategies, and analysis

methodology.

4. Study Methodology

the analysis process.

performance of these tools under controlled conditions, we

| Objective. | Q1 evaluates the ability of various dynamic | Reasons. | While resilience to ARA techniques is critical, |  |
| --- | --- | --- | --- | --- |
| analysis tools to mitigate or bypass ARA techniques during | efficiency | is equally important—especially when analyzing |  |  |
| analysis. | large-scale datasets comprising hundreds or thousands of |  |  |  |
| Method. | To ensure general applicability, especially in the | APKs. A tool that can bypass protections but fails to scale |  |  |
| context of closed-source tools, we use code coverage as the | efficiently becomes impractical in real-world workflows. |  |  |  |
| primary evaluation metric. Specifically, we compare cov- | Objective. | Assess the | efficiency and reliability | of rep- |
| erage between the original APKs (unprocessed) and those | resentative dynamic analysis tools on a large-scale dataset |  |  |  |
| instrumented by dynamic analysis tools. If a tool effectively | of ARA-protected apps, providing actionable guidance for |  |  |  |
| handles ARA logic, it should be able to increase coverage | time- and resource-constrained analysis settings. |  |  |  |
| relative to the original baseline. | Method. | We evaluate efficiency along two key axes. |  |  |
| Implication. | Q1 results guide dynamic analysis tool de- | (i) | Preprocessing (instrumentation) time | : the time required |
| velopers to identify current limitations and improve robust- | to modify each APK prior to execution, which can be- |  |  |  |
| ness. For security analysts, this information aids selecting | come a bottleneck at scale. (ii) | Validity and success rates | : |  |
| tools that deliver reliable results in real-world protected | whether instrumentation yields a valid APK (installable |  |  |  |
| application settings. | and executable on the analysis platform), and the subse- |  |  |  |
| Q2: What are the differences in the impact of var- | app–configuration, we perform three independent runs and |  |  |  |
| ious categories and quantities of ARA technology on | report averages to reduce variance. |  |  |  |
| dynamic analysis tools? | Implication. | The results help security analysts select |  |  |
| Method. | We categorize applications by the | type | and | This section outlines the methodology adopted for evalu- |
| number | of ARA methods they deploy, and then analyze the | ating the effectiveness of dynamic analysis tools in handling |  |  |
| resulting changes in | code coverage | under dynamic analysis. | Anti-Runtime Analysis (ARA) technologies. The core idea |  |
| In theory, more protections may enhance resistance but | behind our research is that dynamic analysis tools, by prepro- |  |  |  |
| also introduce runtime overhead or diminishing returns; we | cessing Android APKs, enhance the analyzability of the ap- |  |  |  |
| empirically examine these trade-offs by comparing coverage | plications and increase code coverage during analysis. This |  |  |  |
| distributions across categories and increasing counts of de- | is achieved by inserting monitoring and logging code into the |  |  |  |
| ployed methods. | APK, which alters the application’s original behavior, pre- |  |  |  |
| Implication. | The results reveal the relative impact of | venting it from detecting the debugging environment or other |  |  |
| specific ARA categories against current tools and the ef- | runtime anomalies. As a result, the application is unable to |  |  |  |
| fect of increasing protection quantity. For tool developers, | execute self-defense mechanisms, such as terminating itself |  |  |  |
| identifying which categories (e.g., VED) are most obstruc- | or disabling certain features, which would otherwise hinder |  |  |  |
| environment emulation). For security analysts, unexpectedly | Our approach begins with the selection of a dataset |  |  |  |
| low coverage can serve as a diagnostic signal of high-impact | of benign and malicious applications, followed by ARA |  |  |  |
| techniques, suggesting the need for alternative tools or man- | technology detection using ARAP. Next, we use ACVTool |  |  |  |
| ual intervention. For application developers, the findings | for code coverage measurement and conduct experiments |  |  |  |
| indicate which techniques most effectively hinder analysis, | using a modular evaluation framework to assess the capa- |  |  |  |
| informing more robust protection designs. | bilities of various dynamic analysis tools. By comparing the |  |  |  |
| Suo et al.: | Preprint submitted to Elsevier | Page 4 of 18 |  |  |

---

## Page 5

| aim to provide valuable insights into their effectiveness in | In this study, we adopt a systematic and representa- |
| --- | --- |
| counteracting ARA techniques. | tive categorization of ARA techniques guided by the Mo- |

bile Application Security Verification Standard (MASVS),

| 4.1. Study Subjects | whose resiliency requirements cover common runtime tam- |  |  |
| --- | --- | --- | --- |
| We first collected 1,000 benign applications and 1,000 | pering and anti-analysis mechanisms. Following these re- |  |  |
| malicious applications for constructing the dataset. To en- | quirements—and to make the taxonomy practical for large- |  |  |
| sure the reliability of the data, we obtained samples from | scale empirical evaluation—we consolidate the landscape |  |  |
| AndroZoo [2] and used the "vt_detection" values as the | into five representative categories (AD, AT, AH, RD, VED) |  |  |
| criterion to classify the samples as benign or malicious. | that are widely deployed in real-world apps and well sup- |  |  |
| AndroZoo is a renowned large-scale repository for collecting | ported by our detector. These five categories serve as the |  |  |
| and storing Android application samples, and it includes | basis for our measurements and analysis across the dataset. |  |  |
| a "vt_detection" value indicating how many antivirus pro- | To operationalize this classification, we employed ARAP [55] |  |  |
| grams flagged the app as malicious (not a percentage). In | for ARA detection. ARAP combines static and dynamic |  |  |
| this study, we considered an app with a "vt_detection" value | analysis to identify concrete ARA techniques via feature |  |  |
| of 0 as benign, while an app with a "vt_detection" value of 10 | matching. It maintains a list of 1,515 distinct features and |  |  |
| or more, indicating detection by over ten antivirus programs, | supports detection across the above five categories and 32 |  |  |
| was considered malicious. | finer-grained subcategories. This enables us to consistently |  |  |
| To ensure that our dataset reflects the most current real- | map observed defenses in APKs to the five-category taxon- |  |  |
| world scenarios and to optimize the performance of the | omy used throughout the paper. |  |  |
| dynamic analysis tools, we focused only on applications | Due to space limitations, the detailed implementation |  |  |
| from AndroZoo that were uploaded after 2020. This decision | and workflow of ARAP are provided in our prior work, |  |  |
| was made to capture more recent trends in app development | where extensive experiments demonstrate high detection |  |  |
| and malicious behavior. Furthermore, in this study, we aimed | accuracy. We also conducted a comparative analysis with |  |  |
| to construct a dataset as large as possible to reduce the impact | ATADetector [8]—the only other available tool in this |  |  |
| of randomness on our results. However, due to the high com- | area—and found that ARAP significantly outperforms ATADe- |  |  |
| putational and time overhead of dynamic analysis tasks, the | tector in overall detection performance. |  |  |
| dataset size had to be balanced against practical constraints. | The output of ARAP is a JSON report that records the |  |  |
| Specifically, we conducted 21 dynamic analysis runs for | various ARA techniques identified. This report allows for |  |  |
| each APK sample—covering six different analysis tools (see | easy identification of the number of different ARA tech- |  |  |
| Section 4.4 for details) plus one baseline, with three repeated | niques used in a specific APK. Based on the number of ARA |  |  |
| experiments for each (i.e., 6+1=7 configurations × 3 runs | techniques detected, we classified the APKs into four cate- |  |  |
| = 21 runs per APK). Given this substantial testing cost, it | gories: EASY (0 ARA techniques), NORMAL (1–5 ARA |  |  |
| was necessary to limit the overall dataset size. After careful | techniques), HARD (6–10 ARA techniques), and CHAL- |  |  |
| consideration, we settled on a dataset that balances coverage | LENGING (more than 10 ARA techniques). |  |  |
| and feasibility. | 4.3. Code Coverage Measurement |  |  |
| Additionally, to prevent potential contamination from | Another challenge faced in our research is achieving |  |  |
| outdated "vt_detection" values in AndroZoo, we re-scanned | reliable fine-grained code coverage measurement for closed- |  |  |
| all selected APKs using VirusTotal. This re-scanning pro- | source APKs when access to the source code is unavailable. |  |  |
| cess led to slight adjustments in the dataset, resulting in 993 | Achieving reliable code coverage in a black-box setting is a |  |  |
| benign applications and 991 malicious applications. While | non-trivial task. |  |  |
| we initially aimed for 1,000 applications in each category, | In our study, we utilized ACVTool [44] as the code |  |  |
| this adjustment was necessary to ensure the accuracy and | coverage detection tool. ACVTool measures fine-grained |  |  |
| reliability of the data. Given the large-scale nature of the | coverage for third-party Android applications by inserting |  |  |
| dataset and the rigorous testing procedures employed, our | probes into the smali representation of Dalvik bytecode, |  |  |
| dataset is among the largest used in dynamic analysis tool | supporting class-, method-, and instruction-level granular- |  |  |
| evaluations, especially in comparison to other similar stud- | ity. Following the tool authors’ recommendation, we adopt |  |  |
| ies. Ultimately, we utilized a dataset comprising 993 benign | the default | instruction-level | coverage and report instruction |
| applications and 991 malicious applications. | coverage in all our experiments. ACVTool can be integrated |  |  |

with any testing or dynamic analysis framework, which fits

| 4.2. ARA Technology Detection | our experimental pipeline. According to the original authors, |  |
| --- | --- | --- |
| Detecting the use of ARA technology in such a large- | ACVTool introduces negligible instrumentation overhead |  |
| scale dataset swiftly and accurately poses a significant chal- | and exhibits very high reliability. |  |
| lenge in this study. ARA technology encompasses a wide | Prior to conducting the experiments, we used ACVTool |  |
| range of types and complex implementations, making it a | to instrument all APKs to ensure that ACVTool could work |  |
| non-trivial task to conduct rapid and precise assessments. | properly on these APKs. The final instrumentation results, as |  |
| Suo et al.: | Preprint submitted to Elsevier | Page 5 of 18 |

---

## Page 6

Table 1 ① APK Instrumentation ④

ACVTool Instrumentation Results Dynamic Analyzer

| Benign | 86.3 | 857 |
| --- | --- | --- |
| Malicious | 76.5 | 758 |
| Tool | Year | Function |

DroidDissector 2023 Dynamic Behavior Capture

ESdroid 2023 Dynamic Slicing

4.4. Dynamic Analysis Tools

To conduct a comprehensive evaluation of dynamic anal-

ysis tools and ensure that we covered as many relevant

tools as possible, we performed searches using keywords

such as "Android," "Dynamic," "Analysis," and "Tool" in

well-known literature databases, including IEEE Xplore,

ACM Digital Library, Springer Link, and ScienceDirect.

Furthermore, we manually reviewed the papers to identify

those that included active tools, with particular attention to

the "Background" and "Related Work" sections to ensure no

relevant tools were overlooked.

As a result, we reviewed 58 articles published from

2012 to the present that discussed these tools, identifying 65

distinct tools. After this review, we attempted to replicate

the identified tools and excluded those that could not be

built due to issues such as lack of support, incomplete

build information, or incompatibility with our operational

analysis environment (Section 4.5). This process led to the

confirmation of 6 usable dynamic analysis tools, as shown in

Table 2. For transparency and reproducibility, we provide a

comprehensive list of all reviewed tools, including excluded

ones and reasons for exclusion, in our open-source reposi-

tory, along with detailed reasons for their exclusion.

∙ APIMonitor [17] inserts monitoring code into the

APK file. By running the repackaged APK, APIMonitor

can capture API call logs to understand the behavior of

the application. The analysis includes information on in-

bound/outbound network data, file read/write operations,

and activities such as sending messages and making calls.

Although APIMonitor was released in 2013, it remains

relevant to our study for several reasons. Firstly, we aimed

for a comprehensive review and analysis of dynamic analysis

tools, ensuring we did not overlook any potential tools that

might contribute to the current landscape. Secondly, API-

Monitor claims to fully consider backward compatibility,

Assistant

② Dynamic Analysis ⑥

Data Analyzer

Initializer

vides valuable insights into dynamic analysis, particularly in

terms of API-level monitoring.

actual phones, and without requiring the app’s source code.

∙ DroidCat [10] is a dynamic app classification tool

that uses a diverse set of dynamic features based on method

superior robustness compared to static methods and dynamic

approaches that rely on system calls.

∙ T-Recs [30] is a novel dynamic taint analyzer. It tracks

information flow by recording application bytecode-level

executions on Android devices and reconstructing the exe-

cutions on a server independent of specific Android versions

and devices.

∙ DroidDissector [37] is a tool for extracting static and

dynamic features. It aims to provide malware researchers

and analysts in the Android domain with an integrated tool

capable of extracting all commonly used features in Android

malware detection. Its dynamic analysis module analyzes the

complete behavior of applications by tracking system calls,

generated network traffic, API calls, and generated log files

used by the application.

∙ ESdroid [63] is a dynamic slicing technique that is

event-aware and suitable for Android applications. The nov-

elty of ESdroid lies in its combination of segment-based

incremental debugging and dynamic backward slicing to

narrow down the search space, thereby generating precise

slices for Android.

4.5. Evaluation Framework

To conduct our study, we developed a modular eval-

uation framework (Figure 2), consisting of four key com-

ponents: APK Instrumentation Assistant, Dynamic Analy-

sis Initializer, Dynamic Analyzer, and Data Analyzer. Our

framework is designed to be reusable and easily extendable,

allowing users to integrate new dynamic analysis tools for

performance assessment. In the spirit of transparency and

collaboration, we have decided to open-source this tool [14].

The framework is written in Python and consists of over

3,300 lines of code.

In our framework, there are two distinct paths, referred

to as Route 1 (2, 3, 4, 5, 6) and Route 2 (1, 4, 5, 6). This is

| Category | Success Rate (%) | Success Count | ③ | ⑤ |  |
| --- | --- | --- | --- | --- | --- |
| Overall | 81.4 | 1,615 | Figure 2: | Study Methodology |  |
| Table 2 | making it suitable for analyzing modern applications despite |  |  |  |  |
| Dynamic Analysis Tool Are Involved in This Study | its age. Thus, its inclusion in our study is justified, as it pro- |  |  |  |  |
| APIMonitor | 2013 | Dynamic Behavior Capture | ∙ | AndroidSlicer | [6] combines a novel asynchronous |
| AndroidSlicer | 2019 | Dynamic Slicing | slicing approach for modeling data and control dependencies |  |  |
| DroidCat | 2019 | Dynamic Behavior Capture | in the presence of callbacks with lightweight and precise |  |  |
| T-Recs | 2022 | Dynamic Taint Analysis | instrumentation; this allows slicing for apps running on |  |  |
| shown in Table 1, indicated that 81.4% of them were success- | calls and inter-component communication (ICC) Intents. |  |  |  |  |
| fully instrumented by ACVTool. We conducted subsequent | It does not rely on permissions, app resources, or system |  |  |  |  |
| experiments using these 1,615 instrumented APK files. | calls and can fully handle reflection. This approach achieves |  |  |  |  |
| Suo et al.: | Preprint submitted to Elsevier | Page 6 of 18 |  |  |  |

---

## Page 7

| because we want to demonstrate the capabilities of dynamic | environment. To achieve automated application exploration, |  |
| --- | --- | --- |
| analysis tools by comparing the changes in code coverage | we use the well-known automation testing tool Monkey [18]. |  |
| after processing the APK code through these tools. In Route | For each dynamic analysis, we use Monkey to randomly |  |
| 2, the APK is only processed by ACVTool, which serves | generate 50,000 events as input. For each APK file, we |  |
| as a baseline, reflecting code coverage achievable through | conduct 3 analyses and take the average of the 3 runs as |  |
| dynamic analysis without modifications to ARA techniques. | the final code coverage. After each dynamic analysis, we |  |
| In Route 1, the APK is first preprocessed by dynamic anal- | use snapshots to restore the emulator’s state to ensure the |  |
| ysis tools, which may bypass certain ARA techniques, thus | independence of each analysis. For each set of controlled |  |
| potentially resulting in higher code coverage. By comparing | experiments (Route 1 and Route 2), we used the same - |  |
| the difference in code coverage between Route 1 and Route | s parameter to generate identical event sequences, thereby |  |
| 2, we can evaluate the capabilities of dynamic analysis tools. | minimizing any bias introduced by the Monkey tool. |  |
| APK Instrumentation Assistant. | This module takes an | Furthermore, in this study, effective triggering of ARA |
| Android APK file as input, utilizing ACVTool to statically | techniques embedded in the APK is essential. Assuming |  |
| instrument the APK for the purpose of obtaining code cover- | that the ARA technology used in the APK is not triggered, |  |
| age during dynamic analysis. Additionally, in order to better | the research process becomes meaningless because it is |  |
| trigger ARA technology, the APK Instrumentation Assistant | equivalent to the APK not utilizing any ARA technology. |  |
| will add "android:debuggable="true"" to the APK’s mani- | To address this issue, we meticulously designed the dynamic |  |
| fest file, setting it as debuggable to trigger AD technology. | analysis environment in the Dynamic Analyzer to maximize |  |
| At the same time, the repackaged APK will help trigger the | the triggering of the ARA technology used in the applica- |  |
| AT technology. | tion. Specifically, in addition to using the emulator as the |  |
| Dynamic Analysis Initializer. | In Route 2, the APK | runtime environment to trigger VED technology, we also 1) |
| will first be processed by this module. This module invokes | set the emulator state to root to trigger RD technology; 2) |  |
| various dynamic analysis tools to preprocess the input APK | configure Xposed and Frida in the emulator to trigger AH |  |
| file and generate the processed APK file. We expect that the | technology. |  |
| APK, after being preprocessed by dynamic analysis tools, | Data Analyzer. | This module analyzes and aggregates |
| will have enhanced analyzability, thereby achieving higher | the results from both evaluation routes, storing them in a |  |
| code coverage. | CSV file and generating statistical reports. These reports |  |
| To further clarify this logic, when an APK is analyzed | enable users to easily assess and compare the performance |  |
| dynamically, the application may attempt to detect certain | of the dynamic analysis tools under evaluation. |  |
| runtime anomalies, such as the presence of debugging tools. | Based on the methods described above, we conducted |  |
| In its original state, upon detecting such anomalies, the | controlled experiments to assess the performance of various |  |
| application might take actions to prevent further analysis, | dynamic analysis tools in handling ARA techniques. In |  |
| such as displaying a message to the user and terminating the | the next section, we present and analyze the experimental |  |
| program, or restricting certain features to avoid detection. | results, focusing on key metrics such as code coverage and |  |
| These self-defense mechanisms limit the analysis process | efficiency, and examining how different ARA techniques |  |
| and result in lower code coverage. | impact dynamic analysis. |  |

However, when dynamic analysis tools preprocess the

| APK by inserting monitoring and logging code, they modify | 5. DATA ANALYSIS AND RESULTS |
| --- | --- |
| the application’s original behavior. This alteration reduces | In the previous section, we outlined the methodology |
| the application’s capacity to detect debugging environments | used to evaluate the effectiveness of dynamic analysis tools |
| or other runtime anomalies. Consequently, even if the ap- | in addressing Anti-Runtime Analysis (ARA) technologies. |
| plication recognizes an abnormal runtime environment, it | In this section, we present the results of the experiments |
| can no longer take defensive actions like terminating itself | based on the outlined methodology. Our focus is on key |
| or blocking certain functionalities. As a result, the instru- | metrics such as code coverage and the efficiency of dynamic |
| mented version of the APK becomes more analyzable, and | analysis tools. |
| a larger portion of the application’s functionality is explored | To carry out the experiments, we utilized four desktop |
| during testing, leading to higher code coverage compared to | computers for parallel analysis. Each system was equipped |
| the original APK. | with an Intel Xeon E-2224G processor and 16GB of mem- |
| This enhanced analyzability and increased code cov- | ory, running Android version 12 on the Android Virtual |
| erage in the instrumented APK are direct results of the | Device. The entire experiment was conducted over a span |
| dynamic analysis tools modifying the application’s logic, | of 3 months. The following subsections will present and |
| which prevents the application from evading analysis through | analyze the results obtained from these experiments. |

runtime detection mechanisms.

Q1: Can dynamic analysis tools effectively handle

Dynamic Analyzer. This module loads the input APK

ARA technology?

file into an emulator for dynamic analysis and utilizes ACV-

Tool to capture the corresponding code coverage. In this

In the first research question, we aim to evaluate the

study, we choose the Android Virtual Device as the emulator

ability of various dynamic analysis tools to handle ARA

Suo et al.: Preprint submitted to Elsevier Page 7 of 18

---

## Page 8

100%

80%

60%

40%

Coverage 20%

0

Original APIMonitor AndroidSlicer DroidCat T-Recs DroidDissector ESdroid

Tool

Figure 3: Code Coverage of the Malicious APKs

60%

40%

20%

Coverage

0

Original APIMonitor AndroidSlicer DroidCat T-Recs DroidDissector ESdroid

Tool

Figure 4: Code Coverage of the Benign APKs

| techniques from a holistic perspective. Ideally, such tools | benign APKs average 10.98 MB. To eliminate the impact |  |
| --- | --- | --- |
| should possess certain capabilities to mitigate the impact of | of resource files on size measurements, we calculated only |  |
| ARA techniques. Under Route 2—where no preprocessing | the size of the application code. |  |
| or instrumentation is applied—the APK under analysis re- | More critically, when comparing the "Original" baseline |  |
| tains all its ARA mechanisms, which can be triggered by our | to the results obtained after applying each dynamic analysis |  |
| specially crafted runtime environment. As a result, dynamic | tool (i.e., Route 2 vs. Route 1), we observe no significant |  |
| analysis under Route 2 generally yields lower code coverage | improvement in code coverage—regardless of whether the |  |
| due to the active ARA techniques. In contrast, Route 1 | APK is benign or malicious. This indicates that none of the |  |
| introduces preprocessing steps by the dynamic analysis tools | tested dynamic analysis tools effectively handle the ARA |  |
| prior to execution. This may neutralize or bypass some ARA | techniques deployed in these applications. It is this compar- |  |
| techniques, potentially resulting in higher code coverage | ison—between the tools-processed results and the baseline |  |
| under identical input conditions. | scenario—that leads us to conclude the current ineffective- |  |
| Figures 3 and 4 respectively illustrate the code coverage | ness of dynamic analysis tools in overcoming runtime ARA |  |
| during dynamic analysis of malicious and benign APKs. The | defenses. |  |
| results of six different dynamic analysis tools are compared | For malicious APKs, DroidCat and DroidDissector are |  |
| with the analysis results of the original, untreated APKs on | the two best-performing tools. However, "best-performing" |  |
| the same coordinate system, facilitating a clearer compari- | only means that their analysis results are closest to the orig- |  |
| son of the performance of each tool. The "Original" results in | inal results. The code coverage during dynamic analysis of |  |
| Figures 3 and 4 correspond to the experimental configuration | the APKs slightly decreased after being processed by these |  |
| described as Route 2 in Figure 2, where no preprocessing | tools. For the other four tools—APIMonitor, AndroidSlicer, |  |
| is performed and ARA techniques remain active during | T-Recs, and ESdroid—the code coverage during dynamic |  |
| execution. In the violin plots within Figures 3 and 4, the y- | analysis is significantly lower than that of the unprocessed |  |
| axis represents the code coverage achieved during dynamic | APKs. In particular, APIMonitor renders the processed APK |  |
| analysis, while the width of the violin plot indicates the | files nearly unanalyzable. |  |
| density of samples at a given coverage level. Note that the | The performance of the dynamic analysis tools on benign |  |
| filled area appearing below the axis in the violins does not | APKs was similarly disappointing, with no tool effectively |  |
| indicate negative coverage values; it is a rendering artifact | handling ARA techniques to improve code coverage during |  |
| caused by the presence of zero-coverage samples and the | dynamic analysis. However, unlike the results for malicious |  |
| polygon closure used by the plotting library. In all analy- | APKs, all the tools performed somewhat better when analyz- |  |
| ses, an app–tool configuration that fails to produce a valid | ing benign APKs. Among them, DroidDissector performed |  |
| run (instrumentation failure, install/startup crash, emulator | the best, with its code coverage nearly identical to the |  |
| deadlock/timeout) is assigned 0% coverage, reflecting the | original results. This was followed by T-Recs, which slightly |  |
| tool’s effective runtime visibility for that app. | reduced the APK’s code coverage. AndroidSlicer, DroidCat, |  |
| By comparing the results for benign and malicious | and ESdroid displayed similar performance, all significantly |  |
| APKs, we observe that malicious APKs achieve higher code | reducing the APK’s code coverage. Although APIMonitor |  |
| coverage than benign APKs when the same number of inputs | performed better on benign APKs than on malicious ones, |  |
| (50,000) are provided. This outcome is expected, given that | it still rendered most APKs unanalyzable, reducing the code |  |
| benign APKs typically possess broader functionality and | coverage to zero. |  |
| larger codebases, which result in lower code coverage during | The experimental results for Q1 were surprising. Not |  |
| dynamic analysis. Specifically, in our dataset, malicious | only did the code coverage during dynamic analysis of APKs |  |
| APKs have an average code size of 6.09 MB, whereas | processed by dynamic analysis tools fail to improve, but only |  |
| Suo et al.: | Preprint submitted to Elsevier | Page 8 of 18 |

---

## Page 9

Table 3

Paired Wilcoxon tests (tool vs. Original ) with Holm correction on benign and malicious datasets. The rank-biserial correlation

( 𝑟 ) indicates effect size (negative = lower coverage than baseline). All results are significant at 𝑝 holm < 0 . 05 .

Benign Dataset Malicious Dataset

Tool

| 𝑟 | 𝑝 | holm | Sig. | 𝑟 | 𝑝 | holm | Sig. |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| APIMonitor | −0 | . | 972 | 2 | . | 18 × 10 | −15 | TRUE | −0 | . | 991 | 1 | . | 30 × 10 | −16 | TRUE |
| AndroidSlicer | −0 | . | 778 | 4 | . | 25 × 10 | −12 | TRUE | −0 | . | 836 | 2 | . | 52 × 10 | −12 | TRUE |
| ESdroid | −0 | . | 758 | 7 | . | 10 × 10 | −12 | TRUE | −0 | . | 813 | 5 | . | 09 × 10 | −12 | TRUE |
| T-Recs | −0 | . | 721 | 3 | . | 85 × 10 | −10 | TRUE | −0 | . | 781 | 1 | . | 46 × 10 | −10 | TRUE |
| DroidCat | −0 | . | 503 | 1 | . | 09 × 10 | −6 | TRUE | −0 | . | 579 | 8 | . | 47 × 10 | −7 | TRUE |
| DroidDissecto | −0 | . | 235 | 3 | . | 55 × 10 | −2 | TRUE | −0 | . | 271 | 4 | . | 00 × 10 | −2 | TRUE |
| a few tools could ensure that code coverage during dynamic | differences from the baseline after Holm correction ( | 𝑝 | holm | < |  |  |  |  |  |  |  |  |  |  |  |  |
| analysis did not significantly decline. | 0 | . | 05 | ), with negative | 𝑟 | values for all tools, as summarized |  |  |  |  |  |  |  |  |  |  |
| Among all tools, APIMonitor demonstrated the poor- | in Table 3. This pattern indicates that, in general, dynamic |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| est performance. APKs processed by APIMonitor became | analysis tools achieved lower code coverage than the base- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| nearly unanalyzable. This poor performance is partly at- | line configuration, suggesting that ARA defenses remain |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tributable to the age of APIMonitor; it cannot effectively | effective in impeding runtime exploration. The effect sizes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| handle newer APK files. Although APIMonitor’s authors | were slightly stronger in the malicious dataset (e.g., | API- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| claim that it has some backward compatibility and can work | Monitor | : | 𝑟 | ≈ −0 | . | 99 | ; | AndroidSlicer | : | 𝑟 | ≈ −0 | . | 84 | ) than in the |  |  |
| on newer versions of Android, our experimental results | benign dataset (e.g., | APIMonitor | : | 𝑟 | ≈ −0 | . | 97 | ; | AndroidSlicer | : |  |  |  |  |  |  |
| indicate that it struggles to function effectively on more | 𝑟 | ≈ −0 | . | 78 | ), which aligns with the expectation that malicious |  |  |  |  |  |  |  |  |  |  |  |
| recent Android versions. | applications tend to implement more complex and aggres- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| DroidCat and DroidDissector, like APIMonitor, are Dy- | sive ARA protections. These results quantitatively confirm |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| namic Behavior Capture tools and were the best performers | the conclusions drawn from our coverage-based evaluation: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| on the malicious APK dataset. This suggests that, compared | existing dynamic analysis tools remain substantially limited |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| to other types of tools, these two were more designed with | in their ability to counter ARA mechanisms, particularly |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the analysis of malicious APKs in mind. DroidDissector also | when analyzing malware. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

performed well on the benign dataset, whereas DroidCat’s

Q1 Finding

performance declined on it. T-Recs, which is used for taint

| analysis, did not perform well on the malicious APK dataset, | We discovered that the existing dynamic analysis tools |
| --- | --- |
| indicating it is more suitable for analyzing benign APKs. | are generally ineffective at handling the ARA techniques |
| The two Dynamic Slicing tools, AndroidSlicer and ESdroid, | used in APKs. Among them, DroidDissector performed |
| performed poorly on the malicious APK dataset but showed | the best, with its results on both the benign and malicious |
| better results on the benign dataset, indicating they are more | datasets closely matching the original results. |

appropriate for analyzing benign APKs.

To further validate the robustness of our findings, we

| conducted paired Wilcoxon signed-rank tests to compare | Q2: What are the differences in the impact of var- |  |  |
| --- | --- | --- | --- |
| each dynamic analysis tool with the baseline ( | Original | ). | ious categories and quantities of ARA technology on |
| The Wilcoxon test was chosen over parametric alternatives | dynamic analysis tools? |  |  |

because code-coverage data are non-normally distributed,

| bounded within [0,1], and contain many zero values, making | In Question 2, we aim to explore how different types |  |  |
| --- | --- | --- | --- |
| non-parametric methods more appropriate and robust. Each | and quantities of ARA techniques impact the performance |  |  |
| test was performed on paired coverage values from the | of dynamic analysis tools, specifically their effectiveness in |  |  |
| same APK before and after instrumentation, ensuring direct | achieving code coverage. We begin by analyzing the impact |  |  |
| comparability. To account for multiple comparisons across | of ARA technique categories on dynamic analysis outcomes. |  |  |
| tools, we applied the Holm correction to control the family- | We combined the benign and malicious APK datasets |  |  |
| wise error rate while maintaining higher statistical power | from Question 1 and categorized them based on whether |  |  |
| than the Bonferroni adjustment. Additionally, we computed | they employed a specific category of ARA technique. In |  |  |
| the rank-biserial correlation ( | 𝑟 | ) as an effect-size measure, | other words, an APK that deploys multiple different cate- |
| which complements | 𝑝 | -values by indicating both the direction | gories of ARA techniques would be placed into multiple cat- |
| and magnitude of change. | egories. To assess the impact of ARA technology categories |  |  |
| We performed this statistical analysis separately on the | on code coverage during dynamic analysis, we focused on |  |  |
| benign and malicious datasets to account for potential be- | the five major categories into which ARAP divides ARA |  |  |
| havioral differences between the two categories. Across | techniques. |  |  |
| both datasets, all six tools exhibited statistically significant | Figure 5 presents our experimental results, with five |  |  |

subfigures displayed top to bottom, each showcasing the

Suo et al.: Preprint submitted to Elsevier Page 9 of 18

---

## Page 10

40% AD

20%

0

100% AH

80%

60%

40%

20%

0

AT

20%

Code Coverage 0

40% RD

20%

0

40% VED

20%

0

Figure 5:

| AH | 9.21 | 9.19 |
| --- | --- | --- |
| AT | 8.73 | 8.65 |

drawn some interesting conclusions.

environments and alter application behavior accordingly.

Conversely, tools achieved relatively higher code coverage

Code Coverage Rates for Different Categories of ARA techniques Tool

analysis.

ness of input event generation and the intrinsic variability

across application sets associated with each ARA technique.

As previously described in Section 4, the experimental de-

Monkey-generated events. This setup helps reduce the im-

categories.

| Original | APIMonitor | AndroidSlicer | DroidCat | T-Recs | DroidDissector | ESdroid |
| --- | --- | --- | --- | --- | --- | --- |
| Table 4 | on APKs deploying AH, with some samples even exceeding |  |  |  |  |  |
| Average Mean and Average Median of Code Coverage Rates | 90%. This may imply that AH, as implemented in these sam- |  |  |  |  |  |
| under Different Technologies | ples, is comparatively less effective in hindering dynamic |  |  |  |  |  |
| Technology | Average Mean (%) | Average Median (%) | It is important to note that dynamic analysis outcomes |  |  |  |
| AD | 8.61 | 8.66 | can be influenced by multiple factors, including the random- |  |  |  |
| RD | 8.43 | 8.45 | sign leverages a large-scale dataset of 1,615 applications, |  |  |  |
| VED | 7.49 | 7.47 | with each APK undergoing three independent runs of 50,000 |  |  |  |
| outcomes of APK datasets incorporating the AD, AH, AT, | pact of nondeterministic UI behavior and supports more sta- |  |  |  |  |  |
| RD, and VED techniques. By observing Figure 5 , we have | tistically robust comparisons across different ARA technique |  |  |  |  |  |
| To more intuitively demonstrate the impact of different | The relatively high coverage in AH-deploying apps may |  |  |  |  |  |
| categories of ARA techniques on code coverage, we calcu- | also reflect characteristics of real-world deployment: unlike |  |  |  |  |  |
| lated the average mean and average median values of the | other techniques, AH lacks formal mitigation support in |  |  |  |  |  |
| six tools under the influence of various ARA techniques | Android and is known for its implementation complexity, |  |  |  |  |  |
| (Table 4). In the table, the highest values for each metric are | which may limit its adoption or lead to inconsistent enforce- |  |  |  |  |  |
| highlighted in red, and the lowest values are highlighted in | ment. These factors collectively suggest that AH may be less |  |  |  |  |  |
| orange. In this document, subsequent tables also adhere to | reliably implemented in the wild, contributing to its limited |  |  |  |  |  |
| this convention. | efficacy in practice. In contrast, VED has been shown in prior |  |  |  |  |  |
| By comparing the experimental results of the original | research (e.g., ARAP) to be widely adopted—appearing in |  |  |  |  |  |
| APK set, we observed that dynamic analysis tools achieved | 92.6% of benign apps and 33.0% of malicious apps—likely |  |  |  |  |  |
| the lowest code coverage on APKs deploying VED tech- | due to its native support in the Android ecosystem. VED |  |  |  |  |  |
| niques among the five categories. This observation suggests | is also known to be adopted across a broad spectrum of |  |  |  |  |  |
| a potential association between VED and reduced code ex- | application domains, suggesting that the observed reduction |  |  |  |  |  |
| posure, possibly due to its ability to detect virtual execution | in code coverage is primarily attributable to the mechanism |  |  |  |  |  |
| Suo et al.: | Preprint submitted to Elsevier | Page 10 of 18 |  |  |  |  |

---

## Page 11

| Table 5 | Table 6 |
| --- | --- |
| Pairwise differences in median coverage between ARA cat- | Code Coverage Rates Under Different Difficulty Levels for the |
| egories using app-level cluster bootstrap (B=10,000). Stars | Original Apks |

reflect Holm-adjusted significance: *** 𝑝 < 0 . 001 , ** 𝑝 < 0 . 01 ,

AD–AT −0 . 18 [ −0 . 43 , 0.05] (n.s.) AT–VED 1.17 [0.89, 1.36] ∗∗∗

AT–AH 1.06 [0.75, 1.29] ∗∗∗ RD–VED 0.94 [0.71, 1.13] ∗∗∗

AT–RD 0.22 [0.05, 0.42] (n.s.)

of the VED technique itself rather than category-specific

application behaviors.

Moreover, it was observed that none of the samples in

the AT-deploying group exceeded 20% code coverage during

dynamic analysis. While multiple factors may contribute to

this result, one plausible explanation relates to the nature of

AT implementations. According to findings from ARAP, AT

techniques are often deployed using Android-supported offi-

cial mechanisms such as signature verification and installer

checks, which are typically executed at early stages of the

application lifecycle. This design increases the likelihood of

early application termination upon detection of tampering,

potentially limiting dynamic execution paths. Furthermore,

the widespread use of these standardized mechanisms may

discourage the adoption of more complex or customized AT

logic, reducing the chance that low code coverage results

from application complexity alone.

The AD and RD techniques demonstrated similar be-

havior, with most samples exhibiting coverage levels below

40%, suggesting that these mechanisms can also effectively

constrain dynamic code exploration, albeit to a lesser degree.

For various dynamic analysis tools, APIMonitor, An-

droidSlicer, DroidCat, and ESdroid show minimal differ-

ences in their performance across the five categories of ARA

techniques, without any of them exhibiting a clear inclina-

tion towards handling a particular category of technique. In

contrast, T-Recs and DroidDissector outperform the other

four tools but do not demonstrate a marked preference for

handling any specific category technique.

To formally support the observations in Table 4, we

performed an app-level cluster bootstrap (B=10,000): apps

were resampled with replacement, median coverage was

recomputed per category for each resample, and all pairwise

contrasts were formed; percentile 95% CIs and two-sided 𝑝 -

values were obtained from the empirical distributions with

Holm correction across the ten contrasts. As summarized

in Table 5, the contrasts that involve VED are consistently

significant and indicate lower median coverage for VED

than for the other categories, quantitatively reinforcing that

VED imposes the strongest resistance to dynamic analysis.

Among the remaining categories (AD/AT/AH/RD), pair-

wise differences are comparatively small; where significance

occurs, the effect sizes are modest and do not alter the

qualitative ordering shown in Table 4.

impact of the number of ARA techniques deployed on the

code coverage achievable during dynamic analysis. Figure 6

illustrates our experimental results. As described in Section

4.2, we categorized the APKs into four datasets—EASY,

NORMAL, HARD, and CHALLENGING—based on the

number of ARA techniques employed, with an increasing

number of techniques used for each subsequent category.

When discussing the impact of the number of ARA tech-

niques on the code coverage achievable during dynamic

analysis, we referred to the subcategory information from the

outputs of the ARAP tool, dividing ARA techniques into 32

subcategories. The distribution of samples across these four

subsets is as follows: EASY (22), NORMAL (730), HARD

(687), and CHALLENGING (176). The relatively small

number of EASY and CHALLENGING samples reflects an

earlier observation: few applications completely avoid ARA

techniques, particularly those released after 2020, while

excessive use of ARA techniques may negatively impact

application performance and user experience.

Table 6 presents various code coverage metrics for the

original dataset under different difficulty levels, including

the mean, median, first quartile, and third quartile. The

experimental results on the original dataset more accurately

reflect the impact of the number of ARA technology deploy-

ments on code coverage.

Combining the data from Figure 6 and Table 6, it can be

observed that the code coverage achieved by dynamic anal-

ysis tools decreases significantly as the number of deployed

ARA techniques in the target APK increases. The highest

values for all code coverage metrics appear in the EASY

dataset, while the lowest are found in the CHALLENGING

dataset. Additionally, as the difficulty level increases, each

metric shows a consistent downward trend. Table 6 further

illustrates that with each increase in difficulty level, the

coverage metrics decline markedly.

To evaluate whether application complexity—independent

of ARA techniques—could have contributed to the observed

differences, we also examined the average app size for each

category. The results show a gradual increase across the

four datasets: 8.35 MB (EASY), 8.65 MB (NORMAL),

8.97 MB (HARD), and 9.02 MB (CHALLENGING). While

app size does tend to increase alongside ARA deployment

level—possibly reflecting added complexity—the magni-

tude of increase is relatively minor. Notably, there is a clear

gap in code coverage between the EASY and NORMAL

categories, despite their similar average sizes. This suggests

| * | 𝑝 < | 0 | . | 05 | , (n.s.) not significant. | Metric (%) | EASY | NORMAL | HARD | CHALLENGING |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Non-VED contrasts | VED contrasts | Mean | 36.49 | 9.77 | 7.65 | 5.58 |  |  |  |  |  |  |  |  |
| Pair | Δ | median [pp] (95% CI) | Pair | Δ | median [pp] (95% CI) | Median | 38.11 | 12.32 | 8.34 | 5.65 |  |  |  |  |
| AD–AH | 0.87 [0.62, 1.05] | ∗∗∗ | AD–VED | 0.98 [0.75, 1.18] | ∗∗∗ | 1st Quartile | 12.58 | 8.12 | 5.51 | 3.65 |  |  |  |  |
| AD–RD | 0.02 [ | −0 | . | 13 | , 0.17] (n.s.) | AH–VED | 0.11 [0.03, 0.20] | ∗∗ | 4th Quartile | 94.55 | 14.71 | 9.75 | 7.29 |  |
| AH–RD | −0 | . | 83 | [ | −1 | . | 05 | , | −0 | . | 65 | ] | ∗∗∗ | In Question 2, the second aspect we need to discuss is the |
| Suo et al.: | Preprint submitted to Elsevier | Page 11 of 18 |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 12

EASY

100%

80%

60%

40%

20%

0

100% NORMAL

80%

60%

40%

20%

0

40% HARD

Code Coverage

20%

0

40%

CHALLENGING

20%

0

Figure 6:

that app size alone is unlikely to explain the observed

coverage degradation.

Based on the data from the charts, we believe that de-

ploying ARA technology at the NORMAL level or above can

effectively enhance an application’s resistance to dynamic

analysis, thereby ensuring runtime security. It should be

noted, however, that deploying too many ARA techniques

may introduce significant overhead, potentially degrading

the user experience. We will continue to investigate this issue

in future work to determine the optimal number of ARA

Furthermore, by observing the performance of various

dynamic analysis tools across different difficulty levels, we

These results highlight the varying resilience of existing

dynamic analysis tools under different protection levels, em-

phasizing the critical and practical need to carefully match

tool capabilities with the complexity of the target application

being analyzed.

Tool

Code Coverage Rates for Different Quantity of ARA techniques

Q2 Finding

We found that dynamic analysis tools were most severely

impacted by VED technology, resulting in the lowest

code coverage. In contrast, tools were least affected by

AH technology, allowing for relatively higher cover-

age.Additionally, the number of ARA techniques de-

ployed significantly impacts the code coverage achiev-

able during dynamic analysis.

tected by ARA techniques?

the time consumption during the preprocessing phase, which

serves as a direct indicator of a tool’s runtime performance.

The second is the success rate of preprocessing and installa-

tion; failure to produce a valid, executable output effectively

invalidates the analysis effort. Given the inherent time and

resource intensiveness of dynamic analysis—particularly on

| Original | APIMonitor | AndroidSlicer | DroidCat | T-Recs | DroidDissector | ESdroid |
| --- | --- | --- | --- | --- | --- | --- |
| deployments, aiming to achieve the best balance between | Q3: How efficient are dynamic analysis tools when |  |  |  |  |  |
| performance and security. | processing a large-scale dataset of applications pro- |  |  |  |  |  |
| have reached the following conclusions. APIMonitor is al- | In Question 3, we aim to assess the overall efficiency of |  |  |  |  |  |
| most ineffective on datasets of any level. Both AndroidSlicer | dynamic analysis tools when processing a large-scale dataset |  |  |  |  |  |
| and ESdroid demonstrate significant performance declines | of applications protected by ARA techniques. For example, |  |  |  |  |  |
| at the HARD level, which suggests that they are better | in our empirical study, each tool was executed on a dataset |  |  |  |  |  |
| suited for analyzing APKs at EASY and NORMAL levels. | comprising 1,615 APKs, which we consider representative |  |  |  |  |  |
| DroidCat shows a severe performance drop on the CHAL- | of a large-scale dynamic analysis scenario. This stands in |  |  |  |  |  |
| LENGING dataset, making it more suitable for analyzing | contrast to small-scale evaluations, where only a handful |  |  |  |  |  |
| APKs below the CHALLENGING level. In contrast, T-Recs | of selected samples are analyzed, and execution time or |  |  |  |  |  |
| and DroidDissector exhibit consistently stable performance | resource consumption may be less critical. |  |  |  |  |  |
| across APKs of all difficulty levels, with DroidDissector | The efficiency of each tool is evaluated from two key |  |  |  |  |  |
| showing particularly outstanding and reliable results. | aspects under large-scale analysis conditions. The first is |  |  |  |  |  |
| Suo et al.: | Preprint submitted to Elsevier | Page 12 of 18 |  |  |  |  |

---

## Page 13

Table 7

Average Pretreatment Time and Success Rate of Tools

Ben. Avg. Ben. Success Mal. Avg. Mal. Success Overall Avg. Overall Success

Tool

| Time (s) | Rate (%) | Time (s) | Rate (%) | Time (s) | Rate (%) |  |
| --- | --- | --- | --- | --- | --- | --- |
| APIMonitor | 3.26 | 86.1 | 5.43 | 72.3 | 4.34 | 79.2 |
| AndroidSlicer | 310.88 | 75.2 | 57.83 | 80.3 | 184.36 | 77.8 |
| DroidCat | 48.37 | 41.2 | 20.10 | 92.3 | 34.20 | 66.8 |
| T-Recs | 129.82 | 95.0 | 50.83 | 90.3 | 90.32 | 92.7 |
| DroidDissector | 25.23 | 100.0 | 9.20 | 99.5 | 17.22 | 99.8 |
| ESdroid | 327.16 | 75.5 | 58.56 | 80.3 | 192.85 | 77.9 |
| a large-scale dataset—tool scalability and stability become | emulator after being pre-processed by a dynamic analysis |  |  |  |  |  |
| essential factors influencing practical adoption and usability. | tool. Only APK files that are valid and usable for dynamic |  |  |  |  |  |
| While it is acknowledged that the tools listed in Table 2 | analysis are meaningful to researchers. Accordingly, this |  |  |  |  |  |
| serve different primary purposes, some—such as APIMoni- | metric serves as a critical indicator of tool efficiency. |  |  |  |  |  |
| tor, DroidCat, and DroidDissector—offer overlapping func- | Among them, APIMonitor achieved the lowest success |  |  |  |  |  |
| tionalities and are often employed in similar types of dy- | rate on both types of datasets, with an overall success rate |  |  |  |  |  |
| namic analysis workflows. Therefore, comparative insights | of only 20.5%. Apart from APIMonitor, AndroidSlicer and |  |  |  |  |  |
| regarding time efficiency and tool reliability remain valu- | ESdroid had the next lowest success rates, with success |  |  |  |  |  |
| able. For example, users can use this information to esti- | rates of only 56.8% and 63.9%, respectively. This means that |  |  |  |  |  |
| mate expected preprocessing time, assess the tool’s stability | approximately half of the APKs cannot be correctly used |  |  |  |  |  |
| across benign and malicious apps, and determine whether | for subsequent dynamic analysis, and the success rates of |  |  |  |  |  |
| the time cost is acceptable under constrained analysis sce- | these two tools differ significantly compared to others. Both |  |  |  |  |  |
| narios. These insights can support more informed decisions | AndroidSlicer and ESdroid had significantly lower success |  |  |  |  |  |
| regarding resource allocation and tool selection in practice. | rates on benign datasets compared to malicious datasets. |  |  |  |  |  |
| Moreover, identifying cases where a tool demonstrates | Among the benign datasets, DroidDissector achieved the |  |  |  |  |  |
| limitations—such as consistent preprocessing failures or | highest success rate at 87.6%. For the malicious datasets, T- |  |  |  |  |  |
| substantial delays—can inform both practical adjustments | Recs achieved the highest success rate, reaching an impres- |  |  |  |  |  |
| (e.g., pre-filtering samples) and future tool improvements. | sive 96.2%. Furthermore, T-Recs also had the highest overall |  |  |  |  |  |
| Thus, the evaluation not only benchmarks performance but | success rate among all the tools, with an overall success rate |  |  |  |  |  |
| also highlights actionable insights for users and developers | of 91.1%. |  |  |  |  |  |
| alike. | Considering the data presented in Table 7 and Table |  |  |  |  |  |
| Table 7 presents the time consumption of each tool | 8, T-Recs and DroidDissector demonstrate excellent overall |  |  |  |  |  |
| during the preprocessing phase and whether they can output | efficiency. For large-scale analysis datasets, researchers can |  |  |  |  |  |
| a APK file without errors during this phase. | prioritize using these two tools to enhance their research |  |  |  |  |  |
| Among the tools, APIMonitor achieved the shortest time | efficiency. |  |  |  |  |  |

consumption on both benign and malicious datasets, with

| an average time of 4.34 seconds. In contrast, ESdroid had | Q3 Finding |
| --- | --- |
| the highest time overhead, with an average time of 192.85 | APIMonitor is unable to effectively handle newer ver- |
| seconds on both types of datasets. Regarding preprocess- | sions of APK files, while the combined efficiency of T- |
| ing success rates, DroidCat had the lowest success rate on | Recs and DroidDissector makes them more suitable for |
| the benign dataset at only 41.2%, but its success rate on | large-scale datasets. |

the malicious dataset was 92.3%. This discrepancy may

be attributed to two possible explanations: one possibility

is that DroidCat, being a dynamic behavior capture tool,

| is more suited for malicious APKs; another possibility is | 6. DISCUSSION |  |
| --- | --- | --- |
| that DroidCat struggles with larger APK files. APIMonitor | Our research highlights the persistent and multifaceted |  |
| had the lowest preprocessing success rate on the malicious | challenges that developers of dynamic analysis tools face |  |
| dataset at 72.3%. On both types of datasets, DroidDissector | in effectively coping with ARA techniques widely de- |  |
| achieved the highest preprocessing success rate, with an | ployed in modern Android applications. The evaluation |  |
| average success rate of 99.8%. Specifically, DroidDissector | results underscore a critical and urgent gap: none of the |  |
| achieved a 100% preprocessing success rate on the benign | six tested tools—regardless of their intended analysis pur- |  |
| dataset. | pose—demonstrated sufficient capability to overcome ARA |  |
| In Table 8, the success rate indicates the probability that | techniques, in either benign or malicious apps. This limi- |  |
| an APK can be properly installed and run smoothly on an | tation holds even when applications are instrumented and |  |
| Suo et al.: | Preprint submitted to Elsevier | Page 13 of 18 |

---

## Page 14

| Table 8 | For malware analysts and forensic engineers, the im- |
| --- | --- |
| Installation and Operate Success Rate | plications are equally important. Our findings show that |

Ben. Success Mal. Success Overall Success

| T-Recs | 86.3 | 96.2 | 91.1 |
| --- | --- | --- | --- |
| DroidDissector | 87.6 | 90.7 | 89.1 |
| ESdroid | 40.4 | 86.1 | 63.9 |

mechanisms like AH. Strategic selection is essential to main-

taining usability while enhancing security.

existing dynamic analysis tools fail to automatically bypass

and effort, thereby increasing the barrier to scalable analysis.

Even the best-performing tool in our evaluation, DroidDis-

sector, while demonstrating relatively better code coverage

and runtime performance, still struggled to overcome ARA

| Tool | ARA protections, regardless of application type or tool |  |  |  |
| --- | --- | --- | --- | --- |
| Rate (%) | Rate (%) | Rate (%) | design. In practice, this necessitates manual intervention in |  |
| APIMonitor | 25.1 | 14.9 | 20.5 | many cases—such as altering the execution environment, |
| AndroidSlicer | 36.3 | 76.1 | 56.8 | disabling protection routines, or manually patching out ob- |
| DroidCat | 77.2 | 89.1 | 85.4 | fuscation logic. These tasks demand considerable expertise |
| analyzed under favorable conditions (Route 1), indicating | techniques when multiple layers were deployed. |  |  |  |
| a systemic shortcoming in current dynamic analysis infras- | Although our evaluation primarily used code coverage |  |  |  |
| tructures. | as a proxy for dynamic analysis effectiveness, which does |  |  |  |
| From a technical standpoint, different ARA categories | not fully represent a tool’s total functionality (e.g., behav- |  |  |  |
| vary significantly in effectiveness. Among the five ARA | ior monitoring, network tracing, or anomaly detection), it |  |  |  |
| types we examined, VED exhibited the strongest resistance | remains a critical baseline indicator. Given the diverse pur- |  |  |  |
| to dynamic analysis. In contrast, AH techniques had the | poses of the tested tools, achieving uniform evaluation re- |  |  |  |
| weakest practical impact—some failed to activate even un- | mains difficult. Nonetheless, their collective failure to re- |  |  |  |
| der controlled analysis conditions. This discrepancy is ex- | spond effectively to ARA techniques exposes a common |  |  |  |
| plainable by deployment context and ecosystem support: | weakness that limits the practical utility of dynamic analysis |  |  |  |
| VED enjoys official support from Android, which ensures | in modern software environments. |  |  |  |
| standardized implementation and stable behavior. This ad- | In light of these observations, it is imperative that future |  |  |  |
| vantage is reflected in its real-world prevalence: 92.6% of | development of dynamic analysis tools emphasize robust, |  |  |  |
| benign applications and 33.0% of malicious applications in | modular support for ARA detection and mitigation. The |  |  |  |
| our dataset implemented VED techniques. AH lacks any | limitations exposed in our evaluation indicate that tradi- |  |  |  |
| platform-level support and involves higher implementation | tional models of behavior capture—typically built around |  |  |  |
| complexity, which likely limits its deployment and reliabil- | system call tracing, API monitoring, and surface-level in- |  |  |  |
| ity. These observations suggest that in-the-wild defensive | strumentation—are insufficient in environments where ARA |  |  |  |
| strength of AH may be substantially less than anticipated. | techniques have become both prevalent and increasingly |  |  |  |
| Another key finding relates to the quantity of deployed | sophisticated. Instead, dynamic analysis tools must evolve |  |  |  |
| ARA techniques. Applications that implemented even a | into flexible, extensible frameworks that can adapt to diverse |  |  |  |
| small number of ARA measures showed marked increases | protection strategies, actively detect signs of anti-analysis |  |  |  |
| in analysis resistance. The most pronounced decline in code | behavior, and respond with effective countermeasures. |  |  |  |
| coverage occurred when comparing applications with zero | Rather than relying solely on runtime observation, future |  |  |  |
| ARA techniques to those with 1–5 techniques. While further | tools should adopt hybrid analysis paradigms, integrating |  |  |  |
| increasing the number of techniques (beyond five) continued | static and dynamic techniques in a coordinated manner. |  |  |  |
| to suppress coverage, the marginal benefit diminished. This | Static analysis can play a key role in identifying potentially |  |  |  |
| observation suggests that deploying a moderate number | protected regions, opaque predicates, or environmental de- |  |  |  |
| (1–5) of carefully selected ARA techniques strikes an effec- | pendency checks that may hinder execution. When com- |  |  |  |
| tive balance between protection and runtime performance, | bined with dynamic execution, this hybrid approach enables |  |  |  |
| thus serving as a practical guideline for developers balancing | more targeted and efficient exploration of program logic. |  |  |  |
| security and performance. | For instance, static control-flow graph (CFG) extraction |  |  |  |
| From the standpoint of benign developers, these find- | can help isolate code blocks likely to be guarded by ARA |  |  |  |
| ings highlight ARA techniques’ dual impact. On one hand, | techniques, guiding the dynamic engine to focus inputs or |  |  |  |
| ARA implementation significantly hinders code inspection, | emulate specific runtime conditions. This not only improves |  |  |  |
| providing crucial protection for intellectual property and | code coverage but also reduces the time required for com- |  |  |  |
| helping mitigate reverse engineering–based vulnerabilities. | prehensive behavior extraction. |  |  |  |
| On the other hand, overuse of such techniques introduces | Another promising direction lies in the integration of |  |  |  |
| non-trivial runtime overhead, which may impair applica- | lightweight machine learning (ML) models. These models |  |  |  |
| tion responsiveness and user experience. Developers should | can be trained to recognize patterns of code obfuscation, |  |  |  |
| therefore adopt a targeted deployment strategy—prioritizing | behavioral anomalies, or unusual branching behavior indica- |  |  |  |
| highly effective, low-overhead techniques such as VED, and | tive of ARA routines. During runtime, ML-assisted detec- |  |  |  |
| carefully evaluating trade-offs introduced by more complex | tion can trigger adaptive behaviors in the analysis tool—such |  |  |  |
| Suo et al.: | Preprint submitted to Elsevier | Page 14 of 18 |  |  |

---

## Page 15

| as toggling instrumentation strategies, injecting crafted en- | took three months. Additionally, to reduce potential dataset |
| --- | --- |
| vironment variables, or applying symbolic execution selec- | contamination caused by outdated vt_detection values in |
| tively. These capabilities allow the tool to move beyond | AndroZoo, we re-scanned all samples using VirusTotal to |
| reactive tracing and toward proactive analysis, anticipating | ensure the reliability of the dataset. |
| and preempting ARA-based disruptions. | Internal validity threats relate to the reliability and ef- |
| Equally essential is enhancing execution environments. | fectiveness of the measurement tools used. In this study, |
| Configurable sandboxes must be designed to simulate a | we measured code coverage using ACVTool. Given the |
| wide variety of device states, system contexts, and user | challenges of measuring fine-grained coverage in closed- |
| behaviors, since many ARA techniques rely on environment | source applications, the coverage results obtained may carry |
| checks to detect emulation or instrumentation. By providing | inherent biases, which are difficult to eliminate. Neverthe- |
| fine-grained control over runtime parameters—including OS | less, we believe these limitations do not hinder our ability to |
| properties, sensor states, installed apps, or even execution | derive meaningful qualitative conclusions. |
| timing—future tools can more effectively bypass or neutral- | Furthermore, in our current implementation, ARAP |
| ize ARA checks. Additionally, advanced sandboxes should | computes the presence of different types of ARA techniques |
| support real-time memory inspection, API call interception, | per APK, but does not count the number of times each |
| and function hooking, allowing analysts to surgically inter- | technique is applied across different locations in the code. |
| vene in execution when necessary. | Repeated application of the same ARA technique across |
| To ensure that research progress is sustainable and mea- | multiple code locations may increase analysis complexity. |
| surable, the field must also prioritize the establishment of | However, due to ARAP’s current limitations, reliably detect- |
| standardized evaluation benchmarks and annotated datasets. | ing multiple instances of the same ARA technique remains a |
| These resources should include applications embedded with | challenge. We consider this a limitation and plan to enhance |
| diverse and well-documented ARA techniques, enabling | the granularity of ARAP’s detection in future work to better |
| comparative evaluation of tool effectiveness. Without such | address this issue. |

shared infrastructure, it is difficult to gauge improvements,

identify persistent blind spots, or promote reproducible re-

8. Related Work

search across the community.

| Finally, dynamic analysis advancement must coordinate | To orient the reader, we organize prior work into four |  |  |
| --- | --- | --- | --- |
| closely with reverse engineering, automated deobfuscation, | complementary strands that move from broad characteri- |  |  |
| and adversarial modeling. These subfields offer comple- | zation to concrete countermeasures: (1) | surveys and tax- |  |
| mentary techniques—binary diffing, symbolic reasoning, | onomies of Android security tooling | , (2) | empirical compar- |
| fuzzing—to enhance ARA-aware analysis. Future tools need | isons of analysis tools | , (3) | studies of resilience to code trans- |
| analytical power and adaptive intelligence, learning from | formations (e.g., obfuscation/anti-analysis) | , and (4) | run- |
| failures and evolving with targeted defenses. | time approaches that attempt to counter ARA techniques | . |  |
| In a software ecosystem where ARA techniques are no | Across these strands, most existing work either focuses on |  |  |
| longer exceptional but expected, the survival and utility of | static analysis or does not evaluate contemporary | dynamic |  |
| dynamic analysis depend on its ability to keep pace. By | analysis tools under real-world anti–runtime-analysis (ARA) |  |  |
| embracing hybrid architectures, intelligent automation, en- | defenses. Our study fills this gap by providing a large- |  |  |
| vironment simulation, and collaborative benchmarking, the | scale, tool-centric empirical evaluation of dynamic analysis |  |  |
| next generation of dynamic analysis tools can re-establish | tools confronted with diverse ARA categories, quantifying |  |  |
| their relevance as essential instruments in the ongoing battle | runtime visibility (coverage) and practical efficiency at scale. |  |  |
| between software protection and security analysis. | (1) Summarizing and categorizing tool features. | Several |  |

studies systematically catalog and compare features of An-

droid security tools. Daoudi et al. [13] evaluate state-of-

7. THREATS TO VALIDITY

the-art malware detection methods and discuss strategies for

| External validity threats concern the generalizability of | combining them to improve detection rates. Heid and Heider |  |
| --- | --- | --- |
| our experimental results. The findings of this study are based | [25] summarize characteristics of vulnerability detection |  |
| on application samples obtained from AndroZoo. However, | tools with an emphasis on usability, and Baheux et al. [7] |  |
| due to the limited number of analyzed applications and their | analyze a large body of research from top venues to assess |  |
| market distribution, this research may not fully represent the | tool usability. |  |
| entire Android application ecosystem. To mitigate this, we | These studies offer a crucial foundational overview of |  |
| attempted to acquire and analyze as many applications as | the tooling landscape, aiding researchers and practitioners |  |
| possible to enhance the universality of the results. Large- | in understanding available options. However, their primary |  |
| scale dynamic analysis is highly time-consuming; in our | focus remains on theoretical feature comparison and high- |  |
| work, we performed multiple analyses on each APK file, | level usability, and they do not include empirical evalu- |  |
| with each analysis taking approximately 10 minutes. Despite | ations of how these tools perform under real-world con- |  |
| these constraints, our dataset includes 993 benign and 991 | straints.Specifically, they lack experimental data on a critical |  |
| malicious applications, and the complete analysis process | practical challenge: the tools’ resilience against widespread |  |
| Suo et al.: | Preprint submitted to Elsevier | Page 15 of 18 |

---

## Page 16

| ARA techniques. Our work seeks to build upon this foun- | techniques, moving beyond obfuscation to provide a holistic |
| --- | --- |
| dational research by providing a comprehensive empirical | view of their defensive capabilities. |

assessment that quantifies tool effectiveness and efficiency

(4) Addressing new attempts to counter ARA techniques.

when confronted with such protections.

A final strand proposes runtime mechanisms to tame or

| (2) Measuring tool performance through experiments. | bypass ARA defenses. Wang et al. [61] present Droid- |  |  |
| --- | --- | --- | --- |
| A second line of work performs controlled, head-to-head | AntiRM, which detects anti-analysis checks and manipu- |  |  |
| comparisons of analysis tools, most often in | static | set- | lates bytecode to force specific runtime behaviors. Tang et |
| tings. Zhang et al. [68] provide a comprehensive, con- | al. [58] introduce Dual-Force, simultaneously forcing Java |  |  |
| trolled, and independent comparison of three prominent | and JavaScript (WebView) execution paths to expose hidden |  |  |
| static analysis tools for information-flow (pollution): Flow- | payloads without manual input. Wang et al. [60] propose |  |  |
| Droid [5], Amandroid [62], and DroidSafe [19]. Ranganath | DirectDroid, which enhances fuzzing via on-demand en- |  |  |
| et al. [45] evaluate Android vulnerability detection tools | forcement to bypass checks and redirect execution to target |  |  |
| using the Ghera benchmark (considering 64 tools, assessing | locations. |  |  |
| 14). Bonett et al. [9] systematically evaluate static tools | These studies provide valuable conceptual frameworks |  |  |
| to discover, document, and fix defects, showing defect | and pave the way for future research. However, a significant |  |  |
| propagation across derivatives. Pauck et al. [43] intro- | barrier to practical adoption and independent validation |  |  |
| duce BareDroid/ReproDroid to enable accurate comparisons | exists: the tools themselves are not publicly available. The |  |  |
| among six information-flow tools (Amandroid [62], DIAL- | lack of open-source implementations or readily deployable |  |  |
| Droid [15], DidFail [52], DroidSafe [19], FlowDroid [5], | systems makes it difficult to benchmark these novel ap- |  |  |
| IccTA [32]). Aloraini et al. [3] study six static tools for | proaches against existing tools or to integrate their insights |  |  |
| buffer-overflow detection and report limited effectiveness for | into practical workflows. Our future work aims to reconstruct |  |  |
| advanced FOSS tools. | these tools to facilitate continued research progress. |  |  |
| These studies have established a strong methodological | In contrast to prior surveys, static-focused benchmarks, |  |  |
| foundation for the empirical assessment of analysis tools. | and obfuscation-centric or non-public counter-ARA pro- |  |  |
| However, their focus has been predominantly confined to the | posals, our work provides the first large-scale, tool-centric |  |  |
| domain of static analysis. Furthermore, these evaluations are | assessment of contemporary dynamic analysis tools con- |  |  |
| conducted from a traditional perspective, assessing tools un- | fronted with diverse ARA categories, measuring both run- |  |  |
| der ideal conditions rather than against the sophisticated and | time coverage (visibility) and practical efficiency across |  |  |
| widespread ARA techniques deployed in modern applica- | thousands of runs. |  |  |

tions. Consequently, it remains unclear how well these tools,

and particularly dynamic analysis tools which are renowned

9. CONCLUSION

for their accuracy but are also highly susceptible to runtime

| environments, would perform when such protections are | In this study, we conducted an initial evaluation of ex- |
| --- | --- |
| present. Our work directly addresses this gap by conducting | isting Android dynamic analysis tools in handling ARA |
| the first large-scale empirical evaluation of dynamic analysis | techniques, using code coverage as the primary assessment |
| tools specifically under the challenge of ARA techniques. | metric. This research addresses a notable gap in the literature |

on ARA techniques and dynamic analysis tools, offering

| (3) Evaluating the ability of tools to counter code trans- | valuable insights to guide the future development of secu- |  |
| --- | --- | --- |
| formations. | A third strand investigates how obfuscation or | rity protection technologies. Our findings reveal that while |
| related transformations affect analysis or detection quality. | current dynamic analysis tools fall short in addressing ARA |  |
| Hammad et al. [22] conduct a large-scale empirical study | techniques, they exhibit promising potential for enhance- |  |
| showing that code obfuscation significantly impacts Android | ment. Future work may explore approaches to improve the |  |
| anti-malware products. Soi et al. [54] propose a visibility | adaptability of dynamic analysis tools to ARA techniques |  |
| metric to assess the difficulty of detecting non-operational | and enhance their practical effectiveness. Overall, this study |  |
| code (e.g., NOPs) and discuss the stealthiness of evasive | deepens our understanding of Android application security |  |
| applications. Nawaz et al. [39] evaluate anti-malware tools | and anti-analysis mechanisms, contributing meaningfully to |  |
| under complex hybrid obfuscation and observe substantial | both academic research and real-world security practices. |  |

effects on detection rates.

These studies have established rigorous methodologies

| for evaluating tool resilience against code transformations | Acknowledgements |  |
| --- | --- | --- |
| and yielded valuable insights into obfuscation’s impact on | The authors would like to thank the anonymous review- |  |
| static analysis. However, their scope remains limited to | ers for their valuable comments and helpful suggestions. |  |
| static analysis and malware detection, with the broader spec- | We acknowledge the support received from the National |  |
| trum of ARA techniques that threaten dynamic analysis | Natural Science Foundation of China (No. 62472234, No. |  |
| still largely unexplored. Our work extends this important | 62372245), and the Natural Science Foundation of Xinjiang |  |
| research direction by conducting a comprehensive evalua- | Uygur Autonomous Region, China under the grant number |  |
| tion of dynamic analysis tools against a wide range of ARA | of 2024D01A55. |  |
| Suo et al.: | Preprint submitted to Elsevier | Page 16 of 18 |

---

## Page 17

References [19] Gordon, M.I., Kim, D., Perkins, J.H., Gilham, L., Nguyen, N., Rinard,

M.C., 2015. Information flow analysis of android applications in

| [1] | Afonso, V.M., Kalysch, A., Müller, T., Oliveira, D., Grégio, A.R.A., | droidsafe., in: NDSS, p. 110. |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| de Geus, P.L., 2018. Lumus: Dynamically uncovering evasive android | [20] | Guerra-Manzanares, A., Bahsi, H., Nõmm, S., 2019. Differences in |  |  |  |  |  |  |  |
| applications, in: Information Security Conference. | android behavior between real device and emulator: A malware de- |  |  |  |  |  |  |  |  |
| [2] | Allix, K., Bissyandé, T.F., Klein, J., Traon, Y.L., 2016. | Androzoo: | tection perspective. 2019 Sixth International Conference on Internet |  |  |  |  |  |  |
| Collecting millions of android apps for the research community. 2016 | of Things: Systems, Management and Security (IOTSMS) , 399–404. |  |  |  |  |  |  |  |  |
| IEEE/ACM 13th Working Conference on Mining Software Reposito- | [21] | Guo, R., Liu, Q., Zhang, M., Hu, N., Lu, H., 2022. A survey of obfus- |  |  |  |  |  |  |  |
| ries (MSR) , 468–471. | cation and deobfuscation techniques in android code protection. 2022 |  |  |  |  |  |  |  |  |
| [3] | Aloraini, B., Nagappan, M., 2017. Evaluating state-of-the-art free and | 7th IEEE International Conference on Data Science in Cyberspace |  |  |  |  |  |  |  |
| open source static analysis tools against buffer errors in android apps, | (DSC) , 40–47. |  |  |  |  |  |  |  |  |
| in: 2017 IEEE International Conference on Software Maintenance and | [22] | Hammad, M., Garcia, J., Malek, S., 2018a. A large-scale empirical |  |  |  |  |  |  |  |
| Evolution, ICSME 2017, Shanghai, China, September 17-22, 2017, | study on the effects of code obfuscations on android apps and anti- |  |  |  |  |  |  |  |  |
| IEEE Computer Society. pp. 295–306. | URL: | https://doi.org/10. | malware products, in: Chaudron, M., Crnkovic, I., Chechik, M., |  |  |  |  |  |  |
| 1109/ICSME.2017.77 | , doi: | 10.1109/ICSME.2017.77 | . | Harman, M. (Eds.), Proceedings of the 40th International Conference |  |  |  |  |  |
| [4] | Apostolopoulos, T.K., Katos, V., Choo, K.R., Patsakis, C., 2021. | on Software Engineering, ICSE 2018, Gothenburg, Sweden, May 27 |  |  |  |  |  |  |  |
| Resurrecting anti-virtualization and anti-debugging: Unhooking your | - June 03, 2018, ACM. pp. 421–431. URL: | https://doi.org/10.1145/ |  |  |  |  |  |  |  |
| hooks. Future Gener. Comput. Syst. 116, 393–405. | 3180155.3180228 | , doi: | 10.1145/3180155.3180228 | . |  |  |  |  |  |
| [5] | Arzt, S., Rasthofer, S., Fritz, C., Bodden, E., Bartel, A., Klein, J., | [23] | Hammad, M.M., Garcia, J., Malek, S., 2018b. | A large-scale em- |  |  |  |  |  |
| Le Traon, Y., Octeau, D., McDaniel, P., 2014. | Flowdroid: Precise | pirical study on the effects of code obfuscations on android apps |  |  |  |  |  |  |  |
| context, flow, field, object-sensitive and lifecycle-aware taint analysis | and anti-malware products. | 2018 IEEE/ACM 40th International |  |  |  |  |  |  |  |
| for android apps. ACM sigplan notices 49, 259–269. | Conference on Software Engineering (ICSE) , 421–431URL: | https: |  |  |  |  |  |  |  |
| [6] | Azim, T., Alavi, A., Neamtiu, I., Gupta, R., 2019. Dynamic slicing for | //api.semanticscholar.org/CorpusID:46848460 | . |  |  |  |  |  |  |
| android. 2019 IEEE/ACM 41st International Conference on Software | [24] | Haupert, V., Maier, D., Schneider, N., Kirsch, J., Müller, T., 2018. |  |  |  |  |  |  |  |
| Engineering (ICSE) , 1154–1164URL: | https://api.semanticscholar. | Honey, i shrunk your app security: The state of android app hardening, |  |  |  |  |  |  |  |
| org/CorpusID:174800284 | . | in: International Conference on Detection of intrusions and malware, |  |  |  |  |  |  |  |
| [7] | Baheux, I., Aktouf, O.E.K., Tebib, M.E.A., Graa, M., André, P., | and vulnerability assessment. |  |  |  |  |  |  |  |
| Ledru, Y., 2023. Droidsectester: Towards context-driven modelling | [25] | Heid, K., Heider, J., 2021. | Automated, dynamic android app vul- |  |  |  |  |  |  |
| and detection of android application vulnerabilities. | 2023 IEEE | nerability and privacy leak analysis: Design considerations, required |  |  |  |  |  |  |  |
| 34th International Symposium on Software Reliability Engineering | components and available tools. | Proceedings of the 2021 Euro- |  |  |  |  |  |  |  |
| Workshops (ISSREW) , 136–141URL: | https://api.semanticscholar. | pean Interdisciplinary Cybersecurity Conference URL: | https://api. |  |  |  |  |  |  |
| org/CorpusID:264976950 | . | semanticscholar.org/CorpusID:244480691 | . |  |  |  |  |  |  |
| [8] | Berlato, S., Ceccato, M., 2020. A large-scale study on the adoption | [26] | Hong, Y., Hu, Y., Lai, C.M., Wu, S.F., Neamtiu, I., Mcdaniel, P., Yu, |  |  |  |  |  |  |
| of anti-debugging and anti-tampering protections in android apps. J. | P.L., Çam, H., Ahn, G.J., 2017. Defining and detecting environment |  |  |  |  |  |  |  |  |
| Inf. Secur. Appl. 52, 102463. | discrimination in android apps, in: Security and Privacy in Commu- |  |  |  |  |  |  |  |  |
| [9] | Bonett, R., Kafle, K., Moran, K., Nadkarni, A., Poshyvanyk, D., 2018. | nication Networks. |  |  |  |  |  |  |  |
| Discovering flaws in security-focused static analysis tools for android | [27] | Hu, H., Wang, H., Dong, R., Chen, X., Chen, C., 2024. Enhancing |  |  |  |  |  |  |  |
| using systematic mutation, in: Enck, W., Felt, A.P. (Eds.), 27th | GUI exploration coverage of android apps with deep link-integrated |  |  |  |  |  |  |  |  |
| USENIX Security Symposium, USENIX Security 2018, Baltimore, | monkey. ACM Trans. Softw. Eng. Methodol. 33, 163. URL: | https: |  |  |  |  |  |  |  |
| MD, USA, August 15-17, 2018, USENIX Association. pp. 1263– | //doi.org/10.1145/3664810 | , doi: | 10.1145/3664810 | . |  |  |  |  |  |
| 1280. | URL: | https://www.usenix.org/conference/usenixsecurity18/ | [28] | Huang, W., Dong, Y., Milanova, A.L., 2014. Type-based taint analysis |  |  |  |  |  |
| presentation/bonett | . | for java web applications, in: Fundamental Approaches to Software |  |  |  |  |  |  |  |
| [10] | Cai, H., Meng, N., Ryder, B.G., Yao, D., 2019. Droidcat: Effective | Engineering. |  |  |  |  |  |  |  |
| android malware detection and categorization via app-level profiling. | [29] | IDC, 2024. | Smartphone market share. | https://www.idc.com/promo/ |  |  |  |  |  |
| IEEE Transactions on Information Forensics and Security 14, 1455– | smartphone-market-share | . |  |  |  |  |  |  |  |
| 1470. URL: | https://api.semanticscholar.org/CorpusID:54092966 | . | [30] | Inayoshi, H., Kakei, S., Saito, S., 2022. | Plug and analyze: Usable |  |  |  |  |
| [11] | Chan, J.T., Yang, W., 2004. Advanced obfuscation techniques for java | dynamic taint tracker for android apps. 2022 IEEE 22nd International |  |  |  |  |  |  |  |
| bytecode. J. Syst. Softw. 71, 1–10. | Working Conference on Source Code Analysis and Manipulation |  |  |  |  |  |  |  |  |
| [12] | Conti, M., Vinod, P., Vitella, A., 2022. | Obfuscation detection in | (SCAM) , 24–34URL: | https://api.semanticscholar.org/CorpusID: |  |  |  |  |  |
| android applications using deep learning. | J. Inf. Secur. Appl. 70, | 255777043 | . |  |  |  |  |  |  |
| 103311. | [31] | Jang, D., Jeong, Y., Lee, S., Park, M., Kwak, K., Kim, D., Kang, B.B., |  |  |  |  |  |  |  |
| [13] | Daoudi, N., Allix, K., Bissyandé, T.F., Klein, J., 2022. Assessing the | 2019. Rethinking anti-emulation techniques for large-scale software |  |  |  |  |  |  |  |
| opportunity of combining state-of-the-art android malware detectors. | deployment. Comput. Secur. 83, 182–200. |  |  |  |  |  |  |  |  |
| Empirical Software Engineering 28. | [32] | Li, L., Bartel, A., Bissyandé, T.F., Klein, J., Le Traon, Y., Arzt, S., |  |  |  |  |  |  |  |
| [14] | DFPP, 2024. | Ara study framework. | https://github.com/dfpp/ | Rasthofer, S., Bodden, E., Octeau, D., McDaniel, P., 2015. | Iccta: |  |  |  |  |
| Anti-ARA | . | Detecting inter-component privacy leaks in android apps, in: 2015 |  |  |  |  |  |  |  |
| [15] | DIALDroid, | 2025. | DIALDroid: | A | static | analysis | tool | for | IEEE/ACM 37th IEEE International Conference on Software Engi- |
| android | inter-component | communication. | https://github.com/ | neering, IEEE. pp. 280–291. |  |  |  |  |  |
| dialdroid-android/DIALDroid | . Accessed: 2025-06-05. | [33] | Li, L., Bissyandé, T.F., Klein, J., 2018. | Rebooting research on |  |  |  |  |  |
| [16] | Gao, C., Huang, G., Li, H., Wu, B., Wu, Y., Yuan, W., 2024. | A | detecting repackaged android apps: Literature review and benchmark. |  |  |  |  |  |  |
| comprehensive study of learning-based android malware detectors un- | IEEE Transactions on Software Engineering 47, 676–693. |  |  |  |  |  |  |  |  |
| der challenging environments, in: International Conference on Soft- | [34] | Liang, S., Bracha, G., 1998. Dynamic class loading in the java [tm] |  |  |  |  |  |  |  |
| ware Engineering. URL: | https://api.semanticscholar.org/CorpusID: | virtual machine. ACM SIGPLAN Notices 33, 36–44. |  |  |  |  |  |  |  |
| 267523865 | . | [35] | Lita, C.V., Cosovan, D., Gavrilut, D., 2018. | Anti-emulation trends |  |  |  |  |  |
| [17] | GOOGLE, 2013. | Apimonitor. | https://code.google.com/archive/p/ | in modern packers: a survey on the evolution of anti-emulation |  |  |  |  |  |
| droidbox/wikis/APIMonitor.wiki | . | techniques in upa packers. Journal of Computer Virology and Hacking |  |  |  |  |  |  |  |
| [18] | GOOGLE, 2025. | Monkey. | https://developer.android.google.cn/ | Techniques 14, 107–126. |  |  |  |  |  |

studio/test/other-testing-tools/monkey .

Suo et al.: Preprint submitted to Elsevier Page 17 of 18

---

## Page 18

| [36] | Lv, Z., Peng, C., Zhang, Z., Su, T., Liu, K., Yang, P., 2022. Fastbot2: | abs/2312.17356. | URL: | https://doi.org/10.48550/arXiv.2312.17356 | , |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Reusable automated model-based GUI testing for android enhanced | doi: | 10.48550/ARXIV.2312.17356 | , | arXiv:2312.17356 | . |  |  |
| by reinforcement learning, in: 37th IEEE/ACM International Confer- | [55] | Suo, D., Xue, L., Yu, L., Tan, R., Huang, W., Sun, G., 5555. |  |  |  |  |  |
| ence on Automated Software Engineering, ASE 2022, Rochester, MI, | ARAP: Demystifying Anti Runtime Analysis Code in Android Apps |  |  |  |  |  |  |
| USA, October 10-14, 2022, ACM. pp. 135:1–135:5. | URL: | https: | . IEEE Transactions on Software Engineering , 1–16URL: | https:// |  |  |  |
| //doi.org/10.1145/3551349.3559505 | , doi: | 10.1145/3551349.3559505 | . | doi.ieeecomputersociety.org/10.1109/TSE.2025.3596016 | , doi: | 10.1109/ |  |
| [37] | Muzaffar, A., Hassen, H.R., Zantout, H., Lones, M.A., 2023. Droid- | TSE.2025.3596016 | . |  |  |  |  |
| dissector: A static and dynamic analysis tool for android malware de- | [56] | Tam, K., Feizollah, A., Anuar, N.B., Salleh, R.B., Cavallaro, L., 2017. |  |  |  |  |  |
| tection. ArXiv abs/2308.04170. URL: | https://api.semanticscholar. | The evolution of android malware and android analysis techniques. |  |  |  |  |  |
| org/CorpusID:260704315 | . | ACM Computing Surveys (CSUR) 49, 1 – 41. |  |  |  |  |  |
| [38] | Nawaz, U., Aleem, M., Lin, C.W., 2022a. On the evaluation of android | [57] | Tang, J., Li, R., Jiang, Y., Gu, X., Li, Y., 2021. | Android malware |  |  |  |
| malware detectors against code-obfuscation techniques. PeerJ Com- | obfuscation variants detection method based on multi-granularity |  |  |  |  |  |  |
| puter Science 8. | URL: | https://api.semanticscholar.org/CorpusID: | opcode features. Future Gener. Comput. Syst. 129, 141–151. |  |  |  |  |
| 249932710 | . | [58] | Tang, Z., Zhai, J., Pan, M., Aafer, Y., Ma, S., Zhang, X., Zhao, |  |  |  |  |
| [39] | Nawaz, U., Aleem, M., Lin, J.C., 2022b. | On the evaluation of | J., 2018. | Dual-force: Understanding webview malware via cross- |  |  |  |
| android malware detectors against code-obfuscation techniques. PeerJ | language forced execution. 2018 33rd IEEE/ACM International Con- |  |  |  |  |  |  |
| Comput. Sci. 8, e1002. | URL: | https://doi.org/10.7717/peerj-cs. | ference on Automated Software Engineering (ASE) , 714–725URL: |  |  |  |  |
| 1002 | , doi: | 10.7717/PEERJ-CS.1002 | . | https://api.semanticscholar.org/CorpusID:52068854 | . |  |  |
| [40] | Nellaivadivelu, G., Troia, F.D., Stamp, M., 2020. Black box analysis | [59] | Wan, J., Zulkernine, M., Liem, C., 2018. | A dynamic app anti- |  |  |  |
| of android malware detectors. Array 6, 100022. URL: | https://api. | debugging approach on android art runtime. | 2018 IEEE 16th Intl |  |  |  |  |
| semanticscholar.org/CorpusID:215765442 | . | Conf on Dependable, Autonomic and Secure Computing, 16th Intl |  |  |  |  |  |
| [41] | Nguyen-Vu, L., Chau, N.T., Kang, S., Jung, S., 2017. Android rooting: | Conf on Pervasive Intelligence and Computing, 4th Intl Conf on Big |  |  |  |  |  |
| An arms race between evasion and detection. | Secur. Commun. | Data Intelligence and Computing and Cyber Science and Technology |  |  |  |  |  |
| Networks 2017, 4121765:1–4121765:13. | Congress(DASC/PiCom/DataCom/CyberSciTech) , 560–567. |  |  |  |  |  |  |
| [42] | oleavr, 2024. Frida. [Online] | https://github.com/frida/frida | . | [60] | Wang, X., Yang, Y., Zhu, S., 2019. | Automated hybrid analysis of |  |
| [43] | Pauck, F., Bodden, E., Wehrheim, H., 2018. Do android taint analysis | android malware through augmenting fuzzing with forced execution. |  |  |  |  |  |
| tools keep their promises?, in: Leavens, G.T., Garcia, A., Pasare- | IEEE Transactions on Mobile Computing 18, 2768–2782. | URL: |  |  |  |  |  |
| anu, C.S. (Eds.), Proceedings of the 2018 ACM Joint Meeting on | https://api.semanticscholar.org/CorpusID:69821821 | . |  |  |  |  |  |
| European Software Engineering Conference and Symposium on the | [61] | Wang, X., Zhu, S., Zhou, D., Yang, Y., 2017. Droid-antirm: Taming |  |  |  |  |  |
| Foundations of Software Engineering, ESEC/SIGSOFT FSE 2018, | control flow anti-analysis to support automated dynamic analysis of |  |  |  |  |  |  |
| Lake Buena Vista, FL, USA, November 04-09, 2018, ACM. pp. 331– | android malware. | Proceedings of the 33rd Annual Computer Se- |  |  |  |  |  |
| 341. | URL: | https://doi.org/10.1145/3236024.3236029 | , doi: | 10.1145/ | curity Applications Conference URL: | https://api.semanticscholar. |  |
| 3236024.3236029 | . | org/CorpusID:24391129 | . |  |  |  |  |
| [44] | Pilgun, A., Gadyatskaya, O., Zhauniarovich, Y., Dashevskyi, S., | [62] | Wei, F., Roy, S., Ou, X., Robby, 2018. | Amandroid: A precise and |  |  |  |
| Kushniarou, A., Mauw, S., 2020. Fine-grained code coverage mea- | general inter-component data flow analysis framework for security |  |  |  |  |  |  |
| surement in automated black-box android testing. ACM Transactions | vetting of android apps. ACM Transactions on Privacy and Security |  |  |  |  |  |  |
| on Software Engineering and Methodology (TOSEM) 29, 1–35. | (TOPS) 21, 1–32. |  |  |  |  |  |  |
| [45] | Ranganath, V., Mitra, J., 2020. Are free android app security analysis | [63] | Win, H.M., Tan, S.H., Sui, Y., 2023. | Event-aware precise dy- |  |  |  |
| tools effective in detecting known vulnerabilities? Empir. Softw. Eng. | namic slicing for automatic debugging of android applications. | J. |  |  |  |  |  |
| 25, 178–219. | URL: | https://doi.org/10.1007/s10664-019-09749-y | , | Syst. Softw. 198, 111606. | URL: | https://api.semanticscholar.org/ |  |
| doi: | 10.1007/S10664-019-09749-Y | . | CorpusID:249166776 | . |  |  |  |
| [46] | rovo89, 2017. | Xposed framework. | [Online] | https://github.com/ | [64] | Wu, T., Deng, X., Yan, J., Zhang, J., 2019. | Analyses for specific |
| rovo89/Xposed | . | defects in android applications: a survey. | Frontiers of Computer |  |  |  |  |
| [47] | Ruggia, A., Losiouk, E., Verderame, L., Conti, M., Merlo, A., 2021. | Science 13, 1210 – 1227. | URL: | https://api.semanticscholar.org/ |  |  |  |
| Repack me if you can: An anti-repackaging solution based on android | CorpusID:58953676 | . |  |  |  |  |  |
| virtualization. Annual Computer Security Applications Conference . | [65] | Xie, Z., Wen, M., Jia, H., Guo, X., Huang, X., Zou, D., Jin, H., |  |  |  |  |  |
| [48] | Ruggia, A., Nisi, D., Dambra, S., Merlo, A., Balzarotti, D., Aonzo, S., | 2023. Precise and efficient patch presence test for android applications |  |  |  |  |  |
| 2024. Unmasking the Veiled: A Comprehensive Analysis of Android | against code obfuscation. Proceedings of the 32nd ACM SIGSOFT |  |  |  |  |  |  |
| Evasive Malware, in: ASIAACS 2024, 19th ACM ASIA Conference | International Symposium on Software Testing and Analysis . |  |  |  |  |  |  |
| on Computer and Communications Security, ACM, Singapore, Sin- | [66] | Xu, F., Shen, S., Diao, W., Li, Z., Chen, Y., Li, R., Zhang, K., |  |  |  |  |  |
| gapore. URL: | https://hal.science/hal-04378941 | . | 2021. Android on pc: On the security of end-user android emulators. |  |  |  |  |
| [49] | Sahin, O., Coskun, A.K., Egele, M., 2018. | Proteus: Detecting | Proceedings of the 2021 ACM SIGSAC Conference on Computer and |  |  |  |  |
| android emulators from instruction-level profiles, in: International | Communications Security . |  |  |  |  |  |  |
| Symposium on Recent Advances in Intrusion Detection. | [67] | Yang, S.Z., Hou, Q., Li, S., Xu, F., Diao, W., 2024. From guidelines to |  |  |  |  |  |
| [50] | Shen, Y., Vervier, P.A., Stringhini, G., 2021. A large-scale temporal | practice: assessing android app developer compliance with google’s |  |  |  |  |  |
| measurement of android malicious apps: Persistence, migration, and | security recommendations. Empir. Softw. Eng. 30, 11. URL: | https: |  |  |  |  |  |
| lessons learned, in: USENIX Security Symposium. | //api.semanticscholar.org/CorpusID:273670059 | . |  |  |  |  |  |
| [51] | Sihag, V.K., Vardhan, M., Singh, P., 2021. | A survey of android | [68] | Zhang, J., Wang, Y., Qiu, L., Rubin, J., 2022. Analyzing android taint |  |  |  |
| application and malware hardening. Comput. Sci. Rev. 39, 100365. | analysis tools: Flowdroid, amandroid, and droidsafe. | IEEE Trans. |  |  |  |  |  |
| [52] | Software Engineering Institute, Carnegie Mellon University, 2025. | Software Eng. 48, 4014–4040. URL: | https://doi.org/10.1109/TSE. |  |  |  |  |
| DidFail: Data Flow Analysis for Android. | https://insights.sei.cmu. | 2021.3109563 | , doi: | 10.1109/TSE.2021.3109563 | . |  |  |

edu/library/didfail/ . Accessed: 2025-06-05.

[53] Soi, D., Maiorca, D., Giacinto, G., Berger, H., 2023a. Can you see me?

on the visibility of nops against android malware detectors. ArXiv

abs/2312.17356. URL: https://api.semanticscholar.org/CorpusID:

266690728 .

[54] Soi, D., Maiorca, D., Giacinto, G., Berger, H., 2023b. Can you see me?

on the visibility of nops against android malware detectors. CoRR

Suo et al.: Preprint submitted to Elsevier Page 18 of 18
